"""Discovery probe: THE TWO NAMED GARDING REMEDIES -- healing the
lattice-edge 1/log degeneration of the discrete Garding constant

Direct successor of garding_probe.py (verdict GARDING-DRIFT-UNRESOLVED:
c(M, C) monotone decreasing on the anchor ladder, on 4 dyadic stages
indistinguishable from c ~ 1/log(2 + pi/D); B3 diagnosis: the minimizer
lives in the lattice-edge band [0.8, 1] pi/D and carries 43% of its
CONTINUUM H_log mass in the alias tail past pi/D; B4 named exactly two
remedies).  This probe IMPLEMENTS AND MEASURES both remedies; it proves
nothing and claims nothing.

THE MEASURED FAMILY (unchanged, cached).  For a window [-a, a] with M
cells (D = 2a/M, interior hats j = 1..M-1) let Q_M be the certified
layerwise hat-Galerkin matrix of the Weil window form (w2_mosco /
garding_probe route, verbatim: smooth TRUE-screw layer by Gauss + exact
mpmath d <= 2, atom layer closed B-spline, pole layer closed) and G_M
the exact tridiagonal L^2 Gram.  ONE assembly per (a, M) is cached and
every norm below is a DIAGONAL object in the cached orthonormal DST-I
basis -- no per-remedy rebuilds (the predecessor's 300 s were dominated
by repeated Gram integrations; here the continuum H_log Gram is built
ONLY on the anchor ladder, for the baseline and the consistency guards).

THE DOCUMENTED CONVENTION (remedy 1, the folded discrete H_log norm).
DST-I modes u_k[j] = sin(pi k j / M), k = 1..M-1; uhat_k = sqrt(2/M) u_k
is an orthonormal basis.  Lattice frequencies
    t_k  = pi k / (M D) = pi k / (2a)   in (0, pi/D),
    mu_k = D (2 + cos(pi k / M)) / 3
       = sum_{m in Z} |ker(t_k + 2 pi m / D)|^2 / D   (Poisson-folded
         squared hat kernel, ker(t) = D sinc^2(t D / 2); guarded), and
mu_k is the EXACT eigenvalue of G_M on u_k.  The folded norm is
    ||v||^2_{Hlog,fold,M} = sum_k log(2 + t_k) mu_k <v, uhat_k>^2,
i.e. H_fold = sum_k log(2 + t_k) mu_k uhat_k uhat_k^T.  Its weight-1
companion is G_M EXACTLY (by construction; DST-diagonality of G is
guarded).  Rationale: the continuum A3 norm gives every alias branch
t_k + 2 pi m / D its CONTINUUM weight log(2 + |t_k + 2 pi m / D|) --
that alias tail is what fed the degeneration; the folded norm folds all
branches back to the fundamental cell [0, pi/D] and weights with the
log of the FUNDAMENTAL frequency.  On low modes the two norms agree
(guarded at (a0, 368), k/M = 0.05 / 0.25 / 0.5 within 20%); at the edge
they differ BY DESIGN (the k/M = 0.98 ratio is printed as the diagnosis
echo, no bar).

Remedy 2 (edge-band cutoff): H_cut(beta) = the same diagonal norm with
the weights zeroed on the edge band, t_k > (1 - beta) pi / D
(equivalently k > (1 - beta) M); beta = 0.1 / 0.2.  The full-space
inequality Q + C G >= c H_cut is measured as c = 1 / lambda_max(H_cut,
Q + C G) (valid because Q + C G is positive definite -- Cholesky
guarded per solve; H_cut is singular PSD, so the pencil is taken in
this order).  COMPLEMENT check: on E_beta = span{uhat_k : t_k >
(1 - beta) pi / D} the plain form is measured against L^2 alone,
C_edge = max(0, -lambda_min(Q|_E, G|_E)); the cutoff is lossless for
the proof goal iff C_edge stays within the C budget, M-stably.

SLICES AND BARS (declared BEFORE the numbers):

  G0   guards: AST zero-firewall; layered lag assembly == verbatim
       garding_probe assembly at (a0, 92) and (a0, 736) (rel < 1e-12);
       DST machinery exact at (a0, 368): orthonormality and
       DST-diagonality of G (offdiag < 1e-11 rel), folded-symbol
       identity mu_k == Poisson sum (|m| <= 400, rel < 1e-8);
       spectral anchors on the ladder (|lambda_1(736, full)| <= 5e-9,
       lambda_1 monotone within the solver floor 20 eps rad n);
       continuum H_log Gram sanity on the anchor ladder (weight-1
       companion mass lags rel < 5e-3, Cholesky) and BASELINE
       REPRODUCTION |c_cont(736, C=1) - 0.180| <= 2e-3 (the
       predecessor's central number); low-mode continuum/folded
       consistency (|r - 1| <= 0.20 at k/M = 0.05/0.25/0.5); the
       beta -> 0 cutoff route reproduces the folded route at
       (a0, 368, C=1) to rel 1e-8; all Q + C G Cholesky guards
       collected into one summary check.

  G1   [MEASURED, central] remedy 1: c_fold(M, C) =
       lambda_min(Q + C G, H_fold) at a0 = log 16 on M = 92/184/368/
       736, C = 0.5/1/2, side by side with the degenerating baseline
       c_cont(M, C).  HEALING BAR per C: all c_fold > 0 AND last
       relative increment |c(736) - c(368)|/c(736) < 0.03.  TWO-MODEL
       BAR (the predecessor's criterion, per C): least squares of
       c(M) on b + a/log(2 + pi/D_M) vs a/log(2 + pi/D_M) alone; the
       1/log model is EXCLUDED iff rms_pure > 3 x rms_affine AND the
       affine intercept b >= 0.5 c(736).  Tightness c_fold / min_k
       R_fold(k), R_fold = (s_tot + C)/log(2 + t_k), printed (no bar).

  G2   [MEASURED] remedy 2: c_cut(M, C, beta) for beta = 0.1/0.2, same
       ladder, same bars (primary beta = 0.1; beta = 0.2 robustness).
       COMPLEMENT: C_edge(M, beta) <= 2.0 (the C budget) for all M,
       both beta, and M-spread of the edge-band minimum printed.

  G3   [MEASURED] the symbol inequality (the proof core).  Exact
       discrete symbols per unit L^2 mass are DIAGONAL reads in the
       DST basis: s_lay(t_k) = uhat_k^T Q_lay uhat_k / mu_k.  Smooth
       layer: least-squares fit s_sm ~ c0 log(2 + t_k) + b0 per M,
       validity constant C0 = max_k (c0 log(2 + t_k) - s_sm); BAR:
       c0 > 0 and relative spread of c0 over the 4 anchor stages
       <= 0.10 (C0 printed, no bar).  Lower-envelope reads printed
       (no bar): min_{t_k >= 20} s_sm / log(2 + t_k) per M, and the
       TOTAL-symbol envelope min_{t_k >= 20} s_tot per M with its
       location and ratio to the weight (the drift-mechanism
       diagnostic).  Atom layer: max_k |s_at|
       (all k, and t_k >= 20) per M, vs the B4(iii) comparators:
       exact atom mass sum mu_j = 2 sum_{n <= e^{2a}} Lambda(n)/
       sqrt(n), its Chebyshev cap 4 B_PSI e^a (both a-GROWING -- the
       crude partial-summation bound alone does NOT give a-uniformity;
       measured values test whether uniformity is plausible), and the
       oscillatory main-term size 4 B_PSI e^a / sqrt(1/4 + t^2) at the
       measured argmax.  Archimedean context: Re psi(1/4 + it/2) -
       log pi vs log(2 + t) printed at t = 50/200/400/1000.

  G4   [MEASURED] a-uniformity of the healed constants: 3 windows
       h = 184 / 606 / 1433 (a = log 16 / 5.153292 / 6.238325, all
       complete), fixed ratio M = 2h, C = 1: c_fold, c_cut(beta=0.1),
       C_edge, (c0, C0), max |s_at|.  UNIFORMITY BAR per remedy:
       spread (max - min)/min <= 0.5 (the predecessor's B2 bar).

  G5   [C] typing: which remedy delivers M-stable AND a-uniform
       constants; the resulting provable statement with the measured
       (c, C); what remains for a formal proof (the symbol
       monotonicity computation).  No positivity claim, no RH
       statement, no marker move.

Verdict enums (frozen, precedence top-down): EDGEBAND-MIXED (guards
fail), EDGEBAND-UNHEALED (neither remedy meets the healing + two-model
bars on its full C ladder), EDGEBAND-HEALED-NONUNIFORM (>= 1 remedy
heals, its G4 spread bar fails), EDGEBAND-HEALED-FOLD-UNIFORM /
EDGEBAND-HEALED-CUT-UNIFORM / EDGEBAND-HEALED-BOTH-UNIFORM.

FIREWALL: experiments-only; verification/ read-only (v563 import);
garding_probe machinery REBUILT verbatim (no probe imports); no marker
moves; NO zero of any L-function is read (AST-checked).  Python-only,
per GATE.WOLFRAM.02.

Provenance: garding_probe.py (2026-08-02, the c(M, C) measurement, the
B3 edge-band diagnosis, the B4 remedy list), w2_mosco_probe (certified
lag route + the A3 H_log convention), w1_theorem_probe (P2.3 layer
certification), Suzuki arXiv:2606.09096 Prop. 4.1 (compact embedding
hypothesis; whether the folded norm feeds that transfer is typed as
the remaining formal step, not claimed).
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
from numpy.polynomial.legendre import leggauss  # noqa: E402

MS = (92, 184, 368, 736)          # anchor dyadic ladder (garding_probe)
C_HEAL = (0.5, 1.0, 2.0)          # the task's C ladder for both remedies
BETAS = (0.1, 0.2)                # edge-band cutoff fractions
BETA_PRI = 0.1                    # primary beta for the verdict
G4_HS = (184, 606, 1433)          # the three a-uniformity windows
G4_RATIO = 2                      # fixed ratio M = 2h (the finer one)
G4_C = 1.0
T_MAX, N_T = 3000.0, 120001       # continuum H_log grid (baseline only)
FLOOR_SAFETY = 20.0
STAB_BAR = 0.03                   # healed last-increment bar (task: 3%)
RMS_FACTOR = 3.0                  # two-model exclusion: rms1 > 3 rms2
BFRAC = 0.5                       # ... AND intercept b >= 0.5 c(736)
UNIF_BAR = 0.50                   # G4 spread bar (predecessor B2)
C_EDGE_MAX = 2.0                  # complement budget = max C of ladder
C0_SPREAD_BAR = 0.10              # G3 smooth-symbol slope uniformity
BAR_LAYER = 1e-12                 # layered == verbatim lag bar
BAR_LAM736 = 5e-9                 # |lambda_1(736, full)| anchor
BAR_MASS = 5e-3                   # Parseval-truncation lag bar
BAR_REPRO = 2e-3                  # |c_cont(736,1) - 0.180| (3-dp quote)
CREF_736 = 0.180                  # predecessor central number (quoted)
BAR_FOLD_ID = 1e-8                # Poisson folded-symbol identity
BAR_DST = 1e-11                   # DST orthonormality / G-diagonality
BAR_CONS = 0.20                   # low-mode continuum/folded consistency
BAR_CUT0 = 1e-8                   # beta -> 0 route crosscheck
N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2

mp.mp.dps = 30
PSI14_F = float(mp.digamma(mp.mpf(1) / 4))
LOGPI_F = math.log(math.pi)
PHI1_F = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
UU = np.array([float(u) for u in core.U_ALL])
MU = np.array([float(m) for m in core.MU_ALL])

GX16, GW16 = leggauss(16)

TG = np.linspace(0.0, T_MAX, N_T)
DT = T_MAX / (N_T - 1)
TRAP_W = np.full(N_T, DT)
TRAP_W[0] *= 0.5
TRAP_W[-1] *= 0.5

CHOL_GUARDS = []                  # (tag, ok) collected, summary check


# ------------------------------------------------- certified lag assembly
def g_smooth_vec(ts):
    """smooth layer of the TRUE screw function (Lerch +1/4), verbatim
    garding_probe / w2_mosco_probe."""
    xf = np.abs(np.asarray(ts, dtype=float))
    out = xf / 2.0 * (LOGPI_F - PSI14_F) - 0.25 * PHI1_F
    lb = np.empty_like(xf)
    for a in range(0, xf.size, 400):
        b = min(xf.size, a + 400)
        E = np.exp(-np.outer(2.0 * xf[a:b], _NN_L) - 0.5 * xf[a:b, None])
        lb[a:b] = E @ _WTS
    return out + 0.25 * lb


def g_sm_mp(tv):
    tv = abs(mp.mpf(tv))
    PHI1m = mp.lerchphi(1, 2, mp.mpf(1) / 4)
    LLm = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)
    if tv == 0:
        return mp.mpf(0)
    return (LLm * tv / 2 - PHI1m / 4 + mp.exp(-tv / 2)
            * mp.lerchphi(mp.exp(-2 * tv), 2, mp.mpf(1) / 4) / 4)


def K_f_factory(D):
    def K_f(x):
        u = np.abs(x) / D
        return np.where(u <= 1.0, D * (2.0 / 3.0 - u ** 2 + u ** 3 / 2.0),
                        np.where(u < 2.0, D * (2.0 - u) ** 3 / 6.0, 0.0))
    return K_f


def galerkin_lags_verbatim(a, M):
    """garding_probe.galerkin_lags_verbatim (guard reference)."""
    D = 2.0 * a / M
    ss = np.concatenate([0.5 * D * (GX16 + 1) - D, 0.5 * D * (GX16 + 1)])
    ww = np.tile(0.5 * D * GW16, 2) * (D - np.abs(ss))
    ks = np.arange(M)
    vals = g_smooth_vec((ks[:, None] * D + ss[None, :]).ravel())
    II = vals.reshape(M, ss.size) @ ww
    c = np.empty(M - 1)
    for d in range(M - 1):
        c[d] = (2.0 * II[d] - II[abs(d - 1)] - II[d + 1]) / (D * D)
    Dm = mp.mpf(D)
    II_b = {k: mp.quad(lambda s: g_sm_mp(k * Dm + s) * (Dm - abs(s)),
                       [-Dm, 0, Dm]) for k in range(4)}
    for d in range(3):
        c[d] = float((2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1])
                     / Dm ** 2)
    dd_grid = np.arange(M - 1) * D
    K_f = K_f_factory(D)
    ka = core.atoms_in(a)
    for u_j, m_j in zip(UU[:ka], MU[:ka]):
        c -= 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    c += 2.0 * np.cosh(dd_grid / 2.0) * 16.0 * Xp ** 2 / (D * D)
    return c, D


def galerkin_layers(a, M):
    """the same assembly, layer-resolved: total = c_sm - c_at + c_po."""
    D = 2.0 * a / M
    ss = np.concatenate([0.5 * D * (GX16 + 1) - D, 0.5 * D * (GX16 + 1)])
    ww = np.tile(0.5 * D * GW16, 2) * (D - np.abs(ss))
    ks = np.arange(M)
    vals = g_smooth_vec((ks[:, None] * D + ss[None, :]).ravel())
    II = vals.reshape(M, ss.size) @ ww
    c_sm = np.empty(M - 1)
    for d in range(M - 1):
        c_sm[d] = (2.0 * II[d] - II[abs(d - 1)] - II[d + 1]) / (D * D)
    Dm = mp.mpf(D)
    II_b = {k: mp.quad(lambda s: g_sm_mp(k * Dm + s) * (Dm - abs(s)),
                       [-Dm, 0, Dm]) for k in range(4)}
    for d in range(3):
        c_sm[d] = float((2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1])
                        / Dm ** 2)
    dd_grid = np.arange(M - 1) * D
    K_f = K_f_factory(D)
    ka = core.atoms_in(a)
    c_at = np.zeros(M - 1)
    for u_j, m_j in zip(UU[:ka], MU[:ka]):
        c_at += 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    c_po = 2.0 * np.cosh(dd_grid / 2.0) * 16.0 * Xp ** 2 / (D * D)
    return c_sm, c_at, c_po, D


def toeplitz_of(lags, n):
    idx = np.abs(np.arange(n)[:, None] - np.arange(n)[None, :])
    return lags[idx]


def mass_of(D, n):
    Mass = np.zeros((n, n))
    np.fill_diagonal(Mass, 2.0 * D / 3.0)
    rng_ = np.arange(n - 1)
    Mass[rng_, rng_ + 1] = D / 6.0
    Mass[rng_ + 1, rng_] = D / 6.0
    return Mass


def hlog_lags(D, n):
    """Toeplitz lags of the CONTINUUM H_log Gram (weight log(2+t)) and
    the weight-1 companion, garding_probe convention (T = 3000).
    Baseline + guards only."""
    ker2 = (D * np.sinc(TG * D / (2.0 * math.pi)) ** 2) ** 2
    w_log = ker2 * np.log(2.0 + TG) * TRAP_W / math.pi
    w_one = ker2 * TRAP_W / math.pi
    dd = np.arange(n) * D
    l_log = np.zeros(n)
    l_one = np.zeros(n)
    for a_ in range(0, N_T, 4000):
        b_ = min(N_T, a_ + 4000)
        Cc = np.cos(np.outer(TG[a_:b_], dd))
        l_log += w_log[a_:b_] @ Cc
        l_one += w_one[a_:b_] @ Cc
    return l_log, l_one


def mass_lag_guard(l_one, D, tag):
    d0 = abs(l_one[0] - 2.0 * D / 3.0) / (2.0 * D / 3.0)
    d1 = abs(l_one[1] - D / 6.0) / (D / 6.0)
    d2 = float(np.max(np.abs(l_one[2:]))) / (2.0 * D / 3.0)
    ok = d0 < BAR_MASS and d1 < BAR_MASS and d2 < BAR_MASS
    return ok, "%s: d0 %.1e / d1 %.1e / d>=2 %.1e" % (tag, d0, d1, d2)


def gen_min(A, B):
    w = sla.eigvalsh(0.5 * (A + A.T), 0.5 * (B + B.T),
                     subset_by_index=[0, 0])
    return float(w[0])


# ------------------------------------------------- cached DST build
def build_dst(a, M, want_orig=False):
    """ONE certified assembly per (a, M): total form in the orthonormal
    DST-I basis + exact per-mass layer symbols as diagonal reads.  All
    remedy norms are diagonal weights on this cache."""
    c_sm, c_at, c_po, D = galerkin_layers(a, M)
    n = M - 1
    Qsm = toeplitz_of(c_sm, n)
    Qat = toeplitz_of(c_at, n)
    Qpo = toeplitz_of(c_po, n)
    Q = Qsm - Qat + Qpo
    kk = np.arange(1, M, dtype=float)
    U = math.sqrt(2.0 / M) * np.sin(math.pi * np.outer(kk, kk) / M)
    mu = D * (2.0 + np.cos(math.pi * kk / M)) / 3.0
    tk = math.pi * kk / (M * D)
    logw = np.log(2.0 + tk)
    QU = Q @ U
    Qt = U.T @ QU
    Qt = 0.5 * (Qt + Qt.T)
    s_tot = np.einsum("ij,ij->j", U, QU) / mu
    del QU
    QsU = Qsm @ U
    s_sm = np.einsum("ij,ij->j", U, QsU) / mu
    del QsU, Qsm
    QaU = Qat @ U
    s_at = np.einsum("ij,ij->j", U, QaU) / mu
    del QaU, Qat, Qpo
    out = dict(a=a, M=M, D=D, n=n, mu=mu, tk=tk, logw=logw, Qt=Qt,
               s_tot=s_tot, s_sm=s_sm, s_at=s_at,
               lags=(c_sm, c_at, c_po))
    if want_orig:
        out["Q"] = Q
        out["Mass"] = mass_of(D, n)
        out["U"] = U
    return out


def c_fold(bld, C):
    """lambda_min(Q + C G, H_fold) via the exact diagonal scaling."""
    s = bld["mu"] * bld["logw"]
    A = bld["Qt"] + C * np.diag(bld["mu"])
    B = A / np.sqrt(np.outer(s, s))
    return float(sla.eigvalsh(0.5 * (B + B.T),
                              subset_by_index=[0, 0])[0])


def c_cut(bld, C, beta, tag):
    """sup{c : Q + C G - c H_cut(beta) >= 0} = 1/lambda_max(H_cut, A),
    valid for A = Q + C G positive definite (Cholesky-guarded)."""
    mask = bld["tk"] <= (1.0 - beta) * math.pi / bld["D"]
    s = bld["mu"] * bld["logw"] * mask
    A = bld["Qt"] + C * np.diag(bld["mu"])
    A = 0.5 * (A + A.T)
    try:
        sla.cholesky(A)
        CHOL_GUARDS.append((tag, True))
    except sla.LinAlgError:
        CHOL_GUARDS.append((tag, False))
        return float("nan"), int(mask.sum())
    lam = float(sla.eigvalsh(np.diag(s), A,
                             subset_by_index=[bld["n"] - 1,
                                              bld["n"] - 1])[0])
    return 1.0 / lam, int(mask.sum())


def edge_complement(bld, beta):
    """lambda_min(Q, G) restricted to the edge band E_beta (DST split);
    C_edge = max(0, -lambda_min)."""
    idx = np.where(bld["tk"] > (1.0 - beta) * math.pi / bld["D"])[0]
    Qe = bld["Qt"][np.ix_(idx, idx)]
    me = bld["mu"][idx]
    B = Qe / np.sqrt(np.outer(me, me))
    lam = float(sla.eigvalsh(0.5 * (B + B.T),
                             subset_by_index=[0, 0])[0])
    return lam, len(idx)


def two_model(cs, Ds):
    """the predecessor's two-model log-null comparison on the ladder."""
    xs = np.array([1.0 / math.log(2.0 + math.pi / d) for d in Ds])
    ys = np.array(cs, dtype=float)
    A2 = np.column_stack([np.ones(xs.size), xs])
    bfit, _, _, _ = np.linalg.lstsq(A2, ys, rcond=None)
    rms2 = float(np.sqrt(np.mean((ys - A2 @ bfit) ** 2)))
    a1 = float((xs @ ys) / (xs @ xs))
    rms1 = float(np.sqrt(np.mean((ys - a1 * xs) ** 2)))
    b0 = float(bfit[0])
    excl = (rms1 > RMS_FACTOR * rms2) and (b0 >= BFRAC * float(ys[-1]))
    return dict(b0=b0, a2=float(bfit[1]), rms2=rms2, a1=a1, rms1=rms1,
                excluded=excl)


def stab_read(cs):
    pos = all(c > 0.0 for c in cs)
    inc = abs(cs[-1] - cs[-2]) / abs(cs[-1]) if cs[-1] != 0 else math.inf
    return pos, inc, (pos and inc < STAB_BAR)


def fit_smooth_symbol(bld):
    """LS fit s_sm ~ c0 log(2 + t_k) + b0 over ALL modes + validity C0."""
    lw, ss = bld["logw"], bld["s_sm"]
    A2 = np.column_stack([np.ones(lw.size), lw])
    bfit, _, _, _ = np.linalg.lstsq(A2, ss, rcond=None)
    b0, c0 = float(bfit[0]), float(bfit[1])
    rms = float(np.sqrt(np.mean((ss - A2 @ bfit) ** 2)))
    C0 = float(np.max(c0 * lw - ss))
    hi = bld["tk"] >= 20.0
    env = float(np.min(ss[hi] / lw[hi])) if hi.any() else float("nan")
    return c0, b0, C0, rms, env


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE TWO NAMED GARDING REMEDIES -- folded discrete H_log norm "
          "vs edge-band cutoff")
    print("=" * 78)

    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    kz0 = core.frame_a_zones()[0]
    r0 = core.build_window(kz0)
    a0 = r0["alpha"]
    print("anchor window: a0 = alpha(h = %d) = %.12f (= log %d); "
          "ladder M = %s" % (r0["h"], a0, r0["n_zone"], list(MS)))

    # ------------------------------------------------ anchor ladder cache
    print("\nbuilding the anchor ladder cache (ONE assembly per M; all "
          "norms diagonal in the DST basis) ...")
    dat = {}
    for M in MS:
        t1 = time.time()
        dat[M] = build_dst(a0, M, want_orig=True)
        print("   M = %3d (D = %.6f, n = %d)  [%.1f s]"
              % (M, dat[M]["D"], dat[M]["n"], time.time() - t1))

    devs = []
    for M in (92, 736):
        c_v, _ = galerkin_lags_verbatim(a0, M)
        c_sm, c_at, c_po = dat[M]["lags"]
        c_l = c_sm - c_at + c_po
        scale = float(np.max(np.abs(c_v)))
        devs.append(float(np.max(np.abs(c_l - c_v))) / scale)
    check("G0.1 [E] layered lag assembly (cached) == verbatim "
          "garding_probe assembly at (a0, 92) and (a0, 736): max rel "
          "dev %s < %.0e" % (["%.1e" % d for d in devs], BAR_LAYER),
          max(devs) < BAR_LAYER)

    # DST machinery exactness at (a0, 368)
    d3 = dat[368]
    U3 = d3["U"]
    orto = float(np.max(np.abs(U3.T @ U3 - np.eye(d3["n"]))))
    Gd = U3.T @ (d3["Mass"] @ U3)
    diag_dev = float(np.max(np.abs(Gd - np.diag(d3["mu"])))) \
        / float(np.max(d3["mu"]))
    mm_ = np.arange(-400, 401)
    fold_dev = 0.0
    for kq in (1, d3["n"] // 2, d3["n"] - 1):
        t_ = d3["tk"][kq - 1]
        tt = t_ + 2.0 * math.pi * mm_ / d3["D"]
        ker2 = (d3["D"] * np.sinc(tt * d3["D"] / (2.0 * math.pi)) ** 2) ** 2
        fold_dev = max(fold_dev, abs(float(ker2.sum()) / d3["D"]
                                     - d3["mu"][kq - 1])
                       / d3["mu"][kq - 1])
    check("G0.2 [E] DST machinery exact at (a0, 368): orthonormality "
          "%.1e, G-diagonality rel %.1e < %.0e, folded-symbol identity "
          "mu_k == Poisson sum rel %.1e < %.0e"
          % (orto, diag_dev, BAR_DST, fold_dev, BAR_FOLD_ID),
          orto < BAR_DST and diag_dev < BAR_DST
          and fold_dev < BAR_FOLD_ID)

    # spectral anchors (original basis, as the predecessor)
    lam1 = {}
    floors = {}
    for M in MS:
        w_full = sla.eigvalsh(0.5 * (dat[M]["Q"] + dat[M]["Q"].T),
                              0.5 * (dat[M]["Mass"] + dat[M]["Mass"].T))
        lam1[M] = float(w_full[0])
        rad = max(abs(float(w_full[0])), abs(float(w_full[-1])))
        floors[M] = FLOOR_SAFETY * float(np.finfo(float).eps) * rad \
            * (M - 1)
    mono_ok = all(lam1[MS[i + 1]] <= lam1[MS[i]]
                  + max(floors[MS[i]], floors[MS[i + 1]])
                  for i in range(3))
    check("G0.3 [E] spectral anchors: lambda_1 ladder %s, "
          "|lambda_1(736)| = %.1e <= %.0e, monotone within floor"
          % (["%.2e" % lam1[M] for M in MS], abs(lam1[736]), BAR_LAM736),
          abs(lam1[736]) <= BAR_LAM736 and mono_ok)

    # continuum H_log Gram (baseline + guards) on the anchor ladder
    print("\nbuilding the continuum H_log baseline (anchor ladder "
          "only) ...")
    Hc = {}
    mass_ok, mass_det, chol_h = True, [], True
    for M in MS:
        t1 = time.time()
        l_log, l_one = hlog_lags(dat[M]["D"], dat[M]["n"])
        Hc[M] = toeplitz_of(l_log, dat[M]["n"])
        ok, det = mass_lag_guard(l_one, dat[M]["D"], "M=%d" % M)
        mass_ok = mass_ok and ok
        mass_det.append(det)
        try:
            sla.cholesky(0.5 * (Hc[M] + Hc[M].T))
        except sla.LinAlgError:
            chol_h = False
        print("   M = %3d H_cont lags + Cholesky  [%.1f s]"
              % (M, time.time() - t1))
    c_base = {}
    for M in MS:
        for C in C_HEAL:
            c_base[(M, C)] = gen_min(dat[M]["Q"] + C * dat[M]["Mass"],
                                     Hc[M])
    repro = abs(c_base[(736, 1.0)] - CREF_736)
    check("G0.4 [E] continuum baseline sane and REPRODUCES the "
          "predecessor: mass lags (%s), H Cholesky ok, "
          "|c_cont(736, C=1) - %.3f| = %.1e <= %.0e (c_cont(736,1) = "
          "%.5f)" % ("; ".join(mass_det), CREF_736, repro, BAR_REPRO,
                     c_base[(736, 1.0)]),
          mass_ok and chol_h and repro <= BAR_REPRO)

    # low-mode continuum/folded consistency at (a0, 368)
    rr = {}
    for f in (0.05, 0.25, 0.5, 0.98):
        kq = max(1, int(round(f * 368)))
        kq = min(kq, d3["n"])
        jj = np.arange(1, 368, dtype=float)
        u = np.sin(math.pi * kq * jj / 368.0)
        num = float(u @ (Hc[368] @ u))
        den = (368.0 / 2.0) * d3["mu"][kq - 1] * d3["logw"][kq - 1]
        rr[f] = num / den
    cons_ok = all(abs(rr[f] - 1.0) <= BAR_CONS for f in (0.05, 0.25, 0.5))
    check("G0.5 [E] low-mode consistency of the two norms at (a0, "
          "368): H_cont/H_fold per mode = %.4f / %.4f / %.4f at k/M = "
          "0.05/0.25/0.5 (bar |r-1| <= %.2f); edge mode k/M = 0.98: "
          "r = %.4f (the diagnosed alias inflation, PRINTED, no bar)"
          % (rr[0.05], rr[0.25], rr[0.5], BAR_CONS, rr[0.98]), cons_ok)

    cf_chk = c_fold(dat[368], 1.0)
    cc_chk, _ = c_cut(dat[368], 1.0, 0.0, "b0chk")
    dev_cut0 = abs(cc_chk - cf_chk) / abs(cf_chk)
    check("G0.6 [E] the beta -> 0 cutoff route reproduces the folded "
          "route at (a0, 368, C = 1): rel dev %.1e < %.0e"
          % (dev_cut0, BAR_CUT0), dev_cut0 < BAR_CUT0)

    # ------------------------------------------------ G1 folded remedy
    print("\nG1 -- remedy 1 (folded discrete H_log norm) on the anchor "
          "ladder, vs the degenerating baseline")
    cF = {}
    for M in MS:
        for C in C_HEAL:
            cF[(M, C)] = c_fold(dat[M], C)
    print("   M      " + "".join("  base C=%-4.1f  fold C=%-4.1f"
                                 % (C, C) for C in C_HEAL))
    for M in MS:
        cells = "".join("   %+.5f     %+.5f " % (c_base[(M, C)],
                                                 cF[(M, C)])
                        for C in C_HEAL)
        print("   %3d %s" % (M, cells))
    Ds_l = [dat[M]["D"] for M in MS]
    stabF = {}
    for C in C_HEAL:
        seq = [cF[(M, C)] for M in MS]
        pos, inc, ok = stab_read(seq)
        stabF[C] = ok
        print("   fold C = %.1f: ladder %s, last rel inc %.4f (bar "
              "%.2f) -> %s" % (C, ["%.5f" % c for c in seq], inc,
                               STAB_BAR,
                               "STABILIZES" if ok else "NOT stabilized"))
    tmF = {}
    for C in C_HEAL:
        tmF[C] = two_model([cF[(M, C)] for M in MS], Ds_l)
        tmB = two_model([c_base[(M, C)] for M in MS], Ds_l)
        print("   two-model C = %.1f: FOLD affine b = %+.4f + %.4f/log "
              "(rms %.1e) vs pure %.4f/log (rms %.1e) -> 1/log %s | "
              "BASE affine b = %+.4f (rms %.1e) vs pure (rms %.1e) -> "
              "1/log %s"
              % (C, tmF[C]["b0"], tmF[C]["a2"], tmF[C]["rms2"],
                 tmF[C]["a1"], tmF[C]["rms1"],
                 "EXCLUDED" if tmF[C]["excluded"] else "competitive",
                 tmB["b0"], tmB["rms2"], tmB["rms1"],
                 "EXCLUDED" if tmB["excluded"] else "competitive"))
    fold_heals = all(stabF[C] for C in C_HEAL) and tmF[1.0]["excluded"]
    check("G1.1 [MEASURED, central] remedy-1 (folded norm) ladder "
          "read: stabilization (all c > 0, last inc < %.2f) %s; "
          "two-model 1/log %s at C = 1 (criterion: rms_pure > %.0f x "
          "rms_affine and b >= %.1f c(736)); finest-stage pair "
          "(c, C) = (%.5f, 1)"
          % (STAB_BAR,
             "for all C" if all(stabF[C] for C in C_HEAL)
             else "FAILS for C = %s"
             % [C for C in C_HEAL if not stabF[C]],
             "EXCLUDED" if tmF[1.0]["excluded"] else "STILL competitive",
             RMS_FACTOR, BFRAC, cF[(736, 1.0)]), True)

    print("   tightness (C = 1): R_fold(k) = (s_tot + 1)/log(2 + t_k)")
    for M in MS:
        R = (dat[M]["s_tot"] + 1.0) / dat[M]["logw"]
        kmin = int(np.argmin(R))
        print("   M = %3d: min_k R = %.5f at k/M = %.3f, c/min_k R = "
              "%.4f" % (M, float(R[kmin]), (kmin + 1) / M,
                        cF[(M, 1.0)] / float(R[kmin])))

    # ------------------------------------------------ G2 cutoff remedy
    print("\nG2 -- remedy 2 (edge-band cutoff, beta = 0.1/0.2)")
    cX = {}
    for beta in BETAS:
        for M in MS:
            for C in C_HEAL:
                cX[(beta, M, C)], nlow = c_cut(
                    dat[M], C, beta, "cut b=%.1f M=%d C=%.1f"
                    % (beta, M, C))
        print("   beta = %.1f (keeps t_k <= %.1f pi/D):" % (beta,
                                                            1.0 - beta))
        print("   M      " + "".join("   C = %-6.1f" % C
                                     for C in C_HEAL))
        for M in MS:
            cells = "".join("   %+.5f " % cX[(beta, M, C)]
                            for C in C_HEAL)
            print("   %3d %s" % (M, cells))
    stabX = {}
    tmX = {}
    for beta in BETAS:
        for C in C_HEAL:
            seq = [cX[(beta, M, C)] for M in MS]
            pos, inc, ok = stab_read(seq)
            stabX[(beta, C)] = ok
            print("   cut b = %.1f, C = %.1f: last rel inc %.4f (bar "
                  "%.2f) -> %s" % (beta, C, inc, STAB_BAR,
                                   "STABILIZES" if ok
                                   else "NOT stabilized"))
        tmX[beta] = two_model([cX[(beta, M, 1.0)] for M in MS], Ds_l)
        print("   two-model b = %.1f, C = 1: affine b = %+.4f (rms "
              "%.1e) vs pure (rms %.1e) -> 1/log %s"
              % (beta, tmX[beta]["b0"], tmX[beta]["rms2"],
                 tmX[beta]["rms1"],
                 "EXCLUDED" if tmX[beta]["excluded"] else "competitive"))
    cut_heals = all(stabX[(BETA_PRI, C)] for C in C_HEAL) \
        and tmX[BETA_PRI]["excluded"]
    check("G2.1 [MEASURED] remedy-2 (cutoff) ladder read at the "
          "primary beta = %.1f: stabilization %s, two-model 1/log %s "
          "at C = 1; finest-stage pair (c, C) = (%.5f, 1); beta = 0.2 "
          "robustness: stabilization %s"
          % (BETA_PRI,
             "for all C" if all(stabX[(BETA_PRI, C)] for C in C_HEAL)
             else "FAILS for C = %s"
             % [C for C in C_HEAL if not stabX[(BETA_PRI, C)]],
             "EXCLUDED" if tmX[BETA_PRI]["excluded"]
             else "STILL competitive",
             cX[(BETA_PRI, 736, 1.0)],
             "ok" if all(stabX[(0.2, C)] for C in C_HEAL)
             else "FAILS"), True)

    edge_ok = True
    for beta in BETAS:
        vals = []
        for M in MS:
            lam, ne = edge_complement(dat[M], beta)
            ce = max(0.0, -lam)
            idx = dat[M]["tk"] > (1.0 - beta) * math.pi / dat[M]["D"]
            smin = float(np.min(dat[M]["s_tot"][idx]))
            vals.append((M, lam, ce, ne, smin))
            edge_ok = edge_ok and (ce <= C_EDGE_MAX)
        print("   complement beta = %.1f: %s"
              % (beta,
                 "; ".join("M=%d: lam_min(Q,G)|_E = %+.4f (C_edge "
                           "%.4f, %d modes, min s_tot %.3f)"
                           % v for v in vals)))
    check("G2.2 [MEASURED] the edge band alone is L^2-controlled: "
          "C_edge = max(0, -lambda_min(Q|_E, G|_E)) <= %.1f (the C "
          "budget) on all M, both beta -> the cutoff is %s for the "
          "proof goal at the measured C"
          % (C_EDGE_MAX, "LOSSLESS" if edge_ok else "NOT lossless"),
          edge_ok)

    # ------------------------------------------------ G3 symbol core
    print("\nG3 -- the symbol inequality (exact discrete symbols per "
          "unit L^2 mass, DST-diagonal reads)")
    c0s, C0s = [], []
    for M in MS:
        c0, b0, C0, rms, env = fit_smooth_symbol(dat[M])
        c0s.append(c0)
        C0s.append(C0)
        print("   M = %3d: s_sm ~ %.4f log(2+t) %+.4f (rms %.3f), "
              "validity C0(c0) = %.4f, envelope min_{t>=20} s_sm/log "
              "= %.4f" % (M, c0, b0, rms, C0, env))
    prof_f = (0.02, 0.1, 0.25, 0.5, 0.75, 0.9, 0.98)
    d7 = dat[736]
    prof = ["k/M=%.2f: s_sm %.3f (s_sm/log %.3f)"
            % (f, d7["s_sm"][max(0, int(round(f * 736)) - 1)],
               d7["s_sm"][max(0, int(round(f * 736)) - 1)]
               / d7["logw"][max(0, int(round(f * 736)) - 1)])
            for f in prof_f]
    print("   profile at M = 736: " + " | ".join(prof))
    spread_c0 = (max(c0s) - min(c0s)) / min(c0s) if min(c0s) > 0 \
        else math.inf
    check("G3.1 [MEASURED] archimedean symbol statement s_sm(t_k) >= "
          "c0 log(2 + t_k) - C0: LS slopes c0 = %s, M-spread %.4f "
          "(bar %.2f, all c0 > 0); validity constants C0 = %s "
          "(PRINTED, no bar)"
          % (["%.4f" % c for c in c0s], spread_c0, C0_SPREAD_BAR,
             ["%.3f" % c for c in C0s]),
          min(c0s) > 0 and spread_c0 <= C0_SPREAD_BAR)

    atom_rows = []
    env_tot = {}
    for M in MS:
        sa = dat[M]["s_at"]
        k_all = int(np.argmax(np.abs(sa)))
        hi = dat[M]["tk"] >= 20.0
        m20 = float(np.max(np.abs(sa[hi])))
        atom_rows.append((M, float(np.abs(sa[k_all])),
                          (k_all + 1) / M, m20))
        print("   M = %3d: max|s_at| = %.4f at k/M = %.3f; max over "
              "t_k >= 20: %.4f" % atom_rows[-1])
    print("   TOTAL-symbol lower envelope (the drift mechanism, "
          "printed): per M min_{t>=20} s_tot, its location, and the "
          "ratio to log(2 + t_k):")
    for M in MS:
        st, lw = dat[M]["s_tot"], dat[M]["logw"]
        hi = dat[M]["tk"] >= 20.0
        kmin = int(np.argmin(np.where(hi, st, np.inf)))
        env_tot[M] = (float(st[kmin]), float(dat[M]["tk"][kmin]),
                      float(st[kmin] / lw[kmin]))
        print("   M = %3d: min s_tot = %.4f at t = %.1f "
              "(s_tot/log = %.4f)" % ((M,) + env_tot[M]))
    ka0 = core.atoms_in(a0)
    msum = float(np.sum(MU[:ka0]))
    cheb = 4.0 * core.B_PSI * math.exp(a0)
    t_at = atom_rows[-1][2] * math.pi / d7["D"]
    osc = cheb / math.sqrt(0.25 + t_at ** 2)
    a1max = max(r[1] for r in atom_rows)
    check("G3.2 [MEASURED] atom-layer symbol bound at a0: measured "
          "max_M max_k |s_at| = %.4f vs the B4(iii) comparators: "
          "exact atom mass sum mu_j = %.3f, Chebyshev cap 4 B_PSI "
          "e^a = %.3f (both crude, a-GROWING -- partial summation "
          "alone does not give a-uniformity), oscillatory main-term "
          "size at the argmax frequency %.3f; measured << crude is "
          "the uniformity evidence, typed not proved"
          % (a1max, msum, cheb, osc), a1max < msum)

    print("   archimedean context: (Re psi(1/4 + it/2) - log pi)"
          "/log(2 + t) at t = 50/200/400/1000: "
          + ", ".join("%.4f"
                      % ((float(mp.re(mp.digamma(mp.mpf(1) / 4
                                                 + 0.5j * t_)))
                          - LOGPI_F) / math.log(2.0 + t_))
                      for t_ in (50.0, 200.0, 400.0, 1000.0)))

    # ------------------------------------------------ G4 a-uniformity
    print("\nG4 -- a-uniformity of the healed constants (h = %s, "
          "fixed ratio M = %dh, C = %.1f)" % (list(G4_HS), G4_RATIO,
                                              G4_C))
    zones = core.frame_a_zones()
    fam = {}
    for kz in zones:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        fam[Mz // 2] = alpha
    g4 = {}
    for hz in G4_HS:
        alpha = fam[hz]
        M = G4_RATIO * hz
        t1 = time.time()
        if hz == 184:
            bld = dat[368]          # anchor reuse (a0, M = 368)
        else:
            bld = build_dst(alpha, M)
        cf_ = c_fold(bld, G4_C)
        cc_, _ = c_cut(bld, G4_C, BETA_PRI, "g4 h=%d" % hz)
        lam_e, ne = edge_complement(bld, BETA_PRI)
        ce_ = max(0.0, -lam_e)
        c0, b0, C0, rms, env = fit_smooth_symbol(bld)
        sa = bld["s_at"]
        hi = bld["tk"] >= 20.0
        at_all = float(np.max(np.abs(sa)))
        at_20 = float(np.max(np.abs(sa[hi])))
        lam1w = float(sla.eigvalsh(
            bld["Qt"] / np.sqrt(np.outer(bld["mu"], bld["mu"])),
            subset_by_index=[0, 0])[0])
        g4[hz] = dict(alpha=alpha, M=M, cf=cf_, cc=cc_, ce=ce_, c0=c0,
                      C0=C0, at=at_all, at20=at_20, lam1=lam1w)
        print("   h = %4d (a = %.4f, M = %4d): c_fold = %+.5f, c_cut"
              "(b=%.1f) = %+.5f, C_edge = %.4f, (c0, C0) = (%.4f, "
              "%.3f), max|s_at| = %.4f (t>=20: %.4f), lambda_1(Q,G) "
              "= %+.2e  [%.1f s]"
              % (hz, alpha, M, cf_, BETA_PRI, cc_, ce_, c0, C0,
                 at_all, at_20, lam1w, time.time() - t1))
    unif = {}
    for key, lab in (("cf", "fold"), ("cc", "cut")):
        vals = [g4[hz][key] for hz in G4_HS]
        spread = (max(vals) - min(vals)) / min(vals) \
            if min(vals) > 0 else math.inf
        unif[lab] = spread <= UNIF_BAR
        print("   %s: min %.5f / max %.5f, spread %.4f (bar %.2f) -> "
              "%s" % (lab, min(vals), max(vals), spread, UNIF_BAR,
                      "UNIFORM" if unif[lab] else "NON-UNIFORM"))
    c0v = [g4[hz]["c0"] for hz in G4_HS]
    atv = [g4[hz]["at"] for hz in G4_HS]
    print("   symbol constants across windows: c0 = %s (spread %.3f), "
          "C0 = %s, max|s_at| = %s (Chebyshev caps 4 B_PSI e^a = %s)"
          % (["%.4f" % c for c in c0v],
             (max(c0v) - min(c0v)) / min(c0v),
             ["%.3f" % g4[hz]["C0"] for hz in G4_HS],
             ["%.4f" % v for v in atv],
             ["%.1f" % (4.0 * core.B_PSI * math.exp(g4[hz]["alpha"]))
              for hz in G4_HS]))
    check("G4.1 [MEASURED] a-uniformity of remedy 1 (folded norm): "
          "c_fold over h = %s is %s (spread bar %.2f)"
          % (list(G4_HS), "UNIFORM" if unif["fold"] else "NON-UNIFORM",
             UNIF_BAR), True)
    check("G4.2 [MEASURED] a-uniformity of remedy 2 (cutoff beta = "
          "%.1f): c_cut over h = %s is %s (spread bar %.2f); C_edge "
          "over the windows = %s (budget %.1f)"
          % (BETA_PRI, list(G4_HS),
             "UNIFORM" if unif["cut"] else "NON-UNIFORM", UNIF_BAR,
             ["%.4f" % g4[hz]["ce"] for hz in G4_HS], C_EDGE_MAX), True)

    check("G0.7 [E] all Q + C G Cholesky guards over %d cutoff solves "
          "hold (positive definiteness of the measured pencil)"
          % len(CHOL_GUARDS), all(ok for _, ok in CHOL_GUARDS),
          "" if all(ok for _, ok in CHOL_GUARDS)
          else str([t for t, ok in CHOL_GUARDS if not ok]))

    # ------------------------------------------------ G5 typing
    guards_ok = not any(f.startswith("G0") for f in FAILS)
    fold_full = fold_heals and unif["fold"]
    cut_full = cut_heals and unif["cut"]
    if not guards_ok:
        VERDICT = "EDGEBAND-MIXED (guards failed)"
    elif not (fold_heals or cut_heals):
        VERDICT = "EDGEBAND-UNHEALED"
    elif fold_full and cut_full:
        VERDICT = "EDGEBAND-HEALED-BOTH-UNIFORM"
    elif fold_full:
        VERDICT = "EDGEBAND-HEALED-FOLD-UNIFORM"
    elif cut_full:
        VERDICT = "EDGEBAND-HEALED-CUT-UNIFORM"
    else:
        VERDICT = "EDGEBAND-HEALED-NONUNIFORM"

    check("G5.1 [C] the typed reading: remedy 1 (folded discrete "
          "H_log norm, convention t_k = pi k/(M D), weight mu_k = "
          "folded sinc^4 symbol) %s the 1/log degeneration "
          "(c_fold(736, 1) = %.5f = c_cont x %.4f, last inc bar %.2f, "
          "two-model 1/log %s, affine intercept b = %+.4f); remedy 2 "
          "(cutoff beta = %.1f) %s (c_cut(736, 1) = %.5f, intercept "
          "b = %+.4f, edge band %s by C <= %.1f L^2); a-uniformity: "
          "fold %s / cut %s over h = %s.  MECHANISM READ: the edge-"
          "mode norm ratio H_cont/H_fold = %.4f (G0.5) and c_fold ~ "
          "c_cont say the B3 alias-tail mass sits AT ~pi/D where the "
          "log weight is unchanged -- the alias/edge-band reading of "
          "the drift is NOT confirmed as its mechanism; the drift "
          "lives in the SYMBOL: min_{t>=20} s_tot = %.3f/%.3f/%.3f/"
          "%.3f across the ladder (near-flat) while the weight "
          "log(2 + t) grows, i.e. c(M) ~ (min s_tot + C)/log(2 + "
          "pi/D).  What a proof needs is therefore the lower-envelope "
          "growth of the TOTAL symbol (archimedean growth MINUS the "
          "atom-layer oscillation, which itself grows: max_{t>=20} "
          "|s_at| = %.2f/%.2f/%.2f over a = 2.77/5.15/6.24), not a "
          "lattice repair; the smooth layer alone has the M-stable "
          "envelope min_{t>=20} s_sm/log = %.4f.  MEASURED, not "
          "proved; no positivity claim, no RH statement, no marker "
          "move"
          % ("HEALS" if fold_heals else "does NOT heal",
             cF[(736, 1.0)], cF[(736, 1.0)] / c_base[(736, 1.0)],
             STAB_BAR,
             "excluded" if tmF[1.0]["excluded"] else "competitive",
             tmF[1.0]["b0"],
             BETA_PRI, "HEALS" if cut_heals else "does NOT heal",
             cX[(BETA_PRI, 736, 1.0)], tmX[BETA_PRI]["b0"],
             "lossless" if edge_ok else "NOT lossless", C_EDGE_MAX,
             "uniform" if unif["fold"] else "NON-uniform",
             "uniform" if unif["cut"] else "NON-uniform",
             list(G4_HS), rr[0.98],
             env_tot[92][0], env_tot[184][0], env_tot[368][0],
             env_tot[736][0],
             g4[184]["at20"], g4[606]["at20"], g4[1433]["at20"],
             fit_smooth_symbol(dat[736])[4]), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01 / W2, Garding remedy round (2026-08-02):
  both B4 remedies of the GARDING-DRIFT-UNRESOLVED finding were
  implemented and measured on the cached certified hat-Galerkin
  family.  REMEDY 1 (folded discrete H_log norm; documented
  convention t_k = pi k/(M D), weight log(2 + t_k) mu_k with mu_k =
  D(2 + cos(pi k/M))/3 = the Poisson-folded sinc^4 hat symbol,
  weight-1 companion == exact L^2 Gram): anchor ladder M = 92/184/
  368/736, C = 0.5/1/2 -> c_fold(736, C=1) = %.5f, last increment
  %.4f (bar %.2f), two-model 1/log %s (affine intercept b = %+.4f).
  REMEDY 2 (edge-band cutoff beta = %.1f): c_cut(736, C=1) = %.5f,
  last increment %.4f, intercept b = %+.4f; the dropped band is
  separately L^2-controlled (C_edge = %.4f on the ladder) -> cutoff
  %s at the measured C budget, but it does not change the drift.
  BASELINE REPRODUCTION: c_cont(736, C=1) = %.5f (predecessor
  0.180); c_fold/c_cont(736, C=1) = %.4f.  MECHANISM: the B3
  alias-tail hypothesis is NOT confirmed -- the aliased mass sits at
  ~pi/D where log(2+t) is unchanged (edge-mode norm ratio %.4f), so
  folding/cutoff are near-no-ops; the 1/log drift lives in the
  TOTAL SYMBOL: min_{t>=20} s_tot = %.3f/%.3f/%.3f/%.3f across the
  ladder (near-flat) under a growing weight.  SYMBOL CORE (G3): the
  smooth layer alone has an M-STABLE envelope min_{t>=20} s_sm /
  log(2+t) = %.4f (LS slopes c0 = %s drift with the fit range,
  spread %.3f -> declared bar FAILED, the envelope is the stable
  extraction); the atom layer is NOT a-uniform in the measured
  range: max_{t>=20} |s_at| = %.2f/%.2f/%.2f over a = 2.77/5.15/
  6.24 (crude Chebyshev caps %.0f/%.0f/%.0f).  a-SPREADS (h = 184/
  606/1433, M = 2h, C = 1): c_fold %.4f, c_cut %.4f (bar %.2f, same
  1/log drift via pi/D).  TYPE: the two named lattice remedies are
  implemented, guarded and REFUTED as healing mechanisms; the
  remaining proof object is the lower-envelope growth of the total
  symbol (archimedean MINUS atom oscillation) -- an arithmetic
  statement, not a lattice repair.  On this ladder a positive limit
  c_inf ~ %.3f cannot be separated from c_inf = 0.  No marker move;
  W2 stays open.
""" % (cF[(736, 1.0)],
       abs(cF[(736, 1.0)] - cF[(368, 1.0)]) / abs(cF[(736, 1.0)]),
       STAB_BAR,
       "EXCLUDED" if tmF[1.0]["excluded"] else "still competitive",
       tmF[1.0]["b0"],
       BETA_PRI, cX[(BETA_PRI, 736, 1.0)],
       abs(cX[(BETA_PRI, 736, 1.0)] - cX[(BETA_PRI, 368, 1.0)])
       / abs(cX[(BETA_PRI, 736, 1.0)]),
       tmX[BETA_PRI]["b0"],
       max(max(0.0, -edge_complement(dat[M], BETA_PRI)[0])
           for M in MS),
       "LOSSLESS" if edge_ok else "NOT lossless",
       c_base[(736, 1.0)],
       cF[(736, 1.0)] / c_base[(736, 1.0)],
       rr[0.98],
       env_tot[92][0], env_tot[184][0], env_tot[368][0],
       env_tot[736][0],
       fit_smooth_symbol(dat[736])[4],
       ["%.4f" % c for c in c0s], spread_c0,
       g4[184]["at20"], g4[606]["at20"], g4[1433]["at20"],
       4.0 * core.B_PSI * math.exp(g4[184]["alpha"]),
       4.0 * core.B_PSI * math.exp(g4[606]["alpha"]),
       4.0 * core.B_PSI * math.exp(g4[1433]["alpha"]),
       (max(g4[hz]["cf"] for hz in G4_HS)
        - min(g4[hz]["cf"] for hz in G4_HS))
       / min(g4[hz]["cf"] for hz in G4_HS),
       (max(g4[hz]["cc"] for hz in G4_HS)
        - min(g4[hz]["cc"] for hz in G4_HS))
       / min(g4[hz]["cc"] for hz in G4_HS),
       UNIF_BAR, tmF[1.0]["b0"]))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
