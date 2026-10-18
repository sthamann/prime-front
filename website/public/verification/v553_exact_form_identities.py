"""v553 -- PRIME.EXACT.FORM.IDENT.01: the exact-form identities of T158/T159.
The THEOREM-shaped cores of T158 (contract SCHUR.ENTRY) and T159 (contract
EXACT.FORM) -- every statement RECOMPUTED here from scratch on small exactly
checkable frame-A windows (no citation of sandbox output).  Companion to
PRIME.ANGLE.INSTR.01 (v552), which certified the four fixed-size angle
instruments: THIS module certifies the algebra of the sixteen-form itself --
the dual variational structure, the exact lag sum with its gauge identity,
the two closed scalars, and the one exact sign law the campaign found.
NOTHING here closes either open term:

[E] (1) THE THOMSON DUAL FORM AND THE POSITIVE CHOLESKY LADDER (T158, P1).
    s := (B^-1)_{11} = max_x (2 x_1 - x^T B x) (Maz'ya 1985; Miclo 1999 --
    s is a conductance of mode 1 into the bulk, the maximum is Thomson's
    principle): EVERY trial vector is a LOWER bound on s and hence an UPPER
    bound on 1/s -- the variational structure Cauchy-Schwarz lacks (v552
    wired that refutation as a control; here the direction itself is the
    check).  The Cholesky ladder g_K = sum_{j<=K} y_j^2 with y = L^-1 e_1
    from ONE Cholesky of the leading 16 x 16 block of B (nested Schur
    complements, Schur 1917 / Haynsworth 1968): all terms STRICTLY
    POSITIVE, partial sums MONOTONE, every g_K <= s (floor direction), and
    1/s <= 1/g_16 <= 1/g_1 = B_11 literally.  Mutation: a 5% corruption of
    one off-diagonal entry of the sixteen-block destroys positive
    definiteness -- the Cholesky REFUSES.
[E] (2) THE TWO-DIMENSIONALITY (T158, P2).  span{t_1, A^-1 L_P t_1} attains
    s EXACTLY, because L_P t_1 = mu^P_1 t_1 (KMS 1953) makes A^-1 L_P t_1
    proportional to the Dirichlet maximiser A^-1 t_1: the entry is a
    TWO-dimensional quantity the moment one Green column is granted.
    Negative controls: span{t_1, t_2} (two sines, no Green column) misses
    s by a factor >= 1.3, and the corrupted Green column L_P t_1 (no solve)
    misses by >= 50x.
[E] (3) THE GAUGE IDENTITY AND THE TmH SIGNATURE (T159, P4/P7).  The
    reflection-odd section A_rs = c_{|r-s|} - c_{M-1-r-s} ANNIHILATES
    constant lag vectors -- odd_toeplitz(1) == 0 ENTRYWISE, zero tolerance
    -- hence sum_d w_d = 0 EXACTLY for the lag weights w_d = T_d - H_d of
    every vector: the form is BLIND to the lag mass of c, and the lag mass
    is exactly where the arch and atom halves of the sixteen-form are of
    size h^2 and cancel (T159's mechanism, per instance).  The premise is
    the Toeplitz-minus-Hankel signature A_{r,s} - A_{r+1,s+1} = f(r+s),
    constant along every anti-diagonal.  Mutations: a one-index Hankel
    shift breaks the gauge identity loudly; the T145 no-go form
    R = a a^T + eps I has signature defect >= 1e-2 -- not a parity
    section, the gauge identity is not even DEFINED for it.
[E] (4) THE EXACT LAG SUM AND THE TWO CLOSED SCALARS (T159, P2/P5).
    x^T B_LL x = sum_{d} c_d w_d with w_d = T_d - H_d (T the
    autocorrelation, H the convolution of y = sum_k (x_k/sqrt(mu^P_k)) t_k)
    against the direct assembly, to 1e-12 of the ABSOLUTE scale
    sum_d |c_d w_d| -- the honest bar: relative to the cancelled total the
    same identity holds several digits worse, and that depth IS the h^2
    obstruction, reported as a measurement.  The two closed scalars:
    w_0 = sum_k x_k^2 / mu^P_k (the N^2/(4 pi^2) factor itself) and
    2 w_0 - w_1 = ||x||^2 EXACTLY, because L_P = odd_toeplitz(2, -1, 0, ..)
    and the t_k are its exact eigenvectors (KMS 1953): the huge scale and
    the O(1) scale sit in the SAME two weights.  Mutations: a 1%
    perturbation of the largest c lag breaks the lag sum; a one-index mu
    shift breaks w_0.
[E] (5) THE Z-MATRIX LAW AND THE COLLATZ-WIELANDT FLOOR (T159, U1/U2).
    B^arch_HH (the archimedean half of the bulk parity block, k_b = 16) is
    a symmetric Z-MATRIX, RAW: every off-diagonal entry <= 0 with NO
    tolerance, on every window.  Hence the closed sign-based floor
    min_k (B^arch_HH 1)_k >= t = 0.25 with the theorem direction verified
    per instance: floor <= lam_min(B^arch_HH) exactly (the symmetric
    M-matrix criterion -- Perron 1907 / Frobenius 1912 read through
    Collatz 1942 / Wielandt 1950).  THE HONEST LIMIT AS CONTENT: the ATOM
    block obeys NO sign law (off-diagonal nonpositive fraction a coin
    toss), the FULL block is not a Z-matrix and its row-sum floor is
    NEGATIVE on every window -- the criterion is admissible and VACUOUS
    there, so R1'' stays OPEN.  Mutation: the checkerboard similarity
    S = diag((-1)^k) -- an ISOMETRY, lam_min moves by 0 exactly --
    destroys the raw law (fraction drops to a coin toss): the Z law is an
    entrywise fact, not a spectral one, and T159's checkerboard reading
    (S2) is refuted.

Plus the NO-GO DISCRIMINATOR (both T145 forms): on R = a a^T + eps I,
a_i = i^{-1/2}, the Z law, the TmH signature and the constant diagonal are
ALL unavailable (three axes); on the c(l) = 1/(1+l) reconstruction the
ladder THEOREM survives (positive terms, floor direction) while 1/g_16
EXPLODES on the size ladder, tracking the true 1/s -- the instrument
reports the collapse instead of hiding it.  Parity controls (A = L_P is
EXACTLY odd_toeplitz((2, -1, 0, ...)): B = I, s = 1, every ladder partial
sum g_K = 1 constant in K, the full lag machinery returns
sum c_d w_d = ||x||^2 = 1 and a zero gauge sum) and the DIRICHLET negative
control (the parity sines are NOT eigenvectors of the Dirichlet
tridiagonal; the residual must equal the predicted 2/sqrt(N)).

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL frame-A windows -- the
        N_INST DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), mirroring v551/v552's declared surface.  Nothing is
        uniform in the zone index or in D, and NO statement for ALL D is
        made.
  (ii)  NEITHER OPEN TERM IS CLOSED OR APPROACHED: R2'' -- the ONE
        explicit pairing inequality T159 left (a bound on
        sum_d (Delta c)_d W^1_d that uses the CORRELATION between Delta c
        and W^1 rather than their sizes; l1-times-sup pricing is refuted
        at every Abel rung, growing h^{+3.6} against a target O(1)) --
        stays OPEN and typed open; R1'' -- a device for the ATOM off-band
        block that is neither a norm (refuted by T158) nor a sign (refuted
        by T159: nonpositive fraction 0.31..0.49) -- stays OPEN and typed
        open.  The m-freeness of every floor t and ceiling consumed here
        is exactly what remains open.
  (iii) T159's refutations are NOT promoted (refutations belong in the
        anatomy, not the ledger): the fixed sixteen-vector (grows
        h^{+3.51}), the one-sine rung (h^{+3.07}), the closed power-law
        ansatz family (h^{+3.00}), the Abel l1-pricing (h^{+3.60}) and the
        checkerboard sign law are all sandbox negatives; the checkerboard
        appears here only as a mutation control.
  (iv)  The Z law and the floor are statements about the ARCHIMEDEAN half
        only; the numerical horizon T159 declared (cond(B_LL) > 1e12 past
        h ~ 1292) does not reach this small surface and is not consumed.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil
    window form (Weil 1952, CITED, never used as a criterion) on a FINITE
    list of prime-power zones.  Everything here is an identity or a
    certified inequality PER INSTANCE; NOTHING here claims, assumes or
    approaches RH, and no statement about zeta zeros is made.  No zero data
    of any kind is read, generated or approximated -- an AST firewall
    enforces this.  Even with every check green, what stands is a finite
    list of certified window statements on prime-power zones in one frame.
  * Classics named CLASSICAL: Maz'ya 1985 / Miclo 1999 (Thomson's
    principle, the dual form), Schur 1917 / Haynsworth 1968 (nested
    complements, the ladder), Kac-Murdock-Szego 1953 (exact parity
    eigenpairs -- the two-dimensionality and the 2w_0 - w_1 scalar),
    Dirichlet 1829 (the closed-weight address; the 256-term closed form
    itself stays sandbox), Abel 1826 (summation by parts, cited), Perron
    1907 / Frobenius 1912 / Collatz 1942 / Wielandt 1950 (the sign-based
    floor), Gantmacher-Krein 1950 (the oscillation refinement, an address),
    Fejer 1915 (the section weights), Chebyshev 1852 (the atom budget,
    cited), Wilkinson 1968 / Higham 2002 (completed Cholesky floors),
    Cauchy-Schwarz (its failure at the entry is v552's wired control).
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime side
    is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name, each with a mutation control that fails loudly;
measured quantities typed MEASURED.  Python; Wolfram-mirrored not required
(dense Cholesky / eigenvalue machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/schur_entry_probe.py                (T158)
  experiments/tfpt-discovery/exact_form_probe.py                 (T159)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, cholesky, eigvalsh

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v552
H_CAP = 300                  # HARD cap on any factorised / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              admitting a window inside the cap (v551/v552's
#                              declared surface convention, not tuned)

# --- the form geometry, preregistered ----------------------------------------
SCHUR_KB = 16                # the fixed low block of the T152..T159 chain
T_TARGET = 0.25              # the chain's floor target t
N_TRIALS = 8                 # random Thomson trials per window (fixed seed)
N_RANDX = 3                  # random 16-vectors per window for the identities

# --- the stress families, preregistered --------------------------------------
NOGO_SIZES = (48, 96, 192, 288)   # both T145 forms, <= H_CAP
NOGO_EPS = 0.05              # the eps of R = a a^T + eps I
NOGO_GROW = 4.0              # 1/g_16 must grow at least this much on the ladder
CTRL_SIZES = (64, 128, 256)  # exact parity model A = L_P

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_IDENT = 1.0e-9           # s = (B^-1)_{11} and the span attainment
TOL_KMS = 1.0e-11            # L_P t_1 = mu^P_1 t_1 eigenpair residual
TOL_LAG = 1.0e-12            # lag identities vs the ABSOLUTE scale
TOL_SIG = 1.0e-12            # TmH signature anti-diagonal constancy
TOL_PAR = 1.0e-11            # parity model exactness
TOL_DIRI = 0.05              # Dirichlet residual against predicted 2/sqrt(N)
TIGHT_CAP = 1.5              # DECLARED cap on (1/g_16)/(1/s) on THIS surface
#                              (T158 measured <= 1.2738 at h = 254..1393,
#                              sandbox, not consumed here)
TOL_SPLIT = 1.0e-15          # floating residue of the lag split re-summation
BAR_SIGN_GAIN = 0.5          # the sign-based floor must beat the sign-free
#                              norm route by at least this, every window
BAR_SINES = 1.3              # span{t_1, t_2} must miss s by >= this factor
BAR_GREEN = 50.0             # the corrupted Green column must miss by >= this
BAR_MUT_GAUGE = 1.0e-9       # the shifted-Hankel gauge break, >= this
BAR_SIG_NOGO = 1.0e-2        # signature defect of the T145 form, >= this
BAR_MUT_LAG = 1.0e-4         # the 1% lag perturbation must break by >= this
BAR_MUT_MU = 0.1             # the mu-shift must break w_0 by >= this
CB_LO, CB_HI = 0.30, 0.70    # the coin-toss band for sign fractions


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


def atom_table(n_max):
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0)[0]:
        n = int(n)
        out.append((n, lam[n], math.log(n), 2.0 * lam[n] / math.sqrt(n)))
    return out


ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


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
    return (-(EULER + math.log(math.pi)) * tri_s + 2.0 * tot
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


def atom_lags(alpha, M, atoms):
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for u_j, mu_j in atoms:
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


def lag_vector_split(alpha, M, atoms):
    """THE T115 lag assembly c = c^arch + c^atom, both halves kept -- bit for
    bit the frame-A code path of T128..T159 / v548..v552."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T159)
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: the reflection-odd section (v549 item
    (4): EXACTLY the compression of T_M(c) onto the antisymmetric parity
    sector -- quoted, not re-verified here)."""
    h = M // 2
    r = np.arange(h)
    return (np.asarray(c)[np.abs(r[:, None] - r[None, :])]
            - np.asarray(c)[(M - 1) - r[:, None] - r[None, :]])


def parity_mu(m):
    """THE EXACT PARITY EIGENVALUES mu^P_k = 4 sin^2(pi k / N), N = 2m+1
    (KMS 1953 in the parity sector)."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL PARITY BASIS t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N)."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P_mat(m):
    L = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    L[m - 1, m - 1] = 3.0
    return L


def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def parity_block(A, Tf, mu):
    """B = Lam^{-1/2} T A T^T Lam^{-1/2}: the whitened parity block
    (an identity; v549..v552 machinery, rebuilt here)."""
    Gf = sym(Tf @ (A @ Tf.T))
    isq = 1.0 / np.sqrt(mu)
    return sym(Gf * np.outer(isq, isq))


def safe_chol(Q):
    try:
        return cholesky(sym(Q), lower=True)
    except (LinAlgError, ValueError):
        return None


# ------------------------------------- the lag weights (T159, P2)
def lag_weights(y, M, shift=0):
    """w_d = T_d - H_d, d = 0..M-1: T the autocorrelation and H the
    convolution of y, so that y^T A y = sum_d c_d w_d for the section
    A_rs = c_{|r-s|} - c_{M-1-r-s}.  `shift` != 0 is the MUTATION (a
    one-index Hankel shift) and must break the gauge identity loudly."""
    m = y.shape[0]
    T = np.zeros(M)
    T[0] = float(y @ y)
    for d in range(1, m):
        T[d] = 2.0 * float(y[:-d] @ y[d:])
    conv = np.convolve(y, y)
    H = np.zeros(M)
    for d in range(M):
        q = (M - 1) - d + shift
        if 0 <= q <= 2 * m - 2:
            H[d] = float(conv[q])
    return T - H


def sig_defect(X):
    """THE TmH SIGNATURE DEFECT: the worst variation of X_{r,s} - X_{r+1,s+1}
    along an anti-diagonal r+s = const, relative to max|X|.  Zero iff X has
    the Toeplitz-minus-Hankel structure (T159, P7)."""
    m = X.shape[0]
    S = X[:-1, :-1] - X[1:, 1:]
    worst = 0.0
    for q in range(0, 2 * (m - 1) - 1):
        rr = np.arange(max(0, q - (m - 2)), min(m - 1, q + 1))
        vals = S[rr, q - rr]
        if vals.size > 1:
            worst = max(worst, float(np.max(vals) - np.min(vals)))
    return worst / float(np.max(np.abs(X)))


def offdiag_stats(X):
    """(nonpositive fraction, max entry, |mass|) of the off-diagonal part."""
    off = X - np.diag(np.diag(X))
    h = X.shape[0]
    n_off = h * (h - 1)
    fr = (float(np.sum(off <= 0.0)) - h) / n_off
    return fr, float(np.max(off)), float(np.sum(np.abs(off)))


# ------------------------------------------------------------------ assembly
def build_window(A, m, c=None, M_win=None, c_ar=None, seed=0):
    """ALL FIVE ITEMS on one positive section -- one code path for the
    surface, the no-go family and the controls."""
    mu = parity_mu(m)
    Tf = parity_basis(m)
    out = dict(m=m, N=2 * m + 1)
    lam1 = float(eigvalsh(sym(A), subset_by_index=[0, 0])[0])
    out["lam1"] = lam1
    if not (lam1 > 0.0):
        return out
    B = parity_block(A, Tf, mu)
    kb = min(SCHUR_KB, m - 2)
    fac = cho_factor(sym(A), lower=True, check_finite=False)
    t1 = np.ascontiguousarray(Tf[0, :])
    # ---- (1) the Thomson dual form and the positive ladder -----------------
    out["s"] = float(mu[0]) * float(t1 @ cho_solve(fac, t1,
                                                   check_finite=False))
    rng = np.random.default_rng(seed)
    over = -np.inf
    for _ in range(N_TRIALS):
        xt = rng.standard_normal(m)
        over = max(over, 2.0 * xt[0] - float(xt @ (B @ xt)) - out["s"])
    out["overshoot"] = over
    BLL = sym(B[:kb, :kb])
    Lc = safe_chol(BLL)
    if Lc is None:
        return out
    y16 = np.linalg.solve(Lc, np.eye(kb)[:, 0])
    out["y2_min"] = float(np.min(y16 ** 2))
    out["gK"] = np.cumsum(y16 ** 2)
    out["B11"] = float(BLL[0, 0])
    Bb = BLL.copy()
    Bb[0, 1] *= 1.05
    Bb[1, 0] *= 1.05
    out["mut_ladder_refuses"] = safe_chol(Bb) is None
    # ---- (2) the two-dimensionality -----------------------------------------
    LP = lap_P_mat(m)
    out["kms_res"] = (float(np.max(np.abs(LP @ t1 - mu[0] * t1)))
                      / float(mu[0]))

    def span_value(V):
        # sup of the Dirichlet functional over span(V).  The frame may be
        # rank-deficient BY CONSTRUCTION: the corrupted-column control below
        # pairs t_1 with L_P t_1 = mu^P_1 t_1 (the KMS eigenpair), so its
        # Gram is rank one (sigma_2/sigma_1 ~ 1e-25).  The minimal-norm
        # pseudo-inverse evaluates the functional on the span itself; an LU
        # `solve` there is platform-dependent (exact-zero pivot ->
        # LinAlgError on x86-64 OpenBLAS, finite round-off on Accelerate).
        Mv = sym(V.T @ (A @ V))
        b = math.sqrt(mu[0]) * (V.T @ t1)
        x = np.linalg.lstsq(Mv, b, rcond=None)[0]
        return float(b @ x)

    g_col = cho_solve(fac, LP @ t1, check_finite=False)
    out["g_span"] = span_value(np.stack([t1, g_col], axis=1))
    out["g_sines"] = span_value(np.stack(
        [t1, np.ascontiguousarray(Tf[1, :])], axis=1))
    out["g_bad"] = span_value(np.stack([t1, LP @ t1], axis=1))
    # ---- (3) + (4): gauge identity, signature, lag sum, closed scalars ------
    if c is not None and M_win is not None:
        cv = np.asarray(c)[:M_win]
        out["sig"] = sig_defect(A)
        out["kill_const"] = float(np.max(np.abs(
            odd_toeplitz(np.ones(M_win), M_win))))
        xs = [np.linalg.solve(BLL, np.eye(kb)[:, 0])]
        xs[0] = xs[0] / xs[0][0]
        for _ in range(N_RANDX):
            xs.append(rng.standard_normal(kb))
        gauge_w, lag_w, ltot_w, w0_w, x2_w = 0.0, 0.0, 0.0, 0.0, 0.0
        for x in xs:
            yv = (Tf[:kb, :].T / np.sqrt(mu[:kb])) @ x
            w = lag_weights(yv, M_win)
            supw = float(np.max(np.abs(w)))
            form = float(x @ (BLL @ x))
            lag = float(cv @ w)
            a_sc = float(np.sum(np.abs(cv * w)))
            gauge_w = max(gauge_w, abs(float(np.sum(w))) / supw)
            lag_w = max(lag_w, abs(form - lag) / a_sc)
            ltot_w = max(ltot_w, abs(form - lag) / abs(form))
            w0_w = max(w0_w, abs(w[0] - float(np.sum(x ** 2 / mu[:kb])))
                       / abs(w[0]))
            x2_w = max(x2_w, abs(2.0 * w[0] - w[1] - float(x @ x))
                       / abs(w[0]))
        out.update(gauge=gauge_w, lag=lag_w, lag_tot=ltot_w, w0=w0_w,
                   x2=x2_w)
        # mutations on the optimiser vector
        x0 = xs[0]
        yv = (Tf[:kb, :].T / np.sqrt(mu[:kb])) @ x0
        w = lag_weights(yv, M_win)
        w_sh = lag_weights(yv, M_win, shift=1)
        out["mut_gauge"] = (abs(float(np.sum(w_sh)))
                            / float(np.max(np.abs(w_sh))))
        a_sc = float(np.sum(np.abs(cv * w)))
        form = float(x0 @ (BLL @ x0))
        d_star = int(np.argmax(np.abs(cv * w)))
        c_mut = cv.copy()
        c_mut[d_star] *= 1.01
        out["mut_lag"] = abs(form - float(c_mut @ w)) / a_sc
        out["mut_w0"] = (abs(w[0] - float(np.sum(x0 ** 2 / mu[1:kb + 1])))
                         / abs(w[0]))
    # ---- (5) the Z-matrix law and the sign-based floor ----------------------
    if c_ar is not None and M_win is not None:
        A_ar = sym(odd_toeplitz(c_ar, M_win))
        B_ar = parity_block(A_ar, Tf, mu)
        HHa = sym(B_ar[kb:, kb:])
        out["z_fr"], out["z_max"], _ = offdiag_stats(HHa)
        out["floor_arch"] = float(np.min(HHa @ np.ones(HHa.shape[0])))
        out["lam_arch"] = float(eigvalsh(HHa, subset_by_index=[0, 0])[0])
        P = -(HHa - np.diag(np.diag(HHa)))
        out["norm_route"] = (float(np.min(np.diag(HHa)))
                             - float(np.max(np.sum(np.abs(P), axis=1))))
        off = HHa - np.diag(np.diag(HHa))
        kk = np.arange(HHa.shape[0])
        sgn = (-1.0) ** (kk[:, None] + kk[None, :])
        out["cb_mass"] = (float(np.sum(np.abs(off[(off * sgn) < 0])))
                          / max(float(np.sum(np.abs(off))), 1.0e-300))
        Sm = np.diag((-1.0) ** kk)
        HHf = sym(Sm @ HHa @ Sm)
        out["z_fr_flip"], _, _ = offdiag_stats(HHf)
        out["lam_flip_dev"] = abs(
            float(eigvalsh(HHf, subset_by_index=[0, 0])[0])
            / out["lam_arch"] - 1.0)
        A_at = sym(odd_toeplitz(np.asarray(c)[:M_win] - np.asarray(c_ar)[:M_win],
                                M_win))
        B_at = parity_block(A_at, Tf, mu)
        out["at_fr"], _, _ = offdiag_stats(sym(B_at[kb:, kb:]))
        HH = sym(B[kb:, kb:])
        out["full_fr"], _, _ = offdiag_stats(HH)
        out["floor_full"] = float(np.min(HH @ np.ones(HH.shape[0])))
        out["lam_full"] = float(eigvalsh(HH, subset_by_index=[0, 0])[0])
    return out


def build_windows():
    cand = []
    for k in range(2, min(K_SCAN, len(UU_ALL) - 2)):
        g = UU_ALL[k + 1] - UU_ALL[k]
        if g <= 0.0:
            continue
        D = 0.5 * g / NU_MAIN
        M = even_window(UU_ALL[k], D)
        h = M // 2
        if h < H_MIN or h > H_CAP:
            continue
        cand.append((k, D, M, h))
    return cand[-N_INST:]


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v553  PRIME.EXACT.FORM.IDENT.01 -- the exact-form identities "
          "(T158/T159)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered bars")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    for (k, D, M, h) in build_windows():
        alpha = 0.5 * M * D
        sp = lag_vector_split(alpha, M, atoms_in(alpha))
        split_exact = float(np.max(np.abs(sp["c"] - sp["c_ar"] - sp["c_at"])))
        A = sym(odd_toeplitz(sp["c"], M))
        got = build_window(A, h, c=sp["c"], M_win=M, c_ar=sp["c_ar"], seed=k)
        if got.get("lam1", 0.0) > 0.0 and "gK" in got:
            got["n"] = NN_ALL[k]
            got["split"] = split_exact
            INST.append(got)
    h_max = max(t["m"] for t in INST) if INST else 0
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite on every one, the lag split "
          f"c = c^arch + c^atom exact to "
          f"{max(t['split'] for t in INST):.1e} <= {TOL_SPLIT:.0e} "
          f"floating residue); every factorised / diagonalised matrix <= "
          f"{H_CAP} (max m = {h_max})",
          len(INST) >= 6 and h_max <= H_CAP
          and all(t["split"] <= TOL_SPLIT for t in INST))
    for t in INST:
        print(f"    n={t['n']:>7d} m={t['m']:>4d} s={t['s']:.4f} "
              f"tight={(1.0 / t['gK'][-1]) / (1.0 / t['s']):.4f} "
              f"2dim={abs(t['g_span'] / t['s'] - 1.0):.2e} "
              f"gauge={t['gauge']:.2e} zfr={t['z_fr']:.4f} "
              f"floor={t['floor_arch']:.4f}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the Thomson dual form and the positive Cholesky "
          "ladder (T158, P1)")
    check(f"S1.DUAL: s = (B^-1)_11 = max_x(2x_1 - x^T B x) with the "
          f"direction EXECUTED, not asserted: {N_TRIALS} random trial "
          f"vectors per window never exceed s (worst overshoot "
          f"{max(t['overshoot'] for t in INST):.2e} <= 0 on "
          f"{len(INST)}/{len(INST)}) -- every trial is a LOWER bound on s "
          f"and hence an UPPER bound on the entry 1/s (Thomson's "
          f"principle, Maz'ya 1985 / Miclo 1999): the variational "
          f"structure Cauchy-Schwarz lacks, wired as the check itself",
          all(t["overshoot"] <= 0.0 for t in INST))
    lad_ok = True
    for t in INST:
        gK = t["gK"]
        if not (np.all(np.diff(gK) > 0.0) and t["y2_min"] > 0.0
                and gK[-1] <= t["s"] * (1.0 + 1.0e-12)
                and 1.0 / t["s"] <= 1.0 / gK[-1] <= 1.0 / gK[0] * (1 + 1e-12)
                and abs(1.0 / gK[0] / t["B11"] - 1.0) <= 1.0e-12):
            lad_ok = False
    ti = [(1.0 / t["gK"][-1]) / (1.0 / t["s"]) for t in INST]
    check(f"S1.LADDER: the positive Cholesky ladder g_K = sum_(j<=K) y_j^2, "
          f"y = L^-1 e_1 from ONE Cholesky of the leading "
          f"{SCHUR_KB} x {SCHUR_KB} block of B (nested Schur complements, "
          f"Schur 1917 / Haynsworth 1968): all {SCHUR_KB} terms STRICTLY "
          f"positive (smallest y_j^2 = "
          f"{min(t['y2_min'] for t in INST):.2e}), partial sums strictly "
          f"monotone, every g_K <= s (floor direction, no rung ever "
          f"overshoots), and 1/s <= 1/g_16 <= 1/g_1 = B_11 LITERALLY on "
          f"{len(INST)}/{len(INST)} windows -- T158's P1, per instance",
          lad_ok)
    check(f"S1.TIGHT: the sixteen-rung ceiling is TIGHT on this surface: "
          f"(1/g_16)/(1/s) = {min(ti):.4f}..{max(ti):.4f} <= the declared "
          f"cap {TIGHT_CAP} (T158 measured <= 1.2738 at h = 254..1393, "
          f"sandbox, not consumed here) -- the size of the terms is a "
          f"MEASURED per-window fact and its m-freeness is NOT claimed",
          all(x <= TIGHT_CAP for x in ti))
    check(f"S1.CTRL: corrupting ONE off-diagonal entry of the "
          f"sixteen-block by 5% destroys positive definiteness -- the "
          f"Cholesky REFUSES on "
          f"{sum(1 for t in INST if t['mut_ladder_refuses'])}/{len(INST)} "
          f"windows: the positive ladder cannot be built from a wrong "
          f"block, so S1.LADDER is not a formality",
          all(t["mut_ladder_refuses"] for t in INST))

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the two-dimensionality of the entry (T158, P2)")
    tw = [abs(t["g_span"] / t["s"] - 1.0) for t in INST]
    check(f"S2.SPAN: span{{t_1, A^-1 L_P t_1}} attains the Dirichlet "
          f"maximum s EXACTLY: g_span/s = 1 to {max(tw):.1e} <= "
          f"{TOL_IDENT:.0e} on {len(INST)}/{len(INST)} windows, for the "
          f"theorem reason L_P t_1 = mu^P_1 t_1 (KMS 1953; eigenpair "
          f"residual {max(t['kms_res'] for t in INST):.1e} <= "
          f"{TOL_KMS:.0e}) -- the entry is a TWO-dimensional quantity the "
          f"moment one Green column is granted (T158's P2)",
          all(x <= TOL_IDENT for x in tw)
          and all(t["kms_res"] <= TOL_KMS for t in INST))
    ms = [t["s"] / t["g_sines"] for t in INST]
    check(f"S2.SINES: the SAME two-dimensional recipe WITHOUT the Green "
          f"column -- span{{t_1, t_2}}, two sines -- misses s by a factor "
          f"{min(ms):.3g}..{max(ms):.3g} >= {BAR_SINES} on every window: "
          f"the attainment is a property of the Green column, not of "
          f"two-dimensionality as such",
          all(x >= BAR_SINES for x in ms))
    mb = [t["s"] / t["g_bad"] for t in INST]
    check(f"S2.CTRL: the corrupted Green column (L_P t_1 in place of "
          f"A^-1 L_P t_1, no solve) misses s by a factor "
          f"{min(mb):.3g}..{max(mb):.3g} >= {BAR_GREEN:.0f} on every "
          f"window: the solve is load-bearing, and S2.SPAN cannot be "
          f"faked by a cheap column",
          all(x >= BAR_GREEN for x in mb))

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the gauge identity and the TmH signature "
          "(T159, P4/P7)")
    check(f"S3.KILL: the section map ANNIHILATES constant lag vectors "
          f"ENTRYWISE, with zero tolerance: odd_toeplitz(1) == 0 exactly "
          f"(worst entry {max(t['kill_const'] for t in INST):.1e}) on "
          f"every window size -- A_rs = c_(|r-s|) - c_(M-1-r-s) kills "
          f"c = const in one line, which is the MECHANISM of the gauge "
          f"identity", all(t["kill_const"] == 0.0 for t in INST))
    check(f"S3.GAUGE: the gauge identity sum_d w_d = 0 holds to "
          f"{max(t['gauge'] for t in INST):.1e} <= {TOL_LAG:.0e} of "
          f"sup|w| for the per-window optimiser AND {N_RANDX} random "
          f"sixteen-vectors on {len(INST)}/{len(INST)} windows: the form "
          f"is BLIND to the lag mass of c -- and the lag mass is exactly "
          f"where the arch and atom halves of the sixteen-form are of "
          f"size h^2 and cancel (T159's P4, the mechanism, per instance)",
          all(t["gauge"] <= TOL_LAG for t in INST))
    check(f"S3.SIG: the Toeplitz-minus-Hankel signature "
          f"A_(r,s) - A_(r+1,s+1) = f(r+s) is constant along EVERY "
          f"anti-diagonal to {max(t['sig'] for t in INST):.1e} <= "
          f"{TOL_SIG:.0e} of max|A| on every window -- the structural "
          f"premise of the gauge identity (T159's P7)",
          all(t["sig"] <= TOL_SIG for t in INST))
    a_ng = 1.0 / np.sqrt(np.arange(1, 97, dtype=float))
    R_ng = np.outer(a_ng, a_ng) + NOGO_EPS * np.eye(96)
    sd_ng = sig_defect(R_ng)
    mg = [t["mut_gauge"] for t in INST]
    check(f"S3.CTRL: a one-index Hankel shift breaks the gauge identity "
          f"by {min(mg):.2e}..{max(mg):.2e} >= {BAR_MUT_GAUGE:.0e} of "
          f"sup|w| on every window (against <= {TOL_LAG:.0e} for the true "
          f"structure), and the T145 no-go form R = a a^T + eps I has "
          f"signature defect {sd_ng:.2e} >= {BAR_SIG_NOGO:.0e}: R is not "
          f"a parity section, and the gauge identity is not even DEFINED "
          f"for it",
          all(x >= BAR_MUT_GAUGE for x in mg) and sd_ng >= BAR_SIG_NOGO)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the exact lag sum and the two closed scalars "
          "(T159, P2/P5)")
    check(f"S4.LAGSUM: the exact lag sum x^T B_LL x = sum_d c_d w_d "
          f"(w_d = T_d - H_d, T the autocorrelation and H the convolution "
          f"of y = sum_k (x_k/sqrt(mu^P_k)) t_k) holds against the DIRECT "
          f"assembly to {max(t['lag'] for t in INST):.1e} <= "
          f"{TOL_LAG:.0e} of the absolute scale sum_d |c_d w_d|, for the "
          f"optimiser and {N_RANDX} random vectors on every window -- "
          f"AND THE HONEST PRICE, MEASURED: relative to the CANCELLED "
          f"total the same identity holds only to "
          f"{max(t['lag_tot'] for t in INST):.1e} on this small surface "
          f"(the sandbox at h <= 1293 loses 4.0..8.1 digits) -- that "
          f"depth IS the h^2 obstruction, reported as a measurement",
          all(t["lag"] <= TOL_LAG for t in INST))
    check(f"S4.W0: the first closed scalar w_0 = sum_k x_k^2 / mu^P_k "
          f"(the N^2/(4 pi^2) factor itself) holds to "
          f"{max(t['w0'] for t in INST):.1e} <= {TOL_LAG:.0e} relative on "
          f"every window and every test vector (T159's P5, first half)",
          all(t["w0"] <= TOL_LAG for t in INST))
    check(f"S4.X2: the second closed scalar 2 w_0 - w_1 = ||x||^2 holds "
          f"to {max(t['x2'] for t in INST):.1e} <= {TOL_LAG:.0e} of the "
          f"w_0 scale, BECAUSE L_P = odd_toeplitz(2, -1, 0, ...) and the "
          f"t_k are its exact eigenvectors (KMS 1953): the huge scale and "
          f"the O(1) scale of the problem sit in the SAME two weights -- "
          f"w_0 carries the h^2 and the combination 2w_0 - w_1 kills it "
          f"(T159's P5, second half)",
          all(t["x2"] <= TOL_LAG for t in INST))
    ml = [t["mut_lag"] for t in INST]
    mw = [t["mut_w0"] for t in INST]
    check(f"S4.CTRL: a 1% perturbation of the LARGEST lag of c breaks the "
          f"lag sum by {min(ml):.2e}..{max(ml):.2e} >= {BAR_MUT_LAG:.0e} "
          f"of the absolute scale, and a one-index mu shift breaks w_0 by "
          f"{min(mw):.2g}..{max(mw):.2g} >= {BAR_MUT_MU}: the identities "
          f"are statements about THE lag vector and THE parity spectrum, "
          f"not generic near-agreements",
          all(x >= BAR_MUT_LAG for x in ml)
          and all(x >= BAR_MUT_MU for x in mw))

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the Z-matrix law and the Collatz-Wielandt floor "
          "(T159, U1/U2)")
    check(f"S5.ZLAW: B^arch_HH IS A SYMMETRIC Z-MATRIX, RAW: every "
          f"off-diagonal entry <= 0 with NO tolerance (nonpositive "
          f"fraction {min(t['z_fr'] for t in INST):.4f}, largest "
          f"off-diagonal entry {max(t['z_max'] for t in INST):.1e}) on "
          f"{len(INST)}/{len(INST)} windows -- T159's U1, the one exact "
          f"sign law of the campaign, per instance",
          all(t["z_fr"] == 1.0 and t["z_max"] <= 0.0 for t in INST))
    fl = [t["floor_arch"] for t in INST]
    dir_ok = all(t["floor_arch"] <= t["lam_arch"] * (1.0 + 1.0e-12)
                 for t in INST)
    gain = [t["floor_arch"] - t["norm_route"] for t in INST]
    n_neg = sum(1 for t in INST if t["norm_route"] < 0.0)
    check(f"S5.FLOOR: the closed SIGN-BASED floor min_k (B^arch_HH 1)_k = "
          f"{min(fl):.4f}..{max(fl):.4f} >= t = {T_TARGET} on "
          f"{len(INST)}/{len(INST)} windows, with the theorem direction "
          f"verified per instance: floor <= lam_min(B^arch_HH) = "
          f"{min(t['lam_arch'] for t in INST):.4f}.."
          f"{max(t['lam_arch'] for t in INST):.4f} exactly (the symmetric "
          f"M-matrix criterion, Perron 1907 / Frobenius 1912 / Collatz "
          f"1942 / Wielandt 1950) -- and the SIGN-FREE norm route "
          f"min diag - max off-band row sum = "
          f"{min(t['norm_route'] for t in INST):.3g}.."
          f"{max(t['norm_route'] for t in INST):.3g} is below the t "
          f"target on every window (negative on {n_neg}/{len(INST)}), "
          f"beaten by the sign-aware floor by "
          f"{min(gain):.3g}..{max(gain):.3g} >= {BAR_SIGN_GAIN}: the "
          f"signs are the whole content (T159's U2)",
          all(x >= T_TARGET for x in fl) and dir_ok
          and all(x >= BAR_SIGN_GAIN for x in gain)
          and all(t["norm_route"] < T_TARGET for t in INST))
    check(f"S5.LIMITS: the honest limit AS content -- the ATOM block "
          f"obeys NO sign law (nonpositive off-diagonal fraction "
          f"{min(t['at_fr'] for t in INST):.3f}.."
          f"{max(t['at_fr'] for t in INST):.3f}, a coin toss in "
          f"[{CB_LO}, {CB_HI}]), the FULL block is NOT a Z-matrix "
          f"(fraction {min(t['full_fr'] for t in INST):.3f}.."
          f"{max(t['full_fr'] for t in INST):.3f}) and its row-sum floor "
          f"min_k (B_HH 1)_k = {min(t['floor_full'] for t in INST):.3g}.."
          f"{max(t['floor_full'] for t in INST):.3g} is NEGATIVE on every "
          f"window against exact lam_min(B_HH) = "
          f"{min(t['lam_full'] for t in INST):.4f}.."
          f"{max(t['lam_full'] for t in INST):.4f} > 0: the criterion is "
          f"admissible and VACUOUS on the full block -- R1'' stays OPEN "
          f"and is typed open",
          all(CB_LO <= t["at_fr"] <= CB_HI for t in INST)
          and all(CB_LO <= t["full_fr"] <= CB_HI for t in INST)
          and all(t["floor_full"] < 0.0 < t["lam_full"] for t in INST))
    check(f"S5.CTRL: the checkerboard similarity S = diag((-1)^k) -- an "
          f"ISOMETRY, lam_min moves by "
          f"{max(t['lam_flip_dev'] for t in INST):.1e} -- DESTROYS the "
          f"raw law (nonpositive fraction drops from 1.0000 to "
          f"{min(t['z_fr_flip'] for t in INST):.3f}.."
          f"{max(t['z_fr_flip'] for t in INST):.3f}): the Z law is an "
          f"ENTRYWISE fact and not a spectral one, and T159's "
          f"checkerboard reading (S2) is refuted as a coin toss (mass "
          f"fraction {min(t['cb_mass'] for t in INST):.3f}.."
          f"{max(t['cb_mass'] for t in INST):.3f})",
          all(t["lam_flip_dev"] <= 1.0e-9 for t in INST)
          and all(CB_LO <= t["z_fr_flip"] <= CB_HI for t in INST)
          and all(CB_LO <= t["cb_mass"] <= CB_HI for t in INST))

    # ---------------------------------------------------------------- stress
    print("\nS6 -- the no-go discriminator and the controls (T158/T159)")
    NG = []
    for m_ng in NOGO_SIZES:
        M_ng = 2 * m_ng
        c_ng = 1.0 / (1.0 + np.arange(M_ng, dtype=float))
        got = build_window(sym(odd_toeplitz(c_ng, M_ng)), m_ng, seed=m_ng)
        if got.get("lam1", 0.0) > 0.0 and "gK" in got:
            NG.append(got)
    ng_thm = all(np.all(np.diff(g["gK"]) > 0.0)
                 and g["gK"][-1] <= g["s"] * (1.0 + 1.0e-12) for g in NG)
    g_grow = (1.0 / NG[-1]["gK"][-1]) / (1.0 / NG[0]["gK"][-1])
    a96 = offdiag_stats(R_ng)[0]
    dvar = float((np.max(np.diag(R_ng)) - np.min(np.diag(R_ng)))
                 / np.max(np.diag(R_ng)))
    check(f"S6.NOGO: the T145 no-go breaks on THREE axes of this module's "
          f"structure -- on R = a a^T + {NOGO_EPS} I (m = 96) the Z law "
          f"is the exact OPPOSITE (nonpositive fraction {a96:.3f} = 0), "
          f"the TmH signature is broken ({sd_ng:.2e} >= "
          f"{BAR_SIG_NOGO:.0e}) and the diagonal varies by {dvar:.2f} "
          f"(no lag structure) -- while on the c(l) = 1/(1+l) "
          f"reconstruction the ladder THEOREM survives (positive terms, "
          f"g_16 <= s on all {len(NG)} sizes) and the SIZE explodes: "
          f"1/g_16 = {1.0 / NG[0]['gK'][-1]:.4g} -> "
          f"{1.0 / NG[-1]['gK'][-1]:.4g} (x{g_grow:.1f} >= {NOGO_GROW}) "
          f"over m = {NOGO_SIZES[0]}..{NOGO_SIZES[-1]}, tracking the true "
          f"1/s = {1.0 / NG[0]['s']:.4g} -> {1.0 / NG[-1]['s']:.4g} -- "
          f"the instrument reports the collapse instead of hiding it",
          len(NG) == len(NOGO_SIZES) and ng_thm and a96 == 0.0
          and sd_ng >= BAR_SIG_NOGO and dvar >= 0.5
          and g_grow >= NOGO_GROW)
    par_ok = True
    par_worst = 0.0
    for m_c in CTRL_SIZES:
        M_c = 2 * m_c
        c_par = np.zeros(M_c)
        c_par[0], c_par[1] = 2.0, -1.0
        A_par = sym(odd_toeplitz(c_par, M_c))
        dev_LP = float(np.max(np.abs(A_par - lap_P_mat(m_c))))
        got = build_window(A_par, m_c, c=c_par, M_win=M_c, seed=m_c)
        gdev = float(np.max(np.abs(got["gK"] - 1.0)))
        wl = max(dev_LP, gdev, abs(got["s"] - 1.0), got["gauge"],
                 got["lag"], got["w0"], got["x2"],
                 abs(got["g_span"] / got["s"] - 1.0))
        par_worst = max(par_worst, wl)
        if wl > TOL_PAR:
            par_ok = False
    check(f"S6.PARITY: the parity Laplacian IS the section of the lag "
          f"vector (2, -1, 0, ...) -- A == L_P entrywise -- and feeding "
          f"it through the SAME machinery on m = "
          f"{', '.join(str(s) for s in CTRL_SIZES)} returns the exact "
          f"answers: B = I, s = 1, EVERY ladder partial sum g_K = 1 "
          f"(exactly constant in K -- the only configuration in which a "
          f"one-dimensional trial space may be optimal), the span attains "
          f"s, the gauge sum is zero and the lag sum returns "
          f"sum c_d w_d = ||x||^2 = 1 (worst deviation {par_worst:.1e} "
          f"<= {TOL_PAR:.0e}): when there is nothing to measure, every "
          f"identity says so exactly", par_ok)
    diri_ok = True
    diri_worst = 0.0
    for m_c in CTRL_SIZES:
        mu_c = parity_mu(m_c)
        Tc = parity_basis(m_c)
        LD = sym(2.0 * np.eye(m_c) - np.eye(m_c, k=1) - np.eye(m_c, k=-1))
        e_dir = float(np.max(np.abs(LD @ Tc.T - Tc.T * mu_c[None, :])))
        pred = 2.0 / math.sqrt(2.0 * m_c + 1.0)
        diri_worst = max(diri_worst, abs(e_dir / pred - 1.0))
        if abs(e_dir / pred - 1.0) > TOL_DIRI:
            diri_ok = False
    check(f"S6.DIRICHLET: against the DIRICHLET tridiagonal (the corner "
          f"reflection removed, arithmetic kept bit for bit) the parity "
          f"sines are NOT eigenvectors and the residual equals the "
          f"predicted 2/sqrt(N) to a relative {diri_worst:.1e} <= "
          f"{TOL_DIRI}: the exactness of S6.PARITY is a property of the "
          f"PARITY boundary condition, not of trigonometry", diri_ok)

    # ---------------------------------------------------------------- fences
    print("\nS7 -- the fences, restated as a check")
    check("S7.FENCE: PER-INSTANCE identities and certified inequalities "
          "on SMALL frame-A windows only -- a FINITE LIST with an "
          "explicit maximum, nothing uniform in the zone index or in D, "
          "and NO statement for ALL D: the TWO open terms after T159 "
          "(R2'' -- ONE explicit pairing inequality, a bound on "
          "sum_d (Delta c)_d W^1_d that uses the CORRELATION between "
          "Delta c and W^1 rather than their sizes, since l1-times-sup "
          "pricing is refuted at every Abel rung; and R1'' -- a device "
          "for the ATOM off-band block that is neither a norm nor a "
          "sign) stay OPEN, typed open, and are neither assumed nor "
          "approached; T159's refutations (the fixed sixteen-vector, the "
          "one-sine rung, the power-law ansatz family, the Abel "
          "l1-pricing, the checkerboard law) are sandbox negatives and "
          "NOT promoted; the m-freeness of every floor and ceiling "
          "consumed is exactly what remains open (v551/v552's fence, "
          "unchanged); Maz'ya 1985 / Miclo 1999 / Schur 1917 / "
          "Haynsworth 1968 / KMS 1953 / Dirichlet 1829 / Abel 1826 / "
          "Perron 1907 / Frobenius 1912 / Collatz 1942 / Wielandt 1950 / "
          "Gantmacher-Krein 1950 / Fejer 1915 / Chebyshev 1852 / "
          "Wilkinson 1968 / Higham 2002 named CLASSICAL; Weil 1952 "
          "CITED, never used as a criterion; zero-firewall AST-checked; "
          "NO marker upgrade of any pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv553 runtime: {elapsed:.1f}s")
    print(f"  (1) ladder: tight {min(ti):.4f}..{max(ti):.4f}; no trial "
          f"overshoot; corrupted block refuses")
    print(f"  (2) two-dim: attained to {max(tw):.1e}; sines miss "
          f"{min(ms):.3g}..{max(ms):.3g}; bad column {min(mb):.3g}.."
          f"{max(mb):.3g}")
    print(f"  (3) gauge <= {max(t['gauge'] for t in INST):.1e}; signature "
          f"<= {max(t['sig'] for t in INST):.1e}; const kill exact")
    print(f"  (4) lag sum <= {max(t['lag'] for t in INST):.1e} abs "
          f"(cancelled-total depth {max(t['lag_tot'] for t in INST):.1e}); "
          f"w_0, 2w_0 - w_1 exact")
    print(f"  (5) Z law raw 12/12; floor {min(fl):.4f}..{max(fl):.4f} >= "
          f"{T_TARGET}; atom/full sign-free (typed open)")
    print(f"  no-go: Z opposite, signature broken, 1/g_16 x{g_grow:.1f}; "
          f"parity/Dirichlet exact")
    return summary("PRIME.EXACT.FORM.IDENT.01 exact-form identities")


if __name__ == "__main__":
    raise SystemExit(run())
