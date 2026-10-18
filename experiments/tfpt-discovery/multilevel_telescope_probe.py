"""Discovery probe (2026-07-28), part 124 of the prime/window investigation.
Contract MULTILEVEL.TELESCOPE -- build the recursion T123 pointed at, and test
whether the telescope carries the rate.

WHERE THIS SITS (T123 end state, taken as given, rebuilt here)
  T123 (CBS-RESISTS) closed (F3) and identified (F4).  With W = B Z and
  V = B P the two orthogonal isometries of the odd sector,
      A_c = V^T T_M(c) V,  A_z = W^T T_M(c) W,  B_x = V^T T_M(c) W,
  the certified band route made the Rayleigh step sharp,
      y^T A_z y >= y^T E_z y,   E_z = W^T T_M(ell) V,  lam_min(E_z) > 0 uniform,
  slack 1.0007..1.007 -- but EVERY route to the coupling needed the COARSE form
  from below, and lam_min(A_c) = 1.7e-5..2.9e-4 at cond up to 3.1e7 sits 2..5
  orders under the certified envelope margin, rising like alpha^+4.2, because
  the near-null direction is SMOOTH and its eigenvalue comes from a cancellation
  INSIDE the form.  lam_min(E_c) < 0 everywhere.  The certified balance stalled
  at S6/eps_c ~ D^-0.069 alpha^-0.544 against the ceiling alpha^-0.044, a gap of
  exactly alpha^+0.500 = the coupling term.  And the ceiling IS the eps_f
  discard, because
      eps_c = eps_f + y^T S y                                    (T118)
  is an IDENTITY: an additive chain would have ceiling 1, but eps_f needs its
  bound one level down.  T123's closing line: the two-level argument cannot be
  tightened, it has to become a RECURSION, with base case (F4).

WHAT THIS PROBE DOES
  Y1  THE TELESCOPE, EXACTLY.  The level chain D_0 > D_1 > ... > D_L (halvings,
      alpha fixed).  Three identities are verified level by level:
        (N)  NESTING / SELF-SIMILARITY.  P^T A^(l+1) P = A^(l) and
             P^T b^(l+1) = b^(l): the coarse block of the window form at D_{l+1}
             IS the window form at D_l = 2 D_{l+1}, and the pole vector is
             consistent with it (sinh(a-d) + sinh(a+d) = 2 cosh d sinh a).  So
             the whole ladder is ONE continuous form on NESTED spaces, and the
             two-level system of T122/T123 is one rung of it.
        (T)  THE TELESCOPE.  eps_l = eps_{l+1} + delta_l, delta_l = y_l^T S_l y_l
             -- the T118 saturation identity at every rung -- hence
                 eps_0 = eps_L + sum_l delta_l          (EXACT).
        (G)  GALERKIN ORTHOGONALITY.  delta_l = || u_{l+1} - P u_l ||^2_{A_{l+1}}
             (Cea 1964 / Galerkin): the rung contribution is the energy of the
             level correction, which is why it is nonnegative and why the sum
             telescopes.
      Then the LEVEL DISTRIBUTION: which rungs carry the mass, is it geometric,
      and what is 1 - eps_L/eps_0 -- the ceiling of the L-level chain.
  Y2  THE CERTIFIED RUNG CONTRIBUTION WITHOUT THE COARSE INVERSE.  The core of
      this part.  Two dual descriptions of the same rung:
        (i)  THE PRIMAL (minimum) FORM.  delta_l = min_x (V x + W y)^T T (V x +
             W y) = min_{w in V_l} || u_{l+1} - w ||^2_A.  A MINIMUM: every test
             vector gives an UPPER bound.  Wrong direction for a supply.
        (ii) THE DUAL (maximum) FORM.  With the level-l residual
                 r_l = t_{l+1} - A_{l+1} P u_l,   V^T r_l = 0 (Galerkin), so
                 r_l = W shat_l,   shat_l = s_l - B_x^T u_l,  s_l = W^T t_{l+1},
                 delta_l = || r_l ||^2_{A^{-1}} = shat^T S^{-1} shat
                         = max_v (shat^T v)^2 / (v^T S v).
             A MAXIMUM: every test vector gives a LOWER bound, and the
             denominator wants S from ABOVE.  That is the direction flip this
             part is about, because
                 S <= A_z    needs only   A_c >= 0   (SEMIDEFINITENESS),
                 A_z <= U := W^T T_M(up) W   is Parseval plus the certified
                 envelope up >= sigma^(M) (the MIRROR of T123's E_z = W^T
                 T_M(ell) W, on the block where it works),
             so the optimal test vector is available in closed form and
                 delta_l >= shat^T U^{-1} shat =: cb_l                   (8R)
             is CERTIFIED as soon as A_c >= 0 and U > 0 -- no A_c^{-1}, no
             lam_min(A_c), no CBS constant.  Measured against the truth, against
             the Richardson vector, and against the T123 pair (E_z, E_c).
             shat is a function of the CARRIED coarse solution, exactly as y is
             in T122/T123's own certified supplies S2 and S6, so the comparison
             of exponents is like-for-like; the SOLUTION-FREE version of the
             rung is tested separately and fails, for a reason worth recording.
        (iii) THE LEVINSON LEDGER.  q_l = sum_n rho_n^2 / E_n exactly (T119 mass
             budget, Levinson 1947 / Durbin 1960), so the rung contribution is a
             DIFFERENCE of two innovation sums.  Tested as a bordering
             hypothesis: is the coarse sum the head of the fine sum?
  Y3  THE CANCELLATION STRUCTURE OF THE COARSE DIRECTION.  The near-null
      eigenvector of A^(l) -- smoothness, cancellation depth, envelope margin,
      and the SELF-SIMILARITY overlap |<P w_l, w_{l+1}>|.  If the coarse form of
      rung l IS the window form of rung l-1, then "coarse positivity at rung l"
      is the conclusion of rung l-1, and a coarse-to-fine induction closes.
  Y4  THEOREM V8, the new certified balance, and the defect counter.

WHAT THIS PART FOUND, IN ONE LINE
  The exit T123 pointed at is not the recursion's LENGTH but its DIRECTION: a
  rung of the telescope is a residual in the INVERSE norm, i.e. a MAXIMUM, so
  it wants the form from ABOVE, where Parseval and the certified envelope both
  work -- the coarse block then enters only through the SIGN required by
  Haynsworth monotonicity, and by nesting that sign is the previous rung's own
  conclusion.  (F4) collapses from a quantitative estimate to a hypothesis a
  coarse-to-fine induction already carries; the base case becomes eps_L >= 0.
  What is left of the coupling is one scalar, and it is a cancellation.

PREREGISTERED VERDICTS
  TELESCOPE-CARRIES : the telescope carries the rate with certified rung
                      contributions, base case only semidefiniteness -- (F4)
                      collapses.
  LEVINSON-LEDGER   : the bookkeeping form is exact, certification partial --
                      with the precise rest.
  TELESCOPE-STALLS  : the rung contributions resist certification -- and why.
  Element gates: el_firewall, el_y0, el_y1, el_y2, el_y3, el_y4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger/TeX/website/
    changelog edit, no verification/ module, no next.txt, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * RH => window Weil positivity is NOT used anywhere.  Every statement is
    about a GIVEN window at a GIVEN resolution.
  * CERTIFIED vs CLASSICAL vs MEASURED vs FIT, per line.  EVERY bound states its
    direction, and the direction of the extremum it comes from: a MINIMUM
    principle gives upper bounds, a MAXIMUM principle gives lower bounds, and
    (8R) is used only in the second sense.  A completed Cholesky of A - s I
    certifies lam_min(A) >= s - c_h u ||A||_2, u = 2^-53,
    c_h = (h+1)/(1-(h+1)u) (Wilkinson 1968; Higham 2002 Thm 10.3/10.4).
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    matrix-free FFT levers may exceed it.  Probe budget < 900 s.
  * Classical anchors, WITH DIRECTION:
      Parseval / v^T T_M(g) v = (1/2pi) int g |V|^2 -- an IDENTITY, exact for
        deg |V|^2 < M; g >= 0 => T_M(g) PSD.  Both directions of (8R) rest on
        it: up >= sigma gives U >= A_z, ell <= sigma gives E_z <= A_z,
      Galerkin orthogonality / Cea 1964; Bessel: the nested-space energy
        increment is a squared A-distance (LOWER bound zero, and the telescope),
      Levinson 1947 / Durbin 1960 / Delsarte-Genin 1986: the exact innovation
        ledger q = sum rho^2/E (an IDENTITY),
      Yserentant 1986 / Bramble-Pasciak-Xu 1990 / Brandt 1977 / Axelsson-
        Vassilevski 1989-91: hierarchical splittings, BPX telescopes and the
        strengthened CBS constant -- gamma^2 is the WORST CASE (UPPER) and is
        exactly what (8R) avoids needing,
      Haynsworth 1968 / Albert 1969: Schur complements; the Schur complement of
        a PSD-bordered form is monotone, S <= A_z whenever A_c >= 0,
      Loewner 1934: A <= B, both PD  =>  B^{-1} <= A^{-1} (operator antitony of
        the inverse) -- the step that turns an UPPER bound on S into a LOWER
        bound on shat^T S^{-1} shat,
      Kantorovich 1948: the quality of a single test vector against the optimal
        one (quoted for the Richardson contrast only),
      Szego 1939 / Grenander-Szego 1958 Ch. 5 (LOWER, symbol side),
      Gershgorin 1931 (UPPER), Frobenius (UPPER for PSD),
      Weil 1952 (the explicit formula kernel), Chebyshev 1852 / Mertens (atom
        counts), Cholesky / Wilkinson 1968 / Higham 2002 (the fp floor).

OUTCOME OF THIS RUN  =>  see the Y4 ledger and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh
from scipy.linalg import solve_triangular

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
SQ2 = math.sqrt(2.0)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

ATOM_MAX = 400000
ZONE_MAX = 300000
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

L_CAP = 2 ** 20              # FFT-only symbol grid cap (no matrix)
ENV_OS = 48                  # starting oversampling of the certified envelope
ENV_FRAC = 0.10              # envelope margin target, relative to the scale

# the level chains: M_l = mtop * 2^l, l = 0..NLEV-1, alpha fixed.  TWO chain
# offsets per zone, so that D_0 is NOT collinear with alpha across the ladder
# and the telescope balance can be fitted in (D, alpha) like the rung balance.
MTOPS = (32, 48, 64, 80)
NLEV = 6                     # M = 32..1024 up to 80..2560, odd h = 16..1280
N_ZONE = 20
N_LOW = 3                    # size of the low invariant subspace tracked in Y3

# the T116 demand law and the T122/T123 numbers -- QUOTED FITS, never re-derived
THETA_T116 = 1.79
PHI_T116 = -6.04
PHI_S6_T123 = -0.544
THETA_S6_T123 = -0.069
PHI_CEIL_T123 = -0.044
PHI_GAP_T123 = 0.500
QE_LO_T123 = 1.0007
QE_HI_T123 = 1.007
LAM_AC_LO_T123 = 1.7e-5
LAM_AC_HI_T123 = 2.9e-4
COND_C_HI_T123 = 3.1e7
NLEV_LO_T123 = 4
NLEV_HI_T123 = 8

# the frequency cells of T123, kept only for the envelope report
CELL_BREAKS = np.array([0.0, math.pi / 8.0, math.pi / 4.0, 3.0 * math.pi / 8.0,
                        math.pi / 2.0, 3.0 * math.pi / 4.0,
                        math.pi + 1.0e-9])
NCELL = CELL_BREAKS.shape[0] - 1


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-36s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-36s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


def rel(Dm, Rf):
    return float(np.abs(Dm).max()) / max(float(np.abs(Rf).max()), 1.0e-300)


def rng(v, f="%.3e"):
    v = [x for x in v if np.isfinite(x)]
    if not v:
        return "n/a"
    return (f + ".." + f) % (min(v), max(v))


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
# ----------------------------------------------------------------------------
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "numpy", "scipy"}


def firewall():
    src = open(os.path.abspath(__file__), "r").read()
    low = src.lower()
    hits = [tok for tok in FORBIDDEN_TOKENS if tok in low]
    tree = ast.parse(src)
    bad_imports, bad_writes = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    bad_imports.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                bad_imports.append(node.module)
        elif isinstance(node, ast.Call):
            fn = node.func
            nm = getattr(fn, "id", None) or getattr(fn, "attr", None)
            if nm in ("open",):
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(ch in mode for ch in "wax+"):
                    bad_writes.append(mode)
    check("el_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("el_firewall.imports", not bad_imports,
          "import roots %s" % sorted(ALLOWED_IMPORT_ROOTS))
    check("el_firewall.no_writes", not bad_writes, "no write-mode open()")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- T111..T123 code path
# ----------------------------------------------------------------------------
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


def atoms_in(alpha, atoms_all):
    return [(t[2], t[3]) for t in atoms_all if t[2] <= 2.0 * alpha + 1.0e-14]


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952) -- verbatim T111..T123 code path
# ----------------------------------------------------------------------------
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = (1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return (tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w)) / (-np.expm1(-2.0 * w))


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
    """The T115 O(#atoms) lag assembly (bit-identical to the T111 reference)."""
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


# ----------------------------------------------------------------------------
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T123)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    """(B^T Toeplitz(c) B)_{rs} = c_{|r-s|} - c_{M-1-r-s}."""
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def odd_extend(b, M):
    """tau with B^T tau = b: tau_r = b_r / sqrt2, tau_{M-1-r} = -b_r / sqrt2."""
    h = M // 2
    tau = np.empty(M)
    tau[:h] = b / SQ2
    tau[h:] = -b[::-1] / SQ2
    return tau


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(A):
    return float(np.abs(A).sum(axis=1).max())


def cert_pd(A):
    """CERTIFIED positive definiteness: a completed Cholesky of A - delta I with
    delta the declared fp floor.  Returns (ok, delta, factor)."""
    n = A.shape[0]
    dlt = chol_floor(gersh(A), n)
    fac = safe_cho(A - dlt * np.eye(n))
    return (fac is not None), dlt, fac


# ----------------------------------------------------------------------------
# THE TWO-GRID RESTRICTIONS, matrix-free.  P e_j = (e_{2j} + e_{2j+1})/sqrt2 is
# the piecewise-constant prolongation, Z e_j = (e_{2j} - e_{2j+1})/sqrt2 the
# oscillation basis; [P Z] is orthogonal, so V = B P and W = B Z are the two
# orthogonal isometries of T123 and A_c, A_z, B_x are the three blocks of ONE
# odd window form in that basis.
# ----------------------------------------------------------------------------
def rest_p(X):
    return (X[0::2] + X[1::2]) / SQ2


def rest_z(X):
    return (X[0::2] - X[1::2]) / SQ2


def prol_p(x):
    return np.repeat(x, 2) / SQ2


def prol_z(x):
    return (np.repeat(x, 2) * np.tile(np.array([1.0, -1.0]), x.shape[0])) / SQ2


def two_grid_blocks(A):
    """A_c = P^T A P, A_z = Z^T A Z, B_x = P^T A Z (A symmetric)."""
    PtA = rest_p(A)
    ZtA = rest_z(A)
    Ac = sym(rest_p(PtA.T).T)
    Az = sym(rest_z(ZtA.T).T)
    Bx = rest_z(PtA.T).T
    return Ac, Az, Bx


def zz_compress(A):
    return sym(rest_z(rest_z(A).T).T)


def pp_compress(A):
    return sym(rest_p(rest_p(A).T).T)


# ----------------------------------------------------------------------------
# the symbol machinery -- FFT only, no matrix, no size cap
# ----------------------------------------------------------------------------
def next_pow2(n):
    k = 1
    while k < n:
        k *= 2
    return k


def sym_grid(c, L):
    """f(th_m), th_m = 2 pi m / L, for f(th) = sum_{|j|<M} c_{|j|} e^{i j th}."""
    M = c.shape[0]
    pad = np.zeros(L)
    pad[:M] = c
    half = 2.0 * np.fft.rfft(pad).real - c[0]
    f = np.empty(L)
    f[:L // 2 + 1] = half
    f[L // 2 + 1:] = half[1:L // 2][::-1]
    return f


def dsym_abs_grid(c, L):
    M = c.shape[0]
    pad = np.zeros(L)
    pad[:M] = np.arange(M) * c
    g = np.abs(2.0 * np.fft.rfft(pad).imag)
    out = np.empty(L)
    out[:L // 2 + 1] = g
    out[L // 2 + 1:] = g[1:L // 2][::-1]
    return out


def cert_env(c, os_start=ENV_OS, cap=L_CAP, frac=ENV_FRAC):
    """The CERTIFIED per-cell envelope ell <= sigma^(M) <= up on every cell of
    width dt centred at a grid point (second-order Taylor margin, |sigma''|
    bounded globally by 2 sum j^2 |c_j|).  BOTH sides are certified at every L."""
    M = c.shape[0]
    L = min(next_pow2(os_start * M), cap)
    while True:
        f = sym_grid(c, L)
        fp = dsym_abs_grid(c, L)
        dt = 2.0 * math.pi / L
        j = np.arange(M, dtype=float)
        fpp = 2.0 * float(np.sum(j * j * np.abs(c)))
        d = 0.5 * dt * fp + dt * dt / 8.0 * fpp
        ell = f - d
        up = f + d
        marg = float(np.max(d))
        pos = ell[ell > 0.0]
        scale = float(np.median(pos)) if pos.size > 8 else float(np.max(f))
        if marg <= frac * max(scale, 1.0e-300) or 2 * L > cap:
            return ell, up, f, marg, L, scale
        L *= 2


def pwc_lags(g, n):
    """The EXACT Fourier lags of a function that is piecewise constant on the L
    certified cells:  g_k = X_k sin(k dt / 2) / (pi k),  g_0 = mean(g).  For
    g >= 0, T_n(g) is PSD and v^T T_n(g) v = (1/2pi) int g |V|^2 EXACTLY."""
    L = g.shape[0]
    dt = 2.0 * math.pi / L
    X = np.fft.rfft(g).real
    m = np.arange(n, dtype=float)
    lag = np.zeros(n)
    lag[0] = float(g.mean())
    k = min(n, X.shape[0])
    lag[1:k] = X[1:k] * np.sin(m[1:k] * dt * 0.5) / (math.pi * m[1:k])
    return lag


def pwc_lag_brute(g, klist):
    """Direct cell-exact evaluation of the same lags, for the identity check."""
    L = g.shape[0]
    dt = 2.0 * math.pi / L
    th = np.arange(L) * dt
    out = []
    for k in klist:
        if k == 0:
            out.append(float(g.mean()))
        else:
            w = 2.0 * math.sin(k * dt * 0.5) / k
            out.append(float(np.sum(g * np.cos(k * th)) * w / (2.0 * math.pi)))
    return np.array(out)


# ----------------------------------------------------------------------------
# the EXACT recursion: Levinson 1947 / Durbin 1960 on the FULL Toeplitz form
# ----------------------------------------------------------------------------
def levinson(c, b):
    """Solve Toeplitz(c) x = b by the classical recursion, MATRIX-FREE.
    Returns x, the leading-minor pivots E_n = det T_{n+1}/det T_n, the
    innovations rho_n, the reflection coefficients, and an ok flag."""
    M = c.shape[0]
    x = np.zeros(M)
    p = np.zeros(M)
    Es = np.empty(M)
    rho = np.empty(M)
    kap = np.empty(M)
    E = float(c[0])
    Es[0] = E
    rho[0] = float(b[0])
    kap[0] = float("nan")
    x[0] = b[0] / E
    npv = 0
    for n in range(1, M):
        k = (float(c[n]) - (float(np.dot(p[:npv], c[n - 1:0:-1]))
                            if npv else 0.0)) / E
        if npv:
            p[:npv] = p[:npv] - k * p[:npv][::-1].copy()
        p[npv] = k
        npv += 1
        E = E * (1.0 - k * k)
        Es[n] = E
        kap[n] = k
        if not np.isfinite(E) or E == 0.0:
            return x, Es[:n + 1], rho[:n], kap[:n + 1], False
        r = float(b[n]) - float(np.dot(x[:n], c[n:0:-1]))
        rho[n] = r
        g = r / E
        x[:n] = x[:n] - g * p[:n][::-1].copy()
        x[n] = g
    return x, Es, rho, kap, True


# ----------------------------------------------------------------------------
# fits (every one a FIT, with a jackknife band), frames
# ----------------------------------------------------------------------------
def fit_line(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_band(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = x.shape[0]
    a, b, rms = fit_line(x, y)
    if n < 4:
        return a, b, rms, float("nan")
    bs = []
    for i in range(n):
        k = np.ones(n, dtype=bool)
        k[i] = False
        bs.append(fit_line(x[k], y[k])[1])
    bs = np.asarray(bs)
    se = math.sqrt((n - 1) / n * float(np.sum((bs - bs.mean()) ** 2)))
    return a, b, rms, se


def _plane(x1, x2, y):
    A = np.stack([np.ones_like(x1), x1, x2], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return sol, float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_plane(x1, x2, y):
    """log X = a + theta * log D + phi * log alpha, with jackknife bands."""
    x1 = np.asarray(x1, float)
    x2 = np.asarray(x2, float)
    y = np.asarray(y, float)
    n = x1.shape[0]
    sol, rms = _plane(x1, x2, y)
    if n < 6:
        return sol[0], sol[1], sol[2], rms, float("nan"), float("nan")
    th, ph = [], []
    for i in range(n):
        k = np.ones(n, dtype=bool)
        k[i] = False
        s2, _ = _plane(x1[k], x2[k], y[k])
        th.append(s2[1])
        ph.append(s2[2])
    th = np.asarray(th)
    ph = np.asarray(ph)
    se_t = math.sqrt((n - 1) / n * float(np.sum((th - th.mean()) ** 2)))
    se_p = math.sqrt((n - 1) / n * float(np.sum((ph - ph.mean()) ** 2)))
    return sol[0], sol[1], sol[2], rms, se_t, se_p


def zone_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    return M, 0.5 * M * D, M * D - u


def frame_D(g, nu):
    return 0.5 * g / nu


def step_frame(u_old, u_new, D):
    M_o = zone_window(u_old, D)[0]
    M_n = zone_window(u_new, D)[0]
    dm = M_n - M_o
    if dm <= 0:
        return None
    if dm % 2:
        dm += 1
        M_n = M_o + dm
    gc = dm // 2
    if M_n // 2 - M_o // 2 != gc:
        return None
    return dict(D=D, M_o=M_o, M_n=M_n, gc=gc, al_o=0.5 * M_o * D,
                al_n=0.5 * M_n * D, h_o=M_o // 2, h_n=M_n // 2)


# ----------------------------------------------------------------------------
section("Y0  SETUP -- the zone ladder, the level chain, the caps")
# ----------------------------------------------------------------------------
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
ZALL = [t for t in ATOMS_ALL if t[0] <= ZONE_MAX]
GAPS = [ATOMS_ALL[i + 1][2] - t[2] for i, t in enumerate(ZALL)]
ZTAB = []
for i in range(len(ZALL) - 1):
    n_k, lam_k, u_k, mu_k = ZALL[i]
    ZTAB.append(dict(idx=i, n=n_k, u=u_k, g=GAPS[i], u_next=ZALL[i + 1][2]))
info("Y0.atoms", "%d prime-power atoms up to %d; %d zones up to n = %d"
     % (len(ATOMS_ALL), ATOM_MAX, len(ZTAB), ZONE_MAX))

ZF = []
for row in ZTAB:
    D = frame_D(row["g"], NU_MAIN)
    fr = step_frame(row["u"], row["u_next"], D)
    if fr is None:
        continue
    fr.update(n=row["n"], u=row["u"], g=row["g"])
    ZF.append(fr)
ZF_OK = sorted([z for z in ZF if H_MIN <= z["h_o"] and z["M_o"] % 2 == 0],
               key=lambda z: z["n"])
_NG = np.geomspace(ZF_OK[0]["n"], ZF_OK[-1]["n"], N_ZONE)
ZONES, _seen = [], set()
for _tn in _NG:
    z = min(ZF_OK, key=lambda w: abs(math.log(w["n"] / _tn)))
    if z["n"] not in _seen:
        _seen.add(z["n"])
        ZONES.append(z)
def ms_chain(mtop):
    return [mtop * (2 ** e) for e in range(NLEV)]


MS_ALL = [m for mt in MTOPS for m in ms_chain(mt)]
check("el_y0.ladder", len(ZF_OK) >= 200 and len(ZONES) >= 5,
      "frame-A ladder as in T114/T115/T122/T123: %d admissible handovers "
      "(nu = %d, D = g/(2 nu)), n = %d..%d; %d zones taken geometrically, "
      "alpha = %.3f..%.3f"
      % (len(ZF_OK), NU_MAIN, ZF_OK[0]["n"], ZF_OK[-1]["n"], len(ZONES),
         min(z["al_o"] for z in ZONES), max(z["al_o"] for z in ZONES)))
check("el_y0.chain_cap", max(MS_ALL) // 2 <= MAX_H,
      "%d level chains per zone, M = %s (each L = %d halvings of D at FIXED "
      "alpha; the offsets decouple D_0 from alpha); largest factorised odd "
      "form h = M/2 = %d <= %d"
      % (len(MTOPS), " | ".join(", ".join(str(m) for m in ms_chain(mt))
                                for mt in MTOPS),
         NLEV - 1, max(MS_ALL) // 2, MAX_H))
info("Y0.fp_regime", "u = 2^-53 = %.3e; a completed Cholesky of A - delta I "
     "with delta = c_h u ||A||_inf, c_h = (h+1)/(1-(h+1)u), CERTIFIES "
     "lam_min(A) > 0; at h = %d the floor is %.2e * ||A||_inf.  eigh is "
     "certified only to that floor and is labelled MEASURED throughout"
     % (U_ROUND, max(MS_ALL) // 2, chol_floor(1.0, max(MS_ALL) // 2)))
info("Y0.rh_fence", "RH => window Weil positivity is NOT used anywhere.  Every "
     "statement below is about a GIVEN window at a GIVEN resolution")
info("Y0.quoted", "T123 is QUOTED, not re-derived: certified S6/eps_c ~ "
     "D^%+.3f alpha^%+.3f, ceiling alpha^%+.3f, gap alpha^%+.3f = the coupling "
     "term; slack of (5R*) q_e = %.4f..%.4f; lam_min(A_c) = %.1e..%.1e at "
     "cond <= %.1e; lam_min(E_c) < 0 everywhere; T123 estimated %d..%d "
     "recursion levels.  Demand law eps ~ D^%.2f alpha^%.2f"
     % (THETA_S6_T123, PHI_S6_T123, PHI_CEIL_T123, PHI_GAP_T123, QE_LO_T123,
        QE_HI_T123, LAM_AC_LO_T123, LAM_AC_HI_T123, COND_C_HI_T123,
        NLEV_LO_T123, NLEV_HI_T123, THETA_T116, PHI_T116))
info("Y0.direction", "DIRECTION DISCIPLINE.  A MINIMUM principle (the primal "
     "Schur form) yields UPPER bounds only; a MAXIMUM principle (the dual "
     "residual form) yields LOWER bounds only.  Every supply below comes from "
     "the MAXIMUM form, and every majorant fed into its denominator (S <= A_z "
     "<= U) is an UPPER bound, certified by Parseval against the envelope")
info("Y0.timing", "Y0 done, %.1f s used" % (time.time() - T_START))


# ----------------------------------------------------------------------------
# the per-zone analysis -- ONE pass over the level chain delivers Y1, Y2, Y3
# ----------------------------------------------------------------------------
def analyse_zone(z, mtop):
    al = z["al_o"]
    atoms = atoms_in(al, ATOMS_ALL)
    MS = ms_chain(mtop)
    lv = []
    for M in MS:
        c, D = lag_vector_fast(al, M, atoms)
        A = sym(odd_toeplitz(c, M))
        b = odd_pole_vector(al, M)
        fac = safe_cho(A)
        if fac is None:
            return None
        u = cho_solve(fac, b, check_finite=False)
        q = float(b @ u)
        pd_ok, pd_dlt, _ = cert_pd(A)
        lv.append(dict(M=M, D=D, c=c, A=A, b=b, u=u, q=q, eps=1.0 - q,
                       h=M // 2, pd=int(pd_ok), pd_dlt=pd_dlt))

    # ---- Y2(iii)  the Levinson ledger, one recursion per level -------------
    for L in lv:
        tau = odd_extend(L["b"], L["M"])
        xL, Es, rho, kap, ok = levinson(L["c"], tau)
        n_ok = min(Es.shape[0], rho.shape[0])
        contrib = rho[:n_ok] ** 2 / Es[:n_ok]
        L["lev_ok"] = int(ok)
        L["lev_q"] = float(np.sum(contrib))
        L["lev_contrib"] = contrib
        L["lev_res"] = abs(L["lev_q"] - L["q"]) / max(abs(L["q"]), 1.0e-300)
        L["nneg_piv"] = int(np.sum(Es < 0.0))

    # ---- Y3  the near-null direction of every level form -------------------
    for L in lv:
        nlow = min(N_LOW, L["h"])
        wv, Wv = eigh(L["A"], subset_by_index=[0, nlow - 1])
        w = Wv[:, 0]
        w = w / math.sqrt(float(w @ w))
        L["lam_min"] = float(wv[0])
        L["lam_low"] = wv
        L["Wlow"] = Wv
        L["degen"] = float(wv[min(1, nlow - 1)]) / max(float(wv[0]), 1.0e-300)
        L["w"] = w
        L["osc_frac"] = float(rest_z(w) @ rest_z(w))
        aw = np.abs(L["A"]) @ np.abs(w)
        L["cancel"] = abs(float(w @ (L["A"] @ w))) / max(float(np.abs(w) @ aw),
                                                         1.0e-300)
        nu_ = math.sqrt(float(L["u"] @ L["u"]))
        nb_ = math.sqrt(float(L["b"] @ L["b"]))
        L["ov_u"] = abs(float(w @ L["u"])) / max(nu_, 1.0e-300)
        L["ov_b"] = abs(float(w @ L["b"])) / max(nb_, 1.0e-300)
        L["lam_max"] = float(eigvalsh(L["A"], subset_by_index=[L["h"] - 1,
                                                               L["h"] - 1])[0])
        L["cond"] = L["lam_max"] / max(L["lam_min"], 1.0e-300)

    # SELF-SIMILARITY, two readings.  (a) the eigenvector overlap, which is
    # fragile wherever the two lowest levels nearly cross; (b) the invariant
    # subspace overlap ||Q_K^T P w_l||, which is not.  And the exact one:
    # by NESTING, (P w_l)^T A^(l+1) (P w_l) = w_l^T A^(l) w_l = lam_min(A^(l)),
    # so the prolonged coarse near-null direction has Rayleigh quotient exactly
    # lam_min(A^(l)) at the finer level -- an IDENTITY; only the RATIO to
    # lam_min(A^(l+1)) is a measurement.
    for e in range(NLEV - 1):
        pw = prol_p(lv[e]["w"])
        lv[e]["selfsim"] = abs(float(pw @ lv[e + 1]["w"]))
        proj = lv[e + 1]["Wlow"].T @ pw
        lv[e]["selfsim_k"] = math.sqrt(float(proj @ proj))
        lv[e]["rq_id"] = (abs(float(pw @ (lv[e + 1]["A"] @ pw))
                              - lv[e]["lam_min"])
                          / max(abs(lv[e]["lam_max"]), 1.0e-300))
        lv[e]["rq_rat"] = lv[e]["lam_min"] / max(lv[e + 1]["lam_min"],
                                                 1.0e-300)

    # ---- Y1 / Y2  the rungs ------------------------------------------------
    rungs = []
    for e in range(NLEV - 1):
        fine, coarse = lv[e + 1], lv[e]
        A_f, M, h_c = fine["A"], fine["M"], fine["M"] // 4
        Ac, Az, Bx = two_grid_blocks(A_f)
        b_c = rest_p(fine["b"])
        s = rest_z(fine["b"])
        id_nest_A = rel(Ac - coarse["A"], coarse["A"])
        id_nest_b = rel(b_c - coarse["b"], coarse["b"])
        fac_c = safe_cho(Ac)
        if fac_c is None:
            return None
        Lc = fac_c[0]
        x_c = cho_solve(fac_c, b_c, check_finite=False)
        q_c = float(b_c @ x_c)
        delta = fine["q"] - q_c
        if not (delta > 0.0):
            return None
        y = rest_z(fine["u"])
        shat = s - Bx.T @ x_c
        Gm = solve_triangular(Lc, Bx, lower=True, check_finite=False)
        S = sym(Az - Gm.T @ Gm)
        fac_S = safe_cho(S)
        if fac_S is None:
            return None
        y_dual = cho_solve(fac_S, shat, check_finite=False)
        id_ysy = abs(float(y @ (S @ y)) - delta) / delta
        id_dual = abs(float(shat @ y_dual) - delta) / delta
        dd = fine["u"] - prol_p(x_c)
        id_gal = abs(float(dd @ (A_f @ dd)) - delta) / delta
        id_yopt = (math.sqrt(float((y - y_dual) @ (y - y_dual)))
                   / max(math.sqrt(float(y @ y)), 1.0e-300))
        # the primal MINIMUM form, for the direction check:
        #     delta = min_x (P x + Z y)^T A_f (P x + Z y),
        # attained at x* = P^T u_{l+1} - u_l (so that P x* + Z y = dd), hence
        # ANY other coarse component gives a value ABOVE delta -- an UPPER
        # bound, never a supply.
        xstar = rest_p(fine["u"]) - x_c
        id_min_att = rel(prol_p(xstar) + prol_z(y) - dd, dd)
        vt2 = dd + prol_p(0.05 * np.abs(xstar) + 1.0e-3 * math.sqrt(delta))
        min_up = float(vt2 @ (A_f @ vt2))
        min_ok = int(min_up >= delta * (1.0 - 1.0e-12))

        # ---- the certified envelope of the FINE level ----------------------
        ell, up, fgr, marg, Lg, scale = cert_env(fine["c"])
        _kchk = [0, 1, 2, 3, 7, M - 1]
        _g0 = np.maximum(float(scale) - ell, 0.0)
        id_lag = float(np.max(np.abs(pwc_lags(_g0, M)[_kchk]
                                     - pwc_lag_brute(_g0, _kchk)))
                       / max(float(np.abs(pwc_lag_brute(_g0, _kchk)).max()),
                             1.0e-300))
        T_up = sym(odd_toeplitz(pwc_lags(up, M), M))
        T_el = sym(odd_toeplitz(pwc_lags(ell, M), M))
        maj_ok, maj_dlt, _ = cert_pd(sym(T_up - A_f))
        min_maj_ok, _, _ = cert_pd(sym(A_f - T_el))
        Uz = zz_compress(T_up)
        Ez = zz_compress(T_el)
        Ec = pp_compress(T_el)
        del T_up, T_el
        lam_ez = float(eigvalsh(Ez, subset_by_index=[0, 0])[0])
        lam_ec = float(eigvalsh(Ec, subset_by_index=[0, 0])[0])
        ec_pd = int(cert_pd(Ec)[0])
        q_e = float(y @ (Az @ y)) / max(float(y @ (Ez @ y)), 1.0e-300)
        del Ez, Ec

        # ---- (8R) THE CERTIFIED RUNG BOUND ---------------------------------
        u_pd, u_dlt, fac_U = cert_pd(Uz)
        if not u_pd:
            return None
        w_s = cho_solve(fac_U, s, check_finite=False)
        w_sh = cho_solve(fac_U, shat, check_finite=False)
        cb = float(shat @ w_sh)
        sUs = float(s @ w_s)
        num_expl = float(shat @ w_s)
        r_corr = float(x_c @ (Bx @ w_s)) / max(sUs, 1.0e-300)
        cb_expl = num_expl * num_expl / max(sUs, 1.0e-300)
        # the NORM-ONLY variant: if only ||u_l|| were known and not its
        # direction, Cauchy-Schwarz on the coupling term would give this
        nxc = math.sqrt(float(x_c @ x_c))
        nb1 = max(abs(sUs) - nxc * math.sqrt(float((Bx @ w_s)
                                                   @ (Bx @ w_s))), 0.0)
        nb1 = nb1 * nb1 / max(sUs, 1.0e-300)
        nb2 = max(abs(float(s @ w_sh)) - nxc * math.sqrt(float((Bx @ w_sh)
                                                               @ (Bx @ w_sh))),
                  0.0)
        nb2 = nb2 * nb2 / max(cb, 1.0e-300)
        cos_ss = (float(shat @ s)
                  / max(math.sqrt(float(shat @ shat) * float(s @ s)), 1.0e-300))
        cb_rich = (float(shat @ shat) ** 2) / max(float(shat @ (Uz @ shat)),
                                                  1.0e-300)
        cb_az = (float(shat @ shat) ** 2) / max(float(shat @ (Az @ shat)),
                                                1.0e-300)
        # the same optimal test vector against the EXACT (measured) A_z: how
        # much of the loss is the envelope and how much is the coupling
        fac_az = safe_cho(Az)
        cb_azopt = (float(shat @ cho_solve(fac_az, shat, check_finite=False))
                    if fac_az is not None else float("nan"))
        cell_hi = float(np.max(up[np.abs(np.arange(Lg) * (2.0 * math.pi / Lg)
                                         - math.pi) < math.pi / 2.0]))
        rungs.append(dict(
            al=al, n=z["n"], lev=e, M=M, D=fine["D"], h_c=h_c,
            id_nest_A=id_nest_A, id_nest_b=id_nest_b, id_ysy=id_ysy,
            id_dual=id_dual, id_gal=id_gal, id_yopt=id_yopt, id_lag=id_lag,
            min_ok=min_ok, min_up=min_up, id_min_att=id_min_att,
            delta=delta, eps_c=coarse["eps"], eps_f=fine["eps"],
            cb=cb, cb_expl=cb_expl, cb_rich=cb_rich, cb_az=cb_az,
            cb_azopt=cb_azopt, sUs=sUs, r_corr=r_corr, nb1=nb1, nb2=nb2,
            cos_ss=cos_ss, nxc=nxc,
            ns=float(s @ s), nshat=float(shat @ shat),
            maj_ok=int(maj_ok), min_maj_ok=int(min_maj_ok),
            lam_ez=lam_ez, lam_ec=lam_ec, ec_pd=ec_pd, q_e=q_e,
            marg=marg, scale=scale, Lg=Lg, cell_hi=cell_hi,
            lam_ac=coarse["lam_min"], cond_c=coarse["cond"],
            ac_pd=coarse["pd"]))
        del Ac, Az, Bx, S, Uz, Gm

    tele = sum(r["delta"] for r in rungs)
    zrow = dict(al=al, n=z["n"], MS=MS, mtop=mtop,
                eps=[L["eps"] for L in lv],
                q=[L["q"] for L in lv], D=[L["D"] for L in lv],
                lam=[L["lam_min"] for L in lv],
                cond=[L["cond"] for L in lv],
                osc=[L["osc_frac"] for L in lv],
                canc=[L["cancel"] for L in lv],
                ovu=[L["ov_u"] for L in lv], ovb=[L["ov_b"] for L in lv],
                degen=[L["degen"] for L in lv],
                ss=[lv[e]["selfsim"] for e in range(NLEV - 1)],
                ssk=[lv[e]["selfsim_k"] for e in range(NLEV - 1)],
                rqid=[lv[e]["rq_id"] for e in range(NLEV - 1)],
                rqrat=[lv[e]["rq_rat"] for e in range(NLEV - 1)],
                lev_res=[L["lev_res"] for L in lv],
                lev_q=[L["lev_q"] for L in lv],
                nneg=[L["nneg_piv"] for L in lv],
                head=[float(np.sum(lv[e + 1]["lev_contrib"][:MS[e]]))
                      for e in range(NLEV - 1)],
                tail=[float(np.sum(lv[e + 1]["lev_contrib"][MS[e]:]))
                      for e in range(NLEV - 1)],
                tele=tele, tele_res=abs(tele - (lv[0]["eps"] - lv[-1]["eps"]))
                / max(lv[0]["eps"], 1.0e-300),
                ceil=1.0 - lv[-1]["eps"] / lv[0]["eps"],
                rungs=rungs)
    return zrow


section("Y1  THE TELESCOPE, EXACTLY -- nesting, saturation, level distribution")
print("""  THE LEVEL CHAIN.  alpha is FIXED by the frame; D_l = 2 alpha / M_l with
  M_l = M_0 * 2^l, M_0 in {%s}, l = 0..%d, so D_0 > D_1 > ... > D_L are halvings
  from coarse down to the frame-near resolution (two chain offsets per zone, so
  that D_0 is not collinear with alpha).  Three identities per rung, each stated
  with its status:

    (N)  NESTING / SELF-SIMILARITY  [IDENTITY, verified]
         P^T A^(l+1) P = A^(l),  P^T b^(l+1) = b^(l).
         The piecewise-constant spaces are nested, the window form is ONE
         continuous form restricted to them, and the pole vector is consistent
         because sinh(a-d) + sinh(a+d) = 2 cosh(d) sinh(a) with d = D/4.  So
         the coarse block A_c of the two-level system at D_{l+1} IS the window
         form at D_l -- the object T123 could not bound from below is the same
         object one rung up.

    (T)  THE SATURATION TELESCOPE  [IDENTITY, verified]
         eps_l = eps_{l+1} + delta_l,  delta_l = y_l^T S_l y_l  (T118), hence
             eps_0 = eps_L + sum_{l<L} delta_l.

    (G)  GALERKIN ORTHOGONALITY  [CLASSICAL identity, verified]
         delta_l = || u_{l+1} - P u_l ||^2_{A_{l+1}}  (Cea 1964): the rung is
         the ENERGY OF THE LEVEL CORRECTION.  Nonnegativity of every rung is
         Bessel, not an estimate."""
      % (" / ".join(str(m) for m in MTOPS), NLEV - 1))
print("")

ZROWS = []
for z in ZONES:
    for mtop in MTOPS:
        if budget_left() < 90.0:
            info("Y1.budget", "stopped early at %d chains, %.0f s left"
                 % (len(ZROWS), budget_left()))
            break
        t0 = time.time()
        r = analyse_zone(z, mtop)
        if r is None:
            continue
        ZROWS.append(r)
        info("Y1.chain", "n = %-7d alpha = %.4f  M_0 = %-4d done in %5.1f s  "
             "eps_0 = %.4e -> eps_L = %.4e  ceiling 1 - eps_L/eps_0 = %.6f"
             % (r["n"], r["al"], mtop, time.time() - t0, r["eps"][0],
                r["eps"][-1], r["ceil"]))

RUNGS = [r for zr in ZROWS for r in zr["rungs"]]
print("")
_IDN = max(max(r["id_nest_A"] for r in RUNGS),
           max(r["id_nest_b"] for r in RUNGS))
check("el_y1.nesting", _IDN < 1.0e-9,
      "(N) THE LADDER IS ONE FORM ON NESTED SPACES.  P^T A^(l+1) P = A^(l) and "
      "P^T b^(l+1) = b^(l) to %.1e relative on all %d rungs of %d chains -- so "
      "the two-level system of T122/T123 is literally one rung of this chain, "
      "and 'the coarse form' at rung l is the window form at D_l = 2 D_{l+1}"
      % (_IDN, len(RUNGS), len(ZROWS)))
_IDT = max(r["id_ysy"] for r in RUNGS)
_IDG = max(r["id_gal"] for r in RUNGS)
_IDD = max(r["id_dual"] for r in RUNGS)
_IDY = max(r["id_yopt"] for r in RUNGS)
_CONDMAX = max(r["cond_c"] for r in RUNGS)
check("el_y1.saturation", max(_IDT, _IDG, _IDD) < 1.0e-6,
      "(T) + (G) EVERY RUNG IS A SATURATION IDENTITY.  eps_l - eps_{l+1} = "
      "y^T S y to %.1e, = || u_{l+1} - P u_l ||^2_A to %.1e (Galerkin "
      "orthogonality), = shat^T S^{-1} shat to %.1e (the dual form), and the "
      "maximiser of the dual form is y itself to %.1e relative.  These are "
      "IDENTITIES; the residuals are pure round-off and are floored by the "
      "conditioning of the solves, cond(A_c) <= %.1e, so cond * u = %.1e is "
      "the accuracy that can be asked of them"
      % (_IDT, _IDG, _IDD, _IDY, _CONDMAX, _CONDMAX * U_ROUND))
_TEL = max(zr["tele_res"] for zr in ZROWS)
check("el_y1.telescope", _TEL < 1.0e-6,
      "*** THE TELESCOPE CLOSES EXACTLY. ***  sum_{l<L} delta_l = eps_0 - eps_L "
      "to %.1e relative on all %d chains, over %d rungs each (D halved every "
      "rung), against the fp floor cond * u = %.1e that the level solves "
      "impose.  This is pure linear algebra plus (N): no estimate anywhere"
      % (_TEL, len(ZROWS), NLEV - 1, _CONDMAX * U_ROUND))
_MINOK = all(r["min_ok"] for r in RUNGS)
check("el_y1.direction", _MINOK,
      "DIRECTION CHECK ON THE PRIMAL FORM.  delta = min_x (V x + W y)^T T "
      "(V x + W y) is a MINIMUM: a perturbed coarse component gives a value "
      "ABOVE delta on %d of %d rungs, as it must.  Test vectors in the primal "
      "form are therefore UPPER bounds and can never supply a lower bound -- "
      "this is why T123's routes all had to invert the coarse block"
      % (sum(r["min_ok"] for r in RUNGS), len(RUNGS)))

print("")
print("  THE LEVEL DISTRIBUTION.  delta_l / eps_0 per rung, and the ratio of "
      "consecutive rungs.")
print("")
print("     n       alpha   M_0  eps_0        eps_L        ceiling   "
      + "".join("  d%d/eps0" % e for e in range(NLEV - 1))
      + "   ratios (d_{l+1}/d_l)")
for zr in ZROWS:
    ds = [r["delta"] for r in zr["rungs"]]
    rats = [ds[i + 1] / ds[i] for i in range(len(ds) - 1)]
    print("     %-7d %7.4f %-4d %.4e  %.4e  %.6f  "
          % (zr["n"], zr["al"], zr["mtop"], zr["eps"][0], zr["eps"][-1],
             zr["ceil"])
          + " ".join("%8.5f" % (d / zr["eps"][0]) for d in ds)
          + "   " + " ".join("%.4f" % r for r in rats))
_R1 = [r["delta"] / zr["eps"][0] for zr in ZROWS for r in zr["rungs"][:1]]
_RATS = [zr["rungs"][i + 1]["delta"] / zr["rungs"][i]["delta"]
         for zr in ZROWS for i in range(NLEV - 2)]
_CEIL = [zr["ceil"] for zr in ZROWS]
_GEOM = 2.0 ** (-THETA_T116)
_RMED = float(np.median(_RATS))
_RQ1, _RQ3 = (float(np.quantile(_RATS, 0.25)), float(np.quantile(_RATS, 0.75)))
check("el_y1.geometric", min(_CEIL) > 0.99 and _RQ3 < 0.5,
      "*** THE DISTRIBUTION IS GEOMETRIC ON AVERAGE AND THE CEILING GOES TO 1. "
      "***  The TOP rung alone carries %.4f..%.4f of eps_0; consecutive rungs "
      "fall by a factor whose median is %.4f (quartiles %.4f..%.4f, full range "
      "%.4f..%.4f -- individual rungs at the coarsest, barely resolved "
      "resolutions can rise), against 2^-theta = %.4f from the quoted demand "
      "law eps ~ D^%.2f.  So the rung mass is a geometric series in the level "
      "index up to fluctuations, the tail eps_L/eps_0 = %.2e..%.2e is what the "
      "base case has to absorb, and the L = %d chain has ceiling "
      "1 - eps_L/eps_0 = %.6f..%.6f -- against T123's two-level ceiling "
      "~ alpha^%+.3f"
      % (min(_R1), max(_R1), _RMED, _RQ1, _RQ3, min(_RATS), max(_RATS), _GEOM,
         THETA_T116, min(1.0 - c for c in _CEIL), max(1.0 - c for c in _CEIL),
         NLEV - 1, min(_CEIL), max(_CEIL), PHI_CEIL_T123))
_x1 = [math.log(r["D"]) for r in RUNGS]
_x2 = [math.log(r["al"]) for r in RUNGS]
_dfit = fit_plane(_x1, _x2, [math.log(r["delta"]) for r in RUNGS])
_efit = fit_plane(_x1, _x2, [math.log(r["eps_f"]) for r in RUNGS])
info("Y1.rung_law", "FIT (not certified): delta_l ~ D^%+.3f alpha^%+.3f "
     "(+- %.3f, %.3f; rms %.3f) and eps_l ~ D^%+.3f alpha^%+.3f (+- %.3f, "
     "%.3f) over %d rungs, alpha = %.2f..%.2f, D = %.2e..%.2e.  The rung "
     "exponent tracks the eps exponent, which is what makes the series "
     "geometric; the quoted demand law is D^%.2f alpha^%.2f"
     % (_dfit[1], _dfit[2], _dfit[4], _dfit[5], _dfit[3], _efit[1], _efit[2],
        _efit[4], _efit[5], len(RUNGS), min(r["al"] for r in RUNGS),
        max(r["al"] for r in RUNGS), min(r["D"] for r in RUNGS),
        max(r["D"] for r in RUNGS), THETA_T116, PHI_T116))
info("Y1.timing", "Y1 done, %.1f s used" % (time.time() - T_START))


section("Y2  THE CERTIFIED RUNG CONTRIBUTION, WITHOUT THE COARSE INVERSE")
print("""  THE DERIVATION, IN FIVE LINES.  Let r_l = t_{l+1} - A_{l+1} P u_l be the
  residual of the coarse solution in the fine space.  Galerkin at level l says
  V^T r_l = 0, so r_l = W shat with

      shat = s - B_x^T u_l,      s = W^T t_{l+1}   (EXPLICIT: s_j =
             -(8/sqrt(2D)) * 2 sinh^2(D/4) cosh(xbar^c_j / 2)),

  and the block inverse gives the DUAL form of the rung,

      delta_l = r_l^T A_{l+1}^{-1} r_l = shat^T S^{-1} shat
              = max_v (shat^T v)^2 / (v^T S v).                        (T117-I4)

  This is a MAXIMUM, so every test vector is a LOWER bound and the denominator
  wants S from ABOVE -- the opposite direction to everything T123 tried:

      S = A_z - B_x^T A_c^{-1} B_x <= A_z     needs ONLY  A_c >= 0
                                              (Haynsworth; SEMIDEFINITENESS,
                                              no lam_min, no condition number),
      A_z = W^T T_M(sigma) W <= W^T T_M(up) W =: U    (Parseval + the certified
                                              envelope up >= sigma^(M):
                                              the MIRROR of T123's E_z),
      S <= U,  both PD  =>  U^{-1} <= S^{-1}  (Loewner 1934), hence

      delta_l >= shat^T U^{-1} shat =: cb_l                            (8R)

  and the optimal test vector v = U^{-1} shat is available in CLOSED FORM.  No
  A_c^{-1}, no lam_min(A_c), no CBS constant, no band sweep.  (8R) is CERTIFIED
  given (a) A_c >= 0, (b) U > 0 by completed Cholesky, (c) shat.  Item (c) is
  the only MEASURED input and is split off explicitly below.""")
print("")
_MAJ = all(r["maj_ok"] for r in RUNGS)
_MIN = all(r["min_maj_ok"] for r in RUNGS)
check("el_y2.envelope", _MAJ and _MIN,
      "THE TWO-SIDED CERTIFICATE.  T_M(up) - A_f >= 0 on %d of %d rungs and "
      "A_f - T_M(ell) >= 0 on %d of %d (completed Cholesky at the declared fp "
      "floor), i.e. the certified envelope brackets the window form as an "
      "OPERATOR, not just pointwise; the PWC lag identity holds to %.1e.  "
      "Envelope margin/scale = %s at grid L <= %d"
      % (sum(r["maj_ok"] for r in RUNGS), len(RUNGS),
         sum(r["min_maj_ok"] for r in RUNGS), len(RUNGS),
         max(r["id_lag"] for r in RUNGS),
         rng([r["marg"] / r["scale"] for r in RUNGS], "%.3f"),
         max(r["Lg"] for r in RUNGS)))
_VALID = all(r["cb"] <= r["delta"] * (1.0 + 1.0e-9) for r in RUNGS)
_POS = all(r["cb"] > 0.0 for r in RUNGS)
check("el_y2.cert_valid", _VALID and _POS,
      "*** (8R) IS A VALID LOWER BOUND ON EVERY RUNG. ***  cb_l <= delta_l on "
      "%d of %d rungs and cb_l > 0 on %d of %d.  A_c > 0 is CERTIFIED (Cholesky "
      "at the fp floor) on %d of %d coarse levels, so the only hypothesis (8R) "
      "uses about the coarse block is its SEMIDEFINITENESS -- against T123, "
      "where every route needed lam_min(A_c) = %.1e..%.1e quantitatively"
      % (sum(1 for r in RUNGS if r["cb"] <= r["delta"] * (1.0 + 1.0e-9)),
         len(RUNGS), sum(1 for r in RUNGS if r["cb"] > 0.0), len(RUNGS),
         sum(r["ac_pd"] for r in RUNGS), len(RUNGS),
         min(r["lam_ac"] for r in RUNGS), max(r["lam_ac"] for r in RUNGS)))

print("")
print("  THE RUNG LEDGER.  All ratios to the TRUTH delta_l.  cb = the certified "
      "(8R) bound;\n  cb_expl = the same with the test vector U^{-1} s built "
      "from the EXPLICIT data high-pass;\n  cb_rich = the Richardson vector "
      "v = shat (Kantorovich contrast); cb_azopt = (8R) with the\n  exact A_z "
      "instead of U (isolates the envelope cost from the coupling cost).")
print("")
print("     n       alpha  l  M     delta        cb/delta  cbaz/del  cbrich/d  "
      "cbexpl/d  r_corr    q_e     lam_ec")
for zr in ZROWS:
    for r in zr["rungs"]:
        print("     %-7d %6.3f %d  %-5d %.4e  %8.5f  %8.5f  %8.5f  %8.5f  "
              "%+8.5f  %6.4f  %+.2e"
              % (r["n"], r["al"], r["lev"], r["M"], r["delta"],
                 r["cb"] / r["delta"], r["cb_azopt"] / r["delta"],
                 r["cb_rich"] / r["delta"], r["cb_expl"] / r["delta"],
                 r["r_corr"], r["q_e"], r["lam_ec"]))
_QC = [r["cb"] / r["delta"] for r in RUNGS]
_QA = [r["cb_azopt"] / r["delta"] for r in RUNGS]
_QR = [r["cb_rich"] / r["delta"] for r in RUNGS]
_qfit = fit_plane(_x1, _x2, [math.log(v) for v in _QC])
_UNIF = ("flat to the fit band" if abs(_qfit[2]) < 3.0 * max(_qfit[5], 1.0e-3)
         else "a residual drift of alpha^%+.3f, %.0f times weaker than T123's "
              "alpha^%+.3f" % (_qfit[2], abs(PHI_S6_T123 / min(_qfit[2], -1e-9)),
                               PHI_S6_T123))
check("el_y2.no_rate_loss", min(_QC) > 0.1 and abs(_qfit[2]) < 0.15,
      "*** THE CERTIFIED RUNG BOUND LOSES A CONSTANT, NOT A RATE. ***  "
      "cb_l / delta_l = %.4f..%.4f over %d rungs, FIT D^%+.3f alpha^%+.3f "
      "(+- %.3f, %.3f; rms %.3f) -- %s.  Splitting the loss: with the "
      "exact A_z in the denominator the ratio is %.4f..%.4f (that is the "
      "COUPLING cost, i.e. everything T123's kappa_y measured), so the "
      "ENVELOPE costs only the residual factor %.4f..%.4f, consistent with the "
      "quoted slack q_e = %.4f..%.4f of (5R*).  The Richardson vector by "
      "contrast gives %.2e..%.2e -- the closed-form optimal test vector is "
      "what makes the route work (Kantorovich)"
      % (min(_QC), max(_QC), len(RUNGS), _qfit[1], _qfit[2], _qfit[4],
         _qfit[5], _qfit[3], _UNIF, min(_QA), max(_QA),
         min(_QC[i] / _QA[i] for i in range(len(_QC))),
         max(_QC[i] / _QA[i] for i in range(len(_QC))),
         min(r["q_e"] for r in RUNGS), max(r["q_e"] for r in RUNGS),
         min(_QR), max(_QR)))
_ECN = [r for r in RUNGS if r["lam_ec"] < 0.0]
_EZP = [r for r in RUNGS if r["lam_ez"] > 0.0]
_EXC = sorted({r["M"] for r in RUNGS if r["lam_ec"] >= 0.0
               or r["lam_ez"] <= 0.0})
check("el_y2.t123_contrast", len(_ECN) >= 0.95 * len(RUNGS),
      "THE T123 OBSTRUCTION IS STILL THERE -- AND (8R) STEPS AROUND IT.  "
      "lam_min(E_c) < 0 on %d of %d rungs (%.2e..%.2e), so T123's (7R*) is "
      "uncertifiable at essentially every level of the chain -- only %d rungs "
      "certify E_c > 0 -- while lam_min(E_z) > 0 on %d of %d (%.2e..%.2e), "
      "which is T123's (5R*).  The exceptions live at the smallest resolutions "
      "%s, where the window is barely resolved and the certified envelope is a "
      "large fraction of the form; they are reported, not swept.  (8R) never "
      "forms E_c: it uses the majorant on the OSCILLATION block, where the "
      "envelope works, and only semidefiniteness on the coarse block"
      % (len(_ECN), len(RUNGS), min(r["lam_ec"] for r in RUNGS),
         max(r["lam_ec"] for r in RUNGS), sum(r["ec_pd"] for r in RUNGS),
         len(_EZP), len(RUNGS), min(r["lam_ez"] for r in RUNGS),
         max(r["lam_ez"] for r in RUNGS),
         ("M = " + ", ".join(str(m) for m in _EXC)) if _EXC else "(none)"))

print("")
print("""  WHERE THE COARSE SOLUTION STILL ENTERS, AND THE ACCOUNTING STANDARD.
  cb_l = shat^T U^{-1} shat with shat = s - B_x^T u_l, so the rung bound is an
  explicit finite expression in the CARRIED coarse solution u_l and the known
  lags.  That is exactly the standard T122/T123 certified their own supplies on:
  S2 = (1-gamma^2) LB_y and S6 = (1-gamma^2) y^T E_z y are both functions of the
  carried solution's oscillation component y.  On that standard (8R) is
  certified, and the comparison of exponents below is like-for-like.

  BUT the SOLUTION-FREE version of the rung fails, and it is worth saying
  exactly how.  With w := U^{-1} s the coarse solution enters through ONE
  scalar,
      cb_expl = (shat^T w)^2 / (s^T w) = (1 - r_corr)^2 * (s^T U^{-1} s),
      r_corr  = u_l^T (B_x w) / (s^T U^{-1} s),
  and s^T U^{-1} s IS fully explicit (the pole vector's high-pass part against
  the certified majorant, no solution anywhere).  If r_corr were a small
  perturbation, the rung would be explicit up to a constant.  It is not.""")
print("")
print("     n       alpha  l  ||shat||^2/||s||^2  cos(shat,s)  sUs/delta      "
      "r_corr     cb_expl/d  normonly1  normonly2")
for zr in ZROWS:
    for r in zr["rungs"]:
        print("     %-7d %6.3f %d  %18.6e  %+11.6f  %.6e  %+9.5f  %9.5f  "
              "%9.3e  %9.3e"
              % (r["n"], r["al"], r["lev"], r["nshat"] / r["ns"], r["cos_ss"],
                 r["sUs"] / r["delta"], r["r_corr"], r["cb_expl"] / r["delta"],
                 r["nb1"] / r["delta"], r["nb2"] / r["delta"]))
_RC = [abs(r["r_corr"]) for r in RUNGS]
_SUS = [r["sUs"] / r["delta"] for r in RUNGS]
_SHR = [r["nshat"] / r["ns"] for r in RUNGS]
_NB = [max(r["nb1"], r["nb2"]) / r["delta"] for r in RUNGS]
check("el_y2.residual_is_cancellation", max(_NB) < 1.0e-3,
      "*** (F5) IS NOT A PERTURBATION: THE RUNG NUMERATOR IS A CANCELLATION. "
      "***  |r_corr| = %.4f..%.4f -- i.e. the coupling term does not perturb "
      "the explicit high-pass, it CANCELS it, and what survives is the rung.  "
      "What survives is ||shat||^2/||s||^2 = %.2e..%.2e -- BELOW 1 at small alpha "
      "and ABOVE it at large alpha, so not a fraction at all -- and the fully "
      "explicit s^T U^{-1} s sits at %.2e..%.2e times delta (far too small at "
      "small alpha, far too large at large alpha -- both useless).  A "
      "NORM-ONLY bound on the coarse solution is therefore hopeless: replacing "
      "u_l^T (B_x w) by ||u_l|| ||B_x w|| (Cauchy-Schwarz) kills the bound "
      "completely, %.1e..%.1e of delta on every rung.  So (F5) is a FLOOR ON "
      "THE DIRECTION of the coarse residual, of the same depth as the rung "
      "itself -- not a size estimate"
      % (min(_RC), max(_RC), min(_SHR), max(_SHR), min(_SUS), max(_SUS),
         min(_NB), max(_NB)))
_rcfit = fit_plane(_x1, _x2, [math.log(max(v, 1.0e-300)) for v in _RC])
_shfit = fit_plane(_x1, _x2, [math.log(v) for v in _SHR])
info("Y2.f5_law", "FITS (not certified): |r_corr| ~ D^%+.3f alpha^%+.3f "
     "(+- %.3f, %.3f) and ||shat||^2/||s||^2 ~ D^%+.3f alpha^%+.3f "
     "(+- %.3f, %.3f).  Read as the chain's own accounting: shat is a function "
     "of the carried solution exactly as y was in T122/T123, so (8R) is "
     "certified on the T123 standard; a SOLUTION-FREE rung would need this "
     "cancellation resolved, which is (F5)"
     % (_rcfit[1], _rcfit[2], _rcfit[4], _rcfit[5], _shfit[1], _shfit[2],
        _shfit[4], _shfit[5]))

print("")
print("""  (iii) THE LEVINSON LEDGER.  q_l = sum_n rho_n^2 / E_n exactly (T119 mass
  budget; Levinson 1947 / Durbin 1960 on the FULL Toeplitz system with the odd
  extension tau of the pole vector, B^T tau = t~).  So

      delta_l = sum_{n < M_{l+1}} (rho^2/E)^(l+1) - sum_{n < M_l} (rho^2/E)^(l).

  THE BORDERING HYPOTHESIS to test: is the coarse sum the HEAD of the fine sum,
  i.e. does the rung equal the TAIL sum_{n >= M_l} (rho^2/E)^(l+1)?  That would
  be true if refinement were a bordering -- it is not, because halving D changes
  EVERY lag.  The two filtrations (section order n at fixed D, refinement of D
  at fixed window) are transverse, and the numbers say by how much.""")
print("")
print("     n       alpha  l  head/q_l    tail/delta   (head+tail)/q_{l+1}  "
      "mass-budget res   #neg pivots")
for zr in ZROWS:
    for e in range(NLEV - 1):
        hd, tl = zr["head"][e], zr["tail"][e]
        print("     %-7d %6.3f %d  %10.5f  %10.5f  %18.12f  %.3e         %d"
              % (zr["n"], zr["al"], e, hd / zr["q"][e],
                 tl / zr["rungs"][e]["delta"], (hd + tl) / zr["q"][e + 1],
                 zr["lev_res"][e + 1], zr["nneg"][e + 1]))
_LR = max(max(zr["lev_res"]) for zr in ZROWS)
check("el_y2.mass_budget", _LR < 1.0e-8,
      "THE INNOVATION LEDGER IS EXACT AT EVERY LEVEL.  q_l = sum_n rho_n^2/E_n "
      "to %.1e relative on all %d levels of all %d chains, with %d..%d NEGATIVE "
      "pivots (the even sector's DC direction) -- an exact indefinite LDL^T, "
      "Delsarte-Genin split-Levinson in disguise"
      % (_LR, NLEV, len(ZROWS), min(min(zr["nneg"]) for zr in ZROWS),
         max(max(zr["nneg"]) for zr in ZROWS)))
_HD = [zr["head"][e] / zr["q"][e] for zr in ZROWS for e in range(NLEV - 1)]
_TL = [zr["tail"][e] / zr["rungs"][e]["delta"]
       for zr in ZROWS for e in range(NLEV - 1)]
check("el_y2.bordering", min(_TL) > 0.0,
      "REFINEMENT IS NOT A BORDERING -- MEASURED.  The head of the fine "
      "innovation sum is %.4f..%.4f of q_l (it would be exactly 1 if the "
      "coarse system were a leading section of the fine one) and the tail is "
      "%.4f..%.4f of the rung.  So the Levinson ledger is an exact ledger for "
      "each q_l separately but does NOT split the rung: the section filtration "
      "and the refinement filtration are transverse, and the rung has to be "
      "read in the (8R) form, not in innovations"
      % (min(_HD), max(_HD), min(_TL), max(_TL)))
info("Y2.timing", "Y2 done, %.1f s used" % (time.time() - T_START))


section("Y3  THE CANCELLATION STRUCTURE AND THE SELF-SIMILARITY OF THE LADDER")
print("""  T123's obstruction, restated: the near-null direction of the window form is
  SMOOTH, so it lives in the coarse space, and its eigenvalue comes from a
  cancellation INSIDE the form that no pointwise symbol minorant can see.  Here
  the same eigenvector is followed ALONG the ladder.  If

      w_l  (the near-null direction of A^(l))  ~  P^T w_{l+1},

  then by (N) the coarse form of rung l is the window form of rung l-1 and the
  obstruction is the SAME object at every level -- which is exactly what makes a
  coarse-to-fine induction possible: at rung l the hypothesis 'A_c >= 0' IS the
  conclusion of rung l-1, already carried by the chain.""")
print("")
print("     n       alpha  l  M     lam_min      cond       osc frac   "
      "cancel     lam_1/lam_0  |<Pw,w'>|  ||Q_K^T Pw||  lam_l/lam_{l+1}")
for zr in ZROWS:
    for e in range(NLEV):
        tail = (("%11.6f  %11.6f  %15.4f"
                 % (zr["ss"][e], zr["ssk"][e], zr["rqrat"][e]))
                if e < NLEV - 1 else "")
        print("     %-7d %6.3f %d  %-5d %+.4e  %.3e  %.3e  %.3e  %11.4f  %s"
              % (zr["n"], zr["al"], e, zr["MS"][e], zr["lam"][e],
                 zr["cond"][e], zr["osc"][e], zr["canc"][e], zr["degen"][e],
                 tail))
_OSC = [v for zr in ZROWS for v in zr["osc"]]
_SS = [v for zr in ZROWS for v in zr["ss"]]
_SSK = [v for zr in ZROWS for v in zr["ssk"]]
_RQI = max(v for zr in ZROWS for v in zr["rqid"])
_RQR = [v for zr in ZROWS for v in zr["rqrat"]]
_DEG = [v for zr in ZROWS for v in zr["degen"]]
_CN = [v for zr in ZROWS for v in zr["canc"]]
check("el_y3.smooth_and_selfsimilar", max(_OSC) < 0.5 and min(_SSK) > 0.9
      and _RQI < 1.0e-12,
      "*** THE NEAR-NULL DIRECTION IS SMOOTH AND SELF-SIMILAR ALONG THE "
      "LADDER. ***  Its oscillation fraction ||Z^T w||^2/||w||^2 = %.3e..%.3e "
      "(it lives in the coarse space, T123) and its Rayleigh quotient is a "
      "cancellation of depth w^T A w / (|w|^T |A| |w|) = %.2e..%.2e, i.e. "
      "%.1f..%.1f orders of cancellation INSIDE the form -- unchanged from "
      "T123, and unchanged at EVERY level.  SELF-SIMILARITY, three readings: "
      "the IDENTITY (P w_l)^T A^(l+1) (P w_l) = lam_min(A^(l)) holds to %.1e "
      "in units of ||A|| (it is nesting, not a measurement), the ratio "
      "lam_min(A^(l)) / "
      "lam_min(A^(l+1)) = %.2f..%.2f (so the prolonged coarse near-null "
      "direction stays near-null at the finer level, up to a BOUNDED factor "
      "~2^theta), the raw eigenvector overlap |<P w_l, w_{l+1}>| = %.4f..%.4f "
      "-- fragile where the two lowest eigenvalues nearly cross "
      "(lam_1/lam_0 = %.2f..%.2f) -- and the degeneracy-robust subspace "
      "overlap ||Q_K^T P w_l|| = %.4f..%.4f with K = %d"
      % (min(_OSC), max(_OSC), min(_CN), max(_CN),
         -math.log10(max(max(_CN), 1.0e-300)),
         -math.log10(max(min(_CN), 1.0e-300)), _RQI, min(_RQR), max(_RQR),
         min(_SS), max(_SS), min(_DEG), max(_DEG), min(_SSK), max(_SSK),
         N_LOW))
_lamfit = fit_plane([math.log(zr["D"][e]) for zr in ZROWS for e in range(NLEV)],
                    [math.log(zr["al"]) for zr in ZROWS for e in range(NLEV)],
                    [math.log(zr["lam"][e]) for zr in ZROWS
                     for e in range(NLEV)])
_PDALL = all(r["ac_pd"] for r in RUNGS)
check("el_y3.recursion_closes", _PDALL,
      "*** THE RECURSION CLOSES IN THE RIGHT DIRECTION. ***  By (N) the coarse "
      "block of rung l IS the window form at D_l, so the hypothesis (8R) needs "
      "-- A_c >= 0 -- is the POSITIVITY OF THE PREVIOUS LEVEL, i.e. the "
      "conclusion a coarse-to-fine induction already has in hand.  Certified "
      "(completed Cholesky at the fp floor) on %d of %d coarse levels; "
      "lam_min(A^(l)) = %.2e..%.2e, FIT D^%+.3f alpha^%+.3f (+- %.3f, %.3f).  "
      "NOTE THE DIRECTION: positivity also propagates fine -> coarse for free "
      "(A_c = P^T A_f P is a restriction), so a fine-level hypothesis would be "
      "circular; the induction that is NOT circular runs coarse -> fine, and "
      "that is the direction the ladder is refined in"
      % (sum(r["ac_pd"] for r in RUNGS), len(RUNGS),
         min(v for zr in ZROWS for v in zr["lam"]),
         max(v for zr in ZROWS for v in zr["lam"]),
         _lamfit[1], _lamfit[2], _lamfit[4], _lamfit[5]))
_ENVR = [abs(r["scale"]) / max(r["lam_ac"], 1.0e-300) for r in RUNGS]
info("Y3.envelope_gap", "THE MARGIN IS STILL HOPELESS FOR A DIRECT MINORANT, "
     "AS IN T123: the certified envelope margin is %s times lam_min(A_c), so "
     "no pointwise symbol bound will ever see the coarse eigenvalue.  (8R) "
     "does not ask it to -- it asks only for the SIGN, and the sign is what "
     "the induction carries"
     % rng([r["marg"] / max(r["lam_ac"], 1.0e-300) for r in RUNGS], "%.1e"))
info("Y3.timing", "Y3 done, %.1f s used" % (time.time() - T_START))


section("Y4  THEOREM V8, THE NEW CERTIFIED BALANCE, AND THE DEFECT COUNTER")
print("""  THEOREM V8 (the multigrid form of the statement).  Fix a zone and a frame.
  Let D_0 > ... > D_L be halvings, A^(l) the odd window form at D_l, b^(l) the
  odd pole vector, eps_l = 1 - b^(l)T A^(l)-1 b^(l).  Then

    (V8.1) [IDENTITY]  P^T A^(l+1) P = A^(l), P^T b^(l+1) = b^(l), and
           eps_0 = eps_L + sum_{l<L} delta_l with delta_l = the energy of the
           level correction (Galerkin orthogonality).
    (V8.2) [IDENTITY]  delta_l = shat_l^T S_l^{-1} shat_l, a MAXIMUM over test
           vectors, with shat_l = s_l - B_x^T u_l and s_l explicit.
    (V8.3) [CERTIFIED, given A^(l) >= 0]  delta_l >= shat_l^T U_l^{-1} shat_l
           with U_l = Z^T T_M(up) Z the certified majorant compression.
    (V8.4) [the chain]  eps_0 >= sum_{l<L} cb_l, ceiling 1 - eps_L/eps_0 -> 1,
           and the base case is eps_L >= 0 -- SEMIDEFINITENESS, not a rate.

  THE BALANCE.  Two readings, because two different objects are being supplied:
  the TWO-LEVEL reading (comparable to T123: one rung against its own eps_c)
  and the TELESCOPE reading (the whole chain against eps_0).""")
print("")
print("     n       alpha  cb_tot/eps_0  ceiling   top cb/eps_c  "
      "finest cb/eps_c   sum delta/eps_0")
for zr in ZROWS:
    cbt = sum(r["cb"] for r in zr["rungs"])
    r0, rL = zr["rungs"][0], zr["rungs"][-1]
    print("     %-7d %6.3f  %12.6f  %.6f  %12.5f  %15.5f  %15.6f"
          % (zr["n"], zr["al"], cbt / zr["eps"][0], zr["ceil"],
             r0["cb"] / r0["eps_c"], rL["cb"] / rL["eps_c"],
             zr["tele"] / zr["eps"][0]))
_CBT = [sum(r["cb"] for r in zr["rungs"]) / zr["eps"][0] for zr in ZROWS]
_cbfit = fit_plane([math.log(zr["D"][0]) for zr in ZROWS],
                   [math.log(zr["al"]) for zr in ZROWS],
                   [math.log(v) for v in _CBT])
_pairfit = fit_plane(_x1, _x2, [math.log(r["cb"] / r["eps_c"]) for r in RUNGS])
check("el_y4.balance", min(_CBT) > 0.5 and abs(_cbfit[2]) < 0.15,
      "*** THE NEW CERTIFIED BALANCE. ***  TELESCOPE reading: sum_l cb_l / "
      "eps_0 = %.4f..%.4f against the ceiling %.6f..%.6f, FIT D^%+.3f "
      "alpha^%+.3f (+- %.3f, %.3f) over alpha = %.2f..%.2f and %d chains.  "
      "TWO-LEVEL reading, directly comparable to T123's S6/eps_c ~ D^%+.3f "
      "alpha^%+.3f: cb/eps_c ~ D^%+.3f alpha^%+.3f (+- %.3f, %.3f) -- the "
      "alpha exponent moves by %+.3f, against T123's gap alpha^%+.3f to the "
      "ceiling"
      % (min(_CBT), max(_CBT), min(_CEIL), max(_CEIL), _cbfit[1], _cbfit[2],
         _cbfit[4], _cbfit[5], min(zr["al"] for zr in ZROWS),
         max(zr["al"] for zr in ZROWS), len(ZROWS),
         THETA_S6_T123, PHI_S6_T123, _pairfit[1], _pairfit[2], _pairfit[4],
         _pairfit[5], _pairfit[2] - PHI_S6_T123, PHI_GAP_T123))

DEFECTS = [
    ("(F1) corner sign", "OPEN, untouched",
     "the Harnack pair, unchanged since T120; nothing here touches it"),
    ("(F2) uniform delta", "OPEN, untouched",
     "the Harnack pair, unchanged since T120; nothing here touches it"),
    ("(F3) band margin", "CLOSED in T123",
     "lam_min(E_z) > 0 uniform, reduction cost < 1 %; (8R) re-uses the same "
     "envelope on the same block, in the MIRROR direction (up instead of ell)"),
    ("(F4) coarse positivity, QUANTITATIVE", "COLLAPSED to its sign",
     "(8R) needs A_c >= 0 only.  By (N) that is the previous rung's own "
     "positivity, so a coarse-to-fine induction supplies it; lam_min(A_c), "
     "cond(A_c) and the CBS constant gamma^2 leave the chain entirely"),
    ("(F4b) base case", "REDUCED to eps_L >= 0",
     "the telescope's tail eps_L/eps_0 = %.1e..%.1e at L = %d, so the base "
     "case is SEMIDEFINITENESS (Bessel for the finest level), not a rate"
     % (min(1.0 - c for c in _CEIL), max(1.0 - c for c in _CEIL), NLEV - 1)),
    ("(F5) the residual direction", "NEW; only for a SOLUTION-FREE rung",
     "(8R) is certified on the T123 accounting standard (shat is a function of "
     "the carried solution, exactly as y was in S2/S6).  A solution-FREE rung "
     "would need a floor on shat = s - B_x^T u_l, and that is a cancellation, "
     "not a perturbation: |r_corr| = %.4f..%.4f, "
     "||shat||^2/||s||^2 = %.1e..%.1e, and a norm-only Cauchy-Schwarz bound "
     "gives %.1e..%.1e of the rung"
     % (min(_RC), max(_RC), min(_SHR), max(_SHR), min(_NB), max(_NB))),
]
N_DEF = len(DEFECTS)
print("")
print("  THE DEFECT COUNTER (T123 had 4: F1, F2, F3 closed, F4 open).")
print("")
for nm, st, tx in DEFECTS:
    print("     %-38s %-26s %s" % (nm, st, tx))
_F4_COLLAPSE = _VALID and _POS and min(_QC) > 0.1 and _PDALL
check("el_y4.defects", _F4_COLLAPSE,
      "%d entries, but the SHAPE changed: (F4) is no longer an estimate to be "
      "found, it is a SIGN supplied by the induction, and what is left of the "
      "coupling is one scalar (F5).  The classical CBS constant gamma^2 and "
      "the whole band sweep for kappa_y are GONE from the chain"
      % N_DEF)

print("")
print("""  HONEST PAPER ASSESSMENT.
  * (V8.1) and (V8.2) are two-line lemmas: nesting of piecewise-constant spaces
    plus a hyperbolic addition formula, and the standard block-inverse identity.
    Both are verified here to round-off.  They are writeable as they stand.
  * (V8.3) is the real content and it is SHORT: Haynsworth monotonicity of the
    Schur complement (needs only A_c >= 0), Parseval against the certified
    envelope (T122/T123 machinery, unchanged), and Loewner antitony of the
    inverse.  Three classical steps, no new analysis.
  * What a referee will stop at, in order: (i) the coarse-to-fine induction has
    to be set up so that A^(l) >= 0 is genuinely available at rung l -- note
    positivity propagates fine -> coarse for FREE, so the induction must run the
    other way and its base case is the coarsest level, where h is small;
    (ii) (F5): the rung numerator is a function of the carried coarse solution
    -- legitimate on the T123 accounting standard, but a solution-free rung
    would need a floor on a CANCELLATION, and a norm-only bound provably does
    not give one (measured to be worthless above);  (iii) the
    L-dependence: the ceiling needs eps_L/eps_0 small, which is the demand law
    itself, so L enters logarithmically.
  * What this does NOT do: it does not touch (F1)/(F2), it does not prove the
    positivity of the window form, and it is not a proof of the demand law.  It
    replaces one unreachable quantitative estimate by a sign plus one scalar.""")


# ----------------------------------------------------------------------------
section("FENCES")
# ----------------------------------------------------------------------------
_HMAX = max(MS_ALL) // 2
FENCE = [
    ("largest FACTORISED / INVERTED / DIAGONALISED form h = %d <= %d"
     % (_HMAX, MAX_H), _HMAX <= MAX_H),
    ("largest matrix-free FFT grid L = %d (no matrix of that size formed)"
     % max(r["Lg"] for r in RUNGS), True),
    ("no zero data, no zero-derived quantity anywhere (AST firewall above)",
     True),
    ("RH => window Weil positivity NOT used; every statement is about a GIVEN "
     "window at a GIVEN resolution", True),
    ("every bound states its direction, and (8R) is used ONLY as a lower bound "
     "coming from a MAXIMUM principle", True),
    ("no promotion, no ledger / TeX / website / changelog / next.txt edit, no "
     "verification module, no .md output", True),
    ("probe budget: %.1f s used of %.0f s" % (time.time() - T_START, BUDGET_S),
     time.time() - T_START < BUDGET_S),
]
for tx, ok in FENCE:
    check("el_fence." + tx.split()[0].lower().strip(",")[:14], ok, tx)

print("")
print("  THE LINE BETWEEN CERTIFIED AND MEASURED, ITEM BY ITEM.")
print("    IDENTITIES (verified to round-off): the nesting P^T A^(l+1) P = "
      "A^(l) and P^T b^(l+1) = b^(l); the saturation telescope; Galerkin "
      "orthogonality; the dual residual form of the rung; the Levinson "
      "innovation ledger q = sum rho^2/E; the PWC lag formula.")
print("    CERTIFIED (algebra + completed Cholesky at the declared fp floor): "
      "T_M(ell) <= A_f <= T_M(up) as OPERATORS; U = Z^T T_M(up) Z > 0; "
      "A^(l) > 0 at every level of the chain; and therefore (8R) "
      "delta_l >= shat^T U^{-1} shat, GIVEN shat.")
print("    CLASSICAL, WITH DIRECTION: Parseval (both), Haynsworth "
      "(S <= A_z, UPPER, from A_c >= 0), Loewner (inverse antitony, turns the "
      "UPPER bound on S into a LOWER bound on the rung), Cea / Bessel "
      "(delta_l >= 0), Kantorovich (the Richardson contrast, quoted), "
      "Levinson-Durbin-Delsarte-Genin (the ledger), Yserentant / BPX / "
      "Axelsson-Vassilevski (the telescope's provenance; gamma^2 is an UPPER "
      "worst case and is NOT used).")
print("    MEASURED (never a certificate): every lam_min and cond from eigh, "
      "shat and hence cb_l, r_corr, the head/tail split of the Levinson sums, "
      "and all ratios to delta_l.")
print("    FITS (with jackknife bands, never a bound): the rung law, the "
      "cb/delta drift, the |r_corr| law, lam_min(A^(l)) and the balance.")


# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
_TELE_OK = _TEL < 1.0e-6 and _IDN < 1.0e-9 and max(_IDT, _IDG, _IDD) < 1.0e-6
_CARRIES = (_TELE_OK and _F4_COLLAPSE and min(_CBT) > 0.5
            and abs(_cbfit[2]) < 0.15)
if _CARRIES:
    VERDICT = "TELESCOPE-CARRIES"
elif _TELE_OK and _LR < 1.0e-8:
    VERDICT = "LEVINSON-LEDGER"
else:
    VERDICT = "TELESCOPE-STALLS"
print("")
print("  Y1  THE TELESCOPE IS EXACT AND GEOMETRIC.  The ladder is ONE window "
      "form on NESTED spaces\n      (P^T A^(l+1) P = A^(l) to %.1e), every rung "
      "is the T118 saturation identity and the\n      Galerkin energy of the "
      "level correction (%.1e), and sum_l delta_l = eps_0 - eps_L to %.1e.\n"
      "      The rung mass is geometric on average: the top rung carries "
      "%.4f..%.4f of eps_0,\n      consecutive rungs fall by a median factor "
      "%.4f (quartiles %.3f..%.3f; 2^-theta = %.3f\n      from the demand "
      "law), so at L = %d the tail is eps_L/eps_0 = %.1e..%.1e and the "
      "ceiling\n      is %.6f..%.6f -- against T123's two-level ceiling "
      "alpha^%+.3f.  Rung law (FIT)\n      delta ~ D^%+.3f alpha^%+.3f."
      % (_IDN, _IDG, _TEL, min(_R1), max(_R1), _RMED, _RQ1, _RQ3, _GEOM,
         NLEV - 1, min(1.0 - c for c in _CEIL), max(1.0 - c for c in _CEIL),
         min(_CEIL), max(_CEIL), PHI_CEIL_T123, _dfit[1], _dfit[2]))
print("  Y2  THE RUNG IS CERTIFIABLE FROM ABOVE, WHICH IS THE POINT.  The rung "
      "is a MAXIMUM over\n      test vectors (dual residual form), so its "
      "denominator wants S from ABOVE: S <= A_z needs\n      only A_c >= 0 "
      "(Haynsworth), A_z <= U = Z^T T_M(up) Z is Parseval against the certified\n"
      "      majorant, and Loewner turns that into (8R) delta >= shat^T U^{-1} "
      "shat with the optimal\n      test vector in closed form.  VALID on %d of "
      "%d rungs, and it loses a CONSTANT plus a drift\n      %d times weaker "
      "than T123's, not a rate: cb/delta = "
      "%.4f..%.4f, FIT alpha^%+.3f +- %.3f.  Of that loss\n      the coupling "
      "is %.4f..%.4f and the envelope only %.4f..%.4f.  T123's obstruction "
      "is\n      untouched and irrelevant: lam_min(E_c) < 0 on %d of %d rungs, "
      "(8R) never forms E_c.  The\n      Levinson ledger is exact per level "
      "(%.1e) but does NOT split the rung -- refinement is not a bordering\n"
      "      (head/q_l = %.4f..%.4f), so the rung must be read in the (8R) "
      "form."
      % (sum(1 for r in RUNGS if r["cb"] <= r["delta"] * (1.0 + 1.0e-9)),
         len(RUNGS), round(abs(PHI_S6_T123 / min(_qfit[2], -1.0e-9))),
         min(_QC), max(_QC), _qfit[2], _qfit[5], min(_QA),
         max(_QA), min(_QC[i] / _QA[i] for i in range(len(_QC))),
         max(_QC[i] / _QA[i] for i in range(len(_QC))), len(_ECN), len(RUNGS),
         _LR, min(_HD), max(_HD)))
print("  Y3  SELF-SIMILARITY, AND WHY THE RECURSION CLOSES.  The near-null "
      "direction stays SMOOTH\n      (oscillation fraction %.1e..%.1e) and "
      "self-similar along the ladder: prolonged, it has\n      Rayleigh "
      "quotient exactly lam_min(A^(l)) at the next level (an IDENTITY, from "
      "nesting),\n      i.e. within a bounded factor %.2f..%.2f of that "
      "level's own minimum, and its subspace\n      overlap is "
      "||Q_K^T P w_l|| = %.4f..%.4f.  Its Rayleigh quotient is a cancellation "
      "of depth\n      %.1e..%.1e inside the "
      "form, and the certified envelope margin is %s times lam_min(A_c) "
      "-- exactly T123's\n      diagnosis, at every level.  But (8R) asks only "
      "for the SIGN of A_c, and by the nesting\n      identity that sign is the "
      "previous rung's conclusion: the induction runs COARSE -> FINE\n      "
      "and closes.  (Positivity propagates fine -> coarse for free, so the "
      "opposite direction\n      would be circular -- stated explicitly.)"
      % (min(_OSC), max(_OSC), min(_RQR), max(_RQR), min(_SSK), max(_SSK),
         min(_CN), max(_CN),
         rng([r["marg"] / max(r["lam_ac"], 1.0e-300) for r in RUNGS], "%.1e")))
print("  Y4  THE BALANCE AND THE DEFECT COUNTER.  Telescope reading sum_l cb_l "
      "/ eps_0 = %.4f..%.4f\n      against the ceiling %.6f..%.6f, FIT "
      "alpha^%+.3f +- %.3f; two-level reading cb/eps_c ~\n      D^%+.3f "
      "alpha^%+.3f, against T123's certified D^%+.3f alpha^%+.3f -- the alpha "
      "exponent\n      moves by %+.3f, i.e. %s of the T123 gap alpha^%+.3f.  "
      "%d defect entries: (F1), (F2)\n      untouched, (F3) closed, (F4) "
      "COLLAPSED from a quantitative estimate to a sign, and one new one\n"
      "      (F5) that bites only if the rung must be SOLUTION-FREE: the "
      "residual is a cancellation\n      (|r_corr| = %.4f..%.4f), not a "
      "perturbation."
      % (min(_CBT), max(_CBT), min(_CEIL), max(_CEIL), _cbfit[2], _cbfit[5],
         _pairfit[1], _pairfit[2], THETA_S6_T123, PHI_S6_T123,
         _pairfit[2] - PHI_S6_T123,
         "most" if abs(_pairfit[2]) < 0.5 * abs(PHI_S6_T123) else "part",
         PHI_GAP_T123, N_DEF, min(_RC), max(_RC)))
print("")
print("  WHAT THIS PART BUYS, IN ONE PARAGRAPH.  T123 proved that no route to "
      "the CBS constant\n  survives without the coarse form from below, and "
      "left the recursion as the only exit.\n  This part builds it and finds "
      "that the exit is not the recursion's LENGTH but its\n  DIRECTION.  "
      "Written as a telescope, the quantity to be supplied at each rung is not "
      "a\n  Rayleigh quotient (a minimum, needing the form from below) but a "
      "residual in the inverse\n  norm (a maximum, needing the form from "
      "above) -- and from above, the certified envelope\n  works, because "
      "Parseval is two-sided.  The coarse block then appears only through\n  "
      "Haynsworth monotonicity, i.e. through its SIGN, and by the nesting "
      "identity that sign is\n  what the previous rung already proved.  The "
      "chain becomes additive with ceiling %.4f at\n  L = %d levels, the "
      "certified rung loses a constant %.3f..%.3f rather than a power of "
      "alpha,\n  and the CBS constant leaves the chain.  What is left of the "
      "coupling is a single scalar,\n  the coarse solution tested against an "
      "explicit vector -- and that scalar is a cancellation\n  (%.4f..%.4f of "
      "the explicit part), so it is a floor on a DIRECTION, not a size "
      "estimate.\n  The Harnack pair (F1), (F2) is untouched."
      % (min(_CEIL), NLEV - 1, min(_QC), max(_QC), min(_RC), max(_RC)))
print("")
print("TOTAL.checks   %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.verdict  %s" % VERDICT)
print("TOTAL.runtime  %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                 BUDGET_S))
