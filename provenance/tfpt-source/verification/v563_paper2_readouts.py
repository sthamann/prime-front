"""v563 -- PRIME.PAPER2.READOUT.01: the Paper-II readouts, recomputed.

THE CHECK CLOSURE OF THE CLASSIFICATION PAPER (Paper II,
parity_toeplitz_classification): every number that paper QUOTED from an
exploration probe without a recomputing module is recomputed here on the
identical declared surface, and the one mechanism it declared as a
caveat without exhibiting it (the rung-ladder shift of the binned
exponent) is exhibited as a STRUCTURE FACT.  Pure readout / identity
checks -- NO new claim, NO marker move, NO rate, NO uniformity:

[E] (1) THE REFERENCE WINDOW (meas:refwindow).  The declared T170
    frame-A scan (bilinear_sieve_probe.py, bit for bit: table cap 4e5,
    zone horizon 3.8e5, nu = 4, h in [128, 1450], mid element) lands on
    h = 540 with node cap X = 2.465e4 = 157^2, and the four quoted
    numbers are RECOMPUTED: det B = 6.18, -D(B,S) = -198.8, det S =
    192.6, sum = det Ahat = 4.22e-3 -- a 4.7-order cancellation between
    three pieces of size ~200, a further factor 383 above the absolute
    target ahat11 ahat22 h^-3 = 1.10e-5.  The split Ahat = B - S is
    verified against the direct t_i^T A_h t_j and the polarisation
    det Ahat = det B - D(B,S) + det S holds to round-off.  Mutations:
    the wrong polarisation cross-coefficient misses by 2.7e3 of det
    Ahat; the position scramble (uniform u at the SAME masses) moves
    |1 - r12^2| by 4e5 while every identity keeps holding.
[E] (2) THE l1-TO-SIGNED RATIO (meas:l1, eq:l1mass).  On the declared
    900-node subsample of the same window the l1 kernel mass is 40.6x
    the signed value (the price of any triangle-inequality route); the
    explicit double sum against K(n,m) = (1/2) D(X_n, X_m) equals det S
    to round-off (Cauchy-Binet), the rank-one defect of the reads is
    median 1.3e-4 and the kernel diagonal carries 5.9% of det S in
    magnitude ('about 6%', as quoted).  Mutation: the wrong kernel
    coefficient misses by 11x the signed value.
[E] (3) THE TIGHTNESS RANGE WHERE CHEAP (meas:sharpness).  On the cheap
    sub-range of the Surface-II family (22 windows h = 142..388,
    cond(B_LL) <= 1e12) the declared trial family (the v555 Fejer knob,
    51 sigma values, at the untapered optimiser) reproduces the QUOTED
    envelope mu^P_1 TV in [5.00, 23.20] with BOTH ENDS ATTAINED (min
    4.999 at the taper end, max 23.205 at the untapered optimiser of
    h = 203); the floor mu^P_1 TV >= 1 holds on all 1122 trial vectors.
    Mutation: the inadmissible vector lambda x* undercuts the floor by
    EXACTLY lambda^2 (degree-2 homogeneity to 1.9e-16).
[E] (4) LEM:DUALPOINT END TO END.  On the reference window the three
    reads S_11, S_22, S_12 are ASSEMBLED as values of ONE exponential
    sum of length X and its first log moment at the two dual points
    gamma_k = 2 pi k/(ND) -- gamma_1 = 0.6208, gamma_2 = 1.2415,
    1/Delta-gamma = 1.611, READ OFF eq:dualpoints and not fitted: the
    polarised weights lie in the 8-dim band space exactly (fit residual
    2e-13; the single-mode coefficients reproduce eq:closedweight in
    closed form), the band read equals the exponential-sum read to
    8e-16, the interpolation residual sits at 0.024 of its declared
    budget eta ||rho||_1 (lem:spline), and the Montgomery-Vaughan step
    of eq:mvread holds as used (fraction 6e-2 -- valid and far from
    sharp, which is meas:routes' point about R3).  The 19 tail atoms
    within one lag of the node cap are excluded exactly as the lemma's
    interior hypothesis demands.  Mutations: shifted dual points
    (x 1.01) and a dropped log moment miss loudly; on the polarised
    cross read W^(12) the moment coefficients VANISH IDENTICALLY (the
    linear-in-tau coefficients are proportional to a_k^2 and cancel in
    the polarisation -- lem:band), so the two points carry that read
    alone.
[E] (5) THE LADDER SHIFT IS ANCHOR SELECTION (rem:undecidable made a
    structure fact).  On the identical v562 surface (18 complete-comb
    anchors x the 2^(1/4) ladder, 108/108 PD) the declared bin gives
    +0.0245 (fine) vs -0.0110 (coarse sqrt(2) sub-ladder), the v562
    shift 0.0355 >= 1e-3 reproduced -- and DECOMPOSED: the two ladders
    select DIFFERENT anchor sets in the SAME bin (13 vs 12; the fine
    ladder's extra anchor is n = 157, because an anchor needs 3 in-bin
    rungs and the coarse ladder offers it fewer), the anchor part
    +0.0490 alone reproduces the whole shift, the rung part at FIXED
    anchor set is -0.0135 <= half the shift, and transporting every
    slope with the paper's MEASURED curvature a2 = -0.0842 moves the
    shift by only -0.0111: THE SHIFT LIVES IN WHICH ANCHORS ENTER THE
    BIN, NOT IN HOW THE RUNGS SAMPLE THE CURVATURE.  The ladder caveat
    stays (the number still depends on the declared ladder) -- but it
    is now an EXPLAINED selection effect, not an unexplained
    instability.  Mutation: a wrong curvature (a2 = +1) moves the
    fixed-anchor comparison 11.9x louder than the true transport.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   READOUTS, NOT CLAIMS: every number here is a recomputation of a
        quantity the paper types MEASURED on a declared finite surface;
        no bound, no rate, no uniformity in the window index is claimed,
        and the open problem R1 (prob:R1 / link 16) is untouched.
  (ii)  The tightness recomputation covers the CHEAP sub-range
        h <= 420 of the Surface-II family; the deep end (h up to 1445)
        stays covered by the quoted T163 envelope, which this module
        reproduces at both ends but does not re-measure in full.
  (iii) The anchor-selection decomposition is exhibited on the SMALL
        declared v562 surface (one bin, 18 anchors); T176's shifts up
        to 0.20 on the big surface stay sandbox MEASURED numbers, and
        the measured curvature a2 = -0.0842 is consumed only as the
        declared transport channel, never as a claim of this module.
HONEST FENCES: NO RH statement anywhere -- RH_DELTA = 0.5 is a yardstick
in exactly one role; the arithmetic input is a FINITE von Mangoldt table
below a declared cap (Chebyshev 1852 / Rosser-Schoenfeld 1962, verified
on the table); no zero of any L-function is read and no L-function is
evaluated (AST firewall); the Weil fence is hard (positivity of a finite
A_h is never routed through the Weil criterion; Weil 1952 cited, never
used); Montgomery-Vaughan 1974, Vaughan 1977, Kac-Murdock-Szego 1953,
Schur 1917, Fejer 1915, Lagrange 1773, Cauchy-Binet 1812/1815, Dirichlet
1829, Chebyshev 1852 named CLASSICAL.  Status: [E] per-instance readout
and identity checks with mutation controls; deterministic (fixed seeds,
no wall-clock dependence); Python-only, counted per GATE.WOLFRAM.02.
Discovery provenance:
  experiments/tfpt-discovery/bilinear_sieve_probe.py   (T170, 44/44)
  experiments/tfpt-discovery/sector_change_probe.py    (T163 surface)
  experiments/tfpt-discovery/dense_limit_probe.py      (T176, 24/24)
  verification/v562_dense_limit_identities.py          (the S5 surface)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
# the T170 probe surface (bilinear_sieve_probe.py), verbatim
ATOM_MAX = 400000            # the probe's atom-table cap
ZONE_DEEP = 380000           # the probe's zone horizon
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN, HCAP = 128, 1450      # the probe's frame-A window range
N_ATOM_MIN = 40              # atom floor per window
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
EPSM = float(np.finfo(float).eps)

# --- the Chebyshev input, preregistered (T162..T176) --------------------------
KAPPA_X0 = 100.0
KAPPA_REF = 0.038821
TOL_KAPPA = 1.0e-6
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962)

# --- yardsticks / quotes (never claims) ---------------------------------------
RH_DELTA = 0.5               # RH-equivalent strength, a YARDSTICK only
SEED = 563

# --- the Paper-II quotes being recomputed (meas:refwindow, meas:l1) -----------
Q_H_REF = 540                # the reference window
Q_X_REF = 2.465e4            # its node cap X = e^{2 alpha} = n_zone^2
Q_DET_B = 6.18               # det B                       (eq:refwindow)
Q_MIX = -198.8               # -D(B, S)                    (eq:refwindow)
Q_DET_S = 192.6              # det S                       (eq:refwindow)
Q_SUM = 4.22e-3              # det Ahat = the three-term sum
Q_TARGET = 1.10e-5           # ahat11 ahat22 h^{-3} at the reference window
Q_FACTOR = 384.0             # sum / target
Q_L1 = 40.6                  # l1-to-signed kernel ratio   (eq:l1mass)
Q_R1DEF = 1.3e-4             # median rank-one defect of X_n
Q_DIAG = 0.06                # diagonal share of det S ("about 6%")
NS_SUB = 900                 # the DECLARED subsample horizon of meas:l1
Q_TV_LO, Q_TV_HI = 5.00, 23.20   # the tightness range of meas:sharpness
Q_G1, Q_G2 = 0.6208, 1.2415  # the dual points at the reference window
Q_DGINV = 1.611              # 1/(gamma_2 - gamma_1) there (lem:dualpoint)

# --- the cheap tightness sub-surface (S3), declared ----------------------------
H_TIGHT = (142, 420)         # the CHEAP sub-range of the Surface-II family
SCHUR_KB = 16                # the fixed low block of the T152..T163 chain
SIGMA_LO, SIGMA_HI = 1.0, 4096.0   # the v555 Fejer knob, verbatim
N_SIGMA = 50
LAM_NEG = 1.0e-2             # the inadmissible control scale (rem:negcontrol)

# --- the v562 ladder surface (S5), verbatim ------------------------------------
ATOM_562 = 320000            # the v562 table cap (a PREFIX of the S1 table)
ANCHOR_LO = 40               # every anchor n has a COMPLETE comb: n^2 <= cap
ANCHOR_STEP = 6              # every 6th prime-power anchor (cost only, v562)
H_FINE = (128, 152, 181, 215, 256, 304)   # the 2^(1/4) ladder (T176's ratio)
H_COARSE = (128, 181, 256)   # the sqrt(2) sub-ladder (T175's)
DENS_BIN = (6.4, 102.4)      # the ONE declared T175/T176 ratio-4x2 bin
KB_CELL = 32                 # parity modes carried per cell (v562)
Q_A2 = -0.0842               # the MEASURED per-anchor curvature of log R in
#                              log h (T176 / rem:undecidable) -- consumed here
#                              only as the declared transport channel
BAR_LADDER = 1.0e-3          # fine vs coarse ladder must differ by >= this
FRAC_RUNG = 0.5              # rung part at fixed anchors <= this x full shift
FRAC_TRANS = 0.5             # curvature transport moves the shift <= this x
BAR_MUT_A2 = 10.0            # a wrong curvature must move >= this x the true

# --- preregistered tolerances / bars (declared BEFORE any number) --------------
TOL_QUOTE = 5.0e-3           # 3-significant-figure quotes, relative
TOL_SPLIT = 1.0e-6           # Ahat = B - S vs the direct block (probe horizon)
TOL_POLAR = 1.0e-9           # det expansion, relative
TOL_DSUM = 1.0e-9            # explicit kernel double sum, relative
BAR_MUT_POLAR = 1.0e2        # wrong polarisation coefficient: relative miss >=
BAR_SCRAM = 10.0             # scramble must move |1 - r12^2| by >= this
BAR_SIGNS = 10.0             # a mutated kernel must miss by >= this
TOL_TV_END = 1.0e-2          # both quoted ends of [5.00, 23.20], absolute
TOL_FLOOR = 1.0e-9           # mu^P_1 TV >= 1 - TOL_FLOOR (the floor theorem)
TOL_HOMOG = 1.0e-12          # degree-2 homogeneity of the control, relative
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
TOL_BAND = 1.0e-8            # band fit of W^(ij) on d = 1..M-1, relative sup
TOL_EXPSUM = 1.0e-10         # band read == exponential-sum read, relative
BAR_MUT_DUAL = 1.0e-2        # a mutated dual read must miss by >= this (rel.)


def sym(A):
    return 0.5 * (A + A.T)


def ast_zero_firewall(src_path: str) -> bool:
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                "zetazero", "nzeros", "second_sheet_zero",
            ):
                hits.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero", "nzeros"):
                hits.append(f.id)
        if isinstance(node, ast.Attribute) and node.attr in ("zetazero",):
            hits.append(node.attr)
    return not hits


# ---------------------------------------------------------------- atoms
def von_mangoldt_table(n_max):
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


LAM_TAB = von_mangoldt_table(ATOM_MAX)
_NN = np.nonzero(LAM_TAB > 0.0)[0]
U_ALL = np.log(_NN.astype(float))
MU_ALL = 2.0 * LAM_TAB[_NN] / np.sqrt(_NN.astype(float))
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)


def chebyshev_kappa():
    nn = _NN.astype(float)
    psi = np.cumsum(LAM_TAB[_NN])
    keep = nn >= KAPPA_X0
    return float(np.max(np.abs(psi[keep] - nn[keep]) / nn[keep]))


NZ_DEEP = int(np.searchsorted(_NN, ZONE_DEEP, side="right"))
G_ALL = np.diff(U_ALL)


def atoms_in(alpha):
    return int(np.searchsorted(U_ALL, 2.0 * alpha + 1.0e-14, side="right"))


# --------------------------------- the archimedean kernel (Weil 1952, cited)
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return ((tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w))
            / (-np.expm1(-2.0 * w)))


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        tot += half * float(np.dot(_GLW, _arch_integrand(w, s, D)))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * W))))


def arch_A(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = _arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = _arch_A_near(sv[i], D)
    return out


def arch_lags(M, D):
    out = np.empty(M)
    for a in range(0, M, CHUNK):
        b = min(M, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


# --------------------------------- parity geometry (KMS 1953; Dirichlet 1829)
def parity_mu(m):
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def odd_toeplitz(c, M):
    h = M // 2
    rr = np.arange(h)
    return (np.asarray(c)[np.abs(rr[:, None] - rr[None, :])]
            - np.asarray(c)[(M - 1) - rr[:, None] - rr[None, :]])


# --------------------------------- the T163/T170 weights and reads, verbatim
def lag_weights_from_v(v, m):
    """w_0 = A_0, w_d = 2 A_d - H_{M-1-d} (d >= 1); then v^T A_h v =
    sum_d c_d w_d EXACTLY (the T163 correlation theorem)."""
    M = 2 * m
    ac = np.correlate(v, v, "full")[m - 1:]
    cv = np.convolve(v, v)
    w = np.zeros(M)
    w[:m] = 2.0 * ac
    w[0] = ac[0]
    ee = (M - 1) - np.arange(1, M)
    w[1:] -= np.where(ee <= M - 2, cv[np.minimum(ee, M - 2)], 0.0)
    return w


def spline_project(W, u, D, M):
    """phi_n . W: the CLOSED two-point read of the weight vector W at
    tau = u/D (+ the d = 0 reflection when u < D), bit for bit T170."""
    i0 = int(math.floor(u / D))
    f = u / D - i0
    val = 0.0
    if 0 <= i0 < M:
        val += (1.0 - f) * W[i0]
    if 0 <= i0 + 1 < M:
        val += f * W[i0 + 1]
    if u < D:
        val += (1.0 - u / D) * W[0]
    return val


def mixed_det(P, Q):
    """D(P, Q) = P11 Q22 + P22 Q11 - 2 P12 Q12: the polarisation of det."""
    return (P[0, 0] * Q[1, 1] + P[1, 1] * Q[0, 0] - 2.0 * P[0, 1] * Q[0, 1])


def atom_lags_at(alpha, M, positions, masses):
    """The T115 tent assembly at EXPLICIT positions (real or scrambled)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for u_j, mu_j in zip(positions, masses):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


def frame_a_zones():
    """The T170 frame-A candidate scan, verbatim: every deep prime-power
    zone whose frame-A window lands inside [H_MIN, HCAP]."""
    out = []
    for kz in range(2, NZ_DEEP - 2):
        D_k = 0.5 * float(G_ALL[kz]) / float(NU_MAIN)
        M_k = int(math.ceil(U_ALL[kz] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        h_k = M_k // 2
        if h_k < H_MIN or h_k > HCAP or atoms_in(U_ALL[kz]) < N_ATOM_MIN:
            continue
        out.append(kz)
    return out


def build_window(kz, scramble_seed=None):
    """One frame-A window with the split Ahat = B - S and the per-atom
    2 x 2 spline reads X_n (bilinear_sieve_probe.py, bit for bit)."""
    alpha = float(U_ALL[kz])
    D_k = 0.5 * float(G_ALL[kz]) / float(NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = atoms_in(alpha)
    uu = U_ALL[:ka].copy()
    mm = MU_ALL[:ka].copy()
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    c_at, D = atom_lags_at(alpha, Mz, uu, mm)
    c_ar = arch_lags(Mz, D)
    Tb = parity_basis(hz, 2)
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    W11 = lag_weights_from_v(t1, hz)
    W22 = lag_weights_from_v(t2, hz)
    Wpp = lag_weights_from_v(t1 + t2, hz)
    W12 = 0.5 * (Wpp - W11 - W22)
    B = np.array([[float(c_ar @ W11), float(c_ar @ W12)],
                  [float(c_ar @ W12), float(c_ar @ W22)]])
    lam = 0.5 * mm                       # rho_n = Lambda(n)/sqrt(n)
    Xn = np.empty((ka, 3))
    for i in range(ka):
        Xn[i, 0] = spline_project(W11, uu[i], D, Mz)
        Xn[i, 1] = spline_project(W22, uu[i], D, Mz)
        Xn[i, 2] = spline_project(W12, uu[i], D, Mz)
    S = np.array([[float(lam @ Xn[:, 0]), float(lam @ Xn[:, 2])],
                  [float(lam @ Xn[:, 2]), float(lam @ Xn[:, 1])]])
    Ah = B - S
    A_full = odd_toeplitz(c_ar + c_at, Mz)
    Ah_dir = np.array([[float(t1 @ (A_full @ t1)), float(t1 @ (A_full @ t2))],
                       [float(t1 @ (A_full @ t2)), float(t2 @ (A_full @ t2))]])
    del A_full
    r = dict(k=kz, h=hz, M=Mz, D=D, alpha=alpha, n_zone=int(_NN[kz]),
             n_atom=ka, X=math.exp(2.0 * alpha), uu=uu, lam=lam, Xn=Xn,
             B=B, S=S, Ah=Ah, Ah_dir=Ah_dir,
             W11=W11, W22=W22, W12=W12, t1=t1, t2=t2)
    r["a11"], r["a22"], r["a12"] = (float(Ah[0, 0]), float(Ah[1, 1]),
                                    float(Ah[0, 1]))
    r["det"] = float(np.linalg.det(Ah))
    r["onem"] = r["det"] / (r["a11"] * r["a22"])
    return r


def tv_of(y, m):
    """TV(x) = ||Delta w||_1 with the T163 convention w_M := 0."""
    w = lag_weights_from_v(y, m)
    return float(np.sum(np.abs(np.diff(np.append(w, 0.0)))))


def tightness_window(kz):
    """One cheap Surface-II window for the tightness readout: the 16-mode
    normalised low block, its untapered optimiser and the Fejer knob
    (v555's declared trial family, verbatim)."""
    alpha = float(U_ALL[kz])
    D_k = 0.5 * float(G_ALL[kz]) / float(NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = atoms_in(alpha)
    c_at, D = atom_lags_at(alpha, Mz, U_ALL[:ka], MU_ALL[:ka])
    A = odd_toeplitz(arch_lags(Mz, D) + c_at, Mz)
    mu = parity_mu(hz)
    T16 = parity_basis(hz, SCHUR_KB)
    isq = 1.0 / np.sqrt(mu[:SCHUR_KB])
    BLL = sym((T16 @ (A @ T16.T)) * np.outer(isq, isq))
    del A
    ev = np.linalg.eigvalsh(BLL)
    e1 = np.zeros(SCHUR_KB)
    e1[0] = 1.0
    xs = np.linalg.solve(BLL, e1)
    xs /= max(abs(float(xs[0])), 1.0e-300)
    vals = []
    for sg in list(np.geomspace(SIGMA_LO, SIGMA_HI, N_SIGMA)) + [math.inf]:
        t = (np.ones(SCHUR_KB) if math.isinf(sg)
             else np.maximum(0.0, 1.0 - np.arange(SCHUR_KB) / sg))
        x = t * xs
        if float(x @ (BLL @ x)) <= 0.0:
            continue
        y = (T16.T / np.sqrt(mu[:SCHUR_KB])) @ x
        vals.append(float(mu[0]) * tv_of(y, hz))
    y_un = (T16.T / np.sqrt(mu[:SCHUR_KB])) @ xs
    return dict(h=hz, cond=float(ev[-1] / max(ev[0], 1e-300)),
                vals=vals, mu1=float(mu[0]), y_un=y_un,
                tv_un=float(mu[0]) * tv_of(y_un, hz))


def band_fit(W, hz):
    """Fit (w_d)_{d=1}^{M-1} on the 4K = 8 sequences of eq:bandspace
    (K = 2): returns the coefficients in the lem:dualpoint notation
    (a_k + b_k tau) cos(omega_k tau) + (c_k + d_k tau) sin(omega_k tau)
    and the sup-norm residual of the fit (lem:band says it is zero)."""
    M = 2 * hz
    N = 2 * hz + 1
    dd = np.arange(1, M, dtype=float)
    cols = []
    for k in (1, 2):
        om = 2.0 * math.pi * k / N
        cols += [np.cos(om * dd), dd * np.cos(om * dd),
                 np.sin(om * dd), dd * np.sin(om * dd)]
    Bm = np.column_stack(cols)
    coef, _, _, _ = np.linalg.lstsq(Bm, np.asarray(W)[1:], rcond=None)
    resid = float(np.max(np.abs(Bm @ coef - np.asarray(W)[1:])))
    a = (coef[0], coef[4])
    b = (coef[1], coef[5])
    c = (coef[2], coef[6])
    d = (coef[3], coef[7])
    return a, b, c, d, resid


def band_eval(a, b, c, d, hz, tau):
    N = 2 * hz + 1
    out = np.zeros_like(np.asarray(tau, dtype=float))
    for i, k in enumerate((1, 2)):
        om = 2.0 * math.pi * k / N
        out += ((a[i] + b[i] * tau) * np.cos(om * tau)
                + (c[i] + d[i] * tau) * np.sin(om * tau))
    return out


def dual_read(a, b, c, d, rho, uu, gam, D, drop_moment=False):
    """The lem:dualpoint main term: sum_k Re[(a_k - i c_k) T_0(gamma_k)
    + (1/D)(b_k - i d_k) T_1(gamma_k)] with T_q(g) = sum rho_n
    (log n)^q n^{i g}."""
    tot = 0.0
    for i in range(2):
        e = np.exp(1j * gam[i] * uu)
        T0 = complex(np.sum(rho * e))
        T1 = complex(np.sum(rho * uu * e))
        tot += ((a[i] - 1j * c[i]) * T0).real
        if not drop_moment:
            tot += (((b[i] - 1j * d[i]) * T1).real / D)
    return tot


# --------------------------------- the v562 cell machinery, verbatim (S5)
_TB = {}


def basis_of(hz):
    if hz not in _TB:
        _TB[hz] = (parity_basis(hz, KB_CELL), parity_mu(hz)[:KB_CELL])
    return _TB[hz]


def atom_lags_binned(alpha, M, u, mu):
    """T176's production assembly (bincount), bit for bit v562."""
    D = 2.0 * alpha / M
    q = u / D
    i0 = np.floor(q).astype(np.int64)
    f = q - i0
    c = np.bincount(i0, weights=-mu * 0.5 * (1.0 - f), minlength=M)[:M].copy()
    idx = i0 + 1
    ok = idx < M
    c += np.bincount(idx[ok], weights=-mu[ok] * 0.5 * f[ok], minlength=M)[:M]
    refl = u < D
    if refl.any():
        c[0] -= 0.5 * float(np.sum(mu[refl] * (1.0 - u[refl] / D)))
    return c, D


def build_cell(n_zone, hz):
    """ONE (anchor, rung) cell of the v562 surface; the builder sees
    (n_zone, alpha, M) and nothing else."""
    alpha = math.log(float(n_zone))
    M = 2 * hz
    ka = int(np.searchsorted(U_ALL, 2.0 * alpha + 1.0e-14, side="right"))
    c_at, D = atom_lags_binned(alpha, M, U_ALL[:ka], MU_ALL[:ka])
    Tb, mu = basis_of(hz)
    Ah = sym(Tb @ (odd_toeplitz(arch_lags(M, D) + c_at, M) @ Tb.T))
    isq = 1.0 / np.sqrt(np.asarray(mu, dtype=float)[:SCHUR_KB])
    ev = np.linalg.eigvalsh(sym(Ah[:SCHUR_KB, :SCHUR_KB]
                                * np.outer(isq, isq)))
    lmin, lmax = float(ev[0]), float(ev[-1])
    a11, a12, a22 = float(Ah[0, 0]), float(Ah[0, 1]), float(Ah[1, 1])
    dl = (a11 * a22 - a12 * a12) / (a11 * a22)
    return dict(n=n_zone, h=hz, dens=float(ka) / float(M),
                R=(lmin / lmax) / max(abs(dl), 1.0e-300),
                pd=bool(lmin > 0.0),
                complete=float(n_zone) ** 2 <= float(ATOM_562) + 0.5)


def bin_rows(cells, lo, hi, min_rung=3):
    """The in-bin (anchor -> cells) map of the T175/T176 estimator."""
    byn = {}
    for r in cells:
        if lo <= r["dens"] < hi:
            byn.setdefault(r["n"], []).append(r)
    return {n: sorted(v, key=lambda r: r["h"])
            for n, v in byn.items() if len(v) >= min_rung}


def anchor_slope(row):
    """One OLS slope of log|R| on log h, plus the rung mean of log h."""
    lx = np.array([math.log(float(r["h"])) for r in row])
    ly = np.array([math.log(abs(r["R"])) for r in row])
    xc = lx - lx.mean()
    return float(xc @ ly / np.sum(xc * xc)), float(lx.mean())


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v563  PRIME.PAPER2.READOUT.01 -- the Paper-II readouts, recomputed")
    print("=" * 72)

    # ================================================================ S0
    print("\nS0 -- firewall + the one arithmetic input")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__), True, exact=True)
    kappa = chebyshev_kappa()
    check(f"S0.KAPPA: kappa = {kappa:.6f} reproduced to "
          f"{abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} at every jump "
          f"point of psi(x)/x on the table in [{KAPPA_X0:.0f}, {ATOM_MAX}] "
          f"(Chebyshev 1852 / Rosser-Schoenfeld 1962)",
          abs(kappa - KAPPA_REF) <= TOL_KAPPA, True, exact=True)

    # ================================================================ S1
    print("\nS1 -- the reference window: the three-term cancellation "
          "(meas:refwindow)")
    KZ = frame_a_zones()
    kz_ref = KZ[len(KZ) // 2]
    R0 = build_window(kz_ref)
    detB = float(np.linalg.det(R0["B"]))
    detS = float(np.linalg.det(R0["S"]))
    mix = float(mixed_det(R0["B"], R0["S"]))
    target = R0["a11"] * R0["a22"] * float(R0["h"]) ** (-3.0)
    e_split = (float(np.max(np.abs(R0["Ah_dir"] - R0["Ah"])))
               / max(1.0, float(np.max(np.abs(R0["Ah_dir"])))))
    e_polar = abs(detB - mix + detS - R0["det"]) / max(1e-300, abs(R0["det"]))
    print(f"    reference window: h = {R0['h']}, M = {R0['M']}, "
          f"n_zone = {R0['n_zone']}, X = {R0['X']:.4g}, "
          f"{R0['n_atom']} atoms, D = {R0['D']:.6e}")
    print(f"    det B = {detB:.6f}   -D(B,S) = {-mix:.6f}   "
          f"det S = {detS:.6f}")
    print(f"    sum = det Ahat = {R0['det']:.6e}   target = {target:.6e}   "
          f"ratio = {R0['det'] / target:.1f}")
    check(f"S1.WINDOW: the declared T170 frame-A scan (mid element of "
          f"{len(KZ)} candidates) lands on the reference window h = "
          f"{R0['h']} with node cap X = {R0['X']:.4g} = n_zone^2 "
          f"({R0['n_zone']}^2), as declared in the paper",
          R0["h"] == Q_H_REF
          and abs(R0["X"] - Q_X_REF) / Q_X_REF <= TOL_QUOTE, True,
          exact=True)
    check(f"S1.SPLIT [E] Ahat = B - S reproduces the DIRECT t_i^T A_h t_j "
          f"to rel {e_split:.2e} <= {TOL_SPLIT:.0e}, and det Ahat = det B "
          f"- D(B,S) + det S to rel {e_polar:.2e} <= {TOL_POLAR:.0e} "
          f"(the exact polarisation)",
          e_split <= TOL_SPLIT and e_polar <= TOL_POLAR, True, exact=True)
    e_q = max(abs(detB - Q_DET_B) / abs(Q_DET_B),
              abs(-mix - Q_MIX) / abs(Q_MIX),
              abs(detS - Q_DET_S) / abs(Q_DET_S),
              abs(R0["det"] - Q_SUM) / abs(Q_SUM))
    check(f"S1.READOUT [E] the four quoted numbers of eq:refwindow are "
          f"RECOMPUTED: det B = {detB:.4f} (quote {Q_DET_B}), -D(B,S) = "
          f"{-mix:.4f} (quote {Q_MIX}), det S = {detS:.4f} (quote "
          f"{Q_DET_S}), sum = {R0['det']:.4e} (quote {Q_SUM:.2e}) -- "
          f"worst relative deviation {e_q:.1e} <= {TOL_QUOTE:.0e}",
          e_q <= TOL_QUOTE, True, exact=True)
    orders = math.log10(abs(mix) / abs(R0["det"]))
    e_t = max(abs(target - Q_TARGET) / Q_TARGET,
              abs(R0["det"] / target - Q_FACTOR) / Q_FACTOR)
    check(f"S1.SCALE [E] the absolute target ahat11 ahat22 h^-3 = "
          f"{target:.3e} (quote {Q_TARGET:.2e}) sits a further factor "
          f"{R0['det'] / target:.0f} (quote {Q_FACTOR:.0f}) below the "
          f"residual sum, and the cancellation spans "
          f"{orders:.2f} orders of magnitude (the paper's 'five orders', "
          f"quoted to the nearest order)",
          e_t <= TOL_QUOTE and 4.5 <= orders <= 5.5, True, exact=True)
    # mutation: the wrong polarisation cross-coefficient misses loudly
    mix_bad = (R0["B"][0, 0] * R0["S"][1, 1] + R0["B"][1, 1] * R0["S"][0, 0]
               - 1.0 * R0["B"][0, 1] * R0["S"][0, 1])
    e_bad = abs(detB - mix_bad + detS - R0["det"]) / abs(R0["det"])
    # control: uniform positions at the SAME masses move the value
    R0s = build_window(kz_ref, scramble_seed=SEED)
    move = abs(R0s["onem"]) / max(abs(R0["onem"]), 1e-300)
    move = max(move, 1.0 / max(move, 1e-300))
    check(f"S1.MUT [must-break] the polarisation with the WRONG "
          f"cross-coefficient (-1 for -2) misses by {e_bad:.1e} >= "
          f"{BAR_MUT_POLAR:.0e} of det Ahat, and the position scramble "
          f"(uniform u at the SAME masses, seeded) moves |1 - r12^2| by a "
          f"factor {move:.1e} >= {BAR_SCRAM:.0f} while the split and "
          f"polarisation identities keep holding on the scrambled window "
          f"-- the cancellation is WHERE the atoms sit",
          e_bad >= BAR_MUT_POLAR and move >= BAR_SCRAM, True, exact=True)

    # ================================================================ S2
    print("\nS2 -- mixed signs: the l1-to-signed ratio (meas:l1)")
    lam, Xn = R0["lam"], R0["Xn"]
    nn = len(lam)
    idx = (np.linspace(0, nn - 1, NS_SUB).astype(int) if nn > NS_SUB
           else np.arange(nn))
    lx, Xx = lam[idx], Xn[idx]
    Sx = np.array([[float(lx @ Xx[:, 0]), float(lx @ Xx[:, 2])],
                   [float(lx @ Xx[:, 2]), float(lx @ Xx[:, 1])]])
    K = 0.5 * (np.outer(Xx[:, 0], Xx[:, 1]) + np.outer(Xx[:, 1], Xx[:, 0])
               - 2.0 * np.outer(Xx[:, 2], Xx[:, 2]))
    dsum = float(lx @ (K @ lx))
    e_dsum = abs(dsum - np.linalg.det(Sx)) / max(1e-300, abs(dsum))
    absK = float(lx @ (np.abs(K) @ lx))
    ratio = absK / abs(dsum)
    print(f"    subsample {len(idx)} of {nn} atoms; det Sx = "
          f"{np.linalg.det(Sx):.6e}; l1 mass = {absK:.6e}; ratio = "
          f"{ratio:.2f}")
    check(f"S2.KERNEL [E] the explicit double sum sum lam_n lam_m K(n,m) "
          f"with K = (1/2) D(X_n, X_m) equals det S on the declared "
          f"{len(idx)}-atom subsample to rel {e_dsum:.1e} <= "
          f"{TOL_DSUM:.0e} (Cauchy-Binet 1812/1815; Lagrange 1773)",
          e_dsum <= TOL_DSUM, True, exact=True)
    e_r = abs(ratio - Q_L1) / Q_L1
    check(f"S2.L1 [E] the l1 kernel mass is {ratio:.2f} x the signed "
          f"value on the declared {NS_SUB}-node subsample (quote "
          f"{Q_L1}; relative deviation {e_r:.1e} <= {TOL_QUOTE:.0e}): a "
          f"triangle-inequality route loses that factor before it starts",
          e_r <= TOL_QUOTE, True, exact=True)
    dX = Xn[:, 0] * Xn[:, 1] - Xn[:, 2] ** 2
    nX = Xn[:, 0] ** 2 + Xn[:, 1] ** 2 + 2.0 * Xn[:, 2] ** 2
    r1_def = float(np.median(np.abs(dX) / np.maximum(nX, 1e-300)))
    diag_share = abs(float(np.sum(lam ** 2 * dX)) / detS)
    check(f"S2.WEDGE [E] the rank-one defect of the reads is median "
          f"|det X_n|/||X_n||^2 = {r1_def:.2e} (quote {Q_R1DEF:.1e}), "
          f"and the diagonal n = m carries {100.0 * diag_share:.1f}% of "
          f"det S in magnitude (the paper's 'about 6%'): the wedge "
          f"reading is accurate but not exact, as stated",
          abs(r1_def - Q_R1DEF) / Q_R1DEF <= 0.05
          and 0.05 <= diag_share <= 0.07, True, exact=True)
    # mutation: the wrong polarisation coefficient breaks the kernel loudly
    K_bad = K + 0.5 * np.outer(Xx[:, 2], Xx[:, 2])   # -2 -> -1 cross term
    miss = abs(float(lx @ (K_bad @ lx)) - dsum) / abs(dsum)
    check(f"S2.MUT [must-break] the kernel with the WRONG polarisation "
          f"cross-coefficient (-1 for -2) misses det S by a factor "
          f"{miss:.1e} >= {BAR_SIGNS:.0f} of the signed value: the "
          f"cancellation is carried by the exact rank-3 kernel with "
          f"inertia (1, 2) (mixed signs), not by any positive kernel",
          miss >= BAR_SIGNS, True, exact=True)

    # ================================================================ S3
    print("\nS3 -- the tightness range where cheap (meas:sharpness)")
    cheap = []
    for kz in KZ:
        D_k = 0.5 * float(G_ALL[kz]) / float(NU_MAIN)
        M_k = int(math.ceil(U_ALL[kz] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if H_TIGHT[0] <= M_k // 2 <= H_TIGHT[1]:
            cheap.append(kz)
    TW = [tightness_window(kz) for kz in cheap]
    all_vals = [v for r in TW for v in r["vals"]]
    lo_all, hi_all = min(all_vals), max(all_vals)
    print(f"    {len(TW)} cheap windows h = {min(r['h'] for r in TW)}.."
          f"{max(r['h'] for r in TW)}; sweep {len(all_vals)} trial "
          f"vectors; mu1 TV = {lo_all:.4f}..{hi_all:.4f}")
    check(f"S3.FLOOR [E] mu^P_1 TV(x) >= 1 on ALL {len(all_vals)} trial "
          f"vectors of the declared family ({N_SIGMA + 1} Fejer sigma x "
          f"{len(TW)} cheap Surface-II windows h in [{H_TIGHT[0]}, "
          f"{H_TIGHT[1]}], cond(B_LL) <= "
          f"{max(r['cond'] for r in TW):.1e} <= {COND_BAR:.0e}): the "
          f"closed floor of thm:tvfloor, worst value {lo_all:.4f}",
          lo_all >= 1.0 - TOL_FLOOR
          and max(r["cond"] for r in TW) <= COND_BAR, True, exact=True)
    check(f"S3.RANGE [E] the QUOTED tightness range [{Q_TV_LO}, "
          f"{Q_TV_HI}] of meas:sharpness is recomputed on the cheap "
          f"sub-surface: every trial value lies inside it (up to the "
          f"quote rounding {TOL_TV_END}), and BOTH ends are attained -- "
          f"min {lo_all:.4f} vs {Q_TV_LO} (the taper end), max "
          f"{hi_all:.4f} vs {Q_TV_HI} (the untapered optimiser)",
          Q_TV_LO - TOL_TV_END <= lo_all
          and hi_all <= Q_TV_HI + TOL_TV_END
          and abs(lo_all - Q_TV_LO) <= TOL_TV_END
          and abs(hi_all - Q_TV_HI) <= TOL_TV_END, True, exact=True)
    # the inadmissible control (rem:negcontrol): x_1 = lambda != 1
    r0 = TW[0]
    v_neg = r0["mu1"] * tv_of(LAM_NEG * r0["y_un"], r0["h"])
    e_hom = abs(v_neg - LAM_NEG ** 2 * r0["tv_un"]) / max(v_neg, 1e-300)
    check(f"S3.MUT [must-break] the INADMISSIBLE vector lambda x* with "
          f"lambda = {LAM_NEG} undercuts the floor: mu^P_1 TV = "
          f"{v_neg:.1e} << 1 (the paper's ~7e-4 reading), and it does so "
          f"by EXACTLY the predicted factor lambda^2 (degree-2 "
          f"homogeneity, rel {e_hom:.1e} <= {TOL_HOMOG:.0e}): the floor "
          f"is a statement about the normalisation x_1 = 1, and "
          f"recognising the violation is the content of the control",
          v_neg < 1.0e-2 and e_hom <= TOL_HOMOG, True, exact=True)

    # ================================================================ S4
    print("\nS4 -- lem:dualpoint assembled end to end (the dual-point read)")
    hz, Mz, D = R0["h"], R0["M"], R0["D"]
    N = 2 * hz + 1
    gam = np.array([2.0 * math.pi * 1.0 / (N * D),
                    2.0 * math.pi * 2.0 / (N * D)])
    dginv = N * D / (2.0 * math.pi)
    uu_all, rho_all = R0["uu"], R0["lam"]
    tau_all = uu_all / D
    interior = (tau_all >= 1.0) & (tau_all <= float(Mz - 1))
    uu, rho = uu_all[interior], rho_all[interior]
    n_tail = int(np.sum(~interior))
    e_gq = max(abs(gam[0] - Q_G1) / Q_G1, abs(gam[1] - Q_G2) / Q_G2,
               abs(dginv - Q_DGINV) / Q_DGINV)
    check(f"S4.POINTS [E] the dual points of eq:dualpoints are READ OFF, "
          f"not fitted: gamma_1 = {gam[0]:.4f} (quote {Q_G1}), gamma_2 = "
          f"{gam[1]:.4f} (quote {Q_G2}), spacing 1/Delta-gamma = "
          f"{dginv:.4f} (quote {Q_DGINV}), X = {R0['X']:.4g} (quote "
          f"{Q_X_REF:.4g}) -- worst deviation {e_gq:.1e} <= "
          f"{TOL_QUOTE:.0e}; {len(uu)} of {len(uu_all)} reads are "
          f"interior (1 <= tau <= M-1, the lemma's hypothesis), the "
          f"{n_tail} tail atoms within one lag of the node cap are "
          f"excluded as the hypothesis demands",
          e_gq <= TOL_QUOTE, True, exact=True)
    rho1 = float(np.sum(rho))
    rho2sq = float(np.sum(rho ** 2))
    Qmv = math.sqrt((R0["X"] + dginv) * rho2sq)
    names = ("11", "22", "12")
    weights = (R0["W11"], R0["W22"], R0["W12"])
    e_band, e_id, e_res, e_mv = [], [], [], []
    e_mut_g, e_mut_m, mom12 = [], [], 0.0
    for nm, W in zip(names, weights):
        a, b, c, d, resid = band_fit(W, hz)
        scale = float(np.max(np.abs(W[1:])))
        e_band.append(resid / scale)
        lam0 = (abs(a[0]) + abs(c[0]) + abs(a[1]) + abs(c[1])
                + Mz * (abs(b[0]) + abs(d[0]) + abs(b[1]) + abs(d[1])))
        lam1 = abs(b[0]) + abs(d[0]) + abs(b[1]) + abs(d[1])
        om2 = 2.0 * math.pi * 2.0 / N
        eta = 0.125 * (om2 ** 2 * lam0 + 2.0 * om2 * lam1)
        s_dir = float(sum(r * spline_project(W, u, D, Mz)
                          for r, u in zip(rho, uu)))
        s_band = float(np.sum(rho * band_eval(a, b, c, d, hz, uu / D)))
        s_dual = dual_read(a, b, c, d, rho, uu, gam, D)
        e_id.append(abs(s_dual - s_band) / max(abs(s_band), 1e-300))
        e_res.append(abs(s_dir - s_dual) / (eta * rho1))
        e_mv.append(abs(s_dir) / (lam0 * Qmv + eta * rho1))
        m1 = dual_read(a, b, c, d, rho, uu, gam * 1.01, D)
        e_mut_g.append(abs(m1 - s_dual) / max(abs(s_dir), 1e-300))
        if nm == "12":
            mom12 = max(abs(b[0]), abs(b[1]), abs(d[0]), abs(d[1]))
        else:
            m2 = dual_read(a, b, c, d, rho, uu, gam, D, drop_moment=True)
            e_mut_m.append(abs(m2 - s_dual) / max(abs(s_dir), 1e-300))
        print(f"    S_{nm}: direct = {s_dir:+.6e}, dual read = "
              f"{s_dual:+.6e}, eta ||rho||_1 = {eta * rho1:.3e}, "
              f"MV bound = {lam0 * Qmv + eta * rho1:.3e}")
    a1, b1, c1, d1, _ = band_fit(R0["W11"], hz)
    om1 = 2.0 * math.pi / N
    e_closed = max(abs(a1[0] - 2.0), abs(b1[0] + 2.0 / N),
                   abs(c1[0] - 2.0 / N / math.tan(om1)), abs(d1[0]),
                   abs(a1[1]), abs(b1[1]), abs(c1[1]), abs(d1[1]))
    check(f"S4.BAND [E] every polarised weight W^(ij) lies in the "
          f"8-dimensional band space of eq:bandspace (K = 2): sup-norm "
          f"fit residual {max(e_band):.1e} <= {TOL_BAND:.0e} of the "
          f"weight scale on d = 1..M-1 (lem:band), and the single-mode "
          f"coefficients reproduce eq:closedweight in closed form "
          f"(alpha = 2, beta = -2/N, gamma = (2/N) cot omega_1, delta = "
          f"0; worst {e_closed:.1e})",
          max(e_band) <= TOL_BAND and e_closed <= 1.0e-6, True,
          exact=True)
    check(f"S4.EXPSUM [E] THE THREE READS ARE VALUES OF ONE EXPONENTIAL "
          f"SUM: the band read equals sum_k Re[(a_k - i c_k) "
          f"T_0(gamma_k) + (1/D)(b_k - i d_k) T_1(gamma_k)] with T_q the "
          f"length-X exponential sum and its first log moment, at the "
          f"two dual points AND AT NO OTHERS, to rel {max(e_id):.1e} <= "
          f"{TOL_EXPSUM:.0e} on all three reads (eq:dualread, the "
          f"identity half)",
          max(e_id) <= TOL_EXPSUM, True, exact=True)
    check(f"S4.RESID [E] the interpolation residual of eq:dualread is "
          f"INSIDE its declared budget on all three reads: |S_ij - main "
          f"term| <= eta^(ij) ||rho||_1 with eta from eq:splinebound, "
          f"used fraction {max(e_res):.3f} <= 1 (the two-point read "
          f"against the analytic read, lem:spline)",
          max(e_res) <= 1.0, True, exact=True)
    mv0 = (abs(np.sum(rho * np.exp(1j * gam[0] * uu))) ** 2
           + abs(np.sum(rho * np.exp(1j * gam[1] * uu))) ** 2)
    mv1 = (abs(np.sum(rho * uu * np.exp(1j * gam[0] * uu))) ** 2
           + abs(np.sum(rho * uu * np.exp(1j * gam[1] * uu))) ** 2)
    mv1_bar = (R0["X"] + dginv) * float(np.sum((rho * uu) ** 2))
    check(f"S4.MV [E] the Montgomery-Vaughan step of eq:mvread holds as "
          f"used: sum_k |T_0(gamma_k)|^2 = {mv0:.4e} <= (X + "
          f"1/Delta-gamma) ||rho||_2^2 = {Qmv ** 2:.4e}, the log-moment "
          f"analogue {mv1:.4e} <= {mv1_bar:.4e}, and |S_ij| <= "
          f"Lambda_0 Q + eta ||rho||_1 on all three reads (used "
          f"fraction {max(e_mv):.1e} -- the bound holds and is far from "
          f"sharp, which is meas:routes' point about route R3)",
          mv0 <= Qmv ** 2 and mv1 <= mv1_bar and max(e_mv) <= 1.0,
          True, exact=True)
    check(f"S4.MUT [must-break] the dual read with SHIFTED points "
          f"(gamma_k x 1.01) misses by >= {BAR_MUT_DUAL:.0e} of |S_ij| "
          f"on every read (worst {min(e_mut_g):.2e}), and DROPPING the "
          f"log-moment term misses on both single-mode reads (worst "
          f"{min(e_mut_m):.2e}); on the polarised cross read W^(12) the "
          f"moment coefficients VANISH IDENTICALLY ({mom12:.1e} <= "
          f"1e-10 -- lem:band: the linear-in-tau coefficients are "
          f"proportional to a_k^2 and cancel in the polarisation), so "
          f"the two points carry that read alone",
          min(e_mut_g) >= BAR_MUT_DUAL and min(e_mut_m) >= BAR_MUT_DUAL
          and mom12 <= 1.0e-10, True, exact=True)

    # ================================================================ S5
    print("\nS5 -- the ladder shift is ANCHOR SELECTION (rem:undecidable)")
    zone_max = int(math.isqrt(ATOM_562))
    anchors = [int(n) for n in _NN
               if ANCHOR_LO <= n <= zone_max
               and n * n <= ATOM_562][::ANCHOR_STEP]
    CELLS = [build_cell(n, h) for n in anchors for h in H_FINE]
    fine = bin_rows(CELLS, *DENS_BIN)
    coarse = bin_rows([r for r in CELLS if r["h"] in H_COARSE], *DENS_BIN)
    sF = {n: anchor_slope(v) for n, v in fine.items()}
    sC = {n: anchor_slope(v) for n, v in coarse.items()}
    A_F, A_C = set(sF), set(sC)
    d_F = -float(np.mean([sF[n][0] for n in sorted(A_F)]))
    d_C = -float(np.mean([sC[n][0] for n in sorted(A_C)]))
    d_FC = -float(np.mean([sF[n][0] for n in sorted(A_C)]))
    shift = d_F - d_C
    part_anchor = d_F - d_FC
    part_rung = d_FC - d_C
    extra = sorted(A_F - A_C)
    print(f"    surface: {len(anchors)} anchors x {len(H_FINE)} rungs = "
          f"{len(CELLS)} cells, {sum(r['pd'] for r in CELLS)}/{len(CELLS)}"
          f" PD; bin dens in [{DENS_BIN[0]}, {DENS_BIN[1]})")
    print(f"    d_fine = {d_F:+.6f} ({len(A_F)} anchors), d_coarse = "
          f"{d_C:+.6f} ({len(A_C)} anchors), d_fine|coarse anchors = "
          f"{d_FC:+.6f}")
    print(f"    shift = {shift:+.6f} = anchor part {part_anchor:+.6f} + "
          f"rung part {part_rung:+.6f}; extra anchors {extra}")
    check(f"S5.BASELINE [E] the v562 anti-promotion reproduced on the "
          f"identical declared surface ({len(anchors)} complete-comb "
          f"anchors x the 2^(1/4) ladder, "
          f"{sum(r['pd'] for r in CELLS)}/{len(CELLS)} PD): the same "
          f"declared bin gives {d_F:+.4f} on the fine and {d_C:+.4f} on "
          f"the coarse sqrt(2) sub-ladder -- a shift of {abs(shift):.4f} "
          f">= {BAR_LADDER:.0e}: the estimator is LADDER-DEPENDENT",
          all(r["pd"] and r["complete"] for r in CELLS)
          and abs(shift) >= BAR_LADDER, True, exact=True)
    check(f"S5.ANCHOR [E] THE SHIFT IS ANCHOR SELECTION: the two ladders "
          f"select DIFFERENT anchor sets in the SAME bin ({len(A_F)} vs "
          f"{len(A_C)} anchors; the fine ladder's extra anchors are "
          f"{extra} -- an anchor needs 3 in-bin rungs, and the coarse "
          f"ladder offers it fewer).  Removing them reproduces the whole "
          f"shift: the anchor part is {part_anchor:+.4f} "
          f"(|part| >= |shift| = {abs(shift):.4f}), while the rung part "
          f"at FIXED anchor set is {part_rung:+.4f} "
          f"(<= {FRAC_RUNG} x |shift|)",
          A_C < A_F and abs(part_anchor) >= abs(shift)
          and abs(part_rung) <= FRAC_RUNG * abs(shift), True, exact=True)
    xbF = float(np.mean([sF[n][1] for n in sorted(A_F)]))
    xbC = float(np.mean([sC[n][1] for n in sorted(A_C)]))
    xbFC = float(np.mean([sF[n][1] for n in sorted(A_C)]))
    corr_full = 2.0 * Q_A2 * (xbF - xbC)
    corr_fix = 2.0 * Q_A2 * (xbFC - xbC)
    shift_t = shift + corr_full
    check(f"S5.TRANSPORT [E] CURVATURE TRANSPORT DOES NOT EXPLAIN THE "
          f"SHIFT: transporting every anchor slope to a common log-h "
          f"reference with the paper's MEASURED curvature a2 = {Q_A2} "
          f"(the only curvature channel rem:undecidable names) moves "
          f"the shift by {corr_full:+.4f} <= {FRAC_TRANS} x |shift|, "
          f"leaving {shift_t:+.4f} -- the shift survives transport "
          f"because it lives in WHICH anchors enter the bin, not in how "
          f"the rungs sample the curvature",
          abs(corr_full) <= FRAC_TRANS * abs(shift)
          and abs(shift_t) >= (1.0 - FRAC_TRANS) * abs(shift), True,
          exact=True)
    corr_bad = 2.0 * 1.0 * (xbFC - xbC)
    check(f"S5.MUT [must-break] the transport channel has teeth: a WRONG "
          f"curvature (a2 = +1.0 in place of the measured {Q_A2}) moves "
          f"the fixed-anchor comparison by {corr_bad:+.4f}, a factor "
          f"{abs(corr_bad / corr_fix):.1f} >= {BAR_MUT_A2:.0f} louder "
          f"than the true transport ({corr_fix:+.4f}) -- the smallness "
          f"of the true correction is a measurement, not a no-op of the "
          f"construction",
          abs(corr_bad) >= BAR_MUT_A2 * abs(corr_fix), True, exact=True)

    print(f"\n[TIME] {time.time() - t0:.1f} s")
    return summary("PRIME.PAPER2.READOUT.01 paper-II readouts")


if __name__ == "__main__":
    raise SystemExit(run())
