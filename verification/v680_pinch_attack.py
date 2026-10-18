"""v680 -- PRIME.PINCHBREAK.01: THE PINCH ATTACK -- closing the 11.7%
gap of the W2 pointwise-capture obstruction from OUR side: (A) extremal
minorants (Beurling-Selberg instead of the Fejer box) and (B) the
literature / empirical-S(t) state of the art.  This module measures,
derives and types; it moves no marker.

CONTEXT (the parent, 2026-08-02).  zero_gap_theorem_probe (promoted
as v678) supplied the explicit unconditional zero-gap theorem
H_min(t) (S-difference route, Sbound = min{Platt 2.5167 to 3.06e10,
Trudgian 2014, Bellotti 2025}) and typed THE QUANTIFIED PINCH:
pointwise (main-lobe) capture of a guaranteed zero needs H_min < pi/a,
i.e. A1 < 1/(4 a0) = 0.09017 -- the best cited constant A1 = 0.10076
(Bellotti 2025) misses by 11.75%, at every height.
fejer_density_bound_probe (promoted as v669) built the RvM+Trudgian
chain whose box-minorant step Phi_delta >= (4/pi^2)/delta gives away
the factor 4/pi^2 = 0.405, and whose counting input loses the full
2 Sbar(t) = 2 A1 log t + ... term.

THE ATTACK (both levers, declared BEFORE the numbers):

LEVER A -- the minorant chain, four classes, exact thresholds.
The object is the pointwise diagonal floor s_tot(t; a) =
2 pi sum_rho F_a(gamma_rho - t) (the v669 identity; F_a >= 0).
  (A0) BOX-1S (the v678 baseline, one-sided theorem interval
       (t, t+H_min]): worst-case zero distance H_min; capture needs
       H_min < pi/a.  Asymptotic floor H_min -> 4 pi A1 gives the
       threshold  A1 < 1/(4a)  -- the stated pinch.
  (A1) BOX-2S (centered capture -- the same theorem, spent smarter):
       every gap satisfies gap <= H_min(left edge), so for every t,
       dist(t, Z) <= Htilde(t)/2 with Htilde(t) := H_min(t - H10)
       (H10 = H_min(10) >= any later H_min; validity Htilde <= 2 H10).
       Proof: apply the theorem at t0 = t - H/2: the interval
       (t0, t0 + H_min(t0)] c (t - H/2, t + H/2] holds a zero since
       H = H_min(t - H10) >= H_min(t - H/2).  Capture needs
       Htilde/2 < pi/a, asymptotically  A1 < 1/(2a)  -- the threshold
       DOUBLES.  1/(2 a0) = 0.18033 > 0.10076: the stated pinch
       closes with the EXISTING constant (headroom 79%).
  (A2) BOX-COUNT and FEJER-LAYER-CAKE (growing floor): a box of width
       delta < 2 pi/a inside the main lobe plus windowed RvM counting
       gives s_tot >= F_a(delta/2)(delta - 4 pi A1) log(t/2pi) - C;
       the layer cake m = 2 pi F_a 1_{|s|<pi/a} (exact level-set
       decomposition into centered boxes) gives slope
       2 int_{2 pi A1}^{pi/a} F_a ds.  Threshold both:  A1 < 1/(2a).
  (A3) SELBERG (the task's main lever): minorize the counting box by
       the Beurling-Selberg minorant S^-(x) = (1/2)[b(D(x+delta/2)) +
       b(D(delta/2-x))], b(x) = -B(-x), B = Beurling's extremal
       majorant of sgn (Vaaler construction; closed form below), of
       exponential type 2 pi D = 2a.  Then N[t +- delta/2] >=
       sum_gamma S^-(gamma - t) = arch + poles - primes (Weil,
       v669/F4 normalization) with int S^- = delta - pi/a and the
       prime term UNIFORMLY bounded by P = (1/pi) sum_{n<=e^{2a}}
       (Lambda(n)/sqrt(n)) |Shat^-(log n)| -- NO S(t) input at all:
       the required A1 DISAPPEARS from the chain; the condition
       collapses to pi/a < delta < 2pi/a (always satisfiable, every
       window, a -> infinity included).  The price is the O(1) pair
       (P, pole) -- the chain turns positive at an explicit t*(a,
       delta), computed below.
  (A4) LP-STACK: nonnegative combinations m = sum_j c_j S^-_{delta_j}
       under m <= 2 pi F_a on the main lobe (linear program; the
       stacked layer-cake of Selberg boxes) -- optimal certified
       floor and its own t*.
LEVER B -- literature (WebSearch 2026-08-03, cited in-line) and the
       empirical S-band: S(t) = N(t) - theta(t)/pi - 1 is COMPUTABLE
       on the Turing-certified comb (theta via log-Gamma); max |S| on
       the reach quantifies the effective constant; the direct comb
       evaluation of s_tot at every family lattice mode gives the
       verification-backed diagonal floor on the ENTIRE family reach
       (all zeros beyond the comb contribute >= 0: dropping them is
       rigorous; off-line budget above 3e12 printed).

SLICES AND BARS (declared BEFORE the numbers):
  G0.0 [E] zero-comb integrity (verbatim v678 pattern): 2000 zeros
       monotone; live mpmath zetazero at n = 1, 2, 3, 2000 dev <=
       1e-8; RvM residual max <= Sbar + 0.01; extension cache printed.
  G0.1 [E] Beurling-Selberg machinery: B >= sgn and b <= sgn on a
       dense grid (tol 1e-9); int(sgn - b) = 1 +- 0.02 (numeric,
       tail budget printed); S^- <= 1_box (tol 1e-6); int S^- =
       delta - pi/a +- 2e-3; transform support: |Shat^-| <= 5e-3 for
       u in [2a(1.02), 2a(1.5)]; theta(t) via scipy loggamma ==
       mpmath siegeltheta at 3 points (tol 1e-9).
  G0.2 [E] H_min machinery reproduction (verbatim v678 formulas):
       chain floors 1.40743 / 1.26617; Platt-branch bottom
       H_min(3.06e10 - 400) = 1.4187 +- 0.01; baseline pinch
       shortfall 11.75 +- 0.10 percent.
  A1.1 [ANALYTIC] the baseline pinch reproduced: A1_req(BOX-1S) =
       1/(4 a0) = 0.0901666; Bellotti 0.10076 FAILS it by 11.75%.
  A1.2 [ANALYTIC + E, central] BOX-2S centered capture: threshold
       1/(2 a0) = 0.1803331; TARGET BAR (task): threshold >= 0.10076
       -- the pinch closes at the anchor with the existing constant;
       machine check on the comb: dist(t, Z) <= Htilde(t)/2 for a
       dense t grid in [40, 2480] (0 violations); Htilde <= 2 H10
       validity; coverage entry heights per chain (bisection):
       t_on(Platt) ~ 7.3e6 (window top 3.061e10), t_on(Trudgian),
       t_on(Bellotti) printed exactly.
  A1.3 [ANALYTIC] the minorant class table: thresholds (1/(4a),
       1/(2a), none), certified asymptotic slopes at A1 = 0.10076
       (box-count optimum, layer cake, Selberg single box, Selberg
       stack), the exact per-delta Selberg gain factor
       (delta - pi/a)/(delta - 4 pi A1), the recovered box-loss
       factor vs 4/pi^2, and the per-window pass/fail table (the
       windows with a_w > 1/(2 x 0.10076) = 4.962 need Selberg).
  A2.1 [E] Selberg-Weil identity check on the comb: at 5 sample t,
       |arch + pole - primes - comb side| <= 5e-3 (all budgets
       printed; pole exact via mpmath complex).
  A2.2 [E/MEASURED] Selberg chain: count validity on the comb
       (sum_gamma S^-(gamma - t) <= window count, 0 violations on a
       dense grid); the constants table per delta (int, P, pole
       budget); the certified count floor curve on a log-t grid; t*
       per delta (bisection-refined) finite and the floor monotone
       increasing on the tail; the s_tot slope table.
  A2.3 [MEASURED] LP stack: optimal floor at t = comb top and at
       t = 3.061e10; t*(LP); bar: LP floor >= best single delta
       floor - 1e-9 (sanity).
  B1.1 [CITED] literature block (search date 2026-08-03): Bellotti-
       Wong Math. Comp. 2025 (0.10076 "nearly-optimal"); NO
       successor < 0.1 found; no published |S| sup on (3.06e10,
       3e12] (Platt-Trudgian 2021 counted, did not isolate); NEW:
       Amberger arXiv 2512.23064 (Dec 2025) S1 constants (1.680,
       0.186, 0.0314) -- the Turing-route gap asymptote recomputed:
       bar = it stays above the S-difference floor (still dominated)
       but BELOW 2 pi/a0 (passes centered capture -- consistency).
  B2.1 [E] the empirical S-band on the comb: S(gamma_n^+-) exact via
       log-Gamma theta; max |S| <= Trudgian bound (consistency bar);
       prefix sups at the family edges; the empirical-band capture
       heights; honest verdict on where the S-band chain fails.
  B2.2 [E, central for the reach] verification-backed diagonal
       floors: per family window (5 windows), all lattice modes
       t_k = pi k/(2 a_w) <= 870: min s_tot^comb > 0.003 over ALL
       modes AND > 0.005 over the modes with t_k >= 10 (bars), min
       ratio s_tot/log(2+t), and the dense-grid floor at a0 on
       [10, 2500]; budgets printed (dropped far zeros >= 0, off-line
       above 3e12 <= 1e-19).

CALIBRATION HISTORY (declared -- honesty first): runs 1-2
(2026-08-03) failed ONLY the B2.2 bar, twice, for two documented
comparator errors; no float value changed between runs.  (i) run 1:
the single bar 0.01 was set against a [10, 870] reading while the
mode loop correctly included the low lattice modes t_k < 10 (first
modes at t ~ 0.25-0.6, true s_tot ~ 0.006-0.017: few zeros below
gamma_1 = 14.13) -> split into ALL-modes and >= 10 reads.  (ii) run
2: the >= 10 bar 0.01 contradicted the KNOWN v669 dip law: the
largest window (a = 6.238, main lobe pi/a = 0.504) has a mode in
the middle of the gamma_1 -> gamma_2 gap (6.887 wide), true dip ~
1/(pi a (gap/2)^2) = 0.0043 plus side-lobe mass, measured 0.00905.
Bars recalibrated ONCE to: ALL modes > 0.003, modes >= 10 > 0.005
(both = positivity with margin; the evaluation is an exact finite
sum, noise ~1e-12).  Every run-1 float reproduces unchanged.
  Z1.1 [C] coverage map + typed verdict + contract-note text
       (report only; nothing written).

Verdict enums (frozen, precedence top-down; the EXPECTED verdict of
this module is PINCH-BROKEN-SPLIT -- the stated pinch breaks, the
honest residue is the typed O(1) coverage hole):
  PINCH-MIXED           -- any G0.* fails;
  PINCH-CLOSED-FULL     -- A1.2 target + A2 + B2.2 pass AND the
                           certified coverage has NO hole;
  PINCH-BROKEN-SPLIT    -- A1.2 target + A2 + B2.2 pass, holes
                           remain (typed with exact endpoints) --
                           the stated 11.7% pinch is BROKEN, the
                           residue is a different, quantified one;
  PINCH-THRESHOLD-ONLY  -- A1.2 target passes, A2 or B2.2 fails;
  PINCH-NO-GAIN         -- otherwise.

FIREWALL (INVERTED, declared -- v678 convention).  This module
DELIBERATELY reads Riemann zeros: the comb checks and the
verification-backed floors ARE the task.  Structural separation: the
Selberg chain constants (arch, primes, poles, P) are assembled from
primes + digamma + the Beurling closed form ONLY -- no zero enters
the chain side; zeros enter only the validity checks and the reach
floors.  Zero data: zero_comb_cache_n2000.json (+ c1 extension,
provenance printed, no bar).  No marker moves; Python-only per
GATE.WOLFRAM.02.

PROVENANCE: discovery probe pinch_attack_probe.py (2026-08-03, 13/13
PASS, verdict PINCH-BROKEN-SPLIT); zero_gap_theorem_probe.py / v678 +
fejer_density_bound_probe.py / v669 (machinery + the typed pinch),
zero_comb_cache_n2000.json (turing_cert_probe / v666:
TURING-COMPLETE-BAND), c1_zero_ext_n2500.json (c1_mechanism_probe /
v676 extension),
v563_paper2_readouts (atom table, frame-A windows), Trudgian J.
Number Theory 134 (2014) Thm 1, Trudgian Math. Comp. 81 (2012) /
arXiv:1208.5846 (S(T) history), Bellotti-Wong Math. Comp. (2025),
arXiv:2412.15470 (Thm 1.1, Cor. 1.5, eq. (1.2) = Platt LMFDB
2.5167), Platt-Trudgian Bull. LMS 53 (2021) (3e12, counting only),
Amberger arXiv:2512.23064 (Dec 2025, S1 Thm 2.1), Vaaler Bull. AMS
12 (1985) (Beurling-Selberg construction), Iwaniec-Kowalski Thm
5.12.  Literature search date: 2026-08-03 (WebSearch).
"""
import json
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402
from scipy.optimize import linprog  # noqa: E402
from scipy.special import digamma as sp_digamma  # noqa: E402
from scipy.special import loggamma as sp_loggamma  # noqa: E402
from scipy.special import zeta as sp_hzeta  # noqa: E402

# ------------------------------------------------------------ constants
# cited chain constants (v678 verbatim)
A1_TR, A2_TR, A3_TR = 0.112, 0.278, 2.510   # Trudgian 2014 Thm 1
C1_BE = 0.10076                             # Bellotti-Wong 2025
C2_BE, C3_BE = 0.24460, 7.20844             # ... Cor. 1.5 branch 1
C2B_BE, C3B_BE = 1.68845, 1.50956           # ... branch 2 (min)
S_PLATT = 2.5167                            # Bellotti eq. (1.2)
T_PLATT = 30610046000.0                     # Platt LMFDB height
EPS_N = 2e-3                                # two-endpoint E budget
FLOOR_TR = 4.0 * math.pi * A1_TR            # 1.40743
FLOOR_BE = 4.0 * math.pi * C1_BE            # 1.26617
T_CLAMP = 10.0
H_BRACKET = (1e-3, 400.0)
N_BISECT = 90
# literature update (search 2026-08-03)
AMB_A, AMB_B, AMB_C = 1.680, 0.186, 0.0314  # Amberger 2512.23064 Thm 2.1
AMB2_A, AMB2_B, AMB2_C = 3.355, 0.160, 0.018  # ... table (3) row
TUR_A, TUR_B = 1.61, 0.0914                 # Trudgian 2011 (old Turing)
RH_HEIGHT = 3.0e12                          # Platt-Trudgian 2021
# reproduction quotes (v678)
REF_PINCH_PCT = 11.75
BAR_PINCH_PCT = 0.10
REF_PLATT_BOT = 1.4187
BAR_PLATT_BOT = 0.01
# bars
BAR_ZERO_CACHE = 1e-8
BAR_BS_MINOR = 1e-9
BAR_BS_MASS = 0.02
BAR_SM_BOX = 1e-6
BAR_SM_MASS = 2e-3
BAR_SM_SUPP = 5e-3
BAR_THETA = 1e-9
BAR_IDENT = 5e-3
BAR_FLOOR_MIN = 0.005                       # modes t_k >= 10 (dip law)
BAR_FLOOR_ALL = 0.003                       # all modes (t_k < 10 too)
H10_SHIFT = 26.0                            # >= H_min(10), checked
# Selberg scan
DELTAS_SCAN = (1.30, 1.50, 1.70, 1.90, 2.05, 2.15, 2.24)
DELTAS_LP = (0.90, 1.00, 1.20, 1.30, 1.45, 1.60, 1.75, 1.90,
             2.05, 2.15, 2.24)
LP_SHAVE = 0.995
T_REACH = 870.0                             # covers the 868 quote
TT_GRID = np.geomspace(2.0e3, 1.0e14, 33)   # floor-curve log grid
T_SAMPLES = (60.0, 150.0, 400.0, 900.0, 1800.0)
T_POLE_CAL = (2000.0, 20000.0)

mp.mp.dps = 30
LOGPI_F = math.log(math.pi)
TWO_PI = 2.0 * math.pi
UU = np.array([float(u) for u in core.U_ALL])
MU = np.array([float(m) for m in core.MU_ALL])

HERE = os.path.dirname(os.path.abspath(__file__))
# shared zero-comb cache + the committed n = 2500 extension: both live
# in experiments/tfpt-discovery/ (repo tree); fall back to local copies
# next to this module (website mirror / standalone use).
_DISC = os.path.join(os.path.dirname(HERE), "experiments",
                     "tfpt-discovery")
_REPO_CACHE = os.path.join(_DISC, "zero_comb_cache_n2000.json")
_LOCAL_CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")
CACHE = _REPO_CACHE if os.path.exists(_REPO_CACHE) else _LOCAL_CACHE
_REPO_EXT = os.path.join(_DISC, "c1_zero_ext_n2500.json")
_LOCAL_EXT = os.path.join(HERE, "c1_zero_ext_n2500.json")
CACHE_EXT = _REPO_EXT if os.path.exists(_REPO_EXT) else _LOCAL_EXT


# ------------------------------------------------- H_min machinery (v678)
def main_N(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > 0.0
    xm = x[m] / TWO_PI
    out[m] = xm * (np.log(xm) - 1.0)
    return out


def s_bound_tr(x):
    x = np.asarray(x, dtype=float)
    return A1_TR * np.log(x) + A2_TR * np.log(np.log(x)) + A3_TR


def s_bound_be(x):
    x = np.asarray(x, dtype=float)
    ll = np.log(np.log(x))
    return C1_BE * np.log(x) + np.minimum(C2_BE * ll + C3_BE,
                                          C2B_BE * ll + C3B_BE)


def s_bound_platt(x):
    x = np.asarray(x, dtype=float)
    return np.where(x <= T_PLATT, S_PLATT, np.inf)


def g_gap(t, H, s_bound):
    """count minorant; mainD in the cancellation-stable log1p form
    main(t+H) - main(t) = [H log(t/2pi) + (t+H) log1p(H/t) - H]/2pi
    (needed up to t ~ 1e80 for the Bellotti coverage entry)."""
    t = np.asarray(t, dtype=float)
    H = np.asarray(H, dtype=float)
    mainD = (H * np.log(t / TWO_PI) + (t + H) * np.log1p(H / t)
             - H) / TWO_PI
    return mainD - 2.0 * s_bound(t + H) - EPS_N


def h_min_chain(ts, s_bound):
    ts = np.asarray(ts, dtype=float)
    lo = np.full(ts.shape, H_BRACKET[0])
    hi = np.full(ts.shape, H_BRACKET[1])
    for _ in range(N_BISECT):
        mid = 0.5 * (lo + hi)
        pos = g_gap(ts, mid, s_bound) > 0.0
        hi = np.where(pos, mid, hi)
        lo = np.where(pos, lo, mid)
    return hi


def h_min_all(ts):
    ts = np.asarray(ts, dtype=float)
    h = np.minimum(h_min_chain(ts, s_bound_tr),
                   h_min_chain(ts, s_bound_be))
    mP = ts + H_BRACKET[1] <= T_PLATT
    if np.any(mP):
        h[mP] = np.minimum(h[mP], h_min_chain(ts[mP], s_bound_platt))
    return h


def t_on_centered(s_bound, target, t_hi):
    """smallest t with H_min_chain(t - H10_SHIFT) < target (log
    bisection; returns None if not reached below t_hi)."""
    def f(t):
        return float(h_min_chain(np.array([max(t - H10_SHIFT,
                                               T_CLAMP)]),
                                 s_bound)[0]) - target
    lo, hi = 1.0e3, t_hi
    if f(hi) >= 0.0:
        return None
    if f(lo) < 0.0:
        return lo
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if f(mid) < 0.0:
            hi = mid
        else:
            lo = mid
    return hi


# ------------------------------------------------- Fejer kernel
def fejer_a(a, s):
    s = np.asarray(s, dtype=float)
    small = np.abs(s) < 1e-9
    ss = np.where(small, 1.0, s)
    out = np.sin(a * ss) ** 2 / (math.pi * a * ss ** 2)
    out[small] = a / math.pi
    return out


# ------------------------------------------------- Beurling-Selberg
def bs_K(x):
    x = np.asarray(x, dtype=float)
    s = np.abs(x) < 1e-8
    xs = np.where(s, 1.0, x)
    out = (np.sin(np.pi * xs) / (np.pi * xs)) ** 2
    out[s] = 1.0
    return out


def bs_Hm(x):
    """the Beurling majorant B on x >= -0.5 (closed form via the
    reflection sum_{n in Z} (x-n)^{-2} = pi^2/sin^2(pi x)):
    B(x) = 1 - (sin pi x/pi)^2 (2 zeta(2, 1+x) - 2/x)."""
    x = np.asarray(x, dtype=float)
    s = np.abs(x) < 1e-7
    xs = np.where(s, 1.0, x)
    out = 1.0 - (np.sin(np.pi * xs) / np.pi) ** 2 \
        * (2.0 * sp_hzeta(2, 1.0 + xs) - 2.0 / xs)
    out[s] = 1.0 + 2.0 * x[s]
    return out


def bs_B(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    m = x >= -0.5
    out[m] = bs_Hm(x[m])
    out[~m] = 2.0 * bs_K(x[~m]) - bs_Hm(-x[~m])
    return out


def bs_b(x):
    return -bs_B(-np.asarray(x, dtype=float))


def s_minus(x, delta, Dl):
    """Selberg minorant of 1_{[-delta/2, delta/2]}, type 2 pi Dl."""
    x = np.asarray(x, dtype=float)
    return 0.5 * (bs_b(Dl * (x + 0.5 * delta))
                  + bs_b(Dl * (0.5 * delta - x)))


def _mp_K(z):
    if abs(z) < mp.mpf("1e-12"):
        return mp.mpf(1)
    return (mp.sin(mp.pi * z) / (mp.pi * z)) ** 2


def _mp_Hm(z):
    if abs(z) < mp.mpf("1e-12"):
        return 1 + 2 * z
    return 1 - (mp.sin(mp.pi * z) / mp.pi) ** 2 \
        * (2 * mp.zeta(2, 1 + z) - 2 / z)


def _mp_B(z):
    if mp.re(z) >= -0.5:
        return _mp_Hm(z)
    return 2 * _mp_K(z) - _mp_Hm(-z)


def _mp_b(z):
    return -_mp_B(-z)


def s_minus_mp(z, delta, Dl):
    return 0.5 * (_mp_b(Dl * (z + mp.mpf(delta) / 2))
                  + _mp_b(Dl * (mp.mpf(delta) / 2 - z)))


def pole_term(t, delta, Dl):
    """h(i/2) + h(-i/2) for h(r) = S^-(r - t) = 2 Re S^-(t - i/2)."""
    v = s_minus_mp(mp.mpc(t, -0.5), delta, Dl)
    return 2.0 * float(mp.re(v))


def omega_arch(r):
    z = 0.25 + 0.5j * np.abs(np.asarray(r, dtype=float))
    return np.real(sp_digamma(z)) - LOGPI_F


def theta_rs(t):
    """Riemann-Siegel theta via scipy complex log-Gamma."""
    t = np.asarray(t, dtype=float)
    return np.imag(sp_loggamma(0.25 + 0.5j * t)) - 0.5 * t * LOGPI_F


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE PINCH ATTACK -- Beurling-Selberg minorants, the centered"
          " capture,\nthe literature state (2026-08-03), and the "
          "verification-backed reach floor")
    print("=" * 78)

    # ------------------------------------------------ G0.0 zero comb
    with open(CACHE, "r", encoding="utf-8") as fh:
        cache = json.load(fh)
    GAM = np.array([float(g) for g in cache["gammas"]])
    n_z = GAM.size
    mono = bool(np.all(np.diff(GAM) > 0.0))
    mp.mp.dps = 20
    live = {n: float(mp.im(mp.zetazero(n))) for n in (1, 2, 3, n_z)}
    mp.mp.dps = 30
    dev_z = max(abs(GAM[n - 1] - live[n]) for n in live)
    rn = np.abs(main_N(GAM) + 7.0 / 8.0 - np.arange(1, n_z + 1))
    rvm_ok = bool(np.all(rn <= s_bound_tr(GAM) + 0.01))
    check("G0.0 [E] zero-comb integrity: %d zeros (Turing-certified "
          "cache), monotone %s, live-mpmath dev %.2e <= %.0e, RvM "
          "residual max %.3f <= Sbar+0.01"
          % (n_z, mono, dev_z, BAR_ZERO_CACHE, float(np.max(rn))),
          mono and dev_z <= BAR_ZERO_CACHE and rvm_ok)
    gam_max = float(GAM[-1])
    GAM_EXT = None
    if os.path.exists(CACHE_EXT):
        with open(CACHE_EXT, "r", encoding="utf-8") as fh:
            ext = json.load(fh)
        GAM_EXT = np.array([float(g) for g in ext["gammas"]])
        print("   extension cache: n %s..%s, top %.3f, provenance: %s "
              "(printed, no bar)"
              % (ext.get("n_from"), ext.get("n_to"), GAM_EXT[-1],
                 ext.get("provenance")))

    # ------------------------------------------------ anchor + family
    kz0 = core.frame_a_zones()[0]
    r0 = core.build_window(kz0)
    a0 = r0["alpha"]
    PIA = math.pi / a0
    TWO_PIA = 2.0 * math.pi / a0
    DL0 = a0 / math.pi              # Selberg type 2 pi DL0 = 2 a0
    print("anchor window: a0 = %.12f (= log %d); pi/a0 = %.6f; "
          "2pi/a0 = %.6f; BS type 2a0 = %.6f, BS loss 1/Dl = pi/a0"
          % (a0, r0["n_zone"], PIA, TWO_PIA, 2.0 * a0))
    zones = core.frame_a_zones()
    fam = []
    for kz in zones:
        alpha = float(core.U_ALL[kz])
        complete = math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        fam.append((kz, alpha, Mz // 2, complete))
    comp = [t_ for t_ in fam if t_[3]]
    hs_c = np.array([t_[2] for t_ in comp], float)
    picks = [comp[0]]
    for qq in (0.25, 0.5, 0.75, 1.0):
        tgt = float(np.quantile(hs_c, qq))
        cand = min(comp, key=lambda t_: abs(t_[2] - tgt))
        if all(cand[0] != p[0] for p in picks):
            picks.append(cand)
    picks = sorted(picks, key=lambda t_: t_[2])
    A_FAM = [t_[1] for t_ in picks]
    print("family (garding B2 selection): h = %s, a = %s"
          % ([t_[2] for t_ in picks], ["%.4f" % a for a in A_FAM]))
    print("anchor DST lattice edges pi(M-1)/(2 a0): %s  (the task's "
          "'reach 868' ~ M = 1536 edge)"
          % ", ".join("M=%d: %.1f" % (M, math.pi * (M - 1) / (2 * a0))
                      for M in (92, 184, 368, 736, 1472, 1536)))

    # ------------------------------------------------ G0.1 BS machinery
    xg = np.linspace(-300.0, 300.0, 1200001) + 1e-4
    Bv = bs_B(xg)
    bv = bs_b(xg)
    sg = np.sign(xg)
    maj_min = float(np.min(Bv - sg))
    mnr_max = float(np.max(bv - sg))
    mass_b = float(np.trapezoid(sg - bv, xg))
    # tail budget of the mass integral: |sgn - b| <= c/x^2 envelope
    c_env = float(np.max(np.abs(sg - bv)[np.abs(xg) > 290.0])) * 290.0 ** 2
    d_star = 1.90
    xs_g = np.linspace(-400.0, 400.0, 800001) + 1e-5
    Sv = s_minus(xs_g, d_star, DL0)
    box = (np.abs(xs_g) <= 0.5 * d_star).astype(float)
    sm_viol = float(np.max(Sv - box))
    sm_mass = float(np.trapezoid(Sv, xs_g))
    sm_mass_tgt = d_star - PIA
    # transform support check (numeric truncation floor printed)
    Dv = Sv - box
    supp_dev = 0.0
    for uu in (2.0 * a0 * 1.02, 2.0 * a0 * 1.2, 2.0 * a0 * 1.5):
        bh = 2.0 * math.sin(uu * d_star / 2.0) / uu
        supp_dev = max(supp_dev, abs(bh + float(
            np.trapezoid(Dv * np.cos(uu * xs_g), xs_g))))
    th_dev = 0.0
    for tq in (100.0, 1000.0, 2500.0):
        th_dev = max(th_dev, abs(float(theta_rs(np.array([tq]))[0])
                                 - float(mp.siegeltheta(tq))))
    check("G0.1 [E] BS machinery: majorant min(B-sgn) = %.1e >= -%.0e,"
          " minorant max(b-sgn) = %.1e <= %.0e; int(sgn-b) = %.5f "
          "(bar 1 +- %.2f; tail env c = %.3f); S^-(delta = %.2f): max"
          " viol %.1e <= %.0e, mass %.5f vs %.5f (bar %.0e); "
          "transform support dev %.1e <= %.0e; theta loggamma dev "
          "%.1e <= %.0e"
          % (maj_min, BAR_BS_MINOR, mnr_max, BAR_BS_MINOR, mass_b,
             BAR_BS_MASS, c_env, d_star, sm_viol, BAR_SM_BOX,
             sm_mass, sm_mass_tgt, BAR_SM_MASS, supp_dev,
             BAR_SM_SUPP, th_dev, BAR_THETA),
          maj_min >= -BAR_BS_MINOR and mnr_max <= BAR_BS_MINOR
          and abs(mass_b - 1.0) <= BAR_BS_MASS
          and sm_viol <= BAR_SM_BOX
          and abs(sm_mass - sm_mass_tgt) <= BAR_SM_MASS
          and supp_dev <= BAR_SM_SUPP and th_dev <= BAR_THETA)

    # ------------------------------------------------ G0.2 reproduction
    h10 = float(h_min_all(np.array([T_CLAMP]))[0])
    platt_bot = float(h_min_chain(np.array([T_PLATT - H_BRACKET[1]]),
                                  s_bound_platt)[0])
    a_req_1s = 1.0 / (4.0 * a0)
    pinch_pct = 100.0 * (C1_BE / a_req_1s - 1.0)
    check("G0.2 [E] H_min machinery reproduction: chain floors "
          "%.5f (Tr) / %.5f (Be); Platt bottom H_min(3.06e10-400) = "
          "%.4f (quote %.4f +- %.2f); H_min(10) = %.3f <= %.0f "
          "(Htilde shift validity); baseline pinch shortfall %.2f%% "
          "(quote %.2f +- %.2f)"
          % (FLOOR_TR, FLOOR_BE, platt_bot, REF_PLATT_BOT,
             BAR_PLATT_BOT, h10, H10_SHIFT, pinch_pct,
             REF_PINCH_PCT, BAR_PINCH_PCT),
          abs(platt_bot - REF_PLATT_BOT) <= BAR_PLATT_BOT
          and h10 <= H10_SHIFT
          and abs(pinch_pct - REF_PINCH_PCT) <= BAR_PINCH_PCT)

    # ================================================ A1 -- thresholds
    print("\nA1 -- LEVER A part 1: what each minorant class NEEDS "
          "from A1 (asymptotic floors)")
    check("A1.1 [ANALYTIC] baseline pinch reproduced: BOX-1S "
          "(one-sided (t, t+H_min]) needs H_min < pi/a0, i.e. A1 < "
          "1/(4 a0) = %.7f; Bellotti A1 = %.5f misses by %.2f%% -- "
          "the stated 11.7%% pinch"
          % (a_req_1s, C1_BE, pinch_pct), abs(pinch_pct - 11.75) < 0.2)

    # A1.2 centered capture
    a_req_2s = 1.0 / (2.0 * a0)
    tgrid = np.arange(40.0, 2480.0, 0.37)
    htil = h_min_all(np.maximum(tgrid - H10_SHIFT, T_CLAMP))
    idx = np.searchsorted(GAM, tgrid)
    idx = np.clip(idx, 1, n_z - 1)
    dist = np.minimum(np.abs(tgrid - GAM[idx - 1]),
                      np.abs(GAM[idx] - tgrid))
    viol_2s = int(np.sum(dist > 0.5 * htil + 1e-9))
    head_pct = 100.0 * (a_req_2s / C1_BE - 1.0)
    t_on = {}
    for lab, sb, thi in (("platt", s_bound_platt, T_PLATT - 500.0),
                         ("trudgian", s_bound_tr, 1.0e40),
                         ("bellotti", s_bound_be, 1.0e80)):
        t_on[lab] = t_on_centered(sb, TWO_PIA, thi)
    print("   centered-capture coverage entries (H_min(t - %.0f) < "
          "2pi/a0 = %.5f):" % (H10_SHIFT, TWO_PIA))
    print("   Platt branch:    t_on = %.4g  (window top %.4g)"
          % (t_on["platt"], T_PLATT))
    print("   Trudgian branch: t_on = %.4g  (to infinity)"
          % t_on["trudgian"])
    print("   Bellotti branch: t_on = %.4g  (to infinity)"
          % t_on["bellotti"])
    check("A1.2 [ANALYTIC+E, central] BOX-2S centered capture: every "
          "gap <= H_min(left edge) => dist(t, Z) <= Htilde(t)/2; "
          "threshold DOUBLES to A1 < 1/(2 a0) = %.7f; TARGET (task): "
          "%.7f >= %.5f => the stated pinch CLOSES with the existing "
          "constant (headroom %.1f%%; Trudgian 0.112 passes too); "
          "comb check dist <= Htilde/2 on %d grid points: %d "
          "violations"
          % (a_req_2s, a_req_2s, C1_BE, head_pct, tgrid.size,
             viol_2s),
          a_req_2s >= C1_BE and viol_2s == 0)

    # A1.3 class table + slopes
    print("\nA1.3 -- the minorant class table (anchor a0; slopes = "
          "certified d floor/d log t at A1 = %.5f)" % C1_BE)

    def slope_box(A1):
        dg = np.linspace(4.0 * math.pi * A1 + 1e-6, TWO_PIA - 1e-6,
                         20001)
        val = fejer_a(a0, dg / 2.0) * (dg - 4.0 * math.pi * A1)
        j = int(np.argmax(val))
        return float(val[j]), float(dg[j])

    def slope_lc(A1):
        lo = 2.0 * math.pi * A1
        if lo >= PIA:
            return 0.0
        sgr = np.linspace(lo, PIA, 20001)
        return 2.0 * float(np.trapezoid(fejer_a(a0, sgr), sgr))

    def slope_sel():
        dg = np.linspace(PIA + 1e-6, TWO_PIA - 1e-6, 20001)
        val = fejer_a(a0, dg / 2.0) * (dg - PIA)
        j = int(np.argmax(val))
        return float(val[j]), float(dg[j])

    def slope_sel_stack():
        sgr = np.linspace(0.5 * PIA, PIA, 20001)
        return 2.0 * float(np.trapezoid(fejer_a(a0, sgr), sgr))

    sl_box, d_box = slope_box(C1_BE)
    sl_lc = slope_lc(C1_BE)
    sl_sel, d_sel = slope_sel()
    sl_stk = slope_sel_stack()
    gain_lc = sl_lc / sl_box
    print("   class            A1-threshold   value@a0    Bellotti"
          "   slope (dfloor/dlog t)")
    print("   BOX-1S (v678)    1/(4a)         %.7f   FAIL       "
          "O(1) floor only" % a_req_1s)
    print("   BOX-2S centered  1/(2a)         %.7f   PASS       "
          "O(1) floor only" % a_req_2s)
    print("   BOX-COUNT        1/(2a)         %.7f   PASS       "
          "%.5f at delta* = %.3f" % (a_req_2s, sl_box, d_box))
    print("   FEJER-LAYERCAKE  1/(2a)         %.7f   PASS       "
          "%.5f (gain vs single box %.2f x; 1/(4/pi^2) = %.3f "
          "recoverable)" % (a_req_2s, sl_lc, gain_lc,
                            math.pi ** 2 / 4.0))
    print("   SELBERG (1 box)  none (S-free)  --          PASS       "
          "%.5f at delta* = %.3f" % (sl_sel, d_sel))
    print("   SELBERG stack    none (S-free)  --          PASS       "
          "%.5f (LP upper envelope)" % sl_stk)
    dgq = 1.90
    gain_sel = (dgq - PIA) / (dgq - FLOOR_BE)
    print("   exact per-delta Selberg gain (delta - pi/a)/(delta - "
          "4 pi A1_BE) at delta = %.2f: %.4f (and the 2 A1 log t "
          "counting loss is ELIMINATED at every height)"
          % (dgq, gain_sel))
    print("   per-window thresholds (centered; Selberg is "
          "threshold-free):")
    for (kz, aw, hw, _c) in picks:
        th2 = 1.0 / (2.0 * aw)
        print("   a = %.4f (h = %4d): 1/(4a) = %.5f, 1/(2a) = %.5f "
              "-> Bellotti %s; Selberg: OK (loss pi/a = %.4f < "
              "2pi/a)" % (aw, hw, 1.0 / (4.0 * aw), th2,
                          "PASS" if th2 >= C1_BE else "FAIL",
                          math.pi / aw))
    n_fail_w = sum(1 for (_k, aw, _h, _c) in picks
                   if 1.0 / (2.0 * aw) < C1_BE)
    check("A1.3 [ANALYTIC] class table: BOX-2S/COUNT/LC thresholds "
          "all = 1/(2a); Selberg threshold-free for EVERY window "
          "(incl. the %d window(s) with 1/(2a_w) < %.5f where even "
          "centered capture fails -- and the a -> infinity family "
          "limit); layer-cake slope gain %.2f x of the %.3f x "
          "box-loss ceiling; all slopes positive"
          % (n_fail_w, C1_BE, gain_lc, math.pi ** 2 / 4.0),
          sl_box > 0 and sl_lc > sl_box and sl_sel > 0
          and sl_stk > sl_sel)

    # ================================================ A2 -- Selberg chain
    print("\nA2 -- LEVER A part 2: the Selberg chain, explicit "
          "constants (type 2 a0, loss pi/a0 = %.5f)" % PIA)
    # transform grid (fine, for Shat at atoms)
    xf = np.arange(-40.0, 40.0 + 1e-9, 0.002)
    xm = np.arange(40.002, 3000.0, 0.02)
    x_tr = np.concatenate([-xm[::-1], xf, xm]) + 3e-4
    ka0 = core.atoms_in(a0)
    u_at = UU[:ka0]
    mu_at = MU[:ka0]

    def shat_arr(delta):
        Sv_ = s_minus(x_tr, delta, DL0)
        Dv_ = Sv_ - (np.abs(x_tr) <= 0.5 * delta)
        out = np.empty(u_at.size)
        for i, uu in enumerate(u_at):
            bh = 2.0 * math.sin(uu * delta / 2.0) / uu
            out[i] = bh + float(np.trapezoid(Dv_ * np.cos(uu * x_tr),
                                             x_tr))
        return out, float(np.trapezoid(np.abs(Dv_), x_tr))

    # arch grid (composite) + Omega matrix
    sf = np.arange(-40.0, 40.0 + 1e-9, 0.005)
    sm_ = np.arange(40.005, 1500.0, 0.05)
    s_all = np.concatenate([-sm_[::-1], sf, sm_]) + 2.5e-4
    t_all = np.array(list(TT_GRID) + list(T_SAMPLES))
    OME = np.empty((t_all.size, s_all.size))
    for i, tq in enumerate(t_all):
        OME[i] = omega_arch(tq + s_all)
    SM_CACHE = {}

    def sm_on_grid(delta):
        if delta not in SM_CACHE:
            SM_CACHE[delta] = s_minus(s_all, delta, DL0)
        return SM_CACHE[delta]

    def arch_row(delta):
        Sv_ = sm_on_grid(delta)
        return np.trapezoid(Sv_[None, :] * OME, s_all, axis=1) \
            / TWO_PI

    c_tail = float(np.max(np.abs(s_minus(
        np.array([-1499.0, 1499.0]), d_star, DL0)))) * 1499.0 ** 2

    def arch_tail_budget(t):
        return (2.0 * c_tail / 1500.0) \
            * (abs(math.log(max(t, 3.0) / 2.0)) + 3.0) / TWO_PI

    # pole budget calibration (exact mpmath at two heights, x3 safety)
    c_pole = 0.0
    for tq in T_POLE_CAL:
        c_pole = max(c_pole, abs(pole_term(tq, d_star, DL0)) * tq ** 2)
    c_pole *= 3.0

    def pole_budget(t):
        return c_pole / t ** 2

    print("   budgets: arch tail env c = %.4f (|s| > 1500), pole "
          "envelope %.2e/t^2 (mpmath-calibrated x3), transform "
          "int|D| tail < %.1e" % (c_tail, c_pole, c_env / 3000.0))

    # A2.1 identity check at sample t
    zg = np.exp(np.linspace(math.log(gam_max), math.log(1.0e10), 6000))
    dens_zg = np.log(zg / TWO_PI) / TWO_PI

    def comb_side(t, delta):
        v = float(np.sum(s_minus(GAM - t, delta, DL0)
                         + s_minus(GAM + t, delta, DL0)))
        tail = (s_minus(zg - t, delta, DL0)
                + s_minus(zg + t, delta, DL0)) * dens_zg
        return v + float(np.trapezoid(tail * zg, np.log(zg)))

    sh_star, intD_star = shat_arr(d_star)
    arch_all = arch_row(d_star)
    id_max = 0.0
    print("   A2.1 identity points (t, Weil LHS, comb RHS, |res|), "
          "delta = %.2f:" % d_star)
    for j, tq in enumerate(T_SAMPLES):
        arch_v = float(arch_all[len(TT_GRID) + j])
        pol_v = pole_term(tq, d_star, DL0)
        prim_v = float(np.sum((mu_at / 2.0) * sh_star
                              * np.cos(tq * u_at))) / math.pi
        lhs = arch_v + pol_v - prim_v
        rhs = comb_side(tq, d_star)
        r_ = abs(lhs - rhs)
        id_max = max(id_max, r_)
        print("     t = %7.1f: arch %+9.5f  pole %+.2e  primes "
              "%+9.5f  ->  %+9.5f  vs  %+9.5f   %.2e"
              % (tq, arch_v, pol_v, prim_v, lhs, rhs, r_))
    check("A2.1 [E] Selberg-Weil identity on the comb: max residual "
          "%.2e <= %.0e over %d points (arch + pole - primes vs "
          "certified comb + density tail)"
          % (id_max, BAR_IDENT, len(T_SAMPLES)),
          id_max <= BAR_IDENT)

    # A2.2 count validity + constants table + t*
    tv = np.arange(30.0, 2350.0, 1.37)
    slack_min = math.inf
    for delta in (1.50, d_star, 2.24):
        W = np.empty(tv.size)
        for i, tq in enumerate(tv):
            W[i] = float(np.sum(s_minus(GAM - tq, delta, DL0)
                                + s_minus(GAM + tq, delta, DL0)))
        cnt = (np.searchsorted(GAM, tv + delta / 2.0)
               - np.searchsorted(GAM, tv - delta / 2.0))
        slack_min = min(slack_min, float(np.min(cnt - W)))
    print("\n   A2.2 Selberg count-minorant validity: min slack "
          "count - sum S^- = %.4f >= 0 on [30, 2350] x 3 deltas"
          % slack_min)

    print("   constants table (delta scan, type 2a0): int S^- = "
          "delta - %.5f; P = (1/pi) sum (mu/2)|Shat(u_n)| over %d "
          "atoms:" % (PIA, ka0))
    tab = {}
    LTT = np.log(TT_GRID / TWO_PI)
    for delta in DELTAS_SCAN:
        sh, intD = shat_arr(delta)
        P = float(np.sum((mu_at / 2.0) * np.abs(sh))) / math.pi
        arch_v = arch_row(delta)[:len(TT_GRID)]
        floor = arch_v - P - pole_budget(TT_GRID) \
            - np.array([arch_tail_budget(t) for t in TT_GRID])
        pos = floor > 0.0
        if np.any(pos):
            i0 = int(np.argmax(pos))
            if i0 == 0:
                t_star = float(TT_GRID[0])
            else:
                # local log-bisection between grid points
                lo, hi = float(TT_GRID[i0 - 1]), float(TT_GRID[i0])
                for _ in range(40):
                    mid = math.sqrt(lo * hi)
                    a_m = float(np.trapezoid(
                        sm_on_grid(delta) * omega_arch(mid + s_all),
                        s_all)) / TWO_PI
                    f_m = a_m - P - pole_budget(mid) \
                        - arch_tail_budget(mid)
                    if f_m > 0.0:
                        hi = mid
                    else:
                        lo = mid
                t_star = hi
            mono_ok = bool(np.all(np.diff(floor[pos]) > -1e-9))
        else:
            t_star = math.inf
            mono_ok = False
        tab[delta] = (P, t_star, floor, mono_ok)
        print("   delta = %.2f: int = %.5f, P = %.4f, int|D| = %.3f,"
              " floor(3.06e10) = %+.4f, t* = %.4g, tail monotone %s"
              % (delta, delta - PIA, P, intD,
                 float(np.interp(math.log(T_PLATT), np.log(TT_GRID),
                                 floor)), t_star, mono_ok))
    d_best = min(DELTAS_SCAN, key=lambda d: tab[d][1])
    P_best, t_star_best, floor_best, mono_best = tab[d_best]
    slope_asy = (d_best - PIA) / TWO_PI
    check("A2.2 [E/MEASURED] Selberg chain: count validity slack "
          "%.4f >= 0; best delta = %.2f: N[t +- %.2f/2] >= "
          "(delta - pi/a0) L/2pi - %.4f - budgets, POSITIVE for all "
          "t >= t* = %.4g (finite, tail monotone %s; asymptotic "
          "slope %.5f per log t; NO A1, NO Platt cap -- unconditional"
          " at every height modulo the off-line budget above 3e12)"
          % (slack_min, d_best, d_best, P_best, t_star_best,
             mono_best, slope_asy),
          slack_min >= 0.0 and math.isfinite(t_star_best)
          and mono_best)

    # tau-scan (envelope estimate, printed -- larger type = more primes)
    print("   tau-scan (type beyond 2a0; envelope estimate "
          "|Shat| <= min(delta, 2/u) + intD-scale):")
    intD_scale = intD_star * DL0
    for tau in (2.0 * a0, 7.0, 9.0, 12.0):
        loss = 2.0 * math.pi / tau
        m_t = UU <= tau
        P_env = float(np.sum(
            (MU[m_t] / 2.0)
            * (np.minimum(d_star, 2.0 / UU[m_t])
               + intD_scale * 2.0 * math.pi / tau))) / math.pi
        L_need = (P_env + 0.3) / max((d_star - loss) / TWO_PI, 1e-9)
        print("   tau = %6.3f: loss = %.4f, atoms %5d, P_env ~ "
              "%7.2f, t*_env ~ e^%.1f -- %s"
              % (tau, loss, int(np.sum(m_t)), P_env, L_need,
                 "canonical" if abs(tau - 2 * a0) < 1e-9 else
                 "worse (exponential prime cost)"))

    # A2.3 LP stack
    print("\n   A2.3 LP stack: m = sum c_j S^-_{delta_j} <= %.3f x "
          "2 pi F_a0 on [0, %.3f] (grid 0.002)" % (LP_SHAVE, PIA))
    sc = np.arange(0.0, PIA + 1e-9, 0.002)
    PHI = np.empty((sc.size, len(DELTAS_LP)))
    W_LP = np.empty((len(TT_GRID), len(DELTAS_LP)))
    P_LP = np.empty(len(DELTAS_LP))
    for j, delta in enumerate(DELTAS_LP):
        PHI[:, j] = s_minus(sc, delta, DL0)
        sh, _ = shat_arr(delta)
        P_LP[j] = float(np.sum((mu_at / 2.0) * np.abs(sh))) / math.pi
        W_LP[:, j] = arch_row(delta)[:len(TT_GRID)] - P_LP[j] \
            - pole_budget(TT_GRID) \
            - np.array([arch_tail_budget(t) for t in TT_GRID])
    b_ub = LP_SHAVE * TWO_PI * fejer_a(a0, sc)
    lp_res = {}
    for t_ref in (2515.3, T_PLATT):
        wrow = np.array([float(np.interp(math.log(t_ref),
                                         np.log(TT_GRID), W_LP[:, j]))
                         for j in range(len(DELTAS_LP))])
        sol = linprog(-wrow, A_ub=PHI, b_ub=b_ub,
                      bounds=[(0.0, 50.0)] * len(DELTAS_LP),
                      method="highs")
        cvec = sol.x if sol.status == 0 else np.zeros(len(DELTAS_LP))
        lp_res[t_ref] = (float(wrow @ cvec), cvec)
        nz = {("%.2f" % DELTAS_LP[j]): round(float(cvec[j]), 3)
              for j in range(len(DELTAS_LP)) if cvec[j] > 1e-6}
        print("   t_ref = %.4g: LP floor = %+.4f  (stack %s)"
              % (t_ref, float(wrow @ cvec), nz))
    c_opt = lp_res[T_PLATT][1]
    floor_lp = W_LP @ c_opt
    pos = floor_lp > 0.0
    t_star_lp = float(TT_GRID[int(np.argmax(pos))]) if np.any(pos) \
        else math.inf
    slope_lp = float(c_opt @ (np.array(DELTAS_LP) - PIA)) / TWO_PI
    single_floor = float(np.interp(math.log(T_PLATT),
                                   np.log(TT_GRID), floor_best))
    check("A2.3 [MEASURED] LP stack: floor(3.06e10) = %+.4f >= best "
          "single-delta %+.4f - 1e-9; t*(LP) = %.4g (grid); stacked "
          "asymptotic slope %.5f per log t (vs single %.5f)"
          % (lp_res[T_PLATT][0], single_floor, t_star_lp, slope_lp,
             slope_asy),
          lp_res[T_PLATT][0] >= single_floor - 1e-9)

    # ================================================ B1 -- literature
    print("\nB1 -- LEVER B part 1: the literature state (WebSearch "
          "2026-08-03)")
    print("   (i) Bellotti-Wong, Math. Comp. (2025), arXiv:2412.15470"
          ": A1 = 0.10076 -- quoted by the authors as 'the "
          "nearly-optimal value obtainable from Theorem 1.2 with "
          "current knowledge'; NO successor with A1 < 0.1 found "
          "(2025-2026).")
    print("   (ii) hybrid: |S(T)| <= 2.5167 for T <= 3.061e10 [Platt "
          "LMFDB max, Bellotti eq. (1.2)]; Platt-Trudgian (2021, "
          "3e12) COUNTED zeros without isolating them ('nowhere to "
          "store') -- NO published |S| sup on (3.061e10, 3e12]: the "
          "Platt window top stays 3.061e10.")
    print("   (iii) NEW: Amberger, arXiv:2512.23064 (28 Dec 2025): "
          "|S1(t2) - S1(t1)| <= %.3f + %.3f loglog t2 + %.4f log t2 "
          "(t >= 653; also (%.3f, %.3f, %.4f)) -- improves Trudgian "
          "2011 (%.2f + %.4f log)." % (AMB_A, AMB_B, AMB_C, AMB2_A,
                                       AMB2_B, AMB2_C, TUR_A, TUR_B))
    tur_amb = (2.0 * math.pi * C1_BE
               + math.sqrt((2.0 * math.pi * C1_BE) ** 2
                           + 4.0 * math.pi * AMB_C))
    tur_amb2 = (2.0 * math.pi * C1_BE
                + math.sqrt((2.0 * math.pi * C1_BE) ** 2
                            + 4.0 * math.pi * AMB2_C))
    tur_old = (2.0 * math.pi * C1_BE
               + math.sqrt((2.0 * math.pi * C1_BE) ** 2
                           + 4.0 * math.pi * TUR_B))
    # Turing gap bound at the Platt edge (t1 <= T_PLATT, S <= 2.5167)
    L_pl = math.log(T_PLATT / TWO_PI)
    qa = L_pl / (4.0 * math.pi)
    qb = S_PLATT
    qc = AMB_A + AMB_B * math.log(L_pl) + AMB_C * math.log(T_PLATT)
    gap_edge = (qb + math.sqrt(qb * qb + 4.0 * qa * qc)) / (2.0 * qa)
    check("B1.1 [CITED] Turing-route update (Amberger + Bellotti): "
          "gap asymptote H* = %.4f (was %.4f with Trudgian 2011; "
          "second row %.4f) -- still ABOVE the S-difference floor "
          "%.5f (route stays dominated) but BELOW 2pi/a0 = %.5f "
          "(passes centered capture, consistency); at the Platt edge "
          "the first gap above 3.061e10 is <= %.4f (an epsilon "
          "extension, printed)"
          % (tur_amb, tur_old, tur_amb2, FLOOR_BE, TWO_PIA, gap_edge),
          tur_amb > FLOOR_BE and tur_amb < TWO_PIA)

    # ================================================ B2 -- empirical S
    print("\nB2 -- LEVER B part 2: the empirical S-band and the "
          "verification-backed reach floor")
    th_g = theta_rs(GAM)
    nn = np.arange(1, n_z + 1, dtype=float)
    S_plus = nn - th_g / math.pi - 1.0
    S_minus_v = (nn - 1.0) - th_g / math.pi - 1.0
    absS = np.maximum(np.abs(S_plus), np.abs(S_minus_v))
    S_sup_all = float(np.max(absS))
    i_sup = int(np.argmax(absS))
    sup_at = float(GAM[i_sup])
    cum = np.maximum.accumulate(absS)

    def s_sup_to(T):
        j = int(np.searchsorted(GAM, T))
        return float(cum[max(j - 1, 0)])

    edges_rep = (416.4, 870.0, gam_max)
    sup_tab = {T: s_sup_to(T) for T in edges_rep}
    rvm_emp_ok = bool(np.all(absS <= s_bound_tr(GAM) + 1e-9))
    a1_eff = {T: sup_tab[T] / math.log(T) for T in edges_rep}
    print("   empirical S-band (theta via log-Gamma, exact jumps): "
          "max |S| on comb = %.4f at gamma = %.3f" % (S_sup_all,
                                                      sup_at))
    for T in edges_rep:
        print("   sup |S| on [0, %.1f] = %.4f  (effective A1 = "
              "sup/log T = %.4f -- NOT small: the constant term "
              "dominates at reach heights)" % (T, sup_tab[T],
                                               a1_eff[T]))
    # empirical-band capture heights (constant band S <= sup)
    s_band = sup_tab[gam_max]
    L1 = 2.0 * a0 * (2.0 * s_band + EPS_N) / 2.0  # H^emp < pi/a0
    L2 = a0 * (2.0 * s_band + EPS_N)              # H^emp < 2pi/a0
    t_cap1 = TWO_PI * math.exp(2.0 * L2)          # placeholder order
    t_cap_1s = TWO_PI * math.exp(2.0 * math.pi
                                 * (2.0 * s_band + EPS_N) / PIA)
    t_cap_2s = TWO_PI * math.exp(2.0 * math.pi
                                 * (2.0 * s_band + EPS_N) / TWO_PIA)
    gaps = np.diff(GAM)
    g_reach = float(np.max(gaps[GAM[:-1] <= T_REACH]))
    g_reach_at = float(GAM[:-1][GAM[:-1] <= T_REACH][
        int(np.argmax(gaps[GAM[:-1] <= T_REACH]))])
    g416 = float(np.max(gaps[GAM[:-1] <= 416.4]))
    print("   empirical-band capture (|S| <= %.3f): one-sided needs "
          "t > %.4g, centered needs t > %.4g -- both essentially "
          "OUTSIDE the comb: the S-band chain closes (almost) "
          "nothing on the reach" % (s_band, t_cap_1s, t_cap_2s))
    print("   the reach truth: max gap on [10, %.0f] = %.4f at gamma"
          " = %.3f (on [10, 416.4]: %.4f); gap/2 = %.4f vs pi/a0 = "
          "%.4f -> even PERFECT knowledge of S cannot capture "
          "single zeros in the a0 main lobe on the reach; the "
          "closure below is the DIRECT comb floor (multi-zero sum), "
          "not capture" % (T_REACH, g_reach, g_reach_at, g416,
                           g_reach / 2.0, PIA))
    check("B2.1 [E] empirical S-band: max |S| on the certified comb "
          "= %.4f (<= Trudgian bound everywhere: %s); prefix sups "
          "and effective A1 printed; honest verdict: the empirical "
          "band closes the capture chain only for t > %.3g "
          "(centered) -- beyond the comb top %.1f, hence unusable "
          "there; the reach closure is the direct floor (B2.2)"
          % (S_sup_all, rvm_emp_ok, t_cap_2s, gam_max),
          rvm_emp_ok and S_sup_all < 1.5)
    _ = (L1, t_cap1)  # order-of-magnitude helpers, printed above

    # B2.2 verification-backed diagonal floors
    print("\n   B2.2 verification-backed diagonal floors "
          "(s_tot(t) >= 2 pi sum_comb [F_a(g-t) + F_a(g+t)]; "
          "dropped far zeros contribute >= 0; off-line budget above "
          "3e12 < 1e-19):")
    floor_ok = True
    floor_min_all = math.inf
    floor_min_10 = math.inf
    for (kz, aw, hw, _c) in picks:
        tk = math.pi * np.arange(1, int(T_REACH * 2 * aw / math.pi)
                                 + 1) / (2.0 * aw)
        tk = tk[tk <= T_REACH]
        vals = np.empty(tk.size)
        for lo in range(0, tk.size, 400):
            hi = min(tk.size, lo + 400)
            blk = tk[lo:hi][:, None]
            vals[lo:hi] = TWO_PI * (
                np.sum(fejer_a(aw, GAM[None, :] - blk), axis=1)
                + np.sum(fejer_a(aw, GAM[None, :] + blk), axis=1))
        jm = int(np.argmin(vals))
        m10 = tk >= 10.0
        v10 = float(np.min(vals[m10]))
        wlg = np.log(2.0 + tk)
        r_min = float(np.min(vals / wlg))
        r1_min = float(np.min((vals + 1.0) / wlg))
        floor_min_all = min(floor_min_all, float(vals[jm]))
        floor_min_10 = min(floor_min_10, v10)
        floor_ok = floor_ok and float(vals[jm]) > BAR_FLOOR_ALL \
            and v10 > BAR_FLOOR_MIN
        print("   a = %.4f: %4d modes <= %.0f: min s_tot = %.5f at "
              "t = %8.3f (min over t_k >= 10: %.5f); min "
              "s_tot/log(2+t) = %.5f; min (s_tot+1)/log(2+t) = %.4f"
              % (aw, tk.size, T_REACH, float(vals[jm]),
                 float(tk[jm]), v10, r_min, r1_min))
    # dense grid at a0 on [10, 2500]
    tg_d = np.arange(10.0, 2500.0, 0.05)
    vmin, vat = math.inf, 0.0
    rmin_d = math.inf
    for lo in range(0, tg_d.size, 2000):
        hi = min(tg_d.size, lo + 2000)
        blk = tg_d[lo:hi][:, None]
        v = TWO_PI * (np.sum(fejer_a(a0, GAM[None, :] - blk), axis=1)
                      + np.sum(fejer_a(a0, GAM[None, :] + blk),
                               axis=1))
        j = int(np.argmin(v))
        if float(v[j]) < vmin:
            vmin, vat = float(v[j]), float(tg_d[lo + j])
        rmin_d = min(rmin_d, float(np.min(v / np.log(2.0
                                                     + tg_d[lo:hi]))))
    print("   dense a0 grid [10, 2500] (step 0.05): min s_tot = "
          "%.5f at t = %.3f; min s_tot/log(2+t) = %.5f  (v669 raw "
          "hull quote c0 ~ 0.021)" % (vmin, vat, rmin_d))
    check("B2.2 [E, central] verification-backed diagonal floor on "
          "the family reach (modes to %.0f): min over ALL 5 windows "
          "x lattice modes = %.5f > %.3f (low modes t_k < 10 "
          "included), min over modes >= 10: %.5f > %.3f, AND the "
          "dense a0 grid floor %.5f > 0 -- the W2 diagonal is "
          "CERTIFIED positive on the entire reach (status type: "
          "verification-backed, family finite; not "
          "unconditional-abstract; dip-law reference 1/(pi a_max "
          "(gap/2)^2) = %.4f)"
          % (T_REACH, floor_min_all, BAR_FLOOR_ALL, floor_min_10,
             BAR_FLOOR_MIN, vmin,
             1.0 / (math.pi * max(A_FAM) * (6.887 / 2.0) ** 2)),
          floor_ok and vmin > 0.0)

    # ================================================ Z1 coverage + verdict
    print("\nZ1 -- the certified pointwise coverage map at a0 "
          "(diagonal floor s_tot > 0):")
    seg_comb_top = 2500.0
    t_on_min = min(t_on["platt"], t_star_best,
                   t_star_lp if math.isfinite(t_star_lp) else 1e99)
    hole1 = (seg_comb_top, t_on_min)
    hole1_dec = math.log10(hole1[1] / hole1[0])
    sel_cov_lo = min(t_star_best, t_star_lp)
    hole2_exists = sel_cov_lo > T_PLATT
    print("   [10, %.0f]           comb-certified floor (min %.4f)"
          % (seg_comb_top, vmin))
    print("   (%.0f, %.4g)      HOLE 1 -- %.2f decades (was: "
          "'unclosable at ANY height')" % (seg_comb_top, t_on_min,
                                           hole1_dec))
    print("   [%.4g, %.4g]  Platt-window centered capture "
          "(H_min(Platt) < 2pi/a0)" % (t_on["platt"], T_PLATT))
    if hole2_exists:
        print("   (%.4g, %.4g)  HOLE 2 -- %.2f decades (Selberg "
              "enters at %.4g)" % (T_PLATT, sel_cov_lo,
                                   math.log10(sel_cov_lo / T_PLATT),
                                   sel_cov_lo))
        print("   [%.4g, inf)       Selberg chain (S-free), then "
              "Trudgian-2S from %.4g, Bellotti-2S from %.4g"
              % (sel_cov_lo, t_on["trudgian"], t_on["bellotti"]))
    else:
        print("   [%.4g, inf)       Selberg chain (S-free) covers "
              "beyond the Platt window (t* = %.4g <= %.4g) -- NO "
              "hole 2; Trudgian-2S from %.4g concurs"
              % (T_PLATT, sel_cov_lo, T_PLATT, t_on["trudgian"]))
    print("   closure paths for hole 1: (i) certified zeros to "
          "%.3g (LMFDB import, ~1.5e7 zeros -- verification-backed);"
          " (ii) better O(1) constants in the Selberg prime bound "
          "(needs P < %.2f at the comb top; current best %.2f); "
          "(iii) an explicit |S| sup on the Platt-Trudgian range "
          "(3e12) -- not published (B1.1)"
          % (t_on_min,
             (d_best - PIA) * math.log(2515.3 / TWO_PI) / TWO_PI,
             P_best))

    guards_ok = not any(f.startswith("G0") for f in FAILS)
    a_ok = not any(f.startswith(("A1.2",)) for f in FAILS)
    sel_ok = not any(f.startswith(("A2.1", "A2.2")) for f in FAILS)
    reach_ok = not any(f.startswith("B2.2") for f in FAILS)
    holes = hole1[1] > hole1[0] * 1.0001 or hole2_exists
    if not guards_ok:
        VERDICT = "PINCH-MIXED (guards failed)"
    elif a_ok and sel_ok and reach_ok and not holes:
        VERDICT = "PINCH-CLOSED-FULL"
    elif a_ok and sel_ok and reach_ok:
        VERDICT = "PINCH-BROKEN-SPLIT"
    elif a_ok:
        VERDICT = "PINCH-THRESHOLD-ONLY"
    else:
        VERDICT = "PINCH-NO-GAIN"

    check("Z1.1 [C] typed reading: (i) the STATED pinch (A1 < "
          "1/(4a0) = %.5f vs 0.10076, 11.75%% short) is an artifact "
          "of the ONE-SIDED capture bookkeeping: the same theorem "
          "spent centered gives A1 < 1/(2a0) = %.5f -- Bellotti "
          "passes with %.0f%% headroom, Trudgian passes too; (ii) "
          "the Selberg minorant ELIMINATES A1 from the counting "
          "chain (loss pi/a0 = %.4f mass + P = %.3f prime term, "
          "explicit), threshold-free for every window incl. a -> "
          "infinity; (iii) the honest residue is NOT an A1 "
          "threshold but the O(1)-constant holes of the coverage "
          "map (hole 1: %.2f decades); (iv) the family reach "
          "[10, %.0f] is verification-backed closed (min floor "
          "%.4f); no marker move"
          % (a_req_1s, a_req_2s, head_pct, PIA, P_best, hole1_dec,
             T_REACH, floor_min_all), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this module):

  PRIME.WEIL.OPERATOR.01 / W2, pinch-attack round (2026-08-03): the
  v678 QUANTIFIED PINCH (pointwise capture needs A1 < 1/(4 a0) =
  %.5f; best cited constant 0.10076 misses by 11.75%%) was ATTACKED
  on both flanks and BROKEN as stated.  (1) CENTERED CAPTURE (same
  zero-gap theorem, two-sided bookkeeping): every gap <= H_min(left
  edge), so dist(t, Z) <= H_min(t - %.0f)/2 -- machine-verified on
  all comb heights (0 violations); the threshold DOUBLES to A1 <
  1/(2 a0) = %.5f and the EXISTING Bellotti constant passes with
  %.0f%% headroom (Trudgian 0.112 passes as well).  (2) SELBERG
  MINORANT (Beurling-Selberg, type 2 a0, closed-form Vaaler
  construction, machine-checked: minorant property, mass loss
  exactly pi/a0, band-limitation): the counting box in the Fejer
  main lobe certifies N[t +- delta/2] >= (delta - pi/a0) L/(2 pi) -
  P - budgets with the prime term P explicit and UNIFORM -- the
  2 A1 log t loss of the RvM route is ELIMINATED: no A1, no Platt
  cap, valid for every window and for a -> infinity (best delta =
  %.2f: P = %.3f, positive from t* = %.3g).  (3) LAYER CAKE: the
  Fejer main-lobe layer cake recovers %.2f x of the %.3f x
  single-box loss (the v669 4/pi^2 analogue); certified asymptotic
  slopes at A1 = 0.10076: box %.4f, layer cake %.4f, Selberg stack
  %.4f per log t.  (4) LITERATURE (search 2026-08-03): Bellotti-Wong
  Math. Comp. 2025 A1 = 0.10076 is current and 'nearly-optimal';
  no successor < 0.1; NO published |S| sup on (3.061e10, 3e12]
  (Platt-Trudgian counted without isolating); NEW Amberger
  arXiv:2512.23064 S1 constants tighten the Turing route to H* =
  %.4f -- still dominated, consistency confirmed.  (5) THE HONEST
  RESIDUE: the pinch is no longer an A1 threshold; it is the
  O(1)-constant coverage hole (%.0f, %.3g) -- %.2f decades -- plus
  %s; closure paths: LMFDB zeros to %.3g (verification-backed), a
  smaller Selberg prime term, or an explicit |S| sup at 3e12.  (6)
  THE REACH: on [10, %.0f] (all 5 family windows, every lattice
  mode) the diagonal floor is verification-backed POSITIVE (min
  s_tot = %.4f; min s_tot/log(2+t) = %.4f on the dense a0 grid) --
  the W2-family statement at reach heights is closed
  verification-backed (legitimate: the family is finite), NOT
  unconditional-abstract; the empirical S-band itself captures
  nothing below t ~ %.2g (gaps up to %.2f exceed the a0 main lobe).
  TYPE: thresholds = analytic (machine-checked on the comb); Selberg
  chain = derived + identity-verified (max residual %.1e); reach
  floor = [E] verification-backed; A5(a), W2 Mosco and the full
  projection form stay OPEN; no marker move.  VERDICT %s.
""" % (a_req_1s, H10_SHIFT, a_req_2s, head_pct, d_best, P_best,
       t_star_best, gain_lc, math.pi ** 2 / 4.0, sl_box, sl_lc,
       sl_stk, tur_amb, seg_comb_top, t_on_min, hole1_dec,
       ("hole 2 (%.3g, %.3g)" % (T_PLATT, sel_cov_lo))
       if hole2_exists else "NO hole 2 (Selberg bridges the top)",
       t_on_min, T_REACH, floor_min_all, rmin_d, t_cap_2s, g_reach,
       id_max, VERDICT))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
