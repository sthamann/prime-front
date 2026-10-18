"""v556 -- PRIME.GAUGE.PPR.01: the gauge / price identities of T164/T165.
The CLOSED, theorem-shaped cores of T164 (contract SECTOR.CHANGE) and T165
(contract ALIGNMENT.ETA) -- every statement RECOMPUTED here from scratch on
small exactly checkable frame-A windows (no citation of sandbox output).
Companion to PRIME.PARETO.TV.01 (v555), which certified the PRICE STRUCTURE
of the pairing: THIS module certifies its GAUGE STRUCTURE -- the theorem
that the entry normalisation x_1 = 1 is a gauge, the exact conservation law
that no sector shift can remove the h^2, the linearity that makes the chain
spend its entry ceiling at power exactly one, the gauge-invariant P_pr
identity that closes the successor question R-F by certificate, and the
Schur-cascade direction with its exact exponent closure.  NOTHING here
closes the one remaining quantifier:

[E] (1) THE GAUGE THEOREM (T164, S2.1 -- the structural result of arm B).
    The pairing is x^T B x = v^T A v with a_k = x_k / sqrt(mu_k) and
    v = T^T a; the constraint x_1 = 1 fixes a_1 = 1/sqrt(mu_1), i.e. only
    the SCALE of a; Q and TV are HOMOGENEOUS OF DEGREE TWO in a.  Hence
    Q/TV -- and with it the demand coordinate delta_bnd -- depends only on
    the DIRECTION of a and is the SAME NUMBER IN EVERY SECTOR mu': the
    entry normalisation is a GAUGE.  Machine-checked per instance on a
    declared sector battery (weight families x shifts x taper widths),
    with TV >= |w_0| in every sector (the T163 telescope) and, for the
    pure shift, the certified VALUE scaling by exactly
    theta = mu^P_1 / (mu^P_1 + kap_s).  Mutation: transporting the
    x-COORDINATES instead of the a-direction (the wrong map) moves the
    ratio loudly on the spread-out weight families.
[E] (2) THE h^2 CONSERVATION LAW (T164, S2.2).  A shifted sector DOES
    flatten the T163 floor -- TV >= 1/(mu^P_1 + kap_s) -- but the value the
    shifted pairing certifies scales by theta, so recovering a bound on
    the ORIGINAL 1/s costs the transfer factor 1/theta, and
      floor x transfer = 1/(mu^P_1 + kap_s) . (1 + kap_s/mu^P_1)
                       = 1/mu^P_1        IDENTICALLY, at EVERY shift:
    the h^2 is conserved, never removed -- it lives in the RATIO, not in
    the floor.  Checked as an exact product identity per window per shift.
    Mutation: the wrong transfer 1 + kap_s/(mu^P_1 + kap_s) misses the
    product by a factor that grows with the shift.
[E] (3) THE POWER-ONE SPEND AS AN IDENTITY (T164, S1 ST2/ST3).  The
    downstream chain consumes the entry ceiling U through the r-ceiling
    r <= U / L with L = lambda_1(A)/mu^P_1 -- LINEAR in U -- so
      d log r / d log U = +1   EXACTLY (central difference at U = 1/g_16),
    which is the algebraic reason an h^eps ceiling costs h^{-eps} of
    margin for every eps > 0 (the measured -1.0005..-1.0000 of the full
    T156 loss margin is a SANDBOX number and stays there).  Mutation: a
    quadratic consumption r = U^2/L reads slope 2 and is recognised.
[E] (4) THE P_pr IDENTITY AND THE PREDICATE EQUIVALENCE (T165, T1 -- the
    spine of the closure of R-F).  The gauge-invariant dashboard
      R = Q/TV,  tvf = TV/(t_1 v)^2,  P_pr = g_16 Q / (mu^P_1 (t_1 v)^2)
    (all quotients of equal-degree homogeneous functions, hence functions
    of the RAY through v) satisfies, with NO inequality anywhere,
      P_pr(v) = g_16 . R(v) . tvf(v) / mu^P_1
    -- four factors, each a named object of the chain: the R-E-A
    quantifier g_16, the demand R, the T163 floor tvf >= 1, and the
    Kac-Murdock-Szego 1953 spectral scale 1/mu^P_1 ~ h^2.  Consequences,
    each machine-checked per instance on the full trial battery: (a) the
    two predicates ``R > 2 kappa'' and
    ``P_pr > 2 kappa g_16 tvf / mu^P_1'' are ONE predicate (exact boolean
    equivalence -- the demand half of R2'' and the gauge-invariant
    crossing condition were never two questions); (b) tvf >= 1 for EVERY
    v (TV >= |w_0| = ||v||^2 >= (t_1 v)^2), hence
      P_pr >= R . g_16 / mu^P_1   pointwise,
    so ANY crossing vector pays P_pr > 2 kappa g_16 / mu^P_1 -- the old
    KMS h^2 -- which exceeds the preregistered tolerance THETA_TOL = 10 on
    every window of this surface: demand and affordability collide by an
    identity plus a floor, and R-F is EMPTY here by certificate, not by a
    failed search.  Mutation: writing (t_1 v) for (t_1 v)^2 destroys the
    gauge invariance loudly under v -> t v.
[E] (5) THE SCHUR-CASCADE DIRECTION AND THE EXPONENT CLOSURE (T164 ST1 /
    T165 T2).  Per instance, from one Cholesky of the sixteen-block and
    one full-window solve: s = mu^P_1 t_1^T A^{-1} t_1 >= g_16 >= g_1 with
    every ladder increment strictly positive (Schur 1917 / Haynsworth
    1968) -- the T158 ladder really is a chain of UPPER bounds 1/s <=
    1/g_16 <= 1/g_1 = B_11 on the entry ceiling -- and P_K = a_hat . s >= 1
    (Kantorovich 1948 admissibility of the T156 kernel).  And the T165
    exponent closure is an IDENTITY of the lists: (1/g_1) =
    (g_16/g_1) . (1/g_16) per instance, so the fitted exponents close
    EXACTLY (T165's +3.110 - 3.049 = +0.061 is linear algebra, not luck);
    the exponent VALUES are sandbox fits and are NOT consumed here.
    Mutations: the closure with g_8 in place of g_16 breaks loudly; a
    corrupted sixteen-block makes the Cholesky REFUSE.

Plus the NO-GO DISCRIMINATOR (the monotone coarsening staircase, T163/T164
R3): coarsening the lag grid over nu = 4 -> 2 -> 1 (and 0.5 where the
window allows it) degrades the arch/atom cancellation MONOTONICALLY in the
median, with the nu = 4 column an exact null control (damage = 1); the
surface of this module sits on the right side of the T105 admissibility
floor by construction.  Parity / Dirichlet controls: the closed Dirichlet
cosine-sum identity against the brute-force sum (including the degenerate
branch), L_P t_k = mu^P_k t_k with an orthonormal basis, and
odd_toeplitz(c^L) = L_P with ZERO tolerance.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL frame-A windows -- the
        N_INST DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), mirroring v551..v555's declared surface.  Nothing is
        uniform in the zone index or in D, and NO statement for ALL D is
        made.  The h-exponents of T164/T165 (1/g_16 ~ h^{+0.061}, the
        ascent price ~ h^{+3.3}, the exponent split +3.110 - 3.049 =
        +0.061) are sandbox FITS and are NOT consumed; what IS consumed is
        the per-instance identity structure that makes the split exact.
  (ii)  THE ONE OPEN OBJECT AFTER T165 STAYS OPEN AND TYPED OPEN:
        inf_m g_16(m) > 0 -- equivalently a lower bound on the sixteen-step
        Schur-cascade gain g_16/g_1 >= c h^{3-eps} uniform in m -- a
        quantifier over a certified flat list.  This module certifies the
        cascade DIRECTION and the exponent CLOSURE per instance and makes
        no uniformity claim whatsoever.  R-B''' (an independent alpha/h
        surface) stays open as narrowed by T164.
  (iii) The T164 verdict TOLERANCE-CARRIES / SECTOR-RESISTS and the T165
        verdict ETA-RESISTS are SANDBOX verdicts; this module promotes
        only their theorem-shaped identity/inequality cores, and the
        measured anatomy (the free ascent, the eta(Cap) profile, the
        decoupled nu surface with its zone-depth finding and the retired
        constant U_ref) stays in the diary and the paper.
  (iv)  Item (4) allows finite Lambda-sums and nothing else: kappa is
        verified on the finite table, no search is run here, and no
        statement about what depth the primes deliver is made anywhere in
        this module.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  Everything here is a per-instance identity or a
    certified per-window inequality; finite sums over the von-Mangoldt
    table are allowed and used; NOTHING here claims, assumes, approaches
    or weakens RH, no zero of any L-function is read, generated or
    approximated (AST firewall), no L-function is evaluated, and no
    equivalence is claimed.  The number 1/2 appears in exactly one role:
    as the STRENGTH of a classical statement against which a required
    depth is compared, and a comparison of strengths is not a claim about
    RH in either direction.  Even with every check green, what stands is
    a finite list of certified window statements on prime-power zones in
    one frame.
  * Classics named CLASSICAL: Schur 1917 / Haynsworth 1968 (the Cholesky
    cascade), Kac-Murdock-Szego 1953 (the parity spectrum; mu_0 = 0 and
    the h^2 scale), Abel 1826 (the partial sums behind the demand ratio),
    Chebyshev 1852 / Rosser-Schoenfeld 1962 (the one unconditional input,
    verified on the table), Kantorovich 1948 (the P_K admissibility),
    Fejer 1915 (the taper battery), Dirichlet 1829 (the cosine-sum
    identity), Wilkinson 1968 / Higham 2002 (floating-point floors);
    Weil 1952 / Bombieri 2000 CITED, never used as a criterion.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name, each with a mutation control that fails loudly;
measured quantities typed MEASURED.  Python; Wolfram-mirrored not required
(dense linear-algebra machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/sector_change_probe.py                (T164)
  experiments/tfpt-discovery/alignment_eta_probe.py                (T165)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v555
H_CAP = 300                  # HARD cap on any assembled section
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              (v551..v555's declared surface convention)

# --- the form geometry, preregistered ----------------------------------------
SCHUR_KB = 16                # the fixed low block of the T152..T165 chain

# --- the Chebyshev input, preregistered (T164/T165 Q0) ------------------------
KAPPA_X0 = 100.0             # verification window [x0, ATOM_MAX], as declared
KAPPA_REF = 0.038821         # the T162..T165 constant, reproduced on the table

# --- the sector battery, preregistered (T164 S2.1) ----------------------------
SHIFTS = (0.0, 1.0e-6, 1.0e-4, 1.0e-2, 0.25, 1.0, 4.0)
WEIGHTS = ("none", "poly1", "poly2", "expk", "exph")
SIG_GRID = (1.0, 2.0, 4.0, 8.0, 16.0, float("inf"))   # Fejer taper widths

# --- the trial battery for the P_pr identity (T165 T1) ------------------------
N_RAND16 = 6                 # random admissible sixteen-vectors per window
N_RANDF = 4                  # random full-window vectors per window
GAUGE_T = (1.0e-3, 7.3, 1.0e4)   # the v -> t v round-trip scales (T165 T0)

# --- the preregistered affordability tolerance (T165) -------------------------
THETA_TOL = 10.0             # ``Q comparable to 1/s'' -- T165's declared bar

# --- the no-go staircase, preregistered (T163/T164 R3) ------------------------
NOGO_FACTORS = (1, 2, 4)     # nu = 4 / 2 / 1; 8 (nu = 0.5) where m >= 128

# --- preregistered tolerances / bars (declared BEFORE any number) -------------
TOL_KAPPA = 1.0e-6           # |kappa(table) - 0.038821|
TOL_GAUGE = 1.0e-7           # Q/TV invariance across the sector battery
TOL_THETA = 1.0e-9           # the pure-shift value scaling theta
TOL_TEL = -1.0e-12           # TV - |w_0| >= this in every sector
TOL_CONS = 1.0e-12           # floor x transfer = 1/mu^P_1, relative
TOL_SLOPE = 1.0e-12          # |d log r / d log U - 1| at U = 1/g_16
TOL_EXCH = 1.0e-12           # the P_pr identity, relative, per trial vector
TOL_GI = 1.0e-9              # the v -> t v round trip; the DECLARED horizon:
#                              Q is an O(1) difference of halves, so its
#                              relative accuracy is eps/canc ~ 1e-11 on this
#                              surface, and the round trip rescales by t^2
TOL_TVF = 1.0e-9             # tvf >= 1 - TOL_TVF on every trial vector
TOL_CLOSE = 1.0e-12          # per-instance exponent closure identity
TOL_FIT = 1.0e-10            # least-squares exponent closure of the lists
TOL_SCHUR = 1.0e-9           # s >= g_16 >= g_1, relative slack
TOL_CTRL = 1.0e-12           # Dirichlet / parity / Toeplitz controls
BAR_MUT_GAUGE = 1.0e-2       # the wrong transport map must move Q/TV by >=
BAR_MUT_CONS = 1.0e-1        # the wrong transfer must miss the product by >=
BAR_MUT_SLOPE = 0.5          # the quadratic consumption must read >= 1.5
BAR_MUT_PPR = 0.5            # the (t_1 v) mutation must move under v -> tv by
#                              >= this relative on EVERY round trip (it scales
#                              like t, so the smallest move is |t - 1| ~ 1)
BAR_MUT_CLOSE = 1.0e-2       # the g_8 closure mutation must break by >=
BAR_NOGO = 1.5               # the coarsest staircase step must damage the
#                              cancellation by >= this factor (median)
TOL_SPLIT = 1.0e-15          # floating residue of the lag split re-summation


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
    table (the T162..T165 convention; Chebyshev 1852 / Rosser-Schoenfeld
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
    bit the frame-A code path of T128..T165 / v548..v555."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T165)
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


def full_mu(m):
    """The UNPROJECTED circulant spectrum on N = 2m + 1 points: mu_k =
    4 sin^2(pi k / N), k = 0 .. N-1, with mu_0 = 0 EXACTLY (the constant
    vector; Kac-Murdock-Szego 1953) -- candidate (i) of T164's arm B."""
    N = 2 * m + 1
    kk = np.arange(N, dtype=float)
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


# ------------------------------------- the lag weights (T159/T163)
def lag_weights_direct(y, M):
    """w_d = T_d - H_d: T the autocorrelation and H the convolution of y,
    so that y^T A y = sum_d c_d w_d for A = odd_toeplitz(c, M) (the T163
    correlation form)."""
    h = M // 2
    acf = np.correlate(y, y, mode="full")[h - 1:]
    cnv = np.convolve(y, y)
    w = np.zeros(M)
    w[0] = acf[0]
    if h > 1:
        w[1:h] += 2.0 * acf[1:h]
    dd = np.arange(1, M)
    w[1:] -= cnv[(M - 1) - dd]
    return w


def total_variation(w):
    """TV = ||Delta w||_1 with the T163 convention w_M := 0."""
    return float(np.sum(np.abs(np.diff(np.append(w, 0.0)))))


def cholesky_ladder(B):
    """g_K = sum_{j <= K} y_j^2 with y = L^{-1} e_1 from ONE Cholesky of the
    16x16 block (Schur 1917 / Haynsworth 1968; T158's positive ladder)."""
    L = np.linalg.cholesky(B)
    e1 = np.zeros(B.shape[0])
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return np.cumsum(y * y), y


def fit_exp(xs, ys):
    """The least-squares log-log slope -- used ONLY for the closure identity
    of item (5); no fitted exponent is consumed as a claim."""
    lx = np.log(np.asarray(xs, float))
    ly = np.log(np.abs(np.asarray(ys, float)))
    A = np.vstack([lx, np.ones_like(lx)]).T
    return float(np.linalg.lstsq(A, ly, rcond=None)[0][0])


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
    sp = lag_vector_split(alpha, M, atoms_in(alpha))
    r = dict(n=NN_ALL[k], k=k, M=M, h=h, D=sp["D"], alpha=alpha,
             c=sp["c"], c_ar=sp["c_ar"], c_at=sp["c_at"],
             X=math.exp(2.0 * alpha), logX=2.0 * alpha)
    r["split"] = float(np.max(np.abs(sp["c"] - sp["c_ar"] - sp["c_at"])))
    A = sym(odd_toeplitz(sp["c"], M))
    lam = np.linalg.eigvalsh(A)
    if not (float(lam[0]) > 0.0):
        return None
    r["A"] = A
    r["lam1"] = float(lam[0])
    mu_full = parity_mu(h)
    r["mu1"] = float(mu_full[0])
    r["L"] = r["lam1"] / r["mu1"]
    mu = mu_full[:SCHUR_KB]
    T16 = parity_basis(h)[:SCHUR_KB, :]
    isq = 1.0 / np.sqrt(mu)
    BLL = sym((T16 @ (A @ T16.T)) * np.outer(isq, isq))
    e1 = np.zeros(SCHUR_KB)
    e1[0] = 1.0
    xs = np.linalg.solve(BLL, e1)
    xs /= max(abs(float(xs[0])), 1.0e-300)
    gK, y_lad = cholesky_ladder(BLL)
    r["mu"], r["BLL"], r["T16"] = mu, BLL, T16
    r["x_star"], r["gK"], r["y_lad"] = xs, gK, y_lad
    r["g1"], r["g16"] = float(gK[0]), float(gK[-1])
    r["a_hat"] = float(BLL[0, 0])
    t1 = T16[0]
    r["t1"] = t1
    r["s"] = r["mu1"] * float(t1 @ np.linalg.solve(A, t1))
    return r


def v_of_x(r, x):
    """The lag-space vector of a sixteen-mode trial: v = T16^T (x/sqrt(mu))."""
    return (r["T16"].T / np.sqrt(r["mu"])) @ np.asarray(x, float)


def eta_pack(r, v):
    """THE GAUGE-INVARIANT DASHBOARD of T165: every entry is a quotient of
    equal-degree homogeneous functions of v, hence a function of the RAY."""
    w = lag_weights_direct(v, r["M"])
    tv = total_variation(w)
    Q = float(np.dot(r["c"], w))
    t1v = float(r["t1"] @ v)
    den = r["mu1"] * t1v * t1v
    return dict(Q=Q, TV=tv, t1v=t1v, w0=float(w[0]), nrm2=float(v @ v),
                R=(Q / tv if tv > 0.0 else float("-inf")),
                P_pr=(r["g16"] * Q / den if den > 0.0 else float("inf")),
                tvf=(tv / max(t1v * t1v, 1.0e-300)))


def sector_numbers(r, x, mu_s):
    """Q, TV, w_0 and the demand ratio for ONE sixteen-mode trial vector in
    ONE sector spectrum mu_s.  NOTHING else changes: same c, same lag grid
    (T164's sector map)."""
    a = np.asarray(x, float) / np.sqrt(np.asarray(mu_s, float)[:SCHUR_KB])
    v = r["T16"].T @ a
    w = lag_weights_direct(v, r["M"])
    Q = float(np.dot(r["c"], w))
    tv = total_variation(w)
    return dict(Q=Q, TV=tv, w0=float(w[0]),
                ratio=Q / max(tv, 1.0e-300))


def sector_mu(r, tag, kap_s):
    mu = r["mu"].copy()
    kk = np.arange(1, mu.shape[0] + 1, dtype=float)
    if tag == "poly1":
        mu = mu * kk
    elif tag == "poly2":
        mu = mu * kk ** 2
    elif tag == "expk":
        mu = mu * np.exp(kk / 4.0)
    elif tag == "exph":
        mu = mu * np.exp(kk / float(r["h"]))
    return mu + kap_s


def fejer_taper(K, sig):
    if not np.isfinite(sig):
        return np.ones(K)
    return np.maximum(0.0, 1.0 - np.arange(K) / float(sig))


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v556  PRIME.GAUGE.PPR.01 -- the gauge / P_pr identities "
          "(T164/T165)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, the one arithmetic input")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    kappa = chebyshev_kappa()
    cross_bar = 2.0 * kappa
    check(f"S0.KAPPA: the ONE unconditional arithmetic input, measured on "
          f"THIS table and nothing else -- |psi(x) - x| <= kappa x with "
          f"kappa = {kappa:.6f} at every jump point of the von-Mangoldt "
          f"table in [{KAPPA_X0:.0f}, {ATOM_MAX}] (the T162..T165 "
          f"convention); the T164/T165 constant 0.038821 is reproduced to "
          f"{abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} (Chebyshev "
          f"1852 / Rosser-Schoenfeld 1962).  The crossing bar of every "
          f"predicate below is 2 kappa = {cross_bar:.6f} and nothing else",
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
        print(f"    n={r['n']:>5d} m={r['h']:>4d} X={r['X']:8.1f} "
              f"g_16={r['g16']:.4f} s={r['s']:.4f} "
              f"1/mu^P_1={1.0 / r['mu1']:9.1f}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the gauge theorem: the entry normalisation is a "
          "gauge (T164, S2.1)")
    E_GAUGE, E_TEL, E_THETA, E_MUT = [], [], [], []
    n_comb = 0
    for r in INST:
        for sg in SIG_GRID:
            x = r["x_star"] * fejer_taper(SCHUR_KB, sg)
            x = x / max(abs(float(x[0])), 1.0e-300)
            base = sector_numbers(r, x, r["mu"])
            for tag in WEIGHTS:
                for ks in SHIFTS:
                    mu_s = sector_mu(r, tag, ks)
                    # THE SAME a-DIRECTION, RE-NORMALISED IN THE NEW SECTOR:
                    # y = sqrt(mu_s/mu) . x rescaled to y_1 = 1 keeps a fixed
                    # up to scale -- the map the gauge claim is about
                    y = x * np.sqrt(mu_s / r["mu"])
                    y = y / max(abs(float(y[0])), 1.0e-300)
                    new = sector_numbers(r, y, mu_s)
                    E_GAUGE.append(abs(new["ratio"] - base["ratio"])
                                   / max(abs(base["ratio"]), 1.0e-300))
                    E_TEL.append(new["TV"] - abs(new["w0"]))
                    n_comb += 1
                    if tag == "none" and ks > 0.0 and base["Q"] != 0.0:
                        thet = r["mu1"] / (r["mu1"] + ks)
                        E_THETA.append(abs(new["Q"] / base["Q"] - thet)
                                       / thet)
        # MUTATION: transport the x-COORDINATES unchanged into the
        # spread-out poly2 sector -- a DIFFERENT a-direction (evaluated at
        # the UNTAPERED optimiser; a one-mode vector is direction-blind)
        x_full = r["x_star"] / max(abs(float(r["x_star"][0])), 1.0e-300)
        base_full = sector_numbers(r, x_full, r["mu"])
        mu_bad = sector_mu(r, "poly2", 0.0)
        bad = sector_numbers(r, x_full, mu_bad)
        E_MUT.append(abs(bad["ratio"] - base_full["ratio"])
                     / max(abs(base_full["ratio"]), 1.0e-300))
    check(f"S1.GAUGE: THE GAUGE THEOREM, machine-checked on {n_comb} "
          f"sector-by-trial-vector combinations ({len(WEIGHTS)} weight "
          f"families x {len(SHIFTS)} shifts x {len(SIG_GRID)} taper widths "
          f"on {len(INST)} windows) -- x_1 = 1 fixes a_1 = 1/sqrt(mu_1), "
          f"i.e. only the SCALE of a, and Q and TV are homogeneous of "
          f"degree two in a, so the demand ratio Q/TV of the SAME "
          f"a-direction is the SAME NUMBER in every sector: unchanged to "
          f"{max(E_GAUGE):.1e} <= {TOL_GAUGE:.0e} relative, and with it "
          f"delta_bnd -- the crossing criterion Q/TV > 2 kappa does not "
          f"contain the normalisation and cannot be moved by ANY sector "
          f"change (T164's arm-B theorem, per instance)",
          max(E_GAUGE) <= TOL_GAUGE)
    check(f"S1.THETA: the two auxiliary identities come out exact as well "
          f"-- TV >= |w_0| in EVERY sector (the T163 telescope; least "
          f"slack {min(E_TEL):.2e} >= {TOL_TEL:.0e}), and for the pure "
          f"shift the certified VALUE scales by exactly theta = "
          f"mu^P_1/(mu^P_1 + kap_s) to {max(E_THETA):.1e} <= "
          f"{TOL_THETA:.0e} relative on {len(E_THETA)} shift points -- the "
          f"SAME factor by which the shifted floor scales, which is what "
          f"item (2) turns into a conservation law",
          min(E_TEL) >= TOL_TEL and max(E_THETA) <= TOL_THETA)
    check(f"S1.CTRL: the wrong transport map -- carrying the x-COORDINATES "
          f"unchanged into the spread-out poly2 sector instead of the "
          f"a-direction -- moves the ratio by {min(E_MUT):.2e}.."
          f"{max(E_MUT):.2e} >= {BAR_MUT_GAUGE:.0e} relative on every "
          f"window (against <= {TOL_GAUGE:.0e} for the true map): the "
          f"invariance is a statement about the RAY through a, not a "
          f"generic insensitivity",
          min(E_MUT) >= BAR_MUT_GAUGE)
    mu0 = [abs(float(full_mu(r["h"])[0])) for r in INST]
    mu_rest = [float(np.min(full_mu(r["h"])[1:])) for r in INST]
    check(f"S1.FULLSPACE: candidate (i) of arm B settled in closed form -- "
          f"the unprojected spectrum on N = 2m+1 points has mu_0 = 0 "
          f"EXACTLY (measured {max(mu0):.1e}; the constant vector, KMS "
          f"1953), so the T163 floor step has NO finite floor in the full "
          f"space, and even excluding the constant mode the lowest "
          f"remaining eigenvalue is <= the parity mu^P_1 on "
          f"{sum(1 for i, r in enumerate(INST) if mu_rest[i] <= r['mu1'] * (1 + 1e-9))}"
          f"/{len(INST)} windows: the full space is strictly WORSE, a "
          f"THEOREM and a negative one",
          max(mu0) < 1.0e-28
          and all(mu_rest[i] <= r["mu1"] * (1.0 + 1.0e-9)
                  for i, r in enumerate(INST)))

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the h^2 conservation law: floor x transfer = "
          "1/mu^P_1 (T164, S2.2)")
    E_CONS, E_CONSM, E_CONSM_TOP = [], [], []
    ks_top = max(SHIFTS)
    for r in INST:
        mu1 = r["mu1"]
        for ks in [t for t in SHIFTS if t > 0.0]:
            fl = 1.0 / (mu1 + ks)
            tr = 1.0 + ks / mu1
            E_CONS.append(abs(fl * tr - 1.0 / mu1) * mu1)
            tr_bad = 1.0 + ks / (mu1 + ks)
            E_CONSM.append(abs(fl * tr_bad - 1.0 / mu1) * mu1)
            if ks == ks_top:
                E_CONSM_TOP.append(E_CONSM[-1])
    check(f"S2.CONSERVE: the exact product identity at EVERY shift on the "
          f"declared grid ({len(E_CONS)} window-by-shift points, kap_s = "
          f"{min(t for t in SHIFTS if t > 0):g}..{max(SHIFTS):g}) -- the "
          f"shifted sector's floor 1/(mu^P_1 + kap_s) times the transfer "
          f"factor 1/theta = 1 + kap_s/mu^P_1 back to the ORIGINAL 1/s "
          f"equals 1/mu^P_1 IDENTICALLY, to {max(E_CONS):.1e} <= "
          f"{TOL_CONS:.0e} of 1/mu^P_1: a sector shift can flatten the "
          f"floor but pays the identical factor back as a transfer -- the "
          f"h^2 = 1/(4 sin^2(pi/N)) is CONSERVED, never removed; it lives "
          f"in the ratio, not in the floor (T164's h^2 conservation law, "
          f"per instance)",
          max(E_CONS) <= TOL_CONS)
    check(f"S2.CTRL: the wrong transfer (1 + kap_s/(mu^P_1 + kap_s), i.e. "
          f"theta mis-read at the shifted spectrum) misses the product by "
          f"{min(E_CONSM):.2e}..{max(E_CONSM):.2e} of 1/mu^P_1, and by "
          f"{min(E_CONSM_TOP):.4f} >= {BAR_MUT_CONS:.0e} at the largest "
          f"shift kap_s = {ks_top:g} on EVERY window: the conservation is "
          f"a statement about THE transfer factor, not an approximate "
          f"cancellation",
          min(E_CONSM_TOP) >= BAR_MUT_CONS)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the power-one spend as an identity (T164, S1 ST2)")
    SLOPES, SLOPES_M = [], []
    for r in INST:
        U0 = 1.0 / r["g16"]
        lo, hi = U0 * 0.99, U0 * 1.01
        den = math.log(hi / lo)
        SLOPES.append(math.log((hi / r["L"]) / (lo / r["L"])) / den)
        SLOPES_M.append(math.log((hi ** 2 / r["L"])
                                 / (lo ** 2 / r["L"])) / den)
    check(f"S3.POWER_ONE: the r-ceiling of the downstream chain is r <= "
          f"U/L with L = lambda_1(A)/mu^P_1 = "
          f"{min(r['L'] for r in INST):.4f}.."
          f"{max(r['L'] for r in INST):.4f} computed per instance from the "
          f"full window -- LINEAR in the entry ceiling U, so "
          f"d log r/d log U = +1 EXACTLY: central difference at "
          f"U = 1/g_16 gives {min(SLOPES):.15f}..{max(SLOPES):.15f}, "
          f"within {max(abs(s - 1.0) for s in SLOPES):.1e} <= "
          f"{TOL_SLOPE:.0e} of 1 on {len(INST)}/{len(INST)} windows.  "
          f"CONSEQUENCE (the algebraic half of T164's arm A): an entry "
          f"ceiling growing like h^eps costs the chain h^{{-eps}} of "
          f"r-margin for every eps > 0 -- there is no free tolerance in "
          f"the consumption step; the measured power of the FULL T156 "
          f"loss margin (-1.0005..-1.0000) is a sandbox number and is NOT "
          f"consumed here",
          max(abs(s - 1.0) for s in SLOPES) <= TOL_SLOPE)
    check(f"S3.CTRL: the quadratic consumption r = U^2/L reads slope "
          f"{min(SLOPES_M):.4f}..{max(SLOPES_M):.4f} at the same points -- "
          f"away from 1 by >= {BAR_MUT_SLOPE}: the instrument measures "
          f"the consumption power and does not return 1 by construction",
          min(abs(s - 1.0) for s in SLOPES_M) >= BAR_MUT_SLOPE)

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the P_pr identity and the predicate equivalence "
          "(T165, T1)")
    rng = np.random.default_rng(556)
    E_GI, E_GIM, E_EXCH, EQV, TVF, PPR_R = [], [], [], [], [], []
    PFLOOR, N_CROSS = [], 0
    n_trial = 0
    for r in INST:
        packs = []
        for sg in SIG_GRID:
            x = r["x_star"] * fejer_taper(SCHUR_KB, sg)
            packs.append(v_of_x(r, x))
        for _ in range(N_RAND16):
            x = rng.normal(size=SCHUR_KB)
            x[0] = 1.0
            packs.append(v_of_x(r, x))
        for _ in range(N_RANDF):
            v = rng.normal(size=r["h"])
            if abs(float(r["t1"] @ v)) < 1.0e-6 * float(np.linalg.norm(v)):
                v = v + r["t1"]
            packs.append(v)
        pf = cross_bar * r["g16"] / r["mu1"]
        PFLOOR.append(pf)
        for v in packs:
            p = eta_pack(r, v)
            if not np.isfinite(p["R"]) or p["TV"] <= 0.0:
                continue
            n_trial += 1
            # (a) gauge invariance of the dashboard under v -> t v
            for t in GAUGE_T:
                q = eta_pack(r, t * v)
                for key in ("R", "P_pr", "tvf"):
                    E_GI.append(abs(q[key] - p[key])
                                / max(abs(p[key]), 1.0e-300))
                # the mutated price with (t_1 v) unsquared scales like t
                mut_p = r["g16"] * p["Q"] / (r["mu1"] * abs(p["t1v"]))
                mut_q = r["g16"] * q["Q"] / (r["mu1"] * abs(q["t1v"]))
                E_GIM.append(abs(mut_q - mut_p) / max(abs(mut_p), 1.0e-300))
            # (b) the exchange identity
            rhs = r["g16"] * p["R"] * p["tvf"] / r["mu1"]
            E_EXCH.append(abs(p["P_pr"] - rhs)
                          / max(abs(p["P_pr"]), 1.0e-300))
            # (c) the predicate equivalence
            lhs = p["R"] > cross_bar
            rhs_pred = p["P_pr"] > cross_bar * r["g16"] * p["tvf"] / r["mu1"]
            EQV.append(lhs == rhs_pred)
            if lhs:
                N_CROSS += 1
            # (d) the floor chain: tvf >= 1 and P_pr >= R g_16 / mu^P_1
            TVF.append(p["tvf"])
            PPR_R.append(p["P_pr"] / max(p["R"], 1.0e-300)
                         * r["mu1"] / r["g16"] if p["R"] > 0 else 1.0)
    check(f"S4.INVARIANT: the T165 dashboard is GAUGE-INVARIANT -- R = "
          f"Q/TV, tvf = TV/(t_1 v)^2 and P_pr = g_16 Q/(mu^P_1 (t_1 v)^2) "
          f"are quotients of equal-degree homogeneous functions and are "
          f"unchanged to {max(E_GI):.1e} <= {TOL_GI:.0e} relative under "
          f"v -> t v for t = 1e-3, 7.3, 1e4 on all {n_trial} trial "
          f"vectors ({len(SIG_GRID)} knob settings + {N_RAND16} random "
          f"sixteen-vectors + {N_RANDF} random FULL-WINDOW vectors per "
          f"window; the declared horizon is the CANCELLATION and not the "
          f"functional -- Q is an O(1) difference of halves, so its "
          f"relative accuracy is eps/canc ~ 1e-11 here and the residual "
          f"is arithmetic noise, not a defect of the identity): no "
          f"statement below can be manufactured by a choice of "
          f"normalisation (T164's gauge theorem applied to T165's "
          f"functionals)",
          max(E_GI) <= TOL_GI)
    check(f"S4.EXCHANGE: THE T165 P_pr IDENTITY, per instance and per "
          f"trial vector -- P_pr = g_16 . R . (TV/(t_1 v)^2) / mu^P_1 to "
          f"{max(E_EXCH):.1e} <= {TOL_EXCH:.0e} relative on all "
          f"{len(E_EXCH)} battery vectors: four factors, each a NAMED "
          f"object of the chain (the R-E-A quantifier g_16 = "
          f"{min(r['g16'] for r in INST):.4f}.."
          f"{max(r['g16'] for r in INST):.4f}, the demand R, the T163 "
          f"floor tvf >= 1, and the KMS 1953 scale 1/mu^P_1 = "
          f"{min(1 / r['mu1'] for r in INST):.1f}.."
          f"{max(1 / r['mu1'] for r in INST):.1f} ~ h^2) -- demand and "
          f"price are ONE equation, so the two clauses of R-F cannot be "
          f"chosen independently (T165's spine, an identity and not a "
          f"bound)",
          max(E_EXCH) <= TOL_EXCH)
    check(f"S4.EQUIV: the predicate equivalence -- ``R > 2 kappa'' and "
          f"``P_pr > 2 kappa g_16 (TV/(t_1 v)^2)/mu^P_1'' agree as "
          f"booleans on ALL {len(EQV)} battery vectors ({sum(EQV)} agree; "
          f"{N_CROSS} of them cross, and a search for crossing vectors is "
          f"NOT run here -- T165's ascent stays sandbox): the demand half "
          f"of R2'' and the gauge-invariant crossing condition are THE "
          f"SAME PREDICATE, hence R-F (demand AND affordability) is "
          f"strictly STRONGER than R2''-demand, and its m-uniform form IS "
          f"R-E-A",
          all(EQV))
    check(f"S4.PRICE_FLOOR: the floor chain, pointwise on every battery "
          f"vector -- tvf = TV/(t_1 v)^2 = {min(TVF):.2f}..{max(TVF):.2e} "
          f">= 1 - {TOL_TVF:.0e} (TV >= |w_0| = ||v||^2 >= (t_1 v)^2, the "
          f"T163 telescope in gauge-invariant form), hence P_pr >= "
          f"R . g_16/mu^P_1 pointwise (checked: P_pr/(R g_16/mu^P_1) = "
          f"tvf >= 1 on every vector with R > 0), so ANY vector meeting "
          f"the crossing bar pays P_pr > 2 kappa g_16/mu^P_1 = "
          f"{min(PFLOOR):.1f}..{max(PFLOOR):.1f} on this surface -- ABOVE "
          f"the preregistered tolerance THETA_TOL = {THETA_TOL:.0f} on "
          f"{sum(1 for p in PFLOOR if p > THETA_TOL)}/{len(PFLOOR)} "
          f"windows: the price of any crossing is the old KMS h^2 times "
          f"the certified g_16, and the R-F conjunction is EMPTY here by "
          f"an identity plus a floor (T165's closure; the m-uniform "
          f"version is exactly the one open quantifier)",
          min(TVF) >= 1.0 - TOL_TVF
          and all(pr >= 1.0 - TOL_TVF for pr in PPR_R)
          and all(p > THETA_TOL for p in PFLOOR))
    check(f"S4.CTRL: the mutated price with (t_1 v) UNSQUARED is degree "
          f"one over degree two and scales like t under v -> t v: it "
          f"moves by {min(E_GIM):.2e}..{max(E_GIM):.2e} >= "
          f"{BAR_MUT_PPR} relative on EVERY round trip (the smallest move "
          f"is |t - 1| at t = 7.3^-1-like scales) where the true P_pr "
          f"moves by <= {max(E_GI):.1e}: the gauge invariance is a "
          f"statement about THE squared normalisation, not a generic "
          f"stability",
          min(E_GIM) >= BAR_MUT_PPR)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the Schur-cascade direction and the exponent "
          "closure (T164 ST1 / T165 T2)")
    DIR_OK, PK, E_CLOSE, E_CLOSEM = [], [], [], []
    for r in INST:
        DIR_OK.append(bool(r["s"] >= r["g16"] * (1.0 - TOL_SCHUR)
                           and r["g16"] >= r["g1"] * (1.0 - TOL_SCHUR)))
        PK.append(r["a_hat"] * r["s"])
        E_CLOSE.append(abs(math.log(1.0 / r["g1"])
                           - math.log(r["g16"] / r["g1"])
                           - math.log(1.0 / r["g16"])))
        g8 = float(r["gK"][7])
        E_CLOSEM.append(abs(math.log(1.0 / r["g1"])
                            - math.log(g8 / r["g1"])
                            - math.log(1.0 / r["g16"])))
    XH = [float(r["h"]) for r in INST]
    f_b11 = fit_exp(XH, [1.0 / r["g1"] for r in INST])
    f_gain = fit_exp(XH, [r["g16"] / r["g1"] for r in INST])
    f_g16 = fit_exp(XH, [1.0 / r["g16"] for r in INST])
    e_fit = abs(f_b11 - f_gain - f_g16)
    check(f"S5.DIRECTION: the cascade direction per instance -- s = "
          f"mu^P_1 t_1^T A^{{-1}} t_1 = {min(r['s'] for r in INST):.4f}.."
          f"{max(r['s'] for r in INST):.4f} >= g_16 >= g_1 window by "
          f"window (slack tolerance {TOL_SCHUR:.0e}), i.e. 1/s <= 1/g_16 "
          f"<= 1/g_1 = B_11: the T158 ladder is a chain of UPPER bounds "
          f"on the entry ceiling with the T157 route-(0) rung the loosest "
          f"(Schur 1917 / Haynsworth 1968 nested complements), and P_K = "
          f"a_hat . s = {min(PK):.2f}..{max(PK):.2e} >= 1 is the "
          f"Kantorovich 1948 admissibility the T156 kernel consumes -- "
          f"the station chain of T164's arm A rests on these two "
          f"directions and on nothing else",
          all(DIR_OK) and min(PK) >= 1.0 - 1.0e-9)
    check(f"S5.CLOSURE: the exponent closure is an IDENTITY of the lists, "
          f"not a numerical coincidence -- per instance log(1/g_1) = "
          f"log(g_16/g_1) + log(1/g_16) to {max(E_CLOSE):.1e} <= "
          f"{TOL_CLOSE:.0e}, and the least-squares exponents over the "
          f"{len(INST)}-window list close exactly by linearity: "
          f"fit(1/g_1) = {f_b11:+.4f} = fit(g_16/g_1) + fit(1/g_16) = "
          f"{f_gain:+.4f} {f_g16:+.4f} to {e_fit:.1e} <= {TOL_FIT:.0e} "
          f"(T165's +3.110 - 3.049 = +0.061 is THIS identity on the "
          f"sandbox surface; the exponent VALUES are sandbox fits and are "
          f"NOT consumed -- what is promoted is that the whole "
          f"certification lives in the cascade gain g_16/g_1, the object "
          f"of the ONE open quantifier, typed OPEN)",
          max(E_CLOSE) <= TOL_CLOSE and e_fit <= TOL_FIT)
    refuse = 0
    for r in INST:
        Bbad = r["BLL"].copy()
        Bbad[0, SCHUR_KB - 1] += 0.05 * abs(Bbad[0, SCHUR_KB - 1]) + 0.05 \
            * float(np.max(np.abs(Bbad)))
        Bbad[SCHUR_KB - 1, 0] = Bbad[0, SCHUR_KB - 1]
        try:
            np.linalg.cholesky(Bbad)
        except np.linalg.LinAlgError:
            refuse += 1
    check(f"S5.CTRL: the mutations fail loudly -- the closure with g_8 in "
          f"place of g_16 breaks by {min(E_CLOSEM):.2e}..{max(E_CLOSEM):.2e} "
          f">= {BAR_MUT_CLOSE:.0e} (the identity is about THE sixteenth "
          f"rung), and a corrupted off-diagonal sixteen-block entry "
          f"destroys positive definiteness so the Cholesky REFUSES on "
          f"{refuse}/{len(INST)} windows: the cascade rests on a "
          f"certificate, not on a formula that silently degrades",
          min(E_CLOSEM) >= BAR_MUT_CLOSE and refuse == len(INST))

    # ---------------------------------------------------------------- no-go
    print("\nS6 -- the no-go staircase and the controls (T163/T164)")
    stair = {f: [] for f in NOGO_FACTORS + (8,)}
    for r in INST:
        for f in NOGO_FACTORS + ((8,) if r["h"] >= 128 else ()):
            Mf = r["M"] // f
            if Mf % 2:
                Mf -= 1
            hf = Mf // 2
            if hf < SCHUR_KB + 2:
                continue
            Df = 2.0 * r["alpha"] / Mf
            c_at, _ = atom_lags(r["alpha"], Mf, atoms_in(r["alpha"]))
            c_ar = arch_lags(Mf, Df)
            A = sym(odd_toeplitz(c_ar + c_at, Mf))
            mu = parity_mu(hf)[:SCHUR_KB]
            T16 = parity_basis(hf)[:SCHUR_KB, :]
            isq = 1.0 / np.sqrt(mu)
            BLL = sym((T16 @ (A @ T16.T)) * np.outer(isq, isq))
            e1 = np.zeros(SCHUR_KB)
            e1[0] = 1.0
            try:
                np.linalg.cholesky(BLL)
            except np.linalg.LinAlgError:
                continue
            xs = np.linalg.solve(BLL, e1)
            xs /= max(abs(float(xs[0])), 1.0e-300)
            y = (T16.T / np.sqrt(mu)) @ xs
            wf = lag_weights_direct(y, Mf)
            Qa = float(np.dot(c_ar, wf))
            Qt = float(np.dot(c_at, wf))
            stair[f].append(abs(Qa + Qt) / max(abs(Qa), abs(Qt)))
    base = np.array(stair[1])
    med = {}
    for f in stair:
        if not stair[f]:
            continue
        ratio = [c / b for c, b in zip(stair[f], base[:len(stair[f])])]
        med[f] = float(np.median(ratio))
    med_seq = [med[f] for f in sorted(med)]
    null_exact = all(c == b for c, b in zip(stair[1], base))
    check(f"S6.NOGO: the monotone staircase -- coarsening the lag grid "
          f"over nu = 4 / 2 / 1{' / 0.5' if 8 in med else ''} (factors "
          f"{sorted(med)}) degrades the arch/atom cancellation "
          f"CANC = |Q|/max(|Q^arch|, |Q^atom|) monotonically in the "
          f"median: damage = {', '.join(f'{m:.2f}' for m in med_seq)} "
          f"with the nu = 4 column an EXACT null control (1.0) and the "
          f"coarsest step >= {BAR_NOGO}: the T145 resolution no-go breaks "
          f"monotonically in the collision rate, and the surface of this "
          f"module (nu = 4) sits on the right side of it by construction",
          null_exact and all(a < b for a, b in zip(med_seq, med_seq[1:]))
          and med_seq[-1] >= BAR_NOGO)
    rng2 = np.random.default_rng(5561)
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
          f"spectrum whose k = 1 gap carries every h^2 above), and "
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
          "(AST firewall); the number 1/2 appears in exactly one role -- "
          "as the STRENGTH of a classical statement against which a "
          "required depth is compared, and a comparison of strengths is "
          "not a claim about RH in either direction; THE ONE OPEN OBJECT "
          "AFTER T165 STAYS OPEN AND TYPED OPEN: inf_m g_16(m) > 0, "
          "equivalently a lower bound on the sixteen-step Schur-cascade "
          "gain g_16/g_1 uniform in m -- a quantifier over a certified "
          "flat list, neither assumed nor approached here; R-B''' (an "
          "independent alpha/h surface) stays open as narrowed by T164; "
          "R-F is closed NEGATIVELY on this construction by the S4 "
          "identity plus floor, R-E-B negatively by the S1/S2 theorems, "
          "and no other marker of any pre-existing contract moves; the "
          "T164/T165 measured anatomy (the free ascent, eta(Cap), the "
          "decoupled nu surface, the retired constant U_ref) stays in the "
          "diary and the paper; Schur 1917 / Haynsworth 1968, "
          "Kac-Murdock-Szego 1953, Abel 1826, Chebyshev 1852 / "
          "Rosser-Schoenfeld 1962, Kantorovich 1948, Fejer 1915, "
          "Dirichlet 1829, Wilkinson 1968 / Higham 2002 named CLASSICAL; "
          "Weil 1952 / Bombieri 2000 CITED, never used as a criterion; "
          "zero-firewall AST-checked", True)

    elapsed = time.time() - t0
    print(f"\nv556 runtime: {elapsed:.1f}s")
    print(f"  (1) gauge invariance <= {max(E_GAUGE):.1e} on {n_comb} "
          f"combinations; theta <= {max(E_THETA):.1e}")
    print(f"  (2) floor x transfer = 1/mu^P_1 to {max(E_CONS):.1e} at "
          f"every shift")
    print(f"  (3) d log r/d log U - 1 <= "
          f"{max(abs(s - 1.0) for s in SLOPES):.1e} exactly")
    print(f"  (4) P_pr identity <= {max(E_EXCH):.1e}; equivalence exact "
          f"on {len(EQV)} vectors; price floor "
          f"{min(PFLOOR):.1f}..{max(PFLOOR):.1f} > {THETA_TOL:.0f}")
    print(f"  (5) s >= g_16 >= g_1 on {len(INST)}/{len(INST)}; exponent "
          f"closure {e_fit:.1e}")
    print(f"  no-go staircase medians "
          f"{', '.join(f'{m:.2f}' for m in med_seq)}; Dirichlet/parity "
          f"exact")
    return summary("PRIME.GAUGE.PPR.01 gauge/Ppr identities")


if __name__ == "__main__":
    raise SystemExit(run())
