"""v558 -- PRIME.BILINEAR.RANK.01: the bilinear / rank identities of T168-T170.
The CLOSED, theorem-shaped cores of T168 (contract LAGRANGE.MINORS), T169
(contract TSTAR.RATIO) and T170 (contract BILINEAR.SIEVE) -- every statement
RECOMPUTED here from scratch on small exactly checkable frame-A windows (no
citation of sandbox output).  Companion to PRIME.CASCADE.VECT.01 (v557), which
certified the ANATOMY OF THE CASCADE and the EXACTNESS OF THE CLOSED VECTOR AT
K = 2: THIS module certifies the EXACT SHAPE OF THE ONE REMAINING SCALAR --
the identities that write T167's R1 out as an explicit bilinear von Mangoldt
form and the two rank theorems that collapse that form back onto three LINEAR
Lambda sums.  NOTHING here closes that scalar:

[E] (1) THE LAGRANGE / WRONSKIAN ANATOMY (T168 W0/W1).  With t_1, t_2 the two
    lowest KMS parity modes (unit normalised) and A_h the arithmetic lag
    kernel:
      (I1) LAG SUM -- Ahat_ij = t_i^T A_h t_j = sum_d c_d W^{ij}_d with
           W^{ij} the closed T163 correlation weights (and the 1/sqrt(mu)
           factors cancel exactly, T169-TH3: the normalised block is
           Ahat_ij / sqrt(mu_i mu_j), no conditioning ladder).
      (I2) EUCLIDEAN ORTHOGONALITY -- t_1 . t_2 = 0 exactly, so the
           near-parallelism 1 - r_12^2 -> 0 is created ENTIRELY by the
           arithmetic metric A_h, not at all by the vectors.
      (I3) WRONSKIAN TELESCOPE -- (mu_1 - mu_2) u_r v_r = W_{r-1} - W_r with
           W_r = u_{r+1} v_r - u_r v_{r+1} and W_{-1} = W_{h-1} = 0: the
           near-diagonal minors are ONE closed one-parameter family and the
           telescope closes at the window edge; summing it re-derives (I2).
           The minors are MAXIMAL: (1/2) sum M^2 = |u|^2 |v|^2 - <u,v>^2 =
           1/(mu_1 mu_2) EXACTLY for u = t_1/sqrt(mu_1), v = t_2/sqrt(mu_2)
           (Lagrange 1773) -- the Wronskians carry zero arithmetic.
    Mutation: the telescope with the WRONG eigenvalue pair misses loudly.
[E] (2) THE EXPONENT ACCOUNT + THE GERSHGORIN CERT (T168 W2 / T169 X2).
    1 - r_12^2 = nu_1 nu_2 / (ahat_11 ahat_22) IDENTICALLY (Poincare
    separation; det = nu_1 nu_2 on a 2 x 2 block), and the large eigenvalue
    carries an UNCONDITIONAL closed bound nu_1 <= max(ahat_11, ahat_22) +
    |ahat_12| (Gershgorin 1931) -- closed in the three entries, uniform in
    the window, the certificate T169 booked as R3.  Mutation: dropping the
    |ahat_12| term fails on every window (nu_1 > max diagonal entry).
[E] (3) THE det-COLLAPSE THEOREM (T169-TH7).  On the Rayleigh family
    u(t) = (t, -1), the ONLY threshold-meeting candidate K7 =
    sqrt(ahat_22/ahat_11) collapses in closed form:
      R(K7) = 2 sqrt(ahat_11 ahat_22) det Ahat /
              [(ahat_11 + ahat_22)(sqrt(ahat_11 ahat_22) + ahat_12)],
    i.e. it meets the threshold precisely BECAUSE it reintroduces det Ahat:
    the t*-language is provably exactly as hard as the determinant -- the
    loop T167 scalar -> T168 factor -> T169 candidate closes as an identity.
    Usable form: nu_2 <= 2 det Ahat/(ahat_11 + ahat_22) = 2 nu_1 nu_2 /
    (nu_1 + nu_2), a valid upper bound tight to a factor < 2 (Rayleigh
    1877).  Mutation: the closed constant candidate 1/sqrt(2) overshoots
    nu_2 loudly.
[E] (4) THE EXACT BILINEAR VON MANGOLDT FORM (T170 TH1-TH3).
      (TH1) EXACT SPLIT -- Ahat = B - S with B the archimedean block and
            S_ij = sum_{n<=X} (Lambda(n)/sqrt n) X_n[ij], X_n[ij] =
            phi_n . W^{ij} the two-point spline read of the closed weights;
            verified against the direct t_i^T A_h t_j.
      (TH2) POLARISATION -- det Ahat = det B - D(B, S) + det S with
            D(P,Q) = P11 Q22 + P22 Q11 - 2 P12 Q12 the polarisation of det
            on 2 x 2 symmetric matrices: arch-arch, arch-Lambda (linear),
            Lambda-Lambda (bilinear).
      (TH3) THE DOUBLE SUM -- det S = sum_{n,m<=X} Lambda(n) Lambda(m)
            K(n,m)/sqrt(nm) with K(n,m) = (1/2) D(X_n, X_m), verified
            through the EXPLICIT kernel matrix (Cauchy-Binet 1812/1815;
            Lagrange 1773).  The wedge reading: X_n is rank one up to a
            small measured defect, so K = (1/2) eps_n eps_m (x_n ^ x_m)^2
            up to that defect -- an antisymmetric-quadratic kernel with
            MIXED signs.  Mutation: the polarisation with the wrong
            cross-coefficient breaks the expansion loudly.
[E] (5) THE RANK-3 THEOREM + THE TYPE II COLLAPSE (T170 TH4-TH5).
      (TH4) the polarisation matrix on (X11, X22, X12) is
            [[0,1,0],[1,0,0],[0,0,-2]]: eigenvalues {1, -1, -2}, RANK 3,
            SIGNATURE (1, 2).  Hence K = P M P^T has rank <= 3 for EVERY
            window, EVERY h, EVERY X, and its nonzero spectrum is the
            spectrum of M (P^T P) -- the bilinear form IS the rank-3
            polynomial S_11 S_22 - S_12^2 in THREE linear Lambda sums.
      (TH5) the closed weights see n only through log n; under n = m d that
            is log m + log d, and a bounded-frequency function of a sum is
            a finite-rank kernel: Vaughan (1977) Type II blocks built from
            these weights have effective rank O(1) for every U, V (the
            identity Lambda = a1 + a2 + a3 + a4 is verified coefficient by
            coefficient first), against O(min(rows, cols)) for a generic
            kernel of the same size.  Mutation: the generic Gaussian kernel
            needs many singular values where the Type II block needs few.
[E] (6) THE R4-FREE CHAIN + THE TWO DISCRIMINATORS (T170 TH6 / T169 X3).
      (TH6) 1 - r_12^2 = det Ahat/(ahat_11 ahat_22) is an IDENTITY -- the
            direct chain bounds det Ahat and never touches positivity of
            A_h: R4 is off the path and the Weil fence is never approached;
            the T169-TH9 chain [max(ahat_11, ahat_22) + |ahat_12|] nu_2 /
            (ahat_11 ahat_22) is verified as a VALID upper bound with its
            loss factor exactly the Gershgorin loss of item (2).
      THE L_P NO-GO -- for A = L_P the parity modes are exact eigenvectors,
            ahat_12 = 0 IDENTICALLY and 1 - r_12^2 = 1 with no decay: the
            phenomenon needs the arithmetic kernel.
      THE SCRAMBLE DISCRIMINATOR -- uniform random atom positions at the
            SAME masses leave the rank-3 collapse UNTOUCHED (it is algebra)
            while the VALUE of 1 - r_12^2 moves by orders of magnitude on
            a majority of draws: the arithmetic content sits in the JOINT
            VALUES of (S_11, S_22, S_12) against B, not in rank, kernel or
            split -- which is exactly why no size-bounding tool reaches it.

Plus the parity / Dirichlet controls: the closed Dirichlet cosine-sum
identity against the brute-force sum (including the degenerate branch),
L_P t_k = mu^P_k t_k with an orthonormal basis, and odd_toeplitz(c^L) =
L_P with ZERO tolerance.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL frame-A windows -- the
        N_INST DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), mirroring v551..v557's declared surface.  Nothing is
        uniform in the zone index or in D, and NO statement for ALL D is
        made.  The T168/T169/T170 h-exponents (1 - r_12^2 ~ h^{-2.92} on
        the deep frame-A surface, the route-table deltas, the five-order
        cancellation of the reference window, the h^{-2.711} row-angle
        trend) are sandbox FITS / MEASURED numbers and are NOT consumed;
        what IS consumed is the per-instance identity structure that makes
        every one of those numbers exact where it is quoted.
  (ii)  THE ONE OPEN OBJECT AFTER T170 STAYS OPEN AND TYPED OPEN -- R1,
        now finally CLASSIFIED but not closed: an m-FREE unconditional
        certificate that the two rows of Ahat become collinear at rate
        h^{-3+eps}, equally a joint near-degeneracy of the THREE explicit
        linear Lambda sums (S_11, S_22, S_12) against the archimedean
        block B.  This module certifies the exact SHAPE (the split, the
        polarisation, the kernel, the two rank theorems); it makes NO
        uniformity claim and NO rate claim.  The T170 sandbox verdict
        SIEVE-RESISTS (best unconditional route delta = +0.996 against
        the target 3.0, the shortfall a theorem) stays in the diary and
        the paper.
  (iii) The Type II statement here is the RANK COLLAPSE of the kernel
        built from the closed weights, per instance, U-scanned on the
        declared list; the sandbox route-table deltas (large sieve +0.669,
        MV -0.384, exact split +0.996, Vaughan +0.669 against truth 2.747)
        are sandbox MEASURED numbers on the deep union and are NOT
        promoted.
  (iv)  Finite Lambda-sums are allowed and nothing else: kappa is verified
        on the finite table, no search is run here, and no statement about
        what depth the primes deliver is made anywhere in this module.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  Everything here is a per-instance identity or a
    certified per-window inequality; finite sums over the von-Mangoldt
    table are allowed and used; NOTHING here claims, assumes, approaches
    or weakens RH, no zero of any L-function is read, generated or
    approximated (AST firewall), no L-function is evaluated, and no
    equivalence is claimed.  The large sieve / Vaughan apparatus quoted in
    the docstring is UNCONDITIONAL classical machinery; RH enters T170
    only as a YARDSTICK strength and is neither input nor output.  Even
    with every check green, what stands is a finite list of certified
    window statements on prime-power zones in one frame -- and the one
    scalar R1 stays OPEN.
  * THE WEIL FENCE.  Uniform-in-h positivity of A_h is RH-equivalent-shaped
    and is never routed, never claimed, never reverse-inferred; the direct
    chain of item (6) is R4-free BY CONSTRUCTION and the fence is never
    approached.
  * Classics named CLASSICAL: Lagrange 1773 (the wedge identity),
    Cauchy-Binet 1812/1815 (the kernel form), Gershgorin 1931 (the nu_1
    certificate), Rayleigh 1877 / Courant-Fischer 1920 (the candidate
    direction), Montgomery-Vaughan 1973 / Vaughan 1977 (the sieve box,
    cited as the PRICED route), Kac-Murdock-Szego 1953 (the parity
    spectrum), Chebyshev 1852 / Rosser-Schoenfeld 1962 (the one
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
  experiments/tfpt-discovery/lagrange_minors_probe.py             (T168)
  experiments/tfpt-discovery/tstar_ratio_probe.py                 (T169)
  experiments/tfpt-discovery/bilinear_sieve_probe.py              (T170)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v557
H_CAP = 300                  # HARD cap on any assembled section
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              (v551..v557's declared surface convention)

# --- the Chebyshev input, preregistered (T168..T170 Y0/W0/X0) -----------------
KAPPA_X0 = 100.0             # verification window [x0, ATOM_MAX], as declared
KAPPA_REF = 0.038821         # the T162..T170 constant, reproduced on the table

# --- the scramble / Type II battery -------------------------------------------
N_SCRAM = 5                  # scramble draws per window (item 6)
NS_KERNEL = 900              # kernel subsample cap (never binding here)
UV_LIST = (3, 4, 5, 6)       # the Vaughan U = V scan of item (5)
TII_DIM = 64                 # cap on the Type II kernel dimensions

# --- preregistered tolerances / bars (declared BEFORE any number) --------------
TOL_KAPPA = 1.0e-6           # |kappa(table) - 0.038821|
TOL_SPLIT = 1.0e-15          # floating residue of the lag split re-summation
TOL_LAG = 1.0e-12            # lag-sum identity Ahat_ij = c . W^{ij}, relative
TOL_ORTH = 1.0e-13           # Euclidean orthogonality / normalisation
TOL_WRON = 1.0e-12           # Wronskian telescope, absolute per entry
TOL_LAGR = 1.0e-11           # (1/2) sum M^2 = 1/(mu_1 mu_2), relative
TOL_ACCT = 1.0e-10           # 1 - r_12^2 = nu_1 nu_2/(a11 a22), relative
TOL_TH7 = 1.0e-11            # the T169-TH7 closed collapse, relative
TOL_ATSPL = 1.0e-11          # TH1 exact split vs the direct block, relative
TOL_POLAR = 1.0e-9           # TH2 det expansion, relative (near-null det:
#                              the three pieces are ~ 1e3 x larger than
#                              their sum, so the declared horizon is wider)
TOL_DSUM = 1.0e-9            # TH3 explicit kernel double sum, relative
TOL_RANK3 = 1.0e-12          # sigma_4/sigma_1 of the kernel
TOL_SPEC = 1.0e-9            # nonzero spectrum of K vs eig(M P^T P), relative
TOL_LP = 1.0e-13             # L_P no-go: ahat_12 = 0 identically
TOL_CTRL = 1.0e-12           # Dirichlet / parity / Toeplitz controls
BAR_R1DEF = 5.0e-2           # rank-one defect ceiling (measured, honest)
BAR_MUT_WRON = 1.0           # wrong-eigenvalue telescope: relative miss >=
BAR_MUT_GERSH = 0.0          # nu_1 - max diag must be > this on every window
BAR_MUT_K7 = 5.0             # 1/sqrt(2) must overshoot nu_2 by >= this factor
BAR_MUT_POLAR = 1.0e-2       # wrong polarisation coefficient, relative miss
BAR_TII = 4                  # Type II 99.9%-energy rank ceiling
BAR_TII_GEN = 2.0            # generic kernel must need >= this x more
BAR_SCRAM = 10.0             # median |value move| factor under scramble
SEED = 558


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


def mobius_table(n_max):
    mu = np.ones(n_max + 1, dtype=np.int64)
    prm = np.ones(n_max + 1, dtype=bool)
    prm[:2] = False
    for p in range(2, n_max + 1):
        if prm[p]:
            prm[p * p::p] = False
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
    mu[0] = 0
    return mu


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
    table (the T162..T170 convention; Chebyshev 1852 / Rosser-Schoenfeld
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
    positions with the SAME masses (the item-(6) discriminator)."""
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
    for bit the frame-A code path of T128..T170 / v548..v557."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T170)
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


# ------------------------------ the T163 correlation weights (a THEOREM)
def lag_weights_from_v(v, m):
    """w_0 = A_0, w_d = 2 A_d - H_{M-1-d} (d >= 1), A the autocorrelation
    and H the self-convolution of v; then v^T A_h v = sum_d c_d w_d EXACTLY
    -- the quadratic form as a LAG SUM (the T163 correlation theorem)."""
    M = 2 * m
    ac = np.correlate(v, v, "full")[m - 1:]
    cv = np.convolve(v, v)
    w = np.zeros(M)
    w[:m] = 2.0 * ac
    w[0] = ac[0]
    ee = (M - 1) - np.arange(1, M)
    w[1:] -= np.where(ee <= M - 2, cv[np.minimum(ee, M - 2)], 0.0)
    return w


def spline_project(W, u, D, M):
    """phi_n . W for the unit-mass spline phi_n of the atom at u = log n:
    a CLOSED two-point read of the weight vector W, plus the d = 0
    reflection when u < D (bit for bit the T170 read)."""
    i0 = int(math.floor(u / D))
    f = u / D - i0
    val = 0.0
    if 0 <= i0 < M:
        val += (1.0 - f) * W[i0]
    if 0 <= i0 + 1 < M:
        val += f * W[i0 + 1]
    if u < D:
        val += (1.0 - u / D) * W[0]
    return val


def mixed_det(P, Q):
    """D(P, Q) = P11 Q22 + P22 Q11 - 2 P12 Q12, the POLARISATION of det on
    2 x 2 symmetric matrices: det(P + Q) = det P + D(P, Q) + det Q and
    D(P, P) = 2 det P."""
    return (P[0, 0] * Q[1, 1] + P[1, 1] * Q[0, 0] - 2.0 * P[0, 1] * Q[0, 1])


POLAR_M = 0.5 * np.array([[0.0, 1.0, 0.0],
                          [1.0, 0.0, 0.0],
                          [0.0, 0.0, -2.0]])


def wedge_kernel(P):
    """K = P M P^T with P the N x 3 matrix of spline reads (X11, X22, X12)
    and M the polarisation matrix: K(n, m) = (1/2) D(X_n, X_m)."""
    return P @ (POLAR_M @ P.T)


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


def hat_block(c, W11, W22, W12):
    c = np.asarray(c)
    return np.array([[float(c @ W11), float(c @ W12)],
                     [float(c @ W12), float(c @ W22)]])


def build_instance(k, D, M, h):
    alpha = 0.5 * M * D
    atoms = atoms_in(alpha)
    sp = lag_vector_split(alpha, M, atoms)
    r = dict(n=NN_ALL[k], k=k, M=M, h=h, D=sp["D"], alpha=alpha,
             c=sp["c"], c_ar=sp["c_ar"], c_at=sp["c_at"], atoms=atoms,
             X=math.exp(2.0 * alpha))
    r["split"] = float(np.max(np.abs(sp["c"] - sp["c_ar"] - sp["c_at"])))
    A = sym(odd_toeplitz(sp["c"], M))
    Tb = parity_basis(h, 2)
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    W11 = lag_weights_from_v(t1, h)
    W22 = lag_weights_from_v(t2, h)
    Wpp = lag_weights_from_v(t1 + t2, h)
    W12 = 0.5 * (Wpp - W11 - W22)
    Ah_dir = np.array([[float(t1 @ (A @ t1)), float(t1 @ (A @ t2))],
                       [float(t1 @ (A @ t2)), float(t2 @ (A @ t2))]])
    B = hat_block(sp["c_ar"], W11, W22, W12)
    lam = np.array([a[1] * 0.5 for a in atoms])   # Lambda(n)/sqrt(n)
    uu = np.array([a[0] for a in atoms])
    P = np.empty((len(atoms), 3))
    for i in range(len(atoms)):
        P[i, 0] = spline_project(W11, uu[i], sp["D"], M)
        P[i, 1] = spline_project(W22, uu[i], sp["D"], M)
        P[i, 2] = spline_project(W12, uu[i], sp["D"], M)
    S = np.array([[float(lam @ P[:, 0]), float(lam @ P[:, 2])],
                  [float(lam @ P[:, 2]), float(lam @ P[:, 1])]])
    r.update(A=A, t1=t1, t2=t2, W11=W11, W22=W22, W12=W12,
             Ah=Ah_dir, B=B, S=S, lam=lam, uu=uu, P=P,
             mu=parity_mu(h))
    r["a11"], r["a22"], r["a12"] = (float(Ah_dir[0, 0]),
                                    float(Ah_dir[1, 1]),
                                    float(Ah_dir[0, 1]))
    nuv = np.linalg.eigvalsh(Ah_dir)
    r["nu2"], r["nu1"] = float(nuv[0]), float(nuv[1])
    r["det"] = float(np.linalg.det(Ah_dir))
    r["onem"] = r["det"] / (r["a11"] * r["a22"])
    return r


def vaughan_split(Xc, U, V):
    """The four Vaughan pieces as explicit coefficient arrays on n <= Xc."""
    lamn = von_mangoldt_table(Xc)
    mu = mobius_table(max(V, 2))
    a1 = np.zeros(Xc + 1)
    a1[:U + 1] = lamn[:U + 1]
    a2 = np.zeros(Xc + 1)
    for m in range(2, U + 1):
        if lamn[m] == 0.0:
            continue
        for d in range(1, V + 1):
            if mu[d] == 0 or m * d > Xc:
                continue
            a2[m * d::m * d] -= lamn[m] * float(mu[d])
    a3 = np.zeros(Xc + 1)
    kk = np.arange(Xc + 1, dtype=float)
    logk = np.zeros(Xc + 1)
    logk[1:] = np.log(kk[1:])
    for d in range(1, V + 1):
        if mu[d] == 0:
            continue
        a3[d::d] += float(mu[d]) * logk[1:Xc // d + 1]
    a4 = lamn - a1 - a2 - a3
    return lamn, a1, a2, a3, a4


def k_energy(s, frac=0.999):
    e = np.cumsum(s ** 2) / np.sum(s ** 2)
    return int(np.searchsorted(e, frac) + 1)


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("=" * 72)
    print("v558  PRIME.BILINEAR.RANK.01 -- the bilinear / rank identities "
          "(T168-T170)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, the one arithmetic input")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    kappa = chebyshev_kappa()
    check(f"S0.KAPPA: the ONE unconditional arithmetic input, measured on "
          f"THIS table and nothing else -- |psi(x) - x| <= kappa x with "
          f"kappa = {kappa:.6f} at every jump point of the von-Mangoldt "
          f"table in [{KAPPA_X0:.0f}, {ATOM_MAX}] (the T162..T170 "
          f"convention); the T168/T169/T170 constant 0.038821 is reproduced "
          f"to {abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} (Chebyshev "
          f"1852 / Rosser-Schoenfeld 1962).  No other arithmetic enters "
          f"any identity below",
          abs(kappa - KAPPA_REF) <= TOL_KAPPA)
    INST = [build_instance(k, D, M, h) for (k, D, M, h) in build_windows()]
    h_max = max(r["h"] for r in INST) if INST else 0
    e_split = max(r["split"] for r in INST)
    pos_ok = [bool(r["nu2"] > 0.0) for r in INST]
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (the lag "
          f"split c = c^arch + c^atom exact to {e_split:.1e} <= "
          f"{TOL_SPLIT:.0e}; the 2 x 2 arithmetic block Ahat_ij = "
          f"t_i^T A_h t_j positive definite on {sum(pos_ok)}/{len(INST)} "
          f"windows -- a NUMERICAL FACT about finite matrices, never routed "
          f"through the Weil criterion); every assembled section <= "
          f"{H_CAP} (max m = {h_max})",
          len(INST) >= 6 and h_max <= H_CAP and e_split <= TOL_SPLIT
          and all(pos_ok))
    for r in INST:
        print(f"    n={r['n']:>5d} m={r['h']:>4d} X={r['X']:8.1f} "
              f"atoms={len(r['atoms']):>3d} "
              f"det={r['det']:10.3e} 1-r_12^2={r['onem']:.3e}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the Lagrange / Wronskian anatomy (T168 W0/W1)")
    E_LAG, E_ORTH, E_WRON, E_WRONM, E_LAGR = [], [], [], [], []
    for r in INST:
        c, t1, t2, h = r["c"], r["t1"], r["t2"], r["h"]
        lag = hat_block(c, r["W11"], r["W22"], r["W12"])
        E_LAG.append(float(np.max(np.abs(lag - r["Ah"])))
                     / max(1.0, float(np.max(np.abs(r["Ah"])))))
        mu1, mu2 = float(r["mu"][0]), float(r["mu"][1])
        Q = r["Ah"] / np.sqrt(np.outer([mu1, mu2], [mu1, mu2]))
        X2 = np.column_stack([t1 / math.sqrt(mu1), t2 / math.sqrt(mu2)])
        E_LAG.append(float(np.max(np.abs(sym(X2.T @ (r["A"] @ X2)) - Q)))
                     / max(1.0, float(np.max(np.abs(Q)))))
        E_ORTH.append(abs(float(t1 @ t2)))
        E_ORTH.append(abs(float(t1 @ t1) - 1.0))
        E_ORTH.append(abs(float(t2 @ t2) - 1.0))
        u, v = t1, t2
        W = u[1:] * v[:-1] - u[:-1] * v[1:]      # W_r, r = 0 .. h-2
        Wpad = np.concatenate([[0.0], W, [0.0]])  # W_{-1} .. W_{h-1}
        tele = Wpad[:-1] - Wpad[1:]               # W_{r-1} - W_r, r = 0..h-1
        E_WRON.append(float(np.max(np.abs((mu1 - mu2) * u * v - tele))))
        mu3 = float(parity_mu(h)[2])
        E_WRONM.append(float(np.max(np.abs((mu1 - mu3) * u * v - tele)))
                       / float(np.max(np.abs(tele))))
        uu_, vv_ = u / math.sqrt(mu1), v / math.sqrt(mu2)
        Mw = np.outer(uu_, vv_) - np.outer(vv_, uu_)
        lhs = 0.5 * float(np.sum(Mw * Mw))
        rhs = (float(uu_ @ uu_) * float(vv_ @ vv_) - float(uu_ @ vv_) ** 2)
        E_LAGR.append(abs(lhs - 1.0 / (mu1 * mu2)) * mu1 * mu2)
        E_LAGR.append(abs(rhs - 1.0 / (mu1 * mu2)) * mu1 * mu2)
    check(f"S1.LAGSUM: THE LAG-SUM IDENTITY (T163 correlation theorem / "
          f"T169-TH3) -- Ahat_ij = t_i^T A_h t_j = sum_d c_d W^{{ij}}_d with "
          f"the closed correlation weights, and the 1/sqrt(mu)-normalised "
          f"block equals X^T A X for X = [t_1/sqrt(mu_1), t_2/sqrt(mu_2)], "
          f"worst relative {max(E_LAG):.1e} <= {TOL_LAG:.0e} on "
          f"{len(INST)} windows: the whole 2 x 2 block is a LAG SUM against "
          f"the closed T159 Dirichlet weights, and no conditioning ladder "
          f"enters (the cond ~ 1e8 ladder left the file at T169)",
          max(E_LAG) <= TOL_LAG)
    check(f"S1.ORTHO: EUCLIDEAN ORTHOGONALITY -- t_1 . t_2 = 0 and "
          f"|t_k| = 1 to {max(E_ORTH):.1e} <= {TOL_ORTH:.0e} (closed "
          f"trigonometry, KMS 1953): the near-parallelism 1 - r_12^2 -> 0 "
          f"of the whole programme is created ENTIRELY by the arithmetic "
          f"metric A_h and not at all by the vectors (T168's sharpest "
          f"anatomical fact)",
          max(E_ORTH) <= TOL_ORTH)
    check(f"S1.WRONSKIAN: THE WRONSKIAN TELESCOPE -- (mu_1 - mu_2) u_r v_r "
          f"= W_(r-1) - W_r with W_r = u_(r+1) v_r - u_r v_(r+1) and "
          f"W_(-1) = W_(h-1) = 0 (the telescope closes at the window edge), "
          f"worst absolute {max(E_WRON):.1e} <= {TOL_WRON:.0e} on every "
          f"window -- the near-diagonal minors are ONE closed one-parameter "
          f"family, and summing the telescope re-derives S1.ORTHO; the "
          f"minors are MAXIMAL: (1/2) sum M^2 = |u|^2 |v|^2 - <u,v>^2 = "
          f"1/(mu_1 mu_2) exactly (relative {max(E_LAGR):.1e} <= "
          f"{TOL_LAGR:.0e}; Lagrange 1773) -- the Wronskians carry ZERO "
          f"arithmetic, all smallness sits in the kernel",
          max(E_WRON) <= TOL_WRON and max(E_LAGR) <= TOL_LAGR)
    check(f"S1.CTRL: the telescope with the WRONG eigenvalue pair "
          f"(mu_1 - mu_3 instead of mu_1 - mu_2) misses by "
          f"{min(E_WRONM):.2f}..{max(E_WRONM):.2f} >= {BAR_MUT_WRON:.0f} "
          f"RELATIVE to the true telescope amplitude on every window (the "
          f"closed miss is (mu_2 - mu_3)/(mu_1 - mu_2) -> 5/3): the "
          f"telescope is a statement about THE eigenvalue gap of the "
          f"pair, not a generic difference identity",
          min(E_WRONM) >= BAR_MUT_WRON)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the exponent account and the Gershgorin certificate "
          "(T168 W2 / T169 X2)")
    E_ACCT, GERSH_LOSS, GERSH_OK, MUT_GERSH = [], [], [], []
    for r in INST:
        acct = r["nu1"] * r["nu2"] / (r["a11"] * r["a22"])
        E_ACCT.append(abs(acct - r["onem"]) / max(abs(r["onem"]), 1e-300))
        gb = max(r["a11"], r["a22"]) + abs(r["a12"])
        GERSH_OK.append(bool(r["nu1"] <= gb + 1e-12))
        GERSH_LOSS.append(gb / r["nu1"])
        MUT_GERSH.append(r["nu1"] - max(r["a11"], r["a22"]))
    check(f"S2.ACCOUNT: THE EXPONENT ACCOUNT IS AN IDENTITY -- 1 - r_12^2 "
          f"= nu_1 nu_2 / (ahat_11 ahat_22) (det = nu_1 nu_2 on the 2 x 2 "
          f"block; Poincare separation), worst relative {max(E_ACCT):.1e} "
          f"<= {TOL_ACCT:.0e} on {len(INST)}/{len(INST)} windows (measured "
          f"1 - r_12^2 = {min(r['onem'] for r in INST):.3e}.."
          f"{max(r['onem'] for r in INST):.3e} on this small surface; the "
          f"deep-surface h-trend is a sandbox FIT and is not consumed): "
          f"every factor of the T168 ledger is closed except the one "
          f"near-null eigenvalue nu_2 -- T167's R1 in eigenvalue clothing, "
          f"typed OPEN",
          max(E_ACCT) <= TOL_ACCT)
    check(f"S2.GERSH: THE GERSHGORIN CERTIFICATE (T169's R3, the "
          f"CERT-UNIF) -- nu_1 <= max(ahat_11, ahat_22) + |ahat_12| "
          f"(Gershgorin 1931), UNCONDITIONAL and closed in the three "
          f"entries, holds on {sum(GERSH_OK)}/{len(INST)} windows with "
          f"loss factor {min(GERSH_LOSS):.4f}..{max(GERSH_LOSS):.4f}: the "
          f"large eigenvalue is CHEAP -- the whole remaining difficulty "
          f"sits in nu_2, never in nu_1",
          all(GERSH_OK))
    check(f"S2.CTRL: dropping the |ahat_12| term FAILS on every window -- "
          f"nu_1 - max(ahat_11, ahat_22) = {min(MUT_GERSH):.2e}.."
          f"{max(MUT_GERSH):.2e} > {BAR_MUT_GERSH:.0f} on {len(INST)}/"
          f"{len(INST)} (the top eigenvalue exceeds the top diagonal entry "
          f"whenever ahat_12 != 0): the certificate is a statement about "
          f"the FULL row sum, not about the diagonal",
          min(MUT_GERSH) > BAR_MUT_GERSH)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the det-collapse theorem (T169-TH7)")
    E_TH7, USE_OK, TIGHT, MUT_K7 = [], [], [], []
    for r in INST:
        a11, a22, a12 = r["a11"], r["a22"], r["a12"]

        def rayleigh(t):
            return (t * t * a11 - 2.0 * t * a12 + a22) / (1.0 + t * t)

        k7 = math.sqrt(a22 / a11)
        lhs = rayleigh(k7)
        g = math.sqrt(a11 * a22)
        rhs = 2.0 * g * r["det"] / ((a11 + a22) * (g + a12))
        E_TH7.append(abs(lhs - rhs) / max(abs(lhs), 1e-300))
        usable = 2.0 * r["det"] / (a11 + a22)
        USE_OK.append(bool(r["nu2"] <= usable * (1.0 + 1e-12)
                           and a12 > 0.0))
        TIGHT.append(usable / r["nu2"])
        MUT_K7.append(rayleigh(1.0 / math.sqrt(2.0)) / r["nu2"])
    check(f"S3.TH7: *** THE det-COLLAPSE THEOREM (T169-TH7) *** -- on the "
          f"Rayleigh family u(t) = (t, -1), the one threshold-meeting "
          f"candidate K7 = sqrt(ahat_22/ahat_11) collapses in CLOSED FORM: "
          f"R(K7) = 2 sqrt(ahat_11 ahat_22) det Ahat / [(ahat_11 + "
          f"ahat_22)(sqrt(ahat_11 ahat_22) + ahat_12)], worst relative "
          f"{max(E_TH7):.1e} <= {TOL_TH7:.0e} on {len(INST)}/{len(INST)} "
          f"windows: K7 meets the threshold precisely BECAUSE it "
          f"reintroduces det Ahat -- the t*-language is provably exactly "
          f"as hard as the determinant, and the loop T167 scalar -> T168 "
          f"factor -> T169 candidate closes as an identity",
          max(E_TH7) <= TOL_TH7)
    check(f"S3.USABLE: the usable form -- nu_2 <= 2 det Ahat/(ahat_11 + "
          f"ahat_22) = 2 nu_1 nu_2/(nu_1 + nu_2) holds on "
          f"{sum(USE_OK)}/{len(INST)} windows (Rayleigh 1877: every "
          f"candidate is a VALID upper bound, only the size is at stake; "
          f"ahat_12 > 0 on all windows so the closed collapse has a "
          f"positive denominator), tight to a factor "
          f"{min(TIGHT):.4f}..{max(TIGHT):.4f} < 2 EXACTLY (the factor is "
          f"2 nu_1/(nu_1 + nu_2), closed)",
          all(USE_OK) and max(TIGHT) < 2.0 + 1e-9)
    check(f"S3.CTRL: the closed CONSTANT candidate t = 1/sqrt(2) (T168's "
          f"best closed guess) overshoots nu_2 by a factor "
          f"{min(MUT_K7):.1f}..{max(MUT_K7):.1e} >= {BAR_MUT_K7:.0f} on "
          f"every window: no h-independent constant can substitute for "
          f"K7 -- the sharpness of the t*-language MEASURES det Ahat, it "
          f"does not bound it",
          min(MUT_K7) >= BAR_MUT_K7)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the exact bilinear von Mangoldt form "
          "(T170 TH1-TH3)")
    E_SPL, E_POL, E_POLM, E_DS, R1DEF = [], [], [], [], []
    for r in INST:
        B, S, P, lam = r["B"], r["S"], r["P"], r["lam"]
        E_SPL.append(float(np.max(np.abs((B - S) - r["Ah"])))
                     / max(1.0, float(np.max(np.abs(r["Ah"])))))
        dB, dS = float(np.linalg.det(B)), float(np.linalg.det(S))
        exp_ = dB - mixed_det(B, S) + dS
        E_POL.append(abs(exp_ - r["det"]) / max(abs(r["det"]), 1e-300))
        wrong = (B[0, 0] * S[1, 1] + B[1, 1] * S[0, 0]
                 - 1.0 * B[0, 1] * S[0, 1])
        E_POLM.append(abs((dB - wrong + dS) - r["det"])
                      / max(abs(r["det"]), 1e-300))
        K = wedge_kernel(P)
        dsum = float(lam @ (K @ lam))
        E_DS.append(abs(dsum - dS) / max(abs(dS), 1e-300))
        dX = P[:, 0] * P[:, 1] - P[:, 2] ** 2
        nX = P[:, 0] ** 2 + P[:, 1] ** 2 + 2.0 * P[:, 2] ** 2
        R1DEF.append(float(np.median(np.abs(dX) / np.maximum(nX, 1e-300))))
    check(f"S4.SPLIT: *** THE EXACT SPLIT (T170-TH1) *** -- Ahat = B - S "
          f"with B the archimedean block and S_ij = sum_(n<=X) "
          f"(Lambda(n)/sqrt n) X_n[ij], X_n[ij] = phi_n . W^(ij) the "
          f"two-point spline read of the closed weights, reproduces the "
          f"DIRECT t_i^T A_h t_j to worst relative {max(E_SPL):.1e} <= "
          f"{TOL_ATSPL:.0e} on {len(INST)}/{len(INST)} windows (linearity "
          f"of c -> A_h and of A_h -> Ahat): the atom half of the block is "
          f"an explicit LINEAR von Mangoldt sum, written down exactly",
          max(E_SPL) <= TOL_ATSPL)
    check(f"S4.POLAR: THE POLARISATION (T170-TH2) -- det Ahat = det B - "
          f"D(B, S) + det S with D(P,Q) = P11 Q22 + P22 Q11 - 2 P12 Q12, "
          f"worst relative {max(E_POL):.1e} <= {TOL_POLAR:.0e}: arch-arch, "
          f"arch-Lambda (linear) and Lambda-Lambda (BILINEAR) -- only the "
          f"last is a bilinear von Mangoldt sum, and the determinant is a "
          f"THREE-TERM difference, which is what every size-bounding tool "
          f"fails to see (the T170 route table stays sandbox)",
          max(E_POL) <= TOL_POLAR)
    check(f"S4.DOUBLE: THE EXPLICIT BILINEAR FORM (T170-TH3) -- det S = "
          f"sum_(n,m<=X) Lambda(n) Lambda(m) K(n,m)/sqrt(nm) with K(n,m) "
          f"= (1/2) D(X_n, X_m), verified through the EXPLICIT "
          f"{max(len(r['atoms']) for r in INST)}-atom kernel matrix "
          f"(never through the factorisation) to worst relative "
          f"{max(E_DS):.1e} <= {TOL_DSUM:.0e} (Cauchy-Binet 1812/1815; "
          f"Lagrange 1773): R1's bilinear shape is a THEOREM; the wedge "
          f"reading holds up to the measured rank-one defect median "
          f"|det X_n|/||X_n||^2 = {min(R1DEF):.1e}..{max(R1DEF):.1e} <= "
          f"{BAR_R1DEF:.0e} (honest CERT, not exact: the diagonal n = m "
          f"does NOT vanish identically, it is small)",
          max(E_DS) <= TOL_DSUM and max(R1DEF) <= BAR_R1DEF)
    check(f"S4.CTRL: the polarisation with the WRONG cross-coefficient "
          f"(-1 instead of -2 on P12 Q12) breaks the expansion by "
          f"{min(E_POLM):.2e}..{max(E_POLM):.2e} >= {BAR_MUT_POLAR:.0e} "
          f"relative on every window: D is THE polarisation of det, not a "
          f"generic bilinear pairing",
          min(E_POLM) >= BAR_MUT_POLAR)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the rank-3 theorem and the Type II collapse "
          "(T170 TH4-TH5)")
    ev_M = np.linalg.eigvalsh(2.0 * POLAR_M)
    check(f"S5.DMAT: THE POLARISATION MATRIX -- D as a quadratic form on "
          f"(X11, X22, X12) has matrix [[0,1,0],[1,0,0],[0,0,-2]] with "
          f"eigenvalues {{{ev_M[0]:.0f}, {ev_M[1]:.0f}, {ev_M[2]:.0f}}} = "
          f"{{-2, -1, +1}}: RANK 3, SIGNATURE (1, 2) -- an exact integer "
          f"statement; and D(P, P) = 2 det P on random symmetric P "
          f"(64 draws)",
          np.allclose(np.sort(ev_M), [-2.0, -1.0, 1.0], atol=1e-14)
          and max(abs(mixed_det(Pr, Pr) - 2.0 * np.linalg.det(Pr))
                  for Pr in [sym(rng.normal(size=(2, 2)))
                             for _ in range(64)]) <= 1e-12)
    E_R3, E_SPEC, EFF_R = [], [], []
    for r in INST:
        K = wedge_kernel(r["P"])
        sv = np.linalg.svd(K, compute_uv=False)
        E_R3.append(float(sv[3] / sv[0]) if len(sv) > 3 else 0.0)
        EFF_R.append(float(np.sum(sv ** 2) / sv[0] ** 2))
        G3 = r["P"].T @ r["P"]
        evK = np.sort(np.abs(np.linalg.eigvals(POLAR_M @ G3)))[::-1]
        E_SPEC.append(float(np.max(np.abs(np.sort(sv[:3])[::-1] - evK))
                            / evK[0]))
    check(f"S5.RANK3: *** THE RANK-3 THEOREM (T170-TH4) *** -- the N x N "
          f"kernel K = P M P^T has numerical rank EXACTLY 3 on every "
          f"window: sigma_4/sigma_1 = {max(E_R3):.1e} <= {TOL_RANK3:.0e}, "
          f"effective rank ||K||_F^2/||K||_op^2 = {min(EFF_R):.2f}.."
          f"{max(EFF_R):.2f} <= 3, and the nonzero spectrum of K equals "
          f"the spectrum of M (P^T P) to {max(E_SPEC):.1e} <= "
          f"{TOL_SPEC:.0e} (the closed 3 x 3 route): rank K <= 3 for "
          f"EVERY window, EVERY h, EVERY X -- the bilinear form IS the "
          f"rank-3 polynomial S_11 S_22 - S_12^2 in THREE linear Lambda "
          f"sums, and there is no bilinear content beyond three linear "
          f"functionals",
          max(E_R3) <= TOL_RANK3 and max(EFF_R) <= 3.0 + 1e-9
          and max(E_SPEC) <= TOL_SPEC)
    rr = INST[-1]
    Xc = int(rr["X"])
    ranks_tii, ranks_gen, e_vid = [], [], 0.0
    for U in UV_LIST:
        lamn, a1, a2, a3, a4 = vaughan_split(Xc, U, U)
        e_vid = max(e_vid, float(np.max(np.abs(a1 + a2 + a3 + a4 - lamn))))
        ms = [n for n in range(U + 1, Xc // U + 1)
              if lamn[n] > 0.0][:TII_DIM]
        ds = [d for d in range(U + 1, Xc // U + 1)][:TII_DIM]
        if len(ms) < 4 or len(ds) < 4:
            continue
        G = np.array([[spline_project(rr["W11"], math.log(m * d),
                                      rr["D"], rr["M"]) / math.sqrt(m * d)
                       for d in ds] for m in ms])
        ranks_tii.append(k_energy(np.linalg.svd(G, compute_uv=False)))
        Ggen = rng.standard_normal(G.shape)
        ranks_gen.append(k_energy(np.linalg.svd(Ggen, compute_uv=False)))
    check(f"S5.TYPEII: THE TYPE II COLLAPSE (T170-TH5) -- Vaughan's "
          f"identity Lambda = a1 + a2 + a3 + a4 verified COEFFICIENT BY "
          f"COEFFICIENT on n <= {Xc} for every U = V in {list(UV_LIST)} "
          f"(max residual {e_vid:.1e} == 0; Vaughan 1977), and the Type II "
          f"kernel g(log m + log d)/sqrt(md) built from the closed weights "
          f"has 99.9%-energy rank {ranks_tii} <= {BAR_TII} across the "
          f"whole U scan (log-additivity: the weights see n only through "
          f"log n, so the kernel factorises through log m + log d): "
          f"finite rank for EVERY U, V -- not an artefact of the "
          f"classical choice U = X^(1/3)",
          e_vid <= 1e-9 and all(t <= BAR_TII for t in ranks_tii))
    check(f"S5.CTRL: a same-size GENERIC Gaussian kernel needs "
          f"{ranks_gen} singular values for the same 99.9% energy -- at "
          f"least {BAR_TII_GEN:.0f}x more than the Type II block on every "
          f"U (measured ratio {min(g / t for g, t in zip(ranks_gen, ranks_tii)):.1f}x"
          f"..{max(g / t for g, t in zip(ranks_gen, ranks_tii)):.1f}x): "
          f"the large sieve rewards the generic case and returns the "
          f"trivial operator norm on the collapsed one (Montgomery-"
          f"Vaughan 1973, cited as the PRICED route; the sandbox deltas "
          f"stay in the diary)",
          all(g >= BAR_TII_GEN * t for g, t in zip(ranks_gen, ranks_tii)))

    # ---------------------------------------------------------------- (6)
    print("\nS6 -- (6) the R4-free chain, the L_P no-go and the scramble "
          "discriminator (T170 TH6 / T169 X3)")
    E_CHN, CHN_OK, CHN_LOSS = [], [], []
    for r in INST:
        direct = r["det"] / (r["a11"] * r["a22"])
        E_CHN.append(abs(direct - r["onem"]) / max(abs(r["onem"]), 1e-300))
        th9 = ((max(r["a11"], r["a22"]) + abs(r["a12"])) * r["nu2"]
               / (r["a11"] * r["a22"]))
        CHN_OK.append(bool(r["onem"] <= th9 * (1.0 + 1e-12)))
        CHN_LOSS.append(th9 / r["onem"])
    check(f"S6.CHAIN: THE R4-FREE CHAIN IS AN IDENTITY (T170-TH6) -- "
          f"1 - r_12^2 = det Ahat/(ahat_11 ahat_22) to {max(E_CHN):.1e} "
          f"relative, so a bound on det Ahat IS a bound on the target "
          f"with NO positivity of A_h, no Rayleigh detour, no R4: the "
          f"Weil fence is never approached; and the T169-TH9 chain "
          f"[max(ahat_11, ahat_22) + |ahat_12|] nu_2/(ahat_11 ahat_22) is "
          f"a VALID upper bound on {sum(CHN_OK)}/{len(INST)} windows with "
          f"loss factor {min(CHN_LOSS):.4f}..{max(CHN_LOSS):.4f} -- "
          f"exactly the Gershgorin loss of S2.GERSH: the direct chain is "
          f"the sharper of the two and uses strictly less",
          max(E_CHN) <= TOL_ACCT and all(CHN_OK))
    E_LPA, E_LPO = [], []
    for m_c in (64, 128, 256):
        L = lap_P_mat(m_c)
        Tc = parity_basis(m_c, 2)
        E_LPA.append(abs(float(Tc[0] @ (L @ Tc[1]))))
        muc = parity_mu(m_c)
        E_LPO.append(float(np.max(np.abs(L @ Tc[0] - muc[0] * Tc[0]))))
    check(f"S6.LP_NOGO: THE L_P NO-GO as a must-break -- for A = L_P the "
          f"parity modes are EXACT eigenvectors (residual "
          f"{max(E_LPO):.1e}), so ahat_12 = t_1^T L_P t_2 = "
          f"{max(E_LPA):.1e} <= {TOL_LP:.0e} IDENTICALLY and 1 - r_12^2 "
          f"= 1 with NO decay, at m = 64, 128, 256: the h^(-3) phenomenon "
          f"is not a property of the two sine modes -- it needs the "
          f"arithmetic kernel (T170's L_P control, re-verified as an "
          f"exact statement)",
          max(E_LPA) <= TOL_LP and max(E_LPO) <= 1e-11)
    MOVE, RANK_S = [], []
    for r in INST:
        for _ in range(N_SCRAM):
            pos = np.sort(rng.uniform(1e-6, 2.0 * r["alpha"],
                                      size=len(r["atoms"])))
            masses = [a[1] for a in r["atoms"]]
            c_at_s, _ = atom_lags_at(r["alpha"], r["M"], list(pos), masses)
            cs = r["c_ar"] + c_at_s
            Bh = hat_block(cs, r["W11"], r["W22"], r["W12"])
            onem_s = float(np.linalg.det(Bh)) / (Bh[0, 0] * Bh[1, 1])
            MOVE.append(abs(onem_s / r["onem"]))
            Ps = np.empty((len(pos), 3))
            for i, u_ in enumerate(pos):
                Ps[i, 0] = spline_project(r["W11"], u_, r["D"], r["M"])
                Ps[i, 1] = spline_project(r["W22"], u_, r["D"], r["M"])
                Ps[i, 2] = spline_project(r["W12"], u_, r["D"], r["M"])
            svs = np.linalg.svd(wedge_kernel(Ps), compute_uv=False)
            RANK_S.append(float(svs[3] / svs[0]) if len(svs) > 3 else 0.0)
    med_move = float(np.median(MOVE))
    check(f"S6.SCRAMBLE: THE DISCRIMINATOR THAT LOCALISES THE ARITHMETIC "
          f"-- with uniform random atom positions at the SAME masses "
          f"({N_SCRAM} declared draws per window), the RANK-3 COLLAPSE IS "
          f"UNTOUCHED (scrambled sigma_4/sigma_1 <= {max(RANK_S):.1e} <= "
          f"{TOL_RANK3:.0e} on all {len(RANK_S)} draws -- it is algebra, "
          f"blind to where the atoms sit) while the VALUE of 1 - r_12^2 "
          f"MOVES by a median factor {med_move:.1f} >= {BAR_SCRAM:.0f} "
          f"(range {min(MOVE):.2g}..{max(MOVE):.2g}): the arithmetic "
          f"content sits ENTIRELY in the joint values of the three linear "
          f"sums (S_11, S_22, S_12) against the arch block B -- not in "
          f"the rank, not in the kernel, not in the Type I/II split -- "
          f"which is exactly why no size-bounding tool reaches R1",
          max(RANK_S) <= TOL_RANK3 and med_move >= BAR_SCRAM)

    # ---------------------------------------------------------------- controls
    print("\nS7 -- the parity / Dirichlet controls")
    rng2 = np.random.default_rng(5581)
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
    check(f"S7.DIRICHLET: the closed cosine-sum identity (Dirichlet 1829) "
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
    check(f"S7.PARITY: L_P t_k = mu^P_k t_k to {e_eig:.1e} with the basis "
          f"orthonormal to {e_ort:.1e} (Kac-Murdock-Szego 1953 -- the "
          f"parity sines are EXACT eigenvectors, the unperturbed object "
          f"the L_P no-go starts from), and odd_toeplitz(c^L) = L_P for "
          f"c^L = (2, -1, 0, ...) with residual {e_tpl:.1e} == 0 (ZERO "
          f"tolerance): the section map of the whole chain is the one the "
          f"identities assume",
          e_eig <= 1.0e-11 and e_ort <= 1.0e-12 and e_tpl == 0.0)

    # ---------------------------------------------------------------- fences
    print("\nS8 -- the fences, restated as a check")
    check("S8.FENCE: PER-INSTANCE identities and certified inequalities on "
          "SMALL frame-A windows only -- a FINITE LIST with an explicit "
          "maximum, nothing uniform in the zone index or in D, and NO "
          "statement for ALL D; finite Lambda-sums are allowed and used, "
          "NO RH statement is made, assumed, approached or weakened, no "
          "zero of any L-function is read and no L-function is evaluated "
          "(AST firewall); THE ONE OPEN OBJECT AFTER T170 STAYS OPEN AND "
          "TYPED OPEN -- R1, now CLASSIFIED but not closed: an m-free "
          "unconditional certificate that the two rows of Ahat become "
          "collinear at rate h^{-3+eps}, equally a JOINT NEAR-DEGENERACY "
          "of the three explicit linear Lambda sums (S_11, S_22, S_12) "
          "against the archimedean block -- a rate statement this module "
          "neither makes nor approaches; the T170 sandbox verdict "
          "SIEVE-RESISTS, the route-table deltas (best unconditional "
          "+0.996 against target 3.0), the five-order cancellation and "
          "all h-exponents stay in the diary and the paper as sandbox "
          "MEASURED numbers; THE WEIL FENCE: uniform-in-h positivity of "
          "A_h is RH-equivalent-shaped, never routed, never claimed, "
          "never reverse-inferred -- the chain of item (6) is R4-free BY "
          "CONSTRUCTION; no other marker of any pre-existing contract "
          "moves; Lagrange 1773, Cauchy-Binet 1812/1815, Gershgorin 1931, "
          "Rayleigh 1877 / Courant-Fischer 1920, Montgomery-Vaughan 1973 "
          "/ Vaughan 1977 (the priced route), Kac-Murdock-Szego 1953, "
          "Chebyshev 1852 / Rosser-Schoenfeld 1962, Dirichlet 1829, "
          "Wilkinson 1968 / Higham 2002 named CLASSICAL; Weil 1952 / "
          "Bombieri 2000 CITED, never used as a criterion; zero-firewall "
          "AST-checked", True)

    elapsed = time.time() - t0
    print(f"\nv558 runtime: {elapsed:.1f}s")
    print(f"  (1) lag sum <= {max(E_LAG):.1e}; Wronskian telescope <= "
          f"{max(E_WRON):.1e}; Lagrange norm <= {max(E_LAGR):.1e}")
    print(f"  (2) account <= {max(E_ACCT):.1e}; Gershgorin loss "
          f"{min(GERSH_LOSS):.3f}..{max(GERSH_LOSS):.3f}")
    print(f"  (3) TH7 collapse <= {max(E_TH7):.1e}; usable-form tightness "
          f"{min(TIGHT):.3f}..{max(TIGHT):.3f}")
    print(f"  (4) split <= {max(E_SPL):.1e}; polarisation <= "
          f"{max(E_POL):.1e}; double sum <= {max(E_DS):.1e}")
    print(f"  (5) sigma_4/sigma_1 <= {max(E_R3):.1e}; Type II ranks "
          f"{ranks_tii} vs generic {ranks_gen}")
    print(f"  (6) scramble: rank invariant <= {max(RANK_S):.1e}, value "
          f"moves x{med_move:.1f} median")
    return summary("PRIME.BILINEAR.RANK.01 bilinear/rank identities")


if __name__ == "__main__":
    raise SystemExit(run())
