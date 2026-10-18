"""v670 -- PRIME.BLOCKDEFL.01: THE BLOCK DEFLATION -- the named
successor of the FAILED rank-1 rotation predicate
(v660_theta_predicate.py, 2026-08-02, THETA-PRED-FAIL): replace the
eigenvector-free 2x2
[[lambda_lock, B], [B, mu1]] by a (1+K)-block Rayleigh-Ritz
compression of the window pencil onto the space

    span{ w_hat_lock(alpha),  v_1(alpha), ..., v_K(alpha) },

with v_1..v_K the K LOWEST eigenvectors of the pencil DEFLATED to the
G-orthocomplement of the closed v591 lock direction (nested secular
construction: the K lowest roots of the Wilkinson secular equation
sum_j c_j^2/(lambda_j - mu) = 0 merged with the deflated inactive
levels |c_j| <= C_TOL).  NOTHING in the construction reads the
minimal mode, so theta_block(alpha) (the angle of the lowest Ritz
mode to the lock direction) is a legitimate PREDICTIVE quantity for
every K -- exactly as the rank-1 K2 was, whose failure mode is the
declared starting point:

  RANK-1 FAIL RECORD (run-2 quotes, the anchors of THIS probe):
    * 2-space leak median = p90 = max = 1.000 (the pencil action on
      w_hat has essentially NO overlap with the 2-space: there is no
      single 2-level partner -- MULTI-MODE coupling);
    * angle fidelity |theta_K2 - theta_full| median 6.641 deg but
      p90 = 50.532 deg on the 635 landscape grid points;
    * predicate f = lambda_lock - mu1 >= 0: recall 1.0000 (f >= 0 is
      a COMPLETE necessary condition) but precision 0.1765;
    * mechanism: 47/52 landscape needles carry a diagonal crossing
      lambda_lock <-> mu1 (CROSS); 33/52 needles are ROT-regime;
    * the probe named its successor: "a carrying path needs BLOCK
      DEFLATION".  THIS probe is that successor.

THE CONSTRUCTION (declared BEFORE running):
  * per (h, alpha): full generalized eigendecomposition (lambda_j,
    V) of the window pencil (A, G) (landscape numerics verbatim);
    c = V^T G w_hat_lock (G-orthonormal coordinates of the lock
    direction, sum c^2 = 1);
  * nested deflation: the K_MAX = 8 lowest constrained eigenpairs
    (mu_i, a_i) of the deflated pencil -- secular roots in the first
    8 active gaps (brentq, the rank-1 probe's bracket machinery
    verbatim) merged with inactive levels; constrained eigenvector
    coordinates a_j = c_j/(lambda_j - mu_i), exact-constraint
    projected (a <- a - (c.a) c, normalized; run-2 hygiene verbatim);
  * per K in K_LIST = (1, 2, 4, 8): orthonormal block basis W by QR
    of [c | a_1 .. a_K] (first column IS c, the a_i are already
    c-orthogonal, so QR only cleans float residue); block matrix
    M = W^T diag(lambda) W; theta_block = angle of the lowest
    eigenvector of M to the first basis vector; block leak =
    || (I - W W^T) diag(lambda) c || / || diag(lambda) c ||  (the
    invariance defect of the (1+K)-space under the pencil action on
    the lock direction -- the K = 1 case is the rank-1 leak);
  * K = 1 is the ANCHOR RUNG: it must reproduce the rank-1 run-2
    fidelity and predicate quotes (bars below).

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * base sweep, sample, slice choice, grid, guards G0.1-G0.8: the
    theta_rotation_predicate probe VERBATIM (67 complete frame-A
    windows, truncated {1219, 1292, 1445}; lock sign; float floor;
    top-4 by P {859, 363, 1430, 1393} + 4 h-quantile picks; 81-point
    alpha-grid +-10%, s = 0 forced, Mz fixed per window, atom-
    complete only; anchors: 52 peaks with per-slice counts
    [9, 9, 6, 9, 8, 5, 1, 5], theta(859) = 43.5 +- 0.2 deg, the rid
    anchor block, 635 feasible grid points);
  * B1 wiring bars [E]: W^T W = I to 1e-10 (QR); interlacing
    lambda_min - tol <= mu_1 <= lambda_2 + tol (tol 1e-9 x radius);
    |c . a_i| < 1e-8 after projection; spectral lambda_lock
    consistency rel < 1e-6; variational sanity lambda_min - tol <=
    lam_block(K) and lam_block monotone non-increasing in K (tol
    1e-9 x radius); first-gap secular anomaly share < 1% (the
    rank-1 bar); any-gap anomaly share REPORTED (no gate, declared:
    deeper gaps are nearer degeneracy);
  * B2 anchor bars [E] (K = 1 vs the rank-1 run-2 quotes): fidelity
    median 6.641 +- 0.5 deg, p90 50.532 +- 2.0 deg; PRED1 f >= 0
    pointwise precision 0.1765 +- 0.005, recall >= 0.999;
  * A1 FIDELITY LADDER [MEASURED, selection rule frozen]: pooled
    |theta_block(K) - theta_full| median / p90 / max on the 635
    grid points, split by regime; K_STAR = smallest K in {2, 4, 8}
    with p90 < FID_BAR = 5.0 deg; if none, K_STAR = 8 and A1 =
    MISS (A2 still evaluated, declared);
  * A2 THE BLOCK PREDICATE [MEASURED, gate]: needle level over the
    52 classified landscape peaks (window = FWHM +- 1 grid step;
    truth label = peak regime ROT, the landscape typing verbatim);
    FIRE(peak) <=> max over the window of theta_block(K_STAR) >= 45
    deg; gate: precision AND recall >= PR_BAR = 0.8 over the 52;
    reported alongside (no gate): pointwise theta_block >= 45 vs
    ROT truth, and the pooled event match (45-deg crossings of
    theta_block vs theta_full, greedy 1-1, tol one grid step);
  * A3 CONDITIONAL (frozen): IF the A2 gate hits -> frame-A safety
    table rebuilt with the BLOCK predicate: scan g(s) =
    theta_block(K_STAR, s) - 45 on s in +-2.5% step 0.25%, nearest
    sign change per side bisection-refined to 1e-5, <= 2 interior
    g-maxima refined by one parabolic vertex each (needle CONFIRMED
    iff refined g >= 0); distance in units W_NEEDLE = 2.5e-4;
    censored at 2.5%; FRAME-A-SAFE iff min distance over analysis
    windows >= 10 W; the MEASURED theta_full = 45 distance printed
    per window from the same scans (diagnostic).  IF the gate
    misses -> NO scan; instead the honest failure record: the leak
    distribution over K (median / p90 / max, by regime) documents
    where multi-mode coupling breaks the block too;
  * A4 typing only: contract-note text printed; no marker move.

Verdict enums (frozen, precedence top-down):
  BLOCK-MIXED            guards or B1/B2 bars fail;
  BLOCK-DEFL-PASS        A1 hit (some K in {2,4,8}) AND A2 gate hit;
  BLOCK-DEFL-PRED-ONLY   A2 gate hits but A1 misses;
  BLOCK-DEFL-FID-ONLY    A1 hits but the A2 gate misses;
  BLOCK-DEFL-FAIL        neither A1 nor A2 reaches its bar.

FIREWALL: v563 import read-only; v618/v591/rid/landscape/theta
machinery REBUILT verbatim (no other imports); no marker moves; no
positivity claim; no RH statement; NO zero of any L-function is read
(AST-checked).  Python-only, per GATE.WOLFRAM.02.

PROVENANCE: discovery probe w3_block_deflation_probe.py (2026-08-02,
18/18, verdict BLOCK-DEFL-FAIL -- the honest preregistered result);
theta_rotation_predicate_probe (2026-08-02, THETA-PRED-FAIL + the K2
secular machinery + the run-2 quotes), w3_resonance_landscape_probe
(52 peaks + regime typing), rid_alignment_probe (lock geometry),
v618 (C = 1 reads), v591 (closed lock direction).
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
# reproduction anchors (landscape/rid/theta quotes, verbatim)
P_MAX_QUOTE, P_MAX_TOL = 0.9636, 0.005
H_AT_PMAX = 859
SP_P_H_QUOTE, SP_TOL = 0.735, 0.03
SP_RID_H_QUOTE = -0.784
RID_MED_QUOTE, RID_TOL = 0.584, 0.005
THETA_MED_QUOTE = 9.1
PEAKS_QUOTE = 52
PEAKS_SLICE_QUOTE = [9, 9, 6, 9, 8, 5, 1, 5]
THETA_859_QUOTE, THETA_859_TOL = 43.5, 0.2
N_POINTS_QUOTE = 635
BAR_EIGEN = 1e-6
BAR_REBUILD = 1e-12
# rank-1 run-2 quotes (the K = 1 anchor rung)
K1_FID_MED_QUOTE, K1_FID_MED_TOL = 6.641, 0.5
K1_FID_P90_QUOTE, K1_FID_P90_TOL = 50.532, 2.0
K1_PREC_QUOTE, K1_PREC_TOL = 0.1765, 0.005
K1_REC_BAR = 0.999
K1_LEAK_MED_QUOTE = 1.000    # reported reference
# this probe's frozen additions
C_TOL = 1e-10                # secular active-level threshold on |c_j|
K_MAX = 8                    # deepest block rung
K_LIST = (1, 2, 4, 8)        # K = 1 is the anchor rung
FID_BAR = 5.0                # A1 fidelity bar on p90 (deg)
PR_BAR = 0.80                # A2 precision/recall bar
EV_TOL = 0.0025              # event match tolerance (one grid step)
ANOM_BAR = 0.01              # first-gap secular anomaly share bar
QR_TOL = 1e-10               # W^T W = I bar
W_NEEDLE = 2.5e-4            # needle-width unit (landscape zoom read)
S_SCAN = 0.025               # A3 scan half-width
SCAN_STEP = 0.0025           # A3 scan step
BIS_TOL = 1.0e-5             # A3 bisection tolerance in s
MAX_PARAB = 2                # A3 refined maxima per window
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


# --------------------------------------- nested secular block deflation
def deflated_pairs(lams, cs, rad, kmax):
    """The kmax lowest constrained eigenpairs of the pencil deflated
    to the G-orthocomplement of w_hat (coordinates cs in the
    G-orthonormal eigenbasis, sum cs^2 = 1).  Secular roots in the
    first kmax active gaps (rank-1 bracket machinery verbatim)
    merged with inactive levels (|c_j| <= C_TOL).  Returns
    (mus, cols, anom_first, anom_any): mus ascending, cols the
    exact-constraint-projected unit coordinate vectors."""
    n = len(lams)
    act = np.abs(cs) > C_TOL
    idx_act = np.nonzero(act)[0]
    la = lams[act]
    ca2 = cs[act] ** 2
    n_act = int(act.sum())
    anom_first = False
    anom_any = False
    cand = []
    n_gap = min(kmax, max(0, n_act - 1))
    for i in range(n_gap):
        lo, hi = float(la[i]), float(la[i + 1])
        span = hi - lo
        if span <= 0.0:
            cand.append((lo, "root", i))
            anom_any = True
            if i == 0:
                anom_first = True
            continue

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
            anom_any = True
            if i == 0:
                anom_first = True
        cand.append((root, "root", i))
    mu_cap = cand[-1][0] if len(cand) == kmax else np.inf
    for j in np.nonzero(~act)[0]:
        if float(lams[j]) <= mu_cap or len(cand) < kmax:
            cand.append((float(lams[j]), "level", int(j)))
    cand.sort(key=lambda t: t[0])
    cand = cand[:kmax]
    mus, cols = [], []
    for rank, (mu, kind, j) in enumerate(cand):
        a = np.zeros(n)
        if kind == "root":
            den = lams[act] - mu
            if float(np.min(np.abs(den))) < 1e-13 * max(rad, 1.0):
                j_near = int(np.argmin(np.abs(den)))
                a[idx_act[j_near]] = 1.0
                anom_any = True
                if rank == 0:
                    anom_first = True
            else:
                a[act] = cs[act] / den
        else:
            a[j] = 1.0
        a = a - float(cs @ a) * cs
        nrm = float(np.linalg.norm(a))
        if nrm <= 0.0:
            anom_any = True
            if rank == 0:
                anom_first = True
            continue
        cols.append(a / nrm)
        mus.append(mu)
    return mus, cols, anom_first, anom_any


def block_reads(lams, cs, rad):
    """theta_block, leak and the lowest block eigenvalue per K in
    K_LIST from ONE nested deflation (K_MAX pairs)."""
    mus, cols, anom_first, anom_any = deflated_pairs(lams, cs, rad,
                                                     K_MAX)
    y = lams * cs
    ny = float(np.linalg.norm(y))
    out = {}
    qr_dev = 0.0
    orth_dev = 0.0
    for K in K_LIST:
        kk = min(K, len(cols))
        X = np.column_stack([cs] + cols[:kk])
        W, _ = np.linalg.qr(X)
        qr_dev = max(qr_dev, float(np.max(np.abs(
            W.T @ W - np.eye(1 + kk)))))
        orth_dev = max(orth_dev, float(np.max(np.abs(
            cs @ np.column_stack(cols[:kk])))) if kk else 0.0)
        M = W.T @ (lams[:, None] * W)
        M = 0.5 * (M + M.T)
        w2, V2 = np.linalg.eigh(M)
        x0 = abs(float(V2[0, 0]))
        th = math.degrees(math.acos(min(1.0, x0)))
        proj = W @ (W.T @ y)
        leak = float(np.linalg.norm(y - proj) / ny)
        out[K] = dict(th=th, leak=leak, lam_b=float(w2[0]), kk=kk,
                      M00=float(M[0, 0]))
    return out, mus, anom_first, anom_any, qr_dev, orth_dev


# ------------------------------------------------------ window builder
def window_eval(alpha, Mz):
    """One window at EXPLICIT (alpha, Mz): the landscape/theta
    window_eval numerics verbatim (same assembly, same eigh),
    extended by the nested block-deflation reads."""
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
    # rid geometry: theta_full from the minimal mode (truth only)
    wl = vl[0] * t1v + vl[1] * t2v
    wlGwl = float(wl @ (Gm @ wl))
    wlAwl = float(wl @ (A @ wl))
    w_hat = wl / math.sqrt(wlGwl)
    vGv = float(v_min @ (Gm @ v_min))
    m_vec = v_min / math.sqrt(vGv)
    ct = float(w_hat @ (Gm @ m_vec))
    if ct < 0.0:
        ct = -ct
    ct = min(1.0, ct)
    st = math.sqrt(max(0.0, 1.0 - ct * ct))
    lam_lock = wlAwl / wlGwl
    t2 = (st / ct) ** 2 if ct > 0.0 else float("inf")
    # perp Rayleigh for P (landscape verbatim)
    perp = m_vec - float(w_hat @ (Gm @ m_vec)) * w_hat
    pn = math.sqrt(max(0.0, float(perp @ (Gm @ perp))))
    w_perp = perp / pn if pn > 0.0 else perp
    Q_perp = float(w_perp @ (A @ w_perp))
    qq = Q_perp / lam_lock
    # nested block deflation (eigenvector-free)
    c_vec = V_all.T @ (Gm @ w_hat)
    lam_lock_spec = float(np.sum(c_vec ** 2 * w_all))
    blocks, mus, an_f, an_a, qr_dev, orth_dev = block_reads(
        w_all, c_vec, rad)
    mu1 = mus[0] if mus else float("nan")
    f_gap = lam_lock - mu1
    rec = dict(h=hz, alpha=alpha, D=D, complete=complete,
               lam=lam_min, lam2=lam_2, floor=floor, rad=rad,
               qr=q_r, qm=q_m, lock=q_r * q_m > 0.0,
               ct=ct, st=st, t2=t2, qq=qq, P=qq * t2,
               lam_lock=lam_lock, theta=math.degrees(math.acos(ct)),
               lam_lock_spec=lam_lock_spec,
               mu1=mu1, f=f_gap, blocks=blocks,
               anom_first=an_f, anom_any=an_a,
               qr_dev=qr_dev, orth_dev=orth_dev)
    return rec


# ------------------------------------------------------ peak analysis
def detect_peaks(ss, Pv_):
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
    if rv["lam"] < -rv["floor"]:
        return "NEG"
    if rv["theta"] >= THETA_BAR:
        return "ROT"
    if rv["lam_lock"] <= 0.0:
        return "LCK"
    return "MARGIN"


def cross_events(ss, vals, level):
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
    print("THE BLOCK DEFLATION -- the (1+K) Rayleigh-Ritz successor "
          "of the rank-1 predicate")
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
    check("G0.3b [E] the angle anchor: theta(h = 859, s = 0) = %.3f "
          "deg (quote %.1f, tol %.1f); block angles there: %s"
          % (th859, THETA_859_QUOTE, THETA_859_TOL,
             {K: "%.2f" % r859[0]["blocks"][K]["th"]
              for K in K_LIST} if r859 else "n/a"),
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
          "verbatim; block entries per point)")
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
        pr = dict(i_w=i_w, tag=tag, r0=r0, ss=ss, recs=recs,
                  Pp=np.array([rv["P"] for rv in recs]),
                  i0=int(np.where(ss == 0.0)[0][0]),
                  n_infeas=n_infeas,
                  f=np.array([rv["f"] for rv in recs]),
                  th=np.array([rv["theta"] for rv in recs]))
        for K in K_LIST:
            pr["thb%d" % K] = np.array(
                [rv["blocks"][K]["th"] for rv in recs])
            pr["lkb%d" % K] = np.array(
                [rv["blocks"][K]["leak"] for rv in recs])
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
    per_slice = [len(pr["peaks"]) for pr in profiles]
    check("G0.8 [E] the landscape peak set reproduces: %d peaks "
          "total (quote %d); per-slice counts %s (quote %s)"
          % (n_peaks_tot, PEAKS_QUOTE, per_slice, PEAKS_SLICE_QUOTE),
          n_peaks_tot == PEAKS_QUOTE and per_slice == PEAKS_SLICE_QUOTE)

    # ------------------------------------------------ B1: wiring
    print("\nB1 -- block wiring on the pooled points")
    pool = list(lock_c)
    for pr in profiles:
        pool.extend(pr["recs"])
    dev_int, dev_lls, dev_qr, dev_orth = 0.0, 0.0, 0.0, 0.0
    dev_var, dev_mono = 0.0, 0.0
    n_anf, n_ana = 0, 0
    for rv in pool:
        dev_int = max(dev_int,
                      (rv["lam"] - rv["mu1"]) / rv["rad"],
                      (rv["mu1"] - rv["lam2"]) / rv["rad"])
        dev_lls = max(dev_lls, abs(rv["lam_lock_spec"]
                                   - rv["lam_lock"])
                      / abs(rv["lam_lock"]))
        dev_qr = max(dev_qr, rv["qr_dev"])
        dev_orth = max(dev_orth, rv["orth_dev"])
        lb_prev = None
        for K in K_LIST:
            lb = rv["blocks"][K]["lam_b"]
            dev_var = max(dev_var, (rv["lam"] - lb) / rv["rad"])
            if lb_prev is not None:
                dev_mono = max(dev_mono, (lb - lb_prev) / rv["rad"])
            lb_prev = lb
        n_anf += 1 if rv["anom_first"] else 0
        n_ana += 1 if rv["anom_any"] else 0
    check("B1.1 [E] block wiring on %d pooled points: interlacing "
          "lambda_min <= mu1 <= lambda_2 (max violation %.1e of the "
          "radius < 1e-9), QR orthonormality max |W^T W - I| = %.1e "
          "< %.0e, post-projection |c.a_i| max %.1e < 1e-8, spectral "
          "lambda_lock consistency max rel %.1e < %.0e, variational "
          "sanity lam_block >= lambda_min (max violation %.1e < "
          "1e-9) and monotone in K (max increase %.1e < 1e-9); "
          "first-gap anomalies %d/%d (share %.4f < %.2f), any-gap "
          "anomalies %d/%d (share %.4f, REPORTED)"
          % (len(pool), dev_int, dev_qr, QR_TOL, dev_orth, dev_lls,
             BAR_EIGEN, dev_var, dev_mono,
             n_anf, len(pool), n_anf / float(len(pool)), ANOM_BAR,
             n_ana, len(pool), n_ana / float(len(pool))),
          dev_int < 1e-9 and dev_qr < QR_TOL and dev_orth < 1e-8
          and dev_lls < BAR_EIGEN and dev_var < 1e-9
          and dev_mono < 1e-9
          and n_anf / float(len(pool)) < ANOM_BAR)

    # ------------------------------------------------ A1: the ladder
    print("\nA1 -- the fidelity ladder |theta_block(K) - theta_full| "
          "on the profile grid")
    th_flat = np.concatenate([pr["th"] for pr in profiles])
    regs_flat = np.concatenate([np.array(pr["regs"])
                                for pr in profiles])
    n_pts = len(th_flat)
    check("A1.0 [E] the grid-point count reproduces: %d feasible "
          "profile points (quote %d)" % (n_pts, N_POINTS_QUOTE),
          n_pts == N_POINTS_QUOTE)

    fid = {}
    print("      K    median     p90       max     | MARGIN med  "
          "ROT med   | leak med  leak p90  leak max")
    for K in K_LIST:
        thb = np.concatenate([pr["thb%d" % K] for pr in profiles])
        lkb = np.concatenate([pr["lkb%d" % K] for pr in profiles])
        d = np.abs(thb - th_flat)
        d_m = d[regs_flat == "MARGIN"]
        d_r = d[regs_flat == "ROT"]
        fid[K] = dict(med=float(np.median(d)),
                      p90=float(np.quantile(d, 0.9)),
                      mx=float(d.max()),
                      med_m=float(np.median(d_m)) if len(d_m)
                      else float("nan"),
                      med_r=float(np.median(d_r)) if len(d_r)
                      else float("nan"),
                      lk_med=float(np.median(lkb)),
                      lk_p90=float(np.quantile(lkb, 0.9)),
                      lk_max=float(lkb.max()))
        print("      %d   %7.3f   %7.3f   %7.2f  |   %7.3f   "
              "%7.3f   |  %.4f    %.4f    %.4f"
              % (K, fid[K]["med"], fid[K]["p90"], fid[K]["mx"],
                 fid[K]["med_m"], fid[K]["med_r"], fid[K]["lk_med"],
                 fid[K]["lk_p90"], fid[K]["lk_max"]))

    check("B2.1 [E] the K = 1 anchor rung reproduces the rank-1 "
          "run-2 quotes: fidelity median %.3f (quote %.3f +- %.1f), "
          "p90 %.3f (quote %.3f +- %.1f); leak median %.3f (quote "
          "%.3f, reported)"
          % (fid[1]["med"], K1_FID_MED_QUOTE, K1_FID_MED_TOL,
             fid[1]["p90"], K1_FID_P90_QUOTE, K1_FID_P90_TOL,
             fid[1]["lk_med"], K1_LEAK_MED_QUOTE),
          abs(fid[1]["med"] - K1_FID_MED_QUOTE) <= K1_FID_MED_TOL
          and abs(fid[1]["p90"] - K1_FID_P90_QUOTE) <= K1_FID_P90_TOL)

    f_flat = np.concatenate([pr["f"] for pr in profiles])
    rot_flat = regs_flat == "ROT"
    pred1 = f_flat >= 0.0
    tp = int(np.sum(pred1 & rot_flat))
    prec1 = tp / float(np.sum(pred1)) if np.sum(pred1) else float("nan")
    rec1 = tp / float(np.sum(rot_flat)) if np.sum(rot_flat) \
        else float("nan")
    check("B2.2 [E] the K = 1 predicate anchor reproduces: f >= 0 "
          "pointwise precision %.4f (quote %.4f +- %.3f), recall "
          "%.4f (>= %.3f)"
          % (prec1, K1_PREC_QUOTE, K1_PREC_TOL, rec1, K1_REC_BAR),
          abs(prec1 - K1_PREC_QUOTE) <= K1_PREC_TOL
          and rec1 >= K1_REC_BAR)

    k_star = None
    for K in (2, 4, 8):
        if fid[K]["p90"] < FID_BAR:
            k_star = K
            break
    a1_hit = k_star is not None
    if k_star is None:
        k_star = 8
    check("A1.1 [MEASURED, selection rule frozen] fidelity ladder: "
          "p90 = %s deg for K = %s (rank-1 p90 was %.1f); smallest "
          "K in {2, 4, 8} with p90 < %.1f deg: %s -> K_STAR = %d "
          "(A1 %s)"
          % (["%.3f" % fid[K]["p90"] for K in K_LIST], list(K_LIST),
             K1_FID_P90_QUOTE, FID_BAR,
             ("K = %d" % k_star) if a1_hit else "NONE",
             k_star, "HIT" if a1_hit else "MISS"), True)

    # ------------------------------------------------ A2: predicate
    print("\nA2 -- the block predicate at K = %d" % k_star)
    thb_flat = np.concatenate([pr["thb%d" % k_star]
                               for pr in profiles])
    predb = thb_flat >= THETA_BAR
    tp_b = int(np.sum(predb & rot_flat))
    prec_pt = tp_b / float(np.sum(predb)) if np.sum(predb) \
        else float("nan")
    rec_pt = tp_b / float(np.sum(rot_flat)) if np.sum(rot_flat) \
        else float("nan")
    print("      pointwise theta_block >= 45: flags %d of %d points "
          "| truth ROT %d | precision %.4f recall %.4f (reported)"
          % (int(np.sum(predb)), n_pts, int(np.sum(rot_flat)),
             prec_pt, rec_pt))

    ev_truth_n, ev_pred_n, ev_match = 0, 0, 0
    for pr in profiles:
        ev_t = cross_events(pr["ss"], pr["th"], THETA_BAR)
        ev_p = cross_events(pr["ss"], pr["thb%d" % k_star],
                            THETA_BAR)
        ev_truth_n += len(ev_t)
        ev_pred_n += len(ev_p)
        ev_match += greedy_match(ev_t, ev_p, EV_TOL)
    prec_ev = ev_match / float(ev_pred_n) if ev_pred_n \
        else float("nan")
    rec_ev = ev_match / float(ev_truth_n) if ev_truth_n \
        else float("nan")
    print("      event level: %d theta_full-45-crossings vs %d "
          "theta_block-45-crossings, matched %d within one grid "
          "step -> precision %.4f recall %.4f (reported)"
          % (ev_truth_n, ev_pred_n, ev_match, prec_ev, rec_ev))

    # needle level over the 52 classified peaks (the A2 gate)
    step = 2.0 * S_MAX / (N_GRID - 1)
    n_rot_pk, n_fire, n_hit = 0, 0, 0
    conf = {("ROT", True): 0, ("ROT", False): 0,
            ("MARGIN", True): 0, ("MARGIN", False): 0}
    print("\n      needle table (window = FWHM +- 1 step; FIRE <=> "
          "max theta_block >= 45 in window):")
    print("      h      s*        P*        regime  theta   "
          "th_blk  maxWin_blk  FIRE")
    for pr, iv in all_peaks:
        ss = pr["ss"]
        lo, hi = iv["s_l"] - step, iv["s_r"] + step
        idx = np.where((ss >= lo - 1e-15) & (ss <= hi + 1e-15))[0]
        mx_b = float(np.max(pr["thb%d" % k_star][idx]))
        fire = mx_b >= THETA_BAR
        rg = pr["regs"][iv["ip"]]
        lbl = "ROT" if rg == "ROT" else "MARGIN"
        conf[(lbl, fire)] = conf.get((lbl, fire), 0) + 1
        if rg == "ROT":
            n_rot_pk += 1
            if fire:
                n_hit += 1
        if fire:
            n_fire += 1
        ip = iv["ip"]
        print("      %4d  %+7.4f  %9.3g  %-6s  %5.2f  %6.2f   "
              "%6.2f     %s"
              % (pr["r0"]["h"], iv["s"], iv["P"], rg,
                 pr["th"][ip], pr["thb%d" % k_star][ip], mx_b,
                 "YES" if fire else "no"))
    prec_nd = n_hit / float(n_fire) if n_fire else float("nan")
    rec_nd = n_hit / float(n_rot_pk) if n_rot_pk else float("nan")
    a2_hit = n_fire > 0 and n_rot_pk > 0 \
        and prec_nd >= PR_BAR and rec_nd >= PR_BAR
    check("A2.1 [MEASURED, gate] the block predicate at K = %d over "
          "the %d classified needles (truth = ROT regime, %d of "
          "them): FIRE on %d, hits %d -> precision %.4f, recall "
          "%.4f (bar both >= %.2f) -> %s; confusion (regime, FIRE): "
          "%s; pointwise precision %.4f / recall %.4f, event "
          "precision %.4f / recall %.4f (reported)"
          % (k_star, n_peaks_tot, n_rot_pk, n_fire, n_hit, prec_nd,
             rec_nd, PR_BAR, "HIT" if a2_hit else "MISS",
             {("%s|%s" % (k[0], "F" if k[1] else "-")): v
              for k, v in sorted(conf.items())},
             prec_pt, rec_pt, prec_ev, rec_ev), True)

    # ------------------------------------------------ A3: conditional
    t4_rows = []
    d_min, h_min, safe = float("inf"), [], False
    d859 = float("nan")
    tr859 = None
    if a2_hit:
        print("\nA3 -- frame-A safety with the BLOCK predicate "
              "(unit W = %.1e)" % W_NEEDLE)
        offs = [k * SCAN_STEP for k in range(-10, 11) if k != 0]

        def eval_at(r0_, s):
            a_p = r0_["alpha"] * (1.0 + s)
            if math.exp(2.0 * a_p) > core.ATOM_MAX + 0.5:
                return None
            return window_eval(a_p, r0_["Mz"])

        for w_i, r0_ in enumerate(sorted(comp, key=lambda r: r["h"])):
            pts = {0.0: r0_}
            for s in offs:
                rv = eval_at(r0_, s)
                if rv is not None:
                    pts[s] = rv
            ssc = np.array(sorted(pts.keys()))
            gsc = np.array([pts[s]["blocks"][k_star]["th"]
                            - THETA_BAR for s in ssc])
            needles = []
            brks = [(float(ssc[i]), float(ssc[i + 1]),
                     float(gsc[i]), float(gsc[i + 1]))
                    for i in range(len(ssc) - 1)
                    if gsc[i] * gsc[i + 1] < 0.0]
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
                    fm = rv["blocks"][k_star]["th"] - THETA_BAR
                    if fa * fm <= 0.0:
                        sb, fb = sm, fm
                    else:
                        sa, fa = sm, fm
                needles.append(0.5 * (sa + sb))
            maxima = [i for i in range(1, len(ssc) - 1)
                      if gsc[i] >= gsc[i - 1] and gsc[i] >= gsc[i + 1]
                      and gsc[i] < 0.0]
            maxima.sort(key=lambda i: abs(ssc[i]))
            for i in maxima[:MAX_PARAB]:
                x0, x1, x2 = ssc[i - 1], ssc[i], ssc[i + 1]
                y0, y1, y2 = gsc[i - 1], gsc[i], gsc[i + 1]
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
                if rv["blocks"][k_star]["th"] - THETA_BAR >= 0.0:
                    needles.append(xv)
            thsc = np.array([pts[s]["theta"] for s in ssc])
            ev45 = cross_events(ssc, thsc, THETA_BAR)
            d_th = min((abs(z) for z in ev45), default=float("nan"))
            d_near = min((abs(z) for z in needles),
                         default=float("nan"))
            analysis = r0_["lock"] and r0_["lam"] > r0_["floor"]
            t4_rows.append(dict(h=r0_["h"], theta=r0_["theta"],
                                thb=r0_["blocks"][k_star]["th"],
                                d=d_near, d_th=d_th,
                                analysis=analysis))
            if (w_i + 1) % 10 == 0:
                print("      ... %d/%d windows scanned (%.0f s, %d "
                      "evals)" % (w_i + 1, len(comp),
                                  time.time() - T0, N_EVAL))

        print("\n      h     theta   th_blk   d_near      d/W       "
              "d_theta45   d45/W")
        for tr in t4_rows:
            d_s = ("%.6f" % tr["d"]) if not math.isnan(tr["d"]) \
                else (">=%.4f" % S_SCAN)
            dw_s = ("%8.1f" % (tr["d"] / W_NEEDLE)) \
                if not math.isnan(tr["d"]) \
                else (">=%6.0f" % (S_SCAN / W_NEEDLE))
            dt_s = ("%.6f" % tr["d_th"]) \
                if not math.isnan(tr["d_th"]) \
                else (">=%.4f" % S_SCAN)
            dtw_s = ("%8.1f" % (tr["d_th"] / W_NEEDLE)) \
                if not math.isnan(tr["d_th"]) \
                else (">=%6.0f" % (S_SCAN / W_NEEDLE))
            print("      %4d%s %6.2f  %6.2f   %s  %s  %s  %s"
                  % (tr["h"], " " if tr["analysis"] else "*",
                     tr["theta"], tr["thb"], d_s, dw_s, dt_s, dtw_s))
        ana = [tr for tr in t4_rows if tr["analysis"]]
        d_ana = [tr["d"] for tr in ana if not math.isnan(tr["d"])]
        n_cens = sum(1 for tr in ana if math.isnan(tr["d"]))
        d_min = min(d_ana) if d_ana else float("inf")
        h_min = [tr["h"] for tr in ana if tr["d"] == d_min] \
            if d_ana else []
        safe = d_min >= SAFE_BAR * W_NEEDLE
        tr859 = [tr for tr in t4_rows if tr["h"] == 859][0]
        d859 = tr859["d"]
        check("A3.1 [MEASURED] frame-A block-needle distances on the "
              "%d analysis windows: %d have a confirmed block needle "
              "within +-%.1f%%, %d censored; MIN distance %.6f at "
              "h = %s = %.1f needle widths (bar %.0f W) -> %s; "
              "h = 859: theta = %.2f, theta_block = %.2f, nearest "
              "block needle %s"
              % (len(ana), len(d_ana), 100 * S_SCAN, n_cens, d_min,
                 h_min, d_min / W_NEEDLE, SAFE_BAR,
                 "FRAME-A-SAFE" if safe else "FRAME-A-TIGHT",
                 tr859["theta"], tr859["thb"],
                 ("%.6f" % d859) if not math.isnan(d859)
                 else ">= %.4f" % S_SCAN), True)
    else:
        print("\nA3 -- SKIPPED (frozen rule: the A2 gate missed); "
              "the honest failure record is the leak ladder:")
        print("      leak by K and regime (median / p90 / max):")
        for K in K_LIST:
            lkb = np.concatenate([pr["lkb%d" % K] for pr in profiles])
            lk_m = lkb[regs_flat == "MARGIN"]
            lk_r = lkb[regs_flat == "ROT"]
            print("      K = %d: pooled %.4f / %.4f / %.4f | MARGIN "
                  "med %.4f | ROT med %.4f"
                  % (K, float(np.median(lkb)),
                     float(np.quantile(lkb, 0.9)), float(lkb.max()),
                     float(np.median(lk_m)) if len(lk_m)
                     else float("nan"),
                     float(np.median(lk_r)) if len(lk_r)
                     else float("nan")))
        check("A3.2 [MEASURED] failure documentation: the leak "
              "ladder above localizes where multi-mode coupling "
              "breaks the (1+K)-block too; K = %d leak median %.4f "
              "(K = 1 was %.3f)"
              % (K_MAX, fid[K_MAX]["lk_med"], fid[1]["lk_med"]),
              True)

    # ------------------------------------------------ verdict
    guards_ok = not any(f_.startswith(("G0", "B1", "B2", "A1.0"))
                        for f_ in FAILS)
    if not guards_ok:
        VERDICT = "BLOCK-MIXED (guards or anchor bars failed)"
    elif a1_hit and a2_hit:
        VERDICT = "BLOCK-DEFL-PASS"
    elif a2_hit:
        VERDICT = "BLOCK-DEFL-PRED-ONLY"
    elif a1_hit:
        VERDICT = "BLOCK-DEFL-FID-ONLY"
    else:
        VERDICT = "BLOCK-DEFL-FAIL"

    check("A4.1 [C] the typed reading: the (1+K)-block deflation "
          "{w_hat_lock, K lowest deflated eigenvectors} replaces "
          "the failed rank-1 2x2; fidelity ladder p90 = %s deg "
          "(K = %s; rank-1 %.1f); K_STAR = %d; block predicate "
          "(needle level, %d needles, %d ROT): precision %.3f / "
          "recall %.3f -> %s; leak ladder median %s; %s.  NO "
          "positivity claim, NO RH statement, NO marker move; W3 "
          "stays open"
          % (["%.2f" % fid[K]["p90"] for K in K_LIST], list(K_LIST),
             K1_FID_P90_QUOTE, k_star, n_peaks_tot, n_rot_pk,
             prec_nd, rec_nd, "HIT" if a2_hit else "MISS",
             ["%.3f" % fid[K]["lk_med"] for K in K_LIST],
             ("frame-A safety rebuilt: min block-needle distance "
              "%.1f W -> %s" % (d_min / W_NEEDLE,
                                "FRAME-A-SAFE" if safe
                                else "FRAME-A-TIGHT")) if a2_hit
             else "A3 skipped by the frozen rule"), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, block-deflation round (2026-08-02): the
  rank-1 rotation predicate (THETA-PRED-FAIL: leak 1.000, fidelity
  p90 50.5 deg, precision 0.18 at recall 1.00) was replaced by its
  named successor, the (1+K)-block Rayleigh-Ritz compression onto
  {w_hat_lock, the K lowest eigenvectors of the pencil deflated to
  the G-orthocomplement of the v591 lock direction} (nested secular
  construction, K = 1/2/4/8; the K = 1 rung reproduces the rank-1
  quotes as anchors).  The construction reads NO minimal mode --
  theta_block(alpha) is predictive.  FIDELITY LADDER (635 landscape
  grid points): |theta_block - theta_full| p90 = %s deg for
  K = %s; block leak median %s -> K_STAR = %d (%s the declared
  5-deg bar).  BLOCK PREDICATE (needle level, the 52 classified
  landscape peaks, truth = ROT regime, %d of 52): max-in-window
  theta_block >= 45 fires on %d, precision %.3f / recall %.3f
  (bar 0.8 both) -> %s; pointwise precision %.3f / recall %.3f;
  event-level (45-crossing match) precision %.3f / recall %.3f.
  %s  CONSEQUENCE FOR W3 (typed, open): %s  TYPE: measured
  landscape reduction on the declared surface; no positivity claim;
  no RH statement; Problem 7.1 untouched; no marker move.
""" % (["%.2f" % fid[K]["p90"] for K in K_LIST], list(K_LIST),
       ["%.3f" % fid[K]["lk_med"] for K in K_LIST], k_star,
       "reaches" if a1_hit else "does NOT reach",
       n_rot_pk, n_fire, prec_nd, rec_nd,
       "HIT" if a2_hit else "MISS", prec_pt, rec_pt,
       prec_ev, rec_ev,
       ("FRAME-A SAFETY (block predicate, all 67 windows): min "
        "distance to a block-predicted needle %.6f = %.1f needle "
        "widths (W = 2.5e-4) at h = %s; h = 859 at %s -> %s."
        % (d_min, d_min / W_NEEDLE, h_min,
           ("%.1f W" % (d859 / W_NEEDLE)) if not math.isnan(d859)
           else ">= %.0f W" % (S_SCAN / W_NEEDLE),
           "FRAME-A-SAFE" if safe else "FRAME-A-TIGHT"))
       if a2_hit else
       ("FRAME-A SAFETY: not rebuilt (frozen rule -- the predicate "
        "did not carry); the failure is localized by the leak "
        "ladder: even at K = 8 the leak median is %.3f -- the "
        "pencil action on the lock direction is NOT captured by "
        "the %d lowest deflated modes; the multi-mode coupling is "
        "spread across the spectrum."
        % (fid[K_MAX]["lk_med"], K_MAX)),
       ("the 'generic block bound + needle exclusion' contract "
        "text is FORMULATABLE: needles are the 45-deg passages of "
        "the explicit (1+%d)-block angle theta_block(alpha), an "
        "eigenvector-free, per-window computable object."
        % k_star) if (a1_hit and a2_hit) else
       ("the block predicate carries at the needle level but the "
        "angle fidelity stays above the 5-deg bar -- usable as an "
        "EVENT predicate only." if a2_hit else
        "the block deflation does NOT rescue the rank-1 failure "
        "at the declared bars; the needle mechanism remains only "
        "partially characterized.")))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s (%d window evals)"
          % (time.time() - T0, N_EVAL))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
