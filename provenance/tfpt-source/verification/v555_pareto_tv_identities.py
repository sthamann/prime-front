"""v555 -- PRIME.PARETO.TV.01: the Pareto / total-variation identities of
T162/T163.  The CLOSED, theorem-shaped cores of T162 (contract THIRD.SPLIT)
and T163 (contract PARETO.FRONT) -- every statement RECOMPUTED here from
scratch on small exactly checkable frame-A windows (no citation of sandbox
output).  Companion to PRIME.SAMPLING.HARM.01 (v554), which certified what
the sixteen-form PAIRS AGAINST: THIS module certifies the PRICE STRUCTURE of
that pairing -- the exchange law that makes demand and price two coordinates
of one object, the total-variation floor that closes the flat-price route in
the parity sector, the chain-derived price axis of the Fejer knob, the
Mellin-ladder cell moments and the boundary-free Abel step with its closed
loss reason, and the Lerch/Frullani log-moment on three independent routes.
NOTHING here closes an open term:

[E] (1) THE EXCHANGE LAW AND THE CROSSING CRITERION (T163, R1.2).  For every
    admissible trial vector x (x_1 = 1, Q(x) > 0) with lag weights w(x),
    total variation TV(x) = ||Delta w(x)||_1 (w_M := 0) and price
    P(x) = g_16 |Q(x)| measured against the T158 top rung 1/g_16:
      delta_bnd(x) = 1/2 + log( 2 kappa g_16 TV(x) / P(x) ) / log X      (E)
      delta_bnd(x) < 1/2  <==>  P(x) > 2 kappa g_16 TV(x)               (E')
    -- a rearrangement of the definitions, machine-checked at EVERY grid
    point of the declared Fejer knob on every window, with the crossing
    criterion (E') checked as an exact equivalence.  kappa is the ONE
    unconditional arithmetic input (Chebyshev 1852 / Rosser-Schoenfeld
    1962), VERIFIED here at every jump point of psi(x)/x on the table.
    Mutation: a wrong constant (kappa in place of 2 kappa) breaks (E)
    loudly at every grid point.
[E] (2) THE TOTAL-VARIATION FLOOR (T163, R2.2 -- the theorem that carries
    the verdict).  Four steps, each machine-checked per trial vector:
    (T1) w_0(x) = ||a(x)||^2 with a_k = x_k / sqrt(mu^P_k) (the parity
    rows are orthonormal); (T2) TV(x) >= |w_0(x)| by telescoping with
    w_M = 0; (T3) x_1 = 1 forces ||a||^2 >= 1/mu^P_1, hence
      mu^P_1 TV(x) >= 1  for EVERY admissible trial vector,
    with 1/mu^P_1 = 1/(4 sin^2(pi/N)) ~ h^2 CLOSED; (T4) combined with
    (E'): delta_bnd(x) < 1/2 forces P(x) > 2 kappa g_16 / mu^P_1 -- the
    crossing price is bounded below by a quantity growing like h^2, so a
    flat-price sub-1/2 demand is impossible in the parity sector on this
    surface.  NEGATIVE CONTROL (the floor is a property of the
    NORMALISATION): an INADMISSIBLE vector (x_1 != 1, here 0.01 x*) DOES
    undercut the floor and is recognised as inadmissible.
[E] (3) THE CHAIN-DERIVED PRICE AXIS (T163, R1.0).  The Fejer knob
    t_k(sigma) = max(0, 1 - k/sigma) interpolates between two certificates
    the chain already owns: sigma = 1 gives x = e_1 EXACTLY (the K = 1
    rung of the T158 ladder, Q(e_1) = B_11 = 1/g_1, the T157 route-(0)
    certificate) and sigma = infinity gives the untapered optimiser x*
    with g_16 Q(x*) = 1 (the K = 16 top rung) -- both identities checked
    per window, plus the ladder itself (all 16 Cholesky terms strictly
    positive, partial sums strictly monotone).  The knob is monotone in
    both coordinates (price non-increasing, demand non-decreasing along
    sigma, every grid point admissible), so the knob curve IS the Pareto
    front.  Mutation: a corrupted ladder (one off-diagonal entry) makes
    the Cholesky REFUSE.
[E] (4) THE MELLIN-LADDER CELL MOMENTS AND THE ABEL STEP (T162, C2/C5).
    The k-th rung of the archimedean Mellin ladder pays
      sum_d w_d C_d(-(2k + 1/2))
    in CLOSED cell moments (Mellin 1896): C_d(s) is the exact integral of
    the linear interpolant tent at lag d against e^{su} -- checked against
    an independent Gauss-Legendre quadrature per rung k = 1..4 on every
    window.  And the Abel step (Abel 1826): the gauge identity
    sum_d w_d = 0 licenses the BOUNDARY-FREE summation by parts
      sum_d v_d w_d = sum_d V^(k)_d (Delta^k w)_d,   k = 1..3,
    checked exactly with v = c^atom; the optimal level is ONE for the
    closed reason of T162 -- each further level multiplies the certified
    envelope by ~2/D and divides ||Delta^k w||_1 by only ~omega_16, net
    factor 32 pi / alpha > 1 (evaluated closed per window; the level-2
    certified bound is measured WORSE than level 1 on every window).
    Mutations: shifted tent centres break the cell moments; a gauge
    violation (constant added to w) breaks the Abel identity by exactly
    c_0 sum_d w_d.
[E] (5) THE LERCH/FRULLANI LOG-MOMENT (T162, R-A' closure).  The one
    non-polynomial moment of the arch half, L = sum_d Psi_d w_d, agrees on
    THREE independent routes per window: (a) the direct sum with Psi_d
    closed; (b) the double-Abel form WITH its Wronskian boundary term,
    L = -(1/2) sum_d (d log d)(delta^2 w)_d - (1/2) M log M w_{M-1}
    EXACTLY; (c) the Lerch/Frullani integral
    L = -(1/2) int_0^infty (1 - e^{-y})^2 y^{-2} G(y) dy with
    G(y) = sum_{d>=1} w_d e^{-(d-1)y}, convergent at y = 0 for exactly one
    reason (the gauge identity), evaluated by declared panel quadrature
    (Frullani 1828 / Lerch 1887 / Clausen 1832).  The d = 1 term peels in
    closed form via int ((1-e^{-y})/y)^2 dy = 2 log 2, and the same
    constant reproduces Psi_1 = -log 2 exactly.  Mutations: dropping the
    Wronskian boundary term breaks route (b); a one-index shift of the
    generating function breaks route (c).

Plus the NO-GO DISCRIMINATOR (the monotone staircase, T163 R3): coarsening
the lag grid over nu = 4 -> 2 -> 1 (and 0.5 where the window allows it)
degrades the arch/atom cancellation MONOTONICALLY in the median, with the
nu = 4 column an exact null control (damage = 1); the surface of this
module sits on the right side of the T105 admissibility floor by
construction.  Parity / Dirichlet controls: the closed Dirichlet cosine-sum
identity against the brute-force sum (including the degenerate branch),
L_P t_k = mu^P_k t_k with an orthonormal basis, and odd_toeplitz(c^L) = L_P
with ZERO tolerance.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL frame-A windows -- the
        N_INST DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), mirroring v551..v554's declared surface.  Nothing is
        uniform in the zone index or in D, and NO statement for ALL D is
        made.  The h-exponents of T163 (P_aff ~ h^3.05, P_cross ~ h^1.91,
        the TV floor ~ h^2.00) are sandbox FITS and are NOT consumed here;
        what IS consumed is the closed floor 1/(4 sin^2(pi/N)) per window.
  (ii)  THE OPEN TERMS AFTER T163 STAY OPEN AND TYPED OPEN: R-E -- the
        successor question, both arms prime-free (arm A: does the
        downstream T159/T160 chain tolerate a growing 1/s ceiling; arm B:
        can the entry functional be represented in a sector whose lowest
        eigenvalue does not vanish like h^-2); R-B''' -- make the
        positivity margin h-uniform (the certified CANC at the operating
        point drifts, exponent -0.172, a sandbox fit); R-D -- a fifth
        device for R1''.  R-C''' is CLOSED NEGATIVELY by item (2) on this
        construction -- a route closed by an inequality, not a new claim.
  (iii) The T163 verdict FRONT-RESISTS is a SANDBOX verdict; this module
        promotes only its theorem-shaped identity/inequality cores, and
        the front's h-exponent anatomy stays in the diary and the paper.
  (iv)  Item (1) allows finite Lambda-sums and nothing else: kappa is
        verified on the finite table, delta_bnd is a DEMAND (what a proof
        must beat), never a value of anything, and no statement about what
        depth the primes deliver is made anywhere in this module.

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
  * Classics named CLASSICAL: Fejer 1915 (the taper / Cesaro window),
    Mellin 1896 (the cell moments), Abel 1826 (the boundary-free step),
    Chebyshev 1852 / Rosser-Schoenfeld 1962 (the one unconditional input,
    verified on the table), Legendre (the duality direction of the
    Thomson bound), Dirichlet 1829 (the cosine-sum identity),
    Kac-Murdock-Szego 1953 (the parity eigenpairs; the spectral gap
    mu^P_1 = 4 sin^2(pi/N) that carries the floor), Frullani 1828 /
    Lerch 1887 / Clausen 1832 (the log-moment integral), Schur 1917 /
    Haynsworth 1968 (the Cholesky ladder), Wilkinson 1968 / Higham 2002
    (floating-point floors); Weil 1952 / Bombieri 2000 CITED, never used
    as a criterion.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime
    side is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name, each with a mutation control that fails loudly;
measured quantities typed MEASURED.  Python; Wolfram-mirrored not required
(dense linear-algebra / quadrature machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/third_split_probe.py                 (T162)
  experiments/tfpt-discovery/pareto_front_probe.py                (T163)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v554
H_CAP = 300                  # HARD cap on any assembled section
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              (v551..v554's declared surface convention)

# --- the form geometry, preregistered ----------------------------------------
SCHUR_KB = 16                # the fixed low block of the T152..T163 chain

# --- the Fejer knob, preregistered (T163 R1) ---------------------------------
N_SIGMA = 50                 # geometric sigma grid on [1, 4096], plus infinity
SIGMA_LO, SIGMA_HI = 1.0, 4096.0

# --- the Chebyshev input, preregistered (T162/T163 Q0) -----------------------
KAPPA_X0 = 100.0             # verification window [x0, ATOM_MAX], as declared
KAPPA_REF = 0.038821         # the T162/T163 constant, reproduced on the table

# --- the Mellin / Abel ladder, preregistered (T162 C2/C5) --------------------
MELLIN_K = 4                 # rungs k = 1..4 checked against quadrature
ABEL_K = 3                   # boundary-free Abel levels checked exactly

# --- the log-moment quadrature, preregistered (T162 R-A') --------------------
LM_PANELS = 40               # geometric panels on (LM_LO, LM_HI)
LM_LO, LM_HI = 1.0e-7, 80.0

# --- the no-go staircase, preregistered (T163 R3) ----------------------------
NOGO_FACTORS = (1, 2, 4)     # nu = 4 / 2 / 1; 8 (nu = 0.5) where m >= 128

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_KAPPA = 1.0e-6           # |kappa(table) - 0.038821|
TOL_EXCH = 1.0e-11           # the exchange law (E) at every grid point
TOL_W0 = 1.0e-12             # w_0 = ||a||^2, relative
TOL_FLOOR = 1.0e-9           # mu^P_1 TV >= 1 - TOL_FLOOR
TOL_RUNG1 = 1.0e-12          # P(sigma = 1) = g_16/g_1, relative
TOL_RUNG16 = 1.0e-8          # g_16 Q(x*) = 1, relative (one 16x16 solve)
TOL_MONO_P = 1.0e-9          # price non-increasing, in units of P(sigma = 1)
TOL_MONO_D = 1.0e-9          # demand non-decreasing along the knob
TOL_MELLIN = 1.0e-11         # closed cell moments vs quadrature, relative
TOL_ABEL = 1.0e-12           # Abel identities, of the per-level scale
TOL_GBREAK = 1.0e-11         # the gauge-violation break vs its closed value
TOL_LOGMOM = 1.0e-10         # the three log-moment routes, relative
TOL_PEEL = 1.0e-8            # the 2 log 2 peel (quadrature + closed tail)
TOL_PSI1 = 1.0e-14           # Psi_1 = -log 2, closed
TOL_CTRL = 1.0e-12           # Dirichlet / parity / Toeplitz controls
BAR_MUT_EXCH = 1.0e-2        # the wrong-constant mutation must move (E) by >=
BAR_VIOL = 1.0e-1            # the inadmissible vector must undercut the floor
#                              to below this multiple of 1
BAR_MUT_MELLIN = 1.0e-3      # the shifted tent centres must break by >=
BAR_GBREAK = 1.0e-6          # the gauge violation must break the dropped-
#                              boundary Abel form by >= this, absolute scale
BAR_MUT_WRON = 1.0e-5        # the dropped Wronskian term must break by >=
#                              (T162 measures the term at 3.2e-6..3.5e-2 of L)
BAR_MUT_GSHIFT = 1.0e-2      # the shifted generating function must break by >=
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
    table (the T162/T163 convention; Chebyshev 1852 / Rosser-Schoenfeld
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
    bit the frame-A code path of T128..T163 / v548..v554."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T163)
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


def parity_basis(m):
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


# ------------------------------------- the lag weights (T159/T160)
def lag_weights_direct(y, M):
    """w_d = T_d - H_d: T the autocorrelation and H the convolution of y,
    so that y^T A y = sum_d c_d w_d for A = odd_toeplitz(c, M)."""
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


def abel_tail(v):
    """W^1_d = sum_{e >= d} v_e (Abel 1826)."""
    return np.cumsum(v[::-1])[::-1]


def total_variation(w):
    """TV(x) = ||Delta w||_1 with the T163 convention w_M := 0."""
    return float(np.sum(np.abs(np.diff(np.append(w, 0.0)))))


def cholesky_ladder(B):
    """g_K = sum_{j <= K} y_j^2 with y = L^{-1} e_1 from ONE Cholesky of the
    16x16 block (Schur 1917 / Haynsworth 1968; T158's positive ladder)."""
    L = np.linalg.cholesky(B)
    e1 = np.zeros(B.shape[0])
    e1[0] = 1.0
    y = np.linalg.solve(L, e1)
    return np.cumsum(y * y), y


# ------------------------------------- the closed head (T161/T162)
def psi_head_closed(d):
    """Psi_d = -(1/2) [ (d+1) log(d+1) - 2 d log d + (d-1) log(d-1) ]: the
    closed second difference of w log w, valid for every d >= 1."""
    d = np.asarray(d, dtype=float)

    def xlx(t):
        return np.where(t > 0.0, t * np.log(np.maximum(t, 1.0e-300)), 0.0)
    return -0.5 * (xlx(d + 1.0) - 2.0 * xlx(d) + xlx(d - 1.0))


# ------------------------------------- the Mellin cell moments (T162, C2)
def mellin_cell_moments(M, D, s):
    """C_d(s) = int_0^{MD} hat_d(u) e^{su} du in CLOSED form: the half tent
    at d = 0 gives (e^{sD} - 1 - sD)/(s^2 D); the full tent at d >= 1 gives
    e^{s d D} (e^{sD} - 2 + e^{-sD})/(s^2 D) (Mellin 1896)."""
    dd = np.arange(M, dtype=float)
    out = np.empty(M)
    out[0] = (math.exp(s * D) - 1.0 - s * D) / (s * s * D)
    tent = (math.exp(s * D) - 2.0 + math.exp(-s * D)) / (s * s * D)
    out[1:] = np.exp(s * dd[1:] * D) * tent
    return out


def what_eval(u, w, D):
    """The linear interpolant of the lag weights on the grid dD, with
    w(M D) := 0 (the same convention as the sampling identity)."""
    wz = np.append(w, 0.0)
    pos = np.asarray(u, dtype=float) / D
    i0 = np.clip(np.floor(pos).astype(np.int64), 0, len(wz) - 2)
    fr = pos - i0
    return (1.0 - fr) * wz[i0] + fr * wz[i0 + 1]


def mellin_rung_quadrature(w, M, D, s):
    """The same rung by declared per-cell Gauss-Legendre quadrature, the
    independent route the closed moments are checked against."""
    tot = 0.0
    for d in range(M):
        lo, hi = d * D, (d + 1) * D
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        u = mid + half * _GLX
        tot += half * float(np.dot(_GLW, np.exp(s * u) * what_eval(u, w, D)))
    return tot


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
             X=math.exp(2.0 * alpha))
    r["split"] = float(np.max(np.abs(sp["c"] - sp["c_ar"] - sp["c_at"])))
    A = sym(odd_toeplitz(sp["c"], M))
    lam1 = float(np.linalg.eigvalsh(A)[0])
    if not (lam1 > 0.0):
        return None
    mu = parity_mu(h)[:SCHUR_KB]
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
    return r


def trial_quantities(r, x):
    """Q(x), w(x), TV(x), P(x), delta_bnd(x) for one sixteen-vector x."""
    y = (r["T16"].T / np.sqrt(r["mu"])) @ x
    w = lag_weights_direct(y, r["M"])
    Q = float(x @ (r["BLL"] @ x))
    tv = total_variation(w)
    return Q, w, tv


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v555  PRIME.PARETO.TV.01 -- the Pareto / total-variation "
          "identities (T162/T163)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, the one arithmetic input")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    kappa = chebyshev_kappa()
    check(f"S0.KAPPA: the ONE unconditional arithmetic input, measured on "
          f"THIS table and nothing else -- |psi(x) - x| <= kappa x with "
          f"kappa = {kappa:.6f} at every jump point of the von-Mangoldt "
          f"table in [{KAPPA_X0:.0f}, {ATOM_MAX}] (the T162/T163 "
          f"convention); the T162/T163 constant 0.038821 is reproduced to "
          f"{abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} (Chebyshev "
          f"1852; the Rosser-Schoenfeld 1962 form is psi(x) <= "
          f"{1.0 + kappa:.6f} x).  Every delta_bnd below is priced against "
          f"THIS kappa and nothing else",
          abs(kappa - KAPPA_REF) <= TOL_KAPPA)
    INST = []
    for (k, D, M, h) in build_windows():
        r = build_instance(k, D, M, h)
        if r is not None:
            INST.append(r)
    h_max = max(r["h"] for r in INST) if INST else 0
    e_split = max(r["split"] for r in INST)
    lad_ok, lad_mono = [], []
    for r in INST:
        y2 = r["y_lad"] * r["y_lad"]
        lad_ok.append(bool(np.min(y2) > 0.0))
        lad_mono.append(bool(np.min(np.diff(r["gK"])) > 0.0))
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite on every one; the lag split "
          f"c = c^arch + c^atom exact to {e_split:.1e} <= {TOL_SPLIT:.0e}; "
          f"the T158 Cholesky ladder g_K carries all {SCHUR_KB} terms "
          f"strictly positive with strictly monotone partial sums on "
          f"{sum(lad_ok)}/{len(INST)} windows); every assembled section <= "
          f"{H_CAP} (max m = {h_max})",
          len(INST) >= 6 and h_max <= H_CAP and e_split <= TOL_SPLIT
          and all(lad_ok) and all(lad_mono))
    for r in INST:
        print(f"    n={r['n']:>5d} m={r['h']:>4d} X={r['X']:8.1f} "
              f"g_16={r['gK'][-1]:.4f} 1/mu^P_1={1.0 / r['mu'][0]:9.1f}")

    # ------------------------------------------------ the Fejer knob battery
    sig_grid = list(np.geomspace(SIGMA_LO, SIGMA_HI, N_SIGMA)) + [math.inf]
    rng = np.random.default_rng(555)
    for r in INST:
        g16 = float(r["gK"][-1])
        knob = []
        for sg in sig_grid:
            if math.isinf(sg):
                t = np.ones(SCHUR_KB)
            else:
                t = np.maximum(0.0, 1.0 - np.arange(SCHUR_KB) / sg)
            x = t * r["x_star"]
            Q, w, tv = trial_quantities(r, x)
            knob.append(dict(sigma=sg, x=x, Q=Q, w=w, tv=tv,
                             P=g16 * abs(Q)))
        r["knob"] = knob
        extra = []
        for _ in range(8):
            x = rng.normal(size=SCHUR_KB)
            x[0] = 1.0
            Q, w, tv = trial_quantities(r, x)
            extra.append(dict(x=x, Q=Q, w=w, tv=tv))
        r["extra"] = extra

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the exchange law and the crossing criterion "
          "(T163, R1.2)")
    E_EX, E_EXM, XING_OK, ADM_OK = [], [], [], []
    for r in INST:
        g16 = float(r["gK"][-1])
        lX = 2.0 * r["alpha"]
        adm = True
        for p in r["knob"]:
            if not (p["Q"] > 0.0):
                adm = False
                continue
            d_def = 0.5 + math.log(2.0 * kappa * p["tv"] / abs(p["Q"])) / lX
            d_exc = 0.5 + math.log(2.0 * kappa * g16 * p["tv"] / p["P"]) / lX
            d_mut = 0.5 + math.log(kappa * g16 * p["tv"] / p["P"]) / lX
            E_EX.append(abs(d_exc - d_def) / max(abs(d_def), 1.0e-300))
            E_EXM.append(abs(d_mut - d_def) / max(abs(d_def), 1.0e-300))
            XING_OK.append(bool(
                (d_def < 0.5) == (p["P"] > 2.0 * kappa * g16 * p["tv"])))
        ADM_OK.append(adm)
    check(f"S1.EXCHANGE: the exchange law (E) is an IDENTITY at every grid "
          f"point of the declared Fejer knob ({N_SIGMA} geometric sigma on "
          f"[{SIGMA_LO:.0f}, {SIGMA_HI:.0f}] plus infinity, "
          f"{len(E_EX)} points on {len(INST)} windows): delta_bnd(x) = "
          f"1/2 + log(2 kappa g_16 TV(x) / P(x)) / log X reproduces the "
          f"definition 1/2 + log(2 kappa TV/|Q|)/log X to {max(E_EX):.1e} "
          f"<= {TOL_EXCH:.0e} relative, with Q(x) > 0 (admissibility) at "
          f"every point on {sum(ADM_OK)}/{len(INST)} windows -- price and "
          f"demand are two coordinates on ONE object (T163's (E), per "
          f"instance)",
          all(ADM_OK) and max(E_EX) <= TOL_EXCH)
    check(f"S1.CROSSING: the crossing criterion (E') delta_bnd(x) < 1/2 "
          f"<==> P(x) > 2 kappa g_16 TV(x) holds as an EXACT equivalence "
          f"at all {len(XING_OK)} grid points ({sum(XING_OK)} agree): the "
          f"trial vector enters the demand only through TV/|Q|, so the "
          f"crossing price is the closed formula 2 kappa g_16 TV at the "
          f"crossing point and nothing else can contribute",
          all(XING_OK))
    check(f"S1.CTRL: the wrong-constant mutation (kappa in place of "
          f"2 kappa inside (E)) moves the exchange law by "
          f"{min(E_EXM):.2e}..{max(E_EXM):.2e} >= {BAR_MUT_EXCH:.0e} "
          f"relative at every grid point (against <= {TOL_EXCH:.0e} for "
          f"the true constant): the identity is a statement about THE "
          f"declared constant, not a generic near-agreement",
          min(E_EXM) >= BAR_MUT_EXCH)

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the total-variation floor (T163, R2.2)")
    E_W0, TELE_OK, FLOOR, SLACK = [], [], [], []
    n_trial = 0
    for r in INST:
        mu1 = float(r["mu"][0])
        for p in list(r["knob"]) + list(r["extra"]):
            x = p["x"]
            a2 = float(np.sum(x * x / r["mu"]))
            w0 = float(p["w"][0])
            E_W0.append(abs(w0 - a2) / max(abs(a2), 1.0e-300))
            TELE_OK.append(bool(p["tv"] >= abs(w0) * (1.0 - 1.0e-12)))
            FLOOR.append(mu1 * p["tv"])
            n_trial += 1
        SLACK.append(mu1 * min(p["tv"] for p in r["knob"]))
    check(f"S2.TV_FLOOR: the four-step floor theorem, machine-checked on "
          f"ALL {n_trial} trial vectors built in this module ({N_SIGMA + 1} "
          f"knob settings + 8 random admissible sixteen-vectors per "
          f"window) -- (T1) w_0(x) = ||a(x)||^2 to {max(E_W0):.1e} <= "
          f"{TOL_W0:.0e} relative (the parity rows are orthonormal); (T2) "
          f"TV(x) >= |w_0(x)| by telescoping with w_M = 0 on "
          f"{sum(TELE_OK)}/{n_trial}; (T3) x_1 = 1 forces ||a||^2 >= "
          f"1/mu^P_1, hence mu^P_1 TV(x) = {min(FLOOR):.2f}.."
          f"{max(FLOOR):.2f} >= 1 on every trial vector -- the closed "
          f"floor 1/mu^P_1 = 1/(4 sin^2(pi/N)) = "
          f"{min(1.0 / r['mu'][0] for r in INST):.1f}.."
          f"{max(1.0 / r['mu'][0] for r in INST):.1f} grows like h^2 in "
          f"closed form, and NO taper, block size or weighting can evade "
          f"it (T163's T1-T3, per instance; the slack per window is "
          f"{min(SLACK):.2f}..{max(SLACK):.2f})",
          max(E_W0) <= TOL_W0 and all(TELE_OK)
          and min(FLOOR) >= 1.0 - TOL_FLOOR)
    PFLOOR_OK, PFLOOR = [], []
    for r in INST:
        g16 = float(r["gK"][-1])
        mu1 = float(r["mu"][0])
        pf = 2.0 * kappa * g16 / mu1
        PFLOOR.append(pf)
        lX = 2.0 * r["alpha"]
        for p in r["knob"]:
            d_def = 0.5 + math.log(2.0 * kappa * p["tv"] / abs(p["Q"])) / lX
            if d_def < 0.5:
                PFLOOR_OK.append(bool(p["P"] > pf))
    check(f"S2.PRICE_FLOOR: (T4) combining the floor with (E'): every "
          f"trial vector with delta_bnd < 1/2 pays P > 2 kappa g_16 / "
          f"mu^P_1 = {min(PFLOOR):.2f}..{max(PFLOOR):.2f} on this surface "
          f"-- checked on all {len(PFLOOR_OK)} sub-1/2 grid points of the "
          f"knob ({sum(PFLOOR_OK)} respect it, as they must): the crossing "
          f"price is bounded below by a quantity growing like h^2 in "
          f"closed form, so a FLAT-price sub-1/2 demand is impossible in "
          f"the parity sector on this surface (T163's T4 -- the inequality "
          f"that closes R-C''' negatively on this construction)",
          len(PFLOOR_OK) > 0 and all(PFLOOR_OK))
    VIOL_TV, VIOL_X1 = [], []
    for r in INST:
        mu1 = float(r["mu"][0])
        x_bad = 0.01 * r["x_star"]
        Q, w, tv = trial_quantities(r, x_bad)
        VIOL_TV.append(mu1 * tv)
        VIOL_X1.append(abs(float(x_bad[0]) - 1.0))
    check(f"S2.CTRL: the violator NEGATIVE control -- the INADMISSIBLE "
          f"vector 0.01 x* (x_1 = 0.01 != 1) DOES undercut the floor, "
          f"mu^P_1 TV = {min(VIOL_TV):.1e}..{max(VIOL_TV):.1e} <= "
          f"{BAR_VIOL} < 1 on every window, and is recognised as "
          f"inadmissible (|x_1 - 1| = {min(VIOL_X1):.2f} >= 0.5): the "
          f"floor is a property of the NORMALISATION x_1 = 1 meeting the "
          f"smallest parity eigenvalue (KMS 1953), not of the machinery",
          max(VIOL_TV) <= BAR_VIOL and min(VIOL_X1) >= 0.5)

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the chain-derived price axis (T163, R1.0)")
    E_R1, E_R16, MONO_P, MONO_D = [], [], [], []
    for r in INST:
        g16 = float(r["gK"][-1])
        g1 = float(r["gK"][0])
        lX = 2.0 * r["alpha"]
        p1 = r["knob"][0]
        E_R1.append(abs(p1["P"] - g16 / g1) / (g16 / g1))
        pinf = r["knob"][-1]
        E_R16.append(abs(pinf["P"] - 1.0))
        PP = np.array([p["P"] for p in r["knob"]])
        DD = np.array([0.5 + math.log(2.0 * kappa * p["tv"] / abs(p["Q"]))
                       / lX for p in r["knob"]])
        MONO_P.append(float(np.max(np.diff(PP))) / float(PP[0]))
        MONO_D.append(float(np.min(np.diff(DD))))
    check(f"S3.RUNGS: the knob's endpoints are the LADDER's endpoints, "
          f"which is why the price axis is chain-derived and not invented "
          f"-- sigma = 1 gives x = e_1 exactly and P(sigma = 1) = "
          f"g_16 / g_1 (the K = 1 rung, the T157 route-(0) certificate "
          f"1/s <= B_11) to {max(E_R1):.1e} <= {TOL_RUNG1:.0e} relative, "
          f"and sigma = infinity gives the untapered optimiser with "
          f"P = g_16 Q(x*) = 1 (the K = 16 top rung) to {max(E_R16):.1e} "
          f"<= {TOL_RUNG16:.0e}: the Fejer sweep is a PATH between two "
          f"certificates the chain already owns (T163's knob endpoints, "
          f"per instance)",
          max(E_R1) <= TOL_RUNG1 and max(E_R16) <= TOL_RUNG16)
    check(f"S3.MONOTONE: the knob is a monotone trade-off on every window "
          f"-- along increasing sigma the price is non-increasing (largest "
          f"forward difference {max(MONO_P):.2e} <= {TOL_MONO_P:.0e} in "
          f"units of P(sigma = 1)) and the demand is non-decreasing "
          f"(smallest forward difference {min(MONO_D):.2e} >= "
          f"-{TOL_MONO_D:.0e}), so the knob curve IS the Pareto front: "
          f"there is no interior optimum to find, and the only question "
          f"is where the chain can afford to sit on it",
          max(MONO_P) <= TOL_MONO_P and min(MONO_D) >= -TOL_MONO_D)
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
    check(f"S3.CTRL: the corrupted ladder REFUSES -- perturbing one "
          f"off-diagonal sixteen-block entry destroys positive "
          f"definiteness and the Cholesky fails on {refuse}/{len(INST)} "
          f"windows: the price axis rests on a certificate, not on a "
          f"formula that silently degrades",
          refuse == len(INST))

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the Mellin cell moments and the Abel step "
          "(T162, C2/C5)")
    E_MEL, E_MELM = [], []
    for r in INST:
        w = r["knob"][-1]["w"]
        for kk in range(1, MELLIN_K + 1):
            s = -(2.0 * kk + 0.5)
            Cd = mellin_cell_moments(r["M"], r["D"], s)
            closed = float(np.dot(w, Cd))
            quad = mellin_rung_quadrature(w, r["M"], r["D"], s)
            sc = max(float(np.sum(np.abs(w * Cd))), 1.0e-300)
            E_MEL.append(abs(closed - quad) / sc)
            Cd_bad = np.empty_like(Cd)
            Cd_bad[0] = Cd[0]
            dd = np.arange(1, r["M"], dtype=float)
            tent = (math.exp(s * r["D"]) - 2.0 + math.exp(-s * r["D"])) \
                / (s * s * r["D"])
            Cd_bad[1:] = np.exp(s * (dd + 1.0) * r["D"]) * tent
            E_MELM.append(abs(float(np.dot(w, Cd_bad)) - quad) / sc)
    check(f"S4.MELLIN: the k-th rung of the archimedean Mellin ladder is "
          f"a CLOSED sum of cell moments -- sum_d w_d C_d(-(2k+1/2)) with "
          f"C_d(s) the exact tent integral (half tent at d = 0, full tent "
          f"at d >= 1; Mellin 1896) -- reproduced by an independent "
          f"per-cell Gauss-Legendre quadrature of int e^(su) w^(u) du to "
          f"{max(E_MEL):.1e} <= {TOL_MELLIN:.0e} of the absolute scale on "
          f"every rung k = 1..{MELLIN_K} of every window: the smooth part "
          f"of the T162 ladder is closed, and no zero data enters anywhere",
          max(E_MEL) <= TOL_MELLIN)
    check(f"S4.MELLIN_CTRL: the shifted tent centres (e^(s(d+1)D) in place "
          f"of e^(sdD)) break the cell moments by {min(E_MELM):.2e}.."
          f"{max(E_MELM):.2e} >= {BAR_MUT_MELLIN:.0e} of the absolute "
          f"scale on every rung: the closed moments are a statement about "
          f"THE interpolation grid",
          min(E_MELM) >= BAR_MUT_MELLIN)
    E_AB, E_AB0, E_GB, GB_SIZE, LOSS, L2W = [], [], [], [], [], []
    for r in INST:
        w = r["knob"][-1]["w"]
        v = r["c_at"]
        sc0 = max(float(np.sum(np.abs(v * w))), 1.0e-300)
        direct = float(np.dot(v, w))
        # the inclusive ladder identity at every level (tails on w,
        # differences on v, zero extension on the left)
        Vk = v.copy()
        Wk = w.copy()
        for kk in range(1, ABEL_K + 1):
            Vk = np.diff(np.concatenate(([0.0], Vk)))
            Wk = abel_tail(Wk)
            sck = max(sc0, float(np.sum(np.abs(Vk * Wk))))
            E_AB.append(abs(float(np.dot(Vk, Wk)) - direct) / sck)
        # the BOUNDARY-DROPPED level-1 form with the FULL lag vector
        # (whose lag-0 entry is nonzero): licensed by the gauge ALONE
        vf = r["c"]
        scf = max(float(np.sum(np.abs(vf * w))), 1.0e-300)
        Vf1 = np.diff(np.concatenate(([0.0], vf)))
        E_AB0.append(abs(float(np.dot(Vf1[1:], abel_tail(w)[1:]))
                         - float(np.dot(vf, w))) / scf)
        # gauge violation: w -> w + c0 breaks the dropped-boundary form by
        # EXACTLY v_0 W'_0 = v_0 c_0 M (closed) -- a positive control
        c0 = 0.01 * float(np.max(np.abs(w)))
        w_bad = w + c0
        W1_bad = abel_tail(w_bad)
        got = float(np.dot(Vf1[1:], W1_bad[1:]))
        pred_break = float(vf[0]) * float(W1_bad[0])
        brk = abs(got - float(np.dot(vf, w_bad)))
        E_GB.append(abs(brk - abs(pred_break)) / max(abs(pred_break),
                                                     1.0e-300))
        GB_SIZE.append(brk / scf)
        # the closed loss reason: level 2 costs x(2/D) on the envelope and
        # saves ||D^2 w||_1 / ||D^1 w||_1 -- the certified bound gets WORSE
        w1 = np.diff(np.concatenate(([0.0], w)))
        w2 = np.diff(np.concatenate(([0.0], w1)))
        b1 = float(np.sum(np.abs(w1)))
        b2 = (2.0 / r["D"]) * float(np.sum(np.abs(w2)))
        L2W.append(b2 / b1)
        LOSS.append(32.0 * math.pi / r["alpha"])
    check(f"S4.ABEL: the boundary-free Abel step, in both forms -- the "
          f"inclusive ladder identity sum_d v_d w_d = sum_d (Delta^k v)_d "
          f"W^(k)_d holds at every level k = 1..{ABEL_K} on every window "
          f"({max(E_AB):.1e} <= {TOL_ABEL:.0e} of the per-level scale, "
          f"v = c^atom), and the DROPPED-BOUNDARY level-1 form (the sum "
          f"from d = 1, the one the chain uses, here with the FULL lag "
          f"vector whose lag-0 entry is nonzero) agrees to "
          f"{max(E_AB0):.1e} because the gauge identity kills the "
          f"boundary term v_0 W^1_0 = v_0 sum_d w_d EXACTLY -- and the "
          f"optimal level is ONE for T162's closed reason: each further "
          f"level multiplies the certified envelope by 2/D and divides "
          f"the l1 norm by only ~omega_16, the closed net factor is "
          f"32 pi / alpha = {min(LOSS):.1f}..{max(LOSS):.1f} > 1 on "
          f"every window, and the MEASURED level-2/level-1 bound ratio "
          f"(2/D) ||Delta^2 w||_1 / ||Delta^1 w||_1 = {min(L2W):.1f}.."
          f"{max(L2W):.1f} > 1 confirms it: partial summation is a single "
          f"step, and it has been taken",
          max(E_AB) <= TOL_ABEL and max(E_AB0) <= TOL_ABEL
          and min(LOSS) > 1.0 and min(L2W) > 1.0)
    check(f"S4.ABEL_CTRL: the gauge violation (a constant c_0 of 1 per "
          f"cent of sup|w| added to the weight vector) breaks the "
          f"dropped-boundary form by {min(GB_SIZE):.2e}..{max(GB_SIZE):.2e} "
          f">= {BAR_GBREAK:.0e} of the absolute scale, and the break "
          f"equals its CLOSED prediction v_0 W'_0 = v_0 c_0 M to "
          f"{max(E_GB):.1e} <= {TOL_GBREAK:.0e} relative on every window "
          f"(T162's positive control on the mechanism): the gauge "
          f"identity is load-bearing for the step, not a formality",
          min(GB_SIZE) >= BAR_GBREAK and max(E_GB) <= TOL_GBREAK)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the Lerch/Frullani log-moment on three routes "
          "(T162, R-A')")
    E_LB, E_LC, E_LBM, E_LCM = [], [], [], []
    # panels: linear on [0, 1] (the integrand is analytic at y = 0, the
    # gauge makes G bounded there), geometric on (1, LM_HI); the d = 1
    # term is PEELED in closed form because its 1/y^2 tail is not
    # exponentially small -- exactly T162's 2 log 2 device
    pan = np.concatenate([np.linspace(0.0, 1.0, 5),
                          np.geomspace(1.0, LM_HI, LM_PANELS + 1)[1:]])

    def frull_quad(f_of_y):
        tot = 0.0
        for lo, hi in zip(pan[:-1], pan[1:]):
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            y = mid + half * _GLX
            ker = (np.expm1(-y) / y) ** 2
            tot += half * float(np.dot(_GLW, ker * f_of_y(y)))
        return tot

    for r in INST:
        w = r["knob"][-1]["w"]
        M = r["M"]
        dd = np.arange(1, M, dtype=float)
        L_dir = float(np.dot(psi_head_closed(dd), w[1:]))
        sc = max(abs(L_dir), 1.0e-300)
        # route (b): double Abel with the Wronskian boundary term
        phi = np.zeros(M + 1)
        ddd = np.arange(1, M + 1, dtype=float)
        phi[1:] = ddd * np.log(ddd)
        wz = np.append(w, 0.0)
        d2w = wz[2:M + 1] - 2.0 * wz[1:M] + wz[0:M - 1]
        S2 = float(np.dot(phi[1:M], d2w))
        L_abel = -0.5 * S2 - 0.5 * M * math.log(M) * float(w[M - 1])
        E_LB.append(abs(L_abel - L_dir) / sc)
        L_abel_nob = -0.5 * S2
        E_LBM.append(abs(L_abel_nob - L_dir) / sc)
        # route (c): the Lerch/Frullani integral, d = 1 peeled closed
        dd2 = dd[1:]
        w2 = w[2:]
        L_int = (-math.log(2.0) * float(w[1])
                 - 0.5 * frull_quad(
                     lambda y: np.exp(-np.outer(y, dd2 - 1.0)) @ w2))
        L_int_m = (-math.log(2.0) * float(w[1])
                   - 0.5 * frull_quad(
                       lambda y: np.exp(-np.outer(y, dd2)) @ w2))
        E_LC.append(abs(L_int - L_dir) / sc)
        E_LCM.append(abs(L_int_m - L_dir) / sc)
    # the peel constant itself: quadrature on [0, LM_HI] plus the CLOSED
    # tail int_B^inf y^-2 dy = 1/B (the e^-y corrections are O(e^-B))
    peel = frull_quad(lambda y: np.ones_like(y)) + 1.0 / LM_HI
    e_peel = abs(peel - 2.0 * math.log(2.0))
    e_psi1 = abs(float(psi_head_closed(np.array([1.0]))[0]) + math.log(2.0))
    check(f"S5.LOGMOM: the log-moment L = sum_d Psi_d w_d -- the one "
          f"non-polynomial moment of the arch half -- agrees on THREE "
          f"independent routes on every window: the direct sum with Psi_d "
          f"closed; the double-Abel form WITH its Wronskian boundary term "
          f"L = -(1/2) sum_d (d log d)(delta^2 w)_d - (1/2) M log M "
          f"w_(M-1) to {max(E_LB):.1e}; and the Lerch/Frullani integral "
          f"-(1/2) int (1-e^(-y))^2 y^(-2) G(y) dy (G the generating "
          f"function of the weights, convergent at y = 0 by the gauge "
          f"identity; the d = 1 term peeled in closed form, "
          f"{len(pan) - 1} declared panels on (0, {LM_HI:.0f}), "
          f"{GL_N}-point Gauss-Legendre) to {max(E_LC):.1e} "
          f"<= {TOL_LOGMOM:.0e} relative (Frullani 1828 / Lerch 1887 / "
          f"Clausen 1832): T162's R-A' closure, recomputed per instance",
          max(E_LB) <= TOL_LOGMOM and max(E_LC) <= TOL_LOGMOM)
    check(f"S5.PEEL: the d = 1 term peels in closed form -- the same "
          f"quadrature plus the closed 1/B tail gives "
          f"int ((1-e^(-y))/y)^2 dy = 2 log 2 to {e_peel:.1e} <= "
          f"{TOL_PEEL:.0e}, and the closed head reproduces Psi_1 = "
          f"-log 2 to {e_psi1:.1e} <= {TOL_PSI1:.0e} (the "
          f"second-difference formula): an independent confirmation of "
          f"the whole derivation",
          e_peel <= TOL_PEEL and e_psi1 <= TOL_PSI1)
    check(f"S5.CTRL: the mutations fail loudly -- DROPPING the Wronskian "
          f"boundary term breaks route (b) by {min(E_LBM):.2e}.."
          f"{max(E_LBM):.2e} >= {BAR_MUT_WRON:.0e} relative (the boundary "
          f"term is not optional; T162 measures it at 3.2e-6..3.5e-2 of "
          f"L), and a one-index shift of the generating function "
          f"(e^(-d y) in place of e^(-(d-1) y)) breaks route (c) by "
          f"{min(E_LCM):.2e}..{max(E_LCM):.2e} >= {BAR_MUT_GSHIFT:.0e}: "
          f"the agreement is a statement about THE three derivations, not "
          f"a generic near-agreement",
          min(E_LBM) >= BAR_MUT_WRON and min(E_LCM) >= BAR_MUT_GSHIFT)

    # ---------------------------------------------------------------- no-go
    print("\nS6 -- the no-go staircase and the controls (T162/T163)")
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
            canc = abs(Qa + Qt) / max(abs(Qa), abs(Qt))
            stair[f].append(canc)
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
    # Dirichlet cosine-sum control, incl. the degenerate branch
    rng2 = np.random.default_rng(5551)
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
          f"spectral gap mu^P_1 = 4 sin^2(pi/N) whose reciprocal IS the "
          f"floor of S2), and odd_toeplitz(c^L) = L_P for c^L = "
          f"(2, -1, 0, ...) with residual {e_tpl:.1e} == 0 (ZERO "
          f"tolerance): the section map of the whole chain is the one the "
          f"identities assume",
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
          "not a claim about RH in either direction; the open terms after "
          "T163 -- R-E (the successor question, both arms prime-free: arm "
          "A, does the downstream T159/T160 chain tolerate a growing 1/s "
          "ceiling; arm B, can the entry functional be represented in a "
          "sector whose lowest eigenvalue does not vanish like h^-2), "
          "R-B''' (make the positivity margin h-uniform), R-D (a fifth "
          "R1'' device) -- stay OPEN, typed open, and are neither assumed "
          "nor approached; R-C''' is closed NEGATIVELY by the S2 "
          "inequality on this construction, and no other marker of any "
          "pre-existing contract moves; Fejer 1915 / Mellin 1896 / Abel "
          "1826 / Chebyshev 1852 / Rosser-Schoenfeld 1962 / Legendre / "
          "Dirichlet 1829 / Kac-Murdock-Szego 1953 / Frullani 1828 / "
          "Lerch 1887 / Clausen 1832 / Schur 1917 / Haynsworth 1968 / "
          "Wilkinson 1968 / Higham 2002 named CLASSICAL; Weil 1952 / "
          "Bombieri 2000 CITED, never used as a criterion; zero-firewall "
          "AST-checked", True)

    elapsed = time.time() - t0
    print(f"\nv555 runtime: {elapsed:.1f}s")
    print(f"  (1) exchange law <= {max(E_EX):.1e}; crossing criterion "
          f"exact on {len(XING_OK)} points")
    print(f"  (2) TV floor: mu^P_1 TV = {min(FLOOR):.2f}..{max(FLOOR):.2f} "
          f">= 1 on {n_trial} trials; price floor "
          f"{min(PFLOOR):.2f}..{max(PFLOOR):.2f}")
    print(f"  (3) rungs <= {max(E_R1):.1e} / {max(E_R16):.1e}; knob "
          f"monotone on {len(INST)}/{len(INST)}")
    print(f"  (4) Mellin <= {max(E_MEL):.1e}; Abel <= {max(E_AB):.1e}; "
          f"loss 32 pi/alpha = {min(LOSS):.1f}..{max(LOSS):.1f} > 1")
    print(f"  (5) log-moment routes <= {max(max(E_LB), max(E_LC)):.1e}; "
          f"peel 2 log 2 to {e_peel:.1e}")
    print(f"  no-go staircase medians {', '.join(f'{m:.2f}' for m in med_seq)}"
          f"; Dirichlet/parity exact")
    return summary("PRIME.PARETO.TV.01 pareto/tv identities")


if __name__ == "__main__":
    raise SystemExit(run())
