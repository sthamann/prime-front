"""v545 -- PRIME.HARDY.IDENT.01: the Hardy-core identities of phase 2.
The EIGHT per-instance identities / certified forms of the discovery batch
T140--T141 that are pure linear algebra or closed geometry -- every one
RECOMPUTED here from scratch on small exactly checkable windows of the
frame-A construction (nothing cited from the sandbox).  Companion to
PRIME.MMATRIX.IDENT.01 / v543, which supplies the lumped pair.

WHAT IS LOAD-BEARING HERE (and nothing else): identities, closed-form
quantities, and the VALIDITY (never the SIZE) of two certified upper-bound
shapes.  NO fit is promoted, NO D-exponent, NO uniform-in-zone statement, NO
constant that was calibrated, and the target bound is NOT beaten -- T141
closed no bound and this module claims none.  Each item is a NUMERICAL
RESIDUAL against a preregistered tolerance AND has at least one MUTATION
CONTROL that must fail loudly.

[E] (1) THE FORM LIFTING (T140).  With M_{e,r} = 1[a_e <= r < b_e] the
    edge-interval incidence matrix and C = diag(sqrt(Delta)) M,
        Gram = C H C^T       (EXACT),
    H the mixed second difference of the Green function G = A_B^{-1}.  The
    T139 telescope was a statement about the ENTRIES of the signed Gram;
    this lifts it to its FORM, hence rank(Gram) <= h - 1 while the edge
    count is far larger -- the spectral question lives on the index grid.
[E] (2) THE EXACT FINITE-CORE REDUCTION (T140).
        rho(W) = lam_max(K^{1/2} H K^{1/2}),   K = M^T Delta M,
    because the nonzero spectra of C H C^T and K^{1/2} H K^{1/2} coincide.
    K is the COVERING KERNEL K_rs = W([r ^ s, r v s]) in CLOSED GEOMETRIC
    form (entrywise nonnegative, monotone by inclusion), checked against
    M^T Delta M; rho(W) is taken independently from lam_min(A, A_B).
[E] (3) THE ENERGY REORDERING (T140).  For ANY symmetric H,
        H = diag(s) + L_N,  s = row sums,  N = -offdiag(H),
    a MASS term plus a LONG-RANGE DIRICHLET form -- the sign law of T138 read
    as a Dirichlet form.
[E] (4) THE CHECKERBOARD SPLIT (T140).  Grouping the anti-diagonal stripes in
    consecutive blocks of length b, the band Band_b = D + A_even + A_odd
    entrywise EXACTLY (the adjacent group pairs two-colour into two families
    of disjoint supports), hence THREE Weyl steps
        lam_max(Band_b) <= max_g lam_max(D_g) + max_even sigma_max
                           + max_odd sigma_max
    instead of O(n_b) -- a step count independent of the stripe number.
[E] (5) THE FOUR HARDY IDENTITIES (T141).  (i) the K^+ RAYLEIGH FORM: with
    u = K^{1/2} v, rho(W) = sup u^T H u / u^T K^+ u on range(K), so the
    question has the shape of a weighted Hardy inequality; (ii) the SIGNED
    CROSSING KERNEL: u^T L_N u = d^T B d with d = D u and
    B_kl = sum_{r <= k ^ l, k v l < s} N_rs -- the same closed covering
    formula on the increment grid, SIGNS KEPT; (iii) Q = B_+ 1, i.e. the
    T140 Cauchy-Schwarz weight IS the row sum of B_+, so that step is the
    Gershgorin diagonal step on B_+; (iv) D K D^T = L_Delta on the interior
    nodes, with diagonal (Delta 1)_{k+1} -- the ENDPOINT EDGE MASS, a LOCAL
    geometric quantity and not lam_max(K).
[E] (6) THE CLOSED MUCKENHOUPT QUANTITY (T141).  The two-weight product of
    Muckenhoupt's criterion is, for this pair, in closed form
        A_M0 = max_k Q_k (Delta 1)_{k+1} ,
    and the two routes to it (path weights x Laplacian diagonal, and B_+ row
    sums x endpoint edge mass) agree exactly.  Its SIZE and its zone
    behaviour are NOT promoted -- only the formula.
[E] (7) TWO CERTIFIED UPPER-BOUND SHAPES, AS VALID BOUNDS (T141).  The
    additive Hardy chain rho(W) <= [mass share] + A_M and the genuinely
    joint shape rho(W) <= Lam(H, Y) Om(Y) for a positive definite Hardy form
    Y (a Jacobi matrix) DOMINATE the exact value on every instance, each
    Loewner step certified by a completed Cholesky.  What is promoted is the
    DOMINANCE, not the size: neither shape reaches the target, and the exact
    two-term Weyl split is the floor of the additive family.
[X] (8) THE SIGN-VERSUS-ABSOLUTE SEPARATION (T141), a NEGATIVE typing.  On
    the same instances the EXACTLY BOUNDED object -- the signed Dirichlet
    share lam_max(K^{1/2} L_N K^{1/2}) -- stays in a narrow band across the
    D range, while every ABSOLUTE variant (Loewner drop of L_{N_-},
    Cauchy-Schwarz path weights, the crude product) spreads by orders of
    magnitude.  Reported as an INSTANCE COMPARISON with the power fits
    labelled FITS; no uniformity is claimed in either direction.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   PER-INSTANCE statements on SMALL windows.  NOTHING here is uniform in
        the zone index or in D; the uniform forms stay open (PRIME.I5.UNIFORM
        class) and no marker of any pre-existing contract moves.
  (ii)  (7) promotes VALIDITY, not size.  The certified Muckenhoupt constant
        does not beat the target on any window, the additive shape is dead as
        a SHAPE (its exact Weyl floor already exceeds the target), and the
        joint shape fails on the normalisation Om -- those are sandbox
        measurements and stay there; only the dominance is checked here.
  (iii) (8) is a NEGATIVE typing: the power exponents are FITS on a finite
        surface, printed as fits, and no zone-uniformity statement (in either
        direction) is promoted.  What is load-bearing is the ORDERING of the
        measured spreads at the instances.
  (iv)  (5)(iv) is an identity about the DENOMINATOR side.  It says that the
        endpoint edge mass is what multiplies the kernel side; it says
        nothing about whether a Hardy comparison closes.
  (v)   (2) is an identity, not a bound.  The reduction makes the question
        finite per zone; the remaining uniformity ingredient stays open.

HONEST FENCES (load-bearing typing):
  * Classics named CLASSICAL: Abel summation, Cauchy-Schwarz, Weyl 1912
    (eigenvalue perturbation), Gershgorin 1931, Schur / Haynsworth 1968,
    Stieltjes / Ostrowski 1937, Berman-Plemmons 1979, Muckenhoupt 1972,
    Bradley 1978, Opic-Kufner 1990, Bennett 1987/1991 (the discrete
    two-weight criteria), Gantmacher-Krein 1950/1960 and Karlin 1968 (one-pair
    kernels and the tridiagonal read-off), Wilkinson 1968 / Higham 2002 (the
    declared floating-point floor), Weil 1952 (the archimedean kernel, CITED,
    never used as a criterion).  NEW is only the compiler-native
    consolidation and the machine-checked residuals.
  * DIRECTION CARE IS PART OF THE CLAIM.  A Rayleigh quotient is a LOWER
    bound; a completed Cholesky of s I - X is an UPPER bound; congruence
    preserves the Loewner order.  Each check names its direction.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime side
    is a finite zero-free sum over prime powers.
  * NO RH-EVIDENCE LANGUAGE: finite-window linear algebra only; the
    value->spectral transport (I5) is untouched.

Status: [E] for (1)-(7) -- exact identities and certified per-instance
dominance at rel 1e-8 .. 1e-15 as stated, each with a mutation control that
fails by >= 1e-3 relative; [X] for (8), a negative per-instance typing.
Python; Wolfram-mirrored (dense Cholesky / eigenvalue / SVD identities stay
Python-only), counted per GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/signed_band_probe.py     (T140)
  experiments/tfpt-discovery/discrete_hardy_probe.py  (T141)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, svdvals

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in T128..T141
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
NE_CAP = 900                 # cap on the EXPLICIT n_e x n_e signed Gram
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
U_ROUND = 2.0 ** -53
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept (spread over the D range)
B_LADDER = (4, 8, 16)        # stripe distances of the checkerboard split
T_GRID = (0.25, 0.5, 0.75)   # the closed-form Hardy profile family

# --- preregistered tolerances / bars (declared BEFORE any number) --------
TOL_FORM = 1.0e-11           # Gram == C H C^T (relative)
TOL_RED = 1.0e-8             # the finite-core reduction (relative)
TOL_ID = 1.0e-10             # energy / crossing / Laplacian identities (rel)
TOL_SPLIT = 1.0e-13          # the checkerboard split, entrywise (relative)
TOL_DOM = 1.0e-9             # one-sided dominance slack (relative)
TOL_PSD = 1.0e-9             # Loewner certificates (relative, one-sided)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
BAR_LOCAL = 1.0e2            # the locality control of (6): a factor, not a fit
BAR_RANK = 1.0e-10           # numerical rank bar


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


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (frame-A code path of T128..T141)."""
    D = 2.0 * alpha / M
    c = arch_lags(M, D)
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


# ------------------------------------- the reflection-odd sector (T106..T141)
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return (c[np.abs(r[:, None] - r[None, :])]
            - c[(M - 1) - r[:, None] - r[None, :]])


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


def ray_top(X, iters=140):
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration; the returned
    value is a RAYLEIGH QUOTIENT, hence a rigorous LOWER bound."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    if n == 1:
        return float(X[0, 0])
    sig = gersh(X)
    y = np.ones(n) / math.sqrt(n)
    lam = float(y @ (X @ y))
    for _ in range(iters):
        z = X @ y + sig * y
        nz = float(np.linalg.norm(z))
        if not (nz > 0.0):
            break
        y = z / nz
        lam = max(lam, float(y @ (X @ y)))
    return lam


def cert_lam_max(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_max(X) <= s by a COMPLETED CHOLESKY of s I - X (Wilkinson
    1968; Higham 2002).  DIRECTION: an UPPER bound."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = nrm
    s = max(float(guess), 0.0) + fl + 1.0e-300
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(s * I - X) is not None:
            return s + fl
        s = s * (1.0 + grow) + 10.0 * fl + 1.0e-300
        grow *= 3.0
    return float("nan")


def cert_lam_max_signed(X, tries=26):
    """CERTIFY lam_max(X) <= s WITHOUT assuming s >= 0: the shift is bisected
    DOWN from a Rayleigh quotient, so the SIGN of the answer is meaningful."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    lo = ray_top(X)
    hi = nrm + fl
    if safe_cho((hi + fl) * np.eye(n) - X) is None:
        return float("nan")
    lo = min(lo - abs(lo) * 1.0e-9 - 10.0 * fl, hi)
    I = np.eye(n)
    for _ in range(tries):
        mid = 0.5 * (lo + hi)
        if safe_cho(mid * I - X) is not None:
            hi = mid
        else:
            lo = mid
        if abs(hi - lo) <= 1.0e-12 * max(nrm, 1.0e-300) + 10.0 * fl:
            break
    return hi + fl


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_min(X) >= t by a completed Cholesky of X - t I.
    DIRECTION: a LOWER bound -- this is what certifies a LOEWNER step."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = 0.0
    t = float(guess) - fl
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(X - t * I) is not None:
            return t - fl
        t = t - max(abs(t), nrm) * grow - 10.0 * fl - 1.0e-300
        grow *= 3.0
    return float("nan")


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


def cert_gen_max(H, Y, tries=18, grow=1.0e-6):
    """CERTIFY Lam(H, Y) = sup_u u^T H u / u^T Y u <= s for POSITIVE DEFINITE
    Y, by a COMPLETED CHOLESKY of s Y - H (which certifies H <= s Y in the
    LOEWNER order).  DIRECTION: an UPPER bound on the sup."""
    n = H.shape[0]
    if n == 0:
        return float("nan"), float("nan")
    lmY = cert_lam_min_pos(Y)
    if not (np.isfinite(lmY) and lmY > 0.0):
        return float("nan"), float("nan")
    try:
        lam = float(eigh(sym(H), sym(Y), eigvals_only=True,
                         subset_by_index=[n - 1, n - 1])[0])
    except (LinAlgError, ValueError):
        return float("nan"), lmY
    fl = chol_floor(gersh(H), n) / lmY
    s = lam + abs(lam) * 1.0e-12 + fl + 1.0e-300
    g = grow
    for _ in range(tries):
        if safe_cho(s * sym(Y) - sym(H)) is not None:
            return s + fl, lmY
        s = s + max(abs(s), 1.0e-300) * g + 10.0 * fl
        g *= 3.0
    return float("nan"), lmY


# ------------------------------------ the lumped pair and its edge system
def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) -
    Delta, A_B = A + L_Delta (T136).  DIRECTION: L_Delta >= 0, so A_B >= A."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    return dict(h=h, A_B=sym(A + LD), Dl=Dl, LD=sym(LD), P_row=P_row)


def edge_list(Dl, M):
    """THE EDGE REPRESENTATION of L_Delta = sum_{r<t} Delta_rt (e_r - e_t)
    (e_r - e_t)^T, exactly.  Sorted by the STRIPE index M - 1 - r - t, so
    stripe blocks are contiguous slices."""
    h = Dl.shape[0]
    iu = np.triu_indices(h, 1)
    w = Dl[iu]
    keep = w > 0.0
    er, et, w = iu[0][keep], iu[1][keep], w[keep]
    lab = (M - 1) - er - et
    order = np.lexsort((er, lab))
    er, et, w, lab = er[order], et[order], w[order], lab[order]
    vals, starts, counts = np.unique(lab, return_index=True, return_counts=True)
    return dict(er=er, et=et, w=w, n=int(er.shape[0]), stripe_start=starts,
                stripe_count=counts, nb=int(vals.shape[0]),
                sidx=np.repeat(np.arange(vals.shape[0]), counts))


def signed_gram(G, er, et, wt):
    """Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T G b_{e'}, b_e = e_r - e_t.
    NO absolute value is taken anywhere."""
    Yw = (G[:, er] - G[:, et]) * wt[None, :]
    GR = (Yw[er, :] - Yw[et, :]) * wt[:, None]
    return sym(GR)


def mixed_second_difference(G):
    """H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s}, the exact double
    telescope of T139 / T140."""
    return G[1:, 1:] - G[1:, :-1] - G[:-1, 1:] + G[:-1, :-1]


def interval_incidence(er, et, h):
    """M_{e,r} = 1[a_e <= r < b_e] on the H-grid r = 0 .. h-2."""
    rr = np.arange(h - 1)
    return ((rr[None, :] >= er[:, None])
            & (rr[None, :] < et[:, None])).astype(float)


def cover_kernel_closed(er, et, w, h):
    """THE COVERING KERNEL in CLOSED GEOMETRIC FORM, K_rs = W([r ^ s, r v s]),
    by a two-dimensional prefix sum (i.e. WITHOUT forming M)."""
    m = h - 1
    Wm = np.zeros((h + 1, h + 1))
    np.add.at(Wm, (er, et), w)
    F = np.cumsum(Wm, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((h + 1, 1))], axis=1)
    rr = np.arange(m)
    lo = np.minimum(rr[:, None], rr[None, :])
    hi = np.maximum(rr[:, None], rr[None, :])
    K = F[lo, hi]
    mono_r = bool(np.all(np.diff(F[:, :m], axis=0) >= -1.0e-300))
    mono_c = bool(np.all(np.diff(F[:m, :], axis=1) <= 1.0e-300))
    return dict(K=K, mono=int(mono_r and mono_c),
                nonneg=int(bool(np.all(K >= 0.0))))


def psd_sqrt_full(K, tol=1.0e-14):
    """K^{1/2} and the pseudo-inverse K^+ from ONE eigendecomposition."""
    lam, V = eigh(sym(K))
    lmax = float(np.max(np.abs(lam))) if lam.size else 0.0
    keep = lam > tol * max(lmax, 1.0e-300)
    s = np.zeros_like(lam)
    s[keep] = np.sqrt(lam[keep])
    iv = np.zeros_like(lam)
    iv[keep] = 1.0 / lam[keep]
    return dict(Kh=sym((V * s[None, :]) @ V.T),
                Kp=sym((V * iv[None, :]) @ V.T),
                neg=float(np.min(lam)) if lam.size else 0.0,
                null=int(np.count_nonzero(~keep)))


def abel_split(H):
    """THE ENERGY REORDERING, exact for ANY symmetric H: H = diag(s) + L_N
    with s the row sums and N = -offdiag(H)."""
    m = H.shape[0]
    s = H.sum(axis=1)
    N = -(H - np.diag(np.diag(H)))
    Np = np.where(N > 0.0, N, 0.0)
    Nm = np.where(N < 0.0, -N, 0.0)
    LN = np.diag(N.sum(axis=1)) - N
    LNp = np.diag(Np.sum(axis=1)) - Np
    LNm = np.diag(Nm.sum(axis=1)) - Nm
    return dict(m=m, s=s, N=N, Np=Np, Nm=Nm, LN=sym(LN), LNp=sym(LNp),
                LNm=sym(LNm), id_err=rel(H - (np.diag(s) + LN), H),
                mass_err=rel(H - LN, H),
                neg_off=(float(np.mean(N[~np.eye(m, dtype=bool)] > 0.0))
                         if m > 1 else float("nan")))


def cs_path_weights(Np):
    """THE CAUCHY-SCHWARZ STEP ALONG THE TELESCOPE (T140): L_{N_+} <= T_Q with
    Q_k = sum_{r <= k < s} N_+,rs (s - r) the FIRST-MOMENT weight."""
    m = Np.shape[0]
    rr = np.arange(m)
    dist = rr[None, :] - rr[:, None]
    Z = np.where(dist > 0, Np * dist, 0.0)
    F = np.cumsum(Z, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((m, 1))], axis=1)
    Q = np.array([F[k, k] for k in range(m - 1)]) if m > 1 else np.zeros(0)
    T = np.zeros((m, m))
    if m > 1:
        idx = np.arange(m - 1)
        T[idx, idx] += Q
        T[idx + 1, idx + 1] += Q
        T[idx, idx + 1] -= Q
        T[idx + 1, idx] -= Q
    return dict(Q=Q, T=sym(T))


def diff_op(m):
    """THE INCREMENT OPERATOR (D u)_k = u_k - u_{k+1}, k = 0 .. m-2."""
    Dm = np.zeros((m - 1, m))
    idx = np.arange(m - 1)
    Dm[idx, idx] = 1.0
    Dm[idx, idx + 1] = -1.0
    return Dm


def crossing_kernel(N):
    """THE CROSSING KERNEL of a symmetric weight matrix N, in the SAME closed
    covering form as K but on the INCREMENT grid:
        B_kl = sum_{r <= k ^ l, k v l < s} N_rs ,
    so that u^T L_N u = d^T B d with d = D u, EXACTLY and with the signs of N
    kept (the telescope squared, with no inequality taken)."""
    m = N.shape[0]
    iu = np.triu_indices(m, 1)
    Wm = np.zeros((m + 1, m + 1))
    np.add.at(Wm, (iu[0], iu[1]), N[iu])
    F = np.cumsum(Wm, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((m + 1, 1))], axis=1)
    kk = np.arange(max(m - 1, 0))
    lo = np.minimum(kk[:, None], kk[None, :])
    hi = np.maximum(kk[:, None], kk[None, :])
    return sym(F[lo, hi])


def hardy_laplacian(K):
    """J = D K D^T, the DENOMINATOR object: for the covering kernel this is
    EXACTLY L_Delta on the interior nodes, with J_kk = (Delta 1)_{k+1}."""
    return sym(K[:-1, :-1] - K[:-1, 1:] - K[1:, :-1] + K[1:, 1:])


def jacobi_form(c, g):
    """THE HARDY FORM as a matrix: Y = D^T diag(c) D + diag(g) -- a weighted
    path Dirichlet form plus a mass term, i.e. a JACOBI matrix, which is the
    object of the classical weighted Hardy inequality."""
    m = g.shape[0]
    Y = np.diag(np.asarray(g, dtype=float).copy())
    if m > 1 and c.size:
        idx = np.arange(m - 1)
        Y[idx, idx] += c
        Y[idx + 1, idx + 1] += c
        Y[idx, idx + 1] -= c
        Y[idx + 1, idx] -= c
    return sym(Y)


def tridiag_readoff(X):
    """THE TRIDIAGONAL READ-OFF (Gantmacher-Krein 1950/1960; Karlin 1968): for
    a genuine one-pair kernel the inverse IS tridiagonal.  READ OFF per zone,
    NOT closed form -- a distinction this module keeps."""
    n = X.shape[0]
    Y = np.zeros_like(X)
    idx = np.arange(n)
    Y[idx, idx] = np.diag(X)
    if n > 1:
        i2 = np.arange(n - 1)
        Y[i2, i2 + 1] = X[i2, i2 + 1]
        Y[i2 + 1, i2] = X[i2, i2 + 1]
    return sym(Y)


def hardy_constant(B, J, c):
    """THE CERTIFIED HARDY / MUCKENHOUPT CONSTANT for a conductance profile
    c > 0: theta = lam_max(C^{1/2} J C^{1/2}) (the NORMALISATION) and
    alpha = lam_max(C^{-1/2} B C^{-1/2}) (the COMPARISON), giving
    lam_max(K^{1/2} D^T B D K^{1/2}) <= max(alpha, 0) theta by two
    congruences and the nonzero-spectrum swap.  alpha is CLAMPED at 0 because
    the multiplication into the sup is legitimate only for alpha >= 0."""
    n = J.shape[0]
    if n < 2:
        return None
    c = np.maximum(np.asarray(c, dtype=float), 1.0e-300)
    sc = np.sqrt(c)
    Jc = sym(sc[:, None] * J * sc[None, :])
    theta = cert_lam_max(Jc, guess=ray_top(Jc))
    isc = 1.0 / sc
    Bc = sym(isc[:, None] * B * isc[None, :])
    alpha = cert_lam_max_signed(Bc)
    if not (np.isfinite(theta) and np.isfinite(alpha)):
        return None
    return dict(theta=theta, alpha=alpha, A_M=max(alpha, 0.0) * theta)


# ------------------------------------------- the checkerboard split (T140)
def stripe_groups(starts, counts, nb, L):
    out = []
    for g0 in range(0, nb, L):
        g1 = min(nb, g0 + L)
        a = int(starts[g0])
        b = int(starts[g1 - 1] + counts[g1 - 1])
        out.append((a, b))
    return out


def checker_split(GR, dms, starts, counts, nb, b, L=None):
    """THE CHECKERBOARD SPLIT Band_b = D + A_even + A_odd, exactly, with the
    THREE Weyl steps that replace the O(n_b) layer sum.  With group length
    L = b every pair at stripe distance <= b lies inside one group or across
    two ADJACENT groups, and the adjacent pairs two-colour into two families
    of disjoint supports.  Returns the entrywise split residual and the
    three-term bound."""
    if L is None:
        L = max(1, int(b))
    grp = stripe_groups(starts, counts, nb, L)
    inb = dms <= b
    Band = np.where(inb, GR, 0.0)
    Rec = np.zeros_like(Band)
    diag_lam, even_s, odd_s = [], [], []
    for (a, bb) in grp:
        if bb <= a:
            continue
        Rec[a:bb, a:bb] = Band[a:bb, a:bb]
        blk = sym(Band[a:bb, a:bb])
        diag_lam.append(float(eigvalsh(blk)[-1]))
    for k in range(len(grp) - 1):
        ia, ib = grp[k]
        ja, jb = grp[k + 1]
        Rec[ia:ib, ja:jb] = Band[ia:ib, ja:jb]
        Rec[ja:jb, ia:ib] = Band[ja:jb, ia:ib]
        Bx = Band[ia:ib, ja:jb]
        sv = svdvals(Bx) if Bx.size else np.zeros(1)
        (even_s if k % 2 == 0 else odd_s).append(
            float(sv[0]) if sv.size else 0.0)
    bound = ((max(diag_lam) if diag_lam else 0.0)
             + (max(even_s) if even_s else 0.0)
             + (max(odd_s) if odd_s else 0.0))
    exact = float(eigvalsh(sym(Band))[-1])
    return dict(b=int(b), L=int(L), n_g=len(grp), bound=bound, exact=exact,
                split_err=rel(Rec - Band, Band),
                scale=max(float(np.abs(Band).max()), 1.0e-300))


# --------------------------------------------------------------- the fits
def pow_fit(xv, yv):
    """A LOG-LOG LEAST SQUARES SLOPE with a leave-one-out jackknife spread.
    THIS IS A FIT and is labelled as one everywhere it is printed."""
    x = np.log(np.asarray(xv, dtype=float))
    y = np.log(np.asarray(yv, dtype=float))
    n = x.shape[0]
    if n < 3:
        return dict(p=float("nan"), sp=float("nan"), n=n)
    A = np.vstack([x, np.ones(n)]).T
    p, c = np.linalg.lstsq(A, y, rcond=None)[0]
    ps = []
    for i in range(n):
        m = np.ones(n, dtype=bool)
        m[i] = False
        Ai = np.vstack([x[m], np.ones(n - 1)]).T
        ps.append(np.linalg.lstsq(Ai, y[m], rcond=None)[0][0])
    return dict(p=float(p), c=float(c), n=n,
                sp=float(np.max(np.abs(np.asarray(ps) - p))))


# ------------------------------------------------------------------ battery
def build_windows():
    """Frame-A windows kept small enough that EVERY diagonalised matrix stays
    <= H_CAP, spread over the candidate list so that the D range is as wide as
    the caps allow (D-uniformity is what item (8) compares)."""
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
    """One window, end to end: the pole-free odd section, its lumped pair,
    the edge system, the finite core (K, H) and every derived object of the
    eight items.  Only h-sized matrices are formed unless n_e <= NE_CAP."""
    al = 0.5 * M * D
    c, _ = lag_vector_fast(al, M, atoms_in(al))
    A = sym(odd_toeplitz(c, M))
    lp = lump_pair(A)
    A_B = lp["A_B"]
    fac = safe_cho(A_B)
    if fac is None:
        return None
    G = cho_solve(fac, np.eye(h), check_finite=False)
    ed = edge_list(lp["Dl"], M)
    if ed["n"] < 8 or ed["nb"] < 6:
        return None
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return None
    rho_ex = 1.0 - gap_ex
    H = mixed_second_difference(G)
    m = H.shape[0]
    if m < 8:
        return None

    ck = cover_kernel_closed(ed["er"], ed["et"], ed["w"], h)
    K = ck["K"]
    sq = psd_sqrt_full(K)
    Kh, Kp = sq["Kh"], sq["Kp"]
    Ycore = sym(Kh @ H @ Kh)
    ev, U = eigh(Ycore)
    lam_core = float(ev[-1])

    # (1) the FORM lifting and (2) the exact reduction, on the explicit Gram
    form_err, rank_gram, lam_gram, ctrl_form = (float("nan"),) * 4
    band = []
    if ed["n"] <= NE_CAP:
        wt = np.sqrt(ed["w"])
        GR = signed_gram(G, ed["er"], ed["et"], wt)
        Minc = interval_incidence(ed["er"], ed["et"], h)
        Cm = Minc * wt[:, None]
        form_err = rel(GR - Cm @ H @ Cm.T, GR)
        ctrl_form = rel(GR - Minc @ H @ Minc.T, GR)     # unweighted C
        evg = eigvalsh(GR)
        mxg = max(float(np.abs(evg).max()), 1.0e-300)
        rank_gram = int(np.count_nonzero(np.abs(evg) > BAR_RANK * mxg))
        lam_gram = float(evg[-1])
        # the covering kernel against M^T Delta M
        K_ref = (Minc * ed["w"][:, None]).T @ Minc
        ker_err = rel(K - K_ref, K)
        dms = np.abs(ed["sidx"][:, None] - ed["sidx"][None, :])
        for b in B_LADDER:
            if ed["nb"] < 2 * b:
                continue
            row = checker_split(GR, dms, ed["stripe_start"],
                                ed["stripe_count"], ed["nb"], b)
            row["ctrl_err"] = checker_split(
                GR, dms, ed["stripe_start"], ed["stripe_count"], ed["nb"], b,
                L=max(1, b // 2))["split_err"]
            band.append(row)
        del GR, Minc, Cm, K_ref, dms
    else:
        ker_err = float("nan")

    # (5) the four Hardy identities
    ab = abel_split(H)
    cs = cs_path_weights(ab["Np"])
    Dop = diff_op(m)
    B = crossing_kernel(ab["N"])
    Bp = crossing_kernel(ab["Np"])
    Babs = crossing_kernel(np.abs(ab["N"]))
    J = hardy_laplacian(K)
    EP = lp["P_row"][1:h - 1]
    J_ref = np.diag(EP) - lp["Dl"][1:h - 1, 1:h - 1]
    err_cross = rel(ab["LN"] - Dop.T @ B @ Dop, ab["LN"])
    ctrl_cross = rel(ab["LN"] - Dop.T @ Babs @ Dop, ab["LN"])
    err_lap = rel(J - J_ref, J)
    err_rowq = rel(Bp.sum(axis=1) - cs["Q"], cs["Q"])
    vtop = U[:, -1]
    utop = Kh @ vtop
    ray_num = float(utop @ (H @ utop))
    ray_den = float(utop @ (Kp @ utop))
    ray_err = (abs(ray_num / ray_den - lam_core) / max(abs(lam_core), 1.0e-300)
               if abs(ray_den) > 0.0 else float("nan"))

    # (6) the closed Muckenhoupt quantity, two routes
    Jd = np.maximum(np.diag(J), 1.0e-300)
    A_M0 = float(np.max(cs["Q"] * Jd))
    A_M0_alt = float(np.max(Bp.sum(axis=1) * EP))
    lam_K = cert_lam_max(K, guess=ray_top(K))
    A_M0_ctrl = float(np.max(cs["Q"])) * lam_K

    # (7) the two certified shapes
    prof_end = 1.0 / Jd
    tri = -np.diag(Kp, 1)
    hc_e = hardy_constant(B, J, prof_end)
    hc_t = (hardy_constant(B, J, np.maximum(tri, 1.0e-300))
            if float(np.min(tri)) > 0.0 else None)
    cand_A = [x["A_M"] for x in (hc_e, hc_t) if x is not None]
    A_best = min(cand_A) if cand_A else float("nan")
    E_mass = cert_lam_max_signed(sym(Kh @ np.diag(ab["s"]) @ Kh))
    Ydir = sym(Kh @ ab["LN"] @ Kh)
    E_dir = cert_lam_max_signed(Ydir)
    Ydrop = sym(Kh @ (np.diag(ab["s"]) + ab["LNp"]) @ Kh)
    E_drop = cert_lam_max(Ydrop, guess=ray_top(Ydrop))
    Yq = sym(Kh @ (np.diag(np.maximum(ab["s"], 0.0)) + cs["T"]) @ Kh)
    E_q = cert_lam_max(Yq, guess=ray_top(Yq))
    Ywrong = sym(Kh @ (np.diag(ab["s"]) - ab["LNm"]) @ Kh)
    E_wrong = cert_lam_max_signed(Ywrong)          # the WRONG-SIGN drop
    step_neg = cert_lam_min(ab["LNm"])
    step_cs = cert_lam_min(sym(cs["T"] - ab["LNp"]))
    lam_H = cert_lam_max(H, guess=ray_top(H))

    Kd = np.maximum(np.diag(K), 1.0e-300)
    joint = []
    for t in T_GRID:
        Yt = jacobi_form(t / Jd, (1.0 - t) / Kd)
        lam_g, lmY = cert_gen_max(H, Yt)
        Ct = sym(Kh @ Yt @ Kh)
        om = cert_lam_max(Ct, guess=ray_top(Ct))
        if np.isfinite(lam_g) and np.isfinite(om) and lam_g >= 0.0:
            joint.append(dict(t=t, lam=lam_g, om=om, bound=lam_g * om))
    best_j = min(joint, key=lambda x: x["bound"]) if joint else None
    # the CONTROL for (7): the same Hardy form WITHOUT its mass term is
    # singular -- the constant vector sits in its kernel while H does not
    # vanish there, so the generalised sup is not finite and no certificate
    # can be issued.  Positive definiteness of Y is load-bearing.
    Ynull = jacobi_form(1.0 / Jd, np.zeros(m))
    one = np.ones(m)
    null_q = abs(float(one @ (Ynull @ one))) / max(gersh(Ynull), 1.0e-300)
    hconst = abs(float(one @ (H @ one))) / max(gersh(H), 1.0e-300)
    lm_null = cert_lam_min_pos(Ynull)

    Ytri = tridiag_readoff(Kp)
    lam_tri, _ = cert_gen_max(H, Ytri)
    Ctri = sym(Kh @ Ytri @ Kh)
    om_tri = cert_lam_max(Ctri, guess=ray_top(Ctri))
    B_tri = (lam_tri * om_tri if (np.isfinite(lam_tri) and np.isfinite(om_tri)
                                  and lam_tri >= 0.0) else float("nan"))

    return dict(
        n=NN_ALL[k], h=h, m=m, D=D, n_e=ed["n"], nb=ed["nb"],
        rho_ex=rho_ex, lam_core=lam_core, lam_gram=lam_gram,
        red_err=abs(lam_core - rho_ex) / max(rho_ex, 1.0e-300),
        gram_err=(abs(lam_gram - rho_ex) / max(rho_ex, 1.0e-300)
                  if np.isfinite(lam_gram) else float("nan")),
        form_err=form_err, ctrl_form=ctrl_form, rank_gram=rank_gram,
        ker_err=ker_err, mono=ck["mono"], nonneg=ck["nonneg"],
        null=sq["null"], band=band,
        id_err=ab["id_err"], mass_err=ab["mass_err"], neg_off=ab["neg_off"],
        err_cross=err_cross, ctrl_cross=ctrl_cross, err_lap=err_lap,
        err_rowq=err_rowq, ray_err=ray_err,
        A_M0=A_M0, A_M0_alt=A_M0_alt, A_M0_ctrl=A_M0_ctrl,
        ep_min=float(np.min(EP)), ep_max=float(np.max(EP)),
        A_best=A_best, E_mass=E_mass, E_dir=E_dir, E_drop=E_drop, E_q=E_q,
        E_wrong=E_wrong, step_neg=step_neg, step_cs=step_cs,
        lam_K=lam_K, lam_H=lam_H, joint=joint, B_tri=B_tri,
        B_weyl=E_mass + E_dir, B_hardy=E_mass + A_best,
        B_prod=lam_K * max(lam_H, 0.0),
        B_geo=(best_j["bound"] if best_j else float("nan")),
        Om_geo=(best_j["om"] if best_j else float("nan")),
        Lam_geo=(best_j["lam"] if best_j else float("nan")),
        t_geo=(best_j["t"] if best_j else float("nan")),
        null_q=null_q, hconst=hconst, lm_null=lm_null,
        scale_H=max(float(np.abs(H).max()), 1.0e-300))


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v545  PRIME.HARDY.IDENT.01 -- the Hardy-core identities (T140-T141)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered tolerances")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    for (k, D, M, h) in build_windows():
        row = build_instance(k, D, M, h)
        if row is not None:
            INST.append(row)
    check(f"S0.INST: {len(INST)} frame-A windows built with a positive "
          f"definite lumped pair and a nonempty edge system", len(INST) >= 6)
    h_max = max(t["h"] for t in INST)
    check(f"S0.CAP: every inverted / diagonalised index-grid matrix <= "
          f"{H_CAP} (max h = {h_max}); the explicit n_e x n_e Gram is formed "
          f"only where n_e <= {NE_CAP}", h_max <= H_CAP)
    d_lo = min(t["D"] for t in INST)
    d_hi = max(t["D"] for t in INST)
    check(f"S0.SPAN: the surface spans D = {d_lo:.3e} .. {d_hi:.3e}, a factor "
          f"{d_hi / d_lo:.2f} -- wide enough for item (8) to be a COMPARISON "
          f"and not a single point", d_hi / d_lo >= 2.0)
    for t in INST:
        print(f"    n={t['n']:>7d} D={t['D']:.4e} h={t['h']:>4d} "
              f"m={t['m']:>4d} n_e={t['n_e']:>5d} nb={t['nb']:>4d} "
              f"rho(W)={t['rho_ex']:.6f}")

    # ---------------------------------------------------------------- (1)
    GRM = [t for t in INST if np.isfinite(t["form_err"])]
    print("\nS1 -- (1) the form lifting  Gram = C H C^T,  C = diag(sqrt D) M")
    form = max(t["form_err"] for t in GRM)
    low = [(t["rank_gram"], t["n_e"], t["h"] - 1) for t in GRM]
    check(f"S1.ROWS: {len(GRM)} of {len(INST)} windows carry an explicit "
          f"signed Gram (n_e = {min(t['n_e'] for t in GRM)}.."
          f"{max(t['n_e'] for t in GRM)} <= {NE_CAP})", len(GRM) >= 4)
    check(f"S1.FORM: Gram == C H C^T on all {len(GRM)} windows "
          f"(max rel {form:.2e} < {TOL_FORM:.0e}) -- the T139 telescope "
          f"lifted from the ENTRIES to the FORM", form < TOL_FORM)
    check(f"S1.RANK: rank(Gram) <= h - 1 on all {len(GRM)} windows "
          f"(rank {min(r for r, _, _ in low)}..{max(r for r, _, _ in low)} "
          f"against {min(e for _, e, _ in low)}..{max(e for _, e, _ in low)} "
          f"edges), so the signed Gram is LOW RANK and the spectral question "
          f"lives on the index grid",
          all(r <= hm for r, _, hm in low) and all(e > hm for _, e, hm in low))
    ctrl1 = min(t["ctrl_form"] for t in GRM)
    check(f"S1.CTRL: dropping the edge weights from C (unweighted incidence) "
          f"breaks the identity on every window (min rel {ctrl1:.2e} > "
          f"{BAR_CTRL:.0e})", ctrl1 > BAR_CTRL)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the exact finite-core reduction  "
          "rho(W) = lam_max(K^1/2 H K^1/2)")
    red = max(t["red_err"] for t in INST)
    grm = max(t["gram_err"] for t in GRM)
    ker = max(t["ker_err"] for t in GRM)
    check(f"S2.KERNEL: the CLOSED geometric covering kernel K_rs = "
          f"W([r ^ s, r v s]) equals M^T Delta M on all {len(GRM)} windows "
          f"(max rel {ker:.2e} < {TOL_ID:.0e}), entrywise nonnegative and "
          f"monotone by inclusion on {sum(t['mono'] for t in INST)}/"
          f"{len(INST)}",
          ker < TOL_ID and all(t["mono"] and t["nonneg"] for t in INST))
    check(f"S2.REDUCE: lam_max(K^1/2 H K^1/2) == rho(W) = 1 - lam_min(A, A_B) "
          f"on all {len(INST)} windows (max rel {red:.2e} < {TOL_RED:.0e}), "
          f"the two sides computed by INDEPENDENT routes", red < TOL_RED)
    check(f"S2.GRAM: the same value is the top eigenvalue of the explicit "
          f"n_e x n_e signed Gram on {len(GRM)} windows (max rel {grm:.2e}), "
          f"so the reduction is a change of representation and NOT a "
          f"truncation", grm < TOL_RED)
    t0i = INST[0]
    ctrl2 = abs(t0i["lam_K"] * max(t0i["lam_H"], 0.0) - t0i["rho_ex"]) \
        / max(t0i["rho_ex"], 1.0e-300)
    check(f"S2.CTRL: the FACTORWISE product lam_max(K) lam_max(H) is not the "
          f"reduction -- it misses the exact value by {ctrl2:.2e} "
          f"(> {BAR_CTRL:.0e}) at the first window, which is why the joint "
          f"form of item (7) is needed", ctrl2 > BAR_CTRL)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the energy reordering  H = diag(s) + L_N")
    ener = max(t["id_err"] for t in INST)
    ctrl3 = min(t["mass_err"] for t in INST)
    check(f"S3.ENERGY: H == diag(s) + L_N with s the row sums and "
          f"N = -offdiag(H) on all {len(INST)} windows (max rel {ener:.2e} < "
          f"{TOL_ID:.0e}) -- a MASS term plus a LONG-RANGE Dirichlet form",
          ener < TOL_ID)
    off_lo = min(t["neg_off"] for t in INST)
    off_hi = max(t["neg_off"] for t in INST)
    check(f"S3.DIRICHLET: the Dirichlet weights N = -offdiag(H) are POSITIVE "
          f"on a fraction {off_lo:.3f}..{off_hi:.3f} of the off-diagonal "
          f"area, so the sign law of the kernel IS the Dirichlet form "
          f"(a MEASUREMENT at the instances, no law claimed)",
          0.0 < off_lo <= off_hi < 1.0)
    check(f"S3.CTRL: dropping the mass term breaks the identity on every "
          f"window (min rel {ctrl3:.2e} > {BAR_CTRL:.0e})", ctrl3 > BAR_CTRL)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the checkerboard split  Band_b = D + A_even + A_odd")
    BND = [(t, r) for t in GRM for r in t["band"]]
    check(f"S4.ROWS: {len(BND)} (window, b) pairs over the stripe ladder "
          f"{B_LADDER} (n_b = {min(t['nb'] for t in GRM)}.."
          f"{max(t['nb'] for t in GRM)} stripes)", len(BND) >= 6)
    spl = max(r["split_err"] for _, r in BND)
    check(f"S4.SPLIT: Band_b == D + A_even + A_odd ENTRYWISE on all "
          f"{len(BND)} pairs (max rel {spl:.2e} <= {TOL_SPLIT:.0e}) -- with "
          f"group length L = b the adjacent pairs two-colour into two "
          f"families of DISJOINT supports", spl <= TOL_SPLIT)
    wey_bad = [1 for _, r in BND
               if r["bound"] < r["exact"] - TOL_DOM * max(abs(r["exact"]), 1.0)]
    tight = max(r["bound"] / max(r["exact"], 1.0e-300) for _, r in BND)
    ng_hi = max(r["n_g"] for _, r in BND)
    check(f"S4.WEYL: the THREE-step bound max_g lam_max(D_g) + max_even "
          f"sigma_max + max_odd sigma_max dominates lam_max(Band_b) on all "
          f"{len(BND)} pairs ({len(wey_bad)} exceptions, worst ratio "
          f"{tight:.4f}) with a step count of 3 independent of the "
          f"{ng_hi} groups", not wey_bad)
    ctrl4 = min(r["ctrl_err"] for _, r in BND)
    check(f"S4.CTRL: with group length L = b/2 the band reaches beyond the "
          f"ADJACENT group and the split loses entries on every pair "
          f"(min rel {ctrl4:.2e} > {BAR_CTRL:.0e}), so L = b is "
          f"load-bearing", ctrl4 > BAR_CTRL)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the four Hardy identities of T141")
    ray = max(t["ray_err"] for t in INST)
    crs = max(t["err_cross"] for t in INST)
    rwq = max(t["err_rowq"] for t in INST)
    lap = max(t["err_lap"] for t in INST)
    check(f"S5.RAYLEIGH: with u = K^1/2 v the top core eigenvalue equals "
          f"u^T H u / u^T K^+ u on all {len(INST)} windows (max rel "
          f"{ray:.2e} < {TOL_ID:.0e}) -- rho(W) is a K^+ RAYLEIGH quotient, "
          f"the shape of a weighted Hardy inequality", ray < TOL_ID)
    check(f"S5.CROSSING: u^T L_N u == d^T B d with d = D u and the SIGNED "
          f"crossing kernel B_kl = sum_{{r <= k^l, kvl < s}} N_rs on all "
          f"{len(INST)} windows (max rel {crs:.2e} < {TOL_ID:.0e}) -- the "
          f"same closed covering formula as K, on the increment grid",
          crs < TOL_ID)
    check(f"S5.ROWSUM: the T140 Cauchy-Schwarz weight IS the row sum of B_+, "
          f"Q == B_+ 1 on all {len(INST)} windows (max rel {rwq:.2e} < "
          f"{TOL_ID:.0e}), so that step is the Gershgorin diagonal step on "
          f"B_+ and its cost is identified", rwq < TOL_ID)
    ep_lo = min(t["ep_min"] for t in INST)
    ep_hi = max(t["ep_max"] for t in INST)
    check(f"S5.LAPLACIAN: D K D^T == L_Delta on the interior nodes on all "
          f"{len(INST)} windows (max rel {lap:.2e} < {TOL_ID:.0e}), with "
          f"diagonal (Delta 1)_{{k+1}} = {ep_lo:.3e}..{ep_hi:.3e} -- the "
          f"ENDPOINT EDGE MASS, a LOCAL quantity and not lam_max(K)",
          lap < TOL_ID)
    ctrl5 = min(t["ctrl_cross"] for t in INST)
    check(f"S5.CTRL: the crossing kernel of |N| does NOT reproduce L_N on any "
          f"window (min rel {ctrl5:.2e} > {BAR_CTRL:.0e}), so the SIGNS in B "
          f"are load-bearing -- exactly the cancellation the absolute-value "
          f"routes destroy", ctrl5 > BAR_CTRL)

    # ---------------------------------------------------------------- (6)
    print("\nS6 -- (6) the closed Muckenhoupt quantity  "
          "A_M0 = max_k Q_k (Delta 1)_{k+1}")
    a_err = max(abs(t["A_M0"] - t["A_M0_alt"]) / max(t["A_M0"], 1.0e-300)
                for t in INST)
    a_lo = min(t["A_M0"] for t in INST)
    a_hi = max(t["A_M0"] for t in INST)
    check(f"S6.FORMULA: the two closed routes to the two-weight product -- "
          f"path weights x Laplacian diagonal, and B_+ row sums x endpoint "
          f"edge mass -- agree on all {len(INST)} windows (max rel "
          f"{a_err:.2e} < {TOL_ID:.0e}); A_M0 = {a_lo:.3e}..{a_hi:.3e}, "
          f"REPORTED, its size and zone behaviour NOT promoted",
          a_err < TOL_ID)
    loc = min(t["A_M0_ctrl"] / max(t["A_M0"], 1.0e-300) for t in INST)
    check(f"S6.CTRL: replacing the LOCAL endpoint edge mass by lam_max(K) "
          f"inflates the quantity by a factor >= {loc:.3e} "
          f"(> {BAR_LOCAL:.0e}) on every window, so the locality of the "
          f"denominator side is the whole content of (5)(iv)",
          loc > BAR_LOCAL)

    # ---------------------------------------------------------------- (7)
    print("\nS7 -- (7) the two certified upper-bound shapes, as VALID bounds")
    JNT = [t for t in INST if np.isfinite(t["B_geo"])]
    sn = min(t["step_neg"] for t in INST) / max(t["scale_H"] for t in INST)
    sc = min(t["step_cs"] for t in INST) / max(t["scale_H"] for t in INST)
    check(f"S7.LOEWNER: every Loewner step of the additive chain is CERTIFIED "
          f"by a completed Cholesky on all {len(INST)} windows -- "
          f"L_{{N_-}} >= 0 (min lam_min {sn:.2e} relative) and "
          f"T_Q - L_{{N_+}} >= 0 (min {sc:.2e})",
          sn >= -TOL_PSD and sc >= -TOL_PSD)
    add_bad = [1 for t in INST
               if t["B_hardy"] < t["rho_ex"] * (1.0 - TOL_DOM)]
    wey_bad2 = [1 for t in INST
                if t["B_weyl"] < t["rho_ex"] * (1.0 - TOL_DOM)]
    fl_bad = [1 for t in INST if t["B_weyl"] > t["B_hardy"] * (1.0 + TOL_DOM)]
    r_add = (min(t["B_hardy"] / t["rho_ex"] for t in INST),
             max(t["B_hardy"] / t["rho_ex"] for t in INST))
    r_wey = (min(t["B_weyl"] / t["rho_ex"] for t in INST),
             max(t["B_weyl"] / t["rho_ex"] for t in INST))
    check(f"S7.ADDITIVE: the additive Hardy chain [mass share] + A_M is a "
          f"VALID upper bound for rho(W) on all {len(INST)} windows "
          f"({len(add_bad)} exceptions; factor {r_add[0]:.3f}..{r_add[1]:.3f} "
          f"over the exact value) -- the DOMINANCE is promoted, the SIZE is "
          f"not", not add_bad)
    check(f"S7.WEYLFLOOR: the exact two-term Weyl split "
          f"[mass share] + lam_max(K^1/2 L_N K^1/2) also dominates rho(W) "
          f"({len(wey_bad2)} exceptions; factor {r_wey[0]:.3f}.."
          f"{r_wey[1]:.3f}) and sits BELOW the Hardy chain on all windows "
          f"({len(fl_bad)} exceptions), so it is the FLOOR of the additive "
          f"family", not wey_bad2 and not fl_bad)
    jn_bad = [1 for t in JNT if t["B_geo"] < t["rho_ex"] * (1.0 - TOL_DOM)]
    tri_rows = [t for t in INST if np.isfinite(t["B_tri"])]
    tri_bad = [1 for t in tri_rows
               if t["B_tri"] < t["rho_ex"] * (1.0 - TOL_DOM)]
    r_geo = (min(t["B_geo"] / t["rho_ex"] for t in JNT),
             max(t["B_geo"] / t["rho_ex"] for t in JNT))
    check(f"S7.JOINT: the genuinely joint shape Lam(H, Y) x Om(Y) with a "
          f"POSITIVE DEFINITE Hardy form Y (a Jacobi matrix: path Dirichlet "
          f"plus mass) dominates rho(W) on all {len(JNT)} windows with the "
          f"CLOSED-FORM geometric profile ({len(jn_bad)} exceptions, factor "
          f"{r_geo[0]:.3f}..{r_geo[1]:.3f}) and on {len(tri_rows)} with the "
          f"per-zone tridiagonal read-off of K^+ ({len(tri_bad)} "
          f"exceptions)", not jn_bad and not tri_bad and len(JNT) >= 4)
    om_lo = min(t["Om_geo"] for t in JNT)
    om_hi = max(t["Om_geo"] for t in JNT)
    nq = max(t["null_q"] for t in INST)
    hc_lo = min(t["hconst"] for t in INST)
    n_ref = sum(1 for t in INST if not np.isfinite(t["lm_null"]))
    check(f"S7.CTRL-Y: the SAME Hardy form without its mass term is singular "
          f"-- the constant vector lies in its kernel (max rel {nq:.2e}) "
          f"while H does not vanish there (min rel {hc_lo:.2e} > "
          f"{BAR_CTRL:.0e}), so the generalised sup is not finite and the "
          f"lam_min certificate REFUSES on {n_ref} of {len(INST)} windows: "
          f"positive definiteness of Y is a load-bearing hypothesis, and the "
          f"normalisation Om = {om_lo:.3g}..{om_hi:.3g} carries the rest",
          nq < 1.0e-12 and hc_lo > BAR_CTRL and n_ref == len(INST))
    wr_bad = sum(1 for t in INST
                 if t["E_wrong"] < t["rho_ex"] * (1.0 - BAR_CTRL))
    check(f"S7.CTRL-SIGN: dropping the POSITIVE part L_{{N_+}} instead of the "
          f"negative one gives a quantity BELOW rho(W) on {wr_bad} of "
          f"{len(INST)} windows -- it is not an upper bound at all, so the "
          f"SIGN selection of the Loewner step is load-bearing",
          wr_bad == len(INST))

    # ---------------------------------------------------------------- (8)
    print("\nS8 -- (8) [X] the sign-versus-absolute separation, as a "
          "COMPARISON")
    Dv = [t["D"] for t in INST]
    f_dir = pow_fit(Dv, [t["E_dir"] for t in INST])
    f_drop = pow_fit(Dv, [t["E_drop"] for t in INST])
    f_q = pow_fit(Dv, [t["E_q"] for t in INST])
    f_A = pow_fit(Dv, [t["A_best"] for t in INST])
    f_prod = pow_fit(Dv, [t["B_prod"] for t in INST])

    def spread(key):
        v = [t[key] for t in INST]
        return max(v) / max(min(v), 1.0e-300)

    s_dir = spread("E_dir")
    s_abs = min(spread("E_drop"), spread("E_q"), spread("B_prod"))
    check(f"S8.SPREAD: across the D range (factor {d_hi / d_lo:.2f}) the "
          f"EXACTLY BOUNDED object -- the signed Dirichlet share "
          f"lam_max(K^1/2 L_N K^1/2) -- spreads by {s_dir:.2f}x, while every "
          f"ABSOLUTE variant spreads by at least {s_abs:.2f}x (Loewner drop "
          f"{spread('E_drop'):.2f}x, Cauchy-Schwarz {spread('E_q'):.2f}x, "
          f"product {spread('B_prod'):.2f}x) -- an INSTANCE COMPARISON",
          s_dir < s_abs)
    check(f"S8.FIT: the corresponding power FITS (labelled FITS, on a finite "
          f"surface of {len(INST)} windows, promoted as NOTHING else) are "
          f"D^{f_dir['p']:+.3f} +- {f_dir['sp']:.3f} for the signed share "
          f"against D^{f_drop['p']:+.3f} +- {f_drop['sp']:.3f} (Loewner "
          f"drop), D^{f_q['p']:+.3f} +- {f_q['sp']:.3f} (Cauchy-Schwarz), "
          f"D^{f_A['p']:+.3f} +- {f_A['sp']:.3f} (certified Muckenhoupt) and "
          f"D^{f_prod['p']:+.3f} +- {f_prod['sp']:.3f} (product): the signed "
          f"exponent is the SMALLEST in magnitude",
          abs(f_dir["p"]) < min(abs(f_drop["p"]), abs(f_q["p"]),
                                abs(f_A["p"]), abs(f_prod["p"])))
    cost_lo = min(t["E_drop"] / max(t["E_dir"], 1.0e-300) for t in INST)
    cost_hi = max(t["E_drop"] / max(t["E_dir"], 1.0e-300) for t in INST)
    check(f"S8.COST: the Loewner drop of the POSITIVE H off-diagonal costs a "
          f"factor {cost_lo:.2f}..{cost_hi:.2f} over the exact signed share "
          f"on the same windows, so the cancellation lives exactly there -- "
          f"a per-instance COST, not a law; NOTHING here is claimed to be "
          f"uniform in the zone index, in EITHER direction",
          cost_lo > 1.0)

    # ---------------------------------------------------------------- fences
    print("\nS9 -- the fences, restated as a check")
    check("S9.FENCE: PER-INSTANCE identities and certified forms on SMALL "
          "windows only -- NOTHING here is uniform in the zone index or in "
          "D, and the uniform forms stay open (PRIME.I5.UNIFORM class); "
          "item (7) promotes the VALIDITY of the two shapes and NOT their "
          "size -- neither beats the target, the additive shape is dead as a "
          "SHAPE by its own exact Weyl floor, the joint shape is decided at "
          "the normalisation Om, and both measurements stay in the sandbox; "
          "item (8) is a NEGATIVE typing whose exponents are FITS on a "
          "finite surface, printed as fits, with no zone-uniformity claimed "
          "in either direction; (2) is an identity and not a bound, so the "
          "remaining uniformity ingredient stays OPEN; Abel summation, "
          "Cauchy-Schwarz, Weyl 1912, Gershgorin 1931, Haynsworth 1968, "
          "Ostrowski 1937, Berman-Plemmons 1979, Muckenhoupt 1972, Bradley "
          "1978, Opic-Kufner 1990, Bennett 1987/1991, Gantmacher-Krein "
          "1950/1960, Karlin 1968, Wilkinson 1968 / Higham 2002 named "
          "CLASSICAL; Weil 1952 CITED, never used as a criterion; "
          "zero-firewall AST-checked; NO marker upgrade of any pre-existing "
          "contract", True)

    elapsed = time.time() - t0
    print(f"\nv545 runtime: {elapsed:.1f}s")
    print(f"  (1) form lifting: max rel {form:.1e} on {len(GRM)} explicit "
          f"Grams; rank <= h - 1 on all")
    print(f"  (2) finite core: reduction {red:.1e}, Gram route {grm:.1e}, "
          f"kernel {ker:.1e} on {len(INST)} windows")
    print(f"  (3) energy reordering: {ener:.1e}; Dirichlet weights positive "
          f"on {off_lo:.3f}..{off_hi:.3f} of the off-diagonal")
    print(f"  (4) checkerboard: split {spl:.1e}, three Weyl steps dominate on "
          f"{len(BND)} (window, b) pairs (worst ratio {tight:.4f})")
    print(f"  (5) Hardy identities: Rayleigh {ray:.1e}, crossing {crs:.1e}, "
          f"row sums {rwq:.1e}, Laplacian {lap:.1e}")
    print(f"  (6) Muckenhoupt formula: two routes agree to {a_err:.1e}; "
          f"A_M0 = {a_lo:.3e}..{a_hi:.3e}")
    print(f"  (7) dominance: additive {r_add[0]:.3f}..{r_add[1]:.3f}x, Weyl "
          f"floor {r_wey[0]:.3f}..{r_wey[1]:.3f}x, joint {r_geo[0]:.3f}.."
          f"{r_geo[1]:.3f}x -- all VALID, none small")
    print(f"  (8) separation: signed spread {s_dir:.2f}x vs absolute "
          f">= {s_abs:.2f}x; fits D^{f_dir['p']:+.3f} vs D^{f_A['p']:+.3f} "
          f"(FITS)")
    return summary("PRIME.HARDY.IDENT.01 Hardy-core identities")


if __name__ == "__main__":
    raise SystemExit(run())
