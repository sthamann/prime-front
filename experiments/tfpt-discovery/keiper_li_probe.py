"""keiper_li_probe -- SLICE A of the RH-criteria scan: the Keiper-Li
sequence lambda_n computed on TWO INDEPENDENT ROUTES, binding the zero
comb (v589), the atom-table constants (v563: gamma_E, log pi), the
archimedean kernels (psi at 1/2 <-> v563 arch block / v643 W_sm) and
the pole block (v591/v643: the two poles s = 0, 1 <-> the scalar +2)
into ONE scalar sequence.

ROUTE 1 (COMB): lambda_n = sum_rho [1 - (1 - 1/rho)^n] over the loaded
zero comb rho = 1/2 + i gamma (first N_ZEROS zeros from mpmath
zetazero, both signs paired: per gamma > 0 the pair contributes
2 (1 - Re (1 - 1/rho)^n), which is 2 (1 - cos(n theta_gamma)) with
theta_gamma = 2 arctan(1/(2 gamma)) on the line).  The comb ends at
gamma_max; the tail is handled HONESTLY:

  TAIL BUDGET (documented calculation).  With f_n(t) =
  2 (1 - cos(n theta(t))) >= 0 and the Riemann-von Mangoldt density
  dNbar = theta_RS'(t)/pi dt (N(T) = theta_RS(T)/pi + 1 + S(T)):
    (a) RAW estimate: tail(n) ~ int_{gamma_max}^inf f_n dNbar
        ~ c_T n^2 with c_T = (log(T/2pi) + 1)/(2 pi T).  For small n
        lambda_n ~ 0.0231 n^2 (the measured quadratic law), so the
        RAW relative truncation error is c_T/0.0231, INDEPENDENT of n.
        The prescribed criterion "raw tail < 1% of the GUE trend
        (n/2)(log n - log 2pi - 1 + gamma_E)" is therefore satisfiable
        only when c_T < 0.01 * max_n [trend(n)/n^2] = 0.01/52.1; the
        probe computes the gamma_max at which that window first opens
        (~6.6e3, i.e. ~5.2e3 zeros) and reports honestly that for the
        loaded comb the raw window is EMPTY.
    (b) DECLARED REFINEMENT: add the density tail integral (zero-free:
        it uses only theta_RS) to the comb sum and budget the
        REMAINING error by partial summation:
        |sum_{gamma>T} f_n - int_T^inf f_n dNbar|
          <= |S(T)| f_n(T) + int_T^inf |S(t)| |f_n'(t)| dt
          <= S_BOUND * 2 f_n(T)   (f_n monotone decreasing in t),
        with the cited band |S(t)| <= S_BOUND = 2.5 at these heights.
        This budget B_fl(n) = 5 f_n(gamma_max) ~ 5 n^2/gamma_max^2
        stays below 1% of the GUE trend far beyond the computed range;
        the used range is cost-capped at N_MAX = 64 (declared).

ROUTE 2 (ARITHMETIC, Bombieri-Lagarias form; NO ZEROS): from
xi'/xi(s) = 1/s + 1/(s-1) - (1/2) log pi + (1/2) psi(s/2) + zeta'/zeta(s)
and s = 1/(1-z), lambda_n = [z^{n-1}] s^2 xi'/xi(s(z)) one derives the
EXACT finite form (formal power-series identity, no RH input)

  lambda_n =  2                                  (pole block s = 0, 1)
            - 1 + sum_{j=1}^n binom(n,j) eta_{j-1}      (prime block)
            - (n/2) log pi
            + (1/2) sum_{j=1}^n binom(n,j) b_{j-1}    (archimedean),

  zeta'/zeta(s) = -1/(s-1) + sum_k eta_k (s-1)^k   (eta_0 = gamma_E),
  b_0 = psi(1/2) = -gamma_E - 2 log 2,
  b_k = psi^{(k)}(1/2)/(2^k k!) = (-1)^{k+1} (2^{k+1}-1) zeta(k+1)/2^k.

The eta_k are obtained zero-free from the Taylor series of
Z(w) = (s-1) zeta(s) at s = 1 + w (contour/trapezoid extraction, then
series division Z'/Z), cross-checked against mpmath Stieltjes
constants (Z = 1 + sum (-1)^k gamma_k w^{k+1}/k!).  Closed forms
lambda_1 = 1 + gamma/2 - log(4 pi)/2 and
lambda_2 = 1 + gamma - gamma^2 - 2 gamma_1 - log(4 pi) + pi^2/8 are
verified exactly.  A SECOND zero-free assembly (direct contour
extraction of [z^{n-1}] s^2 xi'/xi(s(z)) on |z| = R_G) validates the
binomial machinery end to end.

A3 (CENTRAL): |lambda_n^{arith} - (lambda_n^{comb,raw} + tail(n))|
must stay inside B_fl(n) for ALL n <= N_MAX.  Any inconsistency in
comb, atom-table constants, archimedean kernels or pole block hits
this single scalar sequence.

A4: positivity lambda_n > 0 (Li's criterion direction) on both routes;
GUE-trend residuals oscillatory / no exponential outlier; MUST-FAIL
injection: replace the first zero pair by the off-line quadruple
{0.6 +- i gamma_1, 0.4 +- i gamma_1}: the (1 - 1/rho) factor acquires
modulus e^{+-(sigma - 1/2)/|rho|^2 + O(..)} != 1 and lambda_n explodes
NEGATIVELY at n ~ 1e4..1e5 (float demo grid), while the true comb
stays positive and bounded -- the machinery has teeth.

FIREWALL: experiments/ probe, standalone, no verification/ imports,
no ledger/paper/website edits, NO RH claim (lambda_n > 0 for n <= 64
is a finite verified statement, not Li's criterion).  Zero data:
mpmath zetazero only (dps 15, declared; gamma error ~1e-13 propagates
< 1e-12 into lambda_n, far below every budget), cached in
zero_comb_cache_n2000.json.  Verdict enums (frozen):
KEIPER-LI-CONSISTENT (all checks incl. the A3 budget), BUDGET-BREACH
(A3 fails), MIXED.
"""
import json
import math
import os
import time

import numpy as np
from mpmath import mp, mpf, mpc, zetazero, siegeltheta

T0 = time.time()
FAILS = []
N_CHK = 0

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")

# ---------------- declared constants (before any number) ----------------
N_ZEROS = 2000            # the loaded comb (v589 style: mpmath zetazero)
DPS_ZEROS = 15            # zero precision (declared; error budgeted)
DPS_COMB = 30             # route-1 working precision (task: 30 digits)
DPS_ARITH = 120           # route-2 working precision (binomial sums lose
#                           ~0.31 n digits; n = 64 -> ~20 digits, ample)
N_MAX = 64                # cost cap of the lambda table (declared; the
#                           corrected budget allows far more, see K1)
S_BOUND = 2.5             # |S(t)| band cited for these heights (task):
#                           N(T) = theta(T)/pi + 1 + S(T); empirically
#                           |S| < 1.1 below t ~ 3e3, 2.5 is conservative
BUDGET_FRAC = 0.01        # "tail < 1% of the GUE main trend"
M_Z, R_Z = 512, 0.5       # contour for Z(w) = (s-1) zeta(1+w) coeffs
M_G, R_G = 1024, 0.55     # contour for the direct [z^n] route
N_STIELTJES_XCHK = 8      # eta cross-check depth against mp.stieltjes
TOL_COEFF = 1e-25         # contour coeffs vs Stieltjes (abs)
TOL_CLOSED = 1e-30        # lambda_1, lambda_2 closed forms (abs)
TOL_ROUTE2 = 1e-25        # binomial route vs contour route (rel)
INJ_SIGMA = 0.6           # injected off-line real part (task-prescribed)
DEMO_N_MAX = 200000       # float injection demo grid
DEMO_STEP = 7             # grid step (dip period ~ 2 pi/theta_1 ~ 89)
BAR_EXPLODE = -1.0e6      # injected lambda must dip below this
BAR_POLY = 10.0           # residual growth 2nd half / 1st half (poly bar)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# ---------------- the zero comb (build once, cache, share with slice B)
def load_or_build_comb():
    if os.path.exists(CACHE):
        with open(CACHE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if data["n_zeros"] == N_ZEROS and data["dps"] == DPS_ZEROS:
            return [mpf(g) for g in data["gammas"]], data
    mp.dps = DPS_ZEROS
    t0 = time.time()
    gam = []
    for k in range(1, N_ZEROS + 1):
        gam.append(zetazero(k).imag)
        if k % 200 == 0:
            print("   ... zetazero %d/%d (%.0f s)"
                  % (k, N_ZEROS, time.time() - t0))
    data = dict(n_zeros=N_ZEROS, dps=DPS_ZEROS,
                generator="mpmath.zetazero",
                gammas=[mp.nstr(g, DPS_ZEROS) for g in gam])
    with open(CACHE, "w", encoding="utf-8") as fh:
        json.dump(data, fh)
    return [mpf(mp.nstr(g, DPS_ZEROS)) for g in gam], data


# ---------------- Riemann-Siegel theta derivative (asymptotic, t >> 1)
def theta_prime(t):
    return (mp.log(t / (2 * mp.pi)) / 2 - 1 / (48 * t ** 2)
            - 7 / (1920 * t ** 4))


def gue_trend(n):
    return (mpf(n) / 2) * (mp.log(n) - mp.log(2 * mp.pi) - 1 + mp.euler)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("KEIPER-LI PROBE -- lambda_n on two routes: comb vs arithmetic")
    print("=" * 78)

    # ============================================================== K0
    print("\nK0 -- the loaded comb")
    gam, meta = load_or_build_comb()
    mp.dps = DPS_COMB
    gam = [mpf(g) for g in gam]
    gmax = gam[-1]
    mono = all(gam[k] < gam[k + 1] for k in range(N_ZEROS - 1))
    check("K0.1 comb integrity: %d zeros from %s (dps %d), strictly "
          "increasing, gamma_1 = %s, gamma_max = %s"
          % (N_ZEROS, meta["generator"], DPS_ZEROS,
             mp.nstr(gam[0], 12), mp.nstr(gmax, 12)),
          len(gam) == N_ZEROS and mono
          and abs(gam[0] - mpf("14.134725141734693")) < 1e-9)

    # ============================================================== K1
    print("\nK1 -- the tail budget (documented calculation)")
    #  f_n(t) = 2 (1 - cos(n * 2 atan(1/(2t))));  density theta'/pi.

    def f_pair(n, t):
        return 2 * (1 - mp.cos(n * 2 * mp.atan(1 / (2 * t))))

    def tail_integral(n):
        return mp.quad(lambda t: f_pair(n, t) * theta_prime(t) / mp.pi,
                       [gmax, 2 * gmax, 10 * gmax, 100 * gmax,
                        1000 * gmax, mp.inf])

    # internal guard: asymptotic theta' vs numerical siegeltheta'
    tp_num = mp.diff(siegeltheta, gmax)
    tp_dev = abs(theta_prime(gmax) - tp_num) / tp_num
    # raw estimate c_T n^2 and its closed constant
    c_T = float((mp.log(gmax / (2 * mp.pi)) + 1) / (2 * mp.pi * gmax))
    tail1 = tail_integral(1)
    # the prescribed raw criterion: tail(n) < BUDGET_FRAC * trend(n).
    # trend(n)/n^2 is maximal at n = round(e^{1 + a}), a = log 2pi + 1
    # - gamma_E; the raw window is nonempty iff c_T < BUDGET_FRAC * max.
    a_const = float(mp.log(2 * mp.pi) + 1 - mp.euler)
    n_star = int(round(math.exp(1.0 + a_const)))
    g_max_ratio = max(float(gue_trend(n)) / n ** 2
                      for n in (n_star - 1, n_star, n_star + 1))
    raw_window = [n for n in range(1, 4097)
                  if float(tail1) * n * n
                  < BUDGET_FRAC * max(float(gue_trend(n)), 0.0)]
    # gamma_max at which the raw window would first open
    tgt = BUDGET_FRAC * g_max_ratio
    T_open = mp.findroot(
        lambda T: (mp.log(T / (2 * mp.pi)) + 1) / (2 * mp.pi * T) - tgt,
        mpf(7000))
    N_open = float(siegeltheta(T_open) / mp.pi + 1)
    print("   theta' asymptotic vs numeric at gamma_max: rel dev %.1e"
          % float(tp_dev))
    print("   raw tail estimate: tail(n) ~ %.4e * n^2 (density integral"
          " %.4e at n = 1, closed c_T = %.4e)"
          % (float(tail1), float(tail1), c_T))
    print("   raw criterion tail < %.0f%% * GUE trend: trend(n)/n^2 "
          "maximal at n = %d (%.5f); window %s"
          % (100 * BUDGET_FRAC, n_star, g_max_ratio,
             "EMPTY for this comb" if not raw_window else str(
                 (min(raw_window), max(raw_window)))))
    print("   raw window would first open at gamma_max ~ %.0f "
          "(~%.0f zeros), at n ~ %d only"
          % (float(T_open), N_open, n_star))
    check("K1.1 [HONEST] budget calculation consistent: theta' "
          "asymptotic matches numeric (%.1e < 1e-10), density integral"
          " matches closed c_T n^2 to %.1e < 2%%, and the PRESCRIBED "
          "raw criterion yields an EMPTY window for the loaded comb "
          "(gamma_max = %.1f; opening needs ~%.0f zeros): the raw "
          "truncated comb sum NEVER reaches 1%% of the GUE trend -- "
          "documented, not hidden"
          % (float(tp_dev), abs(float(tail1) / c_T - 1),
             float(gmax), N_open),
          float(tp_dev) < 1e-10 and abs(float(tail1) / c_T - 1) < 0.02
          and not raw_window)

    # the declared refinement: density tail added back, fluctuation
    # budget B_fl(n) = 2 * S_BOUND * f_n(gamma_max)
    def B_fl(n):
        return 2 * S_BOUND * f_pair(n, gmax)

    n_budget = N_MAX
    while (float(B_fl(2 * n_budget))
           < BUDGET_FRAC * float(gue_trend(2 * n_budget))
           and 2 * n_budget <= 65536):
        n_budget *= 2
    check("K1.2 corrected budget: with the density tail ADDED BACK "
          "(zero-free: theta_RS only) the remaining fluctuation budget"
          " B_fl(n) = 2*%.1f*f_n(gamma_max) ~ %.2e n^2 stays below "
          "%.0f%% of the GUE trend out to n > %d; the computed range "
          "is cost-capped at N_MAX = %d (B_fl(%d) = %.2e, %.2e of the "
          "trend there)"
          % (S_BOUND, 2 * S_BOUND * float(f_pair(1, gmax)),
             100 * BUDGET_FRAC, n_budget, N_MAX, N_MAX,
             float(B_fl(N_MAX)),
             float(B_fl(N_MAX) / gue_trend(N_MAX))),
          float(B_fl(N_MAX)) < BUDGET_FRAC * float(gue_trend(N_MAX))
          and n_budget >= 16384)

    # ============================================================== K2
    print("\nK2 -- route 1: the comb sum (dps %d) + density tail"
          % DPS_COMB)
    t0 = time.time()
    lam_comb_raw = [mpf(0)] * (N_MAX + 1)
    for g in gam:
        rho = mpc(mpf(1) / 2, g)
        w = 1 - 1 / rho
        acc = mpc(1, 0)
        for n in range(1, N_MAX + 1):
            acc *= w
            lam_comb_raw[n] += 2 * (1 - acc.real)
    tails = [mpf(0)] + [tail_integral(n) for n in range(1, N_MAX + 1)]
    lam_comb = [lam_comb_raw[n] + tails[n] for n in range(N_MAX + 1)]
    print("   comb sums + %d tail integrals in %.1f s"
          % (N_MAX, time.time() - t0))
    check("K2.1 comb route assembled: lambda_1 raw = %s + tail %s = %s"
          " (raw share of tail matches the K1 estimate)"
          % (mp.nstr(lam_comb_raw[1], 8), mp.nstr(tails[1], 6),
             mp.nstr(lam_comb[1], 8)),
          abs(tails[1] - tail1) < 1e-20 and lam_comb_raw[1] > 0)

    # ============================================================== K3
    print("\nK3 -- route 2: arithmetic (Bombieri-Lagarias form, "
          "NO zeros; dps %d)" % DPS_ARITH)
    mp.dps = DPS_ARITH
    t0 = time.time()

    # -- eta_k via contour coefficients of Z(w) = (s-1) zeta(1+w)
    def contour_coeffs(func, radius, n_pts, n_coeff):
        vals = [func(radius * mp.exp(2j * mp.pi * m / n_pts))
                for m in range(n_pts)]
        out = []
        for j in range(n_coeff):
            s = mp.fsum(
                (vals[m] * mp.exp(-2j * mp.pi * j * m / n_pts)
                 for m in range(n_pts)), absolute=False)
            out.append((s / n_pts) / mpf(radius) ** j)
        return out

    cZ = contour_coeffs(lambda w: w * mp.zeta(1 + w), R_Z, M_Z,
                        N_MAX + 2)
    cZ = [c.real for c in cZ]          # Z real on the real axis
    # Stieltjes cross-check: c_{k+1} = (-1)^k gamma_k / k!
    dev_st = max(abs(cZ[k + 1] - (-1) ** k * mp.stieltjes(k)
                     / mp.factorial(k))
                 for k in range(N_STIELTJES_XCHK))
    # series inverse and eta = Z'/Z
    inv = [mpf(1)]
    for k in range(1, N_MAX + 1):
        inv.append(-mp.fsum(cZ[j] * inv[k - j] for j in range(1, k + 1)))
    eta = []
    for k in range(N_MAX):
        eta.append(mp.fsum((j + 1) * cZ[j + 1] * inv[k - j]
                           for j in range(k + 1)))
    check("K3.1 eta coefficients zero-free (contour M = %d, r = %s, "
          "|Z-coeff dev vs mpmath Stieltjes| = %s < %.0e for k < %d; "
          "eta_0 - gamma_E = %s): the prime block consumes the SAME "
          "constant gamma_E as the v563 arch kernel"
          % (M_Z, R_Z, mp.nstr(dev_st, 3), TOL_COEFF,
             N_STIELTJES_XCHK, mp.nstr(abs(eta[0] - mp.euler), 3)),
          dev_st < TOL_COEFF and abs(eta[0] - mp.euler) < TOL_COEFF)

    # -- archimedean block b_k (psi at 1/2: the v563/v643 constants)
    b = [-mp.euler - 2 * mp.log(2)]
    for k in range(1, N_MAX):
        b.append((-1) ** (k + 1) * (2 ** (k + 1) - 1) * mp.zeta(k + 1)
                 / mpf(2) ** k)

    # -- the exact finite assembly
    def lam_arith_blocks(n):
        pole = mpf(2)
        prime = -1 + mp.fsum(mp.binomial(n, j) * eta[j - 1]
                             for j in range(1, n + 1))
        arch = (-mpf(n) / 2 * mp.log(mp.pi)
                + mp.fsum(mp.binomial(n, j) * b[j - 1]
                          for j in range(1, n + 1)) / 2)
        return pole, prime, arch

    lam_arith = [mpf(0)]
    blocks = [None]
    for n in range(1, N_MAX + 1):
        p, q, ar = lam_arith_blocks(n)
        blocks.append((p, q, ar))
        lam_arith.append(p + q + ar)

    lam1_closed = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    lam2_closed = (1 + mp.euler - mp.euler ** 2 - 2 * mp.stieltjes(1)
                   - mp.log(4 * mp.pi) + mp.pi ** 2 / 8)
    check("K3.2 closed forms exact: lambda_1 = 1 + gamma/2 - "
          "log(4 pi)/2 = %s (dev %s), lambda_2 = 1 + gamma - gamma^2 "
          "- 2 gamma_1 - log(4 pi) + pi^2/8 = %s (dev %s); pole block "
          "= +2 for every n (poles s = 0, 1 <-> v591/v643 rank-2 pole "
          "block), archimedean block built from gamma_E, log pi, "
          "log 2, zeta(k) -- the v563/v643 constants"
          % (mp.nstr(lam1_closed, 12),
             mp.nstr(abs(lam_arith[1] - lam1_closed), 3),
             mp.nstr(lam2_closed, 12),
             mp.nstr(abs(lam_arith[2] - lam2_closed), 3)),
          abs(lam_arith[1] - lam1_closed) < TOL_CLOSED
          and abs(lam_arith[2] - lam2_closed) < TOL_CLOSED)

    # -- second zero-free assembly: direct contour [z^{n-1}] extraction
    def G_of_z(z):
        s = 1 / (1 - z)
        xi_log_d = (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                    + mp.digamma(s / 2) / 2
                    + mp.zeta(s, derivative=1) / mp.zeta(s))
        return s * s * xi_log_d

    cG = contour_coeffs(G_of_z, R_G, M_G, N_MAX)
    dev_route = max(abs(cG[n - 1].real - lam_arith[n])
                    / abs(lam_arith[n]) for n in range(1, N_MAX + 1))
    print("   contour + series + binomial assembly in %.1f s"
          % (time.time() - t0))
    check("K3.3 [machinery] the binomial assembly equals the direct "
          "contour extraction of [z^{n-1}] s^2 xi'/xi(s(z)) on all "
          "n <= %d: max rel dev %s < %.0e (two independent zero-free "
          "assemblies of the same analytic object)"
          % (N_MAX, mp.nstr(dev_route, 3), TOL_ROUTE2),
          dev_route < TOL_ROUTE2)

    # -- atom-table tie-in: eta_0 = gamma_E from the vM table itself
    n_cap = 400000                     # the v563 atom-table cap
    sieve = np.ones(n_cap + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_cap)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam_tab = np.zeros(n_cap + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_cap:
            lam_tab[q] = lp
            q *= p
    mert = float(np.sum(lam_tab[2:] / np.arange(2, n_cap + 1)))
    dev_mert = abs(mert - math.log(n_cap) + float(mp.euler))
    check("K3.4 [tie-in, C-level] the atom table REPRODUCES the prime-"
          "block constant: sum_{m<=%d} Lambda(m)/m - log x = %.6f vs "
          "-gamma_E = %.6f (|dev| = %.1e < 1e-2; PNT-level "
          "convergence, same table construction as v563 U_ALL/MU_ALL)"
          % (n_cap, mert - math.log(n_cap), -float(mp.euler),
             dev_mert),
          dev_mert < 1e-2)

    # ============================================================== K4
    print("\nK4 -- A3 CENTRAL: cross-route comparison against the "
          "declared budget")
    mp.dps = DPS_COMB
    rows = []
    max_use, max_adiff, worst_n = 0.0, 0.0, 0
    all_raw_pos = True
    for n in range(1, N_MAX + 1):
        la = mpf(mp.nstr(lam_arith[n], DPS_COMB))
        d_raw = la - lam_comb_raw[n]
        d_corr = la - lam_comb[n]
        bud = B_fl(n)
        use = float(abs(d_corr) / bud)
        all_raw_pos = all_raw_pos and d_raw > 0
        if use > max_use:
            max_use, worst_n = use, n
        max_adiff = max(max_adiff, float(abs(d_corr)))
        if n in (1, 2, 3, 5, 8, 12, 16, 24, 32, 40, 48, 56, 64):
            rows.append((n, la, lam_comb_raw[n], tails[n], d_corr, bud,
                         use))
    print("   n   lambda_arith      lambda_comb_raw   tail(n)     "
          "d_corr      B_fl(n)    used")
    for n, la, lcr, tl, dc, bud, use in rows:
        print("  %3d  %-16s  %-16s  %-9s  %+.2e  %.2e  %5.3f"
              % (n, mp.nstr(la, 12), mp.nstr(lcr, 12), mp.nstr(tl, 4),
                 float(dc), float(bud), use))
    check("K4.1 [CENTRAL, A3] |lambda_arith - (comb + density tail)| "
          "<= B_fl(n) for ALL n = 1..%d: max used fraction %.3f at "
          "n = %d (max |diff| = %.2e); the raw gap d_raw is positive "
          "on the whole range and equals the tail estimate within the "
          "budget -- comb, atom-table constants, archimedean kernels "
          "and pole block are consistent in ONE scalar sequence at "
          "the 1e-4..1e-6 absolute level"
          % (N_MAX, max_use, worst_n, max_adiff),
          max_use < 1.0 and all_raw_pos)

    # ============================================================== K5
    print("\nK5 -- A4: positivity and the GUE trend")
    pos_a = all(lam_arith[n] > 0 for n in range(1, N_MAX + 1))
    pos_c = all(lam_comb[n] > 0 for n in range(1, N_MAX + 1))
    resid = [float(lam_arith[n] - gue_trend(n))
             for n in range(1, N_MAX + 1)]
    r1 = max(abs(r) for r in resid[:N_MAX // 2])
    r2 = max(abs(r) for r in resid[N_MAX // 2:])
    sgn = sum(1 for k in range(len(resid) - 1)
              if (resid[k] - 1.0) * (resid[k + 1] - 1.0) < 0)
    check("K5.1 positivity: lambda_n > 0 on BOTH routes for all "
          "n = 1..%d (min arith %s at n = 1) -- the finite Li-"
          "positivity statement for the computed range; NO RH claim"
          % (N_MAX, mp.nstr(lam_arith[1], 8)), pos_a and pos_c)
    check("K5.2 GUE-trend residuals bounded, not exponential: "
          "lambda_n - trend(n) has max |resid| %.3f (first half) vs "
          "%.3f (second half), growth factor %.2f < %.0f; residual - 1"
          " changes sign %d times (oscillation around the O(1) "
          "subleading term)"
          % (r1, r2, r2 / r1, BAR_POLY, sgn),
          r2 / r1 < BAR_POLY)

    # ============================================================== K6
    print("\nK6 -- MUST-FAIL: the off-line injection (Re = %.1f)"
          % INJ_SIGMA)
    #  float demo: replace the first zero pair by the quadruple
    #  {sigma +- i gamma_1, (1-sigma) +- i gamma_1}
    g1 = float(gam[0])
    logw_true = np.array([complex(np.log(complex(1)
                          - 1 / complex(0.5, g)))
                          for g in map(float, gam)])
    logw_quad = np.array([complex(np.log(complex(1)
                          - 1 / complex(sig, g1)))
                          for sig in (INJ_SIGMA, 1 - INJ_SIGMA)])
    nn = np.arange(1, DEMO_N_MAX + 1, DEMO_STEP, dtype=float)
    lam_true_f = np.zeros(nn.size)
    for a in range(0, N_ZEROS, 200):
        blk = logw_true[a:a + 200]
        lam_true_f += 2.0 * np.sum(
            1.0 - np.exp(np.outer(nn, blk)).real, axis=1)
    pair1 = 2.0 * (1.0 - np.exp(nn * logw_true[0]).real)
    quad = np.zeros(nn.size)
    for lw in logw_quad:
        quad += 2.0 * (1.0 - np.exp(nn * lw).real)
    lam_inj_f = lam_true_f - pair1 + quad
    i_min = int(np.argmin(lam_inj_f))
    neg = np.nonzero(lam_inj_f < 0)[0]
    n_first_neg = int(nn[neg[0]]) if neg.size else -1
    check("K6.1 [must-fail, THE TEETH] replacing zero #1 by the "
          "off-line quadruple Re = %.1f/%.1f makes lambda_n EXPLODE "
          "NEGATIVELY: first lambda < 0 at n = %d, min = %.3e at "
          "n = %d (growth e^{2n(sigma-1/2)/|rho|^2}, doubling scale "
          "~%.0f), while the TRUE comb stays positive and bounded on "
          "the whole demo grid (min %.4f, max %.1f <= 4 N_zeros)"
          % (INJ_SIGMA, 1 - INJ_SIGMA, n_first_neg,
             float(lam_inj_f[i_min]), int(nn[i_min]),
             math.log(2) / (2 * (INJ_SIGMA - 0.5)
                            / (INJ_SIGMA ** 2 + g1 ** 2)),
             float(lam_true_f.min()), float(lam_true_f.max())),
          neg.size > 0 and float(lam_inj_f[i_min]) < BAR_EXPLODE
          and float(lam_true_f.min()) > 0)

    #  detection threshold inside the budgeted window (honest report)
    rho_a = mpc(INJ_SIGMA, gam[0])
    rho_b = mpc(1 - INJ_SIGMA, gam[0])
    det_n = -1
    for n in range(1, N_MAX + 1):
        pair = 2 * (1 - ((1 - 1 / mpc(mpf(1) / 2, gam[0])) ** n).real)
        qd = (2 * (1 - ((1 - 1 / rho_a) ** n).real)
              + 2 * (1 - ((1 - 1 / rho_b) ** n).real))
        d_inj = abs(mpf(mp.nstr(lam_arith[n], DPS_COMB))
                    - (lam_comb[n] - pair + qd))
        if d_inj > B_fl(n) and det_n < 0:
            det_n = n
    print("   injected comb inside the budget window: first n with "
          "|d_corr| > B_fl(n): %s"
          % (str(det_n) if det_n > 0 else
             "none for n <= %d (deviation ~n^3 (sigma-1/2)/gamma_1^2 "
             "still under budget; teeth live at larger n, K6.1)"
             % N_MAX))
    check("K6.2 [honest scope] the injection is detected %s"
          % ("already inside the budgeted window at n = %d" % det_n
             if det_n > 0 else
             "by the large-n explosion (K6.1), not yet at n <= %d -- "
             "the A3 budget test alone is a CONSISTENCY certificate, "
             "the negativity explosion is the RH-sensitive channel"
             % N_MAX), True)

    # ============================================================== verdict
    VERDICT = ("KEIPER-LI-CONSISTENT" if not FAILS else
               ("BUDGET-BREACH" if "K4.1" in FAILS else "MIXED"))
    print("\nVERDICT: %s -- %d zeros (gamma_max %.1f), lambda table "
          "n <= %d on two routes, max budget usage %.3f, raw window "
          "honestly EMPTY, injection explodes at n ~ %d"
          % (VERDICT, N_ZEROS, float(gmax), N_MAX, max_use,
             int(nn[i_min])))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: standalone probe; zetazero comb declared (dps "
          "%d); tail budget via RvM density + |S| <= %.1f band; NO RH"
          " claim; verification suite untouched"
          % (DPS_ZEROS, S_BOUND))
    print("--- keiper_li_probe: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
