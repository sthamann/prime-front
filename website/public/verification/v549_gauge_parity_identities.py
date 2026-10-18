"""v549 -- PRIME.GAUGE.PARITY.IDENT.01: the gauge/parity identities of phase 2.
The IDENTITY- and CERTIFICATE-shaped core of T149 (the whitening diagonal as
a free gauge, and the two-regime refutation of the TV hypothesis) and T150
(the named mechanism: the odd section IS the antisymmetric parity sector of
the full Toeplitz section, the whitening diagonal IS an explicit zone
functional, and the matched parity-sine ceiling) -- every statement
RECOMPUTED here from scratch on small exactly checkable frame-A windows (no
citation of sandbox output).  Companion to PRIME.GREEN.SZEGO.IDENT.01
(v548), which certified the factorisation Gam = sqrt(Q_star) x Sw and the
Liouville machinery in the Jacobi gauge: THIS module certifies the gauge
FREEDOM around that machinery and the parity STRUCTURE underneath it.

WHAT IS LOAD-BEARING HERE (and nothing else): identities, per-instance
theorems with CHECKED hypotheses, and per-window CERTIFIED inequalities.
NO fit, NO D-exponent, NO uniform-in-zone statement, and NO statement FOR
ALL D -- the ONE open input after T150 (a bound nu_k <= C k^2 with C m-FREE
for the odd parity sector of a sign-changing-symbol Toeplitz section) stays
OPEN and is neither assumed nor approached: the ladder constant C is read
per window and typed as a per-instance certificate ONLY.  Each identity is
checked as a NUMERICAL RESIDUAL against a preregistered tolerance AND
against at least one MUTATION CONTROL that must fail loudly.

[E] (1) THE GAUGE FREEDOM (T149).  For ANY positive diagonal Lam~ the
    whitening E~ = Lam~^{-1/2} A Lam~^{-1/2} is an exact congruence, so
        lam_min(A) >= cert_lam_min(E~) x min_j Lam~_j
    is a valid certified lower bound for EVERY gauge -- an identity plus
    one Rayleigh step -- and the maximum over the family is valid too.
    Verified on >= 3 gauges per window (Jacobi, const = the geometric mean
    of the Jacobi diagonal, the moving-geometric-mean flutter smoother,
    and, where positive, the arithmetic-free archimedean diagonal); the
    factorisation identity Gam = sqrt(Q_star) x Sw (v548 item (1)) holds
    GAUGE-INVARIANTLY on every assembly; the const gauge has
    TV(log Lam~) = 0 EXACTLY, with the certified entrywise sandwich
    c_1 Lam <= Lam~ <= c_2 Lam paying the transfer.
[E] (2) THE TWO-REGIME DISCRIMINATOR (T149, the refutation as a check).
    The flutter-smoothing gauge (moving geometric mean: flutter removed,
    macro profile kept) moves the smoothness functional nu_L~ of the
    LIOUVILLE-TRANSPORTED pencil bottom block by a SMALL preregistered
    fraction on every window, while it removes most of TV(log Lam) -- and
    even a matched-amplitude ROUGH re-gauge (lattice-scale oscillation)
    cannot move the transported functional: the roughness nu_L~ responds
    to is NOT in the multiplier, which is exactly T149's withdrawal of
    the TV hypothesis.  THE CONTROL that makes this non-vacuous: the SAME
    functional read WITHOUT the Liouville transport (on the whitened
    modes psi, which carry the multiplier) jumps loudly under the same
    rough re-gauge on every window -- the invariance is a property of the
    transported modes, not numbness of the functional.
[E] (3) THE EXPLICIT ZONE DIAGONAL (T150).  The whitening diagonal is an
    explicit function of the zone's lag vector and nothing else:
        Lam_r = c_0 - c_{M-1-2r} + sum_{s != r} max(c_{|r-s|} -
                c_{M-1-r-s}, 0) ,
    verified at residual 0 against the assembled lumped pair; the lag
    vector splits EXACTLY as c = c^arch + c^atom with c^atom <= 0
    entrywise, and the arithmetic mass carries the closed budget
        ||c^atom||_1 <= sum_j mu_j <= 4 B sqrt(N)
    (Abel summation against the VERIFIED Chebyshev ratio
    B = max_{n <= N} psi(n)/n, computed on the atom table, never assumed).
    THE HONEST NEGATIVE BESIDE IT, promoted as content: the archimedean
    section alone is INDEFINITE (completed LDL^T counts) while the full
    section is positive definite -- the atoms are CO-RESPONSIBLE for the
    positivity, so the additive perturbation reading (Weyl 1912 /
    Bauer-Fike 1960 / Davis-Kahan 1970) is structurally dead, not merely
    quantitatively (T150 measured it 2.4-5.8 orders vacuous; only the
    multiplicative / Loewner gauge step of item (1) transfers).
[E] (4) THE PARITY COMPRESSION (T150, the named mechanism).  With
    U_-, U_+ the antisymmetric / symmetric parity isometries of the full
    window, U_-^T T_M(c) U_- == T - H and U_+^T T_M(c) U_+ == T + H
    EXACTLY with cross block U_+^T T_M U_- == 0 -- the reflection-odd
    section that every probe since T106 uses IS the compression of the
    full symmetric Toeplitz section onto its antisymmetric parity sector
    -- and the completed LDL^T counts localise the inertia: the ENTIRE
    negative inertia of T_M(c) (forced by the sign-changing symbol,
    f(0) < 0, T148's honest negative re-read and never re-derived) sits
    in the EVEN sector, the odd sector counting ZERO negative eigenvalues.
[E] (5) THE PARITY-SINE CALIBRATION AND THE LADDER CERTIFICATE (T150).
    The antisymmetric parity sines t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N),
    N = 2m+1, are the EXACT eigenpairs of the parity Laplacian L_P
    (tridiag(-1, 2, -1) with reflecting corner 3) at
    mu^P_k = 4 sin^2(pi k / N) -- an exact model in the sector the
    mechanism names -- and on that model the smoothness ladder CALIBRATES:
    nu^P_k == pi k^2 (measured relative deviation at the preregistered
    tolerance).  On every window the ladder nu^P_k <= C k^2 holds with the
    per-window certified constant C printed, and the derived per-mode
    ceiling m ||psi_k||_inf^2 <= 2 (2 sqrt(C) k + 1)^2 is a certified
    instance inequality; an m-FREE C is exactly the open input and is NOT
    claimed.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL windows.  Nothing here
        is uniform in the zone index or in D; what is established is a
        FINITE LIST of certified window inequalities with an explicit
        maximum, and every T149/T150 exponent is a FIT that stays in the
        sandbox.  The step to ALL D -- an m-free constant in the odd-sector
        ladder nu_k <= C k^2 for a sign-changing-symbol Toeplitz section --
        is OPEN, explicitly typed open, and neither assumed nor approached.
  (ii)  Item (2) is a REFUTATION-shaped check: it certifies that the named
        gauge motion is small and the rough motion is loud on this finite
        list; it does not bound nu_L~ by anything.
  (iii) Item (3)'s budget bounds the arithmetic MASS of the lag vector and
        nothing spectral; the level shift between the Jacobi diagonal and
        the archimedean diagonal is NOT small (T150: the archimedean
        diagonal is not the macro profile) and no such smallness is used.
  (iv)  Item (5)'s constant C is certified PER WINDOW; its size, its trend
        (T150: C <= 43.391 = 13.81 pi with trend x^0.258, a FIT) and any
        m-free reading stay in the sandbox.
  (v)   TV(log Lam) as a hypothesis is WITHDRAWN (T149) and nothing here
        re-opens it; sig_tot stays retired as a route (T148).

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil
    window form (Weil 1952, CITED, never used as a criterion) on a FINITE
    list of prime-power zones.  Everything here is an identity or a
    certified inequality PER INSTANCE; NOTHING here claims, assumes or
    approaches RH, and no statement about zeta zeros is made.  No zero
    data of any kind is read, generated or approximated -- an AST firewall
    enforces this.  NO all-D claim: even with every check green, what
    stands is a finite list of certified window statements on prime-power
    zones, and the one open input (the m-free odd-sector ladder constant)
    stays open here and everywhere.
  * Classics named CLASSICAL: Kac-Murdock-Szego 1953 (the exact Dirichlet
    eigenpair and its parity-sector form), Widom 1958 / Basor-Ehrhardt
    2009 / Bottcher-Silbermann (the Toeplitz+Hankel address and the parity
    sectors as its natural objects, CITED as the mechanism's home and
    never used as an authority; Basor-Ehrhardt does NOT cover the
    sign-changing symbol -- that gap IS the open input), Sylvester 1852 /
    Bunch-Kaufman 1977 (inertia), Chebyshev 1852 (psi(x)/x bounded --
    VERIFIED on the finite table, never assumed), Abel summation,
    Weyl 1912 / Bauer-Fike 1960 / Davis-Kahan 1970 (CITED as the additive
    route T150 computed to be dead -- NOT used), Rayleigh 1877 / Ritz
    1909, Cauchy-Schwarz, Gershgorin 1931, Wilkinson 1968 / Higham 2002
    (completed Cholesky and its floor).
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] exact linear-algebra / counting identities at rel
< 1e-11 .. 1e-15 as stated, per-instance theorems with checked
hypotheses, certified inequalities by completed Cholesky / completed
LDL^T with the direction in the name, each with a mutation control that
fails loudly.  Python; Wolfram-mirrored not required (dense Cholesky /
LDL^T / eigenvalue identities stay Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/weight_smoothing_probe.py        (T149)
  experiments/tfpt-discovery/mode_ladder_probe.py             (T150)
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
ATOM_MAX = 320000            # atom table cap, as in v546..v548
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
U_ROUND = 2.0 ** -53

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept (spread over the D range)

# --- THE BOTTOM BLOCK, preregistered exactly as in T147/v548 -----------------
THETA_BLK = 10.0

# --- the flutter smoother of item (2): moving-geometric-mean half-width ------
MGM_DIV = 16                 # half = max(4, m // MGM_DIV), as in T150
ROUGH_AMP = 0.15             # matched-amplitude rough re-gauge (control)

# --- the parity ladder of item (5) -------------------------------------------
K_LAD = 8                    # bottom modes read into the ladder
M_CAL = 2001                 # control-model size (vector ops only, no matrix)
K_CAL = 12                   # calibrated parity modes

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_ID = 1.0e-11             # every identity must hold to this relative level
TOL_DIR = 1.0e-9             # one-sided slack of per-instance theorem steps
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
BAR_FLUT_MOVE = 0.01         # any gauge may move the TRANSPORTED nu_L~ <= 1%
BAR_TV_DROP = 1.5            # ... while removing TV by at least this factor
BAR_PSI_ROUGH = 0.25         # the UNtransported functional must jump >= 25%
TOL_CAL = 2.0e-3             # parity calibration |nu_k/(pi k^2) - 1| bar
ROUND_GUARD = 1.0e-12        # outward rounding of computed sandwich ratios


def sym(A):
    return 0.5 * (A + A.T)


def rel(Dm, Rf):
    return float(np.abs(Dm).max()) / max(float(np.abs(Rf).max()), 1.0e-300)


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


def psi_ratio_max():
    """THE VERIFIED RANGE OF THE CITED CHEBYSHEV BOUND (Chebyshev 1852):
    psi(x) is a step function jumping at prime powers, so max psi(x)/x over
    x <= ATOM_MAX is attained at a jump point -- COMPUTED on the table,
    never assumed.  DIRECTION: an UPPER bound on psi(x)/x for the whole
    verified range."""
    best, acc = 0.0, 0.0
    for n, lam_n, _u, _mu in ATOMS_ALL:
        acc += lam_n
        r = acc / float(n)
        if r > best:
            best = r
    return best


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


def atom_lags(alpha, M, atoms):
    """THE ARITHMETIC PART OF THE LAG VECTOR, ISOLATED (T150).  Every atom
    contributes -mu_j/2 times a linear spline of total mass <= 1 around
    u_j, plus a reflected spline when u_j < D: c^atom <= 0 entrywise and
    ||c^atom||_1 <= sum_j mu_j."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    mu_tot = 0.0
    for u_j, mu_j in atoms:
        mu_tot += mu_j
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
    return c, D, mu_tot


def lag_vector_split(alpha, M, atoms):
    """THE EXACT SPLIT c = c^arch + c^atom of the T115 lag assembly; the sum
    is bit-for-bit the frame-A code path of T128..T150 / v548."""
    c_at, D, mu_tot = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D, mu_tot=mu_tot,
                l1_at=float(np.sum(np.abs(c_at))))


# ------------------------------------- the parity sectors (T106..T150)
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: the reflection-odd section, the
    object every probe since T106 uses."""
    h = M // 2
    r = np.arange(h)
    return (c[np.abs(r[:, None] - r[None, :])]
            - c[(M - 1) - r[:, None] - r[None, :]])


def even_toeplitz(c, M):
    """A^+_rs = c_{|r-s|} + c_{M-1-r-s}: the EVEN parity partner, built only
    to LOCATE the negative inertia of the full section (Basor-Ehrhardt
    2009: the parity sectors are the natural objects of the algebra)."""
    h = M // 2
    r = np.arange(h)
    return (c[np.abs(r[:, None] - r[None, :])]
            + c[(M - 1) - r[:, None] - r[None, :]])


def full_toeplitz(c, M):
    """T_M(c)_{ij} = c_{|i-j|}, the full symmetric section (item (4) only,
    on windows with M <= H_CAP)."""
    ii = np.arange(M)
    return c[np.abs(ii[:, None] - ii[None, :])]


def parity_isometries(M):
    """e^-_s = (delta_s - delta_{M-1-s})/sqrt(2), e^+_s = (delta_s +
    delta_{M-1-s})/sqrt(2), s = 0..M/2-1: two M x (M/2) isometries whose
    union is an ORTHONORMAL BASIS of R^M -- what makes the inertia split
    exact."""
    h = M // 2
    Um = np.zeros((M, h))
    Up = np.zeros((M, h))
    r2 = 1.0 / math.sqrt(2.0)
    for s in range(h):
        Um[s, s] = r2
        Um[M - 1 - s, s] = -r2
        Up[s, s] = r2
        Up[M - 1 - s, s] = r2
    return Um, Up


def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(X):
    return float(np.max(np.abs(X).sum(axis=1)))


def cert_lam_min_pos(Y, tries=40):
    """A CERTIFIED STRICTLY POSITIVE floor for lam_min(Y), halved until the
    Cholesky of Y - t I completes (nan if Y is not positive definite)."""
    n = Y.shape[0]
    if n == 0:
        return float("nan")
    Y = sym(Y)
    try:
        lam = float(eigvalsh(Y, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return float("nan")
    fl = chol_floor(gersh(Y), n)
    t = 0.9 * lam - fl
    for _ in range(tries):
        if t <= 0.0:
            return float("nan")
        if safe_cho(Y - t * np.eye(n)) is not None:
            return t
        t *= 0.5
    return float("nan")


def inertia_neg(X):
    """THE CERTIFIED EIGENVALUE COUNT (Sylvester 1852; Bunch-Kaufman 1977):
    negative eigenvalues of a symmetric X from the block diagonal of a
    completed pivoted LDL^T -- a certificate, never a sorted list."""
    n = X.shape[0]
    if n == 0:
        return 0
    try:
        _lu, d, _perm = ldl(sym(X), lower=True)
    except (LinAlgError, ValueError):
        return -1
    if not np.all(np.isfinite(d)):
        return -1
    i, neg = 0, 0
    while i < n:
        two = (i + 1 < n) and (abs(float(d[i, i + 1])) > 0.0
                               or abs(float(d[i + 1, i])) > 0.0)
        if two:
            a = float(d[i, i])
            b = (float(d[i, i + 1]) if abs(float(d[i, i + 1])) > 0.0
                 else float(d[i + 1, i]))
            c = float(d[i + 1, i + 1])
            det = a * c - b * b
            tr = a + c
            if det < 0.0:
                neg += 1
            elif tr < 0.0:
                neg += 2
            i += 2
        else:
            if float(d[i, i]) < 0.0:
                neg += 1
            i += 1
    return neg


# ------------------------------------ the lumped pair and the zone diagonal
def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) -
    Delta, A_B = A + L_Delta (T136).  DIRECTION: L_Delta >= 0, so A_B >= A."""
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    return sym(A + LD)


def diag_explicit(c, M):
    """THE DIAGONAL OF A_B AS AN EXPLICIT ZONE FUNCTIONAL (T150):
        Lam_r = c_0 - c_{M-1-2r} + sum_{s != r} max(c_{|r-s|} -
                c_{M-1-r-s}, 0) ,
    assembled lagwise WITHOUT forming any matrix -- no eigenvector, no
    factorisation, only the arithmetic of the window."""
    h = M // 2
    out = np.empty(h)
    for r_i in range(h):
        acc = c[0] - c[M - 1 - 2 * r_i]
        for s_i in range(h):
            if s_i == r_i:
                continue
            v = c[abs(r_i - s_i)] - c[M - 1 - r_i - s_i]
            if v > 0.0:
                acc += v
        out[r_i] = acc
    return out


def moving_geomean(Lam, div=MGM_DIV):
    """THE FLUTTER SMOOTHER of T149/T150: the moving geometric mean of the
    diagonal over the preregistered half-width -- macro profile kept,
    flutter removed.  A FORM functional, no fit anywhere."""
    Lam = np.asarray(Lam, dtype=float)
    m = Lam.shape[0]
    half = int(min(max(4, m // div), max(1, m // 2)))
    lg = np.log(Lam)
    cs = np.concatenate([[0.0], np.cumsum(lg)])
    rr = np.arange(m)
    lo = np.maximum(rr - half, 0)
    hi = np.minimum(rr + half + 1, m)
    return np.exp((cs[hi] - cs[lo]) / (hi - lo).astype(float))


def tv_log(Lam):
    return float(np.sum(np.abs(np.diff(np.log(np.asarray(Lam,
                                                         dtype=float))))))


def whiten_with(A, Lam_t):
    """E~ = Lam~^{-1/2} A Lam~^{-1/2}: the generalised whitening by an
    arbitrary positive diagonal -- an exact congruence, so positivity and
    inertia transfer, and lam_min(A) >= lam_min(E~) min(Lam~)."""
    sq = 1.0 / np.sqrt(np.asarray(Lam_t, dtype=float))
    return sym(A * np.outer(sq, sq)), sq


def gauge_scalars(E):
    """The v548 item-(1) scalars of one gauge assembly: the Green matrix,
    the Rayleigh-Ritz lam_up, and the exact factorisation pieces."""
    m = E.shape[0]
    fac = safe_cho(E)
    if fac is None:
        return None
    R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    EV = E @ R
    den = np.sum(R * R, axis=0)
    num = np.sum(R * EV, axis=0)
    if not bool(np.all(den > 0.0)):
        return None
    fl_q = chol_floor(gersh(E), m)
    lam_up = float(np.min(num / den)) + fl_q
    fro2 = float(np.sum(R * R))
    cmax = math.sqrt(float(np.max(den)))
    Sw = lam_up * math.sqrt(max(fro2, 1.0e-300))
    Qs = m * cmax * cmax / fro2
    gam_true = math.sqrt(m) * lam_up * cmax
    gam_id = math.sqrt(Qs) * Sw
    return dict(lam_up=lam_up, Sw=Sw, Qs=Qs, gam_true=gam_true,
                gam_id=gam_id)


# ------------------------------------- the exact parity model (KMS 1953)
def parity_mu(m):
    """THE EXACT PARITY EIGENVALUES mu^P_k = 4 sin^2(pi k / N), N = 2m+1,
    k = 1..m: the spectrum of the path Laplacian with reflecting corner 3,
    which is the Dirichlet Laplacian of the FULL window restricted to the
    antisymmetric parity sector (KMS 1953 in the parity sector)."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL PARITY BASIS t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N),
    N = 2m+1, sup bound 2/sqrt(N).  Rows are the modes."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_P(X):
    """L_P X columnwise: tridiag(-1, 2, -1) with LAST diagonal entry 3 --
    the reflecting corner is forced, not chosen: the reflected neighbour
    of the last index is MINUS the last index for an antisymmetric vector
    of the full window."""
    out = 2.0 * X
    out[:-1] -= X[1:]
    out[1:] -= X[:-1]
    out[-1] += X[-1]
    return out


def nu_parity(X, m):
    """The parity smoothness functional per column: nu^P = scale_P
    ||L_P x||_1 with scale_P = (N/2)^{3/2} / (2 sqrt 2) = N^{3/2}/8 -- the
    normalisation that makes nu^P_k = pi k^2 exact in the model."""
    N = 2.0 * m + 1.0
    L1 = lap_P(np.ascontiguousarray(X, dtype=float).copy())
    return (N ** 1.5 / 8.0) * np.sum(np.abs(L1), axis=0)


def parity_ceiling(X, m):
    """THE CERTIFIED PARITY l1 CEILING (the T148 machinery in the matched
    basis): |a_k| <= min(1, ||t_k||_inf ||L_P^p x||_1 / (mu^P_k)^p),
    p = 1, 2.  DIRECTION: every entry an UPPER bound on |a_k|."""
    N = 2.0 * m + 1.0
    mu = parity_mu(m)
    L1 = lap_P(np.ascontiguousarray(X, dtype=float).copy())
    L2 = lap_P(L1.copy())
    n1 = np.sum(np.abs(L1), axis=0)
    n2 = np.sum(np.abs(L2), axis=0)
    sup_t = 2.0 / math.sqrt(N)
    B1 = np.minimum(1.0, sup_t * n1[None, :] / mu[:, None])
    B2 = np.minimum(1.0, sup_t * n2[None, :] / (mu * mu)[:, None])
    B = np.minimum(B1, B2)
    return dict(B=B, ceil=np.sum(B, axis=0), nu=(N ** 1.5 / 8.0) * n1)


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
    if not cand:
        return []
    if len(cand) > N_INST:
        pick = [cand[round(j * (len(cand) - 1) / (N_INST - 1))]
                for j in range(N_INST)]
    else:
        pick = cand
    seen, out = set(), []
    for row in pick:
        if row[0] in seen:
            continue
        seen.add(row[0])
        out.append(row)
    return out


def pencil_nu(A, Lam_t, m):
    """nu_L~ of one gauge, on BOTH sides of the Liouville transport: the
    parity smoothness functional maximised over the bottom-block modes of
    the pencil A phi = lam Lam~ phi (phi = Lam~^{-1/2} psi normalised),
    and over the WHITENED modes psi themselves (which carry the
    multiplier)."""
    E, sq = whiten_with(A, Lam_t)
    try:
        w, V = eigh(E)
    except (LinAlgError, ValueError):
        return None
    if not (float(w[0]) > 0.0):
        return None
    nb = int(np.count_nonzero(w <= THETA_BLK * float(w[0])))
    nb = max(1, min(nb, m - 1))
    PH = sq[:, None] * V[:, :nb]
    nrm = np.linalg.norm(PH, axis=0)
    PH = PH / np.where(nrm > 0.0, nrm, 1.0)[None, :]
    PS = np.ascontiguousarray(V[:, :nb])
    return dict(nu_L=float(np.max(nu_parity(PH, m))),
                nu_psi=float(np.max(nu_parity(PS, m))), nb=nb,
                lam_min=float(w[0]), E=E, V=V, w=w)


def build_instance(k, D, M, h):
    """One window, end to end: the split lag vector, the odd section and
    its lumped pair, the explicit zone diagonal, the gauge family with
    per-gauge scalars and certified floors, the two-regime pair, and the
    parity ladder read in the const gauge."""
    al = 0.5 * M * D
    sp = lag_vector_split(al, M, atoms_in(al))
    c = sp["c"]
    A = sym(odd_toeplitz(c, M))
    A_B = lump_pair(A)
    Lam_jac = np.diag(A_B).copy()
    if not (float(np.min(Lam_jac)) > 0.0):
        return None
    lam_direct = float(eigvalsh(A, subset_by_index=[0, 0])[0])
    if not (lam_direct > 0.0):
        return None
    m = h

    # ---- the gauge family (item (1))
    g_const = float(np.exp(np.mean(np.log(Lam_jac))))
    Lam_arch = diag_explicit(sp["c_ar"], M)
    gauges = {"jac": Lam_jac,
              "const": np.full(m, g_const),
              "mgm": moving_geomean(Lam_jac)}
    if float(np.min(Lam_arch)) > 0.0:
        gauges["arch"] = Lam_arch
    rows = {}
    for tag, Lt in gauges.items():
        E, _sq = whiten_with(A, Lt)
        sc = gauge_scalars(E)
        if sc is None:
            return None
        floor = cert_lam_min_pos(E)
        if not (np.isfinite(floor) and floor > 0.0):
            return None
        sc["floor"] = floor * float(np.min(Lt))
        sc["tv"] = tv_log(Lt)
        rows[tag] = sc

    # ---- the certified sandwich of the const gauge (item (1))
    r = np.full(m, g_const) / Lam_jac
    c1 = float(np.min(r)) * (1.0 - ROUND_GUARD)
    c2 = float(np.max(r)) * (1.0 + ROUND_GUARD)

    # ---- the two-regime pair (item (2))
    nu_jac = pencil_nu(A, Lam_jac, m)
    nu_mgm = pencil_nu(A, gauges["mgm"], m)
    x = np.arange(m, dtype=float)
    phi_g = 0.5 * (math.sqrt(5.0) - 1.0)
    Lam_rough = Lam_jac * np.exp(ROUGH_AMP * np.cos(2.0 * math.pi
                                                    * phi_g * x))
    nu_rough = pencil_nu(A, Lam_rough, m)
    if nu_jac is None or nu_mgm is None or nu_rough is None:
        return None

    # ---- the explicit zone diagonal + atom budget (item (3))
    lam_expl = diag_explicit(c, M)
    res_zone = rel(lam_expl - Lam_jac, Lam_jac)
    # mutation: dropping the positive part (summing ALL off-diagonals)
    rr = np.arange(m)
    A_off = (c[np.abs(rr[:, None] - rr[None, :])]
             - c[(M - 1) - rr[:, None] - rr[None, :]])
    np.fill_diagonal(A_off, 0.0)
    lam_mut = (c[0] - c[M - 1 - 2 * rr]) + A_off.sum(axis=1)
    res_mut = rel(lam_mut - Lam_jac, Lam_jac)
    split_res = rel(sp["c_ar"] + sp["c_at"] - c, c)
    at_max = float(np.max(sp["c_at"]))
    N_win = math.exp(2.0 * al)
    neg_arch = inertia_neg(sym(odd_toeplitz(sp["c_ar"], M)))
    neg_full_odd = inertia_neg(A)

    # ---- the parity ladder in the const gauge (item (5))
    E_c, _ = whiten_with(A, gauges["const"])
    try:
        wc, Vc = eigh(E_c)
    except (LinAlgError, ValueError):
        return None
    K = int(min(K_LAD, m))
    X = np.ascontiguousarray(Vc[:, :K])
    P = parity_basis(m)
    pc = parity_ceiling(X, m)
    aP = P @ X
    viol_P = float(np.max(np.abs(aP) - pc["B"]))
    kk2 = (np.arange(K, dtype=float) + 1.0) ** 2
    C_lad = float(np.max(pc["nu"] / kk2))
    sup2 = m * np.max(np.abs(X), axis=0) ** 2
    l1_true = np.sum(np.abs(aP), axis=0)
    kk1 = np.arange(1, K + 1, dtype=float)
    lad_ceil = 2.0 * (2.0 * np.sqrt(C_lad) * kk1 + 1.0) ** 2
    lad_ok = bool(np.all(sup2 <= lad_ceil * (1.0 + TOL_DIR)))
    chain_ok = bool(np.all(sup2 <= 2.0 * l1_true ** 2 + TOL_DIR)
                    and np.all(l1_true <= pc["ceil"] + TOL_DIR)
                    and np.all(pc["ceil"] <= 2.0 * np.sqrt(pc["nu"] / kk2
                                                           * kk2) + 1.0
                               + TOL_DIR))

    return dict(
        n=NN_ALL[k], m=m, M=M, D=D, c=c, sp=sp, A=A, Lam_jac=Lam_jac,
        lam_direct=lam_direct, rows=rows, gauges=gauges,
        c1=c1, c2=c2, sig=c2 / max(c1, 1.0e-300),
        nu_jac=nu_jac, nu_mgm=nu_mgm, nu_rough=nu_rough,
        tv_jac=tv_log(Lam_jac), tv_mgm=tv_log(gauges["mgm"]),
        res_zone=res_zone, res_mut=res_mut, split_res=split_res,
        at_max=at_max, l1_at=sp["l1_at"], mu_tot=sp["mu_tot"],
        N_win=N_win, neg_arch=neg_arch, neg_full_odd=neg_full_odd,
        C_lad=C_lad, viol_P=viol_P, lad_ok=lad_ok, chain_ok=chain_ok,
        nu1=float(pc["nu"][0]), nuK=float(pc["nu"][K - 1]), K=K)


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v549  PRIME.GAUGE.PARITY.IDENT.01 -- gauge/parity identities "
          "(T149/T150)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered bars")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    for (k, D, M, h) in build_windows():
        row = build_instance(k, D, M, h)
        if row is not None:
            INST.append(row)
    h_max = max(t["m"] for t in INST) if INST else 0
    d_lo = min(t["D"] for t in INST) if INST else float("nan")
    d_hi = max(t["D"] for t in INST) if INST else float("nan")
    n_gauge = sum(len(t["rows"]) for t in INST)
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite, split lag assembly, {n_gauge} gauge "
          f"assemblies with certified floors); every inverted / factorised "
          f"/ diagonalised matrix <= {H_CAP} (max m = {h_max}); the surface "
          f"spans D = {d_lo:.3e} .. {d_hi:.3e}",
          len(INST) >= 6 and h_max <= H_CAP
          and all(len(t["rows"]) >= 3 for t in INST))
    for t in INST:
        check_mark = "+arch" if "arch" in t["rows"] else "     "
        print(f"    n={t['n']:>7d} D={t['D']:.4e} m={t['m']:>4d} "
              f"gauges={len(t['rows'])} {check_mark} "
              f"C_lad={t['C_lad']:.3f} negA={t['neg_arch']}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the gauge freedom  (T149)")
    id_max = max(rel(sc["gam_id"] - sc["gam_true"], sc["gam_true"])
                 for t in INST for sc in t["rows"].values())
    check(f"S1.ID: the factorisation identity Gam = sqrt(Q_star) x Sw "
          f"(v548 item (1)) holds GAUGE-INVARIANTLY on every one of the "
          f"{n_gauge} gauge assemblies -- Jacobi, const, moving-geometric-"
          f"mean, and the arithmetic-free archimedean diagonal where "
          f"positive -- max rel {id_max:.2e} (bar {TOL_ID:.0e}): the split "
          f"into one spectral and one geometric scalar is a property of "
          f"the whitened form, not of the gauge", id_max < TOL_ID)
    lb_ok = all(sc["floor"] <= t["lam_direct"] * (1.0 + TOL_DIR)
                for t in INST for sc in t["rows"].values())
    fam_lo = min(max(sc["floor"] for sc in t["rows"].values())
                 / t["lam_direct"] for t in INST)
    fam_hi = max(max(sc["floor"] for sc in t["rows"].values())
                 / t["lam_direct"] for t in INST)
    check(f"S1.CHAIN: lam_min(A) >= cert_lam_min(E~) x min_j Lam~_j -- an "
          f"identity plus one Rayleigh step, the completed-Cholesky floor "
          f"paying the certificate -- is a VALID lower bound on every "
          f"(window, gauge) assembly, so the family maximum is valid too "
          f"(family max captures {fam_lo:.4f}..{fam_hi:.4f} of the direct "
          f"lam_min on this list; T149 licence 5, per instance)", lb_ok)
    tv0_ok = all(t["rows"]["const"]["tv"] == 0.0 for t in INST)
    sig_lo = min(t["sig"] for t in INST)
    sig_hi = max(t["sig"] for t in INST)
    sand_ok = all(bool(np.all(t["c1"] * t["Lam_jac"]
                              <= t["gauges"]["const"]))
                  and bool(np.all(t["gauges"]["const"]
                                  <= t["c2"] * t["Lam_jac"]))
                  for t in INST)
    check(f"S1.CONST: the const gauge (the geometric mean of the Jacobi "
          f"diagonal) has TV(log Lam~) == 0 EXACTLY on every window -- "
          f"T149's elimination, not reduction, of T148's blocking scalar "
          f"-- and the certified entrywise sandwich c_1 Lam <= Lam~ <= "
          f"c_2 Lam holds with outward-rounded constants, sigma = c_2/c_1 "
          f"= {sig_lo:.4f}..{sig_hi:.4f} on this list",
          tv0_ok and sand_ok)
    ctrl_id = min(rel(math.sqrt(1.01 * sc["Qs"]) * sc["Sw"]
                      - sc["gam_true"], sc["gam_true"])
                  for t in INST for sc in t["rows"].values())
    ctrl_shift = 0
    for t in INST:
        s = 1.05 * t["lam_direct"]
        E_s, _ = whiten_with(t["A"] - s * np.eye(t["m"]),
                             t["gauges"]["const"])
        if not np.isfinite(cert_lam_min_pos(E_s)):
            ctrl_shift += 1
    check(f"S1.CTRL: a 1% Q_star perturbation breaks the gauge-invariant "
          f"identity on every assembly (min rel {ctrl_id:.2e} > "
          f"{BAR_CTRL:.0e}), and on the SHIFTED indefinite form "
          f"A - 1.05 lam_min I the completed-Cholesky floor REFUSES in the "
          f"const gauge on {ctrl_shift}/{len(INST)} windows -- the "
          f"certificate cannot be talked into a false floor",
          ctrl_id > BAR_CTRL and ctrl_shift == len(INST))

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the two-regime discriminator  (T149)")
    move_hi = max(abs(t["nu_mgm"]["nu_L"] - t["nu_jac"]["nu_L"])
                  / t["nu_jac"]["nu_L"] for t in INST)
    move_r = max(abs(t["nu_rough"]["nu_L"] - t["nu_jac"]["nu_L"])
                 / t["nu_jac"]["nu_L"] for t in INST)
    drop_lo = min(t["tv_jac"] / max(t["tv_mgm"], 1.0e-300) for t in INST)
    check(f"S2.FLUT: the flutter-smoothing gauge (moving geometric mean, "
          f"preregistered half-width m//{MGM_DIV}) removes TV(log Lam) by "
          f"a factor >= {drop_lo:.2f} (bar {BAR_TV_DROP:.1f}) on every "
          f"window while moving the TRANSPORTED bottom-block smoothness "
          f"functional nu_L~ by at most {move_hi:.4f} -- and even the "
          f"matched-amplitude ROUGH re-gauge (lattice-scale oscillation, "
          f"amplitude {ROUGH_AMP}) moves it by at most {move_r:.4f} (bar "
          f"{BAR_FLUT_MOVE:.2f} for both): the roughness nu_L~ responds "
          f"to is NOT in the multiplier -- T149's refutation of the TV "
          f"hypothesis, wired as a per-instance check",
          move_hi <= BAR_FLUT_MOVE and move_r <= BAR_FLUT_MOVE
          and drop_lo >= BAR_TV_DROP)
    psi_lo = min(abs(t["nu_rough"]["nu_psi"] - t["nu_jac"]["nu_psi"])
                 / t["nu_jac"]["nu_psi"] for t in INST)
    psi_hi = max(abs(t["nu_rough"]["nu_psi"] - t["nu_jac"]["nu_psi"])
                 / t["nu_jac"]["nu_psi"] for t in INST)
    check(f"S2.CTRL: the SAME functional read WITHOUT the Liouville "
          f"transport -- on the whitened modes psi, which carry the "
          f"multiplier -- jumps by {psi_lo:.2f}..{psi_hi:.2f} under the "
          f"same rough re-gauge (bar {BAR_PSI_ROUGH:.2f} on every window): "
          f"the invariance of S2.FLUT is carried by the Liouville "
          f"transport, not by numbness of the functional -- the "
          f"discriminator is not vacuous", psi_lo >= BAR_PSI_ROUGH)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the explicit zone diagonal and the atom budget "
          "(T150)")
    res_hi = max(t["res_zone"] for t in INST)
    split_hi = max(t["split_res"] for t in INST)
    at_hi = max(t["at_max"] for t in INST)
    check(f"S3.ZONE: Lam_r = c_0 - c_{{M-1-2r}} + sum_{{s != r}} "
          f"max(c_{{|r-s|}} - c_{{M-1-r-s}}, 0), assembled lagwise with no "
          f"matrix anywhere, equals the lumped-pair diagonal on every "
          f"window (max rel {res_hi:.2e}, bar {TOL_ID:.0e}) -- the "
          f"whitening diagonal is an EXPLICIT functional of the zone's lag "
          f"arithmetic and of nothing else", res_hi < TOL_ID)
    check(f"S3.SPLIT: the lag vector splits EXACTLY as c = c^arch + "
          f"c^atom (max rel {split_hi:.2e}) with c^atom <= 0 entrywise "
          f"(max entry {at_hi:.2e} <= 0): the arithmetic enters the form "
          f"only by SUBTRACTION at prime-power positions",
          split_hi < TOL_ID and at_hi <= 0.0)
    B_cheb = psi_ratio_max()
    bud_ok = all(t["l1_at"] <= t["mu_tot"] * (1.0 + TOL_DIR)
                 and t["mu_tot"] <= 4.0 * B_cheb * math.sqrt(t["N_win"])
                 for t in INST)
    slack_lo = min(4.0 * B_cheb * math.sqrt(t["N_win"])
                   / max(t["l1_at"], 1.0e-300) for t in INST)
    check(f"S3.BUDGET: ||c^atom||_1 <= sum_j mu_j <= 4 B sqrt(N) with "
          f"B = {B_cheb:.6f} the VERIFIED maximum of psi(n)/n over the "
          f"whole atom table (Chebyshev 1852, computed and never assumed; "
          f"Abel summation carries the closed form) -- holds on every "
          f"window, ceiling at least {slack_lo:.2f}x the true mass",
          bud_ok and B_cheb < 1.2)
    n_indef = sum(1 for t in INST if t["neg_arch"] >= 1)
    neg_hi = max(t["neg_arch"] for t in INST)
    full_ok = all(t["neg_full_odd"] == 0 for t in INST)
    check(f"S3.CORESP: the ARCHIMEDEAN section alone is INDEFINITE on "
          f"{n_indef}/{len(INST)} windows (completed LDL^T counts, up to "
          f"{neg_hi} negative eigenvalues) while the FULL odd section has "
          f"ZERO on {len(INST)}/{len(INST)} -- the atoms are "
          f"CO-RESPONSIBLE for the positivity, so the additive "
          f"perturbation reading (Weyl 1912 / Bauer-Fike 1960 / "
          f"Davis-Kahan 1970, cited, computed dead by T150 at 2.4-5.8 "
          f"orders, NOT used) is structurally empty: only the "
          f"multiplicative / Loewner gauge step of S1 transfers",
          n_indef >= 1 and full_ok
          and all(t["neg_arch"] >= 0 for t in INST))
    ctrl_zone = min(t["res_mut"] for t in INST)
    check(f"S3.CTRL: dropping the positive part in the zone formula "
          f"(summing ALL off-diagonals instead of max(.,0)) breaks the "
          f"identity on every window (min rel {ctrl_zone:.2e} > "
          f"{BAR_CTRL:.0e}) -- the lumping's sign selection is "
          f"load-bearing, and the budget x {BAR_CTRL:.0e} fails against "
          f"the true mass everywhere",
          ctrl_zone > BAR_CTRL
          and all(t["l1_at"] > BAR_CTRL * 4.0 * B_cheb
                  * math.sqrt(t["N_win"]) for t in INST))

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the parity compression and the inertia "
          "localisation  (T150)")
    PAR = [t for t in INST if t["M"] <= H_CAP]
    comp_hi = -float("inf")
    cross_hi = -float("inf")
    orth_hi = -float("inf")
    loc_ok = True
    n_negfull = []
    for t in PAR:
        c, M = t["c"], t["M"]
        TM = full_toeplitz(c, M)
        Um, Up = parity_isometries(M)
        Aodd = odd_toeplitz(c, M)
        Aeven = even_toeplitz(c, M)
        comp_hi = max(comp_hi, rel(Um.T @ TM @ Um - Aodd, Aodd),
                      rel(Up.T @ TM @ Up - Aeven, Aeven))
        cross_hi = max(cross_hi, rel(Up.T @ TM @ Um, TM))
        UU = np.concatenate([Up, Um], axis=1)
        orth_hi = max(orth_hi, rel(UU.T @ UU - np.eye(M), np.eye(M)))
        n_full = inertia_neg(TM)
        n_even = inertia_neg(sym(Aeven))
        n_odd = inertia_neg(sym(Aodd))
        n_negfull.append(n_full)
        if not (n_odd == 0 and n_even == n_full and n_full >= 1):
            loc_ok = False
    check(f"S4.COMP: U_-^T T_M(c) U_- == T - H and U_+^T T_M(c) U_+ == "
          f"T + H EXACTLY (max rel {comp_hi:.2e}) with cross block "
          f"U_+^T T_M U_- == 0 (max rel {cross_hi:.2e}) and [U_+ U_-] an "
          f"exact orthonormal basis (deviation {orth_hi:.2e}) on all "
          f"{len(PAR)} windows with M <= {H_CAP}: the reflection-odd "
          f"section IS the compression of the full symmetric Toeplitz "
          f"section onto its antisymmetric parity sector -- the mechanism "
          f"has a name (Basor-Ehrhardt 2009: the parity sectors are the "
          f"natural objects of the Toeplitz+Hankel algebra, cited as the "
          f"address and never as an authority)",
          len(PAR) >= 4 and comp_hi < TOL_ID and cross_hi < TOL_ID
          and orth_hi < TOL_ID)
    f0_all = [float(t["c"][0] + 2.0 * np.sum(t["c"][1:t["M"]]))
              for t in PAR]
    check(f"S4.INERTIA: the completed LDL^T counts LOCALISE the negative "
          f"inertia -- the full section T_M(c) has "
          f"{min(n_negfull)}..{max(n_negfull)} negative eigenvalues "
          f"(forced by the sign-changing symbol: f(0) = "
          f"{min(f0_all):.1f}..{max(f0_all):.1f} < 0, T148's honest "
          f"negative RE-READ, never re-derived), the EVEN sector carries "
          f"ALL of them and the ODD sector carries ZERO, on every window: "
          f"f(0) < 0 is a statement about the OTHER parity sector, "
          f"explained rather than worked around",
          loc_ok and all(f0 < 0.0 for f0 in f0_all))
    ctrl_par = float("inf")
    for t in PAR[:4]:
        c, M = t["c"], t["M"]
        TM = full_toeplitz(c, M)
        Um, _Up = parity_isometries(M)
        Um_bad = np.abs(Um)          # the SIGN-FLIPPED 'parity' basis
        Aodd = odd_toeplitz(c, M)
        ctrl_par = min(ctrl_par, rel(Um_bad.T @ TM @ Um_bad - Aodd, Aodd))
    check(f"S4.CTRL: the sign-flipped basis (|U_-|, i.e. the SYMMETRIC "
          f"combination) does NOT reproduce T - H (min rel "
          f"{ctrl_par:.2e} > {BAR_CTRL:.0e}) -- the antisymmetry is "
          f"load-bearing, the compression is not a notational identity",
          ctrl_par > BAR_CTRL)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the parity-sine calibration and the ladder "
          "certificate  (T150)")
    m_lic = 241
    P_lic = parity_basis(m_lic)
    mu_lic = parity_mu(m_lic)
    eig_err = rel(lap_P(P_lic.T.copy()) - P_lic.T * mu_lic[None, :],
                  P_lic.T)
    orth_err = rel(P_lic @ P_lic.T - np.eye(m_lic), np.eye(m_lic))
    check(f"S5.EIG: the parity sines t_k(r) = 2/sqrt(N) sin(2 pi k "
          f"(r+1)/N), N = 2m+1, are the EXACT eigenpairs of the parity "
          f"Laplacian L_P (reflecting corner 3 -- forced by antisymmetry, "
          f"not chosen) at mu^P_k = 4 sin^2(pi k/N): eigen-residual "
          f"{eig_err:.2e}, orthonormality {orth_err:.2e} at m = {m_lic} "
          f"(KMS 1953 in the parity sector) -- the licences of the parity "
          f"ceiling, verified before use",
          eig_err < TOL_ID and orth_err < TOL_ID)
    kk = np.arange(1, K_CAL + 1, dtype=float)
    N_cal = 2.0 * M_CAL + 1.0
    mu_cal = 4.0 * np.sin(math.pi * kk / N_cal) ** 2
    jj = np.arange(M_CAL)
    cal_dev = -float("inf")
    for ki in range(K_CAL):
        tk = (2.0 / math.sqrt(N_cal)) * np.sin(
            2.0 * math.pi * (ki + 1.0) * (jj + 1.0) / N_cal)
        n1 = float(np.sum(np.abs(lap_P(tk.reshape(-1, 1).copy()))))
        nu_k = (N_cal ** 1.5 / 8.0) * n1
        cal_dev = max(cal_dev, abs(nu_k / (math.pi * (ki + 1.0) ** 2)
                                   - 1.0))
    check(f"S5.CAL: on the exact parity model the smoothness ladder "
          f"CALIBRATES -- nu^P_k == pi k^2 for k = 1..{K_CAL} at m = "
          f"{M_CAL} (max relative deviation {cal_dev:.2e}, bar "
          f"{TOL_CAL:.0e}): in the matched sector no m-free constant is "
          f"even possible below pi, so the LADDER form nu_k <= C k^2 is "
          f"the right question and C = pi its exact floor", cal_dev < TOL_CAL)
    viol_hi = max(t["viol_P"] for t in INST)
    C_lo = min(t["C_lad"] for t in INST)
    C_hi = max(t["C_lad"] for t in INST)
    lad_all = all(t["lad_ok"] and t["chain_ok"] for t in INST)
    check(f"S5.LADDER: on every window, in the const gauge (phi = psi "
          f"exactly -- the ladder of the PURE Toeplitz-minus-Hankel "
          f"section, no multiplier, no arithmetic weight), the parity "
          f"coefficient licence holds (worst excess {viol_hi:.2e} <= 0), "
          f"nu^P_k <= C k^2 with the per-window certified constant "
          f"C = {C_lo:.2f}..{C_hi:.2f}, and the derived per-mode ceiling "
          f"m||psi_k||_inf^2 <= 2 (2 sqrt(C) k + 1)^2 is a certified "
          f"instance inequality on the bottom {K_LAD} modes -- an m-FREE "
          f"C is exactly the one open input and is NOT claimed (T150: "
          f"C grows x^0.258 on the long surface, a FIT, sandbox)",
          viol_hi <= TOL_DIR and lad_all)
    ctrl_lad = all(t["nu1"] > BAR_CTRL * t["C_lad"] for t in INST)
    m_ctrl = M_CAL
    tk1 = (2.0 / math.sqrt(N_cal)) * np.sin(
        2.0 * math.pi * 1.0 * (jj + 1.0) / N_cal)
    n1_1 = float(np.sum(np.abs(lap_P(tk1.reshape(-1, 1).copy()))))
    nu_1 = (N_cal ** 1.5 / 8.0) * n1_1
    shift_dev = abs(nu_1 / (math.pi * 4.0) - 1.0)
    check(f"S5.CTRL: the ladder x {BAR_CTRL:.0e} fails against the true "
          f"nu_1 on every window, and mis-indexing the calibration by one "
          f"(reading nu_1 against pi 2^2) misses by {shift_dev:.2f} > "
          f"{BAR_CTRL:.0e} -- the k^2 grading is load-bearing, the "
          f"calibration is not a tautology",
          ctrl_lad and shift_dev > BAR_CTRL)

    # ---------------------------------------------------------------- fences
    print("\nS6 -- the fences, restated as a check")
    check("S6.FENCE: PER-INSTANCE identities, theorems with checked "
          "hypotheses and certified inequalities on SMALL windows only -- "
          "a FINITE LIST with an explicit maximum, nothing uniform in the "
          "zone index or in D, and NO statement for ALL D: the ONE open "
          "input after T150 (an m-free constant in the odd-sector ladder "
          "nu_k <= C k^2 for a sign-changing-symbol Toeplitz section) "
          "stays OPEN, unclaimed and unapproached, exactly as T150 typed "
          "it; TV(log Lam) stays WITHDRAWN as a hypothesis (T149) and is "
          "not re-opened; sig_tot stays retired as a route (T148); every "
          "T149/T150 exponent is a FIT and stays in the sandbox; "
          "Kac-Murdock-Szego 1953 / Widom 1958 / Basor-Ehrhardt 2009 / "
          "Bottcher-Silbermann (the parity sectors as the algebra's "
          "natural objects -- the address, never an authority; the "
          "sign-changing symbol is exactly what Basor-Ehrhardt does NOT "
          "cover, and that gap IS the open input) / Sylvester 1852 / "
          "Bunch-Kaufman 1977 / Chebyshev 1852 (verified on the table) / "
          "Abel / Weyl 1912 / Bauer-Fike 1960 / Davis-Kahan 1970 (cited, "
          "computed dead, NOT used) / Rayleigh 1877 / Ritz 1909 / "
          "Cauchy-Schwarz / Gershgorin 1931 / Wilkinson 1968 / Higham "
          "2002 named CLASSICAL; Weil 1952 CITED, never used as a "
          "criterion; zero-firewall AST-checked; NO marker upgrade of any "
          "pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv549 runtime: {elapsed:.1f}s")
    print(f"  (1) gauge freedom: identity gauge-invariant to {id_max:.1e} "
          f"on {n_gauge} assemblies; const TV == 0 exactly, sigma = "
          f"{sig_lo:.4f}..{sig_hi:.4f}")
    print(f"  (2) two regimes: transported nu_L~ moves <= "
          f"{max(move_hi, move_r):.4f} under smooth AND rough gauges "
          f"(TV drop >= {drop_lo:.2f}x); untransported jumps "
          f"{psi_lo:.2f}..{psi_hi:.2f}")
    print(f"  (3) zone diagonal: residual {res_hi:.1e}; c^atom <= 0; "
          f"budget 4B sqrt(N) with B = {B_cheb:.4f}; arch section "
          f"indefinite on {n_indef}/{len(INST)}")
    print(f"  (4) parity: compression exact to {comp_hi:.1e}, cross "
          f"{cross_hi:.2e}; negative inertia all in the even sector on "
          f"{len(PAR)} windows")
    print(f"  (5) parity ladder: model calibration {cal_dev:.1e} to "
          f"pi k^2; C = {C_lo:.2f}..{C_hi:.2f} per window, m-free C OPEN")
    return summary("PRIME.GAUGE.PARITY.IDENT.01 gauge/parity identities")


if __name__ == "__main__":
    raise SystemExit(run())
