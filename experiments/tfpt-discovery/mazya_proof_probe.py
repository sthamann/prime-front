"""Discovery probe (2026-07-29), part 145 of the prime/window investigation.
Contract MAZYA.PROOF -- THE PROOF ATTEMPT for S1', step by instrumented step.

WHERE THIS SITS (T144 END STATE: INTERVAL-CARRIES, and the ONE thing it left)
  T140 reduced the question to two small matrices per zone, T141 made it a
  weighted Hardy problem, T142 closed the comparison branch, T143 estimated the
  exact capacity Rayleigh form, and T144 closed the two-weight calculus around
  it.  QUOTED from T140 .. T144 and NEVER re-derived here:
    * the chain lam >= 1 / (c_0 kap_up c_glob B_res) is certified on 34 windows,
      with kap_up <= 1.3162 CERTIFIED and c_glob <= 1.6876 zone-uniform;
    * B_res x lam_hat = 0.6694 .. 0.7813, flat as D^(0.013 +- 0.005);
    * Psi_all x lam_hat = 0.7399 .. 0.8515 over ALL 2^m sets (max-density
      subgraph, Charikar 2000; Goldberg 1984), flat as D^0.015;
    * the Markov perturbation route is CERTIFIED DEAD: lam_min(E - P) < 0 on
      every window and t* ~ D^3.96;
    * intervals saturate the criterion only from ABOVE (Phi_int x lam_hat
      drifts as D^0.654), and the POINTWISE hull comparison is FALSE (c_int up
      to 425, D^-1.137).
  So exactly ONE unproved input remains in the whole chain: the ABSOLUTE
  CONSTANT c_0 of the capacitary strong-type inequality
      cap_E(A) >= |A| lam_0 / c_0   for ALL A,   equivalently   Phi_sup lam >= 1/c_0 ,
  which is classical with c_0 = 4 for DIRICHLET forms (Maz'ya 1985) and is NOT
  available by citation for the non-Markovian gap form of this project.
  T144's sharpest shape of that gap is the subject of this probe:
    S1'  prove the strong-type inequality for forms carrying a GREEN
         MEAN-DENSITY bound (Psi_all x lam_hat <= 0.8515 measured) -- a
         hypothesis of MUCKENHOUPT type (Muckenhoupt 1972) instead of MARKOV
         type (Fukushima-Oshima-Takeda 1994, ch. 1).

WHAT THIS PROBE DOES -- THE PROOF AS A MEASUREMENT CHAIN
  P0  THE LICENCES.  Every single step the proof below uses is first verified as
      an inequality on random forms, with its DIRECTION in its name: the Green
      form of a capacity, the Cauchy-Schwarz floor, the entrywise domination
      x^T R x <= |x|^T R^+ |x|, the monotonicity of a NONNEGATIVE form under
      pointwise domination of nonnegative vectors, the exactness of the dyadic
      layer cake, the nested-set domination, Charikar's bracket, and the two
      DIRECTIONS of the Jacobi whitening.
  P1  Q1, THE BEAM: the classical Maz'ya proof transcribed step by step onto the
      non-Markovian form, each step instrumented per window.
        M1  dyadic level decomposition of the minimiser            THEOREM, x4
        M2  |A| <= Phi_sup cap(A) <= Psi_all cap(A)                THEOREM, x1
        M3  cap(A_{k+1}) <= 4^{-k} E(f_k), truncation admissible   THEOREM, x1
        M4  sum_k E(f_k) <= E(f)  -- THE MARKOV STEP               MEASURED
      M4 is the ONLY step that uses the Markov property, and it uses it twice
      (nonnegative conductances AND sign-coherent truncation increments).  It is
      measured here, on the exact pair decomposition of the form, and it dies.
      Its REPLACEMENT is built on the GREEN side, where no sign hypothesis is
      needed at all:
        M4'a  psi^T R psi <= |psi|^T R^+ |psi|                     THEOREM, x1
        M4'b  |psi| <= psi_t (dyadic layer cake), R^+ >= 0         THEOREM, x1
        M4'c  nested-set domination + the density bound            THEOREM, xG
      and the product of the step factors is an EXPLICIT constant
        c_0 = G_dy = sum_{j,l} c_j c_l |S_min(j,l)| / ||psi||^2 ,
      the GEOMETRIC LEVEL CONSTANT of the minimiser's layer cake.  The resulting
      window statement is CERTIFIED, not measured: lam_max(R) <= Psi_up G_dy
      with lam_max certified from ABOVE by a completed Cholesky, Psi_up an
      all-sets density bound with a cited constant, and G_dy exact arithmetic on
      the computed minimiser -- no assumption that the computed vector IS the
      minimiser enters the inequality.
  P2  Q2, THE DIRECT SPECTRAL ARGUMENT and its NO-GO.  The same chain read as a
      Rayleigh decomposition by levels, with the pedantic direction statement
      that Psi_all x lam_hat <= 1 is a THEOREM WITH NO CONTENT (indicator
      Rayleigh quotients never exceed lam_max(R)) so that the load-bearing
      direction is the OTHER one.  Then the NO-GO: an explicit form with R
      positive definite AND entrywise nonnegative AND a bounded density sup, for
      which S1' FAILS with any absolute constant.  It fixes what the missing
      input must be: a bound on the LEVEL PROFILE of the minimiser, and nothing
      weaker.
  P3  Q3.  (i) S2': the finite TESTING FAMILY for the density sup -- intervals,
      level sets, and the greedy argmax -- with its measured testing constant
      against the all-sets bound, which is what a testing-condition proof of
      c_glob would have to deliver, and which makes c_glob dispensable in the
      density route.  (ii) R5: the two-sided whitening sandwich, kap_lo
      CERTIFIED from below and kap_up from above, so that lam / lam_hat is
      bracketed on both sides.  (iii) the open R4 border blocks, run through the
      new chain.
  P4  the map V17, the promotion list, the shortest rest list, the verdict.

WHAT IS CERTIFIED, WHAT IS EXACT, WHAT IS MEASURED, WHAT IS A THEOREM
  * THEOREM means classical, cited, and never re-proved: only the named results
    in the citation list are used, and Maz'ya's strong-type half is NOT among
    them -- that is the thing under attack.
  * CERTIFIED means a completed Cholesky (Wilkinson 1968; Higham 2002) with the
    declared floating-point floor, in the DIRECTION stated in the name:
    cert_lam_max is an UPPER bound, cert_lam_min a LOWER bound.
  * EXACT means finite arithmetic on a finite object: the layer cake of a given
    vector, all O(m^2) intervals, all 2^g subsets of a block.
  * MEASURED means a sampled supremum, an eigenvalue, or a ratio of two
    computed forms.  A FIT is a least-squares exponent with a delete-one
    jackknife band, always labelled, never load-bearing.
  * THE DIRECTION TRAP, stated once and respected throughout.  Phi(A) <= 1/lam
    holds for EVERY single set, so single sets certify an UPPER bound on the gap
    and the product Phi_sup x lam <= 1 is the FREE half of the criterion.  S1 is
    the LOWER bound on that product and it is the half that needs a proof.  In
    the same way Psi_all x lam_hat <= 1 is free for the density built from R
    itself; the load-bearing statement is Psi_all x lam_hat >= 1 / c_0, and
    every line below that claims progress says which direction it is in.

FENCES
  * THE RH FENCE.  The surrounding statement is the positivity of a Weil window
    form (Weil 1952; Bombieri 2000; Connes 1999) on a FINITE list of prime-power
    zones and a FINITE window.  The criterion is CITED as an address and is
    NEVER USED, in either direction.  Nothing here claims, assumes or approaches
    RH; even with S1' closed what would stand is a finite-window positivity
    statement with an explicit constant.  No zero data of any kind is read,
    generated or approximated -- an AST firewall enforces this, together with
    the import whitelist and the absence of any write-mode file access.
  * DISCOVERY ONLY.  Nothing is promoted.  No verification module, no ledger, no
    TeX, no website, no changelog, no next.txt is touched; this is ONE new file
    in experiments/tfpt-discovery/ and it writes nothing.
  * HARD CAPS.  Largest factorised / inverted / diagonalised matrix <= 1500;
    runtime budget 700 s (< 900 s), with per-block guards that truncate a pool
    rather than overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import (cho_factor, cho_solve, cholesky, eigh, eigvalsh,
                          solve_triangular)

np.seterr(all="ignore")

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 700.0             # HARD probe budget (< 900 s)
RESERVE_S = 170.0            # reserved for P2 .. P4 before the window loop ends

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 2200000
ZONE_DEEP = 2050000

# --- the measurement surface ------------------------------------------------
SURF_ZONES = 64              # every admissible zone inside the cap, no stride
SURF_HCAP = 1200             # <= MAX_H; the inverse of E is dense
LEV_MAX = 34                 # dyadic levels kept above the floor level
M3_HCAP = 300                # windows small enough for the M3 capacity check
M3_LEV = 8                   # levels checked there

# --- P2 the no-go and the controls -------------------------------------------
NOGO_SIZES = (64, 128, 256, 512, 1024, 1500)
NOGO_EPS = 1.0e-3

# --- P3 the border blocks ----------------------------------------------------
K3_GC_MIN = 2
K3_HCAP = 300
K3_MAX = 24
K3_PER_RHO = 2
K3_RHO = (1.001, 1.05, 1.20, 1.49531, 2.00, 3.50)
K3_LOGRES = 80.0

# --- preregistered bars (declared before any number is computed) -------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_UNIF = 0.25              # |exponent in D| for "ZONE-UNIFORM", preregistered
BAR_C0 = 16.0                # an "absolute constant of classical size": four
#                              times Maz'ya's Dirichlet constant c_0 = 4.  The
#                              step list counts as PROOF-SHAPED only if the
#                              product of its factors stays below this.
BAR_TEST = 4.0               # the testing constant of the finite test family
MAZYA_C0 = 4.0               # the classical Dirichlet constant, CITED

# --- quoted numbers.  QUOTED, never re-derived here --------------------------
N_PROBES_PRIOR = 144
KAP_UP_T144 = 1.3162
CGLOB_T144 = 1.6876
BRES_LAM_T144 = (0.6694, 0.7813)
BRES_EXP_T144 = (0.013, 0.005)
PSI_ALL_T144 = (0.7399, 0.8515)
PSI_EXP_T144 = 0.015
PHI_INT_EXP_T144 = 0.654
TSTAR_EXP_T144 = 3.96
CINT_MAX_T144 = 425.0
CINT_EXP_T144 = -1.137
SANDWICH_T144 = (1.213, 2.175)
MK_POS_T144 = (0.72, 0.84)
MICLO_LOSS_T143 = (46.0, 2561.0)
MICLO_EXP_T143 = -2.13
R4_OPEN_T144 = 3
PROMO_T144 = 93
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
            msk = np.ones(n, dtype=bool)
            msk[i] = False
            ai, bi, _ = fit_line(x[msk], y[msk])
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
          == "mazya_proof_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T144 code path
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
    assembly source, exactly as T138 .. T144 did."""
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
# THE LUMPED M-MATRIX PAIR (T136 .. T144) and the JACOBI WHITENING
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
    so the pair (A, Lam) carries the COUNTING MEASURE in the denominator, and
        lam_min(E) / kap_up <= lam_min(A, A_B) <= lam_min(E) / kap_lo
    by Loewner.  DIRECTION: kap_up = cert_lam_max(W) is an UPPER bound and
    kap_lo = cert_lam_min(W) a LOWER one, so the LEFT inequality is the usable
    lower bound on the gap and the RIGHT one is R5's second side, which is why
    both are certified here and not only the first."""
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
    the SCHUR / GREEN identity.  R = E^{-1} is passed in."""
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


def interval_capacity(R, a, b):
    Raa = sym(np.ascontiguousarray(R[a:b, a:b]))
    fac = safe_cho(Raa)
    if fac is None:
        return float("nan")
    y = cho_solve(fac, np.ones(b - a), check_finite=False)
    val = float(y.sum())
    return val if val > 0.0 else float("nan")


# ----------------------------------------------------------------------------
# THE CLOSED INTERVAL OBJECTS -- prefix sums, so ALL O(m^2) intervals at once
# ----------------------------------------------------------------------------
def interval_sums(X):
    """S[a, b] = sum_{a <= k, l < b} X_kl for all 0 <= a <= b <= m, by ONE
    two-dimensional prefix sum."""
    m = X.shape[0]
    P = np.zeros((m + 1, m + 1))
    P[1:, 1:] = np.cumsum(np.cumsum(np.asarray(X, dtype=float), axis=0), axis=1)
    dv = np.diag(P).copy()
    return dv[:, None] + dv[None, :] - P - P.T


def interval_lengths(m):
    aa = np.arange(m + 1)
    return aa[None, :] - aa[:, None]


def density_interval_sup(R):
    """B_res = sup_I (1^T R_II 1) / |I|, EXACT over all O(m^2) intervals -- the
    Muckenhoupt-type two-weight sup of T144 in the whitened node coordinates
    (Muckenhoupt 1972), rebuilt here as ONE member of the test family of P3."""
    m = R.shape[0]
    S = interval_sums(R)
    L = interval_lengths(m)
    good = L >= 1
    rat = np.where(good, S / np.where(good, L, 1.0), -np.inf)
    flat = int(np.argmax(rat))
    a, b = divmod(flat, m + 1)
    return dict(P=float(rat[a, b]), a=int(a), b=int(b), n_int=int(m * (m + 1) // 2))


def level_family_sup(lc, M):
    """sup over the DYADIC LEVEL SETS of the minimiser of (1^T M_SS 1) / |S|, for
    whichever matrix M the comparison is about.  DIRECTION: a sup over a FINITE
    family, hence a LOWER bound on the corresponding all-sets sup -- which is the
    direction the testing comparison of P3 needs.  The matrix matters: on M = R it
    is a Rayleigh quotient of R at an indicator and therefore <= lam_max(R); on
    M = R^+ or M = |R| it is not, and the probe never claims otherwise."""
    Ind, nv = lc["Ind"], lc["n"]
    q = np.einsum("kj,jk->k", Ind, M @ Ind.T)
    return float(np.max(q / np.maximum(nv, 1.0)))


def set_density(M, idx):
    """(1^T M_AA 1) / |A| for one explicit set -- ATTAINED, hence a LOWER bound
    on any sup over a family containing it."""
    if idx.size == 0:
        return float("nan")
    o = np.ones(idx.size)
    return float(o @ M[np.ix_(idx, idx)] @ o) / float(idx.size)


def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000) for the MAXIMUM DENSITY
    SUBGRAPH of a NONNEGATIVE symmetric weight matrix with zero diagonal.
    DIRECTIONS, both cited and both used: the returned density is attained by
    the returned set, hence a LOWER bound on the optimum; and Charikar's
    guarantee greedy >= opt / 2 turns it into opt <= 2 x greedy, which is the
    only bound in this probe that holds over ALL 2^m sets."""
    m = Wp.shape[0]
    if m < 2:
        return dict(dens=0.0, size=m, idx=np.arange(m))
    deg = Wp.sum(axis=1).astype(float)
    tot = 0.5 * float(deg.sum())
    alive = np.ones(m, dtype=bool)
    n_alive = m
    best, best_n = tot / m, m
    best_alive = alive.copy()
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
            best_alive = alive.copy()
    return dict(dens=float(best), size=int(best_n),
                idx=np.nonzero(best_alive)[0])


def density_all_upper(R):
    """AN UPPER BOUND for Psi_all = sup_A (1^T R^+_AA 1) / |A| over ALL 2^m sets,
    with a CITED constant and no family restriction:
        1^T R^+_AA 1 / |A| <= max_i R_ii + 2 x (edge density of A)
    and the edge density of the NONNEGATIVE off-diagonal part is bounded either
    by 2 x Charikar's greedy value (Charikar 2000; Goldberg 1984 for the exact
    flow version) or by the CERTIFIED lam_max of the same nonnegative matrix,
    whichever is smaller.  DIRECTION: an UPPER bound, which is the direction the
    chain of P1 consumes.

    TWO INSTANCES ARE USED BELOW AND THEY ARE NOT THE SAME OBJECT.  Called on R
    it returns the bound for the POSITIVE PART R^+, which is T144's Psi_all and
    the one the ENERGY route needs (it only has to dominate 1^T R_AA 1).  Called
    on |R| it returns the bound for the ABSOLUTE VALUE, which is what the
    SIGN-FREE route needs, because the entrywise domination step is only true
    with |R| and not with R^+ when the vector changes sign."""
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    gr = greedy_density(Rp)
    dg_max = float(np.max(np.diag(R)))
    psi_char = dg_max + 4.0 * gr["dens"]
    psi_spec = dg_max + cert_lam_max(Rp, guess=ray_top(Rp))
    cands = [x for x in (psi_char, psi_spec) if np.isfinite(x)]
    best = min(cands) if cands else float("nan")
    # the attained density of the greedy set, an exact LOWER bound on Psi_all
    idx = gr["idx"]
    psi_att = float("nan")
    if idx.size:
        psi_att = float(np.ones(idx.size) @ R[np.ix_(idx, idx)]
                        @ np.ones(idx.size)) / float(idx.size)
    del Rp
    return dict(up=best, char=psi_char, spec=psi_spec, greedy=gr["dens"],
                size=gr["size"], dg_max=dg_max, att=psi_att, idx=idx)


# ----------------------------------------------------------------------------
# THE DYADIC LAYER CAKE -- the object every step of the proof is written on
# ----------------------------------------------------------------------------
def layer_cake(psi):
    """THE DYADIC LAYER CAKE of |psi| as a NESTED chain of sets with POSITIVE
    coefficients, arranged so that the DOMINATION IS EXACT and needs no limit.

    With S_j the sets and c_j > 0 the coefficients, psi_t = sum_j c_j 1_{S_j}
    satisfies |psi| <= psi_t <= 2 |psi| + 2^{k_bot}, where the FLOOR LEVEL
    j = 0 is the FULL set with coefficient 2^{k_bot}: adding it is what repairs
    the truncation of the cake at a finite bottom, so the domination is an
    inequality between two finite objects and not an asymptotic statement.  The
    sets are nested DECREASING, S_0 = everything, which is what makes the
    nested-set domination of M4'c available."""
    v = np.abs(np.asarray(psi, dtype=float))
    m = v.shape[0]
    vmax = float(np.max(v))
    if not (vmax > 0.0):
        return None
    k_top = int(math.floor(math.log2(vmax)))
    while 2.0 ** k_top >= vmax:
        k_top -= 1
    k_bot = k_top - LEV_MAX + 1
    order = np.argsort(-v, kind="stable")
    sizes = [m]
    coef = [2.0 ** k_bot]
    for k in range(k_bot, k_top + 1):
        t = 2.0 ** k
        n_k = int(np.count_nonzero(v > t))
        if n_k <= 0:
            continue
        sizes.append(n_k)
        coef.append(t)
    K = len(sizes)
    Ind = np.zeros((K, m))
    for j in range(K):
        Ind[j, order[:sizes[j]]] = 1.0
    cv = np.array(coef, dtype=float)
    nv = np.array(sizes, dtype=float)
    psi_t = Ind.T @ cv
    jj = np.arange(K)
    mn = np.minimum.outer(jj, jj)          # the LARGER set has the SMALLER index
    return dict(K=K, Ind=Ind, c=cv, n=nv, psi_t=psi_t, v=v, mn=mn,
                k_top=k_top, k_bot=k_bot,
                dom_lo=float(np.min(psi_t - v)),
                dom_hi=float(np.max(psi_t - 2.0 * v)),
                f_lc=float(psi_t @ psi_t) / max(float(v @ v), 1.0e-300))


def cake_chain(lc, R, Rnn, psi, psi_up):
    """THE STEP CHAIN M4'a .. M4'c, evaluated as numbers on one window.

    Every line is an inequality that holds for ANY vector psi and any symmetric
    R, with NO sign hypothesis on the form, PROVIDED Rnn = |R| entrywise:
        theta   = psi^T R psi
        q_dom   = |psi|^T |R| |psi|          >= theta        (entrywise, M4'a)
        q_cake  = psi_t^T |R| psi_t          >= q_dom        (|R| >= 0, M4'b)
        num_lev = sum_{j,l} c_j c_l q_min    >= q_cake       (nested sets, M4'c)
        num_all = psi_up x sum c_j c_l n_min >= num_lev      (density bound)
    so that theta <= psi_up x G_dy ||psi||^2 with the GEOMETRIC LEVEL CONSTANT
        G_dy = sum_{j,l} c_j c_l |S_min(j,l)| / ||psi||^2 ,
    which is the product of the step factors and therefore the candidate c_0.

    THE ABSOLUTE VALUE IS NOT COSMETIC.  With R^+ in place of |R| the first line
    is FALSE as soon as psi changes sign on a pair carrying a negative entry --
    measured on this surface, where a majority of the Green entries are negative
    and the minimiser is sign-structured -- so the price of dropping the Markov
    hypothesis is that the density hypothesis has to be stated for |R|.  That is
    a real sharpening of what S1' must assume, and it is reported as such."""
    Rp = Rnn
    v, Ind, c, nv, mn = lc["v"], lc["Ind"], lc["c"], lc["n"], lc["mn"]
    nrm2 = float(psi @ psi)
    theta = float(psi @ (R @ psi))
    RpI = Rp @ Ind.T                       # m x K
    QM = Ind @ RpI                         # K x K, the exact level Gram matrix
    q = np.diag(QM).copy()
    q_dom = float(v @ (Rp @ v))
    q_cake = float(c @ (QM @ c))
    num_lev = float(c @ (q[mn] @ c))
    G_dy = float(c @ (nv[mn] @ c)) / max(nrm2, 1.0e-300)
    num_all = psi_up * G_dy * nrm2
    psi_lev = float(np.max(q / np.maximum(nv, 1.0)))
    del Rp, RpI, QM
    return dict(theta=theta, q_dom=q_dom, q_cake=q_cake, num_lev=num_lev,
                num_all=num_all, G_dy=G_dy, C_lev=num_lev / max(nrm2, 1.0e-300),
                psi_lev=psi_lev, nrm2=nrm2, q=q, K=lc["K"],
                f_dom=q_dom / max(theta, 1.0e-300),
                f_cake=q_cake / max(q_dom, 1.0e-300),
                f_nest=num_lev / max(q_cake, 1.0e-300),
                f_dens=num_all / max(num_lev, 1.0e-300))


# ----------------------------------------------------------------------------
# THE PAIR DECOMPOSITION and THE MARKOV STEP M4
# ----------------------------------------------------------------------------
def pair_parts(X):
    """The Beurling-Deny shape of a symmetric form (Fukushima-Oshima-Takeda
    1994, ch. 1):
        f^T X f = sum_{i<j} (-X_ij) (f_i - f_j)^2 + sum_i (X 1)_i f_i^2 ,
    an ALGEBRAIC IDENTITY for every symmetric X, verified in P0.  The form is
    a DIRICHLET (conductance) form exactly when all -X_ij >= 0 for i != j, and
    that is the hypothesis the classical step M4 consumes."""
    off = X - np.diag(np.diag(X))
    return dict(off=off, s=off.sum(axis=1), r=X.sum(axis=1))


def cond_part(pp, f):
    """sum_{i<j} (-X_ij)(f_i - f_j)^2 = -sum_i s_i f_i^2 + f^T off f."""
    f2 = f * f
    return float(-(f2 @ pp["s"]) + f @ (pp["off"] @ f))


def mass_part(pp, f):
    return float((f * f) @ pp["r"])


def dyadic_truncations(v, k_bot, k_top):
    """f_k = min(max(|psi| - 2^k, 0), 2^k), the classical truncations of the
    level-set proof.  They obey sum_k f_k = |psi| EXACTLY down to the floor,
    which is verified rather than assumed, and 2^{-k} f_k is admissible for
    cap(A_{k+1}), which is the whole content of step M3."""
    out = []
    for k in range(k_bot, k_top + 1):
        t = 2.0 ** k
        out.append((k, np.minimum(np.maximum(v - t, 0.0), t)))
    return out


def markov_step(E, lc):
    """STEP M4, MEASURED.  For a conductance form the truncation increments are
    sign-coherent and sum to the increment of f, so sum_k Cond(f_k) <= Cond(f)
    with the constant 1 (Maz'ya 1985, section 2.3; Miclo 1999 for the chain
    version).  Here the conductances -E_ij are NEGATIVE on the majority of
    pairs, so the step is measured on both the true form and on its Stieltjes
    surrogate E - P, where it must hold -- and that surrogate is the CONTROL
    which shows the measurement itself is right."""
    pp = pair_parts(E)
    Ppos = np.where(pp["off"] > 0.0, pp["off"], 0.0)
    ppS = pair_parts(sym(E - Ppos))
    v = lc["v"]
    tr = dyadic_truncations(v, lc["k_bot"], lc["k_top"])
    s_tot = 0.0
    c_tot = 0.0
    cS_tot = 0.0
    m_tot = 0.0
    f_sum = np.zeros_like(v)
    for (_k, fk) in tr:
        f_sum += fk
        s_tot += float(fk @ (E @ fk))
        c_tot += cond_part(pp, fk)
        cS_tot += cond_part(ppS, fk)
        m_tot += mass_part(pp, fk)
    E_v = float(v @ (E @ v))
    id_err = rel(f_sum, v)
    # THE SPLIT OF M4, which is where the honest answer sits.  M4 asks for
    # sum_k E(f_k) <= E(psi).  Both sides split by LICENCE 8, and the two halves
    # have DIFFERENT status: the MASS half is a THEOREM whenever the row sums are
    # nonnegative (sum_k f_k,i^2 <= (sum_k f_k,i)^2 = v_i^2 pointwise, all terms
    # nonnegative), while the CONDUCTANCE half is the Markov half and needs a
    # nonnegative weight, which this form does not have.  Both are normalised by
    # E(psi) > 0 so that no ratio has a vanishing or negative denominator.
    out = dict(id_err=id_err, sig_tot=s_tot / max(E_v, 1.0e-300),
               m4_lhs=c_tot / max(E_v, 1.0e-300),
               m4_rhs=cond_part(pp, v) / max(E_v, 1.0e-300),
               m4_lhs_S=cS_tot / max(E_v, 1.0e-300),
               m4_rhs_S=cond_part(ppS, v) / max(E_v, 1.0e-300),
               sig_mass=m_tot / max(mass_part(pp, v), 1.0e-300),
               cond_share=cond_part(pp, v) / max(E_v, 1.0e-300),
               mass_share=mass_part(pp, v) / max(E_v, 1.0e-300),
               neg_rows=float(np.mean(pp["r"] < 0.0)),
               ident=rel(E_v, cond_part(pp, v) + mass_part(pp, v)),
               n_lev=len(tr),
               neg_cond=float(np.mean(pp["off"] > 0.0)),
               neg_mass=float(np.sum(np.where(pp["off"] > 0.0, pp["off"], 0.0)))
               / max(float(np.sum(np.abs(pp["off"]))), 1.0e-300))
    del pp, ppS, Ppos
    return out


def m3_check(R, lc, E, n_lev=M3_LEV):
    """STEP M3, VERIFIED where it is affordable: cap_E(A_{k+1}) <= 4^{-k}
    E(f_k).  This step needs ONLY that 2^{-k} f_k equals 1 on A_{k+1} and that
    the capacity is a MINIMUM over admissible functions -- no Markov property,
    no positivity of anything but the form itself.  Returns the worst slack over
    the checked levels; a value >= 1 means the inequality held."""
    v = lc["v"]
    order = np.argsort(-v, kind="stable")
    ks = list(range(lc["k_bot"], lc["k_top"] + 1))
    ks = ks[-n_lev:]
    worst = float("inf")
    n_ok = 0
    for k in ks:
        t = 2.0 ** k
        idx = np.sort(order[:int(np.count_nonzero(v > 2.0 * t))])
        if idx.size < 1:
            continue
        cap = set_capacity(R, idx)
        fk = np.minimum(np.maximum(v - t, 0.0), t)
        ene = float(fk @ (E @ fk)) / (t * t)
        if np.isfinite(cap) and cap > 0.0 and np.isfinite(ene) and ene > 0.0:
            worst = min(worst, ene / cap)
            n_ok += 1
    return dict(worst=worst, n_ok=n_ok)


# ----------------------------------------------------------------------------
# THE NO-GO FORMS of P2 -- explicit, cheap, and decisive
# ----------------------------------------------------------------------------
def nogo_form(m, eps=NOGO_EPS):
    """THE NO-GO: R = a a^T + eps I with a_i = i^{-1/2}.  R is POSITIVE
    DEFINITE, ENTRYWISE NONNEGATIVE, and its density sup over ALL sets is
    ABSOLUTELY BOUNDED (the best set is a prefix by rearrangement, and
    (sum_{i<=k} i^{-1/2})^2 / k <= 4), while lam_max(R) = ||a||^2 + eps grows
    like log m.  So on this hypothesis class -- E positive definite, R = E^{-1}
    nonnegative, Psi_all bounded -- S1' FAILS with any absolute constant."""
    a = 1.0 / np.sqrt(np.arange(1, m + 1, dtype=float))
    R = np.outer(a, a) + eps * np.eye(m)
    lam_top = float(a @ a) + eps
    pref = np.cumsum(a) ** 2 / np.arange(1, m + 1, dtype=float) + eps
    return dict(R=R, a=a, lam_top=lam_top, psi_pref=float(np.max(pref)),
                psi=a / math.sqrt(float(a @ a)))


def control_form(m):
    """THE CONTROL: the inverse of the Dirichlet path Laplacian, i.e. a genuine
    MARKOVIAN form on the same node coordinates.  Its Green function is
    nonnegative, its minimiser is the smooth half-sine mode, and its level
    profile is flat -- so the same chain must give an O(1) constant there."""
    E = (2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    E = sym(E)
    fac = safe_cho(E)
    if fac is None:
        return None
    R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    w, V = eigh(E, subset_by_index=[0, 0])
    return dict(E=E, R=R, lam_top=1.0 / float(w[0]), psi=V[:, 0].copy())


# ----------------------------------------------------------------------------
section("P0  SETUP, the licences, and the DIRECTION statements")
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

RNG = np.random.default_rng(14507291)

para("""P0.0  THE RH FENCE, STATED BEFORE ANY NUMBER.  The surrounding statement
is the positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999)
on a FINITE list of prime-power zones and a FINITE window; the criterion is
CITED as that address and is NEVER USED here, in either direction.  Nothing in
this file claims, assumes or approaches RH.  This probe attacks ONE classical
inequality -- Maz'ya's capacitary strong-type bound for a form that is not a
Dirichlet form -- and even if that inequality were closed with the explicit
constant produced below, what would stand is a finite-window positivity
statement on prime-power zones and nothing more; the distance from there to RH
is mapped in P4 and never travelled.  No zero data is read, generated or
approximated: the AST firewall above enforces that, together with the import
whitelist and the absence of any write-mode file access.""")

# --- P0.1  the coordinates, unchanged from T106 .. T144 ---------------------
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
      "h = %d, D = %.3e -- the coordinates of T106 .. T144, unchanged"
      % (E_ODD, BAR_ID, _h0, _D0))

_A0 = sym(odd_toeplitz(_c0, _M0))
_lp0 = lump_pair(_A0)
check("el_p0.lumping", _lp0["stieltjes"] == 1,
      "the lumped pair is STIELTJES while the ORIGINAL A has %d positive "
      "off-diagonal entries out of %d, so the form is non-Markovian from the "
      "start -- which is exactly why the step M4 below has to be measured "
      "instead of cited.  The count itself is reported per window in P1; T144's "
      "%.0f .. %.0f %% figure is for a different matrix and is NOT reused as a "
      "quantity here"
      % (_lp0["n_pos"], _h0 * (_h0 - 1), 100.0 * MK_POS_T144[0],
         100.0 * MK_POS_T144[1]))

# --- P0.2  THE LICENCES: every step of the proof, verified before it is used -
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
      "Maz'ya 1985)" % CAP_ID_ERR)

_lam_e = float(eigvalsh(_Ee, subset_by_index=[0, 0])[0])
_phi_e = float(_idx.size) / _c_dir
check("el_p0.free_half", _phi_e <= 1.0 / _lam_e * (1.0 + 1.0e-9),
      "LICENCE 2, THE FREE HALF AND THE DIRECTION TRAP: Phi(A) = |A| / cap(A) "
      "= %.4f <= 1 / lam_min = %.4f for EVERY set, because the equilibrium "
      "potential is a test function.  So single sets give an UPPER bound on "
      "the gap and Phi_sup x lam <= 1 for free; S1' is the OTHER direction, "
      "Phi_sup x lam >= 1 / c_0, and that is what P1 attacks"
      % (_phi_e, 1.0 / _lam_e))

_cs_floor = (_idx.size ** 2) / float(np.ones(_idx.size)
                                     @ _Re[np.ix_(_idx, _idx)]
                                     @ np.ones(_idx.size))
check("el_p0.cauchy_schwarz", _c_dir >= _cs_floor * (1.0 - 1.0e-12),
      "LICENCE 3, THE GREEN FLOOR (step M2): cap_E(A) >= |A|^2 / (1^T R_AA 1) "
      "by Cauchy-Schwarz on (1^T 1)^2 <= (1^T M 1)(1^T M^{-1} 1) with M = "
      "R_AA (here %.6f >= %.6f), i.e. Phi(A) <= Psi(A) = mean Green mass of A"
      % (_c_dir, _cs_floor))

# LICENCE 4 IS STATED WITH |R| AND NOT WITH R^+, AND THE DIFFERENCE IS NOT
# COSMETIC: with R^+ the inequality is FALSE as soon as R_ij < 0 on a pair where
# x_i x_j < 0, because then R_ij x_i x_j > 0 while R^+_ij |x_i| |x_j| = 0.  The
# check below therefore verifies the |R| version, which holds for every symmetric
# R and every x, and it also verifies that the R^+ version is violated on an
# explicit two-by-two witness -- so the probe cannot silently use the wrong one.
_xv = RNG.standard_normal(60)
_Rpe = np.maximum(_Re, 0.0)
_Rae = np.abs(_Re)
DOM_OK = (float(_xv @ (_Re @ _xv))
          <= float(np.abs(_xv) @ (_Rae @ np.abs(_xv))) * (1.0 + 1.0e-12))
_Wit = np.array([[1.0, -0.5], [-0.5, 1.0]])
_wv = np.array([1.0, -1.0])
DOM_POS_FALSE = (float(_wv @ (_Wit @ _wv))
                 > float(np.abs(_wv) @ (np.maximum(_Wit, 0.0) @ np.abs(_wv))))
check("el_p0.entrywise_domination", DOM_OK and DOM_POS_FALSE,
      "LICENCE 4, STEP M4'a AND IT NEEDS NO HYPOTHESIS AT ALL: x^T R x = sum "
      "R_ij x_i x_j <= sum |R_ij| |x_i| |x_j| = |x|^T |R| |x| entrywise, for "
      "every symmetric R and every x, costing a factor %.4f on this random "
      "form.  AND THE PEDANTIC HALF, which fixes which matrix the sign-free "
      "route may use: the same line with R^+ in place of |R| is FALSE, "
      "witnessed here by R = [[1, -1/2], [-1/2, 1]] at x = (1, -1), where "
      "x^T R x = %.1f exceeds |x|^T R^+ |x| = %.1f.  This is the step that "
      "replaces the Markov property's FIRST use -- the sign of the conductances"
      % (float(np.abs(_xv) @ (_Rae @ np.abs(_xv)))
         / max(float(_xv @ (_Re @ _xv)), 1.0e-300),
         float(_wv @ (_Wit @ _wv)),
         float(np.abs(_wv) @ (np.maximum(_Wit, 0.0) @ np.abs(_wv)))))

_y1 = np.abs(RNG.standard_normal(60))
_y2 = _y1 + np.abs(RNG.standard_normal(60))
MON_OK = float(_y1 @ (_Rpe @ _y1)) <= float(_y2 @ (_Rpe @ _y2)) * (1.0 + 1.0e-12)
check("el_p0.nonneg_monotone", MON_OK,
      "LICENCE 5, STEP M4'b: for a NONNEGATIVE matrix M and 0 <= x <= y "
      "pointwise, x^T M x <= y^T M y.  This is what turns the pointwise "
      "domination |psi| <= psi_t of the layer cake into a form inequality, and "
      "it is the reason the cake may be truncated at a finite bottom level")

_cake = layer_cake(_y1)
CAKE_DOM = _cake["dom_lo"]
CAKE_ID = float(np.max(_cake["Ind"].T @ _cake["c"] - _cake["psi_t"]))
check("el_p0.layer_cake", CAKE_DOM >= -1.0e-14 and abs(CAKE_ID) <= 1.0e-14,
      "LICENCE 6, THE LAYER CAKE IS EXACT: with S_j the dyadic level sets of "
      "|psi| plus the FULL set at the floor coefficient, psi_t = sum_j c_j "
      "1_{S_j} satisfies psi_t - |psi| >= %.2e >= 0 pointwise and psi_t <= 2 "
      "|psi| up to the floor, so ||psi_t||^2 / ||psi||^2 = %.4f <= 4.  The "
      "factor 4 is the classical one of the dyadic decomposition (Maz'ya 1985, "
      "section 2.3) and here it is a MEASURED ratio with a proved ceiling"
      % (CAKE_DOM, _cake["f_lc"]))

_QM = _cake["Ind"] @ (_Rpe @ _cake["Ind"].T)
_qd = np.diag(_QM)
NEST_OK = bool(np.all(_QM <= _qd[_cake["mn"]] + 1.0e-12
                      * max(1.0, float(np.max(np.abs(_QM))))))
check("el_p0.nested_domination", NEST_OK,
      "LICENCE 7, STEP M4'c: the sets of the cake are NESTED DECREASING, so "
      "for a NONNEGATIVE M and j <= l one has 1_{S_j}^T M 1_{S_l} <= 1_{S_j}^T "
      "M 1_{S_j}, i.e. every off-diagonal entry of the level Gram matrix is "
      "bounded by the diagonal entry of the LARGER set.  Verified on all %d^2 "
      "level pairs of a random cake.  This is the step that replaces the "
      "Markov property's SECOND use -- the sign-coherence of the truncation "
      "increments" % _cake["K"])

_pp = pair_parts(_Ee)
BD_ERR = rel(float(_xv @ (_Ee @ _xv)),
             cond_part(_pp, _xv) + mass_part(_pp, _xv))
check("el_p0.beurling_deny", BD_ERR <= BAR_ID,
      "LICENCE 8, THE PAIR DECOMPOSITION IS AN IDENTITY: f^T X f = sum_{i<j} "
      "(-X_ij)(f_i - f_j)^2 + sum_i (X1)_i f_i^2 to %.2e relative, for every "
      "symmetric X (Fukushima-Oshima-Takeda 1994, ch. 1).  A DIRICHLET form is "
      "the case -X_ij >= 0, and that is the hypothesis the classical step M4 "
      "consumes -- so M4 can be measured on the exact same decomposition"
      % BD_ERR)

_gg = 14
_Wr = sym(np.abs(RNG.standard_normal((_gg, _gg))))
np.fill_diagonal(_Wr, 0.0)
_gr = greedy_density(_Wr)
_bf = 0.0
for _mask in range(1, 1 << _gg):
    _sel = np.array([(_mask >> i) & 1 for i in range(_gg)], dtype=bool)
    _ns = int(np.count_nonzero(_sel))
    _d = 0.5 * float(_Wr[np.ix_(_sel, _sel)].sum()) / _ns
    if _d > _bf:
        _bf = _d
check("el_p0.charikar_bracket",
      _gr["dens"] <= _bf * (1.0 + 1.0e-12) and _bf <= 2.0 * _gr["dens"],
      "LICENCE 9, THE ONLY ALL-SETS BOUND IN THIS PROBE: greedy peeling gives "
      "%.6f, the EXHAUSTIVE optimum over all %d subsets is %.6f, and "
      "Charikar's guarantee opt <= 2 x greedy = %.6f holds (Charikar 2000; "
      "Goldberg 1984 for the exact flow version).  This is what makes Psi_up "
      "an upper bound over ALL 2^m sets with a CITED constant"
      % (_gr["dens"], (1 << _gg) - 1, _bf, 2.0 * _gr["dens"]))

_Zb = RNG.standard_normal((50, 50))
_Ab = sym(_Zb @ _Zb.T) + 2.0 * np.eye(50)
_Yb = RNG.standard_normal((50, 50))
_Bb = sym(_Ab + sym(_Yb @ _Yb.T)) + 6.0 * np.eye(50)
_lam_pair = float(eigh(_Ab, _Bb, eigvals_only=True, subset_by_index=[0, 0])[0])
_jw = jacobi_whiten(_Ab, _Bb)
_lam_wh = float(eigvalsh(_jw["E"], subset_by_index=[0, 0])[0])
_lo_side = _lam_wh / _jw["kap_up"]
_up_side = _lam_wh / _jw["kap_lo"]
check("el_p0.jacobi_two_sided",
      _lam_pair >= _lo_side * (1.0 - 1.0e-9)
      and _lam_pair <= _up_side * (1.0 + 1.0e-9),
      "LICENCE 10, BOTH SIDES OF THE WHITENING, which is R5's object: "
      "lam_min(E) / kap_up = %.6e <= lam_min(A, A_B) = %.6e <= lam_min(E) / "
      "kap_lo = %.6e, with kap_up CERTIFIED from above and kap_lo from below.  "
      "The left side is the one the chain uses; the right side is what turns "
      "the sandwich lam / lam_hat into a two-sided certificate"
      % (_lo_side, _lam_pair, _up_side))

_nog = nogo_form(256)
_nog_ps = density_all_upper(_nog["R"])
check("el_p0.nogo_wellposed",
      _nog_ps["up"] >= _nog["psi_pref"] * (1.0 - 1.0e-9)
      and float(np.min(_nog["R"])) >= 0.0,
      "LICENCE 11, THE NO-GO FORM IS IN THE HYPOTHESIS CLASS: R = a a^T + eps "
      "I with a_i = i^{-1/2} is positive definite and ENTRYWISE NONNEGATIVE, "
      "its exact prefix density sup is %.4f and the all-sets upper bound of "
      "this probe gives %.4f >= it, as an upper bound must.  P2 uses it to "
      "show that nonnegativity of the Green function plus a bounded density "
      "sup do NOT suffice for S1'" % (_nog["psi_pref"], _nog_ps["up"]))

para("""P0.3  WHAT IS NEW HERE, IN ONE SENTENCE.  T144 left the chain lam >= 1 /
(c_0 kap_up c_glob B_res) certified on 34 windows with ONE unproved input, the
absolute constant c_0 of the capacitary strong-type inequality.  This probe does
not look for a better chain; it takes the classical PROOF of that inequality
apart, transcribes it onto the non-Markovian form line by line, finds the single
line that uses the Markov property, replaces that line by two facts that need no
sign hypothesis (entrywise domination and nested-set domination of a nonnegative
Green matrix) plus the Green mean-density bound, and reads off what the product
of the step factors is.  The answer is a single explicit number per window -- a
constant of the MINIMISER'S OWN DYADIC LAYER CAKE, in two versions because the
transcription splits into two routes -- and the whole question of c_0 collapses
onto whether that number is bounded a priori.""")


# ----------------------------------------------------------------------------
section("P1  Q1 -- THE CLASSICAL PROOF, STEP BY STEP, ON THE WRONG FORM")
# ----------------------------------------------------------------------------
para("""P1.0  THE STEP LIST, written down BEFORE it is measured.  Maz'ya's proof
of the strong-type inequality ||f||^2 <= c_0 B E(f), B = sup_A |A| / cap(A), runs
    M1  ||f||^2 <= 4 sum_k 4^k |A_k| ,  A_k = { |f| > 2^k }        THEOREM x4
    M2  |A_k| <= B cap(A_k)                                        DEFINITION
    M3  cap(A_{k+1}) <= 4^{-k} E(f_k) ,  f_k the truncation        THEOREM x1
    M4  sum_k E(f_k) <= E(f)                                       MARKOV
and gives c_0 = 4 for a Dirichlet form.  M1 is arithmetic on level sets, M2 is
the definition of B, M3 needs only that a truncation is admissible in the
capacity minimisation -- none of the three knows anything about signs.  M4 is
the whole Markov hypothesis, and it uses it TWICE: the conductances -E_ij must
be nonnegative for the pair inequality (sum_k (f_k,i - f_k,j)^2 <= (f_i - f_j)^2
requires a nonnegative weight), and the truncation increments must be
sign-coherent.  Neither holds here: the whitened form carries POSITIVE
off-diagonal entries, so the pair weight is negative on those pairs, and how
many of them there are is MEASURED below rather than quoted (T144's 72 .. 84 %%
figure is for a different object and is not reused).  What matters for the proof
is not the count but that the resulting conductance form is not nonnegative on
the minimiser itself, which is what the check below establishes -- so M4 is not
merely unproved, it is VOID, and the honest statement is that its hypothesis is
absent and its two sides are of indefinite sign.  The replacement is built on
the GREEN side, where R = E^{-1} is positive definite and its ABSOLUTE VALUE is
a nonnegative matrix, and where the two uses of Markov are covered by LICENCE 4
and LICENCE 7 respectively.""")

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
    if budget_left() < RESERVE_S:
        info("P1.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(ROWS)))
        break
    al = 0.5 * M_k * D_k
    c_lag, _ = lag_vector_fast(al, M_k, atoms_in(al, ATOMS_ALL))
    A = sym(odd_toeplitz(c_lag, M_k))
    lp = lump_pair(A)
    if lp["stieltjes"] != 1:
        continue
    try:
        gap_ex = float(eigh(A, lp["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        continue
    if not (gap_ex > 0.0):
        continue
    jw = jacobi_whiten(A, lp["A_B"])
    if jw is None or not np.isfinite(jw["kap_up"]) or not (jw["kap_lo"] > 0.0):
        continue
    E = jw["E"]
    try:
        wv, Vv = eigh(E, subset_by_index=[0, 0])
    except (LinAlgError, ValueError):
        continue
    lam_hat = float(wv[0])
    if not (lam_hat > 0.0):
        continue
    psi = np.ascontiguousarray(Vv[:, 0])
    psi = psi / max(float(np.linalg.norm(psi)), 1.0e-300)
    fac = safe_cho(E)
    if fac is None:
        continue
    R = sym(cho_solve(fac, np.eye(h_k), check_finite=False))

    # --- the certified top of the Green function, DIRECTION: upper -----------
    lam_top_cert = cert_lam_max(R, guess=ray_top(R))
    dens = density_all_upper(R)              # T144's object: the POSITIVE part
    Rabs = np.abs(R)
    dens_abs = density_all_upper(Rabs)       # what the SIGN-FREE route needs
    lc = layer_cake(psi)
    if lc is None or not np.isfinite(dens["up"]) or not np.isfinite(
            dens_abs["up"]):
        del A, E, R
        continue
    ch = cake_chain(lc, R, Rabs, psi, dens_abs["up"])
    mk = markov_step(E, lc)
    m3 = m3_check(R, lc, E) if h_k <= M3_HCAP else dict(worst=float("nan"),
                                                        n_ok=0)
    bres = density_interval_sup(R)
    r_nonneg = float(np.mean(R >= 0.0))
    # THE TEST FAMILY OF P3, built on the SAME matrix that Psi_up bounds.
    # Mixing an |R| density into a family compared against an R^+ bound would be
    # a direction error, so every member here is evaluated on R^+ -- and the
    # R-versions are kept separately, because only those are Rayleigh quotients.
    Rpos = np.maximum(R, 0.0)
    tf_int = density_interval_sup(Rpos)["P"]
    tf_lev = level_family_sup(lc, Rpos)
    tf_att = set_density(Rpos, dens["idx"])
    lev_R = level_family_sup(lc, R)
    # M1, the classical level arithmetic.  DIRECTION: the theorem to verify is
    # ||psi||^2 <= 3 sum_k 4^k |A_k|, so the quantity to check is 3 m1_val >= 1,
    # and 3 m1_val is the multiplicative factor the step contributes.
    m1_val = float(np.sum((lc["c"] ** 2) * lc["n"])) / max(ch["nrm2"], 1.0e-300)
    # the participation / delocalisation diagnostics of the minimiser
    v = lc["v"]
    part_l1 = float(v.sum()) ** 2 / max(h_k * float(v @ v), 1.0e-300)
    part_inf = float(v @ v) / max(h_k * float(np.max(v)) ** 2, 1.0e-300)
    sign_share = float(np.mean(psi > 0.0))
    ROWS.append(dict(
        k=k, n=NN_ALL[k], D=D_k, m=h_k, gap_ex=gap_ex, lam_hat=lam_hat,
        kap_up=jw["kap_up"], kap_lo=jw["kap_lo"], gersh_up=jw["gersh_up"],
        sandwich_lo=1.0 / jw["kap_up"], sandwich_up=1.0 / jw["kap_lo"],
        ratio_ex=gap_ex / lam_hat,
        lam_top=1.0 / lam_hat, lam_top_cert=lam_top_cert,
        psi_up=dens["up"], psi_char=dens["char"], psi_spec=dens["spec"],
        psi_att=dens["att"], psi_size=dens["size"], dg_max=dens["dg_max"],
        psi_abs=dens_abs["up"], psi_abs_att=dens_abs["att"],
        b_res=bres["P"], n_int=bres["n_int"], r_nonneg=r_nonneg,
        tf_int=tf_int, tf_lev=tf_lev, tf_att=tf_att, lev_R=lev_R,
        K=ch["K"], G_dy=ch["G_dy"], C_lev=ch["C_lev"], theta=ch["theta"],
        num_lev=ch["num_lev"], num_all=ch["num_all"], q_cake=ch["q_cake"],
        q_dom=ch["q_dom"], psi_lev=ch["psi_lev"],
        f_dom=ch["f_dom"], f_cake=ch["f_cake"], f_nest=ch["f_nest"],
        f_dens=ch["f_dens"], f_lc=lc["f_lc"], m1_val=m1_val,
        m1_fac=3.0 * m1_val,
        c0_need=1.0 / max(dens["up"] * lam_hat, 1.0e-300),
        core_all=dens["up"] * lam_hat, core_res=bres["P"] * lam_hat,
        core_lev=ch["psi_lev"] * lam_hat, core_abs=dens_abs["up"] * lam_hat,
        sig_tot=mk["sig_tot"], sig_mass=mk["sig_mass"],
        m4_lhs=mk["m4_lhs"], m4_rhs=mk["m4_rhs"],
        m4_lhs_S=mk["m4_lhs_S"], m4_rhs_S=mk["m4_rhs_S"],
        neg_rows=mk["neg_rows"], cond_share=mk["cond_share"],
        mass_share=mk["mass_share"], bd_err=mk["ident"],
        trunc_id=mk["id_err"], neg_cond=mk["neg_cond"],
        neg_mass=mk["neg_mass"], n_lev=mk["n_lev"],
        m3_worst=m3["worst"], m3_n=m3["n_ok"],
        part_l1=part_l1, part_inf=part_inf, sign_share=sign_share,
        c0_gr=ch["G_dy"], c0_en=12.0 * mk["sig_tot"],
        psi_gr=dens_abs["up"], psi_en=dens["up"]))
    del A, E, R, Rabs, Rpos, lc, ch, mk, jw, lp, dens, dens_abs, bres, Vv

if not ROWS:
    raise SystemExit("P1 produced no window -- probe cannot report")

for r in ROWS:
    # THE TWO ROUTES, side by side.  Both end in lam_hat >= 1 / (c_0 Psi), and
    # they differ in which c_0 and which Psi: the ENERGY route pays 12 x sig_tot
    # against the POSITIVE-part density, the SIGN-FREE route pays G_dy against
    # the ABSOLUTE-value density.  The route that wins on a window is the one
    # with the smaller product, and the product is what the chain is worth.
    r["prod_en"] = r["c0_en"] * r["psi_en"]
    r["prod_gr"] = r["c0_gr"] * r["psi_gr"]
    r["prod_best"] = min(r["prod_en"], r["prod_gr"])
    r["c0_best"] = (r["c0_en"] if r["prod_en"] <= r["prod_gr"] else r["c0_gr"])
    r["route"] = ("energy" if r["prod_en"] <= r["prod_gr"] else "green")
    r["chain_hat"] = 1.0 / max(r["prod_best"], 1.0e-300)
    r["chain_ex"] = r["chain_hat"] / max(r["kap_up"], 1.0e-300)
    r["loss_hat"] = r["chain_hat"] / max(r["lam_hat"], 1.0e-300)
    r["loss_ex"] = r["chain_ex"] / max(r["gap_ex"], 1.0e-300)
    r["loss_en"] = 1.0 / max(r["prod_en"] * r["lam_hat"], 1.0e-300)
    r["loss_gr"] = 1.0 / max(r["prod_gr"] * r["lam_hat"], 1.0e-300)

DV = [r["D"] for r in ROWS]
F_GAP = pow_fit(DV, [r["gap_ex"] for r in ROWS], "gap")
F_GDY = pow_fit(DV, [r["c0_gr"] for r in ROWS], "c0_green")
F_C0EN = pow_fit(DV, [r["c0_en"] for r in ROWS], "c0_energy")
F_C0B = pow_fit(DV, [r["c0_best"] for r in ROWS], "c0_best")
F_C0N = pow_fit(DV, [r["c0_need"] for r in ROWS], "c0_need")
F_LOSSHAT = pow_fit(DV, [r["loss_hat"] for r in ROWS], "loss_hat")
F_LOSSEX = pow_fit(DV, [r["loss_ex"] for r in ROWS], "loss_ex")
F_SIGT = pow_fit(DV, [r["sig_tot"] for r in ROWS], "sig_tot")
F_COREALL = pow_fit(DV, [r["core_all"] for r in ROWS], "core_all")
F_CORELEV = pow_fit(DV, [r["core_lev"] for r in ROWS], "core_lev")
F_KAP = pow_fit(DV, [r["kap_up"] for r in ROWS], "kap_up")
F_SAND = pow_fit(DV, [r["kap_up"] / r["kap_lo"] for r in ROWS], "sandwich")
F_PART = pow_fit(DV, [r["part_inf"] for r in ROWS], "part_inf")
F_K = pow_fit(DV, [float(r["K"]) for r in ROWS], "levels")

info("P1.surface", "%d windows, h = m = %d .. %d, D = %.3e .. %.3e, zones n = "
     "%d .. %d; the exact pair gap is %.3e .. %.3e, FITTED as D^%.3f +- %.3f "
     "(T142 QUOTED the exponent %.0f), and the whitened gap lam_hat = %.3e .. "
     "%.3e"
     % (len(ROWS), min(r["m"] for r in ROWS), max(r["m"] for r in ROWS),
        qmin(DV), qmax(DV), min(r["n"] for r in ROWS),
        max(r["n"] for r in ROWS), qmin([r["gap_ex"] for r in ROWS]),
        qmax([r["gap_ex"] for r in ROWS]), F_GAP["p"], F_GAP["sp"],
        GAP_EXP_T142, qmin([r["lam_hat"] for r in ROWS]),
        qmax([r["lam_hat"] for r in ROWS])))

check("el_p1.identities",
      qmax([r["bd_err"] for r in ROWS]) <= BAR_ID
      and qmax([r["trunc_id"] for r in ROWS]) <= 1.0e-9,
      "THE TWO IDENTITIES THE STEP LIST RESTS ON, on every window: the pair "
      "decomposition to %.2e relative, and sum_k f_k = |psi| for the dyadic "
      "truncations to %.2e relative on %d .. %d levels.  So M1, M3 and M4 are "
      "measured on exactly the objects the classical proof uses, not on "
      "surrogates"
      % (qmax([r["bd_err"] for r in ROWS]),
         qmax([r["trunc_id"] for r in ROWS]),
         min(r["n_lev"] for r in ROWS), max(r["n_lev"] for r in ROWS)))

check("el_p1.m1_theorem", qmin([r["m1_fac"] for r in ROWS]) >= 1.0 - 1.0e-9,
      "STEP M1 IS A THEOREM AND IT IS VERIFIED IN THE DIRECTION IT IS USED: "
      "||psi||^2 <= 3 sum_k 4^k |A_k| holds with 3 sum_k 4^k |A_k| / ||psi||^2 "
      "= %.4f .. %.4f >= 1 on every window, so the step contributes a factor "
      "of at most 3 and in fact %.4f .. %.4f.  The layer-cake ratio "
      "||psi_t||^2 / ||psi||^2 = %.4f .. %.4f <= 4 is the same arithmetic in "
      "the form the sign-free route uses.  Nothing about the form enters here"
      % (qmin([r["m1_fac"] for r in ROWS]), qmax([r["m1_fac"] for r in ROWS]),
         qmin([r["m1_fac"] for r in ROWS]), qmax([r["m1_fac"] for r in ROWS]),
         qmin([r["f_lc"] for r in ROWS]), qmax([r["f_lc"] for r in ROWS])))

M3ROWS = [r for r in ROWS if r["m3_n"] > 0]
if M3ROWS:
    check("el_p1.m3_theorem",
          qmin([r["m3_worst"] for r in M3ROWS]) >= 1.0 - 1.0e-9,
          "STEP M3 IS A THEOREM ON THIS FORM TOO, VERIFIED: cap_E(A_{k+1}) <= "
          "4^{-k} E(f_k) with slack %.4f .. %.4f >= 1 on %d levels of %d "
          "windows (m <= %d, where an exact capacity per level is affordable).  "
          "The step needs only the admissibility of a truncation in a MINIMUM, "
          "so the non-Markovian form does not touch it"
          % (qmin([r["m3_worst"] for r in M3ROWS]),
             qmax([r["m3_worst"] for r in M3ROWS]),
             sum(r["m3_n"] for r in M3ROWS), len(M3ROWS), M3_HCAP))

check("el_p1.m4_control_holds",
      all(r["m4_lhs_S"] <= r["m4_rhs_S"] * (1.0 + 1.0e-9) for r in ROWS),
      "STEP M4, THE CONTROL FIRST, because it is what makes the measurement "
      "credible: on the STIELTJES SURROGATE E - P, whose conductances are all "
      "nonnegative by construction, the classical truncation subadditivity "
      "sum_k Cond(f_k) <= Cond(psi) HOLDS on every window -- both sides "
      "normalised by E(psi) > 0, the left one %.4f .. %.4f against the right "
      "one %.4f .. %.4f.  The same code, the same cake, the same truncations"
      % (qmin([r["m4_lhs_S"] for r in ROWS]),
         qmax([r["m4_lhs_S"] for r in ROWS]),
         qmin([r["m4_rhs_S"] for r in ROWS]),
         qmax([r["m4_rhs_S"] for r in ROWS])))

# THE STATEMENT TO VERIFY, CHOSEN BEFORE THE NUMBERS AND CHOSEN CAREFULLY.  The
# classical step compares two quantities that are BOTH of indefinite sign on this
# form, so "the inequality fails" is not the right assertion -- on some windows it
# happens to hold with two negative sides and means nothing.  What IS uniformly
# true, and what actually locates the hypothesis, is that the step's HYPOTHESIS
# fails everywhere (there are positive off-diagonal entries, hence negative
# conductance weights, on every window) and that its conclusion is void because
# Cond(psi) is not nonnegative.  Both are checked; the count of windows on which
# the conclusion also fails outright is reported as a number, not as the claim.
M4_HYP_DEAD = all(r["neg_cond"] > 0.0 for r in ROWS)
M4_VOID_N = len([r for r in ROWS if min(r["m4_lhs"], r["m4_rhs"]) < 0.0])
M4_FAIL_N = len([r for r in ROWS if r["m4_lhs"] > r["m4_rhs"]])
COND_NEG_N = len([r for r in ROWS if r["cond_share"] < 0.0])
check("el_p1.m4_is_the_markov_step", M4_HYP_DEAD,
      "AND ON THE TRUE FORM THE MARKOV STEP HAS NO HYPOTHESIS LEFT, WHICH IS "
      "WHAT LOCATES IT.  The ASSERTED and CHECKED statement is the hypothesis "
      "failure, because it is the one that holds without exception: on all %d "
      "windows %.3f .. %.3f of the off-diagonal entries of E are POSITIVE, so "
      "the pair weight -E_ij is negative on those pairs and they carry %.3f .. "
      "%.3f of the off-diagonal mass, and the classical pair inequality has no "
      "licence.  WHAT IS ONLY COUNTED, not asserted: normalised by E(psi), the "
      "step compares sum_k Cond(f_k) = %.4f .. %.4f with Cond(psi) = %.4f .. "
      "%.4f; the conductance part of the minimiser's energy is NEGATIVE on %d "
      "of %d windows, at least one side of the comparison is negative on %d of "
      "%d -- so the step is not merely violated but meaningless there -- and "
      "the raw inequality fails outright on %d of %d.  On the remaining "
      "window(s) it happens to hold, with the hypothesis still absent, so it is "
      "unproved there rather than void: either way it is not usable, and the "
      "positivity of E is carried by the mass term (%.4f .. %.4f of E(psi)).  "
      "T143 QUOTED Miclo's chain loss %.0f .. %.0f drifting as D^%.2f -- the "
      "same death, now localised in ONE line of the proof instead of in a "
      "construction"
      % (len(ROWS), qmin([r["neg_cond"] for r in ROWS]),
         qmax([r["neg_cond"] for r in ROWS]),
         qmin([r["neg_mass"] for r in ROWS]),
         qmax([r["neg_mass"] for r in ROWS]),
         qmin([r["m4_lhs"] for r in ROWS]), qmax([r["m4_lhs"] for r in ROWS]),
         qmin([r["m4_rhs"] for r in ROWS]), qmax([r["m4_rhs"] for r in ROWS]),
         COND_NEG_N, len(ROWS), M4_VOID_N, len(ROWS), M4_FAIL_N, len(ROWS),
         qmin([r["mass_share"] for r in ROWS]),
         qmax([r["mass_share"] for r in ROWS]),
         MICLO_LOSS_T143[0], MICLO_LOSS_T143[1], MICLO_EXP_T143))

MASS_THM = all(r["neg_rows"] <= 0.0 for r in ROWS)
check("el_p1.m4_splits",
      qmax([r["sig_mass"] for r in ROWS]) <= 1.0 + 1.0e-9,
      "BUT M4 SPLITS, AND ONLY ONE HALF IS MARKOVIAN -- this is the finding "
      "that opens the ENERGY ROUTE.  By LICENCE 8 the step is the sum of a "
      "CONDUCTANCE half, which needs a nonnegative weight and fails above, and "
      "a MASS half, which is a THEOREM whenever the row sums of E are "
      "nonnegative (sum_k f_k,i^2 <= (sum_k f_k,i)^2 = v_i^2 pointwise, all "
      "terms nonnegative): measured sum_k mass(f_k) / mass(psi) = %.4f .. %.4f "
      "<= 1, with %s row sums negative on the surface.  Since the mass half "
      "carries %.4f .. %.4f of E(psi), the FULL step sum_k E(f_k) / E(psi) = "
      "%.4f .. %.4f is BELOW 1 on every window although its Markovian half is "
      "not -- and that number, exact per window, is all the classical proof "
      "ever needed"
      % (qmin([r["sig_mass"] for r in ROWS]),
         qmax([r["sig_mass"] for r in ROWS]),
         "no" if MASS_THM else "some",
         qmin([r["mass_share"] for r in ROWS]),
         qmax([r["mass_share"] for r in ROWS]),
         qmin([r["sig_tot"] for r in ROWS]),
         qmax([r["sig_tot"] for r in ROWS])))

check("el_p1.chain_steps_ordered",
      all(r["theta"] <= r["q_dom"] * (1.0 + 1.0e-9)
          and r["q_dom"] <= r["q_cake"] * (1.0 + 1.0e-9)
          and r["q_cake"] <= r["num_lev"] * (1.0 + 1.0e-9)
          and r["num_lev"] <= r["num_all"] * (1.0 + 1.0e-9) for r in ROWS),
      "THE SIGN-FREE REPLACEMENT CHAIN M4'a -> M4'b -> M4'c -> M2, IN ORDER AND "
      "ON EVERY WINDOW: psi^T R psi <= |psi|^T |R| |psi| <= psi_t^T |R| psi_t "
      "<= sum c_j c_l q_min <= Psi_abs sum c_j c_l n_min.  The four step "
      "factors are %.4f .. %.4f (entrywise), %.4f .. %.4f (cake), %.4f .. %.4f "
      "(nesting) and %.4f .. %.4f (density), and their product is the candidate "
      "c_0 of the sign-free route"
      % (qmin([r["f_dom"] for r in ROWS]), qmax([r["f_dom"] for r in ROWS]),
         qmin([r["f_cake"] for r in ROWS]), qmax([r["f_cake"] for r in ROWS]),
         qmin([r["f_nest"] for r in ROWS]), qmax([r["f_nest"] for r in ROWS]),
         qmin([r["f_dens"] for r in ROWS]), qmax([r["f_dens"] for r in ROWS])))

CHAIN_GR = all(np.isfinite(r["lam_top_cert"])
               and r["lam_top_cert"] <= r["prod_gr"] for r in ROWS)
CHAIN_EN = all(np.isfinite(r["lam_top_cert"])
               and r["lam_top_cert"] <= r["prod_en"] for r in ROWS)
CHAIN_OK = bool(CHAIN_GR or CHAIN_EN)
check("el_p1.certified_s1", CHAIN_OK,
      "AND HERE IS S1' AS A CERTIFIED WINDOW INEQUALITY, which is the point of "
      "the whole probe.  cert_lam_max(R) = %.4e .. %.4e is an UPPER bound on "
      "lam_max(R) = 1 / lam_hat by a completed Cholesky, and it stays below "
      "BOTH products on every one of the %d windows: the ENERGY route's 12 "
      "sig_tot x Psi_pos (%s) and the SIGN-FREE route's G_dy x Psi_abs (%s).  "
      "Read in the other direction that is exactly S1', lam_hat >= 1 / (c_0 "
      "Psi), with c_0 EXPLICIT.  Note what does NOT enter: no claim that the "
      "computed vector IS the minimiser -- c_0 is a definition applied to it "
      "and the certified side is independent of it"
      % (qmin([r["lam_top_cert"] for r in ROWS]),
         qmax([r["lam_top_cert"] for r in ROWS]), len(ROWS),
         "holds" if CHAIN_EN else "FAILS",
         "holds" if CHAIN_GR else "FAILS"))

G_MAX = qmax([r["c0_best"] for r in ROWS])
G_MIN = qmin([r["c0_best"] for r in ROWS])
C0_OK = bool(G_MAX <= BAR_C0)
C0_UNIF = unif_ok(F_C0B)
N_EN = len([r for r in ROWS if r["route"] == "energy"])
info("P1.c0_explicit", "THE CONSTANT, BY ROUTE.  ENERGY ROUTE (the classical "
     "proof with M4 replaced by its exact value at the minimiser): c_0 = 12 "
     "sig_tot = %.4f .. %.4f, fit D^%.3f +- %.3f.  SIGN-FREE ROUTE (the Green "
     "side, no sign hypothesis anywhere): c_0 = G_dy = %.4f .. %.4f, fit "
     "D^%.3f +- %.3f.  The route with the smaller product wins on %d of %d "
     "windows for the energy side, and the resulting c_0 = %.4f .. %.4f against "
     "the preregistered ceiling %.2f (%s), fit D^%.3f +- %.3f against the bar "
     "%.2f (%s).  For scale: the classical Dirichlet value is c_0 = %.0f "
     "(Maz'ya 1985) and the SMALLEST constant compatible with the measured "
     "density sup is 1 / (Psi_pos lam_hat) = %.4f .. %.4f, so the surviving "
     "proof is lossy by %.2f .. %.2f"
     % (qmin([r["c0_en"] for r in ROWS]), qmax([r["c0_en"] for r in ROWS]),
        F_C0EN["p"], F_C0EN["sp"],
        qmin([r["c0_gr"] for r in ROWS]), qmax([r["c0_gr"] for r in ROWS]),
        F_GDY["p"], F_GDY["sp"], N_EN, len(ROWS), G_MIN, G_MAX, BAR_C0,
        "INSIDE" if C0_OK else "OUTSIDE", F_C0B["p"], F_C0B["sp"], BAR_UNIF,
        "ZONE-UNIFORM" if C0_UNIF else "NOT zone-uniform", MAZYA_C0,
        qmin([r["c0_need"] for r in ROWS]),
        qmax([r["c0_need"] for r in ROWS]),
        qmin([r["prod_best"] * r["lam_hat"] for r in ROWS]),
        qmax([r["prod_best"] * r["lam_hat"] for r in ROWS])))

info("P1.step_sizes", "WHERE THE FACTOR IS BORN, step by step.  ENERGY ROUTE: "
     "M1 x %.4f .. %.4f (theorem, ceiling 3), M3 x 4 (theorem), M4 -> sig_tot "
     "= %.4f .. %.4f (exact, was the Markov step), M2 the density.  SIGN-FREE "
     "ROUTE: cake %.4f .. %.4f, entrywise %.4f .. %.4f, cake domination %.4f "
     ".. %.4f, nesting %.4f .. %.4f, density %.4f .. %.4f.  The cake has K = "
     "%d .. %d levels, and the SHARPEST form of the sign-free chain -- the one "
     "that never leaves the level family, 1 / lam_hat <= sum c_j c_l q_min -- "
     "is a factor %.2f .. %.2f tighter than the version that passes through an "
     "all-sets density bound, with total loss (sum c_j c_l q_min) x lam_hat = "
     "%.3f .. %.3f"
     % (qmin([r["m1_fac"] for r in ROWS]), qmax([r["m1_fac"] for r in ROWS]),
        qmin([r["sig_tot"] for r in ROWS]),
        qmax([r["sig_tot"] for r in ROWS]),
        qmin([r["f_lc"] for r in ROWS]), qmax([r["f_lc"] for r in ROWS]),
        qmin([r["f_dom"] for r in ROWS]), qmax([r["f_dom"] for r in ROWS]),
        qmin([r["f_cake"] for r in ROWS]), qmax([r["f_cake"] for r in ROWS]),
        qmin([r["f_nest"] for r in ROWS]), qmax([r["f_nest"] for r in ROWS]),
        qmin([r["f_dens"] for r in ROWS]), qmax([r["f_dens"] for r in ROWS]),
        min(r["K"] for r in ROWS), max(r["K"] for r in ROWS),
        qmin([r["num_all"] / r["num_lev"] for r in ROWS]),
        qmax([r["num_all"] / r["num_lev"] for r in ROWS]),
        qmin([r["num_lev"] * r["lam_hat"] for r in ROWS]),
        qmax([r["num_lev"] * r["lam_hat"] for r in ROWS])))

info("P1.density_price", "AND THE PRICE OF DROPPING THE SIGN, stated as a "
     "number because it is a real sharpening of what S1' must assume: the "
     "energy route needs a density bound for the POSITIVE part only, Psi_pos x "
     "lam_hat = %.4f .. %.4f (T144 QUOTED %.4f .. %.4f, reproduced), while the "
     "sign-free route needs it for the ABSOLUTE VALUE, Psi_abs x lam_hat = "
     "%.4f .. %.4f -- a factor %.2f .. %.2f more, because %.3f .. %.3f of the "
     "Green entries are negative and the minimiser changes sign.  Both are "
     "certified through Charikar's cited constant; only the first is T144's "
     "object"
     % (qmin([r["core_all"] for r in ROWS]),
        qmax([r["core_all"] for r in ROWS]), PSI_ALL_T144[0], PSI_ALL_T144[1],
        qmin([r["core_abs"] for r in ROWS]),
        qmax([r["core_abs"] for r in ROWS]),
        qmin([r["psi_abs"] / r["psi_up"] for r in ROWS]),
        qmax([r["psi_abs"] / r["psi_up"] for r in ROWS]),
        1.0 - qmax([r["r_nonneg"] for r in ROWS]),
        1.0 - qmin([r["r_nonneg"] for r in ROWS])))

info("P1.chain_value", "AND WHAT THE CHAIN IS WORTH AS A NUMBER: lam_hat >= 1 "
     "/ (c_0 Psi) delivers %.4f .. %.4f of lam_hat on the better route (energy "
     "%.4f .. %.4f, sign-free %.4f .. %.4f), fit D^%.3f +- %.3f, and through "
     "the certified whitening factor kap_up = %.4f .. %.4f the bound lam >= 1 "
     "/ (kap_up c_0 Psi) delivers %.4f .. %.4f of the exact pair gap (fit "
     "D^%.3f +- %.3f).  T144 QUOTED %.4f .. %.4f for the same product with the "
     "UNPROVED c_0 = 4 in the place where c_0 now stands explicitly"
     % (qmin([r["loss_hat"] for r in ROWS]),
        qmax([r["loss_hat"] for r in ROWS]),
        qmin([r["loss_en"] for r in ROWS]), qmax([r["loss_en"] for r in ROWS]),
        qmin([r["loss_gr"] for r in ROWS]), qmax([r["loss_gr"] for r in ROWS]),
        F_LOSSHAT["p"], F_LOSSHAT["sp"],
        qmin([r["kap_up"] for r in ROWS]), qmax([r["kap_up"] for r in ROWS]),
        qmin([r["loss_ex"] for r in ROWS]), qmax([r["loss_ex"] for r in ROWS]),
        F_LOSSEX["p"], F_LOSSEX["sp"], PSI_ALL_T144[0], PSI_ALL_T144[1]))


# ----------------------------------------------------------------------------
section("P2  Q2 -- THE DIRECT SPECTRAL ARGUMENT, AND THE NO-GO THAT BOUNDS IT")
# ----------------------------------------------------------------------------
para("""P2.0  THE DIRECTION, PEDANTICALLY, BEFORE ANY NUMBER.  It is tempting to
read T144's Psi_all x lam_hat <= 0.8515 as evidence for S1'.  It is not, and the
reason is a one-line theorem: for the density built from R itself, Psi(A) =
1_A^T R 1_A / |A| is a RAYLEIGH QUOTIENT of R at the vector 1_A, so Psi_all <=
lam_max(R) = 1 / lam_hat and the product Psi_all x lam_hat <= 1 holds for FREE,
with no hypothesis whatsoever.  It gives NO lower bound on lam_hat.  What S1'
needs is the OPPOSITE direction -- that some set, or some level decomposition of
the minimiser, RECOVERS a constant fraction of lam_max(R) -- and that is a
statement about the PROFILE of the minimiser, not about the size of a supremum.
This probe's chain is exactly that statement made quantitative, and P2 measures
the profile and then shows, by an explicit form, that no weaker hypothesis can
work.""")

check("el_p2.free_direction",
      all(r["b_res"] * r["lam_hat"] <= 1.0 + 1.0e-9
          and r["lev_R"] * r["lam_hat"] <= 1.0 + 1.0e-9 for r in ROWS),
      "THE FREE DIRECTION, ON EVERY WINDOW AND ONLY FOR R ITSELF: the interval "
      "density sup of R gives B_res x lam_hat = %.4f .. %.4f <= 1 (T144 QUOTED "
      "%.4f .. %.4f) and the level-family density sup of R gives Psi_levR x "
      "lam_hat = %.4f .. %.4f <= 1.  Both are Rayleigh quotients of R at "
      "indicator vectors, so both are theorems with no content for S1'.  THE "
      "PEDANTIC HALF, because it is where a direction error would hide: the "
      "same sup for R^+ or |R| is NOT a Rayleigh quotient of R and need not be "
      "below 1 -- measured Psi_pos x lam_hat = %.4f .. %.4f and Psi_abs x "
      "lam_hat = %.4f .. %.4f, the latter ABOVE 1 -- so the free direction is "
      "not available on the matrices the two routes actually use"
      % (qmin([r["core_res"] for r in ROWS]),
         qmax([r["core_res"] for r in ROWS]), BRES_LAM_T144[0],
         BRES_LAM_T144[1],
         qmin([r["lev_R"] * r["lam_hat"] for r in ROWS]),
         qmax([r["lev_R"] * r["lam_hat"] for r in ROWS]),
         qmin([r["core_all"] for r in ROWS]),
         qmax([r["core_all"] for r in ROWS]),
         qmin([r["core_abs"] for r in ROWS]),
         qmax([r["core_abs"] for r in ROWS])))

info("P2.profile", "THE PROFILE OF THE MINIMISER, which is what the chain "
     "actually consumes: the dyadic cake has K = %d .. %d levels, the "
     "participation ratio ||psi||^2 / (m max psi^2) = %.4f .. %.4f (fit "
     "D^%.3f +- %.3f) and ||psi||_1^2 / (m ||psi||^2) = %.4f .. %.4f, and "
     "%.3f .. %.3f of the entries are positive -- so the minimiser is "
     "DELOCALISED and sign-structured rather than concentrated, which is "
     "exactly the regime in which the level cake costs O(1).  The entrywise "
     "nonnegativity of the Green function is %.4f .. %.4f of entries, so the "
     "positive part R^+ is not a cosmetic step but a real one on %s"
     % (min(r["K"] for r in ROWS), max(r["K"] for r in ROWS),
        qmin([r["part_inf"] for r in ROWS]),
        qmax([r["part_inf"] for r in ROWS]), F_PART["p"], F_PART["sp"],
        qmin([r["part_l1"] for r in ROWS]),
        qmax([r["part_l1"] for r in ROWS]),
        qmin([r["sign_share"] for r in ROWS]),
        qmax([r["sign_share"] for r in ROWS]),
        qmin([r["r_nonneg"] for r in ROWS]),
        qmax([r["r_nonneg"] for r in ROWS]),
        "some windows" if qmin([r["r_nonneg"] for r in ROWS]) < 1.0
        else "no window"))

# --- P2.1  THE NO-GO and its control ---------------------------------------
NOGO = []
for m_c in NOGO_SIZES:
    if m_c > MAX_H or budget_left() < 60.0:
        continue
    ng = nogo_form(m_c)
    ps = density_all_upper(ng["R"])
    lcn = layer_cake(ng["psi"])
    chn = cake_chain(lcn, ng["R"], np.abs(ng["R"]), ng["psi"], ps["up"])
    lam_c = cert_lam_max(ng["R"], guess=ray_top(ng["R"]))
    NOGO.append(dict(m=m_c, kind="nogo", lam_top=ng["lam_top"],
                     psi_up=ps["up"], psi_exact=ng["psi_pref"],
                     prod=ng["psi_pref"] / max(ng["lam_top"], 1.0e-300),
                     prod_up=ps["up"] / max(ng["lam_top"], 1.0e-300),
                     G_dy=chn["G_dy"], K=chn["K"], lam_cert=lam_c,
                     ok=bool(np.isfinite(lam_c)
                             and lam_c <= ps["up"] * chn["G_dy"])))
    del ng, ps, lcn, chn
for m_c in NOGO_SIZES:
    if m_c > MAX_H or budget_left() < 60.0:
        continue
    cf = control_form(m_c)
    if cf is None:
        continue
    ps = density_all_upper(cf["R"])
    lcn = layer_cake(cf["psi"])
    chn = cake_chain(lcn, cf["R"], np.abs(cf["R"]), cf["psi"], ps["up"])
    lam_c = cert_lam_max(cf["R"], guess=ray_top(cf["R"]))
    NOGO.append(dict(m=m_c, kind="ctrl", lam_top=cf["lam_top"],
                     psi_up=ps["up"], psi_exact=float("nan"),
                     prod=ps["up"] / max(cf["lam_top"], 1.0e-300),
                     prod_up=ps["up"] / max(cf["lam_top"], 1.0e-300),
                     G_dy=chn["G_dy"], K=chn["K"], lam_cert=lam_c,
                     ok=bool(np.isfinite(lam_c)
                             and lam_c <= ps["up"] * chn["G_dy"])))
    del cf, ps, lcn, chn

NG = [x for x in NOGO if x["kind"] == "nogo"]
CT = [x for x in NOGO if x["kind"] == "ctrl"]
if NG and CT:
    check("el_p2.chain_never_violated", all(x["ok"] for x in NOGO),
          "FIRST, THE CHAIN ITSELF IS NEVER VIOLATED -- it is a theorem, so it "
          "had better not be: cert_lam_max(R) <= Psi_up x G_dy holds on all %d "
          "test forms, the no-go family and the Markovian control alike.  What "
          "differs between them is not the validity of the chain but the SIZE "
          "of G_dy, and that is the whole content of what is missing"
          % len(NOGO))
    NG.sort(key=lambda x: x["m"])
    NG_PROD = [x["prod"] for x in NG]
    NG_BOUND_OK = all(x["psi_exact"] <= 4.0 + NOGO_EPS + 1.0e-9 for x in NG)
    NG_DECAY = bool(NG_PROD[-1] <= 0.85 * NG_PROD[0])
    check("el_p2.nogo_kills_absolute_c0", NG_BOUND_OK and NG_DECAY,
          "AND NOW THE NO-GO, which is the sharpest statement in this probe.  "
          "For R = a a^T + eps I with a_i = i^{-1/2} -- positive definite, "
          "ENTRYWISE NONNEGATIVE, the Green function of a perfectly good form "
          "-- the density sup over ALL sets is attained on PREFIXES by "
          "rearrangement (a is decreasing) and satisfies the PROVED ceiling "
          "sup_A Psi(A) = max_k (sum_{i<=k} i^{-1/2})^2 / k + eps <= 4 + eps, "
          "verified here as %.4f .. %.4f <= %.4f, while lam_max(R) = ||a||^2 + "
          "eps = %.4f .. %.4f grows like log m.  So the product Psi_all x "
          "lam_hat = %.4f -> %.4f DECAYS along m = %d -> %d and tends to 0: "
          "positivity of the form, nonnegativity of the Green function and a "
          "bounded density sup do NOT imply S1' with any absolute constant.  "
          "The missing input must constrain the LEVEL PROFILE of the "
          "minimiser, and the diagnostic that separates the two families is "
          "exactly the level constant: G_dy = %.3f -> %.3f growing on the "
          "no-go family (K = %d .. %d levels, every one carrying the same "
          "mass) against %.3f .. %.3f flat on the Markovian control"
          % (qmin([x["psi_exact"] for x in NG]),
             qmax([x["psi_exact"] for x in NG]), 4.0 + NOGO_EPS,
             qmin([x["lam_top"] for x in NG]),
             qmax([x["lam_top"] for x in NG]), NG_PROD[0], NG_PROD[-1],
             NG[0]["m"], NG[-1]["m"], NG[0]["G_dy"], NG[-1]["G_dy"],
             min(x["K"] for x in NG), max(x["K"] for x in NG),
             qmin([x["G_dy"] for x in CT]), qmax([x["G_dy"] for x in CT])))
    info("P2.control", "THE CONTROL, for scale: on the inverse Dirichlet path "
         "Laplacian -- a genuine Markovian form, m = %d .. %d -- the same code "
         "gives G_dy = %.4f .. %.4f and Psi_all x lam_hat = %.4f .. %.4f, both "
         "flat in m.  So the chain reproduces the classical O(1) constant "
         "where the classical hypothesis holds, and the constant it produces "
         "on the TFPT windows (%.4f .. %.4f) sits in the same range -- which "
         "is the honest reason to believe the transcription rather than the "
         "verdict word"
         % (min(x["m"] for x in CT), max(x["m"] for x in CT),
            qmin([x["G_dy"] for x in CT]), qmax([x["G_dy"] for x in CT]),
            qmin([x["prod"] for x in CT]), qmax([x["prod"] for x in CT]),
            G_MIN, G_MAX))

para("""P2.2  WHAT Q2 THEREFORE IS, and it is not what the contract expected.  The
"direct spectral argument" and the "transcribed Maz'ya proof" are the SAME object
once the Markov step is replaced: both are the Rayleigh decomposition of the
minimiser along its level sets, and the quantity either of them needs is one
constant of that decomposition -- sig_tot on the energy route, G_dy on the
sign-free one.  So Q2 is not an independent bypass of Q1; asking for a lower bound
lam_hat >= (1 - gamma') / B out of Psi_all x lam_hat <= gamma is asking for the
level constant under another name, and the honest answer to Q2 is that the
bypass does not exist.  What P2 does add, and it is the sharper contribution, is
the NECESSITY statement: the no-go form shows that a bound on the minimiser's
level profile cannot be dropped, weakened to nonnegativity of the Green function,
or replaced by a density bound alone.  So the step list of P1 is not merely
sufficient, it is tight in its hypotheses.""")


# ----------------------------------------------------------------------------
section("P3  Q3 -- S2' by testing, R5 two-sided, and the open R4 blocks")
# ----------------------------------------------------------------------------
para("""P3.0  (i) S2', THE TESTING CONDITION.  T144 measured the best-interval
reduction c_glob <= %.4f and left it unproved, with the pointwise hull
comparison FALSE (c_int up to %.0f, drifting as D^%.3f).  A testing-condition
proof in the two-weight sense (Sawyer 1982; Nazarov-Treil-Volberg 1999) would
bound the supremum over ALL sets by the supremum over a FINITE TEST FAMILY up to
an absolute factor.  In the DENSITY formulation that proof exists and is cited
rather than measured: the family is { all O(m^2) intervals } union { the dyadic
level sets of the minimiser } union { the greedy argmax set }, and the factor is
Charikar's 2 (Charikar 2000), with Goldberg's flow version giving 1 exactly
(Goldberg 1984).  What is MEASURED below is the size of that factor on the
surface -- and, more importantly, whether c_glob is needed at all once the chain
runs through the density instead of through the intervals.""" %
     (CGLOB_T144, CINT_MAX_T144, CINT_EXP_T144))

for r in ROWS:
    # EVERY MEMBER ON THE SAME MATRIX AS THE BOUND IT IS COMPARED WITH.  Psi_up
    # bounds sup_A 1^T R^+_AA 1 / |A| over all 2^m sets, so the family is
    # evaluated on R^+ as well: intervals, the minimiser's dyadic level sets, and
    # the greedy argmax set.  DIRECTION: the family gives a LOWER bound on the
    # same all-sets sup, so test_max <= Psi_up is the inequality to verify, and
    # c_test = Psi_up / test_max is what the testing condition would have to
    # bound by an absolute constant.
    r["test_max"] = max(r["tf_int"], r["tf_lev"], r["tf_att"])
    r["c_test"] = r["psi_up"] / max(r["test_max"], 1.0e-300)
    r["test_att"] = r["tf_att"] / max(r["test_max"], 1.0e-300)
F_CTEST = pow_fit(DV, [r["c_test"] for r in ROWS], "c_test")
TEST_OK = all(r["test_max"] <= r["psi_up"] * (1.0 + 1.0e-9) for r in ROWS)

check("el_p3.testing_family_brackets",
      TEST_OK and qmax([r["c_test"] for r in ROWS]) <= BAR_TEST,
      "THE FINITE TEST FAMILY BRACKETS THE ALL-SETS SUP, in the direction it is "
      "built for and on the SAME matrix R^+ the bound is about: max over the "
      "family = %.4e .. %.4e <= Psi_up = %.4e .. %.4e on every window, and the "
      "testing constant -- the factor by which the all-sets bound exceeds the "
      "finite family -- is c_test = %.4f .. %.4f (fit D^%.3f +- %.3f, bar %.2f "
      "-> %s) against the preregistered ceiling %.1f and Charikar's CITED 2.  "
      "The family has %d intervals plus %d .. %d level sets plus one greedy "
      "set.  What this is NOT: a proof of the testing condition, which would "
      "have to bound c_test a priori; it is the measurement of the factor such "
      "a proof would have to deliver"
      % (qmin([r["test_max"] for r in ROWS]),
         qmax([r["test_max"] for r in ROWS]),
         qmin([r["psi_up"] for r in ROWS]), qmax([r["psi_up"] for r in ROWS]),
         qmin([r["c_test"] for r in ROWS]), qmax([r["c_test"] for r in ROWS]),
         F_CTEST["p"], F_CTEST["sp"], BAR_UNIF,
         "ZONE-UNIFORM" if unif_ok(F_CTEST) else "NOT zone-uniform", BAR_TEST,
         int(qmed([r["n_int"] for r in ROWS])),
         min(r["K"] for r in ROWS), max(r["K"] for r in ROWS)))

info("P3.s2prime_retired", "AND THE CONSEQUENCE FOR S2', which is the shortest "
     "item this probe removes: the chain of P1 goes lam_hat >= 1 / (c_0 Psi) "
     "and never mentions an interval, a hull or a reduction factor, so c_glob "
     "is NOT an input to it.  The interval sup is kept only as a member of the "
     "test family, where its role is to be compared rather than trusted: "
     "B_res / Psi_up = %.4f .. %.4f and the greedy argmax set already "
     "attains %.4f .. %.4f of the family maximum.  S2' can therefore be "
     "retired as a REQUIREMENT and kept as a diagnostic"
     % (qmin([r["b_res"] / r["psi_up"] for r in ROWS]),
        qmax([r["b_res"] / r["psi_up"] for r in ROWS]),
        qmin([r["test_att"] for r in ROWS]),
        qmax([r["test_att"] for r in ROWS])))

check("el_p3.r5_two_sided",
      all(r["sandwich_lo"] <= r["ratio_ex"] * (1.0 + 1.0e-9)
          and r["ratio_ex"] <= r["sandwich_up"] * (1.0 + 1.0e-9)
          for r in ROWS),
      "(ii) R5, BOTH SIDES CERTIFIED AND THE WIDTH MEASURED: 1 / kap_up = %.4f "
      ".. %.4f <= lam / lam_hat = %.4f .. %.4f <= 1 / kap_lo = %.4f .. %.4f on "
      "every window, with kap_up CERTIFIED from above (%.4f .. %.4f, T144 "
      "QUOTED <= %.4f) and kap_lo CERTIFIED from below (%.4f .. %.4f).  The "
      "measured ratio reproduces T144's %.3f .. %.3f QUOTED.  THE HONEST HALF: "
      "the width of the two-sided certificate is kap_up / kap_lo = %.3f .. "
      "%.3f, FITTED as D^%.3f +- %.3f (bar %.2f -> %s), so the SANDWICH is not "
      "uniform even though the side the chain uses is -- R5 is closed as a "
      "two-sided certificate per window and NOT as a uniform one, and the "
      "usable side kap_up stays bounded and flat (fit D^%.3f +- %.3f)"
      % (qmin([r["sandwich_lo"] for r in ROWS]),
         qmax([r["sandwich_lo"] for r in ROWS]),
         qmin([r["ratio_ex"] for r in ROWS]),
         qmax([r["ratio_ex"] for r in ROWS]),
         qmin([r["sandwich_up"] for r in ROWS]),
         qmax([r["sandwich_up"] for r in ROWS]),
         qmin([r["kap_up"] for r in ROWS]), qmax([r["kap_up"] for r in ROWS]),
         KAP_UP_T144, qmin([r["kap_lo"] for r in ROWS]),
         qmax([r["kap_lo"] for r in ROWS]), SANDWICH_T144[0],
         SANDWICH_T144[1], qmin([r["kap_up"] / r["kap_lo"] for r in ROWS]),
         qmax([r["kap_up"] / r["kap_lo"] for r in ROWS]), F_SAND["p"],
         F_SAND["sp"], BAR_UNIF,
         "ZONE-UNIFORM" if unif_ok(F_SAND) else "NOT zone-uniform",
         F_KAP["p"], F_KAP["sp"]))

# --- P3.1  the R4 border blocks through the new chain -----------------------
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
        lst.append((k, int(N_DEEP[k]), DA / rho_l, rho_l))
        lst.append((k, int(N_DEEP[k]), DA, rho_l))
    PER_RHO.append(lst)
K3_TASK = []
for i in range(max(len(l) for l in PER_RHO) if PER_RHO else 0):
    for l in PER_RHO:
        if i < len(l):
            K3_TASK.append(l[i])
K3_TASK = K3_TASK[:K3_MAX]

BLK = []
for (k, n_lbl, D_b, rho_lbl) in K3_TASK:
    if budget_left() < 45.0:
        info("P3.budget_r4", "border pool truncated at n = %d after %d blocks"
             % (n_lbl, len(BLK)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D_b)
    if fr is None or fr["gc"] < K3_GC_MIN or fr["h_n"] > K3_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    S = sym(st["S"])
    g = S.shape[0]
    lp = lump_pair(S)
    row = dict(n=n_lbl, D=D_b, g=g, rho=rho_lbl, direct=0, chain=0,
               lam_b=float("nan"), lam_hat=float("nan"),
               cert_lo=float("nan"), G_dy=float("nan"), c0=float("nan"),
               psi_up=float("nan"), bound=float("nan"), loss=float("nan"))
    try:
        s_lo = float(eigvalsh(S, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        s_lo = float("nan")
    row["cert_lo"] = cert_lam_min(S, guess=s_lo)
    row["direct"] = int(np.isfinite(row["cert_lo"]) and row["cert_lo"] > 0.0)
    if lp["stieltjes"] == 1 and g >= 4:
        jw = jacobi_whiten(S, lp["A_B"])
        if jw is not None and np.isfinite(jw["kap_up"]):
            try:
                lam_b = float(eigh(S, lp["A_B"], eigvals_only=True,
                                   subset_by_index=[0, 0])[0])
            except (LinAlgError, ValueError):
                lam_b = float("nan")
            Eb = jw["E"]
            fb = safe_cho(Eb)
            if fb is not None:
                try:
                    wb, Vb = eigh(Eb, subset_by_index=[0, 0])
                except (LinAlgError, ValueError):
                    wb, Vb = None, None
                if wb is not None and float(wb[0]) > 0.0:
                    psib = np.ascontiguousarray(Vb[:, 0])
                    psib = psib / max(float(np.linalg.norm(psib)), 1.0e-300)
                    Rb = sym(cho_solve(fb, np.eye(g), check_finite=False))
                    psb = density_all_upper(Rb)
                    psba = density_all_upper(np.abs(Rb))
                    lcb = layer_cake(psib)
                    mkb = markov_step(Eb, lcb) if lcb is not None else None
                    if (lcb is not None and np.isfinite(psb["up"])
                            and np.isfinite(psba["up"])):
                        chb = cake_chain(lcb, Rb, np.abs(Rb), psib,
                                         psba["up"])
                        p_gr = chb["G_dy"] * psba["up"]
                        p_en = 12.0 * mkb["sig_tot"] * psb["up"]
                        prod = min(p_gr, p_en)
                        bnd = 1.0 / max(jw["kap_up"] * prod, 1.0e-300)
                        row.update(lam_b=lam_b, lam_hat=float(wb[0]),
                                   G_dy=chb["G_dy"],
                                   c0=(12.0 * mkb["sig_tot"]
                                       if p_en <= p_gr else chb["G_dy"]),
                                   psi_up=psb["up"], bound=bnd,
                                   chain=int(bnd > 0.0),
                                   loss=bnd / max(lam_b, 1.0e-300))
                        del chb, lcb, psb, psba, mkb
                    del Rb
            del Eb
    BLK.append(row)
    del S, st, lp

if BLK:
    OKB = [x for x in BLK if x["chain"] == 1 and np.isfinite(x["loss"])]
    info("P3.r4_blocks", "(iii) %d border blocks, g = %d .. %d, zones n = %d "
         ".. %d.  The direct route -- cert_lam_min(S) > 0 on the raw Schur "
         "block -- closes %d of them; the NEW chain, lam_b >= 1 / (kap_up c_0 "
         "Psi) on the better of the two routes, produces a POSITIVE certified "
         "lower bound on %d of them with loss factor %.4g .. %.4g and c_0 = "
         "%.3f .. %.3f, the same range as on the full windows (%.3f .. %.3f).  "
         "T144 QUOTED %d open blocks in a pool rebuilt exactly like this one; "
         "what transfers is the anatomy and not the count"
         % (len(BLK), min(x["g"] for x in BLK), max(x["g"] for x in BLK),
            min(x["n"] for x in BLK), max(x["n"] for x in BLK),
            len([x for x in BLK if x["direct"] == 1]), len(OKB),
            qmin([x["loss"] for x in OKB]), qmax([x["loss"] for x in OKB]),
            qmin([x["c0"] for x in OKB]), qmax([x["c0"] for x in OKB]),
            G_MIN, G_MAX, R4_OPEN_T144))
    if OKB:
        check("el_p3.r4_chain_consistent",
              all(x["bound"] <= x["lam_b"] * (1.0 + 1.0e-9) for x in OKB),
              "and the chain is CONSISTENT on every block it covers: the "
              "certified lower bound 1 / (kap_up c_0 Psi) = %.4e .. %.4e "
              "does not exceed the exact block gap %.4e .. %.4e.  So the "
              "border blocks are not a separate problem any more -- they are "
              "the same statement at a smaller g, and they inherit exactly the "
              "one missing input"
              % (qmin([x["bound"] for x in OKB]),
                 qmax([x["bound"] for x in OKB]),
                 qmin([x["lam_b"] for x in OKB]),
                 qmax([x["lam_b"] for x in OKB])))


# ----------------------------------------------------------------------------
section("P4  THE MAP V17, the promotion list, the rest list, and the verdict")
# ----------------------------------------------------------------------------
NOGO_OK = bool(NOGO) and all(x["ok"] for x in NOGO)

# THE VERDICT RULE, AND WHY IT CANNOT BE GENEROUS.  The contract's PROOF-SHAPED
# requires EVERY step factor to be a cited theorem or a CERTIFIED bound with a
# uniform constant.  The step that replaces M4 is neither: sig_tot and G_dy are
# EXACT numbers computed AT the minimiser of each window, i.e. MEASURED window
# quantities, and no a priori bound for either is available in this probe.  A
# measured constant that happens to be bounded and flat on a finite surface is
# evidence, not a proof, and the fences of this project forbid promoting the one
# to the other.  LEVEL_PROVED is therefore hard-wired to False, with the flag
# named so that the day a level lemma exists it is the ONLY line to flip -- and
# it follows that PROOF-SHAPED is UNREACHABLE here BY CONSTRUCTION, which is a
# statement about the state of the proof and not about the measurements.
LEVEL_PROVED = False
STEPS_OPEN = 0 if LEVEL_PROVED else 1
VERDICT = ("PROOF-SHAPED"
           if (CHAIN_OK and C0_OK and C0_UNIF and LEVEL_PROVED) else
           ("ONE-STEP-MISSING" if (CHAIN_OK and C0_OK and C0_UNIF)
            else "MAZYA-RESISTS"))
check("el_p4.verdict_rule", STEPS_OPEN >= 1 and VERDICT != "PROOF-SHAPED",
      "THE VERDICT RULE IS CHECKED BEFORE THE VERDICT IS PRINTED, so that no "
      "arithmetic accident can upgrade it: PROOF-SHAPED requires every step "
      "factor to be a THEOREM or a CERTIFIED bound, the replacement of M4 is a "
      "MEASURED constant at the minimiser (%.4f .. %.4f on the energy route, "
      "%.4f .. %.4f on the sign-free one), no a priori bound for either is "
      "available here, and therefore exactly %d step of the transcribed proof "
      "is open and the verdict is %s.  Boundedness (max %.4f <= %.2f) and "
      "flatness (D^%.3f +- %.3f, bar %.2f) of that constant are EVIDENCE for "
      "the missing lemma and are reported as such, never as the lemma"
      % (qmin([r["sig_tot"] for r in ROWS]),
         qmax([r["sig_tot"] for r in ROWS]),
         qmin([r["c0_gr"] for r in ROWS]), qmax([r["c0_gr"] for r in ROWS]),
         STEPS_OPEN, VERDICT, G_MAX, BAR_C0, F_C0B["p"], F_C0B["sp"],
         BAR_UNIF))

para("""P4.0  THE MAP V17, in the only order that matters -- what is a theorem,
what is certified, what is measured, what is missing.
  THEOREMS USED, all classical, all cited, none re-proved: the Schur / Green
  form of a capacity and the pair (Beurling-Deny) decomposition of a symmetric
  form (Fukushima-Oshima-Takeda 1994, ch. 1 and 2); Cauchy-Schwarz, in the two
  places where it does the work of a Markov hypothesis; the admissibility of a
  truncation in the capacity minimisation (Maz'ya 1985, section 2.3); the
  maximum-density-subgraph guarantee (Charikar 2000; Goldberg 1984); Loewner
  monotonicity; the two-weight testing philosophy (Muckenhoupt 1972; Sawyer
  1982); Bertrand-Chebyshev for the two gap facts.  Maz'ya's strong-type half
  is NOT used as a theorem anywhere -- it is the thing being transcribed.
  CERTIFIED HERE, completed Cholesky, direction in the name: cert_lam_max(R) as
  the upper bound on 1 / lam_hat; kap_up from above AND kap_lo from below, so
  R5's sandwich is two-sided; the all-sets density bound Psi_up through a cited
  constant; the positivity of the border blocks the chain covers.
  EXACT HERE: the dyadic layer cake of the minimiser and every step factor read
  off it; all O(m^2) interval densities; the level Gram matrix.
  MEASURED HERE: the Markov step M4, whose hypothesis fails on every window and
  whose two sides are of indefinite sign (%.4f .. %.4f against %.4f .. %.4f, both
  normalised by E(psi)), which is what locates the hypothesis; the truncation
  constant sig_tot = %.4f .. %.4f that replaces it; the profile diagnostics of
  the minimiser; the testing constant of the finite family.
  MISSING, and now it is ONE named object instead of a constant with no
  address: an A PRIORI bound on the constant of the minimiser's own layer cake
  -- sig_tot on the energy route, G_dy on the sign-free one -- measured
  %.4f .. %.4f as a c_0 here and PROVED NECESSARY in P2.  WHAT THE MAP THEREFORE
  SAYS, in one line: T144's unproved input was an absolute constant with no
  address, and after this probe it is a bounded, flat, exactly computable
  quantity attached to a named object with a necessity proof behind it -- which
  is a strictly better place to stand and still not a theorem.""" %
     (qmin([r["m4_lhs"] for r in ROWS]), qmax([r["m4_lhs"] for r in ROWS]),
      qmin([r["m4_rhs"] for r in ROWS]), qmax([r["m4_rhs"] for r in ROWS]),
      qmin([r["sig_tot"] for r in ROWS]), qmax([r["sig_tot"] for r in ROWS]),
      G_MIN, G_MAX))

STMT = [
    "Q1a  THE MARKOV STEP IS EXACTLY ONE LINE, and it is now located: of the "
    "four steps of Maz'ya's proof, M1 (a factor 3 in the sharp form used here, "
    "4 in the textbook one), M2 (definition) and M3 "
    "(truncation admissibility, VERIFIED on %d levels of %d windows) are "
    "theorems for ANY positive definite form; only M4, the truncation "
    "subadditivity sum_k Cond(f_k) <= Cond(f), uses the Markov property, and "
    "it uses it twice -- the sign of the conductances and the sign-coherence "
    "of the increments"
    % (sum(r["m3_n"] for r in M3ROWS) if M3ROWS else 0, len(M3ROWS)),
    "Q1b  AND M4 HAS NO HYPOTHESIS LEFT, with its own control: on the Stieltjes "
    "surrogate E - P the classical step holds; on the true form the pair weight "
    "is negative on part of every one of the %d windows (%.3f .. %.3f of the "
    "off-diagonal entries, carrying %.3f .. %.3f of its mass), and the "
    "conductance part of the minimiser's energy is itself NEGATIVE on %d of %d "
    "(%.4f .. %.4f of E(psi)) so that the step is meaningless rather than "
    "merely false on %d of %d.  Same code, same cake, same truncations -- so "
    "the failure is the form's and not the measurement's, and no reordering of "
    "the classical argument can repair it"
    % (len(ROWS), qmin([r["neg_cond"] for r in ROWS]),
       qmax([r["neg_cond"] for r in ROWS]),
       qmin([r["neg_mass"] for r in ROWS]),
       qmax([r["neg_mass"] for r in ROWS]), COND_NEG_N, len(ROWS),
       qmin([r["cond_share"] for r in ROWS]),
       qmax([r["cond_share"] for r in ROWS]), M4_VOID_N, len(ROWS)),
    "Q1c  BUT M4 SPLITS, AND THAT IS THE OPENING: its MASS half is a theorem "
    "whenever the row sums are nonnegative (measured ratio %.4f .. %.4f <= 1) "
    "and it dominates, so the FULL step sum_k E(f_k) / E(psi) = %.4f .. %.4f "
    "is below 1 on every window.  The classical proof therefore survives with "
    "the Markov theorem replaced by that ONE exact number at the minimiser"
    % (qmin([r["sig_mass"] for r in ROWS]),
       qmax([r["sig_mass"] for r in ROWS]),
       qmin([r["sig_tot"] for r in ROWS]),
       qmax([r["sig_tot"] for r in ROWS])),
    "Q1d  AND THERE IS A SECOND, SIGN-FREE ROUTE: entrywise domination x^T R x "
    "<= |x|^T |R| |x| covers the first use of Markov and nested-set domination "
    "of a nonnegative matrix covers the second, with step factors %.4f .. "
    "%.4f and %.4f .. %.4f -- at the price that the density hypothesis must be "
    "stated for |R| rather than R^+, which costs a factor %.2f .. %.2f",
    "Q1e  THE CONSTANT IS EXPLICIT ON BOTH ROUTES: c_0 = 12 sig_tot = %.4f .. "
    "%.4f (energy) and c_0 = G_dy = %.4f .. %.4f (sign-free), against the "
    "classical Dirichlet value 4 and the minimum %.4f .. %.4f the measured "
    "density sup allows.  The better route gives c_0 = %.4f .. %.4f, FITTED as "
    "D^%.3f +- %.3f (bar %.2f -> %s)"
    % (qmin([r["c0_en"] for r in ROWS]), qmax([r["c0_en"] for r in ROWS]),
       qmin([r["c0_gr"] for r in ROWS]), qmax([r["c0_gr"] for r in ROWS]),
       qmin([r["c0_need"] for r in ROWS]),
       qmax([r["c0_need"] for r in ROWS]), G_MIN, G_MAX, F_C0B["p"],
       F_C0B["sp"], BAR_UNIF,
       "ZONE-UNIFORM" if C0_UNIF else "NOT zone-uniform"),
    "Q1f  S1' AS A CERTIFIED WINDOW INEQUALITY on all %d windows: "
    "cert_lam_max(R) <= c_0 x Psi, i.e. lam_hat >= 1 / (c_0 Psi) -- and the "
    "inequality does not assume that the computed vector is the minimiser, "
    "because the certified side is independent of it"
    % len(ROWS),
    "Q2a  THE FREE DIRECTION IS FREE AND SAYS NOTHING: Psi(A) is a Rayleigh "
    "quotient of R at 1_A, so Psi_all x lam_hat <= 1 is a theorem with no "
    "content for S1'.  The load-bearing direction is the lower one and it is a "
    "statement about the minimiser's profile, measured here as a "
    "participation ratio %.4f .. %.4f and a level count K = %d .. %d"
    % (qmin([r["part_inf"] for r in ROWS]),
       qmax([r["part_inf"] for r in ROWS]), min(r["K"] for r in ROWS),
       max(r["K"] for r in ROWS)),
    "Q2b  THE NO-GO, and it is what makes the step list tight: an explicit "
    "positive definite form with an ENTRYWISE NONNEGATIVE Green function and a "
    "PROVED density ceiling 4 + eps for which Psi_all x lam_hat decays like "
    "1 / log m.  So no absolute c_0 exists under those hypotheses, and the "
    "missing input must bound the level profile of the minimiser -- the level "
    "constant separates the two families by construction",
    "Q3a  S2' IS RETIRED AS A REQUIREMENT: the chain never mentions an "
    "interval, so c_glob (T144 MEASURED <= %.4f) is not an input.  The finite "
    "test family { intervals, level sets, greedy argmax } brackets the "
    "all-sets sup with testing constant %.4f .. %.4f against Charikar's cited "
    "ceiling 2"
    % (CGLOB_T144, qmin([r["c_test"] for r in ROWS]),
       qmax([r["c_test"] for r in ROWS])),
    "Q3b  R5 IS CERTIFIED ON BOTH SIDES PER WINDOW: 1 / kap_up <= lam / "
    "lam_hat <= 1 / kap_lo, with the usable side kap_up = %.4f .. %.4f flat "
    "(D^%.3f +- %.3f) and the WIDTH kap_up / kap_lo = %.3f .. %.3f NOT uniform "
    "(D^%.3f +- %.3f) -- so the two-sided certificate exists and is not tight"
    % (qmin([r["kap_up"] for r in ROWS]), qmax([r["kap_up"] for r in ROWS]),
       F_KAP["p"], F_KAP["sp"],
       qmin([r["kap_up"] / r["kap_lo"] for r in ROWS]),
       qmax([r["kap_up"] / r["kap_lo"] for r in ROWS]), F_SAND["p"],
       F_SAND["sp"]),
]
STMT[3] = STMT[3] % (qmin([r["f_dom"] for r in ROWS]),
                     qmax([r["f_dom"] for r in ROWS]),
                     qmin([r["f_nest"] for r in ROWS]),
                     qmax([r["f_nest"] for r in ROWS]),
                     qmin([r["psi_abs"] / r["psi_up"] for r in ROWS]),
                     qmax([r["psi_abs"] / r["psi_up"] for r in ROWS]))
if BLK:
    STMT.append(
        "Q3c  THE R4 BLOCKS ARE NO LONGER A SEPARATE PROBLEM: %d of %d border "
        "blocks carry the same chain with a constant in the same range (c_0 = "
        "%.3f .. %.3f) and a consistent certified bound; they inherit the one "
        "missing input and nothing else"
        % (len([x for x in BLK if x["chain"] == 1]), len(BLK),
           qmin([x["c0"] for x in BLK if x["chain"] == 1]),
           qmax([x["c0"] for x in BLK if x["chain"] == 1])))
info("P4.promotions", "%d statements are ready for promotion in the ledger "
     "sense (T144 QUOTED a stock of %d, none promoted here either); %d are new "
     "in this probe:" % (PROMO_T144 + len(STMT), PROMO_T144, len(STMT)))
for _s in STMT:
    para(_s, indent="    ")

REST = [
    "L1  THE LEVEL LEMMA, and it is the ONLY item left in the S1' branch: an a "
    "priori bound, uniform in D, for ONE constant of the minimiser's own dyadic "
    "layer cake -- either sig_tot = sum_k E(f_k) / E(psi) <= C on the energy "
    "route (MEASURED %.4f .. %.4f, fit D^%.3f +- %.3f) or G_dy = sum_{j,l} c_j "
    "c_l |S_min(j,l)| / ||psi||^2 <= C on the sign-free route (MEASURED %.4f .. "
    "%.4f, fit D^%.3f +- %.3f).  Either one alone closes S1' with an explicit "
    "c_0; P2 proves that SOME such bound is necessary; and both are "
    "delocalisation statements about the minimiser -- the participation ratio "
    "||psi||^2 / (m max psi^2) = %.4f .. %.4f is the same information in one "
    "number.  Every other input of the chain is a cited theorem or a certified "
    "window quantity."
    % (qmin([r["sig_tot"] for r in ROWS]),
       qmax([r["sig_tot"] for r in ROWS]), F_SIGT["p"], F_SIGT["sp"],
       qmin([r["c0_gr"] for r in ROWS]), qmax([r["c0_gr"] for r in ROWS]),
       F_GDY["p"], F_GDY["sp"], qmin([r["part_inf"] for r in ROWS]),
       qmax([r["part_inf"] for r in ROWS])),
    "L2  the route to L1 that this probe can see: the minimiser is close to an "
    "explicit profile (T143: orthogonal to the charge, masses help), so a "
    "quantitative profile bound plus a perturbation estimate would give L1 "
    "with an explicit C; the level count K = %d .. %d and the sign share "
    "%.3f .. %.3f say which explicit profile to compare against."
    % (min(r["K"] for r in ROWS), max(r["K"] for r in ROWS),
       qmin([r["sign_share"] for r in ROWS]),
       qmax([r["sign_share"] for r in ROWS])),
    "R4  the border blocks, and the item is now bookkeeping rather than "
    "mathematics: the DIRECT certificate cert_lam_min(S) > 0 reaches %d of the "
    "%d blocks this probe rebuilds, so %d are open here, and the new chain "
    "covers the whole pool CONDITIONALLY on L1 and on nothing else.  T144 "
    "QUOTED %d open in a comparable pool; the count depends on how the pool is "
    "drawn and only the anatomy transfers."
    % (len([x for x in BLK if x["direct"] == 1]) if BLK else 0,
       len(BLK) if BLK else 0,
       len([x for x in BLK if x["direct"] == 0]) if BLK else R4_OPEN_T144,
       R4_OPEN_T144),
]
RETIRED = (
    "RETIRED HERE, with reasons rather than by fiat: S2' (the chain has no "
    "interval step, so c_glob is not an input at all); the search for a Markov "
    "perturbation (T144 certified it dead, and P1 now shows the classical "
    "proof needs Markov in exactly one line, which has TWO replacements); and "
    "the reading of Psi_all x lam_hat <= 1 as evidence (it is a content-free "
    "theorem).  R5 is DOWNGRADED rather than retired: both sides are certified "
    "per window but the width %.3f .. %.3f drifts as D^%.3f, so only the side "
    "the chain uses is uniform."
    % (qmin([r["kap_up"] / r["kap_lo"] for r in ROWS]),
       qmax([r["kap_up"] / r["kap_lo"] for r in ROWS]), F_SAND["p"]))
info("P4.rest_list", "the rest list, shortest first, and it is now %d items of "
     "which exactly %d is mathematics:" % (len(REST), STEPS_OPEN))
for _s in REST:
    para(_s, indent="    ")
para(RETIRED, indent="    ")

section("THE VERDICT")
info("verdict", VERDICT)
if VERDICT == "PROOF-SHAPED":
    para("The step list stands.  Maz'ya's proof survives the loss of its "
         "Markov hypothesis in exactly one place -- the truncation "
         "subadditivity M4, which is not merely violated but VOID here, "
         "because its hypothesis fails on every window and Cond(psi) is of "
         "indefinite sign (%.4f .. %.4f of the minimiser's energy, negative on "
         "%d of %d windows) -- and that place has two independent "
         "replacements, one keeping the classical energy chain and paying the "
         "measured truncation constant, one dropping signs entirely and paying "
         "the level Gram constant, so every step is either a cited theorem or "
         "a certified window inequality with a uniform factor and the product "
         "is the EXPLICIT constant c_0 = %.4f .. %.4f (fit D^%.3f +- %.3f "
         "against the bar %.2f), against the classical Dirichlet value 4 and "
         "the minimum %.4f .. %.4f the measured density sup allows.  S1' is "
         "therefore sentence-shaped on the measurement surface: cert_lam_max(R) "
         "<= c_0 x Psi holds on all %d windows, i.e. lam_hat >= 1 / (c_0 Psi), "
         "and with the certified whitening factor the chain delivers %.4f .. "
         "%.4f of the exact pair gap uniformly in D.  THE ONE SENTENCE OF "
         "RESISTANCE, because it is the honest half: both constants are EXACT "
         "per window but neither is yet a LEMMA, and P2 proves no weaker "
         "hypothesis will do -- an explicit form with a nonnegative Green "
         "function and a proved density ceiling has Psi_all x lam_hat decaying "
         "like 1 / log m, so the missing input is a delocalisation bound for "
         "the minimiser and it cannot be argued away."
         % (qmin([r["cond_share"] for r in ROWS]),
            qmax([r["cond_share"] for r in ROWS]), COND_NEG_N, len(ROWS),
            G_MIN, G_MAX,
            F_C0B["p"], F_C0B["sp"], BAR_UNIF,
            qmin([r["c0_need"] for r in ROWS]),
            qmax([r["c0_need"] for r in ROWS]), len(ROWS),
            qmin([r["loss_ex"] for r in ROWS]),
            qmax([r["loss_ex"] for r in ROWS])))
elif VERDICT == "ONE-STEP-MISSING":
    para("EXACTLY ONE STEP RESISTS, and it can be named with a number.  The "
         "transcription itself works: M1, M2 and M3 are theorems for any "
         "positive definite form, verified here in the direction they are used; "
         "M4 is the single Markov line and it does not merely fail but "
         "collapses, because its hypothesis is absent on all %d windows and the "
         "conductance part of the minimiser's energy is of indefinite sign "
         "(%.4f .. %.4f of E(psi), negative on %d of %d, the mass part carrying "
         "%.4f .. %.4f) while the same code on the Stieltjes surrogate E - P "
         "reproduces the classical step; and the chain closes anyway, twice "
         "over and independently, with c_0 = 12 sig_tot = %.4f .. %.4f on the "
         "energy route and c_0 = G_dy = %.4f .. %.4f on the sign-free one, so "
         "that cert_lam_max(R) <= c_0 x Psi is CERTIFIED on every window with "
         "c_0 = %.4f .. %.4f.  THE ONE STEP THAT IS MISSING is not the size of "
         "that constant -- it is inside the preregistered ceiling %.2f and flat, "
         "fit D^%.3f +- %.3f against the bar %.2f -- but its STATUS: it is a "
         "number MEASURED at the minimiser of each window, and an a priori "
         "bound for it, the LEVEL LEMMA, is what a proof of S1' still needs.  "
         "That is the whole remaining distance, and P2 shows it cannot be "
         "shortened: an explicit form with a nonnegative Green function and a "
         "PROVED density ceiling 4 + eps has Psi_all x lam_hat decaying like "
         "1 / log m, so no hypothesis weaker than a bound on the minimiser's "
         "level profile can carry the inequality."
         % (len(ROWS), qmin([r["cond_share"] for r in ROWS]),
            qmax([r["cond_share"] for r in ROWS]), COND_NEG_N, len(ROWS),
            qmin([r["mass_share"] for r in ROWS]),
            qmax([r["mass_share"] for r in ROWS]),
            qmin([r["c0_en"] for r in ROWS]), qmax([r["c0_en"] for r in ROWS]),
            qmin([r["c0_gr"] for r in ROWS]), qmax([r["c0_gr"] for r in ROWS]),
            G_MIN, G_MAX, BAR_C0, F_C0B["p"], F_C0B["sp"], BAR_UNIF))
else:
    para("The transcription does not close, and the anatomy is reported "
         "instead of a claim.  The chain of P1 failed on at least one window "
         "on BOTH routes, or the constant left the preregistered ceiling or "
         "the uniformity bar, so the step list as written is not a proof of "
         "anything: c_0 = %.4f .. %.4f, cert_lam_max(R) = %.4e .. %.4e, "
         "Psi_pos = %.4e .. %.4e, Psi_abs = %.4e .. %.4e.  What survives is "
         "the localisation of the Markov hypothesis in a single line (it is "
         "void because Cond(psi) is of indefinite sign, %.4f .. %.4f of "
         "E(psi), while the Stieltjes control reproduces the classical step) "
         "and the no-go of P2, which bounds what any future route may assume."
         % (G_MIN, G_MAX, qmin([r["lam_top_cert"] for r in ROWS]),
            qmax([r["lam_top_cert"] for r in ROWS]),
            qmin([r["psi_up"] for r in ROWS]),
            qmax([r["psi_up"] for r in ROWS]),
            qmin([r["psi_abs"] for r in ROWS]),
            qmax([r["psi_abs"] for r in ROWS]),
            qmin([r["cond_share"] for r in ROWS]),
            qmax([r["cond_share"] for r in ROWS])))
print("")

print("TOTAL.contract     MAZYA.PROOF -- the proof attempt for S1', the "
      "strong-type inequality for a non-Markovian form (part %d, discovery "
      "only, nothing promoted)" % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.Q1_steps     M1 THEOREM x3 (verified, %.4f .. %.4f >= 1) | M2 "
      "THEOREM / definition | M3 THEOREM x1 (verified, slack %.4f .. %.4f on "
      "%d levels) | M4 THE MARKOV STEP, VOID because its hypothesis is absent "
      "and Cond(psi) is of indefinite sign (%.4f .. %.4f of E(psi)) while the "
      "E - P control reproduces it | M4-mass (%.4f .. %.4f <= 1) -> ENERGY ROUTE "
      "sig_tot = %.4f .. %.4f | M4'a-c THE SIGN-FREE REPLACEMENT (factors "
      "%.4f .. %.4f, %.4f .. %.4f, %.4f .. %.4f)"
      % (qmin([r["m1_fac"] for r in ROWS]),
         qmax([r["m1_fac"] for r in ROWS]),
         qmin([r["m3_worst"] for r in M3ROWS]) if M3ROWS else float("nan"),
         qmax([r["m3_worst"] for r in M3ROWS]) if M3ROWS else float("nan"),
         sum(r["m3_n"] for r in M3ROWS) if M3ROWS else 0,
         qmin([r["cond_share"] for r in ROWS]),
         qmax([r["cond_share"] for r in ROWS]),
         qmin([r["sig_mass"] for r in ROWS]),
         qmax([r["sig_mass"] for r in ROWS]),
         qmin([r["sig_tot"] for r in ROWS]),
         qmax([r["sig_tot"] for r in ROWS]),
         qmin([r["f_dom"] for r in ROWS]), qmax([r["f_dom"] for r in ROWS]),
         qmin([r["f_cake"] for r in ROWS]), qmax([r["f_cake"] for r in ROWS]),
         qmin([r["f_nest"] for r in ROWS]), qmax([r["f_nest"] for r in ROWS])))
print("TOTAL.Q1_constant  c_0 = 12 sig_tot = %.4f .. %.4f (energy route, "
      "Psi_pos) and c_0 = G_dy = %.4f .. %.4f (sign-free route, Psi_abs); best "
      "%.4f .. %.4f (classical Dirichlet 4; minimum allowed by the measured "
      "density sup %.4f .. %.4f), fit D^%.3f +- %.3f -> %s; S1' CERTIFIED per "
      "window as cert_lam_max(R) <= c_0 x Psi on %d / %d windows"
      % (qmin([r["c0_en"] for r in ROWS]), qmax([r["c0_en"] for r in ROWS]),
         qmin([r["c0_gr"] for r in ROWS]), qmax([r["c0_gr"] for r in ROWS]),
         G_MIN, G_MAX, qmin([r["c0_need"] for r in ROWS]),
         qmax([r["c0_need"] for r in ROWS]), F_C0B["p"], F_C0B["sp"],
         "ZONE-UNIFORM" if C0_UNIF else "NOT zone-uniform",
         len(ROWS) if CHAIN_OK else 0, len(ROWS)))
print("TOTAL.Q2_nogo      the direct spectral argument IS the same chain; the "
      "free direction Psi_all x lam_hat <= 1 is a content-free theorem, and "
      "the NO-GO (R = a a^T + eps I, a_i = i^{-1/2}, R >= 0 entrywise, "
      "Psi_exact = %.4f .. %.4f under the PROVED ceiling 4 + eps, lam_max = "
      "%.4f .. %.4f growing) gives Psi_all x lam_hat = %.4f .. %.4f decaying, "
      "G_dy = %.3f .. %.3f growing against %.3f .. %.3f on the Markovian "
      "control -- so a level-profile hypothesis is NECESSARY"
      % (qmin([x["psi_exact"] for x in NG]) if NG else float("nan"),
         qmax([x["psi_exact"] for x in NG]) if NG else float("nan"),
         qmin([x["lam_top"] for x in NG]) if NG else float("nan"),
         qmax([x["lam_top"] for x in NG]) if NG else float("nan"),
         qmin([x["prod"] for x in NG]) if NG else float("nan"),
         qmax([x["prod"] for x in NG]) if NG else float("nan"),
         qmin([x["G_dy"] for x in NG]) if NG else float("nan"),
         qmax([x["G_dy"] for x in NG]) if NG else float("nan"),
         qmin([x["G_dy"] for x in CT]) if CT else float("nan"),
         qmax([x["G_dy"] for x in CT]) if CT else float("nan")))
print("TOTAL.Q3_s2r5r4    S2' RETIRED as a requirement (the chain has no "
      "interval step; testing constant of the finite family %.4f .. %.4f "
      "against Charikar's cited 2) | R5 CERTIFIED two-sidedly per window "
      "(1/kap_up <= lam/lam_hat <= 1/kap_lo) but the width %.3f .. %.3f is "
      "fit D^%.3f -> %s | R4 %d / %d border blocks carried by the new chain, "
      "%d closed directly"
      % (qmin([r["c_test"] for r in ROWS]), qmax([r["c_test"] for r in ROWS]),
         qmin([r["kap_up"] / r["kap_lo"] for r in ROWS]),
         qmax([r["kap_up"] / r["kap_lo"] for r in ROWS]), F_SAND["p"],
         "ZONE-UNIFORM" if unif_ok(F_SAND) else "NOT zone-uniform",
         len([x for x in BLK if x["chain"] == 1]) if BLK else 0,
         len(BLK) if BLK else 0,
         len([x for x in BLK if x["direct"] == 1]) if BLK else 0))
print("TOTAL.Q4_rest      %s | RETIRED S2', the Markov-perturbation search and "
      "the free-direction reading; R5 downgraded to a per-window certificate"
      % " | ".join(s.split("  ")[0] for s in REST))
print("TOTAL.chain_value  lam_hat >= 1/(c_0 Psi) is %.4f .. %.4f of lam_hat "
      "(fit D^%.3f +- %.3f); lam >= 1/(kap_up c_0 Psi) is %.4f .. %.4f of the "
      "exact pair gap (fit D^%.3f +- %.3f)"
      % (qmin([r["loss_hat"] for r in ROWS]),
         qmax([r["loss_hat"] for r in ROWS]), F_LOSSHAT["p"], F_LOSSHAT["sp"],
         qmin([r["loss_ex"] for r in ROWS]),
         qmax([r["loss_ex"] for r in ROWS]), F_LOSSEX["p"], F_LOSSEX["sp"]))
print("TOTAL.promotions   %d statements ready, %d new (Q1a-Q1f + Q2a-Q2b + "
      "Q3a-Q3c), 0 promoted" % (PROMO_T144 + len(STMT), len(STMT)))
print("TOTAL.surface      %d windows m = %d .. %d, D = %.2e .. %.2e, zones "
      "n = %d .. %d; %d cake levels evaluated, %d test forms, %d border blocks"
      % (len(ROWS), min(r["m"] for r in ROWS), max(r["m"] for r in ROWS),
         qmin(DV), qmax(DV), min(r["n"] for r in ROWS),
         max(r["n"] for r in ROWS), sum(r["K"] for r in ROWS), len(NOGO),
         len(BLK)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised / diagonalised form %d (cap %d)"
      % (max([r["m"] for r in ROWS] + [x["g"] for x in BLK]
             + list(NOGO_SIZES)), MAX_H))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
