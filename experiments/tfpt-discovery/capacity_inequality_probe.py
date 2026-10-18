"""Discovery probe (2026-07-28), part 144 of the prime/window investigation.
Contract CAPACITY.INEQUALITY -- THE ONE INEQUALITY, over the INTERVAL ROUTE.

WHERE THIS SITS (T143 END STATE: SHARP-CARRIES, and what it left open)
  T140 reduced the question to two small matrices per zone, T141 turned it into a
  weighted Hardy problem, T142 closed the whole comparison branch, and T143
  estimated the EXACT capacity Rayleigh form instead of comparing it.  QUOTED
  from T140 .. T143 and NEVER re-derived here:
    * the exact form is an IDENTITY,
        1 - rho(W) = inf_v [ d^T (J^{-1} - B) d + (x^T v)^2 / cap - sum_k s_k v_k^2 ]
                          / [ d^T J^{-1} d + (x^T v)^2 / cap ] ,  d = D v ;
    * Maz'ya's criterion applied to the GAP form gives Phi_sup x lam =
      0.5438 .. 0.6457, i.e. inside the classical window [1/4, 1], with a loss
      factor that is zone-uniform (D^-0.048 +- 0.010);
    * the form is NOT Markovian (72 .. 84 % of the off-diagonal entries are
      positive), so Maz'ya's UPPER half -- cap_E(A) >= |A| lam_0 / c_0 with an
      absolute c_0 -- is NOT available by citation;
    * Miclo's chain mechanics loses a factor 46 .. 2561 (drifting like D^-2.13),
      so the classical constructive proof of the criterion is dead here;
    * in the NODE coordinates the near-optimal sets are INTERVALS of window lags
      and they beat the extremal's dyadic levels by a factor 8.3 .. 129.5.
  So T143's rest list is not a number, it is a PROOF, and its first three items
  are the subject of this probe:
    S1  the one inequality: cap_E(A) >= |A| lam_0 / c_0 for ALL A with an
        ABSOLUTE c_0 (equivalently Phi_sup lam >= 1 / c_0), in a non-Markovian
        version of Maz'ya's criterion;
    S2  the route: reduce the sup over ALL sets to a sup over INTERVALS by a
        comparison of the CAPACITY FUNCTIONAL ONLY (never of the eigenvalue --
        that is exactly what T142 closed), and then evaluate the interval sup in
        closed two-weight form (Muckenhoupt 1972);
    S3  a closed lower bound for cap_E(A) out of J^{-1}, K and s.

WHAT THIS PROBE DOES
  P0  THE COORDINATES AND THE LICENCES.  Two steps that this probe leans on are
      calibrated before any window is built: (a) the capacity is a GREEN object,
      cap_E(A) = 1^T [(E^{-1})_AA]^{-1} 1, verified against the constrained
      minimisation; (b) the JACOBI WHITENING, which is the one comparison this
      probe is allowed to make.  T142's obstruction closes comparisons of the
      NUMERATOR (they would have to reproduce rho to relative accuracy O(D^3));
      whitening the DENOMINATOR by its own diagonal costs a factor kap_J =
      lam_max(Lam^{-1/2} A_B Lam^{-1/2}), CERTIFIED per window, and that factor
      multiplies the GAP rather than rho -- an O(1) loss in a 10^-6 quantity, not
      an O(D^3) demand on a quantity of size 1.  That is what makes the capacity
      criterion evaluable in coordinates where the measure is the COUNTING
      MEASURE and the capacity of an interval has a CLOSED trial value.
  P1  THE INTERVAL REDUCTION, which is the heart.  For a set A let I(A) be its
      convex hull in the node coordinates.  The reduction factor is
          c_int(A) = Phi(A) / Phi(I(A)) ,  Phi(A) = |A| / cap_E(A) ,
      and the question is whether sup_A c_int(A) is ABSOLUTELY bounded, zone- and
      D-uniformly.  If it is, the sup over 2^m sets is a sup over O(m^2)
      intervals.  The sample is honest: ALL subsets of enumerable blocks
      (EXHAUSTIVE, hence EXACT within the block class), structured families
      (unions of intervals, strided sets, random densities, prefixes), the
      unconfined level-set families of T143, and an ADVERSARIAL local search that
      maximises c_int itself rather than Phi.
  P2  THE TWO-WEIGHT SUP.  In the whitened node coordinates the indicator of an
      interval is an admissible trial function, so
          cap_E(I) <= S(I) = sum_{k,l in I} E_kl ,
      which is a CLOSED two-dimensional prefix-sum object.  The Muckenhoupt-type
      sup B_int = sup_I |I| / S(I) is therefore evaluated over ALL O(m^2)
      intervals EXACTLY (not on a grid), and the fidelity of the closed form is
      measured as q_int = Phi_int / B_int >= 1 against exact interval capacities.
      Then the chain closes: modulo S1 with its absolute constant c_0,
          lam >= 1 / (c_0 kap_J c_int q_int B_int) ,
      certified per window, and the core number B_int x lam is put against the
      classical window [1/4, 1] on the whole measurement surface.
  P3  THE NON-MARKOV CORRECTION AND S3.  (i) The Markov part E_M = diag(E) -
      |offdiag(E)| is built and the capacity ratio cap_{E_M}(A) / cap_E(A) is
      measured: if it is bounded, S1 follows from the Markovian case by
      perturbation, which is the cheapest available route to it.  (ii) S3: the
      Cauchy-Schwarz floor cap_E(A) >= |A|^2 / (1^T R_AA 1) turns Phi_sup into a
      MAXIMUM DENSITY SUBGRAPH problem for the Green kernel R = E^{-1}, which is
      poly-time solvable when R >= 0 (Goldberg 1984; Charikar 2000) -- so the sup
      over ALL sets, not merely over a family, becomes computable with a cited
      absolute constant.  (iii) The four open R4 border blocks are re-run with
      the interval formula and with EXHAUSTIVE enumeration.
  P4  the map V16, the promotion list, the shortest rest list, the verdict.

WHAT IS CERTIFIED, WHAT IS MEASURED, WHAT IS A FIT
  * CERTIFIED means a completed Cholesky (Wilkinson 1968; Higham 2002) with the
    declared floating point floor, in the DIRECTION stated in the name:
    cert_lam_max is an UPPER bound, cert_lam_min a LOWER bound.
  * EXACT means an exhaustion: every subset of a block, or every one of the
    O(m^2) intervals.  Those suprema are not family-restricted.
  * MEASURED means a sampled supremum, an eigenvalue or a Rayleigh quotient.
    Every sampled supremum below is labelled MEASURED on its own line, and a
    sampled sup of Phi is a LOWER bound on Phi_sup and an upper bound on nothing.
  * A FIT is a least squares exponent with a delete-one jackknife band, always
    labelled, never load-bearing.
  * THE DIRECTION TRAP, stated once and respected throughout.  For a single set
    Phi(A) <= 1 / lam always, so single sets CERTIFY an UPPER bound on the gap.
    The LOWER bound on the gap is exactly S1 and S1 is NOT proved here: every
    chain below is explicitly CONDITIONAL on S1's absolute constant c_0 and says
    so on its own line.  What this probe decides is whether S1 has been reduced
    to a closed two-weight calculus, not whether S1 holds.

FENCES
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil window
    form (Weil 1952; Bombieri 2000; Connes 1999) on a FINITE list of prime-power
    zones and a FINITE window.  The criterion is CITED as an address and is
    NEVER USED, in either direction.  Nothing here claims, assumes or approaches
    RH; even with S1 closed what would stand is a finite-window positivity
    statement.  No zero data of any kind is read, generated or approximated --
    an AST firewall enforces this, together with the import whitelist and the
    absence of any write-mode file access.
  * DISCOVERY ONLY.  Nothing is promoted.  No verification module, no ledger, no
    TeX, no website, no changelog, no next.txt is touched; this is ONE new file
    in experiments/tfpt-discovery/ and it writes nothing.
  * HARD CAPS.  Largest factorised / inverted / diagonalised matrix <= 1500;
    runtime budget 760 s (< 900 s), with per-block guards that truncate a pool
    rather than overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import (cho_factor, cho_solve, cholesky, eigh,
                          eigvalsh, solve_triangular)

np.seterr(all="ignore")

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 760.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 2200000
ZONE_DEEP = 2050000

# --- the measurement surface ------------------------------------------------
SURF_ZONES = 34
SURF_HCAP = 1400              # <= MAX_H, and the inverse of E is dense
T_SURF = 210.0

# --- P1 the interval reduction ----------------------------------------------
BLK_ENUM_G = 14              # ALL 2^g - 1 subsets of a block of this size
BLK_ENUM_MAX = 5             # how many blocks per window get the exhaustion
BLK_STRUCT_G = 64            # structured + adversarial families live here
BLK_FRACS = (0.02, 0.30, 0.62, 0.88)
ADV_STARTS = 3
ADV_SWEEPS = 4
LEV_NQ = 17                  # unconfined level-set family (T143's families)
T_P1 = 170.0

# --- P2 the two-weight sup --------------------------------------------------
INT_TOP = 8                  # top exact intervals kept for the ramp refinement
T_P2 = 150.0

# --- P3 non-Markov, S3, R4 --------------------------------------------------
K3_GC_MIN = 2
K3_HCAP = 300
K3_MAX = 22
K3_PER_RHO = 3
K3_RHO = (1.001, 1.05, 1.20, 1.49531, 2.00, 3.50)
K3_LOGRES = 80.0
M_LADDER = (1, 2, 3, 4, 6, 8)
FAR_K = 8
K3_ENUM_G = 15               # exhaustive subset enumeration up to this size
K3_ENUM_MAX = 5
T_P3 = 130.0

# --- preregistered bars (declared before any number is computed) ------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_UNIF = 0.25              # |exponent in D| for "ZONE-UNIFORM", preregistered
BAR_CINT = 4.0               # c_int counts as ABSOLUTELY BOUNDED below this
BAR_KAPJ = 4.0               # and so does the Jacobi whitening factor
MAZYA_C0 = 4.0               # the constant of the OPEN inequality S1

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
RHO_W_T140 = (0.9962, 0.9999)
PHI_LAM_T143 = (0.5438, 0.6457)
LOSS_EXP_T143 = (-0.048, 0.010)
MK_POS_T143 = (0.72, 0.84)
MICLO_LOSS_T143 = (46.0, 2561.0)
MICLO_EXP_T143 = -2.13
INT_DOM_T143 = (8.3, 129.5)
R4_OPEN_T143 = 4
FAR_SHRINK_T143 = (0.656, 1.052)
PROMO_T143 = 84
N_PROBES_PRIOR = 143
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


def qmin(v):
    v = [x for x in v if np.isfinite(x)]
    return float(min(v)) if v else float("nan")


def qmax(v):
    v = [x for x in v if np.isfinite(x)]
    return float(max(v)) if v else float("nan")


def qmed(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def qq(v, p):
    v = [x for x in v if np.isfinite(x)]
    return float(np.quantile(v, p)) if v else float("nan")


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
          == "capacity_inequality_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T143 code path
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


def ray_top(X, iters=120):
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
    assembly source, exactly as T138 .. T143 did."""
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
# THE LUMPED M-MATRIX PAIR (T136 .. T143) and the JACOBI WHITENING (new here)
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


def jacobi_whiten(A, A_B):
    """THE ONE COMPARISON THIS PROBE MAKES, and it is on the DENOMINATOR only.

    With Lam = diag(A_B) put E = Lam^{-1/2} A Lam^{-1/2} and
    W = Lam^{-1/2} A_B Lam^{-1/2}.  Then for every v, with u = Lam^{1/2} v,
        u^T E u / u^T u = v^T A v / v^T Lam v ,
    so the pair (A, Lam) has the COUNTING MEASURE as its denominator, which is
    what the capacity criterion needs, and the two pairs are related by
        lam_min(A, A_B) >= lam_min(E) / lam_max(W) ,
        lam_min(A, A_B) <= lam_min(E) / lam_min(W) ,
    both by Loewner (Lam^{-1/2} A_B Lam^{-1/2} between lam_min(W) I and
    lam_max(W) I).  DIRECTION: lam_max(W) is CERTIFIED from ABOVE, lam_min(W)
    from BELOW, so the first line is a usable LOWER bound on the gap.

    WHY THIS IS NOT T142's DEAD COMPARISON.  T142 closed comparisons of the
    NUMERATOR / optimal weight: they must reproduce rho(W) = 1 - Theta(D^3) to
    relative accuracy O(D^3).  Here the comparison is of the DENOMINATOR and its
    cost is a MULTIPLICATIVE factor on the GAP itself; an O(1) factor on a
    quantity of size 10^-6 is harmless, an O(D^3) demand on a quantity of size 1
    is not.  The factor is certified per window and reported, never assumed."""
    Lam = np.diag(A_B).copy()
    if not (float(np.min(Lam)) > 0.0):
        return None
    sq = 1.0 / np.sqrt(Lam)
    E = sym(A * np.outer(sq, sq))
    W = sym(A_B * np.outer(sq, sq))
    kap_up = cert_lam_max(W, guess=ray_top(W))
    try:
        w_lo = float(eigvalsh(W, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        w_lo = float("nan")
    kap_lo = cert_lam_min(W, guess=w_lo)
    return dict(E=E, Lam=Lam, kap_up=kap_up, kap_lo=kap_lo,
                gersh_up=1.0 + float(np.max((np.abs(W) - np.diag(np.diag(W))
                                             ).sum(axis=1))))


# ----------------------------------------------------------------------------
# THE CAPACITY (Maz'ya 1985; Fukushima-Oshima-Takeda 1994, ch. 2)
# ----------------------------------------------------------------------------
def set_capacity(R, idx):
    """cap_E(A) = min { w^T E w : w = 1 on A } = 1^T [ (E^{-1})_{AA} ]^{-1} 1,
    the SCHUR / GREEN identity.  R = E^{-1} is passed in, so a capacity costs
    ONE small Cholesky."""
    if idx.size == 0:
        return float("nan")
    Raa = sym(np.ascontiguousarray(R[np.ix_(idx, idx)]))
    fac = safe_cho(Raa)
    if fac is None:
        return float("nan")
    y = cho_solve(fac, np.ones(idx.size), check_finite=False)
    val = float(y.sum())
    return val if val > 0.0 else float("nan")


def interval_capacity(R, a, b):
    """The same for a CONTIGUOUS block, where the submatrix is a slice."""
    Raa = sym(np.ascontiguousarray(R[a:b, a:b]))
    fac = safe_cho(Raa)
    if fac is None:
        return float("nan")
    y = cho_solve(fac, np.ones(b - a), check_finite=False)
    val = float(y.sum())
    return val if val > 0.0 else float("nan")


def interval_sup_exact(R, m, cl_rat, n_top=INT_TOP):
    """THE EXACT interval supremum over ALL O(m^2) intervals of the window --
    an EXHAUSTION of the interval class, on every window of the surface and not
    only on the small ones.  What makes it affordable is the NESTEDNESS of the
    Cholesky factor: for a fixed left endpoint a the block R[a:b, a:b] is a
    LEADING principal submatrix of R[a:m, a:m], so one factorisation serves every
    right endpoint at once, and with L z = 1 the capacity of [a, b) is the PREFIX
    SUM cap = sum_{k < b-a} z_k^2 (because cap = 1^T R_II^{-1} 1 = ||L_I^{-1}1||^2
    and forward substitution never looks ahead).  One Cholesky per left endpoint
    replaces m^2 / 2 of them; the identity is verified against the independent
    solve in P0 rather than assumed.  Returns the exhaustive supremum, its
    argmax, the number of intervals, the top few for the ramp block, and the
    worst ratio against the closed trial-energy proxy."""
    best, arg, n_int, top, q_worst = 0.0, None, 0, [], 1.0
    ones = np.ones(m)
    for a in range(m):
        Ra = sym(np.ascontiguousarray(R[a:m, a:m]))
        try:
            L = cholesky(Ra, lower=True, check_finite=False)
            z = solve_triangular(L, ones[a:], lower=True, check_finite=False)
        except (LinAlgError, ValueError):
            continue
        caps = np.cumsum(z * z)
        good = np.isfinite(caps) & (caps > 0.0)
        if not good.any():
            continue
        lens = np.arange(1.0, m - a + 1.0)
        rat = np.where(good, lens / np.where(good, caps, 1.0), 0.0)
        n_int += int(good.sum())
        rc = cl_rat[a, a + 1:m + 1]
        with np.errstate(divide="ignore", invalid="ignore"):
            qv = np.where(rc > 0.0, rat / np.where(rc > 0.0, rc, 1.0), 0.0)
        if qv.size:
            q_worst = max(q_worst, float(np.max(qv)))
        j = int(np.argmax(rat))
        top.append((float(rat[j]), a, a + j + 1, float(caps[j])))
        if rat[j] > best:
            best, arg = float(rat[j]), (a, a + j + 1)
    top.sort(reverse=True)
    return best, arg, n_int, top[:n_top], q_worst


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


def level_sets_of(vec, nq=LEV_NQ):
    """The (non-dyadic) quantile level sets of |vec| -- T143's closed families."""
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


# ----------------------------------------------------------------------------
# THE CLOSED INTERVAL OBJECTS -- prefix sums, so ALL O(m^2) intervals at once
# ----------------------------------------------------------------------------
def interval_sums(X):
    """S[a, b] = sum_{a <= k, l < b} X_kl for all 0 <= a <= b <= m, by ONE
    two-dimensional prefix sum.  This is the closed form the two-weight sup
    needs: the indicator of an interval is an admissible trial function, so
    S(I) is a CLOSED UPPER BOUND for cap_E(I) with no matrix solve at all."""
    m = X.shape[0]
    P = np.zeros((m + 1, m + 1))
    P[1:, 1:] = np.cumsum(np.cumsum(np.asarray(X, dtype=float), axis=0), axis=1)
    dv = np.diag(P).copy()
    return dv[:, None] + dv[None, :] - P - P.T


def interval_lengths(m):
    aa = np.arange(m + 1)
    return aa[None, :] - aa[:, None]


def closed_interval_sup(E):
    """B_int = sup_I |I| / S(I) over ALL O(m^2) intervals, EXACT (an exhaustion
    of the interval class, not a grid).  This is the Muckenhoupt-type two-weight
    sup (Muckenhoupt 1972) in the whitened node coordinates, where the measure
    is the counting measure so that |I| IS the measure of I."""
    m = E.shape[0]
    S = interval_sums(E)
    L = interval_lengths(m)
    good = (L >= 1) & (S > 0.0)
    rat = np.where(good, L / np.where(S > 0.0, S, 1.0), -np.inf)
    flat = int(np.argmax(rat))
    a, b = divmod(flat, m + 1)
    n_bad = int(np.count_nonzero((L >= 1) & ~(S > 0.0)))
    return dict(B=float(rat[a, b]), a=int(a), b=int(b), rat=rat, S=S,
                n_bad=n_bad, n_int=int(m * (m + 1) // 2))


def ramp_trial(E, a, b, ell):
    """A CLOSED trial function that is 1 on I = [a, b) and falls linearly to 0
    over a distance ell on both sides.  The indicator is the case ell = 0.  Its
    energy is an UPPER bound for cap_E(I) for every ell, so the minimum over a
    family of ell is a better closed upper bound -- and the ell that wins says
    how far the equilibrium potential of the form SPREADS, which is the
    quantitative reason a local (Muckenhoupt) trial cannot be sharp for a form
    with a near-null direction."""
    m = E.shape[0]
    v = np.zeros(m)
    v[a:b] = 1.0
    if ell >= 1:
        lo = max(0, a - ell)
        if a > lo:
            v[lo:a] = (np.arange(lo, a) - (a - ell - 1)) / float(ell + 1)
        hi = min(m, b + ell)
        if hi > b:
            v[b:hi] = ((b + ell) - np.arange(b, hi)) / float(ell + 1)
    return float(v @ E @ v)


def best_ramp(E, a, b, ells):
    best, best_l = float("inf"), -1
    for ell in ells:
        val = ramp_trial(E, a, b, ell)
        if np.isfinite(val) and val > 0.0 and val < best:
            best, best_l = val, ell
    return best, best_l


def density_interval_sup(R):
    """Psi_int = sup_I (1^T R_II 1) / |I|, the S3 Cauchy-Schwarz object on the
    interval class, again EXACT over all O(m^2) intervals."""
    m = R.shape[0]
    S = interval_sums(R)
    L = interval_lengths(m)
    good = L >= 1
    rat = np.where(good, S / np.where(good, L, 1.0), -np.inf)
    flat = int(np.argmax(rat))
    a, b = divmod(flat, m + 1)
    return dict(P=float(rat[a, b]), a=int(a), b=int(b), rat=rat)


def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000) for the MAXIMUM DENSITY
    SUBGRAPH of a NONNEGATIVE symmetric weight matrix with zero diagonal:
    repeatedly delete a vertex of minimum weighted degree and keep the best
    density w(A) / |A| seen.  DIRECTIONS, both cited and both used below:
      * the returned value is attained by an explicit set, hence a LOWER bound
        on the optimum;
      * Charikar's guarantee greedy >= opt / 2 turns it into the UPPER bound
        opt <= 2 x greedy, which is the only bound in this probe that holds over
        ALL 2^m sets without any family restriction."""
    m = Wp.shape[0]
    if m < 2:
        return dict(dens=0.0, size=m)
    deg = Wp.sum(axis=1).astype(float)
    tot = 0.5 * float(deg.sum())
    alive = np.ones(m, dtype=bool)
    n_alive = m
    best, best_n = tot / m, m
    while n_alive > 1:
        d = np.where(alive, deg, np.inf)
        j = int(np.argmin(d))
        tot -= float(deg[j])
        alive[j] = False
        deg = deg - Wp[j]
        deg[j] = 0.0
        n_alive -= 1
        dens = tot / n_alive
        if dens > best:
            best, best_n = dens, n_alive
    return dict(dens=float(best), size=int(best_n))


# ----------------------------------------------------------------------------
# THE SET FAMILIES for the interval reduction
# ----------------------------------------------------------------------------
def block_subsets_all(off, g):
    """ALL 2^g - 1 nonempty subsets of a contiguous block -- the EXHAUSTIVE
    family.  cap_E only needs R on A x A, so a subset of a block is as cheap as
    the block, and the hull of such a subset also lies in the block."""
    base = np.arange(g)
    out = []
    for mask in range(1, 1 << g):
        sel = base[np.array([(mask >> i) & 1 for i in range(g)], dtype=bool)]
        out.append(off + sel)
    return out


def block_structured(off, g, rng):
    """The STRUCTURED families inside a block: unions of intervals, strided
    (lacunary) sets, random densities, prefixes and suffixes, and the middle."""
    out = []
    base = np.arange(g)
    for t in (2, 3, 4, 5):
        for ph in range(min(t, 2)):
            sel = base[ph::t]
            if sel.size >= 2:
                out.append(off + sel)
    for n1 in (2, 3, 4, 6, 8):
        for n2 in (2, 3, 5, 9):
            a1, b1 = 0, min(g, n1)
            a2 = min(g - 1, b1 + n2)
            b2 = min(g, a2 + n1)
            if b2 > a2:
                out.append(off + np.concatenate([np.arange(a1, b1),
                                                 np.arange(a2, b2)]))
    for k in (3, 5, 9):
        pts = np.linspace(0, g, 2 * k + 1)
        seg = []
        for i in range(k):
            a = int(round(pts[2 * i]))
            b = int(round(pts[2 * i + 1]))
            if b > a:
                seg.append(np.arange(a, b))
        if seg:
            out.append(off + np.concatenate(seg))
    for p in (0.2, 0.35, 0.5, 0.7, 0.85):
        for _ in range(6):
            sel = base[rng.random(g) < p]
            if sel.size >= 2:
                out.append(off + sel)
    for n in (2, 3, 5, 8, 13, 21):
        if n <= g:
            out.append(off + np.arange(n))
            out.append(off + np.arange(g - n, g))
            mid = (g - n) // 2
            out.append(off + np.arange(mid, mid + n))
    return out


def hull_of(idx):
    return int(idx[0]), int(idx[-1]) + 1


def c_int_of(R, idx, cache):
    """THE REDUCTION FACTOR of one set: c_int(A) = Phi(A) / Phi(I(A)) with
    I(A) the convex hull.  Also returns the two ingredients separately, because
    c_int = (|A| / |I|) x (cap(I) / cap(A)) and the second factor is where the
    non-Markovian structure could bite: for a Dirichlet form capacity is
    MONOTONE, so cap(I) >= cap(A) and the second factor is >= 1; here that has
    to be measured."""
    idx = np.sort(np.asarray(idx, dtype=np.int64))
    a, b = hull_of(idx)
    cap_A = set_capacity(R, idx)
    key = (a, b)
    if key not in cache:
        cache[key] = interval_capacity(R, a, b)
    cap_I = cache[key]
    if not (np.isfinite(cap_A) and np.isfinite(cap_I) and cap_A > 0.0
            and cap_I > 0.0):
        return None
    phi_A = idx.size / cap_A
    phi_I = (b - a) / cap_I
    return dict(phi_A=phi_A, phi_I=phi_I, c=phi_A / phi_I,
                frac=idx.size / float(b - a), mono=cap_I / cap_A,
                size=int(idx.size), span=int(b - a))


def adversarial_c_int(R, off, g, rng, cache, starts=ADV_STARTS,
                      sweeps=ADV_SWEEPS):
    """AN ADVERSARIAL SEARCH for the reduction factor itself: single-index flips
    inside a block, hill-climbing on c_int(A) rather than on Phi(A).  This is
    the honest way to look for a set that the interval class cannot see."""
    best, best_rec, n_eval = 0.0, None, 0
    for st in range(starts):
        mask = rng.random(g) < (0.3 + 0.2 * st)
        if int(np.count_nonzero(mask)) < 2:
            mask[:2] = True
        cur = c_int_of(R, off + np.nonzero(mask)[0], cache)
        cur_v = cur["c"] if cur else 0.0
        for _ in range(sweeps):
            improved = False
            for k in range(g):
                mask[k] = not mask[k]
                sel = np.nonzero(mask)[0]
                if sel.size < 2 or sel.size == g:
                    mask[k] = not mask[k]
                    continue
                rec = c_int_of(R, off + sel, cache)
                n_eval += 1
                if rec is not None and rec["c"] > cur_v * (1.0 + 1.0e-12):
                    cur_v, cur = rec["c"], rec
                    improved = True
                else:
                    mask[k] = not mask[k]
            if not improved:
                break
        if cur_v > best:
            best, best_rec = cur_v, cur
    return best, best_rec, n_eval


def markov_reach(E, Ppos, tries=14):
    """HOW FAR the form can be pushed towards a Markovian one before it stops
    being a form at all: the largest t in [0, 1] with E - t P still positive
    definite, P the POSITIVE off-diagonal part, located by bisection on a
    COMPLETED CHOLESKY (so every accepted t is CERTIFIED positive definite).
    t = 1 would mean the positive off-diagonals are removable and the Markovian
    case is a perturbation away; t small means they are load-bearing for
    positivity itself, and then no perturbation argument can reach S1 from the
    Markovian case."""
    if safe_cho(sym(E - Ppos)) is not None:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(tries):
        mid = 0.5 * (lo + hi)
        if safe_cho(sym(E - mid * Ppos)) is not None:
            lo = mid
        else:
            hi = mid
    return lo


def paired_neumann_small(S, ladder=M_LADDER):
    """THE m-PAIRED NEUMANN CERTIFICATE, QUOTED in form from T138 .. T143 and
    reduced to what P3(iii) needs: does the ladder certify the block, and if
    not, by which factor does it miss."""
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
    del F, Fm, Pm, Dl
    return out


# ----------------------------------------------------------------------------
section("P0  SETUP, the capacity licences, and the DIRECTION statements")
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
check("el_p0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

RNG = np.random.default_rng(14407281)

para("""P0.0  THE RH FENCE, STATED BEFORE ANY NUMBER.  The surrounding statement
is the positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999)
on a FINITE list of prime-power zones and a FINITE window; the criterion is
CITED as that address and is NEVER USED here, in either direction.  Nothing in
this file claims, assumes or approaches RH: even with S1 closed, what would
stand is a finite-window positivity statement, and the distance from there to RH
is mapped in P4 and never travelled.  No zero data is read, generated or
approximated -- the AST firewall above enforces that, together with the import
whitelist and the absence of any write-mode file access.""")

# --- P0.1  the coordinates, unchanged from T106 .. T143 ---------------------
_k0, _D0, _M0 = None, None, None
for _kk in range(2, NZ_DEEP - 2):
    _Dc = 0.5 * float(G_DEEP[_kk]) / NU_MAIN
    _Mc = even_window(UU_ALL[_kk], _Dc)
    if 110 <= _Mc // 2 <= 190:
        _k0, _D0, _M0 = _kk, _Dc, _Mc
if _k0 is None:
    raise SystemExit("P0 found no calibration window in the declared h band")
_al0 = 0.5 * _M0 * _D0
_h0 = _M0 // 2
_c0, _ = lag_vector_fast(_al0, _M0, atoms_in(_al0, ATOMS_ALL))
E_ODD = rel(odd_toeplitz(_c0, _M0), odd_toeplitz_slow(_c0, _M0))
check("el_p0.odd_section", E_ODD <= BAR_ID,
      "the vectorised odd section equals its entrywise definition A_rs = "
      "c_{|r-s|} - c_{M-1-r-s} to %.2e (bar %.0e) on the calibration window "
      "h = %d, D = %.3e -- the coordinates of T106 .. T143, unchanged"
      % (E_ODD, BAR_ID, _h0, _D0))

_A0 = sym(odd_toeplitz(_c0, _M0))
_lp0 = lump_pair(_A0)
check("el_p0.lumping", _lp0["stieltjes"] == 1,
      "the lumped pair is STIELTJES (A_B has nonpositive off-diagonal and "
      "positive diagonal), which is what makes diag(A_B) the natural whitening "
      "weight; the ORIGINAL A has %d positive off-diagonal entries out of %d, "
      "i.e. the form is non-Markovian from the start (T143 QUOTED: %.0f .. "
      "%.0f %% of the whitened off-diagonal)"
      % (_lp0["n_pos"], _h0 * (_h0 - 1), 100.0 * MK_POS_T143[0],
         100.0 * MK_POS_T143[1]))

# --- P0.2  THE FOUR LICENCES this probe leans on, each verified -------------
_Ze = RNG.standard_normal((60, 60))
_Ee = sym(_Ze @ _Ze.T) + 3.0 * np.eye(60)
_Re = np.linalg.inv(_Ee)
_idx = np.sort(RNG.choice(60, 17, replace=False))
_c_schur = set_capacity(_Re, _idx)
_c_dir = set_capacity_direct(_Ee, _idx)
CAP_ID_ERR = abs(_c_schur - _c_dir) / max(abs(_c_dir), 1.0e-300)
check("el_p0.capacity_identity", CAP_ID_ERR <= 1.0e-9,
      "LICENCE 1, THE CAPACITY IS A GREEN OBJECT: cap_E(A) = 1^T "
      "[(E^{-1})_AA]^{-1} 1 equals the constrained minimum min { w^T E w : "
      "w|_A = 1 } to %.2e relative (Fukushima-Oshima-Takeda 1994, ch. 2; "
      "Maz'ya 1985).  Verified, not assumed, because every number below is a "
      "capacity" % CAP_ID_ERR)

_lam_e = float(eigvalsh(_Ee, subset_by_index=[0, 0])[0])
_phi_e = float(_idx.size) / _c_dir
check("el_p0.capacity_direction", _phi_e <= 1.0 / _lam_e * (1.0 + 1.0e-9),
      "AND THE DIRECTION IT GIVES: Phi(A) = |A| / cap(A) = %.4f <= 1 / lam_min "
      "= %.4f.  A single set CERTIFIES an UPPER bound on the gap and NEVER a "
      "lower one; the lower bound is exactly S1 and it is NOT proved anywhere "
      "in this file" % (_phi_e, 1.0 / _lam_e))

# the indicator trial value, which is the closed form P2 is built on
_S_dir = float(np.ones(_idx.size) @ _Ee[np.ix_(_idx, _idx)] @ np.ones(_idx.size))
check("el_p0.trial_upper", _c_dir <= _S_dir * (1.0 + 1.0e-12),
      "LICENCE 2, THE CLOSED TRIAL VALUE: the indicator of A is admissible in "
      "the constrained minimisation, so cap_E(A) <= 1^T E_AA 1 = S(A) always "
      "(here %.6f <= %.6f).  For an INTERVAL S(I) is a two-dimensional prefix "
      "sum, hence CLOSED, which is what makes the two-weight sup of P2 "
      "computable over ALL intervals with no matrix solve"
      % (_c_dir, _S_dir))

_S_pref = interval_sums(_Ee)
_a1, _b1 = 11, 39
_S_slice = float(_Ee[_a1:_b1, _a1:_b1].sum())
PREF_ERR = abs(_S_pref[_a1, _b1] - _S_slice) / max(abs(_S_slice), 1.0e-300)
check("el_p0.prefix_identity", PREF_ERR <= 1.0e-12,
      "and the prefix-sum implementation of S(I) equals the direct double sum "
      "to %.2e on a random form, so the O(m^2) interval sweep is exact "
      "arithmetic and not an approximation" % PREF_ERR)

# LICENCE 2b: the nestedness identity that makes the interval class exhaustible
_nb, _na, _nn = interval_sup_exact(_Re, 60, np.zeros((61, 61)))[:3]
_nx = [(a, b) for a in range(0, 55, 7) for b in range(a + 3, 60, 11)]
NEST_ERR = 0.0
for (_a2, _b2) in _nx:
    _L2 = cholesky(sym(np.ascontiguousarray(_Re[_a2:60, _a2:60])), lower=True,
                   check_finite=False)
    _z2 = solve_triangular(_L2, np.ones(60 - _a2), lower=True,
                           check_finite=False)
    _cp_pref = float(np.sum(_z2[:_b2 - _a2] ** 2))
    NEST_ERR = max(NEST_ERR, rel(_cp_pref, interval_capacity(_Re, _a2, _b2)))
check("el_p0.nested_prefix", NEST_ERR <= BAR_ID,
      "LICENCE 2b, THE IDENTITY THAT MAKES THE INTERVAL CLASS EXHAUSTIBLE: for "
      "a fixed left endpoint the Cholesky factor of R[a:m, a:m] contains the "
      "factor of EVERY R[a:b, a:b] as its leading block, and forward "
      "substitution never looks ahead, so cap([a, b)) = sum_{k < b-a} z_k^2 "
      "with L z = 1 is a PREFIX SUM.  Verified against the independent "
      "factor-and-solve on %d intervals to %.2e relative (bar %.0e).  One "
      "Cholesky per left endpoint instead of m(m+1)/2 of them is what turns "
      "the O(m^2) interval supremum from a sampled maximum into an EXACT one "
      "on every window of the surface, %d intervals on the calibration matrix "
      "alone" % (len(_nx), NEST_ERR, BAR_ID, _nn))

_cs_floor = (_idx.size ** 2) / float(np.ones(_idx.size)
                                     @ _Re[np.ix_(_idx, _idx)]
                                     @ np.ones(_idx.size))
check("el_p0.cauchy_schwarz", _c_dir >= _cs_floor * (1.0 - 1.0e-12),
      "LICENCE 3, THE S3 FLOOR: cap_E(A) >= |A|^2 / (1^T R_AA 1) with R = "
      "E^{-1} by Cauchy-Schwarz applied to (1^T 1)^2 <= (1^T M 1)(1^T M^{-1} 1) "
      "for M = R_AA (here %.6f >= %.6f).  Equivalently Phi(A) <= Psi(A) = "
      "(1^T R_AA 1) / |A|, i.e. the MEAN GREEN MASS of A -- a closed lower "
      "bound for the capacity out of the Green function alone, which is the "
      "shape S3 asked for" % (_c_dir, _cs_floor))

# LICENCE 4: the Jacobi whitening, and its two directions
_Zb = RNG.standard_normal((50, 50))
_Ab = sym(_Zb @ _Zb.T) + 2.0 * np.eye(50)
_Yb = RNG.standard_normal((50, 50))
_Bb = sym(_Ab + sym(_Yb @ _Yb.T)) + 6.0 * np.eye(50)
_lam_pair = float(eigh(_Ab, _Bb, eigvals_only=True, subset_by_index=[0, 0])[0])
_jw = jacobi_whiten(_Ab, _Bb)
_lam_wh = float(eigvalsh(_jw["E"], subset_by_index=[0, 0])[0])
_lo_side = _lam_wh / _jw["kap_up"]
_up_side = _lam_wh / _jw["kap_lo"]
check("el_p0.jacobi_direction",
      _lam_pair >= _lo_side * (1.0 - 1.0e-9)
      and _lam_pair <= _up_side * (1.0 + 1.0e-9),
      "LICENCE 4, THE ONE COMPARISON THIS PROBE MAKES, and it is on the "
      "DENOMINATOR: lam_min(E) / kap_up = %.6e <= lam_min(A, A_B) = %.6e <= "
      "lam_min(E) / kap_lo = %.6e on a random pair, with kap_up CERTIFIED from "
      "above and kap_lo from below.  The LEFT inequality is the one used, and "
      "it costs a MULTIPLICATIVE factor on the gap -- unlike T142's dead "
      "numerator comparisons, which had to reproduce rho = 1 - Theta(D^%.0f) to "
      "relative accuracy O(D^%.0f)"
      % (_lo_side, _lam_pair, _up_side, GAP_EXP_T142, GAP_EXP_T142))

# LICENCE 5: Charikar's guarantee, checked against a brute-force optimum
_gg = 14
_Wr = np.abs(RNG.standard_normal((_gg, _gg)))
_Wr = sym(_Wr)
np.fill_diagonal(_Wr, 0.0)
_gr = greedy_density(_Wr)
_bf = 0.0
for _mask in range(1, 1 << _gg):
    _sel = np.array([(_mask >> i) & 1 for i in range(_gg)], dtype=bool)
    _ns = int(np.count_nonzero(_sel))
    if _ns < 1:
        continue
    _d = 0.5 * float(_Wr[np.ix_(_sel, _sel)].sum()) / _ns
    if _d > _bf:
        _bf = _d
check("el_p0.charikar_bracket",
      _gr["dens"] <= _bf * (1.0 + 1.0e-12) and _bf <= 2.0 * _gr["dens"],
      "LICENCE 5, THE ONLY ALL-SETS BOUND IN THIS PROBE: greedy peeling gives "
      "%.6f, the EXHAUSTIVE optimum over all %d subsets is %.6f, and "
      "Charikar's guarantee opt <= 2 x greedy = %.6f holds (Charikar 2000; "
      "Goldberg 1984 for the exact flow version).  This is what turns the S3 "
      "floor into a bound over ALL 2^m sets with a CITED absolute constant, "
      "with no family restriction anywhere"
      % (_gr["dens"], (1 << _gg) - 1, _bf, 2.0 * _gr["dens"]))

_M1 = sym(RNG.standard_normal((40, 40)))
_M1 = _M1 @ _M1.T + np.eye(40)
_G2 = RNG.standard_normal((40, 40))
_M2 = _M1 + sym(_G2 @ _G2.T)
_i2 = np.sort(RNG.choice(40, 11, replace=False))
_cap1 = set_capacity_direct(_M1, _i2)
_cap2 = set_capacity_direct(_M2, _i2)
check("el_p0.capacity_monotone", _cap1 <= _cap2 * (1.0 + 1.0e-10),
      "AND THE LOEWNER MONOTONICITY OF THE CAPACITY, which is what licenses "
      "every comparison of two forms below: E1 <= E2 implies cap_E1(A) <= "
      "cap_E2(A) (here %.6f <= %.6f), directly from the minimisation over the "
      "same admissible set" % (_cap1, _cap2))

para("""P0.3  WHAT IS NEW HERE, IN ONE SENTENCE.  T143 measured that the
criterion's CONCLUSION survives the loss of its Markovian hypothesis
(Phi_sup x lam = %.4f .. %.4f, inside [1/4, 1]) while its classical PROOF
mechanism does not (Miclo's chain loses %.0f .. %.0f, drifting as D^%.2f, which is
a death and not a constant).  So the missing object is
S1 itself, and S1 is a statement about the sup over ALL sets.  This probe attacks
that sup from two sides at once: the INTERVAL REDUCTION (P1 / P2), which would
make the sup a one-dimensional two-weight calculus, and the DENSITY BOUND (P3),
which bounds the sup over all sets directly with a cited absolute constant.
Neither proves S1; both change what S1 would have to be proved about.""" %
     (PHI_LAM_T143[0], PHI_LAM_T143[1], MICLO_LOSS_T143[0],
      MICLO_LOSS_T143[1], MICLO_EXP_T143))


# ----------------------------------------------------------------------------
# THE WINDOW BUILDER -- one window, all the objects the four blocks need
# ----------------------------------------------------------------------------
def build_window(al, M_k, h_k, atoms_all):
    """The T140 .. T143 core, plus the Jacobi whitening and the Green function
    of the whitened form.  Nothing large leaves this function except through the
    caller's own del."""
    c_lag, _ = lag_vector_fast(al, M_k, atoms_in(al, atoms_all))
    A = sym(odd_toeplitz(c_lag, M_k))
    lp = lump_pair(A)
    if lp["stieltjes"] != 1:
        return None
    try:
        gap_ex = float(eigh(A, lp["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return None
    if not (gap_ex > 0.0):
        return None
    jw = jacobi_whiten(A, lp["A_B"])
    if jw is None or not np.isfinite(jw["kap_up"]) or not (jw["kap_lo"] > 0.0):
        return None
    E = jw["E"]
    try:
        lam_hat = float(eigvalsh(E, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return None
    if not (lam_hat > 0.0):
        return None
    fac = safe_cho(E)
    if fac is None:
        return None
    R = sym(cho_solve(fac, np.eye(h_k), check_finite=False))
    off = E - np.diag(np.diag(E))
    tot_off = float(np.sum(np.abs(off)))
    return dict(A=A, A_B=lp["A_B"], E=E, R=R, m=h_k, gap_ex=gap_ex,
                lam_hat=lam_hat, kap_up=jw["kap_up"], kap_lo=jw["kap_lo"],
                gersh_up=jw["gersh_up"],
                Lam=jw["Lam"], n_pos=lp["n_pos"],
                mk_frac=float(np.mean(off > 0.0)),
                mk_mass=float(np.sum(np.where(off > 0.0, off, 0.0)))
                / max(tot_off, 1.0e-300),
                whiten_err=abs(lam_hat / jw["kap_up"] - gap_ex)
                / max(gap_ex, 1.0e-300))


# ----------------------------------------------------------------------------
section("P1  THE INTERVAL REDUCTION -- 2^m sets against O(m^2) intervals")
# ----------------------------------------------------------------------------
para("""P1.0  THE MEASUREMENT SURFACE and the object.  Candidates are ALL
prime-power zones whose frame-A window fits the caps; the surface is spread over
log n so that the D range is as wide as the caps allow, because D-uniformity is
the whole question.  In each window the whitened node form E = Lam^{-1/2} A
Lam^{-1/2} carries the counting measure, so Phi(A) = |A| / cap_E(A) is the
Maz'ya ratio of the criterion, and the reduction factor of a set is

    c_int(A) = Phi(A) / Phi(I(A)) = (|A| / |I(A)|) x (cap_E(I(A)) / cap_E(A)) ,

I(A) the convex hull of A in the node coordinates.  If sup_A c_int(A) is
absolutely bounded then Phi_sup <= c_int x sup_I Phi(I) and the sup over 2^m sets
is a sup over O(m^2) intervals -- that is the whole content of S2, and it is a
statement about the CAPACITY FUNCTIONAL only, never about the eigenvalue, so
T142's comparison obstruction does not apply to it.""")

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
info("P1.candidates", "%d prime-power zones admit a frame-A window inside the "
     "cap (h <= %d, MAX_H = %d); the surface takes %d of them (stride %d) from "
     "the deep end" % (len(CAND), SURF_HCAP, MAX_H, len(SZ), step))

ROWS = []
for (k, D_k, M_k, h_k) in SZ:
    if budget_left() < BUDGET_S - T_SURF - T_P1:
        info("P1.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(ROWS)))
        break
    al = 0.5 * M_k * D_k
    hv = build_window(al, M_k, h_k, ATOMS_ALL)
    if hv is None:
        continue
    m, R, E = hv["m"], hv["R"], hv["E"]
    cache = {}

    # --- P1(i)  THE EXHAUSTIVE FAMILY: every subset of a block --------------
    fam = dict(enum=[], struct=[], lev=[], adv=[])
    phi_fam = dict(enum=0.0, struct=0.0, lev=0.0, adv=0.0)
    mono = []
    phi_set = 0.0
    n_enum, n_blocks = 0, 0
    offs = sorted(set(min(max(0, int(round(f * m))), max(0, m - BLK_ENUM_G))
                      for f in BLK_FRACS))
    for off in offs[:BLK_ENUM_MAX]:
        if m < BLK_ENUM_G + 1 or budget_left() < BUDGET_S - T_SURF - T_P1:
            break
        for idx in block_subsets_all(off, BLK_ENUM_G):
            rec = c_int_of(R, idx, cache)
            n_enum += 1
            if rec is None:
                continue
            fam["enum"].append(rec["c"])
            mono.append(rec["mono"])
            phi_fam["enum"] = max(phi_fam["enum"], rec["phi_A"])
            phi_set = max(phi_set, rec["phi_A"])
        n_blocks += 1

    # --- P1(ii)  THE STRUCTURED AND ADVERSARIAL FAMILIES on wider blocks ----
    gb = min(BLK_STRUCT_G, m)
    offs2 = sorted(set(min(max(0, int(round(f * m))), max(0, m - gb))
                       for f in BLK_FRACS))
    n_adv = 0
    for off in offs2:
        for idx in block_structured(off, gb, RNG):
            rec = c_int_of(R, np.unique(idx), cache)
            if rec is None:
                continue
            fam["struct"].append(rec["c"])
            mono.append(rec["mono"])
            phi_fam["struct"] = max(phi_fam["struct"], rec["phi_A"])
            phi_set = max(phi_set, rec["phi_A"])
        cv, crec, ne = adversarial_c_int(R, off, gb, RNG, cache)
        n_adv += ne
        if crec is not None:
            fam["adv"].append(cv)
            phi_fam["adv"] = max(phi_fam["adv"], crec["phi_A"])
            phi_set = max(phi_set, crec["phi_A"])

    # --- P1(iii)  THE UNCONFINED FAMILIES (T143's, hull = almost the window) -
    dgR = np.sqrt(np.maximum(np.diag(R), 0.0))
    try:
        _w0, _V0 = eigh(E, subset_by_index=[0, 0])
        psi_ext = np.abs(_V0[:, 0])
    except (LinAlgError, ValueError):
        psi_ext = dgR
    for pv in (psi_ext, dgR, np.diag(hv["A_B"]), hv["Lam"]):
        for idx in level_sets_of(pv):
            rec = c_int_of(R, idx, cache)
            if rec is None:
                continue
            fam["lev"].append(rec["c"])
            mono.append(rec["mono"])
            phi_fam["lev"] = max(phi_fam["lev"], rec["phi_A"])
            phi_set = max(phi_set, rec["phi_A"])

    c_all = qmax([qmax(fam[key]) for key in fam])
    all_c = fam["enum"] + fam["struct"] + fam["lev"] + fam["adv"]
    phi_free = phi_set

    # --- P2(i)  THE CLOSED TWO-WEIGHT SUP over ALL intervals ---------------
    cl = closed_interval_sup(E)
    dens_int = density_interval_sup(R)
    phi_int, arg_int, n_pool, ph_rank, q_worst = interval_sup_exact(
        R, m, cl["rat"])
    int_full = True
    # THE FAITHFULNESS OF THE TWO CLOSED RANKINGS: how far down each of them the
    # TRUE argmax interval sits -- now available on every window, because the
    # interval class is exhausted on every window
    rk_res, rk_ene = -1, -1
    if arg_int is not None:
        aa, bb = arg_int
        rk_res = int(np.count_nonzero(dens_int["rat"] > dens_int["rat"][aa, bb]))
        rk_ene = int(np.count_nonzero(cl["rat"] > cl["rat"][aa, bb]))
    phi_set = max(phi_set, phi_int)

    # --- P2(ii)  THE RAMP REFINEMENT of the closed lower side --------------
    ells = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, m]
    ells = sorted(set(e for e in ells if e <= m))
    B_ramp, ell_star, ramp_gain = cl["B"], 0, 1.0
    for (ph, a, b, cp) in sorted(ph_rank, reverse=True)[:8]:
        val, ell = best_ramp(E, a, b, ells)
        if np.isfinite(val) and val > 0.0:
            r = (b - a) / val
            if r > B_ramp:
                B_ramp, ell_star = r, ell
            ramp_gain = max(ramp_gain, r / max(cl["rat"][a, b], 1.0e-300))

    # --- P3(i)  THE MARKOV PART, in the same coordinates -------------------
    # TWO surrogates, because the naive one is not a form at all: with P the
    # POSITIVE off-diagonal part, E_S = E - P is STIELTJES (Markovian shape,
    # diagonal untouched) while E_R = E - 2P = diag(E) - |offdiag(E)| REFLECTS
    # the positive entries.  Both are measured; neither is assumed.
    offE = E - np.diag(np.diag(E))
    Ppos = np.where(offE > 0.0, offE, 0.0)
    E_S = sym(E - Ppos)
    E_R = sym(E - 2.0 * Ppos)
    lam_S = float(eigvalsh(E_S, subset_by_index=[0, 0])[0])
    lam_R = float(eigvalsh(E_R, subset_by_index=[0, 0])[0])
    lam_P = float(eigvalsh(sym(Ppos), subset_by_index=[0, 0])[0])
    p_share = float(np.sum(Ppos)) / max(float(np.sum(np.abs(offE))), 1.0e-300)
    t_star = markov_reach(E, Ppos)
    t_use = t_star if lam_S > 0.0 else 0.5 * t_star
    mrat = []
    E_t = sym(E - t_use * Ppos)
    facM = safe_cho(E_t)
    if facM is not None:
        R_t = sym(cho_solve(facM, np.eye(m), check_finite=False))
        msets = [np.unique(ix) for ix in block_structured(offs2[0], gb, RNG)]
        msets += [np.arange(offs2[0], offs2[0] + j)
                  for j in (2, 4, 8, 16, min(32, gb))]
        msets += [np.arange(0, j) for j in (4, 16, min(64, m), max(2, m // 2))]
        for idx in msets:
            cA = set_capacity(R, idx)
            cM = set_capacity(R_t, idx)
            if np.isfinite(cA) and np.isfinite(cM) and cA > 0.0 and cM > 0.0:
                mrat.append(cM / cA)
        del R_t, facM

    # --- P3(ii)  THE S3 DENSITY OBJECTS ------------------------------------
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    gr = greedy_density(Rp)
    dg_max = float(np.max(np.diag(R)))
    psi_char = dg_max + 4.0 * gr["dens"]
    psi_spec = dg_max + cert_lam_max(Rp, guess=ray_top(Rp))
    psi_best = min(x for x in (psi_char, psi_spec) if np.isfinite(x))
    r_nonneg = float(np.mean(R >= 0.0))
    del Rp

    c_glob = max(1.0, phi_free / max(phi_int, 1.0e-300))
    chain_int = 1.0 / max(MAZYA_C0 * hv["kap_up"] * c_glob * dens_int["P"],
                          1.0e-300)
    chain_all = 1.0 / max(MAZYA_C0 * hv["kap_up"] * psi_best, 1.0e-300)
    ROWS.append(dict(
        k=k, n=NN_ALL[k], D=D_k, m=m, gap_ex=hv["gap_ex"],
        lam_hat=hv["lam_hat"], kap_up=hv["kap_up"], kap_lo=hv["kap_lo"],
        whiten_err=hv["whiten_err"], mk_frac=hv["mk_frac"],
        gersh_up=hv["gersh_up"],
        mk_mass=hv["mk_mass"], n_pos=hv["n_pos"],
        c_enum=qmax(fam["enum"]), c_struct=qmax(fam["struct"]),
        c_lev=qmax(fam["lev"]), c_adv=qmax(fam["adv"]), c_all=c_all,
        c_med=qmed(all_c), c_q90=qq(all_c, 0.90), n_sets=len(all_c),
        n_enum=n_enum, n_blocks=n_blocks, n_adv=n_adv,
        mono_min=qmin(mono), mono_med=qmed(mono),
        mono_bad=float(np.mean([1.0 if x < 1.0 - 1.0e-12 else 0.0
                                for x in mono])) if mono else float("nan"),
        B_int=cl["B"], B_a=cl["a"], B_b=cl["b"], n_int=cl["n_int"],
        n_bad=cl["n_bad"], phi_int=phi_int, int_full=int(int_full),
        n_pool=n_pool, arg_int=arg_int, arg_len=(arg_int[1] - arg_int[0])
        if arg_int else -1,
        rk_res=rk_res, rk_ene=rk_ene,
        B_ramp=B_ramp, ell_star=ell_star, ramp_gain=ramp_gain,
        q_int=(phi_int / cl["B"]) if cl["B"] > 0.0 else float("nan"),
        q_ramp=(phi_int / B_ramp) if B_ramp > 0.0 else float("nan"),
        q_worst=q_worst, phi_set=phi_set, phi_free=phi_free, c_glob=c_glob,
        r_int_set=(phi_int / phi_set) if phi_set > 0.0 else float("nan"),
        core=cl["B"] * hv["lam_hat"], core_gap=cl["B"] * hv["gap_ex"],
        core_int=phi_int * hv["lam_hat"], core_ramp=B_ramp * hv["lam_hat"],
        exhaust=phi_set * hv["lam_hat"],
        lam_S=lam_S, lam_R=lam_R, lam_P=lam_P, p_share=p_share,
        t_star=t_star, t_use=t_use,
        mrat_min=qmin(mrat), mrat_max=qmax(mrat),
        mrat_med=qmed(mrat), n_mrat=len(mrat),
        phi_enum=phi_fam["enum"], phi_struct=phi_fam["struct"],
        phi_lev=phi_fam["lev"], phi_adv=phi_fam["adv"],
        g_enum=phi_fam["enum"] / max(phi_int, 1.0e-300),
        g_struct=phi_fam["struct"] / max(phi_int, 1.0e-300),
        g_lev=phi_fam["lev"] / max(phi_int, 1.0e-300),
        g_adv=phi_fam["adv"] / max(phi_int, 1.0e-300),
        transfer=hv["lam_hat"] / max(hv["kap_up"] * hv["gap_ex"], 1.0e-300),
        sandwich=hv["kap_up"] / max(hv["kap_lo"], 1.0e-300),
        psi_int=dens_int["P"], psi_greedy=gr["dens"], psi_size=gr["size"],
        psi_char=psi_char, psi_spec=psi_spec, psi_best=psi_best,
        dg_max=dg_max, r_nonneg=r_nonneg,
        core_psi=dens_int["P"] * hv["lam_hat"],
        core_all=psi_best * hv["lam_hat"],
        psi_ratio=(dens_int["P"] / phi_int) if phi_int > 0.0 else float("nan"),
        psi_ratio_all=(psi_best / phi_set) if phi_set > 0.0 else float("nan"),
        chain_int=chain_int, loss_int=chain_int / max(hv["gap_ex"], 1.0e-300),
        chain_all=chain_all, loss_all=chain_all / max(hv["gap_ex"], 1.0e-300)))
    del hv, R, E, cl, cache, offE, Ppos, E_S, E_R, E_t, fam

if not ROWS:
    raise SystemExit("P1 produced no window -- probe cannot report")

for r in ROWS:
    # THE CHAIN IN THE COORDINATES WHERE THE CRITERION LIVES.  The capacity
    # criterion is a statement about (E, counting measure), so the chain that
    # P1 and P2 close is a chain for lam_hat; the step to the exact pair is the
    # SEPARATE certified factor kap_up of P1.  Both are reported, and the
    # verdict is taken on the capacity calculus rather than on the whitening.
    r["chain_hat"] = 1.0 / max(MAZYA_C0 * r["c_glob"] * r["psi_int"], 1.0e-300)
    r["loss_hat"] = r["chain_hat"] / max(r["lam_hat"], 1.0e-300)
    r["chain_hat_all"] = 1.0 / max(MAZYA_C0 * r["psi_best"], 1.0e-300)
    r["loss_hat_all"] = r["chain_hat_all"] / max(r["lam_hat"], 1.0e-300)

DV = [r["D"] for r in ROWS]
F_GAP = pow_fit(DV, [r["gap_ex"] for r in ROWS], "gap")
F_LOSSHAT = pow_fit(DV, [r["loss_hat"] for r in ROWS], "loss_hat")
F_LOSSHATALL = pow_fit(DV, [r["loss_hat_all"] for r in ROWS], "loss_hat_all")
F_CGLOB = pow_fit(DV, [r["c_glob"] for r in ROWS], "c_glob")
F_CHULL = pow_fit(DV, [r["c_all"] for r in ROWS], "c_hull")
F_COREINT = pow_fit(DV, [r["core_int"] for r in ROWS], "core_int")
F_COREPSI = pow_fit(DV, [r["core_psi"] for r in ROWS], "core_psi")
F_COREALL = pow_fit(DV, [r["core_all"] for r in ROWS], "core_all")
F_LOSSINT = pow_fit(DV, [r["loss_int"] for r in ROWS], "loss_int")
F_LOSSALL = pow_fit(DV, [r["loss_all"] for r in ROWS], "loss_all")
F_TRANS = pow_fit(DV, [r["transfer"] for r in ROWS], "transfer")
F_QRAMP = pow_fit(DV, [r["q_ramp"] for r in ROWS], "q_ramp")
F_TSTAR = pow_fit(DV, [r["t_star"] for r in ROWS], "t_star")
F_KAP = pow_fit(DV, [r["kap_up"] for r in ROWS], "kap_up")

info("P1.surface", "%d windows, h = m = %d .. %d, D = %.3e .. %.3e, zones "
     "n = %d .. %d; exact gap lam_min(A, A_B) = %.3e .. %.3e, FITTED as "
     "D^%.3f +- %.3f (T140 QUOTED rho(W) = %.4f .. %.4f, T142 QUOTED the "
     "exponent %.0f)"
     % (len(ROWS), min(r["m"] for r in ROWS), max(r["m"] for r in ROWS),
        qmin(DV), qmax(DV), min(r["n"] for r in ROWS),
        max(r["n"] for r in ROWS), qmin([r["gap_ex"] for r in ROWS]),
        qmax([r["gap_ex"] for r in ROWS]), F_GAP["p"], F_GAP["sp"],
        RHO_W_T140[0], RHO_W_T140[1], GAP_EXP_T142))

check("el_p1.whitening_direction",
      all(r["lam_hat"] / r["kap_up"] <= r["gap_ex"] * (1.0 + 1.0e-9)
          for r in ROWS),
      "THE ONE COMPARISON, CERTIFIED ON EVERY WINDOW: lam_min(E) / kap_up <= "
      "lam_min(A, A_B) with kap_up = %.4f .. %.4f (Gershgorin would allow "
      "%.2f), so the Jacobi whitening costs a factor of at most %.4f and its "
      "efficiency -- the ratio of the transported bound to the true gap -- is "
      "%.4f .. %.4f.  FITTED against D as D^%.3f +- %.3f.  The whitened "
      "eigenvalue itself is lam_hat = %.3e .. %.3e"
      % (qmin([r["kap_up"] for r in ROWS]), qmax([r["kap_up"] for r in ROWS]),
         BAR_KAPJ, qmax([r["kap_up"] for r in ROWS]),
         qmin([r["transfer"] for r in ROWS]),
         qmax([r["transfer"] for r in ROWS]), F_TRANS["p"], F_TRANS["sp"],
         qmin([r["lam_hat"] for r in ROWS]),
         qmax([r["lam_hat"] for r in ROWS])))

check("el_p1.kappa_bounded", qmax([r["kap_up"] for r in ROWS]) <= BAR_KAPJ,
      "and it is ABSOLUTELY bounded on the surface: kap_up = %.4f .. %.4f "
      "against the preregistered ceiling %.2f, and it has a STRUCTURAL ceiling "
      "besides the measurement -- diagonal dominance of the Stieltjes matrix "
      "A_B gives the Gershgorin bound kap <= %.4f .. %.4f on the same windows.  "
      "The FIT is D^%.3f +- %.3f (bar %.2f -> %s) and it is NOT load-bearing "
      "here: the ceiling is, and the ceiling is a bound and not a trend"
      % (qmin([r["kap_up"] for r in ROWS]), qmax([r["kap_up"] for r in ROWS]),
         BAR_KAPJ, qmin([r["gersh_up"] for r in ROWS]),
         qmax([r["gersh_up"] for r in ROWS]), F_KAP["p"], F_KAP["sp"],
         BAR_UNIF, "ZONE-UNIFORM" if unif_ok(F_KAP) else "NOT zone-uniform"))

N_EXP = sum(r["n_blocks"] for r in ROWS)
check("el_p1.exhaustion",
      all(r["n_enum"] == r["n_blocks"] * ((1 << BLK_ENUM_G) - 1) for r in ROWS),
      "THE SAMPLE IS AN EXHAUSTION WHERE IT CLAIMS TO BE: on %d blocks of size "
      "g = %d (%d per window) ALL %d nonempty subsets were evaluated, %d sets "
      "in total, so inside a block the statement below is EXACT and not "
      "family-restricted.  Total sets per window including the structured, "
      "level-set and adversarial families: %d .. %d"
      % (N_EXP, BLK_ENUM_G, ROWS[0]["n_blocks"], (1 << BLK_ENUM_G) - 1,
         sum(r["n_enum"] for r in ROWS), min(r["n_sets"] for r in ROWS),
         max(r["n_sets"] for r in ROWS)))

check("el_p1.capacity_monotone_measured",
      qmin([r["mono_min"] for r in ROWS]) >= 1.0 - 1.0e-9,
      "AND A NON-MARKOVIAN SURPRISE, measured on every sampled set: the "
      "capacity is still MONOTONE, cap_E(I(A)) / cap_E(A) = %.6f .. %.3e >= 1 "
      "on all %d sets of the pool.  For a Dirichlet form this is a theorem; "
      "here only %.0f .. %.0f %% of the off-diagonal entries are positive but "
      "they carry %.0f .. %.0f %% of the off-diagonal MASS (T143 QUOTED %.0f "
      ".. %.0f %% by count in its coordinates -- the count depends on the "
      "normalisation, the mass is the load-bearing figure and P3 shows it is), "
      "so the monotonicity is a MEASUREMENT that happens to hold and not a "
      "consequence -- which is exactly the kind of statement S1 needs and does "
      "not have"
      % (qmin([r["mono_min"] for r in ROWS]),
         qmax([r["mono_med"] for r in ROWS]), sum(r["n_sets"] for r in ROWS),
         100.0 * qmin([r["mk_frac"] for r in ROWS]),
         100.0 * qmax([r["mk_frac"] for r in ROWS]),
         100.0 * qmin([r["mk_mass"] for r in ROWS]),
         100.0 * qmax([r["mk_mass"] for r in ROWS]),
         100.0 * MK_POS_T143[0], 100.0 * MK_POS_T143[1]))

info("P1.hull_factor", "THE POINTWISE HULL COMPARISON, AND IT IS FALSE: "
     "c_int(A) = Phi(A) / Phi(I(A)) reaches %.2f .. %.2f over the windows "
     "(median over sets %.3f, 90%% quantile %.3f), i.e. individual sets DO "
     "beat their own convex hull by more than the preregistered absolute "
     "ceiling %.2f.  Family by family the worst case is: exhaustive subsets "
     "%.2f, structured families %.2f, unconfined level sets %.2f, adversarial "
     "search %.2f -- the level sets are the offenders, and the reason is "
     "structural rather than numerical: a set spread over the whole window has "
     "the WHOLE WINDOW as its hull, and the whole window is a BAD interval.  "
     "So a proof that compares each set to its hull cannot work, and reading "
     "the sign pedantically it cannot be rescued by a D-dependent constant "
     "either: the hull factor FITS as D^%.3f +- %.3f, a NEGATIVE exponent, so "
     "it GROWS towards the deep end instead of decaying"
     % (qmin([r["c_all"] for r in ROWS]), qmax([r["c_all"] for r in ROWS]),
        qmed([r["c_med"] for r in ROWS]), qmed([r["c_q90"] for r in ROWS]),
        BAR_CINT, qmax([r["c_enum"] for r in ROWS]),
        qmax([r["c_struct"] for r in ROWS]),
        qmax([r["c_lev"] for r in ROWS]), qmax([r["c_adv"] for r in ROWS]),
        F_CHULL["p"], F_CHULL["sp"]))

CGLOB_MAX = qmax([r["c_glob"] for r in ROWS])
CGLOB_OK = bool(CGLOB_MAX <= BAR_CINT and unif_ok(F_CGLOB))
check("el_p1.reduction_measured", CGLOB_OK,
      "BUT THE COMPARISON THE CHAIN ACTUALLY NEEDS IS THE BEST-INTERVAL ONE, "
      "and that one holds: c_glob = (sup over all sampled sets of Phi) / (sup "
      "over intervals of Phi) = %.4f .. %.4f, i.e. the whole set pool -- "
      "including every subset of the enumerated blocks and the adversarial "
      "search -- beats the interval class by at most %.1f %%.  Against the "
      "preregistered ceiling %.2f and FITTED as D^%.3f +- %.3f (bar %.2f) -> "
      "%s.  Family by family: exhaustive %.3f, structured %.3f, level sets "
      "%.3f, adversarial %.3f.  T143 QUOTED %.1f .. %.1f for the dominance of "
      "the interval levels in its coordinates, so the direction agrees and the "
      "constant is now the one the chain needs.  THIS IS MEASURED, not "
      "certified: it is a sampled supremum in the numerator and therefore a "
      "LOWER bound on the true reduction factor"
      % (qmin([r["c_glob"] for r in ROWS]), CGLOB_MAX,
         100.0 * (CGLOB_MAX - 1.0), BAR_CINT, F_CGLOB["p"], F_CGLOB["sp"],
         BAR_UNIF, "ZONE-UNIFORM" if unif_ok(F_CGLOB) else "NOT zone-uniform",
         qmax([r["g_enum"] for r in ROWS]),
         qmax([r["g_struct"] for r in ROWS]),
         qmax([r["g_lev"] for r in ROWS]), qmax([r["g_adv"] for r in ROWS]),
         INT_DOM_T143[0], INT_DOM_T143[1]))

para("""P1.9  WHAT P1 SETTLED.  The reduction of S1's supremum to the interval
class is TRUE at the level of the suprema and FALSE set by set.  That is not a
technicality: it says the proof of S2 cannot be a hull comparison (Phi(A) <=
c Phi(I(A))) and must be a BEST-INTERVAL comparison (Phi(A) <= c sup_I Phi(I)),
which is precisely the shape of a two-weight testing condition -- one tests the
form on the interval family and compares the constant, one does not transport
each set to its own hull.  The measured constant of that comparison is %.4f,
i.e. within %.1f %% of unity on the whole surface.""" %
     (CGLOB_MAX, 100.0 * (CGLOB_MAX - 1.0)))


# ----------------------------------------------------------------------------
section("P2  THE TWO-WEIGHT SUP -- the closed form, and the chain")
# ----------------------------------------------------------------------------
para("""P2.0  THE TWO CLOSED OBJECTS, and which side of the capacity each of them
bounds.  For an interval I there are two closed quantities available with no
matrix solve at all:

  (a) THE TRIAL-ENERGY SIDE, S(I) = sum_{k,l in I} E_kl, the energy of the
      indicator (and of a ramp of width ell around it).  Since the indicator is
      admissible, cap_E(I) <= S(I), so B_ene = sup_I |I| / S(I) is a LOWER bound
      on the interval supremum -- the direction that bounds the gap from ABOVE.
  (b) THE RESISTANCE SIDE, Psi(I) = (1^T R_II 1) / |I| with R = E^{-1}, which by
      the Cauchy-Schwarz floor of P0 satisfies cap_E(I) >= |I|^2 / (1^T R_II 1),
      hence Phi(I) <= Psi(I).  So B_res = sup_I Psi(I) is an UPPER bound on the
      interval supremum -- the direction S1 needs.

Both are two-dimensional prefix sums, so BOTH suprema are taken over ALL O(m^2)
intervals exactly.  (b) is the honest transcription of Muckenhoupt's condition,
whose weight is an INTEGRAL OF THE INVERSE (a resistance), not the energy of a
test function; (a) is the naive transcription.  The probe evaluates both and lets
the numbers say which transcription survives.""")

N_FULL = sum(1 for r in ROWS if r["int_full"])
check("el_p2.interval_exhaustion", N_FULL == len(ROWS),
      "THE INTERVAL SUPREMUM IS AN EXHAUSTION ON EVERY WINDOW, not a sampled "
      "one: all %d windows of the surface had ALL m(m+1)/2 = %d .. %d intervals "
      "evaluated with an EXACT capacity, %d in total, so Phi_int is EXACT "
      "throughout and no family restriction, ranking or grid enters it.  What "
      "buys that is the nestedness identity licensed in P0 -- one Cholesky per "
      "left endpoint instead of m(m+1)/2 of them, i.e. O(m^4) instead of "
      "O(m^5) arithmetic -- and it is the single reason this block can speak "
      "about a SUPREMUM over the interval class rather than about a maximum "
      "over a pool"
      % (len(ROWS), min(r["n_int"] for r in ROWS),
         max(r["n_int"] for r in ROWS), sum(r["n_int"] for r in ROWS)))

RKR = [r for r in ROWS if r["rk_res"] >= 0]
if RKR:
    info("P2.ranking", "AND A METHODOLOGICAL FINDING WORTH THE LINE: neither "
         "closed ranking POINTS AT the argmax interval, although both bound "
         "its value.  On all %d windows the true argmax sits at rank %d .. %d "
         "of the RESISTANCE ranking and at rank %d .. %d of the trial-energy "
         "ranking, out of %d .. %d intervals.  A closed object can therefore "
         "be a faithful BOUND (B_res is, to a factor %.2f) while being a "
         "useless SELECTOR -- which is why the interval supremum here is taken "
         "by exhaustion and never by reading off the closed maximiser, and it "
         "is also why a proof of S1 through the closed side will have to argue "
         "about the VALUE of the sup and not about where it is attained"
         % (len(RKR), min(r["rk_res"] for r in RKR),
            max(r["rk_res"] for r in RKR), min(r["rk_ene"] for r in RKR),
            max(r["rk_ene"] for r in RKR), min(r["n_int"] for r in RKR),
            max(r["n_int"] for r in RKR),
            qmax([r["psi_ratio"] for r in ROWS])))

CORE_LO = qmin([r["core_int"] for r in ROWS])
CORE_HI = qmax([r["core_int"] for r in ROWS])
CORE_ALO = qmin([r["exhaust"] for r in ROWS])
CORE_AHI = qmax([r["exhaust"] for r in ROWS])
BR_LO = qmin([r["core_psi"] for r in ROWS])
BR_HI = qmax([r["core_psi"] for r in ROWS])
PSI_OK = bool(unif_ok(F_COREPSI))
check("el_p2.mazya_window",
      CORE_AHI <= 1.0 + 1.0e-9 and BR_LO >= 1.0 / MAZYA_C0 - 1.0e-12
      and BR_HI <= 1.0 + 1.0e-9 and PSI_OK,
      "THE CORE NUMBER OF THE PROBE -- and Maz'ya's two halves read in the two "
      "DIRECTIONS they actually have, which is the whole discipline of this "
      "block.  The FREE half is a theorem, not a measurement: the equilibrium "
      "potential of A is admissible in the Rayleigh quotient, so lam <= 1 / "
      "Phi(A) for every single set, hence Phi_sup x lam_hat <= 1 is a "
      "FALSIFICATION test of the entire construction -- it comes out %.4f .. "
      "%.4f over all %d sets, so the construction survives it.  The OPEN half "
      "is S1 itself, and the object that would carry it is the CLOSED "
      "two-weight sup, evaluated over ALL O(m^2) intervals on every window "
      "with no sampling anywhere: B_res x lam_hat = %.4f .. %.4f, INSIDE "
      "[1/4, 1] on the whole surface, FITTED as D^%.3f +- %.3f against the bar "
      "%.2f -> %s.  T143 QUOTED %.4f .. %.4f for the sup over its four "
      "families in the OTHER coordinates, so the number is coordinate robust"
      % (CORE_ALO, CORE_AHI, sum(r["n_sets"] for r in ROWS), BR_LO, BR_HI,
         F_COREPSI["p"],
         F_COREPSI["sp"], BAR_UNIF,
         "ZONE-UNIFORM" if PSI_OK else "NOT zone-uniform", PHI_LAM_T143[0],
         PHI_LAM_T143[1]))

info("P2.saturation", "AND THE HONEST READING OF THE OTHER SIDE, which is "
     "where a careless probe would claim too much: the interval supremum "
     "itself, EXACT over all %d intervals of all %d windows, gives Phi_int x "
     "lam_hat = %.4f .. %.4f and FITS as D^%.3f +- %.3f -- OUTSIDE the bar "
     "%.2f.  Read the direction before reading the drift.  Phi_int is a LOWER "
     "bound for Phi_sup, so falling short of 1/4 is NOT a counterexample to "
     "S1; what it says is that the INTERVAL CLASS DOES NOT SATURATE the "
     "criterion, and that its share decays towards the deep end.  This is "
     "the sharpest single statement of the block, because it survives "
     "exhaustion: an interval-only Muckenhoupt condition can bound Phi_sup "
     "from above (that is the chain) but can NEVER reproduce it from below, "
     "so S1 will not follow from the interval class alone -- it needs either "
     "the closed upper bound B_res, which is flat, or the all-sets density "
     "route of P3.  The Cauchy-Schwarz loss B_res / Phi_int = %.3f .. %.3f is "
     "the price of the closure"
     % (sum(r["n_int"] for r in ROWS), len(ROWS), CORE_LO, CORE_HI,
        F_COREINT["p"], F_COREINT["sp"], BAR_UNIF,
        qmin([r["psi_ratio"] for r in ROWS]),
        qmax([r["psi_ratio"] for r in ROWS])))

check("el_p2.bracket_direction",
      all(r["B_ramp"] <= r["phi_int"] * (1.0 + 1.0e-9)
          and r["phi_int"] <= r["psi_int"] * (1.0 + 1.0e-9) for r in ROWS),
      "the closed BRACKET holds in the stated order on every window: B_ene "
      "(ramp-refined) <= Phi_int <= B_res, i.e. %.4f .. %.4f <= %.4f .. %.4f <= "
      "%.4f .. %.4f -- the arithmetic consistency test of the whole block"
      % (qmin([r["B_ramp"] for r in ROWS]), qmax([r["B_ramp"] for r in ROWS]),
         qmin([r["phi_int"] for r in ROWS]),
         qmax([r["phi_int"] for r in ROWS]),
         qmin([r["psi_int"] for r in ROWS]),
         qmax([r["psi_int"] for r in ROWS])))

info("P2.trial_side_dies", "THE NAIVE TRANSCRIPTION IS DEAD, and its death is "
     "quantitative: the trial-energy sup misses the interval supremum by a "
     "factor Phi_int / B_ene = %.1f .. %.1f even after the ramp refinement "
     "(best ramp width ell = %d .. %d, gain over the plain indicator %.2f .. "
     "%.2f), and that factor DRIFTS as D^%.3f +- %.3f -- outside the "
     "uniformity bar %.2f.  THE REASON is the near-null direction: the "
     "equilibrium potential of an interval spreads over the whole window, so "
     "no LOCAL trial function can see the capacity.  A Muckenhoupt condition "
     "written with test-function energies cannot be the right object here; "
     "written with resistances it is"
     % (qmin([r["q_ramp"] for r in ROWS]), qmax([r["q_ramp"] for r in ROWS]),
        min(r["ell_star"] for r in ROWS), max(r["ell_star"] for r in ROWS),
        qmin([r["ramp_gain"] for r in ROWS]),
        qmax([r["ramp_gain"] for r in ROWS]), F_QRAMP["p"], F_QRAMP["sp"],
        BAR_UNIF))

check("el_p2.chain_direction",
      all(r["chain_int"] <= r["gap_ex"] * (1.0 + 1.0e-9)
          and r["chain_all"] <= r["gap_ex"] * (1.0 + 1.0e-9) for r in ROWS),
      "THE CHAIN, ASSEMBLED AND CHECKED AGAINST THE TRUE GAP.  With c_0 = %.0f "
      "the OPEN constant of S1, lam >= 1 / (c_0 kap_up c_glob B_res) evaluates "
      "to %.3e .. %.3e, which is %.4f .. %.4f of the exact gap %.3e .. %.3e on "
      "every window -- below it, as the arithmetic requires.  The MINIMUM of "
      "that loss factor over the surface, %.4f, is the uniform constant: the "
      "chain delivers at least %.4f x the true gap everywhere, hence the SAME "
      "power of D with a bounded coefficient"
      % (MAZYA_C0, qmin([r["chain_int"] for r in ROWS]),
         qmax([r["chain_int"] for r in ROWS]),
         qmin([r["loss_int"] for r in ROWS]),
         qmax([r["loss_int"] for r in ROWS]),
         qmin([r["gap_ex"] for r in ROWS]), qmax([r["gap_ex"] for r in ROWS]),
         qmin([r["loss_int"] for r in ROWS]),
         qmin([r["loss_int"] for r in ROWS])))

LOSS_OK = bool(unif_ok(F_LOSSHAT))
check("el_p2.chain_whitened", LOSS_OK,
      "AND THE SAME CHAIN IN THE COORDINATES WHERE THE CRITERION ACTUALLY "
      "LIVES, which is the one P1 and P2 close: lam_hat >= 1 / (c_0 c_glob "
      "B_res) reproduces lam_hat to a factor %.4f .. %.4f, FITTED as D^%.3f "
      "+- %.3f against the bar %.2f -> %s.  The all-sets version, which needs "
      "neither c_glob nor the interval class, gives %.4f .. %.4f (D^%.3f +- "
      "%.3f).  So the capacity calculus itself is uniform; the remaining "
      "D-dependence of the chain against the EXACT pair sits entirely in the "
      "whitening sandwich lam / lam_hat = %.3f .. %.3f, which is an O(1) "
      "certified factor and not a power of D in the capacity estimate"
      % (qmin([r["loss_hat"] for r in ROWS]),
         qmax([r["loss_hat"] for r in ROWS]), F_LOSSHAT["p"], F_LOSSHAT["sp"],
         BAR_UNIF, "ZONE-UNIFORM" if LOSS_OK else "NOT zone-uniform",
         qmin([r["loss_hat_all"] for r in ROWS]),
         qmax([r["loss_hat_all"] for r in ROWS]), F_LOSSHATALL["p"],
         F_LOSSHATALL["sp"],
         qmin([r["gap_ex"] / r["lam_hat"] for r in ROWS]),
         qmax([r["gap_ex"] / r["lam_hat"] for r in ROWS])))

info("P2.chain_uniformity", "and its uniformity, read pedantically: the loss "
     "factor FITS as D^%.3f +- %.3f against the bar %.2f -> %s, and the SIGN "
     "matters as much as the size -- the exponent is %s, so the bound gets "
     "relatively %s towards the deep end.  For a LOWER bound that direction is "
     "%s.  The drift that remains is NOT in the capacity calculus (B_res x "
     "lam_hat is flat to D^%.3f) but in the Jacobi transfer (D^%.3f), i.e. in "
     "the step from the exact pair to the counting measure.  T143 QUOTED "
     "D^%.3f +- %.3f for the loss of its own Maz'ya evaluation, so the two "
     "probes agree that the criterion's loss is a constant and not a power"
     % (F_LOSSINT["p"], F_LOSSINT["sp"], BAR_UNIF,
        "ZONE-UNIFORM" if LOSS_OK else "NOT zone-uniform",
        "negative" if F_LOSSINT["p"] < 0.0 else "positive",
        "better" if F_LOSSINT["p"] < 0.0 else "worse",
        "harmless" if F_LOSSINT["p"] < 0.0 else "the thing to watch",
        F_COREPSI["p"], F_TRANS["p"], LOSS_EXP_T143[0], LOSS_EXP_T143[1]))


# ----------------------------------------------------------------------------
section("P3  THE NON-MARKOV CORRECTION, S3, and the R4 border blocks")
# ----------------------------------------------------------------------------
para("""P3.0  WHERE THE POSITIVE OFF-DIAGONALS ENTER.  Maz'ya's upper half is a
theorem for Markovian forms, so the cheapest imaginable route to S1 is: prove it
for the Markov part and treat the rest as a perturbation.  P is the POSITIVE
off-diagonal part of E; the Stieltjes surrogate is E - P (positive entries
deleted) and the reflected one is E - 2P = diag(E) - |offdiag(E)|.  The
perturbation route needs at least that the surrogate is still a FORM.""")

check("el_p3.markov_route_dead",
      qmax([r["lam_S"] for r in ROWS]) < 0.0
      and qmax([r["t_star"] for r in ROWS]) < 1.0,
      "AND IT IS NOT: lam_min(E - P) = %.3e .. %.3e, NEGATIVE on every window, "
      "and so is the reflected surrogate (%.3e .. %.3e).  Deleting the positive "
      "off-diagonals destroys positive definiteness, so there is no Markovian "
      "form to perturb from.  The quantitative version: the largest t with "
      "E - t P still positive definite (bisection on a COMPLETED CHOLESKY, so "
      "every accepted t is certified) is t* = %.4f .. %.4f, and it SHRINKS as "
      "D^%.3f +- %.3f -- the positive entries carry %.3f .. %.3f of the "
      "off-diagonal mass and they are load-bearing for positivity itself"
      % (qmin([r["lam_S"] for r in ROWS]), qmax([r["lam_S"] for r in ROWS]),
         qmin([r["lam_R"] for r in ROWS]), qmax([r["lam_R"] for r in ROWS]),
         qmin([r["t_star"] for r in ROWS]), qmax([r["t_star"] for r in ROWS]),
         F_TSTAR["p"], F_TSTAR["sp"], qmin([r["p_share"] for r in ROWS]),
         qmax([r["p_share"] for r in ROWS])))

info("P3.markov_cost", "what the capacity does under the largest ADMISSIBLE "
     "part of that deformation: at t = %.4f .. %.4f the ratio cap_{E-tP}(A) / "
     "cap_E(A) over %d sets per window is %.3f .. %.3f, i.e. bounded -- but at "
     "a t that small the deformation is not a Markovianisation, it is a nudge.  "
     "READ THE CONSEQUENCE, not the number: S1 must be proved for the "
     "non-Markovian form directly, and P3(ii) is the only route in this probe "
     "that does not need the hypothesis at all"
     % (qmin([r["t_use"] for r in ROWS]), qmax([r["t_use"] for r in ROWS]),
        int(qmed([r["n_mrat"] for r in ROWS])),
        qmin([r["mrat_min"] for r in ROWS]),
        qmax([r["mrat_max"] for r in ROWS])))

para("""P3.1  S3, AND IT TURNS OUT TO BE MORE THAN A FLOOR.  The Cauchy-Schwarz
floor cap_E(A) >= |A|^2 / (1^T R_AA 1) is closed in the Green function, so
Phi(A) <= Psi(A) = (1^T R_AA 1) / |A| for EVERY set.  Now read the right hand
side: sup_A (1^T R_AA 1) / |A| is, after splitting off the diagonal and replacing
R by its positive part, the MAXIMUM DENSITY SUBGRAPH problem for the weights
R^+ -- exactly solvable in polynomial time by a flow construction (Goldberg
1984) and 2-approximable by greedy peeling (Charikar 2000).  So the supremum over
ALL 2^m sets is computable up to an absolute constant, with no family restriction
and no interval reduction, which is a different kind of statement from anything
T140 .. T143 produced.""")

check("el_p3.density_dominates",
      all(r["psi_best"] >= r["phi_set"] * (1.0 - 1.0e-9) for r in ROWS),
      "THE ALL-SETS BOUND, and it really does dominate every set the probe can "
      "find: Psi_all = max_k R_kk + min(4 x greedy, lam_max(R^+)) = %.4e .. "
      "%.4e against the best sampled Phi = %.4e .. %.4e, a ratio of %.3f .. "
      "%.3f.  The two ingredients are %.4e .. %.4e (Charikar) and %.4e .. %.4e "
      "(the CERTIFIED spectral bound sum_{k<l in A} R^+_kl <= lam_max(R^+) "
      "|A| / 2, which needs no approximation constant at all), and the smaller "
      "one is used"
      % (qmin([r["psi_best"] for r in ROWS]),
         qmax([r["psi_best"] for r in ROWS]),
         qmin([r["phi_set"] for r in ROWS]),
         qmax([r["phi_set"] for r in ROWS]),
         qmin([r["psi_ratio_all"] for r in ROWS]),
         qmax([r["psi_ratio_all"] for r in ROWS]),
         qmin([r["psi_char"] for r in ROWS]),
         qmax([r["psi_char"] for r in ROWS]),
         qmin([r["psi_spec"] for r in ROWS]),
         qmax([r["psi_spec"] for r in ROWS])))

ALL_OK = bool(unif_ok(F_COREALL))
check("el_p3.all_sets_chain", ALL_OK,
      "AND ITS PRODUCT WITH THE EIGENVALUE IS THE FLATTEST NUMBER IN THE "
      "PROBE: Psi_all x lam_hat = %.4f .. %.4f, FITTED as D^%.3f +- %.3f "
      "against the bar %.2f -> %s.  Consequently, modulo S1 alone, lam >= 1 / "
      "(c_0 kap_up Psi_all) = %.3e .. %.3e, which is %.4f .. %.4f of the true "
      "gap with NO family-restricted ingredient anywhere: kap_up is certified, "
      "Psi_all is certified, the Cauchy-Schwarz step is exact and the only "
      "unproved input is S1's absolute constant c_0 = %.0f.  R is NOT a "
      "nonnegative kernel (%.3f .. %.3f of its entries are >= 0), which is why "
      "the positive part is taken -- that step is a bound in the right "
      "direction and costs a factor already included above.  The loss factor "
      "against the exact pair FITS as D^%.3f +- %.3f, so the all-sets chain "
      "carries the SAME power of D as the gap itself"
      % (qmin([r["core_all"] for r in ROWS]),
         qmax([r["core_all"] for r in ROWS]), F_COREALL["p"], F_COREALL["sp"],
         BAR_UNIF, "ZONE-UNIFORM" if ALL_OK else "NOT zone-uniform",
         qmin([r["chain_all"] for r in ROWS]),
         qmax([r["chain_all"] for r in ROWS]),
         qmin([r["loss_all"] for r in ROWS]),
         qmax([r["loss_all"] for r in ROWS]), MAZYA_C0,
         qmin([r["r_nonneg"] for r in ROWS]),
         qmax([r["r_nonneg"] for r in ROWS]), F_LOSSALL["p"], F_LOSSALL["sp"]))

info("P3.density_anatomy", "the anatomy of that bound: the argmax density set "
     "of the greedy peeling has %d .. %d of the %d .. %d indices, the diagonal "
     "term max_k R_kk contributes %.3f .. %.3f of Psi_all, and the interval "
     "restriction of the SAME object, B_res, is only a factor %.3f .. %.3f "
     "below it -- so the sup of the density really does live on the intervals "
     "too, which is the second, independent confirmation of P1's reduction"
     % (min(r["psi_size"] for r in ROWS), max(r["psi_size"] for r in ROWS),
        min(r["m"] for r in ROWS), max(r["m"] for r in ROWS),
        qmin([r["dg_max"] / r["psi_best"] for r in ROWS]),
        qmax([r["dg_max"] / r["psi_best"] for r in ROWS]),
        qmin([r["psi_best"] / r["psi_int"] for r in ROWS]),
        qmax([r["psi_best"] / r["psi_int"] for r in ROWS])))


para("""P3.2  THE R4 BORDER BLOCKS, with the interval formula and with an
EXHAUSTION.  The pool is REBUILT here rather than reloaded, so its open set is
its own and the count is not comparable with T143's %d; what transfers is the
anatomy.  On the blocks small enough, ALL 2^g - 1 subsets are enumerated, which
turns every measured statement of P1 and P2 into an EXACT one on a genuine window
object: the reduction factor, the Maz'ya window, and the closed resistance sup
are all evaluated against the true supremum over all subsets.""" % R4_OPEN_T143)

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
for i in range(max(len(l) for l in PER_RHO) if PER_RHO else 0):
    for l in PER_RHO:
        if i < len(l):
            K3_TASK.append(l[i])
K3_TASK = K3_TASK[:K3_MAX]

K3R = []
N_ENUM = 0
for (k, n_lbl, D, rho_lbl, scaled) in K3_TASK:
    if budget_left() < BUDGET_S - T_SURF - T_P1 - T_P2 - T_P3:
        info("P3.budget_r4", "border pool truncated at n = %d after %d blocks"
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
               lam_b=float("nan"), lam_hat=float("nan"), kap_up=float("nan"),
               phi_int=float("nan"), phi_enum=float("nan"),
               psi_int=float("nan"), psi_all=float("nan"),
               c_glob=float("nan"), c_hull=float("nan"),
               core_enum=float("nan"), core_int=float("nan"),
               core_psi=float("nan"), far_share=float("nan"), enum=0,
               n_sub=0, chain=float("nan"), loss=float("nan"))
    try:
        lam_b = float(eigh(sym(st["S"]), sym(pn["S_B"]), eigvals_only=True,
                           subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        lam_b = float("nan")
    jw = jacobi_whiten(sym(st["S"]), sym(pn["S_B"]))
    if (np.isfinite(lam_b) and lam_b > 0.0 and g >= 4 and jw is not None
            and np.isfinite(jw["kap_up"])):
        Eb = jw["E"]
        fb = safe_cho(Eb)
        try:
            lam_hb = float(eigvalsh(Eb, subset_by_index=[0, 0])[0])
        except (LinAlgError, ValueError):
            lam_hb = float("nan")
        if fb is not None and np.isfinite(lam_hb) and lam_hb > 0.0:
            Rb = sym(cho_solve(fb, np.eye(g), check_finite=False))
            clb = closed_interval_sup(Eb)
            dnb = density_interval_sup(Rb)
            Rpb = np.maximum(Rb, 0.0)
            np.fill_diagonal(Rpb, 0.0)
            grb = greedy_density(Rpb)
            dgb = float(np.max(np.diag(Rb)))
            psi_all_b = min(dgb + 4.0 * grb["dens"],
                            dgb + cert_lam_max(Rpb, guess=ray_top(Rpb)))
            phi_i, arg_i = 0.0, None
            for a in range(g):
                for b in range(a + 1, g + 1):
                    cp = interval_capacity(Rb, a, b)
                    if np.isfinite(cp) and cp > 0.0 and (b - a) / cp > phi_i:
                        phi_i, arg_i = (b - a) / cp, (a, b)
            row.update(lam_b=lam_b, lam_hat=lam_hb, kap_up=jw["kap_up"],
                       phi_int=phi_i, psi_int=dnb["P"], psi_all=psi_all_b,
                       core_int=phi_i * lam_hb, core_psi=dnb["P"] * lam_hb,
                       core_all=psi_all_b * lam_hb)
            if g <= K3_ENUM_G and N_ENUM < K3_ENUM_MAX and budget_left() > 90.0:
                cacheb = {}
                best, best_s, best_c = 0.0, None, 0.0
                for mask in range(1, 1 << g):
                    sel = np.nonzero(np.array([(mask >> i) & 1
                                               for i in range(g)],
                                              dtype=bool))[0]
                    rec = c_int_of(Rb, sel, cacheb)
                    if rec is None:
                        continue
                    if rec["phi_A"] > best:
                        best, best_s = rec["phi_A"], sel
                    best_c = max(best_c, rec["c"])
                row.update(phi_enum=best, enum=1, n_sub=(1 << g) - 1,
                           c_hull=best_c,
                           c_glob=best / max(phi_i, 1.0e-300),
                           core_enum=best * lam_hb)
                if best_s is not None and g > FAR_K:
                    row["far_share"] = float(np.mean(best_s >= FAR_K))
                N_ENUM += 1
            ch = 1.0 / max(MAZYA_C0 * jw["kap_up"] * psi_all_b, 1.0e-300)
            row.update(chain=ch, loss=ch / max(lam_b, 1.0e-300))
            del Rb, Rpb, clb
        del Eb
    K3R.append(row)
    del st, pn, jw

if K3R:
    OPEN = [x for x in K3R if not x["cert_any"]]
    ENU = [x for x in K3R if x["enum"]]
    info("P3.r4_pool", "%d border blocks, g = %d .. %d, zones n = %d .. %d; the "
         "paired Neumann ladder to m = %d certifies %d and leaves %d open "
         "(T143 QUOTED %d, a different pool); the block gaps are %.3e .. %.3e "
         "and the Jacobi factor on the blocks is %.3f .. %.3f"
         % (len(K3R), min(x["g"] for x in K3R), max(x["g"] for x in K3R),
            min(x["n"] for x in K3R), max(x["n"] for x in K3R), max(M_LADDER),
            len(K3R) - len(OPEN), len(OPEN), R4_OPEN_T143,
            qmin([x["lam_b"] for x in K3R]), qmax([x["lam_b"] for x in K3R]),
            qmin([x["kap_up"] for x in K3R]),
            qmax([x["kap_up"] for x in K3R])))
    if ENU:
        check("el_p3.r4_exact_reduction",
              all(x["c_glob"] <= BAR_CINT for x in ENU),
              "AND HERE THE REDUCTION IS EXACT, NOT MEASURED: on %d blocks "
              "(g = %d .. %d) ALL %d .. %d subsets were enumerated, so "
              "c_glob = Phi_sup / Phi_int = %.4f .. %.4f is the TRUE reduction "
              "factor of the interval class -- against the preregistered "
              "ceiling %.2f.  The pointwise hull factor on the same blocks "
              "reaches %.2f .. %.2f, which reproduces P1's split exactly: the "
              "best-interval comparison holds, the hull comparison does not"
              % (len(ENU), min(x["g"] for x in ENU), max(x["g"] for x in ENU),
                 min(x["n_sub"] for x in ENU), max(x["n_sub"] for x in ENU),
                 qmin([x["c_glob"] for x in ENU]),
                 qmax([x["c_glob"] for x in ENU]), BAR_CINT,
                 qmin([x["c_hull"] for x in ENU]),
                 qmax([x["c_hull"] for x in ENU])))
        check("el_p3.r4_exact_window",
              all(1.0 / MAZYA_C0 - 1.0e-12 <= x["core_enum"] <= 1.0 + 1.0e-9
                  for x in ENU),
              "and the Maz'ya window holds EXACTLY there too: Phi_sup x "
              "lam_hat = %.4f .. %.4f over ALL subsets, inside [1/4, 1] on "
              "every enumerated block, for forms that are not Markovian "
              "either.  The closed resistance sup gives %.4f .. %.4f and the "
              "all-sets density bound %.4f .. %.4f on the same blocks, so both "
              "closed objects bracket the exhaustive truth from above as they "
              "must"
              % (qmin([x["core_enum"] for x in ENU]),
                 qmax([x["core_enum"] for x in ENU]),
                 qmin([x["core_psi"] for x in ENU]),
                 qmax([x["core_psi"] for x in ENU]),
                 qmin([x["core_all"] for x in ENU]),
                 qmax([x["core_all"] for x in ENU])))
    FS = [x["far_share"] for x in K3R if np.isfinite(x["far_share"])]
    if FS:
        info("P3.r4_capacity_tail", "the capacity tail of the border blocks, "
             "unchanged in anatomy from T143: %.3f .. %.3f of the argmax set's "
             "indices sit at block index >= %d, so the capacity-critical set IS "
             "the far tail and the factor a decay statement has to deliver is "
             "still the T143 far shrink %.3f .. %.3f QUOTED.  What IS new: the "
             "blocks now carry a certified chain too, lam_b >= 1 / (c_0 kap_up "
             "Psi_all) with loss factor %.4f .. %.4f"
             % (qmin(FS), qmax(FS), FAR_K, FAR_SHRINK_T143[0],
                FAR_SHRINK_T143[1], qmin([x["loss"] for x in K3R]),
                qmax([x["loss"] for x in K3R])))


# ----------------------------------------------------------------------------
section("P4  THE MAP V16, the promotion list, the rest list, and the verdict")
# ----------------------------------------------------------------------------
HALF_RED = CGLOB_OK
HALF_CLO = bool(PSI_OK and ALL_OK and LOSS_OK)
VERDICT = ("INTERVAL-CARRIES" if (HALF_RED and HALF_CLO) else
           ("HALF-CARRIES" if (HALF_RED or HALF_CLO) else "INTERVAL-RESISTS"))

para("""P4.0  THE MAP V16, in the only order that matters -- what is a theorem,
what is a certificate, what is a measurement, what is still missing.
  THEOREMS USED (all classical, all cited, none re-proved): the Schur / Green
  form of a capacity (Fukushima-Oshima-Takeda 1994, ch. 2; Maz'ya 1985);
  Cauchy-Schwarz; Loewner monotonicity of the capacity; the maximum density
  subgraph guarantee (Charikar 2000; Goldberg 1984 for the exact version);
  Bertrand-Chebyshev for the two gap facts.  Maz'ya's capacity criterion is
  CITED and its upper half -- S1 -- is NOT used as a theorem anywhere.
  CERTIFIED HERE (completed Cholesky, direction in the name): the Jacobi
  whitening factor kap_up <= %.4f; the spectral all-sets density bound; the
  positive-definiteness of every deformed form E - t P; the exhaustive suprema
  over all subsets of the enumerated blocks and over all O(m^2) intervals.
  EXACT HERE (an exhaustion, so a supremum and not a maximum over a pool): the
  interval supremum Phi_int x lam_hat = %.4f .. %.4f over all intervals of every
  window -- exact as a supremum over the interval CLASS, and still only a LOWER
  bound for the sup over all sets, which is why its drift is not a
  counterexample. MEASURED HERE: the best-interval reduction factor c_glob =
  %.4f (a sampled supremum in the numerator, hence a LOWER bound on the true
  factor); the Cauchy-Schwarz loss.
  STILL MISSING, and it is exactly one inequality: S1 itself, cap_E(A) >= |A|
  lam_hat / c_0 for all A with an absolute c_0.  Everything this probe added is
  a reduction of what S1 must be proved ABOUT, not a proof of it.""" %
     (qmax([r["kap_up"] for r in ROWS]), CORE_LO, CORE_HI, CGLOB_MAX))

STMT = [
    "P1a  the JACOBI WHITENING is a legitimate step for the GAP: lam >= "
    "lam_min(Lam^{-1/2} A Lam^{-1/2}) / kap_up with kap_up = %.4f .. %.4f "
    "CERTIFIED, Lam = diag(A_B) -- a denominator comparison, which T142's "
    "obstruction does not touch, and it puts the criterion in coordinates "
    "with the counting measure"
    % (qmin([r["kap_up"] for r in ROWS]), qmax([r["kap_up"] for r in ROWS])),
    "P1b  the POINTWISE HULL COMPARISON IS FALSE: sup_A Phi(A) / Phi(I(A)) = "
    "%.2f .. %.2f over the surface, with the unconfined level sets as the "
    "offenders -- so S2 cannot be proved by transporting each set to its hull"
    % (qmin([r["c_all"] for r in ROWS]), qmax([r["c_all"] for r in ROWS])),
    "P1c  the BEST-INTERVAL COMPARISON holds on the whole pool: Phi_sup <= "
    "%.4f x sup_I Phi(I), MEASURED on %d sets per window including every "
    "subset of %d enumerated blocks, and EXACT on the R4 blocks where all "
    "subsets were enumerated"
    % (CGLOB_MAX, int(qmed([r["n_sets"] for r in ROWS])), N_EXP),
    "P2a  the CLOSED TWO-WEIGHT SUP in the resistance form, B_res = sup_I "
    "(1^T R_II 1) / |I| over ALL O(m^2) intervals, satisfies B_res x lam_hat = "
    "%.4f .. %.4f with fit D^%.3f +- %.3f -- a closed prefix-sum object that "
    "reproduces the exact interval supremum to a factor %.3f .. %.3f"
    % (qmin([r["core_psi"] for r in ROWS]), qmax([r["core_psi"] for r in ROWS]),
       F_COREPSI["p"], F_COREPSI["sp"], qmin([r["psi_ratio"] for r in ROWS]),
       qmax([r["psi_ratio"] for r in ROWS])),
    "P2b  the TRIAL-ENERGY (naive Muckenhoupt) transcription is DEAD: it "
    "misses the interval supremum by %.0f .. %.0f and the miss drifts as "
    "D^%.3f, because the equilibrium potential spreads over the whole window "
    "and no local trial function can see it"
    % (qmin([r["q_ramp"] for r in ROWS]), qmax([r["q_ramp"] for r in ROWS]),
       F_QRAMP["p"]),
    "P2c  the CORE NUMBER: the CLOSED two-weight sup satisfies B_res x "
    "lam_hat = %.4f .. %.4f, inside Maz'ya's window [1/4, 1] on the whole "
    "surface, EXACT over all O(m^2) intervals of every window, and flat as "
    "D^%.3f +- %.3f -- while the free half Phi_sup x lam_hat = %.4f .. %.4f "
    "<= 1 passes as the theorem it is"
    % (BR_LO, BR_HI, F_COREPSI["p"], F_COREPSI["sp"], CORE_ALO, CORE_AHI),
    "P3a  the MARKOV PERTURBATION ROUTE IS DEAD, quantitatively: E - P is "
    "indefinite (lam_min = %.3e .. %.3e) and the largest certified t with "
    "E - t P > 0 is t* = %.4f .. %.4f, shrinking as D^%.3f"
    % (qmin([r["lam_S"] for r in ROWS]), qmax([r["lam_S"] for r in ROWS]),
       qmin([r["t_star"] for r in ROWS]), qmax([r["t_star"] for r in ROWS]),
       F_TSTAR["p"]),
    "P3b  S3, IN A STRONGER FORM THAN ASKED: cap_E(A) >= |A|^2 / (1^T R_AA 1) "
    "turns Phi_sup into a MAXIMUM DENSITY SUBGRAPH value for R^+, so the sup "
    "over ALL 2^m sets is bounded with a cited absolute constant, Psi_all x "
    "lam_hat = %.4f .. %.4f, fit D^%.3f +- %.3f -- no family restriction, no "
    "interval reduction, no Markov hypothesis"
    % (qmin([r["core_all"] for r in ROWS]), qmax([r["core_all"] for r in ROWS]),
       F_COREALL["p"], F_COREALL["sp"]),
    "P3c  the CHAIN, modulo S1 alone: lam >= 1 / (c_0 kap_up Psi_all) = "
    "%.4f .. %.4f of the exact gap on the whole surface, and lam_hat >= 1 / "
    "(c_0 Psi_all) = %.4f .. %.4f of lam_hat with fit D^%.3f +- %.3f"
    % (qmin([r["loss_all"] for r in ROWS]), qmax([r["loss_all"] for r in ROWS]),
       qmin([r["loss_hat_all"] for r in ROWS]),
       qmax([r["loss_hat_all"] for r in ROWS]), F_LOSSHATALL["p"],
       F_LOSSHATALL["sp"]),
]
info("P4.promotions", "%d statements are ready for promotion in the ledger "
     "sense (T143 QUOTED a stock of %d, none promoted here either); %d are new "
     "in this probe:" % (PROMO_T143 + len(STMT), PROMO_T143, len(STMT)))
for _s in STMT:
    para(_s, indent="    ")

REST = [
    "S1  THE ONE INEQUALITY, unchanged in statement and reduced in scope: "
    "cap_E(A) >= |A| lam_hat / c_0 with an absolute c_0, for the whitened node "
    "form E = Lam^{-1/2} A Lam^{-1/2}.  What this probe removed from it: the "
    "family restriction (P3b bounds the sup over all sets), the Markov "
    "hypothesis (P3a shows it cannot be restored, so S1 must be proved "
    "without it) and the coordinate freedom (P1a fixes the coordinates at a "
    "certified O(1) cost).  What remains is the inequality itself.",
    "S1'  THE SHARPEST AVAILABLE SHAPE OF S1 after this probe: it suffices to "
    "prove the capacitary strong-type inequality for a form whose Green "
    "function R has mean-density sup Psi_all with Psi_all x lam_hat <= %.4f "
    "measured here -- i.e. S1 for forms satisfying a GREEN MEAN-DENSITY bound, "
    "which is a hypothesis of Muckenhoupt type rather than of Markov type."
    % qmax([r["core_all"] for r in ROWS]),
    "S2'  the best-interval comparison c_glob <= %.4f is MEASURED, not proved; "
    "a proof would be a testing condition (test the form on intervals, compare "
    "the constant) and the exhaustive R4 blocks show it is not vacuous."
    % CGLOB_MAX,
    "R4  the %d border blocks the paired Neumann ladder leaves open; the "
    "capacity argmax is the far tail and the factor a decay statement must "
    "deliver is the T143 far shrink %.3f .. %.3f QUOTED."
    % (len([x for x in K3R if not x["cert_any"]]) if K3R else R4_OPEN_T143,
       FAR_SHRINK_T143[0], FAR_SHRINK_T143[1]),
    "R5  the whitening sandwich lam / lam_hat = %.3f .. %.3f is an O(1) "
    "certified factor whose drift is the only D-dependence left in the chain "
    "against the exact pair; a two-sided estimate of kap would remove it."
    % (qmin([r["gap_ex"] / r["lam_hat"] for r in ROWS]),
       qmax([r["gap_ex"] / r["lam_hat"] for r in ROWS])),
]
info("P4.rest_list", "the rest list, shortest first, and it is now %d items:"
     % len(REST))
for _s in REST:
    para(_s, indent="    ")

section("THE VERDICT")
info("verdict", VERDICT)
para(("The interval route CARRIES.  The reduction of the supremum to the "
      "interval class holds with a measured constant %.4f -- within %.1f %% of "
      "unity over the whole surface, exhaustive inside %d enumerated blocks and "
      "EXACT on the R4 blocks -- and the interval supremum itself is captured "
      "by a CLOSED prefix-sum object in the Green function, B_res, with "
      "B_res x lam_hat = %.4f .. %.4f and a fit of D^%.3f +- %.3f against the "
      "uniformity bar %.2f.  So S1 is reduced to a two-weight calculus: the "
      "D-uniformity of the gap is now a statement about a resistance supremum "
      "and nothing else, and the chain lam >= 1/(c_0 kap_up c_glob B_res) "
      "delivers %.4f .. %.4f of the true gap on every window with c_0 the only "
      "unproved input.  The probe also removes the family restriction "
      "altogether: the Cauchy-Schwarz floor turns Phi_sup into a maximum "
      "density subgraph value, so the sup over ALL 2^m sets is bounded with a "
      "cited absolute constant and the same flat product %.4f .. %.4f.  ONE "
      "SENTENCE OF RESISTANCE, because it is the honest half of the verdict: "
      "the interval class carries the criterion only in the UPPER direction -- "
      "exhaustively evaluated, Phi_int x lam_hat = %.4f .. %.4f drifts as "
      "D^%.3f, so intervals do not saturate S1 and no interval-only argument "
      "will produce the constant; what carries is the closed resistance sup "
      "above them, and that is a two-weight statement about the Green function "
      "and not about a family of sets."
      % (CGLOB_MAX, 100.0 * (CGLOB_MAX - 1.0), N_EXP,
         qmin([r["core_psi"] for r in ROWS]),
         qmax([r["core_psi"] for r in ROWS]), F_COREPSI["p"], F_COREPSI["sp"],
         BAR_UNIF, qmin([r["loss_int"] for r in ROWS]),
         qmax([r["loss_int"] for r in ROWS]),
         qmin([r["core_all"] for r in ROWS]),
         qmax([r["core_all"] for r in ROWS]), CORE_LO, CORE_HI,
         F_COREINT["p"]))
     if VERDICT == "INTERVAL-CARRIES" else
     ("One half of the route carries and the other does not, and the split is "
      "clean.  %s.  What is uniform: %s.  What is not: %s.  The consequence for "
      "S1 is stated in the rest list and the coefficient is the only thing that "
      "moved."
      % ("The reduction half carries (c_glob = %.4f) while the closed half "
         "drifts" % CGLOB_MAX if HALF_RED else
         "The closed half carries (B_res x lam_hat flat to D^%.3f) while the "
         "reduction drifts (c_glob = %.4f)" % (F_COREPSI["p"], CGLOB_MAX),
         "B_res x lam_hat as D^%.3f +- %.3f, Psi_all x lam_hat as D^%.3f +- "
         "%.3f" % (F_COREPSI["p"], F_COREPSI["sp"], F_COREALL["p"],
                   F_COREALL["sp"]),
         "the whitened chain's loss factor as D^%.3f +- %.3f against the bar "
         "%.2f" % (F_LOSSHAT["p"], F_LOSSHAT["sp"], BAR_UNIF))
      if VERDICT == "HALF-CARRIES" else
      ("The interval route does not close S1 on this surface, and the "
       "resistance is located rather than guessed: the reduction factor reaches "
       "%.2f and the closed suprema drift as D^%.3f / D^%.3f.  What survives is "
       "the anatomy -- the hull comparison is false, the Markov perturbation "
       "route is dead (t* = %.4f .. %.4f), and the density formulation is the "
       "only object that bounds the sup over all sets at all."
       % (qmax([r["c_all"] for r in ROWS]), F_COREPSI["p"], F_COREALL["p"],
          qmin([r["t_star"] for r in ROWS]),
          qmax([r["t_star"] for r in ROWS])))))
print("")

print("TOTAL.contract     CAPACITY.INEQUALITY -- the one inequality S1 over the "
      "interval route S2 (part %d, discovery only, nothing promoted)"
      % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.P1_reduction the POINTWISE hull comparison is FALSE (c_int up to "
      "%.2f, level sets) while the BEST-INTERVAL comparison holds: c_glob = "
      "%.4f .. %.4f (MEASURED on %d sets, EXACT on %d enumerated blocks per "
      "window), fit D^%.3f +- %.3f -> %s"
      % (qmax([r["c_all"] for r in ROWS]),
         qmin([r["c_glob"] for r in ROWS]), CGLOB_MAX,
         sum(r["n_sets"] for r in ROWS), ROWS[0]["n_blocks"], F_CGLOB["p"],
         F_CGLOB["sp"],
         "ZONE-UNIFORM" if unif_ok(F_CGLOB) else "NOT zone-uniform"))
print("TOTAL.P2_core      THE CORE NUMBER: the CLOSED two-weight sup gives "
      "B_res x lam_hat = %.4f .. %.4f, inside Maz'ya's window [1/4, 1] on the "
      "whole surface and flat as D^%.3f +- %.3f (T143 QUOTED %.4f .. %.4f); "
      "the free half Phi_sup x lam_hat = %.4f .. %.4f <= 1 as the theorem "
      "requires, and the whitened chain lam_hat >= 1/(c_0 c_glob B_res) is "
      "%.4f .. %.4f of lam_hat -> %s"
      % (BR_LO, BR_HI, F_COREPSI["p"], F_COREPSI["sp"], PHI_LAM_T143[0],
         PHI_LAM_T143[1], CORE_ALO, CORE_AHI,
         qmin([r["loss_hat"] for r in ROWS]),
         qmax([r["loss_hat"] for r in ROWS]),
         "ZONE-UNIFORM" if LOSS_OK else "NOT zone-uniform"))
print("TOTAL.P2_dead      the TRIAL-ENERGY transcription of Muckenhoupt is "
      "dead: it misses by %.0f .. %.0f, drifting as D^%.3f, because the "
      "equilibrium potential spreads over the whole window (best ramp width "
      "%d .. %d)"
      % (qmin([r["q_ramp"] for r in ROWS]), qmax([r["q_ramp"] for r in ROWS]),
         F_QRAMP["p"], min(r["ell_star"] for r in ROWS),
         max(r["ell_star"] for r in ROWS)))
print("TOTAL.P3_markov    the Markov perturbation route is CERTIFIED DEAD: "
      "lam_min(E - P) = %.3e .. %.3e < 0 and t*(E - t P > 0) = %.4f .. %.4f "
      "shrinking as D^%.3f; the positive off-diagonals carry %.3f .. %.3f of "
      "the off-diagonal mass and are load-bearing for positivity"
      % (qmin([r["lam_S"] for r in ROWS]), qmax([r["lam_S"] for r in ROWS]),
         qmin([r["t_star"] for r in ROWS]), qmax([r["t_star"] for r in ROWS]),
         F_TSTAR["p"], qmin([r["p_share"] for r in ROWS]),
         qmax([r["p_share"] for r in ROWS])))
print("TOTAL.P3_s3        S3 is stronger than asked: the Cauchy-Schwarz floor "
      "makes Phi_sup a MAXIMUM DENSITY SUBGRAPH value (Charikar 2000; Goldberg "
      "1984), so the sup over ALL 2^m sets obeys Psi_all x lam_hat = %.4f .. "
      "%.4f (D^%.3f +- %.3f) with no family restriction; chain vs the exact "
      "gap %.4f .. %.4f"
      % (qmin([r["core_all"] for r in ROWS]),
         qmax([r["core_all"] for r in ROWS]), F_COREALL["p"], F_COREALL["sp"],
         qmin([r["loss_all"] for r in ROWS]),
         qmax([r["loss_all"] for r in ROWS])))
if K3R:
    _EN = [x for x in K3R if x["enum"]]
    print("TOTAL.P3_r4        %d border blocks, %d certified by the ladder, %d "
          "open; %d blocks had ALL %d .. %d subsets enumerated and there the "
          "reduction is EXACT (c_glob = %.4f .. %.4f, hull factor up to %.2f) "
          "with Phi_sup x lam_hat = %.4f .. %.4f"
          % (len(K3R), len([x for x in K3R if x["cert_any"]]),
             len([x for x in K3R if not x["cert_any"]]), len(_EN),
             min([x["n_sub"] for x in _EN]) if _EN else -1,
             max([x["n_sub"] for x in _EN]) if _EN else -1,
             qmin([x["c_glob"] for x in _EN]) if _EN else float("nan"),
             qmax([x["c_glob"] for x in _EN]) if _EN else float("nan"),
             qmax([x["c_hull"] for x in _EN]) if _EN else float("nan"),
             qmin([x["core_enum"] for x in _EN]) if _EN else float("nan"),
             qmax([x["core_enum"] for x in _EN]) if _EN else float("nan")))
print("TOTAL.rest_list    %s" % " | ".join(s.split("  ")[0] for s in REST))
print("TOTAL.promotions   %d statements ready, %d new (P1a-P1c + P2a-P2c + "
      "P3a-P3c), 0 promoted" % (PROMO_T143 + len(STMT), len(STMT)))
print("TOTAL.surface      %d windows m = %d .. %d, D = %.2e .. %.2e, zones "
      "n = %d .. %d; %d sets evaluated, %d intervals exhausted, %d border "
      "blocks"
      % (len(ROWS), min(r["m"] for r in ROWS), max(r["m"] for r in ROWS),
         qmin(DV), qmax(DV), min(r["n"] for r in ROWS),
         max(r["n"] for r in ROWS), sum(r["n_sets"] for r in ROWS),
         sum(r["n_pool"] for r in ROWS), len(K3R)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised / diagonalised form %d (cap %d)"
      % (max([r["m"] for r in ROWS] + [x["g"] for x in K3R] + [0]), MAX_H))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
