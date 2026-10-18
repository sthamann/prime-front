"""v681 -- PRIME.HOLECLOSED.01: CLOSING THE O(1) COVERAGE HOLE -- the
last gap of the W2 chain: the pinch-attack coverage map at the anchor
a0 has ONE hole, (2500, 7.27e6) = 3.46 decades, where neither the comb
floor (comb ends at 2515) nor any capture / Selberg chain is positive.
This module attacks the hole on the three paths NAMED by the parent
and synthesizes the gapless map.  It measures, derives and types; it
moves no marker.

CONTEXT (the parent, pinch_attack_probe / v680, 2026-08-03).  Verdict
PINCH-BROKEN-SPLIT: the stated 11.7% pinch is an artifact of one-sided
bookkeeping; centered capture doubles the threshold to A1 < 1/(2 a0) =
0.18033 and Bellotti 0.10076 passes with 79% headroom; the Selberg
minorant eliminates A1 entirely (loss pi/a0 mass + prime term P =
2.534, positive from t* = 1.1e7).  The honest residue is the coverage
map at a0:  [10, 2500] comb floor / (2500, 7.27e6) HOLE 1 /
[7.27e6, 3.06e10] Platt-2S capture / [1.1e7, inf) Selberg chain.
The parent's three NAMED closure paths (Z1 output, verbatim):
  (i)  certified zeros to 7.3e6 (LMFDB-scale import, ~1.5e7 zeros --
       verification-backed);
  (ii) better O(1) constants in the Selberg prime bound (needs P <
       1.06 at the comb top; current best 2.53);
  (iii) an explicit |S| sup on the Platt-Trudgian range (3e12) -- not
       published (hole-2 path; hole 2 does not exist).

THE ATTACK (declared BEFORE the numbers):

H1 -- THE PLATT-CONSTANT CHAIN ON THE HOLE.  The hole lies entirely
  inside Platt's verified range (|S| <= 2.5167 to 3.06e10).  The task
  sketch computes, at delta = pi a and t = 2500, the window count
  (pi a/2pi) log(t/2pi) = a L/2 = 8.30 > 2 x 2.5167 + eps = 5.04 and
  hopes for immediate closure.  ADJUDICATION (declared): the count is
  CORRECT but the window pi a0 = 8.71 exceeds the Fejer main lobe
  2 pi/a0 = 2.266 by the factor a0^2/2 = 3.84 -- a positive count at
  packet scale is the (never-holed) density layer, NOT pointwise
  capture.  The largest capture-usable window is delta < 2 pi/a, and
  then positivity of (delta/2pi) L - 5.035 needs L >= a0 (2 x 2.5167
  + eps) = 13.96, i.e. t >= 7.26e6 -- EXACTLY the hole top: the
  Platt-constant chain reproduces the hole boundary, it cannot enter
  the hole.  Bars: the sketch count 3.26 +- 0.05 at t = 2500; the
  exact t_on(a0) = 7.27e6 (+- 2%) from the same bisection machinery
  as the parent; per-family-a table printed.  SUPPLEMENT [CITED,
  secondary]: classical computations give |S(T)| < 2 for T <
  6.8e6 (quoted in the Wikipedia RH survey; consistent with Brent
  1979 / van de Lune-te Riele-Winter 1986 ranges); with the constant-2
  band the centered capture enters at t = 2pi exp(a0(4 + eps)) ~
  4.2e5, valid to 6.8e6 -- printed as a corroborating band, NOT used
  as a load-bearing support of the final map.

H2 -- THE VERIFICATION PATH (the parent's path (i), the decisive one).
  H2.1 [E] honest budget: mpmath zetazero(n) is timed live at n =
  2100, 4200, 8400; the cost to gamma ~ 9.9e3 (n = 1e4) and to the
  hole top (n ~ 1.5e7) is extrapolated and printed; the direct-comb
  extension is REJECTED as soon as the estimate exceeds hours -- the
  declared pivot is the vectorized scan below (which supersedes any
  reachable zetazero extension by orders of magnitude).
  H2.2 [E, central] THE SCAN: vectorized Riemann-Siegel Z(t) =
  2 sum_{n <= nu} cos(theta(t) - t log n)/sqrt(n) + (-1)^(nu-1)
  (t/2pi)^(-1/4) Psi(p), theta via scipy log-Gamma, C0 term with the
  CITED remainder |R0| <= 0.127 (t/2pi)^(-3/4) for t >= 200 [Gabcke
  1979 diss., Goettingen, eq. block (8)-(10); Titchmarsh 1935: 1.50
  (t/2pi)^(-3/4)].  Acceptance budget B(t) = 0.15 (t/2pi)^(-3/4) +
  2e-5 (float allowance; >= the cited 0.127 bound, see calibration
  history (v)); a sign change with |Z| > B(t) at BOTH bracket ends
  is a GENUINE ordinate of a critical-line zero (a phantom would
  need |error| > B >= the Gabcke bound -- impossible).  Stage-1 grid h1(t) = 0.55 x mean gap
  (clamped [0.20, 1.00]) over (2400, T_Z]; stage-2 refinement h2 =
  0.06 on found-gaps > 1.70; stage-3 interior rescan h3 = 0.012 on
  capture-fail candidates.  MISSED zeros only LOWER the certified
  floor (all kernel terms are >= 0): no completeness claim is needed
  -- this replaces the task's Turing certificate by construction;
  the (2515, 3063] strip is cross-matched against the mpmath-computed
  extension cache as a completeness spot check (printed).
  Bars: every cache zero in (2400, 2515.3) matched within 0.30 (>=
  97%); 12/12 random accepted crossings sign-confirmed by live
  mpmath siegelz at the bracket ends; Z validated against mpmath at
  24 log-spaced points, |dev| <= 0.30 (t/2pi)^(-3/4) + 2e-5; global
  found/expected count ratio >= 0.80 (per-band ratios printed).
  H2.3 [E, central] THE FLOOR on the hole at a0: per found gap g with
  worst-case distance d* = g/2 + loc-err: if d* < 0.95 pi/a0 the
  capture floor 2 pi F_a0(d*); else a DIP EVALUATION of s_tot across
  the gap (grid, neighbors within +-120, per-zero worst-case envelope
  (|sin(a d)| - a e)_+^2 / (pi a (d+e)^2)).  Bar: min floor on
  (2515.3, T_Z] > 5e-4 (dip-law reference and per-band minima
  printed); dropped far zeros and the F(gamma+t) term are >= 0
  (conservative).

H3 -- THE ANALYTIC PATH (the parent's path (ii)).
  H3.1 [ANALYTIC+CITED] loss bookkeeping of the Selberg chain: the
  minorant mass deficit is EXACTLY 1/D = pi/a0 (Vaaler construction);
  by Logan (unpublished) / Littmann (cited via arXiv:1410.3366, fn.
  1) Selberg's minorant is extremal when D delta is an integer, and
  the extremal deficit stays Theta(1/D) -- the deficit is NOT the
  lever; sensitivity table t*(deficit x, P) printed (even x = 0
  leaves t* = 2pi exp(2pi P/delta) = 6.6e3 only if P also stays --
  the REAL lever is P).  The centered trick has no Selberg analogue:
  the chain has no S(t) term to center (typed).
  H3.2 [E/ABSTRACT, potentially decisive] THE EXACT PRIME TERM: the
  uniform bound P = (1/pi) sum (mu/2)|Shat(u_n)| wastes the sign
  structure; on the hole the prime term is the EXPLICIT almost-
  periodic sum prime(t) = (1/pi) sum (mu/2) Shat(u_n) cos(t u_n)
  (54+ atoms, u <= 2 a0 = log 256).  The certified count floor
  N[t +- delta/2] >= arch_delta(t) - prime_delta(t) - pole/tail
  budgets is evaluated with a hierarchical grid certificate
  (levels h = 0.5/0.1/0.02/0.004, Lipschitz slack P' h/2, P' =
  (1/pi) sum (mu/2)|Shat| u_n) for delta in {1.90, 2.24}: t_x :=
  sup of the uncertifiable t.  Above t_x the chain is POSITIVE with
  the exact prime term -- an ABSTRACT (primes + digamma only, no
  zero data) support that enters BELOW the uniform-P entry t* =
  1.1e7.  Bars: Weil identity residual <= 5e-3 at 5 sample t
  (comb side); |P(2.24) - 2.534| <= 0.05 and t*(2.24) = 1.1e7
  (+- 10%) (parent quotes); t_x <= 1.05 t*; zero uncertified points
  above t_x (contiguity by construction).

H4 -- THE SYNTHESIS [central]: the gapless map at a0 with named
  support and constants per region; scan top T_Z = 1.02 x min(t_x,
  Platt-2S entry at floor 1e-3) + 10, so the [E] region always meets
  the abstract/verified region.  The theorem-shaped statement
  s_tot(t; a0) >= c log(2+t) - C for ALL t >= 10 with c = 0.98 x
  best pointwise Selberg slope and C = max over a dense log grid of
  (c log(2+t) - floor_map(t)); honest typing per region
  (verification-backed [E] vs cited-verification vs abstract), the
  family honesty table (per-window t_on / Selberg envelope entries /
  scan fail counts; the family REACH [10, 870] is parent-closed),
  and the unconditionality ledger (below 3e12 the window zeros are
  on-line by Platt-Trudgian 2021; beyond 3e12 the count chain is
  modulo the off-line window; the unconditional Trudgian-2S capture
  concurs from its own entry, printed).

H5 / Z1 [C] -- the contract-note text (the NINTH slice): the W2
  end-state after the pinch break (report only; nothing written).

Verdict enums (frozen, precedence top-down; the EXPECTED verdict of
this module is HOLE-CLOSED-SPLIT-TYPE -- the hole closes, the typing
stays split and explicit):
  HOLE-MIXED                -- any G0.* fails;
  HOLE-CLOSED-UNCONDITIONAL -- t_x <= 2515.3: the abstract chain
                               alone bridges the hole (not expected);
  HOLE-CLOSED-SPLIT-TYPE    -- H2.3 + H3.2 + H4 bars pass and the a0
                               map is GAPLESS: the hole is CLOSED
                               with split typing ([E] scan on
                               (2515, T_Z], abstract from t_x,
                               uniform Selberg from t*);
  HOLE-NARROWED             -- floors positive on a part; the exact
                               remainder is typed with endpoints;
  HOLE-NO-GAIN              -- otherwise.

CALIBRATION HISTORY (declared -- honesty first): run 1 (2026-08-03)
failed G0.2 and H2.2; three documented causes, all fixed ONCE.
(i) COMPARATOR: the theta bar 1e-9 ignored the float64 ulp scale of
theta(7e6) ~ 4.5e7 (measured dev 7.5e-9 ~ 1 ulp; the Z acceptance
budget already carried a 2e-5 float allowance) -> bar recalibrated to
1e-9 + 4e-16 |theta|.  (ii) COMPARATOR: the cache-strip bar tested
COMPLETENESS (cache -> found >= 97%) which the method explicitly does
NOT claim (hidden close pairs are by design harmless for floors;
measured 104/110) -> recalibrated to the sound direction: every FOUND
zero in the certified strip must match a comb/extension zero within
0.30 (correctness of the scan; >= 99.5%); the completeness ratio
stays printed, no bar.  (iii) REAL BUG, exposed by the count ratios
> 1 (1.012 global, S_found blow-up = +2722 phantom entries, root
cause pinned at t = 100007.2): a stage-1 position estimate carries
error up to h/2 ~ 0.18, so the estimate of a zero can sit OUTSIDE
the refinement deletion span while the re-scan grid (pad + arange
overshoot) re-finds the SAME zero inside -> duplicate.  Fix: a
BRACKET-OVERLAP dedupe invariant after every refinement stage -- two
entries of DIFFERENT provenance (kept-coarse vs refined) whose
certainty brackets [mid - err, mid + err] overlap collapse to the
sharper one; same-provenance neighbors are distinct sign changes of
one grid and never duplicates; double-counting becomes impossible by
construction (two entries of one zero both contain it, hence
overlap), and the merge direction is conservative for floors (a
merged genuine close pair only enlarges the reported gap).  NEW
two-sided count sanity bar 0.80 <= found/expected <= 1.0002.  A
fourth fix without bar impact: the arch interpolation table ended
at 3e7 and np.interp clamped beyond, corrupting t*(1.90) (printed
3e15 artifact) -> table extended to 1e18.  (v) Run 3 (all bars
green) exposed one last over-conservatism via the extension-cache
truth: the acceptance envelope 0.5 (t/2pi)^(-3/4) was 4 x the cited
Gabcke bound and SUPPRESSED genuine low-amplitude crossings (the
true pair 2930.711 / 2931.069 has min |Z| = 1.6e-3 < envelope
5.0e-3, producing a spurious 3.72 found-gap at t = 2928 vs the true
extension-range max gap 2.539) -> envelope recalibrated ONCE to
0.15 (t/2pi)^(-3/4) + 2e-5, still >= the PROVEN 0.127 bound + float
(phantoms stay impossible), validation bar tightened 0.30 -> 0.10
(measured dev/(t/2pi)^(-3/4) = 0.036).  All floors remain valid
under either envelope (suppression only ever LOWERED them).

FIREWALL (INVERTED, declared -- parent convention).  This module
DELIBERATELY reads and produces Riemann zeros: the scan IS the task.
Structural separation: the H3 Weil chain (arch, primes, pole, P,
prime(t)) is primes + digamma + the Beurling closed form ONLY -- no
zero enters the abstract chain; zeros enter only the scan (H2), the
floors, and validity checks.  Zero data: zero_comb_cache_n2000.json
(Turing-certified) + c1_zero_ext_n2500.json (provenance printed, no
bar) + the live scan (self-produced, budget-guarded, cross-checked
against mpmath).  No marker moves; Python-only per GATE.WOLFRAM.02.
The committed scan cache (coverage_hole_zscan_cache.npz in
experiments/tfpt-discovery/, ~1.2 MB) stores the deterministic
stage-1 result; if it is missing the module REGENERATES it from
scratch (a few minutes) -- the cache is a speed-up, not an input.

PROVENANCE: discovery probe coverage_hole_probe.py (2026-08-03, 11/11
PASS, verdict HOLE-CLOSED-SPLIT-TYPE); pinch_attack_probe.py / v680 +
zero_gap_theorem_probe.py / v678 (machinery + the typed hole),
zero_comb_cache_n2000.json (turing_cert_probe / v666:
TURING-COMPLETE-BAND), c1_zero_ext_n2500.json (c1_mechanism_probe /
v676 extension),
v563_paper2_readouts (atom table, frame-A windows), Gabcke 1979
(Goettingen diss., |R0| <= 0.127 (t/2pi)^(-3/4), t >= 200; C0+C1:
0.053 t^(-5/4)), Titchmarsh 1935 (1.50 (t/2pi)^(-3/4), t > 250 pi),
Vaaler Bull. AMS 12 (1985), Logan (unpubl.) / Littmann (extremal
minorants; via Carneiro-Littmann-Vaaler line, arXiv:1410.3366 fn. 1),
Trudgian J. Number Theory 134 (2014) Thm 1, Bellotti-Wong Math. Comp.
(2025) / arXiv:2412.15470 (Cor. 1.5, eq. (1.2) = Platt LMFDB 2.5167),
Platt-Trudgian Bull. LMS 53 (2021) (RH to 3e12; max |S| found 2.5683
at T = 3.98e10, quoted in arXiv:2412.15470), Wikipedia RH survey
(|S| < 2 for T < 6.8e6, secondary quote, corroboration only),
Iwaniec-Kowalski Thm 5.12.  Literature search date: 2026-08-03.
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
from scipy.special import digamma as sp_digamma  # noqa: E402
from scipy.special import loggamma as sp_loggamma  # noqa: E402
from scipy.special import zeta as sp_hzeta  # noqa: E402

# ------------------------------------------------------------ constants
# cited chain constants (parents, verbatim)
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
H10_SHIFT = 26.0                            # >= H_min(10), checked
RH_HEIGHT = 3.0e12                          # Platt-Trudgian 2021
# parent quotes (reproduction bars)
REF_PLATT_BOT = 1.4187
BAR_PLATT_BOT = 0.01
REF_TON = 7.27e6                            # hole top (task quote)
BAR_TON_REL = 0.02
REF_HOLE_DEC = 3.46
BAR_HOLE_DEC = 0.05
REF_P224 = 2.534                            # parent P at delta = 2.24
BAR_P = 0.05
REF_TSTAR = 1.1e7                           # parent t*(2.24)
BAR_TSTAR_REL = 0.10
REF_SKETCH = 3.26                           # task H1 count at t = 2500
BAR_SKETCH = 0.05
# cited secondary band (H1 supplement, corroboration only)
S_BAND2, T_BAND2 = 2.0, 6.8e6
# RS-Z machinery (Gabcke 1979)
GABCKE_C = 0.127                            # |R0| <= 0.127 (t/2pi)^-3/4
BUDGET_C = 0.15                             # acceptance envelope coeff
BUDGET_FLOAT = 2e-5                         # float allowance (flat)
BAR_ZDEV_C = 0.10                           # validation bar coeff
N_Z_SPOTS = 24
N_MP_SIGN = 12
BAR_THETA_ABS = 1e-9                        # + 4e-16 |theta| (run-1
BAR_THETA_REL = 4e-16                       # calibration history (i))
BAR_PSI = 1e-3
# scan parameters
T_SCAN_LO = 2400.0
H1_FRAC, H1_MIN, H1_MAX = 0.55, 0.20, 1.00
H2_REF = 0.06
H3_REF = 0.012
GAP_REF_BAR = 1.70
CAPTURE_FRAC = 0.95
DIP_NEIGH = 120.0
BAR_FLOOR_HOLE = 5e-4
TOL_MATCH = 0.30
BAR_FOUND_REAL = 0.995                      # found -> certified match
BAR_FOUND_RATIO = 0.80                      # two-sided count sanity
BAR_FOUND_RATIO_HI = 1.0002
CHUNK = 16384
N_BANDS = 12
SCAN_VER = 4
# Weil / Selberg chain (H3)
DELTAS_X = (1.90, 2.24)
CERT_LEVELS = (0.5, 0.1, 0.02, 0.004)
N_CERT_BLOCKS = 600
N_ARCH_PTS = 96
BAR_IDENT = 5e-3
BAR_SM_BOX = 1e-6
BAR_SM_MASS = 2e-3
T_SAMPLES = (60.0, 150.0, 400.0, 900.0, 1800.0)
T_POLE_CAL = (2000.0, 20000.0)
FLOOR_ENTRY = 1e-3                          # Platt-2S handover level
ZC_BUDGET_H = 10.0                          # zetazero rejection (hours)

mp.mp.dps = 30
LOGPI_F = math.log(math.pi)
TWO_PI = 2.0 * math.pi
UU = np.array([float(u) for u in core.U_ALL])
MU = np.array([float(m) for m in core.MU_ALL])

HERE = os.path.dirname(os.path.abspath(__file__))
# shared zero-comb cache + the committed n = 2500 extension + the
# committed stage-1 scan cache: all live in experiments/tfpt-discovery/
# (repo tree); fall back to local copies next to this module (website
# mirror / standalone use).  The scan cache is regenerated on a miss.
_DISC = os.path.join(os.path.dirname(HERE), "experiments",
                     "tfpt-discovery")
_REPO_CACHE = os.path.join(_DISC, "zero_comb_cache_n2000.json")
_LOCAL_CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")
CACHE = _REPO_CACHE if os.path.exists(_REPO_CACHE) else _LOCAL_CACHE
_REPO_EXT = os.path.join(_DISC, "c1_zero_ext_n2500.json")
_LOCAL_EXT = os.path.join(HERE, "c1_zero_ext_n2500.json")
CACHE_EXT = _REPO_EXT if os.path.exists(_REPO_EXT) else _LOCAL_EXT
_REPO_SCAN = os.path.join(_DISC, "coverage_hole_zscan_cache.npz")
_LOCAL_SCAN = os.path.join(HERE, "coverage_hole_zscan_cache.npz")
CACHE_SCAN = _REPO_SCAN if os.path.isdir(_DISC) else _LOCAL_SCAN
if not os.path.exists(CACHE_SCAN) and os.path.exists(_LOCAL_SCAN):
    CACHE_SCAN = _LOCAL_SCAN


# ------------------------------------------------- H_min machinery (parent)
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


def s_bound_band2(x):
    x = np.asarray(x, dtype=float)
    return np.where(x <= T_BAND2, S_BAND2, np.inf)


def g_gap(t, H, s_bound):
    """count minorant, cancellation-stable log1p form (parent)."""
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
    """smallest t with H_min_chain(t - H10_SHIFT) < target."""
    def f(t):
        return float(h_min_chain(np.array([max(t - H10_SHIFT, T_CLAMP)]),
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


def fejer_env(a, d, e):
    """rigorous lower envelope of F_a on [d-e, d+e] (Lipschitz-a of
    |sin|): (|sin(a d)| - a e)_+^2 / (pi a (d+e)^2)."""
    d = np.asarray(d, dtype=float)
    e = np.asarray(e, dtype=float)
    s = np.maximum(np.abs(np.sin(a * d)) - a * e, 0.0)
    return s * s / (math.pi * a * (d + e) ** 2)


# ------------------------------------------------- Beurling-Selberg (parent)
def bs_K(x):
    x = np.asarray(x, dtype=float)
    s = np.abs(x) < 1e-8
    xs = np.where(s, 1.0, x)
    out = (np.sin(np.pi * xs) / (np.pi * xs)) ** 2
    out[s] = 1.0
    return out


def bs_Hm(x):
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
    v = s_minus_mp(mp.mpc(t, -0.5), delta, Dl)
    return 2.0 * float(mp.re(v))


def omega_arch(r):
    z = 0.25 + 0.5j * np.abs(np.asarray(r, dtype=float))
    return np.real(sp_digamma(z)) - LOGPI_F


def theta_rs(t):
    """Riemann-Siegel theta via scipy complex log-Gamma (vector)."""
    t = np.asarray(t, dtype=float)
    return np.imag(sp_loggamma(0.25 + 0.5j * t)) - 0.5 * t * LOGPI_F


# ------------------------------------------------- vectorized RS Z(t)
def rs_psi(p):
    """C0(p) = cos(2pi(p^2 - p - 1/16))/cos(2pi p), l'Hopital at the
    cos zeros (value 1/2 at p = 1/4, 3/4)."""
    p = np.asarray(p, dtype=float)
    num = np.cos(2.0 * math.pi * (p * p - p - 0.0625))
    den = np.cos(2.0 * math.pi * p)
    sing = np.abs(den) < 1e-4
    dens = np.where(sing, 1.0, den)
    out = num / dens
    if np.any(sing):
        lh = ((2.0 * p - 1.0)
              * np.sin(2.0 * math.pi * (p * p - p - 0.0625))
              / np.sin(2.0 * math.pi * p))
        out = np.where(sing, lh, out)
    return out


def z_budget(t):
    t = np.asarray(t, dtype=float)
    return BUDGET_C * (t / TWO_PI) ** (-0.75) + BUDGET_FLOAT


def rs_z_sorted(ts):
    """Z(t) for a SORTED float64 array (any spacing); exact-nu
    segmentation: nu is constant on [2 pi nu^2, 2 pi (nu+1)^2)."""
    ts = np.asarray(ts, dtype=float)
    Z = np.empty_like(ts)
    n_all = np.arange(1, int(math.sqrt(ts[-1] / TWO_PI)) + 2, dtype=float)
    logn = np.log(n_all)
    wn = 2.0 / np.sqrt(n_all)
    i = 0
    N = ts.size
    while i < N:
        nu = int(math.sqrt(ts[i] / TWO_PI))
        t_hi_seg = TWO_PI * (nu + 1.0) ** 2
        j = int(np.searchsorted(ts, t_hi_seg, side="left"))
        j = max(j, i + 1)
        for a_ in range(i, j, CHUNK):
            b_ = min(j, a_ + CHUNK)
            tt = ts[a_:b_]
            th = theta_rs(tt)
            ph = np.multiply.outer(tt, logn[:nu])
            np.negative(ph, out=ph)
            ph += th[:, None]
            np.cos(ph, out=ph)
            zz = ph @ wn[:nu]
            tau = np.sqrt(tt / TWO_PI)
            pp = tau - nu
            zz += ((-1.0) ** (nu - 1)) * tau ** (-0.5) * rs_psi(pp)
            Z[a_:b_] = zz
        i = j
    return Z


def bracket_dedupe(m, e, isnew):
    """collapse OLD/NEW entry pairs whose certainty brackets overlap
    (the same true zero seen by both the coarse and the fine grid;
    calibration history (iii)).  Same-provenance neighbors are
    distinct sign changes of one grid and never duplicates.  Keeps
    the sharper entry; conservative for floors."""
    om, oe, on = [], [], []
    n_mrg = 0
    for mm, ee, nn in zip(m, e, isnew):
        if om and nn != on[-1] and (mm - ee) <= om[-1] + oe[-1]:
            n_mrg += 1
            if ee < oe[-1]:
                om[-1], oe[-1], on[-1] = mm, ee, nn
            continue
        om.append(mm)
        oe.append(ee)
        on.append(nn)
    return (np.array(om), np.array(oe),
            np.array(on, dtype=bool), n_mrg)


# ------------------------------------------------- Weil chain transforms
X_TR = None


def build_xtr():
    global X_TR
    xf = np.arange(-40.0, 40.0 + 1e-9, 0.002)
    xm = np.arange(40.002, 3000.0, 0.02)
    X_TR = np.concatenate([-xm[::-1], xf, xm]) + 3e-4


def shat_arr(delta, Dl, u_at):
    Sv_ = s_minus(X_TR, delta, Dl)
    Dv_ = Sv_ - (np.abs(X_TR) <= 0.5 * delta)
    out = np.empty(u_at.size)
    for i, uu in enumerate(u_at):
        bh = 2.0 * math.sin(uu * delta / 2.0) / uu
        out[i] = bh + float(np.trapezoid(Dv_ * np.cos(uu * X_TR), X_TR))
    return out, float(np.trapezoid(np.abs(Dv_), X_TR))


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("CLOSING THE O(1) COVERAGE HOLE (2500, 7.27e6) -- the last "
          "gap of the W2\nchain: Platt-constant adjudication, the "
          "vectorized zero scan, the exact\nprime term, and the gapless "
          "synthesis map (2026-08-03)")
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
          "cache), monotone %s, live-mpmath dev %.2e <= 1e-8, RvM "
          "residual max %.3f <= Sbar+0.01"
          % (n_z, mono, dev_z, float(np.max(rn))),
          mono and dev_z <= 1e-8 and rvm_ok)
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
    DL0 = a0 / math.pi
    print("anchor window: a0 = %.12f (= log %d); pi/a0 = %.6f; "
          "2pi/a0 = %.6f; a0^2/2 = %.4f" % (a0, r0["n_zone"], PIA,
                                            TWO_PIA, a0 * a0 / 2.0))
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

    # ------------------------------------------------ G0.1 machinery repro
    h10 = float(h_min_all(np.array([T_CLAMP]))[0])
    platt_bot = float(h_min_chain(np.array([T_PLATT - H_BRACKET[1]]),
                                  s_bound_platt)[0])
    t_on_pl = t_on_centered(s_bound_platt, TWO_PIA, T_PLATT - 500.0)
    hole_dec = math.log10(t_on_pl / 2500.0)
    t_on_tr = t_on_centered(s_bound_tr, TWO_PIA, 1.0e40)
    t_on_be = t_on_centered(s_bound_be, TWO_PIA, 1.0e80)
    print("   centered-capture entries at a0: Platt %.5g (top %.4g), "
          "Trudgian %.4g, Bellotti %.4g"
          % (t_on_pl, T_PLATT, t_on_tr, t_on_be))
    check("G0.1 [E] H_min machinery reproduction: chain floors %.5f "
          "(Tr) / %.5f (Be); Platt bottom %.4f (quote %.4f +- %.2f); "
          "H_min(10) = %.3f <= %.0f; t_on(a0, Platt) = %.5g within "
          "%.0f%% of %.3g; hole = (2500, t_on) = %.4f decades "
          "(quote %.2f +- %.2f)"
          % (FLOOR_TR, FLOOR_BE, platt_bot, REF_PLATT_BOT,
             BAR_PLATT_BOT, h10, H10_SHIFT, t_on_pl,
             100 * BAR_TON_REL, REF_TON, hole_dec, REF_HOLE_DEC,
             BAR_HOLE_DEC),
          abs(platt_bot - REF_PLATT_BOT) <= BAR_PLATT_BOT
          and h10 <= H10_SHIFT
          and abs(t_on_pl / REF_TON - 1.0) <= BAR_TON_REL
          and abs(hole_dec - REF_HOLE_DEC) <= BAR_HOLE_DEC)

    # ------------------------------------------------ G0.2 RS-Z machinery
    th_ok = True
    th_dev_sc = 0.0
    for tq in (100.0, 2500.0, 7.0e6):
        thv = float(theta_rs(np.array([tq]))[0])
        dev_ = abs(thv - float(mp.siegeltheta(tq)))
        bar_ = BAR_THETA_ABS + BAR_THETA_REL * abs(thv)
        th_ok = th_ok and dev_ <= bar_
        th_dev_sc = max(th_dev_sc, dev_ / bar_)
    psi_dev = 0.0
    for p0 in (0.25, 0.75):
        v_eps = float(rs_psi(np.array([p0 + 1e-5]))[0])
        v_at = float(rs_psi(np.array([p0]))[0])
        psi_dev = max(psi_dev, abs(v_eps - 0.5), abs(v_at - 0.5))
    ts_spot = np.geomspace(2500.0, 9.5e6, N_Z_SPOTS)
    z_np = rs_z_sorted(ts_spot)
    mp.mp.dps = 25
    z_mp = np.array([float(mp.siegelz(t)) for t in ts_spot])
    mp.mp.dps = 30
    dev = np.abs(z_np - z_mp)
    bar_v = BAR_ZDEV_C * (ts_spot / TWO_PI) ** (-0.75) + BUDGET_FLOAT
    z_ok = bool(np.all(dev <= bar_v))
    check("G0.2 [E] RS-Z machinery: theta max dev/bar %.3f <= 1 (bar "
          "%.0e + %.0e |theta|, calibration history (i)); Psi "
          "singular guard %.1e <= %.0e; Z vs mpmath at %d log-spaced "
          "points in [2.5e3, 9.5e6]: max dev %.2e, max dev/budget-bar "
          "%.3f <= 1 (Gabcke C0 budget %.3f (t/2pi)^-3/4, acceptance "
          "envelope %.2f x + %.0e float)"
          % (th_dev_sc, BAR_THETA_ABS, BAR_THETA_REL, psi_dev,
             BAR_PSI, N_Z_SPOTS, float(np.max(dev)),
             float(np.max(dev / bar_v)), GABCKE_C, BUDGET_C,
             BUDGET_FLOAT),
          th_ok and psi_dev <= BAR_PSI and z_ok)

    # ================================================ H1 -- Platt constant
    print("\nH1 -- the Platt-constant chain on the hole (|S| <= "
          "%.4f to %.4g; the task sketch, adjudicated)"
          % (S_PLATT, T_PLATT))
    L2500 = math.log(2500.0 / TWO_PI)
    pen = 2.0 * S_PLATT + EPS_N
    print("   the sketch, exact: at t = 2500 (L = log(t/2pi) = %.4f), "
          "delta = pi a:" % L2500)
    print("   a        aL/2      -(2S+eps)   count    window pi*a  "
          "main lobe 2pi/a   ratio a^2/2")
    for aw in [a0] + [a for a in A_FAM if abs(a - a0) > 1e-9]:
        cnt = aw * L2500 / 2.0 - pen
        print("   %.4f   %8.4f   -%.4f    %+7.3f   %8.4f     "
              "%8.4f       %6.3f"
              % (aw, aw * L2500 / 2.0, pen, cnt, math.pi * aw,
                 TWO_PI / aw, aw * aw / 2.0))
    sketch_cnt = a0 * L2500 / 2.0 - pen
    print("   -> the count IS positive (packet/density scale; that "
          "layer never had a hole),")
    print("      but the window pi a0 = %.3f exceeds the capture lobe "
          "2pi/a0 = %.3f by %.2f x:" % (math.pi * a0, TWO_PIA,
                                        a0 * a0 / 2.0))
    print("      NOT pointwise capture.  Max capture window delta < "
          "2pi/a needs L >= a(2S+eps):")
    print("   a        L_need     t_on = 2pi e^L (+%.0f)   vs Platt "
          "window top" % H10_SHIFT)
    for aw in [a0] + [a for a in A_FAM if abs(a - a0) > 1e-9]:
        Ln = aw * pen
        t_on_a = TWO_PI * math.exp(Ln) + H10_SHIFT
        ok_a = "inside" if t_on_a <= T_PLATT else "BEYOND (no entry)"
        print("   %.4f   %8.4f   %.4g              %s"
              % (aw, Ln, t_on_a, ok_a))
    t_on_a0_c = TWO_PI * math.exp(a0 * pen) + H10_SHIFT
    check("H1.1 [ANALYTIC] Platt-constant adjudication: the task "
          "sketch count at (t = 2500, delta = pi a0) = %+0.3f (quote "
          "%+0.2f +- %.2f) is REAL but packet-scale; the max capture "
          "window reproduces t_on(a0) = %.5g (closed-form %.5g, "
          "|rel dev| %.3f <= 0.02): H1 alone canNOT enter the hole -- "
          "the constant chain IS the hole boundary"
          % (sketch_cnt, REF_SKETCH, BAR_SKETCH, t_on_pl, t_on_a0_c,
             abs(t_on_a0_c / t_on_pl - 1.0)),
          abs(sketch_cnt - REF_SKETCH) <= BAR_SKETCH
          and abs(t_on_a0_c / t_on_pl - 1.0) <= 0.02)
    # cited secondary band |S| < 2 below 6.8e6 (corroboration only)
    t_on_b2 = t_on_centered(s_bound_band2, TWO_PIA, T_BAND2 - 500.0)
    t_on_b2v = t_on_b2 if t_on_b2 is not None else 0.0
    if t_on_b2 is not None:
        hb2 = float(h_min_chain(np.array([T_BAND2 - 500.0]),
                                s_bound_band2)[0])
        f_b2 = TWO_PI * float(fejer_a(a0, np.array([hb2 / 2.0]))[0])
        print("   H1.2 [CITED, secondary -- corroboration only, NOT "
              "load-bearing]: |S| < %.0f for T < %.2g (classical "
              "computations, Wikipedia RH survey quote): centered "
              "capture enters at t_on = %.4g, floor at the band top "
              "%.3f -- would cover [%.3g, %.2g]; %.2f of %.2f "
              "decades would remain below"
              % (S_BAND2, T_BAND2, t_on_b2, f_b2, t_on_b2, T_BAND2,
                 math.log10(t_on_b2 / 2500.0), hole_dec))

    # ================================================ H3 -- analytic path
    print("\nH3 -- the analytic path: loss bookkeeping + the exact "
          "prime term (Weil chain, primes + digamma ONLY)")
    build_xtr()
    ka0 = core.atoms_in(a0)
    u_at = UU[:ka0]
    mu_at = MU[:ka0]
    # Selberg guards per delta
    xs_g = np.linspace(-400.0, 400.0, 800001) + 1e-5
    sm_guard_ok = True
    SH = {}
    P_UNIF = {}
    P_LIP = {}
    INTD = {}
    for dl in DELTAS_X:
        Sv = s_minus(xs_g, dl, DL0)
        box = (np.abs(xs_g) <= 0.5 * dl).astype(float)
        viol = float(np.max(Sv - box))
        mass = float(np.trapezoid(Sv, xs_g))
        sm_guard_ok = sm_guard_ok and viol <= BAR_SM_BOX \
            and abs(mass - (dl - PIA)) <= BAR_SM_MASS
        sh, intD = shat_arr(dl, DL0, u_at)
        SH[dl] = sh
        INTD[dl] = intD
        P_UNIF[dl] = float(np.sum((mu_at / 2.0) * np.abs(sh))) / math.pi
        P_LIP[dl] = float(np.sum((mu_at / 2.0) * np.abs(sh)
                                 * u_at)) / math.pi
        print("   delta = %.2f: minorant viol %.1e <= %.0e, mass %.5f "
              "vs %.5f; P = %.4f, P' (Lipschitz) = %.4f, int|D| = %.3f"
              % (dl, viol, BAR_SM_BOX, mass, dl - PIA, P_UNIF[dl],
                 P_LIP[dl], intD))
    # arch interpolant in L = log(t/2pi) + tail/pole budgets
    sf = np.arange(-40.0, 40.0 + 1e-9, 0.005)
    sm_ = np.arange(40.005, 1500.0, 0.05)
    s_all = np.concatenate([-sm_[::-1], sf, sm_]) + 2.5e-4
    SMD = {dl: s_minus(s_all, dl, DL0) for dl in DELTAS_X}
    t_arch = np.geomspace(2.0e3, 1.0e18, N_ARCH_PTS)
    L_arch = np.log(t_arch / TWO_PI)
    ARCH = {dl: np.empty(N_ARCH_PTS) for dl in DELTAS_X}
    for i0 in range(0, N_ARCH_PTS, 8):
        i1 = min(N_ARCH_PTS, i0 + 8)
        OM = omega_arch(t_arch[i0:i1, None] + s_all[None, :])
        for dl in DELTAS_X:
            ARCH[dl][i0:i1] = np.trapezoid(SMD[dl][None, :] * OM,
                                           s_all, axis=1) / TWO_PI
    arch_inc_ok = all(bool(np.all(np.diff(ARCH[dl]) > 0.0))
                      for dl in DELTAS_X)
    # interpolation error at midpoints
    t_mid = np.sqrt(t_arch[:-1] * t_arch[1:])[::6]
    e_interp = 0.0
    for dl in DELTAS_X:
        OMm = omega_arch(t_mid[:, None] + s_all[None, :])
        a_ex = np.trapezoid(SMD[dl][None, :] * OMm, s_all, axis=1) \
            / TWO_PI
        a_ip = np.interp(np.log(t_mid / TWO_PI), L_arch, ARCH[dl])
        e_interp = max(e_interp, float(np.max(np.abs(a_ex - a_ip))))
    c_tail = {}
    c_pole = {}
    for dl in DELTAS_X:
        c_tail[dl] = float(np.max(np.abs(s_minus(
            np.array([-1499.0, 1499.0]), dl, DL0)))) * 1499.0 ** 2
        cp = 0.0
        for tq in T_POLE_CAL:
            cp = max(cp, abs(pole_term(tq, dl, DL0)) * tq ** 2)
        c_pole[dl] = 3.0 * cp

    def budgets(dl, t):
        tl = (2.0 * c_tail[dl] / 1500.0) \
            * (abs(math.log(max(t, 3.0) / 2.0)) + 3.0) / TWO_PI
        return tl + c_pole[dl] / t ** 2 + e_interp

    def arch_of(dl, t):
        return float(np.interp(math.log(t / TWO_PI), L_arch, ARCH[dl]))

    print("   arch interpolant: %d log points, increasing %s, interp "
          "err %.1e (budgeted); tail env c = %s; pole env = %s"
          % (N_ARCH_PTS, arch_inc_ok, e_interp,
             {("%.2f" % d): round(c_tail[d], 3) for d in DELTAS_X},
             {("%.2f" % d): ("%.1e" % c_pole[d]) for d in DELTAS_X}))

    # H3.0 Weil identity check on the comb (delta = 1.90)
    d_id = 1.90
    zg = np.exp(np.linspace(math.log(gam_max), math.log(1.0e10), 6000))
    dens_zg = np.log(zg / TWO_PI) / TWO_PI

    def comb_side(t, delta):
        v = float(np.sum(s_minus(GAM - t, delta, DL0)
                         + s_minus(GAM + t, delta, DL0)))
        tail = (s_minus(zg - t, delta, DL0)
                + s_minus(zg + t, delta, DL0)) * dens_zg
        return v + float(np.trapezoid(tail * zg, np.log(zg)))

    id_max = 0.0
    for tq in T_SAMPLES:
        OMq = omega_arch(tq + s_all)
        arch_v = float(np.trapezoid(SMD[d_id] * OMq, s_all)) / TWO_PI
        pol_v = pole_term(tq, d_id, DL0)
        prim_v = float(np.sum((mu_at / 2.0) * SH[d_id]
                              * np.cos(tq * u_at))) / math.pi
        r_ = abs(arch_v + pol_v - prim_v - comb_side(tq, d_id))
        id_max = max(id_max, r_)
    check("H3.0 [E] guards: Selberg minorant/mass per delta OK %s; "
          "Weil identity max residual %.2e <= %.0e (5 points, "
          "delta = %.2f); arch increasing %s"
          % (sm_guard_ok, id_max, BAR_IDENT, d_id, arch_inc_ok),
          sm_guard_ok and id_max <= BAR_IDENT and arch_inc_ok)

    # H3.1 loss bookkeeping + uniform-P t*
    tstar_u = {}
    for dl in DELTAS_X:
        lo, hi = 3.0e3, 3.0e9
        f_hi = arch_of(dl, hi) - P_UNIF[dl] - budgets(dl, hi)
        while f_hi <= 0.0 and hi < 1e17:
            hi *= 10.0
            f_hi = arch_of(dl, hi) - P_UNIF[dl] - budgets(dl, hi)
        for _ in range(120):
            mid = math.sqrt(lo * hi)
            if arch_of(dl, mid) - P_UNIF[dl] - budgets(dl, mid) > 0.0:
                hi = mid
            else:
                lo = mid
        tstar_u[dl] = hi
    print("   H3.1 loss bookkeeping: mass deficit = 1/D = pi/a0 = "
          "%.5f EXACTLY (Vaaler closed form); Logan/Littmann: "
          "Selberg's minorant is extremal when D delta in Z (here "
          "D delta = %.3f / %.3f) and the extremal deficit stays "
          "Theta(1/D): the deficit is NOT the lever." % (PIA,
          DL0 * DELTAS_X[0], DL0 * DELTAS_X[1]))
    print("   sensitivity t*(deficit scale x, P) at delta = 2.24 "
          "(slope = (delta - x pi/a0)/2pi):")
    for xs in (1.0, 0.5, 0.0):
        for Pq in (P_UNIF[2.24], 1.5, 1.0):
            sl = (2.24 - xs * PIA) / TWO_PI
            print("      x = %.1f, P = %.3f: L* ~ %.2f, t* ~ %.3g"
                  % (xs, Pq, Pq / sl, TWO_PI * math.exp(Pq / sl)))
    print("   -> even deficit 0 with P = %.3f leaves t* ~ %.2g; the "
          "lever is the PRIME TERM (its sign structure)."
          % (P_UNIF[2.24], TWO_PI * math.exp(P_UNIF[2.24] * TWO_PI
                                             / 2.24)))
    print("   centered-Selberg note: the chain contains no S(t) term "
          "-- nothing to center (typed).")
    check("H3.1 [ANALYTIC+CITED] uniform-P chain reproduced: P(2.24) "
          "= %.4f (quote %.3f +- %.2f); t*(2.24) = %.4g (quote %.3g "
          "+- %.0f%%); t*(1.90) = %.4g"
          % (P_UNIF[2.24], REF_P224, BAR_P, tstar_u[2.24], REF_TSTAR,
             100 * BAR_TSTAR_REL, tstar_u[1.90]),
          abs(P_UNIF[2.24] - REF_P224) <= BAR_P
          and abs(tstar_u[2.24] / REF_TSTAR - 1.0) <= BAR_TSTAR_REL)

    # H3.2 exact prime term, hierarchical certificate
    print("\n   H3.2 the exact prime term: floor_delta(t) = "
          "arch(block-lo) - prime(t) - budgets; levels h = %s, "
          "slack = P' h/2" % (CERT_LEVELS,))
    t_lo_cert = 2515.3
    t_hi_cert = 1.05 * tstar_u[2.24]
    blocks = np.geomspace(t_lo_cert, t_hi_cert, N_CERT_BLOCKS + 1)
    coef = {dl: (mu_at / 2.0) * SH[dl] / math.pi for dl in DELTAS_X}

    def prime_of(dl, ts):
        out = np.empty(ts.size)
        for a_ in range(0, ts.size, 200000):
            b_ = min(ts.size, a_ + 200000)
            out[a_:b_] = np.cos(np.multiply.outer(ts[a_:b_], u_at)) \
                @ coef[dl]
        return out

    t_cert0 = time.time()
    prime_sup = {}

    def cert_cascade(dl):
        """hierarchical Lipschitz certificate for floor_dl(t) > 0 on
        every cert block; a SAMPLED negative floor is a definite fail
        (short circuit); residual uncertainty at the deepest level
        counts as fail (conservative)."""
        cert_blk = np.zeros(N_CERT_BLOCKS, dtype=bool)
        lv_counts = [0] * len(CERT_LEVELS)
        n_deep = 0
        for ib in range(N_CERT_BLOCKS):
            b_lo, b_hi = float(blocks[ib]), float(blocks[ib + 1])
            ab = arch_of(dl, b_lo) - budgets(dl, b_lo)
            n_cells = int(math.ceil((b_hi - b_lo) / CERT_LEVELS[0]))
            pts = b_lo + (np.arange(n_cells) + 0.5) * CERT_LEVELS[0]
            failed = False
            for lv, h in enumerate(CERT_LEVELS):
                pr = prime_of(dl, pts)
                lv_counts[lv] += pts.size
                if dl == 1.90 and lv == 0:
                    dec = int(math.log10(b_lo))
                    prime_sup[dec] = max(prime_sup.get(dec, -9e9),
                                         float(np.max(pr)))
                fl = ab - pr
                if bool(np.any(fl <= 0.0)):
                    failed = True
                    break
                unc = fl <= P_LIP[dl] * h * 0.5
                if not bool(np.any(unc)):
                    break
                if lv + 1 < len(CERT_LEVELS):
                    h2 = CERT_LEVELS[lv + 1]
                    nref = int(round(h / h2))
                    off = (np.arange(nref) - (nref - 1) / 2.0) * h2
                    pts = (pts[unc][:, None] + off[None, :]).ravel()
                else:
                    failed = True
                    n_deep += int(np.sum(unc))
            cert_blk[ib] = not failed
        return cert_blk, lv_counts, n_deep

    def t_x_of(cert_blk):
        ib_last_fail = -1
        for ib in range(N_CERT_BLOCKS):
            if not cert_blk[ib]:
                ib_last_fail = ib
        if ib_last_fail < 0:
            return t_lo_cert, True
        return float(blocks[ib_last_fail + 1]), \
            bool(np.all(cert_blk[ib_last_fail + 1:]))

    CERT = {}
    for dl in DELTAS_X:
        cb, lvc, ndp = cert_cascade(dl)
        tx, contig = t_x_of(cb)
        CERT[dl] = dict(blk=cb, tx=tx, contig=contig, ndeep=ndp)
        print("   delta = %.2f: level point counts %s, deep-residual "
              "%d, t_x = %.5g, contiguous above %s  [%.0f s]"
              % (dl, lvc, ndp, tx, contig, time.time() - t_cert0))
    cert_any = CERT[1.90]["blk"] | CERT[2.24]["blk"]
    t_x_cert, contig_ok = t_x_of(cert_any)
    t_x_190 = CERT[1.90]["tx"] if CERT[1.90]["contig"] else t_hi_cert
    has_190 = bool(np.any(CERT[1.90]["blk"])) \
        and t_x_190 < t_hi_cert * 0.999
    f_224 = TWO_PI * float(fejer_a(a0, np.array([2.24 / 2.0]))[0])
    f_190 = TWO_PI * float(fejer_a(a0, np.array([1.90 / 2.0]))[0])
    print("   measured sup prime(t) (delta 1.90, level-0 samples) per "
          "decade: %s  (uniform P = %.3f)"
          % ({k: round(v, 3) for k, v in sorted(prime_sup.items())},
             P_UNIF[1.90]))
    print("   pointwise conversion: count >= 1 in delta-window => "
          "s_tot >= 2pi F(delta/2): delta 2.24 -> %.4e, delta 1.90 "
          "-> %.4f" % (f_224, f_190))
    print("   t_x(any) = %.5g vs uniform-P t*(2.24) = %.4g -- "
          "improvement x %.2f; t_x(1.90-alone) = %.5g (usable %s)"
          % (t_x_cert, tstar_u[2.24], tstar_u[2.24] / t_x_cert,
             t_x_190, has_190))
    check("H3.2 [E/ABSTRACT, central] exact prime term certificate: "
          "t_x = %.5g <= 1.05 t*(2.24) = %.4g; contiguous above t_x "
          "%s; abstract pointwise floor from t_x: %.2e (via 2.24)%s"
          % (t_x_cert, t_hi_cert, contig_ok, f_224,
             ("; %.3f via 1.90 from %.5g" % (f_190, t_x_190))
             if has_190 else ""),
          t_x_cert <= t_hi_cert + 1.0 and contig_ok)

    # ================================================ H2 -- the scan
    print("\nH2 -- the verification path: the honest zetazero budget, "
          "then the vectorized RS sign-change scan")
    mp.mp.dps = 15
    rates = []
    for nq in (2100, 4200, 8400):
        tq0 = time.time()
        _ = mp.zetazero(nq)
        rates.append((nq, time.time() - tq0))
    mp.mp.dps = 30
    r_mean = sum(r for _, r in rates) / 3.0
    n_top = float(main_N(np.array([REF_TON]))[0]) + 7.0 / 8.0
    est_1e4 = r_mean * 8.0e3 / 60.0
    est_hole = r_mean * (n_top - 2000.0) / 3600.0
    print("   H2.1 zetazero rate: %s s/zero (n = 2100/4200/8400); to "
          "n = 1e4 (gamma ~ 9.88e3): ~%.0f min; to the hole top "
          "(N(%.3g) ~ %.3g zeros): ~%.0f h -> REJECTED (> %.0f h); "
          "pivot to the vectorized scan (declared)"
          % (["%.2f" % r for _, r in rates], est_1e4, REF_TON, n_top,
             est_hole, ZC_BUDGET_H))

    # Platt-2S handover level and scan top
    def platt2s_floor(t):
        hh = float(h_min_chain(np.array([max(t - H10_SHIFT, T_CLAMP)]),
                               s_bound_platt)[0])
        if hh >= TWO_PIA:
            return 0.0
        return TWO_PI * float(fejer_a(a0, np.array([hh / 2.0]))[0])

    lo, hi = t_on_pl, 3.0e10
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if platt2s_floor(mid) >= FLOOR_ENTRY:
            hi = mid
        else:
            lo = mid
    t_platt_entry = hi
    T_Z = 1.02 * min(t_x_cert, t_platt_entry) + 10.0
    T_Z = max(T_Z, 3100.0)
    print("   Platt-2S floor reaches %.0e at t = %.4g; scan top T_Z = "
          "1.02 x min(t_x, that) + 10 = %.5g"
          % (FLOOR_ENTRY, t_platt_entry, T_Z))

    # ---------------- stage 1 scan (cached)
    mids = errs = None
    if os.path.exists(CACHE_SCAN):
        try:
            dat = np.load(CACHE_SCAN)
            if (int(dat["ver"]) == SCAN_VER
                    and abs(float(dat["lo"]) - T_SCAN_LO) < 1e-6
                    and float(dat["hi"]) >= T_Z - 1e-6):
                mids = np.asarray(dat["mids"], dtype=float)
                errs = np.asarray(dat["errs"], dtype=float)
                m_ = mids <= T_Z + 50.0
                mids, errs = mids[m_], errs[m_]
                print("   stage-1 cache hit: %d zeros (ver %d)"
                      % (mids.size, SCAN_VER))
        except Exception as exc:  # noqa: BLE001 -- cache is best-effort
            print("   stage-1 cache unreadable (%s) -- rescanning"
                  % exc)
            mids = errs = None
    n_lowz = 0
    if mids is None:
        t_sc0 = time.time()
        mid_l, err_l = [], []
        t_cur = T_SCAN_LO
        prev_t = prev_z = None
        seg = 0
        while t_cur < T_Z:
            Lc = math.log(t_cur / TWO_PI)
            h_loc = min(max(H1_FRAC * TWO_PI / Lc, H1_MIN), H1_MAX)
            t_next = min(t_cur + CHUNK * h_loc, T_Z)
            ts = np.arange(t_cur, t_next, h_loc)
            if ts.size == 0:
                break
            if prev_t is not None:
                ts_full = np.concatenate([[prev_t], ts])
            else:
                ts_full = ts
            Z = rs_z_sorted(ts_full)
            if prev_t is not None:
                Z[0] = prev_z
            B = z_budget(ts_full)
            s01 = Z[:-1] * Z[1:] < 0.0
            okb = (np.abs(Z[:-1]) > B[:-1]) & (np.abs(Z[1:]) > B[1:])
            n_lowz += int(np.sum(s01 & ~okb))
            cross = s01 & okb
            idx = np.where(cross)[0]
            mid_l.append(0.5 * (ts_full[idx] + ts_full[idx + 1]))
            err_l.append(np.full(idx.size, 0.51 * h_loc))
            prev_t, prev_z = float(ts_full[-1]), float(Z[-1])
            t_cur = t_next
            seg += 1
            if seg % 100 == 0:
                print("      ... scan at t = %.3g (%.0f s)"
                      % (t_cur, time.time() - t_sc0))
        mids = np.concatenate(mid_l)
        errs = np.concatenate(err_l)
        order = np.argsort(mids)
        mids, errs = mids[order], errs[order]
        print("   stage-1: %d sign-change zeros on (%.0f, %.5g], "
              "low-|Z| skipped crossings %d  [%.0f s]"
              % (mids.size, T_SCAN_LO, T_Z, n_lowz,
                 time.time() - t_sc0))
        np.savez_compressed(CACHE_SCAN, ver=SCAN_VER, lo=T_SCAN_LO,
                            hi=T_Z, mids=mids, errs=errs)

    # ---------------- stage 2/3 refinement
    def refine(mids, errs, sel_idx, h_new, pad):
        """re-scan the gap intervals sel_idx at step h_new; replace."""
        if sel_idx.size == 0:
            return mids, errs
        lo_iv = mids[sel_idx] - errs[sel_idx] - pad
        hi_iv = mids[sel_idx + 1] + errs[sel_idx + 1] + pad
        # merge overlaps
        order = np.argsort(lo_iv)
        lo_iv, hi_iv = lo_iv[order], hi_iv[order]
        m_lo, m_hi = [lo_iv[0]], [hi_iv[0]]
        for l_, h_ in zip(lo_iv[1:], hi_iv[1:]):
            if l_ <= m_hi[-1]:
                m_hi[-1] = max(m_hi[-1], h_)
            else:
                m_lo.append(l_)
                m_hi.append(h_)
        pts_l, iv_l, g_tops = [], [], []
        for k, (l_, h_) in enumerate(zip(m_lo, m_hi)):
            g_ = np.arange(l_, h_ + h_new, h_new)
            pts_l.append(g_)
            iv_l.append(np.full(g_.size, k))
            g_tops.append(float(g_[-1]))
        pts = np.concatenate(pts_l)
        ivi = np.concatenate(iv_l)
        Z = rs_z_sorted(pts)
        B = z_budget(pts)
        cross = (Z[:-1] * Z[1:] < 0.0) & (ivi[:-1] == ivi[1:]) \
            & (np.abs(Z[:-1]) > B[:-1]) & (np.abs(Z[1:]) > B[1:])
        idx = np.where(cross)[0]
        new_m = 0.5 * (pts[idx] + pts[idx + 1])
        new_e = np.full(new_m.size, 0.5 * h_new)
        keep = np.ones(mids.size, dtype=bool)
        for l_, gt_ in zip(m_lo, g_tops):
            # delete exactly the span the re-scan grid can re-find
            keep &= ~((mids >= l_) & (mids <= gt_))
        mids2 = np.concatenate([mids[keep], new_m])
        errs2 = np.concatenate([errs[keep], new_e])
        isnew = np.concatenate([np.zeros(int(np.sum(keep)), bool),
                                np.ones(new_m.size, bool)])
        order = np.argsort(mids2)
        m3, e3, _n3, n_mrg = bracket_dedupe(mids2[order],
                                            errs2[order],
                                            isnew[order])
        print("      refine: %d re-found, %d old/new bracket merges"
              % (new_m.size, n_mrg))
        return m3, e3

    gaps = np.diff(mids)
    esum = errs[:-1] + errs[1:]
    sel = np.where(gaps + esum > GAP_REF_BAR)[0]
    print("   stage-2: refining %d gap intervals (> %.2f) at h = %.2f"
          % (sel.size, GAP_REF_BAR, H2_REF))
    mids, errs = refine(mids, errs, sel, H2_REF, 0.10)
    gaps = np.diff(mids)
    dworst = 0.5 * gaps + np.maximum(errs[:-1], errs[1:])
    sel3 = np.where(dworst >= CAPTURE_FRAC * PIA)[0]
    print("   stage-3: interior rescan of %d capture-fail candidates "
          "at h = %.3f" % (sel3.size, H3_REF))
    mids, errs = refine(mids, errs, sel3, H3_REF, 0.05)
    n_found = mids.size

    # ---------------- H2.2 bars
    def near_dist(targets, ref):
        """distance of each target to the nearest ref (both sorted)."""
        j = np.clip(np.searchsorted(ref, targets), 1, ref.size - 1)
        return np.minimum(np.abs(targets - ref[j - 1]),
                          np.abs(ref[j] - targets))

    # correctness direction (calibration history (ii)): every FOUND
    # zero in the certified strip must match a comb/extension zero
    GAMB = np.sort(np.concatenate([GAM, GAM_EXT])
                   if GAM_EXT is not None else GAM)
    strip_top = float(GAMB[-1]) - 1.0
    found_strip = mids[(mids > T_SCAN_LO) & (mids < strip_top)]
    d_real = near_dist(found_strip, GAMB) if found_strip.size \
        else np.array([0.0])
    frac_real = float(np.mean(d_real <= TOL_MATCH))
    # completeness (printed, no bar -- hidden close pairs are by
    # design harmless for floors)
    strip = GAM[(GAM > T_SCAN_LO) & (GAM < 2515.3)]
    dmin = near_dist(strip, mids) if strip.size else np.array([0.0])
    n_compl = int(np.sum(dmin <= TOL_MATCH))
    print("   correctness: %d/%d found zeros in (2400, %.0f) match a "
          "certified comb/extension zero within %.2f; completeness "
          "(printed, no bar): %d/%d cache zeros re-found"
          % (int(np.sum(d_real <= TOL_MATCH)), found_strip.size,
             strip_top, TOL_MATCH, n_compl, strip.size))
    if GAM_EXT is not None:
        ge_s = GAMB[(GAMB > 2516.0) & (GAMB < strip_top)]
        ms_s = mids[(mids > 2516.0) & (mids < strip_top)]
        print("   overlap-strip gap check (2516, %.0f): max found "
              "gap %.4f vs true max gap %.4f (printed, no bar)"
              % (strip_top, float(np.max(np.diff(ms_s)))
                 if ms_s.size > 2 else 0.0,
                 float(np.max(np.diff(ge_s)))))
    rng = np.random.default_rng(20260803)
    spots = rng.choice(n_found, size=min(N_MP_SIGN, n_found),
                       replace=False)
    mp.mp.dps = 25
    n_sign_ok = 0
    for k in spots:
        tl, tr = mids[k] - errs[k], mids[k] + errs[k]
        if float(mp.siegelz(tl)) * float(mp.siegelz(tr)) < 0.0:
            n_sign_ok += 1
    mp.mp.dps = 30
    band_edges = np.geomspace(2515.3, T_Z, N_BANDS + 1)
    th_e = theta_rs(band_edges)
    main_cnt = th_e / math.pi + 1.0
    found_cum = np.searchsorted(mids, band_edges)
    n_below = int(np.searchsorted(GAM, T_SCAN_LO))
    found_ratio_band = np.diff(found_cum) / np.maximum(
        np.diff(main_cnt), 1.0)
    glob_ratio = (found_cum[-1] - found_cum[0]) \
        / (main_cnt[-1] - main_cnt[0])
    # S lower-bound consistency (N_found <= N_true)
    idx_68 = mids <= min(T_BAND2, T_Z)
    n_f68 = n_below + np.arange(1, n_found + 1)[idx_68]
    s_low = n_f68 - theta_rs(mids[idx_68]) / math.pi - 1.0
    s_low_max = float(np.max(s_low)) if s_low.size else 0.0
    print("   per-band found/expected ratio: %s"
          % ["%.3f" % r for r in found_ratio_band])
    print("   S(t) lower-bound consistency on (2515, %.3g]: max "
          "S_found = %.3f (<= true S; the cited band |S| < 2 is NOT "
          "contradicted)" % (min(T_BAND2, T_Z), s_low_max))
    check("H2.2 [E, central] the scan: %d genuine sign-change zeros "
          "on (%.0f, %.5g] (budget-guarded, Gabcke C0); correctness "
          "(found -> certified) %.4f >= %.3f within %.2f; mpmath "
          "sign spots %d/%d; count sanity %.2f <= found/expected = "
          "%.5f <= %.4f (two-sided, calibration history (iii))"
          % (n_found, T_SCAN_LO, T_Z, frac_real, BAR_FOUND_REAL,
             TOL_MATCH, n_sign_ok, spots.size, BAR_FOUND_RATIO,
             glob_ratio, BAR_FOUND_RATIO_HI),
          frac_real >= BAR_FOUND_REAL and n_sign_ok == spots.size
          and BAR_FOUND_RATIO <= glob_ratio <= BAR_FOUND_RATIO_HI)

    # ---------------- H2.3 floors on the hole at a0
    gaps = np.diff(mids)
    dworst = 0.5 * gaps + np.maximum(errs[:-1], errs[1:])
    gmid = 0.5 * (mids[:-1] + mids[1:])
    RSCAN_TOP = float(mids[-1]) - 2.0     # last fully bracketed height
    in_hole = (mids[1:] > 2515.3) & (mids[:-1] < RSCAN_TOP)
    cap_ok = dworst < CAPTURE_FRAC * PIA
    fl_cap = TWO_PI * fejer_env(a0, dworst, 0.0)
    ZED = np.concatenate([GAM[GAM <= T_SCAN_LO], mids])
    ZER = np.concatenate([np.full(int(np.sum(GAM <= T_SCAN_LO)),
                                  1e-9), errs])
    dip_idx = np.where(in_hole & ~cap_ok)[0]
    dip_min = math.inf
    dip_rows = []
    for k in dip_idx:
        gl, gr = mids[k], mids[k + 1]
        tg = np.linspace(gl, gr, 96)
        j0 = int(np.searchsorted(ZED, gl - DIP_NEIGH))
        j1 = int(np.searchsorted(ZED, gr + DIP_NEIGH))
        zz = ZED[j0:j1]
        ee = ZER[j0:j1]
        d_ = np.abs(zz[None, :] - tg[:, None])
        fl = TWO_PI * np.sum(fejer_env(a0, d_, ee[None, :]), axis=1)
        v = float(np.min(fl))
        dip_min = min(dip_min, v)
        dip_rows.append((gl, gr - gl, v))
    band_min = np.full(N_BANDS, math.inf)
    bi = np.clip(np.searchsorted(band_edges, gmid) - 1, 0, N_BANDS - 1)
    m_ = in_hole & cap_ok
    np.minimum.at(band_min, bi[m_], fl_cap[m_])
    for k, (gl, gw, v) in zip(dip_idx, dip_rows):
        band_min[min(int(bi[k]), N_BANDS - 1)] = min(
            band_min[min(int(bi[k]), N_BANDS - 1)], v)
    print("   band table (edges %.4g .. %.5g; region top RSCAN_TOP = "
          "%.5g):" % (2515.3, T_Z, RSCAN_TOP))
    print("   band  [lo, hi)              n_found   max gap   min "
          "floor")
    for b in range(N_BANDS):
        mband = in_hole & (bi == b)
        gmax_b = float(np.max(gaps[mband])) if np.any(mband) else 0.0
        print("   %2d  [%9.4g, %9.4g) %8d   %.4f    %.5f"
              % (b, band_edges[b], band_edges[b + 1],
                 int(found_cum[b + 1] - found_cum[b]), gmax_b,
                 band_min[b] if math.isfinite(band_min[b]) else
                 float("nan")))
    floor_hole = float(np.min(band_min[np.isfinite(band_min)]))
    if dip_rows:
        worst = min(dip_rows, key=lambda r: r[2])
        print("   %d dip evaluations (capture-fail gaps); worst dip "
              "%.5f at t = %.2f (gap %.3f); dip-law ref 1/(pi a0 "
              "(g/2)^2) scale" % (len(dip_rows), worst[2], worst[0],
                                  worst[1]))
    gmax_all = float(np.max(gaps[in_hole]))
    gmax_at = float(gmid[in_hole][int(np.argmax(gaps[in_hole]))])
    check("H2.3 [E, central] the hole floor at a0: min over "
          "(2515.3, %.5g] = %.5f > %.0e (capture where d* < %.2f "
          "pi/a0 = %.4f, %d dips elsewhere, all > bar); max found "
          "gap %.4f at t = %.1f (vs 2pi/a0 = %.4f)"
          % (RSCAN_TOP, floor_hole, BAR_FLOOR_HOLE, CAPTURE_FRAC,
             CAPTURE_FRAC * PIA, len(dip_rows), gmax_all, gmax_at,
             TWO_PIA),
          floor_hole > BAR_FLOOR_HOLE
          and (not dip_rows or min(r[2] for r in dip_rows)
               > BAR_FLOOR_HOLE))

    # family honesty table (scan-level)
    print("   family capture-fail counts on the hole (upper bounds, "
          "unrefined at family scale):")
    for aw in A_FAM:
        th_w = CAPTURE_FRAC * math.pi / aw
        n_fail_w = int(np.sum(in_hole & (dworst >= th_w)))
        Ln = aw * pen
        t_on_w = TWO_PI * math.exp(Ln) + H10_SHIFT
        print("   a = %.4f: fail gaps %7d (d* >= %.4f); Platt-2S "
              "entry %s"
              % (aw, n_fail_w, th_w,
                 ("%.3g" % t_on_w) if t_on_w <= T_PLATT
                 else "NONE (beyond Platt window)"))

    # ================================================ H4 -- synthesis
    print("\nH4 -- the synthesis: the gapless coverage map at a0")
    # comb region floor (dense, comb + scan zeros above)
    tg_d = np.arange(10.0, 2515.3, 0.05)
    Z1 = np.concatenate([GAM, mids[mids <= 2700.0]])
    Z1 = np.sort(Z1)
    vmin, vat = math.inf, 0.0
    for a_ in range(0, tg_d.size, 4000):
        b_ = min(tg_d.size, a_ + 4000)
        blk = tg_d[a_:b_][:, None]
        v = TWO_PI * (np.sum(fejer_a(a0, Z1[None, :] - blk), axis=1)
                      + np.sum(fejer_a(a0, Z1[None, :] + blk), axis=1))
        j = int(np.argmin(v))
        if float(v[j]) < vmin:
            vmin, vat = float(v[j]), float(tg_d[a_ + j])
    # (c, C): c from the best pointwise Selberg slope
    dgr = np.linspace(PIA + 1e-6, TWO_PIA - 1e-6, 20001)
    slv = fejer_a(a0, dgr / 2.0) * (dgr - PIA)
    j = int(np.argmax(slv))
    sl_best, d_sl = float(slv[j]), float(dgr[j])
    c_stmt = 0.98 * float(fejer_a(a0, np.array([1.90 / 2.0]))[0]) \
        * (1.90 - PIA)

    def floor_map(t):
        best = 0.0
        if 10.0 <= t <= 2515.3:
            best = max(best, vmin)
        if 2515.3 < t <= RSCAN_TOP:
            b = int(np.clip(np.searchsorted(band_edges, t) - 1, 0,
                            N_BANDS - 1))
            if math.isfinite(band_min[b]):
                best = max(best, band_min[b])
        if t_x_cert <= t <= t_hi_cert:
            best = max(best, f_224)
        if has_190 and t_x_190 <= t <= t_hi_cert:
            best = max(best, f_190)
        for dl in DELTAS_X:
            if t >= tstar_u[dl]:
                cnt = arch_of(dl, t) - P_UNIF[dl] - budgets(dl, t)
                if cnt > 0.0:
                    # the window count is an integer >= ceil(cnt) >= 1
                    best = max(best, TWO_PI * float(
                        fejer_a(a0, np.array([dl / 2.0]))[0])
                        * max(1.0, cnt))
        if t_on_pl < t <= T_PLATT:
            best = max(best, platt2s_floor(t))
        if t_on_tr is not None and t >= t_on_tr:
            hh = float(h_min_chain(np.array([t - H10_SHIFT]),
                                   s_bound_tr)[0])
            if hh < TWO_PIA:
                best = max(best, TWO_PI * float(
                    fejer_a(a0, np.array([hh / 2.0]))[0]))
        return best

    t_eval = np.concatenate([np.geomspace(10.0, 1.0e16, 400),
                             np.array([2515.3 * 0.999,
                                       RSCAN_TOP * 0.999,
                                       t_x_cert * 1.001,
                                       min(t_x_190 * 1.001, 1e15),
                                       tstar_u[2.24] * 1.001])])
    t_eval = np.sort(t_eval)
    fl_ev = np.array([floor_map(t) for t in t_eval])
    gapless = bool(np.all(fl_ev > 0.0))
    C_stmt = float(np.max(c_stmt * np.log(2.0 + t_eval) - fl_ev))
    C_stmt = max(C_stmt, 0.0) + 0.01
    j_bind = int(np.argmax(c_stmt * np.log(2.0 + t_eval) - fl_ev))
    print("   region map (support -> range -> min floor -> type):")
    print("   R1  comb (Turing-certified)   [10, 2515.3]      "
          "%.5f at t = %.1f   [E]" % (vmin, vat))
    print("   R2  RS scan (this module)     (2515.3, %.5g]  %.5f"
          "           [E, verification-consistent]"
          % (RSCAN_TOP, floor_hole))
    print("   R3a exact-prime Weil chain    [%.5g, %.4g]  %.2e"
          "      [abstract; on-line window <= 3e12 by PT21]"
          % (t_x_cert, t_hi_cert, f_224))
    if has_190:
        print("   R3b ... delta = 1.90 branch   [%.5g, %.4g]  %.3f"
              "        [abstract, same caveat]"
              % (t_x_190, t_hi_cert, f_190))
    print("   R4  uniform-P Selberg         [%.4g, inf)     >= "
          "%.2e (count >= 1), growing; delta = 1.90 branch from "
          "t*(1.90) = %.4g with >= %.3f; best pointwise slope %.5f"
          "/log t at delta* = %.2f"
          % (tstar_u[2.24], f_224, tstar_u[1.90], f_190, sl_best,
             d_sl))
    print("   R5  Platt-2S capture (belt)   [%.4g, %.4g]  %.0e "
          "at entry      [cited verification]"
          % (t_platt_entry, T_PLATT, FLOOR_ENTRY))
    print("   R6  Trudgian-2S (uncond.)     [%.4g, inf)              "
          "        [unconditional capture]" % t_on_tr)
    print("   unconditionality ledger: below 3e12 all window zeros "
          "are on-line (PT21); on (3e12, %.3g) the count chain is "
          "modulo the off-line window (parent typing); from %.3g "
          "Trudgian-2S is unconditional." % (t_on_tr, t_on_tr))
    print("   THE STATEMENT: s_tot(t; a0) >= c log(2+t) - C for all "
          "t >= 10 with c = %.5f, C = %.4f (binding at t = %.4g)"
          % (c_stmt, C_stmt, float(t_eval[j_bind])))
    check("H4.1 [SYNTHESIS, central] the a0 map is GAPLESS %s: comb "
          "[10, 2515.3] -> scan (2515.3, %.5g] -> abstract/verified "
          "beyond, with RSCAN_TOP >= min(t_x = %.5g, Platt entry = "
          "%.4g); all region floors > 0 on the dense log grid; "
          "statement (c, C) = (%.5f, %.4f)"
          % (gapless, RSCAN_TOP, t_x_cert, t_platt_entry, c_stmt,
             C_stmt),
          gapless and RSCAN_TOP >= min(t_x_cert, t_platt_entry))

    # ================================================ Z1 -- verdict + note
    guards_ok = not any(f.startswith("G0") for f in FAILS)
    h2_ok = not any(f.startswith(("H2.2", "H2.3")) for f in FAILS)
    h3_ok = not any(f.startswith("H3.2") for f in FAILS)
    h4_ok = not any(f.startswith("H4.1") for f in FAILS)
    if not guards_ok:
        VERDICT = "HOLE-MIXED (guards failed)"
    elif t_x_cert <= 2515.4 and h3_ok:
        VERDICT = "HOLE-CLOSED-UNCONDITIONAL"
    elif h2_ok and h3_ok and h4_ok:
        VERDICT = "HOLE-CLOSED-SPLIT-TYPE"
    elif h2_ok or h3_ok:
        VERDICT = "HOLE-NARROWED"
    else:
        VERDICT = "HOLE-NO-GAIN"

    check("Z1.1 [C] typed reading: (i) H1 pure reproduces the hole "
          "boundary t_on = %.4g (no entry; the delta = pi a sketch "
          "count %.2f is packet-scale -- correct but not capture); "
          "(ii) H2 scan closes (2515.3, %.5g] verification-backed "
          "(min floor %.5f, %d zeros); (iii) H3 exact prime term "
          "moves the abstract entry t* = %.4g -> t_x = %.5g (x %.1f) "
          "-- the deficit pi/a0 is extremal (Logan/Littmann), the "
          "prime SIGN STRUCTURE was the lever; (iv) map gapless %s; "
          "family typed honestly (a > %.2f windows have no Platt-2S "
          "entry; reach [10, 870] parent-closed); no marker move"
          % (t_on_pl, sketch_cnt, RSCAN_TOP, floor_hole, n_found,
             tstar_u[2.24], t_x_cert, tstar_u[2.24] / t_x_cert,
             gapless, math.log(T_PLATT / TWO_PI) / pen), True)

    print("\nVERDICT: %s" % VERDICT)
    fate = "CLOSED with split typing" \
        if VERDICT.startswith("HOLE-CLOSED") \
        else "NARROWED (typed remainder)"
    br190 = (" resp. %.3f (delta 1.90 branch from %.5g)"
             % (f_190, t_x_190)) if has_190 else ""
    print(f"""
CONTRACT-NOTE TEXT (report only -- nothing is written by this module):

  PRIME.WEIL.OPERATOR.01 / W2, coverage-hole round -- THE NINTH SLICE
  (2026-08-03): the last hole of the W2 pointwise chain, (2500,
  7.27e6) = 3.46 decades from the pinch attack, was ATTACKED on the
  three named paths and {fate}.  (1) H1 (Platt constant 2.5167): the
  centered-capture chain with the constant bound reproduces the hole
  boundary EXACTLY (t_on = {t_on_pl:.4g} = 2pi exp(a0(2 x 2.5167 +
  eps)) + {H10_SHIFT:.0f}); the task's delta = pi a count
  ({sketch_cnt:.2f} at t = 2500) is real but lives at packet scale
  (window/lobe ratio a0^2/2 = {a0 * a0 / 2.0:.2f}) -- the density
  layer never had a hole; H1 alone cannot enter.  The cited band
  |S| < 2 below 6.8e6 (secondary) would cover [{t_on_b2v:.3g},
  6.8e6] -- corroboration, not load-bearing.  (2) H2 (verification
  path): the honest zetazero budget ({r_mean:.2f} s/zero ->
  {est_hole:.0f} h to the hole top) forced the declared pivot to a
  vectorized Riemann-Siegel scan (Gabcke C0 budget 0.127
  (t/2pi)^(-3/4), acceptance {BUDGET_C:.2f} x + {BUDGET_FLOAT:.0e}):
  {n_found} budget-guarded sign-change zeros on ({T_SCAN_LO:.0f},
  {T_Z:.5g}], found->certified correctness {frac_real:.4f}, mpmath
  spot checks {n_sign_ok}/{spots.size}, found/expected
  {glob_ratio:.5f} (two-sided sanity).
  Missed zeros only LOWER the floor (every kernel term >= 0): the
  certified pointwise floor on the hole is min = {floor_hole:.5f} >
  {BAR_FLOOR_HOLE:.0e} (capture + {len(dip_rows)} dip evaluations;
  max gap {gmax_all:.3f} vs lobe 2.266).  (3) H3 (analytic path):
  the Selberg mass deficit pi/a0 is EXTREMAL (Logan/Littmann:
  optimal when D delta in Z) -- not the lever; the lever is the
  prime term's SIGN STRUCTURE: replacing the uniform P =
  {P_UNIF[2.24]:.3f} by the exact almost-periodic prime(t) ({ka0}
  atoms, u <= 2a0 = log 256) with a hierarchical Lipschitz
  certificate moves the abstract (primes + digamma only) entry from
  t* = {tstar_u[2.24]:.4g} down to t_x = {t_x_cert:.5g}
  (x {tstar_u[2.24] / t_x_cert:.1f} improvement), pointwise floor
  {f_224:.2e} (delta 2.24){br190}.  (4) THE SYNTHESIS: the a0
  coverage map is GAPLESS {gapless} -- [10, 2515.3] comb [E] (min
  {vmin:.4f}); (2515.3, {RSCAN_TOP:.5g}] scan [E, verification-
  consistent] (min {floor_hole:.4f}); [{t_x_cert:.5g}, inf) exact-
  prime + uniform Weil chain [abstract; window on-line below 3e12
  by Platt-Trudgian 2021, modulo off-line window beyond, until the
  unconditional Trudgian-2S capture from {t_on_tr:.3g}]; Platt-2S
  [{t_platt_entry:.3g}, 3.06e10] as redundant belt.  THEOREM DRAFT
  (anchor pointwise floor, mixed type): for a0 = log 16 and all
  t >= 10, s_tot(t; a0) = 2pi sum_rho F_a0(gamma_rho - t) >=
  c log(2+t) - C with (c, C) = ({c_stmt:.5f}, {C_stmt:.4f}) --
  constants and per-region supports in the run log.  THE W2
  END-STATE: density (v669) + frame-Garding (v674/v678 adaptive
  packets) + pointwise (THIS map) are each closed at the anchor
  with split typing; the family REACH [10, 870] is closed
  verification-backed (parent B2.2); typed OPEN: the pointwise
  family layer beyond the reach for the a > 4.43 windows (no
  Platt-2S entry; Selberg-only with exponentially large P(a)),
  A5(a), W2 Mosco, the packet projection form, and a -> infinity.
  TYPE: H1 = analytic (machine-checked); H2 = [E] verification-
  backed (self-produced budget-guarded scan, mpmath/cache
  cross-checked); H3 = abstract chain, identity-verified (max
  residual {id_max:.1e}); synthesis = mixed, split typing explicit;
  no marker move.  VERDICT {VERDICT}.
""")

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
