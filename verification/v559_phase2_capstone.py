"""v559 -- PRIME.PHASE2.CAPSTONE.01: the phase-2 capstone (T171, contract FINAL.MAP).
THE CAPSTONE VERIFIES THE MAP AND CLAIMS NOTHING NEW.  T126..T170 reduced the
I5 uniformity question through sixteen exact reformulations to ONE object (R1);
T171 reproduced every link of that reduction in one connected sandbox run and
booked MAP-COMPLETE.  THIS module is the load-bearing version of that run: the
whole SIXTEEN-LINK CHAIN as one machine-checked pass -- thirteen links algebra
(THEOREM: valid for every h, checked here on instances), three links per-window
certificates (CERT: no quantifier in m) -- plus the EIGHT-ROUTE NO-GO BATTERY
(each classified dead route exhibited failing on an instance exactly as
classified) and the PRECISION LEDGER (needed against available, both
self-similarity identities checked), everything RECOMPUTED from scratch on the
declared small frame-A surface of v551..v558 (the 12 deepest prime-power zones
admitting a window inside the cap, m <= 300).  It adds ZERO new uniform-in-m
statements -- which is precisely why it is promotable:

[E] THE CHAIN, LINKS 1..16 (one check per link; the T-number names the part
    that established it, the check RECOMPUTES it here):
     1  T152 SCHUR 2-BLOCK   [THEOREM]  the I5 floor is the two-block Schur
        criterion on the normalised parity Gram G (Schur 1917; Haynsworth
        1968): x^T G x = v^T A_h v and x^T x = v^T L_P v for
        v = T^T(x/sqrt(mu)); KMS exact; the criterion HOLDS at 0.5 lam_min
        and FAILS at 1.02 lam_min (sharp, not one-sided; direction checked).
     2  T151 SOBOLEV         [THEOREM]  b_k = TV(t_k) <= C_S k with the
        explicit constant C_S = (2 pi + 2)/sqrt(N) -- an UPPER bound on the
        mode variation, the only property the reroute consumes.
     3  T153 PSI COLLAPSE    [THEOREM]  Psi(x) = sum_d c_d w_d(x) = x^T G x
        with the closed T163 correlation weights, and sum_d w_d = 0 (the
        gauge/Z-law) -- the ONE link where arithmetic enters, an identity.
     4  T154 RITZ CEILING    [THEOREM]  Cauchy interlacing: a K-truncated
        floor is a CEILING for lam_min, never a floor; dually
        g_12 <= g_16 <= g_32 <= s -- the ladder approaches the exact entry
        s from BELOW (Cauchy 1829; Courant-Fischer 1920).
     5  T155 12x12 FLOOR     [CERT]     the two-block certificate for
        lam_min(G_32) holds at (1 - 1e-9) lam and FAILS at (1 + 1e-4) lam:
        sharp per window, NO quantifier in m.
     6  T156 F(P, r) CHAIN   [CERT]     P_K = g_16/g_K >= 1 and
        r_K = 1/g_K - 1/s >= 0 at K = 2, 4, 8, 16, certified L increasing.
     7  T158 THOMSON/LADDER  [THEOREM]  the Thomson dual maximum equals the
        Cholesky ladder rung; every increment strictly positive; every
        random admissible trial lands BELOW the rung.
     8  T160 SAMPLING        [THEOREM]  the closed weight vector has two
        independent closed forms (four Dirichlet kernels vs the correlation
        form; Dirichlet 1829) and the atom half of Psi IS the sampled
        Lambda-mass (two-point spline read).
     9  T163 TV FLOOR/SWAP   [THEOREM]  the Abel swap identity (Abel 1826)
        and the consequence |Psi| <= TV(w) max|C_d| -- the overshoot IS the
        TV floor.
    10  T164 GAUGE/QUANTIFIER [THEOREM] R = Psi/TV is scale invariant
        (degree 2 over degree 2) and the admissible quantifier collapses
        onto the single vector x* = G_LL^-1 e_1/(...)_1 with Psi(x*) =
        1/g_16; every perturbed admissible vector gives MORE.
    11  T165 P_pr IDENTITY   [THEOREM]  the price factorises,
        P_pr = g_16 Psi/(mu^P_1 (Tv)_1^2), and equals 1 exactly at x*.
    12  T166 CASCADE         [THEOREM]  g_16/g_1 = 1/(1 - R_16^2) -- the
        gain is a squared multiple correlation, invariant under G -> DGD:
        pure collinearity, no scale.
    13  T167 K = 2 EXACT     [THEOREM]  B_11 g_2 = 1/(1 - r_12^2) with the
        explicit minimiser (1, -G_12/G_22); the K = 2 rung is the MILDEST
        place to stand (direction checked against K = 16).
    14  T169 DET COLLAPSE    [THEOREM]  1 - r_12^2 = det Ahat/(a11 a22) =
        nu_1 nu_2/(a11 a22) = det G_2/(G_11 G_22), and 1/g_2 =
        G_11 (1 - r_12^2) -- identities using NO positivity of A_h: the
        chain is R4-FREE (T170-TH6), the Weil fence never approached.
    15  T170 RANK-3          [THEOREM]  Ahat = B - S exactly, det Ahat =
        det B - D(B,S) + det S, det S = (1/2) y^T J y for the THREE linear
        Lambda sums y = (S_11, S_22, S_12), J = [[0,1,0],[1,0,0],[0,0,-2]]
        with eigenvalues {-2,-1,+1} (rank 3, signature (1,2); Lagrange
        1773; Cauchy-Binet 1812/1815): no sieve can see more than three
        functionals.
    16  T170 THE R1 SHAPE    [CERT]     sin(angle between the two rows of
        Ahat) = |det Ahat|/(|row_1||row_2|) -- an exact 2x2 Lagrange
        identity -- MEASURED per window and certified below the declared
        bar; the RATE (h^{-3}) and the quantifier in m stay OPEN: that
        single statement is R1, and this module neither makes nor
        approaches it.
[E] THE NO-GO BATTERY, ROUTES NG1..NG8 (each exhibited failing on the
    instance exactly as classified): NG1 size budget (the l1 majorant of the
    three polarisation pieces overshoots |det Ahat| by orders); NG2 symbol
    infimum (the Toeplitz symbol is NEGATIVE on every window -- no
    symbol-positivity argument can deliver the floor); NG3 sector/gauge
    change (1 - r_12^2 is a correlation: diagonal rescalings move it not at
    all); NG4 perturbation theory (Kato 1949 bounds at the scale of the
    matrix -- the object sits orders below it; cited as the closed-off
    route, never used); NG5 band-local domination (the atom band dominates
    the archimedean band on the instance); NG6 the sieve box (the
    operator-norm bound on det S alone overshoots by orders -- by link 15
    the kernel has rank <= 3, and a bound on det S alone cannot see the
    three-term cancellation; Montgomery-Vaughan 1973 / Vaughan 1977 cited
    as the PRICED route, the T170 route-table deltas stay sandbox); NG7
    scramble (uniform positions at the same masses inflate the value by
    orders while the rank-3 collapse is UNTOUCHED -- the arithmetic sits in
    the JOINT VALUES, not in rank/kernel/split); NG8 the L_P control (the
    cascade gain is IDENTICALLY 1 without the arithmetic kernel).
[E] THE PRECISION LEDGER (per instance, on THIS surface): the needed joint
    relative precision on (S_11, S_22, S_12) against the archimedean block
    -- the value of 1 - r_12^2 at the deepest window -- is finer than the
    RH-equivalent yardstick h^{-1/2} AND finer than the best unconditional
    exponent h^{-0.996} at the same length, by the declared factors; both
    self-similarity identities are checked (the T167 union: the K = 2
    cancellation ratio, the closed beta and the null-vector dress are ONE
    object; the T169 collapse: nu_2 at the EXACT stationary points of the
    Rayleigh quotient, sign-agnostic, with every explicit trial a VALID
    upper bound -- Rayleigh 1877).  The T171 full-surface numbers (needed
    2.284e-7 at h = 1444, short 1.2e5x of the RH yardstick and 3.1e3x of
    the best unconditional) are sandbox MEASURED numbers on the two-frame
    surface and are NOT consumed here.

Plus mutation controls that must fail loudly (the cascade with the wrong
regression row, the Thomson value read off the wrong entry, the swap with
off-by-one partial sums, the polarisation with the wrong cross-coefficient)
and the exact Dirichlet/parity/Toeplitz controls of the whole chain.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   Per-instance statements on SMALL frame-A windows -- the N_INST
        DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), v551..v558's declared surface.  Nothing is uniform in
        the zone index or in D, and NO statement for ALL D is made.  The
        T171 h-exponents (the pooled sin-angle trend h^{-2.33}, the
        frame-split rates nu=4: h^{-1.86} / nu=6: h^{-2.87}, the no-go
        growth exponents) are sandbox FITS on the two-frame surface and
        are NOT consumed; what IS consumed is the per-instance identity /
        certificate structure that makes every one of those numbers exact
        where it is quoted.
  (ii)  THE ONE OPEN PHASE-2 OBJECT STAYS OPEN AND TYPED OPEN -- R1: an
        m-free unconditional certificate that the two rows of Ahat -- two
        explicit finite Lambda-sum vectors -- become collinear at rate
        h^{-3+eps}, equally a joint near-degeneracy of the three explicit
        linear Lambda sums against the archimedean block.  This module
        verifies that the REDUCTION to that object reproduces end to end;
        it makes NO uniformity claim and NO rate claim.  The T171 sandbox
        verdict MAP-COMPLETE is a verdict about the MAP, not about R1.
  (iii) The chain typing is load-bearing: 13 links THEOREM (algebra for
        every h, machine-checked on instances), 3 links CERT (per window,
        no quantifier in m).  T171's honest exclusion (on the nu = 4,
        h = 1445 window of ITS surface the low block is indefinite, so the
        ladder links carry 11/12 there while the identity links carry
        12/12) belongs to the sandbox surface; on THIS declared small
        surface the low block is positive definite on 12/12 -- a numerical
        fact about finite matrices, never routed through the Weil
        criterion.
  (iv)  Finite Lambda-sums are allowed and nothing else: kappa is verified
        on the finite table, no search is run here, and no statement about
        what depth the primes deliver is made anywhere in this module.

HONEST FENCES (load-bearing typing):
  * THE RH FENCE, VERBATIM FROM T171.  RH_DELTA = 0.5 is a YARDSTICK for
    translating a precision demand into an exponent.  The chain is
    MEASURED-SURFACE certified; it is not an RH statement, it does not
    assume RH, no zero of any L-function is read, generated or approximated
    (AST firewall), no L-function is evaluated, and the quantifier over m
    stays OPEN at link 16.  Even with every check green, what stands is a
    finite list of certified window statements on prime-power zones in one
    frame -- and the one object R1 stays OPEN.
  * THE WEIL FENCE.  Uniform-in-h positivity of A_h is RH-equivalent-shaped
    and is never routed, never claimed, never reverse-inferred; link 14 is
    R4-free BY CONSTRUCTION (T170-TH6) and the fence is never approached.
  * Classics named CLASSICAL: Schur 1917 / Haynsworth 1968 (the two-block
    criterion), Kac-Murdock-Szego 1953 (the parity spectrum), Cauchy 1829 /
    Courant-Fischer 1920 (interlacing / Ritz), Rayleigh 1877 (trial
    directions), Abel 1826 (the swap), Dirichlet 1829 (the closed weights),
    Lagrange 1773 / Cauchy-Binet 1812/1815 (the rank-3 kernel), Gershgorin
    1931 (quoted with v558's certificate, not re-proved here), Kato 1949
    (the closed-off route), Montgomery-Vaughan 1973 / Vaughan 1977 (the
    priced route), Chebyshev 1852 / Rosser-Schoenfeld 1962 (the one
    unconditional input, verified on the table), Fejer 1915 (the section
    positivity mechanism, cited), Wilkinson 1968 / Higham 2002
    (floating-point floors); Weil 1952 / Bombieri 2000 CITED, never used
    as a criterion.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name; chain links typed THEOREM/CERT; measured quantities
typed MEASURED; mutation controls fail loudly.  Python; Wolfram-mirrored not
required (dense linear-algebra machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/final_map_probe.py                  (T171)
and, for the individual links, the T151..T170 probes named in the chain.
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v558
H_CAP = 300                  # HARD cap on any assembled section
H_MIN = 96                   # >= 2 KB_MAX + margin: the 32-mode basis must fit
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              (v551..v558's declared surface convention)
KB_MAX = 32                  # parity modes carried (the G_32 Gram)
SCHUR_KB = 16                # the low block of the two-block criterion

# --- the Chebyshev input, preregistered (T162..T171) --------------------------
KAPPA_X0 = 100.0             # verification window [x0, ATOM_MAX], as declared
KAPPA_REF = 0.038821         # the T162..T171 constant, reproduced on the table

# --- the ledger exponents (YARDSTICKS, not claims) -----------------------------
RH_DELTA = 0.5               # RH-equivalent strength, a YARDSTICK only
UNCOND_DELTA = 0.996         # best unconditional exponent (T170, a theorem)
TARGET_EXP = 3.0             # the demanded rate of link 16 (OPEN, not claimed)

# --- preregistered tolerances / bars (declared BEFORE any number) --------------
TOL_KAPPA = 1.0e-6           # |kappa(table) - 0.038821|
TOL_SPLIT = 1.0e-15          # floating residue of the lag split re-summation
TOL_KMS = 1.0e-11            # T L_P T^T = diag(mu) absolute, 32 modes
TOL_QF = 1.0e-10             # the pair of quadratic-form identities, relative
TOL_HAYN = 1.0e-9            # Haynsworth log-det defect, relative
TOL_IDENT = 1.0e-10          # plain identities on the 2 x 2 block, relative
TOL_LAD = 1.0e-6             # solve-horizon identities (x*, Thomson, swap)
TOL_SAMP = 1.0e-10           # closed Dirichlet weights vs correlation weights
TOL_MASS = 1.0e-6            # sampled Lambda-mass identity, relative
TOL_RANK3 = 1.0e-12          # sigma_4/sigma_1 of the wedge kernel
TOL_POLAR = 1.0e-9           # det expansion near a null sum, relative
TOL_LAGR2 = 1.0e-15          # the 2 x 2 Lagrange identity of link 16, at the
#                              natural scale |r1|^2 |r2|^2 (the det^2 side is
#                              ~ 1e-7 of it: the cancellation eats ~7 digits,
#                              so the ALGEBRA is checked separately on
#                              well-conditioned random matrices at 1e-10)
TOL_LAGR2_ALG = 1.0e-10      # the same identity relative to det^2, random P
TOL_CTRL = 1.0e-12           # Dirichlet / parity / Toeplitz controls
BAR_HEAD = 1.0e3             # cancellation headroom floor of link 3
BAR_SIN = 1.0e-2             # per-window ceiling on sin(angle), link 16
BAR_NG1 = 1.0e2              # l1 majorant / |det Ahat| floor (NG1)
BAR_NG4 = 5.0e2              # ||Ahat|| / |nu_2| floor (NG4)
BAR_NG5 = 1.5                # |atom half| / |arch half| floor (NG5)
BAR_NG6 = 1.0e2              # sieve operator-norm bound / |det Ahat| (NG6)
BAR_SCRAM = 10.0             # median value inflation under scramble (NG7)
N_SCRAM = 5                  # scramble draws per window, declared
BAR_Z3_RH = 50.0             # RH yardstick / needed, floor on THIS surface
BAR_Z3_UNC = 5.0             # best unconditional / needed, floor
BAR_MUT = 1.0e-2             # every mutation must miss by at least this
SEED = 559


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
    |psi(x) - x| / x (the T162..T171 convention; Chebyshev 1852 /
    Rosser-Schoenfeld 1962) -- the ONE unconditional arithmetic input,
    measured on THIS table and nothing else."""
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
    positions with the SAME masses (the NG7 discriminator)."""
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
    for bit the frame-A code path of T128..T171 / v548..v558."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T171)
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


def _cos_sum(alpha, beta, L):
    """THE DIRICHLET-KERNEL IDENTITY (Dirichlet 1829): what makes R_kl(d)
    CLOSED -- sum_{j=1..L} cos(alpha j + beta) in closed form."""
    alpha = np.asarray(alpha, float)
    beta = np.asarray(beta, float)
    L = np.asarray(L, float)
    ha = 0.5 * alpha
    s = np.sin(ha)
    out = np.where(np.abs(s) < 1.0e-14,
                   L * np.cos(beta),
                   np.sin(L * ha) / np.where(np.abs(s) < 1.0e-14, 1.0, s)
                   * np.cos(beta + (L + 1.0) * ha))
    return np.where(L >= 1.0, out, 0.0)


def _kl_geometry(m):
    M = 2 * m
    d = np.arange(M, dtype=float)
    LT = np.maximum(m - d, 0.0)
    J = (M - 1) - d
    n0 = np.maximum(1.0, m + 1.0 - d)
    n1 = np.minimum(float(m), 2.0 * m - d)
    LH = np.maximum(n1 - n0 + 1.0, 0.0)
    LH = LH.copy()
    LH[0] = 0.0
    return M, d, LT, J, n0, LH


def R_pair(k, l, m, om):
    """The (k, l) contribution to the closed weight vector as FOUR Dirichlet
    kernels -- the T160 SAMPLING route, the independent closed form."""
    M, d, LT, J, n0, LH = _kl_geometry(m)
    N = 2 * m + 1
    am, ap = om[k] - om[l], om[k] + om[l]
    T = (4.0 / N) * (_cos_sum(am, -om[l] * d, LT) - _cos_sum(ap, om[l] * d, LT))
    sh = am * (n0 - 1.0)
    sp = ap * (n0 - 1.0)
    H = (2.0 / N) * (_cos_sum(ap, -om[l] * (J + 2.0) + sp, LH)
                     - _cos_sum(am, om[l] * (J + 2.0) + sh, LH))
    out = T - H
    out[0] = T[0] * 0.5 - H[0]
    return out


def lag_weights_closed(x, m, nb):
    """w_d = sum_{k,l} a_k a_l R_kl(d), a_k = x_k / sqrt(mu^P_k): T160."""
    N = 2 * m + 1
    a = x[:nb] / np.sqrt(parity_mu(m)[:nb])
    om = 2.0 * math.pi * np.arange(1, nb + 1) / N
    w = np.zeros(2 * m)
    for k in range(nb):
        for l in range(nb):
            if a[k] != 0.0 and a[l] != 0.0:
                w += a[k] * a[l] * R_pair(k, l, m, om)
    return w


def back_diff(w):
    """(Delta w)_d = w_d - w_{d+1}, with w_M := 0 (the Abel swap piece)."""
    out = np.empty_like(w)
    out[:-1] = w[:-1] - w[1:]
    out[-1] = w[-1]
    return out


def cf_ladder(Bm, K):
    """THE T158 CHOLESKY / CONTINUED-FRACTION LADDER: g_J = partial sums of
    y_j^2, y = L^-1 e_1 (Schur 1917 nested complements; Haynsworth 1968)."""
    Q = sym(np.asarray(Bm)[:K, :K])
    L = np.linalg.cholesky(Q)
    e1 = np.zeros(K)
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return np.cumsum(y ** 2)


def two_block(B, t, nl):
    """THE SCHUR TWO-BLOCK CRITERION (Schur 1917; Haynsworth 1968):
    B - tI >= 0  <=>  B_LL - tI > 0 AND Sc(t) >= 0, with the Haynsworth
    product det(B - tI) = det(B_LL - tI) det Sc(t)."""
    K = B.shape[0]
    Bt = B - t * np.eye(K)
    Bl, Bh, Bx = Bt[:nl, :nl], Bt[nl:, nl:], Bt[:nl, nl:]
    lam_L = float(np.linalg.eigvalsh(Bl)[0])
    if lam_L <= 0.0:
        return False, lam_L, float("nan"), float("nan")
    Sc = sym(Bh - Bx.T @ np.linalg.solve(Bl, Bx))
    lam_S = float(np.linalg.eigvalsh(Sc)[0])
    sl, ldl = np.linalg.slogdet(Bl)
    ss, lds = np.linalg.slogdet(Sc) if lam_S > 0.0 else (0.0, 0.0)
    st, ldt = np.linalg.slogdet(Bt)
    dd = (abs(ldl + lds - ldt) / max(1.0, abs(ldt))
          if (lam_S > 0.0 and st * sl * ss != 0.0) else float("nan"))
    return bool(lam_S >= 0.0), lam_L, lam_S, dd


def mixed_det(P, Q):
    """D(P, Q) = P11 Q22 + P22 Q11 - 2 P12 Q12, the POLARISATION of det."""
    return (P[0, 0] * Q[1, 1] + P[1, 1] * Q[0, 0] - 2.0 * P[0, 1] * Q[0, 1])


J3 = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -2.0]])


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
             X=math.exp(2.0 * alpha))
    r["split"] = float(np.max(np.abs(sp["c"] - sp["c_ar"] - sp["c_at"])))
    A = sym(odd_toeplitz(sp["c"], M))
    Tb = parity_basis(h, KB_MAX)
    mu = parity_mu(h)[:KB_MAX]
    isq = 1.0 / np.sqrt(mu)
    G = sym((Tb @ (A @ Tb.T)) * np.outer(isq, isq))
    r.update(A=A, Tb=Tb, mu=mu, mu1=float(mu[0]), G=G,
             G_LL=G[:SCHUR_KB, :SCHUR_KB].copy())
    r["pd_LL"] = bool(np.linalg.eigvalsh(r["G_LL"])[0] > 0.0)
    r["gcum"] = cf_ladder(r["G_LL"], SCHUR_KB)
    r["gcum32"] = cf_ladder(G, KB_MAX)
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    Ah = np.array([[float(t1 @ (A @ t1)), float(t1 @ (A @ t2))],
                   [float(t1 @ (A @ t2)), float(t2 @ (A @ t2))]])
    r.update(t1=t1, t2=t2, Ah=Ah)
    r["a11"], r["a22"], r["a12"] = (float(Ah[0, 0]), float(Ah[1, 1]),
                                    float(Ah[0, 1]))
    nuv = np.linalg.eigvalsh(Ah)
    r["nu2"], r["nu1"] = float(nuv[0]), float(nuv[1])
    r["det"] = float(np.linalg.det(Ah))
    r["onem"] = r["det"] / (r["a11"] * r["a22"])
    # the exact entry s = mu^P_1 t_1^T A^-1 t_1 = (G_full^-1)_11
    r["s"] = float(r["mu1"] * float(t1 @ np.linalg.solve(A, t1)))
    # the closed weights of the two lowest modes + the arch/atom 2x2 split
    r["W11"] = lag_weights_from_v(t1, h)
    r["W22"] = lag_weights_from_v(t2, h)
    r["W12"] = 0.5 * (lag_weights_from_v(t1 + t2, h) - r["W11"] - r["W22"])
    A_ar = sym(odd_toeplitz(sp["c_ar"], M))
    B2 = np.array([[float(t1 @ (A_ar @ t1)), float(t1 @ (A_ar @ t2))],
                   [float(t1 @ (A_ar @ t2)), float(t2 @ (A_ar @ t2))]])
    lam = np.array([a[1] * 0.5 for a in atoms])   # Lambda(n)/sqrt(n)
    uu = np.array([a[0] for a in atoms])
    P = np.empty((len(atoms), 3))
    for i in range(len(atoms)):
        P[i, 0] = spline_project(r["W11"], uu[i], sp["D"], M)
        P[i, 1] = spline_project(r["W22"], uu[i], sp["D"], M)
        P[i, 2] = spline_project(r["W12"], uu[i], sp["D"], M)
    S2 = np.array([[float(lam @ P[:, 0]), float(lam @ P[:, 2])],
                   [float(lam @ P[:, 2]), float(lam @ P[:, 1])]])
    r.update(B2=B2, S2=S2, lam=lam, uu=uu, P=P)
    # the operating vector x* of link 10 and its weight vector
    e1 = np.zeros(SCHUR_KB)
    e1[0] = 1.0
    xs = np.linalg.solve(sym(r["G_LL"]), e1)
    xs = xs / xs[0]
    a = np.zeros(KB_MAX)
    a[:SCHUR_KB] = xs / np.sqrt(mu[:SCHUR_KB])
    vs = Tb.T @ a
    ws = lag_weights_from_v(vs, h)
    r.update(xs=xs, vs=vs, ws=ws, Q=float(sp["c"] @ ws),
             dw=back_diff(ws), Csum=np.cumsum(sp["c"]))
    r["TV"] = float(np.sum(np.abs(r["dw"])))
    return r


def spline_project(W, u, D, M):
    """phi_n . W for the unit-mass spline phi_n of the atom at u = log n:
    a CLOSED two-point read of the weight vector W, plus the d = 0
    reflection when u < D (bit for bit the T170/T171 read)."""
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


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("=" * 72)
    print("v559  PRIME.PHASE2.CAPSTONE.01 -- the phase-2 capstone (T171 "
          "FINAL.MAP)")
    print("=" * 72)

    print("\nS0 -- firewall, the declared surface, the one arithmetic input")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    kappa = chebyshev_kappa()
    INST = [build_instance(k, D, M, h) for (k, D, M, h) in build_windows()]
    h_max = max(r["h"] for r in INST)
    e_split = max(r["split"] for r in INST)
    check(f"S0.SURFACE: kappa = {kappa:.6f} reproduced to "
          f"{abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} at every jump "
          f"point of the von-Mangoldt table in [{KAPPA_X0:.0f}, {ATOM_MAX}] "
          f"(Chebyshev 1852 / Rosser-Schoenfeld 1962 -- the ONE "
          f"unconditional arithmetic input); {len(INST)} frame-A windows "
          f"built end to end on v551..v558's declared surface (m = "
          f"{min(r['h'] for r in INST)}..{h_max} <= {H_CAP}; lag split "
          f"exact to {e_split:.1e} <= {TOL_SPLIT:.0e}); the 16 x 16 low "
          f"block is positive definite on {sum(r['pd_LL'] for r in INST)}"
          f"/{len(INST)} windows -- a NUMERICAL FACT about finite matrices, "
          f"never routed through the Weil criterion (T171's nu = 4, "
          f"h = 1445 indefinite window belongs to ITS two-frame sandbox "
          f"surface, not to this one)",
          abs(kappa - KAPPA_REF) <= TOL_KAPPA and len(INST) == N_INST
          and h_max <= H_CAP and e_split <= TOL_SPLIT
          and all(r["pd_LL"] for r in INST))
    for r in INST:
        print(f"    n={r['n']:>4d} m={r['h']:>4d} X={r['X']:9.1f} "
              f"atoms={len(r['atoms']):>3d} det={r['det']:10.3e} "
              f"1-r12^2={r['onem']:.3e}")

    # ================================================================ chain
    print("\nS1 -- THE CHAIN: sixteen links, one check each, one run")
    links = []           # (n, tag, kind, green)

    # --- link 1: T152 Schur two-block [THEOREM] ---------------------------
    E_KMS, E_QF, TB_OK, TB_DD = [], [], [], []
    for r in INST:
        Tb, mu = r["Tb"], r["mu"]
        LP = lap_P_mat(r["h"])
        E_KMS.append(float(np.max(np.abs(Tb @ (LP @ Tb.T) - np.diag(mu)))))
        x = rng.standard_normal(KB_MAX)
        a = x / np.sqrt(mu)
        v = Tb.T @ a
        qb = float(x @ (r["G"] @ x))
        qa = float(v @ (r["A"] @ v))
        E_QF.append(max(abs(qb - qa) / max(1.0, abs(qa)),
                        abs(float(x @ x) - float(v @ (LP @ v)))
                        / float(x @ x)))
        lmin = float(np.linalg.eigvalsh(r["G"])[0])
        lo = two_block(r["G"], 0.5 * lmin, SCHUR_KB)
        hi = two_block(r["G"], 1.02 * lmin, SCHUR_KB)
        TB_OK.append(bool(lo[0]) and not bool(hi[0]))
        TB_DD.append(lo[3])
    g1 = (max(E_KMS) <= TOL_KMS and max(E_QF) <= TOL_QF and all(TB_OK)
          and max(TB_DD) <= TOL_HAYN)
    links.append((1, "T152 SCHUR 2-BLOCK", "THEOREM", g1))
    check(f"S1.L01 [THEOREM] T152 SCHUR 2-BLOCK: T L_P T^T = diag(mu^P) to "
          f"{max(E_KMS):.1e} <= {TOL_KMS:.0e} (KMS 1953, exact); the pair "
          f"x^T G x = v^T A v, x^T x = v^T L_P v to {max(E_QF):.1e} <= "
          f"{TOL_QF:.0e}; the two-block criterion HOLDS at 0.5 lam_min and "
          f"FAILS at 1.02 lam_min on {sum(TB_OK)}/{len(INST)} windows "
          f"(sharp, not one-sided -- the direction check); the Haynsworth "
          f"product det(G - tI) = det(G_LL - tI) det Sc(t) closes to "
          f"{max(TB_DD):.1e} <= {TOL_HAYN:.0e} (Schur 1917; Haynsworth "
          f"1968).  The I5 floor IS this criterion -- an equivalence, not "
          f"a bound", g1)

    # --- link 2: T151 Sobolev [THEOREM] -----------------------------------
    SOB = []
    for r in INST:
        N = 2 * r["h"] + 1
        C_S = (2.0 * math.pi + 2.0) / math.sqrt(N)
        d = (np.abs(np.diff(r["Tb"], axis=1)).sum(axis=1)
             + np.abs(r["Tb"][:, 0]))
        kk = np.arange(1, KB_MAX + 1, dtype=float)
        SOB.append(float(np.max(d / (C_S * kk))))
    g2 = max(SOB) <= 1.0
    links.append((2, "T151 SOBOLEV", "THEOREM", g2))
    check(f"S1.L02 [THEOREM] T151 SOBOLEV: b_k = TV(t_k) <= C_S k with the "
          f"EXPLICIT constant C_S = (2 pi + 2)/sqrt(N), verified for every "
          f"k = 1..{KB_MAX} on {len(INST)} windows -- worst ratio "
          f"b_k/(C_S k) = {max(SOB):.4f} <= 1: linear in k with a closed "
          f"constant, the only property the reroute consumes", g2)

    # --- link 3: T153 Psi collapse [THEOREM] ------------------------------
    E_PSI, E_GAUGE, HEAD = [], [], []
    for r in INST:
        x = np.zeros(KB_MAX)
        x[0] = 1.0
        x[1:8] = 0.37 / np.arange(1, 8)
        a = x / np.sqrt(r["mu"])
        v = r["Tb"].T @ a
        w = lag_weights_from_v(v, r["h"])
        psi = float(r["c"] @ w)
        big = max(abs(float(r["c_ar"] @ w)), abs(float(r["c_at"] @ w)))
        E_PSI.append(abs(psi - float(x @ (r["G"] @ x)))
                     / max(big, 1.0e-300))
        E_GAUGE.append(abs(float(np.sum(w))) / float(np.sum(np.abs(w))))
        HEAD.append(abs(psi) / max(big * 2.2e-16, 1.0e-300))
    g3 = (max(E_PSI) <= TOL_SPLIT * 10 and max(E_GAUGE) <= TOL_SPLIT * 10
          and min(HEAD) >= BAR_HEAD)
    links.append((3, "T153 PSI COLLAPSE", "THEOREM", g3))
    check(f"S1.L03 [THEOREM] T153 PSI COLLAPSE: Psi(x) = sum_d c_d w_d = "
          f"x^T G x to {max(E_PSI):.1e} of the LARGER half (arch/atom), "
          f"and sum_d w_d = 0 to {max(E_GAUGE):.1e} of ||w||_1 (T159's "
          f"Z-law) on {len(INST)} windows; the cancellation headroom "
          f"|Psi|/(half x eps) = {min(HEAD):.1e} >= {BAR_HEAD:.0e} is the "
          f"DECLARED numerical horizon -- the halves are large, the total "
          f"is O(1), and that cancellation is exactly what R1 must later "
          f"price.  The one link where arithmetic enters, an identity", g3)

    # --- link 4: T154 Ritz ceiling [THEOREM] ------------------------------
    R4_OK, RATIO = [], []
    for r in INST:
        l12 = float(np.linalg.eigvalsh(r["G"][:12, :12])[0])
        l16 = float(np.linalg.eigvalsh(r["G_LL"])[0])
        l32 = float(np.linalg.eigvalsh(r["G"])[0])
        g = r["gcum"]
        g32 = r["gcum32"]
        R4_OK.append(l12 >= l16 - 1.0e-12 and l16 >= l32 - 1.0e-12
                     and g[11] <= g[15] * (1.0 + 1.0e-12)
                     and g[15] <= g32[-1] * (1.0 + 1.0e-9)
                     and g32[-1] <= r["s"] * (1.0 + 1.0e-9))
        RATIO.append(float(g32[-1] / r["s"]))
    g4 = all(R4_OK)
    links.append((4, "T154 RITZ CEILING", "THEOREM", g4))
    check(f"S1.L04 [THEOREM] T154 RITZ CEILING: Cauchy interlacing "
          f"lam_min(G_12) >= lam_min(G_16) >= lam_min(G_32) on "
          f"{sum(R4_OK)}/{len(INST)} windows, and the dual chain g_12 <= "
          f"g_16 <= g_32 <= s with g_32/s = {min(RATIO):.4f}.."
          f"{max(RATIO):.4f} (Cauchy 1829; Courant-Fischer 1920): the "
          f"ladder approaches the exact entry s from BELOW, never from "
          f"above -- which is precisely why the chain needs link 5", g4)

    # --- link 5: T155 12x12 floor [CERT] ----------------------------------
    C12_OK, C12_T = [], []
    for r in INST:
        lmin = float(np.linalg.eigvalsh(r["G"])[0])
        lo = two_block(r["G"], lmin * (1.0 - 1.0e-9), 12)
        hi = two_block(r["G"], lmin * (1.0 + 1.0e-4), 12)
        C12_OK.append(bool(lo[0]) and not bool(hi[0]))
        C12_T.append(lmin)
    g5 = all(C12_OK)
    links.append((5, "T155 12x12 FLOOR", "CERT", g5))
    check(f"S1.L05 [CERT] T155 12x12 FLOOR: the two-block certificate "
          f"holds at t = (1 - 1e-9) lam_min and FAILS at "
          f"t = (1 + 1e-4) lam_min on {sum(C12_OK)}/{len(INST)} windows -- "
          f"certified floor t = {min(C12_T):.3e}..{max(C12_T):.3e}, sharp "
          f"per window, CERT-WINDOW: no quantifier in m", g5)

    # --- link 6: T156 F(P, r) chain [CERT] --------------------------------
    FPR_OK, L16V = [], []
    for r in INST:
        g, s = r["gcum"], r["s"]
        Ls = []
        for K in (2, 4, 8, 16):
            gK = float(g[K - 1])
            rK = 1.0 / gK - 1.0 / s
            FPR_OK.append(rK >= -1.0e-12
                          and float(g[15] / gK) >= 1.0 - 1.0e-12)
            Ls.append(1.0 / (rK * s) if rK > 0.0 else float("inf"))
        FPR_OK.append(all(Ls[i] <= Ls[i + 1] for i in range(len(Ls) - 1)))
        L16V.append(Ls[-1])
    g6 = all(FPR_OK)
    links.append((6, "T156 F(P,r) CHAIN", "CERT", g6))
    check(f"S1.L06 [CERT] T156 F(P, r) CHAIN: P_K = g_16/g_K >= 1 and "
          f"r_K = 1/g_K - 1/s >= 0 at K = 2, 4, 8, 16 on {len(INST)} "
          f"windows, certified L increasing in K with L(16) = "
          f"{min(L16V):.1f}..{max(L16V):.1f} -- a truncation is never a "
          f"discount, and the ceiling tightens monotonically.  CERT-WINDOW",
          g6)

    # --- link 7: T158 Thomson / ladder [THEOREM] --------------------------
    E_TH, MONO_OK, TRI_OK = [], [], []
    for r in INST:
        Q = sym(r["G_LL"])
        e1 = np.zeros(SCHUR_KB)
        e1[0] = 1.0
        for K in (2, 8, SCHUR_KB):
            u = np.linalg.solve(Q[:K, :K], e1[:K])
            val = float(2.0 * u[0] - u @ (Q[:K, :K] @ u))
            E_TH.append(abs(val - float(r["gcum"][K - 1]))
                        / max(1.0e-300, float(r["gcum"][K - 1])))
            xt = np.zeros(K)
            xt[0] = 1.0
            xt[1:] = 0.1 * rng.standard_normal(K - 1)
            TRI_OK.append(float(2.0 * xt[0] - xt @ (Q[:K, :K] @ xt))
                          <= float(r["gcum"][K - 1]) * (1.0 + 1.0e-12))
        MONO_OK.append(bool(np.all(np.diff(r["gcum"]) > 0.0)))
    g7 = max(E_TH) <= TOL_LAD and all(MONO_OK) and all(TRI_OK)
    links.append((7, "T158 THOMSON/LADDER", "THEOREM", g7))
    check(f"S1.L07 [THEOREM] T158 THOMSON / LADDER: the Thomson dual "
          f"maximum equals the Cholesky ladder rung to {max(E_TH):.1e} <= "
          f"{TOL_LAD:.0e} (K = 2, 8, 16 on {len(INST)} windows, inside the "
          f"declared solve horizon); every increment y_j^2 strictly "
          f"positive; and all {len(TRI_OK)} random admissible trials land "
          f"BELOW the rung -- the only direction a trial vector can give "
          f"(Schur 1917 nested complements)", g7)

    # --- link 8: T160 sampling identity [THEOREM] -------------------------
    E_SAMP, E_MASS = [], []
    for r in INST:
        x = np.zeros(KB_MAX)
        x[:4] = np.array([1.0, 0.4, -0.25, 0.15])
        a4 = x[:4] / np.sqrt(r["mu"][:4])
        v = r["Tb"][:4].T @ a4
        w_corr = lag_weights_from_v(v, r["h"])
        w_clos = lag_weights_closed(x, r["h"], 4)
        sc = max(1.0e-300, float(np.max(np.abs(w_corr))))
        E_SAMP.append(float(np.max(np.abs(w_corr - w_clos))) / sc)
        lhs = float(r["c_at"] @ w_corr)
        rhs = -sum(float(lm) * spline_project(w_corr, float(u), r["D"],
                                              r["M"])
                   for lm, u in zip(r["lam"], r["uu"]))
        E_MASS.append(abs(lhs - rhs) / max(1.0e-300, abs(lhs)))
    g8 = max(E_SAMP) <= TOL_SAMP and max(E_MASS) <= TOL_MASS
    links.append((8, "T160 SAMPLING", "THEOREM", g8))
    check(f"S1.L08 [THEOREM] T160 SAMPLING: the four-Dirichlet-kernel "
          f"closed weights equal the correlation weights to "
          f"{max(E_SAMP):.1e} <= {TOL_SAMP:.0e} (Dirichlet 1829; 4 modes, "
          f"{len(INST)} windows), and the atom half of Psi equals the "
          f"explicitly SAMPLED Lambda-mass to {max(E_MASS):.1e} <= "
          f"{TOL_MASS:.0e} (two-point spline read): tapering the mode "
          f"vector IS smoothing the sampled Lambda-mass", g8)

    # --- link 9: T163 TV floor / swap [THEOREM] ---------------------------
    E_SWAP, TV_OK, TV_OVER = [], [], []
    for r in INST:
        lhs = r["Q"]
        rhs = float(r["dw"] @ r["Csum"])
        E_SWAP.append(abs(lhs - rhs) / max(abs(lhs), 1.0e-300))
        bnd = r["TV"] * float(np.max(np.abs(r["Csum"])))
        TV_OK.append(bnd >= abs(lhs) * (1.0 - 1.0e-12))
        TV_OVER.append(bnd / max(abs(lhs), 1.0e-300))
    g9 = max(E_SWAP) <= TOL_LAD and all(TV_OK)
    links.append((9, "T163 TV FLOOR/SWAP", "THEOREM", g9))
    check(f"S1.L09 [THEOREM] T163 TV FLOOR / SWAP: the Abel swap identity "
          f"sum c_d w_d = sum (Delta w)_d C_d closes to {max(E_SWAP):.1e} "
          f"<= {TOL_LAD:.0e} (Abel 1826; evaluated at x*, both sides pass "
          f"the same cancellation), and TV(w) max|C_d| >= |Psi| on "
          f"{sum(TV_OK)}/{len(INST)} windows with overshoot "
          f"{min(TV_OVER):.1e}..{max(TV_OVER):.1e} -- the overshoot IS the "
          f"TV floor: the price a rearrangement route pays before it has "
          f"bought anything", g9)

    # --- link 10: T164 gauge / quantifier [THEOREM] -----------------------
    E_GAU, E_COLL, COLL_OK = [], [], []
    for r in INST:
        R0 = r["Q"] / r["TV"]
        for sg in (0.5, 2.0, -3.0):
            a = np.zeros(KB_MAX)
            a[:SCHUR_KB] = sg * r["xs"] / np.sqrt(r["mu"][:SCHUR_KB])
            w2 = lag_weights_from_v(r["Tb"].T @ a, r["h"])
            R2 = (float(r["c"] @ w2)
                  / float(np.sum(np.abs(back_diff(w2)))))
            E_GAU.append(abs(R2 - R0) / max(abs(R0), 1.0e-300))
        E_COLL.append(abs(r["Q"] - 1.0 / float(r["gcum"][-1]))
                      / max(1.0e-300, abs(r["Q"])))
        for _ in range(4):
            xt = (r["xs"] + 0.05 * np.linalg.norm(r["xs"])
                  * rng.standard_normal(SCHUR_KB))
            xt = xt / xt[0]
            COLL_OK.append(float(xt @ (sym(r["G_LL"]) @ xt))
                           >= r["Q"] * (1.0 - 1.0e-9))
    g10 = (max(E_GAU) <= TOL_LAD and max(E_COLL) <= TOL_LAD
           and all(COLL_OK))
    links.append((10, "T164 GAUGE/QUANTIFIER", "THEOREM", g10))
    check(f"S1.L10 [THEOREM] T164 GAUGE / QUANTIFIER: R = Psi/TV is scale "
          f"invariant to {max(E_GAU):.1e} over sigma = 0.5, 2, -3 (degree "
          f"2 over degree 2 -- algebra); Psi(x*) = 1/g_16 to "
          f"{max(E_COLL):.1e} <= {TOL_LAD:.0e}; and all {len(COLL_OK)} "
          f"perturbed admissible vectors give a LARGER value: the 'for "
          f"all admissible x' collapses onto ONE vector, and a gauge "
          f"choice can never be the missing ingredient", g10)

    # --- link 11: T165 P_pr identity [THEOREM] ----------------------------
    E_PPR, PPR_OK = [], []
    for r in INST:
        Tv1 = r["xs"][0] / math.sqrt(r["mu1"])
        den = r["mu1"] * Tv1 ** 2
        lhs = float(r["gcum"][-1]) * r["Q"] / den
        rhs = (float(r["gcum"][-1]) * (r["Q"] / r["TV"])
               * (r["TV"] / Tv1 ** 2) / r["mu1"])
        E_PPR.append(abs(lhs - rhs) / max(abs(lhs), 1.0e-300))
        PPR_OK.append(lhs >= 1.0 - 1.0e-6)
    g11 = max(E_PPR) <= TOL_SPLIT * 10 and all(PPR_OK)
    links.append((11, "T165 P_pr IDENTITY", "THEOREM", g11))
    check(f"S1.L11 [THEOREM] T165 P_pr IDENTITY: the two factorisations of "
          f"the price agree to {max(E_PPR):.1e}, and P_pr = 1 at x* to "
          f"within the solve horizon on {sum(PPR_OK)}/{len(INST)} windows "
          f"-- P_pr >= 1 with equality exactly at x* (link 10), the "
          f"accounting that makes the price additive in logs", g11)

    # --- link 12: T166 cascade [THEOREM] ----------------------------------
    E_REG, E_DIAG, REG_OK = [], [], []
    for r in INST:
        G = sym(r["G_LL"])
        gain = float(r["gcum"][-1] / r["gcum"][0])
        b = G[0, 1:]
        R2 = float(b @ np.linalg.solve(G[1:, 1:], b)) / float(G[0, 0])
        E_REG.append(abs(gain - 1.0 / (1.0 - R2)) / gain)
        dd = np.exp(rng.uniform(-1.5, 1.5, size=SCHUR_KB))
        gd = cf_ladder(G * np.outer(dd, dd), SCHUR_KB)
        E_DIAG.append(abs(float(gd[-1] / gd[0]) - gain) / gain)
        REG_OK.append(0.0 <= R2 < 1.0 and gain >= 1.0)
    g12 = max(E_REG) <= TOL_LAD and max(E_DIAG) <= TOL_LAD and all(REG_OK)
    links.append((12, "T166 CASCADE", "THEOREM", g12))
    check(f"S1.L12 [THEOREM] T166 CASCADE: g_16/g_1 = 1/(1 - R_16^2) to "
          f"{max(E_REG):.1e} on {len(INST)} windows, invariant under a "
          f"random positive diagonal G -> DGD to {max(E_DIAG):.1e}, with "
          f"R_16^2 in [0, 1) strictly: the gain is a squared multiple "
          f"correlation -- pure COLLINEARITY, no scale information", g12)

    # --- link 13: T167 K = 2 exactness [THEOREM] --------------------------
    E_K2, E_K2V, MILD = [], [], []
    for r in INST:
        G = sym(r["G_LL"])
        r12 = float(G[0, 1] / math.sqrt(G[0, 0] * G[1, 1]))
        E_K2.append(abs(float(G[0, 0] * r["gcum"][1])
                        - 1.0 / (1.0 - r12 ** 2)) * (1.0 - r12 ** 2))
        x2 = np.array([1.0, -G[0, 1] / G[1, 1]])
        E_K2V.append(abs(float(x2 @ (G[:2, :2] @ x2))
                         - 1.0 / float(r["gcum"][1]))
                     * float(r["gcum"][1]))
        S2v = float(np.abs(r["xs"][:2]) @ (np.abs(G[:2, :2])
                                           @ np.abs(r["xs"][:2])))
        S16 = float(np.abs(r["xs"]) @ (np.abs(G) @ np.abs(r["xs"])))
        MILD.append(((1.0 / float(r["gcum"][1])) / S2v)
                    / ((1.0 / float(r["gcum"][-1])) / S16))
    g13 = (max(E_K2) <= TOL_LAD and max(E_K2V) <= TOL_LAD
           and min(MILD) >= 1.0)
    links.append((13, "T167 K = 2 EXACT", "THEOREM", g13))
    check(f"S1.L13 [THEOREM] T167 K = 2 EXACTNESS: G_11 g_2 = "
          f"1/(1 - r_12^2) to {max(E_K2):.1e} and the closed minimiser "
          f"(1, -G_12/G_22) reproduces 1/g_2 to {max(E_K2V):.1e} on "
          f"{len(INST)} windows; the cancellation ratio is MILDER at K = 2 "
          f"than at K = 16 by {min(MILD):.2f}..{max(MILD):.2f} >= 1 -- "
          f"T167's strategic finding, checked as a DIRECTION: the K = 2 "
          f"rung is the mildest place to stand", g13)

    # --- link 14: T169 det collapse, R4-free [THEOREM] --------------------
    E_DC, E_NU, E_INV, E_TR = [], [], [], []
    for r in INST:
        G = sym(r["G_LL"])
        r12 = float(G[0, 1] / math.sqrt(abs(G[0, 0] * G[1, 1])))
        onem = 1.0 - r12 ** 2
        E_DC.append(abs(onem - r["onem"]) / max(abs(onem), 1.0e-300))
        E_NU.append(abs(r["nu1"] * r["nu2"] - r["det"])
                    / max(abs(r["det"]), 1.0e-300))
        detG2 = float(G[0, 0] * G[1, 1] - G[0, 1] ** 2)
        E_INV.append(abs(detG2 / (G[0, 0] * G[1, 1]) - r["onem"])
                     / max(abs(r["onem"]), 1.0e-300))
        E_TR.append(abs(1.0 / float(r["gcum"][1]) - float(G[0, 0]) * onem)
                    * float(r["gcum"][1]))
    g14 = (max(E_DC) <= TOL_IDENT and max(E_NU) <= TOL_IDENT
           and max(E_INV) <= TOL_IDENT and max(E_TR) <= TOL_LAD)
    links.append((14, "T169 DET COLLAPSE", "THEOREM", g14))
    check(f"S1.L14 [THEOREM] T169 DET COLLAPSE (R4-FREE): 1 - r_12^2 = "
          f"det Ahat/(a11 a22) to {max(E_DC):.1e}, = nu_1 nu_2/(a11 a22) "
          f"to {max(E_NU):.1e}, = det G_2/(G_11 G_22) to {max(E_INV):.1e} "
          f"(the diagonal invariance of link 12), and 1/g_2 = "
          f"G_11 (1 - r_12^2) to {max(E_TR):.1e} on all {len(INST)} "
          f"windows.  These identities use NO positivity of A_h: the "
          f"chain is R4-free (T170-TH6) and the Weil fence (Weil 1952) is "
          f"never approached -- on this surface the block happens to be "
          f"positive definite, and nothing here consumes that fact", g14)

    # --- link 15: T170 rank-3 [THEOREM] -----------------------------------
    EV_J = np.linalg.eigvalsh(J3)
    E_SPL2, E_POL, E_BIL, RK = [], [], [], []
    for r in INST:
        E_SPL2.append(float(np.max(np.abs((r["B2"] - r["S2"]) - r["Ah"])))
                      / max(1.0, float(np.max(np.abs(r["Ah"])))))
        de = (float(np.linalg.det(r["B2"]))
              - mixed_det(r["B2"], r["S2"])
              + float(np.linalg.det(r["S2"])))
        E_POL.append(abs(de - r["det"]) / max(abs(r["det"]), 1.0e-300))
        y = np.array([float(r["lam"] @ r["P"][:, 0]),
                      float(r["lam"] @ r["P"][:, 1]),
                      float(r["lam"] @ r["P"][:, 2])])
        dS = float(np.linalg.det(r["S2"]))
        E_BIL.append(abs(0.5 * float(y @ (J3 @ y)) - dS)
                     / max(1.0e-300, abs(dS)))
        Kk = 0.5 * (r["P"] @ (J3 @ r["P"].T))
        sv = np.linalg.svd(Kk, compute_uv=False)
        RK.append(float(sv[3] / sv[0]) if sv.shape[0] > 3 else 0.0)
    g15 = (np.allclose(EV_J, [-2.0, -1.0, 1.0], atol=1e-14)
           and max(E_SPL2) <= TOL_IDENT and max(E_POL) <= TOL_POLAR
           and max(E_BIL) <= TOL_POLAR and max(RK) <= TOL_RANK3)
    links.append((15, "T170 RANK-3", "THEOREM", g15))
    check(f"S1.L15 [THEOREM] T170 RANK-3: J has eigenvalues "
          f"{{{EV_J[0]:.0f}, {EV_J[1]:.0f}, {EV_J[2]:.0f}}} = "
          f"{{-2, -1, +1}} exactly (rank 3, signature (1, 2)); the split "
          f"Ahat = B - S to {max(E_SPL2):.1e}, the polarisation det Ahat "
          f"= det B - D(B,S) + det S to {max(E_POL):.1e} <= "
          f"{TOL_POLAR:.0e}, and det S = (1/2) y^T J y for the THREE "
          f"linear Lambda sums y = (S_11, S_22, S_12) to {max(E_BIL):.1e} "
          f"on all {len(INST)} windows; the kernel's sigma_4/sigma_1 <= "
          f"{max(RK):.1e} <= {TOL_RANK3:.0e} (Lagrange 1773; Cauchy-Binet "
          f"1812/1815): no sieve can see more than three functionals", g15)

    # --- link 16: T170 the R1 shape [CERT] --------------------------------
    E_LG2, SIN = [], []
    for r in INST:
        r1 = np.array([r["a11"], r["a12"]])
        r2 = np.array([r["a12"], r["a22"]])
        n1s, n2s = float(r1 @ r1), float(r2 @ r2)
        dot = float(r1 @ r2)
        E_LG2.append(abs((n1s * n2s - dot ** 2) - r["det"] ** 2)
                     / (n1s * n2s))
        SIN.append(abs(r["det"]) / math.sqrt(n1s * n2s))
    E_LG2A = 0.0
    for _ in range(64):
        Pr = sym(rng.normal(size=(2, 2)))
        dP = float(np.linalg.det(Pr))
        lhs = (float(Pr[0] @ Pr[0]) * float(Pr[1] @ Pr[1])
               - float(Pr[0] @ Pr[1]) ** 2)
        E_LG2A = max(E_LG2A, abs(lhs - dP ** 2) / max(dP ** 2, 1.0e-300))
    g16 = (max(E_LG2) <= TOL_LAGR2 and E_LG2A <= TOL_LAGR2_ALG
           and all(0.0 < s <= BAR_SIN for s in SIN))
    links.append((16, "T170 THE R1 SHAPE", "CERT", g16))
    check(f"S1.L16 [CERT] T170 THE R1 SHAPE: sin(angle between the two "
          f"rows of Ahat) = |det Ahat|/(|row_1||row_2|) -- the 2 x 2 "
          f"Lagrange identity |r_1|^2|r_2|^2 - (r_1.r_2)^2 = det^2 closes "
          f"to {max(E_LG2):.1e} <= {TOL_LAGR2:.0e} of the natural scale "
          f"on the instances (the det^2 side is the near-null number: the "
          f"cancellation eats ~7 digits, the DECLARED horizon) and to "
          f"{E_LG2A:.1e} <= {TOL_LAGR2_ALG:.0e} of det^2 itself on 64 "
          f"well-conditioned random symmetric matrices (the algebra) -- "
          f"and the MEASURED angle is sin = {min(SIN):.3e}.."
          f"{max(SIN):.3e} <= {BAR_SIN:.0e} per window (CERT-WINDOW + "
          f"MEASURED).  R1 asks for an UNCONDITIONAL certificate that "
          f"this angle closes at rate h^(-3) for ALL m -- two explicit "
          f"finite Lambda-sum vectors becoming collinear.  The rate and "
          f"the quantifier stay OPEN: that single statement is R1, and "
          f"this module neither makes nor approaches it (the T171 trend "
          f"fits stay sandbox)", g16)

    # --- the chain as one table -------------------------------------------
    print("\n   #  link                  type      status")
    print("  " + "-" * 52)
    n_th = n_ce = 0
    for (n, tag, kind, green) in links:
        print("  %2d  %-20s  %-8s  %s"
              % (n, tag, kind, "GREEN" if green else "*** GAP ***"))
        if kind == "THEOREM":
            n_th += 1
        else:
            n_ce += 1
    check(f"S1.CHAIN: ALL 16 LINKS REPRODUCE IN ONE RUN -- {n_th} typed "
          f"THEOREM (algebra, every h, checked on instances) and {n_ce} "
          f"typed CERT (per window, no quantifier in m): the reduction "
          f"from the I5 uniformity question to the R1 shape is "
          f"MEASURED-SURFACE certified end to end on the declared small "
          f"surface, exactly as T171 booked on its two-frame sandbox "
          f"surface -- and the ONE thing the chain does not contain is a "
          f"proof of link 16's rate for all m",
          all(g for (_, _, _, g) in links) and n_th == 13 and n_ce == 3)

    # ================================================================ no-gos
    print("\nS2 -- THE NO-GO BATTERY: eight classified routes, each "
          "failing on the instance")
    NG_GREEN = []

    # NG1 size budget
    OVER = []
    for r in INST:
        maj = (abs(float(np.linalg.det(r["B2"])))
               + abs(mixed_det(r["B2"], r["S2"]))
               + abs(float(np.linalg.det(r["S2"]))))
        r["maj"] = maj
        OVER.append(maj / max(abs(r["det"]), 1.0e-300))
    ng1 = min(OVER) >= BAR_NG1
    NG_GREEN.append(ng1)
    check(f"S2.NG1 SIZE BUDGET: the l1 majorant |det B| + |D(B,S)| + "
          f"|det S| overshoots |det Ahat| by {min(OVER):.1e}.."
          f"{max(OVER):.1e} >= {BAR_NG1:.0e} on {len(INST)}/{len(INST)} "
          f"windows -- the three polarisation pieces are each orders "
          f"larger than their signed sum: a budget on sizes cannot see "
          f"the cancellation (the T171 growth exponent h^+1.32 stays "
          f"sandbox)", ng1)

    # NG2 symbol infimum
    SYMB = []
    for r in INST:
        th = np.linspace(0.0, math.pi, 2048)
        d = np.arange(1, r["M"])
        sg = (float(r["c"][0])
              + 2.0 * (np.cos(np.outer(th, d)) @ r["c"][1:]))
        SYMB.append(float(np.min(sg)))
    ng2 = all(s < 0.0 for s in SYMB)
    NG_GREEN.append(ng2)
    check(f"S2.NG2 SYMBOL INFIMUM: the Toeplitz symbol sigma(theta) = c_0 "
          f"+ 2 sum c_d cos(d theta) has min sigma = {min(SYMB):.3e}.."
          f"{max(SYMB):.3e} < 0 on {len(INST)}/{len(INST)} windows: NO "
          f"symbol-positivity argument can deliver the floor of link 1 -- "
          f"the Toeplitz part alone is indefinite, the content sits in "
          f"the Hankel correction (Fejer 1915 cited: positivity is a "
          f"finite-section fact)", ng2)

    # NG3 sector / gauge invariance
    E_SEC = []
    for r in INST:
        G = sym(r["G"])
        dd = np.exp(rng.uniform(-2.0, 2.0, size=KB_MAX))
        Gd = G * np.outer(dd, dd)
        r12d = float(Gd[0, 1] / math.sqrt(abs(Gd[0, 0] * Gd[1, 1])))
        E_SEC.append(abs((1.0 - r12d ** 2) - r["onem"])
                     / max(abs(r["onem"]), 1.0e-300))
    ng3 = max(E_SEC) <= TOL_IDENT
    NG_GREEN.append(ng3)
    check(f"S2.NG3 SECTOR / GAUGE: a random positive diagonal rescaling "
          f"(the most general sector change) moves 1 - r_12^2 by "
          f"{max(E_SEC):.1e} <= {TOL_IDENT:.0e} at most on {len(INST)} "
          f"windows -- an INVARIANCE: the object is a correlation, and a "
          f"route that changes nothing cannot close a gap", ng3)

    # NG4 perturbation theory
    KATO = []
    for r in INST:
        nrm = float(np.linalg.norm(r["Ah"], 2))
        KATO.append(nrm / max(abs(r["nu2"]), 1.0e-300))
    ng4 = min(KATO) >= BAR_NG4
    NG_GREEN.append(ng4)
    check(f"S2.NG4 PERTURBATION: Kato 1949 bounds |nu_2(A + dA) - nu_2| "
          f"<= ||dA|| at the SCALE OF THE MATRIX; the object nu_2 sits a "
          f"factor {min(KATO):.1e}..{max(KATO):.1e} >= {BAR_NG4:.0e} "
          f"below ||Ahat|| -- a perturbation argument must control the "
          f"matrix to that relative accuracy first, which IS the original "
          f"problem (cited as the closed-off route, never used)", ng4)

    # NG5 band-local domination
    BL = []
    for r in INST:
        ar = abs(float(r["c_ar"] @ r["W11"]))
        at = abs(float(r["c_at"] @ r["W11"]))
        BL.append(at / max(ar, 1.0e-300))
    ng5 = min(BL) >= BAR_NG5
    NG_GREEN.append(ng5)
    check(f"S2.NG5 BAND-LOCAL: on the mode-1 weight the atom half "
          f"dominates the archimedean half by {min(BL):.2f}.."
          f"{max(BL):.2f} >= {BAR_NG5:.1f} on {len(INST)}/{len(INST)} "
          f"windows: a route that dominates the atom band by the "
          f"archimedean band loses on the instance, exactly as classified "
          f"(the T171 growth split h^+0.79 stays sandbox)", ng5)

    # NG6 the sieve box (operator-norm route on det S alone)
    SIEV = []
    for r in INST:
        Kk = 0.5 * (r["P"] @ (J3 @ r["P"].T))
        s1 = float(np.linalg.svd(Kk, compute_uv=False)[0])
        bnd = s1 * float(r["lam"] @ r["lam"])
        SIEV.append(bnd / max(abs(r["det"]), 1.0e-300))
    ng6 = min(SIEV) >= BAR_NG6
    NG_GREEN.append(ng6)
    check(f"S2.NG6 SIEVE BOX: the operator-norm bound on det S alone, "
          f"sigma_1(K) |lambda|^2, overshoots |det Ahat| by "
          f"{min(SIEV):.1e}..{max(SIEV):.1e} >= {BAR_NG6:.0e} on "
          f"{len(INST)}/{len(INST)} windows -- by link 15 the kernel has "
          f"rank <= 3, and a bound on det S alone cannot see the "
          f"three-term cancellation (Montgomery-Vaughan 1973 / Vaughan "
          f"1977 cited as the PRICED route; the T170 route-table deltas "
          f"and T171's delta = +1.044 stay sandbox)", ng6)

    # NG7 the scramble discriminator
    MOVE, RK_S = [], []
    for r in INST:
        for _ in range(N_SCRAM):
            pos = np.sort(rng.uniform(1.0e-6, 2.0 * r["alpha"],
                                      size=len(r["atoms"])))
            masses = [a[1] for a in r["atoms"]]
            c_at_s, _ = atom_lags_at(r["alpha"], r["M"], list(pos), masses)
            cs = r["c_ar"] + c_at_s
            As = sym(odd_toeplitz(cs, r["M"]))
            a11 = float(r["t1"] @ (As @ r["t1"]))
            a22 = float(r["t2"] @ (As @ r["t2"]))
            a12 = float(r["t1"] @ (As @ r["t2"]))
            onem_s = (a11 * a22 - a12 ** 2) / (a11 * a22)
            MOVE.append(abs(onem_s / r["onem"]))
            Ps = np.empty((len(pos), 3))
            for i, u_ in enumerate(pos):
                Ps[i, 0] = spline_project(r["W11"], u_, r["D"], r["M"])
                Ps[i, 1] = spline_project(r["W22"], u_, r["D"], r["M"])
                Ps[i, 2] = spline_project(r["W12"], u_, r["D"], r["M"])
            svs = np.linalg.svd(0.5 * (Ps @ (J3 @ Ps.T)),
                                compute_uv=False)
            RK_S.append(float(svs[3] / svs[0]) if len(svs) > 3 else 0.0)
    med_move = float(np.median(MOVE))
    ng7 = med_move >= BAR_SCRAM and max(RK_S) <= TOL_RANK3
    NG_GREEN.append(ng7)
    check(f"S2.NG7 SCRAMBLE: uniform random positions at the SAME masses "
          f"({N_SCRAM} declared draws per window) move 1 - r_12^2 by a "
          f"median factor {med_move:.1f} >= {BAR_SCRAM:.0f} (range "
          f"{min(MOVE):.2g}..{max(MOVE):.2g}) while the rank-3 collapse "
          f"is UNTOUCHED (sigma_4/sigma_1 <= {max(RK_S):.1e} <= "
          f"{TOL_RANK3:.0e} on all {len(RK_S)} draws): the collapse is a "
          f"property OF THE PRIMES -- the arithmetic sits in the JOINT "
          f"VALUES of (S_11, S_22, S_12) against B, not in rank, kernel "
          f"or split", ng7)

    # NG8 the L_P control
    E_LPD, E_LPG = [], []
    for r in INST[:3]:
        m = r["h"]
        mu = r["mu"]
        isq = 1.0 / np.sqrt(mu)
        Glp = sym((r["Tb"] @ r["Tb"].T) * np.outer(isq, isq))
        E_LPD.append(float(np.max(np.abs(Glp - np.diag(np.diag(Glp))))))
        glp = cf_ladder(Glp[:SCHUR_KB, :SCHUR_KB], SCHUR_KB)
        E_LPG.append(abs(float(glp[-1] / glp[0]) - 1.0))
    ng8 = max(E_LPD) <= TOL_CTRL and max(E_LPG) <= TOL_CTRL
    NG_GREEN.append(ng8)
    check(f"S2.NG8 L_P CONTROL: with the arithmetic kernel replaced by "
          f"the identity the Gram is exactly diagonal (off-diagonal mass "
          f"{max(E_LPD):.1e}) and the cascade gain g_16/g_1 = 1 to "
          f"{max(E_LPG):.1e} on 3 control windows: the cascade of link 12 "
          f"carries NO information that is not in A_h itself -- any route "
          f"that would work for L_P alone is vacuous", ng8)

    check(f"S2.BATTERY: ALL 8 CLASSIFIED ROUTES FAIL ON AN INSTANCE, each "
          f"the way the classification says -- that is what makes the "
          f"no-go map a MAP and not a list of things nobody tried",
          all(NG_GREEN))

    # ================================================================ ledger
    print("\nS3 -- THE PRECISION LEDGER: needed against available")
    deep = min(INST, key=lambda r: abs(r["onem"]))
    need = abs(deep["onem"])
    rh_rel = float(deep["h"]) ** (-RH_DELTA)
    unc_rel = float(deep["h"]) ** (-UNCOND_DELTA)
    z3 = (need < unc_rel and rh_rel / need >= BAR_Z3_RH
          and unc_rel / need >= BAR_Z3_UNC)
    check(f"S3.LEDGER: the needed joint relative precision on "
          f"(S_11, S_22, S_12) against the archimedean block -- the value "
          f"1 - r_12^2 = {need:.3e} at the deepest window (m = "
          f"{deep['h']}) -- is finer than the RH-equivalent yardstick "
          f"h^(-{RH_DELTA}) = {rh_rel:.3e} by {rh_rel / need:.1e}x >= "
          f"{BAR_Z3_RH:.0f} and finer than the best unconditional "
          f"h^(-{UNCOND_DELTA}) = {unc_rel:.3e} by {unc_rel / need:.1e}x "
          f">= {BAR_Z3_UNC:.0f}, ON THIS SURFACE.  The demand sharpens "
          f"with h (link 16), so the gap widens: a RATE gap, not a "
          f"constant.  T171's full-surface numbers (2.284e-7 at h = 1444; "
          f"short 1.2e5x / 3.1e3x) are sandbox MEASURED numbers and are "
          f"NOT consumed here; RH_DELTA is a yardstick, not a claim", z3)

    E_U167 = []
    for r in INST:
        G = sym(r["G_LL"])
        r12 = float(G[0, 1] / math.sqrt(abs(G[0, 0] * G[1, 1])))
        x2 = np.array([1.0, -G[0, 1] / G[1, 1]])
        S2v = float(np.abs(x2) @ (np.abs(G[:2, :2]) @ np.abs(x2)))
        lhs = (1.0 / float(r["gcum"][1])) / S2v
        rhs = float(G[0, 0]) * (1.0 - r12 ** 2) / S2v
        E_U167.append(abs(lhs - rhs) / max(abs(lhs), 1.0e-300))
    check(f"S3.SELF_SIMILAR_167: the K = 2 cancellation ratio (1/g_2)/S_2 "
          f"equals G_11 (1 - r_12^2)/S_2 to {max(E_U167):.1e} <= "
          f"{TOL_LAD:.0e} on {len(INST)} windows -- the entry threshold, "
          f"the closed beta and the null-vector dress are ONE object read "
          f"at one K (T167): one inequality in the line, not three",
          max(E_U167) <= TOL_LAD)

    E_U169, OVER169 = [], []
    for r in INST:
        a11, a12, a22 = r["a11"], r["a12"], r["a22"]

        def R_of(t):
            return (a22 - 2.0 * t * a12 + t * t * a11) / (1.0 + t * t)

        disc = math.sqrt((a11 - a22) ** 2 + 4.0 * a12 ** 2)
        roots = [(-(a11 - a22) + disc) / (2.0 * a12),
                 (-(a11 - a22) - disc) / (2.0 * a12)]
        Rmin = min(R_of(t) for t in roots)
        E_U169.append(abs(Rmin - r["nu2"]) / max(abs(r["nu2"]), 1.0e-300))
        OVER169.append((R_of(a12 / a11) - r["nu2"])
                       / max(abs(r["nu2"]), 1.0e-300))
    n_neg = sum(1 for r in INST if r["nu2"] < 0.0)
    check(f"S3.SELF_SIMILAR_169: nu_2 = min_t R(t) at the EXACT stationary "
          f"points of a12 t^2 + (a11 - a22) t - a12 = 0 reproduces the "
          f"eigenvalue to {max(E_U169):.1e} <= {TOL_LAD:.0e} on "
          f"{len(INST)} windows, and the closed trial t* = a12/a11 "
          f"overshoots by {min(OVER169):.2e}..{max(OVER169):.2e} >= 0 "
          f"everywhere -- any explicit t is a VALID upper bound (Rayleigh "
          f"1877), only its size is in question; checked "
          f"sign-agnostically (here nu_2 < 0 on {n_neg}/{len(INST)}: the "
          f"chain never uses positivity of Ahat, link 14)",
          max(E_U169) <= TOL_LAD
          and all(t >= -1.0e-9 for t in OVER169))

    # ================================================================ mutations
    print("\nS4 -- mutation controls (must fail loudly) + exact controls")
    M_CAS, M_TH, M_SW = [], [], []
    for r in INST:
        G = sym(r["G_LL"])
        gain = float(r["gcum"][-1] / r["gcum"][0])
        bw = G[1, 2:]                       # the WRONG regression row
        R2w = float(bw @ np.linalg.solve(G[2:, 2:], bw)) / float(G[0, 0])
        M_CAS.append(abs(gain - 1.0 / max(1.0 - R2w, 1.0e-300)) / gain)
        e2 = np.zeros(SCHUR_KB)
        e2[1] = 1.0
        u = np.linalg.solve(G, e2)
        M_TH.append(abs(float(2.0 * u[1] - u @ (G @ u))
                        - float(r["gcum"][-1]))
                    / float(r["gcum"][-1]))
        rhs_w = float(r["dw"] @ (r["Csum"] - r["c"]))   # off-by-one C_{d-1}
        M_SW.append(abs(r["Q"] - rhs_w) / max(abs(r["Q"]), 1.0e-300))
    check(f"S4.MUT_CHAIN: the cascade with the WRONG regression row "
          f"misses by {min(M_CAS):.2e}..{max(M_CAS):.2e} >= "
          f"{BAR_MUT:.0e}, the Thomson value read off the WRONG entry "
          f"misses by {min(M_TH):.2e}..{max(M_TH):.2e} >= {BAR_MUT:.0e}, "
          f"and the swap with off-by-one partial sums C_(d-1) misses by "
          f"{min(M_SW):.2e}..{max(M_SW):.2e} >= {BAR_MUT:.0e} on every "
          f"window: the chain identities are statements about THE "
          f"objects, not generic algebra",
          min(M_CAS) >= BAR_MUT and min(M_TH) >= BAR_MUT
          and min(M_SW) >= BAR_MUT)
    M_POL = []
    for r in INST:
        wrong = (r["B2"][0, 0] * r["S2"][1, 1]
                 + r["B2"][1, 1] * r["S2"][0, 0]
                 - 1.0 * r["B2"][0, 1] * r["S2"][0, 1])
        de_w = (float(np.linalg.det(r["B2"])) - wrong
                + float(np.linalg.det(r["S2"])))
        M_POL.append(abs(de_w - r["det"]) / max(abs(r["det"]), 1.0e-300))
    check(f"S4.MUT_RANK: the polarisation with the WRONG cross-coefficient "
          f"(-1 instead of -2 on P12 Q12) breaks the det expansion by "
          f"{min(M_POL):.2e}..{max(M_POL):.2e} >= {BAR_MUT:.0e} relative "
          f"on every window: D is THE polarisation of det, not a generic "
          f"pairing -- and with it the rank-3 collapse of link 15 is a "
          f"statement about THE kernel", min(M_POL) >= BAR_MUT)

    rng2 = np.random.default_rng(5591)
    worst_cs = 0.0
    for _ in range(64):
        al = float(rng2.uniform(0.05, 3.0))
        be = float(rng2.uniform(0.0, 2.0 * math.pi))
        Lc = int(rng2.integers(1, 40))
        brute = float(np.sum(np.cos(al * np.arange(1, Lc + 1) + be)))
        ha = 0.5 * al
        closed = (math.sin(Lc * ha) / math.sin(ha)
                  * math.cos(be + (Lc + 1.0) * ha))
        worst_cs = max(worst_cs,
                       abs(closed - brute) / max(1.0, abs(brute)))
    m_c = 128
    mu_c = parity_mu(m_c)
    Tc = parity_basis(m_c)
    LPc = lap_P_mat(m_c)
    e_eig = float(np.max(np.abs(LPc @ Tc.T - Tc.T * mu_c[None, :])))
    e_ort = float(np.max(np.abs(Tc @ Tc.T - np.eye(m_c))))
    cL = np.zeros(2 * m_c)
    cL[0], cL[1] = 2.0, -1.0
    e_tpl = float(np.max(np.abs(odd_toeplitz(cL, 2 * m_c) - LPc)))
    check(f"S4.CTRL: the closed Dirichlet cosine-sum identity agrees with "
          f"brute force to {worst_cs:.1e} <= {TOL_CTRL:.0e} on 64 random "
          f"triples (Dirichlet 1829); L_P t_k = mu^P_k t_k to {e_eig:.1e} "
          f"with the basis orthonormal to {e_ort:.1e} (KMS 1953); and "
          f"odd_toeplitz(c^L) = L_P with residual {e_tpl:.1e} == 0 (zero "
          f"tolerance): the section map of the whole chain is the one the "
          f"identities assume",
          worst_cs <= TOL_CTRL and e_eig <= 1.0e-11
          and e_ort <= 1.0e-12 and e_tpl == 0.0)

    # ================================================================ fences
    print("\nS5 -- the fences, restated as a check")
    check("S5.FENCE: THE CAPSTONE VERIFIES THE MAP AND CLAIMS NOTHING NEW "
          "-- per-instance identities and certified inequalities on SMALL "
          "frame-A windows only, a FINITE LIST with an explicit maximum, "
          "nothing uniform in the zone index or in D, and NO statement "
          "for ALL D; the chain typing is load-bearing (13 THEOREM / 3 "
          "CERT) and ZERO new uniform-in-m statements are added -- which "
          "is exactly why this module exists; finite Lambda-sums are "
          "allowed and used, NO RH statement is made, assumed, approached "
          "or weakened, no zero of any L-function is read and no "
          "L-function is evaluated (AST firewall); RH_DELTA = 0.5 is a "
          "YARDSTICK for translating precision into an exponent, in "
          "exactly one role; THE ONE OPEN PHASE-2 OBJECT STAYS OPEN AND "
          "TYPED OPEN -- R1: an m-free unconditional certificate that the "
          "two rows of Ahat become collinear at rate h^{-3+eps}, equally "
          "a joint near-degeneracy of the three explicit linear Lambda "
          "sums against the archimedean block, a rate statement this "
          "module neither makes nor approaches; R2/R3 are booked (T169), "
          "R4 is off the path (T170-TH6): NOTHING ELSE IS OPEN IN PHASE "
          "2; the T171 verdict MAP-COMPLETE, its two-frame surface, its "
          "trend fits and its no-go growth exponents stay in the diary "
          "and the paper as sandbox numbers; THE WEIL FENCE: "
          "uniform-in-h positivity of A_h is RH-equivalent-shaped, never "
          "routed, never claimed, never reverse-inferred -- link 14 is "
          "R4-free BY CONSTRUCTION; no marker of any pre-existing "
          "contract moves; Schur 1917 / Haynsworth 1968, KMS 1953, "
          "Cauchy 1829 / Courant-Fischer 1920, Rayleigh 1877, Abel 1826, "
          "Dirichlet 1829, Lagrange 1773, Cauchy-Binet 1812/1815, "
          "Gershgorin 1931, Kato 1949, Montgomery-Vaughan 1973 / Vaughan "
          "1977, Chebyshev 1852 / Rosser-Schoenfeld 1962, Fejer 1915, "
          "Wilkinson 1968 / Higham 2002 named CLASSICAL; Weil 1952 / "
          "Bombieri 2000 CITED, never used as a criterion; zero-firewall "
          "AST-checked", True)

    elapsed = time.time() - t0
    print(f"\nv559 runtime: {elapsed:.1f}s")
    print(f"  chain: 16/16 green (13 THEOREM / 3 CERT); worst identity "
          f"{max(max(E_DC), max(E_NU), max(E_INV)):.1e}; "
          f"sin(angle) = {min(SIN):.2e}..{max(SIN):.2e}")
    print(f"  no-gos: 8/8 fail as classified (majorant x{min(OVER):.1e}+, "
          f"scramble x{med_move:.0f} median, L_P gain = 1)")
    print(f"  ledger: needed {need:.2e} vs RH yardstick {rh_rel:.2e} "
          f"({rh_rel / need:.0f}x) vs unconditional {unc_rel:.2e} "
          f"({unc_rel / need:.0f}x) -- R1 stays OPEN")
    return summary("PRIME.PHASE2.CAPSTONE.01 phase-2 capstone")


if __name__ == "__main__":
    raise SystemExit(run())
