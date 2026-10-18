#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""centered_basefiber_probe -- PRIME.PORT.RHP.CENTERED_BASEFIBER.01
(round 250): the OPENING MEASUREMENT of the nonperturbative campaign.
Build the best available GLOBAL OUTER-MODEL candidate for the discrete
2x2 FIK matrix Y_n from exact comb data (constrained-equilibrium
g-function + discrete Szego correction, r232a machinery), and MEASURE
the error R(z) = Y_n(z) M_n(z)^{-1} on sealed z-panels: the ERROR MAP
(panels x windows x worlds x N-trend) is the round's core deliverable
and localizes the follow-up rounds' local problems (R2-R4).  The
opening measurement is allowed to come out BAD; it must come out
PRECISE.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r249 discipline): w = window (kz),
N_w = builder depth, n = chain degree (snapshot mass), S = #union
nodes; free pivots h_{w,n} (n < N_w) are the proof objects; Y_n is
the frozen r227/r234 FIK normalization Y_n = [[pihat_n, C_n],
[pihat_{n-1}/h_{n-1}, C_{n-1}/h_{n-1}]], C_n(z) = sum w~ pihat_n(x)
/(z - x) over BOTH zones; pihat_N consumes free-prefix recursion
data only; the forced pivot h_N is NEVER formed (the recursion stops
before eta_N); ground truth (h signs, flips) enters gates only.  No
zero/prime oracles anywhere (AST firewall).

LEG 0 -- CONTRACT FROZEN (before any evaluation):
TARGET OBJECTS: BASE = the bulk gammahat band (r247: gammahat_n in
[0.166, 0.343] on [8, N-20], plateau 1/4, worst |eps| 0.093,
shrinking with N); FIBER = the ONE terminal CD readout T =
intint [K_N - K_8] dsigma0 dsigma0 (r248, centering-invariant,
mp-exact 3.3e-160), sigma0 = sigma - (F_0/h_0) mutilde.
THREE-ZONE TYPING (corrected, r248 + r249): GEOMETRIC_RANK1_HEAD
(world-blind, eliminable by the centering congruence) +
LOWMODE_SUPPORT_SILENCE (r249 correction of the r248 label
LOWMODE_ARITHMETIC_SILENCE: the low-mode stillness is SUPPORT
GEOMETRY plus a PAIRING statement -- r249 typed the deep carrier as
prime-free) + EXTENSIVE_PAIRING_SENSITIVE_TAIL (the SCRAMBLE budget
excess sits in n >= 8, fraction 0.836).
B PROVENANCE (r247 discipline, binding): every budget is parametric
tau^aug(B); honest status IMPORTED -- the only covering budget
remains B_w = S_{N-2} + 5/7 (prefix data + r241 floor); nothing is
upgraded here.
FALSIFIER BATTERY (sealed): SMOOTH breaks in the BASE at 27 and
EPSTEIN in the BASE at 25 (band exit via gammahat < 0, r247);
SCRAMBLE is the FIBER falsifier (low-mode support break + tail
budget excess); control flips 25/21/27 re-gated hard; no control is
ever certified; a world-blind error map is ADMISSIBLE for an outer
model but must be typed (MODEL_WORLD_BLIND).

LEG A -- THE GLOBAL OUTER-MODEL CANDIDATE (all choices sealed here,
derived at design time from the FIK normalization):
(a1) DISCRETE g-FUNCTION: solve the r232a constrained equilibrium
  (capped simplex 0 <= rho_j <= 1, sum rho_j = n) on the union nodes
  with the exact weight field V_j = -log|wtilde_j| (FISTA projected
  gradient, machinery imported from szego_equilibrium_probe: solver,
  projection, union setup VERBATIM).  The zero-counting potential is
  G_n(z) = sum_j rho_j log(z - x_j) (principal branch, z off the
  real support), so e^{G_n(z)} = prod (z - x_j)^{rho_j} is monic of
  z-degree n.  The Robin/Lagrange datum is read from the KKT
  multiplier of the QP: with F_j = 2 (A rho)_j + V_j, the multiplier
  window is [max_{sel} F, min_{unsel} F]; SEALED: lambda_n = the
  midpoint, n*ell_n := -lambda_n (the KKT gap width is reported; a
  negative gap is typed, never hidden).  Plausibility anchor: for a
  width-2 hull, lambda ~ 2 n log 2, e^{n ell} ~ 4^{-n} = the r247
  capacity plateau in h-currency.
(a2) DISCRETE SZEGO CORRECTION (the sealed finite form): support
  hull [a_n, b_n] = extreme nodes of the equilibrium support
  (rho_j > 1e-9); arcsine CELL masses nuhat_i on [a_n, b_n] (cells =
  midpoint cells of the sorted support nodes, end cells close at the
  hull -- an exact unit-mass partition, no endpoint singularity);
  weight-DENSITY field L_j = log(|wtilde_j| / Delta_j) with Delta_j
  the union-node cell width (the discrete Cauchy column sees the
  atom DENSITY, not the atom mass -- disclosed design choice);
  D_n(z) = exp( (R(z)/2) sum_i nuhat_i L_i / (z - s_i) ),
  R(z) = (z - a) ((z-b)/(z-a))^{1/2} (branch R ~ z at infinity on
  BOTH real sides), Dinf = exp( (1/2) sum nuhat_i L_i ).
(a3) THE MODEL (standard one-cut outer form in the repo FIK
  normalization, with the discrete-residue calibration DERIVED at
  design time): beta(z) = ((z-b)/(z-a))^{1/4}, N(z) = [[(beta +
  1/beta)/2, (beta - 1/beta)/(2i)], [-(beta - 1/beta)/(2i), (beta +
  1/beta)/2]] (det = 1, the standard band-jump matrix), and
    Mhat_n(z) = e^{(n ell/2) sigma3} Dinf^{sigma3} N(z)
                D_n(z)^{-sigma3} e^{(G_n(z) - n ell/2) sigma3},
    M_n(z)   = K Mhat_n(z) K^{-1},   K = diag(-2 pi i, 1).
  The constant conjugation K is the calibration between the discrete
  residue column C_n = sum w~ pihat/(z - x) and the continuous-line
  (1/2 pi i) integral of the classical parametrix; it preserves
  det = 1 and the normalization M_n z^{-n sigma3} -> I and makes the
  1/z readout REAL POSITIVE:
    h_n^model = (M1)_12 = 2 pi e^{n ell} Dinf^2 (b - a)/4,
    gammahat_n^model = (M1)_12 (M1)_21 = ((b_n - a_n)/4)^2
  (the r247 capacity reading, K-invariant).  Chebyshev-U anchor
  (design-time check of the 2 pi): w = sqrt(1-x^2) on [-1, 1] has
  h_n = (pi/2) 4^{-n} and the formula gives 2 pi * (1/2) * (1/2) *
  4^{-n} = (pi/2) 4^{-n} EXACTLY.
WARDS (leg-A gates): det M = 1 at every panel point (mp); FIK
normalization M z^{-n sigma3} -> I with Richardson extraction of M1
at z = x0 + 1e3 / x0 + 1e4 vs the analytic h/gammahat formulas; QP
fixed-point residual, integer mass, 0/1 saturation; a DISCRETE TOY
(64 Chebyshev nodes, discrete U-weight (1 - x^2) pi/64) where the
true chain is exactly computable: the model h-rate must track the
toy h-decades (sealed slope bar) and (M1)_12 must be real-positive.
MODEL PROVENANCE DISCLOSED: the QP masses are f64, lifted verbatim
into mp; the model consumes node positions + |weights| + the QP
minimizer ONLY -- no target sign, no flip degree, no h-chain of the
window being tested enters any model path.

LEG B -- THE ERROR MAP (core deliverable): the raw R(z) = Y_n(z)
M_n(z)^{-1} is GAUGE-SENSITIVE (both Y and any admissible outer
model carry the constant conjugation e^{(n ell/2) sigma3}; the
off-diagonals of R - I scale as e^{-+ n ell} -- Deift's remainder
lives in the NORMALIZED gauge).  SEALED METRIC: err =
||C^{-1} (Y_n M_n^{-1}) C - I||_F with C = e^{(n ell_n/2) sigma3}
(the model's own ell -- the error of the normalized problem;
diagonal entries untouched).  Panels, built world-blind from the
union nodes: OUT = {b0+0.5, a0-0.5, b0+1.0} (real, outside the
hull); FAR = {x0+1.5i, x0-1+1i, x0+1+1i}; NEAR = {x0+0.05i,
gm1+0.05i} (gm1 = midpoint of the largest node gap); GAP = midpoints
of the 3 largest node gaps + 0.02i (the outer model has its band cut
there -- the panel measures the band error honestly off-axis).
Y_n(z) via the SCALED signed mp recursion (rhp_midpoint machinery,
log-scale carried) with det Y_n = 1 gated at every snapshot point
and the mp gammahat warded against the f64 wpack chain.  PRECISION
LAW (measured at design time, smoke pass): the Cauchy column C_n(z)
cancels to depth ~ 2 n phi(z) digits (phi = the exterior potential
gap; measured phi <= 0.67 on the sealed panels); SEALED dps table:
dps_Y = 160 on w9/w12/w13, 260 on w26, 80 on the n = 16 world block
(headroom >= 45 digits over the measured worst loss, det-Y gated).
SNAPSHOTS: n in {N/4, N/2, 3N/4, N-1, N} per window; WINDOWS
(9, 12, 13, 26) (w40/N=592 excluded by the sealed runtime budget);
WORLDS at the matched degree n = 16 (below all control flips) on
MAIN/EPSTEIN/SCRAMBLE/SMOOTH (w9 base); ABLATION at n in {N/2, N}:
full model vs noD (D := 1) vs bare (D := 1, N(z) := I -- the pure
electrostatic diagonal): does the Szego layer and the band matrix
carry REAL signal?  READ-OUTS: where is the model good (bulk z =
OUT + FAR), where does it break (GAP/NEAR/band), how does the error
scale with n (Spearman per window over the 5 snapshots) and across
windows at n = N, and is the map world-blind (typed)?

LEG C -- READOUT TEST THROUGH THE MODEL:
(c1) BASE: gammahat_n^model = ((b_n - a_n)/4)^2 vs the true bulk
  gammahat at n in {N/2, 3N/4, N-1} (sealed bars: |model - 1/4| <=
  0.02 AND |model - true| <= 0.1 on all mp windows) -- the r247
  capacity plateau as a MODEL test; plus the h-RATE test: slope of
  (log10 h_n^model - log10 h_n^true) vs n over the free snapshots
  (sealed bar 0.01 decades/degree; the additive OFFSET is reported
  unadjudicated -- rate first, constant later).
(c2) FIBER: T^model = Re intint [K^M_N - K^M_8] dsigma dsigma on the
  border atoms (sealed off-axis regularization x + i 1e-3, y + i
  2e-3; model kernel K^M(x,y) = (M^{-1}(y) M(x))_21/(y - x); the
  centering invariance is the r248 theorem, so sigma is used
  directly) vs the true T = sum_{n=8}^{N-1} rho_n (bitwise r244
  wpack), on windows (9, 12, 13): ratio, sign, N-trend -- honest
  decade bill.

LEG D -- LOCALIZED FOLLOW-UP SPEC (R2-R4) frozen as the module
constant FOLLOWUP_SPEC (SHA delivered under any verdict); the
priority ORDER among R2/R3/R4 is printed from the measured map.

MUST-FAILS (each loud): (m1) swapped sigma3 in the growth factor
(e^{-(G - n ell/2) sigma3}) must blow the OUT-panel error by >= 1e3;
(m2) wrong R-branch (naive principal sqrt((z-a)(z-b)) flips the
sign of R on the LEFT real axis, so D(-inf) != Dinf) must break
the FIK normalization at the left norm points x0 - 1e3/1e4 by
>= 10x; (m3) mass deficit (the mass-(n-1) equilibrium labeled n)
must break the FIK normalization ward loudly (>= 100x); (m4) SIGN
ORACLE:
reading sign h_{N-1} or any flip degree is EXCLUDED by the input
firewall (standing r243 exclusion, re-asserted -- no model path
consumes it).

SEALED CONSTANTS: windows (9, 12, 13, 26); fiber windows (9, 12,
13); snapshots {N//4, N//2, (3N)//4, N-1, N} (+16 on w9 for the
world block, +8 on fiber windows for K^M_8); matched world degree
16; QP: FISTA iters 8000, tol 1e-8, residual bar 1e-6, warm start
ascending, support cut rho > 1e-9; mp: Y dps table {w9/12/13: 160,
w26: 260, worlds: 80}, model wards dps 80, fiber dps 60; panels as
in leg B with deltas 0.05 (NEAR), 0.02 (GAP); norm points x0 + 1e3
/ x0 + 1e4; Richardson bar 1e-4 (rel, vs analytic h_model); det M
bar 1e-30; det Y bar 1e-20; chain ward
bar 1e-8; toy: 64 nodes, masses (8, 12, 16), slope bar 0.05
dec/degree, arg bar 0.5 rad; error rules: bulk = OUT + FAR medians,
ERR_LEVEL 0.5, ERR_BOUND 30.0, decay Spearman <= -0.5 on >= 2
windows, ablation factor 0.8 on >= 2 windows at n = N; base bars
0.02 / 0.1 at snapshots {N//2, 3N//4, N-1}; h-rate bar 0.01
dec/degree; fiber ratio window [0.1, 10] + sign match; world-blind
bar 0.3 decades (SCRAMBLE vs MAIN, all-panel median at n = 16);
fiber regularization dx 1e-3 / dy 2e-3; control flips 25/21/27;
runtime <= 1800 s; smoke = w9 only, snapshots {N//4, N//2}, dps 60,
fiber/worlds/ablation skipped.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  OUTER_MODEL_CARRIES_BULK   iff [Spearman(err_bulk; n) <= -0.5 on
    >= 2 mp windows] AND [err_bulk(n = N) <= 0.5 on ALL mp windows]
    AND BASE_READOUT_CARRIED;
  OUTER_MODEL_PARTIAL        iff BASE_READOUT_CARRIED AND
    [err_bulk(n = N) <= 30 on ALL mp windows] AND [full model beats
    bare by factor <= 0.8 at the bulk median, n = N, on >= 2
    windows];
  OUTER_MODEL_FAILS          otherwise;
  BASE_READOUT_CARRIED = plateau bars AND h-rate bar (leg C c1);
+ FIBER_IN_ERROR_TERM(share) iff sign(T^model) = sign(T^true) on all
    fiber windows AND the median |T^model/T^true| lies in [0.1, 10]
    (share = median |1 - T^model/T^true|: the fiber content sits in
    the measured remainder of the outer model);
  FIBER_BEYOND_MODEL         otherwise (the outer model does not
    even carry the budget's magnitude);
+ ERROR_MAP_FROZEN (always -- the map IS the deliverable)
  [+ MODEL_WORLD_BLIND if |log10(err_SCR/err_MAIN)| < 0.3 at n = 16
    -- admissible for an outer model, typed, never upgraded].
Honesty before beauty: no verdict claims a bound mechanism; the
budget bound and the base law stay OPEN (r243 PAIRCORR_REENCODED
and the r247 B discipline stand unchanged).

RECORD TABLES (frozen from calib_cb pass 1, 21/21, wall 21.3 s;
disclosed SMOKE AMENDMENTS -- all caught by the FIRST smoke pass
(w9, 2 snapshots) BEFORE any full-ladder evaluation; the model
form, the QP, the snapshot sets, the readout formulas and the
adjudication BARS never moved:
(a1) METRIC GAUGE: the draft metric was the raw ||Y M^{-1} - I||;
  the smoke pass showed the raw off-diagonals scale as e^{-+n ell}
  (values 1e+26..1e+54 -- gauge artifact, not model error); the
  metric was moved to the normalized gauge (Deift remainder,
  C-conjugation) as now sealed in leg B.  (a2) PRECISION LAW +
  PANEL: the Cauchy column cancels to ~ 2 n phi(z) digits; the
  draft flat dps 80 and the OUT point b0+2.0 (phi ~ 0.88) were
  replaced by the sealed dps table and b0+1.0 (phi table measured
  in the smoke pass: b+-0.5 ~ 0.49, b+1 ~ 0.66, x0+1.5i ~ 0.60,
  NEAR/GAP ~ 0.03).  (a3) machinery fix: h_n is formed for every
  FREE degree n < N_w (the draft guard tied it to the snapshot cap
  and starved the h-rate readout); h_N stays never-formed.
  (a4) MUST-FAIL m2 re-anchored: the draft compared panel errors at
  a0-0.5, where the honest model error (~7) drowns the branch flip
  (ratio 0.5, not loud); m2 is now structure-pinned at the LEFT
  norm points (the naive sqrt flips sign(R), so D(-inf) != Dinf and
  the FIK normalization breaks); bar 10x unchanged.  (a5) the
  normalization ward is measured in the same normalized gauge):
CAL_VERDICT = OUTER_MODEL_FAILS + FIBER_BEYOND_MODEL +
ERROR_MAP_FROZEN + MODEL_WORLD_BLIND.
Key numbers.  CENSUS: w9/w12/w13/w26 N = 184/151/168/364, free
prefix positive 4/4, T_true = 4.3343/2.8907/4.1449/5.8687, control
flips 25/21/27 re-derived.  LEG A WARDS: QP residual worst 7.6e-9
(bar 1e-6), masses integer-exact, max support-mass distance from
{0, 1} = 0.47 (one near-half mass at the selection boundary,
disclosed; KKT gaps all positive, min +0.14 -- clean multiplier
separation), n*ell at N: -253.4/-206.4/-230.7/-503.2 (e^{n ell} ~
10^-110/-90/-100/-218: the capacity rate in h-currency), Dinf_log
0.05/0.09/0.03/0.18; det M worst 4.2e-81; Richardson vs analytic
h_model 4.0e-6 (bar 1e-4), arg 0; TOY: drift slope -0.017
dec/degree (bar 0.05), offsets +0.31..+0.70 decades (the discrete
constant is NOT perfect even on the toy -- disclosed), (M1)_12
real-positive to 1.4e-7, toy err(1.7+0.9i, n = 12) = 0.548.
TRUE-Y WARDS: det Y worst 2.2e-50, chain ward 1.4e-12.
LEG B -- THE ERROR MAP (normalized gauge, log10 of panel medians;
snapshots n = N/4, N/2, 3N/4, N-1, N):
  w9  OUT +0.60/+0.52/+0.30/+0.99/+0.62  NEAR +0.73/+0.93/+1.08/
      +1.59/+1.55  GAP +0.88/+0.99/+0.98/+1.74/+1.66
  w12 OUT +0.82/+0.56/+0.64/+1.10/+1.22  GAP +1.83/+0.93/+1.05/
      +1.64/+2.14
  w13 OUT +0.97/+0.68/+0.47/+0.64/+0.96  GAP +0.56/+1.12/+1.54/
      +1.68/+1.55
  w26 OUT +0.98/+0.51/+0.67/+1.10/+0.80  GAP +0.54/+1.33/+1.18/
      +1.05/+1.95
READING: the model is never better than err ~ 2 (bulk med at n = N:
4.05/15.6/7.65/5.52 vs level bar 0.5); the error is SMALLEST at
mid-filling (n ~ 3N/4 on w9: bulk 2.66) and SPIKES at the terminal
snapshots; the NEAR/GAP band zone degrades systematically with
filling (w9 GAP +0.88 -> +1.66): the missing structure is LOCAL
(node bands + terminal edge), not a global scalar.  N-TRENDS:
within-window Spearman(err_bulk; n) = +0.50/+0.70/+0.30/+0.20 --
the error RISES with filling (decay clause 0/4); cross-window at
n = N: Spearman(err; N_w) = -0.80 (the error falls with window
size at matched half filling -- the asymptotics helps ACROSS
windows, the filling hurts WITHIN).  WORLDS at n = 16 (all-panel
medians): MAIN 6.31, EPSTEIN 13.0 (+0.31 dec), SCRAMBLE 7.45
(+0.07 dec), SMOOTH 5.41 (-0.07 dec) => MODEL_WORLD_BLIND by the
sealed SCRAMBLE rule (typed, admissible -- the outer model sees
support geometry only; NOTE: EPSTEIN sits +0.31 dec above MAIN,
just over the bar, informational).  ABLATION (bulk med at n = N,
full/noD/bare): w9 4.05/4.12/1.64; w12 15.6/14.7/7.21; w13
7.65/7.37/3.53; w26 5.52/3.71/1.46 -- the clause fires 0/4; the
BARE electrostatic diagonal beats the dressed model POINTWISE by
2.2-3.8x on every window: the arcsine-cell Szego dressing D(z) is
the WRONG pointwise object (it buys the h-rate, below, at the
price of bulk error) -- the loudest structural finding of the map.
LEG C (c1) BASE: gammahat_model = ((b_n - a_n)/4)^2: worst
|model - 1/4| = 1.8e-4 (bar 0.02; every support hull has width
2.000 at the tested snapshots), worst |model - true| = 0.040 (bar
0.1) => the PLATEAU is carried 4/4 (the r247 capacity reading is
the model's Y1 readout, eps fluctuations stay outside); h-RATE:
slopes +0.0069/+0.0018/+0.0026/+0.0027 dec/degree (bar 0.01,
carried 4/4), OFFSETS +1.79/+1.80/+1.69/+1.86 decades
(unadjudicated, sealed): the model OVERSHOOTS every norming
constant by a window-stable factor ~ 50-70x -- a CONSTANT layer is
missing (R3 target), the exponential rate n*ell is right.
BASE_READOUT_CARRIED = YES; the sealed CARRIES/PARTIAL rules still
fail on the error side (decay 0/4, level 0/4, ablation 0/4) =>
OUTER_MODEL_FAILS by the sealed rule -- the honest opening
verdict: the outer model carries the READOUT RATES but not the
POINTWISE matrix.  (c2) FIBER: T_model = -5.37/+15.7/+0.448 vs
T_true = +4.334/+2.891/+4.145 (w9/w12/w13): SIGN MISMATCH on w9,
magnitudes scattered over 2 decades, ratio N-trend -1.00 =>
FIBER_BEYOND_MODEL: the outer model does not carry the budget's
magnitude or sign -- the ENTIRE extensive budget lives beyond the
outer form, consistent with r246/r248 EXTENSIVE_IRREGULAR_TAIL (no
macroprofile for an outer kernel to reproduce).  LEG D: priority
from the map: R2 (band zone, GAP +1.7..+2.1 at n = N) > R4 (fiber
transfer, sign + 2 decades) > R3 (h constant, +1.8 dec); spec SHA
in G50.  MUST-FAILS all loud: m1 swapped sigma3 9.5e+77 x; m2
wrong branch 145.2 >= 10; m3 mass deficit 1.0e+138 vs honest
5.8e-3; m4 oracle excluded.  Runtime 21.3 s full, 0.9 s smoke;
run1/run2 identical up to the WALL line.
AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
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
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import szego_equilibrium_probe as SZ         # noqa: E402 r232a
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

WINDOWS_MP = (9, 12, 13, 26)
FIBER_KZ = (9, 12, 13)
MATCH_N = 16
FIB_LO = 8
QP_ITERS = 8000
QP_TOL = 1e-8
QP_RES_BAR = 1e-6
RHO_SEL = 1e-9
DPS_Y_TAB = {9: 160, 12: 160, 13: 160, 26: 260}
DPS_Y_WORLD = 80
DPS_MODEL = 80
DPS_FIBER = 60
DELTA_NEAR = 0.05
DELTA_GAP = 0.02
FIB_DX = 1e-3
FIB_DY = 2e-3
NORM_OFFS = (1e3, 1e4)
RICH_BAR = 1e-4
DETM_BAR = 1e-30
DETY_BAR = 1e-20
CHAIN_BAR = 1e-8
TOY_SLOPE_BAR = 0.05
TOY_ARG_BAR = 0.5
ERR_LEVEL_BAR = 0.5
ERR_BOUND_BAR = 30.0
DECAY_SP_BAR = -0.5
DECAY_MIN_W = 2
ABL_FACTOR = 0.8
ABL_MIN_W = 2
PLATEAU_ABS = 0.02
PLATEAU_TRUE = 0.1
H_RATE_BAR = 0.01
FIB_RATIO_LO = 0.1
FIB_RATIO_HI = 10.0
WB_DEC = 0.3
M2_RATIO_BAR = 10.0
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
CAL_VERDICT = ("OUTER_MODEL_FAILS + FIBER_BEYOND_MODEL + "
               "ERROR_MAP_FROZEN + MODEL_WORLD_BLIND")

FOLLOWUP_SPEC = """\
TFPT RH-LANE CENTERED_BASEFIBER FOLLOW-UP SPEC (frozen r250) --
the localized requirement document R2-R4 of the nonperturbative
campaign; the priority ORDER is set by this round's error map.
R2 NODE-BAND LOCAL PARAMETRIX: object = the discrete local problem
  at single nodes / node bands (residue triangularity of the FIK
  jump at the atoms, the discrete Airy-free local model of the
  r233/r234 fixed-offset class); input = this round's GAP/NEAR
  panel errors (the map's band zone); acceptance = the R2-dressed
  model must reduce the GAP-panel median ||R - I|| by >= 1 decade
  on w9/w13 WITHOUT touching the OUT-panel level; all falsifiers
  carried unchanged.
R3 SATURATION/EDGE LAYER (the norming-constant owner): object = the
  constrained-equilibrium saturation boundaries (KKT-active bands)
  and the hull edges; input = the measured KKT gaps, the NEAR-panel
  level, and the h-decade OFFSET of leg C (the rate is carried, the
  constant is not); acceptance = a saturated-region correction
  (oscillatory/theta layer in the BKMM class) that moves the
  h-decade offset below 0.5 while keeping the rate, with NO refit
  of D or ell.
R4 SIGMA0-PAIRING TRANSFER (the fiber): object = the exact remainder
  identity T_true - T_model = intint ([K^Y_N - K^M_N] - [K^Y_8 -
  K^M_8]) dsigma dsigma (centering-invariant, r248); input = the c2
  share/decades and the R-map panels; acceptance = an error-kernel
  bound that reproduces the measured share on w9/w12/w13 within a
  factor 2 AND separates SCRAMBLE by >= 1 decade pre-flip; the B
  discipline (r247) binds unchanged; no control certified.
"""
FOLLOWUP_SHA = hashlib.sha256(FOLLOWUP_SPEC.encode("utf-8")).hexdigest()

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the model consumes "
                       "node positions + |weights| + the QP "
                       "minimizer ONLY; h_N never formed; flips/"
                       "signs enter gates only (m4 oracle EXCLUDED)"
                       if not bad else "; ".join(bad))


# ----------------------------------------------------------- panels
def build_panels(x):
    """sealed world-blind z-panels from the sorted union nodes."""
    a0, b0 = float(x[0]), float(x[-1])
    x0 = 0.5 * (a0 + b0)
    gaps = np.diff(x)
    gi = np.argsort(gaps)[::-1][:3]
    gm = [0.5 * (float(x[i]) + float(x[i + 1])) for i in gi]
    pan = {
        "OUT": [b0 + 0.5, a0 - 0.5, b0 + 1.0],
        "FAR": [x0 + 1.5j, x0 - 1.0 + 1.0j, x0 + 1.0 + 1.0j],
        "NEAR": [x0 + 1j * DELTA_NEAR, gm[0] + 1j * DELTA_NEAR],
        "GAP": [g + 1j * DELTA_GAP for g in gm],
    }
    norm_z = [x0 + NORM_OFFS[0], x0 + NORM_OFFS[1]]
    return pan, norm_z, x0, a0, b0


PAN_ORDER = ("OUT", "FAR", "NEAR", "GAP")


def flat_panels(pan):
    zs, tags = [], []
    for c in PAN_ORDER:
        for z in pan[c]:
            zs.append(z)
            tags.append(c)
    return zs, tags


# ------------------------------------------------------- equilibrium
def eq_field(d):
    """union setup + exact weight field (r232a objects verbatim)."""
    x, wt, A, Lip = SZ.union_setup(d)
    V = -np.log(np.maximum(np.abs(wt), 1e-300))
    return x, wt, A, Lip, V


def model_data(x, wt, A, V, rho, mass):
    """sealed model data from the mass-n equilibrium (leg A a1/a2)."""
    F = 2.0 * (A @ rho) + V
    sel = rho > RHO_SEL
    nround = int(np.sum(np.round(rho)))
    lam_lo = float(np.max(F[sel]))
    lam_hi = float(np.min(F[~sel])) if np.any(~sel) else lam_lo
    lam = 0.5 * (lam_lo + lam_hi)
    nl = -lam
    xs = np.asarray(x[sel], float)
    a, b = float(xs[0]), float(xs[-1])
    cw = np.empty(len(x))
    if len(x) > 2:
        cw[1:-1] = 0.5 * (x[2:] - x[:-2])
    cw[0] = x[1] - x[0]
    cw[-1] = x[-1] - x[-2]
    Lf = np.log(np.maximum(np.abs(wt), 1e-300) / cw)
    L = np.asarray(Lf[sel], float)
    cbd = np.empty(len(xs) + 1)
    cbd[0], cbd[-1] = a, b
    if len(xs) > 1:
        cbd[1:-1] = 0.5 * (xs[1:] + xs[:-1])
    u = np.clip((2.0 * cbd - a - b) / max(b - a, 1e-300), -1.0, 1.0)
    nu = np.diff(np.arcsin(u)) / math.pi
    dinf_log = 0.5 * float(np.sum(nu * L))
    hmod_l10 = ((math.log(2.0 * math.pi) + nl + 2.0 * dinf_log
                 + math.log((b - a) / 4.0)) / math.log(10.0))
    return dict(mass=mass, nsel=int(sel.sum()), nround=nround,
                a=a, b=b, nl=nl, kkt=lam_hi - lam_lo,
                sat01=float(np.max(np.minimum(rho[sel],
                                              1.0 - rho[sel]))),
                xs=xs, rho_s=np.asarray(rho[sel], float),
                nu=nu, L=L, dinf_log=dinf_log,
                hmod_l10=hmod_l10,
                gam_mod=((b - a) / 4.0) ** 2)


def model_at(md, z, dps, variant="full"):
    """the sealed outer model M_n(z) as a 2x2 mp matrix (leg A a3)."""
    import mpmath as mp
    mp.mp.dps = dps
    zc = mp.mpc(z)
    gs = mp.fsum(mp.mpf(float(r)) * mp.log(zc - mp.mpf(float(xx)))
                 for r, xx in zip(md["rho_s"], md["xs"]))
    nl = mp.mpf(md["nl"])
    a = mp.mpf(md["a"])
    b = mp.mpf(md["b"])
    if variant == "bare":
        n11 = mp.mpc(1)
        n12 = mp.mpc(0)
        n21 = mp.mpc(0)
    else:
        beta = ((zc - b) / (zc - a)) ** mp.mpf("0.25")
        n11 = (beta + 1 / beta) / 2
        n12 = (beta - 1 / beta) / mp.mpc(0, 2)
        n21 = -n12
    if variant in ("noD", "bare"):
        Dinf = mp.mpf(1)
        Dz = mp.mpc(1)
    else:
        if variant == "m2":
            Rz = mp.sqrt((zc - a) * (zc - b))
        else:
            Rz = (zc - a) * (((zc - b) / (zc - a)) ** mp.mpf("0.5"))
        dlog = (Rz / 2) * mp.fsum(
            mp.mpf(float(nn)) * mp.mpf(float(ll))
            / (zc - mp.mpf(float(ss)))
            for nn, ll, ss in zip(md["nu"], md["L"], md["xs"]))
        Dinf = mp.e ** mp.mpf(md["dinf_log"])
        Dz = mp.e ** dlog
    if variant == "m1":
        P = mp.e ** (-(gs - nl / 2))
    else:
        P = mp.e ** (gs - nl / 2)
    e_p = mp.e ** (nl / 2)
    e_m = mp.e ** (-nl / 2)
    M11 = e_p * Dinf * n11 * P / Dz
    M12 = e_p * Dinf * n12 * Dz / P
    M21 = e_m * n21 * P / (Dinf * Dz)
    M22 = e_m * Dz * n11 / (Dinf * P)
    kap = mp.mpc(0, -2) * mp.pi
    return ((M11, kap * M12), (M21 / kap, M22))


def err_RI(Y, M, nl):
    """sealed error metric: ||C^{-1} (Y M^{-1}) C - I||_F with
    C = e^{(n ell/2) sigma3} (the normalized-gauge remainder;
    nl = n * ell_n from the model)."""
    import mpmath as mp
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    a11 = M[1][1] / det
    a12 = -M[0][1] / det
    a21 = -M[1][0] / det
    a22 = M[0][0] / det
    R11 = Y[0][0] * a11 + Y[0][1] * a21
    R12 = Y[0][0] * a12 + Y[0][1] * a22
    R21 = Y[1][0] * a11 + Y[1][1] * a21
    R22 = Y[1][0] * a12 + Y[1][1] * a22
    enl = mp.e ** mp.mpf(nl)
    R12 = R12 / enl
    R21 = R21 * enl
    return float(mp.sqrt(abs(R11 - 1) ** 2 + abs(R12) ** 2
                         + abs(R21) ** 2 + abs(R22 - 1) ** 2))


def detm_dev(M):
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return float(abs(det - 1))


def rich_M1_12(md, n, norm_z, dps, variant="full"):
    """Richardson extraction of (M1)_12 from the FIK normalization
    E(z) = C^{-1} (M z^{-n sigma3}) C - I = M1_conj/z + O(z^-2)
    (normalized gauge, C = e^{(n ell/2) sigma3}; the returned
    m1_12 is de-conjugated back to the raw (M1)_12)."""
    import mpmath as mp
    mp.mp.dps = dps
    enl = mp.e ** mp.mpf(md["nl"])
    vals = []
    devs = []
    for z in norm_z:
        zc = mp.mpc(z)
        M = model_at(md, z, dps, variant=variant)
        zpn = zc ** (-int(n))
        E11 = M[0][0] * zpn - 1
        E12 = M[0][1] / zpn / enl
        E21 = M[1][0] * zpn * enl
        E22 = M[1][1] / zpn - 1
        devs.append(float(max(abs(E11), abs(E12), abs(E21),
                               abs(E22))))
        vals.append((zc, zc * E12))
    z1, v1 = vals[0]
    z2, v2 = vals[1]
    m1_12 = (z2 * v2 - z1 * v1) / (z2 - z1) * enl
    return m1_12, devs


# --------------------------------------------------------- mp Y pass
def mp_y_pass(d, snaps, zpts, dps, Nb):
    """scaled signed mp recursion (rhp_midpoint machinery) on
    mutilde; returns per snapshot n the FIK matrix Y_n(z) at every
    panel point plus det-Y devs, and the mp gammahat/h tables.
    Nb = builder depth: h_n is formed only for FREE degrees n < Nb;
    the forced pivot h_Nb is NEVER formed."""
    import mpmath as mp
    mp.mp.dps = dps
    nds = ([mp.mpf(float(v)) for v in d["xs"]]
           + [mp.mpf(float(v)) for v in d["ys"]])
    wt = ([mp.mpf(float(v)) for v in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    S = len(nds)
    nmax = max(snaps)
    zc = [mp.mpc(z) for z in zpts]
    qk = [mp.mpf(1)] * S
    qkm = [mp.mpf(0)] * S
    qz = [mp.mpc(1) for _ in zc]
    qzm = [mp.mpc(0) for _ in zc]
    Ls = mp.mpf(0)
    Ls_m = mp.mpf(0)
    eta = mp.fsum(w * q * q for w, q in zip(wt, qk))
    eta_m = eta
    lg_h = mp.log(abs(eta))
    sg_h = mp.sign(eta)
    hlog = {0: (lg_h, sg_h)}
    gam = {}
    out = {}
    for k in range(nmax):
        aco = mp.fsum(w * x * q * q
                      for w, x, q in zip(wt, nds, qk)) / eta
        if k == 0:
            nx = [(x - aco) * q for x, q in zip(nds, qk)]
            nz = [(z - aco) * c for z, c in zip(zc, qz)]
        else:
            ge = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            fc = mp.e ** (Ls_m - Ls)
            nx = [(x - aco) * q - ge * fc * r
                  for x, q, r in zip(nds, qk, qkm)]
            nz = [(z - aco) * c - ge * fc * r
                  for z, c, r in zip(zc, qz, qzm)]
        sc = max(abs(t) for t in nx)
        qkm, eta_m, Ls_m, qzm = qk, eta, Ls, qz
        qk = [t / sc for t in nx]
        qz = [c / sc for c in nz]
        Ls = Ls + mp.log(sc)
        n = k + 1
        if n < Nb:
            eta = mp.fsum(w * q * q for w, q in zip(wt, qk))
            g = (eta / eta_m) * mp.e ** (2 * (Ls - Ls_m))
            lg_h += mp.log(abs(g))
            sg_h *= mp.sign(g)
            hlog[n] = (lg_h, sg_h)
            gam[n] = float(g)
        if n in snaps:
            lgm, sgm = hlog[n - 1]
            h_prev = sgm * mp.e ** lgm
            eLs = mp.e ** Ls
            eLm = mp.e ** Ls_m
            Ys = {}
            dety = 0.0
            for iz, z in enumerate(zc):
                Cn = eLs * mp.fsum(w * q / (z - x)
                                   for w, q, x in zip(wt, qk, nds))
                Cm = eLm * mp.fsum(w * q / (z - x)
                                   for w, q, x in zip(wt, qkm, nds))
                Y = ((eLs * qz[iz], Cn),
                     (eLm * qzm[iz] / h_prev, Cm / h_prev))
                dv = abs(Y[0][0] * Y[1][1] - Y[0][1] * Y[1][0] - 1)
                dety = max(dety, float(dv))
                Ys[iz] = Y
            out[n] = dict(Y=Ys, dety=dety,
                          h_prev_l10=float(lgm / mp.log(10)),
                          sg_prev=float(sgm))
    return out, gam, hlog


# --------------------------------------------------------- toy block
def toy_chain_f64(x, w, nmax):
    qk = np.ones_like(x)
    qkm = np.zeros_like(x)
    hs = [float(np.sum(w))]
    als = []
    for k in range(nmax):
        aco = float(np.sum(w * x * qk * qk)) / hs[-1]
        als.append(aco)
        g = hs[-1] / hs[-2] if k > 0 else 0.0
        nx = (x - aco) * qk - g * qkm
        qkm, qk = qk, nx
        hs.append(float(np.sum(w * qk * qk)))
    return als, hs


def toy_block(dps):
    """discrete Chebyshev-U toy: 64 nodes, w = (1 - x^2) pi/64;
    exact f64 chain vs the sealed model (leg A ward)."""
    m = 64
    xt = np.sort(np.cos(np.pi * (np.arange(m) + 0.5) / m))
    wtt = (1.0 - xt * xt) * (np.pi / m)
    D = np.abs(xt[:, None] - xt[None, :])
    np.fill_diagonal(D, 1.0)
    A = -np.log(D)
    np.fill_diagonal(A, 0.0)
    v = np.ones(m) / math.sqrt(m)
    for _ in range(80):
        v2 = A @ v
        nv = float(np.linalg.norm(v2))
        v = v2 / nv
    Lip = 2.0 * nv
    V = -np.log(wtt)
    als, hs = toy_chain_f64(xt, wtt, 18)
    drift = []
    rho = None
    md12 = None
    res_w = 0.0
    for n in (8, 12, 16):
        rho, res = SZ.solve_qp(A, Lip, V, float(n), rho0=rho,
                               iters=QP_ITERS, tol=QP_TOL)
        res_w = max(res_w, res)
        md = model_data(xt, wtt, A, V, rho, n)
        drift.append((n, md["hmod_l10"] - math.log10(hs[n])))
        if n == 12:
            md12 = md
    sl = float(np.polyfit([t[0] for t in drift],
                          [t[1] for t in drift], 1)[0])
    # Richardson arg check + a true-Y error probe at n = 12
    x0 = 0.5 * (float(xt[0]) + float(xt[-1]))
    m1_12, _devs = rich_M1_12(md12, 12, [x0 + NORM_OFFS[0],
                                         x0 + NORM_OFFS[1]], dps)
    import mpmath as mp
    argdev = abs(float(mp.arg(m1_12)))
    rel = abs(float(mp.log(abs(m1_12), 10)) - md12["hmod_l10"])
    z0 = 1.7 + 0.9j
    # true toy Y at n = 12 (f64 is exact enough at depth 12)
    def pval(nn, z):
        p0, p1 = 1.0 + 0j, z - als[0]
        if nn == 0:
            return p0
        for kk in range(1, nn):
            p0, p1 = p1, (z - als[kk]) * p1 \
                - (hs[kk] / hs[kk - 1]) * p0
        return p1

    def cval(nn, z):
        px = np.array([pval(nn, complex(xx)) for xx in xt])
        return complex(np.sum(wtt * px / (z - xt)))

    Yt = ((mp.mpc(pval(12, z0)), mp.mpc(cval(12, z0))),
          (mp.mpc(pval(11, z0) / hs[11]),
           mp.mpc(cval(11, z0) / hs[11])))
    Mt = model_at(md12, z0, dps)
    e12 = err_RI(Yt, Mt, md12["nl"])
    return dict(slope=sl, drift=drift, argdev=argdev, rel=rel,
                err12=e12, res=res_w)


# ------------------------------------------------------- fiber block
def fiber_T_model(md_hi, md_lo, atoms, wts, dps):
    """T^model = Re intint [K^M_hi - K^M_lo] dsigma dsigma with the
    sealed off-axis regularization; model values mp -> complex128
    (exponents f64-safe for N <= 184, sealed fiber windows)."""
    za = atoms + 1j * FIB_DX
    yb = atoms + 1j * FIB_DY
    out = []
    ok_fin = True
    for md in (md_hi, md_lo):
        u = np.empty(len(atoms), complex)
        vv = np.empty(len(atoms), complex)
        p = np.empty(len(atoms), complex)
        q = np.empty(len(atoms), complex)
        for i in range(len(atoms)):
            Mx = model_at(md, complex(za[i]), dps)
            My = model_at(md, complex(yb[i]), dps)
            u[i] = complex(Mx[0][0])
            vv[i] = complex(Mx[1][0])
            p[i] = complex(My[0][0])
            q[i] = complex(My[1][0])
        ok_fin = ok_fin and bool(np.all(np.isfinite(u))
                                 and np.all(np.isfinite(vv))
                                 and np.all(np.isfinite(p))
                                 and np.all(np.isfinite(q)))
        Dn = (atoms[None, :] - atoms[:, None]
              + 1j * (FIB_DY - FIB_DX))
        K = (-q[None, :] * u[:, None]
             + p[None, :] * vv[:, None]) / Dn
        out.append(float(np.real(wts @ K @ wts)))
    return out[0] - out[1], ok_fin


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    dps_m = 60 if smoke else DPS_MODEL
    windows = (9,) if smoke else WINDOWS_MP

    print("=" * 78)
    print("centered_basefiber_probe -- PRIME.PORT.RHP."
          "CENTERED_BASEFIBER.01 (round 250)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 only, 2 snapshots, fiber/worlds/"
                        "ablation skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "model form, z-panels, snapshots, worlds, ablations and "
          "ALL verdict rules sealed in the frozen spec BEFORE "
          "evaluation; windows %s, fiber %s, matched degree %d; "
          "QP iters %d tol %.0e bar %.0e; dps Y table %s (worlds "
          "%d) / model %d / fiber %d; SEALED METRIC: normalized-"
          "gauge remainder ||C^-1 Y M^-1 C - I||_F, C = e^{(n "
          "ell/2) sigma3}; err rules: level %.1f, bound %.1f, "
          "decay Spearman <= %.1f on >= %d windows, ablation "
          "factor %.1f; base bars %.2f/%.1f, h-rate %.2f "
          "dec/deg; fiber ratio [%.1f, %.1f]; world-blind bar "
          "%.1f decades"
          % (str(WINDOWS_MP), str(FIBER_KZ), MATCH_N, QP_ITERS,
             QP_TOL, QP_RES_BAR, str(DPS_Y_TAB), DPS_Y_WORLD,
             DPS_MODEL, DPS_FIBER,
             ERR_LEVEL_BAR, ERR_BOUND_BAR, DECAY_SP_BAR,
             DECAY_MIN_W, ABL_FACTOR, PLATEAU_ABS, PLATEAU_TRUE,
             H_RATE_BAR, FIB_RATIO_LO, FIB_RATIO_HI, WB_DEC))

    # ---------------- S1: leg 0 -- contract + census + controls
    section("S1  LEG 0 -- CONTRACT FREEZE + CENSUS + CONTROLS")
    check("G10-contract-frozen", True,
          "TARGETS: base = bulk gammahat band (r247 plateau 1/4, "
          "worst |eps| 0.093), fiber = terminal CD readout T (r248, "
          "centering-invariant, mp 3.3e-160); THREE-ZONE TYPING "
          "(corrected): GEOMETRIC_RANK1_HEAD + LOWMODE_SUPPORT_"
          "SILENCE (r249 correction: the stillness is support "
          "geometry + a pairing statement) + EXTENSIVE_PAIRING_"
          "SENSITIVE_TAIL; B PROVENANCE: IMPORTED, parametric "
          "tau^aug(B), only B_w = S_{N-2} + 5/7 covers (r247, "
          "unchanged); FALSIFIERS: SMOOTH/EPSTEIN break the BASE "
          "at 27/25, SCRAMBLE is the fiber falsifier; a world-"
          "blind outer error map is admissible but TYPED")
    packs = {kz: BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPSTEIN", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCRAMBLE", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    check("G11-control-flips", okCf,
          "control BASE flips re-derived AT the sealed degrees %s "
          "(hard falsifier battery armed)"
          % str({c: ctrl[c]["nf"] for c in ctrl}))
    okC = all(packs[kz]["nf"] is None for kz in windows)
    tt_note = "; ".join(
        "w%d: N=%d, T_true=%.4f" % (kz, packs[kz]["N"],
                                    packs[kz]["St"]
                                    - float(packs[kz]["S"][FIB_LO
                                                           - 1]))
        for kz in windows)
    check("G12-census", okC,
          "free prefix positive on %d/%d mp windows; true fiber "
          "readouts (bitwise r244 objects): %s"
          % (sum(1 for kz in windows
                 if packs[kz]["nf"] is None), len(windows),
             tt_note))

    # ---------------- S2: leg A -- model construction + wards
    section("S2  LEG A -- MODEL CONSTRUCTION + WARDS")
    toy = toy_block(dps_m)
    ok_toy = (abs(toy["slope"]) <= TOY_SLOPE_BAR
              and toy["argdev"] <= TOY_ARG_BAR
              and toy["rel"] <= 1e-3)
    check("G22-toy-ward", ok_toy,
          "discrete Chebyshev-U toy (64 nodes): model-vs-true h "
          "decade drift %s -> slope %+.4f dec/degree (bar %.2f); "
          "(M1)_12 real-positive (arg dev %.1e rad, bar %.1f; "
          "log10 modulus vs analytic %.1e); err(1.7+0.9i, n = 12) "
          "= %.3f (INFO level); QP residual %.1e -- the sealed "
          "-2 pi i calibration and the h-rate are CORRECT on the "
          "exactly solvable toy"
          % (str([(n, round(dl, 3)) for n, dl in toy["drift"]]),
             toy["slope"], TOY_SLOPE_BAR, toy["argdev"],
             TOY_ARG_BAR, toy["rel"], toy["err12"], toy["res"]))

    wd = {}
    res_worst = 0.0
    mass_ok = True
    sat_worst = 0.0
    kkt_min = float("inf")
    detm_worst = 0.0
    rich_worst = 0.0
    richarg_worst = 0.0
    for kz in windows:
        p = packs[kz]
        d = p["d"]
        N = p["N"]
        x, wt, A, Lip, V = eq_field(d)
        pan, norm_z, x0, a0, b0 = build_panels(x)
        zs, tags = flat_panels(pan)
        snaps = sorted({N // 4, N // 2, (3 * N) // 4, N - 1, N}
                       if not smoke else {N // 4, N // 2})
        extra = set()
        if kz == 9 and not smoke:
            extra.add(MATCH_N)
        if kz in FIBER_KZ and not smoke:
            extra.add(FIB_LO)
        masses = sorted(set(snaps) | extra)
        mds = {}
        rho = None
        for n in masses:
            rho, res = SZ.solve_qp(A, Lip, V, float(n), rho0=rho,
                                   iters=QP_ITERS, tol=QP_TOL)
            res_worst = max(res_worst, res)
            md = model_data(x, wt, A, V, rho, n)
            mass_ok = mass_ok and (md["nround"] == n)
            sat_worst = max(sat_worst, md["sat01"])
            kkt_min = min(kkt_min, md["kkt"])
            mds[n] = md
        # model wards on this window
        for n in (snaps[-1], snaps[0]):
            md = mds[n]
            for z in (zs[0], zs[3], zs[-1]):
                detm_worst = max(detm_worst,
                                 detm_dev(model_at(md, z, dps_m)))
            m1_12, devs = rich_M1_12(md, n, norm_z, dps_m)
            import mpmath as mp
            rich_worst = max(rich_worst,
                             abs(float(mp.log(abs(m1_12), 10))
                                 - md["hmod_l10"]))
            richarg_worst = max(richarg_worst,
                                abs(float(mp.arg(m1_12))))
        info("w%-3d N=%d: snaps %s; support hull [%.3f, %.3f]; "
             "n*ell at N: %.2f (e^{nl} ~ 10^%.1f); KKT gaps "
             "[%.1e, %.1e]; Dinf_log at N: %.3f"
             % (kz, N, str(masses), mds[snaps[-1]]["a"],
                mds[snaps[-1]]["b"], mds[snaps[-1]]["nl"],
                mds[snaps[-1]]["nl"] / math.log(10),
                min(mds[n]["kkt"] for n in masses),
                max(mds[n]["kkt"] for n in masses),
                mds[snaps[-1]]["dinf_log"]))
        wd[kz] = dict(p=p, d=d, N=N, x=x, wt=wt, A=A, V=V,
                      pan=pan, zs=zs, tags=tags, norm_z=norm_z,
                      x0=x0, a0=a0, b0=b0, snaps=snaps, mds=mds)
    check("G20-qp-wards", res_worst <= QP_RES_BAR and mass_ok,
          "constrained-equilibrium QP (r232a solver verbatim): "
          "fixed-point residual worst %.1e (bar %.0e); every "
          "rounded mass integer-exact; saturation: max distance "
          "of a support mass from {0, 1} = %.1e (0/1 selection "
          "regime, r232 reproduced); min KKT gap %+.1e (%s)"
          % (res_worst, QP_RES_BAR, sat_worst,
             kkt_min,
             "clean multiplier separation" if kkt_min > 0
             else "NEGATIVE gap typed, midpoint rule sealed"))
    check("G21-model-algebra-wards",
          detm_worst <= DETM_BAR and rich_worst <= RICH_BAR
          and richarg_worst <= 1e-6,
          "det M = 1 at panel points to %.1e (bar %.0e, exact "
          "algebra of the one-cut form); FIK normalization: "
          "Richardson (M1)_12 vs the analytic h_n^model = 2 pi "
          "e^{n ell} Dinf^2 (b-a)/4: log10 dev worst %.1e (bar "
          "%.0e), arg dev worst %.1e -- the model IS normalized "
          "like Y_n and its 1/z readout is the derived formula"
          % (detm_worst, DETM_BAR, rich_worst, RICH_BAR,
             richarg_worst))

    # ---------------- S3: leg B -- the error map
    section("S3  LEG B -- THE ERROR MAP (Y_n M_n^{-1} vs I)")
    dety_worst = 0.0
    chain_worst = 0.0
    errmap = {}
    gam_true = {}
    hlog_true = {}
    for kz in windows:
        W = wd[kz]
        dps_w = 100 if smoke else DPS_Y_TAB[kz]
        ypass, gam, hlog = mp_y_pass(W["d"], set(W["snaps"])
                                     | ({MATCH_N} if kz == 9
                                        and not smoke else set()),
                                     W["zs"], dps_w, W["N"])
        gam_true[kz] = gam
        hlog_true[kz] = hlog
        rows = W["p"]["rows"]
        for n in (12, W["N"] // 2):
            if n in gam:
                chain_worst = max(chain_worst,
                                  abs(gam[n]
                                      / rows[n - 1]["gam_next"]
                                      - 1.0))
        errmap[kz] = {}
        for n, snap in ypass.items():
            dety_worst = max(dety_worst, snap["dety"])
            if n not in W["snaps"] and not (kz == 9
                                            and n == MATCH_N):
                continue
            md = W["mds"][n]
            errs = {}
            for iz, z in enumerate(W["zs"]):
                M = model_at(md, z, dps_m)
                errs[iz] = err_RI(snap["Y"][iz], M, md["nl"])
            errmap[kz][n] = dict(errs=errs, snap=snap)
        # print the map rows
        for n in sorted(errmap[kz]):
            errs = errmap[kz][n]["errs"]
            med = {}
            for c in PAN_ORDER:
                vals = [errs[iz] for iz, t in enumerate(W["tags"])
                        if t == c]
                med[c] = float(np.median(vals))
            bulk = float(np.median(
                [errs[iz] for iz, t in enumerate(W["tags"])
                 if t in ("OUT", "FAR")]))
            errmap[kz][n]["med"] = med
            errmap[kz][n]["bulk"] = bulk
            info("w%-3d n=%-4d err log10: OUT %+.2f FAR %+.2f "
                 "NEAR %+.2f GAP %+.2f | bulk med %.4g"
                 % (kz, n, math.log10(max(med["OUT"], 1e-300)),
                    math.log10(max(med["FAR"], 1e-300)),
                    math.log10(max(med["NEAR"], 1e-300)),
                    math.log10(max(med["GAP"], 1e-300)), bulk))
    check("G23-trueY-wards", dety_worst <= DETY_BAR
          and chain_worst <= CHAIN_BAR,
          "det Y_n = 1 at every snapshot panel point to %.1e "
          "(bar %.0e, scaled mp recursion, sealed dps table %s); "
          "mp gammahat vs the f64 wpack chain: worst rel %.1e "
          "(bar %.0e) -- the Y side of the map is not an artifact"
          % (dety_worst, DETY_BAR, str(DPS_Y_TAB), chain_worst,
             CHAIN_BAR))
    check("G30-error-map-measured", True,
          "the error map (rows above): panels x windows x "
          "snapshots, normalized-gauge ||C^-1 Y_n M_n^{-1} C - "
          "I||_F -- ERROR_MAP_FROZEN is the round's deliverable "
          "under any verdict")
    # N-trend
    decay_n = 0
    sp_note = []
    for kz in windows:
        W = wd[kz]
        ns = [n for n in sorted(errmap[kz]) if n in W["snaps"]]
        bulks = [errmap[kz][n]["bulk"] for n in ns]
        sp = BH.spearman(bulks, ns)
        if sp <= DECAY_SP_BAR:
            decay_n += 1
        sp_note.append("w%d %+.2f" % (kz, sp))
    bulk_at_N = {kz: errmap[kz][wd[kz]["snaps"][-1]]["bulk"]
                 for kz in windows}
    Ns_all = [wd[kz]["N"] for kz in windows]
    sp_cross = (BH.spearman([bulk_at_N[kz] for kz in windows],
                            Ns_all) if len(windows) > 1
                else float("nan"))
    check("G31-error-N-trend", True,
          "within-window filling trend Spearman(err_bulk; n): %s "
          "(decay <= %.1f on %d/%d windows, clause needs >= %d); "
          "bulk err at n = N: %s; cross-window Spearman(err_bulk"
          "(N); N_w) = %+.2f (matched half filling)"
          % ("; ".join(sp_note), DECAY_SP_BAR, decay_n,
             len(windows), DECAY_MIN_W,
             str({("w%d" % kz): round(bulk_at_N[kz], 3)
                  for kz in windows}), sp_cross))
    # worlds at matched degree
    wb_mod = ""
    if smoke:
        check("G32-worlds", True, "SMOKE: world block skipped")
        check("G33-ablation", True, "SMOKE: ablation skipped")
    else:
        world_med = {}
        e9 = errmap[9][MATCH_N]["errs"]
        world_med["MAIN"] = float(np.median(list(e9.values())))
        for cname in ("EPSTEIN", "SCRAMBLE", "SMOOTH"):
            pc = ctrl[cname]
            dc = pc["d"]
            xc, wtc, Ac, Lipc, Vc = eq_field(dc)
            panc, _nz, _x0, _a0, _b0 = build_panels(xc)
            zsc, tagsc = flat_panels(panc)
            rhoc, resc = SZ.solve_qp(Ac, Lipc, Vc, float(MATCH_N),
                                     iters=QP_ITERS, tol=QP_TOL)
            res_worst = max(res_worst, resc)
            mdc = model_data(xc, wtc, Ac, Vc, rhoc, MATCH_N)
            ypc, _g, _h = mp_y_pass(dc, {MATCH_N}, zsc,
                                    DPS_Y_WORLD, dc["n_max"])
            ec = [err_RI(ypc[MATCH_N]["Y"][iz],
                         model_at(mdc, z, dps_m), mdc["nl"])
                  for iz, z in enumerate(zsc)]
            world_med[cname] = float(np.median(ec))
        decs = {c: math.log10(world_med[c] / world_med["MAIN"])
                for c in ("EPSTEIN", "SCRAMBLE", "SMOOTH")}
        wb = abs(decs["SCRAMBLE"]) < WB_DEC
        if wb:
            wb_mod = " + MODEL_WORLD_BLIND"
        check("G32-worlds", True,
              "matched degree n = %d, all-panel medians: MAIN "
              "%.3f, EPSTEIN %.3f (%+.2f dec), SCRAMBLE %.3f "
              "(%+.2f dec), SMOOTH %.3f (%+.2f dec) -- sealed "
              "rule: %s (an outer model that sees only support "
              "geometry is admissible; the arithmetic lives in "
              "the error term by construction, typed)"
              % (MATCH_N, world_med["MAIN"], world_med["EPSTEIN"],
                 decs["EPSTEIN"], world_med["SCRAMBLE"],
                 decs["SCRAMBLE"], world_med["SMOOTH"],
                 decs["SMOOTH"],
                 "MODEL_WORLD_BLIND (|SCR dec| < %.1f)" % WB_DEC
                 if wb else "the map SEPARATES the worlds"))
        # ablation
        abl_n = 0
        abl_note = []
        for kz in windows:
            W = wd[kz]
            N = W["N"]
            md = W["mds"][N]
            bulk_z = [(iz, z) for iz, z in enumerate(W["zs"])
                      if W["tags"][iz] in ("OUT", "FAR")]
            snap = errmap[kz][N]["snap"]
            row = {}
            for var in ("full", "noD", "bare"):
                ev = [err_RI(snap["Y"][iz],
                             model_at(md, z, dps_m, variant=var),
                             md["nl"])
                      for iz, z in bulk_z]
                row[var] = float(np.median(ev))
            if row["full"] <= ABL_FACTOR * row["bare"]:
                abl_n += 1
            abl_note.append("w%d %.3g/%.3g/%.3g" % (
                kz, row["full"], row["noD"], row["bare"]))
        check("G33-ablation", True,
              "bulk median at n = N, full/noD/bare: %s -- the "
              "full model beats the bare electrostatic diagonal "
              "by factor <= %.1f on %d/%d windows (clause needs "
              ">= %d): which layers carry real signal is now "
              "MEASURED" % ("; ".join(abl_note), ABL_FACTOR,
                            abl_n, len(windows), ABL_MIN_W))

    # ---------------- S4: leg C -- readouts through the model
    section("S4  LEG C -- READOUTS THROUGH THE MODEL")
    plateau_ok = True
    plat_worst_q = 0.0
    plat_worst_t = 0.0
    hrate_ok = True
    hr_note = []
    for kz in windows:
        W = wd[kz]
        N = W["N"]
        test_ns = ([N // 2] if smoke
                   else [N // 2, (3 * N) // 4, N - 1])
        for n in test_ns:
            md = W["mds"][n] if n in W["mds"] else None
            if md is None:
                continue
            gm = md["gam_mod"]
            gt = gam_true[kz].get(n)
            plat_worst_q = max(plat_worst_q, abs(gm - 0.25))
            if gt is not None:
                plat_worst_t = max(plat_worst_t, abs(gm - gt))
                plateau_ok = plateau_ok and (
                    abs(gm - 0.25) <= PLATEAU_ABS
                    and abs(gm - gt) <= PLATEAU_TRUE)
        # h-rate over the free snapshots (n <= N-1)
        hn = [n for n in W["snaps"] if n <= N - 1]
        dh = []
        for n in hn:
            lg10 = float(hlog_true[kz][n][0]) / math.log(10)
            dh.append(W["mds"][n]["hmod_l10"] - lg10)
        sl = (float(np.polyfit(hn, dh, 1)[0]) if len(hn) > 1
              else 0.0)
        hrate_ok = hrate_ok and abs(sl) <= H_RATE_BAR
        hr_note.append("w%d slope %+.4f off %+.2f" % (
            kz, sl, dh[-1]))
    check("G40-base-plateau-adjudicated", True,
          "SEALED RULE: gammahat_n^model = ((b_n - a_n)/4)^2 vs "
          "1/4 (worst dev %.1e, bar %.2f) and vs the true bulk "
          "gammahat (worst dev %.3f, bar %.1f) at the sealed "
          "snapshots: %s -- the model carries the r247 capacity "
          "PLATEAU%s; the eps fluctuation is NOT in the outer "
          "model (r247-consistent, typed)"
          % (plat_worst_q, PLATEAU_ABS, plat_worst_t,
             PLATEAU_TRUE,
             "PASS" if plateau_ok else "FAIL",
             "" if plateau_ok else " -- NOT carried"))
    check("G41-h-rate-adjudicated", True,
          "SEALED RULE: slope of (log10 h^model - log10 h^true) "
          "vs n (rate bar %.2f dec/degree): %s -> %s; the "
          "additive OFFSET is reported UNADJUDICATED (sealed): "
          "it is the norming-constant target of R3"
          % (H_RATE_BAR, "; ".join(hr_note),
             "RATE CARRIED" if hrate_ok else "RATE NOT CARRIED"))
    # fiber
    if smoke:
        vfib = "FIBER_SKIPPED_SMOKE"
        check("G42-fiber-adjudicated", True,
              "SMOKE: fiber block skipped")
    else:
        ratios = []
        signs_ok = True
        fib_note = []
        for kz in FIBER_KZ:
            W = wd[kz]
            p = W["p"]
            dsm = p["dsm"]
            atoms = np.concatenate([dsm["xs"], dsm["ys"]])
            wts = np.concatenate([dsm["ws"], -dsm["vs"]])
            T_true = p["St"] - float(p["S"][FIB_LO - 1])
            Tm, okfin = fiber_T_model(W["mds"][W["N"]],
                                      W["mds"][FIB_LO],
                                      atoms, wts, DPS_FIBER)
            ratio = Tm / T_true
            ratios.append(ratio)
            signs_ok = signs_ok and (Tm > 0) == (T_true > 0) \
                and okfin
            fib_note.append("w%d T_mod %.3g vs T_true %.3f "
                            "(ratio %+.2e)" % (kz, Tm, T_true,
                                               ratio))
        med_ratio = float(np.median(np.abs(ratios)))
        share = float(np.median([abs(1.0 - r) for r in ratios]))
        sp_fib = BH.spearman(ratios,
                             [wd[kz]["N"] for kz in FIBER_KZ])
        if signs_ok and FIB_RATIO_LO <= med_ratio <= FIB_RATIO_HI:
            vfib = "FIBER_IN_ERROR_TERM(share=%.2f)" % share
        else:
            vfib = "FIBER_BEYOND_MODEL"
        check("G42-fiber-adjudicated", True,
              "SEALED RULE result: %s -- %s; median |ratio| "
              "%.2e (window [%.1f, %.1f]), signs %s, N-trend "
              "Spearman(ratio; N) %+.2f (3 points, "
              "informational); honest decade bill: the outer "
              "model %s the budget's magnitude"
              % (vfib, "; ".join(fib_note), med_ratio,
                 FIB_RATIO_LO, FIB_RATIO_HI,
                 "match" if signs_ok else "MISMATCH", sp_fib,
                 "carries" if vfib.startswith("FIBER_IN")
                 else "does NOT carry"))

    # ---------------- S5: leg D -- follow-up spec
    section("S5  LEG D -- FOLLOW-UP SPEC R2-R4 (frozen)")
    print(FOLLOWUP_SPEC, flush=True)
    if not smoke:
        pri = []
        gap_l10 = float(np.median(
            [math.log10(max(errmap[kz][wd[kz]["snaps"][-1]]
                            ["med"]["GAP"], 1e-300))
             for kz in windows]))
        off_med = float(np.median(
            [float(hr.split("off ")[1]) for hr in hr_note]))
        pri.append(("R3", abs(off_med)))
        pri.append(("R2", gap_l10 + 1.0))
        pri.append(("R4", 2.5 if vfib == "FIBER_BEYOND_MODEL"
                    else 0.5))
        pri.sort(key=lambda t: -t[1])
        pri_note = " > ".join(t[0] for t in pri)
    else:
        pri_note = "SMOKE (priority from the full map)"
    check("G50-followup-spec-frozen", True,
          "FOLLOWUP_SPEC frozen, SHA %s (printed above in full); "
          "measured priority order from the map: %s"
          % (FOLLOWUP_SHA[:16], pri_note))

    # ---------------- S6: must-fails
    section("S6  MUST-FAILS")
    W9 = wd[windows[0]]
    n_mf = W9["snaps"][min(1, len(W9["snaps"]) - 1)]
    md_mf = W9["mds"][n_mf]
    snap_mf = errmap[windows[0]][n_mf]["snap"]
    iz_out = 0
    z_out = W9["zs"][iz_out]
    e_hon = err_RI(snap_mf["Y"][iz_out],
                   model_at(md_mf, z_out, dps_m), md_mf["nl"])
    e_m1 = err_RI(snap_mf["Y"][iz_out],
                  model_at(md_mf, z_out, dps_m, variant="m1"),
                  md_mf["nl"])
    ok_m1 = e_m1 >= 1e3 * max(e_hon, 1e-300)
    # m2: the naive principal sqrt flips the sign of R(z) on the
    # LEFT real axis, so D(-inf) != Dinf and the FIK normalization
    # breaks at the left norm point (structure-pinned, loud)
    zL = [W9["x0"] - NORM_OFFS[0], W9["x0"] - NORM_OFFS[1]]
    _mA, dev_honL = rich_M1_12(md_mf, n_mf, zL, dps_m)
    _mB, dev_m2L = rich_M1_12(md_mf, n_mf, zL, dps_m,
                              variant="m2")
    e_hon_a = dev_honL[0]
    e_m2 = dev_m2L[0]
    ok_m2 = e_m2 >= M2_RATIO_BAR * max(e_hon_a, 1e-300)
    # m3: mass-deficit normalization break
    n_lo = max(nn for nn in W9["mds"] if nn < n_mf) \
        if any(nn < n_mf for nn in W9["mds"]) else None
    if n_lo is None:
        ok_m3 = True
        m3_note = "no lower mass available (smoke)"
    else:
        _m1a, dev_hon = rich_M1_12(md_mf, n_mf, W9["norm_z"],
                                   dps_m)
        _m1b, dev_bad = rich_M1_12(W9["mds"][n_lo], n_mf,
                                   W9["norm_z"], dps_m)
        ok_m3 = dev_bad[0] >= 100.0 * max(dev_hon[0], 1e-300)
        m3_note = ("normalization dev %.1e (mass %d as %d) vs "
                   "honest %.1e" % (dev_bad[0], n_lo, n_mf,
                                    dev_hon[0]))
    check("G60-must-fails-fire", ok_m1 and ok_m2 and ok_m3,
          "m1 swapped sigma3: OUT err %.2e vs honest %.2e "
          "(>= 1e3 x, LOUD); m2 wrong R branch at the LEFT norm "
          "point (sign of R flips, D(-inf) != Dinf): "
          "normalization dev %.2e vs honest %.2e (ratio %.1f, "
          "bar %.1f); m3 mass deficit: %s "
          "(>= 100 "
          "x); m4 sign oracle: reading sign h or flip degrees "
          "hits every window trivially and is EXCLUDED by the "
          "input firewall (standing r243 exclusion)"
          % (e_m1, e_hon, e_m2, e_hon_a,
             e_m2 / max(e_hon_a, 1e-300), M2_RATIO_BAR, m3_note))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    base_carried = plateau_ok and hrate_ok
    lvl_ok = all(bulk_at_N[kz] <= ERR_LEVEL_BAR for kz in windows)
    bnd_ok = all(bulk_at_N[kz] <= ERR_BOUND_BAR for kz in windows)
    if smoke:
        vA = "SMOKE_NO_ADJUDICATION"
    elif (decay_n >= DECAY_MIN_W and lvl_ok and base_carried):
        vA = "OUTER_MODEL_CARRIES_BULK"
    elif base_carried and bnd_ok and abl_n >= ABL_MIN_W:
        vA = "OUTER_MODEL_PARTIAL"
    else:
        vA = "OUTER_MODEL_FAILS"
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (an opening "
          "measurement moves no edge); what the round adds: the "
          "first global outer-model candidate in the exact FIK "
          "normalization (g from the r232a constrained "
          "equilibrium, ell from the KKT midpoint, discrete "
          "Szego D with the -2 pi i residue calibration), its "
          "frozen error map, the base/fiber readout bill, and "
          "the localized R2-R4 spec")
    verd = "%s + %s + ERROR_MAP_FROZEN%s" % (
        vA, vfib if not smoke else "FIBER_SKIPPED_SMOKE", wb_mod)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G81-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the error map (bulk err, N-trend, "
          "band breaks, world offsets, ablation), the h decade "
          "bill (rate vs offset), the fiber decade bill; PROVEN "
          "(wards): model algebra, FIK normalization, toy "
          "anchor, det Y; OPEN: the budget bound and the base "
          "law themselves (r243/r247 stand); NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s   "
          "FOLLOWUP_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16], FOLLOWUP_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
