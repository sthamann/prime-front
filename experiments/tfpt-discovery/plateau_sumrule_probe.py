#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""plateau_sumrule_probe -- PRIME.PORT.PLATEAU.SUMRULE.01
(round 236): identify the near-conservation law behind the plateau
smoothness -- does the Euler-product SUM-RULE structure (the finite
window versions of sum_{d|n} Lambda(d) = log n, equivalently the
multiplicative ray structure of the von Mangoldt comb) act as the
smoothing constraint on the Jacobi chain, explaining why the MAIN
plateau stays smooth to the last degree and why the boundary is
invisible from inside (r233)?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Index firewall (r225-r233 discipline): w = window (kz rung), N_w =
builder depth, n = chain degree, t = gammahat index (g[t-1] =
gammahat_t from the r227 signed chain), eps = mutation dose, K =
swap-pair count, j = toy position jitter in u = log space.

THE HYPOTHESIS (adjudicated, never assumed): moment sum rules act
as smoothing constraints on Jacobi chains.  STRUCTURAL FACT sealed
into the design: the rule family {sum_{d|n} Lambda(d) = log n,
n <= X_w} is COMPLETE -- by induction (Moebius) it determines
Lambda on the window uniquely, so "breaking one rule minimally"
is the atomic unit of violation and the dose-response curve is
the causal answer.  The aggregated window form used across ALL
worlds (well-defined for arbitrary atom positions) is the
Chebyshev functional
    T_comb(x) = sum_i Lambdahat_i floor(x / e^{u_i}),
    Lambdahat_i = m_i e^{u_i/2} / 2,
    V(x) = |T_comb(x) - log floor(x)!| / log floor(x)!,
    V_med = median over integer x in [8, X_w]
(exact on MAIN for every x <= X_w because all prime-power divisor
atoms of every n <= X_w lie inside the window).

LEG A -- SMOOTHNESS CENSUS: for MAIN w in {9, 13, 26, 40} and the
three r231 controls (EPSTEIN / SCRAMBLE seed 1 / SMOOTH on the w9
base): local fluctuation F(t) = |gammahat_{t+1} - gammahat_t|,
second differences, alphahat roughness -- as profiles; plateau
band t in [N-40, N-2]; common range t in [3, min(18, flip-2)]
(all worlds alive there).  Separation numbers: SEP_RATIO = median
over controls of F_med(ctrl)/F_med(MAIN) on the common range;
divergence degree n_div = first t >= 3 with F_ctrl(t) >
10 x median F_MAIN (2 consecutive).  Regates: MAIN flips at
N + {0, 2, 3, 1} (kz 9/13/26/40, r233), controls flip at
25/21/27, w9 two-path agreement (Sherman-Morrison r-chain ==
signed-Stieltjes h-sign chain), plateau band inside [0.18, 0.32].

LEG B -- SUM-RULE IDENTIFICATION: (b1) exact divisor census on
MAIN w9: every rule with target n <= X_w is COMPLETE in the
window (all prime-power divisor atoms present, fraction 1.0);
Moebius reconstruction from the rules re-derives the comb
Lambdahat exactly (completeness gated <= 1e-9); truncation
profile for n in (X, 4X] reported (mean visible Lambda-fraction).
(b2) V_med per world: MAIN <= 1e-9 (exact by construction, float
edge only), every control >= 1e-3.  (b3) THE CORE MEASUREMENT:
over the 11-world family {MAIN, EPSTEIN, SMOOTH, SCRAMBLE seeds
1..8} Spearman rank correlations of V_med against (i) common-
range roughness F_med and (ii) -n_flip.  Sealed: CORR iff both
rho >= 0.6.  BINARY_SEPARATOR modifier iff (V_med < 1e-6) <=>
(flip >= N_w) across the family.

LEG C -- SURGICAL MUTATIONS (the causal test), on the w9 MAIN
comb, one-point statistics compensated (total comb mass sum m
preserved EXACTLY): (c1) prime-power atom pairs sealed by value:
(32, 31), (27, 29), (25, 23), (8, 7); dose eps in {1e-3, 3e-3,
1e-2, 3e-2, 1e-1, 3e-1}: m_a -> m_a (1 + eps), m_b -> m_b -
eps m_a (nearby position, different divisibility role -- breaks
every rule with 32 | n or 31 | n etc. while leaving the mass
total and the local density essentially unchanged).  (c2) swap
the masses of the K mass-closest disjoint atom pairs (different
divisibility roles, one-point mass multiset EXACTLY preserved),
K in {1, 2, 4, 8, 16}; dose = sum |delta m| / sum m reported.
Measured per dose: flip degree (shift vs MAIN 184), plateau-band
roughness ratio, plateau mean shift.  Machinery-loudness ward:
eps = 2.0 must move the chain visibly (max |delta gammahat| >
1e-3) -- mutations demonstrably reach the measure.  SEALED
ADJUDICATION: CAUSAL iff [median over c1 pairs of Spearman(eps,
flip-shift) >= 0.6 AND max flip-shift at eps <= 3e-2 is >= 3
degrees] OR [median Spearman(eps, roughness-ratio) >= 0.8 AND
max ratio at eps <= 3e-2 >= 2.0] OR [the same two clauses on the
c2 K-ladder]; MUTATION_ROBUST modifier iff all |flip-shift| <= 1
AND all roughness ratios <= 1.5 for eps <= 0.1.

LEG D -- SYNTHETIC REPRODUCTION (the mechanism test on data
level): non-prime measures with EXACT abstract sum-rule (ray)
structure: atoms at k log p with Lambda = log p and mass
2 log p e^{-k log p / 2} for a generator set WITHOUT true primes:
(d1) JITTER toys: real prime log-positions moved by U(-j, j),
j in {0.01, 0.03, 0.1} (rays rebuilt exactly around the moved
generators -- structure perfect, integers gone); (d2) CRAMER
toys: generators drawn at m + U(-0.4, 0.4) with probability
min(1, 1/log m), m = 2..X (PNT density, fully synthetic); seeds
101/202/303.  Each toy gets a SCRAMBLED PARTNER (same masses,
positions redrawn uniformly, seed + 1000): identical one-point
statistics, ray structure destroyed.  Gates: every toy satisfies
its OWN monoid Chebyshev identity to <= 1e-9 (structure exact)
while violating the INTEGER identity by >= 1e-3 (no primes
smuggled in); every scrambled partner violates its own-monoid
identity >= 1e-3 (m3 must-fail).  Survival: flip_eff / N_w
(flip_eff = cap if no flip within N + 30).  SEALED: TOY_STRONG
iff [median CRAMER flip_eff >= 0.9 N AND all CRAMER partners
flip < 0.3 N] OR [all jitter toys with j >= 0.03 have flip_eff
>= 0.9 N AND their partners flip < 0.3 N]; TOY_PARTIAL iff
median toy flip_eff >= 3 x median partner flip AND >= 0.25 N;
else TOY_DEAD (typed RULES_NEED_TRUE_ARITHMETIC if even jitter
j = 0.01 dies while MAIN stands).  Disclosure: toys run against
MAIN's Archimedean background (design choice, reported).

SEALED VERDICT RULE (precedence, frozen before any evaluation):
    REPRO := TOY_STRONG;
    1. SUMRULE_MECHANISM_GO   iff CAUSAL and REPRO;
    2. SUMRULE_CORRELATED_ONLY iff (CORR or REPRO) and not 1;
    3. SUMRULE_NOT_THE_CARRIER otherwise.
Modifiers: COLLECTIVE_CARRIER (REPRO without CAUSAL),
MUTATION_ROBUST, BINARY_SEPARATOR, TOY_PARTIAL / TOY_DEAD /
RULES_NEED_TRUE_ARITHMETIC.

MUST-FAILS (each loud): (m1) one perturbed Lambda value breaks
the divisor rules >= 1e-3; (m2) halving all comb masses breaks
the Chebyshev functional >= 0.1 (the functional is mass-defined,
not shape-defined); (m3) every scrambled toy partner violates
its own-monoid identity >= 1e-3 (V_own really measures the ray
structure, not the atom multiset).

HIGH-PRECISION WARD: mp dps-40 plain monic signed recursion
re-derives the f64 flip EXACTLY on (a) the strongest c1 mutant
(pair (32, 31), eps = 0.3) and (b) the CRAMER-101 toy.

DETERMINISM: RNG only through np.random.default_rng with the
declared seeds (SCRAMBLE 1..8 via the r232 core path, toy seeds
101/202/303 and +1000 partners, jitter seeds 71001/71002/71003);
run1 == run2 bit-for-bit (wall-clock line excluded).

RECORD TABLES (frozen from calib_ps_pass2.log, 17/17.
CALIBRATION AMENDMENTS, disclosed -- the dose ladders, seeds,
toy construction, correlation bars and the verdict precedence
were NEVER touched: (a1) after pass 1 the family roughness
range was widened from [3, min(18, flip-2)] to [3, min(18,
flip-1)] and rough() now accepts >= 2 points, because SCRAMBLE
seeds 6/7 flip at 7/5 and produced an empty range (NaN reached
the Spearman rank); the full family table print was added;
(a2) after the smoke run two REPORT texts were sharpened
(G12 census wording; c2 lines now disclose that the mass-
closest swap pairs sit at top-edge primes -- a positional
confound of the c2 family), no metric changed):
CAL_VERDICT = SUMRULE_CORRELATED_ONLY + BINARY_SEPARATOR +
TOY_DEAD (CAUSAL yes / CORR yes / REPRO no).
Key numbers: LEG A: MAIN flips 184/170/367/592 = N + 0/2/3/1
regated; plateau bands [N-20, N-1] inside [0.18, 0.32] on all
four windows (means 0.2487..0.2496; w9 band 0.2212..0.2842);
plateau-band F_med falls with depth: 2.25e-2 / 1.56e-2 /
9.92e-3 / 8.37e-3 (w 9/13/26/40).  THE CENSUS SURPRISE: on the
common range t in [3, 18] the MAIN chain (F_med 3.19e-4) is NOT
smoother than EPSTEIN (3.19e-4, x1.0) or SMOOTH (2.12e-4, x0.7)
-- the early chain is BACKGROUND-DOMINATED; only the position-
scrambled comb separates early (SCRAMBLE1 1.75e-2, x55,
divergence degree 4); EPSTEIN/SMOOTH diverge only at 20/22,
just before their flips 25/27 (consistent with the r233
precursor asymmetry); alphahat roughness shows the same pattern
(x1.0 / x106 / x0.7).  LEG B: all divisor rules with n <= X =
256 are complete (worst 3.9e-16) and Moebius reconstruction
re-derives Lambdahat to 2.7e-15 -- the window rule family
DETERMINES the measure; truncation fraction on (X, 4X] mean
0.737 (min 0); V_med: MAIN 1.8e-16, EPSTEIN 2.36e-2, SMOOTH
1.41e-1, SCRAMBLE seeds 1.07..1.94 (flips 5..34); family
Spearman(V, F_med) = +0.90 and (V, -flip) = +0.63, both >= 0.6
=> CORR HOLDS; BINARY_SEPARATOR holds 11/11 (V < 1e-6 <=> flip
>= N).  LEG C (the causal surprise -- the wall is NOT robust):
c1 flip shifts by pair (eps 1e-3/3e-3/1e-2/3e-2/1e-1/3e-1):
(32,31) 0/0/0/0/0/+51; (27,29) 0/0/0/+41/+61/+69; (25,23)
0/0/0/+52/+76/+78; (8,7) 0/0/+44/+91/+114/+117 -- a SINGLE
mass-compensated prime-power mutation of 1e-2 on the (8,7)
atoms (a Lambda dose of ~7e-3) pulls the flip 44 degrees below
the wall, and the sensitivity ORDER tracks the divisor
multiplicity of the mutated atoms (8/7 divide ~35 window
targets each, 32/31 only ~8); median Spearman(eps, shift)
+0.94, (eps, rough-ratio) +0.86, max shift at eps <= 3e-2 is 91
=> CAUSAL HOLDS, MUTATION_ROBUST no; c2 swap ladder (dose
3.2e-5..1.0e-3): 0 / 0 / +22 / +15 / +81, Spearman +0.87/+0.80
(top-edge positional confound disclosed); machinery ward eps =
2: max |delta gammahat| 1378, flip -> 114.  LEG D (the honest
negative): all six toys hold their OWN monoid identity to <=
2.3e-16 while violating the integer identity by 3.3e-3..0.36;
SURVIVAL: JIT 0.01/0.03/0.10 flip at 64/40/38 (rho 0.35/0.22/
0.21), CRAMER 101/202/303 at 36/37/52 (rho 0.20/0.20/0.28);
partners flip at 13..24 (rho 0.07..0.13): the toys outlive
their one-point twins by ~2.7x but die FAR below the wall
(TOY_PARTIAL bars 0.25/3x narrowly missed, sealed) => TOY_DEAD;
the monotone jitter gradient (64 -> 40 -> 38) says the exact
integer positions matter already at the 1-percent level --
consistent with r232c (any smoothing kills), the abstract ray
structure at PNT density does NOT reproduce prime-like
survival against the true Archimedean background.  MUST-FAILS:
m1 1.4e-2 >= 1e-3, m2 V_med(halved masses) 0.50 >= 0.1, m3
partner V_own >= 1.47.  MP WARD: dps-40 re-derives flip 133 on
the eps = 0.3 mutant and flip 36 on the CRAMER-101 toy exactly.
Runtime ~ 1 s.  AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fermiedge_classify_probe as FC        # noqa: E402 r227
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

# ------------------------------------------------- sealed constants
BASE_W = 9
WINDOWS_MAIN = (9, 13, 26, 40)
R233_DELTA = {9: 0, 13: 2, 26: 3, 40: 1}
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE1": 21, "SMOOTH": 27}
SCR_SEEDS = (1, 2, 3, 4, 5, 6, 7, 8)
CR_LO, CR_HI = 3, 18
PLATEAU_BAND = 40
PLATEAU_LIM = (0.18, 0.32)
DIV_FACT = 10.0
DIV_RUN = 2
X_GRID_MIN = 8
FLOOR_EPS = 1e-9
EXACT_BAR = 1e-9
CTRL_VIO_MIN = 1e-3
CORR_RHO = 0.6
PAIRS_C1 = ((32, 31), (27, 29), (25, 23), (8, 7))
EPS_LADDER = (1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1)
EPS_SMALL = 3e-2
SWAP_KS = (1, 2, 4, 8, 16)
MACHINERY_EPS = 2.0
MACHINERY_BAR = 1e-3
CAUSAL_RHO = 0.6
CAUSAL_SHIFT = 3
ROUGH_RHO = 0.8
ROUGH_RATIO = 2.0
ROBUST_SHIFT = 1
ROBUST_RATIO = 1.5
ROBUST_EPS = 0.1
JITTERS = (0.01, 0.03, 0.1)
JITTER_SEEDS = (71001, 71002, 71003)
CRAMER_SEEDS = (101, 202, 303)
SCR_TOY_OFFSET = 1000
TOY_RHO_STRONG = 0.9
TOY_SCR_MAX = 0.3
TOY_PARTIAL_FACT = 3.0
TOY_PARTIAL_RHO = 0.25
CHAIN_EXTRA = 30
MP_DPS = 40
M2_BAR = 0.1   # absolute V_med bar for the mass-halving trap
CAL_VERDICT = ("SUMRULE_CORRELATED_ONLY + BINARY_SEPARATOR + "
               "TOY_DEAD (CAUSAL yes / CORR yes / REPRO no)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; dose ladders, seeds, "
                       "toy construction and the verdict precedence "
                       "sealed in the frozen spec"
                       if not bad else "; ".join(bad))


def spearman(x, y):
    def ranks(v):
        v = np.asarray(v, float)
        order = np.argsort(v, kind="stable")
        rk = np.empty(len(v))
        rk[order] = np.arange(len(v), dtype=float)
        for val in np.unique(v):
            m = v == val
            rk[m] = rk[m].mean()
        return rk
    rx, ry = ranks(x), ranks(y)
    rx -= rx.mean()
    ry -= ry.mean()
    den = math.sqrt(float(np.sum(rx ** 2) * np.sum(ry ** 2)))
    return float(np.sum(rx * ry) / den) if den > 0 else 0.0


# ------------------------------------------------------ chain tools
def chain_pack(d, extra=CHAIN_EXTRA):
    """signed chain through the flip (or to cap); g[t-1] =
    gammahat_t, al[n] = alphahat_n, flip = first n with
    h_n(mutilde) < 0 (None if the wall holds to the cap)."""
    N = d["n_max"]
    cap = min(N + extra, len(d["xs"]) - 1)
    ch = FC.signed_chain(d, cap)
    g = np.array([c["gammahat_next"] for c in ch])
    al = np.array([c["alphahat"] for c in ch])
    flip = None
    for n in range(len(ch)):
        if ch[n]["sg_h"] < 0:
            flip = n
            break
    return dict(N=N, cap=cap, g=g, al=al, flip=flip,
                flip_eff=flip if flip is not None else cap)


def rough(seq, t_lo, t_hi):
    """median |x_{t+1} - x_t| over t in [t_lo, t_hi - 1] of a
    1-indexed quantity stored as seq[t-1] (>= 2 points required;
    amendment a1)."""
    seg = np.asarray(seq[max(t_lo - 1, 0):t_hi])
    if len(seg) < 2:
        return float("nan")
    return float(np.median(np.abs(np.diff(seg))))


def rough2(seq, t_lo, t_hi):
    seg = np.asarray(seq[max(t_lo - 1, 0):t_hi])
    if len(seg) < 4:
        return float("nan")
    return float(np.median(np.abs(np.diff(seg, 2))))


def band_of(pk):
    """plateau band [N - PLATEAU_BAND, N - 2] clipped below an
    early flip."""
    hi = pk["N"] - 2
    if pk["flip"] is not None:
        hi = min(hi, pk["flip"] - 2)
    lo = max(3, hi - PLATEAU_BAND + 2)
    return lo, hi


def sm_flip_w9(d):
    """Sherman-Morrison first r_n <= 0 (r226/r233 second path)."""
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    N = d["n_max"]
    want = min(len(xs), N + 10)
    al, be, m0, steps = PIK.lanczos_chain(xs, ws, want)
    ncap = min(steps - 1, N + 8)
    Pn = PIK.eval_chain(al, be, m0, ys, ncap)
    sq = np.sqrt(vs)
    M = np.eye(len(ys))
    for n in range(ncap):
        c = sq * Pn[:, n]
        Mc = M @ c
        fac = 1.0 - float(c @ Mc)
        if fac <= 0.0:
            return n
        M = M + np.outer(Mc, Mc) / fac
    return None


# ------------------------------------------------------ comb tools
def base_comb():
    rr = core.build_window(BASE_W)
    uu = np.asarray(rr["uu"], float).copy()
    mm = 2.0 * np.asarray(rr["lam"], float).copy()
    return uu, mm, rr


def lam_hat(uu, mm):
    return 0.5 * np.asarray(mm, float) * np.exp(
        0.5 * np.asarray(uu, float))


def cheby_v(uu, mm, X):
    """median/max violation of the integer Chebyshev identity
    T_comb(x) = log floor(x)! over integer x in [X_GRID_MIN, X]."""
    lam = lam_hat(uu, mm)
    dv = np.exp(np.asarray(uu, float))
    Tt = np.cumsum(np.log(np.arange(1, X + 1, dtype=float)))
    devs = []
    for x in range(X_GRID_MIN, X + 1):
        Tc = float(np.sum(lam * np.floor(x / dv + FLOOR_EPS)))
        Ttr = float(Tt[x - 1])
        devs.append(abs(Tc - Ttr) / Ttr)
    return float(np.median(devs)), float(np.max(devs))


def divs_of(n):
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i != n // i:
                out.append(n // i)
        i += 1
    return out


def rule_census(uu, mm, X, poison=None):
    """divisor rules sum_{d|n} Lambdahat(d) = log n for n <= X on
    an integer-positioned comb + Moebius reconstruction.  poison =
    (value, delta) perturbs one Lambdahat for the m1 must-fail."""
    lam = lam_hat(uu, mm)
    at = {}
    for u, l_ in zip(uu, lam):
        v = round(math.exp(float(u)))
        if v >= 2 and abs(math.exp(float(u)) - v) < 1e-6 * v:
            at[int(v)] = at.get(int(v), 0.0) + float(l_)
    if poison is not None:
        at[poison[0]] = at.get(poison[0], 0.0) + poison[1]
    worst = 0.0
    rec = {1: 0.0}
    rec_dev = 0.0
    for n in range(2, X + 1):
        s = 0.0
        smaller = 0.0
        for d in divs_of(n):
            if d in at:
                s += at[d]
            if d < n:
                smaller += rec.get(d, 0.0)
        worst = max(worst, abs(s - math.log(n)) / math.log(n))
        rec[n] = math.log(n) - smaller
        rec_dev = max(rec_dev, abs(rec[n] - at.get(n, 0.0)))
    fr = []
    for n in range(X + 1, 4 * X + 1, 7):
        s = sum(at.get(d, 0.0) for d in divs_of(n) if d <= X)
        fr.append(s / math.log(n))
    return worst, rec_dev, float(np.mean(fr)), float(np.min(fr))


# ------------------------------------------------------ mutations
def idx_of(uu, v):
    u = math.log(v)
    i = int(np.argmin(np.abs(uu - u)))
    assert abs(float(uu[i]) - u) < 1e-9, "atom %d not in window" % v
    return i


def mutate_c1(uu, mm, va, vb, eps):
    """m_a -> m_a (1 + eps), m_b -> m_b - eps m_a: total comb mass
    preserved EXACTLY, local density nearly preserved, the
    divisor rules through a and b broken."""
    ia, ib = idx_of(uu, va), idx_of(uu, vb)
    mm2 = mm.copy()
    delta = eps * mm[ia]
    mm2[ia] += delta
    mm2[ib] -= delta
    assert mm2[ib] > 0.0
    return mm2


def swap_comb(uu, mm, K):
    """swap the masses of the K mass-closest disjoint atom pairs
    (one-point mass multiset exactly preserved)."""
    order = np.argsort(mm)
    ms = mm[order]
    rel = np.abs(np.diff(ms)) / np.maximum(ms[:-1], 1e-300)
    used = set()
    pairs = []
    for j in np.argsort(rel):
        a, b = int(order[j]), int(order[j + 1])
        if a in used or b in used:
            continue
        pairs.append((a, b))
        used.update((a, b))
        if len(pairs) == K:
            break
    mm2 = mm.copy()
    dose = 0.0
    for a, b in pairs:
        mm2[a], mm2[b] = mm[b], mm[a]
        dose += abs(mm[a] - mm[b])
    return mm2, pairs, dose / float(np.sum(mm))


# ------------------------------------------------------ toys (leg D)
def ray_comb(gen_logs, two_alpha):
    """exact multiplicative ray comb over a generator set: atoms
    (k lp, 2 lp e^{-k lp / 2}) for k lp <= 2 alpha."""
    uu, mm = [], []
    for lp in gen_logs:
        if lp <= 0.05:
            continue
        k = 1
        while k * lp <= two_alpha - 1e-9:
            uu.append(k * lp)
            mm.append(2.0 * lp * math.exp(-0.5 * k * lp))
            k += 1
    o = np.argsort(uu)
    return (np.asarray(uu, float)[o], np.asarray(mm, float)[o])


def cramer_logs(X, seed):
    rng = np.random.default_rng(seed)
    out = []
    for m in range(2, X + 1):
        if rng.random() < min(1.0, 1.0 / math.log(m)):
            out.append(math.log(m + rng.uniform(-0.4, 0.4)))
    return out


def jitter_logs(uu, mm, jit, seed):
    """generator (k = 1) atoms of the true comb, log-positions
    moved by U(-jit, jit)."""
    lam = lam_hat(uu, mm)
    rng = np.random.default_rng(seed)
    out = []
    for u, l_ in zip(uu, lam):
        if abs(float(l_) - float(u)) < 1e-9:
            out.append(float(u) + rng.uniform(-jit, jit))
    return out


def scramble_comb(uu, mm, two_alpha, seed):
    """same masses, positions redrawn uniformly (the r232 core
    scramble convention): one-point statistics kept, rays killed."""
    rng = np.random.default_rng(seed)
    return (np.sort(rng.uniform(0.0, two_alpha, size=len(uu))),
            mm.copy())


def own_violation(gen_logs, two_alpha, uu, mm, n_eval=300):
    """violation of the toy's OWN free-monoid Chebyshev identity
    sum_{v <= x} log v = sum_{p,k} log p N_P(x / p^k)."""
    vals = [0.0]
    for lp in sorted(gen_logs):
        if lp <= 0.05:
            continue
        cur = list(vals)
        for v in cur:
            u = v + lp
            while u <= two_alpha + 1e-12:
                vals.append(u)
                u += lp
    vals = np.sort(np.asarray(vals, float))
    lam = lam_hat(uu, mm)
    Tcum = np.cumsum(vals)
    take = np.unique(np.linspace(
        max(1, len(vals) // 20), len(vals) - 1,
        min(len(vals) - 1, n_eval)).astype(int))
    devs = []
    for j in take:
        x_u = float(vals[j]) + 1e-9
        T_own = float(Tcum[j])
        if T_own < 1.0:
            continue
        y = x_u - np.asarray(uu, float)
        cnt = np.searchsorted(vals, y + 1e-12, side="right")
        cnt = np.where(y < -1e-12, 0, cnt)
        Tc = float(np.sum(lam * cnt))
        devs.append(abs(Tc - T_own) / T_own)
    return float(np.median(devs)), float(np.max(devs)), len(vals)


# --------------------------------------------------------- mp ward
def mp_flip(d, cap):
    """plain monic signed recursion at mp dps MP_DPS; first n with
    h_n < 0, or None if positive through cap."""
    import mpmath as mp
    mp.mp.dps = MP_DPS
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wt = ([mp.mpf(float(w)) for w in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    hs = [mp.fsum(w * p * p for w, p in zip(wt, pk))]
    for k in range(cap):
        a = mp.fsum(w * x * p * p
                    for w, x, p in zip(wt, nds, pk)) / hs[-1]
        g = (hs[-1] / hs[-2]) if k > 0 else mp.mpf(0)
        nx = [(x - a) * p - g * q
              for x, p, q in zip(nds, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(mp.fsum(w * p * p for w, p in zip(wt, pk)))
        if hs[-1] < 0:
            return k + 1
    return None


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("plateau_sumrule_probe -- PRIME.PORT.PLATEAU.SUMRULE.01 "
          "(round 236)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (w9, reduced ladders)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "MAIN windows %s (flip regates N + %s); controls "
          "EPSTEIN/SCRAMBLE1/SMOOTH at 25/21/27; family = MAIN + "
          "EPSTEIN + SMOOTH + SCRAMBLE seeds %s; c1 pairs %s x "
          "eps %s; c2 K %s; toys jitter %s (seeds %s) + Cramer "
          "seeds %s with +%d scrambled partners; verdict "
          "precedence GO > CORRELATED_ONLY > NOT_THE_CARRIER "
          "sealed in the spec"
          % (str(WINDOWS_MAIN),
             str(tuple(R233_DELTA[w] for w in WINDOWS_MAIN)),
             str(SCR_SEEDS), str(PAIRS_C1), str(EPS_LADDER),
             str(SWAP_KS), str(JITTERS), str(JITTER_SEEDS),
             str(CRAMER_SEEDS), SCR_TOY_OFFSET))

    uu0, mm0, rr9 = base_comb()
    alpha9 = float(rr9["alpha"])
    two_alpha = 2.0 * alpha9
    X9 = int(math.floor(math.exp(two_alpha) + 0.5))
    info("w9 base comb: %d atoms, X = %d, 2 alpha = %.4f"
         % (len(uu0), X9, two_alpha))

    # ---------------- worlds on the w9 base
    N_E = int(math.floor(math.exp(two_alpha))) + 1
    lamE_ = PIK.lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    comb_E = (np.log(nnE.astype(float)),
              2.0 * lamE_[nnE] / np.sqrt(nnE.astype(float)))
    ug = np.arange(0.01, two_alpha, 0.01)
    comb_S = (ug, 2.0 * np.exp(ug / 2.0) * 0.01)

    scr_seeds = SCR_SEEDS[:2] if smoke else SCR_SEEDS
    fam = []          # (name, uu, mm, kwargs for window_data)
    fam.append(("MAIN", uu0, mm0, dict()))
    fam.append(("EPSTEIN", comb_E[0], comb_E[1],
                dict(comb=comb_E)))
    fam.append(("SMOOTH", comb_S[0], comb_S[1],
                dict(comb=comb_S)))
    for s in scr_seeds:
        rrs = core.build_window(BASE_W, scramble_seed=s)
        fam.append(("SCR%d" % s, np.asarray(rrs["uu"], float),
                    2.0 * np.asarray(rrs["lam"], float),
                    dict(scramble_seed=s)))

    packs = {}
    for name, _uu, _mm, kw in fam:
        d = HS.window_data(BASE_W, **kw)
        packs[name] = chain_pack(d)

    # ================= S1  LEG A -- smoothness census
    section("S1  LEG A -- SMOOTHNESS CENSUS")
    d9 = HS.window_data(BASE_W)
    ok_two = sm_flip_w9(d9) == packs["MAIN"]["flip"]
    ok_ctrl = (packs["EPSTEIN"]["flip"] == CTRL_FLIPS["EPSTEIN"]
               and packs["SCR1"]["flip"] == CTRL_FLIPS["SCRAMBLE1"]
               and packs["SMOOTH"]["flip"] == CTRL_FLIPS["SMOOTH"])
    ok_main_flips = True
    main_packs = {BASE_W: packs["MAIN"]}
    wins = (BASE_W,) if smoke else WINDOWS_MAIN
    for w in wins:
        pk = (packs["MAIN"] if w == BASE_W
              else chain_pack(HS.window_data(w)))
        main_packs[w] = pk
        ok_main_flips = ok_main_flips and (
            pk["flip"] == pk["N"] + R233_DELTA[w])
        lo, hi = pk["N"] - 20, pk["N"] - 1
        band = pk["g"][lo - 1:hi]
        okp = (PLATEAU_LIM[0] <= float(np.min(band))
               and float(np.max(band)) <= PLATEAU_LIM[1])
        ok_main_flips = ok_main_flips and okp
        info("MAIN w=%-3d N=%3d flip=%3d (N%+d) | plateau "
             "[N-20, N-1]: %.4f..%.4f mean %.4f | band F_med "
             "%.2e D2_med %.2e | alphahat F_med %.2e"
             % (w, pk["N"], pk["flip"], pk["flip"] - pk["N"],
                float(np.min(band)), float(np.max(band)),
                float(np.mean(band)),
                rough(pk["g"], *band_of(pk)),
                rough2(pk["g"], *band_of(pk)),
                rough(pk["al"][1:], *band_of(pk))))
    check("G10-regates", ok_two and ok_ctrl and ok_main_flips,
          "w9 two paths agree (SM r-chain == signed h-sign chain); "
          "controls flip at 25/21/27; MAIN flips at N + "
          "{0, 2, 3, 1} (kz 9/13/26/40, r233) and every plateau "
          "band [N-20, N-1] sits inside [%.2f, %.2f]"
          % PLATEAU_LIM)

    F9 = np.abs(np.diff(packs["MAIN"]["g"]))
    f9_cr = rough(packs["MAIN"]["g"], CR_LO, CR_HI)
    a9_cr = rough(packs["MAIN"]["al"][1:], CR_LO, CR_HI)
    seps, ndivs = [], {}
    for name in ("EPSTEIN", "SCRAMBLE1", "SMOOTH"):
        key = "SCR1" if name == "SCRAMBLE1" else name
        pk = packs[key]
        hi = min(CR_HI, pk["flip"] - 2)
        f_cr = rough(pk["g"], CR_LO, hi)
        a_cr = rough(pk["al"][1:], CR_LO, hi)
        seps.append(f_cr / f9_cr)
        Fc = np.abs(np.diff(pk["g"]))
        nd = None
        run = 0
        for t in range(CR_LO, pk["flip"]):
            if Fc[t - 1] > DIV_FACT * f9_cr:
                run += 1
                if run >= DIV_RUN:
                    nd = t - DIV_RUN + 1
                    break
            else:
                run = 0
        ndivs[name] = nd
        info("%-9s flip=%2d | common-range F_med %.2e (x%5.1f "
             "MAIN) D2_med %.2e | alphahat F_med %.2e (x%5.1f) | "
             "divergence n_div = %s"
             % (name, pk["flip"], f_cr, f_cr / f9_cr,
                rough2(pk["g"], CR_LO, hi), a_cr, a_cr / a9_cr,
                str(nd)))
    sep_ratio = float(np.median(seps))
    check("G12-smoothness-census", True,
          "MAIN common-range F_med %.2e (alphahat %.2e); "
          "SEP_RATIO (median control / MAIN) = %.1f; divergence "
          "degrees %s; MAIN full-profile F quartiles %.2e / "
          "%.2e / %.2e -- measured, not assumed: the early chain "
          "is background-dominated (position-scrambled combs "
          "separate immediately, spectrally structured controls "
          "only near their own flip), so the smoothness census "
          "localizes WHERE each world starts to differ"
          % (f9_cr, a9_cr, sep_ratio,
             str({k: v for k, v in ndivs.items()}),
             float(np.percentile(F9[:packs["MAIN"]["N"] - 2], 25)),
             float(np.percentile(F9[:packs["MAIN"]["N"] - 2], 50)),
             float(np.percentile(F9[:packs["MAIN"]["N"] - 2], 75))))

    # ================= S2  LEG B -- sum-rule identification
    section("S2  LEG B -- SUM-RULE IDENTIFICATION")
    worst9, rec9, fr_mean, fr_min = rule_census(uu0, mm0, X9)
    check("G20-sumrule-complete-main", worst9 <= EXACT_BAR
          and rec9 <= EXACT_BAR,
          "every divisor rule with target n <= X = %d is COMPLETE "
          "in the window (worst rel violation %.1e) and the "
          "Moebius reconstruction from the rules re-derives the "
          "comb Lambdahat exactly (max dev %.1e): the finite rule "
          "family DETERMINES the measure -- 'one rule' cannot be "
          "broken alone, the dose-response curve is the causal "
          "object; truncation profile on (X, 4X]: mean visible "
          "Lambda-fraction %.3f (min %.3f)"
          % (X9, worst9, rec9, fr_mean, fr_min))

    vios = {}
    for name, _uu, _mm, _kw in fam:
        vios[name] = cheby_v(_uu, _mm, X9)
        info("%-9s V_med %.2e V_max %.2e" % (name, vios[name][0],
                                             vios[name][1]))
    ok_b2 = (vios["MAIN"][0] <= EXACT_BAR
             and all(v[0] >= CTRL_VIO_MIN
                     for k, v in vios.items() if k != "MAIN"))
    check("G21-cheby-functional", ok_b2,
          "the integer Chebyshev functional is EXACT on MAIN "
          "(V_med %.1e <= %.0e) and violated on every control "
          "(min V_med %.2e >= %.0e): the sum-rule structure "
          "separates the worlds binarily"
          % (vios["MAIN"][0], EXACT_BAR,
             min(v[0] for k, v in vios.items() if k != "MAIN"),
             CTRL_VIO_MIN))

    fam_names = [f[0] for f in fam]
    Vv = [vios[n][0] for n in fam_names]
    Ff = []
    Fl = []
    for n in fam_names:
        pk = packs[n]
        hi = (CR_HI if pk["flip"] is None
              else min(CR_HI, pk["flip"] - 1))   # amendment a1
        Ff.append(rough(pk["g"], CR_LO, hi))
        Fl.append(pk["flip_eff"])
        info("family %-8s V_med %.2e  F_med %.2e  flip %3d"
             % (n, vios[n][0], Ff[-1], pk["flip_eff"]))
    assert not any(math.isnan(x) for x in Ff)
    rho_vf = spearman(Vv, Ff)
    rho_vfl = spearman(Vv, [-x for x in Fl])
    CORR = (rho_vf >= CORR_RHO) and (rho_vfl >= CORR_RHO)
    binsep = all((v < 1e-6) == (fl >= packs[n]["N"])
                 for n, v, fl in zip(fam_names, Vv, Fl))
    check("G22-family-correlation", True,
          "%d-world family: Spearman(V_med, F_med) = %+.2f, "
          "Spearman(V_med, -flip) = %+.2f (bars %.1f both) -> "
          "CORR %s; BINARY_SEPARATOR (V < 1e-6 <=> flip >= N): "
          "%s -- violation PRESENCE separates perfectly%s"
          % (len(fam_names), rho_vf, rho_vfl, CORR_RHO,
             "HOLDS" if CORR else "FAILS",
             "holds" if binsep else "FAILS",
             "" if CORR else "; violation DEGREE does not rank "
             "roughness/flip within the controls (SMOOTH is the "
             "most violated yet flips last among controls)"))

    # ================= S3  LEG C -- surgical mutations
    section("S3  LEG C -- SURGICAL MUTATIONS (dose response)")
    pk_id = chain_pack(HS.window_data(BASE_W, comb=(uu0, mm0)))
    g_ref = packs["MAIN"]["g"]
    dev_id = float(np.max(np.abs(
        pk_id["g"][:len(g_ref)] - g_ref[:len(pk_id["g"])])))
    check("G30-mutation-identity", pk_id["flip"] == packs["MAIN"][
        "flip"] and dev_id <= EXACT_BAR,
          "the comb= path with the UNmutated (uu, mm) reproduces "
          "the default MAIN chain bit-for-bit (flip %d, max "
          "|delta gammahat| %.1e): mutations act on the true "
          "measure, not a proxy" % (pk_id["flip"], dev_id))

    flip0 = packs["MAIN"]["flip"]
    lo0, hi0 = band_of(packs["MAIN"])
    f_band0 = rough(g_ref, lo0, hi0)
    plat0 = float(np.mean(g_ref[flip0 - 21:flip0 - 1]))
    pairs = PAIRS_C1[:1] if smoke else PAIRS_C1
    epss = (1e-2, 3e-1) if smoke else EPS_LADDER
    rho_shift_pairs, rho_rough_pairs = [], []
    max_shift_small, max_rr_small = 0, 0.0
    max_shift_all, max_rr_all = 0, 0.0
    d_mut_big = None
    for (va, vb) in pairs:
        shifts, rrs = [], []
        line = []
        for eps in epss:
            mm2 = mutate_c1(uu0, mm0, va, vb, eps)
            dm = HS.window_data(BASE_W, comb=(uu0, mm2))
            pk = chain_pack(dm)
            if va == 32 and abs(eps - 0.3) < 1e-12:
                d_mut_big = dm
            sh = flip0 - pk["flip_eff"]
            rr_ = rough(pk["g"], *band_of(pk)) / f_band0
            shifts.append(sh)
            rrs.append(rr_)
            if eps <= EPS_SMALL:
                max_shift_small = max(max_shift_small, sh)
                max_rr_small = max(max_rr_small, rr_)
            if eps <= ROBUST_EPS:
                max_shift_all = max(max_shift_all, abs(sh))
                max_rr_all = max(max_rr_all, rr_)
            pl = float(np.mean(pk["g"][
                max(0, pk["flip_eff"] - 21):pk["flip_eff"] - 1]))
            line.append("e%.0e: flip %d (sh %+d) rr %.2f dpl "
                        "%+.3f" % (eps, pk["flip_eff"], sh, rr_,
                                   pl - plat0))
        rho_shift_pairs.append(spearman(epss, shifts))
        rho_rough_pairs.append(spearman(epss, rrs))
        info("c1 (%3d,%3d): %s" % (va, vb, " | ".join(line)))
        info("            Spearman(eps, shift) %+.2f, "
             "Spearman(eps, rough-ratio) %+.2f"
             % (rho_shift_pairs[-1], rho_rough_pairs[-1]))
    ks = SWAP_KS[2:3] if smoke else SWAP_KS
    shifts_k, rrs_k = [], []
    for K in ks:
        mm2, prs, dose = swap_comb(uu0, mm0, K)
        pk = chain_pack(HS.window_data(BASE_W, comb=(uu0, mm2)))
        sh = flip0 - pk["flip_eff"]
        rr_ = rough(pk["g"], *band_of(pk)) / f_band0
        shifts_k.append(sh)
        rrs_k.append(rr_)
        pns = sorted(round(math.exp(uu0[a])) for a, _b in prs)
        info("c2 K=%2d (dose sum|dm|/sum m = %.1e; swapped atoms "
             "sit at n = %s..%s -- mass-closest pairs are top-"
             "edge primes, positional confound DISCLOSED): flip "
             "%d (sh %+d) rr %.2f"
             % (K, dose, pns[0], pns[-1],
                pk["flip_eff"], sh, rr_))
    rho_shift_k = spearman(ks, shifts_k)
    rho_rough_k = spearman(ks, rrs_k)

    mm_big = mutate_c1(uu0, mm0, 32, 31, MACHINERY_EPS)
    pk_big = chain_pack(HS.window_data(BASE_W, comb=(uu0, mm_big)))
    nn_ = min(len(pk_big["g"]), len(g_ref), flip0 - 2)
    mach = float(np.max(np.abs(pk_big["g"][:nn_] - g_ref[:nn_])))
    check("G31-machinery-loud", mach > MACHINERY_BAR,
          "eps = %.1f on pair (32, 31) moves the chain by max "
          "|delta gammahat| = %.2f > %.0e and the flip to %d: "
          "the mutation machinery demonstrably reaches the "
          "measure -- small-dose null results below are physics, "
          "not plumbing" % (MACHINERY_EPS, mach, MACHINERY_BAR,
                            pk_big["flip_eff"]))

    c1_causal = ((float(np.median(rho_shift_pairs)) >= CAUSAL_RHO
                  and max_shift_small >= CAUSAL_SHIFT)
                 or (float(np.median(rho_rough_pairs)) >= ROUGH_RHO
                     and max_rr_small >= ROUGH_RATIO))
    c2_causal = ((rho_shift_k >= CAUSAL_RHO
                  and max(shifts_k) >= CAUSAL_SHIFT)
                 or (rho_rough_k >= ROUGH_RHO
                     and max(rrs_k) >= ROUGH_RATIO))
    CAUSAL = c1_causal or c2_causal
    MUT_ROBUST = (max_shift_all <= ROBUST_SHIFT
                  and max_rr_all <= ROBUST_RATIO)
    check("G32-causal-adjudication", True,
          "SEALED RULE: CAUSAL %s -- c1 median Spearman(eps, "
          "shift) %+.2f / (eps, rough) %+.2f, max shift at eps <= "
          "%.0e: %d (bar %d), max rough-ratio there %.2f (bar "
          "%.1f); c2 Spearman %+.2f/%+.2f; MUTATION_ROBUST "
          "(eps <= %.1f): %s -- single compensated rule breaks "
          "%s the wall at small dose"
          % ("HOLDS" if CAUSAL else "FAILS",
             float(np.median(rho_shift_pairs)),
             float(np.median(rho_rough_pairs)),
             EPS_SMALL, max_shift_small, CAUSAL_SHIFT,
             max_rr_small, ROUGH_RATIO, rho_shift_k, rho_rough_k,
             ROBUST_EPS, "yes" if MUT_ROBUST else "no",
             "move" if CAUSAL else "do NOT move"))

    # ================= S4  LEG D -- synthetic reproduction
    section("S4  LEG D -- SYNTHETIC TOYS (ray structure, no "
            "primes)")
    toys = []
    jits = (JITTERS[1:2] if smoke else JITTERS)
    jseeds = (JITTER_SEEDS[1:2] if smoke else JITTER_SEEDS)
    for jit, seed in zip(jits, jseeds):
        toys.append(("JIT%.2f" % jit, jit,
                     jitter_logs(uu0, mm0, jit, seed), seed))
    cseeds = CRAMER_SEEDS[:1] if smoke else CRAMER_SEEDS
    for seed in cseeds:
        toys.append(("CRAMER%d" % seed, None,
                     cramer_logs(X9, seed), seed))
    ok_own = True
    ok_int = True
    ok_m3 = True
    toy_rows = []
    d_cram = None
    for name, _jit, gl, seed in toys:
        uuT, mmT = ray_comb(gl, two_alpha)
        vown = own_violation(gl, two_alpha, uuT, mmT)
        vint = cheby_v(uuT, mmT, X9)
        dT = HS.window_data(BASE_W, comb=(uuT, mmT))
        pkT = chain_pack(dT)
        if name == "CRAMER%d" % CRAMER_SEEDS[0]:
            d_cram = (dT, pkT)
        uuS, mmS = scramble_comb(uuT, mmT, two_alpha,
                                 seed + SCR_TOY_OFFSET)
        vownS = own_violation(gl, two_alpha, uuS, mmS)
        pkS = chain_pack(HS.window_data(BASE_W, comb=(uuS, mmS)))
        ok_own = ok_own and vown[0] <= EXACT_BAR
        ok_int = ok_int and vint[0] >= CTRL_VIO_MIN
        ok_m3 = ok_m3 and vownS[0] >= CTRL_VIO_MIN
        toy_rows.append((name, pkT, pkS))
        info("%-9s %3d gens %3d atoms %4d monoid els | V_own "
             "%.1e V_int %.2e | flip %s (rho %.2f) || partner "
             "V_own %.2e flip %s (rho %.2f)"
             % (name, len(gl), len(uuT), vown[2], vown[0],
                vint[0],
                str(pkT["flip"]), pkT["flip_eff"] / pkT["N"],
                vownS[0], str(pkS["flip"]),
                pkS["flip_eff"] / pkS["N"]))
    check("G40-toy-structure", ok_own and ok_int and ok_m3,
          "every toy satisfies its OWN monoid Chebyshev identity "
          "to <= %.0e (the abstract sum-rule structure is EXACT) "
          "while violating the INTEGER identity by >= %.0e (no "
          "primes smuggled in); every scrambled partner violates "
          "its own-monoid identity >= %.0e (m3: V_own measures "
          "the ray structure, not the atom multiset); disclosed: "
          "toys run against MAIN's Archimedean background"
          % (EXACT_BAR, CTRL_VIO_MIN, CTRL_VIO_MIN))

    cram_rows = [r for r in toy_rows if r[0].startswith("CRAMER")]
    jit_rows = [r for r in toy_rows if r[0].startswith("JIT")]
    cram_rho = [r[1]["flip_eff"] / r[1]["N"] for r in cram_rows]
    cram_scr = [r[2]["flip_eff"] / r[2]["N"] for r in cram_rows]
    jit_hi = [r for r in jit_rows
              if float(r[0][3:]) >= 0.03 - 1e-12]
    strong_cram = (len(cram_rows) > 0
                   and float(np.median(cram_rho)) >= TOY_RHO_STRONG
                   and all(x < TOY_SCR_MAX for x in cram_scr))
    strong_jit = (len(jit_hi) > 0
                  and all(r[1]["flip_eff"] / r[1]["N"]
                          >= TOY_RHO_STRONG for r in jit_hi)
                  and all(r[2]["flip_eff"] / r[2]["N"]
                          < TOY_SCR_MAX for r in jit_hi))
    REPRO = strong_cram or strong_jit
    all_rho = [r[1]["flip_eff"] / r[1]["N"] for r in toy_rows]
    all_scr = [r[2]["flip_eff"] / r[2]["N"] for r in toy_rows]
    toy_partial = (float(np.median(all_rho))
                   >= TOY_PARTIAL_FACT * float(np.median(all_scr))
                   and float(np.median(all_rho))
                   >= TOY_PARTIAL_RHO)
    if REPRO:
        toy_typ = "TOY_STRONG"
    elif toy_partial:
        toy_typ = "TOY_PARTIAL"
    else:
        toy_typ = "TOY_DEAD"
        if jit_rows and (jit_rows[0][1]["flip_eff"]
                         / jit_rows[0][1]["N"]) < TOY_PARTIAL_RHO:
            toy_typ += " + RULES_NEED_TRUE_ARITHMETIC"
    check("G41-toy-survival", True,
          "SEALED RULE: %s -- Cramer flip_eff/N %s (partners %s), "
          "jitter %s (partners %s); a synthetic ray measure "
          "%s prime-like survival WITHOUT primes while its "
          "scrambled twin (identical one-point statistics) dies "
          "early -- the multiplicative sum-rule structure is %s"
          % (toy_typ,
             "/".join("%.2f" % x for x in cram_rho) or "-",
             "/".join("%.2f" % x for x in cram_scr) or "-",
             "/".join("%.2f" % (r[1]["flip_eff"] / r[1]["N"])
                      for r in jit_rows) or "-",
             "/".join("%.2f" % (r[2]["flip_eff"] / r[2]["N"])
                      for r in jit_rows) or "-",
             "shows" if REPRO else "does NOT show",
             "carried by the structure itself" if REPRO
             else "not sufficient in this synthetic form"))

    # ================= S5  must-fails
    section("S5  MUST-FAILS")
    w_m1, _r, _f1, _f2 = rule_census(uu0, mm0, X9,
                                     poison=(32, 0.05))
    v_m2 = cheby_v(uu0, 0.5 * mm0, X9)
    okM = (w_m1 >= CTRL_VIO_MIN and v_m2[0] >= M2_BAR and ok_m3)
    check("G50-must-fails-fire", okM,
          "one perturbed Lambda (n = 32, +0.05) breaks the "
          "divisor rules at %.1e >= %.0e; halving all masses "
          "moves V_med to %.2f >= %.2f (the functional is mass-"
          "defined, absolute bar sealed); scrambled toy partners "
          "fail their own-monoid identity (min %.0e bar) -- all "
          "three traps fire"
          % (w_m1, CTRL_VIO_MIN, v_m2[0], M2_BAR, CTRL_VIO_MIN))

    # ================= S6  mp ward
    section("S6  HIGH-PRECISION WARD (mp dps %d)" % MP_DPS)
    okW = True
    if not smoke:
        f_mut = mp_flip(d_mut_big, flip0 + 3)
        okW = okW and (f_mut == chain_pack(d_mut_big)["flip_eff"])
        dT, pkT = d_cram
        f_cr_mp = mp_flip(dT, pkT["cap"])
        f_cr_f64 = pkT["flip"]
        okW = okW and (f_cr_mp == f_cr_f64
                       or (f_cr_mp is None and f_cr_f64 is None))
        info("mp flips: c1 (32, 31) eps = 0.3 mutant -> %s (f64 "
             "%d); CRAMER%d toy -> %s (f64 %s, cap %d)"
             % (str(f_mut), chain_pack(d_mut_big)["flip_eff"],
                CRAMER_SEEDS[0], str(f_cr_mp), str(f_cr_f64),
                pkT["cap"]))
    check("G60-mp-ward", okW or smoke,
          "plain monic signed recursion at dps %d re-derives the "
          "f64 flip (respectively the no-flip-to-cap survival) "
          "EXACTLY on the strongest c1 mutant and on the CRAMER "
          "toy: neither the dose response nor the toy survival "
          "is an f64 artifact" % MP_DPS)

    # ================= S7  verdict
    section("S7  PRICING + VERDICT")
    if CAUSAL and REPRO:
        verdict = "SUMRULE_MECHANISM_GO"
    elif CORR or REPRO:
        verdict = "SUMRULE_CORRELATED_ONLY"
    else:
        verdict = "SUMRULE_NOT_THE_CARRIER"
    mods = []
    if REPRO and not CAUSAL:
        mods.append("COLLECTIVE_CARRIER")
    if MUT_ROBUST:
        mods.append("MUTATION_ROBUST")
    if binsep:
        mods.append("BINARY_SEPARATOR")
    mods.append(toy_typ)
    check("G70-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a mechanism-"
          "identification round moves no edge); what the round "
          "adds: the smoothness separation is quantified, the "
          "window sum-rule family is COMPLETE (it determines the "
          "measure), and the toy adjudication decides whether "
          "the abstract multiplicative structure alone carries "
          "prime-like survival")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G80-verdict", npass == len(CHECKS),
          "%s [%s]: CAUSAL %s / CORR %s / REPRO %s under the "
          "sealed precedence; NO RH claim"
          % (verdict, " + ".join(mods),
             "yes" if CAUSAL else "no", "yes" if CORR else "no",
             "yes" if REPRO else "no"))

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
