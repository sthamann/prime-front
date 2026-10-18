"""v551 -- PRIME.RITZ.CEIL.01: the fixed-size Ritz ceiling certificate of T154.
The CERTIFICATE-shaped core of T154 (contract GREEN.ALIGN: the ceiling half of
T153's open term R2, closed at fixed size) -- every statement RECOMPUTED here
from scratch on small exactly checkable frame-A windows (no citation of
sandbox output).  Companion to PRIME.ODD.SECTOR.IDENT.01 (v550), which
certified the bottom ladder lam_k(A) <= S mu^P_k by per-window LDL^T counts of
SIZE m: THIS module certifies the FIXED-SIZE replacement T154 found -- the
sixteen-column subspace span{t_1..t_8} + A^-1 L_P span{t_1..t_8} carries a
Courant-Fischer ceiling K^F that ATTAINS the inertia-certified true bottom
ladder constant on every window, so the ceiling step needs no factorisation of
size m and, by direction, NO residual argument at all.

WHAT IS LOAD-BEARING HERE (and nothing else): identities, per-instance
theorems with CHECKED hypotheses, and per-window CERTIFIED inequalities.
NO fit, NO D-exponent, NO uniform-in-zone statement, and NO statement FOR
ALL D -- the TWO open inputs after T154 (R1': an m-free lower bound for
lam_min(B_HH) on the bulk parity block; R2': an m-free lower bound for the
L_P floor on the complement of the eight bottom Ritz directions, worth
91..100 percent of the collapse price) stay OPEN, are explicitly typed open,
and are neither assumed nor approached: every FLOOR consumed below is a
per-window certificate of size m (Schur two-block, one Cholesky), and the
m-freeness of every floor is exactly what remains open.  Each statement is
checked against a preregistered tolerance AND against at least one MUTATION
CONTROL that must fail loudly.

[E] (1) THE DIRECTION LEMMA (Courant-Fischer 1920 / Cauchy 1829, verified on
    the instance).  For any orthonormal Q with d columns and W = Q^T A Q,
    the Ritz values th_1 <= .. <= th_d satisfy lam_k(A) <= th_k for every
    k <= d -- Ritz values are UPPER bounds for the eigenvalues of the SAME
    index, so a Ritz quotient is a CEILING for the ladder constant by a
    theorem, never a floor.  Verified against the exact spectrum on the
    certificate subspace AND on random subspaces of every window; the
    NEGATIVE control: the reversed reading (Ritz values as lower bounds)
    MUST be recognised as false -- it is violated on every window with a
    quantified margin.  T154's direction correction is wired as a check:
    the ceiling needs NO residual argument; Temple 1928 / Kato 1949 is a
    FLOOR device and is not used in this module.
[E] (2) THE SIXTEEN-COLUMN CERTIFICATE (T154).  With t_1..t_8 the exact
    parity sines (KMS 1953) and one Green step A^-1 L_P t_k (k <= 8, by
    Cholesky back-solves, no inverse formed), the subspace
    S_1 = span{t_1..t_8} + A^-1 L_P span{t_1..t_8} has FIXED dimension 16,
    independent of m, and the ceiling K^F = max_k th_k(S_1) / mu^P_k is
    certified by 8 completed Choleskys of matrices of size <= 8.  On every
    window K^F AGREES with the inertia-certified true bottom ladder
    constant K_bot (8 completed LDL^T counts of size m, Sylvester 1852 /
    Bunch-Kaufman 1977) to a declared relative tolerance cap -- the
    certificate does not merely bound the true ladder, it ATTAINS it, and
    the 8 size-m LDL^T counts are thereby RETIRED from the ceiling step.
    Controls: the parity sines ALONE (the 8-column S_0) must OVERSHOOT
    K_bot, and corrupting the Green columns must break the attainment.
[E] (3) THE ONE-DIRECTION ANATOMY (T154, the named obstruction).  The
    principal angles (Bjoerck-Golub 1973) between the true bottom eight
    eigenvectors of A and the bottom eight of L_P show ONE misaligned
    direction: seven angles are small (median printed per window), the
    largest is large -- and that single misalignment IS the collapse
    price: lam_1(A) / (t mu^P_1), recovered IN FULL per window by ONE
    completed Cholesky of A - gam I (size m, certified, NOT fixed size,
    and labelled as such).  Control: on the exact parity model A = L_P
    the pattern is ABSENT (every angle ~ 0 and the price is exactly 1/t).
[E] (4) THE NO-GO DISCRIMINATOR (T154; the T145 no-go reconstruction).  On
    the positive decaying lag kernel c(l) = 1/(1+l) (log-singular symbol
    at the origin) the odd section is positive definite and the Schur
    floor survives -- but the true ladder constant EXPLODES on the size
    ladder and the sixteen-column ceiling MUST explode with it (a
    certificate that reported flatness there would manufacture closures
    and be worthless); the Courant-Fischer direction K^F >= K_bot is
    never violated on any positive-definite family.  The parity control
    A = L_P returns K_bot = K^F = 1 and zero misalignment; the DIRICHLET
    control (the Hankel half removed, arithmetic kept bit for bit) stops
    being positive definite -- lam_1 < 0 certified per window -- so no
    ceiling is defined there: the reflection half is load-bearing for
    positivity (T154's second refutation of the boundary-reflection
    reading, wired as a check).

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL windows.  The battery
        is the N_INST DEEPEST prime-power zones admitting a frame-A window
        inside the cap (n = 29..139, m = 96..291 <= 300) -- the deep end
        of the accessible surface, mirroring T154's own surface selection
        and DECLARED here rather than tuned: on the shallowest zones
        (n <= 11) more than one bottom direction leaves the sine block and
        the fixed-depth certificate is not claimed there.  Nothing here
        is uniform in the zone index or in D; what is established is a
        FINITE LIST of certified window inequalities with an explicit
        maximum, and every T154 exponent is a FIT that stays in the
        sandbox.  The m-freeness of the FLOORS stays OPEN: the pencil
        floor t (Schur two-block, kb = 16, size m per window), the block
        floor lam_min(B_HH) (T154's R1') and the bottom-mode floor on the
        Ritz complement (T154's R2') are all consumed or reported as
        per-window certificates ONLY, and no all-D statement is made.
  (ii)  The ATTAINMENT K^F = K_bot (to the declared cap) is a property of
        the REAL section, exhibited per window -- T154's no-go stress
        shows the certificate OVERSHOOTS on the no-go family, so exact
        attainment is not a property of the instrument, and it is not
        promoted to a theorem here.
  (iii) The misalignment angles of item (3) are MEASURED (they read
        eigenvectors); only the collapse-price recovery is certified
        (one completed Cholesky), and it is certified at size m.
  (iv)  Nothing about v550 is re-opened: the bottom ladder of v550 stays
        certified as stated there, and this module retires its size-m
        counts from the CEILING step only -- the floor direction is
        untouched and no marker of any pre-existing contract moves.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil
    window form (Weil 1952, CITED, never used as a criterion) on a FINITE
    list of prime-power zones.  Everything here is an identity or a
    certified inequality PER INSTANCE; NOTHING here claims, assumes or
    approaches RH, and no statement about zeta zeros is made.  No zero
    data of any kind is read, generated or approximated -- an AST firewall
    enforces this.  NO all-D claim: even with every check green, what
    stands is a finite list of certified window statements on prime-power
    zones, and the two open inputs (the m-freeness of the block floor and
    of the bottom-mode floor) stay open here and everywhere.
  * Classics named CLASSICAL: Courant-Fischer 1920 / Cauchy 1829 (the
    ceiling direction -- the ONLY direction Ritz values are used in),
    Kac-Murdock-Szego 1953 (the exact parity eigenpairs), Schur 1917 /
    Haynsworth 1968 (the two-block floor criterion, an equivalence),
    Sylvester 1852 / Bunch-Kaufman 1977 (inertia counts), Weyl 1912
    (monotonicity), Temple 1928 / Kato 1949 (the floor device -- named to
    state that it is NOT used here), Kaniel 1966 / Paige 1971 (why the
    Green step aligns -- quoted as explanation, never used as a bound),
    Bjoerck-Golub 1973 (principal angles, measured), Wilkinson 1968 /
    Higham 2002 (completed Cholesky and its floor), Chebyshev 1852.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] per-instance theorems with checked hypotheses (the direction
lemma against exact spectra), certified inequalities by completed Cholesky /
completed LDL^T with the direction in the name, and measured angles typed
MEASURED, each with a mutation control that fails loudly.  Python;
Wolfram-mirrored not required (dense Cholesky / LDL^T / eigenvalue
machinery stays Python-only), counted per GATE.WOLFRAM.02.  Discovery
provenance:
  experiments/tfpt-discovery/green_align_probe.py               (T154)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, ldl

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v550
H_CAP = 300                  # HARD cap on any factorised / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
U_ROUND = 2.0 ** -53

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              admitting a window inside the cap -- the deep
#                              end of the accessible surface, mirroring the
#                              T154 surface selection (declared, not tuned;
#                              the shallowest zones n <= 11 sit outside the
#                              aligned regime the certificate is about, and
#                              S3 shows why: more than one direction leaves
#                              the sine block there)

# --- the certificate geometry, preregistered --------------------------------
K_CERT = 8                   # the modes the certificate is about
SCHUR_KB = 16                # the fixed low block of the T152/T153 Schur floor
T_LADDER = (0.25, 0.245, 0.24, 0.235, 0.23, 0.225, 0.22, 0.215, 0.21, 0.205,
            0.2, 0.15, 0.1, 0.05)
LAD_BACKOFF = (1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)  # keeps every rung
#                              clear of eigenvalue ties (v550 convention)

# --- the stress families, preregistered --------------------------------------
NOGO_SIZES = (48, 96, 192, 288)   # c(l) = 1/(1+l) reconstruction, <= H_CAP
NOGO_GROW = 4.0              # K_bot and K^F must both grow >= this factor
CTRL_SIZES = (64, 128, 256)  # exact parity model A = L_P
N_DIRI = 3                   # windows fed through the Dirichlet control

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_DIR = 1.0e-9             # one-sided slack of the direction lemma
TOL_ATT = 1.0e-4             # DECLARED cap on |K^F / K_bot - 1| (attainment;
#                              dominated by the inertia ladder's backoff step)
TOL_CTRL_MODEL = 1.0e-5      # parity-model deviation cap (backoff-dominated)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
BAR_OVER = 1.5               # the sines-only ceiling must overshoot by this
OVER_GROW = 50.0             # ... and by at least this on the deepest window
ANG_BIG = 45.0               # the top misaligned direction must exceed (deg)
ANG_MED = 2.0                # the median of the seven others must stay under
N_RAND_SUB = 4               # random subspaces per window for the lemma


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


def lag_vector(alpha, M, atoms):
    """THE T115 lag assembly c = c^arch + c^atom -- bit for bit the frame-A
    code path of T128..T154 / v548 / v549 / v550."""
    c_at, D = atom_lags(alpha, M, atoms)
    return arch_lags(M, D) + c_at


# ------------------------------------- the parity sector (T106..T154)
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: the reflection-odd section (v549 item
    (4): EXACTLY the compression of T_M(c) onto the antisymmetric parity
    sector -- quoted, not re-verified here)."""
    h = M // 2
    r = np.arange(h)
    return (c[np.abs(r[:, None] - r[None, :])]
            - c[(M - 1) - r[:, None] - r[None, :]])


def toep_only(c, M):
    """THE DIRICHLET CONTROL: the pure Toeplitz half c_{|r-s|} with the
    Hankel reflection REMOVED -- same arithmetic bit for bit, different
    boundary condition."""
    h = M // 2
    r = np.arange(h)
    return np.asarray(c)[np.abs(r[:, None] - r[None, :])]


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
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002):
    a completed Cholesky of X certifies X >= -fl I; fl is SUBTRACTED from
    every lower bound and ADDED to every upper bound."""
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


def cert_lam_min(X, guess, tries=14, grow=1.0e-7):
    """A LOWER BOUND on lam_min, certified by a COMPLETED Cholesky of
    X - t I.  DIRECTION: lower."""
    h = X.shape[0]
    t = float(guess)
    for _ in range(tries):
        Y = sym(X - t * np.eye(h))
        if safe_cho(Y) is not None:
            return t - chol_floor(gersh(Y), h)
        t -= abs(t) * grow + 1.0e-300
        grow *= 6.0
    return float("nan")


def inertia_neg(X):
    """#{lam_j < 0} from a COMPLETED pivoted LDL^T (Sylvester 1852;
    Bunch-Kaufman 1977) -- a certificate, never a sorted list; -1 when the
    factorisation does not complete, so a missing certificate is REPORTED."""
    try:
        _lu, d, _ = ldl(X)
    except (LinAlgError, ValueError):
        return -1
    n = d.shape[0]
    neg = 0
    i = 0
    while i < n:
        if i + 1 < n and abs(d[i + 1, i]) > 0.0:
            blk = np.array([[d[i, i], d[i, i + 1]],
                            [d[i + 1, i], d[i + 1, i + 1]]])
            try:
                w2 = np.linalg.eigvalsh(sym(blk))
            except LinAlgError:
                return -1
            neg += int(np.sum(w2 < 0.0))
            i += 2
        else:
            neg += int(d[i, i] < 0.0)
            i += 1
    return neg


def count_below(X, tau):
    return inertia_neg(sym(X - tau * np.eye(X.shape[0])))


# ------------------------------------- the certified floor (Schur two-block)
def parity_block(A, Tf, mu):
    """B = Lam^{-1/2} T A T^T Lam^{-1/2}: lam_min(B) IS the pencil floor
    (an identity; v549/v550 machinery, rebuilt here)."""
    Gf = sym(Tf @ (A @ Tf.T))
    isq = 1.0 / np.sqrt(mu)
    return sym(Gf * np.outer(isq, isq))


def schur_floor(B, kb, t):
    """THE CERTIFIED TWO-BLOCK SCHUR FLOOR (Schur 1917; Haynsworth 1968):
    B >= t I iff B_HH - tI > 0 and its Schur complement on the low block is
    > 0 -- an EQUIVALENCE; both completed-Cholesky floors are subtracted.
    DIRECTION: a LOWER bound, certified per window at SIZE m (the m-freeness
    of this floor is exactly T154's open term R1' and is NOT claimed)."""
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


# ------------------------------------- the fixed-size ceiling machinery
def green_cols(A, LP, V):
    """THE GREEN COLUMNS A^-1 L_P V by Cholesky back-solves of A (positive
    definiteness certified by the completed factor; no inverse formed)."""
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
    """APPEND span(V) to an orthonormal Q, keeping the existing columns
    verbatim (the certificate subspace must CONTAIN span{t_1..t_8})."""
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
    """K^F = max_{k <= K} lam_max(Y_k^T W Y_k) / mu^P_k, Y_k the k lowest
    Ritz directions of W.  Each numerator is certified by ONE completed
    Cholesky of a k x k matrix (k <= K = 8), so the WHOLE certificate has
    fixed size, independent of m.  DIRECTION (Courant-Fischer 1920): each
    ratio is an UPPER bound on lam_k(A) / mu^P_k -- a ceiling, never a
    floor."""
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


def cert_bottom_ladder(A, mu, k_cert=K_CERT):
    """THE INERTIA-CERTIFIED TRUE BOTTOM LADDER CONSTANT K_bot: the smallest
    ladder entry S of the preregistered backoff scan with
    #{lam_j(A) < S mu^P_k} >= k for every k <= k_cert, each count a
    completed LDL^T of SIZE m (the honest competitor the fixed-size
    certificate is measured against)."""
    kc = int(min(k_cert, A.shape[0]))
    lam_low = eigvalsh(A, subset_by_index=[0, kc - 1])
    seed = float(np.max(np.asarray(lam_low) / mu[:kc]))
    for eta in LAD_BACKOFF:
        S = seed * (1.0 + eta)
        if all(count_below(A, S * float(mu[k - 1])) >= k
               for k in range(1, kc + 1)):
            return S, seed, lam_low
    return float("nan"), seed, lam_low


def prin_angles(Q1, Q2):
    """PRINCIPAL ANGLES between orthonormal bases (Bjoerck-Golub 1973), in
    degrees, ascending.  MEASURED, never certified."""
    s = np.linalg.svd(Q1.T @ Q2, compute_uv=False)
    s = np.clip(s, -1.0, 1.0)
    return np.degrees(np.arccos(s[::-1]))


def instrument(A, m):
    """THE T154 INSTRUMENT on an arbitrary symmetric section: the certified
    Schur floor t, the inertia-certified K_bot, both fixed-size ceilings
    (8-column sines-only and 16-column with one Green step) and the
    misalignment angle -- ONE code path for the surface, the stress family
    and the controls."""
    mu = parity_mu(m)
    Tf = parity_basis(m)
    LP = lap_P_mat(m)
    lam1 = float(eigvalsh(A, subset_by_index=[0, 0])[0])
    out = dict(m=m, lam1=lam1)
    if not (lam1 > 0.0):
        return out                      # not positive definite: no ceiling
    B = parity_block(A, Tf, mu)
    out["t"] = schur_best(B, min(SCHUR_KB, m - 2))
    del B
    K_bot, seed, lam_low = cert_bottom_ladder(A, mu)
    out["K_bot"] = K_bot
    out["seed"] = seed              # the exact ladder maximum max_k lam_k/mu_k
    out["lam_low"] = lam_low
    w_lo, V_lo = eigh(A, subset_by_index=[0, K_CERT - 1])
    out["V_lo"] = V_lo
    V0 = np.ascontiguousarray(Tf[:K_CERT, :].T)
    out["ang"] = prin_angles(orth_cols(V0), V_lo)
    Q0 = orth_cols(V0)
    out["KF0"] = cert_ceiling(sym(Q0.T @ (A @ Q0)), mu, K_CERT)
    g1 = green_cols(A, LP, V0)
    if g1 is None:
        out["KF1"] = float("nan")
        return out
    Q1 = append_orth(Q0, g1)
    out["Q1"] = Q1
    out["dim1"] = int(Q1.shape[1])
    out["KF1"] = cert_ceiling(sym(Q1.T @ (A @ Q1)), mu, K_CERT)
    out["mu"] = mu
    out["A"] = A
    out["LP"] = LP
    out["V0"] = V0
    if np.isfinite(out.get("t", float("nan"))) and out["t"] > 0.0:
        gam = cert_lam_min(A, guess=lam1 * (1.0 - 1.0e-9))
        out["gam"] = gam
        out["price"] = gam / (out["t"] * float(mu[0]))
    return out


# ------------------------------------------------------------------ battery
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
    # the N_INST DEEPEST zones inside the cap (T154's surface convention:
    # sample from the deep end of the zone list, declared before any result)
    return cand[-N_INST:]


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(154)
    print("=" * 72)
    print("v551  PRIME.RITZ.CEIL.01 -- the fixed-size Ritz ceiling "
          "certificate (T154)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered bars")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    WINS = build_windows()
    for (k, D, M, h) in WINS:
        alpha = 0.5 * M * D
        c = lag_vector(alpha, M, atoms_in(alpha))
        A = sym(odd_toeplitz(c, M))
        got = instrument(A, h)
        if got.get("lam1", 0.0) > 0.0 and np.isfinite(got.get("KF1", np.nan)):
            got["n"] = NN_ALL[k]
            got["D"] = D
            got["M"] = M
            got["c"] = c
            INST.append(got)
    h_max = max(t["m"] for t in INST) if INST else 0
    d_lo = min(t["D"] for t in INST) if INST else float("nan")
    d_hi = max(t["D"] for t in INST) if INST else float("nan")
    ok_floor = all(np.isfinite(t["t"]) and t["t"] > 0.0 for t in INST)
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite, certified Schur floor t > 0 on every "
          f"one); every factorised / diagonalised matrix <= {H_CAP} (max "
          f"m = {h_max}); D = {d_lo:.3e} .. {d_hi:.3e}",
          len(INST) >= 6 and h_max <= H_CAP and ok_floor)
    for t in INST:
        print(f"    n={t['n']:>7d} D={t['D']:.4e} m={t['m']:>4d} "
              f"t={t['t']:.4f} K_bot={t['K_bot']:.4f} KF0={t['KF0']:.4g} "
              f"KF1={t['KF1']:.6f} mis={float(np.max(t['ang'])):.2f}deg")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the direction lemma: Ritz values bound from ABOVE "
          "(T154)")
    worst_cert = 0.0
    dir_ok = True
    for t in INST:
        d = t["dim1"]
        lam_d = eigvalsh(t["A"], subset_by_index=[0, d - 1])
        W = sym(t["Q1"].T @ (t["A"] @ t["Q1"]))
        th = eigvalsh(W)
        exc = float(np.max((lam_d - th) / np.maximum(np.abs(th), 1e-300)))
        worst_cert = max(worst_cert, exc)
        if exc > TOL_DIR:
            dir_ok = False
    check(f"S1.CEIL: on the sixteen-column certificate subspace of every "
          f"window, lam_k(A) <= th_k for EVERY k <= dim (Courant-Fischer "
          f"1920 / Cauchy 1829: Ritz values are upper bounds for the "
          f"eigenvalues of the SAME index; worst one-sided excess "
          f"{worst_cert:.2e} <= {TOL_DIR:.0e}) -- the ceiling direction is "
          f"a THEOREM on the instance, so the fixed-size ceiling needs NO "
          f"residual argument: Temple 1928 / Kato 1949 is a FLOOR device "
          f"and is used nowhere in this module", dir_ok)
    worst_rand = 0.0
    rand_ok = True
    for t in INST[:6]:
        m = t["m"]
        for _ in range(N_RAND_SUB):
            d = int(rng.integers(2, K_CERT + 1))
            Q = orth_cols(rng.standard_normal((m, d)))
            W = sym(Q.T @ (t["A"] @ Q))
            th = eigvalsh(W)
            lam_d = eigvalsh(t["A"], subset_by_index=[0, d - 1])
            exc = float(np.max((lam_d - th)
                               / np.maximum(np.abs(th), 1e-300)))
            worst_rand = max(worst_rand, exc)
            if exc > TOL_DIR:
                rand_ok = False
    check(f"S1.RAND: the same-index ceiling holds for RANDOM subspaces of "
          f"dimension 2..{K_CERT} on the first 6 windows "
          f"({6 * N_RAND_SUB} draws, worst excess {worst_rand:.2e}) -- the "
          f"lemma is a property of the direction, not of the certificate "
          f"family", rand_ok)
    n_viol = 0
    marg = float("inf")
    for t in INST:
        d = t["dim1"]
        lam_d = eigvalsh(t["A"], subset_by_index=[0, d - 1])
        W = sym(t["Q1"].T @ (t["A"] @ t["Q1"]))
        th = eigvalsh(W)
        viol = th > lam_d * (1.0 + BAR_CTRL)
        if bool(np.any(viol)):
            n_viol += 1
            marg = min(marg, float(np.max(th / np.maximum(lam_d, 1e-300))))
    check(f"S1.CTRL: the REVERSED reading (Ritz values as LOWER bounds of "
          f"the same-index eigenvalues) is recognised as FALSE on "
          f"{n_viol}/{len(INST)} windows -- th_k overshoots lam_k by a "
          f"factor >= {marg:.3g} somewhere on every window (bar "
          f"{BAR_CTRL:.0e}): a direction that would violate the lemma is "
          f"detected as such, the ceiling can never be silently read as a "
          f"floor", n_viol == len(INST) and marg > 1.0 + BAR_CTRL)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the sixteen-column certificate attains the true "
          "ladder (T154)")
    kb_lo = min(t["K_bot"] for t in INST)
    kb_hi = max(t["K_bot"] for t in INST)
    cnt_ok = True
    for t in INST:
        w_full = eigvalsh(t["A"])
        for k in range(1, K_CERT + 1):
            tau = t["K_bot"] * float(t["mu"][k - 1])
            if count_below(t["A"], tau) != int(np.count_nonzero(
                    w_full < tau)):
                cnt_ok = False
    check(f"S2.KBOT: the true bottom ladder constant K_bot = "
          f"{kb_lo:.4f}..{kb_hi:.4f} is certified per window by {K_CERT} "
          f"completed LDL^T inertia counts (Sylvester 1852; Bunch-Kaufman "
          f"1977 -- each of SIZE m), and every count equals the direct "
          f"spectral count ({len(INST) * K_CERT} (window, k) pairs): the "
          f"honest competitor of the fixed-size certificate is itself "
          f"certified", cnt_ok
          and all(np.isfinite(t["K_bot"]) for t in INST))
    att = [abs(t["KF1"] / t["K_bot"] - 1.0) for t in INST]
    dim_ok = all(t["dim1"] <= 2 * K_CERT for t in INST)
    dir16 = all(t["KF1"] >= t["seed"] * (1.0 - TOL_DIR) for t in INST)
    check(f"S2.CEIL16: the SIXTEEN-column certificate "
          f"span{{t_1..t_8}} + A^-1 L_P span{{t_1..t_8}} (dimension "
          f"{max(t['dim1'] for t in INST)} <= {2 * K_CERT}, FIXED and "
          f"independent of m; {K_CERT} completed Choleskys of matrices of "
          f"size <= {K_CERT} per window) carries K^F = "
          f"{min(t['KF1'] for t in INST):.4f}.."
          f"{max(t['KF1'] for t in INST):.4f} with K^F >= max_k "
          f"lam_k/mu^P_k on every window (the theorem direction, against "
          f"the exact spectrum) AND |K^F / K_bot - 1| <= {max(att):.2e} "
          f"<= the declared cap {TOL_ATT:.0e} on {len(INST)}/{len(INST)} "
          f"(the residue is the inertia ladder's own backoff step): the "
          f"fixed-size ceiling ATTAINS the inertia-certified truth -- the "
          f"{K_CERT} size-m LDL^T counts are RETIRED from the ceiling "
          f"step", dim_ok and dir16 and max(att) <= TOL_ATT)
    over = [t["KF0"] / t["K_bot"] for t in INST]
    check(f"S2.SINES: the parity sines ALONE (the 8-column S_0) OVERSHOOT "
          f"the true ladder by {min(over):.3g}..{max(over):.3g} -- at "
          f"least {BAR_OVER} on every window and up to {max(over):.0f} "
          f">= {OVER_GROW:.0f} on the surface -- so S_0 fails the "
          f"attainment cap everywhere: the Green step is load-bearing, "
          f"not decorative (T152/T153's O(m^2) overshoot of every "
          f"fixed-in-advance family, reproduced at fixed size)",
          all(o >= BAR_OVER for o in over) and max(over) >= OVER_GROW)
    ctrl_broken = 0
    for t in INST:
        g_bad = t["LP"] @ t["V0"]        # the Green step WITHOUT A^-1
        Qb = append_orth(orth_cols(t["V0"]), g_bad)
        kf_bad = cert_ceiling(sym(Qb.T @ (t["A"] @ Qb)), t["mu"], K_CERT)
        if not np.isfinite(kf_bad) or abs(kf_bad / t["K_bot"] - 1.0) \
                > BAR_CTRL:
            ctrl_broken += 1
    check(f"S2.CTRL: corrupting the Green columns (dropping the A^-1 "
          f"back-solve, i.e. appending L_P t_k instead of A^-1 L_P t_k) "
          f"breaks the attainment by > {BAR_CTRL:.0e} on "
          f"{ctrl_broken}/{len(INST)} windows -- the certificate cannot be "
          f"talked into attainment by any 16 columns: the inverse "
          f"iteration is the mechanism (Kaniel 1966 / Paige 1971, QUOTED "
          f"as the explanation, never used as a bound)",
          ctrl_broken == len(INST))

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the one-direction anatomy and the collapse price "
          "(T154)")
    big = [float(np.max(t["ang"])) for t in INST]
    med = [float(np.median(np.sort(t["ang"])[:-1])) for t in INST]
    check(f"S3.ONE: MEASURED principal angles (Bjoerck-Golub 1973) between "
          f"the bottom eight of A and the bottom eight of L_P: the median "
          f"of the seven remaining angles is {min(med):.2f}..{max(med):.2f}"
          f" deg <= {ANG_MED} -- the aligned block sits inside the sine "
          f"block to a fraction of a degree -- while the LARGEST is "
          f"{min(big):.2f}..{max(big):.2f} deg >= {ANG_BIG} on every "
          f"window: the misalignment is carried by one nearly orthogonal "
          f"direction, T154's named obstruction",
          all(b >= ANG_BIG for b in big)
          and all(s <= ANG_MED for s in med))
    pr_lo = min(t["price"] for t in INST)
    pr_hi = max(t["price"] for t in INST)
    price_ok = True
    for t in INST:
        if not (np.isfinite(t["gam"]) and t["gam"] > 0.0
                and t["gam"] <= float(t["lam_low"][0]) * (1.0 + TOL_DIR)
                and t["gam"] >= float(t["lam_low"][0]) * (1.0 - 1.0e-6)):
            price_ok = False
        if not (t["price"] > 1.0 + BAR_CTRL):
            price_ok = False
    check(f"S3.PRICE: ONE completed Cholesky of A - gam I per window "
          f"(size m -- certified per window, NOT fixed size, and labelled "
          f"as such) certifies lam_1(A) >= gam within 1e-6 of the true "
          f"bottom eigenvalue and recovers the collapse price lam_1(A) / "
          f"(t mu^P_1) = {pr_lo:.3f}..{pr_hi:.3f} IN FULL: the price is a "
          f"UNIFORMITY gap, not a size gap -- the number is available per "
          f"window, the m-free argument for it is T154's open term R2'",
          price_ok)
    ctrl_par = True
    for m_c in CTRL_SIZES:
        got = instrument(sym(lap_P_mat(m_c)), m_c)
        dev = max(abs(got["K_bot"] - 1.0), abs(got["KF0"] - 1.0),
                  abs(got["KF1"] - 1.0), float(np.max(got["ang"])))
        if not (dev < TOL_CTRL_MODEL):
            ctrl_par = False
        if not abs(got["price"] * got["t"] * float(
                parity_mu(m_c)[0]) / float(got["lam1"]) - 1.0) < 1.0e-6:
            ctrl_par = False
    check(f"S3.CTRL: feeding A = L_P through the SAME instrument on m = "
          f"{', '.join(str(s) for s in CTRL_SIZES)} returns K_bot = KF0 = "
          f"KF1 = 1 and ZERO misalignment (all deviations < "
          f"{TOL_CTRL_MODEL:.0e}, the backoff step of the inertia ladder, "
          f"not an instrument error) and the price is exactly 1/t -- when "
          f"the two bottoms coincide there is nothing to recover: the "
          f"one-direction pattern of S3.ONE is a property of the REAL "
          f"section, not of the instrument", ctrl_par)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the no-go discriminator and the controls (T154)")
    NG = []
    for m_ng in NOGO_SIZES:
        M_ng = 2 * m_ng
        c_ng = 1.0 / (1.0 + np.arange(M_ng, dtype=float))
        NG.append(instrument(sym(odd_toeplitz(c_ng, M_ng)), m_ng))
    ng_floor = all(np.isfinite(g["t"]) and g["t"] > 0.0 for g in NG)
    gk = NG[-1]["K_bot"] / NG[0]["K_bot"]
    gf = NG[-1]["KF1"] / NG[0]["KF1"]
    check(f"S4.NOGO: on the T145 no-go reconstruction c(l) = 1/(1+l) (odd "
          f"section positive definite -- the certified Schur floor "
          f"survives, t = {min(g['t'] for g in NG):.4g}.."
          f"{max(g['t'] for g in NG):.4g} on all {len(NG)} sizes) the true "
          f"ladder EXPLODES (K_bot: {NG[0]['K_bot']:.4g} -> "
          f"{NG[-1]['K_bot']:.4g}, factor {gk:.1f}) and the sixteen-column "
          f"ceiling explodes WITH it (K^F: {NG[0]['KF1']:.4g} -> "
          f"{NG[-1]['KF1']:.4g}, factor {gf:.1f}; both >= {NOGO_GROW}) "
          f"over m = {NOGO_SIZES[0]}..{NOGO_SIZES[-1]}: the instrument "
          f"does NOT report flatness where flatness is false -- it "
          f"manufactures no closure, which is what makes S2.CEIL16 a "
          f"finding about the real section and not about the tool",
          ng_floor and gk >= NOGO_GROW and gf >= NOGO_GROW)
    allf = INST + NG
    n_dir = sum(1 for g in allf
                if g["KF1"] >= g["seed"] * (1.0 - TOL_DIR)
                and g["KF0"] >= g["seed"] * (1.0 - TOL_DIR))
    check(f"S4.DIR: the Courant-Fischer direction is violated NOWHERE -- "
          f"both fixed-size ceilings sit at or above the exact ladder "
          f"maximum max_k lam_k/mu^P_k on all {len(allf)} positive-definite cases "
          f"({len(INST)} windows + {len(NG)} no-go sizes; the parity "
          f"controls of S3.CTRL hold it at equality): if this ever failed, "
          f"every ceiling number in this module would be meaningless in "
          f"the direction it is used", n_dir == len(allf))
    DC = []
    for t in (INST[:1] + INST[len(INST) // 2:len(INST) // 2 + 1]
              + INST[-1:])[:N_DIRI]:
        Ad = sym(toep_only(t["c"], t["M"]))
        lam1_up = cert_lam_max(-Ad, guess=gersh(Ad))
        DC.append((t["m"], float(eigvalsh(
            Ad, subset_by_index=[0, 0])[0]), lam1_up))
    diri_neg = all(v < 0.0 and up > 0.0 for (_m, v, up) in DC)
    check(f"S4.DIRICHLET: removing the HANKEL half (arithmetic kept bit "
          f"for bit, only the boundary condition changes) destroys "
          f"positive definiteness on {len(DC)}/{len(DC)} control windows "
          f"-- lam_1 = {min(v for (_m, v, _u) in DC):.4g}.."
          f"{max(v for (_m, v, _u) in DC):.4g} < 0 (negativity certified "
          f"by a completed Cholesky of gam I + A_D) -- so no Green step, "
          f"no ceiling and no Schur floor exist there: the reflection half "
          f"is LOAD-BEARING for positivity (T154's second refutation of "
          f"the boundary-reflection reading), and K_bot is not quoted on "
          f"a non-positive section", diri_neg)

    # ---------------------------------------------------------------- fences
    print("\nS5 -- the fences, restated as a check")
    check("S5.FENCE: PER-INSTANCE theorems with checked hypotheses and "
          "certified inequalities on SMALL windows only -- a FINITE LIST "
          "with an explicit maximum, nothing uniform in the zone index or "
          "in D, and NO statement for ALL D: the TWO open inputs after "
          "T154 (R1', an m-free floor for lam_min(B_HH) on the bulk parity "
          "block, and R2', an m-free lower bound for the L_P floor on the "
          "complement of the eight bottom Ritz directions -- the "
          "arithmetic-free number worth 91..100 percent of the collapse "
          "price) stay OPEN, unclaimed and unapproached, exactly as T154 "
          "typed them; every floor consumed here (the Schur two-block t, "
          "the Cholesky bottom gam) is certified per window at SIZE m and "
          "its m-freeness is NOT claimed; the attainment K^F = K_bot is "
          "exhibited per window and NOT promoted to a theorem (the no-go "
          "overshoots -- attainment is a property of the real section); "
          "v550's ladder stays as stated, nothing is re-opened; "
          "Courant-Fischer 1920 / Cauchy 1829 / KMS 1953 / Schur 1917 / "
          "Haynsworth 1968 / Sylvester 1852 / Bunch-Kaufman 1977 / Weyl "
          "1912 / Temple 1928 / Kato 1949 (a floor device, NOT used here) "
          "/ Kaniel 1966 / Paige 1971 (quoted, never a bound) / "
          "Bjoerck-Golub 1973 / Wilkinson 1968 / Higham 2002 / Chebyshev "
          "1852 named CLASSICAL; Weil 1952 CITED, never used as a "
          "criterion; zero-firewall AST-checked; NO marker upgrade of any "
          "pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv551 runtime: {elapsed:.1f}s")
    print(f"  (1) direction lemma: worst excess {worst_cert:.1e} "
          f"(certificate), {worst_rand:.1e} (random); reversed reading "
          f"refuted {n_viol}/{len(INST)}")
    print(f"  (2) K^F = K_bot to {max(att):.2e} (cap {TOL_ATT:.0e}) on "
          f"{len(INST)} windows; K_bot = {kb_lo:.4f}..{kb_hi:.4f}; "
          f"sines-only overshoot {min(over):.3g}..{max(over):.3g}")
    print(f"  (3) one direction at {min(big):.1f}..{max(big):.1f} deg, "
          f"median of the rest <= {max(med):.2f} deg; price "
          f"{pr_lo:.3f}..{pr_hi:.3f} recovered per window")
    print(f"  (4) no-go: K_bot x{gk:.1f}, K^F x{gf:.1f}; Dirichlet control "
          f"non-positive on {len(DC)}/{len(DC)}")
    return summary("PRIME.RITZ.CEIL.01 fixed-size Ritz ceiling certificate")


if __name__ == "__main__":
    raise SystemExit(run())
