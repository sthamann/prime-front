"""Discovery probe: THE NEEDLE MECHANISM ON THE ASSEMBLY SIDE -- after
the TRIPLE NEGATIVE, the last open W3 mechanism question.

THE TRIPLE NEGATIVE (declared starting point, all 2026-08-02):
  * NOT low-rank:        w3_block_deflation_probe, BLOCK-DEFL-FAIL --
                         the pencil action on the lock direction leaks
                         1.000 (median = p90 = max) past EVERY (1+K)
                         block, K = 1/2/4/8: the coupling of
                         A w_hat_lock to the bulk is spread across the
                         spectrum;
  * NOT zero-driven:     lehmer_resonance_probe, LEHMER-NULL -- no
                         h-controlled correlation between the needle
                         driver P = q tan^2 theta and Lehmer presence
                         in the resolved zero band;
  * NOT in the BD frame: baez_duarte_probe, BD-CONTROL-CLEAN (B3) --
                         the external Nyman-Beurling/Baez-Duarte
                         Galerkin has NO needle analogue (smooth
                         mu-hierarchy, no isolated outliers): the
                         needles are a WINDOW-FAMILY phenomenon.

THE QUESTION: WHAT in the window ASSEMBLY creates the 52 landscape
needles (w3_resonance_landscape_probe: peaks of P >= 0.8, coarse FWHM
median 0.0025, zoomed fine median 2.5e-4)?  Four frozen candidates:

  (a) TENT DISCRETIZATION (lag quantization): the atom-to-cell
      assignment i0(u_j) = floor(u_j / D) jumps whenever u_j / D
      crosses an integer; at fixed h the profile has D(s) =
      2 alpha_0 (1 + s) / Mz, so the JUMP SET is closed-form
      computable: s = u_j Mz / (2 alpha_0 n) - 1, n in Z, plus the
      atom-entry events 2 alpha_0 (1 + s) = u_n.  DECLARED CAVEAT
      (measured, not assumed): the all-atom jump set may be DENSE
      (thousands of events per profile) -- the density itself is then
      the honest kill; the sharp sub-read uses the K_HEAVY = 12
      globally heaviest atoms (landscape score_b convention).
  (b) ATOM PLACEMENT relative to the lattice -- NOT the zeros, the
      atoms: the collective phase coherence
        K(alpha)  = |sum_j mu_j e^{2 pi i u_j / D}| / sum_j mu_j
        (primary; the tent assignment has period D in u), and
        K_h(alpha) = same with e^{i pi u_j / D} (secondary; the odd
        reflection of the lag pencil has period 2D).
      The landscape probe tested 'edge atom' only as a DISTANCE
      (score_a) and heavy commensurability as a STATIC offset
      (score_b); the frozen read here is the GRADIENT |dK/ds| along
      the profiles -- does it align with the needle positions?
  (c) THE LOCK-DIRECTION CONSTRUCTION itself: w_lock(alpha) =
      v1(alpha) t1 + v2(alpha) t2 with the closed v591 ratio
      v2/v1 = -(alpha^2 + 16 pi^2)/(2 (alpha^2 + 4 pi^2)).  Does the
      lock direction rotate FASTER at the needles than elsewhere
      (then the needle would be a property of the v596 projection,
      not of the form)?  Frozen read: the angular speed
      omega_lock(s) = dtheta_lock/ds by finite differences in the
      G0 metric (G = D G0 exactly -- scale drops out of angles,
      wiring-checked), compared to the minimal-mode angular speed
      omega_min(s) (truth side; ratio distribution reported).
  (d) THE POLE BLOCK: the explicit-formula pole density 2 cosh(u/2)
      reads on the lag lattice as c_pole[d] = kappa(D) 2 cosh(d D/2),
      kappa(D) = 8 (cosh(D/2) - 1)/D, and the assembled form
      A_pole = odd_toeplitz(c_pole) is EXACTLY rank 2:
        A_pole = 2 kappa [ (1-C) a a^T - (1+C) b b^T
                           + S (a b^T + b a^T) ],
        a_i = cosh(i D/2), b_i = sinh(i D/2),
        C = cosh((Mz-1) D/2), S = sinh((Mz-1) D/2)
      (cosh addition theorem; verified elementwise as an [E] bar).
      Frozen read: the pole-block weight W_pole(s) =
      ||P_pole m(s)||_G / ||m(s)||_G of the minimal mode, with P_pole
      the G-orthogonal projector onto span{a, b}; declared direction:
      HIGHER at needles.  (This read consumes the minimal mode -- if
      it hits it names the MECHANISM but is not an eigenvector-free
      predictor; declared, see M2.)

PREREGISTERED DECISIONS (declared BEFORE looking at the numbers):
  * base sweep, sample, slice choice, grid, guards: the
    w3_block_deflation probe VERBATIM (67 complete frame-A windows,
    truncated {1219, 1292, 1445}; lock sign; float floor; top-4 by P
    {859, 363, 1430, 1393} + 4 h-quantile picks {210, 488, 839,
    1215}; 81-point alpha-grid +-10%, s = 0 forced, Mz fixed per
    window, atom-complete only; rid anchor block; theta(859) = 43.5
    +- 0.2 deg; 52 peaks with per-slice counts [9, 9, 6, 9, 8, 5, 1,
    5], of which 33 ROT (block-probe quote); 635 feasible points);
  * E wiring bars [E]: E1 pole rank-2 identity elementwise rel dev
    < 1e-10 (vs max |A_pole|) on all 8 slices at s = 0; E2 metric
    wiring: the s = 0 angle recomputed in G0 matches the Gm angle to
    1e-8 deg AND the lock 2x2 Gram from the T163 lag weights matches
    the direct t_i^T G0 t_j to rel 1e-10; E3 jump closed form: every
    computed crossing s* of the heaviest atom on the h = 210 profile
    has frac(u Mz / (2 alpha_0 (1+s*))) < 1e-9 and the floor differs
    across s* +- 1e-6;
  * T1 teeth [E, must-detect]: a planted score = needle-label +
    N(0, TEETH_SD = 0.5) must pass the pointwise gate machinery
    (prec@prev >= bar AND cyclic-shift p < 0.01) -- otherwise the
    statistics wiring is broken;
  * labels (landscape verbatim): pointwise label = grid point inside
    a FWHM interval; needle window = FWHM +- 1 grid step (block probe
    convention) for needle-level medians; needle centers = the 52
    peak grid indices;
  * M1a gate [frozen]: predicted set = heavy-atom jump events; greedy
    1-1 match to the 52 needle centers (tol EV_TOL = 0.0025, block
    machinery); HIT iff (precision AND recall >= 0.80) OR the
    distance separation carries: pooled mean nearest-event distance
    of the 52 needles vs B_NULL = 2000 per-profile uniform
    placements, p < 0.01 AND obs/median(null) <= 0.5.  The all-atom
    crossing density and the atom-entry count are REPORTED (their PR
    is degenerate at measured density -- the density is the read);
  * M1b/M1c/M1d gate [frozen, landscape R2 verbatim]: pointwise score
    vs label -- precision@prevalence >= max(0.5, 2 x prevalence) AND
    cyclic-shift permutation p < 0.01 (B_PERM = 5000, shifts inside
    each profile) AND the declared sign (all three scores HIGH at
    needles); scores: (b) |dK/ds| and |dK_h/ds| (two declared tests),
    (c) omega_lock, (d) W_pole; 6 gated tests total -> Bonferroni-
    honest bar p < 0.0017 noted, not enforced;
  * M2 decision (frozen precedence): >= 1 of (a)/(b)/(c) hits ->
    NEEDLE-ASSEMBLY-PREDICTED: the predicate is formulated and the
    frame-A safety table is rebuilt from the EIGENVECTOR-FREE
    predictor (precedence a > b > c): per complete window the
    distance from s = 0 to the nearest predicted needle on a fine
    scan (+-2.5%, step 0.025%; (a) events closed-form; (b)/(c) local
    maxima of the score above THRESH = pooled median of the score at
    the 52 needle centers), censored at 2.5%; FRAME-A-SAFE iff min
    distance >= 10 x W_NEEDLE (W = 2.5e-4).  ONLY (d) hits ->
    NEEDLE-POLE-DIAGNOSTIC (mechanism named, NOT a predictor -- no
    safety table, declared).  None hits -> NEEDLE-EMERGENT-BULK: the
    honest conclusion; the needles are documented as an emergent bulk
    property with the best partial structure found, and the W3
    strategy recommendation quotes the carrying form: the v659
    MARGIN-regime statement (lambda_min < -floor on 0.0000 of the
    635 landscape points; MARGIN-regime share of P > 0.95 = 0.0% on
    the unremarkable slices) plus the v668 Ihara calibration (true
    positivity has NO uniform margin -- vanishing margins on deeper
    windows are the EXPECTED profile);
  * M3 typing only: contract-note text printed; no marker move.

Verdict enums (frozen, precedence top-down):
  NEEDLE-MECH-MIXED          guards, E bars or T1 teeth fail;
  NEEDLE-ASSEMBLY-PREDICTED  >= 1 eigenvector-free candidate (a/b/c)
                             passes its gate;
  NEEDLE-POLE-DIAGNOSTIC     only (d) passes;
  NEEDLE-EMERGENT-BULK       no candidate passes.

FIREWALL: experiments-only; verification/ read-only (v563 import;
v618/v591/rid/landscape machinery REBUILT verbatim, no other
imports); no marker moves; no positivity claim; no RH statement; NO
zero of any L-function is read (AST-checked).  Python-only, per
GATE.WOLFRAM.02.

Provenance: w3_block_deflation_probe (2026-08-02, BLOCK-DEFL-FAIL +
the needle table + the grid machinery), lehmer_resonance_probe
(LEHMER-NULL), baez_duarte_probe (BD-CONTROL-CLEAN, B3), w3_
resonance_landscape_probe (the 52 peaks + regime typing + R2 gate
machinery), rid_alignment_probe / margin_link_probe (lock geometry,
P = q tan^2 theta), v618 (C = 1 reads), v591 (closed lock direction),
v659 (landscape promotion, MARGIN quotes), v668 (Ihara calibration).
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
SLICES_QUOTE = [859, 363, 1430, 1393, 210, 488, 839, 1215]
A3_SHIFT_IDX = (-20, -10, 10, 20)
STAB_BAR = 0.15
# reproduction anchors (landscape/rid/block quotes, verbatim)
P_MAX_QUOTE, P_MAX_TOL = 0.9636, 0.005
H_AT_PMAX = 859
SP_P_H_QUOTE, SP_TOL = 0.735, 0.03
SP_RID_H_QUOTE = -0.784
RID_MED_QUOTE, RID_TOL = 0.584, 0.005
THETA_MED_QUOTE = 9.1
PEAKS_QUOTE = 52
PEAKS_SLICE_QUOTE = [9, 9, 6, 9, 8, 5, 1, 5]
N_ROT_QUOTE = 33             # block-probe needle-regime quote
THETA_859_QUOTE, THETA_859_TOL = 43.5, 0.2
N_POINTS_QUOTE = 635
BAR_EIGEN = 1e-6
BAR_REBUILD = 1e-12
# this probe's frozen additions
SEED = 20260812              # fresh (lehmer 20260811, theta 20260810)
B_PERM = 5000                # cyclic-shift budget (landscape verbatim)
B_NULL = 2000                # (a) distance-null placements
P_BAR = 0.01                 # permutation p gate
PR_BAR = 0.80                # (a) precision/recall bar (M2, declared)
RATIO_BAR = 0.50             # (a) distance separation obs/null-median
EV_TOL = 0.0025              # greedy match tolerance (one grid step)
K_HEAVY = 12                 # heaviest atoms (landscape verbatim)
TEETH_SD = 0.5               # T1 planted-noise scale
BAR_POLE_ID = 1e-10          # E1 rank-2 identity bar (rel to max)
BAR_WIRE = 1e-8              # E2 wiring bars (deg / rel)
BAR_JUMP = 1e-9              # E3 crossing residual bar
W_NEEDLE = 2.5e-4            # needle-width unit (landscape zoom read)
S_SCAN = 0.025               # A3 scan half-width
FINE_STEP = 0.00025          # A3 fine-scan step
SAFE_BAR = 10.0              # FRAME-A-SAFE bar in needle widths
N_TESTS = 6                  # gated tests (Bonferroni-honest note)

# declared external quotes for the M2 fallback (sources: v659 run
# 2026-08-02 R3 block; v668 part-1 header; both in this repo)
V659_QUOTE = ("v659 landscape: lambda_min < -floor on 0.0000 of the "
              "635 grid points (all 8 slices; lambda_min > 0 "
              "everywhere above the float floor); MARGIN-regime "
              "share of P > 0.95 = 0.0% on the unremarkable slices "
              "(P > 0.8: 1.3%)")
V668_QUOTE = ("v668 Ihara ground truth: TRUE positivity has NO "
              "uniform margin -- the Toeplitz window forms of a "
              "PROVEN RH instance are PSD with delta(K) > 0 only, "
              "vanishing on deeper windows; a vanishing margin is "
              "the EXPECTED profile of a true positivity")


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


def prec_at_prev(score, label, low_favors):
    N = int(label.sum())
    order = np.argsort(score if low_favors else -score,
                       kind="mergesort")
    return float(label[order[:N]].mean())


def cyclic_gate(name, sc_list, lb, rng, low_favors=False):
    """Landscape R2 gate machinery verbatim: precision@prevalence +
    cyclic-shift permutation p on the pooled Spearman."""
    sc = np.concatenate(sc_list)
    prev = float(lb.mean())
    pp = prec_at_prev(sc, lb, low_favors)
    rho = spearman(sc, lb)
    cnt = 0
    for _ in range(B_PERM):
        sh_ = [np.roll(v_, int(rng.integers(1, len(v_))))
               for v_ in sc_list]
        if abs(spearman(np.concatenate(sh_), lb)) >= abs(rho) - 1e-12:
            cnt += 1
    p_ = (cnt + 1.0) / (B_PERM + 1.0)
    sign_ok = (rho < 0.0) if low_favors else (rho > 0.0)
    bar = max(0.5, 2.0 * prev)
    hit = (pp >= bar) and (p_ < P_BAR) and sign_ok
    print("      %-24s prec@prev = %.3f (bar %.3f)  rho = %+.4f  "
          "p = %.4f  sign %s  -> %s"
          % (name, pp, bar, rho, p_, "ok" if sign_ok else "WRONG",
             "HIT" if hit else "miss"))
    return dict(pp=pp, bar=bar, rho=rho, p=p_, sign_ok=sign_ok,
                hit=hit, prev=prev)


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


# --------------------------------------------- hz-only caches (exact)
_HZ_CACHE = {}
U0_GRID = None
U_HEAVY = None
MU_HEAVY = None
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


# ------------------------------------------------- the candidate reads
def coherence(alpha, D):
    """(b) collective atom-phase coherence on the lag lattice."""
    ka = core.atoms_in(alpha)
    uu = core.U_ALL[:ka]
    muv = core.MU_ALL[:ka]
    ph = (2.0 * math.pi / D) * uu
    tot = float(muv.sum())
    z_full = complex(np.sum(muv * np.exp(1j * ph)))
    z_half = complex(np.sum(muv * np.exp(0.5j * ph)))
    return abs(z_full) / tot, abs(z_half) / tot


def pole_weight(vec, Gm, av, bv):
    """(d) ||P_pole vec||_G / ||vec||_G with P_pole the G-orthogonal
    projector onto span{a, b} (Gram-Schmidt in the G metric)."""
    Ga = Gm @ av
    Gb = Gm @ bv
    ip_aa = float(av @ Ga)
    ip_ab = float(av @ Gb)
    ip_bb = float(bv @ Gb)
    vGv = float(vec @ (Gm @ vec))
    ca = float(vec @ Ga) / math.sqrt(ip_aa)
    b2 = ip_bb - ip_ab ** 2 / ip_aa
    rank1 = b2 <= 1e-14 * ip_bb
    if rank1:
        ce = 0.0
    else:
        ce = (float(vec @ Gb)
              - (ip_ab / ip_aa) * float(vec @ Ga)) / math.sqrt(b2)
    w = math.sqrt(max(0.0, min(vGv, ca ** 2 + ce ** 2)) / vGv)
    return w, rank1


# ------------------------------------------------------ window builder
def window_eval(alpha, Mz):
    """One window at EXPLICIT (alpha, Mz): the landscape/block
    window_eval numerics verbatim (same assembly, same eigh),
    extended by the frozen candidate reads (b) and (d)."""
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
    lam_min, lam_2, v_min, rad = gen_min_eig2(A, Gm)
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
    # rid geometry: theta from the minimal mode (truth side)
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
    t2 = (st / ct) ** 2 if ct > 0.0 else float("inf")
    qq = Q_perp / lam_lock
    # (b) coherence
    K_full, K_half = coherence(alpha, D)
    # (d) pole-block weight (minimal mode + lock direction)
    rr = np.arange(hz, dtype=float)
    av = np.cosh(0.5 * rr * D)
    bv = np.sinh(0.5 * rr * D)
    wp, rank1 = pole_weight(m_vec, Gm, av, bv)
    wpl, _ = pole_weight(w_hat, Gm, av, bv)
    return dict(h=hz, alpha=alpha, D=D, complete=complete,
                lam=lam_min, lam2=lam_2, floor=floor, rad=rad,
                qr=q_r, qm=q_m, lock=q_r * q_m > 0.0,
                ct=ct, st=st, t2=t2, qq=qq, P=qq * t2,
                lam_lock=lam_lock, theta=math.degrees(math.acos(ct)),
                K=K_full, Kh=K_half, wp=wp, wpl=wpl, prank1=rank1,
                m_vec=m_vec, w_hat=w_hat, vl=vl)


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


# ------------------------------------------------- (a) the jump sets
def heavy_events(alpha0, Mz, s_lo, s_hi):
    """Closed-form integer crossings of tau_j(s) = u_j Mz /
    (2 alpha0 (1 + s)) for the K_HEAVY heaviest atoms."""
    ev = []
    for u in U_HEAVY:
        t_hi = u * Mz / (2.0 * alpha0 * (1.0 + s_lo))
        t_lo = u * Mz / (2.0 * alpha0 * (1.0 + s_hi))
        for n in range(int(math.floor(t_lo)) + 1,
                       int(math.floor(t_hi)) + 1):
            s = u * Mz / (2.0 * alpha0 * n) - 1.0
            if s_lo - 1e-12 <= s <= s_hi + 1e-12:
                ev.append(float(s))
    return np.array(sorted(ev))


def all_cross_count(alpha0, Mz, s_lo, s_hi):
    """All-atom integer-crossing count (atoms enter at s_j =
    u_j/(2 alpha0) - 1; tau decreasing in s)."""
    ka_hi = core.atoms_in(alpha0 * (1.0 + s_hi))
    uu = core.U_ALL[:ka_hi]
    s_start = np.maximum(s_lo, uu / (2.0 * alpha0) - 1.0)
    t_start = uu * Mz / (2.0 * alpha0 * (1.0 + s_start))
    t_end = uu * Mz / (2.0 * alpha0 * (1.0 + s_hi))
    return int(np.sum(np.floor(t_start) - np.floor(t_end)))


def nearest_dist(x, ev):
    j = int(np.searchsorted(ev, x))
    best = float("inf")
    if j < len(ev):
        best = min(best, float(ev[j] - x))
    if j > 0:
        best = min(best, float(x - ev[j - 1]))
    return best


# ------------------------------------------------- (c) angular speeds
def mode_speeds(cols, G0, ss):
    """Angular speed (deg per unit s) of a vector family by central
    finite differences in the G0 metric (sign-blind)."""
    n = cols.shape[1]
    GM = G0 @ cols
    nn = np.sqrt(np.einsum("ij,ij->j", cols, GM))
    om = np.empty(n)
    for i in range(n):
        i0, i1 = max(0, i - 1), min(n - 1, i + 1)
        c = abs(float(cols[:, i0] @ GM[:, i1])) / (nn[i0] * nn[i1])
        om[i] = math.degrees(math.acos(min(1.0, c))) \
            / (ss[i1] - ss[i0])
    return om


def lock_speeds(vls, Gam, ss):
    """Angular speed of the lock 2-vector in the (t1, t2) Gram
    metric Gam (exact G0 pullback via the T163 lag weights)."""
    n = len(vls)
    nn = np.sqrt(np.einsum("ij,jk,ik->i", vls, Gam, vls))
    om = np.empty(n)
    for i in range(n):
        i0, i1 = max(0, i - 1), min(n - 1, i + 1)
        c = abs(float(vls[i0] @ (Gam @ vls[i1]))) / (nn[i0] * nn[i1])
        om[i] = math.degrees(math.acos(min(1.0, c))) \
            / (ss[i1] - ss[i0])
    return om


def grad_abs(vals, ss):
    n = len(vals)
    out = np.empty(n)
    for i in range(n):
        i0, i1 = max(0, i - 1), min(n - 1, i + 1)
        out[i] = abs((vals[i1] - vals[i0]) / (ss[i1] - ss[i0]))
    return out


def run():
    global N_CHK, FAILS, U0_GRID, U_HEAVY, MU_HEAVY
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE NEEDLE MECHANISM -- four assembly-side candidates on "
          "the 52 landscape needles")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    U0_GRID = zeta_grid_const()
    mu_all = np.array([float(m) for m in core.MU_ALL])
    heavy_idx = np.argsort(-mu_all)[:K_HEAVY]
    U_HEAVY = np.array([float(core.U_ALL[i]) for i in heavy_idx])
    MU_HEAVY = mu_all[heavy_idx]
    n_all = np.rint(np.exp(np.array(
        [float(u) for u in core.U_ALL]))).astype(int)
    print("      heavy atoms (landscape convention): n = %s"
          % sorted(n_all[heavy_idx].tolist()))

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
    al = np.array([r["alpha"] for r in lock_c])
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
          "deg (quote %.1f, tol %.1f)"
          % (th859, THETA_859_QUOTE, THETA_859_TOL),
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
    sel_hs = [int(hs[i]) for i in sel]
    check("G0.5 [E] slice selection: 8 distinct windows -> h = %s "
          "(declared quote %s)" % (sel_hs, SLICES_QUOTE),
          len(set(sel)) == 8 and sel_hs == SLICES_QUOTE)

    # ------------------------------------------------ the profiles
    print("\nR1 -- the 8 alpha-profiles (landscape grid rebuilt "
          "verbatim; candidate reads per point)")
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
                  th=np.array([rv["theta"] for rv in recs]),
                  Kp=np.array([rv["K"] for rv in recs]),
                  Khp=np.array([rv["Kh"] for rv in recs]),
                  wp=np.array([rv["wp"] for rv in recs]))
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
    step = 2.0 * S_MAX / (N_GRID - 1)
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
        mask = np.zeros(len(ss), bool)
        wmask = np.zeros(len(ss), bool)
        for iv in intervals:
            mask |= (ss >= iv["s_l"]) & (ss <= iv["s_r"])
            wmask |= (ss >= iv["s_l"] - step - 1e-15) \
                & (ss <= iv["s_r"] + step + 1e-15)
        pr["mask"] = mask
        pr["wmask"] = wmask
        all_peaks.extend((pr, iv) for iv in intervals)
    n_peaks_tot = len(all_peaks)
    per_slice = [len(pr["peaks"]) for pr in profiles]
    n_rot_pk = sum(1 for pr, iv in all_peaks
                   if pr["regs"][iv["ip"]] == "ROT")
    check("G0.8 [E] the landscape peak set reproduces: %d peaks "
          "total (quote %d); per-slice counts %s (quote %s); ROT "
          "needles %d (block quote %d)"
          % (n_peaks_tot, PEAKS_QUOTE, per_slice, PEAKS_SLICE_QUOTE,
             n_rot_pk, N_ROT_QUOTE),
          n_peaks_tot == PEAKS_QUOTE
          and per_slice == PEAKS_SLICE_QUOTE
          and n_rot_pk == N_ROT_QUOTE)

    lb = np.concatenate([pr["mask"].astype(float) for pr in profiles])
    n_pts = len(lb)
    check("A0.1 [E] the grid-point count reproduces: %d feasible "
          "profile points (quote %d)" % (n_pts, N_POINTS_QUOTE),
          n_pts == N_POINTS_QUOTE)

    # -------------------------------------- E wiring: pole + metric
    print("\nE -- wiring bars (pole rank-2 identity, metric scale, "
          "lock Gram, jump closed form)")
    dev_pole = 0.0
    sig_rows = []
    for pr in profiles:
        r0 = pr["r0"]
        Mz = r0["Mz"]
        hz = Mz // 2
        D0 = pr["recs"][pr["i0"]]["D"]
        kap = 8.0 * (math.cosh(0.5 * D0) - 1.0) / D0
        dd = np.arange(Mz, dtype=float)
        cp = kap * 2.0 * np.cosh(0.5 * dd * D0)
        Ap = core.odd_toeplitz(cp, Mz)
        rr = np.arange(hz, dtype=float)
        av = np.cosh(0.5 * rr * D0)
        bv = np.sinh(0.5 * rr * D0)
        c0 = 0.5 * (Mz - 1) * D0
        Cc, Sc = math.cosh(c0), math.sinh(c0)
        Ap2 = 2.0 * kap * ((1.0 - Cc) * np.outer(av, av)
                           - (1.0 + Cc) * np.outer(bv, bv)
                           + Sc * (np.outer(av, bv)
                                   + np.outer(bv, av)))
        dev_pole = max(dev_pole, float(np.max(np.abs(Ap - Ap2))
                                       / np.max(np.abs(Ap))))
        # restricted 2x2 signature in the G-orthonormal pole basis
        g0v = np.zeros(Mz)
        g0v[0], g0v[1] = 2.0 / 3.0, 1.0 / 6.0
        G0 = core.odd_toeplitz(g0v, Mz)
        Q = np.column_stack([av, bv])
        Sg = Q.T @ (G0 @ Q)
        L = np.linalg.cholesky(Sg)
        T2 = Q.T @ (Ap @ Q)
        Tn = np.linalg.solve(L, np.linalg.solve(L, T2).T).T
        ev2 = np.linalg.eigvalsh(0.5 * (Tn + Tn.T))
        sig_rows.append((r0["h"], float(ev2[0]), float(ev2[1])))
        pr["G0"] = G0
    check("E1 [E] the pole block is EXACTLY rank 2 on every slice: "
          "odd_toeplitz(kappa 2cosh(dD/2)) == 2 kappa [(1-C) aa^T - "
          "(1+C) bb^T + S(ab^T + ba^T)] with max elementwise rel dev "
          "%.1e < %.0e; restricted signature (lo, hi eigenvalue in "
          "the G-orthonormal pole basis): %s -- one negative, one "
          "positive direction (cosh-like, indefinite)"
          % (dev_pole, BAR_POLE_ID,
             [("h=%d" % h_, "%.2e" % lo_, "%.2e" % hi_)
              for h_, lo_, hi_ in sig_rows[:2]]),
          dev_pole < BAR_POLE_ID)

    dev_ang = 0.0
    dev_gam = 0.0
    for pr in profiles:
        r0 = pr["r0"]
        hz = r0["Mz"] // 2
        G0 = pr["G0"]
        t1v, t2v, W11, W22, W12 = hz_objects(hz)
        rv0 = pr["recs"][pr["i0"]]
        # angle in G0 == angle in Gm (= D G0), against the rec theta
        wv = rv0["w_hat"]
        mv = rv0["m_vec"]
        cg = abs(float(wv @ (G0 @ mv))) / math.sqrt(
            float(wv @ (G0 @ wv)) * float(mv @ (G0 @ mv)))
        th_g0 = math.degrees(math.acos(min(1.0, cg)))
        dev_ang = max(dev_ang, abs(th_g0 - rv0["theta"]))
        # lock 2x2 Gram: lag weights vs direct
        g23, g16 = 2.0 / 3.0, 1.0 / 6.0
        Gam = np.array([[g23 * W11[0] + g16 * W11[1],
                         g23 * W12[0] + g16 * W12[1]],
                        [g23 * W12[0] + g16 * W12[1],
                         g23 * W22[0] + g16 * W22[1]]])
        Gam_d = np.array([[float(t1v @ (G0 @ t1v)),
                           float(t1v @ (G0 @ t2v))],
                          [float(t1v @ (G0 @ t2v)),
                           float(t2v @ (G0 @ t2v))]])
        dev_gam = max(dev_gam, float(np.max(np.abs(Gam - Gam_d))
                                     / np.max(np.abs(Gam_d))))
        pr["Gam"] = Gam
    check("E2 [E] metric wiring: G = D G0 exactly (scale drops out "
          "of angles) -- s = 0 angle recomputed in G0 deviates %.1e "
          "deg < %.0e from the Gm read; lock 2x2 Gram from the T163 "
          "lag weights matches the direct t_i^T G0 t_j to rel %.1e "
          "< 1e-10" % (dev_ang, BAR_WIRE, dev_gam),
          dev_ang < BAR_WIRE and dev_gam < 1e-10)

    pr210 = [pr for pr in profiles if pr["r0"]["h"] == 210][0]
    a0_210 = pr210["r0"]["alpha"]
    Mz_210 = pr210["r0"]["Mz"]
    u_top = float(U_HEAVY[0])
    ev_spot = []
    for u in (u_top,):
        t_hi = u * Mz_210 / (2.0 * a0_210 * (1.0 + pr210["ss"][0]))
        t_lo = u * Mz_210 / (2.0 * a0_210 * (1.0 + pr210["ss"][-1]))
        for n_ in range(int(math.floor(t_lo)) + 1,
                        int(math.floor(t_hi)) + 1):
            ev_spot.append((u * Mz_210 / (2.0 * a0_210 * n_) - 1.0,
                            n_))
    res_max = 0.0
    floor_ok = True
    for s_, n_ in ev_spot:
        tau = u_top * Mz_210 / (2.0 * a0_210 * (1.0 + s_))
        res_max = max(res_max, abs(tau - round(tau)))
        tp = u_top * Mz_210 / (2.0 * a0_210 * (1.0 + s_ + 1e-6))
        tm = u_top * Mz_210 / (2.0 * a0_210 * (1.0 + s_ - 1e-6))
        if int(math.floor(tp)) == int(math.floor(tm)):
            floor_ok = False
    check("E3 [E] jump closed form on the heaviest atom (u = %.4f, "
          "h = 210 profile): %d crossings, max |tau - round(tau)| = "
          "%.1e < %.0e, floor differs across every s* +- 1e-6: %s"
          % (u_top, len(ev_spot), res_max, BAR_JUMP, floor_ok),
          res_max < BAR_JUMP and floor_ok)

    # ------------------------------------------------ scores per point
    for pr in profiles:
        ss = pr["ss"]
        pr["sc_b"] = grad_abs(pr["Kp"], ss)
        pr["sc_bh"] = grad_abs(pr["Khp"], ss)
        Mcols = np.column_stack([rv["m_vec"] for rv in pr["recs"]])
        pr["om_min"] = mode_speeds(Mcols, pr["G0"], ss)
        vls = np.array([rv["vl"] for rv in pr["recs"]])
        pr["om_lock"] = lock_speeds(vls, pr["Gam"], ss)
        del pr["G0"]           # free the h x h metric

    rng = np.random.default_rng(SEED)

    # ------------------------------------------------ T1 teeth
    print("\nT1 -- teeth: the planted score must be detected by the "
          "gate machinery")
    teeth_list = []
    for pr in profiles:
        y = pr["mask"].astype(float) \
            + rng.normal(0.0, TEETH_SD, len(pr["ss"]))
        teeth_list.append(y)
    gt = cyclic_gate("teeth (label + noise)", teeth_list, lb, rng)
    check("T1.1 [E, must-detect] planted score = needle label + "
          "N(0, %.1f): prec@prev %.3f >= %.3f, p = %.4f < %.2f -> "
          "the machinery detects a real needle alignment of this "
          "size" % (TEETH_SD, gt["pp"], gt["bar"], gt["p"], P_BAR),
          gt["hit"])

    # ------------------------------------------------ M1a: jump sets
    print("\nM1a -- candidate (a): the lag-quantization jump set")
    print("      profile   heavy ev   ev/step   all-atom crossings"
          "   /step   atom entries   /step")
    obs_d = []
    ev_by_pr = []
    n_ev_tot = 0
    matched = 0
    for pr in profiles:
        r0 = pr["r0"]
        ss = pr["ss"]
        s_lo, s_hi = float(ss[0]), float(ss[-1])
        ev = heavy_events(r0["alpha"], r0["Mz"], s_lo, s_hi)
        ev_by_pr.append(ev)
        n_step = len(ss) - 1
        n_all_x = all_cross_count(r0["alpha"], r0["Mz"], s_lo, s_hi)
        n_ent = core.atoms_in(r0["alpha"] * (1.0 + s_hi)) \
            - core.atoms_in(r0["alpha"] * (1.0 + s_lo))
        print("      h = %4d   %6d    %6.2f      %8d        %7.1f"
              "      %8d     %7.1f"
              % (r0["h"], len(ev), len(ev) / n_step, n_all_x,
                 n_all_x / n_step, n_ent, n_ent / n_step))
        centers = [iv["s"] for iv in pr["peaks"]]
        n_ev_tot += len(ev)
        matched += greedy_match(centers, ev.tolist(), EV_TOL)
        for c_ in centers:
            obs_d.append(nearest_dist(c_, ev))
    prec_a = matched / float(n_ev_tot) if n_ev_tot else float("nan")
    rec_a = matched / float(n_peaks_tot)
    obs_mean = float(np.mean(obs_d))
    rng_a = np.random.default_rng(SEED + 1)
    null_means = np.empty(B_NULL)
    for b_ in range(B_NULL):
        acc = []
        for pr, ev in zip(profiles, ev_by_pr):
            ss = pr["ss"]
            k_ = len(pr["peaks"])
            if k_ == 0:
                continue
            draws = rng_a.uniform(float(ss[0]), float(ss[-1]), k_)
            for x in draws:
                acc.append(nearest_dist(float(x), ev))
        null_means[b_] = float(np.mean(acc))
    p_null = float((np.sum(null_means <= obs_mean + 1e-15) + 1.0)
                   / (B_NULL + 1.0))
    null_med = float(np.median(null_means))
    ratio_a = obs_mean / null_med if null_med > 0 else float("inf")
    hit_a_pr = prec_a >= PR_BAR and rec_a >= PR_BAR
    hit_a_d = p_null < P_BAR and ratio_a <= RATIO_BAR
    hit_a = hit_a_pr or hit_a_d
    check("M1a.1 [MEASURED, gate] heavy-atom jump events vs the %d "
          "needles: %d events pooled (greedy 1-1, tol %.4f) -> "
          "matched %d, precision %.4f / recall %.4f (bar %.2f both: "
          "%s); distance separation: mean nearest-event distance "
          "%.5f vs null median %.5f (ratio %.2f, bar <= %.2f), "
          "permutation p = %.4f (< %.2f: %s) -> candidate (a) %s.  "
          "The all-atom crossing set and the entry set are DENSE at "
          "the measured rates above -- their PR is degenerate by "
          "density (declared)"
          % (n_peaks_tot, n_ev_tot, EV_TOL, matched, prec_a, rec_a,
             PR_BAR, "HIT" if hit_a_pr else "miss",
             obs_mean, null_med, ratio_a, RATIO_BAR, p_null, P_BAR,
             "HIT" if hit_a_d else "miss",
             "HIT" if hit_a else "MISS"), True)

    # ------------------------------------------------ M1b: coherence
    print("\nM1b -- candidate (b): atom-phase coherence gradient "
          "|dK/ds| (pointwise gate, label = FWHM regions)")
    for pr in profiles:
        print("      h = %4d: K in [%.4f, %.4f], K_half in [%.4f, "
              "%.4f], |dK/ds| median %.4f / max %.4f"
              % (pr["r0"]["h"], float(pr["Kp"].min()),
                 float(pr["Kp"].max()), float(pr["Khp"].min()),
                 float(pr["Khp"].max()),
                 float(np.median(pr["sc_b"])),
                 float(pr["sc_b"].max())))
    g_b = cyclic_gate("(b) |dK/ds| (2pi phase)",
                      [pr["sc_b"] for pr in profiles], lb, rng)
    g_bh = cyclic_gate("(b) |dK_h/ds| (pi phase)",
                       [pr["sc_bh"] for pr in profiles], lb, rng)
    hit_b = g_b["hit"] or g_bh["hit"]
    ranks_b = []
    for pr in profiles:
        sc = pr["sc_b"]
        for iv in pr["peaks"]:
            ranks_b.append((float(np.sum(sc <= sc[iv["ip"]])) - 0.5)
                           / len(sc))
    check("M1b.1 [MEASURED, gate] coherence gradient at the needles: "
          "2pi-phase prec@prev %.3f, rho %+.4f, p %.4f; pi-phase "
          "prec@prev %.3f, rho %+.4f, p %.4f; median within-profile "
          "quantile rank of |dK/ds| at the 52 needle centers = %.3f "
          "(no-signal expectation 0.5) -> candidate (b) %s"
          % (g_b["pp"], g_b["rho"], g_b["p"], g_bh["pp"],
             g_bh["rho"], g_bh["p"], float(np.median(ranks_b)),
             "HIT" if hit_b else "MISS"), True)

    # ------------------------------------------------ M1c: lock speed
    print("\nM1c -- candidate (c): the lock-direction angular speed "
          "dtheta_lock/ds vs the minimal mode")
    om_l_all = np.concatenate([pr["om_lock"] for pr in profiles])
    om_m_all = np.concatenate([pr["om_min"] for pr in profiles])
    wmask_all = np.concatenate([pr["wmask"] for pr in profiles])
    g_c = cyclic_gate("(c) omega_lock",
                      [pr["om_lock"] for pr in profiles], lb, rng)
    hit_c = g_c["hit"]
    med_l_nd = float(np.median(om_l_all[wmask_all]))
    med_l_off = float(np.median(om_l_all[~wmask_all]))
    med_m_nd = float(np.median(om_m_all[wmask_all]))
    med_m_off = float(np.median(om_m_all[~wmask_all]))
    ratio_nd = om_l_all[wmask_all] / om_m_all[wmask_all]
    ratio_off = om_l_all[~wmask_all] / om_m_all[~wmask_all]
    check("M1c.1 [MEASURED, gate] omega_lock median %.3f deg per "
          "unit s at needle windows vs %.3f off (minimal mode: "
          "%.1f vs %.1f); ratio omega_lock/omega_min median %.2e at "
          "needles vs %.2e off -> the lock construction rotates %s "
          "-> candidate (c) %s"
          % (med_l_nd, med_l_off, med_m_nd, med_m_off,
             float(np.median(ratio_nd)), float(np.median(ratio_off)),
             "FASTER at the needles" if med_l_nd > 2.0 * med_l_off
             else "at its smooth background rate everywhere (the "
             "needle rotation belongs to the minimal mode, not the "
             "v596 projection)",
             "HIT" if hit_c else "MISS"), True)

    # ------------------------------------------------ M1d: pole block
    print("\nM1d -- candidate (d): the pole-block weight "
          "||P_pole m||_G / ||m||_G of the minimal mode")
    n_rank1 = sum(int(rv["prank1"]) for pr in profiles
                  for rv in pr["recs"])
    g_d = cyclic_gate("(d) W_pole(minimal mode)",
                      [pr["wp"] for pr in profiles], lb, rng)
    hit_d = g_d["hit"]
    wp_all = np.concatenate([pr["wp"] for pr in profiles])
    wp0 = np.array([r["wp"] for r in lock_c])
    wpl0 = np.array([r["wpl"] for r in lock_c])
    sp_wp_a = spearman(wp0, al)
    check("M1d.1 [MEASURED, gate] W_pole median %.4f at needle "
          "windows vs %.4f off (max %.4f; degenerate-rank points "
          "%d/%d); base-sweep trend Spearman(W_pole(s=0), alpha) = "
          "%+.3f over the %d lock windows (the 'grows with alpha' "
          "read); lock-direction pole alignment W_pole(w_lock) "
          "median %.4f -> candidate (d) %s"
          % (float(np.median(wp_all[wmask_all])),
             float(np.median(wp_all[~wmask_all])),
             float(wp_all.max()), n_rank1, n_pts, sp_wp_a, n,
             float(np.median(wpl0)),
             "HIT" if hit_d else "MISS"), True)

    # ------------------------------------------------ M2: decision
    print("\nM2 -- the decision (frozen precedence: eigenvector-free "
          "a > b > c; d alone is diagnostic-only)")
    hits_free = [nm for nm, hh in (("a", hit_a), ("b", hit_b),
                                   ("c", hit_c)) if hh]
    guards_ok = not any(f_.startswith(("G0", "E", "T1", "A0"))
                        for f_ in FAILS)
    if not guards_ok:
        VERDICT = "NEEDLE-MECH-MIXED (guards or teeth failed)"
    elif hits_free:
        VERDICT = "NEEDLE-ASSEMBLY-PREDICTED"
    elif hit_d:
        VERDICT = "NEEDLE-POLE-DIAGNOSTIC"
    else:
        VERDICT = "NEEDLE-EMERGENT-BULK"

    d_min, h_min, safe = float("inf"), [], False
    if hits_free:
        cand = hits_free[0]
        print("      A3 frame-A safety from the eigenvector-free "
              "predictor (%s); fine scan +-%.1f%%, step %.3f%%"
              % (cand, 100 * S_SCAN, 100 * FINE_STEP))
        if cand == "b":
            th_b = float(np.median(np.concatenate(
                [[pr["sc_b"][iv["ip"]] for iv in pr["peaks"]]
                 for pr in profiles if pr["peaks"]])))
        if cand == "c":
            th_c = float(np.median(np.concatenate(
                [[pr["om_lock"][iv["ip"]] for iv in pr["peaks"]]
                 for pr in profiles if pr["peaks"]])))
        t4 = []
        for r0_ in sorted(comp, key=lambda r: r["h"]):
            a0, Mz = r0_["alpha"], r0_["Mz"]
            hz = Mz // 2
            s_hi_f = min(S_SCAN, math.log(core.ATOM_MAX + 0.5)
                         / (2.0 * a0) - 1.0)
            ss_f = np.arange(-S_SCAN, s_hi_f + 1e-12, FINE_STEP)
            if cand == "a":
                ev = heavy_events(a0, Mz, float(ss_f[0]),
                                  float(ss_f[-1]))
                d0 = nearest_dist(0.0, ev) if len(ev) \
                    else float("nan")
            else:
                if cand == "b":
                    vals = np.array([coherence(
                        a0 * (1.0 + s_), 2.0 * a0 * (1.0 + s_) / Mz
                    )[0] for s_ in ss_f])
                    sc_f = grad_abs(vals, ss_f)
                    thr = th_b
                else:
                    t1v, t2v, W11, W22, W12 = hz_objects(hz)
                    g23, g16 = 2.0 / 3.0, 1.0 / 6.0
                    Gam = np.array(
                        [[g23 * W11[0] + g16 * W11[1],
                          g23 * W12[0] + g16 * W12[1]],
                         [g23 * W12[0] + g16 * W12[1],
                          g23 * W22[0] + g16 * W22[1]]])
                    vls = np.array([lock_dir(a0 * (1.0 + s_))
                                    for s_ in ss_f])
                    sc_f = lock_speeds(vls, Gam, ss_f)
                    thr = th_c
                cands = [float(ss_f[i]) for i in
                         range(1, len(ss_f) - 1)
                         if sc_f[i] >= sc_f[i - 1]
                         and sc_f[i] >= sc_f[i + 1]
                         and sc_f[i] >= thr]
                d0 = min((abs(x) for x in cands),
                         default=float("nan"))
            t4.append((r0_["h"], d0))
        print("      h     d_pred      d/W")
        for h_, d_ in t4:
            d_s = ("%.6f" % d_) if not math.isnan(d_) \
                else (">=%.4f" % S_SCAN)
            dw = ("%8.1f" % (d_ / W_NEEDLE)) if not math.isnan(d_) \
                else (">=%6.0f" % (S_SCAN / W_NEEDLE))
            print("      %4d  %s  %s" % (h_, d_s, dw))
        d_ana = [d_ for _, d_ in t4 if not math.isnan(d_)]
        d_min = min(d_ana) if d_ana else float("inf")
        h_min = [h_ for h_, d_ in t4 if d_ == d_min]
        safe = d_min >= SAFE_BAR * W_NEEDLE
        check("M2.1 [MEASURED] frame-A safety from the %s-predictor "
              "on the %d complete windows: MIN distance %.6f at "
              "h = %s = %.1f needle widths (bar %.0f W) -> %s"
              % (cand, len(comp), d_min, h_min, d_min / W_NEEDLE,
                 SAFE_BAR,
                 "FRAME-A-SAFE" if safe else "FRAME-A-TIGHT"), True)
    else:
        best = max((("(a) jump-distance", 1.0 - p_null),
                    ("(b) coherence gradient", 1.0 - g_b["p"]),
                    ("(b) half-phase gradient", 1.0 - g_bh["p"]),
                    ("(c) omega_lock", 1.0 - g_c["p"]),
                    ("(d) pole weight", 1.0 - g_d["p"])),
                   key=lambda x_: x_[1])
        check("M2.2 [MEASURED] no assembly candidate carries "
              "(%d gated tests, Bonferroni-honest bar p < %.4f): "
              "the needles read as an EMERGENT BULK property of the "
              "window pencil -- consistent with the block-deflation "
              "leak 1.000 (the coupling is spread across the "
              "spectrum); best partial structure: %s (score %.4f); "
              "no scan, no safety table from an unvalidated "
              "predicate (frozen rule)"
              % (N_TESTS, P_BAR / N_TESTS, best[0], best[1]), True)

    # ------------------------------------------------ M3: typing
    check("M3.1 [C] the typed reading: after the triple negative "
          "(not low-rank, not zero-driven, not in the BD frame) the "
          "four assembly candidates measure: (a) jump set %s "
          "(precision %.3f / recall %.3f; separation ratio %.2f, "
          "p %.3f), (b) coherence gradient %s (p %.3f / %.3f), (c) "
          "lock rotation %s (needle/off median ratio %.2e vs %.2e), "
          "(d) pole weight %s (p %.3f) -> %s.  NO positivity claim, "
          "NO RH statement, NO marker move; W3 stays open"
          % ("HIT" if hit_a else "MISS", prec_a, rec_a, ratio_a,
             p_null, "HIT" if hit_b else "MISS", g_b["p"], g_bh["p"],
             "HIT" if hit_c else "MISS",
             float(np.median(ratio_nd)), float(np.median(ratio_off)),
             "HIT" if hit_d else "MISS", g_d["p"], VERDICT), True)

    print("\nVERDICT: %s" % VERDICT)
    if hits_free:
        conseq = ("the 'generic bound + ASSEMBLY predicate' contract "
                  "text is FORMULATABLE: needles are predicted by "
                  "the eigenvector-free candidate (%s); frame-A "
                  "safety: min distance %.1f W at h = %s -> %s."
                  % (hits_free[0], d_min / W_NEEDLE, h_min,
                     "FRAME-A-SAFE" if safe else "FRAME-A-TIGHT"))
    elif hit_d:
        conseq = ("the pole block NAMES the mechanism (the minimal "
                  "mode aligns with the cosh plane at the needles) "
                  "but reads the minimal mode -- diagnostic, not a "
                  "predictor; no safety table (frozen rule).")
    else:
        conseq = ("the needles are an EMERGENT BULK property: no "
                  "assembly-side predicate at the declared bars.  "
                  "The carrying W3 form is the MARGIN-REGIME "
                  "statement -- %s -- combined with the Ihara "
                  "calibration: %s.  The strategy recommendation is "
                  "to contract W3 as 'margin-regime generic bound + "
                  "needle risk map' (v659), NOT as a uniform bound "
                  "with an exception predicate." % (V659_QUOTE,
                                                    V668_QUOTE))
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, needle-mechanism round (2026-08-02): after
  the triple negative (BLOCK-DEFL-FAIL: leak 1.000 over K = 1..8;
  LEHMER-NULL: not zero-comb-driven; BD-CONTROL-CLEAN: no needle in
  the external Baez-Duarte frame), four ASSEMBLY-side candidates
  were gated on the 52 classified landscape needles (8 alpha-
  profiles, 635 points, labels = FWHM regions, cyclic-shift
  permutation B = %d, seed %d):
  (a) LAG QUANTIZATION -- the closed-form jump set of the atom-to-
  cell assignment floor(u_j/D(s)): heavy-atom events matched to the
  needles at precision %.3f / recall %.3f (bar 0.8); distance
  separation obs/null = %.2f (p = %.3f) -> %s;
  (b) ATOM-PHASE COHERENCE K = |sum mu_j e^{2pi i u_j/D}|/sum mu_j:
  gradient gate prec@prev %.3f, rho %+.3f, p = %.3f (pi-phase:
  p = %.3f) -> %s;
  (c) LOCK-DIRECTION ROTATION dtheta_lock/ds: median %.3f deg/unit-s
  at needles vs %.3f off (ratio to the minimal-mode speed %.1e vs
  %.1e -- the needle rotation belongs to the MODE, not the v596
  projection) -> %s;
  (d) POLE BLOCK (exact rank-2, cosh-like, [E]-verified): W_pole =
  ||P_pole m||_G median %.4f at needles vs %.4f off, p = %.3f,
  alpha-trend %+.3f -> %s.
  DECISION: %s.  %s
  TYPE: measured landscape mechanism scan on the declared surface;
  no positivity claim; no RH statement; Problem 7.1 untouched; no
  marker move.
""" % (B_PERM, SEED, prec_a, rec_a, ratio_a, p_null,
       "HIT" if hit_a else "MISS",
       g_b["pp"], g_b["rho"], g_b["p"], g_bh["p"],
       "HIT" if hit_b else "MISS",
       med_l_nd, med_l_off,
       float(np.median(ratio_nd)), float(np.median(ratio_off)),
       "HIT" if hit_c else "MISS",
       float(np.median(wp_all[wmask_all])),
       float(np.median(wp_all[~wmask_all])), g_d["p"], sp_wp_a,
       "HIT" if hit_d else "MISS", VERDICT, conseq))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s (%d window evals)"
          % (time.time() - T0, N_EVAL))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
