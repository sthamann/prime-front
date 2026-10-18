"""Discovery probe (2026-07-28), part 133.  Contract CERT.FLOOR -- CERTIFY the
seam's reflection-positivity PSD statements instead of MEASURING them.  Nothing
else: this probe reads the verification suite, reproduces its RP/Hankel matrices
and issues certificates.  It changes NO ledger row, NO paper, NO website; every
status move below is a RECOMMENDATION printed as output.

WHY (the methodology transfer from the prime-front series)
  The ledger gate SEAM.S3.RP.01 carries reflection positivity with the wording
  "the Hankel/reflection Gram matrix ... is positive semidefinite (min eigenvalue
  >= 0 to numerical tolerance)".  T130 of the prime front hit exactly this shape
  and named it: Lanczos / eigenvalue computations bound lam_min from ABOVE -- they
  are a MEASUREMENT, never a certificate.  A symmetric eigensolver returns a
  number whose own error is of the order of u*||A||; "min eigenvalue >= -1e-10"
  therefore does not separate a PSD matrix from an indefinite one whose most
  negative eigenvalue sits anywhere in the blind band (-1e-10, 0).  E1.5 below
  EXHIBITS such a matrix: certified indefinite, and it PASSES the module's test.
  The replacement is the classical one: a COMPLETED Cholesky factorisation is a
  certificate, with a declared floating-point bar.

THE CERTIFICATE (declared BEFORE any number is computed; cited, not re-derived)
  [W]  Wilkinson, "A priori error analysis of algebraic processes" (1968) -- a
       floating-point Cholesky factorisation that RUNS TO COMPLETION exhibits a
       nearby positive semidefinite matrix.
  [H]  Higham, "Accuracy and Stability of Numerical Algorithms", 2nd ed. (2002),
       Thm 10.3/10.4 (+ Sec. 10.1): the computed factor Rhat of a symmetric A
       satisfies EXACTLY  Rhat^T Rhat = A + dA  with  |dA| <= gam_{n+1} |Rhat^T||Rhat|,
       gam_k = k u / (1 - k u).
  [R]  Rump, "Verification of positive definiteness", BIT 46 (2006) 433-452 --
       the shifted form used here: if fp-Cholesky of A - t I completes, then
       lam_min(A) >= t - (backward-error bar), a LOWER bound.
  Since Rhat^T Rhat >= 0 holds exactly, [H] gives lam_min(A) >= -||dA||_2, i.e. a
  lower bound on lam_min -- the direction an eigensolver cannot supply.

  DECLARED BARS (fixed here; no number below was used to tune them)
    u             = 2^-53 (binary64), resp. mpmath eps/2 at the declared dps
    gam_k(u)      = k u / (1 - k u)
    c_h(n)        = n (n+1) / (1 - (n+1) u)              [normwise reading of [H]:
                    ||dA||_2 <= n gam_{n+1} ||A||_2 = c_h(n) u ||A||_2]
    ||A||_2       <= ||A||_inf  (A symmetric), fp-guarded by (1 + gam_{n+1})
    SAFETY        = 8            (declared slack for the normwise reading)
    eta_chol(A)   = SAFETY * c_h(n) * u * ||A||_2^up     THE FLOATING-POINT BAR
    kappa_ceil(n) = 1 / (SAFETY * c_h(n) * u)            the cond form of the bar:
                    a POSITIVE floor is certifiable only while cond(A) < kappa_ceil
                    (this is the "c_h u cond ||A||" reading -- the bar in relative
                    units; cond itself is only ever REPORTED, and reported as a
                    MEASUREMENT, never used inside a certificate)
    eta_entry(A)  = SAFETY * n * gam_{K+2}(u) * max|A_ij|
                    the bar on the ENTRIES: the matrix the module tests is the
                    fp evaluation Ahat of a transcendental kernel (K summands),
                    so no certificate about Ahat says anything about the
                    mathematical A below eta_entry.  Honest accounting adds it.
    eta_total     = eta_chol + eta_entry
    certified floor(A) = t* - eta_chol,  t* = largest shift whose fp-Cholesky of
                    A - t I completes (geometric bisection)
    HEADROOM      = certified floor / eta_total
  A SECOND, LATTE-FREE ROUTE is admitted and reported separately:
    STRUCTURAL/EXACT: an explicit factorisation A = B^T D B with D >= 0 that
    holds in EXACT arithmetic (symbolic or rational).  It certifies ">= 0" with
    NO floating-point bar, but it cannot give a positive floor when A is
    genuinely singular.  This is the route v171 already uses (Vandermonde Gram)
    and the route v379 could use but does not.
  SEMIDEFINITE BOOKKEEPING (asked for explicitly): when a positive floor is not
    available, the probe computes the SMALLEST t whose fp-Cholesky of A + t I
    completes and reports the certified statement as "A >= -(t + eta_chol)" --
    i.e. it states honestly whether ">= 0" or only ">= -t" is certifiable.

PREREGISTERED VERDICTS (bars fixed here)
  Per tested LEDGER ROW two independent columns, because the two questions differ:
    CLAIM   -- is the mathematical statement ("the RP Gram is PSD") certifiable at
               all, by ANY of the two routes?
    WORDING -- is the statement AS THE LEDGER/MODULE WORDS IT ("PSD, min
               eigenvalue >= 0 to numerical tolerance", i.e. the eigenvalue route
               in binary64) certified?
  Per-matrix labels (from HEADROOM of the fp route, or the exact route):
    [CERT-UP]          Cholesky-certified with HEADROOM >= 10, or exact/structural
                       certificate (headroom = inf, no fp bar)
    [MARGINAL]         HEADROOM in [1, 10)
    [MEASUREMENT-ONLY] HEADROOM < 1 -- the floor sits under the fp bar, so the
                       assertion is a measurement; the row then claims more than
                       is certifiable and a downgrade recommendation is FORMULATED
                       (never executed).
  Global verdict:
    ALL-CERT          every tested RP statement certified in BOTH columns
    MIXED             every CLAIM certified, but >= 1 WORDING is measurement-only
                      (=> wording/method repair recommended, no marker move)
    DOWNGRADE-NEEDED  >= 1 CLAIM not certifiable by either route (=> [E] -> [N]
                      recommendation, named)

WHAT IS REPRODUCED (verification/ read-only; module parameters copied verbatim)
  ROW 1  SEAM.S3.RP.01  -- verification/v379_seam_s3_rp.py
         eps = |d(k)| of the p+ip band, M = 1, N = 40 grid (1600 modes);
         G(tau) = mean_k e^{-eps_k tau};  Hankel M_ij = G(tau_i + tau_j),
         taus = linspace(0.2, 2.0, 10); module test: min eigenvalue > -1e-10;
         plus the module's ghost/neg control G(tau) - 2 e^{0.1 tau}.
         Extra windows/sizes (the module has one; the sweep is ours, declared as
         ours): n in {4,6,8,10,14,20,30,40,60} and three tau windows.
  ROW 2  QFT.OSMOMENT.01 -- verification/v171_os_moment_cluster.py
         atoms {1, (2/3)^6, (1/3)^6} = {1, 64/729, 1/729}, weights (1,1,1),
         Hankel H_ij = C(i+j), N = 5 (module) and N in {3,4,5,8,12} (ours),
         exact rational arithmetic.
  ROW 3  SEAM.CLOCK.SILVER.01 -- verification/v527_seam_clock_silver_spectrum.py
         (A1.1 half-circle Gram) and, per the entrywise reduction certified
         there, the SAME object as WOIT.THETA.FREE.01 / v519 R3.1 (the 8x8
         one-particle bond-cut Gram at N = 16):
         G_ab = C(a + b - (N-1)), a,b in [N/2, N), C(d) = (2/N)/sin(pi d/N) for
         odd d and 0 for even d; N in {8,16,24,32}; module test: min eigenvalue
         > 1e-30 at 40 digits.
  NOT REPRODUCED (flagged, excluded from the verdict): WOIT.BETA2.OS.01 / v524
         (the 37x37 and 16x16 OS Grams) -- their construction needs the module's
         theta/Wick machinery, out of scope for one probe file; the wording
         critique applies verbatim and is carried as a follow-up item.

FINDINGS OF THIS RUN (2026-07-28, 23/23 checks, 1.3 s) -- VERDICT MIXED
  * SEAM.S3.RP.01 (v379): CLAIM certified, WORDING [MEASUREMENT-ONLY].  The fp
    Cholesky of the module's own 10x10 Hankel does NOT complete; the smallest
    completed up-shift only certifies "M >= -2.0e-13"; cond ~ 1.8e18 sits over
    the certifiability ceiling 1.0e13; eta_entry = 7.6e-12 dominates any floor
    the fp route could give.  Sharper than the bar argument: the matrix the
    module builds and tests is, as a matrix of doubles, CERTIFIABLY NOT PSD (a
    certified negative direction, x^T Mhat x = -7.75e-18 at 60 digits, for the
    module's own n = 10 and for n = 14, 20) -- and the module's tolerance passes
    it.  The mathematical Hankel is fine: certified floor 2.66e-25 at 40 digits,
    while rounding the entries to doubles moves the matrix by 3.5e-17, eight
    orders more; the indefiniteness is a pure rounding artifact and binary64
    cannot decide the statement in either direction.  The repair is exact, not
    weaker: M = V^T diag(1/1600) V is a positive-mixture Gram, so M >= 0 in
    exact arithmetic with no bar (symbolically certified).  Only n = 4 certifies
    in binary64 (headroom 8.4e4); 16 of 17 size/window variants are
    MEASUREMENT-ONLY.  Certifying a positive FLOOR instead costs 25/40/70/70
    declared digits at n = 6/10/14/20.  Bonus: the row's gap claim and its ghost
    neg-control are both fully certifiable (gap at 50 digits; a negative
    DIRECTION is a certificate where a negative eigenvalue readout is not).
  * QFT.OSMOMENT.01 (v171): CLAIM and WORDING certified.  H = W diag(1,1,1) W^T
    over Q with a nonzero Vandermonde minor at N = 3,4,5,8,12 -- ">= 0" exactly,
    no bar.  For N > 3 the Gram is exactly rank 3, so lam_min = 0 EXACTLY and no
    positive floor exists; the module's redundant numeric psd side-check
    (eigenvals >= -1e-12) supports nothing.
  * SEAM.CLOCK.SILVER.01 (v527 A1.1) = WOIT.THETA.FREE.01 (v519 R3.1): CLAIM and
    WORDING certified.  Shifted-Cholesky floors 1.3e-1 / 1.9e-3 / 2.2e-5 /
    2.4e-7 at N = 8/16/24/32 with binary64 headroom 4.3e12 ... 6.4e5, and
    headroom >= 7e30 at the 40 digits those modules already run.
  * RECOMMENDATION: no marker moves.  Method/wording repair for SEAM.S3.RP.01
    (exact Gram certificate instead of eigvalsh; drop "to numerical tolerance"),
    certified-floor wording for v527/v519, relabel the v171 side-check, and a
    follow-up certificate for the v524 Grams.  Nothing executed here.

HARD CAPS (declared): largest FACTORISED / DIAGONALISED matrix <= 1500 (the
  largest used here is far below); probe budget < 600 s.
FENCES: sandbox only; verification/ read-only; NO ledger / paper / website /
  changelog / next.txt edit; certified and measured never mixed in one sentence;
  every measurement carries the word MEASUREMENT.

OUTCOME OF THIS RUN => see the E4 table and TOTAL.verdict printed below.
"""
import time

import mpmath as mp
import numpy as np
import sympy as sp

T_START = time.time()
BUDGET_S = 600.0
CAP_FACTOR_N = 1500
N_PROBES_PRIOR = 132
PASS = 0
FAIL = 0
MAX_N_SEEN = 0

# ---------------------------------------------------------------------------
# declared bars (preregistration -- see the module docstring)
# ---------------------------------------------------------------------------
U_D = 2.0 ** -53
SAFETY = 8.0
BAR_CERT = 10.0          # headroom >= 10  => CERT-UP
BAR_MARGINAL = 1.0       # headroom >= 1   => MARGINAL
DPS_LADDER = (25, 40, 70, 120, 200)
MODULE_TOL_V379 = -1e-10   # the tolerance v379 actually uses
MODULE_TOL_V527 = 1e-30    # the 40-digit tolerance v527 actually uses


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-44s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-44s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def note(txt):
    for line in txt.strip("\n").split("\n"):
        print("       " + line.strip())


# ---------------------------------------------------------------------------
# the certificate machinery (binary64)
# ---------------------------------------------------------------------------
def gam(k, u):
    return k * u / (1.0 - k * u)


def c_h(n, u):
    """declared normwise Wilkinson/Higham constant, [H] Thm 10.3/10.4:
    ||dA||_2 <= n * gam_{n+1} * ||A||_2 = c_h(n) * u * ||A||_2."""
    return n * (n + 1) / (1.0 - (n + 1) * u)


def norm2_upper(A):
    """rigorous upper bound on ||A||_2 for symmetric A: ||A||_2 <= ||A||_inf."""
    n = A.shape[0]
    s = float(np.max(np.sum(np.abs(A), axis=1)))
    return s * (1.0 + gam(n + 1, U_D))


def eta_chol(A):
    n = A.shape[0]
    return SAFETY * c_h(n, U_D) * U_D * norm2_upper(A)


def kappa_ceil(n, u=U_D):
    return 1.0 / (SAFETY * c_h(n, u) * u)


def eta_entry(A, k_ops):
    """bar on the ENTRIES: fp evaluation of a kernel with k_ops summands/ops."""
    n = A.shape[0]
    return SAFETY * n * gam(k_ops + 2, U_D) * float(np.max(np.abs(A)))


def chol_ok(A):
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False
    except ValueError:
        return False


def certified_floor(A, coarse=256.0, refine=14):
    """largest shift t with completed fp-Cholesky of A - t I  =>  certified
    lam_min(A) >= t - eta_chol.  Geometric bisection; no eigenvalue is used."""
    global MAX_N_SEEN
    n = A.shape[0]
    MAX_N_SEEN = max(MAX_N_SEEN, n)
    assert n <= CAP_FACTOR_N
    eta = eta_chol(A)
    ident = np.eye(n)
    if not chol_ok(A):
        # no completed factorisation => NO floor is certified at all
        return dict(chol0=False, certified=False, t_star=0.0,
                    floor=float("-inf"), eta=eta)
    hi = norm2_upper(A)
    t = hi
    lo = None
    for _ in range(400):
        if chol_ok(A - t * ident):
            lo = t
            break
        hi = t
        t = t / coarse
        if t < 1e-300:
            break
    if lo is None:
        lo, hi = 0.0, hi
    for _ in range(refine):
        mid = np.sqrt(max(lo, 1e-300) * hi) if lo > 0 else 0.5 * hi
        if chol_ok(A - mid * ident):
            lo = mid
        else:
            hi = mid
    return dict(chol0=True, certified=True, t_star=lo, floor=lo - eta, eta=eta)


def certified_upshift(A, coarse=256.0, refine=14):
    """smallest t with completed fp-Cholesky of A + t I  =>  certified statement
    A >= -(t + eta_chol) only (the honest semidefinite bookkeeping)."""
    n = A.shape[0]
    eta = eta_chol(A)
    ident = np.eye(n)
    if chol_ok(A):
        return dict(t=0.0, eta=eta, ge_zero_route=True)
    t = eta if eta > 0 else 1e-300
    hi = None
    for _ in range(400):
        if chol_ok(A + t * ident):
            hi = t
            break
        t = t * coarse
        if t > 1e300:
            break
    if hi is None:
        return dict(t=float("inf"), eta=eta, ge_zero_route=False)
    lo = hi / coarse
    for _ in range(refine):
        mid = np.sqrt(max(lo, 1e-300) * hi)
        if chol_ok(A + mid * ident):
            hi = mid
        else:
            lo = mid
    return dict(t=hi, eta=eta, ge_zero_route=False)


def certified_negative_direction(A, x):
    """certificate that A is NOT PSD: a vector with x^T A x < 0 beyond the fp bar
    of the quadratic-form evaluation itself."""
    n = A.shape[0]
    q = float(x @ (A @ x))
    bnd = SAFETY * gam(n + 1, U_D) * float(np.abs(x) @ (np.abs(A) @ np.abs(x)))
    return dict(fires=(q + bnd < 0.0), q=q, bnd=bnd)


# ---------------------------------------------------------------------------
# the certificate machinery (mpmath, declared precision)
# ---------------------------------------------------------------------------
def mp_u():
    return mp.eps / 2


def mp_norm2_upper(A):
    n = A.rows
    s = max(sum(abs(A[i, j]) for j in range(n)) for i in range(n))
    return s * (1 + mp.mpf(n + 1) * mp_u())


def mp_eta_chol(A):
    n = A.rows
    u = mp_u()
    return SAFETY * (n * (n + 1) / (1 - (n + 1) * u)) * u * mp_norm2_upper(A)


def mp_chol_ok(A):
    try:
        mp.cholesky(A)
        return True
    except ValueError:
        return False
    except ZeroDivisionError:
        return False


def mp_shifted(A, t):
    n = A.rows
    B = mp.matrix(A)
    for i in range(n):
        B[i, i] = B[i, i] - t
    return B


def mp_certified_floor(A, coarse=256, refine=12):
    global MAX_N_SEEN
    n = A.rows
    MAX_N_SEEN = max(MAX_N_SEEN, n)
    assert n <= CAP_FACTOR_N
    eta = mp_eta_chol(A)
    if not mp_chol_ok(A):
        return dict(chol0=False, certified=False, t_star=mp.mpf(0),
                    floor=-mp.inf, eta=eta)
    hi = mp_norm2_upper(A)
    t = hi
    lo = None
    for _ in range(600):
        if mp_chol_ok(mp_shifted(A, t)):
            lo = t
            break
        hi = t
        t = t / coarse
        if t < mp.mpf(10) ** (-mp.mp.dps - 40):
            break
    if lo is None:
        return dict(chol0=True, certified=True, t_star=mp.mpf(0), floor=-eta,
                    eta=eta)
    for _ in range(refine):
        mid = mp.sqrt(lo * hi)
        if mp_chol_ok(mp_shifted(A, mid)):
            lo = mid
        else:
            hi = mid
    return dict(chol0=True, certified=True, t_star=lo, floor=lo - eta, eta=eta)


# ---------------------------------------------------------------------------
# ROW 1 -- v379 objects (parameters copied verbatim from the module)
# ---------------------------------------------------------------------------
V379_N_GRID = 40
V379_M = 1.0
V379_TAUS = (0.2, 2.0, 10)


def v379_band_energies(M=V379_M, N=V379_N_GRID):
    """verbatim reproduction of v379._band_energies."""
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    d = [np.sqrt(np.sin(kx) ** 2 + np.sin(ky) ** 2
                 + (M - np.cos(kx) - np.cos(ky)) ** 2)
         for kx in ks for ky in ks]
    return np.array(d)


def v379_G(tau, eps):
    """verbatim reproduction of v379._G."""
    return np.mean(np.exp(-np.outer(tau, eps)), axis=1)


def v379_hankel(taus, eps):
    return np.array([[float(v379_G(np.array([ti + tj]), eps)[0]) for tj in taus]
                     for ti in taus])


def v379_hankel_ghost(taus, eps):
    def g(tau):
        return v379_G(tau, eps) - 2.0 * np.exp(0.1 * tau)
    return np.array([[float(g(np.array([ti + tj]))[0]) for tj in taus]
                     for ti in taus])


def band_orbits(N=V379_N_GRID):
    """(a,b,multiplicity) orbit reduction of the band multiset under the grid
    symmetries j -> N-j and kx <-> ky, so the mp rebuild costs O(N^2/8) exps."""
    orb = {}
    for jx in range(N):
        for jy in range(N):
            a = min(jx, (N - jx) % N)
            b = min(jy, (N - jy) % N)
            key = (min(a, b), max(a, b))
            orb[key] = orb.get(key, 0) + 1
    return [(a, b, m) for (a, b), m in sorted(orb.items())]


def mp_band(N=V379_N_GRID, M=V379_M):
    """band energies at the working mp precision, on the reduced orbits."""
    out = []
    for a, b, m in band_orbits(N):
        kx = 2 * mp.pi * a / N
        ky = 2 * mp.pi * b / N
        e = mp.sqrt(mp.sin(kx) ** 2 + mp.sin(ky) ** 2
                    + (mp.mpf(M) - mp.cos(kx) - mp.cos(ky)) ** 2)
        out.append((e, m))
    return out


def mp_v379_hankel(n, t0=0.2, t1=2.0, N=V379_N_GRID):
    band = mp_band(N)
    tot = sum(m for _, m in band)
    taus = [mp.mpf(t0) + (mp.mpf(t1) - mp.mpf(t0)) * i / (n - 1)
            for i in range(n)]
    cache = {}

    def G(s):
        key = mp.nstr(s, 30)
        if key not in cache:
            cache[key] = sum(m * mp.e ** (-e * s) for e, m in band) / tot
        return cache[key]
    A = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = G(taus[i] + taus[j])
    return A


# ---------------------------------------------------------------------------
# ROW 3 -- v527 / v519 silver Hankel (parameters copied verbatim)
# ---------------------------------------------------------------------------
def silver_c(d, N):
    if d % 2 == 0:
        return 0.0
    return (2.0 / N) / np.sin(np.pi * d / N)


def silver_hankel(N):
    half = list(range(N // 2, N))
    n = len(half)
    A = np.zeros((n, n))
    for i, a in enumerate(half):
        for j, b in enumerate(half):
            A[i, j] = silver_c(a + b - (N - 1), N)
    return A


def mp_silver_hankel(N):
    half = list(range(N // 2, N))
    n = len(half)
    A = mp.matrix(n, n)
    for i, a in enumerate(half):
        for j, b in enumerate(half):
            d = a + b - (N - 1)
            A[i, j] = (mp.mpf(0) if d % 2 == 0
                       else (mp.mpf(2) / N) / mp.sin(mp.pi * d / N))
    return A


# ---------------------------------------------------------------------------
# verdict bookkeeping
# ---------------------------------------------------------------------------
ROWS = []


def label_from_headroom(h, exact=False):
    if exact:
        return "CERT-UP"
    if h >= BAR_CERT:
        return "CERT-UP"
    if h >= BAR_MARGINAL:
        return "MARGINAL"
    return "MEASUREMENT-ONLY"


MATRICES = []      # per-matrix certificate records


def record(row, tag, n, floor, eta_tot, kappa_meas, exact=False, extra=""):
    h = float("inf") if exact else (floor / eta_tot if eta_tot > 0 else 0.0)
    if not exact:
        h = max(h, 0.0)
    rec = dict(row=row, tag=tag, n=n, floor=floor, eta=eta_tot,
               kappa=kappa_meas, headroom=h, exact=exact,
               label=label_from_headroom(h, exact), extra=extra)
    MATRICES.append(rec)
    return rec


def fmt(x, k=3):
    if x == float("inf"):
        return "inf"
    if x == float("-inf"):
        return "no cert"
    return ("%." + str(k) + "e") % x


# ===========================================================================
section("E0  SETUP -- declared bars, machinery validation, module reproduction")
# ===========================================================================
info("bars", "u = %.3e, SAFETY = %.0f, CERT bar headroom >= %.0f"
     % (U_D, SAFETY, BAR_CERT))
for n_ in (5, 10, 40, 100):
    info("bar at n = %d" % n_,
         "c_h = %.3e, eta/||A|| = %.3e, cond ceiling kappa_ceil = %.3e"
         % (c_h(n_, U_D), SAFETY * c_h(n_, U_D) * U_D, kappa_ceil(n_)))

# --- E0.1 soundness of the certificate machinery -----------------------------
rng = np.random.default_rng(20260728)
viol = 0
n_tested = 0
sharp = []
for trial in range(240):
    n = int(rng.integers(3, 25))
    Q = np.linalg.qr(rng.standard_normal((n, n)))[0]
    scale = 10.0 ** rng.uniform(-8, 2)
    lam = np.sort(np.abs(rng.standard_normal(n))) * scale
    lam[0] = scale * 10.0 ** rng.uniform(-10, 0)
    if trial % 3 == 2:                       # a third of the controls indefinite
        lam[0] = -lam[0]
    A = Q @ np.diag(lam) @ Q.T
    A = 0.5 * (A + A.T)
    lam_true = float(np.linalg.eigvalsh(A).min())    # MEASUREMENT (reference)
    res = certified_floor(A)
    if not res["certified"]:
        continue                     # no factorisation => nothing was certified
    n_tested += 1
    # soundness: a certified floor may never exceed the true lam_min (allowing
    # the reference eigensolver its own error u*||A||)
    if res["floor"] > lam_true + 4.0 * U_D * norm2_upper(A):
        viol += 1
    if lam_true > 0 and res["floor"] > 0:
        sharp.append(lam_true / res["floor"])
check("E0.1 floor soundness (240 controls)", viol == 0,
      "violations %d / %d certifying controls; sharpness lam_true/floor median "
      "%.3f, max %.3f"
      % (viol, n_tested, float(np.median(sharp)), float(np.max(sharp))))

# --- E0.2 no false certification of positivity on indefinite controls --------
false_pos = 0
fires = 0
for trial in range(200):
    n = int(rng.integers(3, 20))
    Q = np.linalg.qr(rng.standard_normal((n, n)))[0]
    lam = np.abs(rng.standard_normal(n)) + 0.1
    lam[0] = -(10.0 ** rng.uniform(-14, -1))
    A = Q @ np.diag(lam) @ Q.T
    A = 0.5 * (A + A.T)
    res = certified_floor(A)
    if res["certified"] and res["floor"] > 0:
        false_pos += 1
    w, V = np.linalg.eigh(A)
    cert = certified_negative_direction(A, V[:, 0])
    if cert["fires"]:
        fires += 1
check("E0.2 no positive floor on indefinite controls", false_pos == 0,
      "false certifications %d / 200; negative-direction certificate fired on "
      "%d / 200 (fires only when |lam_min| clears its own fp bar)"
      % (false_pos, fires))

# --- E0.3 negative-direction certificate never fires on PD ------------------
false_fire = 0
for trial in range(200):
    n = int(rng.integers(3, 20))
    Q = np.linalg.qr(rng.standard_normal((n, n)))[0]
    lam = np.abs(rng.standard_normal(n)) + 1e-6
    A = Q @ np.diag(lam) @ Q.T
    A = 0.5 * (A + A.T)
    w, V = np.linalg.eigh(A)
    for col in (0, n - 1):
        if certified_negative_direction(A, V[:, col])["fires"]:
            false_fire += 1
check("E0.3 negative certificate soundness", false_fire == 0,
      "false fires %d / 400 directions on PD controls" % false_fire)

# --- E0.4 reproduction of v379 -----------------------------------------------
eps_d = v379_band_energies()
gap_d = float(eps_d.min())
taus_d = np.linspace(*V379_TAUS)
M379 = v379_hankel(taus_d, eps_d)
min_eig_379 = float(np.linalg.eigvalsh(M379).min())      # MEASUREMENT
M379g = v379_hankel_ghost(taus_d, eps_d)
min_eig_379g = float(np.linalg.eigvalsh(M379g).min())    # MEASUREMENT
mod_pass = (min_eig_379 > MODULE_TOL_V379)
mod_pass_g = (min_eig_379g < -1e-6)
check("E0.4 v379 reproduced verbatim", mod_pass and mod_pass_g and gap_d > 0.9,
      "gap = %.6f, Hankel 10x10 min eig (MEASUREMENT) = %.3e -> module check "
      "%s; ghost min eig = %.3e -> module check %s"
      % (gap_d, min_eig_379, mod_pass, min_eig_379g, mod_pass_g))

# --- E0.5 orbit reduction exact ---------------------------------------------
orb = band_orbits()
exp_mult = []
for a, b, m in orb:
    kx = 2 * np.pi * a / V379_N_GRID
    ky = 2 * np.pi * b / V379_N_GRID
    e = np.sqrt(np.sin(kx) ** 2 + np.sin(ky) ** 2
                + (V379_M - np.cos(kx) - np.cos(ky)) ** 2)
    exp_mult.extend([e] * m)
exp_mult = np.sort(np.array(exp_mult))
dev_orb = float(np.max(np.abs(exp_mult - np.sort(eps_d))))
check("E0.5 orbit reduction of the band multiset",
      len(exp_mult) == len(eps_d) and dev_orb < 1e-14,
      "%d orbits carry the full %d-mode multiset, max deviation %.2e"
      % (len(orb), len(eps_d), dev_orb))

# --- E0.6 reproduction of v527 / v519 ---------------------------------------
sil = {}
for N in (8, 16, 24, 32):
    A = silver_hankel(N)
    sil[N] = A
mp.mp.dps = 40
sil_mp_min = {}
for N in (8, 16):
    Amp = mp_silver_hankel(N)
    E, _ = mp.eighe(Amp)
    sil_mp_min[N] = min(E[i] for i in range(Amp.rows))     # MEASUREMENT
ok527 = all(sil_mp_min[N] > mp.mpf(MODULE_TOL_V527) for N in (8, 16))
check("E0.6 v527/v519 half-circle Hankel reproduced", ok527,
      "N=8 (4x4) min eig %s, N=16 (8x8) min eig %s at 40 digits "
      "(MEASUREMENT, module bar %.0e)"
      % (mp.nstr(sil_mp_min[8], 6), mp.nstr(sil_mp_min[16], 6),
         MODULE_TOL_V527))

# ===========================================================================
section("E1  ROW 1 -- SEAM.S3.RP.01 / v379: certify the RP Hankel")
# ===========================================================================
note("""
The module's assertion: "the Hankel/reflection Gram matrix M_ij = G(tau_i+tau_j)
is positive semidefinite (min eigenvalue >= 0 to numerical tolerance)".  Route 1
below is the fp Cholesky certificate on exactly that matrix; route 2 is the
latte-free structural certificate the object actually admits.
""")

# --- E1.1 the module matrix, fp route ---------------------------------------
eta_e_379 = eta_entry(M379, len(eps_d))
res379 = certified_floor(M379)
up379 = certified_upshift(M379)
eta_tot_379 = res379["eta"] + eta_e_379
kap379 = float(np.linalg.cond(M379))                     # MEASUREMENT
rec_mod = record("SEAM.S3.RP.01", "v379 Hankel n=10 (module params)", 10,
                 res379["floor"], eta_tot_379, kap379)
info("E1.1 module matrix, fp route",
     "chol(A) completes: %s; t* = %s; eta_chol = %s; eta_entry = %s; "
     "floor = %s; headroom = %s -> [%s]"
     % (res379["chol0"], fmt(res379["t_star"]), fmt(res379["eta"]),
        fmt(eta_e_379), fmt(res379["floor"]), fmt(rec_mod["headroom"], 2),
        rec_mod["label"]))
info("E1.1 semidefinite bookkeeping",
     "smallest completed up-shift t = %s => certified statement is "
     "'A >= -(t + eta_chol) = -%s'%s"
     % (fmt(up379["t"]), fmt(up379["t"] + res379["eta"]),
        "  ('>= 0' route available)" if up379["ge_zero_route"] else
        "  ('>= 0' NOT certifiable on this route)"))
info("E1.1 conditioning (MEASUREMENT)",
     "cond ~ %.3e vs certifiability ceiling kappa_ceil(10) = %.3e -- %s"
     % (kap379, kappa_ceil(10),
        "over the ceiling" if kap379 > kappa_ceil(10) else "under the ceiling"))
check("E1.1 fp route executed with a declared bar",
      res379["eta"] > 0 and eta_e_379 > 0
      and res379["floor"] <= min_eig_379 + 4.0 * U_D * norm2_upper(M379),
      "certified floor (%s) never exceeds the eigenvalue MEASUREMENT %.3e "
      "(soundness); the fp Cholesky of the module's own matrix does NOT "
      "complete" % (fmt(res379["floor"], 2), min_eig_379))

# --- E1.1b the module's OWN matrix is certifiably NOT positive semidefinite ---
mp.mp.dps = 60
cert_indef = {}
cert_q = {}
for n in (4, 6, 8, 10, 14, 20):
    tt = np.linspace(0.2, 2.0, n)
    Ad = v379_hankel(tt, eps_d)
    Amp = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            Amp[i, j] = mp.mpf(float(Ad[i, j]))      # exact: doubles are exact
    E, V = mp.eighe(Amp)
    kmin = min(range(n), key=lambda k: E[k])
    x = mp.matrix([V[i, kmin] for i in range(n)])
    q = sum(x[i] * sum(Amp[i, j] * x[j] for j in range(n)) for i in range(n))
    absq = sum(abs(x[i]) * sum(abs(Amp[i, j]) * abs(x[j]) for j in range(n))
               for i in range(n))
    bar = SAFETY * (n + 1) * mp_u() * absq
    cert_indef[n] = bool(q + bar < 0)
    cert_q[n] = q
    info("E1.1b n = %d" % n,
         "x^T Mhat x = %s over the minimal direction, own evaluation bar %s -> %s"
         % (mp.nstr(q, 5), mp.nstr(bar, 3),
            "CERTIFIED NOT PSD" if cert_indef[n]
            else "no negative direction (form positive here)"))
check("E1.1b the module's own computed Hankel is certifiably NOT PSD",
      cert_indef[10],
      "at 60 digits, on the EXACT double entries the module tests: the module's "
      "own size n = 10 carries a CERTIFIED negative direction (x^T Mhat x = %s) "
      "and the module's test (min eig > -1e-10) PASSES it -- the PSD assertion "
      "is true of the MATHEMATICAL Hankel only, never of the matrix that is "
      "actually tested; certified-not-PSD at n = %s"
      % (mp.nstr(cert_q[10], 4),
         ", ".join(str(k) for k in sorted(cert_indef) if cert_indef[k])))

# the entry gap: how far the fp evaluation moves the mathematical matrix
Amp10 = mp_v379_hankel(10)
gap_meas = max(abs(mp.mpf(float(M379[i, j])) - Amp10[i, j])
               for i in range(10) for j in range(10))

# --- E1.2 size / window sweep, fp route -------------------------------------
print("")
print("       %-26s %8s %11s %11s %11s %10s  %s"
      % ("v379 Hankel variant", "n", "floor", "eta_total", "cond(MEAS)",
         "headroom", "label"))
sweep_labels = []
for (t0, t1, wname) in ((0.2, 2.0, "module window"),
                        (0.05, 0.5, "short window"),
                        (1.0, 10.0, "long window")):
    for n in (4, 6, 8, 10, 14, 20, 30, 40, 60):
        if wname != "module window" and n not in (6, 10, 20, 40):
            continue
        tt = np.linspace(t0, t1, n)
        A = v379_hankel(tt, eps_d)
        r = certified_floor(A)
        et = r["eta"] + eta_entry(A, len(eps_d))
        kp = float(np.linalg.cond(A))                    # MEASUREMENT
        rc = record("SEAM.S3.RP.01",
                    "v379 Hankel n=%d [%s]" % (n, wname), n,
                    r["floor"], et, kp)
        sweep_labels.append(rc["label"])
        print("       %-26s %8d %11s %11s %11s %10s  [%s]"
              % (wname, n, fmt(r["floor"], 2), fmt(et, 2), fmt(kp, 2),
                 fmt(rc["headroom"], 2), rc["label"]))
n_meas = sum(1 for L in sweep_labels if L == "MEASUREMENT-ONLY")
check("E1.2 size/window sweep completed",
      len(sweep_labels) == 17,
      "%d variants; MEASUREMENT-ONLY in %d of them (fp route in binary64)"
      % (len(sweep_labels), n_meas))

# --- E1.3 the precision ladder: what would it COST to certify --------------
print("")
print("       %-14s %6s %10s %12s %12s %10s"
      % ("precision cost", "n", "dps", "floor", "eta_chol", "headroom"))
ladder = {}
ladder_floor = {}
for n in (6, 10, 14, 20):
    got = None
    for dps in DPS_LADDER:
        mp.mp.dps = dps
        A = mp_v379_hankel(n)
        r = mp_certified_floor(A)
        et = r["eta"]
        h = float(r["floor"] / et) if et > 0 else 0.0
        print("       %-14s %6d %10d %12s %12s %10.3e"
              % ("", n, dps, mp.nstr(r["floor"], 4), mp.nstr(et, 4), h))
        if h >= BAR_CERT:
            got = dps
            ladder_floor[n] = r["floor"]
            break
    ladder[n] = got
info("E1.3 why binary64 cannot decide it",
     "the MATHEMATICAL Hankel at the module's n = 10 has a CERTIFIED floor "
     "lam_min >= %s (%d digits), while merely ROUNDING its entries to doubles "
     "moves the matrix by %s -- eight orders of magnitude more.  So the "
     "indefiniteness of the tested matrix (E1.1b) is a pure rounding artifact, "
     "and no binary64 eigenvalue test can decide the mathematical statement in "
     "either direction: only the exact route (E1.4) or declared extra precision "
     "can" % (mp.nstr(ladder_floor[10], 4), ladder[10], mp.nstr(gap_meas, 4)))
check("E1.3 precision ladder monotone and successful",
      all(ladder[n] is not None for n in ladder)
      and all(ladder[a] <= ladder[b] for a, b in ((6, 10), (10, 14), (14, 20))),
      "digits needed for headroom >= 10: " +
      ", ".join("n=%d -> %s" % (n, ladder[n]) for n in sorted(ladder)))

# --- E1.4 the latte-free structural certificate -----------------------------
nn, KK = 4, 3
tsym = sp.symbols("t1:%d" % (nn + 1), positive=True)
esym = sp.symbols("e1:%d" % (KK + 1), positive=True)
wsym = sp.symbols("w1:%d" % (KK + 1), nonnegative=True)
Msym = sp.Matrix(nn, nn, lambda i, j: sum(
    wsym[k] * sp.exp(-esym[k] * (tsym[i] + tsym[j])) for k in range(KK)))
Vsym = sp.Matrix(KK, nn, lambda k, i: sp.exp(-esym[k] * tsym[i]))
Dsym = Vsym.T * sp.diag(*wsym) * Vsym
gram_exact = all(sp.expand(sp.expand(Msym[i, j]) - sp.expand(Dsym[i, j])) == 0
                 for i in range(nn) for j in range(nn))
check("E1.4 structural (latte-free) certificate",
      gram_exact,
      "M_ij = sum_k w_k e^{-e_k(t_i+t_j)} = V^T diag(w) V EXACTLY (symbolic, "
      "n=4, K=3); v379 has w_k = 1/1600 > 0 => M >= 0 in exact arithmetic, "
      "with NO floating-point bar")
rec_struct = record("SEAM.S3.RP.01", "v379 Hankel -- structural Gram route", 10,
                    0.0, 0.0, kap379, exact=True,
                    extra="exact V^T diag(w) V, w = 1/1600 > 0")
info("E1.4 what the exact route certifies",
     "the MATHEMATICAL M >= 0 exactly (no bar); transferred to the matrix the "
     "module actually tests only down to eta_entry = %s" % fmt(eta_e_379))
check("E1.4b entry bar is honest",
      float(gap_meas) <= eta_e_379,
      "measured |Mhat - M| (60 digits) = %s <= declared eta_entry = %s"
      % (mp.nstr(gap_meas, 4), fmt(eta_e_379)))

# --- E1.5 the blind band of the module's tolerance --------------------------
shift = min_eig_379 + 1e-11
Mbad = M379 - shift * np.eye(10)
Mbad = 0.5 * (Mbad + Mbad.T)
bad_min = float(np.linalg.eigvalsh(Mbad).min())          # MEASUREMENT
w, V = np.linalg.eigh(Mbad)
neg = certified_negative_direction(Mbad, V[:, 0])
check("E1.5 blind band exhibited",
      neg["fires"] and bad_min > MODULE_TOL_V379,
      "a matrix with CERTIFIED negative direction (x^T A x = %.3e, own fp bar "
      "%.3e) PASSES the module test (min eig = %.3e > %.0e): the tolerance "
      "cannot separate PSD from indefinite in (%.0e, 0)"
      % (neg["q"], neg["bnd"], bad_min, MODULE_TOL_V379, MODULE_TOL_V379))

# --- E1.6 the neg control, certified ----------------------------------------
w, V = np.linalg.eigh(M379g)
negg = certified_negative_direction(M379g, V[:, 0])
check("E1.6 ghost/neg control certified indefinite", negg["fires"],
      "x^T A x = %.3e with fp bar %.3e -- the module's non-vacuity check is "
      "CERTIFIABLE (a negative direction is a certificate, unlike a negative "
      "eigenvalue readout)" % (negg["q"], negg["bnd"]))

# --- E1.7 the gap, certified -------------------------------------------------
mp.mp.dps = 50
band50 = mp_band()
gap_mp = min(e for e, _ in band50)
gap_bar = 40 * mp_u() * (1 + gap_mp)
check("E1.7 the module's gap claim certified",
      gap_mp - gap_bar > mp.mpf("0.9"),
      "gap = %s at 50 digits, evaluation bar %s => certified gap > 0.9 "
      "(claim 1 of the row needs no measurement)"
      % (mp.nstr(gap_mp, 12), mp.nstr(gap_bar, 3)))

# ===========================================================================
section("E2  ROW 2 -- QFT.OSMOMENT.01 / v171: the exact Vandermonde Gram")
# ===========================================================================
r_ = sp.Rational(64, 729)
s_ = sp.Rational(1, 729)
atoms = [sp.Integer(1), r_, s_]
wts = [sp.Rational(1), sp.Rational(1), sp.Rational(1)]


def v171_hankel(N):
    def Cn(n):
        return sum(w * a ** n for w, a in zip(wts, atoms))
    return sp.Matrix(N, N, lambda i, j: Cn(i + j))


exact_rows = []
for N in (3, 4, 5, 8, 12):
    H = v171_hankel(N)
    W = sp.Matrix(N, 3, lambda i, k: atoms[k] ** i)
    fact = sp.simplify(H - W * sp.diag(*wts) * W.T) == sp.zeros(N, N)
    minor = sp.Matrix(3, 3, lambda i, k: atoms[k] ** i).det()   # Vandermonde
    rank_ok = (H.rank() == min(N, 3))
    Hf = np.array(H.evalf(30), dtype=float)
    r = certified_floor(Hf)
    et = r["eta"]                    # entries are exact rationals -> no eta_entry
    up = certified_upshift(Hf)
    kp = float(np.linalg.cond(Hf)) if N <= 3 else float("inf")   # MEASUREMENT
    rec = record("QFT.OSMOMENT.01", "v171 Hankel N=%d (exact route)" % N, N,
                 0.0, 0.0, kp, exact=(fact and rank_ok and minor != 0),
                 extra="rank %d, exact zero eigenvalue multiplicity %d"
                       % (min(N, 3), max(0, N - 3)))
    exact_rows.append(dict(N=N, fact=fact, rank_ok=rank_ok, minor=minor,
                           floor=r["floor"], eta=et, up=up["t"],
                           chol0=r["chol0"]))
    info("E2 N=%d" % N,
         "exact factorisation H = W diag(1,1,1) W^T: %s; Vandermonde minor = %s "
         "!= 0 => rank %d; fp route: chol(A) completes %s, floor = %s vs "
         "eta_chol %s; smallest up-shift %s"
         % (fact, minor, H.rank(), r["chol0"], fmt(r["floor"], 2),
            fmt(et, 2), fmt(up["t"], 2)))

check("E2.1 exact structural certificate (all sizes)",
      all(e["fact"] and e["rank_ok"] and e["minor"] != 0 for e in exact_rows),
      "H = W diag(w) W^T over Q with w > 0 and rank(W) = 3 (nonzero Vandermonde "
      "minor) => H >= 0 EXACTLY at every size; no floating-point bar")
lam_exact_zero = [e for e in exact_rows if e["N"] > 3]
check("E2.2 exact lam_min = 0, so no positive floor exists",
      all(sp.Matrix(v171_hankel(e["N"])).rank() == 3 for e in lam_exact_zero),
      "for N > 3 the Gram is exactly rank 3, so lam_min = 0 EXACTLY: '>= 0' is "
      "certifiable (exact route) but a POSITIVE floor is impossible -- the fp "
      "Cholesky route can only ever state '>= -(t + eta)'")
check("E2.3 fp route on the singular Gram behaves as predicted",
      all((e["floor"] <= e["eta"]) for e in lam_exact_zero),
      "every N > 3 fp floor sits at or below its own bar -- the eigenvalue/"
      "Cholesky route alone would read MEASUREMENT-ONLY here, while the module "
      "already argues the exact route (and only adds a redundant numeric psd "
      "side-check that could be dropped)")

# ===========================================================================
section("E3  ROW 3 -- SEAM.CLOCK.SILVER.01 / v527 (= WOIT.THETA.FREE.01 / v519 "
        "R3.1)")
# ===========================================================================
note("""
v527 A1.1 certifies ENTRYWISE (exactly, through the theta/Wick machinery) that
the bond-cut one-particle OS Gram IS the Hankel matrix G_ab = C(a+b-(N-1)) with
C(d) = (2/N)/sin(pi d/N); that reduction is CITED here, not re-derived.  What is
certified below is the positivity statement itself, which both modules assert as
a min-eigenvalue MEASUREMENT (v527: > 1e-30 at 40 digits; v519 R3.1: inertia
(8,0,0) at 40 digits).
""")
print("")
print("       %-10s %6s %11s %11s %11s %10s  %s"
      % ("silver", "n", "floor", "eta_total", "cond(MEAS)", "headroom",
         "label"))
sil_labels = {}
for N in (8, 16, 24, 32):
    A = sil[N]
    r = certified_floor(A)
    et = r["eta"] + eta_entry(A, 4)
    kp = float(np.linalg.cond(A))                        # MEASUREMENT
    rc = record("SEAM.CLOCK.SILVER.01", "v527 half-circle Hankel N=%d" % N,
                A.shape[0], r["floor"], et, kp)
    sil_labels[N] = rc["label"]
    print("       N = %-6d %6d %11s %11s %11s %10s  [%s]"
          % (N, A.shape[0], fmt(r["floor"], 2), fmt(et, 2), fmt(kp, 2),
             fmt(rc["headroom"], 2), rc["label"]))
check("E3.1 fp certificates computed for every N",
      len(sil_labels) == 4,
      "labels: " + ", ".join("N=%d [%s]" % (N, sil_labels[N])
                             for N in sorted(sil_labels)))
mp.mp.dps = 40
sil_mp = {}
for N in (8, 16, 24, 32):
    Amp = mp_silver_hankel(N)
    r = mp_certified_floor(Amp)
    h = float(r["floor"] / r["eta"]) if r["eta"] > 0 else 0.0
    sil_mp[N] = h
    info("E3.2 N=%d at 40 digits" % N,
         "floor = %s, eta_chol = %s, headroom = %.3e"
         % (mp.nstr(r["floor"], 5), mp.nstr(r["eta"], 4), h))
check("E3.2 40-digit route certifies every N",
      all(h >= BAR_CERT for h in sil_mp.values()),
      "the precision the modules already use (40 digits) turns their "
      "MEASUREMENT into a certificate at headroom >= %.0e"
      % min(sil_mp.values()))
check("E3.3 v519 R3.1 object covered",
      sil[16].shape[0] == 8,
      "the N=16 half-circle Hankel IS the 8x8 one-particle bond-cut Gram of "
      "v519 R3.1 (entrywise reduction certified in v527 A1.1, cited): its "
      "positivity is certified here, label [%s] in binary64" % sil_labels[16])

# ===========================================================================
section("E4  SYNTHESIS -- per-row verdicts and the recommendation table")
# ===========================================================================
print("")
print("       %-22s %-38s %10s %8s  %s"
      % ("ledger row", "matrix", "headroom", "route", "label"))
print("       " + "-" * 92)
for m in MATRICES:
    print("       %-22s %-38s %10s %8s  [%s]"
          % (m["row"], m["tag"][:38], fmt(m["headroom"], 2),
             "exact" if m["exact"] else "fp64", m["label"]))

# --- per-row two-column verdict ---------------------------------------------
ROW_VERDICT = {}


def row_verdict(row, wording_matrices, claim_exact_available):
    labs = [m["label"] for m in MATRICES
            if m["row"] == row and m["tag"] in wording_matrices]
    worst = ("MEASUREMENT-ONLY" if "MEASUREMENT-ONLY" in labs
             else ("MARGINAL" if "MARGINAL" in labs else "CERT-UP"))
    claim = "CERT" if (claim_exact_available or worst == "CERT-UP") else "OPEN"
    ROW_VERDICT[row] = dict(wording=worst, claim=claim)
    return ROW_VERDICT[row]


v1 = row_verdict("SEAM.S3.RP.01",
                 {"v379 Hankel n=10 (module params)"}, True)
v2 = row_verdict("QFT.OSMOMENT.01",
                 {"v171 Hankel N=5 (exact route)"}, True)
v3 = row_verdict("SEAM.CLOCK.SILVER.01",
                 {"v527 half-circle Hankel N=%d" % N for N in (8, 16, 24, 32)},
                 False)

print("")
print("       %-22s %-18s %-18s %s"
      % ("ledger row", "CLAIM (any route)", "WORDING (as worded)",
         "recommendation for a promotion / deep-sync pass"))
print("       " + "-" * 108)
RECS = {
    "SEAM.S3.RP.01": (
        "keep [E]; REPLACE the method: the row's own wording 'min eigenvalue >= "
        "0 to numerical tolerance' is a MEASUREMENT -- no fp Cholesky of the "
        "module's matrix completes, its cond is over the certifiability ceiling, "
        "the matrix ACTUALLY TESTED is certifiably NOT PSD (E1.1b) and the "
        "tolerance's blind band is exhibited (E1.5).  The claim is "
        "certifiable LATTE-FREE by the Gram identity M = V^T diag(w) V with "
        "w = 1/1600 > 0 (E1.4) -- the same route v171 uses.  Recommended: v379 "
        "check 2 asserts the exact factorisation (plus the certified entry bar "
        "eta_entry) instead of eigvalsh; ledger text drops 'to numerical "
        "tolerance' in favour of 'exact positive-mixture Gram'.  If the "
        "eigenvalue route were kept as the ONLY support, the honest typing "
        "would be [E] -> [N] (Numerical) -- NOT executed here."),
    "QFT.OSMOMENT.01": (
        "keep [E]/[I]; no change needed.  The exact Vandermonde-Gram route is "
        "already the module's argument and it certifies '>= 0' with no fp bar "
        "(E2.1); lam_min = 0 EXACTLY for N > 3 (E2.2), so the redundant numeric "
        "psd side-check (eigenvals >= -1e-12) supports nothing and may be "
        "dropped or relabelled MEASUREMENT."),
    "SEAM.CLOCK.SILVER.01": (
        "keep [E]; strengthen wording.  The 40-digit min-eigenvalue statement "
        "is a MEASUREMENT, but a shifted-Cholesky certificate at the SAME "
        "precision certifies a positive floor with large headroom (E3.2), and "
        "even binary64 certifies N = 8/16 (E3.1).  Recommended: state the "
        "positivity as a certified floor with the declared bar; this also "
        "covers WOIT.THETA.FREE.01 / v519 R3.1, the same 8x8 object."),
}
for row in ("SEAM.S3.RP.01", "QFT.OSMOMENT.01", "SEAM.CLOCK.SILVER.01"):
    v = ROW_VERDICT[row]
    print("       %-22s %-18s %-18s" % (row, v["claim"], "[" + v["wording"] + "]"))
    note(RECS[row])
    print("")

info("E4 not reproduced (flagged, excluded from the verdict)",
     "WOIT.BETA2.OS.01 / v524: the 37x37 (min eig 1.7801e-6) and 16x16 (min "
     "3.3471e-3) OS Grams are asserted as 40-digit inertia MEASUREMENTS; their "
     "construction needs the module's theta/Wick machinery.  Follow-up item: "
     "same shifted-Cholesky certificate, expected CERT-UP given those floors.")
info("E4 what a promotion / deep-sync pass would have to carry",
     "(1) v379 check 2 rewritten to the exact Gram certificate + entry bar; "
     "(2) ledger text of SEAM.S3.RP.01 (the phrase 'min eigenvalue >= 0 to "
     "numerical tolerance'); (3) v527/v519 positivity wording -> certified "
     "floor with declared bar; (4) v171 numeric side-check relabelled; "
     "(5) v524 follow-up.  NONE of this is executed by this probe.")

check("E4.1 every tested row carries a two-column verdict",
      len(ROW_VERDICT) == 3
      and all(v["claim"] in ("CERT", "OPEN") for v in ROW_VERDICT.values()),
      "rows: " + ", ".join("%s claim=%s wording=%s"
                           % (k, v["claim"], v["wording"])
                           for k, v in ROW_VERDICT.items()))
check("E4.2 verdict logic self-consistent",
      all((v["claim"] == "CERT") or (v["wording"] == "MEASUREMENT-ONLY")
          for v in ROW_VERDICT.values()),
      "a certified wording implies a certified claim (no row certifies its "
      "wording while its claim stays open)")

# ===========================================================================
section("TOTAL")
# ===========================================================================
claims_ok = all(v["claim"] == "CERT" for v in ROW_VERDICT.values())
wording_ok = all(v["wording"] == "CERT-UP" for v in ROW_VERDICT.values())
if claims_ok and wording_ok:
    VERDICT = "ALL-CERT"
elif claims_ok:
    VERDICT = "MIXED"
else:
    VERDICT = "DOWNGRADE-NEEDED"

print("")
note("""
VERDICT %s.  Every RP/PSD statement tested is certifiable -- but SEAM.S3.RP.01 is
not certifiable by the route its own row names, and the strongest form of that
finding is not a bar argument at all: the 10x10 Hankel the module builds and
tests is, as a matrix of doubles, CERTIFIABLY NOT positive semidefinite (a
certified negative direction at 60 digits, E1.1b), and the module's tolerance
passes it anyway.  The exponential ill-conditioning is the reason (cond ~ %.1e,
over the certifiability ceiling %.1e at n = 10), and the entry bar eta_entry =
%.1e -- the price of evaluating a transcendental kernel in binary64 -- dominates
every floor the fp route could produce.  E1.5 makes the blind band explicit: a
matrix with a CERTIFIED negative direction passes 'min eigenvalue > -1e-10'.  The
repair is not a weaker status: the same object is a positive-mixture Gram,
M = V^T diag(1/1600) V, hence >= 0 in EXACT arithmetic with no bar at all (E1.4)
-- exactly the route v171 already takes for its own Hankel.  If one wants a
positive FLOOR rather than '>= 0', E1.3 prices it: %s digits at n = 6..20.  For
the silver Hankel of v527/v519 the 40-digit precision those modules already run
turns their measurement into a certificate with large headroom (E3.2), and n = 8
and 16 even certify in binary64.  No marker moves are warranted; what is
warranted is method and wording -- plus one honest deletion: an eigenvalue
tolerance is not a certificate.
""" % (VERDICT, kap379, kappa_ceil(10), eta_e_379,
       "/".join(str(ladder[n]) for n in sorted(ladder))))

print("")
print("TOTAL.probe        part %d, contract CERT.FLOOR" % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.rows         %s"
      % "; ".join("%s claim=%s wording=[%s]"
                  % (k, v["claim"], v["wording"]) for k, v in ROW_VERDICT.items()))
print("TOTAL.matrices     %d certificates issued (%d exact/structural, %d fp64)"
      % (len(MATRICES), sum(1 for m in MATRICES if m["exact"]),
         sum(1 for m in MATRICES if not m["exact"])))
print("TOTAL.bars         u = %.3e, SAFETY = %.0f, eta_chol = SAFETY*c_h(n)*u*"
      "||A||_inf with c_h(n) = n(n+1)/(1-(n+1)u) (Wilkinson 1968; Higham 2002 "
      "Thm 10.3/10.4; Rump 2006), plus eta_entry for fp-evaluated kernels"
      % (U_D, SAFETY))
print("TOTAL.downgrade    recommended: NONE ([E] stays); method/wording repair "
      "recommended for SEAM.S3.RP.01 (+ v527/v519 wording, v171 side-check)")
print("TOTAL.ledger       untouched by this probe (recommendations are output)")
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised matrix %d (cap %d)"
      % (MAX_N_SEEN, CAP_FACTOR_N))
print("TOTAL.status       %s" % ("ALL CHECKS PASSED" if FAIL == 0
                                 else "%d CHECK(S) FAILED" % FAIL))
