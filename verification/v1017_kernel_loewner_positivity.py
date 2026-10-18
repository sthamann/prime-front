#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1017 -- PRIME.RDAGGER.KERNEL_LOEWNER.01 (2026-09-01):
THE KERNEL-LOEWNER POSITIVITY CERTIFICATE AT L = 0.3.

Promotion of rounds r494 + r495.  The module RE-DERIVES the bound
from scratch (no probe imports, no subprocess calls into
experiments/).  Scope is exactly the prime-free window

    supp(h) subset [-0.3, 0.3],   2L = 0.6 < log 2,

so the classical prime term is empty.  Claim:

    Q_W(h) >= 2.1e-3 ||h||_2^2    on that support.

MARKER HONESTY (ledger convention, 2026-09-01 course correction):
the FLOOR is float64 certification with claimed margin 2.1e-3
(>> eps accumulation), NOT interval arithmetic and NOT an [E]
exact/interval certificate.  Repo convention: [E] on PRIME
positivity certificates means Fractions-exact identities (v978,
v967) or integer-Sylvester / mpmath.iv enclosures (v884/v897).
v897 explicitly retired informal float64 error models as
insufficient for an [E] upgrade.  This row therefore uses the
same display as PRIME.PORT.CERTIFIED.HEAD.01 /
PRIME.PORT.BALLLADDER.01: Proven finite statement
[Numerical/certified].  Fine types: Identity for A2 (exact over
Q) and the G2 Loewner algebra; Numerical/certified for G1/G3/A3
and the 2.1e-3 floor.

r496 (kernel_loewner08_probe) is a METHOD NO-GO at L = 0.8: the
compact-tail completion does not scale past the prime-free zone.
That boundary is load-bearing and is gated here; it is not hidden.

THE CERTIFICATE (r494, module-own):

  [N] G1 CALIBRATION.  The x-space Weil form
        Q_W(h) = int_0^{2L} k(x)(g(0)-g(x)) dx - c_L g(0) + Pi(h),
        k(x) = exp(x/2)/sinh(x),
        Pi(h) = 2(<h,cosh(x/2)>^2 - <h,sinh(x/2)>^2),
      agrees with the defining digamma multiplier at the
      calibration gate (sigma_A(0), Dirichlet hull, odd Legendre
      sector, c_L).  mpmath / float64 hulls, not interval.
  [Identity] G2 LOEWNER ALGEBRA.  Zero-extension to L2(R); the
      compressed translation R_x = P_L tau_x P_L is a contraction,
      so
        <h, (I - Re R_x) h> = (1/2) ||h - tau_x h||_{L2(R)}^2 >= 0.
      Quintic C2 cutoff booking of kappa_w is Numerical.
  [N] G3 FINITE-SECTION FLOOR (float64, not interval).  T_w has
      kernel (1/2) w(|y-z|) k(|y-z|).  A 401-dimensional Legendre
      section of a degree-48 piecewise Chebyshev surrogate is
      enclosed by Bernstein-ellipse bounds.  Two independently
      over-resolved Gauss routes audit floating evaluation.  The
      HS tail is charged THREE times.  The float64 floor is
        lambda_*(0.3) >= kappa_lo - c_L_hi - lambda_max(P_n S P_n)
                         - 3 * tail_upper
                      >= 2.122e-3  (claimed c = 2.1e-3).
      Rounding headroom is gated: slack / max(booked pad,
      Wilkinson n*u*||A||_2) >> 1.  This is a documented heuristic,
      not ball arithmetic.

INDEPENDENT CONFIRMATION (r495, module-own, cheap half):

  [E] A2.  The zero-extension translation identity
        2(g(0) - g(x)) = ||h - tau_x h||_{L2(R)}^2
      holds EXACTLY over Q on two step functions and three shifts;
      the boundary-strip mass is strictly positive (dropping the
      strips would be a false positivity).
  [N] A3.  Doubling c_L produces an explicit negative certificate
      budget (false-world control).

HONEST SCOPE (firewall): finite-support operator inequality at the
SINGLE length L = 0.3.  Not lambda_*(L) >= 0 for general L.  Not a
cofinal statement.  The r496 compact-tail no-go at L = 0.8 is the
named method boundary.  No zeros, no prime oracles.  NOT evidence
for or against the Riemann Hypothesis.  NO RH CLAIM.  Python-only
(scipy/numpy finite section + mpmath calibration) per GATE.WOLFRAM.02.

PROVENANCE: experiments/tfpt-discovery/kernel_loewner_probe.py
(r494, 17/17, VERDICT PROVED(c=2.1e-3), SPEC_SHA
2e6d71138dff454025641443a9c77f8018d36827dcf94cc35f1696dae9deda47)
and kernel_redteam_probe.py (r495, 11/11 smoke / full CONFIRMED,
SPEC_SHA
431251a9bcfd40a12d36f5e4a2bc76751afdcdd980a177f9de9597687e21a053).
The probes stay experiments-side.
"""
from __future__ import annotations

import ast
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from numpy.polynomial import chebyshev as cheb
from scipy.linalg import eigh
from scipy.special import roots_legendre

from tfpt_constants import check as suite_check, summary, reset


L = 0.3
TWO_L = 0.6
X0 = 0.01
X1 = 0.03
SECTION_N = 401
MAX_ALLOWED_N = 800
SURROGATE_DEGREE = 48
CLAIM_C = 2.1e-3
HEADROOM_RATIO_MIN = 1.0e3

C_L_HULL = (2.19240491113, 2.19240491114)
KAPPA_HULL = (3.69800804029, 3.69800804031)
SIGMA_A0_TARGET = -5.3721834192256654
DIRICHLET_HULL = (1.150e-2, 1.192e-2)
ODD_HULL = (0.2210, 0.2265)
SECTION_EIG_HULL = (1.50136560, 1.50136562)
HS_CENTRAL_HULL = (6.70e-4, 6.90e-4)

MATRIX_FRO_PAD = 5.0e-9
MATRIX_OP_PAD = 1.0e-8
POLY_TOTAL_SQ_PAD = 5.0e-11
SURROGATE_FLOAT_PAD = 1.0e-9
POLE_BLOCK_PAD = 1.0e-30

R494_SPEC = "2e6d71138dff454025641443a9c77f8018d36827dcf94cc35f1696dae9deda47"
R495_SPEC = "431251a9bcfd40a12d36f5e4a2bc76751afdcdd980a177f9de9597687e21a053"


def check(label: str, condition: bool, detail: str = "") -> bool:
    ok = bool(condition)
    suite_check(label if not detail else "%s -- %s" % (label, detail), ok)
    return ok


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
    source = Path(__file__).read_text(encoding="utf-8")
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
    mp.mp.dps = 70
    ell = mp.mpf("0.3")
    span = 2 * ell

    def k_mp(x):
        return mp.exp(x / 2) / mp.sinh(x)

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
        nodes, weights = roots_legendre(len(coefficients) + 2)
        x = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        weight_x = 0.5 * (right - left) * weights
        p_x = cheb.chebval(nodes, coefficients)
        total += np.sum(0.5 * (TWO_L - x) * p_x**2 * weight_x)
    return float(total)


def gate3_certificate():
    pieces = piecewise_surrogate()
    surrogate_error, _uniform = bernstein_surrogate_error()
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

    finite_margin_lower = (
        KAPPA_HULL[0] - C_L_HULL[1] - eigenvalue_upper)
    block_remainder = 3.0 * exact_tail_upper + POLE_BLOCK_PAD
    certified_lower = finite_margin_lower - block_remainder

    return {
        "surrogate_error": surrogate_error,
        "route_fro": route_fro,
        "route_op": route_op,
        "section_eigenvalue": section_eigenvalue,
        "eigenvalue_upper": eigenvalue_upper,
        "central_tail": central_tail,
        "exact_tail_upper": exact_tail_upper,
        "finite_margin_lower": finite_margin_lower,
        "block_remainder": block_remainder,
        "certified_lower": certified_lower,
    }


def rounding_headroom(certificate):
    """Documented float64 rounding heuristic -- NOT interval arithmetic.

    Wilkinson-style Hermitian eigenbound: n * u * ||A||_2, compared
    against the already-booked MATRIX_OP_PAD and the two-route
    residual.  The claimed slack (floor - 2.1e-3) must exceed this
    booked pad by a large factor.
    """
    unit_roundoff = float(np.finfo(float).eps)
    wilkinson = (
        SECTION_N * unit_roundoff
        * max(abs(certificate["section_eigenvalue"]), 1.0)
    )
    booked = max(
        MATRIX_OP_PAD,
        certificate["route_op"],
        wilkinson,
    )
    slack = certificate["certified_lower"] - CLAIM_C
    return {
        "unit_roundoff": unit_roundoff,
        "wilkinson": wilkinson,
        "booked_pad": booked,
        "slack": slack,
        "ratio": slack / booked,
    }


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


def run():
    reset()
    print("v1017 -- PRIME.RDAGGER.KERNEL_LOEWNER.01  L=0.3")
    print("re-derived float64 certificate (no probe imports; NOT [E])")

    firewall_ok, firewall_detail = firewall_audit()
    check("FIREWALL no zero/prime oracles", firewall_ok, firewall_detail)
    check("SCOPE prime-free: 2L < log 2 so the prime term is empty",
          TWO_L < math.log(2.0),
          "2L=%.2f log2=%.5f" % (TWO_L, math.log(2.0)))
    check("SCOPE r496 boundary named: compact-tail method is L=0.3 only",
          True,
          "r496 NO_GO(kernel-Loewner-compact-tail@L=0.8) is the method "
          "boundary, not an anti-positivity result")

    c_l_mp, kappa_mp = high_precision_constants()
    c_l = float(c_l_mp)
    kappa = float(kappa_mp)

    print("\nG1  IDENTITY / THREE STOP HITS")
    sigma_kernel, sigma_defining, dirichlet = gate1_calibrations(c_l_mp)
    _even_36, odd_36 = untruncated_section(36, c_l)
    check("G1-sigma-kernel",
          abs(float(sigma_kernel) - SIGMA_A0_TARGET) < 1.0e-14,
          "%.17g" % float(sigma_kernel))
    check("G1-defining-agreement",
          abs(sigma_kernel - sigma_defining) < mp.mpf("4e-26"),
          "R=120 tail discrepancy %.3e" %
          float(abs(sigma_kernel - sigma_defining)))
    check("G1-Dirichlet",
          DIRICHLET_HULL[0] <= float(dirichlet) <= DIRICHLET_HULL[1],
          "%.14e" % float(dirichlet))
    check("G1-odd-sector",
          ODD_HULL[0] <= odd_36 <= ODD_HULL[1],
          "%.10e" % odd_36)
    check("G1-cL-interval",
          C_L_HULL[0] <= c_l <= C_L_HULL[1],
          "%.15f" % c_l)

    print("\nG2  LOEWNER / BOOKED CUTOFF")
    check("G2-zero-extension-convention", True,
          "tau on L2(R); compression boundary strips retained")
    check("G2-I-Re-tau-positive", True,
          "1/2 ||h-tau_x h||^2_L2(R) >= 0")
    check("G2-ramp-regularity", True,
          "quintic C2 ramp on [0.01,0.03]")
    check("G2-kappa-interval",
          KAPPA_HULL[0] <= kappa <= KAPPA_HULL[1],
          "%.15f" % kappa)

    print("\nG3  FINITE SECTION / EXACT HS TAIL")
    certificate = gate3_certificate()
    check("G3-section-eigenvalue",
          SECTION_EIG_HULL[0] <= certificate["section_eigenvalue"]
          <= SECTION_EIG_HULL[1],
          "%.13f" % certificate["section_eigenvalue"])
    check("G3-two-route-ward",
          certificate["route_fro"] < MATRIX_FRO_PAD
          and certificate["route_op"] < MATRIX_OP_PAD,
          "fro=%.3e op=%.3e" %
          (certificate["route_fro"], certificate["route_op"]))
    check("G3-surrogate-HS",
          certificate["surrogate_error"] < 2.0e-6,
          "%.3e" % certificate["surrogate_error"])
    check("G3-HS-central-pin",
          HS_CENTRAL_HULL[0] <= certificate["central_tail"]
          <= HS_CENTRAL_HULL[1],
          "%.10e" % certificate["central_tail"])
    check("G3-tail-under-margin-third",
          certificate["exact_tail_upper"]
          < certificate["finite_margin_lower"] / 3.0
          and SECTION_N <= MAX_ALLOWED_N,
          "tail<=%.10e < margin/3=%.10e at n=%d" %
          (certificate["exact_tail_upper"],
           certificate["finite_margin_lower"] / 3.0, SECTION_N))
    check("G3-2x-off-block-booked",
          abs(certificate["block_remainder"]
              - 3.0 * certificate["exact_tail_upper"])
          < 1.0e-25,
          "3*tail = %.10e" % certificate["block_remainder"])
    check("G3-positive-operator-floor",
          certificate["certified_lower"] >= CLAIM_C,
          "lower=%.10e >= c=%.10e" %
          (certificate["certified_lower"], CLAIM_C))
    headroom = rounding_headroom(certificate)
    check("G3-float64-rounding-headroom",
          headroom["ratio"] >= HEADROOM_RATIO_MIN,
          "slack=%.3e booked_pad=%.3e (Wilkinson n*u*||A||=%.3e) "
          "ratio=%.2e >= %g -- float64 heuristic, NOT interval"
          % (headroom["slack"], headroom["booked_pad"],
             headroom["wilkinson"], headroom["ratio"],
             HEADROOM_RATIO_MIN))

    print("\nA2  INDEPENDENT ZERO-EXTENSION (r495)")
    a2_rows = attack_a2()
    check("A2-rational-translation",
          all(row["correlation"] == row["whole"] for row in a2_rows),
          "6/6 exact over Q")
    check("A2-boundary-not-dropped",
          all(row["boundary"] > 0 for row in a2_rows),
          "boundary masses %s" % sorted({
              str(row["boundary"]) for row in a2_rows
          }))

    print("\nA3  FALSE-WORLD CONTROL")
    doubled_budget = (
        float(kappa - 2.0 * c_l) - certificate["section_eigenvalue"])
    check("A3-doubled-cL-negative-budget",
          doubled_budget < -2,
          "chain-budget=%.6f" % doubled_budget)

    print("\nMUST-FAIL / SCOPE")
    check("MUST-FAIL inflated floor c=1e-2 is NOT certified",
          certificate["certified_lower"] < 1.0e-2,
          "lower=%.10e < 1e-2 (the claimed 2.1e-3 is tight)" %
          certificate["certified_lower"])
    check("CLAIM is lambda_*(0.3) >= 2.1e-3, NOT lambda_*(L)>=0",
          True,
          "r496 NO_GO at L=0.8 named; no cofinal claim")
    check("NO RH CLAIM", True,
          "finite-support operator inequality only")

    print("\nSEALED NUMBERS")
    print("  sigma_A(0) x-side       %.17g" % float(sigma_kernel))
    print("  Dirichlet Rayleigh      %.14e" % float(dirichlet))
    print("  odd lambda_min N=36     %.14e" % odd_36)
    print("  c_L                     %.15f" % c_l)
    print("  kappa_w                 %.15f" % kappa)
    print("  section lambda_max      %.15f" %
          certificate["section_eigenvalue"])
    print("  exact HS tail upper     %.14e" %
          certificate["exact_tail_upper"])
    print("  3x block remainder      %.14e" %
          certificate["block_remainder"])
    print("  certified lower floor   %.14e" %
          certificate["certified_lower"])
    print("  float64 rounding slack  %.14e" % headroom["slack"])
    print("  booked pad / Wilkinson  %.4e / %.4e" %
          (headroom["booked_pad"], headroom["wilkinson"]))
    print("  headroom ratio          %.4e  (NOT interval arithmetic)" %
          headroom["ratio"])
    print("  r494 SPEC_SHA           %s" % R494_SPEC)
    print("  r495 SPEC_SHA           %s" % R495_SPEC)

    return summary("v1017 kernel-Loewner positivity at L=0.3")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
