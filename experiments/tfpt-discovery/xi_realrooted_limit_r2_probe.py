#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""xi_realrooted_limit_r2_probe -- PRIME.XI.REALROOTED.LIMIT.01 ROUND 2

CCCLIII.  FROZEN SPEC v1 (2026-08-13).

EXPLORATION ONLY.  This probe writes no files.  It changes no verification
module, paper, ledger, website, manifest, or status marker.  It makes NO RH
claim, NO positivity claim, and NO counterexample claim.

MISSION.  Round 1 (xi_realrooted_limit_probe.py, CCCXLIII, frozen, untouched)
measured that the naive symmetrized finite-Euler family is comb-blind
(scramble ratio 1.00) and row-diverges through a digit-matched origin-cluster
mechanism.  Round 2 repairs the construction with round 1's own prescription:
(a) tame the origin, (b) respect the local Nyquist budget with an adaptive
comb X(t) <= (t/2pi)^beta (the CCM semilocal scaling of arXiv 2511.22755),
(c) carry the +1 pole-count unit explicitly.  The one question: does the
repaired family SEPARATE from scramble (the ratio must leave 1.00 decisively)
while its gate rows converge in X?

ANTI-CIRCULARITY FENCE (unchanged from round 1).  D is self-adjoint BY
CONSTRUCTION (spectrum = a mirror-symmetric set of real crossings built from
primes and the archimedean Gamma factor only).  No Weil-form wall matrix, no
positivity of any wall object, no zeta zero enters the construction.
mp.zetazero and friends are absent everywhere; mpmath zeta appears ONLY in
the TARGET section: the 55-digit -Xi'/Xi reference AND the Riemann-von
Mangoldt counting reference N(T) = theta(T)/pi + 1 + S(T), whose S(T) is
computed by continuous argument tracking of mp.zeta along sigma = 2 -> 1/2
(a reference readout, not a construction input).

ROUND-2 CONSTRUCTION (source-only, frozen).
(b) ADAPTIVE NYQUIST COMB.  Local truncation X(t) = (t/2pi)^beta.  Atom
    n = p^k enters the Euler phase with a smooth C^2 activation weight
        g_n(t) = s(clip(X(t)/n - 1, 0, 1)),  s(x) = x^3 (10 - 15x + 6x^2),
    i.e. OFF for X(t) <= n, fully ON for X(t) >= 2n.  The adaptive phase is
        phi(t) = - sum_{n <= X} c_n g_n(t) sin(t u_n),
        u_n = log n, c_n = Lambda(n)/(sqrt(n) u_n).
    Atoms whose full-activation time t_full(n) = 2pi (2n)^{1/beta} exceeds
    T - FULL_MARGIN are DROPPED (disclosed as X_eff per cell): the adaptive
    family cannot carry them inside the window, and dropping them keeps the
    per-atom E1 oscillatory tails exact (all kept atoms are fully on for
    t >= T_cut; asserted per cell).
(a) ORIGIN TAMING, which variant and why.  The mission offered two variants
    (Suzuki-style t-window away from 0, or normalizing out the zeta_X(1/2)
    origin factor).  The adaptive comb IS the compactification variant:
    X(t) < 2 for t < 2pi 2^{1/beta}, so g_n = 0 for every atom and
    Theta = theta identically on a neighborhood of the origin -- the origin
    phase velocity -phi'(0) = sum Lambda(n)/sqrt(n) ~ 2 sqrt(X) that spawned
    round 1's spurious cluster is removed EXACTLY, not approximately.  This
    is chosen over the hard t-window because it needs no low-t completion
    term and keeps the crossing set globally defined.  Asserted per cell:
    the edge phase Theta(GRID0) equals the pure-arch value to 1e-9.
(c) POLE-COUNT UNIT.  The counting reference carries the +1 of the pole
    factor s(s-1)/2 explicitly: N_ref(T) = theta(T)/pi + 1 + S(T) (exact
    integer, RvM).  Level algebra frozen BEFORE the run: theta dips to
    -3.53 > -2pi, so the LASTPASS lattice carries base levels {-1, 0} below
    the positive levels; a perfect comb (phi/pi = S exactly) therefore gives
        d(T) = N_D(T) - N_ref(T) = floor(theta/pi + phi/pi) + 2 - N_ref(T)
             = 1 + floor(phi/pi - S(T)) = +1  exactly.
    The +1 is the pole unit; the frozen prediction is POLE_UNIT_PRED = +1
    and the d-histogram is reported per cell.

SPECTRUM AND VARIANTS (as round 1).  Crossings of Theta(t) = theta(t) +
phi(t) through pi*Z on (GRID0, T_cut], T_cut at the crossing midpoint after
the last crossing <= T.  RAW (all crossings) / LASTPASS (last crossing per
level; the gate variant).  Completion: smooth archimedean tail (mpmath quad)
+ exact per-atom E1 oscillatory tails with FULL weights (valid because all
kept atoms are fully activated for t >= T_cut; scipy exp1, validated against
mp.quadosc).  log P via trace-resolvent path integral (GL-32 from z0 = 4i),
cross-checked against the direct window log-det.

TARGETS (mpmath; the ONLY namespace where mp.zeta appears).
    target(z) = -Xi'/Xi(z) at dps 55, s = 1/2 - iz, via
        i [ 1/s + 1/(s-1) - (1/2) log pi + (1/2) psi(s/2) + zeta'/zeta(s) ].
    S(T) at dps 20 by continuous argument tracking sigma: 2 -> 1/2 (the
    vertical leg needs no tracking: |zeta(2+it) - 1| <= zeta(2) - 1 < 1
    keeps Re zeta > 0, so arg is principal there).  Instrument check: the
    resulting N_ref(T) must be integer to 1e-6 at every checkpoint; if not,
    the checkpoint is nudged by +0.37 (max 3 tries, disclosed).

MEASUREMENT GRIDS (frozen).
    SAFE grid: z = x + iy, y in {0.75, 1.0, 1.5, 2.5, 4.0} x
               x in {0, 1.3, 3.7}  (15 points; Re s > 1).
    MID grid:  x in {30, 60, 120} x y in {1.0, 1.5, 2.5}  (9 points; the
               mid window where crossings sit against actual zero
               positions; still Re s > 1).
    Counting checkpoints: T_j = 100 * 2^{j/2}, j = 0..16 (100..25600),
               per cell restricted to T_j <= T_cut - 100.

THE THREE GATE ROWS (each an X-ladder; row rules identical to round 1).
  R1 RESOLVENT vs Az + B - Xi'/Xi:  per cell one joint complex affine fit
     (A, B) over SAFE u MID of R(z) = F_lp(z) - target(z); gate metric =
     post-fit rms over the JOINT grid (SAFE and MID rms reported split).
     The affine gauge is exactly the b + 2cz freedom of the normalized
     determinant e^{a+bz+cz^2} det(zI - D): round 1's comb-blind lattice
     bias is absorbed iff it is affine; everything else must come from the
     primes.
  R2 COUNTING vs RvM:  pole-unit readout d_j = N_D(T_j) - N_ref(T_j)
     (histogram; frozen prediction +1) and gate metric
     m2 = rms_j( phi(T_j)/pi - S(T_j) )  -- the construction-native
     continuous version of the counting comparison (the crossing lattice is
     generated by Theta, so Theta/pi - theta/pi - S = phi/pi - S is its
     counting fluctuation against the true one; the floor() of the raw
     integer d would quantize away the resolution).
  R3 LOG-P PATH INTEGRAL:  path-integral log P vs log Xi on the SAFE grid,
     complex LSQ fit of b (z - z0) + c (z^2 - z0^2); gate metric = post-fit
     rms.  Consistency cross-readout |A - 2c|, |B - b| (the two independent
     fits must agree on the gauge; reported, not gated).

BETA SCAN (frozen model-selection step, runs before the main ladder inside
the same frozen protocol).  BETAS = (0.5, 1.0, 1.5, 2.0) at SCAN_X =
(50, 300), T_SCAN = 10000.  beta = 0.5 is a DISCLOSED extension of the
mission's {1, 3/2, 2}: it is the naive-Nyquist reference point (crossing
density theta'/pi resolves u_n <= (1/2) log(t/2pi), i.e. n <= (t/2pi)^{1/2})
and is allowed to win only on the same frozen rule.  WINNER RULE: smallest
m2 at X = SCAN_X[-1]; ties within 5 percent break by smaller joint rms.
The winner beta is used for the main X ladder, T ladder, and scramble cells.

CONTROLS AND CENSUS (as round 1).  ARCH cell (X = 0): lattice reference.
SCRAMBLE cells at X in {20, 120, 800, 2000}, winner beta: atom positions
u_n -> u_n + 0.35 (2 frac(n golden) - 1), weights AND activation kept
arithmetic (activation depends on n, not on u).  T-ladder at X = 120,
T in {10000, 20000} vs 30000: noise floor NF = max(1e-9, max joint-grid
|F(T=2e4) - F(T=3e4)|).  Dyadic band census with parity assertion,
retrogression excess, origin diagnostic (5 lowest crossings + K-weights).

FROZEN BARS.
    T_MAIN = 30000; T_SCAN = 10000; T_LADDER = (10000, 20000) at X = 120;
    X_LADDER = (8, 20, 50, 120, 300, 800, 2000);
    SCAN_X = (50, 300); BETAS = (0.5, 1.0, 1.5, 2.0);
    SCR_X = (20, 120, 800, 2000); JITTER = 0.35; GOLDEN = (sqrt5 - 1)/2;
    GRID0 = 0.05; GRID_STEP = 0.01; THETA_ASY_MIN = 30.0;
    BISECT_ITERS = 30; REFINE_TOL = 0.15; REFINE_FACTOR = 8;
    SNAP_TOL = 0.05; Y_GRID = (0.75, 1.0, 1.5, 2.5, 4.0);
    X_OFFS = (0.0, 1.3, 3.7); MID_XS = (30.0, 60.0, 120.0);
    MID_YS = (1.0, 1.5, 2.5); Z0 = 4i; GL_PATH = 32;
    DPS_TARGET = 55; DPS_TAIL = 30; DPS_S = 20; FULL_MARGIN = 10.0;
    TJ_BASE = 100; TJ_COUNT = 17; POLE_UNIT_PRED = +1;
    DROP_BAR = 8; WOBBLE = 1.3; FLAT_BAR = 1.15;
    SCR_RATIO_BAR = 5; SCR_MIN_BAR = 1.5; SCR_SELF_BAR = 3;
    NF_FLOOR = 1e-9; RUNTIME_BAR = 1800 s.

VERDICT RULES (frozen).  Row typing on each gate ladder (R1 joint rms, R2
m2, R3 norm rms) exactly as round 1: CONVERGES if err(last) <= err(first)/
DROP_BAR and nonincreasing within WOBBLE at >= (steps-1) rungs (rungs with
both ends <= 10 NF are saturated-pass; NF applies to R1, NF_FLOOR to
R2/R3); DIVERGES if err(last) > 2 err(first); else PLATEAU; FLAT if
err(last) > err(prev)/FLAT_BAR while > 10 NF.  Separation channels at
X = 2000: SEP_MID = rms_MID_scr/rms_MID_main, SEP_CNT = m2_scr/m2_main.
DECISIVE separation := max(SEP_MID, SEP_CNT) >= SCR_RATIO_BAR and
min(SEP_MID, SEP_CNT) >= SCR_MIN_BAR and the max channel's scramble ladder
does not itself converge (scr_last >= scr_first/SCR_SELF_BAR).  Enum
priority (exactly one is printed):
    XILIMIT2-DIVERGES(mechanism)        >= 2 of 3 gate rows DIVERGE;
    XILIMIT2-STILL-VACUOUS(ratios)      separation not decisive;
    XILIMIT2-CONSUMES(sep, slopes)      decisive AND all 3 rows CONVERGE;
    XILIMIT2-CONVERGES-ROW(rows, rates) decisive, partial row convergence
                                        (the non-converging rows are typed
                                        in the parenthetical).
All measured rates, finals, and the d-histograms are printed either way.

SMOKE DISCLOSURE.  The pipeline is shaken out once with --smoke (T = 3000,
X in {8, 50}, scan {1.0, 2.0} x {50}, GRID_STEP = 0.02) before the frozen
run; smoke numbers are not verdict-bearing and are disclosed by this line.
Amendments to this spec, if any, are appended as AMENDMENT blocks with
reasons.
"""

from __future__ import annotations

import argparse
import hashlib
import math
import sys
import time

import mpmath as mp
import numpy as np
from scipy.special import exp1 as sp_exp1

# ----------------------------------------------------------------------
# frozen bars
# ----------------------------------------------------------------------
T_MAIN = 30000.0
T_SCAN = 10000.0
T_LADDER = (10000.0, 20000.0)          # extra T cells at X = 120
X_LADDER = (8, 20, 50, 120, 300, 800, 2000)
SCAN_X = (50, 300)
BETAS = (0.5, 1.0, 1.5, 2.0)
SCR_X = (20, 120, 800, 2000)
JITTER = 0.35
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
GRID0 = 0.05
GRID_STEP = 0.01
THETA_ASY_MIN = 30.0
BISECT_ITERS = 30
REFINE_TOL = 0.15
REFINE_FACTOR = 8
SNAP_TOL = 0.05
Y_GRID = (0.75, 1.0, 1.5, 2.5, 4.0)
X_OFFS = (0.0, 1.3, 3.7)
MID_XS = (30.0, 60.0, 120.0)
MID_YS = (1.0, 1.5, 2.5)
Z0 = 4.0j
GL_PATH = 32
DPS_TARGET = 55
DPS_TAIL = 30
DPS_S = 20
FULL_MARGIN = 10.0
TJ_BASE = 100.0
TJ_COUNT = 17
POLE_UNIT_PRED = 1
DROP_BAR = 8.0
WOBBLE = 1.3
FLAT_BAR = 1.15
SCR_RATIO_BAR = 5.0
SCR_MIN_BAR = 1.5
SCR_SELF_BAR = 3.0
NF_FLOOR = 1e-9
RUNTIME_BAR = 1800.0
GRID_PAD = 6.0
TWO_PI = 2.0 * math.pi

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

SAFE_Z = [complex(x, y) for y in Y_GRID for x in X_OFFS]
MID_Z = [complex(x, y) for y in MID_YS for x in MID_XS]
JOINT_Z = SAFE_Z + MID_Z

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %-36s %s" % ("PASS" if ok else "FAIL", name, detail))


# ----------------------------------------------------------------------
# source side: primes and adaptive atoms  (construction; zeta-free)
# ----------------------------------------------------------------------
def sieve_primes(nmax: int) -> np.ndarray:
    if nmax < 2:
        return np.zeros(0, dtype=np.int64)
    isp = np.ones(nmax + 1, dtype=bool)
    isp[:2] = False
    for p in range(2, int(nmax ** 0.5) + 1):
        if isp[p]:
            isp[p * p:: p] = False
    return np.nonzero(isp)[0].astype(np.int64)


def t_full_of(n: float, beta: float) -> float:
    """full-activation time of atom n: X(t) = 2n  <=>  t = 2pi (2n)^{1/beta}"""
    return TWO_PI * (2.0 * n) ** (1.0 / beta)


def build_atoms(X: int, T: float, beta: float, scramble: bool) -> dict:
    """Prime-power atoms n = p^k <= X, adaptively windowed.

    Atoms with t_full(n) > T - FULL_MARGIN are dropped (X_eff disclosure):
    they can never fully activate inside the window, and dropping them keeps
    the E1 tails exact.  Scramble jitters positions u only; weights and
    activation stay arithmetic (keyed to true n).
    """
    ns, us, aa, cc = [], [], [], []
    dropped = 0
    for p in sieve_primes(X):
        lp = math.log(float(p))
        pk = p
        while pk <= X:
            n = float(pk)
            if t_full_of(n, beta) > T - FULL_MARGIN:
                dropped += 1
            else:
                u_true = math.log(n)
                ns.append(pk)
                us.append(u_true)
                aa.append(lp / math.sqrt(n))
                cc.append(lp / (math.sqrt(n) * u_true))
            pk *= p
    n_arr = np.asarray(ns, dtype=np.float64)
    u = np.asarray(us, dtype=np.float64)
    a = np.asarray(aa, dtype=np.float64)
    c = np.asarray(cc, dtype=np.float64)
    if scramble and len(u):
        jit = JITTER * (2.0 * np.mod(n_arr * GOLDEN, 1.0) - 1.0)
        u = u + jit
    x_eff = int(n_arr.max()) if len(n_arr) else 0
    return {"n": n_arr, "u": u, "a": a, "c": c, "count": len(u),
            "beta": beta, "X": X, "x_eff": x_eff, "dropped": dropped}


def act_of(ts: np.ndarray, n: np.ndarray, beta: float) -> np.ndarray:
    """activation matrix g_n(t), shape (len(ts), len(n)); C^2 smootherstep"""
    Xt = (ts / TWO_PI) ** beta
    x = np.clip(Xt[:, None] / n[None, :] - 1.0, 0.0, 1.0)
    return x * x * x * (10.0 + x * (-15.0 + 6.0 * x))


# ----------------------------------------------------------------------
# archimedean phase theta and theta'
# ----------------------------------------------------------------------
LOG_2PI = math.log(2.0 * math.pi)


def theta_asy(t: np.ndarray) -> np.ndarray:
    return (t / 2.0 * (np.log(t) - LOG_2PI) - t / 2.0 - math.pi / 8.0
            + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t ** 3)
            + 31.0 / (80640.0 * t ** 5))


def theta_mp(t: float) -> float:
    with mp.workdps(DPS_TAIL):
        v = mp.im(mp.loggamma(mp.mpf("0.25") + 0.5j * mp.mpf(t))) \
            - mp.mpf(t) / 2 * mp.log(mp.pi)
    return float(v)


class ThetaGrid:
    """theta on the master grid: mpmath below THETA_ASY_MIN, asymptotic above."""

    def __init__(self, tmax: float):
        self.t = np.arange(GRID0, tmax + GRID_PAD, GRID_STEP)
        self.theta = np.empty_like(self.t)
        lo = self.t < THETA_ASY_MIN
        self.theta[~lo] = theta_asy(self.t[~lo])
        self.theta[lo] = np.array([theta_mp(float(x)) for x in self.t[lo]])


def theta_point(t: float) -> float:
    if t >= THETA_ASY_MIN:
        return float(theta_asy(np.array([t]))[0])
    return theta_mp(t)


# ----------------------------------------------------------------------
# adaptive Euler phase (chunked)
# ----------------------------------------------------------------------
def phi_of(ts: np.ndarray, atoms: dict) -> np.ndarray:
    if atoms["count"] == 0:
        return np.zeros_like(ts)
    out = np.zeros_like(ts)
    u, c, n, beta = atoms["u"], atoms["c"], atoms["n"], atoms["beta"]
    CH = 120_000
    AB = 64
    for i in range(0, len(ts), CH):
        tc = ts[i: i + CH]
        acc = np.zeros_like(tc)
        for j in range(0, len(u), AB):
            g = act_of(tc, n[j: j + AB], beta)
            acc -= (np.sin(np.outer(tc, u[j: j + AB])) * g) @ c[j: j + AB]
        out[i: i + CH] = acc
    return out


def Theta_eval(ts: np.ndarray, atoms: dict) -> np.ndarray:
    """Theta at arbitrary points (asymptotic theta; caller keeps t >= 30)."""
    return theta_asy(ts) + phi_of(ts, atoms)


def Theta_eval_low(t: float, atoms: dict) -> float:
    ph = 0.0
    if atoms["count"]:
        g = act_of(np.array([t]), atoms["n"], atoms["beta"])[0]
        ph = float(-np.dot(atoms["c"] * g, np.sin(t * atoms["u"])))
    return theta_point(t) + ph


# ----------------------------------------------------------------------
# cell construction: crossings of Theta through pi * Z
# ----------------------------------------------------------------------
def find_crossings(tg: ThetaGrid, atoms: dict, T: float) -> dict:
    t = tg.t
    n_grid = int(min(len(t), math.floor((T + GRID_PAD - GRID0) / GRID_STEP) + 1))
    t = t[:n_grid]
    Th = tg.theta[:n_grid] + (phi_of(t, atoms) if atoms["count"] else 0.0)

    m = np.floor(Th / math.pi)
    jump = np.nonzero(np.diff(m) != 0)[0]
    lev = np.maximum(m[jump], m[jump + 1]).astype(np.int64)
    lo = t[jump].copy()
    hi = t[jump + 1].copy()

    # refinement pass: near-tangency intervals without a floor change
    dist = np.abs(Th - (np.round(Th / math.pi) * math.pi))
    near = (dist[:-1] < REFINE_TOL) & (dist[1:] < REFINE_TOL) \
        & (np.diff(m) == 0)
    rec_lo, rec_hi, rec_lev = [], [], []
    idxs = np.nonzero(near)[0]
    if len(idxs):
        sub = np.linspace(0.0, 1.0, REFINE_FACTOR + 1)
        for i in idxs:
            tt = t[i] + sub * (t[i + 1] - t[i])
            if tt[0] >= THETA_ASY_MIN:
                Ts = Theta_eval(tt, atoms)
            else:
                Ts = np.array([Theta_eval_low(float(x), atoms) for x in tt])
            ms = np.floor(Ts / math.pi)
            jj = np.nonzero(np.diff(ms) != 0)[0]
            for j in jj:
                rec_lo.append(tt[j])
                rec_hi.append(tt[j + 1])
                rec_lev.append(int(max(ms[j], ms[j + 1])))
    n_recovered = len(rec_lo)
    if n_recovered:
        lo = np.concatenate([lo, np.array(rec_lo)])
        hi = np.concatenate([hi, np.array(rec_hi)])
        lev = np.concatenate([lev, np.array(rec_lev, dtype=np.int64)])
        order = np.argsort(lo)
        lo, hi, lev = lo[order], hi[order], lev[order]

    # vectorized bisection (t >= 30), scalar mpmath below
    high = lo >= THETA_ASY_MIN
    lo_h, hi_h, lev_h = lo[high], hi[high], lev[high] * math.pi
    for _ in range(BISECT_ITERS):
        mid = 0.5 * (lo_h + hi_h)
        vm = Theta_eval(mid, atoms) - lev_h
        vl = Theta_eval(lo_h, atoms) - lev_h
        left = (np.sign(vm) == np.sign(vl)) & (vm != 0.0)
        lo_h = np.where(left, mid, lo_h)
        hi_h = np.where(left, hi_h, mid)
    roots_h = 0.5 * (lo_h + hi_h)

    roots_l = []
    for L, a_, b_ in zip(lev[~high] * math.pi, lo[~high], hi[~high]):
        aa, bb = float(a_), float(b_)
        va = Theta_eval_low(aa, atoms) - L
        for _ in range(60):
            mm = 0.5 * (aa + bb)
            vm = Theta_eval_low(mm, atoms) - L
            if (vm > 0) == (va > 0) and vm != 0.0:
                aa, va = mm, vm
            else:
                bb = mm
        roots_l.append(0.5 * (aa + bb))
    roots = np.concatenate([np.array(roots_l), roots_h])
    levels = np.concatenate([lev[~high], lev[high]])
    order = np.argsort(roots)
    roots, levels = roots[order], levels[order]

    # cut at crossing midpoint after last crossing <= T
    inside = roots <= T
    if not inside.all():
        first_out = roots[~inside][0]
        last_in = roots[inside][-1]
        t_cut = 0.5 * (last_in + first_out)
    else:
        t_cut = T
    roots_w = roots[roots <= t_cut]
    levels_w = levels[roots <= t_cut]

    # LASTPASS: last crossing per level
    lp: dict[int, float] = {}
    for tv, lv in zip(roots_w, levels_w):
        lp[int(lv)] = float(tv)
    roots_lp = np.array(sorted(lp.values()))

    # dyadic census: count vs net phase per band (snapped edges)
    edges = [GRID0]
    b = 32.0
    while b < t_cut:
        edges.append(b)
        b *= 2.0
    edges.append(t_cut)
    census = []
    parity_ok = True
    excess_total = 0
    for ea, eb in zip(edges[:-1], edges[1:]):
        ia = int(round((ea - GRID0) / GRID_STEP))
        ib = int(round((eb - GRID0) / GRID_STEP))
        ia = min(max(ia, 0), n_grid - 1)
        ib = min(max(ib, 0), n_grid - 1)
        for _ in range(200):
            if abs(Th[ia] - round(Th[ia] / math.pi) * math.pi) > SNAP_TOL:
                break
            ia += 1
        for _ in range(200):
            if abs(Th[ib] - round(Th[ib] / math.pi) * math.pi) > SNAP_TOL:
                break
            ib -= 1
        ta, tb = t[ia], t[ib]
        cnt = int(np.count_nonzero((roots_w >= ta) & (roots_w <= tb)))
        net = int(math.floor(Th[ib] / math.pi) - math.floor(Th[ia] / math.pi))
        exc = cnt - net
        if exc < 0 or exc % 2 != 0:
            parity_ok = False
        excess_total += max(exc, 0)
        census.append((ta, tb, cnt, net, exc))

    edge_phase = float(Th[0])
    return {"roots": roots_w, "levels": levels_w, "roots_lp": roots_lp,
            "t_cut": float(t_cut), "census": census, "parity_ok": parity_ok,
            "excess": excess_total, "recovered": n_recovered,
            "edge_phase": edge_phase, "n_raw": len(roots_w),
            "n_lp": len(roots_lp)}


# ----------------------------------------------------------------------
# tails (exact per-atom E1, full weights: valid beyond T_cut by A13)
# ----------------------------------------------------------------------
_ST_CACHE: dict[tuple[float, complex], complex] = {}


def smooth_tail(z: complex, T: float) -> complex:
    key = (round(T, 6), complex(round(z.real, 12), round(z.imag, 12)))
    if key in _ST_CACHE:
        return _ST_CACHE[key]
    with mp.workdps(DPS_TAIL):
        zz = mp.mpc(z)

        def integrand(t):
            dth = (0.5 * (mp.log(t) - mp.log(2 * mp.pi)) - 1 / (48 * t ** 2)
                   - 7 / (1920 * t ** 4) - 31 / (16128 * t ** 6))
            return dth * 2 * zz / (t * t - zz * zz)

        v = mp.quad(integrand, [mp.mpf(T), 2 * mp.mpf(T), 8 * mp.mpf(T),
                                64 * mp.mpf(T), mp.inf]) / mp.pi
        out = complex(v)
    _ST_CACHE[key] = out
    return out


def osc_tail(z: complex, T: float, atoms: dict) -> complex:
    if atoms["count"] == 0:
        return 0.0 + 0.0j
    u = atoms["u"]
    a = atoms["a"]
    Tm = T - z
    Tp = T + z
    val = np.zeros(len(u), dtype=np.complex128)
    for s in (+1.0, -1.0):
        val += 0.5 * (np.exp(1j * s * u * z) * sp_exp1(-1j * s * u * Tm)
                      - np.exp(-1j * s * u * z) * sp_exp1(-1j * s * u * Tp))
    return complex(-(1.0 / math.pi) * np.dot(a, val))


def K_of(ts: np.ndarray, z: complex) -> np.ndarray:
    return 2.0 * z / (ts.astype(np.complex128) ** 2 - z * z)


def F_completed(roots: np.ndarray, z: complex, T_cut: float,
                atoms: dict) -> complex:
    return (complex(np.sum(K_of(roots, z))) + smooth_tail(z, T_cut)
            + osc_tail(z, T_cut, atoms))


# ----------------------------------------------------------------------
# TARGET SECTION (mpmath; zeta appears HERE ONLY)
# ----------------------------------------------------------------------
def target_parts(z: complex) -> complex:
    """target(z) = -Xi'/Xi(z) at dps 55."""
    with mp.workdps(DPS_TARGET):
        zz = mp.mpc(z)
        s = mp.mpf("0.5") - 1j * zz
        arch = (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                + mp.digamma(s / 2) / 2)
        pr = mp.zeta(s, derivative=1) / mp.zeta(s)
        return complex(1j * (arch + pr))


def log_xi_mp(zz: "mp.mpc") -> "mp.mpc":
    s = mp.mpf("0.5") - 1j * zz
    return (mp.log(mp.mpf("0.5")) + mp.log(s) + mp.log(s - 1)
            - s / 2 * mp.log(mp.pi) + mp.loggamma(s / 2)
            + mp.log(mp.zeta(s)))


def log_xi(z: complex) -> complex:
    with mp.workdps(DPS_TARGET):
        return complex(log_xi_mp(mp.mpc(z)))


def S_of_T(T: float) -> tuple[float, bool]:
    """S(T) by continuous argument tracking sigma: 2 -> 1/2 at height T.

    Vertical leg: Re zeta(2+it) >= 2 - zeta(2) > 0, principal arg suffices.
    Horizontal leg: adaptive steps, halve while |principal darg| > 1.2 or
    the proposed node has |zeta| < 1e-3 (near-zero guard, A1).  Returns
    (S, ok); ok = False if the tracker refused (step underflow).
    """
    with mp.workdps(DPS_S):
        tt = mp.mpf(T)
        cur = mp.zeta(2 + 1j * tt)
        total = mp.arg(cur)
        sigma = mp.mpf(2)
        target_s = mp.mpf("0.5")
        h = mp.mpf("0.25")
        h_min = mp.mpf(2) ** (-16)
        while sigma > target_s:
            h_try = min(h, sigma - target_s)
            ok_step = False
            while h_try >= h_min:
                nxt = mp.zeta(sigma - h_try + 1j * tt)
                if abs(nxt) < mp.mpf("1e-3"):
                    h_try /= 2
                    continue
                darg = mp.arg(nxt / cur)
                if abs(darg) > mp.mpf("1.2"):
                    h_try /= 2
                    continue
                total += darg
                cur = nxt
                sigma -= h_try
                ok_step = True
                break
            if not ok_step:
                return 0.0, False
            h = min(h_try * 2, mp.mpf("0.25"))
        return float(total / mp.pi), True


def build_counting_reference(tj_all: list[float]) -> dict:
    """N_ref(T) = theta(T)/pi + 1 + S(T); integer to 1e-6 or nudge (+0.37 x3)."""
    ref = {}
    for T0 in tj_all:
        T = T0
        got = None
        for _ in range(3):
            s_val, ok = S_of_T(T)
            if ok:
                n_ref = theta_point(T) / math.pi + 1.0 + s_val
                if abs(n_ref - round(n_ref)) <= 1e-6:
                    got = (T, s_val, int(round(n_ref)))
                    break
            T += 0.37
        ref[T0] = got          # None = failed (instrument check reports)
    return ref


# ----------------------------------------------------------------------
# path integral of the trace resolvent
# ----------------------------------------------------------------------
_GL_NODES, _GL_W = np.polynomial.legendre.leggauss(GL_PATH)
_GL_NODES = 0.5 * (_GL_NODES + 1.0)
_GL_W = 0.5 * _GL_W


def path_logdet_delta(roots: np.ndarray, T_cut: float, atoms: dict,
                      z: complex, z0: complex) -> complex:
    seg = z - z0
    acc = 0.0 + 0.0j
    for s_, w_ in zip(_GL_NODES, _GL_W):
        w = z0 + s_ * seg
        acc += w_ * (-F_completed(roots, w, T_cut, atoms))
    return acc * seg


def direct_logdet_delta_window(roots: np.ndarray, z: complex,
                               z0: complex) -> complex:
    r2 = roots.astype(np.complex128) ** 2
    return complex(np.sum(np.log((z * z - r2) / (z0 * z0 - r2))))


def path_logdet_delta_window(roots: np.ndarray, z: complex,
                             z0: complex) -> complex:
    seg = z - z0
    acc = 0.0 + 0.0j
    for s_, w_ in zip(_GL_NODES, _GL_W):
        w = z0 + s_ * seg
        acc += w_ * complex(np.sum(1.0 / (w - roots.astype(np.complex128))
                                   + 1.0 / (w + roots.astype(np.complex128))))
    return acc * seg


# ----------------------------------------------------------------------
# self-tests
# ----------------------------------------------------------------------
def self_tests() -> None:
    print("I. INSTRUMENT SELF-TESTS")
    worst = 0.0
    for t in (30.0, 50.0, 100.0, 1000.0):
        worst = max(worst, abs(float(theta_asy(np.array([t]))[0])
                               - theta_mp(t)))
    check("A1 theta asymptotic", worst <= 1e-11, "worst dev %.3e" % worst)

    pts = [1 + 2j, 3 - 1j, 0.5 + 30j, 200 - 5j]
    worst = 0.0
    with mp.workdps(30):
        for w in pts:
            a_ = complex(sp_exp1(np.complex128(w)))
            b_ = complex(mp.expint(1, mp.mpc(w)))
            worst = max(worst, abs(a_ - b_) / max(abs(b_), 1e-300))
    check("A2 exp1 complex", worst <= 1e-12, "worst rel %.3e" % worst)

    z = 1.3 + 1.5j
    Tq = 500.0
    a_atom = math.log(3.0)
    with mp.workdps(30):
        zz = mp.mpc(z)
        ref = mp.quadosc(lambda t: mp.cos(a_atom * t) * 2 * zz
                         / (t * t - zz * zz),
                         [Tq, mp.inf], period=2 * mp.pi / a_atom)
        ref = complex(ref)
    atoms1 = {"n": np.array([3.0]), "u": np.array([a_atom]),
              "a": np.array([1.0]), "c": np.array([1.0 / a_atom]),
              "count": 1, "beta": 1.0, "X": 3, "x_eff": 3, "dropped": 0}
    got = osc_tail(z, Tq, atoms1)
    dev = abs(got - (-(1.0 / math.pi) * ref))
    check("A3 osc-tail E1 formula", dev <= 3e-9, "dev %.3e" % dev)

    z = 3.7 + 2.5j
    v1 = smooth_tail(z, 10000.0)
    with mp.workdps(DPS_TAIL + 10):
        zz = mp.mpc(z)

        def integrand(t):
            dth = (0.5 * (mp.log(t) - mp.log(2 * mp.pi)) - 1 / (48 * t ** 2)
                   - 7 / (1920 * t ** 4) - 31 / (16128 * t ** 6))
            return dth * 2 * zz / (t * t - zz * zz)
        v2 = complex(mp.quad(integrand,
                             [10000, 12000, 15000, 20000, 40000, 80000,
                              320000, 2560000, mp.inf]) / mp.pi)
    dev = abs(v1 - v2)
    check("A4 smooth-tail quad", dev <= 1e-8, "dev %.3e" % dev)

    tgt = target_parts(2.5j)
    check("A5 target Herglotz sanity",
          abs(tgt.real) <= 1e-40 and tgt.imag > 0,
          "target(2.5i) = %.6e + %.6e i" % (tgt.real, tgt.imag))

    z = 1.3 + 2.5j
    with mp.workdps(DPS_TARGET):
        h = mp.mpf(10) ** (-15)
        zz = mp.mpc(z)
        num = complex(-(log_xi_mp(zz + h) - log_xi_mp(zz - h)) / (2 * h))
    tgt = target_parts(z)
    dev = abs(num - tgt)
    check("A6 target vs d/dz log Xi", dev <= 1e-10, "dev %.3e" % dev)

    # A10a S(T) tracker vs a low checkpoint where N(T) is textbook:
    # N(100) = 29 zeros below 100.
    s100, ok = S_of_T(100.0)
    n100 = theta_point(100.0) / math.pi + 1.0 + s100
    check("A10a S-tracker N(100) = 29",
          ok and abs(n100 - 29.0) <= 1e-6,
          "N(100) = %.9f (S = %+.6f)" % (n100, s100))

    # activation sanity: g = 0 below t_on, 1 above t_full, monotone ramp
    n_test = np.array([5.0])
    beta_t = 1.5
    t_on = TWO_PI * 5.0 ** (1.0 / beta_t)
    t_fu = t_full_of(5.0, beta_t)
    ts = np.array([0.5 * t_on, t_on, 0.5 * (t_on + t_fu), t_fu, 2 * t_fu])
    g = act_of(ts, n_test, beta_t)[:, 0]
    ok_act = (g[0] == 0.0 and g[1] == 0.0 and 0.0 < g[2] < 1.0
              and abs(g[3] - 1.0) <= 1e-12 and g[4] == 1.0)
    check("A15 activation window", ok_act,
          "g = " + ", ".join("%.4f" % x for x in g))


# ----------------------------------------------------------------------
# cell pipeline
# ----------------------------------------------------------------------
def build_cell(name: str, X: int, T: float, beta: float, scramble: bool,
               tg: ThetaGrid) -> dict:
    t0 = time.time()
    atoms = build_atoms(X, T, beta, scramble)
    cr = find_crossings(tg, atoms, T)
    cr["name"] = name
    cr["X"] = X
    cr["T"] = T
    cr["beta"] = beta
    cr["scramble"] = scramble
    cr["atoms"] = atoms
    cr["build_s"] = time.time() - t0
    return cr


def cell_resolvent(cell: dict, targets: dict) -> None:
    """joint affine fit F_lp - (Az + B) - target over SAFE u MID"""
    F = {z: F_completed(cell["roots_lp"], z, cell["t_cut"], cell["atoms"])
         for z in JOINT_Z}
    cell["F_lp"] = F
    R = np.array([F[z] - targets[z] for z in JOINT_Z], dtype=np.complex128)
    A_mat = np.array([[1.0, z] for z in JOINT_Z], dtype=np.complex128)
    sol, *_ = np.linalg.lstsq(A_mat, R, rcond=None)
    res = R - A_mat @ sol
    n_safe = len(SAFE_Z)
    cell["fit_B"] = complex(sol[0])
    cell["fit_A"] = complex(sol[1])
    cell["rms_joint"] = float(np.sqrt(np.mean(np.abs(res) ** 2)))
    cell["rms_safe"] = float(np.sqrt(np.mean(np.abs(res[:n_safe]) ** 2)))
    cell["rms_mid"] = float(np.sqrt(np.mean(np.abs(res[n_safe:]) ** 2)))
    cell["res"] = {z: complex(r) for z, r in zip(JOINT_Z, res)}
    # Herglotz (window only, uniform unit vector in the eigenbasis)
    herg_ok = True
    worst_h = 0.0
    dim = 2 * len(cell["roots_lp"])
    for z in JOINT_Z:
        Fw = complex(np.sum(K_of(cell["roots_lp"], z)))
        if Fw.imag <= 0:
            herg_ok = False
        if dim:
            worst_h = max(worst_h, abs(Fw / dim) * z.imag)
    cell["herg_ok"] = herg_ok
    cell["herg_worst"] = worst_h


def cell_counting(cell: dict, nref: dict, tj_all: list[float]) -> None:
    """pole-unit d_j and tracking metric m2 = rms(phi/pi - S)"""
    tj_use = [Tj for Tj in tj_all
              if Tj <= cell["t_cut"] - 100.0 and nref[Tj] is not None]
    ds, devs = [], []
    for Tj in tj_use:
        T_act, s_val, n_true = nref[Tj]
        n_d = int(np.count_nonzero(cell["roots_lp"] <= T_act))
        ds.append(n_d - n_true)
        if cell["atoms"]["count"]:
            ph = float(phi_of(np.array([T_act]), cell["atoms"])[0])
        else:
            ph = 0.0
        devs.append(ph / math.pi - s_val)
    cell["d_list"] = ds
    cell["m2"] = float(np.sqrt(np.mean(np.array(devs) ** 2))) if devs else 0.0
    cell["tj_used"] = len(tj_use)


# ----------------------------------------------------------------------
# verdict helpers (row rules identical to round 1)
# ----------------------------------------------------------------------
def row_type(errs: list, nf: float) -> tuple[str, float, bool]:
    e = np.array([float(x) for x in errs], dtype=np.float64)
    x = np.array(X_LADDER[:len(e)], dtype=np.float64)
    live = e > 10 * nf
    slope = float("nan")
    if live.sum() >= 3:
        slope = float(np.polyfit(np.log(x[live]), np.log(e[live]), 1)[0])
    diverges = e[-1] > 2.0 * e[0]
    flat = bool(len(e) >= 2 and e[-1] > e[-2] / FLAT_BAR and e[-1] > 10 * nf)
    steps_ok = 0
    steps_tot = 0
    for i in range(len(e) - 1):
        if e[i] <= 10 * nf and e[i + 1] <= 10 * nf:
            steps_ok += 1
            steps_tot += 1
            continue
        steps_tot += 1
        if e[i + 1] <= WOBBLE * e[i]:
            steps_ok += 1
    drops = e[-1] <= e[0] / DROP_BAR
    if drops and steps_ok >= steps_tot - 1:
        return "ROW-CONVERGES", slope, flat
    if diverges:
        return "ROW-DIVERGES", slope, flat
    return "ROW-PLATEAU", slope, flat


def d_hist(ds: list) -> str:
    if not ds:
        return "(none)"
    vals = sorted(set(ds))
    return " ".join("d=%+d:%d" % (v, ds.count(v)) for v in vals)


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
def main() -> int:
    global T_MAIN, T_SCAN, X_LADDER, SCAN_X, BETAS, SCR_X, T_LADDER, GRID_STEP
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke
    if smoke:
        T_MAIN = 3000.0
        T_SCAN = 3000.0
        X_LADDER = (8, 50)
        SCAN_X = (50,)
        BETAS = (1.0, 2.0)
        SCR_X = (50,)
        T_LADDER = (1500.0,)
        GRID_STEP = 0.02

    print("=" * 78)
    print("xi_realrooted_limit_r2_probe  PRIME.XI.REALROOTED.LIMIT.01 R2"
          "  (CCCLIII)")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
                                    "   *** SMOKE (not verdict-bearing) ***"
                                    if smoke else ""))
    print("=" * 78)

    self_tests()
    hard_fail = [c for c in CHECKS if not c[1]]
    if hard_fail:
        print("INSTRUMENT-FAIL: aborting before any verdict.")
        return 1

    # targets (-Xi'/Xi at dps 55) on the joint grid
    targets = {z: target_parts(z) for z in JOINT_Z}
    print("\nII. TARGETS (dps=%d)" % DPS_TARGET)
    for z in [complex(0, 1.0), complex(0, 2.5), complex(60, 1.0),
              complex(120, 1.0)]:
        if z in targets:
            print("  z=%6.1f+%.2fi  -Xi'/Xi = %+.12e %+.12e i"
                  % (z.real, z.imag, targets[z].real, targets[z].imag))

    # counting reference (S(T) tracked; mp.zeta, TARGET section)
    tj_all = [TJ_BASE * 2.0 ** (j / 2.0) for j in range(TJ_COUNT)]
    tj_all = [Tj for Tj in tj_all if Tj <= T_MAIN - 100.0]
    t0 = time.time()
    nref = build_counting_reference(tj_all)
    n_ok = sum(1 for v in nref.values() if v is not None)
    check("A10 N_ref integer at checkpoints", n_ok == len(tj_all),
          "%d/%d checkpoints (%.1f s)" % (n_ok, len(tj_all),
                                          time.time() - t0))
    print("  RvM reference (pole unit +1 explicit): "
          + ", ".join("N(%.0f)=%d" % (v[0], v[2])
                      for Tj, v in list(nref.items())[:6] if v is not None)
          + ", ...")

    # master theta grid
    t0 = time.time()
    tg = ThetaGrid(T_MAIN)
    print("\nIII. CELL BUILDS  (master grid %d pts, %.1f s)"
          % (len(tg.t), time.time() - t0))

    cells: dict[str, dict] = {}

    def register(name, X, T, beta, scr):
        c = build_cell(name, X, T, beta, scr, tg)
        cells[name] = c
        at = c["atoms"]
        print("  %-16s X=%5d Xeff=%5d drop=%3d beta=%.1f T=%7.0f raw=%6d "
              "lp=%6d exc=%5d rec=%2d parity=%s edgePhi=%+.4f  %.1f s"
              % (name, X, at["x_eff"], at["dropped"], beta, T, c["n_raw"],
                 c["n_lp"], c["excess"], c["recovered"],
                 "OK" if c["parity_ok"] else "VIOL", c["edge_phase"],
                 c["build_s"]))
        return c

    arch = register("ARCH", 0, T_MAIN, 1.0, False)

    # beta scan cells
    for beta in BETAS:
        for X in SCAN_X:
            register("SCAN-b%.1f-X%d" % (beta, X), X, T_SCAN, beta, False)

    parity_all = all(c["parity_ok"] for c in cells.values())

    # observables for scan cells + winner selection
    print("\nIV. BETA SCAN (T=%d; winner = min m2 at X=%d, tie -> rms)"
          % (int(T_SCAN), SCAN_X[-1]))
    cell_resolvent(arch, targets)
    cell_counting(arch, nref, tj_all)
    print("  %-16s  m2=%.4e  rms_joint=%.4e  rms_mid=%.4e   [reference]"
          % ("ARCH", arch["m2"], arch["rms_joint"], arch["rms_mid"]))
    scan_stats = {}
    for beta in BETAS:
        for X in SCAN_X:
            c = cells["SCAN-b%.1f-X%d" % (beta, X)]
            cell_resolvent(c, targets)
            cell_counting(c, nref, tj_all)
            scan_stats[(beta, X)] = (c["m2"], c["rms_joint"])
            print("  %-16s  m2=%.4e  rms_joint=%.4e  rms_mid=%.4e  "
                  "d-hist: %s"
                  % (c["name"], c["m2"], c["rms_joint"], c["rms_mid"],
                     d_hist(c["d_list"])))
    Xsel = SCAN_X[-1]
    m2s = {beta: scan_stats[(beta, Xsel)][0] for beta in BETAS}
    best_m2 = min(m2s.values())
    tied = [b for b in BETAS if m2s[b] <= 1.05 * best_m2]
    if len(tied) > 1:
        beta_win = min(tied, key=lambda b: scan_stats[(b, Xsel)][1])
    else:
        beta_win = min(BETAS, key=lambda b: m2s[b])
    print("  WINNER beta = %.1f  (m2 at X=%d: %s)"
          % (beta_win, Xsel,
             ", ".join("b%.1f:%.3e" % (b, m2s[b]) for b in BETAS)))

    # main ladder + T ladder + scramble (winner beta)
    print("\nV. MAIN CELLS (winner beta = %.1f)" % beta_win)
    for X in X_LADDER:
        register("MAIN-X%d" % X, X, T_MAIN, beta_win, False)
    for T in T_LADDER:
        register("TLAD-T%d" % int(T), 120 if not smoke else X_LADDER[-1],
                 T, beta_win, False)
    for X in SCR_X:
        register("SCR-X%d" % X, X, T_MAIN, beta_win, True)

    parity_all = parity_all and all(c["parity_ok"] for c in cells.values())
    check("A8 census parity all cells", parity_all, "%d cells" % len(cells))

    # A13 full-activation bound
    worst_slack = float("inf")
    for c in cells.values():
        at = c["atoms"]
        if at["count"]:
            slack = c["t_cut"] - t_full_of(float(at["n"].max()), at["beta"])
            worst_slack = min(worst_slack, slack)
    check("A13 atoms fully on below T_cut",
          worst_slack > 0.0 or worst_slack == float("inf"),
          "min slack %.1f" % (0.0 if worst_slack == float("inf")
                              else worst_slack))

    # A14 origin clean (adaptive comb: no atom active at GRID0)
    worst_edge = max(abs(c["edge_phase"] - arch["edge_phase"])
                     for c in cells.values())
    check("A14 origin tamed (edge phase = arch)", worst_edge <= 1e-9,
          "max |edgePhi - arch| = %.3e" % worst_edge)

    # A12 scramble displaces comb
    if SCR_X:
        sc = cells["SCR-X%d" % SCR_X[-1]]["atoms"]
        mn = build_atoms(SCR_X[-1], T_MAIN, beta_win, False)
        if sc["count"] and mn["count"] and sc["count"] == mn["count"]:
            dev = float(np.max(np.abs(sc["u"] - mn["u"])))
        else:
            dev = 0.0
        check("A12 scramble displaces comb", dev >= 0.1,
              "max|u_scr-u| = %.3f (atoms %d/%d)"
              % (dev, sc["count"], mn["count"]))

    # observables for main/tlad/scr cells
    print("\nVI. OBSERVABLES (LASTPASS; affine-gauged resolvent + counting)")
    for name, c in cells.items():
        if "rms_joint" not in c:
            cell_resolvent(c, targets)
            cell_counting(c, nref, tj_all)

    # noise floor from T ladder
    nf = NF_FLOOR
    if T_LADDER:
        xa = "MAIN-X120" if "MAIN-X120" in cells else \
            "MAIN-X%d" % X_LADDER[-1]
        ref = cells[xa]
        devs_by_T = {}
        for T in T_LADDER:
            ct = cells["TLAD-T%d" % int(T)]
            devs_by_T[T] = max(abs(ct["F_lp"][z] - ref["F_lp"][z])
                               for z in JOINT_Z)
        nf = max(NF_FLOOR, devs_by_T[T_LADDER[-1]])
        print("  T-ladder saturation vs T=%d:" % int(T_MAIN))
        for T in T_LADDER:
            print("    T=%6d  max joint-grid dev %.3e"
                  % (int(T), devs_by_T[T]))
    print("  DECLARED NOISE FLOOR NF = %.3e" % nf)

    # gate ladders
    print("\nVII. GATE LADDERS (X ladder, winner beta = %.1f)" % beta_win)
    hdr = "  %-24s" + "".join("  X=%-9d" % X for X in X_LADDER)
    print(hdr % "row")
    r1_j = [cells["MAIN-X%d" % X]["rms_joint"] for X in X_LADDER]
    r1_s = [cells["MAIN-X%d" % X]["rms_safe"] for X in X_LADDER]
    r1_m = [cells["MAIN-X%d" % X]["rms_mid"] for X in X_LADDER]
    r2_m = [cells["MAIN-X%d" % X]["m2"] for X in X_LADDER]
    print(("  %-24s" % "R1 rms_joint [GATE]")
          + "".join("  %.3e" % v for v in r1_j))
    print(("  %-24s" % "R1 rms_safe  [split]")
          + "".join("  %.3e" % v for v in r1_s))
    print(("  %-24s" % "R1 rms_mid   [split]")
          + "".join("  %.3e" % v for v in r1_m))
    print(("  %-24s" % "R2 m2 = rms(phi/pi-S)")
          + "".join("  %.3e" % v for v in r2_m))
    print("  ARCH reference: m2 = %.3e  rms_joint = %.3e  rms_mid = %.3e"
          % (arch["m2"], arch["rms_joint"], arch["rms_mid"]))

    # pole-unit histograms
    print("\n  POLE-UNIT READOUT (frozen prediction d = +%d):"
          % POLE_UNIT_PRED)
    for X in X_LADDER:
        c = cells["MAIN-X%d" % X]
        print("    MAIN-X%-5d  %s" % (X, d_hist(c["d_list"])))
    print("    ARCH        %s" % d_hist(arch["d_list"]))

    # affine gauge values
    print("\n  AFFINE GAUGE (A, B per cell):")
    for X in X_LADDER:
        c = cells["MAIN-X%d" % X]
        print("    X=%-5d  A=%+.4e%+.4ei  B=%+.4e%+.4ei"
              % (X, c["fit_A"].real, c["fit_A"].imag,
                 c["fit_B"].real, c["fit_B"].imag))

    # RAW pair-production meter
    print("  RAW excess census per MAIN cell: "
          + ", ".join("X%d:%d" % (X, cells["MAIN-X%d" % X]["excess"])
                      for X in X_LADDER))

    # origin diagnostic
    print("\nVII-b. ORIGIN DIAGNOSTIC (5 lowest LASTPASS crossings, "
          "|K| at z = i)")
    for name in ["ARCH"] + ["MAIN-X%d" % X for X in X_LADDER] \
            + ["SCR-X%d" % X for X in SCR_X]:
        c = cells[name]
        low5 = c["roots_lp"][:5]
        kw = K_of(low5, 1j)
        print("  %-12s edgePhi=%+8.4f  low t: %s"
              % (name, c["edge_phase"],
                 "  ".join("%.3f(|K|=%.2f)" % (t_, abs(k_))
                           for t_, k_ in zip(low5, kw))))

    # scramble control
    print("\nVIII. SCRAMBLE CONTROL (winner beta; ratios at X=%d)"
          % X_LADDER[-1])
    scr_m2 = {X: cells["SCR-X%d" % X]["m2"] for X in SCR_X}
    scr_mid = {X: cells["SCR-X%d" % X]["rms_mid"] for X in SCR_X}
    for X in SCR_X:
        print("  SCR-X%-5d  m2=%.4e  rms_mid=%.4e  rms_joint=%.4e  "
              "d-hist: %s"
              % (X, scr_m2[X], scr_mid[X],
                 cells["SCR-X%d" % X]["rms_joint"],
                 d_hist(cells["SCR-X%d" % X]["d_list"])))
    X_last = X_LADDER[-1]
    m2_main_last = cells["MAIN-X%d" % X_last]["m2"]
    mid_main_last = cells["MAIN-X%d" % X_last]["rms_mid"]
    sep_cnt = scr_m2[SCR_X[-1]] / max(m2_main_last, 1e-300)
    sep_mid = scr_mid[SCR_X[-1]] / max(mid_main_last, 1e-300)
    if sep_cnt >= sep_mid:
        scr_self = scr_m2[SCR_X[-1]] >= scr_m2[SCR_X[0]] / SCR_SELF_BAR
        ch = "CNT"
    else:
        scr_self = scr_mid[SCR_X[-1]] >= scr_mid[SCR_X[0]] / SCR_SELF_BAR
        ch = "MID"
    decisive = (max(sep_cnt, sep_mid) >= SCR_RATIO_BAR
                and min(sep_cnt, sep_mid) >= SCR_MIN_BAR and scr_self)
    print("  SEP_CNT = %.2f   SEP_MID = %.2f   scr-self(%s) = %s"
          % (sep_cnt, sep_mid, ch, scr_self))
    print("  [GATE] separation: %s"
          % ("DECISIVE" if decisive else "NOT DECISIVE -> VACUOUS"))

    # normalization: path-integral log P vs log Xi (R3)
    print("\nIX. R3 NORMALIZATION (path-integral log P, fit b,c; z0 = %s)"
          % Z0)
    ccell = cells["MAIN-X%d" % X_LADDER[min(3, len(X_LADDER) - 1)]]
    worst = 0.0
    for z in SAFE_Z[:3]:
        d1 = path_logdet_delta_window(ccell["roots_lp"], z, Z0)
        d2 = direct_logdet_delta_window(ccell["roots_lp"], z, Z0)
        worst = max(worst, abs(d1 - d2))
    check("A9 path-integral vs direct", worst <= 1e-9,
          "worst dev %.3e" % worst)

    lxi = {z: log_xi(z) for z in SAFE_Z}
    lxi0 = log_xi(complex(Z0))
    A_mat = np.array([[z - Z0, z * z - Z0 * Z0] for z in SAFE_Z],
                     dtype=np.complex128)
    r3 = []
    for X in X_LADDER:
        c = cells["MAIN-X%d" % X]
        r = np.array([(lxi[z] - lxi0)
                      - path_logdet_delta(c["roots_lp"], c["t_cut"],
                                          c["atoms"], z, Z0)
                      for z in SAFE_Z], dtype=np.complex128)
        sol, *_ = np.linalg.lstsq(A_mat, r, rcond=None)
        res = r - A_mat @ sol
        rms = float(np.sqrt(np.mean(np.abs(res) ** 2)))
        r3.append(rms)
        gauge_a = abs(c["fit_A"] - 2.0 * complex(sol[1]))
        gauge_b = abs(c["fit_B"] - complex(sol[0]))
        print("  X=%5d  b=%+.4e%+.4ei  c=%+.4e%+.4ei  rms=%.3e  "
              "|A-2c|=%.2e |B-b|=%.2e"
              % (X, sol[0].real, sol[0].imag, sol[1].real, sol[1].imag,
                 rms, gauge_a, gauge_b))

    # Herglotz
    herg_ok = all(c.get("herg_ok", True) for c in cells.values())
    worst_h = max(c.get("herg_worst", 0.0) for c in cells.values())
    check("A7 Herglotz (Im F>0, y|m|<=1)", herg_ok and worst_h <= 1 + 1e-12,
          "max y|m_N| = %.6f" % worst_h)

    # rate fits + verdict
    print("\nX. RATE FITS AND VERDICT")
    rows = {
        "R1-RESOLVENT": (r1_j, nf),
        "R2-COUNTING": (r2_m, NF_FLOOR),
        "R3-LOGP": (r3, NF_FLOOR),
    }
    row_results = {}
    for rname, (errs, nfr) in rows.items():
        typ, slope, flat = row_type(errs, nfr)
        row_results[rname] = (typ, slope, flat, errs[-1])
        print("  %-14s %s  slope=%.3f  flat=%s  final=%.3e"
              % (rname, typ, slope, flat, errs[-1]))

    conv = [r for r in rows if row_results[r][0] == "ROW-CONVERGES"]
    div = [r for r in rows if row_results[r][0] == "ROW-DIVERGES"]
    slopes = ",".join("%s:%.2f" % (r.split("-")[0], row_results[r][1])
                      for r in rows)
    seps = "SEP_MID %.2f, SEP_CNT %.2f" % (sep_mid, sep_cnt)
    if len(div) >= 2:
        mech = ("rows %s diverge; RAW excess X%d = %d; origin edgePhi "
                "%+.3f (tamed); see ladders"
                % (",".join(div), X_last,
                   cells["MAIN-X%d" % X_last]["excess"],
                   cells["MAIN-X%d" % X_last]["edge_phase"]))
        verdict = "XILIMIT2-DIVERGES(%s)" % mech
    elif not decisive:
        verdict = ("XILIMIT2-STILL-VACUOUS(%s; row types %s)"
                   % (seps, ",".join("%s:%s" % (r, row_results[r][0])
                                     for r in rows)))
    elif len(conv) == len(rows):
        verdict = "XILIMIT2-CONSUMES(%s; slopes %s)" % (seps, slopes)
    else:
        parts = ",".join("%s:%s(slope %.2f)"
                         % (r, row_results[r][0], row_results[r][1])
                         for r in rows)
        verdict = ("XILIMIT2-CONVERGES-ROW(converging: %s; all rows: %s; "
                   "%s)" % (",".join(conv) if conv else "none", parts, seps))

    wall = time.time() - T0_WALL
    check("A11 runtime", wall <= RUNTIME_BAR, "%.1f s" % wall)

    n_pass = sum(1 for c in CHECKS if c[1])
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s   beta_win %.1f"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16], beta_win))
    print("VERDICT: %s" % verdict)
    if smoke:
        print("*** SMOKE RUN — NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
