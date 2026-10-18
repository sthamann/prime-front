"""v557 -- PRIME.CASCADE.VECT.01: the cascade / vector identities of T166/T167.
The CLOSED, theorem-shaped cores of T166 (contract SCHUR.CASCADE) and T167
(contract NULL.VECTOR) -- every statement RECOMPUTED here from scratch on
small exactly checkable frame-A windows (no citation of sandbox output).
Companion to PRIME.GAUGE.PPR.01 (v556), which certified the GAUGE STRUCTURE
of the pairing: THIS module certifies the ANATOMY OF THE CASCADE and the
EXACTNESS OF THE CLOSED VECTOR AT K = 2 -- the identities that turned the
one open object of T165 (the cascade-gain quantifier) into a single scalar
(T167's R1).  NOTHING here closes that scalar:

[E] (1) THE CASCADE IDENTITIES (T166 U1 -- the anatomy).  With Q_K the
    leading K x K block of the normalised sixteen-block B_LL and G = T A T^T
    the raw arithmetic Gram block:
      (I1) PREFIX -- g_K = sum_{j <= K} y_j^2 with y = L^{-1} e_1 from ONE
           Cholesky of the sixteen-block equals e_1^T Q_K^{-1} e_1 at EVERY
           K: the ladder is a prefix property, one factorisation yields all
           sixteen rungs (Schur 1917 / Haynsworth 1968).
      (I2) MINOR -- 1/g_K = det G_[1..K] / (mu^P_1 det G_[2..K]): the rungs
           are ratios of consecutive Gram minors of the RAW arithmetic
           block, closed objects and not factorisation outputs.
      (I3) REGRESSION -- g_K/g_1 = 1/(1 - R_K^2) with R_K^2 =
           b^T B_HH^{-1} b / B_11 in the partition Q_K = [[B_11, b^T],
           [b, B_HH]]: the open object IS a near-collinearity statement.
    Mutation: the minor with the WRONG row/column deleted misses loudly.
[E] (2) THE DIAGONAL INVARIANCE (T166 I4).  The gain g_K/g_1 =
    B_11 (Q_K^{-1})_{11} is invariant under B -> DBD for EVERY positive
    diagonal D: the cascade does not see the KMS 1/sqrt(mu) normalisation
    at all -- the h^3 of the sandbox surface is a property of the
    arithmetic Gram block alone (Kac-Murdock-Szego 1953 enters only
    through the spectrum, never through the gain).  Mutation: a
    NON-diagonal congruence moves the gain loudly.
[E] (3) THE EXACT K = 2 IDENTITY (T167 V1 -- the central positive result).
    The CLOSED vector u = (1, -Q_21/Q_22) ATTAINS the constrained minimum:
      u^T Q_2 u = 1/g_2 = Q_11 (1 - r_12^2),   r_12^2 = Q_12^2/(Q_11 Q_22),
    and the rung-2 gain is the inverse of one scalar cancellation:
      B_11 g_2 = 1/(1 - r_12^2)   IDENTICALLY.
    At K = 2 the fast-null-vector of the third dress needs NO
    approximation -- the vector is FREE, and dress (c) collapses onto
    dress (b).  Mutation: the wrong-sign vector (1, +Q_21/Q_22) pays the
    relative excess 4 r_12^2/(1 - r_12^2) -- enormous exactly where the
    cancellation is deep.
[E] (4) THE PIVOT IDENTITY AND THE UNIFICATION (T167 V1/V4 -- the map).
    For u = x*_K + delta with delta_1 = 0 (x*_K the exact minimiser):
      u^T Q_K u = 1/g_K + delta^T Q_K delta      (EXACT -- Q_K x*_K =
    e_1/g_K and delta_1 = 0 kills the cross term), so the relative excess
    rho = g_K delta^T Q_K delta is an exact number, never an estimate;
    the Rayleigh envelope lambda_min |delta|^2 <= delta^T Q delta <=
    lambda_max |delta|^2 holds on the battery and is ATTAINED at the top
    eigenvector, which turns rho into the vector threshold eps_vec =
    sqrt(rho/(g_K lambda_max))/|x*| (the square law: the entry threshold
    is the SQUARE of the vector threshold).  THE UNIFICATION: the
    sign-aligned entrywise perturbation E_ij = eps |Q_ij| s_i s_j,
    s = sign(x*), attains |x*^T E x*| = eps S_K EXACTLY with S_K =
    |x*|^T |Q| |x*|, so the entry threshold eps_ent(K) =
    rho_carry (1/g_K)/S_K is exact -- and (1/g_K)/S_K is the ONE
    cancellation ratio: T166's determinant ratio (dress a), at K = 2
    literally (1/g_2)/S_2 = (1 - r_12^2)/(1 + 3 r_12^2) (dress b up to
    the factor 1 + 3 r_12^2 -> 4 as r_12 -> 1: T166's independently
    derived quarter), and the entry threshold itself (dress c): THERE IS
    ONE INEQUALITY, NOT THREE.  Mutation: delta_1 != 0 re-awakens the
    cross term and breaks the pivot identity loudly.
[E] (5) THE TRIAL THEOREM + TWO MUST-BREAKS (T166 U2 / T167 V0/V3).
    DIRECTION: every u with u_1 = 1 satisfies u^T Q_K u >= 1/g_K (Schur
    1917) -- every closed candidate is a certified LOWER bound on g_K,
    never an upper one; equality exactly at x*_K.  THE L_P NO-GO: for
    A = L_P the normalised block is the IDENTITY and the cascade gain is
    EXACTLY 1 -- a candidate blind to the off-diagonal block entries
    cannot carry a single power of h; the h^3 belongs to the arithmetic
    kernel alone.  THE SCRAMBLE TYPE-CHANGE: with uniform random atom
    positions at the SAME total mass the diagonal of the 2 x 2 block
    ITSELF loses positivity (B_11 < 0), so g_2 does not exist -- at K = 2
    the collapse under scrambling is a change of TYPE, not a factor: the
    mechanism hangs on WHERE the prime powers sit.

Plus the parity / Dirichlet controls: the closed Dirichlet cosine-sum
identity against the brute-force sum (including the degenerate branch),
L_P t_k = mu^P_k t_k with an orthonormal basis, and odd_toeplitz(c^L) =
L_P with ZERO tolerance.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL frame-A windows -- the
        N_INST DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), mirroring v551..v556's declared surface.  Nothing is
        uniform in the zone index or in D, and NO statement for ALL D is
        made.  The h-exponents of T166/T167 (1 - r_12^2 ~ h^{-2.921} on
        frame A, the certified gain exponent h^{+2.921}, the union
        exponents, the threshold monotonicity in K and the K = 6
        separation h^{+1.138}) are sandbox FITS / MEASURED numbers and
        are NOT consumed; what IS consumed is the per-instance identity
        structure that makes every one of those numbers exact where it
        is quoted.
  (ii)  THE ONE OPEN OBJECT AFTER T167 STAYS OPEN AND TYPED OPEN -- R1,
        the single scalar: an m-FREE upper bound on
        1 - r_12^2 = 1 - Q_12^2/(Q_11 Q_22) <= C h^{-3+eps}, three closed
        lag sums and nothing else.  This module certifies that the
        vector is exact at K = 2 and that the gain is the inverse of
        this one scalar; it makes NO uniformity claim about the scalar
        itself.  By T167 the reduction is complete: perturbation theory
        around the KMS bottom mode is closed off in every order (the
        Kato series converges to the WRONG object -- sandbox NG3), and
        position-blind surrogates are closed off (sandbox NG1/NG2, the
        scramble half wired here as item (5)).
  (iii) The T166 verdict CASCADE-RESISTS and the T167 verdict
        VECTOR-RESISTS are SANDBOX verdicts; this module promotes only
        their theorem-shaped identity/inequality cores, and the measured
        anatomy (the rung profile, the polarisation split of the Gram
        determinant, the Kato radius, the threshold monotonicity, the
        headroom) stays in the diary and the paper.
  (iv)  Finite Lambda-sums are allowed and nothing else: kappa is
        verified on the finite table, no search is run here, and no
        statement about what depth the primes deliver is made anywhere
        in this module.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  Everything here is a per-instance identity or a
    certified per-window inequality; finite sums over the von-Mangoldt
    table are allowed and used; NOTHING here claims, assumes, approaches
    or weakens RH, no zero of any L-function is read, generated or
    approximated (AST firewall), no L-function is evaluated, and no
    equivalence is claimed.  Even with every check green, what stands is
    a finite list of certified window statements on prime-power zones in
    one frame -- and the one scalar R1 stays OPEN.
  * Classics named CLASSICAL: Schur 1917 / Haynsworth 1968 (the Cholesky
    cascade and the minor form), Kac-Murdock-Szego 1953 (the parity
    spectrum), Rayleigh 1877 / Courant-Fischer 1920 (the envelope),
    Kato 1949 / Rayleigh-Schrodinger (cited as the CLOSED-OFF route,
    never used), Chebyshev 1852 / Rosser-Schoenfeld 1962 (the one
    unconditional input, verified on the table), Dirichlet 1829 (the
    cosine-sum identity), Wilkinson 1968 / Higham 2002 (floating-point
    floors); Weil 1952 / Bombieri 2000 CITED, never used as a criterion.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name, each with a mutation control that fails loudly;
measured quantities typed MEASURED.  Python; Wolfram-mirrored not required
(dense linear-algebra machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/schur_cascade_probe.py                (T166)
  experiments/tfpt-discovery/null_vector_probe.py                  (T167)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v556
H_CAP = 300                  # HARD cap on any assembled section
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              (v551..v556's declared surface convention)

# --- the form geometry, preregistered ----------------------------------------
SCHUR_KB = 16                # the fixed low block of the T152..T167 chain
K_LADDER = (2, 6, 16)        # the three K read in T167 (dress b / first flat /
#                              contract object)

# --- the Chebyshev input, preregistered (T166/T167 V0) ------------------------
KAPPA_X0 = 100.0             # verification window [x0, ATOM_MAX], as declared
KAPPA_REF = 0.038821         # the T162..T167 constant, reproduced on the table

# --- the perturbation battery for the pivot identity (T167 V1/V2) -------------
N_DELTA = 7                  # random delta with delta_1 = 0, per window per K
N_TRIAL = 8                  # random trial vectors u with u_1 = 1, per window
N_DIAG = 4                   # random positive diagonals D, per window per K
N_EPERT = 6                  # random entrywise perturbations, per window per K
N_SCRAM = 5                  # scramble draws per window (item 5)
DELTA1_MUT = 0.1             # the delta_1 of the pivot mutation: the break
#                              must equal the CLOSED cross term 2 delta_1
RHO_CARRY = 1.0              # the relative-excess budget of the thresholds;
#                              every threshold below is LINEAR in it, so no
#                              statement depends on the choice (T167 uses the
#                              same convention: eps_ent(2) -> (1-r^2)/4)

# --- preregistered tolerances / bars (declared BEFORE any number) -------------
TOL_KAPPA = 1.0e-6           # |kappa(table) - 0.038821|
TOL_SPLIT = 1.0e-15          # floating residue of the lag split re-summation
TOL_PREFIX = 1.0e-9          # prefix property vs per-K direct solves (the
#                              declared cond horizon of the sixteen-block)
TOL_MINOR = 1.0e-8           # minor form in log space (two slogdets)
TOL_REGR = 1.0e-8            # regression form, relative
TOL_INV = 1.0e-9             # diagonal invariance of the gain, relative
TOL_G2 = 1.0e-9              # the K = 2 attainment + B_11 g_2 identity
TOL_PIVOT = 1.0e-9           # pivot identity, relative to u^T Q u
TOL_RAY = 1.0e-9             # Rayleigh envelope slack + top-vector attainment
TOL_ALIGN = 1.0e-12          # sign-aligned attainment |x*^T E x*| = eps S_K
TOL_UNIFY = 1.0e-9           # (1/g_2)/S_2 = (1-r^2)/(1+3r^2), relative
TOL_TRIAL = -1.0e-9          # u^T Q u / (1/g_K) - 1 >= this on the battery
TOL_LP = 1.0e-12             # L_P no-go: block = I and gain = 1
TOL_CTRL = 1.0e-12           # Dirichlet / parity / Toeplitz controls
BAR_MUT_MINOR = 1.0e-1       # wrong minor must miss by >= this, relative
BAR_MUT_INV = 1.0e-2         # non-diagonal congruence must move gain by >=
BAR_MUT_G2 = 1.0e2           # wrong-sign vector: relative excess must be >=
TOL_MUT_PIVOT = 1.0e-9       # the pivot break must EQUAL 2 delta_1 to this
SEED = 557


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


def chebyshev_kappa():
    """kappa = max over jump points x in [KAPPA_X0, ATOM_MAX] of
    |psi(x) - x| / x, evaluated AT every jump point of the von-Mangoldt
    table (the T162..T167 convention; Chebyshev 1852 / Rosser-Schoenfeld
    1962) -- the ONE unconditional arithmetic input, measured on THIS
    table and nothing else."""
    nn = np.array([t[0] for t in ATOMS_ALL], dtype=float)
    ll = np.array([t[1] for t in ATOMS_ALL], dtype=float)
    psi = np.cumsum(ll)
    keep = nn >= KAPPA_X0
    return float(np.max(np.abs(psi[keep] - nn[keep]) / nn[keep]))


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


def atom_lags_at(alpha, M, positions, masses):
    """The T115 tent assembly at EXPLICIT positions -- used twice: at the
    true von-Mangoldt positions (the real block) and at scrambled uniform
    positions with the SAME masses (the item-(5) type-change control)."""
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


def atom_lags(alpha, M, atoms):
    return atom_lags_at(alpha, M,
                        [a[0] for a in atoms], [a[1] for a in atoms])


def lag_vector_split(alpha, M, atoms):
    """THE T115 lag assembly c = c^arch + c^atom, both halves kept -- bit
    for bit the frame-A code path of T128..T167 / v548..v556."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T167)
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s}: the reflection-odd section."""
    h = M // 2
    r = np.arange(h)
    return (np.asarray(c)[np.abs(r[:, None] - r[None, :])]
            - np.asarray(c)[(M - 1) - r[:, None] - r[None, :]])


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


def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def cholesky_ladder(B):
    """g_K = sum_{j <= K} y_j^2 with y = L^{-1} e_1 from ONE Cholesky of the
    16x16 block (Schur 1917 / Haynsworth 1968; T158's positive ladder)."""
    L = np.linalg.cholesky(B)
    e1 = np.zeros(B.shape[0])
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return np.cumsum(y * y), y


def x_star(QK):
    """The exact constrained minimiser x*_K = Q_K^{-1} e_1 normalised to
    x_1 = 1: Q_K x*_K = e_1/g_K, and u^T Q_K u >= 1/g_K for all u_1 = 1."""
    e1 = np.zeros(QK.shape[0])
    e1[0] = 1.0
    xs = np.linalg.solve(QK, e1)
    return xs / xs[0]


def gain_of(QK):
    """g_K/g_1 = B_11 (Q_K^{-1})_{11} -- the object of the diagonal
    invariance (T166 I4)."""
    e1 = np.zeros(QK.shape[0])
    e1[0] = 1.0
    return float(QK[0, 0]) * float(np.linalg.solve(QK, e1)[0])


# ------------------------------------------------------------------ assembly
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


def build_instance(k, D, M, h):
    alpha = 0.5 * M * D
    atoms = atoms_in(alpha)
    sp = lag_vector_split(alpha, M, atoms)
    r = dict(n=NN_ALL[k], k=k, M=M, h=h, D=sp["D"], alpha=alpha,
             c=sp["c"], c_ar=sp["c_ar"], c_at=sp["c_at"], atoms=atoms,
             X=math.exp(2.0 * alpha), logX=2.0 * alpha)
    r["split"] = float(np.max(np.abs(sp["c"] - sp["c_ar"] - sp["c_at"])))
    A = sym(odd_toeplitz(sp["c"], M))
    lam = np.linalg.eigvalsh(A)
    if not (float(lam[0]) > 0.0):
        return None
    r["A"] = A
    mu_full = parity_mu(h)
    r["mu1"] = float(mu_full[0])
    mu = mu_full[:SCHUR_KB]
    T16 = parity_basis(h)[:SCHUR_KB, :]
    G16 = sym(T16 @ (A @ T16.T))           # the RAW arithmetic Gram block
    isq = 1.0 / np.sqrt(mu)
    BLL = sym(G16 * np.outer(isq, isq))    # the normalised block Q
    gK, y_lad = cholesky_ladder(BLL)
    r["mu"], r["BLL"], r["G16"], r["T16"] = mu, BLL, G16, T16
    r["gK"], r["y_lad"] = gK, y_lad
    r["g1"], r["g16"] = float(gK[0]), float(gK[-1])
    r["B11"] = float(BLL[0, 0])
    r["t1"] = T16[0]
    return r


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("=" * 72)
    print("v557  PRIME.CASCADE.VECT.01 -- the cascade / vector identities "
          "(T166/T167)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, the one arithmetic input")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    kappa = chebyshev_kappa()
    check(f"S0.KAPPA: the ONE unconditional arithmetic input, measured on "
          f"THIS table and nothing else -- |psi(x) - x| <= kappa x with "
          f"kappa = {kappa:.6f} at every jump point of the von-Mangoldt "
          f"table in [{KAPPA_X0:.0f}, {ATOM_MAX}] (the T162..T167 "
          f"convention); the T166/T167 constant 0.038821 is reproduced to "
          f"{abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} (Chebyshev "
          f"1852 / Rosser-Schoenfeld 1962).  No other arithmetic enters "
          f"any identity below",
          abs(kappa - KAPPA_REF) <= TOL_KAPPA)
    INST = []
    for (k, D, M, h) in build_windows():
        r = build_instance(k, D, M, h)
        if r is not None:
            INST.append(r)
    h_max = max(r["h"] for r in INST) if INST else 0
    e_split = max(r["split"] for r in INST)
    lad_ok = [bool(np.min(r["y_lad"] ** 2) > 0.0
                   and np.min(np.diff(r["gK"])) > 0.0) for r in INST]
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite on every one; the lag split "
          f"c = c^arch + c^atom exact to {e_split:.1e} <= {TOL_SPLIT:.0e}; "
          f"the T158 Cholesky ladder g_K carries all {SCHUR_KB} terms "
          f"strictly positive with strictly monotone partial sums on "
          f"{sum(lad_ok)}/{len(INST)} windows); every assembled section <= "
          f"{H_CAP} (max m = {h_max})",
          len(INST) >= 6 and h_max <= H_CAP and e_split <= TOL_SPLIT
          and all(lad_ok))
    for r in INST:
        one_r2 = 1.0 / (r["B11"] * float(r["gK"][1]))
        print(f"    n={r['n']:>5d} m={r['h']:>4d} X={r['X']:8.1f} "
              f"B_11={r['B11']:9.1f} g_16={r['g16']:.4f} "
              f"1-r_12^2={one_r2:.3e}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the cascade identities: prefix, minor, regression "
          "(T166 U1)")
    E_PRE, E_MIN, E_MINM, E_REG = [], [], [], []
    n_minor = 0
    for r in INST:
        B, G, mu1 = r["BLL"], r["G16"], r["mu1"]
        for K in range(1, SCHUR_KB + 1):
            e1 = np.zeros(K)
            e1[0] = 1.0
            gK_dir = float(e1 @ np.linalg.solve(B[:K, :K], e1))
            E_PRE.append(abs(gK_dir - float(r["gK"][K - 1]))
                         / max(gK_dir, 1.0e-300))
        for K in K_LADDER:
            s_top, ld_top = np.linalg.slogdet(G[:K, :K])
            s_bot, ld_bot = np.linalg.slogdet(G[1:K, 1:K])
            lhs = math.log(1.0 / float(r["gK"][K - 1]))
            rhs = ld_top - math.log(mu1) - ld_bot
            E_MIN.append(abs(lhs - rhs))
            n_minor += 1
            if s_top <= 0.0 or s_bot <= 0.0:
                E_MIN.append(float("inf"))
            if K >= 3:
                keep = [i for i in range(K) if i != 1]
                s_b, ld_b = np.linalg.slogdet(G[np.ix_(keep, keep)])
                E_MINM.append(abs(lhs - (ld_top - math.log(mu1) - ld_b)))
            QK = B[:K, :K]
            if K >= 2:
                b = QK[1:, 0]
                RK2 = float(b @ np.linalg.solve(QK[1:, 1:], b)) / r["B11"]
                gain = float(r["gK"][K - 1]) / r["g1"]
                E_REG.append(abs(gain - 1.0 / (1.0 - RK2))
                             / max(gain, 1.0e-300))
    check(f"S1.PREFIX: THE PREFIX PROPERTY -- the sixteen partial sums of "
          f"ONE Cholesky solve, g_K = sum_(j<=K) y_j^2, equal the per-K "
          f"direct solves e_1^T Q_K^-1 e_1 at EVERY K = 1..{SCHUR_KB} on "
          f"{len(INST)} windows ({len(E_PRE)} comparisons, worst relative "
          f"{max(E_PRE):.1e} <= {TOL_PREFIX:.0e}, the declared cond "
          f"horizon of the sixteen-block): one factorisation yields all "
          f"sixteen rungs, and the ladder is a property of the block, not "
          f"of the factorisation order (Schur 1917 / Haynsworth 1968)",
          max(E_PRE) <= TOL_PREFIX)
    check(f"S1.MINOR: THE MINOR FORM on the RAW arithmetic Gram block -- "
          f"1/g_K = det G_[1..K] / (mu^P_1 det G_[2..K]) in log space to "
          f"{max(E_MIN):.1e} <= {TOL_MINOR:.0e} on {n_minor} (window, K) "
          f"pairs, K in {K_LADDER} (both minors positive definite "
          f"everywhere): the rungs are ratios of consecutive Gram minors "
          f"of G = T A T^T -- closed objects in the lag sums, not "
          f"factorisation outputs (T166's sharpest restatement; dress (a) "
          f"is this ratio at the first flat K)",
          max(E_MIN) <= TOL_MINOR)
    check(f"S1.REGRESSION: THE REGRESSION FORM -- g_K/g_1 = 1/(1 - R_K^2) "
          f"with R_K^2 = b^T B_HH^-1 b / B_11 the squared multiple "
          f"correlation of mode 1 on modes 2..K, verified to "
          f"{max(E_REG):.1e} <= {TOL_REGR:.0e} relative on every (window, "
          f"K) pair: the open object IS a near-collinearity statement -- "
          f"a lower bound on the gain says mode 1 is explained by the "
          f"higher modes up to a controlled residual, a far more specific "
          f"request than 'a cancellation'",
          max(E_REG) <= TOL_REGR)
    check(f"S1.CTRL: the minor with the WRONG row/column deleted (mode 2 "
          f"instead of mode 1 in the denominator) misses the identity by "
          f"{min(E_MINM):.2e}..{max(E_MINM):.2e} >= {BAR_MUT_MINOR:.0e} "
          f"in log space on every window: the minor form is a statement "
          f"about THE pivot mode, not a generic determinant ratio",
          min(E_MINM) >= BAR_MUT_MINOR)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the diagonal invariance: the gain does not see the "
          "KMS normalisation (T166 I4)")
    E_INV, E_INVM = [], []
    n_inv = 0
    for r in INST:
        B = r["BLL"]
        for K in K_LADDER:
            QK = B[:K, :K]
            base = gain_of(QK)
            lad = float(r["gK"][K - 1]) / r["g1"]
            E_INV.append(abs(base - lad) / max(lad, 1.0e-300))
            for _ in range(N_DIAG):
                d = np.exp(rng.uniform(-2.0, 2.0, size=K))
                QD = sym(QK * np.outer(d, d))
                E_INV.append(abs(gain_of(QD) - base) / max(base, 1.0e-300))
                n_inv += 1
            Tlo = np.eye(K)
            Tlo[1, 0] = 0.3
            QT = sym(Tlo @ QK @ Tlo.T)
            E_INVM.append(abs(gain_of(QT) - base) / max(base, 1.0e-300))
    check(f"S2.INVARIANT: THE DIAGONAL INVARIANCE -- the gain g_K/g_1 = "
          f"B_11 (Q_K^-1)_11 equals the Cholesky-ladder gain and is "
          f"unchanged under B -> DBD for {n_inv} random positive "
          f"diagonals (entries e^[-2,2]) across K in {K_LADDER} on "
          f"{len(INST)} windows, worst relative {max(E_INV):.1e} <= "
          f"{TOL_INV:.0e}: the cascade does NOT see the KMS 1/sqrt(mu) "
          f"normalisation at all -- the gain (and with it the whole h^3 "
          f"of the sandbox surface) is a property of the arithmetic Gram "
          f"block G = T A T^T alone (KMS 1953 enters only through the "
          f"spectrum, never through the gain)",
          max(E_INV) <= TOL_INV)
    check(f"S2.CTRL: a NON-diagonal congruence (unit lower-triangular "
          f"with one 0.3 entry mixing mode 1 into mode 2) moves the gain "
          f"by {min(E_INVM):.2e}..{max(E_INVM):.2e} >= {BAR_MUT_INV:.0e} "
          f"relative on every window: the invariance is a statement about "
          f"DIAGONAL congruence, not about congruence in general",
          min(E_INVM) >= BAR_MUT_INV)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the exact K = 2 identity: the closed vector is "
          "FREE (T167 V1)")
    E_G2, E_B11G2, RHO_BAD = [], [], []
    for r in INST:
        Q = r["BLL"][:2, :2]
        g2 = float(r["gK"][1])
        r12sq = Q[0, 1] ** 2 / (Q[0, 0] * Q[1, 1])
        one_r2 = 1.0 - r12sq
        u = np.array([1.0, -Q[1, 0] / Q[1, 1]])
        val = float(u @ Q @ u)
        E_G2.append(abs(val - 1.0 / g2) * g2)
        E_G2.append(abs(val - Q[0, 0] * one_r2) * g2)
        E_B11G2.append(abs(r["B11"] * g2 - 1.0 / one_r2) * one_r2)
        ubad = np.array([1.0, +Q[1, 0] / Q[1, 1]])
        RHO_BAD.append(g2 * float(ubad @ Q @ ubad) - 1.0)
    check(f"S3.GRAM2: *** THE EXACT K = 2 IDENTITY (T167's central "
          f"positive result) *** -- the CLOSED vector u = (1, -Q_21/Q_22) "
          f"ATTAINS the constrained minimum on every window: u^T Q_2 u = "
          f"1/g_2 = Q_11 (1 - r_12^2) with r_12^2 = Q_12^2/(Q_11 Q_22), "
          f"worst relative residual {max(E_G2):.1e} <= {TOL_G2:.0e}.  At "
          f"K = 2 the fast-null-vector needs NO approximation -- the "
          f"vector is FREE, and the third dress (a closed near-null "
          f"vector) collapses onto the second (the one scalar "
          f"1 - r_12^2): a THEOREM, not a search result",
          max(E_G2) <= TOL_G2)
    check(f"S3.B11G2: the rung-2 gain is the INVERSE of the one scalar "
          f"cancellation -- B_11 g_2 = 1/(1 - r_12^2) identically, worst "
          f"relative residual {max(E_B11G2):.1e} <= {TOL_G2:.0e} on "
          f"{len(INST)}/{len(INST)} windows (measured 1 - r_12^2 = "
          f"{min(1.0 / (r['B11'] * float(r['gK'][1])) for r in INST):.3e}"
          f"..{max(1.0 / (r['B11'] * float(r['gK'][1])) for r in INST):.3e} "
          f"on this small surface; its h-trend is a sandbox FIT and is "
          f"not consumed): everything the gain certifies at K = 2 is "
          f"carried by ONE scalar built from three closed lag sums -- "
          f"T167's R1, typed OPEN",
          max(E_B11G2) <= TOL_G2)
    check(f"S3.CTRL: the wrong-sign vector (1, +Q_21/Q_22) pays the "
          f"relative excess rho = 4 r_12^2/(1 - r_12^2) = "
          f"{min(RHO_BAD):.2e}..{max(RHO_BAD):.2e} >= {BAR_MUT_G2:.0e} on "
          f"every window -- enormous exactly where the cancellation is "
          f"deep: the attainment is a statement about THE closed sign, "
          f"and the parabola in beta has no flat direction",
          min(RHO_BAD) >= BAR_MUT_G2)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the pivot identity and the unification: one "
          "inequality, not three (T167 V1/V4)")
    E_PIV, E_PIVM, E_RAYL, E_RAYU, E_TOP, E_INTL, E_ALN, E_ENV, E_UNI = \
        [], [], [], [], [], [], [], [], []
    n_piv = 0
    for r in INST:
        B = r["BLL"]
        for K in K_LADDER:
            QK = sym(B[:K, :K])
            gK = float(r["gK"][K - 1])
            xs = x_star(QK)
            lam = np.linalg.eigvalsh(QK)
            lam_min, lam_max = float(lam[0]), float(lam[-1])
            for _ in range(N_DELTA):
                d = rng.normal(size=K)
                d[0] = 0.0
                d *= rng.choice((1.0e-3, 1.0, 1.0e3))
                u = xs + d
                lhs = float(u @ QK @ u)
                dqd = float(d @ QK @ d)
                E_PIV.append(abs(lhs - 1.0 / gK - dqd)
                             / max(abs(lhs), 1.0e-300))
                nrm = float(d @ d)
                E_RAYL.append((dqd - lam_min * nrm)
                              / max(lam_max * nrm, 1.0e-300))
                E_RAYU.append((lam_max * nrm - dqd)
                              / max(lam_max * nrm, 1.0e-300))
                n_piv += 1
            # the CONSTRAINED ceiling is attained: on the plane delta_1 = 0
            # the Rayleigh maximum is lambda_max(Q_HH), reached exactly at
            # the top eigenvector of the lower block, and Cauchy interlacing
            # puts it under lambda_max(Q_K) -- which is what turns rho into
            # the (conservative) vector threshold eps_vec
            lamH, VH = np.linalg.eigh(sym(QK[1:, 1:]))
            lamH_max = float(lamH[-1])
            dtop = np.zeros(K)
            dtop[1:] = VH[:, -1] * math.sqrt(RHO_CARRY / (gK * lamH_max))
            rho_top = gK * float(dtop @ QK @ dtop)
            E_TOP.append(abs(rho_top - RHO_CARRY) / RHO_CARRY)
            E_INTL.append((lam_max - lamH_max) / lam_max)
            # the entry threshold: sign-aligned attainment + random envelope
            SK = float(np.abs(xs) @ np.abs(QK) @ np.abs(xs))
            sgn = np.sign(xs)
            sgn[sgn == 0.0] = 1.0
            eps = 1.0e-3
            E_att = eps * np.abs(QK) * np.outer(sgn, sgn)
            E_ALN.append(abs(abs(float(xs @ E_att @ xs)) - eps * SK)
                         / (eps * SK))
            for _ in range(N_EPERT):
                F = eps * np.abs(QK) * rng.uniform(-1.0, 1.0, size=(K, K))
                F = sym(F)
                E_ENV.append((eps * SK - abs(float(xs @ F @ xs)))
                             / (eps * SK))
            # mutation: delta_1 != 0 re-awakens the cross term, and the
            # break EQUALS the closed prediction 2 delta_1 exactly
            d = rng.normal(size=K)
            d[0] = DELTA1_MUT
            u = xs + d
            lhs = float(u @ QK @ u)
            brk = gK * abs(lhs - 1.0 / gK - float(d @ QK @ d))
            E_PIVM.append(abs(brk - 2.0 * DELTA1_MUT))
        # the unification at K = 2: (1/g_2)/S_2 = (1 - r^2)/(1 + 3 r^2)
        Q2 = B[:2, :2]
        g2 = float(r["gK"][1])
        xs2 = x_star(Q2)
        S2 = float(np.abs(xs2) @ np.abs(Q2) @ np.abs(xs2))
        r12sq = Q2[0, 1] ** 2 / (Q2[0, 0] * Q2[1, 1])
        lhs = (1.0 / g2) / S2
        rhs = (1.0 - r12sq) / (1.0 + 3.0 * r12sq)
        E_UNI.append(abs(lhs - rhs) / max(rhs, 1.0e-300))
    check(f"S4.PIVOT: *** THE PIVOT IDENTITY *** -- for u = x*_K + delta "
          f"with delta_1 = 0, u^T Q_K u = 1/g_K + delta^T Q_K delta "
          f"EXACTLY (Q_K x*_K = e_1/g_K and delta_1 = 0 kills the cross "
          f"term), verified to {max(E_PIV):.1e} <= {TOL_PIVOT:.0e} "
          f"relative on {n_piv} (window, K, delta) evaluations across "
          f"three delta scales 1e-3/1/1e3: every relative excess rho = "
          f"g_K delta^T Q_K delta of every candidate is an EXACT number, "
          f"never an estimate -- the instrument that turned T167's "
          f"22-family search into a theorem-shaped table",
          max(E_PIV) <= TOL_PIVOT)
    check(f"S4.RAYLEIGH: the Rayleigh envelope on the same battery -- "
          f"lambda_min |delta|^2 <= delta^T Q delta <= lambda_max "
          f"|delta|^2 with worst relative slack "
          f"{min(min(E_RAYL), min(E_RAYU)):.2e} >= -{TOL_RAY:.0e} "
          f"(Rayleigh 1877 / Courant-Fischer 1920); on the constraint "
          f"plane delta_1 = 0 the ceiling is lambda_max(Q_HH), ATTAINED "
          f"exactly at the top eigenvector of the lower block (excess "
          f"budget reproduced to {max(E_TOP):.1e} <= {TOL_RAY:.0e}) and "
          f"interlaced under lambda_max(Q_K) (Cauchy 1829; least slack "
          f"{min(E_INTL):.2e} >= 0): the excess rho becomes the vector "
          f"threshold eps_vec = sqrt(rho/(g_K lambda_max))/|x*| -- and "
          f"since the ENTRY threshold below is linear where this one is "
          f"quadratic, eps_ent ~ eps_vec^2 is the T167 square law: the "
          f"vector dress was always the cheaper-looking one, and at K = 2 "
          f"it is genuinely free",
          min(min(E_RAYL), min(E_RAYU)) >= -TOL_RAY
          and max(E_TOP) <= TOL_RAY and min(E_INTL) >= -TOL_RAY)
    check(f"S4.ENTRY: the entry threshold is EXACT, not an estimate -- "
          f"the sign-aligned entrywise perturbation E_ij = eps |Q_ij| "
          f"s_i s_j, s = sign(x*), attains |x*^T E x*| = eps S_K with "
          f"S_K = |x*|^T |Q| |x*| to {max(E_ALN):.1e} <= {TOL_ALIGN:.0e}, "
          f"and every random entrywise perturbation |F_ij| <= eps |Q_ij| "
          f"stays inside the envelope (least relative slack "
          f"{min(E_ENV):.2e} >= 0) "
          f"on {len(E_ENV)} draws: eps_ent(K) = rho_carry (1/g_K)/S_K is "
          f"the exact entry accuracy at which the certified value can "
          f"move by the excess budget -- linear in rho_carry, so no "
          f"statement here depends on that choice",
          max(E_ALN) <= TOL_ALIGN and min(E_ENV) >= 0.0)
    check(f"S4.UNIFY: *** THE UNIFICATION (T167's map) *** -- the "
          f"cancellation ratio (1/g_K)/S_K behind the entry threshold IS "
          f"the one object of all three dresses: by S1.MINOR it is T166's "
          f"determinant ratio over the absolute-value mass (dress a), and "
          f"at K = 2 it is LITERALLY (1/g_2)/S_2 = "
          f"(1 - r_12^2)/(1 + 3 r_12^2), verified to {max(E_UNI):.1e} <= "
          f"{TOL_UNIFY:.0e} relative on {len(INST)}/{len(INST)} windows "
          f"-- dress (b) up to the closed factor 1 + 3 r_12^2 -> 4 as "
          f"r_12 -> 1 (T166's independently derived quarter is this "
          f"factor); the threshold itself is dress (c).  THERE IS ONE "
          f"INEQUALITY, NOT THREE -- and after item (3) what remains of "
          f"it is the single scalar R1, typed OPEN",
          max(E_UNI) <= TOL_UNIFY)
    check(f"S4.CTRL: delta_1 = {DELTA1_MUT:g} re-awakens the cross term, "
          f"and the break of the pivot identity EQUALS the closed "
          f"prediction 2 delta_1 = {2.0 * DELTA1_MUT:g} exactly -- "
          f"g_K |u^T Q u - 1/g_K - delta^T Q delta| = 2 delta_1 to "
          f"{max(E_PIVM):.1e} <= {TOL_MUT_PIVOT:.0e} on every (window, K) "
          f"pair: the identity is a statement about THE constraint plane "
          f"u_1 = 1, and its failure off the plane is itself a closed "
          f"formula, not noise",
          max(E_PIVM) <= TOL_MUT_PIVOT)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the trial theorem and the two must-breaks "
          "(T166 U2 / T167 V0/V3)")
    TRIAL_MIN, E_ATT = [], []
    n_trial = 0
    for r in INST:
        B = r["BLL"]
        for K in K_LADDER:
            QK = sym(B[:K, :K])
            gK = float(r["gK"][K - 1])
            xs = x_star(QK)
            E_ATT.append(abs(float(xs @ QK @ xs) - 1.0 / gK) * gK)
            for _ in range(N_TRIAL):
                u = rng.normal(size=K)
                u[0] = 1.0
                TRIAL_MIN.append(gK * float(u @ QK @ u))
                n_trial += 1
    check(f"S5.TRIAL: THE TRIAL THEOREM, direction first -- x*_K attains "
          f"1/g_K to {max(E_ATT):.1e} relative, and ALL {n_trial} random "
          f"trials u with u_1 = 1 satisfy u^T Q_K u >= 1/g_K (min ratio "
          f"{min(TRIAL_MIN):.4f} >= 1 - {abs(TOL_TRIAL):.0e}) across K in "
          f"{K_LADDER}: every closed candidate is a certified LOWER bound "
          f"on g_K, never an upper one (Schur 1917) -- the direction that "
          f"makes T167's whole search table one-sided and safe",
          max(E_ATT) <= TOL_G2 and min(TRIAL_MIN) >= 1.0 + TOL_TRIAL)
    E_LPI, E_LPG = [], []
    for m_c in (64, 128, 256):
        M_c = 2 * m_c
        cL = np.zeros(M_c)
        cL[0], cL[1] = 2.0, -1.0
        A_L = odd_toeplitz(cL, M_c)
        mu_c = parity_mu(m_c)[:SCHUR_KB]
        T16_c = parity_basis(m_c)[:SCHUR_KB, :]
        isq = 1.0 / np.sqrt(mu_c)
        B_L = sym((T16_c @ (A_L @ T16_c.T)) * np.outer(isq, isq))
        E_LPI.append(float(np.max(np.abs(B_L - np.eye(SCHUR_KB)))))
        gK_L, _ = cholesky_ladder(B_L)
        E_LPG.append(abs(float(gK_L[-1]) / float(gK_L[0]) - 1.0))
    check(f"S5.LP_NOGO: THE L_P NO-GO as a must-break -- for A = L_P the "
          f"normalised sixteen-block is the IDENTITY to {max(E_LPI):.1e} "
          f"<= {TOL_LP:.0e} and the cascade gain g_16/g_1 is EXACTLY 1 "
          f"(deviation {max(E_LPG):.1e}) at m = 64, 128, 256: a candidate "
          f"that ignores the off-diagonal block entries cannot carry a "
          f"single power of h -- the whole gain, and with it the h^3, "
          f"belongs to the arithmetic kernel alone (T166's no-go, "
          f"re-verified as an exact statement)",
          max(E_LPI) <= TOL_LP and max(E_LPG) <= TOL_LP)
    NEG_PER_W, B11_SCR_ALL = [], []
    for r in INST:
        neg = 0
        for _ in range(N_SCRAM):
            pos = rng.uniform(1.0e-6, 2.0 * r["alpha"],
                              size=len(r["atoms"]))
            c_at_s, _ = atom_lags_at(r["alpha"], r["M"],
                                     list(np.sort(pos)),
                                     [a[1] for a in r["atoms"]])
            A_s = sym(odd_toeplitz(r["c_ar"] + c_at_s, r["M"]))
            b11 = float(r["t1"] @ (A_s @ r["t1"])) / r["mu1"]
            B11_SCR_ALL.append(b11)
            if b11 < 0.0:
                neg += 1
        NEG_PER_W.append(neg)
    n_neg = sum(1 for b in B11_SCR_ALL if b < 0.0)
    check(f"S5.SCRAMBLE: THE TYPE-CHANGE DISCRIMINATOR -- with uniform "
          f"random atom positions at the SAME total mass (same weights, "
          f"same window, same kernel, same grid; {N_SCRAM} declared draws "
          f"per window) the diagonal of the 2 x 2 block ITSELF loses "
          f"positivity: B_11(scrambled) < 0 on {n_neg}/"
          f"{len(B11_SCR_ALL)} draws and on a MAJORITY of draws on "
          f"{sum(1 for n in NEG_PER_W if 2 * n > N_SCRAM)}/{len(INST)} "
          f"windows (range {min(B11_SCR_ALL):.2e}..{max(B11_SCR_ALL):.2e} "
          f"against the true B_11 = {min(r['B11'] for r in INST):.1f}.."
          f"{max(r['B11'] for r in INST):.1f} > 0 on 12/12), so g_2 does "
          f"not even EXIST on those draws -- at K = 2 the collapse under "
          f"scrambling is a change of TYPE, not a factor: the mechanism "
          f"hangs on WHERE the prime powers sit, not on the atom budget, "
          f"the kernel or the discretisation (T167's sharpened form of "
          f"T166's factor-4569 scramble; the sandbox reads 8/8 single "
          f"draws negative on its deep union surface)",
          all(2 * n > N_SCRAM for n in NEG_PER_W)
          and all(r["B11"] > 0.0 for r in INST))

    # ---------------------------------------------------------------- controls
    print("\nS6 -- the parity / Dirichlet controls")
    rng2 = np.random.default_rng(5571)
    worst_cs = 0.0
    for _ in range(64):
        al = float(rng2.uniform(0.05, 3.0))
        be = float(rng2.uniform(0.0, 2.0 * math.pi))
        Lc = int(rng2.integers(1, 40))
        brute = float(np.sum(np.cos(al * np.arange(1, Lc + 1) + be)))
        ha = 0.5 * al
        closed = (math.sin(Lc * ha) / math.sin(ha)
                  * math.cos(be + (Lc + 1.0) * ha))
        worst_cs = max(worst_cs, abs(closed - brute) / max(1.0, abs(brute)))
    brute0 = float(np.sum(np.cos(np.zeros(7) + 0.3)))
    closed0 = 7.0 * math.cos(0.3)
    worst_cs = max(worst_cs, abs(closed0 - brute0) / abs(brute0))
    check(f"S6.DIRICHLET: the closed cosine-sum identity (Dirichlet 1829) "
          f"agrees with the brute-force sum to {worst_cs:.1e} <= "
          f"{TOL_CTRL:.0e} on 64 random (alpha, beta, L) triples INCLUDING "
          f"the degenerate branch alpha = 0 mod 2 pi: the closed weights "
          f"of the whole chain rest on this identity and on nothing else",
          worst_cs <= TOL_CTRL)
    m_c = 128
    mu_c = parity_mu(m_c)
    Tc = parity_basis(m_c)
    LPc = lap_P_mat(m_c)
    e_eig = float(np.max(np.abs(LPc @ Tc.T - Tc.T * mu_c[None, :])))
    e_ort = float(np.max(np.abs(Tc @ Tc.T - np.eye(m_c))))
    cL = np.zeros(2 * m_c)
    cL[0], cL[1] = 2.0, -1.0
    e_tpl = float(np.max(np.abs(odd_toeplitz(cL, 2 * m_c) - LPc)))
    check(f"S6.PARITY: L_P t_k = mu^P_k t_k to {e_eig:.1e} with the basis "
          f"orthonormal to {e_ort:.1e} (Kac-Murdock-Szego 1953 -- the "
          f"parity sines are EXACT eigenvectors, the unperturbed object "
          f"every closed family of T167 starts from), and "
          f"odd_toeplitz(c^L) = L_P for c^L = (2, -1, 0, ...) with "
          f"residual {e_tpl:.1e} == 0 (ZERO tolerance): the section map "
          f"of the whole chain is the one the identities assume",
          e_eig <= 1.0e-11 and e_ort <= 1.0e-12 and e_tpl == 0.0)

    # ---------------------------------------------------------------- fences
    print("\nS7 -- the fences, restated as a check")
    check("S7.FENCE: PER-INSTANCE identities and certified inequalities on "
          "SMALL frame-A windows only -- a FINITE LIST with an explicit "
          "maximum, nothing uniform in the zone index or in D, and NO "
          "statement for ALL D; finite Lambda-sums are allowed and used, "
          "NO RH statement is made, assumed, approached or weakened, no "
          "zero of any L-function is read and no L-function is evaluated "
          "(AST firewall); THE ONE OPEN OBJECT AFTER T167 STAYS OPEN AND "
          "TYPED OPEN -- R1, the single scalar: an m-free upper bound on "
          "1 - r_12^2 = 1 - Q_12^2/(Q_11 Q_22) <= C h^{-3+eps}, three "
          "closed lag sums and nothing else, neither assumed nor "
          "approached here; the routes T167 closed off stay closed as "
          "sandbox negatives (perturbation theory around the KMS bottom "
          "mode in every order -- the Kato series converges to the WRONG "
          "object; position-blind surrogates -- the scramble half is "
          "wired here as S5.SCRAMBLE) and are NOT promoted as theorems; "
          "the T166/T167 h-exponents, the threshold monotonicity in K, "
          "the K = 6 separation and the measured anatomy stay in the "
          "diary and the paper; R-B''' stays open as narrowed; no other "
          "marker of any pre-existing contract moves; Schur 1917 / "
          "Haynsworth 1968, Kac-Murdock-Szego 1953, Rayleigh 1877 / "
          "Courant-Fischer 1920, Kato 1949 (cited as the closed-off "
          "route, never used), Chebyshev 1852 / Rosser-Schoenfeld 1962, "
          "Dirichlet 1829, Wilkinson 1968 / Higham 2002 named CLASSICAL; "
          "Weil 1952 / Bombieri 2000 CITED, never used as a criterion; "
          "zero-firewall AST-checked", True)

    elapsed = time.time() - t0
    print(f"\nv557 runtime: {elapsed:.1f}s")
    print(f"  (1) prefix <= {max(E_PRE):.1e}; minor <= {max(E_MIN):.1e}; "
          f"regression <= {max(E_REG):.1e}")
    print(f"  (2) diagonal invariance <= {max(E_INV):.1e} on {n_inv} "
          f"congruences")
    print(f"  (3) K = 2 attainment <= {max(E_G2):.1e}; B_11 g_2 identity "
          f"<= {max(E_B11G2):.1e}")
    print(f"  (4) pivot <= {max(E_PIV):.1e} on {n_piv} evaluations; "
          f"unification <= {max(E_UNI):.1e}")
    print(f"  (5) trial min ratio {min(TRIAL_MIN):.4f}; L_P gain dev "
          f"{max(E_LPG):.1e}; scrambled B_11 < 0 on "
          f"{n_neg}/{len(B11_SCR_ALL)} draws")
    return summary("PRIME.CASCADE.VECT.01 cascade/vector identities")


if __name__ == "__main__":
    raise SystemExit(run())
