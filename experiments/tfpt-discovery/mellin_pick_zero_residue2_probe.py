#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mellin_pick_zero_residue2_probe -- MELLIN.PICK.ZERO-RESIDUE.02

FROZEN SPEC v4 (2026-09-03).  EXPLORATION ONLY.

This standalone probe certifies, or honestly fails to certify, one finite
cell for the entire function and three frozen point evaluations of its
canonical Mellin quotient

    H(z) = 2 M(2z-1) / Gamma(z),
    M(s) = integral_0^infinity Phi(u) u^s du,

where

    Phi(u) = sum_{n>=1}
      (2 pi^2 n^4 exp(9u/2) - 3 pi n^2 exp(5u/2))
      exp(-pi n^2 exp(2u)).

Nothing here is load-bearing.  There is no ledger, paper, Lean, website,
README, or verification claim.  The first-cell certificate concerns only

    B1 = [-5.34,-4.32] + i[-0.25,0.25].

The pointwise Pick kill concerns only the concrete canonical Mellin
interpolant phi defined below.  It does not disprove RH, the KPS theorem,
or every possible alternative Bernstein interpolant.  No zeta-zero
oracle is permitted.

=======================================================================
CANCELLATION-FREE CONTINUATION
=======================================================================
Let A_j = Phi^(2j)(0)/(2j)! and choose

    N(Z) = max(12, ceil(-inf Re Z) + 8).

Then, for p = 2(N + inf Re Z) > 0,

    F(z) = 2 M(2z-1) = sum_{j<N} A_j/(z+j) + R_N(z),

    R_N(z) =
      2 integral_0^1 (Phi(u)-P_N(u)) u^(2z-1) du
      + 2 integral_1^infinity Phi(u) u^(2z-1) du,

    P_N(u) = sum_{j<N} A_j u^(2j).

The direct product H = rgamma * F has removable 0*infinity forms at
negative integers and is never used on contour balls.  Instead

    H(z) = sum_{j<N} A_j E_j(z) + rgamma(z) R_N(z),

    E_j(z) = rgamma(z)/(z+j)
           = product_{k=0}^{j-1}(z+k) rgamma(z+j+1),

is evaluated as an entire function.  Repeated gamma recurrence shifts
the final rgamma argument into a certified right half-plane:

    E_j(z) = product_{0<=k<L, k!=j}(z+k) rgamma(z+L).

All values and derivatives of E_j and rgamma are coefficients of
acb_series([Z,1]); no digamma-times-rgamma expression occurs.

Near z=-j+w, the exact identity

    E_j(-j+w) = (-1)^j j! rgamma(1+w)
                product_{r=1}^j (1-w/r)

gives

    E_j(-j)  = (-1)^j j!,
    E_j'(-j) = (-1)^j j! (EulerGamma-H_j),
    H(-m)    = (-1)^m m! A_m.

The derivative is evaluated only as

    H' = sum A_j E_j' + rgamma' R_N + rgamma R_N'.

For k=0,1,

    R_N^(k)(z) = 2^(k+1) [
      integral_0^1 (Phi-P_N) u^(2z-1) (log u)^k du
      + integral_1^infinity Phi u^(2z-1) (log u)^k du ].

The interval [0,DELTA_LOW] is bounded by a Cauchy Taylor remainder with
p=2(N+inf Re Z).  [DELTA_LOW,1] and [1,U_CUT] use acb.integral.
[U_CUT,infinity) uses the proved Gaussian-power bound copied
mathematically from ZERO-RESIDUE.01.  Every omitted complex tail is a
two-dimensional complex box; only the exact-real Taylor coefficients
may receive a real-only error ball.

=======================================================================
CONTOUR CERTIFICATE
=======================================================================
Each adaptively split contour segment Z is enclosed by

    H(Z) subset H(mid(Z)) + (Z-mid(Z)) H'(Z).

The image ball must exclude zero.  Endpoint ratio balls must avoid the
logarithm cut, and the sum of ball-enclosed argument increments divided
by 2pi must contain one unique integer.  There is no raw phase unwrap.

The independent real certificate uses the inherited continuation
bracket

    eta in [-9.6599319458,-9.6599250793],
    lambda=(eta+1)/2 in
      [-4.3299659729,-4.32996253965].

Opposite endpoint signs plus H' of one sign on the whole lambda bracket
certify one real simple zero.  Winding=1 then proves there is no other
real or nonreal zero in B1.  The unit shift is tested by H(lambda-1),
and the Pick residue is enclosed in the cancellation-free form

    Res phi = 4 H(lambda-1) / H'(lambda).

=======================================================================
FROZEN PICK COUNTERPOINTS
=======================================================================
For q in the upper half-plane, the same function is evaluated by two
algebraically independent forms:

    phi_H(q) = 4 H(q-1/2) / H(q+1/2),

    phi_M(q) = (4q-2) M(2q-2) / M(2q).

The M path uses the literal safe-point continuation

    2M(2z-1) = sum_{j<N} A_j/(z+j) + R_N(z)

without an rgamma factor or an H quotient, and refuses every continuation
denominator ball containing zero.  Exact gamma recurrence gives
phi_H=phi_M.

The frozen points are

    q_bad_1 = -7 + 2i,
    q_bad_2 = -7.5 + 0.25i,
    q_good  = -6.5 + 0.1i.

A negative imaginary upper bound at either bad point, certified by both
forms after denominator exclusion and ball overlap, disproves the Pick
property and hence membership of this concrete phi in BP1.  The positive
control must have a strictly positive imaginary lower bound in both forms.
Midpoints never decide a sign.

=======================================================================
CONTROLS AND VERDICTS
=======================================================================
An exact conjugate-pair polynomial plant is certified on B1 and combined
with the H contour by the exact additive winding law.  Removable-pole
mutants verify that direct rgamma/(z+j) and direct pole-sum products
fail at z=-j while the entire evaluator remains finite.

Smoke uses the same logical box at 256 bits.  Record uses 512 bits.

    FIRST_CELL_CERTIFIED
    KILLED(<rigorously certified violation>)
    INCONCLUSIVE(<first unresolved gate>)

Uncertainty never kills.  A certified contour count greater than one is
INCONCLUSIVE(extra_zero_count_n), not a structural KPS kill: this probe
does not separately classify every extra zero as nonreal, multiple, a
short gap, a shift collision, or a residue violation.  Exact unit-shift
collision and certified nonnegative residue remain genuine kill branches.
A certified zero count of zero is likewise INCONCLUSIVE: it contradicts
the separately forced/root-bracketed local zero but is not itself a KPS
violation.
A clean finite result is still only an experiment-only certificate for
B1 and |Im z| <= 0.25.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

try:
    from flint import acb, acb_series, arb, ctx
except ImportError as exc:
    raise SystemExit(
        "PIPELINE-BROKEN: python-flint is required; run in "
        "experiments/tfpt-discovery/.venv"
    ) from exc


# ---------------------------------------------------------------------------
# Frozen contract
# ---------------------------------------------------------------------------
CONTRACT = "MELLIN.PICK.ZERO-RESIDUE.02"
FENCE = "experiment-only; B1 certificate plus canonical-Mellin Pick counterpoints"
CLAIM_BOUNDARY = (
    "B1 certificate plus canonical Mellin phi only; PICK_SIGN disproves "
    "Pick/BP1 membership for this phi, not RH, KPS, or every alternative "
    "Bernstein interpolant"
)

CAUCHY_RADIUS = "0.5"
DELTA_LOW = "0.08"
U_CUT = "2.2"
MIN_TAYLOR_ORDER = 12
TAYLOR_MARGIN = 8
PHI_N_MAX = 16
PHI_N_SERIES = 26

TARGET_RE_LO = "-5.34"
TARGET_RE_HI = "-4.32"
TARGET_IM_LO = "-0.25"
TARGET_IM_HI = "0.25"

ETA_LO = "-9.6599319458"
ETA_HI = "-9.6599250793"
LAMBDA_LO = "-4.3299659729"
LAMBDA_HI = "-4.32996253965"

SMOKE_BITS = 256
RECORD_BITS = 512
SMOKE_MAX_SEGMENTS = 1400
RECORD_MAX_SEGMENTS = 3200
MAX_REFINE_DEPTH = 20
MIN_SEGMENT = "0.00020"
INTEGRAL_EVAL_LIMIT = 6000
INTEGRAL_DEPTH_LIMIT = 24
INTEGRAL_TOL_BITS = 128

PLANT_A = "-4.80"
PLANT_B = "0.12"

ANCHOR_PHI0 = "0.446696900467"
ANCHOR_RADIUS = "5e-13"
SAFE_CALIBRATION_POINTS = (
    ("positive", "0.75", "0.20"),
    ("target-side", "-4.75", "0.125"),
)
Q_BAD_1 = ("q_bad_1", "-7", "2")
Q_BAD_2 = ("q_bad_2", "-7.5", "0.25")
Q_GOOD = ("q_good", "-6.5", "0.1")

BANNED_IDENTIFIERS = (
    "zetazero",
    "zetazeros",
    "zeta_zero",
    "zeta_zeros",
    "nzeros",
    "find_zeros",
    "zeta_nzeros",
    "backlund_s",
    "digamma",
    "unwrap",
)
VERDICT_SEMANTICS = "canonical_pick_two_path_counterpoints_v4"

FROZEN_NUMERICAL_SPEC = (
    CONTRACT,
    CAUCHY_RADIUS,
    DELTA_LOW,
    U_CUT,
    MIN_TAYLOR_ORDER,
    TAYLOR_MARGIN,
    PHI_N_MAX,
    PHI_N_SERIES,
    TARGET_RE_LO,
    TARGET_RE_HI,
    TARGET_IM_LO,
    TARGET_IM_HI,
    ETA_LO,
    ETA_HI,
    SMOKE_BITS,
    RECORD_BITS,
    VERDICT_SEMANTICS,
    Q_BAD_1,
    Q_BAD_2,
    Q_GOOD,
)
SPEC_SHA = hashlib.sha256(repr(FROZEN_NUMERICAL_SPEC).encode("utf-8")).hexdigest()


WORKING_BITS = SMOKE_BITS
MAX_SEGMENTS = SMOKE_MAX_SEGMENTS
CHECKS: list[tuple[str, bool]] = []
MAIN_GATES: list["MainGate"] = []
T0 = 0.0

_TAYLOR_CACHE: dict[int, list[acb]] = {}
_PHI_DISK_BOUND_CACHE: dict[int, arb] = {}
_N_TAIL_CAUCHY_CACHE: dict[int, list[arb]] = {}
_SERIES_CAP_USED: dict[int, int] = {}
_R_CACHE: dict[tuple[str, int, int, int], "RParts"] = {}
_JET_CACHE: dict[tuple[str, int, int], "JetBundle"] = {}
_H_CACHE: dict[tuple[str, int], acb] = {}
_HP_CACHE: dict[tuple[str, int], acb] = {}


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def check(name: str, ok: bool, detail: str = "") -> bool:
    passed = bool(ok)
    CHECKS.append((name, passed))
    suffix = "  -- " + detail if detail else ""
    print("  [%s] %s%s" % ("PASS" if passed else "FAIL", name, suffix), flush=True)
    return passed


@dataclass
class MainGate:
    name: str
    status: str  # pass | killed | inconclusive
    reason: str
    detail: str = ""


def main_gate(name: str, status: str, reason: str, detail: str = "") -> MainGate:
    if status not in ("pass", "killed", "inconclusive"):
        raise ValueError("illegal main-gate status")
    row = MainGate(name, status, reason, detail)
    MAIN_GATES.append(row)
    label = {"pass": "PASS", "killed": "KILLED", "inconclusive": "INCONCLUSIVE"}[status]
    suffix = "  -- " + detail if detail else ""
    print("  [%s] %s: %s%s" % (label, name, reason, suffix), flush=True)
    return row


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def configure(*, smoke: bool) -> None:
    global WORKING_BITS, MAX_SEGMENTS
    WORKING_BITS = SMOKE_BITS if smoke else RECORD_BITS
    MAX_SEGMENTS = SMOKE_MAX_SEGMENTS if smoke else RECORD_MAX_SEGMENTS
    ctx.prec = WORKING_BITS
    ctx.cap = 2
    CHECKS.clear()
    MAIN_GATES.clear()
    _TAYLOR_CACHE.clear()
    _PHI_DISK_BOUND_CACHE.clear()
    _N_TAIL_CAUCHY_CACHE.clear()
    _SERIES_CAP_USED.clear()
    _R_CACHE.clear()
    _JET_CACHE.clear()
    _H_CACHE.clear()
    _HP_CACHE.clear()


def ast_firewall() -> list[str]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    banned = set(BANNED_IDENTIFIERS)
    issues: list[str] = []

    for node in ast.walk(tree):
        identifier = None
        if isinstance(node, ast.Name):
            identifier = node.id
        elif isinstance(node, ast.Attribute):
            identifier = node.attr
        if identifier in banned:
            issues.append("banned_identifier:" + identifier)
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            module = getattr(node, "module", "") or ""
            names = [alias.name for alias in node.names]
            joined = ",".join([module] + names)
            if "mellin_pick_zero_residue_probe" in joined:
                issues.append("sibling_import:" + joined)

    allowed_direct_callers = {"run_calibrations"}
    allowed_mutant_callers = {"run"}
    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for child in ast.walk(node):
            if not isinstance(child, ast.Call):
                continue
            called = child.func.id if isinstance(child.func, ast.Name) else ""
            if called == "calibration_direct_H" and node.name not in allowed_direct_callers:
                issues.append("direct_H_outside_calibration:" + node.name)
            if called.startswith("mutant_direct_") and node.name not in allowed_mutant_callers:
                issues.append("mutant_outside_run:" + node.name)
    return sorted(set(issues))


# ---------------------------------------------------------------------------
# Ball helpers
# ---------------------------------------------------------------------------
def point(re: str | int, im: str | int = 0) -> acb:
    return acb(str(re), str(im))


def real_interval(lo: str, hi: str) -> arb:
    return arb(lo).union(arb(hi))


def target_box() -> acb:
    return acb(
        real_interval(TARGET_RE_LO, TARGET_RE_HI),
        real_interval(TARGET_IM_LO, TARGET_IM_HI),
    )


def finite(z: acb) -> bool:
    return bool(z.is_finite())


def contains_zero(z: acb) -> bool:
    return bool(z.contains(0))


def certainly_positive(x: arb) -> bool:
    return bool(x > 0)


def certainly_negative(x: arb) -> bool:
    return bool(x < 0)


def certainly_nonnegative(x: arb) -> bool:
    return bool(x.lower() >= 0)


def complex_error_box(radius: arb) -> acb:
    """Square [-R,R]+i[-R,R], not a real-only error interval."""
    return acb(arb(0, radius), arb(0, radius))


def real_error_ball(radius: arb) -> acb:
    """Allowed only for coefficients known a priori to be real."""
    return acb(arb(0, radius), arb(0))


def ball_from_segment(p: acb, q: acb) -> acb:
    return acb(p.real.union(q.real), p.imag.union(q.imag))


def arb_ceil_int(x: arb) -> int:
    """Use Arb for the rounding decision, then convert the exact integer."""
    return int(float(x.ceil()))


def dynamic_order(z: acb) -> int:
    needed = arb_ceil_int(-z.real.lower()) + TAYLOR_MARGIN
    return max(MIN_TAYLOR_ORDER, needed)


def recurrence_shift(z: acb, n: int) -> int:
    """L >= n with inf Re(z+L) >= 3, keeping rgamma away from poles."""
    return max(n, arb_ceil_int(-z.real.lower()) + 4)


def safe_log(u: acb, analytic: bool) -> acb:
    del analytic
    if not finite(u):
        return acb("nan")
    if u.imag.contains(0) and not certainly_positive(u.real):
        return acb("nan")
    return u.log()


# ---------------------------------------------------------------------------
# Phi and proved theta n-tail
# ---------------------------------------------------------------------------
def _pi() -> acb:
    return acb.pi()


def phi_term(u: acb | acb_series, n: int) -> acb | acb_series:
    nn = acb(n)
    n2 = nn * nn
    pi = _pi()
    e2 = (u * acb(2)).exp()
    e5 = (u * acb("2.5")).exp()
    e9 = (u * acb("4.5")).exp()
    return (
        acb(2) * pi * pi * n2 * n2 * e9 - acb(3) * pi * n2 * e5
    ) * ((-pi * n2 * e2).exp())


def _monotonic_start(k: int, c: arb, n_min: int) -> int | None:
    if not certainly_positive(c):
        return None
    m = max(1, n_min)
    for _ in range(100000):
        if arb(2) * c * arb(m * m) > arb(k):
            return m
        m += 1
    return None


def gaussian_power_tail(k: int, c: arb, n0: int) -> arb:
    r"""Certified bound for sum_{n=n0}^infinity n^k exp(-c n^2)."""
    if k not in (2, 4):
        return arb("inf")
    m = _monotonic_start(k, c, n0)
    if m is None:
        return arb("inf")
    total = arb(0)
    for n in range(max(1, n0), m):
        total += (arb(n) ** k) * ((-c * arb(n * n)).exp())
    cm2 = c * arb(m * m)
    shape = arb(k + 1) / arb(2)
    head = (arb(m) ** k) * ((-cm2).exp())
    tail_integral = arb("0.5") * (c ** (-shape)) * cm2.gamma_upper(shape)
    out = total + head + tail_integral
    return out if out.is_finite() else arb("inf")


def phi_n_tail_abs(n0: int, re_exp2_lower: arb, abs_u_upper: arb) -> arb:
    if not certainly_positive(re_exp2_lower):
        return arb("inf")
    c = arb.pi() * re_exp2_lower
    tail4 = gaussian_power_tail(4, c, n0)
    tail2 = gaussian_power_tail(2, c, n0)
    grow9 = (arb("4.5") * abs_u_upper).exp()
    grow5 = (arb("2.5") * abs_u_upper).exp()
    out = (
        arb(2) * arb.pi() * arb.pi() * grow9 * tail4
        + arb(3) * arb.pi() * grow5 * tail2
    )
    return out if out.is_finite() else arb("inf")


def phi_ball(u: acb, analytic: bool = False) -> acb:
    del analytic
    if not finite(u):
        return acb("nan")
    total = acb(0)
    for n in range(1, PHI_N_MAX + 1):
        total += phi_term(u, n)
        if not finite(total):
            return acb("nan")
    exp2u = (u * acb(2)).exp()
    tail = phi_n_tail_abs(PHI_N_MAX + 1, exp2u.real.lower(), u.abs_upper())
    if not tail.is_finite():
        return acb("nan")
    return total + complex_error_box(tail)


def _re_exp2u_disk_lower(radius: arb) -> arb:
    """Lower bound for Re exp(2u) on |u|<=radius<pi/4."""
    return ((-arb(2) * radius).exp()) * (arb(2) * radius).cos()


def _term_prefactor_abs_bound(n: int, radius: arb) -> arb:
    n2 = arb(n * n)
    n4 = n2 * n2
    return (
        arb(2)
        * arb.pi()
        * arb.pi()
        * n4
        * (arb("4.5") * radius).exp()
        + arb(3) * arb.pi() * n2 * (arb("2.5") * radius).exp()
    )


def _disk_phi_abs_bound(radius: arb) -> arb:
    re_lower = _re_exp2u_disk_lower(radius)
    if not certainly_positive(re_lower):
        return arb("inf")
    c = arb.pi() * re_lower
    total = arb(0)
    for n in range(1, PHI_N_SERIES + 1):
        total += _term_prefactor_abs_bound(n, radius) * (
            -c * arb(n * n)
        ).exp()
    total += phi_n_tail_abs(PHI_N_SERIES + 1, re_lower, radius)
    return total if total.is_finite() else arb("inf")


def _n_tail_cauchy_bounds(n_terms: int, radius: arb) -> list[arb]:
    re_lower = _re_exp2u_disk_lower(radius)
    source_tail = phi_n_tail_abs(PHI_N_SERIES + 1, re_lower, radius)
    return [source_tail / (radius ** (2 * j)) for j in range(n_terms)]


def taylor_even_coeffs(n_terms: int) -> list[acb]:
    """Certified A_j, including the omitted theta n-tail by Cauchy."""
    if n_terms in _TAYLOR_CACHE:
        return _TAYLOR_CACHE[n_terms]
    radius = arb(CAUCHY_RADIUS)
    series_cap = 2 * n_terms + 2
    old_cap = ctx.cap
    try:
        ctx.cap = series_cap
        u = acb_series([0, 1])
        series = acb_series([0])
        for n in range(1, PHI_N_SERIES + 1):
            series += phi_term(u, n)
        raw = series.coeffs()
    finally:
        ctx.cap = old_cap

    theta_bounds = _n_tail_cauchy_bounds(n_terms, radius)
    coeffs: list[acb] = []
    for j in range(n_terms):
        degree = 2 * j
        if degree >= len(raw):
            raise RuntimeError("Taylor series cap did not reach degree %d" % degree)
        coeffs.append(raw[degree] + real_error_ball(theta_bounds[j]))

    _TAYLOR_CACHE[n_terms] = coeffs
    _PHI_DISK_BOUND_CACHE[n_terms] = _disk_phi_abs_bound(radius)
    _N_TAIL_CAUCHY_CACHE[n_terms] = theta_bounds
    _SERIES_CAP_USED[n_terms] = series_cap
    return coeffs


def taylor_poly(u: acb, coeffs: list[acb]) -> acb:
    u2 = u * u
    power = acb(1)
    total = acb(0)
    for coefficient in coeffs:
        total += coefficient * power
        power *= u2
    return total


# ---------------------------------------------------------------------------
# R_N and R_N' with explicit low/mid/high boxes
# ---------------------------------------------------------------------------
def _power_log_integral(delta: arb, p: arb, derivative: int) -> arb:
    r"""Integral_0^delta u^(p-1) |log u|^derivative du."""
    if not certainly_positive(p):
        return arb("inf")
    log_delta = delta.log()
    delta_p = delta ** p
    if derivative == 0:
        return delta_p / p
    if derivative == 1:
        return delta_p * ((-log_delta) / p + arb(1) / (p * p))
    return arb("inf")


def low_remainder_box(z: acb, n_terms: int, derivative: int) -> acb:
    """Box for the omitted [0,DELTA_LOW] part of R_N^(derivative)."""
    taylor_even_coeffs(n_terms)
    radius = arb(CAUCHY_RADIUS)
    delta = arb(DELTA_LOW)
    ratio = delta / radius
    if not (ratio < 1):
        return acb("nan")
    disk_bound = _PHI_DISK_BOUND_CACHE[n_terms]
    tail_at_delta = (
        disk_bound
        * (ratio ** (2 * n_terms))
        / (arb(1) - ratio)
    )
    coefficient_on_u_2n = tail_at_delta / (delta ** (2 * n_terms))
    p = arb(2 * n_terms) + arb(2) * z.real.lower()
    integral = _power_log_integral(delta, p, derivative)
    if not integral.is_finite():
        return acb("nan")
    factor = arb(2) ** (derivative + 1)
    return complex_error_box(factor * coefficient_on_u_2n * integral)


def high_mellin_tail_box(s: acb, derivative: int) -> acb:
    """Box for integral_U^infinity Phi(u)u^s(log u)^derivative du."""
    u_cut = arb(U_CUT)
    if not (u_cut >= 1):
        return acb("nan")
    q = s.real.upper().max(arb(0)) + arb(derivative)
    a_decay = arb.pi() * (arb(2) * u_cut).exp()
    den4 = arb(2) * a_decay - arb("4.5") - q / u_cut
    den2 = arb(2) * a_decay - arb("2.5") - q / u_cut
    if not certainly_positive(den4) or not certainly_positive(den2):
        return acb("nan")
    sum4 = gaussian_power_tail(4, a_decay, 1)
    sum2 = gaussian_power_tail(2, a_decay, 1)
    u_power = u_cut ** q
    term4 = (
        arb(2)
        * arb.pi()
        * arb.pi()
        * u_power
        * (arb("4.5") * u_cut).exp()
        * sum4
        / den4
    )
    term2 = (
        arb(3)
        * arb.pi()
        * u_power
        * (arb("2.5") * u_cut).exp()
        * sum2
        / den2
    )
    total = term4 + term2
    return complex_error_box(total) if total.is_finite() else acb("nan")


@dataclass
class RParts:
    n_terms: int
    derivative: int
    low: acb
    mid: acb
    high_finite: acb
    high_tail: acb
    total: acb
    reason: str = ""

    @property
    def ok(self) -> bool:
        return all(
            finite(value)
            for value in (self.low, self.mid, self.high_finite, self.high_tail, self.total)
        )


def _nan_rparts(n_terms: int, derivative: int, reason: str) -> RParts:
    nan = acb("nan")
    return RParts(n_terms, derivative, nan, nan, nan, nan, nan, reason)


def _remainder_integrand(
    u: acb,
    analytic: bool,
    z: acb,
    derivative: int,
    subtract_taylor: bool,
    coeffs: list[acb],
) -> acb:
    phi = phi_ball(u, analytic)
    if not finite(phi):
        return acb("nan")
    source = phi - taylor_poly(u, coeffs) if subtract_taylor else phi
    log_u = safe_log(u, analytic)
    if not finite(log_u):
        return acb("nan")
    s = acb(2) * z - acb(1)
    power = (s * log_u).exp()
    if not finite(power):
        return acb("nan")
    out = source * power
    if derivative == 1:
        out *= log_u
    return out


def eval_R(z: acb, derivative: int) -> RParts:
    if derivative not in (0, 1) or not finite(z):
        return _nan_rparts(0, derivative, "invalid_input")
    n_terms = dynamic_order(z)
    key = (str(z), derivative, n_terms, WORKING_BITS)
    if key in _R_CACHE:
        return _R_CACHE[key]
    coeffs = taylor_even_coeffs(n_terms)

    def mid_integrand(u: acb, analytic: bool) -> acb:
        return _remainder_integrand(
            u, analytic, z, derivative, True, coeffs
        )

    def high_integrand(u: acb, analytic: bool) -> acb:
        return _remainder_integrand(
            u, analytic, z, derivative, False, coeffs
        )

    tolerance = arb(2) ** -min(INTEGRAL_TOL_BITS, WORKING_BITS - 32)
    try:
        mid = acb.integral(
            mid_integrand,
            acb(DELTA_LOW),
            acb(1),
            abs_tol=tolerance,
            eval_limit=INTEGRAL_EVAL_LIMIT,
            depth_limit=INTEGRAL_DEPTH_LIMIT,
        )
        high_finite = acb.integral(
            high_integrand,
            acb(1),
            acb(U_CUT),
            abs_tol=tolerance,
            eval_limit=INTEGRAL_EVAL_LIMIT,
            depth_limit=INTEGRAL_DEPTH_LIMIT,
        )
    except Exception as exc:
        result = _nan_rparts(n_terms, derivative, "integral_exception:%s" % type(exc).__name__)
        _R_CACHE[key] = result
        return result

    low = low_remainder_box(z, n_terms, derivative)
    s = acb(2) * z - acb(1)
    high_tail = high_mellin_tail_box(s, derivative)
    factor = acb(2 ** (derivative + 1))
    mid_scaled = factor * mid
    high_finite_scaled = factor * high_finite
    high_tail_scaled = factor * high_tail
    total = low + mid_scaled + high_finite_scaled + high_tail_scaled
    reason = "" if all(
        finite(value)
        for value in (low, mid_scaled, high_finite_scaled, high_tail_scaled, total)
    ) else "nonfinite_component"
    result = RParts(
        n_terms,
        derivative,
        low,
        mid_scaled,
        high_finite_scaled,
        high_tail_scaled,
        total,
        reason,
    )
    _R_CACHE[key] = result
    return result


# ---------------------------------------------------------------------------
# Entire E_j, rgamma, H and H'
# ---------------------------------------------------------------------------
@dataclass
class JetBundle:
    source_value: acb
    source_prime: acb
    rgamma_value: acb
    rgamma_prime: acb
    shift: int


def _prefix_suffix_products(
    z: acb, n_terms: int
) -> tuple[list[acb_series], list[acb_series], acb_series, int]:
    ctx.cap = 2
    shift = recurrence_shift(z, n_terms)
    variable = acb_series([z, 1])
    factors = [variable + acb(k) for k in range(shift)]
    prefix = [acb_series([1])]
    for factor in factors:
        prefix.append(prefix[-1] * factor)
    suffix = [acb_series([1]) for _ in range(shift + 1)]
    for k in range(shift - 1, -1, -1):
        suffix[k] = factors[k] * suffix[k + 1]
    shifted_rgamma = (variable + acb(shift)).rgamma()
    return prefix, suffix, shifted_rgamma, shift


def source_gamma_jet(z: acb, coeffs: list[acb]) -> JetBundle:
    n_terms = len(coeffs)
    key = (str(z), n_terms, WORKING_BITS)
    if key in _JET_CACHE:
        return _JET_CACHE[key]
    prefix, suffix, shifted_rgamma, shift = _prefix_suffix_products(z, n_terms)
    source_polynomial = acb_series([0])
    for j, coefficient in enumerate(coeffs):
        exclusion = prefix[j] * suffix[j + 1]
        source_polynomial += coefficient * exclusion
    source = shifted_rgamma * source_polynomial
    gamma_series = shifted_rgamma * prefix[shift]
    bundle = JetBundle(
        source[0],
        source[1],
        gamma_series[0],
        gamma_series[1],
        shift,
    )
    _JET_CACHE[key] = bundle
    return bundle


def entire_E_jet(z: acb, j: int) -> tuple[acb, acb]:
    if j < 0:
        return acb("nan"), acb("nan")
    prefix, suffix, shifted_rgamma, _shift = _prefix_suffix_products(z, j + 1)
    series = shifted_rgamma * prefix[j] * suffix[j + 1]
    return series[0], series[1]


def eval_H(z: acb) -> acb:
    key = (str(z), WORKING_BITS)
    if key in _H_CACHE:
        return _H_CACHE[key]
    if not finite(z):
        return acb("nan")
    n_terms = dynamic_order(z)
    coeffs = taylor_even_coeffs(n_terms)
    jet = source_gamma_jet(z, coeffs)
    remainder = eval_R(z, 0)
    if not remainder.ok:
        value = acb("nan")
    else:
        value = jet.source_value + jet.rgamma_value * remainder.total
        if not finite(value):
            value = acb("nan")
    _H_CACHE[key] = value
    return value


def eval_H_prime(z: acb) -> acb:
    key = (str(z), WORKING_BITS)
    if key in _HP_CACHE:
        return _HP_CACHE[key]
    if not finite(z):
        return acb("nan")
    n_terms = dynamic_order(z)
    coeffs = taylor_even_coeffs(n_terms)
    jet = source_gamma_jet(z, coeffs)
    remainder = eval_R(z, 0)
    remainder_prime = eval_R(z, 1)
    if not remainder.ok or not remainder_prime.ok:
        value = acb("nan")
    else:
        value = (
            jet.source_prime
            + jet.rgamma_prime * remainder.total
            + jet.rgamma_value * remainder_prime.total
        )
        if not finite(value):
            value = acb("nan")
    _HP_CACHE[key] = value
    return value


@dataclass
class DirectContinuation:
    value: acb
    n_terms: int
    denominators_exclude_zero: bool
    reason: str

    @property
    def ok(self) -> bool:
        return (
            finite(self.value)
            and self.denominators_exclude_zero
            and self.reason == "certified"
        )


def eval_F_direct(z: acb) -> DirectContinuation:
    """Literal F=sum A_j/(z+j)+R_N at a safe non-pole complex z."""
    n_terms = dynamic_order(z)
    coeffs = taylor_even_coeffs(n_terms)
    remainder = eval_R(z, 0)
    if not remainder.ok:
        return DirectContinuation(
            acb("nan"), n_terms, False, "remainder_" + remainder.reason
        )
    direct_f = remainder.total
    for j, coefficient in enumerate(coeffs):
        denominator = z + acb(j)
        if contains_zero(denominator):
            return DirectContinuation(
                acb("nan"), n_terms, False, "continuation_denominator_%d" % j
            )
        direct_f += coefficient / denominator
    if not finite(direct_f):
        return DirectContinuation(acb("nan"), n_terms, True, "nonfinite_sum")
    return DirectContinuation(direct_f, n_terms, True, "certified")


def eval_M_direct(s: acb) -> DirectContinuation:
    """M(s) from the literal continuation, with no rgamma or H quotient."""
    z = (s + acb(1)) / acb(2)
    direct_f = eval_F_direct(z)
    if not direct_f.ok:
        return direct_f
    return DirectContinuation(
        direct_f.value / acb(2),
        direct_f.n_terms,
        True,
        "certified",
    )


def calibration_direct_H(z: acb) -> acb:
    """Direct 2M(2z-1)*rgamma(z), for safe noninteger points only."""
    direct_f = eval_F_direct(z)
    if not direct_f.ok:
        return acb("nan")
    value = z.rgamma() * direct_f.value
    return value if finite(value) else acb("nan")


def mutant_direct_E_at_pole(j: int) -> acb:
    z = acb(-j)
    try:
        return z.rgamma() / (z + acb(j))
    except Exception:
        return acb("nan")


def mutant_direct_H_at_pole(j: int, coeffs: list[acb]) -> acb:
    z = acb(-j)
    direct_f = acb(0)
    try:
        for k, coefficient in enumerate(coeffs):
            direct_f += coefficient / (z + acb(k))
        return z.rgamma() * direct_f
    except Exception:
        return acb("nan")


# ---------------------------------------------------------------------------
# Exact symbolic derivation gates
# ---------------------------------------------------------------------------
def symbolic_derivation_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp

    z, w, u = sp.symbols("z w u")
    gates: list[tuple[str, bool, str]] = []

    near_ok = True
    derivative_ok = True
    for j in range(0, 8):
        canonical_polynomial = sp.sympify(sp.prod(z + k for k in range(j)))
        near_polynomial = (
            (-1) ** j
            * sp.factorial(j)
            * sp.prod(1 - w / sp.Integer(r) for r in range(1, j + 1))
        )
        near_ok = near_ok and (
            sp.simplify(canonical_polynomial.subs(z, -j + w) - near_polynomial)
            == 0
        )
        near_e = near_polynomial / sp.gamma(1 + w)
        expected_prime = (
            (-1) ** j
            * sp.factorial(j)
            * (sp.EulerGamma - sp.harmonic(j))
        )
        derivative_ok = derivative_ok and (
            sp.simplify(sp.diff(near_e, w).subs(w, 0) - expected_prime) == 0
        )
    gates.append(
        (
            "symbolic near-pole E_j identity",
            near_ok,
            "j=0..7 exact polynomial identity",
        )
    )
    gates.append(
        (
            "symbolic E_j'(-j) identity",
            derivative_ok,
            "(-1)^j j!(EulerGamma-H_j), j=0..7",
        )
    )

    shift_ok = True
    g = sp.Symbol("G")
    for j in range(0, 7):
        for shift in (8, 11):
            canonical_shifted = (
                sp.prod(z + k for k in range(j))
                * sp.prod(z + k for k in range(j + 1, shift))
                * g
            )
            exclusion = sp.prod(z + k for k in range(shift) if k != j) * g
            shift_ok = shift_ok and (
                sp.expand(canonical_shifted - exclusion) == 0
            )
    gates.append(
        (
            "symbolic shifted-rgamma recurrence",
            shift_ok,
            "canonical E_j equals exclusion product",
        )
    )

    factor_ok = True
    kernel = 2 * u ** (2 * z - 1)
    for derivative in (0, 1):
        expected = (
            2 ** (derivative + 1)
            * u ** (2 * z - 1)
            * sp.log(u) ** derivative
        )
        factor_ok = factor_ok and (
            sp.simplify(sp.diff(kernel, z, derivative) - expected) == 0
        )
    gates.append(
        (
            "symbolic R_N derivative factors",
            factor_ok,
            "2^(k+1), k=0,1",
        )
    )

    pole_ok = True
    shift = 10
    for m in range(0, 7):
        gamma_at_shift = sp.Rational(1, sp.factorial(shift - m - 1))
        for j in range(0, 8):
            value = (
                sp.prod((-m + k) for k in range(shift) if k != j)
                * gamma_at_shift
            )
            expected = (-1) ** m * sp.factorial(m) if j == m else 0
            pole_ok = pole_ok and (sp.simplify(value - expected) == 0)
        rgamma_value = (
            sp.prod((-m + k) for k in range(shift)) * gamma_at_shift
        )
        pole_ok = pole_ok and (rgamma_value == 0)
    gates.append(
        (
            "symbolic H(-m) selector",
            pole_ok,
            "only E_m survives, m=0..6",
        )
    )

    lam, h_shift, h_prime, gamma_prev = sp.symbols(
        "lambda Hshift Hprime GammaPrev", nonzero=True
    )
    eta = 2 * lam - 1
    m_shift = gamma_prev * h_shift / 2
    m_prime = ((lam - 1) * gamma_prev) * h_prime / 4
    old_residue = (eta - 1) * m_shift / m_prime
    residue_ok = sp.simplify(old_residue - 4 * h_shift / h_prime) == 0
    gates.append(
        (
            "symbolic residue conversion",
            residue_ok,
            "(eta-1)M(eta-2)/M'(eta)=4H(lambda-1)/H'(lambda)",
        )
    )

    qsym, m_num, m_den, gamma_lower = sp.symbols(
        "q Mnum Mden GammaLower", nonzero=True
    )
    h_lower = 2 * m_num / gamma_lower
    h_upper = 2 * m_den / ((qsym - sp.Rational(1, 2)) * gamma_lower)
    phi_h = 4 * h_lower / h_upper
    phi_m = (4 * qsym - 2) * m_num / m_den
    pick_identity_ok = sp.simplify(phi_h - phi_m) == 0
    gates.append(
        (
            "symbolic H/M Pick quotient identity",
            pick_identity_ok,
            "4H(q-1/2)/H(q+1/2)=(4q-2)M(2q-2)/M(2q)",
        )
    )

    f, q = sp.symbols("f q", nonzero=True)
    fp, qp = sp.symbols("fp qp")
    additive_ok = sp.simplify((fp * q + f * qp) / (f * q) - fp / f - qp / q) == 0
    gates.append(
        (
            "symbolic planted-product winding additivity",
            additive_ok,
            "(Hq)'/(Hq)=H'/H+q'/q",
        )
    )
    return gates


# ---------------------------------------------------------------------------
# Certified adaptive winding
# ---------------------------------------------------------------------------
@dataclass
class ImageEnclosure:
    ok: bool
    ball: acb
    midpoint_value: acb
    reason: str = ""


@dataclass
class CertifiedSegment:
    start: acb
    end: acb
    start_value: acb
    end_value: acb
    image: acb
    darg: arb


@dataclass
class WindingResult:
    status: str
    number: int | None
    reason: str
    segments: list[CertifiedSegment] = field(default_factory=list)
    attempts: int = 0
    winding_ball: arb | None = None


def enclose_image(
    function: Callable[[acb], acb],
    derivative: Callable[[acb], acb],
    start: acb,
    end: acb,
) -> ImageEnclosure:
    hull = ball_from_segment(start, end)
    midpoint = (start + end) / acb(2)
    midpoint_value = function(midpoint)
    if not finite(midpoint_value):
        return ImageEnclosure(False, acb("nan"), midpoint_value, "midpoint_nonfinite")
    derivative_hull = derivative(hull)
    if not finite(derivative_hull):
        return ImageEnclosure(False, acb("nan"), midpoint_value, "derivative_nonfinite")
    enclosure = midpoint_value + (hull - midpoint) * derivative_hull
    if not finite(enclosure):
        return ImageEnclosure(False, acb("nan"), midpoint_value, "image_nonfinite")
    return ImageEnclosure(True, enclosure, midpoint_value)


def darg_ratio(start_value: acb, end_value: acb) -> arb | None:
    if contains_zero(start_value) or contains_zero(end_value):
        return None
    ratio = end_value / start_value
    if not finite(ratio) or contains_zero(ratio):
        return None
    if ratio.imag.contains(0) and not certainly_positive(ratio.real):
        return None
    logarithm = ratio.log()
    if not finite(logarithm):
        return None
    return logarithm.imag


def winding_rectangle(
    function: Callable[[acb], acb],
    derivative: Callable[[acb], acb],
    re_lo: str,
    re_hi: str,
    im_lo: str,
    im_hi: str,
) -> WindingResult:
    corners = (
        point(re_lo, im_lo),
        point(re_hi, im_lo),
        point(re_hi, im_hi),
        point(re_lo, im_hi),
        point(re_lo, im_lo),
    )
    accepted: list[CertifiedSegment] = []
    attempts = 0

    def refine(start: acb, end: acb, depth: int) -> str | None:
        nonlocal attempts
        attempts += 1
        if len(accepted) >= MAX_SEGMENTS:
            return "max_segments"
        image = enclose_image(function, derivative, start, end)
        start_value = function(start)
        end_value = function(end)
        increment = (
            darg_ratio(start_value, end_value)
            if finite(start_value) and finite(end_value)
            else None
        )
        valid = (
            image.ok
            and not contains_zero(image.ball)
            and increment is not None
        )
        if valid:
            accepted.append(
                CertifiedSegment(
                    start,
                    end,
                    start_value,
                    end_value,
                    image.ball,
                    increment,
                )
            )
            return None

        length = (end - start).abs_upper()
        if depth >= MAX_REFINE_DEPTH or length <= arb(MIN_SEGMENT):
            if not image.ok:
                return image.reason
            if contains_zero(image.ball):
                return "zero_in_image_enclosure"
            return "endpoint_ratio_branch"
        midpoint = (start + end) / acb(2)
        return refine(start, midpoint, depth + 1) or refine(
            midpoint, end, depth + 1
        )

    for edge in range(4):
        error = refine(corners[edge], corners[edge + 1], 0)
        if error:
            return WindingResult(
                "inconclusive", None, error, accepted, attempts, None
            )

    total_argument = arb(0)
    for segment in accepted:
        total_argument += segment.darg
    winding_ball = total_argument / (arb(2) * arb.pi())
    unique = winding_ball.unique_fmpz()
    if unique is None:
        return WindingResult(
            "inconclusive",
            None,
            "winding_not_unique",
            accepted,
            attempts,
            winding_ball,
        )
    return WindingResult(
        "ok",
        int(unique),
        "certified",
        accepted,
        attempts,
        winding_ball,
    )


# ---------------------------------------------------------------------------
# Real root, shift, residue, and plants
# ---------------------------------------------------------------------------
@dataclass
class RealRootCertificate:
    status: str
    reason: str
    bracket: arb
    left_value: acb
    right_value: acb
    derivative: acb


def opposite_real_sign(left: acb, right: acb) -> bool:
    return (
        certainly_positive(left.real) and certainly_negative(right.real)
    ) or (
        certainly_negative(left.real) and certainly_positive(right.real)
    )


def isolate_known_real_root() -> RealRootCertificate:
    bracket = real_interval(LAMBDA_LO, LAMBDA_HI)
    left = eval_H(acb(arb(LAMBDA_LO)))
    right = eval_H(acb(arb(LAMBDA_HI)))
    derivative = eval_H_prime(acb(bracket))
    if not finite(left) or not finite(right):
        return RealRootCertificate(
            "inconclusive", "endpoint_nonfinite", bracket, left, right, derivative
        )
    if not finite(derivative):
        return RealRootCertificate(
            "inconclusive", "derivative_nonfinite", bracket, left, right, derivative
        )
    if not opposite_real_sign(left, right):
        return RealRootCertificate(
            "inconclusive", "endpoint_sign_unresolved", bracket, left, right, derivative
        )
    if not (
        certainly_positive(derivative.real)
        or certainly_negative(derivative.real)
    ):
        return RealRootCertificate(
            "inconclusive", "derivative_contains_zero", bracket, left, right, derivative
        )
    return RealRootCertificate(
        "pass", "opposite_signs_and_monotone", bracket, left, right, derivative
    )


def plant_factor(z: acb) -> acb:
    return (z - acb(PLANT_A)) ** 2 + acb(PLANT_B) ** 2


def plant_factor_prime(z: acb) -> acb:
    return acb(2) * (z - acb(PLANT_A))


@dataclass
class IntegratedPlant:
    status: str
    number: int | None
    reason: str
    checked_segments: int


def certify_integrated_plant(
    h_winding: WindingResult, factor_winding: WindingResult
) -> IntegratedPlant:
    if (
        h_winding.status != "ok"
        or h_winding.number is None
        or factor_winding.status != "ok"
        or factor_winding.number is None
    ):
        return IntegratedPlant("inconclusive", None, "component_winding_unresolved", 0)
    checked = 0
    for segment in h_winding.segments:
        factor_image = enclose_image(
            plant_factor,
            plant_factor_prime,
            segment.start,
            segment.end,
        )
        if not factor_image.ok or contains_zero(factor_image.ball):
            return IntegratedPlant(
                "inconclusive", None, "plant_boundary_enclosure", checked
            )
        product_start = segment.start_value * plant_factor(segment.start)
        product_end = segment.end_value * plant_factor(segment.end)
        if contains_zero(product_start) or contains_zero(product_end):
            return IntegratedPlant(
                "inconclusive", None, "product_endpoint_zero", checked
            )
        checked += 1
    return IntegratedPlant(
        "ok",
        h_winding.number + factor_winding.number,
        "additive_winding_with_zero_free_factors",
        checked,
    )


def run_calibrations() -> list[tuple[str, bool, str]]:
    rows: list[tuple[str, bool, str]] = []
    for name, re, im in SAFE_CALIBRATION_POINTS:
        z = point(re, im)
        entire_value = eval_H(z)
        direct_value = calibration_direct_H(z)
        ok = (
            finite(entire_value)
            and finite(direct_value)
            and entire_value.overlaps(direct_value)
        )
        rows.append(
            (
                "entire H agrees with 2M*rgamma at " + name,
                ok,
                "entire=%s direct=%s" % (entire_value, direct_value),
            )
        )
    return rows


@dataclass
class PickPointResult:
    name: str
    q: acb
    expected_sign: str
    h_numerator: acb
    h_denominator: acb
    phi_h: acb
    m_numerator: DirectContinuation
    m_denominator: DirectContinuation
    phi_m: acb
    denominators_exclude_zero: bool
    overlap: bool
    declared_sign_certified: bool
    reason: str

    @property
    def certified(self) -> bool:
        return (
            self.denominators_exclude_zero
            and self.overlap
            and self.declared_sign_certified
            and finite(self.phi_h)
            and finite(self.phi_m)
            and self.reason == "certified"
        )


def evaluate_pick_point(
    specification: tuple[str, str, str], expected_sign: str
) -> PickPointResult:
    name, re, im = specification
    q = point(re, im)
    h_numerator = eval_H(q - acb("0.5"))
    h_denominator = eval_H(q + acb("0.5"))
    h_denominator_safe = finite(h_denominator) and not contains_zero(h_denominator)
    phi_h = (
        acb(4) * h_numerator / h_denominator
        if finite(h_numerator) and h_denominator_safe
        else acb("nan")
    )

    m_numerator = eval_M_direct(acb(2) * q - acb(2))
    m_denominator = eval_M_direct(acb(2) * q)
    m_denominator_safe = (
        m_denominator.ok and not contains_zero(m_denominator.value)
    )
    phi_m = (
        (acb(4) * q - acb(2))
        * m_numerator.value
        / m_denominator.value
        if m_numerator.ok and m_denominator_safe
        else acb("nan")
    )

    denominators_safe = h_denominator_safe and m_denominator_safe
    overlap = (
        finite(phi_h)
        and finite(phi_m)
        and phi_h.overlaps(phi_m)
    )
    if expected_sign == "negative":
        sign_certified = (
            finite(phi_h)
            and finite(phi_m)
            and certainly_negative(phi_h.imag)
            and certainly_negative(phi_m.imag)
        )
    elif expected_sign == "positive":
        sign_certified = (
            finite(phi_h)
            and finite(phi_m)
            and certainly_positive(phi_h.imag)
            and certainly_positive(phi_m.imag)
        )
    else:
        raise ValueError("unsupported Pick-point sign")

    failures: list[str] = []
    if not denominators_safe:
        failures.append("denominator_unresolved")
    if not overlap:
        failures.append("paths_do_not_overlap")
    if not sign_certified:
        failures.append("sign_unresolved")
    reason = "certified" if not failures else ",".join(failures)
    return PickPointResult(
        name,
        q,
        expected_sign,
        h_numerator,
        h_denominator,
        phi_h,
        m_numerator,
        m_denominator,
        phi_m,
        denominators_safe,
        overlap,
        sign_certified,
        reason,
    )


def pick_point_detail(result: PickPointResult) -> str:
    return (
        "q=%s Hnum=%s Hden=%s phi_H=%s "
        "Mnum(N=%d)=%s Mden(N=%d)=%s phi_M=%s reason=%s"
        % (
            result.q,
            result.h_numerator,
            result.h_denominator,
            result.phi_h,
            result.m_numerator.n_terms,
            result.m_numerator.value,
            result.m_denominator.n_terms,
            result.m_denominator.value,
            result.phi_m,
            result.reason,
        )
    )


# ---------------------------------------------------------------------------
# Verdict logic and runner
# ---------------------------------------------------------------------------
def classify_contour(
    winding: WindingResult, root: RealRootCertificate
) -> tuple[str, str]:
    if winding.status != "ok" or winding.number is None:
        return "inconclusive", "contour_" + winding.reason
    if winding.number < 0:
        return "inconclusive", "negative_winding"
    if winding.number == 1:
        return "pass", "winding_one"
    if winding.number == 0:
        reason = (
            "root_contour_certificate_disagreement"
            if root.status == "pass"
            else "zero_count_zero"
        )
        return "inconclusive", reason
    if winding.number > 1:
        return "inconclusive", "extra_zero_count_%d" % winding.number
    return "inconclusive", "unexpected_zero_count_%d" % winding.number


def decide_verdict() -> str:
    failed_checks = [name for name, ok in CHECKS if not ok]
    if failed_checks:
        return "INCONCLUSIVE(instrument:%s)" % failed_checks[0].replace(" ", "_")
    killed = [gate for gate in MAIN_GATES if gate.status == "killed"]
    if killed:
        return "KILLED(%s)" % killed[0].reason
    unresolved = [gate for gate in MAIN_GATES if gate.status == "inconclusive"]
    if unresolved:
        first = unresolved[0]
        return "INCONCLUSIVE(%s:%s)" % (first.name, first.reason)
    return "FIRST_CELL_CERTIFIED"


def run(*, smoke: bool, json_path: str) -> int:
    global T0
    T0 = time.time()
    configure(smoke=smoke)
    mode = "smoke" if smoke else "record"
    print("CONTRACT %s" % CONTRACT)
    print("MODE %s" % mode)
    print("BITS %d" % WORKING_BITS)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA %s" % file_sha256())
    print("FENCE %s" % FENCE)
    print("CLAIM_BOUNDARY %s" % CLAIM_BOUNDARY)

    section("S0 frozen spec and firewall")
    firewall = ast_firewall()
    check("S0.1 AST firewall", firewall == [], str(firewall))
    check("S0.2 record precision is 512 bits", RECORD_BITS == 512, str(RECORD_BITS))
    check(
        "S0.3 smoke uses the same B1 at 256 bits",
        SMOKE_BITS == 256
        and TARGET_RE_LO == "-5.34"
        and TARGET_RE_HI == "-4.32"
        and TARGET_IM_LO == "-0.25"
        and TARGET_IM_HI == "0.25",
        "B1=%s" % target_box(),
    )
    check(
        "S0.4 dynamic order is N=14 on B1",
        dynamic_order(target_box()) == 14,
        "N(B1)=%d" % dynamic_order(target_box()),
    )
    check(
        "S0.5 lambda bracket is the eta affine image",
        arb(LAMBDA_LO).overlaps((arb(ETA_LO) + 1) / 2)
        and arb(LAMBDA_HI).overlaps((arb(ETA_HI) + 1) / 2),
        "[%s,%s]" % (LAMBDA_LO, LAMBDA_HI),
    )

    section("S1 exact symbolic derivation gates")
    for name, ok, detail in symbolic_derivation_gates():
        check(name, ok, detail)

    section("S2 dynamic Taylor source and entire pole removals")
    n_target = dynamic_order(target_box())
    coeffs_target = taylor_even_coeffs(n_target)
    theta_tails = _N_TAIL_CAUCHY_CACHE[n_target]
    check(
        "S2.1 dynamic A_j balls finite with theta n-tail",
        len(coeffs_target) == n_target
        and all(finite(value) for value in coeffs_target)
        and all(value.is_finite() and value >= 0 for value in theta_tails),
        "N=%d max_tail=%s" % (n_target, max(theta_tails)),
    )
    check(
        "S2.2 Taylor series cap >= 2N+2",
        _SERIES_CAP_USED[n_target] >= 2 * n_target + 2,
        "cap=%d" % _SERIES_CAP_USED[n_target],
    )
    phi_zero = phi_ball(acb(0))
    phi_anchor = acb(arb(ANCHOR_PHI0, ANCHOR_RADIUS))
    check(
        "S2.3 Phi(0) overlaps independent printed anchor",
        finite(phi_zero) and phi_zero.overlaps(phi_anchor),
        str(phi_zero),
    )
    phi_plus = phi_ball(acb("0.25"))
    phi_minus = phi_ball(acb("-0.25"))
    check(
        "S2.4 Phi even ward at +/-1/4",
        finite(phi_plus) and finite(phi_minus) and phi_plus.overlaps(phi_minus),
        "%s vs %s" % (phi_plus, phi_minus),
    )

    e_values_ok = True
    e_derivatives_ok = True
    for j in range(n_target):
        value, derivative = entire_E_jet(acb(-j), j)
        sign_factor = -1 if j % 2 else 1
        expected_value = acb(sign_factor * math.factorial(j))
        harmonic = sum((arb(1) / arb(r) for r in range(1, j + 1)), arb(0))
        expected_derivative = (
            acb(sign_factor)
            * acb(math.factorial(j))
            * acb(arb.const_euler() - harmonic)
        )
        e_values_ok = e_values_ok and finite(value) and value.overlaps(expected_value)
        e_derivatives_ok = (
            e_derivatives_ok
            and finite(derivative)
            and derivative.overlaps(expected_derivative)
        )
    check(
        "S2.5 E_j(-j)=(-1)^j j! for j<14",
        e_values_ok,
        "acb_series entire recurrence",
    )
    check(
        "S2.6 E_j'(-j)=(-1)^j j!(EulerGamma-H_j)",
        e_derivatives_ok,
        "acb_series coefficient one",
    )

    recurrence_ok = True
    recurrence_point = point("-4.75", "0.125")
    recurrence_coeffs = taylor_even_coeffs(dynamic_order(recurrence_point))
    recurrence_jet = source_gamma_jet(recurrence_point, recurrence_coeffs)
    for j in (0, 5, len(recurrence_coeffs) - 1):
        e_value, _e_prime = entire_E_jet(recurrence_point, j)
        relation = (recurrence_point + acb(j)) * e_value - recurrence_jet.rgamma_value
        recurrence_ok = recurrence_ok and finite(relation) and relation.contains(0)
    check(
        "S2.7 (z+j)E_j=rgamma(z) away from poles",
        recurrence_ok,
        "j=0,5,N-1 at z=-4.75+0.125i",
    )

    pole_index = 5
    pole_n = dynamic_order(acb(-pole_index))
    pole_coeffs = taylor_even_coeffs(pole_n)
    h_at_pole = eval_H(acb(-pole_index))
    expected_h_at_pole = (
        acb(-1)
        * acb(math.factorial(pole_index))
        * pole_coeffs[pole_index]
    )
    check(
        "S2.8 H(-5)=(-1)^5 5! A_5",
        finite(h_at_pole) and h_at_pole.overlaps(expected_h_at_pole),
        "H(-5)=%s expected=%s" % (h_at_pole, expected_h_at_pole),
    )
    direct_e_mutant = mutant_direct_E_at_pole(pole_index)
    direct_h_mutant = mutant_direct_H_at_pole(pole_index, pole_coeffs)
    stable_e, _stable_ep = entire_E_jet(acb(-pole_index), pole_index)
    check(
        "S2.9 removable-pole E quotient mutant is caught",
        not finite(direct_e_mutant) and finite(stable_e),
        "mutant=%s stable=%s" % (direct_e_mutant, stable_e),
    )
    check(
        "S2.10 removable-pole direct-H mutant is caught",
        not finite(direct_h_mutant) and finite(h_at_pole),
        "mutant=%s stable=%s" % (direct_h_mutant, h_at_pole),
    )

    section("S3 cancellation-free R_N, R_N', and safe calibrations")
    remainder_point = recurrence_point
    r0 = eval_R(remainder_point, 0)
    r1 = eval_R(remainder_point, 1)
    check(
        "S3.1 R_N explicit low/mid/high balls finite",
        r0.ok,
        "N=%d low=%s mid=%s high=%s tail=%s"
        % (r0.n_terms, r0.low, r0.mid, r0.high_finite, r0.high_tail),
    )
    check(
        "S3.2 R_N' explicit low/mid/high balls finite",
        r1.ok,
        "N=%d low=%s mid=%s high=%s tail=%s"
        % (r1.n_terms, r1.low, r1.mid, r1.high_finite, r1.high_tail),
    )
    box_ward = complex_error_box(arb(1))
    check(
        "S3.3 omitted complex tails are two-dimensional boxes",
        box_ward.contains(acb(0, "0.5"))
        and box_ward.contains(acb("0.5", 0))
        and not real_error_ball(arb(1)).contains(acb(0, "0.5")),
        str(box_ward),
    )
    for name, ok, detail in run_calibrations():
        check(name, ok, detail)

    section("S4 conjugate-pair plant control")
    plant_winding = winding_rectangle(
        plant_factor,
        plant_factor_prime,
        TARGET_RE_LO,
        TARGET_RE_HI,
        TARGET_IM_LO,
        TARGET_IM_HI,
    )
    check(
        "S4.1 polynomial plant contributes its conjugate pair",
        plant_winding.status == "ok" and plant_winding.number == 2,
        "status=%s n=%s segs=%d attempts=%d"
        % (
            plant_winding.status,
            plant_winding.number,
            len(plant_winding.segments),
            plant_winding.attempts,
        ),
    )
    synthetic_extra_winding = WindingResult(
        "ok", 2, "synthetic_extra_count", [], 0, arb(2)
    )
    synthetic_pass_root = RealRootCertificate(
        "pass",
        "synthetic_simple_root",
        arb(0),
        acb(-1),
        acb(1),
        acb(1),
    )
    extra_status, extra_reason = classify_contour(
        synthetic_extra_winding, synthetic_pass_root
    )
    check(
        "S4.2 untyped extra count is INCONCLUSIVE, not KILLED",
        extra_status == "inconclusive" and extra_reason == "extra_zero_count_2",
        "classification=%s:%s" % (extra_status, extra_reason),
    )
    synthetic_zero_winding = WindingResult(
        "ok", 0, "synthetic_zero_count", [], 0, arb(0)
    )
    zero_status, zero_reason = classify_contour(
        synthetic_zero_winding, synthetic_pass_root
    )
    check(
        "S4.3 zero count is INCONCLUSIVE, not KILLED",
        zero_status == "inconclusive"
        and zero_reason == "root_contour_certificate_disagreement",
        "classification=%s:%s" % (zero_status, zero_reason),
    )

    section("S5 independent real simple-zero certificate")
    root = isolate_known_real_root()
    print(
        "  lambda bracket=%s H(left)=%s H(right)=%s H'(bracket)=%s"
        % (root.bracket, root.left_value, root.right_value, root.derivative),
        flush=True,
    )
    main_gate(
        "real_simple_root",
        "pass" if root.status == "pass" else "inconclusive",
        root.reason,
        "lambda in [%s,%s]" % (LAMBDA_LO, LAMBDA_HI),
    )

    section("S6 certified full-cell H winding")
    print(
        "  contour B1 Re=[%s,%s] Im=[%s,%s] N(B1)=%d"
        % (
            TARGET_RE_LO,
            TARGET_RE_HI,
            TARGET_IM_LO,
            TARGET_IM_HI,
            dynamic_order(target_box()),
        ),
        flush=True,
    )
    h_winding = winding_rectangle(
        eval_H,
        eval_H_prime,
        TARGET_RE_LO,
        TARGET_RE_HI,
        TARGET_IM_LO,
        TARGET_IM_HI,
    )
    contour_status, contour_reason = classify_contour(h_winding, root)
    print(
        "  H_WINDING status=%s n=%s winding_ball=%s segments=%d attempts=%d reason=%s"
        % (
            h_winding.status,
            h_winding.number,
            h_winding.winding_ball,
            len(h_winding.segments),
            h_winding.attempts,
            h_winding.reason,
        ),
        flush=True,
    )
    main_gate(
        "contour_count",
        contour_status,
        contour_reason,
        "every segment uses midpoint+(Z-midpoint)H'(Z)",
    )

    if root.status == "pass" and h_winding.status == "ok" and h_winding.number == 1:
        main_gate(
            "exact_count_no_nonreal",
            "pass",
            "one_total_minus_one_real_equals_zero_nonreal",
            "|Im z|<=0.25 inside B1",
        )
    elif contour_status == "killed":
        main_gate(
            "exact_count_no_nonreal",
            "killed",
            contour_reason,
            "certified contour count differs from one",
        )
    else:
        main_gate(
            "exact_count_no_nonreal",
            "inconclusive",
            "root_or_contour_unresolved",
            "no subtraction of uncertified counts",
        )

    section("S7 unit shift, residue, and integrated plant")
    residue_ball = acb("nan")
    shift_value = acb("nan")
    shift_bracket = root.bracket - arb(1)
    shift_inside = bool(
        shift_bracket.lower() >= arb(TARGET_RE_LO).lower()
        and shift_bracket.upper() <= arb(TARGET_RE_HI).upper()
    )
    check(
        "S7.1 lambda-1 bracket lies inside B1",
        shift_inside,
        "lambda-1=%s" % shift_bracket,
    )

    if root.status != "pass":
        main_gate(
            "unit_shift",
            "inconclusive",
            "root_not_certified",
            "shift value not classified",
        )
        main_gate(
            "negative_residue",
            "inconclusive",
            "root_not_certified",
            "residue not classified",
        )
    else:
        shift_value = eval_H(acb(shift_bracket))
        if not finite(shift_value):
            main_gate("unit_shift", "inconclusive", "H_shift_nonfinite")
        elif shift_value.is_zero():
            main_gate("unit_shift", "killed", "unit_shift_collision")
        elif contains_zero(shift_value):
            main_gate("unit_shift", "inconclusive", "H_shift_contains_zero")
        else:
            main_gate(
                "unit_shift",
                "pass",
                "H_lambda_minus_one_excludes_zero",
                str(shift_value),
            )

        if (
            finite(shift_value)
            and not contains_zero(shift_value)
            and finite(root.derivative)
            and (
                certainly_positive(root.derivative.real)
                or certainly_negative(root.derivative.real)
            )
        ):
            residue_ball = acb(4) * shift_value / root.derivative
            if not finite(residue_ball):
                main_gate("negative_residue", "inconclusive", "residue_nonfinite")
            elif certainly_negative(residue_ball.real):
                main_gate(
                    "negative_residue",
                    "pass",
                    "residue_upper_below_zero",
                    str(residue_ball),
                )
            elif certainly_nonnegative(residue_ball.real):
                main_gate(
                    "negative_residue",
                    "killed",
                    "residue_not_negative",
                    str(residue_ball),
                )
            else:
                main_gate(
                    "negative_residue",
                    "inconclusive",
                    "residue_sign_unresolved",
                    str(residue_ball),
                )
        else:
            main_gate(
                "negative_residue",
                "inconclusive",
                "shift_or_derivative_unresolved",
            )

    print(
        "  SHIFT lambda-1=%s H(lambda-1)=%s"
        % (shift_bracket, shift_value),
        flush=True,
    )
    print(
        "  RESIDUE 4H(lambda-1)/H'(lambda)=%s"
        % residue_ball,
        flush=True,
    )

    integrated = certify_integrated_plant(h_winding, plant_winding)
    if integrated.status == "ok" and integrated.number == 3:
        main_gate(
            "integrated_conjugate_pair_plant",
            "pass",
            "H_count_plus_two_equals_three",
            "n=%d checked_segments=%d"
            % (integrated.number, integrated.checked_segments),
        )
    else:
        main_gate(
            "integrated_conjugate_pair_plant",
            "inconclusive",
            integrated.reason,
            "n=%s checked_segments=%d"
            % (integrated.number, integrated.checked_segments),
        )

    section("S8 frozen upper-half-plane Pick counterpoints")
    good_point = evaluate_pick_point(Q_GOOD, "positive")
    bad_point_1 = evaluate_pick_point(Q_BAD_1, "negative")
    bad_point_2 = evaluate_pick_point(Q_BAD_2, "negative")
    print("  PICK_POINT %s" % pick_point_detail(good_point), flush=True)
    print("  PICK_POINT %s" % pick_point_detail(bad_point_1), flush=True)
    print("  PICK_POINT %s" % pick_point_detail(bad_point_2), flush=True)
    check(
        "S8.1 positive Pick regression control agrees by H and M",
        good_point.certified,
        pick_point_detail(good_point),
    )
    check(
        "S8.2 q_bad_1 has Im(phi) upper<0 by H and direct M",
        bad_point_1.certified,
        pick_point_detail(bad_point_1),
    )
    check(
        "S8.3 q_bad_2 independently has Im(phi) upper<0",
        bad_point_2.certified,
        pick_point_detail(bad_point_2),
    )
    certified_bad_points = [
        result
        for result in (bad_point_1, bad_point_2)
        if result.certified
    ]
    if good_point.certified and certified_bad_points:
        main_gate(
            "pick_sign",
            "killed",
            "PICK_SIGN",
            "negative Im upper bound by H and M at %s"
            % ",".join(result.name for result in certified_bad_points),
        )
    else:
        unresolved = [
            result.name + ":" + result.reason
            for result in (good_point, bad_point_1, bad_point_2)
            if not result.certified
        ]
        main_gate(
            "pick_sign",
            "inconclusive",
            "counterpoint_unresolved",
            ",".join(unresolved),
        )

    verdict = decide_verdict()
    n_pass = sum(1 for _name, ok in CHECKS if ok)
    runtime = time.time() - T0
    section("RESULT")
    print("VERDICT %s" % verdict)
    print("CHECKS %d/%d PASS" % (n_pass, len(CHECKS)))
    print(
        "MAIN_GATES %s"
        % ",".join("%s=%s" % (gate.name, gate.status) for gate in MAIN_GATES)
    )
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA %s" % file_sha256())
    print("runtime %.3f s" % runtime)
    print(
        "ALL CHECKS PASSED"
        if n_pass == len(CHECKS)
        else "GATE_FAILURES "
        + ",".join(name for name, ok in CHECKS if not ok)
    )
    print("claim_boundary %s" % CLAIM_BOUNDARY)
    print(
        "kill_scope canonical_phi_not_Pick_and_not_in_BP1; "
        "does_not_disprove RH/KPS/alternative_Bernstein_interpolants"
    )

    if json_path:
        payload = {
            "contract": CONTRACT,
            "mode": mode,
            "bits": WORKING_BITS,
            "spec_sha256": SPEC_SHA,
            "file_sha256": file_sha256(),
            "verdict": verdict,
            "target_box": {
                "re": [TARGET_RE_LO, TARGET_RE_HI],
                "im": [TARGET_IM_LO, TARGET_IM_HI],
            },
            "dynamic_order": dynamic_order(target_box()),
            "root": {
                "status": root.status,
                "reason": root.reason,
                "lambda_bracket": str(root.bracket),
                "H_left": str(root.left_value),
                "H_right": str(root.right_value),
                "H_prime": str(root.derivative),
            },
            "winding": {
                "status": h_winding.status,
                "number": h_winding.number,
                "reason": h_winding.reason,
                "winding_ball": str(h_winding.winding_ball),
                "segments": len(h_winding.segments),
                "attempts": h_winding.attempts,
            },
            "shift": {
                "bracket": str(shift_bracket),
                "H": str(shift_value),
            },
            "residue": str(residue_ball),
            "plant": {
                "factor_winding": plant_winding.number,
                "integrated_winding": integrated.number,
                "status": integrated.status,
            },
            "checks": {name: ok for name, ok in CHECKS},
            "main_gates": [
                {
                    "name": gate.name,
                    "status": gate.status,
                    "reason": gate.reason,
                    "detail": gate.detail,
                }
                for gate in MAIN_GATES
            ],
            "runtime_s": runtime,
            "claim_boundary": CLAIM_BOUNDARY,
        }
        Path(json_path).write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print("WROTE %s" % json_path)

    return 0 if n_pass == len(CHECKS) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--smoke", action="store_true")
    modes.add_argument("--record", action="store_true")
    parser.add_argument("--json", default="", help="optional output path")
    args = parser.parse_args()
    smoke = not args.record
    try:
        return run(smoke=smoke, json_path=args.json)
    except Exception as exc:
        print("VERDICT INCONCLUSIVE(runtime_exception:%s)" % type(exc).__name__)
        print("DETAIL %s" % exc)
        print("claim_boundary %s" % CLAIM_BOUNDARY)
        return 1


if __name__ == "__main__":
    sys.exit(main())
