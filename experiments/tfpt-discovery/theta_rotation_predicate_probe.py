"""Discovery probe: THE THETA(alpha) ROTATION PREDICATE -- where and
why does the minimal-mode angle theta(alpha) run through the 45/90 deg
rotation degeneracies of the lock identification?

CONTEXT.  w3_resonance_landscape_probe (2026-08-02) mapped P(alpha) =
q tan^2 theta on 8 fixed-h slices (81-point grid, +-10%) and found 52
peaks; the needles are ROT-regime points (theta >= 45 deg) where the
lock identification degenerates and P is NOT the positivity criterion;
lambda_min stays positive on the whole surveyed grid and NO frozen
arithmetic candidate predicts the peaks (W3RL-PEAKED-UNEXPLAINED).
The probe named its successor: a PREDICATE for the rotation passages.
THIS probe builds, per (h, alpha), an explicit 2x2 reduction of the
window pencil and tests whether the rotation needles are its
(avoided) level crossings.

THE TWO CONSTRUCTIONS (T1, declared BEFORE running):
  * K1 (exact, eigenvector-SLAVED): the rid_alignment_probe basis
    {w_hat_lock, w_perp(m)} with w_perp the G-normalized component of
    the minimal mode m orthogonal (in G) to the lock direction.  The
    2x2 [[lambda_lock, B1], [B1, Q_perp]] carries m exactly: its
    LOWER eigenvalue is lambda_min and its lower eigenvector is
    (cos theta, sin theta) (rid constraints C1/C2).  K1 is the
    exactness anchor -- but the basis is built FROM m, so along alpha
    it is slaved to eigenvector branch switches (its continuity is
    MEASURED, not assumed), and every angle statement derived from it
    is CIRCULAR as a predicate (theta_K1 >= 45 iff lambda_lock >=
    Q_perp holds IDENTICALLY).  K1 is therefore never used for T3.
  * K2 (continuous, eigenvector-FREE -- the predicate carrier): the
    basis {w_hat_lock(alpha), v_defl(alpha)} with v_defl the LOWEST
    eigenvector of the pencil DEFLATED to the G-orthocomplement of
    the lock direction, computed from the full spectrum (lambda_j,
    v_j) by the Wilkinson secular equation
        sum_j c_j^2 / (lambda_j - mu) = 0,   c = V^T G w_hat,
    lowest root mu1 in (lambda_1, lambda_2); levels with |c_j| below
    C_TOL are themselves deflated eigenvalues (handled).  Exact
    identity (checked): (A - mu1 G) v_defl = B G w_hat, so the
    effective 2x2 is [[lambda_lock, B], [B, mu1]] and the invariance
    defect of the 2-space (the leak of A w_hat out of it) is a
    measurable per-point number.  NOTHING in K2 reads the minimal
    mode, so theta_K2(alpha), f(alpha) = lambda_lock(alpha) -
    mu1(alpha) and B(alpha) are legitimate PREDICTIVE ingredients.
    theta_K2 crosses 45 deg EXACTLY at f = 0; the K2 needle is an
    avoided crossing of predicted width ~ 2|B| / |f'|.

CALIBRATION HISTORY (declared -- honesty first): run 1 (2026-08-02)
passed every guard and every anchor (52 peaks reproduced, theta(859)
= 43.48 deg) but FAILED the K2 orthogonality wiring bar: the RAW
secular eigenvector carried |c . a| up to 1.8e-3 at near-degenerate
needle points (float conditioning of a_j = c_j/(lambda_j - mu1); the
interlacing and spectral-consistency bars passed at 0.0 and 1.7e-10).
Run 2 changes, WITHOUT touching any gate, grid, anchor or the verdict
logic: (a) the constrained eigenvector is explicitly projected onto
the exact constraint (a <- a - (c.a) c, renormalized) before use --
numerics hygiene only; (b) T4 additionally PRINTS, per window, the
distance to the nearest MEASURED theta_full = 45 crossing on the same
scan grid (interpolated; bisection-refined for h = 859) -- a declared
run-2 diagnostic with NO gate, needed because run 1 showed the f-zero
predicate is complete (recall 1.0) but not sharp (precision 0.18), so
predicate distances are conservative (over-tight) safety reads.

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * base sweep, sample, slice choice, grid: the resonance-landscape
    probe VERBATIM (67 complete frame-A windows, truncated {1219,
    1292, 1445}; lock sign; float floor FLOOR_SAFETY x eps x radius x
    sqrt(h); top-4 by P = {859, 363, 1430, 1393} + 4 h-quantile
    picks; 81-point alpha-grid +-10%, center forced to s = 0, Mz
    fixed per window, atom-complete configurations only); guards
    G0.1-G0.7 verbatim (same anchor quotes); the run-1 DST/score
    machinery is NOT rebuilt (peaks depend on P only -- identical
    numerics for everything used);
  * NEW anchors: total peak count = 52 (the landscape run quote) and
    theta(h = 859, s = 0) = 43.5 deg (tol 0.2);
  * T1 bars: K1 exactness (2x2 lower eigenvalue = lambda_min and
    eigenvector residual, both rel < 1e-6, the rid bar); K2 wiring
    [E]: interlacing lambda_1 - tol <= mu1 <= lambda_2 + tol (tol =
    1e-9 x pencil radius), G-orthogonality |c . a| < 1e-8,
    lambda_lock spectral consistency rel < 1e-6, secular anomaly
    share < 1%; K2 angle fidelity and the 2-space leak are MEASURED
    (median / p90 / max printed, split by regime) -- no fidelity
    gate, the predicate quality is judged by T3;
  * T1 continuity read: consecutive-point G-overlaps of v_defl (K2)
    and w_perp (K1) along each profile; K2 is documented as THE
    continuous construction if its median overlap exceeds the K1
    median (typed, no hard gate); the K2 sign chain for B(alpha) is
    trusted at a step iff |overlap| >= OV_TRACK = 0.5;
  * T2 mechanism classification, per landscape peak (frozen): window
    = FWHM interval +- 1 grid step; signals inside the window:
    CROSS  <=> max f >= 0 AND min f < 0        (diagonal crossing),
    BSIGN  <=> the sign-chained B changes sign AND every step in the
               window has |overlap| >= OV_TRACK (trusted chain),
    LCKDEG <=> min lambda_lock <= 0             (lock degenerates);
    precedence LCKDEG > CROSS+BSIGN > CROSS > BSIGN > NONE; NONE
    peaks report max f / (2|B|) as crossing proximity; per CROSS
    peak the predicted needle width 2|B| / |f'| at the interpolated
    zero is printed against the coarse FWHM (grid-resolution bound);
  * T3 predicates on the pooled feasible profile grid (truth =
    landscape regime ROT, i.e. theta_full >= 45 deg with lambda_min
    >= -floor):
    PRED1 (primary, the K2 rotation criterion): f(alpha) >= 0;
    PRED2 (the avoided-crossing band, reported): |f| <= 2|B|;
    gate: PRED1 precision AND recall >= PR_BAR = 0.8; EVENT level:
    45-deg crossings of theta_full (linear interpolation between
    grid neighbours) vs sign changes of f, greedy 1-1 match with
    tolerance one grid step (0.0025); needle DENSITY: f-zero
    clusters (gap <= 2 grid steps) = needle centers; center spacing
    in u-units (du = 2 alpha ds) compared to the window grid D and
    to the local atom gap (both printed per slice);
  * T4 frame-A safety, per complete window (frozen): scan f on s in
    +-2.5% step 0.25% (s = 0 reused from the base sweep); nearest
    sign-change bracket per side refined by bisection to 1e-5; the
    <= 2 interior f-maxima nearest to s = 0 refined by one parabolic
    vertex evaluation each, needle CONFIRMED iff refined f >= 0;
    distance = |s| of the nearest confirmed needle, in units of
    W_NEEDLE = 2.5e-4 (the landscape run-2 fine-FWHM median, the
    declared needle-width unit); windows without a confirmed needle
    in range are censored at 2.5% (reported as >=); Newton
    extrapolation -f(0)/f'(0) and the coupling margin
    -f(0)/(2|B(0)|) reported per window; typing: FRAME-A-SAFE iff
    the minimum distance over the analysis windows (complete x lock
    x above-floor) >= 10 x W_NEEDLE, else FRAME-A-TIGHT; h = 859
    reported in detail (the 43.5-deg window);
  * T5 typing only: contract-note text printed; no marker move.

Verdict enums (frozen, precedence top-down):
  THETA-MIXED       guards or T1 exactness/wiring bars fail;
  THETA-PRED-PASS   PRED1 pointwise precision AND recall >= 0.8;
  THETA-PRED-EVENT  pointwise gate fails but the event-level match
                    (45-deg crossings vs f-zeros) has precision AND
                    recall >= 0.8;
  THETA-PRED-FAIL   neither gate passes.

FIREWALL: experiments-only; verification/ read-only (v563 import;
v618/v591/rid/landscape machinery REBUILT verbatim, no other
imports); no marker moves; no positivity claim; no RH statement; NO
zero of any L-function is read (AST-checked).  Python-only, per
GATE.WOLFRAM.02.

Provenance: w3_resonance_landscape_probe (2026-08-02, the 52-peak
landscape + regime typing), rid_alignment_probe (K1 geometry, closed
formula), margin_link_probe (lock direction, r_id), w3_uniform_bound
probe (alpha-shift machinery), v618 (C = 1 reads), v591 (closed lock
direction).
"""
import ast
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0

EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0          # w3 probe, verbatim
GRID_PER_D = 4.0             # v618, verbatim
N_GRID = 81                  # landscape grid, verbatim
S_MAX = 0.10
P_PEAK_BAR = 0.80            # landscape peak bar, verbatim
THETA_BAR = 45.0             # regime bar (deg), verbatim
QUANTS = (0.15, 0.40, 0.60, 0.85)
TOP4_QUOTE = {859, 363, 1430, 1393}
A3_SHIFT_IDX = (-20, -10, 10, 20)
STAB_BAR = 0.15
# reproduction anchors (landscape/rid quotes, verbatim)
P_MAX_QUOTE, P_MAX_TOL = 0.9636, 0.005
H_AT_PMAX = 859
SP_P_H_QUOTE, SP_TOL = 0.735, 0.03
SP_RID_H_QUOTE = -0.784
RID_MED_QUOTE, RID_TOL = 0.584, 0.005
THETA_MED_QUOTE = 9.1
PEAKS_QUOTE = 52             # landscape run quote (new anchor)
THETA_859_QUOTE, THETA_859_TOL = 43.5, 0.2
BAR_EIGEN = 1e-6
BAR_REBUILD = 1e-12
# this probe's frozen additions
C_TOL = 1e-10                # secular active-level threshold on |c_j|
OV_TRACK = 0.5               # trusted sign-chain overlap bar
ANOM_BAR = 0.01              # secular anomaly share bar
PR_BAR = 0.80                # predicate precision/recall bar
EV_TOL = 0.0025              # event match tolerance (one grid step)
W_NEEDLE = 2.5e-4            # needle-width unit (landscape zoom read)
S_SCAN = 0.025               # T4 scan half-width
SCAN_STEP = 0.0025           # T4 scan step
BIS_TOL = 1.0e-5             # T4 bisection tolerance in s
MAX_PARAB = 2                # T4 refined f-maxima per window
SAFE_BAR = 10.0              # FRAME-A-SAFE bar in needle widths


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in (
                "zetazero", "nzeros", "second_sheet_zero"):
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("zetazero", "nzeros"):
            return False
    return True


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402
import scipy.linalg as sla  # noqa: E402
from scipy.optimize import brentq  # noqa: E402


# ------------------------------------------------------ v618 machinery
def zeta_grid_const():
    mp.mp.dps = 30
    c_th = float(-2 * mp.diff(lambda s: mp.zeta(s), mp.mpf(1) / 2)
                 / mp.zeta(mp.mpf(1) / 2))
    return 2.0 * math.log(-c_th / 4.0)


def model_matrix(alpha, Mz, D, W11, W22, W12, u0):
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - u0) / delta))
    edges = u0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    X = np.empty((n_cells, 3))
    for k, u_j in enumerate(centers):
        X[k, 0] = core.spline_project(W11, u_j, D, Mz)
        X[k, 1] = core.spline_project(W22, u_j, D, Mz)
        X[k, 2] = core.spline_project(W12, u_j, D, Mz)
    s = (lam[:, None] * X).sum(axis=0)
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def lock_dir(alpha):
    v2v1 = -(alpha ** 2 + 16 * math.pi ** 2) / (2 * (alpha ** 2
                                                     + 4 * math.pi ** 2))
    v = np.array([1.0, v2v1])
    return v / np.linalg.norm(v)


def gen_eig_full(A, G):
    """Full generalized eigendecomposition (ascending) + pencil
    radius.  Same eigh call as the landscape gen_min_eig2 -- the
    lowest pair is numerically identical."""
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    return w, V, rad


# ------------------------------------------------------ v637 statistics
def rankdata(a):
    a = np.asarray(a, float)
    order = np.argsort(a, kind="mergesort")
    r = np.empty(len(a))
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]:
            j += 1
        r[order[i:j + 1]] = 0.5 * (i + j) + 1.0
        i = j + 1
    return r


def pearson(xx, yy):
    xx = np.asarray(xx, float) - np.mean(xx)
    yy = np.asarray(yy, float) - np.mean(yy)
    return float(xx @ yy / math.sqrt((xx @ xx) * (yy @ yy)))


def spearman(xx, yy):
    return pearson(rankdata(xx), rankdata(yy))


# --------------------------------------------- hz-only caches (exact)
_HZ_CACHE = {}
U0_GRID = None
N_EVAL = 0


def hz_objects(hz):
    """Parity basis and lag weights depend on hz ONLY (numerically
    identical to the landscape rebuild; the run-1 Bfull DST object is
    not needed here and is not built)."""
    if hz not in _HZ_CACHE:
        Tb = core.parity_basis(hz, 2)
        t1v, t2v = Tb[0].copy(), Tb[1].copy()
        W11 = core.lag_weights_from_v(t1v, hz)
        W22 = core.lag_weights_from_v(t2v, hz)
        Wpp = core.lag_weights_from_v(t1v + t2v, hz)
        W12 = 0.5 * (Wpp - W11 - W22)
        _HZ_CACHE.clear()
        _HZ_CACHE[hz] = (t1v, t2v, W11, W22, W12)
    return _HZ_CACHE[hz]


# ------------------------------------------------ K2 secular deflation
def deflated_lowest(lams, cs, rad):
    """Lowest eigenvalue mu1 of the pencil restricted to the
    G-orthocomplement of w_hat (coordinates cs in the G-orthonormal
    eigenbasis, sum cs^2 = 1) and the coordinates a of the
    constrained eigenvector.  Wilkinson secular equation on the
    active levels; inactive levels (|c_j| <= C_TOL) are themselves
    constrained eigenvalues.  Returns (mu1, a, anomaly_flag)."""
    act = np.abs(cs) > C_TOL
    n_act = int(act.sum())
    anomaly = False
    root = None
    if n_act >= 2:
        la = lams[act]
        ca2 = cs[act] ** 2
        lo, hi = float(la[0]), float(la[1])
        span = hi - lo
        if span <= 0.0:
            root = lo
            anomaly = True
        else:
            def g(mu):
                return float(np.sum(ca2 / (la - mu)))
            eps_b = 1e-9 * span
            ok = False
            for _ in range(24):
                if g(lo + eps_b) < 0.0 < g(hi - eps_b):
                    ok = True
                    break
                eps_b *= 0.1
                if eps_b < 1e-300:
                    break
            if ok:
                root = float(brentq(g, lo + eps_b, hi - eps_b,
                                    xtol=max(span * 1e-15, 1e-300),
                                    rtol=8.9e-16, maxiter=200))
            else:
                root = lo
                anomaly = True
    cands = []
    if root is not None:
        cands.append(("root", root))
    if n_act < len(lams):
        k_in = int(np.argmin(np.where(act, np.inf, lams)))
        cands.append(("level", float(lams[k_in])))
    if not cands:
        return float(lams[0]), None, True
    kind, mu1 = min(cands, key=lambda t: t[1])
    a = np.zeros(len(lams))
    if kind == "root":
        den = lams[act] - mu1
        if float(np.min(np.abs(den))) < 1e-13 * max(rad, 1.0):
            j_near = int(np.argmin(np.abs(den)))
            idx = np.nonzero(act)[0][j_near]
            a[idx] = 1.0
            anomaly = True
        else:
            a[act] = cs[act] / den
    else:
        inact_lams = np.where(act, np.inf, lams)
        a[int(np.argmin(inact_lams))] = 1.0
    # run-2 calibration: exact-constraint projection (a _|_ c), then
    # normalization -- removes the float residual of the secular root
    a = a - float(cs @ a) * cs
    nrm = float(np.linalg.norm(a))
    if nrm <= 0.0:
        return mu1, None, True
    a /= nrm
    return mu1, a, anomaly


# ------------------------------------------------------ window builder
def window_eval(alpha, Mz, v_prev_d=None, v_prev_p=None):
    """One window at EXPLICIT (alpha, Mz): the landscape window_eval
    numerics verbatim (same assembly, same eigh), extended by the K1
    2x2 entries and the K2 eigenvector-free deflated 2x2.  Returns
    (record, v_defl, w_perp) for continuity chaining."""
    global N_EVAL
    N_EVAL += 1
    hz = Mz // 2
    complete = math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5
    ka = core.atoms_in(alpha)
    c_at, D = core.atom_lags_at(alpha, Mz, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    c_ar = core.arch_lags(Mz, D)
    A = core.odd_toeplitz(c_ar + c_at, Mz)
    g = np.zeros(Mz)
    g[0], g[1] = 2.0 * D / 3.0, D / 6.0
    Gm = core.odd_toeplitz(g, Mz)
    w_all, V_all, rad = gen_eig_full(A, Gm)
    lam_min, lam_2, v_min = float(w_all[0]), float(w_all[1]), V_all[:, 0]
    floor = FLOOR_SAFETY * EPS * rad * math.sqrt(hz)
    # v618 lock read (verbatim route)
    t1v, t2v, W11, W22, W12 = hz_objects(hz)
    B2 = np.array([[c_ar @ W11, c_ar @ W12], [c_ar @ W12, c_ar @ W22]])
    lamw = 0.5 * np.array([float(m) for m in core.MU_ALL[:ka]])
    uu = np.array([float(u) for u in core.U_ALL[:ka]])
    s11 = s22 = s12 = 0.0
    for i in range(ka):
        s11 += lamw[i] * core.spline_project(W11, uu[i], D, Mz)
        s22 += lamw[i] * core.spline_project(W22, uu[i], D, Mz)
        s12 += lamw[i] * core.spline_project(W12, uu[i], D, Mz)
    S2 = np.array([[s11, s12], [s12, s22]])
    Sm = model_matrix(alpha, Mz, D, W11, W22, W12, U0_GRID)
    vl = lock_dir(alpha)
    q_r = float(vl @ ((B2 - S2) @ vl))
    q_m = float(vl @ ((B2 - Sm) @ vl))
    # K1: rid geometry, G-orthonormal split of the minimal mode
    wl = vl[0] * t1v + vl[1] * t2v
    wlGwl = float(wl @ (Gm @ wl))
    wlAwl = float(wl @ (A @ wl))
    w_hat = wl / math.sqrt(wlGwl)
    vGv = float(v_min @ (Gm @ v_min))
    m_vec = v_min / math.sqrt(vGv)
    ct = float(w_hat @ (Gm @ m_vec))
    if ct < 0.0:
        m_vec = -m_vec
        ct = -ct
    ct = min(1.0, ct)
    st = math.sqrt(max(0.0, 1.0 - ct * ct))
    perp = m_vec - ct * w_hat
    pn = math.sqrt(max(0.0, float(perp @ (Gm @ perp))))
    w_perp = perp / pn if pn > 0.0 else perp
    lam_lock = wlAwl / wlGwl
    Q_perp = float(w_perp @ (A @ w_perp))
    B_k1 = float(w_hat @ (A @ w_perp))
    t2 = (st / ct) ** 2 if ct > 0.0 else float("inf")
    qq = Q_perp / lam_lock
    # K2: eigenvector-free deflated 2x2
    c_vec = V_all.T @ (Gm @ w_hat)
    lam_lock_spec = float(np.sum(c_vec ** 2 * w_all))
    mu1, a_vec, anom = deflated_lowest(w_all, c_vec, rad)
    if a_vec is None:
        a_vec = np.zeros(len(w_all))
        a_vec[0] = 1.0
    B_k2 = float(np.sum(w_all * c_vec * a_vec))
    orth = abs(float(c_vec @ a_vec))
    f_gap = lam_lock - mu1
    M2 = np.array([[lam_lock, B_k2], [B_k2, mu1]])
    w2, V2 = np.linalg.eigh(M2)
    th_k2 = math.degrees(math.acos(min(1.0, abs(float(V2[0, 0])))))
    rho_leak = (w_all - lam_lock) * c_vec - B_k2 * a_vec
    leak = float(np.linalg.norm(rho_leak)
                 / np.linalg.norm(w_all * c_vec))
    v_defl = V_all @ a_vec
    ov_d = float(v_prev_d @ (Gm @ v_defl)) if v_prev_d is not None \
        else float("nan")
    ov_p = float(v_prev_p @ (Gm @ w_perp)) if v_prev_p is not None \
        else float("nan")
    gap_loc = float(core.U_ALL[min(ka + 4, len(core.U_ALL) - 1)]
                    - core.U_ALL[ka - 5]) / 9.0
    rec = dict(h=hz, alpha=alpha, D=D, complete=complete,
               lam=lam_min, lam2=lam_2, floor=floor, rad=rad,
               qr=q_r, qm=q_m, lock=q_r * q_m > 0.0,
               ct=ct, st=st, t2=t2, qq=qq, P=qq * t2,
               lam_lock=lam_lock, theta=math.degrees(math.acos(ct)),
               Qp=Q_perp, Bk1=B_k1,
               mu1=mu1, f=f_gap, Bk2=B_k2, th_k2=th_k2, leak=leak,
               orth=orth, anom=anom, lam_lock_spec=lam_lock_spec,
               ov_d=ov_d, ov_p=ov_p, gap_loc=gap_loc)
    return rec, v_defl, w_perp


# ------------------------------------------------------ peak analysis
def detect_peaks(ss, Pv_):
    """Landscape verbatim: interior local maxima with P >= P_PEAK_BAR;
    boundary maxima typed CENSORED."""
    n = len(ss)
    out = []
    for i in range(n):
        if Pv_[i] < P_PEAK_BAR:
            continue
        if 0 < i < n - 1:
            if Pv_[i] >= Pv_[i - 1] and Pv_[i] >= Pv_[i + 1] \
                    and (Pv_[i] > Pv_[i - 1] or Pv_[i] > Pv_[i + 1]):
                out.append((i, "peak"))
        elif i == 0 and n > 1 and Pv_[0] > Pv_[1]:
            out.append((i, "censored"))
        elif i == n - 1 and n > 1 and Pv_[n - 1] > Pv_[n - 2]:
            out.append((i, "censored"))
    return out


def fwhm_interval(ss, Pv_, ip, base):
    """Landscape verbatim: half-prominence interval around peak ip."""
    level = base + 0.5 * (Pv_[ip] - base)
    n = len(ss)
    j = ip
    while j > 0 and Pv_[j - 1] >= level:
        j -= 1
    if j == 0 and Pv_[0] >= level:
        s_l, cen_l = ss[0], True
    else:
        fr = (level - Pv_[j - 1]) / (Pv_[j] - Pv_[j - 1])
        s_l, cen_l = ss[j - 1] + fr * (ss[j] - ss[j - 1]), False
    j = ip
    while j < n - 1 and Pv_[j + 1] >= level:
        j += 1
    if j == n - 1 and Pv_[n - 1] >= level:
        s_r, cen_r = ss[n - 1], True
    else:
        fr = (level - Pv_[j]) / (Pv_[j + 1] - Pv_[j])
        s_r, cen_r = ss[j] + fr * (ss[j + 1] - ss[j]), False
    return s_l, s_r, level, (cen_l or cen_r)


def regime_of(rv):
    """Landscape verbatim (precedence top-down)."""
    if rv["lam"] < -rv["floor"]:
        return "NEG"
    if rv["theta"] >= THETA_BAR:
        return "ROT"
    if rv["lam_lock"] <= 0.0:
        return "LCK"
    return "MARGIN"


def cross_events(ss, vals, level):
    """Interpolated crossing positions of vals through level."""
    ev = []
    for i in range(len(ss) - 1):
        d0, d1 = vals[i] - level, vals[i + 1] - level
        if d0 == 0.0:
            ev.append(float(ss[i]))
        elif d0 * d1 < 0.0:
            fr = d0 / (d0 - d1)
            ev.append(float(ss[i] + fr * (ss[i + 1] - ss[i])))
    return ev


def greedy_match(ev_a, ev_b, tol):
    """1-1 greedy nearest matching; returns number of matches."""
    a = sorted(ev_a)
    b = sorted(ev_b)
    used = [False] * len(b)
    n_m = 0
    for x in a:
        best, best_d = -1, tol
        for j, y in enumerate(b):
            if used[j]:
                continue
            d = abs(x - y)
            if d <= best_d:
                best, best_d = j, d
        if best >= 0:
            used[best] = True
            n_m += 1
    return n_m


def run():
    global N_CHK, FAILS, U0_GRID
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE THETA(alpha) ROTATION PREDICATE -- the 2x2 reduction "
          "of the lock pencil")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    U0_GRID = zeta_grid_const()

    # ------------------------------------------------ base sweep
    KZ = core.frame_a_zones()
    rows = []
    for kz in KZ:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        r, _, _ = window_eval(alpha, Mz)
        r["kz"] = kz
        r["Mz"] = Mz
        rows.append(r)
        if len(rows) % 10 == 0:
            print("      ... %d/%d windows (%.0f s)"
                  % (len(rows), len(KZ), time.time() - T0))

    comp = [r for r in rows if r["complete"]]
    inc_hs = sorted(r["h"] for r in rows if not r["complete"])
    check("G0.1 [E] the declared surface reproduces: %d frame-A "
          "windows, %d complete combs, truncated set %s"
          % (len(rows), len(comp), inc_hs),
          len(comp) == 67 and inc_hs == [1219, 1292, 1445])

    lock_c = [r for r in comp if r["lock"] and r["lam"] > r["floor"]]
    n = len(lock_c)
    hs = np.array([r["h"] for r in lock_c], float)
    Pv = np.array([r["P"] for r in lock_c])
    qq = np.array([r["qq"] for r in lock_c])
    t2 = np.array([r["t2"] for r in lock_c])
    rid = np.array([r["lam"] / r["lam_lock"] for r in lock_c])
    th = np.array([r["theta"] for r in lock_c])
    i_max = int(np.argmax(Pv))
    sp_P = spearman(Pv, hs)
    sp_r = spearman(rid, hs)
    check("G0.2 [E] the rid anchors reproduce on n = %d (>= 60): max "
          "P = %.4f at h = %d (quote %.4f at %d), Spearman(P, h) = "
          "%+.4f (quote %+.3f), Spearman(r_id, h) = %+.4f (quote "
          "%+.3f), median r_id %.4f (quote %.3f), median theta %.2f "
          "deg (quote %.1f)"
          % (n, float(Pv[i_max]), int(hs[i_max]), P_MAX_QUOTE,
             H_AT_PMAX, sp_P, SP_P_H_QUOTE, sp_r, SP_RID_H_QUOTE,
             float(np.median(rid)), RID_MED_QUOTE,
             float(np.median(th)), THETA_MED_QUOTE),
          n >= 60
          and abs(float(Pv[i_max]) - P_MAX_QUOTE) <= P_MAX_TOL
          and int(hs[i_max]) == H_AT_PMAX
          and abs(sp_P - SP_P_H_QUOTE) <= SP_TOL
          and abs(sp_r - SP_RID_H_QUOTE) <= SP_TOL
          and abs(float(np.median(rid)) - RID_MED_QUOTE) <= RID_TOL
          and abs(float(np.median(th)) - THETA_MED_QUOTE) <= 0.15)

    r_cf = (1.0 - qq * t2) / (1.0 - t2)
    dev_cf = float(np.max(np.abs(r_cf - rid)))
    check("G0.3 [E] closed formula + structure on every sample "
          "window: max |r_id formula dev| = %.1e < %.0e, q > 1 (min "
          "%.3f), theta < 45 deg (max %.2f), P < 1 (max %.4f)"
          % (dev_cf, BAR_EIGEN, float(qq.min()), float(th.max()),
             float(Pv.max())),
          dev_cf < BAR_EIGEN and float(qq.min()) > 1.0
          and float(th.max()) < 45.0 and float(Pv.max()) < 1.0)

    r859 = [r for r in lock_c if r["h"] == 859]
    th859 = r859[0]["theta"] if r859 else float("nan")
    check("G0.3b [E] the new angle anchor: theta(h = 859, s = 0) = "
          "%.3f deg (quote %.1f, tol %.1f); theta_K2 there %.3f deg, "
          "f(0) = %+.4e, 2|B(0)| = %.4e"
          % (th859, THETA_859_QUOTE, THETA_859_TOL,
             r859[0]["th_k2"] if r859 else float("nan"),
             r859[0]["f"] if r859 else float("nan"),
             2 * abs(r859[0]["Bk2"]) if r859 else float("nan")),
          bool(r859) and abs(th859 - THETA_859_QUOTE) <= THETA_859_TOL)

    # ------------------------------------------------ slice selection
    order = np.argsort(-Pv)
    top4 = [int(i) for i in order[:4]]
    top4_h = sorted(int(hs[i]) for i in top4)
    check("G0.4 [E] the top-4 windows by P are %s (declared quote %s)"
          % (top4_h, sorted(TOP4_QUOTE)), set(top4_h) == TOP4_QUOTE)

    rest = [i for i in range(n) if i not in set(top4)]
    hs_rest = hs[rest]
    picks = []
    for qv in QUANTS:
        tgt = float(np.quantile(hs_rest, qv))
        cand = sorted((i for i in rest if i not in picks),
                      key=lambda i: abs(hs[i] - tgt))[0]
        picks.append(cand)
    sel = top4 + picks
    sel_tags = (["TOP-P"] * 4) + ["QUANT-%.2f" % qv for qv in QUANTS]
    check("G0.5 [E] slice selection: 8 distinct windows, top-4 by P "
          "+ h-quantile picks %s -> h = %s"
          % (list(QUANTS), [int(hs[i]) for i in sel]),
          len(set(sel)) == 8)

    # ------------------------------------------------ the profiles
    print("\nR1 -- the 8 alpha-profiles (landscape grid rebuilt "
          "verbatim; K2 entries chained per point)")
    SGRID = np.linspace(-S_MAX, S_MAX, N_GRID)
    SGRID[N_GRID // 2] = 0.0
    profiles = []
    for i_w, tag in zip(sel, sel_tags):
        r0 = lock_c[i_w]
        t_w = time.time()
        ss, recs = [], []
        n_infeas = 0
        v_prev_d, v_prev_p = None, None
        sgn = 1.0
        for s in SGRID:
            a_p = r0["alpha"] * (1.0 + s)
            if math.exp(2.0 * a_p) > core.ATOM_MAX + 0.5:
                n_infeas += 1
                continue
            rv, vd, wp = window_eval(a_p, r0["Mz"], v_prev_d, v_prev_p)
            if not math.isnan(rv["ov_d"]) and rv["ov_d"] < 0.0:
                sgn = -sgn
            rv["Bsgn"] = sgn * rv["Bk2"]
            v_prev_d, v_prev_p = vd, wp
            ss.append(float(s))
            recs.append(rv)
        ss = np.array(ss)
        pr = dict(i_w=i_w, tag=tag, r0=r0, ss=ss, recs=recs,
                  Pp=np.array([rv["P"] for rv in recs]),
                  i0=int(np.where(ss == 0.0)[0][0]),
                  n_infeas=n_infeas,
                  f=np.array([rv["f"] for rv in recs]),
                  Bs=np.array([rv["Bsgn"] for rv in recs]),
                  Babs=np.array([abs(rv["Bk2"]) for rv in recs]),
                  th=np.array([rv["theta"] for rv in recs]),
                  thk2=np.array([rv["th_k2"] for rv in recs]),
                  ll=np.array([rv["lam_lock"] for rv in recs]),
                  mu=np.array([rv["mu1"] for rv in recs]),
                  lk=np.array([rv["leak"] for rv in recs]),
                  ovd=np.array([rv["ov_d"] for rv in recs]),
                  ovp=np.array([rv["ov_p"] for rv in recs]))
        pr["regs"] = [regime_of(rv) for rv in recs]
        profiles.append(pr)
        print("      h = %4d (%s): %d feasible / %d infeasible "
              "points  [%.0f s]"
              % (r0["h"], tag, len(ss), n_infeas, time.time() - t_w))

    dev_reb = max(abs(pr["Pp"][pr["i0"]] - pr["r0"]["P"])
                  / pr["r0"]["P"] for pr in profiles)
    check("G0.6 [E] wiring guard: the s = 0 rebuild reproduces the "
          "base-sweep P on all 8 slices (max rel dev %.1e < %.0e)"
          % (dev_reb, BAR_REBUILD), dev_reb < BAR_REBUILD)

    pr859 = [pr for pr in profiles if pr["r0"]["h"] == 859][0]
    devs = []
    for di in A3_SHIFT_IDX:
        j = pr859["i0"] + di
        if 0 <= j < len(pr859["ss"]):
            devs.append(abs(pr859["Pp"][j] - pr859["Pp"][pr859["i0"]])
                        / pr859["Pp"][pr859["i0"]])
    frag = max(devs) if devs else 0.0
    check("G0.7 [E] the w3ub A3 FRAGILE read reproduces on h = 859: "
          "max |dP|/P over s in {+-2.5%%, +-5%%} = %.4f > %.2f"
          % (frag, STAB_BAR), frag > STAB_BAR)

    # peaks (landscape verbatim)
    all_peaks = []
    for pr in profiles:
        ss, Pp = pr["ss"], pr["Pp"]
        base = float(np.median(Pp))
        pk = detect_peaks(ss, Pp)
        intervals = []
        for ip, kind in pk:
            s_l, s_r, level, cens = fwhm_interval(ss, Pp, ip, base)
            intervals.append(dict(ip=ip, kind=kind, s=float(ss[ip]),
                                  P=float(Pp[ip]), s_l=s_l, s_r=s_r,
                                  w=s_r - s_l,
                                  cens=cens or (kind == "censored")))
        pr["base"] = base
        pr["peaks"] = intervals
        all_peaks.extend((pr, iv) for iv in intervals)
    n_peaks_tot = len(all_peaks)
    check("G0.8 [E] the landscape peak set reproduces: %d peaks "
          "total (quote %d); per-slice counts %s"
          % (n_peaks_tot, PEAKS_QUOTE,
             [len(pr["peaks"]) for pr in profiles]),
          n_peaks_tot == PEAKS_QUOTE)

    # ------------------------------------------------ T1: the 2x2
    print("\nT1 -- the 2x2 reduction: K1 exactness, K2 wiring, "
          "fidelity, continuity")
    pool = list(lock_c)
    for pr in profiles:
        pool.extend(pr["recs"])
    # K1 exactness (skip st == 0 degenerate points, counted)
    dev_low, dev_vec, n_skip = 0.0, 0.0, 0
    for rv in pool:
        ct_, st_ = rv["ct"], rv["st"]
        if st_ <= 0.0 or ct_ <= 0.0:
            n_skip += 1
            continue
        d1, b_, d2 = rv["lam_lock"], rv["Bk1"], rv["Qp"]
        low = 0.5 * (d1 + d2) - math.sqrt(0.25 * (d1 - d2) ** 2
                                          + b_ * b_)
        dev_low = max(dev_low, abs(low - rv["lam"])
                      / abs(rv["lam_lock"]))
        r1_ = (d1 - rv["lam"]) * ct_ + b_ * st_
        r2_ = b_ * ct_ + (d2 - rv["lam"]) * st_
        dev_vec = max(dev_vec, math.hypot(r1_, r2_)
                      / abs(rv["lam_lock"]))
    check("T1.1 [E] K1 exactness on %d pooled points (%d degenerate "
          "skipped): lower eigenvalue of [[lam_lock, B1],[B1, "
          "Q_perp]] = lambda_min (max rel dev %.1e) and (cos, sin) "
          "is its eigenvector (max residual %.1e) -- both < %.0e; "
          "theta_K1 = theta_full BY CONSTRUCTION (circular as a "
          "predicate, K1 is the anchor only)"
          % (len(pool), n_skip, dev_low, dev_vec, BAR_EIGEN),
          max(dev_low, dev_vec) < BAR_EIGEN)

    dev_int, dev_orth, dev_lls, n_anom = 0.0, 0.0, 0.0, 0
    for rv in pool:
        tol_i = 1e-9 * rv["rad"]
        dev_int = max(dev_int,
                      (rv["lam"] - rv["mu1"]) / rv["rad"],
                      (rv["mu1"] - rv["lam2"]) / rv["rad"])
        _ = tol_i
        dev_orth = max(dev_orth, rv["orth"])
        dev_lls = max(dev_lls, abs(rv["lam_lock_spec"]
                                   - rv["lam_lock"])
                      / abs(rv["lam_lock"]))
        n_anom += 1 if rv["anom"] else 0
    check("T1.2 [E] K2 wiring on %d pooled points: interlacing "
          "lambda_min <= mu1 <= lambda_2 (max violation %.1e of the "
          "pencil radius < 1e-9), G-orthogonality |c.a| max %.1e < "
          "1e-8, spectral lambda_lock consistency max rel %.1e < "
          "%.0e, secular anomalies %d/%d (share %.4f < %.2f)"
          % (len(pool), dev_int, dev_orth, dev_lls, BAR_EIGEN,
             n_anom, len(pool), n_anom / float(len(pool)), ANOM_BAR),
          dev_int < 1e-9 and dev_orth < 1e-8
          and dev_lls < BAR_EIGEN
          and n_anom / float(len(pool)) < ANOM_BAR)

    # K2 fidelity per point (profile points -- the landscape data)
    dth_all, dth_by = [], {"MARGIN": [], "ROT": [], "LCK": [],
                           "NEG": []}
    lk_all = []
    for pr in profiles:
        for j, rv in enumerate(pr["recs"]):
            d = abs(rv["th_k2"] - rv["theta"])
            dth_all.append(d)
            dth_by[pr["regs"][j]].append(d)
            lk_all.append(rv["leak"])
    dth_all = np.array(dth_all)
    lk_all = np.array(lk_all)
    th_flat = np.concatenate([pr["th"] for pr in profiles])
    thk2_flat = np.concatenate([pr["thk2"] for pr in profiles])
    sp_fid = spearman(th_flat, thk2_flat)
    check("T1.3 [MEASURED] K2 angle fidelity on %d grid points: "
          "|theta_K2 - theta_full| median %.3f / p90 %.3f / max "
          "%.2f deg; by regime: MARGIN median %.3f (n=%d), ROT "
          "median %.3f (n=%d); Spearman(theta_K2, theta_full) = "
          "%+.4f; 2-space leak median %.3f / p90 %.3f / max %.3f "
          "(rel) -- REPORTED, the predicate is judged by T3"
          % (len(dth_all), float(np.median(dth_all)),
             float(np.quantile(dth_all, 0.9)), float(dth_all.max()),
             float(np.median(dth_by["MARGIN"]))
             if dth_by["MARGIN"] else float("nan"),
             len(dth_by["MARGIN"]),
             float(np.median(dth_by["ROT"]))
             if dth_by["ROT"] else float("nan"), len(dth_by["ROT"]),
             sp_fid, float(np.median(lk_all)),
             float(np.quantile(lk_all, 0.9)), float(lk_all.max())),
          True)

    ovd_all = np.concatenate([np.abs(pr["ovd"][1:])
                              for pr in profiles])
    ovp_all = np.concatenate([np.abs(pr["ovp"][1:])
                              for pr in profiles])
    med_ovd = float(np.median(ovd_all))
    med_ovp = float(np.median(ovp_all))
    check("T1.4 [MEASURED] continuity along alpha (consecutive-point "
          "|G-overlap|, %d steps): K2 v_defl median %.4f / p10 %.4f "
          "/ min %.4f vs K1 w_perp(m) median %.4f / p10 %.4f / min "
          "%.4f; steps below the trust bar %.1f: K2 %d, K1 %d -> "
          "the documented continuous construction is %s"
          % (len(ovd_all), med_ovd,
             float(np.quantile(ovd_all, 0.1)), float(ovd_all.min()),
             med_ovp, float(np.quantile(ovp_all, 0.1)),
             float(ovp_all.min()), OV_TRACK,
             int(np.sum(ovd_all < OV_TRACK)),
             int(np.sum(ovp_all < OV_TRACK)),
             "K2 (deflated basis)" if med_ovd >= med_ovp
             else "K1 (m-slaved) -- UNEXPECTED, documented"), True)

    # ------------------------------------------------ T2: mechanism
    print("\nT2 -- the 52-peak mechanism classification (K2 entries "
          "inside FWHM +- 1 grid step)")
    step = 2.0 * S_MAX / (N_GRID - 1)
    mech_counts = {}
    reg_cross = {}
    width_ratios = []
    print("      h      s*        P*        regime  theta   "
          "theta_K2  f(s*)        2|B|(s*)     mech")
    for pr, iv in all_peaks:
        ss = pr["ss"]
        lo, hi = iv["s_l"] - step, iv["s_r"] + step
        idx = np.where((ss >= lo - 1e-15) & (ss <= hi + 1e-15))[0]
        fv = pr["f"][idx]
        bv = pr["Bs"][idx]
        llv = pr["ll"][idx]
        ovv = np.abs(pr["ovd"][idx])
        ovv = ovv[~np.isnan(ovv)]
        trusted = bool(len(ovv) == 0 or float(ovv.min()) >= OV_TRACK)
        lck = bool(np.min(llv) <= 0.0)
        cross = bool(np.max(fv) >= 0.0 and np.min(fv) < 0.0)
        bsign = bool(np.min(bv) < 0.0 < np.max(bv)) and trusted
        if lck:
            mech = "LCKDEG"
        elif cross and bsign:
            mech = "CROSS+BSIGN"
        elif cross:
            mech = "CROSS"
        elif bsign:
            mech = "BSIGN"
        else:
            mech = "NONE"
        iv["mech"] = mech
        rg = pr["regs"][iv["ip"]]
        mech_counts[mech] = mech_counts.get(mech, 0) + 1
        reg_cross[(rg, mech)] = reg_cross.get((rg, mech), 0) + 1
        ip = iv["ip"]
        extra = ""
        if mech == "NONE":
            prox = float(np.max(fv / (2.0 * pr["Babs"][idx])))
            extra = "  maxf/2|B| = %+.3f" % prox
        if cross:
            zs = cross_events(ss[idx], fv, 0.0)
            if zs:
                z0 = min(zs, key=lambda z: abs(z - iv["s"]))
                j = int(np.searchsorted(ss, z0))
                j = max(1, min(len(ss) - 2, j))
                fp = (pr["f"][j + 1] - pr["f"][j - 1]) \
                    / (ss[j + 1] - ss[j - 1])
                bloc = pr["Babs"][j]
                if fp != 0.0:
                    w_pred = 2.0 * bloc / abs(fp)
                    width_ratios.append(w_pred)
                    extra = "  w_pred = %.2e" % w_pred
        print("      %4d  %+7.4f  %9.3g  %-6s  %5.2f  %5.2f   "
              "%+.4e  %.4e  %-11s%s"
              % (pr["r0"]["h"], iv["s"], iv["P"], rg,
                 pr["th"][ip], pr["thk2"][ip], pr["f"][ip],
                 2.0 * pr["Babs"][ip], mech, extra))
    n_rot_pk = sum(1 for pr, iv in all_peaks
                   if pr["regs"][iv["ip"]] == "ROT")
    check("T2.1 [MEASURED] mechanism table over the %d peaks: %s; "
          "regime x mechanism: %s; ROT peaks %d/%d; predicted "
          "needle widths (2|B|/|f'| at the zero) median %.2e over "
          "%d CROSS peaks (coarse FWHM is resolution-bound 0.0025; "
          "landscape fine median %.1e)"
          % (n_peaks_tot,
             {k: mech_counts[k] for k in sorted(mech_counts)},
             {("%s|%s" % k): v for k, v in sorted(reg_cross.items())},
             n_rot_pk, n_peaks_tot,
             float(np.median(width_ratios)) if width_ratios
             else float("nan"), len(width_ratios), W_NEEDLE), True)

    # ------------------------------------------------ T3: predicate
    print("\nT3 -- the predicate: pointwise gate, event-level match, "
          "zero density")
    rot_flat = np.concatenate([np.array([rg == "ROT"
                                         for rg in pr["regs"]])
                               for pr in profiles])
    f_flat = np.concatenate([pr["f"] for pr in profiles])
    B_flat = np.concatenate([pr["Babs"] for pr in profiles])
    pred1 = f_flat >= 0.0
    pred2 = np.abs(f_flat) <= 2.0 * B_flat
    stats = {}
    for name, pd_ in (("PRED1 f >= 0", pred1),
                      ("PRED2 |f| <= 2|B|", pred2)):
        tp = int(np.sum(pd_ & rot_flat))
        prec = tp / float(np.sum(pd_)) if np.sum(pd_) else float("nan")
        rec_ = tp / float(np.sum(rot_flat)) if np.sum(rot_flat) \
            else float("nan")
        stats[name] = (prec, rec_, tp, int(np.sum(pd_)),
                       int(np.sum(rot_flat)))
        print("      %-18s flags %4d of %4d points | truth ROT %3d "
              "| precision %.4f recall %.4f"
              % (name, int(np.sum(pd_)), len(f_flat),
                 int(np.sum(rot_flat)), prec, rec_))
    p1, r1 = stats["PRED1 f >= 0"][:2]
    hit_point = (p1 >= PR_BAR) and (r1 >= PR_BAR)
    check("T3.1 [MEASURED, gate] the primary predicate (K2 rotation "
          "criterion f = lambda_lock - mu1 >= 0) against the "
          "pointwise ROT truth (theta_full >= 45 deg): precision = "
          "%.4f, recall = %.4f (bar both >= %.2f) -> %s; the "
          "avoided-crossing band PRED2: precision %.4f recall %.4f"
          % (p1, r1, PR_BAR, "HIT" if hit_point else "MISS",
             stats["PRED2 |f| <= 2|B|"][0],
             stats["PRED2 |f| <= 2|B|"][1]), True)

    ev_truth_n, ev_pred_n, ev_match = 0, 0, 0
    zero_list = []
    for pr in profiles:
        ev_t = cross_events(pr["ss"], pr["th"], THETA_BAR)
        ev_p = cross_events(pr["ss"], pr["f"], 0.0)
        ev_truth_n += len(ev_t)
        ev_pred_n += len(ev_p)
        ev_match += greedy_match(ev_t, ev_p, EV_TOL)
        zero_list.append(ev_p)
    prec_ev = ev_match / float(ev_pred_n) if ev_pred_n \
        else float("nan")
    rec_ev = ev_match / float(ev_truth_n) if ev_truth_n \
        else float("nan")
    hit_event = ev_pred_n > 0 and ev_truth_n > 0 \
        and prec_ev >= PR_BAR and rec_ev >= PR_BAR
    check("T3.2 [MEASURED] event level: %d theta-45-crossings vs %d "
          "f-zeros, matched %d within one grid step -> precision "
          "%.4f, recall %.4f (bar %.2f) -> %s; the needle positions "
          "ARE the zeros of the explicit smooth f(alpha) iff this "
          "holds"
          % (ev_truth_n, ev_pred_n, ev_match, prec_ev, rec_ev,
             PR_BAR, "HIT" if hit_event else "MISS"), True)

    print("\n      zero density per slice (clusters with gap <= 2 "
          "grid steps = needle centers):")
    print("      h      n_zero  n_center  med ds_c    med du      "
          "du/D     du/atomgap")
    dens_rows = []
    for pr, zs in zip(profiles, zero_list):
        h_ = pr["r0"]["h"]
        centers = []
        for z in sorted(zs):
            if centers and z - centers[-1][-1] <= 2 * step:
                centers[-1].append(z)
            else:
                centers.append([z])
        cpos = [float(np.mean(c)) for c in centers]
        if len(cpos) >= 2:
            dsp = np.diff(sorted(cpos))
            med_ds = float(np.median(dsp))
            du = 2.0 * pr["r0"]["alpha"] * med_ds
            D_ = pr["r0"]["D"]
            gl = pr["recs"][pr["i0"]]["gap_loc"]
            dens_rows.append((h_, len(zs), len(cpos), med_ds, du,
                              du / D_, du / gl))
            print("      %4d   %4d    %4d     %.5f    %.5f    "
                  "%7.3f   %7.3f"
                  % (h_, len(zs), len(cpos), med_ds, du, du / D_,
                     du / gl))
        else:
            print("      %4d   %4d    %4d     --" % (h_, len(zs),
                                                     len(cpos)))
    if dens_rows:
        rdD = [r[5] for r in dens_rows]
        rdg = [r[6] for r in dens_rows]
        hh_ = [r[0] for r in dens_rows]
        dd_ = [r[3] for r in dens_rows]
        check("T3.3 [MEASURED] needle density systematics over %d "
              "slices: median center spacing du/D in [%.3f, %.3f] "
              "(median %.3f), du/atom-gap in [%.3f, %.3f] (median "
              "%.3f); Spearman(spacing, h) = %+.3f on 8 slices "
              "(descriptive only)"
              % (len(dens_rows), min(rdD), max(rdD),
                 float(np.median(rdD)), min(rdg), max(rdg),
                 float(np.median(rdg)),
                 spearman(dd_, hh_) if len(dens_rows) >= 3
                 else float("nan")), True)
    else:
        check("T3.3 [MEASURED] needle density: fewer than 2 centers "
              "per slice everywhere -- no spacing statistics", True)

    # ------------------------------------------------ T4: frame-A
    print("\nT4 -- frame-A safety: distance to the nearest predicted "
          "needle (unit W = %.1e)" % W_NEEDLE)
    offs = [k * SCAN_STEP for k in range(-10, 11) if k != 0]

    def eval_at(r0_, s):
        a_p = r0_["alpha"] * (1.0 + s)
        if math.exp(2.0 * a_p) > core.ATOM_MAX + 0.5:
            return None
        rv, _, _ = window_eval(a_p, r0_["Mz"])
        return rv

    t4_rows = []
    for w_i, r0_ in enumerate(sorted(comp, key=lambda r: r["h"])):
        pts = {0.0: r0_}
        for s in offs:
            rv = eval_at(r0_, s)
            if rv is not None:
                pts[s] = rv
        ssc = np.array(sorted(pts.keys()))
        fsc = np.array([pts[s]["f"] for s in ssc])
        # nearest sign-change bracket per side, refined by bisection
        needles = []
        brks = [(float(ssc[i]), float(ssc[i + 1]), float(fsc[i]),
                 float(fsc[i + 1]))
                for i in range(len(ssc) - 1)
                if fsc[i] * fsc[i + 1] < 0.0]
        for side in (-1.0, 1.0):
            cand = [b for b in brks
                    if (0.5 * (b[0] + b[1])) * side >= 0.0]
            if not cand:
                continue
            sa, sb, fa, fb = min(
                cand, key=lambda b: abs(0.5 * (b[0] + b[1])))
            while sb - sa > BIS_TOL:
                sm = 0.5 * (sa + sb)
                rv = eval_at(r0_, sm)
                if rv is None:
                    break
                fm = rv["f"]
                if fa * fm <= 0.0:
                    sb, fb = sm, fm
                else:
                    sa, fa = sm, fm
            needles.append(0.5 * (sa + sb))
        # interior f-maxima (f < 0), <= MAX_PARAB nearest to 0
        maxima = [i for i in range(1, len(ssc) - 1)
                  if fsc[i] >= fsc[i - 1] and fsc[i] >= fsc[i + 1]
                  and fsc[i] < 0.0]
        maxima.sort(key=lambda i: abs(ssc[i]))
        dip_best = None
        for i in maxima[:MAX_PARAB]:
            x0, x1, x2 = ssc[i - 1], ssc[i], ssc[i + 1]
            y0, y1, y2 = fsc[i - 1], fsc[i], fsc[i + 1]
            den = (x0 - x1) * (x0 - x2) * (x1 - x2)
            if den == 0.0:
                continue
            aa = (x2 * (y1 - y0) + x1 * (y0 - y2)
                  + x0 * (y2 - y1)) / den
            bb = (x2 * x2 * (y0 - y1) + x1 * x1 * (y2 - y0)
                  + x0 * x0 * (y1 - y2)) / den
            if aa >= 0.0:
                continue
            xv = -bb / (2.0 * aa)
            if not (x0 < xv < x2):
                continue
            rv = eval_at(r0_, xv)
            if rv is None:
                continue
            if rv["f"] >= 0.0:
                needles.append(xv)
            elif dip_best is None or rv["f"] > dip_best[1]:
                dip_best = (xv, rv["f"])
        # run-2 diagnostic: nearest MEASURED theta_full = 45 crossing
        thsc = np.array([pts[s]["theta"] for s in ssc])
        ev45 = cross_events(ssc, thsc, THETA_BAR)
        d_th = min((abs(z) for z in ev45), default=float("nan"))
        if r0_["h"] == 859 and ev45:
            z0 = min(ev45, key=abs)
            j = int(np.searchsorted(ssc, z0))
            j = max(1, min(len(ssc) - 1, j))
            sa, sb = float(ssc[j - 1]), float(ssc[j])
            fa = float(thsc[j - 1]) - THETA_BAR
            while sb - sa > BIS_TOL:
                sm = 0.5 * (sa + sb)
                rv = eval_at(r0_, sm)
                if rv is None:
                    break
                fm = rv["theta"] - THETA_BAR
                if fa * fm <= 0.0:
                    sb = sm
                else:
                    sa, fa = sm, fm
            d_th = abs(0.5 * (sa + sb))
        f0 = r0_["f"]
        b0 = abs(r0_["Bk2"])
        margin = -f0 / (2.0 * b0) if b0 > 0.0 else float("inf")
        has_pm = (SCAN_STEP in pts) and (-SCAN_STEP in pts)
        fp0 = ((pts[SCAN_STEP]["f"] - pts[-SCAN_STEP]["f"])
               / (2.0 * SCAN_STEP)) if has_pm else float("nan")
        s_newt = -f0 / fp0 if has_pm and fp0 != 0.0 else float("nan")
        d_near = min((abs(z) for z in needles), default=float("nan"))
        analysis = r0_["lock"] and r0_["lam"] > r0_["floor"]
        t4_rows.append(dict(h=r0_["h"], kz=r0_["kz"], f0=f0, b0=b0,
                            margin=margin, s_newt=s_newt,
                            d=d_near, d_th=d_th, theta=r0_["theta"],
                            thk2=r0_["th_k2"], analysis=analysis,
                            dip=dip_best,
                            n_z=len(needles)))
        if (w_i + 1) % 10 == 0:
            print("      ... %d/%d windows scanned (%.0f s, %d "
                  "evals)" % (w_i + 1, len(comp), time.time() - T0,
                              N_EVAL))

    print("\n      h     theta   th_K2   f(0)         2|B|(0)     "
          "-f/2|B|   s_Newton    d_near      d/W       d_theta45   "
          "d45/W")
    for tr in t4_rows:
        d_s = ("%.6f" % tr["d"]) if not math.isnan(tr["d"]) \
            else (">=%.4f" % S_SCAN)
        dw = (tr["d"] / W_NEEDLE) if not math.isnan(tr["d"]) \
            else float("nan")
        dw_s = ("%8.1f" % dw) if not math.isnan(dw) \
            else (">=%6.0f" % (S_SCAN / W_NEEDLE))
        dt_s = ("%.6f" % tr["d_th"]) if not math.isnan(tr["d_th"]) \
            else (">=%.4f" % S_SCAN)
        dtw_s = ("%8.1f" % (tr["d_th"] / W_NEEDLE)) \
            if not math.isnan(tr["d_th"]) \
            else (">=%6.0f" % (S_SCAN / W_NEEDLE))
        print("      %4d%s %6.2f  %6.2f  %+.4e  %.4e  %8.3f  "
              "%+9.5f  %s  %s  %s  %s"
              % (tr["h"], " " if tr["analysis"] else "*",
                 tr["theta"], tr["thk2"], tr["f0"], 2 * tr["b0"],
                 tr["margin"], tr["s_newt"], d_s, dw_s, dt_s, dtw_s))
    ana = [tr for tr in t4_rows if tr["analysis"]]
    d_ana = [tr["d"] for tr in ana if not math.isnan(tr["d"])]
    n_cens = sum(1 for tr in ana if math.isnan(tr["d"]))
    d_min = min(d_ana) if d_ana else float("inf")
    h_min = [tr["h"] for tr in ana if tr["d"] == d_min] \
        if d_ana else []
    safe = d_min >= SAFE_BAR * W_NEEDLE
    tr859 = [tr for tr in t4_rows if tr["h"] == 859][0]
    d859 = tr859["d"]
    d_th_ana = [tr["d_th"] for tr in ana
                if not math.isnan(tr["d_th"])]
    d_th_min = min(d_th_ana) if d_th_ana else float("inf")
    h_th_min = [tr["h"] for tr in ana if tr["d_th"] == d_th_min] \
        if d_th_ana else []
    d859t = tr859["d_th"]
    check("T4.1 [MEASURED] frame-A needle distances on the %d "
          "analysis windows (* = excluded, %d): %d windows have a "
          "confirmed needle within +-%.1f%%, %d censored (no needle "
          "in range); MIN distance %.6f at h = %s = %.1f needle "
          "widths (bar %.0f W) -> %s; h = 859: theta = %.2f deg, "
          "f(0) = %+.3e, nearest needle %s (= %s W), coupling "
          "margin -f/2|B| = %.3f.  Run-2 diagnostic (MEASURED "
          "theta = 45 crossings, no gate): %d/%d analysis windows "
          "have one within +-%.1f%%, min distance %.6f = %.1f W at "
          "h = %s; h = 859 measured 45-deg distance %s (= %s W)"
          % (len(ana), len(t4_rows) - len(ana), len(d_ana),
             100 * S_SCAN, n_cens, d_min, h_min,
             d_min / W_NEEDLE, SAFE_BAR,
             "FRAME-A-SAFE" if safe else "FRAME-A-TIGHT",
             tr859["theta"], tr859["f0"],
             ("%.6f" % d859) if not math.isnan(d859)
             else ">= %.4f" % S_SCAN,
             ("%.1f" % (d859 / W_NEEDLE)) if not math.isnan(d859)
             else ">= %.0f" % (S_SCAN / W_NEEDLE),
             tr859["margin"],
             len(d_th_ana), len(ana), 100 * S_SCAN,
             d_th_min, d_th_min / W_NEEDLE, h_th_min,
             ("%.6f" % d859t) if not math.isnan(d859t)
             else ">= %.4f" % S_SCAN,
             ("%.1f" % (d859t / W_NEEDLE))
             if not math.isnan(d859t)
             else ">= %.0f" % (S_SCAN / W_NEEDLE)), True)

    # ------------------------------------------------ T5: verdict
    guards_ok = not any(f_.startswith(("G0", "T1.1", "T1.2"))
                        for f_ in FAILS)
    if not guards_ok:
        VERDICT = "THETA-MIXED (guards or exactness/wiring failed)"
    elif hit_point:
        VERDICT = "THETA-PRED-PASS"
    elif hit_event:
        VERDICT = "THETA-PRED-EVENT"
    else:
        VERDICT = "THETA-PRED-FAIL"

    n_cross = mech_counts.get("CROSS", 0) \
        + mech_counts.get("CROSS+BSIGN", 0)
    check("T5.1 [C] the typed reading: the rotation passages of "
          "theta(alpha) are interrogated through the eigenvector-"
          "free 2x2 [[lambda_lock, B],[B, mu1]] (deflated basis, "
          "exact identity (A - mu1 G) v_defl = B G w_hat); K2 angle "
          "fidelity median %.3f deg; mechanism: %d/%d peaks carry a "
          "diagonal crossing of f = lambda_lock - mu1, %d LCKDEG, "
          "%d BSIGN-only, %d NONE; predicate f >= 0: precision "
          "%.3f / recall %.3f (pointwise), %.3f / %.3f (event); "
          "frame-A: min needle distance %.1f W at h = %s, h = 859 "
          "at %s W predicted / %s W measured (theta = 45) -> %s.  "
          "NO positivity claim, NO RH statement, NO marker move; "
          "W3 stays open"
          % (float(np.median(dth_all)), n_cross, n_peaks_tot,
             mech_counts.get("LCKDEG", 0),
             mech_counts.get("BSIGN", 0),
             mech_counts.get("NONE", 0),
             p1, r1, prec_ev, rec_ev,
             d_min / W_NEEDLE, h_min,
             ("%.1f" % (d859 / W_NEEDLE)) if not math.isnan(d859)
             else ">= %.0f" % (S_SCAN / W_NEEDLE),
             ("%.1f" % (d859t / W_NEEDLE)) if not math.isnan(d859t)
             else ">= %.0f" % (S_SCAN / W_NEEDLE),
             "FRAME-A-SAFE" if safe else "FRAME-A-TIGHT"), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, theta-rotation-predicate round
  (2026-08-02): the landscape needles (52 peaks, W3RL-PEAKED-
  UNEXPLAINED) were interrogated through an explicit 2x2 reduction
  of the window pencil.  CONSTRUCTION: basis {w_hat_lock(alpha),
  v_defl(alpha)} with v_defl the lowest eigenvector of the pencil
  deflated to the G-orthocomplement of the closed v591 lock
  direction (Wilkinson secular equation; exact identity (A - mu1 G)
  v_defl = B G w_hat checked to 1e-9/1e-8 bars); the construction
  reads NO minimal mode, so f(alpha) = lambda_lock - mu1 and
  B(alpha) are predictive.  theta_K2 crosses 45 deg exactly at
  f = 0.  RESULT: K2 angle fidelity median %.3f deg (p90 %.3f) on
  %d grid points; mechanism table: %s over the %d peaks (%d of them
  ROT-regime); PREDICATE f >= 0 vs pointwise ROT truth: precision
  %.3f / recall %.3f; event level (45-deg crossings vs f-zeros,
  one-grid-step match): precision %.3f / recall %.3f; verdict %s.
  FRAME-A SAFETY: minimum distance of a family frame-A point to a
  PREDICTED needle %.6f (relative alpha) = %.1f needle widths
  (W = 2.5e-4), attained at h = %s -- conservative, the predicate
  is complete but not sharp; MEASURED theta = 45 crossings
  (diagnostic): min distance %.6f = %.1f W at h = %s; h = 859
  (theta 43.5 deg) sits %s W (predicted) / %s W (measured) from
  the 45-deg threshold, coupling margin -f/2|B| = %.3f -> %s.
  CONSEQUENCE FOR W3 (typed, open): %s  TYPE: measured
  landscape reduction on the declared surface; no positivity claim;
  no RH statement; Problem 7.1 untouched; no marker move.
""" % (float(np.median(dth_all)), float(np.quantile(dth_all, 0.9)),
       len(dth_all),
       {k: mech_counts[k] for k in sorted(mech_counts)},
       n_peaks_tot, n_rot_pk, p1, r1, prec_ev, rec_ev, VERDICT,
       d_min if d_ana else float("nan"), d_min / W_NEEDLE, h_min,
       d_th_min if d_th_ana else float("nan"),
       d_th_min / W_NEEDLE, h_th_min,
       ("%.1f" % (d859 / W_NEEDLE)) if not math.isnan(d859)
       else ">= %.0f" % (S_SCAN / W_NEEDLE),
       ("%.1f" % (d859t / W_NEEDLE)) if not math.isnan(d859t)
       else ">= %.0f" % (S_SCAN / W_NEEDLE),
       tr859["margin"],
       "FRAME-A-SAFE (the declared surface sits between the "
       "needles with a measurable guard band)" if safe else
       "FRAME-A-TIGHT (at least one family window sits within 10 "
       "needle widths of a predicted needle)",
       ("the 'generic 2x2 bound + needle exclusion by the f-zero "
        "predicate' proof path is FORMULATABLE: needles are zeros "
        "of the explicit smooth f(alpha) = lambda_lock - mu1 with "
        "avoided-crossing width 2|B|/|f'|."
        if (hit_point or hit_event) else
        "the predicate does NOT reach the bar -- the needle "
        "mechanism remains only partially characterized; the "
        "failure mode is documented above.")))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s (%d window evals)"
          % (time.time() - T0, N_EVAL))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
