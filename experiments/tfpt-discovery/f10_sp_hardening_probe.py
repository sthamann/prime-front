#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""f10_sp_hardening_probe -- PRIME.PORT.LSTAR.F10_SP_HARDENING.01
(round 295): HARDEN THE PARTIAL-FREE |sp| STATEMENT ON A LARGE
FRESH ENSEMBLE -- AND DISSECT WHAT DRIVES THE PARTIAL CHANNEL.
r294 sealed F10_FRAGILE: the |sp| win of the split-sealed
curvature energy F10 = x^T H_tr x / 2 over the home L2 size
baseline replicated on ALL five fresh corpora (sp +0.675..
+0.787 vs -0.660..-0.714, margins +0.003..+0.115), but the
partial-correlation channel did NOT replicate at its r293
magnitude (fresh median +0.299 against the sealed 0.3 bar; the
r293 +0.423 was top-of-distribution).  THIS ROUND does two
things and nothing else: (A) the partial-free statement as a
hard-tested theorem candidate -- TWENTY independent fresh
corpora against the UNCHANGED hash-sealed H_tr with a sealed
three-clause bar, ending either in a promotable weaker claim
for wave 8 or an honest death; (B) the partial ANATOMY --
composition decomposition of the partial channel by direction
family on the pooled ensemble, reconstruction of the r293
corpus composition, and the adjudication whether the r293
+0.423 was composition (PATH-heavy mix) or luck.  Bycatch:
(D) one small targeted 'why L2' test -- the conservation
geometry (eta_0 hyperplane projection).  NOT a proof round:
no L* claim, no bound mechanism, no asymptotic law, no
promotion (recommendation only).

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in
either direction.

MACHINERY IMPORTED VERBATIM (no duplication): r293 MR.
partial_sp + DEGEN_EPS; r292 CF.{unit_dir, pol_of_d2,
expand_of_d2, proj_coords, func_q10, auc_rank} + the r292
sealed Hessian constants (HESS_EQ_HS, H_PAIR_H, GCUT,
D2_FLOOR, POL_TOL, direction seeds 292100+/292200+,
TRAIN_FRAC/TRAIN_DENS, ENS_SCR_REPS/SEED_R285_SCR); r291 RA.
{subset_move, atom_ints, split_auditor,
mutant_broken_conservation} + AMP_PAD; r290 PFP.
{measure_density, lag_of, interp_density, dir_frac, dir_dens}
+ PATH_TS / DIST_GRID / RIDGE_FACS / NEAR / DEAD; r280 BL.
{grad_ext, dir_opt, theta_of_dir}; r278 MS.ctx_build; r276 MF.
{local_gaps, pert_jit, conserve_comb}; v881 PIK.{build_rung,
grid_density, lambda_eps}; r243 PB.smooth_comb; r244
BH.spearman; paircorr PC.{Grid, gen_model}; v563 core
READ-ONLY.  theta_eq = the r290-a1 LAG coordinate with the
ANALYTIC reference REF = 0.5 sum m g / Delta, gated on the
r290 pinned calibration quadruple VERBATIM.  Survival depth
s = minC / N_REF at w9 (N_REF = 184); everything in this
round is w9 (window transport was r294 Leg C and is NOT
re-litigated here).

INDEX FIREWALL (binding, r238-r294 discipline): ground truth
(minC, crossings, margins) enters GATES, the DISCLOSED
measurement-consuming training channel (H_tr / g_tr sealed by
the r292 split and RE-SEALED here against the published r294
hash 3447ed198a56 -- NO re-training, a GATE not a sentence)
and record tables only; the sealed source-pure constructors
consume vectors/densities + grid geometry + seeds ONLY (AST
scope audit); no zero/prime oracles anywhere (AST firewall).

LEG 0 -- ANCHOR REGRESSION (all gated): w9 record (S 367/263/
104, minC 184, crossing 185, margin 1.68e-4 rel 0.01, z_v
-3.149 tol 0.02, b34 -0.105 tol 0.01); theta_eq metric (REF ==
125.75 rel 1e-3, inversion identity 1e-12, r290 pinned
quadruple devs <= 0.15); control flips EPST/SCR/SMOOTH/HL2 =
25/21/27/25; r280 ridge anchor (theta_up 3.87e-5 rel 0.05, OPT
endpoint minC 185, top-9 atoms == the r291 record); the r292
29-direction Hessian REBUILT VERBATIM (a1 ladder, full 406-
pair polarization, expansion crosscheck on the 15 selected
pairs): trace share == 0.925 (tol 0.01), lam_top == -0.418
(rel 0.02), SMOOTH |cos| == 0.07 (tol 0.03), ridge L2-rank ==
28/29; H_tr / g_tr / G_tr on the 18 sealed r292 training
directions REBUILT and the hash GATED against the PUBLISHED
r294 seal prefix 3447ed198a56 (the strongest possible
no-re-training statement); the r292/r293 143-point corpus and
94-point test split rebuilt bit-identically (tag-list SHA
prefix a76cc578 gated) with the FULL r293 contest re-gated:
F10 sp == +0.884, F0_M1 == -0.907, F0_M2 == -0.860, AUC(dead)
== 0.097, partial == +0.423 test / +0.826 train-side (tol
0.005 each); the r293 test-split FAMILY CENSUS gated == (MAIN
1, WORLD 5, PATH 40, FRAC 25, DENS 15, ENS_SCR 8) -- the
composition object of Leg B.  R294 CORE REGRESSION (bitnear,
tol 0.005 each): the five r294 fresh corpora (seeds 294000 +
1000 k) REBUILT: sp(F10) +0.787/+0.675/+0.734/+0.720/+0.706
vs sp(F0_M2) -0.672/-0.660/-0.714/-0.684/-0.703, AUC 0.137/
0.142/0.230/0.132/0.142, win 5/5, partial median == 0.299;
the r294 jackknife REBUILT (leave-3-out rotations {j, j+5,
j+10}): sp +0.892/+0.867/+0.879/+0.866/+0.884, sigma ==
0.0101 (tol 0.001); the r294 rank truncation REBUILT: sp
r=1 +0.855 / r=2 +0.863 / r=4 +0.884, top-axis DENS
coefficient-mass share == 0.989.

LEG A -- THE 20-CORPUS ENSEMBLE (the hardening bar, sealed
BEFORE any evaluation): TWENTY independent fresh corpora,
corpus k = 0..19 uses seed base 300000 + 1000 k -- disjoint
by construction AND by gate from every r292 direction seed
(292100+/292200+), every r293 corpus seed, every r294 corpus
seed (294000..298000 bases) and every r294 window seed
(294700+); the FULL forbidden-seed set is enumerated and the
disjointness is a GATE, not a sentence.  Each corpus is built
by the UNCHANGED r294 Leg-A protocol (same conservation
discipline, same family mixture): MAIN (the disclosed shared
anchor) + 6 fresh dead worlds (2 SCR seeds base+1/+2 with
weights gated bitwise, 2 fresh HL2 combs seeds base+3/+4, 2
ENSR scrambles seeds base+5/+6 gated bitwise) + 4 paths x
PATH_TS (to SCR_a / HL2_a / ENSR_a / SCR_b) + 12 fresh FRAC
directions (seeds base+100+i, conservation exact) x DIST_GRID
+ 8 fresh DENS directions (seeds base+200+i, eta_0 projected
exactly) x DIST_GRID = 147 points >= 120.  ATOM/RIDGE points
remain EXCLUDED by the unchanged r292/r293 split seal.  Per
corpus k: F10 with the UNCHANGED H_tr (hash-gated == the
published r294 seal), F0_M2 = |delta|_L2, sp(F10, s),
sp(F0_M2, s), margin_k = |sp(F10)| - |sp(F0_M2)|, AUC(dead =
s < NEAR), partial sp(F10, s | F0_M2).  THE SEALED HARDENING
BAR (three clauses, fixed here before any corpus is built,
UNTOUCHABLE afterwards): F10_SP_HARDENED iff (#win >= 18/20)
AND (median of the 20 margins >= +0.02) AND (no corpus loses
by more than 0.02, i.e. min margin >= -0.02); else
F10_SP_MAJORITY iff #win in {14..17} OR (#win >= 18 with a
failed margin clause -- disclosed sub-case); else F10_SP_DEAD
(#win < 14) -- and then the weak partial-free form is dead
too and the r293 promotion-candidate marking is to be
retracted in the round report (sealed honestly here; nothing
is promoted or retracted inside experiments/ artifacts).
ALWAYS reported alongside (NOT bar-relevant): the partial
distribution over the 20 corpora (median, IQR q25/q75) -- the
honest continuation of the r294 measurement.

LEG B -- PARTIAL ANATOMY BY FAMILY (on the pooled ensemble,
MAIN pooled once, >= 2400 points): partial sp(F10, s | F0_M2)
separately per direction family -- PATH (interpolation paths
into the dead worlds = the WORLD-path family), WORLD (the
dead world points themselves), FRAC (random conserved
log-position combs), DENS (random eta_0-exact density
directions) -- and separately per dose regime (ALIVE s >=
NEAR vs BEYOND s < NEAR; the NEAR radius operationalized on
the survival readout, disclosed).  ATOM/RIDGE families are
structurally ABSENT from every fresh corpus by the unchanged
r292/r293 split seal (they are H_tr training directions);
their only honest partial is the r293 train-side value +0.826
re-gated in Leg 0 (disclosed, typed MEASUREMENT -- no fresh
ATOM ladder is built because that would break the seal).
Fine type PARTIAL_FAMILY_MAP(family: partial, n; STRONG iff
partial >= +0.4, NULL iff |partial| < 0.1).  R293 COMPOSITION
RECONSTRUCTION: the r293 test split census (gated in Leg 0)
is PATH-heavy (40/94 = 0.43 vs 40/147 = 0.27 in the fresh
protocol) and FRAC-light (25/94 = 0.27 vs 60/147 = 0.41); the
sealed composition-matched subsample per fresh corpus = MAIN
+ all 6 worlds + all 40 path points + the FIRST 5 FRAC seeds
(base+100..base+104) x DIST_GRID + the FIRST 3 DENS seeds
(base+200..base+202) x DIST_GRID = 87 points (family shares
PATH 0.46 / FRAC 0.29 / DENS 0.17 -- the closest
deterministic analog of the r293 mix; the r293 ENS_SCR
replicates have no fresh analog, disclosed approximation).
SEALED ADJUDICATION (exactly one): R293_COMPOSITION_EXPLAINED
iff median(matched partial over the 20) - median(full 147-
point partial over the 20) >= +0.05 AND median(matched) >=
0.35; else R293_LUCK (deltas always reported).  PRACTICAL
CONSEQUENCE (a definition, not a measurement): the sealed
composition-standardized partial statistic of future rounds
PARTIAL_STD = the partial on the FULL sealed 147-point fresh
protocol (family mix fixed by construction), reported as
median + IQR over the ensemble -- exactly the Leg-A side
report.

LEG C -- THE CANDIDATE STATEMENT (only on F10_SP_HARDENED):
if and only if the Leg-A bar holds, the round prints the
machine-checkable candidate statement for wave 8 (all
constants explicit: H_tr hash, metric, corpus protocol, bar)
-- the exact form a later v9xx promotion would embed.  NO
promotion here.  If the bar fails, Leg C is VOID without
replacement (no forced positivity).

LEG D -- WHY L2 (mechanism bycatch, small): the conservation
constraints define an affine subspace; on the density grid
the exact machine-checked constraint is the eta_0 functional
(s_l = 4 sin^2(pi l / L) / (2 L); DENS directions are built
eta_0-exact, FRAC/world deviations are not).  Test: L2-
project every test deviation onto the eta_0 hyperplane
{<s_hat, delta> = 0} (the 'physical' coordinate) and re-run
the F10-vs-baseline contest in the projection metric on the
bit-identical 94-point r293 split: F10_P = F10 o P, F0_P =
|P delta|_L2.  SEALED (exactly one): L2_VIA_CONSERVATION iff
the projected contest CONVERGES to the full-L2 contest (same
winner AND both |sp| shifts <= 0.02) -- then L2 is simply the
metric in which the conservation constraint is orthogonal and
the physical component carries everything; else L2_STILL_OPEN.
The projected-out eta_0 component share (median over the
split) is reported alongside (MEASUREMENT; a near-zero share
makes the test weak -- disclosed if so).

WARDS / MUST-FAILS (each loud): (m1) RE-TRAINING of H_tr (one
diagonal entry re-measured on a fresh corpus direction) must
be CAUGHT by the hash gate against the published r294 seal;
(m2) SEED COLLISION: a corpus built on the r294 base 294000
must be CAUGHT by the forbidden-seed auditor (the honest 20
bases show zero overlap); (m3) BAR SHARPNESS (both
directions): a synthetic ensemble at the exact bar (median
+0.02, min -0.02) must grade HARDENED, and mutations of the
RECORD margin list across each clause boundary (seven wins
flipped to losses; one margin pushed to -0.05; every margin
capped at +0.001) must each FLIP the grade away from
HARDENED -- the sealed bar has teeth on every clause; (m4) a
subset move with one weight scaled 1 + 1e-3 must be CAUGHT by
the exact r276 conservation gate.  Scope audits: the sealed
source-pure constructors consume vectors/densities + geometry
+ seeds only; H_tr / g_tr are honestly typed measurement-
consuming (split-sealed, hash-gated); fragment audit (no fit
fragments).  STOP LIST (anti-gates, binding): NO L* claim, NO
bound mechanism, NO asymptotic law, NO derived 5/7, NO
equidistribution premise, NO posthoc window, NO promotion
from here, NO RH claim; r243..r294 stand.

SEALED CONSTANTS: MAIN window 9; N_REF 184; CROSS_REC 185;
MINC_REC 184; S_REC (367, 263, 104); MARGIN_REC 1.68e-4 rel
0.01; ZV_REC -3.149 tol 0.02; B34_REC -0.105 tol 0.01;
CTRL_FLIPS EPST 25 / SCR 21 / SMOOTH 27 / HL2 25 (seed 101);
THUP_REC 3.87e-5 rel 0.05; RIDGE_MINC_REC 185; REF_REC 125.75
rel 1e-3; metric calibration = the r290 pinned quadruple
VERBATIM (CAL_SEEDS 290000/1/2 at 1e-3 + T3_SEED 290010 at
3e-4, tol 0.15); AMP_PAD 1 + 1e-9; NEAR 0.90 / DEAD 0.50;
top-9 atoms (2, 3, 5, 13, 11, 4, 29, 7, 89); r292 HESSIAN
PROTOCOL verbatim (HESS_EQ_HS (7.8125e-6, 1.5625e-5, 3.125e-5)
theta_eq / H_PAIR_H 1.5625e-5 / D2_FLOOR 0.5 / POL_TOL 0.25 /
GCUT 1e-10 / seeds 292100+ (10 FRAC) + 292200+ (6 DENS) /
TRAIN_FRAC (0, 2, 4, 6, 8) / TRAIN_DENS (0, 2, 4) / ENS_SCR
8 seeds 285100+); r292/r293 RECORDS adopted as gates:
SHARE_REC 0.925 tol 0.01 / LAMTOP_REC -0.418 rel 0.02 /
COS_SM_REC 0.07 tol 0.03 / RIDGE_RANK_REC 28 / TEST_N_REC 94 /
TAG_SHA_PREFIX a76cc578 / F10_SP_REC +0.884 / F0M1_SP_REC
-0.907 / F0M2_SP_REC -0.860 / AUC_REC 0.097 / PARTIAL_REC
+0.423 / PARTIAL_SIDE_REC +0.826 (tol 0.005 each) / R293
FAMILY CENSUS (1, 5, 40, 25, 15, 8); r294 RECORDS adopted as
gates: HTR_SHA_PREFIX 3447ed198a56 / R294 corpus sp table
(+0.787, +0.675, +0.734, +0.720, +0.706) vs (-0.672, -0.660,
-0.714, -0.684, -0.703) / AUC (0.137, 0.142, 0.230, 0.132,
0.142) / partial median 0.299 / jackknife sp (+0.892, +0.867,
+0.879, +0.866, +0.884) sigma 0.0101 tol 0.001 / rank sp
(+0.855, +0.863, +0.884) / DENS share 0.989 (tol 0.005 each
unless stated); LEG-A FRESH_BASE20 300000 / N_CORP20 20 /
BASE_STEP 1000 / N_FRAC_C 12 / N_DENS_C 8 / CORP_MIN_PTS 120
/ HARD_WIN_NEED 18 / MAJ_WIN_NEED 14 / MARGIN_MED_BAR +0.02 /
MARGIN_LOSS_MAX 0.02; LEG-B FAM_STRONG 0.4 / FAM_NULL 0.1 /
regime split at NEAR / MATCH_FRAC 5 / MATCH_DENS 3 /
R293_EXPL_GAIN +0.05 / R293_EXPL_LEVEL 0.35; LEG-D CONV_TOL
0.02 / eta_0 normal = unit s_l; ETA0_BAR 1e-12 / THETA_CAL
1e-3; runtime <= 1800 s; smoke = toys + firewall + scopes +
w9 regression + m2/m3-style mutants (anchors, legs, corpora,
adjudications skipped).
PRE-SPEC SCOPING (disclosed): every record number is a
published r276/r280/r290/r291/r292/r293/r294 record adopted
as-is; the 20-corpus construction with its seed plan, the
three-clause hardening bar with its grading, the family map
with its STRONG/NULL typing, the composition-matched
subsample rule with its adjudication, the conservation-
projection test with its convergence tolerance and the
must-fail set were fixed at design time from the published
records and the task contract; a design-time calibration
pass (disclosed below) preceded the freeze; no bar, band or
rule was tuned after the record freeze.

SEALED VERDICT FORM (frozen BEFORE the record freeze, joined
with '+'):
  CORPUS20_TABLE(per fresh corpus: sp(F10), sp(F0_M2),
    margin, partial; compact) [always]
  + [exactly one of] F10_SP_HARDENED(#win, margin median/min)
    / F10_SP_MAJORITY(#win, failed clauses) / F10_SP_DEAD(
    #win, weak form dead, r293 marking to be retracted)
  + PARTIAL20(median, IQR) [always, NOT bar-relevant]
  + PARTIAL_FAMILY_MAP(per family: partial, n, typing;
    regime split alongside) [always]
  + [exactly one of] R293_COMPOSITION_EXPLAINED(deltas) /
    R293_LUCK(deltas)
  + [exactly one of] CANDIDATE_STATEMENT(printed, wave-8
    form) / LEGC_VOID(bar not met)
  + [exactly one of] L2_VIA_CONSERVATION(shifts) /
    L2_STILL_OPEN(shifts, eta_0 share).
Honesty before beauty: every correlation and Hessian entry is
a MEASUREMENT on finite profile space; H_tr is the UNCHANGED
r293 object (hash-gated against the PUBLISHED r294 seal --
re-training is structurally impossible without failing G40);
the 20 fresh corpora share exactly ONE point (MAIN) with each
other and with r293/r294 (disclosed); the partial family map
and the composition adjudication are MEASUREMENTS about a
correlation statistic, not about L*; the hardening bar
grades a RANKING statement, not a bound; no verdict claims
L*, a bound mechanism, a derived 5/7 or an asymptotic law;
the promotion decision itself belongs to the consolidation
wave, NOT to this probe.  NO RH CLAIM in either direction.
NOT evidence for or against RH.

RECORD TABLES (frozen from the record run; calibration
protocol, chronology honest: smoke pass 1 = 11/11 (0.1 s);
calibration pass 1 = first full evaluation = 44/44, wall 144
s -- NO gate failed, NO adjudicated number changed and NO
display fix was needed: the calibration pass IS the record
physics unchanged; record run1/run2 = 44/44 each (wall 143.3
/ 143.0 s), byte-identical up to WALL; the record-table
insertion below is the only post-freeze edit, which IS the
protocol; record rerun after insertion gated again 44/44,
run1/run2 identical up to WALL).
RECORD VERDICT = CORPUS20_TABLE(twenty fresh 147-point
corpora, conservation/eta_0/scramble weights exact, seeds
disjoint from r292/r293/r294 by gate, s ranges [0.02..1.01]:
K00 +0.707/-0.651 m +0.056 p +0.364; K01 +0.741/-0.650 m
+0.092 p +0.477; K02 +0.633/-0.606 m +0.027 p +0.251; K03
+0.714/-0.595 m +0.119 p +0.504; K04 +0.757/-0.739 m +0.018
p +0.289; K05 +0.610/-0.689 m -0.079 p -0.133; K06 +0.699/
-0.670 m +0.029 p +0.270; K07 +0.629/-0.686 m -0.057 p
+0.003; K08 +0.703/-0.640 m +0.063 p +0.387; K09 +0.779/
-0.654 m +0.125 p +0.566; K10 +0.684/-0.649 m +0.034 p
+0.313; K11 +0.727/-0.618 m +0.108 p +0.490; K12 +0.649/
-0.659 m -0.010 p +0.176; K13 +0.656/-0.668 m -0.012 p
+0.165; K14 +0.687/-0.671 m +0.015 p +0.264; K15 +0.690/
-0.594 m +0.096 p +0.442; K16 +0.618/-0.595 m +0.023 p
+0.243; K17 +0.764/-0.731 m +0.034 p +0.339; K18 +0.656/
-0.669 m -0.013 p +0.184; K19 +0.687/-0.727 m -0.041 p
+0.090) + F10_SP_MAJORITY(the honest center of the round:
win 14/20 -- the sealed HARDENED bar fails on TWO clauses
(win 14 < 18; min margin -0.079 < -0.02; the median clause
alone would have passed at +0.028 >= +0.02): the r294 5/5
was itself TOP-OF-DISTRIBUTION -- on a 20-corpus ensemble
F10 loses the |sp| contest against the home L2 baseline on
6 corpora (losses -0.010, -0.012, -0.013, -0.041, -0.057,
-0.079), three of them well beyond the -0.02 floor; the
partial-free statement is NOT a theorem candidate but a
DOCUMENTED REGULARITY (14/20 wins, margin median +0.028,
combined census 19/25 with r294); promotion recommendation
NO for wave 8 -- honest and final under the sealed bar) +
PARTIAL20(median +0.279, IQR [+0.182, +0.401], range
[-0.133, +0.566], 20/20 finite: the honest continuation of
r294 -- the partial channel sits at ~0.28 with a WIDE
spread; the r293 +0.423 sits at the 75th-percentile edge,
again top-of-distribution) + PARTIAL_FAMILY_MAP(pooled 2921
points: PATH +0.156 (n 800) weak / WORLD +0.245 (n 120)
weak / FRAC +0.067 (n 1200) NULL / DENS +0.104 (n 800)
weak; regime split: PATH ALIVE +0.123 (125) / BEYOND +0.150
(675), WORLD ALIVE DEGEN (0) / BEYOND +0.245 (120), FRAC
ALIVE +0.022 (384) / BEYOND +0.045 (816), DENS ALIVE -0.129
(19) / BEYOND +0.090 (781): NO family reaches the STRONG
bar on the pool -- the beyond-distance information is
diffuse, strongest on WORLD/PATH points (structured
deviations toward dead worlds), near-NULL on random FRAC
rays; the pooled family map is WEAKER than the per-corpus
partials because pooling across corpora mixes 20 different
F10-vs-s calibrations, disclosed) + R293_LUCK(matched
median +0.346, full median +0.279, gain +0.067: the sealed
gain clause (>= +0.05) PASSES but the sealed level clause
fails by 0.004 (0.346 < 0.35) -- under the sealed
adjudication the r293 +0.423 is typed LUCK; the honest
nuance stands in the numbers: the r293 PATH-heavy mix DOES
lift the partial (+0.067 median gain, matched IQR [+0.078,
+0.410]), i.e. composition explains PART of the r293/r294
discrepancy but does not reach the r293 magnitude -- the
rest was sampling luck at n = 94) + LEGC_VOID(the Leg-A bar
did not hold -- no candidate statement, no forced
positivity) + L2_VIA_CONSERVATION(same winner after the
eta_0 projection, |sp| shifts F10 0.0000 / F0_M2 0.0000 <=
0.02, projected-out eta_0 share median 2.9e-30 (max
3.2e-03): the contest is INVARIANT under the conservation
projection -- but the eta_0 component of the corpus
deviations is numerically negligible, the invariance is
near-tautological; honest reading: the conservation
constraint is already orthogonal to the corpus in plain L2
and the projection test cannot decide 'why L2' -- the
mechanism question stays OPEN in substance, typed as the
sealed convergence outcome with the weakness disclosed).
Key numbers.  W9: S 367/263/104, minC 184, crossing 185,
margin 1.6752e-4, z_v -3.149, b34 -0.105; REF 125.7462,
inversion 1.5e-16, quadruple devs (0.059, 0.125, 0.117,
0.028); flips 25/21/27/25 == records; theta_up 3.8733e-5,
endpoint minC 185, top-9 atoms == record.  R292/R293
REGRESSION: share 0.925, lam_top -0.418, SMOOTH |cos| 0.07,
ridge rank 28/29; corpus 143, test split 94, tag SHA
a76cc57851826476 == prefix; F10 +0.884 / F0_M1 -0.907 /
F0_M2 -0.860 / AUC 0.097 / partial +0.423 / side +0.826 ==
records; H_tr hash 3447ed198a56530d == the PUBLISHED r294
seal (G40 gate); r293 family census (1, 5, 40, 25, 15, 8)
== sealed, PATH share 0.43 vs 0.27 fresh.  R294 REGRESSION:
all five corpus sp/AUC values == records (tol 0.005), win
5/5, partial median 0.299 == 0.299; jackknife sp == records,
sigma 0.0101; rank sp (+0.855, +0.863, +0.884), DENS share
0.989.  LEG A: 20 x 147 points, sizes all 147; 240 fresh
FRAC + 160 fresh DENS directions conservation/eta_0 exact;
192 forbidden seeds enumerated, overlap 0 on all 20 bases,
pairwise tag overlaps 0.  LEG B: pool 2921 points (MAIN
once); cells WORLD 120 / PATH 800 / FRAC 1200 / DENS 800;
matched subsamples 87 points each.  MUST-FAILS: m1 CAUGHT
(retrained-entry hash 9f2123292279 != published seal
3447ed198a56), m2 CAUGHT (26 forbidden-seed overlaps on the
r294 base 294000; honest bases 0), m3 bar sharpness ALL
probes pass (exact-bar synthetic grades HARDENED; min-margin
mutant -> DEAD, win-count mutant -> DEAD, median mutant ->
MAJORITY), m4 CAUGHT (conservation gate False); scopes +
fragments CLEAN.  Runtime 143 s full / 0.1 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE:
NONE (records inserted per protocol; no calibration fix was
needed; no physics bar, class rule or verdict rule moved).
READING (typed MEASUREMENT): the hardening round is an
HONEST NEGATIVE with a mechanical bycatch: (A) the
partial-free ranking statement does NOT harden -- on 20
fresh corpora F10 beats the home L2 baseline only 14/20
(margin median +0.028, but one loss at -0.079), far from
the sealed 18/20 + no-loss-beyond-0.02 bar; the r294 5/5
was top-of-distribution exactly the way the r293 partial
was: each new, larger ensemble has demoted the previous
round's headline number -- the F10-vs-baseline edge is
REAL as a tendency (19/25 total fresh-corpus wins, median
margin positive) but NOT stable enough for a wave-8
statement; promotion recommendation NO, Leg C void;
(B) the partial anatomy: no direction family is STRONG on
the pooled ensemble (PATH +0.16, WORLD +0.25, FRAC +0.07
NULL, DENS +0.10) and the r293-composition-matched
subsample lifts the median partial by +0.067 but misses
the sealed level by 0.004 -> R293_LUCK: composition
explains PART of the r293 top-of-distribution partial, the
rest was n=94 sampling noise; the honest standardized
statistic going forward is PARTIAL_STD = +0.279 IQR
[+0.182, +0.401] at the sealed 147-point mix; (C) the
eta_0 conservation projection leaves the contest exactly
invariant but only because the corpus barely excites the
constraint direction -- 'why L2' stays open.  Consequence
for the program: the F10 curvature-energy front should
either find a SHARPER functional (the rank-2 DENS core of
r294 as a starting point) or an explanation why the edge
fluctuates corpus-to-corpus (the 6 losing corpora are a
concrete forensic target: what distinguishes K05/K07/K19?)
before any promotion attempt.  NO RH CLAIM in either
direction.  NOT evidence for or against RH.
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

import metric_reconciliation_probe as MR             # noqa: E402 r293
import curvature_form_probe as CF                    # noqa: E402 r292
import ridge_anatomy_probe as RA                     # noqa: E402 r291
import profile_functional_probe as PFP               # noqa: E402 r290
import metric_stability_probe as MS                  # noqa: E402 r278
import minimal_firewall_probe as MF                  # noqa: E402 r276
import budget_localization_probe as BL               # noqa: E402 r280
import port_integrable_kernel_probe as PIK           # noqa: E402 v881
import principal_bessel_probe as PB                  # noqa: E402 r243
import bordered_hankel_probe as BH                   # noqa: E402 r244
import paircorr_margin_probe as PC                   # noqa: E402
import v563_paper2_readouts as core                  # noqa: E402 READ-ONLY

MAIN_KZ = 9
N_REF = 184
CROSS_REC = 185
MINC_REC = 184
S_REC = (367, 263, 104)
MARGIN_REC = 1.68e-4
MARGIN_TOL = 0.01
ZV_REC = -3.149
ZV_TOL = 0.02
B34_REC = -0.105
B34_TOL = 0.01
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27, "HL2": 25}
HL2_SEED = 101
THUP_REC = 3.87e-5
THUP_TOL = 0.05
RIDGE_MINC_REC = 185
REF_REC = 125.75
REF_TOL = 1e-3
NEAR = PFP.NEAR
DEAD = PFP.DEAD
PATH_TS = PFP.PATH_TS
DIST_GRID = PFP.DIST_GRID
AMP_PAD = RA.AMP_PAD
CAL_SEEDS = (290000, 290001, 290002)
T3_SEED = 290010
T3_THETA = 3e-4
T3_TOL = 0.15
THETA_CAL = 1e-3
ETA0_BAR = 1e-12
R291_TOP9 = (2, 3, 5, 13, 11, 4, 29, 7, 89)

# r292 Hessian protocol adopted verbatim (imported constants)
HESS_EQ_HS = CF.HESS_EQ_HS
H_PAIR_H = CF.H_PAIR_H
D2_FLOOR = CF.D2_FLOOR
POL_TOL = CF.POL_TOL
GCUT = CF.GCUT
NDIR_FRAC = CF.NDIR_FRAC
SEED_FRAC = CF.SEED_FRAC
NDIR_DENS = CF.NDIR_DENS
SEED_DENS = CF.SEED_DENS
N_ATOM = CF.N_ATOM
TRAIN_FRAC = CF.TRAIN_FRAC
TRAIN_DENS = CF.TRAIN_DENS
ENS_SCR_REPS = CF.ENS_SCR_REPS
SEED_R285_SCR = CF.SEED_R285_SCR

# r292/r293 records adopted as Leg-0 gates
R292_SHARE_REC = 0.925
R292_SHARE_TOL = 0.01
R292_LAMTOP_REC = -0.418
R292_LAMTOP_TOL = 0.02
R292_COS_SM_REC = 0.07
R292_COS_SM_TOL = 0.03
R292_RIDGE_RANK_REC = 28
R292_TEST_N_REC = 94
TAG_SHA_PREFIX = "a76cc578"
R293_F10_SP_REC = 0.884
R293_F0M1_SP_REC = -0.907
R293_F0M2_SP_REC = -0.860
R293_AUC_REC = 0.097
R293_PARTIAL_REC = 0.423
R293_PARTIAL_SIDE_REC = 0.826
R293_SP_TOL = 0.005
R293_FAM_CENSUS = (1, 5, 40, 25, 15, 8)   # MAIN/WORLD/PATH/FRAC/DENS/ENS

# r294 records adopted as Leg-0 gates
HTR_SHA_PREFIX = "3447ed198a56"
R294_BASE = 294000
R294_N_CORP = 5
R294_SPF_REC = (0.787, 0.675, 0.734, 0.720, 0.706)
R294_SPB_REC = (-0.672, -0.660, -0.714, -0.684, -0.703)
R294_AUC_REC = (0.137, 0.142, 0.230, 0.132, 0.142)
R294_PART_MED_REC = 0.299
R294_JACK_REC = (0.892, 0.867, 0.879, 0.866, 0.884)
R294_JACK_SIG_REC = 0.0101
R294_JACK_SIG_TOL = 0.001
R294_RANK_REC = (0.855, 0.863, 0.884)
R294_DENS_SHARE_REC = 0.989
R294_TOL = 0.005

# Leg A (sealed before any corpus is built)
FRESH_BASE20 = 300000
N_CORP20 = 20
BASE_STEP = 1000
N_FRAC_C = 12
N_DENS_C = 8
CORP_MIN_PTS = 120
HARD_WIN_NEED = 18
MAJ_WIN_NEED = 14
MARGIN_MED_BAR = 0.02
MARGIN_LOSS_MAX = 0.02

# Leg B (sealed)
FAM_STRONG = 0.4
FAM_NULL = 0.1
MATCH_FRAC = 5
MATCH_DENS = 3
R293_EXPL_GAIN = 0.05
R293_EXPL_LEVEL = 0.35
POOL_MIN = 2400

# Leg D (sealed)
CONV_TOL = 0.02

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
    return (not bad), ("NO zero/prime oracles; record numbers enter "
                       "gates and record tables only; the atom labels "
                       "are the r291 integer-root ranking adopted as a "
                       "record" if not bad else "; ".join(bad))


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


CONSTRUCTORS = ("cons_proj", "grade_of", "med_iqr", "seeds_of_base")
SCOPE_FORBIDDEN = {"minC", "mc", "zv", "onsets_true", "MINC_REC",
                   "CROSS_REC", "ZV_REC", "sg_h", "lgh", "s_meas"}


def scope_audit(funcname, forbidden):
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


# ============== sealed source-pure constructors (AST-audited)
def cons_proj(delta, nhat):
    """L2 projection of a deviation onto the conservation
    hyperplane {<nhat, x> = 0} for a UNIT normal nhat:
    P delta = delta - <nhat, delta> nhat.  Consumes vectors
    only."""
    d = np.asarray(delta, float)
    n = np.asarray(nhat, float)
    return d - float(n @ d) * n


def grade_of(margins):
    """SEALED three-clause hardening grade of an ensemble of
    contest margins (margin = |corr(F10)| - |corr(baseline)|):
    HARDENED iff (#positive >= 18) AND (median >= +0.02) AND
    (min >= -0.02); else MAJORITY iff #positive >= 14; else
    DEAD.  Consumes a float list only."""
    m = [float(v) for v in margins]
    nw = sum(1 for v in m if v > 0.0)
    med = float(np.median(m))
    if nw >= HARD_WIN_NEED and med >= MARGIN_MED_BAR \
            and min(m) >= -MARGIN_LOSS_MAX:
        return "HARDENED"
    if nw >= MAJ_WIN_NEED:
        return "MAJORITY"
    return "DEAD"


def med_iqr(vals):
    """median and interquartile range (q25, q75) of a float
    list (numpy linear interpolation, deterministic).
    Consumes a float list only."""
    a = np.asarray([float(v) for v in vals], float)
    return (float(np.median(a)),
            float(np.percentile(a, 25.0)),
            float(np.percentile(a, 75.0)))


def seeds_of_base(base):
    """the full seed set of one sealed 147-point fresh corpus
    at a given base: worlds base+1..+6, FRAC base+100+i
    (12), DENS base+200+i (8).  Consumes an integer only."""
    b = int(base)
    return set([b + i for i in range(1, 7)]
               + [b + 100 + i for i in range(N_FRAC_C)]
               + [b + 200 + i for i in range(N_DENS_C)])


# forbidden-seed set (every seed consumed by r292/r293/r294)
def _forbidden_seeds():
    forb = {1, HL2_SEED, T3_SEED}
    forb |= set(CAL_SEEDS)
    forb |= {SEED_R285_SCR + i for i in range(ENS_SCR_REPS)}
    forb |= {SEED_FRAC + i for i in range(NDIR_FRAC)}
    forb |= {SEED_DENS + i for i in range(NDIR_DENS)}
    for k in range(R294_N_CORP):
        forb |= seeds_of_base(R294_BASE + BASE_STEP * k)
    for wi in range(2):                       # r294 window seeds
        wsd = 294700 + 50 * wi
        forb |= {wsd + i for i in range(4)}
        forb |= {wsd + 10 + i for i in range(3)}
        forb |= {wsd + 20 + i for i in range(4)}
        forb |= {wsd + 30 + i for i in range(2)}
        forb |= {wsd + 40 + i for i in range(3)}
    return forb


FORBIDDEN_SEEDS = _forbidden_seeds()


# ============== must-fail helpers
def mutant_seed_reuse_tags(tags_a, tags_b):
    """m2-style MUST-FAIL helper: the r291 tag auditor must
    flag any overlap."""
    return RA.split_auditor(set(tags_a), set(tags_b))


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("f10_sp_hardening_probe -- PRIME.PORT.LSTAR."
          "F10_SP_HARDENING.01 (round 295)")
    print("SPEC_SHA %s   (r293 MR %s / r292 CF %s / r290 PFP %s)"
          % (SPEC_SHA[:16], MR.SPEC_SHA[:16], CF.SPEC_SHA[:16],
             PFP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + w9 "
                        "regression + m2/m3-style mutants; anchors, "
                        "legs, corpora, adjudications skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the 20-corpus plan (seeds "
          "300000+1000k, 147 points each, r294 protocol verbatim, "
          "forbidden-seed set enumerated and gated), the THREE-"
          "CLAUSE hardening bar (win >= 18/20 AND margin median "
          ">= +0.02 AND min margin >= -0.02 -> HARDENED; win >= "
          "14 -> MAJORITY; else DEAD), the family map with "
          "STRONG/NULL typing (0.4 / 0.1), the r293 composition-"
          "matched subsample rule (all paths + first 5 FRAC + "
          "first 3 DENS seeds) with its adjudication (gain >= "
          "+0.05 AND level >= 0.35), the eta_0 conservation-"
          "projection test with CONV_TOL 0.02 and the must-fail "
          "set; H_tr / g_tr honestly typed measurement-consuming "
          "and hash-gated against the PUBLISHED r294 seal; the "
          "STOP list forbids any L* claim, any promotion from "
          "here and any proof attack")

    # ---------------- S1 toys
    section("S1  TOYS -- CONS PROJECTION, GRADE, MED/IQR, PARTIAL")
    nh_t = np.array([1.0, 0.0, 0.0])
    d_t = np.array([2.0, 1.0, 1.0])
    p_t = cons_proj(d_t, nh_t)
    p2_t = cons_proj(p_t, nh_t)
    ok_t1 = (float(np.max(np.abs(p_t - np.array([0.0, 1.0, 1.0]))))
             <= 1e-12
             and float(np.max(np.abs(p2_t - p_t))) <= 1e-12
             and abs(float(nh_t @ p_t)) <= 1e-12)
    check("G10-toy-cons-proj", ok_t1,
          "HAND PROJECTION (normal e1, delta = (2, 1, 1)): P d = "
          "(0, 1, 1) exact, idempotent, <n, P d> = 0 exact")
    g_a = grade_of([0.05] * 18 + [-0.019, -0.001])
    g_b = grade_of([0.05] * 17 + [-0.019, -0.011, -0.001])
    g_c = grade_of([0.05] * 19 + [-0.03])
    g_d = grade_of([0.019] * 20)
    g_e = grade_of([0.05] * 13 + [-0.01] * 7)
    ok_t2 = (g_a == "HARDENED" and g_b == "MAJORITY"
             and g_c == "MAJORITY" and g_d == "MAJORITY"
             and g_e == "DEAD")
    check("G11-toy-grade", ok_t2,
          "HAND GRADING TABLE: exact-bar quintets -- 18 wins/med "
          "0.05/min -0.019 -> %s (== HARDENED); 17 wins -> %s; "
          "19 wins but one -0.03 loss -> %s; 20 wins but median "
          "0.019 -> %s; 13 wins -> %s -- every sealed clause "
          "discriminates" % (g_a, g_b, g_c, g_d, g_e))
    md_t, q1_t, q3_t = med_iqr([1.0, 2.0, 3.0, 4.0, 5.0])
    ok_t3 = (abs(md_t - 3.0) <= 1e-12 and abs(q1_t - 2.0) <= 1e-12
             and abs(q3_t - 4.0) <= 1e-12)
    psp_t = MR.partial_sp([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 4, 3])
    check("G12-toy-mediqr-partial", ok_t3
          and abs(psp_t - 1.0) <= 1e-12,
          "HAND MED/IQR on (1..5) = (%.1f, %.1f, %.1f) == "
          "(3, 2, 4) exact; MR.partial_sp identity toy == 1 "
          "exact (the r293 sealed partial reused verbatim)"
          % (md_t, q1_t, q3_t))
    sb_t = seeds_of_base(FRESH_BASE20)
    ok_t4 = (len(sb_t) == 6 + N_FRAC_C + N_DENS_C
             and not (sb_t & FORBIDDEN_SEEDS))
    check("G13-toy-seed-audit", ok_t4,
          "HAND SEED SET at base %d: %d seeds (6 worlds + %d "
          "FRAC + %d DENS), overlap with the %d enumerated "
          "forbidden r292/r293/r294 seeds = 0"
          % (FRESH_BASE20, len(sb_t), N_FRAC_C, N_DENS_C,
             len(FORBIDDEN_SEEDS)))

    # ---------------- S2 w9 + anchors
    section("S2  W9 REGRESSION + METRIC + RIDGE ANCHORS")
    ctx9 = MS.ctx_build(MAIN_KZ)
    d9 = np.asarray(ctx9["darm"], float)
    L9 = int(ctx9["L"])
    uu9 = np.asarray(ctx9["uu"], float)
    mm9 = np.asarray(ctx9["mm"], float)
    M9 = L9 // 2 + 1
    M0 = PFP.measure_density(d9, L9)
    margin9 = 1.0 - M0["rho"][N_REF]
    ok_w9 = ((M0["S"], M0["Sp"], M0["Sm"]) == S_REC
             and M0["minC"] == MINC_REC
             and M0["cross"] == CROSS_REC
             and abs(margin9 / MARGIN_REC - 1.0) <= MARGIN_TOL
             and abs(M0["zv"] - ZV_REC) <= ZV_TOL
             and abs(M0["b34"] - B34_REC) <= B34_TOL)
    check("G20-w9-regression", ok_w9,
          "w9 through the r290 channel: S = %d (mu %d / nu %d), "
          "minC = %s, crossing = %s, margin %.4e (rec %.2e), z_v "
          "= %+.3f, b34 = %+.3f"
          % (M0["S"], M0["Sp"], M0["Sm"], str(M0["minC"]),
             str(M0["cross"]), margin9, MARGIN_REC, M0["zv"],
             M0["b34"]))
    if smoke:
        ov_s = seeds_of_base(R294_BASE) & FORBIDDEN_SEEDS
        check("G86-mustfail-seed-reuse", len(ov_s) == 26,
              "m2 SEED REUSE (toy: the r294 base 294000 against "
              "the forbidden set): %d overlaps -- CAUGHT"
              % len(ov_s))
        gm_s = grade_of([0.05] * 19 + [-0.05])
        check("G87-mustfail-bar-flip", gm_s != "HARDENED",
              "m3 BAR FLIP (toy: one corpus pushed to a -0.05 "
              "loss): grade %s != HARDENED -- the min-margin "
              "clause has teeth" % gm_s)
        hits_s = []
        for fn_ in CONSTRUCTORS:
            hits_s += scope_audit(fn_, SCOPE_FORBIDDEN)
        ag_s = antigate_fragment_audit()
        check("G89-scope-audits", not hits_s and not ag_s,
              "the %d sealed source-pure constructors consume "
              "vectors/densities + geometry + seeds ONLY (%s); "
              "fragment audit: %s"
              % (len(CONSTRUCTORS),
                 "CLEAN" if not hits_s else "; ".join(hits_s),
                 "CLEAN" if not ag_s else "; ".join(ag_s)))
        return finish(smoke)

    # metric anchor (r290-a1 coordinate, pinned quadruple verbatim)
    g_loc = MF.local_gaps(uu9)
    Dg9 = 2.0 * ctx9["alpha"] / ctx9["M"]
    REF = 0.5 * float(np.sum(mm9 * g_loc)) / Dg9

    def lag_l1(dd):
        return float(np.sum(np.abs(PFP.lag_of(dd, M9))))

    c_back = PFP.lag_of(d9, M9)
    inv_dev = float(np.max(np.abs(PIK.grid_density(c_back) - d9))) \
        / max(float(np.max(np.abs(d9))), 1e-300)
    devs_c = []
    cons_c = True
    for th_c, seed_c in [(THETA_CAL, s_) for s_ in CAL_SEEDS] \
            + [(T3_THETA, T3_SEED)]:
        u2c, m2c = MF.pert_jit(uu9, mm9, th_c, seed_c, False)
        cons_c = cons_c and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2c, m2c, th_c)
        d2c = np.asarray(PIK.build_rung(MAIN_KZ,
                                        comb=(u2c, m2c))["d"], float)
        devs_c.append(abs(lag_l1(d2c - d9) / REF / th_c - 1.0))
    ok_met = (abs(REF / REF_REC - 1.0) <= REF_TOL
              and inv_dev <= 1e-12 and cons_c
              and max(devs_c) <= T3_TOL)
    check("G21-metric-anchor", ok_met,
          "theta_eq metric (r290-a1 LAG coordinate, pinned "
          "quadruple VERBATIM): analytic REF = %.4f (rec %.2f); "
          "inversion identity rel %.1e; jitter devs %s <= %.2f, "
          "conservation exact"
          % (REF, REF_REC, inv_dev,
             str([round(v, 3) for v in devs_c]), T3_TOL))
    # control worlds (r291/r292/r293 constructions verbatim)
    rr9 = core.build_window(MAIN_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    uE = np.log(nn_idx.astype(float))
    mE = 2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    gpc = PC.Grid()
    comb_hl, _tag = PC.gen_model(gpc, "HL2", HL2_SEED)
    d_worlds = {
        "SMOOTH": np.asarray(MS.ctx_build(
            MAIN_KZ, comb=(ug9, uw9))["darm"], float),
        "SCR": np.asarray(MS.ctx_build(
            MAIN_KZ, scramble_seed=1)["darm"], float),
        "EPST": np.asarray(MS.ctx_build(
            MAIN_KZ, comb=(uE, mE))["darm"], float),
        "HL2": np.asarray(MS.ctx_build(
            MAIN_KZ, comb=comb_hl)["darm"], float),
        "ENSR": np.asarray(MS.ctx_build(
            MAIN_KZ, scramble_seed=SEED_R285_SCR)["darm"], float)}
    worlds_meas = {w: PFP.measure_density(d_worlds[w], L9)
                   for w in d_worlds}
    ok_fl = all(worlds_meas[w]["minC"] == CTRL_FLIPS[w]
                for w in CTRL_FLIPS)
    check("G22-control-flips", ok_fl,
          "control flips through this channel: %s == records "
          "(25/21/27/25)"
          % str({w: worlds_meas[w]["minC"] for w in CTRL_FLIPS}))
    # ridge anchor (r280 rebuilt verbatim) + top-9 atom ranking
    GE = BL.grad_ext(ctx9, N_REF + 2)
    xi = BL.dir_opt(GE["gR"], GE["gL"], GE["gaps"], N_REF)
    th_up, th_kill, cvec = BL.theta_of_dir(GE["gR"], GE["gL"],
                                           GE["gaps"], xi, N_REF)
    du_ridge = 2.0 * th_up * GE["gaps"] * xi
    uR, mR = RA.subset_move(uu9, mm9, du_ridge, np.ones(len(uu9)))
    dR = np.asarray(PIK.build_rung(MAIN_KZ, comb=(uR, mR))["d"],
                    float)
    MRi = PFP.measure_density(dR, L9)
    du1 = GE["gaps"] * xi
    cj = np.where(du1 > 0, du1 * GE["gR"][:, N_REF],
                  du1 * GE["gL"][:, N_REF])
    nn_at = RA.atom_ints(uu9)
    order = np.argsort(cj)
    top9 = tuple(int(v) for v in nn_at[order[:N_ATOM]])
    ok_ridge = (abs(th_up / THUP_REC - 1.0) <= THUP_TOL
                and th_kill > th_up
                and MRi["minC"] == RIDGE_MINC_REC
                and MF.conserve_comb("P2_JIT", uu9, mm9, uR, mR,
                                     2.0 * th_up * AMP_PAD)
                and top9 == R291_TOP9)
    check("G23-ridge-anchor", ok_ridge,
          "r280 RIDGE ANCHOR: theta_up = %.4e (rec %.2e), "
          "theta_kill = %.2e; OPT endpoint minC = %s == %d; "
          "conservation exact; top-9 atoms %s == the r291 record"
          % (th_up, THUP_REC, th_kill, str(MRi["minC"]),
             RIDGE_MINC_REC, str(top9)))

    # ---------------- S3 r292 Hessian rebuilt verbatim (Leg 0)
    section("S3  LEG 0b -- r292 HESSIAN REBUILT VERBATIM "
            "(29 sealed directions)")

    def margin_at(dvec):
        meas = PFP.measure_density(dvec, L9)
        if meas["rho"] is None or meas["cross"] is None \
                or meas["cross"] <= N_REF:
            return float("nan")
        return 1.0 - meas["rho"][N_REF]

    m00 = margin_at(d9)
    dd_R = dR - d9
    dirsD = []      # (name, raw dd)
    for wn in ("SMOOTH", "SCR", "EPST"):
        dirsD.append(("W_" + wn, d_worlds[wn] - d9))
    dirsD.append(("RIDGE", dd_R))
    ok_dcons = True
    for j in range(N_ATOM):
        mask = np.zeros(len(uu9))
        mask[order[j]] = 1.0
        u2, m2 = RA.subset_move(uu9, mm9, du_ridge, mask)
        ok_dcons = ok_dcons and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2, m2, 2.0 * th_up * AMP_PAD)
        ddj = np.asarray(PIK.build_rung(MAIN_KZ,
                                        comb=(u2, m2))["d"],
                         float) - d9
        dirsD.append(("ATOM%02d_n%d" % (j, int(nn_at[order[j]])),
                      ddj))
    for i in range(NDIR_FRAC):
        dd, (u2, m2) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                    THETA_CAL, SEED_FRAC + i)
        ok_dcons = ok_dcons and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2, m2, THETA_CAL)
        dirsD.append(("FRAC%02d" % i, dd))
    ll9 = np.arange(L9)
    s_l9 = 4.0 * np.sin(math.pi * ll9 / L9) ** 2 / (2.0 * L9)
    for i in range(NDIR_DENS):
        dd = PFP.dir_dens(d9, L9, SEED_DENS + i)
        eta0 = abs(float(np.sum(dd * s_l9)))
        ok_dcons = ok_dcons and eta0 <= ETA0_BAR \
            * max(float(np.sum(np.abs(dd * s_l9))), 1.0)
        dirsD.append(("DENS%02d" % i, dd))
    names_D = [n for n, _d in dirsD]
    vhat = {n: CF.unit_dir(dd, lag_l1(dd), REF) for n, dd in dirsD}
    check("G30-direction-set", ok_dcons and len(dirsD) == 29,
          "SEALED DIRECTION SET D (r292 verbatim): %d directions "
          "= 3 world axes + ridge + %d atoms (conservation exact) "
          "+ %d FRAC (seeds 292100+) + %d DENS (seeds 292200+, "
          "eta_0 exact); all theta_eq-normalized"
          % (len(dirsD), N_ATOM, NDIR_FRAC, NDIR_DENS))
    nD = len(dirsD)
    d2_tab = {}
    d1_mid = {}
    ok_finA = True
    for name in names_D:
        v = vhat[name]
        ests = []
        for h in HESS_EQ_HS:
            mp_ = margin_at(d9 + v * h)
            mn_ = margin_at(d9 - v * h)
            ok_finA = ok_finA and math.isfinite(mp_) \
                and math.isfinite(mn_)
            ests.append((mp_ - 2.0 * m00 + mn_) / (h * h))
            if h == H_PAIR_H:
                d1_mid[name] = (mp_ - mn_) / (2.0 * h)
        d2_tab[name] = ests
    diag_mid = {n: d2_tab[n][1] for n in names_D}
    check("G31-diagonal-census", ok_finA,
          "DIAGONAL d2 census (r292 a1 ladder %s, all finite): "
          "worlds %s; RIDGE %.2f; DENS [%.3g..%.3g]"
          % (str(HESS_EQ_HS),
             str({n: "%.1f" % d2_tab[n][0] for n in names_D[:3]}),
             d2_tab["RIDGE"][0],
             min(d2_tab[n][0] for n in names_D[23:]),
             max(d2_tab[n][0] for n in names_D[23:])))
    Hmat = np.zeros((nD, nD))
    for i in range(nD):
        Hmat[i, i] = diag_mid[names_D[i]]
    sel_pairs = [(0, 1), (0, 2), (1, 2),
                 (0, 3), (1, 3), (2, 3)]
    sel_pairs += [(3, 4 + j) for j in range(N_ATOM)]
    ok_finP = True
    pol_dev_max = 0.0
    n_pairs = 0
    d2sum_cache = {}
    for i in range(nD):
        for j in range(i + 1, nD):
            u, v = vhat[names_D[i]], vhat[names_D[j]]
            h = H_PAIR_H
            msp = margin_at(d9 + (u + v) * h)
            msn = margin_at(d9 - (u + v) * h)
            mdp = margin_at(d9 + (u - v) * h)
            mdn = margin_at(d9 - (u - v) * h)
            ok_finP = ok_finP and all(math.isfinite(x)
                                      for x in (msp, msn, mdp, mdn))
            d2su = (msp - 2.0 * m00 + msn) / (h * h)
            d2di = (mdp - 2.0 * m00 + mdn) / (h * h)
            Hij = CF.pol_of_d2(d2su, d2di)
            Hmat[i, j] = Hmat[j, i] = Hij
            d2sum_cache[(i, j)] = d2su
            n_pairs += 1
    for (i, j) in sel_pairs:
        Hij = Hmat[i, j]
        Hexp = CF.expand_of_d2(d2sum_cache[(i, j)],
                               diag_mid[names_D[i]],
                               diag_mid[names_D[j]])
        dev = abs(Hij - Hexp) / max(abs(Hij), D2_FLOOR)
        pol_dev_max = max(pol_dev_max, dev)
    ok_pol = ok_finP and pol_dev_max <= POL_TOL
    check("G32-polarization-matrix", ok_pol,
          "FULL POLARIZATION MATRIX (r292 verbatim): %d pairs at "
          "h = %.3g (all finite); %d selected pairs pass the "
          "expansion crosscheck (worst rel dev %.3f <= %.2f)"
          % (n_pairs, H_PAIR_H, len(sel_pairs), pol_dev_max,
             POL_TOL))
    Vmat = np.stack([vhat[n] for n in names_D], axis=1)
    Gmat = Vmat.T @ Vmat
    wG, UG = np.linalg.eigh(Gmat)
    keep = wG >= GCUT * wG[-1]
    Uk = UG[:, keep]
    Wk = Uk / np.sqrt(wG[keep])[None, :]
    Ared = Wk.T @ Hmat @ Wk
    lam, Y = np.linalg.eigh(Ared)
    o_l = np.argsort(-np.abs(lam))
    lam_s = lam[o_l]
    Evec = Vmat @ (Wk @ Y[:, o_l])
    tr_abs = float(np.sum(np.abs(lam_s)))
    share1 = abs(lam_s[0]) / max(tr_abs, 1e-300)
    e_top = Evec[:, 0]
    vSMn = vhat["W_SMOOTH"]
    cos_sm = abs(float(vSMn @ e_top)
                 / max(float(np.linalg.norm(vSMn))
                       * float(np.linalg.norm(e_top)), 1e-300))
    l2n2 = {n: float(vhat[n] @ vhat[n]) for n in names_D}
    diag_l2 = {n: diag_mid[n] / max(l2n2[n], 1e-300)
               for n in names_D}
    Hrr = diag_l2["RIDGE"]
    diag_sorted = sorted((abs(diag_l2[n]) for n in names_D),
                         reverse=True)
    rank_rr = 1 + sum(1 for v in diag_sorted if v > abs(Hrr))
    ok_r292h = (abs(share1 - R292_SHARE_REC) <= R292_SHARE_TOL
                and abs(lam_s[0] / R292_LAMTOP_REC - 1.0)
                <= R292_LAMTOP_TOL
                and abs(cos_sm - R292_COS_SM_REC)
                <= R292_COS_SM_TOL
                and rank_rr == R292_RIDGE_RANK_REC)
    check("G33-r292-eigen-anchor", ok_r292h,
          "r292 CORE REGRESSION: top-eigenvalue trace share %.3f "
          "== 0.925 (tol %.2f), lam_top %.3f == -0.418 (rel "
          "%.2f), SMOOTH |cos| %.2f == 0.07 (tol %.2f), ridge "
          "L2-diagonal rank %d/29 == 28 -- the r292 spectroscopy "
          "reproduces bit-near"
          % (share1, R292_SHARE_TOL, lam_s[0], R292_LAMTOP_TOL,
             cos_sm, R292_COS_SM_TOL, rank_rr))

    # ---------------- S4 H_tr seal + r293 contest anchor
    section("S4  LEG 0c -- H_tr HASH GATE + r293 CONTEST + "
            "FAMILY CENSUS")
    train_names = tuple("FRAC%02d" % i for i in TRAIN_FRAC) \
        + tuple("DENS%02d" % i for i in TRAIN_DENS)
    train_dirs = list(train_names) + ["RIDGE"] \
        + [n for n in names_D if n.startswith("ATOM")]
    tr_idx = [names_D.index(n) for n in train_dirs]
    V_tr = Vmat[:, tr_idx]
    H_tr = Hmat[np.ix_(tr_idx, tr_idx)]
    g_tr = np.array([d1_mid[n] for n in train_dirs])
    G_tr = V_tr.T @ V_tr
    wGt, UGt = np.linalg.eigh(G_tr)
    H_SEAL = hashlib.sha256(H_tr.tobytes()).hexdigest()
    check("G40-htr-hash-gate", H_SEAL.startswith(HTR_SHA_PREFIX),
          "H_tr on the 18 sealed r292 training directions "
          "REBUILT: sha256(H_tr) = %s == the PUBLISHED r294 seal "
          "prefix %s -- the object is BIT-IDENTICAL to the r293/"
          "r294 functional, re-training structurally excluded"
          % (H_SEAL[:16], HTR_SHA_PREFIX))

    def proj_x(delta):
        return CF.proj_coords(V_tr, wGt, UGt, GCUT, delta)

    # the r292/r293 corpus rebuilt bit-identically
    CORPUS = []

    def add_pt(tag, dvec, meas, theq, src=""):
        CORPUS.append(dict(tag=tag, src=src,
                           delta=np.asarray(dvec, float) - d9,
                           s=meas["s"], theq=theq))

    add_pt("MAIN", d9, M0, 0.0)
    for wn in ("SMOOTH", "SCR", "EPST", "HL2", "ENSR"):
        add_pt("WORLD:" + wn, d_worlds[wn], worlds_meas[wn],
               lag_l1(d_worlds[wn] - d9) / REF)
    for wn in ("SMOOTH", "SCR", "EPST", "ENSR"):
        dT = d_worlds[wn]
        plen = lag_l1(dT - d9) / REF
        for t in PATH_TS:
            dpt = PFP.interp_density(d9, dT, t)
            add_pt("PATH:%s:t=%.4g" % (wn, t), dpt,
                   PFP.measure_density(dpt, L9), t * plen)
    for name, dd in dirsD[13:]:     # the 16 fresh random dirs
        unit = dd / max(lag_l1(dd), 1e-300)
        for dist in DIST_GRID:
            dpt = d9 + unit * (dist * REF)
            add_pt("DIR:%s:d=%.0e" % (name, dist), dpt,
                   PFP.measure_density(dpt, L9), dist, src=name)
    for fac in PFP.RIDGE_FACS:
        dpt = d9 + fac * dd_R
        add_pt("RIDGE:f=%g" % fac, dpt,
               PFP.measure_density(dpt, L9),
               fac * lag_l1(dd_R) / REF, src="RIDGE")
    ok_scr = True
    for i in range(ENS_SCR_REPS):
        sctx = MS.ctx_build(MAIN_KZ,
                            scramble_seed=SEED_R285_SCR + i)
        ok_scr = ok_scr and bool(np.array_equal(
            np.asarray(sctx["mm"]), mm9))
        dS = np.asarray(sctx["darm"], float)
        add_pt("ENS_SCR:%02d" % i, dS,
               PFP.measure_density(dS, L9), lag_l1(dS - d9) / REF)
    excl_src = set(train_names) | {"RIDGE"}
    test_pts = [r for r in CORPUS if r["src"] not in excl_src]
    side_pts = [r for r in CORPUS if r["src"] in excl_src]
    train_tags = set(r["tag"] for r in side_pts)
    overlap = RA.split_auditor(train_tags,
                               set(r["tag"] for r in test_pts))
    tag_sha = hashlib.sha256("|".join(
        sorted(r["tag"] for r in test_pts)).encode()).hexdigest()
    check("G41-r293-split-seal",
          ok_scr and len(CORPUS) >= 140
          and len(test_pts) == R292_TEST_N_REC and not overlap
          and tag_sha.startswith(TAG_SHA_PREFIX),
          "r292/r293 CORPUS REBUILT: %d points, test split %d == "
          "%d, DISJOINT (overlap %s), tag-list SHA %s == prefix "
          "%s -- the r293 split reproduces bit-identically"
          % (len(CORPUS), len(test_pts), R292_TEST_N_REC,
             str(overlap) if overlap else "NONE", tag_sha[:16],
             TAG_SHA_PREFIX))
    for r in CORPUS:
        x = proj_x(r["delta"])
        r["x"] = x
        r["F0_M1"] = r["theq"]
        r["F0_M2"] = float(np.linalg.norm(r["delta"]))
        r["F10"] = CF.func_q10(x, H_tr)
    svec = [r["s"] for r in test_pts]
    dead_lb = [r["s"] < NEAR for r in test_pts]
    svec_side = [r["s"] for r in side_pts]
    sp_f10 = BH.spearman([r["F10"] for r in test_pts], svec)
    sp_f0m1 = BH.spearman([r["F0_M1"] for r in test_pts], svec)
    sp_f0m2 = BH.spearman([r["F0_M2"] for r in test_pts], svec)
    auc_f10 = CF.auc_rank([r["F10"] for r in test_pts], dead_lb)
    psp_test = MR.partial_sp([r["F10"] for r in test_pts], svec,
                             [r["F0_M2"] for r in test_pts])
    psp_side = MR.partial_sp([r["F10"] for r in side_pts],
                             svec_side,
                             [r["F0_M2"] for r in side_pts])
    ok_r293 = (abs(sp_f10 - R293_F10_SP_REC) <= R293_SP_TOL
               and abs(sp_f0m1 - R293_F0M1_SP_REC) <= R293_SP_TOL
               and abs(sp_f0m2 - R293_F0M2_SP_REC) <= R293_SP_TOL
               and abs(auc_f10 - R293_AUC_REC) <= R293_SP_TOL
               and abs(psp_test - R293_PARTIAL_REC) <= R293_SP_TOL
               and abs(psp_side - R293_PARTIAL_SIDE_REC)
               <= R293_SP_TOL)
    check("G42-r293-contest-anchor", ok_r293,
          "r293 CONTEST REGRESSION (bit-identical split): F10 sp "
          "%+.3f == +0.884, F0_M1 %+.3f == -0.907, F0_M2 %+.3f == "
          "-0.860, AUC %.3f == 0.097, partial %+.3f == +0.423 "
          "test / %+.3f == +0.826 train-side (tol %.3f each)"
          % (sp_f10, sp_f0m1, sp_f0m2, auc_f10, psp_test,
             psp_side, R293_SP_TOL))

    def fam_of_tag(tag):
        if tag == "MAIN":
            return "MAIN"
        if tag.startswith("WORLD:"):
            return "WORLD"
        if tag.startswith("PATH:"):
            return "PATH"
        if tag.startswith("DIR:FRAC"):
            return "FRAC"
        if tag.startswith("DIR:DENS"):
            return "DENS"
        if tag.startswith("ENS_SCR:"):
            return "ENS"
        return "OTHER"

    cen = {f: sum(1 for r in test_pts if fam_of_tag(r["tag"]) == f)
           for f in ("MAIN", "WORLD", "PATH", "FRAC", "DENS",
                     "ENS")}
    cen_tup = (cen["MAIN"], cen["WORLD"], cen["PATH"],
               cen["FRAC"], cen["DENS"], cen["ENS"])
    check("G43-r293-family-census", cen_tup == R293_FAM_CENSUS,
          "r293 TEST-SPLIT FAMILY CENSUS: MAIN/WORLD/PATH/FRAC/"
          "DENS/ENS_SCR = %s == sealed %s -- the r293 mix is "
          "PATH-heavy (%.2f vs %.2f in the fresh protocol): the "
          "Leg-B composition object"
          % (str(cen_tup), str(R293_FAM_CENSUS),
             cen["PATH"] / float(len(test_pts)), 40.0 / 147.0))

    # ---------------- S5 r294 core regression
    section("S5  LEG 0d -- r294 CORE REGRESSION (5 corpora + "
            "jackknife + rank)")

    def build_fresh_corpus(base, kpref):
        """the sealed r294 147-point fresh-corpus protocol at a
        seed base (disclosed measurement-consuming builder --
        every point's survival is a measurement)."""
        pts = []

        def addf(tag, fam, seed, dvec, meas):
            pts.append(dict(tag=tag, fam=fam, seed=seed,
                            delta=np.asarray(dvec, float) - d9,
                            s=meas["s"]))

        okb = True
        addf("MAIN", "MAIN", -1, d9, M0)
        w_specs = [("SCR", base + 1), ("SCR", base + 2),
                   ("HL2", base + 3), ("HL2", base + 4),
                   ("ENSR", base + 5), ("ENSR", base + 6)]
        w_dens = []
        for wn, sd in w_specs:
            if wn == "HL2":
                comb_k, _t = PC.gen_model(gpc, "HL2", sd)
                dW = np.asarray(MS.ctx_build(
                    MAIN_KZ, comb=comb_k)["darm"], float)
            else:
                sctx = MS.ctx_build(MAIN_KZ, scramble_seed=sd)
                okb = okb and bool(np.array_equal(
                    np.asarray(sctx["mm"]), mm9))
                dW = np.asarray(sctx["darm"], float)
            w_dens.append(dW)
            addf("%s:WORLD:%s:%d" % (kpref, wn, sd), "WORLD", sd,
                 dW, PFP.measure_density(dW, L9))
        for pi in (0, 2, 4, 1):    # SCR_a / HL2_a / ENSR_a / SCR_b
            dT = w_dens[pi]
            for t in PATH_TS:
                dpt = PFP.interp_density(d9, dT, t)
                addf("%s:PATH:%s:%d:t=%.4g"
                     % (kpref, w_specs[pi][0], w_specs[pi][1], t),
                     "PATH", w_specs[pi][1], dpt,
                     PFP.measure_density(dpt, L9))
        for i in range(N_FRAC_C):
            sd = base + 100 + i
            dd, (u2, m2) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                        THETA_CAL, sd)
            okb = okb and MF.conserve_comb(
                "P2_JIT", uu9, mm9, u2, m2, THETA_CAL)
            unit = dd / max(lag_l1(dd), 1e-300)
            for dist in DIST_GRID:
                dpt = d9 + unit * (dist * REF)
                addf("%s:DIR:FRAC:%d:d=%.0e" % (kpref, sd, dist),
                     "FRAC", sd, dpt,
                     PFP.measure_density(dpt, L9))
        for i in range(N_DENS_C):
            sd = base + 200 + i
            dd = PFP.dir_dens(d9, L9, sd)
            eta0 = abs(float(np.sum(dd * s_l9)))
            okb = okb and eta0 <= ETA0_BAR \
                * max(float(np.sum(np.abs(dd * s_l9))), 1.0)
            unit = dd / max(lag_l1(dd), 1e-300)
            for dist in DIST_GRID:
                dpt = d9 + unit * (dist * REF)
                addf("%s:DIR:DENS:%d:d=%.0e" % (kpref, sd, dist),
                     "DENS", sd, dpt,
                     PFP.measure_density(dpt, L9))
        for r in pts:
            r["F10"] = CF.func_q10(proj_x(r["delta"]), H_tr)
            r["F0_M2"] = float(np.linalg.norm(r["delta"]))
        return pts, okb

    def corpus_stats(pts):
        sv = [r["s"] for r in pts]
        dl = [r["s"] < NEAR for r in pts]
        spF = BH.spearman([r["F10"] for r in pts], sv)
        spB = BH.spearman([r["F0_M2"] for r in pts], sv)
        auc = CF.auc_rank([r["F10"] for r in pts], dl)
        psp = MR.partial_sp([r["F10"] for r in pts], sv,
                            [r["F0_M2"] for r in pts])
        return dict(n=len(pts), spF=spF, spB=spB, auc=auc,
                    psp=psp, marg=abs(spF) - abs(spB),
                    s_lo=min(sv), s_hi=max(sv))

    ok_r294c = H_SEAL.startswith(HTR_SHA_PREFIX)
    r294_rows = []
    for k in range(R294_N_CORP):
        pts, okb = build_fresh_corpus(R294_BASE + BASE_STEP * k,
                                      "C%d" % k)
        ok_r294c = ok_r294c and okb
        r294_rows.append(corpus_stats(pts))
    p_med294 = float(np.median([r["psp"] for r in r294_rows]))
    ok_r294n = all(
        abs(r294_rows[k]["spF"] - R294_SPF_REC[k]) <= R294_TOL
        and abs(r294_rows[k]["spB"] - R294_SPB_REC[k]) <= R294_TOL
        and abs(r294_rows[k]["auc"] - R294_AUC_REC[k]) <= R294_TOL
        and r294_rows[k]["marg"] > 0.0
        for k in range(R294_N_CORP)) \
        and abs(p_med294 - R294_PART_MED_REC) <= R294_TOL
    check("G45-r294-corpus-regression", ok_r294c and ok_r294n,
          "r294 FIVE-CORPUS TABLE REBUILT BITNEAR (bases 294000+"
          "1000k): sp(F10) %s vs sp(F0_M2) %s == records (tol "
          "%.3f), win 5/5, partial median %.3f == 0.299"
          % (str([round(r["spF"], 3) for r in r294_rows]),
             str([round(r["spB"], 3) for r in r294_rows]),
             R294_TOL, p_med294))
    # r294 jackknife rebuilt (no new measurements)
    JACK_OUT = [(j, j + 5, j + 10) for j in range(5)]
    sp_jack = []
    for rot in JACK_OUT:
        keep_i = [i for i in range(len(train_dirs))
                  if i not in rot]
        V_j = V_tr[:, keep_i]
        H_j = H_tr[np.ix_(keep_i, keep_i)]
        G_j = V_j.T @ V_j
        wGj, UGj = np.linalg.eigh(G_j)
        vals = [CF.func_q10(
            CF.proj_coords(V_j, wGj, UGj, GCUT, r["delta"]), H_j)
            for r in test_pts]
        sp_jack.append(BH.spearman(vals, svec))
    sig_jack = float(np.std(sp_jack))
    ok_jack = all(abs(sp_jack[j] - R294_JACK_REC[j]) <= R294_TOL
                  for j in range(5)) \
        and abs(sig_jack - R294_JACK_SIG_REC) <= R294_JACK_SIG_TOL
    check("G46-r294-jackknife-regression", ok_jack,
          "r294 JACKKNIFE REBUILT (leave-3-out rotations, no new "
          "measurements): sp %s == records, sigma %.4f == 0.0101 "
          "(tol %.3f)" % (str([round(v, 3) for v in sp_jack]),
                          sig_jack, R294_JACK_SIG_TOL))
    # r294 rank truncation rebuilt
    keep_t = wGt >= GCUT * wGt[-1]
    Uk_t = UGt[:, keep_t]
    Wk_t = Uk_t / np.sqrt(wGt[keep_t])[None, :]
    Ared_t = Wk_t.T @ H_tr @ Wk_t
    lam_t2, Y_t2 = np.linalg.eigh(Ared_t)
    o_t2 = np.argsort(-np.abs(lam_t2))
    lam_tr_s = lam_t2[o_t2]
    Y_tr_s = Y_t2[:, o_t2]

    def whiten_y(x):
        z = np.sqrt(wGt[keep_t]) * (Uk_t.T @ np.asarray(x, float))
        return Y_tr_s.T @ z

    sp_rank = {}
    for rr_ in (1, 2, 4):
        vals = [0.5 * float(np.sum(
            lam_tr_s[:rr_] * whiten_y(r["x"])[:rr_] ** 2))
            for r in test_pts]
        sp_rank[rr_] = BH.spearman(vals, svec)
    coef_top = (Wk_t @ Y_tr_s)[:, 0]
    dens_idx = [i for i, n in enumerate(train_dirs)
                if n.startswith("DENS")]
    c_top = np.asarray(coef_top, float)
    dens_share = float(np.sum(c_top[dens_idx] ** 2)) \
        / max(float(np.sum(c_top * c_top)), 1e-300)
    ok_rank = (abs(sp_rank[1] - R294_RANK_REC[0]) <= R294_TOL
               and abs(sp_rank[2] - R294_RANK_REC[1]) <= R294_TOL
               and abs(sp_rank[4] - R294_RANK_REC[2]) <= R294_TOL
               and abs(dens_share - R294_DENS_SHARE_REC)
               <= R294_TOL)
    check("G47-r294-rank-regression", ok_rank,
          "r294 RANK TRUNCATION REBUILT: sp r=1 %+.3f / r=2 "
          "%+.3f / r=4 %+.3f == records (+0.855/+0.863/+0.884); "
          "top-axis DENS coefficient-mass share %.3f == 0.989"
          % (sp_rank[1], sp_rank[2], sp_rank[4], dens_share))

    # ---------------- S6 LEG A: the 20-corpus ensemble
    section("S6  LEG A -- TWENTY FRESH CORPORA vs THE UNCHANGED "
            "H_tr (the hardening bar)")
    ok_seed = True
    bases20 = [FRESH_BASE20 + BASE_STEP * k
               for k in range(N_CORP20)]
    for b_ in bases20:
        ok_seed = ok_seed and not (seeds_of_base(b_)
                                   & FORBIDDEN_SEEDS)
    for a in range(N_CORP20):
        for b in range(a + 1, N_CORP20):
            ok_seed = ok_seed and not (seeds_of_base(bases20[a])
                                       & seeds_of_base(bases20[b]))
    check("G50-seed-disjointness", ok_seed,
          "SEED AUDIT (a GATE, not a sentence): all %d fresh "
          "bases (%d..%d) have zero overlap with the %d "
          "enumerated forbidden r292/r293/r294 seeds and zero "
          "pairwise overlap"
          % (N_CORP20, bases20[0], bases20[-1],
             len(FORBIDDEN_SEEDS)))
    ok_build20 = H_SEAL.startswith(HTR_SHA_PREFIX)
    rows20 = []
    corpora20 = []
    all_tag_sets = []
    for k in range(N_CORP20):
        pts, okb = build_fresh_corpus(bases20[k], "K%02d" % k)
        ok_build20 = ok_build20 and okb \
            and len(pts) >= CORP_MIN_PTS
        corpora20.append(pts)
        st = corpus_stats(pts)
        st["k"] = k
        st["win"] = st["marg"] > 0.0
        rows20.append(st)
        all_tag_sets.append(set(r["tag"] for r in pts))
    check("G51-fresh-corpora-20", ok_build20,
          "TWENTY FRESH CORPORA (r294 protocol verbatim, seeds "
          "300000+1000k; conservation / eta_0 / scramble weights "
          "exact; H_tr hash re-gated == the published seal): "
          "sizes all %d (bar >= %d); s ranges [%.2f..%.2f] "
          "global -- worlds dead, ladders alive on every corpus"
          % (rows20[0]["n"], CORP_MIN_PTS,
             min(r["s_lo"] for r in rows20),
             max(r["s_hi"] for r in rows20)))
    ov_pair = 0
    for a in range(N_CORP20):
        for b in range(a + 1, N_CORP20):
            ov_pair += len(RA.split_auditor(
                all_tag_sets[a] - {"MAIN"},
                all_tag_sets[b] - {"MAIN"}))
    check("G52-corpus-disjointness", ov_pair == 0,
          "CORPUS DISJOINTNESS: pairwise tag overlaps %d == 0 "
          "(MAIN excluded as the disclosed shared anchor)"
          % ov_pair)
    tab20 = "; ".join(
        "K%02d(%+.3f/%+.3f, m %+.3f, p %s)"
        % (r["k"], r["spF"], r["spB"], r["marg"],
           ("%+.3f" % r["psp"]) if math.isfinite(r["psp"])
           else "DEGEN")
        for r in rows20)
    check("G53-corpus20-table",
          all(math.isfinite(r["spF"]) and math.isfinite(r["spB"])
              for r in rows20),
          "CORPUS20 TABLE (sp(F10)/sp(F0_M2), margin, partial): "
          "%s" % tab20)
    margins20 = [r["marg"] for r in rows20]
    n_win20 = sum(1 for r in rows20 if r["win"])
    m_med, m_q1, m_q3 = med_iqr(margins20)
    m_min = min(margins20)
    grade = grade_of(margins20)
    if grade == "HARDENED":
        hard_verd = ("F10_SP_HARDENED(win %d/20 >= %d, margin "
                     "median %+.4f >= +%.2f, min %+.4f >= -%.2f: "
                     "all three sealed clauses hold -- the "
                     "partial-free ranking statement is a "
                     "PROMOTABLE weaker claim for wave 8)"
                     % (n_win20, HARD_WIN_NEED, m_med,
                        MARGIN_MED_BAR, m_min, MARGIN_LOSS_MAX))
    elif grade == "MAJORITY":
        fails = []
        if n_win20 < HARD_WIN_NEED:
            fails.append("win %d < %d" % (n_win20, HARD_WIN_NEED))
        if m_med < MARGIN_MED_BAR:
            fails.append("median %+.4f < +%.2f"
                         % (m_med, MARGIN_MED_BAR))
        if m_min < -MARGIN_LOSS_MAX:
            fails.append("min %+.4f < -%.2f"
                         % (m_min, MARGIN_LOSS_MAX))
        hard_verd = ("F10_SP_MAJORITY(win %d/20; failed clauses: "
                     "%s -- a documented regularity, NOT a "
                     "theorem candidate)"
                     % (n_win20, "; ".join(fails)))
    else:
        hard_verd = ("F10_SP_DEAD(win %d/20 < %d: the weak "
                     "partial-free form is dead too -- the r293 "
                     "promotion-candidate marking is to be "
                     "retracted in the round report)"
                     % (n_win20, MAJ_WIN_NEED))
    check("G54-hardening-adjudication", True,
          "SEALED THREE-CLAUSE BAR (fixed before any corpus was "
          "built, untouchable): win >= %d/20 AND margin median "
          ">= +%.2f AND min margin >= -%.2f -> %s"
          % (HARD_WIN_NEED, MARGIN_MED_BAR, MARGIN_LOSS_MAX,
             hard_verd.split("(")[0]))
    psp20 = [r["psp"] for r in rows20 if math.isfinite(r["psp"])]
    p_med, p_q1, p_q3 = med_iqr(psp20)
    part_verd = ("PARTIAL20(median %+.3f, IQR [%+.3f, %+.3f], "
                 "range [%+.3f, %+.3f], n_finite %d/20)"
                 % (p_med, p_q1, p_q3, min(psp20), max(psp20),
                    len(psp20)))
    check("G55-partial20-report", len(psp20) == N_CORP20,
          "PARTIAL DISTRIBUTION over the 20 (NOT bar-relevant, "
          "the honest r294 continuation): %s -- r293 +0.423 vs "
          "this distribution; r294 median 0.299" % part_verd)

    # ---------------- S7 LEG B: partial anatomy by family
    section("S7  LEG B -- PARTIAL ANATOMY BY FAMILY + r293 "
            "COMPOSITION")
    pool = [r for r in corpora20[0] if r["fam"] == "MAIN"]
    for pts in corpora20:
        pool += [r for r in pts if r["fam"] != "MAIN"]
    check("G60-pool-census", len(pool) >= POOL_MIN,
          "POOLED ENSEMBLE (MAIN pooled once, disclosed): %d "
          "points >= %d; family cells %s"
          % (len(pool), POOL_MIN,
             str({f: sum(1 for r in pool if r["fam"] == f)
                  for f in ("MAIN", "WORLD", "PATH", "FRAC",
                            "DENS")})))

    def pool_partial(sel):
        if len(sel) < 4:
            return float("nan"), len(sel)
        return MR.partial_sp([r["F10"] for r in sel],
                             [r["s"] for r in sel],
                             [r["F0_M2"] for r in sel]), len(sel)

    fam_map = {}
    for f in ("PATH", "WORLD", "FRAC", "DENS"):
        val, nf = pool_partial([r for r in pool
                                if r["fam"] == f])
        if not math.isfinite(val):
            typ = "DEGEN"
        elif val >= FAM_STRONG:
            typ = "STRONG"
        elif abs(val) < FAM_NULL:
            typ = "NULL"
        else:
            typ = "weak"
        fam_map[f] = (val, nf, typ)
    fam_txt = "; ".join(
        "%s %s (n %d) %s"
        % (f, ("%+.3f" % fam_map[f][0])
           if math.isfinite(fam_map[f][0]) else "DEGEN",
           fam_map[f][1], fam_map[f][2])
        for f in ("PATH", "WORLD", "FRAC", "DENS"))
    check("G61-family-map",
          all(fam_map[f][1] > 0 for f in fam_map),
          "PARTIAL_FAMILY_MAP (pooled partial sp(F10, s | F0_M2) "
          "per family; STRONG >= +%.1f, NULL < %.1f): %s -- "
          "ATOM/RIDGE structurally absent by the unchanged split "
          "seal (their only honest partial is the r293 train-"
          "side +0.826, re-gated in G42)"
          % (FAM_STRONG, FAM_NULL, fam_txt))
    reg_map = {}
    for f in ("PATH", "WORLD", "FRAC", "DENS"):
        for rg, cond in (("ALIVE", lambda s: s >= NEAR),
                         ("BEYOND", lambda s: s < NEAR)):
            val, nf = pool_partial(
                [r for r in pool
                 if r["fam"] == f and cond(r["s"])])
            reg_map[(f, rg)] = (val, nf)
    reg_txt = "; ".join(
        "%s/%s %s (n %d)"
        % (f, rg, ("%+.3f" % reg_map[(f, rg)][0])
           if math.isfinite(reg_map[(f, rg)][0]) else "DEGEN",
           reg_map[(f, rg)][1])
        for f in ("PATH", "WORLD", "FRAC", "DENS")
        for rg in ("ALIVE", "BEYOND"))
    check("G62-regime-split", True,
          "DOSE-REGIME SPLIT (ALIVE s >= %.2f vs BEYOND s < "
          "%.2f, operationalized on the survival readout, "
          "disclosed; thin or one-sided cells print DEGEN): %s"
          % (NEAR, NEAR, reg_txt))
    # r293 composition-matched subsample per corpus
    psp_match = []
    for k in range(N_CORP20):
        base = bases20[k]
        sel = [r for r in corpora20[k]
               if r["fam"] in ("MAIN", "WORLD", "PATH")
               or (r["fam"] == "FRAC"
                   and r["seed"] < base + 100 + MATCH_FRAC)
               or (r["fam"] == "DENS"
                   and r["seed"] < base + 200 + MATCH_DENS)]
        val, nf = pool_partial(sel)
        psp_match.append(val)
    n_match = 1 + 6 + 4 * len(PATH_TS) \
        + (MATCH_FRAC + MATCH_DENS) * len(DIST_GRID)
    mm_med = float(np.median([v for v in psp_match
                              if math.isfinite(v)]))
    gain = mm_med - p_med
    if gain >= R293_EXPL_GAIN and mm_med >= R293_EXPL_LEVEL:
        comp_verd = ("R293_COMPOSITION_EXPLAINED(matched median "
                     "%+.3f >= %.2f, full median %+.3f, gain "
                     "%+.3f >= +%.2f: re-weighting any fresh "
                     "corpus to the r293 PATH-heavy mix "
                     "reproduces the r293-magnitude partial -- "
                     "the r293 +0.423 was COMPOSITION, not luck)"
                     % (mm_med, R293_EXPL_LEVEL, p_med, gain,
                        R293_EXPL_GAIN))
    else:
        comp_verd = ("R293_LUCK(matched median %+.3f, full "
                     "median %+.3f, gain %+.3f -- the sealed "
                     "thresholds (gain >= +%.2f AND level >= "
                     "%.2f) are not met: composition does NOT "
                     "explain the r293 magnitude)"
                     % (mm_med, p_med, gain, R293_EXPL_GAIN,
                        R293_EXPL_LEVEL))
    check("G63-r293-composition", all(math.isfinite(v)
                                      for v in psp_match),
          "SEALED COMPOSITION-MATCHED SUBSAMPLE (%d points per "
          "corpus: MAIN + 6 worlds + 40 paths + first %d FRAC + "
          "first %d DENS seeds; family shares PATH %.2f / FRAC "
          "%.2f / DENS %.2f ~ the r293 mix): matched partials "
          "median %+.3f (IQR [%+.3f, %+.3f]) vs full-mix median "
          "%+.3f -> %s"
          % (n_match, MATCH_FRAC, MATCH_DENS,
             4 * len(PATH_TS) / float(n_match),
             MATCH_FRAC * len(DIST_GRID) / float(n_match),
             MATCH_DENS * len(DIST_GRID) / float(n_match),
             mm_med, med_iqr(psp_match)[1], med_iqr(psp_match)[2],
             p_med, comp_verd.split("(")[0]))
    check("G64-partial-std-definition", True,
          "PRACTICAL CONSEQUENCE (a DEFINITION, not a "
          "measurement): the sealed composition-standardized "
          "partial statistic of future rounds is PARTIAL_STD = "
          "the partial on the FULL sealed 147-point fresh "
          "protocol (fixed family mix 1/6/40/60/40), reported "
          "as median + IQR over the ensemble = the G55 numbers "
          "(%+.3f, [%+.3f, %+.3f]); composition-dependent "
          "partials (like the r293 split value) are NOT "
          "comparable across mixes" % (p_med, p_q1, p_q3))

    # ---------------- S8 LEG C: candidate statement
    section("S8  LEG C -- THE CANDIDATE STATEMENT (wave 8)")
    if grade == "HARDENED":
        stmt = (
            "CANDIDATE STATEMENT (for Wave 8, partial-free): let "
            "H_tr be the r292-split-sealed 18-direction curvature "
            "form at w9 (sha256(H_tr bytes) prefix %s), F10(d) = "
            "1/2 x(d)^T H_tr x(d) with x(d) the L2-Gram "
            "projection of the density deviation d onto the "
            "training span (eigencut %g), and F0_M2(d) = |d|_L2. "
            "Then on every fresh conservation-gated w9 corpus "
            "built by the sealed 147-point protocol (MAIN + 6 "
            "dead worlds + 4 paths x PATH_TS + 12 FRAC x "
            "DIST_GRID + 8 DENS x DIST_GRID, seeds disjoint "
            "from all training seeds), |spearman(F10, s)| > "
            "|spearman(F0_M2, s)| for the survival depth s = "
            "minC / %d, with ensemble margin median >= +%.2f "
            "and no corpus losing by more than %.2f.  EVIDENCE "
            "CENSUS: %d/%d fresh corpora (r294 5/5 + r295 "
            "%d/%d), margin median %+.4f, min %+.4f.  The "
            "partial-correlation channel is EXPLICITLY NOT part "
            "of this statement (r294 adjudicated it FRAGILE; "
            "r295 Leg B located it in the PATH family)."
            % (HTR_SHA_PREFIX, GCUT, N_REF, MARGIN_MED_BAR,
               MARGIN_LOSS_MAX, 5 + n_win20, 5 + N_CORP20,
               n_win20, N_CORP20, m_med, m_min))
        legc_verd = "CANDIDATE_STATEMENT(printed, wave-8 form)"
        info(stmt)
        check("G70-candidate-statement", True,
              "Leg-A bar HELD -> the machine-checkable wave-8 "
              "candidate statement is printed above (all "
              "constants explicit: H_tr hash prefix, projection "
              "eigencut, corpus protocol, three-clause bar, "
              "evidence census); NO promotion from here -- the "
              "v9xx embedding belongs to the consolidation wave")
    else:
        legc_verd = ("LEGC_VOID(the Leg-A bar did not hold -- "
                     "no candidate statement, no forced "
                     "positivity)")
        check("G70-candidate-statement", True,
              "Leg-A bar NOT met (%s) -> Leg C is VOID without "
              "replacement" % grade)

    # ---------------- S9 LEG D: why L2 -- conservation projection
    section("S9  LEG D -- WHY L2?  THE CONSERVATION PROJECTION")
    nhat = s_l9 / max(float(np.linalg.norm(s_l9)), 1e-300)
    eta_shares = []
    f10p_vals = []
    f0p_vals = []
    for r in test_pts:
        dl = r["delta"]
        nl2 = float(dl @ dl)
        comp = float(nhat @ dl)
        eta_shares.append((comp * comp) / max(nl2, 1e-300)
                          if nl2 > 0 else 0.0)
        pd = cons_proj(dl, nhat)
        f10p_vals.append(CF.func_q10(proj_x(pd), H_tr))
        f0p_vals.append(float(np.linalg.norm(pd)))
    sp_f10p = BH.spearman(f10p_vals, svec)
    sp_f0p = BH.spearman(f0p_vals, svec)
    sh_med = float(np.median(eta_shares))
    sh_max = float(np.max(eta_shares))
    shift_f10 = abs(abs(sp_f10p) - abs(sp_f10))
    shift_f0 = abs(abs(sp_f0p) - abs(sp_f0m2))
    same_winner = ((abs(sp_f10p) > abs(sp_f0p))
                   == (abs(sp_f10) > abs(sp_f0m2)))
    if same_winner and max(shift_f10, shift_f0) <= CONV_TOL:
        legd_verd = ("L2_VIA_CONSERVATION(same winner, |sp| "
                     "shifts F10 %.4f / F0 %.4f <= %.2f: the "
                     "contest is invariant under the eta_0 "
                     "projection -- L2 is a metric in which the "
                     "conservation constraint is orthogonal; "
                     "HONEST WEAKNESS: the projected-out eta_0 "
                     "share is median %.1e (max %.1e) -- the "
                     "invariance is near-tautological and the "
                     "'why L2' mechanism stays open in substance)"
                     % (shift_f10, shift_f0, CONV_TOL, sh_med,
                        sh_max))
    else:
        legd_verd = ("L2_STILL_OPEN(winner preserved %s, shifts "
                     "F10 %.4f / F0 %.4f vs tol %.2f, eta_0 "
                     "share median %.1e: the projected contest "
                     "does NOT converge -- the conservation "
                     "geometry is not the L2 mechanism)"
                     % (str(same_winner), shift_f10, shift_f0,
                        CONV_TOL, sh_med))
    check("G75-cons-projection", math.isfinite(sp_f10p)
          and math.isfinite(sp_f0p),
          "ETA_0 PROJECTION CONTEST (bit-identical 94-point "
          "split; P = I - s_hat s_hat^T on the exact grid "
          "functional): sp(F10 o P) %+.3f (full %+.3f), "
          "sp(|P delta|) %+.3f (full %+.3f); projected-out "
          "share median %.2e, max %.2e"
          % (sp_f10p, sp_f10, sp_f0p, sp_f0m2, sh_med, sh_max))
    check("G76-cons-adjudication", True,
          "SEALED CONVERGENCE RULE (VIA_CONSERVATION iff same "
          "winner AND both |sp| shifts <= %.2f): -> %s"
          % (CONV_TOL, legd_verd.split("(")[0]))

    # ---------------- S10 must-fails + scopes
    section("S10  MUST-FAILS + SCOPE AUDITS")
    dd_m1, (u2m, m2m) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                     THETA_CAL, FRESH_BASE20 + 100)
    v_m1 = CF.unit_dir(dd_m1, lag_l1(dd_m1), REF)
    h_m1 = H_PAIR_H
    mp1 = margin_at(d9 + v_m1 * h_m1)
    mn1 = margin_at(d9 - v_m1 * h_m1)
    H_mut = H_tr.copy()
    H_mut[0, 0] = (mp1 - 2.0 * m00 + mn1) / (h_m1 * h_m1)
    sha_mut = hashlib.sha256(H_mut.tobytes()).hexdigest()
    check("G85-mustfail-retrain",
          not sha_mut.startswith(HTR_SHA_PREFIX),
          "m1 RE-TRAINING (one H_tr entry re-measured on the "
          "fresh corpus-0 FRAC direction): sha256 %s != the "
          "published seal %s -- CAUGHT by the hash gate; every "
          "leg ran on the sealed object only"
          % (sha_mut[:12], HTR_SHA_PREFIX))
    ov_m2 = seeds_of_base(R294_BASE) & FORBIDDEN_SEEDS
    ov_honest = set()
    for b_ in bases20:
        ov_honest |= (seeds_of_base(b_) & FORBIDDEN_SEEDS)
    check("G86-mustfail-seed-reuse", len(ov_m2) == 26
          and len(ov_honest) == 0,
          "m2 SEED COLLISION (a corpus built on the r294 base "
          "294000): the forbidden-seed auditor flags %d overlaps "
          "-- CAUGHT; the honest 20 bases show %d overlaps"
          % (len(ov_m2), len(ov_honest)))
    g_exact = grade_of([0.05] * 17 + [0.02, 0.02, -0.02])
    mut_a = list(margins20)
    mut_a[0] = -0.05                       # min-margin clause
    mut_b = [-abs(v) - 0.001 for v in margins20[:7]] \
        + list(margins20[7:])              # win-count clause
    mut_c = [min(v, 0.001) for v in margins20]   # median clause
    ok_m3 = (g_exact == "HARDENED"
             and grade_of(mut_a) != "HARDENED"
             and grade_of(mut_b) != "HARDENED"
             and grade_of(mut_c) != "HARDENED")
    check("G87-mustfail-bar-sharpness", ok_m3,
          "m3 BAR SHARPNESS (both directions): the exact-bar "
          "synthetic (median +0.02, min -0.02, 20 wins) grades "
          "%s == HARDENED; mutating the RECORD margins across "
          "each clause boundary flips the grade (min-margin "
          "mutant -> %s, win-count mutant -> %s, median mutant "
          "-> %s) -- every sealed clause has teeth on the real "
          "ensemble"
          % (g_exact, grade_of(mut_a), grade_of(mut_b),
             grade_of(mut_c)))
    u_m3, m_m3 = RA.mutant_broken_conservation(uu9, mm9, du_ridge)
    ok_m4 = not MF.conserve_comb("P2_JIT", uu9, mm9, u_m3, m_m3,
                                 2.0 * th_up * AMP_PAD)
    check("G88-mustfail-conservation", ok_m4,
          "m4 BROKEN CONSERVATION (one weight scaled 1 + 1e-3): "
          "the exact r276 gate returns False -- CAUGHT")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G89-scope-audits", not hits and not ag_hits,
          "the %d sealed source-pure constructors consume "
          "vectors/densities + geometry + seeds ONLY (%s); "
          "H_tr / g_tr are OUTSIDE the source-pure list and "
          "honestly typed measurement-consuming (split-sealed, "
          "hash-gated); fragment audit: %s"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S11 honesty + verdict
    section("S11  HONESTY LEDGER + VERDICT")
    check("G90-honesty-ledger", True,
          "every correlation and Hessian entry is a MEASUREMENT "
          "on finite profile space; H_tr is the UNCHANGED r293 "
          "object (hash-gated against the PUBLISHED r294 seal, "
          "mutant-gated); the 20 fresh corpora share exactly ONE "
          "point (MAIN) with each other and with r293/r294 "
          "(disclosed); the hardening bar grades a RANKING "
          "statement, not a bound; the family map and the "
          "composition adjudication are statements about a "
          "correlation statistic; the matched subsample "
          "approximates the r293 mix without an ENS_SCR analog "
          "(disclosed); the eta_0 projection test is typed with "
          "its share weakness disclosed; the promotion decision "
          "belongs to the consolidation wave, NOT to this probe")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no equidistribution "
          "premise, no posthoc window, no promotion from here, "
          "no RH claim; what the round adds: the 20-corpus "
          "hardening adjudication with the sealed three-clause "
          "bar, the family-resolved partial anatomy with the "
          "r293 composition adjudication, the candidate-"
          "statement print (bar-conditional) and the eta_0 "
          "conservation-projection bycatch; r243..r294 stand")
    parts_v = []
    parts_v.append("CORPUS20_TABLE(%s)" % tab20)
    parts_v.append(hard_verd)
    parts_v.append(part_verd)
    parts_v.append("PARTIAL_FAMILY_MAP(%s; regimes %s)"
                   % (fam_txt, reg_txt))
    parts_v.append(comp_verd)
    parts_v.append(legc_verd)
    parts_v.append(legd_verd)
    verd = " + ".join(parts_v)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s -- MEASURED hardening adjudication of the "
          "partial-free F10 statement; NO promotion from here, "
          "NO L* claim, NO RH claim" % verd)
    return finish(smoke)


def finish(smoke):
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
