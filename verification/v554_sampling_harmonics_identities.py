"""v554 -- PRIME.SAMPLING.HARM.01: the sampling / harmonics identities of
T160/T161.  The CLOSED, theorem-shaped cores of T160 (contract PAIRING) and
T161 (contract CLASSICAL.CLOSURE) -- every statement RECOMPUTED here from
scratch on small exactly checkable frame-A windows (no citation of sandbox
output).  Companion to PRIME.EXACT.FORM.IDENT.01 (v553), which certified the
algebra of the sixteen-form: THIS module certifies what that form PAIRS
AGAINST -- the atom half as a Lambda-weighted sampling at the Fourier
harmonics of the log-window, the closed moment laws and the total-variation
theorem of the smooth half, the closed head split of the archimedean kernel
with its scale-free Bernstein rate, and the certified off-diagonal fraction
bound that replaces the refuted sign law.  NOTHING here closes an open term:

[E] (1) THE SAMPLING IDENTITY (T160, P2).  The atom half of the pairing is a
    WEIGHTED SAMPLING of the lag-weight vector at the prime-power positions:
      sum_d c^atom_d w_d = -(1/2) sum_{n <= X} (2 Lambda(n)/sqrt n) w^(log n)
      (+ one reflected term for u < D),
    with w^ the linear interpolant of w -- an identity PER INSTANCE, checked
    against the direct assembly on every window.  Combined with the closed
    Dirichlet-kernel form of w (v553's address), w^(u) is a fixed
    trigonometric polynomial, so the atom half is identically a finite
    combination of sums sum_n Lambda(n) n^{-1/2} cos(t log n) at 2*16
    explicit frequencies.  Mutation: a one-index shift of the sampling grid
    breaks the identity loudly.
[E] (2) THE MOMENT LAWS AND THE TOTAL-VARIATION THEOREM (T160, P1/P4).
    With S0 = sum_r y_r, S1 = sum_r r y_r, P_j = sum_{r<j} y_r:
      m_0 = sum_d w_d      = 0                                  (the gauge law)
      m_1 = sum_d d w_d    = -[ S0^2 + 2 sum_j P_j^2 ]          <= 0
      m_2 = sum_d d^2 w_d  = -[ 2 S1 - (M-1) S0 ]^2             <= 0
    (three-line proofs from the max(r, s) identity; both sign-definite forms
    checked against the direct sums, strictly negative on every window).
    And U3 AS A THEOREM with checked hypotheses: c^arch_d <= 0 and monotone
    non-decreasing on d >= 1 (both CHECKED per window, never assumed), hence
    TV(c^arch) = total rise <= |c^arch_0| + 2 sup_{d>=1} |c^arch_d| < 6 --
    the measured total variation against the closed window-independent
    constant.  Mutations: a one-index prefix shift breaks m_1; an (M-2)
    mis-normalisation breaks m_2; the FULL atom-including kernel violates
    the monotone hypothesis on every window.
[E] (3) THE HARMONIC-FREQUENCY THEOREM AND THE PNT MAIN TERM (T161, P3).
    The 2*16 frequencies t_j = pi j / alpha satisfy t_j * (2 alpha) = 2 pi j
    EXACTLY: they are the FOURIER HARMONICS of the log-window [0, 2 alpha],
    so the atom half is the vector of the first 32 Fourier coefficients of
    the measure sum_n (2 Lambda(n)/sqrt n) delta_{log n} -- checked on every
    frame-A window AND on a deeper DECLARED Lambda-battery (six log-spaced
    cut-offs X = 1e3 .. 3.2e5; finite sums only, no matrix anywhere, so the
    H_CAP does not apply).  At those frequencies partial summation against
    the prime-number theorem gives the CLOSED, parameter-free prediction
    S(t) ~ (sqrt X - 1)/(1/4 + t^2) (theta = t log X = 2 pi j collapses the
    Mellin factor), and the finite sums S(t) -- assembled from the
    von-Mangoldt table and NOTHING else -- agree with it inside a DECLARED
    cap on the battery, with the aggregate residual strictly reduced by the
    subtraction on every cut-off.  Mutation: a wrong Mellin pole
    (1 + 4 t^2 in place of 1/4 + t^2) makes the aggregate residual strictly
    worse on every cut-off.
[E] (4) THE HEAD SPLIT AND THE SCALE-FREE BERNSTEIN RATE (T161, P1).
    For every lag d >= 1 the archimedean lag vector splits EXACTLY as
      c^arch_d = Psi_d + D Ghat(d D, D),
      Psi_d = -(1/2) [ (d+1) log(d+1) - 2 d log d + (d-1) log(d-1) ],
    with Psi CLOSED, D-FREE and m-FREE (the triangle-smeared simple pole of
    g(w) = e^{-w/2}/(1 - e^{-2w}); the log D cancels identically) and Ghat
    the smear of the regularised g_reg = g - 1/(2w), analytic on the whole
    interval.  The two representations of Psi (closed second difference vs
    smeared pole) agree on the first 64 lags; the split holds at machine
    precision at EVERY lag of every window.  And the Bernstein parameter of
    the peeled interval [0.4 alpha, 2 alpha] has the CLOSED SCALE-FREE limit
    rho* = (3 + sqrt 5)/2 = 2.618034 (the root of x^2 - 3x + 1 above 1,
    dependent only on the interval ratio 5, not on alpha, D, h or the
    zone), approached from below by every window's rho(D).  Mutations:
    dropping the Psi term misses c^arch grossly; a wrong interval ratio
    moves the limit away from (3 + sqrt 5)/2.
[E] (5) THE OFF-DIAGONAL FRACTION BOUND AND THE SIGN REFUTATION (T161, P2).
    The gauge identity licenses one boundary-free Abel step, and the closed
    weights give the EXACT decomposition Q^arch = sum_{k,l} a_k a_l
    sum_{d>=1} (Delta c^arch)_d R^1_kl(d).  The certified per-window
    inequality is the FRACTION bound |off-diagonal block| <= (1/4) |Q^arch|
    -- and the REFUTED sign law is wired as the negative control: the arch
    half is NEGATIVE while its off-diagonal block is POSITIVE on every
    window (the harmful direction for the Thomson dual), and per-pair
    violations of sum_{d>=2} (Delta c^arch)_d R_kl(d) <= 0 exist on every
    window, so a one-sign statement was never the right object and the
    fraction bound is what survives.  Mutation: a one-index shift of the
    R-kernel breaks the exact decomposition loudly.

Plus the NO-GO / MEASURE DISCRIMINATORS: the head split is a statement about
THE T115 kernel -- on the T145 no-go reconstruction c(l) = 1/(1+l) the same
closed formula misses grossly; the PNT prediction is a statement about THE
von-Mangoldt measure -- a mass-matched uniform fake measure on the same
window misses the closed prediction grossly.  Parity / Dirichlet controls:
the closed Dirichlet cosine-sum identity against the brute-force sum
(including the degenerate branch), L_P t_k = mu^P_k t_k with an orthonormal
basis, and odd_toeplitz(c^L) = L_P with ZERO tolerance.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   These are PER-INSTANCE statements on SMALL frame-A windows -- the
        N_INST DEEPEST prime-power zones admitting a window inside the cap
        (m <= 300), mirroring v551..v553's declared surface.  Nothing is
        uniform in the zone index or in D, and NO statement for ALL D is
        made.  The PNT-agreement cap and the fraction constant 1/4 are
        DECLARED caps on THIS surface (the sandbox measures tighter values
        on deeper windows -- fits, not consumed here).
  (ii)  THE OPEN TERMS AFTER T161 STAY OPEN AND TYPED OPEN: R-A' -- one
        closed prime-free moment, the log-moment sum_d Psi_d w_d =
        -(1/2) sum_d (d log d)(Delta^2 w)_d, outside the polynomial moment
        ladder; R-B' -- the m-free version of the fraction bound (a 16 x 16
        Gram positivity/norm statement, Fejer 1915 / Schur 1917); R-C' --
        ONE split of the pairing with delta_eff < 1/2 (T161 refutes the
        arch/atom and the arch+smooth/fluctuation splits WITH numbers; the
        delta triage itself is a DOCUMENTATION item, a comparison of
        strengths, and is NOT a claim of this module); R-D -- a fifth
        device for R1''.  None is assumed or approached.
  (iii) T161's refutations (R-B in all four readings; the Abel-against-R
        route) are wired here ONLY as the negative control of item (5); the
        refutation is the reason the fraction bound is the surviving
        object, and nothing single-signed is promoted.
  (iv)  Item (3) allows FINITE Lambda-sums and nothing else: the closed
        prediction is classical partial summation against psi(x) ~ x
        (de la Vallee Poussin 1896), its agreement is a MEASURED fact
        inside a declared cap, and no statement about the residual's decay
        rate is promoted (the X^{-0.39} improvement is a sandbox FIT).

HONEST FENCES (load-bearing typing):
  * THE RH FENCE.  Everything here is a per-instance identity or a
    certified per-window inequality; finite sums over the von-Mangoldt
    table are allowed and used; NOTHING here claims, assumes, approaches or
    weakens RH, no zero of any L-function is read, generated or
    approximated (AST firewall), no L-function is evaluated, and no
    equivalence is claimed.  The delta triage of T161 (required cancellation
    depth vs RH strength) is NOT a claim of this module: it lives in the
    diary and the paper as a comparison of strengths, and R-C' is typed
    OPEN here.  Even with every check green, what stands is a finite list
    of certified window statements on prime-power zones in one frame.
  * Classics named CLASSICAL: Dirichlet 1829 (the cosine-sum identity, the
    closed weights), Abel 1826 (the boundary-free summation by parts),
    Fejer 1915 / Schur 1917 (the Gram address of R-B'), Bernstein 1912
    (the ellipse rate), Chebyshev 1852 / Mertens 1874 (the trivial mass
    bound), de la Vallee Poussin 1896 (the PNT main term), Clausen / Lerch
    (the log-moment address, typed open), Kac-Murdock-Szego 1953 (exact
    parity eigenpairs), Wilkinson 1968 / Higham 2002 (floating-point
    floors); Weil 1952 / Bombieri 2000 CITED, never used as a criterion.
  * ZERO-FIREWALL: AST-checked; no zetazero / nzeros loader; the prime side
    is a finite zero-free sum over prime powers.

Status: [E] per-instance identities and certified inequalities with the
direction in the name, each with a mutation control that fails loudly;
measured quantities typed MEASURED.  Python; Wolfram-mirrored not required
(dense linear-algebra / quadrature machinery stays Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/pairing_probe.py                     (T160)
  experiments/tfpt-discovery/classical_closure_probe.py           (T161)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
ATOM_MAX = 320000            # atom table cap, as in v546..v553
H_CAP = 300                  # HARD cap on any assembled section
H_MIN = 24
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824

K_SCAN = 110                 # prime-power zones scanned
N_INST = 12                  # frame-A windows kept: the N_INST DEEPEST zones
#                              (v551..v553's declared surface convention)

# --- the form geometry, preregistered ----------------------------------------
SCHUR_KB = 16                # the fixed low block of the T152..T161 chain
NF_HARM = 2 * SCHUR_KB       # the 32 harmonic frequencies t_j = pi j / alpha

# --- the peeled Bernstein interval, preregistered (T161 P1) ------------------
SA_LO, SA_HI = 0.4, 2.0      # [0.4 alpha, 2 alpha]: interval ratio 5
RHO_STAR = 0.5 * (3.0 + math.sqrt(5.0))   # the scale-free closed limit

# --- the deep Lambda-battery for item (3), preregistered ---------------------
#     finite von-Mangoldt sums ONLY (no matrix anywhere, so H_CAP does not
#     apply); six log-spaced cut-offs inside the atom table
X_BATTERY = (1.0e3, 3.2e3, 1.0e4, 3.2e4, 1.0e5, 3.2e5)

# --- preregistered tolerances / bars (declared BEFORE any number) -----------
TOL_SAMP = 1.0e-12           # sampling identity vs the ABSOLUTE atom scale
TOL_MOM = 1.0e-11            # closed moment laws vs the direct sums
TOL_GAUGE = 1.0e-12          # m_0 = 0 against ||w||_1
TV_CONST = 6.0               # the closed window-independent TV constant (T160)
TOL_HARM = 1.0e-10           # t_j (2 alpha) = 2 pi j, absolute
PNT_CAP = 0.12               # DECLARED cap on |S - model| / mass on the
#                              Lambda-battery X = 1e3 .. 3.2e5 (the sandbox
#                              measures 0.014..0.232 down to X = 121 with
#                              the residual falling as X^-0.39 -- a FIT,
#                              not consumed here)
PNT_RED = 0.5                # the subtraction must reduce the aggregate
#                              residual to below this fraction of sum|S|
TOL_PSI2 = 1.0e-11           # closed vs smeared Psi on the first 64 lags
TOL_SPLIT_HEAD = 1.0e-10     # head split vs c^arch, of sup|c^arch|
RHO_FLOOR = 2.30             # every window's rho(D) must exceed this
TOL_RHO_ID = 1.0e-12         # rho*^2 - 3 rho* + 1 = 0 and the D -> 0 limit
TOL_DEC = 1.0e-9             # the R^1 decomposition vs Q^arch, relative
FRAC_CAP = 0.25              # the certified off-diagonal fraction constant
TOL_CTRL = 1.0e-12           # Dirichlet / parity / Toeplitz controls
BAR_MUT_SAMP = 1.0e-5        # the shifted sampling grid must break by >= this
#                              (7+ orders above the identity tolerance)
BAR_MUT_MOM = 1.0e-2         # the moment mutations must break by >= this
BAR_MUT_PNT = 1.5            # the wrong Mellin pole must worsen the
#                              aggregate residual by >= this factor
BAR_MUT_HEAD = 0.2           # dropping Psi must miss c^arch by >= this
BAR_MUT_RHO = 0.1            # the wrong interval ratio must move rho* by >=
BAR_MUT_DEC = 1.0e-5         # the shifted R-kernel must break by >= this
#                              (4+ orders above the decomposition tolerance)
BAR_NOGO_HEAD = 0.2          # the head split must miss the no-go c by >= this
BAR_FAKE_PNT = 1.5           # the fake measure must miss the PNT model by
#                              >= this multiple of the declared cap
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
    bit the frame-A code path of T128..T161 / v548..v553."""
    c_at, D = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D)


# ------------------------------------- the parity sector (T106..T161)
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


def fwd_diff(c):
    out = np.zeros_like(c)
    out[1:] = c[1:] - c[:-1]
    return out


def _cos_sum(alpha, beta, L):
    """THE DIRICHLET-KERNEL IDENTITY (Dirichlet 1829), incl. the degenerate
    branch alpha = 0 mod 2 pi; this is what makes w_d and R_kl(d) CLOSED."""
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
    return M, 2 * m + 1, d, LT, J, n0, LH


def R_pair(k, l, m, om, shift=0):
    """R_kl(d): the (k, l) contribution to the closed weight vector -- a sum
    of FOUR Dirichlet kernels at the frequencies om_k -+ om_l.  Closed and
    prime-free.  `shift` != 0 is the MUTATION (a one-index Hankel shift)."""
    M, N, d, LT, J, n0, LH = _kl_geometry(m)
    J = J + float(shift)
    am, ap = om[k] - om[l], om[k] + om[l]
    T = (4.0 / N) * (_cos_sum(am, -om[l] * d, LT) - _cos_sum(ap, om[l] * d, LT))
    sh = am * (n0 - 1.0)
    sp = ap * (n0 - 1.0)
    H = (2.0 / N) * (_cos_sum(ap, -om[l] * (J + 2.0) + sp, LH)
                     - _cos_sum(am, om[l] * (J + 2.0) + sh, LH))
    out = T - H
    out[0] = T[0] * 0.5 - H[0]
    return out


# ------------------------------------- the closed moments (T160, P1)
def moments_closed_012(y, M):
    """m_0 = 0, m_1 = -[S0^2 + 2 sum_j P_j^2], m_2 = -[2 S1 - (M-1) S0]^2:
    the three closed moment laws (T160), sign-definite for p = 1, 2."""
    h = M // 2
    S0 = float(np.sum(y))
    S1 = float(np.dot(np.arange(h, dtype=float), y))
    P = np.concatenate(([0.0], np.cumsum(y)))[:h]
    m1 = -(S0 * S0 + 2.0 * float(np.dot(P[1:h], P[1:h])))
    m2 = -(2.0 * S1 - (M - 1.0) * S0) ** 2
    return 0.0, m1, m2, S0, S1, P


# ------------------------------------- the head split (T161, P1.4)
def g_head(w):
    """g(w) = e^{-w/2} / (1 - e^{-2w}): the T115 integrand head; poles at
    w = i k pi, the k = 0 pole is the 1/s head (g ~ 1/(2w))."""
    return np.exp(-0.5 * w) / (1.0 - np.exp(-2.0 * w))


def cexpm1(z):
    z = np.asarray(z, dtype=np.complex128)
    sm = np.abs(z) < 1.0e-2
    out = np.exp(z) - 1.0
    if sm.any():
        zz = z[sm]
        out[sm] = zz * (1.0 + zz * (0.5 + zz * (1.0 / 6.0 + zz / 24.0)))
    return out


def _g_reg_direct(w):
    """g_reg = B(w)/(2w), B(w) = e^{-w/2} 2w/(1 - e^{-2w}) - 1 = O(w):
    accurate away from w = 0."""
    w = np.asarray(w, dtype=np.complex128)
    tiny = np.abs(w) < 1.0e-300
    ws = np.where(tiny, 1.0, w)
    B = np.exp(-0.5 * ws) * (2.0 * ws / (-cexpm1(-2.0 * ws))) - 1.0
    return np.where(tiny, 0.25, B / (2.0 * ws))


GREG_R = 1.0
GREG_N = 256
GREG_CUT = 0.5
_th = 2.0 * math.pi * np.arange(GREG_N) / GREG_N
_GREG_C = np.fft.fft(_g_reg_direct(GREG_R * np.exp(1j * _th))) / GREG_N \
    / GREG_R ** np.arange(GREG_N)


def g_reg(w):
    """g_reg(w) = g(w) - 1/(2w), analytic in |Im w| < pi with g_reg(0) = 1/4;
    the pole removal is SYMBOLIC (Cauchy coefficients on |w| = 1)."""
    w = np.asarray(w, dtype=np.complex128)
    out = _g_reg_direct(w)
    sm = np.abs(w) <= GREG_CUT
    if sm.any():
        ws = w[sm]
        acc = np.zeros(ws.shape, dtype=np.complex128)
        for n in range(GREG_N // 4 - 1, -1, -1):
            acc = acc * ws + _GREG_C[n]
        out[sm] = acc
    return out


def psi_head(d):
    """Psi_d = -(1/2) int_{-1}^{1} (1 - |v|) dv / (d + v): the triangle-
    smeared simple pole -- CLOSED, D-free, m-free (this is the stable form;
    the second-difference form is checked against it below)."""
    d = np.asarray(d, dtype=float)
    out = np.zeros(d.shape)
    for lo, hi in ((-1.0, 0.0), (0.0, 1.0)):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        v = mid + half * _GLX
        out -= 0.5 * half * (((1.0 - np.abs(v))
                              / (d[..., None] + v)) @ _GLW)
    return out


def psi_head_closed(d):
    """Psi_d = -(1/2) [ (d+1) log(d+1) - 2 d log d + (d-1) log(d-1) ]: the
    closed second difference of w log w, valid for every d >= 1."""
    d = np.asarray(d, dtype=float)

    def xlx(t):
        return np.where(t > 0.0, t * np.log(np.maximum(t, 1.0e-300)), 0.0)
    return -0.5 * (xlx(d + 1.0) - 2.0 * xlx(d) + xlx(d - 1.0))


def arch_G_hat(s, D):
    """Ghat(s, D) = -int (1 - |v|) g_reg(s + D v) dv: the regular part, so
    that c^arch_d = Psi_d + D Ghat(d D, D) EXACTLY for d >= 1."""
    s = np.asarray(s)
    out = np.zeros(np.shape(s), dtype=np.complex128)
    for lo, hi in ((-1.0, 0.0), (0.0, 1.0)):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        v = mid + half * _GLX
        wv = np.asarray(s)[..., None] + D * v
        out -= half * ((1.0 - np.abs(v)) * g_reg(wv)) @ _GLW
    return out


def bernstein_rho(a, b, d_sing):
    """rho = (d + sqrt(d^2 - L^2)) / L for the interval [a, b] with a real
    singularity at distance d_sing from the centre (Bernstein 1912)."""
    c, L = 0.5 * (a + b), 0.5 * (b - a)
    if d_sing <= L:
        return 1.0
    return (d_sing + math.sqrt(d_sing * d_sing - L * L)) / L


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


def run():
    reset()
    t0 = time.time()
    print("=" * 72)
    print("v554  PRIME.SAMPLING.HARM.01 -- the sampling / harmonics "
          "identities (T160/T161)")
    print("=" * 72)

    print("\nS0 -- firewall, frame-A windows, preregistered bars")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    INST = []
    for (k, D, M, h) in build_windows():
        alpha = 0.5 * M * D
        sp = lag_vector_split(alpha, M, atoms_in(alpha))
        r = dict(n=NN_ALL[k], k=k, M=M, h=h, D=sp["D"], alpha=alpha,
                 c=sp["c"], c_ar=sp["c_ar"], c_at=sp["c_at"],
                 X=math.exp(2.0 * alpha))
        r["split"] = float(np.max(np.abs(sp["c"] - sp["c_ar"] - sp["c_at"])))
        A = sym(odd_toeplitz(sp["c"], M))
        lam1 = float(np.linalg.eigvalsh(A)[0])
        if not (lam1 > 0.0):
            continue
        mu = parity_mu(h)[:SCHUR_KB]
        T16 = parity_basis(h)[:SCHUR_KB, :]
        isq = 1.0 / np.sqrt(mu)
        BLL = sym((T16 @ (A @ T16.T)) * np.outer(isq, isq))
        e1 = np.zeros(SCHUR_KB)
        e1[0] = 1.0
        x = np.linalg.solve(BLL, e1)
        x /= max(abs(float(x[0])), 1.0e-300)
        r["mu"], r["x"], r["BLL"] = mu, x, BLL
        y = (T16.T / np.sqrt(mu)) @ x
        r["y"] = y
        w = lag_weights_direct(y, M)
        r["w"] = w
        r["form"] = float(x @ (BLL @ x))
        r["Q_ar"] = float(np.dot(sp["c_ar"], w))
        r["Q_at"] = float(np.dot(sp["c_at"], w))
        INST.append(r)
    h_max = max(r["h"] for r in INST) if INST else 0
    e_form = [abs(r["form"] - r["Q_ar"] - r["Q_at"])
              / max(abs(r["Q_ar"]), abs(r["Q_at"])) for r in INST]
    check(f"S0.INST: {len(INST)} frame-A windows built end to end (odd "
          f"section positive definite on every one; the lag split "
          f"c = c^arch + c^atom exact to "
          f"{max(r['split'] for r in INST):.1e} <= {TOL_SPLIT:.0e}; the "
          f"pairing identity x^T B_LL x = Q^arch + Q^atom holds to "
          f"{max(e_form):.1e} of the large scale on every window); every "
          f"assembled section <= {H_CAP} (max m = {h_max})",
          len(INST) >= 6 and h_max <= H_CAP
          and all(r["split"] <= TOL_SPLIT for r in INST)
          and max(e_form) < 1.0e-12)
    for r in INST:
        print(f"    n={r['n']:>5d} m={r['h']:>4d} X={r['X']:8.1f} "
              f"Q_ar={r['Q_ar']:11.4e} Q_at={r['Q_at']:11.4e} "
              f"form={r['form']:.4f}")

    # ---------------------------------------------------------------- (1)
    print("\nS1 -- (1) the sampling identity (T160, P2)")
    E_S, E_SM = [], []
    for r in INST:
        Mz, Dz, wv = r["M"], r["D"], r["w"]
        at = atoms_in(r["alpha"])
        uu = np.array([t[0] for t in at], dtype=float)
        mm = np.array([t[1] for t in at], dtype=float)
        r["u_at"], r["mu_at"] = uu, mm
        r["mass"] = float(np.sum(mm))
        a_sc = max(float(np.sum(np.abs(r["c_at"] * wv))), 1.0e-300)

        def sample(shift):
            pos = uu / Dz
            i0 = np.floor(pos).astype(np.int64) + shift
            fr = pos - np.floor(pos)
            what = np.zeros(uu.shape[0])
            k0 = (i0 >= 0) & (i0 < Mz)
            what[k0] += (1.0 - fr[k0]) * wv[i0[k0]]
            k1 = (i0 + 1 >= 0) & (i0 + 1 < Mz)
            what[k1] += fr[k1] * wv[i0[k1] + 1]
            samp = -0.5 * float(np.dot(mm, what))
            refl = uu < Dz
            if refl.any():
                samp -= 0.5 * float(np.dot(mm[refl], 1.0 - uu[refl] / Dz)) \
                    * float(wv[0])
            return samp

        E_S.append(abs(sample(0) - r["Q_at"]) / a_sc)
        E_SM.append(abs(sample(1) - r["Q_at"]) / a_sc)
    check(f"S1.SAMPLING: the sampling identity sum_d c^atom_d w_d = "
          f"-(1/2) sum_(n <= X) (2 Lambda(n)/sqrt n) w^(log n) (+ one "
          f"reflected term for u < D), w^ the linear interpolant of the lag "
          f"weights, holds against the direct assembly to "
          f"{max(E_S):.1e} <= {TOL_SAMP:.0e} of the absolute atom scale "
          f"sum|c^atom_d w_d| on {len(INST)}/{len(INST)} windows -- the "
          f"atom half of the pairing IS a Lambda-weighted sampling of w at "
          f"the prime-power positions (T160's P2, per instance); with the "
          f"closed Dirichlet-kernel form of w (v553's address) w^(u) is a "
          f"fixed trigonometric polynomial, so the atom half is identically "
          f"a finite combination of sums sum_n Lambda(n) n^(-1/2) "
          f"cos(t log n) at {NF_HARM} explicit frequencies",
          all(e <= TOL_SAMP for e in E_S))
    check(f"S1.CTRL: a ONE-INDEX SHIFT of the sampling grid breaks the "
          f"identity by {min(E_SM):.2e}..{max(E_SM):.2e} >= "
          f"{BAR_MUT_SAMP:.0e} of the absolute scale on every window "
          f"(against <= {TOL_SAMP:.0e} for the true grid): the identity is "
          f"a statement about THE prime-power positions, not a generic "
          f"near-agreement",
          all(e >= BAR_MUT_SAMP for e in E_SM))

    # ---------------------------------------------------------------- (2)
    print("\nS2 -- (2) the moment laws and the TV theorem (T160, P1/P4)")
    E_M0, E_M1, E_M2, MU_M1, MU_M2, NEG1, NEG2 = [], [], [], [], [], [], []
    for r in INST:
        Mz, wv, y = r["M"], r["w"], r["y"]
        dd = np.arange(Mz, dtype=float)
        m1d = float(np.dot(dd, wv))
        m2d = float(np.dot(dd * dd, wv))
        _, m1c, m2c, S0, S1, P = moments_closed_012(y, Mz)
        E_M0.append(abs(float(np.sum(wv))) / float(np.sum(np.abs(wv))))
        E_M1.append(abs(m1d - m1c) / max(abs(m1c), 1.0e-300))
        E_M2.append(abs(m2d - m2c) / max(abs(m2c), 1.0e-300))
        NEG1.append(m1c)
        NEG2.append(m2c)
        # mutations: a one-index prefix shift in m_1, (M-2) in m_2
        h = Mz // 2
        Pm = np.concatenate(([0.0], np.cumsum(y)))[1:h + 1]
        m1m = -(S0 * S0 + 2.0 * float(np.dot(Pm[1:h], Pm[1:h])))
        MU_M1.append(abs(m1d - m1m) / max(abs(m1c), 1.0e-300))
        m2m = -(2.0 * S1 - (Mz - 2.0) * S0) ** 2
        MU_M2.append(abs(m2d - m2m) / max(abs(m2c), 1.0e-300))
    check(f"S2.MOMENTS: the three closed moment laws hold against the "
          f"direct sums on every window -- m_0 = sum_d w_d = 0 to "
          f"{max(E_M0):.1e} <= {TOL_GAUGE:.0e} of ||w||_1 (the gauge law), "
          f"m_1 = sum_d d w_d = -[S0^2 + 2 sum_j P_j^2] to {max(E_M1):.1e} "
          f"and m_2 = sum_d d^2 w_d = -[2 S1 - (M-1) S0]^2 to "
          f"{max(E_M2):.1e} <= {TOL_MOM:.0e} relative -- with BOTH "
          f"sign-definite forms strictly negative (m_1 = {min(NEG1):.4e}.."
          f"{max(NEG1):.4e}, m_2 = {min(NEG2):.4e}..{max(NEG2):.4e}): the "
          f"pairing cannot see the lag mass, and it sees a linear or "
          f"quadratic trend only with a sign known in advance (T160's "
          f"moment laws, per instance)",
          all(e <= TOL_GAUGE for e in E_M0)
          and all(e <= TOL_MOM for e in E_M1)
          and all(e <= TOL_MOM for e in E_M2)
          and all(v < 0.0 for v in NEG1) and all(v < 0.0 for v in NEG2))
    TVm, TVc, HYP, MUT_TV = [], [], [], []
    for r in INST:
        ca = r["c_ar"]
        tv = float(np.sum(np.abs(np.diff(ca))))
        TVm.append(tv)
        TVc.append(abs(float(ca[0])) + 2.0 * float(np.max(np.abs(ca[1:]))))
        HYP.append(bool(np.max(ca[1:]) <= 0.0
                        and np.min(np.diff(ca[1:])) >= 0.0))
        cf = r["c"]
        MUT_TV.append(bool(np.min(np.diff(cf[1:])) < 0.0))
    check(f"S2.TV: U3 as a THEOREM with checked hypotheses -- c^arch_d <= 0 "
          f"and monotone non-decreasing on d >= 1 (both CHECKED on "
          f"{sum(HYP)}/{len(INST)} windows, never assumed), hence the total "
          f"variation equals the total rise and TV(c^arch) = "
          f"{min(TVm):.4f}..{max(TVm):.4f} <= the closed bound "
          f"|c^arch_0| + 2 sup_(d>=1)|c^arch_d| = {min(TVc):.4f}.."
          f"{max(TVc):.4f} < {TV_CONST:.0f} -- a closed, window-independent "
          f"constant (T160's U3 upgrade, per instance)",
          all(HYP)
          and all(m <= c + 1.0e-12 for m, c in zip(TVm, TVc))
          and all(c < TV_CONST for c in TVc))
    check(f"S2.CTRL: the mutations fail loudly -- a one-index prefix shift "
          f"breaks the m_1 law by {min(MU_M1):.2e}..{max(MU_M1):.2e} >= "
          f"{BAR_MUT_MOM:.0e}, an (M-2) mis-normalisation breaks the m_2 "
          f"law by {min(MU_M2):.2e}..{max(MU_M2):.2e} >= {BAR_MUT_MOM:.0e}, "
          f"and the FULL atom-including kernel violates the monotone "
          f"hypothesis of S2.TV on {sum(MUT_TV)}/{len(INST)} windows: the "
          f"closed laws are statements about THE weight vector and THE "
          f"smooth kernel, not generic near-agreements",
          all(e >= BAR_MUT_MOM for e in MU_M1)
          and all(e >= BAR_MUT_MOM for e in MU_M2) and all(MUT_TV))

    # ---------------------------------------------------------------- (3)
    print("\nS3 -- (3) the harmonic-frequency theorem and the PNT main "
          "term (T161, P3)")
    E_H = []
    for r in INST:
        jj = np.arange(1, NF_HARM + 1, dtype=float)
        tt = math.pi * jj / r["alpha"]
        E_H.append(float(np.max(np.abs(
            tt * 2.0 * r["alpha"] - 2.0 * math.pi * jj))))
    PNTD, RED_TRUE, RED_MUT, FAKE, NB_AT = [], [], [], [], []
    for Xz in X_BATTERY:
        alpha = 0.5 * math.log(Xz)
        at = atoms_in(alpha)
        uu = np.array([t[0] for t in at], dtype=float)
        mm = np.array([t[1] for t in at], dtype=float)
        mass = float(np.sum(mm))
        NB_AT.append(len(at))
        jj = np.arange(1, NF_HARM + 1, dtype=float)
        tt = math.pi * jj / alpha
        E_H.append(float(np.max(np.abs(tt * 2.0 * alpha - 2.0 * math.pi * jj))))
        Sv = (mm[None, :] * np.cos(np.outer(tt, uu))).sum(axis=1)
        mod = 2.0 * (math.sqrt(Xz) * 0.5 - 0.5) / (0.25 + tt * tt)
        PNTD.append(float(np.max(np.abs(Sv - mod))) / mass)
        RED_TRUE.append(float(np.sum(np.abs(Sv - mod)))
                        / max(float(np.sum(np.abs(Sv))), 1.0e-300))
        mod_bad = 2.0 * (math.sqrt(Xz) * 0.5 - 0.5) / (1.0 + 4.0 * tt * tt)
        RED_MUT.append(float(np.sum(np.abs(Sv - mod_bad)))
                       / max(float(np.sum(np.abs(Sv - mod))), 1.0e-300))
        # the measure discriminator: a mass-matched UNIFORM fake measure
        uf = np.linspace(0.0, 2.0 * alpha, uu.shape[0])
        mf = np.full(uu.shape[0], mass / uu.shape[0])
        Sf = (mf[None, :] * np.cos(np.outer(tt, uf))).sum(axis=1)
        FAKE.append(float(np.max(np.abs(Sf - mod))) / mass)
    check(f"S3.HARMONIC: the {NF_HARM} frequencies t_j = pi j / alpha "
          f"satisfy t_j * (2 alpha) = 2 pi j EXACTLY (worst absolute "
          f"deviation {max(E_H):.1e} <= {TOL_HARM:.0e}) on every frame-A "
          f"window AND on the declared Lambda-battery: since the atom "
          f"variable u = log n runs over exactly [0, 2 alpha], the "
          f"{NF_HARM} frequencies of the sampling identity are PRECISELY "
          f"the Fourier harmonics of the log-window, and the atom half of "
          f"the pairing is the vector of the first {NF_HARM} Fourier "
          f"coefficients of the measure sum_n (2 Lambda(n)/sqrt n) "
          f"delta_(log n) (T161's harmonic-frequency theorem, per instance)",
          all(e <= TOL_HARM for e in E_H))
    check(f"S3.PNT: at the harmonic frequencies theta = t log X = 2 pi j "
          f"collapses the partial-summation main term to the CLOSED, "
          f"parameter-free prediction S(t) ~ (sqrt X - 1)/(1/4 + t^2) "
          f"(de la Vallee Poussin 1896; the 1/(1/4 + t^2) is the Mellin "
          f"factor of x^(-1/2)), and on the declared Lambda-battery "
          f"(X = {X_BATTERY[0]:.0e}..{X_BATTERY[-1]:.0e}, "
          f"{min(NB_AT)}..{max(NB_AT)} prime-power atoms, finite sums "
          f"only) the sums S(t) -- assembled from the von-Mangoldt table "
          f"and NOTHING else -- agree with it to {min(PNTD):.4f}.."
          f"{max(PNTD):.4f} of the trivial mass <= the DECLARED cap "
          f"{PNT_CAP} (the sandbox measures 0.014..0.232 down to X = 121, "
          f"falling as X^-0.39 -- a FIT, not consumed); the subtraction is "
          f"NOT vacuous: it reduces the aggregate residual to "
          f"{min(RED_TRUE):.3f}..{max(RED_TRUE):.3f} <= {PNT_RED} of "
          f"sum|S| on every cut-off",
          all(d <= PNT_CAP for d in PNTD)
          and all(x <= PNT_RED for x in RED_TRUE))
    check(f"S3.CTRL: the mutations fail loudly -- a WRONG Mellin pole "
          f"(1 + 4 t^2 in place of 1/4 + t^2) makes the aggregate residual "
          f"{min(RED_MUT):.2f}..{max(RED_MUT):.2f} >= {BAR_MUT_PNT} times "
          f"the true model's on every cut-off, and the MEASURE "
          f"discriminator: a mass-matched UNIFORM fake measure on the same "
          f"window misses the closed prediction by {min(FAKE):.3f}.."
          f"{max(FAKE):.3f} >= {BAR_FAKE_PNT} x the declared cap -- the "
          f"agreement is a property of the von-Mangoldt measure (the "
          f"prime-number theorem), not of any measure with the same mass",
          all(x >= BAR_MUT_PNT for x in RED_MUT)
          and all(f >= BAR_FAKE_PNT * PNT_CAP for f in FAKE))

    # ---------------------------------------------------------------- (4)
    print("\nS4 -- (4) the head split and the scale-free Bernstein rate "
          "(T161, P1)")
    E_P2, E_HS, MUT_HS, RHOW = [], [], [], []
    for r in INST:
        D, Mz = r["D"], r["M"]
        dd = np.arange(1, Mz, dtype=float)
        psi = psi_head(dd)
        E_P2.append(float(np.max(np.abs(psi[:64] - psi_head_closed(dd[:64])))))
        got = psi + D * np.real(arch_G_hat(dd * D, D))
        ref = r["c_ar"][1:]
        sc = max(float(np.max(np.abs(ref))), 1.0e-300)
        E_HS.append(float(np.max(np.abs(got - ref))) / sc)
        MUT_HS.append(float(np.max(np.abs(
            D * np.real(arch_G_hat(dd * D, D)) - ref))) / sc)
        r["psi"] = np.concatenate([[0.0], psi])
        a, b = SA_LO * r["alpha"], SA_HI * r["alpha"]
        RHOW.append(bernstein_rho(a, b, 0.5 * (a + b) - D))
    rho_id = abs(RHO_STAR * RHO_STAR - 3.0 * RHO_STAR + 1.0)
    rho_lim = bernstein_rho(SA_LO, SA_HI, 0.5 * (SA_LO + SA_HI))
    rho_lim2 = bernstein_rho(10.0 * SA_LO, 10.0 * SA_HI,
                             0.5 * (10.0 * SA_LO + 10.0 * SA_HI))
    rho_mut = bernstein_rho(SA_LO, 4.0 * SA_LO,
                            0.5 * (SA_LO + 4.0 * SA_LO))
    check(f"S4.PSI: the two representations of the head -- the closed "
          f"second difference Psi_d = -(1/2)[(d+1)log(d+1) - 2d log d + "
          f"(d-1)log(d-1)] and the smeared pole -(1/2) int (1-|v|) dv/(d+v) "
          f"-- agree to {max(E_P2):.1e} <= {TOL_PSI2:.0e} on the first 64 "
          f"lags, and the HEAD SPLIT c^arch_d = Psi_d + D Ghat(dD, D) "
          f"(Ghat the smear of the regularised g_reg = g - 1/(2w), the "
          f"pole removed SYMBOLICALLY by Cauchy coefficients) holds at "
          f"{max(E_HS):.1e} <= {TOL_SPLIT_HEAD:.0e} of sup|c^arch| at "
          f"EVERY lag d >= 1 of every window -- Psi is CLOSED, D-FREE and "
          f"m-FREE (the log D cancels identically): T161's head split, "
          f"per instance, NO head peel, NO fitted cut",
          all(e <= TOL_PSI2 for e in E_P2)
          and all(e <= TOL_SPLIT_HEAD for e in E_HS))
    check(f"S4.RHO: the scale-free Bernstein rate -- rho* = (3 + sqrt 5)/2 "
          f"= {RHO_STAR:.6f} satisfies rho*^2 - 3 rho* + 1 = 0 to "
          f"{rho_id:.1e} <= {TOL_RHO_ID:.0e}, the D -> 0 limit of the "
          f"peeled interval [{SA_LO} alpha, {SA_HI} alpha] returns it "
          f"exactly ({abs(rho_lim - RHO_STAR):.1e}) and is SCALE-FREE "
          f"(alpha x 10 moves it by {abs(rho_lim2 - rho_lim):.1e}: it "
          f"depends only on the interval ratio {SA_HI / SA_LO:.0f}); every "
          f"window's rho(D) = {min(RHOW):.4f}..{max(RHOW):.4f} exceeds "
          f"{RHO_FLOOR} and sits below rho* (Bernstein 1912): the "
          f"coefficient decay rate of the peeled arch kernel is a FIXED "
          f"constant, uniformly in m (T161's rho_closed, per instance)",
          rho_id <= TOL_RHO_ID
          and abs(rho_lim - RHO_STAR) <= TOL_RHO_ID
          and abs(rho_lim2 - rho_lim) <= TOL_RHO_ID
          and all(RHO_FLOOR < x < RHO_STAR for x in RHOW))
    check(f"S4.CTRL: dropping the Psi term (D Ghat alone) misses c^arch by "
          f"{min(MUT_HS):.2f}..{max(MUT_HS):.2f} >= {BAR_MUT_HEAD} of "
          f"sup|c^arch| on every window (the head IS the non-analytic "
          f"content), and the WRONG interval ratio (b/a = 4 in place of "
          f"{SA_HI / SA_LO:.0f}) moves the closed limit to "
          f"{rho_mut:.4f}, i.e. by {abs(rho_mut - RHO_STAR):.3f} >= "
          f"{BAR_MUT_RHO}: rho* is a property of THE peeled interval",
          all(e >= BAR_MUT_HEAD for e in MUT_HS)
          and abs(rho_mut - RHO_STAR) >= BAR_MUT_RHO)

    # ---------------------------------------------------------------- (5)
    print("\nS5 -- (5) the off-diagonal fraction bound and the sign "
          "refutation (T161, P2)")
    E_D, E_DM, FR, NBADP, SGN_OK = [], [], [], [], []
    for r in INST:
        m = r["h"]
        om = 2.0 * math.pi * np.arange(1, SCHUR_KB + 1) / (2 * m + 1)
        aa = r["x"] / np.sqrt(r["mu"])
        dc_full = fwd_diff(r["c_ar"])
        dc2 = dc_full[2:]
        l1dc = float(np.sum(np.abs(dc2)))
        off = dia = tot = tot_m = 0.0
        nbad = 0
        for k in range(SCHUR_KB):
            for l in range(SCHUR_KB):
                Rk = R_pair(k, l, m, om)
                v_a = float(np.dot(dc_full[1:], abel_tail(Rk)[1:]))
                Rm = R_pair(k, l, m, om, shift=1)
                tot_m += aa[k] * aa[l] * float(
                    np.dot(dc_full[1:], abel_tail(Rm)[1:]))
                tot += aa[k] * aa[l] * v_a
                if k == l:
                    dia += aa[k] * aa[l] * v_a
                else:
                    off += aa[k] * aa[l] * v_a
                    if float(np.dot(dc2, Rk[2:])) / max(l1dc, 1e-300) > 0.0:
                        nbad += 1
        E_D.append(abs(tot - r["Q_ar"]) / max(abs(r["Q_ar"]), 1.0e-300))
        E_DM.append(abs(tot_m - r["Q_ar"]) / max(abs(r["Q_ar"]), 1.0e-300))
        FR.append(abs(off) / max(abs(r["Q_ar"]), 1.0e-300))
        NBADP.append(nbad)
        SGN_OK.append(bool(r["Q_ar"] < 0.0 and off > 0.0))
    check(f"S5.DECOMP: the gauge identity licenses one BOUNDARY-FREE Abel "
          f"step, and the closed weights give the EXACT decomposition "
          f"Q^arch = sum_(k,l) a_k a_l sum_(d>=1) (Delta c^arch)_d "
          f"R^1_kl(d), a_k = x_k / sqrt(mu^P_k), R_kl a difference of four "
          f"Dirichlet kernels -- reproduced to {max(E_D):.1e} <= "
          f"{TOL_DEC:.0e} relative on {len(INST)}/{len(INST)} windows: the "
          f"off-diagonal block is a well-defined piece of the arch half "
          f"(T161's decomposition, per instance)",
          all(e <= TOL_DEC for e in E_D))
    check(f"S5.FRACTION: the certified per-window inequality that SURVIVES "
          f"where the sign law fails -- |off-diagonal block| / |Q^arch| = "
          f"{min(FR):.4f}..{max(FR):.4f} <= {FRAC_CAP} on "
          f"{len(INST)}/{len(INST)} windows (the sandbox measures "
          f"0.1035..0.1713 over h = 50..1218, flat -- a FIT, not consumed): "
          f"the honest replacement for R-B is a FRACTION bound with the "
          f"constant 1/4, costing the chain a factor 1 + 1/4 in the "
          f"constant and nothing in the structure; the m-free version (a "
          f"16 x 16 Gram positivity/norm statement, Fejer 1915 / Schur "
          f"1917) is R-B' and stays OPEN, typed open",
          all(f <= FRAC_CAP for f in FR))
    check(f"S5.SIGN: the REFUTED sign law, wired as the negative control -- "
          f"the arch half is NEGATIVE ({min(r['Q_ar'] for r in INST):.3e}.."
          f"{max(r['Q_ar'] for r in INST):.3e}) while its off-diagonal "
          f"block is POSITIVE on {sum(SGN_OK)}/{len(INST)} windows (the "
          f"HARMFUL direction: the Thomson dual needs an UPPER bound, so "
          f"dropping the block is not safe), and the per-pair inequality "
          f"sum_(d>=2) (Delta c^arch)_d R_kl(d) <= 0 is violated by "
          f"{min(NBADP)}..{max(NBADP)} of {SCHUR_KB * (SCHUR_KB - 1)} "
          f"off-diagonal pairs on every window: R-B as a one-sign "
          f"statement was never the right object, which is exactly WHY "
          f"S5.FRACTION is the surviving statement (T161's refutation, "
          f"per instance -- a refutation wired as content, nothing "
          f"single-signed promoted)",
          all(SGN_OK) and all(n > 0 for n in NBADP))
    check(f"S5.CTRL: a one-index shift of the R-kernel breaks the exact "
          f"decomposition by {min(E_DM):.2e}..{max(E_DM):.2e} >= "
          f"{BAR_MUT_DEC:.0e} relative on every window (against <= "
          f"{TOL_DEC:.0e} for the true kernel): the decomposition is a "
          f"statement about THE Dirichlet-kernel structure",
          all(e >= BAR_MUT_DEC for e in E_DM))

    # ---------------------------------------------------------------- stress
    print("\nS6 -- the no-go discriminator and the controls (T160/T161)")
    m_ng = 96
    M_ng = 2 * m_ng
    c_ng = 1.0 / (1.0 + np.arange(M_ng, dtype=float))
    D_ng = INST[-1]["D"]
    dd_ng = np.arange(1, M_ng, dtype=float)
    got_ng = psi_head(dd_ng) + D_ng * np.real(arch_G_hat(dd_ng * D_ng, D_ng))
    e_ng = float(np.max(np.abs(got_ng - c_ng[1:]))) / float(np.max(np.abs(c_ng[1:])))
    check(f"S6.NOGO: the head split is a statement about THE T115 kernel -- "
          f"on the T145 no-go reconstruction c(l) = 1/(1+l) (m = {m_ng}) "
          f"the same closed formula Psi_d + D Ghat(dD, D) misses by "
          f"{e_ng:.2f} >= {BAR_NOGO_HEAD} of sup|c|: the instrument does "
          f"not report the split where the split is false",
          e_ng >= BAR_NOGO_HEAD)
    # Dirichlet cosine-sum control, incl. the degenerate branch
    rng = np.random.default_rng(554)
    worst_cs = 0.0
    for _ in range(64):
        al = float(rng.uniform(0.05, 3.0))
        be = float(rng.uniform(0.0, 2.0 * math.pi))
        Lc = int(rng.integers(1, 40))
        brute = float(np.sum(np.cos(al * np.arange(1, Lc + 1) + be)))
        closed = float(_cos_sum(np.array([al]), np.array([be]),
                                np.array([float(Lc)]))[0])
        worst_cs = max(worst_cs, abs(closed - brute) / max(1.0, abs(brute)))
    brute0 = float(np.sum(np.cos(np.zeros(7) + 0.3)))
    closed0 = float(_cos_sum(np.array([2.0 * math.pi]), np.array([0.3]),
                             np.array([7.0]))[0])
    worst_cs = max(worst_cs, abs(closed0 - brute0) / abs(brute0))
    check(f"S6.DIRICHLET: the closed cosine-sum identity (Dirichlet 1829) "
          f"agrees with the brute-force sum to {worst_cs:.1e} <= "
          f"{TOL_CTRL:.0e} on 64 random (alpha, beta, L) triples INCLUDING "
          f"the degenerate branch alpha = 0 mod 2 pi: the closed weights "
          f"and R-kernels of S5 rest on this identity and on nothing else",
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
          f"orthonormal to {e_ort:.1e} (Kac-Murdock-Szego 1953), and "
          f"odd_toeplitz(c^L) = L_P for c^L = (2, -1, 0, ...) with residual "
          f"{e_tpl:.1e} == 0 (ZERO tolerance): the section map of the whole "
          f"chain is the one the identities assume",
          e_eig <= 1.0e-11 and e_ort <= 1.0e-12 and e_tpl == 0.0)

    # ---------------------------------------------------------------- fences
    print("\nS7 -- the fences, restated as a check")
    check("S7.FENCE: PER-INSTANCE identities and certified inequalities on "
          "SMALL frame-A windows only -- a FINITE LIST with an explicit "
          "maximum, nothing uniform in the zone index or in D, and NO "
          "statement for ALL D; finite Lambda-sums are allowed and used, "
          "NO RH statement is made, assumed, approached or weakened, no "
          "zero of any L-function is read and no L-function is evaluated "
          "(AST firewall); the delta triage of T161 (required depth vs RH "
          "strength) is a DOCUMENTATION item, NOT a claim of this module; "
          "the open terms after T161 -- R-A' (the prime-free log-moment "
          "sum_d Psi_d w_d, outside the polynomial ladder), R-B' (the "
          "m-free 16 x 16 Gram fraction bound), R-C' (ONE split of the "
          "pairing with delta_eff < 1/2; T161 refutes the arch/atom and "
          "arch+smooth/fluctuation splits with numbers), R-D (a fifth "
          "R1'' device) -- stay OPEN, typed open, and are neither assumed "
          "nor approached; Dirichlet 1829 / Abel 1826 / Fejer 1915 / "
          "Schur 1917 / Bernstein 1912 / Chebyshev 1852 / Mertens 1874 / "
          "de la Vallee Poussin 1896 / Clausen / Lerch / Kac-Murdock-"
          "Szego 1953 / Wilkinson 1968 / Higham 2002 named CLASSICAL; "
          "Weil 1952 / Bombieri 2000 CITED, never used as a criterion; "
          "zero-firewall AST-checked; NO marker upgrade of any "
          "pre-existing contract", True)

    elapsed = time.time() - t0
    print(f"\nv554 runtime: {elapsed:.1f}s")
    print(f"  (1) sampling identity <= {max(E_S):.1e}; grid shift breaks "
          f">= {min(E_SM):.1e}")
    print(f"  (2) moments m_1 <= {max(E_M1):.1e}, m_2 <= {max(E_M2):.1e}; "
          f"TV {min(TVm):.4f}..{max(TVm):.4f} < {TV_CONST:.0f}")
    print(f"  (3) harmonics exact <= {max(E_H):.1e}; PNT deviation "
          f"{min(PNTD):.3f}..{max(PNTD):.3f} <= {PNT_CAP}")
    print(f"  (4) head split <= {max(E_HS):.1e}; rho(D) = {min(RHOW):.4f}.."
          f"{max(RHOW):.4f} < rho* = {RHO_STAR:.6f}")
    print(f"  (5) decomposition <= {max(E_D):.1e}; fraction "
          f"{min(FR):.4f}..{max(FR):.4f} <= {FRAC_CAP}; sign law refuted "
          f"(wired)")
    print(f"  no-go head split misses {e_ng:.2f}; Dirichlet/parity exact")
    return summary("PRIME.SAMPLING.HARM.01 sampling/harmonics identities")


if __name__ == "__main__":
    raise SystemExit(run())
