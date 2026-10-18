#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""delta_alpha_closure_probe -- PRIME.LSTAR.DELTA_ALPHA_CLOSURE.01
(round 347): THE ONE-LINE IDENTITY -- does the margin exponent
follow from the cancellation law?  The named successor round of
r345: the exact 2x2 determinant identity of the DRESSED pair block
is put in charge of the exponent bookkeeping, and the question
delta = 2.67 vs alpha = 3.33 is adjudicated as an ACCOUNTING
statement with every building block typed (theorem-grade /
certified-census / fit-census).

THE CHAIN (r342/r343/r345, all sealed records): r342 established
the two-atom law at the binding point (bare decay laws p -0.754 /
q -0.645 / c -0.697; margin exponent alpha = 3.332 on the 57 with
the composition a_p + a_q + rho_r - a_(p+q) closing to 0.007 and
rho_r = 2.624 OPEN); r343 the exact resolvent dressing (m2'/margin
in [1.0003, 1.031] -- the dressed 2x2 IS the lambda_max carrier;
the dressing works by the signed cancellation Delta c ~ -c); r345
the curvature-honest certificate on BOTH flat coordinates (r'_det,
g21; 0/75 band outliers) and THE CANCELLATION LAW c'/c ~
N_w^-2.668 (halves-stable, EXT3 10/12 high-side, EXT4 6/6;
bookkeeping slope(c') - slope(c) = -2.703 vs -2.668).  THE TYPED
ONE-LINE QUESTION (this round's contract): with the EXACT identity
    m2' (p' + q' - m2') = p' q' - c'^2 = p' q' r'_det
(2x2 algebra of the dressed block, both eigenvalue deficits are
the roots of t^2 - (p'+q') t + (p'q' - c'^2)) and the measured
near-identity m2' == margin (the r343 bridge), the margin exponent
is a SLOPE COMBINATION of dressed columns; and since r'_det is
certified flat and c'^2 = (1 - r'_det) p' q' EXACTLY, the chain
collapses -- if the dressed aspect ratios are flat -- to the ONE
LINE
    alpha == a_c + delta
(the margin exponent = the bare coupling exponent PLUS the
cancellation exponent).  The round seals the fits BEFORE the
record, closes the accounting at the bar |residual| <= 0.1, and
types every building block honestly.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO L* CLAIM, NO RH CLAIM in either
direction, mincut unchanged.  Coexistence: R346 (cover
canonization, terminal lane) may run in parallel -- this probe
touches NOTHING outside its own file and the strictly additive
rh-sync.  Two-commit freeze protocol (r329 convention): spec +
machinery committed BEFORE the record run, record tables inserted
after.

THE EXACT OBJECTS (all gated): per rung the r342 bundle
(PX.build_rung verbatim, SPEC_SHA prefix gated b09f8ccd) already
carries the dressed scalars (d1', d2', c') = the Schur block
A + C (I-D)^{-1} C^T, hence p' = 1 - d1', q' = 1 - d2', r'_det =
1 - c'^2/(p'q'), m2' = 1 - lambda_max(2x2'); THE ONE-LINE IDENTITY
(this round's exact spine, gated per rung): the two deficits
1 - lambda_+' and 1 - lambda_-' of the dressed 2x2 are the roots
of t^2 - s t + (p'q' - c'^2) with s = p' + q', hence EXACTLY
    m2' (s - m2') = p' q' - c'^2 = p' q' r'_det,
verified in exact Fractions on the 3x3 hand toy (the rational
product form det(I - A') == p'q' - c'^2) and per rung in f64 at
the backward-error scale (residual / (p'q' + c'^2) <= 1e-8; the
deficit m2' itself carries a 1 - lambda cancellation, sized in
scoping at <= 3.0e-10); the definitional ward c'^2 ==
(1 - r'_det) p' q' at 1e-12; THE BRIDGE (r343, now protocol-
graded): the ratio column m2'/margin over ALL 75 arbitrated rows
with the sealed clause max |m2'/margin - 1| <= 0.10 AND Theil-Sen
|slope| <= 0.15 -- the dressed second determinant IS the margin;
THE EXPONENT ACCOUNTING (Leg B): sealed Theil-Sen fits on the 57
for the dressed columns p', q', c', m2', s' = p'+q'-m2', the
bridge ratio, |c'/c| (delta), p'/p and q'/q (the dressed
dictionary factors), each with halves curvature and EXT3/EXT4
band counts from the 57-fit; THE FOUR CLOSURES (each bar 0.1):
  C1 (identity route)  alpha_meas == alpha_id = -(s_p' + s_q' +
     s_r' - s_s' - s_bridge)  [the fitted-slope image of the
     exact identity + the bridge],
  C2 (margin bridge)   slope(margin) == slope(m2'),
  C3 (cancellation bookkeeping)  slope(c') == slope(c) +
     slope(c'/c)  [the r345 census -3.401 vs -3.365,
     re-adjudicated with sealed fits],
  C4 (THE ONE LINE)    alpha_meas == a_c + delta = -slope(c) -
     slope(c'/c)  [uses NO dressed diagonal column: the margin
     exponent reduced to the bare coupling law + the cancellation
     law + flatness certificates];
THE SUPPORT CLAUSES: CURV_FLAT(r'_det) re-gated under the r345
protocol verbatim (GR.curvflat_protocol, SPEC_SHA prefix gated
1f99235a); the AUX band clauses (the aspect columns p'/q' and
s'/c' inside 0.5 decades of their 57-median on >= 73 of 75 rows,
no row beyond 0.75 -- the flat-aspect step that turns C1 into
C4); the delta-law re-gate (r345 clauses on |c'/c|: |curv| <=
0.35, EXT3 >= 10/12 in the 0.5-decade band, EXT4 n_low <= 1,
delta >= 0.5); the c-law re-gate (r342 clauses: |curv| <= 0.35,
EXT3 >= 10/12).

LEG C -- THE DRESSED DICTIONARIES: the factor columns f_p = p'/p
and f_q = q'/q (the dressing eats Delta d/p -> 1.000, r343),
adjudicated BOTH ways sealed: (i) DRESSED_DICTIONARY_GO iff both
pass the full r345 curvature-honest FLAT protocol -- p', q' would
then inherit the r342 dictionary slopes unchanged; (ii) else
DRESSED_RESIDUAL_LAW iff both pass the decay-law clauses (|curv|
<= 0.35, EXT3 >= 10/12, EXT4 n_low <= 1, delta_x >= 0.5) -- the
dressed diagonals then inherit the bare dictionary slopes MINUS a
residual cancellation exponent, with the universality census
|delta_p - delta| and |delta_q - delta| printed; (iii) else
DRESSED_FACTOR_CENSUS.  Source side re-gated (r342 route
verbatim): digamma dictionary at the pair folds <= 0.02 and
v_pred <= 0.10 on the six sample rungs -- the WEIGHT side of the
bare scalars stays closed-form, the kernel side census-grade
(r342 negative #4, never upgraded).

LEG D -- THE MIRROR WORLD CLAUSE (the r345 by-catch, sealed):
per world the rest block D at the pair, lambda_rest, and the
finite-order mirror rho_32 = -(sum_{k<=32} u_1^T D^k u_2)/c
(GR.mirror_profile verbatim).  SEALED RULE: mirror EXISTS iff
lambda_rest < 1 (the path series converges); LIVE-side iff it
exists AND |rho_32 - 1| <= MIRROR_LIVE_BAR = 0.5; DEAD-side iff
lambda_rest >= 1 (the finite-order series explodes; |rho_32|
printed, NONFINITE disclosed).  Evaluated on MAIN / TWIN / EPST /
SCR / SMOOTH / HL2 (r278/r280 channel verbatim, flips gated) AND
on the r330 second worlds DIRICHLET / DIRICHLET_ABS
(DSW.dirichlet_comb / dirichlet_abs_comb verbatim, SPEC_SHA
prefix gated 66526018, through the SAME MS/BL/FC channel) -- the
first structural test of the cancellation on a second living
arithmetic; honesty: the r330 record already SPLIT the
half-filling wall on these variants, and the w9 scoping (s1,
disclosed below) already shows both land dead-side in the E-Gram
frame (DIR lambda_rest 3.97e37, ABS 2.28e5) -- the sealed clause
TYPES this, it does not force a living-world reading;
MIRROR_WORLD_CLAUSE_SEALED iff the rule separates live 2/2 from
dead 4/4 with the Dirichlet columns typed by the same rule.

INDEX FIREWALL (binding, r238-r345 discipline): w = window (kz
into the prime-power list), S = #union atoms, S_- = #nu atoms,
N_w = (S+1)//2; ground truth (r283/r284/r286/r329/r334/r342/r343/
r345 records, control flips, kappa_int records) enters GATES and
record tables only; the module-own constructors consume kernel
Gram / spectrum / weight / position arrays and measured columns
ONLY (AST scope audit; withheld identifiers are the RECORD values
and the verdict-side columns); no zero/prime oracles anywhere
(AST firewall; the prime-power grid is the sealed source comb,
r238 convention); no fit primitives (fragment audit; fits are the
imported r286 Theil-Sen; the flat protocol is the imported r345
curvflat_protocol with its module-sealed constants).  MACHINERY
IMPORTED VERBATIM: r342 PX.{build_rung, pair_select, pair_eigs,
det_reserve, schur_dress, arch_dict_density, v_predict,
layer_split} (b09f8ccd), r343 PC3.extend_rung (9ffc2705, w9
anchors g21/K_res only), r345 GR.{curvflat_protocol,
mirror_profile, slope_pair_ci} (1f99235a), r330 DSW.{
dirichlet_comb, dirichlet_abs_comb} (66526018), document pipeline
V.{build_measures, mu_chain, b_matrix, admissible_indices,
lam_max_at, U, W_VM, PP}, r286 LM.{ts_fit, ts_slope_free,
ext_rule}, r334 FC.{world_from_arrays, world_from_mz,
interval_census}, r278 MS.ctx_build, r280 BL.{union_of_ctx,
sign_chain_f64}, v881 PIK.lambda_eps, r243 PB.smooth_comb,
paircorr PC.{Grid, gen_model}, r331 TR.{base_comb, build_world},
r289 AKD.twin_rational, r276 MF.local_gaps, v563 core READ-ONLY.

LEG 0 -- ANCHORS BIT-NEAR (r342/r343/r345 record numbers as
gates): w9 records (S 367, N_w 184, lambda 0.99983248, margin
1.6752e-4); w9 dressed row (d1' 0.999154, d2' 0.998710, c'
0.000872, r'_det 0.302916, lambda_rest 0.996338); w9 r345 row
(c'/c 2.7047e-2, g21 7.517, K_res 2, rho_32 0.9225); the scoped
w9 closure coordinates (p' 8.4606e-4, q' 1.2903e-3, m2'
1.6800e-4, m2'/margin 1.0029, p'/q' 0.6557, s/c' 2.4490 with s =
p'+q', p'/p 2.822e-2, q'/q 3.676e-2); the scoped sample bridges
(kz44 1.0081, kz56 1.0049, kz130 1.0180) and aspects (p'/q'
0.4871 / 0.5148 / 0.3429); the r343 medians (m2'/margin 1.0058,
rho' 0.846); kz56 (r'_det 0.1605); the span anchors (min 0.1383
at kz98, max 0.5361 at kz57); the r342/r345 fit slopes (margin
-3.332, c -0.697, p -0.754, q -0.645, rdetp +0.018, |c'/c|
-2.668, |c'| -3.401) and curvatures (cpc -0.189, rdetp -0.426,
margin -0.347, c +0.308) as DISCLOSED PRIORS; the digamma/tent
dictionary bars (DIGAMMA_BAR 0.02, V_BAR 0.10); the r334/r345
kappa_int records and control flips.

LEG E -- MUST-FAILS (>= 5, each loud): (m1) THE IDENTITY WITH THE
WRONG NORMALIZATION: m2' (p'+q'+m2') instead of m2' (p'+q'-m2')
-- breaks the exact identity by >= 0.1 rel at w9 (the deficit
enters the second factor SIGNED) and loudly on the hand toy;
exactly CAUGHT.  (m2) THE CLOSURE BAR RE-PICKED AFTER SIGHT: a
mutant consuming the withheld measured residual -- AST-FLAGGED,
and on the sealed toy returns != CLOSURE_BAR (protocol-CAUGHT:
the bars are frozen module constants under the two-commit
protocol).  (m3) ALPHA READ CIRCULARLY off the margin column
instead of the identity slopes: a mutant consuming the withheld
margin column -- AST-FLAGGED; the real alpha_id constructor
consumes fitted dressed-column slopes only (scope-audited).
(m4) THE DICTIONARY FACTOR READ BACK from the withheld lambda
record -- AST-FLAGGED.  (m5) THE MIRROR-LIVE BAR RE-PICKED AFTER
SIGHT of the world rho column -- AST-FLAGGED, and on the sealed
toy returns != MIRROR_LIVE_BAR.  STOP LIST (anti-gates, binding):
NO L* claim, NO bound mechanism promoted, NO certificate reading
of any census, NO posthoc bar / band / family / prior move, NO
derived 5/7, NO RH claim, mincut unchanged; r243..r346 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN 1.6752e-4
rel 0.01; PX_SHA b09f8ccd; PC3_SHA 9ffc2705; GR_SHA 1f99235a;
DSW_SHA 66526018; W9 ANCHORS d1p 0.999154 rel 1e-5 / d2p 0.998710
rel 1e-5 / cp 8.7234e-4 rel 1e-3 / rdetp 0.302916 rel 1e-3 /
lam_rest 0.996338 abs 1e-5 / ppr 8.4606e-4 rel 1e-3 / qpr
1.2903e-3 rel 1e-3 / m2p 1.6800e-4 rel 1e-3 / bridge 1.0029 abs
5e-3 / cpc 2.7047e-2 rel 1e-3 / g21 7.517 abs 0.01 / kres 2 /
rho32 0.9225 abs 5e-3 / fp 2.822e-2 rel 1e-2 / fq 3.676e-2 rel
1e-2 / pqr 0.6557 abs 5e-3 / spc 2.4490 abs 0.02; SAMPLE ANCHORS
bridge (kz44 1.0081, kz56 1.0049, kz130 1.0180) abs 5e-3, pqr
(0.4871, 0.5148, 0.3429) abs 5e-3; MED ANCHORS bridge 1.0058 abs
5e-3, rhop 0.846 abs 0.01; KZ56 rdetp 0.1605 abs 2e-3; SPAN (min
0.1383 @ kz98, max 0.5361 @ kz57) abs 5e-3; FIT ANCH (margin
-3.332, c -0.697, p -0.754, q -0.645, rdetp +0.018, cpc -2.668,
cp -3.401) tol 0.02; CURV ANCH (cpc -0.189, rdetp -0.426, margin
-0.347, c +0.308) tol 0.03; EXT3_KZ_B (42, 51, 54, 56, 58, 62);
EXT3_KZ_A (96, 123, 125, 127, 128, 130); EXT3_NW (1721, 2577);
EXT4_KZ_B (72, 75, 66); EXT4_KZ_A (113, 111, 108); EXT4_NW (2656,
3181) (the r343 sealed selections adopted AS-IS); ID_BAR 1e-8;
RDEF_BAR 1e-12; CLOSURE_BAR 0.1; BRIDGE_DEV_BAR 0.10;
BRIDGE_SLOPE_BAR 0.15; AUX_BAND 0.5; AUX_OUT_MAX 2; AUX_HARD
0.75; DEC_CURV_BAR 0.35; DEC_BAND 0.5; DEC_EXT3_MIN 10;
DEC_EXT4_LOW 1; DELTA_MIN 0.5; C_EXT3_MIN 10; MIRROR_LIVE_BAR
0.5; MIRROR_K 32; TOY_ALPHA 3.4; TOY_RP 0.3; TOY_BRIDGE 1.005;
C1_TOY_BAR 1e-9; DIGAMMA_BAR 0.02; V_BAR 0.10; SAMPLE_KZ (18, 9,
52, 119, 42, 130); KINT RECORDS {EPST 1793.99, SCR 8.51e6, SMOOTH
2.193, HL2 1964} rel 0.05, live 0.999567 rel 1e-3; CTRL_FLIPS
{EPST 25, SCR 21, SMOOTH 27}, HL2 seed 101 flip 25; EXT 8;
TWIN_TOL 1e-8; TWIN_BAR 1e-3; M1_BAR 0.1; MUT_MIN 1e-6; TOY_TOL
1e-12; runtime <= 1800 s; smoke = toys + firewall + scopes +
mutants + w9 block (records, dressed anchors, one-line identity
live, bridge, mirror + factor anchors); ladder, twin, fits,
protocols, closures, worlds and adjudication skipped.

PRE-SPEC SCOPING (disclosed, r343-s1/r345-s1 precedent -- no bar,
band, threshold, family or adjudication rule was tuned after any
evaluation except as sized here and said so): (s1) FOUR sample
rungs (kz9, kz44, kz56, kz130 -- all four already printed in the
r342/r343/r345 records) were probed end-to-end for machinery and
bar sizing: the one-line identity residual (backward-error scale)
spans 1.5e-14 (w9) .. 3.0e-10 (kz56) -- sizing ID_BAR 1e-8; the
definitional ward c'^2 == (1-r')p'q' <= 1.1e-16 -- RDEF_BAR
1e-12; bridges m2'/margin 1.0029 / 1.0081 / 1.0049 / 1.0180 --
sizing BRIDGE_DEV_BAR 0.10 (the r343 record says [1.0003, 1.031]
on every scoped row incl. EXT4); aspects p'/q' 0.343..0.656 and
s/c' 2.45..2.80 (both far inside the 0.5-decade AUX band); the
naive two-point slopes w9 -> kz130 (p' -4.05, q' -3.81, c'
-3.94, m2' -3.95, margin -3.95; p'/p -3.46, q'/q -3.34, c'/c
-3.41) -- steeper than the 57-fits will be (the r286 deep-family
curvature), they size NOTHING except the expectation that the
dressed-factor columns are NOT flat (the GO clause of Leg C is
expected NOT to fire; the clause is sealed symmetric anyway);
(s2) the DIR/ABS worlds were built ONCE at w9 through the
MS/BL/FC channel for construction sanity: both construct (S_-
124 / 106) and both land DEAD-side (DIR lambda 5.70e37,
lambda_rest 3.97e37, rho_32 NONFINITE; ABS lambda 2.28e5,
lambda_rest 2.28e5, rho_32 -3.8e176) -- DISCLOSED HONESTLY: the
w9 Dirichlet dead-side result was seen before the freeze; the
sealed mirror rule types it, the six standard worlds and the
whole ladder-side adjudication carry the blind weight.  Runtime
scoping 1.6 s for the four rungs + two worlds; the full run is
sized comfortably under the 1800 s bar.  No ladder-wide fit,
median, protocol clause or closure was evaluated before this
spec froze; the slopes cited above are published record numbers
or the disclosed two-point scoping values, never sealed-fit
previews.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > ACCOUNTING_GAP > ALPHA_CLOSED >
ALPHA_CLOSED_CENSUS -- the enum is exhaustive):
  [exactly one of]
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  ACCOUNTING_GAP(residuals, loci)  iff C2 or C4 misses the 0.1
    bar -- the core reduction is broken, named where /
  ALPHA_CLOSED(alpha_id, a_c + delta, residuals; building blocks
    typed)  iff C1 AND C2 AND C3 AND C4 AND the bridge clause AND
    CURV_FLAT(r'_det) re-gates AND both AUX bands hold AND the
    delta-law re-gates AND the c-law re-gates -- the margin
    exponent is REDUCED to {the bare coupling law a_c (fit-census;
    weight side closed-form), the cancellation law delta (sealed
    fit-census law), the flatness certificates (certified
    census)} through a theorem-grade identity /
  ALPHA_CLOSED_CENSUS(failed support clauses)  iff C2 AND C4 hold
    but a support clause fails
  + [exactly one of] DRESSED_DICTIONARY_GO(both factors flat) /
    DRESSED_RESIDUAL_LAW(delta_p, delta_q, universality census) /
    DRESSED_FACTOR_CENSUS(numbers) [always]
  + [exactly one of] MIRROR_WORLD_CLAUSE_SEALED(live 2/2, dead
    4/4, Dirichlet typed) / MIRROR_WORLD_INCOMPLETE(loci)
    [always]
  + IDENTITY_LEDGER(per-rung devs, Fractions toy) [always]
  + EXPONENT_LEDGER(all sealed slopes + curvatures + bands, the
    four closure residuals) [always]
  + WORLD_LEDGER(lambda_rest separation, kappa_int anchors,
    mirror column incl. DIR/ABS) [always]
  + TWIN_LEDGER(dressed-scalar deviations) [always]
  + MUSTFAIL_LEDGER(m1-m5 + scopes) [always].
Honesty before beauty: the one-line identity is an exact
finite-matrix fact (theorem-grade SKELETON) whose inputs are
measured window scalars (census-grade FLESH); the closures are
consistency statements between SEALED Theil-Sen fits on 57 finite
windows, never asymptotic theorems; a_c and delta remain measured
laws (fit-census with sealed honesty meters) -- the reduction
moves the open analytic remainder from rho_r = 2.624 (r342) to
the SINGLE exponent delta of the cancellation law, it does not
derive delta from the source; the flatness certificates are
sealed census protocols (r345 grade); the mirror world clause is
a measured discriminator on eight instrumented worlds; no verdict
claims L*, a bound mechanism, a derived 5/7, or RH progress in
any direction.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit, which IS the protocol; TWO-COMMIT PROTOCOL
EXECUTED: the sealed spec above was committed as "r347 pre-freeze"
(95f7f944, SPEC_SHA freeze 99100cea2358fe56) BEFORE the first
full evaluation; chronology honest: smoke pass 1 = 32/34 with ONE
machinery finding, fixed BEFORE the freeze commit: the w9 anchor
constant for the aspect (p'+q')/c' carried an arithmetic slip
(3.4494 written where the s1 scoping value is 2.4490) -- constant
and spec text corrected, no adjudication rule touched; smoke pass
2 = 34/34 (0.2 s), byte-identical on re-run; pre-freeze commit
95f7f944; calibration pass 1 = FIRST full evaluation = 34/34
(47.6 s), NO amendment; record run1 = 34/34 (49.9 s), run2 =
34/34 (50.2 s), byte-identical up to WALL and identical to the
calibration pass):
MAIN VERDICT = ALPHA_CLOSED -- the margin exponent FOLLOWS from
the cancellation law: all four sealed closures hit inside the 0.1
bar (C1 identity route |alpha 3.332 - alpha_id 3.382| = 0.050;
C2 margin bridge |{-3.332} - {-3.334}| = 0.001; C3 cancellation
bookkeeping |slope(c') -3.401 - (slope(c) + slope(c'/c)) -3.366|
= 0.035; C4 THE ONE LINE |alpha 3.332 - (a_c 0.697 + delta 2.668)
= 3.366| = 0.033), the bridge clause holds on all 75 rows (max
|m2'/margin - 1| = 0.0605 <= 0.10, ratio slope +0.0001 -- the
dressed second determinant IS the margin, now protocol-graded
ladder-wide), CURV_FLAT(r'_det) re-gates 0 out/0 hard of 75
(slope +0.028, CI [-0.739, +0.825] containing 0, drift 0.012),
both AUX aspect bands hold 0 out/0 hard (p'/q' max dev 0.231 dec
around med 0.5586, s/c' max dev 0.101 dec around med 2.4690 --
the flat-aspect step that turns the identity into the one line),
the delta-law re-gates (delta 2.668, curv -0.189, EXT3 10/12 low
0, EXT4 6/6 low 0) and the c-law re-gates (curv +0.308, EXT3
11/12) -- THE BUILDING BLOCKS TYPED: the identity m2'(p'+q'-m2')
= p'q' - c'^2 = p'q' r'_det is THEOREM-GRADE (exact Fractions on
the toy, f64 max residual 3.3e-09 on 75/75 at the backward-error
scale, definitional ward 1.8e-16); the bridge, the r'_det
flatness and the aspect bands are CERTIFIED CENSUS (sealed
protocols, 0 violations); a_c = 0.697 and delta = 2.668 are
FIT-CENSUS laws with sealed honesty meters (the weight side of
the bare scalars stays closed-form: digamma 2.4e-3, v_pred
9.0e-4 on the six sample rungs) -- the open analytic remainder
of the L* margin law is REDUCED from rho_r = 2.624 (r342) to the
single cancellation exponent delta: one measured law instead of
three, connected by exact algebra and certified flats
+ DRESSED_FACTOR_CENSUS(the GO clause does NOT fire (both factor
columns fail the flat protocol loudly: all-75 protocol slopes
-2.478/-2.478 with CI [-3.958, -1.201] / [-4.066, -1.172]
excluding 0 -- the dressed diagonals do NOT inherit the bare
dictionary slopes unchanged) and the residual-law clause does
NOT fire either: p'/p passes every decay clause (delta_p 2.609,
curv -0.129, EXT3 11/12 low 0, EXT4 6/6 low 0) but q'/q is
halves-CURVED (delta_q 2.665, curv -0.508 > 0.35, EXT3 12/12,
EXT4 6/6) -- the factor laws are typed as CENSUS: p'/p ~
N^-2.609, q'/q ~ N^-2.665 with the UNIVERSALITY CENSUS
|delta_p - delta| = 0.059, |delta_q - delta| = 0.003 -- the
dressing eats p, q and c at a COMMON rate to within 0.06, but
the q-column's curvature keeps the common-rate statement
census-grade, honestly NOT a sealed law)
+ MIRROR_WORLD_CLAUSE_SEALED(live 2/2: MAIN/TWIN lambda_rest
0.996338 < 1 with rho_32 = 0.9225/0.9225, |rho_32 - 1| = 0.078
<= 0.5; dead 4/4: lambda_rest >= 1 and the finite-order mirror
EXPLODES (SMOOTH +7.87e6, EPST -1.71e109, HL2 -4.70e113, SCR
-6.5e198); DIRICHLET TYPED DEAD-SIDE: DIR lambda 5.70e37 /
lambda_rest 3.97e37 (series NONFINITE), ABS lambda 2.28e5 /
lambda_rest 2.28e5 (series explodes -3.85e176) -- the r330
half-filling split RESTATES structurally in the E-Gram frame:
the chi-twist and even the bare p=3 atom removal destroy the
rest-block contraction entirely, the mirror never gets to exist;
the first second-arithmetic test of the cancellation returns
DEAD-side, typed, not forced)
+ IDENTITY_LEDGER(Fractions toy EXACT (det(I-A') == p'q' - c'^2
as rationals); per-rung residuals max 3.3e-09 of 75 (bar 1e-8,
the depth conditioning as scoped); definitional ward max 1.8e-16
(bar 1e-12); the wrong-normalization mutant breaks by 1.7e-01 at
w9 and 1.1e+00 on the toy)
+ EXPONENT_LEDGER(sealed 57-fits (slope | curv | EXT3 in/low |
EXT4 in/low): p' -3.422 | +0.022 | 6/12, 0 | 3/6, 0; q' -3.359 |
-0.241 | 6/12, 0 | 3/6, 0; c' -3.401 | -0.140 | 6/12, 0 | 3/6,
0; m2' -3.334 | -0.368 | 9/12, 0 | 3/6, 0; s' -3.381 | -0.124 |
6/12, 0 | 3/6, 0; bridge -0.001 | -0.007 | 12/12 | 6/6; p'/q'
-0.068 | +0.160 | 12/12 | 6/6; p'/p -2.609 | -0.129 | 11/12 |
6/6; q'/q -2.665 | -0.508 | 12/12 | 6/6; anchors margin -3.332 |
-0.347, c -0.697 | +0.308, p -0.754, q -0.645, rdetp +0.018,
|c'/c| -2.668 | -0.189, |c'| -3.401 all == the disclosed priors
at tol 0.02/0.03; the dressed-decay EXT3/EXT4 misses are ALL
high side (n_low 0 everywhere: the deep family decays SLOWER
than the 57-fit -- the r286 curvature restated as census);
closure residuals C1 0.050 / C2 0.001 / C3 0.035 / C4 0.033, all
<= 0.1; symmetry census 2 s_c' - s_p' - s_q' = -0.020 ~ 0)
+ WORLD_LEDGER(lambda_rest separation re-gated 4/4 dead >= 1 vs
live 0.996338 < 1; kappa_int == records at 5 percent (EPST
1793.99 / SCR 8.509e6 / SMOOTH 2.193 / HL2 1964.35, live
0.999567); 8 instrumented worlds -- the Dirichlet pair enters
the L* lane for the first time)
+ TWIN_LEDGER(dressed scalars dev <= 2.3e-6, m2' dev 1.4e-5,
r'_det dev 9.1e-6, lambda_rest dev 3.5e-8 (bar 1e-3); dose-zero
identity BITWISE)
+ MUSTFAIL_LEDGER(m1 wrong normalization breaks 1.7e-01 >= 0.1
at w9 + 1.1e+00 on the toy; m2 AST-FLAGGED resid_true + toy 0.06
!= the sealed 0.10; m3 AST-FLAGGED margin_col_true (the real
alpha_id constructor consumes fitted dressed slopes only,
scope-audited CLEAN); m4 AST-FLAGGED REC_LAM; m5 AST-FLAGGED
rho_col_true + toy 5e5 != the sealed 0.5; constructor scopes +
fragment audit CLEAN).
Key numbers.  W9: p' 8.4606e-4, q' 1.2903e-3, c' 8.7234e-4, m2'
1.6800e-4, m2'(p'+q'-m2') = 3.306823e-7 == p'q' - c'^2 (residual
1.5e-14), m2'/margin 1.0029, r'_det 0.302916, c'/c 2.7047e-2,
p'/p 2.8215e-2, q'/q 3.6765e-2, p'/q' 0.6557, (p'+q')/c' 2.4490,
g21 7.5175, K_res 2, rho_32 0.9225 -- the r347 coordinates start
exactly where r342/r343/r345 left them; cohort medians
m2'/margin 1.0058 and rho' 0.8459 == the r343 records; kz56
r'_det 0.1605, span kz98 0.1383 / kz57 0.5361 == r345.
HONEST NEGATIVES: (1) the closure does NOT derive delta from the
source -- alpha is reduced to a_c + delta, and delta stays a
measured law: the open analytic question is now ONE exponent
instead of three, and the typed specialist question is why the
rest space mirrors the pair cross-term AND (census) the diagonal
deficits near a common rate N^-2.6..2.7; (2) the dressed decay
columns extend to EXT3/EXT4 only 6/12 + 3/6 in band (ALL misses
high side, n_low 0) -- the closure holds ON the 57-fit family
and its deep extension carries the known r286 curvature, said
with numbers, never certified; (3) the residual-law tag for the
dressed dictionaries does NOT fire (q'/q halves curvature -0.508
> 0.35): Leg C closes as census, not as law -- the universality
reading (0.059/0.003) is a two-decimal coincidence measurement
on 57 windows; (4) the bridge max deviation 0.0605 (ladder-wide)
is twice the r343 scoped span [1.0003, 1.031] -- the deep EXT
rows stretch the bridge, still 40 percent below the sealed bar;
(5) the identity-route alpha_id 3.382 differs from alpha 3.332
by 0.050 -- Theil-Sen slopes are not exactly additive across
curved columns; the exact identity holds per row at 3.3e-9, the
0.050 is pure fit-instrument non-additivity, disclosed; (6) the
Dirichlet mirror test is a DEAD-side typing, not a living-world
confirmation -- inside the MAIN frame no second living
arithmetic exists yet (the r330 honest limit restated; a
GRH-faithful Dirichlet frame stays the named follow-up).  R348
SKETCH (candidates, not commitments): (i) the delta source
anatomy -- the r345 mode profile says the mirror is order-0-
dominated (rho_0 median 0.839): does u1.u2/c alone already carry
the N^-2.67 law (a Gram-row correlation statement,
dictionary-reachable)?; (ii) the common-rate question delta_p ==
delta_q == delta as an exact statement of the resolvent block
(theorem candidate: the dressed block deficit is rank-one-
dominated); (iii) the GRH-faithful Dirichlet frame for the
sealed mirror discriminator.  Runtime 49.9 / 50.2 s record, 47.6
s calibration, 0.2 s smoke; deterministic, run1/run2
byte-identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE except
this record-table insertion.

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

import pair_extremal_probe as PX                 # noqa: E402 r342
import pair_coupling_probe as PC3                # noqa: E402 r343
import gap_ratio_primary_probe as GR             # noqa: E402 r345
import dirichlet_secondworld_probe as DSW        # noqa: E402 r330
import verify_lstar_instance as V                # noqa: E402 document
import lstar_margin_scaling_probe as LM          # noqa: E402 r286
import fold_capacity_probe as FC                 # noqa: E402 r334
import metric_stability_probe as MS              # noqa: E402 r278
import budget_localization_probe as BL           # noqa: E402 r280
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import principal_bessel_probe as PB              # noqa: E402 r243
import paircorr_margin_probe as PC               # noqa: E402
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SM, REC_NW = 367, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
PX_SHA_PREFIX = "b09f8ccd"
PC3_SHA_PREFIX = "9ffc2705"
GR_SHA_PREFIX = "1f99235a"
DSW_SHA_PREFIX = "66526018"
W9_ANCH = dict(d1p=0.999154, d2p=0.998710, cp=8.7234e-4,
               rdetp=0.302916, lam_rest=0.996338,
               ppr=8.4606e-4, qpr=1.2903e-3, m2p=1.6800e-4,
               bridge=1.0029, cpc=2.7047e-2, g21=7.517, kres=2,
               rho32=0.9225, fp=2.822e-2, fq=3.676e-2,
               pqr=0.6557, spc=2.4490)
SAMPLE_ANCH = {44: dict(bridge=1.0081, pqr=0.4871),
               56: dict(bridge=1.0049, pqr=0.5148),
               130: dict(bridge=1.0180, pqr=0.3429)}
MED_ANCH = dict(bridge=1.0058, rhop=0.846)
KZ56_RDETP = 0.1605
SPAN_ANCH = dict(min_rdetp=0.1383, min_kz=98,
                 max_rdetp=0.5361, max_kz=57)
FIT_ANCH = dict(margin=-3.332, c=-0.697, p=-0.754, q=-0.645,
                rdetp=0.018, cpc=-2.668, cp=-3.401)
FIT_ANCH_TOL = 0.02
CURV_ANCH = dict(cpc=-0.189, rdetp=-0.426, margin=-0.347,
                 c=0.308)
CURV_ANCH_TOL = 0.03
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN, EXT3_NW_MAX = 1721, 2577
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT4_NW_MIN, EXT4_NW_MAX = 2656, 3181
ID_BAR = 1.0e-8
RDEF_BAR = 1.0e-12
CLOSURE_BAR = 0.1
BRIDGE_DEV_BAR = 0.10
BRIDGE_SLOPE_BAR = 0.15
AUX_BAND = 0.5
AUX_OUT_MAX = 2
AUX_HARD = 0.75
DEC_CURV_BAR = 0.35
DEC_BAND = 0.5
DEC_EXT3_MIN = 10
DEC_EXT4_LOW = 1
DELTA_MIN = 0.5
C_EXT3_MIN = 10
MIRROR_LIVE_BAR = 0.5
MIRROR_K = 32
TOY_ALPHA = 3.4
TOY_RP = 0.3
TOY_BRIDGE = 1.005
C1_TOY_BAR = 1.0e-9
DIGAMMA_BAR = 0.02
V_BAR = 0.10
SAMPLE_KZ = (18, 9, 52, 119, 42, 130)
KINT_REC = {"EPST": 1793.99, "SCR": 8.51e6, "SMOOTH": 2.193,
            "HL2": 1964.0}
KINT_REC_TOL = 0.05
KINT_LIVE_REC = 0.999567
KINT_LIVE_TOL = 1.0e-3
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
EXT = 8
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
M1_BAR = 0.1
MUT_MIN = 1.0e-6
TOY_TOL = 1.0e-12

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
    return (not bad), ("NO zero/prime oracles; the module-own "
                       "constructors consume kernel Gram / spectrum "
                       "/ weight / position arrays and measured "
                       "columns ONLY; record numbers and flips "
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


CONSTRUCTORS = ("closure_cols", "alpha_from_slopes",
                "bridge_stats", "decay_law", "aux_band",
                "mirror_world_row")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "KINT_REC", "FIT_ANCH",
                   "CURV_ANCH", "W9_ANCH", "MED_ANCH",
                   "SAMPLE_ANCH", "resid_true",
                   "margin_col_true", "rho_col_true"}


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


# ============== module-own constructors (AST-audited)
def closure_cols(R):
    """the r347 closure coordinates of one r342 rung bundle:
    dressed deficits, the one-line identity residual (backward-
    error scale), the definitional ward, the bridge and aspect
    columns; consumes Gram-derived rung scalars only."""
    pp = 1.0 - R["d1p"]
    qq = 1.0 - R["d2p"]
    cp = R["cp"]
    m2p = R["m2p"]
    s = pp + qq
    lhs = m2p * (s - m2p)
    rhs = pp * qq - cp * cp
    dev_id = abs(lhs - rhs) / max(pp * qq + cp * cp, 1e-300)
    dev_rdef = abs(cp * cp - (1.0 - R["rdetp"]) * pp * qq) \
        / max(pp * qq, 1e-300)
    return dict(ppr=pp, qpr=qq, cpr=cp, m2p=m2p, spr=s - m2p,
                bridge=(m2p / R["margin"] if R["margin"] > 0
                        else float("nan")),
                pqr=pp / qq, spc=s / abs(cp),
                cpc=abs(cp / R["c"]), fp=pp / R["p"],
                fq=qq / R["q"],
                rhop=cp / math.sqrt(pp * qq),
                dev_id=dev_id, dev_rdef=dev_rdef)


def alpha_from_slopes(s_pp, s_qp, s_rp, s_sp, s_br):
    """the identity-route margin exponent: from the exact one-line
    identity m2' (p'+q'-m2') = p' q' r'_det and margin =
    m2' / (m2'/margin), in fitted slopes alpha_id = -(s_p' + s_q'
    + s_r'det - s_s' - s_bridge); consumes fitted dressed-column
    slopes only (anti-circular: no margin column enters)."""
    return -(s_pp + s_qp + s_rp - s_sp - s_br)


def bridge_stats(m2p_col, margin_col, lnN):
    """the sealed bridge clause statistics: max |m2'/margin - 1|
    and the Theil-Sen slope of the ratio; consumes measured
    columns only."""
    r = np.asarray(m2p_col, float) / np.asarray(margin_col, float)
    ft = LM.ts_fit(np.asarray(lnN, float), np.log(r))
    return float(np.max(np.abs(r - 1.0))), float(ft[1]), r


def decay_law(lnN57, y57, ext3_pairs, ext4_pairs):
    """the sealed decay-law instrument (r342/r345 convention):
    Theil-Sen fit + halves curvature on the 57, EXT3/EXT4 band
    counts from the 57-fit (0.5 decades); consumes column arrays
    only."""
    lnN57 = np.asarray(lnN57, float)
    y57 = np.asarray(y57, float)
    ft = LM.ts_fit(lnN57, y57)
    a0, b0 = float(ft[0]), float(ft[1])
    o = np.argsort(lnN57)
    half = len(o) // 2
    s_lo = LM.ts_slope_free(lnN57[o[:half]], y57[o[:half]])
    s_hi = LM.ts_slope_free(lnN57[o[half:]], y57[o[half:]])

    def band(pairs):
        n_in, n_low = 0, 0
        for lnn, lv in pairs:
            lg = (lv - (a0 + b0 * lnn)) / math.log(10.0)
            if abs(lg) <= DEC_BAND:
                n_in += 1
            elif lg < -DEC_BAND:
                n_low += 1
        return n_in, n_low

    e3_in, e3_low = band(ext3_pairs)
    e4_in, e4_low = band(ext4_pairs)
    return dict(slope=b0, curv=float(s_hi - s_lo), e3_in=e3_in,
                e3_low=e3_low, e4_in=e4_in, e4_low=e4_low)


def aux_band(vals57, vals_all):
    """the sealed AUX flat-aspect band: deviations (decades) of
    ALL arbitrated rows from the 57-median; consumes measured
    columns only."""
    med = float(np.median(np.asarray(vals57, float)))
    devs = np.abs(np.log10(np.asarray(vals_all, float) / med))
    return (int(np.sum(devs > AUX_BAND)),
            int(np.sum(devs > AUX_HARD)),
            float(np.max(devs)), med)


def mirror_world_row(E, yn):
    """one world row of the sealed mirror clause: pair via
    positions, rest-block top, finite-order mirror rho_32;
    consumes the kernel Gram + positions only."""
    i1, i2 = PX.pair_select(yn)
    n = E.shape[0]
    rest = [k for k in range(n) if k != i1 and k != i2]
    D = E[np.ix_(rest, rest)]
    lam_rest = float(np.linalg.eigvalsh(D)[-1])
    c = float(E[i1, i2])
    with np.errstate(over="ignore", invalid="ignore"):
        rho = GR.mirror_profile(D, E[i1, rest], E[i2, rest], c,
                                (MIRROR_K,))[MIRROR_K]
    return lam_rest, rho, c


# ============== must-fail mutants
def mutant_identity_flip(pp, qq, m2p):
    """m1 MUST-FAIL: the one-line identity with the WRONG
    normalization m2' (p'+q'+m2') -- the deficit enters the second
    factor SIGNED; must break the exact identity loudly."""
    return m2p * (pp + qq + m2p)


def mutant_bar_posthoc(resid_true):
    """m2 MUST-FAIL: the closure bar re-picked AFTER SIGHT of the
    measured residual -- consumes the withheld residual;
    AST-FLAGGED, and the toy value differs from CLOSURE_BAR."""
    return resid_true * 1.2


def mutant_alpha_circular(margin_col_true, lnN):
    """m3 MUST-FAIL: 'alpha' read circularly off the withheld
    margin column instead of the identity slopes -- AST-FLAGGED;
    the real alpha_id constructor consumes fitted dressed-column
    slopes only."""
    x = np.asarray(lnN, float)
    y = np.log(np.asarray(margin_col_true, float))
    return -(y[-1] - y[0]) / (x[-1] - x[0])


def mutant_factor_readback():
    """m4 MUST-FAIL: a 'dictionary factor' read back from the
    withheld lambda record -- the scope audit must FLAG this."""
    return 1.0 - REC_LAM


def mutant_mirrorbar_posthoc(rho_col_true):
    """m5 MUST-FAIL: the mirror-live bar re-picked AFTER SIGHT to
    sit between the seen live and dead |rho - 1| columns --
    consumes the withheld column; AST-FLAGGED."""
    devs = sorted(abs(r - 1.0) for r in rho_col_true)
    return 0.5 * (devs[0] + devs[-1])


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("delta_alpha_closure_probe -- PRIME.LSTAR."
          "DELTA_ALPHA_CLOSURE.01 (round 347)")
    print("SPEC_SHA %s   (r342 PX %s / r343 PC3 %s / r345 GR %s / "
          "r330 DSW %s)"
          % (SPEC_SHA[:16], PX.SPEC_SHA[:16], PC3.SPEC_SHA[:16],
             GR.SPEC_SHA[:16], DSW.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 block; ladder, twin, fits, "
                        "protocols, closures, worlds, adjudication "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and PC3.SPEC_SHA.startswith(PC3_SHA_PREFIX)
              and GR.SPEC_SHA.startswith(GR_SHA_PREFIX)
              and DSW.SPEC_SHA.startswith(DSW_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: the r342/r343/r345/r330 "
          "machinery imported verbatim (SPEC_SHA %s == %s*, %s == "
          "%s*, %s == %s*, %s == %s*), the one-line identity with "
          "its Fractions toy, the four closures at CLOSURE_BAR "
          "%.1f, the bridge clause (dev %.2f / slope %.2f), the "
          "AUX bands (%.1f dec, out <= %d, hard %.2f), the "
          "delta/c-law re-gates, the dressed-dictionary double "
          "adjudication, the sealed mirror world rule (live bar "
          "%.1f at K = %d), the DISCLOSED PRIORS (margin %.3f, c "
          "%.3f, cpc %.3f, cp %.3f), every bar/tolerance, the "
          "mutants and the verdict form; pre-spec scoping s1/s2 "
          "disclosed in the spec (four printed sample rungs + the "
          "w9 DIR/ABS construction); the STOP list forbids any L* "
          "claim and any certificate reading beyond the sealed "
          "census"
          % (PX.SPEC_SHA[:8], PX_SHA_PREFIX, PC3.SPEC_SHA[:8],
             PC3_SHA_PREFIX, GR.SPEC_SHA[:8], GR_SHA_PREFIX,
             DSW.SPEC_SHA[:8], DSW_SHA_PREFIX, CLOSURE_BAR,
             BRIDGE_DEV_BAR, BRIDGE_SLOPE_BAR, AUX_BAND,
             AUX_OUT_MAX, AUX_HARD, MIRROR_LIVE_BAR, MIRROR_K,
             FIT_ANCH["margin"], FIT_ANCH["c"], FIT_ANCH["cpc"],
             FIT_ANCH["cp"]))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m2 = scope_audit("mutant_bar_posthoc")
    hits_m3 = scope_audit("mutant_alpha_circular")
    hits_m4 = scope_audit("mutant_factor_readback")
    hits_m5 = scope_audit("mutant_mirrorbar_posthoc")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m2) and bool(hits_m3) and bool(hits_m4)
          and bool(hits_m5),
          "the %d module-own constructors consume kernel Gram / "
          "spectrum / weight / position arrays and measured "
          "columns ONLY (%s); fragment audit (no fit primitives "
          "beyond the imported r286 Theil-Sen + r345 protocol): "
          "%s; m2 FLAGGED (%s); m3 FLAGGED (%s); m4 FLAGGED (%s); "
          "m5 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS",
             hits_m4[0] if hits_m4 else "MISS",
             hits_m5[0] if hits_m5 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- FRACTIONS IDENTITY + CLOSURE FAMILY + "
            "PROTOCOLS")
    # exact Fractions one-line identity on the 3x3 hand toy
    a11, a12, a22 = Fr(1, 4), Fr(1, 8), Fr(1, 2)
    c1_, c2_, dd_ = Fr(1, 16), Fr(1, 32), Fr(1, 8)
    inv_ = 1 / (1 - dd_)
    d1p_ex = a11 + c1_ * c1_ * inv_
    d2p_ex = a22 + c2_ * c2_ * inv_
    cp_ex = a12 + c1_ * c2_ * inv_
    pp_ex = 1 - d1p_ex
    qq_ex = 1 - d2p_ex
    det_ex = (1 - d1p_ex) * (1 - d2p_ex) - cp_ex * cp_ex
    ok_fr = (pp_ex * qq_ex - cp_ex * cp_ex == det_ex)
    # f64 route on the same toy: m2'(s - m2') == p'q' - c'^2
    d1f, d2f, cf = float(d1p_ex), float(d2p_ex), float(cp_ex)
    lam_p = PX.pair_eigs(d1f, d2f, cf)[0]
    m2f = 1.0 - lam_p
    sf = (1.0 - d1f) + (1.0 - d2f)
    lhs_t = m2f * (sf - m2f)
    rhs_t = (1.0 - d1f) * (1.0 - d2f) - cf * cf
    dev_t = abs(lhs_t - rhs_t) / abs(rhs_t)
    _pt, _qt, r_t = PX.det_reserve(d1f, d2f, cf)
    dev_rt = abs(cf * cf - (1.0 - r_t) * (1.0 - d1f)
                 * (1.0 - d2f)) / ((1.0 - d1f) * (1.0 - d2f))
    check("G10-toy-fractions-identity", ok_fr and dev_t <= TOY_TOL
          and dev_rt <= TOY_TOL,
          "THE ONE-LINE IDENTITY on the 3x3 hand toy: det(I-A') "
          "== p'q' - c'^2 EXACT in Fractions (%s); f64 route: "
          "m2'(p'+q'-m2') == p'q' - c'^2 (dev %.1e) and c'^2 == "
          "(1-r'_det) p'q' (dev %.1e) -- both eigenvalue deficits "
          "of the dressed 2x2 are the roots of t^2 - (p'+q') t + "
          "(p'q' - c'^2): the identity is exact algebra, not an "
          "approximation" % (str(det_ex), dev_t, dev_rt))
    # closure toy: exact power-law family through the identity
    Nt = np.array([200.0 * (1.25 ** k) for k in range(20)])
    pp_t = 0.8e-3 * (Nt / 200.0) ** (-TOY_ALPHA)
    qq_t = 1.3e-3 * (Nt / 200.0) ** (-TOY_ALPHA)
    cp_t = np.sqrt((1.0 - TOY_RP) * pp_t * qq_t)
    s_t = pp_t + qq_t
    m2_t = 0.5 * (s_t - np.sqrt(s_t * s_t
                                - 4.0 * pp_t * qq_t * TOY_RP))
    marg_t = m2_t / TOY_BRIDGE
    lnNt = np.log(Nt)
    sl = {}
    for nm, col in (("pp", pp_t), ("qq", qq_t),
                    ("rp", np.full(20, TOY_RP)),
                    ("sp", s_t - m2_t),
                    ("br", m2_t / marg_t), ("m2", m2_t),
                    ("mg", marg_t), ("cp", cp_t)):
        sl[nm] = float(LM.ts_fit(lnNt, np.log(col))[1])
    a_id_t = alpha_from_slopes(sl["pp"], sl["qq"], sl["rp"],
                               sl["sp"], sl["br"])
    ok_c1t = abs(a_id_t - (-sl["mg"])) <= C1_TOY_BAR
    ok_c4t = abs((-sl["mg"]) - (2.0 * (-sl["cp"]) - (-sl["pp"])
                                - (-sl["qq"]) + (-sl["cp"]))) \
        <= 1.0   # census sanity only: symmetric family
    id_dev_t = max(abs(m2_t[k] * (s_t[k] - m2_t[k])
                       - (pp_t[k] * qq_t[k] - cp_t[k] ** 2))
                   / (pp_t[k] * qq_t[k] + cp_t[k] ** 2)
                   for k in range(20))
    check("G11-toy-closure-family", ok_c1t and ok_c4t
          and id_dev_t <= 1e-12,
          "CLOSURE TOY (exact N^-%.1f family, r' = %.1f flat, "
          "bridge %.3f): the identity holds per row (max dev "
          "%.1e) and the identity-route exponent alpha_id = %.6f "
          "== -slope(margin) = %.6f (dev %.1e, bar %.0e) -- the "
          "accounting instrument recovers the planted exponent "
          "exactly" % (TOY_ALPHA, TOY_RP, TOY_BRIDGE, id_dev_t,
                       a_id_t, -sl["mg"],
                       abs(a_id_t - (-sl["mg"])), C1_TOY_BAR))
    # decay-law instrument toy
    kk = np.arange(25)
    lnS = np.log(300.0 * 1.1 ** kk)
    scat = math.log(2.0) * np.sin(7.0 * kk)
    e3p_t = [(float(lnS[-1] + 0.3), float(np.log(0.3)
                                          - 3.0 * (lnS[-1] + 0.3)
                                          + 0.1))] * 12
    e4p_t = [(float(lnS[-1] + 0.5), float(np.log(0.3)
                                          - 3.0 * (lnS[-1] + 0.5)
                                          - 0.2))] * 6
    dl3 = decay_law(lnS, np.log(0.3) - 3.0 * lnS + scat,
                    e3p_t, e4p_t)
    dl_flat = decay_law(lnS, np.log(0.3) + scat, [], [])
    ok_dl = (abs(dl3["slope"] + 3.0) <= 0.2
             and dl3["e3_in"] == 12 and dl3["e4_low"] == 0
             and (-dl_flat["slope"]) < DELTA_MIN)
    check("G12-toy-decay-law", ok_dl,
          "DECAY-LAW INSTRUMENT: synthetic N^-3 with x2 scatter "
          "fits slope %.3f, EXT3 12/12 in band, EXT4 n_low 0; the "
          "flat column returns delta %.3f < %.1f (the DELTA "
          "clause refuses it) -- the instrument separates decays "
          "from flats" % (dl3["slope"], -dl_flat["slope"],
                          DELTA_MIN))
    # r345 curvflat protocol re-gate on its own toys
    coh_toy = [("c%d" % j, list(range(5 * j, 5 * j + 5)))
               for j in range(5)]
    fitm = [True] * 25
    p_flat = GR.curvflat_protocol(lnS, np.log(0.30) + scat, fitm,
                                  coh_toy)
    p_dec3 = GR.curvflat_protocol(lnS, np.log(0.30) - 3.0 * lnS
                                  + scat, fitm, coh_toy)
    check("G13-toy-curvflat-regate", p_flat["ok"]
          and not p_dec3["ok"],
          "the r345 CURVATURE-HONEST protocol imported verbatim: "
          "flat column with deterministic x2 scatter PASSES "
          "(slope %+.3f, CI [%+.2f, %+.2f]); N^-3 with the same "
          "scatter is CAUGHT (slope %+.3f) -- the sealed protocol "
          "constants live in the r345 module, gated by SPEC_SHA"
          % (p_flat["slope"], p_flat["qlo"], p_flat["qhi"],
             p_dec3["slope"]))
    S_toy = np.array([300.0 * (1.1 ** k) for k in range(25)])
    y_flat = np.log(0.30) + 0.0 * np.log(S_toy)
    ft = LM.ts_fit(np.log(S_toy), y_flat)
    ft_short = LM.ts_fit(np.arange(8.0), np.arange(8.0))
    check("G14-toy-fit", (not isinstance(ft[0], str))
          and abs(ft[1]) <= 1e-12
          and ft_short[0] == "SHORT_LADDER",
          "r286 Theil-Sen imported verbatim: synthetic FLAT "
          "column slope %.1e == 0; the guard REFUSES 8 points "
          "(%s)" % (abs(ft[1]), str(ft_short)))

    # ---------------- S2 w9 flagship
    section("S2  W9 -- RECORDS + DRESSED ANCHORS + IDENTITY LIVE "
            "+ MIRROR")
    R9 = PX.build_rung(MAIN_KZ)
    C9 = closure_cols(R9)
    lam185, _B185 = V.lam_max_at(R9["mz"], REC_NW + 1)
    ok_rec = (R9["S"] == REC_S and R9["Sm"] == REC_SM
              and R9["Nw"] == REC_NW
              and abs(R9["lam"] - REC_LAM) <= 1e-6
              and abs(lam185 - REC_LAM_NEXT) <= 1e-6
              and abs(R9["margin"] / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL)
    check("G20-w9-records", ok_rec,
          "w9: S = %d (nu %d), N_w = %d, lambda_max = %.8f "
          "(record %.8f), margin %.4e (record %.4e), lambda at "
          "185 = %.8f > 1 -- the document route reproduced"
          % (R9["S"], R9["Sm"], R9["Nw"], R9["lam"], REC_LAM,
             R9["margin"], REC_MARGIN, lam185))
    A = W9_ANCH
    X9 = PC3.extend_rung(R9)
    ok_anch = (abs(R9["d1p"] / A["d1p"] - 1.0) <= 1e-5
               and abs(R9["d2p"] / A["d2p"] - 1.0) <= 1e-5
               and abs(R9["cp"] / A["cp"] - 1.0) <= 1e-3
               and abs(R9["rdetp"] / A["rdetp"] - 1.0) <= 1e-3
               and abs(R9["lam_rest"] - A["lam_rest"]) <= 1e-5
               and abs(C9["ppr"] / A["ppr"] - 1.0) <= 1e-3
               and abs(C9["qpr"] / A["qpr"] - 1.0) <= 1e-3
               and abs(C9["m2p"] / A["m2p"] - 1.0) <= 1e-3
               and abs(C9["bridge"] - A["bridge"]) <= 5e-3
               and abs(C9["cpc"] / A["cpc"] - 1.0) <= 1e-3
               and abs(X9["g21"] - A["g21"]) <= 0.01
               and X9["k_res"] == A["kres"])
    check("G21-w9-dressed-anchors", ok_anch,
          "LEG 0 BIT-NEAR: dressed (d1', d2', c') = (%.6f, %.6f, "
          "%.6e) == r343; closure coordinates p' %.4e, q' %.4e, "
          "m2' %.4e, m2'/margin %.4f (scoped %.4f), c'/c %.4e "
          "(r345 %.4e), r'_det %.6f, lambda_rest %.6f; g21 %.4f "
          "(== %.3f), K_res %d -- the r347 coordinates start "
          "exactly where r342/r343/r345 left them"
          % (R9["d1p"], R9["d2p"], R9["cp"], C9["ppr"], C9["qpr"],
             C9["m2p"], C9["bridge"], A["bridge"], C9["cpc"],
             A["cpc"], R9["rdetp"], R9["lam_rest"], X9["g21"],
             A["g21"], X9["k_res"]))
    check("G22-w9-identity-live", C9["dev_id"] <= ID_BAR
          and C9["dev_rdef"] <= RDEF_BAR,
          "THE ONE-LINE IDENTITY LIVE: m2'(p'+q'-m2') = %.6e == "
          "p'q' - c'^2 = %.6e (residual %.1e at the backward-"
          "error scale, bar %.0e); definitional ward c'^2 == "
          "(1 - r'_det) p'q' dev %.1e (bar %.0e) -- the dressed "
          "second determinant condition IS the reserve times the "
          "diagonal deficits, exactly"
          % (C9["m2p"] * C9["spr"],
             C9["ppr"] * C9["qpr"] - C9["cpr"] ** 2, C9["dev_id"],
             ID_BAR, C9["dev_rdef"], RDEF_BAR))
    lam_r9, rho9, _c9 = mirror_world_row(X9["E"],
                                         np.asarray(R9["mz"]["yn"],
                                                    float))
    ok_mir = (abs(lam_r9 - A["lam_rest"]) <= 1e-5
              and abs(rho9 - A["rho32"]) <= 5e-3
              and abs(C9["fp"] / A["fp"] - 1.0) <= 1e-2
              and abs(C9["fq"] / A["fq"] - 1.0) <= 1e-2
              and abs(C9["pqr"] - A["pqr"]) <= 5e-3
              and abs(C9["spc"] - A["spc"]) <= 0.02)
    check("G23-w9-mirror-and-factors", ok_mir,
          "MIRROR + FACTOR ANCHORS: rho_32 = %.4f (r345 %.4f) "
          "with lambda_rest %.6f < 1 (the mirror exists); dressed "
          "dictionary factors p'/p = %.4e (scoped %.4e), q'/q = "
          "%.4e (scoped %.4e); aspects p'/q' = %.4f, (p'+q')/c' "
          "= %.4f -- the Leg C/D coordinates anchored bit-near"
          % (rho9, A["rho32"], lam_r9, C9["fp"], A["fp"],
             C9["fq"], A["fq"], C9["pqr"], C9["spc"]))

    # ---------------- S3 the ladder
    section("S3  LEG A/B -- THE LADDER (42 + 15 + 12 EXT3 + 6 "
            "EXT4)")
    if smoke:
        for g in ("G30-ladder-census", "G31-ladder-identities",
                  "G32-cohort-anchors"):
            check(g, True, "SMOKE: skipped")
        ROWS, CT = {9: R9}, {9: C9}
        core_kzs, ext_kzs, ext3_kzs, ext4_kzs = [9], [], [], []
        excl = []
    else:
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in LM.ext_rule()[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ext4_kzs = list(EXT4_KZ_B + EXT4_KZ_A)
        ROWS, CT = {}, {}
        print("    %-5s %-5s %-5s %-5s | %-10s %-7s | %-10s %-10s "
              "%-10s | %-7s %-6s | %-8s | %-9s %-9s %-9s"
              % ("kz", "z", "S-", "N_w", "margin", "m2'/mg", "p'",
                 "q'", "c'", "p'/q'", "s/c'", "r'_det", "c'/c",
                 "p'/p", "q'/q"))
        neg_rows = []
        for kz in core_kzs + ext_kzs + ext3_kzs + ext4_kzs:
            R = R9 if kz == MAIN_KZ else PX.build_rung(kz)
            C = C9 if kz == MAIN_KZ else closure_cols(R)
            ROWS[kz], CT[kz] = R, C
            if R["margin"] <= 0:
                neg_rows.append(kz)
            print("    %-5d %-5d %-5d %-5d | %.4e %7.4f | %.4e "
                  "%.4e %.4e | %7.4f %6.3f | %8.4f | %.3e %.3e "
                  "%.3e"
                  % (kz, R["z"], R["Sm"], R["Nw"], R["margin"],
                     C["bridge"], C["ppr"], C["qpr"], C["cpr"],
                     C["pqr"], C["spc"], R["rdetp"], C["cpc"],
                     C["fp"], C["fq"]), flush=True)
        excl = list(neg_rows)
        ok_cen = (len(core_kzs) == 42
                  and all(EXT3_NW_MIN <= ROWS[k]["Nw"]
                          <= EXT3_NW_MAX for k in ext3_kzs)
                  and all(EXT4_NW_MIN <= ROWS[k]["Nw"]
                          <= EXT4_NW_MAX for k in ext4_kzs))
        check("G30-ladder-census", ok_cen and not neg_rows,
              "42 core + 15 r286 extension + 12 EXT3 (N_w %d..%d) "
              "+ 6 EXT4 (N_w %d..%d, the r343 sealed selections "
              "adopted AS-IS); every f64 margin positive "
              "(contingency rows: %s)"
              % (EXT3_NW_MIN, EXT3_NW_MAX, EXT4_NW_MIN,
                 EXT4_NW_MAX,
                 str(neg_rows) if neg_rows else "none"))
        all_kz = core_kzs + ext_kzs + ext3_kzs + ext4_kzs
        kz57 = core_kzs + ext_kzs
        max_id = max(CT[k]["dev_id"] for k in all_kz)
        max_rd = max(CT[k]["dev_rdef"] for k in all_kz)
        ok_id = all(CT[k]["dev_id"] <= ID_BAR
                    and CT[k]["dev_rdef"] <= RDEF_BAR
                    and ROWS[k]["det_dev"] <= 1e-12
                    and ROWS[k]["schur_dev"] <= 1e-6
                    for k in all_kz)
        check("G31-ladder-identities", ok_id,
              "THE ONE-LINE IDENTITY on all %d rows: "
              "m2'(p'+q'-m2') == p'q' - c'^2 at the backward-"
              "error scale (max residual %.1e, bar %.0e; the "
              "depth conditioning as scoped) AND c'^2 == "
              "(1-r'_det) p'q' (max %.1e, bar %.0e); r342 "
              "det/Schur identities re-gated; lambda_rest < 1 on "
              "%s" % (len(all_kz), max_id, ID_BAR, max_rd,
                      RDEF_BAR,
                      all(ROWS[k]["lam_rest"] < 1.0
                          for k in all_kz)))

        def med(vals):
            return float(np.median(np.asarray(vals, float)))

        fit_kz = [k for k in kz57 if k not in excl]
        med_br = med([CT[k]["bridge"] for k in fit_kz])
        med_rhop = med([CT[k]["rhop"] for k in fit_kz])
        min_rp_kz = min(fit_kz, key=lambda k: ROWS[k]["rdetp"])
        max_rp_kz = max(fit_kz, key=lambda k: ROWS[k]["rdetp"])
        ok_coh = (abs(med_br - MED_ANCH["bridge"]) <= 5e-3
                  and abs(med_rhop - MED_ANCH["rhop"]) <= 0.01
                  and abs(ROWS[56]["rdetp"] - KZ56_RDETP) <= 2e-3
                  and min_rp_kz == SPAN_ANCH["min_kz"]
                  and max_rp_kz == SPAN_ANCH["max_kz"]
                  and abs(ROWS[min_rp_kz]["rdetp"]
                          - SPAN_ANCH["min_rdetp"]) <= 5e-3
                  and abs(ROWS[max_rp_kz]["rdetp"]
                          - SPAN_ANCH["max_rdetp"]) <= 5e-3
                  and all(abs(CT[k]["bridge"]
                              - SAMPLE_ANCH[k]["bridge"]) <= 5e-3
                          and abs(CT[k]["pqr"]
                                  - SAMPLE_ANCH[k]["pqr"]) <= 5e-3
                          for k in SAMPLE_ANCH))
        check("G32-cohort-anchors", ok_coh,
              "LEG 0 COHORT ANCHORS: median m2'/margin %.4f (== "
              "%.4f r343), median rho' %.4f (== %.3f); kz56 "
              "r'_det %.4f; span kz%d %.4f / kz%d %.4f == r345; "
              "scoped sample bridges/aspects (kz44/56/130) all "
              "bit-near -- Leg 0 closed"
              % (med_br, MED_ANCH["bridge"], med_rhop,
                 MED_ANCH["rhop"], ROWS[56]["rdetp"], min_rp_kz,
                 ROWS[min_rp_kz]["rdetp"], max_rp_kz,
                 ROWS[max_rp_kz]["rdetp"]))

    # ---------------- S4 twin
    section("S4  TWIN WARD")
    if smoke:
        check("G40-twin", True, "SMOKE: skipped")
        mzT = None
    else:
        uu9c, mm9c = TR.base_comb(9)
        mzD = TR.build_world(9, uu9c, mm9c)
        mz9 = R9["mz"]
        ok_dose0 = (np.array_equal(mzD["xp"], mz9["xp"])
                    and np.array_equal(mzD["wp"], mz9["wp"])
                    and np.array_equal(mzD["yn"], mz9["yn"])
                    and np.array_equal(mzD["vn"], mz9["vn"]))
        gaps9 = MF.local_gaps(uu9c)
        u2c, m2c, _dens, _du = AKD.twin_rational(uu9c, mm9c,
                                                 gaps9, mz9["D"],
                                                 TWIN_TOL)
        mzT = TR.build_world(9, u2c, m2c)
        aT, bT, h0T = V.mu_chain(mzT["xp"], mzT["wp"], mzT["Nw"])
        BT = V.b_matrix(aT, bT, h0T, mzT["yn"], mzT["vn"],
                        mzT["Nw"])
        ET = BT @ BT.T
        t1_, t2_ = PX.pair_select(mzT["yn"])
        AdT, lrT, _s1, _s2 = PX.schur_dress(ET, t1_, t2_)
        d1T, d2T = float(AdT[0, 0]), float(AdT[1, 1])
        cT = float(0.5 * (AdT[0, 1] + AdT[1, 0]))
        m2T = 1.0 - PX.pair_eigs(d1T, d2T, cT)[0]
        rT = PX.det_reserve(d1T, d2T, cT)[2]
        devT = dict(
            d=max(abs(d1T - R9["d1p"]) / R9["d1p"],
                  abs(d2T - R9["d2p"]) / R9["d2p"],
                  abs(cT - R9["cp"]) / abs(R9["cp"])),
            m2p=abs(m2T - C9["m2p"]) / C9["m2p"],
            rdetp=abs(rT - R9["rdetp"]) / R9["rdetp"],
            lr=abs(lrT - R9["lam_rest"]) / R9["lam_rest"])
        ok_twin = ok_dose0 and all(v <= TWIN_BAR
                                   for v in devT.values())
        check("G40-twin", ok_twin,
              "RATIONAL TWIN at tol %.0e (dose-zero identity "
              "BITWISE %s): dressed scalars dev <= %.1e, m2' dev "
              "%.1e, r'_det dev %.1e, lambda_rest dev %.1e (bar "
              "%.0e) -- the closure coordinates are twin-stable"
              % (TWIN_TOL, ok_dose0, devT["d"], devT["m2p"],
                 devT["rdetp"], devT["lr"], TWIN_BAR))

    # ---------------- S5 fits + protocols + closures
    section("S5  LEG B/C -- SEALED FITS + BRIDGE + FLATS + LAWS + "
            "THE CLOSURES")
    if smoke:
        for g in ("G50-fit-anchors", "G51-dressed-fits",
                  "G52-bridge", "G53-flats", "G54-laws",
                  "G55-closures", "G56-dressed-dictionary",
                  "G57-source-dictionary"):
            check(g, True, "SMOKE: skipped")
        closures = {}
        bridge_ok = flats_ok = laws_ok = None
        dress_tag = ""
        exp_txt = ""
    else:
        lnN57 = np.log(np.array([ROWS[k]["Nw"] for k in fit_kz],
                                float))
        getters = {
            "margin": lambda k: ROWS[k]["margin"],
            "c": lambda k: abs(ROWS[k]["c"]),
            "p": lambda k: ROWS[k]["p"],
            "q": lambda k: ROWS[k]["q"],
            "rdetp": lambda k: ROWS[k]["rdetp"],
            "cpc": lambda k: CT[k]["cpc"],
            "cp": lambda k: abs(CT[k]["cpr"]),
            "ppr": lambda k: CT[k]["ppr"],
            "qpr": lambda k: CT[k]["qpr"],
            "m2p": lambda k: CT[k]["m2p"],
            "spr": lambda k: CT[k]["spr"],
            "bridge": lambda k: CT[k]["bridge"],
            "pqr": lambda k: CT[k]["pqr"],
            "fp": lambda k: CT[k]["fp"],
            "fq": lambda k: CT[k]["fq"],
        }
        laws = {}
        for nm, get in getters.items():
            e3p = [(math.log(ROWS[k]["Nw"]), math.log(get(k)))
                   for k in ext3_kzs]
            e4p = [(math.log(ROWS[k]["Nw"]), math.log(get(k)))
                   for k in ext4_kzs]
            laws[nm] = decay_law(lnN57,
                                 np.log([get(k) for k in fit_kz]),
                                 e3p, e4p)
        ok_fit = (all(abs(laws[nm]["slope"] - FIT_ANCH[nm])
                      <= FIT_ANCH_TOL for nm in FIT_ANCH)
                  and all(abs(laws[nm]["curv"] - CURV_ANCH[nm])
                          <= CURV_ANCH_TOL for nm in CURV_ANCH))
        check("G50-fit-anchors", ok_fit,
              "LEG 0 FIT ANCHORS on the 57 (slope | record): "
              "margin %.3f | %.3f, c %.3f | %.3f, p %.3f | %.3f, "
              "q %.3f | %.3f, rdetp %+.3f | %+.3f, |c'/c| %.3f | "
              "%.3f, |c'| %.3f | %.3f (tol %.2f); CURVATURE "
              "ANCHORS: cpc %+.3f | %+.3f, rdetp %+.3f | %+.3f, "
              "margin %+.3f | %+.3f, c %+.3f | %+.3f (tol %.2f)"
              % (laws["margin"]["slope"], FIT_ANCH["margin"],
                 laws["c"]["slope"], FIT_ANCH["c"],
                 laws["p"]["slope"], FIT_ANCH["p"],
                 laws["q"]["slope"], FIT_ANCH["q"],
                 laws["rdetp"]["slope"], FIT_ANCH["rdetp"],
                 laws["cpc"]["slope"], FIT_ANCH["cpc"],
                 laws["cp"]["slope"], FIT_ANCH["cp"],
                 FIT_ANCH_TOL, laws["cpc"]["curv"],
                 CURV_ANCH["cpc"], laws["rdetp"]["curv"],
                 CURV_ANCH["rdetp"], laws["margin"]["curv"],
                 CURV_ANCH["margin"], laws["c"]["curv"],
                 CURV_ANCH["c"], CURV_ANCH_TOL))
        exp_txt = "; ".join(
            "%s %.3f (curv %+.3f, EXT3 %d/12 low %d, EXT4 %d/6 "
            "low %d)"
            % (nm, laws[nm]["slope"], laws[nm]["curv"],
               laws[nm]["e3_in"], laws[nm]["e3_low"],
               laws[nm]["e4_in"], laws[nm]["e4_low"])
            for nm in ("ppr", "qpr", "cp", "m2p", "spr", "bridge",
                       "pqr", "fp", "fq"))
        check("G51-dressed-fits", True,
              "THE SEALED DRESSED FITS (first evaluation, VOR the "
              "record frozen): %s -- every band miss is printed; "
              "n_low counts adjudicate nothing here (the closure "
              "gates are C1-C4 + the support clauses)" % exp_txt)
        # bridge clause
        br_dev, br_slope, _brr = bridge_stats(
            [CT[k]["m2p"] for k in all_kz if k not in excl],
            [ROWS[k]["margin"] for k in all_kz if k not in excl],
            [math.log(ROWS[k]["Nw"]) for k in all_kz
             if k not in excl])
        bridge_ok = (br_dev <= BRIDGE_DEV_BAR
                     and abs(br_slope) <= BRIDGE_SLOPE_BAR)
        check("G52-bridge", True,
              "THE BRIDGE CLAUSE m2' == margin on all %d "
              "arbitrated rows: max |m2'/margin - 1| = %.4f (bar "
              "%.2f), ratio slope %+.4f (bar %.2f) => %s -- the "
              "dressed second determinant %s the margin, "
              "protocol-graded"
              % (len(all_kz) - len(excl), br_dev, BRIDGE_DEV_BAR,
                 br_slope, BRIDGE_SLOPE_BAR,
                 "HOLDS" if bridge_ok else "FAILS",
                 "IS" if bridge_ok else "is NOT"))
        # flats: r'_det re-gate under the r345 protocol + AUX bands
        arb_kz = [k for k in all_kz if k not in excl]
        lnN_all = np.log(np.array([ROWS[k]["Nw"] for k in arb_kz],
                                  float))
        fitm = [k in set(fit_kz) for k in arb_kz]
        cohorts = [
            ("core42", [i for i, k in enumerate(arb_kz)
                        if k in set(core_kzs)]),
            ("ext15", [i for i, k in enumerate(arb_kz)
                       if k in set(ext_kzs)]),
            ("ext3B", [i for i, k in enumerate(arb_kz)
                       if k in set(EXT3_KZ_B)]),
            ("ext3A", [i for i, k in enumerate(arb_kz)
                       if k in set(EXT3_KZ_A)]),
            ("ext4", [i for i, k in enumerate(arb_kz)
                      if k in set(ext4_kzs)]),
        ]
        flat_rd = GR.curvflat_protocol(
            lnN_all, np.log([ROWS[k]["rdetp"] for k in arb_kz]),
            fitm, cohorts)
        aux_pqr = aux_band([CT[k]["pqr"] for k in fit_kz],
                           [CT[k]["pqr"] for k in arb_kz])
        aux_spc = aux_band([CT[k]["spc"] for k in fit_kz],
                           [CT[k]["spc"] for k in arb_kz])
        aux_ok = (aux_pqr[0] <= AUX_OUT_MAX and aux_pqr[1] == 0
                  and aux_spc[0] <= AUX_OUT_MAX
                  and aux_spc[1] == 0)
        flats_ok = flat_rd["ok"] and aux_ok
        check("G53-flats", True,
              "CURV_FLAT(r'_det) re-gate (r345 protocol "
              "verbatim): %s (CH1 %d out/%d hard, max |dev| %.3f "
              "dec; CH2 slope %+.3f CI [%+.3f, %+.3f]; CH3 drift "
              "%.3f); AUX ASPECT BANDS (%.1f dec around the "
              "57-median): p'/q' %d out/%d hard (max %.3f dec, "
              "med %.4f), s/c' %d out/%d hard (max %.3f dec, med "
              "%.4f) => aspects %s -- the flat-aspect step that "
              "turns the identity into the one line"
              % ("PASS" if flat_rd["ok"] else "FAIL",
                 flat_rd["n_out"], flat_rd["hard"],
                 flat_rd["max_dev"], flat_rd["slope"],
                 flat_rd["qlo"], flat_rd["qhi"], flat_rd["drift"],
                 AUX_BAND, aux_pqr[0], aux_pqr[1], aux_pqr[2],
                 aux_pqr[3], aux_spc[0], aux_spc[1], aux_spc[2],
                 aux_spc[3], "HOLD" if aux_ok else "BREAK"))
        # law re-gates
        delta = -laws["cpc"]["slope"]
        dlaw_ok = (abs(laws["cpc"]["curv"]) <= DEC_CURV_BAR
                   and laws["cpc"]["e3_in"] >= DEC_EXT3_MIN
                   and laws["cpc"]["e4_low"] <= DEC_EXT4_LOW
                   and delta >= DELTA_MIN)
        claw_ok = (abs(laws["c"]["curv"]) <= DEC_CURV_BAR
                   and laws["c"]["e3_in"] >= C_EXT3_MIN)
        laws_ok = dlaw_ok and claw_ok
        check("G54-laws", True,
              "LAW RE-GATES: the r345 CANCELLATION LAW on |c'/c| "
              "(delta %.3f, curv %+.3f, EXT3 %d/12 low %d, EXT4 "
              "%d/6 low %d) => %s; the r342 c-LAW (curv %+.3f, "
              "EXT3 %d/12) => %s -- both inputs of the one line "
              "carry their own sealed meters"
              % (delta, laws["cpc"]["curv"], laws["cpc"]["e3_in"],
                 laws["cpc"]["e3_low"], laws["cpc"]["e4_in"],
                 laws["cpc"]["e4_low"],
                 "RE-GATES" if dlaw_ok else "FAILS",
                 laws["c"]["curv"], laws["c"]["e3_in"],
                 "RE-GATES" if claw_ok else "FAILS"))
        # THE CLOSURES
        alpha_meas = -laws["margin"]["slope"]
        alpha_id = alpha_from_slopes(
            laws["ppr"]["slope"], laws["qpr"]["slope"],
            laws["rdetp"]["slope"], laws["spr"]["slope"],
            laws["bridge"]["slope"])
        a_c = -laws["c"]["slope"]
        alpha_line = a_c + delta
        closures = dict(
            C1=abs(alpha_meas - alpha_id),
            C2=abs(laws["margin"]["slope"]
                   - laws["m2p"]["slope"]),
            C3=abs(laws["cp"]["slope"]
                   - (laws["c"]["slope"]
                      + laws["cpc"]["slope"])),
            C4=abs(alpha_meas - alpha_line))
        cls_ok = {k: v <= CLOSURE_BAR
                  for k, v in closures.items()}
        sym_cen = (2.0 * laws["cp"]["slope"]
                   - laws["ppr"]["slope"] - laws["qpr"]["slope"])
        check("G55-closures", True,
              "THE FOUR SEALED CLOSURES (bar %.1f): C1 identity "
              "route |alpha_meas %.3f - alpha_id %.3f| = %.3f "
              "(%s); C2 margin bridge |%.3f - %.3f| = %.3f (%s); "
              "C3 cancellation bookkeeping |slope(c') %.3f - "
              "(slope(c) + slope(c'/c)) %.3f| = %.3f (%s); C4 "
              "THE ONE LINE |alpha %.3f - (a_c %.3f + delta "
              "%.3f) = %.3f| = %.3f (%s); symmetry census "
              "2 s_c' - s_p' - s_q' = %+.3f (~ slope(1-r') ~ 0)"
              % (CLOSURE_BAR, alpha_meas, alpha_id,
                 closures["C1"], cls_ok["C1"],
                 laws["margin"]["slope"], laws["m2p"]["slope"],
                 closures["C2"], cls_ok["C2"],
                 laws["cp"]["slope"],
                 laws["c"]["slope"] + laws["cpc"]["slope"],
                 closures["C3"], cls_ok["C3"], alpha_meas, a_c,
                 delta, alpha_line, closures["C4"], cls_ok["C4"],
                 sym_cen))
        # dressed dictionary adjudication
        flat_fp = GR.curvflat_protocol(
            lnN_all, np.log([CT[k]["fp"] for k in arb_kz]),
            fitm, cohorts)
        flat_fq = GR.curvflat_protocol(
            lnN_all, np.log([CT[k]["fq"] for k in arb_kz]),
            fitm, cohorts)
        delta_p = -laws["fp"]["slope"]
        delta_q = -laws["fq"]["slope"]
        go = flat_fp["ok"] and flat_fq["ok"]
        reslaw = (abs(laws["fp"]["curv"]) <= DEC_CURV_BAR
                  and laws["fp"]["e3_in"] >= DEC_EXT3_MIN
                  and laws["fp"]["e4_low"] <= DEC_EXT4_LOW
                  and delta_p >= DELTA_MIN
                  and abs(laws["fq"]["curv"]) <= DEC_CURV_BAR
                  and laws["fq"]["e3_in"] >= DEC_EXT3_MIN
                  and laws["fq"]["e4_low"] <= DEC_EXT4_LOW
                  and delta_q >= DELTA_MIN)
        if go:
            dress_tag = ("DRESSED_DICTIONARY_GO(both factor "
                         "columns flat -- p', q' inherit the "
                         "r342 dictionary slopes unchanged)")
        elif reslaw:
            dress_tag = ("DRESSED_RESIDUAL_LAW(delta_p %.3f, "
                         "delta_q %.3f; universality census "
                         "|delta_p - delta| %.3f, |delta_q - "
                         "delta| %.3f -- the dressed diagonals "
                         "inherit the bare dictionary slopes "
                         "MINUS a residual cancellation exponent)"
                         % (delta_p, delta_q,
                            abs(delta_p - delta),
                            abs(delta_q - delta)))
        else:
            dress_tag = ("DRESSED_FACTOR_CENSUS(fp slope %.3f "
                         "curv %+.3f EXT3 %d/12, fq slope %.3f "
                         "curv %+.3f EXT3 %d/12)"
                         % (laws["fp"]["slope"],
                            laws["fp"]["curv"],
                            laws["fp"]["e3_in"],
                            laws["fq"]["slope"],
                            laws["fq"]["curv"],
                            laws["fq"]["e3_in"]))
        check("G56-dressed-dictionary", True,
              "LEG C DOUBLE ADJUDICATION: flat protocol on p'/p "
              "%s (slope %+.3f, CI [%+.3f, %+.3f]) and q'/q %s "
              "(slope %+.3f, CI [%+.3f, %+.3f]); residual-law "
              "clauses %s => %s"
              % ("PASS" if flat_fp["ok"] else "FAIL",
                 flat_fp["slope"], flat_fp["qlo"], flat_fp["qhi"],
                 "PASS" if flat_fq["ok"] else "FAIL",
                 flat_fq["slope"], flat_fq["qlo"], flat_fq["qhi"],
                 reslaw, dress_tag))
        # source dictionary re-gate (r342 route verbatim)
        dev_dict = 0.0
        dev_v = 0.0
        for kz in SAMPLE_KZ:
            R = ROWS[kz]
            alpha_, M_, L_, D_, ka_, _dd, dA_, _dP = \
                PX.layer_split(kz)
            uu_ = np.asarray(V.U[:ka_], float)
            mm_ = np.asarray(V.W_VM[:ka_], float)
            for (ii, ff) in ((R["i1"], R["f1"]),
                             (R["i2"], R["f2"])):
                th = 2.0 * math.pi * ff / L_
                da_c, _da_p = PX.arch_dict_density(th, alpha_, D_)
                dev_dict = max(dev_dict,
                               abs(da_c - float(dA_[ff]))
                               / max(abs(float(dA_[ff])), 1e-300))
                vp, _a, _p = PX.v_predict(th, alpha_, M_, L_, D_,
                                          uu_, mm_)
                vt = float(R["mz"]["vn"][ii])
                dev_v = max(dev_v, abs(vp - vt) / vt)
        check("G57-source-dictionary", dev_dict <= DIGAMMA_BAR
              and dev_v <= V_BAR,
              "SOURCE SIDE RE-GATED (r342 route verbatim, six "
              "sample rungs): digamma dictionary at the pair "
              "folds max dev %.1e (bar %.2f), weight prediction "
              "max dev %.1e (bar %.2f) -- the weight side of the "
              "bare scalars stays closed-form, the kernel side "
              "census-grade (r342 negative #4, never upgraded)"
              % (dev_dict, DIGAMMA_BAR, dev_v, V_BAR))

    # ---------------- S6 worlds
    section("S6  LEG D/E -- THE WORLD CENSUS + THE MIRROR CLAUSE "
            "(8 WORLDS)")
    if smoke:
        for g in ("G60-controls", "G61-worlds"):
            check(g, True, "SMOKE: skipped")
        mirror_tag = ""
        world_txt = ""
    else:
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9["alpha"])
        comb_hl, _tag = PC.gen_model(PC.Grid(), "HL2", HL2_SEED)
        uD, wD, _nnD, _chD = DSW.dirichlet_comb(9)
        uA, wA, _nnA = DSW.dirichlet_abs_comb(9)
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx]
            / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))),
            ("HL2", dict(comb=comb_hl)),
            ("DIR", dict(comb=(uD, wD))),
            ("ABS", dict(comb=(uA, wA))))
        WORLDS = {}
        ok_ctrl = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            xu, wu, zones = BL.union_of_ctx(cctx)
            xs_z, ws_z, ys_z, vs_z = zones
            N_c = cctx["N"]
            if cn in CTRL_FLIPS or cn == "HL2":
                sg = BL.sign_chain_f64(xu, wu, N_c + EXT)[0]
                mc = next((n for n in range(len(sg))
                           if sg[n] < 0), None)
                flip = CTRL_FLIPS.get(cn, HL2_FLIP)
                ok_ctrl = ok_ctrl and (mc == flip)
            WORLDS[cn] = FC.world_from_arrays(
                cn, xs_z, ws_z, ys_z, vs_z, N_c, int(cctx["L"]))
        check("G60-controls", ok_ctrl,
              "EPST + SCR + SMOOTH + HL2 built verbatim through "
              "the r278/r280 channel at THEIR own N_w: minC == "
              "flips %s + HL2 %d; DIR/ABS built through the SAME "
              "channel from the r330 combs (verbatim import)"
              % (str(CTRL_FLIPS), HL2_FLIP))
        WORLDS["MAIN"] = FC.world_from_mz("MAIN", R9["mz"])
        WORLDS["TWIN"] = FC.world_from_mz("TWIN", mzT)
        cen = {}
        order = ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH", "HL2",
                 "DIR", "ABS")
        for wn in order:
            Wd = WORLDS[wn]
            Ew = Wd["B"] @ Wd["B"].T
            lam_rw, rho32w, _cw = mirror_world_row(Ew, Wd["yn"])
            exists = lam_rw < 1.0
            rtxt = ("%.4f" % rho32w if np.isfinite(rho32w)
                    and abs(rho32w) < 1e4
                    else ("NONFINITE" if not np.isfinite(rho32w)
                          else "%.3g" % rho32w))
            ki = None
            if wn in ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH",
                      "HL2"):
                ki, _loc, _nint, _kaps, ncf = \
                    FC.interval_census(Wd)
            cen[wn] = dict(lam=Wd["lam"], lam_rest=lam_rw,
                           rho32=rho32w, exists=exists, kint=ki,
                           ncf=(ncf if ki is not None else 0),
                           Sm=len(Wd["yn"]))
            info("%s: S_- %d, lambda %.6g, lambda_rest %.6g "
                 "(mirror %s), rho_32 %s%s"
                 % (wn, len(Wd["yn"]), Wd["lam"], lam_rw,
                    "EXISTS" if exists else "DIVERGES", rtxt,
                    (", kappa_int %.6g" % ki)
                    if ki is not None else ""))
        lr_sep = (all(cen[wn]["lam_rest"] >= 1.0
                      for wn in ("EPST", "SCR", "SMOOTH", "HL2"))
                  and all(cen[wn]["lam_rest"] < 1.0
                          for wn in ("MAIN", "TWIN")))
        ok_kint = (all(abs(cen[wn]["kint"] / KINT_REC[wn] - 1.0)
                       <= KINT_REC_TOL
                       for wn in ("EPST", "SCR", "SMOOTH",
                                  "HL2"))
                   and all(abs(cen[wn]["kint"] / KINT_LIVE_REC
                               - 1.0) <= KINT_LIVE_TOL
                           for wn in ("MAIN", "TWIN"))
                   and sum(cen[wn]["ncf"] for wn in cen) == 0)
        live_ok = all(cen[wn]["exists"]
                      and abs(cen[wn]["rho32"] - 1.0)
                      <= MIRROR_LIVE_BAR
                      for wn in ("MAIN", "TWIN"))
        dead_ok = all(not cen[wn]["exists"]
                      for wn in ("EPST", "SCR", "SMOOTH", "HL2"))
        dir_side = {wn: ("DEAD-side (lambda_rest %.3g >= 1, "
                         "series %s)"
                         % (cen[wn]["lam_rest"],
                            "NONFINITE"
                            if not np.isfinite(cen[wn]["rho32"])
                            else "explodes %.3g"
                            % cen[wn]["rho32"]))
                    if not cen[wn]["exists"] else
                    ("LIVE-side" if abs(cen[wn]["rho32"] - 1.0)
                     <= MIRROR_LIVE_BAR else
                     "EXISTS but |rho_32 - 1| %.3f > %.1f"
                     % (abs(cen[wn]["rho32"] - 1.0),
                        MIRROR_LIVE_BAR))
                    for wn in ("DIR", "ABS")}
        if live_ok and dead_ok:
            mirror_tag = ("MIRROR_WORLD_CLAUSE_SEALED(live 2/2 "
                          "|rho_32 - 1| <= %.1f, dead 4/4 "
                          "diverge; DIRICHLET typed: DIR %s, ABS "
                          "%s -- the r330 split restates "
                          "structurally in the E-Gram frame)"
                          % (MIRROR_LIVE_BAR, dir_side["DIR"],
                             dir_side["ABS"]))
        else:
            mirror_tag = ("MIRROR_WORLD_INCOMPLETE(live_ok %s, "
                          "dead_ok %s; DIR %s, ABS %s)"
                          % (live_ok, dead_ok, dir_side["DIR"],
                             dir_side["ABS"]))
        world_txt = ("lambda_rest separates 4/4 (re-gated); "
                     "kappa_int == records at %.0f%%; mirror "
                     "column: live %.4f/%.4f vs dead %s; DIR "
                     "lambda %.3g / lambda_rest %.3g, ABS %.3g / "
                     "%.3g"
                     % (100 * KINT_REC_TOL, cen["MAIN"]["rho32"],
                        cen["TWIN"]["rho32"],
                        str({w: ("%.3g" % cen[w]["rho32"]
                                 if np.isfinite(cen[w]["rho32"])
                                 else "NONFIN")
                             for w in ("EPST", "SCR", "SMOOTH",
                                       "HL2")}),
                        cen["DIR"]["lam"],
                        cen["DIR"]["lam_rest"],
                        cen["ABS"]["lam"],
                        cen["ABS"]["lam_rest"]))
        check("G61-worlds", lr_sep and ok_kint,
              "WORLD LEDGER: lambda_rest >= 1 on dead 4/4 and < 1 "
              "on live 2/2 (r343 separation re-gated); kappa_int "
              "EPST %.6g / SCR %.4g / SMOOTH %.4g / HL2 %.6g == "
              "records at %.0f%%, live %.6f; THE SEALED MIRROR "
              "RULE => %s"
              % (cen["EPST"]["kint"], cen["SCR"]["kint"],
                 cen["SMOOTH"]["kint"], cen["HL2"]["kint"],
                 100 * KINT_REC_TOL, cen["MAIN"]["kint"],
                 mirror_tag))

    # ---------------- S7 must-fails
    section("S7  MUST-FAILS")
    mut1 = mutant_identity_flip(C9["ppr"], C9["qpr"], C9["m2p"])
    rhs9 = C9["ppr"] * C9["qpr"] - C9["cpr"] ** 2
    dev_m1 = abs(mut1 - rhs9) / abs(rhs9)
    mut1t = mutant_identity_flip(0.75, 0.5, m2f)
    dev_m1t = abs(mut1t - rhs_t) / abs(rhs_t)
    check("G70-m1-wrong-normalization", dev_m1 >= M1_BAR
          and dev_m1t >= MUT_MIN,
          "m1 THE WRONG NORMALIZATION m2'(p'+q'+m2'): breaks the "
          "exact one-line identity by %.1e rel at w9 (>= %.1f) "
          "and %.1e on the hand toy -- the deficit enters the "
          "second factor SIGNED, exactly CAUGHT"
          % (dev_m1, M1_BAR, dev_m1t))
    mut2 = mutant_bar_posthoc(0.05)
    check("G71-m2-bar-posthoc", bool(hits_m2)
          and abs(mut2 - CLOSURE_BAR) >= MUT_MIN,
          "m2 CLOSURE BAR AFTER SIGHT: AST-FLAGGED (%s) and the "
          "toy 'recalibrated bar' %.2f != the sealed CLOSURE_BAR "
          "%.1f -- protocol-CAUGHT (the bars are frozen module "
          "constants under the two-commit protocol)"
          % (hits_m2[0] if hits_m2 else "MISS", mut2,
             CLOSURE_BAR))
    mut3 = mutant_alpha_circular([1.0e-3, 1.0e-6],
                                 [math.log(300.0),
                                  math.log(3000.0)])
    check("G72-m3-alpha-circular", bool(hits_m3)
          and abs(mut3 - 3.0) <= 1e-9,
          "m3 ALPHA READ CIRCULARLY off the margin column: "
          "AST-FLAGGED (%s; toy two-point value %.3f) -- the "
          "REAL alpha_id constructor consumes fitted dressed-"
          "column slopes only and is scope-audited CLEAN"
          % (hits_m3[0] if hits_m3 else "MISS", mut3))
    mut4 = mutant_factor_readback()
    check("G73-m4-factor-readback", bool(hits_m4)
          and mut4 > 0.0,
          "m4 DICTIONARY FACTOR READ BACK from the withheld "
          "lambda record: AST-FLAGGED (%s) -- the factor columns "
          "are Gram-block objects, never spectrum-record "
          "read-offs" % (hits_m4[0] if hits_m4 else "MISS"))
    mut5 = mutant_mirrorbar_posthoc([0.92, 1.0e6])
    check("G74-m5-mirrorbar-posthoc", bool(hits_m5)
          and abs(mut5 - MIRROR_LIVE_BAR) >= MUT_MIN,
          "m5 MIRROR-LIVE BAR AFTER SIGHT: AST-FLAGGED (%s) and "
          "the toy posthoc bar %.3g != the sealed %.1f -- "
          "protocol-CAUGHT" % (hits_m5[0] if hits_m5 else "MISS",
                               mut5, MIRROR_LIVE_BAR))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism "
          "promoted, no certificate reading beyond the sealed "
          "census, no posthoc bar/band/family/prior move, no "
          "derived 5/7, NO RH claim, mincut unchanged; what the "
          "round adds: the one-line identity with its exponent "
          "accounting, the bridge protocol, the dressed-"
          "dictionary double adjudication, and the sealed mirror "
          "world clause with the Dirichlet columns; r243..r346 "
          "stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        closures_ok = all(v <= CLOSURE_BAR
                          for v in closures.values())
        support_ok = (bridge_ok and flats_ok and laws_ok)
        if not audits_ok:
            main_v = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif closures["C2"] > CLOSURE_BAR \
                or closures["C4"] > CLOSURE_BAR:
            main_v = ("ACCOUNTING_GAP(C2 %.3f, C4 %.3f vs bar "
                      "%.1f -- the core reduction is broken)"
                      % (closures["C2"], closures["C4"],
                         CLOSURE_BAR))
        elif closures_ok and support_ok:
            main_v = ("ALPHA_CLOSED(alpha %.3f == a_c %.3f + "
                      "delta %.3f = %.3f (C4 %.3f) == alpha_id "
                      "%.3f (C1 %.3f); BLOCKS TYPED: identity "
                      "THEOREM-GRADE (Fractions + f64 %.1e), "
                      "bridge + flats CERTIFIED CENSUS, a_c + "
                      "delta FIT-CENSUS laws -- the margin "
                      "exponent is reduced to the cancellation "
                      "law + the bare coupling law)"
                      % (alpha_meas, a_c, delta, alpha_line,
                         closures["C4"], alpha_id,
                         closures["C1"], max_id))
        else:
            fails = []
            if not closures_ok:
                fails += ["C1 %.3f" % closures["C1"]
                          if closures["C1"] > CLOSURE_BAR else "",
                          "C3 %.3f" % closures["C3"]
                          if closures["C3"] > CLOSURE_BAR else ""]
            if not bridge_ok:
                fails.append("bridge")
            if not flats_ok:
                fails.append("flats")
            if not laws_ok:
                fails.append("laws")
            main_v = ("ALPHA_CLOSED_CENSUS(C2 %.3f + C4 %.3f "
                      "hold; failed support: %s)"
                      % (closures["C2"], closures["C4"],
                         "; ".join(f for f in fails if f)))
        parts = [
            main_v,
            dress_tag,
            mirror_tag,
            "IDENTITY_LEDGER(max per-rung residual %.1e of %d "
            "(bar %.0e), definitional ward %.1e (bar %.0e), "
            "Fractions toy EXACT)"
            % (max_id, len(all_kz), ID_BAR, max_rd, RDEF_BAR),
            "EXPONENT_LEDGER(%s; closures C1 %.3f / C2 %.3f / "
            "C3 %.3f / C4 %.3f)"
            % (exp_txt, closures["C1"], closures["C2"],
               closures["C3"], closures["C4"]),
            "WORLD_LEDGER(%s)" % world_txt,
            "TWIN_LEDGER(dressed dev %.1e, m2' dev %.1e)"
            % (devT["d"], devT["m2p"]),
            "MUSTFAIL_LEDGER(m1-m5 + scopes)",
        ]
        verd = " + ".join(p for p in parts if p)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED accounting + sealed adjudication of "
          "the one-line identity; NO L* claim, NO RH claim"
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
