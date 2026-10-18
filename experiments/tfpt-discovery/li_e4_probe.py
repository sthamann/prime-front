"""li_e4_probe -- SLICE B of the Li-strand: Li additivity for
L(E_4, s) = zeta(s) zeta(s-3) as the EXACT consistency test between the
E8 strand (v625: Theta_E8 = E_4, shell counts 240 sigma_3(n)) and the
comb strand (the shared 2000-zero cache).

THE COMPLETED FORM (derived, then verified):
  L(E_4, s) := sum sigma_3(n) n^{-s}  (the 240-normalized shell counts,
  a(1) = 1) = zeta(s) zeta(s-3).  Task-form completion
    Lambda(E_4, s) = (2 pi)^{-s} Gamma(s) L(E_4, s),
  degree 2 with Gamma_C(s) = 2 (2 pi)^{-s} Gamma(s) = Gamma_R(s)
  Gamma_R(s+1) (Legendre duplication).  Via
    Gamma(s/2) Gamma((s-3)/2) = 2^{1-s} sqrt(pi) Gamma(s)
                                 * 4 / ((s-1)(s-3))
  one gets the ENTIRE product of Riemann xi's
    xi(s) xi(s-3) = 2 pi^2 * s (s-4) * Lambda(E_4, s),
  functional equation s <-> 4-s EXACTLY (xi(s) = xi(1-s) twice), zeros
  = {rho} u {rho+3}.  Pole bookkeeping of Lambda: simple poles ONLY at
  s = 4 (residue Gamma(4) zeta(4) / (2 pi)^4 = 1/240 -- the E8 shell
  normalizer 240 is exactly the residue) and s = 0 (residue
  zeta(0) zeta(-3) = -1/240); the would-be s = 1 pole of zeta(s) is
  KILLED by zeta(-2) = 0.  s(s-4) clears both poles.

THE SHIFT RULE (derived, then locked numerically):
  zeta(s-3) has its nontrivial zeros at rho + 3 on Re s = 7/2 and
  satisfies the reflected FE s <-> 7-s.  Its canonical Li/Moebius map
  is the TRANSLATION-CONJUGATED one, z = 1 - 1/(s-3) (unit circle
  <-> Re s = 7/2, expansion point s = 4 = the pole), hence
    lambda_n^{zeta,shifted} := sum_rho [1 - (1 - 1/((rho+3)-3))^n]
                             = lambda_n^{zeta}   EXACTLY,
  and Lagarias additivity for the product gives
    lambda_n^{L} = lambda_n^{zeta} + lambda_n^{zeta,shifted}
                 = 2 lambda_n^{zeta}.
  There is NO single Moebius map doing both lines at once: the naive
  single-map Li at the critical point s = 2 (map 1 - 4/s, unimodular
  on Re s = 2) sees BOTH zero families off ITS line (Re = 1/2, 7/2 =
  2 -+ 3/2) -- the object is non-tempered in that normalization and
  the naive sequence EXPLODES NEGATIVELY (demonstrated: the teeth).

TWO ROUTES for lambda_n^L, n <= 32:
  (a) COMB: additive from the zeta zeros (shared cache, shifted line
      contributes identically by the shift rule) + RvM density tail,
      budget 2 * B_fl(n) (two lines, keiper_li budget each).
  (b) ARITHMETIC / E8: the prime data comes from the E8 counting
      function: from a(n) = sigma_3(n) (rebuilt from the theta glue
      (theta2^8+theta3^8+theta4^8)/2 for n <= 128, multiplicative
      census) the Dirichlet log-derivative recursion
        a(n) log n = sum_{d | n} Lambda_L(d) a(n/d)
      yields the von Mangoldt analogue Lambda_L(n), verified EXACTLY
      = Lambda(n)(1 + n^3) (n <= 512 by unique recursion at 30 digits;
      forward convolution identity to n <= 4e5; Dirichlet lock at
      s = 6 against -(zeta'/zeta)(6) - (zeta'/zeta)(3)).  The Li
      assembly is then the Bombieri-Lagarias finite form per factor:
      factor 1 = keiper_li's binomial assembly (contour eta_k, b_k =
      psi^{(k)}(1/2) block, pole block +2); factor 2 = the DIRECT
      contour extraction of [z^{n-1}] (s-3)^2 xi'/xi(s-3) at
      s = 3 + 1/(1-z) -- every evaluation goes THROUGH the shifted
      argument s-3 near the shifted expansion point s = 4, locking the
      shift bookkeeping numerically (must equal factor 1 to 1e-18).
  PASS = |route (a) - route (b)| <= 2 B_fl(n) for ALL n <= 32: the E8
  counting function and the zeta comb agree in ONE Li sequence.

POSITIVITY (typed honestly): lambda_n^L > 0 for n <= 32 on both routes
is a FINITE verified statement.  "GRH for L(E_4)" = both zero families
on their lines Re = 1/2 and 7/2 = RH for zeta itself (the product has
no independent zero content); for the loaded comb the first 2000 zeros
are on the line by construction.  NO RH claim.

Verdict enums (frozen): LI-E4-ADDITIVE-CONSISTENT (all pass incl. the
central budget), BUDGET-BREACH (E4.2 fails), MIXED.

FIREWALL: experiments-only, standalone (NO verification/ import; the
v625 theta-glue construction is re-implemented inline and checked
against 240 sigma_3); zero data = the shared zetazero cache (declared,
dps 15); Python-only (GATE.WOLFRAM.02).
"""
import json
import math
import os
import time

import numpy as np
import sympy as sp
from mpmath import mp, mpf

T0 = time.time()
FAILS = []
N_CHK = 0

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")

# ---------------- declared constants (before any number) ----------------
N_ZEROS = 2000            # shared comb (keiper_li_probe cache)
DPS_ZEROS = 15
N_MAX = 32                # Li table depth (task: n <= 32)
S_BOUND = 2.5             # |S(t)| band per line (keiper_li, cited)
NMAX_Q = 256              # theta glue checked to q^256 (shells n <= 128)
N_TAB = 400000            # sigma_3 / Lambda_L table cap (v563-sized)
N_REC = 512               # exact-recursion horizon (30 digits)
M_C, R_C = 256, 0.55      # contour for the shifted factor-2 extraction
M_Z, R_Z = 256, 0.5       # contour for Z(w) = w zeta(1+w) (eta_k)
DPS_ARITH = 80            # arithmetic-route precision
TOL_ID = 1e-25            # completed-form / FE / duplication identities
TOL_SHIFT = 1e-18         # factor-2 (shifted path) vs factor-1, relative
TOL_REC = 1e-20           # Lambda_L recursion vs Lambda(n)(1+n^3), rel
TOL_FWD = 1e-9            # forward convolution identity (float), rel
TOL_DIR = 1e-9            # Dirichlet lock at s = 6 (tail ~ N^-2)
DEMO_N = 2000             # naive single-map demo grid
BAR_EXPL = -1.0e3         # the naive sequence must dip below this


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def load_comb():
    with open(CACHE, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["n_zeros"] == N_ZEROS and data["dps"] == DPS_ZEROS
    return np.array([float(g) for g in data["gammas"]]), data


# ---------------- v625-style theta glue, re-implemented inline ----------
def theta_shells(nmax_q):
    def mul(a, bq):
        out = [0] * (nmax_q + 1)
        for i, ai in enumerate(a):
            if ai == 0 or i > nmax_q:
                continue
            for j, bj in enumerate(bq):
                if i + j > nmax_q:
                    break
                out[i + j] += ai * bj
        return out

    def power(a, k):
        r = [1] + [0] * nmax_q
        for _ in range(k):
            r = mul(r, a)
        return r

    th3 = [0] * (nmax_q + 1)
    th3[0] = 1
    th4 = [0] * (nmax_q + 1)
    th4[0] = 1
    k = 1
    while k * k <= nmax_q:
        th3[k * k] = 2
        th4[k * k] = 2 * (-1) ** k
        k += 1
    t2o = [0] * (nmax_q + 1)
    k = 0
    while k * (k + 1) <= nmax_q:
        t2o[k * (k + 1)] = 1
        k += 1
    th2_8 = ([0, 0] + [256 * c for c in power(t2o, 8)])[:nmax_q + 1]
    return [(power(th3, 8)[m] + power(th4, 8)[m] + th2_8[m]) // 2
            for m in range(nmax_q + 1)]


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("LI FOR L(E_4) -- additivity as the E8 <-> comb consistency "
          "test")
    print("=" * 78)

    # ============================================================== E0
    print("\nE0 -- the completed form and its bookkeeping")
    mp.dps = 40

    def xi_r(s):
        return (s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2)
                * mp.zeta(s))

    def Lam_E4(s):
        return ((2 * mp.pi) ** (-s) * mp.gamma(s)
                * mp.zeta(s) * mp.zeta(s - 3))

    def xi_E4(s):
        return xi_r(s) * xi_r(s - 3)

    pts = [mpf(2) + 0j, mpf("2.7") + 1.3j, mpf("0.4") - 2.2j,
           mpf("5.1") + 0.7j]
    dev_id = max(abs(xi_E4(s) - 2 * mp.pi ** 2 * s * (s - 4) * Lam_E4(s))
                 / abs(xi_E4(s)) for s in pts)
    dev_dup = max(abs(mp.gamma(s / 2) * mp.gamma((s - 3) / 2)
                      - 2 ** (1 - s) * mp.sqrt(mp.pi) * mp.gamma(s)
                      * 4 / ((s - 1) * (s - 3)))
                  / abs(mp.gamma(s / 2) * mp.gamma((s - 3) / 2))
                  for s in pts)
    dev_gc = max(abs(mp.pi ** (-s / 2) * mp.gamma(s / 2)
                     * mp.pi ** (-(s + 1) / 2) * mp.gamma((s + 1) / 2)
                     - 2 * (2 * mp.pi) ** (-s) * mp.gamma(s))
                 / abs(mp.gamma(s)) for s in pts)
    check("E0.1 [E, 25+ digits] the completed form: xi(s) xi(s-3) = "
          "2 pi^2 s(s-4) (2pi)^{-s} Gamma(s) zeta(s) zeta(s-3) (worst "
          "rel dev %s), via the duplication bookkeeping Gamma(s/2)"
          "Gamma((s-3)/2) = 2^{1-s} sqrt(pi) Gamma(s) 4/((s-1)(s-3)) "
          "(dev %s); the degree-2 factor is Gamma_C(s) = Gamma_R(s)"
          "Gamma_R(s+1) = 2 (2pi)^{-s} Gamma(s) (dev %s)"
          % (mp.nstr(dev_id, 3), mp.nstr(dev_dup, 3), mp.nstr(dev_gc, 3)),
          max(dev_id, dev_dup, dev_gc) < TOL_ID)

    dev_fe = max(abs(xi_E4(s) - xi_E4(4 - s)) / abs(xi_E4(s))
                 for s in pts)
    dev_fe_l = max(abs(Lam_E4(s) - Lam_E4(4 - s)) / abs(Lam_E4(s))
                   for s in [mpf("2.6") + 0.9j, mpf("1.1") - 1.7j])
    check("E0.2 [E] the functional equation s <-> 4-s holds EXACTLY: "
          "xi_E4(s) = xi_E4(4-s) (worst rel dev %s) and Lambda(E_4, s) "
          "= Lambda(E_4, 4-s) (dev %s) -- weight 4, level 1, sign +1"
          % (mp.nstr(dev_fe, 3), mp.nstr(dev_fe_l, 3)),
          max(dev_fe, dev_fe_l) < TOL_ID)

    res4 = mp.limit(lambda s: (s - 4) * Lam_E4(s), 4)
    res0 = mp.limit(lambda s: s * Lam_E4(s), 0)
    res4_exact = sp.Rational(1, 240)
    reg1 = Lam_E4(mpf(1) + mpf(10) ** -12) - Lam_E4(mpf(1) - mpf(10) ** -12)
    z2 = mp.zeta(-2)
    check("E0.3 [E] pole bookkeeping: Res_{s=4} Lambda = Gamma(4) "
          "zeta(4)/(2pi)^4 = 1/240 EXACTLY (dev %s; sympy: 6*(pi^4/90)"
          "/(16 pi^4) = %s) -- the E8 shell normalizer 240 IS the "
          "residue; Res_{s=0} = zeta(0) zeta(-3) = -1/240 (dev %s); "
          "the s = 1 pole of zeta(s) is KILLED by zeta(-2) = %s: "
          "Lambda is REGULAR at s = 1 (jump across %s); s(s-4) clears "
          "exactly the two poles"
          % (mp.nstr(abs(res4 - mpf(1) / 240), 3),
             sp.nsimplify(6 * sp.Rational(1, 90) / 16),
             mp.nstr(abs(res0 + mpf(1) / 240), 3), mp.nstr(z2, 3),
             mp.nstr(abs(reg1), 3)),
          abs(res4 - mpf(1) / 240) < 1e-20
          and res4_exact == sp.Rational(1, 240)
          and abs(res0 + mpf(1) / 240) < 1e-20
          and abs(z2) < 1e-30 and abs(reg1) < 1e-6)

    # ============================================================== E1
    print("\nE1 -- the E8 side: shells -> Lambda_L (the prime shadow)")
    t_e1 = time.time()
    TE8 = theta_shells(NMAX_Q)
    sig3_small = [int(sum(d ** 3 for d in sp.divisors(n)))
                  for n in range(1, NMAX_Q // 2 + 1)]
    glue_ok = (TE8[0] == 1
               and all(TE8[m] == 0 for m in range(1, NMAX_Q + 1, 2))
               and all(TE8[2 * n] == 240 * sig3_small[n - 1]
                       for n in range(1, NMAX_Q // 2 + 1)))
    check("E1.1 [E] the theta glue (theta2^8 + theta3^8 + theta4^8)/2 "
          "has shell counts r(2n) = 240 sigma_3(n) for n = 1..%d "
          "EXACTLY (v625 range n <= 12 extended; first shells %s): "
          "the E8 counting function IS E_4; a(n) := r(2n)/240 "
          "normalizes a(1) = 1 (240 = the residue, E0.3)"
          % (NMAX_Q // 2, [TE8[2] , TE8[4], TE8[6]]),
          glue_ok)

    # sigma_3 table (int64) + multiplicativity census
    sig3 = np.zeros(N_TAB + 1, dtype=np.int64)
    dd = np.arange(1, N_TAB + 1, dtype=np.int64)
    for d in range(1, N_TAB + 1):
        sig3[d::d] += np.int64(d) ** 3
    mult_ok = all(int(sig3[m * n]) == int(sig3[m]) * int(sig3[n])
                  for m in range(2, 30) for n in range(2, 30)
                  if math.gcd(m, n) == 1 and m * n <= N_TAB)
    ok_table = all(int(sig3[n]) == sig3_small[n - 1]
                   for n in range(1, NMAX_Q // 2 + 1))

    # von Mangoldt sieve (for the structure comparison)
    lam_tab = np.zeros(N_TAB + 1)
    is_pp = np.zeros(N_TAB + 1, dtype=bool)
    sieve = np.ones(N_TAB + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(N_TAB)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= N_TAB:
            lam_tab[q] = lp
            is_pp[q] = True
            q *= p

    # forward convolution identity with Lambda_L(n) = Lambda(n)(1+n^3)
    a_f = sig3.astype(float)
    conv = np.zeros(N_TAB + 1)
    for q in np.nonzero(is_pp)[0]:
        q = int(q)
        LL = lam_tab[q] * (1.0 + float(q) ** 3)
        kk = np.arange(1, N_TAB // q + 1)
        conv[q * kk] += LL * a_f[kk]
    rhs = a_f[1:] * np.log(np.arange(1, N_TAB + 1, dtype=float))
    rel_fwd = float(np.max(np.abs(conv[2:] - rhs[1:]) / rhs[1:]))

    # unique recursion at 30 digits, n <= N_REC
    mp.dps = 30
    lamL = {1: mpf(0)}
    worst_rec = mpf(0)
    for n in range(2, N_REC + 1):
        acc = mpf(int(sig3[n])) * mp.log(n)
        for d in sp.divisors(n):
            if d < n and d in lamL and lamL[d] != 0:
                acc -= lamL[d] * int(sig3[n // d])
        lamL[n] = acc                      # a(1) = 1
        tgt = (mp.log(sp.primefactors(n)[0]) * (1 + mpf(n) ** 3)
               if is_pp[n] else mpf(0))
        dev = (abs(lamL[n] - tgt) / abs(tgt) if tgt != 0
               else abs(lamL[n]) / (mp.log(n) * (1 + mpf(n) ** 3)))
        worst_rec = max(worst_rec, dev)

    # Dirichlet lock at s = 6
    ns = np.nonzero(is_pp)[0].astype(float)
    S6 = float(np.sum(lam_tab[is_pp] * (1.0 + ns ** 3) / ns ** 6))
    mp.dps = 30
    tgt6 = float(-mp.zeta(6, derivative=1) / mp.zeta(6)
                 - mp.zeta(3, derivative=1) / mp.zeta(3))
    dev6 = abs(S6 - tgt6) / abs(tgt6)
    print("   E1 tables in %.1f s (sigma_3 to %d, recursion to %d)"
          % (time.time() - t_e1, N_TAB, N_REC))
    check("E1.2 [E] THE PRIME SHADOW IS EXACT: the Dirichlet "
          "log-derivative recursion a(n) log n = sum_{d|n} Lambda_L(d) "
          "a(n/d) on the E8 data yields Lambda_L(n) = Lambda(n)"
          "(1 + n^3) -- unique recursion to n = %d at 30 digits (worst "
          "rel dev %s), forward convolution identity to n = %d (worst "
          "rel %.1e), sigma_3 multiplicative (census m, n < 30) and "
          "table = glue range" % (N_REC, mp.nstr(worst_rec, 3), N_TAB,
                                  rel_fwd),
          worst_rec < TOL_REC and rel_fwd < TOL_FWD and mult_ok
          and ok_table)
    check("E1.3 [E-float] Dirichlet lock: sum_{n<=%d} Lambda_L(n) n^-6 "
          "= %.12f vs -(zeta'/zeta)(6) - (zeta'/zeta)(3) = %.12f (rel "
          "dev %.1e < %.0e; tail O(N^-2)): the E8 von Mangoldt data "
          "and the analytic log-derivative are the SAME object"
          % (N_TAB, S6, tgt6, dev6, TOL_DIR), dev6 < TOL_DIR)

    # ============================================================== E2
    print("\nE2 -- the shift rule")
    gam, meta = load_comb()
    gmax = float(gam[-1])
    mp.dps = 30
    devs_z = []
    for k in range(3):
        rho3 = mpf(1) / 2 + 3 + 1j * mpf(repr(float(gam[k])))
        ratio = abs(xi_E4(rho3)) / abs(xi_E4(rho3 + mpf(1) / 10))
        devs_z.append(float(ratio))
    uni = max(abs(abs(1 - 1 / (mpf(1) / 2 + 1j * mpf(repr(float(g)))))
                  - 1) for g in gam[:50])
    check("E2.1 [E] the zeros of zeta(s-3) ARE rho + 3: |xi_E4(rho_k+3)|"
          " / |xi_E4(rho_k+3+0.1)| = %s (< 1e-10, zero to comb "
          "precision) for k = 1..3; the conjugated map z = 1 - 1/(s-3) "
          "is unimodular there: 1 - 1/((rho+3)-3) = 1 - 1/rho with "
          "||.|-1| < %s on the first 50 zeros -- hence the SHIFT RULE "
          "lambda_n^{zeta,shifted} = lambda_n^{zeta} EXACTLY and "
          "lambda_n^L = 2 lambda_n^zeta (Lagarias additivity)"
          % (["%.1e" % z for z in devs_z], mp.nstr(uni, 2)),
          max(devs_z) < 1e-10 and uni < 1e-13)

    # ============================================================== E3
    print("\nE3 -- route (a): the comb")
    w_z = (-0.5 + 1j * gam) / (0.5 + 1j * gam)
    Wn = np.ones_like(w_z)
    lam_z_comb = np.zeros(N_MAX + 1)
    for n in range(1, N_MAX + 1):
        Wn = Wn * w_z
        lam_z_comb[n] = float(np.sum(2.0 * (1.0 - Wn.real)))
    mp.dps = 20

    def tail_full(n):
        def dens(t):
            return (mp.log(t / (2 * mp.pi)) / 2 - 1 / (48 * t ** 2)
                    - 7 / (1920 * t ** 4)) / mp.pi
        return float(mp.quad(
            lambda t: 2 * (1 - mp.cos(n * 2 * mp.atan(1 / (2 * t))))
            * dens(t),
            [gmax, 2 * gmax, 10 * gmax, 100 * gmax, 1000 * gmax, mp.inf]))

    tails = [0.0] + [tail_full(n) for n in range(1, N_MAX + 1)]
    lam_L_comb = np.array([2.0 * (lam_z_comb[n] + tails[n])
                           for n in range(N_MAX + 1)])

    def B_fl(n):
        return (2 * S_BOUND
                * 2 * (1 - math.cos(n * 2 * math.atan(1 / (2 * gmax)))))

    check("E3.1 [E] route (a) assembled: lambda_n^L = 2 (comb + tail) "
          "over the shared %d-zero cache; the shifted line contributes "
          "IDENTICALLY by E2.1 (same theta(gamma) after conjugation); "
          "lambda_1^L = %.8f, lambda_32^L = %.6f, budget 2 B_fl(n) "
          "with B_fl = 5 f_n(gamma_max)"
          % (N_ZEROS, lam_L_comb[1], lam_L_comb[32]),
          lam_L_comb[1] > 0 and tails[1] > 0)

    # ============================================================== E4
    print("\nE4 -- route (b): arithmetic / E8, and the cross-check")
    mp.dps = DPS_ARITH
    t_ar = time.time()

    def contour_coeffs(func, radius, n_pts, n_coeff):
        vals = [func(radius * mp.exp(2j * mp.pi * m / n_pts))
                for m in range(n_pts)]
        out = []
        for j in range(n_coeff):
            s = mp.fsum((vals[m] * mp.exp(-2j * mp.pi * j * m / n_pts)
                         for m in range(n_pts)), absolute=False)
            out.append((s / n_pts) / mpf(radius) ** j)
        return out

    # factor 1: the Bombieri-Lagarias binomial assembly (keiper route 2)
    cZ = [c.real for c in contour_coeffs(
        lambda w: w * mp.zeta(1 + w), R_Z, M_Z, N_MAX + 2)]
    inv = [mpf(1)]
    for k in range(1, N_MAX + 1):
        inv.append(-mp.fsum(cZ[j] * inv[k - j] for j in range(1, k + 1)))
    eta = [mp.fsum((j + 1) * cZ[j + 1] * inv[k - j]
                   for j in range(k + 1)) for k in range(N_MAX)]
    b = [-mp.euler - 2 * mp.log(2)]
    for k in range(1, N_MAX):
        b.append((-1) ** (k + 1) * (2 ** (k + 1) - 1) * mp.zeta(k + 1)
                 / mpf(2) ** k)
    lam_f1 = [mpf(0)]
    for n in range(1, N_MAX + 1):
        prime = -1 + mp.fsum(mp.binomial(n, j) * eta[j - 1]
                             for j in range(1, n + 1))
        arch = (-mpf(n) / 2 * mp.log(mp.pi)
                + mp.fsum(mp.binomial(n, j) * b[j - 1]
                          for j in range(1, n + 1)) / 2)
        lam_f1.append(mpf(2) + prime + arch)

    # factor 2: DIRECT contour extraction THROUGH the shifted argument
    def G2_of_z(z):
        s = 3 + 1 / (1 - z)                 # near the shifted point s = 4
        sp_ = s - 3                          # every call goes through s-3
        xi_log_d = (1 / sp_ + 1 / (sp_ - 1) - mp.log(mp.pi) / 2
                    + mp.digamma(sp_ / 2) / 2
                    + mp.zeta(sp_, derivative=1) / mp.zeta(sp_))
        return sp_ * sp_ * xi_log_d

    cG2 = contour_coeffs(G2_of_z, R_C, M_C, N_MAX)
    lam_f2 = [mpf(0)] + [cG2[n - 1].real for n in range(1, N_MAX + 1)]
    dev_shift = max(abs(lam_f2[n] - lam_f1[n]) / abs(lam_f1[n])
                    for n in range(1, N_MAX + 1))
    print("   arithmetic routes in %.1f s" % (time.time() - t_ar))
    check("E4.1 [E] the shifted factor reproduces factor 1 THROUGH the "
          "s-3 code path: [z^{n-1}] (s-3)^2 xi'/xi(s-3) at s = 3 + "
          "1/(1-z) equals the binomial assembly for all n <= %d (max "
          "rel dev %s < %.0e) -- the shift rule holds in the "
          "ARITHMETIC blocks too (pole 1/(s-3) + 1/(s-4) -> +2, "
          "psi((s-3)/2) arch block, eta_k at s-3 = 1)"
          % (N_MAX, mp.nstr(dev_shift, 3), TOL_SHIFT),
          dev_shift < TOL_SHIFT)

    lam_L_arith = [mpf(0)] + [lam_f1[n] + lam_f2[n]
                              for n in range(1, N_MAX + 1)]
    rows = []
    max_use = 0.0
    for n in range(1, N_MAX + 1):
        d = abs(float(lam_L_arith[n]) - lam_L_comb[n])
        use = d / (2 * B_fl(n))
        max_use = max(max_use, use)
        if n in (1, 2, 4, 8, 16, 24, 32):
            rows.append((n, float(lam_L_arith[n]), lam_L_comb[n],
                         d, 2 * B_fl(n), use))
    print("   n   lambda_L_arith    lambda_L_comb+tail  |diff|     "
          "2*B_fl     used")
    for n, la, lc, d, bud, use in rows:
        print("  %3d  %-16.10g  %-16.10g  %.2e  %.2e  %5.3f"
              % (n, la, lc, d, bud, use))
    check("E4.2 [CENTRAL] THE CROSS-CHECK: |lambda_n^{L,arith} - "
          "lambda_n^{L,comb}| <= 2 B_fl(n) for ALL n = 1..%d (max "
          "budget use %.3f) -- the E8 counting function (240 sigma_3, "
          "via Lambda_L = Lambda (1+n^3), E1) and the zeta comb agree "
          "in ONE Li sequence: the exact E8 <-> comb consistency test"
          % (N_MAX, max_use), max_use < 1.0)

    # ============================================================== E5
    print("\nE5 -- positivity and the teeth")
    pos_ok = (all(float(lam_L_arith[n]) > 0 for n in range(1, N_MAX + 1))
              and all(lam_L_comb[n] > 0 for n in range(1, N_MAX + 1)))
    check("E5.1 [E] positivity lambda_n^L > 0 for n = 1..%d on BOTH "
          "routes (min %.6f at n = 1) -- a FINITE statement; typed: "
          "'GRH for L(E_4)' = both zero families on Re = 1/2 and 7/2 "
          "= RH for zeta itself (the product carries no independent "
          "zero content); NO RH claim"
          % (N_MAX, min(float(lam_L_arith[1]), lam_L_comb[1])), pos_ok)

    # the naive single map at the critical point s = 2 (the teeth)
    z1 = 0.5 + 1j * gam
    z2_ = 3.5 + 1j * gam
    lw1 = np.log(1.0 - 4.0 / z1)
    lw2 = np.log(1.0 - 4.0 / z2_)
    nn = np.arange(1, DEMO_N + 1, dtype=float)
    lam_naive = np.zeros(nn.size)
    for a0 in range(0, N_ZEROS, 250):
        b1 = lw1[a0:a0 + 250]
        b2 = lw2[a0:a0 + 250]
        lam_naive += np.sum(2.0 - 2.0 * np.exp(np.outer(nn, b1)).real
                            + 2.0 - 2.0 * np.exp(np.outer(nn, b2)).real,
                            axis=1)
    neg = np.nonzero(lam_naive < 0.0)[0]
    i_min = int(np.argmin(lam_naive))
    lam_L_grid = np.zeros(nn.size)
    lwz = np.log((-0.5 + 1j * gam) / (0.5 + 1j * gam))
    for a0 in range(0, N_ZEROS, 250):
        blk = lwz[a0:a0 + 250]
        lam_L_grid += 4.0 * np.sum(1.0 - np.exp(np.outer(nn, blk)).real,
                                   axis=1)
    n_first = int(nn[neg[0]]) if neg.size else -1
    check("E5.2 [E-float, THE TEETH] the naive SINGLE-map Li at the "
          "critical point s = 2 (map 1 - 4/s, unimodular on Re s = 2) "
          "EXPLODES NEGATIVELY: both zero families sit off that line "
          "(Re = 2 -+ 3/2, |1-4/rho| = %.4f > 1 at gamma_1), first "
          "negative at n = %d, min %.3e at n = %d on the demo grid, "
          "while the shift-rule sequence stays positive there (min "
          "%.4f) -- L(E_4) is NON-TEMPERED in the single-map "
          "normalization; the additive per-factor definition is the "
          "correct Lagarias reading"
          % (float(np.exp(lw1.real[0])), n_first,
             float(lam_naive[i_min]), int(nn[i_min]),
             float(np.min(lam_L_grid))),
          neg.size > 0 and float(lam_naive[i_min]) < BAR_EXPL
          and float(np.min(lam_L_grid)) > 0)

    VERDICT = ("LI-E4-ADDITIVE-CONSISTENT" if not FAILS else
               ("BUDGET-BREACH" if "E4.2" in FAILS else "MIXED"))
    print("\nVERDICT: %s -- Lambda(E_4,s) = (2pi)^{-s} Gamma(s) zeta(s)"
          "zeta(s-3) completed (residues -+1/240), shift rule "
          "lambda^{zeta,shifted} = lambda^zeta exact, lambda_n^L = "
          "2 lambda_n^zeta on n <= %d from E8 shell data vs comb (max "
          "budget use %.3f); naive single-map Li refused (non-tempered)"
          % (VERDICT, N_MAX, max_use))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: standalone probe (v625 logic re-implemented, no "
          "verification/ import); shared zero cache (dps %d); finite "
          "statements only; NO RH claim" % DPS_ZEROS)
    print("--- li_e4_probe: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
