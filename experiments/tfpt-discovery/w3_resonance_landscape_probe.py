"""Discovery probe: THE W3 RESONANCE LANDSCAPE -- mapping P(alpha) =
q tan^2 theta around the frame-A points of the window family.

CONTEXT.  w3_uniform_bound_probe (2026-08-02) typed the reduced W3
obstruction (P = q tan^2 theta <= 1 - delta uniformly) and returned
W3UB-FRAGILE: at fixed h the alpha-shift moves P by up to ~60% at
+-5% -- P is a THIN RESONANCE of the frame-A alpha <-> h coupling,
not a smooth depth function.  THIS probe maps that landscape.  If
P > 1 - delta lives only on a thin exceptional set in alpha-space,
W3 can be reformulated as "generically small + exception control"
instead of "uniformly small".  The probe makes NO positivity claim,
NO uniform-bound claim and NO RH statement; it measures a landscape.

CALIBRATION HISTORY (declared -- honesty first): run 1 (2026-08-02)
passed all guards and found 52 peaks, but (i) the median coarse FWHM
came out EQUAL to the grid step (0.0025) -- the widths were
resolution-limited -- and (ii) the profiles carry values P >> 1 (up
to 2e7) at points where the lock identification itself degenerates
(theta -> 90 deg or lambda_lock -> 0), which the run-1 share metrics
counted as exceedances although P is NOT the positivity criterion
there.  THIS version adds, WITHOUT touching any run-1 gate or the
verdict logic: (a) a ZOOM stage R1b (step 0.025%, +-0.75% around at
most 2 declared peaks per slice: the peak nearest the frame-A point
and the highest peak) for resolution-corrected FWHM; (b) a REGIME
type per grid point -- NEG (lambda_min < -floor, the realized margin
loss), ROT (theta >= 45 deg), LCK (lambda_lock <= 0), MARGIN
(otherwise; there P < 1 <=> lambda_min > 0) -- with regime-
restricted share columns and the direct lambda_min < -floor count
per slice; (c) a PRINTED margin-regime R2 diagnostic (no gate).
Run-1 also observed the frame-A rank mean 0.242 (LOW side of the
profile) -- reported post-hoc, not gated.

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * base sweep: the w3_uniform_bound analysis sample verbatim
    (complete frame-A windows, lock sign q_real q_model > 0,
    lambda_min above the float floor FLOOR_SAFETY x eps x radius x
    sqrt(h)); guards: the surface (67 complete, truncated {1219,
    1292, 1445}); the rid anchors max P = 0.9636 at h = 859 (tol
    0.005), Spearman(P, h) = +0.735 (tol 0.03), Spearman(r_id, h) =
    -0.784 (tol 0.03), median r_id 0.584 (tol 0.005), median theta
    9.1 deg (tol 0.15); the closed formula per window (< 1e-6) with
    structural q > 1, theta < 45 deg, P < 1;
  * slice choice (8 windows): the top-4 windows by P -- guarded to
    be {859, 363, 1430, 1393} (the w3ub A2 top list) -- plus 4
    UNREMARKABLE windows picked by h-quantiles q = 0.15/0.40/0.60/
    0.85 among the REMAINING lock-sign complete windows (nearest h,
    duplicates skipped);
  * grid: relative alpha-shift s in [-10%, +10%], N_GRID = 81 points
    (step 0.25%), the center forced to s = 0 exactly; Mz FIXED per
    window (the w3ub A3 variant machinery verbatim); only atom-
    complete configurations e^{2 alpha'} <= ATOM_MAX + 0.5 are built
    (feasibility is reported, not forced; the infeasible set is a
    suffix in s, so every profile stays contiguous); hz-only objects
    (parity basis, lag weights) are cached -- numerically identical,
    keyed by h;
  * wiring guards: the s = 0 rebuild reproduces the base-sweep P to
    1e-12 on EVERY selected window; the h = 859 profile reproduces
    the w3ub A3 FRAGILE read (max over s in {+-2.5%, +-5%} of
    |P(s) - P(0)|/P(0) > 0.15);
  * R1 profile metrics per slice: median P, shares of the feasible
    grid with P > 0.5 / 0.8 / 0.9 / 0.95; PEAK SET = interior local
    maxima with P >= P_PEAK_BAR = 0.8 (boundary maxima with P >= 0.8
    typed CENSORED); FWHM per peak at the half-prominence level
    P_base + 0.5 (P_peak - P_base), P_base = profile median, with
    linear interpolation at the crossings (censored crossings report
    >=-widths); the quantile rank of the frame-A point P(0) inside
    its own profile; distance s = 0 -> nearest peak center and the
    boolean "frame-A inside a FWHM interval";
  * R1 construction-bias read: mean quantile rank of P(0) over the 4
    UNREMARKABLE slices against the uniform null (mean 0.5, SD =
    sqrt(1/(12 x 4)) = 0.1443); BIASED iff mean rank >= 0.7374 (one-
    sided 95%); the top-4 ranks are reported but EXCLUDED from the
    test (selection-conditioned by construction);
  * R2 resonance-condition candidates, frozen per grid point:
      (a) edge-atom alignment   score_a = min_n |2 alpha - u_n| / D
          (declared caveat: the atom set is DENSE at depth -- the
          local u-gap ~ 2 alpha e^{-2 alpha} can be far below D, so
          score_a may be degenerate; measured ranges are printed),
      (b) heavy-atom commensurability   score_b = the mu-weighted
          mean of dist(u_j/D, Z) over the K_HEAVY = 12 globally
          heaviest atoms (mu = 2 Lambda(n)/sqrt(n)); the p = 2/3/5/7
          offsets are printed per peak as a diagnostic,
      (c) DST edge-band coupling   score_c = share of the w_perp DST
          mass at k > 0.8 h (the garding_probe lattice edge band);
    peak-region label = grid point inside a FWHM interval; pooled
    association per candidate = Spearman(score, label) with CYCLIC-
    SHIFT permutation inside each profile (B = 5000; declared: plain
    permutation would be anticonservative under smooth profiles) and
    precision@prevalence (top-N points by resonance-favoring score,
    N = number of peak-region points; there precision = recall);
    HIT gate per candidate: precision@prevalence >= max(0.5, 2 x
    prevalence) AND p < 0.01 AND the sign matches the declared
    direction (a: LOW at peaks, b: LOW at peaks, c: HIGH at peaks);
  * R3 measure estimate: per-slice feasible-grid shares with P >
    1 - delta for delta = 0.05 / 0.2 / 0.5, aggregated (i) over all
    8 slices and (ii) over the 4 UNREMARKABLE slices alone -- the
    honest estimate, since the top-4 are conditioned on high P;
    uncertainty by SLICE BOOTSTRAP (B = 10000, seed 20260809):
    resample slices with replacement, mean of per-slice shares,
    5-95% band; the slices are 8 cuts of a 2D landscape -- the
    statement is about the SURVEYED region, nothing deeper;
  * R4 typing only: contract-note text printed; no marker move.

Verdict enums (frozen, precedence top-down): W3RL-MIXED (guards or
wiring fail), W3RL-SMOOTH (no peak on any profile), W3RL-PEAKED-
ARITHMETIC (>= 1 R2 candidate passes the HIT gate), W3RL-PEAKED-
UNEXPLAINED (peaks exist, no candidate passes).

FIREWALL: experiments-only; verification/ read-only (v563 import;
v618/v591/rid/w3ub machinery REBUILT verbatim, no other imports); no
marker moves; no positivity claim; no RH statement; NO zero of any
L-function is read (AST-checked).  Python-only, per GATE.WOLFRAM.02.

Provenance: w3_uniform_bound_probe (2026-08-02, W3UB-FRAGILE + the
A3 alpha-shift machinery), rid_alignment_probe (closed formula
P = q tan^2 theta), garding_probe (lattice edge-band read),
v618 (C = 1 reads), v591 (lock direction), v637 (control ethos).
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
SEED = 20260809              # fresh (w3ub probe used 20260808)
N_GRID = 81                  # grid points over +-10% (step 0.25%)
S_MAX = 0.10
P_PEAK_BAR = 0.80            # peak height bar (= 1 - delta, delta 0.2)
K_HEAVY = 12                 # heaviest atoms for score_b
B_PERM = 5000                # cyclic-shift permutation budget
B_SLICE = 10000              # slice bootstrap budget
P_BAR = 0.01                 # permutation p gate
RANK_BIAS_BAR = 0.5 + 1.6448536269514722 * math.sqrt(1.0 / 48.0)
QUANTS = (0.15, 0.40, 0.60, 0.85)
TOP4_QUOTE = {859, 363, 1430, 1393}
DELTAS = (0.05, 0.2, 0.5)    # R3 thresholds P > 1 - delta
SHARE_THRESH = (0.5, 0.8, 0.9, 0.95)
A3_SHIFT_IDX = (-20, -10, 10, 20)   # +-5%, +-2.5% at step 0.25%
STAB_BAR = 0.15              # w3ub A3 bar, verbatim
ZOOM_HALF = 0.0075           # run-2 zoom half-width (+-0.75%)
N_ZOOM = 61                  # run-2 zoom points (step 0.025%)
THETA_BAR = 45.0             # regime bar (deg): tan^2 flips at 45
# reproduction anchors (rid/w3ub quotes, verbatim)
P_MAX_QUOTE, P_MAX_TOL = 0.9636, 0.005
H_AT_PMAX = 859
SP_P_H_QUOTE, SP_TOL = 0.735, 0.03
SP_RID_H_QUOTE = -0.784
RID_MED_QUOTE, RID_TOL = 0.584, 0.005
THETA_MED_QUOTE = 9.1
BAR_EIGEN = 1e-6
BAR_REBUILD = 1e-12


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


def gen_min_eig2(A, G):
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    return float(w[0]), float(w[1]), V[:, 0], rad


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
U_MAX = None
U_HEAVY = None
MU_HEAVY = None
U_SMALLP = None


def hz_objects(hz):
    """Parity basis and lag weights depend on hz ONLY -- caching them
    is numerically identical to the w3ub verbatim rebuild.  The cache
    holds ONE hz (memory bound: Bfull is hz x hz)."""
    if hz not in _HZ_CACHE:
        Tb = core.parity_basis(hz, 2)
        t1v, t2v = Tb[0].copy(), Tb[1].copy()
        W11 = core.lag_weights_from_v(t1v, hz)
        W22 = core.lag_weights_from_v(t2v, hz)
        Wpp = core.lag_weights_from_v(t1v + t2v, hz)
        W12 = 0.5 * (Wpp - W11 - W22)
        Bfull = core.parity_basis(hz)
        _HZ_CACHE.clear()
        _HZ_CACHE[hz] = (t1v, t2v, W11, W22, W12, Bfull)
    return _HZ_CACHE[hz]


# ------------------------------------------------------ window builder
def window_eval(alpha, Mz):
    """One window at EXPLICIT (alpha, Mz): the w3_uniform_bound A3
    variant body verbatim (hz-only objects cached), extended by the
    frozen R2 candidate scores."""
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
    lam_min, lam_2, v_min, rad = gen_min_eig2(A, Gm)
    floor = FLOOR_SAFETY * EPS * rad * math.sqrt(hz)
    # v618 lock read (verbatim route)
    t1v, t2v, W11, W22, W12, Bfull = hz_objects(hz)
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
    # rid geometry: G-orthonormal split of the minimal mode
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
    t2 = (st / ct) ** 2
    qq = Q_perp / lam_lock
    # w_perp DST edge-band share (garding lattice edge band read)
    coef2 = (Bfull @ w_perp) ** 2
    tot = float(coef2.sum())
    kk = np.arange(1, hz + 1, dtype=float)
    dst_hi = float(coef2[kk > 0.8 * hz].sum()) / tot
    dst_cen = float((kk * coef2).sum()) / tot / hz
    # ---- R2 candidate scores (this probe's frozen additions)
    d_lo = 2.0 * alpha - float(core.U_ALL[ka - 1])
    d_hi = (float(core.U_ALL[ka]) - 2.0 * alpha) \
        if ka < len(core.U_ALL) else math.inf
    score_a = min(d_lo, d_hi) / D
    off_h = np.abs(U_HEAVY / D - np.round(U_HEAVY / D))
    score_b = float((MU_HEAVY * off_h).sum() / MU_HEAVY.sum())
    off_sp = np.abs(U_SMALLP / D - np.round(U_SMALLP / D))
    gap_loc = float(core.U_ALL[min(ka + 4, len(core.U_ALL) - 1)]
                    - core.U_ALL[ka - 5]) / 9.0
    return dict(h=hz, alpha=alpha, D=D, complete=complete,
                lam=lam_min, lam2=lam_2, floor=floor, qr=q_r, qm=q_m,
                lock=q_r * q_m > 0.0, ct=ct, st=st, t2=t2, qq=qq,
                P=qq * t2, lam_lock=lam_lock, rid=lam_min / lam_lock,
                theta=math.degrees(math.acos(ct)),
                dst_hi=dst_hi, dst_cen=dst_cen,
                score_a=score_a, score_b=score_b,
                off_smallp=off_sp, gap_loc=gap_loc)


# ------------------------------------------------------ peak analysis
def detect_peaks(ss, Pv_):
    """Interior local maxima with P >= P_PEAK_BAR; boundary maxima
    with P >= bar are typed CENSORED.  Returns list of (idx, kind)."""
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
    """Half-prominence interval around peak ip; linear interpolation
    at the crossings; censored ends flagged."""
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
    """Frozen run-2 regime type of one grid point (precedence
    top-down): NEG = realized margin loss; ROT/LCK = the lock
    identification degenerates and P is NOT the criterion; MARGIN =
    the clean regime where P < 1 <=> lambda_min > 0."""
    if rv["lam"] < -rv["floor"]:
        return "NEG"
    if rv["theta"] >= THETA_BAR:
        return "ROT"
    if rv["lam_lock"] <= 0.0:
        return "LCK"
    return "MARGIN"


def prec_at_prev(score, label, low_favors):
    N = int(label.sum())
    order = np.argsort(score if low_favors else -score,
                       kind="mergesort")
    return float(label[order[:N]].mean())


def run():
    global N_CHK, FAILS, U0_GRID, U_MAX, U_HEAVY, MU_HEAVY, U_SMALLP
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE W3 RESONANCE LANDSCAPE -- P(alpha) = q tan^2 theta on "
          "8 fixed-h slices")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    U0_GRID = zeta_grid_const()
    U_MAX = float(core.U_ALL[-1])
    mu_all = np.array([float(m) for m in core.MU_ALL])
    heavy_idx = np.argsort(-mu_all)[:K_HEAVY]
    U_HEAVY = np.array([float(core.U_ALL[i]) for i in heavy_idx])
    MU_HEAVY = mu_all[heavy_idx]
    n_all = np.rint(np.exp(np.array(
        [float(u) for u in core.U_ALL]))).astype(int)
    sp_idx = [int(np.where(n_all == p)[0][0]) for p in (2, 3, 5, 7)]
    U_SMALLP = np.array([float(core.U_ALL[i]) for i in sp_idx])
    print("      heavy atoms (score_b): n = %s (max u = %.3f)"
          % (sorted(n_all[heavy_idx].tolist()), float(U_HEAVY.max())))

    # ------------------------------------------------ base sweep
    KZ = core.frame_a_zones()
    rows = []
    for kz in KZ:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        r = window_eval(alpha, Mz)
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
    rid = np.array([r["rid"] for r in lock_c])
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

    # ------------------------------------------------ slice selection
    order = np.argsort(-Pv)
    top4 = [int(i) for i in order[:4]]
    top4_h = sorted(int(hs[i]) for i in top4)
    check("G0.4 [E] the top-4 windows by P are %s (declared quote %s;"
          " P = %s)"
          % (top4_h, sorted(TOP4_QUOTE),
             ["%.4f" % Pv[i] for i in top4]),
          set(top4_h) == TOP4_QUOTE)

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

    # ------------------------------------------------ R1: the profiles
    print("\nR1 -- the resonance profiles P(alpha) at fixed h "
          "(grid +-%.0f%%, %d points, step %.2f%%)"
          % (100 * S_MAX, N_GRID, 100 * 2 * S_MAX / (N_GRID - 1)))
    SGRID = np.linspace(-S_MAX, S_MAX, N_GRID)
    SGRID[N_GRID // 2] = 0.0
    profiles = []
    for i_w, tag in zip(sel, sel_tags):
        r0 = lock_c[i_w]
        t_w = time.time()
        ss, recs = [], []
        n_infeas = 0
        for s in SGRID:
            a_p = r0["alpha"] * (1.0 + s)
            if math.exp(2.0 * a_p) > core.ATOM_MAX + 0.5:
                n_infeas += 1
                continue
            rv = window_eval(a_p, r0["Mz"])
            ss.append(float(s))
            recs.append(rv)
        ss = np.array(ss)
        Pp = np.array([rv["P"] for rv in recs])
        i0 = int(np.where(ss == 0.0)[0][0])
        profiles.append(dict(i_w=i_w, tag=tag, r0=r0, ss=ss, recs=recs,
                             Pp=Pp, i0=i0, n_infeas=n_infeas))
        print("      h = %4d (%s): %d feasible / %d infeasible "
              "points  [%.0f s]"
              % (r0["h"], tag, len(ss), n_infeas, time.time() - t_w))

    dev_reb = max(abs(pr["Pp"][pr["i0"]] - pr["r0"]["P"])
                  / pr["r0"]["P"] for pr in profiles)
    check("G0.6 [E] wiring guard: the s = 0 rebuild reproduces the "
          "base-sweep P on all 8 slices (max rel dev %.1e < %.0e)"
          % (dev_reb, BAR_REBUILD), dev_reb < BAR_REBUILD)

    pr859 = [pr for pr in profiles if pr["r0"]["h"] == 859]
    if pr859:
        pr = pr859[0]
        devs = []
        for di in A3_SHIFT_IDX:
            j = pr["i0"] + di
            if 0 <= j < len(pr["ss"]):
                devs.append(abs(pr["Pp"][j] - pr["Pp"][pr["i0"]])
                            / pr["Pp"][pr["i0"]])
        frag = max(devs) if devs else 0.0
        check("G0.7 [E] the w3ub A3 FRAGILE read reproduces on h = "
              "859: max |dP|/P over s in {+-2.5%%, +-5%%} = %.4f > "
              "%.2f" % (frag, STAB_BAR), frag > STAB_BAR)
    else:
        check("G0.7 [E] h = 859 present among slices", False)

    # profile metrics + peaks
    all_peaks = []
    print("\n      per-slice profiles (P values on the feasible grid,"
          " * = detected peak, ^ = frame-A point):")
    for pr in profiles:
        ss, Pp, i0, r0 = pr["ss"], pr["Pp"], pr["i0"], pr["r0"]
        base = float(np.median(Pp))
        pk = detect_peaks(ss, Pp)
        intervals = []
        for ip, kind in pk:
            s_l, s_r, level, cens = fwhm_interval(ss, Pp, ip, base)
            intervals.append(dict(ip=ip, kind=kind, s=float(ss[ip]),
                                  P=float(Pp[ip]), s_l=s_l, s_r=s_r,
                                  w=s_r - s_l, cens=cens or
                                  (kind == "censored")))
        pr["base"] = base
        pr["peaks"] = intervals
        mask = np.zeros(len(ss), bool)
        for iv in intervals:
            mask |= (ss >= iv["s_l"]) & (ss <= iv["s_r"])
        pr["mask"] = mask
        pr["rank0"] = (float(np.sum(Pp <= Pp[i0])) - 0.5) / len(ss)
        pr["shares"] = {thr: float(np.mean(Pp > thr))
                        for thr in SHARE_THRESH}
        pr["n_flip"] = sum(1 for rv in pr["recs"] if not rv["lock"])
        # run-2 regime typing per grid point
        regs = [regime_of(rv) for rv in pr["recs"]]
        pr["regs"] = regs
        pr["margin_mask"] = np.array([rg == "MARGIN" for rg in regs])
        pr["n_neg"] = regs.count("NEG")
        pr["n_rot"] = regs.count("ROT")
        pr["n_lck"] = regs.count("LCK")
        pr["min_lam_fl"] = min(rv["lam"] / rv["floor"]
                               for rv in pr["recs"])
        all_peaks.extend((pr, iv) for iv in intervals)
        print("      h = %4d (%s): base(median) = %.4f, %d peak(s), "
              "%d lock flips; regimes MARGIN %d / ROT %d / LCK %d / "
              "NEG %d, min lam/floor %+.2e"
              % (r0["h"], pr["tag"], base, len(intervals),
                 pr["n_flip"], int(pr["margin_mask"].sum()),
                 pr["n_rot"], pr["n_lck"], pr["n_neg"],
                 pr["min_lam_fl"]))
        marks = ["*" if any(abs(ss[j] - iv["s"]) < 1e-12
                            for iv in intervals) else
                 ("^" if j == i0 else " ") for j in range(len(ss))]
        for a0 in range(0, len(ss), 10):
            b0 = min(len(ss), a0 + 10)
            print("        s=%+6.2f%%: %s"
                  % (100 * ss[a0],
                     " ".join("%.2f%s" % (Pp[j], marks[j])
                              for j in range(a0, b0))))

    print("\n      R1 profile table:")
    print("      h      tag         P(0)   rank(P0)  medP   >0.5  "
          ">0.8  >0.9  >0.95  peaks  medFWHM[da/a]  dist0->peak  "
          "in-FWHM")
    for pr in profiles:
        ivs = pr["peaks"]
        med_w = float(np.median([iv["w"] for iv in ivs])) if ivs \
            else float("nan")
        d0 = min((abs(iv["s"]) for iv in ivs), default=float("nan"))
        in_f = any(iv["s_l"] <= 0.0 <= iv["s_r"] for iv in ivs)
        sh = pr["shares"]
        print("      %4d  %-10s  %.4f   %.3f    %.4f  %.3f %.3f "
              "%.3f  %.3f   %d(%s)   %s      %s     %s"
              % (pr["r0"]["h"], pr["tag"], pr["Pp"][pr["i0"]],
                 pr["rank0"], float(np.median(pr["Pp"])), sh[0.5],
                 sh[0.8], sh[0.9], sh[0.95], len(ivs),
                 sum(1 for iv in ivs if iv["cens"]),
                 ("%.4f" % med_w) if ivs else "--",
                 ("%.4f" % d0) if ivs else "--",
                 "YES" if in_f else "no"))
    n_peaks_tot = len(all_peaks)
    n_cens = sum(1 for _, iv in all_peaks if iv["cens"])
    check("R1.1 [MEASURED] the landscape is PEAKED: %d peak(s) found "
          "across 8 slices (%d censored at a boundary); peak count "
          "per slice %s; FWHM range %s (in relative alpha units)"
          % (n_peaks_tot, n_cens,
             [len(pr["peaks"]) for pr in profiles],
             ("[%.4f, %.4f]" % (min(iv["w"] for _, iv in all_peaks),
                                max(iv["w"] for _, iv in all_peaks)))
             if all_peaks else "n/a"), True)

    # ------------------------------------ R1b: zoom (run-2, declared)
    print("\nR1b -- zoom refinement (run-2 calibration: step 0.025%%,"
          " +-%.2f%% around <= 2 peaks per slice)" % (100 * ZOOM_HALF))
    zoom_rows = []
    for pr in profiles:
        ivs = pr["peaks"]
        if not ivs:
            continue
        iv_near = min(ivs, key=lambda iv: abs(iv["s"]))
        iv_high = max(ivs, key=lambda iv: iv["P"])
        pairs = [(iv_near, "near-frameA")]
        if iv_high is not iv_near:
            pairs.append((iv_high, "highest"))
        for iv, ztag in pairs:
            t_z = time.time()
            zs = np.linspace(iv["s"] - ZOOM_HALF, iv["s"] + ZOOM_HALF,
                             N_ZOOM)
            ssz, recz = [], []
            for s in zs:
                a_p = pr["r0"]["alpha"] * (1.0 + s)
                if math.exp(2.0 * a_p) > core.ATOM_MAX + 0.5:
                    continue
                ssz.append(float(s))
                recz.append(window_eval(a_p, pr["r0"]["Mz"]))
            ssz = np.array(ssz)
            Pz = np.array([r_["P"] for r_ in recz])
            izm = int(np.argmax(Pz))
            s_l, s_r, _, cens = fwhm_interval(ssz, Pz, izm,
                                              pr["base"])
            n_sub = len(detect_peaks(ssz, Pz))
            zoom_rows.append(dict(
                h=pr["r0"]["h"], ztag=ztag, s_c=iv["s"], P_c=iv["P"],
                w_c=iv["w"], s_f=float(ssz[izm]), P_f=float(Pz[izm]),
                w_f=s_r - s_l, cens=cens, rg=regime_of(recz[izm]),
                th=recz[izm]["theta"], n_sub=n_sub))
            zr = zoom_rows[-1]
            print("      h = %4d %-11s coarse s* %+7.4f P* %10.4f "
                  "FWHM %.4f -> fine s* %+8.5f P* %10.4f FWHM "
                  "%s%.5f  regime %-6s theta %5.2f  sub-peaks %d  "
                  "[%.0f s]"
                  % (zr["h"], ztag, zr["s_c"], zr["P_c"], zr["w_c"],
                     zr["s_f"], zr["P_f"],
                     ">=" if zr["cens"] else "", zr["w_f"], zr["rg"],
                     zr["th"], zr["n_sub"], time.time() - t_z))
    w_fine = [zr["w_f"] for zr in zoom_rows if not zr["cens"]]
    ratio_wf = [zr["w_f"] / zr["w_c"] for zr in zoom_rows
                if not zr["cens"] and zr["w_c"] > 0]
    check("R1b.1 [MEASURED, run-2] resolution-corrected widths on %d "
          "zoomed peaks (%d censored by the zoom window): fine FWHM "
          "median %.5f, range %s (coarse median was 0.0025 = grid "
          "step); fine/coarse ratio median %.2f; regimes at fine "
          "maxima: %s"
          % (len(zoom_rows),
             sum(1 for zr in zoom_rows if zr["cens"]),
             float(np.median(w_fine)) if w_fine else float("nan"),
             ("[%.5f, %.5f]" % (min(w_fine), max(w_fine)))
             if w_fine else "n/a",
             float(np.median(ratio_wf)) if ratio_wf else
             float("nan"),
             {rg: sum(1 for zr in zoom_rows if zr["rg"] == rg)
              for rg in ("MARGIN", "ROT", "LCK", "NEG")}), True)

    unrem = [pr for pr in profiles if pr["tag"].startswith("QUANT")]
    ranks_u = np.array([pr["rank0"] for pr in unrem])
    ranks_t = np.array([pr["rank0"] for pr in profiles
                        if pr["tag"] == "TOP-P"])
    mean_u = float(ranks_u.mean())
    biased = mean_u >= RANK_BIAS_BAR
    check("R1.2 [MEASURED] construction-bias read on the 4 "
          "UNREMARKABLE slices: quantile ranks of P(0) = %s, mean = "
          "%.3f (uniform null 0.5 +- SD 0.144; bias bar %.3f) -> "
          "frame-A points are %s; top-4 ranks %s reported but "
          "selection-conditioned (excluded from the test)"
          % (["%.3f" % r_ for r_ in ranks_u], mean_u, RANK_BIAS_BAR,
             "SYSTEMATICALLY NEAR THE PEAKS (construction bias)"
             if biased else
             "NOT systematically on the peaks (the family reads as a "
             "fair sample of its landscape)",
             ["%.3f" % r_ for r_ in ranks_t]), True)

    # ------------------------------------------------ R2: the condition
    print("\nR2 -- the resonance condition: what distinguishes the "
          "peak alphas?")
    ga_all = np.concatenate([[rv["score_a"] for rv in pr["recs"]]
                             for pr in profiles])
    print("      score_a degeneracy read: local atom gap / D per "
          "slice = %s; pooled score_a range [%.4f, %.4f]"
          % (["%.3f" % (pr["recs"][pr["i0"]]["gap_loc"]
                        / pr["recs"][pr["i0"]]["D"])
              for pr in profiles],
             float(ga_all.min()), float(ga_all.max())))

    if all_peaks:
        print("\n      per-peak diagnosis (scores at the peak center "
              "+ within-profile quantile rank; run-2 regime):")
        print("      h      s*        P*     FWHM    regime  theta   "
              "score_a (rk)   score_b (rk)   score_c (rk)   "
              "p=2/3/5/7 offsets")
        for pr, iv in all_peaks:
            rv = pr["recs"][iv["ip"]]
            sa = np.array([r_["score_a"] for r_ in pr["recs"]])
            sb = np.array([r_["score_b"] for r_ in pr["recs"]])
            sc_ = np.array([r_["dst_hi"] for r_ in pr["recs"]])
            rk_a = (float(np.sum(sa <= rv["score_a"])) - 0.5) / len(sa)
            rk_b = (float(np.sum(sb <= rv["score_b"])) - 0.5) / len(sb)
            rk_c = (float(np.sum(sc_ <= rv["dst_hi"])) - 0.5) / len(sc_)
            print("      %4d  %+7.4f  %.4f  %s  %-6s  %5.2f  "
                  "%.4f (%.2f)   %.4f (%.2f)   %.4f (%.2f)   %s"
                  % (pr["r0"]["h"], iv["s"], iv["P"],
                     ("%s%.4f" % (">=" if iv["cens"] else "  ",
                                  iv["w"])),
                     pr["regs"][iv["ip"]], rv["theta"],
                     rv["score_a"], rk_a, rv["score_b"], rk_b,
                     rv["dst_hi"], rk_c,
                     "/".join("%.3f" % o for o in rv["off_smallp"])))

    # pooled association: label = inside a FWHM interval
    scores_list = {
        "a (edge atom /D, LOW)": ([np.array([r_["score_a"]
                                             for r_ in pr["recs"]])
                                   for pr in profiles], True),
        "b (heavy commens., LOW)": ([np.array([r_["score_b"]
                                               for r_ in pr["recs"]])
                                     for pr in profiles], True),
        "c (DST edge band, HIGH)": ([np.array([r_["dst_hi"]
                                               for r_ in pr["recs"]])
                                     for pr in profiles], False)}
    labels_list = [pr["mask"].astype(float) for pr in profiles]
    lb = np.concatenate(labels_list)
    prev = float(lb.mean())
    rng = np.random.default_rng(SEED)
    hits = []
    print("\n      pooled candidate gates (N = %d points, prevalence "
          "= %.3f -> precision bar %.3f, p bar %.2f, cyclic-shift "
          "B = %d):" % (len(lb), prev, max(0.5, 2.0 * prev), P_BAR,
                        B_PERM))
    r2_stats = {}
    for name, (sc_list, low_fav) in scores_list.items():
        sc = np.concatenate(sc_list)
        if lb.sum() == 0:
            print("      %s: no peak points -- skipped" % name)
            continue
        pp = prec_at_prev(sc, lb, low_fav)
        rho = spearman(sc, lb)
        cnt = 0
        for _ in range(B_PERM):
            sh_ = [np.roll(v_, int(rng.integers(1, len(v_))))
                   for v_ in sc_list]
            if abs(spearman(np.concatenate(sh_), lb)) \
                    >= abs(rho) - 1e-12:
                cnt += 1
        p_ = (cnt + 1.0) / (B_PERM + 1.0)
        sign_ok = (rho < 0.0) if low_fav else (rho > 0.0)
        hit = (pp >= max(0.5, 2.0 * prev)) and p_ < P_BAR and sign_ok
        r2_stats[name] = (pp, rho, p_, hit)
        if hit:
            hits.append(name)
        print("      %-26s prec@prev = %.3f  rho = %+.4f  p = %.4f  "
              "sign %s  -> %s"
              % (name, pp, rho, p_, "ok" if sign_ok else "WRONG",
                 "HIT" if hit else "miss"))
    check("R2.1 [MEASURED] resonance-condition gate (frozen: "
          "precision@prevalence >= max(0.5, 2 x prevalence) AND "
          "cyclic-shift p < %.2f AND declared sign): %s"
          % (P_BAR,
             ("HIT by %s" % "; ".join(hits)) if hits else
             "NO candidate passes -- the peaks are measured but not "
             "arithmetically characterized by (a)/(b)/(c)"), True)

    # run-2 diagnostic: the same candidates on MARGIN-regime peaks
    # only (PRINTED, no gate -- the run-1 gate above stays binding)
    labels2_list = []
    for pr in profiles:
        m2 = np.zeros(len(pr["ss"]), bool)
        for iv in pr["peaks"]:
            if pr["regs"][iv["ip"]] == "MARGIN":
                m2 |= (pr["ss"] >= iv["s_l"]) & (pr["ss"] <= iv["s_r"])
        labels2_list.append(m2.astype(float))
    lb2 = np.concatenate(labels2_list)
    if lb2.sum() > 0:
        print("\n      run-2 diagnostic, MARGIN-regime peaks only "
              "(printed, no gate; N = %d, prevalence = %.3f):"
              % (len(lb2), float(lb2.mean())))
        for name, (sc_list, low_fav) in scores_list.items():
            sc = np.concatenate(sc_list)
            pp2 = prec_at_prev(sc, lb2, low_fav)
            rho2 = spearman(sc, lb2)
            cnt2 = 0
            for _ in range(B_PERM):
                sh_ = [np.roll(v_, int(rng.integers(1, len(v_))))
                       for v_ in sc_list]
                if abs(spearman(np.concatenate(sh_), lb2)) \
                        >= abs(rho2) - 1e-12:
                    cnt2 += 1
            print("      %-26s prec@prev = %.3f  rho = %+.4f  "
                  "p = %.4f"
                  % (name, pp2, rho2, (cnt2 + 1.0) / (B_PERM + 1.0)))
    else:
        print("\n      run-2 diagnostic: no MARGIN-regime peak "
              "points -- skipped")

    # ------------------------------------------------ R3: the measure
    print("\nR3 -- measure estimate: which share of the surveyed "
          "alpha-space carries P > 1 - delta?")
    rng3 = np.random.default_rng(SEED + 1)

    def slice_boot(per):
        boot = np.empty(B_SLICE)
        for b_ in range(B_SLICE):
            idx = rng3.integers(0, len(per), len(per))
            boot[b_] = float(per[idx].mean())
        return (float(np.quantile(boot, 0.05)),
                float(np.quantile(boot, 0.95)))

    meas = {}
    meas_cl = {}
    for group, name in ((profiles, "ALL-8"), (unrem, "UNREMARK-4")):
        for dl in DELTAS:
            thr = 1.0 - dl
            per = np.array([float(np.mean(pr["Pp"] > thr))
                            for pr in group])
            q05, q95 = slice_boot(per)
            meas[(name, dl)] = (float(per.mean()), q05, q95,
                                per.tolist())
            per_cl = np.array([float(np.mean((pr["Pp"] > thr)
                                             & pr["margin_mask"]))
                               for pr in group])
            c05, c95 = slice_boot(per_cl)
            meas_cl[(name, dl)] = (float(per_cl.mean()), c05, c95)
            print("      %-11s delta = %.2f (P > %.2f): raw share "
                  "%.4f [5%% %.4f, 95%% %.4f]  |  MARGIN-regime "
                  "share %.4f [%.4f, %.4f]; per-slice raw %s"
                  % (name, dl, thr, float(per.mean()), q05, q95,
                     float(per_cl.mean()), c05, c95,
                     ["%.3f" % v for v in per]))
        per_neg = np.array([pr["n_neg"] / float(len(pr["ss"]))
                            for pr in group])
        per_deg = np.array([(pr["n_rot"] + pr["n_lck"])
                            / float(len(pr["ss"])) for pr in group])
        meas[(name, "neg")] = (float(per_neg.mean()),
                               float(per_deg.mean()))
        print("      %-11s direct reads: lambda_min < -floor on "
              "%.4f of the points (per-slice %s); identification-"
              "degenerate (ROT/LCK) on %.4f"
              % (name, float(per_neg.mean()),
                 ["%.3f" % v for v in per_neg],
                 float(per_deg.mean())))
    med_w_all = float(np.median([iv["w"] for _, iv in all_peaks])) \
        if all_peaks else float("nan")
    med_w_fine = float(np.median(w_fine)) if w_fine else float("nan")
    m95a = meas[("ALL-8", 0.05)]
    m95u = meas[("UNREMARK-4", 0.05)]
    m80u = meas[("UNREMARK-4", 0.2)]
    m95u_cl = meas_cl[("UNREMARK-4", 0.05)]
    m80u_cl = meas_cl[("UNREMARK-4", 0.2)]
    neg_u = meas[("UNREMARK-4", "neg")]
    check("R3.1 [MEASURED, surveyed region only] P > 0.95 lives on "
          "%.1f%% [%.1f%%, %.1f%%] of the surveyed alpha-space over "
          "all 8 slices and on %.1f%% [%.1f%%, %.1f%%] over the 4 "
          "unremarkable slices (raw; top-4 are P-selected); "
          "restricted to the MARGIN regime -- where P IS the "
          "positivity criterion -- the unremarkable shares drop to "
          "%.1f%% (P > 0.95) and %.1f%% (P > 0.8); lambda_min < "
          "-floor directly on %.1f%% and identification-degenerate "
          "points (ROT/LCK) on %.1f%% of the unremarkable grid; the "
          "exceedance concentrates on peaks of median coarse FWHM "
          "%.4f (grid-resolution bound; zoomed fine median %.5f).  "
          "8 slices of a 2D landscape -- a survey, not a theorem"
          % (100 * m95a[0], 100 * m95a[1], 100 * m95a[2],
             100 * m95u[0], 100 * m95u[1], 100 * m95u[2],
             100 * m95u_cl[0], 100 * m80u_cl[0],
             100 * neg_u[0], 100 * neg_u[1],
             med_w_all, med_w_fine), True)

    # ------------------------------------------------ R4: typing
    guards_ok = not any(f.startswith("G0") for f in FAILS)
    if not guards_ok:
        VERDICT = "W3RL-MIXED (guards or wiring failed)"
    elif n_peaks_tot == 0:
        VERDICT = "W3RL-SMOOTH"
    elif hits:
        VERDICT = "W3RL-PEAKED-ARITHMETIC"
    else:
        VERDICT = "W3RL-PEAKED-UNEXPLAINED"

    check("R4.1 [C] the typed reading: the W3UB-FRAGILE finding "
          "resolves into a LANDSCAPE statement -- P > 0.95 on ~%.1f%%"
          " raw / ~%.1f%% MARGIN-regime and P > 0.8 on ~%.1f%% raw / "
          "~%.1f%% MARGIN-regime of the surveyed alpha-space "
          "(unremarkable slices), concentrated on peaks of median "
          "coarse FWHM %.4f (zoomed fine median %.5f); lambda_min < "
          "-floor on %.1f%% of the unremarkable grid (typed: OFF-"
          "frame-A the discrete assembly is uncertified -- a risk "
          "read, not a Weil-form statement); frame-A bias read: %s "
          "(mean unremarkable rank %.3f -- the LOW side); resonance "
          "condition: %s.  The reformulated W3 target is 'GENERIC "
          "bound + exception control', NOT a uniform bound; NO "
          "positivity claim, NO RH statement, NO marker move; W3 "
          "stays open"
          % (100 * m95u[0], 100 * m95u_cl[0], 100 * m80u[0],
             100 * m80u_cl[0], med_w_all, med_w_fine,
             100 * neg_u[0],
             "BIASED" if biased else "FAIR-SAMPLE", mean_u,
             ("characterized by %s" % "; ".join(hits)) if hits
             else "NOT characterized by the frozen candidates"), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, resonance-landscape round (2026-08-02):
  the W3UB-FRAGILE finding (P = q tan^2 theta moves by ~60%% under
  +-5%% alpha-shift at fixed h) was mapped on 8 fixed-h slices
  (top-4 by P: h = %s; 4 h-quantile picks: h = %s) with an 81-point
  alpha-grid (+-10%%, atom-complete only) plus a run-2 zoom (step
  0.025%%) and a run-2 regime typing (MARGIN: theta < 45 deg and
  lambda_lock > 0, where P < 1 <=> lambda_min > 0; ROT/LCK:
  identification degenerate; NEG: lambda_min < -floor).  LANDSCAPE:
  %d peak(s) with P >= %.2f, coarse FWHM %s, zoomed fine median
  %.5f; P > 0.95 on %.1f%% [%.1f%%, %.1f%%] raw and %.1f%% MARGIN-
  regime, P > 0.8 on %.1f%% raw / %.1f%% MARGIN-regime of the
  surveyed alpha-space; lambda_min < -floor on %.1f%% and ROT/LCK
  degeneracies on %.1f%% (unremarkable slices; slice bootstrap
  B = %d; off-frame-A the assembly is uncertified -- risk numbers,
  not Weil-form statements).  FRAME-A PLACEMENT: mean P(0)
  quantile rank %.3f on the unremarkable slices (bias bar %.3f) ->
  %s.  RESONANCE CONDITION: candidates (a) edge-atom alignment,
  (b) heavy-atom commensurability dist(u/D, Z), (c) DST edge-band
  share of w_perp -> %s.  CONSEQUENCE FOR W3 (typed, open): %s
  TYPE: measured landscape survey on the declared surface; no
  positivity claim; no RH statement; Problem 7.1 untouched; no
  marker move.
""" % (sorted(int(hs[i]) for i in top4),
       [int(hs[i]) for i in picks],
       n_peaks_tot, P_PEAK_BAR,
       ("median %.4f, range [%.4f, %.4f] in relative alpha units"
        % (med_w_all, min(iv["w"] for _, iv in all_peaks),
           max(iv["w"] for _, iv in all_peaks))) if all_peaks
       else "n/a",
       med_w_fine,
       100 * m95u[0], 100 * m95u[1], 100 * m95u[2],
       100 * m95u_cl[0], 100 * m80u[0], 100 * m80u_cl[0],
       100 * neg_u[0], 100 * neg_u[1],
       B_SLICE, mean_u, RANK_BIAS_BAR,
       "the frame-A points sit SYSTEMATICALLY NEAR the peaks "
       "(construction bias: the 67 family values OVERSTATE the "
       "generic landscape)" if biased else
       "the frame-A points are NOT systematically on the peaks "
       "(the 67 family values read as a fair sample of the "
       "landscape)",
       ("HIT: %s -- peak-alphas are predictable; precision/recall "
        "at prevalence %s" % ("; ".join(hits),
                              ["%s %.3f" % (k.split()[0], v[0])
                               for k, v in r2_stats.items()]))
       if hits else
       ("NO frozen candidate predicts the peaks (prec@prev %s); "
        "the landscape is a RISK MAP, not yet an exception theorem"
        % ["%s %.3f" % (k.split()[0], v[0])
           for k, v in r2_stats.items()]),
       ("the proof path is 'generic bound + peak exclusion by "
        "condition %s': show P <= 1 - delta off the exception set "
        "and control the set by the predicting condition."
        % "; ".join(hits)) if hits else
       ("no exception-set characterization yet -- the landscape "
        "documents WHERE the uniform bound is at risk (peaks of "
        "median width %.4f); the 'generic + exception' route needs "
        "a predicate for the peaks first." % med_w_all)))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
