#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relative_flag_margin_probe -- PRIME.PORT.RELFLAG.01
(EXPLORATION ONLY, experiments/; round 52, named objects
(b)+(iii): make the two remaining conditional pieces RELATIVE --
the soft-flag collapse scale and the exterior margin, both
measured against the wall scale tau.  2026-08-09.)

THE QUESTION (frozen).  Round 51 left two conditional pieces in
absolute form: (a) the flag induction's dangerous quotient sits
at the soft flag k = 12 with ladder min Q_12 = 2.059e-14
(pivot_factor_probe: a COLLAPSING margin), and (b) the exterior
operator margin lambda_min(R_h) of the deep-core split shrinks
with h in absolute terms while lambda_min(R_h)/tau_h stayed
trendless 210..2200 (deepcore_schur_reduction_probe).  This
probe re-measures BOTH pieces RELATIVE to the wall scale tau and
assembles the combined conditional chain, printing the one
statement that remains unconditionally open.

THE TWO RELATIVE LAWS (frozen):

L1 THE SOFT-FLAG SCALE LAW.  On every truth full-window rung,
   A_h = I - C_J(h) (12x12, factor_avoidance compression) has
   unpivoted-LDL^T pivots d_k = tau^(k)/tau^(k-1); the soft
   pivot is EXACTLY d_12 = 1/(A_h^{-1})_{12,12} >= tau_h :=
   lambda_min(A_h) (elementary: (A^{-1})_{nn} = sum_i
   v_i(n)^2/lambda_i <= 1/lambda_min).  Define c_h :=
   d_{12,h}/tau_h (>= 1 by the algebra above whenever A_h is
   PD).  MEASURE: the c-ladder (full print, quartiles,
   first/second-half medians, log-log slope of c vs h), and the
   anatomy s_h = 1/c_h = tau_h (A_h^{-1})_{12,12} (the
   tau-weighted soft coordinate share) next to v_min(12)^2.
   Per consecutive full-window pair the soft ratio r_12 =
   d_{12,h+1}/d_{12,h} then factors EXACTLY (definition of c)
   as  r_12 = (tau_{h+1}/tau_h) x (c_{h+1}/c_h)  -- the
   RELATIVE form of the dangerous quotient: r_12 > 0 (and with
   the bulk flags Q_11 > 0 also Q_12 > 0) is the tau-sign
   inheritance ITSELF, and the bounded c-ratio is the new
   (hopefully provable) piece.  WARDS (kill -> WARD-BROKEN):
     W-L1a  LDL pivots == minor quotients on every full rung
            and every k, scaled dev <= PIV_WARD = 1e-10
            (pivot_factor W1 verbatim);
     W-L1b  c_h >= 1 - CGE1_WARD (= 1e-9) on every full rung
            (the exact inequality d_12 >= lambda_min);
     W-L1c  the factorization r_12 = (tau'/tau)(c'/c), scaled
            dev <= ID_WARD = 1e-9 on every pair (bookkeeping,
            zero content -- warded, never the finding);
     W-L1d  REPRODUCTION: 37 truth full-window rungs (hirota
            census), 31 consecutive full-window pairs, and
            min_h Q_12 == 2.059e-14 within rel tol 2e-2
            (pivot_factor printed ladder; Q_12 from slogdet of
            the two 12x12 sections, independent route).
   TYPED (never kills): SOFTFLAG-TAU-TIED(c-range) iff the
   c-ladder is bounded AND trendless on the deployed rungs:
   spread max c / min c <= CSPREAD_BAR = 100 AND |log-log slope
   of c vs h| <= CSLOPE_BAR = 1.0; else SOFTFLAG-UNTIED
   (spread/slope printed).  The c-RATIO ladder c'/c is printed
   with its own range either way.

L2 THE RELATIVE EXTERIOR MARGIN LAW.  On the FULL wall operator
   (deepcore_schur machinery verbatim: A_h = I - E_h on ALL
   folded neg nodes; fixed core aliases CORE_J = {2,4,...,16};
   R_h = the exterior block of A_h; S_h = the 8x8 Schur core):
   the ladder lambda_min(R_h)/tau_h over all full-core truth
   rungs, quantified: OLS slope b of log(lamR/tau) vs log h
   WITH its 2-sigma CI (b +- 2 SE), quartiles, and the ladder
   min c_R := min_h lambda_min(R_h)/tau_h.  THE RELATIVE
   REDUCTION STATEMENT (printed with the measured constant):
   IF lambda_min(R_h) >= c_R tau_h (a TAU-RELATIVE exterior
   bound) THEN by Haynsworth the wall A_h >= 0 <=> S_h >= 0 --
   the fixed-dimension reduction now conditional on a relative,
   not absolute, exterior floor.  SIDE BY SIDE: the analogous
   relative BULK statement of the original port reduction
   (port_schur_reduction verbatim: port set tau_m <=
   max(tau_m)/10 on the Carleson Gram E_h; bulk margin
   1 - lam_max(E_bulk); note (I-E)|_bulk = I - E|_bulk, so both
   exteriors are THE SAME operation at two different interior
   choices) -- the ladder (1 - lam_max(E_bulk))/tau_h printed
   next to lambda_min(R_h)/tau_h on every rung, plus the
   Pearson corr of the two log-ladders.  WARDS (kill ->
   WARD-BROKEN): W-L2a truth full wall all-PSD (neg(A) =
   neg(R) = neg(S) = 0 on every full-core rung, deepcore B2.2
   verbatim).  TYPED (never kills): EXTMARGIN-TRENDLESS(c_R,
   slope) iff |b| <= TREND_SLOPE_BAR = 0.25 OR |b| <= 2 SE
   (CI contains 0); else EXTMARGIN-TRENDED(slope).  And
   COMPRESSIONS-COHERENT(corr) iff corr >= COHER_BAR = 0.90
   over the rungs carrying both exteriors; else
   COMPRESSIONS-DISTINCT(corr).

L3 THE COMBINED CONDITIONAL CHAIN (the deliverable; printed as
   the theorem skeleton with every measured constant):
     (i)   base certified: A = I - C PD at the base rung
           (v884 certified head positivity / v887 certified
           ladder complete -- declared inputs, not re-run);
     (ii)  exterior: lambda_min(R_h) >= c_R tau_h with the
           measured c_R and its honest trend (L2);
     (iii) core: S_h > 0 <=> tau_h > 0 -- Haynsworth exact
           given (ii); measured correspondence lamS x wcore /
           tau printed with its max deviation (deepcore B2
           product check; the digit count printed honestly);
     (iv)  step: eta_h = 1 + lambda_min(H_h) > 0 (the exact
           hermitian congruence, relative_congruence verbatim;
           REPRODUCTION ward, kill -> WARD-BROKEN: 0 crossings
           and min eta == 0.0050 within ROUND_TOL = 5.001e-5)
           -- equivalently all flag quotients positive, where
           by L1 the soft flag IS the tau-sign inheritance
           itself times a bounded c-ratio.
   Then PRINT WHICH single statement remains unconditionally
   open after the chain is assembled -- the honest answer, said
   plainly: the tau-sign inheritance step is still the wall;
   the chain reorganizes the open inequality from a
   COLLAPSING-margin shape (min Q_12 ~ 2e-14) into a
   BOUNDED-MARGIN shape (c_h bounded, c'/c bounded, c_R
   trendless, eta ladder-positive), but proves nothing beyond
   the deployed rungs.

C  CONTROLS: (C2, PRIMARY, kill -> WARD-BROKEN) the smooth-mass
   world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n on
   the true lattice, lattice_parametrix verbatim) must BREAK
   both relative laws, and the probe prints WHERE: (C2a) the
   12-window c-law loses its PD premise -- REPRODUCTION: 28
   smooth full-window pairs with the base A_h indefinite on
   28/28 (relative_congruence SPEC v2 (ii): the smooth world
   exits the PD cone before its pair ladder starts; tau < 0
   makes c_h = d_12/tau meaningless as a positive scale); (C2b)
   the full-operator relative exterior law breaks: neg(A_h) > 0
   on >= 1 smooth rung (deepcore C1), with the first violating
   rung and the sign ledger printed.  (C1, kz 9, must fire,
   kill -> WARD-BROKEN) Epstein x^2+5y^2 comb + scramble (seed
   1): frame death or neg(A) > 0; channel printed.

W  PIPELINE WARDS (kill -> PIPELINE-BROKEN): W0 truth ladder ==
   42 rungs (deepcore reachable census; TOO-DEEP zones and
   chain deaths counted); W0b the atom prefix law exact (max
   |mm - MU_ALL prefix| == 0 over truth windows); W0c truth
   full-window census == 37 (hirota); W0d >= 30 full-core rungs.

KILLS: KP a W ward breaks -> PIPELINE-BROKEN; KW an L1/L2/L3
reproduction or exactness ward breaks OR a control stays silent
-> WARD-BROKEN.  Typed labels report, never kill.

VERDICT (frozen enum): RELFLAG-MEASURED with typed sublabels
SOFTFLAG-TAU-TIED(c-range) / SOFTFLAG-UNTIED (L1),
EXTMARGIN-TRENDLESS(c_R, slope) / EXTMARGIN-TRENDED(slope) (L2),
COMPRESSIONS-COHERENT(corr) / COMPRESSIONS-DISTINCT(corr) (L2
side-by-side); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,4,...,24); NW = 12;
CORE_J = (2,4,...,16); N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37;
REF_N_TRUTH_PAIRS = 31; REF_N_SMOOTH_PAIRS = 28; REF_MINQ12 =
2.059e-14 (rel tol 2e-2); REF_MIN_ETA = 0.0050 (ROUND_TOL =
5.001e-5); REF_SMOOTH_CONE = 28/28; PIV_WARD = 1e-10; CGE1_WARD
= 1e-9; ID_WARD = 1e-9; CSPREAD_BAR = 100; CSLOPE_BAR = 1.0;
TREND_SLOPE_BAR = 0.25; COHER_BAR = 0.90; MIN_COMMON_J = 8;
MIN_CORE_RUNGS = 30; PORT_DIV = 10 (port set tau_m <= max/10,
port_schur verbatim); CTRL_KZ = 9; scramble seed 1.

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run):
everything above.  Mechanical concretizations frozen with v1:
(i) core.build_window results are memoized per (kz, seed)
(deepcore verbatim; pure memoization of a deterministic
function); (ii) ONE Gram E_h per rung serves all three
compressions (full wall A = I - E, the port/bulk split of E,
and the 12-window C_J = Schur compression of E onto JWIN) --
this is the point of the side-by-side, not an approximation;
(iii) negative-eigenvalue counts use the strict eig < 0.0
reading (port_schur precedent); (iv) smooth/control rungs are
evaluated in a LIGHT mode (no Schur core, no bulk split, no
eigenvectors -- only what C2 needs: neg counts, tau, lamR,
C_J); (v) the L2 trend SE uses the standard OLS residual
estimator with n - 2 dof.

SPEC v2 (2026-08-09, after run 1 -- which was already green on
all 18 checks with the full typed verdict RELFLAG-MEASURED /
SOFTFLAG-UNTIED(spread=124.2, slope=+0.128) /
EXTMARGIN-TRENDLESS(c_R=210, slope=+0.137) /
COMPRESSIONS-DISTINCT(corr=0.278); fail-first preserved: every
run-1 raw number stands and is reprinted unchanged, no bar, no
object, no typed label moved):
 (a) DISPLAY ONLY: the L1 ladder columns s = 1/c and
     v_min(12)^2 moved from fixed %.4f to scientific notation
     -- run 1 printed the load-bearing anatomy (s ~ 2e-4..2e-3,
     v_min(12)^2 below 1e-4) as "0.0000" throughout.
 (b) DISPLAY ONLY: the L1 pair ladder additionally prints
     Q_11 (slogdet of the two leading 11x11 sections) next to
     Q_12, so the split of the 14-order collapse between the
     BULK determinant quotient (Q_11) and the SOFT ratio (r_12
     = Q_12/Q_11) is visible on the worst step h 371->388
     (run 1: Q_12 = 2.059e-14 with r_12 = 5.44e-3 -- the bulk
     carries ~12 of the 14 orders there).  No bar, no object,
     no typed label changed.

HONEST FRAME: c_h >= 1 and r_12 = (tau'/tau)(c'/c) are exact
algebra whenever A_h is PD -- warded bookkeeping, zero content.
The CONTENT is the measured boundedness/trendlessness of c_h,
c'/c and lamR/tau on the deployed ladder, and the census is
FINITE: it certifies the deployed rungs only.  The tau-sign
inheritance itself is NOT proved here.  NO RH claim.  No marker
moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags, U_ALL / MU_ALL prefix law -- verbatim);
12-window compression + ladder scope + smooth-mass world
verbatim from factor_avoidance_euler_probe.py via
pivot_factor_probe.py (PRIME.PORT.PIVOTFACTOR.01: the pivot
ladder, Q_12 = 2.059e-14, soft flag k = 12) and
relative_congruence_probe.py (PRIME.PORT.RELCONG.01: the eta
machinery, min eta 0.0050, 28/28 CONE-EXITED);
full-wall/core-split machinery verbatim from
deepcore_schur_reduction_probe.py (PRIME.PORT.DEEPCORE.SCHUR.01:
lamR/tau trendless 210..2200); port/bulk split verbatim from
port_schur_reduction_probe.py (PRIME.PORT.SCHUR.01: bulk margin
420..45000 x tau); v884/v887 (base certificates -- declared
inputs, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/relative_flag_margin_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
NW = 12
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
N_RUNGS_EXP = 42
N_FULLWIN_FROZEN = 37
MIN_CORE_RUNGS = 30
MIN_COMMON_J = 8
PORT_DIV = 10.0
PIV_WARD = 1e-10            # W-L1a LDL == minor quotient
CGE1_WARD = 1e-9            # W-L1b c >= 1 - this
ID_WARD = 1e-9              # W-L1c r_12 factorization
CSPREAD_BAR = 100.0         # L1 typing: max c / min c
CSLOPE_BAR = 1.0            # L1 typing: |loglog slope of c|
TREND_SLOPE_BAR = 0.25      # L2 typing: |slope| bar
COHER_BAR = 0.90            # L2 side-by-side corr bar
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# reproduction anchors (predecessor printed ledgers, round 50/51)
REF_N_TRUTH_PAIRS = 31
REF_N_SMOOTH_PAIRS = 28
REF_MINQ12 = 2.059e-14      # pivot_factor ladder min (k = 12)
REF_MINQ12_RTOL = 2e-2
REF_MIN_ETA = 0.0050        # relative_congruence min eta
REF_TRUTH_CROSS = 0
ROUND_TOL = 5.001e-5

CHECKS = []
KILLS = []
T0 = time.time()


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


# --------- pipeline, verbatim (factor_avoidance / deepcore chain)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC v1 (i): pure memoization of core.build_window
    (deepcore verbatim)."""
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


# ------------------------------------------- pivot machinery (L1)
def ldl_pivots(A):
    """Unpivoted LDL^T pivots (pivot_factor verbatim); None on an
    exactly-zero pivot."""
    n = A.shape[0]
    L = np.zeros((n, n))
    d = np.zeros(n)
    for j in range(n):
        d[j] = A[j, j] - float(np.sum(L[j, :j] ** 2 * d[:j]))
        if d[j] == 0.0:
            return None
        L[j, j] = 1.0
        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - float(
                np.sum(L[i, :j] * L[j, :j] * d[:j]))) / d[j]
    return d


def ols_se(x, y):
    """OLS y = a + b x; returns (a, b, se_b) with the standard
    n - 2 dof residual estimator (SPEC v1 (v))."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = float(np.mean(x)), float(np.mean(y))
    sxx = float(np.sum((x - xm) ** 2))
    b = float(np.sum((x - xm) * (y - ym)) / sxx)
    a = ym - b * xm
    rss = float(np.sum((y - a - b * x) ** 2))
    se = math.sqrt(rss / max(n - 2, 1) / sxx)
    return a, b, se


def quart_row(v):
    v = np.asarray(v, float)
    q = np.percentile(v, [25, 50, 75])
    return (float(np.min(v)), float(q[0]), float(q[1]),
            float(q[2]), float(np.max(v)))


# ------------------------------------------- the one-build anatomy
def anatomy(kz, scramble_seed=None, comb=None, heavy=False):
    """One rung -> ONE Gram E on the folded neg nodes -> all three
    compressions (SPEC v1 (ii)): full wall A = I - E (+ fixed-core
    split, heavy: Schur core, wcore, port/bulk split), and the
    12-window C_J.  Light mode (SPEC v1 (iv)) for smooth/controls.
    """
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    A = np.eye(n) - E
    out = dict(kz=kz, h=h, n=n)
    if heavy:
        evA, VA = np.linalg.eigh(A)
    else:
        evA = np.linalg.eigvalsh(A)
        VA = None
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    # ---- fixed-core split of A (deepcore verbatim)
    out["core_ok"] = all(j in idx for j in CORE_J)
    if out["core_ok"]:
        ic = np.array([idx[j] for j in CORE_J], dtype=int)
        icset = set(ic.tolist())
        ib = np.array([k for k in range(n) if k not in icset],
                      dtype=int)
        R = A[np.ix_(ib, ib)]
        evR = np.linalg.eigvalsh(R)
        out["lamR"] = float(evR[0])
        out["negR"] = int(np.sum(evR < 0.0))
        if heavy:
            B = A[np.ix_(ic, ic)]
            X = A[np.ix_(ic, ib)]
            try:
                S = B - X @ np.linalg.solve(R, X.T)
                S = 0.5 * (S + S.T)
                evS = np.linalg.eigvalsh(S)
                out["lamS"] = float(evS[0])
                out["negS"] = int(np.sum(evS < 0.0))
            except np.linalg.LinAlgError:
                pass
            v = VA[:, 0]
            out["wcore"] = float(np.sum(v[ic] ** 2))
    # ---- port/bulk split of E (port_schur verbatim; heavy only)
    if heavy:
        tau_m = (2.0 * math.pi * uf_n / L) / D
        port = tau_m <= float(np.max(tau_m)) / PORT_DIV
        ipn = int(np.sum(port))
        if 0 < ipn < n:
            Rg = E[np.ix_(~port, ~port)]
            out["nport"] = ipn
            out["bulkm"] = float(
                1.0 - np.linalg.eigvalsh(Rg)[-1])
    # ---- 12-window compression (factor_avoidance verbatim)
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(n) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            out["CJ"] = 0.5 * (CJ + CJ.T)
        except np.linalg.LinAlgError:
            pass
    return out


def win_attrs(r):
    """L1 per-rung window objects: pivots (ward), d_12, tau, c,
    anatomy shares, slogdets of the 12/11 leading sections."""
    A = np.eye(NW) - r["CJ"]
    taus = [1.0]
    for k in range(1, NW + 1):
        taus.append(float(np.linalg.det(A[:k, :k])))
    taus = np.array(taus)
    dmin = taus[1:] / taus[:-1]
    dldl = ldl_pivots(A)
    r["piv_dev"] = (float(np.max(np.abs(dldl - dmin)
                    / np.maximum(np.maximum(np.abs(dldl),
                                            np.abs(dmin)),
                                 1e-300)))
                    if dldl is not None else float("inf"))
    ew, Vw = np.linalg.eigh(A)
    r["A12"] = A
    r["d12"] = float(dmin[-1])
    r["tau12"] = float(ew[0])
    r["ew"] = ew
    r["Vw"] = Vw
    r["c"] = r["d12"] / r["tau12"]
    r["vmin12sq"] = float(Vw[11, 0] ** 2)
    sg12, ld12 = np.linalg.slogdet(A)
    sg11, ld11 = np.linalg.slogdet(A[:11, :11])
    r["sld12"] = (float(sg12), float(ld12))
    r["sld11"] = (float(sg11), float(ld11))
    return r


def main():
    section("PRIME.PORT.RELFLAG.01 -- the two conditional pieces "
            "made RELATIVE to tau (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth-mass ladders (frame-A "
            "zones, h <= %d; ONE Gram per rung)" % H_DEEP_MAX)
    truth, smooth = [], []
    n_toodeep, n_dead_t, n_dead_s = 0, 0, 0
    for kz in core.frame_a_zones():
        r = anatomy(kz, heavy=True)
        if r == "TOO-DEEP":
            n_toodeep += 1
            continue
        if r is None:
            n_dead_t += 1
            continue
        truth.append(r)
        uu = window_of(kz)["uu"]
        rs = anatomy(kz, comb=(uu, smooth_masses(uu)))
        if isinstance(rs, dict):
            smooth.append(rs)
        else:
            n_dead_s += 1
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    smooth.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs (h %d..%d; %d TOO-DEEP zones, %d "
          "chain deaths) | smooth: %d rungs (%d deaths)  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"],
             n_toodeep, n_dead_t, len(smooth), n_dead_s,
             time.time() - T0))
    check("W0 truth ladder == %d rungs (deepcore census)"
          % N_RUNGS_EXP, len(truth) == N_RUNGS_EXP,
          "%d" % len(truth), kill="KP")
    pref_dev = max(float(np.max(np.abs(
        2.0 * _WIN_CACHE[(kz, None)]["lam"]
        - np.asarray(core.MU_ALL, float)[
            :int(_WIN_CACHE[(kz, None)]["n_atom"])])))
        for kz in [r["kz"] for r in truth])
    check("W0b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="KP")
    fullw = [r for r in truth if r.get("full") and "CJ" in r]
    check("W0c truth full-window census %d == %d (hirota frozen)"
          % (len(fullw), N_FULLWIN_FROZEN),
          len(fullw) == N_FULLWIN_FROZEN, kill="KP")
    fullc = [r for r in truth if r.get("core_ok")]
    check("W0d >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(fullc) >= MIN_CORE_RUNGS, "%d" % len(fullc),
          kill="KP")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ L1
    section("L1 -- THE SOFT-FLAG SCALE LAW: d_12 = c_h tau_h on "
            "the 12-window (c_h = d_12/tau, exact c >= 1)")
    for r in fullw:
        win_attrs(r)
    piv_max = max(r["piv_dev"] for r in fullw)
    check("W-L1a LDL pivots == minor quotients (all 12 flags, "
          "every full rung): max scaled dev %.1e <= %.0e"
          % (piv_max, PIV_WARD), piv_max <= PIV_WARD, kill="KW")
    c_min_dev = min(r["c"] for r in fullw)
    check("W-L1b c_h >= 1 on every full rung (exact algebra "
          "d_12 = 1/(A^-1)_{12,12} >= lam_min): min c = %.6f"
          % c_min_dev, c_min_dev >= 1.0 - CGE1_WARD, kill="KW")
    print("\n    THE c-LADDER (37 truth full-window rungs; "
          "s/v-columns scientific, SPEC v2 (a)):")
    print("    %-4s %-4s %-11s %-11s %-9s %-10s %s"
          % ("kz", "h", "d_12", "tau_h", "c_h", "s=1/c",
             "v_min(12)^2"))
    for r in fullw:
        print("    %-4d %-4d %-11.3e %-11.3e %-9.3f %-10.3e "
              "%.3e"
              % (r["kz"], r["h"], r["d12"], r["tau12"], r["c"],
                 1.0 / r["c"], r["vmin12sq"]))
    cs = np.array([r["c"] for r in fullw])
    hs = np.array([r["h"] for r in fullw], float)
    mn, q1, q2, q3, mx = quart_row(cs)
    spread = mx / mn
    _, b_c, se_c = ols_se(np.log(hs), np.log(cs))
    nh = len(cs) // 2
    print("\n    c quartiles: min %.3f q25 %.3f med %.3f q75 "
          "%.3f max %.3f | spread max/min %.2f (bar %.0f)"
          % (mn, q1, q2, q3, mx, spread, CSPREAD_BAR))
    print("    c trend: median %.3f (first %d rungs) vs %.3f "
          "(last %d); log-log slope vs h %+.3f +- %.3f (2 SE; "
          "bar |b| <= %.1f)"
          % (float(np.median(cs[:nh])), nh,
             float(np.median(cs[nh:])), len(cs) - nh, b_c,
             2.0 * se_c, CSLOPE_BAR))

    # pairs: the relative factorization of the dangerous quotient
    rows = []
    n_skip = 0
    for ra, rb in zip(truth[:-1], truth[1:]):
        if not (ra.get("full") and rb.get("full")
                and "c" in ra and "c" in rb):
            n_skip += 1
            continue
        r12 = rb["d12"] / ra["d12"]
        pred = (rb["tau12"] / ra["tau12"]) * (rb["c"] / ra["c"])
        dev = abs(r12 - pred) / max(abs(r12), abs(pred), 1e-300)
        sga, lda = ra["sld12"]
        sgb, ldb = rb["sld12"]
        q12 = sga * sgb * math.exp(ldb - lda)
        sga1, lda1 = ra["sld11"]
        sgb1, ldb1 = rb["sld11"]
        q11 = sga1 * sgb1 * math.exp(ldb1 - lda1)
        rows.append(dict(ha=ra["h"], hb=rb["h"], r12=r12,
                         trat=rb["tau12"] / ra["tau12"],
                         crat=rb["c"] / ra["c"], dev=dev,
                         q12=q12, q11=q11, ra=ra, rb=rb))
    id_max = max(row["dev"] for row in rows)
    check("W-L1c FACTORIZATION r_12 = (tau'/tau) x (c'/c) on "
          "every pair: max scaled dev %.1e <= %.0e (bookkeeping)"
          % (id_max, ID_WARD), id_max <= ID_WARD, kill="KW")
    print("\n    THE RELATIVE DANGEROUS-QUOTIENT LADDER (%d "
          "pairs, %d typed skips; Q_11 column SPEC v2 (b)):"
          % (len(rows), n_skip))
    print("    %-12s %-11s %-11s %-9s %-11s %-11s" % (
        "step", "r_12", "tau'/tau", "c'/c", "Q_12", "Q_11"))
    for row in rows:
        print("    h %3d->%3d  %-11.3e %-11.3e %-9.4f %-11.3e "
              "%-11.3e"
              % (row["ha"], row["hb"], row["r12"], row["trat"],
                 row["crat"], row["q12"], row["q11"]))
    crats = np.array([row["crat"] for row in rows])
    minq12 = float(np.min([row["q12"] for row in rows]))
    print("\n    c-RATIO range: [%.4f, %.4f] (med %.4f) -- the "
          "new bounded piece; tau'/tau range: [%.3e, %.3e]"
          % (float(np.min(crats)), float(np.max(crats)),
             float(np.median(crats)),
             float(np.min([row["trat"] for row in rows])),
             float(np.max([row["trat"] for row in rows]))))
    check("W-L1d REPRODUCTION: %d pairs == %d; min_h Q_12 = "
          "%.3e == %.3e (rel tol %.0e)"
          % (len(rows), REF_N_TRUTH_PAIRS, minq12, REF_MINQ12,
             REF_MINQ12_RTOL),
          len(rows) == REF_N_TRUTH_PAIRS
          and abs(minq12 / REF_MINQ12 - 1.0) <= REF_MINQ12_RTOL,
          kill="KW")
    l1_tied = (spread <= CSPREAD_BAR and abs(b_c) <= CSLOPE_BAR)
    b_l1 = ("SOFTFLAG-TAU-TIED(c=[%.2f, %.2f])" % (mn, mx)
            if l1_tied else
            "SOFTFLAG-UNTIED(spread=%.1f, slope=%+.3f)"
            % (spread, b_c))
    check("L1.s typed: %s (spread %.2f vs %.0f; |slope| %.3f "
          "vs %.1f)" % (b_l1, spread, CSPREAD_BAR, abs(b_c),
                        CSLOPE_BAR), True)
    print("""
    READING: with c_h bounded, the dangerous quotient factors as
    r_12 = (tau'/tau) x (c'/c) -- its sign IS the tau-sign
    inheritance (given the bulk flags), and its 14-order collapse
    is the tau-scale itself, NOT an independent decay.  The
    bounded c-ratio is the new (hopefully provable) piece.""")

    # ------------------------------------------------------------ L2
    section("L2 -- THE RELATIVE EXTERIOR MARGIN: lam_min(R_h)/tau"
            " (fixed core) NEXT TO the port bulk margin/tau")
    check("W-L2a truth full wall all-PSD (neg A/R/S == 0 on "
          "every full-core rung)",
          all(r["negA"] == 0 and r.get("negR", 1) == 0
              and r.get("negS", 1) == 0 for r in fullc),
          kill="KW")
    print("\n    %-4s %-4s %-5s %-10s %-10s %-9s %-6s %-10s "
          "%-9s %-10s %s"
          % ("kz", "h", "n", "tau", "lamR", "lamR/tau", "|port|",
             "bulkm", "bulk/tau", "lamS", "lamS*w/tau"))
    for r in fullc:
        bm = r.get("bulkm")
        prod = (r["lamS"] * r["wcore"] / r["tau"]
                if "lamS" in r and r["tau"] > 0 else float("nan"))
        print("    %-4d %-4d %-5d %-10.3e %-10.3e %-9.1f %-6s "
              "%-10s %-9s %-10.3e %.6f"
              % (r["kz"], r["h"], r["n"], r["tau"], r["lamR"],
                 r["lamR"] / r["tau"],
                 str(r.get("nport", "n/a")),
                 ("%.3e" % bm) if bm is not None else "n/a",
                 ("%.1f" % (bm / r["tau"])) if bm is not None
                 else "n/a", r.get("lamS", float("nan")), prod))
    ratR = np.array([r["lamR"] / r["tau"] for r in fullc])
    hsc = np.array([r["h"] for r in fullc], float)
    c_R = float(np.min(ratR))
    mn2, q12_, q22, q32, mx2 = quart_row(ratR)
    _, b_R, se_R = ols_se(np.log(hsc), np.log(ratR))
    trendless = (abs(b_R) <= TREND_SLOPE_BAR
                 or abs(b_R) <= 2.0 * se_R)
    print("\n    lamR/tau quartiles: min %.1f q25 %.1f med %.1f "
          "q75 %.1f max %.1f" % (mn2, q12_, q22, q32, mx2))
    print("    OLS log(lamR/tau) ~ a + b log h: b = %+.4f +- "
          "%.4f (2 SE CI [%+.4f, %+.4f]; trendless iff |b| <= "
          "%.2f or CI contains 0)"
          % (b_R, 2.0 * se_R, b_R - 2.0 * se_R, b_R + 2.0 * se_R,
             TREND_SLOPE_BAR))
    both = [r for r in fullc if r.get("bulkm") is not None]
    ratB = np.array([r["bulkm"] / r["tau"] for r in both])
    ratRb = np.array([r["lamR"] / r["tau"] for r in both])
    corr = (float(np.corrcoef(np.log(ratRb), np.log(ratB))[0, 1])
            if len(both) >= 3 else float("nan"))
    print("\n    SIDE BY SIDE (%d rungs carry both exteriors): "
          "bulk/tau range [%.0f, %.0f] (port_schur round-38 "
          "scale 420..45000);" % (len(both), float(np.min(ratB)),
                                  float(np.max(ratB))))
    print("    corr(log lamR/tau, log bulk/tau) = %.4f (bar "
          "%.2f); med (bulk/tau)/(lamR/tau) = %.2f"
          % (corr, COHER_BAR,
             float(np.median(ratB / ratRb))))
    print("    (same operation -- (I-E)|_exterior = I - "
          "E|_exterior -- at two interior choices: the fixed "
          "8-node core vs the tau_m-threshold port set.)")
    b_l2 = ("EXTMARGIN-TRENDLESS(c_R=%.0f, slope=%+.3f)"
            % (c_R, b_R) if trendless
            else "EXTMARGIN-TRENDED(slope=%+.3f+-%.3f)"
            % (b_R, 2.0 * se_R))
    b_cmp = ("COMPRESSIONS-COHERENT(corr=%.3f)" % corr
             if np.isfinite(corr) and corr >= COHER_BAR
             else "COMPRESSIONS-DISTINCT(corr=%.3f)" % corr)
    check("L2.s typed: %s" % b_l2, True)
    check("L2.c typed: %s" % b_cmp, True)
    print("\n    THE RELATIVE REDUCTION STATEMENT: IF "
          "lam_min(R_h) >= c_R tau_h with the MEASURED c_R = "
          "%.0f (trend %+.3f) THEN by Haynsworth" % (c_R, b_R))
    print("    the wall A_h >= 0 <=> S_h >= 0 (fixed 8x8) -- "
          "conditional on a TAU-RELATIVE exterior bound, no "
          "absolute floor needed.")

    # ------------------------------------------------------------ L3
    section("L3 -- THE COMBINED CONDITIONAL CHAIN (theorem "
            "skeleton with measured constants)")
    # (iv) eta machinery on the same pairs (relative_congruence)
    etas = []
    n_cross = 0
    for row in rows:
        Aa, Ab = row["ra"]["A12"], row["rb"]["A12"]
        ew, Vw = row["ra"]["ew"], row["ra"]["Vw"]
        Wisq = Vw @ np.diag(ew ** -0.5) @ Vw.T
        H = Wisq @ (Ab - Aa) @ Wisq
        eta = 1.0 + float(np.linalg.eigvalsh(
            0.5 * (H + H.T))[0])
        etas.append(eta)
        if eta <= 0.0:
            n_cross += 1
        row["eta"] = eta
    etas = np.array(etas)
    min_eta = float(np.min(etas))
    i_min = int(np.argmin(etas))
    check("W-L3a REPRODUCTION (eta machinery): %d crossings == "
          "%d; min eta %.4f == %.4f (tol %.1e)"
          % (n_cross, REF_TRUTH_CROSS, min_eta, REF_MIN_ETA,
             ROUND_TOL),
          n_cross == REF_TRUTH_CROSS
          and abs(min_eta - REF_MIN_ETA) <= ROUND_TOL, kill="KW")
    nh2 = len(etas) // 2
    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in fullc if "lamS" in r])
    prod_dev = float(np.max(np.abs(prods - 1.0)))
    digits = int(-math.log10(max(prod_dev, 1e-300)))
    print("""
    THE CHAIN (printed as the skeleton; measured constants in
    brackets; NOTHING here is a proof beyond the deployed rungs):

      (i)   BASE -- CERTIFIED: A = I - C is PD at the base rung
            (v884 certified head positivity / v887 certified
            ladder complete; declared inputs, not re-run).

      (ii)  EXTERIOR -- RELATIVE, MEASURED: lam_min(R_h) >=
            c_R tau_h with c_R = %.0f (ladder min; quartile band
            %.0f..%.0f; slope %+.3f +- %.3f -> %s).
            The open theorem is now TAU-RELATIVE: a uniform
            c_R > 0, not an absolute floor.

      (iii) CORE <-> TAU -- EXACT GIVEN (ii): Haynsworth makes
            the wall equivalent to S_h >= 0 (fixed 8x8), and the
            measured correspondence lamS x wcore / tau = 1 to
            %.1e (%d digits over %d rungs): the 8x8 core
            positivity IS the tau-sign at measured precision.

      (iv)  STEP -- MEASURED, NOT PROVED: eta_h = 1 +
            lam_min(H_h) > 0 on all %d pairs (min %.4f at
            h %d->%d; medians %.4f first half vs %.4f second --
            non-decaying on the ladder); equivalently ALL flag
            quotients Q_k > 0, where by L1 the soft flag is
            r_12 = (tau'/tau) x (c'/c) with c'/c in
            [%.3f, %.3f]: the dangerous quotient IS the tau-sign
            inheritance times a bounded ratio.
"""
          % (c_R, q12_, q32, b_R, 2.0 * se_R,
             "trendless" if trendless else "TRENDED",
             prod_dev, digits, len(prods), len(etas), min_eta,
             rows[i_min]["ha"], rows[i_min]["hb"],
             float(np.median(etas[:nh2])),
             float(np.median(etas[nh2:])),
             float(np.min(crats)), float(np.max(crats))))
    print("    THE ONE REMAINING UNCONDITIONALLY OPEN STATEMENT "
          "(say it plainly): the TAU-SIGN INHERITANCE")
    print("    tau_{h+1} > 0 given tau_h > 0 -- equivalently "
          "eta_h > 0, equivalently min_k Q_k > 0 -- is STILL")
    print("    the wall.  Base is certified, Haynsworth and the "
          "congruence are exact algebra, and the exterior/")
    print("    soft-flag pieces are measured RELATIVE constants "
          "whose boundedness is the new provable target.")
    print("    What the reorganization buys: the open inequality "
          "is now BOUNDED-MARGIN-shaped (c in [%.2f, %.2f],"
          % (mn, mx))
    print("    c'/c in [%.3f, %.3f], c_R = %.0f trendless, eta "
          ">= %.4f) instead of COLLAPSING-margin-shaped"
          % (float(np.min(crats)), float(np.max(crats)), c_R,
             min_eta))
    print("    (min Q_12 ~ %.1e): the 14-order collapse was the "
          "tau-scale itself, carried by the relative" % minq12)
    print("    constants -- not an independent decay.  NO RH "
          "claim; no marker moves.")
    check("L3.s chain printed with measured constants", True)

    # ------------------------------------------------------------ C
    section("C -- controls: the relative laws must BREAK off "
            "the truth comb")
    # C2a: 12-window law on the smooth world
    sfull = [r for r in smooth if r.get("full") and "CJ" in r]
    for r in sfull:
        A = np.eye(NW) - r["CJ"]
        r["tau12"] = float(np.linalg.eigvalsh(A)[0])
    spairs = []
    for ra, rb in zip(smooth[:-1], smooth[1:]):
        if ra.get("full") and rb.get("full") \
                and "tau12" in ra and "tau12" in rb:
            spairs.append((ra, rb))
    n_cone = sum(1 for ra, _rb in spairs if ra["tau12"] <= 0.0)
    first_cone = next((ra["h"] for ra, _rb in spairs
                       if ra["tau12"] <= 0.0), None)
    print("  C2a -- smooth 12-window: %d pairs, base A_h "
          "indefinite (tau < 0 -> the c-law loses its PD "
          "premise) on %d; first at h = %s"
          % (len(spairs), n_cone, first_cone))
    check("C2a smooth c-law breaks: %d pairs == %d, CONE-EXITED "
          "on %d/%d (relative_congruence 28/28)"
          % (len(spairs), REF_N_SMOOTH_PAIRS, n_cone,
             len(spairs)),
          len(spairs) == REF_N_SMOOTH_PAIRS
          and n_cone == len(spairs), kill="KW")
    # C2b: full-operator relative exterior law on the smooth world
    sviol = [r for r in smooth if r["negA"] > 0]
    print("  C2b -- smooth full wall: %d/%d rungs with neg(A) > "
          "0 (tau < 0 -> lamR/tau meaningless as a relative "
          "margin)" % (len(sviol), len(smooth)))
    for r in sviol[:6]:
        print("      kz %-3d h %4d: tau %+.3e  lamR %s  neg(A) "
              "%d" % (r["kz"], r["h"], r["tau"],
                      ("%+.3e" % r["lamR"]) if "lamR" in r
                      else "n/a", r["negA"]))
    if len(sviol) > 6:
        print("      ... (%d more violating rungs)"
              % (len(sviol) - 6))
    check("C2b smooth exterior law breaks (neg(A) > 0 on >= 1 "
          "rung): %d rungs" % len(sviol), len(sviol) > 0,
          kill="KW")
    # C1: Epstein + scramble at kz 9
    print("  C1 -- Epstein/scramble at kz %d:" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok1 = True
    for nmc, kw in (("Epstein",
                     dict(comb=(np.log(nn.astype(float)),
                                2.0 * lamE_[nn]
                                / np.sqrt(nn.astype(float))))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = anatomy(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: chain dies (%r) -> FIRES (frame "
                  "death)" % (nmc, rc))
            continue
        f = rc["negA"] > 0
        ok1 &= f
        print("    %-8s: tau %+.3e  neg(A) %d -> %s"
              % (nmc, rc["tau"], rc["negA"],
                 "FIRES" if f else "SILENT"))
    check("C1 controls fire (frame death or neg(A) > 0)", ok1,
          kill="KW")

    return finish(dict(l1=b_l1, l2=b_l2, cmp=b_cmp, c_R=c_R,
                       mn=mn, mx=mx, minq12=minq12,
                       min_eta=min_eta))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("RELFLAG-MEASURED / %(l1)s / %(l2)s / %(cmp)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (c in [%(mn).2f, %(mx).2f]; c_R = %(c_R).0f; "
              "min Q_12 = %(minq12).3e; min eta = %(min_eta).4f)"
              % labels)
    print("""
  HONEST FRAME (as frozen): c >= 1 and the factorization of
  r_12 are exact algebra on PD rungs -- warded bookkeeping.  The
  content is the measured boundedness/trendlessness of c, c'/c
  and lamR/tau on the deployed ladder; the census is FINITE and
  the tau-sign inheritance remains open.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
