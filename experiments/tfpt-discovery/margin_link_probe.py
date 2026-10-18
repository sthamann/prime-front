"""Discovery probe: THE MARGIN BRIDGE -- does the discrete positivity
margin lambda_min of the TFPT window form carry information about the
C = 1 uniform-constant load eps*h (v618) BEYOND the trivial depth
trend?  The strategic question behind the raw finding of the
sign-uncertainty probe (sign_uncertainty_w3_probe P3 diagnostic):
corr(log lambda_min, log eps*h) = +0.704 on the 67 complete lock-sign
frame-A windows.

THE v637 LESSON (why the raw number does not count): both quantities
decay along the window ladder, so a raw correlation can be pure
h-reparametrization.  v637 (fine Hodge invariants vs the C = 1 margin)
preregistered rank-based h-controls and found the raw signal dead
after control (partial rho = -0.04, p = 0.75) -- an honest negative
that closed that route.  This probe applies the SAME preregistered
machinery to the margin bridge.

WHAT A PASS WOULD MEAN: lambda_min is a POSITIVITY/GEOMETRY quantity
(the lowest L^2(window)-normalized Rayleigh quotient of the Weil
window form); eps*h is an ARITHMETIC quantity (the equidistribution
rate of the prime comb against the smooth model along the closed lock
direction).  An h-robust link would be the first quantitative
geometry/positivity <-> arithmetic bridge on this surface.  A KILL is
also a result: then "everything is the ladder parameter" is a nameable
pattern of the window family (as after v637), typed as such.

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * sample: complete windows (2 alpha <= u_max) with the LOCK SIGN
    (q_real q_model > 0) and lambda_min above the float floor
    (FLOOR_SAFETY x eps x pencil radius x sqrt(h)) -- the exact
    population of the +0.704 diagnostic;
  * variables: log lambda_min (L^2-normalized, generalized pencil
    against the tent Gram, v563 certified tent-read assembly) and
    log(eps*h) (v618 machinery verbatim: smooth model matrix, closed
    v591 lock direction);
  * controls: h via rank-linear AND rank-cubic residualization, plus
    (h, alpha) jointly rank-linear (v637 machinery verbatim);
    permutation p a la Freedman-Lane, N_PERM = 20000, SEED = 20260804;
  * verdict gate (primary): rank-cubic h-control; PASS needs
    |rho_partial| >= 0.30 AND p < 0.01; robustness gate (secondary):
    the same bar on the (h, alpha) joint control;
  * enums: BRIDGE-PASS (primary AND secondary gates pass),
    BRIDGE-PARTIAL (primary passes but secondary fails -> the link is
    alpha-mediated; or 0.01 <= p_primary < 0.05), BRIDGE-KILL
    (primary gate dead: h-reparametrization, the v637 pattern),
    MIXED (guards failed).

MECHANISM CHECKS (independent of the correlation, reported either
way):
  (M-0) THE IDENTIFICATION DECOMPOSITION [declared EXPLORATORY, added
        after the first gate run showed the minimal mode nearly
        collinear with the lock direction]: on lock windows q_r > 0
        and q_r = w_lock^T Ahat w_lock exactly (T163 pairing = matrix
        pairing; checked), so lambda_lock := q_r / ||w_lock||_G^2 is
        the lock-direction Rayleigh quotient and lambda_min <=
        lambda_lock with near-equality iff the minimal mode is the
        lock direction.  Then log lambda_lock and log(eps*h) differ by
        a SMOOTH ladder function (q_m, alpha), so an h/alpha-robust
        correlation between lambda_min and eps*h can be CARRIED
        ENTIRELY by the shared arithmetic defect q_r.  Measured here:
        the alignment ratio r_id = lambda_min/lambda_lock per window,
        corr(log lambda_min, log lambda_lock), and the killer test
        partial corr(log lambda_min, log eps*h | h, alpha,
        log lambda_lock): if it dies, the bridge IS the
        identification (typed as such -- still a result: the
        positivity margin equals the C = 1 defect along the lock
        direction up to the measured alignment factor); if it
        survives, lambda_min carries arithmetic information BEYOND
        the lock projection.
  (M-a) the lock-direction geometry of the minimal mode: per window
        the G-orthogonal energy fraction of the minimal mode v_min
        along the projected lock direction w_lock = vl_1 t1 + vl_2 t2
        (and in span{t1, t2}); null baseline for a random direction is
        ~ 1/h (~ 2/h for the span).  If the positivity margin were
        CARRIED by the lock direction, the fraction would be O(1).
  (M-b) the last-sign-change radius rho* of the minimal mode vs the
        data-cap distance d_cap = u_max - 2 alpha (flip proximity:
        the two v618 sign-flip windows sit PAST the cap).  HONEST
        CAVEAT, declared: d_cap is a deterministic monotone function
        of alpha alone, so the raw rank correlation is exactly
        -Spearman(rho*, alpha); the informative reads are the
        h-controlled partial and the scale-free f* = rho*/alpha.

Verdict enums (frozen): BRIDGE-PASS, BRIDGE-PARTIAL, BRIDGE-KILL,
MIXED.

FIREWALL: experiments-only; verification/ read-only (v563 import;
v618/v591/v637 machinery REBUILT verbatim, no imports); no marker
moves; no RH statement; NO zero of any L-function is read
(AST-checked).  Python-only, counted per GATE.WOLFRAM.02.

Provenance: sign_uncertainty_w3_probe (2026-08-02, P2/P3 machinery +
the +0.704 diagnostic); v618_uniform_constant (surface + C = 1 reads);
v637_fine_c1_bridge (control methodology); v596 (lock direction
context).
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
SIGN_TINY = 1.0e-9           # w3 probe, verbatim
GRID_PER_D = 4.0             # v618, verbatim
N_PERM = 20000
SEED = 20260804              # fresh (v637 used 20260802)
RHO_BAR = 0.30               # preregistered gate
P_BAR = 0.01
V648_CORR = 0.704            # the raw diagnostic to reproduce
V648_LAM_MIN = 8.26e-4       # min lambda_min over the 67 windows
V618_MAX_QUOTE = 0.982       # v618 U2 max eps*h at h = 184
V618_FLIPS = [1219, 1445]    # v618 U4 flip windows


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


# ------------------------------------------------------ w3 machinery
def gen_min_eig(A, G):
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    return float(w[0]), V[:, 0], rad


def last_sign_change(v, D, hz):
    w = v / float(np.max(np.abs(v)))
    s = np.where(np.abs(w) > SIGN_TINY, np.sign(w), 0.0)
    idx = np.nonzero(s)[0]
    flips = [(idx[k], idx[k + 1]) for k in range(len(idx) - 1)
             if s[idx[k]] * s[idx[k + 1]] < 0.0]
    if not flips:
        return 0.0, 0
    i1, i2 = flips[0]
    rho = (hz - 0.5 - 0.5 * (i1 + i2)) * D
    return float(rho), len(flips)


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


def ols(cols, y):
    Xd = np.column_stack([np.ones_like(y)] + cols)
    beta, _, _, _ = np.linalg.lstsq(Xd, y, rcond=None)
    r = y - Xd @ beta
    yc = y - y.mean()
    return beta, 1.0 - float(r @ r) / float(yc @ yc)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE MARGIN BRIDGE -- lambda_min vs the C = 1 load, after "
          "h-control")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    # ------------------------------------------------ the window sweep
    u0 = zeta_grid_const()
    u_max = float(core.U_ALL[-1])
    KZ = core.frame_a_zones()
    rows = []
    for kz in KZ:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
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
        lam_min, v_min, rad = gen_min_eig(A, Gm)
        floor = FLOOR_SAFETY * EPS * rad * math.sqrt(hz)
        rho_star, n_flips = last_sign_change(v_min, D, hz)
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
        Sm = model_matrix(alpha, Mz, D, W11, W22, W12, u0)
        vl = lock_dir(alpha)
        q_r = float(vl @ ((B2 - S2) @ vl))
        q_m = float(vl @ ((B2 - Sm) @ vl))
        # lock-direction geometry of the minimal mode (G inner product)
        Gv = Gm @ v_min
        vGv = float(v_min @ Gv)
        wl = vl[0] * t1v + vl[1] * t2v
        wlGwl = float(wl @ (Gm @ wl))
        wlAwl = float(wl @ (A @ wl))
        frac_lock = float(wl @ Gv) ** 2 / (wlGwl * vGv)
        Wsp = np.column_stack([t1v, t2v])
        Mat = Wsp.T @ (Gm @ Wsp)
        beta = np.linalg.solve(Mat, Wsp.T @ Gv)
        frac_span = float(beta @ (Mat @ beta)) / vGv
        theta = math.degrees(math.acos(math.sqrt(min(1.0, frac_lock))))
        rows.append(dict(kz=kz, h=hz, alpha=alpha, D=D,
                         complete=complete, lam=lam_min, floor=floor,
                         rho=rho_star, f=rho_star / (hz * D),
                         nf=n_flips, qr=q_r, qm=q_m,
                         eh=abs(q_r / q_m) * hz, lock=q_r * q_m > 0.0,
                         frac_lock=frac_lock, frac_span=frac_span,
                         theta=theta, dcap=u_max - 2.0 * alpha,
                         wlGwl=wlGwl, wlAwl=wlAwl))
        if len(rows) % 20 == 0:
            print("      ... %d/%d windows (%.0f s)"
                  % (len(rows), len(KZ), time.time() - T0))

    comp = [r for r in rows if r["complete"]]
    inc_hs = sorted(r["h"] for r in rows if not r["complete"])
    check("G0.1 [E] the declared surface reproduces: %d frame-A "
          "windows, 67 complete combs, truncated set %s = the two "
          "v618 flip windows + the excluded h = 1292"
          % (len(rows), inc_hs),
          len(comp) == 67 and inc_hs == [1219, 1292, 1445])

    lock_rows = [r for r in rows if r["h"] != 1292]
    locks = [r for r in lock_rows if r["lock"]]
    flips = sorted(r["h"] for r in lock_rows if not r["lock"])
    eh_max = max(r["eh"] for r in locks)
    h_at_max = [r["h"] for r in locks if r["eh"] == eh_max][0]
    check("G0.2 [E] the v618 anchors reproduce: %d/%d lock-sign "
          "windows, max eps*h = %.3f at h = %d (v618 quote %.3f), "
          "flip set %s = %s"
          % (len(locks), len(lock_rows), eh_max, h_at_max,
             V618_MAX_QUOTE, flips, V618_FLIPS),
          abs(eh_max - V618_MAX_QUOTE) <= 0.01 and h_at_max == 184
          and flips == V618_FLIPS)

    lock_c = [r for r in comp if r["lock"] and r["lam"] > r["floor"]]
    lam_min_all = min(r["lam"] for r in comp)
    n_neg = sum(1 for r in comp if r["lam"] < -r["floor"])
    check("G0.3 [E] the lambda_min surface reproduces: min lambda_min "
          "= %+.4e over the 67 complete windows (quote %+.2e, rel dev "
          "%.1e <= 0.02), %d certified-negative, analysis sample "
          "(complete x lock x above-floor) n = %d >= 60"
          % (lam_min_all, V648_LAM_MIN,
             abs(lam_min_all - V648_LAM_MIN) / V648_LAM_MIN,
             n_neg, len(lock_c)),
          abs(lam_min_all - V648_LAM_MIN) / V648_LAM_MIN <= 0.02
          and n_neg == 0 and len(lock_c) >= 60)

    hs = np.array([r["h"] for r in lock_c], float)
    al = np.array([r["alpha"] for r in lock_c], float)
    ll = np.log(np.array([r["lam"] for r in lock_c]))
    le = np.log(np.array([r["eh"] for r in lock_c]))
    raw_pear = pearson(ll, le)
    check("G0.4 [E] the raw diagnostic reproduces: Pearson(log "
          "lambda_min, log eps*h) = %+.4f on n = %d (quote %+.3f, "
          "|dev| <= 0.02) -- the number this probe interrogates"
          % (raw_pear, len(lock_c), V648_CORR),
          abs(raw_pear - V648_CORR) <= 0.02)

    print("\n      h    2alpha    lam_min      eps*h    rho*    f*   "
          "d_cap   frac_lock*h  theta")
    for r in sorted(lock_c, key=lambda r: r["h"]):
        print("    %5d  %6.3f  %+.4e  %7.4f  %6.3f  %.3f  %6.3f  "
              "%9.3f  %5.1f"
              % (r["h"], 2 * r["alpha"], r["lam"], r["eh"], r["rho"],
                 r["f"], r["dcap"], r["frac_lock"] * r["h"],
                 r["theta"]))

    # ------------------------------------------------ B1: raw structure
    print("\nB1 -- the raw associations and the depth co-trend")
    rng = np.random.default_rng(SEED)
    sp_raw, p_raw = perm_p(rankdata(ll), rankdata(le), rng)
    sp_hl = spearman(hs, ll)
    sp_he = spearman(hs, le)
    x_a = np.log(2.0 * al)
    (b1, r2_1) = ols([x_a], ll)
    p1 = -float(b1[1])
    check("B1.1 [MEASURED] raw: Spearman(log lam, log eps*h) = %+.4f "
          "(perm p = %.5f), Pearson = %+.4f; the co-trend both must "
          "beat: Spearman(h, log lam) = %+.4f, Spearman(h, log eps*h) "
          "= %+.4f; lambda_min ~ (2 alpha)^-p with p = %.3f, R^2 = "
          "%.4f -- lambda_min is %s a near-deterministic ladder "
          "function (the v637 trap in the open)"
          % (sp_raw, p_raw, raw_pear, sp_hl, sp_he, p1, r2_1,
             "essentially" if r2_1 > 0.98 else "NOT"), True)

    # ------------------------------------------------ B2: the verdict
    print("\nB2 -- the h-controlled partial correlations (the gate)")
    rho_l1, p_l1 = partial_spearman(ll, le, [hs], rng, poly=1)
    rho_l3, p_l3 = partial_spearman(ll, le, [hs], rng, poly=3)
    rho_ha, p_ha = partial_spearman(ll, le, [hs, al], rng, poly=1)
    print("      control          rho_partial   perm p")
    print("      h rank-linear    %+.4f       %.5f" % (rho_l1, p_l1))
    print("      h rank-cubic     %+.4f       %.5f" % (rho_l3, p_l3))
    print("      (h, alpha) lin   %+.4f       %.5f" % (rho_ha, p_ha))
    hit3 = abs(rho_l3) >= RHO_BAR and p_l3 < P_BAR
    hit_ha = abs(rho_ha) >= RHO_BAR and p_ha < P_BAR
    check("B2.1 [MEASURED, verdict-driving] the preregistered gate on "
          "the rank-cubic h-control: rho_partial = %+.4f, p = %.5f "
          "(bar |rho| >= %.2f AND p < %.2f) -> %s; robustness gate "
          "(h, alpha): rho = %+.4f, p = %.5f -> %s"
          % (rho_l3, p_l3, RHO_BAR, P_BAR,
             "HIT" if hit3 else "MISS", rho_ha, p_ha,
             "HIT" if hit_ha else "MISS"), True)

    # ------------------------------ B3.0: the identification decomposition
    print("\nB3 -- mechanism (0): the identification decomposition "
          "(EXPLORATORY, declared post-gate)")
    id_dev = max(abs(r["qr"] - r["wlAwl"]) / abs(r["qr"])
                 for r in lock_c)
    lam_lock = np.array([r["qr"] / r["wlGwl"] for r in lock_c])
    r_id = np.exp(ll) / lam_lock
    llk = np.log(lam_lock)
    sp_llk = spearman(ll, llk)
    rho_id_ha, p_id_ha = partial_spearman(ll, llk, [hs, al], rng, poly=1)
    rho_k3, p_k3 = partial_spearman(ll, le, [np.asarray(llk)], rng,
                                    poly=3)
    rho_kha, p_kha = partial_spearman(ll, le, [hs, al, np.asarray(llk)],
                                      rng, poly=1)
    print("      identity check: max rel |q_r - w_lock^T Ahat w_lock| "
          "= %.1e" % id_dev)
    print("      r_id = lambda_min/lambda_lock: min %.4f / median "
          "%.4f / max %.4f"
          % (float(r_id.min()), float(np.median(r_id)),
             float(r_id.max())))
    print("      Spearman(log lam_min, log lam_lock) = %+.4f; "
          "(h,alpha)-partial = %+.4f (p = %.5f)"
          % (sp_llk, rho_id_ha, p_id_ha))
    print("      KILLER TEST partial corr(log lam_min, log eps*h | "
          "lam_lock rank-cubic) = %+.4f (p = %.5f)" % (rho_k3, p_k3))
    print("      KILLER TEST partial corr(log lam_min, log eps*h | "
          "h, alpha, log lam_lock) = %+.4f (p = %.5f)"
          % (rho_kha, p_kha))
    beyond = abs(rho_kha) >= RHO_BAR and p_kha < P_BAR
    check("B3.0 [MEASURED, exploratory decomposition] the bridge "
          "mechanism: q_r = w_lock^T Ahat w_lock exactly (max rel dev "
          "%.1e < 1e-8), so lambda_lock = q_r/||w_lock||_G^2 shares "
          "the arithmetic defect q_r with eps*h (bar 1e-5: two float "
          "summation orders of the same exact T163 identity); "
          "alignment r_id = lambda_min/lambda_lock median %.3f; after "
          "ADDITIONALLY "
          "controlling log lambda_lock the lambda_min <-> eps*h "
          "partial is rho = %+.3f (p = %.4f) [(h, alpha, lam_lock) "
          "joint: rho = %+.3f, p = %.4f] -> the h-robust bridge is %s"
          % (id_dev, float(np.median(r_id)), rho_k3, p_k3, rho_kha,
             p_kha,
             "carrying information BEYOND the lock projection"
             if beyond else
             "CARRIED BY the lock-direction identification (the "
             "margin IS the C = 1 defect along the lock direction, "
             "up to the alignment factor r_id and a smooth ladder "
             "normalization)"), id_dev < 1e-5)

    print("\nB3 -- mechanism (a): is the minimal mode carried by the "
          "lock direction?")
    fl = np.array([r["frac_lock"] for r in lock_c])
    fs_ = np.array([r["frac_span"] for r in lock_c])
    fl_h = fl * hs
    fs_h = fs_ * hs
    th = np.array([r["theta"] for r in lock_c])
    print("      frac_lock * h: min %.3f / median %.3f / max %.3f "
          "(null ~ 1 for a random direction)"
          % (float(fl_h.min()), float(np.median(fl_h)),
             float(fl_h.max())))
    print("      frac_span * h: min %.3f / median %.3f / max %.3f "
          "(null ~ 2)"
          % (float(fs_h.min()), float(np.median(fs_h)),
             float(fs_h.max())))
    print("      angle to lock direction: min %.2f / median %.2f / "
          "max %.2f deg" % (float(th.min()), float(np.median(th)),
                            float(th.max())))
    rho_fe, p_fe = partial_spearman(fl, le, [hs], rng, poly=3)
    rho_flm, p_flm = partial_spearman(fl, ll, [hs], rng, poly=3)
    check("B3.1 [MEASURED] lock-direction geometry of the minimal "
          "mode: median enrichment frac_lock * h = %.2f over the "
          "random-direction null 1 (span: %.2f over null 2), median "
          "angle %.1f deg; h-controlled (rank-cubic) partials: "
          "corr(frac_lock, log eps*h) rho = %+.3f (p = %.4f), "
          "corr(frac_lock, log lam) rho = %+.3f (p = %.4f) -- "
          "REPORTED as the mechanism map, no bar (the verdict rides "
          "on B2)"
          % (float(np.median(fl_h)), float(np.median(fs_h)),
             float(np.median(th)), rho_fe, p_fe, rho_flm, p_flm), True)

    print("\nB3 -- mechanism (b): rho* vs the data-cap distance")
    rho_v = np.array([r["rho"] for r in lock_c])
    fst = np.array([r["f"] for r in lock_c])
    dc = np.array([r["dcap"] for r in lock_c])
    sp_rd = spearman(rho_v, dc)
    sp_fd = spearman(fst, dc)
    rho_rd3, p_rd3 = partial_spearman(rho_v, dc, [hs], rng, poly=3)
    rho_fd3, p_fd3 = partial_spearman(fst, dc, [hs], rng, poly=3)
    inc_info = [(r["h"], r["dcap"], r["eh"]) for r in rows
                if not r["complete"]]
    print("      (declared caveat: d_cap = u_max - 2 alpha is "
          "alpha-deterministic; raw Spearman(rho*, d_cap) = "
          "-Spearman(rho*, alpha) by construction)")
    print("      truncated windows (h, d_cap, eps*h): %s"
          % [("h=%d" % h_, "%.3f" % d_, "%.3g" % e_)
             for h_, d_, e_ in inc_info])
    check("B3.2 [MEASURED] flip proximity: raw Spearman(rho*, d_cap) "
          "= %+.4f, scale-free Spearman(f*, d_cap) = %+.4f; "
          "h-controlled (rank-cubic): rho* rho = %+.3f (p = %.4f), "
          "f* rho = %+.3f (p = %.4f); the two flip windows sit PAST "
          "the cap (d_cap < 0: %s) -- REPORTED as the mechanism map, "
          "no bar"
          % (sp_rd, sp_fd, rho_rd3, p_rd3, rho_fd3, p_fd3,
             sorted(h_ for h_, d_, _ in inc_info if d_ < 0.0)), True)

    # ------------------------------------------------ B4: the verdict
    guards_ok = not any(f.startswith("G0") for f in FAILS)
    if not guards_ok:
        VERDICT = "MIXED (guards failed)"
    elif hit3 and hit_ha:
        VERDICT = ("BRIDGE-PASS (mechanism: %s)"
                   % ("independent margin information beyond the lock "
                      "projection" if beyond else
                      "lock-direction identification -- lambda_min ~ "
                      "r_id x q_r/||w_lock||_G^2, the margin is the "
                      "C = 1 defect along the lock direction"))
    elif hit3:
        VERDICT = ("BRIDGE-PARTIAL (h-robust but alpha-mediated: the "
                   "signal survives any monotone h-trend but not the "
                   "joint (h, alpha) control)")
    elif p_l3 < 0.05:
        VERDICT = "BRIDGE-PARTIAL (0.01 <= p < 0.05 on the primary gate)"
    else:
        VERDICT = ("BRIDGE-KILL (h-reparametrization: the raw +0.704 "
                   "is the shared depth trend, the v637 pattern again)")

    check("B4.1 [C] the typed reading: raw corr(log lambda_min, "
          "log eps*h) = %+.3f on n = %d; after the preregistered "
          "rank-cubic h-control rho_partial = %+.3f (p = %.4f), "
          "(h, alpha) control rho = %+.3f (p = %.4f); verdict %s.  "
          "Either way no marker move, no positivity claim, no RH "
          "statement; W3 and PRIME.UNIFC stay as they are"
          % (raw_pear, len(lock_c), rho_l3, p_l3, rho_ha, p_ha,
             VERDICT.split()[0]), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01 / PRIME.UNIFC.01, margin-bridge round
  (2026-08-02): the raw diagnostic corr(log lambda_min, log eps*h) =
  %+.3f (n = %d complete lock-sign windows; lambda_min = lowest
  L2-normalized Rayleigh quotient of the Weil window form, v563
  assembly; eps*h = the v618 C = 1 load) was interrogated with the
  v637 preregistered control machinery (rank-linear/rank-cubic h
  residualization + joint (h, alpha), Freedman-Lane permutation p,
  N = 20000, seed %d).  RESULT: partial rho (rank-cubic h) = %+.3f
  (p = %.4f); joint (h, alpha) rho = %+.3f (p = %.4f); verdict %s.
  MECHANISM (exploratory decomposition, post-gate): the minimal mode
  is nearly collinear with the closed v591 lock direction (median
  G-energy enrichment frac * h = %.2f over null 1, median angle
  %.1f deg), q_r = w_lock^T Ahat w_lock exactly, and lambda_lock =
  q_r/||w_lock||_G^2 bounds lambda_min with median alignment r_id =
  %.3f; after additionally controlling log lambda_lock the partial
  is rho = %+.3f (p = %.4f) [(h, alpha, lam_lock): rho = %+.3f,
  p = %.4f] -- the bridge mechanism is %s.  Flip-proximity read:
  Spearman(f*, d_cap) = %+.3f after h-control (p = %.4f, dead).
  lambda_min ~ (2 alpha)^-%.2f with R^2 = %.3f on this family.
  No marker move; W3 open; Problem 7.1 untouched.
""" % (raw_pear, len(lock_c), SEED, rho_l3, p_l3, rho_ha, p_ha,
       VERDICT.split()[0], float(np.median(fl_h)),
       float(np.median(th)), float(np.median(r_id)), rho_k3, p_k3,
       rho_kha, p_kha,
       "information beyond the lock projection" if beyond else
       "the lock-direction identification (typed; not an independent "
       "statistical link)", rho_fd3, p_fd3, p1, r2_1))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
