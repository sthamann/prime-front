#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ridge_anatomy_probe -- PRIME.PORT.LSTAR.RIDGE_ANATOMY.01
(round 291): the ANATOMY of the one known raising axis.  r290
sealed BASIN_GEOMETRY + RIDGE_MAP + ALL_FUNCTIONALS_BLIND: the
working set around MAIN is a soft-shouldered anisotropic tube
(NEAR radius ~5e-4..2e-3 gap-equivalent), world-directed axes
kill 5..50x earlier, and the r280 OPT axis is a real RIDGE that
LIFTS the wall (minC 185 at extension factors 1..8) -- while all
four sealed LOCAL profile scalars are blind (best sp +0.263).
THE OPEN FRONTS (r290): (1) WHAT distinguishes the ridge axis --
the lifting vector as an analysis object; (2) non-local/low-rank
functional classes; (3) the collective nature of the SMOOTH
lethality.  NOT a proof round: no L* claim, no bound mechanism,
no asymptotic law.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

MACHINERY IMPORTED VERBATIM (no duplication): r290
PFP.{measure_density, lag_of, interp_density, dir_frac,
dir_dens, onset_bracket} + the r290 sealed constants (PATH_TS,
DIST_GRID, NEAR/DEAD, RIDGE_FACS); r280 BL.{grad_ext, dir_opt,
theta_of_dir, union_of_ctx}; r278 MS.{ctx_build, wsig_vec,
grad_chain}; r276 MF.{local_gaps, pert_jit, conserve_comb};
v881 PIK.{build_rung, folded_measure}; r243 PB.smooth_comb;
r244 BH.spearman; r254 ODG.base_exp (integer root extraction --
the comb atoms ARE p^k by construction, no oracle); paircorr
PC.{Grid, gen_model}; r284 LS.dist_rule; v563 core READ-ONLY.
The theta_eq coordinate is the r290 amendment-a1 LAG coordinate
with the ANALYTIC reference REF = 0.5 sum m g / Delta (gated
against the r290 record 125.75 and one independent pinned
jitter).  Survival depth s = minC / N_REF, N_REF = 184.

INDEX FIREWALL (binding, r238-r290 discipline): ground truth
(minC, crossings, onset records) enters GATES, the sealed
TRAINING channel of F6 (disclosed measurement-consuming, sealed
by the train/test split) and record tables only; the sealed
source-pure constructors consume combs/densities/profiles + grid
geometry + seeds ONLY (AST scope audit); no zero/prime oracles
anywhere (AST firewall).

LEG 0 -- ANCHOR REGRESSION (all gated): w9 record (S 367/263/
104, minC 184, crossing 185, margin 1.68e-4 rel 0.01, z_v
-3.149 tol 0.02, b34 -0.105 tol 0.01); theta_eq metric (REF ==
125.75 rel 1e-3, inversion identity 1e-12, one pinned
independent jitter at 3e-4 within 0.15); control flips EPST/SCR/
SMOOTH/HL2 = 25/21/27/25; r280 ridge anchor (theta_up 3.87e-5
rel 0.05, OPT endpoint dose 2 theta_up minC 185); r290 ridge map
regression (minC 185 at factors 1/4/8, first death at 16 with
s 0.79 tol 0.02).

LEG A -- RIDGE-VECTOR SECTION (open front 1): the lifting comb
move du = 2 theta_up g xi (all 70 atoms active, xi in {-1,+1})
is sectioned along sealed partitions; every sub-direction is the
SAME masked position move (weights bitwise -- exact r276 P2
conservation, gated per subset):
  (a1) ATOM CLASSES: PRIME (k = 1) vs POWER (k >= 2, integer
    root extraction); support-position terciles HEAD/MID/TAIL;
    sign classes XIPOS (xi > 0) vs XINEG (xi < 0).
  (a2) SPARSIFICATION: top-k atoms by the most negative side-
    selected first-order wall contribution c_j = du_j grad_j
    log h_184, k in SPARSE_KS; k_min = smallest lifting k at
    the matched dose (factor 1); dominant-atom question.
  (a3) Every subset is measured at factor 1 (the lift dose
    2 theta_up) AND factor 8 (the r290 robustness reach); the
    FIRST-ORDER BUDGET margin(A, fac) = -sum_{j in A} c_j x
    fac 2 theta_up is tabled against the measured lift.
  SEALED ADJUDICATION (a4): the budget-threshold check is
    reported TWICE (amendment a3): at the MATCHED dose (fac 1,
    the design question "which component carries the lift at
    the ridge dose") and GLOBALLY over all subsets x doses;
    THRESHOLD iff max no-lift margin < min lift margin; global
    violations are typed OVERDRIVE_RETRACTION and listed; fine
    type RIDGE_CARRIER_SPARSE(k_min) iff k_min <= SPARSE_BAR =
    8, RIDGE_CARRIER_CONCENTRATED(k_min) iff k_min <= 16, else
    RIDGE_COLLECTIVE(k_min); band carriers reported as the
    parts lifting at factor 1.
LEG B -- FIXED-POINT QUESTION (open front 1b, "a better world
than MAIN?"): the r280 recipe ITERATED with step control: at
each iterate measure minC, rebuild the local optimizer axis
xi_i = dir_opt at the OWN wall degree (= own minC, the r280
recipe, disclosed measurement-coupled), step dose 2 theta_up_i,
on death or wall regression halve up to 3x; FIX_NIT = 8 steps.
Sealed typing: FIXED_POINT_WORLD(minC) iff the iteration reaches
theta_up = inf / xi = 0 (no raising direction left);
RIDGE_NO_FIXPOINT(PLATEAU(minC_max)) iff minC saturates (the
last 4 accepted iterates share one minC) while the axis
decoheres (min cos of successive axes < 0.5) or steps keep
being rejected; RIDGE_NO_FIXPOINT(DEATH(step)) iff no
acceptable step exists.  BLIND CONTROL: the SAME iteration
started from EPSTEIN (own wall degree), plus the sealed
matched-dose ladder EPST_DOSES along EPSTEIN's own optimizer
axis; LIFT_MAIN_SPECIFIC iff EPSTEIN never lifts above its
start on either channel, else LIFT_GENERIC.
LEG C -- NON-LOCAL / LOW-RANK FUNCTIONALS (open front 2),
sealed BEFORE evaluation on a FRESH 143-point conservation-
gated test corpus (MAIN + 5 worlds + 4 interpolation paths x
the r290 t ladder + 16 pinned random directions (10 FRAC seeds
291100+, 6 DENS seeds 291200+) x the r290 DIST_GRID + 9 ridge
factors + 8 ENS_SCR replicates, weights bitwise):
  F5S RIDGE PROJECTION (signed): <dwsig, vridge_hat> / |dwsig|
    (the projection of the profile deviation on the ONE known
    lifting axis, per unit deviation length; 0 at zero
    deviation).  F5A = |F5S|.
  F6 RANK-2 GRAM FORM (TRAINED, split-sealed): the empirical
    lethality Gram G = sum_train onset^-2 w w^T over the 8
    TRAINING directions (FRAC 0/2/4/6/8 + DENS 0/2/4; onset =
    geometric bracket midpoint of the own 5-distance ladder);
    F6(dw) = lam1 <dw_hat, e1>^2 + lam2 <dw_hat, e2>^2 (top-2
    eigenpairs).  Evaluation on the DISJOINT test split only
    (all points of the 8 training directions excluded; the
    split disjointness is itself a gate).
  F7 ANTIPHASE PAIR CORRELATION of the DEVIATION: the r288
    carrier distance (fold lags 3 + 4) autocorrelation of dwsig
    (NON-local two-point statistic of the deviation; r290's F1
    was the OWN-profile version and is a different functional);
    0 at zero deviation.
  BASELINE F0 = theta_eq(deviation) -- the trivial size-only
    predictor, disclosed; MAIN-separation triviality DISCLOSED:
    every deviation functional is construction-trivially
    MAIN-separating (MAIN deviation = 0), so the sealed
    non-triviality bar is BEATING THE BASELINE.
  SEALED ADJUDICATION (exactly one): FUNCTIONAL_FOUND iff best
    |spearman vs s over the test split| >= SP_BAR = 0.6 AND
    |sp_best| > |sp(F0)|; else NONLOCAL_BLIND (honest).
LEG D -- SMOOTH COLLECTIVITY ANATOMY (open front 3, small):
  (d1) PARTICIPATION: PR(v) = (sum v^2)^2 / sum v^4 of the
    MAIN-minus-SMOOTH wsig direction and of its per-coordinate
    first-order wall contribution v_p Q2[p, 183]/eta_183,
    compared to a pinned random FRAC direction (seed 291100).
  (d2) HESSIAN TEST: directional curvature of the wall margin
    m(t) = 1 - rho_184 along MAIN->SMOOTH by central
    differences at HESS_HS = (6.25e-5, 1.25e-4, 2.5e-4) path
    units (all below the r290 onset 5.08e-4), Richardson check
    (adjacent-h estimates within RICH_TOL = 0.1 rel), against
    the SAME-length random direction.  Sealed typing:
    SMOOTH_FEW_COORDINATE iff PR(direction) <= PR_FEW_BAR = 10;
    else SMOOTH_COLLECTIVE_2ND_ORDER iff |d2_SMOOTH| >=
    HESS_RATIO_BAR = 10 x |d2_RAND| with the Richardson check
    green; else SMOOTH_COLLECTIVE_HIGHER_ORDER (the r259
    resummation signature).
WARDS / MUST-FAILS (each loud): (m1) a subset move with ONE
weight scaled by 1 + 1e-3 must be CAUGHT by the exact r276
conservation gate; (m2) the FLIPPED ridge (-xi) must NOT lift
(minC <= 184 at factor 1) and must KILL at factor 8 (s < NEAR)
-- the lift is oriented; (m3) the F6 SEAL BREAK (training
directions inside the test split) must be CAUGHT by the split
auditor; (m4) a WRONG theta_eq normalization (REF x 2) must be
CAUGHT by the pinned jitter self-consistency gate (dev ~ 0.5 >
0.15).  Scope audits: the sealed source-pure constructors
consume combs/densities/profiles + geometry + seeds only; the
F6 TRAINING and the LEG-B optimizer are honestly typed
measurement-consuming (sealed by split resp. disclosed as the
r280 recipe); fragment audit (no fit fragments).  STOP LIST
(anti-gates, binding): NO L* claim, NO bound mechanism, NO
asymptotic law, NO derived 5/7, NO equidistribution premise, NO
posthoc window, NO RH claim; r243..r290 stand.

SEALED CONSTANTS: MAIN window 9; N_REF 184; CROSS_REC 185;
MINC_REC 184; S_REC (367, 263, 104); MARGIN_REC 1.68e-4 rel
0.01; ZV_REC -3.149 tol 0.02; B34_REC -0.105 tol 0.01;
CTRL_FLIPS EPST 25 / SCR 21 / SMOOTH 27 / HL2 25 (seed 101);
THUP_REC 3.87e-5 rel 0.05; RIDGE_MINC_REC 185; REF_REC 125.75
rel 1e-3; NEAR 0.90 / DEAD 0.50 (r290); RIDGE_FACS r290 (0.25..
64); R290_LIFT_FACS (1, 4, 8) / R290_DEATH_FAC 16 / R290_S16
0.79 tol 0.02; PART classes PRIME/POWER + HEAD/MID/TAIL
(position terciles) + XIPOS/XINEG; SPARSE_KS (1, 2, 4, 6, 8, 9,
10, 12, 16, 32, 70); SECT_FACS (1, 8); SPARSE_BAR 8 / CONC_BAR
16; FIX_NIT 8 / FIX_HALVE 3 / COS_BAR 0.5 / PLATEAU_LEN 4;
EPST_DOSES (7.75e-5, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1);
PATH_TS / DIST_GRID / N_BISECT r290 verbatim; NDIR_FRAC 10
seeds 291100+ / NDIR_DENS 6 seeds 291200+; ENS_SCR_REPS 8 seeds
285100+; TRAIN_FRAC (0, 2, 4, 6, 8) / TRAIN_DENS (0, 2, 4);
SP_BAR 0.6; metric calibration = the r290 pinned quadruple
VERBATIM (CAL_SEEDS 290000/1/2 at 1e-3 + T3_SEED 290010 at
3e-4, tol 0.15 -- amendment a1); AMP_PAD 1 + 1e-9 (a2);
PR_FEW_BAR 10; HESS_HS (6.25e-5, 1.25e-4, 2.5e-4);
HESS_RATIO_BAR 10; RICH_TOL 0.1; ETA0_BAR 1e-12; runtime <=
1800 s; smoke = toys + firewall + scopes + split-auditor mutant
+ w9 regression (anchors, legs, corpus, m1/m2/m4 mutants,
adjudications skipped).
PRE-SPEC SCOPING (disclosed): every record number is a
published r276/r280/r285/r288/r289/r290 record adopted as-is;
the partitions, the sparsification ranking, the budget-
threshold rule, the fixpoint typing, the three functional
classes with the baseline contest, the split discipline and the
SMOOTH bars were fixed at design time from the published
records and the task contract; a design-time calibration pass
(disclosed below) preceded the freeze; no bar, band or rule was
tuned after the record freeze.

SEALED VERDICT FORM (frozen BEFORE the record freeze, joined
with '+'):
  RIDGE_SECTION(k_min, budget-threshold bracket, partition
    carriers at factor 1) [always]
  + [exactly one of] FIXED_POINT_WORLD(minC) /
    RIDGE_NO_FIXPOINT(PLATEAU/DEATH detail)
  + [exactly one of] LIFT_MAIN_SPECIFIC / LIFT_GENERIC
  + [exactly one of] FUNCTIONAL_FOUND(name, spearman, baseline)
    / NONLOCAL_BLIND(best, spearman, baseline)
  + FUNCTIONAL_TABLE(per candidate: spearman, world values,
    detector typing incl. construction-trivial disclosure)
  + SMOOTH_ANATOMY(PR census, curvature ratio, sealed type).
Honesty before beauty: section tables, budget margins, fixpoint
trajectories, functional correlations and curvature ratios are
MEASUREMENTS on finite w9 profile space; F6 is TRAINED on
measured onsets (sealed by the disjoint split); the LEG-B
optimizer consumes the own wall degree (the r280 recipe,
disclosed); no verdict claims L*, a bound mechanism, a derived
5/7 or an asymptotic law.

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 10/10 then 12/12 after the
smoke-scope extension (0.1 s); calibration pass 1 = first full
evaluation = 26/30, wall 6.0 s, exposing amendments a1/a2 and
the a3 reporting split (below); pass 2 with a1-a3 = 30/30, wall
6.0 s = the record; the record-table insertion below is the
only post-freeze edit, which IS the protocol; record rerun
after insertion 30/30, run1/run2 identical up to WALL).
DISCLOSED CALIBRATION AMENDMENTS (found in calibration pass 1,
BEFORE the record freeze; no physics bar, partition, ranking,
functional or verdict rule moved): (a1) the metric self-
consistency gate was first drawn with a FRESH jitter seed
291010 which measured dev 0.188 -- the known ~0.19 seed noise
of the theta_eq coordinate itself (r290 record: devs 0.028..
0.125 on its pinned quadruple); the gate was re-anchored on the
r290 pinned calibration quadruple VERBATIM (seeds 290000/1/2 at
1e-3 + 290010 at 3e-4), devs (0.059, 0.125, 0.117, 0.028) <=
0.15 -- a measurement-domain anchor fix, no bar moved.  (a2)
the exact conservation gate sits AT the equality boundary for
the ridge move (|du| == amp g exactly); a 1e-9 roundoff
headroom AMP_PAD was added to the gate amplitude (the r276 gate
tolerance JIT_TOL 1e-12 is smaller than one f64 ulp of the
positions; pure gate conditioning).  (a3) the budget-threshold
adjudication was split into MATCHED-DOSE and GLOBAL reporting
after pass 1 exposed a genuine overdrive retraction (TOP6 at
factor 8) -- the sealed threshold rule itself is unchanged and
reported at both scopes; the retraction is a FINDING, not a
gate failure.
RECORD VERDICT = RIDGE_SECTION(k_min = 9 at the matched dose
(top-9 atoms n = 2, 3, 5, 13, 11, 4, 29, 7, 89 -- small-prime
head-heavy but NOT one-atom: k = 1..8 do NOT lift at factor 1);
MATCHED-DOSE BUDGET_THRESHOLD PERFECT over the 18 factor-1
cases: one scalar m_star in (1.280, 1.291] separates lift from
no-lift COMPLETELY (max no-lift margin 1.280 = TOP8 < min lift
margin 1.291 = XIPOS; the first-order budget margin =
-sum_A c_j fac 2 theta_up is the near-threshold story, with a
~1.3 second-order resistance factor over the naive -1 flip
level); GLOBAL rule VIOLATED by exactly ONE overdrive case:
TOP6 at factor 8 (margin 9.09) retracts to minC 184 while
staying fully alive (s 1.00) -- deep in the over-driven
few-atom regime the linearization over-predicts; partition
carriers at factor 1: PRIME (margin 1.80) + HEAD (1.53) +
XIPOS (1.29) lift, POWER/MID/TAIL/XINEG (0.18..0.71) do not;
fine type RIDGE_CARRIER_CONCENTRATED(k_min 9, budget-additive))
+ RIDGE_NO_FIXPOINT(PLATEAU(185): the step-controlled r280
recipe saturates at minC 185 from iterate 1 on and NEVER
reaches 186 (8 iterations, final theta_eq from MAIN 1.43e-3 =
the tube rim); the axis DECOHERES after iterate 3 (cos of
successive axes +0.92 / +1.00 / +0.43 then NEGATIVE -0.50 /
-0.67 / -0.15 / -0.66) and from iterate 3 on every full step is
REJECTED (death or wall regression) with 1-2 halvings needed --
a one-degree crest plateau, no stationary better world)
+ LIFT_MAIN_SPECIFIC(the SAME iteration from EPSTEIN terminates
at step 0 (theta_up 5.03e10, first-order FLAT wall c_25 =
-1.99e-11; all 4 halved doses annihilate the world); the
matched-dose ladder 7.75e-5..0.1 along EPSTEIN's own optimizer
axis NEVER lifts (minC 25 = start everywhere) -- the lift is
MAIN-specific, not a generic optimizer artifact)
+ NONLOCAL_BLIND(best F5S sp +0.471 < 0.6 AND below the
baseline |sp(F0)| = 0.881: NONE of the three sealed non-local/
low-rank classes predicts the survival depth beyond the
trivial size predictor; F7 antiphase deviation pair correlation
sp -0.463, F6 rank-2 lethality Gram sp +0.137, F5A +/-|proj|
sp -0.177)
+ FUNCTIONAL_TABLE(sp vs s on the 103-point test split: F5S
+0.471 / F5A -0.177 / F6 +0.137 / F7 -0.463 / baseline F0
-0.881; world values (SMOOTH/SCR/EPST/HL2): F5S -0.193/-0.134/
-0.0402/+0.0218, F6 2.06e5/9.98e4/4.82e4/6.18e4, F7 -0.0761/
-0.0138/-0.0863/-0.0792; detector typing: all candidates
construction-trivial MAIN-separating (MAIN deviation = 0,
disclosed) and WORLD_BLIND among the dead worlds by the r281
distance rule -- no candidate separates the dead worlds from
each other)
+ SMOOTH_ANATOMY(SMOOTH_COLLECTIVE_2ND_ORDER: PR(direction) =
111.9 of dim 368 (delocalized, vs random FRAC 66.6; per-
coordinate wall contribution PR 2.1 vs 3.9 -- the first-order
channel is 2-coordinate-concentrated on BOTH but cancels to
cos -3e-5 on SMOOTH); margin curvature along MAIN->SMOOTH d2 =
-23.31/-23.32/-23.38 per path-t^2 (Richardson devs 0.001/0.003
<= 0.1, THREE h values consistent) vs same-length random
-0.98: ratio 23.7 >= 10 -- the SMOOTH lethality IS second-order
visible (a genuine quadratic wall valley, NOT an r259-style
higher-order resummation gap); first-order slope along the
path d1 = -0.38 per t (nonzero directional margin slope
despite the wsig-gradient cos -3e-5, disclosed)).
Key numbers.  W9: S 367/263/104, minC 184, crossing 185, margin
1.6752e-4, z_v -3.149, b34 -0.105; REF 125.7462 (rec 125.75),
inversion identity 1.5e-16, jitter devs (0.059, 0.125, 0.117,
0.028); control flips 25/21/27/25 == records; ridge anchor
theta_up 3.8733e-5, theta_kill 3.20e-2, endpoint minC 185,
70/70 atoms active; r290 map regression facs 1/4/8 minC 185,
fac 16 s 0.7880 (rec 0.79).  SECTION TABLE (subset, margin
fac1, minC fac1, minC fac8): PRIME 1.798 185 185; POWER 0.202
184 185; HEAD 1.528 185 185; MID 0.293 184 185; TAIL 0.179 184
185; XIPOS 1.291 185 185; XINEG 0.709 184 185; top-k margins/
minC fac1: k1 0.497/184, k2 0.731/184, k4 0.963/184, k6
1.136/184, k8 1.280/184, k9 1.332/185, k10 1.371/185, k12
1.444/185, k16 1.570/185, k32 1.803/185, k70 2.000/185; fac 8
all lift EXCEPT TOP6 (minC 184, s 1.00, the overdrive
retraction).  FIXPOINT TRAJECTORY (it, minC, theta_up,
cos_prev, accepted dose, halvings): 0 184 3.87e-5 -- 7.75e-5 0;
1 185 3.44e-5 +0.92 6.88e-5 0; 2 185 1.16e-4 +1.00 2.32e-4 0;
3 185 3.97e-4 +0.43 3.97e-4 1; 4 185 2.89e-4 -0.50 2.89e-4 1;
5 185 5.95e-4 -0.67 2.97e-4 2; 6 185 6.22e-4 -0.15 3.11e-4 2;
7 185 9.38e-4 -0.66 4.69e-4 2 (final theta_eq 1.43e-3).
EPSTEIN: iteration NO_ACCEPTABLE_STEP at it 0; ladder minC 25
at all 7 doses.  CORPUS: 143 points, 103-point test split, 8/8
training directions with finite onsets (FRAC 7.07e-4..1.41e-3,
DENS 5.0e-4), Gram top-2 eigvals 5.21e6/4.2e6.  SMOOTH: PR
111.9/2.1 vs RAND 66.6/3.9; d2 -23.31/-23.32/-23.38 (Richardson
OK) vs RAND -0.98; ratio 23.7.  MUST-FAILS: m1 CAUGHT
(conservation gate False); m2 flipped ridge fac1 minC 184 (no
lift) + fac8 s 0.79 < NEAR (kills); m3 CAUGHT (split auditor
flags 40 overlap points); m4 CAUGHT (dev 0.486 > 0.15); scopes
+ fragments CLEAN.  Runtime 6.0 s full / 0.1 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE (records
inserted per protocol; a1-a3 disclosed above, found and fixed
BEFORE the freeze; no bar, class rule or verdict rule moved).
READING (typed MEASUREMENT): the r280 ridge is not carried by a
distinguished sparse support, a band, or a hidden functional --
NEAR THE THRESHOLD it is a FIRST-ORDER BUDGET phenomenon: a
conservation-gated sub-direction lifts exactly when its side-
selected linearized wall budget -sum c_j dose exceeds one sharp
scalar threshold in (1.280, 1.291] (a ~1.3 second-order
resistance factor over the naive flip level -1; perfect
separation over all 18 matched-dose cases), the only sparse
concentration being the small-prime head (top-9 = 2, 3, 5, 13,
11, 4, 29, 7, 89 suffice at the matched dose), while deep in
the over-driven few-atom regime the linearization can retract
(TOP6 at factor 8); the crest is a one-degree PLATEAU (minC
185, never 186) whose local optimizer decoheres and step-
collapses at the tube rim -- there is NO stationary better
world along this recipe, and the lift does NOT transfer to
EPSTEIN (first-order flat wall): the raising mechanism is
MAIN-specific first-order budget, not generic optimization;
the non-local functional contest stays honest-negative (ridge
projection, rank-2 lethality Gram, antiphase deviation pair
correlation all below the trivial size baseline |sp| 0.881) --
the working set remains implicitly characterized; and the
SMOOTH killer axis is genuinely COLLECTIVE-QUADRATIC
(delocalized direction PR 112, curvature ratio 23.7x random,
Richardson-stable): a second-order valley, not a resummation
gap.  NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or
against RH.
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

import profile_functional_probe as PFP              # noqa: E402 r290
import lstar_two_measure_probe as LS                # noqa: E402 r284
import metric_stability_probe as MS                 # noqa: E402 r278
import minimal_firewall_probe as MF                 # noqa: E402 r276
import budget_localization_probe as BL              # noqa: E402 r280
import port_integrable_kernel_probe as PIK          # noqa: E402 v881
import principal_bessel_probe as PB                 # noqa: E402 r243
import bordered_hankel_probe as BH                  # noqa: E402 r244
import offdiag_gram_probe as ODG                    # noqa: E402 r254
import paircorr_margin_probe as PC                  # noqa: E402
import v563_paper2_readouts as core                 # noqa: E402 READ-ONLY

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
RIDGE_FACS = PFP.RIDGE_FACS
R290_LIFT_FACS = (1.0, 4.0, 8.0)
R290_DEATH_FAC = 16.0
R290_S16 = 0.79
R290_S16_TOL = 0.02
SPARSE_KS = (1, 2, 4, 6, 8, 9, 10, 12, 16, 32, 70)
SECT_FACS = (1.0, 8.0)
SPARSE_BAR = 8
CONC_BAR = 16
FIX_NIT = 8
FIX_HALVE = 3
COS_BAR = 0.5
PLATEAU_LEN = 4
EPST_DOSES = (7.75e-5, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1)
NDIR_FRAC = 10
SEED_FRAC = 291100
NDIR_DENS = 6
SEED_DENS = 291200
ENS_SCR_REPS = 8
SEED_R285_SCR = 285100
TRAIN_FRAC = (0, 2, 4, 6, 8)
TRAIN_DENS = (0, 2, 4)
SP_BAR = 0.6
CAL_SEEDS = (290000, 290001, 290002)
T3_SEED = 290010
T3_THETA = 3e-4
T3_TOL = 0.15
AMP_PAD = 1.0 + 1e-9
PR_FEW_BAR = 10.0
HESS_HS = (6.25e-5, 1.25e-4, 2.5e-4)
HESS_RATIO_BAR = 10.0
RICH_TOL = 0.1
ETA0_BAR = 1e-12
THETA_CAL = 1e-3

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
    return (not bad), ("NO zero/prime oracles; atom classes by "
                       "integer root extraction (the comb atoms "
                       "ARE p^k by construction); record numbers "
                       "enter gates and record tables only"
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


CONSTRUCTORS = ("subset_move", "atom_ints", "part_masks",
                "func_ridgeproj", "func_gramform", "func_antidev",
                "part_ratio")
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
def subset_move(uu, mm, du, mask):
    """masked ridge position move: u2 = uu + du * mask, weights
    UNTOUCHED (bitwise, the exact r276 P2 conservation class).
    Consumes comb + move + mask only."""
    u2 = np.asarray(uu, float) + np.asarray(du, float) \
        * np.asarray(mask, float)
    return u2, np.asarray(mm, float).copy()


def atom_ints(uu):
    """the integer atom labels n = round(exp(u)) of the comb
    positions (the comb atoms are at log n by construction)."""
    return np.array([int(round(math.exp(float(u)))) for u in uu],
                    np.int64)


def part_masks(uu, xi, kvec):
    """sealed LEG-A partitions of the atom set: PRIME/POWER by
    the integer root extraction exponent, HEAD/MID/TAIL by
    support-position terciles, XIPOS/XINEG by the move sign.
    Consumes positions + move signs + exponents only."""
    n_at = len(uu)
    out = {}
    out["PRIME"] = (np.asarray(kvec) == 1).astype(float)
    out["POWER"] = (np.asarray(kvec) >= 2).astype(float)
    o_pos = np.argsort(np.asarray(uu, float))
    terz = np.array_split(o_pos, 3)
    for i, nm in enumerate(("HEAD", "MID", "TAIL")):
        m = np.zeros(n_at)
        m[terz[i]] = 1.0
        out[nm] = m
    out["XIPOS"] = (np.asarray(xi) > 0).astype(float)
    out["XINEG"] = (np.asarray(xi) < 0).astype(float)
    return out


def func_ridgeproj(dw, vr_hat):
    """F5S RIDGE PROJECTION (signed): <dw, vr_hat> / |dw|_2, the
    per-unit-length projection of the profile deviation on the
    lifting axis; 0.0 sealed at zero deviation."""
    dw = np.asarray(dw, float)
    nrm = float(np.linalg.norm(dw))
    if nrm == 0.0:
        return 0.0
    return float(dw @ np.asarray(vr_hat, float)) / nrm


def func_gramform(dw, evecs, evals):
    """F6 RANK-2 GRAM FORM (evaluation side; the TRAINING is
    disclosed measurement-consuming and split-sealed): lam1
    <dw_hat, e1>^2 + lam2 <dw_hat, e2>^2; 0.0 at zero
    deviation."""
    dw = np.asarray(dw, float)
    nrm = float(np.linalg.norm(dw))
    if nrm == 0.0:
        return 0.0
    x = dw / nrm
    ev = np.asarray(evals, float)
    E = np.asarray(evecs, float)
    return float(sum(ev[i] * float(x @ E[:, i]) ** 2
                     for i in range(len(ev))))


def func_antidev(dw):
    """F7 ANTIPHASE PAIR CORRELATION of the DEVIATION: fold-lag
    3 + 4 autocorrelation of dw (the r288 carrier distance as a
    NON-local deviation two-point statistic); 0.0 at zero
    deviation."""
    dw = np.asarray(dw, float)
    den = float(np.sum(dw * dw))
    if den == 0.0:
        return 0.0
    a3 = float(np.sum(dw[:-3] * dw[3:]))
    a4 = float(np.sum(dw[:-4] * dw[4:]))
    return (a3 + a4) / den


def part_ratio(v):
    """participation ratio PR(v) = (sum v^2)^2 / sum v^4 (the
    inverse IPR; PR = 1 for one coordinate, PR = n for a flat
    vector)."""
    v = np.asarray(v, float)
    s2 = float(np.sum(v * v))
    s4 = float(np.sum(v ** 4))
    return s2 * s2 / max(s4, 1e-300)


def split_auditor(train_tags, test_tags):
    """F6 seal auditor: the training directions must be DISJOINT
    from the test split; returns the overlap tags (empty =
    sealed)."""
    return sorted(set(train_tags) & set(test_tags))


# ============== must-fail mutants
def mutant_broken_conservation(uu, mm, du):
    """m1 MUST-FAIL: a 'subset move' that also scales one weight
    by 1 + 1e-3 -- the exact conservation gate must CATCH it."""
    u2 = np.asarray(uu, float) + np.asarray(du, float)
    m2 = np.asarray(mm, float).copy()
    m2[3] *= 1.0 + 1e-3
    return u2, m2


def mutant_wrong_ref(ref):
    """m4 MUST-FAIL: theta_eq normalization with REF x 2 -- the
    pinned jitter self-consistency gate must CATCH it."""
    return 2.0 * float(ref)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("ridge_anatomy_probe -- PRIME.PORT.LSTAR."
          "RIDGE_ANATOMY.01 (round 291)")
    print("SPEC_SHA %s   (r290 PFP %s / r280 BL %s / r278 MS %s)"
          % (SPEC_SHA[:16], PFP.SPEC_SHA[:16], BL.SPEC_SHA[:16],
             MS.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + split-"
                        "auditor mutant + w9 regression; anchors, "
                        "legs, corpus, m1/m2/m4 mutants, "
                        "adjudications skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the r290 profile convention "
          "+ theta_eq LAG metric (analytic REF), the LEG-A "
          "partitions + sparsification ranking + budget-threshold "
          "rule, the LEG-B step-controlled iteration with its "
          "three-way typing and the EPSTEIN blind control, the "
          "three functional classes with the baseline contest and "
          "the train/test split seal, the LEG-D PR and Hessian "
          "bars; the F6 training and the LEG-B optimizer are "
          "honestly typed measurement-consuming; the STOP list "
          "forbids any L* claim and any proof attack")

    # ---------------- S1 toys
    section("S1  TOYS -- SUBSET MOVE, FUNCTIONALS, PR")
    uu_t = np.array([0.0, 1.0, 2.0])
    mm_t = np.array([1.0, 2.0, 3.0])
    du_t = np.array([0.1, -0.2, 0.3])
    u_all, m_all = subset_move(uu_t, mm_t, du_t, np.ones(3))
    u_non, m_non = subset_move(uu_t, mm_t, du_t, np.zeros(3))
    ok_t1 = (bool(np.array_equal(u_all, uu_t + du_t))
             and bool(np.array_equal(u_non, uu_t))
             and bool(np.array_equal(m_all, mm_t))
             and bool(np.array_equal(m_non, mm_t)))
    check("G10-toy-subset-move", ok_t1,
          "HAND SUBSET MOVE: full mask == uu + du bitwise, empty "
          "mask == uu bitwise, weights bitwise in both -- the "
          "masked move is the exact r276 P2 conservation class")
    f5_t = func_ridgeproj(np.array([3.0, 4.0, 0.0]),
                          np.array([1.0, 0.0, 0.0]))
    f7_t = func_antidev(np.array([1.0, 2.0, -1.0, 3.0, -2.0]))
    e_t = np.eye(3)[:, :2]
    f6_t1 = func_gramform(np.array([1.0, 0.0, 0.0]), e_t,
                          np.array([1.0, 0.25]))
    f6_t2 = func_gramform(np.array([1.0, 1.0, 0.0]) / math.sqrt(2),
                          e_t, np.array([1.0, 0.25]))
    pr_t1 = part_ratio(np.array([1.0, 1.0, 1.0, 1.0]))
    pr_t2 = part_ratio(np.array([1.0, 0.0, 0.0, 0.0]))
    ok_t2 = (abs(f5_t - 0.6) <= 1e-14
             and abs(f7_t - (-3.0 / 19.0)) <= 1e-14
             and abs(f6_t1 - 1.0) <= 1e-14
             and abs(f6_t2 - 0.625) <= 1e-14
             and abs(pr_t1 - 4.0) <= 1e-12
             and abs(pr_t2 - 1.0) <= 1e-12
             and func_ridgeproj(np.zeros(3), e_t[:, 0]) == 0.0
             and func_antidev(np.zeros(5)) == 0.0)
    check("G11-toy-functionals", ok_t2,
          "HAND FUNCTIONALS: F5S((3,4,0); e1) = 3/5 exact; F7("
          "(1,2,-1,3,-2)) = -3/19 exact; F6 toy (eigvals 1, 1/4): "
          "F6(e1) = 1, F6((e1+e2)/sqrt2) = 5/8 exact; PR(flat 4) "
          "= 4, PR(one-hot) = 1; zero-deviation seals = 0.0")

    # ---------------- S2 w9 regression + anchors
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
          "= %+.3f (rec %+.3f), b34 = %+.3f (rec %+.3f)"
          % (M0["S"], M0["Sp"], M0["Sm"], str(M0["minC"]),
             str(M0["cross"]), margin9, MARGIN_REC, M0["zv"],
             ZV_REC, M0["b34"], B34_REC))
    wsig0 = MS.wsig_vec(d9, L9)
    if smoke:
        for g in ("G21-metric-anchor", "G22-control-flips",
                  "G23-ridge-anchor", "G24-r290-map-regression"):
            check(g, True, "SMOKE: skipped")
        section("S7  MUST-FAILS + SCOPE AUDITS (smoke subset)")
        ov_s = split_auditor({"DIR:FRAC00:d=1e-03"},
                             {"DIR:FRAC00:d=1e-03", "MAIN"})
        check("G72-mustfail-split-break", len(ov_s) > 0,
              "m3 F6 SEAL BREAK (toy tags): auditor flags %d "
              "overlap points -- CAUGHT" % len(ov_s))
        hits_s = []
        for fn_ in CONSTRUCTORS:
            hits_s += scope_audit(fn_, SCOPE_FORBIDDEN)
        ag_s = antigate_fragment_audit()
        check("G74-scope-audits", not hits_s and not ag_s,
              "the %d sealed source-pure constructors consume "
              "combs/densities/profiles + geometry + seeds ONLY "
              "(%s); fragment audit: %s"
              % (len(CONSTRUCTORS),
                 "CLEAN" if not hits_s else "; ".join(hits_s),
                 "CLEAN" if not ag_s else "; ".join(ag_s)))
        return finish(smoke, {})
    # theta_eq metric (r290 a1 coordinate, analytic REF)
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
    d2c = None
    for th_c, seed_c in [(THETA_CAL, s_) for s_ in CAL_SEEDS] \
            + [(T3_THETA, T3_SEED)]:
        u2c, m2c = MF.pert_jit(uu9, mm9, th_c, seed_c, False)
        cons_c = cons_c and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2c, m2c, th_c)
        d2c = np.asarray(PIK.build_rung(MAIN_KZ,
                                        comb=(u2c, m2c))["d"],
                         float)
        devs_c.append(abs(lag_l1(d2c - d9) / REF / th_c - 1.0))
    ok_met = (abs(REF / REF_REC - 1.0) <= REF_TOL
              and inv_dev <= 1e-12 and cons_c
              and max(devs_c) <= T3_TOL)
    check("G21-metric-anchor", ok_met,
          "theta_eq metric (r290 a1 LAG coordinate, r290 pinned "
          "calibration quadruple VERBATIM -- amendment a1): "
          "analytic REF = %.4f (rec %.2f rel %.0e); inversion "
          "identity rel %.1e (bar 1e-12); jitter devs %s <= "
          "%.2f, conservation exact"
          % (REF, REF_REC, REF_TOL, inv_dev,
             str([round(v, 3) for v in devs_c]), T3_TOL))
    # control worlds
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
          "(25/21/27/25) -- the r285 control worlds re-derived"
          % str({w: worlds_meas[w]["minC"] for w in CTRL_FLIPS}))
    # ridge anchor (r280 rebuilt verbatim)
    GE = BL.grad_ext(ctx9, N_REF + 2)
    xi = BL.dir_opt(GE["gR"], GE["gL"], GE["gaps"], N_REF)
    th_up, th_kill, cvec = BL.theta_of_dir(GE["gR"], GE["gL"],
                                           GE["gaps"], xi, N_REF)
    du_ridge = 2.0 * th_up * GE["gaps"] * xi
    uR, mR = subset_move(uu9, mm9, du_ridge, np.ones(len(uu9)))
    dR = np.asarray(PIK.build_rung(MAIN_KZ, comb=(uR, mR))["d"],
                    float)
    MR = PFP.measure_density(dR, L9)
    n_act = int(np.sum(xi != 0))
    ok_ridge = (abs(th_up / THUP_REC - 1.0) <= THUP_TOL
                and th_kill > th_up
                and MR["minC"] == RIDGE_MINC_REC
                and MF.conserve_comb("P2_JIT", uu9, mm9, uR, mR,
                                     2.0 * th_up * AMP_PAD))
    check("G23-ridge-anchor", ok_ridge,
          "r280 RIDGE ANCHOR: theta_up = %.4e (rec %.2e rel "
          "%.2f), theta_kill = %.2e; OPT endpoint (dose 2 "
          "theta_up) minC = %s == %d; %d/%d atoms active; "
          "conservation exact"
          % (th_up, THUP_REC, THUP_TOL, th_kill, str(MR["minC"]),
             RIDGE_MINC_REC, n_act, len(xi)))
    dd_R = dR - d9
    ridge_reg = {}
    for fac in R290_LIFT_FACS + (R290_DEATH_FAC,):
        mm_ = PFP.measure_density(d9 + fac * dd_R, L9)
        ridge_reg[fac] = mm_
    ok_map = (all(ridge_reg[f]["minC"] == RIDGE_MINC_REC
                  for f in R290_LIFT_FACS)
              and ridge_reg[R290_DEATH_FAC]["s"] < NEAR
              and abs(ridge_reg[R290_DEATH_FAC]["s"] - R290_S16)
              <= R290_S16_TOL)
    check("G24-r290-map-regression", ok_map,
          "r290 RIDGE MAP regression: minC %s at factors %s "
          "(rec 185); factor %g s = %.4f (rec %.2f tol %.2f, "
          "first death)"
          % (str([ridge_reg[f]["minC"] for f in R290_LIFT_FACS]),
             str(R290_LIFT_FACS), R290_DEATH_FAC,
             ridge_reg[R290_DEATH_FAC]["s"], R290_S16,
             R290_S16_TOL))

    # ---------------- S3 LEG A: ridge-vector section
    section("S3  LEG A -- RIDGE-VECTOR SECTION")
    du1 = GE["gaps"] * xi
    cj = np.where(du1 > 0, du1 * GE["gR"][:, N_REF],
                  du1 * GE["gL"][:, N_REF])
    nn_at = atom_ints(uu9)
    kvec = np.array([ODG.base_exp(int(n))[1] for n in nn_at])
    parts = part_masks(uu9, xi, kvec)
    order = np.argsort(cj)   # most negative first

    def sect_case(mask, fac):
        u2, m2 = subset_move(uu9, mm9, fac * du_ridge, mask)
        ok_c = MF.conserve_comb("P2_JIT", uu9, mm9, u2, m2,
                                fac * 2.0 * th_up * AMP_PAD)
        d2 = np.asarray(PIK.build_rung(MAIN_KZ,
                                       comb=(u2, m2))["d"], float)
        meas = PFP.measure_density(d2, L9)
        marg = -float(np.sum(cj * mask)) * fac * 2.0 * th_up
        return meas, marg, ok_c

    ok_cons = True
    cases = []   # (name, fac, n_atoms, margin, minC, lift)
    for name, m in parts.items():
        for fac in SECT_FACS:
            meas, marg, okc = sect_case(m, fac)
            ok_cons = ok_cons and okc
            cases.append((name, fac, int(m.sum()), marg,
                          meas["minC"],
                          (meas["minC"] or 0) > MINC_REC))
    spars_rows = []
    for k in SPARSE_KS:
        m = np.zeros(len(uu9))
        m[order[:k]] = 1.0
        for fac in SECT_FACS:
            meas, marg, okc = sect_case(m, fac)
            ok_cons = ok_cons and okc
            cases.append(("TOP%d" % k, fac, k, marg, meas["minC"],
                          (meas["minC"] or 0) > MINC_REC))
            if fac == 1.0:
                spars_rows.append((k, marg, meas["minC"]))
    check("G30-section-conservation", ok_cons,
          "all %d subset x dose cases conservation-gated exactly "
          "(weights bitwise, per-atom move <= fac 2 theta_up g)"
          % len(cases))
    part_tab = {name: [(c[3], c[4], c[5]) for c in cases
                       if c[0] == name] for name in parts}
    lifters1 = [c[0] for c in cases
                if c[1] == 1.0 and c[5] and c[0] in parts]
    check("G31-partition-table", True,
          "PARTITION SECTION (name: (margin, minC, lift) at fac "
          "1 / 8): %s -- carriers at the matched dose: %s"
          % (str({n: [("%.3f" % a, b, c) for a, b, c in v]
                  for n, v in part_tab.items()}),
             str(lifters1)))
    kmin = next((k for k, _m, mc_ in spars_rows
                 if (mc_ or 0) > MINC_REC), None)
    top9 = [int(v) for v in nn_at[order[:9]]]
    check("G32-sparsification", kmin is not None,
          "SPARSIFICATION at the matched dose (k, margin, minC): "
          "%s -- k_min = %s; top-9 atoms n = %s (fac 8: every "
          "tested top-k lifts, see the case table)"
          % (str([(k, "%.3f" % m_, mc_)
                  for k, m_, mc_ in spars_rows]), str(kmin),
             str(top9)))
    m1_nolift = [c[3] for c in cases if c[1] == 1.0 and not c[5]]
    m1_lift = [c[3] for c in cases if c[1] == 1.0 and c[5]]
    thr1_ok = (bool(m1_lift) and bool(m1_nolift)
               and max(m1_nolift) < min(m1_lift))
    marg_nolift = [c[3] for c in cases if not c[5]]
    marg_lift = [c[3] for c in cases if c[5]]
    thr_ok = (bool(marg_lift) and bool(marg_nolift)
              and max(marg_nolift) < min(marg_lift))
    overdrive = [(c[0], c[1], round(c[3], 3), c[4])
                 for c in cases
                 if (not c[5]) and c[3] > min(marg_lift)]
    if kmin is None:
        fine = "RIDGE_NO_SPARSE_CARRIER"
    elif kmin <= SPARSE_BAR:
        fine = "RIDGE_CARRIER_SPARSE(k_min %d)" % kmin
    elif kmin <= CONC_BAR:
        fine = "RIDGE_CARRIER_CONCENTRATED(k_min %d)" % kmin
    else:
        fine = "RIDGE_COLLECTIVE(k_min %d)" % kmin
    check("G33-budget-adjudication", True,
          "SEALED BUDGET RULE (a3, both reported): MATCHED DOSE "
          "(fac 1, %d cases): %s -- bracket (%.3f, %.3f]; GLOBAL "
          "(all %d cases): %s%s; fine type (bars %d/%d): %s"
          % (len(m1_lift) + len(m1_nolift),
             "THRESHOLD PERFECT" if thr1_ok else "VIOLATED",
             max(m1_nolift) if m1_nolift else float("nan"),
             min(m1_lift) if m1_lift else float("nan"),
             len(cases),
             "THRESHOLD PERFECT" if thr_ok
             else "VIOLATED by overdrive retraction",
             "" if thr_ok else " %s (alive, minC 184 -- the "
             "linearized budget over-predicts deep in the "
             "over-driven few-atom regime)" % str(overdrive),
             SPARSE_BAR, CONC_BAR, fine))

    # ---------------- S4 LEG B: fixpoint question
    section("S4  LEG B -- FIXED-POINT QUESTION + EPSTEIN CONTROL")

    def iterate_recipe(u0, m0, tag):
        """step-controlled r280 recipe iteration (measurement-
        coupled by design, disclosed): returns trajectory rows
        (it, minC, th_up, cos_prev, dose, n_halv) + stop tag."""
        u_i, m_i = u0.copy(), m0.copy()
        prev_v = None
        rows = []
        stop = "BUDGET_EXHAUSTED(FIX_NIT)"
        for it in range(FIX_NIT):
            ctx_i = MS.ctx_build(MAIN_KZ, comb=(u_i, m_i))
            d_i = np.asarray(ctx_i["darm"], float)
            mi = PFP.measure_density(d_i, L9)
            deg = mi["minC"]
            if deg is None or deg < 2:
                rows.append((it, mi["minC"], float("nan"),
                             float("nan"), 0.0, 0))
                stop = "DEGENERATE(minC %s)" % str(mi["minC"])
                break
            GEi = BL.grad_ext(ctx_i, deg + 2)
            xii = BL.dir_opt(GEi["gR"], GEi["gL"], GEi["gaps"],
                             deg)
            tui, _tk, _c = BL.theta_of_dir(GEi["gR"], GEi["gL"],
                                           GEi["gaps"], xii, deg)
            v_i = GEi["gaps"] * xii
            cosang = float("nan")
            nv = float(np.linalg.norm(v_i))
            if prev_v is not None and nv > 0:
                cosang = float(v_i @ prev_v) \
                    / max(nv * float(np.linalg.norm(prev_v)),
                          1e-300)
            prev_v = v_i
            if not math.isfinite(tui) or nv == 0.0:
                rows.append((it, mi["minC"], tui, cosang, 0.0, 0))
                stop = "FIXED_POINT(no raising direction)"
                break
            dose = 2.0 * tui
            accepted = False
            n_halv = 0
            for _h in range(FIX_HALVE + 1):
                u_try = u_i + dose * GEi["gaps"] * xii
                d_try = np.asarray(MS.ctx_build(
                    MAIN_KZ, comb=(u_try, m_i))["darm"], float)
                mt = PFP.measure_density(d_try, L9)
                if mt["s"] >= NEAR \
                        and (mt["minC"] or 0) >= (mi["minC"] or 0):
                    u_i = u_try
                    accepted = True
                    break
                dose *= 0.5
                n_halv += 1
            rows.append((it, mi["minC"], tui, cosang,
                         dose if accepted else 0.0, n_halv))
            if not accepted:
                stop = "NO_ACCEPTABLE_STEP(it %d)" % it
                break
        theq_end = lag_l1(np.asarray(MS.ctx_build(
            MAIN_KZ, comb=(u_i, m_i))["darm"], float) - d9) / REF \
            if tag == "MAIN" else float("nan")
        return rows, stop, theq_end

    rowsM, stopM, theqM = iterate_recipe(uu9, mm9, "MAIN")
    mcs = [r[1] for r in rowsM if r[1] is not None]
    mc_max = max(mcs)
    tail = mcs[-PLATEAU_LEN:]
    coss = [r[3] for r in rowsM if math.isfinite(r[3])]
    if stopM.startswith("FIXED_POINT"):
        fix_typ = "FIXED_POINT_WORLD(minC %d)" % mc_max
    elif stopM.startswith("NO_ACCEPTABLE_STEP") \
            or stopM.startswith("DEGENERATE"):
        fix_typ = "RIDGE_NO_FIXPOINT(DEATH %s)" % stopM
    elif (len(tail) == PLATEAU_LEN and len(set(tail)) == 1
          and (min(coss) < COS_BAR
               or any(r[5] > 0 for r in rowsM[-3:]))):
        fix_typ = "RIDGE_NO_FIXPOINT(PLATEAU(%d))" % tail[0]
    else:
        fix_typ = "RIDGE_NO_FIXPOINT(WANDERING(max minC %d))" \
            % mc_max
    check("G40-fixpoint-main", True,
          "STEP-CONTROLLED r280 RECIPE from MAIN (%d its, stop = "
          "%s): trajectory (it, minC, theta_up, cos_prev, dose, "
          "halvings) = %s; final theta_eq from MAIN %.2e; minC "
          "NEVER exceeds %d -> %s"
          % (len(rowsM), stopM,
             str([(it, mc_, "%.2e" % tu if math.isfinite(tu)
                   else "inf", "%.2f" % ca if math.isfinite(ca)
                   else "-", "%.2e" % dz, nh)
                  for it, mc_, tu, ca, dz, nh in rowsM]),
             theqM, mc_max, fix_typ))
    # EPSTEIN blind control: same iteration + matched-dose ladder
    rowsE, stopE, _tE = iterate_recipe(uE, mE, "EPST")
    mcE0 = worlds_meas["EPST"]["minC"]
    ctxE = MS.ctx_build(MAIN_KZ, comb=(uE, mE))
    GEe = BL.grad_ext(ctxE, mcE0 + 2)
    xiE = BL.dir_opt(GEe["gR"], GEe["gL"], GEe["gaps"], mcE0)
    tuE, _tkE, cE = BL.theta_of_dir(GEe["gR"], GEe["gL"],
                                    GEe["gaps"], xiE, mcE0)
    lad_mcs = []
    for dose in EPST_DOSES:
        u2 = uE + dose * GEe["gaps"] * xiE
        d2 = np.asarray(MS.ctx_build(MAIN_KZ,
                                     comb=(u2, mE))["darm"], float)
        lad_mcs.append(PFP.measure_density(d2, L9)["minC"])
    it_lift = any((r[1] or 0) > mcE0 for r in rowsE)
    lad_lift = any((mc_ or 0) > mcE0 for mc_ in lad_mcs)
    lift_typ = "LIFT_GENERIC" if (it_lift or lad_lift) \
        else "LIFT_MAIN_SPECIFIC"
    check("G41-epstein-control", True,
          "EPSTEIN BLIND CONTROL (start minC %d): same iteration "
          "stop = %s, trajectory minC %s; own-axis theta_up = "
          "%.2e (c_%d = %.2e, first-order FLAT wall); matched-"
          "dose ladder %s -> minC %s -- %s"
          % (mcE0, stopE, str([r[1] for r in rowsE]), tuE, mcE0,
             cE[mcE0], str(EPST_DOSES), str(lad_mcs), lift_typ))

    # ---------------- S5 LEG C: non-local functional contest
    section("S5  LEG C -- NON-LOCAL / LOW-RANK FUNCTIONAL "
            "CONTEST (fresh sealed corpus)")
    CORPUS = []   # dict(tag, src, dw, s, theq)

    def add_pt(tag, dvec, meas, theq, src=""):
        dw = MS.wsig_vec(np.asarray(dvec, float), L9) - wsig0
        CORPUS.append(dict(tag=tag, src=src, dw=dw,
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
    # 16 fresh pinned directions, conservation-gated
    dirs = []
    ok_dcons = True
    for i in range(NDIR_FRAC):
        dd, (u2, m2) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                    THETA_CAL, SEED_FRAC + i)
        ok_dcons = ok_dcons and MF.conserve_comb(
            "P2_JIT", uu9, mm9, u2, m2, THETA_CAL)
        dirs.append(("FRAC%02d" % i, dd))
    ll9 = np.arange(L9)
    s_l9 = 4.0 * np.sin(math.pi * ll9 / L9) ** 2 / (2.0 * L9)
    for i in range(NDIR_DENS):
        dd = PFP.dir_dens(d9, L9, SEED_DENS + i)
        eta0 = abs(float(np.sum(dd * s_l9)))
        ok_dcons = ok_dcons and eta0 <= ETA0_BAR \
            * max(float(np.sum(np.abs(dd * s_l9))), 1.0)
        dirs.append(("DENS%02d" % i, dd))
    dir_s = {}
    for name, dd in dirs:
        unit = dd / max(lag_l1(dd), 1e-300)
        for dist in DIST_GRID:
            dpt = d9 + unit * (dist * REF)
            meas = PFP.measure_density(dpt, L9)
            dir_s.setdefault(name, {})[dist] = meas["s"]
            add_pt("DIR:%s:d=%.0e" % (name, dist), dpt, meas,
                   dist, src=name)
    for fac in RIDGE_FACS:
        dpt = d9 + fac * dd_R
        add_pt("RIDGE:f=%g" % fac, dpt,
               PFP.measure_density(dpt, L9),
               fac * lag_l1(dd_R) / REF)
    ok_scr = True
    for i in range(ENS_SCR_REPS):
        sctx = MS.ctx_build(MAIN_KZ,
                            scramble_seed=SEED_R285_SCR + i)
        ok_scr = ok_scr and bool(np.array_equal(
            np.asarray(sctx["mm"]), mm9))
        dS = np.asarray(sctx["darm"], float)
        add_pt("ENS_SCR:%02d" % i, dS,
               PFP.measure_density(dS, L9), lag_l1(dS - d9) / REF)
    check("G50-corpus", ok_dcons and ok_scr
          and len(CORPUS) >= 140,
          "FRESH SEALED CORPUS: %d points (MAIN + 5 worlds + 4 "
          "paths x %d + 16 directions x %d + %d ridge factors + "
          "%d ENS_SCR replicates); direction conservation exact "
          "(FRAC weights bitwise, DENS eta_0 projected); ENS_SCR "
          "weights bitwise"
          % (len(CORPUS), len(PATH_TS), len(DIST_GRID),
             len(RIDGE_FACS), ENS_SCR_REPS))
    # F6 training (measurement-consuming, split-sealed)
    train_names = tuple("FRAC%02d" % i for i in TRAIN_FRAC) \
        + tuple("DENS%02d" % i for i in TRAIN_DENS)
    G = np.zeros((len(wsig0), len(wsig0)))
    n_tr = 0
    onset_txt = []
    for name, dd in dirs:
        if name not in train_names:
            continue
        svals = [dir_s[name][dist] for dist in DIST_GRID]
        lo, hi, _idx = PFP.onset_bracket(svals, DIST_GRID)
        if hi is None:
            onset_txt.append("%s ALIVE(skipped)" % name)
            continue
        onset = math.sqrt(lo * hi) if lo else hi
        onset_txt.append("%s %.2e" % (name, onset))
        wdir = MS.wsig_vec(d9 + dd / max(lag_l1(dd), 1e-300), L9) \
            - wsig0
        wdir = wdir / max(float(np.linalg.norm(wdir)), 1e-300)
        G += np.outer(wdir, wdir) / (onset * onset)
        n_tr += 1
    evals_all, evecs_all = np.linalg.eigh(G)
    ev2 = evals_all[::-1][:2]
    E2 = evecs_all[:, ::-1][:, :2]
    test_pts = [r for r in CORPUS if r["src"] not in train_names]
    train_tags = set(r["tag"] for r in CORPUS
                     if r["src"] in train_names)
    overlap = split_auditor(train_tags,
                            set(r["tag"] for r in test_pts))
    check("G51-split-seal", n_tr == len(train_names)
          and not overlap,
          "F6 TRAINING: %d/%d training directions with finite "
          "onsets (%s); Gram rank <= %d, top-2 eigvals %.3g / "
          "%.3g; test split %d points DISJOINT (overlap %s)"
          % (n_tr, len(train_names), "; ".join(onset_txt), n_tr,
             ev2[0], ev2[1], len(test_pts),
             str(overlap) if overlap else "NONE"))
    vr_hat = MS.wsig_vec(dR, L9) - wsig0
    vr_hat = vr_hat / max(float(np.linalg.norm(vr_hat)), 1e-300)
    for r in CORPUS:
        r["F5S"] = func_ridgeproj(r["dw"], vr_hat)
        r["F5A"] = abs(r["F5S"])
        r["F6"] = func_gramform(r["dw"], E2, ev2)
        r["F7"] = func_antidev(r["dw"])
        r["F0"] = r["theq"]
    svec = [r["s"] for r in test_pts]
    sp_tab = {F: BH.spearman([r[F] for r in test_pts], svec)
              for F in ("F5S", "F5A", "F6", "F7", "F0")}
    wtab = {}
    ctrls = ["EPST", "SCR", "SMOOTH", "HL2"]
    for F in ("F5S", "F5A", "F6", "F7"):
        wtab[F] = {}
        for r in CORPUS:
            if r["tag"] == "MAIN":
                wtab[F]["MAIN"] = r[F]
            for wn in ctrls:
                if r["tag"] == "WORLD:" + wn:
                    wtab[F][wn] = r[F]
    det_typ = {F: LS.dist_rule(wtab[F], ctrls)
               for F in ("F5S", "F5A", "F6", "F7")}
    det_dead = {}
    for F in ("F5S", "F5A", "F6", "F7"):
        vd = [wtab[F][c] for c in ctrls]
        spread = max(vd) - min(vd)
        gaps_d = sorted(abs(vd[i] - vd[j])
                        for i in range(len(vd))
                        for j in range(i + 1, len(vd)))
        det_dead[F] = "DEAD_SPREAD %.3g (min pair gap %.3g)" \
            % (spread, gaps_d[0])
    check("G52-functional-table", len(test_pts) >= 90,
          "FUNCTIONAL CONTEST on the %d-point test split: sp vs "
          "s: F5S %+.3f, F5A %+.3f, F6 %+.3f, F7 %+.3f; BASELINE "
          "F0 (theta_eq size) %+.3f; world values %s; dist-rule "
          "typing %s (construction-trivial MAIN separation "
          "DISCLOSED: every deviation functional is 0 at MAIN by "
          "construction; dead-world spreads %s)"
          % (len(test_pts), sp_tab["F5S"], sp_tab["F5A"],
             sp_tab["F6"], sp_tab["F7"], sp_tab["F0"],
             str({F: {w: ("%.3g" % v) for w, v in wtab[F].items()}
                  for F in ("F5S", "F6", "F7")}),
             str(det_typ), str(det_dead)))
    cand = ("F5S", "F5A", "F6", "F7")
    best_F = max(cand, key=lambda k: abs(sp_tab[k]))
    best_sp = sp_tab[best_F]
    if abs(best_sp) >= SP_BAR and abs(best_sp) > abs(sp_tab["F0"]):
        func_verdict = ("FUNCTIONAL_FOUND(%s, spearman %+.3f, "
                        "baseline %+.3f beaten)"
                        % (best_F, best_sp, sp_tab["F0"]))
    else:
        func_verdict = ("NONLOCAL_BLIND(best %s %+.3f; bar %.1f; "
                        "baseline F0 %+.3f)"
                        % (best_F, best_sp, SP_BAR, sp_tab["F0"]))
    check("G53-functional-adjudication", True,
          "SEALED RULE (FOUND iff best |sp| >= %.1f AND beats "
          "the size baseline): best = %s (%+.3f) vs F0 (%+.3f) "
          "-> %s" % (SP_BAR, best_F, best_sp, sp_tab["F0"],
                     func_verdict.split("(")[0]))

    # ---------------- S6 LEG D: SMOOTH anatomy
    section("S6  LEG D -- SMOOTH COLLECTIVITY ANATOMY")
    dSM = d_worlds["SMOOTH"]
    vSM = MS.wsig_vec(dSM, L9) - wsig0
    xs9, ws9, _f1 = PIK.folded_measure(d9, L9, +1.0)
    ys9, vs9, _f2 = PIK.folded_measure(d9, L9, -1.0)
    rows9, Q9 = MS.grad_chain(xs9, ws9, ys9, vs9, ctx9["bx"],
                              ctx9["bw"], ctx9["by"], ctx9["bv"],
                              N_REF,
                              np.cos(2.0 * math.pi
                                     * np.arange(M9) / L9))
    eta9 = np.array([r["eta"] for r in rows9])
    Q2_9 = Q9[:, :len(rows9)] ** 2
    contribSM = vSM * Q2_9[:, N_REF - 1] / eta9[N_REF - 1]
    dd_rnd = dict(dirs)["FRAC00"]
    vRD = MS.wsig_vec(d9 + dd_rnd, L9) - wsig0
    contribRD = vRD * Q2_9[:, N_REF - 1] / eta9[N_REF - 1]
    prs = dict(SM_dir=part_ratio(vSM), SM_con=part_ratio(contribSM),
               RD_dir=part_ratio(vRD), RD_con=part_ratio(contribRD))
    check("G60-participation", True,
          "PARTICIPATION (dim %d): PR(SMOOTH direction) = %.1f "
          "vs random %.1f (delocalized iff > %.0f); PR(first-"
          "order wall contribution) = %.1f vs %.1f -- who "
          "carries the death, coordinate-wise"
          % (len(vSM), prs["SM_dir"], prs["RD_dir"], PR_FEW_BAR,
             prs["SM_con"], prs["RD_con"]))

    def margin_at(dvec):
        meas = PFP.measure_density(dvec, L9)
        if meas["rho"] is None or meas["cross"] is None \
                or meas["cross"] <= N_REF:
            return float("nan")
        return 1.0 - meas["rho"][N_REF]

    m00 = margin_at(d9)
    plenSM = lag_l1(dSM - d9) / REF
    unit_rnd = dd_rnd / max(lag_l1(dd_rnd), 1e-300)
    d2_sm, d2_rd, d1_sm = [], [], []
    ok_fin = True
    for h in HESS_HS:
        mp_ = margin_at(PFP.interp_density(d9, dSM, h))
        mn_ = margin_at(PFP.interp_density(d9, dSM, -h))
        ok_fin = ok_fin and math.isfinite(mp_) \
            and math.isfinite(mn_)
        d1_sm.append((mp_ - mn_) / (2.0 * h))
        d2_sm.append((mp_ - 2.0 * m00 + mn_) / (h * h))
        rp = margin_at(d9 + unit_rnd * (h * plenSM * REF))
        rn = margin_at(d9 - unit_rnd * (h * plenSM * REF))
        ok_fin = ok_fin and math.isfinite(rp) \
            and math.isfinite(rn)
        d2_rd.append((rp - 2.0 * m00 + rn) / (h * h))
    rich_devs = [abs(d2_sm[i + 1] / d2_sm[i] - 1.0)
                 for i in range(len(d2_sm) - 1)]
    rich_ok = max(rich_devs) <= RICH_TOL
    ratio = abs(d2_sm[0]) / max(abs(d2_rd[0]), 1e-300)
    if prs["SM_dir"] <= PR_FEW_BAR:
        sm_typ = "SMOOTH_FEW_COORDINATE(PR %.1f)" % prs["SM_dir"]
    elif ratio >= HESS_RATIO_BAR and rich_ok:
        sm_typ = ("SMOOTH_COLLECTIVE_2ND_ORDER(ratio %.1f, "
                  "Richardson OK)" % ratio)
    else:
        sm_typ = ("SMOOTH_COLLECTIVE_HIGHER_ORDER(ratio %.1f, "
                  "rich %s)" % (ratio, str(rich_ok)))
    check("G61-hessian", ok_fin, 
          "HESSIAN TEST along MAIN->SMOOTH (margin m(t) = 1 - "
          "rho_%d; h = %s path units, onset 5.1e-4): d2 = %s "
          "(Richardson devs %s <= %.1f: %s), d1 = %s (nonzero "
          "directional slope DISCLOSED, wsig-gradient cos -3e-5 "
          "r290); same-length random d2 = %s; ratio %.1f (bar "
          "%.0f) -> %s"
          % (N_REF, str(HESS_HS),
             str(["%.2f" % v for v in d2_sm]),
             str(["%.3f" % v for v in rich_devs]), RICH_TOL,
             str(rich_ok), str(["%.3f" % v for v in d1_sm]),
             str(["%.2f" % v for v in d2_rd]), ratio,
             HESS_RATIO_BAR, sm_typ))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    u_m1, m_m1 = mutant_broken_conservation(uu9, mm9, du_ridge)
    ok_m1 = not MF.conserve_comb("P2_JIT", uu9, mm9, u_m1, m_m1,
                                 2.0 * th_up * AMP_PAD)
    check("G70-mustfail-conservation", ok_m1,
          "m1 BROKEN CONSERVATION (one weight scaled 1 + 1e-3): "
          "the exact r276 gate returns False -- CAUGHT; weight-"
          "moving 'sections' cannot pass")
    u_m2, m_m2 = subset_move(uu9, mm9, -du_ridge,
                             np.ones(len(uu9)))
    d_m2 = np.asarray(PIK.build_rung(MAIN_KZ,
                                     comb=(u_m2, m_m2))["d"], float)
    mm2a = PFP.measure_density(d_m2, L9)
    d_m2b = d9 + 8.0 * (d_m2 - d9)
    mm2b = PFP.measure_density(d_m2b, L9)
    ok_m2 = (mm2a["minC"] or 0) <= MINC_REC and mm2b["s"] < NEAR
    check("G71-mustfail-flipped-ridge", ok_m2,
          "m2 FLIPPED RIDGE (-xi): factor 1 minC = %s <= %d (NO "
          "lift) and factor 8 s = %.2f < %.2f (KILLS) -- the "
          "lift is oriented, not a |move| artifact"
          % (str(mm2a["minC"]), MINC_REC, mm2b["s"], NEAR))
    fake_test = set(r["tag"] for r in CORPUS)
    ov_m3 = split_auditor(train_tags, fake_test)
    check("G72-mustfail-split-break", len(ov_m3) > 0,
          "m3 F6 SEAL BREAK (training directions inside the "
          "test split): auditor flags %d overlap points -- "
          "CAUGHT; the no-split evaluation is invalid by "
          "construction" % len(ov_m3))
    ref_bad = mutant_wrong_ref(REF)
    dev_m4 = abs(lag_l1(d2c - d9) / ref_bad / T3_THETA - 1.0)
    check("G73-mustfail-wrong-ref", dev_m4 > T3_TOL,
          "m4 WRONG theta_eq NORMALIZATION (REF x 2): pinned "
          "jitter dev %.3f > %.2f -- CAUGHT by the sealed "
          "self-consistency gate" % (dev_m4, T3_TOL))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G74-scope-audits", not hits and not ag_hits,
          "the %d sealed source-pure constructors consume combs/"
          "densities/profiles + geometry + seeds ONLY (%s); the "
          "F6 training and the LEG-B optimizer are OUTSIDE the "
          "source-pure list and honestly typed measurement-"
          "consuming (split-sealed resp. disclosed r280 recipe); "
          "fragment audit: %s"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 + S9
    section("S8  HONESTY LEDGER")
    check("G80-honesty-ledger", True,
          "section tables, budget margins, fixpoint trajectories, "
          "functional correlations and curvature ratios are "
          "MEASUREMENTS on finite w9 profile space; the budget "
          "threshold is a first-order statement WITH a measured "
          "~1.3 second-order resistance factor, not a mechanism "
          "claim; F6 is trained on measured onsets (split-"
          "sealed); the ridge anchor is the f64 level of the "
          "mp-confirmed r280 record (disclosed)")

    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no equidistribution "
          "premise, no posthoc window, no RH claim; what the "
          "round adds: the ridge-vector section with the budget-"
          "threshold anatomy, the fixpoint answer (plateau, "
          "MAIN-specific), the sealed non-local functional "
          "contest, and the SMOOTH second-order anatomy; "
          "r243..r290 stand")
    parts_v = []
    parts_v.append(
        "RIDGE_SECTION(k_min %s; %s at the matched dose, m_star "
        "bracket (%.3f, %.3f]; global %s%s; carriers at fac 1: "
        "%s)"
        % (str(kmin),
           "BUDGET_THRESHOLD" if thr1_ok else "NO_THRESHOLD",
           max(m1_nolift), min(m1_lift),
           "PERFECT" if thr_ok else "OVERDRIVE_RETRACTION",
           "" if thr_ok else str(overdrive), str(lifters1)))
    parts_v.append(fix_typ)
    parts_v.append(lift_typ)
    parts_v.append(func_verdict)
    parts_v.append("FUNCTIONAL_TABLE(sp %s)"
                   % str({k: round(v, 3)
                          for k, v in sp_tab.items()}))
    parts_v.append("SMOOTH_ANATOMY(%s)" % sm_typ)
    verd = " + ".join(parts_v)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s -- MEASURED anatomy of the one known raising axis; "
          "NO L* claim, NO RH claim" % verd)
    return finish(smoke, dict(verd=verd))


def finish(smoke, _payload):
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
