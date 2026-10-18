"""v672 -- PRIME.LICOROLLARY.01: SLICE A of the Li-strand -- the
W1 => Li corollary SPELLED OUT.  The scan thesis was: "W1 probably
already implies finite Li positivity for the test functions spanned
by our windows."  This module makes that precise and measures it on
the LARGEST complete frame-A window (h = 1433, the v563/v648
surface).

THE g_n DERIVATION (u = log x picture, documented and verified):
  Bombieri-Lagarias write lambda_n = sum_rho [1 - (1 - 1/rho)^n]; their
  h_n(x) polynomials arise from the Moebius map s = 1/(1-z).  Expanding
    1 - (1 - 1/rho)^n = sum_{k=1}^n binom(n,k) (-1)^{k+1} rho^{-k}
  and using rho^{-k} = int_{-inf}^0 e^{u/2} (-u)^{k-1}/(k-1)! e^{i g u} du
  (rho = 1/2 + i gamma) gives, after even symmetrization over the
  conjugate zero pairs, the EXPLICIT Weil test function
    g_n(u) = (1/2) e^{-|u|/2} L^{(1)}_{n-1}(|u|)
  (generalized Laguerre, alpha = 1; in x = e^u this is the classical
  (1/2) x^{-1/2} h_n(log x) form), with Fourier transform
    ghat_n(gamma) = 1 - cos(n theta(gamma)),  theta = 2 arctan(1/(2 gamma))
  and lambda_n = sum_rho ghat_n(gamma_rho).  CRUCIALLY
    g_n = (1/2) G_n * ~G_n   (autocorrelation),
    G_n(u) = e^{u/2} L^{(1)}_{n-1}(-u) 1_{u<0},
  because |1 - 1/rho| = 1 identically on Re rho = 1/2, so
  ghat_n = (1/2)|Ghat_n|^2 = 2 sin^2(n theta/2) >= 0: the Li functional
  is a QUADRATIC-FORM value of the Weil form at the GENERATOR G_n.
  The window frame therefore has to approximate the generator (support
  [-atil, atil]), not g_n itself (whose autocorrelation support would
  be [-2 atil, 2 atil]); G_n has INFINITE support, so the honest
  question is approximation, never membership.

PARITY SPLIT (exact at zero level): with Ge/Go the even/odd parts of
  G_n, the cross term vanishes pointwise on the line, so
    lambda_n = lambda_n^odd + lambda_n^even,
    lambda_n^odd  = sum_{gamma>0} (Im Ghat_n)^2 = sum sin^2(n theta),
    lambda_n^even = sum_{gamma>0} (1 - cos(n theta))^2.
  The v648 positivity datum lives on the ODD parity sector; the even
  sector is measured here, not previously certified.

THE POLE BLOCK AND THE POLE-FREE HYPERPLANE: for a window function
  phi_V the explicit formula reads (locked numerically in L3)
    sum_{gamma>0} |phihat_V(gamma)|^2  =  -+ c_+^2  +  D v^T A_par v,
  c_+ = int phi_V e^{x/2} (minus sign on the odd fold, plus on the
  even), A_par = parity-folded Toeplitz(c_ar + c_at) = the v563 window
  matrix, D = lattice pitch (the w1 one-scalar dictionary).  For the
  Li generators c_+^2 is HUGE (e^{x/2} against the truncated Laguerre
  tail), so the corollary is stated on the pole-free hyperplane
  {c_+ = 0}: killing c_+ costs almost nothing in L^2 (the L^2 mass of
  e^{x/2} on the window is ~e^{2 alpha}), and there
    Q_win(v) = D v^T A v >= D lambda_min(A, G) ||v||_G^2 > 0
  is CERTIFIED by the v648-type datum lambda_min > 0.

WHAT IS CHECKED:
  L0  comb integrity (shared zero cache, 2000 zeros, dps 15).
  L1  the g_n derivation: Laguerre closed form (sympy), Fourier pair
      (mpmath quad, 20+ digits), autocorrelation identity (quad).
  L2  reference lambda_n table n <= 32 on two routes: comb + density
      tail vs the zero-free Bombieri-Lagarias binomial assembly
      (contour eta_k, psi(1/2) block, pole block +2), budget
      B_fl(n) = 2 * 2.5 * f_n(gamma_max) as in keiper_li_probe.
  L3  the explicit-formula LOCK on the h = 1433 window: for parity
      test vectors the comb read equals -+c_+^2 + D v^T A v (pole term
      verified sign-correctly on both parities, corrected vectors need
      none) -- this is the operational W1 => Li bridge.
  L4  CENTRAL: the approximation table.  P = L2 (Gram) projection onto
      the window frame, then the G-orthogonal pole-free correction;
      form error err(n) = |lambda_n - Q_win(P g_n)| / lambda_n; the
      band {n <= 32 : err < 10%} is reported (task bar).  HONEST MISS
      built in: every Li generator carries a JUMP at u = 0 (|Ghat| ~
      1/gamma is forced because a fixed share of lambda_n lives at
      high gamma); the frame resolves it at pitch D, which floors the
      form error at the few-percent level and breaks n = 1 (small
      denominator, artifact components adding instead of canceling).
  L5  the corollary on the band: Q_win^odd >= D lambda_min^constr
      ||v||_G^2 > 0 numerically -- "the verified window positivity
      contains these Li coefficients" (odd part certified; even part
      + measured lambda_min^even documented honestly).
  L6  [C] typing: a FINITE statement about the band coefficients of
      a 2000-zero comb and one declared window; NO RH statement.

Verdict enums (frozen): LI-COROLLARY-FINITE (all pass, N_eff >= 1),
FORM-MISMATCH (L3/L4 structure fails), MIXED.

FIREWALL: v563 imported READ-ONLY; zero data = the shared committed
zetazero cache (experiments/tfpt-discovery/zero_comb_cache_n2000.json,
dps 15; completeness certified by v666_turing_cert.py; diagnostic
zero-side line, v589 convention); finite statements only, NO RH
claim; Python-only (GATE.WOLFRAM.02).

PROVENANCE: discovery probe li_corollary_probe.py (2026-08-02, 11/11,
verdict LI-COROLLARY-FINITE); keiper_li_probe / v665 (the
Bombieri-Lagarias binomial assembly + tail budget), v648 (the odd-
sector positivity datum), v563 (window matrices), v643 (the W1
one-scalar dictionary), Bombieri-Lagarias J. Number Theory 77 (1999).
"""
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import sympy as sp  # noqa: E402
from mpmath import mp, mpf, mpc  # noqa: E402

T0 = time.time()
FAILS = []
N_CHK = 0

HERE = _here
# shared zero-comb cache: committed in experiments/tfpt-discovery/
# (repo tree); fall back to a local copy next to this module (website
# mirror / standalone use).
_REPO_CACHE = os.path.join(os.path.dirname(HERE), "experiments",
                           "tfpt-discovery",
                           "zero_comb_cache_n2000.json")
_LOCAL_CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")
CACHE = _REPO_CACHE if os.path.exists(_REPO_CACHE) else _LOCAL_CACHE

# ---------------- declared constants (before any number) ----------------
N_ZEROS = 2000            # the shared comb (keiper_li_probe cache)
DPS_ZEROS = 15
N_MAX = 32                # lambda table depth (declared, cost cap)
H_TARGET = 1433           # the LARGEST complete-comb frame-A window
S_BOUND = 2.5             # |S(t)| band (keiper_li_probe, cited)
M_Z, R_Z = 256, 0.5       # contour for Z(w) = (s-1) zeta(1+w)
DPS_ARITH = 80            # route-2 precision (0.31*32 ~ 10 digits lost)
TOL_DERIV = 1e-20         # L1 Fourier/autocorrelation identities (abs)
TOL_CLOSED = 1e-25        # lambda_1/lambda_2 closed forms (abs)
BAR_LOCK = 2.5e-2         # L3 lock bar: the tent dictionary carries a
#                           (gamma D)^2/12 discretization error at the
#                           lock frequencies (~2e-3 at gamma ~ 38), the
#                           atom re-binning roughly doubles it; typed
BAR_FORM = 0.10           # the task bar: form error < 10% (relative)
N_LOCK_VEC = 3            # parity lock vectors
N_MODES = 16              # parity modes for the lock vectors
SEED = 20260802
FLOOR_SAFETY = 20.0       # v648 eigh backward-error safety factor
EPS = float(np.finfo(float).eps)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# ---------------- shared comb ----------------
def load_comb():
    with open(CACHE, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    assert data["n_zeros"] == N_ZEROS and data["dps"] == DPS_ZEROS
    return np.array([float(g) for g in data["gammas"]]), data


def theta_prime(t):
    return (math.log(t / (2 * math.pi)) / 2 - 1 / (48 * t ** 2)
            - 7 / (1920 * t ** 4))


def theta_of(t):
    return 2.0 * np.arctan(1.0 / (2.0 * t))


# ---------------- Laguerre L^{(1)}_{n-1} on arrays, recurrence ----------
def laguerre1_rows(t, nmax):
    """rows[m] = L^{(1)}_m(t) for m = 0..nmax-1 (alpha = 1)."""
    t = np.asarray(t, dtype=float)
    rows = np.empty((nmax, t.size))
    rows[0] = 1.0
    if nmax > 1:
        rows[1] = 2.0 - t
    for m in range(2, nmax):
        rows[m] = ((2 * m + 1 - 2 - t + 1) * rows[m - 1]
                   - (m - 1 + 1) * rows[m - 2]) / m
        # standard: m L_m^(a) = (2m-1+a-t) L_{m-1}^(a) - (m-1+a) L_{m-2}^(a)
    return rows


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("LI COROLLARY PROBE -- W1 window positivity vs the first Li "
          "coefficients")
    print("=" * 78)

    # ============================================================== L0
    print("\nL0 -- the shared comb")
    gam, meta = load_comb()
    gmax = float(gam[-1])
    check("L0.1 comb integrity: %d zeros (%s, dps %d), gamma_1 = %.9f, "
          "gamma_max = %.3f, strictly increasing"
          % (N_ZEROS, meta["generator"], DPS_ZEROS, gam[0], gmax),
          gam.size == N_ZEROS and np.all(np.diff(gam) > 0)
          and abs(gam[0] - 14.134725141734693) < 1e-9)

    # ============================================================== L1
    print("\nL1 -- the g_n derivation (u = log x picture)")
    tt_s = sp.symbols("tt_s", nonnegative=True)
    dev_lag = 0
    for n in (1, 2, 3, 5, 8):
        Pn = sum(sp.binomial(n, k) * (-1) ** (k + 1)
                 * tt_s ** (k - 1) / sp.factorial(k - 1)
                 for k in range(1, n + 1))
        dev_lag = max(dev_lag,
                      0 if sp.simplify(
                          Pn - sp.assoc_laguerre(n - 1, 1, tt_s)) == 0
                      else 1)
    th_s, = sp.symbols("th_s", real=True),
    trig_ok = sp.simplify(sp.Abs(1 - sp.exp(sp.I * th_s)) ** 2
                          - 2 * (1 - sp.cos(th_s))) == 0
    check("L1.1 [E] closed form: sum_k binom(n,k)(-1)^{k+1} t^{k-1}/(k-1)!"
          " = L^{(1)}_{n-1}(t) for n = 1,2,3,5,8 (sympy exact) and "
          "|1 - e^{i n theta}|^2 = 2(1 - cos n theta): ghat_n = "
          "(1/2)|Ghat_n|^2 >= 0 -- g_n IS an autocorrelation",
          dev_lag == 0 and trig_ok)

    mp.dps = 30

    def G_mp(u, n):
        # generator G_n(u) = e^{u/2} L^{(1)}_{n-1}(-u), u < 0
        if u >= 0:
            return mp.mpf(0)
        return mp.exp(u / 2) * mp.laguerre(n - 1, 1, -u)

    def g_mp(u, n):
        return mp.exp(-abs(u) / 2) * mp.laguerre(n - 1, 1, abs(u)) / 2

    # (a) the algebraic core of the derivation, 25+ digits: the binomial
    #     expansion of 1 - (1 - 1/rho)^n equals 1 - cos(n theta) on the
    #     line (this IS the Fourier transform by the term-by-term pair
    #     rho^{-k} <-> e^{u/2} (-u)^{k-1}/(k-1)! 1_{u<0}); dps 50: the
    #     binomial sum loses ~10 digits to cancellation at n = 32
    mp.dps = 50
    devs_alg = []
    for n in (1, 3, 8, 32):
        for gv in (mpf("0.7"), mpf("14.134725141734693"), mpf(300)):
            rho = mpf(1) / 2 + 1j * gv
            binom_sum = mp.re(mp.fsum(
                mp.binomial(n, k) * (-1) ** (k + 1) * rho ** (-k)
                for k in range(1, n + 1)))
            th = 2 * mp.atan(1 / (2 * gv))
            devs_alg.append(abs(binom_sum - (1 - mp.cos(n * th))))
    # (b) direct quadrature of the Fourier pair at non-oscillatory gamma
    mp.dps = 30
    devs_ft = []
    for n, gv in ((1, mpf("0.7")), (3, mpf("0.7"))):
        ft = 2 * mp.quad(lambda u: g_mp(u, n) * mp.cos(gv * u),
                         [0, 5, 20, 60, mp.inf])
        th = 2 * mp.atan(1 / (2 * gv))
        devs_ft.append(abs(ft - (1 - mp.cos(n * th))))
    devs_ac = []
    for n, u0 in ((2, mpf("0.3")), (5, mpf("2.0"))):
        ac = mp.quad(lambda t: G_mp(t, n) * G_mp(t - u0, n),
                     [-mp.inf, -40, -10, 0]) / 2
        devs_ac.append(abs(ac - g_mp(u0, n)))
    check("L1.2 [E, 25+ digits] the derivation is exact: the binomial "
          "form Re sum_k binom(n,k)(-1)^{k+1} rho^{-k} equals "
          "1 - cos(n theta(gamma)) on the line for n = 1, 3, 8, 32 at "
          "gamma = 0.7, gamma_1, 300 (worst dev %s); the Fourier pair "
          "verifies by quadrature at gamma = 0.7 (worst dev %s) and "
          "g_n(u0) = (1/2)(G_n star ~G_n)(u0) at (2, .3), (5, 2.0) "
          "(worst dev %s)"
          % (mp.nstr(max(devs_alg), 3), mp.nstr(max(devs_ft), 3),
             mp.nstr(max(devs_ac), 3)),
          max(devs_alg) < TOL_CLOSED and max(devs_ft) < TOL_DERIV
          and max(devs_ac) < TOL_DERIV)

    # ============================================================== L2
    print("\nL2 -- reference lambda table, two routes, n <= %d" % N_MAX)
    # route 1: comb, closed per-zero values
    w_z = (-0.5 + 1j * gam) / (0.5 + 1j * gam)     # e^{i theta(gamma)}
    Wn = np.ones_like(w_z)
    lam_odd_c = np.zeros(N_MAX + 1)
    lam_even_c = np.zeros(N_MAX + 1)
    for n in range(1, N_MAX + 1):
        Wn = Wn * w_z
        lam_odd_c[n] = float(np.sum(Wn.imag ** 2))
        lam_even_c[n] = float(np.sum((1.0 - Wn.real) ** 2))
    lam_full_c = lam_odd_c + lam_even_c

    # density tails (RvM density, zero-free)
    mp.dps = 20

    def tail_pair(n):
        def th_t(t):
            return 2 * mp.atan(1 / (2 * t))

        def dens(t):
            return (mp.log(t / (2 * mp.pi)) / 2 - 1 / (48 * t ** 2)
                    - 7 / (1920 * t ** 4)) / mp.pi
        pts = [gmax, 2 * gmax, 10 * gmax, 100 * gmax, 1000 * gmax, mp.inf]
        t_o = mp.quad(lambda t: mp.sin(n * th_t(t)) ** 2 * dens(t), pts)
        t_e = mp.quad(lambda t: (1 - mp.cos(n * th_t(t))) ** 2 * dens(t),
                      pts)
        return float(t_o), float(t_e)

    t_lam = time.time()
    tails_o = [0.0]
    tails_e = [0.0]
    for n in range(1, N_MAX + 1):
        a, b = tail_pair(n)
        tails_o.append(a)
        tails_e.append(b)
    lam_odd = np.array([lam_odd_c[n] + tails_o[n]
                        for n in range(N_MAX + 1)])
    lam_even = np.array([lam_even_c[n] + tails_e[n]
                         for n in range(N_MAX + 1)])
    lam_ref = lam_odd + lam_even
    print("   comb + %d tail pairs in %.1f s" % (N_MAX,
                                                 time.time() - t_lam))

    def B_fl(n):
        return (2 * S_BOUND
                * 2 * (1 - math.cos(n * 2 * math.atan(1 / (2 * gmax)))))

    # route 2: zero-free Bombieri-Lagarias binomial assembly
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
    lam_arith = [mpf(0)]
    for n in range(1, N_MAX + 1):
        prime = -1 + mp.fsum(mp.binomial(n, j) * eta[j - 1]
                             for j in range(1, n + 1))
        arch = (-mpf(n) / 2 * mp.log(mp.pi)
                + mp.fsum(mp.binomial(n, j) * b[j - 1]
                          for j in range(1, n + 1)) / 2)
        lam_arith.append(mpf(2) + prime + arch)
    lam1_closed = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    lam2_closed = (1 + mp.euler - mp.euler ** 2 - 2 * mp.stieltjes(1)
                   - mp.log(4 * mp.pi) + mp.pi ** 2 / 8)
    dev_cl = max(abs(lam_arith[1] - lam1_closed),
                 abs(lam_arith[2] - lam2_closed))
    print("   arithmetic route in %.1f s" % (time.time() - t_ar))
    check("L2.1 [E] zero-free route reproduces the closed forms: "
          "lambda_1 = %s, lambda_2 = %s (worst dev %s < %.0e)"
          % (mp.nstr(lam1_closed, 10), mp.nstr(lam2_closed, 10),
             mp.nstr(dev_cl, 3), TOL_CLOSED), dev_cl < TOL_CLOSED)
    ref_dev = [abs(float(lam_arith[n]) - lam_ref[n]) / B_fl(n)
               for n in range(1, N_MAX + 1)]
    check("L2.2 [E] REFERENCE LOCK: |lambda_arith - (comb + tail)| <= "
          "B_fl(n) = 5 f_n(gamma_max) for ALL n <= %d (max budget use "
          "%.3f); positivity lambda_n > 0 and both parity parts >= 0 "
          "on the whole range (parts are sums of squares) -- finite "
          "statement" % (N_MAX, max(ref_dev)),
          max(ref_dev) < 1.0 and all(lam_ref[1:] > 0))

    # ============================================================== L3
    print("\nL3 -- the h = %d window and the explicit-formula lock"
          % H_TARGET)
    t_w = time.time()
    kz_pick = None
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        if Mz // 2 == H_TARGET:
            kz_pick = kz
            break
    assert kz_pick is not None, "h = %d window not found" % H_TARGET
    alpha = float(core.U_ALL[kz_pick])
    Mz = 2 * H_TARGET
    hz = H_TARGET
    ka = core.atoms_in(alpha)
    c_at, D = core.atom_lags_at(alpha, Mz, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    c_ar = core.arch_lags(Mz, D)
    c_all = c_ar + c_at
    atil = alpha + D / 2.0
    X_cap = math.exp(2.0 * alpha)
    complete = X_cap <= core.ATOM_MAX + 0.5
    pj = (np.arange(Mz) - (Mz - 1) / 2.0) * D
    print("   window: h = %d, alpha = %.6f, D = %.6e, atil = %.6f, "
          "atoms = %d, X = %.4g (complete comb: %s), built in %.1f s"
          % (hz, alpha, D, atil, ka, X_cap, complete, time.time() - t_w))

    def parity_toeplitz(c, M, sign):
        h = M // 2
        rr = np.arange(h)
        return (np.asarray(c)[np.abs(rr[:, None] - rr[None, :])]
                + sign * np.asarray(c)[(M - 1) - rr[:, None] - rr[None, :]])

    A_odd = parity_toeplitz(c_all, Mz, -1.0)
    A_even = parity_toeplitz(c_all, Mz, +1.0)
    g_lag = np.zeros(Mz)
    g_lag[0], g_lag[1] = 2.0 * D / 3.0, D / 6.0
    G_odd = parity_toeplitz(g_lag, Mz, -1.0)
    G_even = parity_toeplitz(g_lag, Mz, +1.0)

    # pole weight: c_+ = sum_j V_j kap e^{p_j/2},  kap = int tent e^{s/2}
    s_s, D_s = sp.symbols("s_s D_s", positive=True)
    kap_sym = 2 * sp.integrate((1 - s_s / D_s) * sp.cosh(s_s / 2),
                               (s_s, 0, D_s))
    kap = float(kap_sym.subs(D_s, sp.Float(D, 30)))
    w_pole = kap * np.exp(pj / 2.0)
    r_odd = w_pole[:hz] - w_pole[::-1][:hz]
    r_even = w_pole[:hz] + w_pole[::-1][:hz]

    def gen_min_eig(A, G):
        w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
        rad = max(abs(float(w[0])), abs(float(w[-1])))
        return float(w[0]), V[:, 0], rad

    def constrained_min_eig(A, G, r):
        u = r / np.linalg.norm(r)
        u = u.copy()
        u[0] += math.copysign(1.0, u[0] if u[0] != 0 else 1.0)
        u /= np.linalg.norm(u)          # Householder: H r ~ e_0

        def H_conj(Mx):
            Mx = Mx - 2.0 * np.outer(Mx @ u, u)
            Mx = Mx - 2.0 * np.outer(u, u @ Mx)
            return Mx
        Ah = H_conj(A)[1:, 1:]
        Gh = H_conj(G)[1:, 1:]
        w = sla.eigh(0.5 * (Ah + Ah.T), 0.5 * (Gh + Gh.T),
                     eigvals_only=True, subset_by_index=[0, 0])
        return float(w[0])

    lam_min_o, _, rad_o = gen_min_eig(A_odd, G_odd)
    lam_min_e, _, rad_e = gen_min_eig(A_even, G_even)
    floor_o = FLOOR_SAFETY * EPS * rad_o * math.sqrt(hz)
    lam_min_oc = constrained_min_eig(A_odd, G_odd, r_odd)
    lam_min_ec = constrained_min_eig(A_even, G_even, r_even)
    print("   pencil lambda_min: odd %+.4e (floor %.1e), even %+.4e; "
          "pole-free hyperplane: odd %+.4e, even %+.4e"
          % (lam_min_o, floor_o, lam_min_e, lam_min_oc, lam_min_ec))
    check("L3.1 [E] the v648-type positivity datum reproduces on h = %d:"
          " odd-sector lambda_min(A, G) = %+.4e > floor %.1e (v648: "
          "min over the 67 complete windows +8.26e-4); NEW MEASUREMENT:"
          " even-sector lambda_min = %+.4e, pole-free-hyperplane values"
          " odd %+.4e / even %+.4e"
          % (hz, lam_min_o, floor_o, lam_min_e, lam_min_oc, lam_min_ec),
          complete and lam_min_o > floor_o)

    # phase matrices for the comb reads of window functions
    t_ph = time.time()
    SINM = np.sin(np.outer(gam, pj))
    COSM = np.cos(np.outer(gam, pj))
    x_h = gam * (D / 2.0)
    hat_ft = D * np.sinc(x_h / math.pi) ** 2
    print("   phase matrices %d x %d in %.1f s"
          % (N_ZEROS, Mz, time.time() - t_ph))

    def comb_read(V, parity):
        proj = (SINM @ V) if parity == "odd" else (COSM @ V)
        return float(np.sum((hat_ft * proj) ** 2))

    def tail_bound(V):
        # |phihat|^2 <= (sum|V|)^2 D^2 (2/(tD))^4 beyond the comb
        s1 = float(np.sum(np.abs(V))) ** 2
        integ = mp.quad(lambda t: (mp.log(t / (2 * mp.pi)) / 2) / mp.pi
                        / t ** 4, [gmax, 10 * gmax, mp.inf])
        return s1 * D ** 2 * (2.0 / D) ** 4 * float(integ)

    rng = np.random.default_rng(SEED)
    chol_Go = sla.cho_factor(G_odd)
    chol_Ge = sla.cho_factor(G_even)
    Gr_o = sla.cho_solve(chol_Go, r_odd)
    Gr_e = sla.cho_solve(chol_Ge, r_even)
    rGr_o = float(r_odd @ Gr_o)
    rGr_e = float(r_even @ Gr_e)

    # lock vectors MUST carry spectral mass at the zeros: parity mode k
    # sits at gamma ~ pi k / atil, so modes 60..75 cover gamma ~ 30..38
    # (inside the comb); a LOW-mode vector (k <= 16, gamma < 8, i.e.
    # BELOW gamma_1) is kept as the pole-cancellation exhibit.
    K_HI_LO, K_HI_N = 60, 16
    T_hi = core.parity_basis(hz, K_HI_LO + K_HI_N)[K_HI_LO:]
    T_lo = core.parity_basis(hz, N_MODES)

    rows_lock = []
    for iv in range(N_LOCK_VEC):
        cf = rng.standard_normal(K_HI_N) / np.arange(1, K_HI_N + 1)
        v = cf @ T_hi
        V = np.concatenate([v, -v[::-1]])
        cplus = float(v @ r_odd)
        q_comb = comb_read(V, "odd")
        q_win = D * float(v @ (A_odd @ v)) - cplus ** 2
        vc = v - (cplus / rGr_o) * Gr_o
        Vc = np.concatenate([vc, -vc[::-1]])
        q_comb_c = comb_read(Vc, "odd")
        q_win_c = D * float(vc @ (A_odd @ vc))
        rows_lock.append((abs(q_win - q_comb) / abs(q_comb),
                          abs(q_win_c - q_comb_c) / abs(q_comb_c),
                          cplus ** 2, q_comb, tail_bound(V)))
    # one even-sector high-mode lock vector
    cf = rng.standard_normal(K_HI_N) / np.arange(1, K_HI_N + 1)
    ve = cf @ T_hi
    Ve = np.concatenate([ve, ve[::-1]])
    cplus_e = float(ve @ r_even)
    q_comb_e = comb_read(Ve, "even")
    q_win_e = D * float(ve @ (A_even @ ve)) + cplus_e ** 2
    dev_even = abs(q_win_e - q_comb_e) / abs(q_comb_e)
    worst_unc = max(z[0] for z in rows_lock)
    worst_cor = max(z[1] for z in rows_lock)
    print("   lock rows (odd, modes %d..%d): rel dev %s | pole-free %s |"
          " c_+^2 %s | Q_comb %s"
          % (K_HI_LO + 1, K_HI_LO + K_HI_N,
             ["%.1e" % z[0] for z in rows_lock],
             ["%.1e" % z[1] for z in rows_lock],
             ["%.2e" % z[2] for z in rows_lock],
             ["%.2e" % z[3] for z in rows_lock]))
    gam_hi = math.pi * (K_HI_LO + K_HI_N) / atil
    disc_scale = (gam_hi * D) ** 2 / 12.0
    check("L3.2 [E, THE LOCK] the explicit formula holds on the window: "
          "sum_{gamma>0}|phihat|^2 = -c_+^2 + D v^T A_odd v on %d "
          "high-mode odd parity vectors (worst rel dev %.1e) and "
          "= +c_+^2 + D v A_even v on the even fold (dev %.1e); on the "
          "pole-free hyperplane the pole term is exactly absent (worst "
          "dev %.1e); the residual IS the typed tent-dictionary "
          "discretization scale (gamma D)^2/12 = %.1e at gamma ~ %.0f "
          "(bar %.0e)"
          % (N_LOCK_VEC, worst_unc, dev_even, worst_cor, disc_scale,
             gam_hi, BAR_LOCK),
          worst_unc < BAR_LOCK and dev_even < BAR_LOCK
          and worst_cor < BAR_LOCK)

    # the pole-cancellation exhibit: a low-mode vector (all spectral
    # mass BELOW gamma_1) has near-zero zero-side value, so the window
    # form must cancel the pole term to high accuracy
    cf = rng.standard_normal(N_MODES) / np.arange(1, N_MODES + 1)
    vl = cf @ T_lo
    Vl = np.concatenate([vl, -vl[::-1]])
    cp_l = float(vl @ r_odd)
    q_form_l = D * float(vl @ (A_odd @ vl))
    q_comb_l = comb_read(Vl, "odd")
    canc = abs(q_form_l - cp_l ** 2 - q_comb_l) / cp_l ** 2
    check("L3.3 [E] the pole-cancellation exhibit: for a LOW-mode odd "
          "vector (spectral mass below gamma_1) the zero side is "
          "near-empty (Q_comb = %.2e) and the window form cancels the "
          "pole term to %d digits: |D v A v - c_+^2 - Q_comb| / c_+^2 "
          "= %.1e (D v A v = %.6f vs c_+^2 = %.6f) -- the rank-2 pole "
          "block is EXACTLY the piece of the Weil form that the "
          "positivity certificate must exclude"
          % (q_comb_l, int(-math.log10(max(canc, 1e-300))), canc,
             q_form_l, cp_l ** 2), canc < 1e-5)

    # ============================================================== L4
    print("\nL4 -- CENTRAL: L2 projection table, N_eff at the %.0f%% bar"
          % (100 * BAR_FORM))
    # P = the G-orthogonal (L2) projection onto the hat frame: solve
    # G v = b with b_j = <G_n parity part, hat_j>, Gauss cells split at
    # the u = 0 jump of the generator.
    from numpy.polynomial.legendre import leggauss
    GX8, GW8 = leggauss(8)
    pts_l, wts_l, jid_l = [], [], []
    for j in range(hz):
        p = pj[j]
        for a, c in ((p - D, p), (p, p + D)):
            subs = (a, c) if not a < 0.0 < c else (a, 0.0, c)
            for lo, hi in zip(subs[:-1], subs[1:]):
                mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
                x = mid + half * GX8
                pts_l.append(x)
                wts_l.append(half * GW8 * (1.0 - np.abs(x - p) / D))
                jid_l.append(np.full(8, j, dtype=np.int64))
    pts = np.concatenate(pts_l)
    wts = np.concatenate(wts_l)
    jid = np.concatenate(jid_l)
    absu = np.abs(pts)
    Lrows = laguerre1_rows(absu, N_MAX)
    Gm = np.exp(-absu / 2.0) * Lrows          # G_n(-|u|), rows n-1
    sgn_o = np.where(pts < 0.0, 0.5, -0.5)    # Go = +-G(-|u|)/2
    q_odd_win = np.zeros(N_MAX + 1)
    q_even_win = np.zeros(N_MAX + 1)
    q_comb_o = np.zeros(N_MAX + 1)
    cert_lo = np.zeros(N_MAX + 1)
    cp_kill = np.zeros(N_MAX + 1)
    for n in range(1, N_MAX + 1):
        b_o = np.bincount(jid, weights=wts * sgn_o * Gm[n - 1],
                          minlength=hz)
        b_e = np.bincount(jid, weights=wts * 0.5 * Gm[n - 1],
                          minlength=hz)
        v_o = sla.cho_solve(chol_Go, b_o)
        v_e = sla.cho_solve(chol_Ge, b_e)
        cp_o = float(v_o @ r_odd)
        cp_e = float(v_e @ r_even)
        vco = v_o - (cp_o / rGr_o) * Gr_o
        vce = v_e - (cp_e / rGr_e) * Gr_e
        q_odd_win[n] = D * float(vco @ (A_odd @ vco))
        q_even_win[n] = D * float(vce @ (A_even @ vce))
        q_comb_o[n] = comb_read(np.concatenate([vco, -vco[::-1]]), "odd")
        cert_lo[n] = D * lam_min_oc * float(vco @ (G_odd @ vco))
        cp_kill[n] = (cp_o ** 2 / rGr_o) / max(float(v_o @ (G_odd @ v_o)),
                                               1e-300)
    q_tot_win = q_odd_win + q_even_win
    print("   n   lambda_n     lam_odd      lam_even     Q_win_odd    "
          "Q_comb_odd   Q_win_even   err_odd  err_tot  cert_floor")
    err_tot = np.zeros(N_MAX + 1)
    for n in range(1, N_MAX + 1):
        e_o = abs(q_odd_win[n] - lam_odd[n]) / lam_ref[n]
        err_tot[n] = abs(q_tot_win[n] - lam_ref[n]) / lam_ref[n]
        print("  %3d  %-11.6g  %-11.6g  %-11.6g  %-11.6g  %-11.6g  "
              "%-11.6g  %7.4f  %7.4f  %.2e"
              % (n, lam_ref[n], lam_odd[n], lam_even[n], q_odd_win[n],
                 q_comb_o[n], q_even_win[n], e_o, err_tot[n],
                 cert_lo[n]))
    s_eff = [n for n in range(1, N_MAX + 1) if err_tot[n] < BAR_FORM]
    n_eff = len(s_eff)
    runs = []
    for n in s_eff:
        if runs and n == runs[-1][1] + 1:
            runs[-1][1] = n
        else:
            runs.append([n, n])
    band = " u ".join("%d..%d" % (a, c) if a != c else "%d" % a
                      for a, c in runs)
    # the n = 1 diagnosis: every Li generator carries a JUMP at u = 0
    # (|Ghat| ~ 1/gamma is forced: a fixed share of lambda_n lives at
    # high gamma), the frame resolves it at pitch D; the two ~10%
    # artifact components (in-band projection excess, beyond-comb alias
    # mass of the resolved jump) ADD at n = 1 and partially cancel for
    # n >= 2 -- quantified by the Q_comb_odd column
    e1_proj = (q_comb_o[1] - lam_odd_c[1]) / lam_ref[1]
    e1_alias = (q_odd_win[1] - q_comb_o[1] - tails_o[1]) / lam_ref[1]
    check("L4.1 [MEASURED, CENTRAL] the approximation table: L2 (Gram) "
          "projection + pole-free correction on h = %d reproduces "
          "lambda_n with form error < %.0f%% on the BAND %s (N_eff = "
          "%d of %d); HONEST MISS: n = 1 fails at %.2f -- the u = 0 "
          "JUMP of the generator (forced by |Ghat| ~ 1/gamma) is "
          "resolved at pitch D, and its two artifact components (in-"
          "band projection excess %+.2f, beyond-comb alias mass %+.2f "
          "of lambda_1) ADD there while partially canceling for "
          "n >= 2; pole-free correction costs <= %.1e of the L2 mass"
          % (hz, 100 * BAR_FORM, band, n_eff, N_MAX, err_tot[1],
             e1_proj, e1_alias, float(np.max(cp_kill[1:]))),
          n_eff >= 1)

    # ============================================================== L5
    print("\nL5 -- the corollary, spelled out")
    ok_cert = all(q_odd_win[n] > cert_lo[n] > 0.0 for n in s_eff)
    ok_pos = all(q_tot_win[n] > 0.0 and q_odd_win[n] > 0.0
                 for n in s_eff)
    share_odd = [lam_odd[n] / lam_ref[n] for n in s_eff]
    check("L5.1 [E/MEASURED] THE COROLLARY: for every n in the band %s "
          "the window read is POSITIVE and sits ABOVE the certified "
          "floor: Q_win_odd(n) >= D lambda_min^constr ||v||_G^2 > 0 "
          "(floors %.1e..%.1e, margins Q/floor %.0f..%.0f); the odd "
          "sector carries %.3f..%.3f of lambda_n there, so the v648-"
          "type datum lambda_min > 0 on the odd sector CONTAINS these "
          "%d Li coefficients up to the measured form error; the even "
          "complement is covered by the NEW even-sector measurement "
          "lambda_min^even,constr = %+.3e (pole-free hyperplane; the "
          "unconstrained even sector is INDEFINITE, lambda_min = "
          "%+.2e: the rank-2 pole block lives there)"
          % (band, min(cert_lo[n] for n in s_eff),
             max(cert_lo[n] for n in s_eff),
             min(q_odd_win[n] / cert_lo[n] for n in s_eff),
             max(q_odd_win[n] / cert_lo[n] for n in s_eff),
             min(share_odd), max(share_odd), n_eff, lam_min_ec,
             lam_min_e),
          ok_cert and ok_pos)

    # ============================================================== L6
    check("L6.1 [C] typing: everything here is a FINITE statement -- "
          "one declared window (h = %d), a 2000-zero comb with a "
          "declared tail budget, %d reproduced coefficients (band %s);"
          " the corollary direction is 'verified window positivity "
          "contains finite Li data', NOT Li's criterion, NOT an RH "
          "statement" % (hz, n_eff, band), True)

    VERDICT = ("LI-COROLLARY-FINITE" if not FAILS else
               ("FORM-MISMATCH" if ("L3.2" in FAILS or "L4.1" in FAILS)
                else "MIXED"))
    print("\nVERDICT: %s -- g_n = (1/2) e^{-|u|/2} L^(1)_{n-1}(|u|) "
          "derived and locked; window h = %d reproduces %d Li "
          "coefficients (band %s, < %.0f%% form error; n = 1 misses at"
          " %.2f, jump artifact) on the pole-free hyperplane, odd part"
          " certified by lambda_min = %+.3e > 0"
          % (VERDICT, hz, n_eff, band, 100 * BAR_FORM, err_tot[1],
             lam_min_o))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: v563 READ-ONLY; shared committed zero cache "
          "(dps %d, diagnostic zero-side line); finite statements "
          "only; NO RH claim" % DPS_ZEROS)
    print("--- v672_li_corollary: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
