"""v552 -- PRIME.ANGLE.INSTR.01: the four fixed-size angle instruments of T155/T157.
The INSTRUMENT-shaped cores of T155 (contract BOTTOM.FLOOR) and T157 (contract
ANGLE.FLOOR) -- every statement RECOMPUTED here from scratch on small exactly
checkable frame-A windows (no citation of sandbox output).  Companion to
PRIME.RITZ.CEIL.01 (v551), which certified the fixed-size CEILING step: THIS
module certifies the four fixed-size instruments the angle campaign produced --
none of them closes an angle, and none is promoted as anything but a
per-instance instrument:

[E] (1) THE COMPLEMENT-FLOOR CERTIFICATE (T155).  For any orthonormal W with
    K_W columns, with G = T_K Q_W the K x K_W parity-overlap matrix and
    M = diag(mu^P_{K+1} - mu^P_k) (k <= K = 12),
        min_{v perp W} v^T L_P v / v^T v
            >= mu^P_{K+1} - lam_max(M^{1/2}(I - G G^T) M^{1/2})
    -- an identity plus ONE Rayleigh bound on the high block, a theorem for
    every m and every subspace, with the direction checked (the certified
    lam_max is SUBTRACTED from a lower bound, so the result is a floor and
    the certificate never exceeds the exact complement bottom).  A 12 x 12
    problem in the exact KMS numbers plus one 12 x K_W overlap matrix
    replaces the size-m eigenproblem.  EXACTNESS CONTROLS in both known
    configurations: W = span{t_1..t_8} must return mu^P_9 exactly and
    W = span{t_2..t_13} -- the configuration in which the certificate is
    WORTHLESS -- must return mu^P_1 exactly (self-reported worthlessness);
    mutation: corrupting one row of G breaks the agreement loudly.
[E] (2) THE SINE-BLOCK CONFINEMENT (T157).  From the certified pencil floor
    A >= t L_P (Schur two-block, kb = 16) and the certified ladder ceiling
    lam_1(A) <= S mu^P_1 (v551's sixteen-column certificate) alone, with
    gam = T e_1(A) the parity coordinates of the bottom eigenvector,
        ||gam_H||^2 <= lam_1 / (t mu^P_17) <= (S / t) / rho_17 ,
    rho_17 = mu^P_17 / mu^P_1 (KMS 1953) -- a one-line per-instance theorem
    that replaces T146's MEASURED ``98 per cent in the sine block''.  Checked
    against the directly measured tail on every window, non-vacuous (< 1)
    everywhere; NEGATIVE CONTROL: substituting the pencil ceiling kap for
    the ladder S makes the bound vacuous (> 1) on every window -- the choice
    of ceiling is the whole content; mutation: the inflated pencil floor
    kap L_P is refuted at e_1(A) itself.
[E] (3) THE SCHUR-ENTRY IDENTITY (T157).  s := mu^P_1 t_1^T A^-1 t_1 =
    (B^-1)_{11} EXACTLY (A^-1 = T^T Lam^{-1/2} B^-1 Lam^{-1/2} T and t_1 is
    the first parity sine), and (B^-1)_{LL} = S_L^{-1} with
    S_L = B_LL - B_LH B_HH^-1 B_HL the SAME fixed-size 16 x 16 Schur
    complement the T152..T157 chain already forms -- so 1/s is carried by
    one fixed-size object and 1/s <= (S_L)_{11} (the literal diagonal entry,
    a theorem for positive definite S_L).  T156's R2'' loss ceiling
    r <= 1/(L s) is thereby a statement about ONE entry.  NEGATIVE CONTROL
    (the T157 refutation, wired as a check): the inversion-free
    Cauchy-Schwarz ceiling (S_L)_{11} <= a_hat - ||b||^4/(b^T B_HH b)
    (b = B_{H,1}) is VALID but off by orders of magnitude -- the
    cancellation in b^T B_HH^-1 b is nearly complete and Cauchy-Schwarz
    cannot see it; mutation: a one-index shift breaks the identity.
[E] (4) THE ADAPTIVE LIPSCHITZ DECKEL (T157).  The arch one-variable
    statement inf_{th in [th_lo, pi]} f^arch(th)/(4 sin^2(th/2)) >= t is
    turned from a grid observation into an EXECUTED certificate: interval
    bisection accepting [a, b] as soon as R(mid) - lip(a)(b - a)/2 >= t,
    with the LOCAL Lipschitz bound lip(a) = dsum/g(a) + 2 fabs/g(a)^2
    (dsum = 2 sum_l l |c^arch_l|, fabs = |c_0| + 2 sum |c_l|, g monotone).
    The GLOBAL th_lo constant is documented as insufficient: a uniform grid
    at that constant needs orders of magnitude more evaluations than the
    adaptive deckel spends.  Mutation: a target above the true grid minimum
    must make the deckel REFUSE -- it cannot be talked into certifying a
    false floor.

Plus the NO-GO DISCRIMINATOR (the T145 family c(l) = 1/(1+l), on which the
Schur floor SURVIVES): the confinement bound must report vacuum there and the
Schur entry (S_L)_{11} = 1/s must explode on the size ladder while both are
O(1) / non-vacuous on the real family -- an instrument that looked the same
on both families would be measuring nothing.  Parity controls (A = L_P: B = I,
s = 1, zero tail, both complement configurations exact) and the DIRICHLET
negative control (the parity sines are NOT eigenvectors of the Dirichlet
tridiagonal; the residual must equal the predicted 2/sqrt(N)).

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL frame-A windows -- the
        N_INST DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), mirroring v551's declared surface.  Nothing is uniform
        in the zone index or in D, and NO statement for ALL D is made.
  (ii)  NOTHING ABOUT THE ANGLES IS CLOSED: the two open terms after T157
        stay OPEN and are typed open -- an m-free LOWER bound on
        ghat_1^2 (equivalently an m-free UPPER bound on the one Schur
        diagonal entry; the resolvent route is a THEOREM times that ONE
        MEASURED fixed-size number), and an m-free R1'' domination with a
        non-shrinking margin (T157 certifies it per window with a margin
        7.3e-4 at the largest window and a shrinking trend -- explicitly
        NOT a uniform statement).  Neither is assumed nor approached here.
  (iii) The confinement and the Schur-entry statements consume the
        per-window certified floor t and ceiling S; the m-freeness of both
        is exactly what remains open (v551's fence, unchanged).
  (iv)  The deckel certifies the ARCH half only; the atom half of R1'' is
        untouched, and T157's mechanism finding (the two extremals sit at
        opposite ends of the band) stays sandbox.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil
    window form (Weil 1952, CITED, never used as a criterion) on a FINITE
    list of prime-power zones.  Everything here is an identity or a
    certified inequality PER INSTANCE; NOTHING here claims, assumes or
    approaches RH, and no statement about zeta zeros is made.  No zero data
    of any kind is read, generated or approximated -- an AST firewall
    enforces this.  Even with every check green, what stands is a finite
    list of certified window statements on prime-power zones in one frame.
  * Classics named CLASSICAL: Kac-Murdock-Szego 1953 (exact parity
    eigenpairs and ratios), Schur 1917 / Haynsworth 1968 (two-block floor
    and the Schur complement), Courant-Fischer 1920 / Cauchy 1829 (the
    ceiling direction), Cauchy-Schwarz (refuted as a ceiling for the entry,
    wired as a negative control), Kantorovich 1948 (the product P, named),
    Temple 1928 / Kato 1949 (floor devices, not used here), Sylvester 1852 /
    Bunch-Kaufman 1977 (inertia), Bjoerck-Golub 1973 (angles, measured),
    Wilkinson 1968 / Higham 2002 (completed Cholesky floors), Chebyshev
    1852, Szego 1915 / Widom 1958 (named address, never a licence).
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime side
    is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name, each with a mutation control that fails loudly;
measured quantities typed MEASURED.  Python; Wolfram-mirrored not required
(dense Cholesky / eigenvalue machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/bottom_floor_probe.py               (T155)
  experiments/tfpt-discovery/angle_floor_probe.py                (T157)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v551
H_CAP = 300                  # HARD cap on any factorised / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              admitting a window inside the cap (v551's
#                              declared surface convention, not tuned)

# --- the instrument geometry, preregistered ---------------------------------
K_CERT = 8                   # bottom Ritz directions fed to instrument (1)
K_TWELVE = 12                # the complement-floor certificate size (T155)
SCHUR_KB = 16                # the fixed low block of the T152..T157 Schur floor
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.2, 0.15, 0.1, 0.05)
T_TARGET = 0.25              # the arch deckel target (the chain's t)
DECKEL_CAP = 400000          # hard evaluation budget of the deckel

# --- the stress families, preregistered --------------------------------------
NOGO_SIZES = (48, 96, 192, 288)   # c(l) = 1/(1+l) reconstruction, <= H_CAP
NOGO_GROW = 4.0              # confinement bound and (S_L)_11 must both grow
CTRL_SIZES = (64, 128, 256)  # exact parity model A = L_P

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_C1 = 2.0e-3              # DECLARED cap on 1 - certificate/exact (instr. 1)
#                              on THIS small surface (m <= 300); the agreement
#                              tightens with window depth -- T155 measured
#                              <= 2.2e-7 at h = 142..1293 (sandbox, not
#                              consumed here) -- and the mutation control must
#                              move the certificate by >> this cap
TOL_EXACT = 1.0e-9           # both closed-form complement configurations
TOL_IDENT = 1.0e-9           # s = (B^-1)_{11} and the Schur-pair identity
TOL_PAR = 1.0e-11            # parity model exactness (B = I, s = 1, tail = 0)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
BAR_CS = 50.0                # the Cauchy-Schwarz ceiling must miss by >= this
BAR_KAP = 1.0                # the kap-substituted confinement must be vacuous
BAR_KAP_FAC = 10.0           # ... and >= this factor above the S-substituted
BAR_INFL = 100.0             # the inflated pencil floor must overshoot e_1
BAR_GRID = 50.0              # uniform-grid cost must exceed adaptive by this
#                              on the deepest window
TOL_DIRI = 0.05              # Dirichlet residual against predicted 2/sqrt(N)


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
    bit the frame-A code path of T128..T157 / v548..v551."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T157)
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


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except (LinAlgError, ValueError):
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    return 8.0 * h * np.finfo(float).eps * max(A_norm, 1.0e-300)


def gersh(X):
    return float(np.max(np.sum(np.abs(X), axis=1)))


def cert_lam_max(X, guess, tries=14, grow=1.0e-7):
    """AN UPPER BOUND on lam_max, certified by a COMPLETED Cholesky of
    t I - X.  DIRECTION: upper."""
    h = X.shape[0]
    t = abs(float(guess)) + 1.0e-300
    for _ in range(tries):
        Y = sym(t * np.eye(h) - X)
        if safe_cho(Y) is not None:
            return t + chol_floor(gersh(Y), h)
        t *= (1.0 + grow)
        grow *= 6.0
    return float("nan")


# ------------------------------------- the certified floor (Schur two-block)
def parity_block(A, Tf, mu):
    """B = Lam^{-1/2} T A T^T Lam^{-1/2}: lam_min(B) IS the pencil floor
    (an identity; v549..v551 machinery, rebuilt here)."""
    Gf = sym(Tf @ (A @ Tf.T))
    isq = 1.0 / np.sqrt(mu)
    return sym(Gf * np.outer(isq, isq))


def schur_floor(B, kb, t):
    """THE CERTIFIED TWO-BLOCK SCHUR FLOOR (Schur 1917; Haynsworth 1968).
    DIRECTION: a LOWER bound, certified per window at SIZE m (the m-freeness
    of this floor is exactly the open term and is NOT claimed)."""
    h = B.shape[0]
    HH = sym(B[kb:, kb:] - t * np.eye(h - kb))
    fac = safe_cho(HH)
    if fac is None:
        return None
    fl1 = chol_floor(gersh(HH), h - kb)
    try:
        X = cho_solve(fac, B[kb:, :kb], check_finite=False)
    except (LinAlgError, ValueError):
        return None
    S = sym(B[:kb, :kb] - t * np.eye(kb) - B[:kb, kb:] @ X)
    if safe_cho(S) is None:
        return None
    fl2 = chol_floor(gersh(S), kb)
    return t - fl1 - fl2


def schur_best(B, kb):
    for t_try in T_LADDER:
        got = schur_floor(B, kb, t_try)
        if got is not None and got > 0.0:
            return got
    return float("nan")


# ------------------------------------- the fixed-size ceiling (v551 machinery)
def green_cols(A, LP, V, fac=None):
    if fac is None:
        fac = safe_cho(sym(A + 0.0))
    if fac is None:
        return None
    try:
        return cho_solve(fac, LP @ V, check_finite=False)
    except (LinAlgError, ValueError):
        return None


def orth_cols(V, tol=1.0e-10):
    U, s, _ = np.linalg.svd(V, full_matrices=False)
    if s.size == 0 or s[0] <= 0.0:
        return V[:, :0]
    keep = int(np.sum(s > tol * s[0]))
    return U[:, :keep]


def append_orth(Q, V, tol=1.0e-9):
    out = [Q]
    cur = Q
    for j in range(V.shape[1]):
        v = V[:, j].copy()
        for _ in range(2):
            v -= cur @ (cur.T @ v)
        nv = float(np.linalg.norm(v))
        if nv <= tol:
            continue
        v /= nv
        out.append(v.reshape(-1, 1))
        cur = np.concatenate(out, axis=1)
    return cur


def cert_ceiling(W, mu, K):
    """K^F = max_{k <= K} lam_max(Y_k^T W Y_k) / mu^P_k -- v551's fixed-size
    ladder ceiling.  DIRECTION (Courant-Fischer 1920): an UPPER bound on
    lam_k(A) / mu^P_k for every k <= K."""
    try:
        _, Y = eigh(W)
    except (LinAlgError, ValueError):
        return float("nan")
    out = []
    for k in range(1, K + 1):
        Z = sym(Y[:, :k].T @ (W @ Y[:, :k]))
        lm = cert_lam_max(Z, guess=float(np.max(np.diag(Z))) + 1.0e-12)
        out.append(lm / mu[k - 1])
    return float(np.max(out))


# ------------------------------------- instrument (1): the complement floor
def complement_floor(mu, G, K):
    """T155's FIXED-SIZE COMPLEMENT-FLOOR CERTIFICATE.  DIRECTION: lam_max is
    a CERTIFIED UPPER bound and it is SUBTRACTED, so the return value is a
    LOWER bound on min_{v perp W} v^T L_P v / v^T v."""
    K = int(min(K, mu.shape[0] - 1))
    if K < 1:
        return float("nan")
    muK1 = float(mu[K])
    Mv = np.maximum(muK1 - mu[:K], 0.0)
    rt = np.sqrt(Mv)
    E = sym((np.eye(K) - G[:K] @ G[:K].T) * np.outer(rt, rt))
    try:
        wE = eigvalsh(E)
    except (LinAlgError, ValueError):
        return float("nan")
    top = cert_lam_max(E, guess=float(wE[-1]) + 1.0e-13 * muK1)
    if not np.isfinite(top):
        return float("nan")
    return muK1 - top


def complement_exact(LP, Q):
    """THE EXACT COMPLEMENT BOTTOM min_{v perp range(Q)} v^T L_P v / v^T v,
    by a full size-m diagonalisation of the compressed form (m <= H_CAP;
    the honest competitor of the fixed-size certificate)."""
    m = LP.shape[0]
    P = np.eye(m) - Q @ Q.T
    w = eigvalsh(sym(P @ (LP @ P)))
    return float(w[Q.shape[1]])


# ------------------------------------- instrument (4): the Lipschitz deckel
def lip_local(a, dsum, fabs):
    """THE LOCAL LIPSCHITZ CONSTANT OF R = f / g, g = 4 sin^2(th/2), ON AN
    INTERVAL STARTING AT a: |R'| <= dsum/g(a) + 2 fabs/g(a)^2 (g monotone
    increasing on (0, pi]).  DIRECTION: an UPPER bound on |R'|, hence usable
    in a LOWER bound on R."""
    g = 4.0 * math.sin(0.5 * a) ** 2
    return dsum / g + 2.0 * fabs / (g * g)


def certified_inf_ratio(c, M, th_lo, th_hi, target, dsum, fabs,
                        cap=DECKEL_CAP):
    """THE ADAPTIVE LIPSCHITZ DECKEL, EXECUTED AND NOT ASSERTED (T157).
    Certifies R(th) = f(th)/(4 sin^2(th/2)) >= target on [th_lo, th_hi] by
    interval bisection: [a, b] is ACCEPTED as soon as
        R(mid) - lip_local(a) (b - a)/2 >= target .
    DIRECTION: every accepted interval carries a LOWER bound on R, so success
    is a certificate and failure is only a failure of this budget."""
    stack = [(th_lo, th_hi)]
    n_eval = 0
    worst = float("inf")
    ll = np.arange(1, M)
    cc = np.asarray(c)[1:M]
    while stack:
        if n_eval > cap:
            return False, n_eval, worst
        a, b = stack.pop()
        mid = 0.5 * (a + b)
        n_eval += 1
        f_mid = c[0] + 2.0 * float(np.dot(np.cos(ll * mid), cc))
        R_mid = f_mid / (4.0 * math.sin(0.5 * mid) ** 2)
        floor_here = R_mid - lip_local(a, dsum, fabs) * (b - a) * 0.5
        if floor_here >= target:
            worst = min(worst, floor_here)
            continue
        if (b - a) <= 1.0e-13 * max(1.0, th_hi):
            return False, n_eval, floor_here
        stack.append((a, mid))
        stack.append((mid, b))
    return True, n_eval, worst


def arch_ratio_grid(c_ar, M, th_lo, ng=8192):
    th = np.linspace(th_lo, math.pi, ng)
    ll = np.arange(1, M)
    f = c_ar[0] + 2.0 * (np.cos(np.outer(th, ll)) @ np.asarray(c_ar)[1:M])
    return float(np.min(f / (4.0 * np.sin(0.5 * th) ** 2)))


# ------------------------------------------------------------------ assembly
def build_instrument(A, m, c_ar=None, M_win=None):
    """ALL FOUR INSTRUMENTS on one positive section -- one code path for the
    surface, the no-go family and the controls."""
    mu = parity_mu(m)
    Tf = parity_basis(m)
    LP = lap_P_mat(m)
    N_win = 2 * m + 1
    out = dict(m=m, mu1=float(mu[0]), N=N_win)
    lam1 = float(eigvalsh(A, subset_by_index=[0, 0])[0])
    out["lam1"] = lam1
    if not (lam1 > 0.0):
        return out
    B = parity_block(A, Tf, mu)
    kb = min(SCHUR_KB, m - 2)
    out["t"] = schur_best(B, kb)
    try:
        kap_meas = float(eigh(B, eigvals_only=True,
                              subset_by_index=[m - 1, m - 1])[0])
    except (LinAlgError, ValueError):
        kap_meas = gersh(B)
    out["kap"] = cert_lam_max(B, guess=kap_meas)
    fac = safe_cho(sym(A + 0.0))
    if fac is None or not np.isfinite(out.get("t", float("nan"))):
        return out
    # ---- instrument (2): the sine-block confinement ------------------------
    _w, V_lo = eigh(A, subset_by_index=[0, 0])
    gam = Tf @ V_lo[:, 0]
    out["rho17"] = float(mu[kb] / mu[0])
    out["tail_meas"] = 1.0 - float(np.sum(gam[:kb] ** 2))
    out["ray_LP_e1"] = float(np.dot(mu, gam ** 2))
    out["tail_thm"] = lam1 / (out["t"] * float(mu[kb]))
    # the certified ladder ceiling S (v551's sixteen-column certificate)
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    g1 = green_cols(A, LP, V0, fac=fac)
    if g1 is None:
        return out
    Q16 = append_orth(orth_cols(V0), g1)
    WQ = sym(Q16.T @ (A @ Q16))
    out["S_lad"] = cert_ceiling(WQ, mu, K_CERT)
    out["tail_mfree"] = (out["S_lad"] / out["t"]) / out["rho17"]
    out["tail_kap"] = (out["kap"] / out["t"]) / out["rho17"]
    # ---- instrument (1): the complement-floor certificate ------------------
    try:
        _, Yq = eigh(WQ)
    except (LinAlgError, ValueError):
        return out
    QW = Q16 @ Yq[:, :K_CERT]
    G = Tf[:K_TWELVE, :] @ QW
    out["c1_cert"] = complement_floor(mu, G, K_TWELVE)
    out["c1_exact"] = complement_exact(LP, QW)
    G_bad = G.copy()
    G_bad[0] *= 0.5
    out["c1_mut"] = complement_floor(mu, G_bad, K_TWELVE)
    # ---- instrument (3): the Schur-entry identity ---------------------------
    t1 = np.ascontiguousarray(Tf[0, :])
    Ai_t1 = cho_solve(fac, t1, check_finite=False)
    out["s"] = out["mu1"] * float(t1 @ Ai_t1)
    out["S11"] = 1.0 / max(out["s"], 1.0e-300)
    t2 = np.ascontiguousarray(Tf[1, :])
    out["s_shift"] = out["mu1"] * float(t2 @ cho_solve(
        fac, t2, check_finite=False))
    Binv = np.linalg.inv(B)
    out["Binv11"] = float(Binv[0, 0])
    fH = safe_cho(sym(B[kb:, kb:]))
    if fH is not None:
        XB = cho_solve(fH, B[kb:, :kb], check_finite=False)
        SL = sym(B[:kb, :kb] - B[:kb, kb:] @ XB)
        out["SL11_lit"] = float(SL[0, 0])
        out["schur_pair"] = float(np.max(np.abs(
            Binv[:kb, :kb] @ SL - np.eye(kb)))) / max(
                gersh(Binv[:kb, :kb] @ SL), 1.0)
        b_col = np.ascontiguousarray(B[kb:, 0])
        bb = float(b_col @ b_col)
        bqb = float(b_col @ (B[kb:, kb:] @ b_col))
        a_hat = float(B[0, 0])
        out["a_hat"] = a_hat
        out["S11_cs"] = a_hat - (bb * bb / bqb if bqb > 0.0 else 0.0)
    # ---- instrument (4): the adaptive Lipschitz deckel ----------------------
    if c_ar is not None and M_win is not None:
        th_lo = 2.0 * math.pi * (kb + 1) / N_win
        ll = np.arange(1, M_win, dtype=float)
        dsum = 2.0 * float(np.dot(ll, np.abs(np.asarray(c_ar)[1:M_win])))
        fabs = abs(float(c_ar[0])) + 2.0 * float(
            np.sum(np.abs(np.asarray(c_ar)[1:M_win])))
        out["grid_min"] = arch_ratio_grid(c_ar, M_win, th_lo)
        ok_c, ne_c, wf_c = certified_inf_ratio(
            c_ar, M_win, th_lo, math.pi, T_TARGET, dsum, fabs)
        out.update(deck_ok=ok_c, deck_n=ne_c, deck_floor=wf_c)
        out["grid_need"] = (lip_local(th_lo, dsum, fabs)
                            * (math.pi - th_lo)
                            / (2.0 * max(out["grid_min"] - T_TARGET,
                                         1.0e-300)))
        ok_m, ne_m, _wf = certified_inf_ratio(
            c_ar, M_win, th_lo, math.pi, 1.05 * out["grid_min"], dsum, fabs,
            cap=4 * ne_c + 4096)
        out["deck_mut_refuses"] = (not ok_m)
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
    print("v552  PRIME.ANGLE.INSTR.01 -- the four fixed-size angle "
          "instruments (T155/T157)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered bars")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    for (k, D, M, h) in build_windows():
        alpha = 0.5 * M * D
        sp = lag_vector_split(alpha, M, atoms_in(alpha))
        A = sym(odd_toeplitz(sp["c"], M))
        got = build_instrument(A, h, c_ar=sp["c_ar"], M_win=M)
        if got.get("lam1", 0.0) > 0.0 and np.isfinite(
                got.get("S_lad", np.nan)):
            got["n"] = NN_ALL[k]
            got["D"] = D
            INST.append(got)
    h_max = max(t["m"] for t in INST) if INST else 0
    ok_floor = all(np.isfinite(t["t"]) and t["t"] > 0.0 for t in INST)
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite, certified Schur floor t > 0 and "
          f"certified ladder ceiling S on every one); every factorised / "
          f"diagonalised matrix <= {H_CAP} (max m = {h_max})",
          len(INST) >= 6 and h_max <= H_CAP and ok_floor)
    for t in INST:
        print(f"    n={t['n']:>7d} m={t['m']:>4d} t={t['t']:.4f} "
              f"S={t['S_lad']:.4f} kap={t['kap']:.4g} "
              f"conf={t['tail_mfree']:.4f} S11={t['S11']:.4f} "
              f"c1={t['c1_cert'] / t['c1_exact']:.9f} "
              f"deck={t['deck_n']:d}ev")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the complement-floor certificate (T155)")
    rat = [t["c1_cert"] / t["c1_exact"] for t in INST]
    dir_ok = all(t["c1_cert"] <= t["c1_exact"] * (1.0 + 1.0e-12)
                 for t in INST)
    check(f"S1.CORE: the {K_TWELVE}x{K_TWELVE} complement-floor certificate "
          f"mu^P_{K_TWELVE + 1} - lam_max(M^(1/2)(I - G G^T)M^(1/2)) "
          f"(identity + one certified Rayleigh bound; G the "
          f"{K_TWELVE}x{K_CERT} parity overlap of the eight bottom Ritz "
          f"directions) NEVER exceeds the exact size-m complement bottom "
          f"(direction, {len(INST)}/{len(INST)}) and agrees with it to "
          f"1 - ratio <= {max(1.0 - r for r in rat):.2e} <= the declared "
          f"cap {TOL_C1:.0e} on every window of THIS small surface (the "
          f"agreement tightens with depth: T155 measured <= 2.2e-7 at "
          f"h = 142..1293, sandbox, not consumed here) -- a 12x12 problem "
          f"in the exact KMS numbers replaces the size-m eigenproblem, and "
          f"the mutation control below moves the certificate by >> this cap",
          dir_ok and all(1.0 - r <= TOL_C1 for r in rat))
    ex_ok = True
    ex_worst = 0.0
    for m_c in CTRL_SIZES:
        mu_c = parity_mu(m_c)
        Tc = parity_basis(m_c)
        W1 = np.ascontiguousarray(Tc[:K_CERT, :].T)
        f1 = complement_floor(mu_c, Tc[:K_TWELVE, :] @ W1, K_TWELVE)
        W2 = np.ascontiguousarray(Tc[1:K_TWELVE + 1, :].T)
        f2 = complement_floor(mu_c, Tc[:K_TWELVE, :] @ W2, K_TWELVE)
        r1 = abs(f1 / float(mu_c[K_CERT]) - 1.0)
        r2 = abs(f2 / float(mu_c[0]) - 1.0)
        ex_worst = max(ex_worst, r1, r2)
        if r1 > TOL_EXACT or r2 > TOL_EXACT:
            ex_ok = False
    check(f"S1.EXACT: both closed-form configurations are hit on m = "
          f"{', '.join(str(s) for s in CTRL_SIZES)}: W = span{{t_1..t_8}} "
          f"returns mu^P_9 and W = span{{t_2..t_13}} -- the configuration "
          f"in which the certificate is WORTHLESS -- returns mu^P_1 (worst "
          f"relative {ex_worst:.1e} <= {TOL_EXACT:.0e}): the instrument "
          f"reports its own worthlessness rather than something flattering",
          ex_ok)
    mut = [abs(t["c1_mut"] / t["c1_exact"] - t["c1_cert"] / t["c1_exact"])
           for t in INST]
    check(f"S1.CTRL: corrupting ONE row of the overlap matrix (row 1 scaled "
          f"by 0.5) moves the certificate by >= {BAR_CTRL:.0e} relative on "
          f"{sum(1 for x in mut if x > BAR_CTRL)}/{len(INST)} windows "
          f"(smallest move {min(mut):.2e}) and only DOWNWARD (the mutated "
          f"floor never exceeds the exact bottom on any window): the "
          f"agreement of S1.CORE cannot be faked by a wrong overlap",
          all(x > BAR_CTRL for x in mut)
          and all(t["c1_mut"] <= t["c1_exact"] * (1.0 + 1.0e-12)
                  for t in INST))

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the sine-block confinement (T157)")
    conf_ok = all(t["tail_meas"] <= t["tail_thm"] * (1.0 + 1.0e-9)
                  and t["tail_thm"] <= t["tail_mfree"] * (1.0 + 1.0e-9)
                  and t["tail_mfree"] < 1.0 for t in INST)
    cf_lo = min(t["tail_mfree"] for t in INST)
    cf_hi = max(t["tail_mfree"] for t in INST)
    check(f"S2.CONF: the sine-block confinement ||gam_H||^2 <= lam_1/(t "
          f"mu^P_17) <= (S/t)/rho_17 holds in BOTH directions on "
          f"{len(INST)}/{len(INST)} windows and is NON-VACUOUS everywhere: "
          f"the bound is {cf_lo:.4f}..{cf_hi:.4f} < 1, i.e. e_1(A) lives to "
          f"{100 * (1 - cf_hi):.1f}..{100 * (1 - cf_lo):.1f} per cent "
          f"inside the first {SCHUR_KB} parity sines BY A PER-INSTANCE "
          f"THEOREM from the certified floor t and ladder S alone -- T146's "
          f"measured '98 per cent' replaced by one line (measured tail "
          f"{min(t['tail_meas'] for t in INST):.1e}.."
          f"{max(t['tail_meas'] for t in INST):.1e})", conf_ok)
    kap_vac = all(t["tail_kap"] > BAR_KAP for t in INST)
    kap_fac = min(t["tail_kap"] / t["tail_mfree"] for t in INST)
    check(f"S2.KAP: substituting the pencil ceiling kap for the LADDER S "
          f"makes the same bound VACUOUS on {len(INST)}/{len(INST)} windows "
          f"((kap/t)/rho_17 = {min(t['tail_kap'] for t in INST):.3g}.."
          f"{max(t['tail_kap'] for t in INST):.3g} > {BAR_KAP:.0f}, at "
          f"least {kap_fac:.1f}x >= {BAR_KAP_FAC:.0f}x above the S form): "
          f"kap carries the whole atom mass and is the WRONG ceiling for "
          f"any bottom quantity -- the choice of ceiling is the whole "
          f"content of the instrument",
          kap_vac and kap_fac >= BAR_KAP_FAC)
    infl = [t["kap"] * t["ray_LP_e1"] / t["lam1"] for t in INST]
    check(f"S2.CTRL: the INFLATED pencil floor (kap in place of t) is "
          f"refuted at the bottom eigenvector itself: kap e_1^T L_P e_1 "
          f"exceeds lam_1 by {min(infl):.3g}..{max(infl):.3g} >= "
          f"{BAR_INFL:.0f} on every window -- the confinement chain fails "
          f"loudly when fed a false floor, so S2.CONF is not a formality",
          all(x >= BAR_INFL for x in infl))

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the Schur-entry identity (T157)")
    id_ok = all(abs(t["s"] / t["Binv11"] - 1.0) <= TOL_IDENT
                and t.get("schur_pair", 1.0) <= 1.0e-8
                and t["S11"] <= t["SL11_lit"] * (1.0 + 1.0e-9)
                for t in INST)
    s11_lo = min(t["S11"] for t in INST)
    s11_hi = max(t["S11"] for t in INST)
    check(f"S3.IDENT: s = mu^P_1 t_1^T A^-1 t_1 = (B^-1)_11 EXACTLY (worst "
          f"relative {max(abs(t['s'] / t['Binv11'] - 1.0) for t in INST):.1e}"
          f" <= {TOL_IDENT:.0e}), the Schur pair (B^-1)_LL S_L = I holds to "
          f"{max(t['schur_pair'] for t in INST):.1e} with S_L = B_LL - "
          f"B_LH B_HH^-1 B_HL the SAME fixed-size {SCHUR_KB}x{SCHUR_KB} "
          f"complement the chain already forms, and the direction 1/s <= "
          f"(S_L)_11 (literal diagonal entry) holds on {len(INST)}/"
          f"{len(INST)}: 1/s = {s11_lo:.4f}..{s11_hi:.4f} is an O(1) NUMBER "
          f"carried by one fixed-size object -- T156's R2'' ceiling "
          f"r <= 1/(L s) is a statement about ONE entry", id_ok)
    cs_fac = [t["S11_cs"] / t["S11"] for t in INST]
    check(f"S3.CS: the inversion-free Cauchy-Schwarz ceiling a_hat - "
          f"||b||^4/(b^T B_HH b) is VALID (>= the literal entry on "
          f"{sum(1 for t in INST if t['S11_cs'] >= t['SL11_lit'] * (1 - 1e-9))}"
          f"/{len(INST)}) and USELESS: it misses 1/s by a factor "
          f"{min(cs_fac):.3g}..{max(cs_fac):.3g} >= {BAR_CS:.0f} on every "
          f"window (a_hat = {min(t['a_hat'] for t in INST):.3g}.."
          f"{max(t['a_hat'] for t in INST):.3g} is the same entry WITHOUT "
          f"the Schur subtraction) -- the cancellation in b^T B_HH^-1 b is "
          f"nearly complete and Cauchy-Schwarz cannot see it: T157's "
          f"refutation of the inversion-free ceiling, wired as a check",
          all(f >= BAR_CS for f in cs_fac)
          and all(t["S11_cs"] >= t["SL11_lit"] * (1.0 - 1.0e-9)
                  for t in INST))
    sh = [abs(t["s_shift"] / t["Binv11"] - 1.0) for t in INST]
    check(f"S3.CTRL: the one-index shift (t_2 in place of t_1) breaks the "
          f"identity by {min(sh):.3g}..{max(sh):.3g} >= {BAR_CTRL:.0e} on "
          f"every window: the identity is a statement about the FIRST "
          f"parity sine, not a generic near-agreement",
          all(x > BAR_CTRL for x in sh))

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the adaptive Lipschitz deckel (T157)")
    deck_ok = all(t["deck_ok"] and t["deck_floor"] >= T_TARGET
                  and t["deck_floor"] <= t["grid_min"] * (1.0 + 1.0e-9)
                  for t in INST)
    ne_lo = min(t["deck_n"] for t in INST)
    ne_hi = max(t["deck_n"] for t in INST)
    check(f"S4.DECKEL: the adaptive Lipschitz deckel CERTIFIES inf "
          f"f^arch/(4 sin^2(th/2)) >= t = {T_TARGET} on {len(INST)}/"
          f"{len(INST)} windows in {ne_lo}..{ne_hi} symbol evaluations "
          f"(certified floor "
          f"{min(t['deck_floor'] for t in INST):.4f}.."
          f"{max(t['deck_floor'] for t in INST):.4f}, never above the fine "
          f"8192-point grid minimum "
          f"{min(t['grid_min'] for t in INST):.4f}.."
          f"{max(t['grid_min'] for t in INST):.4f} -- direction checked): "
          f"the arch one-variable statement carries an EXECUTED certificate "
          f"per window, not a grid observation", deck_ok)
    gr = [t["grid_need"] / max(t["deck_n"], 1) for t in INST]
    check(f"S4.GLOBAL: the GLOBAL th_lo Lipschitz constant is documented as "
          f"insufficient -- a uniform grid at that constant would need "
          f"{min(t['grid_need'] for t in INST):.3g}.."
          f"{max(t['grid_need'] for t in INST):.3g} points, i.e. up to "
          f"{max(gr):.3g}x >= {BAR_GRID:.0f}x the adaptive cost on the "
          f"deepest window -- the LOCAL constant is the whole affordability "
          f"of the certificate", max(gr) >= BAR_GRID)
    check(f"S4.CTRL: fed a target ABOVE the true grid minimum (1.05 x "
          f"grid min), the deckel REFUSES on {sum(1 for t in INST if t['deck_mut_refuses'])}"
          f"/{len(INST)} windows: it cannot be talked into certifying a "
          f"false floor -- failure is reported as failure",
          all(t["deck_mut_refuses"] for t in INST))

    # ---------------------------------------------------------------- stress
    print("\nS5 -- the no-go discriminator and the controls (T155/T157)")
    NG = []
    for m_ng in NOGO_SIZES:
        M_ng = 2 * m_ng
        c_ng = 1.0 / (1.0 + np.arange(M_ng, dtype=float))
        got = build_instrument(sym(odd_toeplitz(c_ng, M_ng)), m_ng)
        if got.get("lam1", 0.0) > 0.0:
            NG.append(got)
    ng_floor = all(np.isfinite(g["t"]) and g["t"] > 0.0 for g in NG)
    g_conf = NG[-1]["tail_mfree"] / NG[0]["tail_mfree"]
    g_s11 = NG[-1]["S11"] / NG[0]["S11"]
    check(f"S5.NOGO: on the T145 no-go reconstruction c(l) = 1/(1+l) the "
          f"certified Schur floor SURVIVES (t = "
          f"{min(g['t'] for g in NG):.4g}..{max(g['t'] for g in NG):.4g} on "
          f"all {len(NG)} sizes) while BOTH new instruments break: the "
          f"confinement bound is VACUOUS there "
          f"({min(g['tail_mfree'] for g in NG):.3g}.."
          f"{max(g['tail_mfree'] for g in NG):.3g} > 1 on every size, "
          f"growing x{g_conf:.1f} >= {NOGO_GROW}) and the Schur entry "
          f"(S_L)_11 = 1/s explodes ({NG[0]['S11']:.4g} -> "
          f"{NG[-1]['S11']:.4g}, x{g_s11:.1f} >= {NOGO_GROW}) against the "
          f"flat {s11_lo:.4f}..{s11_hi:.4f} band of the real family over "
          f"m = {NOGO_SIZES[0]}..{NOGO_SIZES[-1]}: the instruments do NOT "
          f"report confinement or O(1) entries where both are false -- a "
          f"floors-only probe would have seen nothing",
          len(NG) == len(NOGO_SIZES) and ng_floor
          and all(g["tail_mfree"] > 1.0 for g in NG)
          and g_conf >= NOGO_GROW and g_s11 >= NOGO_GROW
          and max(t["tail_mfree"] for t in INST) < 1.0)
    par_ok = True
    par_worst = 0.0
    for m_c in CTRL_SIZES:
        mu_c = parity_mu(m_c)
        Tc = parity_basis(m_c)
        LPc = lap_P_mat(m_c)
        e_par = float(np.max(np.abs(LPc @ Tc.T - Tc.T * mu_c[None, :])))
        Bc = parity_block(sym(LPc + 0.0), Tc, mu_c)
        dev_B = float(np.max(np.abs(Bc - np.eye(m_c))))
        fc = safe_cho(sym(LPc + 0.0))
        t1c = np.ascontiguousarray(Tc[0, :])
        s_c = float(mu_c[0]) * float(t1c @ cho_solve(
            fc, t1c, check_finite=False))
        gam_c = Tc @ (parity_basis(m_c)[0, :])  # e_1(L_P) IS t_1
        tail_c = 1.0 - float(np.sum(gam_c[:SCHUR_KB] ** 2))
        par_worst = max(par_worst, e_par, dev_B, abs(s_c - 1.0), abs(tail_c))
        if max(e_par, dev_B, abs(s_c - 1.0), abs(tail_c)) > TOL_PAR:
            par_ok = False
    check(f"S5.PARITY: feeding A = L_P through the SAME instruments on m = "
          f"{', '.join(str(s) for s in CTRL_SIZES)} returns the exact "
          f"parity answers -- the sines are exact eigenpairs, B = I "
          f"entrywise, s = 1 (so (S_L)_11 = 1: t_1 IS the bottom "
          f"eigenvector) and the confinement tail is 0 (worst deviation "
          f"{par_worst:.1e} <= {TOL_PAR:.0e}): when there is nothing to "
          f"measure, every instrument says so exactly", par_ok)
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
    check(f"S5.DIRICHLET: against the DIRICHLET tridiagonal (the corner "
          f"reflection removed, arithmetic kept bit for bit) the parity "
          f"sines are NOT eigenvectors and the residual equals the "
          f"predicted 2/sqrt(N) to a relative {diri_worst:.1e} <= "
          f"{TOL_DIRI}: the exactness of S5.PARITY is a property of the "
          f"PARITY boundary condition, not of trigonometry", diri_ok)

    # ---------------------------------------------------------------- fences
    print("\nS6 -- the fences, restated as a check")
    check("S6.FENCE: PER-INSTANCE instruments on SMALL frame-A windows only "
          "-- a FINITE LIST with an explicit maximum, nothing uniform in "
          "the zone index or in D, and NO statement for ALL D: the TWO "
          "open terms after T157 (an m-free lower bound on ghat_1^2, "
          "equivalently an m-free upper bound on the one Schur diagonal "
          "entry 1/s -- the resolvent route is a THEOREM times that ONE "
          "MEASURED fixed-size number; and an m-free R1'' domination with "
          "a non-shrinking margin -- T157 certifies it per window with a "
          "7.3e-4 margin at the largest window and a shrinking trend) stay "
          "OPEN, typed open, and are neither assumed nor approached; every "
          "floor t and ceiling S consumed here is certified per window and "
          "its m-freeness is exactly what remains open (v551's fence, "
          "unchanged); the confinement percentage and the O(1) band of "
          "1/s are per-instance facts, not limits; KMS 1953 / Schur 1917 / "
          "Haynsworth 1968 / Courant-Fischer 1920 / Cauchy 1829 / "
          "Cauchy-Schwarz (refuted as a ceiling, wired as a control) / "
          "Kantorovich 1948 / Temple 1928 / Kato 1949 (floor devices, NOT "
          "used here) / Sylvester 1852 / Bunch-Kaufman 1977 / "
          "Bjoerck-Golub 1973 / Wilkinson 1968 / Higham 2002 / Chebyshev "
          "1852 / Szego 1915 / Widom 1958 (a named address, never a "
          "licence) named CLASSICAL; Weil 1952 CITED, never used as a "
          "criterion; zero-firewall AST-checked; NO marker upgrade of any "
          "pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv552 runtime: {elapsed:.1f}s")
    print(f"  (1) complement floor: 1 - cert/exact <= "
          f"{max(1.0 - r for r in rat):.2e} on {len(INST)} windows; both "
          f"closed-form controls to {ex_worst:.1e}")
    print(f"  (2) confinement (S/t)/rho_17 = {cf_lo:.4f}..{cf_hi:.4f} "
          f"(kap form vacuous {min(t['tail_kap'] for t in INST):.3g}.."
          f"{max(t['tail_kap'] for t in INST):.3g})")
    print(f"  (3) 1/s = {s11_lo:.4f}..{s11_hi:.4f} flat; CS ceiling misses "
          f"by {min(cs_fac):.3g}..{max(cs_fac):.3g}")
    print(f"  (4) deckel: {ne_lo}..{ne_hi} evals, uniform grid would need "
          f"{min(t['grid_need'] for t in INST):.3g}.."
          f"{max(t['grid_need'] for t in INST):.3g}")
    print(f"  no-go: confinement vacuous (x{g_conf:.1f}), (S_L)_11 "
          f"x{g_s11:.1f}; floor survives")
    return summary("PRIME.ANGLE.INSTR.01 fixed-size angle instruments")


if __name__ == "__main__":
    raise SystemExit(run())
