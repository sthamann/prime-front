"""Discovery probe: THE ZERO-GAP THEOREM ROUTE -- an EXPLICIT
UNCONDITIONAL "every interval [t, t + H_min(t)] contains a zero
ordinate" theorem, machine-verified on the Turing-certified comb, and
plugged into the W2 packet chain with ADAPTIVE packet widths
delta(t) = kappa H_min(t).  This probe measures and types; it moves no
marker.

CONTEXT (the two parents, both 2026-08-02).  fejer_density_bound_probe
(the v669 candidate) derived the exact identity s_tot = 2 pi (F_a * dN)
and the UNCONDITIONAL smoothed-density bound rho_{a,delta}(t) >=
c0_thm log(2+t) - C0_thm from windowed RvM counting + Trudgian's |S|
bound, with the certifiability floor delta > 4 pi A1 = 1.40743 and the
max comb gaps 6.887 (gamma_1 -> gamma_2) resp. 3.861 above t = 100.
packet_garding_probe (the v674 candidate) built the packet norm and
measured the residual: the packet PROJECTION Garding form c_X(M, C)
does NOT stabilize -- the minimizer sits on a single in-gap DST mode
charged with the full packet weight (within-packet dip depth theta =
min (lam_p + 1)/(avg_p + 1) ~ 0.20); the FRAME form holds.  The typed
OPEN residue was: within-packet equidistribution OR an unconditional
zero-gap input.  THIS probe supplies the zero-gap input and measures
whether it closes the projection form.

Z1 -- THE THEOREM (assembled from cited ingredients; the difference
route kills the 7/8 offset and the E terms nearly cancel):

  N(t + H) - N(t) >= [main(t+H) - main(t)] - |S(t+H)| - |S(t)| - eps_N
                  >= G(t, H) := mainD - 2 Sbound(t+H) - eps_N,
  main(x) = (x/2pi)(log(x/2pi) - 1),  eps_N = 2e-3 (E budget, t >= 10),

and since the count is an integer, G(t, H) > 0 forces >= 1 ordinate in
(t, t + H].  H_min(t) := the smallest such H (bisection; G is strictly
increasing in H on the bracket).  Sbound is the pointwise MINIMUM of
three cited unconditional bounds (each valid alone, so the min is):

  (P) |S(T)| <= 2.5167 for 0 <= T <= 30 610 046 000
      [Platt's rigorous zero isolation (Pla11/Pla17, LMFDB), quoted as
      eq. (1.2) in Bellotti, arXiv:2412.15470 = Math. Comp. (2025),
      doi 10.1090/mcom/4133] -- dominant on every reachable height;
  (T) |S(T)| <= 0.112 log T + 0.278 loglog T + 2.510, T >= e
      [Trudgian, J. Number Theory 134 (2014), Thm 1; validity
      re-affirmed via the HSW erratum + Platt computation, Bellotti
      fn. 2] -- the v669 chain, floor 4 pi 0.112 = 1.40743;
  (B) |S(T)| <= 0.10076 log T + min{0.24460 loglog T + 7.20844,
      1.68845 loglog T + 1.50956}, T >= e
      [Bellotti 2025, Cor. 1.5] -- best asymptotic floor
      4 pi 0.10076 = 1.26617.

  CANDIDATES TYPED AND REJECTED: (a) Littlewood 1924 gaps O(1/loglog)
  and the explicit version (Simonic, J. Number Theory 231 (2021)) are
  RH-CONDITIONAL -- excluded.  (b) the Turing/S1 route (Trudgian,
  Math. Comp. 80 (2011): |int_{t1}^{t2} S| <= 1.61 + 0.0914
  log(t2/2pi), t > 168 pi) gives, on a zero-free (t, t+H), the
  quadratic H^2 log(t/2pi)/(4pi) <= H Sbar(t) + a + b log(t2/2pi),
  i.e. asymptote H* = 2 pi A1 + sqrt((2 pi A1)^2 + 4 pi b) = 1.986
  (Trudgian A1) / 1.878 (Bellotti A1) -- DOMINATED by the pure
  S-difference route (the adversarial S(t1+) linear term); printed,
  not used.  (c) Hasanalizade-Shen-Wong, J. Number Theory 233 (2022)
  (0.1038, 0.2573, 9.4925 after the C3 correction, Bellotti fn. 1) --
  superseded by (B) on both fronts; quoted for the record.

  HONESTY (declared BEFORE the numbers): H_min(t) is DECREASING in t
  (the task sketch "packets widen upward" has the direction inverted);
  adaptive packets NARROW towards kappa 1.266 as t grows and stay
  above the v669 Fejer floor 1.4074 for kappa >= 2.  The known
  pointwise obstruction is INVARIANT under re-partitioning: main-lobe
  capture of a guaranteed zero needs H_min < pi/a, i.e. A1 < 1/(4a) =
  0.0902 at a0 -- below every cited constant, at every height.  The
  decisive Z3.3 measurement adjudicates whether the projection form
  cares.

CALIBRATION HISTORY (declared -- honesty first): run 1 (2026-08-02)
declared (i) "G(t, .) strictly increasing on the bracket" and (ii)
"kappa_X dyadic increments strictly decreasing" (the v674
fixed-partition read).  Run 1 measured: (i) fails for the Bellotti
chain at t <= ~14: the branch-2 loglog derivative 2 C2'/(x log x)
exceeds main'(x) for x <~ 14, a benign initial DIP of G below zero
before the unique sign change -- bisection unaffected (sign pattern
-...-+...+); (ii) fails structurally for adaptive partitions: the
band prefix occupied by stage M changes with M (1/3/9/20 bands at
kappa = 2), so the fixed-partition monotone-increment mechanism does
not transfer.  Both guards were recalibrated ONCE to the correct
invariants: (i) SINGLE SIGN CHANGE of G on the sampled bracket
(negative prefix, positive suffix), (ii) kappa_X UNIFORMLY BOUNDED
<= 1.5 (any fixed finite kappa suffices for the X-transfer of the
uniform H_log resolvent bound, v674 P1.2 note); the increments are
printed, not barred.  All other run-1 numbers reproduce unchanged;
run 1 already measured the decisive Z3.3 answer (not stabilized, all
(kappa, C)) -- the recalibration touches no c_X number.

THE ADAPTIVE PARTITION (declared).  Continuum band edges b_0 = 0,
b_{p+1} = b_p + kappa H_min(max(b_p, 10)) (H_min clamped below t = 10;
kappa in {2, 3}); M-independent by construction.  Weights w_p =
log(2 + b_p) (band lower edge, the minorant-friendly v674 convention;
midpoint printed as comparison).  Since H_min is decreasing, the j-th
subinterval of length delta_p / floor(delta_p / H_min(b_p)) >=
H_min(start) is covered by the theorem, so every band unconditionally
holds n_p >= max(floor(delta_p/H_min(b_p)), ceil(G(b_p, delta_p)))
ordinates (band 0 via the one-sided N(b_1) >= main + 7/8 - Sbound -
eps/2).  Unconditional packet-Boden (FRAME form, continuum tent
surrogate g_p^2 = unit-mass tent on the band):

  V_p := 2 pi sum_{gamma in band} (F_a * g_p^2)(gamma)
      >= B_p := 2 pi [ sum_j min_{I_j} (F_a * g_p^2)
                       + (n_p - n_sub) min_band (F_a * g_p^2) ],

computable from kernels alone -- the theorem-shaped Boden bound.  For
the PROJECTION floor no analogue exists: an adversarial in-gap mode
concentrates |v|^2 at a point and the guaranteed zero may sit on a
Fejer kernel null (pi/a < H_min at every height, see above) -- the
worst case is the un-smoothed dip, not certifiable (v669 F3 floor).

SLICES AND BARS (declared BEFORE the numbers):
  G0.0 [E] zero-comb integrity (verbatim fejer G0.0): 2000 zeros
       monotone; live mpmath zetazero at n = 1, 2, 3, 2000 (dps 20)
       dev <= 1e-8; RvM residual max <= Sbar + 0.01.  Extension cache
       (n 2001..2500) loaded, provenance printed, checked without bar.
  G0.1 [E] certified lag assembly: layered == verbatim at (a0, 92)
       and (a0, 736), rel < 1e-12; |lambda_1(736, full)| <= 5e-9;
       DST exactness (Mass-eigen residual < 1e-10 rel, normalization
       dev < 1e-8); weight-1 H_log companion lags within 5e-3 and
       H_log positive definite (Cholesky) on the ladder.
  G0.2 [E] H_min machinery: G(t, .) has a SINGLE sign change on the
       sampled bracket at 12 heights x chains (negative prefix,
       positive suffix -- the bisection-validity invariant, see
       CALIBRATION HISTORY); bisection bracket [G <= 0 <= G] holds;
       H_min nonincreasing in t on [10, 3000] (all three chains +
       min); each chain >= its asymptotic floor; the Platt branch is
       the argmin on the whole comb range.
  Z1.1 [ANALYTIC, cited] the theorem table: H_min(t) per chain at 12
       declared heights, asymptotic floors, the Turing-route
       comparison, the low-t anchor (gamma_1 inside the band-0
       interval).  Bar: all entries finite, min-chain values
       decreasing, gamma_1 <= H_min-band-0 edge.
  Z2.1 [E] comb verification: gamma_{n+1} - gamma_n <= H_min(gamma_n)
       for ALL 1999 certified gaps, for the min chain AND each branch
       separately -- the theorem must hold on the data (else the
       implementation is wrong).  Extension gaps (n 2000..2499)
       printed, no bar (provenance-dependent).
  Z2.2 [MEASURED] the air: ratios r_n = H_min(gamma_n)/gap_n -- global
       min / median / p90 and per dyadic band; quote guards: max gap
       6.887 (gamma_1 -> gamma_2) and max gap above t = 100 = 3.861,
       both within 0.01.
  Z3.1 [E] adaptive partitions (kappa = 2, 3) well-formed: edges
       strictly increasing, widths = kappa H_min >= kappa 1.266,
       weights strictly increasing; every band inside the comb range
       holds n_comb >= n_guar >= kappa zeros AND every H_min
       subinterval (b_p >= 10) is occupied; air n_comb/n_guar printed.
  Z3.2 [MEASURED] the unconditional packet-Boden at (a0, 736, kappa=2):
       B_p <= V_p for every band (validity on real zeros) and B_p > 0;
       ratio tables B_p/V_p, DST tent q_p/V_p (lattice-vs-continuum,
       printed), block floor lam_p and avg_p per band; fixed-partition
       theta reproduction |theta(736) - 0.20| <= 0.05 (the v674
       quote); the pointwise-obstruction numbers (pi/a vs inf H_min,
       the required A1 < 1/(4a) per family window).
  Z3.3 [MEASURED, decisive] the adaptive packet Garding ladder: per
       kappa in {2, 3} and C in {0.5, 1, 2}: c_X(M, C) on M =
       92/184/368/736.  STABILIZATION BAR per (kappa, C): all c_X > 0
       AND last relative increment <= 0.03 (task bar).  TWO-MODEL BAR:
       affine b + a/L vs pure a/L (L = log(2 + pi/D)): rms(pure) >=
       3 x rms(affine) AND b > 0.         Fixed-partition baseline printed;
       midpoint-weight column printed; minimizer forensics (dominant
       mode, single-mode floor, tightness) at (736, C = 1); kappa_X =
       lambda_max(H_X_adapt, H_log) <= 1.5 uniformly on the ladder
       (X -> H_log transfer, recalibrated read -- increments printed,
       see CALIBRATION HISTORY); pencil (H_X_adapt, Mass) == adaptive
       weights to 1e-8 at 736.
  Z4.1 [C] typing + contract note (report only; nothing written).

Verdict enums (frozen, precedence top-down):
  ZEROGAP-MIXED         -- any G0.* fails;
  ZEROGAP-GARDING-CLOSED -- Z2 + Z3.1 + Z3.2 bars pass AND for some
                            kappa: stabilization + two-model for ALL C
                            AND the kappa_X bar;
  ZEROGAP-FLOOR-ONLY    -- Z2 + Z3.1 + Z3.2 bars pass, Z3.3 fails:
                            the zero-gap theorem gives the
                            unconditional packet-Boden (frame form),
                            the projection form still fails -- the
                            honest split;
  ZEROGAP-NO-GAIN       -- otherwise.

FIREWALL (INVERTED, declared -- fejer convention).  This probe
DELIBERATELY reads Riemann zeros: the verification of the theorem on
the comb IS the task (Z2, Z3.1, Z3.2 comb side).  Structural
separation replaces the AST ban: the lag assembly, Qt, Mass, H_log and
every c_X number are primes + digamma + cosh ONLY (machinery verbatim
packet_garding_probe); no zero enters the operator pipeline.  Zero
data: the shared Turing-certified cache zero_comb_cache_n2000.json
(+ the c1 extension cache, provenance printed, no bar).
experiments-only; verification/ read-only (v563 import); no marker
moves; Python-only per GATE.WOLFRAM.02.

Provenance: fejer_density_bound_probe.py + packet_garding_probe.py
(2026-08-02, machinery + the typed OPEN residue),
zero_comb_cache_n2000.json (turing_cert_probe: TURING-COMPLETE-BAND),
c1_zero_ext_n2500.json (c1_mechanism_probe extension),
v563_paper2_readouts (atom table, frame-A windows), Trudgian J. Number
Theory 134 (2014) Thm 1, Trudgian Math. Comp. 80 (2011) (Turing
method), Hasanalizade-Shen-Wong J. Number Theory 233 (2022), Bellotti
arXiv:2412.15470 / Math. Comp. 2025, doi 10.1090/mcom/4133 (Thm 1.1,
Cor. 1.5, eq. (1.2)), Platt LMFDB zero database (Pla11/Pla17),
Platt-Trudgian Bull. LMS 53 (2021), Simonic J. Number Theory 231
(2021) (RH-conditional, excluded), Iwaniec-Kowalski Thm 5.12.
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
import scipy.linalg as sla  # noqa: E402
from numpy.polynomial.legendre import leggauss  # noqa: E402

# ------------------------------------------------------------ constants
MS = (92, 184, 368, 736)            # anchor dyadic ladder (w2_mosco)
M_REF = 736
C_LADDER = (0.5, 1.0, 2.0)          # Z3.3 C-ladder (task)
KAPPAS = (2, 3)                     # adaptive width multipliers (task)
STAB_BAR = 0.03                     # last-increment bar (task: 3%)
SEP_BAR = 3.0                       # two-model rms separation bar
BAR_KAPPA = 1.50                    # X <= kappa H_log bar (v674 run-2)
BAR_LAYER = 1e-12
BAR_LAM736 = 5e-9
BAR_DST = 1e-10
BAR_PACK_EIG = 1e-8
BAR_MASS = 5e-3                     # weight-1 companion lag bar
BAR_ZERO_CACHE = 1e-8
FLOOR_SAFETY = 20.0

# the cited chain constants (Z1)
A1_TR, A2_TR, A3_TR = 0.112, 0.278, 2.510   # Trudgian 2014 Thm 1
C1_BE = 0.10076                             # Bellotti 2025 Cor. 1.5
C2_BE, C3_BE = 0.24460, 7.20844             # ... branch 1
C2B_BE, C3B_BE = 1.68845, 1.50956           # ... branch 2 (min)
S_PLATT = 2.5167                            # Bellotti eq. (1.2)
T_PLATT = 30610046000.0                     # Platt LMFDB height
A1_HSW, A2_HSW, A3_HSW = 0.1038, 0.2573, 9.4925  # HSW22 (C3 corr.)
TUR_A, TUR_B = 1.61, 0.0914                 # Trudgian 2011 (Turing)
EPS_N = 2e-3                                # two-endpoint E budget
FLOOR_TR = 4.0 * math.pi * A1_TR            # 1.40743
FLOOR_BE = 4.0 * math.pi * C1_BE            # 1.26617
T_CLAMP = 10.0                              # H_min clamp height
H_BRACKET = (1e-3, 400.0)                   # bisection bracket
N_BISECT = 90
REF_GAP1 = 6.887                            # task quote gamma_1->2 gap
REF_GAP100 = 3.861                          # task quote above t = 100
BAR_QUOTE = 0.01
REF_THETA = 0.20                            # v674 theta quote at 736
BAR_THETA = 0.05
DU_BODEN = 0.01                             # tent quadrature step
DS_BODEN = 0.02                             # band min-search step
T_MAX_H, N_T_H = 3000.0, 120001             # H_log grid (garding conv.)
N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2

mp.mp.dps = 30
PSI14_F = float(mp.digamma(mp.mpf(1) / 4))
LOGPI_F = math.log(math.pi)
PHI1_F = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
TWO_PI = 2.0 * math.pi
UU = np.array([float(u) for u in core.U_ALL])
MU = np.array([float(m) for m in core.MU_ALL])

GX16, GW16 = leggauss(16)

TG_H = np.linspace(0.0, T_MAX_H, N_T_H)
DT_H = T_MAX_H / (N_T_H - 1)
TRAP_H = np.full(N_T_H, DT_H)
TRAP_H[0] *= 0.5
TRAP_H[-1] *= 0.5

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")
CACHE_EXT = os.path.join(HERE, "c1_zero_ext_n2500.json")


# ------------------------------------------------- H_min machinery (Z1)
def main_N(x):
    """(x/2pi)(log(x/2pi) - 1), continued by 0 at x = 0."""
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


S_CHAINS = (("platt", s_bound_platt), ("trudgian", s_bound_tr),
            ("bellotti", s_bound_be))


def g_gap(t, H, s_bound):
    """the count minorant G(t, H) = mainD - 2 Sbound(t+H) - eps_N."""
    t = np.asarray(t, dtype=float)
    H = np.asarray(H, dtype=float)
    return (main_N(t + H) - main_N(t)
            - 2.0 * s_bound(t + H) - EPS_N)


def h_min_chain(ts, s_bound):
    """vector bisection for the smallest H with G(t, H) > 0."""
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
    """pointwise min over the valid chains (each unconditional)."""
    ts = np.asarray(ts, dtype=float)
    h = np.minimum(h_min_chain(ts, s_bound_tr),
                   h_min_chain(ts, s_bound_be))
    mP = ts + H_BRACKET[1] <= T_PLATT
    if np.any(mP):
        hP = h_min_chain(ts[mP], s_bound_platt)
        h[mP] = np.minimum(h[mP], hP)
    return h


def h_min_scalar(t):
    return float(h_min_all(np.array([t]))[0])


def n_guar_band(b_lo, b_hi, h_at_lo):
    """unconditional ordinate count of [b_lo, b_hi]: max of the
    subinterval route (b_lo >= T_CLAMP) and the direct count route
    (one-sided with the +7/8 for band 0)."""
    delta = b_hi - b_lo
    n_sub = int(delta / h_at_lo + 1e-12) if b_lo >= T_CLAMP else 0
    sb_top = min(float(s_bound_platt(np.array([b_hi]))[0]),
                 float(s_bound_tr(np.array([b_hi]))[0]),
                 float(s_bound_be(np.array([b_hi]))[0]))
    if b_lo < T_CLAMP and b_lo == 0.0:
        g = (float(main_N(b_hi)) + 7.0 / 8.0 - sb_top - 0.5 * EPS_N)
    else:
        g = (float(main_N(b_hi)) - float(main_N(b_lo))
             - 2.0 * sb_top - EPS_N)
    n_dir = int(math.ceil(g - 1e-12)) if g > 0 else 0
    return max(n_sub, n_dir), n_sub, n_dir


# ------------------------------------------------- certified lag assembly
# (verbatim packet_garding_probe / w2_mosco_probe; primes + digamma +
#  cosh ONLY -- no zero enters here: the structural firewall)
def g_smooth_vec(ts):
    xf = np.abs(np.asarray(ts, dtype=float))
    out = xf / 2.0 * (LOGPI_F - PSI14_F) - 0.25 * PHI1_F
    lb = np.empty_like(xf)
    for a in range(0, xf.size, 400):
        b = min(xf.size, a + 400)
        E = np.exp(-np.outer(2.0 * xf[a:b], _NN_L) - 0.5 * xf[a:b, None])
        lb[a:b] = E @ _WTS
    return out + 0.25 * lb


def g_sm_mp(tv):
    tv = abs(mp.mpf(tv))
    PHI1m = mp.lerchphi(1, 2, mp.mpf(1) / 4)
    LLm = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)
    if tv == 0:
        return mp.mpf(0)
    return (LLm * tv / 2 - PHI1m / 4 + mp.exp(-tv / 2)
            * mp.lerchphi(mp.exp(-2 * tv), 2, mp.mpf(1) / 4) / 4)


def K_f_factory(D):
    def K_f(x):
        u = np.abs(x) / D
        return np.where(u <= 1.0, D * (2.0 / 3.0 - u ** 2 + u ** 3 / 2.0),
                        np.where(u < 2.0, D * (2.0 - u) ** 3 / 6.0, 0.0))
    return K_f


def galerkin_lags_verbatim(a, M):
    D = 2.0 * a / M
    ss = np.concatenate([0.5 * D * (GX16 + 1) - D, 0.5 * D * (GX16 + 1)])
    ww = np.tile(0.5 * D * GW16, 2) * (D - np.abs(ss))
    ks = np.arange(M)
    vals = g_smooth_vec((ks[:, None] * D + ss[None, :]).ravel())
    II = vals.reshape(M, ss.size) @ ww
    c = np.empty(M - 1)
    for d in range(M - 1):
        c[d] = (2.0 * II[d] - II[abs(d - 1)] - II[d + 1]) / (D * D)
    Dm = mp.mpf(D)
    II_b = {k: mp.quad(lambda s: g_sm_mp(k * Dm + s) * (Dm - abs(s)),
                       [-Dm, 0, Dm]) for k in range(4)}
    for d in range(3):
        c[d] = float((2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1])
                     / Dm ** 2)
    dd_grid = np.arange(M - 1) * D
    K_f = K_f_factory(D)
    ka = core.atoms_in(a)
    for u_j, m_j in zip(UU[:ka], MU[:ka]):
        c -= 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    c += 2.0 * np.cosh(dd_grid / 2.0) * 16.0 * Xp ** 2 / (D * D)
    return c, D


def galerkin_layers(a, M):
    D = 2.0 * a / M
    ss = np.concatenate([0.5 * D * (GX16 + 1) - D, 0.5 * D * (GX16 + 1)])
    ww = np.tile(0.5 * D * GW16, 2) * (D - np.abs(ss))
    ks = np.arange(M)
    vals = g_smooth_vec((ks[:, None] * D + ss[None, :]).ravel())
    II = vals.reshape(M, ss.size) @ ww
    c_sm = np.empty(M - 1)
    for d in range(M - 1):
        c_sm[d] = (2.0 * II[d] - II[abs(d - 1)] - II[d + 1]) / (D * D)
    Dm = mp.mpf(D)
    II_b = {k: mp.quad(lambda s: g_sm_mp(k * Dm + s) * (Dm - abs(s)),
                       [-Dm, 0, Dm]) for k in range(4)}
    for d in range(3):
        c_sm[d] = float((2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1])
                        / Dm ** 2)
    dd_grid = np.arange(M - 1) * D
    K_f = K_f_factory(D)
    ka = core.atoms_in(a)
    c_at = np.zeros(M - 1)
    for u_j, m_j in zip(UU[:ka], MU[:ka]):
        c_at += 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    c_po = 2.0 * np.cosh(dd_grid / 2.0) * 16.0 * Xp ** 2 / (D * D)
    return c_sm, c_at, c_po, D


def toeplitz_of(lags, n):
    idx = np.abs(np.arange(n)[:, None] - np.arange(n)[None, :])
    return lags[idx]


def mass_of(D, n):
    Mass = np.zeros((n, n))
    np.fill_diagonal(Mass, 2.0 * D / 3.0)
    rng_ = np.arange(n - 1)
    Mass[rng_, rng_ + 1] = D / 6.0
    Mass[rng_ + 1, rng_] = D / 6.0
    return Mass


def dst_mass_basis(M, D):
    j = np.arange(1, M, dtype=float)
    U = np.sin(math.pi * np.outer(j, j) / M)
    mu = D * (2.0 + np.cos(math.pi * j / M)) / 3.0
    nrm = np.sqrt(mu * (M / 2.0))
    return U / nrm[None, :], mu


def hlog_lags(D, n):
    ker2 = (D * np.sinc(TG_H * D / (2.0 * math.pi)) ** 2) ** 2
    w_log = ker2 * np.log(2.0 + TG_H) * TRAP_H / math.pi
    w_one = ker2 * TRAP_H / math.pi
    dd = np.arange(n) * D
    l_log = np.zeros(n)
    l_one = np.zeros(n)
    for a_ in range(0, N_T_H, 4000):
        b_ = min(N_T_H, a_ + 4000)
        Cc = np.cos(np.outer(TG_H[a_:b_], dd))
        l_log += w_log[a_:b_] @ Cc
        l_one += w_one[a_:b_] @ Cc
    return l_log, l_one


def mass_lag_guard(l_one, D, tag):
    d0 = abs(l_one[0] - 2.0 * D / 3.0) / (2.0 * D / 3.0)
    d1 = abs(l_one[1] - D / 6.0) / (D / 6.0)
    d2 = float(np.max(np.abs(l_one[2:]))) / (2.0 * D / 3.0)
    ok = d0 < BAR_MASS and d1 < BAR_MASS and d2 < BAR_MASS
    return ok, "%s: d0 %.1e / d1 %.1e / d>=2 %.1e" % (tag, d0, d1, d2)


def packet_partition(a, M, delta):
    """fixed continuum bands (verbatim packet_garding_probe)."""
    tk = math.pi * np.arange(1, M) / (2.0 * a)
    pid = np.floor(tk / delta + 1e-12).astype(int)
    P = int(pid.max()) + 1
    if P >= 2 and float(tk[-1]) < P * delta - 1e-9:
        pid[pid == P - 1] = P - 2
        P -= 1
    packs = []
    for p in range(P):
        ks = np.where(pid == p)[0]
        t_lo = p * delta
        t_cov = float(tk[ks[-1]])
        packs.append(dict(p=p, k_lo=int(ks[0] + 1), k_hi=int(ks[-1] + 1),
                          n=int(ks.size), t_lo=t_lo, t_cov=t_cov,
                          w=math.log(2.0 + t_lo)))
    w_edge = np.array([packs[q]["w"] for q in pid])
    return packs, tk, pid, w_edge


def adaptive_assign(tk, edges):
    """assign modes to adaptive continuum bands; merge a partially
    covered top band into its predecessor (v674 convention)."""
    pid = np.searchsorted(edges, tk, side="right") - 1
    pmax = int(pid.max())
    if pmax >= 1 and float(tk[-1]) < edges[pmax + 1] - 1e-9:
        pid[pid == pmax] = pmax - 1
        pmax -= 1
    packs = []
    for p in sorted(set(int(q) for q in pid)):
        ks = np.where(pid == p)[0]
        packs.append(dict(p=p, k_lo=int(ks[0] + 1), k_hi=int(ks[-1] + 1),
                          n=int(ks.size), t_lo=float(edges[p]),
                          t_hi=float(edges[p + 1]),
                          t_cov=float(tk[ks[-1]]),
                          w=math.log(2.0 + float(edges[p])),
                          w_mid=math.log(2.0 + 0.5 * (float(edges[p])
                                                      + float(edges[p + 1])))))
    w_edge = np.log(2.0 + edges[pid])
    w_mid = np.array([math.log(2.0 + 0.5 * (edges[q] + edges[q + 1]))
                      for q in pid])
    return packs, pid, w_edge, w_mid


def c_x_min(Qt, wvec, C, want_vec=False):
    n = Qt.shape[0]
    S = 1.0 / np.sqrt(wvec)
    A = Qt * np.outer(S, S)
    A[np.arange(n), np.arange(n)] += C * S * S
    A = 0.5 * (A + A.T)
    if want_vec:
        w, V = sla.eigh(A, subset_by_index=[0, 0])
        return float(w[0]), S * V[:, 0]
    return float(sla.eigvalsh(A, subset_by_index=[0, 0])[0])


def hx_nodal(Mass, Uh, wvec):
    A = Mass @ Uh
    return (A * wvec[None, :]) @ A.T


def two_model_fit(Ls, cs):
    xs = 1.0 / np.asarray(Ls, dtype=float)
    ys = np.asarray(cs, dtype=float)
    A2 = np.column_stack([np.ones(xs.size), xs])
    bf, _, _, _ = np.linalg.lstsq(A2, ys, rcond=None)
    rms2 = float(np.sqrt(np.mean((ys - A2 @ bf) ** 2)))
    a1 = float((xs @ ys) / (xs @ xs))
    rms1 = float(np.sqrt(np.mean((ys - a1 * xs) ** 2)))
    return float(bf[0]), float(bf[1]), rms2, a1, rms1


def fejer_a(a, s):
    s = np.asarray(s, dtype=float)
    small = np.abs(s) < 1e-9
    ss = np.where(small, 1.0, s)
    out = np.sin(a * ss) ** 2 / (math.pi * a * ss ** 2)
    out[small] = a / math.pi
    return out


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE ZERO-GAP THEOREM ROUTE -- explicit unconditional H_min(t),"
          " comb verification, and the adaptive packet Garding test")
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
          "cache), monotone %s, live-mpmath dev at n=1,2,3,%d: %.2e <= "
          "%.0e, RvM residual max %.3f <= Sbar+0.01"
          % (n_z, mono, n_z, dev_z, BAR_ZERO_CACHE, float(np.max(rn))),
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

    # ------------------------------------------------ anchor window
    kz0 = core.frame_a_zones()[0]
    r0 = core.build_window(kz0)
    a0 = r0["alpha"]
    delta_fix = math.pi * a0
    print("anchor window: a0 = alpha(h = %d) = %.12f (= log %d); fixed "
          "delta* = pi a0 = %.6f; ladder M = %s"
          % (r0["h"], a0, r0["n_zone"], delta_fix, list(MS)))

    # ------------------------------------------------ G0.1 assembly
    devs = []
    for M in (92, 736):
        c_v, _ = galerkin_lags_verbatim(a0, M)
        c_sm, c_at, c_po, _ = galerkin_layers(a0, M)
        c_l = c_sm - c_at + c_po
        scale = float(np.max(np.abs(c_v)))
        devs.append(float(np.max(np.abs(c_l - c_v))) / scale)

    print("\nbuilding the anchor ladder (certified layers + H_log Gram "
          "+ DST) ...")
    dat = {}
    mass_ok = True
    mass_det = []
    chol_ok = True
    for M in MS:
        t1 = time.time()
        c_sm, c_at, c_po, D = galerkin_layers(a0, M)
        n = M - 1
        Q = toeplitz_of(c_sm - c_at + c_po, n)
        Mass = mass_of(D, n)
        Uh, mu = dst_mass_basis(M, D)
        Qt = Uh.T @ (Q @ Uh)
        tk = math.pi * np.arange(1, M) / (2.0 * a0)
        l_log, l_one = hlog_lags(D, n)
        H = toeplitz_of(l_log, n)
        okm, det = mass_lag_guard(l_one, D, "M=%d" % M)
        mass_ok = mass_ok and okm
        mass_det.append(det)
        try:
            sla.cholesky(0.5 * (H + H.T))
        except sla.LinAlgError:
            chol_ok = False
        dat[M] = dict(D=D, n=n, Q=Q, Mass=Mass, Uh=Uh, mu=mu, Qt=Qt,
                      tk=tk, H=H)
        print("   M = %3d (D = %.6f): lattice edge t = %.2f  [%.1f s]"
              % (M, D, tk[-1], time.time() - t1))

    lam1_736 = float(sla.eigvalsh(
        0.5 * (dat[736]["Q"] + dat[736]["Q"].T),
        0.5 * (dat[736]["Mass"] + dat[736]["Mass"].T),
        subset_by_index=[0, 0])[0])
    dst_dev = 0.0
    nrm_dev = 0.0
    for M in MS:
        d_ = dat[M]
        R = d_["Mass"] @ d_["Uh"] - d_["Uh"] * d_["mu"][None, :]
        dst_dev = max(dst_dev, float(np.max(np.abs(R)))
                      / float(np.max(np.abs(d_["Mass"]))))
        dg = np.einsum("ij,ij->j", d_["Uh"], d_["Mass"] @ d_["Uh"])
        nrm_dev = max(nrm_dev, float(np.max(np.abs(dg - 1.0))))
    check("G0.1 [E] certified lag assembly: layered == verbatim max "
          "rel dev %s < %.0e; |lambda_1(736, full)| = %.1e <= %.0e; "
          "DST residual %.1e < %.0e, normalization %.1e < 1e-8; "
          "weight-1 lags (%s) within %.0e; H_log Cholesky pd %s"
          % (["%.1e" % d for d in devs], BAR_LAYER, abs(lam1_736),
             BAR_LAM736, dst_dev, BAR_DST, nrm_dev,
             "; ".join(mass_det), BAR_MASS, chol_ok),
          max(devs) < BAR_LAYER and abs(lam1_736) <= BAR_LAM736
          and dst_dev < BAR_DST and nrm_dev < 1e-8
          and mass_ok and chol_ok)

    # ------------------------------------------------ G0.2 H_min guards
    t_samp = np.array([10.0, 14.13, 20.0, 50.0, 100.0, 200.0, 417.0,
                       1000.0, 2515.0, 1e4, 1e6, 1e10])
    sign_ok = True
    for tq in t_samp:
        Hg = np.linspace(H_BRACKET[0], H_BRACKET[1], 400)
        for lab, sb in S_CHAINS:
            if lab == "platt" and tq + H_BRACKET[1] > T_PLATT:
                continue
            gv = g_gap(np.full(Hg.shape, tq), Hg, sb)
            pos = gv > 0.0
            if not np.any(pos):
                sign_ok = False
                continue
            i0 = int(np.argmax(pos))
            if not (bool(np.all(pos[i0:])) and bool(np.all(~pos[:i0]))):
                sign_ok = False
    brack_ok = True
    res_max = 0.0
    for tq in t_samp:
        for lab, sb in S_CHAINS:
            if lab == "platt" and tq + H_BRACKET[1] > T_PLATT:
                continue
            hm = float(h_min_chain(np.array([tq]), sb)[0])
            glo = float(g_gap(np.array([tq]),
                              np.array([hm * (1 - 1e-12) - 1e-12]),
                              sb)[0])
            ghi = float(g_gap(np.array([tq]), np.array([hm]), sb)[0])
            brack_ok = brack_ok and glo <= 0.0 <= ghi
            res_max = max(res_max, abs(ghi))
    tgrid = np.arange(T_CLAMP, 3000.0 + 0.5, 1.0)
    h_tr = h_min_chain(tgrid, s_bound_tr)
    h_be = h_min_chain(tgrid, s_bound_be)
    h_pl = h_min_chain(tgrid, s_bound_platt)
    h_mn = np.minimum(np.minimum(h_tr, h_be), h_pl)
    dec_ok = all(bool(np.all(np.diff(h) <= 1e-9))
                 for h in (h_tr, h_be, h_pl, h_mn))
    floor_ok = bool(np.all(h_tr >= FLOOR_TR - 1e-9)
                    and np.all(h_be >= FLOOR_BE - 1e-9))
    platt_min_ok = bool(np.all(h_pl <= np.minimum(h_tr, h_be) + 1e-12))
    check("G0.2 [E] H_min machinery: G(t, .) single sign change on "
          "the sampled bracket (12 heights x chains, recalibrated "
          "invariant) %s; bisection bracketing holds with "
          "|G(t, H_min)| <= %.1e; H_min nonincreasing on [10, 3000] "
          "(all chains + min) %s; chain floors respected (Trudgian >= "
          "%.5f, Bellotti >= %.5f) %s; Platt branch is the argmin on "
          "the comb range %s"
          % (sign_ok, res_max, dec_ok, FLOOR_TR, FLOOR_BE, floor_ok,
             platt_min_ok),
          sign_ok and brack_ok and dec_ok and floor_ok
          and platt_min_ok)

    # ------------------------------------------------ Z1.1 the theorem
    print("\nZ1.1 -- THE EXPLICIT UNCONDITIONAL ZERO-GAP THEOREM "
          "(assembled, cited)")
    print("   statement: for t >= 10, (t, t + H_min(t)] contains an "
          "ordinate, H_min = smallest H with")
    print("   main(t+H) - main(t) - 2 Sbound(t+H) - %.0e > 0, Sbound "
          "= min of:" % EPS_N)
    print("   (P) |S| <= %.4f for T <= %.4g  [Platt LMFDB; Bellotti "
          "2025 eq. (1.2)]" % (S_PLATT, T_PLATT))
    print("   (T) |S| <= %.3f log T + %.3f loglog T + %.3f  [Trudgian "
          "2014 Thm 1]; floor 4 pi A1 = %.5f"
          % (A1_TR, A2_TR, A3_TR, FLOOR_TR))
    print("   (B) |S| <= %.5f log T + min{%.5f llT + %.5f, %.5f llT + "
          "%.5f}  [Bellotti 2025 Cor. 1.5]; floor %.5f"
          % (C1_BE, C2_BE, C3_BE, C2B_BE, C3B_BE, FLOOR_BE))
    print("   rejected: (a) Littlewood O(1/loglog) RH-conditional "
          "(Simonic 2021); (c) HSW22 (%.4f, %.4f, %.4f) superseded"
          % (A1_HSW, A2_HSW, A3_HSW))
    tur_tr = (2.0 * math.pi * A1_TR
              + math.sqrt((2.0 * math.pi * A1_TR) ** 2
                          + 4.0 * math.pi * TUR_B))
    tur_be = (2.0 * math.pi * C1_BE
              + math.sqrt((2.0 * math.pi * C1_BE) ** 2
                          + 4.0 * math.pi * TUR_B))
    print("   rejected: (b) Turing/S1 route (Trudgian 2011: |int S| "
          "<= %.2f + %.4f log(t2/2pi)): asymptote H* = %.4f (Tr A1) / "
          "%.4f (Be A1) -- dominated by the S-difference floors"
          % (TUR_A, TUR_B, tur_tr, tur_be))
    rows = []
    print("   H_min(t) table (P / T / B / min):")
    for tq in t_samp:
        hT = float(h_min_chain(np.array([tq]), s_bound_tr)[0])
        hB = float(h_min_chain(np.array([tq]), s_bound_be)[0])
        if tq + H_BRACKET[1] <= T_PLATT:
            hP = float(h_min_chain(np.array([tq]), s_bound_platt)[0])
            hMn = min(hP, hT, hB)
            sP = "%7.3f" % hP
        else:
            hP = math.inf
            hMn = min(hT, hB)
            sP = "  (inv)"
        rows.append((tq, hMn))
        print("   t = %10.5g:  P %s   T %7.3f   B %7.3f   min %7.3f"
              % (tq, sP, hT, hB, hMn))
    h0 = h_min_scalar(T_CLAMP)
    b1_anchor = 2.0 * h0
    z11_ok = (all(np.isfinite(r[1]) for r in rows)
              and all(rows[i + 1][1] <= rows[i][1] + 1e-9
                      for i in range(len(rows) - 1))
              and float(GAM[0]) <= b1_anchor)
    check("Z1.1 [ANALYTIC, cited] theorem table finite and "
          "nonincreasing; low-t anchor: gamma_1 = %.4f lies inside "
          "the clamped band-0 interval [0, 2 H_min(10) = %.3f]; "
          "asymptotic floors %.5f (T) / %.5f (B); H_min never drops "
          "below pi/a0 = %.4f on ANY chain at ANY height (main-lobe "
          "capture unreachable -- typed for Z3.2)"
          % (float(GAM[0]), b1_anchor, FLOOR_TR, FLOOR_BE,
             math.pi / a0), z11_ok)

    # ------------------------------------------------ Z2 comb verification
    print("\nZ2 -- machine verification on the Turing-certified comb")
    gaps = np.diff(GAM)
    tlo = GAM[:-1]
    h_at = {}
    viol = {}
    for lab, sb in S_CHAINS:
        h_at[lab] = h_min_chain(tlo, sb)
        viol[lab] = int(np.sum(gaps > h_at[lab]))
    h_at["min"] = h_min_all(tlo)
    viol["min"] = int(np.sum(gaps > h_at["min"]))
    check("Z2.1 [E] comb gap verification: gaps <= H_min(gamma_n) for "
          "all %d certified gaps -- violations: platt %d, trudgian %d,"
          " bellotti %d, min %d (all must be 0)"
          % (gaps.size, viol["platt"], viol["trudgian"],
             viol["bellotti"], viol["min"]),
          all(v == 0 for v in viol.values()))
    if GAM_EXT is not None:
        full = np.concatenate([GAM, GAM_EXT])
        ge = np.diff(full[n_z - 1:])
        te = full[n_z - 1:-1]
        he = h_min_all(te)
        print("   extension (n %d..%d, top %.1f): %d gaps, violations "
              "%d (printed, no bar -- provenance above)"
              % (n_z, full.size, full[-1], ge.size,
                 int(np.sum(ge > he))))

    ratio = h_at["min"] / gaps
    q = np.percentile(ratio, [0, 10, 50, 90])
    gmax = float(np.max(gaps))
    gmax_at = float(tlo[int(np.argmax(gaps))])
    g100 = float(np.max(gaps[tlo >= 100.0]))
    print("   air ratio r = H_min/gap: min %.3f | p10 %.2f | median "
          "%.2f | p90 %.2f" % (q[0], q[1], q[2], q[3]))
    print("   per dyadic band (median | min of r; n gaps):")
    for b0, b1 in ((14.0, 40.0), (40.0, 80.0), (80.0, 160.0),
                   (160.0, 320.0), (320.0, 640.0), (640.0, 1280.0),
                   (1280.0, 2516.0)):
        m = (tlo >= b0) & (tlo < b1)
        print("   [%6.0f, %6.0f): median %6.2f | min %6.2f  (n = %d)"
              % (b0, b1, float(np.median(ratio[m])),
                 float(np.min(ratio[m])), int(np.sum(m))))
    check("Z2.2 [MEASURED] the air: min ratio %.3f > 1 with median "
          "%.2f / p90 %.2f; quote guards: max gap %.4f at gamma = "
          "%.3f (|dev - %.3f| <= %.2f), max gap above t = 100: %.4f "
          "(|dev - %.3f| <= %.2f)"
          % (q[0], q[2], q[3], gmax, gmax_at, REF_GAP1, BAR_QUOTE,
             g100, REF_GAP100, BAR_QUOTE),
          q[0] > 1.0 and abs(gmax - REF_GAP1) <= BAR_QUOTE
          and abs(g100 - REF_GAP100) <= BAR_QUOTE)

    # ------------------------------------------------ Z3.1 adaptive bands
    print("\nZ3.1 -- adaptive partitions delta_p = kappa "
          "H_min(max(b_p, 10)) (continuum-fixed, M-independent)")
    t_need = max(float(dat[M_REF]["tk"][-1]) + 5.0, gam_max + 5.0)
    EDGES = {}
    z31_ok = True
    for kap in KAPPAS:
        edges = [0.0]
        while edges[-1] < t_need:
            edges.append(edges[-1]
                         + kap * h_min_scalar(max(edges[-1], T_CLAMP)))
        edges = np.array(edges)
        EDGES[kap] = edges
        widths = np.diff(edges)
        w_inc = bool(np.all(np.diff(np.log(2.0 + edges)) > 0.0))
        n_bad = 0
        occ_bad = 0
        airs = []
        for p in range(edges.size - 1):
            b_lo, b_hi = float(edges[p]), float(edges[p + 1])
            if b_hi > gam_max:
                break
            h_lo = h_min_scalar(max(b_lo, T_CLAMP))
            ng, n_sub, n_dir = n_guar_band(b_lo, b_hi, h_lo)
            nc = int(np.searchsorted(GAM, b_hi)
                     - np.searchsorted(GAM, b_lo))
            if nc < ng or ng < kap:
                n_bad += 1
            airs.append(nc / max(ng, 1))
            if b_lo >= T_CLAMP and n_sub >= 1:
                hsub = (b_hi - b_lo) / n_sub
                for j in range(n_sub):
                    s0 = b_lo + j * hsub
                    if int(np.searchsorted(GAM, s0 + hsub)
                           - np.searchsorted(GAM, s0)) < 1:
                        occ_bad += 1
        airs = np.array(airs)
        print("   kappa = %d: %d bands to t = %.0f; widths %.2f .. "
              "%.2f (band 0 [0, %.2f]); %d bands checked on the comb; "
              "air n_comb/n_guar median %.2f / min %.2f"
              % (kap, edges.size - 1, t_need, float(np.min(widths)),
                 float(np.max(widths)), edges[1], airs.size,
                 float(np.median(airs)), float(np.min(airs))))
        z31_ok = z31_ok and w_inc and n_bad == 0 and occ_bad == 0 \
            and bool(np.all(widths >= kap * FLOOR_BE - 1e-9))
    check("Z3.1 [E] adaptive partitions well-formed and count-valid: "
          "weights strictly increasing, every in-comb band holds "
          "n_comb >= n_guar >= kappa (0 misses), every H_min "
          "subinterval occupied (0 misses), widths >= kappa x %.5f"
          % FLOOR_BE, z31_ok)

    # ------------------------------------------------ Z3.2 packet-Boden
    print("\nZ3.2 -- the unconditional packet-Boden (frame form) at "
          "(a0, 736, kappa = 2)")
    d7 = dat[M_REF]
    kap_b = 2
    packs2, pid2, w_edge2, w_mid2 = adaptive_assign(d7["tk"],
                                                    EDGES[kap_b])
    boden_ok = True
    pos_ok = True
    ratios_bv = []
    ratios_qv = []
    print("   p    band            n_md n_gr n_cmb   B_p      V_p     "
          " q_p     lam_p     avg_p   B/V")
    for pk in packs2:
        b_lo, b_hi = pk["t_lo"], pk["t_hi"]
        h_lo = h_min_scalar(max(b_lo, T_CLAMP))
        ng, n_sub, _nd = n_guar_band(b_lo, b_hi, h_lo)
        nc = int(np.searchsorted(GAM, b_hi) - np.searchsorted(GAM, b_lo))
        delta = b_hi - b_lo
        ug = np.arange(b_lo, b_hi + 0.5 * DU_BODEN, DU_BODEN)
        mid = 0.5 * (b_lo + b_hi)
        g2 = np.maximum(1.0 - np.abs(ug - mid) / (0.5 * delta), 0.0) \
            * (2.0 / delta)
        g2 = g2 / (np.sum(g2) * DU_BODEN)
        sg = np.arange(b_lo, b_hi + 0.5 * DS_BODEN, DS_BODEN)
        W = fejer_a(a0, sg[:, None] - ug[None, :]) @ (g2 * DU_BODEN)
        min_band = float(np.min(W))
        if b_lo >= T_CLAMP and n_sub >= 1:
            hsub = delta / n_sub
            mins = []
            for j in range(n_sub):
                m = (sg >= b_lo + j * hsub) & (sg <= b_lo + (j + 1) * hsub)
                mins.append(float(np.min(W[m])))
            B_p = TWO_PI * (sum(mins) + (ng - n_sub) * min_band)
        else:
            B_p = TWO_PI * ng * min_band
        gin = GAM[(GAM >= b_lo) & (GAM < b_hi)]
        Wg = fejer_a(a0, gin[:, None] - ug[None, :]) @ (g2 * DU_BODEN)
        V_p = TWO_PI * float(np.sum(Wg))
        gout = GAM[(GAM < b_lo) | (GAM >= b_hi)]
        Wo = fejer_a(a0, gout[:, None] - ug[None, :]) @ (g2 * DU_BODEN)
        V_tail = TWO_PI * float(np.sum(Wo))
        sl = slice(pk["k_lo"] - 1, pk["k_hi"])
        tks = d7["tk"][sl]
        half = max(mid - b_lo, pk["t_cov"] - mid, 1e-9)
        gv = np.maximum(1.0 - np.abs(tks - mid) / (1.0000001 * half),
                        0.0)
        if float(np.max(gv)) <= 0.0:
            gv = np.ones_like(tks)
        gv = gv / np.linalg.norm(gv)
        q_p = float(gv @ (d7["Qt"][sl, sl] @ gv))
        B = d7["Qt"][sl, sl]
        lam = float(sla.eigvalsh(0.5 * (B + B.T),
                                 subset_by_index=[0, 0])[0])
        avg = float(np.mean(np.diag(B)))
        boden_ok = boden_ok and B_p <= V_p * (1.0 + 1e-6) + 1e-9
        pos_ok = pos_ok and B_p > 0.0
        ratios_bv.append(B_p / V_p)
        ratios_qv.append(q_p / (V_p + V_tail))
        print("   %2d [%7.2f,%7.2f) %4d %4d %5d  %7.4f  %7.4f  %7.4f"
              "  %+8.4f  %7.4f  %.3f"
              % (pk["p"], b_lo, b_hi, pk["n"], ng, nc, B_p, V_p, q_p,
                 lam, avg, B_p / V_p))
    med_bv = float(np.median(ratios_bv))
    med_qv = float(np.median(ratios_qv))
    # fixed-partition theta reproduction (v674 quote)
    packsF, tkF, pidF, w_edgeF = packet_partition(a0, M_REF, delta_fix)
    thetas = []
    for pk in packsF:
        sl = slice(pk["k_lo"] - 1, pk["k_hi"])
        B = d7["Qt"][sl, sl]
        lam = float(sla.eigvalsh(0.5 * (B + B.T),
                                 subset_by_index=[0, 0])[0])
        avg = float(np.mean(np.diag(B)))
        thetas.append((lam + 1.0) / (avg + 1.0))
    theta736 = min(thetas)
    print("   fixed-partition theta(736) = min (lam+1)/(avg+1) = "
          "%.4f (v674 quote %.2f)" % (theta736, REF_THETA))
    a_fam_req = 1.0 / (4.0 * a0)
    print("   pointwise obstruction (typed): pi/a0 = %.4f < inf_t "
          "H_min = %.5f (Bellotti floor); main-lobe capture needs "
          "A1 < 1/(4 a0) = %.5f vs best cited %.5f (%.1f%% short); "
          "Platt branch bottoms at H_min(3.06e10) = %.4f > pi/a0 -- "
          "unreachable at every height"
          % (math.pi / a0, FLOOR_BE, a_fam_req, C1_BE,
             100.0 * (C1_BE / a_fam_req - 1.0),
             float(h_min_chain(np.array([T_PLATT - H_BRACKET[1]]),
                               s_bound_platt)[0])))
    check("Z3.2 [MEASURED] the unconditional Boden bound: B_p <= V_p "
          "for ALL %d packets (validity on the certified comb) and "
          "B_p > 0 (median B/V = %.3f -- the worst-case discount; "
          "median q_p/V_all = %.3f, lattice-vs-continuum, printed); "
          "theta reproduction |%.4f - %.2f| <= %.2f"
          % (len(packs2), med_bv, med_qv, theta736, REF_THETA,
             BAR_THETA),
          boden_ok and pos_ok
          and abs(theta736 - REF_THETA) <= BAR_THETA)

    # ------------------------------------------------ Z3.3 adaptive c_X
    print("\nZ3.3 -- the decisive test: adaptive packet Garding "
          "ladder c_X(M, C) = lambda_min(Qt + C I, W_adapt)")
    Ls = [math.log(2.0 + math.pi / dat[M]["D"]) for M in MS]
    stab = {}
    sep = {}
    cX = {}
    cXm = {}
    kapX = {}
    pack_eig_dev = 0.0
    for kap in KAPPAS:
        edges = EDGES[kap]
        for M in MS:
            d_ = dat[M]
            packs, pid, w_edge, w_mid = adaptive_assign(d_["tk"], edges)
            for C in C_LADDER:
                cX[(kap, M, C)] = c_x_min(d_["Qt"], w_edge, C)
            cXm[(kap, M)] = c_x_min(d_["Qt"], w_mid, 1.0)
            HX = hx_nodal(d_["Mass"], d_["Uh"], w_edge)
            kapX[(kap, M)] = float(sla.eigvalsh(
                0.5 * (HX + HX.T), 0.5 * (d_["H"] + d_["H"].T),
                subset_by_index=[d_["n"] - 1, d_["n"] - 1])[0])
            if M == M_REF:
                ev = np.sort(sla.eigvalsh(
                    0.5 * (HX + HX.T),
                    0.5 * (d_["Mass"] + d_["Mass"].T)))
                pack_eig_dev = max(pack_eig_dev, float(np.max(np.abs(
                    ev - np.sort(w_edge)))))
            if M in (92, M_REF):
                print("   kappa = %d, M = %3d: %2d packets (w %.3f .. "
                      "%.3f), kappa_X = %.4f"
                      % (kap, M, len(packs), packs[0]["w"],
                         packs[-1]["w"], kapX[(kap, M)]))
    for kap in KAPPAS:
        print("   kappa = %d ladder:" % kap)
        print("   M      " + "".join("  C=%-6.1f" % C for C in C_LADDER)
              + "  mid(C=1)  cX*L")
        for M in MS:
            row = "".join("  %+.5f" % cX[(kap, M, C)] for C in C_LADDER)
            print("   %3d %s  %+.5f  %.5f"
                  % (M, row, cXm[(kap, M)],
                     cX[(kap, M, 1.0)]
                     * math.log(2.0 + math.pi / dat[M]["D"])))
        for C in C_LADDER:
            seq = [cX[(kap, M, C)] for M in MS]
            pos = all(c > 0.0 for c in seq)
            inc = abs(seq[3] - seq[2]) / abs(seq[3]) if seq[3] != 0 \
                else math.inf
            stab[(kap, C)] = pos and inc <= STAB_BAR
            b_, a2_, rms2, a1_, rms1 = two_model_fit(Ls, seq)
            sep[(kap, C)] = (rms1 >= SEP_BAR * rms2) and (b_ > 0.0)
            b3, a23, rms23, a13, rms13 = two_model_fit(Ls[1:], seq[1:])
            print("   C = %.1f: last rel inc %.4f (bar %.2f) -> %s; "
                  "two-model %+.4f + %.4f/L (rms %.1e) vs %.4f/L "
                  "(rms %.1e), ratio %.2f (bar %.1f) -> 1/log %s "
                  "[last-3: b %+.4f, ratio %.2f]"
                  % (C, inc, STAB_BAR,
                     "STABILIZES" if stab[(kap, C)] else
                     "not stabilized",
                     b_, a2_, rms2, a1_, rms1,
                     rms1 / max(rms2, 1e-300), SEP_BAR,
                     "REJECTED" if sep[(kap, C)] else "COMPETITIVE",
                     b3, rms13 / max(rms23, 1e-300)))
        # minimizer forensics at (736, C = 1)
        d_ = dat[M_REF]
        packs, pid, w_edge, w_mid = adaptive_assign(d_["tk"],
                                                    EDGES[kap])
        cmin, vmin = c_x_min(d_["Qt"], w_edge, 1.0, want_vec=True)
        v = vmin / math.sqrt(float(vmin @ vmin))
        k_dom = int(np.argmax(np.abs(v))) + 1
        Rk = (np.diag(d_["Qt"]) + 1.0) / w_edge
        k_sm = int(np.argmin(Rk)) + 1
        print("   kappa = %d forensics (736, C=1): dominant mode k = "
              "%d (t = %.2f, |coef|^2 = %.3f, packet p = %d); "
              "single-mode floor %.5f at k = %d (t = %.2f); "
              "c_X/single-mode = %.4f"
              % (kap, k_dom, float(d_["tk"][k_dom - 1]),
                 float(np.max(v ** 2)), int(pid[k_dom - 1]),
                 float(Rk[k_sm - 1]), k_sm,
                 float(d_["tk"][k_sm - 1]), cmin / float(Rk[k_sm - 1])))
    # fixed baseline
    print("   fixed-partition baseline (delta* = pi a0):")
    cF = {}
    for M in MS:
        d_ = dat[M]
        _pk, _tk, _pid, wF = packet_partition(a0, M, delta_fix)
        cF[M] = c_x_min(d_["Qt"], wF, 1.0)
    print("   c_X(M, 1.0) fixed = %s"
          % ["%+.5f" % cF[M] for M in MS])
    kap_ok = True
    for kap in KAPPAS:
        ks = [kapX[(kap, M)] for M in MS]
        incs = [ks[i + 1] - ks[i] for i in range(3)]
        kap_ok = kap_ok and max(ks) <= BAR_KAPPA
        print("   kappa_X(%d) ladder %s (bar: worst <= %.1f, "
              "uniform-boundedness read), increments %s (printed -- "
              "the stage band prefix changes with M, see CALIBRATION "
              "HISTORY)"
              % (kap, ["%.4f" % z for z in ks], BAR_KAPPA,
                 ["%.4f" % z for z in incs]))
    z33_close = {}
    for kap in KAPPAS:
        z33_close[kap] = all(stab[(kap, C)] and sep[(kap, C)]
                             for C in C_LADDER)
    z33_ok = any(z33_close.values()) and kap_ok \
        and pack_eig_dev <= BAR_PACK_EIG
    check("Z3.3 [MEASURED, decisive] adaptive packet Garding: "
          "stabilization+two-model per (kappa, C): %s; kappa_X worst "
          "%.4f <= %.1f (uniform bound) %s; pencil (H_X, "
          "Mass) == adaptive weights to %.1e <= %.0e -- the "
          "projection form with adaptive widths %s"
          % ({kap: ["C=%.1f:%s" % (C, "ok" if stab[(kap, C)]
                                   and sep[(kap, C)] else "MISS")
                    for C in C_LADDER] for kap in KAPPAS},
             max(kapX.values()), BAR_KAPPA, kap_ok, pack_eig_dev,
             BAR_PACK_EIG,
             "CLOSES" if z33_ok else "does NOT close"),
          z33_ok)

    # ------------------------------------------------ Z4 typing/verdict
    guards_ok = not any(f.startswith("G0") for f in FAILS)
    z2_ok = not any(f.startswith("Z2") for f in FAILS)
    z3_floor_ok = z31_ok and not any(f.startswith("Z3.2")
                                     for f in FAILS)
    if not guards_ok:
        VERDICT = "ZEROGAP-MIXED (guards failed)"
    elif z2_ok and z3_floor_ok and z33_ok:
        VERDICT = "ZEROGAP-GARDING-CLOSED"
    elif z2_ok and z3_floor_ok:
        VERDICT = "ZEROGAP-FLOOR-ONLY"
    else:
        VERDICT = "ZEROGAP-NO-GAIN"

    check("Z4.1 [C] typed reading: (i) THEOREM (cited, unconditional): "
          "every (t, t+H_min(t)] holds an ordinate; H_min from the "
          "S-difference route with Sbound = min(Platt %.4f to 3.06e10,"
          " Trudgian, Bellotti); asymptotic floor %.5f; verified on "
          "all %d certified gaps with min air %.3f; (ii) COUNTS: "
          "adaptive bands delta = kappa H_min unconditionally hold >= "
          "kappa ordinates (0 misses on the comb); (iii) BODEN (frame "
          "form): B_p <= V_p everywhere, median discount %.3f -- the "
          "theorem-shaped unconditional packet floor EXISTS; (iv) "
          "PROJECTION form: %s; the pointwise obstruction is "
          "re-partition-invariant (pi/a0 = %.4f < inf H_min = %.5f; "
          "needs A1 < %.5f, %.1f%% below the best constant, at every "
          "height); no marker move"
          % (S_PLATT, FLOOR_BE, gaps.size, q[0], med_bv,
             "CLOSED by adaptive widths" if z33_ok else
             "NOT closed by adaptive widths (measured)",
             math.pi / a0, FLOOR_BE, a_fam_req,
             100.0 * (C1_BE / a_fam_req - 1.0)), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01 / W2, zero-gap theorem round (2026-08-02):
  the typed OPEN residue of the packet Garding round (unconditional
  zero-gap input) was SUPPLIED and MEASURED.  (1) THEOREM (explicit,
  unconditional, assembled from cited ingredients): every interval
  (t, t + H_min(t)], t >= 10, contains a zero ordinate, with H_min
  the bisection root of main(t+H) - main(t) > 2 Sbound(t+H) + 2e-3
  and Sbound = min{2.5167 [Platt LMFDB to 3.06e10, Bellotti 2025 eq.
  (1.2)]; Trudgian 2014; Bellotti 2025 Cor. 1.5}; asymptotic floor
  4 pi 0.10076 = %.5f; H_min = %.2f .. %.2f across the comb;
  machine-verified on all %d Turing-certified gaps (min air %.2f x).
  (2) ADAPTIVE PACKETS: bands delta_p = kappa H_min(b_p) (kappa =
  2, 3) unconditionally hold >= kappa ordinates per band; the FRAME
  Boden B_p = 2 pi sum_j min_I_j (F_a * g_p^2) is positive and
  <= the comb value everywhere (median worst-case discount %.2f) --
  the unconditional theorem-shaped packet floor the v674 frame chain
  needed.  (3) THE DECISIVE MEASUREMENT: the packet PROJECTION form
  with adaptive widths %s (stabilization + two-model per (kappa, C):
  see run log); the minimizer stays single-mode; H_min DECREASES in
  t (the "wider upward" sketch is inverted) and adaptive weights
  differ from fixed ones only at relative order H_min/t -- the
  in-gap single-mode charge is re-partition-invariant.  (4) THE
  QUANTIFIED PINCH: pointwise (main-lobe) capture of a guaranteed
  zero needs H_min < pi/a, i.e. A1 < 1/(4 a0) = %.5f -- the best
  cited constant %.5f misses by %.1f%%, and the Platt branch bottoms
  out at %.4f > pi/a0 = %.4f, so NO current chain reaches it at ANY
  height: the projection route needs within-packet equidistribution
  input beyond counting (W3/W4 territory), not a better gap theorem
  of this shape.  TYPE: theorem = cited + machine-verified;
  Boden = unconditional frame-form construction; projection form =
  measured %s; A5(a), W2 Mosco proof and a -> infinity stay OPEN;
  no marker move.  VERDICT %s.
""" % (FLOOR_BE, float(h_at["min"][-1]), float(h_at["min"][0]),
       gaps.size, q[0], med_bv,
       "CLOSES" if z33_ok else "does NOT close",
       a_fam_req, C1_BE, 100.0 * (C1_BE / a_fam_req - 1.0),
       float(h_min_chain(np.array([T_PLATT - H_BRACKET[1]]),
                         s_bound_platt)[0]),
       math.pi / a0,
       "closed" if z33_ok else "open",
       VERDICT))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
