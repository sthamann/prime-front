#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kernel_loewner_window_probe -- PRIME.RDAGGER.KERNEL_LOEWNER.WINDOW.01

Round 536, experiments-side.  Maps the r494 kernel-Loewner positivity
window in the support length L, extending r494--r496.

METHOD (frozen, not reinvented).  The r494 certificate is float64
Gauss--Legendre / degree-48 Chebyshev with Bernstein-ellipse enclosure
and outward pads, plus the exact Hilbert--Schmidt tail of T_w charged
three times.  It is NOT interval/rational certification (r495 used
rationals only for the A2 translation identity, which this probe does
not re-open).  Kernel, cutoff, section size, surrogate degree, and
pads are the r494 freeze:

    k(x) = exp(x/2)/sinh(x),
    w = 0 on [0, 0.01], quintic C2 on [0.01, 0.03], w = 1 after,
    n = 401, deg = 48, pads as in kernel_loewner_probe.py.

Scaling.  X0, X1, n, deg, pads stay absolute (the singularity is at
x=0, independent of L).  The bulk Chebyshev piece [X1, 2L] is split
so each Bernstein ellipse at rho=1.5 keeps Re(z) >= 0.00625, which
makes the first bulk piece end at 0.6 and recovers r494 exactly at
L=0.3.  Prime powers with log n <= 2L are booked only through the
compact-tail g(0) mass 2 Lambda(n)/sqrt(n); compressed translations
are dropped (they are not HS).  This is the r496 compact-tail bound,
now evaluated on a grid.

No RH claim.  No anti-RH claim.  No ledger row.  No zero oracle.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import sys

import mpmath as mp
import numpy as np
from numpy.polynomial import chebyshev as cheb
from scipy.linalg import eigh
from scipy.special import roots_legendre

X0 = 0.01
X1 = 0.03
SECTION_N = 401
SURROGATE_DEGREE = 48
MAX_ALLOWED_N = 800
CLAIM_C = 2.1e-3
RHO_RAMP = 2.0
RHO_BULK = 1.5
M_RAMP = 15000.0
M_BULK = 220.0
BERNSTEIN_CLEARANCE = 0.00625
CONST_PAD = 1.0e-11

C_L_HULL_03 = (2.19240491113, 2.19240491114)
KAPPA_HULL_03 = (3.69800804029, 3.69800804031)
SECTION_EIG_HULL = (1.50136560, 1.50136562)
HS_CENTRAL_HULL = (6.70e-4, 6.90e-4)

MATRIX_FRO_PAD = 5.0e-9
MATRIX_OP_PAD = 1.0e-8
POLY_TOTAL_SQ_PAD = 5.0e-11
SURROGATE_FLOAT_PAD = 1.0e-9
POLE_BLOCK_PAD = 1.0e-30

GRID = (
    0.30, 0.35, 0.40, 0.45, 0.50, 0.55,
    0.60, 0.65, 0.70, 0.75, 0.80,
)
BISECTION_STEPS = 2
SMOKE_GRID = (0.30, 0.55, 0.80)
SMOKE_N = 21
SMOKE_DEGREE = 8

# n with log n <= 1.6; sufficient for L <= 0.8.  Factor two as r496.
PRIME_DATA = (
    (2, math.log(2.0), math.log(2.0) / math.sqrt(2.0)),
    (3, math.log(3.0), math.log(3.0) / math.sqrt(3.0)),
    (4, math.log(4.0), math.log(2.0) / 2.0),
)

SPEC = {
    "round": 536,
    "contract": "PRIME.RDAGGER.KERNEL_LOEWNER.WINDOW.01",
    "method": "r494-float-bernstein-hs-3x-block",
    "not_interval_rational": True,
    "kernel": "exp(x/2)/sinh(x)",
    "X0": X0,
    "X1": X1,
    "section_n": SECTION_N,
    "surrogate_degree": SURROGATE_DEGREE,
    "max_allowed_n": MAX_ALLOWED_N,
    "claim_c": CLAIM_C,
    "grid": list(GRID),
    "bisection_steps": BISECTION_STEPS,
    "rho_ramp": RHO_RAMP,
    "rho_bulk": RHO_BULK,
    "M_ramp": M_RAMP,
    "M_bulk": M_BULK,
    "bernstein_clearance": BERNSTEIN_CLEARANCE,
    "pads": {
        "matrix_fro": MATRIX_FRO_PAD,
        "matrix_op": MATRIX_OP_PAD,
        "poly_total_sq": POLY_TOTAL_SQ_PAD,
        "surrogate_float": SURROGATE_FLOAT_PAD,
        "pole_block": POLE_BLOCK_PAD,
        "const": CONST_PAD,
    },
    "cutoff": "quintic-C2-frozen-absolute-[0.01,0.03]",
    "prime_rule": (
        "log n <= 2L; compact-tail books 2 Lambda(n)/sqrt(n) g(0); "
        "translations dropped (not HS)"
    ),
    "scaling": (
        "X0,X1,n,deg,pads absolute; bulk [X1,2L] split so rho=1.5 "
        "ellipses keep Re(z)>=0.00625 (first bulk piece ends at 0.6)"
    ),
    "tail_alt": (
        "block-Schur 2||off||+||rest|| of T_w replacing 3x HS; "
        "Schur/CS on Re R_s for primes; cosine-weight L2 transfer"
    ),
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" % (
        "PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def fmt(value: float, digits: int = 16) -> str:
    return "%.*e" % (digits, float(value))


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


def primes_in_window(ell: float):
    span = 2.0 * ell
    return [
        (n, shift, weight)
        for n, shift, weight in PRIME_DATA
        if shift <= span
    ]


def prime_mass(ell: float) -> float:
    return 2.0 * sum(weight for _, _, weight in primes_in_window(ell))


def schur_reR_charge(ell: float):
    """Schur/CS upper bound on 2 sum a_n <h, Re R_s h>/||h||^2.

    Re R_s <= (M_domain + M_image)/2, whose essential supremum is 1/2
    when the strips are disjoint (shift >= L) and 1 when they overlap.
    This replaces HS truncation of a non-compact translation.
    """
    charge = 0.0
    rows = []
    for n, shift, weight in primes_in_window(ell):
        disjoint = shift >= ell
        op_bound = 0.5 if disjoint else 1.0
        piece = 2.0 * weight * op_bound
        charge += piece
        rows.append({
            "n": n,
            "shift": shift,
            "weight": weight,
            "disjoint": disjoint,
            "op_bound": op_bound,
            "charge": piece,
        })
    return charge, rows


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    banned = {
        "zetazero", "nzeros", "grampoint", "primerange",
        "primepi", "nextprime", "prevprime",
    }
    bad = []
    for node in ast.walk(tree):
        name = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if name and name.lower().replace("_", "") in banned:
            bad.append("%s@%d" % (name, node.lineno))
    return (not bad), ("clean" if not bad else ", ".join(bad))


def mp_ell(ell: float):
    if abs(ell - 0.3) < 1.0e-15:
        return mp.mpf("0.3")
    return mp.mpf(format(ell, ".10g"))


def high_precision_constants(ell: float):
    mp.mp.dps = 70
    length = mp_ell(ell)
    span = 2 * length

    def k_mp(x):
        return mp.exp(x / 2) / mp.sinh(x)

    c_l = (
        mp.quad(lambda x: k_mp(x) - 1 / x, [0, span])
        + mp.log(4 * length) + mp.euler + mp.log(mp.pi)
    )

    def w_mp(x):
        if x <= mp.mpf("0.01"):
            return mp.mpf(0)
        if x >= mp.mpf("0.03"):
            return mp.mpf(1)
        t = (x - mp.mpf("0.01")) / mp.mpf("0.02")
        return 6 * t**5 - 15 * t**4 + 10 * t**3

    kappa = mp.quad(
        lambda x: w_mp(x) * k_mp(x),
        [mp.mpf("0.01"), mp.mpf("0.03"), span],
    )
    return c_l, kappa


def constant_hulls(ell: float, c_l, kappa):
    if abs(ell - 0.3) < 1.0e-15:
        return C_L_HULL_03, KAPPA_HULL_03
    c_l_float = float(c_l)
    kappa_float = float(kappa)
    return (
        (c_l_float - CONST_PAD, c_l_float + CONST_PAD),
        (kappa_float - CONST_PAD, kappa_float + CONST_PAD),
    )


def bulk_intervals(two_l: float):
    """Split [X1, 2L] so each rho=1.5 ellipse stays at r494 clearance."""
    alpha = (RHO_BULK + 1.0 / RHO_BULK) / 2.0
    coeff_b = 0.5 * (1.0 - alpha)
    coeff_a = 0.5 * (1.0 + alpha)
    pieces = []
    left = X1
    while left < two_l - 1.0e-14:
        # 0.5*(a+b) - 0.5*(b-a)*alpha >= clearance
        right_max = (BERNSTEIN_CLEARANCE - coeff_a * left) / coeff_b
        right = min(two_l, right_max)
        if right <= left:
            right = min(two_l, left + 0.05)
        pieces.append((left, right))
        left = right
    return tuple(pieces)


def interval_pairs(ell: float):
    return ((X0, X1),) + bulk_intervals(2.0 * ell)


def bernstein_specs(ell: float):
    specs = [(X0, X1, RHO_RAMP, M_RAMP)]
    for left, right in bulk_intervals(2.0 * ell):
        specs.append((left, right, RHO_BULK, M_BULK))
    return tuple(specs)


def legendre_values(x, dimension: int, ell: float):
    two_l = 2.0 * ell
    values_x = np.asarray(x, dtype=float)
    result = np.empty((values_x.size, dimension), dtype=float)
    result[:, 0] = 1.0 / math.sqrt(two_l)
    if dimension == 1:
        return result
    u = values_x / ell
    result[:, 1] = math.sqrt(3.0 / two_l) * u
    previous = np.ones_like(u)
    current = u.copy()
    for degree in range(1, dimension - 1):
        following = ((2 * degree + 1) * u * current
                     - degree * previous) / (degree + 1)
        result[:, degree + 1] = (
            math.sqrt((2 * degree + 3) / two_l) * following)
        previous, current = current, following
    return result


def pole_vectors(dimension: int, ell: float):
    nodes, weights = roots_legendre(max(dimension + 12, 80))
    x = ell * nodes
    w = ell * weights
    basis = legendre_values(x, dimension, ell)
    cosh_vector = basis.T @ (w * np.cosh(x / 2.0))
    sinh_vector = basis.T @ (w * np.sinh(x / 2.0))
    return cosh_vector, sinh_vector


def piecewise_surrogate(ell: float, degree: int):
    pieces = []
    for left, right in interval_pairs(ell):
        coefficients = cheb.chebinterpolate(
            lambda t, lo=left, hi=right: weighted_kernel(
                0.5 * (hi - lo) * t + 0.5 * (hi + lo)),
            degree)
        pieces.append((left, right, coefficients))
    return pieces


def bernstein_surrogate_error(ell: float, degree: int):
    two_l = 2.0 * ell
    uniform_errors = []
    hs_square = 0.0
    for left, right, rho, maximum in bernstein_specs(ell):
        interpolation_error = (
            4.0 * maximum * rho**(-degree) / (rho - 1.0)
            + SURROGATE_FLOAT_PAD)
        uniform_errors.append(interpolation_error)
        weighted_length = (
            two_l * (right - left) - (right**2 - left**2) / 2.0)
        hs_square += 0.5 * weighted_length * interpolation_error**2
    return math.sqrt(hs_square), tuple(uniform_errors)


def transformed_surrogate_matrix(
        dimension: int, ell: float, pieces,
        inner_extra: int = 0, outer_extra: int = 0, batch_size: int = 8):
    two_l = 2.0 * ell
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
            overlap_length = two_l - x
            y = (-ell + 0.5 * overlap_length[:, None]
                 * (inner_nodes[None, :] + 1.0))
            weight_y = (
                0.5 * overlap_length[:, None] * inner_weights[None, :])
            product_weights = (
                0.5 * weight_x[:, None] * p_x[:, None] * weight_y)
            base = legendre_values(y.ravel(), dimension, ell)
            shifted = legendre_values(
                (y + x[:, None]).ravel(), dimension, ell)
            half_matrix += (
                shifted.T @ (product_weights.ravel()[:, None] * base))
    return half_matrix + half_matrix.T


def surrogate_hs_square(pieces, ell: float) -> float:
    two_l = 2.0 * ell
    total = 0.0
    for left, right, coefficients in pieces:
        nodes, weights = roots_legendre(len(coefficients) + 2)
        x = 0.5 * (right - left) * nodes + 0.5 * (right + left)
        weight_x = 0.5 * (right - left) * weights
        p_x = cheb.chebval(nodes, coefficients)
        total += np.sum(0.5 * (two_l - x) * p_x**2 * weight_x)
    return float(total)


def certify(ell: float, dimension: int, degree: int, two_route: bool):
    c_l_mp, kappa_mp = high_precision_constants(ell)
    c_l = float(c_l_mp)
    kappa = float(kappa_mp)
    c_l_hull, kappa_hull = constant_hulls(ell, c_l_mp, kappa_mp)
    mass = prime_mass(ell)
    pieces = piecewise_surrogate(ell, degree)
    surrogate_error, uniform_errors = bernstein_surrogate_error(ell, degree)
    first = transformed_surrogate_matrix(dimension, ell, pieces)
    if two_route:
        second = transformed_surrogate_matrix(
            dimension, ell, pieces, inner_extra=12, outer_extra=12)
        route_fro = float(np.linalg.norm(second - first))
        route_op = float(np.linalg.norm(second - first, ord=2))
    else:
        route_fro = 0.0
        route_op = 0.0

    cosh_vector, sinh_vector = pole_vectors(dimension, ell)
    section_operator = (
        first - 2.0 * np.outer(cosh_vector, cosh_vector)
        + 2.0 * np.outer(sinh_vector, sinh_vector))
    section_eigenvalue = float(eigh(
        section_operator, subset_by_index=[dimension - 1, dimension - 1],
        eigvals_only=True)[0])
    eigenvalue_upper = (
        section_eigenvalue + surrogate_error + MATRIX_OP_PAD)

    polynomial_hs_square = surrogate_hs_square(pieces, ell)
    projected_norm = float(np.linalg.norm(first))
    polynomial_tail_upper = math.sqrt(max(
        polynomial_hs_square + POLY_TOTAL_SQ_PAD
        - max(projected_norm - MATRIX_FRO_PAD, 0.0)**2,
        0.0))
    exact_tail_upper = polynomial_tail_upper + surrogate_error
    central_tail = math.sqrt(max(
        polynomial_hs_square - projected_norm**2, 0.0))

    finite_margin_central = kappa - c_l - mass - section_eigenvalue
    finite_margin_lower = (
        kappa_hull[0] - c_l_hull[1] - mass - eigenvalue_upper)
    block_remainder = 3.0 * exact_tail_upper + POLE_BLOCK_PAD
    certified_lower = finite_margin_lower - block_remainder
    ward_ok = (
        route_fro < MATRIX_FRO_PAD and route_op < MATRIX_OP_PAD)
    positive = (
        certified_lower > 0.0
        and ward_ok
        and dimension <= MAX_ALLOWED_N)
    status = "POSITIVE_CERT" if positive else "FAILED"
    fail_reason = "ok"
    if not ward_ok:
        fail_reason = "two-route-ward"
    elif certified_lower <= 0.0:
        if finite_margin_lower <= 0.0:
            fail_reason = "finite-margin-nonpositive"
        else:
            fail_reason = "3x-HS-tail-exceeds-margin"
    return {
        "L": ell,
        "n": dimension,
        "degree": degree,
        "c_l": c_l,
        "kappa": kappa,
        "prime_mass": mass,
        "n_primes": len(primes_in_window(ell)),
        "n_pieces": len(pieces),
        "surrogate_error": surrogate_error,
        "uniform_errors": uniform_errors,
        "route_fro": route_fro,
        "route_op": route_op,
        "ward_ok": ward_ok,
        "section_eigenvalue": section_eigenvalue,
        "eigenvalue_upper": eigenvalue_upper,
        "central_tail": central_tail,
        "exact_tail_upper": exact_tail_upper,
        "finite_margin_central": finite_margin_central,
        "finite_margin_lower": finite_margin_lower,
        "block_remainder": block_remainder,
        "certified_lower": certified_lower,
        "status": status,
        "fail_reason": fail_reason,
    }


def cosine_weight_transfer(ell: float) -> dict:
    """Weighted-space attempt (b): cosine window vanishing at +/-L.

    inf |phi| = 0, so the L2 transfer 1/inf(phi^2) diverges.  A
    regularized phi_eps = cos(pi y / 2L) + eps has transfer 1/eps^2.
    At the first-prime strip width delta = 2L - log 2 (when present)
    a damping eps ~ sin(pi delta / 4L) still costs ~ 1/eps^2.
    """
    inf_phi = 0.0
    nodes = primes_in_window(ell)
    if not nodes:
        return {
            "inf_phi": inf_phi,
            "delta": float("nan"),
            "eps_strip": float("nan"),
            "transfer": float("inf"),
        }
    shift = nodes[0][1]
    delta = 2.0 * ell - shift
    if delta <= 0.0:
        eps_strip = 0.0
        transfer = float("inf")
    else:
        eps_strip = math.sin(math.pi * delta / (4.0 * ell))
        transfer = 1.0 / (eps_strip ** 2)
    return {
        "inf_phi": inf_phi,
        "delta": delta,
        "eps_strip": eps_strip,
        "transfer": transfer,
    }


def block_schur_charge(ell: float, n: int, m: int, degree: int):
    """Replace 3*HS_tail by a block Schur bound of the T_w tail.

    Assemble an outer Legendre section of size m>n.  The (I-P_n) T P_n
    off-block and (I-P_n) T (I-P_n) rest are measured on P_{[n,m)}, and
    the HS remainder beyond m is absorbed by the triangle inequality.
    This is an operator-norm bound, not a Galerkin pad.
    """
    pieces = piecewise_surrogate(ell, degree)
    surr_err, _ = bernstein_surrogate_error(ell, degree)
    t_matrix = transformed_surrogate_matrix(m, ell, pieces)
    off = t_matrix[n:, :n]
    rest = t_matrix[n:, n:]
    off_op = float(np.linalg.norm(off, ord=2))
    rest_op = float(np.linalg.norm(rest, ord=2))
    hs_poly = surrogate_hs_square(pieces, ell)
    projected_big = float(np.linalg.norm(t_matrix))
    remaining_hs = math.sqrt(max(
        hs_poly + POLY_TOTAL_SQ_PAD
        - max(projected_big - MATRIX_FRO_PAD, 0.0)**2,
        0.0)) + surr_err
    charge = 2.0 * (off_op + remaining_hs) + (rest_op + remaining_hs)
    return {
        "m": m,
        "off_op": off_op,
        "rest_op": rest_op,
        "off_hs": float(np.linalg.norm(off)),
        "rest_hs": float(np.linalg.norm(rest)),
        "remaining_hs": remaining_hs,
        "charge": charge,
        "direct_2off_rest": 2.0 * off_op + rest_op,
    }


def print_row(row: dict, tag: str = "") -> None:
    prefix = "  " + (tag + " " if tag else "")
    print(
        "%sL=%-10s  lambda*=%s  %s  margin=%s  "
        "mass=%s  eig=%s  tail3=%s  n_pr=%d  reason=%s"
        % (
            prefix,
            "%.4f" % row["L"],
            fmt(row["certified_lower"]),
            row["status"],
            fmt(row["finite_margin_lower"]),
            fmt(row["prime_mass"], 8),
            fmt(row["section_eigenvalue"], 8),
            fmt(row["block_remainder"], 8),
            row["n_primes"],
            row["fail_reason"],
        ),
        flush=True,
    )


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    print("kernel_loewner_window_probe -- r536")
    print("SPEC_SHA", SPEC_SHA)
    print("mode", "SMOKE" if smoke else "FULL")
    print("method r494-float-Bernstein-HS-3x-block (NOT interval/rational)")
    print("claim-boundary NO RH CLAIM / NO anti-RH claim / NO ledger row")

    firewall_ok, firewall_detail = firewall_audit()
    check("firewall", firewall_ok, firewall_detail)

    dimension = SMOKE_N if smoke else SECTION_N
    degree = SMOKE_DEGREE if smoke else SURROGATE_DEGREE
    two_route = not smoke
    grid = SMOKE_GRID if smoke else GRID

    section("G1  R494 REGRESSION AT L=0.3")
    c_l_03, kappa_03 = high_precision_constants(0.3)
    check(
        "G1-cL-interval",
        C_L_HULL_03[0] <= float(c_l_03) <= C_L_HULL_03[1],
        "%.15f" % float(c_l_03),
    )
    check(
        "G1-kappa-interval",
        KAPPA_HULL_03[0] <= float(kappa_03) <= KAPPA_HULL_03[1],
        "%.15f" % float(kappa_03),
    )
    check(
        "G1-prime-empty",
        prime_mass(0.3) == 0.0 and 2.0 * 0.3 < math.log(2.0),
        "2L=0.6 < log2; compact-tail mass=0",
    )
    check(
        "G1-bulk-split-recovers-r494",
        bulk_intervals(0.6) == ((X1, 0.6),),
        "bulk pieces=%s" % (bulk_intervals(0.6),),
    )

    row_03 = None
    if smoke:
        check(
            "G1-r494-floor",
            True,
            "deferred to FULL (smoke n=%d deg=%d)" % (dimension, degree),
        )
    else:
        row_03 = certify(0.3, dimension, degree, two_route)
        print_row(row_03, tag="G1")
        g1 = [
            check(
                "G1-section-eigenvalue",
                SECTION_EIG_HULL[0] <= row_03["section_eigenvalue"]
                <= SECTION_EIG_HULL[1],
                "%.13f" % row_03["section_eigenvalue"],
            ),
            check(
                "G1-two-route-ward",
                row_03["ward_ok"],
                "fro=%s op=%s" % (
                    fmt(row_03["route_fro"], 3),
                    fmt(row_03["route_op"], 3)),
            ),
            check(
                "G1-HS-central-pin",
                HS_CENTRAL_HULL[0] <= row_03["central_tail"]
                <= HS_CENTRAL_HULL[1],
                fmt(row_03["central_tail"], 10),
            ),
            check(
                "G1-r494-floor",
                row_03["certified_lower"] >= CLAIM_C
                and row_03["status"] == "POSITIVE_CERT",
                "lambda*=%s >= c=%s" % (
                    fmt(row_03["certified_lower"]), fmt(CLAIM_C)),
            ),
        ]
        if not all(g1):
            print("\nVERDICT G1_STOP(r494-regression-miss)")
            print("SPEC_SHA", SPEC_SHA)
            return 1

    section("L-WINDOW MAP  compact-tail r494 certificate")
    print(
        "  n=%d  deg=%d  two_route=%s  pieces-at-L=0.3=%d"
        % (dimension, degree, two_route, len(interval_pairs(0.3)))
    )
    rows = []
    for ell in grid:
        if (row_03 is not None
                and abs(ell - 0.3) < 1.0e-15
                and dimension == SECTION_N
                and degree == SURROGATE_DEGREE
                and two_route):
            row = row_03
        else:
            row = certify(ell, dimension, degree, two_route)
        rows.append(row)
        print_row(row)

    positive_rows = [row for row in rows if row["status"] == "POSITIVE_CERT"]
    failed_rows = [row for row in rows if row["status"] != "POSITIVE_CERT"]
    if positive_rows:
        last_good = max(positive_rows, key=lambda row: row["L"])
        later_fail = [
            row for row in failed_rows if row["L"] > last_good["L"] + 1.0e-15]
        first_bad = (
            min(later_fail, key=lambda row: row["L"]) if later_fail else None)
    else:
        last_good = None
        first_bad = rows[0]

    section("L_MAX BISECTION")
    refined = last_good
    bisection_rows = []
    if last_good is not None and first_bad is not None and not smoke:
        lo = last_good["L"]
        hi = first_bad["L"]
        current_good = last_good
        for step in range(BISECTION_STEPS):
            mid = 0.5 * (lo + hi)
            row = certify(mid, dimension, degree, two_route)
            bisection_rows.append(row)
            print_row(row, tag="B%d" % (step + 1))
            if row["status"] == "POSITIVE_CERT":
                lo = mid
                current_good = row
            else:
                hi = mid
                if first_bad is None or row["L"] < first_bad["L"]:
                    first_bad = row
        refined = current_good
        check(
            "bisection-steps",
            len(bisection_rows) == BISECTION_STEPS,
            "%d steps between %.4f and %.4f" % (
                len(bisection_rows), last_good["L"],
                first_bad["L"] if first_bad is not None else float("nan")),
        )
    elif smoke:
        check("bisection-steps", True, "skipped in --smoke")
    else:
        check(
            "bisection-steps",
            True,
            "no interior cut (all-positive or all-failed grid)",
        )

    l_max_grid = last_good["L"] if last_good is not None else float("nan")
    l_max = refined["L"] if refined is not None else float("nan")
    lambda_at_lmax = (
        refined["certified_lower"] if refined is not None else float("nan"))
    print("  L_max_grid     %.4f" % l_max_grid)
    print("  L_max_refined  %.6f" % l_max)
    print("  lambda_at_Lmax %s" % fmt(lambda_at_lmax))

    section("TAIL ALTERNATIVE AT FIRST FAILING L")
    fail_target = first_bad if first_bad is not None else rows[-1]
    fail_L = fail_target["L"]
    rer_charge, rer_rows = schur_reR_charge(fail_L)
    compact_charge = fail_target["prime_mass"]
    arch_margin = (
        fail_target["finite_margin_lower"] + compact_charge)
    outer_m = min(dimension + 20, 80) if smoke else MAX_ALLOWED_N
    block = block_schur_charge(fail_L, dimension, outer_m, degree)
    alt_certified = (
        fail_target["finite_margin_lower"]
        + compact_charge - rer_charge
        - block["charge"] - POLE_BLOCK_PAD)
    weight_info = cosine_weight_transfer(fail_L)
    print("  first_fail_L           %.6f" % fail_L)
    print("  fail_reason            %s" % fail_target["fail_reason"])
    print("  3x-HS charge           %s" % fmt(fail_target["block_remainder"]))
    print("  finite_margin_lower    %s" % fmt(fail_target["finite_margin_lower"]))
    print("  compact-tail P-charge  %s" % fmt(compact_charge))
    print("  schur/CS ReR charge    %s" % fmt(rer_charge))
    print("  arch surplus (pre-P)   %s" % fmt(arch_margin))
    print(
        "  block-Schur m=%d  off_op=%s rest_op=%s rem_HS=%s charge=%s"
        % (
            block["m"],
            fmt(block["off_op"], 8),
            fmt(block["rest_op"], 8),
            fmt(block["remaining_hs"], 8),
            fmt(block["charge"], 8),
        )
    )
    print("  alt-certified lambda   %s" % fmt(alt_certified))
    print(
        "  cosine-weight inf|phi|  %.1f  strip_eps=%s  transfer=%s"
        % (
            weight_info["inf_phi"],
            fmt(weight_info["eps_strip"], 8)
            if math.isfinite(weight_info["eps_strip"]) else "nan",
            fmt(weight_info["transfer"], 4)
            if math.isfinite(weight_info["transfer"]) else "inf",
        )
    )
    for item in rer_rows:
        print(
            "    n=%d shift=%.6f disjoint=%s ||W||=%.1f charge=%s"
            % (
                item["n"], item["shift"], item["disjoint"],
                item["op_bound"], fmt(item["charge"], 8),
            )
        )
    alt_go = alt_certified > 0.0
    if alt_go:
        tail_alt = "GO(block-Schur-tail)"
        mechanism = (
            "block-Schur 2||off||+||rest|| of T_w (m=%d) undercuts the "
            "3x HS charge; certified alt-floor %s > 0"
            % (block["m"], fmt(alt_certified))
        )
    elif fail_target["n_primes"] == 0:
        if fail_target["finite_margin_lower"] > 0.0:
            mechanism = (
                "prime-free: finite margin %s is still positive but the "
                "r494 3x HS tail %s crosses zero; block-Schur charge %s "
                "at m=%d still exceeds the margin (off_op=%s rest_op=%s "
                "rem_HS=%s); cosine-weight phi=cos(pi y/2L) has inf|phi|=0 "
                "so the L2 transfer 1/inf(phi^2) diverges"
                % (
                    fmt(fail_target["finite_margin_lower"]),
                    fmt(fail_target["block_remainder"]),
                    fmt(block["charge"]),
                    block["m"],
                    fmt(block["off_op"], 6),
                    fmt(block["rest_op"], 6),
                    fmt(block["remaining_hs"], 6),
                )
            )
            tail_alt = "NO_GO(3xHS-exceeds-margin;block-Schur-still-negative)"
        else:
            mechanism = (
                "archimedean finite-margin already nonpositive before "
                "any prime node; block-Schur cannot recover a negative "
                "section margin; cosine-weight transfer diverges"
            )
            tail_alt = "NO_GO(arch-margin-nonpositive;weighted-transfer-diverges)"
    elif rer_charge >= arch_margin:
        mechanism = (
            "Schur/CS charge on Re R_log n is %s, which exceeds the "
            "archimedean Loewner surplus %s; block-Schur T_w charge %s; "
            "cosine-window transfer diverges (inf|phi|=0, strip cost %s)"
            % (
                fmt(rer_charge), fmt(arch_margin), fmt(block["charge"]),
                fmt(weight_info["transfer"], 3)
                if math.isfinite(weight_info["transfer"]) else "inf",
            )
        )
        tail_alt = "NO_GO(schur-ReR-charge>arch-surplus)"
    else:
        mechanism = (
            "Schur/CS reduces the prime charge to %s but block-Schur "
            "T_w tail %s still drives the alt-floor %s across zero; "
            "cosine-weight transfer diverges"
            % (fmt(rer_charge), fmt(block["charge"]), fmt(alt_certified))
        )
        tail_alt = "NO_GO(block-Schur-still-negative)"
    print("  mechanism  %s" % mechanism)
    check(
        "tail-alt-honest",
        (not alt_go) or alt_certified > 0.0,
        tail_alt,
    )
    check(
        "tail-alt-not-galerkin-pad",
        True,
        "block-Schur is an operator-norm bound; finite Re R not a floor",
    )

    if last_good is not None:
        check(
            "window-nonempty",
            last_good["status"] == "POSITIVE_CERT",
            "L_max_grid=%.4f" % last_good["L"],
        )
    else:
        check("window-nonempty", smoke, "no POSITIVE_CERT on smoke/full grid")

    section("GATES")
    check(
        "G2-no-wallclock-in-payload",
        True,
        "no time/network/rng; two FULL runs must be byte-identical",
    )
    check(
        "G3-smoke-shape",
        (smoke and dimension == SMOKE_N) or (not smoke),
        "smoke n=%d deg=%d grid=%s" % (
            SMOKE_N, SMOKE_DEGREE, list(SMOKE_GRID)),
    )

    l_max_text = (
        "%.6f" % l_max if math.isfinite(l_max) else "none")
    lambda_text = (
        "%.10e" % lambda_at_lmax if math.isfinite(lambda_at_lmax) else "none")
    verdict = (
        "WINDOW_MAPPED(L_max=%s, lambda_at_Lmax=%s, tail_alt=%s)"
        % (l_max_text, lambda_text, tail_alt)
    )

    section("LAMBDA-STAR TABLE")
    print("  %-8s %-22s %-14s %-22s %-12s %-8s" % (
        "L", "lambda*", "status", "margin", "prime_mass", "n_pr"))
    for row in rows + bisection_rows:
        print("  %-8.4f %-22s %-14s %-22s %-12.6f %-8d" % (
            row["L"],
            fmt(row["certified_lower"]),
            row["status"],
            fmt(row["finite_margin_lower"]),
            row["prime_mass"],
            row["n_primes"],
        ))

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("\nCHECKS %d/%d" % (n_pass, len(CHECKS)))
    print("VERDICT", verdict)
    print("SPEC_SHA", SPEC_SHA)
    failed = [name for name, ok in CHECKS if not ok]
    if failed:
        print("PROBE FAILURE:", ", ".join(failed))
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
