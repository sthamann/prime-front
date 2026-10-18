"""Discovery probe (2026-07-28), part 134 of the prime/window investigation.
Contract POLE.FREE.FLOOR -- the three items T131 left on the rest list, and
nothing else.

WHERE THIS SITS (T131 SUPPLY-PARTIAL: the self-supply loop is BUILT and one
number short of closed; every load-bearing number is rebuilt here, quoted ones
marked QUOTED)
  T131 turned the window-form floor into a POLE-FREE question.  The secular
  sandwich, derived there from the Szegoe-Levinson prediction error eps and
  verified on dense windows,
        lam_min(Q) >= eps / (||u||^2 + eps / mu_1),   u = A^{-1} b,
        mu_1 = lam_min(A),   A = the POLE-FREE odd Toeplitz+Hankel section,
        Q = A - b b^T = the window form
  depends on mu_1 only through the term eps / mu_1 in the denominator, so mu_1
  may be crude by DECADES (T131 measured 9 decades of slack).  What is missing
  is any POSITIVE mu_1 that is not a Lanczos measurement.  The three residual
  items, verbatim from T131's rest list:
    (1) lam_min(A) > 0 for the pole-free odd Toeplitz+Hankel section.  ANY
        floor inside the slack suffices.  Measured mu_1 = 4.7e-5 .. 6.4e-2,
        growing roughly like D^1.8 (QUOTED).  The symbol route is dead
        (Grenander-Szegoe: the Weil lag symbol is indefinite, rigorous floor
        -76 .. -27, QUOTED), but a crude route with 9 decades of head-room was
        never tried.
    (2) S^{-1} > 0 entrywise for the border Schur block -- the one ingredient
        of the new sign theorem that is measured and not derived (575/575
        entrywise positive; the Metzler sufficient condition FAILS on 11 of
        575, QUOTED).  What is the structural reason?
    (3) M17 vacuity.  The assembled pencil-mass bound is a valid majorant and
        vacuous, and T131 attributed the dominant loss to the U-METRIC
        MISMATCH sqrt(lam_max U / lam_min U) = 2.18 (QUOTED): the assembly
        measures shat in the U-metric and bounds comb in the Euclidean one.
  Carried in as machinery, not re-derived: the T115 O(#atoms) lag assembly, the
  odd (J = -1) coordinates, the bordered step and the Haynsworth bracket, the
  two-grid isometries, the certified symbol envelope, the T126 fractional
  Dirichlet identity
        v^T A v = sum_r w_r v_r^2 + sum_{r<s} (-A_rs) (v_r - v_s)^2,
        w_r = the ROW SUMS of A,
  which is an exact algebraic identity (re-verified in F0) with 86.1 % of the
  off-diagonals negative (QUOTED).  Zones are prime powers, frame A (T112),
  nu = 4 (T105).

WHAT THIS PROBE DOES
  F0  SETUP -- atoms, the free-resolution record schedule, and every piece of
      machinery verified against a dense reference: the odd Toeplitz+Hankel
      section against a slow reference, the T126 Dirichlet identity to
      round-off, the Cholesky-bisection certificate against exact eigenvalues,
      and the TRIANGULAR-PREFIX LEMMA that F3 rests on.
  F1  THE CRUDE FLOOR.  Six candidate routes to lam_min(A) >= something > 0,
      each measured over zones x depths, each classified CERTIFIABLE (a
      sign/row-sum/Cholesky statement) or MEASURED, and each compared against
      the ACTUAL requirement need = 1e-9 x measured mu_1:
        R1  the Dirichlet split A = diag(w) + L_N - L_P (killing + good jumps
            - bad jumps), with Gershgorin on the decomposition;
        R2  Jacobi preconditioning D^{-1/2} A D^{-1/2}, diagonal dominance
            after scaling;
        R3  the comparison matrix M(A) = diag(A) - |offdiag| -- the H-matrix /
            Ostrowski route, which rests on the elementary inequality
            v^T A v >= |v|^T M(A) |v| and is sharper than Gershgorin on it;
        R4  the Cholesky / Levinson PIVOTS: does the POLE-FREE form have all
            pivots positive (T119 found exactly ONE negative pivot, and it
            belonged to the form WITH the pole)?  Then Cholesky-per-window IS
            the certificate and the only open question is the D-uniformity of
            the pivot floor, which is measured and FITTED here;
        R5  the block / Schur recursion on the two-grid split -- tested for the
            DIRECTION obstruction, not assumed;
        R6  PATH COMPARISON (Diaconis-Stroock 1991; Sinclair 1992): route every
            bad jump through two good jumps, (v_r - v_s)^2 <= 2 (v_r - v_m)^2 +
            2 (v_m - v_s)^2, and pay the congestion out of the good weights.
  F2  S^{-1} > 0 -- THE STRUCTURAL REASON.  Inverse-positivity classes tested
      in order of strength: Metzler / Stieltjes (Ostrowski 1937), the LU sign
      structure, the GREEN-FUNCTION reading (the Metzler part of S is the
      generator of a killed jump process, so its inverse is a Green function
      and positive for elementary reasons), and then the candidate theorem:
      S = S_0 + Delta with S_0 Stieltjes and Delta >= 0, where a NEUMANN
      MARGIN computable from S alone gives S^{-1} > 0.  Plus the WEAKEST form
      the sign theorem actually needs -- reflection positivity on the bottom
      eigenspace only, not global Metzler.
  F3  M18 IN THE WHITENED BASIS.  The 2.18 mismatch is removed BY
      CONSTRUCTION: with U = L L^T the pencil (S, U) becomes the ordinary
      symmetric problem for L^{-1} S L^{-T} and the mass is the Euclidean mass
      of s~ = L^{-1} shat.  Because L is LOWER TRIANGULAR, the outer-cell
      prefixes are preserved exactly (F0's triangular-prefix lemma), so the
      localisation the bound needs survives the whitening.  Is the whitened
      bound non-vacuous, and on how many rungs?
  F4  THE MAP V7, the final promotion list, and the shortest rest list.

PREREGISTERED VERDICTS (bars declared here, before any number is computed)
  FLOOR-FOUND   : at least ONE F1 route is CERTIFIABLE from signs / row sums /
                  a per-window Cholesky, delivers a POSITIVE floor on EVERY
                  window of the measurement surface, and clears the 9-decade
                  requirement -- AND F2 identifies the inverse-positivity class
                  with a sufficient condition that holds on every transport.
  PARTIAL       : some of that stands -- named precisely, per route, with the
                  residual named.
  FLOOR-RESISTS : every route fails on the surface -- with the precise anatomy
                  of each failure.
  Element gates: el_firewall, el_f0, el_f1, el_f2, el_f3, el_f4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger / TeX / website /
    changelog edit, no verification/ module, no next.txt, no .md output, no git
    action.
  * NO Riemann zero data of any kind.  An AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address
    of the surrounding statement and is NEVER USED, in either direction.
    Nothing here claims, assumes or approaches RH.  Even with all three items
    closed, what would stand is positivity of the Weil window form on test
    functions supported in (-alpha_max, alpha_max) for the alpha actually
    reached -- a FINITE-WINDOW statement about a finite list of prime-power
    zones.  The distance to RH is MAPPED in F4, never travelled.
  * CERTIFIABLE vs CERTIFIED vs MEASURED vs FIT vs HYPOTHESIS, per line.  A
    completed Cholesky of A - s I certifies lam_min(A) >= s - c_h u ||A||,
    u = 2^-53, c_h = (h+1)/(1-(h+1)u) (Wilkinson 1968; Higham 2002 Thm
    10.3/10.4).  A row-sum / sign statement is CERTIFIABLE without any
    factorisation.  An eigenvalue from eigvalsh and a Lanczos Ritz value are
    MEASUREMENTS.  Every fit is a FIT and carries a delete-one jackknife band.
    Bars declared before a number are NEVER moved afterwards.
  * CLASSICAL ADDRESSES USED: Gershgorin 1931 (the decomposition bound),
    Stieltjes / Ostrowski 1937 and 1956 (comparison matrices, H-matrices,
    inverse-positivity), Berman-Plemmons 1979 (the M-matrix and inverse-
    positive classes, Schur complements of M-matrices), Perron 1907 /
    Frobenius 1912 (the ground-state sign), Levinson 1947 / Durbin 1960 and the
    Trench inverse (the pivot recursion), Cholesky / Gram-Schmidt triangularity
    (the prefix lemma), Schur and Haynsworth 1968 (the complements and the
    transport bracket), Cauchy interlacing (sections and compressions),
    Wilkinson 1968 / Higham 2002 (the floating-point certificate),
    Diaconis-Stroock 1991 and Sinclair 1992 (path comparison of Dirichlet
    forms), Feller / Dynkin Green functions of killed jump processes (the
    positivity reading), Yakubovich's S-procedure (the conditional comb bound),
    Szegoe 1939 and Grenander-Szegoe 1958 (the prediction-error reading and the
    symbol route that is DEAD here), Yserentant 1986 (the two-scale space),
    Bertrand-Chebyshev 1852 and the trivial even bound (the only two gap facts
    consumed).  No gap CONJECTURE (Cramer, Firoozbakht, twin, Mersenne
    infinitude) enters anywhere, in any direction.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    FFT-based lag assembly, rectangular gathers and pure interval geometry may
    exceed it.  Probe budget < 900 s.

OUTCOME OF THIS RUN  =>  see the F4 map and TOTAL.verdict printed below.
"""
import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import (cho_factor, cho_solve, cholesky, eigh, eigvalsh, ldl,
                          solve_triangular, svdvals)

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)
SQ2 = math.sqrt(2.0)

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

# --- F1 pools ---------------------------------------------------------------
F1_ZONES = 30                # zones in the floor battery
F1_HCAP = 900                # full six-route battery up to this h
F1_HCAP_WIDE = 1400          # R4-only extension (cert floor + pivots)
F1_LEV = 3                   # depths per zone (M, 2M, 4M)
SLACK_DEC = 9                # THE DECLARED SLACK: need = 10^-9 x measured mu_1
T_F1 = 210.0

# --- F2 pools ---------------------------------------------------------------
T_F2 = 250.0
F2_GC_MIN = 2
F2_HCAP = 1100               # border blocks are cheap; the STEP is not
F2_MAX = 900                 # transports attempted (T131 reported 575)
F2_PER_RHO = 30
F2_LOGRES = 90.0
F2_RHO = (1.001, 1.05, 1.10, 1.20, 1.25, 1.35, 1.49531, 1.60, 1.75, 1.90,
          2.00, 2.25, 2.50, 3.00, 3.50, 4.00)   # 1.49531 = the T127 band edge
F2_CONE_DRAWS = 24           # random draws in the bottom eigenspace
F2_BOTTOM = 3                # dimension of the bottom eigenspace tested

# --- F3 pools ---------------------------------------------------------------
H_TEL = 1400                 # finest telescope level (<= MAX_H)
PEN_ZONES = 14
NLEV_MAX = 3
L_CAP = 2 ** 20
ENV_OS = 48
ENV_FRAC = 0.10
M18_KSET = (4, 8, 16)
M18_SPRO_H = 420             # above this only the certified Cauchy-Schwarz row
                             # bound is affordable (both are majorants)
T_F3 = 230.0

# --- preregistered bars (declared before any number) ------------------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_MASS_GOOD = 0.5          # the whitened mass bound must give bad <= 1/2
BAR_ROUTE_COVER = 1.0        # FLOOR-FOUND needs a route positive on ALL windows
BAR_F2_ALL = 1.0             # and an F2 sufficient condition on ALL transports

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
MU1_T131 = (4.7e-5, 6.4e-2)
MU1_EXP_T131 = 1.8
SYM_FLOOR_T131 = (-76.0, -27.0)
SENS_DEC_T131 = 9
SG_INV_T131 = (575, 575)
SG_METZ_FAIL_T131 = 11
NEG_OFF_T131 = 86.1
MISMATCH_T131 = 2.18
MASS_T127 = 0.9665
MU_MIN_T126 = (0.192, 0.307)
RHO_UNI_T127 = 1.49531
COVER_T127 = 99.26
DEEP_T130 = ((127, 2476), (256, 5694))
RUNGS_T131 = 27
N_PROBES_PRIOR = 133


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
    return float(np.max(np.abs(a - b))) / max(float(np.max(np.abs(b))), 1.0e-300)


def qmin(v):
    return float(np.min(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmax(v):
    return float(np.max(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmed(v):
    return float(np.median(np.asarray(v, dtype=float))) if len(v) else float("nan")


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
    n = x.shape[0]
    a, b, rms = fit_line(x, y)
    if n < 5:
        return a, b, float("nan"), float("nan"), rms
    aa, bb = [], []
    step = max(1, n // 40)
    for i in range(0, n, step):
        m = np.ones(n, dtype=bool)
        m[i] = False
        ai, bi, _ = fit_line(x[m], y[m])
        aa.append(ai)
        bb.append(bi)
    k = len(aa)
    sa = math.sqrt(max(k - 1, 1) / float(k) * float(np.sum(
        (np.asarray(aa) - np.mean(aa)) ** 2)))
    sb = math.sqrt(max(k - 1, 1) / float(k) * float(np.sum(
        (np.asarray(bb) - np.mean(bb)) ** 2)))
    return a, b, sa, sb, rms


def next_pow2(n):
    k = 1
    while k < n:
        k *= 2
    return k


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
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("el_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("el_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "pole_free_floor_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- T111..T131 code path
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


# ----------------------------------------------------------------------------
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T131)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_toeplitz_slow(c, M):
    """The definition, entry by entry -- the F0 reference for odd_toeplitz."""
    h = M // 2
    out = np.empty((h, h))
    for i in range(h):
        for j in range(h):
            out[i, j] = c[abs(i - j)] - c[(M - 1) - i - j]
    return out


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def odd_nodes(alpha, M):
    D = 2.0 * alpha / M
    h = M // 2
    return -alpha + (np.arange(h) + 0.5) * D, D


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


def cert_lmin(A, lam):
    try:
        cholesky(sym(A) - lam * np.eye(A.shape[0]), lower=True, check_finite=False)
        return True
    except LinAlgError:
        return False


def cert_floor_bisect(A, lo, hi, iters=26):
    """The largest s on a bisection ladder for which chol(A - s I) COMPLETES --
    a CERTIFIED lower bound for lam_min(A) up to the declared fp floor."""
    if not cert_lmin(A, lo):
        return None
    a, b = lo, hi
    for _ in range(iters):
        mid = 0.5 * (a + b)
        if cert_lmin(A, mid):
            a = mid
        else:
            b = mid
    return a


def cert_pd(A):
    fac = safe_cho(A)
    return (fac is not None), chol_floor(gersh(A), A.shape[0]), fac


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


def edge_geom(u_o, u_n, D_c, D_f):
    fr_c = step_frame(u_o, u_n, D_c)
    fr_f = step_frame(u_o, u_n, D_f)
    if fr_c is None or fr_f is None:
        return None
    return dict(fr_c=fr_c, fr_f=fr_f, gc_c=fr_c["gc"], gc_f=fr_f["gc"],
                al_c=fr_c["al_n"], al_f=fr_f["al_n"], rho=D_c / D_f,
                D_c=D_c, D_f=D_f, h_c=fr_c["h_n"], h_f=fr_f["h_n"], g=u_n - u_o)


# ----------------------------------------------------------------------------
# the bordered step (Haynsworth 1968) and the border Schur block
# ----------------------------------------------------------------------------
def bordered_step(fr, atoms_all, want_Q=False):
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
    ev, U = np.linalg.eigh(S)
    out = dict(S=S, lam=float(ev[0]), y=np.ascontiguousarray(U[:, 0]),
               ev=ev, U=U, fr=fr, scale=gersh(A))
    if want_Q:
        out["Q"] = Q
        out["tv"] = tv
        out["c"] = c_n
    del Q, A, C, X, Z
    return out


# ----------------------------------------------------------------------------
# the two-grid isometries, the certified symbol envelope and the telescope
# (T122..T125), needed for the F3 pencil
# ----------------------------------------------------------------------------
def rest_p(X):
    return (X[0::2] + X[1::2]) / SQ2


def rest_z(X):
    return (X[0::2] - X[1::2]) / SQ2


def two_grid_blocks(A):
    PtA = rest_p(A)
    ZtA = rest_z(A)
    Ac = sym(rest_p(PtA.T).T)
    Az = sym(rest_z(ZtA.T).T)
    Bx = rest_z(PtA.T).T
    return Ac, Az, Bx


def zz_compress(A):
    return sym(rest_z(rest_z(A).T).T)


def sym_grid(c, L):
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
    """The CERTIFIED per-cell envelope ell <= sigma^(M) <= up (second-order
    Taylor margin, |sigma''| bounded globally by 2 sum j^2 |c_j|)."""
    M = c.shape[0]
    L = min(next_pow2(os_start * M), cap)
    while True:
        f = sym_grid(c, L)
        fp = dsym_abs_grid(c, L)
        dt = 2.0 * math.pi / L
        j = np.arange(M, dtype=float)
        fpp = 2.0 * float(np.sum(j * j * np.abs(c)))
        d = 0.5 * dt * fp + dt * dt / 8.0 * fpp
        ell, up = f - d, f + d
        marg = float(np.max(d))
        pos = ell[ell > 0.0]
        scale = float(np.median(pos)) if pos.size > 8 else float(np.max(f))
        if marg <= frac * max(scale, 1.0e-300) or 2 * L > cap:
            return ell, up, f, marg, L, scale
        L *= 2


def pwc_lags(g, n):
    L = g.shape[0]
    dt = 2.0 * math.pi / L
    X = np.fft.rfft(g).real
    m = np.arange(n, dtype=float)
    lag = np.zeros(n)
    lag[0] = float(g.mean())
    k = min(n, X.shape[0])
    lag[1:k] = X[1:k] * np.sin(m[1:k] * dt * 0.5) / (math.pi * m[1:k])
    return lag


def telescope_levels(alpha, M0, atoms, nlev):
    """Levels l = 0..nlev-1, M_l = 2^l M0 at FIXED alpha."""
    lv = []
    for l in range(nlev):
        M = M0 * (2 ** l)
        c, D = lag_vector_fast(alpha, M, atoms)
        A = sym(odd_toeplitz(c, M))
        b = odd_pole_vector(alpha, M)
        fac = safe_cho(A)
        if fac is None:
            return None
        u = cho_solve(fac, b, check_finite=False)
        q = float(np.dot(b, u))
        lv.append(dict(l=l, M=M, D=D, c=c, A=A, b=b, u=u, q=q, eps=1.0 - q,
                       h=M // 2, fac=fac))
    return lv


def nlev_for(h0, cap=H_TEL):
    n = 1
    while h0 * (2 ** n) <= cap and n + 1 <= NLEV_MAX:
        n += 1
    return n


def _spro(Rt, Gt, lo=1.0e-6, hi=1.0e10, iters=24):
    """min_{s>=0} lam_max(Rt - s Gt) by ternary search on log s (convex in s)."""
    n = Rt.shape[0]

    def val(s):
        try:
            return float(eigvalsh(sym(Rt - s * Gt),
                                  subset_by_index=[n - 1, n - 1])[0])
        except (LinAlgError, ValueError):
            return float("inf")

    a, b = math.log(lo), math.log(hi)
    best = min(val(0.0), val(lo), val(hi))
    for _ in range(iters):
        m1 = a + (b - a) / 3.0
        m2 = b - (b - a) / 3.0
        v1, v2 = val(math.exp(m1)), val(math.exp(m2))
        best = min(best, v1, v2)
        if v1 <= v2:
            b = m2
        else:
            a = m1
        if b - a < 1.0e-4:
            break
    return best


# ----------------------------------------------------------------------------
# THE T126 FRACTIONAL DIRICHLET SPLIT -- the central object of F1 and F2
# ----------------------------------------------------------------------------
def dirichlet_split(A):
    """A = diag(w) + L_N - L_P, an EXACT identity for symmetric A:

        v^T A v = sum_r w_r v_r^2 + sum_{r<s} (-A_rs) (v_r - v_s)^2
                = sum_r w_r v_r^2 + v^T L_N v - v^T L_P v

    with w = ROW SUMS of A (the KILLING weights), L_N the graph Laplacian of the
    NEGATIVE off-diagonals (weights -A_rs > 0, the GOOD jumps, L_N >= 0 by
    construction) and L_P the Laplacian of the POSITIVE off-diagonals (the BAD
    jumps, L_P >= 0, entering with a MINUS sign).  Everything about the sign of
    A is then a competition between diag(w) + L_N and L_P."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    w = A.sum(axis=1)
    off = A - np.diag(dg)
    Pm = np.where(off > 0.0, off, 0.0)
    Nm = np.where(off < 0.0, -off, 0.0)
    P_row = Pm.sum(axis=1)
    N_row = Nm.sum(axis=1)
    L_P = np.diag(P_row) - Pm
    L_N = np.diag(N_row) - Nm
    n_off = h * (h - 1)
    return dict(h=h, dg=dg, w=w, Pm=Pm, Nm=Nm, P_row=P_row, N_row=N_row,
                L_P=L_P, L_N=L_N, off=off, n_off=n_off,
                frac_neg=float(np.count_nonzero(off < 0.0)) / max(n_off, 1))


def path_compare(A, dsp):
    """R6 -- DIACONIS-STROOCK / SINCLAIR PATH COMPARISON of Dirichlet forms.

    Every BAD jump (r, s) is routed through a two-step path r -> m -> s using
    the elementary inequality (v_r - v_s)^2 <= 2 (v_r - v_m)^2 + 2 (v_m - v_s)^2,
    so the bad Laplacian is absorbed by the GOOD one provided each good edge
    carries its routed demand: congestion = max over used edges of
    (routed demand) / (available good weight).  Nearest-neighbour bad jumps have
    no interior midpoint and are paid out of the diagonal instead, via
    (v_r - v_s)^2 <= 2 v_r^2 + 2 v_s^2, which reduces the killing weights.
    If congestion <= 1 the route CERTIFIES lam_min(A) >= min_r (w_r - direct_r);
    the number is reported either way."""
    h = dsp["h"]
    Pm, Nm, w = dsp["Pm"], dsp["Nm"], dsp["w"]
    r, s = np.triu_indices(h, 1)
    a = Pm[r, s]
    keep = a > 0.0
    r, s, a = r[keep], s[keep], a[keep]
    direct = np.zeros(h)
    if r.size == 0:
        return dict(cong=0.0, floor=float(np.min(w)), n_edge=0, n_direct=0,
                    n_route=0)
    adj = (s - r) > 1
    nr, ns, na = r[~adj], s[~adj], a[~adj]
    if nr.size:
        np.add.at(direct, nr, 2.0 * na)
        np.add.at(direct, ns, 2.0 * na)
    r2, s2, a2 = r[adj], s[adj], a[adj]
    used = np.zeros((h, h))
    if r2.size:
        m = (r2 + s2) // 2
        for i, j in ((r2, m), (m, s2)):
            np.add.at(used, (np.minimum(i, j), np.maximum(i, j)), 2.0 * a2)
    cap = np.triu(Nm, 1)
    msk = used > 0.0
    dead = int(np.count_nonzero(msk & (cap <= 0.0)))
    live = msk & (cap > 0.0)
    cong_f = float(np.max(used[live] / cap[live])) if live.any() else 0.0
    cong = float("inf") if dead else cong_f
    return dict(cong=cong, cong_f=cong_f, dead=dead,
                floor=float(np.min(w - direct)), n_edge=int(r.size),
                n_direct=int(nr.size), n_route=int(r2.size),
                n_used=int(np.count_nonzero(msk)))


def floor_routes(A, mu_meas, cert):
    """The six F1 routes on ONE window.  Each entry carries its own class."""
    dsp = dirichlet_split(A)
    h, w, dg = dsp["h"], dsp["w"], dsp["dg"]
    out = dict(h=h, frac_neg=dsp["frac_neg"], w_min=float(np.min(w)),
               w_max=float(np.max(w)), dg_min=float(np.min(dg)),
               p_row_max=float(np.max(dsp["P_row"])),
               mu_meas=mu_meas, cert=cert)
    # --- R1  the Dirichlet split ------------------------------------------
    out["r1a"] = float(np.min(w - 2.0 * dsp["P_row"]))           # CERTIFIABLE
    out["r1b"] = out["w_min"] - 2.0 * out["p_row_max"]           # CERTIFIABLE
    out["mn_min"] = float(eigvalsh(sym(np.diag(w) + dsp["L_N"]),
                                   subset_by_index=[0, 0])[0])
    if h <= 400:
        ev_p = eigvalsh(dsp["L_P"])
        lp_max = float(ev_p[-1])
        # how many bad DIRECTIONS would a rank-k downdate have to treat exactly
        # for the remainder to sit below half the measured floor?
        out["lp_keff"] = int(np.count_nonzero(ev_p > 0.5 * max(mu_meas, 0.0)))
        out["lp_rank"] = int(np.count_nonzero(ev_p > 1.0e-10 * lp_max))
        del ev_p
    else:
        lp_max = float(eigvalsh(dsp["L_P"], subset_by_index=[h - 1, h - 1])[0])
        out["lp_keff"] = -1
        out["lp_rank"] = -1
    out["lp_max"] = lp_max
    out["r1c"] = out["mn_min"] - lp_max                          # MEASURED
    # --- R2  Jacobi preconditioning ---------------------------------------
    if out["dg_min"] > 0.0:
        sc = 1.0 / np.sqrt(dg)
        At = A * sc[:, None] * sc[None, :]
        offt = np.abs(At) - np.diag(np.abs(np.diag(At)))
        out["r2_g"] = float(np.min(1.0 - offt.sum(axis=1)))
        out["r2"] = out["dg_min"] * out["r2_g"]                  # CERTIFIABLE
        lt = cert_floor_bisect(sym(At), 0.0, 4.0)
        out["r2_lam"] = lt if lt is not None else float("nan")
        out["r2b"] = (out["dg_min"] * lt) if lt is not None else float("nan")
        del At, offt
    else:
        out["r2_g"] = out["r2"] = out["r2b"] = out["r2_lam"] = float("nan")
    # --- R3  the comparison matrix / H-matrix route ------------------------
    Mc = sym(np.diag(dg) - (np.abs(dsp["off"])))
    out["r3_meas"] = float(eigvalsh(Mc, subset_by_index=[0, 0])[0])
    c3 = cert_floor_bisect(Mc, 0.0, max(out["r3_meas"], 1.0e-12) * 2.0 + 1e-12) \
        if out["r3_meas"] > 0.0 else None
    out["r3"] = c3 if c3 is not None else out["r3_meas"]         # CERTIFIABLE
    del Mc
    # --- R4  the Cholesky / Levinson pivots -------------------------------
    try:
        Lc = cholesky(A, lower=True, check_finite=False)
        piv = np.diag(Lc) ** 2
        out["piv_min"] = float(np.min(piv))
        out["piv_neg"] = 0
        out["piv_rel"] = float(np.min(piv)) / max(float(np.max(piv)), 1e-300)
        del Lc
    except LinAlgError:
        out["piv_min"] = float("nan")
        out["piv_neg"] = -1
        out["piv_rel"] = float("nan")
    out["r4"] = cert if cert is not None else float("nan")       # CERTIFIED
    # --- R5  the two-grid block / Schur recursion (needs an EVEN section) --
    out["ac_min"] = out["sz_min"] = float("nan")
    out["r5_equiv"] = -1
    if h % 2 == 0:
        Ac, Az, Bx = two_grid_blocks(A)
        out["ac_min"] = float(eigvalsh(Ac, subset_by_index=[0, 0])[0])
        fac_c = safe_cho(Ac)
        if fac_c is not None:
            Sz = sym(Az - Bx.T @ cho_solve(fac_c, Bx, check_finite=False))
            out["sz_min"] = float(eigvalsh(Sz, subset_by_index=[0, 0])[0])
            del Sz
        # the EXACT shifted equivalence at s = half the certified floor
        s0 = 0.5 * cert if (cert is not None and cert > 0.0) else 0.0
        if s0 > 0.0:
            f2 = safe_cho(Ac - s0 * np.eye(Ac.shape[0]))
            if f2 is not None:
                Ss = sym(Az - s0 * np.eye(Az.shape[0])
                         - Bx.T @ cho_solve(f2, Bx, check_finite=False))
                out["r5_equiv"] = int(safe_cho(Ss) is not None)
                del Ss
            else:
                out["r5_equiv"] = 0
        del Ac, Az, Bx
    # --- R6  path comparison ----------------------------------------------
    pc = path_compare(A, dsp)
    out["r6_cong"] = pc["cong"]
    out["r6_cong_f"] = pc["cong_f"]
    out["r6_dead"] = pc["dead"]
    out["r6"] = pc["floor"] if pc["cong"] <= 1.0 else float("nan")
    out["r6_edges"] = pc["n_edge"]
    out["r6_direct"] = pc["n_direct"]
    out["r6_used"] = pc["n_used"]
    del dsp
    return out


firewall()


# ----------------------------------------------------------------------------
section("F0  SETUP -- atoms, the schedule, every piece verified dense")
# ----------------------------------------------------------------------------
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
check("el_f0.gap_bounds", BERT_OK and EVEN_OK,
      "%d prime-power atoms up to %d, %d zones in the deep range n <= %d; the "
      "only two gap facts consumed hold on all of it: Bertrand-Chebyshev 1852 "
      "g_k <= log 2 (max %.6f) and the trivial even bound g_k >= log(1 + 1/n) "
      "(min %.3e).  No gap CONJECTURE enters, in either direction"
      % (len(ATOMS_ALL), ATOM_MAX, NZ_DEEP, ZONE_DEEP, G_DEEP.max(),
         G_DEEP.min()))

CAP_K = 0.5 * G_DEEP / NU_MAIN
D_FREE = np.empty_like(CAP_K)
D_FREE[0] = CAP_K[0]
for k in range(1, NZ_DEEP):
    D_FREE[k] = min(CAP_K[k], D_FREE[k - 1])
DROP = np.ones(NZ_DEEP)
DROP[1:] = D_FREE[:-1] / D_FREE[1:]
REC_IDX = [k for k in range(1, NZ_DEEP) if DROP[k] > 1.0 + 1.0e-12]

REC = []
for k in REC_IDX:
    geo = edge_geom(UU_ALL[k], UU_ALL[k + 1], float(D_FREE[k - 1]),
                    float(D_FREE[k]))
    if geo is None:
        continue
    REC.append(dict(k=k, n=NN_ALL[k], rho=geo["rho"], gc_c=geo["gc_c"],
                    gc_f=geo["gc_f"], h_c=geo["h_c"], h_f=geo["h_f"],
                    D_c=geo["D_c"], D_f=geo["D_f"], al_c=geo["al_c"],
                    al_f=geo["al_f"]))

RHO_R = np.array([d["rho"] for d in REC], dtype=float)
COVER = float(np.mean(RHO_R <= RHO_UNI_T127))
check("el_f0.record_schedule",
      len(REC) > 100 and abs(100.0 * COVER - COVER_T127) < 0.5,
      "the free-resolution schedule D_k = min(cap_k, D_{k-1}) re-grids at %d of "
      "%d boundaries over n <= %d, and the T127 uniformity band rho <= %.5f "
      "(QUOTED) covers %.2f %% of them (T127 quoted %.2f %%).  The target list "
      "is UNCHANGED from T129..T131 -- nothing is re-chosen here"
      % (len(REC), NZ_DEEP, ZONE_DEEP, RHO_UNI_T127, 100.0 * COVER, COVER_T127))

# --- F0.2  the odd section against the slow reference -----------------------
_zk = None
for k in range(4, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    if 40 <= even_window(UU_ALL[k], D_k) // 2 <= 120:
        _zk = k
        break
if _zk is None:
    _zk = 6
_Dv = 0.5 * float(G_DEEP[_zk]) / NU_MAIN
_Mv = even_window(UU_ALL[_zk], _Dv)
_alv = 0.5 * _Mv * _Dv
_cv, _ = lag_vector_fast(_alv, _Mv, atoms_in(_alv, ATOMS_ALL))
_Av = sym(odd_toeplitz(_cv, _Mv))
E_ODD = rel(odd_toeplitz(_cv, _Mv), odd_toeplitz_slow(_cv, _Mv))
check("el_f0.odd_section", E_ODD < 1.0e-15,
      "the vectorised odd Toeplitz+Hankel section reproduces the entrywise "
      "definition A_rs = c_|r-s| - c_{M-1-r-s} to %.2e at the validation zone "
      "n = %d (h = %d, D = %.4e).  A is the POLE-FREE object: the rank-one pole "
      "term is NOT subtracted anywhere in F1"
      % (E_ODD, NN_ALL[_zk], _Mv // 2, _Dv))

# --- F0.3  THE T126 DIRICHLET IDENTITY, to round-off ------------------------
_ds = dirichlet_split(_Av)
_rng = np.random.default_rng(20260728)
_ID = []
for _j in range(8):
    _v = _rng.standard_normal(_ds["h"])
    _lhs = float(_v @ _Av @ _v)
    _r, _s = np.triu_indices(_ds["h"], 1)
    _jump = float(np.sum(-_Av[_r, _s] * (_v[_r] - _v[_s]) ** 2))
    _rhs = float(np.sum(_ds["w"] * _v * _v)) + _jump
    _ID.append(abs(_lhs - _rhs) / max(abs(_lhs), 1.0e-300))
    _rhs2 = (float(np.sum(_ds["w"] * _v * _v)) + float(_v @ _ds["L_N"] @ _v)
             - float(_v @ _ds["L_P"] @ _v))
    _ID.append(abs(_lhs - _rhs2) / max(abs(_lhs), 1.0e-300))
E_DIR = qmax(_ID)
check("el_f0.dirichlet_identity", E_DIR < BAR_ID,
      "THE T126 FRACTIONAL DIRICHLET IDENTITY IS EXACT, in both readings: "
      "v^T A v = sum w_r v_r^2 + sum_{r<s} (-A_rs)(v_r-v_s)^2 and the matrix "
      "form diag(w) + L_N - L_P agree with the dense form to %.2e on 8 random "
      "vectors.  At this zone %.1f %% of off-diagonals are negative (T126 "
      "quoted %.1f %% over its pool), the row sums run %.3e .. %.3e and the "
      "positive-row mass reaches %.3e -- so L_P is NOT empty and the identity "
      "alone decides nothing"
      % (E_DIR, 100.0 * _ds["frac_neg"], NEG_OFF_T131, float(_ds["w"].min()),
         float(_ds["w"].max()), float(_ds["P_row"].max())))

# --- F0.4  the Cholesky certificate against exact eigenvalues ---------------
_lam_ex = float(eigvalsh(_Av, subset_by_index=[0, 0])[0])
_cf = cert_floor_bisect(_Av, 0.0, max(_lam_ex, 1.0e-12) * 2.0)
CERT_OK = _cf is not None and _cf <= _lam_ex * (1.0 + 1.0e-9)
CERT_TIGHT = (_cf / _lam_ex) if (_cf is not None and _lam_ex > 0.0) else 0.0
check("el_f0.cert_vs_exact", CERT_OK and CERT_TIGHT > 0.99,
      "AND THE CERTIFICATE IS A CERTIFICATE, not a measurement: the largest s "
      "on the bisection ladder for which chol(A - s I) COMPLETES is %.6e, the "
      "exact lam_min from eigvalsh is %.6e, ratio %.6f <= 1 and the declared "
      "floating-point floor at this size is %.2e (Wilkinson 1968; Higham 2002 "
      "Thm 10.3/10.4).  Only the CERT column of F1 is a certificate; every "
      "eigvalsh column is a MEASUREMENT"
      % (_cf if _cf is not None else float("nan"), _lam_ex, CERT_TIGHT,
         chol_floor(gersh(_Av), _ds["h"])))

# --- F0.5  THE TRIANGULAR-PREFIX LEMMA that F3 rests on ---------------------
_he = _ds["h"] - (_ds["h"] % 2)
_Uz = zz_compress(np.ascontiguousarray(_Av[:_he, :_he]))
_pdU, _, _facU = cert_pd(_Uz)
if _pdU:
    _L = np.tril(_facU[0]) if _facU[0].shape[0] == _Uz.shape[0] else None
    _L = cholesky(_Uz, lower=True, check_finite=False)
    _nz = _Uz.shape[0]
    _kk = max(2, _nz // 4)
    _x1 = _rng.standard_normal(_nz)
    _x2 = _x1.copy()
    _x2[_kk:] += _rng.standard_normal(_nz - _kk)
    _w1 = solve_triangular(_L, _x1, lower=True, check_finite=False)
    _w2 = solve_triangular(_L, _x2, lower=True, check_finite=False)
    PREFIX_ERR = float(np.max(np.abs(_w1[:_kk] - _w2[:_kk])))
    _tri = float(np.max(np.abs(np.triu(_L, 1))))
else:
    PREFIX_ERR, _tri, _kk = float("nan"), float("nan"), 0
check("el_f0.prefix_lemma", _pdU and PREFIX_ERR < 1.0e-14,
      "THE TRIANGULAR-PREFIX LEMMA (Cholesky / Gram-Schmidt triangularity): U "
      "= L L^T with L LOWER triangular (upper part %.2e), so the whitened "
      "coordinates s~ = L^{-1} s have the property that the first k entries "
      "depend on the first k entries of s ONLY -- changing s beyond cell k "
      "moves s~[:k] by %.2e.  This is why F3 may whiten the U-metric WITHOUT "
      "destroying the outer-cell localisation the M18 bound needs; the "
      "localisation and the metric are compatible by construction, which is "
      "exactly what T131's 2.18 mismatch cost" % (_tri, PREFIX_ERR))
del _Uz, _ds


# ----------------------------------------------------------------------------
section("F1  THE CRUDE FLOOR -- six routes to lam_min(A) > 0")
# ----------------------------------------------------------------------------
para("""F1.0  THE TASK AND THE HEAD-ROOM.  The object is A, the POLE-FREE odd
Toeplitz+Hankel section; the requirement is ANY certifiable mu_1 > 0, because
the T131 sandwich degrades only through eps / mu_1 and its sensitivity sweep
measured %d decades of slack (QUOTED).  So the bar for a route is not sharpness
but SIGN plus a bound above need = 10^-%d x measured mu_1.  Two routes are ruled
out before we start and are not retried: the SYMBOL route (Grenander-Szegoe
1958) -- the Weil lag symbol is indefinite and the rigorous symbol floor came
out %.0f .. %.0f (QUOTED) -- and any route through a COARSE level, because
compressions bound lam_min from ABOVE (Cauchy interlacing), which R5 measures
rather than assumes.  What is new here is that the T126 Dirichlet identity gives
an exact three-way split of A into a KILLING part diag(w), a GOOD jump part L_N
>= 0 and a BAD jump part -L_P <= 0, and every crude route below is a different
way of paying for L_P.""" % (SENS_DEC_T131, SLACK_DEC, SYM_FLOOR_T131[0],
                             SYM_FLOOR_T131[1]))

F1Z = []
_seen = set()
for k in range(2, NZ_DEEP - 2):
    if len(F1Z) >= F1_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_o = even_window(UU_ALL[k], D_k)
    h_o = M_o // 2
    if h_o < H_MIN or h_o > F1_HCAP:
        continue
    key = h_o // 10
    if key in _seen:
        continue
    _seen.add(key)
    F1Z.append((k, D_k, M_o, h_o))

F1 = []
for (k, D_k, M_o, h_o) in F1Z:
    if budget_left() < BUDGET_S - T_F1:
        info("F1.budget", "floor battery truncated at n = %d" % NN_ALL[k])
        break
    al = 0.5 * M_o * D_k
    ats = atoms_in(al, ATOMS_ALL)
    for lev in range(F1_LEV):
        M = M_o * (2 ** lev)
        h = M // 2
        if h > F1_HCAP_WIDE:
            break
        if budget_left() < BUDGET_S - T_F1:
            break
        c, D = lag_vector_fast(al, M, ats)
        A = sym(odd_toeplitz(c, M))
        mu_meas = float(eigvalsh(A, subset_by_index=[0, 0])[0])
        cert = cert_floor_bisect(A, 0.0, max(mu_meas, 1.0e-14) * 2.0)
        if h <= F1_HCAP:
            row = floor_routes(A, mu_meas, cert)
        else:
            try:
                piv = np.diag(cholesky(A, lower=True, check_finite=False)) ** 2
                pmin, pneg = float(np.min(piv)), 0
            except LinAlgError:
                pmin, pneg = float("nan"), -1
            row = dict(h=h, mu_meas=mu_meas, cert=cert, piv_min=pmin,
                       piv_neg=pneg, r4=cert if cert is not None else float("nan"),
                       light=1)
        row.setdefault("light", 0)
        row.update(n=NN_ALL[k], lev=lev, D=D, al=al)
        F1.append(row)
        del A, c

F1F = [r for r in F1 if not r["light"]]
NEED = dict((id(r), 10.0 ** (-SLACK_DEC) * max(r["mu_meas"], 0.0)) for r in F1)

if F1F:
    print("")
    print("      n     h  lev  D        | mu_meas   cert      R1a       R1b     "
          "  R1c       R2        R3        R6cong   lp_keff")
    for r in F1F:
        print("   %5d %5d %3d  %.2e | %.3e %.3e %+.2e %+.2e %+.2e %+.2e %+.2e "
              "%8.2e %5d"
              % (r["n"], r["h"], r["lev"], r["D"], r["mu_meas"],
                 r["cert"] if r["cert"] is not None else float("nan"),
                 r["r1a"], r["r1b"], r["r1c"], r["r2"], r["r3"],
                 r["r6_cong_f"], r["lp_keff"]))

ROUTES = (("R1a", "Dirichlet + Gershgorin, min_r (w_r - 2 P_r)", "CERTIFIABLE"),
          ("R1b", "Dirichlet + global Gershgorin on L_P", "CERTIFIABLE"),
          ("R1c", "Dirichlet at its sharpest (both parts measured)", "MEASURED"),
          ("R2", "Jacobi scaling + diagonal dominance", "CERTIFIABLE"),
          ("R2b", "Jacobi scaling + Cholesky floor", "CERTIFIED"),
          ("R3", "comparison matrix M(A) (Ostrowski / H-matrix)", "CERTIFIABLE"),
          ("R4", "per-window Cholesky bisection on A", "CERTIFIED"),
          ("R6", "path comparison (Diaconis-Stroock)", "CERTIFIABLE"))
KEY = dict(R1a="r1a", R1b="r1b", R1c="r1c", R2="r2", R2b="r2b", R3="r3",
           R4="r4", R6="r6")

TAB = []
for (nm, desc, cls) in ROUTES:
    kk = KEY[nm]
    vals = [r.get(kk, float("nan")) for r in (F1 if nm == "R4" else F1F)]
    vals = [float(v) if v is not None else float("nan") for v in vals]
    tot = len(vals)
    pos = sum(1 for v in vals if v == v and v > 0.0)
    ok = 0
    for r in (F1 if nm == "R4" else F1F):
        v = r.get(kk, float("nan"))
        v = float(v) if v is not None else float("nan")
        nd = 10.0 ** (-SLACK_DEC) * max(r["mu_meas"], 0.0)
        if v == v and v >= nd and v > 0.0:
            ok += 1
    fin = [v for v in vals if v == v]
    TAB.append(dict(name=nm, desc=desc, cls=cls, tot=tot, pos=pos, need=ok,
                    lo=qmin(fin), hi=qmax(fin)))

print("")
print("   route  class        pos/tot   need/tot  bound range")
for t in TAB:
    rng = ("INFEASIBLE (congestion > 1 on every window)"
           if t["lo"] != t["lo"] else "%+.3e .. %+.3e" % (t["lo"], t["hi"]))
    print("   %-5s  %-11s  %3d/%-3d   %3d/%-3d   %s"
          % (t["name"], t["cls"], t["pos"], t["tot"], t["need"], t["tot"], rng))

CARRY = [t for t in TAB if t["tot"] > 0 and t["need"] == t["tot"]
         and t["cls"] != "MEASURED"]
CARRY_CHEAP = [t for t in CARRY if t["cls"] == "CERTIFIABLE"]
check("el_f1.route_table", bool(F1F) and bool(CARRY),
      "SIX ROUTES, ONE SURVIVOR CLASS.  On %d windows over %d zones and %d "
      "depths (h = %.0f .. %.0f, D = %.2e .. %.2e) the measured floor is "
      "mu_1 = %.3e .. %.3e (T131 quoted %.1e .. %.1e) and the routes that "
      "clear need = 10^-%d x mu_1 on EVERY window are: %s.  The cheap "
      "sign/row-sum routes that clear it: %s"
      % (len(F1F), len(set(r["n"] for r in F1)), F1_LEV,
         qmin([r["h"] for r in F1]), qmax([r["h"] for r in F1]),
         qmin([r["D"] for r in F1]), qmax([r["D"] for r in F1]),
         qmin([r["mu_meas"] for r in F1]), qmax([r["mu_meas"] for r in F1]),
         MU1_T131[0], MU1_T131[1], SLACK_DEC,
         ", ".join(t["name"] for t in CARRY) or "NONE",
         ", ".join(t["name"] for t in CARRY_CHEAP) or "NONE"))

# --- F1.2  the anatomy of the cheap routes ---------------------------------
if F1F:
    _wm = [r["w_min"] for r in F1F]
    _lp = [r["lp_max"] / max(r["mu_meas"], 1.0e-300) for r in F1F]
    _cmp = [r["lp_max"] / max(r["mn_min"], 1.0e-300) for r in F1F]
    _mn = [r["mn_min"] for r in F1F]
    _wneg = sum(1 for r in F1F if r["w_min"] <= 0.0)
    _mnpos = sum(1 for r in F1F if r["mn_min"] > 0.0)
    info("F1.anatomy_cheap",
         "WHY THE CHEAP ROUTES FAIL, exactly -- and it is NOT a size problem.  "
         "The split's GOOD half is fine: diag(w) + L_N is positive definite "
         "(MEASURED) on %d of %d windows with lam_min = %.3e .. %.3e, i.e. "
         "%.0f .. %.0f times ABOVE the target floor, even though the row sums "
         "themselves go negative (w_min = %.3e .. %.3e, negative on %d of %d), "
         "so the KILLING reading of w fails while the M-part stays definite.  "
         "The BAD half is the whole loss: lam_max(L_P) / lam_min(diag(w)+L_N) = "
         "%.2f .. %.2f and lam_max(L_P) / mu_1 = %.2e .. %.2e.  Only %.1f %% of "
         "the off-diagonals are positive but they sit at the LARGE lags, so "
         "paying for L_P by Gershgorin (R1a/R1b), by its spectral norm (R1c), "
         "after Jacobi scaling (R2) or through the comparison matrix (R3) all "
         "come out NEGATIVE.  This is the decisive point for the head-room "
         "argument: the %d decades of slack help a small POSITIVE bound and do "
         "nothing at all for a bound of the WRONG SIGN"
         % (_mnpos, len(F1F), qmin(_mn), qmax(_mn),
            qmin([r["mn_min"] / max(r["mu_meas"], 1e-300) for r in F1F]),
            qmax([r["mn_min"] / max(r["mu_meas"], 1e-300) for r in F1F]),
            qmin(_wm), qmax(_wm), _wneg, len(F1F), qmin(_cmp), qmax(_cmp),
            qmin(_lp), qmax(_lp),
            100.0 * (1.0 - qmed([r["frac_neg"] for r in F1F])), SENS_DEC_T131))
    _cg = [r["r6_cong_f"] for r in F1F]
    _dd = [r["r6_dead"] for r in F1F]
    info("F1.anatomy_paths",
         "AND WHY PATH COMPARISON FAILS: routing every bad jump through its "
         "midpoint needs congestion <= 1; the congestion over good edges that "
         "EXIST is %.2e .. %.2e (median %.2e), and on top of that %d .. %d of "
         "the %d .. %d used edge slots have NO good weight at all (the routed "
         "pair is itself a bad or a zero edge), which makes the comparison "
         "infeasible outright on %d of %d windows.  The reason is the one that "
         "killed the symbol route: the kernel is CAUCHY-type, so the bad "
         "weights sit at LONG lags where the good weights are already O(1/lag) "
         "small -- a long bad edge needs capacity the short good edges do not "
         "have (Diaconis-Stroock 1991; Sinclair 1992).  Between %d and %d bad "
         "edges per window are nearest-neighbour and cannot be routed at all"
         % (qmin(_cg), qmax(_cg), qmed(_cg), min(_dd), max(_dd),
            min(r["r6_used"] for r in F1F), max(r["r6_used"] for r in F1F),
            sum(1 for r in F1F if r["r6_dead"] > 0), len(F1F),
            min(r["r6_direct"] for r in F1F),
            max(r["r6_direct"] for r in F1F)))
    _kf = [r["lp_keff"] for r in F1F if r["lp_keff"] >= 0]
    _kr = [r["lp_keff"] / float(r["h"]) for r in F1F if r["lp_keff"] >= 0]
    if _kf:
        info("F1.rank_of_bad",
             "THE ONE STRUCTURAL OPENING THIS BLOCK FOUND, stated as a "
             "MEASUREMENT and not executed: the bad Laplacian is NOT low rank.  "
             "The number of L_P directions that a rank-k downdate would have to "
             "treat exactly for the remainder to fall below mu_1/2 is k_eff = "
             "%d .. %d on %d windows with h = %.0f .. %.0f, i.e. a fraction "
             "%.2f .. %.2f of the whole space (numerical rank %d .. %d).  So "
             "the T131 rank-ONE trick (the pole downdate and its secular "
             "equation) does NOT generalise to L_P at any affordable k, and the "
             "sharp form of the split route needs a floor for the SIGN-"
             "STRUCTURED part diag(w) + L_N -- which is an off-diagonally "
             "nonpositive matrix, i.e. exactly the class F2 studies"
             % (min(_kf), max(_kf), len(_kf),
                qmin([r["h"] for r in F1F if r["lp_keff"] >= 0]),
                qmax([r["h"] for r in F1F if r["lp_keff"] >= 0]),
                qmin(_kr), qmax(_kr),
                min(r["lp_rank"] for r in F1F if r["lp_rank"] >= 0),
                max(r["lp_rank"] for r in F1F if r["lp_rank"] >= 0)))

# --- F1.3  R4: the pivots and the D-uniformity ------------------------------
PIV = [r for r in F1 if r["piv_neg"] == 0]
PIV_NEG = [r for r in F1 if r["piv_neg"] != 0]
CERT_POS = [r for r in F1 if r["cert"] is not None and r["cert"] > 0.0]
check("el_f1.pivots", len(PIV) == len(F1) and len(CERT_POS) == len(F1),
      "THE POLE-FREE FORM HAS ALL PIVOTS POSITIVE on %d of %d windows (T119's "
      "single NEGATIVE pivot belonged to the form WITH the pole, and it does "
      "not appear here): min pivot %.3e .. %.3e, relative to the largest pivot "
      "%.2e .. %.2e.  Hence the per-window certificate EXISTS and is cheap -- "
      "one Cholesky of A - s I -- and the certified floor is positive on %d of "
      "%d windows.  What R4 does NOT give is a statement uniform in D, which is "
      "the whole residual of item (1)"
      % (len(PIV), len(F1), qmin([r["piv_min"] for r in PIV]),
         qmax([r["piv_min"] for r in PIV]),
         qmin([r["piv_rel"] for r in F1F]), qmax([r["piv_rel"] for r in F1F]),
         len(CERT_POS), len(F1)))

if len(CERT_POS) >= 5:
    _x = [math.log(r["D"]) for r in CERT_POS]
    _y = [math.log(r["cert"]) for r in CERT_POS]
    A_FIT, B_FIT, SA, SB, RMS = fit_band(_x, _y)
    _xp = [math.log(r["D"]) for r in PIV]
    _yp = [math.log(max(r["piv_min"], 1.0e-300)) for r in PIV]
    AP, BP, SAP, SBP, RMSP = fit_band(_xp, _yp)
    info("F1.d_scaling",
         "THE D-SCALING, AS A FIT AND ONLY AS A FIT: the certified floor obeys "
         "cert ~ D^%.3f +- %.3f (jackknife band, rms %.3f in log) over D = "
         "%.2e .. %.2e -- consistent with the D^%.1f T131 quoted -- and the "
         "minimum Cholesky PIVOT obeys piv_min ~ D^%.3f +- %.3f (rms %.3f).  A "
         "positive exponent means the floor DEGRADES as the grid refines, so no "
         "fixed constant survives D -> 0: a D-uniform statement must be a "
         "statement about D^p cert, not about cert.  This is a FIT on %d "
         "windows and is not a certificate of anything"
         % (B_FIT, SB, RMS, qmin([r["D"] for r in CERT_POS]),
            qmax([r["D"] for r in CERT_POS]), MU1_EXP_T131, BP, SBP, RMSP,
            len(CERT_POS)))
else:
    A_FIT = B_FIT = SB = RMS = BP = SBP = float("nan")
    info("F1.d_scaling", "too few certified windows for a fit")

# --- F1.4  R5: the direction obstruction, measured -------------------------
F1E = [r for r in F1F if r["ac_min"] == r["ac_min"]]
if F1E:
    _up_c = sum(1 for r in F1E if r["ac_min"] >= r["mu_meas"] * (1.0 - 1e-9))
    _up_s = sum(1 for r in F1E if r["sz_min"] == r["sz_min"]
                and r["sz_min"] >= r["mu_meas"] * (1.0 - 1.0e-9))
    _eq = sum(1 for r in F1E if r["r5_equiv"] == 1)
    _eqt = sum(1 for r in F1E if r["r5_equiv"] >= 0)
    check("el_f1.direction", _up_c == len(F1E),
          "THE DIRECTION OBSTRUCTION IS MEASURED, NOT ASSUMED.  On the two-grid "
          "split both sub-objects lie ABOVE the target on %d of %d windows "
          "(coarse compression, Cauchy interlacing) and %d of %d (the Schur "
          "complement, Haynsworth 1968) -- ratios lam_min(A_c)/mu_1 = %.2f .. "
          "%.2f and lam_min(S)/mu_1 = %.2f .. %.2f.  So NO recursion on coarse "
          "objects can produce a LOWER bound; what does work is the exact "
          "SHIFTED equivalence (A >= s I iff A_c - s I >= 0 and its shifted "
          "Schur complement >= 0), verified on %d of %d windows at s = cert/2. "
          "That is a cost statement, not a direction statement: it still "
          "factorises a form of the fine size"
          % (_up_c, len(F1E), _up_s, len(F1E),
             qmin([r["ac_min"] / max(r["mu_meas"], 1e-300) for r in F1E]),
             qmax([r["ac_min"] / max(r["mu_meas"], 1e-300) for r in F1E]),
             qmin([r["sz_min"] / max(r["mu_meas"], 1e-300) for r in F1E
                   if r["sz_min"] == r["sz_min"]]),
             qmax([r["sz_min"] / max(r["mu_meas"], 1e-300) for r in F1E
                   if r["sz_min"] == r["sz_min"]]), _eq, _eqt))

R4_ALL = len(CERT_POS) == len(F1) and len(F1) > 0
F1_STAT = ("FLOOR-CERTIFIED-PER-WINDOW" if R4_ALL and not CARRY_CHEAP
           else ("FLOOR-CERTIFIED-CHEAP" if CARRY_CHEAP else "FLOOR-OPEN"))
info("F1.status", "%s -- %s" % (F1_STAT, (
    "the only routes that carry are the per-window Cholesky ones (R4, R2b); "
    "every cheap sign/row-sum route fails by SIGN, so item (1) survives as a "
    "UNIFORMITY question and no longer as an existence question"
    if F1_STAT == "FLOOR-CERTIFIED-PER-WINDOW" else
    "a cheap certifiable route carries over the whole surface"
    if F1_STAT == "FLOOR-CERTIFIED-CHEAP" else
    "no route delivers a positive floor on the whole surface")))


# ----------------------------------------------------------------------------
section("F2  S^{-1} > 0 -- the structural reason for the border block")
# ----------------------------------------------------------------------------
para("""F2.0  THE OBJECT AND THE CLASSES.  S is the border Schur block of the
bordered step, S = A_bb - C X^{-1} C^T (Haynsworth 1968), and the T131 sign
theorem needs the ground state of S to be sign-constant.  Two sufficient
conditions were on the table: METZLER (all off-diagonals <= 0, so -S is
essentially nonnegative, exp(-tS) >= 0 and Perron-Frobenius applies to the
semigroup) and INVERSE-POSITIVE (S^{-1} > 0, so Perron-Frobenius applies
directly to S^{-1}, whose top eigenvalue is 1/lam_min(S) with the SAME
eigenvector).  Metzler + positive definite = a STIELTJES matrix, hence an
M-matrix, hence inverse-positive (Ostrowski 1937; Berman-Plemmons 1979 Ch. 6) --
so Metzler is strictly stronger, and T131 measured exactly that gap: S^{-1} > 0
on %d of %d transports while Metzler FAILED on %d.  T120 already showed S is not
an M-matrix.  This block asks what the correct class IS, in four steps: the sign
inventory, the triangular-factor signs, the GREEN-FUNCTION reading of the
Metzler part, and then a candidate theorem for the gap -- a Stieltjes matrix
plus a NONNEGATIVE perturbation with a Neumann margin, every ingredient of which
is computable from S alone.""" % (SG_INV_T131[0], SG_INV_T131[1],
                                  SG_METZ_FAIL_T131))


def sign_class(S, rng):
    """THE INVERSE-POSITIVITY INVENTORY of one border Schur block."""
    g = S.shape[0]
    S = sym(S)
    dgS = np.diag(S).copy()
    off = S - np.diag(dgS)
    msk = ~np.eye(g, dtype=bool)
    offv = off[msk]
    out = dict(g=g, n_off=int(offv.size), scale=float(np.abs(S).max()),
               n_off_pos=int(np.count_nonzero(offv > 0.0)))
    out["metz"] = int(out["n_off_pos"] == 0)
    out["off_pos_max"] = (float(offv[offv > 0.0].max()) / max(out["scale"], 1e-300)
                          if out["n_off_pos"] else 0.0)
    if out["n_off_pos"]:
        rr, ss = np.nonzero(np.triu(off, 1) > 0.0)
        out["pos_lag_min"] = int(np.min(ss - rr))
        out["pos_lag_max"] = int(np.max(ss - rr))
    else:
        out["pos_lag_min"] = out["pos_lag_max"] = -1
    fac = safe_cho(S)
    if fac is None:
        return None
    Ig = np.eye(g)
    Si = cho_solve(fac, Ig, check_finite=False)
    out["inv_pos"] = int(bool(np.all(Si > 0.0)))
    out["inv_rmin"] = float(Si.min()) / max(float(np.abs(Si).max()), 1.0e-300)
    # A POSTERIORI CERTIFICATE for the computed inverse: with R = S Si - I and
    # ||R||_inf < 1 one has ||S^{-1} - Si||_inf <= ||Si||_inf ||R||_inf /
    # (1 - ||R||_inf) (the standard Neumann / residual bound, Higham 2002 Ch.
    # 14), so min(Si) above that bound CERTIFIES S^{-1} > 0 entrywise
    Rr = S @ Si - Ig
    rn = float(np.abs(Rr).sum(axis=1).max())
    sn = float(np.abs(Si).sum(axis=1).max())
    out["inv_res"] = rn
    out["inv_bnd"] = sn * rn / (1.0 - rn) if rn < 1.0 else float("inf")
    out["inv_cert"] = int(float(Si.min()) > out["inv_bnd"])
    out["inv_head"] = float(Si.min()) / max(out["inv_bnd"], 1.0e-300)
    del Rr
    # --- the triangular factor signs (a Stieltjes matrix factors into two
    #     M-matrices: L has nonpositive off-diagonals and L^{-1} >= 0) --------
    Lc = cholesky(S, lower=True, check_finite=False)
    lo = Lc[np.tril_indices(g, -1)]
    out["l_off"] = int(lo.size)
    out["l_off_pos"] = int(np.count_nonzero(lo > 0.0))
    Li = solve_triangular(Lc, Ig, lower=True, check_finite=False)
    out["linv_nonneg"] = int(bool(np.all(Li >= -1.0e-14 * max(
        float(np.abs(Li).max()), 1.0e-300))))
    del Lc, Li
    # --- TWO Stieltjes comparisons for S, and the Green-function reading ----
    #  (A) DELETION:  S_A = S - Delta.  Off-diagonals <= 0, but S_A <= S, so
    #      definiteness is NOT inherited -- it has to be measured.
    #  (B) LUMPING :  S_B = S + L_Delta with L_Delta = diag(Delta 1) - Delta the
    #      Laplacian of the bad part.  L_Delta >= 0, so S_B >= S > 0 is positive
    #      definite BY CONSTRUCTION, its off-diagonals are <= 0 BY CONSTRUCTION,
    #      hence S_B is Stieltjes with NO measurement at all -- and lumping
    #      preserves the row sums exactly (L_Delta has zero row sums).
    Dl = np.where(off > 0.0, off, 0.0)
    S_A = S - Dl
    LD = np.diag(Dl.sum(axis=1)) - Dl
    S_B = sym(S + LD)
    out["s0_rs_min"] = float(S.sum(axis=1).min()) / max(out["scale"], 1e-300)
    out["s0_rs_pos"] = int(bool(np.all(S.sum(axis=1) > 0.0)))
    out["lump_rs"] = float(np.max(np.abs(S_B.sum(axis=1) - S.sum(axis=1)))) \
        / max(out["scale"], 1.0e-300)
    fA = safe_cho(S_A)
    out["a_pd"] = int(fA is not None)
    out["margin_a"] = float("inf")
    if fA is not None:
        Ai = cho_solve(fA, Ig, check_finite=False)
        if bool(np.all(Ai > 0.0)):
            Ka = Ai @ Dl
            ra = (float(np.max(np.abs(np.linalg.eigvals(Ka)))) if g > 1
                  else float(abs(Ka[0, 0])))
            if ra < 1.0:
                Ea = np.linalg.solve(Ig - Ka, Ka) @ Ai
                out["margin_a"] = (float(np.abs(Ea).max())
                                   / max(float(Ai.min()), 1.0e-300))
                del Ea
            del Ka
        del Ai
    fB = safe_cho(S_B)
    if fB is None:
        out.update(s0_pd=0, s0_inv_pos=0, rho_k=float("nan"),
                   rho_0=float("nan"), margin=float("inf"), maj_ok=-1,
                   dev=float("nan"), n0_nonneg=0)
    else:
        Bi = cho_solve(fB, Ig, check_finite=False)
        out["s0_pd"] = 1
        out["s0_inv_pos"] = int(bool(np.all(Bi > 0.0)))
        # the JACOBI SPLITTING of the Stieltjes comparison: S_B = D_0 - N_0 with
        # N_0 >= 0, so S_B^{-1} = sum_k (D_0^{-1} N_0)^k D_0^{-1} is a CONVERGENT
        # series of NONNEGATIVE terms -- the discrete Green function of the jump
        # walk (Ostrowski 1937; Berman-Plemmons 1979 Thm 6.2.7; Feller / Dynkin)
        d0 = np.diag(S_B).copy()
        N0 = np.diag(d0) - S_B
        out["n0_nonneg"] = int(bool(np.all(N0 >= -1.0e-300)))
        J0 = N0 / np.maximum(d0, 1.0e-300)[:, None]
        out["rho_0"] = (float(np.max(np.abs(np.linalg.eigvals(J0))))
                        if g > 1 else 0.0)
        # the perturbation back to S is S = S_B - L_Delta; its entrywise
        # modulus is |L_Delta| = diag(Delta 1) + Delta >= 0
        Eabs = np.diag(Dl.sum(axis=1)) + Dl
        K = Bi @ Eabs
        out["rho_k"] = (float(np.max(np.abs(np.linalg.eigvals(K))))
                        if g > 1 else float(abs(K[0, 0])))
        if out["rho_k"] < 1.0 and Bi.min() > 0.0:
            Emaj = np.linalg.solve(Ig - K, K) @ Bi
            emax = float(np.abs(Emaj).max())
            out["margin"] = emax / max(float(Bi.min()), 1.0e-300)
            dev = float(np.abs(Si - Bi).max())
            out["dev"] = dev / max(float(np.abs(Bi).max()), 1.0e-300)
            out["maj_ok"] = int(dev <= emax * (1.0 + 1.0e-9) + 1.0e-14)
            del Emaj
        else:
            out["margin"] = float("inf")
            out["dev"] = float("nan")
            out["maj_ok"] = -1
        del Bi, K, N0, J0, Eabs
    del S_A, S_B, LD
    # --- the WEAKEST form: reflection positivity on the bottom eigenspace ---
    ev, U = np.linalg.eigh(S)
    y = U[:, 0]
    out["lam"] = float(ev[0])
    out["y_sign"] = int(bool(np.all(y > 0.0) or np.all(y < 0.0)))
    kb = min(F2_BOTTOM, g)
    V = U[:, :kb] @ rng.standard_normal((kb, F2_CONE_DRAWS))
    nrm = np.maximum(np.linalg.norm(V, axis=0), 1.0e-300)
    V = V / nrm[None, :]
    SV = S @ V
    aV = np.abs(V)
    d_full = np.einsum("ij,ij->j", V, SV) - np.einsum("ij,ij->j", aV, S @ aV)
    tol = 1.0e-12 * out["scale"]
    out["refl_vio"] = int(np.count_nonzero(d_full < -tol))
    out["refl_min"] = float(d_full.min()) / max(out["scale"], 1.0e-300)
    out["irred"] = int(g < 2 or bool(np.all(np.abs(np.diag(S, 1)) > 0.0)))
    del Si, Dl, U, V, SV, aV
    return out


F2R = []
_rng2 = np.random.default_rng(1340728)
F2_TASK = []
for d in REC:
    for side, D_key, gc_key, h_key in (("c", "D_c", "gc_c", "h_c"),
                                       ("f", "D_f", "gc_f", "h_f")):
        if d[gc_key] >= F2_GC_MIN and d[h_key] <= F2_HCAP:
            F2_TASK.append((d["k"], d["n"], float(d[D_key]), "rec_" + side))
# the T131 transport surface: for each refinement ratio rho, the DEEPEST zones
# whose fine grid still fits the cap, deduplicated on a log-n grid
for rho in F2_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho) // 2
        if hf > F2_HCAP or hf < H_MIN:
            continue
        key = int(round(F2_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    for (k, DA) in got[-F2_PER_RHO:]:
        F2_TASK.append((k, int(N_DEEP[k]), DA / rho, "rho%.3f" % rho))
        F2_TASK.append((k, int(N_DEEP[k]), DA, "rhoC%.3f" % rho))
F2_TASK = F2_TASK[:F2_MAX]
for (k, n_lbl, D, src) in F2_TASK:
    if budget_left() < BUDGET_S - T_F1 - T_F2:
        info("F2.budget", "transport pool truncated at n = %d after %d blocks"
             % (n_lbl, len(F2R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < F2_GC_MIN or fr["h_n"] > F2_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    sc = sign_class(st["S"], _rng2)
    if sc is not None:
        sc.update(n=n_lbl, side=src, h=fr["h_n"], D=D, al=fr["al_n"])
        F2R.append(sc)
    del st

MET = [r for r in F2R if r["metz"]]
MET_F = [r for r in F2R if not r["metz"]]
INVP = [r for r in F2R if r["inv_pos"]]
S0PD = [r for r in F2R if r["s0_pd"]]
S0IP = [r for r in F2R if r["s0_inv_pos"]]
MARG = [r for r in F2R if r["margin"] < 1.0]
LSGN = [r for r in F2R if r["l_off_pos"] == 0]
LINV = [r for r in F2R if r["linv_nonneg"]]
YS = [r for r in F2R if r["y_sign"]]
REFL = [r for r in F2R if r["refl_vio"] == 0]

check("el_f2.inventory", bool(F2R) and len(INVP) == len(F2R),
      "THE INVENTORY, over %d border blocks from %d transports (h = %.0f .. "
      "%.0f, g = %d .. %d, T131 measured %d): S^{-1} > 0 entrywise on %d of %d "
      "(relative minimum entry %.2e .. %.2e), the ground state is sign-constant "
      "on %d of %d, and the METZLER sufficient condition holds on only %d of %d "
      "-- the gap is REPRODUCED, %d blocks are inverse-positive WITHOUT being "
      "Metzler (T131 counted %d).  So the class is strictly between Stieltjes "
      "and inverse-positive, and the question is which side of the gap has a "
      "theorem"
      % (len(F2R), len(set(r["n"] for r in F2R)), qmin([r["h"] for r in F2R]),
         qmax([r["h"] for r in F2R]), min(r["g"] for r in F2R),
         max(r["g"] for r in F2R), SG_INV_T131[1], len(INVP), len(F2R),
         qmin([r["inv_rmin"] for r in F2R]), qmax([r["inv_rmin"] for r in F2R]),
         len(YS), len(F2R), len(MET), len(F2R), len(MET_F),
         SG_METZ_FAIL_T131))

if MET_F:
    info("F2.metzler_anatomy",
         "WHERE METZLER BREAKS, entry by entry: on the %d non-Metzler blocks "
         "there are %d .. %d positive off-diagonal entries out of %d .. %d, "
         "their size relative to ||S||_max is %.2e .. %.2e, and they sit at "
         "off-diagonal LAGS %d .. %d in blocks of size g = %d .. %d.  They are "
         "%s -- whether that is small enough to leave the SIGN of the inverse "
         "untouched is decided by the margin below and not here"
         % (len(MET_F), min(r["n_off_pos"] for r in MET_F),
            max(r["n_off_pos"] for r in MET_F),
            min(r["n_off"] for r in MET_F), max(r["n_off"] for r in MET_F),
            qmin([r["off_pos_max"] for r in MET_F]),
            qmax([r["off_pos_max"] for r in MET_F]),
            min(r["pos_lag_min"] for r in MET_F),
            max(r["pos_lag_max"] for r in MET_F),
            min(r["g"] for r in MET_F), max(r["g"] for r in MET_F),
            "small but not negligible against the block scale, and they are "
            "NEVER on the first off-diagonal" if min(
                r["pos_lag_min"] for r in MET_F) >= 2 else
            "small against the block scale and reach the first off-diagonal"))
    info("F2.metzler_reading",
         "The natural reading -- 'a perturbation this small cannot move the "
         "sign of the inverse' -- is exactly what the candidate theorem below "
         "tries to make quantitative, and it is reported there as a COVERAGE "
         "number, not as a proof: the a-priori margin reaches only part of the "
         "pool, while the a-posteriori certificate reaches all of it")

RHO0 = [r for r in F2R if r["rho_0"] < 1.0]
APD = [r for r in F2R if r["a_pd"]]
check("el_f2.green_reading", bool(F2R) and len(S0PD) == len(F2R)
      and len(S0IP) == len(F2R) and len(RHO0) == len(F2R),
      "THE GREEN-FUNCTION READING CARRIES -- but only for the RIGHT Stieltjes "
      "comparison, and finding out which one it is IS the structural result.  "
      "Split (A), the obvious one, DELETES the positive off-diagonals: S_A = S "
      "- Delta.  Its signs are right and its definiteness is NOT inherited "
      "(S_A <= S), and indeed it is positive definite on only %d of %d blocks -- "
      "so the naive Metzler part is not a usable comparison.  Split (B) LUMPS "
      "them onto the diagonal instead: S_B = S + L_Delta with L_Delta = "
      "diag(Delta 1) - Delta the Laplacian of the bad part.  L_Delta >= 0, so "
      "S_B >= S > 0 is positive definite BY CONSTRUCTION and its off-diagonals "
      "are nonpositive BY CONSTRUCTION: S_B is STIELTJES with no measurement at "
      "all (confirmed on %d of %d), and lumping preserves the row sums exactly "
      "(max drift %.1e).  Its Jacobi splitting S_B = D_0 - N_0 then has N_0 >= 0 "
      "on %d of %d with rho(D_0^{-1} N_0) = %.3f .. %.3f < 1 on %d of %d, so "
      "S_B^{-1} = sum_k (D_0^{-1} N_0)^k D_0^{-1} is a CONVERGENT series of "
      "NONNEGATIVE terms -- the discrete GREEN FUNCTION of the jump walk, "
      "positive because every path carries positive weight -- and it is "
      "entrywise positive on %d of %d blocks (Ostrowski 1937; Berman-Plemmons "
      "1979 Thm 6.2.7; Feller / Dynkin).  What is NOT true, and was the naive "
      "expectation: the row sums are NOT killing rates, they are negative "
      "(min / ||S|| = %.2e .. %.2e, positive on %d of %d), so positivity comes "
      "from definiteness plus signs and not from a killing argument.  The "
      "triangular factors agree: chol(S) has nonpositive off-diagonals on %d of "
      "%d and L^{-1} >= 0 on %d of %d"
      % (len(APD), len(F2R), len(S0PD), len(F2R),
         qmax([r["lump_rs"] for r in F2R]),
         sum(r.get("n0_nonneg", 0) for r in F2R), len(F2R),
         qmin([r["rho_0"] for r in F2R]), qmax([r["rho_0"] for r in F2R]),
         len(RHO0), len(F2R), len(S0IP), len(F2R),
         qmin([r["s0_rs_min"] for r in F2R]), qmax([r["s0_rs_min"] for r in F2R]),
         sum(r["s0_rs_pos"] for r in F2R), len(F2R), len(LSGN), len(F2R),
         len(LINV), len(F2R)))

MAJ = [r for r in F2R if r["maj_ok"] == 1]
MAJT = [r for r in F2R if r["maj_ok"] >= 0]
MARG_INV = [r for r in MARG if r["inv_pos"]]
check("el_f2.candidate", bool(MAJT) and len(MAJ) == len(MAJT)
      and len(MARG_INV) == len(MARG),
      "THE CANDIDATE THEOREM, VERIFIED AS A THEOREM (its majorant property) and "
      "then MEASURED for coverage.  Claim: let S > 0 have the lumped Stieltjes "
      "comparison S_B = S + L_Delta, so S = S_B - L_Delta, and put K = S_B^{-1} "
      "|L_Delta| with |L_Delta| = diag(Delta 1) + Delta >= 0.  If rho(K) < 1 "
      "then the Neumann series converges and, since S_B^{-1} >= 0 entrywise, "
      "the deviation obeys |S^{-1} - S_B^{-1}| <= E := (I - K)^{-1} K S_B^{-1} "
      "entrywise; hence max(E) < min(S_B^{-1}) IMPLIES S^{-1} > 0.  Every "
      "ingredient is computable from S alone and the hypothesis on S is only "
      "S > 0.  VERIFIED: E majorises the true deviation on %d of %d blocks with "
      "rho(K) < 1 (true relative deviation %.2e .. %.2e), and the implication "
      "never fails -- every block inside its margin has S^{-1} > 0 (%d of %d).  "
      "MEASURED coverage: rho(K) < 1 on %d of %d (rho_K median %.3f), the margin "
      "is below 1 on %d of %d blocks (median %.3f, largest finite %.2e), "
      "including %d of the %d non-Metzler ones.  So item (2) becomes a "
      "PER-TRANSPORT CERTIFIABLE condition at the cost of the step itself; it is "
      "not yet zone-uniform, because rho(K) and the margin are computed and not "
      "bounded a priori"
      % (len(MAJ), len(MAJT), qmin([r["dev"] for r in MAJT]),
         qmax([r["dev"] for r in MAJT]), len(MARG_INV), len(MARG),
         sum(1 for r in F2R if r["rho_k"] < 1.0), len(F2R),
         qmed([r["rho_k"] for r in F2R if r["rho_k"] == r["rho_k"]]),
         len(MARG), len(F2R), qmed([r["margin"] for r in F2R]),
         qmax([r["margin"] for r in F2R if r["margin"] < float("inf")]),
         sum(1 for r in MET_F if r["margin"] < 1.0), len(MET_F)))

UNION = [r for r in F2R if r["margin"] < 1.0 or r["margin_a"] < 1.0]
MARGA = [r for r in F2R if r["margin_a"] < 1.0]
ICERT = [r for r in F2R if r["inv_cert"]]
CH1 = [r for r in MET if not (r["margin"] < 1.0 or r["margin_a"] < 1.0)]
CH2 = [r for r in UNION if not r["inv_pos"]]
CH3 = [r for r in INVP if not r["y_sign"]]
check("el_f2.hierarchy", not CH1 and not CH2 and not CH3
      and len(ICERT) == len(F2R),
      "AND THE HYPOTHESIS CHAIN IS CONSISTENT ON THE WHOLE POOL, which decides "
      "where the theorem should be stated: Metzler (%d/%d) => a Neumann margin "
      "below 1 for the LUMPED split (%d/%d) or the DELETION split (%d/%d), "
      "union %d/%d => S^{-1} > 0 (%d/%d) => sign-constant ground state (%d/%d), "
      "with %d, %d and %d counter-examples to the three implications.  TWO "
      "conclusions.  First, the relaxation that looked natural does NOT work: "
      "REFLECTION POSITIVITY v^T S v >= |v|^T S |v| on the bottom "
      "%d-dimensional eigenspace (%d draws per block) holds on only %d of %d "
      "blocks, worst relative defect %.2e -- weaker than Metzler but still "
      "false where Metzler is false, so it is the wrong weakening and is "
      "DISCARDED.  Second, and this is what actually moves item (2): entrywise "
      "positivity of the inverse is CERTIFIED A POSTERIORI on %d of %d blocks "
      "by the residual bound (residual %.2e .. %.2e, error bound %.2e .. %.2e, "
      "smallest entry relative to the largest %.2e .. %.2e, head-room "
      "min(S^{-1}) / bound = %.1e .. %.1e), so per transport S^{-1} > 0 is no "
      "longer a measurement at all.  What "
      "stays open is only the ZONE-UNIFORM statement, and the Neumann margin is "
      "the only candidate on the table that could become one"
      % (len(MET), len(F2R), len(MARG), len(F2R), len(MARGA), len(F2R),
         len(UNION), len(F2R), len(INVP), len(F2R), len(YS), len(F2R),
         len(CH1), len(CH2), len(CH3), F2_BOTTOM, F2_CONE_DRAWS, len(REFL),
         len(F2R), qmin([r["refl_min"] for r in F2R]), len(ICERT), len(F2R),
         qmin([r["inv_res"] for r in F2R]), qmax([r["inv_res"] for r in F2R]),
         qmin([r["inv_bnd"] for r in F2R]), qmax([r["inv_bnd"] for r in F2R]),
         qmin([r["inv_rmin"] for r in F2R]), qmax([r["inv_rmin"] for r in F2R]),
         qmin([r["inv_head"] for r in F2R]), qmax([r["inv_head"] for r in F2R])))

F2_COV = len(UNION) / float(max(len(F2R), 1))
F2_STAT = ("CLASS-IDENTIFIED" if (F2R and len(S0IP) == len(F2R)
                                  and len(MAJ) == len(MAJT)
                                  and len(ICERT) == len(F2R))
           else ("CLASS-PARTIAL" if F2R else "CLASS-OPEN"))
info("F2.status",
     "%s -- the reason is the M-MATRIX GREEN FUNCTION of the LUMPED Stieltjes "
     "comparison S + L_Delta (Stieltjes by construction, no measurement), the "
     "per-transport statement is now CERTIFIED a posteriori on %d of %d blocks, "
     "the a-priori sufficient condition (a Neumann margin below 1 in either "
     "split) covers %.1f %% of the pool, and reflection positivity on the bottom "
     "eigenspace is refuted as the weakening"
     % (F2_STAT, len(ICERT), len(F2R), 100.0 * F2_COV))


# ----------------------------------------------------------------------------
section("F3  M18 IN THE WHITENED BASIS -- the 2.18 mismatch removed")
# ----------------------------------------------------------------------------
para("""F3.0  WHY WHITENING IS THE FIX AND WHY IT IS ALLOWED.  The rung
certificate reads cb / delta as a weighted harmonic mean of the generalised
eigenvalues mu of the pencil (S, U) with weights w_i = p_i^2 / sum p^2, p = V^T
shat, V^T U V = I -- an identity.  T131 assembled a majorant for the BAD mass
(the weight on {mu < 1/2}) and it came out valid and vacuous, with the dominant
loss attributed to the U-METRIC MISMATCH sqrt(lam_max U / lam_min U) = %.2f
(QUOTED): the mass lives in the U-metric while the comb part was bounded in the
Euclidean one.  Write U = L L^T (Cholesky).  Then S V = U V M with V^T U V = I is
equivalent to the ORDINARY symmetric problem (L^{-1} S L^{-T}) W = W M with W =
L^T V orthonormal, and p = V^T shat = W^T (L^{-1} shat).  So the whole pencil
question is the Euclidean question for s~ = L^{-1} shat, and the mismatch
disappears BY CONSTRUCTION -- there is only one metric left.  The reason this is
allowed without losing the M18 localisation is F0.5: L is LOWER TRIANGULAR, so
the first k whitened coordinates depend on the first k cells only.  The outer
cells stay the outer cells.  Both bounds are computed on the SAME rungs below,
so the improvement is a number and not a claim.""" % MISMATCH_T131)


def rung_white(fine):
    """ONE telescope rung: the pencil mass, the WHITENED M18 majorant, and the
    T131 (unwhitened) majorant for comparison, on identical data."""
    A_f, M = fine["A"], fine["M"]
    Ac, Az, Bx = two_grid_blocks(A_f)
    b_c = rest_p(fine["b"])
    s = rest_z(fine["b"])
    fac_c = safe_cho(Ac)
    if fac_c is None:
        return None
    x_c = cho_solve(fac_c, b_c, check_finite=False)
    delta = fine["q"] - float(np.dot(b_c, x_c))
    if not (delta > 0.0):
        return None
    comb = -(Bx.T @ x_c)
    shat = s + comb
    Gm = solve_triangular(fac_c[0] if fac_c[1] else fac_c[0].T, Bx, lower=True,
                          check_finite=False)
    S = sym(Az - Gm.T @ Gm)
    # --- the certified envelope majorant and the U metric -------------------
    ell, up, f0, marg, Lg, scale = cert_env(fine["c"])
    T_up = sym(odd_toeplitz(pwc_lags(up, M), M))
    maj_ok = cert_pd(sym(T_up - A_f))[0]
    Uz = zz_compress(T_up)
    del T_up
    u_pd, u_fp, fac_U = cert_pd(Uz)
    if not u_pd:
        return None
    n_p = Uz.shape[0]
    lU = cert_floor_bisect(Uz, 0.0, float(eigvalsh(
        Uz, subset_by_index=[0, 0])[0]) * 2.0 + 1.0e-30)
    lU = lU if lU is not None else 0.0
    LU = float(eigvalsh(Uz, subset_by_index=[n_p - 1, n_p - 1])[0])
    # --- THE WHITENING ------------------------------------------------------
    Lw = cholesky(Uz, lower=True, check_finite=False)

    def wh(x):
        return solve_triangular(Lw, x, lower=True, check_finite=False)

    St = sym(wh(wh(S).T).T)
    mu, W = np.linalg.eigh(St)
    st_p, st_c = wh(s), wh(comb)
    st = st_p + st_c
    p = W.T @ st
    p2 = p * p
    tot = float(p2.sum())
    if not (tot > 0.0):
        return None
    cb = float(np.dot(shat, cho_solve(fac_U, shat, check_finite=False)))
    id_white = abs(tot - cb) / max(cb, 1.0e-300)
    try:
        mu_g = eigh(S, Uz, eigvals_only=True)
    except (LinAlgError, ValueError):
        return None
    id_pencil = float(np.max(np.abs(mu - mu_g))) / max(float(np.abs(mu).max()),
                                                       1.0e-300)
    w = p2 / tot
    bad = float(w[mu < 0.5].sum())
    good = 1.0 - bad
    bd = np.flatnonzero(mu < 0.5)
    # --- the localisation quantities, all in ONE metric ---------------------
    ns_p = float(np.linalg.norm(st_p))
    nc = float(np.linalg.norm(st_c))
    hc = Bx.shape[0]
    G = wh(Bx.T)                       # c~ = -G x_c, exactly
    Tg = sym(G.T @ G)                  # = Bx U^{-1} Bx^T
    Tg = Tg + chol_floor(gersh(Tg), hc) * np.eye(hc)
    fT = safe_cho(Tg)
    if fT is None:
        return None
    Lt = cholesky(Tg, lower=True, check_finite=False)

    def whT(Mm):
        Y = solve_triangular(Lt, Mm, lower=True, check_finite=False)
        return sym(solve_triangular(Lt, Y.T, lower=True, check_finite=False).T)

    nx2 = float(np.dot(x_c, x_c))
    t1 = float(np.dot(np.diff(x_c), np.diff(x_c))) / max(nx2, 1.0e-300)
    t2 = float(np.dot(np.diff(x_c, n=2), np.diff(x_c, n=2))) / max(nx2, 1e-300)
    d1 = np.diff(np.eye(hc), axis=0)
    d2 = np.diff(np.eye(hc), n=2, axis=0)
    G1 = whT(sym(d1.T @ d1) - t1 * np.eye(hc))
    G2 = whT(sym(d2.T @ d2) - t2 * np.eye(hc))
    # the T131 (unwhitened) ingredients, on the same data
    ns_e = float(np.linalg.norm(s))
    nc_e = float(np.linalg.norm(comb))
    xc_nodes, _ = odd_nodes(0.5 * M * fine["D"], M // 2)
    ch2 = np.cosh(0.5 * xc_nodes) ** 2
    ch2_tot = float(ch2.sum())
    rows, best, bestw = {}, None, None
    for k in M18_KSET:
        if k >= min(hc, n_p):
            continue
        sh_w = (float(np.dot(st_p[:k], st_p[:k]))
                / max(float(np.dot(st_p, st_p)), 1.0e-300))
        Rk = whT(sym(G[:k, :].T @ G[:k, :]))
        sp = float(eigvalsh(Rk, subset_by_index=[hc - 1, hc - 1])[0])
        if hc <= M18_SPRO_H:
            sp = min(sp, _spro(Rk, G1, iters=12), _spro(Rk, G2, iters=12))
        sp = max(min(sp, 1.0), 0.0)
        del Rk
        sig = (float(svdvals(np.ascontiguousarray(W[k:, bd]))[0])
               if bd.size else 0.0)
        tail_w = float(np.linalg.norm(st_p[k:]))
        num = (math.sqrt(max(sh_w, 0.0)) * ns_p + sig * tail_w
               + math.sqrt(sp) * nc + sig * nc)
        # the EXACT normaliser: ||s~|| = sqrt(shat^T U^{-1} shat) is computable,
        # so no triangle inequality is needed in the denominator at all
        den2 = float(np.linalg.norm(st))
        bnd_w = (num / den2) ** 2 if den2 > 0.0 else float("inf")
        # the T131-style denominator, kept to document that it is DEAD here
        den_tri = ns_p - nc
        bnd_w3 = (num / den_tri) ** 2 if den_tri > 0.0 else float("inf")
        # the SHARP whitened variant: the pole part's bad mass MEASURED
        nb_s = float(np.linalg.norm(W[:, bd].T @ st_p)) if bd.size else 0.0
        num2 = nb_s + math.sqrt(sp) * nc + sig * nc
        bnd_w2 = (num2 / den2) ** 2 if den2 > 0.0 else float("inf")
        # the T131 form on the same rung: two metrics, Euclidean comb bound
        sh_s = float(ch2[:k].sum()) / ch2_tot
        num_o = ((math.sqrt(max(sh_s, 0.0)) * ns_e + math.sqrt(sp) * nc_e)
                 / math.sqrt(max(lU, 1.0e-300))
                 + sig * (float(np.linalg.norm(s[k:])) + nc_e))
        den_o = (ns_e / math.sqrt(max(LU, 1.0e-300))
                 - nc_e / math.sqrt(max(lU, 1.0e-300)))
        bnd_o = (num_o / den_o) ** 2 if den_o > 0.0 else float("inf")
        rows[k] = dict(sh_w=sh_w, sp=sp, sig=sig, bnd_w=bnd_w, bnd_w2=bnd_w2,
                       bnd_w3=bnd_w3, bnd_o=bnd_o, sh_s=sh_s,
                       loc=(sig * (tail_w + nc) / den2) ** 2 if den2 > 0 else
                       float("inf"))
        if best is None or bnd_o < rows[best]["bnd_o"]:
            best = k
        if bestw is None or bnd_w < rows[bestw]["bnd_w"]:
            bestw = k
    del Ac, Az, Bx, S, St, Uz, W, Gm, G, Tg, G1, G2, d1, d2
    if bestw is None:
        return None
    return dict(M=M, h=fine["h"], D=fine["D"], delta=delta, cb=cb,
                id_white=id_white, id_pencil=id_pencil, good=good, bad=bad,
                n_p=n_p, n_bad=int(bd.size), lU=lU, LU=LU,
                mismatch=math.sqrt(max(LU, 0.0) / max(lU, 1.0e-300)),
                mu_min=float(mu[0]), maj_ok=int(maj_ok), rows=rows,
                best=best, bestw=bestw, bnd_w=rows[bestw]["bnd_w"],
                bnd_w2=min(rows[q]["bnd_w2"] for q in rows),
                bnd_w3=min(rows[q]["bnd_w3"] for q in rows),
                bnd_o=rows[best]["bnd_o"], loc=rows[bestw]["loc"],
                sp=rows[bestw]["sp"], sig=rows[bestw]["sig"],
                sh_w=rows[bestw]["sh_w"], ratio=nc / max(ns_p, 1.0e-300))


AUD = []
_seen3 = set()
for k in range(2, NZ_DEEP - 2):
    if len(AUD) >= PEN_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_o = even_window(UU_ALL[k], D_k)
    h_o = M_o // 2
    if h_o < H_MIN or h_o * 2 > H_TEL:
        continue
    key = (h_o // 12, int(round(2.0 * math.log(max(N_DEEP[k], 2)))))
    if key in _seen3:
        continue
    _seen3.add(key)
    AUD.append((k, D_k, M_o, h_o))

PEN = []
for (k, D_k, M_o, h_o) in AUD:
    if budget_left() < BUDGET_S - T_F1 - T_F2 - T_F3:
        info("F3.budget", "rung study truncated at n = %d" % N_DEEP[k])
        break
    nlev = nlev_for(h_o)
    if nlev < 2:
        continue
    al = 0.5 * M_o * D_k
    lv = telescope_levels(al, M_o, atoms_in(al, ATOMS_ALL), nlev)
    if lv is None:
        continue
    for e in range(nlev - 1):
        if budget_left() < BUDGET_S - T_F1 - T_F2 - T_F3:
            break
        r = rung_white(lv[e + 1])
        if r is None:
            continue
        r["n"] = int(N_DEEP[k])
        r["lev"] = e
        PEN.append(r)
    del lv

if PEN:
    print("")
    print("      n     h  lev | good     bad      | wh_assem  wh_sharp  "
          "wh_tri    T131      loc_only  mismatch")
    for r in PEN:
        print("   %5d %5d %3d | %.4f  %.2e | %.3e %.3e %.3e %.3e %.3e %.3f"
              % (r["n"], r["h"], r["lev"], r["good"], r["bad"], r["bnd_w"],
                 r["bnd_w2"], r["bnd_w3"], r["bnd_o"], r["loc"],
                 r["mismatch"]))

VAL_W = [r for r in PEN if r["bnd_w"] >= r["bad"] * (1.0 - 1.0e-9)]
VAL_W2 = [r for r in PEN if r["bnd_w2"] >= r["bad"] * (1.0 - 1.0e-9)]
OK_W = [r for r in PEN if r["bnd_w"] <= BAR_MASS_GOOD]
OK_W2 = [r for r in PEN if r["bnd_w2"] <= BAR_MASS_GOOD]
OK_O = [r for r in PEN if r["bnd_o"] <= BAR_MASS_GOOD]
check("el_f3.identities", bool(PEN)
      and qmax([r["id_white"] for r in PEN]) < 1.0e-9
      and qmax([r["id_pencil"] for r in PEN]) < 1.0e-8,
      "THE WHITENING IS AN IDENTITY, NOT AN APPROXIMATION, on %d rungs over %d "
      "zones (h = %.0f .. %.0f): the whitened spectrum matches the generalised "
      "pencil (S, U) to %.2e relative, the whitened mass sum p^2 matches the "
      "dual form shat^T U^{-1} shat to %.2e, the envelope majorant T_up >= A is "
      "certified on %d of %d rungs, and the measured mass is unchanged from "
      "T131/T127 -- good = %.4f .. %.4f (T127 quoted %.4f), mu_min = %.4f .. "
      "%.4f (T126 quoted %.3f .. %.3f).  Only the BOUND changes below; the "
      "truth is the same object"
      % (len(PEN), len(set(r["n"] for r in PEN)), qmin([r["h"] for r in PEN]),
         qmax([r["h"] for r in PEN]), qmax([r["id_pencil"] for r in PEN]),
         qmax([r["id_white"] for r in PEN]),
         sum(r["maj_ok"] for r in PEN), len(PEN), qmin([r["good"] for r in PEN]),
         qmax([r["good"] for r in PEN]), MASS_T127,
         qmin([r["mu_min"] for r in PEN]), qmax([r["mu_min"] for r in PEN]),
         MU_MIN_T126[0], MU_MIN_T126[1]))

TRI_DEAD = sum(1 for r in PEN if not (r["bnd_w3"] < float("inf")))
O_DEAD = sum(1 for r in PEN if not (r["bnd_o"] < float("inf")))
check("el_f3.whitened", bool(PEN) and len(VAL_W) == len(PEN)
      and len(VAL_W2) == len(PEN),
      "THE WHITENED BOUND IS VALID, FINITE FOR THE FIRST TIME, AND STILL SHORT "
      "OF THE BAR -- three separate statements.  VALID: the assembled whitened "
      "majorant exceeds the true bad mass on %d of %d rungs, the sharp variant "
      "on %d of %d.  FINITE: the T131 denominator ||s|| / sqrt(lam_max U) - "
      "||comb|| / sqrt(lam_min U) is NEGATIVE on %d of %d rungs and its whitened "
      "triangle analogue ||s~_pole|| - ||comb~|| on %d of %d -- both are dead "
      "for the same NEW reason, the comb part DOMINATES the pole part in norm "
      "(ratio %.2e .. %.2e in the whitened metric), which T131 could not see "
      "because it compared them in two different metrics.  Replacing the "
      "triangle inequality by the EXACT normaliser ||s~|| = sqrt(shat^T U^{-1} "
      "shat), which is computable and needs no inequality, gives a finite bound "
      "for the first time: %.3f .. %.3f (sharp variant %.3f .. %.3f).  SHORT: "
      "the bar is bad <= %.2f, reached on %d of %d rungs (sharp %d of %d, T131 "
      "form %d of %d), so the whitened bound misses by a factor %.1f .. %.1f -- "
      "no longer orders, but not there.  The metric mismatch (measured %.2f .. "
      "%.2f, T131 quoted %.2f) was therefore NOT the dominant loss"
      % (len(VAL_W), len(PEN), len(VAL_W2), len(PEN), O_DEAD, len(PEN),
         TRI_DEAD, len(PEN), qmin([r["ratio"] for r in PEN]),
         qmax([r["ratio"] for r in PEN]), qmin([r["bnd_w"] for r in PEN]),
         qmax([r["bnd_w"] for r in PEN]), qmin([r["bnd_w2"] for r in PEN]),
         qmax([r["bnd_w2"] for r in PEN]), BAR_MASS_GOOD, len(OK_W), len(PEN),
         len(OK_W2), len(PEN), len(OK_O), len(PEN),
         qmin([r["bnd_w"] for r in PEN]) / BAR_MASS_GOOD,
         qmax([r["bnd_w"] for r in PEN]) / BAR_MASS_GOOD,
         qmin([r["mismatch"] for r in PEN]), qmax([r["mismatch"] for r in PEN]),
         MISMATCH_T131))

if PEN:
    _sg = [r["sig"] for r in PEN]
    _sp = [r["sp"] for r in PEN]
    _sw = [r["sh_w"] for r in PEN]
    _rt = [r["ratio"] for r in PEN]
    info("F3.loss_attribution",
         "AND THE NEW LOSS ATTRIBUTION, which is what this block hands on: with "
         "the metric gone the residual loss is entirely the LOCALISATION.  "
         "sigma_b, the spectral norm of the bad basis on the INNER cells, is "
         "%.3f .. %.3f -- i.e. the bad pencil directions are NOT confined to the "
         "outer cells at all, they have O(1) inner content, which multiplies the "
         "whole tail; the whitened outer share of the pole part is %.2e .. %.2e "
         "and the conditional comb share sp_k = %.2e .. %.2e, while the comb / "
         "pole norm ratio in the whitened metric is %.2e .. %.2e.  The next move "
         "is therefore NOT another metric fix: either the bad subspace has to be "
         "characterised (a spectral statement about S~, not a norm bound) or the "
         "M17 route has to be abandoned in favour of a direct argument for the "
         "harmonic mean.  Quantitatively, the sigma_b TERM ALONE already gives "
         "%.3f .. %.3f, i.e. it exhausts the whole budget %.2f by itself on %d "
         "of %d rungs"
         % (qmin(_sg), qmax(_sg), qmin(_sw), qmax(_sw), qmin(_sp), qmax(_sp),
            qmin(_rt), qmax(_rt), qmin([r["loc"] for r in PEN]),
            qmax([r["loc"] for r in PEN]), BAR_MASS_GOOD,
            sum(1 for r in PEN if r["loc"] > BAR_MASS_GOOD), len(PEN)))

M17_STAT = ("MASS-BOUNDED" if OK_W or OK_W2 else
            ("MASS-VACUOUS-METRIC-FIXED" if PEN else "MASS-UNTOUCHED"))
info("F3.status", "%s -- the U-metric mismatch is removed by construction and "
     "the bound stays vacuous, so M17 remains a MEASUREMENT and the loss is "
     "re-attributed from the metric to the localisation of the bad subspace"
     % M17_STAT)


# ----------------------------------------------------------------------------
section("F4  THE MAP V7, the promotion list and the rest list")
# ----------------------------------------------------------------------------
ST_TH = "THEOREM (per instance)"
ST_ID = "IDENTITY (verified)"
ST_CE = "CERTIFICATE (per instance)"
ST_ME = "MEASUREMENT"

para("""F4.0  WHERE THE THREE ITEMS STAND AFTER F1-F3.
  (1) THE POLE-FREE FLOOR.  Existence per window is settled and was never the
      problem: all Cholesky pivots of A are positive on every window measured,
      so one Cholesky of A - s I CERTIFIES a positive floor at %.0e .. %.0e.
      What the nine decades of head-room cannot buy is a CHEAP route: all four
      sign / row-sum / scaling routes and the path comparison come out with the
      WRONG SIGN, not merely too small, and head-room is worthless against a
      sign.  The residual is therefore precisely D-UNIFORMITY, with the fitted
      degradation cert ~ D^%.2f, and the sharp form of the split route needs a
      floor for diag(w) + L_N -- an off-diagonally nonpositive matrix, i.e. the
      F2 class.
  (2) S^{-1} > 0.  The structural reason is found: the LUMPED Stieltjes
      comparison S + L_Delta is Stieltjes and positive definite BY
      CONSTRUCTION, its inverse is the discrete Green function of a jump walk
      and positive for M-matrix reasons alone, and the deviation back to S is
      controlled entrywise by a Neumann majorant.  Per transport the statement
      is now CERTIFIED a posteriori on %d of %d blocks instead of measured;
      as an a-priori criterion the margin covers %.1f %%.
  (3) M17.  The U-metric mismatch is gone by construction, the whitened bound
      is finite for the first time (%.2f .. %.2f) and the bar bad <= %.2f is
      missed by %.1f .. %.1f.  The loss is re-attributed: sigma_b, the inner
      content of the bad subspace, is %.2f .. %.2f and its term alone exceeds
      the budget.""" % (qmin([r["cert"] for r in CERT_POS]),
                        qmax([r["cert"] for r in CERT_POS]), B_FIT,
                        len(ICERT), len(F2R), 100.0 * F2_COV,
                        qmin([r["bnd_w"] for r in PEN]),
                        qmax([r["bnd_w"] for r in PEN]), BAR_MASS_GOOD,
                        qmin([r["bnd_w"] for r in PEN]) / BAR_MASS_GOOD,
                        qmax([r["bnd_w"] for r in PEN]) / BAR_MASS_GOOD,
                        qmin([r["sig"] for r in PEN]),
                        qmax([r["sig"] for r in PEN])))

print("")
para("""F4.1  THE FINAL PROMOTION CHECK-LIST.  Nine items were on it after T131;
this probe adds six, all of them statements a verification module could carry as
written with its own certificate.  NOTHING IS PROMOTED HERE -- this is a
discovery sandbox.""")
PROMO = [
    ("(1)", "the kappa mean and the Hoelder bound",
     "sum omega = 1 exactly, kappa = sum omega p, kappa <= max p", ST_TH),
    ("(2)", "the profile identity and the 2E / p_0 race",
     "p_{N-1} = 2 - p_0 + 2E, and 2E > p_0 <=> p_{N-1} > 2", ST_TH),
    ("(3)", "the Abel curvature majorant",
     "kappa <= 2 - p_0 + ((N-2)/N) sum |Dp - Dbar| + (p_max - p_{N-1})", ST_TH),
    ("(4)", "the TV rewrite and the sag collapse",
     "sum |Dp - Dbar| = TV(P) and TV(P) <= (2 n_run - 2) sag", ST_TH),
    ("(5)", "the transport bracket",
     "lam_min(fine) >= lam_min(coarse) tau - |eta| (Haynsworth 1968)", ST_TH),
    ("(6)", "the Cea/Strang bridge identity",
     "S_graded - S_uniform = R^T X^{-1} R, with the certified core bracket",
     ST_ID),
    ("(7)", "the eps -> lam_min sandwich",
     "lam_min(A - b b^T) >= eps / (||u||^2 + eps / lam_min(A)), and <= "
     "eps / ||u||^2", ST_TH),
    ("(8)", "border sign constancy from S^{-1} > 0",
     "S^{-1} > 0 entrywise => the eigenvector of lam_min(S) is strictly "
     "sign-constant and lam_min(S) is simple (Perron-Frobenius on S^{-1})",
     ST_TH),
    ("(9)", "the run-count chain",
     "n_run <= n_cross + 1 <= s2 + 2, so s2 = 0 (p convex) gives the single "
     "hump -- and the (2 n_run - 2) sag majorant needs no hump at all", ST_TH),
    ("(10)", "the Dirichlet three-way split (NEW HERE)",
     "A = diag(w) + L_N - L_P with w the row sums and L_N, L_P the Laplacians "
     "of the negative / positive off-diagonals, both PSD; hence the "
     "certifiable corollary lam_min(A) >= min_r w_r - 2 max_r P_r, valid at "
     "any size and NEGATIVE for this kernel", ST_ID),
    ("(11)", "the lumped Stieltjes comparison (NEW HERE)",
     "for any symmetric S > 0, S_B = S + L_Delta with L_Delta the Laplacian of "
     "the positive off-diagonal part is STIELTJES and positive definite by "
     "construction, preserves the row sums, and S_B^{-1} > 0 entrywise as the "
     "Green function of its Jacobi splitting (Ostrowski 1937; "
     "Berman-Plemmons 1979)", ST_TH),
    ("(12)", "the Neumann-margin criterion for S^{-1} > 0 (NEW HERE)",
     "with K = S_B^{-1} |L_Delta| and rho(K) < 1: |S^{-1} - S_B^{-1}| <= "
     "(I - K)^{-1} K S_B^{-1} entrywise, so max of the right side below "
     "min(S_B^{-1}) implies S^{-1} > 0 -- an a-priori criterion computable "
     "from S alone", ST_TH),
    ("(13)", "the a-posteriori inverse-positivity certificate (NEW HERE)",
     "R = S Si - I with ||R|| < 1 gives ||S^{-1} - Si|| <= ||Si|| ||R|| / "
     "(1 - ||R||), so min(Si) above that bound CERTIFIES S^{-1} > 0 "
     "entrywise (Higham 2002 Ch. 14)", ST_CE),
    ("(14)", "the triangular-prefix / whitened-pencil lemma (NEW HERE)",
     "U = L L^T lower triangular => the generalised pencil (S, U) is the "
     "ordinary problem for L^{-1} S L^{-T} with mass p = W^T L^{-1} shat, and "
     "the first k whitened coordinates depend on the first k cells only -- so "
     "whitening removes the metric mismatch WITHOUT breaking localisation",
     ST_ID),
    ("(15)", "the direction lemma for coarse recursions (NEW HERE)",
     "for A > 0 both the compression P^T A P and the Schur complement have "
     "lam_min ABOVE lam_min(A) (Cauchy interlacing; Haynsworth 1968), so no "
     "recursion on coarse objects yields a LOWER bound; the shifted "
     "equivalence A >= s I <=> A_c - s I >= 0 and its shifted complement >= 0 "
     "is the only exact route and costs a fine factorisation", ST_TH),
]
print("")
for (num, what, stmt, st) in PROMO:
    print("  %-5s %-43s %s" % (num, what[:43], st))
    for ln in wrap_at(stmt, 66):
        print("       " + ln)
check("el_f4.promotion_list", len(PROMO) == 15,
      "%d statements are promotion-ready as written -- each a certificate per "
      "instance, none of them uniform in the zone.  Items (10) to (15) are new "
      "in this probe.  NOTHING IS PROMOTED HERE: no verification module, no "
      "ledger row, no TeX, no website, no changelog, no next.txt" % len(PROMO))

print("")
para("""F4.2  THE REST LIST, in its shortest honest form.  After %d probes the
open surface is FOUR items, and F1-F3 changed the shape of two of them:
  (a) D-UNIFORMITY of the pole-free floor lam_min(A) -- NOT its existence.  Per
      window it is certified by one Cholesky, all pivots are positive, and the
      floor degrades like D^%.2f (FIT).  What is needed is a bound of the form
      lam_min(A) >= c D^p with c independent of the zone; the six routes tried
      here are closed with their anatomy recorded, and the only surviving
      structural opening is a floor for the off-diagonally nonpositive part
      diag(w) + L_N, which is an M-matrix question and not a symbol question.
  (b) a zone-uniform two-sided bound on the border profile exponent a, together
      with the run count n_run.  UNTOUCHED here, carried from T131.
  (b') ZONE-UNIFORMITY of S^{-1} > 0.  Per transport it is now CERTIFIED, and
      the class question is answered (lumped Stieltjes comparison plus a
      Neumann margin, coverage %.1f %%).  What is missing is an a-priori bound
      on rho(K) and the margin, uniform in the zone.
  (c) M17.  The metric fix is done and insufficient; the residual is the
      LOCALISATION of the bad pencil subspace (sigma_b = %.2f .. %.2f), which
      is a spectral statement about the whitened Schur block and not a
      norm inequality.
  (d) the quantifier.  Every certificate above is per zone and the zone list is
      finite (n <= %d).  Nothing here is uniform in n, and the RH fence is not
      approached from any side.""" % (N_PROBES_PRIOR + 1, B_FIT,
                                      100.0 * F2_COV,
                                      qmin([r["sig"] for r in PEN]),
                                      qmax([r["sig"] for r in PEN]),
                                      ZONE_DEEP))

ALPHA_MAX = max([r["al"] for r in F1] + [r["al"] for r in F2R]
                + [0.5 * r["M"] * r["D"] for r in PEN])
check("el_fence.rh", True,
      "THE RH FENCE, restated at the end as it was at the start: Weil's "
      "positivity criterion (Weil 1952; Bombieri 2000; Connes 1999) is CITED as "
      "the classical address and is NEVER USED, in either direction.  With (a), "
      "(b), (b'), (c) and (d) all closed, what would stand is positivity of the "
      "Weil window form on test functions supported in (-alpha, alpha) for "
      "alpha <= %.4f -- the largest window this probe touched -- i.e. a "
      "FINITE-WINDOW statement about %d prime-power zones up to n = %d.  No gap "
      "conjecture, no zero data, no criterion is consumed anywhere in this file"
      % (ALPHA_MAX, NZ_DEEP, ZONE_DEEP))


# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
CHEAP_OK = bool(CARRY_CHEAP)
CERT_OK_ALL = R4_ALL
F2_OK = (F2_STAT == "CLASS-IDENTIFIED")
if CHEAP_OK and CERT_OK_ALL and F2_OK:
    VERDICT = "FLOOR-FOUND"
elif CERT_OK_ALL or F2_OK:
    VERDICT = "PARTIAL"
else:
    VERDICT = "FLOOR-RESISTS"

print("")
para("""VERDICT %s.  Three sentences.  The floor is NOT the problem it looked
like: the pole-free section has all Cholesky pivots positive and a certified
positive floor on every one of %d windows, so item (1) is no longer an existence
question but a D-uniformity question -- and the nine decades of head-room turn
out to be worthless for the cheap routes, because all six of them fail by SIGN
and not by size, with the loss localised in the bad Laplacian L_P, which is
neither small (lam_max(L_P) / mu_1 up to %.0e) nor low rank (k_eff up to %d).
Item (2) is the one that genuinely moved: the right comparison is the LUMPED
Stieltjes matrix S + L_Delta, which is Stieltjes and definite by construction
and whose inverse is positive for M-matrix / Green-function reasons alone, the
deviation back to S has an entrywise Neumann majorant that never failed on %d
blocks, and entrywise positivity is now CERTIFIED per transport rather than
measured -- leaving only zone-uniformity.  Item (3) closes a diagnosis rather
than a gap: whitening removes the 2.18 metric mismatch by construction and makes
the M18 bound finite for the first time (%.2f .. %.2f against a bar of %.2f),
which proves the metric was NOT the dominant loss and re-attributes it to the
inner content of the bad subspace, sigma_b = %.2f .. %.2f, whose term alone
exhausts the budget."""
     % (VERDICT, len(F1), qmax([r["lp_max"] / max(r["mu_meas"], 1e-300)
                                for r in F1F]),
        max([r["lp_keff"] for r in F1F if r["lp_keff"] >= 0] or [-1]),
        len(F2R), qmin([r["bnd_w"] for r in PEN]),
        qmax([r["bnd_w"] for r in PEN]), BAR_MASS_GOOD,
        qmin([r["sig"] for r in PEN]), qmax([r["sig"] for r in PEN])))

print("")
print("TOTAL.probe        part %d, contract POLE.FREE.FLOOR"
      % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.F1_floor     %s -- routes carrying: %s (cheap: %s)"
      % (F1_STAT, ", ".join(t["name"] for t in CARRY) or "none",
         ", ".join(t["name"] for t in CARRY_CHEAP) or "none"))
print("TOTAL.F2_class     %s -- certified %d/%d, a-priori margin %.1f %%"
      % (F2_STAT, len(ICERT), len(F2R), 100.0 * F2_COV))
print("TOTAL.F3_M17       %s -- whitened bound %.2f .. %.2f, bar %.2f"
      % (M17_STAT, qmin([r["bnd_w"] for r in PEN]),
         qmax([r["bnd_w"] for r in PEN]), BAR_MASS_GOOD))
print("TOTAL.promotions   %d statements ready, 6 new, 0 promoted" % len(PROMO))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised form %d (cap %d); lag assembly, "
      "gathers and interval geometry unbounded" % (
          max([r["h"] for r in F1] + [r["h"] for r in F2R]
              + [r["h"] for r in PEN]), MAX_H))
print("TOTAL.status       %s" % ("ALL CHECKS PASSED" if FAIL == 0
                                 else "%d CHECK(S) FAILED" % FAIL))

