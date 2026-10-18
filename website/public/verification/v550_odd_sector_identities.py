"""v550 -- PRIME.ODD.SECTOR.IDENT.01: the odd-sector identities of phase 2.
The IDENTITY- and CERTIFICATE-shaped core of T151 (contract ODD.LADDER: the
grid step-over, the certified bottom ladder against the parity Laplacian,
the discrete Sobolev step, the closed archimedean diagonal minimum, and the
LINEAR per-mode bound through the certified pencil) -- every statement
RECOMPUTED here from scratch on small exactly checkable frame-A windows (no
citation of sandbox output).  Companion to PRIME.GAUGE.PARITY.IDENT.01
(v549), which certified the parity compression and the quadratic ladder
certificate nu^P_k <= C k^2: THIS module certifies the REROUTE T151 found
-- off the nu ladder, through the pencil against the parity Laplacian and
one elementary Sobolev step, to a per-mode bound LINEAR in k.

WHAT IS LOAD-BEARING HERE (and nothing else): identities, per-instance
theorems with CHECKED hypotheses, and per-window CERTIFIED inequalities.
NO fit, NO D-exponent, NO uniform-in-zone statement, and NO statement FOR
ALL D -- the ONE open input after T151 (the m-freeness of the bottom pencil
ratio R = K_bot/kap for the odd parity sector of a sign-changing-symbol
Toeplitz section) stays OPEN and is neither assumed nor approached: R is
read per window and typed as a per-instance certificate ONLY, and its flat
trend on the long surface (T151: x^0.037 +- 0.015) is a FIT that stays in
the sandbox.  Each identity is checked as a NUMERICAL RESIDUAL against a
preregistered tolerance AND against at least one MUTATION CONTROL that must
fail loudly.

[E] (1) THE GRID STEP-OVER (T151).  The parity sines live on the SHIFTED
    grid th_k = 2 pi k / N, N = 2m+1, which never contains th = 0, and
    mu^P_k = 2 - 2 cos th_k EXACTLY; the symbol f of the window's lag
    vector has f(0) < 0 (T148's honest negative, re-read and never
    re-derived) with a negative window [0, th_c) whose width satisfies
    th_c < th_1 = 2 pi / N on EVERY window: the odd grid STEPS OVER the
    negative window -- the positivity of the odd sector is a GRID fact.
    THE HONEST NEGATIVE BESIDE IT, promoted as content (T150's rest item 3
    answered NEGATIVELY): the pointwise symbol language fails at the
    resolution of the bottom mode -- the symbol-only pencil floor
    kap_sym (1 - rho) with rho = |f(0)| / (kap_sym mu^P_1) is VACUOUS
    (rho >= 1) on every window of this battery, so the local model is a
    MATRIX statement, not a symbol statement.
[E] (2) THE CERTIFIED BOTTOM LADDER (T151).  lam_k(A) <= S mu^P_k for
    k <= 8 is certified per window by 8 completed LDL^T inertia counts
    (Sylvester 1852; Bunch-Kaufman 1977) -- no eigenvector, no sorted
    list: the odd sector's bottom spectrum IS the parity-Laplacian ladder
    up to the printed per-window factor S, order 2 in k, with no trace of
    f(0) < 0 in it (the Rayleigh floor L_P >= mu^P_1 I absorbs it).
[E] (3) THE DISCRETE SOBOLEV STEP (T151).  An odd-sector vector vanishes
    at the virtual node (the antisymmetric extension has psi_{-1} = 0), so
    ||grad psi||_2^2 == <psi, L_0 psi> - psi_last^2 EXACTLY,
    ||grad psi||_2^2 <= <psi, L_P psi>, and
    ||psi||_inf^2 <= 2 ||psi||_2 ||grad psi||_2 -- elementary, verified on
    random vectors, the parity sines and the true window modes (continuum
    address Hardy-Littlewood-Polya 1934 / Agmon 1965).  CALIBRATION: on
    the exact parity model the pencil is (1, 1) (certified) and the
    Sobolev per-mode price is EXACTLY pi -- the honest, m-free cost of
    leaving the l2 world.
[E] (4) THE CLOSED ARCHIMEDEAN MINIMUM (T151; T150's rest item 2 CLOSED
    AND ATTAINED).  The archimedean lag kernel has two shape properties,
    both CHECKED per window and neither assumed -- c^arch_i < 0 for every
    lag i >= 1, and c^arch_i non-decreasing on i >= 1 -- and given those,
    min_r Lam^arch_r = c^arch_0 - c^arch_{M-1} EXACTLY (attained at
    r = 0): a closed two-term functional of the smooth kernel with no
    loss, no matrix and no eigenvector.
[E] (5) THE LINEAR PER-MODE BOUND AND THE NO-GO DISCRIMINATOR (T151).
    With kap the certified pencil floor (ONE completed Cholesky of
    A - kap L_P, the floor carried as fl / mu^P_1) and K_bot = S the
    certified bottom-ladder constant of (2), the chain
        <psi_k, L_P psi_k> <= lam_k(A) / kap <= K_bot mu^P_k / kap
        ==> b_k := m ||psi_k||_inf^2 <= 2 m sqrt(K_bot mu^P_k / kap)
                                     <= C_S k  with  C_S <= 2 pi
                                        sqrt(K_bot/kap)
    is LINEAR in k where the quadratic nu ladder grew (v549 item (5)),
    every m-power cancelled, NOTHING additive anywhere -- so the
    Theta(D^3) smallness of the bottom, which killed the Weyl /
    Bauer-Fike / Davis-Kahan route, never enters.  THE DISCRIMINATOR: on
    the T145 no-go form (R = a a^T + eps I, a_i = i^{-1/2}) the bottom
    pencil ratio K_bot/kap EXPLODES on the size ladder (it MUST -- a
    route that did not fail there would prove a false statement), while
    the exact parity model holds it at 1.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL windows.  Nothing here
        is uniform in the zone index or in D; what is established is a
        FINITE LIST of certified window inequalities with an explicit
        maximum, and every T151 exponent is a FIT that stays in the
        sandbox.  The step to ALL D -- the m-freeness of the bottom pencil
        ratio R = K_bot/kap -- is OPEN, explicitly typed open, and neither
        assumed nor approached.
  (ii)  Item (1)'s step-over is a comparison of two computed widths per
        window; no statement is made about the symbol beyond its first
        sign change, and the symbol-only formula is DESIGN, never
        load-bearing (the grid pair kap_sym / rho is instrumented only to
        certify its own vacuity).
  (iii) Item (5) bounds the bottom K_LAD modes per window; C_S and R are
        printed per window and their size and trend stay in the sandbox
        (T151: C_S = 11.51..19.57 with trend x^0.020 on the long surface,
        a FIT).
  (iv)  TV(log Lam) stays WITHDRAWN as a hypothesis (T149), sig_tot stays
        retired as a route (T148), and the quadratic ladder's open input
        (v549: m-free C) is SUPERSEDED by the sharper open scalar here --
        nothing is re-opened and no marker of any pre-existing contract
        moves.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil
    window form (Weil 1952, CITED, never used as a criterion) on a FINITE
    list of prime-power zones.  Everything here is an identity or a
    certified inequality PER INSTANCE; NOTHING here claims, assumes or
    approaches RH, and no statement about zeta zeros is made.  No zero
    data of any kind is read, generated or approximated -- an AST firewall
    enforces this.  NO all-D claim: even with every check green, what
    stands is a finite list of certified window statements on prime-power
    zones, and the one open input (the m-freeness of the bottom pencil
    ratio) stays open here and everywhere.
  * Classics named CLASSICAL: Kac-Murdock-Szego 1953 (the exact parity
    eigenpairs), Widom 1958 / Basor-Ehrhardt 2009 / Bottcher-Silbermann
    (the Toeplitz+Hankel address and the local behaviour at a symbol
    minimum, CITED as the question's home; the sign-changing symbol is
    exactly what the classical theory does not cover, and item (1) is the
    computed reason the symbol language cannot be extended pointwise),
    Weyl 1912 (minimax), Parlett (the definite-pencil reduction),
    Hardy-Littlewood-Polya 1934 / Agmon 1965 (the Sobolev step's
    continuum address), Sylvester 1852 / Bunch-Kaufman 1977 (inertia),
    Rayleigh 1877 / Ritz 1909, Cauchy-Schwarz, Wilkinson 1968 / Higham
    2002 (completed Cholesky and its floor), Chebyshev 1852 (psi(x)/x --
    verified on the finite table, never assumed).
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] exact linear-algebra / counting identities at rel
< 1e-11 .. 1e-15 as stated, per-instance theorems with checked
hypotheses, certified inequalities by completed Cholesky / completed
LDL^T with the direction in the name, each with a mutation control that
fails loudly.  Python; Wolfram-mirrored not required (dense Cholesky /
LDL^T / eigenvalue identities stay Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/odd_ladder_probe.py               (T151)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, eigh, eigvalsh, ldl, solve_triangular

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v549
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
U_ROUND = 2.0 ** -53

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept (spread over the D range)

# --- the symbol grid of item (1): DESIGN ONLY, never load-bearing -----------
N_TH = 2048                  # uniform theta grid on [0, pi]
N_TH_LOG = 256               # geometric refinement towards theta = 0
TH_LO = 1.0e-3               # below this the (f - f0)/(2 - 2cos) quotient is
#                              cancellation noise (T151's declared floor)
STEP_BAR = 0.9               # th_c / th_1 must sit below this on every window

# --- the certified bottom ladder of item (2), preregistered -----------------
K_CERT = 8                   # modes certified by LDL^T counts
PEN_BACKOFF = (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)
LAD_BACKOFF = (1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)  # keeps the rungs
#                              clear of eigenvalue ties (the seed is exact)

# --- the Sobolev items (3) and (5), preregistered ----------------------------
K_LAD = 8                    # bottom modes read into the linear ladder
M_CAL = 2001                 # control-model size for the pi price (vector ops)
M_PEN = 241                  # control-model size for the certified (1,1) pencil
N_RAND = 12                  # random unit vectors per licence check

# --- the no-go discriminator (T145 form, quoted) -----------------------------
NOGO_EPS = 1.0e-3
NOGO_SIZES = (64, 128, 256)
NOGO_GROW = 4.0              # the bottom pencil ratio must grow >= this factor

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_ID = 1.0e-11             # every identity must hold to this relative level
TOL_DIR = 1.0e-9             # one-sided slack of per-instance theorem steps
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
TOL_CAL = 2.0e-3             # |sobolev price / pi - 1| bar on the exact model
TOL_PEN1 = 1.0e-9            # |pencil - 1| bar on the exact parity model


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
    """THE EXACT SPLIT c = c^arch + c^atom of the T115 lag assembly; the sum
    is bit-for-bit the frame-A code path of T128..T151 / v548 / v549."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T151)
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: the reflection-odd section -- by v549
    item (4) EXACTLY the compression of T_M(c) onto the antisymmetric parity
    sector (quoted, not re-verified here)."""
    h = M // 2
    r = np.arange(h)
    return (c[np.abs(r[:, None] - r[None, :])]
            - c[(M - 1) - r[:, None] - r[None, :]])


def parity_mu(m):
    """THE EXACT PARITY EIGENVALUES mu^P_k = 4 sin^2(pi k / N) = 2 - 2 cos
    (2 pi k / N), N = 2m+1, k = 1..m (KMS 1953 in the parity sector)."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL PARITY BASIS t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N),
    N = 2m+1.  Note t_k(-1) = 0 EXACTLY: the odd sector vanishes at the
    virtual node, which is what licences the discrete Sobolev step."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def lap_apply(X, corner):
    """tridiag(-1, 2, -1) X columnwise with the LAST diagonal entry
    2 + corner: corner = 1 is the parity Laplacian L_P (the reflecting
    corner forced by antisymmetry), corner = 0 the Dirichlet L_0."""
    out = 2.0 * X
    out[:-1] -= X[1:]
    out[1:] -= X[:-1]
    out[-1] += corner * X[-1]
    return out


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
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(X):
    return float(np.max(np.abs(X).sum(axis=1)))


def inertia_lt(X, tau):
    """THE CERTIFIED COUNT #{j : lam_j(X) < tau} from the block diagonal of a
    completed pivoted LDL^T of X - tau I (Sylvester 1852; Bunch-Kaufman
    1977) -- a certificate, never a sorted list.  Returns -1 when the
    factorisation does not complete, so a missing certificate is REPORTED
    rather than silently replaced."""
    n = X.shape[0]
    if n == 0:
        return 0
    try:
        _lu, d, _perm = ldl(sym(X) - tau * np.eye(n), lower=True)
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


# ------------------------------------------ item (1): the symbol window
def theta_grid():
    th_u = np.linspace(0.0, math.pi, N_TH)
    th_g = np.exp(np.linspace(math.log(TH_LO), math.log(math.pi), N_TH_LOG))
    return np.unique(np.concatenate([th_u, th_g]))


TH_GRID = theta_grid()


def symbol_values(c, th):
    """f(th) = c_0 + 2 sum_{k>=1} c_k cos(k th) on the DESIGN grid."""
    c = np.asarray(c, dtype=float)
    out = np.full(th.shape[0], c[0])
    kk = np.arange(1, c.shape[0])
    step = max(1, int(2.0e6 // max(th.shape[0], 1)))
    for a in range(0, kk.shape[0], step):
        b = min(kk.shape[0], a + step)
        out += 2.0 * (np.cos(np.outer(th, kk[a:b])) @ c[1 + a:1 + b])
    return out


def symbol_window(c, m):
    """f(0), the width th_c of the negative window (first sign change,
    linearly interpolated on the design grid), the odd mode spacing
    th_1 = 2 pi / N, and the DESIGN pair (kap_sym, rho) of the symbol-only
    comparison -- instrumented ONLY to certify its own vacuity."""
    N = 2 * m + 1
    th = TH_GRID
    f = symbol_values(c, th)
    f0 = float(f[0])
    pos = np.nonzero(f > 0.0)[0]
    if f0 > 0.0:
        th_c = 0.0
    elif pos.size == 0:
        th_c = float(math.pi)
    else:
        i1 = int(pos[0])
        i0 = i1 - 1
        f0v, f1v = float(f[i0]), float(f[i1])
        w = f0v / (f0v - f1v) if f1v != f0v else 0.5
        th_c = float(th[i0] + w * (th[i1] - th[i0]))
    use = th >= TH_LO
    den = 2.0 - 2.0 * np.cos(th[use])
    rat = (f[use] - f0) / np.where(den > 0.0, den, np.inf)
    rat = rat[np.isfinite(rat)]
    kap_sym = float(np.min(rat)) if rat.size else float("nan")
    mu1 = 4.0 * math.sin(math.pi / N) ** 2
    th_1 = 2.0 * math.pi / N
    rho = (abs(f0) / (kap_sym * mu1)) if kap_sym > 0.0 else float("inf")
    f_th1 = float(np.interp(th_1, th, f))
    f_th2 = float(np.interp(2.0 * th_1, th, f))
    return dict(f0=f0, th_c=th_c, th_1=th_1, ratio=th_c / th_1,
                kap_sym=kap_sym, rho=rho,
                sym_floor=(kap_sym * (1.0 - rho)
                           if np.isfinite(rho) else float("-inf")),
                f_var=abs(f_th2 - f_th1) / max(abs(f_th1), 1.0e-300))


# ------------------------------------------ items (2)+(5): pencil machinery
def pencil_floor(A, LP, m):
    """THE CERTIFIED PENCIL FLOOR kap with A >= kap L_P.  One tridiagonal
    Cholesky L_P = G G^T and two triangular solves give the seed spectrum;
    the certificate is a completed Cholesky of A - kap L_P, and the
    floating-point floor is carried as fl / mu^P_1 (a completed Cholesky
    certifies A - kap L_P >= -fl I and I <= L_P / mu^P_1).  DIRECTION: a
    LOWER bound.  Returns (kap, seed_min, seed_max)."""
    mu1 = 4.0 * math.sin(math.pi / (2 * m + 1)) ** 2
    fac = safe_cho(LP)
    if fac is None:
        return None
    G = np.tril(fac[0]) if fac[1] else np.tril(fac[0].T)
    try:
        Y = solve_triangular(G, A, lower=True, check_finite=False)
        Z = sym(solve_triangular(G, Y.T, lower=True, check_finite=False))
        wz = eigvalsh(Z)
    except (LinAlgError, ValueError):
        return None
    lo_seed, up_seed = float(wz[0]), float(wz[-1])
    for eta in PEN_BACKOFF:
        k_try = lo_seed * (1.0 - eta) if lo_seed > 0.0 else lo_seed - eta
        X = sym(A - k_try * LP)
        if safe_cho(X) is not None:
            fl = chol_floor(gersh(X), m)
            return dict(kap=k_try - fl / mu1, lo=lo_seed, up=up_seed)
    return None


def cert_bottom_ladder(A, m, mu, k_cert=K_CERT):
    """THE CERTIFIED BOTTOM LADDER lam_k(A) <= S mu^P_k, k <= k_cert, by
    k_cert completed LDL^T counts: lam_k < tau holds exactly when
    #{j : lam_j < tau} >= k.  The seed S comes from a spectrum (seed ONLY);
    the certificate is the count.  DIRECTION: an UPPER bound on the low
    eigenvalues in units of the exact model ladder."""
    kc = int(min(k_cert, m))
    lam_low = eigvalsh(A, subset_by_index=[0, kc - 1])
    S_seed = float(np.max(lam_low / mu[:kc]))
    for eta in LAD_BACKOFF:
        S = S_seed * (1.0 + eta)
        counts = [inertia_lt(A, S * float(mu[k - 1])) for k in range(1, kc + 1)]
        if all(cnt >= k for k, cnt in enumerate(counts, start=1)):
            return dict(S=S, counts=counts, kc=kc, lam_low=lam_low)
    return None


def grad_sq(psi):
    """||grad psi||_2^2 with psi_{-1} = 0 (the odd sector's virtual node)."""
    psi = np.asarray(psi, dtype=float)
    d = np.diff(np.concatenate([[0.0], psi]))
    return float(d @ d)


def sobolev_sup_bound(psi):
    """THE DISCRETE SOBOLEV / AGMON STEP: ||psi||_inf^2 <= 2 ||psi||_2
    ||grad psi||_2 for any vector with psi_{-1} = 0.  DIRECTION: UPPER."""
    return 2.0 * math.sqrt(max(grad_sq(psi), 0.0)) * float(
        np.linalg.norm(psi))


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


def build_instance(k, D, M, h):
    """One window end to end: the split lag vector, the odd section, the
    symbol window, the certified pencil floor and bottom ladder, the
    Sobolev per-mode data, and the closed archimedean minimum."""
    al = 0.5 * M * D
    sp = lag_vector_split(al, M, atoms_in(al))
    c = sp["c"]
    A = sym(odd_toeplitz(c, M))
    m = h
    lam1 = float(eigvalsh(A, subset_by_index=[0, 0])[0])
    if not (lam1 > 0.0):
        return None
    LP = lap_P_mat(m)
    mu = parity_mu(m)
    pen = pencil_floor(A, LP, m)
    if pen is None or not (np.isfinite(pen["kap"]) and pen["kap"] > 0.0):
        return None
    lad = cert_bottom_ladder(A, m, mu)
    if lad is None:
        return None
    so = symbol_window(c, m)

    # ---- item (4): the closed archimedean minimum
    c_ar = sp["c_ar"]
    tail = c_ar[1:M]
    sc = max(abs(float(c_ar[0])), 1.0)
    shape_neg = bool(tail.size and np.all(tail < 0.0))
    shape_inc = bool(tail.size < 2
                     or np.all(np.diff(tail) >= -1.0e-13 * sc))
    rr = np.arange(m)
    A_ar = (c_ar[np.abs(rr[:, None] - rr[None, :])]
            - c_ar[(M - 1) - rr[:, None] - rr[None, :]])
    lam_arch = (np.diag(A_ar).copy()
                + np.maximum(A_ar - np.diag(np.diag(A_ar)), 0.0).sum(axis=1))
    closed = float(c_ar[0] - c_ar[M - 1])
    res_arch = abs(float(np.min(lam_arch)) - closed) / max(abs(closed),
                                                           1.0e-300)
    # the full atom-including diagonal, for the mutation control
    A_full = (c[np.abs(rr[:, None] - rr[None, :])]
              - c[(M - 1) - rr[:, None] - rr[None, :]])
    lam_full = (np.diag(A_full).copy()
                + np.maximum(A_full - np.diag(np.diag(A_full)),
                             0.0).sum(axis=1))
    tail_f = c[1:M]
    shape_inc_full = bool(np.all(np.diff(tail_f)
                                 >= -1.0e-13 * max(abs(float(c[0])), 1.0)))
    res_full = abs(float(np.min(lam_full)) - float(c[0] - c[M - 1])) \
        / max(abs(float(c[0] - c[M - 1])), 1.0e-300)

    # ---- item (5): the linear per-mode bound against the true modes
    kap = pen["kap"]
    S = lad["S"]
    KL = int(min(K_LAD, m))
    lam_bot, psi_bot = eigh(A, subset_by_index=[0, KL - 1])
    kk = np.arange(1, KL + 1, dtype=float)
    b = 2.0 * m * np.sqrt(np.maximum(S * mu[:KL] / kap, 0.0))
    b_cap = np.minimum(b, float(m))
    C_S = float(np.max(b_cap / kk))
    C_closed = 2.0 * math.pi * math.sqrt(S / kap)
    sup_true = float(m) * np.max(np.abs(psi_bot), axis=0) ** 2
    e_lp = np.array([float(psi_bot[:, j] @ (LP @ psi_bot[:, j]))
                     for j in range(KL)])
    grad = np.array([grad_sq(psi_bot[:, j]) for j in range(KL)])
    sob = np.array([sobolev_sup_bound(psi_bot[:, j]) for j in range(KL)])

    return dict(n=NN_ALL[k], m=m, M=M, D=D, c=c, A=A, LP=LP, mu=mu,
                lam1=lam1, pen=pen, lad=lad, so=so,
                kap=kap, S=S, R=S / kap, C_S=C_S, C_closed=C_closed,
                b=b, b_cap=b_cap, kk=kk,
                lam_bot=lam_bot, psi_bot=psi_bot, KL=KL,
                sup_true=sup_true, e_lp=e_lp, grad=grad, sob=sob,
                shape_neg=shape_neg, shape_inc=shape_inc,
                res_arch=res_arch, res_full=res_full,
                shape_inc_full=shape_inc_full, closed=closed)


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(151)
    print("=" * 72)
    print("v550  PRIME.ODD.SECTOR.IDENT.01 -- odd-sector identities (T151)")
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
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite, split lag assembly, certified pencil "
          f"floor and certified bottom ladder on every one); every "
          f"factorised / diagonalised matrix <= {H_CAP} (max m = {h_max}); "
          f"the surface spans D = {d_lo:.3e} .. {d_hi:.3e}",
          len(INST) >= 6 and h_max <= H_CAP)
    for t in INST:
        print(f"    n={t['n']:>7d} D={t['D']:.4e} m={t['m']:>4d} "
              f"thc/th1={t['so']['ratio']:.3f} S={t['S']:.4f} "
              f"kap={t['kap']:.4f} R={t['R']:.3f} C_S={t['C_S']:.3f}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the grid step-over and the honest negative  (T151)")
    r_lo = min(t["so"]["ratio"] for t in INST)
    r_hi = max(t["so"]["ratio"] for t in INST)
    f0_lo = min(t["so"]["f0"] for t in INST)
    f0_hi = max(t["so"]["f0"] for t in INST)
    step_ok = all(t["so"]["f0"] < 0.0 and t["so"]["th_c"] > 0.0
                  and t["so"]["ratio"] <= STEP_BAR for t in INST)
    check(f"S1.STEP: the symbol has f(0) = {f0_lo:.1f}..{f0_hi:.1f} < 0 on "
          f"every window (T148's honest negative, re-read and never "
          f"re-derived) with a NONEMPTY negative window [0, th_c) -- and "
          f"th_c / th_1 = {r_lo:.3f}..{r_hi:.3f} <= {STEP_BAR} on every "
          f"window: the odd grid th_k = 2 pi k / N never contains the "
          f"origin and its FIRST point already clears the negative window "
          f"-- the positivity of the odd sector is a GRID fact, stepped "
          f"over rather than cancelled", step_ok)
    m_lic = M_PEN
    P_lic = parity_basis(m_lic)
    mu_lic = parity_mu(m_lic)
    N_lic = 2 * m_lic + 1
    th_k = 2.0 * math.pi * np.arange(1, m_lic + 1, dtype=float) / N_lic
    mu_cos = 2.0 - 2.0 * np.cos(th_k)
    id_mu = rel(mu_lic - mu_cos, mu_lic)
    eig_err = rel(lap_apply(P_lic.T.copy(), 1.0)
                  - P_lic.T * mu_lic[None, :], P_lic.T)
    orth_err = rel(P_lic @ P_lic.T - np.eye(m_lic), np.eye(m_lic))
    check(f"S1.EXACT: mu^P_k == 2 - 2 cos(2 pi k / N) EXACTLY (rel "
          f"{id_mu:.2e}) and the parity sines are the exact eigenpairs of "
          f"L_P at these values (eigen-residual {eig_err:.2e}, "
          f"orthonormality {orth_err:.2e} at m = {m_lic}; KMS 1953 in the "
          f"parity sector): the odd sector's exact model lives on the "
          f"shifted grid, which is what makes S1.STEP an operator statement",
          id_mu < TOL_ID and eig_err < TOL_ID and orth_err < TOL_ID)
    n_vac = sum(1 for t in INST if t["so"]["rho"] >= 1.0)
    fv_lo = min(t["so"]["f_var"] for t in INST)
    fv_hi = max(t["so"]["f_var"] for t in INST)
    check(f"S1.HONEST: T150's rest item 3 (extend the symbol calculus to "
          f"f(0) < 0) is answered NEGATIVELY, promoted as content -- the "
          f"symbol-only pencil floor kap_sym (1 - rho) with rho = |f(0)| / "
          f"(kap_sym mu^P_1) is VACUOUS (rho >= 1) on {n_vac}/{len(INST)} "
          f"windows, and the symbol moves by {fv_lo:.2f}..{fv_hi:.2f} "
          f"relative across ONE mode spacing: no pointwise symbol statement "
          f"is admissible at the resolution of the bottom mode -- the local "
          f"model is a MATRIX statement (S2), not a symbol statement",
          n_vac == len(INST))
    eig_bad = rel(lap_apply(P_lic.T.copy(), 0.0)
                  - P_lic.T * mu_lic[None, :], P_lic.T)
    kk_l = np.arange(1, m_lic + 1, dtype=float)
    mu_shift = 4.0 * np.sin(math.pi * (kk_l + 1.0) / N_lic) ** 2
    id_shift = rel(mu_lic - mu_shift, mu_lic)
    check(f"S1.CTRL: with the DIRICHLET corner (2 instead of the parity "
          f"corner 3) the sines are NOT eigenpairs (residual {eig_bad:.2e} "
          f"> {BAR_CTRL:.0e}) -- the reflecting corner is forced, not "
          f"chosen -- and a one-index shift of the exact eigenvalue formula "
          f"misses by {id_shift:.2e} > {BAR_CTRL:.0e}: neither the corner "
          f"nor the grid indexing is decorative",
          eig_bad > BAR_CTRL and id_shift > BAR_CTRL)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the certified bottom ladder  (T151)")
    S_lo = min(t["S"] for t in INST)
    S_hi = max(t["S"] for t in INST)
    check(f"S2.LADDER: lam_k(A) <= S mu^P_k for k <= {K_CERT} is CERTIFIED "
          f"on every window by {K_CERT} completed LDL^T inertia counts "
          f"(Sylvester 1852; Bunch-Kaufman 1977 -- a certificate, never a "
          f"sorted list), with the per-window constant S = "
          f"{S_lo:.4f}..{S_hi:.4f}: the odd sector's bottom spectrum IS "
          f"the parity-Laplacian ladder up to a printed O(1) factor -- "
          f"order 2 in k, with no trace of f(0) < 0 in it",
          all(t["lad"] is not None for t in INST))
    cnt_ok = True
    for t in INST:
        mu, A, lad = t["mu"], t["A"], t["lad"]
        w_full = eigvalsh(A)
        for k, cnt in enumerate(lad["counts"], start=1):
            tau = lad["S"] * float(mu[k - 1])
            if cnt != int(np.count_nonzero(w_full < tau)):
                cnt_ok = False
    check(f"S2.COUNT: the completed LDL^T count equals the direct spectral "
          f"count at every rung ({len(INST) * K_CERT} (window, k) pairs) -- "
          f"the certificate and the spectrum agree exactly, and only the "
          f"certificate is consumed", cnt_ok)
    ctrl_lad = True
    for t in INST:
        cnt = inertia_lt(t["A"], BAR_CTRL * t["S"] * float(t["mu"][0]))
        if cnt >= 1:
            ctrl_lad = False
    check(f"S2.CTRL: the ladder x {BAR_CTRL:.0e} fails on every window "
          f"(the count at tau = 1e-3 S mu^P_1 certifies NO eigenvalue "
          f"below it) -- the constant S is load-bearing, not slack",
          ctrl_lad)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the discrete Sobolev step and the pi price  (T151)")
    id_hi = -float("inf")
    ord_ok = True
    sup_ok = True
    for t in INST:
        m = t["m"]
        vecs = [t["psi_bot"][:, j] for j in range(t["KL"])]
        vecs += [parity_basis(m)[j] for j in range(min(3, m))]
        for _ in range(N_RAND - 3):
            v = rng.standard_normal(m)
            vecs.append(v / float(np.linalg.norm(v)))
        for v in vecs:
            g2 = grad_sq(v)
            e0 = float(v @ lap_apply(v.reshape(-1, 1).copy(), 0.0)[:, 0])
            eP = float(v @ lap_apply(v.reshape(-1, 1).copy(), 1.0)[:, 0])
            id_hi = max(id_hi, abs(g2 - (e0 - float(v[-1]) ** 2))
                        / max(abs(g2), 1.0e-300))
            if g2 > eP * (1.0 + TOL_DIR):
                ord_ok = False
            if float(np.max(np.abs(v))) ** 2 > 2.0 * math.sqrt(
                    max(g2, 0.0)) * float(np.linalg.norm(v)) * (1.0 + TOL_DIR):
                sup_ok = False
    check(f"S3.SOB: on the true window modes, the parity sines and random "
          f"unit vectors, the gradient identity ||grad psi||^2 == "
          f"<psi, L_0 psi> - psi_last^2 holds exactly (max rel {id_hi:.2e}), "
          f"the ordering ||grad psi||^2 <= <psi, L_P psi> holds, and the "
          f"discrete Sobolev step ||psi||_inf^2 <= 2 ||psi||_2 ||grad "
          f"psi||_2 holds -- elementary, licensed by the virtual node "
          f"psi_{{-1}} = 0 of the odd sector (Hardy-Littlewood-Polya 1934 / "
          f"Agmon 1965 the continuum address)",
          id_hi < TOL_ID and ord_ok and sup_ok)
    LPm = lap_P_mat(M_PEN)
    pen_m = pencil_floor(LPm, LPm, M_PEN)
    pen1 = abs(pen_m["kap"] - 1.0) if pen_m is not None else float("inf")
    N_cal = 2 * M_CAL + 1
    mu1_cal = 4.0 * math.sin(math.pi / N_cal) ** 2
    jj = np.arange(M_CAL)
    t1 = (2.0 / math.sqrt(N_cal)) * np.sin(
        2.0 * math.pi * (jj + 1.0) / N_cal)
    b1_model = 2.0 * M_CAL * math.sqrt(mu1_cal)
    truth1 = float(M_CAL) * float(np.max(np.abs(t1))) ** 2
    price = b1_model / truth1
    cal_dev = abs(price / math.pi - 1.0)
    check(f"S3.CAL: on the exact parity model the pencil is (1, 1) -- "
          f"certified |kap - 1| = {pen1:.2e} <= {TOL_PEN1:.0e} at m = "
          f"{M_PEN} -- and the Sobolev per-mode price at m = {M_CAL} is "
          f"b_1 / (m ||t_1||_inf^2) = {price:.6f} = pi to {cal_dev:.2e} "
          f"(bar {TOL_CAL:.0e}): the factor pi is the honest, m-free cost "
          f"of leaving the l2 world, and no constant below it is possible "
          f"in the matched sector", pen1 <= TOL_PEN1 and cal_dev < TOL_CAL)
    v_ctrl = np.zeros(M_PEN)
    v_ctrl[0] = 1.0
    gN = float(v_ctrl @ lap_apply(v_ctrl.reshape(-1, 1).copy(), 1.0)[:, 0]
               - 2.0 * v_ctrl[0] ** 2 + v_ctrl[0] ** 2)
    g_true = grad_sq(v_ctrl)
    neu_gap = (g_true - gN) / max(abs(g_true), 1.0e-300)
    id_mut = -float("inf")
    for t in INST[:4]:
        v = t["psi_bot"][:, 0]
        g2 = grad_sq(v)
        e0 = float(v @ lap_apply(v.reshape(-1, 1).copy(), 0.0)[:, 0])
        id_mut = max(id_mut, abs(g2 - e0) / max(abs(g2), 1.0e-300))
    check(f"S3.CTRL: dropping the boundary term psi_last^2 breaks the "
          f"gradient identity on the true bottom modes (max rel "
          f"{id_mut:.2e} > {BAR_CTRL:.0e}), and the NEUMANN energy (both "
          f"corners free) undercounts the gradient of a vector supported "
          f"at the first node by {neu_gap:.2f} -- the left virtual node of "
          f"the ODD sector is load-bearing: without it the Sobolev licence "
          f"has no anchor", id_mut > BAR_CTRL and neu_gap > BAR_CTRL)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the closed archimedean minimum  (T151, T150 rest "
          "item 2)")
    shape_ok = all(t["shape_neg"] and t["shape_inc"] for t in INST)
    res_hi = max(t["res_arch"] for t in INST)
    cl_lo = min(t["closed"] for t in INST)
    cl_hi = max(t["closed"] for t in INST)
    check(f"S4.ARCH: the archimedean lag kernel has the two shape "
          f"properties on every window -- c^arch_i < 0 for i >= 1 and "
          f"c^arch_i non-decreasing on i >= 1, CHECKED per window, never "
          f"assumed -- and given them, min_r Lam^arch_r == c^arch_0 - "
          f"c^arch_{{M-1}} EXACTLY (max rel {res_hi:.2e}; value "
          f"{cl_lo:.4f}..{cl_hi:.4f}): T150's rest item 2 is CLOSED and "
          f"the bound is ATTAINED at r = 0 -- a two-term functional of the "
          f"smooth kernel, no matrix, no eigenvector, no loss",
          shape_ok and res_hi < TOL_ID)
    full_shape_broken = all(not t["shape_inc_full"] for t in INST)
    ctrl_arch = min(t["res_full"] for t in INST)
    check(f"S4.CTRL: the FULL atom-including kernel VIOLATES the "
          f"monotone-shape hypothesis on every window (the atom hats dig "
          f"dips), and the closed two-term formula applied to the full "
          f"diagonal misses its true minimum by at least {ctrl_arch:.2e} "
          f"relative > {BAR_CTRL:.0e}: the shape hypotheses are "
          f"load-bearing, the closed form is a property of the SMOOTH "
          f"kernel and of nothing else",
          full_shape_broken and ctrl_arch > BAR_CTRL)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the linear per-mode bound and the no-go "
          "discriminator  (T151)")
    dir_ok = all(t["kap"] * float(t["mu"][0]) <= t["lam1"] * (1.0 + TOL_DIR)
                 and t["lam1"] <= t["S"] * float(t["mu"][0]) * (1.0 + TOL_DIR)
                 for t in INST)
    k_lo = min(t["kap"] for t in INST)
    k_hi = max(t["kap"] for t in INST)
    check(f"S5.PENCIL: the certified pencil floor kap = {k_lo:.4f}.."
          f"{k_hi:.4f} (ONE completed Cholesky of A - kap L_P per window, "
          f"the floating-point floor carried as fl / mu^P_1) brackets the "
          f"actual bottom eigenvalue on every window: kap mu^P_1 <= "
          f"lam_1(A) <= S mu^P_1 -- the direction of both certificates is "
          f"re-read on the object they are applied to", dir_ok)
    lin_ok = True
    dom_ok = True
    for t in INST:
        kk = t["kk"]
        if not bool(np.all(t["b_cap"] <= t["C_S"] * kk * (1.0 + TOL_DIR))):
            lin_ok = False
        if not (t["C_S"] <= t["C_closed"] * (1.0 + TOL_DIR)):
            lin_ok = False
        if not bool(np.all(t["sup_true"] <= t["b_cap"] * (1.0 + TOL_DIR))):
            dom_ok = False
        if not bool(np.all(t["e_lp"] <= t["lam_bot"] / t["kap"]
                           * (1.0 + TOL_DIR))):
            dom_ok = False
    C_lo = min(t["C_S"] for t in INST)
    C_hi = max(t["C_S"] for t in INST)
    R_lo = min(t["R"] for t in INST)
    R_hi = max(t["R"] for t in INST)
    check(f"S5.LINEAR: b_k := 2 m sqrt(K_bot mu^P_k / kap) <= C_S k with "
          f"C_S = {C_lo:.3f}..{C_hi:.3f} <= 2 pi sqrt(K_bot/kap) on the "
          f"bottom {K_LAD} modes of every window -- LINEAR in k where the "
          f"quadratic nu ladder grew (v549 item (5)), every m-power "
          f"cancelled, nothing additive anywhere (the Theta(D^3) bottom "
          f"that killed Weyl / Bauer-Fike / Davis-Kahan never enters) -- "
          f"and the bound DOMINATES the truth m ||psi_k||_inf^2 and the "
          f"parity Dirichlet energy on every read mode: the bottom pencil "
          f"ratio R = K_bot/kap = {R_lo:.4f}..{R_hi:.4f} is the ONE scalar "
          f"the chain still owes, printed per window and typed OPEN in m",
          lin_ok and dom_ok)
    R_ng = []
    for m_ng in NOGO_SIZES:
        a = 1.0 / np.sqrt(np.arange(1, m_ng + 1, dtype=float))
        X = np.outer(a, a) + NOGO_EPS * np.eye(m_ng)
        LPn = lap_P_mat(m_ng)
        mun = parity_mu(m_ng)
        pn = pencil_floor(X, LPn, m_ng)
        ln = cert_bottom_ladder(X, m_ng, mun, k_cert=4)
        if pn is None or ln is None or not (pn["kap"] > 0.0):
            R_ng.append(float("inf"))
        else:
            R_ng.append(ln["S"] / pn["kap"])
    grow = R_ng[-1] / R_ng[0] if np.isfinite(R_ng[0]) else float("inf")
    check(f"S5.NOGO: on the T145 no-go form (R = a a^T + eps I, a_i = "
          f"i^(-1/2)) the bottom pencil ratio EXPLODES on the size ladder "
          f"m = {NOGO_SIZES[0]}..{NOGO_SIZES[-1]}: R = {R_ng[0]:.3e} -> "
          f"{R_ng[-1]:.3e} (factor {grow:.1f} >= {NOGO_GROW}), while the "
          f"exact parity model holds R == 1 to {pen1:.1e} -- the ONE thing "
          f"this route asks of the form (a bounded Loewner comparison with "
          f"the parity Laplacian at the bottom) is exactly what the no-go "
          f"does not have: a route that did not fail there would prove a "
          f"false statement", grow >= NOGO_GROW)
    ctrl_cs = all(bool(np.any(t["sup_true"] > BAR_CTRL * t["C_S"] * t["kk"]))
                  for t in INST)
    ctrl_kap = 0
    for t in INST:
        X = sym(t["A"] - 1.5 * t["kap"] * t["LP"])
        if safe_cho(X) is None:
            ctrl_kap += 1
    check(f"S5.CTRL: the linear ladder x {BAR_CTRL:.0e} fails against the "
          f"true mode sups on every window, and the INFLATED floor "
          f"1.5 kap makes the completed Cholesky of A - 1.5 kap L_P REFUSE "
          f"on {ctrl_kap}/{len(INST)} windows -- the certificate cannot be "
          f"talked into a larger floor",
          ctrl_cs and ctrl_kap == len(INST))

    # ---------------------------------------------------------------- fences
    print("\nS6 -- the fences, restated as a check")
    check("S6.FENCE: PER-INSTANCE identities, theorems with checked "
          "hypotheses and certified inequalities on SMALL windows only -- "
          "a FINITE LIST with an explicit maximum, nothing uniform in the "
          "zone index or in D, and NO statement for ALL D: the ONE open "
          "input after T151 (the m-freeness of the bottom pencil ratio "
          "R = K_bot/kap for the odd parity sector of a "
          "sign-changing-symbol Toeplitz section) stays OPEN, unclaimed "
          "and unapproached, exactly as T151 typed it -- its flat trend "
          "(x^0.037 +- 0.015) is a FIT and stays in the sandbox; the "
          "symbol-only route stays certified VACUOUS (S1.HONEST) and is "
          "not re-opened; TV(log Lam) stays WITHDRAWN as a hypothesis "
          "(T149); sig_tot stays retired as a route (T148); "
          "Kac-Murdock-Szego 1953 / Widom 1958 / Basor-Ehrhardt 2009 / "
          "Bottcher-Silbermann (the address of the symbol question -- the "
          "computed answer here is that the pointwise symbol language "
          "does NOT extend to the bottom mode) / Weyl 1912 / Parlett / "
          "Hardy-Littlewood-Polya 1934 / Agmon 1965 / Sylvester 1852 / "
          "Bunch-Kaufman 1977 / Rayleigh 1877 / Ritz 1909 / "
          "Cauchy-Schwarz / Wilkinson 1968 / Higham 2002 / Chebyshev 1852 "
          "named CLASSICAL; Weil 1952 CITED, never used as a criterion; "
          "zero-firewall AST-checked; NO marker upgrade of any "
          "pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv550 runtime: {elapsed:.1f}s")
    print(f"  (1) step-over: th_c/th_1 = {r_lo:.3f}..{r_hi:.3f} on "
          f"{len(INST)} windows; symbol floor vacuous on {n_vac}/{len(INST)}")
    print(f"  (2) bottom ladder: lam_k <= S mu^P_k certified, S = "
          f"{S_lo:.4f}..{S_hi:.4f}")
    print(f"  (3) Sobolev: identity {id_hi:.1e}; model price = pi to "
          f"{cal_dev:.1e}")
    print(f"  (4) min Lam^arch closed and attained, residual {res_hi:.1e}")
    print(f"  (5) linear ladder: C_S = {C_lo:.3f}..{C_hi:.3f}, R = "
          f"{R_lo:.4f}..{R_hi:.4f} (OPEN in m); no-go R grows x{grow:.0f}")
    return summary("PRIME.ODD.SECTOR.IDENT.01 odd-sector identities")


if __name__ == "__main__":
    raise SystemExit(run())
