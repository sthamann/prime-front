#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kernel_redteam_probe -- PRIME.RDAGGER.KERNEL_LOEWNER_REDTEAM.01

Round 495, adversarial and independent of the r494 implementation.
Target: kill the asserted fixed-support floor

    Q_W(h) >= 2.1e-3 ||h||_2^2,  supp(h) subset [-0.3,0.3].

A1 derives and checks the x-space identity from the defining digamma
multiplier on five non-calibration polynomial tests.  A2 checks the
zero-extension translation identity exactly over Q on two step
functions and three shifts.  A3 doubles c_L and requires both an
explicit negative Rayleigh quotient and a negative certificate budget.
A4 recomputes the constants and finite section by Clenshaw--Curtis
Nyström quadrature, not the r494 Gauss--Legendre/Chebyshev route.
A5 resolves the old off-space question by decomposing the sampled
Hilbert--Schmidt residual into both off-blocks and the block-diagonal
rest beyond degree 400.

The independent Nyström numbers are diagnostics.  The adjudication
uses the outward r494 interval bounds after A1--A5 have tested every
premise.  Success means CONFIRMED(c=2.1e-3), not an RH claim.

NO RH CLAIM.  NO anti-RH claim.  NO ledger row.  No zero oracle.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
from scipy.integrate import quad_vec
from scipy.linalg import eigh
from scipy.special import eval_legendre, roots_legendre


L = mp.mpf("0.3")
SPAN = 2 * L
X0 = mp.mpf("0.01")
X1 = mp.mpf("0.03")
SECTION_N = 401
CLAIM_C = mp.mpf("0.0021")

R494_C_LO = mp.mpf("2.19240491113")
R494_C_HI = mp.mpf("2.19240491114")
R494_KAPPA_LO = mp.mpf("3.69800804029")
R494_KAPPA_HI = mp.mpf("3.69800804031")
R494_SECTION_UPPER = mp.mpf("1.5013673873")
R494_TAIL_UPPER = mp.mpf("7.0457565325e-4")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-34s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def polynomial_product(left, right):
    result = [mp.mpf("0")] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def test_polynomials():
    base = [mp.mpf("0")] * 17
    for index in range(9):
        base[2 * index] = mp.mpf(math.comb(8, index)) * (-1) ** index
    factors = (
        [1],
        [0, 1],
        [1, mp.mpf(7) / 10, -mp.mpf(2) / 5],
        [1, 0, -2, mp.mpf(3) / 10],
        [1, -mp.mpf(1) / 3, mp.mpf(1) / 5, -mp.mpf(1) / 7],
    )
    return [polynomial_product(base, factor) for factor in factors]


def x_coefficients(u_coefficients):
    return [coefficient / L**degree
            for degree, coefficient in enumerate(u_coefficients)]


def polynomial_value(coefficients, point):
    result = mp.mpf("0")
    for coefficient in reversed(coefficients):
        result = result * point + coefficient
    return result


def autocorrelation_coefficients(coefficients):
    """Polynomial g(x)=int_{-L+x}^L h(u)h(u-x)du, 0<=x<=2L."""
    degree = len(coefficients) - 1
    result = [mp.mpf("0")] * (2 * degree + 2)
    for i, coefficient_i in enumerate(coefficients):
        for j, coefficient_j in enumerate(coefficients):
            for k in range(j + 1):
                x_power = j - k
                u_power = i + k
                factor = (
                    coefficient_i * coefficient_j * math.comb(j, k)
                    * (-1) ** x_power / (u_power + 1)
                )
                result[x_power] += factor * L ** (u_power + 1)
                for r in range(u_power + 2):
                    result[x_power + r] -= (
                        factor * math.comb(u_power + 1, r)
                        * (-L) ** (u_power + 1 - r)
                    )
    while result and abs(result[-1]) < mp.mpf("1e-70"):
        result.pop()
    return result


def monomial_fourier(degree, frequency):
    """Integral x^degree exp(i frequency x) dx over [-L,L]."""
    if abs(frequency * L) < mp.mpf("0.4"):
        total = mp.mpc(0)
        exponential_term = mp.mpc(1)
        for index in range(300):
            power = degree + index
            moment = (
                L ** (power + 1) - (-L) ** (power + 1)
            ) / (power + 1)
            contribution = exponential_term * moment
            total += contribution
            if index > 30 and abs(contribution) < mp.mpf("1e-75"):
                break
            exponential_term *= 1j * frequency / (index + 1)
        return total
    imaginary_frequency = 1j * frequency
    exp_plus = mp.exp(1j * frequency * L)
    exp_minus = mp.exp(-1j * frequency * L)
    current = 2 * mp.sin(frequency * L) / frequency
    for current_degree in range(1, degree + 1):
        boundary = (
            L**current_degree * exp_plus
            - (-L)**current_degree * exp_minus
        )
        current = (
            boundary / imaginary_frequency
            - current_degree * current / imaginary_frequency
        )
    return current


def fourier_value(coefficients, frequency):
    return sum(
        coefficient * monomial_fourier(degree, frequency)
        for degree, coefficient in enumerate(coefficients)
    )


def kernel_mp(point):
    return mp.exp(point / 2) / mp.sinh(point)


def compute_c_l():
    return (
        mp.quad(lambda x: kernel_mp(x) - 1 / x, [0, SPAN])
        + mp.log(4 * L) + mp.euler + mp.log(mp.pi)
    )


def pole_term(coefficients):
    cosh_inner = mp.quad(
        lambda x: polynomial_value(coefficients, x) * mp.cosh(x / 2),
        [-L, L],
    )
    sinh_inner = mp.quad(
        lambda x: polynomial_value(coefficients, x) * mp.sinh(x / 2),
        [-L, L],
    )
    # H(i/2)H(-i/2), not |H(i/2)|^2.
    return 2 * (cosh_inner**2 - sinh_inner**2)


def x_side(coefficients, c_l):
    correlation = autocorrelation_coefficients(coefficients)
    g0 = polynomial_value(correlation, mp.mpf("0"))

    def integrand(point):
        if point == 0:
            return mp.mpf("0")
        return kernel_mp(point) * (
            g0 - polynomial_value(correlation, point)
        )

    arch = mp.quad(integrand, [0, mp.mpf(".02"), mp.mpf(".1"), SPAN])
    return arch - c_l * g0 + pole_term(coefficients), g0


def frequency_side(coefficients, cutoff):
    def integrand(frequency):
        sigma = (
            mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * frequency))
            - mp.log(mp.pi)
        )
        transform = fourier_value(coefficients, frequency)
        return sigma * abs(transform) ** 2 / mp.pi

    breakpoints = [
        mp.mpf(10) * index
        for index in range(int(cutoff / 10) + 1)
    ]
    return mp.quad(integrand, breakpoints) + pole_term(coefficients)


def attack_a1(smoke: bool):
    mp.mp.dps = 50 if smoke else 60
    c_l = compute_c_l()
    cutoff = mp.mpf(100 if smoke else 400)
    selected = test_polynomials()[:2 if smoke else 5]
    rows = []
    for index, u_coefficients in enumerate(selected, start=1):
        coefficients = x_coefficients(u_coefficients)
        q_x, norm = x_side(coefficients, c_l)
        q_frequency = frequency_side(coefficients, cutoff)
        rows.append({
            "index": index,
            "frequency": q_frequency / norm,
            "x": q_x / norm,
            "difference": (q_frequency - q_x) / norm,
        })
    mp.mp.dps = 80
    c_l_80 = compute_c_l()
    return c_l, c_l_80, rows


def step_value(steps, point):
    for left, right, value in steps:
        if left <= point < right:
            return value
    return Fraction(0)


def step_difference_norm(steps, shift, restriction=None):
    endpoints = set()
    for left, right, _ in steps:
        endpoints.update((left, right, left - shift, right - shift))
    total = Fraction(0)
    ordered = sorted(endpoints)
    for left, right in zip(ordered, ordered[1:]):
        segment_left = left if restriction is None else max(
            left, restriction[0])
        segment_right = right if restriction is None else min(
            right, restriction[1])
        if segment_right <= segment_left:
            continue
        midpoint = (segment_left + segment_right) / 2
        difference = (
            step_value(steps, midpoint)
            - step_value(steps, midpoint + shift)
        )
        total += (segment_right - segment_left) * difference**2
    return total


def step_correlation(steps, shift):
    total = Fraction(0)
    for left_i, right_i, value_i in steps:
        for left_j, right_j, value_j in steps:
            overlap_left = max(left_i, left_j - shift)
            overlap_right = min(right_i, right_j - shift)
            if overlap_right > overlap_left:
                total += (
                    value_i * value_j * (overlap_right - overlap_left)
                )
    return total


def attack_a2():
    ell = Fraction(3, 10)
    examples = (
        (
            (-ell, Fraction(-1, 10), Fraction(2)),
            (Fraction(-1, 10), Fraction(1, 10), Fraction(-1)),
            (Fraction(1, 10), ell, Fraction(3)),
        ),
        (
            (-ell, Fraction(0), Fraction(-2)),
            (Fraction(0), ell, Fraction(5, 2)),
        ),
    )
    rows = []
    for example_index, steps in enumerate(examples, start=1):
        g0 = step_correlation(steps, Fraction(0))
        for shift in (Fraction(1, 20), Fraction(1, 10), Fraction(1, 4)):
            correlation_side = 2 * (
                g0 - step_correlation(steps, shift)
            )
            whole_line = step_difference_norm(steps, shift)
            interval_only = step_difference_norm(
                steps, shift, (-ell, ell))
            rows.append({
                "example": example_index,
                "shift": shift,
                "correlation": correlation_side,
                "whole": whole_line,
                "interval": interval_only,
                "boundary": whole_line - interval_only,
            })
    return rows


def ramp_float(points):
    values = np.asarray(points, dtype=float)
    result = np.zeros_like(values)
    result[values >= 0.03] = 1.0
    transition = (values > 0.01) & (values < 0.03)
    t = (values[transition] - 0.01) / 0.02
    result[transition] = 6 * t**5 - 15 * t**4 + 10 * t**3
    return result


def weighted_kernel_float(distances):
    result = np.zeros_like(distances)
    positive = distances > 0.01
    points = distances[positive]
    result[positive] = (
        ramp_float(points) * np.exp(points / 2) / np.sinh(points)
    )
    return result


def clenshaw_curtis(order):
    degree = order - 1
    theta = np.pi * np.arange(order) / degree
    nodes = np.cos(theta)
    weights = np.zeros(order)
    interior = np.arange(1, degree)
    values = np.ones(degree - 1)
    if degree % 2 == 0:
        weights[0] = weights[degree] = 1 / (degree**2 - 1)
        for index in range(1, degree // 2):
            values -= (
                2 * np.cos(2 * index * theta[interior])
                / (4 * index**2 - 1)
            )
        values -= (
            np.cos(degree * theta[interior]) / (degree**2 - 1)
        )
    else:
        weights[0] = weights[degree] = 1 / degree**2
        for index in range(1, (degree + 1) // 2):
            values -= (
                2 * np.cos(2 * index * theta[interior])
                / (4 * index**2 - 1)
            )
    weights[interior] = 2 * values / degree
    return 0.3 * nodes, 0.3 * weights


def legendre_table(points, dimension):
    scaled = points / 0.3
    result = np.empty((len(points), dimension))
    for degree in range(dimension):
        result[:, degree] = (
            math.sqrt((2 * degree + 1) / 0.6)
            * eval_legendre(degree, scaled)
        )
    return result


def nystrom_and_hs(order):
    points, weights = clenshaw_curtis(order)
    sqrt_weights = np.sqrt(weights)
    distances = np.abs(points[:, None] - points[None, :])
    t_matrix = (
        0.5 * sqrt_weights[:, None]
        * weighted_kernel_float(distances)
        * sqrt_weights[None, :]
    )
    cosh_vector = sqrt_weights * np.cosh(points / 2)
    sinh_vector = sqrt_weights * np.sinh(points / 2)
    s_matrix = (
        t_matrix
        - 2 * np.outer(cosh_vector, cosh_vector)
        + 2 * np.outer(sinh_vector, sinh_vector)
    )
    operator_lambda = float(eigh(
        s_matrix,
        subset_by_index=[order - 1, order - 1],
        eigvals_only=True,
        check_finite=False,
    )[0])

    sampled_basis = (
        sqrt_weights[:, None] * legendre_table(points, SECTION_N)
    )
    gram_error = float(np.linalg.norm(
        sampled_basis.T @ sampled_basis - np.eye(SECTION_N), ord=2))
    orthonormal_basis, _ = np.linalg.qr(sampled_basis, mode="reduced")
    t_times_basis = t_matrix @ orthonormal_basis
    projected_t = orthonormal_basis.T @ t_times_basis
    projected_cosh = orthonormal_basis.T @ cosh_vector
    projected_sinh = orthonormal_basis.T @ sinh_vector
    section_s = (
        projected_t
        - 2 * np.outer(projected_cosh, projected_cosh)
        + 2 * np.outer(projected_sinh, projected_sinh)
    )
    section_lambda = float(eigh(
        section_s,
        subset_by_index=[SECTION_N - 1, SECTION_N - 1],
        eigvals_only=True,
        check_finite=False,
    )[0])

    total_hs_square = float(np.linalg.norm(t_matrix, "fro") ** 2)
    projected_hs_square = float(np.linalg.norm(projected_t, "fro") ** 2)
    off_hs_square = max(
        float(np.linalg.norm(t_times_basis, "fro") ** 2)
        - projected_hs_square,
        0.0,
    )
    diagonal_rest_square = max(
        total_hs_square - projected_hs_square - 2 * off_hs_square,
        0.0,
    )
    aggregate_tail = math.sqrt(max(
        total_hs_square - projected_hs_square, 0.0))
    return {
        "order": order,
        "operator_lambda": operator_lambda,
        "section_lambda": section_lambda,
        "gram_error": gram_error,
        "aggregate_tail": aggregate_tail,
        "off_hs": math.sqrt(off_hs_square),
        "diagonal_rest_hs": math.sqrt(diagonal_rest_square),
    }


def uncut_even_section(c_l):
    dimension = 37
    inner_nodes, inner_weights = roots_legendre(60)
    identity = np.eye(dimension)

    def matrix_integrand(square_root_x):
        if square_root_x == 0:
            return np.zeros((dimension, dimension))
        x = square_root_x**2
        overlap_length = 0.6 - x
        y = -0.3 + 0.5 * overlap_length * (inner_nodes + 1)
        y_weights = 0.5 * overlap_length * inner_weights
        base = legendre_table(y, dimension)
        shifted = legendre_table(y + x, dimension)
        overlap = shifted.T @ (y_weights[:, None] * base)
        difference = identity - 0.5 * (overlap + overlap.T)
        return (
            2 * square_root_x * math.exp(x / 2) / math.sinh(x)
        ) * difference

    difference_form, _ = quad_vec(
        matrix_integrand,
        0,
        math.sqrt(0.6),
        epsabs=2e-11,
        epsrel=2e-11,
    )
    nodes, weights = clenshaw_curtis(257)
    basis = legendre_table(nodes, dimension)
    cosh_vector = basis.T @ (weights * np.cosh(nodes / 2))
    sinh_vector = basis.T @ (weights * np.sinh(nodes / 2))
    q_matrix = (
        difference_form - float(c_l) * identity
        + 2 * np.outer(cosh_vector, cosh_vector)
        - 2 * np.outer(sinh_vector, sinh_vector)
    )
    return float(np.linalg.eigvalsh(q_matrix[::2, ::2])[0])


def attack_a3_a4_a5(smoke: bool, c_l):
    mp.mp.dps = 70

    def weight(point):
        if point <= X0:
            return mp.mpf("0")
        if point >= X1:
            return mp.mpf("1")
        t = (point - X0) / (X1 - X0)
        return 6 * t**5 - 15 * t**4 + 10 * t**3

    kappa = mp.quad(
        lambda x: weight(x) * kernel_mp(x), [X0, X1, SPAN])
    orders = (513, 769) if smoke else (513, 769, 1025)
    numerical = [nystrom_and_hs(order) for order in orders]
    best = numerical[-1]
    uncut_even = uncut_even_section(c_l)
    finite_target = float(kappa - c_l) - best["section_lambda"]
    return {
        "kappa": kappa,
        "numerical": numerical,
        "uncut_even": uncut_even,
        "finite_target": finite_target,
        "cutoff_loss": uncut_even - finite_target,
        "doubled_c_budget": (
            float(kappa - 2 * c_l) - best["operator_lambda"]
        ),
        "r494_floor": (
            R494_KAPPA_LO - R494_C_HI - R494_SECTION_UPPER
            - 3 * R494_TAIL_UPPER
        ),
    }


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("kernel_redteam_probe -- r495")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")

    section("A1  INDEPENDENT DIGAMMA / X-SPACE IDENTITY")
    c_l, c_l_80, a1_rows = attack_a1(smoke)
    a1_tolerance = mp.mpf("1e-8" if smoke else "1e-15")
    max_cross_error = max(abs(row["difference"]) for row in a1_rows)
    check(
        "A1-cL-and-dps",
        R494_C_LO <= c_l <= R494_C_HI
        and abs(c_l - c_l_80) < mp.mpf("1e-48"),
        "cL=%s; |dps50/80|=%.2e" % (
            mp.nstr(c_l, 20), float(abs(c_l - c_l_80))),
    )
    check(
        "A1-five-cross-tests" if not smoke else "A1-smoke-cross-tests",
        max_cross_error < a1_tolerance,
        "count=%d max |Qf-Qx|/||h||2=%.3e" % (
            len(a1_rows), float(max_cross_error)),
    )
    for row in a1_rows:
        print(
            "  A1 h%d  Qfreq/norm=%s  Qx/norm=%s  delta=%+.3e"
            % (
                row["index"],
                mp.nstr(row["frequency"], 17),
                mp.nstr(row["x"], 17),
                float(row["difference"]),
            )
        )

    section("A2  EXACT ZERO-EXTENSION BOUNDARY STRIPS")
    a2_rows = attack_a2()
    check(
        "A2-rational-translation",
        all(row["correlation"] == row["whole"] for row in a2_rows),
        "6/6 exact over Q",
    )
    check(
        "A2-boundary-not-dropped",
        all(row["boundary"] > 0 for row in a2_rows),
        "boundary masses %s" % sorted({
            str(row["boundary"]) for row in a2_rows
        }),
    )
    for row in a2_rows:
        print(
            "  A2 step%d x=%s: 2(g0-gx)=%s whole=%s interval=%s strip=%s"
            % (
                row["example"], row["shift"], row["correlation"],
                row["whole"], row["interval"], row["boundary"],
            )
        )

    section("A3--A5  FALSE WORLD / NUMBERS / OPERATOR CLASS")
    analysis = attack_a3_a4_a5(smoke, c_l)
    best = analysis["numerical"][-1]
    control_rayleigh = a1_rows[0]["x"] - c_l
    check(
        "A3-negative-control-functional",
        control_rayleigh < -1 and analysis["doubled_c_budget"] < -2,
        "Rayleigh=%.6f chain-budget=%.6f" % (
            float(control_rayleigh), analysis["doubled_c_budget"]),
    )
    check(
        "A4-kappa-independent",
        abs(analysis["kappa"] - mp.mpf("3.6980080402989774465"))
        < mp.mpf("1e-18"),
        mp.nstr(analysis["kappa"], 22),
    )
    check(
        "A4-section-independent",
        abs(best["section_lambda"] - 1.5013657) < 5e-6,
        "CC%d lambda=%.15f" % (
            best["order"], best["section_lambda"]),
    )
    check(
        "A4-cutoff-loss",
        abs(analysis["cutoff_loss"] - 0.0033345) < 3e-6,
        "uncut=%.13e loss=%.13e" % (
            analysis["uncut_even"], analysis["cutoff_loss"]),
    )
    check(
        "A5-HS-tail-convergence",
        5.5e-4 < best["aggregate_tail"] < 7.0e-4,
        "r401=%.10e" % best["aggregate_tail"],
    )
    check(
        "A5-diagonal-rest-present",
        best["off_hs"] > 1e-4
        and best["diagonal_rest_hs"] > 5e-4
        and (
            2 * best["off_hs"] + best["diagonal_rest_hs"]
            < 3 * R494_TAIL_UPPER
        ),
        "off=%.3e QQ=%.3e direct-charge=%.3e < 3r=%.3e" % (
            best["off_hs"],
            best["diagonal_rest_hs"],
            2 * best["off_hs"] + best["diagonal_rest_hs"],
            float(3 * R494_TAIL_UPPER),
        ),
    )
    check(
        "A5-final-outward-floor",
        analysis["r494_floor"] >= CLAIM_C,
        "%s >= %s" % (
            mp.nstr(analysis["r494_floor"], 14),
            mp.nstr(CLAIM_C, 8),
        ),
    )

    for row in analysis["numerical"]:
        print(
            "  CC%-4d lambda_op=%.15f lambda_401=%.15f "
            "r401=%.10e off=%.10e QQ=%.10e Gram=%.3e"
            % (
                row["order"], row["operator_lambda"],
                row["section_lambda"], row["aggregate_tail"],
                row["off_hs"], row["diagonal_rest_hs"],
                row["gram_error"],
            )
        )
    print("  kappa_w                 ", mp.nstr(analysis["kappa"], 24))
    print("  uncut even N=36         %.15e" % analysis["uncut_even"])
    print("  independent cutoff loss %.15e" % analysis["cutoff_loss"])
    print("  false-world chain       %.15e" % analysis["doubled_c_budget"])
    print("  outward r494 floor      ", mp.nstr(analysis["r494_floor"], 18))

    failures = [name for name, passed in CHECKS if not passed]
    elapsed = time.perf_counter() - started
    print("\nCHECKS %d/%d elapsed %.2fs" % (
        len(CHECKS) - len(failures), len(CHECKS), elapsed))
    if failures:
        print("VERDICT KILLED_OR_WEAKENED(" + ",".join(failures) + ")")
        return 1
    print("VERDICT CONFIRMED(c=2.1000e-3)")
    print("SPEC_SHA", SPEC_SHA)
    print("KERNEL LOEWNER REDTEAM -- CONFIRMED(c=2.1000e-3)")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
