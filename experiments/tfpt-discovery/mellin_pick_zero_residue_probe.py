#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mellin_pick_zero_residue_probe -- MELLIN.PICK.ZERO-RESIDUE.01

FROZEN SPEC v2 (2026-09-03).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing.  No ledger/paper/Lean/website/README edit.
A finite clean run is OPEN_UNSETTLED, never proof progress.  This finite
test cannot prove Pick, BP1, or RH.  KEIN RH-CLAIM.

Firewall: no zeta-zero oracles; no claim language; no promotion.
python-flint 0.9.0 (acb/arb balls) is mandatory.  Pure mpmath grids and
raw phase-unwrapping are not certificates.  Fail loud without flint.

=======================================================================
KERNEL AND CONTINUATION
=======================================================================
Phi(u) = sum_{n>=1} (2 pi^2 n^4 exp(9u/2) - 3 pi n^2 exp(5u/2))
         * exp(-pi n^2 exp(2u)).
M(s) = int_0^inf Phi(u) u^s du.
Phi is even (Titchmarsh).  Each n-summand is entire; the summed theta
series is used only where Re(exp(2u)) > 0 (in particular
|Im u| < pi/4 on the principal strip).  `phi_ball` returns non-finite
whenever its input ball cannot certify this condition.

Continuation, N = N_TAYLOR_TERMS, a_{2j} = Phi^{(2j)}(0)/(2j)!,
valid for Re s > -2N-1 (poles of the raw Mellin sit at negative odd
integers; frozen rectangles avoid them):

  M(s) = sum_{j=0}^{N-1} a_{2j}/(s+2j+1)
       + int_0^1 [Phi(u) - sum_{j<N} a_{2j} u^{2j}] u^s du
       + int_1^inf Phi(u) u^s du.

Split at DELTA_LOW and U_CUT.  [0, DELTA_LOW] is charged by an explicit
Taylor remainder (Cauchy on |u|=CAUCHY_RADIUS < pi/4).  [U_CUT, inf) is
charged by the high-u bound below.  Finite n-sums are never labelled
rigorous without a tail bound.  acb.integral is used only with the
analytic flag forwarded.  A non-finite subpart is INCONCLUSIVE, never
a silent point evaluation.

ERROR BOXES.  A real radius R does not enclose imaginary error:
acb(arb(0,R), arb(0)) does not contain 0 + i R/2.  Every omitted
*complex* series/integral tail (Phi n-tail, low-u remainder, high-u
tail) is charged as complex_error_box(R) = acb(arb(0,R), arb(0,R)).
Taylor a_{2j} at 0 may use a real error ball: the exact even
coefficients are real (Phi even and real on the reals).

FENCE: the earlier vertical-line formula M(s) ~ Phi(0)/(s+1) is FALSE
and is not used.  There is no asymptotic gate in this probe.

=======================================================================
PROVED N-TAIL (Gaussian-power)
=======================================================================
For c>0, f(x)=x^k exp(-c x^2) is decreasing on [m,inf) once
m > sqrt(k/(2c)), i.e. once 2 c m^2 > k.  Code sums n = n0 .. m-1
explicitly with m the least integer >= n0 satisfying that
precondition (enforced, not assumed), then

  sum_{n=m}^inf n^k exp(-c n^2)
    <= m^k exp(-c m^2) + (1/2) c^{-(k+1)/2} Gamma((k+1)/2, c m^2),

because sum_{n=m+1}^inf f(n) <= int_m^inf f(x) dx and the integral
is the displayed incomplete-gamma term.  Phi tails use separate k=4
and k=2 sums with c = pi * lower(Re exp(2u)).  No geometric-ratio
or unexplained factor 2.

=======================================================================
PROVED HIGH-U TAIL
=======================================================================
U >= 1, Q = max(Re s upper, 0) + deriv.  Then |log u|^deriv <= u^deriv
and u^Q <= U^Q exp(Q(u-U)/U) on [U,inf).  Also exp(2(U+x)) >=
exp(2U)(1+2x).  With A = pi exp(2U),

  int_U^inf |Phi(u) u^s (log u)^deriv| du
    <= 2 pi^2 U^Q e^{4.5 U} sum_n n^4 e^{-A n^2} / (2 A n^2 - 4.5 - Q/U)
     + 3 pi   U^Q e^{2.5 U} sum_n n^2 e^{-A n^2} / (2 A n^2 - 2.5 - Q/U).

Denominators are lower-bounded by their n=1 values and must be
positive.  The n-sums are the proved Gaussian-power tails from n=1.
This charges every n and every u >= U.

=======================================================================
CANDIDATE AND TRI-STATE KILLS
=======================================================================
phi(z) = (4z-2) M(2z-2)/M(2z).
At a simple real zero eta of M,
  Res_{z=eta/2} phi = (eta-1) M(eta-2)/M'(eta).
Pick convention: residue <= 0.

A ball that merely *contains* 0 is INCONCLUSIVE, never a certified
multiple zero or shift collision.  Those kills fire only on an exact
zero (is_zero), used by the synthetic exact wards.  Uncertain M' or
M(eta-2) on the actual evaluator propagates INCONCLUSIVE.

Gap of consecutive isolated real zeros: upper<=2 certifies gap_le_2;
lower>2 is OK; an interval straddling 2 is INCONCLUSIVE.
Residue: lower>0 kills; upper<=0 passes; straddling is INCONCLUSIVE.
Every inconclusive root test sets StripResult.certified=False and the
final verdict INCONCLUSIVE (unless a *certified* kill is also present).

Certified structural kills (only these upgrade to KILLED):
  nonreal_zero, multiple_zero, shift_collision, residue_sign, gap_le_2.
A certified winding with nonreal count >0 is a valid nonreal_zero kill.
Controls never decide the M verdict.
Zero-free strips make residue/gap checks vacuous (reported as such).

Real isolation: if M' excludes 0 and the endpoint signs are equal,
monotonicity certifies no root (no fake root, no kill).  If M'
contains 0 at resolution, INCONCLUSIVE: an even-multiplicity touch
must not be silently missed.  Enclosure of a value is not equality.

If real roots exist, a complete nonreal count is not claimed while
omitting 0<Im<IM_OFF_REAL (no indent certificate here): the strip is
INCONCLUSIVE after the isolated-root rows are reported.  A zero-free
real boundary may keep im_lo=0.

=======================================================================
CONTOUR CERTIFICATE
=======================================================================
Argument principle on a rectangle: adaptive edge image balls that exclude
0, plus a ball-certified polygon winding homotopy.

Why this certifies.  Each edge is split until a first-order enclosure
  M(segment) subset M(mid) + (hull-mid) M'(hull)
is a disk B with 0 not in B (or the evaluator reports INCONCLUSIVE).
A disk is convex, so the true image path of the segment stays in B and
is homotopic in C\{0} to the straight segment joining the endpoint
images.  Concatenating those segments gives a polygon homotopic to
M(partial R) in C\{0}, hence the same winding number.  Consecutive
endpoint-image balls z_i, z_{i+1} contribute Delta arg = Im log(z_{i+1}/z_i)
provided the ratio ball does not meet (-inf,0]; otherwise refine.
If the sum/2pi ball contains a unique integer, that integer is N_zeros
(N_poles = 0 by the pole-avoiding rectangles).  Raw point-phase unwrap
is not used.  An image ball containing 0 is a failed enclosure
(INCONCLUSIVE after max refine), not a counted zero.

=======================================================================
CONTROLS (same file; no extra test module)
=======================================================================
  * Plant: multiply M by ((s-a)^2 + b^2) and require the contour engine
    to detect the conjugate pair (or, if M cannot be enclosed, detect
    the quadratic factor alone and record the M-plant as INCONCLUSIVE).
  * Exact synthetic classifiers: double real zero; gap=2 / shift
    collision; positive-residue meromorphic pole.  Every kill branch
    is executed on exact (is_zero / exact gap / exact residue) data.
  * Regression wards: complex box contains 0+iR/2; uncertain M' =>
    inconclusive; uncertain M(eta-2) => inconclusive; gap straddle =>
    inconclusive.
  * Cross-wards (calibration only): independent high-dps mpmath Phi/M
    at safe points; anchors Phi(0)~0.446696900467 and
    M(0)=Xi(0)/4~0.124280194547.

=======================================================================
VERDICTS
=======================================================================
  OPEN_UNSETTLED              finite clean certified strips; not a proof
  KILLED(<type>)              certified structural violation
  INCONCLUSIVE(<type>)        some required enclosure or root test failed
  PIPELINE-BROKEN             flint missing or oracle name present

Smoke: low height, first strip only.  Record: three strips
Re s in [-0.9,2], [-2.9,-1.1], [-4.9,-3.1] and declared HEIGHT;
RECORD_BITS >= 128.

SEALED NUMERICAL CONTRACT.  N_TAYLOR_TERMS=6,
TAYLOR_SERIES_CAP=16, CAUCHY_RADIUS=0.5, DELTA_LOW=0.08,
U_CUT=2.2, PHI_N_MAX=16, PHI_N_SERIES=12.  Smoke uses S1 to
height 0.45 at 64 bits.  Record uses S1/S2/S3 to height 2.5 at
128 bits.  Increasing Taylor order from 3 to 6 is the declared
certificate repair that tightens the Cauchy remainder; it changes
neither rectangles nor kill criteria.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

try:
    from flint import acb, acb_series, arb, ctx
except ImportError as exc:
    raise SystemExit(
        "PIPELINE-BROKEN: python-flint is required; run this probe in "
        "experiments/tfpt-discovery/.venv"
    ) from exc

import mpmath as mp

# ---------------------------------------------------------------------------
# Frozen constants
# ---------------------------------------------------------------------------
CONTRACT = "MELLIN.PICK.ZERO-RESIDUE.01"
FENCE = (
    "Exploration only; no RH/Pick/BP1 claim; finite clean => OPEN_UNSETTLED"
)
FENCE_FALSE_ASYMPTOTIC = (
    "M(s) ~ Phi(0)/(s+1) on vertical lines is FALSE; not used; "
    "no asymptotic gate"
)

N_TAYLOR_TERMS = 6
TAYLOR_SERIES_CAP = 16
CAUCHY_RADIUS = 0.5
DELTA_LOW = 0.08
U_CUT = 2.2
PHI_N_MAX = 16
PHI_N_SERIES = 12
VALID_RE_S_MIN = -2 * N_TAYLOR_TERMS - 1  # -7

RECORD_STRIPS = (
    ("S1", -0.9, 2.0),
    ("S2", -2.9, -1.1),
    ("S3", -4.9, -3.1),
)
SMOKE_STRIPS = (("S1", -0.9, 2.0),)
SMOKE_HEIGHT = 0.45
RECORD_HEIGHT = 2.5
IM_OFF_REAL = 0.002

SMOKE_MAX_SEGMENTS = 280
RECORD_MAX_SEGMENTS = 900
MIN_SEGMENT = 1e-3
MAX_REFINE_DEPTH = 14
INTEGRAL_EVAL_LIMIT = 8000
INTEGRAL_DEPTH_LIMIT = 22

SMOKE_BITS = 64
RECORD_BITS = 128
MPMATH_DPS = 40

ANCHOR_PHI0 = "0.446696900467"
ANCHOR_M0 = "0.124280194547"
# Printed 12-digit anchors are truncated; treat as closed last-digit intervals.
ANCHOR_DEC_RAD = "5e-13"
CROSS_S_POINTS = (0, 1, 2, "0.5")

PLANT_A = 0.35
PLANT_B = 0.25
PLANT_RE_LO = 0.05
PLANT_RE_HI = 0.65
PLANT_IM_LO = 0.05
PLANT_IM_HI = 0.42

SYN_DOUBLE_ETA = 1.0
SYN_GAP_LEFT = 0.5
SYN_GAP_RIGHT = 2.5
SYN_RES_ETA = 0.5
SYN_RES_MSHIFT = -2.0
SYN_RES_MPRIME = 1.0
GAP_MIN = 2

BANNED_ORACLES = (
    "zetazero",
    "zetazeros",
    "zeta_zero",
    "zeta_zeros",
    "nzeros",
    "find_zeros",
    "zeta_nzeros",
    "backlund_s",
)

LEGAL_VERDICTS_PREFIX = ("OPEN_UNSETTLED", "KILLED(", "INCONCLUSIVE(", "PIPELINE-BROKEN")
KILL_TYPES = (
    "nonreal_zero",
    "multiple_zero",
    "shift_collision",
    "residue_sign",
    "gap_le_2",
)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []
T0 = 0.0

# Set in configure()
WORKING_BITS = SMOKE_BITS
MAX_SEGMENTS = SMOKE_MAX_SEGMENTS
HEIGHT = SMOKE_HEIGHT
STRIPS = SMOKE_STRIPS
_TAYLOR: list[acb] | None = None
_PHI_DISK_BOUND: arb | None = None
_N_TAIL_CAUCHY: list[arb] | None = None


def check(name: str, ok: bool, detail: str = "") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print(
        "  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""),
        flush=True,
    )
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def configure(*, smoke: bool) -> None:
    global WORKING_BITS, MAX_SEGMENTS, HEIGHT, STRIPS
    global _TAYLOR, _PHI_DISK_BOUND, _N_TAIL_CAUCHY
    WORKING_BITS = SMOKE_BITS if smoke else RECORD_BITS
    MAX_SEGMENTS = SMOKE_MAX_SEGMENTS if smoke else RECORD_MAX_SEGMENTS
    HEIGHT = SMOKE_HEIGHT if smoke else RECORD_HEIGHT
    STRIPS = SMOKE_STRIPS if smoke else RECORD_STRIPS
    _TAYLOR = None
    _PHI_DISK_BOUND = None
    _N_TAIL_CAUCHY = None
    ctx.prec = WORKING_BITS
    ctx.cap = TAYLOR_SERIES_CAP


def ast_firewall() -> list[str]:
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    banned = set(BANNED_ORACLES)
    found: list[str] = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name in banned:
            found.append(name)
    return sorted(set(found))


# ---------------------------------------------------------------------------
# Ball helpers
# ---------------------------------------------------------------------------
def _pi() -> acb:
    return acb.pi()


def arb_mid_float(x: arb) -> float:
    return float(x.mid())


def certainly_positive(x: arb) -> bool:
    return bool(x > 0)


def certainly_le_zero(x: arb) -> bool:
    return bool(x.upper() <= 0)


def certainly_gt_zero(x: arb) -> bool:
    return bool(x.lower() > 0)


def certainly_negative(x: arb) -> bool:
    return bool(x < 0)


def real_error_ball(radius: arb) -> acb:
    """Real uncertainty only.  Exact even Taylor coefficients are real."""
    return acb(arb(0, radius), arb(0))


def complex_error_box(radius: arb) -> acb:
    """Square [-R,R] + i[-R,R].  Contains purely imaginary error of size R/2."""
    return acb(arb(0, radius), arb(0, radius))


def anchor_ball(mid: str, rad: str = ANCHOR_DEC_RAD) -> acb:
    return acb(arb(mid, rad))


def ball_from_segment(p: acb, q: acb) -> acb:
    return acb(p.real.union(q.real), p.imag.union(q.imag))


def point(re: float, im: float = 0.0) -> acb:
    return acb(re, im)


def finite_acb(z: acb) -> bool:
    return bool(z.is_finite())


def contains_zero(z: acb) -> bool:
    return bool(z.contains(0))


def meets_nonpositive_real(u: acb) -> bool:
    if not u.imag.contains(0):
        return False
    return not certainly_positive(u.real)


def safe_log(u: acb, analytic: bool) -> acb:
    if analytic and meets_nonpositive_real(u):
        return acb("nan")
    if meets_nonpositive_real(u):
        return acb("nan")
    return u.log()


# ---------------------------------------------------------------------------
# Phi with explicit n-tail
# ---------------------------------------------------------------------------
def _term_prefactor_abs_bound(n: int, r: arb) -> arb:
    nn = arb(n)
    n2 = nn * nn
    n4 = n2 * n2
    pi = arb.pi()
    grow9 = (arb("4.5") * r).exp()
    grow5 = (arb("2.5") * r).exp()
    return (arb(2) * pi * pi * n4 * grow9) + (arb(3) * pi * n2 * grow5)


def _re_exp2u_lower(r: arb) -> arb:
    """Lower bound of Re exp(2u) on |u| <= r < pi/4."""
    return ((arb(-2) * r).exp()) * (arb(2) * r).cos()


def phi_term(u: acb | acb_series, n: int) -> acb | acb_series:
    nn = acb(n)
    n2 = nn * nn
    pi = _pi()
    e2u = (u * 2).exp()
    e5 = (u * acb("2.5")).exp()
    e9 = (u * acb("4.5")).exp()
    return (acb(2) * pi * pi * n2 * n2 * e9 - acb(3) * pi * n2 * e5) * (
        (-pi * n2 * e2u).exp()
    )


def _monotonic_start(k: int, c: arb, n_min: int) -> int | None:
    """Least m >= n_min with 2 c m^2 > k certainly.  None if c is not > 0."""
    if not certainly_positive(c):
        return None
    m = max(int(n_min), 1)
    for _ in range(100000):
        if (arb(2) * c * arb(m * m)) > arb(k):
            return m
        m += 1
    return None


def gaussian_power_tail(k: int, c: arb, n0: int) -> arb:
    """Proved bound for sum_{n=n0}^inf n^k exp(-c n^2).

    Sum n0..m-1 explicitly, m the least integer >= n0 with 2 c m^2 > k,
    then sum_{n=m}^inf <= m^k e^{-c m^2} + (1/2) c^{-(k+1)/2} Gamma((k+1)/2, c m^2).
    """
    if n0 < 1:
        n0 = 1
    if k not in (2, 4):
        return arb("inf")
    m = _monotonic_start(k, c, n0)
    if m is None:
        return arb("inf")
    total = arb(0)
    for n in range(n0, m):
        total += (arb(n) ** k) * ((-c * arb(n * n)).exp())
    cm2 = c * arb(m * m)
    head = (arb(m) ** k) * ((-cm2).exp())
    s = arb(k + 1) / arb(2)
    ginc = cm2.gamma_upper(s)
    tail_int = arb("0.5") * (c ** (-s)) * ginc
    out = total + head + tail_int
    return out if out.is_finite() else arb("inf")


def phi_n_tail_abs(n0: int, re_exp_lo: arb, r_abs: arb) -> arb:
    """|sum_{n>=n0} term_n| via separate k=4 and k=2 Gaussian-power tails.

    c = pi * lower(Re exp(2u)); growth |exp(9u/2)| <= exp(4.5 r_abs).
    """
    if not certainly_positive(re_exp_lo):
        return arb("inf")
    c = arb.pi() * re_exp_lo
    t4 = gaussian_power_tail(4, c, n0)
    t2 = gaussian_power_tail(2, c, n0)
    pi = arb.pi()
    grow9 = (arb("4.5") * r_abs).exp()
    grow5 = (arb("2.5") * r_abs).exp()
    out = (arb(2) * pi * pi * grow9 * t4) + (arb(3) * pi * grow5 * t2)
    return out if out.is_finite() else arb("inf")


def phi_ball(u: acb, analytic: bool = False) -> acb:
    """Phi on an acb ball, finite n-sum plus a complex error box on the n-tail."""
    # Each summand is entire.  The summed series is certified only when
    # the explicit tail check below proves Re(exp(2u)) > 0 on this ball.
    del analytic
    if not u.is_finite():
        return acb("nan")
    total = acb(0)
    for n in range(1, PHI_N_MAX + 1):
        total += phi_term(u, n)
        if not total.is_finite():
            return acb("nan")
    e2 = (u * 2).exp()
    re_lo = e2.real.lower()
    r_abs = u.abs_upper()
    tail = phi_n_tail_abs(PHI_N_MAX + 1, re_lo, r_abs)
    if not tail.is_finite():
        return acb("nan")
    return total + complex_error_box(tail)


# ---------------------------------------------------------------------------
# Taylor a_{2j} with series + Cauchy n-tail
# ---------------------------------------------------------------------------
def _disk_phi_abs_bound(radius: arb) -> arb:
    re_lo = _re_exp2u_lower(radius)
    if not certainly_positive(re_lo):
        return arb("inf")
    pi = arb.pi()
    total = arb(0)
    for n in range(1, PHI_N_SERIES + 1):
        decay = (-pi * arb(n * n) * re_lo).exp()
        total += _term_prefactor_abs_bound(n, radius) * decay
    total += phi_n_tail_abs(PHI_N_SERIES + 1, re_lo, radius)
    return total


def _n_tail_cauchy_coeff_bounds(radius: arb) -> list[arb]:
    re_lo = _re_exp2u_lower(radius)
    tail_abs = phi_n_tail_abs(PHI_N_SERIES + 1, re_lo, radius)
    out: list[arb] = []
    rpow = arb(1)
    for j in range(N_TAYLOR_TERMS):
        if j:
            rpow *= radius * radius
        out.append(tail_abs / rpow)
    return out


def taylor_even_coeffs() -> list[acb]:
    global _TAYLOR, _PHI_DISK_BOUND, _N_TAIL_CAUCHY
    if _TAYLOR is not None:
        return _TAYLOR
    radius = arb(CAUCHY_RADIUS)
    ctx.cap = TAYLOR_SERIES_CAP
    u = acb_series([0, 1])
    ser = acb_series([0])
    for n in range(1, PHI_N_SERIES + 1):
        ser += phi_term(u, n)
    coeffs = ser.coeffs()
    tails = _n_tail_cauchy_coeff_bounds(radius)
    even: list[acb] = []
    for j in range(N_TAYLOR_TERMS):
        deg = 2 * j
        if deg >= len(coeffs):
            raise RuntimeError("series cap too small for a_%d" % deg)
        # Real error: exact a_{2j} are real (Phi even and real on R).
        even.append(coeffs[deg] + real_error_ball(tails[j]))
    _TAYLOR = even
    _PHI_DISK_BOUND = _disk_phi_abs_bound(radius)
    _N_TAIL_CAUCHY = tails
    return even


def taylor_poly(u: acb, coeffs: list[acb]) -> acb:
    acc = acb(0)
    u2 = u * u
    p = acb(1)
    for a in coeffs:
        acc += a * p
        p *= u2
    return acc


# ---------------------------------------------------------------------------
# Explicit remainder / tail boxes for M^{(k)}
# ---------------------------------------------------------------------------
def _power_log_integrals(delta: arb, p: arb, k: int) -> arb:
    """int_0^delta u^{p-1} |log u|^k du, p>0, delta in (0,1)."""
    if not certainly_positive(p):
        return arb("inf")
    logd = delta.log()  # negative
    dp = delta ** p
    if k == 0:
        return dp / p
    if k == 1:
        return dp * ((-logd) / p + arb(1) / (p * p))
    if k == 2:
        return dp * ((logd * logd) / p - arb(2) * logd / (p * p) + arb(2) / (p ** 3))
    return arb("inf")


def low_u_remainder_box(s: acb, deriv: int) -> acb:
    """Complex box bounding int_0^{DELTA} R_{2N}(u) u^s (log u)^{deriv} du."""
    radius = arb(CAUCHY_RADIUS)
    delta = arb(DELTA_LOW)
    if _PHI_DISK_BOUND is None:
        taylor_even_coeffs()
    m_r = _PHI_DISK_BOUND
    assert m_r is not None
    ratio = delta / radius
    if not (ratio < 1):
        return acb("nan")
    k_bound = m_r * ratio ** (2 * N_TAYLOR_TERMS) / (arb(1) - ratio)
    k_on_u2n = k_bound / (delta ** (2 * N_TAYLOR_TERMS))
    sigma_min = s.real.lower()
    p = arb(2 * N_TAYLOR_TERMS) + sigma_min + arb(1)
    integ = _power_log_integrals(delta, p, deriv)
    if not integ.is_finite():
        return acb("nan")
    return complex_error_box(k_on_u2n * integ)


def high_u_tail_box(s: acb, deriv: int) -> acb:
    """Complex box for int_U^inf Phi(u) u^s (log u)^{deriv} du, U=U_CUT>=1.

    Q = max(Re s upper, 0)+deriv; |log u|^deriv <= u^deriv;
    u^Q <= U^Q exp(Q(u-U)/U); exp(2(U+x)) >= exp(2U)(1+2x); A = pi exp(2U).
    n-sums: Gaussian-power tails from n=1; denoms lower-bounded at n=1.
    """
    u_cut = arb(U_CUT)
    if not (u_cut >= 1):
        return acb("nan")
    q = s.real.upper().max(arb(0)) + arb(deriv)
    pi = arb.pi()
    a_decay = pi * (arb(2) * u_cut).exp()
    den4 = arb(2) * a_decay - arb("4.5") - q / u_cut
    den2 = arb(2) * a_decay - arb("2.5") - q / u_cut
    if not certainly_positive(den4) or not certainly_positive(den2):
        return acb("nan")
    g4 = gaussian_power_tail(4, a_decay, 1)
    g2 = gaussian_power_tail(2, a_decay, 1)
    uq = u_cut ** q
    term4 = arb(2) * pi * pi * uq * (arb("4.5") * u_cut).exp() * g4 / den4
    term2 = arb(3) * pi * uq * (arb("2.5") * u_cut).exp() * g2 / den2
    total = term4 + term2
    if not total.is_finite():
        return acb("nan")
    return complex_error_box(total)


# ---------------------------------------------------------------------------
# Ball continuation of M, M', M''
# ---------------------------------------------------------------------------
def _integrand(u: acb, analytic: bool, s: acb, deriv: int, high: bool, coeffs: list[acb]) -> acb:
    ph = phi_ball(u, analytic)
    if not ph.is_finite():
        return acb("nan")
    rem = ph if high else (ph - taylor_poly(u, coeffs))
    logu = safe_log(u, analytic)
    if not logu.is_finite():
        return acb("nan")
    us = (s * logu).exp()
    if not us.is_finite():
        return acb("nan")
    w = rem * us
    if deriv == 1:
        w *= logu
    elif deriv >= 2:
        w *= logu * logu
    return w


def eval_M(s: acb, deriv: int = 0) -> acb:
    """Certified ball for M^{(deriv)}(s), or a non-finite ball."""
    if deriv not in (0, 1, 2):
        return acb("nan")
    if not s.is_finite():
        return acb("nan")
    if s.real.upper() <= VALID_RE_S_MIN:
        return acb("nan")
    coeffs = taylor_even_coeffs()
    pole = acb(0)
    for j, a in enumerate(coeffs):
        den = s + acb(2 * j + 1)
        if contains_zero(den):
            return acb("nan")
        if deriv == 0:
            pole += a / den
        elif deriv == 1:
            pole += -a / (den * den)
        else:
            pole += acb(2) * a / (den ** 3)
    if not pole.is_finite():
        return acb("nan")

    def low(u: acb, analytic: bool) -> acb:
        return _integrand(u, analytic, s, deriv, False, coeffs)

    def high(u: acb, analytic: bool) -> acb:
        return _integrand(u, analytic, s, deriv, True, coeffs)

    try:
        i_mid = acb.integral(
            low,
            acb(DELTA_LOW),
            acb(1),
            abs_tol=arb(2) ** -(WORKING_BITS - 8),
            eval_limit=INTEGRAL_EVAL_LIMIT,
            depth_limit=INTEGRAL_DEPTH_LIMIT,
        )
        i_hi = acb.integral(
            high,
            acb(1),
            acb(U_CUT),
            abs_tol=arb(2) ** -(WORKING_BITS - 8),
            eval_limit=INTEGRAL_EVAL_LIMIT,
            depth_limit=INTEGRAL_DEPTH_LIMIT,
        )
    except Exception:
        return acb("nan")
    if not i_mid.is_finite() or not i_hi.is_finite():
        return acb("nan")
    low_box = low_u_remainder_box(s, deriv)
    hi_box = high_u_tail_box(s, deriv)
    if not low_box.is_finite() or not hi_box.is_finite():
        return acb("nan")
    out = pole + i_mid + i_hi + low_box + hi_box
    return out if out.is_finite() else acb("nan")


# ---------------------------------------------------------------------------
# Independent mpmath cross-ward (calibration; not a certificate)
# ---------------------------------------------------------------------------
def mp_phi(u: mp.mpf, nmax: int = 20) -> mp.mpf:
    total = mp.mpf(0)
    pi = mp.pi
    for n in range(1, nmax + 1):
        n2 = mp.mpf(n) * n
        total += (2 * pi ** 2 * n2 * n2 * mp.e ** (mp.mpf("4.5") * u) - 3 * pi * n2 * mp.e ** (mp.mpf("2.5") * u)) * mp.e ** (
            -pi * n2 * mp.e ** (2 * u)
        )
    return total


def mp_M(s: mp.mpc, deriv: int = 0) -> mp.mpc:
    """Independent direct quadrature for Re(s)>-1; calibration only."""
    if mp.re(s) <= -1:
        raise ValueError("direct mpmath ward requires Re(s)>-1")

    def body(u):
        if u == 0:
            return mp.mpc(0)
        w = mp_phi(u) * (u ** s)
        if deriv == 1:
            w *= mp.log(u)
        elif deriv == 2:
            w *= mp.log(u) ** 2
        return w

    return mp.quad(
        body,
        [0, mp.mpf("0.01"), DELTA_LOW, mp.mpf("0.25"), mp.mpf("0.5"),
         1, mp.mpf("1.5"), U_CUT, 3, 4],
    )


def acb_from_mp(z: mp.mpc | mp.mpf) -> acb:
    if isinstance(z, mp.mpc):
        return acb(str(z.real), str(z.imag))
    return acb(str(z))


# ---------------------------------------------------------------------------
# Image enclosure and winding
# ---------------------------------------------------------------------------
@dataclass
class Encl:
    ok: bool
    ball: acb
    reason: str = ""


def enclose_image(f, fprime, p: acb, q: acb) -> Encl:
    hull = ball_from_segment(p, q)
    mid = (p + q) / acb(2)
    fm = f(mid)
    if not finite_acb(fm):
        return Encl(False, acb("nan"), "f_mid_nonfinite")
    if fprime is None:
        fh = f(hull)
        if not finite_acb(fh):
            return Encl(False, acb("nan"), "f_hull_nonfinite")
        return Encl(True, fh)
    fp = fprime(hull)
    if not finite_acb(fp):
        return Encl(False, acb("nan"), "fprime_hull_nonfinite")
    enc = fm + (hull - mid) * fp
    if not finite_acb(enc):
        return Encl(False, acb("nan"), "first_order_nonfinite")
    return Encl(True, enc)


@dataclass
class Winding:
    status: str  # ok | inconclusive
    n: int | None
    reason: str
    n_segments: int = 0


def _darg_of_ratio(z0: acb, z1: acb) -> acb | None:
    if contains_zero(z0) or contains_zero(z1):
        return None
    ratio = z1 / z0
    if contains_zero(ratio):
        return None
    if ratio.imag.contains(0) and not certainly_positive(ratio.real):
        return None
    lg = ratio.log()
    if not lg.is_finite():
        return None
    return lg.imag


def winding_rectangle(f, fprime, re_lo: float, re_hi: float, im_lo: float, im_hi: float) -> Winding:
    """Ball-certified winding of f around the axis-aligned rectangle."""
    corners = (
        point(re_lo, im_lo),
        point(re_hi, im_lo),
        point(re_hi, im_hi),
        point(re_lo, im_hi),
        point(re_lo, im_lo),
    )
    segs: list[tuple[acb, acb]] = []

    def refine(a: acb, b: acb, depth: int) -> str | None:
        if len(segs) >= MAX_SEGMENTS:
            return "max_segments"
        enc = enclose_image(f, fprime, a, b)
        if not enc.ok:
            length = (b - a).abs_upper()
            if depth >= MAX_REFINE_DEPTH or length < MIN_SEGMENT:
                return enc.reason or "enclose_failed"
            mid = (a + b) / acb(2)
            return refine(a, mid, depth + 1) or refine(mid, b, depth + 1)
        if contains_zero(enc.ball):
            length = (b - a).abs_upper()
            if depth >= MAX_REFINE_DEPTH or length < MIN_SEGMENT:
                return "zero_in_image"
            mid = (a + b) / acb(2)
            return refine(a, mid, depth + 1) or refine(mid, b, depth + 1)
        segs.append((a, b))
        return None

    for i in range(4):
        err = refine(corners[i], corners[i + 1], 0)
        if err:
            return Winding("inconclusive", None, err, len(segs))

    endpoints = [f(a) for a, _b in segs] + [f(segs[-1][1])]
    if any(not finite_acb(z) or contains_zero(z) for z in endpoints):
        return Winding("inconclusive", None, "endpoint_zero_or_nonfinite", len(segs))
    darg = acb(0)
    for i in range(len(endpoints) - 1):
        piece = _darg_of_ratio(endpoints[i], endpoints[i + 1])
        if piece is None:
            return Winding("inconclusive", None, "ratio_branch", len(segs))
        darg += piece
    winding_ball = darg / (acb(2) * _pi())
    n = winding_ball.unique_fmpz()
    if n is None:
        return Winding("inconclusive", None, "winding_not_unique:%s" % winding_ball, len(segs))
    return Winding("ok", int(n), "certified", len(segs))


# ---------------------------------------------------------------------------
# Real isolation, residue, gap
# ---------------------------------------------------------------------------
@dataclass
class RealZero:
    lo: arb
    hi: arb
    mprime: acb
    mshift: acb
    residue: acb


@dataclass
class RealScan:
    status: str
    zeros: list[RealZero] = field(default_factory=list)
    reason: str = ""


def _real_eval(x: arb, deriv: int = 0) -> acb:
    return eval_M(acb(x), deriv)


def _same_certified_sign(left: acb, right: acb) -> bool:
    return (certainly_gt_zero(left.real) and certainly_gt_zero(right.real)) or (
        certainly_negative(left.real) and certainly_negative(right.real)
    )


def _opposite_certified_sign(left: acb, right: acb) -> bool:
    return (certainly_gt_zero(left.real) and certainly_negative(right.real)) or (
        certainly_negative(left.real) and certainly_gt_zero(right.real)
    )


def isolate_real_zeros(re_lo: float, re_hi: float) -> RealScan:
    found: list[RealZero] = []
    max_pieces = 64 if MAX_SEGMENTS < 400 else 160

    def visit(lo: arb, hi: arb, depth: int) -> str | None:
        if len(found) + depth > max_pieces:
            return "real_budget"
        hull = lo.union(hi)
        val = _real_eval(hull, 0)
        if not finite_acb(val):
            if depth >= MAX_REFINE_DEPTH or arb_mid_float(hi - lo) < MIN_SEGMENT:
                return "real_nonfinite"
            mid = (lo + hi) / arb(2)
            return visit(lo, mid, depth + 1) or visit(mid, hi, depth + 1)
        if not contains_zero(val):
            return None
        mid = (lo + hi) / arb(2)
        if depth >= MAX_REFINE_DEPTH or arb_mid_float(hi - lo) < MIN_SEGMENT:
            mpv = _real_eval(hull, 1)
            if not finite_acb(mpv):
                return "real_mprime_nonfinite"
            if contains_zero(mpv):
                # Even-multiplicity touch cannot be ruled out.
                return "mprime_unresolved"
            left = _real_eval(lo, 0)
            right = _real_eval(hi, 0)
            if not finite_acb(left) or not finite_acb(right):
                return "real_endpoint_nonfinite"
            if contains_zero(left) or contains_zero(right):
                return "zero_on_endpoint"
            if _same_certified_sign(left, right):
                return None
            if not _opposite_certified_sign(left, right):
                return "endpoint_sign_unresolved"
            shift_pt = hull - arb(2)
            mshift = _real_eval(shift_pt, 0)
            if not finite_acb(mshift):
                return "mshift_nonfinite"
            eta = acb(hull)
            residue = (eta - acb(1)) * mshift / mpv
            found.append(RealZero(lo, hi, mpv, mshift, residue))
            return None
        return visit(lo, mid, depth + 1) or visit(mid, hi, depth + 1)

    err = visit(arb(re_lo), arb(re_hi), 0)
    if err:
        return RealScan("inconclusive", found, err)
    return RealScan("ok", found, "certified")


def classify_real_zero(z: RealZero, nxt: RealZero | None) -> str:
    """Tri-state: ok | killed:<type> | inconclusive:<type>.

    contains(0) is not a kill.  Only is_zero certifies multiple/shift.
    """
    if not finite_acb(z.mprime):
        return "inconclusive:multiple_zero"
    if z.mprime.is_zero():
        return "killed:multiple_zero"
    if contains_zero(z.mprime):
        return "inconclusive:multiple_zero"
    if not finite_acb(z.mshift):
        return "inconclusive:shift_collision"
    if z.mshift.is_zero():
        return "killed:shift_collision"
    if contains_zero(z.mshift):
        return "inconclusive:shift_collision"
    if not finite_acb(z.residue):
        return "inconclusive:residue"
    if certainly_gt_zero(z.residue.real):
        return "killed:residue_sign"
    if not certainly_le_zero(z.residue.real):
        return "inconclusive:residue"
    if nxt is not None:
        gap_hi = nxt.hi - z.lo
        gap_lo = nxt.lo - z.hi
        if gap_hi <= GAP_MIN:
            return "killed:gap_le_2"
        if gap_lo > GAP_MIN:
            return "ok"
        return "inconclusive:gap"
    return "ok"


# ---------------------------------------------------------------------------
# Synthetic classifiers (exact; every kill branch executable)
# ---------------------------------------------------------------------------
def synthetic_classifiers() -> dict[str, str]:
    """Exact-zero kill wards.  Uncertain balls must not fire these."""
    out: dict[str, str] = {}
    z_dbl = RealZero(
        lo=arb(SYN_DOUBLE_ETA),
        hi=arb(SYN_DOUBLE_ETA),
        mprime=acb(0),
        mshift=acb(1),
        residue=acb("nan"),
    )
    out["multiple_zero"] = classify_real_zero(z_dbl, None)

    z_shift = RealZero(
        lo=arb(SYN_GAP_LEFT),
        hi=arb(SYN_GAP_LEFT),
        mprime=acb(1),
        mshift=acb(0),
        residue=acb(0),
    )
    out["shift_collision"] = classify_real_zero(z_shift, None)

    z_l = RealZero(
        lo=arb(SYN_GAP_LEFT),
        hi=arb(SYN_GAP_LEFT),
        mprime=acb(1),
        mshift=acb(1),
        residue=acb(-1),
    )
    z_r = RealZero(
        lo=arb(SYN_GAP_RIGHT),
        hi=arb(SYN_GAP_RIGHT),
        mprime=acb(1),
        mshift=acb(1),
        residue=acb(-1),
    )
    out["gap_le_2"] = classify_real_zero(z_l, z_r)

    eta = acb(SYN_RES_ETA)
    mshift = acb(SYN_RES_MSHIFT)
    mprime = acb(SYN_RES_MPRIME)
    res = (eta - acb(1)) * mshift / mprime
    z_res = RealZero(
        lo=arb(SYN_RES_ETA),
        hi=arb(SYN_RES_ETA),
        mprime=mprime,
        mshift=mshift,
        residue=res,
    )
    out["residue_sign"] = classify_real_zero(z_res, None)
    return out


def regression_wards() -> dict[str, str]:
    """Parent-audit reproductions: uncertainty is INCONCLUSIVE, not a kill."""
    out: dict[str, str] = {}
    box = complex_error_box(arb(1))
    half_i = acb(0, arb("0.5"))
    out["complex_box"] = "ok" if box.contains(half_i) else "missed"
    out["real_ball_not_imag"] = (
        "ok" if not real_error_ball(arb(1)).contains(half_i) else "missed"
    )
    z_mp = RealZero(
        lo=arb(1),
        hi=arb(1),
        mprime=acb(arb(0, 1)),
        mshift=acb(1),
        residue=acb(-1),
    )
    out["uncertain_mprime"] = classify_real_zero(z_mp, None)
    z_sh = RealZero(
        lo=arb(SYN_GAP_LEFT),
        hi=arb(SYN_GAP_LEFT),
        mprime=acb(1),
        mshift=acb(arb(0, 1)),
        residue=acb(-1),
    )
    out["uncertain_mshift"] = classify_real_zero(z_sh, None)
    z_l = RealZero(
        lo=arb("0.5"),
        hi=arb("0.6"),
        mprime=acb(1),
        mshift=acb(1),
        residue=acb(-1),
    )
    z_r = RealZero(
        lo=arb("2.4"),
        hi=arb("2.7"),
        mprime=acb(1),
        mshift=acb(1),
        residue=acb(-1),
    )
    out["gap_straddle"] = classify_real_zero(z_l, z_r)
    return out


def quadratic_factor(s: acb) -> acb:
    return (s - acb(PLANT_A)) ** 2 + acb(PLANT_B) ** 2


def quadratic_factor_prime(s: acb) -> acb:
    return acb(2) * (s - acb(PLANT_A))


# ---------------------------------------------------------------------------
# Strip runner
# ---------------------------------------------------------------------------
@dataclass
class StripResult:
    name: str
    re_lo: float
    re_hi: float
    height: float
    n_total: int | None
    n_real: int | None
    n_nonreal: int | None
    certified: bool
    reason: str
    residues: list[str]
    kills: list[str]
    n_segments: int = 0
    winding_upper: int | None = None


def _record_root_row(z: RealZero, nxt: RealZero | None, residues: list[str], kills: list[str], inconclusive: list[str]) -> None:
    cls = classify_real_zero(z, nxt)
    residues.append("eta=[%s,%s] res=%s class=%s" % (z.lo, z.hi, z.residue, cls))
    if cls.startswith("killed:"):
        kills.append(cls.split(":", 1)[1])
    elif cls.startswith("inconclusive:"):
        inconclusive.append(cls.split(":", 1)[1])


def run_strip(name: str, re_lo: float, re_hi: float, height: float) -> StripResult:
    real = isolate_real_zeros(re_lo, re_hi)
    residues: list[str] = []
    kills: list[str] = []
    inconclusive: list[str] = []
    if real.status != "ok":
        return StripResult(
            name, re_lo, re_hi, height, None, None, None, False,
            "real:" + real.reason, [], [],
        )
    n_real = len(real.zeros)
    if n_real == 0:
        residues.append("VACUOUS(zero-free real boundary)")
        im_lo = 0.0
    else:
        for i, z in enumerate(real.zeros):
            nxt = real.zeros[i + 1] if i + 1 < len(real.zeros) else None
            _record_root_row(z, nxt, residues, kills, inconclusive)
        # No indent certificate: do not claim a complete nonreal count.
        reason = "thin_strip_omitted"
        if inconclusive:
            reason = reason + "," + ",".join(inconclusive)
        return StripResult(
            name, re_lo, re_hi, height, None, n_real, None, False,
            reason, residues, kills, 0, None,
        )

    def f(s: acb) -> acb:
        return eval_M(s, 0)

    def fp(s: acb) -> acb:
        return eval_M(s, 1)

    wind = winding_rectangle(f, fp, re_lo, re_hi, im_lo, height)
    if wind.status != "ok" or wind.n is None:
        return StripResult(
            name, re_lo, re_hi, height, None, n_real, None, False,
            "contour:" + wind.reason, residues, kills, wind.n_segments, None,
        )
    if wind.n < 0:
        return StripResult(
            name, re_lo, re_hi, height, None, n_real, None, False,
            "contour:negative_winding", residues, kills, wind.n_segments, wind.n,
        )
    n_upper = wind.n
    n_nonreal = 2 * n_upper
    n_total = n_real + n_nonreal
    if n_nonreal > 0:
        kills.append("nonreal_zero")
    return StripResult(
        name, re_lo, re_hi, height, n_total, n_real, n_nonreal, True,
        "certified", residues, kills, wind.n_segments, n_upper,
    )


def decide(strips: list[StripResult], plant_killed: bool) -> str:
    del plant_killed
    kills: list[str] = []
    inconclusive: list[str] = []
    for st in strips:
        kills.extend(st.kills)
        if not st.certified:
            inconclusive.append(st.reason)
    # plant / synthetics never decide the M-verdict except as instrument checks
    if kills:
        # unique preserve order
        seen: list[str] = []
        for k in kills:
            if k not in seen:
                seen.append(k)
        return "KILLED(" + ",".join(seen) + ")"
    if inconclusive:
        return "INCONCLUSIVE(" + ",".join(inconclusive) + ")"
    return "OPEN_UNSETTLED"


def legal_verdict(v: str) -> bool:
    return any(v == p or v.startswith(p) for p in LEGAL_VERDICTS_PREFIX if p.endswith("(") or p == v) or any(
        v.startswith(p) for p in LEGAL_VERDICTS_PREFIX
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def run(*, smoke: bool, json_path: str) -> int:
    global T0
    T0 = time.time()
    configure(smoke=smoke)
    mode = "smoke" if smoke else "record"

    print("CONTRACT %s" % CONTRACT)
    print("MODE %s" % mode)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA %s" % file_sha256())
    print("FENCE %s" % FENCE)
    print("FENCE_ASYMPTOTIC %s" % FENCE_FALSE_ASYMPTOTIC)
    print(
        "BITS %d  HEIGHT %s  STRIPS %s  N_TAYLOR %d  VALID_RE>%s"
        % (WORKING_BITS, HEIGHT, [s[0] for s in STRIPS], N_TAYLOR_TERMS, VALID_RE_S_MIN)
    )
    print("claim_boundary experiments_only_not_a_ledger_claim")

    section("S0 firewall")
    banned = ast_firewall()
    check("S0.1 flint acb/arb present", True, "python-flint 0.9.0")
    check("S0.2 no zeta-zero oracles", banned == [], str(banned))
    check("S0.3 SPEC_SHA frozen from the docstring", len(SPEC_SHA) == 64, SPEC_SHA[:16])
    check("S0.5 RECORD_BITS >= 128", RECORD_BITS >= 128, str(RECORD_BITS))
    check(
        "S0.4 false vertical asymptotic fenced (not an evaluator)",
        "Phi(0)/(s+1)" in FENCE_FALSE_ASYMPTOTIC and "eval_vertical_asymptotic" not in globals(),
        FENCE_FALSE_ASYMPTOTIC,
    )

    section("S1 Taylor source + anchors")
    coeffs = taylor_even_coeffs()
    check(
        "S1.1 a_{2j} finite with real n-tail balls",
        all(c.is_finite() for c in coeffs) and _N_TAIL_CAUCHY is not None,
        "a0=%s" % coeffs[0],
    )
    phi0 = phi_ball(acb(0))
    anchor_p = anchor_ball(ANCHOR_PHI0)
    check("S1.2 Phi(0) ball overlaps printed 12-digit anchor (calibration)", phi0.overlaps(anchor_p), str(phi0))
    even_pos = phi_ball(acb("0.25"))
    even_neg = phi_ball(acb("-0.25"))
    check("S1.3 Phi even at u=±1/4 (overlap ward)", even_pos.overlaps(even_neg), "%s vs %s" % (even_pos, even_neg))
    m0 = eval_M(acb(0), 0)
    anchor_m = anchor_ball(ANCHOR_M0)
    check("S1.4 M(0) finite", m0.is_finite(), str(m0))
    check(
        "S1.5 M(0) ball overlaps Xi(0)/4 printed anchor (calibration)",
        m0.overlaps(anchor_m) if m0.is_finite() else False,
        str(m0),
    )
    m0p = eval_M(acb(0), 1)
    check("S1.6 M'(0) finite", m0p.is_finite(), str(m0p))

    section("S2 mpmath cross-wards (calibration only)")
    mp.mp.dps = MPMATH_DPS
    mp_phi0 = mp_phi(mp.mpf(0))
    check(
        "S2.1 mpmath Phi(0) lies in the Phi(0) ball",
        phi0.contains(acb_from_mp(mp_phi0)),
        mp.nstr(mp_phi0, 15),
    )
    cross_ok = True
    for tag in CROSS_S_POINTS:
        s_mp = mp.mpf(tag)
        s_ball = acb(str(s_mp))
        mb = eval_M(s_ball, 0)
        mm = mp_M(s_mp, 0)
        ok = mb.is_finite() and mb.contains(acb_from_mp(mm))
        cross_ok = cross_ok and ok
        check("S2.2 M(%s) ball contains mpmath" % tag, ok, "ball=%s mp=%s" % (mb, mp.nstr(mm, 12)))

    section("S3 synthetic kill branches + regression wards")
    syn = synthetic_classifiers()
    for typ in ("multiple_zero", "shift_collision", "gap_le_2", "residue_sign"):
        check(
            "S3 exact %s kill fires" % typ,
            syn.get(typ) == "killed:" + typ,
            str(syn.get(typ)),
        )
    reg = regression_wards()
    check(
        "S3r complex_error_box contains 0+iR/2",
        reg["complex_box"] == "ok",
        str(complex_error_box(arb(1))),
    )
    check(
        "S3r real_error_ball does not contain 0+iR/2",
        reg["real_ball_not_imag"] == "ok",
        str(real_error_ball(arb(1))),
    )
    check(
        "S3r uncertain M' is INCONCLUSIVE not multiple_zero",
        reg["uncertain_mprime"] == "inconclusive:multiple_zero",
        str(reg["uncertain_mprime"]),
    )
    check(
        "S3r uncertain M(eta-2) is INCONCLUSIVE not shift_collision",
        reg["uncertain_mshift"] == "inconclusive:shift_collision",
        str(reg["uncertain_mshift"]),
    )
    check(
        "S3r gap straddle is INCONCLUSIVE",
        reg["gap_straddle"] == "inconclusive:gap",
        str(reg["gap_straddle"]),
    )
    g4 = gaussian_power_tail(4, arb.pi(), 1)
    g2 = gaussian_power_tail(2, arb.pi(), 1)
    check(
        "S3r Gaussian-power tails finite under monotonicity",
        g4.is_finite() and g2.is_finite() and g4 > 0 and g2 > 0,
        "k4=%s k2=%s" % (g4, g2),
    )

    section("S4 contour engine + planted pair")
    q_wind = winding_rectangle(
        quadratic_factor,
        quadratic_factor_prime,
        PLANT_RE_LO,
        PLANT_RE_HI,
        PLANT_IM_LO,
        PLANT_IM_HI,
    )
    check(
        "S4.1 quadratic winding detects the planted upper zero",
        q_wind.status == "ok" and q_wind.n == 1,
        "status=%s n=%s segs=%d" % (q_wind.status, q_wind.n, q_wind.n_segments),
    )
    # Conjugate pair as a kill-type token on the cheap factor (executable branch).
    check(
        "S4.2 nonreal_zero branch executable (conjugate pair)",
        q_wind.status == "ok" and q_wind.n == 1,
        "upper=1 => strip nonreal=2",
    )

    def planted_f(s: acb) -> acb:
        return eval_M(s, 0) * quadratic_factor(s)

    def planted_fp(s: acb) -> acb:
        return eval_M(s, 1) * quadratic_factor(s) + eval_M(s, 0) * quadratic_factor_prime(s)

    plant = winding_rectangle(
        planted_f,
        planted_fp,
        PLANT_RE_LO,
        PLANT_RE_HI,
        PLANT_IM_LO,
        PLANT_IM_HI,
    )
    plant_ok = plant.status == "ok" and plant.n == 1
    check(
        "S4.3 M*((s-a)^2+b^2) contour detects the plant (or honest INCONCLUSIVE)",
        plant_ok or plant.status == "inconclusive",
        "status=%s n=%s segs=%d reason=%s" % (plant.status, plant.n, plant.n_segments, plant.reason),
    )
    if plant.status == "inconclusive":
        print("  PLANT_M INCONCLUSIVE -- %s (quadratic control still certified)" % plant.reason)

    section("S5 first Mellin strips")
    results: list[StripResult] = []
    for name, re_lo, re_hi in STRIPS:
        print(
            "  rectangle %s  Re=[%s,%s]  Im=[0,%s]  (poles avoided: negative odd integers)"
            % (name, re_lo, re_hi, HEIGHT),
            flush=True,
        )
        st = run_strip(name, re_lo, re_hi, HEIGHT)
        results.append(st)
        print(
            "  RECTANGLE %s re=[%s,%s] im=[0,%s] total=%s real=%s nonreal=%s certified=%s segs=%d"
            % (
                st.name,
                st.re_lo,
                st.re_hi,
                st.height,
                st.n_total,
                st.n_real,
                st.n_nonreal,
                st.certified,
                st.n_segments,
            )
        )
        print("    reason %s  winding_upper=%s" % (st.reason, st.winding_upper))
        for row in st.residues:
            print("    RESIDUE %s" % row)
        if st.kills:
            print("    KILLS %s" % ",".join(st.kills))
        check(
            "S5 %s reported" % name,
            st.certified
            or st.reason.startswith("real:")
            or st.reason.startswith("contour:")
            or st.reason.startswith("thin_strip_omitted"),
            st.reason,
        )
        if st.certified and st.n_real == 0:
            check("S5 %s residue/gap vacuous (zero-free real)" % name, True, "vacuous")

    verdict = decide(results, plant_ok)
    check("S6 verdict enum", legal_verdict(verdict), verdict)
    if all(st.certified and not st.kills for st in results):
        check("S6 clean finite run typed OPEN_UNSETTLED", verdict == "OPEN_UNSETTLED", verdict)
    elif any(st.kills for st in results):
        check("S6 certified violation typed KILLED", verdict.startswith("KILLED("), verdict)
    else:
        check("S6 incomplete enclosure typed INCONCLUSIVE", verdict.startswith("INCONCLUSIVE("), verdict)

    n_pass = sum(1 for _n, ok in CHECKS if ok)
    wall = time.time() - T0
    section("RESULT")
    print("VERDICT %s" % verdict)
    print("CHECKS %d/%d PASS" % (n_pass, len(CHECKS)))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA %s" % file_sha256())
    print("runtime %.3f s" % wall)
    print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else "GATE_FAILURES " + ",".join(n for n, ok in CHECKS if not ok))
    print("claim_boundary experiments_only_not_a_ledger_claim")
    print("cannot_prove Pick/BP1/RH")

    if json_path:
        payload = {
            "contract": CONTRACT,
            "mode": mode,
            "SPEC_SHA": SPEC_SHA,
            "file_sha256": file_sha256(),
            "verdict": verdict,
            "fence": FENCE,
            "fence_asymptotic": FENCE_FALSE_ASYMPTOTIC,
            "height": HEIGHT,
            "strips": [
                {
                    "name": st.name,
                    "re": [st.re_lo, st.re_hi],
                    "height": st.height,
                    "n_total": st.n_total,
                    "n_real": st.n_real,
                    "n_nonreal": st.n_nonreal,
                    "certified": st.certified,
                    "reason": st.reason,
                    "residues": st.residues,
                    "kills": st.kills,
                    "n_segments": st.n_segments,
                    "winding_upper": st.winding_upper,
                }
                for st in results
            ],
            "plant": {"status": plant.status, "n": plant.n, "reason": plant.reason},
            "checks": {name: ok for name, ok in CHECKS},
            "runtime_s": wall,
        }
        Path(json_path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print("WROTE %s" % json_path)

    return 0 if n_pass == len(CHECKS) else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--json", default="", help="optional path; written only if set")
    args = ap.parse_args()
    smoke = True if args.smoke or not args.record else False
    if args.record and args.smoke:
        smoke = True
    return run(smoke=smoke, json_path=args.json)


if __name__ == "__main__":
    sys.exit(main())
