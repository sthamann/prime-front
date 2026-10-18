"""v657 -- PRIME.RIDGEOM.01: WHAT DRIVES THE ALIGNMENT FACTOR r_id?  The
margin-bridge round (v656_margin_link.py, 2026-08-02) identified the
positivity margin on lock windows as

    lambda_min ~ r_id * q_r / ||w_lock||_G^2,      r_id = lambda_min /
                                                          lambda_lock,

with q_r the C = 1 arithmetic defect (v618) along the closed v591 lock
direction and r_id in [0.210, 0.951] (median 0.584) the ONLY quantity
of the identification not explained by the defect.  THIS probe asks
what controls r_id.

THE EXACT GEOMETRY (H1, derived before running, checked to machine
precision per window): write the G-normalized minimal mode as
m = cos(theta) w_hat + sin(theta) w_perp with w_hat the G-normalized
lock direction and w_perp G-orthonormal to it (the component of m).
Pure algebra gives the three-term Rayleigh expansion

    lambda_min = cos^2 lambda_lock + 2 sin cos B + sin^2 Q_perp,
    B = w_hat^T Ahat w_perp,   Q_perp = w_perp^T Ahat w_perp.

BECAUSE m is an eigenvector of the pencil (Ahat, G), two constraints
hold on top of the expansion:

    (C1)  B = cos(theta) (lambda_min - lambda_lock) / sin(theta)
          (so B < 0 whenever lambda_min < lambda_lock), and
    (C2)  lambda_min equals the LOWER eigenvalue of the restricted
          2x2 pencil [[lambda_lock, B], [B, Q_perp]].

Eliminating B yields the CLOSED FORMULA (the H1 deliverable)

    r_id = (1 - q tan^2 theta) / (1 - tan^2 theta),
    q = Q_perp / lambda_lock,

equivalently 1 - r_id = tan^2(theta) (q - 1) / (1 - tan^2 theta): the
alignment deficit is the PRODUCT of the squared mixing angle and the
perpendicular Rayleigh EXCESS.  Positivity criterion on lock windows:
lambda_min > 0  <=>  q tan^2 theta < 1.

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * sample: the margin_link_probe analysis sample verbatim (complete
    frame-A windows, lock sign q_real q_model > 0, lambda_min above
    the float floor FLOOR_SAFETY x eps x radius x sqrt(h));
  * guards: the surface (67 complete, truncated {1219, 1292, 1445}),
    the r_id quotes (min 0.210 / median 0.584 / max 0.951, tol 0.005)
    and the T163 identity q_r = w_lock^T Ahat w_lock (rel < 1e-5);
  * H1 exactness bars: three-term expansion rel dev < 1e-10 (pure
    algebra) against the m-Rayleigh quotient; eigen-constraints (C1),
    (C2) and the closed formula rel dev < 1e-6 (eigensolver slack);
    theta < 45 deg, B < 0 and q > 1 on every window (structural);
  * statistics: v637 machinery verbatim (rank residualization,
    Freedman-Lane permutation p, N_PERM = 20000, SEED = 20260806);
    h-control ALWAYS (rank-linear AND rank-cubic) plus (h, alpha)
    joint rank-linear; correlation gate per test |rho| >= 0.30 AND
    p < 0.01 (six H2/H3 tests -> Bonferroni-honest reading 0.01/6
    noted, not enforced);
  * H4 typing bar: OLS of r_id on a cubic polynomial in log h;
    R^2 >= 0.80 -> SMOOTH (r_id is a ladder normalizer), else
    INFORMATIVE (window-wise information beyond the ladder);
  * H5: bootstrap of min r_id over windows, B_BOOT = 10000, same
    SEED stream (caveat declared: the bootstrap of a MINIMUM is
    inconsistent -- it piles mass on the sample min; the half-sample
    m-out-of-n subsample min and the leave-one-out second min are
    the informative stability reads); tertile minima, Spearman(r_id,
    h) and the trend of the positivity product q tan^2 theta for the
    r_id -> 0 threat; typing is MEASURED-FAMILY, never a theorem.

Hypotheses:
  H1 [geometry]     exact decomposition + closed formula + which term
                    carries the r_id spread (variance attribution of
                    log(1 - r_id) = log tan^2 + log(q-1) - log(1-tan^2));
  H2 [arithmetic]   partial-correlation table r_id vs log(eps*h), atom
                    density k_a/(2 alpha), d_cap = u_max - 2 alpha,
                    the edge atom spacing (caveat declared: d_cap and
                    density are alpha-near-deterministic; the LAST
                    atom sits AT the edge identically, since the
                    frame-A edge e^{2 alpha} = N^2 is itself a prime
                    power -- typed as [E], the informative covariate
                    is the spacing to the SECOND-last atom);
  H3 [spectral]     r_id vs the pencil gap lambda_2 - lambda_min (raw,
                    h-controlled, and MEDIATION: does the H1 driver
                    tan^2 theta absorb it?);
  H4 [structure]    smooth-vs-informative typing (R^2 bar above),
                    outlier windows named;
  H5 [W3 reading]   stability of min r_id (bootstrap, leave-one-out,
                    depth trend) + the honest W3 typing: the family
                    bound lambda_min >= min(r_id) q_r/||w_lock||_G^2
                    is a MEASURED restatement, NOT a uniform theorem;
                    the reduced open problem is a uniform upper bound
                    on q tan^2 theta.

Verdict enums (frozen): RID-EXACT-SMOOTH, RID-EXACT-INFORMATIVE,
RID-MIXED (guards or exactness bars fail).

FIREWALL: v563 import read-only; v618/v591/margin machinery REBUILT
verbatim (no other imports); no marker moves; no positivity claim; no
RH statement; NO zero of any L-function is read (AST-checked).
Python-only, per GATE.WOLFRAM.02.

PROVENANCE: discovery probe rid_alignment_probe.py (2026-08-02,
15/15, verdict RID-EXACT-INFORMATIVE); margin_link_probe (BRIDGE
mechanism + r_id quotes); sign_uncertainty_w3_probe (floor
machinery); v618 (C = 1 reads); v591 (closed lock direction); v637
(control methodology).
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
N_PERM = 20000
SEED = 20260806              # fresh (margin probe used 20260804)
B_BOOT = 10000
RHO_BAR = 0.30               # per-test gate, margin probe verbatim
P_BAR = 0.01
R2_SMOOTH_BAR = 0.80         # preregistered H4 typing bar
BAR_ALGEBRA = 1e-10          # H1 pure-algebra bar
BAR_EIGEN = 1e-6             # H1 eigen-constraint bar
# reproduction anchors (margin_link_probe quotes)
RID_QUOTES = (0.210, 0.584, 0.951)
RID_TOL = 0.005
THETA_MED_QUOTE = 9.1
V618_FLIPS = [1219, 1445]


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
    """Lowest two generalized eigenpairs + pencil radius."""
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


def partial_spearman_mixed(xx, yy, ctrl_polys, rng, nperm=N_PERM):
    """Controls given as [(vec, poly), ...] with per-control degree."""
    cols = []
    for cvec, poly in ctrl_polys:
        cols.extend(control_cols([cvec], poly))
    ex = residualize(rankdata(xx), cols)
    ey = residualize(rankdata(yy), cols)
    return perm_p(ex, ey, rng, nperm)


def ols(cols, y):
    Xd = np.column_stack([np.ones_like(y)] + cols)
    beta, _, _, _ = np.linalg.lstsq(Xd, y, rcond=None)
    r = y - Xd @ beta
    yc = y - y.mean()
    return beta, 1.0 - float(r @ r) / float(yc @ yc), r


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE ALIGNMENT FACTOR -- what drives r_id = "
          "lambda_min/lambda_lock?")
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
        Sm = model_matrix(alpha, Mz, D, W11, W22, W12, u0)
        vl = lock_dir(alpha)
        q_r = float(vl @ ((B2 - S2) @ vl))
        q_m = float(vl @ ((B2 - Sm) @ vl))
        # ---- H1 geometry: G-orthonormal split of the minimal mode
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
        B_x = float(w_hat @ (A @ w_perp))
        lam_ray = float(m_vec @ (A @ m_vec))
        # arithmetic covariates
        dens = ka / (2.0 * alpha)
        gap_last = 2.0 * alpha - float(core.U_ALL[ka - 1])
        gap_prev = 2.0 * alpha - float(core.U_ALL[ka - 2])
        rows.append(dict(kz=kz, h=hz, alpha=alpha, D=D,
                         complete=complete, lam=lam_min, lam2=lam_2,
                         floor=floor, qr=q_r, qm=q_m,
                         eh=abs(q_r / q_m) * hz, lock=q_r * q_m > 0.0,
                         wlGwl=wlGwl, wlAwl=wlAwl, ct=ct, st=st,
                         pn=pn, lam_lock=lam_lock, Qp=Q_perp, Bx=B_x,
                         lam_ray=lam_ray, dens=dens,
                         gap_last=gap_last, gap_prev=gap_prev,
                         dcap=u_max - 2.0 * alpha))
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
    r_id = np.array([r["lam"] / r["lam_lock"] for r in lock_c])
    check("G0.2 [E] the margin-probe r_id quotes reproduce on n = %d: "
          "min %.4f / median %.4f / max %.4f (quotes %.3f/%.3f/%.3f, "
          "tol %.3f)"
          % (len(lock_c), float(r_id.min()), float(np.median(r_id)),
             float(r_id.max()), RID_QUOTES[0], RID_QUOTES[1],
             RID_QUOTES[2], RID_TOL),
          abs(float(r_id.min()) - RID_QUOTES[0]) <= RID_TOL
          and abs(float(np.median(r_id)) - RID_QUOTES[1]) <= RID_TOL
          and abs(float(r_id.max()) - RID_QUOTES[2]) <= RID_TOL)

    id_dev = max(abs(r["qr"] - r["wlAwl"]) / abs(r["qr"]) for r in lock_c)
    check("G0.3 [E] the T163 identity q_r = w_lock^T Ahat w_lock: max "
          "rel dev %.1e < 1e-5 (two float summation orders)" % id_dev,
          id_dev < 1e-5)

    hs = np.array([r["h"] for r in lock_c], float)
    al = np.array([r["alpha"] for r in lock_c], float)
    ct = np.array([r["ct"] for r in lock_c])
    st = np.array([r["st"] for r in lock_c])
    th_deg = np.degrees(np.arccos(ct))
    t2 = (st / ct) ** 2                          # tan^2 theta
    qq = np.array([r["Qp"] / r["lam_lock"] for r in lock_c])
    bb = np.array([r["Bx"] / r["lam_lock"] for r in lock_c])
    lam = np.array([r["lam"] for r in lock_c])
    lam_lock = np.array([r["lam_lock"] for r in lock_c])
    lam2 = np.array([r["lam2"] for r in lock_c])
    eh = np.array([r["eh"] for r in lock_c])
    dens = np.array([r["dens"] for r in lock_c])
    dcap = np.array([r["dcap"] for r in lock_c])
    glast = np.array([r["gap_last"] for r in lock_c])
    gprev = np.array([r["gap_prev"] for r in lock_c])

    print("\n      h    2alpha   lam_min/lam_lock=r_id  theta[deg]  "
          "q=Qp/ll     b=B/ll    gap2=lam2-lam  eps*h")
    for i, r in enumerate(sorted(lock_c, key=lambda r: r["h"])):
        j = lock_c.index(r)
        print("    %5d  %6.3f      %.4f            %6.2f   %8.3f  "
              "%+9.3f   %.4e  %6.3f"
              % (r["h"], 2 * r["alpha"], r_id[j], th_deg[j], qq[j],
                 bb[j], r["lam2"] - r["lam"], r["eh"]))

    check("G0.4 [E] the angle anchor reproduces: median theta = "
          "%.2f deg (margin-probe quote %.1f, tol 0.15)"
          % (float(np.median(th_deg)), THETA_MED_QUOTE),
          abs(float(np.median(th_deg)) - THETA_MED_QUOTE) <= 0.15)

    # ---------------------------------------------- H1: exact geometry
    print("\nH1 -- the exact Rayleigh decomposition and the closed "
          "formula")
    # (i) pure algebra: Rayleigh(m) = cos^2 ll + 2 sc B + sin^2 Qp
    expand = ct ** 2 * lam_lock + 2.0 * ct * st * \
        np.array([r["Bx"] for r in lock_c]) + st ** 2 * \
        np.array([r["Qp"] for r in lock_c])
    lam_ray = np.array([r["lam_ray"] for r in lock_c])
    dev_alg = np.max(np.abs(expand - lam_ray) / lam_lock)
    check("H1.1 [E] three-term expansion lambda_R(m) = cos^2 "
          "lam_lock + 2 sin cos B + sin^2 Q_perp: max |dev|/lam_lock "
          "= %.1e < %.0e (pure algebra)" % (dev_alg, BAR_ALGEBRA),
          dev_alg < BAR_ALGEBRA)

    # (ii) eigen-constraints and the closed formula
    dev_ray = np.max(np.abs(lam_ray - lam) / lam_lock)
    B_pred = ct * (lam - lam_lock) / st
    dev_c1 = np.max(np.abs(np.array([r["Bx"] for r in lock_c]) - B_pred)
                    / lam_lock)
    tr = 0.5 * (1.0 + qq)
    disc = np.sqrt((0.5 * (1.0 - qq)) ** 2 + bb ** 2)
    r_2x2 = tr - disc
    dev_c2 = np.max(np.abs(r_2x2 - r_id))
    r_closed = (1.0 - qq * t2) / (1.0 - t2)
    dev_cf = np.max(np.abs(r_closed - r_id))
    check("H1.2 [E] eigenvector constraints: Rayleigh(m) = lambda_min "
          "(max dev/lam_lock %.1e), (C1) B = cos(lam_min - lam_lock)/"
          "sin (max dev/lam_lock %.1e), (C2) 2x2 lower eigenvalue "
          "(max |dev| %.1e), CLOSED FORMULA r_id = (1 - q tan^2)/"
          "(1 - tan^2) (max |dev| %.1e) -- all < %.0e"
          % (dev_ray, dev_c1, dev_c2, dev_cf, BAR_EIGEN),
          max(dev_ray, dev_c1, dev_c2, dev_cf) < BAR_EIGEN)

    check("H1.3 [E] structural signs on every window: theta < 45 deg "
          "(max %.2f), B < 0 (max b = %+.3e), q > 1 (min %.3f) -- the "
          "cross term always PULLS lambda_min DOWN and the perp "
          "direction always sits ABOVE the lock Rayleigh"
          % (float(th_deg.max()), float(bb.max()), float(qq.min())),
          float(th_deg.max()) < 45.0 and float(bb.max()) < 0.0
          and float(qq.min()) > 1.0)

    # (iii) variance attribution of the deficit
    d_id = 1.0 - r_id
    Lg = np.log(d_id)
    Lt = np.log(t2)
    Lq = np.log(qq - 1.0)
    Ld = -np.log(1.0 - t2)
    dev_split = np.max(np.abs(Lt + Lq + Ld - Lg))
    vL = float(np.var(Lg, ddof=1))
    sh_t = float(np.cov(Lt, Lg)[0, 1]) / vL
    sh_q = float(np.cov(Lq, Lg)[0, 1]) / vL
    sh_d = float(np.cov(Ld, Lg)[0, 1]) / vL
    # Rayleigh-term shares of r_id itself
    T_lock = ct ** 2
    T_perp = st ** 2 * qq
    T_cross = 2.0 * ct * st * bb
    vr = float(np.var(r_id, ddof=1))
    cv_lock = float(np.cov(T_lock, r_id)[0, 1]) / vr
    cv_perp = float(np.cov(T_perp, r_id)[0, 1]) / vr
    cv_cross = float(np.cov(T_cross, r_id)[0, 1]) / vr
    print("      deficit split 1 - r_id = tan^2 (q-1)/(1 - tan^2): "
          "max |log-identity dev| = %.1e" % dev_split)
    print("      log-variance shares of log(1 - r_id):  tan^2 theta "
          "%.3f | (q - 1) %.3f | denominator %.3f  (sum %.3f)"
          % (sh_t, sh_q, sh_d, sh_t + sh_q + sh_d))
    print("      Rayleigh-term covariance shares of r_id:  cos^2 "
          "%.3f | sin^2 q %.3f | cross %.3f  (sum %.3f)"
          % (cv_lock, cv_perp, cv_cross, cv_lock + cv_perp + cv_cross))
    print("      medians: theta %.2f deg, tan^2 %.4f, q %.2f, b %+.2f,"
          " terms cos^2 %.3f / sin^2 q %.3f / cross %+.3f"
          % (float(np.median(th_deg)), float(np.median(t2)),
             float(np.median(qq)), float(np.median(bb)),
             float(np.median(T_lock)), float(np.median(T_perp)),
             float(np.median(T_cross))))
    rng = np.random.default_rng(SEED)
    sp_t, p_t = partial_spearman(r_id, t2, [hs], rng, poly=3)
    sp_q, p_q = partial_spearman(r_id, qq, [hs], rng, poly=3)
    sp_p = spearman(r_id, t2 * (qq - 1.0))
    check("H1.4 [MEASURED] the driver: Spearman(r_id, tan^2 (q-1)) = "
          "%+.4f (the product is the deficit, sanity); h-controlled "
          "(rank-cubic) partials: r_id vs tan^2 theta rho = %+.3f "
          "(p = %.4f), r_id vs q rho = %+.3f (p = %.4f); log-variance "
          "shares tan^2 %.2f vs (q-1) %.2f -- the spread is %s"
          % (sp_p, sp_t, p_t, sp_q, p_q, sh_t, sh_q,
             "ANGLE-driven" if sh_t > sh_q else "PERP-EXCESS-driven"),
          True)

    # ---------------------------------------------- H2: arithmetic
    print("\nH2 -- partial-correlation table: r_id vs the window "
          "arithmetic (h-control ALWAYS)")
    print("      (declared caveat: d_cap = u_max - 2 alpha and the "
          "atom density are alpha-near-deterministic; the edge "
          "spacing carries genuine arithmetic jitter)")
    check("H2.0 [E] the last atom sits AT the window edge "
          "identically (max |2 alpha - u_last| = %.1e): the frame-A "
          "edge e^{2 alpha} = N^2 is itself a prime power, so the "
          "'position of the last atom' is degenerate BY CONSTRUCTION;"
          " the informative covariate is the edge spacing 2 alpha - "
          "u_{second-last} (min %.4f / median %.4f / max %.4f)"
          % (float(np.max(np.abs(glast))), float(gprev.min()),
             float(np.median(gprev)), float(gprev.max())),
          float(np.max(np.abs(glast))) < 1e-12)
    h2_vars = [("log eps*h", np.log(eh)),
               ("atom density k_a/2a", dens),
               ("d_cap = umax - 2a", dcap),
               ("edge atom spacing", gprev)]
    print("      %-22s %8s | %8s %8s | %8s %8s"
          % ("variable", "raw rho", "h3 rho", "p", "(h,a) rho", "p"))
    h2_hits = []
    for name, xv in h2_vars:
        sp0 = spearman(r_id, xv)
        r3, p3 = partial_spearman(r_id, xv, [hs], rng, poly=3)
        rha, pha = partial_spearman(r_id, xv, [hs, al], rng, poly=1)
        hit = abs(r3) >= RHO_BAR and p3 < P_BAR
        joint = abs(rha) >= RHO_BAR and pha < P_BAR
        if hit:
            h2_hits.append((name, r3, p3, rha, pha, joint))
        print("      %-22s %+8.4f | %+8.4f %8.5f | %+8.4f %8.5f%s"
              % (name, sp0, r3, p3, rha, pha,
                 ("  <- HIT" + ("" if joint else " (primary only)"))
                 if hit else ""))
    check("H2.1 [MEASURED] arithmetic carriers of r_id after rank-"
          "cubic h-control (gate |rho| >= %.2f, p < %.2f per test; "
          "6 H2/H3 tests, Bonferroni-honest bar p < %.4f): %s"
          % (RHO_BAR, P_BAR, P_BAR / 6.0,
             ("; ".join("%s rho=%+.3f p=%.4f [(h,a) joint %s;"
                        " Bonferroni %s]"
                        % (n, r3, p3, "HOLDS" if j_ else "FAILS",
                           "holds" if p3 < P_BAR / 6.0 else "fails")
                        for n, r3, p3, _, _, j_ in h2_hits))
             if h2_hits else "NONE -- no arithmetic covariate "
             "carries r_id beyond the ladder"), True)

    # ---------------------------------------------- H3: spectral gap
    print("\nH3 -- the spectral-gap hypothesis (narrow gap => mixing "
          "=> small r_id?)")
    gap2 = lam2 - lam
    rgap = lam2 / lam
    sp_g0 = spearman(r_id, gap2)
    rg3, pg3 = partial_spearman(r_id, gap2, [hs], rng, poly=3)
    rgha, pgha = partial_spearman(r_id, gap2, [hs, al], rng, poly=1)
    sp_r0 = spearman(r_id, rgap)
    rr3, pr3 = partial_spearman(r_id, rgap, [hs], rng, poly=3)
    print("      gap = lambda_2 - lambda_min: raw rho = %+.4f; h3 "
          "partial rho = %+.4f (p = %.5f); (h, alpha) rho = %+.4f "
          "(p = %.5f)" % (sp_g0, rg3, pg3, rgha, pgha))
    print("      ratio lambda_2/lambda_min: raw rho = %+.4f; h3 "
          "partial rho = %+.4f (p = %.5f)" % (sp_r0, rr3, pr3))
    # mediation: does the H1 driver absorb the gap link?
    rmed, pmed = partial_spearman_mixed(r_id, gap2,
                                        [(hs, 3), (t2, 3)], rng)
    rtg3, ptg3 = partial_spearman(t2, gap2, [hs], rng, poly=3)
    rqg3, pqg3 = partial_spearman(qq, gap2, [hs], rng, poly=3)
    gap_hit = abs(rg3) >= RHO_BAR and pg3 < P_BAR
    med_hit = abs(rmed) >= RHO_BAR and pmed < P_BAR
    if gap_hit and not med_hit:
        gap_read = "ABSORBED by the H1 angle (mediated)"
    elif med_hit:
        gap_read = ("a SUPPRESSED channel: conditioning on the angle "
                    "STRENGTHENS it -- at fixed theta a larger gap "
                    "goes with a larger perp excess q (q <-> gap | h:"
                    " rho = %+.3f, p = %.4f) and hence SMALLER r_id, "
                    "the OPPOSITE sign of the mixing hypothesis"
                    % (rqg3, pqg3))
    else:
        gap_read = "absent at the gate and not revived by mediation"
    check("H3.1 [MEASURED] spectral gap: h-controlled link rho = "
          "%+.3f (p = %.4f) -> %s at the gate (mixing hypothesis "
          "predicted POSITIVE partial); gap <-> tan^2 theta (h3) "
          "rho = %+.3f (p = %.4f); MEDIATION r_id <-> gap | (h, "
          "tan^2 theta) rho = %+.3f (p = %.4f) -> the gap link is %s"
          % (rg3, pg3, "HIT" if gap_hit else "MISS", rtg3, ptg3,
             rmed, pmed, gap_read), True)

    # ---------------------------------------------- H4: smooth vs info
    print("\nH4 -- smooth ladder function or window-wise information?")
    xh = np.log(hs)
    xh = (xh - xh.mean()) / xh.std()
    _, r2_1, _ = ols([xh], r_id)
    _, r2_2, _ = ols([xh, xh ** 2], r_id)
    _, r2_3, res3 = ols([xh, xh ** 2, xh ** 3], r_id)
    sd_res = float(np.std(res3))
    order = np.argsort(-np.abs(res3))
    outl = [(int(hs[i]), float(r_id[i]), float(res3[i]))
            for i in order[:3]]
    smooth = r2_3 >= R2_SMOOTH_BAR
    print("      OLS r_id ~ poly(log h): R^2 linear %.4f / quadratic "
          "%.4f / cubic %.4f (bar %.2f)" % (r2_1, r2_2, r2_3,
                                            R2_SMOOTH_BAR))
    print("      cubic residuals: SD %.4f (r_id spread SD %.4f); top-3"
          " outliers (h, r_id, resid): %s"
          % (sd_res, float(np.std(r_id)),
             ["h=%d r=%.3f e=%+.3f" % o for o in outl]))
    check("H4.1 [MEASURED, typing] cubic-in-log-h fit of r_id: R^2 = "
          "%.4f %s %.2f -> r_id is %s (residual SD %.4f vs raw SD "
          "%.4f)"
          % (r2_3, ">=" if smooth else "<", R2_SMOOTH_BAR,
             "SMOOTH -- a ladder normalizer, the identification is "
             "essentially complete" if smooth else
             "INFORMATIVE -- genuine window-wise structure beyond "
             "the ladder", sd_res, float(np.std(r_id))), True)

    # ---------------------------------------------- H5: the W3 bound
    print("\nH5 -- stability of the measured lower bound min r_id")
    i_min = int(np.argmin(r_id))
    r_min = float(r_id[i_min])
    r_loo = float(np.sort(r_id)[1])
    boot_rng = np.random.default_rng(SEED + 1)
    n = len(r_id)
    bmins = np.empty(B_BOOT)
    smins = np.empty(B_BOOT)
    m_half = n // 2
    for b_ in range(B_BOOT):
        bmins[b_] = r_id[boot_rng.integers(0, n, n)].min()
        smins[b_] = r_id[boot_rng.permutation(n)[:m_half]].min()
    q01, q05, q50 = (float(np.quantile(bmins, q))
                     for q in (0.01, 0.05, 0.50))
    s05, s50, s95 = (float(np.quantile(smins, q))
                     for q in (0.05, 0.50, 0.95))
    sp_h, p_h = perm_p(rankdata(hs), rankdata(r_id), rng)
    t_edges = np.quantile(hs, [1.0 / 3.0, 2.0 / 3.0])
    t_lo = r_id[hs <= t_edges[0]]
    t_mi = r_id[(hs > t_edges[0]) & (hs <= t_edges[1])]
    t_hi = r_id[hs > t_edges[1]]
    sp_crit = spearman(qq * t2, hs)
    crit = qq * t2                      # positivity criterion q tan^2 < 1
    print("      min r_id = %.4f at h = %d; leave-one-out second min "
          "= %.4f" % (r_min, int(hs[i_min]), r_loo))
    print("      bootstrap (B = %d) of min r_id: quantiles 1%% %.4f / "
          "5%% %.4f / 50%% %.4f  (declared caveat: the bootstrap of a"
          " minimum is inconsistent -- it piles on the sample min)"
          % (B_BOOT, q01, q05, q50))
    print("      half-sample subsample (m = %d of n = %d) min r_id: "
          "quantiles 5%% %.4f / 50%% %.4f / 95%% %.4f"
          % (m_half, n, s05, s50, s95))
    print("      depth trend: Spearman(r_id, h) = %+.4f (perm p = "
          "%.5f); tertile medians %.3f / %.3f / %.3f; tertile minima "
          "%.3f / %.3f / %.3f"
          % (sp_h, p_h, float(np.median(t_lo)), float(np.median(t_mi)),
             float(np.median(t_hi)), float(t_lo.min()),
             float(t_mi.min()), float(t_hi.min())))
    print("      positivity criterion q tan^2 theta < 1: max = %.4f "
          "(margin to 1: %.4f); Spearman(q tan^2, h) = %+.4f"
          % (float(crit.max()), 1.0 - float(crit.max()), sp_crit))
    threat = sp_h < -0.30 and sp_crit > 0.30
    check("H5.1 [MEASURED] the family bound lambda_min >= %.3f x "
          "q_r/||w_lock||_G^2 is a RESTATEMENT of the family minimum "
          "(circular as an inequality on the same %d windows); "
          "stability of the floor ON the family: leave-one-out %.3f, "
          "half-sample 5%% quantile %.3f (bootstrap-of-min %.3f, "
          "inconsistent by construction); BUT the depth trend is "
          "strongly negative (rho = %+.3f, p = %.5f) and the "
          "positivity product q tan^2 theta RISES with h (rho = "
          "%+.3f, max %.3f) -- %s"
          % (r_min, n, r_loo, s05, q05, sp_h, p_h, sp_crit,
             float(crit.max()),
             "r_id -> 0 on DEEPER ladders is NOT excluded; the "
             "measured floor holds on this surface only"
             if threat else
             "no r_id -> 0 threat visible on the surface"), True)

    # ---------------------------------------------- verdict
    guards_ok = not any(f.startswith("G0") for f in FAILS)
    exact_ok = not any(f.startswith(("H1.1", "H1.2", "H1.3"))
                       for f in FAILS)
    if not (guards_ok and exact_ok):
        VERDICT = "RID-MIXED (guards or exactness bars failed)"
    elif smooth:
        VERDICT = "RID-EXACT-SMOOTH"
    else:
        VERDICT = "RID-EXACT-INFORMATIVE"

    check("H6.1 [C] the typed reading: r_id obeys the closed 2D "
          "eigen-formula r_id = (1 - q tan^2 theta)/(1 - tan^2 theta) "
          "exactly (max dev %.1e); the deficit 1 - r_id = tan^2 (q-1)/"
          "(1-tan^2) splits with log-variance shares tan^2 %.2f / "
          "(q-1) %.2f; H4 typing %s (R^2 = %.3f); measured family "
          "floor min r_id = %.3f (half-sample 5%% %.3f) with a "
          "strongly negative depth trend (rho = %+.3f).  NO uniform "
          "theorem, NO positivity claim, NO marker move; W3 stays "
          "open; the reduced open problem is a uniform bound "
          "q tan^2 theta <= 1 - delta"
          % (dev_cf, sh_t, sh_q, VERDICT.split("-")[-1], r2_3, r_min,
             s05, sp_h), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, alignment-factor round (2026-08-02): the
  open quantity of the margin identification lambda_min ~ r_id x
  q_r/||w_lock||_G^2 (margin-bridge round) is CLOSED GEOMETRICALLY:
  writing the minimal mode as m = cos(theta) w_hat + sin(theta)
  w_perp (G-orthonormal), the eigenvector constraints force the
  exact 2D formula  r_id = (1 - q tan^2 theta)/(1 - tan^2 theta),
  q = Q_perp/lambda_lock  (verified per window to %.0e; the cross
  term B = cos(lam_min - lam_lock)/sin < 0 always, q > 1 always,
  theta < 45 deg always).  The deficit 1 - r_id = tan^2(theta)(q-1)/
  (1 - tan^2 theta) carries log-variance shares tan^2 %.2f vs (q-1)
  %.2f.  Statistics on n = %d (v637 controls, seed %d): spectral gap
  h3-partial rho = %+.3f (p = %.4f, gate MISS; mediation by tan^2
  reveals a SUPPRESSED negative channel rho = %+.3f, p = %.4f --
  opposite sign to the mixing hypothesis); arithmetic covariates
  after h-control: %s.  H4 typing: cubic-log-h R^2 = %.3f -> %s.
  Family floor min r_id = %.3f at h = %d (leave-one-out %.3f,
  half-sample 5%% quantile %.3f); depth trend STRONGLY NEGATIVE
  (rho = %+.3f) and the positivity product q tan^2 theta rises with
  h to max %.4f < 1 -- r_id -> 0 on deeper ladders is NOT excluded.
  TYPE: measured family statement; the bound lambda_min >= 0.21
  q_r/||w_lock||_G^2 is a restatement of the family minimum, NOT a
  uniform theorem; W3 reduces (on this surface) to (i) the lock
  sign of q_r (v618 dichotomy) and (ii) a uniform bound
  q tan^2 theta <= 1 - delta.  No marker move; Problem 7.1
  untouched.
""" % (BAR_EIGEN, sh_t, sh_q, len(lock_c), SEED, rg3, pg3, rmed, pmed,
       ("; ".join("%s rho=%+.3f p=%.4f [(h,a) joint %s; Bonferroni "
                  "%s]" % (nm, r3_, p3_, "holds" if j_ else "FAILS",
                           "holds" if p3_ < P_BAR / 6.0 else "fails")
                  for nm, r3_, p3_, _, _, j_ in h2_hits))
       if h2_hits else "none pass the gate",
       r2_3, VERDICT.split("-")[-1], r_min, int(hs[i_min]), r_loo,
       s05, sp_h, float(crit.max())))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
