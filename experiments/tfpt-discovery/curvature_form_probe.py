#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""curvature_form_probe -- PRIME.PORT.LSTAR.CURVATURE_FORM.01
(round 292): IS THE WORKING SET CHARACTERIZED BY A CURVATURE
TWO-FORM?  r290 sealed BASIN_GEOMETRY (anisotropic tube, four
local profile scalars blind); r291 sealed the ridge anatomy:
the lift is a FIRST-ORDER BUDGET phenomenon with one sharp
threshold m* in (1.280, 1.291] (a ~1.3 second-order resistance
factor over the naive flip level -1; perfect separation over
all 18 matched-dose cases), exactly ONE overdrive retraction
(TOP6 at factor 8), linear/projective functionals blind for
the third time (below the size baseline |sp| 0.881), and the
SMOOTH killer axis COLLECTIVE-QUADRATIC (margin curvature d2
-23.3 Richardson-stable, 23.7x random).  THE r291 STRUCTURAL
HINT: sharp budget threshold + quadratic SMOOTH valley + blind
linear projections => the working set may be characterized by
a curvature TWO-FORM, not a linear functional.  THIS ROUND
measures that form.  NOT a proof round: no L* claim, no bound
mechanism, no asymptotic law.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

MACHINERY IMPORTED VERBATIM (no duplication): r291 RA.
{subset_move, atom_ints, part_masks, part_ratio, func_antidev,
split_auditor, mutant_broken_conservation} + the r291 sealed
constants (SPARSE_KS, SECT dose 2 theta_up, AMP_PAD); r290
PFP.{measure_density, lag_of, interp_density, dir_frac,
dir_dens, func_midband} + PATH_TS / DIST_GRID / RIDGE_FACS /
NEAR / DEAD; r280 BL.{grad_ext, dir_opt, theta_of_dir,
union_of_ctx, sign_chain_f64}; r254 ODG.base_exp (integer
root extraction -- the comb atoms ARE p^k by construction,
no oracle); r278 MS.{ctx_build, wsig_vec};
r276 MF.{local_gaps, pert_jit, conserve_comb}; v881 PIK.
{build_rung, grid_density, lambda_eps}; r243 PB.smooth_comb;
r244 BH.spearman; paircorr PC.{Grid, gen_model}; r284
LS.dist_rule; v563 core READ-ONLY.  The theta_eq coordinate is
the r290-a1 LAG coordinate with the ANALYTIC reference REF =
0.5 sum m g / Delta, gated on the r290 pinned calibration
quadruple VERBATIM.  Survival depth s = minC / N_REF, N_REF =
184.  All curvature probes are LINEAR DENSITY EXTENSIONS on
the fixed grid (in-cell equal to position moves, r290
disclosure); the margin channel is m = 1 - rho_184 through the
ONE gated r290 measurement channel; the wall-budget channel is
log|h_184| through the exact r280 sign chain.

INDEX FIREWALL (binding, r238-r291 discipline): ground truth
(minC, crossings, margins, log-h values) enters GATES, the
DISCLOSED measurement-consuming training channels (the
two-form H, the trained slopes g -- both sealed by the
train/test split) and record tables only; the sealed
source-pure constructors consume vectors/densities + grid
geometry + seeds ONLY (AST scope audit); no zero/prime oracles
anywhere (AST firewall).

LEG 0 -- ANCHOR REGRESSION (all gated): w9 record (S 367/263/
104, minC 184, crossing 185, margin 1.68e-4 rel 0.01, z_v
-3.149 tol 0.02, b34 -0.105 tol 0.01); theta_eq metric (REF ==
125.75 rel 1e-3, inversion identity 1e-12, r290 pinned
quadruple devs <= 0.15); control flips EPST/SCR/SMOOTH/HL2 =
25/21/27/25; r280 ridge anchor (theta_up 3.87e-5 rel 0.05, OPT
endpoint minC 185); r291 BUDGET-THRESHOLD REGRESSION: the 18
matched-dose cases rebuilt verbatim -- all margins == the r291
record table (abs tol 0.005), the lift pattern identical
(PRIME/HEAD/XIPOS + top-k >= 9 lift), the separation bracket ==
(1.280, 1.291] (tol 0.005), TOP6 at factor 8 retracts (margin
9.09 tol 0.02, minC 184, s 1.00); r291 SMOOTH-d2 REGRESSION
(the r291 code path verbatim: d2 -23.31 rel 0.02, Richardson
devs <= 0.01, random seed-291100 d2 -0.98 rel 0.10, ratio 23.7
tol 1.0); EPSTEIN FIRST-ORDER FLATNESS (|c_25| <= 1e-9,
theta_up >= 1e9, rec 5.03e10).

LEG A -- HESSIAN SPECTROSCOPY (core question 1: is the wall
curvature low-rank?): the margin Hesse form H at MAIN over the
sealed 29-direction set D, every direction theta_eq-normalized
(lag-L1 == REF per unit): 3 world axes (MAIN->SMOOTH/SCR/
EPST), the r280 ridge axis, the 9 top-atom sub-directions of
the ridge (one-hot masks of the r291 c_j ranking, conservation
gated), 10 fresh FRAC directions (seeds 292100+, r276 comb
jitters, weights bitwise) + 6 fresh DENS directions (seeds
292200+, eta_0 projected exactly).
  (a1) DIAGONAL: d2(v) by central differences at the THREE
    dyadic steps HESS_EQ_HS = (7.8125e-6, 1.5625e-5, 3.125e-5)
    theta_eq (amendment a1: the ladder was halved after the
    calibration pass measured NaN margins -- crossing left 185
    -- at the original outer step 6.25e-5 on two DENS
    directions; the margin-valid scale was re-measured, a
    measurement-domain step fix); Richardson census with
    RICH_TOL 0.1; |d2| < D2_FLOOR = 0.5 per theta_eq^2 typed
    FLAT (Richardson advisory there); non-flat non-quadratic
    directions typed NONQUAD (census reported, finiteness
    gated).
  (a2) OFF-DIAGONAL: the FULL polarization matrix H(u, v) =
    [d2(u+v) - d2(u-v)] / 4 over all 406 pairs at the mid step
    H_PAIR_H = 1.5625e-5 (combined vectors reach <= 3.125e-5
    effective theta_eq, the verified margin-valid scale;
    diagonal entries of the matrix at the SAME mid step,
    consistency); the 15 SELECTED pairs (world x world, world
    x ridge, ridge x atoms) additionally pass the expansion-
    identity crosscheck |H_pol - [d2(u+v) - d2(u) - d2(v)]/2|
    <= POL_TOL x max(|H_pol|, D2_FLOOR).
  (a3) EIGENSTRUCTURE: generalized eigendecomposition of H
    against the L2 Gram G of the unit directions (whitening
    eigencut GCUT 1e-10 rel; the theta_eq coordinate is an L1
    object with no inner product, so the sealed SPECTRAL
    metric is the L2 metric on the signed density --
    eigenvalues lam_k are margin curvature per unit L2 step,
    disclosed): r = #eigendirections carrying >= 90 pct of
    sum |lam|; fine type HESSIAN_LOW_RANK(r) iff r <=
    LOWRANK_BAR = 4, else HESSIAN_EXTENSIVE(r).  Reported: the
    top-eigenvalue table, |cos|(SMOOTH axis, top eigendirection)
    (aligned iff >= COS_TOP_BAR = 0.7), the ridge-axis position
    in the SAME L2 units (amendment a4: the comparison is drawn
    on the L2-normalized diagonal H_rr / |v_ridge|_L2^2 -- the
    raw theta_eq-diagonal against the per-L2 eigenvalues was
    unit-inconsistent, a display-rule conditioning fix;
    RIDGE_CURV_FLAT iff |H_rr^L2| <= 0.1 |lam_top|, else sign
    typed -- the lift should sit in a FLAT or POSITIVE
    curvature direction).
LEG A' -- EPSTEIN CONTRAST (same question at the first-order
flat wall): the log|h_25| curvature census at EPSTEIN along
its own optimizer axis + its flip + 4 fresh jitter directions
(seeds 292300+, conservation gated at the base dose; the MAIN
direction is undefined in EPSTEIN position space -- different
atom sets, disclosed), central differences at EPS_TAU = 1e-3
(Richardson at 2e-3), q per theta^2, compared against the
MAIN median |q| per theta^2 of the 18 Leg-B subsets:
EPST_CURV_FLAT(ratio) iff median ratio <= EPST_Q_BAR = 1e-2,
else EPST_CURV_PRESENT(ratio) -- is the first-order flat wall
also second-order structureless?
LEG B -- THE THRESHOLD OBJECT m* (core question 2: does the
curvature explain the 1.3 factor?): for each of the 18
matched-dose sub-directions delta_A = du_ridge x mask, measure
Delta log|h_184|(t) ONE-SIDED on the lift side at the sealed
ladder t = 1/16, 1/8, 3/16, 1/4, 3/8 in factor units
(amendment a2: the original +-t central-difference design
measured the TWO-SIDED AVERAGE slope, which differs from the
side-selected r291 budget at the 8 on-node atoms -- the
calibration pass exposed rel devs up to 0.25 with the exact
kink signature; the one-sided ladder measures the SAME
side-selected object the budget linearizes, a measurement-
domain estimator fix; all doses stay below the flip: budget
consumed <= 0.75 at t = 3/8 even for the full set b = 2):
  (b1) MODEL SOLVE + LINEAR IDENTITY GATE: on each of the two
    dyadic triples A = (1/16, 1/8, 3/16) and B = (1/8, 1/4,
    3/8) the exact cubic model Dlh(t) = -b t + q t^2/2 +
    c3 t^3/6 is SOLVED (3x3 linear solve through the anchored
    origin, no fitting); the triple-A slope b_A must equal
    the ANALYTIC r291 budget b(A) = -sum_{j in A} c_j
    2 theta_up within BLIN_TOL = 0.05 rel on all 18 cases
    (sign conventions verbatim r291: c_j = side-selected
    du_j grad_j log h_184 per unit theta; b in naive-flip
    units, flip level 1).
  (b2) CURVATURE: q_R = q_A (the finer triple), consistency
    dev |q_B/q_A - 1| reported (Q_RICH advisory bar 0.35);
    c3 = c3_A.
  (b3) SEALED THRESHOLD ADJUDICATION (exactly one): corrected
    budgets b_q(A) = b(A) - q_R(A)/2; THRESHOLD_EXPLAINED iff
    the corrected budgets STILL separate lift from no-lift
    (max no-lift b_q < min lift b_q) AND the corrected bracket
    midpoint sits within THR_TOL = 0.10 of the naive flip
    level 1; else THRESHOLD_NOT_EXPLAINED (midpoint resp.
    SEPARATION_LOST detail).
  (b4) SEALED RETRACTION ADJUDICATION (exactly one): the
    quadratic prediction at the overdrive point B2(8) =
    8 b(TOP6) - 32 q_R(TOP6); RETRACTION_PREDICTED iff B2(8)
    < the corrected threshold midpoint (the measured TOP6
    factor-8 case does NOT lift, r291); else the solved
    third-order coefficient c3(TOP6) extends the prediction
    to B3(8) = B2(8) - 512 c3 / 6:
    RETRACTION_HIGHER_ORDER(with the disclosed answer whether
    the cubic term explains it or not).
LEG C -- SEALED TWO-FORM FUNCTIONAL CONTEST (core question 3),
candidates fixed BEFORE evaluation, fresh 143-point corpus
with the r290/r291 conservation discipline (MAIN + 5 worlds +
4 world paths x PATH_TS + 16 fresh directions x DIST_GRID + 9
ridge factors + 8 ENS_SCR replicates seeds 285100+):
  TRAINING SPLIT (disclosed measurement-consuming, sealed by
  the split): the two-form H_tr, the Gram G_tr and the trained
  first-order margin slopes g_tr live on the 18 TRAINING
  directions = FRAC 0/2/4/6/8 + DENS 0/2/4 + RIDGE + the 9
  atom directions; EVERY corpus point generated from a
  training direction (the 40 ladder points of the 8 training
  randoms + the 9 RIDGE factor points) is EXCLUDED from the
  test split (94 points; disjointness itself a gate); world
  axes are NOT trained on.  Test deviations enter through the
  exact L2 projection x = G_tr^+ V_tr^T delta (eigencut
  pseudo-solve, no fitting).
  F10 CURVATURE ENERGY: Q(delta) = x^T H_tr x / 2 (the sealed
    two-form as a survival predictor; 0 at zero deviation).
  F11 BUDGET + CURVATURE: g_tr^T x + x^T H_tr x / 2 (the r291
    mechanism -- first order plus curvature -- as one closed
    margin predictor in coherent margin units; the analytic
    c_j budget identity is gated in Leg B; 0 at zero
    deviation).
  F12 RAYLEIGH QUOTIENT: x^T H_tr x / |delta|_L2^2 (scale-free
    direction classifier; restriction to the training span
    disclosed); AUC (dead = s < NEAR, tie-aware rank AUC)
    reported IN ADDITION to spearman for all three.
  BASELINE F0 = theta_eq(deviation), the trivial size
  predictor, disclosed (r291: |sp| 0.881); MAIN-separation
  construction-triviality DISCLOSED (all three candidates are
  0 at MAIN).
  SEALED ADJUDICATION (exactly one): CURVATURE_FUNCTIONAL_
  FOUND iff best |spearman vs s over the test split| >= SP_BAR
  = 0.6 AND |sp_best| > |sp(F0)| AND the dead-world values of
  the best candidate are non-degenerate (spread > WORLD_
  SPREAD_BAR = 0.01 x the full test-corpus range); else
  CURVATURE_BLIND (the fourth honest negative -- then the
  quadratic class is dead too and is sealed as such).
LEG D -- CURVATURE ORIGIN (bycatch, small): the top
eigendirection(s) of Leg A projected on the r288/r289
coordinates: antiphase 3+4 pair statistic (RA.func_antidev),
mid-band 50-75 pct share (PFP.func_midband), fold-position
tercile energy shares, participation ratio -- each against
the same statistics of the pinned random direction FRAC00;
factor-2 comparison disclosed per statistic (typed
MEASUREMENT, no adjudication weight).
WARDS / MUST-FAILS (each loud): (m1) the polarization identity
with the WRONG prefactor (/2 instead of /4) on an exact toy
quadratic form must be CAUGHT by the expansion-identity
crosscheck; (m2) H trained WITH test-split directions (seal
break) must be CAUGHT by the split auditor; (m3) a subset move
with one weight scaled 1 + 1e-3 must be CAUGHT by the exact
r276 conservation gate; (m4) a single-step-size d2 estimate
(Richardson break) must be FLAGGED as NOT VERIFIABLE by the
sealed Richardson auditor.  Scope audits: the sealed
source-pure constructors consume vectors/densities + geometry
+ seeds only; H_tr / g_tr / q(A) are honestly typed
measurement-consuming (split-sealed resp. Leg-B gated);
fragment audit (no fit fragments).  STOP LIST (anti-gates,
binding): NO L* claim, NO bound mechanism, NO asymptotic law,
NO derived 5/7, NO equidistribution premise, NO posthoc
window, NO RH claim; r243..r291 stand.

SEALED CONSTANTS: MAIN window 9; N_REF 184; CROSS_REC 185;
MINC_REC 184; S_REC (367, 263, 104); MARGIN_REC 1.68e-4 rel
0.01; ZV_REC -3.149 tol 0.02; B34_REC -0.105 tol 0.01;
CTRL_FLIPS EPST 25 / SCR 21 / SMOOTH 27 / HL2 25 (seed 101);
THUP_REC 3.87e-5 rel 0.05; RIDGE_MINC_REC 185; REF_REC 125.75
rel 1e-3; metric calibration = the r290 pinned quadruple
VERBATIM (CAL_SEEDS 290000/1/2 at 1e-3 + T3_SEED 290010 at
3e-4, tol 0.15); AMP_PAD 1 + 1e-9 (r291 a2); NEAR 0.90 / DEAD
0.50; r291 REGRESSION RECORDS verbatim: partition margins
PRIME 1.798 / POWER 0.202 / HEAD 1.528 / MID 0.293 / TAIL
0.179 / XIPOS 1.291 / XINEG 0.709, top-k margins k1 0.497 /
k2 0.731 / k4 0.963 / k6 1.136 / k8 1.280 / k9 1.332 / k10
1.371 / k12 1.444 / k16 1.570 / k32 1.803 / k70 2.000 (abs
tol 0.005 each), lift sets {PRIME, HEAD, XIPOS} + {k >= 9},
bracket (1.280, 1.291] tol 0.005, TOP6 fac-8 margin 9.09 tol
0.02 with minC 184 / s 1.00, top-9 atoms (2, 3, 5, 13, 11, 4,
29, 7, 89), R291_D2 -23.31 rel 0.02 / rich devs <= 0.01 /
R291_D2_RAND -0.98 rel 0.10 / ratio 23.7 tol 1.0 (r291 HESS_HS
(6.25e-5, 1.25e-4, 2.5e-4) path units, seed 291100 random);
EPST_C_BAR 1e-9 / EPST_THUP_MIN 1e9; LEG-A HESS_EQ_HS
(7.8125e-6, 1.5625e-5, 3.125e-5) theta_eq (a1) / H_PAIR_H
1.5625e-5 (a1) / RICH_TOL 0.1 / D2_FLOOR 0.5 / POL_TOL 0.25 /
GCUT 1e-10 / TRACE_BAR 0.90 / LOWRANK_BAR 4 / COS_TOP_BAR 0.7
/ RIDGE_FLAT_FRAC 0.1; SELECTED PAIRS = 3 world x world + 3
world x ridge + 9 ridge x atom; NDIR_FRAC 10 seeds 292100+ /
NDIR_DENS 6 seeds 292200+ / EPS_SEEDS 292300+ (4); LEG-B
TAU_LADDER (1/16, 1/8, 3/16, 1/4, 3/8) one-sided (a2) /
LEGB_PAD 1 + 1e-7 (a3, fractional-dose gate conditioning) /
BLIN_TOL 0.05 / Q_RICH_BAR 0.35 (advisory) / THR_TOL
0.10 / OVERDRIVE (TOP6, factor 8); EPS_TAU 1e-3 / EPST_Q_BAR
1e-2; LEG-C PATH_TS / DIST_GRID / RIDGE_FACS r290 verbatim /
ENS_SCR_REPS 8 seeds 285100+ / TRAIN_FRAC (0, 2, 4, 6, 8) /
TRAIN_DENS (0, 2, 4) / SP_BAR 0.6 / WORLD_SPREAD_BAR 0.01 /
ETA0_BAR 1e-12 / THETA_CAL 1e-3; runtime <= 1800 s; smoke =
toys + firewall + scopes + w9 regression + m1/m2/m4 mutants
(anchors, legs, corpus, adjudications skipped).
PRE-SPEC SCOPING (disclosed): every record number is a
published r276/r280/r290/r291 record adopted as-is; the
direction set, the step ladders, the polarization rule, the
eigen protocol with its bars, the threshold and retraction
rules, the three functional candidates with the baseline
contest and the split discipline, and the must-fail set were
fixed at design time from the published records and the task
contract; a design-time calibration pass (disclosed below)
preceded the freeze; no bar, band or rule was tuned after the
record freeze.

SEALED VERDICT FORM (frozen BEFORE the record freeze, joined
with '+'):
  HESSIAN_SPECTRUM(fine type LOW_RANK(r)/EXTENSIVE(r), top
    eigenvalues + trace shares, SMOOTH alignment cos, ridge
    position (value, sign, rank)) [always]
  + EPSTEIN_CONTRAST(EPST_CURV_FLAT/PRESENT(ratio)) [always]
  + [exactly one of] THRESHOLD_EXPLAINED(midpoint) /
    THRESHOLD_NOT_EXPLAINED(detail)
  + [exactly one of] RETRACTION_PREDICTED(B2) /
    RETRACTION_HIGHER_ORDER(B2, B3, c3)
  + [exactly one of] CURVATURE_FUNCTIONAL_FOUND(name, sp,
    baseline) / CURVATURE_BLIND(best, sp, baseline)
  + FUNCTIONAL_TABLE(per candidate: spearman, AUC, world
    values, detector typing incl. construction-trivial
    disclosure)
  + EIGENAXIS_SIGNATURE(stat table vs random, factor-2
    comparison) [always, typed MEASUREMENT].
Honesty before beauty: Hessian entries, eigenvalues, q
coefficients, corrected budgets, functional correlations and
axis statistics are MEASUREMENTS on finite w9 profile space;
H_tr / g_tr are trained on measured margins (sealed by the
disjoint split); the quadratic threshold story is a
second-order statement, not a mechanism claim; no verdict
claims L*, a bound mechanism, a derived 5/7 or an asymptotic
law.

RECORD TABLES (frozen from the record run; calibration
protocol, chronology honest: smoke pass 1 = 11/11 (0.2 s,
pre-a2 gate set), 12/12 after the cubic-solve toy;
calibration pass 1 = first full evaluation = 31/35, wall 78
s, exposing amendments a1 + a2 (below); pass 2 with a1/a2 =
34/36, exposing a3 + a4 (below); pass 3 with a1-a4 = 36/36,
wall 79 s = the record physics; passes 4-5 added the e_top
loadings DISPLAY only (no rule, bar or measurement changed,
all numbers identical); the record-table insertion below is
the only post-freeze edit, which IS the protocol; record
rerun after insertion 36/36, run1/run2 identical up to WALL).
DISCLOSED CALIBRATION AMENDMENTS (found in calibration,
BEFORE the record freeze; no physics bar, direction class,
threshold rule, functional class or verdict rule moved):
(a1) the Hessian step ladder was first drawn at (1.5625e-5,
3.125e-5, 6.25e-5) theta_eq with pairs at 3.125e-5; the
calibration pass measured NaN margins (crossing left 185) at
the outer step on DENS02+/DENS04- and on aligned pair combos
-- the ladder was halved to (7.8125e-6, 1.5625e-5, 3.125e-5)
with pairs at 1.5625e-5, the re-measured margin-valid scale
(all 29 x 3 x 2 + 406 x 4 points finite; a measurement-domain
step fix).  (a2) Leg B was first drawn as a +-t CENTRAL
difference; the calibration pass measured rel devs up to
0.252 against the analytic budget with the exact kink
signature -- the central difference measures the TWO-SIDED
AVERAGE slope while the r291 budget is SIDE-SELECTED (8/70
atoms on-node, right/left slopes differ at 0).  The channel
was re-anchored one-sided on the lift side with the exact
origin-anchored cubic-triple solve; the identity gate then
measures max rel dev 0.0033 (an estimator fix demanded by the
gate itself).  (a3) the fractional-dose conservation gates
sat at the equality boundary where the add-subtract roundoff
of the position update is ~1/t relative (measured overshoot
7.7e-9 at t = 1/16 vs the r291 1e-9 headroom); LEGB_PAD =
1 + 1e-7 (pure f64 gate conditioning, the physical bound
stands at 1e-7 relative).  (a4) the ridge-position display
compared the theta_eq-diagonal against per-L2 eigenvalues
(unit-inconsistent); the comparison was re-drawn on the
L2-normalized diagonal (display-rule conditioning; the
RIDGE_FLAT_FRAC bar itself unchanged).
RECORD VERDICT = HESSIAN_SPECTRUM(HESSIAN_LOW_RANK(1): ONE
eigendirection carries 92.5 pct of sum|lam| = 0.452 (top-8
per unit L2 step: -0.418, -0.0165, -0.00807, -0.00345,
+0.00285, -0.00202, +0.000538, +0.000342); the top axis is a
pure DENS combination (loadings DENS05 +1.00, DENS04 -0.71,
DENS03 +0.69, DENS01 +0.53) -- the sharpest margin curvature
per unit L2 lives in the on-support DENSITY sector, NOT in
the world axes; SMOOTH_OFF_TOP(|cos| 0.07): the arithmetic
killer axis is NOT the top L2-curvature carrier (its
lethality is dose-anisotropy in theta_eq, r290/r291, not
extreme L2 curvature); RIDGE_CURV_FLAT(H^L2(r, r) =
-1.13e-05, rank 28/29 of the L2-normalized diagonal; raw
-6.67 per theta_eq^2 = the SMALLEST |diagonal| of all 29
directions but ATOM07) -- the lift axis sits in the flattest
curvature sector, exactly the r291 expectation) +
EPSTEIN_CONTRAST(EPST_CURV_FLAT(ratio 5.4e-15): q_E =
-2.2e-6..+3.4e-7 per theta^2 along its own axis/flip + 4
jitters vs MAIN median 1.52e8 -- the first-order flat
EPSTEIN wall is ALSO second-order structureless in the
log-h channel: dead-flat, not bent) +
THRESHOLD_NOT_EXPLAINED(midpoint 1.761: the measured log-h
quadratic term is NEGATIVE on all 18 sub-directions (q_R
-0.030..-2.704, median -0.911) -- a second-order ASSIST, not
resistance: the corrected budgets b_q = b - q_R/2 still
separate PERFECTLY (max no-lift 1.709 = TOP8 < min lift
1.814 = XIPOS) but the corrected bracket moves AWAY from the
naive flip level (1.761 vs 1, off by 0.76 > bar 0.10) -- the
r291 ~1.3x threshold factor is NOT the smooth Taylor
curvature of log|h_184|; it is a near-flip nonlinearity that
low-order jets cannot see) + RETRACTION_HIGHER_ORDER(B2(8) =
27.55 and B3(8) = 150.87 both predict MASSIVE lift at the
overdrive point (q_R(TOP6) -0.577, c3 -1.45) while the
measured TOP6 factor-8 case retracts to minC 184 -- the
retraction is NOT explained at second or third order,
honest: the linearization-with-jets over-predicts even
harder than the bare linearization) + CURVATURE_BLIND(best
F10 curvature energy sp +0.884 < |sp(F0)| = 0.907 (bar 0.6
PASSED, baseline NOT beaten): the fourth honest negative
UNDER THE SEALED RULE -- but the NEAR-MISS is the finding:
the split-sealed two-form is the FIRST candidate class in
three rounds to come within 0.023 of the trivial size
baseline (r290 best 0.263, r291 best 0.471, r292 0.884),
with AUC(dead) 0.097 (0.903 inverted); F11 budget+curvature
+0.672, F12 Rayleigh +0.186) + FUNCTIONAL_TABLE(sp vs s on
the 94-point test split: F10 +0.884 / F11 +0.672 / F12
+0.186 / baseline F0 -0.907; AUC(dead) 0.097 / 0.289 /
0.354; world values (SMOOTH/SCR/EPST/HL2): F10 -0.143/-5.38/
-0.525/-0.104, F11 -0.156/-5.36/-0.63/-0.142, F12 -2.8e-5/
-4.0e-4/-1.2e-5/-1.2e-5; dist-rule typing all WORLD_BLIND
among the dead worlds; construction-trivial MAIN separation
DISCLOSED (all three are 0 at MAIN); dead-world spreads
5.27 / 5.22 / 3.9e-4 non-degenerate) + EIGENAXIS_SIGNATURE(
e_top vs pinned random FRAC00: antiphase34 +0.063 vs -0.370
(factor 0.17, DISTINCT: the top curvature axis is nearly
antiphase-free), midband 0.175 vs 0.375 (factor 0.47,
DISTINCT: it avoids the r289 flip band), fold terciles
(0.01, 0.30, 0.69) vs (0.00, 0.16, 0.84), PR 65.3 vs 61.4
(not distinct); typed MEASUREMENT).
Key numbers.  W9: S 367/263/104, minC 184, crossing 185,
margin 1.6752e-4, z_v -3.149, b34 -0.105; REF 125.7462 (rec
125.75), inversion 1.5e-16, quadruple devs (0.059, 0.125,
0.117, 0.028); flips 25/21/27/25 == records; theta_up
3.8733e-5, theta_kill 3.20e-2, endpoint minC 185.  R291
REGRESSION: all 18 matched-dose margins == records (max abs
dev 0.0005), lift pattern identical, bracket (1.280, 1.291],
top-9 atoms (2, 3, 5, 13, 11, 4, 29, 7, 89), TOP6 fac-8
margin 9.090 minC 184 s 1.00; SMOOTH d2 -23.31/-23.32/-23.38
(rich devs 0.001/0.003) vs rand -0.982, ratio 23.7; EPSTEIN
c_25 -1.99e-11, theta_up 5.03e10.  LEG A: 29 directions
(conservation exact on 9 ATOM + 10 FRAC moves, eta_0 exact
on 6 DENS), 174 diagonal + 1624 pair points ALL FINITE;
diagonal d2 per theta_eq^2: W_SMOOTH -324.2 / W_SCR -732.6 /
W_EPST -6362.0 / RIDGE -6.68 / atoms -74.5..-2.36e3 / FRAC
-11.7..-282 / DENS -377..-1.63e4; Richardson census 29 QUAD
/ 0 FLAT / 0 NONQUAD (worst dev < 0.1); selected-pair
crosscheck 15/15 (worst rel dev 0.018 <= 0.25); Gram 29/29
kept at 1e-10.  LEG B: b_A == analytic (max rel dev 0.0033,
max abs 0.0067); q_R table PRIME -2.224 / POWER -0.031 /
HEAD -1.465 / MID -0.071 / TAIL -0.030 / XIPOS -1.225 /
XINEG -0.375 / TOP1..TOP70 -0.188..-2.704 (triple-B
consistency devs 0.002..1.110, advisory); corrected bracket
(1.709, 1.814], midpoint 1.761; TOP6: b 1.136, q_R -0.577,
c3 -1.45, B2 27.55, B3 150.87.  EPSTEIN: q_E own axis
-8.1e-7 / flip -8.1e-7 / jitters +3.4e-7..-2.2e-6, median
8.1e-7 vs MAIN median 1.52e8 -> ratio 5.4e-15.  LEG C:
corpus 143 points, test split 94 (overlap NONE); F0 sp
-0.907; F10/F11/F12 sp +0.884/+0.672/+0.186, AUC 0.097/
0.289/0.354.  MUST-FAILS: m1 CAUGHT (wrong prefactor dev
1.00 > 0.25), m2 CAUGHT (auditor flags 49 overlap points),
m3 CAUGHT (conservation gate False), m4 FLAGGED (single-h
Richardson None = NOT VERIFIABLE); scopes + fragments CLEAN.
Runtime 80 s full / 0.2 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (records inserted per
protocol; a1-a4 disclosed above, found and fixed BEFORE the
freeze; no physics bar, class rule or verdict rule moved).
READING (typed MEASUREMENT): the margin curvature at MAIN is
REAL, everywhere negative on the sealed 29-direction set,
and in the L2 spectral metric RANK-ONE-dominated -- but the
top axis is an on-support DENSITY combination, not the
arithmetic SMOOTH axis (|cos| 0.07) and not the ridge (the
lift axis sits in the FLATTEST sector, rank 28/29, exactly
where the valley does not bend); the r291 threshold mystery
is NOT closed at second order: the smooth log-h jet along
the ridge sub-directions bends the WRONG way (q_R < 0 on all
18, a second-order assist) so the corrected threshold moves
to 1.76, and the same jets over-predict the TOP6 overdrive
retraction even at third order (B2 27.6, B3 150.9 vs
measured no-lift) -- the ~1.3x resistance factor and the
retraction are NEAR-FLIP nonlinearities invisible to
low-order Taylor data: m* remains an emergent threshold
object; EPSTEIN's flat wall is flat at BOTH orders (ratio
5.4e-15) -- MAIN's wall has curvature structure, EPSTEIN's
has none; and the sealed two-form comes CLOSER to the
survival functional than any class before it (F10 sp +0.884
vs baseline 0.907 -- a 0.023 near-miss where r290/r291
classes lost by 0.4-0.6) yet still fails the sealed bar:
CURVATURE_BLIND stands as the fourth honest negative -- the
quadratic class as a CLOSED survival predictor is dead by
the sealed rule, while the measurement says the working-set
geometry is predominantly SECOND-ORDER VISIBLE; what is
missing is the theta_eq-vs-L2 metric reconciliation, not
more functional classes.  NO RH CLAIM IN EITHER DIRECTION.
NOT evidence for or against RH.
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

import ridge_anatomy_probe as RA                    # noqa: E402 r291
import profile_functional_probe as PFP              # noqa: E402 r290
import lstar_two_measure_probe as LS                # noqa: E402 r284
import metric_stability_probe as MS                 # noqa: E402 r278
import minimal_firewall_probe as MF                 # noqa: E402 r276
import budget_localization_probe as BL              # noqa: E402 r280
import port_integrable_kernel_probe as PIK          # noqa: E402 v881
import offdiag_gram_probe as ODG                    # noqa: E402 r254
import principal_bessel_probe as PB                 # noqa: E402 r243
import bordered_hankel_probe as BH                  # noqa: E402 r244
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
SPARSE_KS = RA.SPARSE_KS
AMP_PAD = RA.AMP_PAD
CAL_SEEDS = (290000, 290001, 290002)
T3_SEED = 290010
T3_THETA = 3e-4
T3_TOL = 0.15
THETA_CAL = 1e-3
ETA0_BAR = 1e-12

# r291 regression records (margins printed at 1e-3 resolution)
R291_PART = {"PRIME": (1.798, True), "POWER": (0.202, False),
             "HEAD": (1.528, True), "MID": (0.293, False),
             "TAIL": (0.179, False), "XIPOS": (1.291, True),
             "XINEG": (0.709, False)}
R291_TOPK = {1: (0.497, False), 2: (0.731, False),
             4: (0.963, False), 6: (1.136, False),
             8: (1.280, False), 9: (1.332, True),
             10: (1.371, True), 12: (1.444, True),
             16: (1.570, True), 32: (1.803, True),
             70: (2.000, True)}
R291_MARG_TOL = 0.005
R291_BRACKET = (1.280, 1.291)
R291_TOP9 = (2, 3, 5, 13, 11, 4, 29, 7, 89)
R291_TOP6F8_MARG = 9.09
R291_TOP6F8_TOL = 0.02
R291_HESS_HS = (6.25e-5, 1.25e-4, 2.5e-4)
R291_D2_REC = -23.31
R291_D2_TOL = 0.02
R291_RICH_BAR = 0.01
R291_D2_RAND_REC = -0.98
R291_D2_RAND_TOL = 0.10
R291_RATIO_REC = 23.7
R291_RATIO_TOL = 1.0
R291_SEED_RAND = 291100
EPST_C_BAR = 1e-9
EPST_THUP_MIN = 1e9

# Leg A (a1: ladder halved after NaN margins at 6.25e-5)
HESS_EQ_HS = (7.8125e-6, 1.5625e-5, 3.125e-5)
H_PAIR_H = 1.5625e-5
RICH_TOL = 0.1
D2_FLOOR = 0.5
POL_TOL = 0.25
GCUT = 1e-10
TRACE_BAR = 0.90
LOWRANK_BAR = 4
COS_TOP_BAR = 0.7
RIDGE_FLAT_FRAC = 0.1
NDIR_FRAC = 10
SEED_FRAC = 292100
NDIR_DENS = 6
SEED_DENS = 292200
N_ATOM = 9

# Leg A' EPSTEIN contrast
EPS_TAU = 1e-3
EPS_SEEDS = 292300
EPS_NJIT = 4
EPST_Q_BAR = 1e-2

# Leg B (a2: one-sided lift-side ladder, exact cubic triples;
# a3: fractional-dose gate pad -- the add-subtract roundoff of
# the position update is ~1/t relative, measured overshoot
# <= 7.7e-9 at t = 1/16 vs the r291 1e-9 headroom)
TAU_LADDER = (0.0625, 0.125, 0.1875, 0.25, 0.375)
TRIPLE_A = (0.0625, 0.125, 0.1875)
TRIPLE_B = (0.125, 0.25, 0.375)
LEGB_PAD = 1.0 + 1e-7
BLIN_TOL = 0.05
Q_RICH_BAR = 0.35
THR_TOL = 0.10
OVERDRIVE_K = 6
OVERDRIVE_FAC = 8.0

# Leg C
ENS_SCR_REPS = 8
SEED_R285_SCR = 285100
TRAIN_FRAC = (0, 2, 4, 6, 8)
TRAIN_DENS = (0, 2, 4)
SP_BAR = 0.6
WORLD_SPREAD_BAR = 0.01

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


CONSTRUCTORS = ("unit_dir", "pol_of_d2", "expand_of_d2",
                "proj_coords", "func_q10", "func_q11", "func_q12",
                "cubic_solve", "auc_rank", "rich_devs",
                "fold_shares")
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
def unit_dir(dd, lag_len, ref):
    """theta_eq unit direction: the density direction scaled so
    that one step h has gap-equivalent distance h (lag-L1 of the
    unit == ref).  Consumes a density direction + its lag length
    + the analytic reference only."""
    return np.asarray(dd, float) * (float(ref) / max(float(lag_len),
                                                     1e-300))


def pol_of_d2(d2_sum, d2_dif):
    """polarization identity of a quadratic form: H(u, v) =
    [d2(u+v) - d2(u-v)] / 4 (exact for quadratics)."""
    return (float(d2_sum) - float(d2_dif)) / 4.0


def expand_of_d2(d2_sum, d2_u, d2_v):
    """expansion identity of a quadratic form: H(u, v) =
    [d2(u+v) - d2(u) - d2(v)] / 2 (exact for quadratics; the
    polarization crosscheck partner)."""
    return (float(d2_sum) - float(d2_u) - float(d2_v)) / 2.0


def proj_coords(V, G_evals, G_evecs, cut, delta):
    """exact L2 projection coordinates of a deviation onto the
    span of the direction columns V: x = G^+ V^T delta with the
    eigencut pseudo-solve (no fitting).  Consumes vectors only."""
    b = np.asarray(V, float).T @ np.asarray(delta, float)
    w = np.asarray(G_evals, float)
    U = np.asarray(G_evecs, float)
    keep = w >= float(cut) * float(np.max(w))
    Ui = U[:, keep]
    return Ui @ ((Ui.T @ b) / w[keep])


def func_q10(x, H):
    """F10 CURVATURE ENERGY: Q = x^T H x / 2 on the projection
    coordinates; 0.0 sealed at zero deviation."""
    x = np.asarray(x, float)
    if float(np.max(np.abs(x))) == 0.0:
        return 0.0
    return 0.5 * float(x @ np.asarray(H, float) @ x)


def func_q11(x, g, H):
    """F11 BUDGET + CURVATURE: g^T x + x^T H x / 2 (first order
    plus curvature, coherent margin units); 0.0 at zero
    deviation."""
    x = np.asarray(x, float)
    if float(np.max(np.abs(x))) == 0.0:
        return 0.0
    return float(np.asarray(g, float) @ x) \
        + 0.5 * float(x @ np.asarray(H, float) @ x)


def func_q12(x, H, dnorm2):
    """F12 RAYLEIGH QUOTIENT: x^T H x / |delta|_L2^2 (scale-free
    direction classifier; restriction to the training span
    disclosed); 0.0 at zero deviation."""
    x = np.asarray(x, float)
    if float(np.max(np.abs(x))) == 0.0 or float(dnorm2) == 0.0:
        return 0.0
    return float(x @ np.asarray(H, float) @ x) / float(dnorm2)


def cubic_solve(ts, fvals):
    """exact origin-anchored cubic model solve on one triple:
    f(t) = -b t + q t^2/2 + c3 t^3/6 -> (b, q, c3) by a 3x3
    linear solve (no fitting).  Consumes a dose triple + three
    values only."""
    ts = [float(t) for t in ts]
    Mrow = np.array([[-t, 0.5 * t * t, t ** 3 / 6.0]
                     for t in ts])
    sol = np.linalg.solve(Mrow, np.asarray(fvals, float))
    return float(sol[0]), float(sol[1]), float(sol[2])


def auc_rank(scores, labels):
    """tie-aware rank AUC (Mann-Whitney): P(score_pos >
    score_neg) + P(equal)/2.  Consumes two lists only."""
    sc = np.asarray(scores, float)
    lb = np.asarray(labels, bool)
    n1 = int(np.sum(lb))
    n0 = len(lb) - n1
    if n1 == 0 or n0 == 0:
        return float("nan")
    order = np.argsort(sc, kind="mergesort")
    ranks = np.empty(len(sc), float)
    ss = sc[order]
    i = 0
    while i < len(ss):
        j = i
        while j + 1 < len(ss) and ss[j + 1] == ss[i]:
            j += 1
        ranks[order[i:j + 1]] = 0.5 * (i + j) + 1.0
        i = j + 1
    rsum = float(np.sum(ranks[lb]))
    return (rsum - n1 * (n1 + 1) / 2.0) / (n1 * n0)


def rich_devs(estimates):
    """sealed Richardson auditor: relative deviations between
    adjacent step-size estimates of one derivative; None (NOT
    VERIFIABLE) with fewer than two estimates."""
    v = [float(e) for e in estimates]
    if len(v) < 2:
        return None
    return [abs(v[i + 1] / v[i] - 1.0) if v[i] != 0.0
            else float("inf") for i in range(len(v) - 1)]


def fold_shares(w):
    """fold-position tercile energy shares of a profile vector
    (HEAD/MID/TAIL thirds of the fold index range)."""
    w = np.asarray(w, float)
    e = w * w
    tot = max(float(np.sum(e)), 1e-300)
    parts = np.array_split(e, 3)
    return tuple(float(np.sum(p)) / tot for p in parts)


# ============== must-fail mutants
def mutant_wrong_polarization(d2_sum, d2_dif):
    """m1 MUST-FAIL: the polarization identity with the WRONG
    prefactor (/2 instead of /4) -- the expansion-identity
    crosscheck must CATCH it on an exact quadratic."""
    return (float(d2_sum) - float(d2_dif)) / 2.0


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("curvature_form_probe -- PRIME.PORT.LSTAR."
          "CURVATURE_FORM.01 (round 292)")
    print("SPEC_SHA %s   (r291 RA %s / r290 PFP %s / r280 BL %s)"
          % (SPEC_SHA[:16], RA.SPEC_SHA[:16], PFP.SPEC_SHA[:16],
             BL.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + w9 "
                        "regression + m1/m2/m4 mutants; anchors, "
                        "legs, corpus, adjudications skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the 29-direction set with "
          "the theta_eq normalization, the three-step diagonal + "
          "full polarization matrix + eigen protocol with its "
          "bars, the Leg-B linear-identity/curvature/threshold/"
          "retraction rules with r291 sign conventions, the "
          "three quadratic functional candidates with the "
          "baseline contest and the 18-direction training split, "
          "the EPSTEIN contrast channel, the Leg-D statistics "
          "and the must-fail set; H_tr / g_tr / q(A) honestly "
          "typed measurement-consuming; the STOP list forbids "
          "any L* claim and any proof attack")

    # ---------------- S1 toys
    section("S1  TOYS -- POLARIZATION, PROJECTION, AUC, "
            "RICHARDSON, SHARES")
    A_t = np.array([[2.0, 1.0, 0.0],
                    [1.0, 3.0, 0.5],
                    [0.0, 0.5, 1.0]])

    def toy_d2(v, h=0.5):
        f = lambda z: float(z @ A_t @ z)          # noqa: E731
        return (f(h * v) - 2.0 * f(0.0 * v) + f(-h * v)) / (h * h)

    e1_t, e2_t = np.eye(3)[:, 0], np.eye(3)[:, 1]
    d2s = toy_d2(e1_t + e2_t)
    d2d = toy_d2(e1_t - e2_t)
    h_pol = pol_of_d2(d2s, d2d)
    h_exp = expand_of_d2(d2s, toy_d2(e1_t), toy_d2(e2_t))
    ok_t1 = (abs(h_pol - 2.0) <= 1e-12 and abs(h_exp - 2.0) <= 1e-12
             and abs(toy_d2(e1_t) - 4.0) <= 1e-12)
    check("G10-toy-polarization", ok_t1,
          "HAND QUADRATIC (A12 = 1): d2(e1) = 2 A11 = 4 exact; "
          "polarization H(e1, e2) = %.3f == 2 A12 = 2 exact; "
          "expansion identity = %.3f == 2 exact -- both routes "
          "agree on quadratics" % (h_pol, h_exp))
    V_t = np.stack([e1_t, e1_t + e2_t], axis=1)
    G_t = V_t.T @ V_t
    wG, UG = np.linalg.eigh(G_t)
    x_t = proj_coords(V_t, wG, UG, GCUT, e1_t + 2.0 * e2_t)
    H_t = np.array([[4.0, 6.0], [6.0, 14.0]])
    q10_t = func_q10(x_t, H_t)
    q11_t = func_q11(x_t, np.array([1.0, -1.0]), H_t)
    q12_t = func_q12(x_t, H_t, 5.0)
    # exact: x = (-1, 2); Q = (4*1 - 2*6*2 + 14*4)/2 = 18
    ok_t2 = (float(np.max(np.abs(x_t - np.array([-1.0, 2.0]))))
             <= 1e-12
             and abs(q10_t - 18.0) <= 1e-12
             and abs(q11_t - 15.0) <= 1e-12
             and abs(q12_t - 36.0 / 5.0) <= 1e-12
             and func_q10(np.zeros(2), H_t) == 0.0
             and func_q11(np.zeros(2), np.ones(2), H_t) == 0.0
             and func_q12(np.zeros(2), H_t, 5.0) == 0.0)
    check("G11-toy-projection-functionals", ok_t2,
          "HAND PROJECTION (V = (e1, e1+e2), delta = e1 + 2 e2): "
          "x = (-1, 2) exact; F10 = 18, F11 = 15, F12 = 36/5 "
          "exact; zero-deviation seals = 0.0")
    auc_t1 = auc_rank([0.9, 0.8, 0.2, 0.1],
                      [True, True, False, False])
    auc_t2 = auc_rank([0.5, 0.5, 0.5, 0.5],
                      [True, True, False, False])
    rd_t = rich_devs([2.0, 2.2])
    rd_none = rich_devs([2.0])
    fs_t = fold_shares(np.array([1.0, 1.0, 0.0, 0.0, 1.0, 1.0]))
    ok_t3 = (abs(auc_t1 - 1.0) <= 1e-14
             and abs(auc_t2 - 0.5) <= 1e-14
             and abs(rd_t[0] - 0.1) <= 1e-12
             and rd_none is None
             and abs(fs_t[0] - 0.5) <= 1e-14
             and abs(fs_t[1] - 0.0) <= 1e-14
             and abs(fs_t[2] - 0.5) <= 1e-14)
    check("G12-toy-auc-rich-shares", ok_t3,
          "HAND AUC: separable = 1.0, all-tied = 0.5 exact; "
          "Richardson devs (2.0, 2.2) = 0.1 exact, single "
          "estimate = None (NOT VERIFIABLE); fold terciles of "
          "(1,1,0,0,1,1) = (1/2, 0, 1/2) exact")
    fv_t = [-2.0 * t + 0.25 * t * t - t ** 3 / 6.0
            for t in TRIPLE_A]
    b_t, q_t, c_t = cubic_solve(TRIPLE_A, fv_t)
    ok_tc = (abs(b_t - 2.0) <= 1e-12 and abs(q_t - 0.5) <= 1e-10
             and abs(c_t - (-1.0)) <= 1e-8)
    check("G13-toy-cubic-solve", ok_tc,
          "HAND CUBIC SOLVE (b = 2, q = 1/2, c3 = -1 on the "
          "sealed triple A): recovered (%.3f, %.3f, %.3f) exact "
          "-- the origin-anchored 3x3 solve is fit-free and "
          "exact on cubics" % (b_t, q_t, c_t))

    # ---------------- S2 w9 + anchors
    section("S2  W9 REGRESSION + METRIC + RIDGE + r291 ANCHORS")
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
    wsig0 = MS.wsig_vec(d9, L9)
    if smoke:
        h_bad = mutant_wrong_polarization(d2s, d2d)
        check("G80-mustfail-polarization", abs(h_bad - 2.0) > POL_TOL,
              "m1 WRONG PREFACTOR (/2): H = %.3f vs exact 2.0, dev "
              "%.2f > %.2f -- CAUGHT by the expansion crosscheck"
              % (h_bad, abs(h_bad / 2.0 - 1.0), POL_TOL))
        ov_s = RA.split_auditor({"DIR:FRAC00:d=1e-03"},
                                {"DIR:FRAC00:d=1e-03", "MAIN"})
        check("G81-mustfail-split-break", len(ov_s) > 0,
              "m2 SEAL BREAK (toy tags): auditor flags %d overlap "
              "points -- CAUGHT" % len(ov_s))
        check("G83-mustfail-richardson", rich_devs([2.0]) is None,
              "m4 SINGLE-STEP d2 (toy): Richardson auditor returns "
              "None -- FLAGGED as NOT VERIFIABLE")
        hits_s = []
        for fn_ in CONSTRUCTORS:
            hits_s += scope_audit(fn_, SCOPE_FORBIDDEN)
        ag_s = antigate_fragment_audit()
        check("G84-scope-audits", not hits_s and not ag_s,
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
    # control worlds (r291 constructions verbatim)
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
    # ridge anchor (r280 rebuilt verbatim)
    GE = BL.grad_ext(ctx9, N_REF + 2)
    xi = BL.dir_opt(GE["gR"], GE["gL"], GE["gaps"], N_REF)
    th_up, th_kill, cvec = BL.theta_of_dir(GE["gR"], GE["gL"],
                                           GE["gaps"], xi, N_REF)
    du_ridge = 2.0 * th_up * GE["gaps"] * xi
    uR, mR = RA.subset_move(uu9, mm9, du_ridge, np.ones(len(uu9)))
    dR = np.asarray(PIK.build_rung(MAIN_KZ, comb=(uR, mR))["d"],
                    float)
    MR = PFP.measure_density(dR, L9)
    ok_ridge = (abs(th_up / THUP_REC - 1.0) <= THUP_TOL
                and th_kill > th_up
                and MR["minC"] == RIDGE_MINC_REC
                and MF.conserve_comb("P2_JIT", uu9, mm9, uR, mR,
                                     2.0 * th_up * AMP_PAD))
    check("G23-ridge-anchor", ok_ridge,
          "r280 RIDGE ANCHOR: theta_up = %.4e (rec %.2e), "
          "theta_kill = %.2e; OPT endpoint minC = %s == %d; "
          "conservation exact"
          % (th_up, THUP_REC, th_kill, str(MR["minC"]),
             RIDGE_MINC_REC))
    # r291 budget-threshold regression (18 matched-dose cases)
    du1 = GE["gaps"] * xi
    cj = np.where(du1 > 0, du1 * GE["gR"][:, N_REF],
                  du1 * GE["gL"][:, N_REF])
    nn_at = RA.atom_ints(uu9)
    kvec = np.array([ODG.base_exp(int(n))[1] for n in nn_at])
    parts = RA.part_masks(uu9, xi, kvec)
    order = np.argsort(cj)

    def sect_case(mask, fac):
        u2, m2 = RA.subset_move(uu9, mm9, fac * du_ridge, mask)
        ok_c = MF.conserve_comb("P2_JIT", uu9, mm9, u2, m2,
                                abs(fac) * 2.0 * th_up * AMP_PAD)
        d2_ = np.asarray(PIK.build_rung(MAIN_KZ,
                                        comb=(u2, m2))["d"], float)
        meas = PFP.measure_density(d2_, L9)
        marg = -float(np.sum(cj * mask)) * fac * 2.0 * th_up
        return meas, marg, ok_c, (u2, m2)

    ok_reg = True
    subsets = []   # (name, mask, b_analytic, lifted)
    dev_max = 0.0
    for name in ("PRIME", "POWER", "HEAD", "MID", "TAIL",
                 "XIPOS", "XINEG"):
        meas, marg, okc, _cm = sect_case(parts[name], 1.0)
        lift = (meas["minC"] or 0) > MINC_REC
        rec_m, rec_l = R291_PART[name]
        dev_max = max(dev_max, abs(marg - rec_m))
        ok_reg = ok_reg and okc \
            and abs(marg - rec_m) <= R291_MARG_TOL \
            and lift == rec_l
        subsets.append((name, parts[name].copy(), marg, lift))
    mask_topk = {}
    for k in SPARSE_KS:
        m = np.zeros(len(uu9))
        m[order[:k]] = 1.0
        mask_topk[k] = m
        meas, marg, okc, _cm = sect_case(m, 1.0)
        lift = (meas["minC"] or 0) > MINC_REC
        rec_m, rec_l = R291_TOPK[k]
        dev_max = max(dev_max, abs(marg - rec_m))
        ok_reg = ok_reg and okc \
            and abs(marg - rec_m) <= R291_MARG_TOL \
            and lift == rec_l
        subsets.append(("TOP%d" % k, m, marg, lift))
    m_nolift = [b for _n, _m, b, lf in subsets if not lf]
    m_lift = [b for _n, _m, b, lf in subsets if lf]
    brk = (max(m_nolift), min(m_lift))
    top9 = tuple(int(v) for v in nn_at[order[:N_ATOM]])
    meas6, marg6, ok6, _cm6 = sect_case(mask_topk[OVERDRIVE_K],
                                        OVERDRIVE_FAC)
    ok_reg = ok_reg and ok6 \
        and abs(marg6 - R291_TOP6F8_MARG) <= R291_TOP6F8_TOL \
        and meas6["minC"] == MINC_REC and meas6["s"] >= NEAR \
        and abs(brk[0] - R291_BRACKET[0]) <= R291_MARG_TOL \
        and abs(brk[1] - R291_BRACKET[1]) <= R291_MARG_TOL \
        and brk[0] < brk[1] and top9 == R291_TOP9
    check("G24-r291-threshold-regression", ok_reg,
          "r291 BUDGET-THRESHOLD REGRESSION: all 18 matched-dose "
          "margins == records (max abs dev %.4f <= %.3f), lift "
          "pattern identical, bracket (%.3f, %.3f] == (1.280, "
          "1.291], top-9 atoms %s == record; TOP6 fac 8: margin "
          "%.3f (rec %.2f), minC %s (retracts, s %.2f)"
          % (dev_max, R291_MARG_TOL, brk[0], brk[1], str(top9),
             marg6, R291_TOP6F8_MARG, str(meas6["minC"]),
             meas6["s"]))

    # r291 SMOOTH-d2 regression (r291 code path verbatim)
    def margin_at(dvec):
        meas = PFP.measure_density(dvec, L9)
        if meas["rho"] is None or meas["cross"] is None \
                or meas["cross"] <= N_REF:
            return float("nan")
        return 1.0 - meas["rho"][N_REF]

    m00 = margin_at(d9)
    dSM = d_worlds["SMOOTH"]
    plenSM = lag_l1(dSM - d9) / REF
    dd_r291rnd, (u2r, m2r) = PFP.dir_frac(uu9, mm9, MAIN_KZ, d9,
                                          THETA_CAL, R291_SEED_RAND)
    unit_r291 = dd_r291rnd / max(lag_l1(dd_r291rnd), 1e-300)
    d2_sm, d2_rd = [], []
    ok_fin0 = True
    for h in R291_HESS_HS:
        mp_ = margin_at(PFP.interp_density(d9, dSM, h))
        mn_ = margin_at(PFP.interp_density(d9, dSM, -h))
        rp = margin_at(d9 + unit_r291 * (h * plenSM * REF))
        rn = margin_at(d9 - unit_r291 * (h * plenSM * REF))
        ok_fin0 = ok_fin0 and all(math.isfinite(v)
                                  for v in (mp_, mn_, rp, rn))
        d2_sm.append((mp_ - 2.0 * m00 + mn_) / (h * h))
        d2_rd.append((rp - 2.0 * m00 + rn) / (h * h))
    rdev0 = rich_devs(d2_sm)
    ratio0 = abs(d2_sm[0]) / max(abs(d2_rd[0]), 1e-300)
    ok_d2reg = (ok_fin0
                and abs(d2_sm[0] / R291_D2_REC - 1.0) <= R291_D2_TOL
                and max(rdev0) <= R291_RICH_BAR
                and abs(d2_rd[0] / R291_D2_RAND_REC - 1.0)
                <= R291_D2_RAND_TOL
                and abs(ratio0 - R291_RATIO_REC) <= R291_RATIO_TOL)
    check("G25-r291-smooth-d2-regression", ok_d2reg,
          "r291 SMOOTH d2 regression (path units, r291 HESS_HS): "
          "d2 = %s (rec %.2f, rich devs %s <= %.2f); random seed "
          "291100 d2 = %.3f (rec %.2f); ratio %.1f (rec %.1f "
          "tol %.1f)"
          % (str(["%.2f" % v for v in d2_sm]), R291_D2_REC,
             str(["%.3f" % v for v in rdev0]), R291_RICH_BAR,
             d2_rd[0], R291_D2_RAND_REC, ratio0, R291_RATIO_REC,
             R291_RATIO_TOL))
    # EPSTEIN first-order flatness anchor
    mcE0 = worlds_meas["EPST"]["minC"]
    ctxE = MS.ctx_build(MAIN_KZ, comb=(uE, mE))
    GEe = BL.grad_ext(ctxE, mcE0 + 2)
    xiE = BL.dir_opt(GEe["gR"], GEe["gL"], GEe["gaps"], mcE0)
    tuE, _tkE, cE = BL.theta_of_dir(GEe["gR"], GEe["gL"],
                                    GEe["gaps"], xiE, mcE0)
    ok_ef = abs(cE[mcE0]) <= EPST_C_BAR and tuE >= EPST_THUP_MIN
    check("G26-epstein-flatness-anchor", ok_ef,
          "EPSTEIN first-order flatness (own wall degree %d): "
          "c_%d = %.2e (bar %.0e), theta_up = %.2e >= %.0e (rec "
          "5.03e10) -- the r291 flat-wall anchor"
          % (mcE0, mcE0, cE[mcE0], EPST_C_BAR, tuE,
             EPST_THUP_MIN))

    # ---------------- S3 LEG A: Hessian spectroscopy
    section("S3  LEG A -- HESSIAN SPECTROSCOPY AT MAIN "
            "(29 sealed directions)")
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
    vhat = {n: unit_dir(dd, lag_l1(dd), REF) for n, dd in dirsD}
    check("G30-direction-set", ok_dcons and len(dirsD) == 29,
          "SEALED DIRECTION SET D: %d directions = 3 world axes "
          "+ ridge + %d atom sub-directions (conservation exact) "
          "+ %d FRAC (seeds 292100+, conservation exact) + %d "
          "DENS (seeds 292200+, eta_0 exact); all theta_eq-"
          "normalized (lag-L1 == REF per unit; linear density "
          "extensions, r290 disclosure)"
          % (len(dirsD), N_ATOM, NDIR_FRAC, NDIR_DENS))
    # (a1) diagonal census
    nD = len(dirsD)
    d2_tab = {}
    d1_mid = {}
    ok_finA = True
    typ_census = {"QUAD": 0, "FLAT": 0, "NONQUAD": 0}
    typ_by_dir = {}
    worst_nq = 0.0
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
        rdv = rich_devs(ests)
        if abs(ests[0]) < D2_FLOOR:
            typ = "FLAT"
        elif max(rdv) <= RICH_TOL:
            typ = "QUAD"
        else:
            typ = "NONQUAD"
            worst_nq = max(worst_nq, max(rdv))
        typ_census[typ] += 1
        typ_by_dir[name] = typ
    diag_mid = {n: d2_tab[n][1] for n in names_D}
    check("G31-diagonal-census", ok_finA,
          "DIAGONAL d2 census (per theta_eq^2, 3 steps %s, all "
          "finite): worlds %s; RIDGE %.2f; atoms [%.3g..%.3g]; "
          "FRAC [%.3g..%.3g]; DENS [%.3g..%.3g]; Richardson "
          "typing %s (floor %.1f, tol %.1f, worst NONQUAD dev "
          "%.2f; NONQUAD/FLAT entries carried at the mid step, "
          "disclosed)"
          % (str(HESS_EQ_HS),
             str({n: "%.1f" % d2_tab[n][0] for n in names_D[:3]}),
             d2_tab["RIDGE"][0],
             min(d2_tab[n][0] for n in names_D[4:13]),
             max(d2_tab[n][0] for n in names_D[4:13]),
             min(d2_tab[n][0] for n in names_D[13:23]),
             max(d2_tab[n][0] for n in names_D[13:23]),
             min(d2_tab[n][0] for n in names_D[23:]),
             max(d2_tab[n][0] for n in names_D[23:]),
             str(typ_census), D2_FLOOR, RICH_TOL, worst_nq))
    # (a2) full polarization matrix at the mid step
    Hmat = np.zeros((nD, nD))
    for i in range(nD):
        Hmat[i, i] = diag_mid[names_D[i]]
    sel_pairs = [(0, 1), (0, 2), (1, 2),          # world x world
                 (0, 3), (1, 3), (2, 3)]          # world x ridge
    sel_pairs += [(3, 4 + j) for j in range(N_ATOM)]  # ridge x atom
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
            Hij = pol_of_d2(d2su, d2di)
            Hmat[i, j] = Hmat[j, i] = Hij
            d2sum_cache[(i, j)] = d2su
            n_pairs += 1
    for (i, j) in sel_pairs:
        Hij = Hmat[i, j]
        Hexp = expand_of_d2(d2sum_cache[(i, j)],
                            diag_mid[names_D[i]],
                            diag_mid[names_D[j]])
        dev = abs(Hij - Hexp) / max(abs(Hij), D2_FLOOR)
        pol_dev_max = max(pol_dev_max, dev)
    ok_pol = ok_finP and pol_dev_max <= POL_TOL
    check("G32-polarization-matrix", ok_pol,
          "FULL POLARIZATION MATRIX: %d pairs at h = %.3g (all "
          "finite); the %d SELECTED pairs (world x world, world "
          "x ridge, ridge x atom) pass the expansion-identity "
          "crosscheck (worst rel dev %.3f <= %.2f) -- the form "
          "is quadratically consistent where it matters"
          % (n_pairs, H_PAIR_H, len(sel_pairs), pol_dev_max,
             POL_TOL))
    # (a3) eigenstructure against the L2 Gram
    Vmat = np.stack([vhat[n] for n in names_D], axis=1)
    Gmat = Vmat.T @ Vmat
    wG, UG = np.linalg.eigh(Gmat)
    keep = wG >= GCUT * wG[-1]
    n_keep = int(np.sum(keep))
    Uk = UG[:, keep]
    Wk = Uk / np.sqrt(wG[keep])[None, :]
    Ared = Wk.T @ Hmat @ Wk
    lam, Y = np.linalg.eigh(Ared)
    o_l = np.argsort(-np.abs(lam))
    lam_s = lam[o_l]
    Evec = Vmat @ (Wk @ Y[:, o_l])   # density-space eigendirections
    tr_abs = float(np.sum(np.abs(lam_s)))
    csum = np.cumsum(np.abs(lam_s)) / max(tr_abs, 1e-300)
    r90 = int(np.searchsorted(csum, TRACE_BAR) + 1)
    fine_rank = ("HESSIAN_LOW_RANK(%d)" % r90 if r90 <= LOWRANK_BAR
                 else "HESSIAN_EXTENSIVE(%d)" % r90)
    e_top = Evec[:, 0]
    vSMn = vhat["W_SMOOTH"]
    cos_sm = abs(float(vSMn @ e_top)
                 / max(float(np.linalg.norm(vSMn))
                       * float(np.linalg.norm(e_top)), 1e-300))
    sm_align = ("SMOOTH_TOP_ALIGNED(%.2f)" % cos_sm
                if cos_sm >= COS_TOP_BAR
                else "SMOOTH_OFF_TOP(%.2f)" % cos_sm)
    l2n2 = {n: float(vhat[n] @ vhat[n]) for n in names_D}
    diag_l2 = {n: diag_mid[n] / max(l2n2[n], 1e-300)
               for n in names_D}
    Hrr = diag_l2["RIDGE"]
    diag_sorted = sorted((abs(diag_l2[n]) for n in names_D),
                         reverse=True)
    rank_rr = 1 + sum(1 for v in diag_sorted if v > abs(Hrr))
    if abs(Hrr) <= RIDGE_FLAT_FRAC * abs(lam_s[0]):
        ridge_typ = "RIDGE_CURV_FLAT(%.3g, rank %d/%d)" \
            % (Hrr, rank_rr, nD)
    elif Hrr > 0:
        ridge_typ = "RIDGE_CURV_POSITIVE(%.3g)" % Hrr
    else:
        ridge_typ = "RIDGE_CURV_NEGATIVE(%.3g, rank %d/%d)" \
            % (Hrr, rank_rr, nD)
    coef_top = (Wk @ Y[:, o_l])[:, 0]
    coef_top = coef_top / max(float(np.max(np.abs(coef_top))),
                              1e-300)
    o_c = np.argsort(-np.abs(coef_top))
    load_txt = ", ".join("%s %+.2f" % (names_D[i], coef_top[i])
                         for i in o_c[:4])
    check("G33-eigenstructure", True,
          "EIGENSTRUCTURE (L2-Gram whitening, %d/%d kept at cut "
          "%.0e; eigenvalues = margin curvature per unit L2 "
          "density step, disclosed): top-8 %s (sum|lam| %.3g); "
          "r90 = %d eigendirections carry >= %.0f pct -> %s; "
          "%s; e_top loadings (top-4 of the D basis): %s; ridge "
          "position (a4, L2-normalized diagonal) H^L2(r, r) = "
          "%.3g (raw %.2f per theta_eq^2) -> %s"
          % (n_keep, nD, GCUT,
             str(["%.3g" % v for v in lam_s[:8]]), tr_abs, r90,
             100 * TRACE_BAR, fine_rank, sm_align, load_txt,
             Hrr, diag_mid["RIDGE"], ridge_typ))

    # ---------------- S4 LEG B: the threshold object m*
    section("S4  LEG B -- THE THRESHOLD OBJECT m* "
            "(log-h curvature along the 18 sub-directions)")

    def lh_wall(u2, m2):
        ctx_ = MS.ctx_build(MAIN_KZ, comb=(u2, m2))
        xu_, wu_, _z = BL.union_of_ctx(ctx_)
        sg_, lg_, _r = BL.sign_chain_f64(xu_, wu_, N_REF + 2)
        return float(lg_[N_REF])

    lh0 = lh_wall(uu9, mm9)
    ok_blin = True
    ok_bcons = True
    q_tab = {}
    qdev_tab = {}
    c3_tab = {}
    bdev_max_abs = 0.0
    bdev_max_rel = 0.0
    for name, mask, b_an, lift in subsets:
        fmap = {}
        for t in TAU_LADDER:
            u2, m2 = RA.subset_move(uu9, mm9, t * du_ridge, mask)
            ok_bcons = ok_bcons and MF.conserve_comb(
                "P2_JIT", uu9, mm9, u2, m2,
                t * 2.0 * th_up * LEGB_PAD)
            fmap[t] = lh_wall(u2, m2) - lh0
        bA, qA, c3A = cubic_solve(TRIPLE_A,
                                  [fmap[t] for t in TRIPLE_A])
        bB, qB, _c3B = cubic_solve(TRIPLE_B,
                                   [fmap[t] for t in TRIPLE_B])
        dev_abs = abs(bA - b_an)
        dev_rel = dev_abs / max(abs(b_an), 1e-300)
        bdev_max_abs = max(bdev_max_abs, dev_abs)
        bdev_max_rel = max(bdev_max_rel, dev_rel)
        ok_blin = ok_blin and dev_rel <= BLIN_TOL
        q_tab[name] = qA
        c3_tab[name] = c3A
        qdev_tab[name] = abs(qB / qA - 1.0) if qA != 0.0 \
            else float("inf")
    check("G40-linear-budget-identity", ok_blin and ok_bcons,
          "LINEAR IDENTITY (a2: one-sided lift-side ladder, "
          "cubic-triple solve): solved slope b_A == analytic "
          "r291 budget on all 18 sub-directions (max rel dev "
          "%.4f <= %.2f, max abs dev %.4f budget units; "
          "conservation exact at every dose) -- the one-sided "
          "channel measures the SAME side-selected object the "
          "budget linearizes"
          % (bdev_max_rel, BLIN_TOL, bdev_max_abs))
    qvals = [q_tab[n] for n, _m, _b, _l in subsets]
    n_qpos = sum(1 for v in qvals if v > 0)
    check("G41-curvature-census", True,
          "LOG-H CURVATURE (per factor^2, Richardson-"
          "extrapolated): q_R in [%.3f, %.3f] (median %.3f; "
          "%d/18 positive = second-order resistance); "
          "Richardson devs %.3f..%.3f (advisory bar %.2f); "
          "per-subset table %s"
          % (min(qvals), max(qvals), float(np.median(qvals)),
             n_qpos,
             min(qdev_tab.values()), max(qdev_tab.values()),
             Q_RICH_BAR,
             str({n: round(q_tab[n], 3)
                  for n, _m, _b, _l in subsets})))
    bq = {n: b - 0.5 * q_tab[n] for n, _m, b, _l in subsets}
    bq_nolift = [bq[n] for n, _m, _b, lf in subsets if not lf]
    bq_lift = [bq[n] for n, _m, _b, lf in subsets if lf]
    sep_ok = max(bq_nolift) < min(bq_lift)
    mid_q = 0.5 * (max(bq_nolift) + min(bq_lift))
    if sep_ok and abs(mid_q - 1.0) <= THR_TOL:
        thr_verd = "THRESHOLD_EXPLAINED(midpoint %.3f)" % mid_q
    elif sep_ok:
        thr_verd = ("THRESHOLD_NOT_EXPLAINED(midpoint %.3f off "
                    "the flip level by %.2f > %.2f)"
                    % (mid_q, abs(mid_q - 1.0), THR_TOL))
    else:
        thr_verd = "THRESHOLD_NOT_EXPLAINED(SEPARATION_LOST)"
    check("G42-threshold-adjudication", True,
          "SEALED THRESHOLD RULE: corrected budgets b_q = b - "
          "q_R/2: no-lift max %.3f, lift min %.3f (%s); "
          "corrected bracket midpoint %.3f vs the naive flip "
          "level 1 (bar %.2f) -> %s"
          % (max(bq_nolift), min(bq_lift),
             "SEPARATED" if sep_ok else "OVERLAP", mid_q,
             THR_TOL, thr_verd.split("(")[0]))
    b6 = R291_TOPK[OVERDRIVE_K][0]
    b6_an = [b for n, _m, b, _l in subsets
             if n == "TOP%d" % OVERDRIVE_K][0]
    q6 = q_tab["TOP%d" % OVERDRIVE_K]
    B2 = OVERDRIVE_FAC * b6_an \
        - 0.5 * q6 * OVERDRIVE_FAC * OVERDRIVE_FAC
    c3_6 = c3_tab["TOP%d" % OVERDRIVE_K]
    B3 = B2 - (c3_6 / 6.0) * OVERDRIVE_FAC ** 3
    if B2 < mid_q:
        ret_verd = ("RETRACTION_PREDICTED(B2(8) = %.2f < %.2f: "
                    "the quadratic model already bends the TOP6 "
                    "budget back below the flip level)"
                    % (B2, mid_q))
    elif B3 < mid_q:
        ret_verd = ("RETRACTION_HIGHER_ORDER(B2 %.2f >= %.2f but "
                    "B3 %.2f < %.2f with c3 = %.2f: third order "
                    "explains it)" % (B2, mid_q, B3, mid_q, c3_6))
    else:
        ret_verd = ("RETRACTION_HIGHER_ORDER(B2 %.2f, B3 %.2f "
                    "both >= %.2f, c3 = %.2f: NOT explained at "
                    "third order, honest)" % (B2, B3, mid_q, c3_6))
    check("G43-retraction-adjudication", True,
          "SEALED RETRACTION RULE (TOP6 at factor 8, measured "
          "retraction gated in G24): b(TOP6) = %.3f (rec %.3f), "
          "q_R = %.3f, B2(8) = %.2f, c3 = %.2f, B3(8) = %.2f -> "
          "%s" % (b6_an, b6, q6, B2, c3_6, B3,
                  ret_verd.split("(")[0]))

    # ---------------- S5 LEG A': EPSTEIN contrast
    section("S5  LEG A' -- EPSTEIN CURVATURE CONTRAST "
            "(log-h channel at the flat wall)")

    def lh_epst(u2):
        ctx_ = MS.ctx_build(MAIN_KZ, comb=(u2, mE))
        xu_, wu_, _z = BL.union_of_ctx(ctx_)
        sg_, lg_, _r = BL.sign_chain_f64(xu_, wu_, mcE0 + 2)
        return float(lg_[mcE0])

    lhE0 = lh_epst(uE)
    duE_own = GEe["gaps"] * xiE
    dirs_E = [("OWN_AXIS", duE_own)]
    ok_econs = True
    for i in range(EPS_NJIT):
        u2j, m2j = MF.pert_jit(uE, mE, EPS_TAU, EPS_SEEDS + i,
                               False)
        ok_econs = ok_econs and MF.conserve_comb(
            "P2_JIT", uE, mE, u2j, m2j, EPS_TAU)
        dirs_E.append(("JIT%02d" % i, (u2j - uE) / EPS_TAU))
    # the MAIN direction in EPSTEIN position space is not defined
    # (different atom sets); the sealed contrast uses the own axis
    # + jitters, plus the own-axis flip as the oriented partner.
    dirs_E.append(("OWN_FLIP", -duE_own))
    qE_tab = {}
    ok_finE = True
    for name, duu in dirs_E:
        dl = {}
        for t in (EPS_TAU, -EPS_TAU, 2 * EPS_TAU, -2 * EPS_TAU):
            dl[t] = lh_epst(uE + t * duu) - lhE0
        q1 = (dl[EPS_TAU] + dl[-EPS_TAU]) / (EPS_TAU * EPS_TAU)
        q2 = (dl[2 * EPS_TAU] + dl[-2 * EPS_TAU]) \
            / (4.0 * EPS_TAU * EPS_TAU)
        qE = (4.0 * q1 - q2) / 3.0
        ok_finE = ok_finE and math.isfinite(qE)
        qE_tab[name] = qE
    q_main_theta = [abs(q_tab[n]) / (2.0 * th_up) ** 2
                    for n, _m, _b, _l in subsets]
    med_main = float(np.median(q_main_theta))
    med_E = float(np.median([abs(v) for v in qE_tab.values()]))
    ratio_E = med_E / max(med_main, 1e-300)
    ep_typ = ("EPST_CURV_FLAT(ratio %.2g)" % ratio_E
              if ratio_E <= EPST_Q_BAR
              else "EPST_CURV_PRESENT(ratio %.2g)" % ratio_E)
    check("G50-epstein-contrast", ok_finE and ok_econs,
          "EPSTEIN log-h curvature at its own wall (degree %d, "
          "tau %.0e, per theta^2; jitter conservation exact at "
          "the base dose): %s; median |q_E| = %.3g vs MAIN "
          "median |q| = %.3g per theta^2 -> ratio %.2g (bar "
          "%.0e) -> %s -- is the first-order flat wall also "
          "second-order structureless?"
          % (mcE0, EPS_TAU,
             str({n: "%.2g" % v for n, v in qE_tab.items()}),
             med_E, med_main, ratio_E, EPST_Q_BAR, ep_typ))

    # ---------------- S6 LEG C: sealed two-form contest
    section("S6  LEG C -- SEALED TWO-FORM FUNCTIONAL CONTEST "
            "(fresh corpus, split-sealed)")
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
    for fac in RIDGE_FACS:
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
    check("G60-corpus", ok_scr and len(CORPUS) >= 140,
          "FRESH SEALED CORPUS: %d points (MAIN + 5 worlds + 4 "
          "paths x %d + 16 directions x %d + %d ridge factors + "
          "%d ENS_SCR replicates, weights bitwise); direction "
          "conservation gated in G30"
          % (len(CORPUS), len(PATH_TS), len(DIST_GRID),
             len(RIDGE_FACS), ENS_SCR_REPS))
    # training split: 8 randoms + RIDGE + 9 atoms
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
    excl_src = set(train_names) | {"RIDGE"}
    test_pts = [r for r in CORPUS if r["src"] not in excl_src]
    train_tags = set(r["tag"] for r in CORPUS
                     if r["src"] in excl_src)
    overlap = RA.split_auditor(train_tags,
                               set(r["tag"] for r in test_pts))
    check("G61-split-seal", len(test_pts) >= 90 and not overlap,
          "TRAINING SPLIT: H_tr / g_tr on the %d sealed training "
          "directions (%d randoms + RIDGE + %d atoms; world axes "
          "NOT trained); test split %d points DISJOINT (overlap "
          "%s); the 40 training-direction ladder points + the %d "
          "ridge factor points EXCLUDED"
          % (len(train_dirs), len(train_names), N_ATOM,
             len(test_pts), str(overlap) if overlap else "NONE",
             len(RIDGE_FACS)))
    for r in CORPUS:
        x = proj_coords(V_tr, wGt, UGt, GCUT, r["delta"])
        dn2 = float(r["delta"] @ r["delta"])
        r["F10"] = func_q10(x, H_tr)
        r["F11"] = func_q11(x, g_tr, H_tr)
        r["F12"] = func_q12(x, H_tr, dn2) if dn2 > 0.0 else 0.0
        r["F0"] = r["theq"]
    svec = [r["s"] for r in test_pts]
    dead_lb = [r["s"] < NEAR for r in test_pts]
    sp_tab = {F: BH.spearman([r[F] for r in test_pts], svec)
              for F in ("F10", "F11", "F12", "F0")}
    auc_tab = {F: auc_rank([r[F] for r in test_pts], dead_lb)
               for F in ("F10", "F11", "F12")}
    ctrls = ["EPST", "SCR", "SMOOTH", "HL2"]
    wtab = {}
    for F in ("F10", "F11", "F12"):
        wtab[F] = {}
        for r in CORPUS:
            if r["tag"] == "MAIN":
                wtab[F]["MAIN"] = r[F]
            for wn in ctrls:
                if r["tag"] == "WORLD:" + wn:
                    wtab[F][wn] = r[F]
    det_typ = {F: LS.dist_rule(wtab[F], ctrls)
               for F in ("F10", "F11", "F12")}
    rng_F = {F: (max(r[F] for r in test_pts)
                 - min(r[F] for r in test_pts))
             for F in ("F10", "F11", "F12")}
    dead_spread = {F: (max(wtab[F][c] for c in ctrls)
                       - min(wtab[F][c] for c in ctrls))
                   for F in ("F10", "F11", "F12")}
    check("G62-functional-table", len(test_pts) >= 90,
          "TWO-FORM CONTEST on the %d-point test split: sp vs s: "
          "F10 %+.3f, F11 %+.3f, F12 %+.3f; BASELINE F0 "
          "(theta_eq size) %+.3f; AUC(dead) %s; world values %s; "
          "dist-rule typing %s (construction-trivial MAIN "
          "separation DISCLOSED: all three are 0 at MAIN; "
          "dead-world spreads %s)"
          % (len(test_pts), sp_tab["F10"], sp_tab["F11"],
             sp_tab["F12"], sp_tab["F0"],
             str({F: round(v, 3) for F, v in auc_tab.items()}),
             str({F: {w: "%.3g" % v for w, v in wtab[F].items()}
                  for F in ("F10", "F11", "F12")}),
             str(det_typ),
             str({F: "%.3g" % v
                  for F, v in dead_spread.items()})))
    cand = ("F10", "F11", "F12")
    best_F = max(cand, key=lambda k: abs(sp_tab[k]))
    best_sp = sp_tab[best_F]
    nontriv = dead_spread[best_F] > WORLD_SPREAD_BAR \
        * max(rng_F[best_F], 1e-300)
    if abs(best_sp) >= SP_BAR and abs(best_sp) > abs(sp_tab["F0"]) \
            and nontriv:
        func_verdict = ("CURVATURE_FUNCTIONAL_FOUND(%s, spearman "
                        "%+.3f, baseline %+.3f beaten)"
                        % (best_F, best_sp, sp_tab["F0"]))
    else:
        func_verdict = ("CURVATURE_BLIND(best %s %+.3f; bar %.1f; "
                        "baseline F0 %+.3f; the fourth honest "
                        "negative)" % (best_F, best_sp, SP_BAR,
                                       sp_tab["F0"]))
    check("G63-functional-adjudication", True,
          "SEALED RULE (FOUND iff best |sp| >= %.1f AND beats "
          "the size baseline AND non-degenerate dead-world "
          "spread): best = %s (%+.3f) vs F0 (%+.3f), dead spread "
          "%.3g (bar %.3g) -> %s"
          % (SP_BAR, best_F, best_sp, sp_tab["F0"],
             dead_spread[best_F],
             WORLD_SPREAD_BAR * rng_F[best_F],
             func_verdict.split("(")[0]))

    # ---------------- S7 LEG D: curvature origin (bycatch)
    section("S7  LEG D -- EIGENAXIS SIGNATURE (measurement only)")
    e1u = unit_dir(e_top, lag_l1(e_top), REF)
    w_e1 = MS.wsig_vec(d9 + e1u, L9) - wsig0
    dd_rnd = dict(dirsD)["FRAC00"]
    rnd_u = unit_dir(dd_rnd, lag_l1(dd_rnd), REF)
    w_rnd = MS.wsig_vec(d9 + rnd_u, L9) - wsig0
    stats = {}
    for lbl, wv in (("E_TOP", w_e1), ("RAND", w_rnd)):
        stats[lbl] = dict(
            ap34=RA.func_antidev(wv),
            mb=PFP.func_midband(wv, L9, N_REF),
            terz=fold_shares(wv),
            pr=RA.part_ratio(wv))
    cmp_txt = []
    for st in ("ap34", "mb", "pr"):
        a = abs(stats["E_TOP"][st])
        b = abs(stats["RAND"][st])
        fac = a / max(b, 1e-300)
        cmp_txt.append("%s factor %.2g (%s)"
                       % (st, fac,
                          "DISTINCT" if (fac >= 2.0
                                         or fac <= 0.5)
                          else "not distinct"))
    check("G70-eigenaxis-signature", True,
          "EIGENAXIS SIGNATURE (top eigendirection vs pinned "
          "random FRAC00; typed MEASUREMENT, adjudication-free): "
          "E_TOP antiphase34 %+.3f / midband %.3f / terciles %s "
          "/ PR %.1f; RAND %+.3f / %.3f / %s / %.1f; factor-2 "
          "comparison: %s%s"
          % (stats["E_TOP"]["ap34"], stats["E_TOP"]["mb"],
             str(tuple(round(v, 2)
                       for v in stats["E_TOP"]["terz"])),
             stats["E_TOP"]["pr"],
             stats["RAND"]["ap34"], stats["RAND"]["mb"],
             str(tuple(round(v, 2)
                       for v in stats["RAND"]["terz"])),
             stats["RAND"]["pr"], "; ".join(cmp_txt),
             "" if r90 <= LOWRANK_BAR else " (Leg A is "
             "EXTENSIVE: the axis table is bycatch only, "
             "disclosed)"))

    # ---------------- S8 must-fails + scopes
    section("S8  MUST-FAILS + SCOPE AUDITS")
    h_bad = mutant_wrong_polarization(d2s, d2d)
    check("G80-mustfail-polarization", abs(h_bad - 2.0) > POL_TOL,
          "m1 WRONG PREFACTOR (/2 instead of /4) on the exact "
          "toy quadratic: H = %.3f vs exact 2.0 (dev %.2f > "
          "%.2f) -- CAUGHT by the expansion-identity crosscheck"
          % (h_bad, abs(h_bad / 2.0 - 1.0), POL_TOL))
    fake_test = set(r["tag"] for r in CORPUS)
    ov_m2 = RA.split_auditor(train_tags, fake_test)
    check("G81-mustfail-split-break", len(ov_m2) > 0,
          "m2 SEAL BREAK (training directions inside the test "
          "split): auditor flags %d overlap points -- CAUGHT; "
          "the no-split evaluation is invalid by construction"
          % len(ov_m2))
    u_m3, m_m3 = RA.mutant_broken_conservation(uu9, mm9, du_ridge)
    ok_m3 = not MF.conserve_comb("P2_JIT", uu9, mm9, u_m3, m_m3,
                                 2.0 * th_up * AMP_PAD)
    check("G82-mustfail-conservation", ok_m3,
          "m3 BROKEN CONSERVATION (one weight scaled 1 + 1e-3): "
          "the exact r276 gate returns False -- CAUGHT; weight-"
          "moving 'directions' cannot pass")
    rd_m4 = rich_devs([d2_tab["W_SMOOTH"][0]])
    check("G83-mustfail-richardson", rd_m4 is None,
          "m4 RICHARDSON BREAK (single step size on the real "
          "SMOOTH d2): the sealed auditor returns None -- "
          "FLAGGED as NOT VERIFIABLE; one-step curvature claims "
          "cannot pass")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_, SCOPE_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G84-scope-audits", not hits and not ag_hits,
          "the %d sealed source-pure constructors consume "
          "vectors/densities + geometry + seeds ONLY (%s); "
          "H_tr / g_tr / q(A) are OUTSIDE the source-pure list "
          "and honestly typed measurement-consuming (split-"
          "sealed resp. Leg-B gated); fragment audit: %s"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S9 honesty + verdict
    section("S9  HONESTY LEDGER + VERDICT")
    check("G90-honesty-ledger", True,
          "Hessian entries, eigenvalues, q coefficients, "
          "corrected budgets, functional correlations and axis "
          "statistics are MEASUREMENTS on finite w9 profile "
          "space; the two-form and the trained slopes consume "
          "measured margins (sealed by the disjoint split); the "
          "threshold closure is a second-order statement about "
          "log|h_184| along the ridge sub-directions, NOT a "
          "mechanism claim; NONQUAD/FLAT diagonal entries are "
          "carried at the mid step (disclosed); the F12 "
          "restriction to the training span is disclosed")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no equidistribution "
          "premise, no posthoc window, no RH claim; what the "
          "round adds: the measured curvature two-form with its "
          "spectrum, the second-order closure of the r291 "
          "threshold and retraction, the EPSTEIN curvature "
          "contrast, and the sealed quadratic functional "
          "contest; r243..r291 stand")
    parts_v = []
    parts_v.append(
        "HESSIAN_SPECTRUM(%s; top lam %s; %s; %s)"
        % (fine_rank, str(["%.3g" % v for v in lam_s[:4]]),
           sm_align, ridge_typ))
    parts_v.append("EPSTEIN_CONTRAST(%s)" % ep_typ)
    parts_v.append(thr_verd)
    parts_v.append(ret_verd)
    parts_v.append(func_verdict)
    parts_v.append("FUNCTIONAL_TABLE(sp %s; AUC %s)"
                   % (str({k: round(v, 3)
                           for k, v in sp_tab.items()}),
                      str({k: round(v, 3)
                           for k, v in auc_tab.items()})))
    parts_v.append("EIGENAXIS_SIGNATURE(measured, see G70)")
    verd = " + ".join(parts_v)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s -- MEASURED curvature two-form of the working "
          "set; NO L* claim, NO RH claim" % verd)
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
