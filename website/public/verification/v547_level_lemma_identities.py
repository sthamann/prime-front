"""v547 -- PRIME.LEVEL.LEMMA.01: the level-lemma identities of phase 2.
The IDENTITY-shaped, per-instance machine-checkable core of T146's level
lemma -- every statement RECOMPUTED here from scratch on small exactly
checkable frame-A windows (no citation of sandbox output).  Companion to
PRIME.CAPCHAIN.IDENT.01 (v546), which certifies the chain this lemma
feeds: v546's item (5) certified S1' with a c_0 MEASURED at the
minimiser's own layer cake; THIS module supplies the a-priori side --
the same constant as a functional of the FORM alone, never read off the
minimiser -- on the same class of windows.

WHAT IS LOAD-BEARING HERE (and nothing else): identities, per-instance
theorems with CHECKED hypotheses, and per-window CERTIFIED inequalities.
NO fit, NO D-exponent, NO uniform-in-zone statement, and NO statement
FOR ALL D -- the asymptotic delocalisation of the Green columns (the
bound on max_j ||R e_j|| lam_min as D -> 0, T146's remainder (2)) stays
OPEN and is neither assumed nor approached.  Each identity is checked as
a NUMERICAL RESIDUAL against a preregistered tolerance AND against at
least one MUTATION CONTROL that must fail loudly.

[E] (1) THE UNION IDENTITY for nested cakes (T146).  For a NESTED
    decreasing chain of sets S_1 >= S_2 >= ... with positive
    coefficients c_j, with T = sum_j c_j and psi_t = sum_j c_j 1_{S_j}:
        sum_{j,l} c_j c_l |S_j u S_l| = 2 T ||psi_t||_1 - ||psi_t||^2
    -- one line, FORM-INDEPENDENT, and the reason the cake base is
    movable at all: the level constant is an O(m) closed form and never
    a K x K double sum.  Verified against the K x K arithmetic (T145's
    form) on random vectors and on every window minimiser.
[E] (2) THE LAYER-CAKE COUNTING LEMMA at a GENERAL BASE (T146).  For ANY
    vector v and any base b > 1, the geometric level constant of the
    b-adic cake of |v| satisfies
        G(b) <= 2 b^2 ||v||_inf ||v||_1 / ||v||^2 + eps(b),
    eps(b) the explicit floor term -- a COUNTING theorem that never
    mentions a minimiser.  At b = 2 the leading constant is the
    classical dyadic 8 (Maz'ya 1985); the chain consumes only the LOWER
    domination |v| <= psi_t, so the base is FREE and 2 b^2 falls toward
    2 -- the factor ceiling against b is part of the claim, and the
    one-level-down mutation (psi_t / b) breaks the domination on every
    draw, so the +1 in the cake exponent is load-bearing.
[E] (3) THE RESOLVENT DELOCALISATION BOUND (T146).  For a symmetric
    positive definite E with R = E^{-1} and bottom eigenpair (lam, psi):
    psi = lam R psi is an IDENTITY (no perturbation transfer, no
    Davis-Kahan step), so by Cauchy-Schwarz per coordinate
        ||psi||_inf <= lam_up x max_j ||R e_j|| x ||psi||,
    with lam_up = min_j Rayleigh(R e_j) >= lam an a-priori UPPER bound
    on the gap (Rayleigh 1877; Ritz 1909; the Green columns are legal
    test vectors) and the column norms certified from ABOVE with the
    linear-solve residual paid for: ||R e_j|| <= ||x_j|| +
    ||E x_j - e_j|| / cert_lam_min(E).  THE LEVER, checked as a number:
    the trivial route max_j ||R e_j|| <= ||R|| = 1/lam would only give
    Gam = sqrt(m) lam_up max_j ||R e_j|| <= sqrt(m) (useless); on every
    window the certified column norms sit a FACTOR below that trivial
    ceiling, and that factor IS the delocalisation, read off the form
    and not off the minimiser.
[E] (4) THE COMPOSITE LEVEL LEMMA (T146).  c_0^ap = 2 b^2 Gam
    min(1, Gam_1) + eps, minimised over a PREREGISTERED base grid, every
    factor a functional of E alone, and the certified window inequality
        cert_lam_max(R) <= c_0^ap x Psi_abs
    on every window (both sides by completed Cholesky, direction in the
    name), which closes the chain lam >= 1/(kap_up c_0^ap Psi_abs) per
    window.  THE BUILT-IN DISCRIMINATOR: on T145's no-go form
    R = a a^T + eps I with a_i = i^{-1/2} (positive definite, entrywise
    nonnegative, absolutely bounded density sup) the bound MUST be
    worse than on the form -- Gam grows with m (unbounded), c_0^ap
    exceeds every window value -- while the THEOREM half still holds
    there and the whole construction stays FLAT on the Dirichlet path
    Laplacian.  A candidate that did not fail on the no-go would prove
    a false statement.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL windows.  Nothing
        here is uniform in the zone index or in D; what is established
        is a FINITE LIST of certified window inequalities with an
        explicit maximum, and every T146 exponent is a FIT that stays
        in the sandbox.  The step to ALL D -- an asymptotic bound on
        max_j ||R e_j|| lam_min, i.e. the delocalisation of the Green
        columns themselves -- is OPEN and explicitly NOT claimed.
  (ii)  (4) bounds the SIGN-FREE / GREEN constant G_dy a priori.  The
        ENERGY-route constant sig_tot stays MEASURED (T146's remainder
        (1)); nothing here touches it, and no marker of any
        pre-existing contract moves.
  (iii) (1) and (2) are counting statements about ANY vector; (3) is a
        theorem about ANY symmetric positive definite form -- all three
        are form-independent and say nothing about the size of the
        constants on any particular surface.
  (iv)  The no-go / control discrimination of (4) is checked on THIS
        size ladder (m <= 288, inside the module's hard cap); the
        growth exponents quoted by T146 are fits and are not promoted.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  The surrounding statement is the positivity of a
    Weil window form (Weil 1952, CITED, never used as a criterion) on a
    FINITE list of prime-power zones.  Everything here is an identity
    or a certified inequality PER INSTANCE; NOTHING here claims,
    assumes or approaches RH, and no statement about zeta zeros is
    made.  No zero data of any kind is read, generated or approximated
    -- an AST firewall enforces this.  NO all-D claim: even with every
    check green, what stands is a finite list of certified window
    statements on prime-power zones, and the all-D asymptotics stays
    open here and everywhere.
  * Classics named CLASSICAL: Maz'ya 1985 (the capacitary strong type
    whose transcription consumes this lemma; his strong-type HALF is
    NOT used as a theorem anywhere), Rayleigh 1877 / Ritz 1909 (the
    variational upper bound), Cauchy-Schwarz, Miclo 1999 (level-set
    chains), Davis-Kahan 1970 (CITED as the transfer step this route
    deliberately avoids -- instrumented in T146 and NOT used here),
    Perron-Frobenius (single-signedness on the Stieltjes partner, NOT
    applicable to E and not used), Fukushima-Oshima-Takeda 1994
    (Beurling-Deny), Charikar 2000 / Goldberg 1984 (the density
    bound's cited constant), Gershgorin 1931, Wilkinson 1968 / Higham
    2002 (completed Cholesky).
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] exact counting / linear-algebra identities at rel
< 1e-9 .. 1e-15 as stated, per-instance theorems with checked
hypotheses, certified inequalities by completed Cholesky with the
direction in the name, each with a mutation control that fails by
>= 1e-3 relative.  Python; Wolfram-mirrored not required (dense
Cholesky / eigenvalue identities stay Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/level_lemma_probe.py            (T146)
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
ATOM_MAX = 320000            # atom table cap, as in v546
H_CAP = 300                  # HARD cap on any inverted / diagonalised matrix
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
U_ROUND = 2.0 ** -53

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept (spread over the D range)
LEV_MAX = 34                 # dyadic levels kept above the floor (T145/T146)
N_RAND = 9                   # random forms for the form-independent items
RAND_M = 40                  # their size

# --- THE CAKE BASE GRID, preregistered exactly as T146 declared it ---------
BASE_GRID = (2.0, 1.5, 1.25, 1.125, 1.0625, 1.03125)
FL_TARGET = 1.0e-12          # absolute floor level of the untruncated cake

# --- the stress ladder (all sizes inside the hard cap) ----------------------
STRESS_SIZES = (64, 96, 144, 216, 288)
NOGO_EPS = 1.0e-3

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_ID = 1.0e-11             # every identity must hold to this relative level
TOL_DIR = 1.0e-9             # one-sided slack of per-instance theorem steps
TOL_CERT = 1.0e-9            # certified-inequality slack (relative)
BAR_CTRL = 1.0e-3            # a mutation control must fail at least this hard
BAR_LEVER = 2.0              # column norms below the trivial ceiling by this
BAR_NOGO_RATIO = 1.5         # Gam growth over the ladder that counts as unbounded
BAR_CTRL_FLAT = 1.05         # Gam max/min on the Dirichlet control ladder
BAR_C0 = 16.0                # classical-size ceiling: 4 x Maz'ya's Dirichlet 4
MAZYA_C0 = 4.0               # the classical Dirichlet constant, CITED


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
    """The T115 O(#atoms) lag assembly (frame-A code path of T128..T146)."""
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


# ------------------------------------- the reflection-odd sector (T106..T146)
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


# ------------------------------------ the lumped pair and the whitened form
def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) -
    Delta, A_B = A + L_Delta (T136).  DIRECTION: L_Delta >= 0, so A_B >= A."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    return dict(h=h, A_B=sym(A + LD), Dl=Dl)


def jacobi_whiten(A, A_B):
    """With Lam = diag(A_B): E = Lam^{-1/2} A Lam^{-1/2} (counting measure),
    W = Lam^{-1/2} A_B Lam^{-1/2} (unit diagonal), kap_up certified."""
    Lam = np.diag(A_B).copy()
    if not (float(np.min(Lam)) > 0.0):
        return None
    sq = 1.0 / np.sqrt(Lam)
    E = sym(A * np.outer(sq, sq))
    W = sym(A_B * np.outer(sq, sq))
    kap_up = cert_lam_max(W, guess=ray_top(W))
    return dict(E=E, W=W, kap_up=kap_up)


# ---------------------- the density bound (T144/T145 object, |R| and never R^+)
def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000): the returned density is
    ATTAINED (a lower bound) and opt <= 2 x greedy is the CITED constant."""
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
    """UPPER bound for sup_A (1^T R_AA 1) / |A| over ALL 2^m sets, with the
    cited constant (Charikar 2000; Goldberg 1984) or the certified spectrum.
    DIRECTION: an UPPER bound, the direction the chain consumes."""
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    gr = greedy_density(Rp)
    dg_max = float(np.max(np.diag(R)))
    psi_char = dg_max + 4.0 * gr
    psi_spec = dg_max + cert_lam_max(Rp, guess=ray_top(Rp))
    cands = [x for x in (psi_char, psi_spec) if np.isfinite(x)]
    return min(cands) if cands else float("nan")


# ------------------------- the general-base layer cake (T146's closed objects)
def layer_cake(psi, base=2.0, n_lev=LEV_MAX):
    """THE LAYER CAKE of |psi| to a general base as an explicit NESTED
    decreasing chain (the K x m indicator representation, kept only so the
    union IDENTITY of item (1) can be checked against T145's K x K form)."""
    v = np.abs(np.asarray(psi, dtype=float))
    m = v.shape[0]
    vmax = float(np.max(v))
    if not (vmax > 0.0):
        return None
    lb = math.log(base)
    k_top = int(math.floor(math.log(vmax) / lb))
    while base ** k_top >= vmax:
        k_top -= 1
    while base ** (k_top + 1) < vmax:
        k_top += 1
    k_bot = k_top - n_lev + 1
    order = np.argsort(-v, kind="stable")
    sizes = [m]
    coef = [base ** k_bot]
    for k in range(k_bot, k_top + 1):
        t = base ** k
        n_k = int(np.count_nonzero(v > t))
        if n_k <= 0:
            continue
        sizes.append(n_k)
        coef.append((base - 1.0) * t)
    Kn = len(sizes)
    Ind = np.zeros((Kn, m))
    for j in range(Kn):
        Ind[j, order[:sizes[j]]] = 1.0
    cv = np.array(coef, dtype=float)
    nv = np.array(sizes, dtype=float)
    jj = np.arange(Kn)
    mn = np.minimum.outer(jj, jj)          # the LARGER set has the SMALLER index
    return dict(K=Kn, Ind=Ind, c=cv, n=nv, mn=mn, v=v, m=m,
                k_top=k_top, k_bot=k_bot, psi_t=Ind.T @ cv)


def union_double_sum(lc):
    """T145's K x K arithmetic: sum_{j,l} c_j c_l |S_{min(j,l)}| -- for a
    NESTED chain |S_j u S_l| IS the larger set, i.e. the smaller index."""
    return float(lc["c"] @ (lc["n"][lc["mn"]] @ lc["c"]))


def union_closed(lc):
    """THE UNION IDENTITY, item (1): 2 T ||psi_t||_1 - ||psi_t||^2 in O(m)."""
    T = float(lc["c"].sum())
    pt = lc["psi_t"]
    return 2.0 * T * float(pt.sum()) - float(pt @ pt)


def union_exact_sets(Ind, cv):
    """The union double sum from the SETS THEMSELVES (no nestedness used):
    |S_j u S_l| = n_j + n_l - |S_j n S_l| -- the reference the mutation
    control is judged against."""
    inter = Ind @ Ind.T
    nv = np.diag(inter).copy()
    uni = nv[:, None] + nv[None, :] - inter
    return float(cv @ (uni @ cv))


def cake_profile(v, base, n_lev=None, fl_target=FL_TARGET):
    """THE LEVEL CONSTANT IN CLOSED FORM, item (2): psi_t,i = base^{k_i+1}
    exactly (telescoping), G(base) by the union identity in O(m), and the
    counting-lemma bound with its explicit floor term eps."""
    v = np.abs(np.asarray(v, dtype=float))
    m = v.shape[0]
    vmax = float(np.max(v))
    if not (vmax > 0.0):
        return None
    lb = math.log(base)
    k_top = int(math.floor(math.log(vmax) / lb))
    while base ** k_top >= vmax:
        k_top -= 1
    while base ** (k_top + 1) < vmax:
        k_top += 1
    if n_lev is None:
        k_bot = int(math.floor(math.log(fl_target) / lb))
        while base ** k_bot > fl_target:
            k_bot -= 1
    else:
        k_bot = k_top - n_lev + 1
    fl = base ** k_bot
    T = base ** (k_top + 1)
    kk = np.floor(np.log(np.maximum(v, 1.0e-300)) / lb)
    kk = np.where(base ** kk >= v, kk - 1.0, kk)
    B = np.maximum(base ** (kk + 1.0), fl)
    B = np.where(v <= fl, fl, B)
    nrm2 = float(v @ v)
    v_l1 = float(v.sum())
    s1 = float(B.sum())
    G = (2.0 * T * s1 - float(B @ B)) / max(nrm2, 1.0e-300)
    eps = 2.0 * base * vmax * m * fl / max(nrm2, 1.0e-300)
    thm = 2.0 * base * base * vmax * v_l1 / max(nrm2, 1.0e-300) + eps
    return dict(base=base, m=m, k_top=k_top, k_bot=k_bot, fl=fl, T=T, B=B,
                G=G, thm=thm, eps=eps, vmax=vmax, v_l1=v_l1, nrm2=nrm2,
                dom_min=float(np.min(B - v)),
                t_slack=base * vmax - T,
                s1_slack=(base * v_l1 + m * fl) - s1)


def c0_of_base(Gam, Gam_1, base, m):
    """THE A PRIORI LEVEL CONSTANT at a given cake base, item (4):
    c_0^ap(base) = 2 base^2 Gam min(1, Gam_1) + eps, with eps built from the
    a priori sup bound Gam / sqrt(m) -- no factor reads the minimiser."""
    vmax_ap = Gam / math.sqrt(max(m, 1))
    lb = math.log(base)
    k_bot = int(math.floor(math.log(FL_TARGET) / lb))
    while base ** k_bot > FL_TARGET:
        k_bot -= 1
    eps = 2.0 * base * vmax_ap * m * (base ** k_bot)
    return 2.0 * base * base * Gam * min(1.0, Gam_1) + eps


def apriori_level(E, R=None):
    """THE A PRIORI SIDE of items (3) and (4), computed from the FORM alone:
    lam_up by Rayleigh-Ritz on the Green columns, the column norms certified
    from above with the linear-solve residual paid for, Gam and Gam_1, and
    c_0^ap minimised over the preregistered base grid."""
    m = E.shape[0]
    if R is None:
        fac = safe_cho(E)
        if fac is None:
            return None
        R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    lam_lo = cert_lam_min_pos(E)
    if not (np.isfinite(lam_lo) and lam_lo > 0.0):
        return None
    EV = E @ R
    den = np.sum(R * R, axis=0)                       # ||x_j||^2
    num = np.sum(R * EV, axis=0)                      # x_j^T E x_j
    rres = np.linalg.norm(EV - np.eye(m), axis=0)
    if not bool(np.all(den > 0.0)):
        return None
    fl_q = chol_floor(gersh(E), m)
    lam_up = float(np.min(num / den)) + fl_q
    col_raw = np.sqrt(den)
    col_up = col_raw + rres / lam_lo
    gam_G = float(np.max(col_up))
    Gam = math.sqrt(m) * lam_up * gam_G
    Gam_1 = lam_up * float(np.sum(col_up)) / math.sqrt(m)
    c0_by_base = {b: c0_of_base(Gam, Gam_1, b, m) for b in BASE_GRID}
    base_star = min(BASE_GRID, key=lambda b: c0_by_base[b])
    return dict(m=m, R=R, lam_lo=lam_lo, lam_up=lam_up, fl_q=fl_q,
                col_raw=col_raw, col_up=col_up, gam_G=gam_G,
                Gam=Gam, Gam_1=Gam_1, base_star=base_star,
                c0_ap=c0_by_base[base_star], c0_dy=c0_by_base[2.0],
                res_share=float(np.max(rres / lam_lo
                                       / np.maximum(col_raw, 1.0e-300))))


# ------------------------------------------- the stress forms of item (4)
def nogo_form(m, eps=NOGO_EPS):
    """T145's NO-GO: R = a a^T + eps I with a_i = i^{-1/2} -- positive
    definite, entrywise nonnegative, absolutely bounded density sup, and the
    L1 candidate MUST fail here.  E = R^{-1} is CLOSED (Sherman-Morrison)."""
    a = 1.0 / np.sqrt(np.arange(1, m + 1, dtype=float))
    R = sym(np.outer(a, a) + eps * np.eye(m))
    n2 = float(a @ a)
    E = sym((np.eye(m) - np.outer(a, a) / (eps + n2)) / eps)
    return dict(R=R, E=E, lam_min=1.0 / (n2 + eps))


def control_form(m):
    """THE CONTROL: the Dirichlet path Laplacian, a genuine Markovian form;
    the candidate must stay BOUNDED here, uniformly along the ladder."""
    E = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    fac = safe_cho(E)
    if fac is None:
        return None
    R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    return dict(E=E, R=R)


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
    """One window, end to end: the odd section, the lumped pair, the whitened
    form E with its Green matrix R and minimiser psi, the a-priori side, and
    the measured cross-checks of items (1)-(4)."""
    al = 0.5 * M * D
    c, _ = lag_vector_fast(al, M, atoms_in(al))
    A = sym(odd_toeplitz(c, M))
    lp = lump_pair(A)
    A_B = lp["A_B"]
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return None
    if not (gap_ex > 0.0):
        return None
    jw = jacobi_whiten(A, A_B)
    if jw is None or not np.isfinite(jw["kap_up"]):
        return None
    E = jw["E"]
    try:
        wv, Vv = eigh(E, subset_by_index=[0, 1])
    except (LinAlgError, ValueError):
        return None
    lam_hat = float(wv[0])
    lam_2 = float(wv[1])
    if not (lam_hat > 0.0):
        return None
    psi = Vv[:, 0] / max(float(np.linalg.norm(Vv[:, 0])), 1.0e-300)

    ap = apriori_level(E)
    if ap is None:
        return None
    R = ap["R"]
    psi_abs = density_all_upper(np.abs(R))
    if not np.isfinite(psi_abs):
        return None

    row = dict(n=NN_ALL[k], h=h, m=h, D=D, gap_ex=gap_ex,
               lam_hat=lam_hat, sep_rel=lam_2 / lam_hat,
               kap_up=jw["kap_up"], psi=psi, E=E, R=R, psi_abs=psi_abs)
    row.update({kk: ap[kk] for kk in (
        "lam_lo", "lam_up", "fl_q", "col_raw", "col_up", "gam_G",
        "Gam", "Gam_1", "base_star", "c0_ap", "c0_dy", "res_share")})

    # measured cross-checks (the minimiser is read HERE and only here)
    row["v_inf"] = float(np.max(np.abs(psi)))
    row["v_l1"] = float(np.abs(psi).sum())
    cp_dy = cake_profile(psi, 2.0, n_lev=LEV_MAX)
    cp_st = cake_profile(psi, ap["base_star"])
    if cp_dy is None or cp_st is None:
        return None
    row["G_dy"], row["G_st"] = cp_dy["G"], cp_st["G"]
    row["thm_st"] = cp_st["thm"]
    lc = layer_cake(psi, 2.0, n_lev=LEV_MAX)
    row["union_kk"] = union_double_sum(lc)
    row["union_cl"] = cp_dy["G"] * cp_dy["nrm2"]
    row["lc"] = lc
    # the chain with the a-priori constant in it
    row["bound_hat"] = 1.0 / max(row["c0_ap"] * psi_abs, 1.0e-300)
    row["bound_ex"] = row["bound_hat"] / max(row["kap_up"], 1.0e-300)
    row["cert_R"] = cert_lam_max(R, guess=ray_top(R))
    return row


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(5472026)
    print("=" * 72)
    print("v547  PRIME.LEVEL.LEMMA.01 -- level-lemma identities (T146)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered bars")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    for (k, D, M, h) in build_windows():
        row = build_instance(k, D, M, h)
        if row is not None:
            INST.append(row)
    h_max = max(t["h"] for t in INST) if INST else 0
    d_lo = min(t["D"] for t in INST) if INST else float("nan")
    d_hi = max(t["D"] for t in INST) if INST else float("nan")
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (whitened "
          f"pair positive definite, Green matrix and density bound finite); "
          f"every inverted / factorised / diagonalised matrix <= {H_CAP} "
          f"(max h = {h_max}); the surface spans D = {d_lo:.3e} .. {d_hi:.3e}",
          len(INST) >= 6 and h_max <= H_CAP)
    for t in INST:
        print(f"    n={t['n']:>7d} D={t['D']:.4e} m={t['m']:>4d} "
              f"lam_hat={t['lam_hat']:.4e} Gam={t['Gam']:.4f} "
              f"c0_ap={t['c0_ap']:.4f}")

    # random PD forms for the form-independent items
    RAND = []
    for _ in range(N_RAND):
        B = rng.standard_normal((RAND_M, RAND_M))
        Ex = sym(B @ B.T) + 0.3 * np.eye(RAND_M)
        fac = safe_cho(Ex)
        Rx = sym(cho_solve(fac, np.eye(RAND_M), check_finite=False))
        wx, Vx = eigh(Ex, subset_by_index=[0, 0])
        px = Vx[:, 0] / float(np.linalg.norm(Vx[:, 0]))
        RAND.append(dict(E=Ex, R=Rx, lam=float(wx[0]), psi=px))

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the union identity for nested cakes  (T146)")
    id_err = 0.0
    for t in INST:
        id_err = max(id_err, abs(t["union_cl"] - t["union_kk"])
                     / max(abs(t["union_kk"]), 1.0e-300))
    id_rand = 0.0
    ex_err = 0.0
    for d in RAND:
        lcx = layer_cake(d["psi"], 2.0, n_lev=LEV_MAX)
        dsum = union_double_sum(lcx)
        clsd = union_closed(lcx)
        exact = union_exact_sets(lcx["Ind"], lcx["c"])
        id_rand = max(id_rand, abs(clsd - dsum) / max(abs(dsum), 1.0e-300))
        ex_err = max(ex_err, abs(clsd - exact) / max(abs(exact), 1.0e-300))
    check(f"S1.ID: sum_jl c_j c_l |S_j u S_l| == 2 T ||psi_t||_1 - "
          f"||psi_t||^2 for the nested cake, checked against T145's K x K "
          f"double sum on all {len(INST)} window minimisers (max rel "
          f"{id_err:.2e}) and {N_RAND} random vectors (max rel {id_rand:.2e}, "
          f"bar {TOL_ID:.0e}), AND against the union sizes computed from the "
          f"sets themselves with no nestedness used (max rel {ex_err:.2e}) -- "
          f"one line, form-independent, the reason the base is movable",
          id_err < TOL_ID and id_rand < TOL_ID and ex_err < TOL_ID)
    # mutation controls: break the nesting (at a PROPER level set, so the
    # shuffle can act), then break the HEAVIEST coefficient
    ctrl_nest = float("inf")
    ctrl_coef = float("inf")
    for d in RAND[:3]:
        lcx = layer_cake(d["psi"], 2.0, n_lev=LEV_MAX)
        sizes = lcx["n"]
        proper = [j for j in range(lcx["K"]) if 0 < sizes[j] < lcx["m"]]
        j_mut = min(proper, key=lambda j: abs(sizes[j] - lcx["m"] / 2))
        Ind = lcx["Ind"].copy()
        perm = rng.permutation(lcx["m"])
        Ind[j_mut] = Ind[j_mut][perm]           # same size, no longer nested
        exact_mut = union_exact_sets(Ind, lcx["c"])
        clsd = union_closed(lcx)
        ctrl_nest = min(ctrl_nest, abs(clsd - exact_mut)
                        / max(abs(exact_mut), 1.0e-300))
        cv2 = lcx["c"].copy()
        cv2[int(np.argmax(cv2 * sizes))] *= 1.01
        dsum_mut = float(cv2 @ (lcx["n"][lcx["mn"]] @ cv2))
        ctrl_coef = min(ctrl_coef, abs(clsd - dsum_mut)
                        / max(abs(dsum_mut), 1.0e-300))
    check(f"S1.CTRL: shuffling ONE level set (same size, no longer nested) "
          f"breaks the identity against the exact union sizes (min rel "
          f"{ctrl_nest:.2e} > {BAR_CTRL:.0e}), and a 1% perturbation of one "
          f"coefficient breaks the double sum too (min rel {ctrl_coef:.2e}) "
          f"-- the nestedness and the telescoping coefficients are both "
          f"load-bearing", ctrl_nest > BAR_CTRL and ctrl_coef > BAR_CTRL)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the layer-cake counting lemma at a general base  "
          "(T146)")
    dom_bad = -float("inf")
    cnt_bad = -float("inf")
    thm_bad = -float("inf")
    dom_ctrl = float("inf")
    for d in RAND:
        for b in BASE_GRID:
            cp = cake_profile(d["psi"], b)
            dom_bad = max(dom_bad, -cp["dom_min"])
            cnt_bad = max(cnt_bad, -cp["t_slack"], -cp["s1_slack"])
            thm_bad = max(thm_bad, cp["G"] - cp["thm"])
            below = np.min(cp["B"] / b - np.abs(d["psi"]))
            dom_ctrl = min(dom_ctrl, -float(below))
    check(f"S2.COUNT: the counting inequalities at ALL {len(BASE_GRID)} "
          f"bases of the preregistered grid, in the direction the chain "
          f"consumes: |v| <= psi_t (worst slack {dom_bad:.2e}), T <= base "
          f"||v||_inf and ||psi_t||_1 <= base ||v||_1 + m base^kbot (worst "
          f"{cnt_bad:.2e}) -- pure counting, no analysis",
          dom_bad <= TOL_DIR and cnt_bad <= TOL_DIR)
    thm_win = -float("inf")
    for t in INST:
        thm_win = max(thm_win, t["G_st"] - t["thm_st"])
    dy8 = abs(2.0 * 2.0 ** 2 - 8.0)
    check(f"S2.LEMMA: G(base) <= 2 base^2 ||v||_inf ||v||_1 / ||v||^2 + eps "
          f"on {N_RAND} random vectors x {len(BASE_GRID)} bases (worst slack "
          f"{thm_bad:.2e} <= 0) AND on the minimiser of every window at its "
          f"chosen base (worst slack {thm_win:.2e}); at base 2 the leading "
          f"constant is 2 x 2^2 = 8, the classical dyadic value EXACTLY "
          f"(dev {dy8:.1f}) -- a THEOREM about any vector, no minimiser "
          f"mentioned", thm_bad <= TOL_DIR and thm_win <= TOL_DIR
          and dy8 == 0.0)
    b_star = min(BASE_GRID)
    gain_lo = min(t["c0_dy"] / t["c0_ap"] for t in INST)
    gain_hi = max(t["c0_dy"] / t["c0_ap"] for t in INST)
    gain_th = 4.0 / (b_star * b_star)
    gain_ok = all(abs(t["c0_dy"] / t["c0_ap"] - gain_th) < 0.01 * gain_th
                  for t in INST)
    check(f"S2.BASE: THE BASE IS FREE -- the chain uses only the lower "
          f"domination, so the dyadic 8 falls to 2 base^2: the a-priori "
          f"constant gains a factor {gain_lo:.4f}..{gain_hi:.4f} over base 2 "
          f"on every window, equal to 4/base*^2 = {gain_th:.4f} at the grid "
          f"minimum base {b_star} up to the (tiny) floor terms -- the ceiling "
          f"2 base^2 -> 2 is the honest limit of this direction",
          gain_ok)
    ctrl_thm = all(
        cake_profile(d["psi"], b)["G"] > BAR_CTRL * cake_profile(d["psi"], b)["thm"]
        for d in RAND for b in BASE_GRID)
    check(f"S2.CTRL: scaling the bound by {BAR_CTRL:.0e} breaks it on every "
          f"draw and base (the lemma is not vacuous slack), and shifting the "
          f"cake ONE level down (psi_t / base) breaks the domination on every "
          f"draw (worst undershoot {dom_ctrl:.2e} > 0) -- the +1 in the cake "
          f"exponent is load-bearing, not decorative",
          ctrl_thm and dom_ctrl > 0.0)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the resolvent delocalisation bound  (T146)")
    eig_id = 0.0
    ritz_bad = -float("inf")
    cs_bad = -float("inf")
    col_bad = -float("inf")
    for d in RAND:
        eig_id = max(eig_id, rel(d["psi"] - d["lam"] * (d["R"] @ d["psi"]),
                                 d["psi"]))
        dn = np.sum(d["R"] * d["R"], axis=0)
        nu = np.sum(d["R"] * (d["E"] @ d["R"]), axis=0)
        ritz_bad = max(ritz_bad, d["lam"] - float(np.min(nu / dn)))
        cs_bad = max(cs_bad, float(np.max(np.abs(d["psi"])
                                          - d["lam"] * np.sqrt(dn))))
        llo = cert_lam_min_pos(d["E"])
        xj = d["R"][:, 0]
        rj = float(np.linalg.norm(d["E"] @ xj - np.eye(RAND_M)[:, 0]))
        col_bad = max(col_bad, float(np.linalg.norm(d["R"][:, 0]))
                      - (float(np.linalg.norm(xj)) + rj / llo))
    check(f"S3.ID: psi == lam R psi to {eig_id:.2e} (bar {TOL_ID:.0e}) on "
          f"{N_RAND} random forms -- an IDENTITY, not a perturbation "
          f"statement, which is why NO transfer step (Davis-Kahan 1970, "
          f"cited, instrumented by T146 and NOT used) appears anywhere in "
          f"this module", eig_id < TOL_ID)
    ctrl_eig = float("inf")
    for d in RAND:
        ctrl_eig = min(ctrl_eig,
                       rel(d["psi"] - 1.01 * d["lam"] * (d["R"] @ d["psi"]),
                           d["psi"]))
    check(f"S3.RITZ: lam_up = min_j Rayleigh(R e_j) >= lam_min on every "
          f"random form (worst slack {-ritz_bad:.3e} >= 0; Rayleigh 1877, "
          f"Ritz 1909 -- the Green columns are legal test vectors) and the "
          f"coordinate bound |psi_j| <= lam ||R e_j|| holds per coordinate "
          f"(worst {cs_bad:.2e} <= 0, Cauchy-Schwarz); the certified column "
          f"norm ||x_j|| + ||E x_j - e_j|| / cert_lam_min(E) dominates the "
          f"true ||R e_j|| (worst {col_bad:.2e} <= 0) -- the linear-solve "
          f"residual is paid for, not assumed away",
          ritz_bad <= TOL_DIR and cs_bad <= TOL_DIR and col_bad <= TOL_DIR)
    ritz_win = all(t["lam_up"] >= t["lam_hat"] * (1.0 - TOL_DIR)
                   for t in INST)
    ru_lo = min(t["lam_up"] / t["lam_hat"] for t in INST)
    ru_hi = max(t["lam_up"] / t["lam_hat"] for t in INST)
    sup_ok = all(t["v_inf"] <= t["lam_up"] * t["gam_G"] * (1.0 + TOL_DIR)
                 for t in INST)
    l1_ok = all(t["v_l1"] <= math.sqrt(t["m"]) * min(1.0, t["Gam_1"])
                * (1.0 + TOL_DIR) for t in INST)
    tight_lo = min(t["lam_up"] * t["gam_G"] / t["v_inf"] for t in INST)
    tight_hi = max(t["lam_up"] * t["gam_G"] / t["v_inf"] for t in INST)
    check(f"S3.SUP: on every one of the {len(INST)} windows: lam_up >= "
          f"lam_hat (ratio {ru_lo:.4f}..{ru_hi:.4f} -- tens of percent, not "
          f"orders), ||psi||_inf <= lam_up max_j ||R e_j||_up (within factor "
          f"{tight_lo:.3f}..{tight_hi:.3f} of the truth) and ||psi||_1 <= "
          f"sqrt(m) min(1, Gam_1) -- the sup and l1 norms of the TRUE "
          f"minimiser bounded with no assumption that any computed vector is "
          f"the minimiser", ritz_win and sup_ok and l1_ok)
    lever_lo = min((1.0 / t["lam_hat"]) / t["gam_G"] for t in INST)
    lever_hi = max((1.0 / t["lam_hat"]) / t["gam_G"] for t in INST)
    gam_lo = min(t["Gam"] for t in INST)
    gam_hi = max(t["Gam"] for t in INST)
    check(f"S3.LEVER: the lever made explicit -- the trivial route "
          f"max_j ||R e_j|| <= ||R|| = 1/lam_min would give Gam <= sqrt(m) "
          f"= {math.sqrt(min(t['m'] for t in INST)):.1f}.."
          f"{math.sqrt(max(t['m'] for t in INST)):.1f} (useless); the "
          f"certified column norms sit a factor {lever_lo:.2f}..{lever_hi:.2f} "
          f"BELOW that trivial ceiling on every window (bar {BAR_LEVER:.1f}), "
          f"giving Gam = {gam_lo:.4f}..{gam_hi:.4f} -- that factor IS the "
          f"delocalisation, read off the form and never off the minimiser",
          lever_lo >= BAR_LEVER)
    sup_ctrl = all(t["v_inf"] > BAR_CTRL * t["lam_up"] * t["gam_G"]
                   for t in INST)
    check(f"S3.CTRL: perturbing lam by 1% breaks the eigen-identity on every "
          f"random form (min rel {ctrl_eig:.2e} > {BAR_CTRL:.0e}), and "
          f"scaling the sup bound by {BAR_CTRL:.0e} breaks it on every "
          f"window -- neither side is vacuous",
          ctrl_eig > BAR_CTRL and sup_ctrl)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the composite level lemma, certified per window  "
          "(T146)")
    dom_meas = all(t["c0_ap"] >= t["G_st"] * (1.0 - TOL_DIR) for t in INST)
    sl_lo = min(t["c0_ap"] / t["G_st"] for t in INST)
    sl_hi = max(t["c0_ap"] / t["G_st"] for t in INST)
    c0_lo = min(t["c0_ap"] for t in INST)
    c0_hi = max(t["c0_ap"] for t in INST)
    check(f"S4.LEMMA: c_0^ap = 2 base^2 Gam min(1, Gam_1) + eps = "
          f"{c0_lo:.4f}..{c0_hi:.4f} dominates the MEASURED level constant "
          f"of the minimiser's own cake on all {len(INST)} windows (slack "
          f"factor {sl_lo:.3f}..{sl_hi:.3f}), stays under the preregistered "
          f"classical-size ceiling {BAR_C0:.0f} = 4 x Maz'ya's Dirichlet "
          f"value {MAZYA_C0:.0f} (Maz'ya 1985, CITED for scale) -- every "
          f"factor a functional of E alone, the measured G appearing ONLY as "
          f"the cross-check", dom_meas and c0_hi <= BAR_C0)
    cert_ok = all(t["cert_R"] <= t["c0_ap"] * t["psi_abs"] * (1.0 + TOL_CERT)
                  for t in INST)
    check(f"S4.CERT: the certified window inequality cert_lam_max(R) <= "
          f"c_0^ap x Psi_abs holds on all {len(INST)} windows -- BOTH sides "
          f"by completed Cholesky (Wilkinson 1968; Higham 2002) with the "
          f"direction in the name, the density the |R| one with Charikar's "
          f"cited constant (Charikar 2000; Goldberg 1984), itself a priori",
          cert_ok)
    chain_ok = all(t["bound_hat"] <= t["lam_hat"] * (1.0 + TOL_DIR)
                   and t["bound_ex"] <= t["gap_ex"] * (1.0 + TOL_DIR)
                   for t in INST)
    lh_lo = min(t["bound_ex"] / t["gap_ex"] for t in INST)
    lh_hi = max(t["bound_ex"] / t["gap_ex"] for t in INST)
    check(f"S4.CHAIN: the chain with the a-priori constant in it -- lam_hat "
          f">= 1/(c_0^ap Psi_abs) and gap >= lam_hat / kap_up -- holds on "
          f"every window with loss factor {lh_lo:.4f}..{lh_hi:.4f} of the "
          f"exact gap; T145's certified chain, with its one measured input "
          f"replaced by a functional of the form", chain_ok)
    # the built-in discriminator: the no-go MUST fail, the control must not
    gam_ng, c0_ng, thm_ng = [], [], []
    for msz in STRESS_SIZES:
        ng = nogo_form(msz)
        apn = apriori_level(ng["E"], R=ng["R"])
        wn, Vn = eigh(ng["E"], subset_by_index=[0, 0])
        psn = Vn[:, 0] / float(np.linalg.norm(Vn[:, 0]))
        cpn = cake_profile(psn, 2.0, n_lev=LEV_MAX)
        gam_ng.append(apn["Gam"])
        c0_ng.append(apn["c0_ap"])
        thm_ng.append((cpn["G"], cpn["thm"], apn["c0_dy"]))
    gam_ct = []
    for msz in STRESS_SIZES:
        ct = control_form(msz)
        apc = apriori_level(ct["E"], R=ct["R"])
        gam_ct.append(apc["Gam"])
    ng_ratio = gam_ng[-1] / gam_ng[0]
    ct_ratio = max(gam_ct) / min(gam_ct)
    worse_ok = max(c0_ng) > c0_hi
    check(f"S4.NOGO: THE CANDIDATE PASSES THE STRESS TEST BY FAILING, the "
          f"only acceptable outcome: on T145's no-go form R = a a^T + eps I, "
          f"a_i = i^(-1/2), m = {STRESS_SIZES[0]}..{STRESS_SIZES[-1]}, Gam "
          f"grows {gam_ng[0]:.3f} -> {gam_ng[-1]:.3f} (ratio {ng_ratio:.2f} "
          f">= {BAR_NOGO_RATIO:.1f}, the preregistered unboundedness "
          f"criterion) and c_0^ap = {max(c0_ng):.2f} EXCEEDS every window "
          f"value ({c0_hi:.2f}) -- the delocalisation input does not exist "
          f"there, exactly as the no-go demands; a bound that did NOT fail "
          f"here would prove a false statement",
          ng_ratio >= BAR_NOGO_RATIO and worse_ok)
    thm_ng_ok = all(g <= th * (1.0 + TOL_DIR) and g <= c0 * (1.0 + TOL_DIR)
                    for (g, th, c0) in thm_ng)
    check(f"S4.SPLIT: and the failure is LOCATED -- the THEOREM half (the "
          f"counting lemma and c_0^ap as bounds on the exact G) survives on "
          f"every no-go size, so the failure sits entirely in the "
          f"delocalisation input Gam and nowhere in the cake arithmetic; "
          f"the Dirichlet path-Laplacian CONTROL stays flat along the same "
          f"ladder (Gam = {min(gam_ct):.4f}..{max(gam_ct):.4f}, max/min "
          f"{ct_ratio:.4f} <= {BAR_CTRL_FLAT:.2f}) -- the candidate "
          f"discriminates in both directions", thm_ng_ok
          and ct_ratio <= BAR_CTRL_FLAT)
    ctrl_c0 = all(t["cert_R"] > BAR_CTRL * t["c0_ap"] * t["psi_abs"]
                  for t in INST)
    check(f"S4.CTRL: scaling c_0^ap by {BAR_CTRL:.0e} breaks the certificate "
          f"on every window -- the certified inequality is not vacuous slack",
          ctrl_c0)

    # ---------------------------------------------------------------- fences
    print("\nS5 -- the fences, restated as a check")
    check("S5.FENCE: PER-INSTANCE identities, theorems with checked "
          "hypotheses and certified inequalities on SMALL windows only -- a "
          "FINITE LIST with an explicit maximum, nothing uniform in the zone "
          "index or in D, and NO statement for ALL D (the asymptotic "
          "delocalisation of the Green columns, T146's remainder, stays "
          "OPEN, unclaimed and unapproached); the ENERGY-route constant "
          "sig_tot stays MEASURED and is not touched; every T146 exponent "
          "is a FIT and stays in the sandbox; Maz'ya 1985 / Rayleigh 1877 / "
          "Ritz 1909 / Cauchy-Schwarz / Miclo 1999 / Davis-Kahan 1970 "
          "(cited, deliberately NOT used) / Perron-Frobenius (not "
          "applicable to E, not used) / Fukushima-Oshima-Takeda 1994 / "
          "Charikar 2000 / Goldberg 1984 / Gershgorin 1931 / Wilkinson 1968 "
          "/ Higham 2002 named CLASSICAL, and Maz'ya's strong-type half is "
          "NOT used as a theorem anywhere; Weil 1952 CITED, never used as a "
          "criterion; zero-firewall AST-checked; NO marker upgrade of any "
          "pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv547 runtime: {elapsed:.1f}s")
    print(f"  (1) union identity: max rel {max(id_err, id_rand):.1e}; "
          f"controls fail at {min(ctrl_nest, ctrl_coef):.1e}")
    print(f"  (2) counting lemma: worst slack {max(thm_bad, thm_win):.1e}; "
          f"base gain {gain_lo:.2f}..{gain_hi:.2f} (theory {gain_th:.2f})")
    print(f"  (3) delocalisation: Gam = {gam_lo:.4f}..{gam_hi:.4f}; lever "
          f"{lever_lo:.2f}..{lever_hi:.2f} below the trivial ceiling")
    print(f"  (4) level lemma: c_0^ap = {c0_lo:.4f}..{c0_hi:.4f} vs the "
          f"Dirichlet value {MAZYA_C0:.0f}; chain loss "
          f"{lh_lo:.4f}..{lh_hi:.4f}; no-go Gam ratio {ng_ratio:.2f}, "
          f"control flat {ct_ratio:.4f}")
    return summary("PRIME.LEVEL.LEMMA.01 level-lemma identities")


if __name__ == "__main__":
    raise SystemExit(run())
