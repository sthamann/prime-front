"""Discovery probe: THE W3 UNIFORM BOUND -- risk survey of the reduced
open problem  P := q tan^2 theta <= 1 - delta  (uniform over the
window family).

CONTEXT.  rid_alignment_probe (2026-08-02) closed the geometry of the
margin identification: on lock windows lambda_min = r_id x lambda_lock
with the EXACT 2D formula r_id = (1 - q tan^2 theta)/(1 - tan^2 theta)
(q = Q_perp/lambda_lock > 1, theta < 45 deg, both structural on the
family), so positivity on a lock window is EQUIVALENT to P < 1 and W3
reduces (on this surface) to (i) the lock sign of q_r (v618 dichotomy)
and (ii) a uniform bound P <= 1 - delta.  Measured threat there: P
RISES with h (Spearman +0.735) to max 0.9636 at h = 859.  THIS probe
quantifies the risk in three slices -- it makes NO positivity claim
and NO uniform-bound claim; extrapolations are risk numbers, not
statements about deeper ladders.

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * sample: the rid_alignment analysis sample verbatim (complete
    frame-A windows, lock sign q_real q_model > 0, lambda_min above
    the float floor FLOOR_SAFETY x eps x radius x sqrt(h));
  * guards: the declared surface (67 complete, truncated {1219, 1292,
    1445}); the rid anchors max P = 0.9636 at h = 859 (tol 0.005),
    Spearman(P, h) = +0.735 (tol 0.03), Spearman(r_id, h) = -0.784
    (tol 0.03), median r_id 0.584 (tol 0.005), median theta 9.1 deg
    (tol 0.15); the closed formula per window (< 1e-6); structural
    q > 1, theta < 45 deg, P < 1 on every sample window;
  * A1 decomposition: OLS of log P, log q, log tan^2 theta on log h
    with standard errors; the slope identity beta_P = beta_q + beta_t
    must hold to 1e-10 (pure linear algebra); trend attribution =
    slope shares, spread attribution = covariance shares;
  * A1 extrapolation, THREE frozen model classes fitted by nonlinear
    least squares in P-space (scipy curve_fit):
        M-POW  P = A h^b            (crossing log h* = -log A / b),
        M-LOG  P = a + b log h      (crossing log h* = (1 - a)/b),
        M-SAT  P = c_inf - a h^-b   (finite crossing iff c_inf > 1);
    comparison by AIC = n log(RSS/n) + 2k; uncertainty by CASE
    BOOTSTRAP (B = 2000, seed 20260808), reporting per model the h*
    distribution (median / 5% / 95% among finite), the share of
    replicates crossing below 1e4 and 1e5, and prediction bands at
    h = 2000 / 5000 / 1e4 / 1e5.  Declared honestly: the family ends
    at h ~ 1.1e3, every number beyond is model extrapolation and the
    MODEL SPREAD is the uncertainty statement;
  * A2 mechanism: top-5 windows by P vs the rest; frozen structural
    feature list: edge atom spacing 2a - u_{second-last} (the last
    atom sits AT the edge identically, rid H2.0), atom density
    k_a/(2 alpha), d_cap = u_max - 2 alpha, grid offset of the last
    atoms (min over the 5 atoms below the edge atom of the distance
    of u_j/D to the nearest lattice integer), and the w_perp shape
    reads (Euclidean DST centroid k_bar/h, high-mode share k > 0.8 h,
    low-mode share k <= 5, spatial edge shares j < 0.1 h and
    j >= 0.9 h).  Tests: 5-vs-rest median-difference label
    permutation (B = 10000) AND h-controlled (rank-cubic) partial
    Spearman vs P (v637 machinery, N_PERM = 10000); per-test gate
    |rho| >= 0.30 AND p < 0.01 (9 tests -> Bonferroni-honest bar
    0.01/9 noted, not enforced);
  * A3 stabilization: PRIMARY window = argmax P, SECONDARY = the
    window with P closest to the median; artificial variants keep Mz
    (hence h) FIXED and shift alpha by s in {-5%, -2.5%, 0, +2.5%,
    +5%}, keeping only atom-complete variants (e^{2 alpha'} <=
    ATOM_MAX + 0.5; feasibility is reported, not forced); the s = 0
    rebuild must reproduce the sweep P to 1e-12 (wiring guard);
    STABILITY BAR: max_s |P(s) - P(0)| / P(0) <= 0.15 on the primary
    window -> CONSTRUCTION-STABLE, else FRAGILE;
  * risk typing (A4): with log h* per model (point fits),
      HIGH      iff the AIC-best model crosses at h* <= 2 x max h of
                the surface (~2.3e3),
      MATERIAL  iff (>= 2 of 3 models cross at h* <= 1e4) OR the
                AIC-best model crosses at h* <= 1e4,
      LOW       otherwise.

Verdict enums (frozen, precedence top-down): W3UB-MIXED (guards or
wiring fail), W3UB-FRAGILE (A3 bar fails on the primary window),
W3UB-RISK-HIGH, W3UB-RISK-MATERIAL, W3UB-RISK-LOW.

FIREWALL: experiments-only; verification/ read-only (v563 import;
v618/v591/rid machinery REBUILT verbatim, no other imports); no
marker moves; no positivity claim; no RH statement; NO zero of any
L-function is read (AST-checked).  Python-only, per GATE.WOLFRAM.02.

Provenance: rid_alignment_probe (2026-08-02, closed formula + P
threat), margin_link_probe (lock identification), sign_uncertainty_w3
probe (floor machinery), v618 (C = 1 reads), v591 (lock direction),
v637 (control methodology).
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
SEED = 20260808              # fresh (rid probe used 20260806)
N_PERM = 10000               # A2 permutation budget (declared)
B_LABEL = 10000              # A2 label-permutation budget
B_FIT = 2000                 # A1 case-bootstrap budget
RHO_BAR = 0.30
P_BAR = 0.01
H_EXTRAP = (2000.0, 5000.0, 1.0e4, 1.0e5)
RISK_H_MAT = 1.0e4
STAB_BAR = 0.15              # A3 stability bar (declared)
SHIFTS = (-0.05, -0.025, 0.0, 0.025, 0.05)
# reproduction anchors (rid_alignment_probe quotes)
P_MAX_QUOTE, P_MAX_TOL = 0.9636, 0.005
H_AT_PMAX = 859
SP_P_H_QUOTE, SP_TOL = 0.735, 0.03
SP_RID_H_QUOTE = -0.784
RID_MED_QUOTE, RID_TOL = 0.584, 0.005
THETA_MED_QUOTE = 9.1
BAR_EIGEN = 1e-6
BAR_SLOPE_ID = 1e-10
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
from scipy.optimize import curve_fit  # noqa: E402


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


def perm_p(xx, yy, rng, nperm=N_PERM):
    obs = pearson(xx, yy)
    cnt = 0
    for _ in range(nperm):
        if abs(pearson(rng.permutation(xx), yy)) >= abs(obs) - 1e-12:
            cnt += 1
    return obs, (cnt + 1.0) / (nperm + 1.0)


def control_cols(controls, poly):
    cols = []
    for cvec in controls:
        rc = rankdata(cvec)
        rc = (rc - rc.mean()) / rc.std()
        for p_ in range(1, poly + 1):
            cols.append(rc ** p_)
    return cols


def residualize(vec, cols):
    C = np.column_stack([np.ones(len(vec))] + cols)
    beta, _, _, _ = np.linalg.lstsq(C, vec, rcond=None)
    return vec - C @ beta


def partial_spearman(xx, yy, controls, rng, poly=1, nperm=N_PERM):
    cols = control_cols(controls, poly)
    ex = residualize(rankdata(xx), cols)
    ey = residualize(rankdata(yy), cols)
    return perm_p(ex, ey, rng, nperm)


def ols_se(x, y):
    """OLS y = a + b x with standard errors and R^2."""
    n = len(x)
    Xd = np.column_stack([np.ones(n), np.asarray(x, float)])
    beta, _, _, _ = np.linalg.lstsq(Xd, y, rcond=None)
    r = y - Xd @ beta
    s2 = float(r @ r) / (n - 2)
    cov = s2 * np.linalg.inv(Xd.T @ Xd)
    se = np.sqrt(np.diag(cov))
    yc = y - y.mean()
    r2 = 1.0 - float(r @ r) / float(yc @ yc)
    return beta, se, r2


# ------------------------------------------------------ window builder
U0_GRID = None
U_MAX = None


def window_eval(alpha, Mz):
    """One window at EXPLICIT (alpha, Mz): the rid_alignment sweep body
    verbatim, reusable for the A3 artificial alpha-shifted variants."""
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
    Tb = core.parity_basis(hz, 2)
    t1v, t2v = Tb[0], Tb[1]
    W11 = core.lag_weights_from_v(t1v, hz)
    W22 = core.lag_weights_from_v(t2v, hz)
    Wpp = core.lag_weights_from_v(t1v + t2v, hz)
    W12 = 0.5 * (Wpp - W11 - W22)
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
    # structural features (frozen list)
    dens = ka / (2.0 * alpha)
    gprev = 2.0 * alpha - float(core.U_ALL[ka - 2])
    dcap = U_MAX - 2.0 * alpha
    offs = np.abs(uu[ka - 6:ka - 1] / D
                  - np.round(uu[ka - 6:ka - 1] / D))
    grid_off = float(offs.min())
    # w_perp shape reads (Euclidean DST + spatial shares, declared)
    Bfull = core.parity_basis(hz)
    coef2 = (Bfull @ w_perp) ** 2
    tot = float(coef2.sum())
    kk = np.arange(1, hz + 1, dtype=float)
    dst_cen = float((kk * coef2).sum()) / tot / hz
    dst_hi = float(coef2[kk > 0.8 * hz].sum()) / tot
    dst_lo = float(coef2[:5].sum()) / tot
    w2 = w_perp ** 2
    tot2 = float(w2.sum())
    jj = np.arange(hz)
    sp_e0 = float(w2[jj < 0.1 * hz].sum()) / tot2
    sp_eC = float(w2[jj >= 0.9 * hz].sum()) / tot2
    return dict(h=hz, alpha=alpha, D=D, complete=complete,
                lam=lam_min, lam2=lam_2, floor=floor, qr=q_r, qm=q_m,
                lock=q_r * q_m > 0.0, ct=ct, st=st, t2=t2, qq=qq,
                P=qq * t2, lam_lock=lam_lock,
                rid=lam_min / lam_lock,
                theta=math.degrees(math.acos(ct)), dens=dens,
                gprev=gprev, dcap=dcap, grid_off=grid_off,
                dst_cen=dst_cen, dst_hi=dst_hi, dst_lo=dst_lo,
                sp_e0=sp_e0, sp_eC=sp_eC)


# ------------------------------------------------------ A1 model classes
def f_pow(h, A, b):
    return A * np.power(h, b)


def f_log(h, a, b):
    return a + b * np.log(h)


def f_sat(h, cinf, a, b):
    return cinf - a * np.power(h, -b)


def log_hstar(model, p):
    """log h* of the P = 1 crossing; +inf when the model never
    crosses from below."""
    if model == "POW":
        A, b = p
        return (-math.log(A) / b) if b > 0.0 else math.inf
    if model == "LOG":
        a, b = p
        return ((1.0 - a) / b) if b > 0.0 else math.inf
    cinf, a, b = p
    return (math.log(a / (cinf - 1.0)) / b) if cinf > 1.0 else math.inf


def fit_all(hs, Pv, p0s):
    """least-squares fits of the three frozen classes in P-space."""
    out = {}
    for name, f, p0, bounds in (
            ("POW", f_pow, p0s["POW"], ([1e-12, -5.0], [1e6, 5.0])),
            ("LOG", f_log, p0s["LOG"], ([-1e3, -1e3], [1e3, 1e3])),
            ("SAT", f_sat, p0s["SAT"],
             ([0.5, 1e-8, 0.01], [2.0, 1e4, 3.0]))):
        try:
            popt, pcov = curve_fit(f, hs, Pv, p0=p0, bounds=bounds,
                                   maxfev=20000)
            rss = float(np.sum((Pv - f(hs, *popt)) ** 2))
            out[name] = (popt, np.sqrt(np.diag(pcov)), rss)
        except Exception:
            out[name] = None
    return out


def run():
    global N_CHK, FAILS, U0_GRID, U_MAX
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE W3 UNIFORM BOUND -- risk survey of P = q tan^2 theta "
          "<= 1 - delta")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    U0_GRID = zeta_grid_const()
    U_MAX = float(core.U_ALL[-1])
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

    print("\n      h    2alpha       P=q*tan^2  theta[deg]      q    "
          " tan^2      r_id")
    for r in sorted(lock_c, key=lambda r: r["h"]):
        print("    %5d  %7.3f      %.4f      %6.2f   %8.3f  %.5f"
              "    %.4f"
              % (r["h"], 2 * r["alpha"], r["P"], r["theta"], r["qq"],
                 r["t2"], r["rid"]))

    # ============================================ A1: trend + risk
    print("\nA1 -- trend decomposition and the honest crossing risk")
    lh = np.log(hs)
    bP, seP, r2P = ols_se(lh, np.log(Pv))
    bq, seq_, r2q = ols_se(lh, np.log(qq))
    bt, set_, r2t = ols_se(lh, np.log(t2))
    dev_id = abs(bP[1] - bq[1] - bt[1])
    check("A1.1 [E] slope identity beta_P = beta_q + beta_t on log-"
          "log OLS: |dev| = %.1e < %.0e (pure linear algebra)"
          % (dev_id, BAR_SLOPE_ID), dev_id < BAR_SLOPE_ID)
    vP = float(np.var(np.log(Pv), ddof=1))
    sh_q = float(np.cov(np.log(qq), np.log(Pv))[0, 1]) / vP
    sh_t = float(np.cov(np.log(t2), np.log(Pv))[0, 1]) / vP
    print("      OLS on log h:  log P slope %+.4f +- %.4f (R^2 %.3f)"
          % (bP[1], seP[1], r2P))
    print("                     log q slope %+.4f +- %.4f (R^2 %.3f)"
          "  -> trend share %+.2f" % (bq[1], seq_[1], r2q,
                                      bq[1] / bP[1]))
    print("                     log tan^2   slope %+.4f +- %.4f (R^2 "
          "%.3f)  -> trend share %+.2f" % (bt[1], set_[1], r2t,
                                           bt[1] / bP[1]))
    print("      spread shares of log P (covariance):  q %.3f | "
          "tan^2 theta %.3f  (sum %.3f)"
          % (sh_q, sh_t, sh_q + sh_t))
    print("      Spearman with h:  P %+.4f | q %+.4f | tan^2 %+.4f"
          % (sp_P, spearman(qq, hs), spearman(t2, hs)))
    driver = "tan^2 theta" if abs(bt[1]) > abs(bq[1]) else "q"
    check("A1.2 [MEASURED] the h-trend of P is carried by %s (slope "
          "shares: q %+.2f / tan^2 %+.2f); within-family spread "
          "shares tan^2 %.2f vs q %.2f"
          % (driver, bq[1] / bP[1], bt[1] / bP[1], sh_t, sh_q), True)

    # frozen model fits
    b0 = np.polyfit(lh, np.log(Pv), 1)
    p0s = {"POW": (math.exp(b0[1]), b0[0]),
           "LOG": tuple(np.polyfit(lh, Pv, 1)[::-1])}
    b1 = np.polyfit(lh, np.log(np.maximum(1.0 - Pv, 1e-6)), 1)
    p0s["SAT"] = (1.0, math.exp(b1[1]), -b1[0]
                  if -b1[0] > 0.01 else 0.5)
    fits = fit_all(hs, Pv, p0s)
    labels = {"POW": "P = A h^b", "LOG": "P = a + b log h",
              "SAT": "P = c_inf - a h^-b"}
    aic = {}
    lhs_pt = {}
    print("\n      model             params (+- se)"
          "                          RSS       AIC     h* (P = 1)")
    for name in ("POW", "LOG", "SAT"):
        if fits[name] is None:
            print("      M-%s  %-22s  FIT FAILED" % (name, labels[name]))
            aic[name] = math.inf
            lhs_pt[name] = math.inf
            continue
        popt, perr, rss = fits[name]
        k = len(popt)
        aic[name] = n * math.log(rss / n) + 2 * k
        lhs_pt[name] = log_hstar(name, popt)
        hstar_s = ("%.3g" % math.exp(lhs_pt[name])
                   if lhs_pt[name] < 40.0 else "none (from below)")
        ps = ", ".join("%.4g+-%.2g" % (p_, e_)
                       for p_, e_ in zip(popt, perr))
        print("      M-%s  %-22s  %-38s  %.3e  %+8.2f  %s"
              % (name, labels[name], ps, rss, aic[name], hstar_s))
    best = min(aic, key=aic.get)

    # case bootstrap
    rng = np.random.default_rng(SEED)
    boot_lhs = {m: [] for m in fits}
    boot_pred = {m: {H: [] for H in H_EXTRAP} for m in fits}
    boot_cinf = []
    n_fail = 0
    p0b = {m: tuple(fits[m][0]) for m in fits if fits[m] is not None}
    for _ in range(B_FIT):
        idx = rng.integers(0, n, n)
        fb = fit_all(hs[idx], Pv[idx], {**p0s, **p0b})
        for m in fb:
            if fb[m] is None:
                n_fail += 1
                continue
            popt = fb[m][0]
            boot_lhs[m].append(log_hstar(m, popt))
            f = {"POW": f_pow, "LOG": f_log, "SAT": f_sat}[m]
            for H in H_EXTRAP:
                boot_pred[m][H].append(float(f(H, *popt)))
            if m == "SAT":
                boot_cinf.append(float(popt[0]))
    print("\n      case bootstrap (B = %d, seed %d; %d fit failures "
          "across all models):" % (B_FIT, SEED, n_fail))
    print("      model   h* med [5%%, 95%%] (finite)      share "
          "cross<=1e4  <=1e5   no crossing")
    for m in ("POW", "LOG", "SAT"):
        arr = np.array(boot_lhs[m])
        if arr.size == 0:
            continue
        fin = arr[np.isfinite(arr)]
        cr4 = float(np.mean(arr <= math.log(1e4)))
        cr5 = float(np.mean(arr <= math.log(1e5)))
        nc = float(np.mean(~np.isfinite(arr)))
        if fin.size:
            med, q05, q95 = (math.exp(float(np.quantile(fin, q)))
                             for q in (0.5, 0.05, 0.95))
            print("      M-%s   %.3g [%.3g, %.3g]              "
                  "%.3f        %.3f    %.3f"
                  % (m, med, q05, q95, cr4, cr5, nc))
        else:
            print("      M-%s   never finite                        "
                  "%.3f        %.3f    %.3f" % (m, cr4, cr5, nc))
    if boot_cinf:
        ci = np.array(boot_cinf)
        print("      M-SAT c_inf: point %.4f, bootstrap median %.4f "
              "[5%% %.4f, 95%% %.4f], share c_inf > 1: %.3f"
              % (fits["SAT"][0][0] if fits["SAT"] else float("nan"),
                 float(np.median(ci)), float(np.quantile(ci, 0.05)),
                 float(np.quantile(ci, 0.95)),
                 float(np.mean(ci > 1.0))))
    print("      prediction bands P_hat(h) [bootstrap 5%%, 95%%]:")
    hdr = "      model  " + "".join("   h = %-8.0f" % H
                                    for H in H_EXTRAP)
    print(hdr)
    for m in ("POW", "LOG", "SAT"):
        if fits[m] is None:
            continue
        cells = []
        f = {"POW": f_pow, "LOG": f_log, "SAT": f_sat}[m]
        for H in H_EXTRAP:
            pt = float(f(H, *fits[m][0]))
            band = np.array(boot_pred[m][H])
            cells.append("%.3f [%.2f,%.2f]"
                         % (pt, float(np.quantile(band, 0.05)),
                            float(np.quantile(band, 0.95))))
        print("      M-%s  %s" % (m, "  ".join(cells)))

    n_cross_1e4 = sum(1 for m in lhs_pt
                      if lhs_pt[m] <= math.log(RISK_H_MAT))
    risk_high = lhs_pt[best] <= math.log(2.0 * float(hs.max()))
    risk_mat = (n_cross_1e4 >= 2
                or lhs_pt[best] <= math.log(RISK_H_MAT))
    check("A1.3 [MEASURED, risk numbers -- NOT a claim about deeper "
          "ladders] AIC-best model M-%s; point crossings h*: %s; "
          "%d/3 models cross at h* <= 1e4; AIC-best crosses <= 2 x "
          "max h (%.0f): %s -- margin to 1 on the surface: %.4f at "
          "h = %d"
          % (best,
             ", ".join("%s %s" % (m, ("%.3g" % math.exp(lhs_pt[m])
                                      if lhs_pt[m] < 40.0 else "none"))
                       for m in ("POW", "LOG", "SAT")),
             n_cross_1e4, 2.0 * float(hs.max()),
             "YES" if risk_high else "no",
             1.0 - float(Pv.max()), int(hs[i_max])), True)

    # ============================================ A2: the mechanism
    print("\nA2 -- what distinguishes the largest-P windows?")
    order = np.argsort(-Pv)
    top = np.zeros(n, bool)
    top[order[:5]] = True
    print("      top-5 by P (h, 2a, P, theta, q, tan^2, gprev, dens, "
          "grid_off, dst_cen, dst_hi, sp_e0, sp_eC):")
    for i in order[:5]:
        r = lock_c[i]
        print("      h=%5d  2a=%6.3f  P=%.4f  th=%5.2f  q=%7.3f  "
              "t2=%.5f  gprev=%.4f  dens=%6.1f  off=%.4f  cen=%.4f  "
              "hi=%.2e  e0=%.3f  eC=%.3f"
              % (r["h"], 2 * r["alpha"], r["P"], r["theta"], r["qq"],
                 r["t2"], r["gprev"], r["dens"], r["grid_off"],
                 r["dst_cen"], r["dst_hi"], r["sp_e0"], r["sp_eC"]))
    feats = [("edge spacing gprev", np.array([r["gprev"]
                                              for r in lock_c])),
             ("atom density", np.array([r["dens"] for r in lock_c])),
             ("d_cap", np.array([r["dcap"] for r in lock_c])),
             ("grid offset last5", np.array([r["grid_off"]
                                             for r in lock_c])),
             ("dst centroid", np.array([r["dst_cen"]
                                        for r in lock_c])),
             ("dst high share", np.array([r["dst_hi"]
                                          for r in lock_c])),
             ("dst low5 share", np.array([r["dst_lo"]
                                          for r in lock_c])),
             ("spatial edge j<.1h", np.array([r["sp_e0"]
                                              for r in lock_c])),
             ("spatial edge j>.9h", np.array([r["sp_eC"]
                                              for r in lock_c]))]
    rng2 = np.random.default_rng(SEED + 1)
    print("\n      %-20s  med(top5)   med(rest)   label-perm p | "
          "h3-partial rho vs P      p" % "feature")
    hits = []
    for name, xv in feats:
        m_t = float(np.median(xv[top]))
        m_r = float(np.median(xv[~top]))
        obs = m_t - m_r
        cnt = 0
        for _ in range(B_LABEL):
            mm = np.zeros(n, bool)
            mm[rng2.permutation(n)[:5]] = True
            if abs(float(np.median(xv[mm]))
                   - float(np.median(xv[~mm]))) >= abs(obs) - 1e-15:
                cnt += 1
        p_lab = (cnt + 1.0) / (B_LABEL + 1.0)
        r3, p3 = partial_spearman(Pv, xv, [hs], rng2, poly=3)
        hit = abs(r3) >= RHO_BAR and p3 < P_BAR
        if hit:
            hits.append((name, r3, p3))
        print("      %-20s  %9.4f   %9.4f     %.4f     |   %+8.4f"
              "         %.4f%s"
              % (name, m_t, m_r, p_lab, r3, p3, "  <- HIT" if hit
                 else ""))
    check("A2.1 [MEASURED] mechanism carriers of P after rank-cubic "
          "h-control (gate |rho| >= %.2f, p < %.2f per test; 9 tests, "
          "Bonferroni-honest bar p < %.4f): %s.  theta itself (the "
          "closed-formula constituent) has median %.2f deg on top-5 "
          "vs %.2f deg on the rest -- the top windows are the LARGE-"
          "ANGLE windows by construction"
          % (RHO_BAR, P_BAR, P_BAR / 9.0,
             ("; ".join("%s rho=%+.3f p=%.4f%s"
                        % (nm, r3, p3, " [Bonferroni holds]"
                           if p3 < P_BAR / 9.0 else "")
                        for nm, r3, p3 in hits)) if hits
             else "NONE passes the gate",
             float(np.median(th[top])), float(np.median(th[~top]))),
          True)

    # ============================================ A3: stabilization
    print("\nA3 -- construction stability: alpha-shift at fixed h")
    i_med = int(np.argsort(np.abs(Pv - np.median(Pv)))[0])
    results = {}
    for tag, i_w in (("PRIMARY (max P)", i_max),
                     ("SECONDARY (median P)", i_med)):
        r0 = lock_c[i_w]
        print("      %s: h = %d, 2a = %.4f, P = %.4f"
              % (tag, r0["h"], 2 * r0["alpha"], r0["P"]))
        var_rows = []
        for s in SHIFTS:
            a_p = r0["alpha"] * (1.0 + s)
            if math.exp(2.0 * a_p) > core.ATOM_MAX + 0.5:
                print("        s = %+5.1f%%: NOT atom-complete "
                      "(e^{2a'} = %.3g > %d) -- skipped"
                      % (100 * s, math.exp(2.0 * a_p), core.ATOM_MAX))
                continue
            rv = window_eval(a_p, r0["Mz"])
            var_rows.append((s, rv))
            print("        s = %+5.1f%%: P = %.4f (dP/P = %+7.4f), "
                  "theta = %5.2f, q = %7.3f, lock %s, lam_min %+.3e"
                  % (100 * s, rv["P"], rv["P"] / r0["P"] - 1.0,
                     rv["theta"], rv["qq"],
                     "KEPT" if rv["lock"] else "FLIPPED", rv["lam"]))
        results[tag] = (r0, var_rows)
    r0, vr = results["PRIMARY (max P)"]
    v0 = [rv for s, rv in vr if s == 0.0]
    dev_reb = abs(v0[0]["P"] - r0["P"]) / r0["P"] if v0 else math.inf
    check("A3.1 [E] wiring guard: the s = 0 rebuild reproduces the "
          "sweep P on the primary window (rel dev %.1e < %.0e)"
          % (dev_reb, BAR_REBUILD), dev_reb < BAR_REBUILD)
    spreads = {}
    for tag in results:
        r0_, vr_ = results[tag]
        ds = [abs(rv["P"] - r0_["P"]) / r0_["P"] for s, rv in vr_
              if s != 0.0]
        spreads[tag] = max(ds) if ds else math.inf
    stable = spreads["PRIMARY (max P)"] <= STAB_BAR
    n_var_p = sum(1 for s, _ in results["PRIMARY (max P)"][1]
                  if s != 0.0)
    check("A3.2 [MEASURED] construction stability at fixed h: "
          "primary window max |dP|/P = %.4f over %d feasible "
          "alpha-shifts (bar %.2f) -> %s; secondary window max "
          "|dP|/P = %.4f -- P is %s"
          % (spreads["PRIMARY (max P)"], n_var_p, STAB_BAR,
             "STABLE" if stable else "FRAGILE",
             spreads["SECONDARY (median P)"],
             "a smooth property of the declared window construction "
             "(depth carries it, not the exact frame-A alpha)"
             if stable else
             "FRAGILE under alpha-shift -- the bound rides on the "
             "exact frame-A coupling"), True)

    # ============================================ A4: typing + verdict
    guards_ok = not any(f.startswith(("G0", "A1.1", "A3.1"))
                        for f in FAILS)
    if not guards_ok:
        VERDICT = "W3UB-MIXED (guards or wiring failed)"
    elif not stable:
        VERDICT = "W3UB-FRAGILE"
    elif risk_high:
        VERDICT = "W3UB-RISK-HIGH"
    elif risk_mat:
        VERDICT = "W3UB-RISK-MATERIAL"
    else:
        VERDICT = "W3UB-RISK-LOW"

    check("A4.1 [C] the typed reading: the reduced W3 obstruction is "
          "the uniform bound P = q tan^2 theta <= 1 - delta; measured "
          "family margin delta_family = %.4f (max P %.4f at h = %d); "
          "the h-trend is carried by %s; crossing-risk point "
          "estimates h* = {%s} with AIC-best M-%s; construction "
          "stability %s.  NO uniform theorem, NO positivity claim, "
          "NO marker move; W3 stays open"
          % (1.0 - float(Pv.max()), float(Pv.max()), int(hs[i_max]),
             driver,
             ", ".join("%s: %s" % (m, ("%.3g" % math.exp(lhs_pt[m])
                                       if lhs_pt[m] < 40.0
                                       else "none"))
                       for m in ("POW", "LOG", "SAT")),
             best, "STABLE" if stable else "FRAGILE"), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, uniform-bound round (2026-08-02): the
  reduced W3 open problem q tan^2 theta <= 1 - delta was risk-
  surveyed on the n = %d lock-sign complete frame-A windows.  TREND:
  the log-log slope of P = q tan^2 theta is %+.3f +- %.3f, carried by
  %s (slope shares: q %+.2f / tan^2 %+.2f); within-family spread
  shares tan^2 %.2f / q %.2f.  RISK (three frozen model classes, case
  bootstrap B = %d, seed %d): crossing points h* = POW %s / LOG %s /
  SAT %s; AIC-best M-%s; SAT saturation level c_inf = %.4f
  [bootstrap 5%%-95%%: %.4f, %.4f], share c_inf > 1 = %.3f.  The
  family margin is delta_family = %.4f at h = %d and every crossing
  number is an extrapolation BEYOND the measured surface (max h =
  %d) -- a risk quantification, not a statement.  MECHANISM: %s.
  STABILITY: alpha-shift at fixed h moves P by at most %.3f (rel) on
  the max-P window -> the bound is %s.  TYPE: measured family
  statement + preregistered risk survey; W3 open; Problem 7.1
  untouched; no marker move.
""" % (n, bP[1], seP[1], driver, bq[1] / bP[1], bt[1] / bP[1],
       sh_t, sh_q, B_FIT, SEED,
       ("%.3g" % math.exp(lhs_pt["POW"]) if lhs_pt["POW"] < 40.0
        else "none"),
       ("%.3g" % math.exp(lhs_pt["LOG"]) if lhs_pt["LOG"] < 40.0
        else "none"),
       ("%.3g" % math.exp(lhs_pt["SAT"]) if lhs_pt["SAT"] < 40.0
        else "none"),
       best,
       fits["SAT"][0][0] if fits["SAT"] is not None else float("nan"),
       float(np.quantile(np.array(boot_cinf), 0.05)) if boot_cinf
       else float("nan"),
       float(np.quantile(np.array(boot_cinf), 0.95)) if boot_cinf
       else float("nan"),
       float(np.mean(np.array(boot_cinf) > 1.0)) if boot_cinf
       else float("nan"),
       1.0 - float(Pv.max()), int(hs[i_max]), int(hs.max()),
       ("; ".join("%s rho=%+.3f p=%.4f" % (nm, r3, p3)
                  for nm, r3, p3 in hits)) if hits
       else "no structural covariate passes the gate after h-control"
       " -- P is angle-driven through the ladder itself",
       spreads["PRIMARY (max P)"],
       "construction-stable (a property of the declared surface, "
       "not of the exact frame-A alpha)" if stable else
       "FRAGILE under alpha-shift"))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
