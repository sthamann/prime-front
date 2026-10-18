#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kernel_loewner08_probe -- PRIME.RDAGGER.KERNEL_LOEWNER.02

Round 496, experiments-side.  This is the final r492-budget scaling test
of the r494 kernel/Loewner method at L=0.8.  Here 2L=1.6 and the exact
prime-power set is {2,3,4}.  The classical normalization is

  P(h) = 2 sum_n Lambda(n)/sqrt(n) g(log n).

Thus

  -P = -2 sum_n a_n g(0) + 2 sum_n a_n (I-Re tau_log(n)),

with every translation and norm taken after zero-extension to L2(R).
The factor two is forced by the r471 and r477 calibration stops.

G1 seals the identity by five dps-50 frequency/x-space cross-tests, the
r495-A2 rational staircase convention, and independent r471/r477 values.
After G1 the probe never evaluates the frequency symbol again.

G2 books c_L, the full prime g(0)-mass, and four quintic-C2 cutoff
families.  Even the most aggressive tested cutoff [0.001,0.003] has a
negative 101-dimensional finite-section margin.  By Cauchy interlacing,
no containing section through n=800 can turn that margin positive.

G3 records the exact archimedean Hilbert--Schmidt tail with the full
three-piece charge.  It also exposes the structural prime obstruction:
compressed translations have delta-line kernels and are bounded but not
Hilbert--Schmidt.  Their measured 101-to-301 Legendre off-block norm is
at least 0.9394, so treating their finite section as the operator would
be the forbidden Galerkin pad.  The r494 compact-kernel completion does
not scale to L=0.8 under the binding contract.

Verdict: NO_GO(kernel-Loewner-compact-tail@L=0.8).
This is a method no-go, not an anti-positivity result.  No RH claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys

import mpmath as mp
import numpy as np
from scipy.linalg import svdvals
from scipy.special import roots_legendre

import classical_cert_probe as classical
import highmode_probe as highmode
import kernel_redteam_probe as redteam

L = 0.8
TWO_L = 1.6
SECTION_N = 101
MAX_ALLOWED_N = 800
FREQUENCY_CUTOFF = 100.0
VERDICT_KIND = "NO_GO(kernel-Loewner-compact-tail@L=0.8)"

PRIME_DATA = (
    (2, math.log(2.0), math.log(2.0) / math.sqrt(2.0)),
    (3, math.log(3.0), math.log(3.0) / math.sqrt(3.0)),
    (4, math.log(4.0), math.log(2.0) / 2.0),
)
CUTOFFS = (
    (0.001, 0.003),
    (0.002, 0.006),
    (0.003, 0.010),
    (0.010, 0.030),
)

C_L_HULL = (3.55987357003554, 3.55987357003555)
PRIME_MASS_HULL = (2.94197352522361, 2.94197352522363)
R471_MU_HULL = (1.3221e-4, 1.3240e-4)
R477_CONST_HULL = (8.0274e-2, 8.0275e-2)
R477_SCHUR_HULL = (7.4138e-2, 7.5074e-2)
BEST_SECTION_HULL = (-1.62e-4, -1.60e-4)
BEST_HS3_HULL = (27.36, 27.38)
PRIME_OFFBLOCK_FLOOR = 0.939
FREQUENCY_AGREEMENT_TOLERANCE = mp.mpf("5e-13")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-40s %s" % (
        "PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    banned = {
        "zetazero", "nzeros", "grampoint", "primepi",
        "nextprime", "prevprime",
    }
    bad = []
    for node in ast.walk(tree):
        name = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if name and name.lower().replace("_", "") in banned:
            bad.append("%s@%d" % (name, node.lineno))
    return not bad, "clean" if not bad else ", ".join(bad)


def kernel_mp(point):
    return mp.exp(point / 2) / mp.sinh(point)


def high_precision_constants():
    mp.mp.dps = 70
    ell = mp.mpf("0.8")
    span = 2 * ell
    c_l = (
        mp.quad(lambda x: kernel_mp(x) - 1 / x, [0, span])
        + mp.log(4 * ell) + mp.euler + mp.log(mp.pi)
    )
    prime_weights = (
        mp.log(2) / mp.sqrt(2),
        mp.log(3) / mp.sqrt(3),
        mp.log(2) / 2,
    )
    return c_l, prime_weights, 2 * sum(prime_weights)


def polynomial_x_values():
    redteam.L = mp.mpf("0.8")
    redteam.SPAN = mp.mpf("1.6")
    c_l = redteam.compute_c_l()
    weights = (
        (mp.log(2), mp.log(2) / mp.sqrt(2)),
        (mp.log(3), mp.log(3) / mp.sqrt(3)),
        (mp.log(4), mp.log(2) / 2),
    )
    rows = []
    coefficient_rows = []
    for u_coefficients in redteam.test_polynomials():
        coefficients = redteam.x_coefficients(u_coefficients)
        correlation = redteam.autocorrelation_coefficients(coefficients)
        g0 = redteam.polynomial_value(correlation, mp.mpf(0))
        arch = mp.quad(
            lambda x: kernel_mp(x) * (
                g0 - redteam.polynomial_value(correlation, x)
            ),
            [0, mp.mpf(".02"), mp.mpf(".1"), mp.mpf(".4"),
             mp.mpf(".8"), mp.mpf("1.6")],
        )
        prime = 2 * sum(
            weight * redteam.polynomial_value(correlation, shift)
            for shift, weight in weights
        )
        q_x = arch - c_l * g0 + redteam.pole_term(coefficients) - prime
        rows.append((q_x, g0))
        coefficient_rows.append(coefficients)
    return rows, coefficient_rows


def frequency_cross_tests(order: int):
    """Shared fixed Gauss rule; every value is evaluated at mp.dps=50."""
    mp.mp.dps = 50
    x_rows, coefficient_rows = polynomial_x_values()
    nodes, weights_gl = roots_legendre(order)
    totals = [mp.mpf(0) for _ in coefficient_rows]
    for interval_index in range(int(FREQUENCY_CUTOFF / 10)):
        for node, weight_gl in zip(nodes, weights_gl):
            frequency = (
                mp.mpf(5) * (mp.mpf(str(node)) + 1)
                + 10 * interval_index
            )
            quadrature_weight = mp.mpf(5) * mp.mpf(str(weight_gl))
            sigma = (
                mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * frequency))
                - mp.log(mp.pi)
                - 2 * sum(
                    mp.mpf(str(weight)) * mp.cos(
                        frequency * mp.mpf(str(shift))
                    )
                    for _, shift, weight in PRIME_DATA
                )
            )
            for index, coefficients in enumerate(coefficient_rows):
                transform = redteam.fourier_value(coefficients, frequency)
                totals[index] += (
                    quadrature_weight * sigma * abs(transform) ** 2 / mp.pi
                )
    output = []
    for (q_x, g0), coefficients, integral in zip(
            x_rows, coefficient_rows, totals):
        q_frequency = integral + redteam.pole_term(coefficients)
        output.append({
            "x": q_x / g0,
            "frequency": q_frequency / g0,
            "difference": (q_frequency - q_x) / g0,
        })
    return output


def legacy_calibrations():
    classical.mp.mp.dps = classical.DPS
    classical.iv.dps = classical.DPS
    ell = classical.iv.mpf("0.8")
    delta = 2 * ell / 24
    rows = [
        row for row in classical.prime_powers_upto(12)
        if row[0] <= classical.n_max_for(ell)
    ]
    q_interval, _, _ = classical.assemble_Q(24, delta, rows)
    r471 = classical.certify_matrix(q_interval)
    r477 = highmode.gram_2x2(ell)
    r_const = highmode.CC.ivsplit(highmode.Q_constant(ell))
    schur = highmode.CC.ivsplit(r477["schur"])
    return r471, r_const, schur


def legendre_values(points, dimension: int):
    values_x = np.asarray(points, dtype=float)
    result = np.empty((values_x.size, dimension), dtype=float)
    result[:, 0] = 1.0 / math.sqrt(TWO_L)
    if dimension == 1:
        return result
    scaled = values_x / L
    previous = np.ones_like(scaled)
    current = scaled.copy()
    result[:, 1] = math.sqrt(3.0 / TWO_L) * current
    for degree in range(1, dimension - 1):
        following = (
            (2 * degree + 1) * scaled * current - degree * previous
        ) / (degree + 1)
        result[:, degree + 1] = (
            math.sqrt((2 * degree + 3) / TWO_L) * following
        )
        previous, current = current, following
    return result


def pole_vectors(dimension: int):
    nodes, weights = roots_legendre(max(dimension + 16, 100))
    points = L * nodes
    scaled_weights = L * weights
    values = legendre_values(points, dimension)
    return (
        values.T @ (scaled_weights * np.cosh(points / 2)),
        values.T @ (scaled_weights * np.sinh(points / 2)),
    )


def shift_matrix(shift: float, rows: int, columns: int | None = None):
    columns = columns or rows
    order = max(rows, columns) + 8
    nodes, weights = roots_legendre(order)
    overlap_length = TWO_L - shift
    points = -L + 0.5 * overlap_length * (nodes + 1)
    scaled_weights = 0.5 * overlap_length * weights
    forward = (
        legendre_values(points + shift, rows).T
        @ (scaled_weights[:, None] * legendre_values(points, columns))
    )
    backward = (
        legendre_values(points, rows).T
        @ (scaled_weights[:, None]
           * legendre_values(points + shift, columns))
    )
    return 0.5 * (forward + backward)


def ramp(points, x0: float, x1: float):
    values = np.asarray(points, dtype=float)
    output = np.zeros_like(values)
    output[values >= x1] = 1.0
    transition = (values > x0) & (values < x1)
    coordinate = (values[transition] - x0) / (x1 - x0)
    output[transition] = (
        6 * coordinate**5 - 15 * coordinate**4 + 10 * coordinate**3
    )
    return output


def archimedean_matrix(
        dimension: int, x0: float, x1: float, outer_order: int | None = None):
    inner_nodes, inner_weights = roots_legendre(dimension + 8)
    outer_order = outer_order or dimension + 80
    half_matrix = np.zeros((dimension, dimension))
    for left, right in ((x0, x1), (x1, TWO_L)):
        outer_nodes, outer_weights = roots_legendre(outer_order)
        distances = (
            0.5 * (right - left) * outer_nodes + 0.5 * (right + left)
        )
        distance_weights = 0.5 * (right - left) * outer_weights
        weighted_kernel = (
            ramp(distances, x0, x1)
            * np.exp(distances / 2) / np.sinh(distances)
        )
        for start in range(0, outer_order, 8):
            local_distances = distances[start:start + 8]
            overlap_lengths = TWO_L - local_distances
            points = (
                -L + 0.5 * overlap_lengths[:, None]
                * (inner_nodes[None, :] + 1)
            )
            point_weights = (
                0.5 * overlap_lengths[:, None] * inner_weights[None, :]
            )
            total_weights = (
                0.5 * distance_weights[start:start + 8, None]
                * weighted_kernel[start:start + 8, None] * point_weights
            )
            values = legendre_values(points.ravel(), dimension)
            shifted = legendre_values(
                (points + local_distances[:, None]).ravel(), dimension
            )
            half_matrix += (
                shifted.T @ (total_weights.ravel()[:, None] * values)
            )
    return half_matrix + half_matrix.T


def cutoff_constants(x0: float, x1: float):
    mp.mp.dps = 60
    lower = mp.mpf(str(x0))
    upper = mp.mpf(str(x1))

    def weight(point):
        if point <= lower:
            return mp.mpf(0)
        if point >= upper:
            return mp.mpf(1)
        coordinate = (point - lower) / (upper - lower)
        return 6 * coordinate**5 - 15 * coordinate**4 + 10 * coordinate**3

    kappa = mp.quad(
        lambda x: weight(x) * kernel_mp(x),
        [lower, upper, mp.mpf("1.6")],
    )
    hs_squared = mp.mpf("0.5") * mp.quad(
        lambda x: (
            (mp.mpf("1.6") - x) * (weight(x) * kernel_mp(x))**2
        ),
        [lower, upper, mp.mpf("1.6")],
    )
    return kappa, hs_squared


def cutoff_section(dimension: int, x0: float, x1: float, c_l: float):
    t_matrix = archimedean_matrix(dimension, x0, x1)
    cosh_vector, sinh_vector = pole_vectors(dimension)
    kappa, hs_squared = cutoff_constants(x0, x1)
    q_matrix = (float(kappa) - c_l) * np.eye(dimension) - t_matrix
    q_matrix += (
        2 * np.outer(cosh_vector, cosh_vector)
        - 2 * np.outer(sinh_vector, sinh_vector)
    )
    prime_matrix = np.zeros((dimension, dimension))
    for _, shift, weight in PRIME_DATA:
        prime_matrix += 2 * weight * shift_matrix(shift, dimension)
    q_matrix -= prime_matrix
    eigenvalues = np.linalg.eigvalsh(q_matrix)
    projected_hs_squared = float(np.sum(t_matrix * t_matrix))
    hs_tail = mp.sqrt(max(
        mp.mpf(0), hs_squared - mp.mpf(str(projected_hs_squared))
    ))
    return {
        "x0": x0,
        "x1": x1,
        "kappa": float(kappa),
        "mass_balance": float(kappa) - c_l - sum(
            2 * weight for _, _, weight in PRIME_DATA
        ),
        "lambda_min": float(eigenvalues[0]),
        "lambda_second": float(eigenvalues[1]),
        "hs_total": float(mp.sqrt(hs_squared)),
        "hs_tail": float(hs_tail),
        "hs_charge": float(3 * hs_tail),
    }


def prime_offblock(dimension: int, outer_dimension: int):
    total = np.zeros((outer_dimension, dimension))
    for _, shift, weight in PRIME_DATA:
        total += 2 * weight * shift_matrix(
            shift, outer_dimension, dimension
        )
    block = total[dimension:, :]
    return float(svdvals(block)[0]), float(np.linalg.norm(block))


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    print("kernel_loewner08_probe -- r496")
    print("SPEC_SHA", SPEC_SHA)
    print("mode", "SMOKE" if smoke else "FULL")
    print("verdict-kind", VERDICT_KIND)

    firewall_ok, firewall_detail = firewall_audit()
    check("firewall", firewall_ok, firewall_detail)

    section("G0  g(0) BALANCE -- REQUIRED FIRST")
    c_l, prime_weights, prime_mass = high_precision_constants()
    print("  c_L(0.8)        =", mp.nstr(c_l, 30))
    print("  prime weights   =", " ".join(
        mp.nstr(weight, 20) for weight in prime_weights))
    print("  prime g(0) mass =", mp.nstr(prime_mass, 30))
    check("c_L-interval", C_L_HULL[0] < c_l < C_L_HULL[1])
    check(
        "prime-mass-factor-two",
        PRIME_MASS_HULL[0] < prime_mass < PRIME_MASS_HULL[1],
        "2 sum Lambda(n)/sqrt(n), n=2,3,4",
    )

    section("G1  IDENTITY AND ZERO-EXTENSION CONVENTION")
    frequency_rows = frequency_cross_tests(48)
    for index, row in enumerate(frequency_rows, start=1):
        print(
            "  test%d x=%+.15e frequency=%+.15e diff=%+.3e" % (
                index, float(row["x"]), float(row["frequency"]),
                float(row["difference"]),
            )
        )
    check(
        "frequency-x-cross-5",
        len(frequency_rows) == 5 and all(
            abs(row["difference"]) < FREQUENCY_AGREEMENT_TOLERANCE
            for row in frequency_rows
        ),
        "dps=50, max |difference|=%.3e" % max(
            abs(float(row["difference"])) for row in frequency_rows
        ),
    )
    a2_rows = redteam.attack_a2()
    check(
        "r495-A2-zero-extension",
        len(a2_rows) == 6 and all(
            row["correlation"] == row["whole"] for row in a2_rows
        ),
        "6/6 rational staircase identities exact over Q",
    )
    r471, r_const, schur = legacy_calibrations()
    print(
        "  r471 n=24 hint=%.15e mu_lo=%.15e" % (
            r471["hint"], r471["mu"])
    )
    print(
        "  r477 r(1)=[%.15e,%.15e] Schur=[%.15e,%.15e]" % (
            float(r_const[0]), float(r_const[1]),
            float(schur[0]), float(schur[1]),
        )
    )
    check(
        "r471-L08-n24",
        r471["certified"]
        and R471_MU_HULL[0] < r471["mu"] < R471_MU_HULL[1],
        "GRID_CERTIFIED, factor-two prime normalization",
    )
    check(
        "r477-constant",
        R477_CONST_HULL[0] < float(r_const[0])
        < float(r_const[1]) < R477_CONST_HULL[1],
    )
    check(
        "r477-Schur",
        R477_SCHUR_HULL[0] < float(schur[0])
        < float(schur[1]) < R477_SCHUR_HULL[1],
    )
    print("  FREQUENCY GATE CLOSED: no later frequency evaluation")

    section("G2  BOOKED LOEWNER CUTOFF BUDGET")
    cutoff_rows = [
        cutoff_section(SECTION_N, x0, x1, float(c_l))
        for x0, x1 in CUTOFFS
    ]
    print(
        "  cutoff          kappa       mass balance   section lmin    3*HS tail"
    )
    for row in cutoff_rows:
        print(
            "  [%0.3f,%0.3f]  %10.7f  %+12.6e  %+12.6e  %11.6f" % (
                row["x0"], row["x1"], row["kappa"],
                row["mass_balance"], row["lambda_min"],
                row["hs_charge"],
            )
        )
    best = max(cutoff_rows, key=lambda row: row["lambda_min"])
    check(
        "best-section-negative",
        BEST_SECTION_HULL[0] < best["lambda_min"] < BEST_SECTION_HULL[1],
        "best=[%.3f,%.3f], lmin=%.9e" % (
            best["x0"], best["x1"], best["lambda_min"]),
    )
    check(
        "all-cutoff-losses-booked",
        all(math.isfinite(row["mass_balance"]) for row in cutoff_rows),
        "c_L + full prime g(0) mass + omitted integral",
    )
    check(
        "interlacing-to-n800",
        SECTION_N <= MAX_ALLOWED_N and best["lambda_min"] < 0,
        "a containing Legendre section cannot restore positive lmin",
    )

    section("G3  EXACT HS TAIL AND PRIME OFFBLOCK")
    prime_operator, prime_frobenius = prime_offblock(SECTION_N, 301)
    print(
        "  best arch HS: total=%.9f tail=%.9f full-3x=%.9f" % (
            best["hs_total"], best["hs_tail"], best["hs_charge"])
    )
    print(
        "  prime P_[101,301) R P_101: op=%.9f fro=%.9f" % (
            prime_operator, prime_frobenius)
    )
    check(
        "full-three-piece-HS-charge",
        BEST_HS3_HULL[0] < best["hs_charge"] < BEST_HS3_HULL[1],
        "not HS/3 and not central term alone",
    )
    check(
        "prime-offblock-nonvanishing",
        prime_operator > PRIME_OFFBLOCK_FLOOR,
        "bounded translation is not a compact HS kernel",
    )
    check(
        "G3-NO_GO",
        best["lambda_min"] <= 0
        and best["hs_charge"] > 0
        and prime_operator > 0,
        "no positive margin; remainder < margin/3 impossible at n<=800",
    )
    check(
        "no-Galerkin-as-operator",
        True,
        "finite prime section reported only as obstruction diagnostic",
    )

    section("VERDICT")
    failed = [name for name, ok in CHECKS if not ok]
    if failed:
        print("PROBE FAILURE:", ", ".join(failed))
        return 1
    print("VERDICT", VERDICT_KIND)
    print("G1 PASS; G2 NO_GO; G3 NO_GO")
    print("Method no-go only.  No RH claim.  No anti-RH claim.")
    print("ALL CHECKS PASSED (%d/%d)" % (len(CHECKS), len(CHECKS)))
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
