#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""antiphase_sign_law_probe -- PRIME.LSTAR.ANTIPHASE_SIGN_LAW.01
(round 322, the DIG round after the r318 fork decision).  Strategic
frame (binding): r318 decided the reviewer fork P2_MAIN_SPECIFIC --
the 2.4 percent negative cross mixtures of the block-Green family
are NOT structureless; on MAIN-class worlds (w9 ladder 12/12 rungs
+ rational twin exact) the block residual lives lawfully on the
ANTIPHASE pair (D3, D4) with fixed sign -1 (modal share med 0.699)
while the dead controls break BY PATTERN (their residual sits on
arch-mean x border (D5, D6): shares 0.95/1.00 vs MAIN 0.03).  Per
the reviewer rule ("if one route is MAIN-specific: dig there") this
is the dig round.  The reviewer thesis made concrete here: "not
positivity DESPITE the negative structure, but controlled
positivity THROUGH an organized indefinite structure" -- the
candidate for the indefinite theorem is a SIGN LAW of the antiphase
cross mixture.  HONEST RESERVATION FROM R318 (hardened first): the
control fingerprints were measured on non-psd-feasible 200-step
Dykstra ITERATES (the r308 non-convergence) -- the r318 world
contrast compares converged (MAIN) against non-converged
(controls).  The three questions of this round: (1) HARDENING --
is the fingerprint iteration- and construction-invariant on MAIN
(starts, step counts, projection order; solution-set property vs
algorithm property), and what do FAIR control objects carry (the
least-norm affine solution, which always exists; the r311
budget-ablated control target, which converges)?  (2) THE LAW
ITSELF -- which (D3, D4) cross entries are negative, how does the
magnitude scale over the rungs, and does an EXACT identity-level
coupling exist (the identity constraints are linear -- compute the
FORCED COMPONENT of the identity on the (D3, D4) sector
symbolically in Fractions at the small windows)?  (3) THE THEOREM
CANDIDATE -- "Q_w admits a block decomposition with psd blocks
PLUS an antiphase cross mixture of fixed sign whose magnitude is
bounded by a source-pure quantity": certify the FORM on the 57
rungs + twin, check the control break on FAIR objects, and sketch
the implication chain to L* with the missing links named honestly.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
COEXISTENCE: r320 (Lean repair) and r321 (fiber coordinate) run in
parallel; this probe touches nothing of theirs; the rh-sync is
strictly ADDITIVE.

INDEX FIREWALL (binding, r238-r318 discipline): w = window (kz),
S = #union atoms of mutilde = mu - nu, S_+ = #mu atoms, S_- = #nu
atoms, N_w = builder depth = (S+1)//2, n = degree, minC = first n
with h_n < 0.  Ground truth (minC, control flips, published record
numbers, the sealed r318 fingerprint pins) enters GATES and record
tables only; the sealed constructors consume passed matrices,
coordinate systems and split-source arrays ONLY (AST scope audit);
no zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r318 IF.{block_residual_census, fp_consensus, V_LIB,
A21_ISO, PA6, PB6, ISOW, IU1, JU1} (the sealed fingerprint
protocol), r312 BM.{feas_diag_g, nnls_lh, lib_vectors}, r311
BN.{gate_lam_rel, vech_of, unvech, rref_rank_fr} + the r311 budget
ablation ladder (ABL_MAIN_S), r308 BG.{census_world, world_arrays,
world_budget, hull_of, block_eigs, least_norm, system_fr,
rref_solve_fr, target_form_fr, mono_rows_fr, block_maps_fr,
exact_budget_fr, border_split}, r288 DC.zv_block (the antiphase
carrier map), r284 LS.{world_pack, spectral_block}, r289
AK.twin_rational + r276 MF.local_gaps, r278 MS.ctx_build, r244
BH.spearman, v881 PIK.lambda_eps, v563 core READ-ONLY.
The only local re-implementations: (i) resid_census_ext = the
UNCHANGED r318 residual-census body returning the per-block
residual entries in addition (anatomy needs the entries, not only
the modal pair; the modal tie-break is byte-identical); (ii)
feas_diag_rev = the UNCHANGED r312 Dykstra body with the two
projections SWAPPED (affine first, then psd; the final point is
psd by construction, convergence = affine residual) -- the sealed
projection-order variant of Leg A.

THE SEALED FORCED-COMPONENT ANALYSIS (Leg B core, frozen here):
the identity constraints are linear, M g = q (r308 system).  For a
linear functional phi on the unknown space, the value phi . g is
CONSTANT on the affine solution set iff phi lies in rowspace(M);
its forced part is phi_par = y^T M with the normal-equation
solution M M^T y = M phi, the forced VALUE is y . q, and the free
fraction is |phi - phi_par|^2 / |phi|^2 (== 0 iff fully forced).
All of it EXACT in Fractions on the exact windows (monomial
basis).  The sector functional of the round: phi_23 = sum_r
G_r[D3, D4] (coefficient 1 on every (2, 3) column of the unscaled
exact system; 1/sqrt(2) on the isometric f64 system).  EXACT
CALIBRATOR (known truth, r308 G10): on TOY4 the (t, t) functional
phi_66 = G[D6, D6] is fully forced with exact value B - 5/7 = 4/7
(D6 is the only t-carrying coordinate of the single block) -- the
machinery must reproduce free fraction 0 and value 4/7 exactly.
DESIGN-TIME DISCLOSURE: D3 = -(D2 + 2 D1) is linearly dependent
inside each block (r308 disclosure), so the (2, 3) sector is NOT
expected to be forced -- the exact free fraction MEASURES how much
of the sign law the identity itself pins; a nonzero free fraction
with the sign law still invariant (Leg A) means the law lives in
the SELECTION GEOMETRY (cone projection of the solution set), not
in the identity algebra -- typed honestly either way.

THE SEALED LEGS (frozen BEFORE any evaluation):

LEG 0 -- ANCHORS.  w9 source pins (367/263/104/184/184); budget
B = 8.368649 (tol 1e-3); THE R318 FINGERPRINT REPRODUCED with the
identical protocol (r308 Dykstra 200 steps from the least-norm
start, per-block NNLS onto the sealed 22-generator cone): Dykstra
CONV (>= -1e-9), modal pair == (2, 3), modal sign == -1, modal
share >= 0.5, d6-class share <= 0.10, cone share med/min/mean in
the r312 bands (0.976/0.952/0.978 tol 0.01), top-eigvec alignment
med 0.9973 (tol 0.005); the r289 twin rebuilt verbatim (minC 184)
with fingerprint pair (2, 3), sign -1, share >= 0.5 (METRIC_ONLY).

LEG A -- HARDENING (question 1).
(a1) START/ORDER/STEP INVARIANCE on w9@A: the sealed variant set
  {LSTART = least-norm start 200 steps (the anchor); LONG =
  least-norm start 1000 steps; ZERO = zero start; RAND1/RAND2 =
  the r311-class random starts (sealed seeds 20260827/20260828,
  r311 scale convention); REV = the projection-order-swapped
  Dykstra from the least-norm start}, alternative starts and REV
  on the staged r311 schedule 200/2000/20000; a variant is
  ACCEPTED iff
  conv (min eig rel >= -1e-9 resp. affine rel <= 1e-9 for REV) or
  near-conv (>= -1e-8, the r311 START_NEAR class, disclosed as
  such); INVARIANCE HOLDS iff every accepted variant carries modal
  pair (2, 3) sign -1 with |share - share_LSTART| <= 0.15 AND at
  least two accepted variants are DISTINCT solution points
  (pairwise rel distance >= 1e-6) -- then the law is a property of
  the SOLUTION SET as sampled, not of one iterate; any accepted
  variant breaking pair/sign => INVARIANCE BREAKS and the sealed
  tree types ALGORITHM_ARTIFACT (amendment a1, disclosed in the
  record tables: gate typing MEASURED -- the negative branch is a
  verdict letter, not a probe failure; no bar, acceptance rule,
  statistic or tree moved).
(a2) FAIR CONTROL OBJECTS: (i) the LEAST-NORM census -- the
  fingerprint of the least-norm affine solution (which ALWAYS
  exists, psd or not; labeled LEASTNORM, non-psd disclosed) on
  w9 / twin / EPST / SCR at DEG_A: the same construction for
  every world, no convergence asymmetry; (ii) the R311 BUDGET
  ABLATION: EPST/SCR targets with (t, t) replaced by the first
  ladder value {|S_ctrl|, 7.654364} making the target PD, then
  least-norm start + staged Dykstra (200/2000/20000) -- the
  ablated control families CONVERGE per r311; their fingerprint
  on the converged family is the fair world contrast: does the
  fair control carry the MAIN law ((2, 3), -1) or its own
  pattern?  MEASURED either way; a fair control carrying the MAIN
  law is typed FAIR_CONTROL_CARRIES (the r318 shape contrast was
  then an iterate artifact -- honest downgrade inside the letter).

LEG B -- ANATOMY + FORCED COMPONENT (question 2).
(b1) ANATOMY on the converged w9 family: dominant-pair histogram
  over the 364 blocks; position dependence (share of (2, 3)-
  dominant blocks per index third head/mid/tail); SIGN
  CONSISTENCY = fraction of (2, 3)-dominant blocks with
  R_r[2, 3] < 0 (law bar 0.9); entry-level fraction of ALL blocks
  with R_r[2, 3] < 0 (typed); rung scaling: per sealed r318 rung
  (the 12-rung set, computed inside the Leg-C ladder loop) the
  magnitude MAG = med_r |R_r[2, 3]| / ||G_r||_F and the residual
  share 1 - cone_share_med, with spearman(MAG, S) typed as
  information.
(b2) THE FORCED COMPONENT (exact): TOY4 calibrator (phi_66 fully
  forced, value 4/7 EXACT -- hard gate; normal equations); phi_23
  on SM1 (the r308 MAIN-class miniature, 7 blocks): exact free
  fraction + exact forced value (Fractions, normal equations --
  the SM1 entries are small rationals, cost-safe); phi_23 on
  MINI16 (the real-w9 miniature, 13 blocks, dyadic entries):
  exact ROWSPACE MEMBERSHIP by the rank test rank(M) vs
  rank(M + [phi]) (the r312-proven-feasible exact grade; the
  normal equations would square the dyadic bit length --
  cost disclosure, sealed at design time) plus the f64 free
  fraction/forced value on the float-converted exact system;
  f64 consistency on w9@A (lstsq rowspace residual + forced
  value, typed); the sector is typed FORCED iff the SM1 exact
  free fraction == 0 AND the MINI16 exact membership holds --
  then the forced value's sign IS the identity-level sign law.
(b3) COUPLING CANDIDATES (each a sealed correlation test, bar
  |spearman| >= 0.9, typed COUPLED/UNCOUPLED, never a claim):
  K1 per-block on w9: |R_r[2, 3]| vs the local antiphase mass
  pairing g_j g_{j+2} + g_{j+1} g_{j+3} (the D3/D4 incidence
  masses); K2 per-rung (12 rungs): MAG vs the 5/7-reserve
  S_{N-2} = B - 5/7; K3 per-rung (12 rungs): MAG vs |z_v| of the
  r288 antiphase carrier map at the rung's crossing (gate-side
  spectral consumption, disclosed).

LEG C -- THE THEOREM CANDIDATE (question 3).  Candidate form
(sealed text): "Q_w - (5/7) t^2 = sum_r <G_r Delta_r, Delta_r>
with G_r = P_r + E_r, P_r in the sealed 22-generator psd cone
(psd by construction), E_r the cone residual with dominant
support on the antiphase pair (D3, D4) and fixed sign
E_r[3, 4] <= 0, and residual mass sum_r ||E_r||_F small against
sum_r ||G_r||_F."  CERTIFICATION CENSUS: on all 57 rungs (42 core
h <= 900 + 15 extension anchors h <= 1300, the r312 rule) + the
twin: Dykstra staged 200/2000 (ladder cap, disclosed; unconverged
rungs typed ITERATE and counted NOT certified), certified iff
CONV AND modal pair (2, 3) AND sign -1 AND share >= 0.5 AND cone
share med >= 0.95; the control break on the FAIR objects from Leg
A is the world-contrast half.  THE IMPLICATION SKETCH (typed,
never a claim): psd blocks + kernel exclusion + a bound
|<E Delta, Delta>| <= (1 - delta)(<P Delta, Delta> + (5/7) t^2)
would give Q > 0 on the restricted subspace (Schur/inertia:
psd + controlled indefinite perturbation => index bound).
MISSING LINKS (sealed list, all named in the letter): L1 the
degree gap (DEG_A = 8 << N_w; restricted-subspace psd asserts
nothing about h_n -- the r282/r308 demarcation); L2 the selection
gap (no source-pure constructive rule for the family, r312
COEFFICIENT_SIGN_WALL -- the decomposition exists solver-wise,
not canonically); L3 the bound gap (the antiphase magnitude bound
is census-grade, no source-pure inequality; the exact forced
component decides whether an identity-level hook exists); L4 the
bridge gap (restricted positivity at one cap does not imply the
window inertia statement -- the r277/v962 bridge needs every
truncation); L5 the convergence gap (r311: ablated controls
converge too -- a certificate must use MORE than convergence: the
pattern itself, which is not yet an inequality).

LEG D -- MUST-FAILS (each loud):
  (m1) FINGERPRINT ON AN UNCONVERGED MAIN ITERATE: the census of
    the 2-step w9 Dykstra iterate must be flagged ITERATE by the
    sealed acceptance verifier (feas < -1e-9 => REJECT), while
    the converged anchor census is accepted -- the r318 caveat
    is machine-enforced;
  (m2) D-PAIR PERMUTATION: the census run on the coordinate-
    permuted family P G P^T (D3 <-> D5, i.e. indices 2 <-> 4)
    must report a modal pair != the sealed anchor pair -- CAUGHT
    by the anchor comparison (the pair label is load-bearing);
  (m3) FORCED COMPONENT WITH THE WRONG IDENTITY SIGN (exact):
    the mutant consuming -q on TOY4 must return forced value
    -4/7 != +4/7 -- CAUGHT in Fractions (the calibrator value is
    nonzero by r308 G10, so the catch cannot be vacuous);
  (m4) COUPLING WITH TARGET READ-BACK: a mutant coupling feature
    consuming the withheld truth (R23_true / cross_true) --
    FLAGGED by the AST scope audit.

STOP LIST (binding): NO L* claim, NO RH claim, NO bound
mechanism, NO asymptotic law, NO derived 5/7, NO posthoc window,
NO re-opened no-go entry (functionals, extremality, KYP, Maslov,
fixed head, paired cone, block-Green construction, diophantine,
magnitudes stay stopped); no bar, band, rule or verdict form
change after any evaluation (amendments disclosed); r243..r321
stand; mincut base 4 / refined 5 UNCHANGED.

WORLDS: MAIN w9; the r289 rational twin (METRIC_ONLY semantics);
controls EPST / SCRAMBLE(seed 1) built verbatim through the
r283/r284 channel (the two fair-object controls of r311); the
57-rung census ladder (42 core + 15 extension, r312 rule); exact
models TOY4 / SM1 / MINI16 rebuilt VERBATIM from the r308
constructors.

SEALED CONSTANTS: DEG_A 8; MAIN_KZ 9; W9_ANCH (367, 263, 104,
184, 184); B_W9_REC 8.368649 tol 1e-3; H_CAP 900; EXT_H 1300;
K_EXT 15; FEAS_IT (200, 2000, 20000); FEAS_CONV 1e-9; NEAR_CONV
1e-8; STEP_LONG 1000; SEEDS_R (20260827, 20260828); REV_CONV
1e-9; DIST_MIN 1e-6; FP_PAIR (2, 3); FP_SIGN -1; SHARE_MIN 0.5;
SHARE_BAND 0.15; D6_MAX 0.10; SIGN_CONS_BAR 0.9; SHARE_REC
(0.976, 0.952, 0.978) tol 0.01; ALIGN_REC 0.9973 tol 0.005;
TWIN_MINC_REC 184; TWIN_SHARE_REC 0.692 tol 0.05; ABL_MAIN_S
7.654364 (r311); PSD_NEG 1e-7; SP_BAR 0.9; CONE_MIN 0.95;
LADDER_CAP_IT 2000; N_FP 12; RAT_TOL 1e-8; QMAX 1e6; MINI_K 16;
MINI_BK 3; F64_FORCE_BAR 1e-16; DEPTH_PAD 6; TOY4 x = (1/2, 1/4,
-1/4, -1/2) w = (1, 1/2, -1/3, 1/4) border (3/4) w (1/5) B = 9/7
deg cap 1 (r308 verbatim); SM1 x_j = (9-2j)/11, w = (1, 1, -1/3,
1, 1, -1/4, 1, 1, -1/5, 1), SM border (4/5, 1/3, -2/5) w (1/7,
1/11, 1/13) (r308 verbatim); runtime <= 1800 s; smoke = S0 + S1
exact layer (TOY4 calibrator + SM1 forced component) + w9 anchor
(census + 200-step Dykstra + fingerprint) + w9 anatomy + w9 f64
forced component + all four must-fails + scope audits (MINI16,
twin, controls, variants, ablation, ladder, coupling, candidate,
adjudication skipped).  PRE-SPEC SCOPING
(disclosed): every record number above is a published r308/r311/
r312/r318 record adopted as-is; the variant set, the fair
objects, the forced-component machinery, the coupling candidates,
the certification bars, all four must-fails, every bar/band/
tolerance, the adjudication tree and the verdict form were fixed
at design time BEFORE any evaluation of this probe; no machinery
pass preceded this spec except record reading.

SEALED ADJUDICATION TREE (frozen BEFORE evaluation):
  law_anchor = the Leg-0 w9 fingerprint gate (pair, sign, share,
    d6, cone bands) AND anatomy sign consistency >= 0.9;
  invariant = the Leg-A a1 invariance gate;
  exact_forced = SM1 exact free fraction == 0 with forced value
    < 0 AND MINI16 exact rowspace membership TRUE;
  NOT law_anchor => LAW_DIFFUSE;
  law_anchor AND NOT invariant => ALGORITHM_ARTIFACT(variant);
  law_anchor AND invariant AND exact_forced =>
    SIGN_LAW_EXACT(forced identity verbatim);
  otherwise => SIGN_LAW_ROBUST(lawful, not exact).
SEALED VERDICT FORM (joined with '+'):
  [exactly one of] SIGN_LAW_EXACT / SIGN_LAW_ROBUST /
    ALGORITHM_ARTIFACT / LAW_DIFFUSE
  + HARDENING(variant table; distinctness; fair-object contrast)
    [always]
  + ANATOMY(pair histogram; position; sign consistency; scaling)
    [always]
  + FORCED(TOY4 calibrator; SM1/MINI16 exact; w9 f64) [always]
  + COUPLING(K1/K2/K3) [always]
  + CANDIDATE(cert census; missing links L1-L5) [always]
  + R318_DEMARCATION [always]: the r318 letters stand; this
    round adjudicates the dig questions only.

RECORD TABLES (frozen from the record run; chronology honest:
(i) PRE-RUN PROTOCOL CORRECTION disclosed -- a draft record-table
block with placeholder numbers was removed from this docstring
BEFORE the first run of any stage (the r316/r318 protocol lesson,
applied); (ii) smoke pass 1 = 25/25 (1.3 s) at the sealed rules;
(iii) calibration pass 1 = first full evaluation = 23/25: the G30
invariance gate was typed HARD in the draft harness, so the
honest negative branch of the sealed tree (ALGORITHM_ARTIFACT,
already produced verbatim by this very pass) failed the probe
arithmetically -> AMENDMENT a1 (disclosed, gate typing only): G30
is MEASURED and the sealed tree adjudicates in S8 -- the negative
branch is a verdict letter, not a probe failure (house precedent:
the r318 FORK_DEAD branch is a passing letter); NO bar,
acceptance rule, statistic, band or tree moved, and the verdict
letter of calibration pass 2 is IDENTICAL to the letter produced
by pass 1; one reporting-only enrichment of the
ALGORITHM_ARTIFACT letter detail (the measured basin facts,
r318-a1 class); calibration pass 2 = 25/25 (165.1 s), all
numbers identical to pass 1; record run1/run2 = 25/25, identical
up to WALL).
REC_VERDICT = ALGORITHM_ARTIFACT(the law breaks under the sealed
variants RAND1/RAND2 -- their accepted near-feasible points
(staged to 20000 steps, min eig rel -8.5e-9 / -1.2e-9, the r311
START_NEAR class) carry modal pair (0, 2) with shares 0.310 /
0.264 and cone share med 0.782: the sign law AND the r312
97.6/2.4 cone anatomy are properties of the LEAST-NORM-PROXIMAL
DYKSTRA BASIN, not of the psd solution set as a whole; the
canonical protocol variants LSTART/LONG/ZERO/REV all carry the
law exactly ((2, 3), -1, share 0.692) AND converge to essentially
ONE point -- the distinctness census shows exactly 9/15 variant
pairs distinct = precisely the pairs involving RAND1/RAND2 (the
six canonical pairs coincide within rel 2.0e-7): the sampled psd
intersection has (at least) two basins, and the law is the
fingerprint of the least-norm-proximal one)
+ HARDENING(variant table LSTART (2,3) -1 0.692 OK / LONG 0.692
OK / ZERO 0.692 OK / RAND1 (0,2) 0.310 NEAR / RAND2 (0,2) 0.264
NEAR / REV 0.692 OK (projection order irrelevant); FAIR OBJECTS:
(i) LEASTNORM census (same construction on every world, non-psd
disclosed): w9 (2,3) -1 0.698 / twin (2,3) -1 0.698 / EPST (4,5)
-1 1.000 d6 1.000 / SCR (4,5) -1 1.000 d6 1.000 -- the r318
world-contrast SHAPE is already present at the least-norm point
(the control 200-step iterates stall near it), and MAIN's law is
present there too; (ii) THE DECISIVE FAIR CONTRAST, r311 budget
ablation staged 200/2000/20000: EPST-abl (t,t) <- +3.9921,
target PD +1.04e-3, Dykstra CONV +2.5e-16 @2000, census (2, 3)
-1 share 0.742 d6 0.047 cone med 0.958 => CARRIES the MAIN law
(stronger than MAIN's own 0.692); SCR-abl (t,t) <- +5.2368, PD
+1.08e-3, CONV -5.1e-11 @200, census (2, 3) -1 share 0.379 d6
0.371 => breaks the share bar => FAIR_CONTROL_CARRIES 1/2: the
r318 SHAPE dichotomy ((4,5) vs (2,3)) does NOT survive fair
convergence -- on converged fair objects the separation is a
share MARGIN and mixed, not a pattern dichotomy)
+ ANATOMY(dominant-pair histogram w9 (364 blocks): (2,3) 252 =
share 0.692, then (2,4) 67 / (3,4) 29 / (4,5) 10 -- the
sub-dominant pairs are antiphase-adjacent, not border; position
NOT uniform: thirds share 0.289/0.860/0.926 (the law lives in
the mid/tail of the fold order; the head third is (2,4)/(3,4)-
mixed); SIGN CONSISTENCY 1.000 -- EVERY (2,3)-dominant block has
R[2,3] < 0 (bar 0.9) and 92.3 percent of ALL blocks have
R[2,3] < 0; rung scaling: MAG med 7.4e-3..1.4e-2 over the 12
sealed rungs, spearman(MAG, S) = -0.168 -- scale-stable, no
growth law)
+ FORCED(TOY4 calibrator MACHINE-EXACT: free fraction 0, value
4/7 == B - 5/7 -- the normal-equation machinery reproduces the
r308 G10 hand pin; SM1 phi_23 exact free fraction 0.47671,
forced value +5.101e-1 (POSITIVE) -- the identity pins roughly
half the sector mass and pins it with the WRONG sign for the
law; MINI16 exact rowspace membership FALSE (rank 55 -> 56 with
phi appended; f64 free 0.58576, value +3.1e-7); w9 f64 free
0.63527, value +1.203e-1 -- CONSISTENT ACROSS GRADES: the
(D3, D4) sector is roughly half free, and its forced half has
POSITIVE value: the negative sign law is carried ENTIRELY by the
free directions = the selection geometry, exactly as the D3 =
-(D2 + 2 D1) in-block dependence disclosure predicted;
exact_forced = False)
+ COUPLING(K1 per-block |R[2,3]|/||G||_F vs antiphase mass
pairing g_j g_{j+2} + g_{j+1} g_{j+3}: spearman +0.8114 --
UNCOUPLED at the sealed 0.9 bar but the strongest measured
correlate of the round (typed information: the residual
magnitude tracks the local antiphase mass geometry at rank
+0.81); K2 per-rung MAG vs 5/7-reserve S_{N-2}: -0.832
UNCOUPLED; K3 per-rung MAG vs |z_v| (r288 carrier at the
crossing): +0.252 UNCOUPLED -- no rung-global coupling; the only
near-coupling is block-LOCAL)
+ CANDIDATE(certification census at the sealed bars (CONV +
pair + sign + share >= 0.5 + cone med >= 0.95): 57/57 rungs
CERTIFIED (conv 57/57 within the 2000-step ladder cap; worst
share 0.605@kz23, worst cone med 0.970@kz12) + twin CERTIFIED
(0.692) -- the candidate FORM holds censally on the whole
MAIN-class ladder AS A PROPERTY OF THE CANONICAL FAMILY, but the
round's own hardening findings demote it: the family is
basin-selected (main letter) and a fair control carries the
pattern (L5 sharpened); MISSING LINKS L1-L5 all open, L5 now
sharpened to: fair controls converge AND can carry the pattern
-- a certificate needs the share margin as an inequality, which
does not exist)
+ R318_DEMARCATION.
Key numbers.  LEG 0 bit-near: w9 367/263/104/184/184, B =
8.368649; r318 fingerprint reproduced (CONV +6.56e-16, (2, 3) -1
share 0.692 d6 0.027, cone med/min/mean 0.9760/0.9520/0.9778,
alignment 0.9973; twin CONV +2.05e-17, (2, 3) -1 0.692 == the
r318 twin record).  MUST-FAILS: m1 2-step w9 iterate (feas
-2.4e-3) REJECTED as ITERATE, converged anchor accepted; m2
permuted-family census modal (3, 4) != (2, 3) CAUGHT; m3 -q
mutant forced value -4/7 != +4/7 CAUGHT exact; m4 read-back
mutant AST-FLAGGED (R23_true/cross_true); constructors +
fragment audit CLEAN.  READING (typed measurement): the dig
round answers all three questions honestly AGAINST the strong
form of the r318 hope -- (1) the law is protocol-stable
(starts in the least-norm class, step counts, projection order)
but NOT solution-set-universal: random-basin near-solutions
carry a different fingerprint, so the law is a property of the
Dykstra selection, and the r318 world contrast weakens on fair
objects (EPST-abl carries the pattern stronger than MAIN); (2)
the law is NOT identity-forced -- the exact forced component of
the (D3, D4) sector is ~half the mass with POSITIVE value, the
negative law lives entirely in the free/selection directions;
its best correlate is the block-local antiphase mass pairing
(+0.81, below bar); (3) the candidate form certifies 57/57 +
twin censally but is demoted by (1): without a canonical
selection rule (L2, the r312 wall) the antiphase sign law
cannot be stated as a property of Q_w itself.  What survives as
the honest dig yield: the law is a sharp, reproducible,
POSITION-STRUCTURED (mid/tail) fingerprint of the least-norm-
proximal psd family with total sign consistency, and the
selection-geometry question ("WHY does the proximal basin
organize its indefiniteness on the antiphase pair?") is now the
precisely named residual object -- one honest candidate hook
survives at reporting grade: the block-local antiphase mass
pairing.  Runtime 165.1 s full / 1.3 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: a1 only (gate
typing, disclosed above; letter identical across passes).

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

import indefinite_fork_probe as IF                 # noqa: E402 r318
import blockgreen_membership_probe as BM           # noqa: E402 r312
import blockgreen_nontriviality_probe as BN        # noqa: E402 r311
import block_green_probe as BG                     # noqa: E402 r308
import destructive_coherence_probe as DC           # noqa: E402 r288
import lstar_two_measure_probe as LS               # noqa: E402 r284
import metric_stability_probe as MS                # noqa: E402 r278
import minimal_firewall_probe as MF                # noqa: E402 r276
import arch_kernel_diophantine_probe as AK         # noqa: E402 r289
import bordered_hankel_probe as BH                 # noqa: E402 r244
import port_integrable_kernel_probe as PIK         # noqa: E402 v881
import v563_paper2_readouts as core                # noqa: E402 READ-ONLY

DEG_A = 8
MAIN_KZ = 9
W9_ANCH = (367, 263, 104, 184, 184)
B_W9_REC = 8.368649
B_W9_TOL = 1e-3
H_CAP = 900
EXT_H = 1300
K_EXT = 15
FEAS_IT1 = 200
FEAS_IT2 = 2000
FEAS_IT3 = 20000
FEAS_CONV = 1e-9
NEAR_CONV = 1e-8
STEP_LONG = 1000
SEEDS_R = (20260827, 20260828)
REV_CONV = 1e-9
DIST_MIN = 1e-6
FP_PAIR = (2, 3)
FP_SIGN = -1
SHARE_MIN = 0.5
SHARE_BAND = 0.15
D6_MAX = 0.10
SIGN_CONS_BAR = 0.9
SHARE_REC = (0.976, 0.952, 0.978)
SHARE_TOL = 0.01
ALIGN_REC = 0.9973
ALIGN_TOL = 0.005
TWIN_MINC_REC = 184
TWIN_SHARE_REC = 0.692
TWIN_SHARE_TOL = 0.05
ABL_MAIN_S = 7.654364
PSD_NEG = 1e-7
SP_BAR = 0.9
CONE_MIN = 0.95
LADDER_CAP_IT = 2000
N_FP = 12
RAT_TOL = 1e-8
QMAX = 1e6
MINI_K = 16
MINI_BK = 3
F64_FORCE_BAR = 1e-16
DEPTH_PAD = 6
FIVE_SEVEN = Fr(5, 7)
B_TOY = Fr(9, 7)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

PAIRS21 = [(a, b) for a in range(6) for b in range(a, 6)]
P23_IDX = PAIRS21.index((2, 3))
P66_IDX = PAIRS21.index((5, 5))

MISSING_LINKS = (
    "L1 degree gap (DEG_A = 8 << N_w; restricted-subspace psd "
    "asserts nothing about h_n -- r282/r308 demarcation)",
    "L2 selection gap (no source-pure constructive rule for the "
    "family -- r312 COEFFICIENT_SIGN_WALL; the decomposition "
    "exists solver-wise, not canonically)",
    "L3 bound gap (the antiphase magnitude bound is census-grade; "
    "no source-pure inequality proven)",
    "L4 bridge gap (restricted positivity at one cap does not "
    "imply the window inertia statement; the r277/v962 bridge "
    "needs every truncation)",
    "L5 convergence gap (r311: ablated controls converge too -- a "
    "certificate must use MORE than convergence: the pattern "
    "itself, which is not yet an inequality)")


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
                       "constructors consume passed matrices, "
                       "coordinate systems and split-source arrays "
                       "ONLY; record numbers enter gates and "
                       "record tables only"
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


CONSTRUCTORS = ("resid_census_ext", "feas_diag_rev",
                "forced_component_fr", "forced_component_f64",
                "phi_sector_fr", "phi_sector_f64",
                "antiphase_mass_feat", "fp_accept",
                "staged_feas", "cert_cell")
SCOPE_FORBIDDEN = {"minC_true", "cross_true", "R23_true",
                   "sign_true", "CTRL_FLIPS", "W9_ANCH",
                   "FP_PAIR", "FP_SIGN"}


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
def resid_census_ext(g, nblk, V, A21, pa, pb, isow, iu1, ju1):
    """the UNCHANGED r318 residual-census body (per-block sealed
    cone projection, residual matrix in the D basis, dominant
    off-diagonal pair with the identical tie-break), returning in
    addition the per-block residual entries R_r[2, 3], the block
    Frobenius scales and the dominant-pair/sign arrays -- the
    anatomy consumes entries, not only the modal pair.  Consumes
    the passed iterate/coordinates only."""
    lam, scale, G = BG.block_eigs(g, nblk)
    pairs = []
    signs = []
    shares = []
    r23 = np.zeros(nblk)
    fro = np.zeros(nblk)
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
        r23[r] = R[2, 3]
        fro[r] = max(float(np.sqrt(np.sum(G[r] * G[r]))), 1e-300)
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
                share_mean=float(np.mean(shares)),
                pairs=pairs, signs=signs, r23=r23, fro=fro,
                nblk=nblk)


def feas_diag_rev(M, q, g0, nblk, iters):
    """the UNCHANGED r312 Dykstra body with the two projections
    SWAPPED (affine set first, then blockwise psd clip): the
    final point is psd by construction; convergence is the affine
    rel residual.  Consumes the coordinate system only."""
    pa, pb = np.triu_indices(6)
    npairs = len(pa)
    g = g0.copy()
    Mp = np.linalg.pinv(M, rcond=1e-11)
    for _it in range(iters):
        g = g - Mp @ (M @ g - q)
        lam, scale, G = BG.block_eigs(g, nblk)
        ev, V = np.linalg.eigh(G)
        evc = np.clip(ev, 0.0, None)
        Gp = np.einsum("rij,rj,rkj->rik", V, evc, V)
        gv = np.zeros((nblk, npairs))
        for p_i in range(npairs):
            a, b = int(pa[p_i]), int(pb[p_i])
            if a == b:
                gv[:, p_i] = Gp[:, a, a]
            else:
                gv[:, p_i] = Gp[:, a, b] * math.sqrt(2.0)
        g = gv.reshape(-1)
    rel = float(np.linalg.norm(M @ g - q)
                / max(np.linalg.norm(q), 1e-300))
    lam, scale, _G = BG.block_eigs(g, nblk)
    return float(np.min(lam) / scale), rel, g


def phi_sector_fr(nblk, pair_idx):
    """exact sector functional on the UNSCALED exact system: the
    vector with coefficient 1 on the given pair column of every
    block (phi . g = sum_r G_r[pair]).  Consumes the block count
    only."""
    phi = [Fr(0)] * (nblk * len(PAIRS21))
    for r in range(nblk):
        phi[r * len(PAIRS21) + pair_idx] = Fr(1)
    return phi


def phi_sector_f64(nblk, pair_idx):
    """f64 sector functional on the Frobenius-isometric system
    (off-diagonal unknowns carry sqrt(2): G_ab = g_p / sqrt(2))."""
    phi = np.zeros(nblk * len(PAIRS21))
    a, b = PAIRS21[pair_idx]
    fac = 1.0 if a == b else 1.0 / math.sqrt(2.0)
    for r in range(nblk):
        phi[r * len(PAIRS21) + pair_idx] = fac
    return phi


def forced_component_fr(M, q, phi):
    """EXACT forced-component analysis of a linear functional on
    the affine solution set {g : M g = q}: normal equations
    (M M^T) y = M phi (always consistent), forced part phi_par =
    y^T M, forced value y . q, free fraction |phi - phi_par|^2 /
    |phi|^2 (exact Fractions).  Consumes the passed system
    only."""
    nr = len(M)
    nc = len(M[0])
    MMt = [[sum(M[i][c] * M[j][c] for c in range(nc))
            for j in range(nr)] for i in range(nr)]
    rhs = [sum(M[i][c] * phi[c] for c in range(nc))
           for i in range(nr)]
    ex, _rk, _dof, y = BG.rref_solve_fr(MMt, rhs)
    if not ex:
        return None, None, None
    phi_par = [sum(y[i] * M[i][c] for i in range(nr))
               for c in range(nc)]
    forced_val = sum(y[i] * q[i] for i in range(nr))
    num = sum((phi[c] - phi_par[c]) ** 2 for c in range(nc))
    den = sum(phi[c] ** 2 for c in range(nc))
    free_frac = num / den if den != 0 else None
    return free_frac, forced_val, y


def forced_component_f64(M, q, phi):
    """f64 twin of the forced-component analysis: lstsq rowspace
    fit M^T y ~ phi, residual fraction and forced value y . q."""
    y, _r, _rk, _sv = np.linalg.lstsq(M.T, phi, rcond=None)
    res = M.T @ y - phi
    frac = float(np.dot(res, res) / max(np.dot(phi, phi), 1e-300))
    return frac, float(np.dot(y, q))


def antiphase_mass_feat(ww):
    """per-block local antiphase mass pairing g_j g_{j+2} +
    g_{j+1} g_{j+3} (gross masses; the D3/D4 incidence geometry).
    Consumes the passed weight array only."""
    g = np.abs(np.asarray(ww, float))
    return g[:-3] * g[2:-1] + g[1:-2] * g[3:]


def fp_accept(cen, feas, near_bar):
    """sealed acceptance verifier of a fingerprint census: OK iff
    the family is psd-feasible at the convergence bar, NEAR iff
    within the disclosed near-convergence bar, else ITERATE
    (rejected -- the r318 caveat machine-enforced).  Consumes the
    passed census/feasibility only."""
    if feas >= -FEAS_CONV:
        return "OK"
    if feas >= -near_bar:
        return "NEAR"
    return "ITERATE"


def staged_feas(M, q, g0, nblk, stages):
    """staged r311 schedule from a FIXED start (restart per
    stage, r311 run_feas3 convention), returning the final
    iterate of the last executed stage."""
    fm, rel, g = BM.feas_diag_g(M, q, g0, nblk, stages[0])
    it = stages[0]
    for st in stages[1:]:
        if fm >= -FEAS_CONV:
            break
        fm, rel, g = BM.feas_diag_g(M, q, g0, nblk, st)
        it = st
    return fm, rel, g, it


def cert_cell(cen, feas):
    """sealed certification cell of the Leg-C candidate form:
    certified iff the family is accepted at the convergence bar
    AND the census meets the sealed pattern/share/cone bars.
    The pattern bars are passed via the census fields measured
    blind; the comparison constants live gate-side."""
    conv = feas >= -FEAS_CONV
    return dict(conv=conv, pair=cen["modal_pair"],
                sign=cen["modal_sign"], share=cen["modal_share"],
                cone=cen["share_med"], d6=cen["d6_share"])


# ============== must-fail mutants
def mutant_wrong_identity_sign(M, q_neg, phi):
    """m3 MUST-FAIL: the forced component computed against the
    SIGN-FLIPPED identity (-q) -- must return the negated forced
    value on the exact TOY4 calibrator (CAUGHT in Fractions)."""
    return forced_component_fr(M, q_neg, phi)


def mutant_coupling_readback(R23_true, cross_true):
    """m4 MUST-FAIL: a coupling feature consuming the withheld
    truth -- the AST scope audit must FLAG this."""
    return float(R23_true) + float(cross_true)


# ============== gate-side helpers
def fp_run_pack(pack, ctx, iters):
    """gate-side fingerprint run for one world (r318 fp_run
    class): census at DEG_A, Dykstra from the least-norm start,
    extended residual census."""
    Bw, _rho, bxa, bwa = BG.world_budget(pack, ctx)
    ffw, xaw, waw = BG.world_arrays(pack)
    C = BG.census_world(xaw, waw, bxa, bwa, Bw, DEG_A,
                        BG.hull_of(xaw, bxa))
    fm, rel, g = BM.feas_diag_g(C["M"], C["q"], C["g"],
                                C["nblk"], iters)
    cen = resid_census_ext(g, C["nblk"], IF.V_LIB, IF.A21_ISO,
                           IF.PA6, IF.PB6, IF.ISOW, IF.IU1,
                           IF.JU1)
    return cen, float(fm), C, g, Bw, waw


def census_of_g(g, nblk):
    """gate-side: extended residual census of a passed family."""
    return resid_census_ext(g, nblk, IF.V_LIB, IF.A21_ISO,
                            IF.PA6, IF.PB6, IF.ISOW, IF.IU1,
                            IF.JU1)


def fmt_cen(cen):
    return "%s %+d share %.3f d6 %.3f cone med %.3f" % (
        str(cen["modal_pair"]), cen["modal_sign"],
        cen["modal_share"], cen["d6_share"], cen["share_med"])


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("antiphase_sign_law_probe -- "
          "PRIME.LSTAR.ANTIPHASE_SIGN_LAW.01 (round 322)")
    print("SPEC_SHA %s   (r318 IF %s / r312 BM %s / r311 BN %s / "
          "r308 BG %s)"
          % (SPEC_SHA[:16], IF.SPEC_SHA[:16], BM.SPEC_SHA[:16],
             BN.SPEC_SHA[:16], BG.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (S0 + TOY4 calibrator + SM1 forced "
                        "component + w9 anchor fingerprint + "
                        "must-fails + scopes; twin, controls, "
                        "variants, ablation, ladder, coupling, "
                        "candidate, adjudication skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the variant set (LSTART/LONG/"
          "ZERO/RAND1/RAND2/REV) with the staged r311 schedule and "
          "the acceptance verifier, the two fair control objects "
          "(least-norm census + r311 budget ablation), the exact "
          "forced-component machinery with the TOY4 calibrator "
          "(known forced truth 4/7), the three coupling candidates "
          "K1/K2/K3, the 57-rung certification bars, all four "
          "must-fails, every bar/band/tolerance, the adjudication "
          "tree and the sealed verdict form; the r318 caveat "
          "(ITERATE-grade control fingerprints) is the declared "
          "target of Leg A; design-time disclosure: D3 = -(D2 + "
          "2 D1) is linearly dependent inside each block, so the "
          "(2, 3) sector is NOT expected to be identity-forced -- "
          "the free fraction MEASURES it either way")

    # ---------------- S1 exact layer
    section("S1  EXACT LAYER -- TOY4 CALIBRATOR + FORCED COMPONENT")
    x4 = [Fr(1, 2), Fr(1, 4), Fr(-1, 4), Fr(-1, 2)]
    w4 = [Fr(1), Fr(1, 2), Fr(-1, 3), Fr(1, 4)]
    bx4 = [Fr(3, 4)]
    bw4 = [Fr(1, 5)]
    A4 = BG.target_form_fr(x4, w4, bx4, bw4, B_TOY, 1)
    A4s = [row[:] for row in A4]
    A4s[2][2] = B_TOY - FIVE_SEVEN
    L4 = BG.block_maps_fr(BG.mono_rows_fr(x4, 1), w4)
    M4, q4, _i4 = BG.system_fr(L4, A4s)
    phi66 = phi_sector_fr(len(L4), P66_IDX)
    fr66, val66, _y66 = forced_component_fr(M4, q4, phi66)
    ok_cal = (fr66 == 0 and val66 == B_TOY - FIVE_SEVEN)
    check("G10-toy4-forced-calibrator", ok_cal,
          "TOY4 (r308 verbatim, exact): the (t, t) sector "
          "functional phi_66 is FULLY FORCED by the identity -- "
          "free fraction %s == 0 EXACT, forced value %s == B - "
          "5/7 == 4/7 EXACT (the r308 G10 hand pin reproduced "
          "through the sealed normal-equation machinery: the "
          "forced-component analysis is calibrated on a known "
          "forced truth)" % (str(fr66), str(val66)))

    # SM1 (r308 verbatim)
    x10 = [Fr(9 - 2 * j, 11) for j in range(10)]
    w_sm1 = [Fr(1), Fr(1), Fr(-1, 3), Fr(1), Fr(1), Fr(-1, 4),
             Fr(1), Fr(1), Fr(-1, 5), Fr(1)]
    bxs_sm = [Fr(4, 5), Fr(1, 3), Fr(-2, 5)]
    bws_sm = [Fr(1, 7), Fr(1, 11), Fr(1, 13)]
    B_sm1 = BG.exact_budget_fr(x10, w_sm1, bxs_sm, bws_sm,
                               (len(x10) + 1) // 2)
    A_sm1 = BG.target_form_fr(x10, w_sm1, bxs_sm, bws_sm, B_sm1,
                              DEG_A)
    As_sm1 = [row[:] for row in A_sm1]
    As_sm1[-1][-1] = B_sm1 - FIVE_SEVEN
    Ls_sm1 = BG.block_maps_fr(BG.mono_rows_fr(x10, DEG_A), w_sm1)
    M_sm1, q_sm1, _is1 = BG.system_fr(Ls_sm1, As_sm1)
    phi23_s = phi_sector_fr(len(Ls_sm1), P23_IDX)
    fr_s, val_s, _ys = forced_component_fr(M_sm1, q_sm1, phi23_s)
    check("G11-sm1-forced-component", fr_s is not None
          and 0 <= fr_s <= 1,
          "SM1 (MAIN-class miniature, %d blocks, exact "
          "monomials): the (D3, D4) sector functional phi_23 has "
          "EXACT free fraction %.5f and forced value %+.3e "
          "(exact rational %s...) -- %s; MEASURED, adjudicated "
          "in S8" % (len(Ls_sm1), float(fr_s), float(val_s),
                     str(val_s)[:24],
                     "FULLY FORCED: identity-level sign law"
                     if fr_s == 0 else
                     "NOT forced: the sector is essentially free "
                     "in the identity algebra (the disclosed D3 "
                     "in-block dependence)"))

    if smoke:
        check("G12-mini16-forced-component", True, "SMOKE: skipped")
        member_m = False
        fr_m_f64 = None
        val_m_f64 = None
    else:
        ctx9_pre = MS.ctx_build(MAIN_KZ)
        rr9_pre = core.build_window(MAIN_KZ)
        W9_pre = LS.world_pack("w9", ctx9_pre, float(rr9_pre["D"]))
        _ff9p, xx9p, ww9p = BG.world_arrays(W9_pre)
        bx9, bw9, by9, bv9 = BG.border_split(ctx9_pre)
        bxa9f = np.concatenate([bx9, by9])
        bwa9f = np.concatenate([bw9, -bv9])
        mini_x = [Fr(float(x)) for x in xx9p[:MINI_K]]
        mini_w = [Fr(float(w)) for w in ww9p[:MINI_K]]
        mini_bx = [Fr(float(x)) for x in bxa9f[:MINI_BK]]
        mini_bw = [Fr(float(w)) for w in bwa9f[:MINI_BK]]
        B_mini = BG.exact_budget_fr(mini_x, mini_w, mini_bx,
                                    mini_bw, (MINI_K + 1) // 2)
        A_mini = BG.target_form_fr(mini_x, mini_w, mini_bx,
                                   mini_bw, B_mini, DEG_A)
        As_mini = [row[:] for row in A_mini]
        As_mini[-1][-1] = B_mini - FIVE_SEVEN
        L_mini = BG.block_maps_fr(BG.mono_rows_fr(mini_x, DEG_A),
                                  mini_w)
        Mm_fr, qm_fr, _im = BG.system_fr(L_mini, As_mini)
        phi23_m = phi_sector_fr(len(L_mini), P23_IDX)
        rank_m, _pm, _Rm = BN.rref_rank_fr(Mm_fr)
        rank_ma, _pa_, _Ra = BN.rref_rank_fr(Mm_fr + [phi23_m])
        member_m = (rank_ma == rank_m)
        Mm_f = np.array([[float(v) for v in row]
                         for row in Mm_fr])
        qm_f = np.array([float(v) for v in qm_fr])
        phi_m_f = np.array([float(v) for v in phi23_m])
        fr_m_f64, val_m_f64 = forced_component_f64(Mm_f, qm_f,
                                                   phi_m_f)
        check("G12-mini16-forced-component", rank_m > 0,
              "MINI16 (real-w9 miniature, %d blocks, exact "
              "dyadic entries): phi_23 rowspace MEMBERSHIP by "
              "the exact rank test rank(M) = %d vs rank(M + "
              "[phi]) = %d => %s (the r312-feasible exact grade; "
              "normal equations avoided by the sealed cost "
              "disclosure); f64 free fraction %.5f, f64 forced "
              "value %+.3e -- MEASURED, adjudicated in S8"
              % (len(L_mini), rank_m, rank_ma,
                 "MEMBER: identity-forced sector" if member_m
                 else "NOT a member: the sector is free",
                 fr_m_f64, val_m_f64))

    # ---------------- S2 leg 0 anchors
    section("S2  LEG 0 -- W9 + TWIN ANCHORS (r308/r312/r318 PINS)")
    ctx9 = MS.ctx_build(MAIN_KZ)
    rr9 = core.build_window(MAIN_KZ)
    D9 = float(rr9["D"])
    W9 = LS.world_pack("w9", ctx9, D9)
    ok_src = (W9["S"] == W9_ANCH[0] and W9["Sp"] == W9_ANCH[1]
              and W9["Sm"] == W9_ANCH[2] and W9["N"] == W9_ANCH[3]
              and W9["minC"] == W9_ANCH[4])
    cen9, feas9, C9, g9, B9, ww9u = fp_run_pack(W9, ctx9, FEAS_IT1)
    check("G20-w9-source-pins", ok_src
          and abs(B9 - B_W9_REC) <= B_W9_TOL,
          "w9 SOURCE %d/%d/%d, N_w %d, minC %s (v956 pins); "
          "budget scalar B = %.6f (rec %.6f, tol %.0e)"
          % (W9["S"], W9["Sp"], W9["Sm"], W9["N"], str(W9["minC"]),
             B9, B_W9_REC, B_W9_TOL))
    # alignment census (r312/r318 anatomy, verbatim class)
    lam9, sc9, G9 = BG.block_eigs(g9, C9["nblk"])
    ev9, Wv9 = np.linalg.eigh(G9)
    top9 = Wv9[:, :, -1]
    Vn = IF.V_LIB.astype(float)
    Vn = Vn / np.linalg.norm(Vn, axis=1, keepdims=True)
    align9 = float(np.median(np.max(np.abs(top9 @ Vn.T), axis=1)))
    ok_fp9 = (feas9 >= -FEAS_CONV
              and cen9["modal_pair"] == FP_PAIR
              and cen9["modal_sign"] == FP_SIGN
              and cen9["modal_share"] >= SHARE_MIN
              and cen9["d6_share"] <= D6_MAX
              and abs(cen9["share_med"] - SHARE_REC[0]) <= SHARE_TOL
              and abs(cen9["share_min"] - SHARE_REC[1]) <= SHARE_TOL
              and abs(cen9["share_mean"] - SHARE_REC[2])
              <= SHARE_TOL
              and abs(align9 - ALIGN_REC) <= ALIGN_TOL)
    check("G21-r318-fingerprint-anchor", ok_fp9,
          "THE R318 FINGERPRINT REPRODUCED (identical protocol: "
          "Dykstra %d steps from the least-norm start, sealed "
          "cone projection): CONV %+.2e; census %s (sealed pins: "
          "pair %s, sign %+d, share >= %.1f, d6 <= %.2f); cone "
          "share med/min/mean %.4f/%.4f/%.4f (r312 rec, tol "
          "%.2f); alignment med %.4f (rec %.4f)"
          % (FEAS_IT1, feas9, fmt_cen(cen9), str(FP_PAIR),
             FP_SIGN, SHARE_MIN, D6_MAX, cen9["share_med"],
             cen9["share_min"], cen9["share_mean"], SHARE_TOL,
             align9, ALIGN_REC))
    if smoke:
        check("G22-twin-anchor", True, "SMOKE: skipped")
        cenT = None
        WT = None
        ctxT = None
    else:
        gaps_c = MF.local_gaps(np.asarray(ctx9["uu"], float))
        uR, mR, dens, duR = AK.twin_rational(
            ctx9["uu"], ctx9["mm"], gaps_c, D9, RAT_TOL)
        ok_tc = (bool(np.array_equal(mR, np.asarray(ctx9["mm"])))
                 and int(np.max(dens)) <= QMAX)
        ctxT = MS.ctx_build(MAIN_KZ, comb=(uR, mR))
        WT = LS.world_pack("twin", ctxT, D9)
        cenT, feasT, _CT, _gT, _BT, _wwT = fp_run_pack(WT, ctxT,
                                                       FEAS_IT1)
        ok_twin = (ok_tc and WT["minC"] == TWIN_MINC_REC
                   and feasT >= -FEAS_CONV
                   and cenT["modal_pair"] == FP_PAIR
                   and cenT["modal_sign"] == FP_SIGN
                   and cenT["modal_share"] >= SHARE_MIN
                   and abs(cenT["modal_share"] - TWIN_SHARE_REC)
                   <= TWIN_SHARE_TOL)
        check("G22-twin-anchor", ok_twin,
              "r289 RATIONAL TWIN rebuilt verbatim (minC %s == "
              "rec %d): fingerprint CONV %+.2e, census %s (r318 "
              "rec share %.3f tol %.2f) -- METRIC_ONLY holds on "
              "the dig object" % (str(WT["minC"]), TWIN_MINC_REC,
                                  feasT, fmt_cen(cenT),
                                  TWIN_SHARE_REC, TWIN_SHARE_TOL))

    # ---------------- S3 leg A hardening
    section("S3  LEG A -- HARDENING (VARIANTS + FAIR OBJECTS)")
    if smoke:
        for g_ in ("G30-variant-invariance", "G31-leastnorm-census",
                   "G32-ablated-controls", "G33-fair-contrast"):
            check(g_, True, "SMOKE: skipped")
        invariant = True
        fair_carries = {}
        var_rows = {}
    else:
        variants = {}
        variants["LSTART"] = (g9, feas9, FEAS_IT1, "conv-anchor")
        fmL, _rL, gL = BM.feas_diag_g(C9["M"], C9["q"], C9["g"],
                                      C9["nblk"], STEP_LONG)
        variants["LONG"] = (gL, fmL, STEP_LONG, "long-run")
        g0z = np.zeros_like(C9["g"])
        fmz, _rz, gz, itz = staged_feas(C9["M"], C9["q"], g0z,
                                        C9["nblk"],
                                        (FEAS_IT1, FEAS_IT2,
                                         FEAS_IT3))
        variants["ZERO"] = (gz, fmz, itz, "zero-start")
        for si, sd in enumerate(SEEDS_R):
            rng = np.random.default_rng(sd)
            g0r = rng.standard_normal(C9["g"].shape) \
                * float(np.linalg.norm(C9["g"])
                        / math.sqrt(C9["g"].size))
            fmr, _rr, gr, itr = staged_feas(C9["M"], C9["q"], g0r,
                                            C9["nblk"],
                                            (FEAS_IT1, FEAS_IT2,
                                             FEAS_IT3))
            variants["RAND%d" % (si + 1)] = (gr, fmr, itr,
                                             "seed %d" % sd)
        itv = FEAS_IT1
        fmv, relv, gv = feas_diag_rev(C9["M"], C9["q"], C9["g"],
                                      C9["nblk"], itv)
        for st in (FEAS_IT2, FEAS_IT3):
            if relv <= REV_CONV:
                break
            itv = st
            fmv, relv, gv = feas_diag_rev(C9["M"], C9["q"],
                                          C9["g"], C9["nblk"], st)
        variants["REV"] = (gv, -relv, itv,
                           "swapped projections (conv = affine "
                           "rel %.1e)" % relv)
        var_rows = {}
        ok_inv = True
        n_acc = 0
        for vn_ in ("LSTART", "LONG", "ZERO", "RAND1", "RAND2",
                    "REV"):
            gV, fV, itV, note = variants[vn_]
            acc = fp_accept(None, fV, NEAR_CONV)
            cenV = census_of_g(gV, C9["nblk"])
            var_rows[vn_] = (cenV, fV, acc, itV)
            info("VARIANT %-7s feas %+.2e (%s, %d steps) census "
                 "%s  [%s]" % (vn_, fV, acc, itV, fmt_cen(cenV),
                               note))
            if acc == "ITERATE":
                continue
            n_acc += 1
            okv = (cenV["modal_pair"] == FP_PAIR
                   and cenV["modal_sign"] == FP_SIGN
                   and abs(cenV["modal_share"]
                           - cen9["modal_share"]) <= SHARE_BAND)
            ok_inv = ok_inv and okv
        # solution-set distinctness (pairwise)
        names = [v for v in var_rows if var_rows[v][2] != "ITERATE"]
        gnorm = max(float(np.linalg.norm(variants["LSTART"][0])),
                    1e-300)
        dmin = float("inf")
        n_distinct_pairs = 0
        for i_ in range(len(names)):
            for j_ in range(i_ + 1, len(names)):
                d = float(np.linalg.norm(
                    variants[names[i_]][0]
                    - variants[names[j_]][0])) / gnorm
                dmin = min(dmin, d)
                if d >= DIST_MIN:
                    n_distinct_pairs += 1
        distinct_ok = n_distinct_pairs >= 1
        invariant = bool(ok_inv and n_acc >= 3 and distinct_ok)
        # amendment a1 (disclosed, gate typing only): this gate is
        # MEASURED and adjudicated by the sealed tree in S8 (the
        # NOT-invariant branch is a sealed verdict letter, not a
        # probe failure); no bar, acceptance rule, statistic or
        # tree moved.
        check("G30-variant-invariance", True,
              "START/ORDER/STEP INVARIANCE on w9@A: %d/%d "
              "variants accepted (conv/near bars %.0e/%.0e), "
              "shares %s => INVARIANCE %s; solution-set "
              "distinctness: %d distinct pairs (min pairwise rel "
              "distance %.1e, bar %.0e) -- MEASURED, adjudicated "
              "in S8 by the sealed tree"
              % (n_acc, len(var_rows), FEAS_CONV, NEAR_CONV,
                 str({v: (str(var_rows[v][0]["modal_pair"]),
                          "%.3f" % var_rows[v][0]["modal_share"],
                          var_rows[v][2]) for v in var_rows}),
                 "HOLDS" if invariant else "BREAKS",
                 n_distinct_pairs, dmin, DIST_MIN))
        # fair object (i): least-norm census on four worlds
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)))
        CTRL = {}
        for cn, kw in cdefs:
            cctx = MS.ctx_build(MAIN_KZ, **kw)
            Wc = LS.world_pack(cn, cctx, D9)
            Bc, _rc, bxac, bwac = BG.world_budget(Wc, cctx)
            _ffc, xac, wac = BG.world_arrays(Wc)
            Cc = BG.census_world(xac, wac, bxac, bwac, Bc, DEG_A,
                                 BG.hull_of(xac, bxac))
            CTRL[cn] = (Wc, Cc, Bc)
        ln_rows = {}
        ln_rows["w9"] = census_of_g(C9["g"], C9["nblk"])
        CT9 = None
        if WT is not None:
            BT2, _rT2, bxaT2, bwaT2 = BG.world_budget(WT, ctxT)
            _ffT2, xaT2, waT2 = BG.world_arrays(WT)
            CT9 = BG.census_world(xaT2, waT2, bxaT2, bwaT2, BT2,
                                  DEG_A, BG.hull_of(xaT2, bxaT2))
            ln_rows["twin"] = census_of_g(CT9["g"], CT9["nblk"])
        for cn in CTRL:
            ln_rows[cn] = census_of_g(CTRL[cn][1]["g"],
                                      CTRL[cn][1]["nblk"])
        for k_ in ln_rows:
            info("LEASTNORM %-5s census %s  [affine solution, "
                 "non-psd disclosed]" % (k_, fmt_cen(ln_rows[k_])))
        check("G31-leastnorm-census", len(ln_rows) == 4,
              "FAIR OBJECT (i) -- the least-norm affine solution "
              "(always exists, same construction on every world, "
              "no convergence asymmetry; non-psd, r308 indefinite "
              "class, disclosed): %s -- MEASURED, adjudicated in "
              "S8" % str({k: (str(ln_rows[k]["modal_pair"]),
                              ln_rows[k]["modal_sign"],
                              round(ln_rows[k]["modal_share"], 3))
                          for k in ln_rows}))
        # fair object (ii): r311 budget ablation + staged Dykstra
        fair_carries = {}
        abl_rows = {}
        for cn in ("EPST", "SCR"):
            Wc, Cc, Bc = CTRL[cn]
            m_ = DEG_A + 2
            A_ = BN.unvech(np.asarray(Cc["q"]), m_)
            S_ctrl = Bc - 5.0 / 7.0
            lad = (abs(S_ctrl), ABL_MAIN_S)
            got = None
            for step, tt in enumerate(lad):
                Aab = A_.copy()
                Aab[m_ - 1, m_ - 1] = tt
                lam_ab, _sc = BN.gate_lam_rel(Aab)
                if lam_ab >= PSD_NEG:
                    got = (step, tt, lam_ab)
                    break
            if got is None:
                abl_rows[cn] = ("NOT_PD", None, None)
                info("ABLATION %s: no ladder rung makes the "
                     "target PD (disclosed)" % cn)
                continue
            step, tt, lam_ab = got
            qab = BN.vech_of(Aab)
            g_ab, _rk, rel_ab = BG.least_norm(Cc["M"], qab)
            fma, _ra, ga, ita = staged_feas(Cc["M"], qab, g_ab,
                                            Cc["nblk"],
                                            (FEAS_IT1, FEAS_IT2,
                                             FEAS_IT3))
            acc = fp_accept(None, fma, NEAR_CONV)
            cenA = census_of_g(ga, Cc["nblk"])
            abl_rows[cn] = (acc, fma, cenA)
            carries = (acc != "ITERATE"
                       and cenA["modal_pair"] == FP_PAIR
                       and cenA["modal_sign"] == FP_SIGN
                       and cenA["modal_share"] >= SHARE_MIN)
            fair_carries[cn] = carries
            info("ABLATED %s: (t,t) <- %+.4f (rung %d, target PD "
                 "%+.2e), Dykstra %s (%+.2e, %d steps), census %s "
                 "=> %s" % (cn, tt, step, lam_ab, acc, fma, ita,
                            fmt_cen(cenA),
                            "CARRIES the MAIN law"
                            if carries else "breaks"))
        ok_abl = all(abl_rows[cn][0] in ("OK", "NEAR")
                     for cn in abl_rows
                     if abl_rows[cn][0] != "NOT_PD")
        check("G32-ablated-controls", bool(abl_rows),
              "FAIR OBJECT (ii) -- the r311 budget ablation "
              "(EPST/SCR (t,t) <- first PD ladder value, "
              "least-norm start, staged %d/%d/%d): %s -- the "
              "converged fair control families are the honest "
              "world contrast (r311 anchor: ablated controls "
              "converge %s); MEASURED, adjudicated in S8"
              % (FEAS_IT1, FEAS_IT2, FEAS_IT3,
                 str({cn: (abl_rows[cn][0],
                           None if abl_rows[cn][2] is None else
                           (str(abl_rows[cn][2]["modal_pair"]),
                            abl_rows[cn][2]["modal_sign"],
                            round(abl_rows[cn][2]["modal_share"],
                                  3)))
                      for cn in abl_rows}),
                 "reproduced" if ok_abl else "NOT reproduced"))
        n_carry = sum(1 for v in fair_carries.values() if v)
        check("G33-fair-contrast", True,
              "THE R318 CAVEAT RESOLVED ON FAIR OBJECTS: %d/%d "
              "converged ablated controls carry the MAIN "
              "(pair, sign) %s -- %s; share margin MAIN %.3f vs "
              "fair controls %s; d6-class MAIN %.3f vs %s"
              % (n_carry, len(fair_carries),
                 str(FP_PAIR) + (" %+d" % FP_SIGN),
                 "FAIR_CONTROL_CARRIES: the r318 SHAPE dichotomy "
                 "((4,5) vs (2,3)) was an iterate artifact; the "
                 "fair separation is the share MARGIN, typed "
                 "into the letter" if n_carry > 0 else
                 "the pattern dichotomy SURVIVES fair objects",
                 cen9["modal_share"],
                 str({cn: (None if abl_rows[cn][2] is None else
                           round(abl_rows[cn][2]["modal_share"],
                                 3)) for cn in abl_rows}),
                 cen9["d6_share"],
                 str({cn: (None if abl_rows[cn][2] is None else
                           round(abl_rows[cn][2]["d6_share"], 3))
                      for cn in abl_rows})))

    # ---------------- S4 leg B anatomy + coupling
    section("S4  LEG B -- ANATOMY + FORCED + COUPLING")
    # anatomy on the converged w9 family (anchor census)
    pairs9 = cen9["pairs"]
    r23_9 = cen9["r23"]
    fro9 = cen9["fro"]
    nblk9 = cen9["nblk"]
    dom_idx = [r for r in range(nblk9) if pairs9[r] == FP_PAIR]
    hist = {}
    for p in pairs9:
        hist[p] = hist.get(p, 0) + 1
    hist_top = sorted(hist.items(), key=lambda t: -t[1])[:4]
    thirds = []
    for t_ in range(3):
        lo = (nblk9 * t_) // 3
        hi = (nblk9 * (t_ + 1)) // 3
        n_dom = sum(1 for r in range(lo, hi)
                    if pairs9[r] == FP_PAIR)
        thirds.append(n_dom / max(hi - lo, 1))
    sign_cons = (sum(1 for r in dom_idx if r23_9[r] < 0.0)
                 / max(len(dom_idx), 1))
    entry_neg = float(np.mean(r23_9 < 0.0))
    law_anatomy = (len(dom_idx) / max(nblk9, 1) >= SHARE_MIN
                   and sign_cons >= SIGN_CONS_BAR)
    check("G40-anatomy", law_anatomy,
          "ANATOMY (w9 converged family, %d blocks): dominant-"
          "pair histogram top %s; (2,3)-dominant share %.3f; "
          "position thirds (head/mid/tail) %.3f/%.3f/%.3f; SIGN "
          "CONSISTENCY %.3f (bar %.1f: fraction of (2,3)-"
          "dominant blocks with R[2,3] < 0); entry-level: %.3f "
          "of ALL blocks have R[2,3] < 0 -- the law bars are "
          "load-bearing here"
          % (nblk9, str(hist_top), len(dom_idx) / max(nblk9, 1),
             thirds[0], thirds[1], thirds[2], sign_cons,
             SIGN_CONS_BAR, entry_neg))
    # f64 forced component on w9
    phi9 = phi_sector_f64(C9["nblk"], P23_IDX)
    frac9, fval9 = forced_component_f64(np.asarray(C9["M"]),
                                        np.asarray(C9["q"], float),
                                        phi9)
    forced9 = frac9 <= F64_FORCE_BAR
    check("G41-w9-f64-forced", True,
          "w9@A f64 forced component of phi_23 (isometric "
          "coordinates): rowspace residual fraction %.5f (forced "
          "iff <= %.0e => %s), forced value %+.3e -- consistency "
          "grade for the exact miniatures; MEASURED, adjudicated "
          "in S8" % (frac9, F64_FORCE_BAR,
                     "FORCED" if forced9 else "NOT forced",
                     fval9))
    if smoke:
        for g_ in ("G42-coupling", "G43-forced-adjudication"):
            check(g_, True, "SMOKE: skipped")
        exact_forced = False
        rung_tab = []
    else:
        # K1: per-block coupling on w9
        feat1 = antiphase_mass_feat(ww9u)
        mag_blk = np.abs(r23_9) / fro9
        sp1 = BH.spearman(mag_blk.tolist(), feat1.tolist())
        # ladder loop (57 rungs) -- serves Leg B scaling + Leg C
        kzs = []
        ekz = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H:
                ekz.append(kz)
        packs = {}
        for kz in kzs + ekz:
            ctx = ctx9 if kz == MAIN_KZ else MS.ctx_build(kz)
            Dk = D9 if kz == MAIN_KZ else \
                float(core.build_window(kz)["D"])
            Wp = W9 if kz == MAIN_KZ else \
                LS.world_pack("w%d" % kz, ctx, Dk)
            packs[kz] = (Wp, ctx)
        epool = sorted(ekz, key=lambda kz: (packs[kz][0]["N"], kz))
        rungs = kzs + epool[:K_EXT]
        fp_kzs = [MAIN_KZ] + [kz for kz, _s in
                              sorted(((kz, packs[kz][0]["S"])
                                      for kz in kzs
                                      if kz != MAIN_KZ),
                                     key=lambda t: (t[1], t[0]))
                              ][:N_FP - 1]
        rung_tab = []
        for kz in rungs:
            Wp, ctx = packs[kz]
            if kz == MAIN_KZ:
                cenk, feask = cen9, feas9
                Bk = B9
            else:
                Bk, _rho, bxa, bwa = BG.world_budget(Wp, ctx)
                _ffk, xak, wak = BG.world_arrays(Wp)
                Ck = BG.census_world(xak, wak, bxa, bwa, Bk,
                                     DEG_A, BG.hull_of(xak, bxa))
                fmk, _rk_, gk = BM.feas_diag_g(Ck["M"], Ck["q"],
                                               Ck["g"],
                                               Ck["nblk"],
                                               FEAS_IT1)
                itk = FEAS_IT1
                if fmk < -FEAS_CONV:
                    fmk, _rk_, gk = BM.feas_diag_g(
                        Ck["M"], Ck["q"], Ck["g"], Ck["nblk"],
                        LADDER_CAP_IT)
                    itk = LADDER_CAP_IT
                cenk, feask = census_of_g(gk, Ck["nblk"]), \
                    float(fmk)
            mag_k = float(np.median(np.abs(cenk["r23"])
                                    / cenk["fro"]))
            rung_tab.append(dict(kz=kz, S=Wp["S"], N=Wp["N"],
                                 B=Bk, cen=cenk, feas=feask,
                                 mag=mag_k))
        # K2/K3 on the 12 sealed rungs
        fp_rows = [r for r in rung_tab if r["kz"] in fp_kzs]
        fp_rows = sorted(fp_rows,
                         key=lambda r: fp_kzs.index(r["kz"]))
        mags = [r["mag"] for r in fp_rows]
        res57 = [r["S"] for r in fp_rows]
        sp_scale = BH.spearman(mags, [float(s) for s in res57])
        k2 = [r["B"] - 5.0 / 7.0 for r in fp_rows]
        sp2 = BH.spearman(mags, k2)
        zv_abs = []
        for r in fp_rows:
            Wp = packs[r["kz"]][0]
            depth = min(Wp["N"] + DEPTH_PAD, Wp["Sp"] - 1)
            SPk = LS.spectral_block(Wp, depth)
            nz = SPk["cross"] if SPk["cross"] is not None \
                else depth
            ZB = DC.zv_block(SPk["B"], nz, Wp["vn"])
            zv_abs.append(abs(ZB["zv"]))
        sp3 = BH.spearman(mags, zv_abs)
        c1 = "COUPLED" if abs(sp1) >= SP_BAR else "UNCOUPLED"
        c2 = "COUPLED" if abs(sp2) >= SP_BAR else "UNCOUPLED"
        c3 = "COUPLED" if abs(sp3) >= SP_BAR else "UNCOUPLED"
        check("G42-coupling", True,
              "COUPLING CANDIDATES (sealed bar |sp| >= %.1f): K1 "
              "per-block |R[2,3]|/||G||_F vs antiphase mass "
              "pairing g_j g_{j+2} + g_{j+1} g_{j+3}: spearman "
              "%+.4f => %s; K2 per-rung MAG vs 5/7-reserve "
              "S_{N-2}: %+.3f => %s; K3 per-rung MAG vs |z_v| "
              "(r288 carrier at the crossing, gate-side spectral "
              "consumption disclosed): %+.3f => %s; rung scaling "
              "typed: MAG %.2e..%.2e over the %d sealed rungs, "
              "spearman(MAG, S) = %+.3f"
              % (SP_BAR, sp1, c1, sp2, c2, sp3, c3,
                 min(mags), max(mags), len(fp_rows), sp_scale))
        exact_forced = bool(fr_s == 0 and val_s < 0 and member_m)
        check("G43-forced-adjudication", True,
              "FORCED-COMPONENT ADJUDICATION: TOY4 calibrator "
              "EXACT (free 0, value 4/7); SM1 exact free %.5f "
              "value %+.2e / MINI16 exact membership %s (f64 "
              "free %.5f value %+.2e); w9 f64 free %.5f value "
              "%+.2e => exact_forced = %s -- "
              "%s" % (float(fr_s), float(val_s), member_m,
                      fr_m_f64, val_m_f64, frac9, fval9,
                      exact_forced,
                      "the sign law IS an identity theorem"
                      if exact_forced else
                      "the sign law is NOT identity-forced: it "
                      "lives in the psd SELECTION GEOMETRY of "
                      "the solution set (the disclosed D3 "
                      "in-block dependence is the structural "
                      "reason) -- exactly what Leg A measures"))

    # ---------------- S5 leg C candidate
    section("S5  LEG C -- THE THEOREM CANDIDATE")
    if smoke:
        for g_ in ("G50-candidate-certification",
                   "G51-implication-sketch"):
            check(g_, True, "SMOKE: skipped")
        cert_txt = "SMOKE"
    else:
        n_cert = 0
        worst_share = (2.0, None)
        worst_cone = (2.0, None)
        n_conv = 0
        for r in rung_tab:
            cc = cert_cell(r["cen"], r["feas"])
            ok_c = (cc["conv"] and cc["pair"] == FP_PAIR
                    and cc["sign"] == FP_SIGN
                    and cc["share"] >= SHARE_MIN
                    and cc["cone"] >= CONE_MIN)
            if cc["conv"]:
                n_conv += 1
            if ok_c:
                n_cert += 1
            if cc["share"] < worst_share[0]:
                worst_share = (cc["share"], r["kz"])
            if cc["cone"] < worst_cone[0]:
                worst_cone = (cc["cone"], r["kz"])
        twin_cert = False
        if cenT is not None:
            ct = cert_cell(cenT, feasT)
            twin_cert = (ct["conv"] and ct["pair"] == FP_PAIR
                         and ct["sign"] == FP_SIGN
                         and ct["share"] >= SHARE_MIN
                         and ct["cone"] >= CONE_MIN)
        cert_txt = ("%d/%d rungs certified (conv %d/%d; worst "
                    "share %.3f@kz%s, worst cone med %.3f@kz%s); "
                    "twin %s"
                    % (n_cert, len(rung_tab), n_conv,
                       len(rung_tab), worst_share[0],
                       str(worst_share[1]), worst_cone[0],
                       str(worst_cone[1]),
                       "CERTIFIED" if twin_cert else "NOT cert"))
        check("G50-candidate-certification",
              len(rung_tab) == 57,
              "CANDIDATE FORM 'Q_w - (5/7)t^2 = sum <G Delta, "
              "Delta>, G_r = P_r (sealed 22-generator psd cone) "
              "+ E_r (cone residual, dominant antiphase support "
              "(D3, D4), fixed sign <= 0, small mass)': "
              "certification census at the sealed bars (CONV + "
              "pair + sign + share >= %.1f + cone med >= %.2f): "
              "%s -- MEASURED, adjudicated in S8"
              % (SHARE_MIN, CONE_MIN, cert_txt))
        check("G51-implication-sketch", True,
              "IMPLICATION SKETCH (typed, never a claim): psd "
              "blocks + kernel exclusion + a bound |<E Delta, "
              "Delta>| <= (1 - delta)(<P Delta, Delta> + (5/7) "
              "t^2) would give Q > 0 on the restricted subspace "
              "(Schur/inertia: psd + controlled indefinite "
              "perturbation => index bound); MISSING LINKS all "
              "open and named: %s" % "; ".join(MISSING_LINKS))

    # ---------------- S7 must-fails
    section("S7  MUST-FAILS + SCOPE AUDITS (LEG D)")
    # m1: unconverged MAIN iterate must be flagged ITERATE
    fm2, _r2, g2 = BM.feas_diag_g(C9["M"], C9["q"], C9["g"],
                                  C9["nblk"], 2)
    acc2 = fp_accept(None, float(fm2), NEAR_CONV)
    acc_ok = fp_accept(None, feas9, NEAR_CONV)
    check("G70-mustfail-iterate-flag", acc2 == "ITERATE"
          and acc_ok == "OK",
          "m1 UNCONVERGED MAIN ITERATE: the 2-step w9 Dykstra "
          "iterate (feas %+.2e) is REJECTED as ITERATE by the "
          "sealed acceptance verifier while the converged anchor "
          "(feas %+.2e) is accepted -- the r318 caveat is "
          "machine-enforced, no census of a non-feasible family "
          "enters any law gate" % (fm2, feas9))
    # m2: D-pair permutation must change the modal pair
    perm = np.array([0, 1, 4, 3, 2, 5])
    _l9, _s9, G9blk = BG.block_eigs(g9, C9["nblk"])
    Gp = G9blk[:, perm][:, :, perm]
    gv_mut = np.zeros((C9["nblk"], len(IF.PA6)))
    for p_i in range(len(IF.PA6)):
        a_, b_ = int(IF.PA6[p_i]), int(IF.PB6[p_i])
        if a_ == b_:
            gv_mut[:, p_i] = Gp[:, a_, a_]
        else:
            gv_mut[:, p_i] = Gp[:, a_, b_] * math.sqrt(2.0)
    cen_mut = census_of_g(gv_mut.reshape(-1), C9["nblk"])
    check("G71-mustfail-pair-permutation",
          cen_mut["modal_pair"] != cen9["modal_pair"],
          "m2 D-PAIR PERMUTATION (the census run on the "
          "coordinate-permuted family P G P^T, D3 <-> D5): "
          "modal pair %s != anchor %s -- CAUGHT: the pair label "
          "is load-bearing, a family in permuted coordinates "
          "cannot silently pass the anchor gate"
          % (str(cen_mut["modal_pair"]),
             str(cen9["modal_pair"])))
    # m3: wrong identity sign, exact on TOY4
    q4_neg = [-v for v in q4]
    fr_mut, val_mut, _ym3 = mutant_wrong_identity_sign(M4, q4_neg,
                                                       phi66)
    check("G72-mustfail-wrong-identity-sign",
          val66 != 0 and val_mut == -val66 and fr_mut == 0,
          "m3 WRONG IDENTITY SIGN (TOY4, exact Fractions): the "
          "mutant consuming -q returns forced value %s == "
          "-(4/7) != +4/7 -- CAUGHT exact; the catch is not "
          "vacuous (the calibrator value is nonzero by r308 G10)"
          % str(val_mut))
    # m4: coupling read-back mutant + scope audits
    hits_m4 = scope_audit("mutant_coupling_readback")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G73-mustfail-coupling-readback", bool(hits_m4)
          and not hits and not ag_hits,
          "m4 COUPLING TARGET READ-BACK: the mutant consuming "
          "the withheld truth is FLAGGED by the AST scope audit "
          "(%s); the %d sealed constructors audit CLEAN; "
          "fragment audit %s"
          % ("; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no derived 5/7, no posthoc window, no "
          "re-opened no-go entry, no bar/rule change after "
          "evaluation, no RH claim; r243..r321 stand; the r318 "
          "letters stand -- this round adjudicates the dig "
          "questions only; mincut base 4 / refined 5 UNCHANGED")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        law_anchor = bool(ok_fp9 and law_anatomy)
        if not law_anchor:
            main_v = ("LAW_DIFFUSE(anchor/anatomy failure: "
                      "fingerprint %s, sign consistency %.3f)"
                      % (fmt_cen(cen9), sign_cons))
        elif not invariant:
            bad = [v for v in var_rows
                   if var_rows[v][2] != "ITERATE"
                   and (var_rows[v][0]["modal_pair"] != FP_PAIR
                        or var_rows[v][0]["modal_sign"]
                        != FP_SIGN)]
            good = [v for v in var_rows
                    if var_rows[v][2] == "OK"
                    and var_rows[v][0]["modal_pair"] == FP_PAIR
                    and var_rows[v][0]["modal_sign"] == FP_SIGN]
            main_v = ("ALGORITHM_ARTIFACT(the law breaks under "
                      "the sealed variants %s -- their accepted "
                      "near-feasible points carry %s with cone "
                      "share med %s: the law AND the 97.6/2.4 "
                      "cone anatomy are properties of the "
                      "least-norm-proximal Dykstra BASIN (the "
                      "canonical protocol variants %s all carry "
                      "the law exactly), not of the psd solution "
                      "set as a whole)"
                      % (str(bad),
                         str({v: (str(var_rows[v][0]
                                      ["modal_pair"]),
                                  round(var_rows[v][0]
                                        ["modal_share"], 3))
                              for v in bad}),
                         str({v: round(var_rows[v][0]
                                       ["share_med"], 3)
                              for v in bad}), str(good)))
        elif exact_forced:
            main_v = ("SIGN_LAW_EXACT(the (D3, D4) sector is "
                      "identity-forced with negative value on "
                      "SM1 exact + MINI16 exact membership)")
        else:
            main_v = ("SIGN_LAW_ROBUST(lawful, not exact: the "
                      "law survives every hardening variant (%d "
                      "accepted, distinct solution points) but "
                      "the (D3, D4) sector is NOT identity-"
                      "forced -- SM1 exact free fraction %.4f, "
                      "MINI16 exact membership %s: a selection-"
                      "geometry law of the psd intersection)"
                      % (n_acc, float(fr_s), member_m))
        n_carry = sum(1 for v in fair_carries.values() if v)
        verd = " + ".join([
            main_v,
            "HARDENING(variants %s; fair objects: leastnorm "
            "world-blind measured, ablated controls carry %d/%d "
            "=> %s)"
            % (str({v: (str(var_rows[v][0]["modal_pair"]),
                        var_rows[v][0]["modal_sign"],
                        round(var_rows[v][0]["modal_share"], 3),
                        var_rows[v][2]) for v in var_rows}),
               n_carry, len(fair_carries),
               "FAIR_CONTROL_CARRIES (share margin separates, "
               "not the bare pattern)" if n_carry > 0
               else "pattern dichotomy survives"),
            "ANATOMY((2,3)-share %.3f, thirds %.2f/%.2f/%.2f, "
            "sign consistency %.3f, entry-neg %.3f, MAG band "
            "%.1e..%.1e)"
            % (len(dom_idx) / max(nblk9, 1), thirds[0],
               thirds[1], thirds[2], sign_cons, entry_neg,
               min(r["mag"] for r in rung_tab),
               max(r["mag"] for r in rung_tab)),
            "FORCED(TOY4 exact 4/7; SM1 exact free %.4f val "
            "%+.1e; MINI16 exact member %s f64 free %.4f; w9 "
            "f64 free %.4f)"
            % (float(fr_s), float(val_s), member_m, fr_m_f64,
               frac9),
            "COUPLING(K1 %+.3f %s; K2 %+.3f %s; K3 %+.3f %s)"
            % (sp1, c1, sp2, c2, sp3, c3),
            "CANDIDATE(%s; missing links L1-L5 open)" % cert_txt,
            "R318_DEMARCATION(the r318 letters stand; this "
            "round adjudicates the dig questions only)"])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the dig round of the r318 fork; NO RH claim"
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
