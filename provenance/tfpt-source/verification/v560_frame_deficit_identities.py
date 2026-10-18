"""v560 -- PRIME.FRAME.DEFICIT.01: the frame / deficit identities (T172+T173+T174).
THE GAUGE ROUTE OF PHASE 2, CLOSED AS ALGEBRA.  T172 (contract FRAME.BEYOND)
measured that the identity links of the certified map transfer unchanged
beyond frame A; T173 (contract FRAME.RATE) showed the demanded rate is itself
a frame datum via the exact identity q = 1 - s and calibrated the gap
functional; T174 (contract CANCEL.IDENTITY) turned "do the frame factors
cancel" into blindness theorems of two scale-free functionals of ONE raw Gram
matrix.  THIS module is the load-bearing version of the theorem-shaped cores
of those three parts -- per instance, machine-checkable, each with a mutation
control -- and it makes NO rate claim and NO uniformity claim:

[E] (1) THE IDENTITY TRANSFER (T172 P1) + THE SIEVE-HORIZON DISCRIMINATOR
    (T172 P2).  Four representative chain links -- the KMS/Schur pair
    (T L_P T^T = diag(mu^P); the quadratic-form pair), the lag-sum /
    correlation-weights identity (v^T A_h v = sum_d c_d w_d, T163), the
    R4-free det collapse (1 - r_12^2 = det Ahat_2/(a11 a22) = nu_1 nu_2 /
    (a11 a22) = det G_2/(G_11 G_22), no positivity of A_h consumed), and the
    additive split (Ahat = Ahat_arch + Ahat_comb by linearity) -- are
    re-derived EXACTLY on a gap-blind frame-B instance AND on a
    non-prime-power-anchor instance: the links use no property of the frame
    rule or the anchor arithmetic, which is WHY they transfer (the T172
    surface is the evidence, the derivation is the reason).  The
    DISCRIMINATOR: on a truncated-comb instance (the anchor's zone runs past
    the sieve cap, so the comb is CUT while the grid runs to X = e^{2 alpha})
    the low block turns INDEFINITE while every complete-comb cell is positive
    definite -- indefiniteness is located at the DECLARED sieve horizon, not
    at a frame or a zone family -- and the identity links keep holding there,
    because none of them uses positivity.
[E] (2) THE q = 1 - s IDENTITY + THE GAP-FUNCTIONAL CALIBRATION (T173 P5/P8).
    h D = alpha holds per cell (frame B's defining rule, checked to 1e-10),
    hence log D = log alpha - log h POINTWISE, hence for ANY leg through the
    surface the two OLS slopes against log h obey q = 1 - s EXACTLY (OLS is
    linear in its response) -- T171's h^{-3} is the q = 1 idealisation of a
    Theta(D^3) law, as an identity and not as a fit.  The CALIBRATION, gauge-
    sorted: the measured gauge degrees (d_amp, d_mu) come out as INTEGERS --
    the delivery 1 - r_12^2 and the relative gap G2 = t/lam_max(B_LL) both
    at (0, 0), the absolute gap G1 = mu^P_1 t at d_amp = 1, the mu-weighted
    G3 = mu^P_1 G2 at d_mu = 1 -- so G2 is the unique doubly-gauge-invariant
    arithmetic member of T173's family; G3 = mu^P_1 G2 IDENTICALLY (so the
    G3-G2 offset is exactly the mu^P_1 exponent, measured -2 up to the
    discrete (2h+1) correction -- T173's "offset exactly 2" explained); and
    G6 = (D/alpha)^3 satisfies G6 h^3 = 1 IDENTICALLY (a tautology: a frame-
    independent demand carries zero information about frame dependence).
[E] (3) THE BLINDNESS THEOREMS (T174 P9/P10).  AMPLITUDE: A_h is linear in
    the lag vector c and both functionals are homogeneous of degree zero, so
    c -> kap c is a gauge of GAP, of 1 - r_12^2 and of R = GAP/(1 - r_12^2)
    -- checked over twelve decades against per-cell CONDITIONED round-off
    bars, and rebuilt from scratch.  THE mu^P_1 CHANNEL: the relative gap is
    invariant under S -> cs S (scalar congruence) and the delivery under the
    FULL positive diagonal group, so the scalar mu^P_1 = 4 sin^2(pi/(2h+1))
    -- the entire h^{-2} channel of the demand -- cancels EXACTLY on both
    sides and is not part of the deficit at all.  THE ASYMMETRY: a NON-scalar
    diagonal congruence moves the demand while the delivery stays at
    round-off -- the demand keeps the SHAPE of the KMS ladder, and that
    asymmetry is the whole anatomy of the cancellation.  THE ADDITIVE LIMIT
    (T174, the honest boundary): Ahat = Ahat_arch + Ahat_comb is ADDITIVE,
    and NEITHER term alone has a positive-definite low block on a single
    cell while the sum has one on every cell -- no factorisation
    Ahat = (frame) x (arithmetic) exists, so the gauge route STOPS here:
    the multiplicative half of T173's P6 is theorem-form, the mixture half
    is not, and P6 as a whole is NOT promoted to a theorem.
[E] (4) THE KMS SHAPE BAND (T174 P11; UNCONDITIONAL, with declared epsilon).
    The one channel the two sides do not share is the SHAPE
    Shat_k = mu^P_k/mu^P_1 against its universal k^2 limit.  With
    x = pi/(2h+1) and K = 16 the elementary two-sided sine bound gives
    |sqrt(Shat_k/k^2) - 1| <= eps_cert = (K x)^2/6, hence |log GAP(k^2) -
    log GAP(KMS)| <= 2 log((1+eps)/(1-eps)) for a PSD block (Rayleigh;
    Schur 1917) -- an unconditional, h-explicit band, checked per cell, with
    the delivery exactly blind (item 3).
[E] (5) THE PLACEMENT DISCRIMINATOR (T172 P4 / T174).  Replacing the
    prime-power positions u_n = log n by sorted uniform samples at the SAME
    Lambda-value multiset destroys the positive low block on EVERY declared
    draw and moves the ratio R by orders of magnitude: the demand side is a
    statement about WHERE the prime powers are, not about how many there
    are -- no scrambled comb reproduces the object.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   Per-instance identities and certified inequalities on a SMALL
        declared surface: a 4 x 3 (anchor, h) rectangle of gap-blind frame-B
        cells with the comb COMPLETE on every cell (X = n_zone^2 <= the
        sieve cap), one non-prime-power instance, one truncated-comb stress
        instance.  A FINITE LIST with an explicit maximum; NOTHING uniform
        in the zone index or in D, and NO statement for ALL D.
  (ii)  THE FRAME-FREE DEFICIT IS A MEASUREMENT, NOT A CLAIM OF THIS MODULE.
        T174's rectangle measurement -- DEFICIT(frame-free, dens >= 3.0) =
        +0.1111 +- 0.0222 (5.0 sigma, 151 anchor clusters, cluster-robust),
        agreeing with T173's frame-rule value +0.155 +- 0.102 at 0.4 sigma
        -- is a sandbox MEASURED number on T174's large surface and is NOT
        consumed here; the same holds for every T172/T173/T174 h-exponent
        and for the comb-density anatomy (the deficit falls +0.281 ->
        +0.062 across the density cuts; log nu collinear with log dens at
        r = -0.921 on legs).  What IS consumed is the identity structure
        that makes those measurements well-typed.
  (iii) THE ONE OPEN PHASE-2 OBJECT STAYS OPEN AND TYPED OPEN -- R1: an
        m-free unconditional certificate that two explicit finite
        Lambda-sum vectors become collinear at the demanded rate, now
        stated frame-free (T173/T174).  The quantifier is OPEN; T174's
        residual per-anchor scatter (chi^2/dof = 3.02 across the dense
        anchors) and the sparse-corner question are sandbox items.  P6
        (D-rule invariance) is NOT a theorem -- only its multiplicative
        half is (item 3) -- and it is less load-bearing after T174: the
        deficit is measured on a D-rule-free surface.
  (iv)  Finite Lambda-sums are allowed and nothing else: kappa = 0.038821
        is verified at every jump point of psi(x)/x on the finite table --
        the ONE unconditional arithmetic input.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE, VERBATIM FROM T174.  RH_DELTA = 0.5 is a YARDSTICK for
    translating a precision demand into an exponent, in exactly one role.
    A cancellation identity between two finite functionals of a finite
    matrix is a statement about FINITE MATRICES; it is not an RH statement,
    it does not assume RH, no zero of any L-function is read, generated or
    approximated (AST firewall), no L-function is evaluated, and no gauge
    theorem in this module may be read as closing the open quantifier at
    link 16.
  * THE WEIL FENCE.  Positivity of a finite A_h is never routed through the
    Weil criterion (Weil 1952); the audited chain is the R4-free R1 form of
    T171/T172/T173, and positive definiteness of the small blocks here is a
    numerical fact about finite matrices.
  * Classics named CLASSICAL: Schur 1917 (complements and congruence),
    Kac-Murdock-Szego 1953 (the sine eigenbasis and mu^P_k), Dirichlet 1829
    (the closed kernel and the odd reflection), Rayleigh 1877 (the
    congruence bounds of the shape band), Abel 1826 (the lag-sum swap),
    Chebyshev 1852 / Rosser-Schoenfeld 1962 (the one unconditional input,
    verified on the table), Wilkinson 1968 / Higham 2002 (floating-point
    floors and the conditioned bars); Weil 1952 / Bombieri 2000 CITED,
    never used as a criterion.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime side
    is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name; theorem-form cores typed THEOREM in the check text,
the unconditional band typed CERT, measured quantities typed MEASURED and
not consumed; mutation controls fail loudly.  Python; Wolfram-mirrored not
required (dense linear-algebra machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/frame_beyond_probe.py            (T172)
  experiments/tfpt-discovery/frame_rate_probe.py              (T173)
  experiments/tfpt-discovery/cancellation_identity_probe.py   (T174)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
ATOM_MAX = 320000            # atom table cap, as in v546..v559
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

KB_MAX = 32                  # parity modes carried
SCHUR_KB = 16                # the low block of the T152..T174 chain
EPSM = float(np.finfo(float).eps)

# --- the declared surface (fixed BEFORE any number) ---------------------------
N_ANCHOR = 4                 # prime-power anchors, geometrically spaced
ANCHOR_LO, ANCHOR_HI = 40, 560   # n_zone^2 = X <= ATOM_MAX: comb COMPLETE
H_LADDER = (160, 226, 320)   # the declared geometric h ladder (frame B rule)
NPP_ANCHOR = 210             # 2*3*5*7 -- Lambda(210) = 0: NOT a prime power
NPP_H = 226
TRUNC_ANCHOR = 1009          # prime; X = 1.018e6 > ATOM_MAX: comb CUT (T172)
TRUNC_H = 320

# --- the Chebyshev input, preregistered (T162..T174) --------------------------
KAPPA_X0 = 100.0
KAPPA_REF = 0.038821
TOL_KAPPA = 1.0e-6

# --- the ledger exponents (YARDSTICKS, not claims) -----------------------------
RH_DELTA = 0.5               # RH-equivalent strength, a YARDSTICK only
T174_DEFICIT = 0.1111        # T174 frame-free deficit -- sandbox MEASURED,
T174_DEFICIT_SE = 0.0222     # quoted for documentation, NOT consumed

# --- preregistered tolerances / bars (declared BEFORE any number) --------------
TOL_EXACT = 1.0e-12          # small-matrix identities (2x2 .. 32x32)
TOL_KMS = 1.0e-11            # T L_P T^T = diag(mu), 32 modes, absolute
TOL_QF = 1.0e-10             # quadratic-form pair, relative
TOL_LAGSUM = 1.0e-12         # lag-sum identity, relative to the LARGER half
TOL_SCALE = 1.0e-10          # h D = alpha per cell
TOL_OLS = 1.0e-12            # q = 1 - s as an OLS identity
TOL_DEG = 1.0e-2             # measured gauge degrees vs their integers
BAR_SAFE = 64.0              # declared safety factor on a conditioned bar
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
BAR_ASYM = 1.0e-2            # a NON-scalar diagonal must move the demand
BAR_MUT = 1.0e-2             # every mutation must miss by at least this
BAR_SCRAM_MED = 1.0e2        # median |R| move under the scramble
CAP_SCRAM = 1.0e6            # declared REPORTING cap on a single move
N_SCRAM = 2                  # scramble draws per cell, declared (12 x 2 = 24)
TOL_CTRL = 1.0e-12           # Dirichlet / parity / Toeplitz controls
SEED = 560


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
    """kappa = max over jump points x in [KAPPA_X0, ATOM_MAX] of
    |psi(x) - x| / x (Chebyshev 1852 / Rosser-Schoenfeld 1962) -- the ONE
    unconditional arithmetic input, measured on THIS table and nothing
    else."""
    nn = _NN.astype(float)
    psi = np.cumsum(LAM_TAB[_NN])
    keep = nn >= KAPPA_X0
    return float(np.max(np.abs(psi[keep] - nn[keep]) / nn[keep]))


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


def lap_P_mat(m):
    L = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    L[m - 1, m - 1] = 3.0
    return L


_IDX = {}


def toeplitz_index(M):
    if M not in _IDX:
        h = M // 2
        rr = np.arange(h)
        _IDX[M] = (np.abs(rr[:, None] - rr[None, :]),
                   (M - 1) - rr[:, None] - rr[None, :])
    return _IDX[M]


def odd_toeplitz(c, M):
    it, ih = toeplitz_index(M)
    return np.asarray(c)[it] - np.asarray(c)[ih]


def atom_lags_at(alpha, M, u, mu):
    """The T115 tent assembly at EXPLICIT positions (vectorised) -- used at
    the true von-Mangoldt positions and, in item (5), at scrambled uniform
    positions with the SAME masses."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    u = np.asarray(u, dtype=float)
    mu = np.asarray(mu, dtype=float)
    i0 = np.floor(u / D).astype(np.int64)
    for off in (-2, -1, 0, 1, 2):
        idx = i0 + off
        ok = (idx >= 0) & (idx < M)
        v = 1.0 - np.abs(idx[ok] * D - u[ok]) / D
        pos = v > 0.0
        np.add.at(c, idx[ok][pos], -mu[ok][pos] * 0.5 * v[pos])
    refl = u < D
    if refl.any():
        v = 1.0 - u[refl] / D
        pos = v > 0.0
        np.add.at(c, np.zeros(int(pos.sum()), dtype=np.int64),
                  -mu[refl][pos] * 0.5 * v[pos])
    return c, D


# ------------------- the two functionals of ONE raw Gram (T173/T174)
def gap_of(Ahat, prof, kb=SCHUR_KB):
    """REQ side: lam_min and lam_max of B_LL = S^{-1/2} Ahat_LL S^{-1/2}."""
    isq = 1.0 / np.sqrt(np.asarray(prof, dtype=float)[:kb])
    ev = np.linalg.eigvalsh(sym(Ahat[:kb, :kb] * np.outer(isq, isq)))
    return float(ev[0]), float(ev[-1])


def del_of(Ahat):
    """DEL side: 1 - r_12^2 = det Ahat_2 / (a11 a22), the 2 x 2 corner of
    the very same Gram."""
    a11, a12, a22 = float(Ahat[0, 0]), float(Ahat[0, 1]), float(Ahat[1, 1])
    det = a11 * a22 - a12 * a12
    return det / (a11 * a22), det, a11, a12, a22


def lag_weights_from_v(v, m):
    """w_0 = A_0, w_d = 2 A_d - H_{M-1-d} (d >= 1): v^T A_h v = sum c_d w_d
    EXACTLY (the T163 correlation theorem; Abel 1826)."""
    M = 2 * m
    ac = np.correlate(v, v, "full")[m - 1:]
    cv = np.convolve(v, v)
    w = np.zeros(M)
    w[:m] = 2.0 * ac
    w[0] = ac[0]
    ee = (M - 1) - np.arange(1, M)
    w[1:] -= np.where(ee <= M - 2, cv[np.minimum(ee, M - 2)], 0.0)
    return w


UNIV = np.arange(1.0, KB_MAX + 1.0) ** 2       # the universal k^2 profile


def eps_cert(h):
    """The declared epsilon of the unconditional KMS-shape band (T174)."""
    x = math.pi / (2.0 * h + 1.0)
    return (SCHUR_KB * x) ** 2 / 6.0


def log_band(eps):
    return 2.0 * math.log((1.0 + eps) / (1.0 - eps))


def build_cell(n_zone, h):
    """ONE gap-blind frame-B cell.  THE SIGNATURE IS THE POINT (T174 P12):
    the builder sees (n_zone, alpha, M) and nothing about any frame label,
    so no frame provenance can leak into an observable."""
    alpha = math.log(float(n_zone))
    M = 2 * h
    ka = atoms_in(alpha)
    c_at, D = atom_lags_at(alpha, M, U_ALL[:ka], MU_ALL[:ka])
    c_ar = arch_lags(M, D)
    Tb = parity_basis(h, KB_MAX)
    mu = parity_mu(h)[:KB_MAX]
    Ah = sym(Tb @ (odd_toeplitz(c_ar + c_at, M) @ Tb.T))
    r = dict(n=n_zone, alpha=alpha, h=h, M=M, D=D, n_atom=ka,
             X=math.exp(2.0 * alpha), c=c_ar + c_at, c_ar=c_ar, c_at=c_at,
             Tb=Tb, mu=mu, Ah=Ah,
             Ah_ar=sym(Tb @ (odd_toeplitz(c_ar, M) @ Tb.T)),
             Ah_at=sym(Tb @ (odd_toeplitz(c_at, M) @ Tb.T)))
    r["lmin"], r["lmax"] = gap_of(Ah, mu)
    r["GAP"] = r["lmin"] / r["lmax"]
    r["pd"] = bool(r["lmin"] > 0.0)
    r["cond"] = abs(r["lmax"] / max(abs(r["lmin"]), 1.0e-300))
    r["DEL"] = del_of(Ah)[0]
    r["R"] = r["GAP"] / max(abs(r["DEL"]), 1.0e-300)
    r["complete"] = bool(float(n_zone) ** 2 <= float(ATOM_MAX) + 0.5)
    return r


def bar_gap(r):
    """Conditioned bar on a gap identity: BAR_SAFE * eps * cond(B_LL) per
    cell (Wilkinson 1968 / Higham 2002) -- declared, not wished away."""
    return BAR_SAFE * EPSM * r["cond"]


def bar_del(r):
    """Conditioned bar on a delivery identity: BAR_SAFE * eps / |1-r12^2|."""
    return BAR_SAFE * EPSM / abs(r["DEL"])


def transfer_links(r, rng):
    """The four T172-transfer identity links on ONE instance; returns the
    worst residuals (KMS, quadratic pair, lag sum, det collapse, additive
    split).  None of these uses positivity of the block."""
    h, M = r["h"], r["M"]
    LP = lap_P_mat(h)
    e_kms = float(np.max(np.abs(r["Tb"] @ (LP @ r["Tb"].T)
                                - np.diag(r["mu"]))))
    A_h = odd_toeplitz(r["c"], M)
    x = rng.standard_normal(KB_MAX)
    a = x / np.sqrt(r["mu"])
    v = r["Tb"].T @ a
    isq = 1.0 / np.sqrt(r["mu"])
    G = sym(r["Ah"] * np.outer(isq, isq))
    qg = float(x @ (G @ x))
    qa = float(v @ (A_h @ v))
    e_qf = max(abs(qg - qa) / max(1.0, abs(qa)),
               abs(float(x @ x) - float(v @ (LP @ v))) / float(x @ x))
    w = lag_weights_from_v(v, h)
    big = max(abs(float(r["c_ar"] @ w)), abs(float(r["c_at"] @ w)))
    e_lag = abs(float(r["c"] @ w) - qa) / max(big, 1.0e-300)
    dl, det, a11, a12, a22 = del_of(r["Ah"])
    bar = BAR_SAFE * EPSM / abs(dl)      # the det is a NEAR-NULL number:
    #                                      the honest bar is conditioned
    nu = np.linalg.eigvalsh(r["Ah"][:2, :2])
    e_nu = (abs(float(nu[0] * nu[1]) - det) / max(abs(det), 1.0e-300)
            / bar)
    e_g2 = (abs(float(G[0, 0] * G[1, 1] - G[0, 1] ** 2)
                / float(G[0, 0] * G[1, 1]) - dl)
            / max(abs(dl), 1.0e-300) / bar)
    e_add = (float(np.max(np.abs(r["Ah"] - (r["Ah_ar"] + r["Ah_at"]))))
             / float(np.max(np.abs(r["Ah"]))))
    return e_kms, e_qf, e_lag, max(e_nu, e_g2), e_add, w, v, qa


def ols_slope(lx, ly):
    lx = np.asarray(lx, dtype=float)
    ly = np.asarray(ly, dtype=float)
    xc = lx - lx.mean()
    return float(np.sum(xc * ly) / np.sum(xc * xc))


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("=" * 72)
    print("v560  PRIME.FRAME.DEFICIT.01 -- the frame / deficit identities "
          "(T172+T173+T174)")
    print("=" * 72)

    # ================================================================ S0
    print("\nS0 -- firewall, the one arithmetic input, the declared surface")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    kappa = chebyshev_kappa()
    pp = [int(n) for n in _NN if ANCHOR_LO <= n <= ANCHOR_HI]
    tgt = np.geomspace(float(pp[0]), float(pp[-1]), N_ANCHOR)
    anchors = sorted(set(min(pp, key=lambda n, t=t: abs(math.log(n)
                                                        - math.log(t)))
                         for t in tgt))
    CELLS = [build_cell(n, h) for n in anchors for h in H_LADDER]
    e_scale = max(abs(r["h"] * r["D"] - r["alpha"]) for r in CELLS)
    check(f"S0.SURFACE: kappa = {kappa:.6f} reproduced to "
          f"{abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} at every jump "
          f"point of the von-Mangoldt table in [{KAPPA_X0:.0f}, {ATOM_MAX}] "
          f"(Chebyshev 1852 / Rosser-Schoenfeld 1962 -- the ONE "
          f"unconditional arithmetic input); the declared rectangle is "
          f"{len(anchors)} prime-power anchors n = {anchors} crossed with "
          f"the declared ladder h = {list(H_LADDER)} = {len(CELLS)} "
          f"gap-blind frame-B cells, ALL with a complete comb "
          f"(X = n^2 <= {ATOM_MAX}), h D = alpha to {e_scale:.1e} <= "
          f"{TOL_SCALE:.0e}, positive definite low block on "
          f"{sum(r['pd'] for r in CELLS)}/{len(CELLS)} with cond(B_LL) <= "
          f"{max(r['cond'] for r in CELLS):.1e} <= {COND_BAR:.0e} (the "
          f"declared T159 horizon).  The builder's signature is "
          f"(n_zone, alpha, M): no frame label is an argument of any "
          f"observable (T174 P12)",
          abs(kappa - KAPPA_REF) <= TOL_KAPPA
          and len(CELLS) == N_ANCHOR * len(H_LADDER)
          and all(r["pd"] and r["complete"] for r in CELLS)
          and e_scale <= TOL_SCALE
          and max(r["cond"] for r in CELLS) <= COND_BAR)
    for r in CELLS:
        print(f"    n={r['n']:>4d} h={r['h']:>4d} atoms={r['n_atom']:>6d} "
              f"GAP={r['GAP']:9.3e} 1-r12^2={r['DEL']:9.3e} "
              f"R={r['R']:9.3e}")
    r_npp = build_cell(NPP_ANCHOR, NPP_H)
    r_trunc = build_cell(TRUNC_ANCHOR, TRUNC_H)
    check(f"S0.BEYOND: two beyond-frame-A instances built on the SAME "
          f"builder -- a NON-PRIME-POWER anchor n = {NPP_ANCHOR} "
          f"(Lambda({NPP_ANCHOR}) = 0; h = {NPP_H}, {r_npp['n_atom']} "
          f"atoms, comb complete) and a TRUNCATED-COMB stress instance "
          f"n = {TRUNC_ANCHOR} (h = {TRUNC_H}; X = {r_trunc['X']:.3e} > "
          f"{ATOM_MAX} = sieve cap, so the comb is CUT -- declared out "
          f"loud, this is T172's sieve-horizon mechanism, not a bug)",
          LAM_TAB[NPP_ANCHOR] == 0.0 and r_npp["complete"]
          and not r_trunc["complete"])

    # ================================================================ S1
    print("\nS1 -- the identity transfer (T172 P1) + the sieve-horizon "
          "discriminator (T172 P2)")
    tr_b = transfer_links(CELLS[len(CELLS) // 2], rng)
    tr_n = transfer_links(r_npp, rng)
    tr_t = transfer_links(r_trunc, rng)
    check(f"S1.KMS [THEOREM] T152/T172 link 1 on BOTH beyond-frame-A "
          f"instances: T L_P T^T = diag(mu^P) to "
          f"{max(tr_b[0], tr_n[0]):.1e} <= {TOL_KMS:.0e} (KMS 1953, exact "
          f"closed form) and the quadratic-form pair x^T G x = v^T A_h v, "
          f"x^T x = v^T L_P v to {max(tr_b[1], tr_n[1]):.1e} <= "
          f"{TOL_QF:.0e} -- the link uses no property of the frame rule or "
          f"the anchor arithmetic, which is WHY it transfers (T172's four "
          f"surfaces are the evidence; the derivation is the reason)",
          max(tr_b[0], tr_n[0]) <= TOL_KMS
          and max(tr_b[1], tr_n[1]) <= TOL_QF)
    check(f"S1.LAGSUM [THEOREM] T163/T172 link 8 (the most zone-sensitive "
          f"link): v^T A_h v = sum_d c_d w_d with the closed correlation "
          f"weights, to {max(tr_b[2], tr_n[2]):.1e} <= {TOL_LAGSUM:.0e} of "
          f"the LARGER (arch/comb) half on the frame-B and the "
          f"non-prime-power instance (Abel 1826) -- the anchor arithmetic "
          f"decides WHERE the atom combs sit on the grid, and the identity "
          f"is untouched", max(tr_b[2], tr_n[2]) <= TOL_LAGSUM)
    check(f"S1.DETCOLLAPSE [THEOREM] T169/T170 link 14, R4-FREE: "
          f"1 - r_12^2 = det Ahat_2/(a11 a22) = nu_1 nu_2/(a11 a22) = "
          f"det G_2/(G_11 G_22) at a worst ratio {max(tr_b[3], tr_n[3]):.3f}"
          f" < 1 of the CONDITIONED bar {BAR_SAFE:.0f} eps / |1 - r_12^2| "
          f"on both instances (the 2 x 2 determinant is a near-null "
          f"number: 'exact' means 'at round-off for this cancellation', "
          f"Wilkinson 1968 / Higham 2002) -- identities using NO "
          f"positivity of A_h: the chain is R4-free and the Weil fence "
          f"(Weil 1952) is never approached",
          max(tr_b[3], tr_n[3]) < 1.0)
    check(f"S1.ADDSPLIT [THEOREM] T174 C1.4: Ahat = Ahat_arch + Ahat_comb "
          f"to {max(tr_b[4], tr_n[4]):.1e} <= {TOL_EXACT:.0e} relative on "
          f"both instances (linearity of the odd Toeplitz-minus-Hankel "
          f"form in the lag vector c; Dirichlet 1829) -- EXACT, and "
          f"ADDITIVE: which is precisely why it is not a gauge (item S3)",
          max(tr_b[4], tr_n[4]) <= TOL_EXACT)
    check(f"S1.HORIZON [THEOREM+CERT] THE SIEVE-HORIZON DISCRIMINATOR "
          f"(T172 P2): the truncated-comb instance (n = {TRUNC_ANCHOR}, "
          f"comb cut at the sieve cap while the grid runs to "
          f"X = e^(2 alpha)) has an INDEFINITE low block, lam_min = "
          f"{r_trunc['lmin']:.3e} < 0, against {sum(r['pd'] for r in CELLS)}"
          f"/{len(CELLS)} positive definite complete-comb cells -- "
          f"indefiniteness is located at the DECLARED sieve horizon, not "
          f"at a frame or a zone family (T171's open worry, retired) -- "
          f"AND the identity links keep holding there: lag sum "
          f"{tr_t[2]:.1e} <= {TOL_LAGSUM:.0e}, det collapse at "
          f"{tr_t[3]:.3f} of its conditioned bar, additive split "
          f"{tr_t[4]:.1e} <= {TOL_EXACT:.0e} -- because none of them uses "
          f"positivity",
          r_trunc["lmin"] < 0.0 and all(r["pd"] for r in CELLS)
          and tr_t[2] <= TOL_LAGSUM and tr_t[3] < 1.0
          and tr_t[4] <= TOL_EXACT)
    # mutations: off-by-one edge in the correlation weights; wrong-N ladder
    r0 = CELLS[len(CELLS) // 2]
    _, _, _, _, _, w0, v0, qa0 = transfer_links(r0, rng)
    w_bad = w0.copy()
    w_bad[0] = 2.0 * w_bad[0]        # drop the d = 0 halving
    m_lag = abs(float(r0["c"] @ w_bad) - qa0) / max(abs(qa0), 1.0e-300)
    mu_bad = 4.0 * np.sin(math.pi * np.arange(1, KB_MAX + 1)
                          / (2.0 * r0["h"])) ** 2   # N = 2h, NOT 2h+1
    LP0 = lap_P_mat(r0["h"])
    m_kms = float(np.max(np.abs(r0["Tb"] @ (LP0 @ r0["Tb"].T)
                                - np.diag(mu_bad))))
    check(f"S1.MUT: the correlation weights with the d = 0 halving dropped "
          f"miss the lag-sum identity by {m_lag:.2e} >= {BAR_MUT:.0e} "
          f"relative, and the KMS ladder built with N = 2h instead of "
          f"N = 2h + 1 misses T L_P T^T = diag(mu) by {m_kms:.2e} >= "
          f"1e-5 absolute: the transfer identities are statements about "
          f"THE objects, not generic algebra",
          m_lag >= BAR_MUT and m_kms >= 1.0e-5)

    # ================================================================ S2
    print("\nS2 -- the q = 1 - s identity + the gap-functional calibration "
          "(T173 P5/P8)")
    # a declared diagonal leg through the rectangle: anchor i with rung i%3
    leg = [CELLS[i * len(H_LADDER) + (i % len(H_LADDER))]
           for i in range(N_ANCHOR)]
    lh = [math.log(r["h"]) for r in leg]
    s_slope = ols_slope(lh, [math.log(r["alpha"]) for r in leg])
    q_slope = -ols_slope(lh, [math.log(r["D"]) for r in leg])
    e_q = abs(q_slope - (1.0 - s_slope))
    check(f"S2.QIDENT [THEOREM] T173's key identity: h D = alpha per cell "
          f"(<= {e_scale:.1e}, item S0) forces log D = log alpha - log h "
          f"POINTWISE, hence on the declared diagonal leg the OLS slopes "
          f"obey q = 1 - s to {e_q:.1e} <= {TOL_OLS:.0e} (q = "
          f"{q_slope:+.4f}, s = {s_slope:+.4f}; OLS is linear in its "
          f"response, so the identity lifts from cells to slopes) -- "
          f"T171's h^-3 is the q = 1 idealisation of a Theta(D^3) law, as "
          f"an IDENTITY and never as a fit; the T173 values q = "
          f"0.667..0.777 on the eleven frame legs stay sandbox MEASURED",
          e_q <= TOL_OLS)
    # gauge degrees, measured as integers (T173 P8 / T174 C1.5)
    KAPS = (1.0e-6, math.pi, 1.0e6)
    CSS = (1.0e-4, 7.0, 1.0e4)

    def fam(r, kap=1.0, cs=1.0):
        Ah = kap * r["Ah"]
        pf = cs * r["mu"]
        l1, l2 = gap_of(Ah, pf)
        m1 = float(pf[0])
        return dict(G1=m1 * l1, G2=l1 / l2, G3=m1 * l1 / l2,
                    DEL=del_of(Ah)[0])

    def degree(r, key, knob):
        vals = [(math.log(k), math.log(abs(fam(r, **{knob: k})[key])))
                for k in (KAPS if knob == "kap" else CSS)]
        return ols_slope([v[0] for v in vals], [v[1] for v in vals])

    d_amp_g2 = max(abs(degree(r, "G2", "kap")) for r in leg)
    d_amp_del = max(abs(degree(r, "DEL", "kap")) for r in leg)
    d_mu_g2 = max(abs(degree(r, "G2", "cs")) for r in leg)
    d_mu_del = max(abs(degree(r, "DEL", "cs")) for r in leg)
    d_amp_g1 = max(abs(degree(r, "G1", "kap") - 1.0) for r in leg)
    d_mu_g3 = max(abs(degree(r, "G3", "cs") - 1.0) for r in leg)
    check(f"S2.DEGREES [THEOREM] the gauge-degree account of T173's "
          f"functional family, measured over twelve (amplitude) and eight "
          f"(mu-scalar) decades and coming out as INTEGERS: the relative "
          f"gap G2 = t/lam_max(B_LL) and the delivery 1 - r_12^2 both have "
          f"(d_amp, d_mu) = (0, 0) (worst |d| = "
          f"{max(d_amp_g2, d_amp_del, d_mu_g2, d_mu_del):.1e} <= "
          f"{TOL_DEG:.0e}), while G1 = mu^P_1 t has d_amp = 1 and "
          f"G3 = mu^P_1 G2 has d_mu = 1 (worst |d - 1| = "
          f"{max(d_amp_g1, d_mu_g3):.1e}) -- G2 is the unique doubly-"
          f"gauge-invariant ARITHMETIC member of the family: the "
          f"dimensional argument and the numerical calibration were forced "
          f"to pick the same functional (T173 P8)",
          max(d_amp_g2, d_amp_del, d_mu_g2, d_mu_del) <= TOL_DEG
          and max(d_amp_g1, d_mu_g3) <= TOL_DEG)
    e_g3 = max(abs(fam(r)["G3"] / (float(r["mu"][0]) * fam(r)["G2"]) - 1.0)
               for r in CELLS)
    e_mu1 = max(abs(float(r["mu"][0])
                    - 4.0 * math.sin(math.pi / (2.0 * r["h"] + 1.0)) ** 2)
                for r in CELLS)
    sl_mu1 = ols_slope([math.log(r["h"]) for r in CELLS],
                       [math.log(float(r["mu"][0])) for r in CELLS])
    check(f"S2.G3OFFSET [THEOREM] G3 = mu^P_1 G2 IDENTICALLY (to "
          f"{e_g3:.1e} <= {TOL_EXACT:.0e} on {len(CELLS)}/{len(CELLS)} "
          f"cells), mu^P_1 = 4 sin^2(pi/(2h+1)) reproduced to {e_mu1:.1e} "
          f"(KMS 1953, exact closed form) with measured exponent "
          f"h^{sl_mu1:+.4f} = -2 up to the discrete (2h+1) correction "
          f"(|slope + 2| = {abs(sl_mu1 + 2.0):.4f} <= 0.01 over the "
          f"declared 2x lever) -- T173's 'G3-G2 offset exactly 2' "
          f"(measured 1.9974) is EXPLAINED: G3 differs from G2 by exactly "
          f"the mu^P_1 factor and by nothing else, because G2 is "
          f"mu^P_1-blind (item S3)",
          e_g3 <= TOL_EXACT and e_mu1 <= TOL_EXACT
          and abs(sl_mu1 + 2.0) <= 0.01)
    e_g6 = max(abs((r["D"] / r["alpha"]) ** 3 * float(r["h"]) ** 3 - 1.0)
               for r in CELLS)
    check(f"S2.G6TAUT [THEOREM] the G6 tautology: (D/alpha)^3 h^3 = 1 to "
          f"{e_g6:.1e} <= {TOL_EXACT:.0e} on {len(CELLS)}/{len(CELLS)} "
          f"cells -- G6 = (D/alpha)^3 is EXACTLY h^-3 given h D = alpha, "
          f"zero scatter and zero arithmetic: a frame-independent demand "
          f"subtracts a constant and can measure NOTHING about frame "
          f"dependence (T173's tautology finding, as an identity)",
          e_g6 <= TOL_EXACT)
    m_q = max(abs((r["h"] + 1) * r["D"] - r["alpha"]) / r["alpha"]
              for r in leg)
    check(f"S2.MUT: the scale identity read with an off-by-one h misses "
          f"h D = alpha by {m_q:.2e} >= 1e-3 relative on every leg cell "
          f"(the break is exactly 1/h), and the mu ladder with the wrong N "
          f"misses by {m_kms:.2e} (item S1): the q = 1 - s identity is a "
          f"statement about the BUILT window, not about any pair of "
          f"numbers", m_q >= 1.0e-3)

    # ================================================================ S3
    print("\nS3 -- the blindness theorems (T174 P9/P10) + the additive "
          "limit")
    E_AMP, E_REB = [], []
    for r in CELLS:
        b = fam(r)
        bg, bd = bar_gap(r), bar_del(r)
        for k in KAPS:
            g = fam(r, kap=k)
            E_AMP.append(max(abs(g["G2"] / b["G2"] - 1.0) / bg,
                             abs(g["DEL"] / b["DEL"] - 1.0) / bd,
                             abs((g["G2"] / abs(g["DEL"]))
                                 / (b["G2"] / abs(b["DEL"])) - 1.0)
                             / (bg + bd)))
    for k in KAPS:
        Ah = sym(r0["Tb"] @ (odd_toeplitz(k * r0["c"], r0["M"])
                             @ r0["Tb"].T))
        l1, l2 = gap_of(Ah, r0["mu"])
        E_REB.append(max(abs(l1 / l2 / r0["GAP"] - 1.0) / bar_gap(r0),
                         abs(del_of(Ah)[0] / r0["DEL"] - 1.0)
                         / bar_del(r0)))
    check(f"S3.AMPLITUDE [THEOREM] T174 P9, gauge one: c -> kap c over "
          f"twelve decades (kap = 1e-6, pi, 1e6) leaves GAP, 1 - r_12^2 "
          f"and R = GAP/(1 - r_12^2) unchanged BELOW each cell's own "
          f"conditioned round-off bar (worst ratio to bar "
          f"{max(E_AMP):.3f} < 1 over {len(E_AMP)} (cell, kap) pairs; "
          f"bars = {BAR_SAFE:.0f} eps cond(B_LL) resp. {BAR_SAFE:.0f} eps "
          f"/ |1 - r_12^2|, Wilkinson 1968 / Higham 2002); REBUILT FROM "
          f"SCRATCH (odd Toeplitz re-assembled from kap c) the worst "
          f"ratio is {max(E_REB):.3f} < 1.  A_h is linear in c and both "
          f"functionals are homogeneous of degree zero: THEOREM, the "
          f"check is a check", max(E_AMP) < 1.0 and max(E_REB) < 1.0)
    E_MU, E_M1 = [], []
    for r in CELLS:
        b = fam(r)
        bg = bar_gap(r)
        for cs in CSS:
            E_MU.append(abs(fam(r, cs=cs)["G2"] / b["G2"] - 1.0) / bg)
        l1, l2 = gap_of(r["Ah"], r["mu"] / float(r["mu"][0]))
        E_M1.append(abs(l1 / l2 / b["G2"] - 1.0) / bg)
    check(f"S3.MUCHANNEL [THEOREM] T174 P10, the load-bearing gauge: the "
          f"relative gap is invariant under mu -> cs mu over eight decades "
          f"(worst ratio to bar {max(E_MU):.3f} < 1) and dividing the KMS "
          f"ladder by mu^P_1 changes it by at most {max(E_M1):.3f} of its "
          f"bar -- THE ENTIRE h^-2 CHANNEL OF THE DEMAND (the scalar "
          f"mu^P_1, the one factor that is a pure function of the grid) "
          f"CANCELS EXACTLY in R and is not part of the deficit at all "
          f"(Schur 1917 congruence)", max(E_MU) < 1.0 and max(E_M1) < 1.0)
    E_DIAG, MOVE_GAP = [], []
    for r in CELLS:
        bd = bar_del(r)
        for _ in range(4):
            e2 = np.exp(rng.uniform(-8.0, 8.0, size=2))
            E_DIAG.append(abs(del_of(r["Ah"][:2, :2] * np.outer(e2, e2))[0]
                              / r["DEL"] - 1.0) / bd)
        e16 = np.exp(rng.uniform(-1.0, 1.0, size=SCHUR_KB))
        l1, l2 = gap_of(r["Ah"], r["mu"][:SCHUR_KB] / e16 ** 2)
        MOVE_GAP.append(abs((l1 / l2) / fam(r)["G2"] - 1.0))
    check(f"S3.ASYMMETRY [THEOREM] T174's anatomy: the delivery is "
          f"invariant under the FULL positive diagonal group ({len(E_DIAG)}"
          f" random congruences spanning e^-8..e^+8 per entry, worst ratio "
          f"to bar {max(E_DIAG):.3f} < 1 -- a correlation does not know "
          f"the units of its coordinates) while a NON-scalar diagonal "
          f"congruence moves the demand by {min(MOVE_GAP):.3f}.."
          f"{max(MOVE_GAP):.3f} >= {BAR_ASYM:.0e} on every cell: the "
          f"demand keeps the SHAPE of the KMS ladder, the delivery is "
          f"blind to it -- this asymmetry is the whole anatomy of the "
          f"cancellation, and it is algebra, not a fit",
          max(E_DIAG) < 1.0 and min(MOVE_GAP) >= BAR_ASYM)
    pd_ar = sum(1 for r in CELLS if gap_of(r["Ah_ar"], r["mu"])[0] > 0.0)
    pd_at = sum(1 for r in CELLS if gap_of(r["Ah_at"], r["mu"])[0] > 0.0)
    check(f"S3.NOFACTOR [THEOREM] the additive limit -- where the gauge "
          f"route STOPS: NEITHER the archimedean term ({pd_ar}/"
          f"{len(CELLS)} positive definite) NOR the comb term ({pd_at}/"
          f"{len(CELLS)}) has a positive definite low block on a single "
          f"cell, while their SUM has one on {sum(r['pd'] for r in CELLS)}"
          f"/{len(CELLS)}: the positive Schur floor is a property of the "
          f"MIXTURE alone, no factorisation Ahat = (frame) x (arithmetic) "
          f"exists, and T173's P6 (D-rule invariance) is therefore NOT "
          f"promoted to a theorem -- only its multiplicative half is "
          f"(S3.AMPLITUDE + S3.MUCHANNEL); the deficit itself no longer "
          f"needs an invariance argument: T174 measured it on a "
          f"D-rule-free surface (sandbox, not consumed)",
          pd_ar == 0 and pd_at == 0 and all(r["pd"] for r in CELLS))
    m_comb = []
    for r in (r0,):
        Ah = sym(r["Tb"] @ (odd_toeplitz(r["c_ar"] + 2.0 * r["c_at"],
                                         r["M"]) @ r["Tb"].T))
        l1, l2 = gap_of(Ah, r["mu"])
        Rm = (l1 / l2) / max(abs(del_of(Ah)[0]), 1.0e-300)
        m_comb.append(abs(Rm / r["R"] - 1.0))
    check(f"S3.MUT: rescaling ONLY the comb half (c_comb -> 2 c_comb, arch "
          f"unchanged) moves R by {max(m_comb):.2e} >= {BAR_MUT:.0e} -- an "
          f"additive-part rescaling is NOT a gauge, exactly as the "
          f"additive-limit theorem says; the gauge statements are about "
          f"the WHOLE lag vector", max(m_comb) >= BAR_MUT)

    # ================================================================ S4
    print("\nS4 -- the KMS shape band (T174 P11; unconditional, declared "
          "epsilon)")
    SH_OK, SH_RAT, DEL_BLIND = [], [], []
    for r in CELLS:
        e = eps_cert(r["h"])
        sh = r["mu"] / float(r["mu"][0])
        emeas = float(np.max(np.abs(
            np.sqrt(sh[:SCHUR_KB] / UNIV[:SCHUR_KB]) - 1.0)))
        SH_OK.append(emeas <= e + 1.0e-14)
        l1, l2 = gap_of(r["Ah"], UNIV)
        d = abs(math.log(abs(l1 / l2)) - math.log(r["GAP"]))
        SH_RAT.append(d / log_band(e))
        DEL_BLIND.append(abs(del_of(r["Ah"])[0] / r["DEL"] - 1.0))
    check(f"S4.SHAPEBAND [CERT, UNCONDITIONAL] the one surviving "
          f"multiplicative channel, bounded with a DECLARED epsilon: with "
          f"x = pi/(2h+1) and K = {SCHUR_KB} the elementary sine bounds "
          f"give |sqrt(Shat_k/k^2) - 1| <= eps_cert = (K x)^2/6 = "
          f"{min(eps_cert(r['h']) for r in CELLS):.2e}.."
          f"{max(eps_cert(r['h']) for r in CELLS):.2e} (holds on "
          f"{sum(SH_OK)}/{len(CELLS)} cells), and swapping the KMS ladder "
          f"for the universal k^2 profile moves log GAP by at most "
          f"{max(SH_RAT):.3f} of the certified band "
          f"2 log((1+eps)/(1-eps)) on every cell (Rayleigh 1877; Schur "
          f"1917 congruence bounds on a PSD block), while the delivery "
          f"does not move at all (worst {max(DEL_BLIND):.1e}, exact "
          f"blindness, S3) -- an unconditional h-explicit band, not a "
          f"fitted residual; T174's propagation of this band through the "
          f"OLS weights (<= 0.0075 in deficit units = 4.8% of T173's "
          f"+0.155) is a sandbox consequence on ITS declared ladder and "
          f"is not consumed here",
          all(SH_OK) and max(SH_RAT) < 1.0 and max(DEL_BLIND) < 1.0e-12)
    m_sh = []
    for r in leg:
        e = eps_cert(r["h"])
        wrong = np.arange(1.0, KB_MAX + 1.0)      # k, NOT k^2
        l1, l2 = gap_of(r["Ah"], wrong)
        m_sh.append(abs(math.log(abs(l1 / l2)) - math.log(r["GAP"]))
                    / log_band(e))
    check(f"S4.MUT: the WRONG universal profile (k instead of k^2) "
          f"overshoots the certified band by {min(m_sh):.1e}.."
          f"{max(m_sh):.1e} >= 10 on every leg cell: the band is a "
          f"statement about THE KMS shape against ITS limit, not a slack "
          f"that absorbs any profile", min(m_sh) >= 10.0)

    # ================================================================ S5
    print("\nS5 -- the placement discriminator (T172 P4 / T174) + exact "
          "controls")
    n_neg, MOVE_R = 0, []
    for r in CELLS:
        for _ in range(N_SCRAM):
            pos = np.sort(rng.uniform(1.0e-6, 2.0 * r["alpha"],
                                      size=r["n_atom"]))
            c_at_s, _ = atom_lags_at(r["alpha"], r["M"], pos,
                                     MU_ALL[:r["n_atom"]])
            Ah_s = sym(r["Tb"] @ (odd_toeplitz(r["c_ar"] + c_at_s, r["M"])
                                  @ r["Tb"].T))
            l1, l2 = gap_of(Ah_s, r["mu"])
            if l1 < 0.0:
                n_neg += 1
            R_s = (abs(l1) / l2) / max(abs(del_of(Ah_s)[0]), 1.0e-300)
            MOVE_R.append(min(CAP_SCRAM,
                              max(R_s / r["R"],
                                  r["R"] / max(R_s, 1.0e-300))))
    med_move = float(np.median(MOVE_R))
    check(f"S5.SCRAMBLE [MUST-BREAK] T172's placement finding, T174's "
          f"control: replacing the prime-power positions u_n = log n by "
          f"sorted uniform samples at the SAME Lambda-value multiset "
          f"({N_SCRAM} declared draws x {len(CELLS)} cells = "
          f"{len(MOVE_R)} draws) destroys the positive low block on "
          f"{n_neg}/{len(MOVE_R)} draws and moves |R| by a median factor "
          f"{med_move:.1e} >= {BAR_SCRAM_MED:.0e} (range "
          f"{min(MOVE_R):.2g}..{max(MOVE_R):.2g}, each move clipped at "
          f"the declared reporting cap {CAP_SCRAM:.0e}): the demand side "
          f"is a "
          f"statement about WHERE the prime powers are, not about how "
          f"many there are -- no scrambled comb reproduces the object "
          f"whose deficit T173/T174 measured",
          n_neg == len(MOVE_R) and med_move >= BAR_SCRAM_MED)
    rng2 = np.random.default_rng(5601)
    worst_cs = 0.0
    for _ in range(64):
        al = float(rng2.uniform(0.05, 3.0))
        be = float(rng2.uniform(0.0, 2.0 * math.pi))
        Lc = int(rng2.integers(1, 40))
        brute = float(np.sum(np.cos(al * np.arange(1, Lc + 1) + be)))
        ha = 0.5 * al
        closed = (math.sin(Lc * ha) / math.sin(ha)
                  * math.cos(be + (Lc + 1.0) * ha))
        worst_cs = max(worst_cs,
                       abs(closed - brute) / max(1.0, abs(brute)))
    m_c = 128
    mu_c = parity_mu(m_c)
    Tc = parity_basis(m_c)
    LPc = lap_P_mat(m_c)
    e_eig = float(np.max(np.abs(LPc @ Tc.T - Tc.T * mu_c[None, :])))
    e_ort = float(np.max(np.abs(Tc @ Tc.T - np.eye(m_c))))
    cL = np.zeros(2 * m_c)
    cL[0], cL[1] = 2.0, -1.0
    e_tpl = float(np.max(np.abs(odd_toeplitz(cL, 2 * m_c) - LPc)))
    check(f"S5.CTRL: the closed Dirichlet cosine-sum identity agrees with "
          f"brute force to {worst_cs:.1e} <= {TOL_CTRL:.0e} on 64 random "
          f"triples (Dirichlet 1829); L_P t_k = mu^P_k t_k to {e_eig:.1e} "
          f"with the basis orthonormal to {e_ort:.1e} (KMS 1953); and "
          f"odd_toeplitz(c^L) = L_P with residual {e_tpl:.1e} == 0 (zero "
          f"tolerance): the classical spine every gauge statement above "
          f"stands on is the one the identities assume",
          worst_cs <= TOL_CTRL and e_eig <= 1.0e-11
          and e_ort <= 1.0e-12 and e_tpl == 0.0)

    # ================================================================ S6
    print("\nS6 -- the fences, restated as a check")
    check("S6.FENCE: per-instance identities and certified inequalities on "
          "a SMALL declared surface only -- a FINITE LIST with an explicit "
          "maximum, NOTHING uniform in the zone index or in D, and NO "
          "statement for ALL D; finite Lambda-sums are allowed and used, "
          "NO RH statement is made, assumed, approached or weakened, no "
          "zero of any L-function is read and no L-function is evaluated "
          "(AST firewall); RH_DELTA = 0.5 is a YARDSTICK in exactly one "
          "role; THE FRAME-FREE DEFICIT IS A MEASUREMENT AND NOT A CLAIM "
          "OF THIS MODULE -- T174's +0.1111 +- 0.0222 (5.0 sigma, 151 "
          "anchor clusters, dens >= 3.0, cluster-robust; 0.4 sigma from "
          "T173's +0.155 +- 0.102) stays a sandbox MEASURED number on ITS "
          "surface, as do all T172/T173/T174 h-exponents, the density "
          "anatomy and the nu/density collinearity; P6 (D-rule "
          "invariance) is NOT a theorem -- only its multiplicative half "
          "is, the additive arch/comb mixture admits no factorisation "
          "(S3.NOFACTOR) -- and P6 is less load-bearing after T174 "
          "because the deficit is measured on a D-rule-free surface; THE "
          "ONE OPEN PHASE-2 OBJECT STAYS OPEN AND TYPED OPEN -- R1, now "
          "stated frame-free: an m-free unconditional certificate that "
          "two explicit finite Lambda-sum vectors become collinear at the "
          "demanded rate; the residual per-anchor scatter (chi^2/dof = "
          "3.02) and the sparse-corner question are sandbox items under "
          "test in T175; THE WEIL FENCE: positivity of a finite A_h is "
          "never routed through the Weil criterion, the audited chain is "
          "the R4-free R1 form; no marker of any pre-existing contract "
          "moves; Schur 1917, KMS 1953, Dirichlet 1829, Rayleigh 1877, "
          "Abel 1826, Chebyshev 1852 / Rosser-Schoenfeld 1962, Wilkinson "
          "1968 / Higham 2002 named CLASSICAL; Weil 1952 / Bombieri 2000 "
          "CITED, never used as a criterion; zero-firewall AST-checked",
          True)

    elapsed = time.time() - t0
    print(f"\nv560 runtime: {elapsed:.1f}s")
    print(f"  transfer: 4 links exact on frame-B + non-prime-power; "
          f"horizon discriminator lam_min = {r_trunc['lmin']:.2e} < 0 "
          f"(truncated) vs {len(CELLS)}/{len(CELLS)} PD (complete)")
    print(f"  gauges: amplitude + mu^P_1 channel cancel exactly (worst "
          f"bar-ratio {max(max(E_AMP), max(E_MU), max(E_M1)):.3f}); "
          f"shape band <= {max(SH_RAT):.3f} of the unconditional bound; "
          f"no factorisation (0/{len(CELLS)} single-term floors)")
    print(f"  scramble: {n_neg}/{len(MOVE_R)} draws destroy the floor, "
          f"|R| moves x{med_move:.1e} median (reporting cap "
          f"{CAP_SCRAM:.0e}) -- R1 stays OPEN, the deficit stays a "
          f"MEASUREMENT")
    return summary("PRIME.FRAME.DEFICIT.01 frame/deficit identities")


if __name__ == "__main__":
    raise SystemExit(run())
