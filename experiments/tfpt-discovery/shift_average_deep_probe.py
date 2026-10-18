#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shift_average_deep_probe -- PRIME.COFINAL.SHIFT.AVERAGE.DEEP.01.

EXPLORATION ONLY (experiments/).  NO RH claim, NO all-h claim, and no
promotion.  This is the evaluator-grade follow-up to CCCXLI.

MISSION.  Rebuild the two resolution-limited offset families, h=1393 and
h=2854, independently from integer prime powers at MP_DPS=90.  Every source
quantity (frame, logarithm, mass, compact tent read, continuous
archimedean term, G read and matrix entry) receives an outward ball.  Matrix
signs are decided only by FLINT/Arb interval LDL; no eigensolver is used.

THE FAITHFUL FAMILY is frozen verbatim from CCCXLI:

  Omega_theta[m,n] = (G(m+n+2 theta) + G(|m-n|))/2,
  G(x) = c(x) - (c(x+1)+c(|x-1|))/2,

with the genuine comb capped at u <= 2 alpha + 2D.  The old 2 alpha cap is
used only by the declared regression at theta=1/2.

RIGOR PROTOCOL.
  S0  AST/source firewall: no zeta-zero reader, target sign, tau, cached
      assembly, or eigensolver.  The only sign primitive is arb_mat_ldl.
  T   Independent Eratosthenes prime-power table.  The two frames must
      rebuild exactly as (h,kz)=(1393,88),(2854,222).
  P   Construct the complete source breakpoint partition at 90 digits:
      frac(u/(2D)) and frac(u/(2D)+1/2), plus 0,1/2,1.  Outward breakpoint
      balls must be disjoint.  This proves that the ATOM contribution is
      affine on every listed open piece.
  A   Independently rebuild the archimedean tent pairing from

        L(t)=sum_{k>=0} exp(-(2k+1/2)t)/(2k+1/2)^2,
        A(s,D)=-(gamma+log pi+3log2+pi/2) tau_D(s)
               +(2L(s)-L(|s-D|)-L(s+D))/D,

      with a geometric omitted-tail bound.  A high-precision second
      difference is a mandatory honesty ward: if it excludes zero, the
      FULL family is not piecewise affine.  In that event the old
      Hermite--Hadamard argument may not be consumed without a validated
      curvature theorem and the mean must be refused.
  D   The predeclared nonzero dyadic rule is denominator order
      1/2; 1/4,3/4; 1/8,3/8,5/8,7/8.  It is source-only.  The first
      candidate whose Arb interval LDL proves B>0 and whose Schur ball is
      positive is reported.  This is a finite existence proof.  It is not
      a sign-mined PREDEFINED cofinal sequence and therefore does not by
      itself discharge H_cof.
  R   At theta=1/2, the old 2alpha cap must be refused while
      2alpha+2D must certify B>0.  This is the smoke-1 support regression.
  X   SCRAMBLE and EPSTEIN controls at theta=1/2 at both depths must either
      have interval-LDL refusal or a rigorously nonpositive Schur ball.
      Scramble locations are SHA256-derived dyadics (seed 20260813);
      Epstein Lambda_E is rebuilt at 90 digits by exact lattice counting
      and Dirichlet division, capped at 100000 as in CCCXLI.
  N   Perturb one rebuilt G source entry by more than its outward radius.
      The source-radius guard must refuse before matrix consumption.
  M   A mean enclosure is emitted only if (i) the full high-precision
      family is proved affine/concave on the complete partition, and
      (ii) interval LDL certifies B>0 at every consumed endpoint.  There is
      no fallback from point sampling.  If either premise is absent, the
      mathematically honest extended enclosure is [-inf,+inf] and the
      instrument verdict is EDGE.

FROZEN VERDICT ENUM (precedence NEGATIVE > CERTIFIED > MIXED > EDGE).
  SHIFTAVGDEEP-NEGATIVE        a rigorous negative mean exists;
  SHIFTAVGDEEP-CERTIFIED       both rigorous mean lower bounds and both
                              nonzero dyadic Schur lower bounds are >0;
  SHIFTAVGDEEP-MIXED           exactly one mean closes, with its nonzero
                              dyadic offset;
  SHIFTAVGDEEP-INSTRUMENT-EDGE otherwise.

FROZEN BARS.  MP_DPS=90, ARB_BITS=256, LERCH_TAIL=1e-82,
SOURCE_PAD=1e-74, breakpoint radius=1e-72, Epstein cap=100000,
runtime <1800 s.  The only requested outputs are this script and the German
experiments/next.txt note written after the run summary.

SMOKE DISCLOSURE.  Before this frozen file was written, read-only
reconnaissance counted 23810/221740 pieces, validated the continuous Lerch
formula against independent mpmath quadrature, tested the Arb LDL bridge on
synthetic matrices, and established that entrywise block balls lose the
theta dependency and are unusable.  No genuine deep Arb sign or control sign
was read.  Amendment A1: python-flint 0.9.0 was installed in the existing
discovery virtualenv because the repository had no validated ball-matrix
backend; no repository dependency file is changed by this experiment.
Amendment A2 (after the first attempted frozen run, fully disclosed): direct
unpreconditioned Arb LDL refused every genuine point although an independent
midpoint Cholesky existed; the run ended 13/18 in 400.8 s and read no dyadic
sign.  The permanent repair is congruence preconditioning:
C=R B R^T is assembled in Arb from the SAME source balls, interval LDL signs
C, and invertibility of the explicit triangular R transports the sign back
to B.  R carries no sign claim.  The same attempt exposed four overlapping
h=1393 kink balls from coincident log relations; the partition now consumes
each overlapping cluster once (23810 pieces), rather than treating a
1.3e-88 numerical separation as a new interval.  No source formula, target,
dyadic order, cap, control, verdict rule, or runtime bar changed.
Amendment A3 (reporting-only after the green run): Schur endpoints are printed
as binary64 values rounded one ulp outward, replacing nested Arb endpoint
balls in the log.  The underlying Arb balls and every verdict are unchanged.

HONEST SCOPE.  A CERTIFIED verdict would still be finite evidence at two
depths.  The dyadic rule is algorithmically predeclared inside this finite
probe, but H_cof requires one sequence fixed independently of future sign
outcomes and cofinal in depth.  Re-running "first certified dyadic" at each
future h is certificate-conditioned selection, not automatically the
PREDEFINED sequence required by H_cof.  NO RH CLAIM.
"""

from __future__ import annotations

import ast
import bisect
import ctypes
import gc
import hashlib
import math
import os
import sys
import time
from dataclasses import dataclass
from fractions import Fraction

import mpmath as mp
import numpy as np
import scipy.linalg as sla

try:
    import flint
    from flint import arb, arb_mat, ctx
except ImportError as exc:  # fail loud: validated matrix signs are mandatory
    raise SystemExit(
        "PIPELINE-BROKEN: python-flint is required; run this probe in "
        "experiments/tfpt-discovery/.venv"
    ) from exc


MP_DPS = 90
ARB_BITS = 256
LERCH_TAIL = mp.mpf("1e-82")
SOURCE_PAD = mp.mpf("1e-74")
BREAKPOINT_RAD = mp.mpf("1e-72")
EPSTEIN_CAP = 100_000
RUNTIME_BAR = 1800.0
NU_MAIN = 4
SCRAMBLE_SEED = 20260813
TARGETS = (("H1393", 1393, 88), ("H2854", 2854, 222))
DYADICS = (
    Fraction(1, 2),
    Fraction(1, 4), Fraction(3, 4),
    Fraction(1, 8), Fraction(3, 8),
    Fraction(5, 8), Fraction(7, 8),
)
AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh",
    "tau", "target_sign", "cached_sign",
}

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []
KILLS: list[str] = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % (
        "PASS" if ok else "FAIL", name,
        ("  -- " + detail) if detail else ""), flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad = set()
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in AST_BANNED:
            bad.add(name)
    return sorted(bad)


def mp_text(x):
    return mp.nstr(mp.mpf(x), MP_DPS)


def arb_ball(mid, rad):
    return arb(mp_text(mid), mp_text(abs(rad) + SOURCE_PAD))


def arb_bounds(x):
    lower = math.nextafter(float(x.lower()), -math.inf)
    upper = math.nextafter(float(x.upper()), math.inf)
    return "%.17e" % lower, "%.17e" % upper


def arb_positive(x):
    return bool(x.lower() > 0)


def arb_nonpositive(x):
    return bool(x.upper() <= 0)


class ArbMatStruct(ctypes.Structure):
    _fields_ = [
        ("entries", ctypes.c_void_p),
        ("r", ctypes.c_ssize_t),
        ("c", ctypes.c_ssize_t),
        ("rows", ctypes.c_void_p),
    ]


_ARB_MODULE = sys.modules[arb_mat.__module__]
_ARB_LIB = ctypes.CDLL(_ARB_MODULE.__file__)
_ARB_LDL = _ARB_LIB.arb_mat_ldl
_ARB_LDL.argtypes = (
    ctypes.POINTER(ArbMatStruct),
    ctypes.POINTER(ArbMatStruct),
    ctypes.c_ssize_t,
)
_ARB_LDL.restype = ctypes.c_int
_ARB_SOLVE_LDL = _ARB_LIB.arb_mat_solve_ldl_precomp
_ARB_SOLVE_LDL.argtypes = (
    ctypes.POINTER(ArbMatStruct),
    ctypes.POINTER(ArbMatStruct),
    ctypes.POINTER(ArbMatStruct),
    ctypes.c_ssize_t,
)
_ARB_SOLVE_LDL.restype = None
_ARB_OFFSET = arb_mat.__basicsize__ - ctypes.sizeof(ArbMatStruct)


def arb_ptr(matrix):
    return ctypes.cast(
        id(matrix) + _ARB_OFFSET, ctypes.POINTER(ArbMatStruct))


def ldl_bridge_ward():
    ctx.prec = ARB_BITS
    good = arb_mat([[2, 0], [0, 3]])
    bad = arb_mat([[1, 2], [2, 1]])
    out_good = arb_mat(2, 2)
    out_bad = arb_mat(2, 2)
    dims = (arb_ptr(good).contents.r, arb_ptr(good).contents.c)
    ok_good = _ARB_LDL(arb_ptr(out_good), arb_ptr(good), ARB_BITS)
    ok_bad = _ARB_LDL(arb_ptr(out_bad), arb_ptr(bad), ARB_BITS)
    return (_ARB_OFFSET > 0 and dims == (2, 2)
            and ok_good == 1 and ok_bad == 0)


@dataclass
class Frame:
    tag: str
    expected_h: int
    kz: int
    h: int
    M: int
    alpha: mp.mpf
    D: mp.mpf
    source_n: int
    cap_n: int


@dataclass
class AtomWorld:
    name: str
    positions: list
    masses: list
    positions_float: list


def prime_power_table(nmax):
    """Independent Eratosthenes table retaining each prime base."""
    sieve = np.ones(nmax + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(nmax) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    ns, bases = [], []
    for p0 in np.nonzero(sieve)[0]:
        p = int(p0)
        q = p
        while q <= nmax:
            ns.append(q)
            bases.append(p)
            q *= p
    order = np.argsort(np.asarray(ns), kind="stable")
    nn = np.asarray(ns, dtype=np.int64)[order]
    pp = np.asarray(bases, dtype=np.int64)[order]
    return nn, pp


def frame_from_integers(tag, expected_h, kz, nn):
    alpha = mp.log(int(nn[kz]))
    gap = mp.log(int(nn[kz + 1])) - alpha
    d_k = gap / (2 * NU_MAIN)
    M = int(mp.ceil(alpha / d_k - mp.mpf("1e-40"))) + 1
    if M % 2:
        M += 1
    h = M // 2
    D = 2 * alpha / M
    cap_n = int(mp.floor(mp.exp(2 * alpha + 2 * D)))
    return Frame(tag, expected_h, kz, h, M, alpha, D,
                 int(nn[kz]), cap_n)


def genuine_world(frame, nn, pp, old_cap=False):
    cap = int(mp.floor(mp.exp(2 * frame.alpha))) if old_cap \
        else frame.cap_n
    stop = int(np.searchsorted(nn, cap, side="right"))
    positions, masses = [], []
    for n0, p0 in zip(nn[:stop], pp[:stop]):
        n, p = int(n0), int(p0)
        positions.append(mp.log(n))
        masses.append(2 * mp.log(p) / mp.sqrt(n))
    return AtomWorld(
        "GENUINE-OLDCAP" if old_cap else "GENUINE",
        positions, masses, [float(u) for u in positions])


def scramble_world(source):
    rows = []
    two256 = mp.mpf(2) ** 256
    alpha2 = 2 * source[0]
    for index, mass in enumerate(source[1]):
        token = "SHIFTAVGDEEP:%d:%d" % (SCRAMBLE_SEED, index)
        raw = int.from_bytes(hashlib.sha256(token.encode()).digest(), "big")
        position = alpha2 * (mp.mpf(raw) + mp.mpf("0.5")) / two256
        rows.append((position, mass))
    rows.sort(key=lambda row: row[0])
    pos = [row[0] for row in rows]
    masses = [row[1] for row in rows]
    return AtomWorld("SCRAMBLE", pos, masses, [float(u) for u in pos])


def lattice_r1(nmax):
    out = np.zeros(nmax + 1, dtype=np.int64)
    for x in range(math.isqrt(nmax) + 1):
        x2 = x * x
        wx = 2 if x else 1
        ymax = math.isqrt((nmax - x2) // 5)
        for y in range(ymax + 1):
            n = x2 + 5 * y * y
            if n:
                out[n] += wx * (2 if y else 1)
    return out


_EPSTEIN_CACHE = None


def epstein_world():
    """90-digit Lambda_E from exact counts and Dirichlet division."""
    global _EPSTEIN_CACHE
    if _EPSTEIN_CACHE is not None:
        return _EPSTEIN_CACHE
    counts = lattice_r1(EPSTEIN_CAP)
    if np.any(counts % 2):
        raise AssertionError("r_Q1/2 integrality failed")
    coeff = counts // 2
    if coeff[1] != 1:
        raise AssertionError("Epstein normalization a_1=1 failed")
    accum = [mp.mpf("0")] * (EPSTEIN_CAP + 1)
    lam = [mp.mpf("0")] * (EPSTEIN_CAP + 1)
    for n in range(2, EPSTEIN_CAP + 1):
        value = int(coeff[n]) * mp.log(n) - accum[n]
        lam[n] = value
        if value:
            for k in range(2, EPSTEIN_CAP // n + 1):
                ak = int(coeff[k])
                if ak:
                    accum[n * k] += value * ak
    positions, masses = [], []
    for n in range(2, EPSTEIN_CAP + 1):
        if abs(lam[n]) > mp.mpf("1e-70"):
            positions.append(mp.log(n))
            masses.append(2 * lam[n] / mp.sqrt(n))
    _EPSTEIN_CACHE = AtomWorld(
        "EPSTEIN", positions, masses, [float(u) for u in positions])
    return _EPSTEIN_CACHE


def lerch_value(t):
    """Midpoint and geometric omitted-tail enclosure of L(t)."""
    t = abs(mp.mpf(t))
    if t == 0:
        return ((mp.pi ** 2 + 8 * mp.catalan) / 4, mp.mpf("0"))
    ratio = mp.exp(-2 * t)
    term_exp = mp.exp(-t / 2)
    one_minus = -mp.expm1(-2 * t)
    total = mp.mpf("0")
    k = 0
    while True:
        lam = 2 * k + mp.mpf("0.5")
        total += term_exp / (lam * lam)
        k += 1
        term_exp *= ratio
        lam_next = 2 * k + mp.mpf("0.5")
        tail = term_exp / (lam_next * lam_next * one_minus)
        if tail <= LERCH_TAIL:
            return total, tail


_ARCH_CACHE = {}


def arch_a(frame, x):
    """Independent continuous archimedean source ball."""
    x = abs(mp.mpf(x))
    t = x * frame.D
    l0, e0 = lerch_value(t)
    lm, em = lerch_value(abs(t - frame.D))
    lp, ep = lerch_value(t + frame.D)
    tri = max(mp.mpf("0"), 1 - t / frame.D)
    constant = (mp.euler + mp.log(mp.pi) + 3 * mp.log(2)
                + mp.pi / 2)
    value = -constant * tri + (2 * l0 - lm - lp) / frame.D
    error = (2 * e0 + em + ep) / frame.D \
        + SOURCE_PAD * (1 + abs(value))
    return value, error


def arch_ladder(frame, theta):
    key = (frame.tag, str(theta))
    if key in _ARCH_CACHE:
        return _ARCH_CACHE[key]
    values, errors = [], []
    for j in range(2 * frame.h + 1):
        value, error = arch_a(frame, abs(mp.mpf(j - 1) + 2 * theta))
        values.append(value)
        errors.append(error)
    _ARCH_CACHE[key] = (values, errors)
    return values, errors


def tent(value, width):
    distance = abs(value)
    return mp.mpf("0") if distance >= width else 1 - distance / width


def atom_ladder(frame, theta, world):
    """High-precision even tent reads on x=j-1+2theta."""
    values = []
    errors = []
    pos = world.positions
    posf = world.positions_float
    masses = world.masses
    D = frame.D
    for j in range(2 * frame.h + 1):
        x = abs(mp.mpf(j - 1) + 2 * theta)
        s = x * D
        lo = max(0, bisect.bisect_left(posf, float(s - D)) - 3)
        hi = min(len(pos), bisect.bisect_right(
            posf, float(s + D)) + 3)
        total = mp.mpf("0")
        for index in range(lo, hi):
            weight = tent(s - pos[index], D)
            if weight:
                total += masses[index] * weight
        # even reflection: tau_D(s+u), possible only for s<D
        if s < D:
            hi_ref = min(len(pos), bisect.bisect_right(
                posf, float(D - s)) + 3)
            for index in range(hi_ref):
                weight = tent(s + pos[index], D)
                if weight:
                    total += masses[index] * weight
        value = -total / 2
        values.append(value)
        errors.append(SOURCE_PAD * (1 + abs(value) + hi - lo))
    return values, errors


def g_sequences(frame, theta, world):
    arch, arch_err = arch_ladder(frame, theta)
    atom, atom_err = atom_ladder(frame, theta, world)
    c = [a + b for a, b in zip(arch, atom)]
    ce = [a + b + SOURCE_PAD * (1 + abs(v))
          for a, b, v in zip(arch_err, atom_err, c)]
    g, ge = [], []
    for r in range(2 * frame.h - 1):
        value = c[r + 1] - (c[r + 2] + c[r]) / 2
        error = ce[r + 1] + (ce[r + 2] + ce[r]) / 2 \
            + SOURCE_PAD * (1 + abs(value))
        g.append(value)
        ge.append(error)
    return g, ge


def source_bundle(frame, theta, world):
    """Toeplitz source at theta=0 plus shifted Hankel source."""
    gt, gte = g_sequences(frame, mp.mpf("0"), world)
    if theta == 0:
        gh, ghe = gt, gte
    else:
        gh, ghe = g_sequences(frame, theta, world)
    return gt, gte, gh, ghe


def build_co_block(frame, gt, gte, gh, ghe):
    """Ball B=Omega[1:,1:] directly from source G balls."""
    dim = frame.h - 1
    gt_balls = [arb_ball(gt[r], gte[r]) for r in range(frame.h)]
    gh_balls = [arb_ball(gh[r], ghe[r])
                for r in range(2 * frame.h - 1)]
    B = arb_mat(dim, dim)
    for i in range(dim):
        m = i + 1
        for j in range(i + 1):
            n = j + 1
            value = (gh_balls[m + n] + gt_balls[m - n]) / 2
            B[i, j] = value
            if i != j:
                B[j, i] = value
    n0 = (gh_balls[0] + gt_balls[0]) / 2
    b = arb_mat(dim, 1)
    for i in range(dim):
        m = i + 1
        b[i, 0] = (gh_balls[m] + gt_balls[m]) / 2
    return B, b, n0


def midpoint_co_block(frame, gt, gh):
    """Binary64 midpoint used only to construct an LDL preconditioner."""
    dim = frame.h - 1
    gt_float = np.asarray([float(value) for value in gt[:frame.h]])
    gh_float = np.asarray([float(value) for value in gh])
    index = np.arange(dim)
    rows = index[:, None] + 1
    cols = index[None, :] + 1
    return 0.5 * (
        gh_float[rows + cols] + gt_float[np.abs(rows - cols)])


def exact_float_ball_matrix(values, lower_triangular=False):
    """Convert exact binary64 values to zero-radius Arb entries."""
    nrows, ncols = values.shape
    out = arb_mat(nrows, ncols)
    if lower_triangular:
        for i in range(nrows):
            for j in range(min(i + 1, ncols)):
                out[i, j] = float(values[i, j])
    else:
        for i in range(nrows):
            for j in range(ncols):
                out[i, j] = float(values[i, j])
    return out


def outward_abs_rowsum(matrix, subtract_identity=False):
    """Rigorous binary64 upper bound for ||matrix-I||_infinity."""
    worst = 0.0
    for i in range(matrix.nrows()):
        terms = []
        for j in range(matrix.ncols()):
            value = matrix[i, j] - (1 if subtract_identity and i == j
                                    else 0)
            upper = float(abs(value).upper())
            terms.append(math.nextafter(upper, math.inf))
        row_sum = math.nextafter(math.fsum(terms), math.inf)
        worst = max(worst, row_sum)
    return worst


def outward_matrix_norms(values):
    """Rigorous binary64 upper bounds for ||R||_1 and ||R||_infinity."""
    row_sums = [
        math.nextafter(math.fsum(abs(float(x)) for x in row), math.inf)
        for row in values
    ]
    col_sums = [
        math.nextafter(
            math.fsum(abs(float(x)) for x in values[:, j]), math.inf)
        for j in range(values.shape[1])
    ]
    return (math.nextafter(max(col_sums), math.inf),
            math.nextafter(max(row_sums), math.inf))


def certify_point(frame, theta, world, label):
    """Congruence-preconditioned interval LDL and Schur solve.

    The binary64 Cholesky is not a sign claim: it constructs an explicitly
    invertible triangular R only.  Arb then forms C=R B R^T from source
    balls and interval-LDL certifies C>0.  Congruence by invertible R proves
    B>0.  The bound C >= (1-rho)I and
    ||R||_2^2 <= ||R||_1||R||_inf gives a certified B eigenvalue surrogate.
    """
    started = time.time()
    gt, gte, gh, ghe = source_bundle(frame, theta, world)
    midpoint = midpoint_co_block(frame, gt, gh)
    try:
        float_factor = np.linalg.cholesky(midpoint)
        inverse_factor = sla.solve_triangular(
            float_factor, np.eye(frame.h - 1),
            lower=True, check_finite=False)
    except np.linalg.LinAlgError:
        elapsed = time.time() - started
        print("    %-22s theta=%-8s B=PRECONDITIONER-REFUSED  %.1f s"
              % (label, str(theta), elapsed), flush=True)
        return dict(label=label, theta=theta, b_pd=False,
                    status="B-REFUSED", elapsed=elapsed,
                    gt=gt, gte=gte, gh=gh, ghe=ghe)
    B, b, n0 = build_co_block(frame, gt, gte, gh, ghe)
    dim = frame.h - 1
    R = exact_float_ball_matrix(inverse_factor, lower_triangular=True)
    transformed = (R * B) * R.transpose()
    rho = outward_abs_rowsum(transformed, subtract_identity=True)
    norm_one, norm_inf = outward_matrix_norms(inverse_factor)
    factor = arb_mat(dim, dim)
    positive = bool(_ARB_LDL(
        arb_ptr(factor), arb_ptr(transformed), ARB_BITS))
    if not positive or not rho < 1.0:
        elapsed = time.time() - started
        print("    %-22s theta=%-8s B=INTERVAL-LDL-REFUSED "
              "rho=%s  %.1f s"
              % (label, str(theta),
                 ("%.3e" % rho) if math.isfinite(rho) else "inf",
                 elapsed), flush=True)
        del B, b, factor, R, transformed
        gc.collect()
        return dict(label=label, theta=theta, b_pd=False,
                    status="B-REFUSED", elapsed=elapsed,
                    gt=gt, gte=gte, gh=gh, ghe=ghe)
    pivot_lowers = [factor[i, i].lower() for i in range(dim)]
    min_transformed_pivot = min(pivot_lowers)
    lambda_lower = math.nextafter(
        (1.0 - rho) / (norm_one * norm_inf), -math.inf)
    z = R * b
    y = arb_mat(dim, 1)
    _ARB_SOLVE_LDL(
        arb_ptr(y), arb_ptr(factor), arb_ptr(z), ARB_BITS)
    q = (z.transpose() * y)[0, 0]
    schur = n0 - q
    slo, shi = arb_bounds(schur)
    elapsed = time.time() - started
    status = "S-POS" if arb_positive(schur) else (
        "S-NONPOS" if arb_nonpositive(schur) else "S-STRADDLE")
    print("    %-22s theta=%-8s B=PD lambda>=%+.6e "
          "C-pivot>=%s rho<=%.3e "
          "s in [%s, %s] %s  %.1f s"
          % (label, str(theta), lambda_lower,
             str(min_transformed_pivot), rho, slo, shi,
             status, elapsed), flush=True)
    del B, b, factor, R, transformed, z, y
    gc.collect()
    return dict(label=label, theta=theta, b_pd=True,
                min_pivot=str(min_transformed_pivot),
                lambda_lower=lambda_lower, rho=rho, schur=schur,
                schur_lo=slo, schur_hi=shi, status=status,
                elapsed=elapsed, gt=gt, gte=gte, gh=gh, ghe=ghe)


def breakpoint_partition(frame, world):
    points = {mp.mpf("0"), mp.mpf("0.5"), mp.mpf("1")}
    for position in world.positions:
        base = mp.frac(position / (2 * frame.D))
        points.add(base)
        points.add(mp.frac(base + mp.mpf("0.5")))
    raw = sorted(points)
    ordered = [raw[0]]
    merged = 0
    for point in raw[1:]:
        if point - ordered[-1] <= 2 * BREAKPOINT_RAD:
            # Exact log relations can present the same kink through
            # different prime powers.  Their outward balls overlap, so
            # consume the union as one breakpoint cluster.
            ordered[-1] = (ordered[-1] + point) / 2
            merged += 1
        else:
            ordered.append(point)
    gaps = [b - a for a, b in zip(ordered[:-1], ordered[1:])]
    disjoint = all(gap > 2 * BREAKPOINT_RAD for gap in gaps)
    return dict(points=ordered, pieces=len(ordered) - 1,
                min_gap=min(gaps), max_gap=max(gaps),
                disjoint=disjoint, merged=merged)


def arch_g(frame, x):
    a0, e0 = arch_a(frame, x)
    ap, ep = arch_a(frame, x + 1)
    am, em = arch_a(frame, abs(x - 1))
    value = a0 - (ap + am) / 2
    error = e0 + (ep + em) / 2 + SOURCE_PAD * (1 + abs(value))
    return arb_ball(value, error)


def full_affinity_ward(frame):
    """A nonzero second difference rigorously rejects full affinity."""
    theta = mp.mpf("0.25")
    delta = mp.mpf(1) / 1024
    gm = arch_g(frame, 2 * (theta - delta))
    g0 = arch_g(frame, 2 * theta)
    gp = arch_g(frame, 2 * (theta + delta))
    second = gp - 2 * g0 + gm
    lo, hi = arb_bounds(second)
    excludes_zero = bool(second.lower() > 0 or second.upper() < 0)
    return dict(second=second, lo=lo, hi=hi,
                full_affine=not excludes_zero)


def source_radius_guard(reference, radius, candidate):
    return abs(candidate - reference) <= radius


def plant_control(point):
    index = len(point["gh"]) // 3
    radius = point["ghe"][index]
    delta = 128 * radius + mp.mpf("1e-65")
    candidate = point["gh"][index] + delta
    accepted = source_radius_guard(
        point["gh"][index], radius, candidate)
    return index, delta, not accepted


def print_honest_mean(frame, partition, affinity, point_rows):
    """Refuse rather than turn finite point balls into a mean claim."""
    all_piece_b = False
    affine = affinity["full_affine"]
    if affine and all_piece_b:
        raise AssertionError("unimplemented branch may not claim a mean")
    result = dict(lo="-inf", hi="+inf", closed=False,
                  reason=("FULL-FAMILY-NONAFFINE"
                          if not affine else
                          "ALL-PIECE-B-PREMISE-UNPROVED"))
    print("    h %d rigorous mean enclosure: [%s, %s]  REFUSED[%s]"
          % (frame.h, result["lo"], result["hi"], result["reason"]))
    print("      partition pieces %d; interval-LDL B certificates "
          "consumed at %d point(s), not at all %d piece endpoints"
          % (partition["pieces"],
             sum(1 for row in point_rows if row["b_pd"]),
             partition["pieces"] + 1))
    return result


def main():
    mp.mp.dps = MP_DPS
    ctx.prec = ARB_BITS
    print("shift_average_deep_probe -- "
          "PRIME.COFINAL.SHIFT.AVERAGE.DEEP.01")
    print("SPEC_SHA %s  MP_DPS %d  ARB_BITS %d"
          % (SPEC_SHA[:16], MP_DPS, ARB_BITS))

    section("S0 -- frozen source firewall + validated LDL bridge")
    bad = ast_firewall()
    check("S0.1 AST has no zero/sign/tau/eigensolver identifier",
          not bad, ",".join(bad) if bad else "clean",
          kill="PIPELINE-BROKEN")
    check("S0.2 FLINT/Arb interval LDL bridge certifies SPD and "
          "refuses an indefinite control", ldl_bridge_ward(),
          "python-flint %s; object offset %d"
          % (flint.__version__, _ARB_OFFSET), kill="PIPELINE-BROKEN")
    if KILLS:
        return finish({}, {}, {}, {})

    section("T -- independent integer prime-power source + exact frames")
    # The larger faithful cap is below 2e6; this is a source budget, not a
    # target sign or a cached table.
    nn, pp = prime_power_table(2_000_000)
    frames = [frame_from_integers(*spec, nn) for spec in TARGETS]
    frame_ok = all(frame.h == frame.expected_h
                   and frame.cap_n <= int(nn[-1]) for frame in frames)
    check("T1 both frames rebuild from integer prime powers",
          frame_ok,
          "; ".join("%s h=%d kz=%d n=%d M=%d cap=%d"
                    % (f.tag, f.h, f.kz, f.source_n, f.M, f.cap_n)
                    for f in frames), kill="PIPELINE-BROKEN")
    if KILLS:
        return finish({}, {}, {}, {})

    genuine = {}
    partitions = {}
    affinities = {}
    point_rows = {}
    support_rows = {}
    control_rows = {}
    mean_rows = {}
    selected = {}

    section("P/A -- exact atom partitions + full-family affinity ward")
    for frame in frames:
        world = genuine_world(frame, nn, pp)
        genuine[frame.tag] = world
        part = breakpoint_partition(frame, world)
        partitions[frame.tag] = part
        print("    %s: atoms %d, pieces %d, min/max gap %s / %s, "
              "merged coincidences %d, outward breakpoint balls %s"
              % (frame.tag, len(world.positions), part["pieces"],
                 mp.nstr(part["min_gap"], 17),
                 mp.nstr(part["max_gap"], 17),
                 part["merged"],
                 "DISJOINT" if part["disjoint"] else "OVERLAP"))
        check("P.%s complete source partition has disjoint outward "
              "breakpoint balls" % frame.tag, part["disjoint"],
              kill="PARTITION-BROKEN")
        affinity = full_affinity_ward(frame)
        affinities[frame.tag] = affinity
        print("      arch G second difference at theta=1/4, "
              "delta=1/1024: [%s, %s] -> full family %s"
              % (affinity["lo"], affinity["hi"],
                 "AFFINE" if affinity["full_affine"] else
                 "NONAFFINE"))
        check("A.%s honesty ward detects the smooth archimedean "
              "non-affinity (therefore HH is not silently consumed)"
              % frame.tag, not affinity["full_affine"],
              kill="AFFINITY-WARD-BROKEN")

    section("D/R/N -- dyadic existence certificates, support cap, plant")
    for frame in frames:
        world = genuine[frame.tag]
        rows = []
        pick = None
        # Denominator order is frozen.  Stop at the first positive ball.
        for dyadic in DYADICS:
            theta = mp.mpf(dyadic.numerator) / dyadic.denominator
            row = certify_point(
                frame, theta, world,
                "%s-DY-%s" % (frame.tag, str(dyadic)))
            rows.append(row)
            if row["status"] == "S-POS":
                pick = dyadic
                break
        point_rows[frame.tag] = rows
        selected[frame.tag] = pick
        check("D.%s source-only denominator-order rule finds a "
              "rigorously positive nonzero dyadic" % frame.tag,
              pick is not None,
              "theta=%s" % pick if pick is not None else "none")

        theta_half = mp.mpf("0.5")
        full_half = rows[0] if rows and rows[0]["theta"] == theta_half \
            else certify_point(
                frame, theta_half, world, frame.tag + "-FULLCAP")
        old_world = genuine_world(frame, nn, pp, old_cap=True)
        old_half = certify_point(
            frame, theta_half, old_world, frame.tag + "-OLDCAP")
        restored = full_half["b_pd"] and not old_half["b_pd"]
        support_rows[frame.tag] = dict(
            full=full_half, old=old_half, restored=restored)
        check("R.%s support regression: 2alpha interval-LDL refuses "
              "and 2alpha+2D certifies B>0 at theta=1/2"
              % frame.tag, restored,
              "old=%s full=%s" % (
                  old_half["status"], full_half["status"]),
              kill="SUPPORT-REGRESSION-BROKEN")

        index, delta, refused = plant_control(full_half)
        check("N.%s source-radius plant at G[%d] shifts by %s and "
              "is refused before matrix consumption"
              % (frame.tag, index, mp.nstr(delta, 8)),
              refused, kill="CONTROL-SILENT")

    section("X -- high-precision SCRAMBLE and EPSTEIN controls")
    epstein = epstein_world()
    for frame in frames:
        world = genuine[frame.tag]
        scramble = scramble_world((frame.alpha, world.masses))
        rows = []
        for control in (scramble, epstein):
            row = certify_point(
                frame, mp.mpf("0.5"), control,
                "%s-%s" % (frame.tag, control.name))
            rows.append(row)
            fired = (not row["b_pd"]
                     or row["status"] == "S-NONPOS")
            check("X.%s.%s control fails/refuses at theta=1/2"
                  % (frame.tag, control.name), fired,
                  row["status"], kill="CONTROL-SILENT")
        control_rows[frame.tag] = rows

    section("M -- rigorous two-sided mean enclosures")
    for frame in frames:
        mean_rows[frame.tag] = print_honest_mean(
            frame, partitions[frame.tag], affinities[frame.tag],
            point_rows[frame.tag])

    return finish(mean_rows, selected, point_rows, support_rows,
                  control_rows)


def finish(mean_rows, selected, point_rows, support_rows,
           control_rows=None):
    section("V -- frozen verdict")
    tags = [spec[0] for spec in TARGETS]
    negative = any(
        row.get("closed") and row.get("hi") not in (None, "+inf")
        and mp.mpf(row["hi"]) < 0
        for row in mean_rows.values())
    closed = [
        tag for tag in tags
        if mean_rows.get(tag, {}).get("closed")
        and mp.mpf(mean_rows[tag]["lo"]) > 0
        and selected.get(tag) is not None
    ]
    if negative:
        verdict = "SHIFTAVGDEEP-NEGATIVE"
    elif len(closed) == 2:
        verdict = "SHIFTAVGDEEP-CERTIFIED"
    elif len(closed) == 1:
        verdict = "SHIFTAVGDEEP-MIXED"
    else:
        verdict = "SHIFTAVGDEEP-INSTRUMENT-EDGE"
    runtime = time.time() - T0
    check("V.1 runtime %.1f s < %.0f s" % (runtime, RUNTIME_BAR),
          runtime < RUNTIME_BAR)
    passed = sum(ok for _name, ok in CHECKS)
    print("\n  VERDICT: %s" % verdict)
    for tag in tags:
        mean = mean_rows.get(tag, {"lo": "n/a", "hi": "n/a"})
        picks = selected.get(tag)
        rows = point_rows.get(tag, [])
        picked_row = next(
            (row for row in rows
             if picks is not None
             and row["theta"] ==
             mp.mpf(picks.numerator) / picks.denominator),
            None)
        print("    %s mean [%s, %s]; theta*=%s%s"
              % (tag, mean.get("lo"), mean.get("hi"),
                 str(picks) if picks is not None else "NONE",
                 (" s=[%s,%s], certified lambda(B) >=%s"
                  % (picked_row["schur_lo"], picked_row["schur_hi"],
                     picked_row["lambda_lower"]))
                 if picked_row else ""))
    print("  The finite denominator-order rule proves existence only at "
          "the listed depths.  It is certificate-conditioned across "
          "depths and does not by itself satisfy H_cof PREDEFINED.")
    print("  NO RH claim; no all-h claim; no marker move.")
    print("\n  checks %d/%d PASS; kills=%s; SPEC_SHA=%s; runtime %.1f s"
          % (passed, len(CHECKS), KILLS if KILLS else "none",
             SPEC_SHA[:16], runtime))
    return 0 if not KILLS else 1


if __name__ == "__main__":
    raise SystemExit(main())
