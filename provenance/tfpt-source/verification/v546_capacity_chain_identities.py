"""v546 -- PRIME.CAPCHAIN.IDENT.01: the capacity-chain identities of phase 2.
The IDENTITY-shaped, per-instance machine-checkable core of the capacity
cycle T142--T145 -- every statement RECOMPUTED here from scratch on small
exactly checkable frame-A windows (no citation of sandbox output).
Companion to PRIME.HARDY.IDENT.01 (v545), which supplies the finite core
(K, H) that the whole cycle runs on.

WHAT IS LOAD-BEARING HERE (and nothing else): identities, per-instance
theorems with CHECKED hypotheses, and per-window CERTIFIED inequalities.
NO fit, NO D-exponent, NO uniform-in-zone statement, NO level lemma --
the a-priori bound for the layer-cake constant (T145's L1) stays OPEN
and is neither assumed nor approached.  Each identity is checked as a
NUMERICAL RESIDUAL against a preregistered tolerance AND against at
least one MUTATION CONTROL that must fail loudly.

[E] (1) THE CAPACITY DECOMPOSITION (T142).  For the positive definite
    covering kernel K, with D the increment operator, J = D K D^T,
    x = K^{-1} 1 the equilibrium charge and cap = 1^T K^{-1} 1:
        K^{-1} = D^T J^{-1} D + x x^T / cap
    as a MATRIX identity, and under the congruence u = K^{1/2} v the
    Dirichlet half P = K^{1/2} D^T J^{-1} D K^{1/2} is an ORTHOGONAL
    PROJECTION (P^2 = P, lam_max(P) = 1, i.e. Omega = 1 EXACTLY) whose
    complement is the capacity rank-one, and P annihilates the
    equilibrium direction K^{-1/2} 1.
[E] (2) THE EXACT CAPACITY-RAYLEIGH IDENTITY (T143).  With
    H = diag(s) + D^T B D (B the signed crossing kernel) and d = D v:
        [ d^T (J^{-1} - B) d + (x^T v)^2 / cap - sum_k s_k v_k^2 ]
        / [ d^T J^{-1} d + (x^T v)^2 / cap ]
        == v^T (K^{-1} - H) v / v^T K^{-1} v          for EVERY v,
    its infimum is 1 - rho(W) (reproduced at the exact top eigenvector
    under the DECLARED 1/gap conditioning factor), and every assembled
    quotient at a random v stays >= 1 - rho(W) (the inf property).  On
    the constant vector the WHOLE denominator is the capacity term.
[E] (3) CHOLESKY NESTEDNESS (T144).  For the Green matrix R = E^{-1} of
    the whitened form, cap_E([a, a+j)) = 1^T [(R_AA)]^{-1} 1 equals the
    PREFIX SUM sum_{i<j} w_i^2 of ONE forward substitution
    w = L^{-1} 1, L the Cholesky factor of R_{[a,m),[a,m)} -- the whole
    interval fan of one anchor from one triangular solve, verified
    against independent Schur solves (exhaustively on one window) and
    monotone in b by construction.
[E] (4) THE WHITENING CERTIFICATE (T144).  kap_up = cert_lam_max(W),
    W = Lam^{-1/2} A_B Lam^{-1/2}, Lam = diag(A_B), is a completed-
    Cholesky UPPER bound with lam_max(W) <= kap_up <= the Gershgorin
    ceiling, and the chain direction it licenses,
    lam_min(E) / kap_up <= lam_min(A, A_B), holds on every window.
[E] (5) THE M4 SPLIT AND THE CERTIFIED CHAIN (T145).  The mass half of
    Maz'ya's step M4 rests on the pointwise theorem
    sum_k f_k^2 <= |psi|^2 for the dyadic truncations (exact, zero
    exceptions) and on rows with (E 1)_i >= 0 the mass comparison is an
    implication verified per instance; the measured full step
    sig_tot = sum_k E(f_k) / E(psi) < 1 on every window.  LICENCE 4 is
    stated with |R| and NOT with R^+, with the explicit witness
    R = [[1, -1/2], [-1/2, 1]], x = (1, -1) (x^T R x = 3 > 2 =
    |x|^T R^+ |x|) built in as a counterexample check.  The step chain
    theta <= q_dom <= q_cake <= num_lev <= Psi_abs G_dy ||psi||^2 is
    ordered on every window, and S1' is CERTIFIED per window as
        cert_lam_max(R) <= c_0 x Psi
    on BOTH routes (energy: c_0 = 12 sig_tot with Psi_pos; sign-free:
    c_0 = G_dy with Psi_abs), with the all-sets density bound carrying
    a CITED constant (Charikar 2000; Goldberg 1984) whose bracket is
    verified by exhaustive enumeration on a small block.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL windows.  Nothing
        here is uniform in the zone index or in D; every T142..T145
        D-exponent is a FIT and stays in the sandbox.
  (ii)  (5) certifies S1' PER WINDOW with a c_0 MEASURED at the
        minimiser's own layer cake.  The a-priori bound for that
        constant -- the LEVEL LEMMA L1 of T145 -- is NOT claimed, and
        no marker of any pre-existing contract moves.
  (iii) (1) and (2) are identities and not bounds; (3) computes the
        interval capacities exactly and says nothing about their size;
        (4) certifies the DENOMINATOR comparison only (T142's
        numerator obstruction is untouched).
  (iv)  sig_tot < 1 and the two chain inequalities of (5) are checked
        on THIS battery; they are window facts, not laws.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  The surrounding statement is the positivity of a
    Weil window form (Weil 1952, CITED, never used as a criterion) on a
    FINITE list of prime-power zones.  Everything here is an identity
    or a certified inequality PER INSTANCE; NOTHING here claims,
    assumes or approaches RH, and no statement about zeta zeros is
    made.  No zero data of any kind is read, generated or approximated
    -- an AST firewall enforces this.
  * Classics named CLASSICAL: Maz'ya 1985 (capacitary strong type; the
    truncation admissibility), Muckenhoupt 1972 (two-weight calculus),
    Fukushima-Oshima-Takeda 1994 (Beurling-Deny pair decomposition,
    Green form of a capacity), Miclo 1999 (the chain version),
    Charikar 2000 / Goldberg 1984 (max-density subgraph), Gershgorin
    1931, Cauchy-Schwarz, Wilkinson 1968 / Higham 2002 (completed
    Cholesky).  Maz'ya's strong-type HALF is NOT used as a theorem
    anywhere -- it is the thing the cycle transcribes.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] exact linear-algebra / interval-geometry identities at
rel < 1e-9 .. 1e-15 as stated, certified inequalities by completed
Cholesky with the direction in the name, each with a mutation control
that fails by >= 1e-3 relative.  Python; Wolfram-mirrored not required
(dense Cholesky / eigenvalue identities stay Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/conductance_profile_probe.py   (T142)
  experiments/tfpt-discovery/sharp_capacity_probe.py        (T143)
  experiments/tfpt-discovery/capacity_inequality_probe.py   (T144)
  experiments/tfpt-discovery/mazya_proof_probe.py           (T145)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, cholesky, eigh, eigvalsh, \
    solve_triangular

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in T128..T145
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
U_ROUND = 2.0 ** -53

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept (spread over the D range)
LEV_MAX = 30                 # dyadic levels kept above the floor level
N_RAND_V = 24                # random vectors per window for the (2) identity
N_RAND_X = 4                 # random vectors per window for LICENCE 4
G_ENUM = 12                  # block size of the exhaustive density bracket

# --- preregistered tolerances (declared BEFORE any number is computed) ---
TOL_DEC = 1.0e-10            # the capacity decomposition (relative)
TOL_PROJ = 1.0e-9            # projection / complement / annihilation
TOL_ASM = 1.0e-10            # the assembled Rayleigh identity (relative)
TOL_EIG = 1.0e-12            # eigenvalue reproduction, TIMES 1/gap (declared)
TOL_RED = 1.0e-8             # rho(W) two-route agreement (v545 convention)
TOL_NEST = 1.0e-9            # Cholesky-nestedness vs independent solve
TOL_ONE = 1.0e-11            # one-sided slack of ordered chain steps
TOL_CERT = 1.0e-9            # certified-inequality slack (relative)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard


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


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (frame-A code path of T128..T145)."""
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


# ------------------------------------- the reflection-odd sector (T106..T145)
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


# ------------------------------------ the lumped pair, whitening, finite core
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


def jacobi_whiten(A, A_B):
    """THE DENOMINATOR COMPARISON of T144.  With Lam = diag(A_B):
    E = Lam^{-1/2} A Lam^{-1/2}, W = Lam^{-1/2} A_B Lam^{-1/2} (diag(W) = 1),
    and lam_min(E) / kap_up <= lam_min(A, A_B) <= lam_min(E) / kap_lo."""
    Lam = np.diag(A_B).copy()
    if not (float(np.min(Lam)) > 0.0):
        return None
    sq = 1.0 / np.sqrt(Lam)
    E = sym(A * np.outer(sq, sq))
    W = sym(A_B * np.outer(sq, sq))
    kap_up = cert_lam_max(W, guess=ray_top(W))
    gersh_up = 1.0 + float(np.max((np.abs(W) - np.diag(np.diag(W))
                                   ).sum(axis=1)))
    return dict(E=E, W=W, kap_up=kap_up, gersh_up=gersh_up)


def edge_list(Dl, M):
    """The positive-edge system of L_Delta (er < et, weights w)."""
    h = Dl.shape[0]
    iu = np.triu_indices(h, 1)
    w = Dl[iu]
    keep = w > 0.0
    return dict(er=iu[0][keep], et=iu[1][keep], w=w[keep],
                n=int(np.count_nonzero(keep)))


def mixed_second_difference(G):
    """H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s} (T139/T140)."""
    return G[1:, 1:] - G[1:, :-1] - G[:-1, 1:] + G[:-1, :-1]


def cover_kernel_closed(er, et, w, h):
    """THE COVERING KERNEL K_rs = W([r ^ s, r v s]) by a 2-d prefix sum."""
    m = h - 1
    Wm = np.zeros((h + 1, h + 1))
    np.add.at(Wm, (er, et), w)
    F = np.cumsum(Wm, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((h + 1, 1))], axis=1)
    rr = np.arange(m)
    lo = np.minimum(rr[:, None], rr[None, :])
    hi = np.maximum(rr[:, None], rr[None, :])
    return sym(np.ascontiguousarray(F[lo, hi]))


def psd_sqrt(K, tol=1.0e-14):
    lam, V = eigh(sym(K))
    lmax = float(np.max(np.abs(lam))) if lam.size else 0.0
    keep = lam > tol * max(lmax, 1.0e-300)
    s = np.zeros_like(lam)
    s[keep] = np.sqrt(lam[keep])
    return sym((V * s[None, :]) @ V.T)


def abel_split(H):
    """H = diag(s) + L_N with s the row sums and N = -offdiag(H), exact."""
    s = H.sum(axis=1)
    N = -(H - np.diag(np.diag(H)))
    LN = np.diag(N.sum(axis=1)) - N
    return dict(s=s, N=N, LN=sym(LN),
                id_err=rel(H - (np.diag(s) + LN), H))


def diff_op(m):
    """THE INCREMENT OPERATOR (D u)_k = u_k - u_{k+1}, k = 0 .. m-2."""
    Dm = np.zeros((m - 1, m))
    idx = np.arange(m - 1)
    Dm[idx, idx] = 1.0
    Dm[idx, idx + 1] = -1.0
    return Dm


def crossing_kernel(N):
    """B_kl = sum_{r <= k ^ l, k v l < s} N_rs, signs of N kept, so that
    u^T L_N u = d^T B d with d = D u EXACTLY (T141/v545)."""
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
    return sym(np.ascontiguousarray(F[lo, hi]))


def hardy_laplacian(K):
    """J = D K D^T assembled entrywise (the endpoint Laplacian of T142)."""
    return sym(K[:-1, :-1] - K[:-1, 1:] - K[1:, :-1] + K[1:, 1:])


def set_capacity(R, idx):
    """cap_E(A) = 1^T [(E^{-1})_{AA}]^{-1} 1, the Schur / Green identity
    (Fukushima-Oshima-Takeda 1994, ch. 2; Maz'ya 1985).  R = E^{-1}."""
    Raa = sym(np.ascontiguousarray(R[np.ix_(idx, idx)]))
    fac = safe_cho(Raa)
    if fac is None:
        return float("nan")
    return float(cho_solve(fac, np.ones(idx.size), check_finite=False).sum())


# ----------------------- the layer cake and the density bound (T145 objects)
def layer_cake(psi):
    """THE DYADIC LAYER CAKE of |psi|: nested decreasing sets S_j with
    coefficients c_j > 0 and a floor level (the FULL set at 2^{k_bot}), so
    |psi| <= psi_t = sum_j c_j 1_{S_j} pointwise EXACTLY."""
    v = np.abs(np.asarray(psi, dtype=float))
    m = v.shape[0]
    vmax = float(np.max(v))
    if not (vmax > 0.0):
        return None
    k_top = int(math.floor(math.log2(vmax)))
    while 2.0 ** k_top >= vmax:
        k_top -= 1
    k_bot = k_top - LEV_MAX + 1
    order = np.argsort(-v, kind="stable")
    sizes = [m]
    coef = [2.0 ** k_bot]
    for k in range(k_bot, k_top + 1):
        t = 2.0 ** k
        n_k = int(np.count_nonzero(v > t))
        if n_k <= 0:
            continue
        sizes.append(n_k)
        coef.append(t)
    Kn = len(sizes)
    Ind = np.zeros((Kn, m))
    for j in range(Kn):
        Ind[j, order[:sizes[j]]] = 1.0
    cv = np.array(coef, dtype=float)
    nv = np.array(sizes, dtype=float)
    psi_t = Ind.T @ cv
    jj = np.arange(Kn)
    mn = np.minimum.outer(jj, jj)          # the LARGER set has the SMALLER index
    return dict(K=Kn, Ind=Ind, c=cv, n=nv, psi_t=psi_t, v=v, mn=mn,
                k_top=k_top, k_bot=k_bot,
                dom_lo=float(np.min(psi_t - v)))


def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000) for the max-density subgraph
    of a NONNEGATIVE symmetric weight matrix with zero diagonal.  The value is
    ATTAINED (a lower bound on the optimum) and opt <= 2 x greedy is CITED."""
    m = Wp.shape[0]
    deg = Wp.sum(axis=1).astype(float)
    tot = 0.5 * float(deg.sum())
    alive = np.ones(m, dtype=bool)
    n_alive = m
    best = tot / m
    while n_alive > 1:
        d = np.where(alive, deg, np.inf)
        j = int(np.argmin(d))
        tot -= float(deg[j])
        alive[j] = False
        deg = deg - Wp[j]
        deg[j] = 0.0
        n_alive -= 1
        best = max(best, tot / n_alive)
    return float(best)


def density_all_upper(R):
    """UPPER bound for sup_A (1^T R^+_AA 1) / |A| over ALL 2^m sets:
    max_i R_ii + min(4 x greedy, 2 x cert_lam_max(R_offplus)) via Charikar's
    cited constant (Charikar 2000; Goldberg 1984) or the certified spectrum.
    DIRECTION: an UPPER bound, the direction the chain consumes."""
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    gr = greedy_density(Rp)
    dg_max = float(np.max(np.diag(R)))
    psi_char = dg_max + 4.0 * gr
    psi_spec = dg_max + cert_lam_max(Rp, guess=ray_top(Rp))
    cands = [x for x in (psi_char, psi_spec) if np.isfinite(x)]
    return dict(up=(min(cands) if cands else float("nan")),
                char=psi_char, greedy=gr, dg_max=dg_max)


def pair_parts(X):
    """The Beurling-Deny shape (Fukushima-Oshima-Takeda 1994, ch. 1):
    f^T X f = sum_{i<j} (-X_ij)(f_i - f_j)^2 + sum_i (X 1)_i f_i^2."""
    off = X - np.diag(np.diag(X))
    return dict(off=off, s=off.sum(axis=1), r=X.sum(axis=1))


def mass_part(pp, f):
    return float((f * f) @ pp["r"])


def dyadic_truncations(v, k_bot, k_top):
    """f_k = min(max(|psi| - 2^k, 0), 2^k); sum_k f_k = |psi| to the floor."""
    out = []
    for k in range(k_bot, k_top + 1):
        t = 2.0 ** k
        out.append(np.minimum(np.maximum(v - t, 0.0), t))
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


def build_instance(k, D, M, h, rng):
    """One window, end to end: the odd section, its lumped pair, the finite
    core (K, H), the whitened pair (E, W) with its Green matrix R and
    minimiser psi, and every derived object of the five items."""
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
    if ed["n"] < 8:
        return None
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return None
    if not (gap_ex > 0.0):
        return None
    H = mixed_second_difference(G)
    m = H.shape[0]
    if m < 8:
        return None
    K = cover_kernel_closed(ed["er"], ed["et"], ed["w"], h)

    row = dict(n=NN_ALL[k], h=h, m=m, D=D, n_e=ed["n"], gap_ex=gap_ex,
               rho_ex=1.0 - gap_ex)

    # ---- (1) + (2): need K positive definite ------------------------------
    lmK = cert_lam_min_pos(K)
    row["k_pd"] = bool(np.isfinite(lmK) and lmK > 0.0)
    if row["k_pd"]:
        facK = safe_cho(K)
        Kinv = sym(cho_solve(facK, np.eye(m), check_finite=False))
        one = np.ones(m)
        x = Kinv @ one
        cap = float(one @ x)
        Dop = diff_op(m)
        J = hardy_laplacian(K)
        row["j_asm_err"] = rel(J - Dop @ K @ Dop.T, J)
        facJ = safe_cho(J)
        if facJ is None:
            row["k_pd"] = False
        else:
            Jinv = sym(cho_solve(facJ, np.eye(m - 1), check_finite=False))
            dir_part = Dop.T @ Jinv @ Dop
            rk1 = np.outer(x, x) / cap
            row["dec_err"] = rel(Kinv - (dir_part + rk1), Kinv)
            row["dec_ctrl"] = rel(Kinv - dir_part, Kinv)
            row["cap_ctrl"] = rel(Kinv - (dir_part + rk1 / 1.01), Kinv)
            Kh = psd_sqrt(K)
            P = sym(Kh @ dir_part @ Kh)
            row["proj_err"] = rel(P @ P - P, P)
            evP = eigvalsh(P)
            row["omega"] = float(evP[-1])
            Q1 = sym(Kh @ rk1 @ Kh)
            row["compl_err"] = rel(P + Q1 - np.eye(m), np.eye(m))
            kx = Kh @ x
            row["annih"] = (float(np.linalg.norm(P @ kx))
                            / max(float(np.linalg.norm(kx)), 1.0e-300))
            # ---- (2) the capacity-Rayleigh identity ------------------------
            ab = abel_split(H)
            B = crossing_kernel(ab["N"])
            row["ab_err"] = ab["id_err"]
            row["cross_err"] = rel(ab["LN"] - Dop.T @ B @ Dop, ab["LN"])
            Babs = crossing_kernel(np.abs(ab["N"]))
            row["cross_ctrl"] = rel(ab["LN"] - Dop.T @ Babs @ Dop, ab["LN"])
            Ycore = sym(Kh @ H @ Kh)
            evc, Uc = eigh(Ycore)
            rho_c = float(evc[-1])
            row["rho_c"] = rho_c
            row["red_err"] = abs(rho_c - row["rho_ex"]) / max(row["rho_ex"],
                                                              1.0e-300)
            gap_c = 1.0 - rho_c
            row["gap_c"] = gap_c
            s = ab["s"]

            def quo(v):
                d = Dop @ v
                xv = float(x @ v)
                den = float(d @ (Jinv @ d)) + xv * xv / cap
                num = (float(d @ ((Jinv - B) @ d)) + xv * xv / cap
                       - float((v * v) @ s))
                return num, den

            asm_err = 0.0
            inf_slack = float("inf")
            KmH = Kinv - H
            for _ in range(N_RAND_V):
                v = rng.standard_normal(m)
                num, den = quo(v)
                dnum = float(v @ (KmH @ v))
                dden = float(v @ (Kinv @ v))
                sc = max(abs(dden), abs(dnum), 1.0e-300)
                asm_err = max(asm_err, abs(num - dnum) / sc,
                              abs(den - dden) / sc)
                inf_slack = min(inf_slack, (num / den) / gap_c)
            row["asm_err"] = asm_err
            row["inf_slack"] = inf_slack
            vstar = Kh @ Uc[:, -1]
            num_s, den_s = quo(vstar)
            row["eig_err"] = abs(num_s / den_s - gap_c) / max(gap_c, 1.0e-300)
            # the constant vector: the WHOLE denominator is the capacity term
            num_1, den_1 = quo(one)
            row["const_den"] = abs(den_1 - cap) / cap
            row["const_ctrl"] = abs(den_1 - float((Dop @ one)
                                                  @ (Jinv @ (Dop @ one)))) / cap

    # ---- (3) + (4) + (5): the whitened pair -------------------------------
    jw = jacobi_whiten(A, A_B)
    if jw is None:
        return None
    E, W = jw["E"], jw["W"]
    row["kap_up"], row["gersh_up"] = jw["kap_up"], jw["gersh_up"]
    row["lam_W"] = float(eigvalsh(W)[-1])
    row["kap_refuse"] = safe_cho(0.995 * row["lam_W"] * np.eye(h) - W) is None
    lam_lo, Vlo = eigh(E, subset_by_index=[0, 0])
    row["lam_E"] = float(lam_lo[0])
    psi = Vlo[:, 0].copy()
    facE = safe_cho(E)
    if facE is None:
        return None
    R = sym(cho_solve(facE, np.eye(h), check_finite=False))

    # (3) Cholesky nestedness of the interval capacities
    nest_err = 0.0
    n_pref = 0
    for a in (0, h // 3, (2 * h) // 3):
        blk = sym(np.ascontiguousarray(R[a:, a:]))
        L = cholesky(blk, lower=True, check_finite=False)
        wf = solve_triangular(L, np.ones(h - a), lower=True,
                              check_finite=False)
        pref = np.cumsum(wf * wf)
        n_pref += pref.size
        row.setdefault("pref", {})[a] = pref
        for j in np.unique(np.linspace(1, h - a, 5).astype(int)):
            cap_ind = set_capacity(R, np.arange(a, a + j))
            nest_err = max(nest_err, abs(pref[j - 1] - cap_ind)
                           / max(abs(cap_ind), 1.0e-300))
    row["nest_err"] = nest_err
    row["n_pref"] = n_pref
    # the reversal control: suffix capacities are NOT the prefix capacities
    blkr = sym(np.ascontiguousarray(R[::-1, ::-1]))
    Lr = cholesky(blkr, lower=True, check_finite=False)
    wr = solve_triangular(Lr, np.ones(h), lower=True, check_finite=False)
    prefr = np.cumsum(wr * wr)
    pj = row["pref"][0]
    row["rev_ctrl"] = float(np.max(np.abs(prefr[:-1] - pj[:-1])
                                   / np.maximum(np.abs(pj[:-1]), 1.0e-300)))

    # (5) the M4 split and the certified chain
    lc = layer_cake(psi)
    if lc is None:
        return None
    v, Ind, cv, nv, mn = lc["v"], lc["Ind"], lc["c"], lc["n"], lc["mn"]
    row["cake_dom"] = lc["dom_lo"]
    tr = dyadic_truncations(v, lc["k_bot"], lc["k_top"])
    f_sum = np.zeros_like(v)
    f2_sum = np.zeros_like(v)
    s_tot = 0.0
    m_tot = 0.0
    pp = pair_parts(E)
    for fk in tr:
        f_sum += fk
        f2_sum += fk * fk
        s_tot += float(fk @ (E @ fk))
        m_tot += mass_part(pp, fk)
    row["cake_id"] = rel(f_sum - v, v)
    row["ptw_slack"] = float(np.min(v * v - f2_sum))
    pos = pp["r"] >= 0.0
    lhs_pos = float(np.sum(np.where(pos, pp["r"] * f2_sum, 0.0)))
    rhs_pos = float(np.sum(np.where(pos, pp["r"] * v * v, 0.0)))
    row["mass_impl"] = lhs_pos <= rhs_pos * (1.0 + 1.0e-12)
    E_v = float(v @ (E @ v))
    row["sig_tot"] = s_tot / max(E_v, 1.0e-300)
    row["sig_mass"] = m_tot / max(mass_part(pp, v), 1.0e-300)
    ks = np.arange(lc["k_bot"], lc["k_top"] + 1)
    n_lev = np.array([float(np.count_nonzero(v > 2.0 ** kk)) for kk in ks])
    nrm2 = float(v @ v)
    row["m1_ratio"] = 3.0 * float((4.0 ** ks.astype(float)) @ n_lev) / nrm2
    Rabs = np.abs(R)
    theta = float(psi @ (R @ psi))
    q_dom = float(v @ (Rabs @ v))
    QM = Ind @ (Rabs @ Ind.T)
    qd = np.diag(QM).copy()
    q_cake = float(cv @ (QM @ cv))
    num_lev = float(cv @ (qd[mn] @ cv))
    G_dy = float(cv @ (nv[mn] @ cv)) / nrm2
    row.update(theta=theta, q_dom=q_dom, q_cake=q_cake, num_lev=num_lev,
               G_dy=G_dy)
    row["psi_abs"] = density_all_upper(Rabs)["up"]
    row["psi_pos"] = density_all_upper(R)["up"]
    row["cert_R"] = cert_lam_max(R, guess=ray_top(R))
    row["c0_energy"] = 12.0 * row["sig_tot"]
    row["c0_free"] = G_dy
    row["lic4"] = True
    for _ in range(N_RAND_X):
        xr = rng.standard_normal(h)
        if (float(xr @ (R @ xr))
                > float(np.abs(xr) @ (Rabs @ np.abs(xr))) * (1.0 + 1.0e-12)):
            row["lic4"] = False
    row["R"] = R
    return row


def exhaustive_density(S):
    """The EXACT density sup over all nonempty subsets of a small block, and
    the exact EDGE-density optimum of its nonnegative off-diagonal part --
    affordable only because the block is small, which is the point."""
    g = S.shape[0]
    Sp = np.maximum(S, 0.0)
    np.fill_diagonal(Sp, 0.0)
    best_all = -float("inf")
    best_edge = -float("inf")
    idx = np.arange(g)
    for mask in range(1, 2 ** g):
        sel = idx[np.array([(mask >> i) & 1 for i in range(g)], dtype=bool)]
        o = np.ones(sel.size)
        best_all = max(best_all,
                       float(o @ S[np.ix_(sel, sel)] @ o) / sel.size)
        best_edge = max(best_edge,
                        0.5 * float(o @ Sp[np.ix_(sel, sel)] @ o) / sel.size)
    return best_all, best_edge


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(5462026)
    print("=" * 72)
    print("v546  PRIME.CAPCHAIN.IDENT.01 -- capacity-chain identities "
          "(T142-T145)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered tolerances")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    for (k, D, M, h) in build_windows():
        row = build_instance(k, D, M, h, rng)
        if row is not None:
            INST.append(row)
    PD = [t for t in INST if t["k_pd"]]
    check(f"S0.INST: {len(INST)} frame-A windows built with a positive "
          f"definite whitened pair; the covering kernel is positive definite "
          f"on {len(PD)} of them (items (1)-(2) run there)",
          len(INST) >= 6 and len(PD) >= 6)
    h_max = max(t["h"] for t in INST)
    d_lo = min(t["D"] for t in INST)
    d_hi = max(t["D"] for t in INST)
    check(f"S0.CAP: every inverted / factorised / diagonalised matrix <= "
          f"{H_CAP} (max h = {h_max}); the surface spans D = {d_lo:.3e} .. "
          f"{d_hi:.3e}", h_max <= H_CAP)
    for t in INST:
        print(f"    n={t['n']:>7d} D={t['D']:.4e} h={t['h']:>4d} "
              f"m={t['m']:>4d} n_e={t['n_e']:>5d} rho(W)={t['rho_ex']:.6f} "
              f"K_pd={int(t['k_pd'])}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the capacity decomposition "
          "K^-1 = D^T J^-1 D + x x^T / cap  (T142)")
    dec = max(t["dec_err"] for t in PD)
    jasm = max(t["j_asm_err"] for t in PD)
    check(f"S1.ID: K^-1 == D^T J^-1 D + x x^T / cap on all {len(PD)} windows "
          f"(max rel {dec:.2e} < {TOL_DEC:.0e}), with J = D K D^T assembled "
          f"entrywise (max rel {jasm:.2e}) -- the optimal Hardy weight is "
          f"geometry, not a guess", dec < TOL_DEC and jasm < TOL_DEC)
    pj = max(t["proj_err"] for t in PD)
    om_lo = min(t["omega"] for t in PD)
    om_hi = max(t["omega"] for t in PD)
    check(f"S1.PROJ: under the congruence u = K^(1/2) v the Dirichlet half is "
          f"an ORTHOGONAL PROJECTION: P^2 == P (max rel {pj:.2e}) and "
          f"Omega = lam_max(P) = {om_lo:.12f}..{om_hi:.12f} == 1 EXACTLY -- "
          f"the T142 normalisation, where T141 had guessed 20.7..2724",
          pj < TOL_PROJ and abs(om_lo - 1.0) < TOL_PROJ
          and abs(om_hi - 1.0) < TOL_PROJ)
    cmpl = max(t["compl_err"] for t in PD)
    ann = max(t["annih"] for t in PD)
    check(f"S1.SPLIT: the complement I - P IS the capacity rank-one (max rel "
          f"{cmpl:.2e}) and P annihilates the equilibrium direction "
          f"K^(-1/2) 1 (max {ann:.2e}) -- the two halves are complementary "
          f"orthogonal projections", cmpl < TOL_PROJ and ann < TOL_PROJ)
    ctl1 = min(t["dec_ctrl"] for t in PD)
    ctl2 = min(t["cap_ctrl"] for t in PD)
    check(f"S1.CTRL: dropping the capacity rank-one breaks the identity on "
          f"every window (min rel {ctl1:.2e} > {BAR_CTRL:.0e}); a 1% "
          f"perturbation of cap breaks it too (min rel {ctl2:.2e})",
          ctl1 > BAR_CTRL and ctl2 > BAR_CTRL)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the exact capacity-Rayleigh identity for 1 - rho(W)  "
          "(T143)")
    crs = max(t["cross_err"] for t in PD)
    abe = max(t["ab_err"] for t in PD)
    red = max(t["red_err"] for t in PD)
    check(f"S2.CROSS: the two ingredients recomputed, not cited: "
          f"H == diag(s) + L_N (max rel {abe:.2e}) and L_N == D^T B D with "
          f"the SIGNED crossing kernel (max rel {crs:.2e}); "
          f"rho(W) = lam_max(K^(1/2) H K^(1/2)) agrees with "
          f"1 - lam_min(A, A_B) to {red:.2e} (bar {TOL_RED:.0e})",
          crs < TOL_DEC and abe < TOL_DEC and red < TOL_RED)
    asm = max(t["asm_err"] for t in PD)
    check(f"S2.ASSEMBLE: the assembled numerator and denominator equal "
          f"v^T (K^-1 - H) v and v^T K^-1 v on {N_RAND_V} random vectors per "
          f"window (max rel {asm:.2e} < {TOL_ASM:.0e}) -- the T143 form is an "
          f"IDENTITY, no inequality taken", asm < TOL_ASM)
    eig_bar = max(TOL_EIG / t["gap_c"] for t in PD)
    eig = max(t["eig_err"] for t in PD)
    check(f"S2.EIG: at the exact top eigenvector the assembled quotient "
          f"reproduces 1 - rho(W) to {eig:.2e} relative, inside the DECLARED "
          f"1/gap conditioning bar {eig_bar:.2e} (the numerator is a "
          f"cancellation of O(1) terms down to the gap)", eig < eig_bar)
    infs = min(t["inf_slack"] for t in PD)
    cden = max(t["const_den"] for t in PD)
    check(f"S2.INF: every assembled quotient at a random vector stays >= "
          f"1 - rho(W) (min slack {infs:.6f} >= 1), and on the CONSTANT "
          f"vector the whole denominator is the capacity term (den == cap to "
          f"{cden:.2e}) -- the rank-one completes the decomposition exactly "
          f"where D vanishes", infs >= 1.0 - 1.0e-8 and cden < TOL_ASM)
    ctl3 = min(t["const_ctrl"] for t in PD)
    ctl4 = min(t["cross_ctrl"] for t in PD)
    check(f"S2.CTRL: dropping the capacity term empties the denominator at "
          f"the constant vector (min rel {ctl3:.2e} > {BAR_CTRL:.0e}, in fact "
          f"= 1), and the crossing kernel of |N| does NOT reproduce L_N (min "
          f"rel {ctl4:.2e}) -- the signs are load-bearing",
          ctl3 > BAR_CTRL and ctl4 > BAR_CTRL)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) Cholesky nestedness: interval capacities as prefix "
          "sums  (T144)")
    nst = max(t["nest_err"] for t in INST)
    npref = sum(t["n_pref"] for t in INST)
    check(f"S3.NEST: cap_E([a, a+j)) == prefix sum of the squared forward-"
          f"substitution entries of ONE triangular solve, verified against "
          f"independent Schur solves at sampled (a, j) on all {len(INST)} "
          f"windows, 3 anchors each, {npref} interval capacities from "
          f"{3 * len(INST)} solves (max rel {nst:.2e} < {TOL_NEST:.0e})",
          nst < TOL_NEST)
    mid = sorted(INST, key=lambda t: t["h"])[len(INST) // 2]
    ex_h = int(mid["h"])
    pref0 = mid["pref"][0]
    ex_err = 0.0
    for j in range(1, ex_h + 1):
        cap_ind = set_capacity(mid["R"], np.arange(j))
        ex_err = max(ex_err, abs(pref0[j - 1] - cap_ind)
                     / max(abs(cap_ind), 1.0e-300))
    mono_ok = bool(np.all(np.diff(pref0) >= -1.0e-300))
    check(f"S3.ALL: on the median window (h = {ex_h}) EVERY prefix "
          f"j = 1..{ex_h} of anchor 0 is verified against an independent "
          f"solve (max rel {ex_err:.2e} < {TOL_NEST:.0e}), and the interval "
          f"capacities are monotone in b BY CONSTRUCTION (a prefix sum of "
          f"squares) -- the whole interval fan of one anchor is one "
          f"triangular solve", ex_err < TOL_NEST and mono_ok)
    rev = min(t["rev_ctrl"] for t in INST)
    check(f"S3.CTRL: reversing the ordering computes SUFFIX capacities, which "
          f"differ from the prefix capacities on every window (min max-rel "
          f"deviation {rev:.2e} > {BAR_CTRL:.0e}) -- the prefix property is "
          f"the NESTEDNESS of the ordering, not generic algebra",
          rev > BAR_CTRL)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the whitening certificate kap_up, direction-correct  "
          "(T144)")
    kap_ok = all(t["lam_W"] <= t["kap_up"] <= t["gersh_up"] * (1.0 + 1.0e-12)
                 for t in INST)
    k_lo = min(t["kap_up"] for t in INST)
    k_hi = max(t["kap_up"] for t in INST)
    g_hi = max(t["gersh_up"] for t in INST)
    check(f"S4.KUP: lam_max(W) <= kap_up (completed Cholesky) <= the "
          f"Gershgorin ceiling on every window, kap_up = {k_lo:.4f}.."
          f"{k_hi:.4f} against Gershgorin <= {g_hi:.4f} (Gershgorin 1931) -- "
          f"the certificate is strictly sharper than the ceiling that "
          f"licenses it", kap_ok)
    dir_ok = all(t["lam_E"] / t["kap_up"] <= t["gap_ex"] * (1.0 + TOL_CERT)
                 for t in INST)
    check(f"S4.DIR: the licensed chain direction lam_min(E) / kap_up <= "
          f"lam_min(A, A_B) holds on every window -- a DENOMINATOR "
          f"comparison, which T142's numerator obstruction does not touch",
          dir_ok)
    refuse = all(t["kap_refuse"] for t in INST)
    check(f"S4.CTRL: at the shrunken shift 0.995 lam_max(W) the Cholesky "
          f"REFUSES on every window -- the certificate cannot be talked "
          f"below the spectrum", refuse)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the M4 split and the certified chain "
          "cert_lam_max(R) <= c_0 Psi  (T145)")
    cid = max(t["cake_id"] for t in INST)
    cdom = min(t["cake_dom"] for t in INST)
    check(f"S5.CAKE: the dyadic layer cake dominates pointwise, psi_t >= "
          f"|psi| (min slack {cdom:.2e} >= 0), and the truncations telescope, "
          f"sum_k f_k == |psi| down to the declared floor (max rel {cid:.2e})",
          cdom >= -1.0e-14 and cid < 1.0e-8)
    ptw = min(t["ptw_slack"] for t in INST)
    impl = all(t["mass_impl"] for t in INST)
    sg_lo = min(t["sig_tot"] for t in INST)
    sg_hi = max(t["sig_tot"] for t in INST)
    sm_hi = max(t["sig_mass"] for t in INST)
    m1_lo = min(t["m1_ratio"] for t in INST)
    check(f"S5.MASS: the mass half of M4 -- sum_k f_k^2 <= psi^2 POINTWISE "
          f"(min slack {ptw:.2e} >= 0, a theorem for nonnegative truncations "
          f"summing to |psi|), the row-wise implication on rows with "
          f"(E 1)_i >= 0 holds on every window, the measured mass ratio "
          f"{sm_hi:.4f} <= 1, and the FULL step sig_tot = sum_k E(f_k) / "
          f"E(psi) = {sg_lo:.4f}..{sg_hi:.4f} < 1 on every window although "
          f"the Markov hypothesis is absent; M1 holds in the direction used "
          f"(3 sum 4^k |A_k| / ||psi||^2 = {m1_lo:.4f} >= 1)",
          ptw >= -1.0e-14 and impl and sm_hi <= 1.0 + 1.0e-12
          and sg_hi < 1.0 and m1_lo >= 1.0)
    lic = all(t["lic4"] for t in INST)
    Wit = np.array([[1.0, -0.5], [-0.5, 1.0]])
    wv = np.array([1.0, -1.0])
    wit_lhs = float(wv @ (Wit @ wv))
    wit_rhs = float(np.abs(wv) @ (np.maximum(Wit, 0.0) @ np.abs(wv)))
    check(f"S5.LIC4: x^T R x <= |x|^T |R| |x| on {N_RAND_X} random vectors "
          f"per window (LICENCE 4, no hypothesis), AND the R^+ version is "
          f"FALSE on the built-in witness R = [[1,-1/2],[-1/2,1]], "
          f"x = (1,-1): {wit_lhs:.1f} > {wit_rhs:.1f} -- the direction error "
          f"this module is fenced against", lic and wit_lhs > wit_rhs)
    step_ok = all(
        t["theta"] <= t["q_dom"] * (1.0 + TOL_ONE)
        and t["q_dom"] <= t["q_cake"] * (1.0 + TOL_ONE)
        and t["q_cake"] <= t["num_lev"] * (1.0 + TOL_ONE)
        and t["num_lev"] <= t["psi_abs"] * t["G_dy"] * (1.0 + TOL_ONE)
        for t in INST)
    check(f"S5.STEPS: the sign-free replacement chain is ORDERED on every "
          f"window: psi^T R psi <= |psi|^T |R| |psi| <= psi_t^T |R| psi_t <= "
          f"sum c_j c_l q_min <= Psi_abs G_dy ||psi||^2 (one-sided slack "
          f"{TOL_ONE:.0e}) -- M4'a entrywise, M4'b cake, M4'c nested sets, "
          f"then the density bound", step_ok)
    cert_ok = all(
        t["cert_R"] <= t["c0_energy"] * t["psi_pos"] * (1.0 + TOL_CERT)
        and t["cert_R"] <= t["c0_free"] * t["psi_abs"] * (1.0 + TOL_CERT)
        for t in INST)
    ce_lo = min(t["c0_energy"] for t in INST)
    ce_hi = max(t["c0_energy"] for t in INST)
    cf_lo = min(t["c0_free"] for t in INST)
    cf_hi = max(t["c0_free"] for t in INST)
    cb_lo = min(min(t["c0_energy"], t["c0_free"]) for t in INST)
    cb_hi = max(min(t["c0_energy"], t["c0_free"]) for t in INST)
    check(f"S5.CERT: S1' as a certified window inequality on BOTH routes and "
          f"all {len(INST)} windows: cert_lam_max(R) <= 12 sig_tot x Psi_pos "
          f"(energy, c_0 = {ce_lo:.4f}..{ce_hi:.4f}) and cert_lam_max(R) <= "
          f"G_dy x Psi_abs (sign-free, c_0 = {cf_lo:.4f}..{cf_hi:.4f}); the "
          f"better route gives c_0 = {cb_lo:.4f}..{cb_hi:.4f} against the "
          f"classical Dirichlet value 4 (Maz'ya 1985) -- the constant is "
          f"EXPLICIT and MEASURED at the minimiser, and no a-priori bound "
          f"for it is claimed (T145's L1 stays OPEN)", cert_ok)
    small = min(INST, key=lambda t: t["h"])
    Sblk = np.abs(small["R"])[:G_ENUM, :G_ENUM]
    ex_all, ex_edge = exhaustive_density(Sblk)
    du = density_all_upper(Sblk)
    gr_ok = (du["greedy"] <= ex_edge * (1.0 + 1.0e-12)
             and ex_edge <= 2.0 * du["greedy"] * (1.0 + 1.0e-12))
    up_ok = ex_all <= du["up"] * (1.0 + 1.0e-12)
    check(f"S5.ENUM: on the leading {G_ENUM} x {G_ENUM} block of |R| "
          f"(smallest window) the EXHAUSTIVE optimum over all "
          f"{2 ** G_ENUM - 1} nonempty subsets is bracketed: greedy "
          f"{du['greedy']:.4f} <= exhaustive edge optimum {ex_edge:.4f} <= "
          f"2 x greedy (Charikar 2000, the CITED constant; Goldberg 1984 for "
          f"the exact flow version), and the all-sets bound dominates the "
          f"exhaustive density sup ({du['up']:.4f} >= {ex_all:.4f})",
          gr_ok and up_ok)
    ctl5 = all(t["cert_R"] > BAR_CTRL * min(t["c0_energy"], t["c0_free"])
               * min(t["psi_pos"], t["psi_abs"]) for t in INST)
    check(f"S5.CTRL: scaling c_0 by {BAR_CTRL:.0e} breaks the certificate on "
          f"every window -- the chain inequality is not vacuous slack",
          ctl5)

    # ---------------------------------------------------------------- fences
    print("\nS6 -- the fences, restated as a check")
    check("S6.FENCE: PER-INSTANCE identities and certified inequalities on "
          "SMALL windows only -- nothing here is uniform in the zone index "
          "or in D, every T142..T145 exponent is a FIT and stays in the "
          "sandbox; the c_0 of item (5) is MEASURED at the minimiser's layer "
          "cake and the a-priori LEVEL LEMMA (T145 L1) stays OPEN, unclaimed "
          "and unapproached; Maz'ya 1985 / Muckenhoupt 1972 / "
          "Fukushima-Oshima-Takeda 1994 / Miclo 1999 / Charikar 2000 / "
          "Goldberg 1984 / Gershgorin 1931 / Wilkinson 1968 / Higham 2002 "
          "named CLASSICAL, and Maz'ya's strong-type half is NOT used as a "
          "theorem anywhere; Weil 1952 CITED, never used as a criterion; "
          "zero-firewall AST-checked; NO marker upgrade of any pre-existing "
          "contract", True)

    elapsed = time.time() - t0
    print(f"\nv546 runtime: {elapsed:.1f}s")
    print(f"  (1) capacity decomposition: max rel {dec:.1e}; Omega - 1 <= "
          f"{max(abs(om_lo - 1.0), abs(om_hi - 1.0)):.1e} on {len(PD)} windows")
    print(f"  (2) capacity-Rayleigh: assembly {asm:.1e}; eigenvalue {eig:.1e} "
          f"(declared bar {eig_bar:.1e}); inf slack >= {infs:.6f}")
    print(f"  (3) nestedness: {npref} interval capacities from "
          f"{3 * len(INST)} solves, max rel {nst:.1e}; exhaustive window "
          f"{ex_err:.1e}")
    print(f"  (4) whitening: kap_up = {k_lo:.4f}..{k_hi:.4f} vs Gershgorin "
          f"<= {g_hi:.4f}; refusal at 0.995 lam_max on all")
    print(f"  (5) M4 split: sig_tot = {sg_lo:.4f}..{sg_hi:.4f} < 1; chain "
          f"c_0 = {cb_lo:.4f}..{cb_hi:.4f} certified on {len(INST)} windows")
    return summary("PRIME.CAPCHAIN.IDENT.01 capacity-chain identities")


if __name__ == "__main__":
    raise SystemExit(run())
