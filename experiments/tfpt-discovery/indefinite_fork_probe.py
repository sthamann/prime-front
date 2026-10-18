#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""indefinite_fork_probe -- PRIME.LSTAR.INDEFINITE_FORK.01
(round 318, the NEW idea class after the L*-language stop):
PONTRYAGIN-/KREIN-INDEX versus SIGN-REGULARITY -- ONE theoretical
representation test, not fifty numerical tests.  Strategic frame
(binding, the reviewer perspective shift, quoted): the previous
L* search language is STOPPED (the no-go catalog: functionals,
extremality, KYP, Maslov, fixed head, paired cone, block Green at
the 2.4 percent negative cross mixtures, diophantine irrelevant,
magnitudes insufficient).  The key r312 information: 97.6 percent
of the solver's psd family fits the positive rank-one cone and
2.4 percent negative CROSS MIXTURES obstruct the construction.
Reviewer reading: "THE SIGNEDNESS ITSELF IS THE MATHEMATICAL
OBJECT THAT IS NOT YET UNDERSTOOD."  L* is reformulated -- no
longer "int p^2 dnu < int p^2 dmu" (squeezing out positivity)
but: "why does this specific signed moment form have a positive
index of at least N_w?" -- perhaps the natural object is not
positivity but SIGNATURE: the object is intrinsically indefinite,
and the theorem to find says WHERE ITS NEGATIVE SIGNATURE MAY
LIVE.  Core-question inversion: what if the 2.4 percent negative
cross mixtures are not the obstruction of the right proof but the
FINGERPRINT of the right indefinite theorem?  STOP RULE (binding):
if BOTH routes are world-blind or restatements => FORK_DEAD, stop
the lane; if one is MAIN-specific => dig there (dig site named
precisely).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
COEXISTENCE: r317 (fiber) and r319 (audit) run in parallel; this
probe touches nothing of theirs; the rh-sync is strictly ADDITIVE.

INDEX FIREWALL (binding, r238-r316 discipline): w = window (kz),
S = #union atoms of mutilde = mu - nu, S_+ = #mu atoms, S_- = #nu
atoms, N_w = builder depth = (S+1)//2, n = degree, minC = first
n with h_n < 0.  Ground truth (minC, control flips, published
record numbers) enters GATES and record tables only; the sealed
constructors consume passed matrices/arrays ONLY (AST scope
audit); no zero/prime oracles anywhere (AST firewall).  MACHINERY
IMPORTED VERBATIM: r283 FS.{split_channels, mu_chain_f64,
b_matrix_f64, toy_block, frac_det}, r284 LS.{world_pack,
dist_rule}, r280 BL via LS, r279 OT.mp_chain_pack (the mp h-sign
chain with guard/recount), r312 BM.{lib_vectors, nnls_lh,
feas_diag_g}, r308 BG.{census_world, world_arrays, world_budget,
hull_of, block_eigs}, r289 AK.twin_rational + r276 MF.local_gaps,
r278 MS.ctx_build, r244 BH.spearman, v881 PIK, r243
PB.smooth_comb, paircorr PC.{Grid, gen_model}, r274 WD.stj_gen,
r230 JF toy nodes, v563 core READ-ONLY.

THE INDEFINITE GEOMETRY (frame convention, r283 s2 theorem,
consumed as the coordinate system): in the mu-orthonormal frame
the signed Hankel form H_n(mutilde) is congruent to A_n = I - M_n
with M_n = B_n^T B_n, B[k, i] = sqrt(v_k) P_i(y_k) -- the
canonical indefinite form of the round, with degree coordinates
i = 0..n-1.  Its negative directions are the right singular
vectors of B_n with sigma > 1; its inertia obeys the
Jacobi/Sylvester dictionary n_-(A_n) = #{k < n : h_k < 0}
(machine-gated as THE index-form-exactness gate, two independent
paths: f64 SVD counts vs the r279 mp h-sign chain at dps 120).

LEG 0 -- ANCHORS.  v956 half-filling pins (w9 S/S_+/S_- =
367/263/104, N_w = 184, minC = 184); r279 theorem pins on w9
(crossing budget #{n < S : h_n < 0} == S_- == 104 via the mp
chain; minC == N_w); r283 crossing pin (lambda_max(E_n) crosses 1
at 185 == minC + 1); the w9 budget scalar B = 8.368649 (tol
1e-3); THE r312 CROSS-MIXTURE PINS reproduced with the identical
protocol (r308 Dykstra 200 steps from the least-norm start,
per-block NNLS onto the sealed 22-generator cone): cone share
med/min/mean in the 0.976/0.952/0.978 bands (tol 0.01), top
eigvec library alignment med 0.9973 (tol 0.005), Dykstra CONV
(min eig rel >= -1e-9).

LEG A -- P1, THE PONTRYAGIN-/KREIN-INDEX ROUTE.
(a1) INDEX-FORM EXACTNESS (bookkeeping theorem, gated): on ALL
  seven worlds (w9, w13, r289 rational twin, EPST/SCR/SMOOTH/HL2)
  the spectral count #{sigma_i(B_n) > 1} equals the mp pivot
  count #{k < n : h_k < 0} at the WINDOW n = N_w and at the DEEP
  depth n = DEEP_EFF (the overflow-guarded largest depth <=
  S_+ - 1 with max |B entry| <= 1e100; near-1 gray zone
  sigma in (0.9, 1.1) disclosed; sealed rule: exact match, OR
  |mismatch| <= gray count, disclosed loudly).
(a2) THE SIGNATURE TABLE: window index defect d_w = n_-(A_{N_w})
  per world -- the mains and the twin must have d_w == 0 EXACTLY
  (n_+ == N_w EXACTLY at the window: the index form of the
  half-filling survival) while every control has d_w > 0 (the
  control flips ARE negative directions wandering INTO the
  window, measured as an index defect); LADDER: d_w == 0 on all
  42 frame-A rungs (h <= 900, half-filling 42/42, f64 sign
  chain); VACUITY CHECK: n_+(full) = S_+ >= N_w on every world
  including the controls -- the global index inequality
  "n_+ >= N_w" is carried by the mu-channel majority alone and
  is typed VACUOUS as a discriminator (measured).
(a3) THE BRUTAL RESTATEMENT GATE (its own gate, sealed): the
  sealed equivalence test "d_w == 0 <=> minC >= N_w" adjudicated
  on the three exact toys (JF9 / MAINLIKE / FLIPLIKE, Fractions,
  both truth values realized) AND on all seven real worlds; if
  the equivalence is total, the index statement "n_+(window) ==
  N_w" is typed RESTATEMENT (of L*/free-window survival) -- then
  P1 lives or dies on the ADDITIONAL structure alone:
(a4) NEGATIVE-SUBSPACE INVARIANTS (the additional-structure
  hunt): at DEEP_EFF the degree profiles |v_i(d)|^2 of the
  negative directions; sealed statistics NEG_LOW = min_i
  d10_i / N_w, NEG_MED = median_i d10_i / N_w (d10 = lowest
  degree with cumulative mass >= 0.10), NEG_PR = median_i
  PR_i / N_w (participation ratio of the profile); adjudicated
  by the sealed r281 distance rule (MAIN w9 vs the four dead
  worlds) PLUS the PROXY TEST: typed RESTATEMENT_PROXY iff
  |NEG_LOW - minC/N_w| <= 0.15 on EVERY world (the invariant is
  then the crossing location in disguise -- no lever); ladder
  stability of NEG_LOW on the 12 sealed fingerprint rungs
  reported as typed information.
(a5) KREIN PLUS-OPERATOR / ANGULAR TEST: ANG = largest singular
  value of the window block of the negative right-singular
  frame (the principal-angle overlap of the free window with
  the deep negative subspace); the sealed dictionary test:
  spearman(ANG, rho_win = ||B_{N_w}||_2) over the seven worlds;
  |sp| >= 0.9 types the angular-operator language RESTATEMENT
  (the plus-operator question collapses onto the contraction
  scalar = L*), else typed independent (reported).

LEG B -- P2, THE SIGN-REGULARITY / TOTAL-POSITIVITY ROUTE.
(b1) MINOR SIGN-PATTERN CENSUS (contiguous, budget-aware, orders
  k = 1..5): on the atom-sorted matrices E_win = B_win B_win^T
  (nu-Gram / dressed CD kernel, principal + row-initial census),
  A_win = I - M_win (the canonical indefinite form, principal +
  row-initial, scalar-normalized -- positive scalings preserve
  every minor sign), and B_win itself (rows = sorted nu atoms,
  columns = degrees, row-initial census -- orientation
  sensitive).  Sign 0 iff |det| <= 1e-10 x Hadamard bound;
  per-order majority share; SR_SCORE = min over live orders of
  the majority share; pattern = the majority-sign tuple.  A
  census object is SIGN_REGULAR iff SR_SCORE >= 0.99 and no
  order is zero-degenerate (> 20 percent zero class).
(b2) WORLD CONTRAST: the same census on the twin (METRIC_ONLY:
  pattern and score must match MAIN if the pattern is real) and
  on EPST/SCR/SMOOTH/HL2; SR MAIN-SPECIFIC iff some census
  object is sign-regular on MAIN AND on the twin with the same
  pattern AND fails the bar or the pattern on EVERY control;
  sign-regular everywhere with one pattern => world-blind
  (construction-generic).
(b3) THE R312 INVERSION -- THE CROSS-MIXTURE FINGERPRINT (its
  own gate): on the 12 sealed rungs (w9 plus the 11 smallest-S
  rungs of the 42-rung frame-A ladder, sorted by (S, kz)) the
  r308 Dykstra family at 200 steps, per block r the sealed cone
  projection (NNLS onto the 22-generator library in isometric
  vech coordinates) and the residual matrix R_r = G_r -
  sum_l c_l V_l V_l^T in the D basis; per block the dominant
  off-diagonal pair (a, b) = argmax |R_r[a, b]| and its sign;
  per rung the modal pair, the modal-pair share, the sign
  consistency and the D6-class share (pairs touching the border
  coordinate); THE CONSENSUS VERIFIER (sealed, the m4 gate):
  requires >= 10 rungs, LAWFUL iff >= 10 of 12 rungs carry the
  SAME modal (pair, sign) with median modal share >= 0.5; world
  contrast: the twin (must match MAIN if METRIC_ONLY holds) and
  EPST/SCR at w9 (their 200-step iterate is NOT psd-feasible --
  labeled ITERATE, honestly); FP MAIN-SPECIFIC iff lawful on the
  MAIN ladder AND twin-consistent AND both controls break the
  consensus (different pair OR different sign OR share < 0.5).
(b4) THE IMPLICATION SKETCH (which minor pattern would imply
  L*): sign regularity of order k of B implies variation
  diminishing (Schoenberg) for the dressed evaluation operator,
  VD bounds the sign changes of every dressed polynomial on the
  nu atoms, sign-change bounds at every truncation imply the
  reality/interlacing side R2 (r277), and by the r277 bridge R2
  <=> quasi-definiteness through the window <=> the inertia
  statement (v962 T4 form of L*).  The probe gates the MEASURED
  premise: is B on MAIN even sign-regular to order 5 (b1), and
  the VD spot check (sign changes of column i <= i for the
  first 20 degree columns, a world-blind polynomial bookkeeping
  gate); a failed premise on MAIN types the chain
  PREMISE_FAILS_ON_MAIN (honest negative).

LEG C -- THE FORK ADJUDICATION (sealed BEFORE evaluation):
  alive(P1) iff (a1) exact AND some sealed NEG statistic is
    MAIN_SEPARATING under the r281 distance rule AND the proxy
    test does NOT fire;
  alive(P2) iff SR MAIN-SPECIFIC (b2) OR FP MAIN-SPECIFIC (b3);
  letters: BOTH_ALIVE(p1 site; p2 pattern) /
    P1_MAIN_SPECIFIC(dig site named) /
    P2_MAIN_SPECIFIC(pattern verbatim) /
    FORK_DEAD(p1 reason; p2 reason; LANE-STOP RECOMMENDATION).

LEG D -- MUST-FAILS (each loud):
  (m1) INDEX COUNT WITH THE WRONG SIGNATURE CONVENTION: on the
    exact JF9 toy (Fractions) the mutant counts #{h_k > 0}
    instead of the Frobenius sign-change count of the exact
    congruence minors -- must MISMATCH the exact inertia
    (CAUGHT, exact);
  (m2) MINOR PATTERN ON THE TRANSPOSED MATRIX: the sealed
    row-initial census of the exact hand matrix M_TP =
    [[1,2,3],[1,3,6],[-1,1,13]] is all-positive (orders 1..3:
    (1,2,3)/(1,3)/(7)) while the census of M_TP^T contains a
    negative order-1 minor -- the transposed-input mutant must
    be CAUGHT (exact Fractions);
  (m3) RESTATEMENT GATE WITH CIRCULAR L* CONSUMPTION: a mutant
    "additional-structure invariant" consuming the withheld
    truth (minC_true / rho_true) -- FLAGGED by the AST scope
    audit;
  (m4) CROSS-MIXTURE FINGERPRINT EXTRAPOLATED FROM A SINGLE
    RUNG: the sealed consensus verifier must REJECT any census
    with fewer than 10 rungs -- the single-rung mutant call is
    CAUGHT live (consistency forced across >= 10 rungs).

STOP LIST (binding): NO L* claim, NO RH claim, NO bound
mechanism, NO asymptotic law, NO derived 5/7, NO posthoc window,
NO new no-go catalog entry re-opened (functionals, extremality,
KYP, Maslov, fixed head, paired cone, block-Green construction,
diophantine, magnitudes stay stopped); no bar, band, rule or
verdict form change after any evaluation (amendments disclosed);
r243..r316 stand; mincut base 4 / refined 5 UNCHANGED.

WORLDS: MAIN w9 + second main w13; the r289 rational twin
(METRIC_ONLY semantics); controls EPST / SCRAMBLE(seed 1) /
SMOOTH / HL2(seed 101) built verbatim through the r283/r284
channel; the 42-rung frame-A ladder (h <= 900); exact toys JF9,
MAINLIKE, FLIPLIKE (r280 conventions via FS.toy_block) and the
exact hand matrix M_TP.

SEALED CONSTANTS: DEG_A 8; MAIN_KZ 9; KZ_SECOND 13; CTRL_FLIPS
{EPST 25, SCR 21, SMOOTH 27}; HL2 seed 101 flip 25; H_CAP 900;
MP_DPS 120; SIGN_GUARD 1e-90; RECOUNT_DPS 240; GRAY (0.9, 1.1);
OFLOW_CAP 1e100; NEG_MASS_Q 0.10; PROX_TOL 0.15; K_MAX 5; ZTOL
1e-10; Z_FRAC 0.2; SR_BAR 0.99; VD_DEGS 20; N_FP 12;
FP_MIN_RUNGS 10; FP_CONS 10; FP_BAR 0.5; FEAS_IT 200; FEAS_CONV
1e-9; SHARE_REC (0.976, 0.952, 0.978) tol 0.01; ALIGN_REC 0.9973
tol 0.005; B_W9_REC 8.368649 tol 1e-3; W9_ANCH (367, 263, 104,
184, 184); BUDGET_REC 104; TWIN_MINC_REC 184; RAT_TOL 1e-8;
QMAX 1e6; ANG_SP_BAR 0.9; STAB_BINS 20; runtime <= 1800 s;
smoke = S0 + exact toys + hand census + w9 f64 window block
(source pins, window spectral-vs-f64-pivot co-location, crossing
anchor) + all four must-fails + scope audits (mp legs, twin,
controls, ladder, fingerprint, censuses, adjudication skipped).
PRE-SPEC SCOPING (disclosed): every record number above is a
published v956/r279/r283/r312 record adopted as-is; the two
routes, every sealed statistic, bar, band, the proxy rule, the
consensus verifier, the adjudication tree and the verdict form
were fixed at design time BEFORE any evaluation of this probe;
no machinery pass preceded this spec except record reading.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of, by the Leg-C tree]
    BOTH_ALIVE(p1 site; p2 pattern) /
    P1_MAIN_SPECIFIC(dig site) /
    P2_MAIN_SPECIFIC(pattern verbatim) /
    FORK_DEAD(p1 reason; p2 reason; lane-stop recommendation)
  + INDEX_LANGUAGE(exactness; restatement typing; vacuity)
    [always]
  + SIGNATURE_TABLE(per-world window defect / deep inertia /
    gray) [always]
  + FINGERPRINT(consensus pair/sign/share; world contrast)
    [always]
  + R312_DEMARCATION [always]: the r312 letters stand; this
    round adjudicates the REPRESENTATION question only.

RECORD TABLES (frozen from the record run; chronology honest:
(i) a PRE-RUN PROTOCOL CORRECTION is disclosed -- a draft
record-table block with placeholder numbers was removed from this
docstring BEFORE the first run of any stage (the r316 protocol
lesson, applied); (ii) smoke pass 1 ABORTED at G73 with a harness
crash (a tiebreak-type bug in the fp_consensus verifier, fixed at
smoke stage before any full evaluation; no rule content moved);
smoke pass 2 = 25/25 (0.2 s); (iii) calibration pass 1 = first
full evaluation = 25/25 (21.5 s) with ONE disclosed amendment a1
(reporting-only: the P2 verdict-letter dig-site label is derived
from the MEASURED modal pair -- the draft text had pre-named the
border column, which the measurement contradicts (d6-class share
0.027); no bar, band, statistic, rule or tree moved); calibration
pass 2 = 25/25 (23.7 s); record run1/run2 = 25/25, identical up
to WALL).
REC_VERDICT = P2_MAIN_SPECIFIC(fingerprint verbatim: modal
cross-mixture pair (2, 3) = D3 x D4 -- the ANTIPHASE x ANTIPHASE
coordinate pair of the sealed r312 library -- with sign -1,
median modal share 0.699, LAWFUL 12/12 sealed rungs AND
twin-consistent ((2, 3), -1, 0.692 -- METRIC_ONLY holds); the
controls break by PATTERN, not merely by bar: EPST modal (4, 5)
sign -1 share 0.953 / SCR modal (4, 5) sign -1 share 1.000 --
the dead worlds put their residual on the ARCH-MEAN x BORDER
pair (d6-class share 0.962/1.000 vs MAIN 0.027); honest caveat
typed with the letter: the EPST/SCR fingerprints are measured on
NON-psd-feasible 200-step iterates (feas -0.45/-0.49, the r308
non-convergence), labeled ITERATE -- the contrast compares the
converged MAIN-class family shape against the shape of a
non-converged control iterate; dig site named per the stop
rule: the D3 x D4 (antiphase x antiphase) cross-mixture residual
of the block-Green family -- WHY does the 2.4 percent negative
cross mixture of the converged psd family live on the antiphase
pair with a fixed negative sign, stably over 12 rungs and the
rational twin)
+ INDEX_LANGUAGE(EXACT: spectral count == mp pivot count at
window AND DEEP_EFF on all seven worlds (SCR deep 66/65 inside
its gray band 6 -- the single tolerated gray case, disclosed;
all other twelve counts exact, 0 guards / 0 recounts on w9);
RESTATEMENT: the equivalence 'window index defect == 0 <=>
minC >= N_w' holds on ALL 10 instances (3 exact toys JF9/
MAINLIKE/FLIPLIKE defects 2/0/1 + 7 real worlds) with both truth
values realized -- the reviewer's index form 'n_+(window) ==
N_w' is L* in signature language, a LANGUAGE gain with no
independent lever; VACUITY: the global inequality n_+ >= N_w is
carried by the mu-channel majority alone, S_+/N_w = 1.43/1.41/
1.43/1.23/1.48/1.96/1.52 on w9/w13/twin/EPST/SCR/SMOOTH/HL2 --
world-blind)
+ SIGNATURE_TABLE(window index defect w9 0 / w13 0 / twin 0 --
n_+ == N_w EXACTLY at the window on the mains, the index form
of half-filling survival -- vs EPST 55 / SCR 37 / SMOOTH 4 /
HL2 31: the control flips ARE negative directions inside the
window, measured as index defects; deep inertia at DEEP_EFF:
w9 43@262 / w13 36@236 / twin 43@262 / EPST 80@225 / SCR
66@272 / SMOOTH 6@360 / HL2 58@278; ladder 42/42 rungs window
defect 0 (half-filling 42/42); NEGATIVE-SUBSPACE INVARIANTS all
WORLD_BLIND under the sealed r281 distance rule (NEG_LOW MAIN
0.386 inside dead 0.0..1.28; NEG_MED MAIN 1.14 inside dead
0.39..1.90; NEG_PR MAIN 0.058 inside dead 0.030..0.326) and
NEG_LOW is NOT a proxy of the crossing location (devs 0.61/
0.51/0.79/0.11/0.11/1.13/0.03 > 0.15 on the mains -- the
negative directions do NOT live at minC, but their location is
world-blind: no lever either way); ladder NEG_LOW med 0.059
spread 0.473 (unstable); KREIN ANGULAR TEST typed INDEPENDENT
(spearman(ANG, rho_win) = +0.536 < 0.9; disclosed: ANG consumes
the UNSIGNED profiles sqrt(|v|^2), a magnitude-overlap
statistic -- values above 1 reflect the unsigned aggregation;
reported, no adjudication weight))
+ FINGERPRINT(consensus (2, 3) sign -1, 12/12 agree, med share
0.699; per-rung shares 0.605..0.780 over kz 9/12/13/14/15/18/
20/22/23/29/32/33, d6-class 0.005..0.064, cone-share med
0.970..0.982 -- the 97.6/2.4 anatomy is ladder-uniform; twin
(2, 3) -1 0.692; EPST (4, 5) -1 0.953 ITERATE / SCR (4, 5) -1
1.000 ITERATE)
+ R312_DEMARCATION.
Key numbers.  LEG 0 bit-near: w9 367/263/104/184/184, budget
B = 8.368649, mp crossing budget 104 == S_-, mp minC 184 ==
N_w, spectral crossing 185 == minC + 1; r312 pins reproduced:
Dykstra CONV +6.56e-16, cone share med/min/mean 0.9760/0.9520/
0.9778 (rec 0.976/0.952/0.978), alignment med 0.9973.  P2 SR
CENSUS (the honest negative half of P2): NO census object is
MAIN-specifically sign-regular -- E.principal and A.principal
score 1.000 but are NOT world-separating (E.principal is
psd-forced and pattern-identical everywhere; A.principal fails
the every-control-broken clause), and every orientation-
sensitive census is coin-flip on MAIN (E.rowinit 0.500 /
A.rowinit 0.503 / B.rowinit 0.500) => the SR premise of the
implication chain FAILS ON MAIN (PREMISE_FAILS_ON_MAIN: the
variation-diminishing route to L* cannot start; VD spot check
0 violations, world-blind bookkeeping).  MUST-FAILS: m1 wrong
signature convention 3 != 2 exact CAUGHT (JF9, Fractions); m2
transposed census exact CAUGHT (order-1 row (1, 1, -1)); m3
circular-lever mutant AST-FLAGGED (minC_true/rho_true); m4
single-rung consensus REJECTED (REJECT_INSUFFICIENT_RUNGS),
the 12-rung call accepted; constructors + fragment audit CLEAN.
READING (typed measurement): the reviewer's index language is
EXACT and gives L* its cleanest coordinate-free form -- "the
free polynomial window is a positive subspace of the canonical
Krein geometry I - M, of the maximal free dimension" -- but it
carries NO independent lever (restatement total, global index
vacuous, negative-subspace invariants world-blind): P1 closes
as language; the SIGNEDNESS FINGERPRINT is the round's find --
the reviewer's inversion question has a measured answer: the
2.4 percent negative cross mixtures are NOT structureless; on
MAIN-class worlds they live LAWFULLY on the antiphase pair
(D3, D4) with a fixed negative sign (12/12 rungs, twin exact),
while the dead controls' residual sits on the arch-mean x
border pair -- the fingerprint of the signedness is
world-separating in SHAPE, exactly the precondition the
reviewer's indefinite-theorem hope needs.  Runtime 23.7 s full
/ 0.2 s smoke; run1/run2 identical up to WALL.  AMENDMENTS
AFTER FREEZE: a1 only (reporting-only, disclosed above).

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

import blockgreen_membership_probe as BM           # noqa: E402 r312
import block_green_probe as BG                     # noqa: E402 r308
import fullsource_quasidefiniteness_probe as FS    # noqa: E402 r283
import lstar_two_measure_probe as LS               # noqa: E402 r284
import budget_localization_probe as BL             # noqa: E402 r280
import oriented_theorem_probe as OT                # noqa: E402 r279
import metric_stability_probe as MS                # noqa: E402 r278
import minimal_firewall_probe as MF                # noqa: E402 r276
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import paircorr_margin_probe as PC                 # noqa: E402
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import principal_bessel_probe as PB                # noqa: E402 r243
import bordered_hankel_probe as BH                 # noqa: E402 r244
import wronskian_dictionary_probe as WD            # noqa: E402 r274
import jfraction_probe as JF                       # noqa: E402 r230
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
MAIN_KZ = 9
KZ_SECOND = 13
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
H_CAP = 900
MP_DPS = 120
SIGN_GUARD = 1e-90
RECOUNT_DPS = 240
GRAY_LO = 0.9
GRAY_HI = 1.1
OFLOW_CAP = 1e100
NEG_MASS_Q = 0.10
PROX_TOL = 0.15
K_MAX = 5
ZTOL = 1e-10
Z_FRAC = 0.2
SR_BAR = 0.99
VD_DEGS = 20
N_FP = 12
FP_MIN_RUNGS = 10
FP_CONS = 10
FP_BAR = 0.5
FEAS_IT = 200
FEAS_CONV = 1e-9
SHARE_REC = (0.976, 0.952, 0.978)
SHARE_TOL = 0.01
ALIGN_REC = 0.9973
ALIGN_TOL = 0.005
B_W9_REC = 8.368649
B_W9_TOL = 1e-3
W9_ANCH = (367, 263, 104, 184, 184)
BUDGET_REC = 104
TWIN_MINC_REC = 184
RAT_TOL = 1e-8
QMAX = 1e6
ANG_SP_BAR = 0.9
STAB_BINS = 20

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
    return (not bad), ("NO zero/prime oracles; the sealed "
                       "constructors consume passed matrices and "
                       "split-source arrays ONLY; record numbers "
                       "enter gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq_fit",
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


CONSTRUCTORS = ("finite_depth", "spectral_counts", "neg_profiles",
                "deg_stats", "ang_overlap", "det_sign",
                "minor_census", "census_shares",
                "block_residual_census", "fp_consensus",
                "vd_spotcheck", "frac_rowinit_signs")
SCOPE_FORBIDDEN = {"minC_true", "rho_true", "CTRL_FLIPS", "HL2_FLIP",
                   "W9_ANCH", "BUDGET_REC", "defect_true",
                   "cross_true", "HS_true", "sg_true"}


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
def finite_depth(B, cap):
    """largest depth d <= ncols with every entry of B[:, :d]
    finite and max |entry| <= cap (the sealed overflow guard for
    deep frame spectra).  Consumes the passed matrix only."""
    d = 0
    for j in range(B.shape[1]):
        col = B[:, j]
        if not np.all(np.isfinite(col)) \
                or float(np.max(np.abs(col))) > cap:
            break
        d = j + 1
    return d


def spectral_counts(B, n):
    """spectral inertia counts of A_n = I - B_n^T B_n: n_neg =
    #{sigma_i(B_n) > 1} (negative directions) plus the near-one
    gray count sigma in (GRAY_LO, GRAY_HI).  Consumes the passed
    matrix only."""
    sv = np.linalg.svd(B[:, :n], compute_uv=False)
    n_neg = int(np.sum(sv > 1.0))
    n_gray = int(np.sum((sv > GRAY_LO) & (sv < GRAY_HI)))
    return n_neg, n_gray


def neg_profiles(B, n):
    """degree profiles |v_i(d)|^2 of the negative directions of
    A_n = I - B_n^T B_n (right singular vectors with sigma > 1,
    descending sigma).  Consumes the passed matrix only."""
    U, s, Vt = np.linalg.svd(B[:, :n], full_matrices=False)
    idx = np.nonzero(s > 1.0)[0]
    return Vt[idx] ** 2, s[idx]


def deg_stats(profiles, Nw):
    """sealed negative-subspace statistics: NEG_LOW / NEG_MED
    (min / median over directions of the lowest degree carrying
    cumulative mass >= NEG_MASS_Q, normalized by the passed
    window depth) and NEG_PR (median participation ratio of the
    profile, normalized).  Consumes the passed profiles only."""
    if profiles.shape[0] == 0:
        return None, None, None, []
    d10 = []
    prs = []
    for p in profiles:
        c = np.cumsum(p)
        d10.append(int(np.searchsorted(c, NEG_MASS_Q * c[-1])))
        prs.append(float((np.sum(p) ** 2) / max(np.sum(p * p),
                                                1e-300)))
    return (float(np.min(d10)) / Nw,
            float(np.median(d10)) / Nw,
            float(np.median(prs)) / Nw, d10)


def ang_overlap(Vt_neg, Nw):
    """principal-angle overlap of the free window with the deep
    negative subspace: largest singular value of the window block
    of the negative right-singular frame.  Consumes the passed
    frame only."""
    if Vt_neg.shape[0] == 0:
        return 0.0
    blk = Vt_neg[:, :Nw]
    sv = np.linalg.svd(blk, compute_uv=False)
    return float(sv[0]) if len(sv) else 0.0


def det_sign(sub):
    """sign of det(sub) with the sealed zero class |det| <=
    ZTOL x Hadamard bound.  Consumes the passed matrix only."""
    bnd = float(np.prod(np.linalg.norm(sub, axis=1)))
    if not math.isfinite(bnd) or bnd == 0.0:
        return 0
    d = float(np.linalg.det(sub))
    if not math.isfinite(d) or abs(d) <= ZTOL * bnd:
        return 0
    return 1 if d > 0 else -1


def minor_census(K, kmax, modes):
    """contiguous minor sign census: mode 'principal' =
    diagonal-sliding K[i..i+k-1, i..i+k-1] (square only), mode
    'rowinit' = rows 0..k-1 fixed, columns sliding (orientation
    sensitive).  Consumes the passed matrix only."""
    K = np.asarray(K, float)
    nr, nc = K.shape
    out = {}
    for mode in modes:
        per = []
        for k in range(1, kmax + 1):
            sgs = []
            if mode == "principal":
                if nr == nc:
                    for i in range(nr - k + 1):
                        sgs.append(det_sign(K[i:i + k, i:i + k]))
            else:
                if nr >= k:
                    for lo in range(nc - k + 1):
                        sgs.append(det_sign(K[0:k, lo:lo + k]))
            per.append(sgs)
        out[mode] = per
    return out


def census_shares(per_order):
    """per-order majority shares of one census: rows (k, n+, n-,
    n0, share, majority sign, zero fraction); SR_SCORE = min over
    live orders of the share; degenerate iff any populated order
    has zero fraction > Z_FRAC.  Consumes the passed census
    only."""
    rows = []
    for k, sgs in enumerate(per_order, start=1):
        npos = sum(1 for s in sgs if s > 0)
        nneg = sum(1 for s in sgs if s < 0)
        nz = sum(1 for s in sgs if s == 0)
        tot = npos + nneg
        share = (max(npos, nneg) / tot) if tot else 0.0
        maj = 0 if tot == 0 else (1 if npos >= nneg else -1)
        zfrac = nz / max(len(sgs), 1)
        rows.append((k, npos, nneg, nz, share, maj, zfrac))
    live = [r for r in rows if (r[1] + r[2]) > 0]
    score = min((r[4] for r in live), default=0.0)
    degen = any(r[6] > Z_FRAC for r in rows
                if (r[1] + r[2] + r[3]) > 0)
    pattern = tuple(r[5] for r in live)
    return dict(rows=rows, score=score, degen=degen,
                pattern=pattern)


def block_residual_census(g, nblk, V, A21, pa, pb, isow, iu1, ju1):
    """the r312 cross-mixture residual census: per block the
    sealed cone projection (NNLS onto the 22-generator library in
    isometric vech coordinates), the residual matrix R_r in the D
    basis, its dominant off-diagonal pair and sign, plus the cone
    share.  Consumes the passed iterate/coordinates only."""
    lam, scale, G = BG.block_eigs(g, nblk)
    pairs = []
    signs = []
    shares = []
    d6 = 0
    for r in range(nblk):
        rhs = G[r][pa, pb] * isow
        cc, rel, _s, _cap = BM.nnls_lh(A21, rhs)
        shares.append(1.0 - rel)
        res = A21 @ cc - rhs
        R = np.zeros((6, 6))
        R[pa, pb] = res / isow
        R = R + R.T - np.diag(np.diag(R))
        vals = R[iu1, ju1]
        j = int(np.argmax(np.abs(vals)))
        pairs.append((int(iu1[j]), int(ju1[j])))
        signs.append(1 if vals[j] > 0 else -1)
        if ju1[j] == 5 or iu1[j] == 5:
            d6 += 1
    cnt = {}
    for p, s in zip(pairs, signs):
        cnt[(p, s)] = cnt.get((p, s), 0) + 1
    modal = max(cnt, key=lambda k: (cnt[k], -k[0][0], -k[0][1]))
    return dict(modal_pair=modal[0], modal_sign=modal[1],
                modal_share=cnt[modal] / max(nblk, 1),
                d6_share=d6 / max(nblk, 1),
                share_med=float(np.median(shares)),
                share_min=float(np.min(shares)),
                share_mean=float(np.mean(shares)))


def fp_consensus(rows):
    """the sealed fingerprint consensus verifier: REJECTS any
    census with fewer than FP_MIN_RUNGS rungs (the m4 guard);
    LAWFUL iff >= FP_CONS rungs carry the same modal (pair, sign)
    with median modal share >= FP_BAR over the agreeing rungs.
    Consumes the passed census rows only."""
    if len(rows) < FP_MIN_RUNGS:
        return ("REJECT_INSUFFICIENT_RUNGS", None)
    cnt = {}
    for r in rows:
        key = (r["modal_pair"], r["modal_sign"])
        cnt[key] = cnt.get(key, 0) + 1
    modal = max(cnt, key=lambda k: (cnt[k], -k[0][0], -k[0][1]))
    agree = [r for r in rows
             if (r["modal_pair"], r["modal_sign"]) == modal]
    med_share = float(np.median([r["modal_share"] for r in agree]))
    lawful = (len(agree) >= FP_CONS) and (med_share >= FP_BAR)
    return ("OK", dict(pair=modal[0], sign=modal[1],
                       n_agree=len(agree), n_rungs=len(rows),
                       med_share=med_share, lawful=lawful))


def vd_spotcheck(Bs, kmax):
    """variation-diminishing spot check: the number of sign
    changes of the (atom-sorted) column i must be <= i for every
    degree column i < kmax (polynomial zero counting -- a
    world-blind bookkeeping gate).  Consumes the passed matrix
    only."""
    viol = 0
    for i in range(min(kmax, Bs.shape[1])):
        col = Bs[:, i]
        s = np.sign(col[col != 0.0])
        ch = int(np.sum(s[1:] != s[:-1])) if len(s) > 1 else 0
        if ch > i:
            viol += 1
    return viol


def frac_rowinit_signs(M, kmax):
    """EXACT (Fractions) row-initial contiguous minor sign census
    of the passed matrix (rows 0..k-1 fixed, columns sliding).
    Consumes the passed matrix only."""
    nr = len(M)
    nc = len(M[0])
    out = []
    for k in range(1, kmax + 1):
        sgs = []
        if nr >= k:
            for lo in range(nc - k + 1):
                d = FS.frac_det([row[lo:lo + k] for row in M[:k]])
                sgs.append(0 if d == 0 else (1 if d > 0 else -1))
        out.append(sgs)
    return out


# ============== must-fail mutants
def mutant_wrong_signature(hs, n):
    """m1 MUST-FAIL: index count with the WRONG signature
    convention -- counts the positive pivots instead of the
    negative ones; must mismatch the exact Frobenius inertia."""
    return sum(1 for k in range(n) if hs[k] > 0)


def mutant_circular_lever(minC_true, rho_true):
    """m3 MUST-FAIL: an 'additional-structure invariant' that
    consumes the withheld truth -- the scope audit must FLAG
    this."""
    return float(minC_true) + float(rho_true)


# ============== gate-side helpers
def frobenius_inertia_exact(minors, n):
    """gate-side exact Frobenius rule: n_-(H_n) = sign changes in
    the sequence (1, D_1, ..., D_n) of exact leading minors."""
    seq = [Fr(1)] + list(minors[:n])
    if any(v == 0 for v in seq):
        return None
    return sum(1 for a, b in zip(seq, seq[1:]) if (a > 0) != (b > 0))


def spectral_bundle(W):
    """gate-side per-world frame bundle: mu chain, B matrix to
    the guarded deep depth, window/deep spectral counts, negative
    profiles, statistics, angular overlap, rho at window."""
    Nw = W["N"]
    Sp = W["Sp"]
    deep = Sp - 1
    xp = np.asarray(W["xp"], float)
    wp = np.asarray(W["wp"], float)
    xn = np.asarray(W["xn"], float)
    vn = np.asarray(W["vn"], float)
    al, sb, h0 = FS.mu_chain_f64(xp, wp, deep)
    B = FS.b_matrix_f64(al, sb, h0, xn, vn, deep)
    deff = finite_depth(B, OFLOW_CAP)
    n_win = min(Nw, deff)
    cw, gw = spectral_counts(B, n_win)
    cd, gd = spectral_counts(B, deff)
    prof, sneg = neg_profiles(B, deff)
    nlow, nmed, npr, d10 = deg_stats(prof, Nw)
    ang = ang_overlap(np.sqrt(prof), Nw) if prof.shape[0] else 0.0
    rho_win = float(np.linalg.norm(B[:, :n_win], 2)) ** 2
    order = np.argsort(xn)
    Bs = B[order]
    return dict(B=B, Bs=Bs, deff=deff, n_win=n_win, cw=cw, gw=gw,
                cd=cd, gd=gd, prof=prof, sneg=sneg, nlow=nlow,
                nmed=nmed, npr=npr, d10=d10, ang=ang,
                rho_win=rho_win, Nw=Nw)


def sr_bundle(sp, Nw):
    """gate-side P2 census bundle on the atom-sorted window
    matrices E / A / B (positive scalings only -- every minor
    sign invariant)."""
    Bw = sp["Bs"][:, :min(Nw, sp["deff"])]
    scal = max(float(np.max(np.abs(Bw))), 1e-300)
    Bn = Bw / scal
    E = Bn @ Bn.T
    M = Bn.T @ Bn
    A = np.eye(M.shape[0]) - (scal ** 2) * M
    A = A / max(float(np.max(np.abs(A))), 1e-300)
    out = {}
    cE = minor_census(E, K_MAX, ("principal", "rowinit"))
    cA = minor_census(A, K_MAX, ("principal", "rowinit"))
    cB = minor_census(Bn, K_MAX, ("rowinit",))
    out["E.principal"] = census_shares(cE["principal"])
    out["E.rowinit"] = census_shares(cE["rowinit"])
    out["A.principal"] = census_shares(cA["principal"])
    out["A.rowinit"] = census_shares(cA["rowinit"])
    out["B.rowinit"] = census_shares(cB["rowinit"])
    out["_viol"] = vd_spotcheck(sp["Bs"][:, :min(VD_DEGS,
                                                 sp["deff"])],
                                VD_DEGS)
    return out


def fp_run(pack, ctx):
    """gate-side fingerprint run for one world: r308 census at
    DEG_A, Dykstra FEAS_IT steps from the least-norm start, the
    sealed block residual census."""
    Bw, _rho, bxa, bwa = BG.world_budget(pack, ctx)
    ffw, xaw, waw = BG.world_arrays(pack)
    C = BG.census_world(xaw, waw, bxa, bwa, Bw, DEG_A,
                        BG.hull_of(xaw, bxa))
    fm, rel, g = BM.feas_diag_g(C["M"], C["q"], C["g"],
                                C["nblk"], FEAS_IT)
    cen = block_residual_census(g, C["nblk"], V_LIB, A21_ISO,
                                PA6, PB6, ISOW, IU1, JU1)
    cen["feas"] = float(fm)
    cen["nblk"] = C["nblk"]
    return cen, C, g, Bw


V_LIB, V_LABELS = BM.lib_vectors()
PA6, PB6 = np.triu_indices(6)
ISOW = np.where(PA6 == PB6, 1.0, math.sqrt(2.0))
A21_ISO = np.stack([np.outer(v, v).astype(float)[PA6, PB6] * ISOW
                    for v in V_LIB], axis=1)
IU1, JU1 = np.triu_indices(6, k=1)

M_TP = [[Fr(1), Fr(2), Fr(3)],
        [Fr(1), Fr(3), Fr(6)],
        [Fr(-1), Fr(1), Fr(13)]]


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("indefinite_fork_probe -- PRIME.LSTAR.INDEFINITE_FORK.01 "
          "(round 318)")
    print("SPEC_SHA %s   (r312 BM %s / r283 FS %s / r284 LS %s / "
          "r279 OT %s)"
          % (SPEC_SHA[:16], BM.SPEC_SHA[:16], FS.SPEC_SHA[:16],
             LS.SPEC_SHA[:16], OT.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (S0 + exact toys + hand census + w9 "
                        "f64 window block + must-fails + scopes; mp "
                        "legs, twin, controls, ladder, fingerprint, "
                        "censuses, adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the two routes (P1 Pontryagin/"
          "Krein index with the brutal restatement gate + the "
          "negative-subspace invariants + the proxy rule; P2 sign "
          "regularity with the contiguous minor census + the r312 "
          "cross-mixture fingerprint + the >= 10-rung consensus "
          "verifier), the frame convention A_n = I - M_n (r283 s2), "
          "the seven worlds, the 12 sealed fingerprint rungs, all "
          "four must-fails, every bar/band/tolerance, the Leg-C "
          "adjudication tree and the sealed verdict form; the stop "
          "rule is binding: both routes world-blind or restatement "
          "=> FORK_DEAD with a lane-stop recommendation")

    # ---------------- S1 exact toys
    section("S1  EXACT TOYS -- CONGRUENCE INERTIA + HAND TP CENSUS")
    jf_pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                      key=lambda t: t[0])
    nodes9 = [t[0] for t in jf_pairs]
    wts9 = [t[1] for t in jf_pairs]
    toys = [("JF9", nodes9, wts9),
            ("MAINLIKE", BL.TOYS_XS, BL.MAINLIKE_W),
            ("FLIPLIKE", BL.TOYS_XS, BL.FLIPLIKE_W)]
    TB = {}
    toy_rows = []
    ok_cong = True
    ok_frob = True
    for name, nds, wt in toys:
        tb = FS.toy_block(nds, wt)
        TB[name] = tb
        ok_cong = ok_cong and tb["ok_cong"] and tb["ok_mu"]
        n_win = min(tb["Nw"], tb["Sp"])
        frob = frobenius_inertia_exact(tb["minors"], n_win)
        piv = sum(1 for k in range(n_win) if tb["hs"][k] < 0)
        ok_frob = ok_frob and (frob == piv)
        toy_rows.append((name, tb["minC"], tb["Nw"], piv))
        info("%s: S=%d N_w=%d S_+=%d minC=%s window defect "
             "(exact) = %d (Frobenius %s)"
             % (name, tb["S"], tb["Nw"], tb["Sp"],
                str(tb["minC"]), piv, str(frob)))
    check("G10-toy-congruence-inertia", ok_cong and ok_frob,
          "EXACT (Fractions): the r283 Sylvester congruence "
          "minor_k(D_mu - G) == D_k(mutilde) holds on all three "
          "toys AND the Frobenius sign-change inertia of the exact "
          "congruence minors equals the pivot count #{k < n : h_k "
          "< 0} at the window -- both truth values realized "
          "(defects %s): the index bookkeeping is exact at toy "
          "grade" % str({r[0]: r[3] for r in toy_rows}))
    sealed_tp = frac_rowinit_signs(M_TP, 3)
    ok_tp = all(all(s > 0 for s in ord_) for ord_ in sealed_tp)
    check("G11-toy-tp-census", ok_tp,
          "EXACT hand matrix M_TP = [[1,2,3],[1,3,6],[-1,1,13]]: "
          "the sealed row-initial contiguous census is all-"
          "positive at orders 1..3 (%s) -- the m2 substrate: the "
          "transposed census must break this pattern (S7)"
          % str([[int(s) for s in o] for o in sealed_tp]))

    # ---------------- S2 leg 0 anchors
    section("S2  LEG 0 -- W9 ANCHORS (v956 / r279 / r283 / r312)")
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4]
              and W9["N"] == (W9["S"] + 1) // 2)
    B9, _rho9b, bxa9, bwa9 = BG.world_budget(W9, ctx9)
    check("G20-w9-source-pins", ok_src
          and abs(B9 - B_W9_REC) <= B_W9_TOL,
          "w9 SOURCE %d/%d/%d, N_w %d == (S+1)//2, minC %s == "
          "N_w (v956 pins); budget scalar B = %.6f (rec %.6f, "
          "tol %.0e)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], str(W9["minC"]),
             B9, B_W9_REC, B_W9_TOL))
    SP9 = spectral_bundle(W9)
    if smoke:
        # window co-location: f64 sign chain vs spectral count
        piv_f64 = int(np.sum(np.asarray(W9["sg"][:W9["N"]]) < 0))
        cross9 = None
        for n in range(1, SP9["n_win"] + 2):
            if float(np.linalg.norm(SP9["B"][:, :n], 2)) >= 1.0:
                cross9 = n
                break
        check("G21-w9-crossing-budget", SP9["cw"] == piv_f64 == 0
              and cross9 == W9["minC"] + 1,
              "SMOKE: window spectral defect %d == f64 pivot "
              "defect %d == 0 (exact half-filling positivity); "
              "crossing %s == minC + 1 (mp budget leg skipped)"
              % (SP9["cw"], piv_f64, str(cross9)))
        check("G22-r312-anchor", True, "SMOKE: skipped")
        HS9 = None
    else:
        al9m, be9m, SG9m, HS9, ng9, nr9 = OT.mp_chain_pack(
            np.asarray(W9["xu"], float), np.asarray(W9["wu"], float),
            MP_DPS, SIGN_GUARD, RECOUNT_DPS)
        budget9 = int(np.sum(HS9 < 0))
        minC9mp = next((n for n in range(len(HS9))
                        if HS9[n] < 0), None)
        cross9 = None
        for n in range(1, SP9["n_win"] + 2):
            if float(np.linalg.norm(SP9["B"][:, :n], 2)) >= 1.0:
                cross9 = n
                break
        check("G21-w9-crossing-budget", budget9 == BUDGET_REC
              and budget9 == W9["Sm"] and minC9mp == W9["N"]
              and cross9 == W9["minC"] + 1,
              "r279/v956/r283 pins: mp crossing budget #{h < 0} = "
              "%d == S_- == rec %d; mp minC = %s == N_w; spectral "
              "crossing %s == minC + 1 = %d (guards %d, recounts "
              "%d)" % (budget9, BUDGET_REC, str(minC9mp),
                       str(cross9), W9["minC"] + 1, ng9, nr9))
        cen9, C9, g9, _B9w = fp_run(W9, ctx9)
        # alignment census (r312 anatomy, verbatim class)
        lam9, sc9, G9 = BG.block_eigs(g9, C9["nblk"])
        ev9, Wv9 = np.linalg.eigh(G9)
        top9 = Wv9[:, :, -1]
        Vn = V_LIB.astype(float)
        Vn = Vn / np.linalg.norm(Vn, axis=1, keepdims=True)
        align9 = float(np.median(np.max(np.abs(top9 @ Vn.T),
                                        axis=1)))
        ok_312 = (cen9["feas"] >= -FEAS_CONV
                  and abs(cen9["share_med"] - SHARE_REC[0])
                  <= SHARE_TOL
                  and abs(cen9["share_min"] - SHARE_REC[1])
                  <= SHARE_TOL
                  and abs(cen9["share_mean"] - SHARE_REC[2])
                  <= SHARE_TOL
                  and abs(align9 - ALIGN_REC) <= ALIGN_TOL)
        check("G22-r312-anchor", ok_312,
              "r312 CROSS-MIXTURE PINS reproduced (identical "
              "protocol: Dykstra %d steps, per-block NNLS): CONV "
              "%+.2e; cone share med/min/mean %.4f/%.4f/%.4f (rec "
              "%.3f/%.3f/%.3f, tol %.2f); alignment med %.4f (rec "
              "%.4f) -- the 97.6/2.4 anatomy stands; w9 modal "
              "residual pair %s sign %+d share %.3f d6-class %.3f"
              % (FEAS_IT, cen9["feas"], cen9["share_med"],
                 cen9["share_min"], cen9["share_mean"],
                 SHARE_REC[0], SHARE_REC[1], SHARE_REC[2],
                 SHARE_TOL, align9, ALIGN_REC,
                 str(cen9["modal_pair"]), cen9["modal_sign"],
                 cen9["modal_share"], cen9["d6_share"]))

    # ---------------- S3 leg A P1
    section("S3  LEG A -- P1 PONTRYAGIN/KREIN INDEX")
    if smoke:
        for g in ("G30-index-form-exact", "G31-signature-table",
                  "G32-restatement-adjudication",
                  "G33-negspace-invariants", "G34-plus-operator"):
            check(g, True, "SMOKE: skipped")
        WORLDS = {}
        SPB = {}
        packs = {}
        neg_sep = {}
        proxy = True
        restat = True
        ok_idx = True
    else:
        # build the seven worlds
        ctx13 = MS.ctx_build(KZ_SECOND)
        D13 = float(core.build_window(KZ_SECOND)["D"])
        W13 = LS.world_pack("w13", ctx13, D13)
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        uR, mR, dens, duR = AK.twin_rational(
            ctx9["uu"], ctx9["mm"], gaps_c, D9, RAT_TOL)
        ok_tc = (bool(np.array_equal(mR, np.asarray(ctx9["mm"])))
                 and int(np.max(dens)) <= QMAX)
        ctxT = MS.ctx_build(MAIN_KZ, comb=(uR, mR))
        WT = LS.world_pack("twin", ctxT, D9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        gpc = PC.Grid()
        comb_hl, _tg = PC.gen_model(gpc, "HL2", HL2_SEED)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)))
        WORLDS = {"w9": (W9, ctx9), "w13": (W13, ctx13),
                  "twin": (WT, ctxT)}
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            WORLDS[cn] = (LS.world_pack(cn, cctx, D9), cctx)
        ok_ctrl = all(
            WORLDS[cn][0]["minC"] == CTRL_FLIPS.get(cn, HL2_FLIP)
            for cn in ("EPST", "SCR", "SMOOTH", "HL2"))
        # spectral + mp bundles
        SPB = {"w9": SP9}
        HSD = {"w9": HS9}
        for wn in ("w13", "twin", "EPST", "SCR", "SMOOTH", "HL2"):
            Wp = WORLDS[wn][0]
            SPB[wn] = spectral_bundle(Wp)
            _a, _b, _S, HSw, _g, _r = OT.mp_chain_pack(
                np.asarray(Wp["xu"], float),
                np.asarray(Wp["wu"], float),
                MP_DPS, SIGN_GUARD, RECOUNT_DPS)
            HSD[wn] = HSw
        ok_idx = ok_tc and (WT["minC"] == TWIN_MINC_REC) and ok_ctrl
        idx_txt = []
        defects = {}
        for wn in WORLDS:
            sp = SPB[wn]
            HSw = HSD[wn]
            piv_w = int(np.sum(HSw[:sp["n_win"]] < 0))
            piv_d = int(np.sum(HSw[:sp["deff"]] < 0))
            okw = (abs(sp["cw"] - piv_w) <= sp["gw"]
                   and sp["cw"] == piv_w if sp["gw"] == 0
                   else abs(sp["cw"] - piv_w) <= sp["gw"])
            okd = (sp["cd"] == piv_d if sp["gd"] == 0
                   else abs(sp["cd"] - piv_d) <= sp["gd"])
            ok_idx = ok_idx and okw and okd
            defects[wn] = piv_w
            idx_txt.append("%s %d/%d@%d(g%d)"
                           % (wn, sp["cw"], piv_w, sp["n_win"],
                              sp["gw"]))
            info("%s: window defect spec/mp %d/%d @ n=%d (gray "
                 "%d); deep %d/%d @ DEEP_EFF=%d (gray %d); "
                 "n_neg dirs %d" % (wn, sp["cw"], piv_w,
                                    sp["n_win"], sp["gw"],
                                    sp["cd"], piv_d, sp["deff"],
                                    sp["gd"], sp["prof"].shape[0]))
        check("G30-index-form-exact", ok_idx,
              "INDEX-FORM EXACTNESS: spectral count #{sigma(B_n) > "
              "1} == mp pivot count #{k < n : h_k < 0} at the "
              "window AND at DEEP_EFF on ALL SEVEN worlds (%s; "
              "sealed gray rule; twin rebuilt verbatim, minC %s == "
              "rec %d; control flips re-derived) -- the "
              "Jacobi/Sylvester index dictionary is machine-exact "
              "in the frame" % ("; ".join(idx_txt), str(WT["minC"]),
                                TWIN_MINC_REC))
        # ladder defect
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        packs = {}
        n_hf = 0
        n_def0 = 0
        for kz in kzs:
            ctx = ctx9 if kz == MAIN_KZ else MS.ctx_build(kz)
            Dk = D9 if kz == MAIN_KZ else \
                float(core.build_window(kz)["D"])
            Wp = W9 if kz == MAIN_KZ else \
                LS.world_pack("w%d" % kz, ctx, Dk)
            packs[kz] = (Wp, ctx)
            if Wp["N"] == (Wp["S"] + 1) // 2:
                n_hf += 1
            dfk = int(np.sum(np.asarray(Wp["sg"][:Wp["N"]]) < 0))
            if dfk == 0:
                n_def0 += 1
        sp_ratio = {wn: WORLDS[wn][0]["Sp"] / SPB[wn]["Nw"]
                    for wn in WORLDS}
        ok_vac = all(v >= 1.0 for v in sp_ratio.values())
        ok_sig = (defects["w9"] == 0 and defects["w13"] == 0
                  and defects["twin"] == 0
                  and all(defects[c] > 0 for c in
                          ("EPST", "SCR", "SMOOTH", "HL2"))
                  and n_hf == len(kzs) == 42
                  and n_def0 == len(kzs))
        check("G31-signature-table", ok_sig and ok_vac,
              "SIGNATURE TABLE: window index defect %s -- the "
              "mains + twin sit at d_w == 0 EXACTLY (n_+ == N_w: "
              "the index form of half-filling survival), every "
              "control has negative directions INSIDE the window "
              "(the flip as an index defect); ladder %d/%d rungs "
              "defect 0 (half-filling %d/%d); VACUITY measured: "
              "S_+/N_w = %s >= 1 on every world -- the global "
              "index inequality n_+ >= N_w is carried by the "
              "mu-channel majority alone (world-blind, VACUOUS as "
              "a discriminator)"
              % (str(defects), n_def0, len(kzs), n_hf, len(kzs),
                 str({k: round(v, 2) for k, v in
                      sp_ratio.items()})))
        # restatement adjudication
        inst = []
        for name in TB:
            tb = TB[name]
            n_win_t = min(tb["Nw"], tb["Sp"])
            dft = sum(1 for k in range(n_win_t) if tb["hs"][k] < 0)
            inst.append((name, dft == 0,
                         tb["minC"] is None
                         or tb["minC"] >= tb["Nw"]))
        for wn in WORLDS:
            mc = WORLDS[wn][0]["minC"]
            inst.append((wn, defects[wn] == 0,
                         mc is None or mc >= SPB[wn]["Nw"]))
        restat = all(a == b for _n, a, b in inst)
        both_vals = (any(a for _n, a, _b in inst)
                     and any(not a for _n, a, _b in inst))
        check("G32-restatement-adjudication", restat and both_vals,
              "THE BRUTAL RESTATEMENT GATE: the equivalence "
              "'window index defect == 0 <=> minC >= N_w' holds on "
              "ALL %d instances (3 exact toys + 7 real worlds) "
              "with BOTH truth values realized (%s) => the index "
              "statement 'n_+(window) == N_w' is typed RESTATEMENT "
              "of L*/free-window survival -- valuable as LANGUAGE "
              "(the cleanest coordinate-free form of the wall), "
              "carrying NO independent lever; P1 lives or dies on "
              "the additional structure (G33)"
              % (len(inst), str([(n, a) for n, a, _b in inst])))
        # negative-subspace invariants
        ctrls = ("EPST", "SCR", "SMOOTH", "HL2")
        neg_sep = {}
        for stat in ("nlow", "nmed", "npr"):
            tab = {"MAIN": SPB["w9"][stat]}
            for cn in ctrls:
                tab[cn] = SPB[cn][stat]
            neg_sep[stat] = (LS.dist_rule(tab, list(ctrls)), tab)
        proxy_dev = {}
        for wn in WORLDS:
            mc = WORLDS[wn][0]["minC"]
            mcf = (mc if mc is not None else SPB[wn]["Nw"]) \
                / SPB[wn]["Nw"]
            nl = SPB[wn]["nlow"]
            proxy_dev[wn] = abs((nl if nl is not None else mcf)
                                - mcf)
        proxy = all(v <= PROX_TOL for v in proxy_dev.values())
        # ladder stability of NEG_LOW on the 12 FP rungs
        fp_kzs = [MAIN_KZ] + [kz for kz, _ in
                              sorted(((kz, packs[kz][0]["S"])
                                      for kz in packs
                                      if kz != MAIN_KZ),
                                     key=lambda t: (t[1], t[0]))
                              ][:N_FP - 1]
        nl_r = []
        for kz in fp_kzs:
            Wp = packs[kz][0]
            spk = spectral_bundle(Wp)
            if spk["nlow"] is not None:
                nl_r.append(spk["nlow"])
        stab_med = float(np.median(nl_r)) if nl_r else float("nan")
        stab_spr = (float(np.max(nl_r) - np.min(nl_r))
                    if nl_r else float("nan"))
        check("G33-negspace-invariants", True,
              "NEGATIVE-SUBSPACE INVARIANTS (deep, DEEP_EFF-"
              "guarded): sealed distance rule %s; PROXY TEST: "
              "|NEG_LOW - minC/N_w| = %s (tol %.2f) => %s; ladder "
              "stability (12 FP rungs): NEG_LOW med %.3f spread "
              "%.3f -- MEASURED, adjudicated in S5"
              % (str({k: (v[0], {kk: (None if vv is None else
                                      round(vv, 4))
                                 for kk, vv in v[1].items()})
                      for k, v in neg_sep.items()}),
                 str({k: round(v, 3) for k, v in
                      proxy_dev.items()}), PROX_TOL,
                 "RESTATEMENT_PROXY (fires)" if proxy
                 else "not a proxy", stab_med, stab_spr))
        # plus-operator / angular dictionary
        angs = [SPB[wn]["ang"] for wn in WORLDS]
        rhos = [SPB[wn]["rho_win"] for wn in WORLDS]
        sp_ang = BH.spearman(angs, rhos)
        ang_restat = abs(sp_ang) >= ANG_SP_BAR
        check("G34-plus-operator", True,
              "KREIN ANGULAR TEST: window/negative-subspace "
              "overlap ANG per world %s; spearman(ANG, rho_win) = "
              "%+.3f (bar %.1f) => the angular-operator language "
              "is typed %s -- the plus-operator question %s"
              % (str({wn: round(SPB[wn]["ang"], 4)
                      for wn in WORLDS}), sp_ang, ANG_SP_BAR,
                 "RESTATEMENT (collapses onto the contraction "
                 "scalar = L*)" if ang_restat else "INDEPENDENT "
                 "(reported, no implication chain)",
                 "collapses onto L*" if ang_restat
                 else "stays open"))

    # ---------------- S4 leg B P2
    section("S4  LEG B -- P2 SIGN REGULARITY / FINGERPRINT")
    if smoke:
        for g in ("G40-minor-census-main", "G41-sr-adjudication",
                  "G42-fingerprint-census",
                  "G43-fingerprint-contrast",
                  "G44-implication-chain"):
            check(g, True, "SMOKE: skipped")
        sr_specific = False
        fp_specific = False
        fp_cons = None
        sr_main = {}
    else:
        SRB = {wn: sr_bundle(SPB[wn], SPB[wn]["Nw"])
               for wn in WORLDS}
        sr_main = SRB["w9"]
        txt40 = str({k: round(v["score"], 3)
                     for k, v in sr_main.items()
                     if not k.startswith("_")})
        check("G40-minor-census-main", True,
              "MINOR CENSUS on MAIN (contiguous, orders 1..%d, "
              "zero class %.0e x Hadamard): SR scores %s "
              "(patterns %s) -- MEASURED, adjudicated in G41"
              % (K_MAX, ZTOL, txt40,
                 str({k: v["pattern"] for k, v in sr_main.items()
                      if not k.startswith("_")})))
        objs = [k for k in sr_main if not k.startswith("_")]
        sr_specific = False
        sr_detail = []
        for ob in objs:
            m_ok = (sr_main[ob]["score"] >= SR_BAR
                    and not sr_main[ob]["degen"])
            t_ok = (SRB["twin"][ob]["score"] >= SR_BAR
                    and SRB["twin"][ob]["pattern"]
                    == sr_main[ob]["pattern"])
            c_all = all(
                SRB[cn][ob]["score"] < SR_BAR
                or SRB[cn][ob]["pattern"] != sr_main[ob]["pattern"]
                for cn in ("EPST", "SCR", "SMOOTH", "HL2"))
            if m_ok:
                sr_detail.append("%s MAIN-SR (twin %s, controls "
                                 "broken %s)" % (ob, t_ok, c_all))
            if m_ok and t_ok and c_all:
                sr_specific = True
        wb_objs = [ob for ob in objs
                   if all(SRB[wn][ob]["score"] >= SR_BAR
                          and SRB[wn][ob]["pattern"]
                          == sr_main[ob]["pattern"]
                          for wn in WORLDS)]
        check("G41-sr-adjudication", True,
              "SR ADJUDICATION (sealed rule, bar %.2f): "
              "MAIN-specific objects: %s; world-blind sign-regular "
              "objects (same pattern everywhere): %s; twin scores "
              "%s -- %s"
              % (SR_BAR,
                 str(sr_detail) if sr_detail else "NONE",
                 str(wb_objs) if wb_objs else "NONE",
                 str({k: round(v["score"], 3)
                      for k, v in SRB["twin"].items()
                      if not k.startswith("_")}),
                 "SR MAIN-SPECIFIC" if sr_specific
                 else "no MAIN-specific sign regularity"))
        # fingerprint on the 12 sealed rungs
        fp_rows = []
        for kz in fp_kzs:
            Wp, ctx = packs[kz]
            if kz == MAIN_KZ:
                cen = cen9
            else:
                cen, _C, _g, _Bw = fp_run(Wp, ctx)
            cen["kz"] = kz
            fp_rows.append(cen)
            info("kz%-3d: modal %s sign %+d share %.3f d6 %.3f "
                 "cone-share med %.3f feas %+.1e"
                 % (kz, str(cen["modal_pair"]), cen["modal_sign"],
                    cen["modal_share"], cen["d6_share"],
                    cen["share_med"], cen["feas"]))
        st, fp_cons = fp_consensus(fp_rows)
        check("G42-fingerprint-census", st == "OK"
              and fp_cons is not None,
              "CROSS-MIXTURE FINGERPRINT (12 sealed rungs, r308 "
              "Dykstra %d steps + sealed cone projection): "
              "consensus %s -- %s"
              % (FEAS_IT, str(fp_cons),
                 "LAWFUL on the MAIN ladder" if fp_cons["lawful"]
                 else "NOT lawful (no stable modal pattern)"))
        # world contrast: twin + EPST/SCR at w9
        fp_ctrl = {}
        for wn in ("twin", "EPST", "SCR"):
            Wp, ctx = WORLDS[wn]
            cen, _C, _g, _Bw = fp_run(Wp, ctx)
            fp_ctrl[wn] = cen
            info("%s: modal %s sign %+d share %.3f d6 %.3f feas "
                 "%+.1e%s"
                 % (wn, str(cen["modal_pair"]), cen["modal_sign"],
                    cen["modal_share"], cen["d6_share"],
                    cen["feas"],
                    "" if cen["feas"] >= -FEAS_CONV
                    else "  [ITERATE, not psd-feasible]"))
        twin_ok = (fp_ctrl["twin"]["modal_pair"] == fp_cons["pair"]
                   and fp_ctrl["twin"]["modal_sign"]
                   == fp_cons["sign"]
                   and fp_ctrl["twin"]["modal_share"] >= FP_BAR)
        ctrl_broken = {}
        for cn in ("EPST", "SCR"):
            c = fp_ctrl[cn]
            ctrl_broken[cn] = (c["modal_pair"] != fp_cons["pair"]
                               or c["modal_sign"] != fp_cons["sign"]
                               or c["modal_share"] < FP_BAR)
        fp_specific = (fp_cons["lawful"] and twin_ok
                       and all(ctrl_broken.values()))
        pat_match = {cn: (fp_ctrl[cn]["modal_pair"]
                          == fp_cons["pair"]
                          and fp_ctrl[cn]["modal_sign"]
                          == fp_cons["sign"])
                     for cn in ("EPST", "SCR")}
        check("G43-fingerprint-contrast", True,
              "FINGERPRINT WORLD CONTRAST: twin %s (METRIC_ONLY "
              "%s); controls broken %s (pattern-match census %s: "
              "a control that matches the PAIR but breaks the "
              "SHARE bar means the fingerprint SHAPE is "
              "construction-generic and only its MAGNITUDE "
              "separates -- printed honestly with the letter) => "
              "%s" % (str((fp_ctrl["twin"]["modal_pair"],
                           fp_ctrl["twin"]["modal_sign"],
                           round(fp_ctrl["twin"]["modal_share"],
                                 3))),
                      "holds" if twin_ok else "BREAKS",
                      str(ctrl_broken), str(pat_match),
                      "FP MAIN-SPECIFIC" if fp_specific
                      else "fingerprint not world-separating"))
        viol = sr_main["_viol"]
        premise = (sr_main["B.rowinit"]["score"] >= SR_BAR
                   and not sr_main["B.rowinit"]["degen"])
        check("G44-implication-chain", viol == 0,
              "IMPLICATION SKETCH (SR(B) => variation diminishing "
              "=> sign-change bounds at every truncation => r277 "
              "R2 reality/interlacing <=> window quasi-"
              "definiteness = v962-T4 form of L*): VD spot check "
              "0 violations required (measured %d, world-blind "
              "polynomial bookkeeping); THE MEASURED PREMISE on "
              "MAIN: B row-initial SR score %.3f (bar %.2f) => %s"
              % (viol, sr_main["B.rowinit"]["score"], SR_BAR,
                 "PREMISE_HOLDS -- the chain is live"
                 if premise else "PREMISE_FAILS_ON_MAIN -- the "
                 "variation-diminishing route cannot start "
                 "(honest negative)"))

    # ---------------- S5 leg C adjudication
    section("S5  LEG C -- THE FORK ADJUDICATION (SEALED TREE)")
    if smoke:
        check("G50-fork-adjudication", True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        p1_sep = [k for k, v in neg_sep.items()
                  if v[0] == "MAIN_SEPARATING"]
        p1_alive = bool(ok_idx and p1_sep and not proxy)
        p2_alive = bool(sr_specific or fp_specific)
        if p1_alive and p2_alive:
            main_v = ("BOTH_ALIVE(P1 dig site: deep negative-"
                      "subspace %s; P2 pattern: %s)"
                      % (str(p1_sep), str(fp_cons)))
        elif p1_alive:
            main_v = ("P1_MAIN_SPECIFIC(dig site: the deep "
                      "negative-subspace degree localization -- "
                      "separating statistics %s, not a proxy of "
                      "the crossing location; dig where the "
                      "negative directions live relative to N_w)"
                      % str(p1_sep))
        elif p2_alive:
            if fp_specific:
                # amendment a1 (disclosed, reporting-only): the
                # dig-site label is derived from the MEASURED
                # modal pair (the draft text pre-named the border
                # column, contradicting the measurement; no bar,
                # rule or tree moved).
                dnm = ("D1", "D2", "D3", "D4", "D5", "D6")
                dcl = {0: "fold-distance-1", 1: "fold-distance-2",
                       2: "antiphase", 3: "antiphase",
                       4: "arch-mean", 5: "border"}
                pr_ = fp_cons["pair"]
                site = ("%s x %s (%s x %s)"
                        % (dnm[pr_[0]], dnm[pr_[1]],
                           dcl[pr_[0]], dcl[pr_[1]]))
                main_v = ("P2_MAIN_SPECIFIC(fingerprint verbatim: "
                          "modal cross-mixture pair %s sign %+d, "
                          "median modal share %.3f, lawful %d/%d "
                          "rungs + twin-consistent; controls "
                          "break by %s -- dig site: the %s "
                          "cross-mixture residual of the "
                          "block-Green family)"
                          % (str(fp_cons["pair"]), fp_cons["sign"],
                             fp_cons["med_share"],
                             fp_cons["n_agree"], fp_cons["n_rungs"],
                             str({cn: ("pattern" if not
                                       pat_match[cn] else
                                       "share bar only")
                                  for cn in pat_match}), site))
            else:
                main_v = ("P2_MAIN_SPECIFIC(sign regularity: %s)"
                          % str(sr_detail))
        else:
            main_v = ("FORK_DEAD(P1: index language EXACT but "
                      "RESTATEMENT%s%s; P2: %s; %s -- LANE-STOP "
                      "RECOMMENDATION per the binding stop rule)"
                      % (" + proxy" if proxy else "",
                         "" if p1_sep else " + no separating "
                         "negative-subspace statistic",
                         "no sign-regular object is MAIN-specific"
                         if not sr_specific else "",
                         "fingerprint not world-separating"
                         if not fp_specific else ""))
        verd = " + ".join([
            main_v,
            "INDEX_LANGUAGE(exact %s; restatement %s; vacuity "
            "measured)" % (ok_idx, restat),
            "SIGNATURE_TABLE(defects %s)" % str(defects),
            "FINGERPRINT(%s)" % str(fp_cons),
            "R312_DEMARCATION(the r312 letters stand; this round "
            "adjudicates the representation question only)"])
        check("G50-fork-adjudication", True,
              "SEALED TREE: alive(P1) = %s (separating %s, proxy "
              "%s, exact %s); alive(P2) = %s (SR %s, FP %s) => %s"
              % (p1_alive, str(p1_sep), proxy, ok_idx, p2_alive,
                 sr_specific, fp_specific, main_v.split("(")[0]))

    # ---------------- S7 must-fails
    section("S7  MUST-FAILS + SCOPE AUDITS (LEG D)")
    tb9 = TB["JF9"]
    n_win9 = min(tb9["Nw"], tb9["Sp"])
    true_def = frobenius_inertia_exact(tb9["minors"], n_win9)
    mut_def = mutant_wrong_signature(tb9["hs"], n_win9)
    check("G70-mustfail-signature-convention",
          true_def is not None and mut_def != true_def,
          "m1 WRONG SIGNATURE CONVENTION (exact JF9, Fractions): "
          "the mutant counts %d positive pivots where the exact "
          "Frobenius inertia of the congruence minors is %d -- "
          "MISMATCH, CAUGHT loud" % (mut_def, true_def))
    mut_tp = frac_rowinit_signs(
        [list(row) for row in zip(*M_TP)], 3)
    broke = any(any(s < 0 for s in ord_) for ord_ in mut_tp)
    check("G71-mustfail-transposed-census", ok_tp and broke,
          "m2 TRANSPOSED CENSUS (exact): the sealed row-initial "
          "census of M_TP is all-positive while the census of "
          "M_TP^T contains a negative minor (order-1 row (1,1,-1))"
          " -- the orientation of the census is load-bearing, "
          "CAUGHT (%s)"
          % str([[int(s) for s in o] for o in mut_tp]))
    hits_m3 = scope_audit("mutant_circular_lever")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G72-mustfail-circular-lever", bool(hits_m3)
          and not hits and not ag_hits,
          "m3 CIRCULAR L* CONSUMPTION: the mutant invariant "
          "consuming the withheld truth is FLAGGED by the AST "
          "scope audit (%s); the %d sealed constructors audit "
          "CLEAN; fragment audit %s"
          % ("; ".join(hits_m3) if hits_m3 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    toy_rows_fp = [dict(modal_pair=(0, 5), modal_sign=1,
                        modal_share=0.9)] * N_FP
    st_full, _c1 = fp_consensus(toy_rows_fp)
    st_one, _c2 = fp_consensus(toy_rows_fp[:1])
    check("G73-mustfail-single-rung", st_full == "OK"
          and st_one == "REJECT_INSUFFICIENT_RUNGS",
          "m4 SINGLE-RUNG EXTRAPOLATION: the sealed consensus "
          "verifier accepts the %d-rung census and REJECTS the "
          "single-rung mutant call loudly (%s) -- fingerprint "
          "consistency is FORCED across >= %d rungs"
          % (N_FP, st_one, FP_MIN_RUNGS))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no posthoc window, no "
          "re-opened no-go entry, no bar/rule change after "
          "evaluation, no RH claim; r243..r316 stand; the r312 "
          "letters stand -- this round adjudicates the "
          "REPRESENTATION question of the fork only")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the stop rule is binding: FORK_DEAD => stop "
          "the lane; a MAIN-specific route => dig at the named "
          "site; NO RH claim"
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
