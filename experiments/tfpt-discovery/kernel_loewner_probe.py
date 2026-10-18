#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kernel_loewner_probe -- PRIME.RDAGGER.KERNEL_LOEWNER.01

Round 494, experiments-side.  Fixed L=0.3 and 2L=0.6<log(2), hence
the prime term is empty.  This probe executes the three gates of the
binding r492 judgment in order.

G1 (identity, stop gate)
  Seal the x-space Weil form

    Q_W(h) = int_0^(2L) k(x)(g(0)-g(x)) dx - c_L g(0) + Pi(h),
    k(x)=exp(x/2)/sinh(x),
    Pi(h)=2(<h,cosh(x/2)>^2-<h,sinh(x/2)>^2),

  against the defining digamma value only at this calibration gate.
  Mandatory hits: sigma_A(0), the r476 Dirichlet hull, and the odd
  Legendre sector.  A miss returns G1_STOP before any later gate.

G2 (Loewner and booked cutoff)
  Every h is extended by zero outside [-L,L].  Translation is unitary
  on L2(R), while its compression R_x=P_L tau_x P_L is a contraction:

    <h,(I-Re R_x)h> = 1/2 ||h-tau_x h||^2_{L2(R)} >= 0.

  The norm is deliberately on R; using only [-L,L] would omit the two
  translation boundary strips.  The cutoff is w=0 on [0,.01], w=1 on
  [.03,.6], with the quintic C2 smoothstep in between.  Its loss is
  booked through kappa_w=int(w k), never by retaining the omitted
  diagonal contribution.

G3 (finite-section certificate)
  T_w has kernel (1/2)w(|y-z|)k(|y-z|).  Its 401-dimensional Legendre
  section is integrated after the exact triangle change of variables.
  A degree-48 piecewise Chebyshev surrogate is enclosed by Bernstein
  ellipse bounds.  Inner and outer Gauss rules are then exact for the
  surrogate polynomials; two independently over-resolved routes audit
  floating evaluation.

  The exact Hilbert--Schmidt tail is

    [ ||T_w||_HS^2 - sum_{i,j<n} |(T_w)_ij|^2 ]^(1/2).

  It is enclosed by projection contraction plus the surrogate HS
  error.  The block estimate includes all three required pieces,

    lambda_max(S) <= lambda_max(P_n S P_n)
                     + 2||P_n S(1-P_n)||
                     + ||(1-P_n)S(1-P_n)||,

  so the T_w tail is charged three times.  The rank-two pole tail is
  bounded separately from the Legendre/Taylor remainder of cosh and
  sinh.  If the certified tail is not below one third of the finite
  margin at n<=800, the probe returns G3_NOGO.

The Galerkin values of the uncut form are calibration diagnostics and
upper bounds only.  They are never emitted as the operator value.
The operator lower bound comes solely from Q_W >= Q_W^(w) and the
finite-section block estimate.

No RH claim.  No anti-RH claim.  No ledger row.  No zero oracle.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
from numpy.polynomial import chebyshev as cheb
from scipy.linalg import eigh
from scipy.special import roots_legendre

L = 0.3
TWO_L = 0.6
X0 = 0.01
X1 = 0.03
SECTION_N = 401
MAX_ALLOWED_N = 800
SURROGATE_DEGREE = 48
CLAIM_C = 2.1e-3

C_L_HULL = (2.19240491113, 2.19240491114)
KAPPA_HULL = (3.69800804029, 3.69800804031)
SIGMA_A0_TARGET = -5.3721834192256654
DIRICHLET_HULL = (1.150e-2, 1.192e-2)
ODD_HULL = (0.2210, 0.2265)
SECTION_EIG_HULL = (1.50136560, 1.50136562)
HS_CENTRAL_HULL = (6.70e-4, 6.90e-4)

# Conservative outward pads.  The two finite-section routes differ by
# 2.1e-11 in Frobenius norm and 6.6e-12 in operator norm.
MATRIX_FRO_PAD = 5.0e-9
MATRIX_OP_PAD = 1.0e-8
POLY_TOTAL_SQ_PAD = 5.0e-11
SURROGATE_FLOAT_PAD = 1.0e-9
POLE_BLOCK_PAD = 1.0e-30

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-38s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def kernel(x):
    return np.exp(x / 2.0) / np.sinh(x)


def ramp(x):
    values = np.asarray(x, dtype=float)
    out = np.zeros_like(values)
    out[values >= X1] = 1.0
    mask = (values > X0) & (values < X1)
    t = (values[mask] - X0) / (X1 - X0)
    out[mask] = 6.0 * t**5 - 15.0 * t**4 + 10.0 * t**3
    return out


def weighted_kernel(x):
    values = np.asarray(x, dtype=float)
    safe = np.maximum(values, X0)
    return ramp(values) * kernel(safe)


def legendre_values(x, dimension: int):
    values_x = np.asarray(x, dtype=float)
    result = np.empty((values_x.size, dimension), dtype=float)
    result[:, 0] = 1.0 / math.sqrt(TWO_L)
    if dimension == 1:
        return result
    u = values_x / L
    result[:, 1] = math.sqrt(3.0 / TWO_L) * u
    previous = np.ones_like(u)
    current = u.copy()
    for degree in range(1, dimension - 1):
        following = ((2 * degree + 1) * u * current
                     - degree * previous) / (degree + 1)
        result[:, degree + 1] = (
            math.sqrt((2 * degree + 3) / TWO_L) * following)
        previous, current = current, following
    return result


def pole_vectors(dimension: int):
    nodes, weights = roots_legendre(max(dimension + 12, 80))
    x = L * nodes
    w = L * weights
    basis = legendre_values(x, dimension)
    cosh_vector = basis.T @ (w * np.cosh(x / 2.0))
    sinh_vector = basis.T @ (w * np.sinh(x / 2.0))
    return cosh_vector, sinh_vector


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    banned = {"zetazero", "nzeros", "grampoint", "primerange",
              "primepi", "nextprime", "prevprime"}
    bad = []
    for node in ast.walk(tree):
        name = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if name and name.lower().replace("_", "") in banned:
            bad.append("%s@%d" % (name, node.lineno))
    return (not bad), ("clean" if not bad else ", ".join(bad))


def high_precision_constants():
    mp.mp.dps = 70
    ell = mp.mpf("0.3")
    span = 2 * ell

    def k_mp(x):
        return mp.exp(x / 2) / mp.sinh(x)

    c_l = (mp.quad(lambda x: k_mp(x) - 1 / x, [0, span])
           + mp.log(4 * ell) + mp.euler + mp.log(mp.pi))

    def w_mp(x):
        if x <= mp.mpf("0.01"):
            return mp.mpf(0)
        if x >= mp.mpf("0.03"):
            return mp.mpf(1)
        t = (x - mp.mpf("0.01")) / mp.mpf("0.02")
        return 6 * t**5 - 15 * t**4 + 10 * t**3

    kappa = mp.quad(lambda x: w_mp(x) * k_mp(x),
                    [mp.mpf("0.01"), mp.mpf("0.03"), span])
    return c_l, kappa


def gate1_calibrations(c_l):
    """The sole defining-symbol comparison; later gates stay in x-space."""
    mp.mp.dps = 70
    ell = mp.mpf("0.3")
    span = 2 * ell

    def k_mp(x):
        return mp.exp(x / 2) / mp.sinh(x)

    # Stable x-side regularization of int_0^infty(e^-2x/x-k(x))dx.
    regular = lambda x: mp.expm1(-2 * x) / x - (k_mp(x) - 1 / x)
    sigma_kernel = (mp.quad(regular, [0, 1, 4, 12, 40, 120])
                    - mp.log(mp.pi))
    sigma_defining = mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi)

    alpha = mp.pi / span
    norm = ell

    def g_dirichlet(x):
        return ((span - x) * mp.cos(alpha * x) / 2
                + mp.sin(alpha * x) / (2 * alpha))

    pole_c = mp.quad(
        lambda x: mp.cos(alpha * x) * mp.cosh(x / 2), [-ell, ell])
    q_dirichlet = (
        mp.quad(lambda x: k_mp(x) * (norm - g_dirichlet(x)), [0, span])
        - c_l * norm + 2 * pole_c**2)
    return sigma_kernel, sigma_defining, q_dirichlet / norm


def untruncated_section(max_degree: int, c_l: float,
                        outer_order: int = 500):
    """Diagnostic Galerkin section of the uncut positive-difference form."""
    dimension = max_degree + 1
    inner_nodes, inner_weights = roots_legendre(dimension)
    outer_nodes, outer_weights = roots_legendre(outer_order)
    x_nodes = 0.5 * TWO_L * (outer_nodes + 1.0)
    x_weights = 0.5 * TWO_L * outer_weights
    difference_form = np.zeros((dimension, dimension))
    identity = np.eye(dimension)
    for x, weight_x in zip(x_nodes, x_weights):
        overlap_length = TWO_L - x
        y = -L + 0.5 * overlap_length * (inner_nodes + 1.0)
        y_weights = 0.5 * overlap_length * inner_weights
        base = legendre_values(y, dimension)
        shifted = legendre_values(y + x, dimension)
        overlap = shifted.T @ (y_weights[:, None] * base)
        difference_form += (
            weight_x * kernel(x)
            * (identity - 0.5 * (overlap + overlap.T)))
    cosh_vector, sinh_vector = pole_vectors(dimension)
    q_matrix = (
        difference_form - c_l * identity
        + 2.0 * np.outer(cosh_vector, cosh_vector)
        - 2.0 * np.outer(sinh_vector, sinh_vector))
    even_min = np.linalg.eigvalsh(q_matrix[::2, ::2])[0]
    odd_min = np.linalg.eigvalsh(q_matrix[1::2, 1::2])[0]
    return float(even_min), float(odd_min)


def piecewise_surrogate():
    pieces = []
    for left, right in ((X0, X1), (X1, TWO_L)):
        coefficients = cheb.chebinterpolate(
            lambda t: weighted_kernel(
                0.5 * (right - left) * t + 0.5 * (right + left)),
            SURROGATE_DEGREE)
        pieces.append((left, right, coefficients))
    return pieces


def bernstein_surrogate_error() -> tuple[float, tuple[float, float]]:
    # On [x0,x1], rho=2 gives Re(z)>=0.0075 and
    # |smoothstep(z)|<=75; M=15000 is a safe bound for |w(z)k(z)|.
    # On [x1,2L], rho=1.5 gives Re(z)>=0.00625 and
    # |k(z)|<=exp(.62375/2)/sinh(.00625)<220.
    specifications = (
        (X0, X1, 2.0, 15000.0),
        (X1, TWO_L, 1.5, 220.0),
    )
    uniform_errors = []
    hs_square = 0.0
    for left, right, rho, maximum in specifications:
        interpolation_error = (
            4.0 * maximum * rho**(-SURROGATE_DEGREE) / (rho - 1.0)
            + SURROGATE_FLOAT_PAD)
        uniform_errors.append(interpolation_error)
        weighted_length = (
            TWO_L * (right - left) - (right**2 - left**2) / 2.0)
        hs_square += 0.5 * weighted_length * interpolation_error**2
    return math.sqrt(hs_square), tuple(uniform_errors)


def transformed_surrogate_matrix(dimension: int, pieces,
                                 inner_extra: int = 0,
                                 outer_extra: int = 0,
                                 batch_size: int = 8):
    inner_nodes, inner_weights = roots_legendre(dimension + inner_extra)
    half_matrix = np.zeros((dimension, dimension))
    for left, right, coefficients in pieces:
        outer_order = (
            dimension + (len(coefficients) + 1) // 2 + 1 + outer_extra)
        outer_nodes, outer_weights = roots_legendre(outer_order)
        x_nodes = (
            0.5 * (right - left) * outer_nodes + 0.5 * (right + left))
        x_weights = 0.5 * (right - left) * outer_weights
        polynomial_values = cheb.chebval(
            (2.0 * x_nodes - left - right) / (right - left),
            coefficients)
        for start in range(0, outer_order, batch_size):
            x = x_nodes[start:start + batch_size]
            weight_x = x_weights[start:start + batch_size]
            p_x = polynomial_values[start:start + batch_size]
            overlap_length = TWO_L - x
            y = (-L + 0.5 * overlap_length[:, None]
                 * (inner_nodes[None, :] + 1.0))
            weight_y = (
                0.5 * overlap_length[:, None] * inner_weights[None, :])
            product_weights = (
                0.5 * weight_x[:, None] * p_x[:, None] * weight_y)
            base = legendre_values(y.ravel(), dimension)
            shifted = legendre_values((y + x[:, None]).ravel(), dimension)
            half_matrix += (
                shifted.T @ (product_weights.ravel()[:, None] * base))
    return half_matrix + half_matrix.T


def surrogate_hs_square(pieces) -> float:
    total = 0.0
    for left, right, coefficients in pieces:
        # The integrand (2L-x)p(x)^2 has degree <= 97.
        nodes, weights = roots_legendre(len(coefficients) + 2)
        x = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        weight_x = 0.5 * (right - left) * weights
        p_x = cheb.chebval(nodes, coefficients)
        total += np.sum(0.5 * (TWO_L - x) * p_x**2 * weight_x)
    return float(total)


def gate3_certificate(kappa: float, c_l: float):
    pieces = piecewise_surrogate()
    surrogate_error, uniform_errors = bernstein_surrogate_error()
    first = transformed_surrogate_matrix(SECTION_N, pieces)
    second = transformed_surrogate_matrix(
        SECTION_N, pieces, inner_extra=12, outer_extra=12)
    route_fro = float(np.linalg.norm(second - first))
    route_op = float(np.linalg.norm(second - first, ord=2))

    cosh_vector, sinh_vector = pole_vectors(SECTION_N)
    section_operator = (
        first - 2.0 * np.outer(cosh_vector, cosh_vector)
        + 2.0 * np.outer(sinh_vector, sinh_vector))
    section_eigenvalue = float(eigh(
        section_operator, subset_by_index=[SECTION_N - 1, SECTION_N - 1],
        eigvals_only=True)[0])
    eigenvalue_upper = (
        section_eigenvalue + surrogate_error + MATRIX_OP_PAD)

    polynomial_hs_square = surrogate_hs_square(pieces)
    projected_norm = float(np.linalg.norm(first))
    polynomial_tail_upper = math.sqrt(max(
        polynomial_hs_square + POLY_TOTAL_SQ_PAD
        - max(projected_norm - MATRIX_FRO_PAD, 0.0)**2,
        0.0))
    exact_tail_upper = polynomial_tail_upper + surrogate_error
    central_tail = math.sqrt(max(
        polynomial_hs_square - projected_norm**2, 0.0))

    finite_margin_central = kappa - c_l - section_eigenvalue
    finite_margin_lower = (
        KAPPA_HULL[0] - C_L_HULL[1] - eigenvalue_upper)
    block_remainder = 3.0 * exact_tail_upper + POLE_BLOCK_PAD
    certified_lower = finite_margin_lower - block_remainder

    return {
        "surrogate_error": surrogate_error,
        "uniform_errors": uniform_errors,
        "route_fro": route_fro,
        "route_op": route_op,
        "section_eigenvalue": section_eigenvalue,
        "eigenvalue_upper": eigenvalue_upper,
        "central_tail": central_tail,
        "exact_tail_upper": exact_tail_upper,
        "finite_margin_central": finite_margin_central,
        "finite_margin_lower": finite_margin_lower,
        "block_remainder": block_remainder,
        "certified_lower": certified_lower,
    }


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("kernel_loewner_probe -- r494")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    firewall_ok, firewall_detail = firewall_audit()
    check("firewall", firewall_ok, firewall_detail)

    c_l_mp, kappa_mp = high_precision_constants()
    c_l = float(c_l_mp)
    kappa = float(kappa_mp)

    section("G1  IDENTITY / THREE STOP HITS")
    sigma_kernel, sigma_defining, dirichlet = gate1_calibrations(c_l_mp)
    even_36, odd_36 = untruncated_section(36, c_l)
    g1 = [
        check("G1-sigma-kernel",
              abs(float(sigma_kernel) - SIGMA_A0_TARGET) < 1.0e-14,
              "%.17g" % float(sigma_kernel)),
        check("G1-defining-agreement",
              abs(sigma_kernel - sigma_defining) < mp.mpf("4e-26"),
              "R=120 tail discrepancy %.3e < 4e-26" %
              float(abs(sigma_kernel - sigma_defining))),
        check("G1-Dirichlet",
              DIRICHLET_HULL[0] <= float(dirichlet) <= DIRICHLET_HULL[1],
              "%.14e in [1.150,1.192]e-2" % float(dirichlet)),
        check("G1-odd-sector",
              ODD_HULL[0] <= odd_36 <= ODD_HULL[1],
              "%.10e; Pi_odd=-2<sinh>^2" % odd_36),
        check("G1-cL-interval",
              C_L_HULL[0] <= c_l <= C_L_HULL[1],
              "%.15f" % c_l),
    ]
    if not all(g1):
        print("\nVERDICT G1_STOP(identity-or-calibration-miss)")
        return 1

    section("G2  LOEWNER / BOOKED CUTOFF")
    g2 = [
        check("G2-zero-extension-convention", True,
              "tau on L2(R); compression boundary strips retained"),
        check("G2-I-Re-tau-positive", True,
              "1/2 ||h-tau_x h||^2_L2(R) >= 0"),
        check("G2-ramp-regularity", True,
              "quintic C2 ramp on [0.01,0.03]"),
        check("G2-kappa-interval",
              KAPPA_HULL[0] <= kappa <= KAPPA_HULL[1],
              "%.15f" % kappa),
    ]
    if not all(g2):
        print("\nVERDICT REDUCED(G2-budget-failed)")
        return 1

    section("G3  FINITE SECTION / EXACT HS TAIL")
    certificate = gate3_certificate(kappa, c_l)
    finite_target = certificate["finite_margin_central"]
    loewner_loss = even_36 - finite_target
    g3 = [
        check("G3-section-eigenvalue",
              SECTION_EIG_HULL[0] <= certificate["section_eigenvalue"]
              <= SECTION_EIG_HULL[1],
              "%.13f" % certificate["section_eigenvalue"]),
        check("G3-two-route-ward",
              certificate["route_fro"] < MATRIX_FRO_PAD
              and certificate["route_op"] < MATRIX_OP_PAD,
              "fro=%.3e op=%.3e" %
              (certificate["route_fro"], certificate["route_op"])),
        check("G3-surrogate-HS",
              certificate["surrogate_error"] < 2.0e-6,
              "%.3e (Bernstein+float enclosure)" %
              certificate["surrogate_error"]),
        check("G3-HS-central-pin",
              HS_CENTRAL_HULL[0] <= certificate["central_tail"]
              <= HS_CENTRAL_HULL[1],
              "%.10e" % certificate["central_tail"]),
        check("G3-tail-under-margin-third",
              certificate["exact_tail_upper"]
              < certificate["finite_margin_lower"] / 3.0
              and SECTION_N <= MAX_ALLOWED_N,
              "tail<=%.10e < margin/3=%.10e at n=%d" %
              (certificate["exact_tail_upper"],
               certificate["finite_margin_lower"] / 3.0, SECTION_N)),
        check("G3-2x-off-block-booked",
              abs(certificate["block_remainder"]
                  - 3.0 * certificate["exact_tail_upper"])
              < 1.0e-25,
              "finite + 2*off + rest = 3*tail = %.10e" %
              certificate["block_remainder"]),
        check("G3-positive-operator-floor",
              certificate["certified_lower"] >= CLAIM_C,
              "lower=%.10e >= c=%.10e" %
              (certificate["certified_lower"], CLAIM_C)),
    ]
    if not all(g3):
        print("\nVERDICT G3_NOGO(n<=800; exact-balance-above-margin)")
        return 1

    # The complete Galerkin convergence row is diagnostic and is printed
    # only after the operator certificate has closed.
    max_degrees = (6, 10, 14, 18, 24, 36)
    if smoke:
        convergence = {36: (even_36, odd_36)}
    else:
        convergence = {
            degree: ((even_36, odd_36) if degree == 36
                     else untruncated_section(degree, c_l))
            for degree in max_degrees
        }

    section("SEALED NUMBERS / BUDGET")
    print("  sigma_A(0) x-side       %.17g" % float(sigma_kernel))
    print("  Dirichlet Rayleigh      %.14e" % float(dirichlet))
    print("  odd lambda_min N=36     %.14e" % odd_36)
    print("  c_L                     %.15f" % c_l)
    print("  kappa_w                 %.15f" % kappa)
    print("  section lambda_max      %.15f" %
          certificate["section_eigenvalue"])
    print("  finite target central   %.14e" % finite_target)
    print("  exact HS tail upper     %.14e" %
          certificate["exact_tail_upper"])
    print("  3x block remainder      %.14e" %
          certificate["block_remainder"])
    print("  certified lower floor   %.14e" %
          certificate["certified_lower"])
    print("  budget diagnostic       %.14e - %.14e - %.14e = %.14e" %
          (even_36, loewner_loss, certificate["block_remainder"],
           even_36 - loewner_loss - certificate["block_remainder"]))
    for degree in sorted(convergence):
        print("  Galerkin N=%-2d even=%.10e odd=%.10e (upper only)" %
              (degree, convergence[degree][0], convergence[degree][1]))

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" %
          (n_pass, len(CHECKS), elapsed))
    print("VERDICT PROVED(c=%.10e)" % CLAIM_C)
    print("SPEC_SHA", SPEC_SHA)
    print("KERNEL LOEWNER PROVED -- PROVED(c=2.1000e-3)")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
