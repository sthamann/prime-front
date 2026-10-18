#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""xi_realrooted_limit_probe -- PRIME.XI.REALROOTED.LIMIT.01

CCCXLIII.  FROZEN SPEC v1 (2026-08-13).

EXPLORATION ONLY.  This probe writes no files.  It changes no verification
module, paper, ledger, website, manifest, or status marker.  It makes NO RH
claim, NO positivity claim, and NO counterexample claim.

ARCHITECTURE UNDER TEST (five-line endgame, this probe tests only round 1).
Let Xi(z) = xi(1/2 - iz), xi the completed Riemann xi.  RH is equivalent to
all zeros of Xi being real.  If finite SELF-ADJOINT operators D_N and
normalized determinants P_N(z) = exp(a_N + b_N z + c_N z^2) det(zI - D_N)
satisfy P_N -> Xi locally uniformly, Hurwitz forbids nonreal zeros in the
limit and RH follows.  Herglotz variant: m_N(z) = <e_N,(D_N - z)^{-1} e_N>
is a normal family with |m_N(z)| <= ||e_N||^2 / Im z; convergence on a safe
domain plus Vitali extends to the whole upper half-plane.  ROUND 1 measures
exactly one thing: whether a concrete source-side operator family has the
right resolvent-trace limit on the safe domain at all.  Nothing else.

ANTI-CIRCULARITY FENCE.  D_N is self-adjoint BY CONSTRUCTION (its spectrum
is a set of real numbers built from primes and the archimedean Gamma factor
only).  No Weil-form wall matrix is consumed, no positivity of any wall
object is used, no zeta zero enters the construction.  mp.zetazero and
friends are absent from the construction; mpmath zeta appears ONLY in the
TARGET section (the 50-digit reference -Xi'/Xi).

CONSTRUCTION (source-only, frozen).  Truncated-Euler-product multiplication
+ symmetrization, operator-ized through its phase on the Fourier-log
lattice.  With theta(t) = Im loggamma(1/4 + it/2) - (t/2) log pi (the
Riemann-Siegel theta: Gamma and pi only) and the finite Euler phase

    phi_X(t) = Im log zeta_X(1/2 + it) = - sum_{n = p^k <= X} c_n sin(t u_n),
    u_n = log n,  c_n = Lambda(n) / (sqrt(n) u_n),

the symmetrized finite-Euler surrogate 2 Im[e^{i theta} zeta_X(1/2+it)]
vanishes exactly where Theta_X(t) = theta(t) + phi_X(t) crosses pi * Z (SIN
branch; branch fixed a priori by the source-side pole factor s(s-1)/2 of xi,
which carries the +1 count unit).  D_{X,T} is the self-adjoint operator
whose spectrum is the mirror-symmetric crossing set {+-t_k} in (0, T_cut].
Two variants, both frozen: RAW (every crossing = every real zero of the
symmetrized partial Euler product) and LASTPASS (for each integer level m
keep the last crossing; = functional calculus of the monotone completion of
Theta_X applied to the free clock).  T_cut sits at the crossing midpoint
after the last crossing <= T (kills the boundary sawtooth).

RESOLVENT AND COMPLETION.  F(z) = sum_k K(t_k; z) + ST(z,T) + OT(z,T) with
K(t; z) = 1/(t - z) + 1/(-t - z) = 2z/(t^2 - z^2), ST the smooth
archimedean tail integral (1/pi) int_T^inf theta'(t) K(t) dt (mpmath quad),
OT the exact per-atom oscillatory tail -(1/pi) sum_n a_n int_T^inf
cos(t u_n) K(t) dt via complex E_1 (a_n = Lambda(n)/sqrt(n); scipy exp1,
formula validated against mpmath quadosc in a hard self-test).
log P_N is computed as a trace-of-resolvent path integral (Gauss-Legendre
32 along segments from z0), NOT by eigenvalue tracking; a direct window
log-det cross-check must agree to 1e-9.

TARGET (50 digits, mpmath).  s = 1/2 - iz, and
    target(z) = -Xi'/Xi(z) = i [ 1/s + 1/(s-1) - (1/2) log pi
                                 + (1/2) psi(s/2) + zeta'/zeta(s) ].
Safe domain: Im z > 1/2 <=> Re s > 1 (absolutely convergent Euler product).
Sample grid: z = x + iy, y in {0.75, 1.0, 1.5, 2.5, 4.0} x x in
{0, 1.3, 3.7} (15 points).  primetarget(z) = i (zeta'/zeta)(s) - i (pole,
Gamma, log pi terms removed); archtarget = target - primetarget.

OBSERVABLES (all reported per cell and per z):
  ABS   Delta_abs  = F - target                      (absolute limit);
  DIFF  Delta_diff = [F_X - F_arch] - primetarget    (prime response, the
        arch-only cell is the lattice-bias reference; X-independent lattice
        defects cancel here);
  DIFFX Delta_diffX = [F_X - F_arch] - primetarget_{n<=X} (matched
        truncation; isolates response fidelity from the Euler tail);
  LIN   Delta_lin  = [F_X - F_arch] - LM, LM the exact first-order crossing
        displacement model  - sum_{arch crossings} K'(t) phi_X(t)/Theta'(t)
        (second-order/backreaction meter, X <= 120 cells);
  NORM  path-integral log P vs log Xi, complex LSQ fit of
        b (z - z0) + c (z^2 - z0^2): drift of (b_N, c_N) and post-fit rms;
  HERG  m_N(z) = (1/dim) sum 1/(lambda - z): assert Im F_window > 0 and
        y |m_N| <= 1 (Herglotz normal-family bound).

HYPOTHESIS FROZEN BEFORE THE RUN.  On the safe domain the DIFF error should
fall like the absolutely-convergent Euler tail, |Delta_diff| ~ X^{1/2 - y},
until pair-production (retrogressions of Theta_X, censused per band)
breaks the RAW family; the ABS error should saturate at the X-independent
archimedean lattice bias measured by the arch cell.  A scrambled comb
(atom positions u_n -> u_n + 0.35 (2 frac(n golden) - 1), weights kept)
must NOT converge: otherwise the family never consumed the primes.

CONTROLS AND CENSUS.  ARCH cell (X = 0): lattice-bias reference + pipeline
calibration.  SCRAMBLE cells at X in {20, 120, 800, 2000}.  T-ladder at
X = 120, T in {10000, 20000, 30000}: tail-completion saturation defines the
declared noise floor NF = max(1e-9, max gate-point |F(T=2e4) - F(T=3e4)|).
Per-cell dyadic band census: crossing count vs net phase (parity asserted),
retrogression excess = pair-production meter, low-edge phase margins.

FROZEN BARS.
    T_MAIN = 30000; T_LADDER = (10000, 20000) at X = 120;
    X_LADDER = (8, 20, 50, 120, 300, 800, 2000);
    SCR_X = (20, 120, 800, 2000); JITTER = 0.35; GOLDEN = (sqrt5 - 1)/2;
    GRID0 = 0.05; GRID_STEP = 0.01; THETA_ASY_MIN = 30.0;
    BISECT_ITERS = 30; REFINE_TOL = 0.15 rad; REFINE_FACTOR = 8;
    SNAP_TOL = 0.05 rad; Y_GRID = (0.75, 1.0, 1.5, 2.5, 4.0);
    X_OFFS = (0.0, 1.3, 3.7); GATE_YS = (1.0, 1.5, 2.5); Z0 = 4i;
    GL_PATH = 32; DPS_TARGET = 55; DPS_TAIL = 30;
    DROP_BAR = 8; WOBBLE = 1.3; SCR_RATIO_BAR = 5; SCR_SELF_BAR = 3;
    NF_FLOOR = 1e-9; RUNTIME_BAR = 1800 s.

VERDICT RULES (frozen).  Gate rows: LASTPASS |Delta_diff| at
(x, y) = (0, 1.0), (0, 1.5), (0, 2.5) across the X ladder.  A row
CONVERGES if err(2000) <= err(8)/DROP_BAR and the ladder is nonincreasing
within factor WOBBLE at >= 5 of 6 steps (steps where both ends < 10 NF are
skipped as saturated-pass); PLATEAU if it stalls > 10 NF; DIVERGES if
err(2000) > 2 err(8).  Scramble gate: err_scr(2000) >= SCR_RATIO_BAR *
err_main(2000) on >= 2 of 3 gate rows AND err_scr(2000) >= err_scr(20) /
SCR_SELF_BAR; else XILIMIT-VACUOUS.  Overall enum:
    XILIMIT-CONVERGES(rates, domain)  all gate rows CONVERGE and
        |Delta_abs(X = 2000)| <= 10 NF at gate points;
    XILIMIT-WRONGLIMIT(identified)    gate rows CONVERGE (prime response
        correct) but ABS saturates at an identified defect (arch-lattice
        bias, digit-matched to the arch cell within the DIFF error);
    XILIMIT-DIVERGES                  >= 2 gate rows DIVERGE;
    XILIMIT-VACUOUS                   scramble gate fails.
Mixed outcomes are reported per row and the overall enum takes the worst
gate row with a parenthetical.  All measured rates and the empirical safe
domain (X range before RAW pair-production breaks) are printed either way.

SMOKE DISCLOSURE.  The pipeline is shaken out once with --smoke
(T = 3000, X in {8, 50}, GRID_STEP = 0.02) before the frozen run; smoke
numbers are not verdict-bearing and are disclosed by this line.  Amendments
to this spec, if any, are appended as AMENDMENT blocks with reasons.

AMENDMENT A1 (implementation only, after the first smoke attempt).  The
self-test A6 (target vs numeric derivative of log Xi) was computed through
float64 casts and failed at 1.0e-2 from catastrophic cancellation, not from
a target defect; it is recomputed entirely in mpmath at dps 55 and now
agrees to < 1e-40.  No bar, observable, or verdict rule changed.

AMENDMENT A2 (gate observable, after the disclosed smoke run and BEFORE any
frozen run).  The smoke run measured two facts that falsify the drafted
gate: (i) the prime-free ARCH lattice already sits within 1.5e-2 of the
FULL target at y = 1 (the integer count defect of the lattice happens to
lie at the same 1/(y - 1/2) pole scale as the zeta'/zeta pole, so the
"arch-bias reference" is not prime-clean), and (ii) the measured linear
prime response of the crossing lattice is strongly attenuated relative to
the naive per-atom model i Lambda(n) n^{-1/2} e^{izu} (the crossing lattice
at the kernel-dominant low-t region is sparser than the atom frequencies -
an aliasing attenuation the smoke quantified at roughly 5x-100x).  DIFF
therefore measures a falsified linear-response model, not the mission
question.  The gate observable is moved to the mission-native ABS =
|F - (-Xi'/Xi)| on the same gate rows, the scramble non-vacuity gate is
likewise evaluated on ABS, and DIFF / DIFFX / LM are demoted to reported
attenuation diagnostics.  The predicted slope 1/2 - y is demoted to a
reference line (it belonged to the falsified linear model).  All numeric
bars are unchanged (DROP_BAR = 8, WOBBLE = 1.3, SCR_RATIO_BAR = 5,
SCR_SELF_BAR = 3, NF rule).  Plateau detection (frozen here): a gate row is
FLAT if err(X=2000) > err(X=800)/1.15; if any gate row is FLAT above 10 NF
the overall enum is XILIMIT-WRONGLIMIT with the residual field reported and
its X-stability quantified; if all gate rows CONVERGE and the final row
values are <= 10 NF the enum is XILIMIT-CONVERGES.

AMENDMENT A3 (exit semantics and origin diagnostics, after the first
completed frozen run; no bar, enum rule, or measured value changed).  The
first frozen run produced its honest verdict (scramble ties the main comb,
gate rows diverge) but exited 1 because the scramble VERDICT GATE A13 was
wired as an instrument assertion; a failed scientific gate is a verdict,
not an instrument fault, so A13 is reclassified as a reported gate and the
exit code covers instrument checks only.  Two diagnostics are added for the
attribution of the measured divergence: (i) the five lowest crossings per
cell with their K-weights at z = i (the origin cluster: the Euler phase
velocity at t = 0 is -phi'(0) = sum Lambda(n)/sqrt(n) ~ 2 sqrt(X), which
pulls Theta through negative levels near the origin), and (ii) an explicit
disclosure when Theta(GRID0) < -pi, in which case additional crossings
exist below the grid start and are not collected -- including them would
add further origin-cluster weight, i.e. strengthen the measured
divergence, not weaken it.  The first frozen run's numbers were reproduced
identically on the re-run (deterministic pipeline).
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
T_LADDER = (10000.0, 20000.0)          # extra T cells at X = 120
X_LADDER = (8, 20, 50, 120, 300, 800, 2000)
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
GATE_YS = (1.0, 1.5, 2.5)
Z0 = 4.0j
GL_PATH = 32
DPS_TARGET = 55
DPS_TAIL = 30
DROP_BAR = 8.0
WOBBLE = 1.3
SCR_RATIO_BAR = 5.0
SCR_SELF_BAR = 3.0
NF_FLOOR = 1e-9
RUNTIME_BAR = 1800.0
LIN_XMAX = 120                          # LM diagnostic on X <= 120 cells
GRID_PAD = 6.0                          # grid extends past T for midpoint cut

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

Z_GRID = [complex(x, y) for y in Y_GRID for x in X_OFFS]
GATE_Z = [complex(0.0, y) for y in GATE_YS]

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %-34s %s" % ("PASS" if ok else "FAIL", name, detail))


# ----------------------------------------------------------------------
# source side: primes and atoms  (construction; zeta-free)
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


def build_atoms(X: int, scramble: bool) -> dict:
    """Prime-power atoms n = p^k <= X.

    u  : positions log n (scrambled -> jittered, weights untouched)
    a  : Lambda(n)/sqrt(n)      (phi' coefficients)
    c  : Lambda(n)/(sqrt(n) u)  (phi coefficients, TRUE u even when scrambled
                                 the weight stays the arithmetic one)
    """
    ns, us, aa, cc = [], [], [], []
    for p in sieve_primes(X):
        lp = math.log(float(p))
        pk = p
        while pk <= X:
            n = float(pk)
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
    return {"n": n_arr, "u": u, "a": a, "c": c, "count": len(u)}


# ----------------------------------------------------------------------
# archimedean phase theta and theta'
# ----------------------------------------------------------------------
LOG_2PI = math.log(2.0 * math.pi)
LOG_PI = math.log(math.pi)


def theta_asy(t: np.ndarray) -> np.ndarray:
    """Riemann-Siegel theta, asymptotic series, valid t >= THETA_ASY_MIN."""
    return (t / 2.0 * (np.log(t) - LOG_2PI) - t / 2.0 - math.pi / 8.0
            + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t ** 3)
            + 31.0 / (80640.0 * t ** 5))


def dtheta_asy(t: np.ndarray) -> np.ndarray:
    return (0.5 * (np.log(t) - LOG_2PI) - 1.0 / (48.0 * t * t)
            - 7.0 / (1920.0 * t ** 4) - 31.0 / (16128.0 * t ** 6))


def theta_mp(t: float) -> float:
    with mp.workdps(DPS_TAIL):
        v = mp.im(mp.loggamma(mp.mpf("0.25") + 0.5j * mp.mpf(t))) \
            - mp.mpf(t) / 2 * mp.log(mp.pi)
    return float(v)


def dtheta_mp(t: float) -> float:
    with mp.workdps(DPS_TAIL):
        v = 0.5 * mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * mp.mpf(t))) \
            - 0.5 * mp.log(mp.pi)
    return float(v)


class ThetaGrid:
    """theta on the master grid: mpmath below THETA_ASY_MIN, asymptotic above."""

    def __init__(self, tmax: float):
        self.t = np.arange(GRID0, tmax + GRID_PAD, GRID_STEP)
        self.theta = np.empty_like(self.t)
        lo = self.t < THETA_ASY_MIN
        self.theta[~lo] = theta_asy(self.t[~lo])
        self.theta[lo] = np.array([theta_mp(float(x)) for x in self.t[lo]])
        self.dtheta = np.empty_like(self.t)
        self.dtheta[~lo] = dtheta_asy(self.t[~lo])
        self.dtheta[lo] = np.array([dtheta_mp(float(x)) for x in self.t[lo]])


def theta_point(t: float) -> float:
    if t >= THETA_ASY_MIN:
        return float(theta_asy(np.array([t]))[0])
    return theta_mp(t)


def dtheta_point(t: float) -> float:
    if t >= THETA_ASY_MIN:
        return float(dtheta_asy(np.array([t]))[0])
    return dtheta_mp(t)


# ----------------------------------------------------------------------
# Euler phase on arrays (chunked)
# ----------------------------------------------------------------------
def phi_of(ts: np.ndarray, atoms: dict) -> np.ndarray:
    if atoms["count"] == 0:
        return np.zeros_like(ts)
    out = np.zeros_like(ts)
    u, c = atoms["u"], atoms["c"]
    CH = 200_000
    AB = 64
    for i in range(0, len(ts), CH):
        tc = ts[i: i + CH]
        acc = np.zeros_like(tc)
        for j in range(0, len(u), AB):
            acc -= np.sin(np.outer(tc, u[j: j + AB])) @ c[j: j + AB]
        out[i: i + CH] = acc
    return out


def dphi_of(ts: np.ndarray, atoms: dict) -> np.ndarray:
    if atoms["count"] == 0:
        return np.zeros_like(ts)
    out = np.zeros_like(ts)
    u, a = atoms["u"], atoms["a"]
    CH = 200_000
    AB = 64
    for i in range(0, len(ts), CH):
        tc = ts[i: i + CH]
        acc = np.zeros_like(tc)
        for j in range(0, len(u), AB):
            acc -= np.cos(np.outer(tc, u[j: j + AB])) @ a[j: j + AB]
        out[i: i + CH] = acc
    return out


def Theta_eval(ts: np.ndarray, atoms: dict) -> np.ndarray:
    """Theta at arbitrary points (asymptotic theta; caller keeps t >= 30)."""
    return theta_asy(ts) + phi_of(ts, atoms)


def Theta_eval_low(t: float, atoms: dict) -> float:
    ph = 0.0
    if atoms["count"]:
        ph = float(-np.dot(atoms["c"], np.sin(t * atoms["u"])))
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
    jump = np.nonzero(np.diff(m) != 0)[0]           # bracket [i, i+1]
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
        t_cut = T          # no crossing beyond T on padded grid (censused)
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
        # snap away from levels
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
# tails
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
    """-(1/pi) sum_n a_n int_T^inf cos(t u_n) K(t;z) dt  via complex E1."""
    if atoms["count"] == 0:
        return 0.0 + 0.0j
    u = atoms["u"]
    a = atoms["a"]
    # int_T^inf cos(at)/(t -+ z) dt =
    #   1/2 sum_{s=+-} e^{s i a z} E1(-s i a (T - z))        [for (t - z)]
    #   1/2 sum_{s=+-} e^{-s i a z} E1(-s i a (T + z))       [for (t + z)]
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
# targets (mpmath, 50+ digits)  -- zeta appears HERE ONLY
# ----------------------------------------------------------------------
def target_parts(z: complex) -> tuple[complex, complex]:
    """returns (target, primetarget) = (-Xi'/Xi(z), i zeta'/zeta(s))."""
    with mp.workdps(DPS_TARGET):
        zz = mp.mpc(z)
        s = mp.mpf("0.5") - 1j * zz
        arch = (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                + mp.digamma(s / 2) / 2)
        pr = mp.zeta(s, derivative=1) / mp.zeta(s)
        tgt = 1j * (arch + pr)
        return complex(tgt), complex(1j * pr)


def primetarget_trunc(z: complex, atoms: dict) -> complex:
    """-i sum_{n<=X} Lambda(n) n^{-1/2} e^{i z log n}  (TRUE positions)."""
    if atoms["count"] == 0:
        return 0.0 + 0.0j
    n = atoms["n"]
    lam_over_sqrt = atoms["a"]
    return complex(-1j * np.sum(lam_over_sqrt
                                * np.exp(1j * z * np.log(n))))


def log_xi_mp(zz: "mp.mpc") -> "mp.mpc":
    s = mp.mpf("0.5") - 1j * zz
    return (mp.log(mp.mpf("0.5")) + mp.log(s) + mp.log(s - 1)
            - s / 2 * mp.log(mp.pi) + mp.loggamma(s / 2)
            + mp.log(mp.zeta(s)))


def log_xi(z: complex) -> complex:
    with mp.workdps(DPS_TARGET):
        return complex(log_xi_mp(mp.mpc(z)))


# ----------------------------------------------------------------------
# path integral of the trace resolvent
# ----------------------------------------------------------------------
_GL_NODES, _GL_W = np.polynomial.legendre.leggauss(GL_PATH)
_GL_NODES = 0.5 * (_GL_NODES + 1.0)
_GL_W = 0.5 * _GL_W


def path_logdet_delta(roots: np.ndarray, T_cut: float, atoms: dict,
                      z: complex, z0: complex) -> complex:
    """int_{z0}^{z} tr (wI - D)^{-1} dw with completed trace = -F(w)."""
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
    # A1 theta asymptotic vs mpmath
    worst = 0.0
    for t in (30.0, 50.0, 100.0, 1000.0):
        worst = max(worst, abs(float(theta_asy(np.array([t]))[0])
                               - theta_mp(t)))
    check("A1 theta asymptotic", worst <= 1e-11, "worst dev %.3e" % worst)

    # A2 scipy exp1 vs mpmath expint on complex points
    pts = [1 + 2j, 3 - 1j, 0.5 + 30j, 200 - 5j]
    worst = 0.0
    with mp.workdps(30):
        for w in pts:
            a_ = complex(sp_exp1(np.complex128(w)))
            b_ = complex(mp.expint(1, mp.mpc(w)))
            worst = max(worst, abs(a_ - b_) / max(abs(b_), 1e-300))
    check("A2 exp1 complex", worst <= 1e-12, "worst rel %.3e" % worst)

    # A3 osc tail formula vs mpmath quadosc (one hard case)
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
              "count": 1}
    got = osc_tail(z, Tq, atoms1)          # = -(1/pi) * integral
    dev = abs(got - (-(1.0 / math.pi) * ref))
    check("A3 osc-tail E1 formula", dev <= 3e-9, "dev %.3e" % dev)

    # A4 smooth tail: mpmath quad vs finer split
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

    # A5 target sanity: purely imaginary on the imaginary axis, Im > 0
    tgt, pr = target_parts(2.5j)
    check("A5 target Herglotz sanity",
          abs(tgt.real) <= 1e-40 and tgt.imag > 0,
          "target(2.5i) = %.6e + %.6e i" % (tgt.real, tgt.imag))

    # A6 target vs numeric derivative of log Xi (all in mpmath, dps 55)
    z = 1.3 + 2.5j
    with mp.workdps(DPS_TARGET):
        h = mp.mpf(10) ** (-15)
        zz = mp.mpc(z)
        num = complex(-(log_xi_mp(zz + h) - log_xi_mp(zz - h)) / (2 * h))
    tgt, _ = target_parts(z)
    dev = abs(num - tgt)
    check("A6 target vs d/dz log Xi", dev <= 1e-10, "dev %.3e" % dev)


# ----------------------------------------------------------------------
# cell pipeline
# ----------------------------------------------------------------------
def build_cell(name: str, X: int, T: float, scramble: bool,
               tg: ThetaGrid) -> dict:
    t0 = time.time()
    atoms = build_atoms(X, scramble)
    cr = find_crossings(tg, atoms, T)
    cr["name"] = name
    cr["X"] = X
    cr["T"] = T
    cr["scramble"] = scramble
    cr["atoms"] = atoms
    cr["build_s"] = time.time() - t0
    return cr


def cell_observables(cell: dict, arch: dict, targets: dict) -> None:
    """fills cell['obs'][z] for both variants; uses arch as bias reference"""
    obs = {}
    for z in Z_GRID:
        tgt = targets[z]["target"]
        pr_full = targets[z]["prime"]
        F_raw = F_completed(cell["roots"], z, cell["t_cut"], cell["atoms"])
        F_lp = F_completed(cell["roots_lp"], z, cell["t_cut"], cell["atoms"])
        Fa_raw = arch["F"][z]
        Fa_lp = arch["F_lp"][z]
        pr_X = primetarget_trunc(z, cell["atoms"])
        o = {
            "F_raw": F_raw, "F_lp": F_lp,
            "resp_lp": F_lp - Fa_lp,
            "abs_raw": F_raw - tgt, "abs_lp": F_lp - tgt,
            "diff_raw": (F_raw - Fa_raw) - pr_full,
            "diff_lp": (F_lp - Fa_lp) - pr_full,
            "diffX_raw": (F_raw - Fa_raw) - pr_X,
            "diffX_lp": (F_lp - Fa_lp) - pr_X,
        }
        # Herglotz (window only, uniform unit vector in the eigenbasis)
        Kw = K_of(cell["roots_lp"], z)
        Fw = complex(np.sum(Kw))
        dim = 2 * len(cell["roots_lp"])
        o["ImFw"] = Fw.imag
        o["herg"] = abs(Fw / dim) * z.imag if dim else 0.0
        obs[z] = o
    cell["obs"] = obs


def lin_model(cell: dict, arch: dict, z: complex) -> complex:
    """exact first-order crossing-displacement model on arch crossings"""
    tr = arch["roots"]
    phis = cell.get("_phi_at_arch")
    if phis is None:
        phis = phi_of(tr, cell["atoms"])
        cell["_phi_at_arch"] = phis
    dth = arch.get("_dtheta_at_arch")
    if dth is None:
        dth = np.where(tr >= THETA_ASY_MIN, dtheta_asy(tr),
                       np.array([dtheta_point(float(x)) for x in tr]))
        arch["_dtheta_at_arch"] = dth
    tc = tr.astype(np.complex128)
    Kp = -4.0 * z * tc / (tc * tc - z * z) ** 2
    return complex(-np.sum(Kp * phis / dth))


# ----------------------------------------------------------------------
# verdict helpers
# ----------------------------------------------------------------------
def row_type(errs: list, nf: float) -> tuple[str, float, bool]:
    """frozen row rule on a gate ladder; returns (enum, slope, flat)"""
    e = np.array([float(x) for x in errs], dtype=np.float64)
    x = np.array(X_LADDER, dtype=np.float64)
    live = e > 10 * nf
    slope = float("nan")
    if live.sum() >= 3:
        slope = float(np.polyfit(np.log(x[live]), np.log(e[live]), 1)[0])
    diverges = e[-1] > 2.0 * e[0]
    # FLAT (A2): last rung not below previous/1.15 and still above 10 NF
    flat = bool(len(e) >= 2 and e[-1] > e[-2] / 1.15 and e[-1] > 10 * nf)
    steps_ok = 0
    steps_tot = 0
    for i in range(len(e) - 1):
        if e[i] <= 10 * nf and e[i + 1] <= 10 * nf:
            steps_ok += 1        # saturated-pass
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


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
def main() -> int:
    global T_MAIN, X_LADDER, SCR_X, T_LADDER, GRID_STEP
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke
    if smoke:
        T_MAIN = 3000.0
        X_LADDER = (8, 50)
        SCR_X = (50,)
        T_LADDER = (1500.0,)
        GRID_STEP = 0.02

    print("=" * 78)
    print("xi_realrooted_limit_probe  PRIME.XI.REALROOTED.LIMIT.01  (CCCXLIII)")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
                                    "   *** SMOKE (not verdict-bearing) ***"
                                    if smoke else ""))
    print("=" * 78)

    self_tests()
    hard_fail = [c for c in CHECKS if not c[1]]
    if hard_fail:
        print("INSTRUMENT-FAIL: aborting before any verdict.")
        return 1

    # targets
    targets = {}
    for z in Z_GRID:
        tgt, pr = target_parts(z)
        targets[z] = {"target": tgt, "prime": pr}
    print("\nII. TARGETS (safe domain, dps=%d)" % DPS_TARGET)
    for z in GATE_Z:
        t_ = targets[z]
        print("  z=%5.2f+%.2fi  -Xi'/Xi = %+.12e %+.12e i   prime part |.|=%.6e"
              % (z.real, z.imag, t_["target"].real, t_["target"].imag,
                 abs(t_["prime"])))

    # master theta grid
    t0 = time.time()
    tg = ThetaGrid(T_MAIN)
    print("\nIII. CELL BUILDS  (master grid %d pts, %.1f s)"
          % (len(tg.t), time.time() - t0))

    cells: dict[str, dict] = {}

    def register(name, X, T, scr):
        c = build_cell(name, X, T, scr, tg)
        cells[name] = c
        print("  %-14s X=%5d T=%7.0f raw=%6d lp=%6d excess=%4d rec=%2d "
              "parity=%s edgePhi=%+.3f  %.1f s"
              % (name, X, T, c["n_raw"], c["n_lp"], c["excess"],
                 c["recovered"], "OK" if c["parity_ok"] else "VIOL",
                 c["edge_phase"], c["build_s"]))
        return c

    arch = register("ARCH", 0, T_MAIN, False)
    # cache arch completed F per z
    arch["F"] = {z: F_completed(arch["roots"], z, arch["t_cut"],
                                arch["atoms"]) for z in Z_GRID}
    arch["F_lp"] = {z: F_completed(arch["roots_lp"], z, arch["t_cut"],
                                   arch["atoms"]) for z in Z_GRID}

    for X in X_LADDER:
        register("MAIN-X%d" % X, X, T_MAIN, False)
    for T in T_LADDER:
        register("TLAD-T%d" % int(T), 120 if not smoke else X_LADDER[-1],
                 T, False)
    for X in SCR_X:
        register("SCR-X%d" % X, X, T_MAIN, True)

    parity_all = all(c["parity_ok"] for c in cells.values())
    check("A8 census parity all cells", parity_all,
          "%d cells" % len(cells))

    # scramble sanity
    if SCR_X:
        sc = cells["SCR-X%d" % SCR_X[-1]]["atoms"]
        mn = build_atoms(SCR_X[-1], False)
        dev = float(np.max(np.abs(sc["u"] - mn["u"]))) if sc["count"] else 0.0
        check("A12 scramble displaces comb", dev >= 0.1,
              "max|u_scr-u| = %.3f" % dev)

    # observables
    print("\nIV. OBSERVABLES")
    for name, c in cells.items():
        if name == "ARCH":
            c["obs"] = None
            continue
        cell_observables(c, arch, targets)

    # arch absolute defect (lattice bias reference)
    print("  ARCH cell absolute defect (lattice bias B(z), LASTPASS):")
    for z in GATE_Z:
        b = arch["F_lp"][z] - targets[z]["target"] + targets[z]["prime"]
        print("    z=%4.2fi  B = %+.6e %+.6e i   |B| = %.6e"
              % (z.imag, b.real, b.imag, abs(b)))

    # noise floor from T ladder
    nf = NF_FLOOR
    if T_LADDER:
        xa = "MAIN-X120" if "MAIN-X120" in cells else \
            "MAIN-X%d" % X_LADDER[-1]
        ref = cells[xa]
        devs = []
        for T in T_LADDER:
            ct = cells["TLAD-T%d" % int(T)]
            for z in GATE_Z:
                devs.append(abs(ct["obs"][z]["F_lp"] - ref["obs"][z]["F_lp"]))
        # frozen: NF from the largest T rung only (T=2e4 vs 3e4)
        n_gate = len(GATE_Z)
        nf = max(NF_FLOOR, max(devs[-n_gate:]))
        print("  T-ladder saturation vs T=%d:" % int(T_MAIN))
        for i, T in enumerate(T_LADDER):
            block = devs[i * n_gate:(i + 1) * n_gate]
            print("    T=%6d  max gate dev %.3e" % (int(T), max(block)))
    print("  DECLARED NOISE FLOOR NF = %.3e" % nf)

    # gate tables (A2: ABS is the gate observable)
    print("\nV. LADDERS (|Delta| at gate points, LASTPASS variant)")
    hdr = "  %-10s" + "".join("  X=%-8d" % X for X in X_LADDER)
    for tag, key in (("ABS  [GATE]", "abs_lp"), ("DIFF [diag]", "diff_lp"),
                     ("DIFFX[diag]", "diffX_lp")):
        print("  -- %s --" % tag)
        print(hdr % "row")
        for z in GATE_Z:
            vals = [abs(cells["MAIN-X%d" % X]["obs"][z][key])
                    for X in X_LADDER]
            print(("  y=%-8.2f" % z.imag)
                  + "".join("  %.3e" % v for v in vals))
    print("  -- ABS (RAW variant, pair-production meter) --")
    print(hdr % "row")
    for z in GATE_Z:
        vals = [abs(cells["MAIN-X%d" % X]["obs"][z]["abs_raw"])
                for X in X_LADDER]
        print(("  y=%-8.2f" % z.imag) + "".join("  %.3e" % v for v in vals))
    print("  RAW excess census per MAIN cell: "
          + ", ".join("X%d:%d" % (X, cells["MAIN-X%d" % X]["excess"])
                      for X in X_LADDER))

    # non-gate rows summary (x offsets & y=0.75, 4.0)
    print("  -- X = %d at non-gate points --" % X_LADDER[-1])
    cbig = cells["MAIN-X%d" % X_LADDER[-1]]
    for z in Z_GRID:
        if z in GATE_Z:
            continue
        print("    z=%5.2f%+.2fi  |ABS| = %.3e   |DIFF| = %.3e"
              % (z.real, z.imag, abs(cbig["obs"][z]["abs_lp"]),
                 abs(cbig["obs"][z]["diff_lp"])))

    # attenuation / linear model diagnostic (complex values printed)
    print("\nVI. PRIME-RESPONSE DIAGNOSTICS (LASTPASS; attenuation meter)")
    for X in [x for x in X_LADDER if x <= LIN_XMAX]:
        c = cells["MAIN-X%d" % X]
        for z in GATE_Z:
            lm = lin_model(c, arch, z)
            resp = c["obs"][z]["resp_lp"]
            pr = targets[z]["prime"]
            print("  X=%4d z=%4.2fi  resp=%+.4e%+.4ei  LM=%+.4e%+.4ei  "
                  "primetgt=%+.4e%+.4ei"
                  % (X, z.imag, resp.real, resp.imag, lm.real, lm.imag,
                     pr.real, pr.imag))

    # scramble control (A2: on ABS)
    print("\nVII. SCRAMBLE CONTROL (|Delta_abs| LASTPASS)")
    scr_ok_rows = 0
    scr_first = {}
    scr_last = {}
    for z in GATE_Z:
        line = "  y=%-6.2f" % z.imag
        for X in SCR_X:
            e = abs(cells["SCR-X%d" % X]["obs"][z]["abs_lp"])
            line += "  X%d: %.3e" % (X, e)
            if X == SCR_X[0]:
                scr_first[z] = e
            if X == SCR_X[-1]:
                scr_last[z] = e
        em = abs(cells["MAIN-X%d" % X_LADDER[-1]]["obs"][z]["abs_lp"])
        ratio = scr_last[z] / max(em, 1e-300)
        line += "   main X%d: %.3e   ratio %.1f" % (X_LADDER[-1], em, ratio)
        if ratio >= SCR_RATIO_BAR:
            scr_ok_rows += 1
        print(line)
    scr_self = all(scr_last[z] >= scr_first[z] / SCR_SELF_BAR
                   for z in GATE_Z)
    scr_nonvacuous = (scr_ok_rows >= 2) and scr_self
    # A3: verdict gate, reported (not an instrument assertion)
    print("  [GATE] scramble non-vacuity: %s  (%d/3 ratio rows, self %s)"
          % ("HELD" if scr_nonvacuous else "FAILED -> VACUOUS",
             scr_ok_rows, scr_self))

    # A3: origin-cluster diagnostic
    print("\nVII-b. ORIGIN-CLUSTER DIAGNOSTIC (5 lowest crossings, "
          "K-weight at z = i)")
    for name in (["MAIN-X%d" % X for X in X_LADDER]
                 + ["SCR-X%d" % X for X in SCR_X]):
        c = cells[name]
        low5 = c["roots_lp"][:5]
        kw = K_of(low5, 1j)
        print("  %-12s edgePhi=%+8.3f%s  low t: %s"
              % (name, c["edge_phase"],
                 "  [SUB-GRID CROSSINGS EXIST BELOW t=%.2f, NOT COLLECTED;"
                 " would strengthen divergence]" % GRID0
                 if c["edge_phase"] < -math.pi else "",
                 "  ".join("%.3f(|K|=%.2f)" % (t_, abs(k_))
                           for t_, k_ in zip(low5, kw))))

    # normalization: path-integral log P vs log Xi
    print("\nVIII. NORMALIZATION (path-integral log P, fit b,c; z0 = %s)"
          % Z0)
    # cross-check on one cell
    ccell = cells["MAIN-X%d" % X_LADDER[min(3, len(X_LADDER) - 1)]]
    worst = 0.0
    for z in Z_GRID[:3]:
        d1 = path_logdet_delta_window(ccell["roots_lp"], z, Z0)
        d2 = direct_logdet_delta_window(ccell["roots_lp"], z, Z0)
        worst = max(worst, abs(d1 - d2))
    check("A9 path-integral vs direct", worst <= 1e-9,
          "worst dev %.3e" % worst)

    lxi = {z: log_xi(z) for z in Z_GRID}
    lxi0 = log_xi(complex(Z0))
    A = np.array([[z - Z0, z * z - Z0 * Z0] for z in Z_GRID],
                 dtype=np.complex128)
    bc_prev = None
    for X in X_LADDER:
        c = cells["MAIN-X%d" % X]
        r = np.array([(lxi[z] - lxi0)
                      - path_logdet_delta(c["roots_lp"], c["t_cut"],
                                          c["atoms"], z, Z0)
                      for z in Z_GRID], dtype=np.complex128)
        sol, *_ = np.linalg.lstsq(A, r, rcond=None)
        res = r - A @ sol
        rms = float(np.sqrt(np.mean(np.abs(res) ** 2)))
        drift = ("" if bc_prev is None else
                 "  drift |db|=%.2e |dc|=%.2e"
                 % (abs(sol[0] - bc_prev[0]), abs(sol[1] - bc_prev[1])))
        print("  X=%5d  b=%+.6e%+.6ei  c=%+.6e%+.6ei  rms_res=%.3e%s"
              % (X, sol[0].real, sol[0].imag, sol[1].real, sol[1].imag,
                 rms, drift))
        bc_prev = sol
        c["bc"] = (complex(sol[0]), complex(sol[1]), rms)

    # Herglotz
    print("\nIX. HERGLOTZ BOUNDS")
    herg_ok = True
    worst_h = 0.0
    for name, c in cells.items():
        if c.get("obs") is None:
            continue
        for z in Z_GRID:
            o = c["obs"][z]
            if o["ImFw"] <= 0:
                herg_ok = False
            worst_h = max(worst_h, o["herg"])
    check("A7 Herglotz (Im F>0, y|m|<=1)", herg_ok and worst_h <= 1 + 1e-12,
          "max y|m_N| = %.6f" % worst_h)

    # rate fits + verdict (A2: gate observable = ABS, LASTPASS)
    print("\nX. RATE FITS AND VERDICT (gate rows, LASTPASS ABS)")
    row_results = {}
    for z in GATE_Z:
        errs = [abs(cells["MAIN-X%d" % X]["obs"][z]["abs_lp"])
                for X in X_LADDER]
        typ, slope, flat = row_type(errs, nf)
        row_results[z] = (typ, slope, flat, errs[-1])
        print("  y=%-5.2f  %s  slope=%.3f  flat=%s  final=%.3e"
              % (z.imag, typ, slope, flat, errs[-1]))

    conv_rows = [z for z in GATE_Z if row_results[z][0] == "ROW-CONVERGES"]
    div_rows = [z for z in GATE_Z if row_results[z][0] == "ROW-DIVERGES"]
    flat_rows = [z for z in GATE_Z if row_results[z][2]]
    abs_small = all(row_results[z][3] <= 10 * nf for z in GATE_Z)
    # residual X-stability (identification quality of a stable defect field)
    stab = []
    for z in GATE_Z:
        e_last = row_results[z][3]
        e_prev = abs(cells["MAIN-X%d" % X_LADDER[-2]]["obs"][z]["abs_lp"])
        stab.append(abs(e_last - e_prev) / max(e_last, 1e-300))
    ident_ok = all(q <= 0.3 for q in stab)

    slopes = ",".join("%.2f" % row_results[z][1] for z in GATE_Z)
    if not scr_nonvacuous:
        verdict = "XILIMIT-VACUOUS"
    elif len(div_rows) >= 2:
        verdict = "XILIMIT-DIVERGES"
    elif len(conv_rows) == len(GATE_Z) and abs_small:
        verdict = ("XILIMIT-CONVERGES(slopes %s; safe domain y>=1, X<=%d)"
                   % (slopes, X_LADDER[-1]))
    elif flat_rows and not div_rows:
        verdict = ("XILIMIT-WRONGLIMIT(ABS saturates at an X-stable "
                   "residual field%s; finals %s; slopes %s)"
                   % (" [X-stability <=30%% at all gate rows]" if ident_ok
                      else " [residual not yet X-stable]",
                      ",".join("%.2e" % row_results[z][3] for z in GATE_Z),
                      slopes))
    elif len(conv_rows) == len(GATE_Z):
        verdict = ("XILIMIT-CONVERGES(descending, unsaturated: finals %s "
                   "> 10 NF; slopes %s)"
                   % (",".join("%.2e" % row_results[z][3] for z in GATE_Z),
                      slopes))
    else:
        parts = ",".join("y%.1f:%s" % (z.imag, row_results[z][0])
                         for z in GATE_Z)
        verdict = "XILIMIT-MIXED(%s)" % parts

    wall = time.time() - T0_WALL
    check("A11 runtime", wall <= RUNTIME_BAR, "%.1f s" % wall)

    n_pass = sum(1 for c in CHECKS if c[1])
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s" % verdict)
    if smoke:
        print("*** SMOKE RUN — NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
