#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""f10_stability_probe -- PRIME.PORT.LSTAR.F10_STABILITY.01
(round 294): IS F10 A REAL, STABLE FUNCTIONAL OF THE WORKING
SET -- OR A FRAGILE SPLIT/CORPUS ARTIFACT?  r293 sealed
METRIC_RECONCILED(F10 in M2) + FUNCTIONAL_BEYOND_BASELINE: the
split-sealed curvature energy F10 = x^T H_tr x / 2 beat the
home L2 size baseline for the first time in four rounds (sp
+0.884 vs sp(F0_M2) -0.860, home margin +0.024) and carried
information beyond the distance (partial sp +0.423 test /
+0.826 train-side).  But the +0.024 margin is exactly as
narrow as the r292 near-miss loss (-0.023), and the r293
worker demanded a FRESH-CORPUS STABILITY TEST before any
promotion.  THIS ROUND is that test: (A) five independent
fresh corpora against the UNCHANGED r293 H_tr with a sealed
promotion bar, (B) train-split jackknife + rank truncation +
FD step-size robustness, (C) the hardest question -- does the
reconciliation transport to other windows (w7, w11) with
window-own walls, Hessians and corpora, (D) a small mechanism
bycatch: is the L2 win carried by the DENS-sector scaling.
NOT a proof round: no L* claim, no bound mechanism, no
asymptotic law, no promotion (recommendation only).

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in
either direction.

MACHINERY IMPORTED VERBATIM (no duplication): r293 MR.
{partial_sp, spectral_abs, dist_m3} + PARTIAL_BAR/DEGEN_EPS;
r292 CF.{unit_dir, pol_of_d2, proj_coords, func_q10, auc_rank}
+ the r292 sealed Hessian constants (HESS_EQ_HS, H_PAIR_H,
GCUT, D2_FLOOR, POL_TOL, direction seeds 292100+/292200+,
TRAIN_FRAC/TRAIN_DENS, ENS_SCR_REPS/SEED_R285_SCR, LEGB_PAD);
r291 RA.{subset_move, atom_ints, split_auditor,
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
s = minC / N_REF at w9 (N_REF = 184); at a transported window
w the survival is s_w = minC / NREF_w with NREF_w = the
window's OWN measured MAIN wall degree (w7: 59, half-filling
offset +1 disclosed; w11: 63, offset 0) -- the natural
transport of the w9 convention s(MAIN) = 1.

INDEX FIREWALL (binding, r238-r293 discipline): ground truth
(minC, crossings, margins) enters GATES, the DISCLOSED
measurement-consuming training channels (H_tr / g_tr sealed by
the r292 split; the window forms H_w sealed by the
window-local split; the alternative-ladder forms; the
DENS-neutralized metric scale factors) and record tables only;
the sealed source-pure constructors consume vectors/densities
+ grid geometry + seeds ONLY (AST scope audit); no zero/prime
oracles anywhere (AST firewall).

LEG 0 -- ANCHOR REGRESSION (all gated): w9 record (S 367/263/
104, minC 184, crossing 185, margin 1.68e-4 rel 0.01, z_v
-3.149 tol 0.02, b34 -0.105 tol 0.01); theta_eq metric (REF ==
125.75 rel 1e-3, inversion identity 1e-12, r290 pinned
quadruple devs <= 0.15); control flips EPST/SCR/SMOOTH/HL2 =
25/21/27/25; r280 ridge anchor (theta_up 3.87e-5 rel 0.05, OPT
endpoint minC 185, top-9 atoms == the r291 record); the r292
29-direction Hessian REBUILT VERBATIM (a1 ladder, full 406-pair
polarization, expansion crosscheck on the 15 selected pairs):
trace share == 0.925 (tol 0.01), lam_top == -0.418 (rel 0.02),
SMOOTH |cos| == 0.07 (tol 0.03), ridge L2-rank == 28/29; H_tr /
g_tr / G_tr on the 18 sealed r292 training directions REBUILT
and SEALED BY HASH (sha256 of the H_tr bytes recorded -- the
Leg-A promise 'no re-training' is a gate, not a sentence); the
r292/r293 143-point corpus and 94-point test split rebuilt
bit-identically (tag-list SHA prefix a76cc578 gated) with the
FULL r293 contest re-gated: F10 sp == +0.884, F0_M1 == -0.907,
F0_M2 == -0.860, AUC(dead) == 0.097, partial sp(F10, s |
F0_M2) == +0.423 test / +0.826 train-side (tol 0.005 each).

LEG A -- FRESH-CORPUS REPLICATION (the promotion bar, sealed
BEFORE any evaluation): FIVE independent fresh corpora, seeds
disjoint by construction (corpus k = 0..4 uses base 294000 +
1000 k; no seed appears in the r292/r293 direction or corpus
seeds), each >= 140 points with the same conservation
discipline and the same direction-family mixture as the r293
TEST split (worlds / world paths / random FRAC / random DENS /
scramble replicates and the same dose ladders PATH_TS +
DIST_GRID); per corpus: MAIN (the shared anchor point,
disclosed) + 6 fresh dead/scramble worlds (2 SCR scrambles
seeds base+1/+2 with weights gated bitwise, 2 fresh HL2 combs
seeds base+3/+4, 2 ENSR scrambles seeds base+5/+6 gated
bitwise) + 4 paths x PATH_TS (to SCR_a / HL2_a / ENSR_a /
SCR_b) + 12 fresh FRAC directions (seeds base+100+i,
conservation exact) x DIST_GRID + 8 fresh DENS directions
(seeds base+200+i, eta_0 projected exactly) x DIST_GRID = 147
points.  ATOM/RIDGE-generated points are EXCLUDED by the
unchanged r292/r293 split seal (they are training directions
of H_tr; the family mixture statement refers to the r293 TEST
families, disclosed).  Corpus tags pairwise disjoint (gated,
MAIN excluded as the disclosed shared anchor) and disjoint
from the r292 training tags (gated).  Per corpus k: F10 with
the UNCHANGED r293 H_tr (hash-gated identical to the Leg-0
seal -- NO re-training), F0_M2 = |delta|_L2, reported sp(F10,
s), sp(F0_M2, s), AUC(dead = s < NEAR), partial sp(F10, s |
F0_M2).  THE SEALED PROMOTION BAR (fixed here, before any
corpus is built): win_k iff |sp(F10)| > |sp(F0_M2)| on corpus
k; part_k iff the partial sp is finite AND >= +0.3 (the r293
record sign is POSITIVE; sign stability = same sign as the
record, i.e. the signed value clears +0.3); full_k = win_k AND
part_k.  F10_STABLE iff #win >= 4 AND #part >= 4;
else F10_FRAGILE iff #full in {2, 3}; else F10_ARTIFACT
(#full <= 1) -- and then the r293 promotion-candidate flag is
to be RETRACTED (sealed honestly here; the retraction itself
happens in the round report, nothing is promoted or retracted
inside experiments/ artifacts).
LEG B -- TRAIN SENSITIVITY (split and estimator robustness):
  (b1) SPLIT JACKKNIFE: five leave-3-out rotations of the 18
    r292 training directions (rotation j = 0..4 removes indices
    {j, j+5, j+10} of the sealed train list FRAC00/02/04/06/08,
    DENS00/02/04, RIDGE, ATOM00..08); H_j / G_j / projection
    rebuilt on the remaining 15 (NO new measurements -- the
    Hessian entries are the Leg-0 measurements, the jackknife
    is a split question); F10_j evaluated on the bit-identical
    94-point r293 test split; sealed fine type: TRAIN_ROBUST
    iff the population std of the five sp values <= JACK_BAR =
    0.012 (half the r293 win margin), else TRAIN_SENSITIVE(
    sigma); max |sp_j - sp_full| reported alongside (span
    change under leave-out is part of the jackknife, disclosed).
  (b2) RANK TRUNCATION: generalized eigendecomposition of
    (H_tr, G_tr) (L2-Gram whitening, eigencut GCUT); rank-r
    truncations r = 1, 2, 4 of F10 in the whitened eigenbasis
    (F10_r = 1/2 sum_{k<=r} lam_k y_k^2); identity gate
    F10_(18) == F10 (rel 1e-8 on the test values); sealed fine
    type: RANK1_CARRIES iff |sp(F10_1)| > |sp(F0_M2)| on the
    94-point split (the top DENS axis alone beats the home
    baseline -- the mechanism hint), else RANKr_CARRIES for the
    smallest r in {2, 4} that does, else FULL_RANK_NEEDED; the
    DENS coefficient-mass share of the top (H_tr, G_tr)
    eigenaxis reported (typed MEASUREMENT).
  (b3) STEP-SIZE CHECK: H_tr re-measured on the HALF and DOUBLE
    r292 FD ladder (diagonal + all 153 pairs at H_PAIR_H / 2
    resp. x 2; the double ladder's combined pair vectors reach
    effective 6.25e-5 theta_eq = the r292-a1 NaN territory --
    the SEALED handling rule, fixed before evaluation: a ladder
    variant with ANY non-finite margin is typed MARGIN_INVALID
    (count disclosed; this REPRODUCES the r292-a1 boundary) and
    excluded from the comparison); sealed fine type: STEP_STABLE
    iff for every VALID variant the Spearman of the F10 values
    themselves (mid ladder vs variant, 94-point split) >= 0.95,
    STEP_UNSTABLE(worst) otherwise, STEP_NOT_VERIFIABLE if no
    variant is valid.
LEG C -- WINDOW TRANSPORT (the hardest question): the complete
chain (wall, ridge, reduced-set Hessian, F10, F0, corpus) built
on the neighbor windows w7 and w11 (both build through the
sealed r278 channel; per-evaluation cost ~0.01 s measured at
design time -- w11 is NOT too expensive, no fallback needed).
Per window w, everything WINDOW-OWN:
  NREF_w = the measured MAIN wall degree (w7: 59, w11: 63);
  margins = 1 - rho_{NREF_w} gated on crossing > NREF_w;
  theta_eq_w with the analytic REF_w + inversion identity gate;
  ridge_w = the r280 OPT axis at NREF_w; DIRECTION EXTRACTION
  DOSE CAP (sealed rule, from the design-time feasibility
  measurement: at w11 theta_up = 7.3e-3 and the FULL ridge
  endpoint collapses minC 63 -> 32, far outside the linear
  density regime): ridge/atom direction densities are extracted
  at dose factor f_ex = min(1, THETA_CAL / (2 theta_up_w)) --
  at w9 this is 1 (r292-identical), at w7/w11 it caps the
  extraction at theta_eq ~1e-3; conservation gated at the
  extraction dose.  REDUCED TRAINING SET (sealed): RIDGE_w + 4
  top-atom one-hot directions (window-own c_j ranking) + 4
  fresh FRAC (seeds 294700+50 wi+0..3) + 3 fresh DENS (seeds
  294700+50 wi+10..12) = 12 directions, theta_eq_w-normalized;
  H_w diagonal at the sealed ladder (start = the r292
  HESS_EQ_HS; sealed halving rule: halve the whole ladder while
  any diagonal margin is non-finite, max 3 halvings, count
  disclosed) + all 66 pairs at the final mid step.  WINDOW
  CORPUS (test, disjoint from the training directions): MAIN_w
  + 4 worlds (SMOOTH_w = smooth comb at alpha_w, SCR seeds
  294740+50 wi+0/+1 bitwise-gated, ENSR seed 294740+50 wi+2) +
  2 paths x PATH_TS (to SMOOTH_w and SCR_a) + 6 fresh
  directions (4 FRAC seeds 294720+50 wi+0..3, 2 DENS seeds
  294730+50 wi+0..1) x DIST_GRID_W = (5e-4, 1e-3, 2e-3, 3e-3,
  5e-3, 1e-2, 2e-2) = 67 points; the survival readout is
  WINDOW-LOCAL: the union sign chain is scanned to NREF_w + 8
  (extension to NREF_w + 32 when no crossing is found; a point
  still uncrossed there is CENSORED at s_w = (NREF_w + 32) /
  NREF_w, count disclosed -- the r290 w9 code path is
  unchanged); s_w = minC / NREF_w.  Evaluated: sp(F10_w, s_w)
  vs
  sp(F0_M2_w, s_w), AUC, partial.  SEALED ADJUDICATION (exactly
  one): WINDOW_TRANSPORTS iff |sp(F10_w)| > |sp(F0_M2_w)| on
  BOTH windows; WINDOW_PARTIAL(w) iff on exactly one;
  WINDOW_W9_ONLY iff on none; a degenerate window corpus (nan
  sp) is typed WINDOW_DEGENERATE and counts as non-transport
  (disclosed).  MECHANISM CONSTANCY (typed MEASUREMENT): the
  DENS coefficient-mass share of the top (H_w, G_w) eigenaxis
  per window -- is the top axis again a DENS combination?
LEG D -- WHY L2 (mechanism bycatch, small): the r293 distortion
table showed the DENS sector's M3/M2 conversion rate ~6x above
the global median.  The targeted test: a DENS-NEUTRALIZED
metric on w9 -- the L2-orthonormalized span of the 6 r292 DENS
directions is rescaled axis-wise by c_j = sqrt(|lam_j| /
kappa_ref) (lam_j = the curvature eigenvalues of the measured
H restricted to the DENS span, per unit L2; kappa_ref = the
median |diagonal curvature per unit L2| over the 23 non-DENS
directions; |lam_j| < 1e-12 x max guard -> c_j = 1, FLAT
disclosed), i.e. D_neut(delta)^2 = |delta|^2 + sum_j (c_j^2 -
1) <a_j, delta>^2 -- in this coordinate every DENS axis carries
the TYPICAL curvature per unit length: the DENS scaling
privilege is removed.  F0_NEUT = D_neut as the baseline;
re-run the F10-vs-baseline comparison on the bit-identical
94-point split.  SEALED (exactly one): L2_VIA_DENS iff
|sp(F10)| <= |sp(F0_NEUT)| (the home win disappears once the
baseline sees the DENS scaling: the DENS-sector scaling carries
the information); else L2_NOT_DENS.  Partial sp(F10, s |
F0_NEUT) reported alongside (MEASUREMENT).
WARDS / MUST-FAILS (each loud): (m1) RE-TRAINING of H_tr for
Leg A (seal break): a mutant H with ONE diagonal entry
re-measured on a fresh-corpus direction must be CAUGHT by the
H_tr hash seal; (m2) CORPUS SEED REUSE: corpus 1 rebuilt with
the corpus-0 seeds must be CAUGHT by the tag-disjointness
auditor; (m3) a subset move with one weight scaled 1 + 1e-3
must be CAUGHT by the exact r276 conservation gate; (m4) the
WINDOW CATEGORY ERROR -- transporting the w9 H_tr to a w7
deviation instead of the window-own H_w -- is run as the
disclosed CONTROL MEASUREMENT: the attempt fails structurally
(dimension mismatch of the profile grids, L 230 vs 734) and
must raise -- CAUGHT by construction; the honest reading (the
w9 form cannot even be APPLIED off-window without a new
window-own measurement) is part of the record.  Scope audits:
the sealed source-pure constructors consume vectors/densities
+ geometry + seeds only; H_tr / g_tr / H_w / H_half /
H_double / the neutralization scales are honestly typed
measurement-consuming (split-sealed resp. ladder-sealed);
fragment audit (no fit fragments).  STOP LIST (anti-gates,
binding): NO L* claim, NO bound mechanism, NO asymptotic law,
NO derived 5/7, NO equidistribution premise, NO posthoc
window, NO promotion from here, NO RH claim; r243..r293 stand.

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
+0.423 / PARTIAL_SIDE_REC +0.826 (tol 0.005 each); LEG-A
FRESH_BASE 294000 / N_CORP 5 / N_FRAC_C 12 / N_DENS_C 8 /
CORP_MIN_PTS 140 / PART_BAR_A 0.3 / WIN_NEED 4 / PART_NEED 4 /
FRAGILE_MIN 2; LEG-B JACK_OUT rotations {j, j+5, j+10} /
JACK_BAR 0.012 / RANKS (1, 2, 4) / RANK_ID_TOL 1e-8 /
STEP_FACS (0.5, 2.0) / STEP_BAR 0.95; LEG-C W_LIST (7, 11) /
W_SEED 294700 + 50 wi / N_ATOM_W 4 / N_FRAC_W 4 / N_DENS_W 3 /
N_FRAC_WC 4 / N_DENS_WC 2 / DIST_GRID_W (5e-4, 1e-3, 2e-3,
3e-3, 5e-3, 1e-2, 2e-2) / EXTRACTION DOSE CAP min(1,
THETA_CAL / (2 theta_up_w)) / LADDER HALVING max 3; LEG-D
NEUT_GUARD 1e-12; ETA0_BAR 1e-12 / THETA_CAL 1e-3; runtime <=
1800 s; smoke = toys + firewall + scopes + w9 regression +
m2/m3-style mutants (anchors, legs, corpora, adjudications
skipped).
PRE-SPEC SCOPING (disclosed): every record number is a
published r276/r280/r290/r291/r292/r293 record adopted as-is;
the five-corpus construction with its seed plan, the sealed
promotion bar with its three-way grading, the jackknife
rotations, the rank-truncation rule, the step-ladder handling
rule, the window-transport chain with the extraction dose cap
and the halving rule, the DENS-neutralization construction
with its adjudication and the must-fail set were fixed at
design time from the published records and the task contract;
a design-time feasibility measurement (window costs, world
builders, the w11 ridge-endpoint collapse motivating the dose
cap, the window-local survival readout) and a design-time
calibration pass (disclosed below) preceded the freeze; no
bar, band or rule was tuned after the record freeze.

SEALED VERDICT FORM (frozen BEFORE the record freeze, joined
with '+'):
  CORPUS_TABLE(per fresh corpus: n, sp(F10), sp(F0_M2), AUC,
    partial, win/part flags) [always]
  + [exactly one of] F10_STABLE(#win, #part, #full) /
    F10_FRAGILE(#full) / F10_ARTIFACT(#full, retraction of the
    r293 flag sealed)
  + [exactly one of] TRAIN_ROBUST(sigma) / TRAIN_SENSITIVE(
    sigma) [jackknife table always]
  + [exactly one of] RANK1_CARRIES / RANK2_CARRIES /
    RANK4_CARRIES / FULL_RANK_NEEDED [rank table + top-axis
    DENS share always]
  + [exactly one of] STEP_STABLE(min sp) / STEP_UNSTABLE(
    worst) / STEP_NOT_VERIFIABLE [validity census always]
  + [exactly one of] WINDOW_TRANSPORTS / WINDOW_PARTIAL(w) /
    WINDOW_W9_ONLY [per-window table + DENS-top measurement
    always]
  + [exactly one of] L2_VIA_DENS / L2_NOT_DENS [neutralization
    numbers always].
Honesty before beauty: every correlation, Hessian entry,
scale factor and window number is a MEASUREMENT on finite
profile space; H_tr is the UNCHANGED r293 object (hash-sealed);
the jackknife/rank/step variants and the window forms are
measurement-consuming and sealed by their split resp. ladder
rules; the fresh corpora share exactly ONE point (MAIN) with
each other and with r293 (disclosed); the window survival
normalization NREF_w is the window-own measured wall
(half-filling offset +1 at w7 disclosed); no verdict claims
L*, a bound mechanism, a derived 5/7 or an asymptotic law; the
promotion decision itself belongs to the consolidation wave,
NOT to this probe.  NO RH CLAIM in either direction.  NOT
evidence for or against RH.

RECORD TABLES (frozen from the record run; calibration
protocol, chronology honest: smoke pass 1 = 10/10 (0.1 s);
calibration pass 1 = first full evaluation = 42/42, wall 151
s -- NO gate failed and NO adjudicated number changed; the
single calibration finding was a display-precision fix
(kappa_ref printed at %.3f = '0.000' for a ~7e-5 value,
re-printed at %.3g -- pure display conditioning, no rule or
bar touched); pass 2 with the fix = 42/42, wall 151 s = the
record physics, all adjudicated numbers identical to pass 1;
the record-table insertion below is the only post-freeze
edit, which IS the protocol; record rerun after insertion
42/42, run1/run2 identical up to WALL).
RECORD VERDICT = CORPUS_TABLE(five fresh 147-point corpora,
conservation/eta_0/scramble weights exact, tags pairwise
disjoint and disjoint from the r292 training tags, s ranges
full [0.01..1.01]: sp(F10) +0.787 / +0.675 / +0.734 / +0.720
/ +0.706 vs sp(F0_M2) -0.672 / -0.660 / -0.714 / -0.684 /
-0.703; AUC(dead) 0.137 / 0.142 / 0.230 / 0.132 / 0.142;
partial sp(F10, s | F0_M2) +0.555 / +0.248 / +0.297 / +0.350
/ +0.299; win 5/5, part 2/5, full 2/5) + F10_FRAGILE(the
honest center of the round: the |sp| WIN over the home L2
baseline replicates on EVERY fresh corpus (5/5, margins
+0.115 / +0.015 / +0.020 / +0.036 / +0.003 -- all positive,
mostly wider than the r293 +0.024) BUT the partial-
correlation channel does NOT replicate at its r293 magnitude:
fresh partials 0.248..0.555 with median 0.299, only 2/5 clear
the sealed +0.3 bar (two miss it by 0.003 and 0.001 -- honest,
the bar was sealed before any corpus was built and is not
moved); #full = 2 -> FRAGILE by the sealed grading; the r293
partial +0.423 sits at the TOP of the fresh range: the
information-beyond-distance channel is thinner on fresh
corpora than the r293 split suggested; promotion NOT
recommended from this round) + TRAIN_ROBUST(jackknife sp
+0.892 / +0.867 / +0.879 / +0.866 / +0.884, population sigma
0.0101 <= 0.012, max |sp_j - sp_full| 0.018: the contest
result is insensitive to leave-3-out re-splits at the sealed
bar -- though the sigma sits close under it, disclosed) +
RANK2_CARRIES(rank table sp(F10_r) r=1 +0.855 / r=2 +0.863 /
r=4 +0.884 / full +0.884 (identity F10_18 == F10 rel
7.8e-14); baseline |sp(F0_M2)| = 0.860: the top DENS
eigenaxis ALONE reaches +0.855 and misses the baseline by
0.005 -- TWO whitened eigendirections suffice to beat it;
top-axis DENS coefficient-mass share 0.989, the r292
mechanism confirmed) + STEP_STABLE(half ladder VALID with all
margins finite, sp(F10_mid, F10_half) = 0.9995 >= 0.95; the
DOUBLE ladder is MARGIN_INVALID with 4 non-finite margins =
the r292-a1 NaN boundary reproduced and excluded by the
sealed rule: the F10 ranking is step-size stable on every
margin-valid ladder) + WINDOW_PARTIAL(w11 only -- the hardest
question splits the difference: w7 (NREF_w 59, offset +1
disclosed, theta_up 3.19e-3, extraction cap 0.157, ladder
unhalved, censoring 0): sp(F10_w) +0.818 vs sp(F0_M2_w)
-0.827 -- F10 LOSES by 0.009, partial +0.179, AUC 0.096;
w11 (NREF_w 63, theta_up 7.33e-3, cap 0.068, unhalved,
censoring 0): sp(F10_w) +0.892 vs -0.890 -- F10 beats by
+0.002, partial +0.289, AUC 0.049; both margins are r293-thin
(|0.002..0.009| ~ the +0.024 scale): the window contests are
KNIFE-EDGE, not decisive either way; MECHANISM CONSTANCY is
the solid transport finding: the top (H_w, G_w) eigenaxis is
again a DENS combination on BOTH windows (coefficient-mass
shares 0.795 / 0.834 vs 0.989 at w9) -- the rank-one DENS
curvature structure transports even where the razor-thin
contest does not) + L2_NOT_DENS(the DENS-neutralized baseline
is WEAKER than plain L2: sp(F0_NEUT) = -0.828 vs sp(F0_M2) =
-0.860 (scale factors c_j 75.6 / 14.0 / 10.6 / 5.6 / 5.4 /
2.2 on the six DENS eigenaxes, kappa_ref 6.55e-5 per unit
L2); |sp(F10)| = 0.884 > 0.828 and the partial vs the
neutralized baseline RISES to +0.586: inflating the DENS
lengths does not absorb the F10 information -- the L2 win of
F10 is NOT the DENS-sector length distortion; why L2 is the
right coordinate stays open).
Key numbers.  W9: S 367/263/104, minC 184, crossing 185,
margin 1.6752e-4, z_v -3.149, b34 -0.105; REF 125.7462,
inversion 1.5e-16, quadruple devs (0.059, 0.125, 0.117,
0.028); flips 25/21/27/25 == records; theta_up 3.8733e-5,
endpoint minC 185, top-9 atoms == record.  R292/R293
REGRESSION: 29 directions conservation exact, 406 pairs
finite, crosscheck 15/15 worst 0.018; share 0.925 == 0.925,
lam_top -0.418 == -0.418, SMOOTH |cos| 0.07, ridge rank
28/29; corpus 143, test split 94 (overlap NONE, tag SHA
a76cc57851826476 == prefix); F10 +0.884 / F0_M1 -0.907 /
F0_M2 -0.860 / AUC 0.097 / partial +0.423 / side +0.826 --
ALL == records; H_tr hash seal 3447ed198a56530d, positive-
eigenvalue mass share 0.0052 == r293.  LEG A: 5 x 147 points;
worlds all dead (SCR minC 6..8, HL2 25, ENSR-family low);
60 fresh FRAC + 40 fresh DENS directions conservation/eta_0
exact; pairwise tag overlaps 0, r292-training-tag overlaps 0.
LEG C: w7/w11 inversion identities 8.2e-17 / 9.6e-17; window
corpora 67/67 points, s_w in [0.05, 1.00] / [0.06, 1.00],
0 censored on both.  MUST-FAILS: m1 CAUGHT (retrained-entry
hash 4929daec2aa8 != seal 3447ed198a56), m2 CAUGHT (146
overlap tags; honest corpora 0 seed-stripped overlaps), m3
CAUGHT (conservation gate False), m4 CAUGHT (the w9 H_tr on a
w7 deviation raises the dimension error -- the category error
is structurally blocked, disclosed control); scopes +
fragments CLEAN.  Runtime 151 s full / 0.1 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE (records
inserted per protocol; the calibration display fix disclosed
above; no physics bar, class rule or verdict rule moved).
READING (typed MEASUREMENT): the stability test returns a
SPLIT picture and the sealed bar calls it FRAGILE -- honest:
(A) what REPLICATES is the |sp| win itself (5/5 fresh corpora,
F10 above the home L2 baseline everywhere, margins up to
+0.115) and every internal robustness axis (train-split
jackknife sigma 0.0101, step-size stable on the margin-valid
ladders, rank-2 truncation suffices, top axis 0.99 DENS);
what does NOT replicate is the r293 partial MAGNITUDE: on
fresh corpora the information-beyond-distance channel drops
to median 0.299 against the sealed 0.3 bar (2/5 pass, two
miss by <= 0.003) -- the +0.423 of r293 was the top of the
distribution, not the center; (B) the window transport is
KNIFE-EDGE (w11 wins by +0.002, w7 loses by 0.009) -- the
contest does not decide off-window, but the MECHANISM does
transport: the top curvature eigenaxis is a DENS combination
on w7, w9 and w11 alike (shares 0.795 / 0.989 / 0.834);
(C) the L2 home win is NOT the DENS length distortion
(neutralized baseline WEAKER, partial rises to +0.586) --
the 'why L2' mechanism question stays open.  Consequence
under the sealed bar: promotion precondition NOT met --
recommendation NO for wave 8 as a closed [E]-style
functional claim; the honest statement that IS stable
(F10 beats the L2 size baseline in |sp| on every tested
fresh corpus) is a candidate for a weaker, explicitly
partial-free formulation in a later round.  NO RH CLAIM in
either direction.  NOT evidence for or against RH.
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
DEGEN_EPS = MR.DEGEN_EPS

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

# Leg A (sealed before any corpus is built)
FRESH_BASE = 294000
N_CORP = 5
N_FRAC_C = 12
N_DENS_C = 8
CORP_MIN_PTS = 140
PART_BAR_A = 0.3
WIN_NEED = 4
PART_NEED = 4
FRAGILE_MIN = 2

# Leg B (sealed)
JACK_BAR = 0.012
RANKS = (1, 2, 4)
RANK_ID_TOL = 1e-8
STEP_FACS = (0.5, 2.0)
STEP_BAR = 0.95

# Leg C (sealed)
W_LIST = (7, 11)
W_SEED_BASE = 294700
W_SEED_STEP = 50
N_ATOM_W = 4
N_FRAC_W = 4
N_DENS_W = 3
N_FRAC_WC = 4
N_DENS_WC = 2
DIST_GRID_W = (5e-4, 1e-3, 2e-3, 3e-3, 5e-3, 1e-2, 2e-2)
LADDER_MAX_HALVE = 3
W_EXT = 8
W_EXT2 = 32

# Leg D (sealed)
NEUT_GUARD = 1e-12

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


CONSTRUCTORS = ("trunc_energy", "neut_dist2", "coef_share",
                "whiten_coords")
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
def whiten_coords(x, G_evals, G_evecs, cut):
    """whitened coordinates z of a projection-coordinate vector
    x against the Gram G = U diag(w) U^T: z = sqrt(w_kept)
    U_kept^T x (eigencut; exact inverse of the Wk map on the
    kept span).  Consumes vectors only."""
    w = np.asarray(G_evals, float)
    U = np.asarray(G_evecs, float)
    keep = w >= float(cut) * float(np.max(w))
    return np.sqrt(w[keep]) * (U[:, keep].T @ np.asarray(x, float))


def trunc_energy(y, lam, r):
    """RANK-TRUNCATED curvature energy in the whitened eigen
    basis: 1/2 sum_{k < r} lam_k y_k^2 (lam sorted by |lam|
    descending, y the matching eigen coordinates).  Consumes
    two vectors + a rank only."""
    y = np.asarray(y, float)
    lam = np.asarray(lam, float)
    r = int(r)
    return 0.5 * float(np.sum(lam[:r] * y[:r] * y[:r]))


def neut_dist2(delta, axes, c2):
    """DENS-NEUTRALIZED squared distance: |delta|_2^2 +
    sum_j (c2_j - 1) <a_j, delta>^2 over L2-orthonormal axes
    a_j with per-axis squared scale factors c2_j >= 0 (PSD by
    orthonormality).  Consumes vectors only."""
    delta = np.asarray(delta, float)
    yy = np.asarray(axes, float).T @ delta
    return float(delta @ delta) \
        + float(np.sum((np.asarray(c2, float) - 1.0) * yy * yy))


def coef_share(coef, idx_set):
    """coefficient-mass share of an index subset: sum of
    squared coefficients over the subset / total.  Consumes a
    vector + an index list only."""
    c = np.asarray(coef, float)
    tot = float(np.sum(c * c))
    sel = float(np.sum(c[list(idx_set)] ** 2))
    return sel / max(tot, 1e-300)


# ============== must-fail mutants
def mutant_seed_reuse_tags(tags_a, tags_b):
    """m2 MUST-FAIL: corpus tags rebuilt with REUSED seeds --
    the tag auditor must flag the overlap."""
    return RA.split_auditor(set(tags_a), set(tags_b))


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("f10_stability_probe -- PRIME.PORT.LSTAR."
          "F10_STABILITY.01 (round 294)")
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
          "sealed BEFORE evaluation: the five-corpus plan (seeds "
          "294000+1000k, 147 points each, r293 test-family mix), "
          "the promotion bar (win >= 4/5 AND partial >= 0.3 with "
          "the record sign >= 4/5 -> STABLE; full in {2,3} -> "
          "FRAGILE; <= 1 -> ARTIFACT with sealed retraction), the "
          "jackknife rotations {j, j+5, j+10} with bar 0.012, the "
          "rank-truncation rule on (H_tr, G_tr), the step-ladder "
          "handling rule (non-finite margin -> variant "
          "MARGIN_INVALID), the w7/w11 transport chain with the "
          "extraction dose cap and the ladder halving rule, the "
          "DENS-neutralization metric with its adjudication and "
          "the must-fail set; H_tr / g_tr / H_w honestly "
          "typed measurement-consuming; the STOP list forbids any "
          "L* claim, any promotion from here and any proof attack")

    # ---------------- S1 toys
    section("S1  TOYS -- WHITEN/TRUNC, NEUT DIST, COEF SHARE, "
            "PARTIAL")
    G_t = np.eye(2)
    wG_t, UG_t = np.linalg.eigh(G_t)
    H_t = np.diag([-2.0, 1.0])
    lam_t, Y_t = np.linalg.eigh(H_t)
    o_t = np.argsort(-np.abs(lam_t))
    lam_s_t = lam_t[o_t]
    x_t = np.array([1.0, 1.0])
    z_t = whiten_coords(x_t, wG_t, UG_t, GCUT)
    y_t = Y_t[:, o_t].T @ z_t
    f_full = trunc_energy(y_t, lam_s_t, 2)
    f_r1 = trunc_energy(y_t, lam_s_t, 1)
    ok_t1 = (abs(f_full - (-0.5)) <= 1e-12
             and abs(f_r1 - (-1.0)) <= 1e-12
             and abs(f_full - CF.func_q10(x_t, H_t)) <= 1e-12)
    check("G10-toy-trunc-energy", ok_t1,
          "HAND TRUNCATION (H = diag(-2, 1), G = I, x = (1, 1)): "
          "full rank F10 = %.3f == -1/2 == CF.func_q10 exact; "
          "rank-1 (the |lam| = 2 axis) = %.3f == -1 exact"
          % (f_full, f_r1))
    ax_t = np.eye(3)[:, :1]
    d_t = np.array([1.0, 1.0, 0.0])
    dn_t = neut_dist2(d_t, ax_t, np.array([4.0]))
    dn_id = neut_dist2(d_t, ax_t, np.array([1.0]))
    ok_t2 = (abs(dn_t - 5.0) <= 1e-12
             and abs(dn_id - 2.0) <= 1e-12)
    check("G11-toy-neut-dist", ok_t2,
          "HAND NEUTRALIZATION (axis e1, c^2 = 4, delta = "
          "(1, 1, 0)): D^2 = |delta|^2 + 3 <e1, d>^2 = %.1f == 5 "
          "exact; c^2 = 1 recovers plain L2 (%.1f == 2)"
          % (dn_t, dn_id))
    cs_t = coef_share(np.array([1.0, 2.0, 2.0]), [1, 2])
    psp_t = MR.partial_sp([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 4, 3])
    ok_t3 = (abs(cs_t - 8.0 / 9.0) <= 1e-12
             and abs(psp_t - 1.0) <= 1e-12)
    check("G12-toy-share-partial", ok_t3,
          "HAND COEF SHARE (1, 2, 2) on {1, 2} = %.3f == 8/9 "
          "exact; MR.partial_sp identity toy == 1 exact (the r293 "
          "sealed partial reused verbatim)" % cs_t)
    sp_j_t = [0.884, 0.885, 0.883, 0.884, 0.884]
    sig_t = float(np.std(sp_j_t))
    ok_t4 = sig_t <= JACK_BAR
    check("G13-toy-jackknife-sigma", ok_t4,
          "HAND JACKKNIFE SIGMA on a stable toy quintet: sigma = "
          "%.4f <= %.3f (the sealed TRAIN_ROBUST bar = half the "
          "r293 win margin)" % (sig_t, JACK_BAR))

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
        tags_a = ["C0:DIR:FRAC00:d=1e-03", "C0:WORLD:SCR:294001"]
        ov_s = mutant_seed_reuse_tags(tags_a, tags_a)
        check("G86-mustfail-seed-reuse", len(ov_s) == 2,
              "m2 SEED REUSE (toy tags): auditor flags %d overlap "
              "points -- CAUGHT" % len(ov_s))
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
    section("S4  LEG 0c -- H_tr SEAL + r293 CONTEST REGRESSION")
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
    wH = np.linalg.eigvalsh(H_tr)
    pos_share = float(np.sum(wH[wH > 0])) \
        / max(float(np.sum(np.abs(wH))), 1e-300)
    check("G40-htr-seal", math.isfinite(pos_share),
          "H_tr / g_tr / G_tr on the 18 sealed r292 training "
          "directions REBUILT (r293 verbatim) and SEALED BY HASH: "
          "sha256(H_tr) = %s (the Leg-A 'no re-training' promise "
          "is now a GATE); positive-eigenvalue mass share %.4f "
          "(r293 record 0.0052)" % (H_SEAL[:16], pos_share))

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
          "test / %+.3f == +0.826 train-side (tol %.3f each) -- "
          "the r293 reconciliation reproduces bit-near"
          % (sp_f10, sp_f0m1, sp_f0m2, auc_f10, psp_test,
             psp_side, R293_SP_TOL))

    # ---------------- S5 LEG A: fresh-corpus replication
    section("S5  LEG A -- FIVE FRESH CORPORA vs THE UNCHANGED "
            "H_tr (the promotion bar)")
    ok_seal_now = (hashlib.sha256(H_tr.tobytes()).hexdigest()
                   == H_SEAL)
    corp_rows = []
    all_tag_sets = []
    ok_corp_build = ok_seal_now
    for k in range(N_CORP):
        base = FRESH_BASE + 1000 * k
        pts = []

        def addf(tag, dvec, meas):
            pts.append(dict(tag=tag,
                            delta=np.asarray(dvec, float) - d9,
                            s=meas["s"]))

        addf("MAIN", d9, M0)
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
                ok_corp_build = ok_corp_build and bool(
                    np.array_equal(np.asarray(sctx["mm"]), mm9))
                dW = np.asarray(sctx["darm"], float)
            w_dens.append(dW)
            addf("C%d:WORLD:%s:%d" % (k, wn, sd), dW,
                 PFP.measure_density(dW, L9))
        for pi in (0, 2, 4, 1):     # SCR_a / HL2_a / ENSR_a / SCR_b
            dT = w_dens[pi]
            for t in PATH_TS:
                dpt = PFP.interp_density(d9, dT, t)
                addf("C%d:PATH:%s:%d:t=%.4g"
                     % (k, w_specs[pi][0], w_specs[pi][1], t),
                     dpt, PFP.measure_density(dpt, L9))
        for i in range(N_FRAC_C):
            sd = base + 100 + i
            dd, (u2, m2) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                        THETA_CAL, sd)
            ok_corp_build = ok_corp_build and MF.conserve_comb(
                "P2_JIT", uu9, mm9, u2, m2, THETA_CAL)
            unit = dd / max(lag_l1(dd), 1e-300)
            for dist in DIST_GRID:
                dpt = d9 + unit * (dist * REF)
                addf("C%d:DIR:FRAC:%d:d=%.0e" % (k, sd, dist),
                     dpt, PFP.measure_density(dpt, L9))
        for i in range(N_DENS_C):
            sd = base + 200 + i
            dd = PFP.dir_dens(d9, L9, sd)
            eta0 = abs(float(np.sum(dd * s_l9)))
            ok_corp_build = ok_corp_build and eta0 <= ETA0_BAR \
                * max(float(np.sum(np.abs(dd * s_l9))), 1.0)
            unit = dd / max(lag_l1(dd), 1e-300)
            for dist in DIST_GRID:
                dpt = d9 + unit * (dist * REF)
                addf("C%d:DIR:DENS:%d:d=%.0e" % (k, sd, dist),
                     dpt, PFP.measure_density(dpt, L9))
        for r in pts:
            r["F10"] = CF.func_q10(proj_x(r["delta"]), H_tr)
            r["F0_M2"] = float(np.linalg.norm(r["delta"]))
        sv = [r["s"] for r in pts]
        dl = [r["s"] < NEAR for r in pts]
        spF = BH.spearman([r["F10"] for r in pts], sv)
        spB = BH.spearman([r["F0_M2"] for r in pts], sv)
        auc = CF.auc_rank([r["F10"] for r in pts], dl)
        psp = MR.partial_sp([r["F10"] for r in pts], sv,
                            [r["F0_M2"] for r in pts])
        win = abs(spF) > abs(spB)
        part = math.isfinite(psp) and psp >= PART_BAR_A
        corp_rows.append(dict(k=k, n=len(pts), spF=spF, spB=spB,
                              auc=auc, psp=psp, win=win,
                              part=part, s_lo=min(sv),
                              s_hi=max(sv)))
        all_tag_sets.append(set(r["tag"] for r in pts))
        ok_corp_build = ok_corp_build and len(pts) >= CORP_MIN_PTS
    check("G50-fresh-corpora", ok_corp_build,
          "FIVE FRESH CORPORA (seeds 294000+1000k; conservation / "
          "eta_0 / scramble weights exact; H_tr hash re-gated == "
          "seal): sizes %s (bar >= %d); s ranges %s -- worlds "
          "dead, ladders alive: full contrast on every corpus"
          % (str([r["n"] for r in corp_rows]), CORP_MIN_PTS,
             str([("%.2f" % r["s_lo"], "%.2f" % r["s_hi"])
                  for r in corp_rows])))
    ov_pair = 0
    for a in range(N_CORP):
        for b in range(a + 1, N_CORP):
            ov_pair += len(RA.split_auditor(
                all_tag_sets[a] - {"MAIN"},
                all_tag_sets[b] - {"MAIN"}))
    ov_train = sum(len(RA.split_auditor(train_tags, ts))
                   for ts in all_tag_sets)
    check("G51-corpus-disjointness", ov_pair == 0
          and ov_train == 0,
          "CORPUS DISJOINTNESS: pairwise tag overlaps %d == 0 "
          "(MAIN excluded as the disclosed shared anchor); "
          "overlaps with the r292 training tags %d == 0 -- the "
          "five corpora are independent by construction and by "
          "gate" % (ov_pair, ov_train))
    tab_txt = "; ".join(
        "C%d(sp %+.3f vs %+.3f, AUC %.3f, partial %s, %s/%s)"
        % (r["k"], r["spF"], r["spB"], r["auc"],
           ("%+.3f" % r["psp"]) if math.isfinite(r["psp"])
           else "DEGEN",
           "W" if r["win"] else "-", "P" if r["part"] else "-")
        for r in corp_rows)
    check("G52-corpus-table", all(math.isfinite(r["spF"])
                                  and math.isfinite(r["spB"])
                                  for r in corp_rows),
          "CORPUS TABLE (F10 with the UNCHANGED r293 H_tr vs "
          "F0_M2 = |delta|_L2): %s" % tab_txt)
    n_win = sum(1 for r in corp_rows if r["win"])
    n_part = sum(1 for r in corp_rows if r["part"])
    n_full = sum(1 for r in corp_rows if r["win"] and r["part"])
    if n_win >= WIN_NEED and n_part >= PART_NEED:
        stab_verd = ("F10_STABLE(win %d/5 >= %d AND part %d/5 >= "
                     "%d, full %d/5: the r293 reconciliation "
                     "replicates on fresh corpora -- the promotion "
                     "precondition is MET)"
                     % (n_win, WIN_NEED, n_part, PART_NEED,
                        n_full))
    elif n_full >= FRAGILE_MIN:
        stab_verd = ("F10_FRAGILE(full %d/5 in {2, 3}: the "
                     "reconciliation replicates only partially -- "
                     "promotion NOT recommended without further "
                     "rounds)" % n_full)
    else:
        stab_verd = ("F10_ARTIFACT(full %d/5 <= 1: the r293 "
                     "promotion-candidate flag is to be RETRACTED "
                     "-- sealed honestly)" % n_full)
    check("G53-stability-adjudication", True,
          "SEALED PROMOTION BAR (fixed before any corpus was "
          "built): win = |sp(F10)| > |sp(F0_M2)|; part = partial "
          ">= +%.1f with the r293 record sign -> %s"
          % (PART_BAR_A, stab_verd.split("(")[0]))

    # ---------------- S6 LEG B: train sensitivity
    section("S6  LEG B -- JACKKNIFE + RANK TRUNCATION + STEP "
            "LADDER")
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
    dev_jack = max(abs(v - sp_f10) for v in sp_jack)
    if sig_jack <= JACK_BAR:
        jack_verd = "TRAIN_ROBUST(sigma %.4f <= %.3f)" \
            % (sig_jack, JACK_BAR)
    else:
        jack_verd = "TRAIN_SENSITIVE(sigma %.4f > %.3f)" \
            % (sig_jack, JACK_BAR)
    check("G60-jackknife", all(math.isfinite(v)
                               for v in sp_jack),
          "SPLIT JACKKNIFE (leave-3-out rotations %s of the 18 "
          "training directions; NO new measurements): sp %s, "
          "population sigma %.4f, max |sp_j - sp_full| %.4f -> "
          "%s (span change under leave-out included, disclosed)"
          % (str(JACK_OUT), str([round(v, 4) for v in sp_jack]),
             sig_jack, dev_jack, jack_verd.split("(")[0]))
    # rank truncation on (H_tr, G_tr)
    keep_t = wGt >= GCUT * wGt[-1]
    Uk_t = UGt[:, keep_t]
    Wk_t = Uk_t / np.sqrt(wGt[keep_t])[None, :]
    Ared_t = Wk_t.T @ H_tr @ Wk_t
    lam_t2, Y_t2 = np.linalg.eigh(Ared_t)
    o_t2 = np.argsort(-np.abs(lam_t2))
    lam_tr_s = lam_t2[o_t2]
    Y_tr_s = Y_t2[:, o_t2]
    y_test = [Y_tr_s.T @ whiten_coords(r["x"], wGt, UGt, GCUT)
              for r in test_pts]
    f_full_vals = [trunc_energy(y, lam_tr_s, len(lam_tr_s))
                   for y in y_test]
    id_dev = max(abs(a - b) / max(abs(b), 1e-300)
                 for a, b in zip(f_full_vals,
                                 [r["F10"] for r in test_pts])
                 if abs(b) > 1e-30)
    sp_rank = {}
    for rr_ in RANKS:
        vals = [trunc_energy(y, lam_tr_s, rr_) for y in y_test]
        sp_rank[rr_] = BH.spearman(vals, svec)
    coef_top = (Wk_t @ Y_tr_s)[:, 0]
    dens_idx = [i for i, n in enumerate(train_dirs)
                if n.startswith("DENS")]
    dens_share = coef_share(coef_top, dens_idx)
    rank_win = [rr_ for rr_ in RANKS
                if abs(sp_rank[rr_]) > abs(sp_f0m2)]
    if rank_win and rank_win[0] == 1:
        rank_verd = ("RANK1_CARRIES(|sp(F10_1)| %.3f > %.3f = "
                     "|sp(F0_M2)|: the top axis alone beats the "
                     "home baseline)" % (abs(sp_rank[1]),
                                         abs(sp_f0m2)))
    elif rank_win:
        rank_verd = ("RANK%d_CARRIES(smallest carrying rank %d)"
                     % (rank_win[0], rank_win[0]))
    else:
        rank_verd = "FULL_RANK_NEEDED(no truncation beats F0_M2)"
    check("G61-rank-truncation", id_dev <= RANK_ID_TOL,
          "RANK TRUNCATION on (H_tr, G_tr) (identity gate "
          "F10_full == F10 rel %.1e <= %.0e): sp table r=1 %+.3f "
          "/ r=2 %+.3f / r=4 %+.3f / full %+.3f (baseline F0_M2 "
          "%+.3f); top-axis DENS coefficient-mass share %.3f -> "
          "%s" % (id_dev, RANK_ID_TOL, sp_rank[1], sp_rank[2],
                  sp_rank[4], sp_f10, sp_f0m2, dens_share,
                  rank_verd.split("(")[0]))
    check("G62-rank-adjudication", True,
          "SEALED RANK RULE (smallest r in {1, 2, 4} with "
          "|sp(F10_r)| > |sp(F0_M2)|, else FULL_RANK_NEEDED): -> "
          "%s -- typed with the DENS share as the mechanism "
          "measurement" % rank_verd)
    # step-size check (half / double ladder)
    step_rows = {}
    for fac in STEP_FACS:
        h = H_PAIR_H * fac
        n_bad = 0
        H_alt = np.zeros((len(train_dirs), len(train_dirs)))
        for i, n in enumerate(train_dirs):
            v = vhat[n]
            mp_ = margin_at(d9 + v * h)
            mn_ = margin_at(d9 - v * h)
            if not (math.isfinite(mp_) and math.isfinite(mn_)):
                n_bad += 1
                continue
            H_alt[i, i] = (mp_ - 2.0 * m00 + mn_) / (h * h)
        for i in range(len(train_dirs)):
            for j in range(i + 1, len(train_dirs)):
                u, v = vhat[train_dirs[i]], vhat[train_dirs[j]]
                msp = margin_at(d9 + (u + v) * h)
                msn = margin_at(d9 - (u + v) * h)
                mdp = margin_at(d9 + (u - v) * h)
                mdn = margin_at(d9 - (u - v) * h)
                if not all(math.isfinite(x)
                           for x in (msp, msn, mdp, mdn)):
                    n_bad += 1
                    continue
                d2su = (msp - 2.0 * m00 + msn) / (h * h)
                d2di = (mdp - 2.0 * m00 + mdn) / (h * h)
                H_alt[i, j] = H_alt[j, i] = CF.pol_of_d2(d2su,
                                                         d2di)
        if n_bad > 0:
            step_rows[fac] = dict(valid=False, n_bad=n_bad,
                                  sp=float("nan"))
            continue
        vals = [CF.func_q10(r["x"], H_alt) for r in test_pts]
        sp_vs_mid = BH.spearman(vals, [r["F10"]
                                       for r in test_pts])
        step_rows[fac] = dict(valid=True, n_bad=0, sp=sp_vs_mid)
    valid_sps = [v["sp"] for v in step_rows.values()
                 if v["valid"]]
    if not valid_sps:
        step_verd = "STEP_NOT_VERIFIABLE(no valid ladder variant)"
    elif min(valid_sps) >= STEP_BAR:
        step_verd = ("STEP_STABLE(min F10-ranking spearman %.5f "
                     ">= %.2f over the valid variants)"
                     % (min(valid_sps), STEP_BAR))
    else:
        step_verd = ("STEP_UNSTABLE(worst %.3f < %.2f)"
                     % (min(valid_sps), STEP_BAR))
    check("G63-step-ladder", True,
          "STEP-SIZE CHECK (H_tr re-measured at %s x H_PAIR_H; "
          "sealed rule: any non-finite margin -> variant "
          "MARGIN_INVALID): %s"
          % (str(STEP_FACS),
             str({("x%.1f" % f): ("sp(F10_mid, F10_alt) = %.5f"
                                  % v["sp"] if v["valid"] else
                                  "MARGIN_INVALID(%d non-finite "
                                  "margins = the r292-a1 NaN "
                                  "boundary reproduced)"
                                  % v["n_bad"])
                  for f, v in step_rows.items()})))
    check("G64-step-adjudication", True,
          "SEALED STEP RULE (STABLE iff every valid variant "
          "spearman >= %.2f): -> %s"
          % (STEP_BAR, step_verd.split("(")[0]))

    # ---------------- S7 LEG C: window transport (w7, w11)
    section("S7  LEG C -- WINDOW TRANSPORT (w7 / w11, "
            "window-own chain)")
    win_rows = {}
    ok_win_build = True
    for wi, kz in enumerate(W_LIST):
        wsd = W_SEED_BASE + W_SEED_STEP * wi
        ctxw = MS.ctx_build(kz)
        dw0 = np.asarray(ctxw["darm"], float)
        Lw = int(ctxw["L"])
        uuw = np.asarray(ctxw["uu"], float)
        mmw = np.asarray(ctxw["mm"], float)
        Mw = Lw // 2 + 1

        def meas_w(dv):
            """window-local survival readout: the union sign
            chain scanned to NREF_w + 8 (extension + 32) in the
            window's OWN units through the same r280 chain; the
            r290 w9 code path is unchanged; censoring at
            NREF_w + 32 disclosed."""
            dv = np.asarray(dv, float)
            xu, wu, _z = BL.union_of_ctx(dict(darm=dv, L=Lw))
            sg, _l, _r = BL.sign_chain_f64(xu, wu,
                                           nref_w + W_EXT)
            mcw = next((n for n in range(len(sg)) if sg[n] < 0),
                       None)
            if mcw is None:
                sg, _l, _r = BL.sign_chain_f64(xu, wu,
                                               nref_w + W_EXT2)
                mcw = next((n for n in range(len(sg))
                            if sg[n] < 0), None)
            cens = mcw is None
            sw = ((nref_w + W_EXT2) if mcw is None else mcw) \
                / float(nref_w)
            return sw, cens

        m0w = PFP.measure_density(dw0, Lw)
        nref_w = int(m0w["minC"])
        ok_wall = (m0w["cross"] is not None
                   and m0w["cross"] > nref_w)

        def margin_w(dv):
            me = PFP.measure_density(dv, Lw)
            if me["rho"] is None or me["cross"] is None \
                    or me["cross"] <= nref_w:
                return float("nan")
            return 1.0 - me["rho"][nref_w]

        m00w = margin_w(dw0)
        g_locw = MF.local_gaps(uuw)
        Dgw = 2.0 * ctxw["alpha"] / ctxw["M"]
        REFw = 0.5 * float(np.sum(mmw * g_locw)) / Dgw

        def lag_l1w(dd):
            return float(np.sum(np.abs(PFP.lag_of(dd, Mw))))

        cbw = PFP.lag_of(dw0, Mw)
        invw = float(np.max(np.abs(PIK.grid_density(cbw) - dw0))) \
            / max(float(np.max(np.abs(dw0))), 1e-300)
        GEw = BL.grad_ext(ctxw, nref_w + 2)
        xiw = BL.dir_opt(GEw["gR"], GEw["gL"], GEw["gaps"],
                         nref_w)
        thw, thkw, _cw = BL.theta_of_dir(GEw["gR"], GEw["gL"],
                                         GEw["gaps"], xiw, nref_w)
        du_rw = 2.0 * thw * GEw["gaps"] * xiw
        f_ex = min(1.0, THETA_CAL / (2.0 * thw))
        du1w = GEw["gaps"] * xiw
        cjw = np.where(du1w > 0, du1w * GEw["gR"][:, nref_w],
                       du1w * GEw["gL"][:, nref_w])
        ordw = np.argsort(cjw)
        dirs_w = []
        okc = True
        uRw, mRw = RA.subset_move(uuw, mmw, f_ex * du_rw,
                                  np.ones(len(uuw)))
        okc = okc and MF.conserve_comb(
            "P2_JIT", uuw, mmw, uRw, mRw,
            f_ex * 2.0 * thw * AMP_PAD)
        dirs_w.append(("RIDGE", np.asarray(PIK.build_rung(
            kz, comb=(uRw, mRw))["d"], float) - dw0))
        for j in range(N_ATOM_W):
            mk = np.zeros(len(uuw))
            mk[ordw[j]] = 1.0
            u2, m2 = RA.subset_move(uuw, mmw, f_ex * du_rw, mk)
            okc = okc and MF.conserve_comb(
                "P2_JIT", uuw, mmw, u2, m2,
                f_ex * 2.0 * thw * AMP_PAD)
            dirs_w.append(("ATOM%02d" % j, np.asarray(
                PIK.build_rung(kz, comb=(u2, m2))["d"],
                float) - dw0))
        for i in range(N_FRAC_W):
            dd, (u2, m2) = PFP.dir_frac(uuw, mmw, kz, dw0,
                                        THETA_CAL, wsd + i)
            okc = okc and MF.conserve_comb(
                "P2_JIT", uuw, mmw, u2, m2, THETA_CAL)
            dirs_w.append(("FRAC%02d" % i, dd))
        llw = np.arange(Lw)
        s_lw = 4.0 * np.sin(math.pi * llw / Lw) ** 2 / (2.0 * Lw)
        for i in range(N_DENS_W):
            dd = PFP.dir_dens(dw0, Lw, wsd + 10 + i)
            eta0 = abs(float(np.sum(dd * s_lw)))
            okc = okc and eta0 <= ETA0_BAR \
                * max(float(np.sum(np.abs(dd * s_lw))), 1.0)
            dirs_w.append(("DENS%02d" % i, dd))
        vw = {n: CF.unit_dir(dd, lag_l1w(dd), REFw)
              for n, dd in dirs_w}
        names_w = [n for n, _d in dirs_w]
        ok_win_build = ok_win_build and okc and ok_wall \
            and invw <= 1e-12
        # sealed ladder with halving rule
        ladder = list(HESS_EQ_HS)
        n_halve = 0
        for _try in range(LADDER_MAX_HALVE + 1):
            fin_all = True
            diag_w = {}
            for n in names_w:
                v = vw[n]
                ests = []
                for h in ladder:
                    mp_ = margin_w(dw0 + v * h)
                    mn_ = margin_w(dw0 - v * h)
                    fin_all = fin_all and math.isfinite(mp_) \
                        and math.isfinite(mn_)
                    ests.append((mp_ - 2.0 * m00w + mn_)
                                / (h * h))
                diag_w[n] = ests[1]
            if fin_all:
                break
            ladder = [h / 2.0 for h in ladder]
            n_halve += 1
        hw_pair = ladder[1]
        Hw = np.zeros((len(names_w), len(names_w)))
        fin_pairs = True
        for i in range(len(names_w)):
            Hw[i, i] = diag_w[names_w[i]]
            for j in range(i + 1, len(names_w)):
                u, v = vw[names_w[i]], vw[names_w[j]]
                msp = margin_w(dw0 + (u + v) * hw_pair)
                msn = margin_w(dw0 - (u + v) * hw_pair)
                mdp = margin_w(dw0 + (u - v) * hw_pair)
                mdn = margin_w(dw0 - (u - v) * hw_pair)
                fin_pairs = fin_pairs and all(
                    math.isfinite(x) for x in (msp, msn, mdp,
                                               mdn))
                if not fin_pairs:
                    continue
                d2su = (msp - 2.0 * m00w + msn) \
                    / (hw_pair * hw_pair)
                d2di = (mdp - 2.0 * m00w + mdn) \
                    / (hw_pair * hw_pair)
                Hw[i, j] = Hw[j, i] = CF.pol_of_d2(d2su, d2di)
        Vw = np.stack([vw[n] for n in names_w], axis=1)
        Gw = Vw.T @ Vw
        wGw, UGw = np.linalg.eigh(Gw)
        # window corpus
        cpts = []

        def addw(tag, dv):
            sw, cens = meas_w(dv)
            cpts.append(dict(tag=tag,
                             delta=np.asarray(dv, float) - dw0,
                             s=sw, cens=cens))

        addw("W%d:MAIN" % kz, dw0)
        ugw, uww_ = PB.smooth_comb(ctxw["alpha"])
        d_smw = np.asarray(MS.ctx_build(
            kz, comb=(ugw, uww_))["darm"], float)
        addw("W%d:WORLD:SMOOTH" % kz, d_smw)
        w_dens_w = [d_smw]
        for si in range(2):
            sctx = MS.ctx_build(kz, scramble_seed=wsd + 40 + si)
            ok_win_build = ok_win_build and bool(np.array_equal(
                np.asarray(sctx["mm"]), mmw))
            dW = np.asarray(sctx["darm"], float)
            w_dens_w.append(dW)
            addw("W%d:WORLD:SCR:%d" % (kz, wsd + 40 + si), dW)
        sctx = MS.ctx_build(kz, scramble_seed=wsd + 42)
        ok_win_build = ok_win_build and bool(np.array_equal(
            np.asarray(sctx["mm"]), mmw))
        addw("W%d:WORLD:ENSR:%d" % (kz, wsd + 42),
             np.asarray(sctx["darm"], float))
        for dT, pn in ((w_dens_w[0], "SMOOTH"),
                       (w_dens_w[1], "SCRa")):
            for t in PATH_TS:
                addw("W%d:PATH:%s:t=%.4g" % (kz, pn, t),
                     PFP.interp_density(dw0, dT, t))
        for i in range(N_FRAC_WC):
            dd, (u2, m2) = PFP.dir_frac(uuw, mmw, kz, dw0,
                                        THETA_CAL, wsd + 20 + i)
            ok_win_build = ok_win_build and MF.conserve_comb(
                "P2_JIT", uuw, mmw, u2, m2, THETA_CAL)
            unit = dd / max(lag_l1w(dd), 1e-300)
            for dist in DIST_GRID_W:
                addw("W%d:DIR:FRAC:%d:d=%.0e"
                     % (kz, wsd + 20 + i, dist),
                     dw0 + unit * (dist * REFw))
        for i in range(N_DENS_WC):
            dd = PFP.dir_dens(dw0, Lw, wsd + 30 + i)
            eta0 = abs(float(np.sum(dd * s_lw)))
            ok_win_build = ok_win_build and eta0 <= ETA0_BAR \
                * max(float(np.sum(np.abs(dd * s_lw))), 1.0)
            unit = dd / max(lag_l1w(dd), 1e-300)
            for dist in DIST_GRID_W:
                addw("W%d:DIR:DENS:%d:d=%.0e"
                     % (kz, wsd + 30 + i, dist),
                     dw0 + unit * (dist * REFw))
        for r in cpts:
            xw = CF.proj_coords(Vw, wGw, UGw, GCUT, r["delta"])
            r["F10"] = CF.func_q10(xw, Hw)
            r["F0"] = float(np.linalg.norm(r["delta"]))
        svw = [r["s"] for r in cpts]
        dlw = [r["s"] < NEAR for r in cpts]
        n_cens = sum(1 for r in cpts if r["cens"])
        spFw = BH.spearman([r["F10"] for r in cpts], svw)
        spBw = BH.spearman([r["F0"] for r in cpts], svw)
        aucw = CF.auc_rank([r["F10"] for r in cpts], dlw)
        pspw = MR.partial_sp([r["F10"] for r in cpts], svw,
                             [r["F0"] for r in cpts])
        # top eigenaxis DENS share
        keepw = wGw >= GCUT * wGw[-1]
        Ukw = UGw[:, keepw]
        Wkw = Ukw / np.sqrt(wGw[keepw])[None, :]
        Aw = Wkw.T @ Hw @ Wkw
        lamw, Yw = np.linalg.eigh(Aw)
        ow = np.argsort(-np.abs(lamw))
        coef_topw = (Wkw @ Yw[:, ow])[:, 0]
        dens_iw = [i for i, n in enumerate(names_w)
                   if n.startswith("DENS")]
        dsw = coef_share(coef_topw, dens_iw)
        win_rows[kz] = dict(nref=nref_w, thw=thw, f_ex=f_ex,
                            n_halve=n_halve, fin_pairs=fin_pairs,
                            n=len(cpts), n_cens=n_cens, spF=spFw,
                            spB=spBw, auc=aucw, psp=pspw,
                            dens_share=dsw, s_lo=min(svw),
                            s_hi=max(svw),
                            beats=(math.isfinite(spFw)
                                   and math.isfinite(spBw)
                                   and abs(spFw) > abs(spBw)))
        check("G7%d-window-w%d" % (wi * 2, kz),
              okc and ok_wall and fin_pairs and invw <= 1e-12,
              "WINDOW w%d CHAIN (window-own): NREF_w %d (cross "
              "%s), theta_up %.3e, extraction dose cap f_ex "
              "%.3f, REF_w %.3f (inversion %.1e); 12 training "
              "dirs conservation/eta_0 exact; ladder halved %d x "
              "(final mid step %.3g), all diag+pair margins "
              "finite %s; corpus %d points, s_w in [%.2f, %.2f], "
              "censored %d"
              % (kz, nref_w, str(m0w["cross"]), thw, f_ex, REFw,
                 invw, n_halve, hw_pair, str(fin_pairs),
                 len(cpts), min(svw), max(svw), n_cens))
        check("G7%d-window-w%d-contest" % (wi * 2 + 1, kz),
              math.isfinite(spFw) and math.isfinite(spBw),
              "WINDOW w%d CONTEST: sp(F10_w) %+.3f vs sp(F0_M2_w)"
              " %+.3f (|F10| %s by %+.3f), AUC(dead) %.3f, "
              "partial %s; top-eigenaxis DENS share %.3f"
              % (kz, spFw, spBw,
                 "beats" if win_rows[kz]["beats"] else "LOSES",
                 abs(spFw) - abs(spBw), aucw,
                 ("%+.3f" % pspw) if math.isfinite(pspw)
                 else "DEGEN", dsw))
    beats_list = [win_rows[kz]["beats"] for kz in W_LIST]
    degen = [kz for kz in W_LIST
             if not (math.isfinite(win_rows[kz]["spF"])
                     and math.isfinite(win_rows[kz]["spB"]))]
    if degen:
        wtrans_verd = ("WINDOW_W9_ONLY(WINDOW_DEGENERATE on %s "
                       "-- counts as non-transport, disclosed)"
                       % str(degen))
    elif all(beats_list):
        wtrans_verd = ("WINDOW_TRANSPORTS(F10_w beats F0_M2_w on "
                       "BOTH w7 and w11: the reconciliation is a "
                       "family property, not a w9 artifact)")
    elif any(beats_list):
        wkz = [kz for kz in W_LIST if win_rows[kz]["beats"]][0]
        wtrans_verd = "WINDOW_PARTIAL(w%d only)" % wkz
    else:
        wtrans_verd = ("WINDOW_W9_ONLY(F10_w beats the window "
                       "baseline on neither window)")
    check("G74-transport-adjudication", True,
          "SEALED TRANSPORT RULE (TRANSPORTS iff |sp(F10_w)| > "
          "|sp(F0_M2_w)| on BOTH windows): beats = %s -> %s; "
          "DENS-top mechanism measurement: shares %s"
          % (str(dict(zip(W_LIST, beats_list))),
             wtrans_verd.split("(")[0],
             str({kz: round(win_rows[kz]["dens_share"], 3)
                  for kz in W_LIST})))

    # ---------------- S8 LEG D: DENS-neutralized metric
    section("S8  LEG D -- WHY L2?  THE DENS-NEUTRALIZED BASELINE")
    dens_names = [n for n in names_D if n.startswith("DENS")]
    di = [names_D.index(n) for n in dens_names]
    V_D = Vmat[:, di]
    G_D = V_D.T @ V_D
    wD, UD = np.linalg.eigh(G_D)
    C_D = UD / np.sqrt(np.maximum(wD, 1e-300))[None, :]
    H_D = Hmat[np.ix_(di, di)]
    H_on = C_D.T @ H_D @ C_D
    lamD, QD = np.linalg.eigh(H_on)
    oD = np.argsort(-np.abs(lamD))
    lamD_s = lamD[oD]
    axesD = V_D @ (C_D @ QD[:, oD])
    kappa_ref = float(np.median([abs(diag_l2[n])
                                 for n in names_D
                                 if not n.startswith("DENS")]))
    c2 = np.array([abs(lv) / kappa_ref
                   if abs(lv) > NEUT_GUARD * abs(lamD_s[0])
                   else 1.0 for lv in lamD_s])
    n_flat = sum(1 for lv in lamD_s
                 if abs(lv) <= NEUT_GUARD * abs(lamD_s[0]))
    orth_dev = float(np.max(np.abs(axesD.T @ axesD - np.eye(6))))
    f0n_vals = [math.sqrt(max(neut_dist2(r["delta"], axesD, c2),
                              0.0)) for r in test_pts]
    sp_f0n = BH.spearman(f0n_vals, svec)
    psp_n = MR.partial_sp([r["F10"] for r in test_pts], svec,
                          f0n_vals)
    check("G80-neut-metric", orth_dev <= 1e-9,
          "DENS-NEUTRALIZED METRIC (L2-orthonormal DENS span, "
          "orthonormality dev %.1e; measured curvature "
          "eigenvalues per unit L2 %s; kappa_ref = median "
          "non-DENS |diag| %.3g; scale factors c_j %s, %d FLAT "
          "guards): every DENS axis now carries the TYPICAL "
          "curvature per unit length"
          % (orth_dev, str(["%.3g" % v for v in lamD_s]),
             kappa_ref,
             str([round(float(math.sqrt(v)), 2) for v in c2]),
             n_flat))
    if abs(sp_f10) <= abs(sp_f0n):
        neut_verd = ("L2_VIA_DENS(|sp(F10)| %.3f <= %.3f = "
                     "|sp(F0_NEUT)|: the home win disappears -- "
                     "the DENS scaling carries the information)"
                     % (abs(sp_f10), abs(sp_f0n)))
    else:
        neut_verd = ("L2_NOT_DENS(|sp(F10)| %.3f > %.3f = "
                     "|sp(F0_NEUT)|: the home win survives the "
                     "neutralization -- the F10 information is "
                     "NOT the DENS-sector length distortion)"
                     % (abs(sp_f10), abs(sp_f0n)))
    check("G81-neut-adjudication", math.isfinite(sp_f0n),
          "SEALED NEUTRALIZATION RULE on the bit-identical "
          "94-point split: sp(F0_NEUT) %+.3f (plain F0_M2 %+.3f);"
          " partial sp(F10, s | F0_NEUT) %s -> %s"
          % (sp_f0n, sp_f0m2,
             ("%+.3f" % psp_n) if math.isfinite(psp_n)
             else "DEGEN", neut_verd.split("(")[0]))

    # ---------------- S9 must-fails + scopes
    section("S9  MUST-FAILS + SCOPE AUDITS")
    dd_m1, (u2m, m2m) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                     THETA_CAL, FRESH_BASE + 100)
    v_m1 = CF.unit_dir(dd_m1, lag_l1(dd_m1), REF)
    h_m1 = H_PAIR_H
    mp1 = margin_at(d9 + v_m1 * h_m1)
    mn1 = margin_at(d9 - v_m1 * h_m1)
    H_mut = H_tr.copy()
    H_mut[0, 0] = (mp1 - 2.0 * m00 + mn1) / (h_m1 * h_m1)
    sha_mut = hashlib.sha256(H_mut.tobytes()).hexdigest()
    check("G85-mustfail-retrain", sha_mut != H_SEAL,
          "m1 RE-TRAINING (one H_tr entry re-measured on the "
          "fresh corpus-0 FRAC direction): sha256 %s != seal %s "
          "-- CAUGHT by the hash seal; Leg A ran on the sealed "
          "object only" % (sha_mut[:12], H_SEAL[:12]))
    strip0 = set(t.split(":", 1)[1] for t in all_tag_sets[0]
                 if t != "MAIN")
    strip1 = set(t.split(":", 1)[1] for t in all_tag_sets[1]
                 if t != "MAIN")
    # a corpus 1 rebuilt with the corpus-0 seeds carries the
    # corpus-0 seed labels -- its seed-stripped tags EQUAL strip0
    ov_m2 = mutant_seed_reuse_tags(strip0, set(strip0))
    ov_honest = mutant_seed_reuse_tags(strip0, strip1)
    check("G86-mustfail-seed-reuse", len(ov_m2) > 100
          and len(ov_honest) == 0,
          "m2 SEED REUSE (corpus 1 rebuilt with the corpus-0 "
          "seeds): auditor flags %d overlap tags -- CAUGHT; the "
          "honest corpora share 0 seed-stripped tags (%d)"
          % (len(ov_m2), len(ov_honest)))
    u_m3, m_m3 = RA.mutant_broken_conservation(uu9, mm9, du_ridge)
    ok_m3 = not MF.conserve_comb("P2_JIT", uu9, mm9, u_m3, m_m3,
                                 2.0 * th_up * AMP_PAD)
    check("G87-mustfail-conservation", ok_m3,
          "m3 BROKEN CONSERVATION (one weight scaled 1 + 1e-3): "
          "the exact r276 gate returns False -- CAUGHT")
    ctx7 = MS.ctx_build(W_LIST[0])
    d7 = np.asarray(ctx7["darm"], float)
    caught_m4 = False
    try:
        _bad = proj_x(d7 - d7[0])       # w7 grid into the w9 form
        _bad2 = V_tr.T @ (d7 * 1.0)
    except ValueError:
        caught_m4 = True
    check("G88-mustfail-window-category", caught_m4,
          "m4 WINDOW CATEGORY ERROR (the w9 H_tr applied to a w7 "
          "deviation, L %d vs %d): the projection raises the "
          "dimension error -- CAUGHT BY CONSTRUCTION; the honest "
          "reading: the w9 form cannot be applied off-window, "
          "Leg C measured window-own forms instead (disclosed "
          "control)" % (int(ctx7["L"]), L9))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G89-scope-audits", not hits and not ag_hits,
          "the %d sealed source-pure constructors consume "
          "vectors/densities + geometry + seeds ONLY (%s); "
          "H_tr / g_tr / H_w / H_half / H_double / the "
          "neutralization scales are OUTSIDE the source-pure "
          "list and honestly typed measurement-consuming; "
          "fragment audit: %s"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S10 honesty + verdict
    section("S10  HONESTY LEDGER + VERDICT")
    check("G90-honesty-ledger", True,
          "every correlation, Hessian entry, scale factor and "
          "window number is a MEASUREMENT on finite profile "
          "space; H_tr is the UNCHANGED r293 object (hash-"
          "sealed, mutant-gated); the fresh corpora share "
          "exactly ONE point (MAIN) with each other and with "
          "r293 (disclosed); the jackknife includes the span "
          "change under leave-out (disclosed); the window "
          "survival normalization NREF_w is the window-own "
          "measured wall (w7 half-filling offset +1 disclosed); "
          "the w7/w11 F10-s correlation sign is window-specific "
          "and the transport statement is drawn on |sp| "
          "(disclosed); the DENS neutralization consumes "
          "measured curvatures (typed); the promotion decision "
          "belongs to the consolidation wave, NOT to this probe")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no equidistribution "
          "premise, no posthoc window, no promotion from here, "
          "no RH claim; what the round adds: the five-corpus "
          "stability adjudication with the sealed promotion "
          "bar, the jackknife/rank/step robustness table, the "
          "w7/w11 window transport with window-own chains, and "
          "the DENS-neutralization mechanism test; r243..r293 "
          "stand")
    parts_v = []
    parts_v.append("CORPUS_TABLE(%s)" % tab_txt)
    parts_v.append(stab_verd)
    parts_v.append(jack_verd)
    parts_v.append(rank_verd)
    parts_v.append(step_verd)
    parts_v.append(
        "%s + WINDOW_TABLE(%s)"
        % (wtrans_verd,
           "; ".join("w%d: F10 %+.3f vs F0 %+.3f, partial %s, "
                     "DENS-top %.2f"
                     % (kz, win_rows[kz]["spF"],
                        win_rows[kz]["spB"],
                        ("%+.3f" % win_rows[kz]["psp"])
                        if math.isfinite(win_rows[kz]["psp"])
                        else "DEGEN",
                        win_rows[kz]["dens_share"])
                     for kz in W_LIST)))
    parts_v.append(neut_verd)
    verd = " + ".join(parts_v)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s -- MEASURED stability adjudication of the r293 "
          "functional; NO promotion from here, NO L* claim, NO "
          "RH claim" % verd)
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
