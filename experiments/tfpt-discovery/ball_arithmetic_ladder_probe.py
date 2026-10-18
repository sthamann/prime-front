#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ball_arithmetic_ladder_probe -- PRIME.PORT.BALLLADDER.01
(EXPLORATION ONLY, experiments/; round 55, the FULL 42-rung
interval-arithmetic rollout, 2026-08-09).

EXTENDS PRIME.PORT.BALLHEAD.01 (ball_arithmetic_head_probe.py,
round 54, verdict BALLHEAD-PROVEN: the three head rungs kz 9/12/13
re-proven with RIGOROUS mpmath.iv interval enclosures through every
transcendental step + the exact integer Bareiss/Sylvester
certificate) to EVERY reachable rung of the deployed v563 window
ladder: the 42 rungs h = 142 .. 878 of PRIME.PORT.CERTIFIED
.LADDER.01/.02 (certified_ladder_probe.py /
certified_ladder_tail_probe.py; previously PROVEN modulo the
stated-but-informal eps_c error model).  After THIS probe,
sigma_h > 0 holds on the WHOLE reachable ladder modulo nothing
except IEEE/mpmath interval correctness (tier 1) resp. the
honestly-labelled validated-precision Cholesky bars run from a
RIGOROUS interval shift (tier 2) -- the informal eps_c model is
retired from the ladder entirely.

ENCLOSURE MACHINERY (verbatim from the head probe; the lemmas are
cited, not re-derived -- see ball_arithmetic_head_probe E1-E4):
 E1  NODE-ENCLOSURE LEMMA (head SPEC v3): the GL-48 nodes are
     enclosed in intervals [x0 -+ r], r = 1e-90 (Newton seeds at mp
     dps 110; P_48 by the interval three-term recurrence at dps
     120 must show a DEFINITE sign change on every interval; all
     48 intervals pairwise disjoint; 2 must lie in the interval
     weight sum).  The tight radius defeats the ~1e16 dependency
     widening in the interval Legendre recurrence for the WEIGHTS
     (the v3 lesson: at r = 1e-70 the weight widths floor at
     ~5e-54 independently of the lag dps).
 E2  ARCHIMEDEAN LAYER: iv.exp / iv.expm1 / iv.log and the
     constants iv.euler / iv.pi, natively outward-rounded; the
     near branch specialised to its only call s = 0 (single panel
     [0, D], tri_s = 1); the far-branch triangle factor via the
     exact identities (1 -+ x)/2; panel ratio values shared
     between adjacent lags (a mechanical cache of identical real
     quantities).
 E3  ATOMS: positions iv.log(n), masses 2 iv.log(spf(n))/iv.sqrt(n)
     on the READ-ONLY v563 atom list; the T115 tent guard
     "if v > 0: add v" transcribed as max0(v) (exactly equivalent
     in real arithmetic); the tent loop range verified rigorously
     per atom (u_j/D inside [i0 - 1, i0 + 1] and u_j > 0); the
     reflection branch applied only at index 0 through max0.
 E4  EXACT DECISION PATH: midpoints/radii by exact fadd/fsub +
     ldexp; the integer grid N = floor(K_mid Q) by exact
     mantissa-shift floor; shift_int = h + ceil_exact(2 h rad_max
     Q) -- no working-precision rounding anywhere in the tier-1
     decision path.

ERROR ACCOUNTING (head probe, verbatim): per entry c_true[i] in
[lo_i, hi_i] (mpmath.iv, rigorous); rad_max = max_i (hi_i-lo_i)/2
(exact); entrywise |K_mid - K_true| <= 2 rad_max, spectral
||K_mid - K_true||_2 <= 2 h rad_max (Frobenius); tier-1 grid
0 <= K_mid Q - N < 1 entrywise, spectral h/Q.

FROZEN PROTOCOL (2026-08-09; the 42 reachable rungs h <= 900,
ascending h; control kz 9; interval lag precision dps 60, node
lemma dps 120):

 E1  the node-enclosure lemma must hold (once, up front).
 T0  FLOAT SURVEY: the deployed float64 assembly must yield the
     frozen count of 42 reachable rungs; lambda_min(K) printed up
     front for every rung.
 C   CONTROL (must fire; runs IMMEDIATELY after the survey so no
     budget event can silently drop it): the Epstein x^2+5y^2 comb
     at kz 9 (von-Mangoldt recursion in INTERVAL arithmetic; the
     support selected by the parent's READ-ONLY float scan)
     through the IDENTICAL interval lag assembly, rigorous shift
     and exact integer Bareiss certificate must hit a nonpositive
     pivot -- the machinery must REFUSE the wall for the wrong
     comb.
 L1  THE ROLLOUT, per rung in ascending h:
     (1) INTERVAL LAG REBUILD (E1-E3, head machinery verbatim) at
         iv dps 60; the rigorous radius bound rad_max is printed;
         gates per rung: the tent-range rigour assertions hold for
         every atom, and the interval MIDPOINTS agree with the
         deployed float64 core lags at relative sup distance
         <= 1e-9 (the cross-implementation ward, unchanged).
     (2) THE RIGOROUS SHIFT: tier 1 shift = 2 h rad_max + h/Q as
         shift_int = h + ceil_exact(2 h rad_max Q) (E4); tier 2
         delta = 2 h rad_max, EXACT (fmul exact) -- and NO
         K-assembly rounding allowance is needed any more, because
         the tier-2 K rows are assembled from the exact midpoints
         by EXACT fsub (unlike the ladder parent's dps-130
         assembly).
     (3) THE CERTIFICATE:
         TIER 1 (h <= 300), "exact-rational (integer Bareiss LDL,
         interval shift)": exact integer fraction-free Bareiss LDL
         of N - (shift_int + m_int) I on the Q = 10^20 grid (every
         division remainder-checked; pivot k = the (k+1)-st
         leading principal minor; Sylvester), with the ladder's
         in-run floor attempt m = 0.5 x lambda_min(f64) and the
         m = 0 retry on refusal; a refusal at m = 0 is a genuine
         refusal (K1).  Reach gate (ladder SPEC v2, prime rungs
         only): float lambda_min >= 100 x the shift bound.
         TIER 2 (h > 300), "validated-precision (mpmath Cholesky
         dps 120/200, interval shift)" -- NOT exact-rational and
         never labelled as such: Cholesky at working dps 120, on
         success RE-RUN at dps 200 (precision doubling); every
         pivot d_j must exceed 10^6 x the accumulated per-pivot
         rounding-bound estimate b_j = 8 (j+2) u (|K_jj - shift|
         + sum_k L_jk^2), u = 2^(2-prec), at BOTH precisions;
         floor attempt m = 0.5 x lambda_min(f64), m = 0 retry.
         Certified only if both passes are PD AND both ratio bars
         hold; nonpositive pivot at dps 200 at m = 0 is a genuine
         refusal (K1); positive pivots below the ratio bar are
         typed out-of-reach, never certified, never a kill.

RUNTIME (frozen): round-54 measured estimate ~8700 s total (tier-1
Bareiss ~7100 s + tier-2 ~1400 s + interval lags ~100 s).  NO
wall-clock cap inside a rung and NO deadline predictor: elapsed
time is printed per rung; ONLY if the run goes wildly over the
estimate (elapsed > 12600 s = 3.5 h, checked BETWEEN rungs, never
interrupting a running rung) are the remaining rungs typed
SKIPPED-BUDGET and printed loudly -- partial coverage is an honest
result.

KILLS: K1 the node lemma fails, a tent-range or ward gate fails on
an attempted rung, or an attempted prime rung above the reach gate
is genuinely refused (tier 1: nonpositive exact pivot at m = 0;
tier 2: nonpositive pivot at dps 200 at m = 0) -> CERT-REFUSED (an
honest kill, reported loudly); K2 the control is certified (does
not fire) -> CONTROL-DEAD.

VERDICT (frozen enum): BALLLADDER-COMPLETE (all 42 rungs certified
with the rigorous interval shift) / BALLLADDER-PARTIAL(n, skipped
list) / CERT-REFUSED / CONTROL-DEAD.

MECHANICAL CACHES (performance only, no protocol content): the
interval atom position/mass PREFIX (the rung atom lists are
prefixes of the one deployed v563 table), the trial-division
smallest-prime-factor memo, and the arch panel-ratio cache inside
one rung (identical real quantities shared between adjacent lags,
as the head probe).

SPEC AMENDMENTS (fail-first history preserved, house precedent):
  v1 (frozen 2026-08-09, pre-run): everything above.  This file
     INHERITS, from the start, the two upstream fail-first
     amendments and documents them here: (i) head SPEC v3 -- the
     node intervals at radius 1e-90 (Newton at mp dps 110) to
     defeat the precision-independent dependency-widening floor of
     the interval Legendre weight recurrence discovered in the
     head's v1/v2 runs; (ii) ladder SPEC v2 -- the reach gate
     applies to PRIME rungs only, so the control always runs its
     certificate (the v1 ordering bug that typed the control
     OUT-OF-REACH instead of REFUSED).  The head's B2 old-model
     comparison is NOT rerun here: the eps_c model was already
     judged there (three-way, SPEC v2) and no certificate below
     depends on it.

NO RH claim: these are finite-h positivity certificates for the 42
reachable rungs of the deployed v563 window ladder; the asymptotic
tail (h -> infinity) is untouched and stays with the registered
port contracts.

FIREWALL: no zeros, no prime oracles (AST scan for zetazero /
nzeros / primerange / isprime / primepi / nextprime / prevprime);
the atom tables come from the deployed v563 window, READ-ONLY; the
only factorisation used is trial-division smallest-prime-factor
recovery on the v563 atom list.  Deterministic, no RNG.  Stdout
only -- writes nothing.  No marker moves.

Sources (read-only): ball_arithmetic_head_probe (round 54, the
interval machinery being rolled out, verbatim);
certified_ladder_probe / certified_ladder_tail_probe (round 40,
the tier split, per-rung recipes and runtime profile);
certified_head_probe (round 40 WP2); v563_paper2_readouts
(window/lag assembly); v866/v876 (wall <=> odd-Toeplitz PSD,
promoted); port_scalar_schur_probe (Epstein control recursion).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ball_arithmetic_ladder_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
from mpmath import iv, mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_LADDER_MAX = 900             # reachable-rung cap (the 42 rungs)
N_RUNGS_EXP = 42               # frozen expected rung count
TIER1_H_MAX = 300              # tier boundary (exact vs validated)
DPS_IV = 60                    # working interval precision (head)
DPS_NODE = 120                 # node-enclosure lemma precision
NODE_R = "1e-90"               # node interval half-width (head v3)
DPS_NEWTON = 110               # Newton dps for the node seeds
DPS_T2 = 120                   # tier-2 Cholesky working precision
DPS_T2V = 200                  # tier-2 verification precision
Q_POW = 20                     # grid denominator Q = 10^20 (head v2)
WARD_REL = 1.0e-9              # cross-implementation ward bar
GL_N = 48                      # the deployed panel order (v563)
REACH_FACTOR = 100.0           # float lam_min >= this x shift bound
PIVOT_FACTOR = 1.0e6           # tier-2 pivot > this x rounding bound
FLOOR_FRAC = 0.5               # floor attempt m = this x lam_f
EST_TOTAL_S = 8700.0           # round-54 measured cost estimate
SOFT_BUDGET_S = 12600.0        # 3.5 h; checked BETWEEN rungs only
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def elapsed():
    return time.time() - T0


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------ interval helpers
def ivsplit(x):
    """Exact mpf endpoints (lo, hi) of an ivmpf."""
    a, b = x._mpi_
    return mp.make_mpf(a), mp.make_mpf(b)


def imax0(x):
    """The interval hull of max(0, x) -- exact for the monotone
    map t -> max(0, t)."""
    lo, hi = ivsplit(x)
    z = mp.mpf(0)
    return iv.mpf([lo if lo > z else z, hi if hi > z else z])


def mid_rad(x):
    """Exact midpoint and radius of an ivmpf (fadd/fsub exact +
    ldexp; no working-precision rounding)."""
    lo, hi = ivsplit(x)
    return (mp.ldexp(mp.fadd(lo, hi, exact=True), -1),
            mp.ldexp(mp.fsub(hi, lo, exact=True), -1))


def mpf_floor_exact(x):
    """Exact floor of a finite mpf via mantissa shift (Python's >>
    floors toward -infinity)."""
    sign, man, exp, _bc = x._mpf_
    if man == 0:
        if exp == 0:
            return 0
        raise ArithmeticError("floor of a special value")
    m = -man if sign else man
    return m << exp if exp >= 0 else m >> (-exp)


def mpf_ceil_exact(x):
    return -mpf_floor_exact(mp.fneg(x, exact=True))


# ------------------------------------------------ E1: node lemma
def legendre_iv(n, x):
    """(P_n(x), P_n'(x)) by the three-term recurrence in mpmath.iv
    -- a finite composition of interval ops, hence rigorous."""
    p0, p1 = iv.mpf(1), x
    for k in range(2, n + 1):
        p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
    dp = n * (x * p1 - p0) / (x * x - 1)
    return p1, dp


def gl_newton_mp(n):
    """Approximate GL nodes by Newton on P_n at the current mp dps
    (the head probe's iteration, nodes only)."""
    xs = []
    tol = mp.mpf(10) ** (-(mp.dps - 6))
    for i in range(n):
        x = mp.cos(mp.pi * (i + mp.mpf(3) / 4) / (n + mp.mpf(1) / 2))
        for _ in range(80):
            p0, p1 = mp.mpf(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < tol:
                break
        xs.append(x)
    return xs


def gl_nodes_enclosed(n):
    """The node-enclosure lemma (E1, head SPEC v3): per node a
    verified interval [x0 - r, x0 + r] with a definite P_n sign
    change, all pairwise disjoint; weights as interval images.
    Returns (X, W, lemma)."""
    with mp.workdps(DPS_NEWTON):
        xs0 = gl_newton_mp(n)
        r = mp.mpf(NODE_R)
        pts = [(x0 - r, x0 + r) for x0 in xs0]
    iv.dps = DPS_NODE
    sign_ok = True
    X, W = [], []
    for lo_pt, hi_pt in pts:
        p_lo, _ = legendre_iv(n, iv.mpf(lo_pt))
        p_hi, _ = legendre_iv(n, iv.mpf(hi_pt))
        la, lb = ivsplit(p_lo)
        ha, hb = ivsplit(p_hi)
        s_lo = 1 if la > 0 else (-1 if lb < 0 else 0)
        s_hi = 1 if ha > 0 else (-1 if hb < 0 else 0)
        if s_lo * s_hi != -1:
            sign_ok = False
        Xi = iv.mpf([lo_pt, hi_pt])
        _, dpi = legendre_iv(n, Xi)
        X.append(Xi)
        W.append(2 / ((1 - Xi * Xi) * dpi * dpi))
    ends = [ivsplit(x) for x in X]
    order = sorted(range(n), key=lambda i: ends[i][0])
    disjoint = all(ends[order[k]][1] < ends[order[k + 1]][0]
                   for k in range(n - 1))
    wsum = iv.mpf(0)
    for w in W:
        wsum += w
    contains2 = iv.mpf(2) in wsum
    iv.dps = DPS_IV
    return X, W, dict(sign_ok=sign_ok, disjoint=disjoint,
                      contains2=contains2,
                      wsum_delta=float(ivsplit(wsum.delta)[1]))


# ------------------------------------------------ E2/E3: iv lags
def arch_lags_iv(M, D, glX, glW):
    """The archimedean lags as intervals (E2, head verbatim).
    Panel cache: panel k covers [kD, (k+1)D] with node abscissae
    w = kD + D/2 + (D/2)x; the ratio exp(-w/2)/(-expm1(-2w)) is
    shared between the two adjacent lags that integrate over the
    panel (identical real quantity).  Far lag i (i >= 1) uses
    panels i-1 and i with the exact triangle identities (1+x)/2
    and (1-x)/2; the near branch (only i = 0, s = 0) uses panel 0
    with tri_s = 1 and S = max0((1-x)/2)."""
    half = D / 2
    ratio = []                 # ratio[k][j]
    e2w0 = []                  # exp(-2w) on panel 0 (near branch)
    for k in range(M):
        base = k * D + half
        row = []
        for j in range(GL_N):
            w = base + half * glX[j]
            row.append(iv.exp(-w / 2) / (-iv.expm1(-2 * w)))
            if k == 0:
                e2w0.append(iv.exp(-2 * (base + half * glX[j])))
        ratio.append(row)
    w_below = [glW[j] * (1 + glX[j]) / 2 for j in range(GL_N)]
    w_above = [glW[j] * (1 - glX[j]) / 2 for j in range(GL_N)]
    out = [None] * M
    for i in range(1, M):
        acc = iv.mpf(0)
        rb, ra = ratio[i - 1], ratio[i]
        for j in range(GL_N):
            acc += w_below[j] * rb[j] + w_above[j] * ra[j]
        out[i] = -half * acc
    # near branch, i = 0 (s = 0): single panel [0, D], W = D
    tot = iv.mpf(0)
    for j in range(GL_N):
        S = imax0((1 - glX[j]) / 2)
        w = half + half * glX[j]
        num = e2w0[j] - S * iv.exp(-w / 2)
        tot += half * glW[j] * (num / (-iv.expm1(-2 * w)))
    out[0] = (-(iv.euler + iv.log(iv.pi)) + 2 * tot
              - iv.log(-iv.expm1(-2 * D)))
    return out


def atom_lags_iv(alpha, M, uu, mm):
    """The T115 tent atoms as intervals (E3, head verbatim).
    Guard 'if v > 0: add' transcribed as max0(v); loop-range
    sufficiency verified per atom (range_ok); the reflection
    branch applied only at index 0 (for i >= 1 its tent value is
    < 0 rigorously since u_j > 0)."""
    D = 2 * alpha / M
    c = [iv.mpf(0)] * M
    range_ok = True
    for u_j, mu_j in zip(uu, mm):
        u_lo, _u_hi = ivsplit(u_j)
        if not u_lo > 0:
            range_ok = False
        t = u_j / D
        t_lo, t_hi = ivsplit(t)
        i0 = int(math.floor(float(mp.ldexp(
            mp.fadd(t_lo, t_hi, exact=True), -1))))
        if not (t_lo >= i0 - 1 and t_hi <= i0 + 1):
            range_ok = False
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1 - abs(i * D - u_j) / D
            c[i] = c[i] - mu_j * imax0(v) / 2
        c[0] = c[0] - mu_j * imax0(1 - u_j / D) / 2
    return c, range_ok


_SPF_CACHE = {}


def spf(n):
    """Smallest prime factor by trial division (n is a prime power
    from the READ-ONLY v563 atom list, so spf(n) = its base p);
    memoised."""
    if n in _SPF_CACHE:
        return _SPF_CACHE[n]
    d = 2
    while d * d <= n:
        if n % d == 0:
            _SPF_CACHE[n] = d
            return d
        d += 1
    _SPF_CACHE[n] = n
    return n


_ATOM_IV = {"uu": [], "mm": []}


def atom_arrays_iv(ka):
    """The first ka interval atom positions log n and masses
    2 log p / sqrt(n) at iv dps DPS_IV.  The rung atom lists are
    PREFIXES of the one deployed v563 table, so the cache extends
    lazily (mechanical cache, no protocol content)."""
    uu, mm = _ATOM_IV["uu"], _ATOM_IV["mm"]
    while len(uu) < ka:
        n = int(core._NN[len(uu)])
        p = spf(n)
        uu.append(iv.log(n))
        mm.append(2 * iv.log(p) / iv.sqrt(n))
    return uu[:ka], mm[:ka]


def lambda_eps_iv(N):
    """The Epstein x^2+5y^2 von-Mangoldt recursion (round-39
    control) in INTERVAL arithmetic: a_n exact rationals, iv.log."""
    r = [0] * (N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1
    a = [iv.mpf(t) / 2 for t in r]
    lam = [iv.mpf(0)] * (N + 1)
    for n in range(2, N + 1):
        acc = a[n] * iv.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def lags_iv(spec):
    """The full interval lag vector of one rung at iv dps DPS_IV
    (E1-E3, head verbatim).  Returns (mid list, rad list,
    range_ok)."""
    iv.dps = DPS_IV
    alpha = iv.log(spec["n_zone"])
    M = spec["M"]
    if spec["kind"] == "prime":
        uu, mm = atom_arrays_iv(spec["ka"])
    else:
        lamE = lambda_eps_iv(spec["N_E"])
        uu = [iv.log(n) for n in spec["nn"]]
        mm = [2 * lamE[n] / iv.sqrt(n) for n in spec["nn"]]
    D = 2 * alpha / M
    c_ar = arch_lags_iv(M, D, _GLX, _GLW)
    c_at, range_ok = atom_lags_iv(alpha, M, uu, mm)
    mids, rads = [], []
    for i in range(M):
        m_i, r_i = mid_rad(c_ar[i] + c_at[i])
        mids.append(m_i)
        rads.append(r_i)
    return mids, rads, range_ok


# --------------------- Epstein float support scan (READ-ONLY, mpf)
def lambda_eps_mp(N):
    """The Epstein recursion in plain mpmath -- used ONLY for the
    parent's READ-ONLY float support scan of the control."""
    r = [0] * (N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1
    a = [mp.mpf(t) / 2 for t in r]
    lam = [mp.mpf(0)] * (N + 1)
    for n in range(2, N + 1):
        acc = a[n] * mp.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


# ------------------------------------------------ exact certificate
def bareiss_pd(A):
    """Exact integer fraction-free LDL (Bareiss).  Pivot k equals
    the (k+1)-st leading principal minor; all pivots > 0 <=> PD
    (Sylvester).  Every exact division is remainder-checked."""
    n = len(A)
    A = [row[:] for row in A]
    prev = 1
    for k in range(n):
        piv = A[k][k]
        if piv <= 0:
            return False, k, piv
        for i in range(k + 1, n):
            Ai, Ak, aik = A[i], A[k], A[i][k]
            for j in range(i, n):
                q, r = divmod(piv * Ai[j] - aik * Ak[j], prev)
                if r:
                    raise ArithmeticError("Bareiss divisibility broken")
                Ai[j] = q
        for i in range(k + 1, n):
            Ai = A[i]
            for j in range(k + 1, i):
                Ai[j] = A[j][i]
        prev = piv
    return True, n, None


def grid_matrix_exact(mids, M, QM):
    """N = floor(K_mid Q) with EXACT arithmetic (E4): entries from
    exact fsub, exact fmul by Q, exact mantissa-shift floor."""
    h = M // 2
    N = [[0] * h for _ in range(h)]
    for i in range(h):
        for j in range(i, h):
            kij = mp.fsub(mids[abs(i - j)], mids[(M - 1) - i - j],
                          exact=True)
            N[i][j] = N[j][i] = mpf_floor_exact(
                mp.fmul(kij, QM, exact=True))
    return N


def rigorous_shift_int(h, rad_max, QM):
    """shift_int = h + ceil(2 h rad_max Q), all exact (E4)."""
    prod = mp.fmul(mp.fmul(rad_max, mp.mpf(2 * h), exact=True),
                   QM, exact=True)
    return h + mpf_ceil_exact(prod)


# ------------------------------------------- tier-2 (validated)
def build_K_rows_exact(mids, M):
    """Lower-triangular K = odd_toeplitz(c_mid, M) with EXACT mpf
    entries (fsub exact) -- NO assembly rounding, so the tier-2
    shift needs no rounding allowance (unlike the ladder parent's
    dps-130 assembly)."""
    h = M // 2
    return [[mp.fsub(mids[abs(i - j)], mids[(M - 1) - i - j],
                     exact=True)
             for j in range(i + 1)] for i in range(h)]


def chol_pass(Krows, shift, dps):
    """One Cholesky pass at working dps with the per-pivot rounding
    bound b_j = 8 (j+2) u (|K_jj - shift| + sum L_jk^2); returns
    (pd_ok, min pivot/bound ratio, pivots_done, first_bad_pivot)
    -- ladder parent, verbatim."""
    h = len(Krows)
    with mp.workdps(dps):
        u = mp.mpf(2) ** (2 - mp.prec)
        sh = mp.mpf(shift)
        Ld, Lo = [], []
        min_ratio = mp.inf
        fdot = mp.fdot
        for i in range(h):
            Ki = Krows[i]
            Li = []
            for j in range(i):
                s = fdot(Li, Lo[j])
                Li.append((Ki[j] - s) / Ld[j])
            s2 = fdot(Li, Li)
            d = Ki[i] - sh - s2
            if d <= 0:
                return False, float(min_ratio), i, d
            bnd = 8 * (i + 2) * u * (abs(Ki[i] - sh) + s2)
            ratio = d / bnd
            if ratio < min_ratio:
                min_ratio = ratio
            Ld.append(mp.sqrt(d))
            Lo.append(Li)
        return True, float(min_ratio), h, None


# ------------------------------------------------ per-rung driver
def certify_rung_ball(spec, c_f, lam_f):
    """One rung end to end: interval rebuild (L1.1), rigorous shift
    (L1.2), tier-1 exact Bareiss or tier-2 validated Cholesky
    (L1.3), with the ladder's floor attempt m = 0.5 lam_f and m = 0
    retry."""
    M, h = spec["M"], spec["M"] // 2
    Q = 10 ** Q_POW
    with mp.workdps(40):
        QM = mp.mpf(Q)                      # exact (47-bit mantissa)
    t0 = time.time()
    mids, rads, range_ok = lags_iv(spec)
    t_iv = time.time() - t0
    rad_max = rads[0]
    for r_ in rads[1:]:
        if r_ > rad_max:
            rad_max = r_
    with mp.workdps(80):
        ward = float(max(abs(a - mp.mpf(b))
                         for a, b in zip(mids, c_f))
                     / max(abs(mp.mpf(b)) for b in c_f))
    out = dict(h=h, rad_max=rad_max, ward=ward, lam_f=lam_f,
               t_iv=t_iv, t_cert=0.0, floor=None, npiv=0, bad=None,
               ratio=None, range_ok=range_ok)
    if h <= TIER1_H_MAX:
        # ---- tier 1: exact-rational, rigorous interval shift
        out["mode"] = "exact-rational (integer Bareiss LDL, " \
                      "interval shift)"
        shift_int = rigorous_shift_int(h, rad_max, QM)
        with mp.workdps(60):
            s_riv = float(mp.mpf(shift_int) / QM)
        out["shift"] = s_riv
        if spec["kind"] == "prime" and lam_f < REACH_FACTOR * s_riv:
            out["status"] = "out-of-reach"
            return out
        N = grid_matrix_exact(mids, M, QM)
        t0 = time.time()
        m_int = int(FLOOR_FRAC * max(lam_f, 0.0) * Q)
        ok, npiv, bad = bareiss_pd(
            [[N[i][j] - (shift_int + m_int if i == j else 0)
              for j in range(h)] for i in range(h)])
        if ok:
            out.update(status="certified", floor=m_int / Q,
                       npiv=npiv)
        elif m_int > 0:
            ok0, npiv0, bad0 = bareiss_pd(
                [[N[i][j] - (shift_int if i == j else 0)
                  for j in range(h)] for i in range(h)])
            if ok0:
                out.update(status="certified", floor=0.0,
                           npiv=npiv0)
            else:
                out.update(status="refused", npiv=npiv0, bad=bad0)
        else:
            out.update(status="refused", npiv=npiv, bad=bad)
        out["t_cert"] = time.time() - t0
        return out
    # ---- tier 2: validated-precision, rigorous interval shift
    out["mode"] = "validated-precision (mpmath Cholesky dps " \
                  "%d/%d, interval shift)" % (DPS_T2, DPS_T2V)
    delta = mp.fmul(rad_max, mp.mpf(2 * h), exact=True)   # EXACT
    out["shift"] = float(delta)
    if lam_f < REACH_FACTOR * float(delta):
        out["status"] = "out-of-reach"
        return out
    Krows = build_K_rows_exact(mids, M)
    t0 = time.time()
    for m in ((FLOOR_FRAC * max(lam_f, 0.0)), 0.0):
        sh = mp.fadd(delta, mp.mpf(m), exact=True)        # EXACT
        ok1, r1, n1, _b1 = chol_pass(Krows, sh, DPS_T2)
        ok2, r2, n2, _b2 = chol_pass(Krows, sh, DPS_T2V)
        if ok1 and ok2 and r1 >= PIVOT_FACTOR and r2 >= PIVOT_FACTOR:
            out.update(status="certified", floor=m, npiv=n2,
                       ratio=min(r1, r2))
            break
        if not ok2 and m == 0.0:
            out.update(status="refused", npiv=n2, bad=_b2, ratio=r2)
            break
        if ok2 and m == 0.0:
            # positive pivots but the validation bar missed
            out.update(status="out-of-reach", npiv=n2,
                       ratio=min(r1, r2))
            break
    out["t_cert"] = time.time() - t0
    return out


# ------------------------------------------------ survey and control
def rung_survey(kz):
    """One rung's deployed float64 assembly: geometry, lags, K and
    lambda_min(K) -- the frame_a_zones/build_window formulas,
    verbatim (ladder parent)."""
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    h = M // 2
    ka = core.atoms_in(alpha)
    c_at, D = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    c_f = core.arch_lags(M, D) + c_at
    lam_f = float(np.linalg.eigvalsh(core.odd_toeplitz(c_f, M))[0])
    return dict(kz=kz, h=h, M=M, alpha=alpha, ka=ka,
                n_zone=int(core._NN[kz]), c_f=list(c_f), lam_f=lam_f)


def run_control_ball():
    """The Epstein x^2+5y^2 comb at kz 9 through the IDENTICAL
    interval machinery (head-probe control, verbatim) -- must be
    REFUSED."""
    r9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * r9["alpha"]))) + 1
    lamE = np.zeros(N_E + 1)
    with mp.workdps(30):
        for n, v in enumerate(lambda_eps_mp(N_E)):
            lamE[n] = float(v)
    nn = [int(n) for n in np.nonzero(np.abs(lamE) > 1e-12)[0]]
    spec_e = dict(kind="epstein", M=r9["M"], n_zone=r9["n_zone"],
                  N_E=N_E, nn=nn)
    uuE = np.log(np.asarray(nn, float))
    mmE = 2.0 * lamE[nn] / np.sqrt(np.asarray(nn, float))
    c_atE, _ = core.atom_lags_at(r9["alpha"], r9["M"], uuE, mmE)
    c_fE = list(core.arch_lags(r9["M"], r9["D"]) + c_atE)
    lam_fE = float(np.linalg.eigvalsh(
        core.odd_toeplitz(np.asarray(c_fE), r9["M"]))[0])
    return certify_rung_ball(spec_e, c_fE, lam_fE)


_GLX = _GLW = None


def main():
    global _GLX, _GLW
    section("PRIME.PORT.BALLLADDER.01 -- the FULL 42-rung interval-"
            "arithmetic rollout (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Tiers: h <= %d exact-"
          "rational (Bareiss, Q = 10^%d, rigorous interval shift); "
          "h > %d validated-precision (Cholesky dps %d/%d, rigorous "
          "interval shift).  Round-54 cost estimate ~%.0f s; soft "
          "budget %.0f s checked between rungs only."
          % (TIER1_H_MAX, Q_POW, TIER1_H_MAX, DPS_T2, DPS_T2V,
             EST_TOTAL_S, SOFT_BUDGET_S))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("E1 -- node-enclosure lemma (head SPEC v3, r = %s)"
            % NODE_R)
    t0 = time.time()
    _GLX, _GLW, lemma = gl_nodes_enclosed(GL_N)
    print("    GL-%d node lemma: %d sign-change intervals of radius "
          "%s at iv dps %d | pairwise disjoint %s | weight-sum "
          "interval width %.1e | %.1f s"
          % (GL_N, GL_N, NODE_R, DPS_NODE, lemma["disjoint"],
             lemma["wsum_delta"], time.time() - t0), flush=True)
    check("E1.1 NODE LEMMA: definite P_%d sign change on every "
          "node interval, all %d intervals pairwise disjoint, and "
          "2 lies in the interval weight sum" % (GL_N, GL_N),
          lemma["sign_ok"] and lemma["disjoint"]
          and lemma["contains2"], kill="K1")

    section("T0 -- float survey: lambda_min(K) on every reachable "
            "rung (h <= %d)" % H_LADDER_MAX)
    rungs = []
    for kz in core.frame_a_zones():
        r = rung_survey(kz)
        if r["h"] <= H_LADDER_MAX:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("T0.1 frozen rung count: %d reachable rungs" % N_RUNGS_EXP,
          len(rungs) == N_RUNGS_EXP, "found %d" % len(rungs))
    print("\n    kz   h     M     n_zone   alpha    lam_min(f64)")
    for r in rungs:
        print("    %-4d %-5d %-5d %-8d %-8.3f %13.4e"
              % (r["kz"], r["h"], r["M"], r["n_zone"], r["alpha"],
                 r["lam_f"]), flush=True)
    n_pos = sum(1 for r in rungs if r["lam_f"] > 0)
    check("T0.2 float floors positive on all rungs (informative)",
          n_pos == len(rungs), "%d/%d positive" % (n_pos, len(rungs)))
    print("    [survey done at %.1f s]" % elapsed())

    section("C -- control (kz 9, Epstein x^2+5y^2 comb through the "
            "IDENTICAL interval machinery; runs before the ladder)")
    res_e = run_control_ball()
    print("    Epstein : h %d | iv rebuild %.1f s | rad_max %s | "
          "ward rel %.2e | pivots done %d | first bad pivot index "
          "%s | lam_min(f64) %.3e | certificate %s"
          % (res_e["h"], res_e["t_iv"],
             mp.nstr(res_e["rad_max"], 3), res_e["ward"],
             res_e["npiv"],
             res_e["npiv"] if res_e["status"] == "refused" else "-",
             res_e["lam_f"],
             "REFUSED (fires)" if res_e["status"] == "refused"
             else res_e["status"].upper()), flush=True)
    check("C0 control ward: the interval Epstein midpoints match "
          "the float64 assembly at rel <= %.0e" % WARD_REL,
          res_e["ward"] <= WARD_REL, kill="K1")
    check("C1 CONTROL FIRES: the interval machinery hits a "
          "nonpositive pivot on the Epstein comb -- the wall is "
          "REFUSED for the wrong comb",
          res_e["status"] == "refused", kill="K2")
    print("    [control done at %.1f s]" % elapsed())

    section("L1 -- the rollout (ascending h; elapsed printed per "
            "rung; NO per-rung cap; soft budget %.0f s between "
            "rungs)" % SOFT_BUDGET_S)
    results = {}

    def report(r, res):
        results[r["kz"]] = res
        st = res["status"]
        extra = ""
        if st == "certified":
            extra = "floor >= %.3e" % res["floor"]
            if res.get("ratio") is not None:
                extra += " | pivot/bound %.1e" % res["ratio"]
        elif st == "out-of-reach":
            if res.get("ratio") is not None:
                extra = ("ratio bar missed: min pivot/bound %.1e < "
                         "%.0e" % (res["ratio"], PIVOT_FACTOR))
            else:
                extra = ("gap: lam_f %.3e < %.0f x shift %.3e"
                         % (res["lam_f"], REACH_FACTOR,
                            res["shift"]))
        elif st == "refused":
            extra = "first bad pivot index %s" % res["npiv"]
        print("    kz %-4d h %-4d %-58s %-12s rad_max %s | shift "
              "%.2e | ward %.1e | %s | iv %.1fs cert %.1fs | "
              "t %.0fs"
              % (r["kz"], r["h"], res["mode"], st.upper(),
                 mp.nstr(res["rad_max"], 3), res["shift"],
                 res["ward"], extra, res["t_iv"], res["t_cert"],
                 elapsed()), flush=True)

    skipped = []
    for r in rungs:
        if elapsed() > SOFT_BUDGET_S:
            skipped.append(r)
            results[r["kz"]] = dict(h=r["h"],
                                    status="skipped-budget",
                                    mode="-", ward=0.0, shift=0.0,
                                    lam_f=r["lam_f"], floor=None,
                                    rad_max=mp.mpf(0),
                                    range_ok=True, t_iv=0.0,
                                    t_cert=0.0)
            continue
        spec = dict(kind="prime", M=r["M"], n_zone=r["n_zone"],
                    ka=r["ka"])
        res = certify_rung_ball(spec, r["c_f"], r["lam_f"])
        report(r, res)
    if skipped:
        print("    [SKIPPED-BUDGET (soft cap %.0f s exceeded): %s]"
              % (SOFT_BUDGET_S,
                 [(r["kz"], r["h"]) for r in skipped]), flush=True)

    # ---- gates over the attempted rungs
    attempted = [(r, results[r["kz"]]) for r in rungs
                 if results[r["kz"]]["status"] in
                 ("certified", "refused", "out-of-reach")]
    att_t1 = [(r, x) for r, x in attempted
              if x["mode"].startswith("exact-rational")]
    att_t2 = [(r, x) for r, x in attempted
              if x["mode"].startswith("validated-precision")]
    check("L1.1 tent-range rigour: the interval u_j/D sits inside "
          "[i0-1, i0+1] and u_j > 0 for every atom on every "
          "attempted rung",
          all(x["range_ok"] for _r, x in attempted), kill="K1")
    check("L1.2 CROSS-IMPLEMENTATION WARD: interval midpoints == "
          "deployed float64 core lags at rel <= %.0e on every "
          "attempted rung" % WARD_REL,
          all(x["ward"] <= WARD_REL for _r, x in attempted),
          kill="K1")
    check("L1.3 TIER-1: no attempted exact-rational rung refused "
          "(%d attempted)" % len(att_t1),
          all(x["status"] != "refused" for _r, x in att_t1),
          kill="K1")
    check("L1.4 TIER-2: no attempted validated-precision rung "
          "refused (%d attempted; certified ones passed both dps "
          "%d/%d and the 10^6 pivot-vs-bound bar)"
          % (len(att_t2), DPS_T2, DPS_T2V),
          all(x["status"] != "refused" for _r, x in att_t2),
          kill="K1")

    section("CENSUS -- per-rung certificate table")
    n_cert = n_oor = n_skip = n_ref = 0
    print("    kz   h     status          mode                     "
          "                          rad_max    shift      floor")
    for r in rungs:
        x = results[r["kz"]]
        st = x["status"]
        n_cert += st == "certified"
        n_oor += st == "out-of-reach"
        n_skip += st == "skipped-budget"
        n_ref += st == "refused"
        fl = ("%.3e" % x["floor"]) if x.get("floor") is not None \
            else "-"
        print("    %-4d %-5d %-15s %-58s %-10s %-10s %s"
              % (r["kz"], r["h"], st.upper(), x["mode"],
                 mp.nstr(x["rad_max"], 3) if st != "skipped-budget"
                 else "-",
                 ("%.2e" % x["shift"]) if st != "skipped-budget"
                 else "-", fl), flush=True)
    print("\n    BALL-PROVEN %d/%d | out-of-reach %d | "
          "skipped-budget %d | refused %d"
          % (n_cert, len(rungs), n_oor, n_skip, n_ref))

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "K2" in KILLS:
        VERDICT = "CONTROL-DEAD"
    elif "K1" in KILLS:
        VERDICT = "CERT-REFUSED"
    elif n_cert == len(rungs):
        VERDICT = "BALLLADDER-COMPLETE"
    else:
        rest = ", ".join("kz %d h %d %s" % (r["kz"], r["h"],
                                            results[r["kz"]]
                                            ["status"])
                         for r in rungs
                         if results[r["kz"]]["status"]
                         != "certified")
        VERDICT = "BALLLADDER-PARTIAL(%d; %s)" % (n_cert, rest)
    print("\n  VERDICT: %s" % VERDICT)
    print("""
  DELIVERABLE: the rigorous ball-arithmetic certificates of
  PRIME.PORT.BALLHEAD.01, extended from the three head rungs to
  ALL %d reachable rungs of the deployed v563 window ladder --
  interval lag enclosures through every transcendental step
  (node-enclosure lemma + native interval exp/expm1/log/sqrt),
  the rigorous shift 2 h rad_max (+ h/Q on the tier-1 grid), the
  exact integer Bareiss/Sylvester certificate (h <= %d) and the
  validated-precision Cholesky bars (h > %d, labelled honestly).
  sigma_h > 0 now holds on the certified rungs modulo nothing but
  IEEE/mpmath interval correctness (tier 1) resp. the stated
  validated-precision bars (tier 2); the informal eps_c model is
  retired.  The asymptotic tail stays with the port contracts.
  NO RH claim.""" % (len(rungs), TIER1_H_MAX, TIER1_H_MAX))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (elapsed(), n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
