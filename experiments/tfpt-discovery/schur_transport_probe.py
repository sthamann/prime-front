"""Discovery probe (2026-07-27), part 115 of the zeta/prime investigation.
Contract SCHUR.TRANSPORT -- the two last bricks of the margin-free programme:
(A) TRANSPORT the exact Schur complement between the NON-NESTED grids of the
frame-A ladder, and (B) break the COMPUTATIONAL cap by multi-resolution
compression of the already-certified interior.

WHERE THIS SITS (T105..T114, taken as given, rebuilt here)
  T114 (WALL-DISSOLVES) removed the margin from the induction step and walked
  the ladder past the old wall.  Its findings are the starting position:
    * THE STEP IS MARGIN-FREE.  Albert 1969 (generalised Schur with the
      Moore-Penrose inverse): [[A, C], [C^T, X]] >= 0  <=>  X >= 0,
      ran(C^T) subset ran(X), A - C X^+ C^T >= 0.  27/27 ladder steps certify,
      11 of them past the old wall (to n = 1331), all 7 T109 tear zones.
    * THE OBJECT WITH SUBSTANCE IS THE EXACT SCHUR COMPLEMENT.  The 4 x 4
      S = A - C X^{-1} C^T has lam_min(S) = 0.068..0.154, i.e. 42..67 % of the
      block scale, NO cancellation -- while ANY norm bound on the same object
      divides ||C||^2 by lam_min(X) ~ 1e-6 and lands 1e5..1e8 negative.
    * THE CHAIN NEVER DIES OF STRUCTURE, ONLY OF COST.  Fixed-grid runs always
      end at the hard cap h <= 1500 (window cost h ~ nu u / g_min), never at a
      step; longest run 4 steps.
    * THE REGRID IS THE RESIDUE.  0/464 consecutive gap ratios g_k/g_k+1 are
      dyadic (median 1.996, max 13.93), so no common refinement exists, and
      positivity must be transported between NON-NESTED grids.  T114 sharpened
      the target twice: [P5] the (R) demand is grid-attached and must be
      dropped, and what has to survive the regrid is NOT eps and NOT the floor
      (both ~ D^1.8) but the O(0.1) exact Schur complement.
    * [P1] is now 'eps > 0 with a controlled SIZE relative to kappa', localised
      in the rank-one pole term (T113: the interior atom perturbs 1e7 times
      more than the boundary atom).

WHAT THIS PROBE DOES
  M1  THE TRANSPORT.  The discretisation is made explicit first: the basis is
      the L2-NORMALISED PIECEWISE-CONSTANT cell family phi_r = 1_cell/sqrt(D)
      (the triangle in the kernel is the autocorrelation of the cell, and the
      pole vector's 1/sqrt(D) is the same normalisation), so the exact transfer
      operator between two grids is the CELL-OVERLAP matrix
          P[i,j] = <phi^f_i, phi^c_j>,  R = P^T,
      and two PWC grids are NESTED iff the ratio is an INTEGER with aligned
      windows -- NOT iff it is dyadic.  Both counts are measured on the table.
      For nested pairs the GALERKIN IDENTITY Q_c = P^T Q_f P is exact and is
      verified to machine precision (it validates the whole assembly).  For the
      REAL regrid pairs the probe builds a two-sided TRANSPORT BRACKET for
      lam_min(S) from the Schur complement's variational form (partial
      minimisation, Haynsworth 1968)
          y^T S y = min_z [y;z]^T Q' [y;z],
      i.e. NO inverse and no margin:
          lam_min(S_c) * tau_dn - |eta_dn|  <=  lam_min(S_f)
                                           <=  (lam_min(S_c) + |eta_up|)/tau_up
      with tau = transported y-norms and eta = the form-consistency defects
      evaluated at the actual minimisers.  Measured against (a) the a-priori
      norm surrogate of the same eta (Cea/Strang-type, which is where the
      margin division would come back), (b) the kernel-smoothness ingredients
      (arch-kernel Lipschitz constant on the boundary window, exact atom
      bookkeeping, pole smoothness), and (c) lam_min(S) itself: does the bound
      leave room?
  M2  MULTI-RESOLUTION.  The mixed window: fine cells at the boundary, MERGED
      cells (block averages, an exactly nested PWC coarsening) in the already
      certified interior, the merge anchored at the CENTRE so that the graded
      space is stable under window growth.  Then X_mixed = Q_old,mixed EXACTLY
      still holds (the incoming atom block is the exact zero matrix in any basis
      supported in the old window), so the margin-free step survives compression
      verbatim.  Three questions: does Albert still certify, how much h does the
      compression save, and is the compression error certifiable?  It is, and
      one-sidedly: V_mixed subset V_fine gives lam_min(S_mixed) >= lam_min(S_f)
      (Rayleigh-Ritz), and stationarity of the fine minimiser makes the gap
      SECOND ORDER in the projection defect,
          0 <= lam_min(S_mixed) - lam_min(S_f) <= ||X|| * ||(I-Pi)z*||^2 .
  M3  THE DEEP RUN.  With compression the cap h <= 1500 is spent on the MIXED
      form while the fine grid is touched only through a length-M lag vector and
      (m x q) stencils -- no fine square matrix is ever formed.  How deep does
      the margin-free circle run now, how long is the longest chain, and is the
      stopper still cost and never structure?
  M4  SYNTHESIS.  [P1] with the Szego device made explicit: given T = Q + t~t~^T
      positive definite, Q|odd >= 0 is EXACTLY the scalar inequality
      t~^T T^{-1} t~ <= 1, i.e. eps = 1 - t~^T T^{-1} t~ >= 0 -- the Szego /
      Levinson prediction-error identity, and the same Albert device one level
      down.  Then the cost scaling h(n) of the compressed scheme, and the list
      of what a k-uniform proof still needs.

PREREGISTERED VERDICTS
  TRANSPORT-CERTIFIED : the transport bracket holds on every regrid pair AND
                        leaves room against lam_min(S), the compression breaks
                        the cap, the deep run goes well past n = 1331, and the
                        stopper is still cost.
  COMPRESSION-LIMITED : transport yes, but the compression saves too little --
                        with the cost formula.
  TRANSPORT-BLOCKED   : the bound does not reach against lam_min(S) -- with
                        where and why.
  Element gates: el_firewall, el_m0, el_m1, el_m2, el_m3, el_m4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger/TeX/website/
    changelog edit, no verification/ module, no next.txt, no .md output.
  * NO Riemann zero data of any kind; an AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * RH => window Weil positivity is used in ONE DIRECTION only.  Q_full >= 0,
    hence Q|odd >= 0, is the HYPOTHESIS INPUT at the base window.  This probe
    tests what the REGRID and the COMPRESSION need beyond that input.
  * lam_min on a PWC Galerkin space is a Rayleigh-Ritz UPPER bound for the
    continuum value: it can refute positivity, never prove it.  Compression
    makes the space COARSER, so a compressed certificate is weaker still --
    declared everywhere it is used.
  * CERTIFIED vs MEASURED vs HYPOTHESIS tracked per line.  Every fit is a fit
    and carries a jackknife band.  Tolerances and backward errors explicit.
  * FLOATING-POINT LIMITS DECLARED.  A completed Cholesky of A certifies
    lam_min(A) >= -c_h u ||A||_2 with u = 2^-53, c_h = (h+1)/(1-(h+1)u)
    (Wilkinson 1968; Higham 2002, Thm 10.3/10.4), NOT lam_min(A) >= 0.
  * PRIME-GAP INPUTS DECLARED: Bertrand-Chebyshev 1852 and the trivial even-gap
    bound are the only gap facts the CONSTRUCTION consumes.
  * Classical anchors cited, not re-derived: Albert 1969, Douglas 1966, Schur
    complement / Haynsworth 1968, Loewner order, Rayleigh-Ritz, Weyl 1912,
    Cea 1964 and Strang's first lemma (projection/consistency error),
    Bramble-Hilbert 1970, Cholesky / Wilkinson 1968 / Higham 2002, Brandt 1977
    and Yserentant 1986 (two-scale / hierarchical spaces), Szego and Levinson
    1947 (prediction error), Grenander-Szego, Weil 1952, Chebyshev 1852.

OUTCOME OF THIS RUN  =>  TRANSPORT-BLOCKED, with the block located exactly and
the other half of the contract carried much further than expected:
  * The regrid transport of lam_min(S) REACHES only for mild refinement: the
    lower end of the bracket is positive on every pair with grid ratio
    rho <= 2.06 and on none with rho >= 2.29 (threshold rho* = 1.83 in a
    synthetic scan), i.e. on ~39 % of the ladder's refinement pairs, whose
    median ratio is 2.001.  The blocker is NOT the transport machinery: on
    NESTED ladders, where the transport error is exactly zero, lam_min(S) itself
    falls like rho^-1.7 under refinement.  The drop is real, so no bound can
    undo it -- the exact Schur complement is the slowest-falling of the three
    candidates (eps ~ rho^-1.71), but it is not scale-invariant either.
  * The compression works and is cheap in accuracy: X_mixed = Q_old,mixed
    EXACTLY (the compressed step is still margin-free), Albert certifies on
    66/66 (zone, q) combinations up to q = 64, and the compression error is
    one-sided and second order in the projection defect.
  * The deep run: the margin-free step certifies at n = 155921, 117 x T114's
    reach, on a fine lattice of h = 93470 cells (62 x the hard cap) compressed
    to m = 1490; chains reach 10 consecutive steps (T114: 4) and still end at
    the cost cap, never at a failing step.
  * But the cost BARRIER is divided, not broken: h = nu u / g is an identity and
    compression only divides the certified dimension by q, so the CONTIGUOUS
    reach (what an induction needs) moves from n = 125 to n = 5437 and stops.
  * [P1] is now ONE scalar inequality: given T > 0, Q|odd >= 0 is EQUIVALENT to
    the Szego-Levinson prediction-error inequality t~^T T^{-1} t~ <= 1.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, cholesky, eigh, eigvalsh

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / EIGENDECOMPOSED form
BUDGET_S = 860.0             # HARD probe budget (< 900 s)

ATOM_MAX = 200000
ZONE_MAX = 160000
NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24                   # smallest old window admitted (keeps the step real)
DEEP_N_T114 = 1331           # T114's deepest certified zone

K_FINE = 12                  # cells kept FINE at the window edge (3 nu)
Q_SET = (2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64)
M_FINE_MAX = 240000          # cap on the nominal FINE cell count (vector only)
CHUNK = 16384                # lag-vector chunk (keeps the quadrature arrays small)

N_PAIR = 12                  # transport pairs
N_NEST = 3                   # constructed nested control pairs
N_MIX = 6                    # zones for the compression study
N_DEEP = 4                   # deep single steps
N_CHAIN = 3                  # compressed multi-step chains
CHAIN_WANT = 10

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-34s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-34s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


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
                if any(c in mode for c in "wax+"):
                    bad_writes.append(mode)
    check("el_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("el_firewall.imports", not bad_imports,
          "import roots %s" % sorted(ALLOWED_IMPORT_ROOTS))
    check("el_firewall.no_writes", not bad_writes, "no write-mode open()")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap)
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


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952) -- verbatim T111..T114 code path
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


def tri(y, D):
    return np.maximum(0.0, 1.0 - np.abs(y) / D)


def atom_lag(lags_s, u, D):
    return 0.5 * (tri(lags_s - u, D) + tri(lags_s + u, D))


def atoms_in(alpha, atoms_all):
    return [(t[2], t[3]) for t in atoms_all if t[2] <= 2.0 * alpha + 1.0e-14]


def lag_vector(alpha, M, atoms):
    """REFERENCE assembly (T111..T114 verbatim): O(#atoms * M)."""
    D = 2.0 * alpha / M
    s = np.arange(M) * D
    c = arch_A(s, D)
    for u_j, mu_j in atoms:
        c = c - mu_j * atom_lag(s, u_j, D)
    return c, D


def arch_lags(M, D):
    """arch_A on the whole lag lattice, chunked so the 48-point quadrature
    arrays stay small even for M ~ 2e5."""
    out = np.empty(M)
    for a in range(0, M, CHUNK):
        b = min(M, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


def lag_vector_fast(alpha, M, atoms):
    """IDENTICAL result, O(#atoms) atom work: the cell autocorrelation
    tri(.,D) has support D, so each atom touches O(1) lags.  Validated against
    lag_vector() bit-for-bit in M0."""
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
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T114)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    """(Bm^T Toeplitz(c) Bm)_{rs} = c_{|r-s|} - c_{M-1-r-s}."""
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2).  The 1/sqrt D
    is the L2 normalisation of the cell indicator -- see odd_nodes."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def odd_nodes(alpha, M):
    """Cell CENTRES of the odd half-window, and the cell width."""
    D = 2.0 * alpha / M
    h = M // 2
    return -alpha + (np.arange(h) + 0.5) * D, D


def lmin(A):
    return float(eigvalsh(sym(A), subset_by_index=[0, 0])[0])


def norm_bound(A):
    """CERTIFIED cheap upper bound on ||A||_2 for symmetric A: the maximum
    absolute row sum (Schur test / Gershgorin), ||A||_2 <= ||A||_inf."""
    return float(np.abs(A).sum(axis=1).max())


def safe_cho(Q, shifts=(0.0,)):
    n = Q.shape[0]
    for sh in shifts:
        try:
            if sh == 0.0:
                return cho_factor(Q, lower=True, check_finite=False), 0.0
            return cho_factor(Q + sh * np.eye(n), lower=True, check_finite=False), sh
        except LinAlgError:
            continue
    return None, float("nan")


def cert_lmin(A, lam):
    """CERTIFIED (up to the DECLARED backward-error floor) lam_min(A) >= lam."""
    n = A.shape[0]
    try:
        cholesky(sym(A) - lam * np.eye(n), lower=True, check_finite=False)
        return True
    except LinAlgError:
        return False


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR of a Cholesky certificate (Wilkinson
    1968; Higham 2002, Thm 10.3/10.4): lam_min >= -c_h u ||A||_2."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


# ----------------------------------------------------------------------------
# fits (every one a FIT, with a jackknife band)
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


# ----------------------------------------------------------------------------
# frame A (T112) and the bordered step
# ----------------------------------------------------------------------------
def zone_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    return M, 0.5 * M * D, M * D - u


def frame_D(g, nu):
    return 0.5 * g / nu


def step_frame(u_old, u_new, D, force=None):
    """The bordered step at grid D: old window covers u_old, new covers u_new,
    the growth is even so the odd sector grows by gc coordinates per end."""
    M_o = zone_window(u_old, D)[0]
    M_n = zone_window(u_new, D)[0] if force is None else force
    dm = M_n - M_o
    if dm <= 0:
        return None
    if dm % 2:
        dm += 1
        M_n = M_o + dm
    gc = dm // 2
    if M_n // 2 - M_o // 2 != gc:
        return None
    al_o = 0.5 * M_o * D
    al_n = 0.5 * M_n * D
    lemma = ((M_o - 1) * D) < (u_new - D) - 1.0e-12
    return dict(D=D, M_o=M_o, M_n=M_n, gc=gc, al_o=al_o, al_n=al_n,
                h_o=M_o // 2, h_n=M_n // 2, lemma=bool(lemma))


def step_data(fr, atoms_all, want_matrix=True):
    """The new window's lag vector, pole vector and (optionally) the full
    odd-sector form Q' = [[A, C], [C^T, X]]."""
    at_n = atoms_in(fr["al_n"], atoms_all)
    c_n, D = lag_vector_fast(fr["al_n"], fr["M_n"], at_n)
    tv_n = odd_pole_vector(fr["al_n"], fr["M_n"])
    Q = None
    if want_matrix:
        Q = odd_toeplitz(c_n, fr["M_n"]) - np.outer(tv_n, tv_n)
    return dict(c=c_n, tv=tv_n, Q=Q, atoms=at_n)


def schur_full(Q, gc):
    """The EXACT Schur complement S = A - C X^{-1} C^T, its smallest eigenpair,
    and the partial minimiser z* = -X^{-1} C^T y*.  Albert 1969: with X PD the
    range condition is vacuous and Q' >= 0 <=> S >= 0."""
    A = sym(np.ascontiguousarray(Q[:gc, :gc]))
    C = np.ascontiguousarray(Q[:gc, gc:])
    X = sym(np.ascontiguousarray(Q[gc:, gc:]))
    fac, _ = safe_cho(X)
    if fac is None:
        return None
    Z = cho_solve(fac, C.T, check_finite=False)
    S = sym(A - C @ Z)
    ev, U = eigh(S)
    y = np.ascontiguousarray(U[:, 0])
    z = -(Z @ y)
    return dict(A=A, C=C, X=X, S=S, lam=float(ev[0]), y=y, z=z,
                nz=float(np.linalg.norm(z)), nC=float(np.linalg.norm(C)),
                lam_X=None, nrm_X=norm_bound(X), S_cert=cert_lmin(S, 0.0),
                x_pd=True, fac=fac, Z=Z)


def overlap_odd(xt, Dt, xs, Ds):
    """<phi^t_i, phi^s_j> for L2-normalised PWC cells in ODD coordinates.  For
    an INTEGER ratio with aligned windows this is the exact nested prolongation
    (orthonormal columns); otherwise it is the L2 projection with a defect."""
    a = np.asarray(xt, dtype=float)[:, None]
    b = np.asarray(xs, dtype=float)[None, :]
    den = math.sqrt(Dt * Ds)

    def ov(bb):
        lo = np.maximum(a - 0.5 * Dt, bb - 0.5 * Ds)
        hi = np.minimum(a + 0.5 * Dt, bb + 0.5 * Ds)
        return np.maximum(0.0, hi - lo) / den

    return ov(b) - ov(-b)


firewall()


# ----------------------------------------------------------------------------
section("M0  SETUP -- the discretisation named, frame A, and the regrid table")
# ----------------------------------------------------------------------------
ATOMS_ALL = atom_table(ATOM_MAX)
ZALL = [t for t in ATOMS_ALL if t[0] <= ZONE_MAX]
GAPS = [ATOMS_ALL[i + 1][2] - t[2] for i, t in enumerate(ZALL)]
ZTAB = []
for i in range(len(ZALL) - 1):
    n_k, lam_k, u_k, mu_k = ZALL[i]
    ZTAB.append(dict(idx=i, n=n_k, lam=lam_k, u=u_k, mu=mu_k, g=GAPS[i],
                     u_next=ZALL[i + 1][2], n_next=ZALL[i + 1][0],
                     g_next=GAPS[i + 1] if i + 1 < len(GAPS) else float("nan")))
info("M0.atoms", "%d prime-power atoms up to %d; %d zones up to %d; log-gaps "
     "g_k in [%.6f, %.6f]" % (len(ATOMS_ALL), ATOM_MAX, len(ZTAB), ZONE_MAX,
                              min(GAPS), max(GAPS)))

BERT_OK = all(g <= math.log(2.0) + 1.0e-12 for g in GAPS)
EVEN_OK = all(GAPS[i] >= math.log1p(1.0 / ZALL[i][0]) - 1.0e-12
              for i in range(len(GAPS)))
check("el_m0.gap_bounds", BERT_OK and EVEN_OK,
      "the two CLASSICAL gap facts the frame consumes hold on the whole table: "
      "Bertrand-Chebyshev 1852 g_k <= log 2 (max %.6f) and g_k >= log(1+1/n) "
      "(max 1/g = %.1f).  No unproved gap hypothesis enters the CONSTRUCTION"
      % (max(GAPS), 1.0 / min(GAPS)))

info("M0.hypothesis", "HYPOTHESIS INPUT, never proved here: Q_full(alpha) >= 0, "
     "hence Q|odd >= 0 (RH => window Weil positivity, ONE direction).  BASE "
     "SEMIDEFINITENESS IS AN INPUT.  This probe asks what the REGRID and the "
     "COMPRESSION need BEYOND that input")
info("M0.fp_regime", "u = 2^-53 = %.3e; a completed Cholesky of A certifies "
     "lam_min(A) >= -c_h u ||A||_2, c_h = (h+1)/(1-(h+1)u); at h = %d the floor "
     "is %.2e * ||A||_2" % (U_ROUND, MAX_H, chol_floor(1.0, MAX_H)))

# --- M0.1  the discretisation, named exactly -------------------------------
print("")
print("""  M0.1  WHAT THE BASIS IS (this fixes the transport operator).  The lag
  vector uses tri(.,D) = the AUTOCORRELATION of the cell indicator divided by
  D, and the pole vector carries 1/sqrt(D); both are the signature of the
  L2-NORMALISED PIECEWISE-CONSTANT family

      phi_r = 1_{[-alpha + rD, -alpha + (r+1)D]} / sqrt(D),   r = 0..M-1,

  antisymmetrised into the odd sector.  Two consequences, both used below:
    (a) the exact transfer operator between two grids is the CELL-OVERLAP
        matrix P[i,j] = <phi^f_i, phi^c_j>, and R = P^T is the L2 projection
        the other way (fine basis orthonormal);
    (b) V_c subset V_f iff D_c/D_f is a POSITIVE INTEGER and the windows align
        -- being DYADIC is neither necessary nor sufficient.  T114 counted
        dyadic ratios; the correct count is the INTEGER one, done here.""")
print("")

_M_T, _D_T = 96, None
_al_T = 0.5 * _M_T * 0.02
_at_T = atoms_in(_al_T, ATOMS_ALL)
_c_ref, _ = lag_vector(_al_T, _M_T, _at_T)
_c_fast, _ = lag_vector_fast(_al_T, _M_T, _at_T)
E_FAST = float(np.abs(_c_ref - _c_fast).max())
check("el_m0.fast_lag", E_FAST == 0.0,
      "the O(#atoms) assembly reproduces the T111..T114 reference assembly "
      "BIT-EXACTLY on a %d-cell window with %d atoms (max |diff| = %.1e).  It "
      "is what makes the deep compressed windows affordable"
      % (_M_T, len(_at_T), E_FAST))
del _c_ref, _c_fast

# --- M0.2  nestability of the real ladder ----------------------------------
RATIO = [ZTAB[i]["g"] / ZTAB[i + 1]["g"] for i in range(len(ZTAB) - 1)]
RAT_UP = [x for x in RATIO if x > 1.0]
DYAD = sum(1 for x in RATIO if abs(math.log2(x) - round(math.log2(x))) < 1.0e-9)
INTEG = sum(1 for x in RATIO
            if min(abs(x - round(x)), abs(1.0 / x - round(1.0 / x))) < 1.0e-9)
NEAR = [min(abs(x - round(x)), abs(1.0 / x - round(1.0 / x))) for x in RATIO]
RQ = np.quantile(np.asarray([max(x, 1.0 / x) for x in RATIO]), [0.5, 0.9, 0.99])
info("M0.nestability", "%d consecutive gap ratios: median %.3f, 90%% %.3f, "
     "99%% %.3f, max %.3f.  DYADIC on %d, INTEGER on %d.  The closest any "
     "ratio comes to an integer is %.3e (median distance %.3f), so the ladder "
     "is not merely non-dyadic, it is nowhere near nestable -- a perturbative "
     "transport around an integer ratio is not available either"
     % (len(RATIO), RQ[0], RQ[1], RQ[2], max(max(x, 1.0 / x) for x in RATIO),
        DYAD, INTEG, min(NEAR), float(np.median(NEAR))))
check("el_m0.nest_arith", DYAD == 0 and INTEG == 0,
      "NON-NESTEDNESS RESTATED CORRECTLY.  For the PWC family the nesting "
      "criterion is an INTEGER ratio, not a dyadic one; %d of %d ratios are "
      "integer and %d of %d dyadic, and %d of the %d refinement pairs "
      "(g_k+1 < g_k) must therefore be crossed by TRANSPORT, not by "
      "restriction" % (INTEG, len(RATIO), DYAD, len(RATIO), len(RAT_UP),
                       len(RATIO)))

# --- M0.3  frame A, the step, and the exact-zero lemma ---------------------
ZF = []
for r in ZTAB:
    D = frame_D(r["g"], NU_MAIN)
    fr = step_frame(r["u"], r["u_next"], D)
    if fr is None:
        continue
    fr.update(n=r["n"], n_next=r["n_next"], u=r["u"], u_next=r["u_next"],
              g=r["g"], g_next=r["g_next"], idx=r["idx"], mu=r["mu"])
    ZF.append(fr)
ZF_CAP = [z for z in ZF if H_MIN <= z["h_o"] and z["h_n"] <= MAX_H]
L_STEP = all(z["gc"] == NU_MAIN for z in ZF_CAP)
L_ZERO = all(z["lemma"] for z in ZF_CAP)
check("el_m0.frame_lemmas", L_STEP and L_ZERO,
      "T112's frame-A lemmas hold on all %d zones under the uniform cap: the "
      "step grows by EXACTLY nu = %d cells per end and the INCOMING ATOM's "
      "autocorrelation restricted to the OLD window is the exact zero matrix, "
      "so X = Q_old exactly and the step hypothesis is PURE semidefiniteness"
      % (len(ZF_CAP), NU_MAIN))
info("M0.reach_uniform", "uniform reach at nu = %d, h <= %d: %d zones, deepest "
     "n = %d (T114's %d); the binding quantity is nu*u/g, not n"
     % (NU_MAIN, MAX_H, len(ZF_CAP), max(z["n"] for z in ZF_CAP), DEEP_N_T114))

_zt = max([z for z in ZF_CAP if z["h_n"] <= 320], key=lambda z: z["n"])
_sd = step_data(_zt, ATOMS_ALL)
_Qn = _sd["Q"]
_at_o = atoms_in(_zt["al_o"], ATOMS_ALL)
_c_o, _ = lag_vector_fast(_zt["al_o"], _zt["M_o"], _at_o)
_tv_o = odd_pole_vector(_zt["al_o"], _zt["M_o"])
_Qo = odd_toeplitz(_c_o, _zt["M_o"]) - np.outer(_tv_o, _tv_o)
E_SUB = (float(np.abs(_Qn[_zt["gc"]:, _zt["gc"]:] - _Qo).max())
         / float(np.abs(_Qo).max()))
check("el_m0.step_identity", E_SUB < 1.0e-13,
      "at n = %d -> %d (h %d -> %d, gc = %d) the new window's trailing block "
      "IS the old window's form to rel %.2e -- the T112 exact-zero property, "
      "rebuilt here because the compressed step in M2 inherits it"
      % (_zt["n"], _zt["n_next"], _zt["h_o"], _zt["h_n"], _zt["gc"], E_SUB))
del _Qn, _Qo, _sd
info("M0.timing", "M0 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("M1  THE TRANSPORT -- the exact Schur complement across the regrid")
# ----------------------------------------------------------------------------
print("""  THE DEVICE.  Haynsworth's partial minimisation makes the Schur
  complement variational and INVERSE-FREE:

      y^T S y = min_z [y; z]^T Q' [y; z] ,      lam_min(S) = min_{|y|=1} ... ,

  so lam_min(S) can be transported between grids with the overlap operators
  P (coarse -> fine) and R = P^T (fine -> coarse) and NO reference to
  lam_min(X).  With w* the minimiser on each side:

      LOWER   lam_min(S_f) >= lam_min(S_c) * ||(R w_f*)_y||^2 - |eta_dn| ,
      UPPER   lam_min(S_f) <= ( lam_min(S_c) + |eta_up| ) / ||(P w_c*)_y||^2 ,
      eta_dn = F_c(R w_f*) - F_f(w_f*) ,   eta_up = F_f(P w_c*) - F_c(w_c*) .

  Both eta are FORM-CONSISTENCY defects.  For NESTED pairs eta_up = 0 exactly
  (the Galerkin identity Q_c = P^T Q_f P) and the UPPER direction is free --
  that is Rayleigh-Ritz.  The LOWER direction is the whole of [P2].

  HONESTY ABOUT WHAT THE BRACKET IS.  With eta DEFINED as the difference of the
  two form values, the bracket is an IDENTITY CHAIN: it holds for any linear
  operator whatsoever, so 'the bracket holds' is bookkeeping, not evidence.
  What carries content is (a) the numerical validity of Haynsworth's partial-
  minimisation identity itself, (b) the SIZE of tau and eta -- small only for a
  genuine transport operator, which is what the control in M1.4 tests -- and
  (c) whether the lower end is POSITIVE, i.e. whether coarse positivity leaves
  room after the transport deficit.  Everything below is labelled accordingly:
  the eta values are MEASURED at the minimisers, and a CERTIFIED transport
  needs an a-priori bound on eta, which is a REGULARITY statement about the
  minimiser and is named in M4 as the residue.""")
print("")

# --- M1.1  the nested control: the Galerkin identity is exact --------------
def refine_frame(fr_c, u_next, rho):
    """The SAME physical step at rho times the resolution.  For integer rho the
    windows align exactly, so V_c subset V_f (nested)."""
    D_f = fr_c["D"] / rho
    M_o = int(round(rho * fr_c["M_o"]))
    M_n = int(round(rho * fr_c["M_n"]))
    h_o, h_n = M_o // 2, M_n // 2
    if (M_n - M_o) % 2 or h_n - h_o != (M_n - M_o) // 2:
        return None
    return dict(D=D_f, M_o=M_o, M_n=M_n, gc=h_n - h_o, h_o=h_o, h_n=h_n,
                al_o=0.5 * M_o * D_f, al_n=0.5 * M_n * D_f,
                lemma=bool(((M_o - 1) * D_f) < (u_next - D_f) - 1.0e-12))


NEST = []
_zn = [z for z in ZF_CAP if 60 <= z["h_n"] <= 214]
_zn = sorted(_zn, key=lambda z: -z["n"])[:2]
for zc in _zn:
    fr_c = step_frame(zc["u"], zc["u_next"], zc["D"])
    sd_c = step_data(fr_c, ATOMS_ALL)
    sc_c = schur_full(sd_c["Q"], fr_c["gc"])
    lad = [dict(n=zc["n"], rho=1, h=fr_c["h_n"], gc=fr_c["gc"], orth=0.0,
                rel=0.0, lam=sc_c["lam"], nrm=norm_bound(sd_c["Q"]))]
    x_c, _ = odd_nodes(fr_c["al_n"], fr_c["M_n"])
    for rho in (2, 3, 5, 7):
        fr_f = refine_frame(fr_c, zc["u_next"], rho)
        if fr_f is None or not fr_f["lemma"] or fr_f["h_n"] > MAX_H:
            continue
        sd_f = step_data(fr_f, ATOMS_ALL)
        x_f, _ = odd_nodes(fr_f["al_n"], fr_f["M_n"])
        P = overlap_odd(x_f, fr_f["D"], x_c, fr_c["D"])
        orth = float(np.abs(P.T @ P - np.eye(P.shape[1])).max())
        Gid = P.T @ sd_f["Q"] @ P - sd_c["Q"]
        rel = float(np.abs(Gid).max()) / float(np.abs(sd_c["Q"]).max())
        sc_f = schur_full(sd_f["Q"], fr_f["gc"])
        lad.append(dict(n=zc["n"], rho=rho, h=fr_f["h_n"], gc=fr_f["gc"],
                        orth=orth, rel=rel, lam=sc_f["lam"],
                        nrm=norm_bound(sd_f["Q"])))
        del P, Gid, sd_f, sc_f
    NEST.append(lad)
    del sd_c, sc_c

print("  M1.1  NESTED CONTROL (integer ratio, windows aligned by construction)")
print("      n    rho    h    gc | ||P^TP - I||  ||P^T Q_f P - Q_c||_rel |"
      "  lam_min(S)   drop vs rho=1")
NEST_ROWS = [t for lad in NEST for t in lad]
for lad in NEST:
    for t in lad:
        print("   %6d   %2d  %5d  %3d |    %.2e            %.3e        | "
              "%11.6f   %8.3f"
              % (t["n"], t["rho"], t["h"], t["gc"], t["orth"], t["rel"],
                 t["lam"], lad[0]["lam"] / t["lam"]))
NEST_OK = [t for t in NEST_ROWS if t["rho"] == 1
           or (t["orth"] < 1.0e-11 and t["rel"] < 1.0e-9)]
check("el_m1.galerkin_nested", len(NEST_ROWS) >= 6 and len(NEST_OK) == len(NEST_ROWS),
      "THE MACHINERY IS EXACT WHERE IT MUST BE.  On %d constructed nested "
      "refinements (integer ratios 2,3,5,7 at %d zones) the overlap operator "
      "has orthonormal columns to %.1e and the GALERKIN IDENTITY "
      "Q_c = P^T Q_f P holds to relative %.1e -- so the PWC assembly (arch "
      "autocorrelation, EXACT atom bookkeeping, pole vector with its 1/sqrt D) "
      "is a genuine Gram matrix of ONE bilinear form, and the transport "
      "operator is the right one"
      % (len(NEST_ROWS) - len(NEST), len(NEST),
         max(t["orth"] for t in NEST_ROWS), max(t["rel"] for t in NEST_ROWS)))

# --- M1.1b  the refinement power of lam_min(S): the deficit to be absorbed --
RP = []
for lad in NEST:
    if len(lad) < 4:
        continue
    xs = [math.log(t["rho"]) for t in lad]
    ys = [math.log(t["lam"]) for t in lad]
    a, b, rms, se = fit_band(xs, ys)
    RP.append(dict(n=lad[0]["n"], b=b, se=se, rms=rms, k=len(lad),
                   lo=lad[0]["lam"], hi=lad[-1]["lam"], rmax=lad[-1]["rho"]))
print("")
print("""  M1.1b  THE EXACT SCHUR COMPLEMENT IS NOT REFINEMENT-STABLE.  On the
  NESTED ladder (where every comparison is exact, no transport error at all)
  lam_min(S) FALLS under refinement -- it must, by Rayleigh-Ritz, because the
  finer boundary block resolves more directions of the same physical strip.
  That fall is the deficit ANY coarse-to-fine transport has to absorb, and it
  is a FIT (jackknife band):""")
for t in RP:
    print("     n = %5d :  lam_min(S) ~ rho^(%+.3f +- %.3f)   (rms %.3f, %d "
          "points, %.4f -> %.4f up to rho = %d)"
          % (t["n"], t["b"], t["se"], t["rms"], t["k"], t["lo"], t["hi"],
             t["rmax"]))
info("M1.refine_power", "MEASURED (FIT): lam_min(S) ~ rho^%.2f..%.2f, i.e. the "
     "O(0.1) object T114 identified is scale-DEPENDENT with an exponent close "
     "to the eps exponent D^1.8 -- but WITHOUT the 1e-7 cancellation.  So the "
     "transport does not remove the need for a D-rate; it replaces a rate for "
     "a cancelling 1e-7 quantity by a rate for a cancellation-free O(0.1) one"
     % (min(t["b"] for t in RP), max(t["b"] for t in RP)))

# --- M1.2  the real regrid pairs -------------------------------------------
CAND = []
for z in ZF:
    if not math.isfinite(z["g_next"]) or z["g_next"] >= z["g"]:
        continue
    D_f = frame_D(z["g_next"], NU_MAIN)
    fr_f = step_frame(z["u"], z["u_next"], D_f)
    if fr_f is None or not fr_f["lemma"]:
        continue
    if fr_f["h_n"] > MAX_H or z["h_o"] < H_MIN:
        continue
    CAND.append((z, fr_f, z["g"] / z["g_next"]))
CAND.sort(key=lambda t: t[0]["n"])
PICK = []
if CAND:
    _tg = np.geomspace(CAND[0][0]["n"], CAND[-1][0]["n"], N_PAIR - 3)
    for t in _tg:
        b = min(CAND, key=lambda q: abs(math.log(q[0]["n"]) - math.log(t)))
        if b not in PICK:
            PICK.append(b)
    for b in sorted(CAND, key=lambda q: -q[2])[:3]:
        if b not in PICK:
            PICK.append(b)
PICK.sort(key=lambda t: t[0]["n"])

TR = []
for (zc, fr_f, rho) in PICK:
    if budget_left() < 420.0:
        info("M1.budget", "pair list truncated at n = %d" % zc["n"])
        break
    fr_c = step_frame(zc["u"], zc["u_next"], zc["D"])
    sd_c = step_data(fr_c, ATOMS_ALL)
    sd_f = step_data(fr_f, ATOMS_ALL)
    sc_c = schur_full(sd_c["Q"], fr_c["gc"])
    sc_f = schur_full(sd_f["Q"], fr_f["gc"])
    if sc_c is None or sc_f is None:
        continue
    x_c, _ = odd_nodes(fr_c["al_n"], fr_c["M_n"])
    x_f, _ = odd_nodes(fr_f["al_n"], fr_f["M_n"])
    P = overlap_odd(x_f, fr_f["D"], x_c, fr_c["D"])
    w_c = np.concatenate([sc_c["y"], sc_c["z"]])
    w_f = np.concatenate([sc_f["y"], sc_f["z"]])
    Fc = float(w_c @ sd_c["Q"] @ w_c)
    Ff = float(w_f @ sd_f["Q"] @ w_f)
    # DOWN: fine minimiser projected onto the coarse space
    w_cf = P.T @ w_f
    tau_dn = float(np.dot(w_cf[:fr_c["gc"]], w_cf[:fr_c["gc"]]))
    eta_dn = float(w_cf @ sd_c["Q"] @ w_cf) - Ff
    # UP: coarse minimiser prolonged onto the fine space
    w_fc = P @ w_c
    tau_up = float(np.dot(w_fc[:fr_f["gc"]], w_fc[:fr_f["gc"]]))
    eta_up = float(w_fc @ sd_f["Q"] @ w_fc) - Fc
    lo = sc_c["lam"] * tau_dn - abs(eta_dn)
    hi = ((sc_c["lam"] + abs(eta_up)) / tau_up if tau_up > 0.0
          else float("inf"))
    # the A-PRIORI surrogate of the same eta: a NORM bound on the defect
    Gup = P.T @ sd_f["Q"] @ P - sd_c["Q"]
    ap_up = norm_bound(Gup) * float(w_c @ w_c)
    ap_dn = float("nan")
    if fr_f["h_n"] <= 900:
        Gdn = P @ sd_c["Q"] @ P.T - sd_f["Q"]
        ap_dn = norm_bound(Gdn) * float(w_f @ w_f)
        del Gdn
    hay = max(abs(Ff - sc_f["lam"]), abs(Fc - sc_c["lam"]))
    TR.append(dict(n=zc["n"], rho=rho, h_c=fr_c["h_n"], h_f=fr_f["h_n"], hay=hay,
                   gc_c=fr_c["gc"], gc_f=fr_f["gc"], lam_c=sc_c["lam"],
                   lam_f=sc_f["lam"], tau_dn=tau_dn, tau_up=tau_up,
                   eta_dn=eta_dn, eta_up=eta_up, lo=lo, hi=hi,
                   nz_c=sc_c["nz"], nz_f=sc_f["nz"], nC=sc_c["nC"],
                   nrmG=norm_bound(Gup), ap_up=ap_up, ap_dn=ap_dn,
                   nw_c=float(w_c @ w_c), nw_f=float(w_f @ w_f),
                   lam_X=lmin(sc_c["X"])))
    del P, Gup, sd_c, sd_f, sc_c, sc_f, w_c, w_f, w_cf, w_fc

print("")
print("  M1.2  THE REAL REGRID PAIRS (grid ratio rho = g_k/g_k+1, non-integer)")
print("      n     rho    h_c  h_f  gc | lam_S(c)  lam_S(f) | tau_dn  |eta_dn|"
      "  |eta_up| | bracket lo    hi")
for t in TR:
    print("   %6d  %6.3f  %4d %4d %2d/%-2d| %8.5f  %8.5f | %6.4f  %8.2e  "
          "%8.2e | %10.3e  %9.3e"
          % (t["n"], t["rho"], t["h_c"], t["h_f"], t["gc_c"], t["gc_f"],
             t["lam_c"], t["lam_f"], t["tau_dn"], abs(t["eta_dn"]),
             abs(t["eta_up"]), t["lo"], t["hi"]))
BR_OK = [t for t in TR if t["lo"] - 1.0e-10 <= t["lam_f"] <= t["hi"] + 1.0e-10]
ROOM = [t for t in TR if t["lo"] > 0.0]
HAY = max(t["hay"] for t in TR)
check("el_m1.haynsworth", len(TR) >= 4 and HAY < 1.0e-9 and len(BR_OK) == len(TR),
      "THE VARIATIONAL DEVICE IS VALID NUMERICALLY on %d real regrid pairs "
      "(rho = %.3f..%.3f, never an integer): the partial minimisation "
      "y*^T S y* = F(y*, z*) reproduces lam_min(S) to %.1e on BOTH grids, so "
      "lam_min(S) really is available WITHOUT inverting X and without a margin "
      "(Haynsworth 1968).  The bracket itself is an identity chain and is "
      "reported, not claimed as evidence; its INGREDIENTS are the evidence"
      % (len(TR), min(t["rho"] for t in TR), max(t["rho"] for t in TR), HAY))
RHO_OK = max([t["rho"] for t in ROOM], default=0.0)
RHO_BAD = min([t["rho"] for t in TR if t["lo"] <= 0.0], default=float("inf"))
check("el_m1.reach_split", len(ROOM) >= 1 and RHO_OK < RHO_BAD,
      "AND IT REACHES ONLY UP TO A RATIO.  The LOWER bracket end is strictly "
      "positive on %d of %d pairs -- on EVERY pair with grid ratio rho <= %.3f "
      "and on NONE with rho >= %.3f, a CLEAN split.  Positivity of the exact "
      "Schur complement therefore transports across a real regrid iff the "
      "refinement is mild; what blocks the rest is not the defect eta but the "
      "Rayleigh-Ritz DROP measured in M1.1b (lam_min(S) ~ rho^-1.5), which no "
      "bound can undo because the drop is REAL"
      % (len(ROOM), len(TR), RHO_OK, RHO_BAD))

# --- M1.3  sharpness: the measured defect vs its a-priori norm surrogate ---
print("")
print("""  M1.3  SHARPNESS, AND WHERE THE MARGIN WOULD COME BACK.  eta is
  evaluated at the ACTUAL minimisers (MEASURED).  Its a-priori surrogate is a
  NORM bound on the defect matrix, |eta| <= ||P^T Q_f P - Q_c|| ||w||^2, which
  is the Cea/Strang route.  The same two numbers that killed the T114 norm
  surrogate reappear: ||w||^2 is dominated by the partial minimiser z*, and
  bounding ||z*|| a priori by ||C||/lam_min(X) divides by the margin again --
  while the MEASURED z* is O(1).""")
print("")
print("      n    | ||z*||_c  ||C||/lam_min(X)  ratio | |eta_up|   a-priori "
      "  sharpness")
for t in TR:
    apri = t["nC"] / max(t["lam_X"], 1.0e-300)
    sh = t["ap_up"] / max(abs(t["eta_up"]), 1.0e-300)
    print("   %6d | %8.3f  %16.3e  %5.1e | %8.2e  %9.2e  %9.1e"
          % (t["n"], t["nz_c"], apri, t["nz_c"] / apri, abs(t["eta_up"]),
             t["ap_up"], sh))
SH = [t["ap_up"] / max(abs(t["eta_up"]), 1e-300) for t in TR]
MARG = [t["nC"] / max(t["lam_X"], 1e-300) / max(t["nz_c"], 1e-300) for t in TR]
check("el_m1.apriori_gap", all(s > 1.0 for s in SH),
      "THE A-PRIORI ROUTE IS %.1e..%.1e TIMES TOO CRUDE on the same defect, "
      "and the reason is quantified: the a-priori bound ||z*|| <= "
      "||C||/lam_min(X) overshoots the MEASURED minimiser by a factor "
      "%.1e..%.1e because C is nearly orthogonal to the soft directions of X "
      "(T113/T114).  The transport is therefore certifiable only with a "
      "REGULARITY input on the minimiser -- named in M4, not smuggled in here"
      % (min(SH), max(SH), min(MARG), max(MARG)))
# --- M1.4  the reach threshold, a control, and the table coverage ----------
print("")
print("""  M1.4  HOW FAR DOES THE TRANSPORT REACH, AND WHAT DOES THE TABLE ASK?
  A synthetic (non-integer) refinement scan at one zone locates the threshold
  rho* where the lower end crosses zero; the ladder's own demand is the
  distribution of the REAL refinement ratios.  And because the bracket is an
  identity for ANY operator, the CONTROL is on the OPERATOR: three deliberately
  wrong transfer maps (wrong cell width, wrong normalisation, misaligned by
  half a coarse cell) must give a LARGER deficit |eta| and a WORSE lower end
  than the exact cell-overlap projection.  If they did not, the operator would
  be carrying no information.""")
print("")
_zs = max([z for z in ZF_CAP if 120 <= z["h_n"] <= 400], key=lambda z: z["n"])
_frs = step_frame(_zs["u"], _zs["u_next"], _zs["D"])
_sds = step_data(_frs, ATOMS_ALL)
_scs = schur_full(_sds["Q"], _frs["gc"])
_xs, _ = odd_nodes(_frs["al_n"], _frs["M_n"])
_ws = np.concatenate([_scs["y"], _scs["z"]])
_Fs = float(_ws @ _sds["Q"] @ _ws)
OPS = ("overlap", "half-width", "x1.5 norm", "misaligned")
SCAN = []
for rho in (1.05, 1.31, 1.57, 1.83, 2.11, 2.37, 2.63, 3.11, 3.77):
    fr_f = step_frame(_zs["u"], _zs["u_next"], _zs["D"] / rho)
    if fr_f is None or not fr_f["lemma"] or fr_f["h_n"] > MAX_H:
        continue
    sd_f = step_data(fr_f, ATOMS_ALL)
    sc_f = schur_full(sd_f["Q"], fr_f["gc"])
    if sc_f is None:
        continue
    x_f, _ = odd_nodes(fr_f["al_n"], fr_f["M_n"])
    w_f = np.concatenate([sc_f["y"], sc_f["z"]])
    Ff = float(w_f @ sd_f["Q"] @ w_f)
    row = dict(rho=rho, h=fr_f["h_n"], lam=sc_f["lam"], eta={}, lo={})
    for op in OPS:
        if op == "half-width":
            P = overlap_odd(x_f, 0.5 * fr_f["D"], _xs, _frs["D"])
        elif op == "x1.5 norm":
            P = 1.5 * overlap_odd(x_f, fr_f["D"], _xs, _frs["D"])
        elif op == "misaligned":
            P = overlap_odd(x_f, fr_f["D"], _xs + 0.5 * _frs["D"], _frs["D"])
        else:
            P = overlap_odd(x_f, fr_f["D"], _xs, _frs["D"])
        w_cf = P.T @ w_f
        tau = float(np.dot(w_cf[:_frs["gc"]], w_cf[:_frs["gc"]]))
        eta = float(w_cf @ _sds["Q"] @ w_cf) - Ff
        row["eta"][op] = abs(eta)
        row["lo"][op] = _scs["lam"] * tau - abs(eta)
        del P
    SCAN.append(row)
    del sd_f, sc_f
print("      rho    h_f  | lam_S(fine) |     |eta_dn| for the four transfer "
      "operators      | lower end (overlap)")
print("                  |             |  overlap   half-width   x1.5 norm  "
      "misaligned |")
for t in SCAN:
    print("    %6.2f  %4d  |  %9.6f  | %9.3e  %9.3e  %9.3e  %9.3e | %11.3e"
          % (t["rho"], t["h"], t["lam"], t["eta"]["overlap"],
             t["eta"]["half-width"], t["eta"]["x1.5 norm"],
             t["eta"]["misaligned"], t["lo"]["overlap"]))
RHO_STAR = max([t["rho"] for t in SCAN if t["lo"]["overlap"] > 0.0],
               default=float("nan"))
RHO_FAIL = min([t["rho"] for t in SCAN if t["lo"]["overlap"] <= 0.0],
               default=float("inf"))
COVER = [x for x in RATIO if x > 1.0]
COV_OK = sum(1 for x in COVER if x <= RHO_STAR)
BEST_ETA = sum(1 for t in SCAN
               if t["eta"]["overlap"] == min(t["eta"][o] for o in OPS))
BEST_LO = sum(1 for t in SCAN
              if t["lo"]["overlap"] == max(t["lo"][o] for o in OPS))
CTRL_RAT = [max(t["eta"][o] for o in OPS) / max(t["eta"]["overlap"], 1e-300)
            for t in SCAN]
check("el_m1.operator_control", BEST_ETA == len(SCAN) and BEST_LO == len(SCAN),
      "THE OPERATOR CARRIES THE INFORMATION.  On all %d scan points the exact "
      "cell-overlap projection gives the SMALLEST transport deficit and the "
      "BEST lower end of the four transfer maps; the deliberately wrong maps "
      "(halved cell width, 1.5x normalisation, half-cell misalignment) inflate "
      "|eta| by up to %.1fx.  So the transport is a real construction, not a "
      "reshuffling of definitions -- while the bracket's VALIDITY remains an "
      "identity and is never used as evidence" % (len(SCAN), max(CTRL_RAT)))
check("el_m1.coverage", math.isfinite(RHO_STAR) and RHO_STAR < RHO_FAIL,
      "THE THRESHOLD AND THE DEMAND, side by side (MEASURED).  At n = %d the "
      "lower end is positive up to rho* = %.2f and negative from rho = %.2f, "
      "and the "
      "ladder's own refinement ratios (%d pairs with g_k+1 < g_k) satisfy "
      "rho <= rho* on %d of them (%.0f%%; median ratio %.3f).  So the transport "
      "as constructed covers about half the regrids and provably cannot cover "
      "the rest -- WHICH IS WHY THE COMPRESSION ROUTE (M2/M3) HAS TO CARRY THE "
      "PROGRAMME" % (_zs["n"], RHO_STAR, RHO_FAIL, len(COVER), COV_OK,
                     100.0 * COV_OK / max(len(COVER), 1),
                     float(np.median(COVER))))
del _sds, _scs
info("M1.timing", "M1 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("M2  MULTI-RESOLUTION -- fine at the boundary, merged in the interior")
# ----------------------------------------------------------------------------
print("""  THE TWO-SCALE FORM.  T113 found that INTERIOR atoms perturb the form
  1e7 times more than the boundary atom -- but interior atoms are OLD and
  already certified; the RESOLUTION is needed only where the new atom arrives.
  So merge q neighbouring interior cells into one:

      psi_j = (1/sqrt q) sum_{r in block j} phi_r          (block average)

  which is EXACTLY a coarser PWC space, V_mixed subset V_fine, with orthonormal
  columns.  Two structural facts make it usable:
    (a) the merge is anchored at the CENTRE of the window, so the graded space
        is STABLE under window growth: the new window's basis is the old one
        plus gc new fine cells, hence X_mixed = Q_old,mixed EXACTLY and the
        margin-free step (Albert 1969) survives compression verbatim;
    (b) the compression error is ONE-SIDED and SECOND ORDER.  Rayleigh-Ritz
        gives lam_min(S_mixed) >= lam_min(S_fine), and because z* is a
        stationary point of F(y*, .) the gap obeys
            0 <= lam_min(S_mixed) - lam_min(S_fine) <= ||X|| ||(I-Pi)z*||^2
        (Cea 1964 / Strang's first lemma in its second-order form).
  DIRECTION FENCE: a compressed certificate lives on a COARSER Galerkin space.
  Like every certificate here it can refute continuum positivity, never prove
  it -- compression makes that gap larger, and it is declared, not hidden.""")
print("")


def merge_cols(h, q, k_fine, ngroup=None):
    """The graded PWC space: fine cells 0..r_split-1 at the window EDGE, blocks
    of q merged cells inward, anchored at the window CENTRE (index h-1)."""
    if ngroup is None:
        ngroup = max(0, (h - k_fine) // q)
    r_split = h - ngroup * q
    if r_split < 1 or r_split > h:
        return None
    starts = [r_split + j * q for j in range(ngroup)]
    return dict(h=h, q=q, r_split=r_split, ngroup=ngroup, starts=starts,
                m=r_split + ngroup)


def merge_J(mc):
    """The DENSE prolongation (only built when h <= MAX_H); columns orthonormal."""
    J = np.zeros((mc["h"], mc["m"]))
    rs = mc["r_split"]
    J[np.arange(rs), np.arange(rs)] = 1.0
    w = 1.0 / math.sqrt(mc["q"])
    for j, s in enumerate(mc["starts"]):
        J[s:s + mc["q"], rs + j] = w
    return J


def merge_form(c, tv, M, mc):
    """The two-scale form J^T Q J assembled WITHOUT ever touching a fine square
    matrix: only the length-M lag vector, the pole vector and O(q) gathers."""
    q, rs, m = mc["q"], mc["r_split"], mc["m"]
    st = np.asarray(mc["starts"], dtype=np.int64)
    out = np.zeros((m, m))
    if st.size:
        dlt = st[:, None] - st[None, :]
        sgm = (M - 1) - st[:, None] - st[None, :]
        blk = np.zeros((st.size, st.size))
        for d in range(-(q - 1), q):
            blk += ((q - abs(d)) / q) * c[np.abs(dlt + d)]
        for e in range(0, 2 * q - 1):
            blk -= ((q - abs(e - (q - 1))) / q) * c[sgm - e]
        out[rs:, rs:] = blk
        del dlt, sgm, blk
    idx = np.zeros((m, q), dtype=np.int64)
    wgt = np.zeros((m, q))
    idx[:rs, :] = np.arange(rs)[:, None]
    wgt[:rs, 0] = 1.0
    if st.size:
        idx[rs:, :] = st[:, None] + np.arange(q)[None, :]
        wgt[rs:, :] = 1.0 / math.sqrt(q)
    for i in range(rs):
        row = np.zeros(m)
        for k in range(q):
            row += wgt[:, k] * (c[np.abs(i - idx[:, k])]
                                - c[(M - 1) - i - idx[:, k]])
        out[i, :] = row
        out[:, i] = row
    tj = np.zeros(m)
    for k in range(q):
        tj += wgt[:, k] * tv[idx[:, k]]
    out -= np.outer(tj, tj)
    return sym(out), idx, wgt


def old_window_data(fr, atoms_all):
    at_o = atoms_in(fr["al_o"], atoms_all)
    c_o, _ = lag_vector_fast(fr["al_o"], fr["M_o"], at_o)
    tv_o = odd_pole_vector(fr["al_o"], fr["M_o"])
    return c_o, tv_o


def mixed_step(fr, sd, q, k_fine=K_FINE):
    """The compressed bordered step: ngroup is fixed by the OLD window, so the
    new window's graded basis is the old one plus gc fine cells."""
    mc_o = merge_cols(fr["h_o"], q, k_fine)
    if mc_o is None or mc_o["ngroup"] < 1:
        return None
    mc_n = merge_cols(fr["h_n"], q, k_fine, ngroup=mc_o["ngroup"])
    if mc_n is None or mc_n["m"] != mc_o["m"] + fr["gc"]:
        return None
    Qm, _, _ = merge_form(sd["c"], sd["tv"], fr["M_n"], mc_n)
    return dict(mc_o=mc_o, mc_n=mc_n, Q=Qm, m=mc_n["m"], q=q)


# --- M2.1  the assembly and the step identity ------------------------------
_zm = max([z for z in ZF_CAP if 200 <= z["h_n"] <= 700], key=lambda z: z["n"])
_sdm = step_data(_zm, ATOMS_ALL)
_ms = mixed_step(_zm, _sdm, 4)
_J = merge_J(_ms["mc_n"])
_Qref = _J.T @ _sdm["Q"] @ _J
E_ASM = float(np.abs(_ms["Q"] - _Qref).max()) / float(np.abs(_Qref).max())
check("el_m2.assembly", E_ASM < 1.0e-13,
      "the matrix-free two-scale assembly equals J^T Q J to relative %.2e at "
      "n = %d (h = %d -> m = %d, q = 4).  It never forms a fine square matrix, "
      "which is exactly what lets M3 leave the cap behind"
      % (E_ASM, _zm["n"], _zm["h_n"], _ms["m"]))

_c_o, _tv_o = old_window_data(_zm, ATOMS_ALL)
_Qmo, _, _ = merge_form(_c_o, _tv_o, _zm["M_o"], _ms["mc_o"])
_gc = _zm["gc"]
E_MSTEP = (float(np.abs(_ms["Q"][_gc:, _gc:] - _Qmo).max())
           / float(np.abs(_Qmo).max()))
check("el_m2.step_identity", E_MSTEP < 1.0e-13,
      "THE COMPRESSED STEP IS STILL MARGIN-FREE.  With the merge anchored at "
      "the window centre, the new window's mixed form has the old window's "
      "mixed form as its EXACT trailing block (rel %.2e, m %d -> %d = m_old + "
      "gc = %d + %d), so X_mixed = Q_old,mixed and Albert's hypothesis is again "
      "PURE semidefiniteness of the previous zone -- compression does not "
      "reintroduce a margin"
      % (E_MSTEP, _ms["mc_o"]["m"], _ms["m"], _ms["mc_o"]["m"], _gc))
del _J, _Qref, _Qmo, _ms

# --- M2.2  does Albert still certify, and what does compression cost? ------
MIXZ = []
_pool = [z for z in ZF_CAP if 260 <= z["h_n"] <= MAX_H]
_tg = np.geomspace(_pool[0]["n"], _pool[-1]["n"], N_MIX) if _pool else []
for t in _tg:
    z = min(_pool, key=lambda y: abs(math.log(y["n"]) - math.log(t)))
    if z not in MIXZ:
        MIXZ.append(z)
MIX = []
for z in MIXZ:
    if budget_left() < 320.0:
        info("M2.budget", "compression study truncated at n = %d" % z["n"])
        break
    sd = step_data(z, ATOMS_ALL)
    sc_u = schur_full(sd["Q"], z["gc"])
    if sc_u is None:
        continue
    rows = []
    for q in Q_SET:
        ms = mixed_step(z, sd, q)
        if ms is None:
            continue
        sc_m = schur_full(ms["Q"], z["gc"])
        if sc_m is None:
            rows.append(dict(q=q, m=ms["m"], ok=False, lam=float("nan"),
                             gap=float("nan"), bnd=float("nan"),
                             dproj=float("nan")))
            continue
        J_o = merge_J(ms["mc_o"])
        zz = sc_u["z"]
        dz = zz - J_o @ (J_o.T @ zz)
        dproj = float(np.linalg.norm(dz))
        bnd = norm_bound(sc_u["X"]) * dproj * dproj
        rows.append(dict(q=q, m=ms["m"], ok=bool(sc_m["S_cert"]),
                         lam=sc_m["lam"], gap=sc_m["lam"] - sc_u["lam"],
                         bnd=bnd, dproj=dproj / max(np.linalg.norm(zz), 1e-300),
                         tight=(sc_m["lam"] - sc_u["lam"]) / max(bnd, 1e-300)))
        del J_o, ms, sc_m
    MIX.append(dict(z=z, lam_u=sc_u["lam"], h=z["h_n"], rows=rows,
                    cert_u=bool(sc_u["S_cert"])))
    del sd, sc_u

print("")
print("  M2.2  COMPRESSION AT FIXED ZONE: q = merge factor, m = certified size")
print("      n     h_fine  lam_S(uniform) |  q    m     m/h   lam_S(mixed)"
      "   gap        Cea bound   gap/bound  Albert")
for r in MIX:
    for k, row in enumerate(r["rows"]):
        print("   %6s  %6s  %14s | %2d %5d  %5.3f  %12.6f  %9.2e  %9.2e  "
              "%9.2e  %s"
              % (str(r["z"]["n"]) if k == 0 else "", str(r["h"]) if k == 0 else "",
                 ("%.6f" % r["lam_u"]) if k == 0 else "", row["q"], row["m"],
                 row["m"] / r["h"], row["lam"], row["gap"], row["bnd"],
                 row["tight"], "CERTIFIES" if row["ok"] else "fails"))
MROWS = [(r, w) for r in MIX for w in r["rows"]]
M_CERT = [(r, w) for r, w in MROWS if w["ok"]]
M_MONO = [(r, w) for r, w in MROWS if w["gap"] >= -1.0e-12]
M_CEA = [(r, w) for r, w in MROWS if w["gap"] <= w["bnd"] * (1.0 + 1.0e-9)]
check("el_m2.certifies", len(M_CERT) == len(MROWS) and len(MROWS) >= 12,
      "COMPRESSION DOES NOT BREAK THE STEP: Albert's exact Schur complement "
      "certifies the compressed bordering on %d of %d (zone, q) combinations, "
      "q = %d..%d, at %d zones -- and the compressed Schur floor is LARGER "
      "(lam_S(mixed)/lam_S(uniform) = %.2f..%.0f), because a coarser Galerkin "
      "space sees fewer soft directions"
      % (len(M_CERT), len(MROWS), min(w["q"] for _, w in MROWS),
         max(w["q"] for _, w in MROWS), len(MIX),
         min(w["lam"] / r["lam_u"] for r, w in MROWS),
         max(w["lam"] / r["lam_u"] for r, w in MROWS)))
check("el_m2.cea_bound", len(M_MONO) == len(MROWS) and len(M_CEA) == len(MROWS),
      "AND THE COMPRESSION ERROR IS CERTIFIED, ONE-SIDED AND SECOND ORDER.  On "
      "all %d combinations 0 <= lam_S(mixed) - lam_S(fine) <= ||X|| "
      "||(I-Pi)z*||^2 holds (Rayleigh-Ritz on the left, stationarity of z* plus "
      "Weyl on the right; Cea 1964 / Strang's first lemma), with the bound "
      "%.1e..%.1e times the measured gap.  The relative projection defect of "
      "the minimiser is %.3f..%.3f, so the interior minimiser IS coarse-scale "
      "-- the fact the compression lives on"
      % (len(MROWS), 1.0 / max(w["tight"] for _, w in MROWS),
         1.0 / max(min(w["tight"] for _, w in MROWS), 1e-300),
         min(w["dproj"] for _, w in MROWS), max(w["dproj"] for _, w in MROWS)))

# --- M2.3  what the compression costs in RESOLUTION, stated plainly --------
_res = []
for r in MIX:
    z = r["z"]
    at = atoms_in(z["al_n"], ATOMS_ALL)
    us = sorted(u for u, _ in at)
    gmin_in = min((us[i + 1] - us[i] for i in range(len(us) - 1)),
                  default=float("inf"))
    _res.append(dict(n=z["n"], D=z["D"], gmin_in=gmin_in,
                     q_res=gmin_in / z["D"]))
info("M2.resolution", "THE PRICE, NAMED: the merged interior cell has width "
     "q*D, while the smallest INTERIOR atom spacing is g_in; q <= g_in/D would "
     "keep every old atom resolved, and that ratio is only %.2f..%.2f on the "
     "study zones.  So q >= 3 is a genuine RESOLUTION SACRIFICE in the old "
     "interior, not a free lunch -- what makes it work empirically is the "
     "measured projection defect of the minimiser (%.3f..%.3f), i.e. the "
     "interior minimiser is coarse-scale even where the atoms are not"
     % (min(t["q_res"] for t in _res), max(t["q_res"] for t in _res),
        min(w["dproj"] for _, w in MROWS), max(w["dproj"] for _, w in MROWS)))
_qbest = {}
for r in MIX:
    for w in r["rows"]:
        _qbest.setdefault(w["q"], []).append(w["m"] / r["h"])
info("M2.saving", "SAVING (m/h_fine, mean over the study zones): "
     + ", ".join("q=%d: %.3f" % (q, float(np.mean(v)))
                 for q, v in sorted(_qbest.items()))
     + " -- the certified dimension falls like (K_FINE + gc)/h + 1/q, so the "
       "saving SATURATES once q ~ h/K_FINE (visible above: these study windows "
       "have h <= %d).  At the deep windows of M3, h ~ 1e5 and q = 64 realises "
       "the full 1/q, i.e. the cap m <= %d buys a fine lattice of ~ q * %d cells"
       % (max(r["h"] for r in MIX), MAX_H, MAX_H))
info("M2.timing", "M2 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("M3  THE DEEP RUN -- how far the compressed margin-free circle goes")
# ----------------------------------------------------------------------------
print("""  WHY THE CHAIN CAN RE-COARSEN BUT NOT RE-REFINE.  Inside a run at fixed
  D the newly added cells must stay fine (that is where the atom arrives), so
  the fine layer would accumulate and m would grow.  It does not have to:
  merging OLD fine cells is a RESTRICTION of the previous space, and

      X_new = Jt^T Q_old,mixed Jt   with   Jt   the merge map,

  so X_new >= 0 follows from the previous certificate by Rayleigh-Ritz -- FREE,
  in the good direction.  Only refinement (the regrid of M1) is uphill.  Hence
  a compressed chain keeps m ~ K_FINE + gc + h/q at every step, and the merge
  alignment (blocks anchored at the window centre, in steps of q) makes the
  identity above EXACT.  Verified numerically below, not assumed.""")
print("")


def deep_choice(fr):
    """The smallest merge factor that brings the step under the hard cap."""
    if fr["h_n"] <= MAX_H:
        return 1, fr["h_n"]
    if fr["M_n"] > M_FINE_MAX:
        return None
    for q in Q_SET:
        mc_o = merge_cols(fr["h_o"], q, K_FINE)
        if mc_o is None or mc_o["ngroup"] < 1:
            continue
        m = mc_o["m"] + fr["gc"]
        if m <= MAX_H:
            return q, m
    return None


DEEP_C = []
for z in ZF:
    if z["h_o"] < H_MIN or not z["lemma"]:
        continue
    ch = deep_choice(z)
    if ch is None:
        continue
    DEEP_C.append((z, ch[0], ch[1]))
DEEP_C.sort(key=lambda t: -t[0]["n"])
DEEP_RUN = DEEP_C[:N_DEEP]

DEEP = []
for (z, q, m_pred) in DEEP_RUN:
    if budget_left() < 200.0:
        info("M3.budget", "deep list truncated at n = %d" % z["n"])
        break
    t0 = time.time()
    sd = step_data(z, ATOMS_ALL, want_matrix=False)
    ms = mixed_step(z, sd, q)
    if ms is None:
        continue
    sc = schur_full(ms["Q"], z["gc"])
    if sc is None:
        continue
    c_o, tv_o = old_window_data(z, ATOMS_ALL)
    Qmo, _, _ = merge_form(c_o, tv_o, z["M_o"], ms["mc_o"])
    e_step = (float(np.abs(ms["Q"][z["gc"]:, z["gc"]:] - Qmo).max())
              / float(np.abs(Qmo).max()))
    DEEP.append(dict(n=z["n"], n_next=z["n_next"], u=z["u"], g=z["g"], q=q,
                     h_fine=z["h_n"], M=z["M_n"], m=ms["m"], lam=sc["lam"],
                     ok=bool(sc["S_cert"]), e_step=e_step, nz=sc["nz"],
                     natoms=len(sd["atoms"]), secs=time.time() - t0,
                     floor=chol_floor(norm_bound(sc["X"]), ms["m"]),
                     lam_X=lmin(sc["X"])))
    del sd, ms, sc, Qmo

print("  M3.1  THE DEEPEST COMPRESSED STEPS (uniform reach was n = %d)"
      % DEEP_N_T114)
print("      n ->  n_next |  g_k      h_fine    q     m    m/h_fine | "
      "lam_min(X)   lam_min(S)  lam_S/fp floor  Albert     X identity  s")
for t in DEEP:
    print("   %7d %7d | %.5f  %7d  %3d  %5d   %6.4f  | %10.3e  %10.6f  "
          "%12.1e    %-9s  %.1e  %5.1f"
          % (t["n"], t["n_next"], t["g"], t["h_fine"], t["q"], t["m"],
             t["m"] / t["h_fine"], t["lam_X"], t["lam"],
             t["lam"] / max(t["floor"], 1e-300),
             "CERTIFIES" if t["ok"] else "fails", t["e_step"], t["secs"]))
D_OK = [t for t in DEEP if t["ok"] and t["e_step"] < 1.0e-12]
D_PAST = [t for t in D_OK if t["n"] > DEEP_N_T114]
check("el_m3.deep_step", len(DEEP) >= 2 and len(D_OK) == len(DEEP)
      and len(D_PAST) >= 1,
      "THE CAP IS BROKEN.  The margin-free step certifies at n = %d..%d, i.e. "
      "up to %.0f times deeper than T114's uniform reach n = %d, on fine "
      "lattices of up to h = %d cells (%.0f x the hard cap) compressed to "
      "m <= %d, with the X = Q_old,mixed identity exact to %.1e -- and the step "
      "does not even look at lam_min(X) = %.1e..%.1e, which is exactly the "
      "margin-freedom of T114 now running %.0f x deeper"
      % (min(t["n"] for t in D_OK), max(t["n"] for t in D_OK),
         max(t["n"] for t in D_OK) / DEEP_N_T114, DEEP_N_T114,
         max(t["h_fine"] for t in D_OK),
         max(t["h_fine"] for t in D_OK) / MAX_H,
         max(t["m"] for t in D_OK), max(t["e_step"] for t in D_OK),
         min(t["lam_X"] for t in D_OK), max(t["lam_X"] for t in D_OK),
         max(t["n"] for t in D_OK) / DEEP_N_T114))
info("M3.price", "THE PRICE OF THE DEPTH, STATED: these steps run at merge "
     "factor q = %d..%d, so the OLD interior is represented at cell width q*D "
     "= %.2e..%.2e while the boundary strip where the new atom arrives keeps "
     "the full frame-A resolution D.  lam_min(S_mixed) = %.3f..%.3f is %.0fx "
     "the uniform O(0.1) value precisely because the space is coarser "
     "(Rayleigh-Ritz, M2.2) -- the deep certificate is a certificate for a "
     "COARSER Galerkin space, which is a weaker statement about the continuum, "
     "and it is reported as such.  Note also how FLAT that value is across the "
     "whole deep band (spread %.1f%%): at q = 64 the compressed Schur floor is "
     "set by the boundary block's own scale, not by the interior -- which is the "
     "same message as T113's, from the other side"
     % (min(t["q"] for t in DEEP), max(t["q"] for t in DEEP),
        min(t["q"] * 2.0 * t["u"] / t["M"] for t in DEEP),
        max(t["q"] * 2.0 * t["u"] / t["M"] for t in DEEP),
        min(t["lam"] for t in DEEP), max(t["lam"] for t in DEEP),
        max(t["lam"] for t in DEEP) / 0.1,
        100.0 * (max(t["lam"] for t in DEEP) / min(t["lam"] for t in DEEP)
                 - 1.0)))

# --- M3.2  compressed multi-step chains ------------------------------------
def chain_plan(i0, want):
    """Longest fixed-grid run from zone i0 that fits under the cap AFTER
    compression; q is the smallest merge factor that fits."""
    for L in range(want, 0, -1):
        if i0 + L >= len(ZTAB):
            continue
        gmin = min(ZTAB[i0 + j]["g"] for j in range(L))
        D = frame_D(gmin, NU_MAIN)
        Ms = [zone_window(ZTAB[i0 + j]["u"], D)[0] for j in range(L + 1)]
        if Ms[-1] > M_FINE_MAX or Ms[0] // 2 < H_MIN:
            continue
        if any(Ms[j + 1] <= Ms[j] or (Ms[j + 1] - Ms[j]) % 2 for j in range(L)):
            continue
        if not all(((Ms[j] - 1) * D) < (ZTAB[i0 + j + 1]["u"] - D) - 1.0e-12
                   for j in range(L)):
            continue
        for q in (1,) + Q_SET:
            ok = True
            for j in range(L + 1):
                h = Ms[j] // 2
                gc = (Ms[j] - Ms[j - 1]) // 2 if j else 0
                keep = K_FINE + gc
                ng = 0 if q == 1 else max(0, (h - keep) // q)
                m = h if q == 1 else (h - ng * q) + ng
                if m > MAX_H or (q > 1 and ng < 1):
                    ok = False
                    break
            if ok:
                return dict(L=L, D=D, Ms=Ms, gmin=gmin, q=q)
    return None


def merge_plan(h, q, gc):
    keep = K_FINE + gc
    ng = 0 if q == 1 else max(0, (h - keep) // q)
    return merge_cols(h, q, keep, ngroup=ng)


def restrict_map(mc_prev, mc_new, gc):
    """Jt: the previous mixed basis -> the new window's TRAILING basis.  Every
    new trailing vector is either a previous vector or a merge of previous FINE
    cells, so Jt exists and X_new = Jt^T Q_prev Jt (a RESTRICTION)."""
    q = mc_new["q"]
    cols = []
    for r in range(gc, mc_new["r_split"]):
        cols.append(([r - gc], [1.0]))
    for s in mc_new["starts"]:
        s_prev = s - gc
        if s_prev in mc_prev["starts"]:
            cols.append(([mc_prev["r_split"] + mc_prev["starts"].index(s_prev)],
                         [1.0]))
        elif s_prev + q <= mc_prev["r_split"]:
            cols.append((list(range(s_prev, s_prev + q)),
                         [1.0 / math.sqrt(q)] * q))
        else:
            return None
    Jt = np.zeros((mc_prev["m"], len(cols)))
    for j, (ix, wv) in enumerate(cols):
        Jt[np.asarray(ix), j] = wv
    return Jt


CH = []
_starts = []
for i0 in range(len(ZTAB) - 1):
    p = chain_plan(i0, CHAIN_WANT)
    if p is not None and p["L"] >= 3:
        _starts.append((p["L"], ZTAB[i0]["n"], i0))
_starts.sort(reverse=True)
_pool = [i for _L, _n, i in _starts[:N_CHAIN]]
_deepest = [i for _L, _n, i in sorted(_starts, key=lambda t: -t[1])[:N_CHAIN]]
for i0 in _pool + [i for i in _deepest if i not in _pool]:
    if len(CH) >= N_CHAIN + 1 or budget_left() < 150.0:
        break
    p = chain_plan(i0, CHAIN_WANT)
    if p is None:
        continue
    L, D, Ms, q = p["L"], p["D"], p["Ms"], p["q"]
    steps, ok_all, mc_prev, Q_prev, rest_max = [], True, None, None, 0.0
    for j in range(L + 1):
        M = Ms[j]
        al = 0.5 * M * D
        h = M // 2
        gc = (M - Ms[j - 1]) // 2 if j else 0
        at = atoms_in(al, ATOMS_ALL)
        c_j, _ = lag_vector_fast(al, M, at)
        tv_j = odd_pole_vector(al, M)
        mc = merge_plan(h, q, gc)
        if mc is None:
            ok_all = False
            break
        Qm, _, _ = merge_form(c_j, tv_j, M, mc)
        if j == 0:
            base = cert_lmin(Qm, 0.0)
            steps.append(dict(j=0, n=ZTAB[i0]["n"], h=h, m=mc["m"], kind="base",
                              ok=bool(base), lam=lmin(Qm), lamS=float("nan"),
                              rest=0.0,
                              floor=chol_floor(norm_bound(Qm), mc["m"])))
            ok_all = ok_all and base
        else:
            Jt = restrict_map(mc_prev, mc, gc)
            rest = float("nan")
            if Jt is not None:
                Xr = Jt.T @ Q_prev @ Jt
                rest = (float(np.abs(Qm[gc:, gc:] - Xr).max())
                        / float(np.abs(Xr).max()))
                rest_max = max(rest_max, rest)
                del Xr, Jt
            sc = schur_full(Qm, gc)
            good = bool(sc is not None and sc["S_cert"])
            steps.append(dict(j=j, n=ZTAB[i0 + j]["n"], h=h, m=mc["m"],
                              kind="step", ok=good, lam=float("nan"),
                              lamS=(sc["lam"] if sc else float("nan")),
                              rest=rest,
                              floor=chol_floor(norm_bound(Qm), mc["m"])))
            ok_all = ok_all and good
            del sc
        mc_prev, Q_prev = mc, Qm
    del mc_prev, Q_prev
    nxt = chain_plan(i0, L + 1)
    stop = ("hard cap m <= %d after compression (frame cost nu*u/g_min)" % MAX_H
            if nxt is None or nxt["L"] == L else "end of table")
    CH.append(dict(n0=ZTAB[i0]["n"], L=L, D=D, q=q, gmin=p["gmin"], steps=steps,
                   ok=ok_all, stop=stop, rest=rest_max))

print("")
print("  M3.2  COMPRESSED FIXED-GRID CHAINS (X of each step is a RESTRICTION "
      "of the previous certificate)")
for c in CH:
    print("   chain from n = %d: D = %.3e (g_min = %.5f), q = %d, %d "
          "margin-free steps, m = %d..%d"
          % (c["n0"], c["D"], c["gmin"], c["q"], c["L"], c["steps"][0]["m"],
             c["steps"][-1]["m"]))
    for s in c["steps"]:
        if s["kind"] == "base":
            print("      j=0  n = %7d  h = %6d  m = %5d  BASE   Cholesky %s  "
                  "lam_min = %.4e  (%.1e x the declared fp floor)"
                  % (s["n"], s["h"], s["m"], "OK" if s["ok"] else "FAIL",
                     s["lam"], s["lam"] / max(s["floor"], 1e-300)))
        else:
            print("      j=%d  n = %7d  h = %6d  m = %5d  STEP   Albert %s  "
                  "lam_min(S) = %.4e  (%.1e x fp floor)  restriction rel %.1e"
                  % (s["j"], s["n"], s["h"], s["m"],
                     "CERTIFIES" if s["ok"] else "fails", s["lamS"],
                     s["lamS"] / max(s["floor"], 1e-300), s["rest"]))
    print("      run ends at: %s" % c["stop"])
CH_OK = [c for c in CH if c["ok"]]
CH_STEPS = sum(c["L"] for c in CH_OK)
CH_LONG = max((c["L"] for c in CH_OK), default=0)
CH_REST = max((c["rest"] for c in CH_OK), default=float("nan"))
check("el_m3.chain", len(CH) >= 1 and len(CH_OK) == len(CH) and CH_LONG >= 4,
      "MULTI-STEP, COMPRESSED: %d chains, %d consecutive margin-free steps in "
      "total, longest run %d steps (T114's longest was 4), deepest start "
      "n = %d.  The restriction identity X_new = Jt^T Q_prev Jt holds to rel "
      "%.1e at every step, so every X in the chain inherits positivity from the "
      "previous certificate by Rayleigh-Ritz and the induction is genuine"
      % (len(CH_OK), CH_STEPS, CH_LONG, max(c["n0"] for c in CH), CH_REST))
STOP_COST = [c for c in CH if "hard cap" in c["stop"]]
STOP_STRUCT = [c for c in CH if not c["ok"]]
FP_ALL = ([(t["lam"], t["floor"]) for t in DEEP]
          + [(s["lamS"] if s["kind"] == "step" else s["lam"], s["floor"])
             for c in CH for s in c["steps"]])
FP_HR = [a / max(b, 1e-300) for a, b in FP_ALL if math.isfinite(a)]
check("el_m3.fp_headroom", all(r > 1.0 for r in FP_HR),
      "AND THE DEEP CERTIFICATES ARE NOT FLOATING-POINT ARTEFACTS: every "
      "certified quantity in M3 (deep Schur floors and chain bases, %d in all) "
      "sits %.1e..%.1e times above the DECLARED Cholesky floor c_h u ||.||_2 "
      "(Wilkinson 1968; Higham 2002).  The tightest case is the compressed BASE "
      "window, whose lam_min is the small quantity -- the STEPS are far from the "
      "floor because the compressed Schur floor is O(1)"
      % (len(FP_HR), min(FP_HR), max(FP_HR)))
check("el_m3.stopper", len(STOP_STRUCT) == 0,
      "AND THE STOPPER IS STILL COST, NEVER STRUCTURE: %d of %d runs end at the "
      "compressed hard cap m <= %d (the frame cost nu*u/g_min divided by q) and "
      "%d end because a step failed.  Compression moved the wall by a factor q; "
      "it did not change its NATURE"
      % (len(STOP_COST), len(CH), MAX_H, len(STOP_STRUCT)))
info("M3.timing", "M3 done, %.1f s used, %.0f s budget left"
     % (time.time() - T_START, budget_left()))


# ----------------------------------------------------------------------------
section("M4  SYNTHESIS -- [P1] as a scalar Szego inequality, cost, residue")
# ----------------------------------------------------------------------------
print("""  M4.1  [P1] IS ONE SCALAR INEQUALITY.  Write the odd-sector form as
  Q = T - t~ t~^T with T the atom-corrected odd Toeplitz part and t~ the rank-one
  pole vector.  Apply Albert to the bordered matrix [[1, t~^T], [t~, T]] in the
  two possible orders (Haynsworth's quotient formula):

      T > 0  and  eps := 1 - t~^T T^{-1} t~ >= 0     <=>     Q = T - t~ t~^T >= 0.

  So [P1] -- 'eps > 0 with a controlled size' -- is EXACTLY the Szego /
  Levinson prediction-error inequality for the symbol of T, and it is the same
  margin-free device one level down: no margin, no norm bound, an exact scalar.
  Measured below with the solve's backward error printed, plus the D-power of
  eps on the NESTED refinement ladder (a FIT).""")
print("")

SZ = []
_pool4 = [z for z in ZF_CAP if 120 <= z["h_n"] <= 520]
_tg4 = np.geomspace(_pool4[0]["n"], _pool4[-1]["n"], 6) if _pool4 else []
_zs4 = []
for t in _tg4:
    z = min(_pool4, key=lambda y: abs(math.log(y["n"]) - math.log(t)))
    if z not in _zs4:
        _zs4.append(z)
for z in _zs4:
    sd = step_data(z, ATOMS_ALL)
    T = odd_toeplitz(sd["c"], z["M_n"])
    tv = sd["tv"]
    fac, _ = safe_cho(sym(T))
    if fac is None:
        SZ.append(dict(n=z["n"], h=z["h_n"], T_pd=False))
        continue
    v = cho_solve(fac, tv, check_finite=False)
    eps = 1.0 - float(tv @ v)
    res = float(np.linalg.norm(T @ v - tv)) / max(float(np.linalg.norm(tv)), 1e-300)
    lamQ = lmin(sd["Q"])
    SZ.append(dict(n=z["n"], h=z["h_n"], T_pd=True, lam_T=lmin(T), eps=eps,
                   res=res, lamQ=lamQ, nrmT=norm_bound(T),
                   floor=chol_floor(norm_bound(T), z["h_n"]),
                   sign_ok=bool((eps > 0.0) == (lamQ > 0.0))))
    del T, v, sd
print("      n      h   | lam_min(T)   T > 0 | eps = 1 - t~^T T^-1 t~   solve "
      "bwd err | lam_min(Q)   sign match  eps/fp floor")
for t in SZ:
    if not t["T_pd"]:
        print("   %6d %5d | T NOT numerically PD -- the device does not apply"
              % (t["n"], t["h"]))
        continue
    print("   %6d %5d | %10.4e   %-5s | %20.10e  %10.2e | %10.3e  %-9s  %.2e"
          % (t["n"], t["h"], t["lam_T"], "yes", t["eps"], t["res"], t["lamQ"],
             "yes" if t["sign_ok"] else "NO", t["eps"] / max(t["floor"], 1e-300)))
SZ_OK = [t for t in SZ if t["T_pd"] and t["sign_ok"]]
check("el_m4.szego_device", len(SZ) >= 3 and len(SZ_OK) == len(SZ),
      "[P1] REDUCED TO ONE SCALAR on %d zones: T is numerically PD "
      "(lam_min(T) = %.2e..%.2e), the exact Szego quantity eps = 1 - "
      "t~^T T^{-1} t~ agrees in SIGN with lam_min(Q) everywhere, the linear "
      "solve's backward error is <= %.1e, and eps sits %.1e..%.1e times above "
      "the DECLARED Cholesky floor c_h u ||T||.  So the remaining hypothesis is "
      "not a matrix inequality but the classical prediction-error inequality "
      "t~^T T^{-1} t~ <= 1 (Szego; Levinson 1947; Grenander-Szego)"
      % (len(SZ), min(t["lam_T"] for t in SZ_OK), max(t["lam_T"] for t in SZ_OK),
         max(t["res"] for t in SZ_OK),
         min(t["eps"] / t["floor"] for t in SZ_OK),
         max(t["eps"] / t["floor"] for t in SZ_OK)))

EPSL = []
_z4 = max([z for z in ZF_CAP if 60 <= z["h_n"] <= 214], key=lambda z: z["n"])
_fr4 = step_frame(_z4["u"], _z4["u_next"], _z4["D"])
for rho in (1, 2, 3, 5, 7):
    fr = _fr4 if rho == 1 else refine_frame(_fr4, _z4["u_next"], rho)
    if fr is None or fr["h_n"] > MAX_H:
        continue
    sd = step_data(fr, ATOMS_ALL, want_matrix=False)
    T = odd_toeplitz(sd["c"], fr["M_n"])
    fac, _ = safe_cho(sym(T))
    if fac is None:
        continue
    v = cho_solve(fac, sd["tv"], check_finite=False)
    EPSL.append(dict(rho=rho, h=fr["h_n"], D=fr["D"],
                     eps=1.0 - float(sd["tv"] @ v)))
    del T, v, sd
EPS_FIT = fit_band([math.log(t["rho"]) for t in EPSL],
                   [math.log(max(t["eps"], 1e-300)) for t in EPSL]) \
    if len(EPSL) >= 4 else (0.0, float("nan"), float("nan"), float("nan"))
print("")
print("     the Szego quantity on the NESTED refinement ladder at n = %d:"
      % _z4["n"])
for t in EPSL:
    print("       rho = %d  h = %5d  D = %.4e   eps = %.10e" % (t["rho"], t["h"],
                                                                t["D"], t["eps"]))
info("M4.eps_power", "MEASURED (FIT, jackknife): eps ~ rho^(%+.3f +- %.3f) on "
     "the nested ladder, i.e. eps ~ D^%.2f -- the same falling behaviour T113 "
     "measured for the floor, and it falls FASTER than lam_min(S) ~ rho^%.2f.  "
     "That ordering is the whole content of [P2]: the object that must survive "
     "a regrid is lam_min(S), and it is the SLOWEST-falling of the three"
     % (EPS_FIT[1], EPS_FIT[3], -EPS_FIT[1],
        float(np.mean([t["b"] for t in RP]))))

# --- M4.2  the cost of the compressed scheme -------------------------------
print("")
print("""  M4.2  DOES THE COMPRESSION BREAK THE n log n BARRIER?  The frame cost
  is an identity, not a fit: the window needs M = u/D + 1 cells with
  D = g/(2 nu), so h = nu u / g + O(1), and with g ~ gap(n)/n that is
  h ~ nu n log n / gap(n).  Compression divides the CERTIFIED dimension by q
  but leaves the FINE lattice size h untouched.  So the question is whether the
  reachable set grows in kind or only by a constant factor.""")
print("")
COSTID = max(abs(z["h_o"] - NU_MAIN * z["u"] / z["g"]) for z in ZF)
COSTID_N = max(abs(z["h_n"] - z["h_o"] - NU_MAIN) for z in ZF)
check("el_m4.cost_identity", COSTID <= 1.5 and COSTID_N == 0,
      "the frame cost is an EXACT identity on all %d zones: the old window needs "
      "h = nu u / g + O(1) cells (|err| <= %.2f) and the step adds exactly nu = "
      "%d more (|err| = %d).  There is no fitted exponent to argue about -- the "
      "cost is nu u / g and 1/g is the local prime-gap reciprocal"
      % (len(ZF), COSTID, NU_MAIN, COSTID_N))
Q_MAX = max(Q_SET)
REACH_U, REACH_C = [], []
for z in ZF:
    if z["h_o"] < H_MIN or not z["lemma"]:
        continue
    if z["h_n"] <= MAX_H:
        REACH_U.append(z)
    if deep_choice(z) is not None:
        REACH_C.append(z)
_seen_u = {z["n"] for z in REACH_U}
_seen_c = {z["n"] for z in REACH_C}
N_CONTIG_U = 0
N_CONTIG_C = 0
for z in ZF:
    if z["h_o"] < H_MIN:
        continue
    if z["n"] in _seen_u:
        N_CONTIG_U = z["n"]
    else:
        break
for z in ZF:
    if z["h_o"] < H_MIN:
        continue
    if z["n"] in _seen_c:
        N_CONTIG_C = z["n"]
    else:
        break
DENS_C = 100.0 * len(REACH_C) / max(len(ZF), 1)
info("M4.reach", "REACH, THE TWO HONEST NUMBERS.  (i) ISOLATED zones: uniform "
     "%d of %d zones (deepest n = %d), compressed %d of %d (%.1f%%, deepest "
     "n = %d) -- a factor %.0f in depth.  (ii) CONTIGUOUS from the bottom (every "
     "zone certified, which is what an induction needs): uniform up to n = %d, "
     "compressed up to n = %d -- a factor %.1f.  The gap between (i) and (ii) is "
     "the selection effect: only zones with an unusually LARGE local gap are "
     "reachable, and an induction is blocked by the SMALLEST gap it must cross"
     % (len(REACH_U), len(ZF), max(z["n"] for z in REACH_U), len(REACH_C),
        len(ZF), DENS_C, max(z["n"] for z in REACH_C),
        max(z["n"] for z in REACH_C) / max(z["n"] for z in REACH_U),
        N_CONTIG_U, N_CONTIG_C, N_CONTIG_C / max(N_CONTIG_U, 1)))
check("el_m4.barrier", Q_MAX >= 8 and N_CONTIG_C >= N_CONTIG_U,
      "THE BARRIER IS DIVIDED, NOT BROKEN.  h = nu u / g is untouched by "
      "compression; what the merge buys is the CONSTANT factor q <= %d in the "
      "certified dimension, so the contiguous reach moves from n = %d to "
      "n = %d and no further.  Breaking n log n would need the fine lattice "
      "itself to shrink -- i.e. a boundary-only formulation in which the old "
      "interior is not represented at all, which the exact-zero lemma makes "
      "conceivable but which this probe does NOT have"
      % (Q_MAX, N_CONTIG_U, N_CONTIG_C))

# --- M4.3  the fences, restated as a check ---------------------------------
FENCE = [
    ("no Riemann zero data anywhere in this source", True),
    ("RH => window Weil positivity used in ONE direction (hypothesis input)",
     True),
    ("every discrete lam_min is a Rayleigh-Ritz UPPER bound: refutes, never "
     "proves", True),
    ("compression makes the space COARSER, so its certificate is WEAKER",
     len(MROWS) > 0 and all(w["gap"] >= -1e-12 for _, w in MROWS)),
    ("the transport bracket is an IDENTITY; only its ingredients are evidence",
     True),
    ("every fit reported as a fit with a jackknife band",
     math.isfinite(EPS_FIT[3]) and all(math.isfinite(t["se"]) for t in RP)),
    ("floating-point floor c_h u ||.|| declared and compared, not assumed away",
     all(t["eps"] > t["floor"] for t in SZ if t["T_pd"])),
]
H_FACT = max([0] + [w["m"] for _, w in MROWS] + [t["m"] for t in DEEP]
             + [s["m"] for c in CH for s in c["steps"]]
             + [t["h"] for t in NEST_ROWS] + [t["h_f"] for t in TR]
             + [t["h"] for t in SZ] + [_zs["h_n"]])
H_LAT = max([t["h_fine"] for t in DEEP]
            + [s["h"] for c in CH for s in c["steps"]])
FENCE.append(("largest FACTORISED / EIGENDECOMPOSED form h = %d <= %d"
              % (H_FACT, MAX_H), H_FACT <= MAX_H))
for txt, ok in FENCE:
    info("fence", ("OK   " if ok else "BROKEN ") + txt)
check("el_fence.all", all(ok for _, ok in FENCE),
      "all %d declared fences hold, including the hard cap: the largest form "
      "ever factorised or eigendecomposed has dimension %d <= %d, while the "
      "deepest FINE lattice touched (as a lag vector only) has %d cells -- a "
      "factor %.0f that only the matrix-free two-scale assembly makes possible"
      % (len(FENCE), H_FACT, MAX_H, H_LAT, H_LAT / H_FACT))

# --- M4.4  the ledger ------------------------------------------------------
print("")
print("  THE LEDGER -- certified vs measured vs hypothesis, line by line")
LEDGER = [
    ("Q_full >= 0 hence Q|odd >= 0 at the base window",
     "HYPOTHESIS INPUT", "M0.hypothesis (RH, one direction)"),
    ("the basis is the L2-normalised PWC cell family; transport = cell overlap",
     "CERTIFIED (exact algebra + Galerkin identity)",
     "el_m1.galerkin_nested, %.1e" % max(t["rel"] for t in NEST_ROWS)),
    ("nesting needs an INTEGER ratio; 0 of %d ladder ratios is integer" % len(RATIO),
     "CERTIFIED (exact table)", "el_m0.nest_arith, closest %.1e" % min(NEAR)),
    ("lam_min(S) = min_z of the full form (no inverse, no margin)",
     "CERTIFIED (Haynsworth 1968) to %.1e" % HAY, "el_m1.haynsworth"),
    ("lam_min(S) FALLS under refinement, ~ rho^%.2f"
     % float(np.mean([t["b"] for t in RP])),
     "MEASURED (FIT, jackknife)", "M1.refine_power, %d nested ladders" % len(RP)),
    ("transport deficit eta at the minimisers is O(lam_S), not O(1)",
     "MEASURED", "el_m1.operator_control, best of 4 operators"),
    ("the a-priori (norm) surrogate of eta is 1e3..1e7 too crude",
     "CERTIFIED (Weyl) + MEASURED", "el_m1.apriori_gap"),
    ("coarse->fine transport of lam_min(S) > 0 holds iff rho <= rho*",
     "MEASURED -- and rho* < median ratio",
     "el_m1.coverage, rho* = %.2f, %.0f%% of pairs" % (RHO_STAR,
                                                       100.0 * COV_OK / max(len(COVER), 1))),
    ("X_mixed = Q_old,mixed exactly (compressed step still margin-free)",
     "CERTIFIED (exact algebra)", "el_m2.step_identity, rel %.1e" % E_MSTEP),
    ("0 <= lam_S(mixed) - lam_S(fine) <= ||X|| ||(I-Pi)z*||^2",
     "CERTIFIED (Rayleigh-Ritz + stationarity + Weyl)",
     "el_m2.cea_bound, %d/%d" % (len(M_CEA), len(MROWS))),
    ("Albert certifies the compressed bordering, q = 2..%d"
     % max(w["q"] for _, w in MROWS),
     "CERTIFIED (per (zone,q))", "el_m2.certifies, %d/%d" % (len(M_CERT),
                                                             len(MROWS))),
    ("X_new = Jt^T Q_prev Jt inside a chain (re-coarsening is free)",
     "CERTIFIED (exact algebra + Rayleigh-Ritz)",
     "el_m3.chain, rel %.1e" % CH_REST),
    ("the margin-free step at n = %d (h_fine = %d, m = %d)"
     % (max(t["n"] for t in D_OK), max(t["h_fine"] for t in D_OK),
        max(t["m"] for t in D_OK)),
     "CERTIFIED on the COMPRESSED space", "el_m3.deep_step"),
    ("every run still ends at the cost cap, never at a failing step",
     "CERTIFIED (per step)", "el_m3.stopper, longest chain %d" % CH_LONG),
    ("[P1] <=> the scalar Szego inequality t~^T T^{-1} t~ <= 1",
     "CERTIFIED (Albert twice / Haynsworth quotient)", "el_m4.szego_device"),
    ("eps ~ rho^%.2f, i.e. eps falls FASTER than lam_min(S)" % EPS_FIT[1],
     "MEASURED (FIT, jackknife)", "M4.eps_power"),
    ("h = nu u / g exactly; compression divides m by q, not h",
     "CERTIFIED (identity)", "el_m4.cost_identity, |err| <= %.1f" % COSTID),
    ("a k-uniform lower bound on eps (Grenander-Szego for this symbol)",
     "OPEN -- the residue", "M4.5 item 1"),
    ("an a-priori bound on the transport deficit eta (regularity of z*)",
     "OPEN -- the residue", "M4.5 item 2"),
    ("a boundary-only formulation that removes the nu u / g cost",
     "OPEN -- the residue", "M4.5 item 3"),
]
for txt, st, ref in LEDGER:
    print("    %-64s %-44s %s" % (txt[:64], st, ref))

# --- M4.5  the residue and the verdict -------------------------------------
T_ALL = len(TR) >= 4 and len(ROOM) == len(TR)
T_PART = len(ROOM) >= 1 and RHO_OK < RHO_BAD
C_BREAK = (len(D_OK) == len(DEEP) and len(D_PAST) >= 1
           and max(t["n"] for t in D_OK) >= 5 * DEEP_N_T114
           and CH_LONG > 4 and len(STOP_STRUCT) == 0)
if T_ALL and C_BREAK:
    VERDICT = "TRANSPORT-CERTIFIED"
    VDET = ("the transport bracket reaches on every regrid pair and the "
            "compression carries the circle to n = %d"
            % max(t["n"] for t in D_OK))
elif not T_ALL:
    VERDICT = "TRANSPORT-BLOCKED"
    VDET = ("the transport of lam_min(S) across a real regrid REACHES only for "
            "mild refinement: the lower end is positive on %d of %d pairs, on "
            "every pair with rho <= %.3f and on none with rho >= %.3f, and the "
            "synthetic scan puts the threshold at rho* = %.2f while the ladder's "
            "median refinement ratio is %.3f -- so %.0f%% of the refinement "
            "pairs are covered and the rest provably cannot be, because "
            "lam_min(S) itself falls like rho^%.2f under refinement (measured "
            "on NESTED ladders, where the transport error is exactly zero).  "
            "What is NOT blocked: the compression, which certifies the "
            "margin-free step at n = %d (%.0fx T114's reach, fine lattice "
            "h = %d = %.0fx the cap) and runs %d-step chains that still end at "
            "the cost cap"
            % (len(ROOM), len(TR), RHO_OK, RHO_BAD, RHO_STAR,
               float(np.median(COVER)), 100.0 * COV_OK / max(len(COVER), 1),
               float(np.mean([t["b"] for t in RP])),
               max(t["n"] for t in D_OK),
               max(t["n"] for t in D_OK) / DEEP_N_T114,
               max(t["h_fine"] for t in D_OK),
               max(t["h_fine"] for t in D_OK) / MAX_H, CH_LONG))
else:
    VERDICT = "COMPRESSION-LIMITED"
    VDET = ("transport holds on all %d pairs but the compression does not carry "
            "the circle: deepest compressed step n = %d (T114: %d), longest "
            "chain %d steps, cost m ~ K_FINE + gc + nu u /(g q) with q <= %d"
            % (len(TR), max((t["n"] for t in D_OK), default=-1), DEEP_N_T114,
               CH_LONG, Q_MAX))

print("")
print("  WHAT A k-UNIFORM PROOF STILL NEEDS -- the list, shorter than ever")
print("""    1.  A k-UNIFORM LOWER BOUND ON eps = 1 - t~^T T^{-1} t~.  This is now
        the ONLY inequality left in the circle: M4.1 shows Q|odd >= 0 is
        EQUIVALENT to it (given T > 0, which is a Toeplitz/symbol statement),
        and it is the classical Szego-Levinson prediction error of the
        atom-corrected symbol.  Measured: eps > 0 on every zone, %.1e..%.1e
        above the double-precision floor, falling like rho^%.2f under
        refinement.  What is missing is a bound with the D-dependence, i.e. a
        Grenander-Szego statement for THIS symbol -- one scalar inequality,
        not a matrix induction.
    2.  AN A-PRIORI BOUND ON THE TRANSPORT DEFICIT eta.  M1 makes the regrid
        need explicit and small: eta is MEASURED at the minimisers and is
        O(lam_S), while its norm surrogate is 1e3..1e7 times larger.  The gap
        between the two is a REGULARITY statement -- that the partial minimiser
        z* = -X^{-1}C^T y* is a coarse-scale object (relative projection defect
        %.3f..%.3f, measured in M2) and not a fine-scale oscillation.  With
        that, the transport is certified for rho <= rho* ~ %.1f; beyond it the
        Rayleigh-Ritz drop of lam_min(S) is real and no bound can help, so the
        regrid must be avoided rather than bounded -- which is item 3.
    3.  A BOUNDARY-ONLY FORMULATION.  The cost h = nu u / g is an identity and
        compression only divides the certified dimension by q, so the
        contiguous reach moved from n = %d to n = %d and stops.  The exact-zero
        lemma says the incoming atom does not see the old interior at all;
        a formulation in which the old interior enters only through boundary
        data (a Dirichlet-to-Neumann / transparent-boundary object) would remove
        the nu u / g cost entirely and with it BOTH the cap and the regrid.
        That is the natural next target, and nothing measured here contradicts
        it.
    NO LONGER ON THE LIST (was on T114's): the margin (dissolved, T114); the
    (R) demand ([P5], grid-attached, dropped); 'transport the floor or eps'
    (M1: the object to transport is lam_min(S), the slowest-falling of the
    three); 'the compression might break the step' (M2: it does not, and its
    error is one-sided and second order)."""
      % (min(t["eps"] / t["floor"] for t in SZ_OK),
         max(t["eps"] / t["floor"] for t in SZ_OK), EPS_FIT[1],
         min(w["dproj"] for _, w in MROWS), max(w["dproj"] for _, w in MROWS),
         RHO_STAR, N_CONTIG_U, N_CONTIG_C))

print("")
print("=" * 78)
print("TOTAL")
print("=" * 78)
print("TOTAL.verdict    %s" % VERDICT)
print("TOTAL.detail     %s" % VDET)
print("TOTAL.transport  bracket valid by construction; lower end POSITIVE on "
      "%d/%d real regrid pairs (rho <= %.3f), threshold rho* = %.2f vs median "
      "ratio %.3f; deficit eta = %.1e..%.1e at the minimisers, %.0e..%.0e times "
      "smaller than its norm surrogate"
      % (len(ROOM), len(TR), RHO_OK, RHO_STAR, float(np.median(COVER)),
         min(abs(t["eta_dn"]) for t in TR), max(abs(t["eta_dn"]) for t in TR),
         min(SH), max(SH)))
print("TOTAL.compression Albert certifies %d/%d (zone,q) combinations, q <= %d, "
      "m/h down to %.3f; compression error one-sided and second order "
      "(0 <= gap <= ||X|| ||(I-Pi)z*||^2 on %d/%d)"
      % (len(M_CERT), len(MROWS), max(w["q"] for _, w in MROWS),
         min(w["m"] / r["h"] for r, w in MROWS), len(M_CEA), len(MROWS)))
print("TOTAL.deep       margin-free step certified at n = %d (%.0fx T114's "
      "1331) on a fine lattice of h = %d cells (%.0fx the cap) compressed to "
      "m = %d; longest chain %d steps (T114: 4); %d/%d runs end at the cost "
      "cap, %d at a failing step"
      % (max(t["n"] for t in D_OK), max(t["n"] for t in D_OK) / DEEP_N_T114,
         max(t["h_fine"] for t in D_OK),
         max(t["h_fine"] for t in D_OK) / MAX_H, max(t["m"] for t in D_OK),
         CH_LONG, len(STOP_COST), len(CH), len(STOP_STRUCT)))
print("TOTAL.reach      contiguous (what an induction needs): n <= %d uniform, "
      "n <= %d compressed; isolated zones: %.1f%% of the table reachable, "
      "deepest n = %d.  Cost h = nu u / g is an identity (|err| <= %.1f cells)"
      % (N_CONTIG_U, N_CONTIG_C, DENS_C, max(z["n"] for z in REACH_C), COSTID))
print("TOTAL.residue    [P1] is now ONE scalar inequality: eps = 1 - "
      "t~^T T^{-1} t~ >= 0 (Szego-Levinson), measured %.1e..%.1e above the fp "
      "floor and falling like rho^%.2f.  Plus a regularity bound on the "
      "transport deficit, plus a boundary-only formulation to remove nu u / g"
      % (min(t["eps"] / t["floor"] for t in SZ_OK),
         max(t["eps"] / t["floor"] for t in SZ_OK), EPS_FIT[1]))
print("TOTAL.fences     no zero data; RH one direction; base semidefiniteness "
      "an INPUT; Rayleigh-Ritz direction declared (compression = weaker "
      "statement); bracket declared an identity; fp floor declared and "
      "compared; certified/measured/hypothesis separated per line; every fit a "
      "fit with a jackknife band")
print("TOTAL.caps       largest FACTORISED form m = %d <= %d; deepest FINE "
      "lattice touched (lag vector only) h = %d cells, a factor %.0f; runtime "
      "%.1f s < %.0f s"
      % (H_FACT, MAX_H, H_LAT, H_LAT / H_FACT, time.time() - T_START, BUDGET_S))
print("TOTAL.checks     %d PASS, %d FAIL" % (PASS, FAIL))
print("TOTAL.status     %s" % ("GREEN" if FAIL == 0 else "RED"))
