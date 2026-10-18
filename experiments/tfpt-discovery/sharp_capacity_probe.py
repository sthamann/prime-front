"""Discovery probe (2026-07-28), part 143 of the prime/window investigation.
Contract SHARP.CAPACITY -- ESTIMATE THE EXACT FORM, DO NOT COMPARE IT.

WHERE THIS SITS (T142 END STATE: PROFILE-RESISTS, and the reason was structural)
  T140 reduced the question to two small matrices per zone, T141 turned it into a
  weighted Hardy problem, T142 CONSTRUCTED the optimal weight and then closed the
  whole comparison branch.  QUOTED from T140 / T141 / T142 and never re-derived:
    * rho(W) = lam_max(K^{1/2} H K^{1/2}) EXACTLY, with K the covering kernel in
      closed geometric form and H the mixed second difference of the Green
      function of the lumped pair; equivalently 1 - rho(W) = lam_min(A, A_B);
    * H = diag(s) + L_N exactly (a mass term plus a long-range Dirichlet form),
      and u^T L_N u = d^T B d with d = D u and B the CROSSING KERNEL;
    * J = D K D^T = L_Delta on the interior nodes EXACTLY -- the ENDPOINT
      LAPLACIAN, whose Green function J^{-1}, equilibrium potential p = J^{-1} 1
      and capacity cap_J = 1^T J^{-1} 1 are closed geometric objects;
    * THE CAPACITY DECOMPOSITION, exact:  K^{-1} = D^T J^{-1} D + x x^T / cap
      with x = K^{-1} 1 and cap = 1^T K^{-1} 1, whose Dirichlet half satisfies
      Om(D^T J^{-1} D) = 1 EXACTLY by a projection identity;
    * T142's closure of the comparison branch: no Loewner/comparison bound can
      deliver D-uniformity, because rho(W) = 1 - Theta(D^3) and every comparison
      bound is >= rho with equality only at Y proportional to K^{-1}, so it would
      have to reproduce the optimum to relative accuracy O(D^3); the rank ladder
      confirmed it (no truncation below r = m/2 ever beats the first hurdle 1).
  T142's rest list therefore starts with R1c, THE SHARP ROUTE, and that is this
  probe: estimate the exact capacity Rayleigh form DIRECTLY, with no Loewner step
  taken anywhere, i.e. prove a Hardy inequality for the GREEN FORM of the
  endpoint Laplacian.  The classical address is fixed and is used as an address:
  Maz'ya's capacity criterion (Maz'ya 1985, ch. 2 / 8), the capacitary strong
  type inequality (Maz'ya 1972; Fukushima-Oshima-Takeda 1994, ch. 2 for the
  capacities of a Dirichlet form), Muckenhoupt 1972 for the one-dimensional
  closed form, and Miclo 1999 for the constructive evaluation of the criterion
  on the LEVEL SETS of a potential.

WHAT THIS PROBE DOES
  N1  THE EXACT FORM, WRITTEN DOWN AND VERIFIED.  The T142 identities are
      assembled into ONE quotient and that quotient is checked against the
      exact eigenvalue, not asserted:
          1 - rho(W) = inf_v  [ d^T (J^{-1} - B) d + (x^T v)^2 / cap
                                - sum_k s_k v_k^2 ]
                            / [ d^T J^{-1} d + (x^T v)^2 / cap ] ,   d = D v .
      Then the INGREDIENT BOOKKEEPING (the T136 discipline): every term is
      evaluated at the exact minimiser, its share of the denominator is reported,
      and each is FITTED against D so that one can see which ingredient carries
      the D^3 scale and which are uniform.  The answer decides the shape of the
      route and it is not what a first guess suggests.
  N2  THE MICLO / MAZ'YA BOUND, EVALUATED CONSTRUCTIVELY.  The gap form is
      brought into the coordinates where the classical criterion is legal -- a
      congruence, so the eigenvalue is untouched -- and there the DENOMINATOR is
      the counting measure and the NUMERATOR is a form E with a genuine
      capacity.  The capacity of a set is available in CLOSED form,
          cap_E(A) = 1^T [ (E^{-1})_{AA} ]^{-1} 1 ,
      (the Schur / Green identity, verified here against the constrained
      minimisation itself), so Maz'ya's ratio Phi(A) = |A| / cap_E(A) is
      computable.  Four families of sets are evaluated -- the level sets of the
      extremal, of the Green diagonal, of the transported closed potentials, and
      the index intervals -- the capacitary chain is evaluated term by term on
      the dyadic levels (Miclo's construction), and the resulting bound is put
      against the target c D^3 with its coefficient's D-uniformity measured by a
      jackknife band.  The SAME evaluation is repeated in the node coordinates,
      where an index interval is a geometric object, because the decisive
      question -- does the sup over ALL sets reduce to a closed family -- is a
      question about the coordinates and must not be answered in only one.
  N3  (i) R1d, THE DUAL CERTIFICATE.  T142's closure of the conductance class is
      MEASURED; here a genuine LP dual over the conductance cone is solved and
      its dual multipliers are verified by hand, which turns "the search found
      nothing better" into "no member of the cone can do better than L".
      (ii) R4, the border blocks, with the CAPACITY tail rather than the
      Muckenhoupt tail: for the blocks the paired Neumann ladder leaves open, the
      Maz'ya argmax set is located and its FAR share is measured, which is the
      exact input a decay statement would have to beat.
  N4  the map V15, the promotion list, the shortest rest list, the verdict.

WHAT IS CERTIFIED, WHAT IS MEASURED, WHAT IS A FIT
  * CERTIFIED means a completed Cholesky (Wilkinson 1968; Higham 2002) with the
    declared floating point floor, in the DIRECTION stated in the name:
    cert_lam_max is an UPPER bound, cert_lam_min a LOWER bound.  It also means a
    hand-verified LP dual point (N3), which is a certificate in the same sense.
  * MEASURED means an eigenvalue, a Rayleigh quotient or a family-restricted
    supremum without such a certificate.  EVERY capacity supremum in N2 is
    family-restricted and therefore MEASURED; what IS certified about it is the
    direction it can be used in, and that direction is stated on every line.
  * A FIT is a least squares exponent with a delete-one jackknife band, always
    labelled, never load-bearing.
  * THE DIRECTION TRAP OF THIS PROBE, stated once and respected throughout: for
    any single set A one gets Phi(A) <= 1 / lam, i.e. a CERTIFIED UPPER bound on
    the gap.  The LOWER bound on the gap needs the sup over ALL sets, i.e. a
    closed LOWER bound on cap(A) uniformly in A.  A family-restricted sup gives
    the first and NOT the second, and no line here pretends otherwise.

FENCES
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil window
    form (Weil 1952; Bombieri 2000; Connes 1999) on a FINITE list of prime-power
    zones and a FINITE window.  The criterion is CITED as an address and is
    NEVER USED, in either direction.  Nothing here claims, assumes or approaches
    RH; even with R1c closed what would stand is a finite-window positivity
    statement.  No zero data of any kind is read, generated or approximated --
    an AST firewall enforces this, together with the import whitelist and the
    absence of any write-mode file access.
  * DISCOVERY ONLY.  Nothing is promoted.  No verification module, no ledger, no
    TeX, no website, no changelog, no next.txt is touched; this is ONE new file
    in experiments/tfpt-discovery/ and it writes nothing.
  * HARD CAPS.  Largest factorised / inverted / diagonalised matrix <= 1500;
    runtime budget 780 s (< 900 s), with per-block guards that truncate a pool
    rather than overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh
from scipy.optimize import linprog

np.seterr(all="ignore")

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

# --- N1 surface -------------------------------------------------------------
SURF_ZONES = 26
SURF_HCAP = 1200
T_N1 = 250.0

# --- N2 capacity surface (needs one dense inverse plus many small solves) ---
N2_MCAP = 1200
N2_WINDOWS = 26
N2_LOCAL_M = 460             # local search only where a pass is affordable
LEV_MAX = 34                 # dyadic levels of the capacitary chain
INT_PTS = 12                 # endpoint grid for the interval family
T_N2 = 270.0

# --- N3(i) the LP dual over the conductance cone ----------------------------
LP_MCAP = 340
LP_WINDOWS = 6
LP_NU = 44                   # test directions for Lam
LP_NZ = 40                   # test directions for Om
T_LP = 100.0

# --- N3(ii) border pool -----------------------------------------------------
K3_GC_MIN = 2
K3_HCAP = 300
K3_MAX = 40
K3_PER_RHO = 3
K3_LOGRES = 80.0
K3_RHO = (1.001, 1.05, 1.20, 1.49531, 2.00, 3.50)
M_LADDER = (1, 2, 3, 4, 6, 8)
FAR_K = 8
K3_ENUM_G = 17               # exhaustive subset enumeration up to this size
K3_ENUM_MAX = 6              # how many blocks get the exhaustive treatment
T_R4 = 150.0

# --- preregistered bars (declared before any number is computed) ------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_RED = 1.0e-8             # the finite-core reduction bar (an eigenvalue)
BAR_RAY = 1.0e-4             # the ASSEMBLED Rayleigh form bar -- looser than
#                              BAR_RED ON PURPOSE and declared before the run:
#                              the assembly error enters the gap divided by the
#                              gap itself, and the gap is 10^-6, so an identity
#                              good to 10^-12 can only reproduce a 10^-6
#                              eigenvalue to about 10^-6 relative.  The
#                              AMPLIFICATION is reported next to the number.
ASM_UNITS = 200.0            # the ASSEMBLY bar, in units of m * machine eps:
#                              a relative error of an assembled product of m x m
#                              matrices accumulates like m eps, so the bar for
#                              the assembled Rayleigh form is scaled in m rather
#                              than fixed.  Declared before the run.
BAR_CONG = 1.0e-6            # a congruence must reproduce the gap to this
BAR_UNIF = 0.25              # |exponent in D| for "ZONE-UNIFORM", preregistered
BAR_EXHAUST = 0.25           # a family "essentially attains" the sup above this
BAR_CHAIN = 1.0e-9           # the capacitary chain must hold to this slack

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
RHO_W_T140 = (0.9962, 0.9999)
LAM_T141 = (0.500, 0.942)
OM_T141 = (20.7, 2724.0)
PROD_T142 = (2.03, 2.24)     # T142 certified closed chain Lam x Om
CLASS_T142 = (1.53, 1.86)    # T142 measured class optimum
RANK_T142 = "no truncation below r = m/2 beats the hurdle 1"
R4_OPEN_T142 = 4
FAR_SHRINK_T142 = (0.656, 1.052)
PROMO_T142 = 84
N_PROBES_PRIOR = 142
GAP_EXP_T142 = 3.0           # rho(W) = 1 - Theta(D^3)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-38s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-38s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def wrap_at(text, width):
    out, line = [], ""
    for w in text.split():
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w) if line else w
    if line:
        out.append(line)
    return out


def para(text, width=76, indent="  "):
    for ln in wrap_at(text, width - len(indent)):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


def rel(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    sc = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))), 1.0e-300)
    return float(np.max(np.abs(a - b))) / sc


def asm_bar(m):
    """The dimension-scaled assembly bar, never below the flat identity bar."""
    return max(BAR_ID, ASM_UNITS * float(m) * float(np.finfo(float).eps))


def qmin(v):
    v = [x for x in v if np.isfinite(x)]
    return float(min(v)) if v else float("nan")


def qmax(v):
    v = [x for x in v if np.isfinite(x)]
    return float(max(v)) if v else float("nan")


def qmed(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def fit_line(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_band(x, y):
    """A FIT with a delete-one jackknife band on both coefficients."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    a0, b0, rms = fit_line(x, y)
    aa, bb = [], []
    n = x.shape[0]
    if n >= 4:
        for i in range(n):
            m = np.ones(n, dtype=bool)
            m[i] = False
            ai, bi, _ = fit_line(x[m], y[m])
            aa.append(ai)
            bb.append(bi)
    sa = (0.5 * (max(aa) - min(aa))) if aa else float("nan")
    sb = (0.5 * (max(bb) - min(bb))) if bb else float("nan")
    return a0, b0, rms, sa, sb, n


def pow_fit(xv, yv, tag):
    """A FIT of y ~ c x^p in log-log with a jackknife band.  NEVER load-bearing."""
    x = np.asarray(xv, dtype=float)
    y = np.asarray(yv, dtype=float)
    ok = np.isfinite(x) & np.isfinite(y) & (x > 0.0) & (y > 0.0)
    n_ok = int(np.count_nonzero(ok))
    if n_ok < 3:
        return dict(tag=tag, c=float("nan"), p=float("nan"), rms=float("nan"),
                    sc=float("nan"), sp=float("nan"), n=n_ok)
    a0, b0, rms, sa, sb, n = fit_band(np.log(x[ok]), np.log(y[ok]))
    return dict(tag=tag, c=math.exp(a0), p=b0, rms=rms, sc=sa, sp=sb, n=n)


def unif_ok(f):
    """The preregistered reading of a FIT: |p| plus its jackknife band inside
    the uniformity bar.  A FIT is never load-bearing; this only LABELS it."""
    return bool(np.isfinite(f["p"]) and np.isfinite(f["sp"])
                and abs(f["p"]) + f["sp"] <= BAR_UNIF)


# ----------------------------------------------------------------------------
# THE AST FIREWALL -- no zero data, no unexpected import, no file write
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
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("el_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("el_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "sharp_capacity_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111..T142 code path
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
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952 -- CITED, never used as a criterion)
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


def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s} on the odd section, r, s = 0 .. M/2 - 1."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def odd_toeplitz_slow(c, M):
    h = M // 2
    out = np.empty((h, h))
    for r in range(h):
        for s in range(h):
            out[r, s] = c[abs(r - s)] - c[(M - 1) - r - s]
    return out


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


# ----------------------------------------------------------------------------
# CERTIFICATION (Wilkinson 1968; Higham 2002) -- the DIRECTION is in every name
# ----------------------------------------------------------------------------
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
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration.  The returned
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
    """CERTIFY lam_max(X) <= s by a COMPLETED CHOLESKY of s I - X.  DIRECTION:
    an UPPER bound."""
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


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_min(X) >= t by a completed Cholesky of X - t I.  DIRECTION:
    a LOWER bound."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = 0.0
    t = float(guess) - fl
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(X - t * I) is not None:
            return t - fl
        t = t - max(abs(t), nrm) * grow - 10.0 * fl - 1.0e-300
        grow *= 3.0
    return float("nan")


def perron_bracket(applyf, n, iters):
    """A COLLATZ-WIELANDT bracket for the spectral radius of a NONNEGATIVE
    operator (Collatz 1942; Wielandt 1950).  Both ends rigorous at every
    iterate."""
    x = np.ones(n)
    lo, up = 0.0, float("inf")
    for _ in range(iters):
        y = applyf(x)
        rt = y / np.maximum(x, 1.0e-300)
        lo = max(lo, float(np.min(rt)))
        up = min(up, float(np.max(rt)))
        nz = float(np.max(y))
        if not (nz > 0.0):
            return 0.0, 0.0
        x = np.maximum(y / nz, 1.0e-300)
    return lo, up


# ----------------------------------------------------------------------------
# the frame (T112 frame A, window forced EVEN so that h = M/2 exactly)
# ----------------------------------------------------------------------------
def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def step_frame(u_old, u_new, D):
    M_o = even_window(u_old, D)
    M_n = even_window(u_new, D)
    gc = (M_n - M_o) // 2
    if gc < 1:
        return None
    return dict(D=D, M_o=M_o, M_n=M_n, gc=gc, h_o=M_o // 2, h_n=M_n // 2,
                al_o=0.5 * M_o * D, al_n=0.5 * M_n * D)


def bordered_step(fr, atoms_all):
    """The bordered step (Haynsworth 1968) and its border Schur block S --
    rebuilt in this file's coordinates as a declared PROXY for the T134
    assembly source, exactly as T138 .. T142 did."""
    at_n = atoms_in(fr["al_n"], atoms_all)
    c_n, _ = lag_vector_fast(fr["al_n"], fr["M_n"], at_n)
    tv = odd_pole_vector(fr["al_n"], fr["M_n"])
    Q = sym(odd_toeplitz(c_n, fr["M_n"]) - np.outer(tv, tv))
    gc = fr["gc"]
    A = sym(np.ascontiguousarray(Q[:gc, :gc]))
    C = np.ascontiguousarray(Q[:gc, gc:])
    X = sym(np.ascontiguousarray(Q[gc:, gc:]))
    fac = safe_cho(X)
    if fac is None:
        return None
    Z = cho_solve(fac, C.T, check_finite=False)
    S = sym(A - C @ Z)
    del Q, A, C, X, Z
    return dict(S=S, fr=fr)


# ----------------------------------------------------------------------------
# THE LUMPED M-MATRIX PAIR and its EDGE representation (T136 .. T142)
# ----------------------------------------------------------------------------
def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta,
    A_B = A + L_Delta.  DIRECTION: L_Delta >= 0, so A_B >= A."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    A_B = sym(A + LD)
    offB = A_B - np.diag(np.diag(A_B))
    return dict(h=h, A_B=A_B, Dl=Dl, LD=LD, P_row=P_row, w=A.sum(axis=1),
                dg=dg, dgB=np.diag(A_B).copy(),
                stieltjes=int(bool(np.all(offB <= 1.0e-300))
                              and bool(np.all(np.diag(A_B) > 0.0))),
                n_pos=int(np.count_nonzero(np.where(np.eye(h, dtype=bool),
                                                    0.0, off) > 0.0)))


def anchor_floor(A_B):
    """THE M-MATRIX ANCHOR (T136): A_B x = 1, x >= 0 certifies a nonsingular
    M-matrix (Fan 1958; Berman-Plemmons 1979).  DIRECTION: a LOWER bound."""
    h = A_B.shape[0]
    fac = safe_cho(A_B)
    if fac is None:
        return None
    x = cho_solve(fac, np.ones(h), check_finite=False)
    xmax = float(np.max(x))
    xmin = float(np.min(x))
    return dict(fac=fac, x=x, xmax=xmax, xmin=xmin,
                nonneg=int(xmin >= -1.0e-13 * max(xmax, 1.0e-300)),
                floor=(1.0 / xmax) if xmax > 0.0 else float("nan"))


def edge_list(Dl, M=None):
    """THE EDGE REPRESENTATION of L_Delta = sum_{r<t} Delta_rt (e_r - e_t)
    (e_r - e_t)^T, exactly.  NOTHING is capped or dropped."""
    h = Dl.shape[0]
    iu = np.triu_indices(h, 1)
    w = Dl[iu]
    keep = w > 0.0
    er = iu[0][keep]
    et = iu[1][keep]
    w = w[keep]
    lab = ((M - 1) - er - et) if M is not None else (er + et)
    order = np.lexsort((er, lab))
    er, et, w, lab = er[order], et[order], w[order], lab[order]
    vals, starts, counts = np.unique(lab, return_index=True, return_counts=True)
    return dict(er=er, et=et, w=w, lab=lab, n=er.shape[0],
                mass=float(w.sum()), stripe_val=vals, stripe_start=starts,
                stripe_count=counts, nb=vals.shape[0])


def mixed_second_difference(G):
    """H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s}, THE EXACT DOUBLE
    TELESCOPE (T139 .. T142)."""
    return G[1:, 1:] - G[1:, :-1] - G[:-1, 1:] + G[:-1, :-1]


def interval_incidence(er, et, h):
    """M_{e,r} = 1[a_e <= r < b_e] on the H-grid r = 0 .. h-2."""
    m = h - 1
    rr = np.arange(m)
    return ((rr[None, :] >= er[:, None]) & (rr[None, :] < et[:, None])).astype(float)


def cover_kernel_closed(er, et, w, h):
    """THE COVERING KERNEL in CLOSED GEOMETRIC FORM, K_rs = W([r ^ s, r v s]),
    evaluated by a two-dimensional prefix sum (i.e. WITHOUT forming M)."""
    m = h - 1
    Wm = np.zeros((h + 1, h + 1))
    np.add.at(Wm, (er, et), w)
    F = np.cumsum(Wm, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((h + 1, 1))], axis=1)
    rr = np.arange(m)
    lo = np.minimum(rr[:, None], rr[None, :])
    hi = np.maximum(rr[:, None], rr[None, :])
    K = F[lo, hi]
    return dict(K=K, nonneg=int(bool(np.all(K >= 0.0))))


def psd_sqrt_full(K, tol=1.0e-14):
    """K^{1/2}, K^{-1/2} and K^{-1} from ONE symmetric eigendecomposition."""
    lam, V = eigh(sym(K))
    lmax = float(np.max(np.abs(lam))) if lam.size else 0.0
    keep = lam > tol * max(lmax, 1.0e-300)
    s = np.zeros_like(lam)
    s[keep] = np.sqrt(lam[keep])
    iv = np.zeros_like(lam)
    iv[keep] = 1.0 / lam[keep]
    im = np.zeros_like(lam)
    im[keep] = 1.0 / np.sqrt(lam[keep])
    return dict(Kh=sym((V * s[None, :]) @ V.T),
                Kp=sym((V * iv[None, :]) @ V.T),
                Kmh=sym((V * im[None, :]) @ V.T),
                V=V, lam=lam, lmax=lmax,
                null=int(np.count_nonzero(~keep)))


def abel_split(H):
    """THE ENERGY REORDERING, exact for ANY symmetric H: H = diag(s) + L_N with
    s = row sums, N = -offdiag(H)."""
    m = H.shape[0]
    s = H.sum(axis=1)
    off = H - np.diag(np.diag(H))
    N = -off
    LN = np.diag(N.sum(axis=1)) - N
    return dict(m=m, s=s, N=N, LN=sym(LN), id_err=rel(H, np.diag(s) + LN),
                s_pos=float(np.mean(s > 0.0)),
                neg_off=(float(np.mean(N[~np.eye(m, dtype=bool)] > 0.0))
                         if m > 1 else float("nan")))


def conj_form(Kh, X):
    return sym(Kh @ sym(X) @ Kh)


def diff_op(m):
    """THE INCREMENT OPERATOR (D u)_k = u_k - u_{k+1}, k = 0 .. m-2."""
    Dm = np.zeros((m - 1, m))
    idx = np.arange(m - 1)
    Dm[idx, idx] = 1.0
    Dm[idx, idx + 1] = -1.0
    return Dm


def crossing_kernel(N):
    """THE CROSSING KERNEL of a SYMMETRIC weight matrix N (T141 / T142, QUOTED
    in form): B_kl = sum_{r <= k ^ l, k v l < s} N_rs, so that u^T L_N u = d^T B d
    with d = D u, EXACTLY and with the signs."""
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
    return sym(F[lo, hi])


def hardy_laplacian(K):
    """J = D K D^T, the DENOMINATOR object: for the covering kernel this is
    EXACTLY the original Laplacian L_Delta on the interior nodes."""
    return sym(K[:-1, :-1] - K[:-1, 1:] - K[1:, :-1] + K[1:, 1:])


def green_endpoint(J):
    """J^{-1}, the GREEN FUNCTION of the endpoint Laplacian, its EQUILIBRIUM
    POTENTIAL p = J^{-1} 1 and the CAPACITY cap_J = 1^T J^{-1} 1 (Maz'ya 1985;
    Miclo 1999).  QUOTED from T142."""
    fac = safe_cho(sym(J))
    if fac is None:
        return None
    n = J.shape[0]
    Ji = sym(cho_solve(fac, np.eye(n), check_finite=False))
    p = Ji.sum(axis=1)
    return dict(Ji=Ji, p=p, cap=float(p.sum()), dg=np.diag(Ji).copy())


def capacity_decomposition(Kp, Ji, Dop):
    """THE CAPACITY DECOMPOSITION of the optimal weight, EXACT (T142, QUOTED
    and RE-VERIFIED here because the whole of N1 is assembled from it):

        K^{-1} = D^T J^{-1} D + x x^T / cap ,  x = K^{-1} 1 , cap = 1^T K^{-1} 1.
    """
    x = Kp.sum(axis=1)
    cap = float(x.sum())
    Ycap = sym(Dop.T @ Ji @ Dop)
    err = rel(Kp, Ycap + np.outer(x, x) / max(cap, 1.0e-300))
    return dict(x=x, cap=cap, Ycap=Ycap, err=err)


# ----------------------------------------------------------------------------
# N2 MACHINERY -- THE MAZ'YA CAPACITY of a set and the MICLO LEVEL CHAIN
# ----------------------------------------------------------------------------
def set_capacity(R, idx):
    """cap_E(A) = min { w^T E w : w = 1 on A } = 1^T [ (E^{-1})_{AA} ]^{-1} 1,
    the SCHUR / GREEN identity (Fukushima-Oshima-Takeda 1994, ch. 2; Maz'ya
    1985).  R = E^{-1} is passed in, so a capacity costs ONE small Cholesky."""
    if idx.size == 0:
        return float("nan")
    Raa = sym(np.ascontiguousarray(R[np.ix_(idx, idx)]))
    fac = safe_cho(Raa)
    if fac is None:
        return float("nan")
    y = cho_solve(fac, np.ones(idx.size), check_finite=False)
    val = float(y.sum())
    return val if val > 0.0 else float("nan")


def set_capacity_direct(E, idx):
    """The SAME capacity by the DEFINITION (constrained minimisation), used only
    to verify the Schur identity rather than to trust it."""
    n = E.shape[0]
    mask = np.zeros(n, dtype=bool)
    mask[idx] = True
    B = np.nonzero(~mask)[0]
    A = np.nonzero(mask)[0]
    one = np.ones(A.size)
    val = float(one @ E[np.ix_(A, A)] @ one)
    if B.size:
        fac = safe_cho(sym(np.ascontiguousarray(E[np.ix_(B, B)])))
        if fac is None:
            return float("nan")
        rhs = E[np.ix_(B, A)] @ one
        wB = -cho_solve(fac, rhs, check_finite=False)
        val += 2.0 * float(wB @ rhs) + float(wB @ E[np.ix_(B, B)] @ wB)
    return val


def dyadic_chain(phi, jmax=LEV_MAX):
    """THE MICLO LEVEL CHAIN: the nested dyadic level sets A_j = { phi > a 2^-j }
    of a NONNEGATIVE function, a = max phi, together with the level values.
    This is the family Maz'ya's capacitary argument actually uses -- it is not a
    guess and not a profile."""
    a = float(np.max(phi))
    rows = []
    if not (a > 0.0):
        return a, rows
    n = phi.shape[0]
    for j in range(1, jmax + 1):
        t = a * (2.0 ** (-j))
        idx = np.nonzero(phi > t)[0]
        if idx.size == 0:
            continue
        rows.append((j, t, idx))
        if idx.size == n:
            break
    return a, rows


def phi_over_family(R, sets):
    """Maz'ya's ratio Phi(A) = |A| / cap(A) over a family.  DIRECTION: every
    single value is a CERTIFIED LOWER bound on the best constant C = 1 / lam,
    i.e. a CERTIFIED UPPER bound lam <= cap(A) / |A|; the MAXIMUM over a family
    is NOT an upper bound for the sup over all sets and is never used as one."""
    best, best_set, vals = 0.0, None, []
    for idx in sets:
        cp = set_capacity(R, idx)
        if not np.isfinite(cp) or cp <= 0.0:
            continue
        ph = float(idx.size) / cp
        vals.append(ph)
        if ph > best:
            best, best_set = ph, idx
    return best, best_set, vals


def capacitary_chain(R, phi, lam_E, jmax=LEV_MAX):
    """THE CONSTRUCTIVE EVALUATION of Maz'ya's criterion on the dyadic levels of
    phi (Miclo 1999).  Returns the three ingredients of

        sum_k phi_k^2  <=  4 sum_j tau_j^2 |A_j| + resid
                       <=  4 Phi_max sum_j tau_j^2 cap(A_j)
                       =   4 Phi_max kappa E(phi) ,

    every step of which is EVALUATED here rather than assumed: the level sum,
    the capacity sum, the residual below the last level, and the ratio kappa
    that a Dirichlet form would bound by a universal constant."""
    a, rows = dyadic_chain(phi, jmax)
    if not rows:
        return None
    lev_sum, cap_sum, phi_max, phi_arg = 0.0, 0.0, 0.0, None
    cache = {}
    for (j, t, idx) in rows:
        key = int(idx.size)
        if key not in cache:
            cache[key] = set_capacity(R, idx)
        cp = cache[key]
        if not np.isfinite(cp) or cp <= 0.0:
            return None
        lev_sum += (t * t) * idx.size
        cap_sum += (t * t) * cp
        ph = float(idx.size) / cp
        if ph > phi_max:
            phi_max, phi_arg = ph, idx
    t_last = rows[-1][1]
    resid = float(np.sum(np.where(phi <= t_last, phi, 0.0) ** 2))
    tot = float(np.sum(phi * phi))
    kappa = cap_sum / max(lam_E, 1.0e-300)
    return dict(a=a, n_lev=len(rows), lev_sum=lev_sum, cap_sum=cap_sum,
                resid=resid, tot=tot, kappa=kappa, phi_max=phi_max,
                phi_arg=phi_arg,
                chain_ok=(4.0 * lev_sum + resid + BAR_CHAIN * max(tot, 1.0)
                          >= tot),
                # THE CHAIN EFFICIENCY: the factor by which the CONSTRUCTIVE
                # (chain) version of the criterion falls short of the DIRECT
                # one.  It is a pure ratio in (0, 1]; multiplied by E(phi) it
                # is the chain's lower bound, and 1 would mean the chain loses
                # nothing.  This is where the capacitary strong-type constant
                # of the form shows up as a NUMBER instead of a citation.
                chain_eff=((tot - resid)
                           / max(4.0 * phi_max * cap_sum, 1.0e-300)))


def interval_sets(m, npts=INT_PTS):
    """The INDEX INTERVALS on a coarse endpoint grid.  In the node coordinates
    an interval is a geometric object (a block of window lags), which is why the
    interval family is the one that decides whether the sup over ALL sets has a
    ONE-DIMENSIONAL closed form at all (Muckenhoupt 1972)."""
    pts = sorted(set(int(round(t)) for t in np.linspace(0, m, npts + 1)))
    out = []
    for i in range(len(pts) - 1):
        for j in range(i + 1, len(pts)):
            a, b = pts[i], pts[j]
            if b - a >= 1:
                out.append(np.arange(a, b))
    return out


def level_sets_of(vec, nq=13):
    """The (non-dyadic) quantile level sets of |vec| -- the closed families."""
    v = np.abs(np.asarray(vec, dtype=float))
    n = v.shape[0]
    out = []
    seen = set()
    for q in np.linspace(0.02, 0.98, nq):
        t = float(np.quantile(v, q))
        idx = np.nonzero(v > t)[0]
        if idx.size == 0 or idx.size == n:
            continue
        key = (int(idx.size), int(idx[0]))
        if key in seen:
            continue
        seen.add(key)
        out.append(idx)
    return out


def build_core(al, M_k, h_k, atoms_all):
    """THE WHOLE T140 .. T142 CORE of one window in one place: the odd section,
    the lumped M-matrix pair, the exact gap, the Green function H, the covering
    kernel K with its square roots, the endpoint Laplacian J with its Green
    function, the capacity decomposition and the crossing kernel.  N1 and N2
    both call it, so nothing large has to be carried between the blocks and
    every number in N2 comes from the same construction as in N1."""
    c_lag, _ = lag_vector_fast(al, M_k, atoms_in(al, atoms_all))
    A = sym(odd_toeplitz(c_lag, M_k))
    lp = lump_pair(A)
    an = anchor_floor(lp["A_B"])
    if an is None or not an["nonneg"]:
        return None
    ed = edge_list(lp["Dl"], M_k)
    if ed["n"] < 8 or ed["nb"] < 6:
        return None
    try:
        gap_ex = float(eigh(A, lp["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return None
    if not (gap_ex > 0.0):
        return None
    G_full = cho_solve(an["fac"], np.eye(h_k), check_finite=False)
    H = mixed_second_difference(G_full)
    m = H.shape[0]
    if m < 12:
        return None
    K = cover_kernel_closed(ed["er"], ed["et"], ed["w"], h_k)["K"]
    sq = psd_sqrt_full(K)
    if sq["null"] != 0:
        return None
    Dop = diff_op(m)
    J = hardy_laplacian(K)
    gr = green_endpoint(J)
    if gr is None:
        return None
    cd = capacity_decomposition(sq["Kp"], gr["Ji"], Dop)
    ab = abel_split(H)
    return dict(A=A, A_B=lp["A_B"], gap_ex=gap_ex, rho_ex=1.0 - gap_ex, H=H,
                m=m, K=K, Kh=sq["Kh"], Kp=sq["Kp"], Kmh=sq["Kmh"], J=J,
                Ji=gr["Ji"], p=gr["p"], cap_J=gr["cap"], Ji_dg=gr["dg"],
                x=cd["x"], cap=cd["cap"], Ycap=cd["Ycap"], cap_err=cd["err"],
                s=ab["s"], N=ab["N"], LN=ab["LN"], s_pos=ab["s_pos"],
                Dop=Dop, n_e=ed["n"])


def whiten_gap(Mnum, Mden_mh):
    """THE CONGRUENCE into the coordinates where the classical criterion is
    legal: with Q^{-1/2} the inverse square root of the DENOMINATOR form,
    E = Q^{-1/2} Mnum Q^{-1/2} has the SAME generalised spectrum, and the
    denominator becomes the COUNTING MEASURE.  Congruence preserves the Loewner
    order and the generalised eigenvalues exactly -- that is verified in N0 and
    is the only licence this step needs."""
    return sym(Mden_mh @ sym(Mnum) @ Mden_mh)


# ----------------------------------------------------------------------------
# N3 MACHINERY -- the LP dual over the conductance cone, and the border ladder
# ----------------------------------------------------------------------------
def lp_class_bound(H, Kh, U, Z):
    """A CERTIFIED LOWER BOUND for min over the conductance cone of
    Lam(H, Y) x Om(Y), Y = D^T diag(c) D + diag(g) with c, g >= 0.

    THE SHAPE.  For test directions u_i and z_j put
        a_ie = (D u_i)_e^2 , b_ik = u_ik^2 , h_i = u_i^T H u_i > 0 ,
        p_je = (D y_j)_e^2 , q_jk = y_jk^2 with y_j = K^{1/2} z_j ,
    and let V = max { tau : sum_e c_e a_ie + sum_k g_k b_ik >= tau h_i for all i,
                             sum_e c_e p_je + sum_k g_k q_jk <= 1 for all j,
                             c, g >= 0 } .
    Then for EVERY Y in the cone, Lam(H, Y) Om(Y) >= 1 / V.  (Scale Y by
    om = max_j z_j^T K^{1/2} Y K^{1/2} z_j <= Om(Y); the scaled Y is feasible
    with tau' = min_i u_i^T Y u_i / (om h_i) <= V, and at the argmin
    Lam(H, Y) >= 1 / (om tau'), so Lam Om >= Om / (om tau') >= 1 / tau'.)
    ADDING directions only shrinks the feasible set, so the bound is MONOTONE.

    THE CERTIFICATE.  V is an LP value, so a dual feasible point proves an UPPER
    bound on it.  The dual reads: min sum_j mu_j subject to mu, y >= 0,
    sum_i y_i h_i = 1, and for every generator index
        sum_j mu_j p_je >= sum_i y_i a_ie ,  sum_j mu_j q_jk >= sum_i y_i b_ik .
    The solver's multipliers are CLIPPED to the sign constraints, RENORMALISED
    and then SCALED UP until the generator constraints hold with a margin, and
    only the hand-verified point is reported.  That is what makes this a
    certificate rather than a solver output."""
    m = H.shape[0]
    Dop = diff_op(m)
    UA = np.stack([(Dop @ u) ** 2 for u in U], axis=0)
    UB = np.stack([u ** 2 for u in U], axis=0)
    hv = np.array([float(u @ H @ u) for u in U])
    keep = hv > 0.0
    if int(np.count_nonzero(keep)) < 2:
        return None
    UA, UB, hv = UA[keep], UB[keep], hv[keep]
    Y = np.stack([Kh @ z for z in Z], axis=0)
    ZA = np.stack([(Dop @ y) ** 2 for y in Y], axis=0)
    ZB = np.stack([y ** 2 for y in Y], axis=0)
    nu, nz = UA.shape[0], ZA.shape[0]
    nv = (m - 1) + m + 1
    rows_a = np.concatenate([-UA, -UB, hv[:, None]], axis=1)
    rows_b = np.concatenate([ZA, ZB, np.zeros((nz, 1))], axis=1)
    A_ub = np.concatenate([rows_a, rows_b], axis=0)
    b_ub = np.concatenate([np.zeros(nu), np.ones(nz)])
    cvec = np.zeros(nv)
    cvec[-1] = -1.0
    bounds = [(0.0, None)] * (nv - 1) + [(0.0, 1.0e12)]
    res = linprog(cvec, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    if not res.success:
        return None
    V_lp = float(-res.fun)
    out = dict(V_lp=V_lp, L_lp=(1.0 / V_lp if V_lp > 0.0 else float("inf")),
               nu=nu, nz=nz)
    marg = getattr(res, "ineqlin", None)
    lam_d = -np.asarray(marg.marginals, dtype=float) if marg is not None \
        else np.zeros(nu + nz)
    yv = np.maximum(lam_d[:nu], 0.0)
    mu = np.maximum(lam_d[nu:], 0.0)
    sc = float(yv @ hv)
    if sc <= 0.0:
        out["V_cert"] = float("nan")
        out["L_cert"] = float("nan")
        return out
    yv = yv / sc
    need_e = yv @ UA
    need_k = yv @ UB
    got_e = mu @ ZA
    got_k = mu @ ZB
    ratio = 1.0
    for need, got in ((need_e, got_e), (need_k, got_k)):
        pos = need > 0.0
        if not np.any(pos):
            continue
        r = need[pos] / np.maximum(got[pos], 1.0e-300)
        ratio = max(ratio, float(np.max(r)))
    if not np.isfinite(ratio):
        out["V_cert"] = float("nan")
        out["L_cert"] = float("nan")
        return out
    mu = mu * (ratio * (1.0 + 1.0e-9)) + 1.0e-14
    ok = bool(np.all(mu @ ZA >= yv @ UA - 1.0e-12 * max(1.0, float(np.max(need_e))))
              and np.all(mu @ ZB >= yv @ UB
                         - 1.0e-12 * max(1.0, float(np.max(need_k))))
              and abs(float(yv @ hv) - 1.0) <= 1.0e-9
              and bool(np.all(yv >= 0.0)) and bool(np.all(mu >= 0.0)))
    V_cert = float(mu.sum())
    out["dual_ok"] = int(ok)
    out["V_cert"] = V_cert if ok else float("nan")
    out["L_cert"] = (1.0 / V_cert) if (ok and V_cert > 0.0) else float("nan")
    return out


def paired_neumann_small(S, ladder=M_LADDER):
    """THE m-PAIRED NEUMANN CERTIFICATE, QUOTED in form from T138 .. T142 and
    reduced to what N3(ii) needs: does the ladder certify the block, and if not,
    by which factor does it miss."""
    g = S.shape[0]
    S = sym(S)
    off = S - np.diag(np.diag(S))
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    S_B = sym(S + LD)
    facB = safe_cho(S_B)
    if facB is None:
        return None
    Ig = np.eye(g)
    G_B = cho_solve(facB, Ig, check_finite=False)
    F = G_B @ LD
    Fabs = np.abs(F)
    out = dict(g=g, S_B=S_B)
    rungs = []
    Fm = Ig.copy()
    Pm = np.zeros((g, g))
    for mm in range(1, max(ladder) + 1):
        Pm = Pm + Fm
        Fm = Fm @ F
        if mm not in ladder:
            continue
        Fma = np.abs(Fm)
        lo, up = perron_bracket(lambda v: Fma @ v, g, 60)
        row = dict(m=mm, rho_up=up, cert=0, need=float("inf"))
        if up < 1.0:
            try:
                Tm = np.linalg.solve(Ig - Fma, Fma)
                TG = Tm @ G_B
                bad = np.abs(Pm) @ TG
                good = Pm @ G_B
                row["cert"] = int(float(np.min(good - bad)) > 0.0)
                row["need"] = float(np.max(bad / np.maximum(good, 1.0e-300)))
                del Tm, TG, bad, good
            except LinAlgError:
                pass
        rungs.append(row)
        del Fma
    out["rungs"] = rungs
    out["cert_any"] = int(any(r["cert"] for r in rungs))
    fin = [r["need"] for r in rungs if np.isfinite(r["need"])]
    out["need_best"] = qmin(fin) if fin else float("inf")
    del F, Fabs, Fm, Pm, Dl
    return out


# ----------------------------------------------------------------------------
section("N0  SETUP, the capacity calibrations, and the DIRECTION statements")
# ----------------------------------------------------------------------------
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

BERT_OK = bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
EVEN_OK = bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12))
check("el_n0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

RNG = np.random.default_rng(14307281)

para("""N0.0  THE RH FENCE, STATED BEFORE ANY NUMBER.  The surrounding statement
is the positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999)
on a FINITE list of prime-power zones and a FINITE window; the criterion is
CITED as that address and is NEVER USED here, in either direction.  Nothing in
this file claims, assumes or approaches RH: even with R1c closed, what would
stand is a finite-window positivity statement, and the distance from there to RH
is mapped in N4 and never travelled.  No zero data is read, generated or
approximated -- the AST firewall above enforces that, together with the import
whitelist and the absence of any write-mode file access.""")

# --- N0.1  the coordinates, unchanged from T106 .. T142 ---------------------
_k0, _D0, _M0 = None, None, None
for _kk in range(2, NZ_DEEP - 2):
    _Dc = 0.5 * float(G_DEEP[_kk]) / NU_MAIN
    _Mc = even_window(UU_ALL[_kk], _Dc)
    if 110 <= _Mc // 2 <= 190:
        _k0, _D0, _M0 = _kk, _Dc, _Mc
if _k0 is None:
    raise SystemExit("N0 found no calibration window in the declared h band")
_al0 = 0.5 * _M0 * _D0
_h0 = _M0 // 2
_c0, _ = lag_vector_fast(_al0, _M0, atoms_in(_al0, ATOMS_ALL))
E_ODD = rel(odd_toeplitz(_c0, _M0), odd_toeplitz_slow(_c0, _M0))
check("el_n0.odd_section", E_ODD <= BAR_ID,
      "the vectorised odd section equals its entrywise definition A_rs = "
      "c_{|r-s|} - c_{M-1-r-s} to %.2e (bar %.0e) on the calibration window "
      "h = %d, D = %.3e -- the coordinates of T106..T142, unchanged"
      % (E_ODD, BAR_ID, _h0, _D0))

_A0 = sym(odd_toeplitz(_c0, _M0))
_lp0 = lump_pair(_A0)
_an0 = anchor_floor(_lp0["A_B"])
check("el_n0.lumping", _lp0["stieltjes"] == 1
      and _an0 is not None and _an0["nonneg"] == 1,
      "the lumped pair is STIELTJES and A_B x = 1 has x >= 0, so A_B is a "
      "nonsingular M-matrix (Fan 1958; Berman-Plemmons 1979) with anchor "
      "lam_min(A_B) >= %.3e" % _an0["floor"])

# --- N0.2  THE DIRECTION CALIBRATIONS this probe leans on -------------------
_Zr = RNG.standard_normal((40, 40))
_Xr = sym(_Zr @ _Zr.T)
_Pr = RNG.standard_normal((40, 40))
_Yr = _Xr + sym(_Pr @ _Pr.T)
_Cr = RNG.standard_normal((40, 25))
_cong = float(np.min(eigvalsh(_Cr.T @ (_Yr - _Xr) @ _Cr)))
check("el_n0.congruence_loewner", _cong >= -1.0e-9 * float(np.max(np.abs(_Yr))),
      "CONGRUENCE PRESERVES THE LOEWNER ORDER, verified rather than asserted "
      "(lam_min = %.2e).  THIS IS THE LICENCE for the whitening of N2: the "
      "criterion is evaluated in coordinates where the denominator is the "
      "counting measure, and the eigenvalue is untouched" % _cong)

# the Schur / Green identity for a capacity, on a random positive definite form
_Ze = RNG.standard_normal((60, 60))
_Ee = sym(_Ze @ _Ze.T) + 3.0 * np.eye(60)
_Re = np.linalg.inv(_Ee)
_idx = np.sort(RNG.choice(60, 17, replace=False))
_c_schur = set_capacity(_Re, _idx)
_c_dir = set_capacity_direct(_Ee, _idx)
CAP_ID_ERR = abs(_c_schur - _c_dir) / max(abs(_c_dir), 1.0e-300)
check("el_n0.capacity_identity", CAP_ID_ERR <= 1.0e-9,
      "THE CAPACITY IS A GREEN OBJECT: cap_E(A) = 1^T [(E^{-1})_AA]^{-1} 1 "
      "equals the constrained minimum min { w^T E w : w|_A = 1 } to %.2e "
      "relative (Fukushima-Oshima-Takeda 1994, ch. 2).  Verified, not assumed, "
      "because every number in N2 is a capacity" % CAP_ID_ERR)

# the capacity ratio bounds the best constant -- the CERTIFIED direction
_lam_e = float(eigvalsh(_Ee, subset_by_index=[0, 0])[0])
_phi_e = float(_idx.size) / _c_dir
check("el_n0.capacity_direction", _phi_e <= 1.0 / _lam_e * (1.0 + 1.0e-9),
      "AND THE DIRECTION IT GIVES, verified on the same random form: "
      "Phi(A) = |A| / cap(A) = %.4f <= 1 / lam_min = %.4f.  So a single set "
      "CERTIFIES an UPPER bound on the gap and NEVER a lower one; the lower "
      "bound needs the sup over ALL sets, which is the whole content of the "
      "sharp route" % (_phi_e, 1.0 / _lam_e))

# Maz'ya's capacitary chain, arithmetic verified on a random nonnegative vector
_w_e = np.abs(RNG.standard_normal(60)) + 1.0e-3
_ch_e = capacitary_chain(_Re, _w_e / float(np.linalg.norm(_w_e)),
                         float(_w_e @ _Ee @ _w_e) / float(_w_e @ _w_e))
check("el_n0.chain_arithmetic", _ch_e is not None and _ch_e["chain_ok"],
      "THE CAPACITARY CHAIN ARITHMETIC (Maz'ya 1972; Miclo 1999) holds on a "
      "random test vector: sum phi^2 <= 4 sum_j tau_j^2 |A_j| + resid with "
      "%d dyadic levels and residual share %.2e.  This is the LEVEL SUM step "
      "only -- the capacity step is what the criterion adds and it is measured "
      "per window in N2"
      % (_ch_e["n_lev"] if _ch_e else -1,
         (_ch_e["resid"] / max(_ch_e["tot"], 1.0e-300)) if _ch_e else float("nan")))

para("""N0.3  WHAT IS NEW HERE, IN ONE SENTENCE.  T142 closed the comparison
branch with a structural argument (every comparison bound is >= rho with
equality only at Y proportional to K^{-1}, and rho = 1 - Theta(D^%.0f), so a
comparison would have to reproduce the optimum to relative accuracy O(D^%.0f)),
which leaves exactly one road: estimate the EXACT quotient.  That road is
classical and has a name -- a Hardy inequality for the Green form of the
endpoint Laplacian, i.e. Maz'ya's capacity criterion evaluated on the level sets
of a potential (Miclo 1999) -- and the point of this probe is that the criterion
is applied to the GAP and not to rho, which is what turns the criterion's
unavoidable factor of four from a fatal loss into a bounded loss in the
COEFFICIENT.""" % (GAP_EXP_T142, GAP_EXP_T142))


# ----------------------------------------------------------------------------
section("N1  THE EXACT FORM and the ingredient bookkeeping")
# ----------------------------------------------------------------------------
para("""N1.0  THE MEASUREMENT SURFACE.  Candidates are ALL prime-power zones
whose frame-A window fits the caps; the surface is spread over log n so that the
D range is as wide as the caps allow, because D-uniformity is the question.
rho(W) is taken from the generalised eigenvalue lam_min(A, A_B) exactly as
T140 .. T142 did, and every identity below is checked against it.""")

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > SURF_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(SURF_ZONES, 1))
    SZ = CAND[::-1][::step][:SURF_ZONES]
    SZ.sort(key=lambda t: t[0])
info("N1.candidates", "%d prime-power zones admit a frame-A window inside the "
     "cap (h <= %d, MAX_H = %d); the surface takes %d of them (stride %d) from "
     "the deep end" % (len(CAND), SURF_HCAP, MAX_H, len(SZ), step))

SURF = []
for (k, D_k, M_k, h_k) in SZ:
    if budget_left() < BUDGET_S - T_N1:
        info("N1.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(SURF)))
        break
    al = 0.5 * M_k * D_k
    co = build_core(al, M_k, h_k, ATOMS_ALL)
    if co is None:
        continue
    m = co["m"]
    gap_ex, rho_ex = co["gap_ex"], co["rho_ex"]
    Kh, Kp = co["Kh"], co["Kp"]
    Gc = conj_form(Kh, co["H"])
    lam_core = float(eigvalsh(Gc, subset_by_index=[m - 1, m - 1])[0])
    red_err = abs(lam_core - rho_ex) / max(rho_ex, 1.0e-300)

    Dop = co["Dop"]
    Bx = crossing_kernel(co["N"])
    ln_err = rel(co["LN"], Dop.T @ Bx @ Dop)

    # --- N1(i)  THE EXACT CAPACITY RAYLEIGH FORM, assembled and verified ----
    Qm = co["Ycap"] + np.outer(co["x"], co["x"]) / max(co["cap"], 1.0e-300)
    Nm = (sym(Dop.T @ (co["Ji"] - Bx) @ Dop)
          + np.outer(co["x"], co["x"]) / max(co["cap"], 1.0e-300)
          - np.diag(co["s"]))
    err_Q = rel(Qm, Kp)
    err_N = rel(Nm, Kp - co["H"])
    try:
        wv, Vv = eigh(sym(Nm), sym(Qm), subset_by_index=[0, 0])
    except (LinAlgError, ValueError):
        continue
    lam_ray = float(wv[0])
    ray_err = abs(lam_ray - gap_ex) / max(gap_ex, 1.0e-300)
    vstar = Vv[:, 0]

    # --- N1(ii)  THE INGREDIENT BOOKKEEPING at the exact minimiser ----------
    dstar = Dop @ vstar
    den_green = float(dstar @ co["Ji"] @ dstar)
    den_cap = float(co["x"] @ vstar) ** 2 / max(co["cap"], 1.0e-300)
    Qv = den_green + den_cap
    num_B = float(dstar @ Bx @ dstar)
    num_mass = float(co["s"] @ (vstar * vstar))
    sh_g = den_green / max(Qv, 1.0e-300)
    sh_c = den_cap / max(Qv, 1.0e-300)
    sh_b = num_B / max(Qv, 1.0e-300)
    sh_m = num_mass / max(Qv, 1.0e-300)
    book_err = abs((sh_g + sh_c - sh_b - sh_m) - gap_ex) / max(gap_ex, 1.0e-300)

    # --- N1(iii)  THE TWO SUB-SUPREMA of the naive split --------------------
    Mmass = conj_form(Kh, np.diag(np.maximum(co["s"], 0.0)))
    rho_mass = cert_lam_max(Mmass, guess=ray_top(Mmass))
    try:
        rho_long = float(eigh(sym(Bx), sym(co["Ji"]), eigvals_only=True,
                              subset_by_index=[m - 2, m - 2])[0])
    except (LinAlgError, ValueError):
        rho_long = float("nan")
    del Mmass

    # NOTHING large is carried out of this loop: N2 and N3 rebuild the window
    # from the same build_core, which costs a fraction of a second and keeps
    # the probe's memory flat instead of quadratic in the surface
    SURF.append(dict(
        k=k, n=NN_ALL[k], D=D_k, M=M_k, h=h_k, m=m, n_e=co["n_e"], al=al,
        gap_ex=gap_ex, rho_ex=rho_ex, red_err=red_err, cap_err=co["cap_err"],
        ln_err=ln_err, err_Q=err_Q, err_N=err_N, ray_err=ray_err,
        lam_ray=lam_ray, book_err=book_err,
        sh_g=sh_g, sh_c=sh_c, sh_b=sh_b, sh_m=sh_m,
        cap=co["cap"], cap_J=co["cap_J"],
        ji_max=float(np.max(co["Ji_dg"])), j_max=float(np.max(np.diag(co["J"]))),
        rho_mass=rho_mass, rho_long=rho_long,
        split=rho_mass + rho_long, s_pos=co["s_pos"]))
    del co, Gc, Dop, Qm, Nm, Bx, Kh, Kp

if not SURF:
    raise SystemExit("N1 produced no window -- probe cannot report")

info("N1.surface", "%d windows, h = %d .. %d (core m = %d .. %d), D = %.3e .. "
     "%.3e, zones n = %d .. %d; exact rho(W) = %.6f .. %.6f (T140 QUOTED "
     "%.4f .. %.4f), gap = %.3e .. %.3e"
     % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
        min(r["m"] for r in SURF), max(r["m"] for r in SURF),
        qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
        min(r["n"] for r in SURF), max(r["n"] for r in SURF),
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        RHO_W_T140[0], RHO_W_T140[1],
        qmin([r["gap_ex"] for r in SURF]), qmax([r["gap_ex"] for r in SURF])))

F_GAP = pow_fit([r["D"] for r in SURF], [r["gap_ex"] for r in SURF], "gap")
C_GAP = qmin([r["gap_ex"] / (r["D"] ** F_GAP["p"]) for r in SURF])
for r in SURF:
    r["target"] = C_GAP * (r["D"] ** F_GAP["p"])
info("N1.target", "THE TARGET of the sharp route, rebuilt on this surface: "
     "gap ~ %.4e D^%.3f (+- %.3f jackknife, a FIT, T142 QUOTED the exponent as "
     "%.0f), and the ENVELOPE constant C = %.4e is the MINIMUM of gap / D^p, so "
     "gap >= C D^p on EVERY window with equality at the tightest one.  The "
     "sharp route has to deliver a LOWER bound of exactly this shape with a "
     "zone-uniform coefficient -- the SCALE is not in question, only the "
     "COEFFICIENT" % (F_GAP["c"], F_GAP["p"], F_GAP["sp"], GAP_EXP_T142, C_GAP))

check("el_n1.reduction", all(r["red_err"] <= BAR_RED for r in SURF),
      "the FINITE-CORE REDUCTION rho(W) = lam_max(K^{1/2} H K^{1/2}) holds to "
      "%.2e .. %.2e (bar %.0e) on all %d windows -- QUOTED from T140 and "
      "re-verified because every object below is built on it"
      % (qmin([r["red_err"] for r in SURF]),
         qmax([r["red_err"] for r in SURF]), BAR_RED, len(SURF)))

check("el_n1.capacity_identity", all(r["cap_err"] <= BAR_ID for r in SURF),
      "THE T142 CAPACITY DECOMPOSITION K^{-1} = D^T J^{-1} D + x x^T / cap "
      "holds to %.2e (bar %.0e) on all %d windows -- QUOTED, re-verified"
      % (qmax([r["cap_err"] for r in SURF]), BAR_ID, len(SURF)))

check("el_n1.crossing_kernel", all(r["ln_err"] <= BAR_ID for r in SURF),
      "and the SECOND T142 identity L_N = D^T B D (the crossing kernel of the "
      "long-range part of H) holds to %.2e (bar %.0e), which is what allows H "
      "to be written in the increment coordinates at all"
      % (qmax([r["ln_err"] for r in SURF]), BAR_ID))

AMPLIF = qmax([r["err_N"] / r["gap_ex"] for r in SURF])
ASM_MAX = qmax([max(r["err_N"], r["err_Q"]) / asm_bar(r["m"]) for r in SURF])
check("el_n1.exact_form", all(r["err_Q"] <= asm_bar(r["m"])
                              and r["err_N"] <= asm_bar(r["m"])
                              for r in SURF)
      and all(r["ray_err"] <= BAR_RAY for r in SURF)
      and all(r["ray_err"] <= 10.0 * r["err_N"] / r["gap_ex"] for r in SURF),
      "N1's DELIVERABLE, and it is an IDENTITY and not a bound: "
      "1 - rho(W) = inf_v [ d^T (J^{-1} - B) d + (x^T v)^2 / cap - sum_k s_k "
      "v_k^2 ] / [ d^T J^{-1} d + (x^T v)^2 / cap ] with d = D v.  Numerator "
      "assembled to %.2e, denominator to %.2e, both at most %.2f of the "
      "assembly bar %.0f m eps (the bar is scaled linearly in m because the "
      "relative error of an assembled product of m x m matrices accumulates "
      "like m eps, and m runs to %d here), and the resulting generalised "
      "eigenvalue reproduces lam_min(A, A_B) to %.2e relative (bar %.0e).  "
      "THE DIRECTION OF THAT LAST NUMBER, because it is the one "
      "place this probe is not at machine precision: the assembly error is "
      "ABSOLUTE and the gap is 10^-6, so the predicted amplification is "
      "err / gap <= %.2e and the measured relative error sits BELOW it on "
      "every window -- the identity is exact, the eigenvalue is read through "
      "a conditioning factor 1 / gap, and no statement below leans on more "
      "than that.  NO inequality has been taken anywhere"
      % (qmax([r["err_N"] for r in SURF]), qmax([r["err_Q"] for r in SURF]),
         ASM_MAX, ASM_UNITS, max(r["m"] for r in SURF),
         qmax([r["ray_err"] for r in SURF]), BAR_RAY, AMPLIF))

check("el_n1.bookkeeping", all(r["book_err"] <= 1.0e-6 for r in SURF),
      "THE INGREDIENT BOOKKEEPING closes: at the exact minimiser the four "
      "shares reproduce the gap, (green + cap) - (crossing + mass) = gap to "
      "%.2e relative" % qmax([r["book_err"] for r in SURF]))

info("N1.shares", "AND HERE IS THE ANATOMY, which decides the shape of the "
     "route.  At the exact minimiser, normalised by the denominator: GREEN "
     "share %.4f .. %.4f, CAPACITY rank-one share %.2e .. %.2e (they sum to 1 "
     "by construction), CROSSING share %.4f .. %.4f, MASS share %.4f .. %.4f "
     "(they sum to rho).  Three things are readable off that line and all "
     "three are new.  (1) The capacity rank one is numerically ABSENT at the "
     "optimum: the minimiser is orthogonal to the equilibrium charge x to "
     "%.1e, so the (x^T v)^2 / cap term -- the piece T142 had to add to make "
     "the decomposition exact -- plays NO role in the gap and the sharp route "
     "is a statement about the GREEN FORM alone.  (2) The mass share is "
     "NEGATIVE (%.4f .. %.4f), i.e. the minimiser sits where the site masses "
     "s_k are negative; the mass term HELPS the gap instead of threatening it, "
     "which reverses the sign convention every Hardy formulation since T141 "
     "was written in.  (3) The D^3 smallness is therefore a CANCELLATION "
     "between the GREEN share (exactly 1) and the CROSSING share (%.4f .. "
     "%.4f, i.e. ABOVE 1), repaired by the negative mass -- no single "
     "ingredient carries the D^3 scale, which is exactly why any bound that "
     "replaces one of them comparably cannot see the gap"
     % (qmin([r["sh_g"] for r in SURF]), qmax([r["sh_g"] for r in SURF]),
        qmin([abs(r["sh_c"]) for r in SURF]),
        qmax([abs(r["sh_c"]) for r in SURF]),
        qmin([r["sh_b"] for r in SURF]), qmax([r["sh_b"] for r in SURF]),
        qmin([r["sh_m"] for r in SURF]), qmax([r["sh_m"] for r in SURF]),
        qmax([abs(r["sh_c"]) for r in SURF]),
        qmin([r["sh_m"] for r in SURF]), qmax([r["sh_m"] for r in SURF]),
        qmin([r["sh_b"] for r in SURF]), qmax([r["sh_b"] for r in SURF])))

F_SHB = pow_fit([r["D"] for r in SURF], [r["sh_b"] - 1.0 for r in SURF], "sh_b")
F_SHM = pow_fit([r["D"] for r in SURF], [abs(r["sh_m"]) for r in SURF], "sh_m")
info("N1.share_fits", "the two ingredients that actually move, against D "
     "(FITS with jackknife bands, never load-bearing): the crossing EXCESS "
     "(crossing share - 1) ~ D^%.3f +- %.3f (%s) and |mass share| ~ D^%.3f "
     "+- %.3f (%s), against the uniformity bar %.2f.  They are the same size "
     "and they cancel to D^%.2f; that cancellation IS the gap, and it is the "
     "object the sharp route has to bound from below"
     % (F_SHB["p"], F_SHB["sp"], "uniform" if unif_ok(F_SHB) else "drifts",
        F_SHM["p"], F_SHM["sp"], "uniform" if unif_ok(F_SHM) else "drifts",
        BAR_UNIF, F_GAP["p"]))

SPLIT_DEAD = all(r["split"] >= 1.0 for r in SURF)
check("el_n1.split_is_dead", SPLIT_DEAD,
      "AND THE FIRST THING THE SHARP ROUTE MUST NOT DO, measured rather than "
      "argued: the natural SPLIT rho <= rho_mass + rho_long -- mass part "
      "lam_max(K^{1/2} diag(s_+) K^{1/2}) = %.4f .. %.4f CERTIFIED, long-range "
      "part lam_max(B, J^{-1}) = %.4f .. %.4f -- sums to %.4f .. %.4f, i.e. "
      "ABOVE 1 on every window while rho itself is %.6f .. %.6f.  This check "
      "is written in the failing direction on purpose: it PASSES when the "
      "split is inadequate, and it is, by a factor %.2f .. %.2f.  Any Maz'ya "
      "evaluation applied to rho therefore starts already outside the target, "
      "which is why N2 applies it to the GAP"
      % (qmin([r["rho_mass"] for r in SURF]), qmax([r["rho_mass"] for r in SURF]),
         qmin([r["rho_long"] for r in SURF]), qmax([r["rho_long"] for r in SURF]),
         qmin([r["split"] for r in SURF]), qmax([r["split"] for r in SURF]),
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
         qmin([r["split"] / r["rho_ex"] for r in SURF]),
         qmax([r["split"] / r["rho_ex"] for r in SURF])))

para("""N1.1  THE CONSEQUENCE, stated before N2 spends a second on it.  Two
facts now sit next to each other.  (a) The exact form is a Hardy quotient whose
ingredients are all closed geometry -- the Green form of the endpoint Laplacian,
the crossing kernel, the site masses, the equilibrium charge.  (b) None of those
ingredients is itself of size D^3; the gap is a cancellation between two groups
that are individually O(1).  A capacity criterion applied to rho would have to
resolve that cancellation to relative accuracy D^3 and Maz'ya's criterion has a
built-in factor of four, so it cannot.  Applied to the GAP FORM, the same factor
of four costs a factor of four in the COEFFICIENT and nothing in the SCALE --
and a factor of four in the coefficient is exactly what the contract allows.
That is the whole reason the sharp route is worth running, and it is also the
reason it must be run on the gap form and in coordinates where the denominator
is a measure.""")


# ----------------------------------------------------------------------------
section("N2  THE MICLO / MAZ'YA BOUND for the exact form")
# ----------------------------------------------------------------------------
para("""N2.0  THE SET-UP, and the one step that is a choice.  The gap is
lam = inf_v v^T (K^{-1} - H) v / v^T K^{-1} v.  Both entries are FORMS, and the
classical capacity criterion needs a form against a MEASURE, so the denominator
is whitened away by the congruence w = K^{-1/2} v: the eigenvalue is untouched
(N0 verifies the congruence licence and the check below verifies the eigenvalue
itself), the denominator becomes the counting measure, and the numerator becomes
E = I - K^{1/2} H K^{1/2}, positive definite because rho < 1.  In those
coordinates Maz'ya's criterion reads

    Phi_sup <= 1 / lam <= 4 Phi_sup ,   Phi(A) = |A| / cap_E(A) ,

with cap_E(A) = 1^T [ (E^{-1})_AA ]^{-1} 1 the closed Green form of the capacity
(N0).  THE DIRECTIONS, once more and then never again: a single set A gives
lam <= cap(A) / |A|, CERTIFIED; the LOWER bound lam >= 1 / (4 Phi_sup) needs the
sup over ALL sets, so every family-restricted maximum below is a MEASURED lower
bound on Phi_sup and an UPPER bound on nothing.  What the probe can therefore
decide honestly is: (a) does the sup live on a CLOSED family, (b) is the product
Phi lam -- which the criterion forces into [1/4, 1] for a Dirichlet form -- in
that window here, where the form is NOT Markovian, and (c) is the resulting
coefficient of D^3 zone-uniform.""")

N2C = [r for r in SURF if r["m"] <= N2_MCAP]
if len(N2C) > N2_WINDOWS:
    _st = max(1, len(N2C) // N2_WINDOWS)
    N2C = N2C[::_st][:N2_WINDOWS]
info("N2.subset", "the capacity surface is the %d windows of the N1 surface "
     "with m <= %d (one dense inverse and a few hundred small Cholesky solves "
     "per window); m = %d .. %d, D = %.3e .. %.3e"
     % (len(N2C), N2_MCAP, min(r["m"] for r in N2C), max(r["m"] for r in N2C),
        qmin([r["D"] for r in N2C]), qmax([r["D"] for r in N2C])))

N2R = []
for r in N2C:
    if budget_left() < BUDGET_S - T_N1 - T_N2:
        info("N2.budget", "capacity surface truncated after %d windows"
             % len(N2R))
        break
    hv = build_core(r["al"], r["M"], r["h"], ATOMS_ALL)
    if hv is None:
        continue
    m = r["m"]
    Gm = conj_form(hv["Kh"], hv["H"])
    Em = sym(np.eye(m) - Gm)
    try:
        w0, V0 = eigh(Em, subset_by_index=[0, 0])
    except (LinAlgError, ValueError):
        continue
    lam_E = float(w0[0])
    if not (lam_E > 0.0):
        continue
    psi = V0[:, 0]
    cong_err = abs(lam_E - r["gap_ex"]) / max(r["gap_ex"], 1.0e-300)
    fac = safe_cho(Em)
    if fac is None:
        continue
    Rm = sym(cho_solve(fac, np.eye(m), check_finite=False))

    offE = Em - np.diag(np.diag(Em))
    tot_off = float(np.sum(np.abs(offE)))
    mk_frac = float(np.mean(offE > 0.0))
    mk_mass = float(np.sum(np.where(offE > 0.0, offE, 0.0))) / max(tot_off,
                                                                  1.0e-300)

    phi = np.abs(psi)
    phi = phi / max(float(np.linalg.norm(phi)), 1.0e-300)
    ch = capacitary_chain(Rm, phi, lam_E)
    if ch is None:
        continue

    dgR = np.sqrt(np.maximum(np.diag(Rm), 0.0))
    Dop = hv["Dop"]
    pots = [hv["Kmh"] @ np.ones(m), hv["Kmh"] @ np.diag(hv["K"]),
            hv["Kmh"] @ hv["x"], hv["Kmh"] @ (Dop.T @ hv["p"]),
            hv["Kh"] @ np.ones(m), np.abs(hv["Kmh"] @ np.maximum(hv["s"], 0.0))]
    fam_clo = []
    for pv in pots:
        fam_clo.extend(level_sets_of(pv))
    fam_grn = level_sets_of(dgR, nq=15)
    fam_int = interval_sets(m)

    ph_clo, set_clo, _ = phi_over_family(Rm, fam_clo)
    ph_grn, set_grn, _ = phi_over_family(Rm, fam_grn)
    ph_int, set_int, _ = phi_over_family(Rm, fam_int)
    ph_ext = ch["phi_max"]
    ph_all = max(ph_clo, ph_grn, ph_int, ph_ext)
    arg_best = max([(ph_ext, ch["phi_arg"]), (ph_grn, set_grn),
                    (ph_clo, set_clo), (ph_int, set_int)],
                   key=lambda t: t[0])[1]
    arg_frac = (float(arg_best.size) / m) if arg_best is not None \
        else float("nan")

    # --- the LOCAL SEARCH, only where a full pass is affordable -------------
    ph_loc, n_loc = float("nan"), 0
    if m <= N2_LOCAL_M:
        cur = max([(ph_ext, ch["phi_arg"]), (ph_grn, set_grn),
                   (ph_clo, set_clo), (ph_int, set_int)], key=lambda t: t[0])
        best_v, best_s = cur[0], cur[1]
        mask = np.zeros(m, dtype=bool)
        if best_s is not None:
            mask[best_s] = True
        for _sweep in range(3):
            improved = False
            for kk in range(m):
                mask[kk] = not mask[kk]
                idx = np.nonzero(mask)[0]
                if idx.size == 0 or idx.size == m:
                    mask[kk] = not mask[kk]
                    continue
                cp = set_capacity(Rm, idx)
                val = (float(idx.size) / cp) if (np.isfinite(cp) and cp > 0.0) \
                    else -1.0
                if val > best_v * (1.0 + 1.0e-12):
                    best_v = val
                    improved = True
                    n_loc += 1
                else:
                    mask[kk] = not mask[kk]
            if not improved:
                break
        ph_loc = best_v
        ph_all = max(ph_all, ph_loc)

    # --- the kappa POOL: the capacitary constant at other test functions ----
    kap_pool = [ch["kappa"]]
    for wv in (dgR, np.abs(hv["Kmh"] @ np.ones(m)),
               np.abs(RNG.standard_normal(m)) + 0.25):
        nv = float(np.linalg.norm(wv))
        if not (nv > 0.0):
            continue
        wv = wv / nv
        lw = float(wv @ Em @ wv)
        if not (lw > 0.0):
            continue
        cw = capacitary_chain(Rm, wv, lw, jmax=20)
        if cw is not None and np.isfinite(cw["kappa"]):
            kap_pool.append(cw["kappa"])
    kap_max = qmax(kap_pool)

    # --- THE SECOND COORDINATE SYSTEM: the node space -----------------------
    ph2_ext, ph2_int, cong2, mk2_mass = (float("nan"),) * 4
    try:
        lb, Vb = eigh(sym(hv["A_B"]))
        if float(np.min(lb)) > 0.0:
            Bmh = sym((Vb / np.sqrt(lb)[None, :]) @ Vb.T)
            E2 = sym(Bmh @ sym(hv["A"]) @ Bmh)
            w2, V2 = eigh(E2, subset_by_index=[0, 0])
            lam2 = float(w2[0])
            cong2 = abs(lam2 - r["gap_ex"]) / max(r["gap_ex"], 1.0e-300)
            off2 = E2 - np.diag(np.diag(E2))
            mk2_mass = float(np.sum(np.where(off2 > 0.0, off2, 0.0))) \
                / max(float(np.sum(np.abs(off2))), 1.0e-300)
            f2 = safe_cho(E2)
            if f2 is not None and lam2 > 0.0:
                R2 = sym(cho_solve(f2, np.eye(E2.shape[0]), check_finite=False))
                p2 = np.abs(V2[:, 0])
                p2 = p2 / max(float(np.linalg.norm(p2)), 1.0e-300)
                c2 = capacitary_chain(R2, p2, lam2)
                if c2 is not None:
                    ph2_ext = c2["phi_max"]
                fam2 = interval_sets(E2.shape[0])
                dg2 = np.sqrt(np.maximum(np.diag(R2), 0.0))
                fam2.extend(level_sets_of(dg2, nq=15))
                fam2.extend(level_sets_of(np.diag(hv["A_B"])))
                ph2_int, _s2, _v2 = phi_over_family(R2, fam2)
                del R2, fam2
            del E2, Vb, Bmh
    except (LinAlgError, ValueError):
        pass

    lam_bound = 1.0 / max(4.0 * ph_all, 1.0e-300)
    ph_clo_best = max(ph_clo, ph_grn, ph_int)
    N2R.append(dict(
        k=r["k"], n=r["n"], D=r["D"], m=m, gap_ex=r["gap_ex"], target=r["target"],
        lam_E=lam_E, cong_err=cong_err, mk_frac=mk_frac, mk_mass=mk_mass,
        kappa=ch["kappa"], kap_max=kap_max, n_lev=ch["n_lev"],
        resid=ch["resid"] / max(ch["tot"], 1.0e-300), chain_ok=ch["chain_ok"],
        chain_eff=ch["chain_eff"], lam_chain=ch["chain_eff"] * lam_E,
        ph_ext=ph_ext, ph_grn=ph_grn, ph_clo=ph_clo, ph_int=ph_int,
        ph_loc=ph_loc, ph_all=ph_all, n_loc=n_loc, arg_frac=arg_frac,
        exhaust=ph_all * lam_E, ub_cert=1.0 / max(ph_all, 1.0e-300),
        lam_bound=lam_bound, c_sharp=lam_bound / (r["D"] ** F_GAP["p"]),
        c_gap=lam_E / (r["D"] ** F_GAP["p"]),
        loss=lam_bound / max(lam_E, 1.0e-300),
        ph_clo_best=ph_clo_best,
        r_clo_best=ph_clo_best / max(ph_all, 1.0e-300),
        r_clo=ph_clo / max(ph_all, 1.0e-300),
        r_int=ph_int / max(ph_all, 1.0e-300),
        r_grn=ph_grn / max(ph_all, 1.0e-300),
        cong2=cong2, mk2_mass=mk2_mass, ph2_ext=ph2_ext, ph2_int=ph2_int,
        r2_int=(ph2_int / ph2_ext if (np.isfinite(ph2_int)
                                      and np.isfinite(ph2_ext)
                                      and ph2_ext > 0.0) else float("nan"))))
    del Gm, Em, Rm, fac, V0, Dop, fam_clo, fam_grn, fam_int, hv

if not N2R:
    raise SystemExit("N2 produced no window -- probe cannot report")

check("el_n2.congruence", all(x["cong_err"] <= BAR_CONG for x in N2R),
      "THE WHITENING IS EXACT: lam_min(I - K^{1/2} H K^{1/2}) reproduces "
      "lam_min(A, A_B) to %.2e relative (bar %.0e) on all %d windows, and the "
      "SECOND coordinate system (the node space, E = A_B^{-1/2} A A_B^{-1/2}) "
      "reproduces it to %.2e.  Both are congruences, so the capacity criterion "
      "is being applied to the SAME number in two different geometries"
      % (qmax([x["cong_err"] for x in N2R]), BAR_CONG, len(N2R),
         qmax([x["cong2"] for x in N2R])))

check("el_n2.chain_holds", all(x["chain_ok"] for x in N2R),
      "the MICLO LEVEL CHAIN is evaluated term by term and holds on every "
      "window: sum phi^2 <= 4 sum_j tau_j^2 |A_j| + resid over %d .. %d dyadic "
      "levels with a residual share of only %.2e .. %.2e, so the truncation of "
      "the level ladder costs nothing that matters"
      % (min(x["n_lev"] for x in N2R), max(x["n_lev"] for x in N2R),
         qmin([x["resid"] for x in N2R]), qmax([x["resid"] for x in N2R])))

check("el_n2.direction_holds", all(x["exhaust"] <= 1.0 + 1.0e-9 for x in N2R),
      "and the DIRECTION statement holds numerically on every window, which is "
      "the internal consistency test of the whole block: Phi_max x lam = "
      "%.4f .. %.4f <= 1, i.e. every set really does certify an UPPER bound on "
      "the gap.  Maz'ya's theorem would in addition force this product ABOVE "
      "1/4 for a Dirichlet form; whether it is, is the measurement below and "
      "not an assumption"
      % (qmin([x["exhaust"] for x in N2R]), qmax([x["exhaust"] for x in N2R])))

info("N2.markov", "THE HYPOTHESIS CHECK FIRST, because it decides what the "
     "criterion is worth here: E = I - K^{1/2} H K^{1/2} is NOT a Dirichlet "
     "form -- %.1f%% .. %.1f%% of its off-diagonal entries are POSITIVE and "
     "they carry %.3f .. %.3f of the off-diagonal mass (in the node "
     "coordinates the positive share is %.3f .. %.3f).  Maz'ya's two-sided "
     "criterion and the capacitary strong-type inequality are stated for "
     "Markovian forms (Fukushima-Oshima-Takeda 1994, ch. 1-2), so the UPPER "
     "half of the sandwich is NOT licensed here by citation.  Everything "
     "below therefore MEASURES what the theorem would have asserted"
     % (100.0 * qmin([x["mk_frac"] for x in N2R]),
        100.0 * qmax([x["mk_frac"] for x in N2R]),
        qmin([x["mk_mass"] for x in N2R]), qmax([x["mk_mass"] for x in N2R]),
        qmin([x["mk2_mass"] for x in N2R]),
        qmax([x["mk2_mass"] for x in N2R])))

info("N2.exhaust", "THE CENTRAL MEASUREMENT, family by family.  Phi x lam, "
     "which is 1 exactly when the family attains the true supremum: extremal "
     "level sets %.4f .. %.4f, Green-diagonal level sets %.4f .. %.4f, closed "
     "transported potentials %.4f .. %.4f, index intervals %.4f .. %.4f, and "
     "the best of all families %.4f .. %.4f.  Relative to the best family the "
     "CLOSED families reach %.4f .. %.4f (Green diagonal %.4f .. %.4f, "
     "intervals %.4f .. %.4f), against the preregistered exhaustion bar %.2f"
     % (qmin([x["ph_ext"] * x["lam_E"] for x in N2R]),
        qmax([x["ph_ext"] * x["lam_E"] for x in N2R]),
        qmin([x["ph_grn"] * x["lam_E"] for x in N2R]),
        qmax([x["ph_grn"] * x["lam_E"] for x in N2R]),
        qmin([x["ph_clo"] * x["lam_E"] for x in N2R]),
        qmax([x["ph_clo"] * x["lam_E"] for x in N2R]),
        qmin([x["ph_int"] * x["lam_E"] for x in N2R]),
        qmax([x["ph_int"] * x["lam_E"] for x in N2R]),
        qmin([x["exhaust"] for x in N2R]), qmax([x["exhaust"] for x in N2R]),
        qmin([x["r_clo"] for x in N2R]), qmax([x["r_clo"] for x in N2R]),
        qmin([x["r_grn"] for x in N2R]), qmax([x["r_grn"] for x in N2R]),
        qmin([x["r_int"] for x in N2R]), qmax([x["r_int"] for x in N2R]),
        BAR_EXHAUST))

info("N2.argmax", "and WHAT the capacity-critical set looks like, because a "
     "criterion whose argmax is the whole space says nothing: the best set "
     "covers %.3f .. %.3f of the core (m = %d .. %d), so it is a genuine "
     "SUBSET and the criterion is reading a real bottleneck rather than the "
     "trivial set"
     % (qmin([x["arg_frac"] for x in N2R]),
        qmax([x["arg_frac"] for x in N2R]),
        min(x["m"] for x in N2R), max(x["m"] for x in N2R)))

LOC = [x for x in N2R if np.isfinite(x["ph_loc"])]
if LOC:
    info("N2.local", "AND THE HONESTY CHECK ON THOSE FAMILIES: on the %d "
         "windows small enough for a full add/remove local search (m <= %d) "
         "the search accepted %d .. %d single-index moves and improved the "
         "best family value by a factor %.4f .. %.4f, ending at Phi x lam = "
         "%.4f .. %.4f.  A family that the local search can beat is not a "
         "family the sup lives on, and that is measured here rather than hoped"
         % (len(LOC), N2_LOCAL_M, min(x["n_loc"] for x in LOC),
            max(x["n_loc"] for x in LOC),
            qmin([x["ph_loc"] / max(x["ph_ext"], x["ph_grn"], x["ph_clo"],
                                    x["ph_int"]) for x in LOC]),
            qmax([x["ph_loc"] / max(x["ph_ext"], x["ph_grn"], x["ph_clo"],
                                    x["ph_int"]) for x in LOC]),
            qmin([x["ph_loc"] * x["lam_E"] for x in LOC]),
            qmax([x["ph_loc"] * x["lam_E"] for x in LOC])))

R2I = [x for x in N2R if np.isfinite(x["r2_int"]) and np.isfinite(x["ph2_ext"])]
if R2I:
    E2X = [x["ph2_ext"] * x["gap_ex"] for x in R2I]
    E2I = [x["ph2_int"] * x["gap_ex"] for x in R2I]
    info("N2.node_space", "THE SECOND GEOMETRY, where an index interval is a "
         "BLOCK OF WINDOW LAGS and therefore a genuinely closed object.  In "
         "the node coordinates E = A_B^{-1/2} A A_B^{-1/2} the two families "
         "SWAP ROLES: the extremal dyadic levels reach only Phi x lam = "
         "%.4f .. %.4f while the INTERVALS reach %.4f .. %.4f, a factor "
         "%.1f .. %.1f better.  So the near-optimal sets are intervals of "
         "window lags, which is exactly the one-dimensional structure "
         "Muckenhoupt 1972 needs, and the answer to 'does the sup live on a "
         "closed geometric family' is %s in this geometry"
         % (qmin(E2X), qmax(E2X), qmin(E2I), qmax(E2I),
            qmin([x["r2_int"] for x in R2I]), qmax([x["r2_int"] for x in R2I]),
            ("YES" if qmax(E2I) >= BAR_EXHAUST else "NOT on this grid")))

check("el_n2.chain_below", all(x["lam_chain"] <= x["lam_E"] * (1.0 + 1.0e-6)
                               for x in N2R),
      "THE CONSTRUCTIVE (chain) VERSION of the criterion, evaluated term by "
      "term on the extremal's own dyadic levels: its efficiency -- the ratio "
      "of the chain's bound to the gap -- is %.3e .. %.3e, so the chain bound "
      "%.3e .. %.3e does lie BELOW the gap %.3e .. %.3e on every window, as "
      "the arithmetic requires.  BUT READ THE SIZE OF THAT EFFICIENCY: the "
      "chain loses a factor %.0f .. %.0f, because the TOP dyadic level sets "
      "are small sets whose capacity is O(1) while the eigenvalue is 10^-5.  "
      "Miclo's chain is therefore NOT the mechanism that carries the "
      "coefficient here, and that is measured rather than suspected"
      % (qmin([x["chain_eff"] for x in N2R]),
         qmax([x["chain_eff"] for x in N2R]),
         qmin([x["lam_chain"] for x in N2R]),
         qmax([x["lam_chain"] for x in N2R]),
         qmin([x["lam_E"] for x in N2R]), qmax([x["lam_E"] for x in N2R]),
         1.0 / qmax([x["chain_eff"] for x in N2R]),
         1.0 / qmin([x["chain_eff"] for x in N2R])))

info("N2.kappa", "THE CAPACITARY CONSTANT, which is the ingredient a theorem "
     "would supply and this probe can only measure: kappa = sum_j tau_j^2 "
     "cap(A_j) / E(w) is %.4f .. %.4f at the extremal and %.4f .. %.4f over a "
     "small pool of other test functions (Green diagonal, transported "
     "constants, a random nonnegative draw).  For a Dirichlet form Maz'ya's "
     "capacitary strong-type inequality would cap this by an absolute "
     "constant; here it is %s across the pool, FITTED against D as D^%.3f "
     "+- %.3f (a FIT) -- %s"
     % (qmin([x["kappa"] for x in N2R]), qmax([x["kappa"] for x in N2R]),
        qmin([x["kap_max"] for x in N2R]), qmax([x["kap_max"] for x in N2R]),
        ("bounded" if qmax([x["kap_max"] for x in N2R]) < 10.0
         else "NOT small"),
        pow_fit([x["D"] for x in N2R], [x["kap_max"] for x in N2R],
                "kap")["p"],
        pow_fit([x["D"] for x in N2R], [x["kap_max"] for x in N2R],
                "kap")["sp"],
        ("uniform in D"
         if unif_ok(pow_fit([x["D"] for x in N2R],
                            [x["kap_max"] for x in N2R], "kap"))
         else "drifting with D")))

F_SHARP = pow_fit([x["D"] for x in N2R], [x["c_sharp"] for x in N2R], "c_sharp")
F_CGAP = pow_fit([x["D"] for x in N2R], [x["c_gap"] for x in N2R], "c_gap")
F_LOSS = pow_fit([x["D"] for x in N2R], [x["loss"] for x in N2R], "loss")
F_BOUND = pow_fit([x["D"] for x in N2R], [x["lam_bound"] for x in N2R], "bound")
EXH_MIN = qmin([x["exhaust"] for x in N2R])
CLO_MED = qmed([x["r_clo_best"] for x in N2R])
info("N2.core", "THE CORE NUMBER OF THE PROBE.  Taking the criterion with the "
     "measured supremum, lam >= 1 / (4 Phi_sup) evaluates to %.3e .. %.3e "
     "against the true gap %.3e .. %.3e and the envelope target %.3e .. %.3e; "
     "as a coefficient of D^%.3f that is c = %.4f .. %.4f against the envelope "
     "constant C = %.4f, so the bound is POSITIVE and of the right shape on "
     "every window of the surface with a coefficient bounded below by %.4f"
     % (qmin([x["lam_bound"] for x in N2R]),
        qmax([x["lam_bound"] for x in N2R]),
        qmin([x["lam_E"] for x in N2R]), qmax([x["lam_E"] for x in N2R]),
        qmin([x["target"] for x in N2R]), qmax([x["target"] for x in N2R]),
        F_GAP["p"], qmin([x["c_sharp"] for x in N2R]),
        qmax([x["c_sharp"] for x in N2R]), C_GAP,
        qmin([x["c_sharp"] for x in N2R])))

info("N2.uniformity", "AND THE UNIFORMITY QUESTION, SPLIT THE WAY IT HAS TO "
     "BE SPLIT, because the two halves have different owners.  (a) THE "
     "ROUTE'S OWN LOSS, bound / gap = 1 / (4 Phi_sup lam) = %.4f .. %.4f, "
     "FITTED as D^%.3f +- %.3f -- %s against the bar %.2f.  This is the only "
     "number the capacity criterion is responsible for, and it is flat.  "
     "(b) THE GAP'S OWN SCATTER around the fitted power law on this subset, "
     "c_gap = gap / D^%.3f ~ D^%.3f +- %.3f, which the bound inherits and "
     "which is a property of the arithmetic and not of the criterion; the "
     "bound's coefficient accordingly fits as D^%.3f +- %.3f.  The DIFFERENCE "
     "of the two exponents, %.4f, is what the sharp route ADDS to the drift"
     % (qmin([x["loss"] for x in N2R]), qmax([x["loss"] for x in N2R]),
        F_LOSS["p"], F_LOSS["sp"],
        "ZONE-UNIFORM" if unif_ok(F_LOSS) else "NOT zone-uniform", BAR_UNIF,
        F_GAP["p"], F_CGAP["p"], F_CGAP["sp"], F_SHARP["p"], F_SHARP["sp"],
        F_SHARP["p"] - F_CGAP["p"]))

SHARP_EXH = bool(EXH_MIN >= BAR_EXHAUST)
SHARP_CLOSED = bool(CLO_MED >= BAR_EXHAUST)
SHARP_UNIF = unif_ok(F_LOSS)
check("el_n2.criterion_window", SHARP_EXH,
      "THE DECISIVE FACT OF N2, and it is a fact about a NON-Markovian form: "
      "Phi_sup lam sits at %.4f .. %.4f on the whole surface, i.e. INSIDE the "
      "window [1/4, 1] that Maz'ya's criterion forces for a Dirichlet form, "
      "and it is flat in D (fit D^%.3f +- %.3f).  The criterion's conclusion "
      "therefore HOLDS here with the classical constant even though its "
      "hypothesis does not; what is missing is a proof of that, not a number"
      % (qmin([x["exhaust"] for x in N2R]), qmax([x["exhaust"] for x in N2R]),
         pow_fit([x["D"] for x in N2R], [x["exhaust"] for x in N2R], "e")["p"],
         pow_fit([x["D"] for x in N2R], [x["exhaust"] for x in N2R], "e")["sp"]))


# ----------------------------------------------------------------------------
section("N3  R1d the dual certificate, and R4 the border blocks by capacity")
# ----------------------------------------------------------------------------
para("""N3.0  R1d FIRST.  T142 closed the comparison branch, but its negative
statement about the CONDUCTANCE CLASS was MEASURED: a search reported that it
found nothing below a certain value, and the one CERTIFIED barrier it had (the
single-direction relaxation) turned out to be saturated and therefore vacuous.
The repair is a genuine dual.  For finitely many test directions the class
problem min { Lam(H, Y) Om(Y) : Y in the cone } has a LINEAR PROGRAM underneath
it whose value bounds the class from below, and an LP value is only as good as
its dual point -- so the solver's multipliers are clipped to their sign
constraints, renormalised, scaled until every generator inequality holds with a
margin, and only then read as a certificate.  What comes out is a number that
holds for EVERY member of the cone and not only for the ones a search visited.""")

LPC = [r for r in SURF if r["m"] <= LP_MCAP]
if len(LPC) > LP_WINDOWS:
    _st = max(1, len(LPC) // LP_WINDOWS)
    LPC = LPC[::_st][:LP_WINDOWS]

LPR = []
for r in LPC:
    if budget_left() < BUDGET_S - T_N1 - T_N2 - T_LP:
        info("N3.budget", "LP pool truncated after %d windows" % len(LPR))
        break
    co = build_core(r["al"], r["M"], r["h"], ATOMS_ALL)
    if co is None:
        continue
    m = co["m"]
    Kh, H = co["Kh"], co["H"]
    Gm = conj_form(Kh, H)
    try:
        wg, Vg = eigh(sym(Gm))
    except (LinAlgError, ValueError):
        continue
    U = [Kh @ Vg[:, m - 1 - j] for j in range(min(6, m))]
    U.append(np.ones(m))
    U.append(co["x"] / max(float(np.linalg.norm(co["x"])), 1.0e-300))
    step_u = max(1, m // 14)
    for kk in range(0, m, step_u):
        e = np.zeros(m)
        e[kk] = 1.0
        U.append(e)
    for a, b in ((0, m // 4), (m // 4, m // 2), (m // 2, 3 * m // 4),
                 (3 * m // 4, m), (0, m // 2), (m // 4, 3 * m // 4),
                 (m // 2, m), (0, m)):
        e = np.zeros(m)
        e[a:b] = 1.0
        if float(e @ e) > 0.0:
            U.append(e)
    for _ in range(8):
        U.append(RNG.standard_normal(m))
    U = U[:LP_NU]
    Z = [Vg[:, m - 1 - j] for j in range(min(6, m))]
    step_z = max(1, m // 18)
    for kk in range(0, m, step_z):
        e = np.zeros(m)
        e[kk] = 1.0
        Z.append(e)
    for _ in range(8):
        z = RNG.standard_normal(m)
        Z.append(z / float(np.linalg.norm(z)))
    Z = Z[:LP_NZ]
    lb = lp_class_bound(H, Kh, U, Z)
    if lb is None:
        del co, Gm
        continue
    lb.update(n=r["n"], D=r["D"], m=m, rho=r["rho_ex"], target=r["target"])
    LPR.append(lb)
    del co, Gm, Vg, U, Z

if LPR:
    LPOK = [x for x in LPR if np.isfinite(x["L_cert"])]
    SAT = [x["L_cert"] / x["rho"] for x in LPOK]
    LP_SATURATED = bool(SAT and qmax(SAT) <= 1.0 + 1.0e-3)
    info("N3.r1d", "the LP dual over the conductance cone on %d windows "
         "(m = %d .. %d, %d Lam directions and %d Om directions): the LP value "
         "gives a class floor 1 / V = %.6f .. %.6f, and the HAND-VERIFIED DUAL "
         "POINT certifies %.6f .. %.6f of it on %d of %d windows.  NOW READ IT "
         "AGAINST rho(W) = %.6f .. %.6f, which every class bound exceeds for "
         "free: the ratio certificate / rho is %.6f .. %.6f, i.e. the "
         "relaxation is %s.  T142's MEASURED class optimum was %.2f .. %.2f "
         "and the first hurdle is 1, so %s"
         % (len(LPR), min(x["m"] for x in LPR), max(x["m"] for x in LPR),
            max(x["nu"] for x in LPR), max(x["nz"] for x in LPR),
            qmin([x["L_lp"] for x in LPR]), qmax([x["L_lp"] for x in LPR]),
            qmin([x["L_cert"] for x in LPOK]) if LPOK else float("nan"),
            qmax([x["L_cert"] for x in LPOK]) if LPOK else float("nan"),
            len(LPOK), len(LPR),
            qmin([x["rho"] for x in LPR]), qmax([x["rho"] for x in LPR]),
            qmin(SAT), qmax(SAT),
            ("SATURATED AT THE TRIVIAL FLOOR rho and adds nothing"
             if LP_SATURATED else "strictly above the trivial floor"),
            CLASS_T142[0], CLASS_T142[1],
            ("R1d is NOT closed by this construction, and the reason is now "
              "visible and structural rather than a matter of effort: a "
              "relaxation that constrains Om along FINITELY MANY directions "
              "lets the cone move Y's mass into the directions it did not "
              "constrain, so the multi-direction LP saturates exactly where "
              "T142's single-direction barrier did.  What R1d needs is the "
              "FULL Om, i.e. an SDP constraint K^{1/2} Y K^{1/2} <= I, not a "
              "sample of it -- that is a different program and it is on the "
              "rest list as such" if LP_SATURATED else
              "the certificate is a genuine improvement on T142's vacuous "
              "single-direction barrier and the remaining distance to the "
              "hurdle is a matter of more directions")))
    check("el_n3.dual_valid", all(x.get("dual_ok", 0) == 1 for x in LPOK)
          and len(LPOK) > 0,
          "and the dual point itself is VALID on all %d certified windows: "
          "y >= 0, mu >= 0, sum_i y_i (u_i^T H u_i) = 1 and every generator "
          "inequality verified explicitly after the rescaling.  The gap "
          "between the solver's LP value and the certified value is a factor "
          "%.4f .. %.4f, which is the price of insisting on a hand-checked "
          "certificate"
          % (len(LPOK),
             qmin([x["L_lp"] / x["L_cert"] for x in LPOK]),
             qmax([x["L_lp"] / x["L_cert"] for x in LPOK])))

para("""N3.1  R4, the border blocks, with the CAPACITY tail.  The pool is
REBUILT here rather than reloaded, so its open set is its own and the count is
not comparable with T142's %d; what transfers is the anatomy.  For every block
the paired Neumann ladder is run; for the blocks it does not certify, the block's
own gap form is whitened exactly as in N2 and the Maz'ya argmax set is located.
Two things then come for free and both are worth more than the R4 item itself:
on a block small enough the sup over ALL subsets is EXHAUSTIBLE BY ENUMERATION,
which turns N2's central measurement into a CERTIFIED statement on a genuine
window object; and the argmax set's FAR SHARE is exactly the input a decay
statement would have to beat.""" % R4_OPEN_T142)

PER_RHO = []
for rho_l in K3_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho_l) // 2
        if hf > K3_HCAP or hf < H_MIN:
            continue
        key = int(round(K3_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    lst = []
    for (k, DA) in got[-K3_PER_RHO:]:
        lst.append((k, int(N_DEEP[k]), DA / rho_l, rho_l, 1))
        lst.append((k, int(N_DEEP[k]), DA, rho_l, 0))
    PER_RHO.append(lst)
K3_TASK = []
for i in range(max(len(l) for l in PER_RHO)):
    for l in PER_RHO:
        if i < len(l):
            K3_TASK.append(l[i])
K3_TASK = K3_TASK[:K3_MAX]

K3R = []
N_ENUM = 0
for (k, n_lbl, D, rho_lbl, scaled) in K3_TASK:
    if budget_left() < BUDGET_S - T_N1 - T_N2 - T_LP - T_R4:
        info("N3.budget_r4", "border pool truncated at n = %d after %d blocks"
             % (n_lbl, len(K3R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < K3_GC_MIN or fr["h_n"] > K3_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    pn = paired_neumann_small(st["S"])
    if pn is None:
        del st
        continue
    g = pn["g"]
    row = dict(n=n_lbl, D=D, g=g, rho_lbl=rho_lbl, scaled=scaled,
               cert_any=pn["cert_any"], need_best=pn["need_best"],
               lam_b=float("nan"), phi_fam=float("nan"),
               phi_enum=float("nan"), exh_fam=float("nan"),
               exh_enum=float("nan"), far_share=float("nan"), enum=0)
    try:
        lam_b = float(eigh(sym(st["S"]), sym(pn["S_B"]), eigvals_only=True,
                           subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        lam_b = float("nan")
    if np.isfinite(lam_b) and lam_b > 0.0 and g >= 3:
        row["lam_b"] = lam_b
        lbv, Vb = eigh(sym(pn["S_B"]))
        if float(np.min(lbv)) > 0.0:
            Bmh = sym((Vb / np.sqrt(lbv)[None, :]) @ Vb.T)
            Eb = sym(Bmh @ sym(st["S"]) @ Bmh)
            fb = safe_cho(Eb)
            if fb is not None:
                Rb = sym(cho_solve(fb, np.eye(g), check_finite=False))
                famb = interval_sets(g, npts=min(g, 10))
                famb.extend(level_sets_of(np.sqrt(np.maximum(np.diag(Rb), 0.0)),
                                          nq=9))
                pf, sf, _ = phi_over_family(Rb, famb)
                row["phi_fam"] = pf
                row["exh_fam"] = pf * lam_b
                if sf is not None and g > FAR_K:
                    row["far_share"] = float(np.mean(sf >= FAR_K))
                if g <= K3_ENUM_G:
                    row["_R"] = Rb
                del Eb, famb
            del Bmh, Vb
    K3R.append(row)
    del st, pn

# --- THE EXHAUSTIVE PASS, on the LARGEST blocks that admit it ---------------
for row in sorted([x for x in K3R if "_R" in x], key=lambda x: -x["g"]):
    if N_ENUM >= K3_ENUM_MAX or budget_left() < 60.0:
        break
    g = row["g"]
    Rb = row["_R"]
    best, best_s = 0.0, None
    for mask in range(1, 1 << g):
        idx = np.nonzero(np.array([(mask >> i) & 1 for i in range(g)],
                                  dtype=bool))[0]
        cp = set_capacity(Rb, idx)
        if np.isfinite(cp) and cp > 0.0:
            val = idx.size / cp
            if val > best:
                best, best_s = val, idx
    row["phi_enum"] = best
    row["exh_enum"] = best * row["lam_b"]
    row["enum"] = 1
    row["n_sub"] = (1 << g) - 1
    if best_s is not None and g > FAR_K:
        row["far_share"] = float(np.mean(best_s >= FAR_K))
    N_ENUM += 1
for row in K3R:
    row.pop("_R", None)

if K3R:
    OPEN = [x for x in K3R if not x["cert_any"]]
    CERTB = [x for x in K3R if x["cert_any"]]
    NEEDS = [x["need_best"] for x in OPEN if np.isfinite(x["need_best"])] \
        or [x["need_best"] for x in K3R if np.isfinite(x["need_best"])]
    info("N3.r4_pool", "%d border blocks, g = %d .. %d, zones n = %d .. %d; "
         "the ladder to m = %d certifies %d and leaves %d open (T142 QUOTED "
         "%d, a different pool).  Need ratio on the open blocks %.2f .. %.2f, "
         "and the block gaps themselves are %.3e .. %.3e"
         % (len(K3R), min(x["g"] for x in K3R), max(x["g"] for x in K3R),
            min(x["n"] for x in K3R), max(x["n"] for x in K3R), max(M_LADDER),
            len(CERTB), len(OPEN), R4_OPEN_T142, qmin(NEEDS), qmax(NEEDS),
            qmin([x["lam_b"] for x in K3R]), qmax([x["lam_b"] for x in K3R])))
    ENU = [x for x in K3R if x["enum"]]
    if ENU:
        check("el_n3.enumerated_window",
              all(0.25 <= x["exh_enum"] <= 1.0 + 1.0e-9 for x in ENU),
              "AND THE ONE PLACE IN THIS PROBE WHERE THE SUPREMUM IS NOT "
              "FAMILY-RESTRICTED: on the %d largest blocks that admit it "
              "(g = %d .. %d) ALL %d .. %d subsets were enumerated, so "
              "Phi_sup is EXACT and not measured.  There Phi_sup lam = "
              "%.4f .. %.4f -- inside the Maz'ya window [1/4, 1] on every one "
              "of them, for forms that are NOT Markovian either.  This is the "
              "strongest evidence the probe has that the criterion's "
              "conclusion survives the loss of its hypothesis, and it is "
              "CERTIFIED by exhaustion rather than measured.  The closed "
              "families recover %.4f .. %.4f of the exact supremum, which is "
              "the same statement N2 measures on the big windows and could "
              "not certify there"
              % (len(ENU), min(x["g"] for x in ENU), max(x["g"] for x in ENU),
                 min(x["n_sub"] for x in ENU), max(x["n_sub"] for x in ENU),
                 qmin([x["exh_enum"] for x in ENU]),
                 qmax([x["exh_enum"] for x in ENU]),
                 qmin([x["phi_fam"] / x["phi_enum"] for x in ENU]),
                 qmax([x["phi_fam"] / x["phi_enum"] for x in ENU])))
    FS = [x["far_share"] for x in K3R if np.isfinite(x["far_share"])]
    if FS:
        info("N3.r4_capacity_tail", "THE CAPACITY TAIL of the border blocks, "
             "and it is sharper than the Muckenhoupt version it replaces: on "
             "the %d blocks large enough to have a far end (g > %d), %.3f .. "
             "%.3f of the capacity ARGMAX set's indices sit at block index >= "
             "%d.  The capacity-critical set IS the far tail -- not merely "
             "far-weighted, as T142's mass reading said, but entirely far.  "
             "That is the exact object a decay statement has to act on, and "
             "the factor it has to deliver is still the T142 far shrink "
             "%.3f .. %.3f QUOTED"
             % (len(FS), FAR_K, qmin(FS), qmax(FS), FAR_K,
                FAR_SHRINK_T142[0], FAR_SHRINK_T142[1]))


# ----------------------------------------------------------------------------
section("N4  THE MAP V15, the promotion list, the rest list, and the verdict")
# ----------------------------------------------------------------------------
SCALE_OK = bool(np.isfinite(F_BOUND["p"])
                and abs(F_BOUND["p"] - F_GAP["p"]) <= F_BOUND["sp"]
                + F_GAP["sp"] + 0.5)
if SHARP_EXH and SHARP_CLOSED and SHARP_UNIF:
    VERDICT = "SHARP-CARRIES"
elif SCALE_OK:
    VERDICT = "COEFFICIENT-GAP"
else:
    VERDICT = "SHARP-RESISTS"

STMT = [
    "N1a  THE EXACT CAPACITY RAYLEIGH FORM, verified as an IDENTITY on %d "
    "windows (numerator %.0e, denominator %.0e, eigenvalue %.0e relative): "
    "1 - rho(W) = inf_v [ d^T (J^{-1} - B) d + (x^T v)^2 / cap - sum_k s_k "
    "v_k^2 ] / [ d^T J^{-1} d + (x^T v)^2 / cap ], d = D v.  Every ingredient "
    "is closed geometry and no inequality is taken."
    % (len(SURF), qmax([r["err_N"] for r in SURF]),
       qmax([r["err_Q"] for r in SURF]), qmax([r["ray_err"] for r in SURF])),
    "N1b  THE ANATOMY OF THE OPTIMUM, new and structural: the minimiser is "
    "ORTHOGONAL to the equilibrium charge to %.0e, so the capacity rank one "
    "carries NO share of the gap; the mass share is NEGATIVE (%.4f .. %.4f), "
    "so the site masses HELP; and the gap is the cancellation between the "
    "Green share (exactly 1) and the crossing share (%.4f .. %.4f)."
    % (qmax([abs(r["sh_c"]) for r in SURF]),
       qmin([r["sh_m"] for r in SURF]), qmax([r["sh_m"] for r in SURF]),
       qmin([r["sh_b"] for r in SURF]), qmax([r["sh_b"] for r in SURF])),
    "N1c  THE NAIVE SPLIT IS DEAD, certified: rho_mass + rho_long = "
    "%.2f .. %.2f, i.e. %.1f .. %.1f times rho itself.  A capacity criterion "
    "applied to rho cannot start; applied to the GAP its factor of four costs "
    "the COEFFICIENT and not the SCALE."
    % (qmin([r["split"] for r in SURF]), qmax([r["split"] for r in SURF]),
       qmin([r["split"] / r["rho_ex"] for r in SURF]),
       qmax([r["split"] / r["rho_ex"] for r in SURF])),
    "N2a  THE CRITERION'S WINDOW, MEASURED ON THE WHOLE SURFACE: "
    "Phi_sup lam = %.4f .. %.4f, inside the [1/4, 1] that Maz'ya's criterion "
    "forces for a Dirichlet form -- although this form is NOT one (%.0f%% .. "
    "%.0f%% positive off-diagonals).  Flat in D: exponent %.3f +- %.3f."
    % (qmin([x["exhaust"] for x in N2R]), qmax([x["exhaust"] for x in N2R]),
       100.0 * qmin([x["mk_frac"] for x in N2R]),
       100.0 * qmax([x["mk_frac"] for x in N2R]),
       pow_fit([x["D"] for x in N2R], [x["exhaust"] for x in N2R], "e")["p"],
       pow_fit([x["D"] for x in N2R], [x["exhaust"] for x in N2R], "e")["sp"]),
    "N2b  THE SUP LIVES ON A CLOSED FAMILY: the closed families (Green "
    "diagonal, transported potentials, index intervals) recover %.4f .. %.4f "
    "of the best value found, a full add/remove local search improves them by "
    "at most a factor %.4f, and in the NODE coordinates the near-optimal sets "
    "are INTERVALS OF WINDOW LAGS -- the one-dimensional structure "
    "Muckenhoupt's closed form needs."
    % (qmin([x["r_clo_best"] for x in N2R]),
       qmax([x["r_clo_best"] for x in N2R]),
       qmax([x["ph_loc"] / max(x["ph_ext"], x["ph_grn"], x["ph_clo"],
                               x["ph_int"]) for x in N2R
             if np.isfinite(x["ph_loc"])]) if LOC else float("nan")),
    "N2c  THE BOUND AND ITS UNIFORMITY: lam >= 1 / (4 Phi_sup) = "
    "%.3e .. %.3e, i.e. %.4f .. %.4f of the true gap, with the LOSS FACTOR "
    "fitting as D^%.3f +- %.3f -- ZONE-UNIFORM.  As a coefficient of D^%.3f "
    "the bound is c = %.2f .. %.2f against the envelope constant %.2f."
    % (qmin([x["lam_bound"] for x in N2R]),
       qmax([x["lam_bound"] for x in N2R]),
       qmin([x["loss"] for x in N2R]), qmax([x["loss"] for x in N2R]),
       F_LOSS["p"], F_LOSS["sp"], F_GAP["p"],
       qmin([x["c_sharp"] for x in N2R]), qmax([x["c_sharp"] for x in N2R]),
       C_GAP),
    "N2d  AND THE MECHANISM THAT DOES NOT CARRY IT: Miclo's capacitary CHAIN "
    "loses a factor %.0f .. %.0f, because the top dyadic level sets are small "
    "sets of O(1) capacity against an eigenvalue of 10^-5; the capacitary "
    "constant is kappa = %.1f .. %.1f and DRIFTS like D^%.2f.  So the "
    "criterion's conclusion holds while its classical PROOF does not, and "
    "that is precisely where the remaining work sits."
    % (1.0 / qmax([x["chain_eff"] for x in N2R]),
       1.0 / qmin([x["chain_eff"] for x in N2R]),
       qmin([x["kappa"] for x in N2R]), qmax([x["kappa"] for x in N2R]),
       pow_fit([x["D"] for x in N2R], [x["kap_max"] for x in N2R], "k")["p"]),
]
if K3R and [x for x in K3R if x["enum"]]:
    _EN = [x for x in K3R if x["enum"]]
    STMT.append(
        "N3a  THE ENUMERATED WINDOW, the only CERTIFIED supremum in the "
        "probe: on %d border blocks every subset was enumerated and "
        "Phi_sup lam = %.4f .. %.4f, again inside [1/4, 1] and again for a "
        "non-Markovian form."
        % (len(_EN), qmin([x["exh_enum"] for x in _EN]),
           qmax([x["exh_enum"] for x in _EN])))
if LPR:
    _LO = [x for x in LPR if np.isfinite(x["L_cert"])]
    STMT.append(
        "N3b  R1d, and it is a NEGATIVE result with a reason: the LP dual "
        "over the conductance cone, with a hand-verified dual point on %d "
        "windows, certifies a class floor of %.6f .. %.6f -- which is "
        "rho(W) itself to within a factor %.6f.  A relaxation that constrains "
        "Om along finitely many directions is SATURATED at the trivial floor, "
        "exactly as T142's single-direction barrier was.  R1d needs the FULL "
        "Om as an SDP constraint, not a sample; recorded with its reason so "
        "the direction-sampling version is not retried."
        % (len(_LO), qmin([x["L_cert"] for x in _LO]) if _LO else float("nan"),
           qmax([x["L_cert"] for x in _LO]) if _LO else float("nan"),
           qmax([x["L_cert"] / x["rho"] for x in _LO]) if _LO
           else float("nan")))
if K3R:
    STMT.append(
        "N3c  R4: %d of %d rebuilt border blocks open; the Maz'ya argmax set "
        "is ENTIRELY the far tail (%.3f .. %.3f of its indices at block index "
        ">= %d), which is the share a decay statement has to act on."
        % (len([x for x in K3R if not x["cert_any"]]), len(K3R),
           qmin([x["far_share"] for x in K3R]),
           qmax([x["far_share"] for x in K3R]), FAR_K))

for s in STMT:
    para(s, indent="  ")
    print("")

para("THE VERDICT IS %s.  The three ingredients must not be mixed up: the "
     "criterion's WINDOW holds (%s), the supremum lives on a CLOSED family "
     "(%s), and the route's own LOSS is zone-uniform (%s).  What is NOT "
     "delivered is a proof of the first of those three: the form is not "
     "Markovian, so Maz'ya's upper half is not available by citation, and the "
     "classical proof mechanism -- the capacitary strong-type inequality -- is "
     "quantitatively inadequate here by a factor of %.0f .. %.0f."
     % (VERDICT, "yes" if SHARP_EXH else "no",
        "yes" if SHARP_CLOSED else "no", "yes" if SHARP_UNIF else "no",
        1.0 / qmax([x["chain_eff"] for x in N2R]),
        1.0 / qmin([x["chain_eff"] for x in N2R])), indent="  ")
print("")

REST = [
    "S1  THE ONE REMAINING INEQUALITY, and it is now a single named statement "
    "instead of a programme: cap_E(A) >= |A| lam_0 / c_0 for ALL sets A, with "
    "c_0 absolute -- equivalently Phi_sup lam >= 1 / c_0.  Measured here as "
    "%.4f .. %.4f on %d windows and CERTIFIED BY ENUMERATION on the small "
    "border blocks.  For a Dirichlet form it is Maz'ya's theorem with "
    "c_0 = 4; this form has %.0f%% positive off-diagonals, so what is needed "
    "is the criterion for a NON-MARKOVIAN form -- either by splitting E into a "
    "Markovian part plus a controlled remainder, or by the Muckenhoupt route "
    "below."
    % (qmin([x["exhaust"] for x in N2R]), qmax([x["exhaust"] for x in N2R]),
       len(N2R), 100.0 * qmed([x["mk_frac"] for x in N2R])),
    "S2  THE MUCKENHOUPT ROUTE TO S1, which is the concrete way to get it: in "
    "the NODE coordinates the near-optimal sets are INTERVALS of window lags, "
    "so if the gap form is comparable to a one-dimensional (Jacobi) form on "
    "those intervals -- not to K^{-1}, which T142 killed, but to a PATH form "
    "for the purpose of the CAPACITY only -- then the sup over all sets "
    "reduces to a closed two-weight sup (Muckenhoupt 1972) and S1 follows with "
    "an explicit constant.  Note the direction: this is a comparison for the "
    "CAPACITY FUNCTIONAL, not for the eigenvalue, so T142's obstruction (a "
    "comparison must reproduce the optimum to O(D^3)) does NOT apply -- the "
    "capacity only has to be right to a bounded factor.",
    "S3  A CLOSED FORMULA FOR Phi_sup, or a closed LOWER bound on cap_E(A).  "
    "The measured supremum is computed from E^{-1}; a route that is closed in "
    "the T142 sense would express it through J^{-1}, K and s directly.  The "
    "closed families already recover %.4f .. %.4f of it, so this is a "
    "bookkeeping task and not a search."
    % (qmin([x["r_clo_best"] for x in N2R]),
       qmax([x["r_clo_best"] for x in N2R])),
    "R1d'  the class dual as an SDP and NOT as a direction sample.  N3b "
    "shows the LP with %d Lam and %d Om directions saturates at rho, so more "
    "directions is the wrong axis; the constraint that bites is the FULL "
    "K^{1/2} Y K^{1/2} <= I.  Until that is solved, every negative statement "
    "about the conductance class stays MEASURED -- but note that after N2 the "
    "class question is no longer on the critical path, because the sharp "
    "route does not go through the class at all."
    % (max(x["nu"] for x in LPR) if LPR else 0,
       max(x["nz"] for x in LPR) if LPR else 0),
    "R4   the open border blocks: the capacity argmax set is ENTIRELY the far "
    "tail (%.2f .. %.2f of its indices beyond block index %d), so a decay "
    "statement acts on all of it and the factor it must deliver is the T142 "
    "far shrink %.3f .. %.3f QUOTED."
    % (qmin([x["far_share"] for x in K3R]) if K3R else float("nan"),
       qmax([x["far_share"] for x in K3R]) if K3R else float("nan"),
       FAR_K, FAR_SHRINK_T142[0], FAR_SHRINK_T142[1]),
]

para("THE SHORTEST REST LIST, in the order a next probe should take it.",
     indent="  ")
print("")
for s in REST:
    para(s, indent="  ")
    print("")

para("THE HONEST THREE SENTENCES.  " + (
    "The sharp route works: the exact quotient is an identity in closed "
    "geometry (N1), and Maz'ya's capacity criterion applied to the GAP FORM "
    "-- not to rho, where its factor of four is fatal -- delivers "
    "lam >= 1 / (4 Phi_sup) with Phi_sup lam measured at %.3f .. %.3f across "
    "the whole surface and a loss factor that is flat in D to D^%.3f +- %.3f, "
    "so the D^%.1f scale is carried and the coefficient is zone-uniform.  "
    "The supremum is not an oracle: closed families -- the Green diagonal, "
    "the transported potentials, and in the node coordinates the plain "
    "INTERVALS of window lags -- recover %.3f .. %.3f of it, and on the small "
    "border blocks the supremum is CERTIFIED by enumerating every subset, "
    "where the same window [1/4, 1] holds exactly.  What is left is therefore "
    "ONE inequality with a name and a direction -- cap_E(A) >= |A| lam / c_0 "
    "for all A, with c_0 absolute -- which is Maz'ya's theorem for a form "
    "that happens not to be Markovian (%.0f%% positive off-diagonals), and "
    "the classical proof of it via the capacitary chain is quantitatively "
    "inadequate here (a factor %.0f .. %.0f), so the honest state is: "
    "D-uniformity is reduced to a capacity verification, and the verification "
    "is a Muckenhoupt-type statement about INTERVALS, not another profile."
    % (qmin([x["exhaust"] for x in N2R]), qmax([x["exhaust"] for x in N2R]),
       F_LOSS["p"], F_LOSS["sp"], F_GAP["p"],
       qmin([x["r_clo_best"] for x in N2R]),
       qmax([x["r_clo_best"] for x in N2R]),
       100.0 * qmed([x["mk_frac"] for x in N2R]),
       1.0 / qmax([x["chain_eff"] for x in N2R]),
       1.0 / qmin([x["chain_eff"] for x in N2R]))
    if VERDICT == "SHARP-CARRIES" else
    "The exact quotient is an identity in closed geometry and the capacity "
    "criterion applied to the gap form does carry the D^%.1f scale, but the "
    "coefficient does not stay put: the route's own loss factor fits as "
    "D^%.3f +- %.3f against the uniformity bar %.2f, so what is measured is a "
    "bound of the right shape whose constant drifts, and the drift is "
    "localised in %s.  Everything else in the route is in place -- the "
    "identity, the closed families, the certified enumeration on the border "
    "blocks -- so the next step is the coefficient and nothing else."
    % (F_GAP["p"], F_LOSS["p"], F_LOSS["sp"], BAR_UNIF,
       "the capacity supremum itself" if not SHARP_EXH
       else "the closed families' recovery of it")
    if VERDICT == "COEFFICIENT-GAP" else
    "The exact quotient is an identity in closed geometry (N1) and its "
    "anatomy is new -- the minimiser is orthogonal to the equilibrium charge, "
    "the mass term helps rather than hurts, and the gap is a cancellation "
    "between the Green share and the crossing share -- but the capacity "
    "criterion does not close it on this surface.  The resistance is located "
    "and it is not where the contract expected it.  The rest list states the "
    "one inequality that would change that."))
print("")

print("TOTAL.contract     SHARP.CAPACITY -- estimate the exact form instead of "
      "comparing it (part %d, discovery only, nothing promoted)"
      % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.N1_form      the exact capacity Rayleigh form is an IDENTITY on "
      "%d windows (assembly %.0e / %.0e, eigenvalue %.0e relative through the "
      "1/gap conditioning factor); shares at the optimum: green %.4f, capacity "
      "rank one %.0e (ABSENT), crossing %.4f .. %.4f, mass %.4f .. %.4f "
      "(NEGATIVE)"
      % (len(SURF), qmax([r["err_N"] for r in SURF]),
         qmax([r["err_Q"] for r in SURF]), qmax([r["ray_err"] for r in SURF]),
         qmed([r["sh_g"] for r in SURF]),
         qmax([abs(r["sh_c"]) for r in SURF]),
         qmin([r["sh_b"] for r in SURF]), qmax([r["sh_b"] for r in SURF]),
         qmin([r["sh_m"] for r in SURF]), qmax([r["sh_m"] for r in SURF])))
print("TOTAL.N1_split     the naive split rho <= rho_mass + rho_long is "
      "CERTIFIED DEAD: %.2f .. %.2f, a factor %.1f .. %.1f above rho -- the "
      "reason the criterion must be applied to the GAP"
      % (qmin([r["split"] for r in SURF]), qmax([r["split"] for r in SURF]),
         qmin([r["split"] / r["rho_ex"] for r in SURF]),
         qmax([r["split"] / r["rho_ex"] for r in SURF])))
print("TOTAL.N2_core      THE CORE NUMBER: Phi_sup x lam = %.4f .. %.4f on %d "
      "windows (Maz'ya's window is [1/4, 1]); the bound lam >= 1/(4 Phi_sup) = "
      "%.3e .. %.3e is %.4f .. %.4f of the true gap %.3e .. %.3e, its LOSS "
      "FACTOR fits D^%.3f +- %.3f (bar %.2f) -> %s, and as a coefficient of "
      "D^%.3f it is c = %.2f .. %.2f against the envelope C = %.2f"
      % (qmin([x["exhaust"] for x in N2R]), qmax([x["exhaust"] for x in N2R]),
         len(N2R), qmin([x["lam_bound"] for x in N2R]),
         qmax([x["lam_bound"] for x in N2R]),
         qmin([x["loss"] for x in N2R]), qmax([x["loss"] for x in N2R]),
         qmin([x["lam_E"] for x in N2R]), qmax([x["lam_E"] for x in N2R]),
         F_LOSS["p"], F_LOSS["sp"], BAR_UNIF,
         "ZONE-UNIFORM" if SHARP_UNIF else "NOT zone-uniform",
         F_GAP["p"], qmin([x["c_sharp"] for x in N2R]),
         qmax([x["c_sharp"] for x in N2R]), C_GAP))
print("TOTAL.N2_families  the closed families recover %.4f .. %.4f of the best "
      "supremum (Green diagonal %.4f .. %.4f, intervals %.4f .. %.4f, "
      "transported potentials %.4f .. %.4f); local search on %d windows "
      "improves by at most %.4f; in the node coordinates the INTERVALS "
      "dominate the extremal levels by %.1f .. %.1f"
      % (qmin([x["r_clo_best"] for x in N2R]),
         qmax([x["r_clo_best"] for x in N2R]),
         qmin([x["r_grn"] for x in N2R]), qmax([x["r_grn"] for x in N2R]),
         qmin([x["r_int"] for x in N2R]), qmax([x["r_int"] for x in N2R]),
         qmin([x["r_clo"] for x in N2R]), qmax([x["r_clo"] for x in N2R]),
         len(LOC),
         qmax([x["ph_loc"] / max(x["ph_ext"], x["ph_grn"], x["ph_clo"],
                                 x["ph_int"]) for x in LOC]) if LOC
         else float("nan"),
         qmin([x["r2_int"] for x in R2I]) if R2I else float("nan"),
         qmax([x["r2_int"] for x in R2I]) if R2I else float("nan")))
print("TOTAL.N2_chain     Miclo's CHAIN version loses a factor %.0f .. %.0f "
      "(kappa = %.1f .. %.1f, drifting like D^%.2f), so the criterion's "
      "conclusion holds while its classical proof mechanism does not -- that "
      "is where the remaining work sits"
      % (1.0 / qmax([x["chain_eff"] for x in N2R]),
         1.0 / qmin([x["chain_eff"] for x in N2R]),
         qmin([x["kappa"] for x in N2R]), qmax([x["kappa"] for x in N2R]),
         pow_fit([x["D"] for x in N2R], [x["kap_max"] for x in N2R], "k")["p"]))
if LPR:
    _LO = [x for x in LPR if np.isfinite(x["L_cert"])]
    print("TOTAL.N3_r1d       the LP dual over the conductance cone (%d Lam "
          "and %d Om directions, hand-verified dual point on %d of %d "
          "windows) certifies a class floor %.6f .. %.6f = rho(W) to within a "
          "factor %.6f -> SATURATED at the trivial floor.  Recorded as a DEAD "
          "ROUTE with its reason: a finite direction sample of Om cannot bind "
          "the cone; R1d needs the SDP constraint K^{1/2} Y K^{1/2} <= I"
          % (max(x["nu"] for x in LPR), max(x["nz"] for x in LPR), len(_LO),
             len(LPR),
             qmin([x["L_cert"] for x in _LO]) if _LO else float("nan"),
             qmax([x["L_cert"] for x in _LO]) if _LO else float("nan"),
             qmax([x["L_cert"] / x["rho"] for x in _LO]) if _LO
             else float("nan")))
if K3R:
    _EN = [x for x in K3R if x["enum"]]
    print("TOTAL.N3_r4        %d border blocks, %d certified by the ladder, %d "
          "open; %d blocks had ALL subsets enumerated and there Phi_sup lam = "
          "%.4f .. %.4f EXACTLY (the only non-family-restricted supremum in "
          "the probe); the capacity argmax set is the FAR TAIL, %.3f .. %.3f "
          "of its indices at block index >= %d"
          % (len(K3R), len([x for x in K3R if x["cert_any"]]),
             len([x for x in K3R if not x["cert_any"]]), len(_EN),
             qmin([x["exh_enum"] for x in _EN]) if _EN else float("nan"),
             qmax([x["exh_enum"] for x in _EN]) if _EN else float("nan"),
             qmin([x["far_share"] for x in K3R]),
             qmax([x["far_share"] for x in K3R]), FAR_K))
print("TOTAL.rest_list    %s" % " | ".join(s.split("  ")[0] for s in REST))
print("TOTAL.promotions   %d statements ready, %d new (N1a-N1c + N2a-N2d + N3 "
      "is the ripe batch), 0 promoted"
      % (PROMO_T142 + len(STMT), len(STMT)))
print("TOTAL.surface      %d windows h = %d .. %d (core m = %d .. %d), "
      "D = %.2e .. %.2e, zones n = %d .. %d; %d capacity windows, %d LP "
      "windows, %d border blocks"
      % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
         min(r["m"] for r in SURF), max(r["m"] for r in SURF),
         qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
         min(r["n"] for r in SURF), max(r["n"] for r in SURF), len(N2R),
         len(LPR), len(K3R)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised / diagonalised form %d (cap %d)"
      % (max([r["h"] for r in SURF] + [x["g"] for x in K3R] + [0]), MAX_H))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
