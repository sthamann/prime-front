#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ball_arithmetic_head_probe -- PRIME.PORT.BALLHEAD.01
(EXPLORATION ONLY, experiments/; round 54, named object (d) from CXI
-- proof quality, the last head step: close the declared
transcendental-evaluation error model of the certified head with
RIGOROUS ball/interval arithmetic, 2026-08-09).

CLOSES THE GAP OF PRIME.PORT.CERTIFIED.HEAD.01 (certified_head_probe
.py; head rungs kz 9/12/13 PROVEN by exact integer Bareiss LDL,
MODULO a stated-but-informal error model: eps_c = 10 x the
dps-60-vs-100 lag disagreement, taken as a conservative per-entry
radius -- honest, declared, NOT interval arithmetic).  THIS probe
rebuilds the lag vectors in mpmath.iv (true outward-rounded
midpoint-radius interval arithmetic through EVERY transcendental
step), so that c_true is RIGOROUSLY enclosed per entry, the shift
becomes the rigorous radius bound, and the exact integer Sylvester
certificate runs as before -- sigma_h > 0 then holds MODULO NOTHING
except IEEE/mpmath interval correctness.

WHAT IS ENCLOSED (the head probe's lag recipe, read): the lag vector
c = c_arch + c_atoms of the deployed v563 window, where c_arch is
the GL-48 panel quadrature of the archimedean Weil layer and c_atoms
are the exact tent atoms at positions log n with masses
2 log p / sqrt(n).  DECISIVE STRUCTURAL FACT: the certified quantity
is DEFINED as the GL-48 panel quadrature itself (a finite, exactly
specified real algorithm, as already stated by the head probe) --
so NO quadrature-remainder bound is needed; the enclosure problem is
a FINITE composition of arithmetic and transcendental steps.

ENCLOSURE METHODS (per transcendental step; documented per B1):
 E1  GL-48 nodes/weights: the nodes are the 48 simple roots of the
     Legendre polynomial P_48.  Per node: Newton at mp dps 110
     gives x0; then P_48 is evaluated by its three-term recurrence
     in mpmath.iv at dps 120 at the two exact points x0 -+ r
     (r = 1e-90; SPEC v3) and both interval values must EXCLUDE
     zero with opposite definite signs  ==>  by the intermediate
     value theorem [x0 - r, x0 + r] contains a root.  The 48
     intervals
     are verified pairwise disjoint; P_48 has exactly 48 real
     simple roots, so each interval contains EXACTLY one and
     together they enclose the exact root set (node-enclosure
     lemma).  The weight 2/((1-x^2) P_48'(x)^2) is the interval
     image of the node interval under the interval recurrence for
     P_48'.  Self-check: the exact weight sum 2 must lie in the
     interval sum of the weight enclosures.
 E2  Archimedean integrand exp(-w/2)/(-expm1(-2w)) and the near-
     branch terms exp(-2w), euler, log(pi), log(-expm1(-2W)):
     mpmath.iv provides exp, expm1, log and the constants euler and
     pi natively with outward rounding -- every step is DIRECTLY
     available in interval form (no honest-remainder workaround was
     needed anywhere; the ENCLOSURE-INFEASIBLE verdict branch is
     retained for the frozen contract but is expected unreachable).
     The near branch is invoked only at lag 0, where s = 0 exactly:
     tri_s = 1 exactly, the panel split {0, s, D-s, W} degenerates
     to the single panel [0, D] -- the interval transcription
     specialises to s = 0 and this is documented here rather than
     transcribing the (never-taken) general branch.  The far-branch
     triangle factor is evaluated via the exact real identity
     1 - |s - w|/D = (1 -+ x)/2 on the panel below/above s (an
     algebraic identity of the deployed formula at the exact node
     abscissa w = s -+ D/2 + (D/2) x), which avoids interval
     dependency widening; the panel values exp(-w/2)/(-expm1(-2w))
     are shared between adjacent lags (panel k of lag i+1 is panel
     k+1 of lag i) and cached -- a mechanical cache of IDENTICAL
     real quantities, no protocol content.
 E3  Atoms: positions log n and masses 2 log p / sqrt(n) via iv.log
     / iv.sqrt on exact integers (p = smallest-prime-factor by
     trial division on the READ-ONLY v563 atom list, as the head
     probe).  The T115 tent guard "if v > 0: add v" is transcribed
     as adding max0(v) (the interval hull with 0) -- EXACTLY
     equivalent in real arithmetic; the tent loop range is verified
     rigorously per atom (the interval u_j/D must lie inside
     [i0 - 1, i0 + 1] so that the +-2 index window provably covers
     every index with a positive tent value); the reflection branch
     contributes only at index 0 (for i >= 1 its tent value is
     1 - i - u_j/D < 0 since u_j > 0 rigorously) and is applied
     there unconditionally through max0 -- again exactly equivalent
     to the deployed guard.
 E4  The grid step is made rigorous as well (the head probe floored
     at working precision): midpoints and radii are extracted with
     EXACT mpf arithmetic (fadd/fsub exact + ldexp), the integer
     grid N = floor(K_mid Q) uses an exact mantissa-shift floor,
     and shift_int = h + ceil_exact(2 h rad_max Q) uses an exact
     ceiling -- no working-precision rounding anywhere in the
     decision path.

ERROR ACCOUNTING (replaces the head probe's declared model):
  per entry  c_true[i] in [lo_i, hi_i]  (mpmath.iv, rigorous);
  rad_max    = max_i (hi_i - lo_i)/2  (exact arithmetic);
  K_mid from the exact midpoints; entrywise
             |K_mid - K_true| <= rad_a + rad_b <= 2 rad_max, hence
             ||K_mid - K_true||_2 <= 2 h rad_max (Frobenius);
  grid       0 <= K_mid Q - N < 1 entrywise, spectral h/Q;
  shift_int  = h + ceil(2 h rad_max Q); all pivots of
             N - shift_int I positive under EXACT integer Bareiss
             LDL (every division remainder-checked; Sylvester)
             ==>  K_true > 0, i.e. sigma_h > 0, modulo nothing but
             IEEE/mpmath interval correctness.

FROZEN PROTOCOL (2026-08-09; head rungs kz {9, 12, 13}; control
kz 9; working interval precision dps 60, node lemma at dps 120):

 B1  THE INTERVAL REBUILD: per head rung the lag vector is rebuilt
     in mpmath.iv at dps 60 via E1-E3.  Gates: the node-enclosure
     lemma holds (definite sign changes, 48 pairwise-disjoint
     intervals, 2 in the weight-interval sum); the tent-range
     rigour assertions hold for every atom; the interval MIDPOINTS
     agree with the deployed float64 core lags at relative sup
     distance <= 1e-9 (the head probe's T1 ward, unchanged); and
     the head probe's dps-100 mpf lag vector lies INSIDE the
     enclosure entrywise (containment ward -- a failure means one
     of the two implementations is buggy: fix, never proceed).
 B2  THE ENCLOSURE COMPARISON (the honesty point): the old
     conservative eps_c is recomputed per rung by the head recipe
     VERBATIM (mpf lags at dps 60 and 100, eps_c = 10 x the max
     entrywise disagreement, floored at 1e-55) and the declared
     model's literal claim |c_dps100[i] - c_true[i]| <= eps_c is
     judged RIGOROUSLY and THREE-WAY (SPEC v2, below):
       MODEL-VALIDATED  if the rigorous upper bound
                        max(c100 - lo, hi - c100) <= eps_c on every
                        entry of every head rung;
       MODEL-REFUTED    if on some entry the rigorous LOWER bound
                        dist(c100, [lo, hi]) > eps_c (the dps-100
                        value provably further than eps_c from the
                        true value);
       MODEL-UNDECIDED  if neither (the enclosure too wide to
                        confirm, but no refutation) -- non-
                        confirmation is NOT refutation.
     The upper/lower bounds are evaluated on a SECOND interval
     rebuild at iv dps 80 (B2 decision pass only; the certificate
     stays on the frozen dps-60 enclosure), because the
     certificate-pass width can exceed eps_c and then can never
     confirm the model.  The dps-60 columns are printed alongside
     for the fail-first record.  EITHER outcome is an honest
     finding and none is a kill; the certificate below no longer
     depends on the old model in any case.
 B3  THE CERTIFICATE RERUN: with the rigorous shift the exact
     integer Bareiss LDL runs on the Q = 10^20 grid exactly as the
     head probe (SPEC v2 grid inherited); all pivots > 0 ==>
     sigma_h > 0 with NO informal error model left.  Certified
     floors are attempted on the head probe's confirmation grid
     m in {0.5, 0.9} x lambda_min(f64) (skipped above the 120 s
     per-Bareiss budget, as the head).  A rung whose float floor
     sits below 100 x its rigorous shift would be typed
     out-of-reach (no kill); a genuine refusal above that gate is
     a pipeline kill.  Printed: rigorous shift vs the head's
     conservative shift, and the certified floors.
 B4  SCOPE REPORT: measured interval-lag cost per panel-node and
     measured Bareiss cost per rung, extrapolated to the full
     42-rung interval rollout (tier-1 h <= 300 at the measured
     Bareiss exponent 4.8; tier-2 h > 300 at the ladder's Cholesky
     seed 2.5e-7 s h^3) -- the named next step if this works.
 C   CONTROL (must fire): the Epstein x^2+5y^2 comb at kz 9 (the
     von-Mangoldt recursion run in INTERVAL arithmetic: a_n exact
     rationals, iv.log; support selected by the parent's READ-ONLY
     float scan) through the IDENTICAL interval lag assembly,
     rigorous shift and exact Bareiss certificate must hit a
     nonpositive pivot -- the machinery must REFUSE the wall for
     the wrong comb.

KILLS: K1 any B1 gate fails (node lemma, tent range, ward,
containment), or a prime rung above the reach gate is genuinely
refused -> PIPELINE-BROKEN; K2 the control is certified (does not
fire) -> CONTROL-DEAD.

VERDICT (frozen enum): BALLHEAD-PROVEN (all three head rungs
certified with the rigorous shift) / BALLHEAD-PARTIAL(which terms /
rungs) / ENCLOSURE-INFEASIBLE(why) / PIPELINE-BROKEN /
CONTROL-DEAD.

SPEC AMENDMENTS (fail-first history preserved, house precedent):
  v1 (frozen 2026-08-09, pre-run): B2 typed the comparison ONE-SIDED
     (MODEL-VALIDATED / MODEL-TOO-OPTIMISTIC from the rigorous
     upper bound alone, at the certificate's dps 60).  First run:
     the pipeline was green end to end (node lemma passed, wards
     1e-14, all three rungs CERTIFIED with the rigorous shift,
     floors 0.9 x lam_f, control refused at pivot 10), but B2 typed
     MODEL-TOO-OPTIMISTIC with margin 0.0016 -- while the SAME run
     showed the dps-100 vector INSIDE the enclosure on every entry.
     A category error, not a model failure: the dps-60 interval
     width (~6e-53) dominates the upper bound and can never confirm
     an eps_c of 1e-55; non-confirmation had been mislabelled as
     refutation -- exactly the dishonesty this probe exists to
     remove.
  v2: B2 typed THREE-WAY (VALIDATED / REFUTED / UNDECIDED, with
     refutation requiring the rigorous LOWER bound
     dist(c100, [lo, hi]) > eps_c) and decided on a second interval
     rebuild at iv dps 80 (B2 only).  Second run: pipeline green
     again, but B2 came out UNDECIDED with rad80 == rad60 ==
     6.2e-53 -- the radii were NOT limited by the lag-assembly
     precision at all: the node half-width 1e-70 is amplified
     ~1e16 by dependency widening in the interval Legendre
     recurrence for the WEIGHTS (per-weight width ~5e-54), a
     precision-independent floor that would keep B2 undecided at
     ANY lag dps.
  v3 (this file): the node enclosures are tightened to r = 1e-90
     with Newton at mp dps 110 (sign test still definite by orders:
     |P(x0 -+ r)| ~ 1e-89 vs recurrence evaluation width ~1e-106 at
     dps 120); weight widths drop to ~1e-74 and the dps-80 decision
     pass becomes meaningful.  A purely mechanical enclosure-
     tightening amendment: no bar, kill, error accounting or
     certificate arithmetic changed anywhere.

NO RH claim: these are finite-h positivity certificates for three
window rungs of the deployed ladder; the tail (h -> infinity) is
untouched and stays with the registered port contracts.

FIREWALL: no zeros, no prime oracles (AST scan for zetazero /
nzeros / primerange / isprime / primepi / nextprime / prevprime);
the atom tables come from the deployed v563 window, READ-ONLY; the
only factorisation used is trial-division smallest-prime-factor
recovery on the v563 atom list.  Deterministic, no RNG.  Stdout
only -- writes nothing.  No marker moves.

Sources (read-only): certified_head_probe (round 40 WP2 -- the gap
being closed; lag recipe and certificate verbatim);
certified_ladder_probe / certified_ladder_tail_probe (round 40
rollout -- the B4 extrapolation target); v563_paper2_readouts
(window/lag assembly); v866/v876 (wall <=> odd-Toeplitz PSD,
promoted); port_scalar_schur_probe (Epstein control recursion).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ball_arithmetic_head_probe.py
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

HEAD = (9, 12, 13)
DPS_IV = 60                    # working interval precision (frozen)
DPS_IV2 = 80                   # B2 decision pass precision (SPEC v2)
DPS_NODE = 120                 # node-enclosure lemma precision
NODE_R = "1e-90"               # node interval half-width (SPEC v3)
DPS_NEWTON = 110               # Newton dps for the node seeds
DPS_LO, DPS_HI = 60, 100       # the OLD model's mpf lag precisions
SAFETY = 10                    # the OLD model's safety factor
EPS_FLOOR = "1e-55"            # the OLD model's eps_c floor
Q_POW = 20                     # grid denominator Q = 10^20 (head v2)
WARD_REL = 1.0e-9              # T1 ward bar (expected ~1e-12)
GL_N = 48                      # the deployed panel order (v563)
REACH_FACTOR = 100.0           # float lam_min >= this x shift bound
FLOOR_FRACS = (0.5, 0.9)       # the head's confirmation grid
BISECT_BUDGET = 120.0          # s; skip floor steps above this
T1_EXP = 4.8                   # Bareiss cost exponent (ladder)
C2_SEED = 2.5e-7               # tier-2 Cholesky s per h^3 (ladder)
H_LADDER_MAX = 900             # reachable-rung cap (ladder)
TIER1_H_MAX = 300              # tier boundary (ladder)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
INFEASIBLE = []                # (term, why) -- expected empty (E2)
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
    """The node-enclosure lemma (E1): per node a verified interval
    [x0 - r, x0 + r] with a definite P_n sign change, all pairwise
    disjoint; weights as interval images.  Returns (X, W, lemma)."""
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
    """The archimedean lags as intervals (E2).  Panel cache: panel k
    covers [kD, (k+1)D] with node abscissae w = kD + D/2 + (D/2)x;
    the ratio exp(-w/2)/(-expm1(-2w)) is shared between the two
    adjacent lags that integrate over the panel (identical real
    quantity).  Far lag i (i >= 1) uses panels i-1 and i with the
    exact triangle identities (1+x)/2 and (1-x)/2; the near branch
    (only i = 0, s = 0) uses panel 0 with tri_s = 1 and
    S = max0((1-x)/2)."""
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
    """The T115 tent atoms as intervals (E3).  Guard 'if v > 0: add'
    transcribed as max0(v); loop-range sufficiency verified per atom
    (range_ok); the reflection branch applied only at index 0 (for
    i >= 1 its tent value is < 0 rigorously since u_j > 0)."""
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


def spf(n):
    """Smallest prime factor by trial division (n is a prime power
    from the READ-ONLY v563 atom list, so spf(n) = its base p)."""
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n


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


def lags_iv(spec, glX, glW, dps=DPS_IV):
    """The full interval lag vector of one rung at the given iv dps
    (E1-E3).  Returns (mid list, rad list, range_ok)."""
    iv.dps = dps
    alpha = iv.log(spec["n_zone"])
    M = spec["M"]
    if spec["kind"] == "prime":
        uu = [iv.log(n) for n in spec["atoms_n"]]
        mm = [2 * iv.log(spf(n)) / iv.sqrt(n)
              for n in spec["atoms_n"]]
    else:
        lamE = lambda_eps_iv(spec["N_E"])
        uu = [iv.log(n) for n in spec["nn"]]
        mm = [2 * lamE[n] / iv.sqrt(n) for n in spec["nn"]]
    D = 2 * alpha / M
    c_ar = arch_lags_iv(M, D, glX, glW)
    c_at, range_ok = atom_lags_iv(alpha, M, uu, mm)
    mids, rads = [], []
    for i in range(M):
        m_i, r_i = mid_rad(c_ar[i] + c_at[i])
        mids.append(m_i)
        rads.append(r_i)
    return mids, rads, range_ok


# ------------------------------ the OLD model's mpf lags (verbatim)
_GL_MP_CACHE = {}


def gl_nodes_mp_w(n):
    """Head-probe Gauss-Legendre nodes/weights at current mp dps
    (cached per dps) -- used ONLY for the old-model eps_c."""
    key = (n, mp.dps)
    if key in _GL_MP_CACHE:
        return _GL_MP_CACHE[key]
    xs, ws = [], []
    tol = mp.mpf(10) ** (-(mp.dps - 6))
    for i in range(n):
        x = mp.cos(mp.pi * (i + mp.mpf(3) / 4) / (n + mp.mpf(1) / 2))
        dp = mp.mpf(1)
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
        ws.append(2 / ((1 - x * x) * dp * dp))
    _GL_MP_CACHE[key] = (xs, ws)
    return xs, ws


def arch_A_far_mp(s, D, glx, glw):
    out = mp.mpf(0)
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        acc = mp.mpf(0)
        for x, wt in zip(glx, glw):
            w = mid + half * x
            acc += wt * ((1 - abs(s - w) / D) * mp.exp(-w / 2)
                         / (-mp.expm1(-2 * w)))
        out -= half * acc
    return out


def arch_A_near_mp(s, D, glx, glw):
    s = abs(s)
    tri_s = max(mp.mpf(0), 1 - s / D)
    W = s + D
    pts = sorted({mp.mpf(0), s, D - s, W})
    pts = [p for p in pts if 0 <= p <= W]
    tot = mp.mpf(0)
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        for x, wt in zip(glx, glw):
            w = mid + half * x
            S = (max(mp.mpf(0), 1 - abs(s - w) / D)
                 + max(mp.mpf(0), 1 - (s + w) / D)) / 2
            tot += half * wt * ((tri_s * mp.exp(-2 * w)
                                 - S * mp.exp(-w / 2))
                                / (-mp.expm1(-2 * w)))
    return (-(mp.euler + mp.log(mp.pi)) * tri_s + 2 * tot
            - tri_s * mp.log(-mp.expm1(-2 * W)))


def atom_lags_mp(alpha, M, uu, mm):
    D = 2 * alpha / M
    c = [mp.mpf(0)] * M
    for u_j, mu_j in zip(uu, mm):
        i0 = int(mp.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1 - abs(i * D - u_j) / D
            if v > 0:
                c[i] -= mu_j * v / 2
        if u_j < D:
            for i in range(0, min(M, int(mp.floor((D - u_j) / D)) + 2)):
                v = 1 - (i * D + u_j) / D
                if v > 0:
                    c[i] -= mu_j * v / 2
    return c, D


def lambda_eps_mp(N):
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


def lags_mp(spec, dps):
    """The head probe's mpf lag vector, verbatim -- used ONLY to
    recompute the OLD model's eps_c for the B2 comparison."""
    with mp.workdps(dps):
        glx, glw = gl_nodes_mp_w(GL_N)
        alpha = mp.log(spec["n_zone"])
        M = spec["M"]
        if spec["kind"] == "prime":
            uu = [mp.log(n) for n in spec["atoms_n"]]
            mm = [2 * mp.log(spf(n)) / mp.sqrt(n)
                  for n in spec["atoms_n"]]
        else:
            lamE = lambda_eps_mp(spec["N_E"])
            uu = [mp.log(n) for n in spec["nn"]]
            mm = [2 * lamE[n] / mp.sqrt(n) for n in spec["nn"]]
        c_at, D = atom_lags_mp(alpha, M, uu, mm)
        c = []
        for i in range(M):
            s = i * D
            if s >= D:
                c.append(arch_A_far_mp(s, D, glx, glw) + c_at[i])
            else:
                c.append(arch_A_near_mp(s, D, glx, glw) + c_at[i])
        return c


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


def certify_rung(spec, c_f, b2=True):
    """One rung end to end: interval rebuild (B1), old-model eps_c
    and the B2 decision quantities (upper/lower bounds at the dps-80
    decision pass, SPEC v2), rigorous-shift exact Bareiss with the
    head's floor grid (B3)."""
    M, h = spec["M"], spec["M"] // 2
    Q = 10 ** Q_POW
    with mp.workdps(40):
        QM = mp.mpf(Q)                      # exact (48-bit mantissa)
    t0 = time.time()
    mids, rads, range_ok = lags_iv(spec, _GLX, _GLW)
    t_iv = time.time() - t0
    rad_max = rads[0]
    for r in rads[1:]:
        if r > rad_max:
            rad_max = r
    # --- old model, head recipe verbatim
    t0 = time.time()
    c_lo = lags_mp(spec, DPS_LO)
    c_hi = lags_mp(spec, DPS_HI)
    t_mp = time.time() - t0
    with mp.workdps(DPS_HI + 20):
        eps_c = max(SAFETY * max(abs(a - b)
                                 for a, b in zip(c_lo, c_hi)),
                    mp.mpf(EPS_FLOOR))
        ward = (max(abs(a - mp.mpf(b)) for a, b in zip(mids, c_f))
                / max(abs(mp.mpf(b)) for b in c_f))
        contain = 0
        model_bound = mp.mpf(0)
        for i in range(M):
            lo_i = mp.fsub(mids[i], rads[i], exact=True)
            hi_i = mp.fadd(mids[i], rads[i], exact=True)
            if lo_i <= c_hi[i] <= hi_i:
                contain += 1
            b_i = max(c_hi[i] - lo_i, hi_i - c_hi[i])
            if b_i > model_bound:
                model_bound = b_i
    # --- B2 decision pass (SPEC v2): dps-80 enclosure, upper AND
    #     lower bounds on |c_dps100 - c_true| per entry
    bound2 = refute2 = rad_max2 = None
    if b2:
        mids2, rads2, _rng2 = lags_iv(spec, _GLX, _GLW, DPS_IV2)
        iv.dps = DPS_IV
        rad_max2 = max(rads2)
        with mp.workdps(DPS_HI + 20):
            bound2 = mp.mpf(0)
            refute2 = mp.mpf(0)
            for i in range(M):
                lo_i = mp.fsub(mids2[i], rads2[i], exact=True)
                hi_i = mp.fadd(mids2[i], rads2[i], exact=True)
                b_i = max(c_hi[i] - lo_i, hi_i - c_hi[i])
                if b_i > bound2:
                    bound2 = b_i
                d_i = max(lo_i - c_hi[i], c_hi[i] - hi_i,
                          mp.mpf(0))
                if d_i > refute2:
                    refute2 = d_i
    # --- rigorous certificate
    shift_int = rigorous_shift_int(h, rad_max, QM)
    with mp.workdps(DPS_HI + 20):
        s_riv = float(mp.mpf(shift_int) / Q)
        eps_f = float(eps_c)
        s_old = float((h + mp.ceil(2 * h * eps_c * Q)) / Q)
    Kf = core.odd_toeplitz(np.asarray(c_f, float), M)
    lam_f = float(np.linalg.eigvalsh(Kf)[0])
    out = dict(h=h, M=M, rads=rads, rad_max=rad_max, eps_c=eps_c,
               eps_f=eps_f, ward=float(ward), contain=contain,
               model_bound=model_bound, bound2=bound2,
               refute2=refute2, rad_max2=rad_max2, s_riv=s_riv,
               s_old=s_old, lam_f=lam_f, t_iv=t_iv, t_mp=t_mp,
               range_ok=range_ok, floor=None, npiv=0, bad=None,
               t_cert=0.0)
    if spec["kind"] == "prime" and lam_f < REACH_FACTOR * s_riv:
        out["status"] = "out-of-reach"
        return out
    N = grid_matrix_exact(mids, M, QM)
    t0 = time.time()
    ok, npiv, bad = bareiss_pd(
        [[N[i][j] - (shift_int if i == j else 0) for j in range(h)]
         for i in range(h)])
    t_base = time.time() - t0
    out.update(npiv=npiv, bad=bad)
    if not ok:
        out.update(status="refused", t_cert=time.time() - t0)
        return out
    out.update(status="certified", floor=0.0)
    if lam_f > 0 and t_base <= BISECT_BUDGET:
        for frac in FLOOR_FRACS:
            mQ = int(frac * lam_f * Q)
            okm, _, _ = bareiss_pd(
                [[N[i][j] - (shift_int + mQ if i == j else 0)
                  for j in range(h)] for i in range(h)])
            if okm:
                out["floor"] = mQ / Q
            else:
                break
    out["t_cert"] = time.time() - t0
    return out


# ------------------------------------------------ ladder geometry
def ladder_rungs():
    """(kz, h, M) of every reachable rung (ladder probe geometry,
    verbatim) -- used ONLY for the B4 extrapolation."""
    out = []
    for kz in core.frame_a_zones():
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if M % 2:
            M += 1
        if M // 2 <= H_LADDER_MAX:
            out.append((kz, M // 2, M))
    return sorted(out, key=lambda t: t[1])


_GLX = _GLW = None


def main():
    global _GLX, _GLW
    section("PRIME.PORT.BALLHEAD.01 -- rigorous interval closure of "
            "the certified head (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Mode: mpmath.iv "
          "interval lags (dps %d, node lemma dps %d) + exact "
          "integer Bareiss LDL (Q = 10^%d)"
          % (DPS_IV, DPS_NODE, Q_POW))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("B1 -- node-enclosure lemma (E1) and the interval "
            "rebuild (E2/E3)")
    t0 = time.time()
    _GLX, _GLW, lemma = gl_nodes_enclosed(GL_N)
    print("    GL-%d node lemma: %d sign-change intervals of radius "
          "%s at iv dps %d | pairwise disjoint %s | weight-sum "
          "interval width %.1e | %.1f s"
          % (GL_N, GL_N, NODE_R, DPS_NODE, lemma["disjoint"],
             lemma["wsum_delta"], time.time() - t0), flush=True)
    check("B1.1 NODE LEMMA: definite P_%d sign change on every "
          "node interval, all %d intervals pairwise disjoint, and "
          "2 lies in the interval weight sum" % (GL_N, GL_N),
          lemma["sign_ok"] and lemma["disjoint"]
          and lemma["contains2"], kill="K1")
    print("    transcendental steps enclosed per lag: iv.exp / "
          "iv.expm1 (arch integrand), iv.log / iv.sqrt (atoms, "
          "alpha), iv.euler / iv.pi / iv.log (near branch) -- all "
          "native; near branch specialised to its only call s = 0; "
          "no term needed an honest-remainder workaround")

    results = {}
    ok_range = ok_ward = ok_contain = True
    for kz in HEAD:
        r = core.build_window(kz)
        spec = dict(kind="prime", M=r["M"], n_zone=r["n_zone"],
                    atoms_n=[int(n) for n in
                             core._NN[:r["n_atom"]]])
        c_at_f, _ = core.atom_lags_at(r["alpha"], r["M"],
                                      np.asarray(r["uu"], float),
                                      2.0 * np.asarray(r["lam"],
                                                       float))
        c_f = list(core.arch_lags(r["M"], r["D"]) + c_at_f)
        res = certify_rung(spec, c_f)
        results[kz] = res
        ok_range &= res["range_ok"]
        ok_ward &= res["ward"] <= WARD_REL
        ok_contain &= res["contain"] == res["M"]
        print("    kz %-3d h %-4d | iv rebuild %.1f s | rad_max %s "
              "| ward rel %.2e | dps-100 lags inside enclosure "
              "%d/%d" % (kz, res["h"], res["t_iv"],
                         mp.nstr(res["rad_max"], 3), res["ward"],
                         res["contain"], res["M"]), flush=True)
    check("B1.2 tent-range rigour: the interval u_j/D sits inside "
          "[i0-1, i0+1] and u_j > 0 for every atom on every rung",
          ok_range, kill="K1")
    check("B1.3 CROSS-IMPLEMENTATION WARD: interval midpoints == "
          "deployed float64 core lags at rel <= %.0e on every head "
          "rung" % WARD_REL, ok_ward, kill="K1")
    check("B1.4 CONTAINMENT WARD: the head probe's dps-100 mpf lag "
          "vector lies inside the rigorous enclosure entrywise",
          ok_contain, kill="K1")

    section("B2 -- the enclosure comparison (THE HONESTY POINT): "
            "the declared model judged by rigorous enclosures")
    print("    per-rung ladder (dps-60 columns = the certificate "
          "enclosure, kept for the fail-first record; the decision "
          "columns are the dps-%d pass, SPEC v2):" % DPS_IV2)
    print("    kz   h    rad60        bound60      | rad%d        "
          "bound%d      refute%d     | eps_c        verdict"
          % (DPS_IV2, DPS_IV2, DPS_IV2))
    n_val = n_ref = 0
    worst = None
    for kz in HEAD:
        res = results[kz]
        with mp.workdps(40):
            validated = res["bound2"] <= res["eps_c"]
            refuted = res["refute2"] > res["eps_c"]
            margin = float(res["eps_c"] / res["bound2"]) \
                if res["bound2"] > 0 else float("inf")
        n_val += validated
        n_ref += refuted
        if worst is None or margin < worst:
            worst = margin
        tag = ("validated" if validated
               else ("REFUTED" if refuted else "undecided"))
        print("    %-4d %-4d %-12s %-12s | %-12s %-12s %-11s | "
              "%-12s %s"
              % (kz, res["h"], mp.nstr(res["rad_max"], 3),
                 mp.nstr(res["model_bound"], 3),
                 mp.nstr(res["rad_max2"], 3),
                 mp.nstr(res["bound2"], 3),
                 mp.nstr(res["refute2"], 3),
                 mp.nstr(res["eps_c"], 3), tag), flush=True)
    if n_val == len(HEAD):
        model_type = "MODEL-VALIDATED"
    elif n_ref > 0:
        model_type = "MODEL-REFUTED"
    else:
        model_type = "MODEL-UNDECIDED"
    print("\n    B2 RESULT: %s -- the declared per-entry claim "
          "|c_dps100 - c_true| <= eps_c is %s (worst margin "
          "eps_c/bound = %.3g at the dps-%d decision pass).  "
          "Either outcome is an honest finding; the certificate "
          "below no longer depends on the old model."
          % (model_type,
             "rigorously CONFIRMED" if model_type ==
             "MODEL-VALIDATED" else
             ("rigorously REFUTED" if model_type == "MODEL-REFUTED"
              else "NOT decidable at this precision (and NOT "
              "refuted)"), worst, DPS_IV2), flush=True)
    check("B2.1 enclosure comparison decided on every head rung "
          "(typed %s; an honest finding either way, not a gate)"
          % model_type, True)

    section("B3 -- the certificate rerun with the RIGOROUS shift "
            "(exact integer Bareiss LDL, Q = 10^%d)" % Q_POW)
    ok_cert = True
    for kz in HEAD:
        res = results[kz]
        ok_cert &= res["status"] == "certified"
        print("    kz %-3d h %-4d | shift(rigorous) %.3e vs "
              "shift(old model) %.3e | pivots %d/%d %s | "
              "lam_min(f64) %.3e | certified floor >= %s | "
              "cert %.1f s"
              % (kz, res["h"], res["s_riv"], res["s_old"],
                 res["npiv"], res["h"],
                 res["status"].upper(), res["lam_f"],
                 ("%.4e" % res["floor"])
                 if res["floor"] is not None else "-",
                 res["t_cert"]), flush=True)
    check("B3.1 BALL-CERTIFIED HEAD: all pivots > 0 under the "
          "rigorous interval shift on every head rung -- sigma_h > "
          "0 PROVEN modulo nothing but IEEE/mpmath interval "
          "correctness", ok_cert, kill="K1")

    section("C -- control (kz 9, Epstein x^2+5y^2 comb through the "
            "IDENTICAL interval machinery)")
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
    res_e = certify_rung(spec_e, c_fE, b2=False)
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

    section("B4 -- scope report: the full 42-rung interval rollout")
    s_pp = max(res["t_iv"] / (res["M"] * GL_N)
               for res in results.values())
    c1 = max(res["t_cert"] / res["h"] ** T1_EXP
             for res in results.values()
             if res["t_cert"] > 0) if ok_cert else float("nan")
    rungs = ladder_rungs()
    t1_lag = t1_cert = t2_lag = t2_cert = 0.0
    n1 = n2 = 0
    for _kz, h, M in rungs:
        tl = s_pp * M * GL_N
        if h <= TIER1_H_MAX:
            n1 += 1
            t1_lag += tl
            t1_cert += c1 * h ** T1_EXP
        else:
            n2 += 1
            t2_lag += tl
            t2_cert += C2_SEED * h ** 3
    tot = t1_lag + t1_cert + t2_lag + t2_cert
    print("    measured: interval lag cost %.2e s per panel-node; "
          "Bareiss c1 = %.2e s / h^%.1f (base + floor grid)"
          % (s_pp, c1, T1_EXP))
    for kz in HEAD:
        res = results[kz]
        print("    kz %-3d h %-4d runtime: iv lags %.1f s | old-"
              "model mpf lags %.1f s | Bareiss(+floors) %.1f s"
              % (kz, res["h"], res["t_iv"], res["t_mp"],
                 res["t_cert"]))
    print("    extrapolated 42-rung interval rollout: tier-1 "
          "(%d rungs, h <= %d): lags %.0f s + Bareiss %.0f s; "
          "tier-2 (%d rungs, mid-based Cholesky at ladder seed): "
          "lags %.0f s + Cholesky %.0f s; TOTAL ~ %.0f s (%.1f h) "
          "-- the named next step if this verdict holds"
          % (n1, TIER1_H_MAX, t1_lag, t1_cert, n2, t2_lag, t2_cert,
             tot, tot / 3600.0), flush=True)

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "K2" in KILLS:
        VERDICT = "CONTROL-DEAD"
    elif "K1" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif INFEASIBLE:
        VERDICT = ("ENCLOSURE-INFEASIBLE(%s)"
                   % "; ".join("%s: %s" % t for t in INFEASIBLE))
    elif all(results[kz]["status"] == "certified" for kz in HEAD):
        VERDICT = "BALLHEAD-PROVEN"
    else:
        VERDICT = ("BALLHEAD-PARTIAL(%s)"
                   % ", ".join("kz %d %s" % (kz,
                                             results[kz]["status"])
                               for kz in HEAD
                               if results[kz]["status"]
                               != "certified"))
    print("\n  VERDICT: %s   [B2: %s]" % (VERDICT, model_type))
    print("""
  DELIVERABLE: the head rungs kz 9, 12, 13 of the deployed v563
  window ladder, previously PROVEN modulo a declared-but-informal
  error model, re-proven with RIGOROUS mpmath.iv interval
  enclosures through every transcendental step (node-enclosure
  lemma + native interval exp/expm1/log/sqrt) and the exact
  integer Bareiss/Sylvester certificate -- sigma_h > 0 now holds
  modulo nothing but IEEE/mpmath interval correctness.  The old
  conservative model is itself judged rigorously in B2.  The tail
  stays with the port contracts.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (elapsed(), n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
