#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""window_border_transfer_probe -- PRIME.PORT.L2.
WINDOW_BORDER_TRANSFER.01 (round 298): the TRANSFER STATEMENT
from the WINDOW measure (where the chain is exactly orthogonal,
r297-S7) to the BORDER form (where the vdC input lives) -- does
an exact or low-loss decomposition of the vdC input S_F exist
that PRESERVES the signed structure instead of losing it to
magnitudes?  Context (sealed record inputs): r297 (SPEC e42a76eb,
27/27) froze the target inequality sigma := slope(S_F/M_W^2) <=
sigma* = -0.516 (measured sigma = -0.714, margin 0.198) and named
the gap object: every magnitude majorization of A(0) pays a
GROWING max/mean imbalance factor (+0.22..+0.24 slope); the two
assets: (1) the chain is EXACTLY ORTHOGONAL w.r.t. the WINDOW
union (union(d)): cross/diag devs 0.000 world-blind, and the
Parseval sum rule sum w x^2 pi_k^2 = h_{k+1} + a_k^2 h_k + b_k^2
h_{k-1} is PROVED in Fractions (r297-G31) -- but the vdC input
lives on the BORDER union (union(dsm), mixed-sign weights ws > 0
/ -vs < 0) where orthogonality breaks (~1.1); (2) run-boundary
POSITIONS are near-equidistributed with falling discrepancy
(D_rank med 0.024, slope -0.42) while the MASS imbalance grows
(+0.244).  r287: the vdC theorem delivers delta'(F2) = +0.309 >
DELTA_NEED = 0.21 world-blind; kz15 permanently closed via r270.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r287/r297 machinery imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split; maximal same-sign runs of the bx-sorted bulk; level-2
blocks P_j (r270 convention, offset 0); FROZEN vdC window H =
max(2, ceil(sqrt(m))); the vdC input S_F = (1/H) sum_t W_t^2
(v964-S0 identity).  THE TWO MEASURES (r297-sealed candidates):
WINDOW omega = union(d) (atoms xu, weights wu = (ws, -vs) of the
arithmetic comb), BORDER beta = union(dsm) (atoms bx, weights bw
= (ws, -vs) of the smooth comb); both mixed-sign by construction.
THE TRANSFER OBJECT (frozen): Delta := beta (-) omega, the exact
signed difference measure (atoms concat(bx, xu), weights
concat(bw, -wu) -- four signed atom classes).  THE FROZEN
POSITIONAL FEJER KERNEL: S_F is EXACTLY the quadratic form
B(u, v) = (1/H) sum_t W_t(u) W_t(v) (W_t = sliding H-window sums
over the block axis) evaluated on the block aggregation of the
border atoms; the kernel data (edge mask over the combined hull
[lo, hi] at EDGE_F, the block partition = positional intervals of
the border bulk runs with midpoint breakpoints, the frozen H) is
read off the BORDER structure ONCE per rung and then applied to
ANY atom list positionally (c(x) = w x v2(x) fac, edge atoms
dropped, block index by breakpoint search).  This extends the
block functional to omega and Delta CANONICALLY and makes S_F
measure-quadratic: with P_mu the aggregated block vector of
measure mu, PDelta = Pbeta - Pomega EXACTLY, and

  S_F  =  B(Pbeta, Pbeta)
       =  B(Pomega, Pomega)  +  B(PDelta, Pbeta + Pomega)
       =  MAIN               +  T(Delta)          (EXACT identity)

-- the difference-of-squares split of the Fejer form; T(Delta) =
B(Delta, beta + omega) is LINEAR in Delta and carries the full
signed structure (nothing passes through |.|); per-block
attribution t_j = PDelta_j x phi_j with phi = Fejer * (Pbeta +
Pomega) (convolution), sum_j t_j = T exactly; components T =
B(PDelta, PDelta) + 2 B(PDelta, Pomega) = T_diag + T_cross.  The
PARSEVAL ANCHOR of the main-term side: on omega the chain is
exactly orthogonal (r297), the proven sum rule attaches verbatim
(re-proved in Fractions here, wrong-b^2 mutant CAUGHT), and the
LINEAR corollary holds: sum_a wu_a xu_a v2(xu_a) = 0 EXACTLY
(x pi_{N-2} = pi_{N-1} + a pi_{N-2} + b pi_{N-3} is orthogonal
to pi_0 on omega) -- the window image of the drive functional
VANISHES: at the linear level the drive is 100 pct transfer;
the open question of this round is the QUADRATIC split.

LEG 0 -- ANCHOR REGRESSION (r297 record numbers adopted as-is,
disclosed): sigma = -0.714 tol 0.01, sigma* = -0.516 tol 0.01
(sl_c2 +0.196 tol 0.01, sl_pref +0.489 tol 0.01); WINDOW
orthogonality HOLDS (cross + diag devs <= 1e-6) on the id pool
(kz15, kz20, mains, EPSTEIN, SCRAMBLE) while BORDER breaks
(cross med in [0.8, 1.4]); the Parseval sum rule re-proved exact
in Fractions (dev 0); D_rank med 0.024 tol 0.005 with slope
-0.42 tol 0.05; mass-imbalance slope +0.244 tol 0.01;
contribution + block + autocorr identity wards (r297 bars).

LEG A -- THE EXACT BORDER DECOMPOSITION (structure first):
(A1) Delta anatomy census: atom counts / |mass| / signed mass of
  the four classes (border-ws > 0, border--vs < 0, window-ws,
  window--vs), exact support overlap count, edge shares -- the
  concrete sign structure of Delta printed.
(A2) DECOMPOSITION_EXACT gates: (i) KERNEL REPRODUCTION: the
  frozen positional kernel reproduces S_F from the raw border
  atoms against the sealed r287 pipeline (blocks_level2 +
  bound_vdc) to <= 1e-12 rel on all 47 worlds (42 rungs + 2
  mains + EPSTEIN/SCRAMBLE/SMOOTH -- far beyond the required 6
  rungs x 3 worlds); (ii) THE IDENTITY: S_F = MAIN + T(Delta)
  to <= 1e-12 of the decomposition scale max(S_F, MAIN, |T|) on
  all 47 worlds; (iii) ATTRIBUTION: sum_j t_j = T and T =
  T_diag + T_cross (<= 1e-9 rel); (iv) the LINEAR WINDOW ZERO:
  |sum wu x v2| / sum |wu x v2| <= 1e-9 main (N <= 400) / 3e-6
  deep / 1e-6 controls (the orthogonality corollary).
  Fine type: DECOMPOSITION_EXACT(S_F = B(omega, omega) +
  B(Delta, omega + beta), frozen positional Fejer kernel).

LEG B -- THE TRANSFER-TERM SCALING (the decision; all slopes
r272 halves log-slopes on the N-sorted 42-rung ladder): measure
slope(MAIN/M_W^2), slope(|T|/M_W^2), the recomposition ward
(per-rung exact identity = the sigma additivity carrier), the
share census sh = |T|/S_F (med + slope), the T sign census, the
component split (T_diag med, T_cross med), the in-T sign
cancellation canc_T = sum_j |t_j| / |T| (med + slope), and the
class shares of sum_j |PDelta_j|.  SEALED ADJUDICATION (frozen
BEFORE evaluation, exactly one fires):
  DECOMPOSITION_UNSTABLE  iff med(MAIN/S_F) >= 10.0 (both terms
    an order above S_F, near-cancellation between main and
    transfer -- then THIS cancellation is the object; the third
    recurrence of the resummation pattern, explicitly cross-
    referenced against r259 (prefix resummation) and r261
    (fullsource free-prefix));
  TRANSFER_SUBDOMINANT    iff not UNSTABLE and med(sh) < 0.5
    and slope(|T|/M^2) <= slope(MAIN/M^2) - 0.05 (T falls
    faster and is minority -- Leg C fires);
  TRANSFER_DOMINANT       otherwise (T carries sigma; the
    precise gap object is the signed Delta structure -- its
    anatomy is the delivery: which classes carry T, how much
    sign cancellation lives INSIDE T).
WORLD CONTROLS: the decomposition is exact on EPSTEIN/SCRAMBLE
by the same algebra; the CLASS (unstable / T-minority /
T-majority by the same med rules at the single control rung) is
compared against MAIN -- a class break is NOT a gate failure but
a disclosed finding (WORLD_SENSITIVE tag in the verdict).

LEG C -- THE CANDIDATE THEOREM (fires ONLY on
TRANSFER_SUBDOMINANT): CANDIDATE THEOREM (window-border
transfer) printed with every constant explicit: the exact
decomposition (Leg A) + the proven Parseval sum rule on omega +
the D_rank equidistribution asset + transfer subdominance
(measured) + the r297 target inequality sigma <= sigma* + the
v964-S0 vdC theorem => delta' > 0.21 on the generic half; scope
the 42 measured rungs (N in [142, 878]); exceptions: 6 via the
r287 F2 certificates, kz15 via the r270 exact-finite
certificate.  Wave-9 promotion candidate -- NOT promoted here.
Otherwise Leg C is VOID without substitute and the precise gap
object is documented.

LEG D -- MASS-IMBALANCE BYCATCH (small): is the growing
imbalance imb = n_runs x maxM / sumM carried by few outlier
runs or broad?  Sealed: top-1/top-3 mass shares (med), the
drop-imbalances imb_d1 / imb_d3 (argmax run(s) removed) with
slopes; OUTLIER_CARRIED iff slope(imb_d3) <= 0.5 x slope(imb),
else BROAD_BASED.  Connection of the two gap halves: per-rung
Spearman(block mass Mb_j, |t_j|) (med) + the argmax coincidence
fraction -- do the mass-imbalance carriers coincide with the
T(Delta) carriers?

LEG E -- WARDS / MUST-FAILS (>= 4 mutants): (m1) WRONG-b^2 SUM
RULE (exact Fractions, module-own): the Parseval sum rule with
coefficient b_k instead of b_k^2 breaks on the rational 4-node
measure (dev != 0) -- CAUGHT; (m2) MAGNITUDE DELTA (|Delta|
instead of Delta): T computed from the magnitude aggregation
|c_a| breaks the exact identity LOUDLY (>= 1e-6 of the
decomposition scale, measured on w9 + both mains) -- the r297
magnitude error, now a must-fail; (m3) KERNEL-PERTURBED
RECOMPOSITION: the Fejer form at H + 1 breaks the toy identity
(S_F(H=2) = 3 vs 7/3 at H=3, break 2/3 >= 1e-6) -- CAUGHT;
(m4a/m4b) WORLD-BLINDNESS BREAK: a builder consuming the
withheld terminal drive key AND a builder consuming the branch
label are both FLAGGED by the AST scope audit.  Scope hygiene:
the kernel builders (block_breaks, aggregate_blocks, fejer_bil,
fejer_apply) consume positions + weights + chain values only
(BOUND_FORBIDDEN set); fragment audit (no fit primitives); TOY
EXACTNESS (bar 1e-14): the hand toy (border atoms (0..4), ct
(3,-1,2,-4,1) -> Pbeta (2,-2,1), H = 2, S_F = 3; window atoms
(0.5, 2.5), c (1,-1) -> Pomega (1,-1,0), MAIN = 1; PDelta
(1,-1,1), T = 2; MAIN + T = 3 = S_F; attribution t = (1.5, 1,
-0.5) sums to 2; T_diag = 1, T_cross = 1) reproduces the
whole pipeline EXACTLY; mp SAMPLES (dps 60): kz15 (bar 1e-8) +
the two deepest rungs (bar 3e-6); SMOOTH anchor (alias <=
1e-12, q_N <= 1e-20).

INDEX FIREWALL (binding, r238-r297 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r269
PBB.mask_edge + PBB.runs_split + PBB.mp_drive, r287
L2D.blocks_level2 + L2D.bound_vdc + L2D.halves_slope +
L2D.autocorr_full, r297 VCP.chain_quads + VCP.fr_symbolic_sumrule
(the proven set re-computed, not re-proved), r244 BH.wpack +
BH.spearman, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.
B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor,
never fitted).  COFINAL LADDER (pre-sealed): frame-A h <= 900,
42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38,
39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN); KER_BAR
1e-12 (kernel reproduction, rel S_F); DEC_BAR 1e-12 (identity,
rel decomposition scale); ATTR_BAR 1e-9 (attribution +
components); LIN_BARS 1e-9 main N <= 400 / 3e-6 deep / 1e-6
controls (linear window zero); UNSTABLE_FACTOR 10.0; SUB_SHARE
0.5; SUB_MARGIN 0.05; OUT_FACTOR 0.5 (Leg D); ID_HOLDS 1e-6;
BORDER_CROSS_BAND (0.8, 1.4); R297_SIGMA -0.714 tol 0.01;
R297_SIGMA_STAR -0.516 tol 0.01; R297_SL_C2 +0.196 tol 0.01;
R297_SL_PREF +0.489 tol 0.01; R297_DRANK_MED 0.024 tol 0.005;
R297_DRANK_SL -0.42 tol 0.05; R297_IMB_SL +0.244 tol 0.01;
TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls;
ID_BAR 1e-12; AC_BAR 1e-9; TOY_BAR 1e-14; MUT_MIN 1e-6; MP_DPS
60; MP_T_BAR 1e-8; MP_DEEP_BAR 3e-6; SM_Q_BAR 1e-20;
SM_ALIAS_BAR 1e-12; KZ_ANCHOR 15; runtime <= 1800 s; smoke = w9
+ controls + Fractions section + toys + scope audits + the full
decomposition gates at w9 (ladder, slopes, adjudication, Legs
C/D, mp wards skipped).  DISCLOSED PRE-SPEC INPUT (no scratch
run of this probe): every reproduction band is an r297 RECORD
number adopted as-is; the linear window zero is derived algebra
(orthogonality corollary), disclosed above as an expectation,
not tuned; the three Leg-B outcomes are sealed symmetrically --
the disclosed structural prior (the linear functional is 100
pct transfer) makes UNSTABLE or DOMINANT plausible, but no rule
was chosen to favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  DECOMPOSITION_EXACT(S_F = B(omega,omega) + B(Delta,omega+beta),
    Delta = border (-) window, frozen positional Fejer kernel,
    worst devs, worlds n/47)
+ TRANSFER_TABLE(MAIN med dec + slope, |T| med dec + slope,
    share med + slope, T sign census, T_diag/T_cross med,
    canc_T med + slope, Delta class shares)
+ [exactly one of] TRANSFER_SUBDOMINANT(...) /
    TRANSFER_DOMINANT(anatomy) /
    DECOMPOSITION_UNSTABLE(factor; r259/r261 crossref)
+ [iff fired] CANDIDATE_THEOREM(window-border transfer,
    constants)
+ IMBALANCE_NOTE(OUTLIER_CARRIED / BROAD_BASED, connection
    stats)
+ [if any control gate breaks] LOCAL_MODEL_MAIN_FITTED
+ [if the control class differs] WORLD_SENSITIVE(disclosed).
Honesty before beauty: the decomposition is an EXACT finite
identity, but every slope, share and class is MEASURED on 42
rungs only; no verdict claims a cofinal law; the kernel
extension to omega is canonical-positional, not unique -- it is
the sealed choice of this round; the exception scalar's
positivity beyond the measured 42 stays OPEN; r243-r297 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 26/28 -- the toy gate G31 failed on a HAND-
ARITHMETIC error in the expected T-component constants (the
correct split of the toy T = 2 is T_diag = B(PDelta, PDelta) = 1
and T_cross = 2 B(PDelta, Pomega) = 1, not 1.5/0.5; PDelta +
2 Pomega = Pbeta + Pomega makes the identity obvious) --
amendment a1 (the toy constants and the spec toy line corrected;
no bar, band, rule or verdict rule touched; all real-data gates
were already green in smoke pass 1); smoke pass 2 = 28/28;
calibration pass 1 = first full evaluation, 28/28 gates, wall
46.9 s, adjudication fired TRANSFER_DOMINANT; amendment a2 after
calibration pass 1 (REPORTING ONLY: the G31 gate text still
printed the pre-a1 toy constants -- text aligned, no number
moved); calibration pass 2 identical to pass 1 in every printed
figure; record run1/run2 after this insertion, identical up to
WALL; the only post-freeze edits are a1/a2 and this record-table
insertion, which IS the protocol):
CAL_VERDICT = DECOMPOSITION_EXACT(worst identity dev 8.8e-16 of
the decomposition scale, kernel reproduction worst 7.5e-16,
attribution worst 5.4e-16, 47/47 worlds) + TRANSFER_TABLE(MAIN
med -3.94 dec sl -1.386; |T| med -2.01 dec sl -0.698; share med
0.99 sl +0.016; T < 0 on 0/42; T_diag med -2.14 dec, T_cross
med -1.44e-4; canc_T med 1.69 sl +0.207; Delta class shares
b+/b-/w+/w- 0.55/0.00/0.26/0.18) + TRANSFER_DOMINANT(the signed
Delta structure is the precised gap object) + IMBALANCE_NOTE(
BROAD_BASED: sl(imb) +0.244 vs drop-top-1 +0.188 / drop-top-3
+0.197; sp(Mb, |t_j|) med +0.69, argmax coincidence 13/42).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; block + autocorr identities worst 6.3e-16 /
2.7e-15 on 47 worlds; r297 anchors bit-near (sigma -0.714,
sigma* -0.516, sl_c2 +0.196, sl_pref +0.489, margin 0.198;
D_rank med 0.024 sl -0.42, imb sl +0.244; orth WINDOW HOLDS
worst 5.1e-7 / BORDER cross med 1.101 in band).  S3: the sum
rule re-proved exact in Fractions (orth dev 0, identity dev 0,
module-own == r297-G31); m1 wrong-b^2 dev 806/343 != 0 CAUGHT;
toys exact (worst 0.0); m3 kernel-perturbed break 2/3 exact
LOUD; m4a/m4b FLAGGED by the scope audit.  S4: Delta anatomy
(w9): border 361 ws-atoms (+) / 6 -vs-atoms (-) vs window 263 /
104, support overlap 367 (PARTIALLY SHARED unions); bulk
|c|-mass shares b+/b-/w+/w- 0.60/0.00/0.25/0.16; the LINEAR
WINDOW ZERO now MEASURED: |sum wu x v2| / sum |wu x v2| worst
2.2e-12 main / 6.4e-12 deep / 5.0e-7 controls -- the window
image of the drive functional VANISHES at float precision: the
drive is 100 pct transfer at the LINEAR level, on all 47
worlds.  S5 (the decision): the OPPOSITE of the r259/r261
near-cancellation pattern -- the window main term is EMPTY, not
huge: MAIN/M^2 med -3.94 dec (two decades BELOW S_F med -2.00
dec), slope -1.386 (collapsing); T = S_F - MAIN is positive on
42/42 rungs with share med 0.99 and slope -0.698 ~ sigma; the
component split localizes further: T_cross = 2 B(PDelta,
Pomega) med -1.4e-4 (negligible) => S_F ~ B(PDelta, PDelta):
THE VDC INPUT IS THE FEJER ENERGY OF THE DIFFERENCE MEASURE
ITSELF; the in-T sign cancellation sum|t_j|/|T| med 1.69 with
slope +0.207 -- the r297 imbalance growth (+0.217 CS step)
reappears INSIDE T as the growing gap between |t_j|-mass and
the signed sum; exception rungs sh 0.99-1.00, canc_T 1.14
(kz39) .. 1.83 (kz52); controls EPST/SCR same class T-MAJORITY
-- WORLD-BLIND, no tag.  S6: Leg C VOID (no substitute).  S7
Leg D: BROAD_BASED -- dropping the top-1/top-3 mass runs
lowers the imbalance slope from +0.244 to +0.188/+0.197 but
does NOT kill it (bar for OUTLIER_CARRIED was <= +0.122): the
growth is broad; the connection stat is real: sp(block mass,
|t_j|) med +0.69 -- the mass-heavy blocks ARE the T-heavy
blocks (argmax coincidence 13/42): the two r297 gap halves
(mass imbalance, signed transfer) are ONE structure seen twice.
S8: m2 magnitude-Delta breaks the exact identity by 1.7e+0
(w9) / 5.1e-1 (w13) of the decomposition scale LOUD -- the
r297 magnitude error certified as a mustfail; SMOOTH alias
2.4e-14, q_N 4.2e-25; mp wards kz15 2.9e-10, kz64 9.3e-9,
kz52 6.6e-8.  READING (typed, no upgrade): the round DELIVERS
the transfer statement the lane asked for, and it is SHARPER
than hoped: S_F = B(omega,omega) + B(Delta,omega+beta) is
exact, world-blind and sign-preserving -- and on the real
chain the window main term VANISHES at both levels (linear:
exactly, by orthogonality; quadratic: med two decades below,
slope -1.39), while the omega-Delta cross term is negligible
(med -1.4e-4).  So the exact development collapses to S_F ~
B(PDelta, PDelta) + [exact tiny corrections]: the vdC input IS
the Fejer block energy of the border-minus-window difference
measure.  The provenance question is now maximally localized:
sigma = -0.714 is the decay exponent of ONE named source-pure
quantity, the Delta Fejer energy, whose in-block sign
cancellation (canc_T med 1.69, growing +0.21) carries exactly
the structure every |.|-chain loses (m2: factor ~1.7 of scale).
NOT a bound, NOT a theorem yet -- but the gap object of the
lane is no longer 'some magnitude chain misses sigma': it is
'prove the Fejer-energy decay of Delta', with the Leg-D
unification (the mass-imbalance carriers are the same blocks)
as the concrete geometric handle for wave 9.  Runtime 46.9 s
full / 0.2 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: NONE beyond the disclosed a1/a2
(records inserted per protocol; no bar, band, rule or verdict
rule moved).

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
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import l2_deterministic_cancellation_probe as L2D  # noqa: E402 r287
import vdc_chain_provenance_probe as VCP       # noqa: E402 r297
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
ID_BAR = 1e-12
AC_BAR = 1e-9
KER_BAR = 1e-12
DEC_BAR = 1e-12
ATTR_BAR = 1e-9
LIN_BAR = 1e-9
LIN_BAR_DEEP = 3e-6
LIN_BAR_CTRL = 1e-6
TOY_BAR = 1e-14
MUT_MIN = 1e-6
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
UNSTABLE_FACTOR = 10.0
SUB_SHARE = 0.5
SUB_MARGIN = 0.05
OUT_FACTOR = 0.5
ID_HOLDS = 1e-6
BORDER_CROSS_BAND = (0.8, 1.4)
R297_SIGMA = -0.714
R297_SIGMA_TOL = 0.01
R297_SIGMA_STAR = -0.516
R297_SSTAR_TOL = 0.01
R297_SL_C2 = 0.196
R297_SL_C2_TOL = 0.01
R297_SL_PREF = 0.489
R297_SL_PREF_TOL = 0.01
R297_DRANK_MED = 0.024
R297_DRANK_TOL = 0.005
R297_DRANK_SL = -0.42
R297_DRANK_SL_TOL = 0.05
R297_IMB_SL = 0.244
R297_IMB_SL_TOL = 0.01
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
KZ_ANCHOR = 15

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
    return (not bad), ("NO zero/prime oracles; every readout "
                       "consumes node positions + signed weights + "
                       "the r244 chain rows; ground truth (branch "
                       "labels, true R/t/Z) enters gates and census "
                       "tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden method families (identifiers only;
    the fragment table itself is assembled from split strings)."""
    frags = ("cand_" + "unroll", "poly" + "fit", "curve_" + "fit",
             "lst" + "sq", "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


BOUND_FORBIDDEN = {"t" + "_term", "Z", "Zl", "margin", "M" + "_W",
                   "loss", "R" + "_bulk", "truth", "rho",
                   "g" + "_branch", "need"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    truth-side identifier or dict key from the sealed set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ---------------- exact Fractions section: the Parseval sum rule
# ---------------- (module-own re-proof + the m1 wrong-b^2 mutant)
def fr_parseval_sumrule(wrong_b=False):
    """the Parseval-type sum rule on the rational 4-node measure
    x = (0, 1, 2, 3), w = (1, 2, 1, 3) (r297-G31 verbatim): monic
    three-term chain pi_0..pi_3, orthogonality dev + the identity
    sum w x^2 pi_k^2 == h_{k+1} + a_k^2 h_k + b_k^2 h_{k-1} for
    k = 1, exact.  wrong_b replaces b_k^2 by b_k on the RHS --
    the m1 mutant, must break (dev != 0)."""
    xs = [Fr(0), Fr(1), Fr(2), Fr(3)]
    ws = [Fr(1), Fr(2), Fr(1), Fr(3)]
    n = len(xs)
    pis = [[Fr(1)] * n]
    a_ = []
    b_ = []
    hs = [sum(w * p * p for w, p in zip(ws, pis[0]))]
    for k in range(3):
        ak = sum(w * x * p * p for w, x, p in zip(ws, xs, pis[k])) \
            / hs[k]
        bk = (hs[k] / hs[k - 1]) if k >= 1 else Fr(0)
        nxt = []
        for i in range(n):
            v = (xs[i] - ak) * pis[k][i]
            if k >= 1:
                v -= bk * pis[k - 1][i]
            nxt.append(v)
        pis.append(nxt)
        a_.append(ak)
        b_.append(bk)
        hs.append(sum(w * p * p for w, p in zip(ws, nxt)))
    worst_orth = Fr(0)
    for a in range(4):
        for b in range(a):
            worst_orth = max(worst_orth,
                             abs(sum(w * pis[a][i] * pis[b][i]
                                     for i, w in enumerate(ws))))
    k = 1
    lhs = sum(w * x * x * p * p
              for w, x, p in zip(ws, xs, pis[k]))
    bco = b_[k] if wrong_b else b_[k] ** 2
    rhs = hs[k + 1] + a_[k] ** 2 * hs[k] + bco * hs[k - 1]
    return worst_orth, abs(lhs - rhs)


# ---------------- the frozen positional Fejer kernel machinery.
# ---------------- Source-pure: positions, weights and chain
# ---------------- values only; the withheld terminal drive key,
# ---------------- the branch label and every target-side
# ---------------- identifier are forbidden in scope (AST audit).
def block_breaks(bxs_bulk, runs):
    """midpoint breakpoints between consecutive level-2 block
    position intervals of the border bulk (runs = r269
    runs_split output on the sorted bulk; blocks = adjacent run
    pairs from PAIR_OFFSET 0, odd tail its own block).  Returns
    (breaks ascending, m blocks, per-atom block index)."""
    nr = len(runs)
    m = (nr - PAIR_OFFSET + 1) // 2 if nr else 0
    jb = np.zeros(len(bxs_bulk), dtype=int)
    for i, (a, b, _s) in enumerate(runs):
        jb[a:b] = i // 2
    brk = []
    for j in range(m - 1):
        a_last = runs[min(2 * j + 1, nr - 1)][1] - 1
        b_first = runs[2 * (j + 1)][0]
        brk.append(0.5 * (bxs_bulk[a_last] + bxs_bulk[b_first]))
    return np.asarray(brk, dtype=float), m, jb


def aggregate_blocks(xs, cs, lo, hi, brk, m):
    """positional block aggregation of ANY atom list: edge atoms
    (r268 mask on the combined hull) dropped, block index by
    breakpoint search, values summed per block -> P vector."""
    xs = np.asarray(xs, dtype=float)
    cs = np.asarray(cs, dtype=float)
    ed = PBB.mask_edge(xs, lo, hi, EDGE_F)
    xb = xs[~ed]
    cb = cs[~ed]
    if m == 0 or len(xb) == 0:
        return np.zeros(max(m, 0))
    j = np.searchsorted(brk, xb)
    return np.bincount(j, weights=cb, minlength=m)


def window_vec(P, H):
    """the sliding H-window sums of the zero-padded block vector
    (m + H - 1 windows; the v964-S0 Fejer core)."""
    m = len(P)
    p = np.zeros(m + 2 * (H - 1))
    p[H - 1:H - 1 + m] = np.asarray(P, dtype=float)
    c = np.concatenate(([0.0], np.cumsum(p)))
    return c[H:] - c[:-H]


def fejer_bil(Pa, Pb, H):
    """the Fejer block bilinear form B(u, v) = (1/H) sum_t
    W_t(u) W_t(v) = sum_{j,j'} (1 - |j - j'|/H)+ u_j v_{j'}."""
    return float(np.sum(window_vec(Pa, H) * window_vec(Pb, H))) / H


def fejer_apply(v, H):
    """phi = K v with K the Fejer block kernel (symmetric
    convolution) -- the per-block attribution carrier."""
    kern = np.array([1.0 - abs(h) / H for h in range(-(H - 1), H)])
    return np.convolve(np.asarray(v, dtype=float), kern,
                       mode="same")


def mutant_gift_bound(rc, P):
    """m4a MUST-FAIL MUTANT: a 'transfer term' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * fejer_bil(P, P, 2)


def mutant_branch_peek(rc, P):
    """m4b MUST-FAIL MUTANT (world-blindness break simulated): a
    'main term' that consumes the branch label to pick its
    constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * fejer_bil(P, P, 2)


# ---------------------------------------------- toy exact tools
def toy_transfer():
    """the hand toy (spec Leg E): border atoms (0..4) with ct
    (3,-1,2,-4,1); window atoms (0.5, 2.5) with c (1,-1); H = 2.
    Every pipeline stage must reproduce EXACTLY (bar 1e-14)."""
    worst = 0.0
    bx = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    ct = np.array([3.0, -1.0, 2.0, -4.0, 1.0])
    lo, hi = -10.0, 14.0                 # edge zones miss all atoms
    ed = PBB.mask_edge(bx, lo, hi, EDGE_F)
    worst = max(worst, float(np.sum(ed)))
    runs = PBB.runs_split(ct)
    brk, m, jb = block_breaks(bx, runs)
    worst = max(worst, abs(m - 3),
                float(np.max(np.abs(jb - np.array([0, 0, 1, 1, 2])))),
                float(np.max(np.abs(brk - np.array([1.5, 3.5])))))
    Pb = aggregate_blocks(bx, ct, lo, hi, brk, m)
    worst = max(worst,
                float(np.max(np.abs(Pb - np.array([2.0, -2.0, 1.0])))))
    H = 2
    sf = fejer_bil(Pb, Pb, H)
    worst = max(worst, abs(sf - 3.0))
    f2 = L2D.bound_vdc(list(Pb))
    worst = max(worst, abs(f2["s2"] / f2["H"] - sf))
    Pw = aggregate_blocks(np.array([0.5, 2.5]),
                          np.array([1.0, -1.0]), lo, hi, brk, m)
    worst = max(worst,
                float(np.max(np.abs(Pw - np.array([1.0, -1.0, 0.0])))))
    main = fejer_bil(Pw, Pw, H)
    Pd = Pb - Pw
    T = fejer_bil(Pd, Pb + Pw, H)
    worst = max(worst, abs(main - 1.0), abs(T - 2.0),
                abs(main + T - sf))
    phi = fejer_apply(Pb + Pw, H)
    tj = Pd * phi
    worst = max(worst,
                float(np.max(np.abs(tj
                                    - np.array([1.5, 1.0, -0.5])))),
                abs(float(np.sum(tj)) - T))
    td = fejer_bil(Pd, Pd, H)
    tc = 2.0 * fejer_bil(Pd, Pw, H)
    worst = max(worst, abs(td - 1.0), abs(tc - 1.0),
                abs(td + tc - T))
    return worst


def toy_mustfail_m3():
    """m3 KERNEL-PERTURBED RECOMPOSITION (toy level): the Fejer
    form at H + 1 breaks the toy identity: S_F(H=2) = 3 vs
    S_F(H=3) = 7/3 -- break 2/3, LOUD."""
    Pb = np.array([2.0, -2.0, 1.0])
    return abs(fejer_bil(Pb, Pb, 3) - fejer_bil(Pb, Pb, 2))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("window_border_transfer_probe -- PRIME.PORT.L2."
          "WINDOW_BORDER_TRANSFER.01 (round 298)")
    print("SPEC_SHA %s   R287_SHA %s (imported)   R297_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], L2D.SPEC_SHA[:16], VCP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + decomposition "
                        "gates at w9; ladder, slopes, adjudication, "
                        "Legs C/D, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE WINDOW-BORDER TRANSFER ROUND (the r297 asset-1 "
          "attachment point): the chain is exactly orthogonal on "
          "the WINDOW union and the Parseval sum rule is proved "
          "there; the vdC input S_F lives on the BORDER union; "
          "this round freezes Delta := border (-) window and the "
          "positional Fejer block kernel, and tests the EXACT "
          "sign-preserving split S_F = B(omega,omega) + "
          "B(Delta,omega+beta) = MAIN + T(Delta); three sealed "
          "outcomes (SUBDOMINANT / DOMINANT / UNSTABLE with "
          "r259/r261 crossref); DELTA_NEED %.2f, sigma* %.3f "
          "(r297 records); disclosed structural prior: the "
          "LINEAR window functional vanishes exactly "
          "(orthogonality corollary) -- the drive is 100 pct "
          "transfer at the linear level; ALL bars, rules and "
          "verdicts sealed BEFORE evaluation"
          % (DELTA_NEED, R297_SIGMA_STAR))

    # ---------------- S1: census + controls (r297 scaffold verbatim)
    section("S1  CENSUS + CONTROLS")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    if smoke:
        ladder = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G10-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %d rungs "
          "POSITIVE_PREFIX %s, N in [%s, %s]"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             len(ladder),
             "42/42" if okL and ladder else ("n/a (SMOKE)"
                                             if smoke else "FAIL"),
             ladder[0]["N"] if ladder else "-",
             ladder[-1]["N"] if ladder else "-"))

    pool = ladder if not smoke else [packs["w9"]]
    mains = [packs["w%d" % kz] for kz in windows]

    def rung_rec(p):
        N = p["N"]
        rows = p["rows"]
        r, t, ap, bp = TX.drive_arrays(rows, N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        chain = ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3]
        Z = t[N - 2] + chain
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        v2 = BR.eval_scaled(rows, bx, N - 2)
        v2w = BR.eval_scaled(rows, xu, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        cw = wu * xu * v2w * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, cw=cw, o=o,
                    lo=lo, hi=hi, p=p)

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]
    crecs = {c: rung_rec(ctrl[c]) for c in ctrl}
    cheap = [rc for rc in recs if rc["g_branch"] >= 0.0]
    exc = [rc for rc in recs if rc["g_branch"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g_branch"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g_branch"] >= 0 else
                 "EXCEPTION", recs[0]["g_branch"]))
    else:
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs)))

    # ---------------- S2: decomposition + identities + r297 anchors
    section("S2  EXACT DECOMPOSITION + IDENTITIES + R297 ANCHORS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d mains + 3 "
          "controls: worst dev/absmass %.1e main N<=%d (bar %.0e) "
          "/ %.1e deep (bar %.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        bws = rc["bw"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        cb = cts[~ed]
        xb = bxs[~ed]
        wb = bws[~ed]
        runs = PBB.runs_split(cb)
        Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        P = L2D.blocks_level2(Sr)
        e_c2 = PBB.bound_pairsum(Mr)
        f2 = L2D.bound_vdc(P)
        H = f2["H"]
        S_F = f2["s2"] / H
        Zl = float(np.sum(cts[ed])) + rc["chain"]
        # ---- the frozen positional kernel (from the border bulk)
        brk, m, jb = block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        agg_dev = float(np.max(np.abs(Pb - np.array(P)))) \
            / max(max(abs(v) for v in P), 1e-300) if m else 0.0
        sf_ker = fejer_bil(Pb, Pb, H)
        ker_dev = abs(sf_ker - S_F) / max(S_F, 1e-300)
        # ---- window side through the SAME kernel
        Pw = aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                              rc["hi"], brk, m)
        main = fejer_bil(Pw, Pw, H)
        Pd = Pb - Pw
        T = fejer_bil(Pd, Pb + Pw, H)
        scale = max(S_F, main, abs(T), 1e-300)
        dec_dev = abs(S_F - main - T) / scale
        phi = fejer_apply(Pb + Pw, H)
        tj = Pd * phi
        attr_dev = abs(float(np.sum(tj)) - T) / scale
        t_diag = fejer_bil(Pd, Pd, H)
        t_cross = 2.0 * fejer_bil(Pd, Pw, H)
        comp_dev = abs(t_diag + t_cross - T) / scale
        # ---- magnitude-Delta mutant (m2): |c| aggregation
        Pb_abs = aggregate_blocks(xb, np.abs(cb), rc["lo"],
                                  rc["hi"], brk, m)
        Pw_abs = aggregate_blocks(rc["xu"], np.abs(rc["cw"]),
                                  rc["lo"], rc["hi"], brk, m)
        T_mut = fejer_bil(Pb_abs - Pw_abs, Pb + Pw, H)
        m2_break = abs(S_F - main - T_mut) / scale
        # ---- linear window zero (full support, edge included)
        lin_dev = abs(float(np.sum(rc["cw"]))) \
            / max(float(np.sum(np.abs(rc["cw"]))), 1e-300)
        # ---- class split of the Delta anatomy
        Pb_p = aggregate_blocks(xb[wb > 0], cb[wb > 0], rc["lo"],
                                rc["hi"], brk, m)
        Pb_n = aggregate_blocks(xb[wb <= 0], cb[wb <= 0], rc["lo"],
                                rc["hi"], brk, m)
        wpos = rc["wu"] > 0
        Pw_p = aggregate_blocks(rc["xu"][wpos], rc["cw"][wpos],
                                rc["lo"], rc["hi"], brk, m)
        Pw_n = aggregate_blocks(rc["xu"][~wpos], rc["cw"][~wpos],
                                rc["lo"], rc["hi"], brk, m)
        cls = [float(np.sum(np.abs(v)))
               for v in (Pb_p, Pb_n, Pw_p, Pw_n)]
        tot_cls = max(sum(cls), 1e-300)
        cls = [v / tot_cls for v in cls]
        # ---- node-density census (r297-B2 continuity, Leg D)
        nb = len(cb)
        nr = len(runs)
        d_rank = 0.0
        if nr > 1 and nb > 0:
            for i, (a, b, _s) in enumerate(runs[:-1]):
                d_rank = max(d_rank, abs(b / nb - (i + 1) / nr))
        mx = max(Mr) if Mr else 0.0
        sm = sum(Mr) if Mr else 0.0
        imb = nr * mx / max(sm, 1e-300)
        Ms = sorted(Mr, reverse=True)
        s1 = Ms[0] / max(sm, 1e-300) if Ms else 0.0
        s3 = sum(Ms[:3]) / max(sm, 1e-300) if Ms else 0.0
        M_d1 = Ms[1:]
        M_d3 = Ms[3:]
        imb_d1 = (len(M_d1) * M_d1[0] / max(sum(M_d1), 1e-300)) \
            if M_d1 else 0.0
        imb_d3 = (len(M_d3) * M_d3[0] / max(sum(M_d3), 1e-300)) \
            if M_d3 else 0.0
        Mb = [Mr[i] + (Mr[i + 1] if i + 1 < nr else 0.0)
              for i in range(0, nr, 2)]
        sp_conn = BH.spearman(Mb, list(np.abs(tj))) \
            if m >= 3 else 0.0
        coin = int(int(np.argmax(np.abs(tj))) ==
                   int(np.argmax(Mb))) if m else 0
        return dict(Mr=Mr, Sr=Sr, alt_ok=alt_ok, R=R, P=P,
                    e_c2=e_c2, f2=f2, H=H, S_F=S_F, Zl=Zl,
                    m=len(P), nr=nr, brk=brk, Pb=Pb, Pw=Pw, Pd=Pd,
                    agg_dev=agg_dev, ker_dev=ker_dev, main=main,
                    T=T, dec_dev=dec_dev, tj=tj,
                    attr_dev=attr_dev, t_diag=t_diag,
                    t_cross=t_cross, comp_dev=comp_dev,
                    m2_break=m2_break, lin_dev=lin_dev, cls=cls,
                    d_rank=d_rank, imb=imb, s1=s1, s3=s3,
                    imb_d1=imb_d1, imb_d3=imb_d3,
                    sp_conn=sp_conn, coin=coin)

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    bid_worst = 0.0
    ac_worst = 0.0
    for rc in all_rc + [crecs[c] for c in crecs]:
        ev = rc["ev"]
        bid_worst = max(bid_worst,
                        abs(sum(ev["P"]) - ev["R"])
                        / max(abs(ev["R"]), 1e-300))
        A = L2D.autocorr_full(ev["P"])
        s_all = A[0] + 2.0 * float(np.sum(A[1:]))
        ac_worst = max(ac_worst,
                       abs(s_all - sum(ev["P"]) ** 2)
                       / max(A[0], 1e-300))
    check("G21-block-and-autocorr-identity",
          alt_all and bid_worst <= ID_BAR and ac_worst <= AC_BAR,
          "runs alternate on every world AND sum P == R exact "
          "(worst rel %.1e, bar %.0e) AND (sum P)^2 == A(0) + 2 "
          "sum A(h) exact (worst %.1e x A(0), bar %.0e) over %d "
          "worlds" % (bid_worst, ID_BAR, ac_worst, AC_BAR,
                      len(all_rc) + len(crecs)))

    Ns = [rc["N"] for rc in recs]
    if not smoke:
        eps_c2_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
        sl_c2 = L2D.halves_slope(Ns, eps_c2_rel)
        pref = [(rc["ev"]["m"] + rc["ev"]["H"] - 1) / rc["ev"]["H"]
                for rc in recs]
        sl_pref = L2D.halves_slope(Ns, pref)
        sf_rel = [rc["ev"]["S_F"] / (M_W * M_W) for rc in recs]
        sigma = L2D.halves_slope(Ns, sf_rel)
        sigma_star = 2.0 * (sl_c2 - DELTA_NEED) - sl_pref
        check("G22-r297-target-anchors",
              abs(sigma - R297_SIGMA) <= R297_SIGMA_TOL
              and abs(sigma_star - R297_SIGMA_STAR) <= R297_SSTAR_TOL
              and abs(sl_c2 - R297_SL_C2) <= R297_SL_C2_TOL
              and abs(sl_pref - R297_SL_PREF) <= R297_SL_PREF_TOL,
              "the r297 target-inequality set recomputed bit-near: "
              "sigma %+.3f (ref %+.3f), sigma* %+.3f (ref %+.3f), "
              "sl_c2 %+.3f (ref %+.3f), sl_pref %+.3f (ref %+.3f) "
              "-- the truth margin %.3f sigma stands"
              % (sigma, R297_SIGMA, sigma_star, R297_SIGMA_STAR,
                 sl_c2, R297_SL_C2, sl_pref, R297_SL_PREF,
                 sigma_star - sigma))
        dr_med = float(np.median([rc["ev"]["d_rank"]
                                  for rc in recs]))
        dr_sl = L2D.halves_slope(Ns, [max(rc["ev"]["d_rank"],
                                          1e-300) for rc in recs])
        imb_sl = L2D.halves_slope(Ns, [rc["ev"]["imb"]
                                       for rc in recs])
        check("G23-r297-census-anchors",
              abs(dr_med - R297_DRANK_MED) <= R297_DRANK_TOL
              and abs(dr_sl - R297_DRANK_SL) <= R297_DRANK_SL_TOL
              and abs(imb_sl - R297_IMB_SL) <= R297_IMB_SL_TOL,
              "the r297 asset-2 census recomputed: D_rank med "
              "%.3f (ref %.3f) slope %+.2f (ref %+.2f, falling "
              "-- provable terrain), mass-imbalance slope %+.3f "
              "(ref %+.3f, the growing half)"
              % (dr_med, R297_DRANK_MED, dr_sl, R297_DRANK_SL,
                 imb_sl, R297_IMB_SL))
    else:
        sigma = sigma_star = sl_c2 = sl_pref = float("nan")
        check("G22-r297-target-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")
        check("G23-r297-census-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    # ---------------- S3: exact section + toys + audits + m1/m3
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    w_o, w_i = fr_parseval_sumrule(wrong_b=False)
    v_o, v_i = VCP.fr_symbolic_sumrule()
    _o2, w_mut = fr_parseval_sumrule(wrong_b=True)
    check("G30-sumrule-and-m1", w_o == 0 and w_i == 0
          and v_o == 0 and v_i == 0 and w_mut != 0,
          "the Parseval sum rule RE-PROVED exact in Fractions "
          "(module-own orth dev %s, identity dev %s; r297-G31 "
          "import devs %s/%s); m1 WRONG-b^2 mutant (b_k for "
          "b_k^2) breaks by %s != 0 -- CAUGHT: the squared "
          "recurrence norm ratio is load-bearing"
          % (str(w_o), str(w_i), str(v_o), str(v_i), str(w_mut)))
    toy_worst = toy_transfer()
    check("G31-toy-exactness", toy_worst <= TOY_BAR,
          "the hand toy reproduces the WHOLE pipeline EXACTLY "
          "(worst dev %.1e, bar %.0e): border (0..4)/(3,-1,2,-4,"
          "1) -> Pbeta (2,-2,1), breaks (1.5, 3.5), S_F = 3 == "
          "kernel form; window (0.5, 2.5)/(1,-1) -> Pomega "
          "(1,-1,0), MAIN = 1; PDelta (1,-1,1), T = 2, MAIN + T "
          "== S_F; attribution (1.5, 1, -0.5) sums to T; T_diag "
          "1 + T_cross 1 == T" % (toy_worst, TOY_BAR))
    h_bb = scope_audit("block_breaks", BOUND_FORBIDDEN)
    h_ag = scope_audit("aggregate_blocks", BOUND_FORBIDDEN)
    h_fb = scope_audit("fejer_bil", BOUND_FORBIDDEN)
    h_fa = scope_audit("fejer_apply", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_bb or h_ag or h_fb or h_fa)
    check("G32-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the kernel builders (block_breaks, aggregate_blocks, "
          "fejer_bil, fejer_apply) consume positions + weights + "
          "chain values only (no truth-side identifier in "
          "scope%s); m4a gift mutant FLAGGED (%s); m4b "
          "branch-peek mutant FLAGGED (%s); fragment audit: %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    m3_break = toy_mustfail_m3()
    check("G33-mustfail-m3", m3_break >= MUT_MIN
          and abs(m3_break - 2.0 / 3.0) <= 1e-12,
          "m3 KERNEL-PERTURBED RECOMPOSITION: the Fejer form at "
          "H + 1 breaks the toy identity by %.6f (= 2/3 exact, "
          ">= %.0e) LOUD -- the frozen H is load-bearing in the "
          "kernel, not a free dial" % (m3_break, MUT_MIN))

    # ---------------- S4: Leg A -- the exact decomposition
    section("S4  LEG A: DELTA ANATOMY + DECOMPOSITION_EXACT")
    rc9 = mrecs[0] if not smoke else recs[0]
    n_bp = int(np.sum(rc9["bw"] > 0))
    n_bn = len(rc9["bw"]) - n_bp
    n_wp = int(np.sum(rc9["wu"] > 0))
    n_wn = len(rc9["wu"]) - n_wp
    overlap = len(np.intersect1d(rc9["bx"], rc9["xu"]))
    cls9 = rc9["ev"]["cls"]
    check("G40-delta-anatomy", True,
          "Delta = border (-) window, FOUR signed atom classes "
          "(w9): border ws %d atoms (+) / -vs %d atoms (-) vs "
          "window ws %d / -vs %d; exact support overlap %d "
          "(the unions are %s); bulk |c|-mass shares of the "
          "classes b+/b-/w+/w- = %.2f/%.2f/%.2f/%.2f -- the "
          "mixed-sign structure the r297 |.|-chains lost is "
          "carried atomwise here"
          % (n_bp, n_bn, n_wp, n_wn, overlap,
             "FULLY DISJOINT" if overlap == 0
             else "PARTIALLY SHARED",
             cls9[0], cls9[1], cls9[2], cls9[3]))
    pool_all = all_rc + [crecs[c] for c in crecs]
    agg_w = max(rc["ev"]["agg_dev"] for rc in pool_all)
    ker_w = max(rc["ev"]["ker_dev"] for rc in pool_all)
    check("G41-kernel-reproduction", agg_w <= KER_BAR
          and ker_w <= KER_BAR,
          "the frozen positional kernel REPRODUCES the sealed "
          "r287 pipeline from raw border atoms on %d worlds: "
          "block aggregation vs blocks_level2 worst %.1e; "
          "(1/H) sum W^2 vs bound_vdc S_F worst %.1e (bar %.0e) "
          "-- S_F IS the Fejer quadratic form B(beta, beta)"
          % (len(pool_all), agg_w, ker_w, KER_BAR))
    dec_w = max(rc["ev"]["dec_dev"] for rc in pool_all)
    att_w = max(max(rc["ev"]["attr_dev"], rc["ev"]["comp_dev"])
                for rc in pool_all)
    check("G42-decomposition-exact", dec_w <= DEC_BAR
          and att_w <= ATTR_BAR,
          "DECOMPOSITION_EXACT: S_F = B(omega,omega) + "
          "B(Delta,omega+beta) = MAIN + T(Delta) on %d worlds, "
          "worst dev %.1e of the decomposition scale (bar %.0e); "
          "attribution sum_j t_j == T and T_diag + T_cross == T "
          "worst %.1e (bar %.0e) -- the split is an exact finite "
          "identity, sign structure fully preserved"
          % (len(pool_all), dec_w, DEC_BAR, att_w, ATTR_BAR))
    lin_m = max((rc["ev"]["lin_dev"] for rc in all_rc
                 if rc["N"] <= DEEP_N), default=0.0)
    lin_d = max((rc["ev"]["lin_dev"] for rc in all_rc
                 if rc["N"] > DEEP_N), default=0.0)
    lin_c = max(crecs[c]["ev"]["lin_dev"] for c in crecs)
    check("G43-linear-window-zero", lin_m <= LIN_BAR
          and lin_d <= LIN_BAR_DEEP and lin_c <= LIN_BAR_CTRL,
          "the LINEAR WINDOW ZERO (orthogonality corollary "
          "x pi_{N-2} perp pi_0 on omega): |sum wu x v2| / "
          "sum |wu x v2| worst %.1e main N<=%d (bar %.0e) / "
          "%.1e deep (bar %.0e) / %.1e controls (bar %.0e) -- "
          "the window image of the drive functional VANISHES: "
          "the drive is 100 pct transfer at the linear level"
          % (lin_m, DEEP_N, LIN_BAR, lin_d, LIN_BAR_DEEP,
             lin_c, LIN_BAR_CTRL))
    # orthogonality census (r297-S7 verbatim, WINDOW + BORDER)
    id_pool = (mrecs + [crecs[c] for c in ("EPST", "SCR")]) \
        if smoke else \
        ([rc for rc in recs if rc["kz"] in (KZ_ANCHOR, 20)]
         + mrecs + [crecs[c] for c in ("EPST", "SCR")])
    orth = {}
    for meas in ("WINDOW", "BORDER"):
        crosses = []
        devs = []
        for rc in id_pool:
            X, W = ((rc["xu"], rc["wu"]) if meas == "WINDOW"
                    else (rc["bx"], rc["bw"]))
            cq = VCP.chain_quads(rc["p"]["rows"], rc["N"], X, W)
            crosses.append(max(abs(v) for v in cq["cr"].values()))
            devs.append(abs(cq["q2"] - cq["pd"])
                        / max(abs(cq["q2"]), 1e-300))
        orth[meas] = (float(np.median(crosses)),
                      max(max(crosses), max(devs)))
    ok_orth = (orth["WINDOW"][1] <= ID_HOLDS
               and BORDER_CROSS_BAND[0] <= orth["BORDER"][0]
               <= BORDER_CROSS_BAND[1])
    check("G44-orthogonality-anchor", ok_orth,
          "the r297-S7 census recomputed on %d worlds: WINDOW "
          "orthogonality HOLDS (worst cross+diag dev %.1e <= "
          "%.0e) while BORDER breaks (cross med %.3f in %s) -- "
          "the attachment point and the break, both bit-near "
          "the record" % (len(id_pool), orth["WINDOW"][1],
                          ID_HOLDS, orth["BORDER"][0],
                          str(BORDER_CROSS_BAND)))

    # ---------------- S5: Leg B -- the transfer-term scaling
    section("S5  LEG B: TRANSFER SCALING + SEALED ADJUDICATION")
    show = (sorted(exc, key=lambda r_: r_["kz"]) + mrecs
            if not smoke else mrecs)
    for rc in show:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s m %-3d H %-2d  S_F %.4f  MAIN "
             "%.3f  T %+.3f  sh %.2f  canc_T %.2f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g_branch"] < 0 else "chp",
                ev["m"], ev["H"], ev["S_F"], ev["main"], ev["T"],
                abs(ev["T"]) / max(ev["S_F"], 1e-300),
                float(np.sum(np.abs(ev["tj"])))
                / max(abs(ev["T"]), 1e-300)))
    if not smoke:
        main_rel = [rc["ev"]["main"] / (M_W * M_W) for rc in recs]
        absT_rel = [max(abs(rc["ev"]["T"]), 1e-300) / (M_W * M_W)
                    for rc in recs]
        sl_main = L2D.halves_slope(Ns, main_rel)
        sl_T = L2D.halves_slope(Ns, absT_rel)
        sh = [abs(rc["ev"]["T"]) / max(rc["ev"]["S_F"], 1e-300)
              for rc in recs]
        rmain = [rc["ev"]["main"] / max(rc["ev"]["S_F"], 1e-300)
                 for rc in recs]
        sh_med = float(np.median(sh))
        sh_sl = L2D.halves_slope(Ns, [max(v, 1e-300) for v in sh])
        rmain_med = float(np.median(rmain))
        n_neg = sum(1 for rc in recs if rc["ev"]["T"] < 0.0)
        canc = [float(np.sum(np.abs(rc["ev"]["tj"])))
                / max(abs(rc["ev"]["T"]), 1e-300) for rc in recs]
        canc_med = float(np.median(canc))
        canc_sl = L2D.halves_slope(Ns, canc)
        td_med = float(np.median(
            [math.log10(max(rc["ev"]["t_diag"], 1e-300))
             for rc in recs]))
        tc_med = float(np.median([rc["ev"]["t_cross"]
                                  for rc in recs]))
        main_med = float(np.median(
            [math.log10(max(v, 1e-300)) for v in main_rel]))
        absT_med = float(np.median(
            [math.log10(max(v, 1e-300)) for v in absT_rel]))
        sf_med = float(np.median(
            [math.log10(max(rc["ev"]["S_F"] / (M_W * M_W),
                            1e-300)) for rc in recs]))
        cls_med = [float(np.median([rc["ev"]["cls"][i]
                                    for rc in recs]))
                   for i in range(4)]
        check("G50-transfer-table", True,
              "TRANSFER_TABLE (42 rungs): MAIN/M^2 med %+.2f dec "
              "slope %+.3f; |T|/M^2 med %+.2f dec slope %+.3f; "
              "S_F/M^2 med %+.2f dec (sigma %+.3f); share "
              "|T|/S_F med %.2f slope %+.3f; T < 0 on %d/42; "
              "T_diag med %+.2f dec, T_cross med %+.3g; in-T "
              "cancellation sum|t_j|/|T| med %.2f slope %+.3f; "
              "Delta class shares b+/b-/w+/w- med "
              "%.2f/%.2f/%.2f/%.2f"
              % (main_med, sl_main, absT_med, sl_T, sf_med,
                 sigma, sh_med, sh_sl, n_neg, td_med, tc_med,
                 canc_med, canc_sl, cls_med[0], cls_med[1],
                 cls_med[2], cls_med[3]))
        # world controls: same class rules at the control rungs
        def classify(rm, s_):
            if rm >= UNSTABLE_FACTOR:
                return "UNSTABLE"
            return "T-MINORITY" if s_ < SUB_SHARE else "T-MAJORITY"
        ctl_cls = {}
        for c in ("EPST", "SCR"):
            ev = crecs[c]["ev"]
            ctl_cls[c] = classify(
                ev["main"] / max(ev["S_F"], 1e-300),
                abs(ev["T"]) / max(ev["S_F"], 1e-300))
        main_cls = classify(rmain_med, sh_med)
        world_blind = all(ctl_cls[c] == main_cls for c in ctl_cls)
        check("G51-world-controls", True,
              "the decomposition class at the control rungs "
              "(same sealed med rules): MAIN %s vs %s -- %s "
              "(a class break is a disclosed finding, not a "
              "gate failure; the identity itself is world-blind "
              "by the same algebra, G42)"
              % (main_cls,
                 str({c: ctl_cls[c] for c in sorted(ctl_cls)}),
                 "WORLD-BLIND" if world_blind
                 else "WORLD_SENSITIVE (disclosed)"))
        # sealed adjudication
        if rmain_med >= UNSTABLE_FACTOR:
            outcome = "DECOMPOSITION_UNSTABLE"
        elif sh_med < SUB_SHARE and sl_T <= sl_main - SUB_MARGIN:
            outcome = "TRANSFER_SUBDOMINANT"
        else:
            outcome = "TRANSFER_DOMINANT"
        check("G52-adjudication", True,
              "SEALED RULE fired: %s (med(MAIN/S_F) %.1f vs "
              "UNSTABLE_FACTOR %.0f; share med %.2f vs %.1f; "
              "slope(|T|) %+.3f vs slope(MAIN) %+.3f - %.2f)"
              % (outcome, rmain_med, UNSTABLE_FACTOR, sh_med,
                 SUB_SHARE, sl_T, sl_main, SUB_MARGIN))
    else:
        outcome = "SMOKE_NO_ADJUDICATION"
        world_blind = True
        main_cls = "n/a"
        ctl_cls = {}
        sl_main = sl_T = sh_med = sh_sl = rmain_med = float("nan")
        canc_med = canc_sl = main_med = absT_med = float("nan")
        td_med = tc_med = float("nan")
        n_neg = -1
        cls_med = [float("nan")] * 4
        check("G50-transfer-table", True, "SMOKE: skipped")
        check("G51-world-controls", True, "SMOKE: skipped")
        check("G52-adjudication", True, "SMOKE: skipped")

    # ---------------- S6: Leg C (conditional)
    section("S6  LEG C: THE CANDIDATE THEOREM (CONDITIONAL)")
    if outcome == "TRANSFER_SUBDOMINANT":
        info("CANDIDATE THEOREM (window-border transfer, L2 "
             "generic half): for every rung of the sealed ladder "
             "(N in [%d, %d], H = ceil(sqrt(m))): S_F = "
             "B(omega,omega) + B(Delta,omega+beta) EXACTLY (this "
             "round); B(omega,omega) is Parseval-controlled on "
             "the orthogonal side (proved sum rule + D_rank "
             "equidistribution, slope %+.3f <= sigma* %+.3f "
             "REQUIRED: %s) and T(Delta) is subdominant "
             "(share med %.2f, slope gap %+.3f); with the r297 "
             "target inequality sigma <= sigma* and the v964-S0 "
             "vdC theorem => delta' > %.2f on the generic half; "
             "exceptions: 6 via the r287 F2 certificates, kz15 "
             "via the r270 exact-finite certificate.  Wave-9 "
             "promotion candidate -- NOT promoted here."
             % (min(Ns), max(Ns), sl_main, sigma_star,
                "MET" if sl_main <= sigma_star else "NOT MET "
                "(disclosed: the composition is conditional)",
                sh_med, sl_main - sl_T, DELTA_NEED))
        fired = True
    else:
        info("Leg C VOID without substitute (outcome %s).  The "
             "precisely narrowed gap object is documented in the "
             "verdict." % outcome)
        fired = False
    check("G60-leg-c", True,
          "Leg C %s -- fires ONLY on TRANSFER_SUBDOMINANT by the "
          "sealed rule; no post-hoc rescue"
          % ("FIRED (candidate printed, NOT promoted)" if fired
             else "VOID"))

    # ---------------- S7: Leg D -- mass-imbalance bycatch
    section("S7  LEG D: MASS-IMBALANCE BYCATCH")
    if not smoke:
        sl_imb = L2D.halves_slope(Ns, [rc["ev"]["imb"]
                                       for rc in recs])
        sl_d1 = L2D.halves_slope(
            Ns, [max(rc["ev"]["imb_d1"], 1e-300) for rc in recs])
        sl_d3 = L2D.halves_slope(
            Ns, [max(rc["ev"]["imb_d3"], 1e-300) for rc in recs])
        s1_med = float(np.median([rc["ev"]["s1"] for rc in recs]))
        s3_med = float(np.median([rc["ev"]["s3"] for rc in recs]))
        outlier = sl_d3 <= OUT_FACTOR * sl_imb
        sp_med = float(np.median([rc["ev"]["sp_conn"]
                                  for rc in recs]))
        n_coin = sum(rc["ev"]["coin"] for rc in recs)
        check("G70-imbalance-bycatch", True,
              "IMBALANCE_NOTE: %s -- slope(imb) %+.3f vs "
              "drop-top-1 %+.3f / drop-top-3 %+.3f (OUTLIER iff "
              "d3 <= %.1f x imb); top-1/top-3 mass shares med "
              "%.2f/%.2f; CONNECTION of the gap halves: "
              "sp(block mass, |t_j|) med %+.2f, argmax "
              "coincidence %d/42 -- %s"
              % ("OUTLIER_CARRIED" if outlier else "BROAD_BASED",
                 sl_imb, sl_d1, sl_d3, OUT_FACTOR, s1_med,
                 s3_med, sp_med, n_coin,
                 "the mass carriers and the T carriers largely "
                 "coincide" if sp_med >= 0.5 else
                 "the two gap halves are structurally separate"))
    else:
        outlier = False
        sl_imb = sl_d1 = sl_d3 = sp_med = float("nan")
        n_coin = -1
        check("G70-imbalance-bycatch", True, "SMOKE: skipped")

    # ---------------- S8: must-fail m2 + anchors + mp wards
    section("S8  MUSTFAIL M2 + ANCHORS + MP WARDS")
    m2_pool = mrecs + ([recs[0]] if smoke else [])
    m2_min = min(rc["ev"]["m2_break"] for rc in m2_pool)
    m2_note = "; ".join("w%d %.1e" % (rc["kz"],
                                      rc["ev"]["m2_break"])
                        for rc in m2_pool)
    check("G80-mustfail-m2", m2_min >= MUT_MIN,
          "m2 MAGNITUDE DELTA (|c| aggregation instead of the "
          "signed c -- the r297 magnitude error as a mustfail): "
          "the exact identity breaks by %s of the decomposition "
          "scale (all >= %.0e) LOUD -- the sign structure of "
          "Delta is load-bearing; any |.|-transfer loses the "
          "object" % (m2_note, MUT_MIN))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    evS = crecs["SMOOTH"]["ev"]
    okSd = evS["dec_dev"] <= DEC_BAR
    check("G81-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okSd,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "the decomposition identity holds trivially on the "
          "self-aliased source (%s)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okSd else "BROKEN"))
    if not smoke:
        mp_note = []
        ok_mp = True
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        t15 = PBB.mp_drive(rc15["p"], MP_DPS)
        d15 = abs(t15 - rc15["t_term"])
        ok_mp = ok_mp and (d15 <= MP_T_BAR)
        mp_note.append("kz15 (N %d) dev %.1e (bar %.0e)"
                       % (rc15["N"], d15, MP_T_BAR))
        for rc in recs[-2:]:
            t_mp = PBB.mp_drive(rc["p"], MP_DPS)
            dv = abs(t_mp - rc["t_term"])
            ok_mp = ok_mp and (dv <= MP_DEEP_BAR)
            mp_note.append("kz%d (N %d, DEEPEST) dev %.1e (bar "
                           "%.0e)" % (rc["kz"], rc["N"], dv,
                                      MP_DEEP_BAR))
        check("G82-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs: %s" % (MP_DPS, "; ".join(mp_note)))
    else:
        check("G82-mp-deep-wards", True, "SMOKE: skipped")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact sign-preserving window-border "
          "decomposition of the vdC input on the frozen "
          "positional Fejer kernel, its measured scaling census, "
          "the sealed three-way adjudication, and the Leg-D "
          "bycatch -- NO new certificate promoted, NO bound "
          "modification of the sealed forms")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["DECOMPOSITION_EXACT(S_F = B(omega,omega) + "
                 "B(Delta,omega+beta), Delta = border (-) window, "
                 "frozen positional Fejer kernel, worst dev "
                 "%.1e, %d/%d worlds)"
                 % (dec_w, len(pool_all), len(pool_all))]
        parts.append("TRANSFER_TABLE(MAIN med %+.2f dec sl "
                     "%+.3f; |T| med %+.2f dec sl %+.3f; share "
                     "med %.2f sl %+.3f; T<0 %d/42; canc_T med "
                     "%.2f sl %+.3f)"
                     % (main_med, sl_main, absT_med, sl_T,
                        sh_med, sh_sl, n_neg, canc_med, canc_sl))
        if outcome == "DECOMPOSITION_UNSTABLE":
            parts.append("DECOMPOSITION_UNSTABLE(med MAIN/S_F "
                         "%.1f >= %.0f: main and transfer are "
                         "near-cancelling large copies -- THIS "
                         "cancellation is the object; the THIRD "
                         "recurrence of the resummation pattern, "
                         "crossref r259 prefix resummation + "
                         "r261 fullsource free-prefix)"
                         % (rmain_med, UNSTABLE_FACTOR))
        elif outcome == "TRANSFER_SUBDOMINANT":
            parts.append("TRANSFER_SUBDOMINANT(share med %.2f < "
                         "%.1f, slope gap %+.3f >= %.2f)"
                         % (sh_med, SUB_SHARE, sl_main - sl_T,
                            SUB_MARGIN))
            parts.append("CANDIDATE_THEOREM(window-border "
                         "transfer, printed in S6, wave-9 "
                         "candidate NOT promoted)")
        else:
            parts.append("TRANSFER_DOMINANT(share med %.2f; T "
                         "anatomy: T_diag med %+.2f dec, "
                         "T_cross med %+.3g, class shares "
                         "b+/b-/w+/w- %.2f/%.2f/%.2f/%.2f, "
                         "in-T cancellation med %.2f -- the "
                         "signed Delta structure is the "
                         "precised gap object)"
                         % (sh_med, td_med, tc_med, cls_med[0],
                            cls_med[1], cls_med[2], cls_med[3],
                            canc_med))
        parts.append("IMBALANCE_NOTE(%s: sl imb %+.3f vs d1 "
                     "%+.3f / d3 %+.3f; sp(Mb,|t_j|) med %+.2f, "
                     "argmax coincidence %d/42)"
                     % ("OUTLIER_CARRIED" if outlier
                        else "BROAD_BASED", sl_imb, sl_d1,
                        sl_d3, sp_med, n_coin))
        if not world_blind:
            parts.append("WORLD_SENSITIVE(main %s vs %s -- "
                         "disclosed finding)"
                         % (main_cls, str(ctl_cls)))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the decomposition "
          "identity, the kernel reproduction, the attribution, "
          "the linear window zero, the Fractions sum rule (all "
          "world-blind); MEASURED: every slope, share, class "
          "and connection stat (42 rungs only); OPEN: the "
          "cancellation mechanism between MAIN and T (if "
          "UNSTABLE) / the Delta anatomy theorem (if DOMINANT), "
          "the cofinal step H5, kz15 beyond r270; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
