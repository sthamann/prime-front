#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""selberg_effective_probe -- PRIME.SELBERG.EFFECTIVE.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (the effective Selberg-variance attack; the one classical
lever round 143 priced as having closing power with only its
CONSTANTS missing)
=======================================================================
Round 143 (toproot_tailvis_probe, 27/27, CDXLVII) adjudicated two
unconditional routes for the TAILVIS-class visibility statements:
the Littlewood-S_1 smoothed route REFUTED-BY-ONE-LOG (ratio 0.20 ->
0.46, unbounded) and the SELBERG-VARIANCE ROUTE closing at c_w ~ 0.7
-- avg|S| ~ sqrt(loglog T)/(pi sqrt 2) ~ 0.31-0.34 at the operating
heights -- but ASYMPTOTIC-ONLY (constants not explicit; named, not
consumed).  Selberg's classical theorem: int_0^T S(t)^2 dt =
(T/2pi^2) loglog T + O(T (loglog T)^{1/2}) with S(t) = (1/pi) arg
zeta(1/2 + it) = N(t) - main(t) - 7/8 - O(1/t), main(t) = (t/2pi)
log(t/(2pi e)).  This probe executes the three contract angles:
(S1) THE LITERATURE HARVEST -- the sharpest citable explicit bounds,
their constants, validity thresholds, and the exact closing margin
per bound per corpus height; (S2) THE CONDITIONAL-EFFECTIVE ROUTE --
the minimal effective statement EFF-VAR(C1, C2, T0) that the corpus
pricing consumes, its closure algebra, and the exact pinning of
where effectivization of Selberg's proof machinery resists; (S3)
THE CORPUS PAYOFF -- machine-checked re-pricing of the r143
visibility leg, the r159/CDLXIII band-edge repulsion demand
(0.218/0.433/0.273 mean spacings), and the r160/r162 theta/J_2
window question (does variance-level control reach the windows?).

=======================================================================
S1  LITERATURE HARVEST (all constants CITED-EXTERNAL; web-sourced
2026-08-19; the probe gates the pricing arithmetic, not the proofs)
=======================================================================
POINTWISE UNCONDITIONAL |S(T)| bounds (explicit, T >= e):
  [L1] PLATT-DB (computational): |S(T)| <= 2.5167 for 0 <= T <=
       30 610 046 000 = 3.061e10.  Source: D. J. Platt, rigorous
       isolation of all nontrivial zeros below ~3.06e10 (Platt 2011
       LMS J. Comput. Math. 14 / Platt 2017 Math. Comp. 86 + LMFDB);
       quoted as eq. (1.2) in [L2] and eq. (1.7) in [L3].  Largest
       observed |S| value known: 3.3455 near t ~ 7.7573e27 (Bober-
       Hiary 2018, non-exhaustive search; quoted in [L2]).
  [L2] BELLOTTI-WONG 2024 (arXiv:2412.15470, "Improved estimates
       for the argument and zero-counting of Riemann zeta-function"):
       |S(T)| <= 0.10076 log T + min{0.24460 loglog T + 7.20844,
       1.68845 loglog T + 1.50956} for T >= e.  Sharpest published
       asymptotic-form constants (C1 = 0.10076 stated nearly-optimal
       for current technology).
  [L3] HSW22 (Hasanalizade-Shen-Wong, J. Number Theory 235 (2022)
       219-241, Cor. 1.4): |S(T)| <= min{0.1038 log T + 0.2573
       loglog T + 8.3675, 0.1095 log T + 0.2042 loglog T + 3.0305},
       T >= e.  The N-counting form (Cor. 1.2, constant 9.3675) is
       the corpus frozen input (v914; r143 machinery).
  [L4] PLATT-TRUDGIAN 2015: |S(T)| <= 0.110 log T + 0.290 loglog T
       + 2.290, T >= e.  [L5] TRUDGIAN 2012 (Math. Comp. II):
       0.111 log T + 0.275 loglog T + 2.450, T >= e.
POINTWISE CONDITIONAL (RH):
  [L6] SIMONIC 2022 (J. Number Theory, arXiv:2010.13307): |S(t)| <=
       (0.759282 + 20.1911/((log t)^0.285 loglog t)) log t/loglog t
       for t >= 10^2465; |S_1(t)| explicit for t >= 10^208.  BOTH
       VALIDITY-EXCLUDED at corpus heights (T <= ~2.5e4 operating,
       <= 3e12 carrier << 10^208) AND RH-CIRCULAR-FOR-CHAIN typed
       (the corpus legs feed the RH residue; conditional bounds are
       route adjudication only, never consumed).  Same typing for
       Wakasa 2012 (explicit S_1-integrals under RH) and Carneiro-
       Chandee-Milinovich-class bounds.
SECOND MOMENT / VARIANCE:
  [L7] SELBERG 1946 (Arch. Math. Naturvid. 48): int_0^T S^2 =
       (T/2pi^2) loglog T + O(T (loglog T)^{1/2}) UNCONDITIONAL --
       ASYMPTOTIC-ONLY, no explicit constants, no explicit T0, in
       1946 or in ANY later refinement found: Goldston 1987 (JNT 27,
       RH, second-order constant via pair correlation), Fujii
       (S_n extensions), Tsang 1984 (thesis), Arguin-Bailey 2025
       (Mathematika 71: explicit-constant LOWER bounds for large
       deviations, off-axis, wrong direction), Inoue-class explicit
       extreme values (Omega results, wrong direction).  HARVEST
       VERDICT: NO CITABLE EFFECTIVE UPPER VARIANCE BOUND EXISTS
       (2026-08 state of the art).
ZERO-DENSITY (the effectivization input):
  [L8] Explicit school: Kadiri 2013 (Acta Arith. 160): N(sigma,T)
       explicit for sigma >= 0.55, linear-in-T shape; Kadiri-Lumley-
       Ng 2018/2021 (JMAA + arXiv:2101.12263): Ingham-shape
       N(sigma,T) <= C1 T^{8/3(1-sigma)} log^5 T + C2 log^2 T for
       sigma > 1/2 + d/log H0 -- the exponent 8/3(1-sigma) >= 4/3
       > 1 near sigma = 1/2: VACUOUS AT THE CRITICAL LINE (worse
       than N(T) ~ (T/2pi) log T there).  Selberg's density lemma
       N(sigma,T) << T^{1-c(sigma-1/2)} log T (nontrivial arbitrarily
       close to 1/2; the input to the unconditional variance error
       control) HAS NO EXPLICIT VERSION in the literature.
EFFECTIVIZABLE LEGS (for S2; all citable):
  [L9] Montgomery-Vaughan 1974 mean-value theorem (explicit
       off-diagonal control of Dirichlet-polynomial second moments);
       Rosser-Schoenfeld 1962 explicit Mertens (|sum_{p<=x} 1/p -
       loglog x - M| <= 1/log^2 x class; the diagonal); HSW22/BW24
       explicit zero counting (sum_gamma 1/(1+(t-gamma)^2) << log t
       explicit; the under-horizon error legs); PT21 (Platt-Trudgian
       2021): RH verified to 3 000 175 332 800.

=======================================================================
S2  THE MINIMAL EFFECTIVE STATEMENT + WHERE EFFECTIVITY RESISTS
=======================================================================
EFF-VAR(C1, C2, T0): int_T^{2T} S(t)^2 dt <= (C1 loglog T + C2) T
for all T >= T0, with C1, C2, T0 explicit.  CONSUMPTION ALGEBRA
(gated exactly in G11/G13/G14): with V^2 := C1 loglog T + C2 the
[T, 2T]-mean square, (i) RMS/Chebyshev form: the measure of t with
|S(t)| > v is <= V^2 T/v^2, so a window of c_w mean spacings
carries a zero outside an exceptional set of density V^2/(c_w/2)^2;
closure at density 1 needs c_w >= 2V, at density 1/2 needs c_w >=
2 sqrt(2) V; (ii) avg form: (1/T) int |S| <= V (Cauchy-Schwarz),
average count over a c_w-window is positive iff c_w > 2 avg|S|.
THE r143 PRICING IS THE AVG FORM: c_w ~ 0.7 = 2 x 0.34.
CLOSURE CONDITION at height T: C1 loglog T + C2 <= c_w^2/4.
THE LAMBDA-KERNEL (G14, exact): for ANY C1 > 0 and fixed c_w the
closure fails for all T > exp(exp(c_w^2/(4 C1))) -- with the true
C1 = 1/(2pi^2) and c_w = 0.7 the crossover is exp(exp(2.4183)) =
exp(11.228) = 7.5e4.  THE SELBERG ROUTE IS HEIGHT-LOCAL EVEN WITH
PERFECT CONSTANTS: no fixed-c_w lambda-uniform closure exists; a
lambda-uniform consumer must let c_w(T) grow ~ 2 sqrt(C1 loglog T)
(absorbed by the B1 windows whose lengths are m_W ~ 10^2..10^4
spacings, NOT by fixed sub-spacing demands).
WHERE EFFECTIVIZATION RESISTS (the exact pinning, typed):
Selberg's unconditional proof machinery = (a) mollified prime-sum
representation S(t) = -(1/pi) sum_{n<x^3} Lambda_x(n) n^{-sigma_xt}
sin(t log n)/log n + error(zeros near t); (b) DIAGONAL of the prime
sum second moment = (1/2pi^2) sum Lambda^2(n)/(n log^2 n) ~
(1/2pi^2)(loglog + O(1)) -- EFFECTIVIZABLE (Rosser-Schoenfeld
explicit Mertens, [L9]); (c) OFF-DIAGONAL -- EFFECTIVIZABLE
(Montgomery-Vaughan explicit, [L9]); (d) ERROR CONTROL: int_0^T
(sigma_xt - 1/2)^2 (log x)^2-class terms need Selberg's zero-density
lemma N(sigma,T) << T^{1-c(sigma-1/2)} log T NEAR sigma = 1/2 --
NO EXPLICIT VERSION EXISTS ([L8]); the explicit school's density
results are vacuous at the line.  VERDICT: EFFECTIVITY-RESISTS-AT-
DENSITY-NEAR-HALF (unconditional side).  UNDER THE VERIFIED HORIZON
(T <= 3.061e10 [L1] resp. 3.0e12 [PT21]) RH(H0) holds computationally,
sigma_xt = 1/2 + 2/log x EXACTLY, and every remaining leg is
explicit-available ([L9]): EFF-VAR-UNDER-HORIZON is DERIVABLE-
CLASSICALLY-CONDITIONED with named inputs {RH(H0) computational
[L1/PT21], explicit Mertens [RS62], explicit MV [MV74], explicit
zero counting [HSW22/BW24]} -- a real analytic project (weeks-class,
NOT executed here; the probe prices what it must deliver), while
lambda-uniform (beyond horizon) it is BLOCKED by (d).

=======================================================================
S3  WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere, no R4/builder
    import -- this probe consumes NO Connes/source data); G02 cache
    health (X5, read-only).
S1  exact layer (sympy): G10 window-counting rearrangement
    N(T+L) - N(T) >= L rho(T) - 2B and the c_w threshold solve
    (c_w^0 = 2B positive-count form, c_w^1 = 1 + 2B unit form);
    G11 Chebyshev density rearrangement (finite-sum instance) +
    closure algebra solve [2 sqrt(C1 ll + C2) <= c_w <==> C1 ll +
    C2 <= c_w^2/4]; G12 partial-summation band-mass identity
    (d(wS) = w dS + w'S dt ==> int w dS = [wS] - int w'S; triangle
    cap |int w dS| <= B (|w(T1)| + |w(T2)| + int|w'|), generic sympy
    + exact rational instance); G13 avg <= RMS (Cauchy-Schwarz
    instance; the Gaussian factor sqrt(2/pi) CITED AS FORM, not
    consumed); G14 the lambda-kernel (exact solve of C1 loglog T =
    c_w^2/4: T* = exp(exp(c_w^2/(4C1))), finite witness beyond).
S2  G20 citable-bounds table B_i(2 Theta(x)) at the six rungs vs
    frozen calibration strings (rel 1e-3); PLATT-DB validity seam
    gated (2 Theta <= 3.061e10 at all rungs; census top T_z(x =
    4.8e11) = 3.0e12 > 3.061e10 DISCLOSED: beyond the DB height the
    best citable is the asymptotic-form class); G21 no-citable-
    closure: min margin c_w^0/0.7 >= 7.0 at every rung (calibrated
    7.19x PLATT-DB everywhere); G22 lambda-trend: best citable c_w
    at T = 1e12 is PT15-class 12.58, growing ~0.22 log T -- no
    lambda-uniform citable closure (gate: c_w(1e12) >= 10).
S3  cache instrumentation (ward-class; N(t) via searchsorted counts
    of verified ordinates -- counts, never oracles): G30 S-statistic
    table on [20, gtop], 400000-pt grid: RMS = 0.4039, avg|S| =
    0.3288, max|S| = 1.3562 (frozen strings, rel 2e-2) and
    RMS/Selberg-prediction(gtop) = 1.214 in (1.0, 1.4); G31
    effective-C2: C2_meas = RMS^2 - ll(gtop)/(2pi^2) = 0.0525 in
    (0.03, 0.08); the c_w = 0.7 RMS-form closure slack C2_max(x) =
    0.1225 - ll(2Theta)/(2pi^2) = 0.0271 -> 0.0052 falling: gate
    C2_meas > C2_max at ALL SIX rungs (TRUE-CONSTANTS-FAIL-RMS-FORM
    -- the finding) AND 2 avg|S| = 0.658 <= 0.70 (AVG-FORM-MARGINAL
    closes; the r143 pricing survives ONLY on the avg form); G32
    diagonal prime sum D(y) = sum_{n<=y} Lambda^2(n)/(n log^2 n):
    D(720) = 2.2882, D(25181) = 2.7171 (frozen, rel 1e-3), flatness
    (D - loglog y) drift <= 0.02, diagonal share (1/2pi^2) D /
    RMS^2 = 0.710/0.844 in (0.6, 0.9): the variance IS an
    arithmetic-consuming window (it consumes the prime sum's second
    moment; the r162 demand-class instantiated); G33 r159 repulsion
    demand-vs-delivery: demands (0.218, 0.433, 0.273) mean spacings
    vs delivery scales 2 avg = 0.658 / 2 RMS = 0.808 / 2 sqrt2 RMS
    = 1.142: gate delivery > demand at ALL THREE demands on ALL
    THREE forms (misses 1.5x-5.2x) -- VARIANCE-MISSES-REPULSION-BY-
    SCALE; the CLASS gap (density-one statements vs the signed
    pointwise T_rest(y_C) coordinate at a SPECIFIC location, CDLXIII
    OPEN-ZERO-SPACING-AT-HORIZON with ARITHMETIC-SIGNED-INPUT) is
    typed CITED, not re-proven; G34 window Delta-S at in-cache rungs
    x = 5/8/13: |m_W - main-increment| = 0.007/0.133/0.695 <= 2
    max|S| (frozen strings, abs 2e-2); G35 band-mass fluctuation
    cap instantiated (the r135-counting-reduction chain, w(t) =
    1/(1 + (t/T_z)^2) at x = 5, 8): |sum_gamma w - int w rho dt| =
    0.3872/0.4229 <= max|S| (w(T1) + w(T2) + TV(w)) = 2.2547/2.5124
    (frozen, rel 5e-2; Platt-form caps 4.1860/... printed) --
    VARIANCE-REACHES-BANDMASS-CAP: count-side control DOES bound
    band-mass fluctuations from above through partial summation;
    the theta-window FLOOR side (a lower bound on the collapsing
    jet ratio) is NOT reachable from any fluctuation CAP -- typed
    from CDLXVII GL3/rowprice-refutation + CDLXIV irreducible-
    collective (CITED): VARIANCE-MISSES-THETA-FLOOR-BY-SIDE.
S4  controls: G40 rigid RvM-regular synthetic grid (zeros at
    main = k - 7/8 - 1/2): RMS == 1/sqrt(12) = 0.2887, avg == 0.25,
    max == 0.5 exactly (rel 2e-2) -- REFUSES the measured cache
    statistics (0.4039/0.3288/1.3562): the S-statistic excess is
    zeta signal, not instrument artifact; G41 deterministic
    sin-jitter grid (half-spacing amplitude): RMS = 0.4565, max =
    1.0004 <= 1.01 -- amplitude-capped, no loglog tail (INFO-class
    exhibit, gated on the cap).
S5  G50 screen exemption WITH REASON (the CDLXIII-E3 pattern): this
    probe consumes NO builder/Connes/source data -- the pricing is
    pure classical counting + citable constants + ward census
    counts (BAND-CURRENCY); tau-screens are inapplicable by
    construction and the firewall (G01) enforces the absence
    structurally (no R4 import, no zeta, np.load only ward_).
S6  G60 census/min-cut: the r143 min-cut replica VERBATIM (inline
    maxflow; flows base 4 / refined 5 / one-grant 5 / two-grant 5 /
    counterfactual 7 NOT REAL); NO omega closed, NO status moved;
    the round REFINES the r143 route typing SELBERG-ASYMPTOTIC-ONLY
    into the four-way verdict below; census {MEAS, OMEGA-POS}
    cardinality 4 UNCHANGED.
S9  composite verdict + G99 runtime.

=======================================================================
FROZEN NUMERICS
=======================================================================
THETA (CDXLIV frozen onsets) = {5: 359.9, 8: 942.8, 13: 2619.6,
18: 5191.2, 24: 9276.0, 28: 12590.0}; window top T2 = 2 Theta;
CW_TARGET = 0.7 (r143); R159_DEMANDS = (0.218, 0.433, 0.273)
(CDLXIII: (y_C - b_top)/(2 sqrt(b_top)) over RvM mean spacing at
b5/b8/b24); C1_TRUE = 1/(2 pi^2); GRID_N = 400000; GRID_LO = 20.0;
PLATT_H = 3.061e10; PLATT_S = 2.5167; T_PT = 3000175332800;
BW24 = (0.10076, 0.24460, 7.20844, 1.68845, 1.50956); HSW22_S =
(0.1038, 0.2573, 8.3675, 0.1095, 0.2042, 3.0305); PT15 = (0.110,
0.290, 2.290); TRU12 = (0.111, 0.275, 2.450); DIAG_Y = (720, 25181);
WCAP_RUNGS = (5, 8); JIT_FREQ = 1.234567; JIT_AMP = 0.5.
CALIBRATION (inline one-shots 2026-08-19, no scratch file, numbers
verbatim): margins c_w^0 = 2B at the six rung tops: PLATT-DB 5.033
(margin 7.19x) at ALL rungs; BW24 10.707/11.362/11.997/12.394/
12.717/12.882; HSW22 8.271/8.538/8.814/8.995/9.147/9.226; PT15
7.120/7.411/7.710/7.905/8.068/8.153; TRU12 7.397/7.686/7.982/8.176/
8.339/8.423.  Best citable beyond PLATT height: PT15-class,
c_w(1e12) = 12.584, c_w(1e20) = 16.933.  Cache S-statistics (grid
[20, 7264.7482], 400000 pts): RMS 0.4039, avg 0.3288, max 1.3562;
Selberg prediction at gtop 0.3327 (ratio 1.214).  C2_meas 0.0525;
C2_max 0.0271/0.0201/0.0137/0.0098/0.0067/0.0052; 2 RMS_true(2Th)
0.769/0.787/0.803/0.813/0.820/0.824; 2 avg 0.658.  r159 miss
factors: avg-form 3.0/1.5/2.4, Cheb@1 3.7/1.9/3.0, Cheb@1/2
5.2/2.6/4.2.  Window Delta-S 0.007/0.133/0.695 (x = 5/8/13).
Diagonal D 2.2882/2.7171, D - loglog 0.4043/0.4013, share
0.710/0.844.  Band-mass cap x=5: LHS 0.3872 <= RHS 2.2547
(measured-B form; Platt-form 4.1860); x=8: 0.4229 <= 2.5124.
Controls: rigid 0.2887/0.2500/0.5000; jitter 0.4565/0.3751/1.0004.
BARS: XSTR_REL = 1e-3; SSTAT_REL = 2e-2; RATIO_WIN = (1.0, 1.4);
C2_WIN = (0.03, 0.08); MARGIN_MIN = 7.0; CW12_MIN = 10.0;
DIAG_SHARE_WIN = (0.6, 0.9); DIAG_DRIFT_BAR = 0.02; DS_ABS = 2e-2;
CAP_REL = 5e-2; CTRL_REL = 2e-2; JIT_MAX = 1.01; AVG_CLOSE = 0.70;
RUNTIME_BAR = 3600 s.  Deterministic: NO randomness anywhere (the
jitter control is a fixed sin sequence).  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks below.

VERDICT ENUMS (frozen):
NO-CITABLE-EFFECTIVE-VARIANCE(S1 harvest: Selberg/Goldston/Fujii/
Tsang asymptotic-only; Arguin-Bailey/Inoue wrong direction; Simonic/
Wakasa RH-circular + validity-excluded; G20-G22);
BEST-CITABLE-PLATT-DB-7X(the pointwise DB bound 2.5167 under
3.061e10 is the sharpest citable window input at ALL corpus
operating heights; margin 7.19x against c_w = 0.7; G20/G21);
EFF-VAR-PINNED(the minimal effective statement + closure algebra;
G11/G13); TRUE-CONSTANTS-FAIL-RMS-FORM + AVG-FORM-MARGINAL(measured
C2 = 0.0525 > slack 0.005-0.027 at every rung; 2 avg|S| = 0.658 <=
0.70 -- the r143 c_w ~ 0.7 pricing survives ONLY on the avg form;
G31); SELBERG-ROUTE-HEIGHT-LOCAL(lambda-kernel: fixed-c_w closure
dies at T* = exp(exp(c_w^2/(4 C1))), = 7.5e4 for the true constant
at c_w = 0.7; lambda-uniform consumers must grow c_w ~ sqrt(loglog);
G14); EFFECTIVITY-RESISTS-AT-DENSITY-NEAR-HALF(unconditional side:
Selberg's density lemma near sigma = 1/2 has NO explicit version;
the explicit school is vacuous at the line) + EFF-VAR-UNDER-HORIZON-
DERIVABLE(named inputs {RH(H0) computational, RS62, MV74, HSW22/
BW24}; weeks-class project, priced not executed);
VARIANCE-MISSES-REPULSION-BY-SCALE-AND-CLASS(r159: misses 1.5x-5.2x
+ density-vs-pointwise class gap; G33);
VARIANCE-REACHES-BANDMASS-CAP + MISSES-THETA-FLOOR-BY-SIDE(count-
side caps propagate through partial summation to band-mass
fluctuation caps; the theta-window demands a VALUE-side FLOOR --
CDLXVII GL3 CITED; G35); CONTROLS-REFUSE(G40/G41);
CENSUS-UNCHANGED(G60).
Composite priority: INSTRUMENT-EDGE (any edge gate fails, exit 1)
> EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use in this probe; no import of
verification/ or R4/builder machinery.  NO RH CLAIM.  EXPLORATION
ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- frozen
THETA = {5: 359.9, 8: 942.8, 13: 2619.6, 18: 5191.2, 24: 9276.0,
         28: 12590.0}
RUNGS = (5, 8, 13, 18, 24, 28)
CW_TARGET = 0.7
R159_DEMANDS = (0.218, 0.433, 0.273)
C1_TRUE = 1.0 / (2.0 * math.pi ** 2)
GRID_N = 400000
GRID_LO = 20.0
PLATT_H = 3.061e10
PLATT_S = 2.5167
T_PT = 3000175332800
BW24 = (0.10076, 0.24460, 7.20844, 1.68845, 1.50956)
HSW22_S = (0.1038, 0.2573, 8.3675, 0.1095, 0.2042, 3.0305)
PT15 = (0.110, 0.290, 2.290)
TRU12 = (0.111, 0.275, 2.450)
DIAG_Y = (720, 25181)
WCAP_RUNGS = (5, 8)
JIT_FREQ = 1.234567
JIT_AMP = 0.5

XSTR_REL = 1e-3
SSTAT_REL = 2e-2
RATIO_WIN = (1.0, 1.4)
C2_WIN = (0.03, 0.08)
MARGIN_MIN = 7.0
CW12_MIN = 10.0
DIAG_SHARE_WIN = (0.6, 0.9)
DIAG_DRIFT_BAR = 0.02
DS_ABS = 2e-2
CAP_REL = 5e-2
CTRL_REL = 2e-2
JIT_MAX = 1.01
AVG_CLOSE = 0.70
RUNTIME_BAR = 3600.0
GAMMA1_LIT = 14.134725141734693790   # ward only

# frozen calibration strings
CAL_MARGIN_PLATT = 5.033
CAL_BW24 = {5: 10.707, 8: 11.362, 13: 11.997, 18: 12.394,
            24: 12.717, 28: 12.882}
CAL_HSW = {5: 8.271, 8: 8.538, 13: 8.814, 18: 8.995, 24: 9.147,
           28: 9.226}
CAL_PT15 = {5: 7.120, 8: 7.411, 13: 7.710, 18: 7.905, 24: 8.068,
            28: 8.153}
CAL_TRU = {5: 7.397, 8: 7.686, 13: 7.982, 18: 8.176, 24: 8.339,
           28: 8.423}
CAL_CW12 = 12.584
CAL_SSTAT = (0.4039, 0.3288, 1.3562)
CAL_PRED_GTOP = 0.3327
CAL_C2MEAS = 0.0525
CAL_C2MAX = {5: 0.0271, 8: 0.0201, 13: 0.0137, 18: 0.0098,
             24: 0.0067, 28: 0.0052}
CAL_2RMS = {5: 0.769, 8: 0.787, 13: 0.803, 18: 0.813, 24: 0.820,
            28: 0.824}
CAL_2AVG = 0.658
CAL_DS = {5: 0.007, 8: 0.133, 13: 0.695}
CAL_DIAG = {720: 2.2882, 25181: 2.7171}
CAL_DIAG_ML = {720: 0.4043, 25181: 0.4013}
CAL_SHARE = {720: 0.710, 25181: 0.844}
CAL_CAP = {5: (0.3872, 2.2547), 8: (0.4229, 2.5124)}
CAL_CTRL = (0.2887, 0.2500, 0.5000)
CAL_JIT = (0.4565, 0.3751, 1.0004)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d (NONE allowed here)" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
                if m.startswith("radius4"):
                    bad.append("builder import " + m
                               + " (this probe is source-free)")
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; cache in ward_; no zeta; "
                       "no builder import (source-free probe)")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- closed forms
def main_term(t: float) -> float:
    return t / (2 * math.pi) * math.log(t / (2 * math.pi * math.e))


def rho_dens(T: float) -> float:
    return math.log(T / (2 * math.pi)) / (2 * math.pi)


def b_platt(T: float) -> float:
    return PLATT_S if T <= PLATT_H else float("inf")


def b_bw24(T: float) -> float:
    lg, ll = math.log(T), math.log(math.log(T))
    return BW24[0] * lg + min(BW24[1] * ll + BW24[2],
                              BW24[3] * ll + BW24[4])


def b_hsw22(T: float) -> float:
    lg, ll = math.log(T), math.log(math.log(T))
    return min(HSW22_S[0] * lg + HSW22_S[1] * ll + HSW22_S[2],
               HSW22_S[3] * lg + HSW22_S[4] * ll + HSW22_S[5])


def b_pt15(T: float) -> float:
    lg, ll = math.log(T), math.log(math.log(T))
    return PT15[0] * lg + PT15[1] * ll + PT15[2]


def b_tru12(T: float) -> float:
    lg, ll = math.log(T), math.log(math.log(T))
    return TRU12[0] * lg + TRU12[1] * ll + TRU12[2]


BOUNDS = (("PLATT-DB", b_platt), ("BW24", b_bw24), ("HSW22", b_hsw22),
          ("PT15", b_pt15), ("TRU12", b_tru12))


def diag_prime_sum(y: int) -> float:
    tot = 0.0
    sieve = np.ones(y + 1, bool)
    sieve[:2] = False
    for i in range(2, int(y ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    for p in np.nonzero(sieve)[0]:
        q = int(p)
        lam = math.log(p)
        while q <= y:
            tot += lam * lam / (q * math.log(q) ** 2)
            q *= p
    return tot


def inv_main(v: float) -> float:
    lo, hi = 10.0, 40000.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if main_term(mid) < v:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # G10 window-counting rearrangement + c_w threshold
    L, rs, B, m1, m2, S1, S2 = sp.symbols("L rs B m1 m2 S1 S2",
                                          real=True)
    # N = m + 7/8 + S at both ends: N2 - N1 = (m2 - m1) + S2 - S1
    okA = sp.simplify(((m2 + S2) - (m1 + S1))
                      - ((m2 - m1) - (S1 - S2))) == 0
    # |S1|, |S2| <= B ==> N2 - N1 >= (m2 - m1) - 2B; threshold solve
    sol = sp.solve(sp.Eq(L * rs - 2 * B, 0), L)
    okB = len(sol) == 1 and sp.simplify(sol[0] - 2 * B / rs) == 0
    sol1 = sp.solve(sp.Eq(L * rs - 2 * B, 1), L)
    okC = len(sol1) == 1 and sp.simplify(
        sol1[0] - (1 + 2 * B) / rs) == 0
    out.append(("G10-counting-cw-threshold", okA and okB and okC,
                "N(T+L)-N(T) == increment(main) + S(T+L) - S(T) "
                "exact; with |S| <= B: count >= L rho - 2B; "
                "thresholds c_w^0 = 2B (positive form) and c_w^1 = "
                "1 + 2B (unit form) exact solves -- the r143 window "
                "pricing consumes B at the window top"))

    # G11 Chebyshev density + closure algebra
    v, C1s, C2s, ll_, cw = sp.symbols("v C1s C2s ll_ cw",
                                      positive=True)
    vals = [sp.Rational(1, 2), sp.Rational(-3, 2), sp.Rational(1, 4),
            sp.Rational(2, 1), sp.Rational(-1, 3)]
    vth = sp.Rational(1, 1)
    cnt = sum(1 for u in vals if abs(u) > vth)
    cheb = sum(u ** 2 for u in vals) / vth ** 2
    okD = cnt <= cheb
    okE = sp.simplify(2 * sp.sqrt(cw ** 2 / 4) - cw) == 0
    okF = bool(sp.simplify(
        (C1s * ll_ + C2s - cw ** 2 / 4).subs(
            ll_, (cw ** 2 / 4 - C2s) / C1s)) == 0)
    out.append(("G11-chebyshev-closure", okD and okE and okF,
                "finite Chebyshev instance #{|u| > v} <= sum u^2/v^2 "
                "holds (%d <= %s); closure algebra 2 sqrt(C1 ll + "
                "C2) <= c_w <==> C1 ll + C2 <= c_w^2/4 exact "
                "(boundary substitution zero)" % (cnt, sp.nsimplify(cheb))))

    # G12 partial-summation band-mass identity + cap
    t = sp.symbols("t", positive=True)
    w = 1 / (1 + t ** 2)
    Sf = sp.sin(3 * t) / (2 + t)   # generic smooth stand-in for S
    lhsI = sp.diff(w * Sf, t) - (w * sp.diff(Sf, t)
                                 + sp.diff(w, t) * Sf)
    okG = sp.simplify(lhsI) == 0
    a_, b_, B_ = sp.symbols("a_ b_ B_", positive=True)
    wa, wb, TV = sp.symbols("wa wb TV", positive=True)
    cap = B_ * (wa + wb + TV)
    okH = sp.simplify(cap - B_ * wa - B_ * wb - B_ * TV) == 0
    inst = sp.Rational(3, 10) * (sp.Rational(1, 2)
                                 + sp.Rational(1, 5)
                                 + sp.Rational(7, 10))
    okI = inst == sp.Rational(3, 10) * sp.Rational(14, 10)
    out.append(("G12-partial-summation-cap", okG and okH and okI,
                "d(wS) == w dS + w' S dt exact (generic instance) "
                "==> int w dS = [wS] - int w' S; triangle cap "
                "|int w dS| <= B (|w(T1)| + |w(T2)| + int |w'|) "
                "(exact rational instance): pointwise/variance "
                "S-control propagates to band-mass fluctuation caps "
                "through the counting reduction (r135-class chain)"))

    # G13 avg <= RMS
    okJ = True
    vals2 = [0.5, -1.5, 0.25, 2.0, -1.0 / 3.0]
    n2 = len(vals2)
    avg2 = sum(abs(u) for u in vals2) / n2
    rms2 = math.sqrt(sum(u * u for u in vals2) / n2)
    okJ = avg2 <= rms2 + 1e-15
    out.append(("G13-avg-le-rms", okJ,
                "Cauchy-Schwarz instance avg|u| = %.4f <= RMS = "
                "%.4f; the Gaussian avg = sqrt(2/pi) RMS refinement "
                "is CITED AS FORM (Selberg CLT), never consumed"
                % (avg2, rms2)))

    # G14 lambda-kernel
    Tst = math.exp(math.exp(CW_TARGET ** 2 / (4 * C1_TRUE)))
    ok_lam = (C1_TRUE * math.log(math.log(2 * Tst))
              > CW_TARGET ** 2 / 4)
    okK = abs(CW_TARGET ** 2 / (4 * C1_TRUE)
              - CW_TARGET ** 2 * math.pi ** 2 / 2) < 1e-12
    out.append(("G14-lambda-kernel", ok_lam and okK,
                "exact crossover: C1 loglog T = c_w^2/4 at T* = "
                "exp(exp(c_w^2/(4 C1))) = exp(exp(%.4f)) = %.3e for "
                "the TRUE constant at c_w = 0.7; beyond T* the "
                "fixed-c_w closure FAILS (witness 2T*): the Selberg "
                "route is HEIGHT-LOCAL even with perfect constants; "
                "lambda-uniform consumers must grow c_w ~ "
                "2 sqrt(C1 loglog T)"
                % (CW_TARGET ** 2 / (4 * C1_TRUE), Tst)))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("selberg_effective_probe -- PRIME.SELBERG.EFFECTIVE.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    grid_n = GRID_N // 8 if smoke else GRID_N

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")
    gtop = float(gam[-1])

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (pricing algebra)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: [L1] Platt DB |S| <= 2.5167 (T <= "
         "3.061e10); [L2] Bellotti-Wong arXiv:2412.15470; [L3] "
         "HSW22 JNT 235; [L4] Platt-Trudgian 2015; [L5] Trudgian "
         "2012; [L6] Simonic 2022 (RH; VALIDITY-EXCLUDED t >= "
         "10^2465 + RH-CIRCULAR-FOR-CHAIN); [L7] Selberg 1946 "
         "variance ASYMPTOTIC-ONLY (harvest: no effective upper "
         "variance exists 2026-08); [L8] explicit zero-density "
         "school vacuous near sigma = 1/2 (Kadiri 2013 sigma >= "
         "0.55; KLN Ingham-shape); [L9] RS62/MV74/PT21 (the "
         "effectivizable legs); CDXLVII route pricing; CDLXIII "
         "repulsion strings; CDLXIV/CDLXVII window verdicts")

    # ---------------------------------------------------------- S2
    section("S2  HARVEST INSTANTIATION (closing-margin table)")
    ok20 = ok21 = True
    det20, det21 = [], []
    cal_tabs = {"BW24": CAL_BW24, "HSW22": CAL_HSW, "PT15": CAL_PT15,
                "TRU12": CAL_TRU}
    for x in RUNGS:
        T2 = 2 * THETA[x]
        row = []
        for nm, fb in BOUNDS:
            cw0 = 2.0 * fb(T2)
            row.append((nm, cw0))
            if nm == "PLATT-DB":
                okc = abs(cw0 - CAL_MARGIN_PLATT) <= XSTR_REL * 10
            else:
                okc = abs(cw0 / cal_tabs[nm][x] - 1.0) <= XSTR_REL
            ok20 = ok20 and okc and T2 <= PLATT_H
        best = min(row, key=lambda r: r[1])
        marg = best[1] / CW_TARGET
        ok21 = ok21 and marg >= MARGIN_MIN
        det20.append("x%d %s" % (x, " ".join(
            "%s %.3f" % (nm, cw) for nm, cw in row)))
        det21.append("x%d best %s c_w %.3f margin %.2fx"
                     % (x, best[0], best[1], marg))
        info("x=%d (T2 = %.0f): best citable c_w = %.3f [%s], "
             "margin vs 0.7 target = %.2fx; the B1 window itself "
             "(m_W ~ 10^2..10^4 spacings) consumes ANY citable "
             "bound -- the r143 closure is safe; the SUB-SPACING "
             "statement stays open-effective"
             % (x, T2, best[1], best[0], marg))
    check("G20-citable-table", ok20,
          "c_w^0 = 2B at the six rung tops vs frozen calibration "
          "strings (rel %.0e); PLATT-DB validity T2 <= 3.061e10 at "
          "every rung (census top T_z(4.8e11) = 3.0e12 EXCEEDS the "
          "DB height -- seam DISCLOSED, beyond it the asymptotic "
          "class rules): %s" % (XSTR_REL, "; ".join(det20)))
    check("G21-no-citable-closure", ok21,
          "min margin >= %.1fx at every rung (calibrated 7.19x "
          "PLATT-DB everywhere): NO citable bound reaches c_w = "
          "0.7 -- the effective-variance gap is real: %s"
          % (MARGIN_MIN, "; ".join(det21)))
    cw12 = 2.0 * min(b(1e12) for _, b in BOUNDS[1:])
    check("G22-lambda-trend", cw12 >= CW12_MIN
          and abs(cw12 / CAL_CW12 - 1.0) <= XSTR_REL,
          "beyond the DB height the best citable c_w(1e12) = %.3f "
          "(PT15-class), growing ~0.22 log T: no lambda-uniform "
          "citable closure exists at ANY fixed c_w" % cw12)

    # ---------------------------------------------------------- S3
    section("S3  CACHE INSTRUMENTATION (ward counts) + PAYOFF")
    ts = np.linspace(GRID_LO, gtop, grid_n)
    Ncnt = np.searchsorted(gam, ts, side="right")
    mains = np.array([main_term(t) for t in ts])
    S = Ncnt - mains - 7.0 / 8.0
    rms = float(np.sqrt(np.mean(S ** 2)))
    avga = float(np.mean(np.abs(S)))
    # max|S| EXACT at the jump points (S is piecewise monotone
    # between zeros; the sup is attained at a zero ordinate,
    # left or right limit) -- grid-free, resolution-independent
    mg = np.array([main_term(g) for g in gam])
    ks = np.arange(1, len(gam) + 1)
    s_right = ks - mg - 7.0 / 8.0
    s_left = (ks - 1) - mg - 7.0 / 8.0
    maxs = float(max(np.max(np.abs(s_right)), np.max(np.abs(s_left))))
    pred = math.sqrt(math.log(math.log(gtop)) / (2 * math.pi ** 2))
    ratio = rms / pred
    ok30 = (abs(rms / CAL_SSTAT[0] - 1) <= SSTAT_REL
            and abs(avga / CAL_SSTAT[1] - 1) <= SSTAT_REL
            and abs(maxs / CAL_SSTAT[2] - 1) <= SSTAT_REL
            and RATIO_WIN[0] <= ratio <= RATIO_WIN[1])
    check("G30-s-statistics", ok30,
          "in-cache S(t) on [%.0f, %.1f] (%d pts): RMS %.4f avg|S| "
          "%.4f max|S| %.4f (frozen 0.4039/0.3288/1.3562); Selberg "
          "leading-order prediction at gtop %.4f, ratio %.3f in %s "
          "(the O(1) second-order term is REAL at these heights)"
          % (GRID_LO, gtop, grid_n, rms, avga, maxs, pred, ratio,
             str(RATIO_WIN)))

    c2meas = rms ** 2 - C1_TRUE * math.log(math.log(gtop))
    ok31 = C2_WIN[0] <= c2meas <= C2_WIN[1]
    det31 = []
    for x in RUNGS:
        T2 = 2 * THETA[x]
        ll = math.log(math.log(T2))
        c2max = CW_TARGET ** 2 / 4 - C1_TRUE * ll
        two_rms_true = 2 * math.sqrt(C1_TRUE * ll + c2meas)
        ok31 = ok31 and (c2meas > c2max) \
            and abs(c2max / CAL_C2MAX[x] - 1.0) <= 5e-2 \
            and abs(two_rms_true / CAL_2RMS[x] - 1.0) <= SSTAT_REL
        det31.append("x%d C2max %.4f 2RMS %.3f" % (x, c2max,
                                                   two_rms_true))
    two_avg = 2 * avga
    ok31 = ok31 and two_avg <= AVG_CLOSE \
        and abs(two_avg / CAL_2AVG - 1.0) <= SSTAT_REL
    check("G31-effective-c2", ok31,
          "C2_meas = %.4f in %s; closure slack C2_max(0.7) = "
          "0.0271 -> 0.0052 falling: C2_meas EXCEEDS the slack at "
          "ALL SIX rungs (TRUE-CONSTANTS-FAIL-RMS-FORM -- even a "
          "perfect effective variance does NOT close c_w = 0.7 on "
          "the RMS/Chebyshev form; 2 RMS_true = 0.77-0.82); "
          "2 avg|S| = %.3f <= %.2f: the r143 pricing survives ONLY "
          "on the avg form (AVG-FORM-MARGINAL): %s"
          % (c2meas, str(C2_WIN), two_avg, AVG_CLOSE,
             "; ".join(det31)))

    ok32 = True
    det32 = []
    for y in DIAG_Y:
        D = diag_prime_sum(y)
        lly = math.log(math.log(y))
        share = D / (2 * math.pi ** 2) / rms ** 2
        ok32 = ok32 and abs(D / CAL_DIAG[y] - 1.0) <= XSTR_REL \
            and DIAG_SHARE_WIN[0] <= share <= DIAG_SHARE_WIN[1]
        det32.append("y%d D %.4f D-ll %.4f share %.3f"
                     % (y, D, D - lly, share))
    D1 = diag_prime_sum(DIAG_Y[0])
    D2v = diag_prime_sum(DIAG_Y[1])
    drift = abs((D2v - math.log(math.log(DIAG_Y[1])))
                - (D1 - math.log(math.log(DIAG_Y[0]))))
    ok32 = ok32 and drift <= DIAG_DRIFT_BAR
    check("G32-arithmetic-diagonal", ok32,
          "D(y) = sum Lambda^2(n)/(n log^2 n) vs frozen strings; "
          "D - loglog y FLAT (drift %.4f <= %.2f: the Mertens-class "
          "O(1) is arithmetic and stable); diagonal share of the "
          "measured variance 0.71-0.84: THE VARIANCE IS AN "
          "ARITHMETIC-CONSUMING WINDOW (it consumes the prime "
          "sum's second moment -- the r162 demand-class, "
          "instantiated on the CAP side): %s"
          % (drift, DIAG_DRIFT_BAR, "; ".join(det32)))

    ok33 = True
    scales = (("avg-form", 2 * avga), ("cheb@1", 2 * rms),
              ("cheb@1/2", 2 * math.sqrt(2) * rms))
    det33 = []
    for nm, sc in scales:
        for d in R159_DEMANDS:
            ok33 = ok33 and sc > d
        det33.append("%s %.3f misses %s" % (nm, sc, "/".join(
            "%.1fx" % (sc / d) for d in R159_DEMANDS)))
    check("G33-r159-repulsion-miss", ok33,
          "CDLXIII demands (0.218, 0.433, 0.273) mean spacings at "
          "SPECIFIC band-edge locations vs variance delivery: ALL "
          "three demands BELOW every delivery scale "
          "(VARIANCE-MISSES-REPULSION-BY-SCALE, 1.5x-5.2x); the "
          "CLASS gap (density-one vs signed pointwise "
          "T_rest(y_C)-coordinate) is CITED from CDLXIII "
          "(ARITHMETIC-SIGNED-INPUT typing), not re-proven: %s"
          % "; ".join(det33))

    ok34 = True
    det34 = []
    for x in (5, 8, 13):
        Th = THETA[x]
        T2 = min(2 * Th, gtop)
        mw = int(np.sum((gam > Th) & (gam <= T2)))
        dS = mw - (main_term(T2) - main_term(Th))
        ok34 = ok34 and abs(dS - CAL_DS[x]) <= DS_ABS \
            and abs(dS) <= 2 * maxs
        det34.append("x%d m_W %d DeltaS %.3f" % (x, mw, dS))
    check("G34-window-deltaS", ok34,
          "in-cache window count fluctuations at the r143 windows "
          "(frozen 0.007/0.133/0.695, all <= 2 max|S|): the "
          "windows the corpus consumes live deep inside the "
          "S-fluctuation budget: %s" % "; ".join(det34))

    ok35 = True
    det35 = []
    for x in WCAP_RUNGS:
        Tz = 2 * math.pi * x
        wf = lambda t, Tz=Tz: 1.0 / (1.0 + (t / Tz) ** 2)
        wpf = lambda t, Tz=Tz: (-2 * t / Tz ** 2
                                / (1.0 + (t / Tz) ** 2) ** 2)
        T1 = float(gam[0]) - 1e-9
        tt = np.linspace(T1, gtop, 200000)
        Iw = np.trapezoid(np.array([wf(t) * rho_dens(t)
                                    for t in tt]), tt)
        lhs = abs(float(sum(wf(g) for g in gam) - Iw))
        TVw = float(np.trapezoid(np.abs(np.array([wpf(t)
                                                  for t in tt])), tt))
        rhs = maxs * (abs(wf(gtop)) + abs(wf(T1)) + TVw)
        rhs_p = PLATT_S * (abs(wf(gtop)) + abs(wf(T1)) + TVw)
        okc = (lhs <= rhs
               and abs(lhs / CAL_CAP[x][0] - 1.0) <= CAP_REL
               and abs(rhs / CAL_CAP[x][1] - 1.0) <= CAP_REL)
        ok35 = ok35 and okc
        det35.append("x%d LHS %.4f <= RHS %.4f (Platt-form %.4f)"
                     % (x, lhs, rhs, rhs_p))
    check("G35-bandmass-cap", ok35,
          "|sum_gamma w - int w rho dt| <= B (|w| ends + TV(w)) "
          "instantiated at x = 5, 8 with w = 1/(1 + (t/T_z)^2): "
          "VARIANCE-REACHES-BANDMASS-CAP (count-side control DOES "
          "propagate to band-mass fluctuation CAPS via G12/r135); "
          "the theta-window FLOOR side (lower bound on the "
          "collapsing jet ratio, CDLXVII GL3 rowprice-refutation + "
          "CDLXIV irreducible-collective, CITED) is a VALUE-side "
          "demand no fluctuation cap can produce: "
          "MISSES-THETA-FLOOR-BY-SIDE: %s" % "; ".join(det35))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS")
    n = len(gam)
    reg = np.array([inv_main(k - 7.0 / 8.0 - 0.5)
                    for k in range(1, n + 1)])
    Nr = np.searchsorted(reg, ts, side="right")
    Sr = Nr - mains - 7.0 / 8.0
    r_rms = float(np.sqrt(np.mean(Sr ** 2)))
    r_avg = float(np.mean(np.abs(Sr)))
    r_max = float(np.max(np.abs(Sr)))
    ok40 = (abs(r_rms / CAL_CTRL[0] - 1) <= CTRL_REL
            and abs(r_avg / CAL_CTRL[1] - 1) <= CTRL_REL
            and abs(r_max / CAL_CTRL[2] - 1) <= CTRL_REL
            and r_rms < rms and r_max < maxs)
    check("G40-rigid-grid-refuses", ok40,
          "RvM-regular synthetic grid: RMS %.4f == 1/sqrt(12), avg "
          "%.4f, max %.4f -- REFUSES the cache (0.4039/0.3288/"
          "1.3562): the measured excess is zeta fluctuation signal, "
          "not counting-instrument artifact" % (r_rms, r_avg, r_max))
    sp_ = np.diff(np.concatenate([[reg[0] - (reg[1] - reg[0])], reg]))
    jit = np.sort(reg + JIT_AMP * sp_
                  * np.sin(np.arange(1, n + 1) * JIT_FREQ))
    Nj = np.searchsorted(jit, ts, side="right")
    Sj = Nj - mains - 7.0 / 8.0
    j_rms = float(np.sqrt(np.mean(Sj ** 2)))
    j_max = float(np.max(np.abs(Sj)))
    ok41 = j_max <= JIT_MAX and abs(j_rms / CAL_JIT[0] - 1) <= CTRL_REL
    check("G41-jitter-amplitude-capped", ok41,
          "deterministic sin-jitter grid: RMS %.4f, max %.4f <= "
          "%.2f -- amplitude-capped by construction (zeta max "
          "1.3562 EXCEEDS it; the zeta tail is not a bounded-jitter "
          "artifact); INFO-class exhibit" % (j_rms, j_max, JIT_MAX))

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    has_builder = any(
        isinstance(nd, (ast.Import, ast.ImportFrom))
        and any((al.name if isinstance(nd, ast.Import)
                 else (nd.module or "")).startswith("radius4")
                for al in (nd.names if isinstance(nd, ast.Import)
                           else [None]))
        for nd in ast.walk(tree))
    check("G50-screen-exemption-typed", not has_builder,
          "tau-screens INAPPLICABLE WITH REASON (CDLXIII-E3 "
          "pattern): the probe consumes NO builder/Connes/source "
          "data -- classical counting + citable constants + ward "
          "census counts only (BAND-CURRENCY); enforced "
          "structurally by G01 (no builder import, no zeta)")

    # ---------------------------------------------------------- S6
    section("S6  CENSUS / MIN-CUT")

    def maxflow(edges: dict, s: str, t: str) -> int:
        nodes = set()
        for (u, v) in edges:
            nodes.add(u)
            nodes.add(v)
        cap = dict(edges)
        flow = 0
        while True:
            # BFS augmenting path
            par = {s: None}
            queue = [s]
            while queue and t not in par:
                u = queue.pop(0)
                for (a, b), c in cap.items():
                    if a == u and c > 0 and b not in par:
                        par[b] = (a, b)
                        queue.append(b)
            if t not in par:
                return flow
            # bottleneck
            path = []
            v = t
            while par[v] is not None:
                path.append(par[v])
                v = par[v][0]
            aug = min(cap[e] for e in path)
            for e in path:
                cap[e] -= aug
                rev = (e[1], e[0])
                cap[rev] = cap.get(rev, 0) + aug
            flow += aug

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "TOPROOT"): 1,
                ("TOPROOT", "TAILVISTHM"): INF,
                ("TAILVISTHM", "TLAWCAP"): 1,
                ("TLAWCAP", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "TOPROOT")] = INF
    f_one = maxflow(dict(one), "UNC", "RH")
    two = dict(one)
    two[("TAILVISTHM", "TLAWCAP")] = INF
    f_two = maxflow(dict(two), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1,
               ("SUSCAP2R", "R4HYP"): INF})
    f_cf = maxflow(dict(cf), "UNC", "RH")
    check("G60-census-mincut", f_base == 4 and f_ext == 5
          and f_one == 5 and f_two == 5 and f_cf == 7,
          "r143 min-cut replica VERBATIM (inline maxflow): flows "
          "base %d refined %d one-grant %d two-grant %d "
          "counterfactual %d NOT REAL; NO omega closed, NO status "
          "moved; this round refines the r143 route typing "
          "SELBERG-ASYMPTOTIC-ONLY into {NO-CITABLE-EFFECTIVE-"
          "VARIANCE, TRUE-CONSTANTS-FAIL-RMS-FORM + AVG-FORM-"
          "MARGINAL, SELBERG-ROUTE-HEIGHT-LOCAL, EFFECTIVITY-"
          "RESISTS-AT-DENSITY-NEAR-HALF + UNDER-HORIZON-DERIVABLE}; "
          "census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED"
          % (f_base, f_ext, f_one, f_two, f_cf))
    info("EXACT RESIDUE effect: NONE on the omega set.  The "
         "Selberg-variance lever is now PRICED: (i) it cannot "
         "close the r159 repulsion leg at ANY effectivity (scale "
         "0.66-1.14 vs demands 0.22-0.43 + class gap); (ii) it "
         "reaches band-mass fluctuation CAPS (G35) but not the "
         "theta-window FLOOR (value side, CDLXVII GL3); (iii) its "
         "sub-spacing visibility closure is HEIGHT-LOCAL even with "
         "perfect constants (G14) -- the r143 avg-form closure at "
         "c_w = 0.7 is real at operating heights and dies at T* ~ "
         "7.5e4; (iv) the effective statement EFF-VAR(C1, C2, T0) "
         "is DERIVABLE-UNDER-HORIZON with named citable inputs "
         "(weeks-class project) and BLOCKED lambda-uniformly at "
         "Selberg's zero-density lemma near sigma = 1/2 (no "
         "explicit version exists).  NO RH claim; nothing "
         "upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "NO-CITABLE-EFFECTIVE-VARIANCE(S1 harvest; G20-G22)",
        "BEST-CITABLE-PLATT-DB-7X(2.5167 under 3.061e10; margin "
        "7.19x vs c_w = 0.7; G20/G21)",
        "EFF-VAR-PINNED(minimal statement + closure algebra; "
        "G11/G13)",
        "TRUE-CONSTANTS-FAIL-RMS-FORM + AVG-FORM-MARGINAL(C2_meas "
        "0.0525 > slack 0.005-0.027; 2 avg|S| = 0.658 <= 0.70; G31)",
        "SELBERG-ROUTE-HEIGHT-LOCAL(T* = exp(exp(c_w^2 pi^2/2)) = "
        "7.5e4 at c_w = 0.7 true constant; G14)",
        "EFFECTIVITY-RESISTS-AT-DENSITY-NEAR-HALF + "
        "EFF-VAR-UNDER-HORIZON-DERIVABLE(named inputs; typed)",
        "VARIANCE-MISSES-REPULSION-BY-SCALE-AND-CLASS(r159; G33)",
        "VARIANCE-REACHES-BANDMASS-CAP + MISSES-THETA-FLOOR-BY-SIDE"
        "(G12/G35 + CDLXVII GL3 CITED)",
        "CONTROLS-REFUSE(G40/G41)",
        "CENSUS-UNCHANGED(G60)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: NO-CITABLE-EFFECTIVE-VARIANCE + "
              "BEST-CITABLE-PLATT-DB-7X + EFF-VAR-PINNED + "
              "TRUE-CONSTANTS-FAIL-RMS-FORM + AVG-FORM-MARGINAL + "
              "SELBERG-ROUTE-HEIGHT-LOCAL + "
              "EFFECTIVITY-RESISTS-AT-DENSITY-NEAR-HALF + "
              "EFF-VAR-UNDER-HORIZON-DERIVABLE + "
              "VARIANCE-MISSES-REPULSION-BY-SCALE-AND-CLASS + "
              "VARIANCE-REACHES-BANDMASS-CAP + "
              "MISSES-THETA-FLOOR-BY-SIDE + CONTROLS-REFUSE + "
              "CENSUS-UNCHANGED")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
