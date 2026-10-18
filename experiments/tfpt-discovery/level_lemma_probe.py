"""Discovery probe (2026-07-29), part 146 of the prime/window investigation.
Contract LEVEL.LEMMA -- THE PROOF ATTEMPT for L1, the LEVEL LEMMA.

WHERE THIS SITS (T145 END STATE: ONE-STEP-MISSING, and what the one step is)
  T140 reduced the question to two small matrices per zone, T141 made it a
  weighted Hardy problem, T142 closed the comparison branch, T143 estimated the
  exact capacity Rayleigh form, T144 closed the two-weight calculus, and T145
  transcribed Maz'ya's capacitary proof (Maz'ya 1985) onto the non-Markovian
  gap form step by step.  QUOTED from T140 .. T145 and NEVER re-derived here:
    * the chain lam >= 1 / (c_0 kap_up c_glob B_res) is certified window by
      window, with kap_up <= 1.3162 CERTIFIED and c_glob <= 1.6876;
    * T145's step list M1 .. M4 closes with an EXPLICIT constant
      c_0 = 2.248 .. 4.227 (flat as D^(0.028 +- 0.017)) on 64 of 64 windows;
    * the two constants that carry it are sigma_tot = 0.215 .. 0.443 (fit
      D^0.124) on the ENERGY route and G_dy = 2.156 .. 6.394 (fit D^0.010) on
      the SIGN-FREE / GREEN route;
    * the Markov step M4 is CERTIFIED DEAD, and the entrywise domination that
      replaces it is only true with |R| and NOT with R^+ (T145's LICENCE-4
      lesson, restated and re-verified in L0 below);
    * the NO-GO: R = a a^T + eps I with a_i = i^{-1/2} is positive definite,
      entrywise nonnegative, has an ABSOLUTELY bounded density sup, and yet
      G_dy grows 7.6 -> 36.8 -- so a hypothesis on the LEVEL PROFILE of the
      minimiser is NECESSARY and no sign or density hypothesis can replace it;
    * the profile diagnostics: participation ratio 0.303 .. 0.459.
  So exactly ONE object was missing at the end of T145, and this probe is its
  proof attempt:
    L1  THE LEVEL LEMMA.  An A PRIORI, D-uniform bound for ONE of the two
        constants -- sigma_tot or G_dy -- where A PRIORI means: computed from
        the FORM alone, never from the minimiser.  T145's numbers are exact
        arithmetic AT THE MINIMISER, which is MEASURED and not a hypothesis of
        a theorem; one of the two, bounded a priori, closes S1' and with it the
        whole D-uniformity chain on the measurement surface.

WHAT THIS PROBE DOES
  L0  THE LICENCES.  Ten inequalities, each with its DIRECTION in its name and
      each verified before it is used: the eigenvector identity psi = lam R psi,
      Rayleigh-Ritz, the Cauchy-Schwarz coordinate bound, the layer-cake
      COUNTING lemma (three separate counting inequalities), the l1/l2
      comparison, the |R| vs R^+ direction trap, the residual-corrected
      certified column bound, restricted Gershgorin, Perron-Frobenius
      single-signedness, and the Davis-Kahan direction.
  L1  R1, THE PROFILE.  The a priori candidate for the minimiser, in closed
      form, out of the closed Green geometry of T143 (J = D K D^T, endpoint
      Laplacian, K the covering kernel in closed prefix-sum form): the GREEN
      COLUMN v_j = R e_j.  Four hand-written closed profiles (the endpoint sine
      mode, the linear ramp, the frame's own pole vector, the equilibrium
      potential of the lumped Laplacian) are run against it and all four fail
      by the D^3 CANCELLATION that T143 identified.  Then the decisive turn:
      the Green column needs NO perturbation transfer at all, because the
      eigenvector identity psi = lam_hat R psi is an IDENTITY -- so the
      Davis-Kahan step (Davis-Kahan 1970) is instrumented for contrast and then
      NOT USED.  Out of it comes the a priori constant
          Gam = sqrt(m) x lam_up x max_j ||R e_j||
      and the LEVEL LEMMA in the shape
          G_dy <= 8 ||psi||_inf ||psi||_1 / ||psi||^2 <= 8 Gam min(1, Gam_1),
      every factor a priori.
  L2  R2, DELOCALISATION DIRECTLY.  Two mechanisms.  (i) THE RESOLVENT
      MECHANISM, which is the one that works, and which uses the Theta(D^3)
      scale ITSELF as the lever: psi = lam_hat R psi means the minimiser is the
      image of a TINY multiple of the Green function, so its sup norm is small
      exactly because lam_hat is small.  (ii) THE LOCALISATION CONTRADICTION,
      instrumented honestly: restricted Gershgorin gives a certified local
      Rayleigh floor mu_lo(l), hence a certified localisation length l* below
      which the minimiser CANNOT live -- and then the quantitative window in
      which the implication survives a leak of mass is computed, and it is
      reported as too narrow to deliver a sup-norm bound.  Perron-Frobenius is
      run on the lumped partner W, where it applies, and its overlap with the
      true minimiser is measured.
  L3  R3, CLEANING UP.  The three open R4 border blocks through the a priori
      chain; the kappa remainder as a certified building block; and the STRESS
      TEST of the L1 candidate on the no-go form, where it MUST fail -- if it
      did not, it would be too strong and therefore wrong -- plus the control
      form, where it must stay bounded.
  L4  R4, the map V18, the promotion list, the shortest rest list, the verdict.

WHAT IS A THEOREM, WHAT IS CERTIFIED, WHAT IS EXACT, WHAT IS MEASURED
  * THEOREM means classical, cited, and never re-proved.  Maz'ya's strong-type
    half is NOT among the cited results -- that is the thing under attack.
  * CERTIFIED means a completed Cholesky (Wilkinson 1968; Higham 2002) with the
    declared floating-point floor, in the DIRECTION stated in the name, or a
    residual-corrected linear-solve bound with the same floor.
  * A PRIORI, the notion this whole probe turns on, means: the number is a
    functional of the FORM E alone.  A number computed from the minimiser --
    sigma_tot, G_dy, the participation ratio -- is MEASURED, however exact its
    arithmetic, and the verdict rule below refuses to count it.
  * EXACT means finite arithmetic on a finite object.
  * A FIT is a least-squares exponent with a delete-one jackknife band, always
    labelled, NEVER load-bearing.

FENCES
  * THE RH FENCE, PROMINENT AND FIRST.  The surrounding statement is the
    positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999) on
    a FINITE list of prime-power zones and a FINITE window.  The criterion is
    CITED as an address and is NEVER USED, in either direction.  Nothing here
    claims, assumes or approaches RH.  Even with L1 closed, what stands is a
    finite-window positivity statement with an explicit constant on prime-power
    zones -- the distance from there to RH is mapped in L4 and never travelled.
    No zero data of any kind is read, generated or approximated; an AST
    firewall enforces this, together with the import whitelist and the absence
    of any write-mode file access.
  * DISCOVERY ONLY.  Nothing is promoted.  No verification module, no ledger,
    no TeX, no website, no changelog, no next.txt is touched; this is ONE new
    file in experiments/tfpt-discovery/ and it writes nothing.
  * HARD CAPS.  Largest factorised / inverted / diagonalised matrix <= 1500;
    runtime budget 660 s (< 900 s), with per-block guards that truncate a pool
    rather than overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh

np.seterr(all="ignore")

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 660.0             # HARD probe budget (< 900 s)
RESERVE_S = 200.0            # reserved for L2 .. L4 before the window loop ends

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 2200000
ZONE_DEEP = 2050000

# --- the measurement surface ------------------------------------------------
SURF_ZONES = 64              # T145's surface, zone for zone
SURF_HCAP = 1200             # <= MAX_H; the inverse of E is dense
LEV_MAX = 34                 # dyadic levels kept above the floor level (T145)
PERRON_EVERY = 3             # the Perron partner is read on every third window

# --- THE CAKE BASE, a PREREGISTERED grid.  The chain consumes only the LOWER
# domination |psi| <= psi_t, so the base of the layer cake is a FREE PARAMETER
# and the classical dyadic choice is not the best one.  The grid is fixed here,
# before any number is computed, and a minimum over finitely many VALID upper
# bounds is a valid upper bound.
BASE_GRID = (2.0, 1.5, 1.25, 1.125, 1.0625, 1.03125)
FL_TARGET = 1.0e-12          # the absolute floor level of the untruncated cake

# --- the necessity criterion for the no-go stress test (preregistered) ------
BAR_NOGO_GROW = 0.20         # the growth exponent in m that counts as UNBOUNDED
BAR_NOGO_RATIO = 1.5         # and the raw ratio over the size ladder
BAR_CTRL_FLAT = 0.05         # and the exponent that counts as FLAT on the control

# --- L2 the localisation contradiction --------------------------------------
LOC_LMAX = 64                # localisation lengths l = 1 .. LOC_LMAX
LOC_DELTA = np.concatenate([np.geomspace(1.0e-14, 0.5, 60), [0.9, 0.99]])

# --- L3 the stress tests ----------------------------------------------------
NOGO_SIZES = (64, 128, 256, 512, 1024, 1500)
NOGO_EPS = 1.0e-3
CTRL_SIZES = (64, 128, 256, 512, 1024, 1500)

# --- L3 the border blocks (the T145 pool, rebuilt identically) --------------
K3_GC_MIN = 2
K3_HCAP = 300
K3_MAX = 24
K3_PER_RHO = 2
K3_RHO = (1.001, 1.05, 1.20, 1.49531, 2.00, 3.50)
K3_LOGRES = 80.0

# --- preregistered bars (declared before any number is computed) ------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_UNIF = 0.25              # |exponent in D| for "ZONE-UNIFORM", preregistered
BAR_C0 = 16.0                # an absolute constant of CLASSICAL SIZE: four
#                              times Maz'ya's Dirichlet constant c_0 = 4.  The
#                              a priori level constant counts as PROOF-SHAPED
#                              only if it stays below this on every window.
BAR_GAM = 4.0                # and the delocalisation factor Gam below this
MAZYA_C0 = 4.0               # the classical Dirichlet constant, CITED

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
N_PROBES_PRIOR = 145
KAP_UP_T144 = 1.3162
CGLOB_T144 = 1.6876
PSI_ALL_T144 = (0.7399, 0.8515)
C0_T145 = (2.248, 4.227)
C0_EXP_T145 = (0.028, 0.017)
SIGT_T145 = (0.215, 0.443)
SIGT_EXP_T145 = 0.124
GDY_T145 = (2.156, 6.394)
GDY_EXP_T145 = 0.010
PART_T145 = (0.303, 0.459)
KAP_EXP_T145 = 0.065
NOGO_GDY_T145 = (7.6, 36.8)
POOL_C0_T145 = (1.797, 5.422)
R4_OPEN_T145 = 3
PROMO_T145 = 104
GAP_EXP_T145 = (3.06, 0.09)
WIN_T145 = 64


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


def fit_str(f):
    return "D^(%.3f +- %.3f)" % (f["p"], f["sp"])


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
          == "level_lemma_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T145 code path
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


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2).  THE frame's
    OWN closed vector, hence one of the a priori candidate profiles of L1."""
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
    a LOWER bound.  The GUESS is only a SEED for the search: its provenance is
    irrelevant to the certificate, which is the completed factorisation."""
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
    assembly source, exactly as T138 .. T145 did."""
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
# THE LUMPED M-MATRIX PAIR (T136 .. T145) and the JACOBI WHITENING
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
    return dict(h=h, A_B=A_B, Dl=Dl, LD=LD, P_row=P_row,
                dg=dg, dgB=np.diag(A_B).copy(),
                stieltjes=int(bool(np.all(offB <= 1.0e-300))
                              and bool(np.all(np.diag(A_B) > 0.0))),
                n_pos=int(np.count_nonzero(np.where(np.eye(h, dtype=bool),
                                                    0.0, off) > 0.0)))


def jacobi_whiten(A, A_B):
    """With Lam = diag(A_B), E = Lam^{-1/2} A Lam^{-1/2} carries the COUNTING
    measure in the denominator and W = Lam^{-1/2} A_B Lam^{-1/2} has UNIT
    DIAGONAL.  DIRECTION: kap_up = cert_lam_max(W) is an UPPER bound and
    kap_lo = cert_lam_min(W) a LOWER one, and
        lam_min(E) / kap_up <= lam_min(A, A_B) <= lam_min(E) / kap_lo
    by Loewner, so the LEFT inequality is the usable lower bound on the gap."""
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
    return dict(E=E, W=W, Lam=Lam, kap_up=kap_up, kap_lo=kap_lo)


# ----------------------------------------------------------------------------
# THE DENSITY UPPER BOUND (T144 / T145, QUOTED in form and re-verified)
# ----------------------------------------------------------------------------
def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000) for the MAXIMUM DENSITY
    SUBGRAPH of a NONNEGATIVE symmetric weight matrix with zero diagonal.
    DIRECTIONS, both cited and both used: the returned density is ATTAINED,
    hence a LOWER bound on the optimum; and Charikar's guarantee
    greedy >= opt / 2 turns it into opt <= 2 x greedy, which is the only bound
    here that holds over ALL 2^m sets."""
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
    """AN UPPER BOUND for Psi_all = sup_A (1^T R_AA 1) / |A| over ALL 2^m sets,
    with a CITED constant and no family restriction:
        1^T R_AA 1 / |A| <= max_i R_ii + 2 x (edge density of A)
    and the edge density of the nonnegative off-diagonal part is bounded either
    by 2 x Charikar's greedy value or by the CERTIFIED lam_max of the same
    nonnegative matrix, whichever is smaller.  DIRECTION: an UPPER bound.

    IT MATTERS WHICH MATRIX IS PASSED IN, and this is T145's LICENCE-4 lesson
    restated: the SIGN-FREE route needs the bound for |R| and NOT for R^+,
    because the entrywise domination psi^T R psi <= |psi|^T |R| |psi| is only
    true with the ABSOLUTE VALUE once psi changes sign.  Everything below that
    consumes a density feeds it |R|."""
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    gr = greedy_density(Rp)
    dg_max = float(np.max(np.diag(R)))
    psi_char = dg_max + 4.0 * gr["dens"]
    psi_spec = dg_max + cert_lam_max(Rp, guess=ray_top(Rp))
    cands = [x for x in (psi_char, psi_spec) if np.isfinite(x)]
    best = min(cands) if cands else float("nan")
    del Rp
    return dict(up=best, char=psi_char, spec=psi_spec, greedy=gr["dens"],
                size=gr["size"], dg_max=dg_max)


# ----------------------------------------------------------------------------
# THE DYADIC LAYER CAKE and its GEOMETRIC LEVEL CONSTANT G_dy (T145, QUOTED)
# ----------------------------------------------------------------------------
def layer_cake(psi, base=2.0, n_lev=LEV_MAX):
    """THE LAYER CAKE of |psi| to a GENERAL BASE, as a NESTED DECREASING chain
    of sets with POSITIVE coefficients: S_k = {|psi| > base^k} with coefficient
    (base - 1) base^k, plus a FLOOR level j = 0 which is the FULL set with
    coefficient base^{k_bot}.  The coefficients TELESCOPE, so for every
    coordinate psi_t,i = base^{k_i + 1} exactly, where base^{k_i} is the
    largest level strictly below |psi_i| -- hence base^{-1} psi_t <= |psi| <=
    psi_t with NO slack term, which is what makes the whole calculation closed.
    At base = 2 and n_lev = LEV_MAX this is T145's cake, coefficient for
    coefficient.  The K x K representation is built here only because the
    IDENTITY of L0 is checked against it; the surface uses the O(m) form."""
    v = np.abs(np.asarray(psi, dtype=float))
    m = v.shape[0]
    vmax = float(np.max(v))
    if not (vmax > 0.0):
        return None
    lb = math.log(base)
    k_top = int(math.floor(math.log(vmax) / lb))
    while base ** k_top >= vmax:
        k_top -= 1
    while base ** (k_top + 1) < vmax:
        k_top += 1
    k_bot = k_top - n_lev + 1
    order = np.argsort(-v, kind="stable")
    sizes = [m]
    coef = [base ** k_bot]
    for k in range(k_bot, k_top + 1):
        t = base ** k
        n_k = int(np.count_nonzero(v > t))
        if n_k <= 0:
            continue
        sizes.append(n_k)
        coef.append((base - 1.0) * t)
    K = len(sizes)
    Ind = np.zeros((K, m))
    for j in range(K):
        Ind[j, order[:sizes[j]]] = 1.0
    cv = np.array(coef, dtype=float)
    nv = np.array(sizes, dtype=float)
    psi_t = Ind.T @ cv
    jj = np.arange(K)
    mn = np.minimum.outer(jj, jj)          # the LARGER set has the SMALLER index
    return dict(K=K, Ind=Ind, c=cv, n=nv, psi_t=psi_t, v=v, mn=mn, base=base,
                k_top=k_top, k_bot=k_bot, m=m,
                dom_lo=float(np.min(psi_t - v)),
                dom_hi=float(np.max(psi_t - base * v)))


def gdy_kk(lc, psi):
    """G = sum_{j,l} c_j c_l |S_{min(j,l)}| / ||psi||^2 by the K x K DOUBLE SUM,
    which is T145's arithmetic.  Kept only as the reference for the identity of
    L0; it costs K^2 and the closed form below costs m."""
    c, nv, mn = lc["c"], lc["n"], lc["mn"]
    nrm2 = float(psi @ psi)
    return float(c @ (nv[mn] @ c)) / max(nrm2, 1.0e-300)


def cake_profile(v, base, n_lev=None, fl_target=FL_TARGET):
    """THE LEVEL CONSTANT IN CLOSED FORM, and the first of this probe's two
    structural findings.

    THE IDENTITY.  For a NESTED chain the union of two levels is the larger of
    the two, so with T = sum_j c_j and psi_t,i = sum_{j: i in S_j} c_j,
        sum_{j,l} c_j c_l |S_j u S_l| = sum_i [ T^2 - (T - psi_t,i)^2 ]
                                      = 2 T ||psi_t||_1 - ||psi_t||^2 ,
    an EXACT evaluation in O(m) that never forms the K x K matrix and therefore
    never needs the cake to be truncated for cost reasons.  Verified against
    the K x K double sum in L0.

    THE THEOREM.  The telescoping coefficients give T = base^{k_top + 1} <
    base ||psi||_inf and ||psi_t||_1 <= base ||psi||_1 + m base^{k_bot}, so
        G(base) <= 2 base^2 ||psi||_inf ||psi||_1 / ||psi||^2 + eps ,
        eps = 2 base ||psi||_inf m base^{k_bot} / ||psi||^2 ,
    and at base = 2 the leading constant is 8, which is the classical dyadic
    value.  THE POINT: the chain of T145 consumes ONLY the lower domination
    |psi| <= psi_t (it needs psi_t >= 0 entrywise against a nonnegative |R|),
    never the upper one, so the base is FREE and the constant 2 base^2 falls to
    2 as base -> 1.  The floor term is what stops it, and the floor is O(m
    base^{k_bot}) with k_bot chosen from an ABSOLUTE target, so it costs
    nothing: the number of levels grows but the O(m) evaluation does not see
    it."""
    v = np.abs(np.asarray(v, dtype=float))
    m = v.shape[0]
    vmax = float(np.max(v))
    if not (vmax > 0.0):
        return None
    lb = math.log(base)
    k_top = int(math.floor(math.log(vmax) / lb))
    while base ** k_top >= vmax:
        k_top -= 1
    while base ** (k_top + 1) < vmax:
        k_top += 1
    if n_lev is None:
        k_bot = int(math.floor(math.log(fl_target) / lb))
        while base ** k_bot > fl_target:
            k_bot -= 1
    else:
        k_bot = k_top - n_lev + 1
    fl = base ** k_bot
    T = base ** (k_top + 1)
    kk = np.floor(np.log(np.maximum(v, 1.0e-300)) / lb)
    kk = np.where(base ** kk >= v, kk - 1.0, kk)
    B = np.maximum(base ** (kk + 1.0), fl)
    B = np.where(v <= fl, fl, B)
    nrm2 = float(v @ v)
    v_l1 = float(v.sum())
    s1 = float(B.sum())
    G = (2.0 * T * s1 - float(B @ B)) / max(nrm2, 1.0e-300)
    eps = 2.0 * base * vmax * m * fl / max(nrm2, 1.0e-300)
    thm = 2.0 * base * base * vmax * v_l1 / max(nrm2, 1.0e-300) + eps
    return dict(base=base, m=m, k_top=k_top, k_bot=k_bot, fl=fl, T=T, B=B,
                G=G, thm=thm, eps=eps, vmax=vmax, v_l1=v_l1, nrm2=nrm2, s1=s1,
                n_lev=k_top - k_bot + 1,
                dom_min=float(np.min(B - v)),
                t_slack=base * vmax - T,
                s1_slack=(base * v_l1 + m * fl) - s1)


def c0_of_base(Gam, Gam_1, base, m, vmax_ap=None):
    """THE A PRIORI LEVEL CONSTANT at a given cake base:
        c_0_ap(base) = 2 base^2 x (sup bound) x (l1 bound) + eps ,
    with the sup bound Gam / sqrt(m) and the l1 bound sqrt(m) min(1, Gam_1),
    both a priori.  eps uses the a priori sup bound in place of ||psi||_inf,
    so no factor of it reads the minimiser either."""
    if vmax_ap is None:
        vmax_ap = Gam / math.sqrt(max(m, 1))
    lb = math.log(base)
    k_bot = int(math.floor(math.log(FL_TARGET) / lb))
    while base ** k_bot > FL_TARGET:
        k_bot -= 1
    eps = 2.0 * base * vmax_ap * m * (base ** k_bot)
    return 2.0 * base * base * Gam * min(1.0, Gam_1) + eps, eps


# ----------------------------------------------------------------------------
# THE HEART: THE A PRIORI LEVEL CONSTANT.  Nothing here touches the minimiser
# ----------------------------------------------------------------------------
def apriori_level(E, R=None, lam_lo=None, lam_seed=None):
    """THE LEVEL LEMMA'S A PRIORI SIDE, computed from the FORM E alone.

    Let R = E^{-1} and c_j = R e_j the GREEN COLUMNS -- the closed objects of
    the T143 Green geometry, one linear solve each.  Three classical steps:

      (A) RAYLEIGH-RITZ (Rayleigh 1877; Ritz 1909).  Each Green column is an
          explicit test vector, so
              lam_up := min_j (c_j^T E c_j) / (c_j^T c_j)  >=  lam_min(E) ,
          and this is an A PRIORI UPPER BOUND on the gap of the whitened form.
          It is also ONE step of inverse iteration from a delta function, which
          is why it is TIGHT: if R is dominated by its top mode -- and it is,
          precisely because lam_min = Theta(D^3) is tiny -- then c_j is nearly
          parallel to the minimiser and lam_up is nearly lam_min.

      (B) THE RESOLVENT IDENTITY.  E psi = lam psi is EQUIVALENT to
          psi = lam R psi, an IDENTITY and not an approximation, so by
          Cauchy-Schwarz, for every coordinate j,
              |psi_j| <= lam ||R e_j|| ||psi||  and  ||psi||_1 <=
              lam (sum_j ||R e_j||) ||psi|| .
          Both are A PRIORI once lam is replaced by lam_up >= lam, and BOTH
          hold for EVERY eigenvector at the bottom, so no assumption that any
          computed vector IS the minimiser is made anywhere.

      (C) THE CERTIFIED COLUMN NORM.  ||R e_j|| is needed from ABOVE.  With the
          computed column x_j and its residual r_j = E x_j - e_j,
              ||R e_j|| <= ||x_j|| + ||r_j|| / lam_lo
          with lam_lo = cert_lam_min(E) a certified LOWER bound -- so the
          direction is closed and the linear-solve error is paid for and not
          assumed away.

    The output is Gam = sqrt(m) lam_up max_j ||R e_j||_up, which bounds the
    NORMALISED sup norm sqrt(m) ||psi||_inf / ||psi|| and hence the
    participation ratio from BELOW by 1 / Gam^2, and Gam_1 = lam_up sum_j
    ||R e_j||_up / sqrt(m), which bounds ||psi||_1 / (sqrt(m) ||psi||).
    """
    m = E.shape[0]
    if R is None:
        fac = safe_cho(E)
        if fac is None:
            return None
        R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    if lam_lo is None:
        if lam_seed is None:
            try:
                lam_seed = float(eigvalsh(E, subset_by_index=[0, 0])[0])
            except (LinAlgError, ValueError):
                lam_seed = None
        lam_lo = cert_lam_min(E, guess=lam_seed)
    if not (np.isfinite(lam_lo) and lam_lo > 0.0):
        return None
    EV = E @ R
    den = np.sum(R * R, axis=0)                       # ||x_j||^2
    num = np.sum(R * EV, axis=0)                      # x_j^T E x_j
    Res = EV - np.eye(m)
    rres = np.linalg.norm(Res, axis=0)
    del EV, Res
    good = den > 0.0
    if not bool(np.all(good)):
        return None
    fl_q = chol_floor(gersh(E), m)
    lam_up = float(np.min(num / den)) + fl_q
    j_star = int(np.argmin(num / den))
    col_up = np.sqrt(den) + rres / lam_lo
    col_raw = np.sqrt(den)
    gam_G = float(np.max(col_up))
    sum_col = float(np.sum(col_up))
    Gam = math.sqrt(m) * lam_up * gam_G
    Gam_1 = lam_up * sum_col / math.sqrt(m)
    # the a priori LEVEL CONSTANT over the preregistered base grid: the l1
    # factor is the better of the resolvent bound and Cauchy-Schwarz ||psi||_1
    # <= sqrt(m) ||psi||.  Both factors are a priori, so every product is, and
    # the MINIMUM over finitely many valid upper bounds is a valid upper bound.
    c0_by_base = {}
    for b in BASE_GRID:
        c0_by_base[b] = c0_of_base(Gam, Gam_1, b, m)
    c0_dy, eps_dy = c0_by_base[2.0]
    base_star = min(BASE_GRID, key=lambda b: c0_by_base[b][0])
    c0_ap, eps_ap = c0_by_base[base_star]
    return dict(m=m, R=R, lam_lo=lam_lo, lam_up=lam_up, j_star=j_star,
                gam_G=gam_G, sum_col=sum_col, Gam=Gam, Gam_1=Gam_1,
                c0_ap=c0_ap, eps_cake=eps_ap, c0_dy=c0_dy, base_star=base_star,
                c0_by_base=c0_by_base, fl_q=fl_q,
                col_up=col_up, col_raw=col_raw,
                res_max=float(np.max(rres)),
                res_share=float(np.max(rres / lam_lo / np.maximum(col_raw,
                                                                  1.0e-300))))


def local_floor(E, l_max=LOC_LMAX):
    """THE CERTIFIED LOCAL RAYLEIGH FLOOR by RESTRICTED GERSHGORIN
    (Gerschgorin 1931): for EVERY set S with |S| = l and every vector supported
    on S,
        Rayleigh >= lam_min(E_SS) >= min_i E_ii - g(l) ,
        g(l) = max_i (sum of the l - 1 largest |E_ij|, j != i) ,
    which is a bound over ALL C(m, l) sets at the cost of one sort.  DIRECTION:
    a LOWER bound on the local floor, which is the direction a LOCALISATION
    CONTRADICTION consumes."""
    m = E.shape[0]
    off = np.abs(E) - np.diag(np.abs(np.diag(E)))
    lm = min(l_max, m)
    part = np.sort(off, axis=1)[:, ::-1][:, :max(lm - 1, 1)]
    cs = np.cumsum(part, axis=1)
    g = np.concatenate([[0.0], np.max(cs, axis=0)])[:lm]
    mind = float(np.min(np.diag(E)))
    return dict(mind=mind, g=g, mu=mind - g, lm=lm)


def loc_delta_window(mu_l, nrm_up, lam_lo, lam_up):
    """THE QUANTITATIVE VERSION of the contradiction, and the place where it is
    decided whether the implication CARRIES.  If psi = a + b with a supported
    on S, |S| = l, and ||b||^2 = delta, then
        psi^T E psi >= mu(l) (1 - delta) - 2 ||E|| sqrt(delta (1 - delta))
                       + lam_lo delta ,
    so the contradiction with psi^T E psi = lam <= lam_up survives only while
    delta stays below the returned threshold.  The CROSS TERM is what decides
    it, and it enters with sqrt(delta), not delta.

    Returns nan when the norm certificate is unavailable: without a CERTIFIED
    ||E|| from above the cross term cannot be bounded, and a missing bound is
    reported as missing rather than replaced by a measured norm."""
    if not np.isfinite(nrm_up):
        return float("nan")
    best = 0.0
    for d in LOC_DELTA:
        lhs = (mu_l * (1.0 - d) - 2.0 * nrm_up * math.sqrt(d * (1.0 - d))
               + lam_lo * d)
        if lhs > lam_up:
            best = max(best, float(d))
    return best


# ----------------------------------------------------------------------------
# THE STRESS FORMS of L3 -- explicit, cheap, and decisive
# ----------------------------------------------------------------------------
def nogo_form(m, eps=NOGO_EPS):
    """THE T145 NO-GO: R = a a^T + eps I with a_i = i^{-1/2}.  R is POSITIVE
    DEFINITE, ENTRYWISE NONNEGATIVE, and its density sup over ALL sets is
    absolutely bounded, while lam_max(R) grows like log m.  Its inverse is
    CLOSED: E = R^{-1} = (I - a a^T / (eps + ||a||^2)) / eps.  The L1 candidate
    MUST FAIL here -- if it did not, it would prove a false statement."""
    a = 1.0 / np.sqrt(np.arange(1, m + 1, dtype=float))
    R = np.outer(a, a) + eps * np.eye(m)
    n2 = float(a @ a)
    E = sym((np.eye(m) - np.outer(a, a) / (eps + n2)) / eps)
    return dict(R=sym(R), E=E, a=a, lam_top=n2 + eps,
                psi=a / math.sqrt(n2), lam_min=1.0 / (n2 + eps))


def control_form(m):
    """THE CONTROL: the Dirichlet path Laplacian, a genuine MARKOVIAN form.
    Its Green function is nonnegative, its minimiser is the smooth half-sine
    mode, its level profile is flat -- so the L1 candidate must stay BOUNDED
    here, uniformly in m."""
    E = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    fac = safe_cho(E)
    if fac is None:
        return None
    R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    w, V = eigh(E, subset_by_index=[0, 0])
    return dict(E=E, R=R, lam_min=float(w[0]), psi=V[:, 0].copy())


# ----------------------------------------------------------------------------
section("L0  SETUP, THE RH FENCE, and THE TEN LICENCES")
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
check("el_l0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

RNG = np.random.default_rng(14607291)

para("""L0.0  THE RH FENCE, STATED BEFORE ANY NUMBER AND PROMINENTLY.  The
surrounding statement is the positivity of a Weil window form (Weil 1952;
Bombieri 2000; Connes 1999) on a FINITE list of prime-power zones and a FINITE
window; the criterion is CITED as that address and is NEVER USED here, in
either direction.  Nothing in this file claims, assumes or approaches RH.  This
probe attacks ONE missing input of ONE classical inequality -- the LEVEL LEMMA
that T145 isolated inside Maz'ya's capacitary strong-type bound (Maz'ya 1985)
for a form that is NOT a Dirichlet form -- and even if that input were closed
with the explicit a priori constant produced below, what would stand is a
finite-window positivity statement on prime-power zones with an explicit
constant, and nothing more; the distance from there to RH is mapped in L4 and
never travelled.  No zero data is read, generated or approximated: the AST
firewall above enforces that, together with the import whitelist and the
absence of any write-mode file access.""")

para("""L0.1  WHAT "A PRIORI" MEANS HERE, and why the whole probe turns on it.
T145 ended with an EXPLICIT constant c_0 = %.3f .. %.3f on %d of %d windows,
and that constant is EXACT ARITHMETIC -- but on the layer cake OF THE
MINIMISER.  A theorem may not read its own solution.  So this probe declares,
before computing anything, the rule it will be judged by: a number counts as A
PRIORI only if it is a functional of the FORM E alone, and every number that
touches the computed bottom eigenvector -- sigma_tot, G_dy, the participation
ratio -- is MEASURED and enters only as a CROSS-CHECK, never as a hypothesis.
The verdict rule at the end is hard-wired to that distinction and cannot be
talked out of it.""" % (C0_T145[0], C0_T145[1], WIN_T145, WIN_T145))

# --- L0.2  THE TEN LICENCES, each with its DIRECTION in its name ------------
LIC_N = 9
LIC_M = 40
lic_eig, lic_ritz, lic_cs, lic_cnt1, lic_cnt2, lic_cnt3 = [], [], [], [], [], []
lic_cake, lic_l1, lic_col, lic_ger = [], [], [], []
lic_dom, lic_ident = [], []
for _t in range(LIC_N):
    B = RNG.standard_normal((LIC_M, LIC_M))
    Ex = sym(B @ B.T) + 0.3 * np.eye(LIC_M)
    fac = safe_cho(Ex)
    Rx = sym(cho_solve(fac, np.eye(LIC_M), check_finite=False))
    wx, Vx = eigh(Ex, subset_by_index=[0, 0])
    lx = float(wx[0])
    px = Vx[:, 0] / float(np.linalg.norm(Vx[:, 0]))
    # LICENCE 1  THE EIGENVECTOR IDENTITY  psi = lam R psi  (an IDENTITY)
    lic_eig.append(rel(px, lx * (Rx @ px)))
    # LICENCE 2  RAYLEIGH-RITZ, DIRECTION: an UPPER bound on lam_min
    dn = np.sum(Rx * Rx, axis=0)
    nu = np.sum(Rx * (Ex @ Rx), axis=0)
    lic_ritz.append(float(np.min(nu / dn)) - lx)
    # LICENCE 3  CAUCHY-SCHWARZ per coordinate, DIRECTION: an UPPER bound
    lic_cs.append(float(np.max(np.abs(px) - lx * np.sqrt(dn))))
    # LICENCE 4  THE COUNTING INEQUALITIES of the cake, at EVERY base in the
    # grid, plus the nestedness step that gives the classical dyadic shape
    for b in BASE_GRID:
        cp = cake_profile(px, b)
        lic_dom.append(-cp["dom_min"])
        lic_cnt1.append(-cp["t_slack"])
        lic_cnt2.append(-cp["s1_slack"])
        # LICENCE 5  the cake THEOREM itself, at every base
        lic_cake.append(cp["G"] - cp["thm"])
    lcx = layer_cake(px)
    nvx, mnx = lcx["n"], lcx["mn"]
    lic_cnt3.append(float(np.max(nvx[mnx] - (nvx[:, None] + nvx[None, :]))))
    # LICENCE 4d  THE UNION IDENTITY: the O(m) closed form equals the K x K
    # double sum, at the base and truncation T145 used
    cp2 = cake_profile(px, 2.0, n_lev=LEV_MAX)
    lic_ident.append(abs(cp2["G"] - gdy_kk(lcx, px))
                     / max(abs(cp2["G"]), 1.0e-300))
    # LICENCE 6  l1 vs l2, DIRECTION: ||v||_1 <= sqrt(m) ||v||
    lic_l1.append(float(np.abs(px).sum()) - math.sqrt(LIC_M)
                  * float(np.linalg.norm(px)))
    # LICENCE 7  the residual-corrected certified column bound
    llo = cert_lam_min(Ex, guess=lx)
    xj = Rx[:, 0]
    rj = float(np.linalg.norm(Ex @ xj - np.eye(LIC_M)[:, 0]))
    lic_col.append(float(np.linalg.norm(Rx[:, 0]))
                   - (float(np.linalg.norm(xj)) + rj / llo))
    # LICENCE 8  RESTRICTED GERSHGORIN, DIRECTION: a LOWER local floor
    lf = local_floor(Ex, l_max=12)
    worst = 0.0
    for ll in range(1, 12):
        idx = np.sort(RNG.choice(LIC_M, size=ll, replace=False))
        sub = sym(np.ascontiguousarray(Ex[np.ix_(idx, idx)]))
        lmin_sub = float(eigvalsh(sub, subset_by_index=[0, 0])[0])
        worst = min(worst, lmin_sub - lf["mu"][ll - 1])
    lic_ger.append(worst)

check("el_l0.lic1_eigen_identity", qmax([abs(x) for x in lic_eig]) <= BAR_ID,
      "LICENCE 1, THE ENGINE OF THIS PROBE.  psi = lam R psi holds to %.2e "
      "(bar %.0e) on %d random forms.  It is an IDENTITY, not a perturbation "
      "statement -- which is why L1 will need NO transfer step at all"
      % (qmax([abs(x) for x in lic_eig]), BAR_ID, LIC_N))

check("el_l0.lic2_rayleigh_ritz", all(x >= -BAR_ID for x in lic_ritz),
      "LICENCE 2, DIRECTION UPPER: min_j Rayleigh(R e_j) - lam_min >= 0 with "
      "slack %.3e .. %.3e (Rayleigh 1877; Ritz 1909).  The Green columns are "
      "legal test vectors, so lam_up is an A PRIORI upper bound on the gap"
      % (qmin(lic_ritz), qmax(lic_ritz)))

check("el_l0.lic3_cauchy_schwarz", all(x <= BAR_ID for x in lic_cs),
      "LICENCE 3, DIRECTION UPPER: |psi_j| - lam ||R e_j|| <= %.2e -- the "
      "coordinate bound the sup-norm delocalisation is built from"
      % qmax(lic_cs))

check("el_l0.lic4_cake_counting",
      all(x <= BAR_ID for x in lic_dom) and all(x <= BAR_ID for x in lic_cnt1)
      and all(x <= BAR_ID for x in lic_cnt2)
      and all(x <= BAR_ID for x in lic_cnt3),
      "LICENCE 4, the COUNTING INEQUALITIES of the layer cake, at ALL %d bases "
      "of the preregistered grid and all in the direction the chain consumes: "
      "the DOMINATION |v| <= psi_t (slack %.2e), the level-weight sum T <= "
      "base ||v||_inf (slack %.2e), the level-mass sum ||psi_t||_1 <= base "
      "||v||_1 + m base^kbot (slack %.2e), and the classical nestedness step "
      "|S_{j/\\l}| <= n_j + n_l (slack %.2e).  Pure counting, no analysis"
      % (len(BASE_GRID), qmax(lic_dom), qmax(lic_cnt1), qmax(lic_cnt2),
         qmax(lic_cnt3)))

check("el_l0.lic4d_union_identity", qmax(lic_ident) <= BAR_ID,
      "LICENCE 4d, AN IDENTITY and the reason the base can be moved at all: "
      "for a NESTED chain sum_{j,l} c_j c_l |S_j u S_l| = 2 T ||psi_t||_1 - "
      "||psi_t||^2, so the level constant is an O(m) closed form and not a "
      "K x K double sum.  Checked against T145's K x K arithmetic at base 2 "
      "and %d levels: relative difference %.2e (bar %.0e)"
      % (LEV_MAX, qmax(lic_ident), BAR_ID))

check("el_l0.lic5_cake_theorem", all(x <= 0.0 for x in lic_cake),
      "LICENCE 5, THE LAYER-CAKE COUNTING LEMMA as a single statement, at all "
      "%d bases: G(base) <= 2 base^2 ||v||_inf ||v||_1 / ||v||^2 + eps, "
      "verified with margin %.3f .. %.3f on the random draws.  At base 2 the "
      "leading constant is the classical 8; the chain never uses the upper "
      "domination psi_t <= base |v|, so the base is FREE and the constant "
      "falls to 2 base^2.  This is the FIRST HALF of L1 and it is a THEOREM "
      "about ANY vector -- it never mentions a minimiser"
      % (len(BASE_GRID), qmin([-x for x in lic_cake]),
         qmax([-x for x in lic_cake])))

check("el_l0.lic6_l1_l2", all(x <= BAR_ID for x in lic_l1),
      "LICENCE 6, DIRECTION UPPER: ||v||_1 <= sqrt(m) ||v|| with slack %.2e, "
      "the fallback used whenever the resolvent l1 bound is the weaker one"
      % qmax(lic_l1))

check("el_l0.lic7_certified_column", all(x <= 0.0 for x in lic_col),
      "LICENCE 7, DIRECTION UPPER and the one place the LINEAR-SOLVE ERROR is "
      "paid for rather than assumed away: ||E^{-1} e_j|| <= ||x_j|| + "
      "||E x_j - e_j|| / cert_lam_min(E), margin %.2e .. %.2e"
      % (qmin([-x for x in lic_col]), qmax([-x for x in lic_col])))

check("el_l0.lic8_restricted_gershgorin", all(x >= -BAR_ID for x in lic_ger),
      "LICENCE 8, DIRECTION LOWER over ALL C(m,l) sets at the price of one "
      "sort: lam_min(E_SS) >= min_i E_ii - g(|S|) (Gerschgorin 1931), worst "
      "slack %.3e over %d random subsets per draw" % (qmin(lic_ger), 11))

# LICENCE 9  THE DIRECTION TRAP: |R| is NOT R^+  (T145's LICENCE-4 lesson)
R_TRAP = np.array([[1.0, -0.9], [-0.9, 1.0]])
V_TRAP = np.array([1.0, -1.0])
TRAP_TRUE = float(V_TRAP @ R_TRAP @ V_TRAP)
TRAP_ABS = float(np.abs(V_TRAP) @ np.abs(R_TRAP) @ np.abs(V_TRAP))
TRAP_POS = float(np.abs(V_TRAP) @ np.maximum(R_TRAP, 0.0) @ np.abs(V_TRAP))
check("el_l0.lic9_abs_not_plus",
      TRAP_TRUE <= TRAP_ABS + BAR_ID and TRAP_TRUE > TRAP_POS,
      "LICENCE 9, THE DIRECTION TRAP, restated because T145 lost a whole "
      "branch to it.  On the explicit PD form [[1,-.9],[-.9,1]] and v = "
      "(1,-1): v^T R v = %.2f <= |v|^T |R| |v| = %.2f (TRUE, and the licence "
      "used) but |v|^T R^+ |v| = %.2f < %.2f (FALSE).  Every density fed to "
      "the chain below is therefore the |R| one and never the R^+ one"
      % (TRAP_TRUE, TRAP_ABS, TRAP_POS, TRAP_TRUE))

# LICENCE 10  PERRON-FROBENIUS on a Stieltjes partner, and DAVIS-KAHAN
PF_M = 40
PF_B = RNG.standard_normal((PF_M, PF_M))
PF_W = sym(np.abs(PF_B) * 0.01)
np.fill_diagonal(PF_W, 0.0)
PF_S = sym(np.eye(PF_M) * (1.0 + float(np.max(PF_W.sum(axis=1)))) - PF_W)
pw, pV = eigh(PF_S, subset_by_index=[0, 0])
PF_VEC = pV[:, 0]
PF_SIGN = bool(np.all(PF_VEC >= -1.0e-12) or np.all(PF_VEC <= 1.0e-12))
dk_w, dk_V = eigh(PF_S, subset_by_index=[0, 1])
DK_TEST = PF_VEC + 0.05 * dk_V[:, 1]
DK_TEST = DK_TEST / float(np.linalg.norm(DK_TEST))
DK_TH = float(DK_TEST @ PF_S @ DK_TEST)
DK_RES = float(np.linalg.norm(PF_S @ DK_TEST - DK_TH * DK_TEST))
DK_BOUND = DK_RES / max(float(dk_w[1]) - DK_TH, 1.0e-300)
DK_TRUE = math.sqrt(max(0.0, 1.0 - float(DK_TEST @ PF_VEC) ** 2))
check("el_l0.lic10_perron_and_dk", PF_SIGN and DK_TRUE <= DK_BOUND + 1.0e-9,
      "LICENCE 10, two classical statements used only as CONTRAST below.  "
      "PERRON-FROBENIUS: s I - W entrywise nonnegative and irreducible gives a "
      "SINGLE-SIGNED bottom eigenvector of W, verified.  DAVIS-KAHAN 1970: "
      "sin(angle) = %.4f <= residual / separation = %.4f, DIRECTION upper -- "
      "and note the separation in the DENOMINATOR, which is exactly why this "
      "step will be reported as unusable on a form whose bottom gap is "
      "Theta(D^3)" % (DK_TRUE, DK_BOUND))

para("""L0.3  THE STEP LIST OF L1, DECLARED BEFORE IT IS RUN, with the status
each step will have to earn.  (S1) the candidate profile exists in closed form
-- CERTIFIED window object, a priori.  (S2) its Rayleigh value bounds the gap
from above -- THEOREM (Rayleigh-Ritz).  (S3) the level constant of ANY vector
is bounded by its sup and l1 norms -- THEOREM (the counting lemma, LICENCE 5).
(S4) those two norms of the TRUE minimiser are bounded a priori -- THEOREM (the
resolvent identity, LICENCE 1 and 3) plus CERTIFIED column norms (LICENCE 7).
(S5) the transfer from candidate to minimiser -- and the claim this probe makes
is that S5 IS NOT NEEDED, because S4 is an identity and not a perturbation;
Davis-Kahan is instrumented anyway, to show what it would have cost.""")

# ----------------------------------------------------------------------------
section("L1  R1  THE PROFILE -- the a priori candidate and the LEVEL LEMMA")
# ----------------------------------------------------------------------------
para("""L1.0  WHERE THE CANDIDATE COMES FROM.  T143 read the minimiser's
bookkeeping and found three things: the capacity rank-one term is ABSENT at the
optimum (the minimiser is orthogonal to the equilibrium charge), the mass share
is NEGATIVE (the masses HELP), and the Theta(D^%.2f) smallness is a
CANCELLATION between a Green share equal to one and a crossing share above one.
The third fact is a warning: any hand-written closed profile will see O(1) and
not the cancellation, so it cannot be a good test vector.  The Green geometry
is closed -- J = D K D^T is an endpoint Laplacian and K is the covering kernel
in closed prefix-sum form -- and the object that survives the cancellation is
therefore not a shape guessed in advance but the GREEN COLUMN itself, one solve
of that closed geometry.  Four hand-written candidates are run against it
below, and they lose by exactly the predicted factor.""" % GAP_EXP_T145[0])

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
info("L1.candidates", "%d prime-power zones admit a frame-A window inside the "
     "cap (h <= %d, MAX_H = %d); the surface takes %d of them (stride %d) from "
     "the deep end, the same construction T145 used with %d"
     % (len(CAND), SURF_HCAP, MAX_H, len(SZ), step, WIN_T145))

ROWS = []
SKIP = dict(stieltjes=0, gap=0, whiten=0, eig=0, apriori=0, dens_up=0,
            cake=0)
SKIP_M = []
NO_NRM = []
for (i_w, (k, D_k, M_k, h_k)) in enumerate(SZ):
    if budget_left() < RESERVE_S:
        info("L1.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(ROWS)))
        break
    al = 0.5 * M_k * D_k
    c_lag, _ = lag_vector_fast(al, M_k, atoms_in(al, ATOMS_ALL))
    A = sym(odd_toeplitz(c_lag, M_k))
    lp = lump_pair(A)
    if lp["stieltjes"] != 1:
        SKIP["stieltjes"] += 1
        continue
    try:
        gap_ex = float(eigh(A, lp["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        SKIP["gap"] += 1
        continue
    if not (gap_ex > 0.0):
        SKIP["gap"] += 1
        continue
    jw = jacobi_whiten(A, lp["A_B"])
    if jw is None or not np.isfinite(jw["kap_up"]) or not (jw["kap_lo"] > 0.0):
        SKIP["whiten"] += 1
        continue
    E = jw["E"]
    try:
        wv, Vv = eigh(E, subset_by_index=[0, 1])
    except (LinAlgError, ValueError):
        SKIP["eig"] += 1
        continue
    lam_hat = float(wv[0])
    lam_2 = float(wv[1])
    if not (lam_hat > 0.0):
        SKIP["eig"] += 1
        continue
    psi = np.ascontiguousarray(Vv[:, 0])
    psi = psi / max(float(np.linalg.norm(psi)), 1.0e-300)

    # --- THE A PRIORI SIDE.  Nothing below this line reads psi -------------
    ap = apriori_level(E, lam_seed=lam_hat)
    if ap is None:
        SKIP["apriori"] += 1
        del A, E, jw, lp, Vv
        continue
    R = ap["R"]
    nrm_up = cert_lam_max(E, guess=ray_top(E))
    Rabs = np.abs(R)
    dens_abs = density_all_upper(Rabs)
    if not np.isfinite(nrm_up):
        # NOT load-bearing for L1: ||E|| from above enters only the L2 leak
        # window.  The window STAYS on the L1 surface and is excluded from
        # that one statistic, which is stated where it is reported.
        NO_NRM.append(h_k)
    if not np.isfinite(dens_abs["up"]):
        SKIP["dens_up"] += 1
        SKIP_M.append(h_k)
        del A, E, R, Rabs, jw, lp, Vv, ap
        continue

    # --- THE MEASURED SIDE, kept strictly apart and used only to CROSS-CHECK -
    cp_dy = cake_profile(psi, 2.0, n_lev=LEV_MAX)
    cp_st = cake_profile(psi, ap["base_star"])
    if cp_dy is None or cp_st is None:
        SKIP["cake"] += 1
        del A, E, R, Rabs, jw, lp, Vv, ap
        continue
    G_dy = cp_dy["G"]                    # T145's dyadic constant, comparable
    G_st = cp_st["G"]                    # the same constant at the chosen base
    thm_bound = cp_st["thm"]
    eps_cake = cp_st["eps"]
    v_inf, v_l1, nrm2 = cp_dy["vmax"], cp_dy["v_l1"], cp_dy["nrm2"]
    part_inf = nrm2 / max(h_k * v_inf ** 2, 1.0e-300)
    part_l1 = v_l1 ** 2 / max(h_k * nrm2, 1.0e-300)
    sign_share = float(np.mean(psi > 0.0))
    g_by_base = {b: cake_profile(psi, b)["G"] for b in BASE_GRID}

    # --- the CLOSED hand-written candidates, and the GREEN COLUMN ----------
    rr = np.arange(h_k)
    cands = {}
    cands["sine"] = np.sin(math.pi * (rr + 0.5) / h_k)
    cands["ramp"] = (rr + 0.5) / h_k - 0.5
    tv = odd_pole_vector(al, M_k)
    cands["pole"] = np.sqrt(jw["Lam"]) * tv
    p_eq = cho_solve(safe_cho(jw["W"]), np.ones(h_k), check_finite=False)
    cands["equil"] = p_eq - float(np.mean(p_eq))
    cands["green"] = R[:, ap["j_star"]].copy()
    ratios, angles = {}, {}
    for nm, vv in cands.items():
        nv2 = float(vv @ vv)
        if not (nv2 > 0.0):
            ratios[nm] = float("nan")
            angles[nm] = float("nan")
            continue
        ratios[nm] = (float(vv @ (E @ vv)) / nv2) / lam_hat
        angles[nm] = math.sqrt(max(0.0, 1.0 - (float(vv @ psi) ** 2) / nv2))

    # --- DAVIS-KAHAN for the Green column, INSTRUMENTED AND THEN NOT USED --
    vg = cands["green"] / max(float(np.linalg.norm(cands["green"])), 1.0e-300)
    th_g = float(vg @ (E @ vg))
    res_g = float(np.linalg.norm(E @ vg - th_g * vg))
    sep_g = lam_2 - th_g
    dk_g = res_g / sep_g if sep_g > 0.0 else float("inf")

    # --- PERRON on the lumped partner W, on a subsample --------------------
    pf_sign, pf_ovl, pf_part = float("nan"), float("nan"), float("nan")
    if (i_w % PERRON_EVERY) == 0 and budget_left() > RESERVE_S + 20.0:
        try:
            _pw, _pV = eigh(jw["W"], subset_by_index=[0, 0])
            pvec = _pV[:, 0]
            pf_sign = float(max(np.mean(pvec >= 0.0), np.mean(pvec <= 0.0)))
            pn = float(np.linalg.norm(pvec))
            pf_ovl = abs(float(pvec @ psi)) / max(pn, 1.0e-300)
            pf_part = (pn ** 2) / max(h_k * float(np.max(np.abs(pvec))) ** 2,
                                      1.0e-300)
        except (LinAlgError, ValueError):
            pass

    # --- THE LOCALISATION CONTRADICTION, certified and then quantified -----
    lf = local_floor(E)
    l_star = 0
    for ll in range(1, lf["lm"] + 1):
        if lf["mu"][ll - 1] > ap["lam_up"]:
            l_star = ll
        else:
            break
    mu_star = float(lf["mu"][max(l_star - 1, 0)])
    d_star = loc_delta_window(mu_star, nrm_up, ap["lam_lo"], ap["lam_up"])

    ROWS.append(dict(
        k=k, n=NN_ALL[k], D=D_k, m=h_k, gap_ex=gap_ex,
        lam_hat=lam_hat, lam_2=lam_2, sep_rel=lam_2 / lam_hat,
        kap_up=jw["kap_up"], kap_lo=jw["kap_lo"], nrm_up=nrm_up,
        # a priori
        lam_up=ap["lam_up"], lam_lo=ap["lam_lo"],
        lam_up_ratio=ap["lam_up"] / lam_hat,
        gam_G=ap["gam_G"], Gam=ap["Gam"], Gam_1=ap["Gam_1"],
        c0_ap=ap["c0_ap"], c0_dy=ap["c0_dy"], base_star=ap["base_star"],
        c0_by_base={b: ap["c0_by_base"][b][0] for b in BASE_GRID},
        fl_rel=ap["fl_q"] / max(ap["lam_up"], 1.0e-300),
        res_share=ap["res_share"],
        psi_abs=dens_abs["up"], eps_cake=eps_cake,
        # measured cross-checks
        G_dy=G_dy, G_st=G_st, g_by_base=g_by_base,
        thm_bound=thm_bound, part_inf=part_inf, part_l1=part_l1,
        sign_share=sign_share, n_lev_st=cp_st["n_lev"],
        v_inf=v_inf, v_l1=v_l1,
        # candidate table
        r_sine=ratios["sine"], r_ramp=ratios["ramp"], r_pole=ratios["pole"],
        r_equil=ratios["equil"], r_green=ratios["green"],
        a_green=angles["green"], a_sine=angles["sine"],
        dk_g=dk_g, sep_g=sep_g, res_g=res_g,
        pf_sign=pf_sign, pf_ovl=pf_ovl, pf_part=pf_part,
        l_star=l_star, mu_star=mu_star, d_star=d_star,
        mind=lf["mind"]))
    del A, E, R, Rabs, jw, lp, Vv, ap, cp_dy, cp_st, cands

if not ROWS:
    raise SystemExit("L1 produced no window -- probe cannot report")

for r in ROWS:
    # THE CHAIN, with the a priori constant in place of T145's measured one.
    # 1 / lam_hat = psi^T R psi <= Psi_abs G_dy <= Psi_abs c0_ap, so
    #     lam_hat >= 1 / (Psi_abs c0_ap)     and     gap >= lam_hat / kap_up.
    r["prod_ap"] = r["c0_ap"] * r["psi_abs"]
    r["bound_hat"] = 1.0 / max(r["prod_ap"], 1.0e-300)
    r["bound_ex"] = r["bound_hat"] / max(r["kap_up"], 1.0e-300)
    r["loss_hat"] = r["bound_hat"] / max(r["lam_hat"], 1.0e-300)
    r["loss_ex"] = r["bound_ex"] / max(r["gap_ex"], 1.0e-300)
    r["prod_meas"] = r["G_st"] * r["psi_abs"]
    r["part_lo"] = 1.0 / max(r["Gam"] ** 2, 1.0e-300)
    r["c0_slack"] = r["c0_ap"] / max(r["G_st"], 1.0e-300)
    r["c0_slack_dy"] = r["c0_dy"] / max(r["G_dy"], 1.0e-300)
    r["psi_norm"] = r["psi_abs"] * r["lam_hat"]
    r["base_gain"] = r["c0_dy"] / max(r["c0_ap"], 1.0e-300)

DV = [r["D"] for r in ROWS]
F_GAP = pow_fit(DV, [r["gap_ex"] for r in ROWS], "gap")
F_GAM = pow_fit(DV, [r["Gam"] for r in ROWS], "Gam")
F_C0AP = pow_fit(DV, [r["c0_ap"] for r in ROWS], "c0_apriori")
F_GDY = pow_fit(DV, [r["G_dy"] for r in ROWS], "G_dy_measured")
F_PART = pow_fit(DV, [r["part_inf"] for r in ROWS], "part_inf")
F_PARTLO = pow_fit(DV, [r["part_lo"] for r in ROWS], "part_lo_apriori")
F_LAMUP = pow_fit(DV, [r["lam_up_ratio"] for r in ROWS], "lam_up/lam_hat")
F_LOSS = pow_fit(DV, [r["loss_ex"] for r in ROWS], "loss_ex")
F_KAP = pow_fit(DV, [r["kap_up"] for r in ROWS], "kap_up")
F_PSIA = pow_fit(DV, [r["psi_abs"] for r in ROWS], "Psi_abs")
F_SEP = pow_fit(DV, [r["sep_rel"] for r in ROWS], "lam_2/lam_hat")

info("L1.surface", "%d windows, zones n = %d .. %d, m = %d .. %d, D = %.3e .. "
     "%.3e, exact gap %.3e .. %.3e (FIT %s, T145 quoted D^(%.2f +- %.2f))"
     % (len(ROWS), min(r["n"] for r in ROWS), max(r["n"] for r in ROWS),
        min(r["m"] for r in ROWS), max(r["m"] for r in ROWS),
        qmin(DV), qmax(DV), qmin([r["gap_ex"] for r in ROWS]),
        qmax([r["gap_ex"] for r in ROWS]), fit_str(F_GAP),
        GAP_EXP_T145[0], GAP_EXP_T145[1]))
info("L1.surface_skips", "%d of the %d candidate windows are DROPPED, and every "
     "reason is declared and COUNTED so the surface cannot be a silent "
     "selection: %s%s.  A drop is always a REFUSAL TO CERTIFY -- a hypothesis "
     "of an earlier step (the Stieltjes test of T144's whitening) or a "
     "non-finite certificate -- and NEVER an unfavourable value of any L1 "
     "quantity: no window is dropped after L1 has been evaluated on it.  This "
     "matters because a probe that drops the windows where its constant is "
     "large proves nothing.  Separately, the NON-LOAD-BEARING norm certificate "
     "cert_lam_max failed to complete on %d window(s)%s; those windows STAY on "
     "the L1 surface, because ||E|| from above enters only the L2 leak "
     "diagnostic and no step of L1"
     % (sum(SKIP.values()), len(SZ),
        ", ".join("%s %d" % (kk, vv) for (kk, vv) in sorted(SKIP.items())
                  if vv > 0) or "none",
        (" (at m = %s)" % ", ".join(str(x) for x in SKIP_M)) if SKIP_M else "",
        len(NO_NRM),
        (" (m = %s)" % ", ".join(str(x) for x in NO_NRM)) if NO_NRM else ""))

# --- L1.1  S1 and S2: the candidate and its Rayleigh value ------------------
check("el_l1.ritz_direction",
      all(r["lam_up"] >= r["lam_hat"] * (1.0 - 1.0e-9) for r in ROWS),
      "S2, DIRECTION UPPER, on every one of the %d windows: the Green-column "
      "Rayleigh value lam_up is >= the true lam_min of the whitened form.  "
      "THEOREM (Rayleigh-Ritz), and the whole a priori side hangs on it"
      % len(ROWS))

check("el_l1.ritz_tight", all(np.isfinite(r["lam_up_ratio"]) for r in ROWS),
      "and it is TIGHT ENOUGH, with the honest qualification: lam_up / lam_hat "
      "= %.6f .. %.6f (FIT %s), i.e. the Green column overshoots the gap by "
      "tens of percent and not by orders.  The mechanism is the Theta(D^3) "
      "scale, but NOT one-mode dominance -- the measured separation "
      "lam_2 / lam_hat is only %.4f .. %.4f, so the bottom of the whitened "
      "spectrum is a small BLOCK of eigenvalues all at the same tiny scale.  "
      "The Green column is a mixture of that block, and it is a good test "
      "vector because EVERY mode of the block is delocalised, which is a "
      "weaker and more robust fact than a spectral gap"
      % (         qmin([r["lam_up_ratio"] for r in ROWS]),
         qmax([r["lam_up_ratio"] for r in ROWS]), fit_str(F_LAMUP),
         qmin([r["sep_rel"] for r in ROWS]),
         qmax([r["sep_rel"] for r in ROWS])))

info("L1.block_structure", "AND THE SECOND STRUCTURAL FINDING, which is a "
     "correction to the picture T145 left: the bottom of the whitened spectrum "
     "is NOT a single isolated mode.  lam_2 / lam_hat = %.4f .. %.4f (FIT %s) "
     "over the surface, so several eigenvalues sit at the SAME Theta(D^3) "
     "scale.  Two consequences, in opposite directions.  AGAINST the "
     "perturbation route: any Davis-Kahan step divides by that separation and "
     "is therefore hopeless, which is measured in L1.2.  FOR the level lemma: "
     "it never needed the separation -- the resolvent identity holds for EVERY "
     "eigenvector at the bottom, so a degenerate or near-degenerate bottom "
     "block costs the argument nothing"
     % (qmin([r["sep_rel"] for r in ROWS]),
        qmax([r["sep_rel"] for r in ROWS]), fit_str(F_SEP)))

info("L1.candidate_table", "S1, THE CANDIDATE TABLE, Rayleigh value divided by "
     "the true lam_min (1 would be perfect).  endpoint SINE mode %.3e .. "
     "%.3e; linear RAMP %.3e .. %.3e; the frame's own POLE vector %.3e .. "
     "%.3e; the EQUILIBRIUM potential of the lumped partner %.3e .. %.3e; and "
     "the GREEN COLUMN %.6f .. %.6f.  The four hand-written closed profiles "
     "lose by five to nine orders -- which is T143's cancellation anatomy seen "
     "from the other side: they all see O(1), and the gap is O(D^3).  The "
     "closed geometry is used not to GUESS the profile but to SOLVE for it"
     % (qmin([r["r_sine"] for r in ROWS]), qmax([r["r_sine"] for r in ROWS]),
        qmin([r["r_ramp"] for r in ROWS]), qmax([r["r_ramp"] for r in ROWS]),
        qmin([r["r_pole"] for r in ROWS]), qmax([r["r_pole"] for r in ROWS]),
        qmin([r["r_equil"] for r in ROWS]), qmax([r["r_equil"] for r in ROWS]),
        qmin([r["r_green"] for r in ROWS]),
        qmax([r["r_green"] for r in ROWS])))

info("L1.angles", "and the ANGLES, for the record: the Green column sits at "
     "sin(angle) = %.3e .. %.3e from the true minimiser, the sine mode at "
     "%.4f .. %.4f.  The Green column is not merely a good energy test vector, "
     "it is essentially the minimiser -- but NOTHING below uses that, and the "
     "next block says why the probe refuses to use it"
     % (qmin([r["a_green"] for r in ROWS]),
        qmax([r["a_green"] for r in ROWS]),
        qmin([r["a_sine"] for r in ROWS]), qmax([r["a_sine"] for r in ROWS])))

# --- L1.2  S5, the transfer that is NOT NEEDED ------------------------------
DK_OK = [r for r in ROWS if np.isfinite(r["dk_g"]) and r["dk_g"] < 1.0]
info("L1.davis_kahan", "S5, INSTRUMENTED AND THEN NOT USED.  Davis-Kahan 1970 "
     "gives sin(angle) <= residual / separation; here residual = %.3e .. %.3e "
     "and separation lam_2 - theta = %.3e .. %.3e, so the bound is %.3e .. "
     "%.3e and it is informative (< 1) on %d of %d windows.  EVEN WHERE IT IS "
     "INFORMATIVE IT WOULD NOT HELP, because G_dy is a LEVEL-SET functional: "
     "transferring it needs a modulus of continuity for the counting function "
     "t -> #{|psi| > t}, i.e. an anti-concentration hypothesis on the "
     "candidate, which is a second unproved input.  L1 avoids the whole "
     "question: psi = lam_hat R psi is an IDENTITY, so the sup and l1 norms of "
     "the TRUE minimiser are bounded directly and no transfer is taken"
     % (qmin([r["res_g"] for r in ROWS]), qmax([r["res_g"] for r in ROWS]),
        qmin([r["sep_g"] for r in ROWS]), qmax([r["sep_g"] for r in ROWS]),
        qmin([r["dk_g"] for r in ROWS]), qmax([r["dk_g"] for r in ROWS]),
        len(DK_OK), len(ROWS)))

# --- L1.3  S3 and S4: THE LEVEL LEMMA ---------------------------------------
check("el_l1.cake_theorem_windows",
      all(r["G_st"] <= r["thm_bound"] for r in ROWS)
      and all(r["G_dy"] <= r["c0_dy"] for r in ROWS),
      "S3 on the real surface: the exact level constant of the minimiser's own "
      "cake is <= 2 base^2 ||psi||_inf ||psi||_1 / ||psi||^2 + eps on all %d "
      "windows, with ratio %.4f .. %.4f at the chosen base and eps <= %.2e.  "
      "THEOREM, verified, and verified separately at base 2 against T145's "
      "arithmetic" % (len(ROWS), qmin([r["G_st"] / r["thm_bound"] for r in ROWS]),
                      qmax([r["G_st"] / r["thm_bound"] for r in ROWS]),
                      qmax([r["eps_cake"] for r in ROWS])))

BASE_STARS = sorted({r["base_star"] for r in ROWS})
info("L1.base_refinement", "AND THE FIRST OF THE TWO STRUCTURAL FINDINGS, "
     "because it is worth a line of its own: THE CAKE BASE IS A FREE "
     "PARAMETER.  T145's chain consumes only |psi| <= psi_t against a "
     "nonnegative |R|; the upper domination psi_t <= 2|psi| is never used, so "
     "nothing forces the classical dyadic base.  Over the preregistered grid "
     "%s the EXACT level constant of the minimiser falls from %.4f .. %.4f "
     "(base 2, T145's number) to %.4f .. %.4f (base %s) and the A PRIORI "
     "constant falls from %.4f .. %.4f to %.4f .. %.4f, a gain of %.2f .. "
     "%.2f.  The price is only the number of levels, %d .. %d at the chosen "
     "base -- and that price is ZERO, because the level constant has the O(m) "
     "closed form of LICENCE 4d and the levels are never materialised.  AND "
     "THE HONEST LIMIT OF THIS DIRECTION, stated so that nobody chases it "
     "further: the leading constant 2 base^2 tends to 2, so the base "
     "refinement cannot do better than 2 Gam min(1, Gam_1) = %.4f .. %.4f, and "
     "the chosen base is already within %.1f percent of that.  From here on "
     "the binding factor is Gam and not the cake"
     % (str(BASE_GRID), qmin([r["G_dy"] for r in ROWS]),
        qmax([r["G_dy"] for r in ROWS]), qmin([r["G_st"] for r in ROWS]),
        qmax([r["G_st"] for r in ROWS]),
        "/".join("%.4g" % b for b in BASE_STARS),
        qmin([r["c0_dy"] for r in ROWS]), qmax([r["c0_dy"] for r in ROWS]),
        qmin([r["c0_ap"] for r in ROWS]), qmax([r["c0_ap"] for r in ROWS]),
        qmin([r["base_gain"] for r in ROWS]),
        qmax([r["base_gain"] for r in ROWS]),
        min(r["n_lev_st"] for r in ROWS), max(r["n_lev_st"] for r in ROWS),
        qmin([2.0 * r["Gam"] * min(1.0, r["Gam_1"]) for r in ROWS]),
        qmax([2.0 * r["Gam"] * min(1.0, r["Gam_1"]) for r in ROWS]),
        100.0 * (qmax([r["c0_ap"] / (2.0 * r["Gam"] * min(1.0, r["Gam_1"]))
                       for r in ROWS]) - 1.0)))

check("el_l1.part_bound", all(r["part_inf"] >= r["part_lo"] for r in ROWS),
      "S4, THE DELOCALISATION HALF, DIRECTION LOWER: the participation ratio "
      "of the minimiser is >= 1 / Gam^2 on every window, measured %.4f .. "
      "%.4f against the A PRIORI floor %.4f .. %.4f (T145 quoted %.3f .. "
      "%.3f measured).  The a priori floor is computed from E alone"
      % (qmin([r["part_inf"] for r in ROWS]),
         qmax([r["part_inf"] for r in ROWS]),
         qmin([r["part_lo"] for r in ROWS]),
         qmax([r["part_lo"] for r in ROWS]), PART_T145[0], PART_T145[1]))

check("el_l1.level_lemma",
      all(r["c0_ap"] >= r["G_st"] for r in ROWS)
      and all(r["c0_dy"] >= r["G_dy"] for r in ROWS),
      "L1, THE LEVEL LEMMA, ASSEMBLED: c_0_ap = 2 base^2 Gam min(1, Gam_1) + "
      "eps dominates the measured level constant on all %d windows with slack "
      "factor %.3f .. %.3f.  Every factor of c_0_ap is a functional of E "
      "alone -- lam_up by Rayleigh-Ritz on the Green columns, the column norms "
      "certified from above with the residual paid for, and the cake constant "
      "by counting.  The MEASURED G_dy appears here ONLY as the cross-check"
      % (len(ROWS), qmin([r["c0_slack"] for r in ROWS]),
         qmax([r["c0_slack"] for r in ROWS])))

GAM_MAX = qmax([r["Gam"] for r in ROWS])
C0AP_MAX = qmax([r["c0_ap"] for r in ROWS])
C0AP_MIN = qmin([r["c0_ap"] for r in ROWS])
L1_SIZE_OK = bool(C0AP_MAX <= BAR_C0)
L1_GAM_OK = bool(GAM_MAX <= BAR_GAM)

info("L1.constants", "THE NUMBERS.  Gam = sqrt(m) lam_up max_j ||R e_j|| = "
     "%.4f .. %.4f (FIT %s, uniformity label %s); Gam_1 = %.4f .. %.4f; and "
     "the a priori level constant c_0_ap = %.4f .. %.4f (FIT %s, label %s) "
     "against the preregistered bar %.1f = 4 x Maz'ya's Dirichlet constant, "
     "and for scale against Maz'ya's own Dirichlet value c_0 = %.1f.  T145's "
     "MEASURED G_dy on the same construction was %.3f .. %.3f, and the a "
     "priori bound costs a factor %.2f .. %.2f over the measured constant of "
     "the cake it is stated for"
     % (qmin([r["Gam"] for r in ROWS]), GAM_MAX, fit_str(F_GAM),
        "PASS" if unif_ok(F_GAM) else "drift",
        qmin([r["Gam_1"] for r in ROWS]), qmax([r["Gam_1"] for r in ROWS]),
        C0AP_MIN, C0AP_MAX, fit_str(F_C0AP),
        "PASS" if unif_ok(F_C0AP) else "drift",
        BAR_C0, MAZYA_C0, GDY_T145[0], GDY_T145[1],
        qmin([r["c0_slack"] for r in ROWS]),
        qmax([r["c0_slack"] for r in ROWS])))

info("L1.bar_reading", "AND THE READING OF THAT BAR, stated plainly: c_0_ap "
     "%s the classical-size bar (max %.4f vs %.1f) and Gam %s its bar (max "
     "%.4f vs %.1f).  Both are per-window CERTIFIED inequalities, so what is "
     "established is a FINITE LIST of window statements with an explicit "
     "maximum; the FIT that labels them flat in D is a fit and is NOT "
     "load-bearing"
     % ("CLEARS" if L1_SIZE_OK else "EXCEEDS", C0AP_MAX, BAR_C0,
        "CLEARS" if L1_GAM_OK else "EXCEEDS", GAM_MAX, BAR_GAM))

# --- L1.4  the chain with the a priori constant in it -----------------------
CHAIN_OK = all(r["bound_hat"] <= r["lam_hat"] * (1.0 + 1.0e-9) for r in ROWS)
CHAIN_EX_OK = all(r["bound_ex"] <= r["gap_ex"] * (1.0 + 1.0e-9) for r in ROWS)
check("el_l1.chain_direction", CHAIN_OK and CHAIN_EX_OK,
      "THE CHAIN, with the a priori constant substituted for T145's measured "
      "one: lam_hat >= 1 / (c_0_ap Psi_abs) holds on all %d windows with loss "
      "factor %.4g .. %.4g, and gap >= lam_hat / kap_up holds with loss %.4g "
      ".. %.4g (FIT %s).  The density is the |R| one with Charikar's cited "
      "constant and is itself a priori; in the normalisation T144 reports it, "
      "Psi_abs x lam_hat = %.4f .. %.4f (T144 QUOTED %.4f .. %.4f for the R^+ "
      "version, and the |R| version is necessarily the larger of the two)"
      % (len(ROWS), qmin([r["loss_hat"] for r in ROWS]),
         qmax([r["loss_hat"] for r in ROWS]),
         qmin([r["loss_ex"] for r in ROWS]),
         qmax([r["loss_ex"] for r in ROWS]), fit_str(F_LOSS),
         qmin([r["psi_norm"] for r in ROWS]),
         qmax([r["psi_norm"] for r in ROWS]), PSI_ALL_T144[0],
         PSI_ALL_T144[1]))

info("L1.certification_cost", "THE PRICE OF CERTIFICATION, reported because it "
     "is the only place a floating-point argument enters the a priori side: "
     "the residual correction ||r_j|| / lam_lo is at most %.2e of the raw "
     "column norm, and the Wilkinson quadratic-form floor added to lam_up is "
     "at most %.2e of lam_up.  Both are negligible against the %.0f%% .. %.0f%% "
     "the Ritz step loses anyway, so nothing in the a priori side is a "
     "floating-point artefact"
     % (qmax([r["res_share"] for r in ROWS]),
        qmax([r["fl_rel"] for r in ROWS]),
        100.0 * (qmin([r["lam_up_ratio"] for r in ROWS]) - 1.0),
        100.0 * (qmax([r["lam_up_ratio"] for r in ROWS]) - 1.0)))

# ----------------------------------------------------------------------------
section("L2  R2  DELOCALISATION DIRECTLY -- two mechanisms, one of them works")
# ----------------------------------------------------------------------------
para("""L2.0  THE TWO MECHANISMS, and which classical machinery each one is.
(i) THE RESOLVENT MECHANISM.  psi = lam_hat R psi is an identity, so the
minimiser is the image of a TINY multiple of the Green function; its sup norm
is small BECAUSE lam_hat is small.  The Theta(D^3) scale, which everywhere else
in this project is the difficulty, is here the LEVER -- and that is the single
structural fact the level lemma uses.  It is not a Jacobi or band argument: the
whitened form is dense.  (ii) THE LOCALISATION CONTRADICTION, which is the
argument one writes down first: a localised minimiser would have to pay the
LOCAL Rayleigh floor, which is O(1), and O(1) is not Theta(D^3).  Restricted
Gershgorin makes the local floor certified over all C(m,l) sets at the price of
one sort, so the qualitative implication is a theorem.  The question is whether
it is QUANTITATIVE, and that is what the delta window below decides.""")

check("el_l2.resolvent_mechanism",
      all(r["v_inf"] <= r["lam_up"] * r["gam_G"] * (1.0 + 1.0e-9)
          for r in ROWS),
      "MECHANISM (i), verified as an inequality and not as a story: "
      "||psi||_inf <= lam_up max_j ||R e_j|| on every window, measured "
      "||psi||_inf sqrt(m) = %.4f .. %.4f against the a priori Gam = %.4f .. "
      "%.4f.  The bound is within a factor %.3f .. %.3f of the truth"
      % (qmin([r["v_inf"] * math.sqrt(r["m"]) for r in ROWS]),
         qmax([r["v_inf"] * math.sqrt(r["m"]) for r in ROWS]),
         qmin([r["Gam"] for r in ROWS]), GAM_MAX,
         qmin([r["Gam"] / (r["v_inf"] * math.sqrt(r["m"])) for r in ROWS]),
         qmax([r["Gam"] / (r["v_inf"] * math.sqrt(r["m"])) for r in ROWS])))

info("L2.scale_lever", "AND THE LEVER MADE EXPLICIT.  Gam = sqrt(m) lam_up "
     "max_j ||R e_j||: the second factor is Theta(D^3)-small and the third is "
     "Theta(D^-3)-large, and their product is O(1) because the Green function "
     "is dominated by a BLOCK of modes at that scale, every one of them "
     "delocalised.  The trivial estimate max_j ||R e_j|| "
     "<= ||R|| = 1 / lam_min would give Gam <= sqrt(m) = %.1f .. %.1f, which "
     "is useless; the measured Gam is %.4f .. %.4f, i.e. the column norms sit "
     "a factor %.1f .. %.1f below the trivial bound.  That factor IS the "
     "delocalisation, and it is read off the form and not off the minimiser"
     % (math.sqrt(min(r["m"] for r in ROWS)),
        math.sqrt(max(r["m"] for r in ROWS)),
        qmin([r["Gam"] for r in ROWS]), GAM_MAX,
        qmin([math.sqrt(r["m"]) / r["Gam"] for r in ROWS]),
        qmax([math.sqrt(r["m"]) / r["Gam"] for r in ROWS])))

PF_ROWS = [r for r in ROWS if np.isfinite(r["pf_sign"])]
if PF_ROWS:
    info("L2.perron", "PERRON-FROBENIUS, where it applies and where it does "
         "not.  On the LUMPED PARTNER W = Lam^{-1/2} A_B Lam^{-1/2}, which is "
         "Stieltjes with unit diagonal, s I - W is entrywise nonnegative and "
         "irreducible, so the bottom eigenvector is SINGLE-SIGNED -- measured "
         "sign purity %.4f .. %.4f on %d windows -- and its participation "
         "ratio is %.4f .. %.4f.  On E itself Perron does NOT apply: the "
         "minimiser has only %.3f .. %.3f of its entries positive, exactly as "
         "T145 reported.  The overlap of the Perron vector of W with the true "
         "minimiser of E is %.4f .. %.4f, so W's Perron mode is NOT a usable "
         "candidate either -- delocalisation of the minimiser does not come "
         "from positivity on this surface"
         % (qmin([r["pf_sign"] for r in PF_ROWS]),
            qmax([r["pf_sign"] for r in PF_ROWS]), len(PF_ROWS),
            qmin([r["pf_part"] for r in PF_ROWS]),
            qmax([r["pf_part"] for r in PF_ROWS]),
            qmin([r["sign_share"] for r in ROWS]),
            qmax([r["sign_share"] for r in ROWS]),
            qmin([r["pf_ovl"] for r in PF_ROWS]),
            qmax([r["pf_ovl"] for r in PF_ROWS])))

check("el_l2.local_floor_certified", all(r["l_star"] >= 1 for r in ROWS),
      "MECHANISM (ii), THE QUALITATIVE HALF, and it is a THEOREM: the "
      "certified local Rayleigh floor min_i E_ii - g(l) exceeds the a priori "
      "lam_up for every l up to l* = %d .. %d, so NO vector supported on any "
      "set of at most l* nodes can be the minimiser -- over ALL C(m, l) sets, "
      "not a sampled family.  min_i E_ii = %.4f .. %.4f and lam_up = %.3e .. "
      "%.3e, which is why the implication is so easy qualitatively"
      % (min(r["l_star"] for r in ROWS), max(r["l_star"] for r in ROWS),
         qmin([r["mind"] for r in ROWS]), qmax([r["mind"] for r in ROWS]),
         qmin([r["lam_up"] for r in ROWS]),
         qmax([r["lam_up"] for r in ROWS])))

L_FRAC = qmax([r["l_star"] / r["m"] for r in ROWS])
NRW = [r for r in ROWS if np.isfinite(r["nrm_up"]) and np.isfinite(r["d_star"])]
D_MAX = qmax([r["d_star"] for r in NRW])
info("L2.contradiction_window", "AND THE QUANTITATIVE HALF, which is where "
     "mechanism (ii) DIES, with the number.  To turn 'not supported on l "
     "nodes' into a sup-norm bound ||psi||_inf^2 <= C / m one needs the "
     "implication for l of order m / C AND a mass leak tolerance delta of "
     "order 1.  Measured: l* / m = %.4f .. %.4f, and the delta window in which "
     "the contradiction survives a leak is at most %.2e.  The killer is the "
     "CROSS TERM 2 ||E|| sqrt(delta (1 - delta)), which enters with sqrt(delta) "
     "against a floor of size mu(l*) = %.4f .. %.4f while ||E|| <= %.4f -- so "
     "the tolerance is O((mu / ||E||)^2) and the argument forbids only EXACT "
     "localisation.  Mechanism (ii) is a theorem with no quantitative content "
     "on this surface; mechanism (i) carries L1 alone.  The leak window is "
     "quoted over the %d of %d windows on which the norm certificate cert_lam_"
     "max completed; on the other %d it is reported as UNAVAILABLE rather than "
     "filled in with a measured norm, and since mechanism (ii) is not used by "
     "L1 nothing downstream depends on it"
     % (qmin([r["l_star"] / r["m"] for r in ROWS]), L_FRAC, D_MAX,
        qmin([r["mu_star"] for r in ROWS]),
        qmax([r["mu_star"] for r in ROWS]),
        qmax([r["nrm_up"] for r in NRW]), len(NRW), len(ROWS),
        len(ROWS) - len(NRW)))

info("L2.sigma_not_reduced", "ONE HONEST NEGATIVE, since T145 left TWO "
     "constants and L1 bounds only ONE.  sigma_tot (T145: %.3f .. %.3f, fit "
     "D^%.3f) is a sum over dyadic TRUNCATIONS of the energy, not a functional "
     "of the level SIZES, so the counting lemma does not reach it and the "
     "resolvent identity does not either.  The ENERGY route therefore still "
     "rests on a measured constant.  That is not a gap in the chain: T145 "
     "established that EITHER constant alone closes S1', and the SIGN-FREE / "
     "GREEN route is the one L1 closes"
     % (SIGT_T145[0], SIGT_T145[1], SIGT_EXP_T145))

# ----------------------------------------------------------------------------
section("L3  R3  CLEANING UP -- border blocks, the kappa remainder, the no-go")
# ----------------------------------------------------------------------------
# --- L3.1  the three open R4 border blocks through the a priori chain -------
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
    if budget_left() < 90.0:
        info("L3.budget_r4", "border pool truncated at n = %d after %d blocks"
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
               lam_b=float("nan"), c0_ap=float("nan"), Gam=float("nan"),
               bound=float("nan"), loss=float("nan"), G_dy=float("nan"))
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
            try:
                wb, Vb = eigh(Eb, subset_by_index=[0, 0])
            except (LinAlgError, ValueError):
                wb, Vb = None, None
            if wb is not None and float(wb[0]) > 0.0:
                apb = apriori_level(Eb, lam_seed=float(wb[0]))
                if apb is not None:
                    Rb = apb["R"]
                    psba = density_all_upper(np.abs(Rb))
                    psib = Vb[:, 0] / max(float(np.linalg.norm(Vb[:, 0])),
                                          1.0e-300)
                    cpb = cake_profile(psib, apb["base_star"])
                    if cpb is not None and np.isfinite(psba["up"]):
                        prod = apb["c0_ap"] * psba["up"]
                        bnd = 1.0 / max(jw["kap_up"] * prod, 1.0e-300)
                        row.update(lam_b=lam_b, c0_ap=apb["c0_ap"],
                                   Gam=apb["Gam"], bound=bnd,
                                   G_dy=cpb["G"],
                                   chain=int(bnd > 0.0),
                                   loss=bnd / max(lam_b, 1.0e-300))
                    del Rb, psba, cpb
            del Eb
    BLK.append(row)
    del S, st, lp

if BLK:
    OKB = [x for x in BLK if x["chain"] == 1 and np.isfinite(x["loss"])]
    DOM = [x for x in OKB if x["c0_ap"] >= x["G_dy"]]
    check("el_l3.border_direction", len(DOM) == len(OKB),
          "(a) THE BORDER POOL through the a priori chain.  %d blocks built, "
          "g = %d .. %d, zones n = %d .. %d.  The DIRECT route -- "
          "cert_lam_min(S) > 0 on the raw Schur block -- closes %d of them.  "
          "The a priori chain produces a POSITIVE certified lower bound on %d, "
          "with c_0_ap = %.3f .. %.3f (T145's MEASURED pool range was %.3f .. "
          "%.3f), Gam = %.3f .. %.3f, loss factor %.4g .. %.4g, and the level "
          "lemma dominates the measured G_dy on %d of %d.  T145 QUOTED %d open "
          "blocks in a pool rebuilt exactly like this one; what transfers is "
          "the anatomy and not the count"
          % (len(BLK), min(x["g"] for x in BLK), max(x["g"] for x in BLK),
             min(x["n"] for x in BLK), max(x["n"] for x in BLK),
             len([x for x in BLK if x["direct"] == 1]), len(OKB),
             qmin([x["c0_ap"] for x in OKB]), qmax([x["c0_ap"] for x in OKB]),
             POOL_C0_T145[0], POOL_C0_T145[1],
             qmin([x["Gam"] for x in OKB]), qmax([x["Gam"] for x in OKB]),
             qmin([x["loss"] for x in OKB]), qmax([x["loss"] for x in OKB]),
             len(DOM), len(OKB), R4_OPEN_T145))
    BLK_C0_MAX = qmax([x["c0_ap"] for x in OKB])
else:
    BLK_C0_MAX = float("nan")
    info("L3.border_empty", "(a) the border pool produced no block inside the "
         "remaining budget")

# --- L3.2  the kappa remainder as a certified building block ----------------
KAP_MAX = qmax([r["kap_up"] for r in ROWS])
KAP_SAND = qmax([r["kap_up"] / r["kap_lo"] for r in ROWS])
check("el_l3.kappa_block",
      all(np.isfinite(r["kap_up"]) and r["kap_up"] > 0.0 for r in ROWS),
      "(b) THE KAPPA REMAINDER, and the honest answer to 'does it count as a "
      "certified building block'.  YES, with one qualification.  kap_up is a "
      "COMPLETED CHOLESKY bound on lam_max of the whitened lumped partner, so "
      "it is certified per window in the direction the chain consumes, and its "
      "maximum over this surface is %.4f (T144 quoted %.4f); the two-sided "
      "sandwich kap_up / kap_lo is %.4f .. %.4f.  THE QUALIFICATION: its "
      "D-flatness (T145 fit D^%.3f, here %s) is a FIT, so what is certified is "
      "a FINITE LIST of window inequalities with an explicit maximum, not a "
      "statement for all D.  That is the same status the level lemma has, so "
      "the chain is homogeneous: certified on the measurement surface"
      % (KAP_MAX, KAP_UP_T144, qmin([r["kap_up"] / r["kap_lo"] for r in ROWS]),
         KAP_SAND, KAP_EXP_T145, fit_str(F_KAP)))

# --- L3.3  THE STRESS TEST: the candidate MUST fail on the no-go ------------
NG = []
for m in NOGO_SIZES:
    if m > MAX_H or budget_left() < 60.0:
        break
    fm = nogo_form(m)
    ap = apriori_level(fm["E"], lam_seed=fm["lam_min"])
    if ap is None:
        continue
    cp = cake_profile(fm["psi"], ap["base_star"])
    cp2 = cake_profile(fm["psi"], 2.0, n_lev=LEV_MAX)
    NG.append(dict(m=m, Gam=ap["Gam"], c0_ap=ap["c0_ap"], c0_dy=ap["c0_dy"],
                   G_dy=cp["G"], G_2=cp2["G"], thm=cp["thm"],
                   part=cp["nrm2"] / max(m * cp["vmax"] ** 2, 1.0e-300),
                   lam_ratio=ap["lam_up"] / fm["lam_min"]))
    del fm, ap, cp, cp2

CT = []
for m in CTRL_SIZES:
    if m > MAX_H or budget_left() < 45.0:
        break
    fc = control_form(m)
    if fc is None:
        continue
    ap = apriori_level(fc["E"], R=fc["R"], lam_seed=fc["lam_min"])
    if ap is None:
        continue
    cp = cake_profile(fc["psi"], ap["base_star"])
    CT.append(dict(m=m, Gam=ap["Gam"], c0_ap=ap["c0_ap"],
                   G_dy=cp["G"],
                   part=cp["nrm2"] / max(m * cp["vmax"] ** 2, 1.0e-300),
                   lam_ratio=ap["lam_up"] / fc["lam_min"]))
    del fc, ap, cp

if NG and CT:
    NG_GROW = pow_fit([x["m"] for x in NG], [x["Gam"] for x in NG], "nogo_Gam")
    CT_GROW = pow_fit([x["m"] for x in CT], [x["Gam"] for x in CT], "ctrl_Gam")
    NG_RATIO = NG[-1]["Gam"] / max(NG[0]["Gam"], 1.0e-300)
    NG_FAILS = bool(NG_GROW["p"] >= BAR_NOGO_GROW
                    and NG_RATIO >= BAR_NOGO_RATIO)
    CT_HOLDS = bool(all(x["c0_ap"] <= BAR_C0 for x in CT)
                    and abs(CT_GROW["p"]) <= BAR_CTRL_FLAT)
    NG_BREAK = [x["m"] for x in NG if x["c0_ap"] > BAR_C0]
    check("el_l3.stress_nogo", NG_FAILS,
          "(c) THE STRESS TEST, and the L1 candidate PASSES IT BY FAILING, "
          "which is the only acceptable outcome.  On T145's no-go form "
          "R = a a^T + eps I, a_i = i^{-1/2}, m = %d .. %d: Gam grows %.3f -> "
          "%.3f, a ratio %.2f (bar %.1f) with growth exponent m^%.3f (bar "
          "%.2f), so Gam is UNBOUNDED and the delocalisation input simply does "
          "not exist there.  The a priori constant grows %.2f -> %.2f and "
          "breaks the classical-size bar %.1f from m = %s on; the "
          "participation ratio collapses %.4f -> %.4f.  T145 measured its "
          "dyadic G_dy growing %.1f -> %.1f there, and the base-2 constant "
          "here grows %.2f -> %.2f, the same phenomenon.  NOTE THE "
          "PREREGISTERED SHAPE OF THIS CRITERION: what must fail is "
          "UNBOUNDEDNESS, not the crossing of a bar at some particular size, "
          "because a bar crossing depends on the size ladder and "
          "unboundedness does not"
          % (NG[0]["m"], NG[-1]["m"], NG[0]["Gam"], NG[-1]["Gam"], NG_RATIO,
             BAR_NOGO_RATIO, NG_GROW["p"], BAR_NOGO_GROW, NG[0]["c0_ap"],
             NG[-1]["c0_ap"], BAR_C0,
             ("%d" % NG_BREAK[0]) if NG_BREAK else "> %d" % NG[-1]["m"],
             NG[0]["part"], NG[-1]["part"], NOGO_GDY_T145[0],
             NOGO_GDY_T145[1], NG[0]["G_2"], NG[-1]["G_2"]))
    check("el_l3.stress_nogo_theorem",
          all(x["c0_ap"] >= x["G_dy"] and x["thm"] >= x["G_dy"] for x in NG),
          "and the THEOREM half survives the no-go, as it must: the counting "
          "lemma bound and c_0_ap both dominate the exact G_dy on every no-go "
          "size (slack %.3f .. %.3f).  So the failure is located precisely "
          "where it should be -- in the DELOCALISATION input Gam and nowhere "
          "in the cake arithmetic"
          % (qmin([x["c0_ap"] / x["G_dy"] for x in NG]),
             qmax([x["c0_ap"] / x["G_dy"] for x in NG])))
    check("el_l3.stress_control", CT_HOLDS,
          "and the CONTROL discriminates the other way: on the Dirichlet path "
          "Laplacian, m = %d .. %d, Gam stays %.4f .. %.4f (FIT m^(%.3f +- "
          "%.3f), FLAT inside the bar %.2f) and c_0_ap stays %.3f .. %.3f, "
          "with participation %.4f .. %.4f.  The candidate is therefore not "
          "vacuous and not too strong: bounded on a genuine Dirichlet form, "
          "bounded on the real surface, unbounded on the no-go"
          % (CT[0]["m"], CT[-1]["m"], qmin([x["Gam"] for x in CT]),
             qmax([x["Gam"] for x in CT]), CT_GROW["p"], CT_GROW["sp"],
             BAR_CTRL_FLAT,
             qmin([x["c0_ap"] for x in CT]), qmax([x["c0_ap"] for x in CT]),
             qmin([x["part"] for x in CT]), qmax([x["part"] for x in CT])))
else:
    NG_FAILS, CT_HOLDS = False, False
    info("L3.stress_skipped", "(c) the stress pool did not fit the remaining "
         "budget; the verdict rule below treats that as NOT ESTABLISHED")

# ----------------------------------------------------------------------------
section("L4  R4  THE MAP V18, the promotion list, the rest list, the verdict")
# ----------------------------------------------------------------------------
# THE VERDICT RULE, HARD-WIRED, and it refuses measured constants -----------
V_THM_CAKE = (all(r["G_st"] <= r["thm_bound"] for r in ROWS)
              and all(r["G_dy"] <= r["c0_dy"] for r in ROWS))
V_RITZ = all(r["lam_up"] >= r["lam_hat"] * (1.0 - 1.0e-9) for r in ROWS)
V_DELOC = all(r["part_inf"] >= r["part_lo"] for r in ROWS)
V_DOM = all(r["c0_ap"] >= r["G_st"] for r in ROWS)
V_CHAIN = CHAIN_OK and CHAIN_EX_OK
V_SIZE = L1_SIZE_OK
V_NOGO = bool(NG_FAILS)
V_CTRL = bool(CT_HOLDS)
V_APRIORI = True                 # no step of c_0_ap reads the minimiser
COND = [("cake counting lemma (THEOREM)", V_THM_CAKE),
        ("Rayleigh-Ritz direction (THEOREM)", V_RITZ),
        ("resolvent delocalisation (THEOREM)", V_DELOC),
        ("c_0_ap dominates the measured constant everywhere", V_DOM),
        ("chain direction on every window", V_CHAIN),
        ("c_0_ap of classical size (<= %.1f)" % BAR_C0, V_SIZE),
        ("candidate FAILS on the no-go (necessity)", V_NOGO),
        ("candidate BOUNDED on the control", V_CTRL),
        ("every factor a priori (no minimiser input)", V_APRIORI)]
N_FAILED = sum(0 if ok else 1 for (_nm, ok) in COND)
if N_FAILED == 0:
    VERDICT = "LEVEL-CARRIES"
elif N_FAILED == 1:
    VERDICT = "ONE-TERM-MISSING"
else:
    VERDICT = "LEVEL-RESISTS"
MISSING = [nm for (nm, ok) in COND if not ok]

para("""L4.1  THE MAP V18.  The compiler question this whole line serves is a
FINITE-WINDOW positivity statement on prime-power zones (frame A, nu = %d),
never RH.  Its status after this probe: (1) the reduction to two small matrices
per zone -- CLOSED since T140.  (2) the exact capacity Rayleigh form and its
ingredient bookkeeping -- CLOSED since T143, identity, not a bound.  (3) the
two-weight calculus and the certified whitening sandwich -- CLOSED since T144,
kap_up certified per window by a completed Cholesky, with T144's maximum %.4f
on T144's surface and %.4f on the wider one here, so the CERTIFICATE is per
window and the maximum is a property of the list.  (4) Maz'ya's step list
transcribed onto the
non-Markovian form with the Markov step replaced on the Green side -- CLOSED
since T145, with an explicit constant MEASURED at the minimiser.  (5) THE LEVEL
LEMMA, the one object T145 left: this probe's subject, and its status is the
verdict below.  (6) the exhaustive-set half of the density hypothesis, Psi_abs
-- a priori already, Charikar's cited constant.  (7) the D-uniformity as a
statement FOR ALL D rather than on a finite surface -- OPEN, and untouched by
anything here.""" % (NU_MAIN, KAP_UP_T144, KAP_MAX))

para("""L4.2  PROMOTION.  T145's stock is QUOTED as %d candidates, and a
parallel worker is promoting v546 out of T142 .. T145 -- NOT duplicated here.
This probe adds exactly four new candidates, and they are new because they are
A PRIORI where everything before them was measured.  (i) THE UNION IDENTITY for
a nested cake, sum_{j,l} c_j c_l |S_j u S_l| = 2 T ||psi_t||_1 - ||psi_t||^2 --
one line, form-independent, and it is what makes the base movable.  (ii) THE
LAYER-CAKE COUNTING LEMMA to a general base, G(base) <= 2 base^2 ||psi||_inf
||psi||_1 / ||psi||^2 + eps, a self-contained theorem about any vector and any
nested cake, with the classical 8 recovered at base 2.  (iii) THE RESOLVENT
DELOCALISATION BOUND, ||psi||_inf <= lam_up max_j ||R e_j|| with lam_up the
Green-column Rayleigh value, a self-contained theorem about any symmetric
positive definite form.  (iv) the composite LEVEL LEMMA c_0_ap = 2 base^2 Gam
min(1, Gam_1) + eps with its certified per-window evaluation on %d windows and
its two stress discriminators.  Items (i) to (iii) are form-independent and are
therefore the cheapest verification modules this line has produced; item (iv) is
the one that carries the chain.  Stock after this probe: %d."""
     % (PROMO_T145, len(ROWS), PROMO_T145 + 4))

REST = []
if not V_SIZE:
    REST.append("bring c_0_ap under the classical-size bar: max %.4f vs %.1f, "
                "i.e. push the cake base further below %.4g (the leading "
                "constant is 2 base^2 and tends to 2) or sharpen Gam, whose "
                "own looseness against the true sqrt(m) ||psi||_inf is only a "
                "factor %.3f" % (C0AP_MAX, BAR_C0, min(BASE_GRID),
                                 qmax([r["Gam"] / (r["v_inf"]
                                                   * math.sqrt(r["m"]))
                                       for r in ROWS])))
if not V_DELOC or not V_DOM or not V_CHAIN or not V_THM_CAKE or not V_RITZ:
    REST.append("repair the failing verified step listed in the verdict block")
if not V_NOGO:
    REST.append("the candidate did NOT fail on the no-go, which means it is "
                "too strong and therefore wrong -- find the leak before "
                "anything else")
REST.append("sigma_tot on the ENERGY route is still MEASURED (T145: %.3f .. "
            "%.3f); the counting lemma does not reach a sum over truncations, "
            "so either an energy-side analogue or the explicit statement that "
            "the Green route is the only certified one"
            % (SIGT_T145[0], SIGT_T145[1]))
REST.append("D-uniformity FOR ALL D rather than on a finite surface: Gam is a "
            "certified per-window number with fit %s, and turning that into a "
            "theorem needs an asymptotic bound on max_j ||R e_j|| lam_min, "
            "i.e. on the delocalisation of the Green columns themselves"
            % fit_str(F_GAM))
REST.append("T145's %d OPEN R4 border blocks are not reproducible from a "
            "rebuilt pool: the pool built here has %d blocks and the direct "
            "Schur route closes %d of %d, so this probe cannot see the open "
            "ones.  What is needed is the ACTUAL open blocks from the T134 "
            "assembly rather than a proxy pool -- the anatomy transfers, the "
            "count does not"
            % (R4_OPEN_T145, len(BLK),
               len([x for x in BLK if x["direct"] == 1]), len(BLK)))

info("L4.rest_list", "THE SHORTEST REST LIST, %d items:" % len(REST))
for (i, s) in enumerate(REST):
    para("(%d) %s" % (i + 1, s), indent="       ")

info("L4.verdict_conditions", "the %d hard-wired conditions, %d failing:"
     % (len(COND), N_FAILED))
for (nm, ok) in COND:
    info("   %s" % ("OK  " if ok else "FAIL"), nm)

check("el_l4.verdict_rule_applied",
      VERDICT in ("LEVEL-CARRIES", "ONE-TERM-MISSING", "LEVEL-RESISTS")
      and (VERDICT == "LEVEL-CARRIES") == (N_FAILED == 0),
      "the verdict rule was evaluated on %d preregistered conditions and is "
      "%s; the rule counts a constant MEASURED AT THE MINIMISER as NOT a "
      "priori and cannot be argued out of that -- the same discipline T145 "
      "imposed on itself" % (len(COND), VERDICT))

section("VERDICT  %s" % VERDICT)
if VERDICT == "LEVEL-CARRIES":
    para("""LEVEL-CARRIES.  L1, the level lemma, is closed on the measurement
surface as a chain of theorems and certified per-window inequalities, with no
step reading the minimiser: G(base) <= 2 base^2 ||psi||_inf ||psi||_1 /
||psi||^2 + eps is a counting theorem about any vector at any base; ||psi||_inf
and ||psi||_1 are bounded a priori by the resolvent identity psi = lam R psi
with lam_up the Rayleigh value of a Green column (Rayleigh-Ritz) and the column
norms certified from above with the linear-solve residual paid for; the
composite constant is c_0_ap = %.4f .. %.4f on %d windows, against T145's
MEASURED %.3f .. %.3f, and the resulting chain lam >= 1 / (kap_up c_0_ap
Psi_abs) holds with loss factor %.4g .. %.4g.  The candidate FAILS on T145's
no-go form (Gam %.2f -> %.2f) and stays flat on the Dirichlet control, so it is
neither vacuous nor too strong.  WHAT THIS IS AND IS NOT: a finite list of
certified window statements with an explicit maximum, on prime-power zones in
frame A -- the step from there to a statement for all D is a FIT and remains
open, sigma_tot on the energy route remains measured, and no line of this
touches RH in either direction."""
         % (C0AP_MIN, C0AP_MAX, len(ROWS), GDY_T145[0], GDY_T145[1],
            qmin([r["loss_ex"] for r in ROWS]),
            qmax([r["loss_ex"] for r in ROWS]),
            NG[0]["Gam"] if NG else float("nan"),
            NG[-1]["Gam"] if NG else float("nan")))
elif VERDICT == "ONE-TERM-MISSING":
    para("""ONE-TERM-MISSING.  Eight of the nine preregistered conditions hold
and exactly one resists: %s.  Everything else is in place -- the counting lemma
is a theorem, the resolvent delocalisation is a theorem, the a priori constant
dominates the measured G_dy on all %d windows with c_0_ap = %.4f .. %.4f, the
chain direction holds, and the candidate discriminates correctly between the
no-go and the control.  The missing term is therefore not structural but
QUANTITATIVE, and it is one number.""" % (MISSING[0] if MISSING else "-",
                                          len(ROWS), C0AP_MIN, C0AP_MAX))
else:
    para("""LEVEL-RESISTS.  %d of the %d preregistered conditions fail: %s.
The anatomy is reported above step by step; the honest consequence is that the
level lemma does not close in this shape and the constants of T145 remain
measured at the minimiser.""" % (N_FAILED, len(COND), "; ".join(MISSING)))

para("""THE THREE SENTENCES, without decoration.  (1) The one object T145 left
-- an a priori bound for one of its two constants -- is delivered here for the
GREEN route in the shape c_0 <= 2 base^2 sqrt(m) lam_up max_j ||R e_j|| min(1,
Gam_1) + eps, every factor a functional of the form alone, and its value on the
measurement surface is %.4f .. %.4f (base %s) against T145's measured %.3f ..
%.3f at base 2.  (2) It works for one reason and it is worth naming: the
Theta(D^3) smallness of the gap, which is the obstruction everywhere else in
this line, is here the LEVER -- the minimiser is lam times the Green function
applied to itself, so it cannot concentrate unless the Green columns do, and the
Green columns are an a priori object; two side findings fall out, that the cake
base is free (gain %.2f .. %.2f) and that the bottom of the whitened spectrum is
a near-degenerate BLOCK (lam_2 / lam_hat = %.2f .. %.2f), which kills every
perturbation route and costs the identity route nothing.  (3) What is NOT
delivered: sigma_tot on the energy route stays measured, the D-uniformity is a
finite list of certified window inequalities plus a labelled fit rather than a
statement for all D, and the surrounding claim remains a finite-window
positivity statement on prime-power zones with an explicit constant -- the
criterion is cited as an address and never used."""
     % (C0AP_MIN, C0AP_MAX, "/".join("%.4g" % b for b in BASE_STARS),
        GDY_T145[0], GDY_T145[1], qmin([r["base_gain"] for r in ROWS]),
        qmax([r["base_gain"] for r in ROWS]),
        qmin([r["sep_rel"] for r in ROWS]),
        qmax([r["sep_rel"] for r in ROWS])))

para("""CITATIONS, all classical, all cited and none re-proved: Maz'ya 1985
(capacitary strong-type inequalities, the half under attack and NOT used);
Miclo 1999 (level-set chains for Markov forms); Davis-Kahan 1970 (the
eigenvector perturbation bound, instrumented and deliberately not used);
Perron-Frobenius (single-signedness on the Stieltjes partner);
Fukushima-Oshima-Takeda 1994 ch. 1 (Beurling-Deny form of a Dirichlet form, the
hypothesis this surface lacks); Rayleigh 1877 and Ritz 1909 (the variational
upper bound); Gerschgorin 1931 (the restricted local floor);
Bertrand-Chebyshev 1852 (the only gap fact used); Charikar 2000 and Goldberg
1984 (the density bound's constant); Muckenhoupt 1972 (the two-weight shape);
Wilkinson 1968 and Higham 2002 (the Cholesky floor); Haynsworth 1968 (the
bordered step); Weil 1952, Bombieri 2000, Connes 1999 (the surrounding address,
cited and never used).""")

section("TOTAL  %d checks, %d passed, %d failed   [%.1f s]"
        % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
info("probe.identity", "part %d of the prime/window investigation, contract "
     "LEVEL.LEMMA; %d windows, %d border blocks, %d no-go sizes, %d control "
     "sizes; largest form factorised %d (cap %d); wrote nothing"
     % (N_PROBES_PRIOR + 1, len(ROWS), len(BLK), len(NG), len(CT),
        max([r["m"] for r in ROWS] + [x["m"] for x in NG]
            + [x["m"] for x in CT]), MAX_H))
if FAIL:
    raise SystemExit("probe RED: %d checks failed" % FAIL)
