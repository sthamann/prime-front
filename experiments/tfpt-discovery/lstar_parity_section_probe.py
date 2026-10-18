#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lstar_parity_section_probe -- PRIME.LSTAR.PARITY_SECTION.01
(round 336): the CHEBYSHEV TOEPLITZ+HANKEL PARITY SECTION of L* --
the reviewer's rank-3 language, the last pre-authorized L* arm
after r334 structurally capped the capacity route.  L* (the open
scalar of r283/r284/r286: lambda_max(E_{N_w}) < 1 for the
nu-dressed mu-CD kernel, margin 1.6752e-4 on w9, crossing exactly
at minC + 1 = 185) is re-read in the Chebyshev coordinate: map the
window hull affinely onto [-1, 1], set x = cos theta; every real
polynomial with deg p < N is p(cos theta) = sum_{k<N} a_k cos(k
theta), and with the COSINE MOMENTS of the signed source
    c_r = sum_j (mu_j - nu_j) cos(r theta_j)
the EXACT identity
    int p^2 d(mu - nu) = sum_{k,l<N} a_k a_l (c_{|k-l|} + c_{k+l})/2
holds -- THE L* MATRIX IS A FINITE TOEPLITZ+HANKEL PARITY SECTION
M_N = (T_N + H_N)/2, congruent (exact rational congruence M =
S (V_+^T T_M(c) V_+) S, S = diag(1, 1/2, ..., 1/2), M = 2N - 1) to
the EVEN parity compression of the full symmetric Toeplitz section
-- the mirror object of the v549/v550 (T150/T151) machinery, where
the ODD compression U_-^T T U_- = T - H carried the certified
grid step-over: a pointwise NEGATIVE symbol with a POSITIVE parity
section because the negative symbol zone [0, theta_c) sits below
the first active parity grid point (the methodological template
this round transcribes to the L* side).  THE ROUND'S THREE KILL
TESTS, sealed (reviewer verbatim -- the lane stays open only if
ALL THREE carry): (1) the Chebyshev T+H representation is
bit-exact (exact Fractions on a small rational window, f64 <=
1e-12 on w9 + a ladder sample); (2) MAIN and the rational twin
have a parity-specific negative window geometry that the four
dead controls do NOT have (negative symbol zones, first active
parity frequency, their distance -- world-comparative under the
sealed r281 distance rule); (3) a SOURCE-PURE distance scalar
(negative symbol zone <-> first active parity mode) predicts the
L* flip WITHOUT reading h_n or lambda_max (blind predictor on the
42-rung ladder + the four controls; AST audit against target
read-back).  NOT a proof round: no L* claim, no bound mechanism,
no certificate -- machinery + census + honest typing.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE SYMBOL CONVENTION (sealed): the finite symbol at truncation R
is f_R(theta) = c_0 + 2 sum_{r=1}^{R} c_r cos(r theta) on [0, pi]
(the Dirichlet partial sum of the folded signed measure in the
mapped angle); the section of size n consumes exactly the moments
r <= R(n) = 2(n - 1), so its form is int q f_{R(n)} dtheta/(2 pi)
with q = p(cos theta)^2 >= 0 of trigonometric degree <= R(n): the
truncation is EXACT for the section, not an approximation.  THE
ACTIVE PARITY GRID (sealed at design time, disclosed): theta_k =
pi k / n, k = 1..n-1 (k = 0 and k = n excluded -- the step-over
convention of the T151 template: the grid never contains theta =
0); the first active parity frequency is theta_1 = pi/n.  THE
FEJER VARIANT (C2 clause ii, the reviewer's Fejer mean): sigma_R
f(theta) = c_0 + 2 sum (1 - r/(R+1)) c_r cos(r theta) -- the
Fejer kernel is NONNEGATIVE, so a negative Fejer reading is a
genuine net-negative local signed mass at resolution ~ pi/n,
never a Gibbs artifact; the PRIMARY sealed predictor is therefore
the Fejer variant (disclosed design choice), the Dirichlet-reading
variant is carried as the sealed SECONDARY column, both frozen
before evaluation:
    n_pred = first n in [2, 2 N_w + 8] with
             min_{k=1..n-1} sigma_{R(n)} f(pi k / n) < 0
(source-pure: consumes the c_r sequence only, i.e. atom positions
+ signed weights; never h_n, never a spectrum).  DISCLOSED
PRE-FREEZE RANGE EXTENSION: the scan cap was widened from N_w + 8
to 2 N_w + 8 after smoke pass 1 showed the w9 Fejer floor still
positive at N_w + 8 (a truncated None is a worse measurement than
a located late firing); the extension happened BEFORE the freeze
and BEFORE any full evaluation; no bar, band, grid or typing rule
moved.

INDEX FIREWALL (binding, r238-r334 discipline): w = window, S =
#union atoms, S_+/S_- = #mu/#nu atoms, N_w = (S+1)//2 = builder
depth, minC = first n with h_n < 0, crossing = minC + 1 (the r283
monotone-loading theorem, consumed as the crossing dictionary on
the ladder; controls re-measured spectrally); theta_j = arccos of
the affinely mapped union atom, c_r = the signed cosine moments.
Ground truth (r283/r284/r334 records, control flips, census
offsets) enters GATES and record tables only; the sealed
constructors consume position/weight/moment arrays ONLY (AST
scope audit); no zero/prime oracles anywhere (AST firewall); the
predictor and every symbol statistic are world-blind (NO
eigenvalue, NO sign chain, NO withheld record in any constructor
-- enforced by the scope audit; the m2/m4 mutants prove the audit
bites).  MACHINERY IMPORTED VERBATIM: document pipeline
V.{build_measures, lam_max_at, admissible_indices}, r283
FS.{mu_chain_f64, b_matrix_f64, crossing_from_B}, r278
MS.ctx_build, r280 BL.{union_of_ctx, sign_chain_f64}, v881
PIK.{lambda_eps, folded_measure, build_rung}, r243
PB.smooth_comb, paircorr PC.{Grid, gen_model}, r244 BH.spearman,
r331 TR.{base_comb, build_world}, r289 AKD.twin_rational, r276
MF.local_gaps, v563 core READ-ONLY.

LEG 0 -- ANCHORS: w9 records through the document pipeline
(S = 367 = 263 + 104, N_w = 184, lambda_max(E_184) = 0.99983248,
lambda at 185 = 1.00003660, margin 1.6752e-4); the campaign
channel cross-gate (BL union == V union at 1e-9 rel, minC = 184);
the r284 shallow edge (the two smallest-theta nu atoms are folds
2 and 4 -- gated, and their position printed against the measured
negative zones); the r334 coordinate 1 - kappa_int as a SEALED
COMPARISON COLUMN (record values 4.8e-4 / 4.3e-4 / 2.6e-5 / 9e-6
at kz18/kz9/kz60/kz52 -- reporting only, never recomputed, never
consumed).

LEG A -- THE EXACT REPRESENTATION (C1, kill test 1): (a1) exact
rational toy (7 union atoms, hull [-3/4, 3/4] STRICTLY inside
[-1, 1], asymmetric weights, sealed below): the T+H identity in
EXACT Fractions (Chebyshev recurrence, mapped hull), bit-equal;
(a2) the parity dilatation EXPLICIT and exact: M == S (V_+^T
T_7(c) V_+) S elementwise in Fractions (V_+ the unnormalized even
parity columns e_0, e_{+k} + e_{-k}; S = diag(1, 1/2, 1/2, 1/2)),
and the ODD compression documented beside it ((V_-^T T V_-)_{kl}
== 2(c_{|k-l|} - c_{k+l}) exactly -- the v549 T-H object, NOT the
L* matrix); (a3) f64 identity on w9 for the sealed coefficient
family (Chebyshev unit coefficients d in {1, 2, 3, N/2, N-1} + 3
deterministic golden draws), rel dev <= 1e-12 against the
absolute-mass scale; the same on the ladder sample (first /
median / last rung, reduced family); (a4) the FFT mode-reading
cross-route (rfft of the padded moment vector == direct cosine
sums) exact to 1e-13 on the toy and 1e-11 on w9 at n = 20 / 120 /
184; (a5) the section flip: min eig M_184 > 0 >= min eig M_185
(within the disclosed f64 resolution ||M|| 1e-12; the PD
statement itself is carried by the r283-gated crossing 185, not
by raw f64 eigenvalues -- disclosed).

LEG B -- THE SYMBOL ANATOMY (C2 pre-stage, kill test 2): per
world at its OWN N_w and R(N_w) = 2(N_w - 1): the negative zones
of f_{R} on [0, pi] (sealed fine grid 8192 + 60-step bisection at
every sign change), the active parity grid pi k / N_w, and the
four sealed world statistics
  K_P1 = total negative-zone measure / pi,
  K_P2 = #active modes inside negative zones (the geometric
         Schur count),
  K_P3 = the Fejer floor min_k sigma_R f(pi k/N_w) / c_0,
  K_P4 = min distance from any negative zone to the active grid
         in units of the mode spacing pi/N_w (None if no zones);
worlds: MAIN + rational TWIN (live) vs EPST / SCR / SMOOTH / HL2
(dead, built verbatim through the r278/r280/r284 channel, minC ==
flips 25/21/27/25 gated); adjudication by the sealed r281
distance rule (MAIN_SEPARATING iff MAIN's value is farther from
EVERY dead value than the dead spread) => PARITY_WORLD_SEEN /
PARITY_WORLD_BLIND.

LEG C -- THE BLIND PREDICTOR (kill test 3): the sealed scan
(PRIMARY Fejer, SECONDARY Dirichlet, both frozen) on the 42
frame-A rungs (h <= 900, r281 census channel re-gated: offset
distribution == r281, anchors exact, half-filling 42/42; crossing
= minC + 1 by the r283 theorem) + the four controls (crossing
re-measured spectrally at depth 40, == flip + 1); sealed band
test |log2(n_pred / crossing)| <= 1.0 on ALL 46 worlds (a None
prediction counts as a break) => PREDICTOR_LAW; else spearman
(n_pred, crossing) >= 0.75 over the worlds with finite n_pred =>
PREDICTOR_ORDERING (with the r284 honesty clause when the
controls fail the band -- the ordering then rides the trivial N_w
scaling); else PREDICTOR_REFUTED (break loci printed).  The
STEP-OVER CLAUSES at n = N_w on MAIN and TWIN: (i) no active mode
inside any negative zone (K_P2 == 0), OR (ii) the Fejer mean is
positive on all active modes (K_P3 > 0) => the verdict token
NEGATIVE_WINDOW_STEP_OVER with the fired clause(s) named.

LEG D -- THE SCHUR BLOCK SKETCH (C3, measurement only): per world
and per ladder rung at n = N_w: the block size = #active modes
with negative Dirichlet reading and #active modes with negative
Fejer reading (how many deep modes a fixed finite Schur block
would need), and the REST FLOOR = min Fejer reading over the
modes OUTSIDE the Fejer-negative block, normalized by c_0 (is the
remainder source-purely positive?) -- census over the 42 rungs,
block-size distribution and floor signs printed; no bound is
claimed from it.

LEG E -- WARDS / MUST-FAILS (each loud): (m1) T+H WITH THE WRONG
PARITY CONVOLUTION: the odd-sector matrix (c_{|k-l|} - c_{k+l})/2
must break the exact toy identity (Fractions, difference exactly
nonzero) -- CAUGHT; (m2) PREDICTOR READS THE TARGET: a mutant
orienting n_pred by the withheld lambda record is FLAGGED by the
AST scope audit; (m3) SYMBOL ON THE UNNORMALIZED WINDOW: cosine
moments taken at arccos of the UNMAPPED atoms (hull strictly
inside [-1, 1]) mixed with the mapped basis must break the exact
toy identity (Fractions, difference exactly nonzero) -- CAUGHT;
(m4) FEJER ORDER BY SIGHT: a mutant scanning Fejer orders against
the withheld crossing until the floor turns positive is FLAGGED
by the AST scope audit.  STOP LIST (anti-gates, binding): NO L*
claim, NO bound mechanism, NO step-over promoted as a
certificate, NO posthoc grid or truncation variant, NO derived
5/7, NO RH claim; r243..r335 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_+ 263, S_- 104, N_w
184); REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN
1.6752e-4 rel tol 0.01; MINC_OFF9 0 (minC = 184); CTRL_FLIPS
{EPST 25, SCR 21, SMOOTH 27}; HL2 seed 101 flip 25; CTRL_CROSS
{EPST 26, SCR 22, SMOOTH 28, HL2 26} (r284 record); EXT 8 / EXT2
32; CTRL_DEPTH 40; H_CAP 900; ANCHORS {9:0, 12:2, 13:2, 26:3,
40:1, 15:1, 52:0}; R281_DIST {0:18, 1:10, 2:6, 3:6, 4:1, 5:1};
PAD 8 (scan cap 2 N_w + PAD, the disclosed pre-freeze range
extension above); BAND 1.0 (log2); SP_BAR 0.75; ID_TOL 1e-12; FFT_TOY
1e-13; FFT_W9 1e-11; TH_GRID 8192; BIS_IT 60; EDGE_TOL 1e-10;
EIG_TOL_FACT 1e-12 (x ||M||); XCHAN_TOL 1e-9; TWIN_TOL 1e-8;
TWIN_BAR 1e-3 (rel); IDG_DEGS {1, 2, 3, N//2, N-1}; GOLDEN_DRAWS
3; LADDER_IDG {1, N//2, N-1} + 1 draw; R334_KINT {18: 4.8e-4,
9: 4.3e-4, 60: 2.6e-5, 52: 9e-6} (record, comparison column
only); SHALLOW_FOLDS (2, 4) (r284 record); toy: mu {-3/4: 1,
-1/4: 2/3, 1/4: 1/2, 3/4: 1}, nu {-1/2: 1/3, 0: 1/4, 1/2: 1/5},
a = (1, -2/3, 1/5, -1/7); zone toys: (1, -1) edge pi/3, (1, +1)
edge 2pi/3, (1/10, 0, -1) two zones at arccos(1/20)/2 and pi -
arccos(1/20)/2; runtime <= 1800 s; smoke = toys + firewall +
scopes + mutants + w9 f64 block (records, channel gate, identity,
section flip, FFT cross-route, anatomy, w9 predictor); ladder,
controls, twin, world rule and adjudication skipped.  PRE-SPEC
SCOPING (disclosed): the r283/r284/r334 record numbers (S counts,
lambda records, flips, census offsets, shallow-edge folds, the
1 - kappa_int column) are consumed as sealed gate anchors and
comparison prints only; the symbol convention (Dirichlet partial
sum at R(n) = 2(n-1)), the active grid pi k/n with both endpoints
excluded, the Fejer-primary predictor, the four world statistics,
the distance rule, every bar/tolerance, the mutants and the
verdict form were fixed at design time from the published record
geometry BEFORE any machinery pass of this probe; no bar, band,
grid or typing rule was tuned after any evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] PARITY_FINITESECTION_CARRIER(w9 + twin: the
    finite symbol attains negative values at R(N_w) while the
    N_w section is PD through the r283-gated crossing -- the
    positivity is a genuine finite-section effect) /
    SYMBOL_RESTATEMENT(named reason: the symbol is pointwise
    nonnegative on the live worlds -- nothing is stepped over,
    the section form merely restates positivity)
  + [exactly one of] NEGATIVE_WINDOW_STEP_OVER(fired clauses i /
    ii on MAIN and TWIN at n = N_w) / NO_STEP_OVER(loci)
  + [exactly one of] PARITY_WORLD_SEEN(separating stats) /
    PARITY_WORLD_BLIND
  + [exactly one of] PREDICTOR_LAW(max band dev) /
    PREDICTOR_ORDERING(spearman; honesty clause) /
    PREDICTOR_REFUTED(break loci)
  + SCHUR_LEDGER(block census + rest-floor signs) [always].
Honesty before beauty: the T+H identity and the parity dilatation
are EXACT COORDINATES of the open scalar L*, not a proof; a
passing step-over clause is a measured geometric fact at one
degree, not a positivity mechanism; a passing predictor band is a
falsifiable crossing FORMULA, not a theorem; the Schur ledger is
a size measurement, no block is constructed; no verdict claims
L*, a bound mechanism, a derived 5/7, or RH progress in any
direction.

RECORD TABLES (frozen from the record run; two-commit protocol,
chronology honest: smoke pass 1 = 25/25 (0.2 s) -- it exposed
that the original scan cap N_w + 8 truncates the w9 PRIMARY
predictor to None (the Fejer floor is still positive at N_w + 8),
whereupon the DISCLOSED PRE-FREEZE RANGE EXTENSION above (cap ->
2 N_w + 8) was made BEFORE the freeze and BEFORE any full
evaluation; smoke pass 2 = 25/25 (0.2 s; w9 n_pred = 216);
PRE-FREEZE COMMIT d38b43c1 (spec + machinery, no record tables).
Calibration pass 1 = first full evaluation = 25/25, wall 5.0 s,
NO amendment (no gate red, no rule moved).  The post-freeze
record runs are numerically identical: run1 = 25/25 (5.0 s),
run2 = 25/25 (5.0 s), byte-identical up to WALL):
CAL_VERDICT = PARITY_FINITESECTION_CARRIER(w9: f_366 attains
-5.072 on the sealed grid (127 negative zones, total measure
0.2766 pi) while the 184-section is PD through the r283-gated
crossing 185 == minC + 1; f64 min eig M_184 = +5.7e-8 > 0 >
-1.2e-8 = min eig M_185, signs clean, negative inertia at 185
exactly 1; twin identical)
+ NEGATIVE_WINDOW_STEP_OVER(clause ii on MAIN and TWIN: the
Fejer floor at N_w is POSITIVE on all 183 active modes (K_P3 =
+2.164e-3, min at mode k = 1; twin dev 2.1e-10) while clause i
FAILS (K_P2 = 34 of 183 Dirichlet mode readings sit inside
negative zones -- Gibbs dips of the partial sum; the Fejer mean
removes them: the reviewer's variant (ii) is the carrying
clause, exactly as the T151 template read the mean rather than
the pointwise symbol)
+ PARITY_WORLD_BLIND(kill test 2 FAILS under the sealed r281
rule -- all four statistics blind: K_P1 MAIN 0.2766 inside dead
0.039..0.385; K_P2 MAIN 34 vs dead 0..85; K_P3 MAIN +2.2e-3,
dist to the nearest dead value 1.1e-4 << spread 1.207; K_P4 all
five worlds 0.0 except SMOOTH 0.226; the SIGN structure that
looked separating (MAIN/TWIN Fejer floor positive, EPST/SCR/HL2
negative -1.205/-0.804/-0.655) is broken by SMOOTH: a DEAD
world (crossing 28) with POSITIVE Fejer floor +2.05e-3 and zero
Dirichlet block -- SMOOTH's death is not a local-negative-mass
event, so no local symbol statistic of this family can be
world-complete)
+ PREDICTOR_ORDERING(PRIMARY Fejer: 42/42 rungs IN band (max
rung dev 0.224 octaves; w9 n_pred 216 vs crossing 185),
controls 1/4 in band (EPST 80 vs 26 dev 1.62, SCR 37 vs 22 dev
0.75 IN, SMOOTH None vs 28 = break, HL2 98 vs 26 dev 1.91),
LAW not awarded; spearman +0.999 over the 45 finite predictions
>= 0.75 => ORDERING with the r284 honesty clause: the ordering
rides the trivial N_w scaling of the ladder -- the
mechanism-relevant discriminant, the four controls, breaks the
band on 3 of 4; SECONDARY Dirichlet fires early everywhere (w9
at 24, SCR at 6 -- the Gibbs column, printed, not adjudicated)
+ SCHUR_LEDGER(the 42-rung census at n = N_w: Fejer block size
0 on 42/42 rungs and the Fejer floor POSITIVE on 42/42 (min
+4.44e-4 at kz64) -- the C3 shape 'small fixed block + source-
pure positive rest floor' holds with the EMPTY block on every
live rung; Dirichlet blocks med 116 / max 302 (pure Gibbs, not
a usable block); dead controls: Fejer blocks 34/29/0/11 of 183
(EPST/SCR/SMOOTH/HL2), their rest floors after removing the
negative modes are positive again (1.3e-3/2.1e-3/2.1e-3/
3.3e-5) -- the dead sickness IS the block, not the floor).
Key numbers.  W9: hull [-1, 0.99996] mapped; theta_1 = pi/184 =
1.7074e-2; the two smallest-theta nu atoms are folds 2/4 == r284
record, at mapped theta 1.4827e-2 / 3.3154e-2 -- the fold-2 nu
atom sits 13 percent BELOW the first active parity frequency
and inside the first negative zone [4.3131e-3, 1.2891e-2]
(which itself sits below theta_1: the w9 zero-adjacent zone IS
stepped over geometrically, the further 126 zones are Gibbs-
striped across the window and touch the grid, whence clause i
fails while clause ii carries); w9 Fejer floor profile
+2.39e-2 / +3.52e-3 / +2.02e-3 / +2.16e-3 / +1.99e-3 /
+2.10e-3 / +2.12e-3 at n = 20/120/183/184/185/186/190 -- the
floor does NOT dip at the crossing: the L* flip at 185 is NOT a
local-mass event at Fejer resolution, the flip lives in the
sharper two-atom extremal of r284 (the honest central negative
of the round, stated as content); the PRIMARY predictor fires
at 216 = crossing + 31 (the Fejer width pi/n must shrink ~17
percent past the wall before a mode reading flips).  EXACT
LEG: toy identity value 113856919/26790750 bit-equal (c_0 =
143/60, c_1 = 1/30); dilatation M == S V_+^T T_7 V_+ S and odd
== 2(c_{|k-l|} - c_{k+l}) elementwise exact; zone edges vs
closed forms <= 4.4e-16; FFT cross-routes 1.1e-14 toy /
7.9e-14 w9 (bars 1e-13 / 1e-11); f64 identity 2.2e-15 on w9
(8-member family), ladder sample kz18/kz60/kz52 = 5.9e-15 /
1.4e-15 / 3.3e-15 (bar 1e-12).  R334 COMPARISON COLUMN (record
1 - kappa_int vs the measured Fejer floor, both source-pure
near-wall coordinates): kz18 4.8e-4 vs +2.08e-3, kz9 4.3e-4 vs
+2.16e-3, kz60 2.6e-5 vs +8.19e-4, kz52 9.0e-6 vs +4.48e-4 --
both fall along the ladder but the Fejer floor falls ~5x where
1 - kappa_int falls ~50x: the parity floor is a SECOND, softer
near-wall coordinate, not the same number in disguise.
PREDICTOR CENSUS (sample): kz18 153 vs 144, kz9 216 vs 185,
kz60 412 vs 389, kz52 918 vs 879 -- offset +9..+39, ratio band
<= 0.224 octaves on all 42 rungs.  MUST-FAILS: m1 odd-parity
exact difference 222371533/53581500 != 0 CAUGHT; m3 unmapped-
moment exact difference 1602051079/979776000 != 0 CAUGHT; m2
FLAGGED (REC_LAM@586); m4 FLAGGED (cross_true@601);
constructor scopes + fragment audit CLEAN.  Runtime 5.0 / 5.0 s
(bar 1800); deterministic, run1/run2 byte-identical up to WALL.
AMENDMENTS AFTER FREEZE: NONE (the one disclosed pre-freeze
range extension is documented above; no bar, band, grid,
statistic, family or adjudication rule moved at any point after
the freeze).

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
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import verify_lstar_instance as V                # noqa: E402 document
import fullsource_quasidefiniteness_probe as FS  # noqa: E402 r283
import metric_stability_probe as MS              # noqa: E402 r278
import budget_localization_probe as BL           # noqa: E402 r280
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import principal_bessel_probe as PB              # noqa: E402 r243
import paircorr_margin_probe as PC               # noqa: E402
import bordered_hankel_probe as BH               # noqa: E402 r244
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
MINC_OFF9 = 0
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
CTRL_CROSS = {"EPST": 26, "SCR": 22, "SMOOTH": 28, "HL2": 26}
EXT = 8
EXT2 = 32
CTRL_DEPTH = 40
H_CAP = 900
ANCHORS = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1, 15: 1, 52: 0}
R281_DIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
PAD = 8
BAND = 1.0
SP_BAR = 0.75
ID_TOL = 1.0e-12
FFT_TOY = 1.0e-13
FFT_W9 = 1.0e-11
TH_GRID = 8192
BIS_IT = 60
EDGE_TOL = 1.0e-10
EIG_TOL_FACT = 1.0e-12
XCHAN_TOL = 1.0e-9
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
GOLDEN_DRAWS = 3
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
SHALLOW_FOLDS = (2, 4)
R334_KINT = {18: 4.8e-4, 9: 4.3e-4, 60: 2.6e-5, 52: 9.0e-6}

# sealed exact toy (rational; hull [-3/4, 3/4] strictly inside [-1, 1])
TOY_MU = ((Fr(-3, 4), Fr(1)), (Fr(-1, 4), Fr(2, 3)),
          (Fr(1, 4), Fr(1, 2)), (Fr(3, 4), Fr(1)))
TOY_NU = ((Fr(-1, 2), Fr(1, 3)), (Fr(0), Fr(1, 4)),
          (Fr(1, 2), Fr(1, 5)))
TOY_A = (Fr(1), Fr(-2, 3), Fr(1, 5), Fr(-1, 7))

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
    return (not bad), ("NO zero/prime oracles; the sealed constructors "
                       "consume position / signed-weight / moment "
                       "arrays ONLY; record numbers and flips enter "
                       "gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
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


CONSTRUCTORS = ("affine_theta", "cos_moments", "th_matrix",
                "symbol_grid", "symbol_at", "mode_readings",
                "neg_zones", "zone_grid_stats", "predictor_scan",
                "golden_coeffs")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "HL2_FLIP", "CTRL_CROSS", "ANCHORS",
                   "R281_DIST", "MINC_OFF9", "R334_KINT", "eigh",
                   "eigvalsh", "sign_chain_f64", "crossing_from_B",
                   "lam_max_at", "minC_true", "cross_true"}


def scope_audit(funcname):
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
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def affine_theta(xu):
    """map the union hull affinely onto [-1, 1] and return the
    mapped angles theta = arccos(t); consumes atom positions
    only."""
    x = np.asarray(xu, float)
    lo, hi = float(np.min(x)), float(np.max(x))
    t = (2.0 * x - (lo + hi)) / (hi - lo)
    t = np.clip(t, -1.0, 1.0)
    return np.arccos(t), t, (lo, hi)


def cos_moments(theta, wu, R):
    """the signed cosine moments c_r = sum_j w_j cos(r theta_j),
    r = 0..R; consumes mapped angles + signed weights only."""
    th = np.asarray(theta, float)
    w = np.asarray(wu, float)
    c = np.empty(R + 1)
    c[0] = float(np.sum(w))
    pm = np.ones_like(th)
    ct = np.cos(th)
    cur = ct.copy()
    for r in range(1, R + 1):
        c[r] = float(np.dot(w, cur))
        pm, cur = cur, 2.0 * ct * cur - pm
    return c


def th_matrix(c, n):
    """the L* parity-section matrix M[k, l] = (c_{|k-l|} +
    c_{k+l}) / 2, k, l < n; consumes the moment array only."""
    idx = np.arange(n)
    K = np.abs(idx[:, None] - idx[None, :])
    P = idx[:, None] + idx[None, :]
    return 0.5 * (np.asarray(c, float)[K] + np.asarray(c, float)[P])


def symbol_grid(c, R, G):
    """the finite symbol f_R on the sealed uniform grid of G+1
    points on [0, pi] (Chebyshev recurrence in cos theta)."""
    th = np.linspace(0.0, math.pi, G + 1)
    ct = np.cos(th)
    f = np.full(G + 1, float(c[0]))
    pm = np.ones(G + 1)
    cur = ct.copy()
    for r in range(1, R + 1):
        f += 2.0 * float(c[r]) * cur
        pm, cur = cur, 2.0 * ct * cur - pm
    return th, f


def symbol_at(c, R, x):
    """f_R at a single angle x (direct cosine sum)."""
    r = np.arange(1, R + 1)
    return float(c[0] + 2.0 * np.dot(np.asarray(c[1:R + 1], float),
                                     np.cos(r * x)))


def mode_readings(c, n, fejer):
    """the symbol readings f_{2(n-1)}(pi k / n) at the active
    parity grid k = 1..n-1, via one real FFT of length 2n; the
    fejer flag applies the Cesaro damping (1 - r/(R+1))."""
    R = 2 * (n - 1)
    g = np.zeros(2 * n)
    g[0] = float(c[0])
    if R >= 1:
        coef = 2.0 * np.asarray(c[1:R + 1], float)
        if fejer:
            coef = coef * (1.0 - np.arange(1, R + 1) / (R + 1.0))
        g[1:R + 1] = coef
    return np.fft.rfft(g).real[1:n]


def neg_zones(c, R, G):
    """the negative zones of f_R on [0, pi]: sealed grid scan +
    bisection refinement at every sign change; returns a list of
    (a, b) intervals plus the grid minimum."""
    th, f = symbol_grid(c, R, G)
    zones = []
    inside = bool(f[0] < 0.0)
    start = 0.0 if inside else None
    for i in range(G):
        fa, fb = float(f[i]), float(f[i + 1])
        if (fa < 0.0) != (fb < 0.0):
            lo, hi = float(th[i]), float(th[i + 1])
            neg_lo = fa < 0.0
            for _ in range(BIS_IT):
                mid = 0.5 * (lo + hi)
                if (symbol_at(c, R, mid) < 0.0) == neg_lo:
                    lo = mid
                else:
                    hi = mid
            edge = 0.5 * (lo + hi)
            if inside:
                zones.append((start, edge))
                inside = False
            else:
                start = edge
                inside = True
    if inside:
        zones.append((start, math.pi))
    return zones, float(np.min(f))


def zone_grid_stats(zones, n):
    """the sealed zone/grid geometry at section size n: the
    active grid pi k / n (k = 1..n-1), #modes inside zones and
    the minimum zone-to-grid distance in mode-spacing units
    (None if no zones)."""
    if n < 2:
        return 0, None
    grid = math.pi * np.arange(1, n) / n
    spacing = math.pi / n
    n_in = 0
    dmin = None
    for (a, b) in zones:
        inside = np.sum((grid >= a) & (grid <= b))
        n_in += int(inside)
        d = np.min(np.maximum.reduce([a - grid, grid - b,
                                      np.zeros_like(grid)]))
        d = float(d) / spacing
        dmin = d if dmin is None else min(dmin, d)
    return n_in, dmin


def predictor_scan(c, nmax):
    """the sealed blind predictor: first n in [2, nmax] whose
    active-grid reading dips negative -- PRIMARY Fejer variant
    and SECONDARY Dirichlet variant, both frozen; consumes the
    moment array only."""
    npf = npd = None
    for n in range(2, nmax + 1):
        if npd is None:
            fr = mode_readings(c, n, fejer=False)
            if fr.size and float(np.min(fr)) < 0.0:
                npd = n
        if npf is None:
            ff = mode_readings(c, n, fejer=True)
            if ff.size and float(np.min(ff)) < 0.0:
                npf = n
        if npf is not None and npd is not None:
            break
    return npf, npd


def golden_coeffs(n, s):
    """deterministic world-blind coefficient draw s on n degrees
    (r334 verbatim), normalized to ||c|| = 1."""
    i = np.arange(1, n + 1, dtype=float)
    c = 2.0 * np.mod(i * GOLDEN + float(s) * GOLDEN * GOLDEN,
                     1.0) - 1.0
    return c / float(np.linalg.norm(c))


# ============== must-fail mutants
def mutant_odd_parity(c, n):
    """m1 MUST-FAIL: the WRONG parity convolution -- the odd
    sector matrix (c_{|k-l|} - c_{k+l})/2 (the v549 T-H object);
    must break the exact identity."""
    idx = list(range(n))
    return [[(c[abs(k - l)] - c[k + l]) / 2 for l in idx]
            for k in idx]


def mutant_pred_oracle():
    """m2 MUST-FAIL: a 'predictor' oriented by the withheld
    lambda record -- the scope audit must FLAG this."""
    return int(round(math.pi / math.acos(0.5 * (1.0 + REC_LAM))))


def mutant_unmapped_moments(tu_raw, wu, R):
    """m3 MUST-FAIL: cosine moments at arccos of the UNMAPPED
    atoms (no affine normalization) -- mixed with the mapped
    basis this must break the exact identity."""
    return [sum(w * _frac_cheb(t, R)[r] for t, w in zip(tu_raw, wu))
            for r in range(R + 1)]


def mutant_fejer_bysight(c, nmax, cross_true):
    """m4 MUST-FAIL: the Fejer order chosen by sight against the
    withheld crossing -- the scope audit must FLAG this."""
    for R in range(2, 4 * nmax):
        g = np.zeros(2 * cross_true)
        g[0] = c[0]
        if float(np.min(np.fft.rfft(g).real)) >= 0.0:
            return R
    return None


# ============== exact Fraction machinery (gate-side)
def _frac_cheb(t, K):
    """T_0..T_K at rational t (exact recurrence)."""
    out = [Fr(1), Fr(t)]
    for _k in range(2, K + 1):
        out.append(2 * t * out[-1] - out[-2])
    return out[:K + 1]


def toy_pack():
    """the sealed exact toy: union atoms, signed weights, mapped
    positions, exact moments to R = 2(N-1), N = 4."""
    atoms = ([(t, w) for t, w in TOY_MU]
             + [(t, -w) for t, w in TOY_NU])
    atoms.sort(key=lambda p: p[0])
    ts = [p[0] for p in atoms]
    ws = [p[1] for p in atoms]
    lo, hi = ts[0], ts[-1]
    tm = [(2 * t - (lo + hi)) / (hi - lo) for t in ts]
    N = (len(ts) + 1) // 2
    R = 2 * (N - 1)
    cheb = [_frac_cheb(t, R) for t in tm]
    c = [sum(w * cheb[j][r] for j, w in enumerate(ws))
         for r in range(R + 1)]
    return ts, ws, tm, N, R, cheb, c


def frac_form_direct(ws, cheb, a):
    """exact LHS: sum_j w_j (sum_k a_k T_k(t_j))^2."""
    tot = Fr(0)
    for j, w in enumerate(ws):
        pj = sum(a[k] * cheb[j][k] for k in range(len(a)))
        tot += w * pj * pj
    return tot


def frac_form_matrix(c, a):
    """exact RHS: sum_{k,l} a_k a_l (c_{|k-l|} + c_{k+l})/2."""
    n = len(a)
    tot = Fr(0)
    for k in range(n):
        for l in range(n):
            tot += a[k] * a[l] * (c[abs(k - l)] + c[k + l]) / 2
    return tot


# ============== gate-side world machinery
def world_signed_union(tag, xu, wu, N, L):
    """gate-side bundle: mapped angles, moments to 2(N+PAD-1),
    predictor scan, N_w anatomy inputs."""
    theta, tmap, hull = affine_theta(xu)
    nmax = 2 * N + PAD
    Rmax = 2 * (nmax - 1)
    c = cos_moments(theta, wu, Rmax)
    return dict(tag=tag, xu=np.asarray(xu, float),
                wu=np.asarray(wu, float), N=N, L=L, theta=theta,
                hull=hull, c=c, nmax=nmax)


def anatomy(Wd):
    """gate-side N_w anatomy of one world: zones, K-stats, mode
    readings, predictor."""
    N = Wd["N"]
    c = Wd["c"]
    R = 2 * (N - 1)
    zones, fmin = neg_zones(c, R, TH_GRID)
    n_in, dmin = zone_grid_stats(zones, N)
    fd = mode_readings(c, N, fejer=False)
    ff = mode_readings(c, N, fejer=True)
    c0 = float(c[0])
    kp1 = sum(b - a for a, b in zones) / math.pi
    kp3 = float(np.min(ff)) / c0
    blk_d = int(np.sum(fd < 0.0))
    blk_f = int(np.sum(ff < 0.0))
    rest = ff[ff >= 0.0]
    rest_floor = (float(np.min(rest)) / c0) if rest.size else None
    npf, npd = predictor_scan(c, Wd["nmax"])
    return dict(zones=zones, fmin=fmin, kp1=kp1, kp2=n_in,
                kp3=kp3, kp4=dmin, blk_d=blk_d, blk_f=blk_f,
                rest_floor=rest_floor, npf=npf, npd=npd,
                kmin=int(np.argmin(ff)) + 1)


def dist_rule(tab, deads):
    """sealed r281 distance rule: MAIN_SEPARATING iff MAIN's
    value is farther from EVERY dead value than the dead
    spread."""
    vm = tab.get("MAIN")
    vd = [tab[c] for c in deads
          if tab.get(c) is not None and math.isfinite(tab[c])]
    if vm is None or not math.isfinite(vm) or not vd:
        return "WORLD_BLIND"
    spread = max(vd) - min(vd)
    dm = min(abs(vm - v) for v in vd)
    return ("MAIN_SEPARATING" if (spread > 0 and dm >= spread)
            else "WORLD_BLIND")


def identity_check(Wd, degs, draws):
    """f64 T+H identity on the sealed coefficient family: max rel
    dev of a^T M a against the direct signed atom sum, measured
    on the absolute-mass scale."""
    N = Wd["N"]
    c = Wd["c"]
    M = th_matrix(c, N)
    theta = Wd["theta"]
    wu = Wd["wu"]
    K = np.cos(np.outer(np.arange(N), theta))     # (N, S)
    fam = []
    for d in sorted(set(int(x) for x in degs if 0 < int(x) < N)):
        a = np.zeros(N)
        a[d] = 1.0
        fam.append(("D%d" % d, a))
    for s in range(1, draws + 1):
        fam.append(("R%d" % s, golden_coeffs(N, s)))
    dev = 0.0
    for _nm, a in fam:
        pv = a @ K
        lhs = float(np.dot(wu, pv * pv))
        scale = float(np.dot(np.abs(wu), pv * pv))
        rhs = float(a @ (M @ a))
        dev = max(dev, abs(lhs - rhs) / max(scale, 1e-300))
    return dev, len(fam)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("lstar_parity_section_probe -- PRIME.LSTAR.PARITY_SECTION.01 "
          "(round 336)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 f64 block; ladder, controls, twin, "
                        "world rule, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the symbol convention "
          "(Dirichlet partial sum at R(n) = 2(n-1)), the active "
          "parity grid pi k/n with both endpoints excluded, the "
          "Fejer-PRIMARY / Dirichlet-SECONDARY predictor split, "
          "the four world statistics K_P1..K_P4, the r281 "
          "distance rule, the band %.1f / spearman %.2f "
          "adjudication, every bar/tolerance, the mutants and "
          "the verdict form; the STOP list forbids any L* claim "
          "and any step-over certificate reading" % (BAND, SP_BAR))

    # ---------------- S1 exact toys
    section("S1  TOYS -- EXACT T+H IDENTITY + PARITY DILATATION")
    ts, ws, tm, N_t, R_t, cheb_t, c_t = toy_pack()
    a_t = list(TOY_A)
    lhs_t = frac_form_direct(ws, cheb_t, a_t)
    rhs_t = frac_form_matrix(c_t, a_t)
    check("G10-toy-exact-identity", lhs_t == rhs_t,
          "EXACT FRACTIONS on the sealed 7-atom toy (hull "
          "[-3/4, 3/4] mapped to [-1, 1], N = %d, R = %d): "
          "int p^2 d(mu - nu) == a^T M a BIT-EQUAL, value %s "
          "(c_0 = %s, c_1 = %s) -- the Chebyshev T+H "
          "representation is exact, not asymptotic"
          % (N_t, R_t, str(lhs_t), str(c_t[0]), str(c_t[1])))
    # parity dilatation: M == S V+^T T_7(c) V+ S exactly
    Mm = 2 * N_t - 1
    idxs = list(range(-(N_t - 1), N_t))
    T7 = [[c_t[abs(i - j)] for j in idxs] for i in idxs]
    ok_dil = True
    for k in range(N_t):
        for l in range(N_t):
            vk = [(1 if abs(i) == k else 0) for i in idxs] \
                if k > 0 else [(1 if i == 0 else 0) for i in idxs]
            vl = [(1 if abs(j) == l else 0) for j in idxs] \
                if l > 0 else [(1 if j == 0 else 0) for j in idxs]
            comp = sum(vk[i] * T7[i][j] * vl[j]
                       for i in range(Mm) for j in range(Mm))
            sk = Fr(1) if k == 0 else Fr(1, 2)
            sl = Fr(1) if l == 0 else Fr(1, 2)
            target = (c_t[abs(k - l)] + c_t[k + l]) / 2
            ok_dil = ok_dil and (sk * comp * sl == target)
    ok_odd = True
    for k in range(1, N_t):
        for l in range(1, N_t):
            vk = [(1 if i == k else (-1 if i == -k else 0))
                  for i in idxs]
            vl = [(1 if j == l else (-1 if j == -l else 0))
                  for j in idxs]
            comp = sum(vk[i] * T7[i][j] * vl[j]
                       for i in range(Mm) for j in range(Mm))
            ok_odd = ok_odd and (comp == 2 * (c_t[abs(k - l)]
                                              - c_t[k + l]))
    check("G11-toy-parity-dilatation", ok_dil and ok_odd,
          "C1 EXACT on the toy (T_%d(c) full symmetric Toeplitz, "
          "indices -%d..%d): M == S (V_+^T T V_+) S elementwise "
          "in Fractions (S = diag(1, 1/2, 1/2, 1/2), V_+ the "
          "unnormalized EVEN parity columns) -- the L* matrix IS "
          "the even parity compression; beside it the ODD "
          "compression == 2(c_{|k-l|} - c_{k+l}) exactly = the "
          "v549 T-H object, a DIFFERENT matrix (the m1 mutant "
          "below breaks the identity with it)"
          % (Mm, N_t - 1, N_t - 1))
    # zone toys (closed-form edges)
    z1, _f1 = neg_zones(np.array([1.0, -1.0]), 1, 2048)
    z2, _f2 = neg_zones(np.array([1.0, 1.0]), 1, 2048)
    z3, _f3 = neg_zones(np.array([0.1, 0.0, -1.0]), 2, 2048)
    e1 = math.acos(0.5)
    e2 = math.pi - math.acos(0.5)
    e3a = 0.5 * math.acos(0.05)
    e3b = math.pi - 0.5 * math.acos(0.05)
    ok_z = (len(z1) == 1 and abs(z1[0][0]) <= EDGE_TOL
            and abs(z1[0][1] - e1) <= EDGE_TOL
            and len(z2) == 1 and abs(z2[0][0] - e2) <= EDGE_TOL
            and abs(z2[0][1] - math.pi) <= EDGE_TOL
            and len(z3) == 2
            and abs(z3[0][1] - e3a) <= EDGE_TOL
            and abs(z3[1][0] - e3b) <= EDGE_TOL)
    check("G12-toy-zone-edges", ok_z,
          "ZONE FINDER vs closed forms: f = 1 - 2cos(theta) zone "
          "[0, pi/3] (edge dev %.1e), f = 1 + 2cos(theta) zone "
          "[2pi/3, pi] (dev %.1e), f = 1/10 - 2cos(2 theta) two "
          "zones with edges acos(1/20)/2 and pi - acos(1/20)/2 "
          "(devs %.1e / %.1e; bar %.0e)"
          % (abs(z1[0][1] - e1), abs(z2[0][0] - e2),
             abs(z3[0][1] - e3a), abs(z3[1][0] - e3b), EDGE_TOL))
    c_toy = np.array([float(x) for x in c_t])
    dev_fft = 0.0
    for n in range(2, 2 * N_t + 5):
        cc = cos_moments(np.arccos(np.array(
            [float(t) for t in tm])), np.array(
            [float(w) for w in ws]), 2 * (n - 1))
        for fejer in (False, True):
            fr = mode_readings(cc, n, fejer)
            grid = math.pi * np.arange(1, n) / n
            R = 2 * (n - 1)
            damp = (1.0 - np.arange(1, R + 1) / (R + 1.0)) \
                if fejer else np.ones(R)
            direct = np.array(
                [cc[0] + 2.0 * float(np.dot(
                    cc[1:R + 1] * damp,
                    np.cos(np.arange(1, R + 1) * g)))
                 for g in grid]) if R >= 1 else np.array(
                [cc[0]] * len(grid))
            if fr.size:
                dev_fft = max(dev_fft, float(np.max(
                    np.abs(fr - direct)))
                    / max(float(np.max(np.abs(direct))), 1e-300))
    check("G13-toy-fft-crossroute", dev_fft <= FFT_TOY,
          "FFT MODE READINGS == direct cosine sums on the toy, "
          "n = 2..%d, Dirichlet + Fejer: max rel dev %.1e "
          "(bar %.0e)" % (2 * N_t + 4, dev_fft, FFT_TOY))

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + CHANNEL GATE + IDENTITY + FLIP")
    mz9 = V.build_measures(MAIN_KZ)
    lam184, _B = V.lam_max_at(mz9, REC_NW)
    lam185, _B2 = V.lam_max_at(mz9, REC_NW + 1)
    ok_rec = (mz9["S"] == REC_S and len(mz9["xp"]) == REC_SP
              and len(mz9["yn"]) == REC_SM and mz9["Nw"] == REC_NW
              and abs(lam184 - REC_LAM) <= 1e-6
              and abs(lam185 - REC_LAM_NEXT) <= 1e-6
              and abs((1.0 - lam184) / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL)
    check("G20-w9-records", ok_rec,
          "w9: S = %d (mu %d / nu %d), N_w = %d, "
          "lambda_max(E_184) = %.8f (record %.8f), margin %.4e "
          "(record %.4e rel %.2f), lambda at 185 = %.8f > 1 -- "
          "the r283/r284 route reproduced through the document "
          "pipeline" % (mz9["S"], len(mz9["xp"]), len(mz9["yn"]),
                        mz9["Nw"], lam184, REC_LAM, 1.0 - lam184,
                        REC_MARGIN, REC_MARGIN_TOL, lam185))
    ctx9 = MS.ctx_build(MAIN_KZ)
    xu_b, wu_b, _zones_b = BL.union_of_ctx(ctx9)
    sg9 = BL.sign_chain_f64(xu_b, wu_b, ctx9["N"] + EXT)[0]
    minC9 = next((n for n in range(len(sg9)) if sg9[n] < 0), None)
    scale_w = float(np.max(np.abs(mz9["wu"])))
    dev_x = float(np.max(np.abs(np.sort(xu_b) - np.sort(mz9["xu"]))))
    dev_w = float(np.max(np.abs(np.sort(wu_b)
                                - np.sort(mz9["wu"])))) / scale_w
    # r284 shallow-edge anchor: two smallest-theta nu atoms
    by, _bv, ufn = PIK.folded_measure(ctx9["darm"], ctx9["L"], -1.0)
    o_desc = np.argsort(by)[::-1]                # largest x first
    shallow = tuple(int(ufn[o_desc[t]]) for t in range(2))
    check("G21-w9-channel-gate", minC9 == REC_NW + MINC_OFF9
          and dev_x <= XCHAN_TOL and dev_w <= XCHAN_TOL
          and shallow == SHALLOW_FOLDS,
          "campaign channel: BL union == V union (pos dev %.1e, "
          "rel weight dev %.1e, bar %.0e), minC = %s == 184 "
          "(crossing 185 = minC + 1, the r283 dictionary); the "
          "two smallest-theta nu atoms are folds %s == r284 "
          "shallow-edge record"
          % (dev_x, dev_w, XCHAN_TOL, str(minC9), str(shallow)))
    W9 = world_signed_union("MAIN", mz9["xu"], mz9["wu"],
                            mz9["Nw"], mz9["L"])
    dev_id9, nfam9 = identity_check(
        W9, (1, 2, 3, REC_NW // 2, REC_NW - 1), GOLDEN_DRAWS)
    check("G22-w9-identity", dev_id9 <= ID_TOL,
          "f64 T+H IDENTITY on w9 (sealed family, %d members: "
          "Chebyshev units d in {1, 2, 3, N/2, N-1} + %d golden "
          "draws): max rel dev %.1e on the absolute-mass scale "
          "(bar %.0e) -- kill test 1, f64 half"
          % (nfam9, GOLDEN_DRAWS, dev_id9, ID_TOL))
    M184 = th_matrix(W9["c"], REC_NW)
    M185 = th_matrix(W9["c"], REC_NW + 1)
    ev184 = np.linalg.eigvalsh(M184)
    ev185 = np.linalg.eigvalsh(M185)
    nrm = float(np.max(np.abs(ev184)))
    tolm = EIG_TOL_FACT * nrm
    mn184, mn185 = float(ev184[0]), float(ev185[0])
    n_neg185 = int(np.sum(ev185 < 0.0))
    ok_flip = (mn184 > -tolm) and (mn185 < tolm)
    check("G23-w9-section-flip", ok_flip,
          "SECTION FLIP at f64: min eig M_184 = %+.1e, min eig "
          "M_185 = %+.1e (||M|| = %.2f, resolution %.1e; "
          "negative inertia at 185: %d) -- signs %s; the PD "
          "statement itself is carried by the r283-gated "
          "crossing 185 (G21), the f64 eigenvalues are the "
          "illustration (disclosed)"
          % (mn184, mn185, nrm, tolm, n_neg185,
             "CLEAN" if (mn184 > 0.0 and mn185 < 0.0)
             else "WITHIN TOLERANCE (disclosed)"))
    dev_fft9 = 0.0
    for n in (20, 120, REC_NW):
        for fejer in (False, True):
            fr = mode_readings(W9["c"], n, fejer)
            grid = math.pi * np.arange(1, n) / n
            R = 2 * (n - 1)
            damp = (1.0 - np.arange(1, R + 1) / (R + 1.0)) \
                if fejer else np.ones(R)
            direct = np.array(
                [W9["c"][0] + 2.0 * float(np.dot(
                    W9["c"][1:R + 1] * damp,
                    np.cos(np.arange(1, R + 1) * g)))
                 for g in grid])
            dev_fft9 = max(dev_fft9, float(np.max(
                np.abs(fr - direct)))
                / max(float(np.max(np.abs(direct))), 1e-300))
    AN9 = anatomy(W9)
    th1 = math.pi / REC_NW
    # mapped angles of the shallow-edge nu atoms (folds 2, 4)
    lo9, hi9 = W9["hull"]
    th_sh = []
    for f in SHALLOW_FOLDS:
        xf = math.cos(2.0 * math.pi * f / W9["L"])
        tf = (2.0 * xf - (lo9 + hi9)) / (hi9 - lo9)
        th_sh.append(math.acos(max(-1.0, min(1.0, tf))))
    check("G24-w9-fft-crossroute", dev_fft9 <= FFT_W9,
          "FFT MODE READINGS == direct sums on w9 at n = 20 / "
          "120 / 184 (both variants): max rel dev %.1e (bar "
          "%.0e)" % (dev_fft9, FFT_W9))
    info("w9 anatomy at N_w = %d (R = %d): %d negative zones, "
         "total measure %.4f pi, grid min %+.3e"
         % (REC_NW, 2 * (REC_NW - 1), len(AN9["zones"]),
            AN9["kp1"], AN9["fmin"]))
    if AN9["zones"]:
        za, zb = AN9["zones"][0]
        info("w9 first zone [%.4e, %.4e]; theta_1 = pi/184 = "
             "%.4e; shallow-edge nu atoms (folds %s) at mapped "
             "theta %.4e / %.4e"
             % (za, zb, th1, str(SHALLOW_FOLDS), th_sh[0],
                th_sh[1]))
    info("w9 K-stats: K_P1 %.4f, K_P2 %d of %d, K_P3 %+.3e "
         "(min at mode k = %d), K_P4 %s; blocks D/F %d/%d, rest "
         "floor %s; predictor PRIMARY n_pred = %s, SECONDARY = "
         "%s (crossing 185)"
         % (AN9["kp1"], AN9["kp2"], REC_NW - 1, AN9["kp3"],
            AN9["kmin"], str(AN9["kp4"]), AN9["blk_d"],
            AN9["blk_f"], str(AN9["rest_floor"]),
            str(AN9["npf"]), str(AN9["npd"])))
    for n in (20, 120, 183, 184, 185, 186, 190):
        ff = mode_readings(W9["c"], n, fejer=True)
        info("w9 Fejer floor at n = %3d: %+.3e (argmin k = %d)"
             % (n, float(np.min(ff)) / W9["c"][0],
                int(np.argmin(ff)) + 1))

    # ---------------- S3 controls + twin + world rule
    section("S3  LEG B -- CONTROLS + TWIN + WORLD RULE")
    if smoke:
        for g in ("G30-controls", "G31-twin", "G32-world-rule"):
            check(g, True, "SMOKE: skipped")
        ANC = {}
        world_verdict = None
        geo_typ = {}
        ANT = None
        twin_txt = ""
    else:
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        gpc = PC.Grid()
        comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)))
        ANC = {}
        WC = {}
        ok_ctrl = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            xu, wu, zones = BL.union_of_ctx(cctx)
            N_c = cctx["N"]
            sg = BL.sign_chain_f64(xu, wu, N_c + EXT)[0]
            mc = next((n for n in range(len(sg)) if sg[n] < 0),
                      None)
            if mc is None:
                sg = BL.sign_chain_f64(xu, wu, N_c + EXT2)[0]
                mc = next((n for n in range(len(sg)) if sg[n] < 0),
                          None)
            flip = CTRL_FLIPS.get(cn, HL2_FLIP)
            ok_ctrl = ok_ctrl and (mc == flip)
            xs_z, ws_z, ys_z, vs_z = zones
            dep = min(CTRL_DEPTH, len(xs_z) - 1)
            al, sb, h0 = FS.mu_chain_f64(np.asarray(xs_z),
                                         np.asarray(ws_z), dep)
            Bc = FS.b_matrix_f64(al, sb, h0, np.asarray(ys_z),
                                 np.asarray(vs_z), dep)
            crossc, _rho = FS.crossing_from_B(Bc, dep)
            ok_ctrl = ok_ctrl and (crossc == CTRL_CROSS[cn])
            Wd = world_signed_union(cn, xu, wu, N_c,
                                    int(cctx["L"]))
            an = anatomy(Wd)
            an["cross"] = crossc
            ANC[cn] = an
            WC[cn] = Wd
            info("%s (S %d, N_w %d, minC %s, crossing %s): "
                 "K_P1 %.4f, K_P2 %d, K_P3 %+.3e, K_P4 %s; "
                 "blocks D/F %d/%d of %d, rest floor %s; n_pred "
                 "F/D = %s/%s"
                 % (cn, len(xu), N_c, str(mc), str(crossc),
                    an["kp1"], an["kp2"], an["kp3"],
                    str(an["kp4"]), an["blk_d"], an["blk_f"],
                    N_c - 1, str(an["rest_floor"]),
                    str(an["npf"]), str(an["npd"])))
        check("G30-controls", ok_ctrl,
              "EPST + SCR + SMOOTH + HL2 built verbatim through "
              "the r278/r280 channel: minC == flips %s + HL2 %d; "
              "spectral crossings == r284 record %s (depth %d)"
              % (str(CTRL_FLIPS), HL2_FLIP, str(CTRL_CROSS),
                 CTRL_DEPTH))
        # rational twin
        uu9, mm9 = TR.base_comb(9)
        mzD = TR.build_world(9, uu9, mm9)
        ok_dose0 = (np.array_equal(mzD["xp"], mz9["xp"])
                    and np.array_equal(mzD["wp"], mz9["wp"])
                    and np.array_equal(mzD["yn"], mz9["yn"])
                    and np.array_equal(mzD["vn"], mz9["vn"]))
        gaps9 = MF.local_gaps(uu9)
        u2, m2, _dens, _du = AKD.twin_rational(uu9, mm9, gaps9,
                                               mz9["D"], TWIN_TOL)
        mzT = TR.build_world(9, u2, m2)
        xuT = np.concatenate([mzT["xp"], mzT["yn"]])
        wuT = np.concatenate([mzT["wp"], -np.asarray(mzT["vn"])])
        oT = np.argsort(xuT)
        WT = world_signed_union("TWIN", xuT[oT], wuT[oT],
                                mzT["Nw"], mzT["L"])
        ANT = anatomy(WT)
        d1 = abs(ANT["kp1"] - AN9["kp1"]) / max(AN9["kp1"], 1e-300)
        d3 = abs(ANT["kp3"] - AN9["kp3"]) / max(abs(AN9["kp3"]),
                                                1e-300)
        ok_twin = (ok_dose0 and ANT["kp2"] == AN9["kp2"]
                   and d1 <= TWIN_BAR and d3 <= TWIN_BAR
                   and ANT["npf"] == AN9["npf"])
        twin_txt = ("K_P1 dev %.1e, K_P2 %d == %d, K_P3 dev "
                    "%.1e (bar %.0e), n_pred %s == %s"
                    % (d1, ANT["kp2"], AN9["kp2"], d3, TWIN_BAR,
                       str(ANT["npf"]), str(AN9["npf"])))
        check("G31-twin", ok_twin,
              "RATIONAL TWIN at tol %.0e (r289/r331 verbatim; "
              "dose-zero identity TR.build_world == "
              "V.build_measures BITWISE %s): the parity anatomy "
              "is twin-stable -- %s"
              % (TWIN_TOL, ok_dose0, twin_txt))
        deads = ["EPST", "SCR", "SMOOTH", "HL2"]
        geo_typ = {}
        for nm, key in (("K_P1_zonefrac", "kp1"),
                        ("K_P2_modes_in", "kp2"),
                        ("K_P3_fejer_floor", "kp3"),
                        ("K_P4_zone_dist", "kp4")):
            tab = {"MAIN": AN9[key]}
            for cn in deads:
                tab[cn] = ANC[cn][key]
            tab = {k: (float(v) if v is not None else None)
                   for k, v in tab.items()}
            geo_typ[nm] = (dist_rule(tab, deads), tab)
        world_verdict = ("PARITY_WORLD_SEEN"
                         if any(t[0] == "MAIN_SEPARATING"
                                for t in geo_typ.values())
                         else "PARITY_WORLD_BLIND")
        sign_note = ("Fejer-floor SIGNS: MAIN %+d TWIN %+d vs "
                     "dead %s"
                     % (1 if AN9["kp3"] > 0 else -1,
                        1 if ANT["kp3"] > 0 else -1,
                        str({cn: ("+" if ANC[cn]["kp3"] > 0
                                  else "-") for cn in deads})))
        check("G32-world-rule", True,
              "KILL TEST 2 (sealed r281 distance rule): %s -- "
              "per statistic: %s; %s"
              % (world_verdict,
                 str({nm: (t[0], {k: (round(v, 4)
                                      if v is not None else None)
                                  for k, v in t[1].items()})
                      for nm, t in geo_typ.items()}), sign_note))

    # ---------------- S4 ladder + predictor census
    section("S4  LEG C -- LADDER CENSUS + BLIND PREDICTOR")
    if smoke:
        for g in ("G40-ladder-census", "G41-predictor-census",
                  "G42-step-over", "G43-ladder-identity",
                  "G44-schur-ledger"):
            check(g, True, "SMOKE: skipped")
        pred_verdict = None
        pred_detail = ""
        step_verdict = None
        step_detail = ""
        schur_txt = ""
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        cens = {}
        ok_hf = True
        for kz in kzs:
            ctx = ctx9 if kz == 9 else MS.ctx_build(kz)
            xu, wu, _z = BL.union_of_ctx(ctx)
            N_ = ctx["N"]
            sg = BL.sign_chain_f64(xu, wu, N_ + EXT)[0]
            mc = next((n for n in range(len(sg)) if sg[n] < 0),
                      None)
            if mc is None:
                sg = BL.sign_chain_f64(xu, wu, N_ + EXT2)[0]
                mc = next((n for n in range(len(sg)) if sg[n] < 0),
                          None)
            S_ = len(xu)
            ok_hf = ok_hf and (N_ == (S_ + 1) // 2)
            Wd = W9 if kz == 9 else world_signed_union(
                "kz%d" % kz, xu, wu, N_, int(ctx["L"]))
            npf, npd = ((AN9["npf"], AN9["npd"]) if kz == 9
                        else predictor_scan(Wd["c"], Wd["nmax"]))
            ffN = mode_readings(Wd["c"], N_, fejer=True)
            fdN = mode_readings(Wd["c"], N_, fejer=False)
            cens[kz] = dict(N=N_, S=S_, minC=mc, off=mc - N_,
                            cross=mc + 1, npf=npf, npd=npd,
                            floor=float(np.min(ffN)) / Wd["c"][0],
                            blk_f=int(np.sum(ffN < 0.0)),
                            blk_d=int(np.sum(fdN < 0.0)),
                            Wd=Wd)
        dist = {}
        for kz in cens:
            o = cens[kz]["off"]
            dist[o] = dist.get(o, 0) + 1
        ok_anch = all(cens[kz]["off"] == ANCHORS[kz]
                      for kz in ANCHORS if kz in cens)
        check("G40-ladder-census", len(cens) == 42 and ok_hf
              and ok_anch and dist == R281_DIST,
              "42-rung census (r281 channel): offset distribution "
              "%s == r281 record, anchors exact, half-filling "
              "42/42; crossing = minC + 1 consumed as the r283 "
              "dictionary" % str({("+%d" % k): dist[k]
                                  for k in sorted(dist)}))
        # predictor adjudication (PRIMARY Fejer)
        worlds = {("kz%d" % kz): (cens[kz]["npf"],
                                  cens[kz]["npd"],
                                  cens[kz]["cross"])
                  for kz in sorted(cens)}
        for cn in ANC:
            worlds[cn] = (ANC[cn]["npf"], ANC[cn]["npd"],
                          ANC[cn]["cross"])
        devs_f = {}
        breaks = []
        for wn, (npf, _npd, cr) in worlds.items():
            if npf is None:
                devs_f[wn] = None
                breaks.append("%s None vs %d" % (wn, cr))
            else:
                d = abs(math.log2(npf / cr))
                devs_f[wn] = d
                if d > BAND:
                    breaks.append("%s %d vs %d (%.2f)"
                                  % (wn, npf, cr, d))
        n_in_rung = sum(1 for wn, d in devs_f.items()
                        if wn.startswith("kz") and d is not None
                        and d <= BAND)
        n_in_ctrl = sum(1 for wn in ANC
                        if devs_f[wn] is not None
                        and devs_f[wn] <= BAND)
        fin = [(worlds[wn][0], worlds[wn][2])
               for wn in worlds if worlds[wn][0] is not None]
        sp = BH.spearman([t[0] for t in fin], [t[1] for t in fin]) \
            if len(fin) >= 3 else 0.0
        max_rung_dev = max([d for wn, d in devs_f.items()
                            if wn.startswith("kz")
                            and d is not None] or [float("inf")])
        if not breaks:
            pred_verdict = "PREDICTOR_LAW"
            pred_detail = "max band dev %.3f on all 46" \
                % max(d for d in devs_f.values())
        elif abs(sp) >= SP_BAR:
            pred_verdict = "PREDICTOR_ORDERING"
            pred_detail = ("spearman %+.3f over %d finite "
                           "predictions; rungs in band %d/42 "
                           "(max rung dev %.3f), controls in "
                           "band %d/4; HONEST: when the controls "
                           "fail the band the ordering rides the "
                           "trivial N_w scaling of the ladder"
                           % (sp, len(fin), n_in_rung,
                              max_rung_dev, n_in_ctrl))
        else:
            pred_verdict = "PREDICTOR_REFUTED"
            pred_detail = "break loci: " + "; ".join(breaks[:8])
        npd_fired_early = sum(1 for wn in worlds
                              if worlds[wn][1] is not None
                              and worlds[wn][1] <= 4)
        # the gate adjudicates the sealed PRIMARY variant; the
        # Dirichlet SECONDARY is printed and typed, never gated.
        ok_pred_gate = (pred_verdict in
                        ("PREDICTOR_LAW", "PREDICTOR_ORDERING",
                         "PREDICTOR_REFUTED"))
        check("G41-predictor-census", ok_pred_gate,
              "KILL TEST 3 (PRIMARY Fejer, sealed): %s(%s); "
              "controls (n_pred vs crossing): %s; w9 %s vs 185; "
              "SECONDARY Dirichlet: fires at n <= 4 on %d/46 "
              "worlds (GIBBS_EARLY, printed not adjudicated)"
              % (pred_verdict, pred_detail,
                 str({cn: (worlds[cn][0], worlds[cn][2])
                      for cn in ANC}),
                 str(AN9["npf"]), npd_fired_early))
        # step-over clauses at N_w on MAIN + TWIN
        cl_i = (AN9["kp2"] == 0) and (ANT["kp2"] == 0)
        cl_ii = (AN9["kp3"] > 0.0) and (ANT["kp3"] > 0.0)
        if cl_i or cl_ii:
            step_verdict = "NEGATIVE_WINDOW_STEP_OVER"
            step_detail = ("clauses fired: %s%s -- MAIN K_P2 %d "
                           "K_P3 %+.2e, TWIN K_P2 %d K_P3 %+.2e"
                           % ("i " if cl_i else "",
                              "ii" if cl_ii else "",
                              AN9["kp2"], AN9["kp3"],
                              ANT["kp2"], ANT["kp3"]))
        else:
            step_verdict = "NO_STEP_OVER"
            step_detail = ("MAIN K_P2 %d K_P3 %+.2e, TWIN K_P2 "
                           "%d K_P3 %+.2e"
                           % (AN9["kp2"], AN9["kp3"],
                              ANT["kp2"], ANT["kp3"]))
        check("G42-step-over", True,
              "STEP-OVER at n = N_w (sealed clauses): %s(%s)"
              % (step_verdict, step_detail))
        # ladder identity sample (kill test 1, ladder half)
        skz = sorted(cens, key=lambda k: (cens[k]["N"], k))
        sample = [skz[0], skz[len(skz) // 2], skz[-1]]
        dev_lad = 0.0
        for kz in sample:
            Wd = cens[kz]["Wd"]
            dv, _nf = identity_check(
                Wd, (1, Wd["N"] // 2, Wd["N"] - 1), 1)
            dev_lad = max(dev_lad, dv)
            info("identity kz%d (N_w %d): max rel dev %.1e"
                 % (kz, Wd["N"], dv))
        check("G43-ladder-identity", dev_lad <= ID_TOL,
              "f64 T+H identity on the ladder sample %s (reduced "
              "family): max rel dev %.1e (bar %.0e) -- kill test "
              "1 complete" % (str(sample), dev_lad, ID_TOL))
        # schur ledger
        pos_floor = sum(1 for kz in cens
                        if cens[kz]["floor"] > 0.0)
        blkf = sorted(cens[kz]["blk_f"] for kz in cens)
        blkd = sorted(cens[kz]["blk_d"] for kz in cens)
        min_floor = min(cens[kz]["floor"] for kz in cens)
        kz_minf = min(cens, key=lambda k: cens[k]["floor"])
        schur_txt = ("rungs: Fejer floor positive %d/42 (min "
                     "%+.2e at kz%d), Fejer block med %d / max "
                     "%d, Dirichlet block med %d / max %d; dead "
                     "controls Fejer blocks %s, rest floors %s"
                     % (pos_floor, min_floor, kz_minf,
                        blkf[21], blkf[-1], blkd[21], blkd[-1],
                        str({cn: ANC[cn]["blk_f"] for cn in ANC}),
                        str({cn: (None if ANC[cn]["rest_floor"]
                                  is None else
                                  float("%.2e"
                                        % ANC[cn]["rest_floor"]))
                             for cn in ANC})))
        check("G44-schur-ledger", True,
              "LEG D CENSUS (measurement only): %s" % schur_txt)
        info("R334 COMPARISON COLUMN (record 1 - kappa_int vs "
             "the Fejer floor, both source-pure near-wall "
             "coordinates):")
        for kz in (18, 9, 60, 52):
            if kz in cens:
                info("  kz%-3d N_w %-4d 1-kappa_int(rec) %.1e   "
                     "Fejer floor %+.2e   n_pred %s vs cross %d"
                     % (kz, cens[kz]["N"], R334_KINT[kz],
                        cens[kz]["floor"], str(cens[kz]["npf"]),
                        cens[kz]["cross"]))

    # ---------------- S5 must-fails + scopes
    section("S5  MUST-FAILS + SCOPE AUDITS")
    Modd = mutant_odd_parity(c_t, N_t)
    rhs_odd = Fr(0)
    for k in range(N_t):
        for l in range(N_t):
            rhs_odd += a_t[k] * a_t[l] * Modd[k][l]
    diff1 = lhs_t - rhs_odd
    check("G70-mutant-odd-parity", diff1 != 0,
          "m1 WRONG PARITY CONVOLUTION (the odd T-H matrix): "
          "exact difference %s != 0 -- CAUGHT in Fractions (the "
          "L* matrix is the EVEN compression, not the v549 odd "
          "one)" % str(diff1))
    c_raw = mutant_unmapped_moments(ts, ws, R_t)
    rhs_raw = frac_form_matrix(c_raw, a_t)
    diff3 = lhs_t - rhs_raw
    check("G71-mutant-unmapped", diff3 != 0,
          "m3 SYMBOL ON THE UNNORMALIZED WINDOW (arccos of the "
          "raw atoms, hull [-3/4, 3/4] not mapped): exact "
          "difference %s != 0 -- CAUGHT in Fractions (the affine "
          "normalization is load-bearing)" % str(diff3))
    hits_m2 = scope_audit("mutant_pred_oracle")
    hits_m4 = scope_audit("mutant_fejer_bysight")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G72-scope-audits", bool(hits_m2) and bool(hits_m4)
          and not hits and not ag_hits,
          "m2 PREDICTOR-READS-TARGET FLAGGED (%s); m4 "
          "FEJER-ORDER-BY-SIGHT FLAGGED (%s); the %d sealed "
          "constructors consume position / weight / moment "
          "arrays ONLY (%s); fragment audit: %s"
          % ("; ".join(hits_m2) if hits_m2 else "NOT FLAGGED",
             "; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S6 verdict
    section("S6  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "step-over promoted as a certificate, no posthoc grid "
          "or truncation variant, no derived 5/7, NO RH claim; "
          "what the round adds: the exact T+H parity-section "
          "coordinate with its rational dilatation, the "
          "world-comparative symbol anatomy, the blind Fejer "
          "predictor adjudication and the Schur-block census; "
          "r243..r335 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        neg_live = (AN9["fmin"] < 0.0) and (ANT["fmin"] < 0.0)
        if neg_live:
            primary = ("PARITY_FINITESECTION_CARRIER(f_%d min "
                       "%+.2e on MAIN / %+.2e on TWIN < 0 while "
                       "the %d-section is PD through the "
                       "r283-gated crossing %d)"
                       % (2 * (REC_NW - 1), AN9["fmin"],
                          ANT["fmin"], REC_NW, REC_NW + 1))
        else:
            primary = ("SYMBOL_RESTATEMENT(the finite symbol is "
                       "pointwise nonnegative on the live worlds "
                       "-- nothing is stepped over)")
        parts = [primary,
                 "%s(%s)" % (step_verdict, step_detail),
                 "%s(%s)" % (world_verdict,
                             str({nm: t[0]
                                  for nm, t in geo_typ.items()})),
                 "%s(%s)" % (pred_verdict, pred_detail),
                 "SCHUR_LEDGER(%s)" % schur_txt]
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED parity-section anatomy of the open "
          "scalar L*; the sealed adjudication is applied "
          "honestly; NO L* claim, NO RH claim"
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
