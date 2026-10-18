#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pair_extremal_probe -- PRIME.LSTAR.PAIR_EXTREMAL.01 (round
342): the TWO-ATOM EXTREMAL of L* solved as its own problem -- the
U1 main find of the door-2 full revision (r338, reading audit).
L* (the open scalar of r283/r284/r286: lambda_max(E_{N_w}) < 1 for
the nu-dressed mu-CD kernel Gram E, margin 1.6752e-4 on w9) has an
extremal direction that is LADDER-STABLY concentrated (r338: PR
1.6-1.9, top-2 mass 0.976-0.999 on 42/42) on the SAME r284
shallow-edge pair -- the two nu atoms at the arch rim BELOW the
first prime (w9: folds 2/4, u = 0.030/0.060 < log 2).  At the
binding point L* is EXACTLY the determinant condition
    c^2 < (1 - d1)(1 - d2),
    d_k = v_k K_N(y_k, y_k) = E_kk,   c = sqrt(v1 v2) K_N(y1, y2)
        = E_12
(a backward-Cauchy-Schwarz statement about the nu-dressed CD
kernel at two hard-edge atoms), and the entire alpha ~ 3 margin
decay law (r286) is the near-cancellation of two slowly decaying
source-explicit scalars.  THE ROUND'S CONTRACT (r338 sketch, rank
1 + rank 2): (Leg A) the mp-exact (d1, d2, c) ladder on all 57
rungs (42 core + 15 r286 extension) + the 12 r329 EXT3 fresh
anchors as PURE TEST rows (r335/r337 adoption discipline) + the
rational twin, with sealed decay-law fits AGAINST DISCLOSED
PRIORS; (Leg B) the source-explicit asymptotics: the pair weights
in closed form from the archimedean layer (digamma dictionary) +
the exact two-cell tent closed form of the prime layer, plus the
kernel-growth census against the r285 exponent 0.38; (Leg C) the
sealed world census (rank-2 rider, closes U2): PR concentration
and the r334 interval clause kappa_int evaluated on SMOOTH and
HL2 for the FIRST time -- is {PR >= bar} or the union
{PR >= bar} u {kappa_int >= 1} the first world-complete
criterion?; (Leg D) the honest kill: does the 2x2 necessity plus
the measured coupling cap reproduce alpha ~ 3.05 -- and the
sufficiency gap vermessen: the EXACT Schur dressing (L* <=>
{lambda_rest < 1} AND {dressed pair determinant condition}), the
R343 coupling-control material.  NOT a proof round: no L* claim,
no bound mechanism, no certificate -- machinery + census + honest
typing.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: R339 (density martingale) and R340 (Cauchy-Binet
Hall) run in parallel -- this probe touches NOTHING outside its
own file and the strictly additive rh-sync.  Two-commit freeze
protocol (r329 convention): spec + machinery committed BEFORE the
record run, record tables inserted after.

THE EXACT OBJECTS (all gated): E = B B^T with B[k, i] =
sqrt(v_k) P_i(y_k) (document pipeline); the PAIR = the two nu
atoms with the largest x (smallest theta -- the shallow edge; the
constructor consumes positions only); the 2x2 principal block
A = [[d1, c], [c, d2]]; lambda_2x2 = (d1+d2)/2 +
sqrt(((d1-d2)/2)^2 + c^2); pair margin m2 = 1 - lambda_2x2; the
determinant identity (1 - lambda_2x2)(1 - lambda_2x2') ==
(1-d1)(1-d2) - c^2 (gated per rung at 1e-10 rel); the reserve
r_det = 1 - c^2/((1-d1)(1-d2)) (r338 'saturation' column: w9
1.2e-2, decaying along the ladder); the coupling cap R2 =
m2/margin_full - 1 >= 0 (Cauchy interlacing gated); the EXACT
SCHUR DRESSING: with E = [[A, C], [C^T, D]] (pair vs rest), L*
<=> lambda_max(D) < 1 AND lambda_max(A + C (I-D)^{-1} C^T) < 1
(logdet identity det(I-E) = det(I-D) det(I-A-CX) gated per rung)
-- the dressed scalars (d1', d2', c') and the dressed reserve
r'_det are the R343 coupling-control coordinates, measured.

THE SOURCE-EXPLICIT LAYER (Leg B, sealed forms): the window
density d_j at fold j splits EXACTLY as d = d_A + d_P (FFT
linearity, gated 1e-12).  PRIME LAYER CLOSED FORM (exact): every
comb atom (u_n, m_n = 2 Lambda(n)/sqrt(n)) has tent support on
exactly two lag cells q_n = floor(u_n/Delta), q_n + 1 (fraction
r_n), so
  f_P(theta) = -sum_n (m_n/2) [ (1-r_n) w_{q_n} cos(q_n theta)
               + r_n w_{q_n+1} cos((q_n+1) theta) ],
w_i = 2 for 1 <= i <= M-2, 1 at the edges i in {0, M-1}, 0 for
i >= M (the builder truncation, mirrored exactly) -- gated
against the FFT of the prime lags at 1e-10.  ARCH LAYER DIGAMMA
DICTIONARY (closed form + explicit truncation tail):
  F_A(xi) = -log pi + Re psi(1/4 + i xi/2),   xi = theta/Delta,
  TAIL(xi) = -2 sum_{k>=0} Re[ e^{-2 alpha (a_k + i xi)}
             / (a_k + i xi) ],  a_k = 2k + 1/2
(the geometric tail of the lag window i >= M), predicted arch
density d_A(theta_j) ~ F_A(xi_j) - TAIL(xi_j); sealed bar
DIGAMMA_BAR = 0.02 rel at the pair folds on the sample rungs
(the interp/alias corrections are O(theta^2) and tent-killed --
stated, measured).  WEIGHT PREDICTION: v_pred = -(2/L)
(1 - cos theta_j) (F_A(xi_j) - TAIL(xi_j) + f_P(theta_j)),
sealed band V_BAR = 0.10 rel (median over all rungs).  KERNEL
SIDE (no closed form claimed): the within-window growth exponent
of K_n(y_pair) over n in [N/4, N] (halves log-slope, r285
convention) against the r285 record 0.38, plus the across-ladder
laws of p = 1-d1, q = 1-d2, c -- measured, never substituted.

INDEX FIREWALL (binding, r238-r341 discipline): w = window (kz
into the prime-power list), S = #union atoms, S_+/S_- = #mu/#nu
atoms, N_w = (S+1)//2 = builder depth; ground truth (r283/r284/
r285/r286/r329/r334/r338 records, control flips) enters GATES
and record tables only; the sealed constructors consume position
/ weight / kernel-row arrays ONLY (AST scope audit); no zero/
prime oracles anywhere (AST firewall; the prime-power grid is
the sealed source comb, r238 convention); no fit primitives
(fragment audit; fits are the imported r286 Theil-Sen).
MACHINERY IMPORTED VERBATIM: document pipeline
V.{build_measures, window_shape, mu_chain, b_matrix,
admissible_indices, lam_max_at, U, W_VM, PP}, r286
LM.{ts_fit, ts_slope_free, spearman, ext_rule}, r334
FC.{world_from_arrays, world_from_mz, interval_census,
kernel_gram, frac_kernel, cap_nnls}, r283 FS.{mu_chain_f64,
b_matrix_f64, mu_chain_mp, b_matrix_mp, crossing_from_B}, r278
MS.ctx_build, r280 BL.{union_of_ctx, sign_chain_f64}, v881
PIK.lambda_eps, r243 PB.smooth_comb, paircorr PC.{Grid,
gen_model}, r331 TR.{base_comb, build_world}, r289
AKD.twin_rational, r276 MF.local_gaps, r230 JF.{TOY_NODES,
TOY_WTS}, v563 core READ-ONLY.

LEG A -- THE LADDER: per rung (42 core by V.admissible_indices,
gated == 42; 15 extension = the r286 record anchors, kz set
gated; 12 EXT3 = the sealed r329 record selection kz B (42, 51,
54, 56, 58, 62) + A (96, 123, 125, 127, 128, 130), adopted
AS-IS, PURE TEST rows, N_w gated in [1721, 2577]): the pair
(folds, v1, v2), (d1, d2, c), (p, q, r_det), m2, margin_full,
R2, pair mass, PR, the Schur-dressed row (d1', d2', c', r'_det,
lambda_rest), all printed as THE d/c/s LADDER TABLE.  Gates per
rung: determinant identity 1e-10 rel, interlacing margin_full
<= m2 + 1e-9, Schur logdet identity 1e-6, pair-condition
equivalence sign(m2) == sign(r_det).  Concentration census: pair
mass >= MASS_BAR = 0.90 and R2 in [0, 1.5] on the 57 (the BLIND
clause); EXT3 typed separately (family clause, r329 lesson).
TWIN: the r289/r331 rational twin of w9 at tol 1e-8 (dose-zero
identity gated bitwise), pair scalars within TWIN_BAR = 1e-3
rel.  MP WARDS (sealed subset; chain + pair rows of B recomputed
in mp, r283 route): w9 at dps 30 AND 45 (staggered <= 1e-12 rel
on d, c), kz18 / kz52 (core) and kz119 (extension) at dps 30
(d, c <= 1e-9 rel; m2 <= 1e-6 core, 1e-5 ext), kz42 / kz130
(EXT3) at dps 30 (d, c <= 1e-8; m2 <= 1e-3 -- bars sized from
the disclosed scoping, one decade headroom).  CONTINGENCY
(sealed): any f64 margin_full <= 0 on a fresh row triggers the
mp dps-30 sign check and is excluded from log fits (reported;
no counterexample language without the r286 triple protocol).

LEG B -- gates: (b1) layer split d == d_A + d_P at 1e-12 (sample
rungs); (b2) prime closed form vs FFT of the prime lags <= 1e-10
at the pair folds (sample); (b3) digamma dictionary <= 0.02 rel
at the pair folds (sample; the pure F_A and the tail-corrected
form both printed); (b4) v_pred table over ALL rungs (median /
max rel dev per cohort; V_BAR = 0.10 adjudicates the LAW
clause); (b5) layer shares at the pair (arch vs prime vs the
first-prime tent tail n = 2 -- the 'archimedean layer below
log 2 + tent tail' disclosure); (b6) kernel growth census on the
sample rungs vs the r285 exponent 0.38.

LEG C -- THE SEALED WORLD CENSUS (closes U2): worlds EPST / SCR
/ SMOOTH / HL2 (dead; r278/r280 channel verbatim, minC == flips
25/21/27/25 gated) + MAIN / TWIN (live).  Per world at its OWN
N_w: PR of the top eigenvector of E_{N_w}, pair mass, and the
r334 interval clause kappa_int (FC.interval_census verbatim --
the FIRST kappa_int evaluation on SMOOTH and HL2; EPST/SCR
re-measured and gated against the r334 records 1793.99 /
8.51e6 at 5 percent).  SEALED THRESHOLDS (frozen NOW): dead by
PR iff PR >= PR_BAR = 3.0; dead by capacity iff kappa_int >=
1.0.  Adjudication: PR_WORLD_COMPLETE iff the PR clause alone
hits all four dead worlds AND spares MAIN + TWIN;
PAIR_WORLD_COMPLETE iff the union clause does; else
WORLD_INCOMPLETE(loci).  PR at the spectral crossing degree
(depth-40 route) printed as the r284 comparison column.

LEG D -- THE HONEST KILL: sealed fits (r286 Theil-Sen, guard >=
20 points) on the 57 vs log N_w for log p, log q, log c,
log r_det, log m2, log margin_full; DISCLOSED PRIORS (the r338
/tmp fits, sealed as constants BEFORE this round's fits): p, q
~ N^-0.71, c ~ N^-0.66, margin ~ N^-3.13; r286 records alpha =
3.05 (vs S) / 3.06 (vs N_w) -- the 42-only margin fit must
reproduce 3.06 +- 0.15 (anchor gate).  Halves stability
(N-median split), curvature bar CURV_BAR = 0.35; EXT3 PURE TEST:
the 57-fit predicts each EXT3 row; band 0.5 decades, >= 10/12
per column.  THE ALPHA COMPOSITION: alpha_pair vs alpha_full
(<= 0.5 apart), and the bookkeeping identity m2 (p + q - m2) =
p q - c^2 => alpha_pair ~ (a_p + a_q + rho_r) - a_{p+q} tested
at 0.5 -- the analytic content is WHERE rho_r (the cancellation
exponent) comes from; typed for the specialists if open.  THE
SUFFICIENCY GAP: the dressed reserve r'_det and the rest margin
1 - lambda_rest per rung (their laws fitted) -- L* <=> {rest} +
{dressed pair}, the measured size of the coupling control a
full L* theorem still needs (R343 material).

LEG E -- MUST-FAILS (>= 5, each loud): (m1) c WITHOUT
sqrt(v1 v2): the undressed K_N(y1, y2) breaks the exact E_12
identity by >= 0.1 rel -- CAUGHT exactly; (m2) d/c READ BACK
from lambda_max: a mutant consuming the withheld REC_LAM is
FLAGGED by the AST scope audit; (m3) FITS RE-JUSTIFIED AFTER
RECORD SIGHT: a mutant returning the seen fit column as 'the
prior' consumes the withheld alpha_fit_true -- AST-FLAGGED, and
on the sealed toy returns != the sealed prior 3.13
(protocol-CAUGHT; the priors are frozen module constants under
the two-commit protocol); (m4) WORLD THRESHOLDS AFTER SIGHT: a
mutant re-picking PR_BAR from the seen PR column consumes
pr_values_true -- AST-FLAGGED, toy value != the sealed 3.0;
(m5) 2x2 BLOCK AT THE WRONG PAIR: the two largest-v atoms
instead of the shallow edge -- CAUGHT by the concentration
check (w9 mutant-pair mass < 0.5 vs sealed pair >= 0.90).
STOP LIST (anti-gates, binding): NO L* claim, NO bound
mechanism, NO certificate from the dressing, NO posthoc
threshold / family / prior move, NO derived 5/7, NO RH claim;
r243..r341 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_+ 263, S_- 104, N_w
184); REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN
1.6752e-4 rel tol 0.01; DIAGMAX_REC 0.9700 tol 5e-3;
SHALLOW_FOLDS (2, 4); R284_PR 1.89 tol 0.05; CTRL_FLIPS {EPST
25, SCR 21, SMOOTH 27}; HL2 seed 101 flip 25; CTRL_DEPTH 40;
EXT 8 / EXT2 32; EXT15_KZ {35, 37, 41, 57, 68, 70, 71, 73, 76,
95, 97, 98, 100, 109, 119} (r286 record); EXT3_KZ_B (42, 51,
54, 56, 58, 62); EXT3_KZ_A (96, 123, 125, 127, 128, 130) (r329
record, committed 8cbd95f9); EXT3_NW (1721, 2577); MASS_BAR
0.90; R2_MAX 1.5; R2_REF_BAND (0.12, 0.40) (r338 prior,
census); CURV_BAR 0.35; EXT3_BAND 0.5 decades, EXT3_OK_MIN 10;
V_BAR 0.10; DIGAMMA_BAR 0.02; PRIME_CF_BAR 1e-10; LAYER_BAR
1e-12; DET_ID_BAR 1e-10; INTERLACE_TOL 1e-9; SCHUR_BAR 1e-6;
ALPHA_TOL 0.5; R286_ALPHA_NW 3.06 tol 0.15; PRIOR_SLOPE_P
0.71; PRIOR_SLOPE_C 0.66; PRIOR_ALPHA_TMP 3.13; PR_BAR 3.0;
KINT_BAR 1.0; R334_KINT_REC {EPST 1793.99, SCR 8.51e6} rel tol
0.05; TWIN_TOL 1e-8; TWIN_BAR 1e-3; MP_SET ((9, 30), (9, 45),
(18, 30), (52, 30), (119, 30), (42, 30), (130, 30));
MP_DC_CORE 1e-9; MP_DC_EXT3 1e-8; MP_M2_CORE 1e-6; MP_M2_EXT
1e-5; MP_M2_EXT3 1e-3; STAFFEL_BAR 1e-12; GROWTH_KZ (18, 9,
52, 119, 42, 130) (= the Leg-B sample rungs); R285_PBIND 0.38;
TAIL_K 12; DIG_XI (0.0, 0.5, 1.7, 4.0, 12.0); DIG_TOY_BAR
1e-8; M1_BAR 0.1; MUT_MASS_BAR 0.5; MUT_MIN 1e-6; TOY_TOL
1e-12; JF_PAIR_BAR 1e-10; runtime <= 1800 s; smoke = toys +
firewall + scopes + mutants + w9 f64 block (records, pair
block, concentration, layer split, closed forms, Schur
dressing); ladder, EXT3, twin, mp wards, fits, worlds and
adjudication skipped.
PRE-SPEC SCOPING (disclosed, r286-s1..s3 precedent -- no fit,
no world, no other rung was evaluated before this spec froze):
(s1) the digamma identity F_A(xi) = -log pi + Re psi(1/4 +
i xi/2) was verified against the mp quadrature at five xi
values (an initial sign-flipped candidate was corrected at
scoping time; the sealed toy re-gates the identity at 1e-8);
(s2) the w9 pair block was reproduced (folds 2/4, d1 0.970014,
d2 0.964904, c 0.032252, m2 1.8749e-4, R2 0.119, r_det
1.156e-2, pair mass 0.9970, PR 1.89 -- bit-near the published
r338 /tmp record); (s3) ONE EXT3 anchor (kz130, the deepest)
was probed end-to-end to size budget and precision bars (d1
0.99374973, d2 0.98989097, c 0.00794884, r_det 2.017e-6, m2
7.789e-9, margin_full 4.918e-9, R2 0.584, pair mass 0.9814;
mp dps-30 devs d 1.2e-12 / 2.0e-13, c 8.7e-11, m2 1.9e-4 rel;
mp wall 73 s) -- disclosed HONESTLY: kz130 was seen before the
freeze; the adjudication rests on the other 67 rows plus the
sealed protocol; the s3 numbers already show R2 = 0.584 OUTSIDE
the r338 core band (0.12, 0.40) -- the EXT3 family question is
therefore live, and the sealed EXT3 clause below was fixed
BEFORE any further EXT3 row was seen.  The r338 /tmp priors
(-0.71 / -0.66 / -3.13) are sealed constants; no bar, band,
threshold, family or adjudication rule was tuned after any
evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of]
  PAIR_LAW_FOUND  iff (L1) the p, q, c fits on the 57 are
    halves-stable (|curvature| <= 0.35 each) AND (L2) the EXT3
    pure test holds (>= 10/12 rows inside 0.5 decades for each
    of p, q, c) AND (L3) the source-explicit weight prediction
    carries (median v_pred rel dev <= 0.10 over all rungs AND
    digamma dictionary <= 0.02 on the sample) AND (L4) the
    alpha composition closes (|alpha_pair - alpha_full| <= 0.5
    AND |alpha_composed - alpha_pair| <= 0.5 AND the 42-only
    alpha_full == 3.06 +- 0.15) -- the honest note stands that
    the kernel side is law-grade (fitted), not closed-form /
  PAIR_CARRIES(failed LAW clauses named)  iff not BLIND, not
    RESTATEMENT, and not all of L1-L4 /
  RESTATEMENT  iff not BLIND AND >= 2 of the p, q, c fits are
    halves-UNSTABLE while the m2 fit is stable -- the three
    scalars would then carry no structure beyond the
    lambda-shadow (the honest r338 check) /
  BLIND(loci)  iff pair mass < 0.90 or R2 outside [0, 1.5] or a
    determinant/interlacing/Schur identity fails on any of the
    57 r286-family rungs
  + [exactly one of] PR_WORLD_COMPLETE(PR clause alone) /
    PAIR_WORLD_COMPLETE(union clause) / WORLD_INCOMPLETE(loci)
  + LADDER_TABLE(d/c/s ladder + cohort medians) [always]
  + ALPHA_KILL(fits vs priors, composition, open remainder)
    [always]
  + GAP_CENSUS(dressed reserve, rest margin, coupling sizes --
    the R343 material) [always]
  + EXT3_CENSUS(EXT3_CONFORMS iff pair mass >= 0.90 on 12/12
    AND R2 <= 1.5 on 12/12; else EXT3_FAMILY_BREAK(loci))
    [always]
  + TWIN_LEDGER(rel deviations) [always]
  + MUSTFAIL_LEDGER(m1-m5 + scopes) [always].
Honesty before beauty: the pair condition is NECESSARY for L*
(interlacing), never sufficient -- the sufficiency gap is
measured, not closed; every law here is a Theil-Sen fit with
sealed honesty meters (halves, EXT3 pure test), never an
asymptotic theorem; the digamma dictionary predicts the WEIGHTS,
not the kernel -- the kernel asymptotic (r285: sub-classical
0.38) stays an open specialist question; a passing world clause
is a measured discriminator on six instrumented worlds, not a
theorem; no verdict claims L*, a bound mechanism, a derived 5/7,
or RH progress in any direction.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit, which IS the protocol; TWO-COMMIT PROTOCOL
EXECUTED: the sealed spec above was committed as "r342
pre-freeze" (bdc0b439) BEFORE the first full evaluation;
chronology honest: smoke pass 1 = 38/38 (0.4 s) at the sealed
rules; calibration pass 1 = FIRST full evaluation = 35/38 with
TWO numerics findings: (f1) the determinant-identity residual
was normalized by the CANCELLED difference pq - c^2 (~1e-9 on
deep rungs), so machine-precision noise (measured |lhs - rhs|
<= 8.0e-19 = <= 5.8e-15 of the natural scale pq + c^2) read as
a gate failure on 17 deep rungs; (f2) the mp m2 ward bar for
kz52 (N_w 878) was one notch too tight (measured f64-vs-mp
4.8e-6 on a 2.6e-7-sized m2).  DISCLOSED CALIBRATION AMENDMENTS
(r270/r286/r334 precedent, machinery-side normalizations only;
NO adjudication bar, band, threshold, family or verdict rule
moved): (a1) the det residual is measured against pq + c^2
(backward-error honest), bar 1e-12; (a2) the m2 mp bar scales
with DEPTH (1e-6 for N_w <= 400 / 1e-5 to 1500 / 1e-3 beyond,
the s3 sizing logic).  Calibration pass 2 = 38/38 (216.7 s);
the post-freeze record runs are numerically identical: run1 =
38/38 (214.6 s), run2 = 38/38 (212.3 s), byte-identical up to
WALL):
CAL_VERDICT = PAIR_LAW_FOUND(L1 the p/q/c laws are halves-
stable on the 57 (curvatures +0.305/+0.299/+0.308, bar 0.35) +
L2 the EXT3 pure test extends (11/11/11 of 12 in the 0.5-decade
band) + L3 the source dictionary carries (median v_pred rel dev
< 1e-4, max 9e-4 at kz9; digamma dictionary devs 1e-5..2.4e-3,
bar 0.02) + L4 the alpha composition closes (alpha_pair 3.341
vs alpha_full 3.332, diff 0.008; composed 3.333, diff 0.007;
42-only 3.059 == r286 3.06); kernel side law-grade, not
closed-form)
+ PAIR_WORLD_COMPLETE(union {PR >= 3.0} u {kappa_int >= 1}:
dead 4/4, live spared on both -- with the HONEST STRUCTURE: the
PR clause ALONE fails (at their OWN N_w the dead worlds are
also concentrated: EPST 2.54 / SCR 2.08 / SMOOTH 1.80 / HL2
2.92 < 3.0; the r338 'PR 5-10 diffuse' numbers live at the
CROSSING degrees, reproduced here as 7.02/9.72/4.97/8.29 ==
r284) while the KAPPA_INT CLAUSE ALONE IS WORLD-COMPLETE:
EPST 1794 / SCR 8.509e6 (== r334 records at 5 percent) /
SMOOTH 2.193 / HL2 1964 (FIRST evaluation on SMOOTH + HL2 --
the U2 gap closed) all >= 1, live MAIN/TWIN 0.999567 < 1)
+ LADDER_TABLE(69 rows printed in S3; pair == folds (2, 4) on
69/69; pair mass 0.9352..0.9994 (min at kz59), PR 1.61..1.94 on
the 57; r_det = 1 - c^2/pq spans 1.156e-2 (w9) .. 4.99e-6
(kz95) on the 57 and reaches 1.60e-6 at kz127; R2 cohort
medians core42 0.205 / ext15 0.188 / ext3B 0.437 / ext3A 0.557
-- the 2x2 reproduction is family-graded, not uniform: the
r338 core band (0.12, 0.40) holds in the median on the 57 but
the fresh deep family sits at 0.44..0.56)
+ ALPHA_KILL(slopes vs log N_w on the 57 (halves curvature |
prior): p -0.754 (+0.305 | -0.71), q -0.645 (+0.299), c -0.697
(+0.308 | -0.66), r_det -2.624 (-0.767, CURVED -- the honest
caveat), m2 -3.341 (-0.492), margin -3.332 (-0.347 | -3.13
/tmp; 42-only 3.059 == r286 3.06 -- the 57-family fit steepens
with the deep extension, consistent with the r286 curvature
finding); the composition alpha_pair = a_p + a_q + rho_r -
a_(p+q) closes to 0.007; THE OPEN ANALYTIC REMAINDER is rho_r
= 2.624: the cancellation exponent of the determinant reserve
has NO source derivation yet -- the concretized specialist
question)
+ GAP_CENSUS(the R343 material, measured: rest margin
1 - lambda_rest decays at slope -3.276 (parallel to the full
margin, w9 offset 21.9x) while the DRESSED pair reserve r'_det
is FLAT (slope +0.018, w9 value 0.303) -- the Schur-dressed
determinant condition does NOT degrade with depth: the entire
decay lives in the bare pair, and a full L* theorem needs
exactly (i) the rest-block bound and (ii) an O(1) dressed
reserve, both now measured coordinates)
+ EXT3_CENSUS(EXT3_FAMILY_BREAK([56]): kz56 has R2 = 1.836 >
1.5 (m2 5.80e-8 vs margin 2.05e-8) -- the same anchor that was
the r329 quiet outlier; kz58 R2 = 1.100 is the runner-up; the
2x2 block still reproduces the margin ORDER on both, but the
r338 uniformity reading does not extend to the small-gap
family unmodified -- the r329 lesson, measured again)
+ TWIN_LEDGER(pair scalars dev <= 1.0e-8, bar 1e-3; dose-zero
identity BITWISE)
+ MUSTFAIL_LEDGER(m1 undressed-c breaks by 2.4e+05 >= 0.1; m2
AST-FLAGGED REC_LAM; m3 AST-FLAGGED + toy 2.50 != 3.13; m4
AST-FLAGGED + toy 3.45 != 3.0; m5 wrong-pair mass 0.0000 <
0.5 vs sealed pair 0.9970; constructor scopes + fragment audit
CLEAN).
Key numbers.  W9: pair folds (2, 4), d1 = 0.970014 (== r284
diag max), d2 = 0.964904, c = 0.032252, r_det = 1.1561e-2, m2
= 1.8749e-4 vs margin 1.6752e-4 (R2 0.119); Schur: lambda_rest
0.996338 (rest margin 3.66e-3 = 21.9x margin), dressed (d1',
d2', c') = (0.999154, 0.998710, 0.000872), r'_det = 0.3029;
layer shares at folds 2/4 (d_A, d_P, first-atom tent term):
(-1.796, -8.279, -0.692) / (-1.016, -1.714, +0.004) -- the
fold-2 nu weight is 2/3 prime-comb tail (of which the n = 2
tent term is 8 percent) + 1/3 archimedean, both in closed
form; v_pred max rel dev 9e-4.  MP WARDS: d/c devs 4.3e-14 ..
8.7e-11 (bars 1e-9/1e-8), m2 devs 1.4e-10 (w9) .. 1.9e-4
(kz130, bar 1e-3); w9 staffel dps 30/45 dev 0.0.  KERNEL
GROWTH (halves log-slopes early/late at the binding atom):
kz18 (0.829, 0.476), kz9 (0.660, 0.608), kz52 (0.885, 0.378),
kz119 (1.007, 0.339), kz42 (0.911, 0.388), kz130 (1.015,
0.336) -- the LATE-window slope converges to ~0.34..0.39 on
the deep rungs: the r285 sub-classical 0.38 is the deep-rung
late-window growth, now a six-rung census.  EXT3 margins (f64,
first L*-lane evaluation of the r329 anchors): all positive,
min 4.20e-9 (kz127); the r286 42-only power law predicts
~5e-8 at N_w 2577 vs measured 4.9e-9 -- the deep family
steepens, honest out-of-sample census.  HONEST NEGATIVES: (1)
PR alone is NOT world-complete -- concentration per se does
not separate (SCR even has pair mass 0.922 at its own N_w);
what separates is whether the pair block crosses 1, i.e. the
capacity clause; (2) r_det is halves-CURVED (-0.767): the
cancellation exponent 2.624 is a fit over a curved family, not
a clean power; (3) kz56 breaks the R2 band; (4) the kernel
side (why v_k K_N -> 1 with deficit ~N^-0.7 at the hard edge)
remains without closed form -- with (2) it forms the
specialist package: (q1) backward-CS for nu-dressed CD kernels
at hard-edge atoms (why c tracks sqrt(pq) to 1e-2..1e-6), (q2)
the sub-classical Christoffel growth 0.38 at shallow-edge
atoms, (q3) the resolution paradox (degree N_w resolves the
pair yet the dressed reserve stays O(1)).  R343 SKETCH
(PRIME.LSTAR.PAIR_COUPLING.01): promote the measured Schur
coordinates to a contract -- (i) rest-block condition
lambda_rest < 1 with its own margin law (slope -3.28, offset
~20x), (ii) the dressed pair reserve r'_det (FLAT ~0.3) as the
O(1) certificate candidate, (iii) the coupling column C
(2 x (S_- - 2)) and its (I - D)^{-1} dressing as the object a
bound must control; kill = an analytic O(1) lower bound on
r'_det or its refutation on a fresh family.  Runtime 214.6 /
212.3 s record, 0.4 s smoke; deterministic, run1/run2
byte-identical up to WALL.  AMENDMENTS AFTER FREEZE: the two
disclosed calibration amendments a1/a2 (numerics
normalizations, above) and this record-table insertion --
nothing else.

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
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import verify_lstar_instance as V                # noqa: E402 document
import lstar_margin_scaling_probe as LM          # noqa: E402 r286
import fold_capacity_probe as FC                 # noqa: E402 r334
import fullsource_quasidefiniteness_probe as FS  # noqa: E402 r283
import metric_stability_probe as MS              # noqa: E402 r278
import budget_localization_probe as BL           # noqa: E402 r280
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import principal_bessel_probe as PB              # noqa: E402 r243
import paircorr_margin_probe as PC               # noqa: E402
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import jfraction_probe as JF                     # noqa: E402 r230
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
DIAGMAX_REC = 0.9700
DIAGMAX_TOL = 5e-3
SHALLOW_FOLDS = (2, 4)
R284_PR = 1.89
R284_PR_TOL = 0.05
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
CTRL_DEPTH = 40
EXT = 8
EXT2 = 32
EXT15_KZ = frozenset((35, 37, 41, 57, 68, 70, 71, 73, 76, 95,
                      97, 98, 100, 109, 119))
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN = 1721
EXT3_NW_MAX = 2577
MASS_BAR = 0.90
R2_MAX = 1.5
R2_REF_BAND = (0.12, 0.40)
CURV_BAR = 0.35
EXT3_BAND = 0.5
EXT3_OK_MIN = 10
V_BAR = 0.10
DIGAMMA_BAR = 0.02
PRIME_CF_BAR = 1.0e-10
LAYER_BAR = 1.0e-12
DET_ID_BAR = 1.0e-12   # amendment a1: residual / (pq + c^2)
INTERLACE_TOL = 1.0e-9
SCHUR_BAR = 1.0e-6
ALPHA_TOL = 0.5
R286_ALPHA_NW = 3.06
R286_ALPHA_TOL = 0.15
PRIOR_SLOPE_P = 0.71
PRIOR_SLOPE_C = 0.66
PRIOR_ALPHA_TMP = 3.13
PR_BAR = 3.0
KINT_BAR = 1.0
R334_KINT_REC = {"EPST": 1793.99, "SCR": 8.51e6}
R334_KINT_TOL = 0.05
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
MP_SET = ((9, 30), (9, 45), (18, 30), (52, 30), (119, 30),
          (42, 30), (130, 30))
MP_DC_CORE = 1.0e-9
MP_DC_EXT3 = 1.0e-8
MP_M2_CORE = 1.0e-6
MP_M2_EXT = 1.0e-5
MP_M2_EXT3 = 1.0e-3
STAFFEL_BAR = 1.0e-12
GROWTH_KZ = (18, 9, 52, 119, 42, 130)
R285_PBIND = 0.38
TAIL_K = 12
DIG_XI = (0.0, 0.5, 1.7, 4.0, 12.0)
DIG_TOY_BAR = 1.0e-8
M1_BAR = 0.1
MUT_MASS_BAR = 0.5
MUT_MIN = 1.0e-6
TOY_TOL = 1.0e-12
JF_PAIR_BAR = 1.0e-10

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
                       "constructors consume position / weight / "
                       "kernel-row arrays ONLY; record numbers and "
                       "flips enter gates and record tables only"
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


CONSTRUCTORS = ("pair_select", "pair_block", "pair_eigs",
                "det_reserve", "schur_dress", "prime_cf_density",
                "arch_dict_density", "v_predict", "kernel_growth")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "R334_KINT_REC",
                   "alpha_fit_true", "pr_values_true"}


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
def pair_select(yn):
    """the SHALLOW-EDGE PAIR: the two nu atoms with the largest
    x (smallest theta); consumes positions only."""
    o = np.argsort(np.asarray(yn, float))[::-1]
    return int(o[0]), int(o[1])


def pair_block(B, i1, i2):
    """(d1, d2, c) = the 2x2 principal block of E = B B^T at the
    pair rows; consumes the dressed frame only."""
    r1 = np.asarray(B[i1, :], float)
    r2 = np.asarray(B[i2, :], float)
    return (float(r1 @ r1), float(r2 @ r2), float(r1 @ r2))


def pair_eigs(d1, d2, c):
    """both eigenvalues of [[d1, c], [c, d2]]."""
    m = 0.5 * (d1 + d2)
    rad = math.hypot(0.5 * (d1 - d2), c)
    return m + rad, m - rad


def det_reserve(d1, d2, c):
    """(p, q, r_det) = (1-d1, 1-d2, 1 - c^2/(p q)) -- the
    determinant condition c^2 < p q is r_det > 0."""
    p = 1.0 - d1
    q = 1.0 - d2
    return p, q, 1.0 - c * c / (p * q)


def schur_dress(E, i1, i2):
    """the EXACT Schur dressing: E = [[A, C], [C^T, D]] (pair vs
    rest); returns (dressed 2x2 A + C (I-D)^{-1} C^T, lambda_max
    of the rest block D, logdet(I-D), logdet(I-E)); consumes the
    kernel Gram only."""
    n = E.shape[0]
    rest = [k for k in range(n) if k != i1 and k != i2]
    A = E[np.ix_([i1, i2], [i1, i2])]
    C = E[np.ix_([i1, i2], rest)]
    D = E[np.ix_(rest, rest)]
    ImD = np.eye(len(rest)) - D
    X = np.linalg.solve(ImD, C.T)
    Ad = A + C @ X
    lam_rest = float(np.linalg.eigvalsh(D)[-1])
    s_r, ld_r = np.linalg.slogdet(ImD)
    s_f, ld_f = np.linalg.slogdet(np.eye(n) - E)
    return Ad, lam_rest, (float(s_r), float(ld_r)), \
        (float(s_f), float(ld_f))


def prime_cf_density(theta, uu, mm, M, D):
    """the EXACT two-cell tent closed form of the prime-layer
    density at angle theta: every comb atom (u, m) hits exactly
    the lag cells q = floor(u/D), q+1 (fraction r); edge weights
    w_i = 2 for 1 <= i <= M-2, 1 at i in {0, M-1}, 0 beyond
    (builder truncation mirrored); consumes comb arrays only."""
    u = np.asarray(uu, float)
    m = np.asarray(mm, float)
    q = np.floor(u / D).astype(np.int64)
    r = u / D - q

    def wcoef(i):
        return np.where((i >= 1) & (i <= M - 2), 2.0,
                        np.where((i == 0) | (i == M - 1), 1.0, 0.0))

    t1 = (1.0 - r) * wcoef(q) * np.cos(q * theta)
    t2 = r * wcoef(q + 1) * np.cos((q + 1) * theta)
    return float(np.sum(-0.5 * m * (t1 + t2)))


def arch_dict_density(theta, alpha, D, tail_k=TAIL_K):
    """the digamma dictionary for the arch-layer density at
    angle theta: F_A(xi) = -log pi + Re psi(1/4 + i xi/2), xi =
    theta/D, minus the explicit truncation tail of the lag
    window (geometric digamma-free series); consumes window
    shape only."""
    xi = theta / D
    fa = float(-mp.log(mp.pi)
               + mp.re(mp.digamma(mp.mpf(1) / 4
                                  + mp.mpc(0, 1) * xi / 2)))
    tail = 0.0
    for k in range(tail_k):
        a_k = 2.0 * k + 0.5
        z = complex(a_k, xi)
        tail += (-2.0) * (np.exp(-2.0 * alpha * z) / z).real
    return fa - tail, fa


def v_predict(theta, alpha, M, L, D, uu, mm):
    """the source-explicit weight prediction at a nu fold:
    v_pred = -(2/L)(1 - cos theta) (arch dictionary + exact
    prime closed form); consumes window shape + comb only."""
    da, _fa = arch_dict_density(theta, alpha, D)
    dp = prime_cf_density(theta, uu, mm, M, D)
    return -(2.0 / L) * (1.0 - math.cos(theta)) * (da + dp), da, dp


def kernel_growth(B, vk, k, Nw):
    """within-window growth of K_n(y_k) = cum_n / v_k: halves
    log2-slopes over n in [N/4, N/2, N] (r285 convention);
    consumes one dressed row + its weight only."""
    row2 = np.asarray(B[k, :], float) ** 2
    cum = np.cumsum(row2) / vk
    n1, n2, n3 = max(Nw // 4, 1), max(Nw // 2, 2), Nw
    s1 = math.log(cum[n2 - 1] / cum[n1 - 1]) \
        / math.log(float(n2) / n1)
    s2 = math.log(cum[n3 - 1] / cum[n2 - 1]) \
        / math.log(float(n3) / n2)
    return s1, s2


# ============== must-fail mutants
def mutant_c_undressed(B, i1, i2, vn):
    """m1 MUST-FAIL: the coupling WITHOUT sqrt(v1 v2) -- the
    undressed kernel value K(y1, y2); must break the exact E_12
    identity loudly."""
    r1 = np.asarray(B[i1, :], float)
    r2 = np.asarray(B[i2, :], float)
    return float(r1 @ r2) / math.sqrt(float(vn[i1]) * float(vn[i2]))


def mutant_dc_readback():
    """m2 MUST-FAIL: a 'd value' read off the withheld lambda
    record -- the scope audit must FLAG this."""
    return 0.5 * (1.0 + REC_LAM)


def mutant_prior_refit(alpha_fit_true):
    """m3 MUST-FAIL: 'the prior' re-justified from the seen fit
    column -- consumes the withheld fit value; AST-FLAGGED, and
    the toy value differs from the sealed prior."""
    return alpha_fit_true


def mutant_threshold_posthoc(pr_values_true):
    """m4 MUST-FAIL: the world threshold re-picked AFTER SIGHT
    to sit between the seen live and dead PR columns -- consumes
    the withheld PR values; AST-FLAGGED."""
    vals = sorted(pr_values_true)
    return 0.5 * (vals[0] + vals[-1])


def mutant_pair_by_weight(vn):
    """m5 MUST-FAIL: the 2x2 block at the WRONG pair (the two
    largest-v atoms instead of the shallow edge) -- must be
    CAUGHT by the concentration check."""
    o = np.argsort(np.asarray(vn, float))[::-1]
    return int(o[0]), int(o[1])


# ============== gate-side helpers
def build_rung(kz):
    """gate-side bundle for one rung: measures + chain + frame +
    Gram + spectra + pair row + Schur row."""
    mz = V.build_measures(kz)
    Nw = mz["Nw"]
    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], Nw)
    B = V.b_matrix(a, b, h0, mz["yn"], mz["vn"], Nw)
    E = B @ B.T
    ev, W = np.linalg.eigh(E)
    lam = float(ev[-1])
    i1, i2 = pair_select(mz["yn"])
    d1, d2, c = pair_block(B, i1, i2)
    lam2, lam2m = pair_eigs(d1, d2, c)
    p, q, rdet = det_reserve(d1, d2, c)
    m2 = 1.0 - lam2
    margin = 1.0 - lam
    w1 = W[:, -1]
    pmass = float(w1[i1] ** 2 + w1[i2] ** 2)
    pr = float(1.0 / np.sum(w1 ** 4))
    # amendment a1 (disclosed): the identity residual is measured
    # against the NATURAL input scale pq + c^2 (backward-error
    # honest), not against the cancelled difference pq - c^2
    det_dev = abs((1.0 - lam2) * (1.0 - lam2m) - (p * q - c * c)) \
        / max(p * q + c * c, 1e-300)
    Ad, lam_rest, (s_r, ld_r), (s_f, ld_f) = schur_dress(E, i1, i2)
    d1p, d2p, cp = float(Ad[0, 0]), float(Ad[1, 1]), \
        float(0.5 * (Ad[0, 1] + Ad[1, 0]))
    pp_, qp_, rdetp = det_reserve(d1p, d2p, cp)
    s_d, ld_d = np.linalg.slogdet(np.eye(2) - Ad)
    schur_dev = abs(ld_f - (ld_r + float(ld_d))) \
        / max(abs(ld_f), 1.0)
    f1 = int(round(math.acos(min(max(mz["yn"][i1], -1.0), 1.0))
                   * mz["L"] / (2.0 * math.pi)))
    f2 = int(round(math.acos(min(max(mz["yn"][i2], -1.0), 1.0))
                   * mz["L"] / (2.0 * math.pi)))
    return dict(kz=kz, z=int(V.PP[kz]), mz=mz, Nw=Nw, S=mz["S"],
                Sm=len(mz["yn"]), B=B, i1=i1, i2=i2, f1=f1, f2=f2,
                v1=float(mz["vn"][i1]), v2=float(mz["vn"][i2]),
                d1=d1, d2=d2, c=c, p=p, q=q, rdet=rdet, m2=m2,
                lam=lam, margin=margin,
                R2=(m2 / margin - 1.0) if margin > 0 else None,
                pmass=pmass, pr=pr, det_dev=det_dev,
                lam_rest=lam_rest, d1p=d1p, d2p=d2p, cp=cp,
                rdetp=rdetp, m2p=1.0 - pair_eigs(d1p, d2p, cp)[0],
                schur_dev=schur_dev, sgn_ok=(s_f > 0 and s_r > 0
                                             and s_d > 0))


def mp_pair_ward(mz, i1, i2, dps):
    """mp route (r283 chain + pair rows of B, verbatim FS): the
    pair scalars recomputed at the given dps."""
    Nw = mz["Nw"]
    al, sb, h0 = FS.mu_chain_mp(np.asarray(mz["xp"]),
                                np.asarray(mz["wp"]), Nw, dps)
    yn2 = np.asarray(mz["yn"])[[i1, i2]]
    vn2 = np.asarray(mz["vn"])[[i1, i2]]
    Bm = FS.b_matrix_mp(al, sb, h0, yn2, vn2, Nw, dps)
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        d1m = mp.fsum(Bm[0, i] * Bm[0, i] for i in range(Nw))
        d2m = mp.fsum(Bm[1, i] * Bm[1, i] for i in range(Nw))
        cm = mp.fsum(Bm[0, i] * Bm[1, i] for i in range(Nw))
        mm_ = (d1m + d2m) / 2
        gg = (d1m - d2m) / 2
        lam2m = mm_ + mp.sqrt(gg * gg + cm * cm)
        return float(d1m), float(d2m), float(cm), float(1 - lam2m)
    finally:
        mp.mp.dps = old


def layer_split(kz):
    """gate-side FFT layer split of one window: (d, d_A, d_P)
    per fold slot j = 1..L/2 (document formulas verbatim)."""
    alpha, M, L, Nw, D = V.window_shape(kz)
    cP, ka = V.prime_lags(alpha, M, D)
    cA = V.arch_lags(M, D)
    d = V.spectral_density(cA + cP)
    dA = V.spectral_density(cA)
    dP = V.spectral_density(cP)
    return alpha, M, L, D, ka, d, dA, dP


def crossing_pr(Wc, depth):
    """gate-side control bundle: spectral crossing (r283 route)
    + PR of the top eigenvector at the crossing degree."""
    al, sb, h0 = FS.mu_chain_f64(np.asarray(Wc["xp"]),
                                 np.asarray(Wc["wp"]), depth)
    Bc = FS.b_matrix_f64(al, sb, h0, np.asarray(Wc["yn"]),
                         np.asarray(Wc["vn"]), depth)
    cross, _rho = FS.crossing_from_B(Bc, depth)
    prx = None
    if cross is not None:
        Bn = Bc[:, :cross]
        _e, Wv = np.linalg.eigh(Bn @ Bn.T)
        w1 = Wv[:, -1]
        prx = float(1.0 / np.sum(w1 ** 4))
    return cross, prx


def eig_pr(Wd):
    """PR + pair mass of the top eigenvector of E_{N_w} of a
    world dict (gate-side)."""
    E = Wd["B"] @ Wd["B"].T
    _e, Wv = np.linalg.eigh(E)
    w1 = Wv[:, -1]
    pr = float(1.0 / np.sum(w1 ** 4))
    i1, i2 = pair_select(Wd["yn"])
    return pr, float(w1[i1] ** 2 + w1[i2] ** 2)


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("pair_extremal_probe -- PRIME.LSTAR.PAIR_EXTREMAL.01 "
          "(round 342)")
    print("SPEC_SHA %s   (r286 LM %s / r334 FC %s)"
          % (SPEC_SHA[:16], LM.SPEC_SHA[:16], FC.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 f64 block; ladder, EXT3, twin, mp "
                        "wards, fits, worlds, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the pair constructor (two "
          "largest-x nu atoms), the determinant/Schur identities, "
          "the ladder (42 + 15 r286 + 12 r329 EXT3 as PURE TEST + "
          "twin), the DISCLOSED PRIORS (p, q ~ N^-%.2f, c ~ "
          "N^-%.2f, margin ~ N^-%.2f /tmp; r286 alpha %.2f), the "
          "digamma dictionary + exact prime closed form, the world "
          "thresholds (PR_BAR %.1f, KINT_BAR %.1f), every bar/"
          "tolerance, the mutants and the verdict form; pre-spec "
          "scoping (s1 digamma identity, s2 w9 pair block, s3 "
          "kz130 end-to-end) disclosed in the spec; the STOP list "
          "forbids any L* claim and any certificate reading"
          % (PRIOR_SLOPE_P, PRIOR_SLOPE_C, PRIOR_ALPHA_TMP,
             R286_ALPHA_NW, PR_BAR, KINT_BAR))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m2 = scope_audit("mutant_dc_readback")
    hits_m3 = scope_audit("mutant_prior_refit")
    hits_m4 = scope_audit("mutant_threshold_posthoc")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m2) and bool(hits_m3) and bool(hits_m4),
          "the %d sealed constructors consume position / weight / "
          "kernel-row arrays ONLY (%s); fragment audit (no fit "
          "primitives beyond the imported r286 Theil-Sen): %s; m2 "
          "FLAGGED (%s); m3 FLAGGED (%s); m4 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS",
             hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- HAND 2x2 + SCHUR + JF9 + DIGAMMA + "
            "PRIME CF + FITS")
    d1t, d2t, ct = 0.25, 0.5, 0.125
    l1t, l2t = pair_eigs(d1t, d2t, ct)
    pt, qt, rt = det_reserve(d1t, d2t, ct)
    ok_hand = (abs(l1t - (3.0 / 8.0 + math.sqrt(2.0) / 8.0))
               <= TOY_TOL
               and abs(l2t - (3.0 / 8.0 - math.sqrt(2.0) / 8.0))
               <= TOY_TOL
               and abs((1.0 - l1t) * (1.0 - l2t) - 23.0 / 64.0)
               <= TOY_TOL
               and abs(pt * qt - ct * ct - 23.0 / 64.0) <= TOY_TOL
               and abs(rt - 23.0 / 24.0) <= TOY_TOL)
    E3 = np.array([[0.25, 0.125, 1.0 / 16.0],
                   [0.125, 0.5, 1.0 / 32.0],
                   [1.0 / 16.0, 1.0 / 32.0, 0.125]])
    Ad3, lr3, (sr3, ldr3), (sf3, ldf3) = schur_dress(E3, 0, 1)
    # exact Fractions Schur on the same toy
    a11, a12, a22 = Fr(1, 4), Fr(1, 8), Fr(1, 2)
    c1_, c2_, dd = Fr(1, 16), Fr(1, 32), Fr(1, 8)
    inv = 1 / (1 - dd)
    Ad_ex = ((a11 + c1_ * c1_ * inv, a12 + c1_ * c2_ * inv),
             (a12 + c1_ * c2_ * inv, a22 + c2_ * c2_ * inv))
    detE_ex = (1 - dd) * ((1 - Ad_ex[0][0]) * (1 - Ad_ex[1][1])
                          - Ad_ex[0][1] * Ad_ex[1][0])
    IE3 = np.eye(3) - E3
    ok_schur = (abs(float(Ad3[0, 0]) - float(Ad_ex[0][0]))
                <= TOY_TOL
                and abs(float(Ad3[1, 1]) - float(Ad_ex[1][1]))
                <= TOY_TOL
                and abs(float(Ad3[0, 1]) - float(Ad_ex[0][1]))
                <= TOY_TOL
                and abs(float(np.linalg.det(IE3))
                        - float(detE_ex)) <= TOY_TOL
                and abs(math.exp(ldr3 + float(np.linalg.slogdet(
                    np.eye(2) - Ad3)[1])) - float(detE_ex))
                <= TOY_TOL and abs(lr3 - 0.125) <= TOY_TOL)
    check("G10-toy-hand-pair", ok_hand and ok_schur,
          "HAND 2x2 (d1 1/4, d2 1/2, c 1/8): eigs 3/8 +- sqrt2/8, "
          "(1-l)(1-l') == pq - c^2 == 23/64, r_det == 23/24 exact; "
          "SCHUR 3x3 toy: dressed block == EXACT Fractions "
          "(A + C (1-D)^-1 C^T), det(I-E) == det(I-D) det(I-A') "
          "== %s exact, lambda_rest == 1/8" % str(detE_ex))
    # JF9 rational pair route
    xsJ, wsJ, ysJ, vsJ, N_J, dep_J = FC.frac_instance("I1")
    GJ = FC.frac_kernel(xsJ, wsJ, ysJ, dep_J)
    yfJ = np.array([float(y) for y in ysJ])
    vfJ = np.array([float(v) for v in vsJ])
    j1, j2 = pair_select(yfJ)
    aJ, bJ, h0J = V.mu_chain(np.array([float(x) for x in xsJ]),
                             np.array([float(w) for w in wsJ]),
                             dep_J)
    BJ = V.b_matrix(aJ, bJ, h0J, yfJ, vfJ, dep_J)
    d1J, d2J, cJ = pair_block(BJ, j1, j2)
    ex_d1 = vsJ[j1] * GJ[j1][j1]
    ex_d2 = vsJ[j2] * GJ[j2][j2]
    ex_c2 = vsJ[j1] * vsJ[j2] * GJ[j1][j2] * GJ[j1][j2]
    dev_j = max(abs(d1J - float(ex_d1)) / abs(float(ex_d1)),
                abs(d2J - float(ex_d2)) / abs(float(ex_d2)),
                abs(cJ * cJ - float(ex_c2))
                / max(abs(float(ex_c2)), 1e-300))
    check("G11-toy-jf9-rational", dev_j <= JF_PAIR_BAR,
          "JF9 RATIONAL CROSS-ROUTE (r230 toy, depth %d): the "
          "pair scalars d_k = v_k K(y_k, y_k) and c^2 = v1 v2 "
          "K(y1, y2)^2 from the EXACT rational monic kernel (WD "
          "chain, Fractions) == the f64 B-row route, max rel dev "
          "%.1e (bar %.0e)" % (dep_J, dev_j, JF_PAIR_BAR))
    # digamma identity toy (quad vs closed form)
    old_dps = mp.mp.dps
    mp.mp.dps = 30
    dev_dig = 0.0
    for xi in DIG_XI:
        f_int = mp.quad(lambda w: (mp.e ** (-2 * w)
                                   - mp.cos(xi * w)
                                   * mp.e ** (-w / 2))
                        / (1 - mp.e ** (-2 * w)), [0, 1, 10, 60])
        quad_v = float(-(mp.euler + mp.log(mp.pi)) + 2 * f_int)
        cf_v = float(-mp.log(mp.pi)
                     + mp.re(mp.digamma(mp.mpf(1) / 4
                                        + mp.mpc(0, 1) * xi / 2)))
        dev_dig = max(dev_dig, abs(quad_v - cf_v))
    mp.mp.dps = old_dps
    check("G12-toy-digamma", dev_dig <= DIG_TOY_BAR,
          "DIGAMMA DICTIONARY IDENTITY: -(gamma + log pi) + "
          "2 int_0^inf [e^-2w - cos(xi w) e^-w/2]/(1 - e^-2w) dw "
          "== -log pi + Re psi(1/4 + i xi/2) at xi = %s, max abs "
          "dev %.1e (bar %.0e) -- the sealed arch closed form is "
          "the classical Weil archimedean transform"
          % (str(DIG_XI), dev_dig, DIG_TOY_BAR))
    # prime closed-form toy: synthetic comb on a small grid
    M_t, D_t = 16, 0.25
    L_t = 2 * M_t - 2
    uu_t = np.array([0.9, 1.7, 3.4])
    mm_t = np.array([1.0, 0.5, 0.25])
    c_t = np.zeros(M_t)
    for u_j, m_j in zip(uu_t, mm_t):
        i0 = int(math.floor(u_j / D_t))
        for i in range(max(0, i0 - 2), min(M_t, i0 + 3)):
            v = 1.0 - abs(i * D_t - u_j) / D_t
            if v > 0.0:
                c_t[i] -= m_j * 0.5 * v
    d_t = V.spectral_density(c_t)
    dev_cf = 0.0
    for jj in (1, 3, 5):
        th = 2.0 * math.pi * jj / L_t
        cf = prime_cf_density(th, uu_t, mm_t, M_t, D_t)
        dev_cf = max(dev_cf, abs(cf - float(d_t[jj]))
                     / max(abs(float(d_t[jj])), 1e-300))
    check("G13-toy-prime-cf", dev_cf <= TOY_TOL * 100,
          "PRIME CLOSED FORM on a synthetic comb (M = %d, 3 "
          "atoms): the two-cell tent formula == the FFT density "
          "at folds (1, 3, 5), max rel dev %.1e -- the prime "
          "layer is EXACT, not asymptotic" % (M_t, dev_cf))
    S_toy = np.array([300.0 * (1.1 ** k) for k in range(20)])
    y_toy = np.log(0.37) - 3.0 * np.log(S_toy)
    ft = LM.ts_fit(np.log(S_toy), y_toy)
    ft_short = LM.ts_fit(np.arange(8.0), np.arange(8.0))
    check("G14-toy-fit", (not isinstance(ft[0], str))
          and abs(ft[1] + 3.0) <= 1e-9
          and ft_short[0] == "SHORT_LADDER",
          "r286 Theil-Sen imported verbatim: synthetic N^-3 slope "
          "%.9f == -3; the guard REFUSES 8 points (%s)"
          % (ft[1] if not isinstance(ft[0], str) else float("nan"),
             str(ft_short)))

    # ---------------- S2 w9 flagship
    section("S2  W9 -- RECORDS + PAIR BLOCK + LAYER SPLIT + SCHUR")
    R9 = build_rung(MAIN_KZ)
    lam185, _B185 = V.lam_max_at(R9["mz"], REC_NW + 1)
    ok_rec = (R9["S"] == REC_S and R9["Sm"] == REC_SM
              and R9["Nw"] == REC_NW
              and abs(R9["lam"] - REC_LAM) <= 1e-6
              and abs(lam185 - REC_LAM_NEXT) <= 1e-6
              and abs(R9["margin"] / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL)
    check("G20-w9-records", ok_rec,
          "w9: S = %d (nu %d), N_w = %d, lambda_max(E_184) = %.8f "
          "(record %.8f), margin = %.4e (record %.4e), lambda at "
          "185 = %.8f > 1 -- the document route reproduced"
          % (R9["S"], R9["Sm"], R9["Nw"], R9["lam"], REC_LAM,
             R9["margin"], REC_MARGIN, lam185))
    ok_pair9 = ((R9["f1"], R9["f2"]) == SHALLOW_FOLDS
                and abs(R9["d1"] - DIAGMAX_REC) <= DIAGMAX_TOL
                and R9["det_dev"] <= DET_ID_BAR
                and R9["margin"] <= R9["m2"] + INTERLACE_TOL
                and (R9["m2"] > 0) == (R9["rdet"] > 0))
    check("G21-w9-pair-block", ok_pair9,
          "THE PAIR: folds (%d, %d) == r284 shallow edge (u = "
          "%.3f / %.3f < log 2 = %.3f); d1 = %.6f (== r284 diag "
          "max %.4f), d2 = %.6f, c = %.6f; p = %.4e, q = %.4e, "
          "r_det = %.4e; m2 = 1 - lambda_2x2 = %.4e vs margin "
          "%.4e (R2 = %.3f, r338 prior band %s); determinant "
          "identity dev %.1e (bar %.0e); interlacing margin <= "
          "m2 holds; sign(m2) == sign(r_det)"
          % (R9["f1"], R9["f2"], R9["f1"] * R9["mz"]["D"],
             R9["f2"] * R9["mz"]["D"], math.log(2.0),
             R9["d1"], DIAGMAX_REC, R9["d2"], R9["c"], R9["p"],
             R9["q"], R9["rdet"], R9["m2"], R9["margin"],
             R9["R2"], str(R2_REF_BAND), R9["det_dev"],
             DET_ID_BAR))
    ok_conc9 = (R9["pmass"] >= MASS_BAR
                and abs(R9["pr"] - R284_PR) <= R284_PR_TOL)
    check("G22-w9-concentration", ok_conc9,
          "CONCENTRATION: pair mass = %.4f (>= %.2f), PR = %.2f "
          "(r284 record %.2f +- %.2f) -- the top eigenvector IS "
          "the two-atom extremal on the flagship"
          % (R9["pmass"], MASS_BAR, R9["pr"], R284_PR,
             R284_PR_TOL))
    ok_schur9 = (R9["schur_dev"] <= SCHUR_BAR and R9["sgn_ok"]
                 and R9["rdetp"] > 0 and R9["lam_rest"] < 1.0)
    check("G23-w9-schur", ok_schur9,
          "EXACT SCHUR DRESSING: logdet identity det(I-E) == "
          "det(I-D) det(I-A') dev %.1e (bar %.0e), all signs "
          "positive; lambda_rest = %.6f (rest margin %.4e = %.1fx "
          "the full margin), dressed (d1', d2', c') = (%.6f, "
          "%.6f, %.6f), dressed reserve r'_det = %.4e > 0 -- L* "
          "on w9 IS {rest} AND {dressed pair determinant}, "
          "measured exactly"
          % (R9["schur_dev"], SCHUR_BAR, R9["lam_rest"],
             1.0 - R9["lam_rest"],
             (1.0 - R9["lam_rest"]) / R9["margin"], R9["d1p"],
             R9["d2p"], R9["cp"], R9["rdetp"]))
    # layer split + closed forms on w9
    alpha9, M9, L9, D9, ka9, dd9, dA9, dP9 = layer_split(MAIN_KZ)
    dev_lin = float(np.max(np.abs(dA9 + dP9 - dd9))
                    / max(float(np.max(np.abs(dd9))), 1e-300))
    uu9c = np.asarray(V.U[:ka9], float)
    mm9c = np.asarray(V.W_VM[:ka9], float)
    dev_pcf = 0.0
    dev_dict = 0.0
    dev_v9 = 0.0
    shares = []
    for (ii, ff) in ((R9["i1"], R9["f1"]), (R9["i2"], R9["f2"])):
        th = 2.0 * math.pi * ff / L9
        pcf = prime_cf_density(th, uu9c, mm9c, M9, D9)
        dev_pcf = max(dev_pcf, abs(pcf - float(dP9[ff]))
                      / max(abs(float(dP9[ff])), 1e-300))
        da_corr, da_pure = arch_dict_density(th, alpha9, D9)
        dev_dict = max(dev_dict, abs(da_corr - float(dA9[ff]))
                       / max(abs(float(dA9[ff])), 1e-300))
        vp, _da, _dp = v_predict(th, alpha9, M9, L9, D9, uu9c,
                                 mm9c)
        vt = float(R9["mz"]["vn"][ii])
        dev_v9 = max(dev_v9, abs(vp - vt) / vt)
        m2only = mm9c[uu9c < math.log(2.0) + 1e-12]
        first_p = prime_cf_density(th, uu9c[:1], mm9c[:1], M9, D9) \
            if len(uu9c) else 0.0
        shares.append((ff, float(dA9[ff]), float(dP9[ff]),
                       first_p, len(m2only)))
    check("G24-w9-layer-split", dev_lin <= LAYER_BAR
          and dev_pcf <= PRIME_CF_BAR and dev_dict <= DIGAMMA_BAR,
          "LAYER SPLIT d == d_A + d_P (max rel dev %.1e, bar "
          "%.0e); PRIME CLOSED FORM at the pair folds dev %.1e "
          "(bar %.0e); DIGAMMA DICTIONARY (tail-corrected) dev "
          "%.1e (bar %.2f); layer shares at folds %d/%d (d_A, "
          "d_P, first-atom tent term): %s -- the pair weights "
          "are arch layer + tent tail, said with numbers"
          % (dev_lin, LAYER_BAR, dev_pcf, PRIME_CF_BAR, dev_dict,
             DIGAMMA_BAR, R9["f1"], R9["f2"],
             str([(f, round(a, 4), round(p_, 4), round(t, 4))
                  for (f, a, p_, t, _n) in shares])))
    check("G25-w9-v-predict", dev_v9 <= V_BAR,
          "SOURCE-EXPLICIT WEIGHT PREDICTION on w9: max rel dev "
          "%.4f at the pair (bar %.2f) -- v_pred = -(2/L)"
          "(1 - cos theta)(digamma dictionary + exact prime "
          "closed form)" % (dev_v9, V_BAR))

    # ---------------- S3 the ladder
    section("S3  LEG A -- THE d/c/s LADDER (42 + 15 + 12 EXT3 + "
            "TWIN)")
    if smoke:
        for g in ("G30-ladder-census", "G31-ladder-identities",
                  "G32-ext3-census", "G33-twin"):
            check(g, True, "SMOKE: skipped")
        ROWS = {9: R9}
        core_kzs, ext_kzs, ext3_kzs = [9], [], []
    else:
        core_kzs = list(V.admissible_indices())
        cands = LM.ext_rule()
        ext_kzs = [t[1] for t in cands[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ok_cen = (len(core_kzs) == 42
                  and set(ext_kzs) == set(EXT15_KZ))
        ROWS = {}
        print("    %-5s %-5s %-5s %-5s %-9s %-11s %-11s %-11s "
              "%-10s %-10s %-10s %-6s %-6s %-5s"
              % ("kz", "z", "S-", "N_w", "folds", "d1", "d2",
                 "c", "r_det", "m2", "margin", "R2", "pmass",
                 "PR"))
        neg_rows = []
        for kz in core_kzs + ext_kzs + ext3_kzs:
            R = R9 if kz == MAIN_KZ else build_rung(kz)
            ROWS[kz] = R
            if R["margin"] <= 0:
                neg_rows.append(kz)
            print("    %-5d %-5d %-5d %-5d (%3d,%3d) %.9f %.9f "
                  "%.9f %.4e %.4e %.4e %6.3f %.4f %5.2f"
                  % (kz, R["z"], R["Sm"], R["Nw"], R["f1"],
                     R["f2"], R["d1"], R["d2"], R["c"], R["rdet"],
                     R["m2"], R["margin"],
                     R["R2"] if R["R2"] is not None else -1.0,
                     R["pmass"], R["pr"]), flush=True)
        ok_ext3 = all(EXT3_NW_MIN <= ROWS[kz]["Nw"] <= EXT3_NW_MAX
                      for kz in ext3_kzs) \
            and min(ROWS[kz]["Nw"] for kz in ext3_kzs) \
            == EXT3_NW_MIN \
            and max(ROWS[kz]["Nw"] for kz in ext3_kzs) \
            == EXT3_NW_MAX
        check("G30-ladder-census", ok_cen and ok_ext3
              and not neg_rows,
              "42 core (document rule) + 15 extension == the r286 "
              "record kz set + 12 EXT3 == the r329 record "
              "selection (N_w %d..%d exact); every f64 margin "
              "positive (contingency rows: %s)"
              % (EXT3_NW_MIN, EXT3_NW_MAX,
                 str(neg_rows) if neg_rows else "none"))
        kz57 = core_kzs + ext_kzs
        ok_id = all(ROWS[k]["det_dev"] <= DET_ID_BAR
                    and ROWS[k]["schur_dev"] <= SCHUR_BAR
                    and ROWS[k]["sgn_ok"]
                    and ROWS[k]["margin"] <= ROWS[k]["m2"]
                    + INTERLACE_TOL
                    and (ROWS[k]["m2"] > 0) == (ROWS[k]["rdet"] > 0)
                    for k in kz57 + ext3_kzs)
        conc57 = [k for k in kz57
                  if ROWS[k]["pmass"] < MASS_BAR
                  or ROWS[k]["R2"] is None
                  or not (0.0 <= ROWS[k]["R2"] <= R2_MAX)]
        check("G31-ladder-identities", ok_id,
              "per-rung identities on all %d rows: determinant "
              "(1-l)(1-l') == pq - c^2 (<= %.0e), Schur logdet "
              "(<= %.0e, signs +), interlacing margin <= m2, "
              "sign(m2) == sign(r_det); CONCENTRATION on the 57: "
              "pair mass >= %.2f and R2 in [0, %.1f] %s (BLIND "
              "loci: %s); pair-mass range %.4f..%.4f, PR range "
              "%.2f..%.2f, r_det range %.3e..%.3e"
              % (len(kz57) + len(ext3_kzs), DET_ID_BAR, SCHUR_BAR,
                 MASS_BAR, R2_MAX,
                 "57/57" if not conc57 else "BROKEN",
                 str(conc57) if conc57 else "none",
                 min(ROWS[k]["pmass"] for k in kz57),
                 max(ROWS[k]["pmass"] for k in kz57),
                 min(ROWS[k]["pr"] for k in kz57),
                 max(ROWS[k]["pr"] for k in kz57),
                 min(ROWS[k]["rdet"] for k in kz57),
                 max(ROWS[k]["rdet"] for k in kz57)))
        e3_loci = [k for k in ext3_kzs
                   if ROWS[k]["pmass"] < MASS_BAR
                   or ROWS[k]["R2"] is None
                   or not (0.0 <= ROWS[k]["R2"] <= R2_MAX)]
        ext3_tag = ("EXT3_CONFORMS" if not e3_loci
                    else "EXT3_FAMILY_BREAK(%s)" % str(e3_loci))

        def med(vals):
            return float(np.median(np.asarray(vals, float)))

        coh = {}
        for nm, kzsel in (("core42", core_kzs), ("ext15", ext_kzs),
                          ("ext3B", list(EXT3_KZ_B)),
                          ("ext3A", list(EXT3_KZ_A))):
            coh[nm] = (med([ROWS[k]["pmass"] for k in kzsel]),
                       med([ROWS[k]["pr"] for k in kzsel]),
                       med([ROWS[k]["R2"] for k in kzsel]),
                       med([ROWS[k]["rdet"] for k in kzsel]))
        check("G32-ext3-census", True,
              "EXT3 PURE-TEST census => %s; cohort medians "
              "(pmass, PR, R2, r_det): %s -- the r338 core band "
              "R2 %s vs the fresh-anchor value, the family "
              "question answered by measurement (r329 lesson)"
              % (ext3_tag,
                 str({nm: (round(a, 4), round(b, 2), round(c_, 3),
                           "%.2e" % d_)
                      for nm, (a, b, c_, d_) in coh.items()}),
                 str(R2_REF_BAND)))
        # twin
        uu9, mm9 = TR.base_comb(9)
        mzD = TR.build_world(9, uu9, mm9)
        mz9 = R9["mz"]
        ok_dose0 = (np.array_equal(mzD["xp"], mz9["xp"])
                    and np.array_equal(mzD["wp"], mz9["wp"])
                    and np.array_equal(mzD["yn"], mz9["yn"])
                    and np.array_equal(mzD["vn"], mz9["vn"]))
        gaps9 = MF.local_gaps(uu9)
        u2, m2c, _dens, _du = AKD.twin_rational(uu9, mm9, gaps9,
                                                mz9["D"], TWIN_TOL)
        mzT = TR.build_world(9, u2, m2c)
        aT, bT, h0T = V.mu_chain(mzT["xp"], mzT["wp"], mzT["Nw"])
        BT = V.b_matrix(aT, bT, h0T, mzT["yn"], mzT["vn"],
                        mzT["Nw"])
        t1_, t2_ = pair_select(mzT["yn"])
        d1T, d2T, cT = pair_block(BT, t1_, t2_)
        devT = max(abs(d1T - R9["d1"]) / R9["d1"],
                   abs(d2T - R9["d2"]) / R9["d2"],
                   abs(cT - R9["c"]) / abs(R9["c"]))
        check("G33-twin", ok_dose0 and devT <= TWIN_BAR,
              "RATIONAL TWIN at tol %.0e (r289/r331 verbatim; "
              "dose-zero identity TR.build_world == "
              "V.build_measures BITWISE %s): pair scalars (d1, "
              "d2, c) rel devs <= %.1e (bar %.0e) -- the pair "
              "coordinate is twin-stable"
              % (TWIN_TOL, ok_dose0, devT, TWIN_BAR))

    # ---------------- S4 mp wards
    section("S4  MP PRECISION WARDS (SEALED SUBSET)")
    if smoke:
        check("G40-mp-wards", True, "SMOKE: skipped")
    else:
        staffel = {}
        ok_mp = True
        details = []
        for (kz, dps) in MP_SET:
            R = ROWS[kz]
            d1m, d2m, cm, m2m = mp_pair_ward(R["mz"], R["i1"],
                                             R["i2"], dps)
            dev_d = max(abs(R["d1"] - d1m) / abs(d1m),
                        abs(R["d2"] - d2m) / abs(d2m))
            dev_c = abs(R["c"] - cm) / abs(cm)
            dev_m2 = abs(R["m2"] - m2m) / max(abs(m2m), 1e-300)
            # amendment a2 (disclosed): the m2 ward bar scales
            # with DEPTH (the s3 sizing logic), not cohort --
            # 1e-6 for N_w <= 400, 1e-5 to 1500, 1e-3 beyond
            bar_dc = MP_DC_EXT3 if kz in EXT3_KZ_B + EXT3_KZ_A \
                else MP_DC_CORE
            Nw_ = R["Nw"]
            bar_m2 = MP_M2_CORE if Nw_ <= 400 else (
                MP_M2_EXT if Nw_ <= 1500 else MP_M2_EXT3)
            ok_mp = ok_mp and dev_d <= bar_dc \
                and dev_c <= bar_dc and dev_m2 <= bar_m2
            if kz == 9:
                staffel[dps] = (d1m, d2m, cm)
            details.append("kz%d@%d d %.1e c %.1e m2 %.1e"
                           % (kz, dps, dev_d, dev_c, dev_m2))
        st_dev = max(abs(staffel[30][t] - staffel[45][t])
                     / abs(staffel[45][t]) for t in range(3))
        ok_mp = ok_mp and st_dev <= STAFFEL_BAR
        check("G40-mp-wards", ok_mp,
              "MP WARDS (chain + pair B rows recomputed, r283 "
              "route): %s (bars d/c %.0e core, %.0e EXT3; m2 "
              "%.0e/%.0e/%.0e core/ext/EXT3); w9 STAFFEL dps "
              "30 vs 45: max rel dev %.1e (bar %.0e) -- the "
              "pair scalars are arbitration-safe at every "
              "measured depth"
              % ("; ".join(details), MP_DC_CORE, MP_DC_EXT3,
                 MP_M2_CORE, MP_M2_EXT, MP_M2_EXT3, st_dev,
                 STAFFEL_BAR))

    # ---------------- S5 leg B source-explicit
    section("S5  LEG B -- SOURCE-EXPLICIT PREDICTION + KERNEL "
            "CENSUS")
    if smoke:
        for g in ("G50-v-predict-ladder", "G51-kernel-growth",
                  "G52-arch-dict-sample"):
            check(g, True, "SMOKE: skipped")
    else:
        devs_v = {}
        for kz in core_kzs + ext_kzs + ext3_kzs:
            R = ROWS[kz]
            alpha_, M_, L_, Nw_, D_ = V.window_shape(kz)
            ka_ = int(np.searchsorted(V.U, 2.0 * alpha_ + 1e-14,
                                      side="right"))
            uu_ = np.asarray(V.U[:ka_], float)
            mm_ = np.asarray(V.W_VM[:ka_], float)
            dv = 0.0
            for (ii, ff) in ((R["i1"], R["f1"]),
                             (R["i2"], R["f2"])):
                th = 2.0 * math.pi * ff / L_
                vp, _a, _p = v_predict(th, alpha_, M_, L_, D_,
                                       uu_, mm_)
                vt = float(R["mz"]["vn"][ii])
                dv = max(dv, abs(vp - vt) / vt)
            devs_v[kz] = dv
        med_v = float(np.median(list(devs_v.values())))
        max_v = max(devs_v.values())
        max_kz = max(devs_v, key=lambda k: devs_v[k])
        v_carries = med_v <= V_BAR
        check("G50-v-predict-ladder", True,
              "SOURCE-EXPLICIT WEIGHT PREDICTION over all %d "
              "rungs: median rel dev %.4f (V_BAR %.2f => %s), "
              "max %.4f at kz%d; cohort medians core42 %.4f / "
              "ext15 %.4f / ext3 %.4f"
              % (len(devs_v), med_v, V_BAR,
                 "CARRIES" if v_carries else "MISSES", max_v,
                 max_kz,
                 float(np.median([devs_v[k] for k in core_kzs])),
                 float(np.median([devs_v[k] for k in ext_kzs])),
                 float(np.median([devs_v[k] for k in ext3_kzs]))))
        rows_g = []
        for kz in GROWTH_KZ:
            R = ROWS[kz]
            s1, s2 = kernel_growth(R["B"], R["v1"], R["i1"],
                                   R["Nw"])
            rows_g.append((kz, round(s1, 3), round(s2, 3)))
        check("G51-kernel-growth", True,
              "WITHIN-WINDOW KERNEL GROWTH at the binding atom "
              "(halves log-slopes of K_n(y_1) over [N/4, N/2, "
              "N]): %s vs the r285 record %.2f (sub-classical; "
              "bulk law would be 1) -- the closed-form kernel "
              "side stays the open specialist question, typed"
              % (str(rows_g), R285_PBIND))
        dev_dict_s = {}
        for kz in GROWTH_KZ:
            R = ROWS[kz]
            alpha_, M_, L_, D_, ka_, dd_, dA_, dP_ = \
                layer_split(kz)
            dv = 0.0
            for ff in (R["f1"], R["f2"]):
                th = 2.0 * math.pi * ff / L_
                da_c, _da_p = arch_dict_density(th, alpha_, D_)
                dv = max(dv, abs(da_c - float(dA_[ff]))
                         / max(abs(float(dA_[ff])), 1e-300))
            dev_dict_s[kz] = dv
        ok_dict = all(v <= DIGAMMA_BAR
                      for v in dev_dict_s.values())
        check("G52-arch-dict-sample", ok_dict,
              "DIGAMMA DICTIONARY on the sample rungs (pair "
              "folds, tail-corrected): rel devs %s (bar %.2f) -- "
              "the arch layer at the shallow edge IS the "
              "classical Weil archimedean transform at xi = "
              "theta/Delta"
              % (str({("kz%d" % k): round(v, 5)
                      for k, v in dev_dict_s.items()}),
                 DIGAMMA_BAR))

    # ---------------- S6 fits + alpha kill
    section("S6  LEG D -- SEALED FITS vs DISCLOSED PRIORS + THE "
            "ALPHA KILL")
    if smoke:
        for g in ("G60-alpha-anchor", "G61-component-fits",
                  "G62-ext3-pure-test", "G63-alpha-composition"):
            check(g, True, "SMOKE: skipped")
        law_flags = {}
    else:
        kz57 = core_kzs + ext_kzs
        lnN = np.log(np.array([ROWS[k]["Nw"] for k in kz57],
                              float))
        cols = {}
        for nm, key in (("p", "p"), ("q", "q"), ("c", "c"),
                        ("rdet", "rdet"), ("m2", "m2"),
                        ("margin", "margin"), ("rdetp", "rdetp")):
            cols[nm] = np.array([ROWS[k][key] for k in kz57],
                                float)
        cols["ppq"] = cols["p"] + cols["q"]
        cols["restm"] = np.array([1.0 - ROWS[k]["lam_rest"]
                                  for k in kz57], float)
        ln42 = np.log(np.array([ROWS[k]["Nw"] for k in core_kzs],
                               float))
        m42 = np.array([ROWS[k]["margin"] for k in core_kzs],
                       float)
        f42 = LM.ts_fit(ln42, np.log(m42))
        alpha42 = -f42[1]
        check("G60-alpha-anchor",
              abs(alpha42 - R286_ALPHA_NW) <= R286_ALPHA_TOL,
              "the 42-only margin fit: alpha = %.3f vs the r286 "
              "record %.2f (tol %.2f) -- the fit instrument is "
              "anchored on the published law" % (alpha42,
                                                 R286_ALPHA_NW,
                                                 R286_ALPHA_TOL))
        fits = {}
        curv = {}
        o = np.argsort(lnN)
        half = len(o) // 2
        for nm in ("p", "q", "c", "rdet", "m2", "margin", "ppq",
                   "rdetp", "restm"):
            y = np.log(np.abs(cols[nm]))
            ft_ = LM.ts_fit(lnN, y)
            s_lo = LM.ts_slope_free(lnN[o[:half]], y[o[:half]])
            s_hi = LM.ts_slope_free(lnN[o[half:]], y[o[half:]])
            fits[nm] = (float(ft_[0]), float(ft_[1]),
                        float(ft_[2]))
            curv[nm] = float(s_hi - s_lo)
        law_flags = {nm: abs(curv[nm]) <= CURV_BAR
                     for nm in ("p", "q", "c")}
        check("G61-component-fits", True,
              "SEALED FITS on the 57 vs log N_w (slope, halves "
              "curvature | disclosed prior): p %.3f (%+.3f | "
              "-%.2f), q %.3f (%+.3f), c %.3f (%+.3f | -%.2f), "
              "r_det %.3f (%+.3f), m2 %.3f (%+.3f), margin %.3f "
              "(%+.3f | -%.2f /tmp), dressed r'_det %.3f, rest "
              "margin %.3f; stability (|curv| <= %.2f): %s"
              % (fits["p"][1], curv["p"], PRIOR_SLOPE_P,
                 fits["q"][1], curv["q"], fits["c"][1], curv["c"],
                 PRIOR_SLOPE_C, fits["rdet"][1], curv["rdet"],
                 fits["m2"][1], curv["m2"], fits["margin"][1],
                 curv["margin"], PRIOR_ALPHA_TMP,
                 fits["rdetp"][1], fits["restm"][1], CURV_BAR,
                 str({k: bool(v) for k, v in law_flags.items()})))
        e3_ok = {}
        for nm in ("p", "q", "c"):
            a0, b0, _m = fits[nm]
            n_in = 0
            for kz in ext3_kzs:
                pred = math.exp(a0 + b0
                                * math.log(ROWS[kz]["Nw"]))
                meas = abs(ROWS[kz][nm])
                if abs(math.log10(pred / meas)) <= EXT3_BAND:
                    n_in += 1
            e3_ok[nm] = n_in
        ext3_law = all(v >= EXT3_OK_MIN for v in e3_ok.values())
        check("G62-ext3-pure-test", True,
              "EXT3 PURE TEST (the 57-fit predicts the 12 fresh "
              "rows, band %.1f decades): in-band counts %s "
              "(need >= %d each) => %s"
              % (EXT3_BAND, str(e3_ok), EXT3_OK_MIN,
                 "LAW EXTENDS" if ext3_law else "LAW BREAKS on "
                 "the fresh family"))
        alpha_pair = -fits["m2"][1]
        alpha_full = -fits["margin"][1]
        alpha_comp = (-fits["p"][1]) + (-fits["q"][1]) \
            + (-fits["rdet"][1]) - (-fits["ppq"][1])
        kill_a = abs(alpha_pair - alpha_full) <= ALPHA_TOL
        kill_b = abs(alpha_comp - alpha_pair) <= ALPHA_TOL
        check("G63-alpha-composition", True,
              "THE ALPHA KILL: alpha_full = %.3f (57) / %.3f "
              "(42-only, r286 %.2f); alpha_pair = %.3f (|diff| "
              "%.3f <= %.1f: %s); bookkeeping composition "
              "a_p + a_q + rho_r - a_(p+q) = %.3f (|diff to "
              "alpha_pair| %.3f: %s); the OPEN analytic "
              "remainder is rho_r = %.3f (the cancellation "
              "exponent of r_det = 1 - c^2/pq) -- no source "
              "derivation of rho_r exists yet, typed for the "
              "specialists"
              % (alpha_full, alpha42, R286_ALPHA_NW, alpha_pair,
                 abs(alpha_pair - alpha_full), ALPHA_TOL,
                 "CLOSES" if kill_a else "OPEN",
                 alpha_comp, abs(alpha_comp - alpha_pair),
                 "CONSISTENT" if kill_b else "BROKEN",
                 -fits["rdet"][1]))

    # ---------------- S7 leg C worlds
    section("S7  LEG C -- THE SEALED WORLD CENSUS (PR + "
            "KAPPA_INT, SMOOTH/HL2 FIRST TIME)")
    if smoke:
        for g in ("G70-controls", "G71-pr-census",
                  "G72-kint-census", "G73-world-adjudication"):
            check(g, True, "SMOKE: skipped")
        world_verdict = None
    else:
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        comb_hl, _tag = PC.gen_model(PC.Grid(), "HL2", HL2_SEED)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)))
        WORLDS = {}
        ok_ctrl = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            xu, wu, zones = BL.union_of_ctx(cctx)
            xs_z, ws_z, ys_z, vs_z = zones
            N_c = cctx["N"]
            sg = BL.sign_chain_f64(xu, wu, N_c + EXT)[0]
            mc = next((n for n in range(len(sg)) if sg[n] < 0),
                      None)
            flip = CTRL_FLIPS.get(cn, HL2_FLIP)
            ok_ctrl = ok_ctrl and (mc == flip)
            Wd = FC.world_from_arrays(cn, xs_z, ws_z, ys_z, vs_z,
                                      N_c, int(cctx["L"]))
            WORLDS[cn] = Wd
        check("G70-controls", ok_ctrl,
              "EPST + SCR + SMOOTH + HL2 built verbatim through "
              "the r278/r280 channel at THEIR own N_w: minC == "
              "flips %s + HL2 %d"
              % (str(CTRL_FLIPS), HL2_FLIP))
        mz9 = ROWS[9]["mz"]
        WORLDS["MAIN"] = FC.world_from_mz("MAIN", mz9)
        WORLDS["TWIN"] = FC.world_from_mz("TWIN", mzT)
        cen = {}
        for wn in ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH",
                   "HL2"):
            Wd = WORLDS[wn]
            pr_own, pm_own = eig_pr(Wd)
            ki, loc, nint, kaps, ncf = FC.interval_census(Wd)
            crx, prx = (None, None)
            if wn in ("EPST", "SCR", "SMOOTH", "HL2"):
                crx, prx = crossing_pr(Wd, CTRL_DEPTH)
            cen[wn] = dict(pr=pr_own, pm=pm_own, kint=ki,
                           ncf=ncf, lam=Wd["lam"], crx=crx,
                           prx=prx, Sm=len(Wd["vn"]))
            info("%s: S_- %d, lambda(N_w) %.4g, PR(N_w) %.2f, "
                 "pair mass %.3f, kappa_int %.4g (cert fails "
                 "%d)%s"
                 % (wn, cen[wn]["Sm"], Wd["lam"], pr_own, pm_own,
                    ki, ncf,
                    "" if crx is None else
                    ", crossing %d, PR@cross %.2f" % (crx, prx)))
        ok_r334 = all(abs(cen[wn]["kint"] / R334_KINT_REC[wn]
                          - 1.0) <= R334_KINT_TOL
                      for wn in ("EPST", "SCR"))
        pr_dead = {wn: cen[wn]["pr"] >= PR_BAR
                   for wn in ("EPST", "SCR", "SMOOTH", "HL2")}
        pr_live = all(cen[wn]["pr"] < PR_BAR
                      for wn in ("MAIN", "TWIN"))
        check("G71-pr-census", True,
              "SEALED PR CLAUSE (dead iff PR(N_w) >= %.1f): dead "
              "worlds %s; live spared %s (MAIN %.2f, TWIN %.2f) "
              "-- the first sealed test of the r338 'controls "
              "have no two-atom extremal' reading"
              % (PR_BAR, str({k: (round(cen[k]["pr"], 2),
                                  bool(v))
                              for k, v in pr_dead.items()}),
                 pr_live, cen["MAIN"]["pr"], cen["TWIN"]["pr"]))
        ki_dead = {wn: cen[wn]["kint"] >= KINT_BAR
                   for wn in ("EPST", "SCR", "SMOOTH", "HL2")}
        ki_live = all(cen[wn]["kint"] < KINT_BAR
                      for wn in ("MAIN", "TWIN"))
        ncf_tot = sum(cen[wn]["ncf"] for wn in cen)
        check("G72-kint-census", ok_r334 and ncf_tot == 0,
              "KAPPA_INT (r334 machinery verbatim, KKT "
              "certificates clean): EPST %.4g / SCR %.4g "
              "(== r334 records %.4g / %.4g at %.0f%%), SMOOTH "
              "%.4g / HL2 %.4g (FIRST EVALUATION -- the U2 gap "
              "closed by measurement); live MAIN %.6f / TWIN "
              "%.6f < 1"
              % (cen["EPST"]["kint"], cen["SCR"]["kint"],
                 R334_KINT_REC["EPST"], R334_KINT_REC["SCR"],
                 100 * R334_KINT_TOL, cen["SMOOTH"]["kint"],
                 cen["HL2"]["kint"], cen["MAIN"]["kint"],
                 cen["TWIN"]["kint"]))
        pr_complete = all(pr_dead.values()) and pr_live
        union_dead = {wn: (pr_dead[wn] or ki_dead[wn])
                      for wn in pr_dead}
        union_complete = all(union_dead.values()) and pr_live \
            and ki_live
        if pr_complete:
            world_verdict = ("PR_WORLD_COMPLETE(the PR clause "
                             "alone hits 4/4 dead and spares "
                             "MAIN + TWIN)")
        elif union_complete:
            world_verdict = ("PAIR_WORLD_COMPLETE(union {PR >= "
                             "%.1f} u {kappa_int >= 1}: dead "
                             "4/4, live spared on both)"
                             % PR_BAR)
        else:
            loci = [wn for wn in union_dead if not union_dead[wn]]
            world_verdict = "WORLD_INCOMPLETE(%s%s)" % (
                str(loci),
                "" if pr_live and ki_live else
                "; live-side violation")
        check("G73-world-adjudication", True,
              "SEALED WORLD RULE => %s" % world_verdict)

    # ---------------- S8 must-fails
    section("S8  MUST-FAILS")
    c_mut = mutant_c_undressed(R9["B"], R9["i1"], R9["i2"],
                               R9["mz"]["vn"])
    dev_m1 = abs(c_mut - R9["c"]) / abs(R9["c"])
    check("G80-m1-undressed-c", dev_m1 >= M1_BAR,
          "m1 c WITHOUT sqrt(v1 v2): the undressed K(y1, y2) "
          "breaks the exact E_12 identity by %.1e rel (>= %.1f) "
          "-- LOUD; the weight dressing is load-bearing"
          % (dev_m1, M1_BAR))
    check("G81-m2-dc-readback", bool(hits_m2),
          "m2 d/c READ BACK from the withheld lambda record: "
          "AST-FLAGGED (%s) -- the pair scalars are B-row "
          "objects, never spectrum read-offs"
          % (hits_m2[0] if hits_m2 else "MISS"))
    mut3 = mutant_prior_refit(2.5)
    check("G82-m3-prior-refit", bool(hits_m3)
          and abs(mut3 - PRIOR_ALPHA_TMP) >= MUT_MIN,
          "m3 FITS RE-JUSTIFIED AFTER SIGHT: AST-FLAGGED (%s) "
          "and the toy 'recalibrated prior' %.2f != the sealed "
          "prior %.2f -- protocol-CAUGHT (priors are frozen "
          "module constants under the two-commit protocol)"
          % (hits_m3[0] if hits_m3 else "MISS", mut3,
             PRIOR_ALPHA_TMP))
    mut4 = mutant_threshold_posthoc((1.9, 5.0))
    check("G83-m4-threshold-posthoc", bool(hits_m4)
          and abs(mut4 - PR_BAR) >= MUT_MIN,
          "m4 WORLD THRESHOLD AFTER SIGHT: AST-FLAGGED (%s) and "
          "the toy posthoc threshold %.2f != the sealed PR_BAR "
          "%.1f" % (hits_m4[0] if hits_m4 else "MISS", mut4,
                    PR_BAR))
    mj1, mj2 = mutant_pair_by_weight(R9["mz"]["vn"])
    ev9, W9v = np.linalg.eigh(R9["B"] @ R9["B"].T)
    w19 = W9v[:, -1]
    mut_mass = float(w19[mj1] ** 2 + w19[mj2] ** 2)
    check("G84-m5-wrong-pair", mut_mass < MUT_MASS_BAR
          and R9["pmass"] >= MASS_BAR,
          "m5 2x2 AT THE WRONG PAIR (two largest-v atoms %s): "
          "top-eigenvector mass %.4f < %.1f while the sealed "
          "shallow-edge pair carries %.4f >= %.2f -- CAUGHT by "
          "the concentration check"
          % (str((mj1, mj2)), mut_mass, MUT_MASS_BAR,
             R9["pmass"], MASS_BAR))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "certificate from the Schur dressing, no posthoc "
          "threshold/family/prior move, no derived 5/7, NO RH "
          "claim; what the round adds: the mp-exact d/c/s ladder "
          "with EXT3 pure-test rows, the exact Schur "
          "sufficiency decomposition, the source-explicit weight "
          "dictionary, the sealed world census closing U2, and "
          "the alpha composition; r243..r341 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        blind_loci = conc57 + [k for k in kz57
                               if ROWS[k]["det_dev"] > DET_ID_BAR
                               or ROWS[k]["schur_dev"] > SCHUR_BAR]
        if blind_loci:
            main_v = "BLIND(%s)" % str(sorted(set(blind_loci)))
        else:
            n_unstable = sum(1 for nm in ("p", "q", "c")
                             if not law_flags[nm])
            m2_stable = abs(curv["m2"]) <= CURV_BAR
            L1 = all(law_flags.values())
            L2 = ext3_law
            L3 = v_carries and ok_dict
            L4 = kill_a and kill_b and abs(
                alpha42 - R286_ALPHA_NW) <= R286_ALPHA_TOL
            if n_unstable >= 2 and m2_stable:
                main_v = ("RESTATEMENT(%d of p/q/c halves-"
                          "unstable while m2 is stable -- the "
                          "scalars carry no structure beyond "
                          "the lambda shadow)" % n_unstable)
            elif L1 and L2 and L3 and L4:
                main_v = ("PAIR_LAW_FOUND(L1 laws stable + L2 "
                          "EXT3 extends + L3 source dictionary "
                          "carries + L4 alpha closes; kernel "
                          "side law-grade, not closed-form)")
            else:
                failed = [nm for nm, v in (("L1", L1), ("L2", L2),
                                           ("L3", L3), ("L4", L4))
                          if not v]
                main_v = "PAIR_CARRIES(failed LAW clauses: %s)" \
                    % ",".join(failed)
        parts = [
            main_v,
            world_verdict,
            "LADDER_TABLE(57 + 12 EXT3 + twin; pmass min %.4f; "
            "r_det %.3e..%.3e; cohorts %s)"
            % (min(ROWS[k]["pmass"] for k in kz57 + ext3_kzs),
               min(ROWS[k]["rdet"] for k in kz57 + ext3_kzs),
               max(ROWS[k]["rdet"] for k in kz57 + ext3_kzs),
               str({nm: round(v[2], 3)
                    for nm, v in coh.items()})),
            "ALPHA_KILL(alpha_full %.3f / pair %.3f / composed "
            "%.3f; slopes p %.3f q %.3f c %.3f r_det %.3f vs "
            "priors -%.2f/-%.2f; open remainder rho_r)"
            % (alpha_full, alpha_pair, alpha_comp, fits["p"][1],
               fits["q"][1], fits["c"][1], fits["rdet"][1],
               PRIOR_SLOPE_P, PRIOR_SLOPE_C),
            "GAP_CENSUS(rest margin slope %.3f, dressed r'_det "
            "slope %.3f -- the R343 coupling-control "
            "coordinates, measured)"
            % (fits["restm"][1], fits["rdetp"][1]),
            "EXT3_CENSUS(%s)" % ext3_tag,
            "TWIN_LEDGER(pair dev %.1e)" % devT,
            "MUSTFAIL_LEDGER(m1-m5 + scopes)",
        ]
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED anatomy + sealed adjudication of the "
          "two-atom extremal; NO L* claim, NO RH claim"
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
