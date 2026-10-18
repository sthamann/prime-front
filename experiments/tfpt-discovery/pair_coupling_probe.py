#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pair_coupling_probe -- PRIME.LSTAR.PAIR_COUPLING.01 (round 343):
the DRESSED PAIR RESERVE r'_det -- the O(1) certificate candidate of
r342 -- put under fire: exact anatomy of the Schur dressing, the
honest refutation attempt on fresh families, the adjudication of the
analytic lower-bound question, and the second Schur clause
lambda_rest < 1 with its peeling structure.

R342 (pair_extremal_probe, SPEC_SHA b09f8ccd, PAIR_LAW_FOUND +
PAIR_WORLD_COMPLETE) established: L* at the binding point is the
determinant condition c^2 < pq of the shallow-edge two-atom block;
the EXACT Schur decomposition L* <=> {lambda_max(D) < 1} AND
{lambda_max(A + C (I-D)^{-1} C^T) < 1} (logdet-gated); the rest
margin 1 - lambda_rest decays parallel to the full margin (slope
-3.276, offset ~20x) while the DRESSED reserve r'_det = 1 -
c'^2/(p'q') is FLAT (slope +0.018, w9 value 0.303) -- the first
flat, positive, source-near O(1) quantity of the L* lane.  THE
ROUND'S CONTRACT (the r342-R343 kill, sharpened): does r'_det
possess an ANALYTIC O(1) lower bound from the source -- or does its
flatness break on a fresh family?

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: R341 (Bellman, terminal) may run in parallel -- this
probe touches NOTHING outside its own file and the strictly
additive rh-sync.  Two-commit freeze protocol (r329 convention):
spec + machinery committed BEFORE the record run, record tables
inserted after.

THE EXACT OBJECTS (all gated): per rung the r342 bundle (d1, d2, c,
p, q, r_det, m2, margin, pair mass, PR, det/interlacing/Schur-logdet
identities) via the IMPORTED r342 build verbatim; the dressed block
A' = A + C (I-D)^{-1} C^T with (d1', d2', c'), p' = 1-d1', q' =
1-d2', r'_det = 1 - c'^2/(p'q'), m2' = 1 - lambda_max(A'); THE
RESOLVENT-CORRELATION IDENTITY (this round's exact spine): I - A'
is the inverse of the 2x2 pair block M of (I-E)^{-1}, hence
    r'_det = 1 - M_12^2 / (M_11 M_22)
-- the dressed reserve IS the Cauchy-Schwarz reserve of the
resolvent (I-E)^{-1} at the pair (gated per rung against the
independent full-inverse route); THE SPECTRAL EXPANSION (exact,
gated): with (delta_m, w_m) the eigenpairs of the rest block D and
alpha_m = u_1 . w_m, beta_m = u_2 . w_m (u_k = the coupling rows
E[pair_k, rest]),
    Delta d_1 = sum_m alpha_m^2 / (1 - delta_m)   (d_2: beta_m),
    Delta c   = sum_m alpha_m beta_m / (1 - delta_m),
    d_k' = d_k + Delta d_k,  c' = c + Delta c
-- the exact decomposition r'_det = f(bare scalars, rest coupling
vectors) demanded by the contract, printed per rung with its
absorption anatomy (Delta d_1/p, Delta c/c, top-mode shares); the
TOP-K RESOLVENT SHADOW r'_K = the same correlation reserve with
(I-E)^{-1} truncated to its top K eigenmodes (K = S_- reproduces
r'_det exactly -- the toy gate); the BARE LAMBDA SHADOW r_shadow =
margin (p + q - margin)/(pq) (what r'_det would be if the dressing
carried NO content beyond lambda_max and the bare scalars -- the
sealed RESTATEMENT test); the GAP RATIO g21 = (1-lambda_2)/
(1-lambda_1) (the reduced O(1) coordinate of the top-2 reading);
the CERTIFIED-BOUND RELAXATION LADDER (Leg C, measured): R1 exact
(== r'_det), R2 sign relaxation |c'| <= |c| + |Delta c|, R3
per-mode Cauchy-Schwarz |Delta c| <= sum |alpha_m beta_m|/(1 -
delta_m), R4 the K-split operator-tail bound (top-K modes exact,
tail by ||tail||^2/(1 - delta_{K+1})) -- each level a THEOREM-GRADE
inequality chain whose INPUTS are measured scalars; r'_lb(K)
printed for K in {0, 1, 3, 8, 32}; THE PEELING COORDINATES (Leg D):
the rest block's own top eigenvector (PR, mass on the rest
shallow-edge pair, folds) and the level-2 Schur dressing of that
pair inside D (lambda_rest2, r''_det) -- the recursion question,
plus the full level-k cascade census on w9.

INDEX FIREWALL (binding, r238-r342 discipline): w = window (kz into
the prime-power list), S = #union atoms, S_- = #nu atoms, N_w =
(S+1)//2; ground truth (r283/r284/r286/r329/r334/r342 records,
control flips, kappa_int records) enters GATES and record tables
only; the module-own constructors consume kernel Gram / spectrum /
weight / position arrays ONLY (AST scope audit; the spectrum of the
INSTRUMENTED matrix is the round's object of study -- the withheld
identifiers are the RECORD values and the verdict-side fit results);
no zero/prime oracles anywhere (AST firewall; the prime-power grid
is the sealed source comb, r238 convention); no fit primitives
(fragment audit; fits are the imported r286 Theil-Sen).  MACHINERY
IMPORTED VERBATIM: r342 PX.{build_rung, pair_select, pair_block,
pair_eigs, det_reserve, schur_dress, prime_cf_density,
arch_dict_density, v_predict, layer_split, mp_pair_ward, eig_pr}
(SPEC_SHA prefix gated b09f8ccd), r329 E3.{admissible_pool,
grel_col, used_kz_set, gap_class} (SPEC_SHA prefix gated bbfaf199),
document pipeline V.{build_measures, window_shape, mu_chain,
b_matrix, admissible_indices, lam_max_at, U, W_VM, PP, TABLE_CAP},
r286 LM.{ts_fit, ts_slope_free, ext_rule}, r334 FC.{world_from_
arrays, world_from_mz, interval_census, frac_instance, frac_kernel,
frac_solve}, r283 FS (via PX mp route), r278 MS.ctx_build, r280
BL.{union_of_ctx, sign_chain_f64}, v881 PIK.lambda_eps, r243
PB.smooth_comb, paircorr PC.{Grid, gen_model}, r331 TR.{base_comb,
build_world}, r289 AKD.twin_rational, r276 MF.local_gaps, v563
core READ-ONLY.

LEG 0 -- ANCHORS BIT-NEAR (r342 record numbers as gates): w9 pair
(d1 0.970014, d2 0.964904, c 0.032252, r_det 1.1561e-2, m2
1.8749e-4), w9 Schur (lambda_rest 0.996338, dressed 0.999154 /
0.998710 / 0.000872, r'_det 0.3029), the kz130 s3 row, the R2
cohort medians 0.205/0.188/0.437/0.557, kz56 R2 1.836, the EXT3
margin minimum 4.20e-9 at kz127, the r342 fit slopes (p -0.754, q
-0.645, c -0.697, m2 -3.341, margin -3.332, restm -3.276, rdetp
+0.018 -- the DISCLOSED PRIORS of this round), the digamma
dictionary on the sample rungs (DIGAMMA_BAR 0.02, V_BAR 0.10), the
r334/r342 kappa_int records (EPST 1793.99, SCR 8.51e6, SMOOTH
2.193, HL2 1964, MAIN/TWIN 0.999567).

LEG A -- THE ANATOMY OF THE DRESSING: per rung the exact
decomposition columns (Delta d_1/p, Delta d_2/q, Delta c/c, bare
correlation rho = c/sqrt(pq), dressed rho' = c'/sqrt(p'q'), m2'/
margin, g21, top-1/top-3 mode shares of Delta d_1); the mechanism
said with numbers: the bare cancellation rho -> 1 (r_det ~ N^-2.6)
is ABSORBED by a signed cancellation Delta c ~ -c in the dressing
while p, q are eaten proportionally -- the dressed correlation
rho' stays bounded; source-explicitness census: the coupling-row
profile share of ||u_1||^2 on arch-rim rest atoms (u < log 2) and
the dictionary prediction of the REST-pair weights (the peeling
pair) on the sample rungs -- the weight side of the dressing is
dictionary-explicit, the kernel side stays census-grade (r342
negative #4, restated honestly).

LEG B -- THE HONEST KILL (sealed fit rules BEFORE the record):
Theil-Sen fit of log r'_det vs log N_w on the 57 (42 core + 15
r286 extension); FLAT_57 iff |slope| <= FLAT_BAR = 0.15 AND
|halves curvature| <= CURV_BAR = 0.35.  PURE TEST on the 12 r329
EXT3 anchors (their per-row r'_det/lambda_rest columns were NEVER
printed in r342 -- genuinely blind rows): in-band iff |log10(pred/
meas)| <= 0.5 with pred from the 57-fit; need >= 10/12; EXT3
low-side count n_low (meas below the lower band edge).  EXT4 (the
fresh-family stress, sealed selection below): same band, low-side
count.  DECAYS iff (slope_57 <= -0.30 with |curv| <= 0.35) OR
(EXT3 n_low >= 4) OR (EXT4 n_low >= 3) OR (any arbitrated
positive-margin row has r'_det <= RDETP_FLOOR = 0.01) OR (FLAT
fails on any clause -- soft decay, clauses named).  FLAT survives
iff FLAT_57 AND EXT3 in-band >= 10/12 AND EXT4 n_low <= 1.  The
decision tree is exhaustive; the kill direction is the default.

LEG C -- THE LOWER-BOUND ADJUDICATION: the relaxation ladder
R1-R4 evaluated on every rung (detailed print on the sample);
sealed census statistic: n_pos(K) = #rows with r'_lb(K) > 0 for
K in {0, 1, 3, 8, 32}; the O1-certificate clause (sealed,
symmetric): DRESSED_RESERVE_O1_CERTIFIED requires FLAT + r'_lb(K
<= 32) >= DELTA_BAR = 0.05 on ALL arbitrated rows + KERNEL_CLOSED_
FORM (a closed-form source derivation of the coupling norms and
lambda_rest -- sealed FALSE this round: the kernel side has no
closed form, r342 negative #4).  Honest typing: every inequality
in R2-R4 is theorem-grade (triangle, Cauchy-Schwarz, operator
norm); the INPUTS are measured; and the s1 scoping already shows
the sign relaxation R2 is CATASTROPHIC at w9 (the dressing works
by the signed cancellation Delta c ~ -c, so |c| + |Delta c| ~ 2|c|
overshoots the cancelled c' by ~70x and r'_R2 = -3708) -- the
reachable positive outcome of this round is FLAT_CENSUS, and the
concretized specialist question is typed: an O(1) bound must
control the SIGNED cancellation, equivalently the gap ratio g21
and the top-2 eigenvector geometry at the pair (the top-2 shadow
census below).

LEG D -- THE SECOND CLAUSE + PEELING: lambda_rest per rung (fit
vs the -3.276 prior, offset ratio (1-lambda_rest)/margin); world
column: does lambda_rest alone separate the dead worlds?; the
rest-top-eigenvector census (PR, rest-shallow-pair mass, folds)
on all rungs; level-2 dressing (lambda_rest2, r''_det) on all
rungs; the w9 level-k cascade (k = 1..6).  PEELING_STRUCTURE_FOUND
(additive tag) iff median rest-pair mass on the 57 >= 0.90 AND min
r''_det on the 57 >= PEEL_R2_FLOOR = 0.05 -- the induction
candidate (L* as pair peeling), typed, never claimed.

LEG E -- WORLDS + MUST-FAILS: MAIN / TWIN / EPST / SCR / SMOOTH /
HL2 (r278/r280 channel verbatim, minC == flips 25/21/27/25 gated)
at their OWN N_w: lambda_max, lambda_rest, dressed reserve (UNDEF
iff lambda_rest >= 1), pair mass, PR, kappa_int (r334 machinery
verbatim, records gated); the EXACT SCHUR EQUIVALENCE GATE per
world: (lambda_max < 1) == (lambda_rest < 1 AND p' > 0 AND q' > 0
AND r'_det > 0).  MUST-FAILS (>= 5, each loud): (m1) DRESSING AT
THE WRONG BLOCK: the two largest-v atoms as 'pair' -- CAUGHT by
the concentration check (top-eigenvector mass < 0.5); (m2) r'_det
READ BACK from the withheld lambda record -- AST-FLAGGED; (m3)
FLATNESS BAR RE-PICKED AFTER SIGHT: a mutant consuming the
withheld fit slope -- AST-FLAGGED, and on the sealed toy returns
!= the sealed FLAT_BAR (protocol-CAUGHT: the bars are frozen
module constants under the two-commit protocol); (m4) SCHUR
IDENTITY WITH SWAPPED BLOCKS: det(I-E) claimed == det(I-A') x
det(I-D'') with BOTH blocks dressed (double-counted coupling) --
breaks the exact logdet identity by >= 1.0 log-units on w9; (m5)
RESOLVENT CORRELATION READ OFF E INSTEAD OF (I-E)^{-1} -- breaks
by >= 0.1 rel on w9.  STOP LIST (anti-gates, binding): NO L*
claim, NO bound mechanism promoted, NO certificate reading of the
census bound, NO posthoc bar / band / family / prior move, NO
derived 5/7, NO RH claim; r243..r342 stand.

THE SEALED EXT4 SELECTION (fresh-family stress, source-pure,
r329 machinery verbatim): USED = E3.used_kz_set(core.frame_a_
zones(), LM.ext_rule(), 35) UNION the 12 r329/r342 EXT3 anchors
(gated == 92); POOL = E3.admissible_pool(H_MIN, EXT4_H_MAX =
3400); DOMAIN: z^2 <= 400000 (= the family's von Mangoldt TABLE
CAP: a window with z^2 beyond the table has a TRUNCATED source
comb and is NOT an instance of the documented family -- the s2
scoping fact: the h-desc queue head kz277 (z 1583) builds a
truncated non-instance with margin -228; the cap is a family-
definition fact, not a posthoc filter); FRESH = POOL minus USED
under the domain (gated == 23); STRATUM B4 = the 3 smallest-grel
fresh kz with z inside the core zone range [16, 317] (grel =
E3.grel_col, r317 W = 5 convention); STRATUM A4 = the 3 deepest
(h desc) of the remainder.  Selection gated == the s3-disclosed
queues B4 (72, 75, 66) / A4 (113, 111, 108), N_w in [2656, 3181]
exact -- ALL deeper than the 57 (max 1218) and interleaving the
EXT3 range.  Grid identity gate: int(V.PP[kz]) == int(core._NN
[kz]) on all 18 EXT3+EXT4 anchors.  CONTINGENCY (sealed): any f64
margin <= 0 on a fresh row is excluded from fits and typed; mp
arbitration only for N_w <= 2600 (budget), else typed
F64_ONLY_NEGATIVE.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_+ 263, S_- 104, N_w
184); REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN
1.6752e-4 rel 0.01; SHALLOW_FOLDS (2, 4); W9 ANCHORS d1 0.970014 /
d2 0.964904 / c 0.032252 (rel 2e-5 = the 6-decimal record print
precision), r_det 1.1561e-2 / m2
1.8749e-4 (rel 1e-3), lambda_rest 0.996338 (abs 1e-5), d1'
0.999154 / d2' 0.998710 (rel 1e-5), c' 0.000872 (abs 2e-6),
r'_det 0.3029 (rel 1e-3); KZ130 ANCHORS d1 0.99374973 / d2
0.98989097 (rel 1e-7), c 0.00794884 (rel 1e-5), r_det 2.017e-6 /
m2 7.789e-9 / margin 4.918e-9 (rel 2e-2), R2 0.584 / pmass 0.9814
(abs 5e-3); R2 COHORT MEDIANS (0.205, 0.188, 0.437, 0.557) abs
0.01; KZ56_R2 1.836 abs 0.01; EXT3_MARGIN_MIN 4.20e-9 at kz127
rel 0.05; FIT ANCHORS (p -0.754, q -0.645, c -0.697, m2 -3.341,
margin -3.332, restm -3.276, rdetp +0.018) abs 0.02; CTRL_FLIPS
{EPST 25, SCR 21, SMOOTH 27}; HL2 seed 101 flip 25; KINT RECORDS
{EPST 1793.99, SCR 8.51e6, SMOOTH 2.193, HL2 1964} rel 0.05,
{MAIN 0.999567, TWIN 0.999567} rel 1e-3; EXT15_KZ = the r286
record set (via LM.ext_rule, gated); EXT3_KZ_B (42, 51, 54, 56,
58, 62); EXT3_KZ_A (96, 123, 125, 127, 128, 130); EXT3_NW (1721,
2577); EXT4_H_MAX 3400; K_EXT4 3; Z2_CAP 400000; EXT4_KZ_B (72,
75, 66); EXT4_KZ_A (113, 111, 108); EXT4_NW (2656, 3181);
USED_EXPECT 92; FRESH_EXPECT 23; CORE_Z (16, 317); MASS_BAR 0.90;
R2_MAX 1.5; DET_ID_BAR 1e-12; INTERLACE_TOL 1e-9; SCHUR_BAR 1e-6;
RES_ROUTE_BAR 1e-6; SPECTRAL_BAR 1e-9; FLAT_BAR 0.15; DECAY_SLOPE
0.30; CURV_BAR 0.35; BAND 0.5 decades; EXT3_OK_MIN 10;
EXT3_LOW_KILL 4; EXT4_LOW_KILL 3; RDETP_FLOOR 0.01; RESTATE_BAR
0.05; TOP2_BAR 0.15; KRES_BAR 0.10; KRES_LIST (1, 2, 3, 5, 10);
K_LIST (0, 1, 3, 8, 32); DELTA_BAR 0.05; KERNEL_CLOSED_FORM False
(sealed); PEEL_MASS_BAR 0.90; PEEL_R2_FLOOR 0.05; PEEL_CASCADE 6;
SAMPLE_KZ (18, 9, 52, 119, 42, 130); DIGAMMA_BAR 0.02; V_BAR
0.10; MP_SET ((9, 30), (9, 45), (52, 30), (130, 30)); MP_DC_CORE
1e-9; MP_DC_EXT3 1e-8; MP_M2 depth-graded 1e-6 (N_w <= 400) /
1e-5 (<= 1500) / 1e-3 (beyond); STAFFEL_BAR 1e-12; TWIN_TOL 1e-8;
TWIN_BAR 1e-3; FRAC_BAR 1e-10; TOY_TOL 1e-12; MUT_MASS_BAR 0.5;
M4_BAR 1.0 (log-units); M5_BAR 0.1; MUT_MIN 1e-6; runtime <=
1800 s; smoke = toys + firewall + scopes + mutants + w9 block
(records, pair/Schur anchors, resolvent identity, spectral
expansion, shadows, bound ladder, dictionary sample, level-1
peel + cascade); ladder, EXT3/EXT4, twin, mp wards, fits, worlds
and adjudication skipped.

PRE-SPEC SCOPING (disclosed, r342-s1..s3 precedent -- no bar,
band, threshold, family or adjudication rule was tuned after any
evaluation except as sized here and said so): (s1) the w9
extension was probed end-to-end: resolvent identity dev 8.9e-14;
m2'/margin 1.0029 (the dressed pair margin IS the full margin to
0.3 percent); top-K shadows 0.0 / 0.2883 / 0.2994 / 0.3015 /
0.3027 at K = 1/2/3/5/10 vs r'_det 0.3029 -- the dressed reserve
is a TOP-2-DOMINATED spectral object; Delta d_1 top-1/top-3 mode
shares 0.19/0.33 (the absorption is NOT single-mode); the
relaxation bounds r'_lb(K) = -inf at every K and the sign-only
reserve r'_R2 = -3708 (Delta c = -0.0314 vs c = +0.0323: the
dressing IS a signed near-cancellation -- the triangle route is
dead on arrival, disclosed BEFORE the freeze); bare shadow ratio
r_shadow/r'_det = 0.034 (the RESTATEMENT test is expected NOT to
fire; rule sealed symmetric anyway); rest-top eigenvector mass
0.9807 on the rest shallow pair folds (6, 8), lambda_rest2
0.973300, r''_det 0.5502 (the peeling signal exists at w9).
(s2) the EXT4 enumeration: without the domain cap the h-desc
queue head is kz277 (z 1583, z^2 = 2.5e6 > TABLE_CAP) -- a
truncated-comb NON-instance (margin -228, lambda_rest 229); the
domain-capped fresh pool has 23 windows.  (s3) the six EXT4 rows
were probed end-to-end for budget and bar sizing (2.5 s each;
margins +3.0e-9..+1.6e-8 all positive; r'_det 0.2368..0.3679;
m2'/margin 1.000..1.031; rest-pair mass 0.944..0.9997; r''_det
0.51..0.73; resolvent-route devs <= 1.1e-8, spectral devs <=
2e-13 -- sizing RES_ROUTE_BAR/SPECTRAL_BAR) -- DISCLOSED
HONESTLY: all six EXT4 rows were seen before the freeze; the
blind teeth of the flatness adjudication are the 12 EXT3 rows
(per-row r'_det / lambda_rest never printed in r342) plus the
sealed fit protocol; the sealed adjudication rules were fixed
BEFORE any EXT3 dressed column was seen.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > RESTATEMENT > the exhaustive FLAT/DECAYS
tree):
  [exactly one of]
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  RESTATEMENT  iff median over the 57 of |r_shadow/r'_det - 1| <=
    0.05 -- r'_det would then be a bare-scalar + lambda_max
    read-off with no dressing content /
  DRESSED_RESERVE_O1_CERTIFIED  iff FLAT survives AND r'_lb(K <=
    32) >= 0.05 on ALL arbitrated rows AND KERNEL_CLOSED_FORM
    (sealed FALSE this round -- the clause exists so the enum is
    complete and honest) /
  DRESSED_RESERVE_FLAT_CENSUS  iff FLAT survives (|slope_57| <=
    0.15, |curv| <= 0.35, EXT3 in-band >= 10/12, EXT4 n_low <= 1)
    -- the O(1) reading carries as a measured census, the lower
    bound stays census-grade /
  DRESSED_RESERVE_DECAYS(clauses, loci)  otherwise -- hard iff
    (slope_57 <= -0.30 AND |curv| <= 0.35) or EXT3 n_low >= 4 or
    EXT4 n_low >= 3 or any arbitrated row r'_det <= 0.01; soft
    iff a FLAT clause fails without a hard clause (named)
  + ANATOMY(the exact decomposition medians: Delta d_1/p, Delta
    c/c, rho', m2'/margin, g21 + its fit) [always]
  + BOUND_LEDGER(n_pos per K, min/median r'_lb(32), the R2 sign
    autopsy -- the Leg C adjudication material) [always]
  + LAMBDA_REST_LEDGER(slope vs -3.276 prior, offset ratio,
    world separation of the lambda_rest clause) [always]
  + [exactly one of] PEELING_STRUCTURE_FOUND(median rest-pair
    mass >= 0.90 on the 57 AND min r''_det >= 0.05) /
    NO_PEELING(numbers)
  + [exactly one of] TOP2_SPECTRAL_OBJECT(median |r'_2/r'_det -
    1| <= 0.15) / TOPK_CENSUS(median K_res)
  + EXT4_CENSUS(per-row table + which stratum stresses what)
    [always]
  + TWIN_LEDGER(rel deviations) [always]
  + MUSTFAIL_LEDGER(m1-m5 + scopes) [always].
Honesty before beauty: r'_det flat on 69 + 6 windows is a MEASURED
census, never an asymptotic theorem; the resolvent-correlation
identity and the R2-R4 inequality chains are exact finite-matrix
facts (theorem-grade SKELETON) whose inputs are measured window
scalars (census-grade FLESH); the sign autopsy shows WHY no
triangle-route certificate can work -- the honest content of Leg C
is the typed specialist question, not a bound; a passing world
clause is a measured discriminator on six instrumented worlds;
the peeling tag is an induction CANDIDATE, not an induction; no
verdict claims L*, a bound mechanism, a derived 5/7, or RH
progress in any direction.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit, which IS the protocol; TWO-COMMIT PROTOCOL
EXECUTED: the sealed spec above was committed as "r343 pre-freeze"
(e652071f) BEFORE the first full evaluation; chronology honest:
smoke pass 1 = 35/38 with TWO machinery findings, both fixed
BEFORE the freeze commit: (f1) the exact-Fraction ward demanded
minors POSITIVITY, but JF9 is not a lambda_rest < 1 instance
(measured lambda_rest 1.6656) -- the gate now demands SIGN
AGREEMENT of the rational minors criterion with the f64 route,
the stronger and correct ward; (f2) the w9 d/c anchor bar 1e-5
sat below the 6-decimal print precision of the r342 record (c
dev 1.52e-5 pure rounding) -- bar sized to 2e-5; two gate TEXTS
were made census-neutral (the arch-rim share and the cascade
concentration are reported, not asserted); NO adjudication rule
touched at any point.  Smoke pass 2 = 38/38 (0.6 s); pre-freeze
commit e652071f; calibration pass 1 = FIRST full evaluation =
38/38 (141.1 s), NO amendment; record run1 = 38/38 (147.4 s),
run2 = 38/38 (141.6 s), byte-identical up to WALL and identical
to the calibration pass):
MAIN VERDICT = DRESSED_RESERVE_DECAYS(soft: FLAT_57 (slope
+0.018, curv -0.426 > bar 0.35)) -- read PRECISELY: every HARD
kill clause MISSES (slope +0.018 is dead flat; EXT3 blind rows
12/12 inside the 0.5-decade band with n_low 0; EXT4 fresh rows
6/6 in band with n_low 0; no row within two decades of the 0.01
floor -- r'_det spans 0.1383 (kz98) .. 0.5361 (kz57), both
MID-ladder), but the sealed FLAT clause fails on the halves
CURVATURE of the 57-column: the flat O(1) column carries ~x2
scatter in both directions and its half-ladder Theil-Sen slopes
differ by 0.43 (a bar inherited from the r342 decay-law
convention, sealed before sight, applied honestly).  The O(1)
candidate is NOT refuted on any family -- and NOT certified
flat under the sealed clause: the letter of record is the soft
decay, the census content stands typed below.
+ ANATOMY(medians on the 57: Delta d_1/p = 1.000, Delta c/c =
-1.000 (to 3 decimals: at depth the dressing eats the ENTIRE
bare reserve and coupling -- w9 still resolves 0.9718 / -0.9730),
rho' = 0.846, m2'/margin = 1.0058, g21 = 8.21 (fit slope +0.049,
curv +0.601 -- flat in slope, curved like r'_det itself); w9
exact decomposition: Delta d1 = 2.9140e-2 = 0.9718 p, Delta c =
-3.1380e-2 = -0.9730 c, dev vs direct Schur 9.8e-15; top-1/top-3
rest-mode shares of Delta d1 = 0.192/0.335 (multi-mode
absorption); the dressed pair margin IS the full margin: m2'/
margin in [1.0003, 1.031] on every scoped row -- the dressed
2x2 is a near-exact lambda_max carrier; coupling-row arch-rim
share 0.8461 at w9 (census); the rest-pair weights are
dictionary-predicted to 7.0e-3 at w9 (bar 0.10) -- the weight
side of the dressing is closed-form, the kernel side stays
census-grade)
+ BOUND_LEDGER(n_pos(K = 0/1/3/8/32) = 0/0/0/0/0 of 75 rows;
min r'_lb(32) = -inf; sign autopsy r'_R2 on the sample: kz9
-3.7e3 / kz18 -1.2e5 / kz52 -2.3e8 / kz119 -9.7e9 / kz42
-2.2e10 / kz130 -2.4e11 -- the theorem-grade R2-R4 chain NEVER
certifies a single row: the triangle step |c| + |Delta c|
overshoots the cancelled |c'| by 73x already at w9 and the
overshoot grows with depth; THE TYPED SPECIALIST QUESTION: an
O(1) lower bound on r'_det must control the SIGNED cancellation
Delta c ~ -c -- equivalently (top-2 reading, gated) the gap
ratio g21 and the top-2 eigenvector 2x2 geometry at the pair;
no census certificate is promoted, the O1 clause cannot fire
(KERNEL_CLOSED_FORM sealed FALSE, bound clause False))
+ LAMBDA_REST_LEDGER(slope of 1 - lambda_rest on the 57 =
-3.276 == the r342 prior -3.276 bit-near (curv +0.395), offset
(1-lambda_rest)/margin median 21.0x, range 8.8..54.2 over all
75 rows -- the second Schur clause carries margin-parallel with
O(20x) headroom; WORLD SEPARATION: lambda_rest ALONE separates
4/4 dead worlds (EPST 2191 / SCR 1.058e6 / SMOOTH 2.211 / HL2
2776 all >= 1; live MAIN/TWIN 0.996338 < 1) -- on the
instrumented worlds the REST clause is already the
discriminator: the dressed-pair clause never has to fire on a
dead world, and the Schur equivalence gate holds 6/6 exactly)
+ PEELING_STRUCTURE_FOUND(median rest-pair mass on the 57 =
0.9902 >= 0.90 (min 0.6917 at kz44 -- honest, printed), min
r''_det on the 57 = 0.2296 >= 0.05; EXT3/EXT4 medians: mass
0.9793 / 0.9901, r''_det 0.60 / 0.66; the w9 level-k cascade
(k = 1..6): folds (2,4) -> (6,8) -> (10,12) -> (14,15) ->
(17,19) -> (21,23), top-vec pair mass 0.997 -> 0.981 -> 0.897
-> 0.0003 -> 0.006 -> 0.687, reserve 0.303 -> 0.550 -> 0.931 ->
0.915 -> 0.997 -> 0.999, lambda_rest_k 0.99634 -> 0.97330 ->
0.96166 -> 0.96152 -> 0.96111 -> 0.93174 -- the reserve stays
positive and lambda_rest_k falls monotonically at every peel;
the shallow-pair CONCENTRATION persists to level 3 and BREAKS
at level 4 (mass 3e-4): the peeling recursion is real at the
adjudicated level-2 depth across the whole ladder, and its
deeper levels are an honest census, not a clean induction)
+ TOP2_SPECTRAL_OBJECT(median |r'_2/r'_det - 1| = 0.0634 <=
0.15 on the 57; K_res median 2, max 3 over all 75 rows --
r'_det is numerically a TOP-2 spectral object: lambda_max,
lambda_2 and their eigenvector 2x2 at the pair carry it to ~6
percent; the flat O(1) content of the dressed reserve IS the
flat gap ratio g21 (median 8.2; kz56 = 16.0) plus bounded
top-2 geometry -- the concretized successor coordinate)
+ EXT4_CENSUS(B4 kz72/75/66 (z 269/281/241, N_w 3022/3181/2656,
small-gap in-zone, grel 0.364/0.402/0.441): margins 1.03e-8/
1.13e-8/1.55e-8, r'_det 0.3270/0.3679/0.2985, bare R2 0.255/
0.536/0.984 -- the small-gap family strains the bare-R2 band
AGAIN (kz66 at 0.98; the r329/r342 lesson) while the DRESSED
reserve stays flat; A4 kz113/111/108 (z 499/487/463, N_w 3113/
3027/2855, deepest fresh): margins 4.34e-9/3.00e-9/4.33e-9,
r'_det 0.3101/0.2444/0.2368 -- the deepest windows ever
measured in the L* lane, all margins positive, dressed reserve
still O(1); used ledger 92, domain-capped fresh 23, grid
identity 18/18)
+ TWIN_LEDGER(dressed scalars dev <= 2.3e-6, r'_det dev 9.1e-6,
lambda_rest dev 3.5e-8 (bar 1e-3); dose-zero identity BITWISE)
+ MUSTFAIL_LEDGER(m1 wrong-block mass 0.0000 < 0.5 vs sealed
pair 0.9970; m2 AST-FLAGGED REC_LAM; m3 AST-FLAGGED + toy 0.42
!= sealed 0.15; m4 double-dress breaks the logdet identity by
3.61 log-units >= 1.0; m5 E-correlation 0.9989 vs 0.3029, dev
2.3 >= 0.1; constructor scopes + fragment audit CLEAN).
Key numbers.  W9: r'_det = 0.302916 == the resolvent-correlation
1 - M12^2/(M11 M22) (independent full-inverse route dev 8.9e-14,
bar 1e-6); spectral-expansion identity dev 9.8e-15; rho =
0.994203 -> rho' = 0.834915; g21 = 7.517; shadows r'_K = -0.000
/ 0.2883 / 0.2994 / 0.3015 / 0.3027 (K = 1/2/3/5/10); bare
shadow ratio 0.0341, RESTATEMENT median dev 0.9997 (does NOT
fire: the dressing is real content, not a lambda_max read-off);
rest-top PR 1.78, mass 0.9807 at folds (6, 8).  EXT3 BLIND ROWS
(first sight of the dressed column on the r329 anchors): r'_det
0.1605 (kz56) .. 0.4893 (kz128), all 12 inside the band -- THE
KLEIN-GAP BREAKER kz56 BREAKS THE BARE R2 BAND (1.836) BUT NOT
THE DRESSED FLATNESS (0.1605, g21 16.0): the dressing absorbs
exactly the family effect that breaks the bare 2x2 uniformity.
IDENTITY LADDER on all 75 rows: det 1e-12 / Schur logdet 1e-6 /
resolvent route 1e-6 / spectral expansion 1e-9 all green;
concentration blind clause 57/57.  MP WARDS (r342 route): d/c
devs 4.3e-14..8.7e-11, m2 devs 1.4e-10 (w9)..1.9e-4 (kz130);
staffel dps 30/45 dev 0.0.  FRACTION WARDS: JF9 dev 1.6e-14,
I2 dev 0.0 (bar 1e-10); minors criterion == f64 sign on both
(JF9 False at lambda_rest 1.6656, I2 True at 0.5382).  WORLDS:
kappa_int EPST 1793.99 / SCR 8.509e6 / SMOOTH 2.193 / HL2
1964.35 == r334/r342 records at 5 percent, MAIN/TWIN 0.999567.
HONEST NEGATIVES: (1) the sealed FLAT clause failed on the
halves-curvature bar -- the letter of record is
DRESSED_RESERVE_DECAYS(soft) even though no hard kill fired and
no family broke the band: the flatness reading survives only as
census, and a curvature-aware flatness test is R344 protocol
material (defined BEFORE the next record, not retrofitted
here); (2) the R2-R4 certificate chain is measured DEAD on all
75 rows -- Leg C closes with a typed question, not a bound; (3)
the EXT4 rows are disclosed-seen (s3), only the EXT3 rows carry
blind weight -- and they carried it 12/12; (4) the cascade
concentration breaks at level 4 on w9 -- the peeling recursion
is a level-2 statement, not an induction; (5) kz44 rest-pair
mass 0.6917 is the honest minimum behind the 0.9902 median.
R344 SKETCH (PRIME.LSTAR.GAP_RATIO.01 candidate): the top-2
reduction is now gated -- promote the gap ratio g21 and the
top-2 eigenvector 2x2 at the pair to primary coordinates: (i)
their source anatomy (why is 1-lambda_2 ~ 8 x (1-lambda_1)
ladder-wide, and why does kz56 sit at 16 with the reserve
unmoved?), (ii) a curvature-honest flatness protocol for O(1)
columns (scatter-aware, sealed a priori), (iii) the peeling
spectrum: the level-k lambda_rest_k cascade vs the E-spectrum
(the cascade IS the spectrum read through Schur -- w9 numbers
above), (iv) the honest kill: does g21 break on rungs where the
pair concentration weakens (kz44/kz59-type)?  Runtime 147.4 /
141.6 s record, 141.1 s calibration, 0.6 s smoke;
deterministic, run1/run2 byte-identical up to WALL.  AMENDMENTS
AFTER FREEZE: NONE except this record-table insertion.

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
import ext3_fresh_anchors_probe as E3            # noqa: E402 r329
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
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
SHALLOW_FOLDS = (2, 4)
PX_SHA_PREFIX = "b09f8ccd"
E3_SHA_PREFIX = "bbfaf199"
W9_DC_TOL = 2e-5    # 6-decimal record print precision
W9_ANCH = dict(d1=0.970014, d2=0.964904, c=0.032252,
               rdet=1.1561e-2, m2=1.8749e-4, lam_rest=0.996338,
               d1p=0.999154, d2p=0.998710, cp=0.000872,
               rdetp=0.3029)
KZ130_ANCH = dict(d1=0.99374973, d2=0.98989097, c=0.00794884,
                  rdet=2.017e-6, m2=7.789e-9, margin=4.918e-9,
                  R2=0.584, pmass=0.9814)
R2_COHORT_MED = dict(core42=0.205, ext15=0.188, ext3B=0.437,
                     ext3A=0.557)
R2_COHORT_TOL = 0.01
KZ56_R2 = 1.836
KZ56_R2_TOL = 0.01
EXT3_MARGIN_MIN = 4.20e-9
EXT3_MARGIN_MIN_KZ = 127
EXT3_MARGIN_MIN_TOL = 0.05
FIT_ANCH = dict(p=-0.754, q=-0.645, c=-0.697, m2=-3.341,
                margin=-3.332, restm=-3.276, rdetp=0.018)
FIT_ANCH_TOL = 0.02
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
HL2_SEED = 101
HL2_FLIP = 25
EXT = 8
KINT_REC = {"EPST": 1793.99, "SCR": 8.51e6, "SMOOTH": 2.193,
            "HL2": 1964.0}
KINT_REC_TOL = 0.05
KINT_LIVE_REC = 0.999567
KINT_LIVE_TOL = 1.0e-3
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN, EXT3_NW_MAX = 1721, 2577
EXT4_H_MAX = 3400
K_EXT4 = 3
Z2_CAP = 400000
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT4_NW_MIN, EXT4_NW_MAX = 2656, 3181
USED_EXPECT = 92
FRESH_EXPECT = 23
CORE_Z = (16, 317)
MASS_BAR = 0.90
R2_MAX = 1.5
DET_ID_BAR = 1.0e-12
INTERLACE_TOL = 1.0e-9
SCHUR_BAR = 1.0e-6
RES_ROUTE_BAR = 1.0e-6
SPECTRAL_BAR = 1.0e-9
FLAT_BAR = 0.15
DECAY_SLOPE = 0.30
CURV_BAR = 0.35
BAND = 0.5
EXT3_OK_MIN = 10
EXT3_LOW_KILL = 4
EXT4_LOW_KILL = 3
RDETP_FLOOR = 0.01
RESTATE_BAR = 0.05
TOP2_BAR = 0.15
KRES_BAR = 0.10
KRES_LIST = (1, 2, 3, 5, 10)
K_LIST = (0, 1, 3, 8, 32)
DELTA_BAR = 0.05
KERNEL_CLOSED_FORM = False   # sealed: r342 negative #4 stands
PEEL_MASS_BAR = 0.90
PEEL_R2_FLOOR = 0.05
PEEL_CASCADE = 6
SAMPLE_KZ = (18, 9, 52, 119, 42, 130)
DIGAMMA_BAR = 0.02
V_BAR = 0.10
MP_SET = ((9, 30), (9, 45), (52, 30), (130, 30))
MP_DC_CORE = 1.0e-9
MP_DC_EXT3 = 1.0e-8
MP_M2_CORE = 1.0e-6
MP_M2_EXT = 1.0e-5
MP_M2_EXT3 = 1.0e-3
STAFFEL_BAR = 1.0e-12
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
FRAC_BAR = 1.0e-10
TOY_TOL = 1.0e-12
MUT_MASS_BAR = 0.5
M4_BAR = 1.0
M5_BAR = 0.1
MUT_MIN = 1.0e-6

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
                       "/ weight / position arrays ONLY; record "
                       "numbers and flips enter gates and record "
                       "tables only"
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


CONSTRUCTORS = ("resolvent_pair_corr", "rest_expand",
                "dressing_from_expand", "certified_bound",
                "topk_shadow", "shadow_bare", "rest_pair_stats",
                "ext4_domain_fresh")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "KINT_REC", "FIT_ANCH",
                   "W9_ANCH", "KZ130_ANCH",
                   "slope_fit_true", "lam_true"}


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
def resolvent_pair_corr(E, i1, i2):
    """the resolvent-correlation route: M = pair block of
    (I-E)^{-1}; returns (1 - M12^2/(M11 M22), M).  Consumes the
    kernel Gram only."""
    n = E.shape[0]
    Minv = np.linalg.inv(np.eye(n) - E)
    M = Minv[np.ix_([i1, i2], [i1, i2])]
    return 1.0 - M[0, 1] ** 2 / (M[0, 0] * M[1, 1]), M


def rest_expand(E, i1, i2):
    """rest-block eigenpairs + coupling projections: returns
    (delta sorted desc, alpha, beta, rest index list); consumes
    the kernel Gram only."""
    n = E.shape[0]
    rest = [k for k in range(n) if k != i1 and k != i2]
    D = E[np.ix_(rest, rest)]
    dv, WD = np.linalg.eigh(D)
    al = WD.T @ E[i1, rest]
    be = WD.T @ E[i2, rest]
    o = np.argsort(dv)[::-1]
    return dv[o], al[o], be[o], rest, D, WD


def dressing_from_expand(dv, al, be):
    """the EXACT spectral decomposition of the dressing:
    (Delta d1, Delta d2, Delta c) = sums over rest modes."""
    g = 1.0 - dv
    return (float(np.sum(al * al / g)), float(np.sum(be * be / g)),
            float(np.sum(al * be / g)))


def certified_bound(p, q, c, dv, al, be, K):
    """the K-split relaxation bound r'_lb(K): top-K rest modes
    exact, tail by the operator norm; sign relaxation |c'| <=
    |c| + Delta_c_ub.  Returns -inf when the diagonal bound
    already fails."""
    K = min(K, len(dv))
    g = 1.0 - dv
    h1 = float(np.sum(al[:K] ** 2 / g[:K]))
    h2 = float(np.sum(be[:K] ** 2 / g[:K]))
    hc = float(np.sum(np.abs(al[:K] * be[:K]) / g[:K]))
    t1 = math.sqrt(float(np.sum(al[K:] ** 2)))
    t2 = math.sqrt(float(np.sum(be[K:] ** 2)))
    gap = g[K] if K < len(dv) else 1.0
    d1u = h1 + t1 * t1 / gap
    d2u = h2 + t2 * t2 / gap
    dcu = hc + t1 * t2 / gap
    plb = p - d1u
    qlb = q - d2u
    if plb <= 0.0 or qlb <= 0.0:
        return float("-inf")
    return 1.0 - (abs(c) + dcu) ** 2 / (plb * qlb)


def topk_shadow(ev, W, i1, i2, K):
    """the top-K resolvent shadow: the correlation reserve of the
    K-mode truncation of (I-E)^{-1} at the pair."""
    idx = np.argsort(ev)[::-1][:K]
    g = 1.0 - ev[idx]
    M11 = float(np.sum(W[i1, idx] ** 2 / g))
    M22 = float(np.sum(W[i2, idx] ** 2 / g))
    M12 = float(np.sum(W[i1, idx] * W[i2, idx] / g))
    return 1.0 - M12 ** 2 / (M11 * M22)


def shadow_bare(p, q, margin):
    """the bare lambda shadow: what r'_det would be if the
    dressing carried no content beyond lambda_max and the bare
    scalars (the exact 2x2 identity with m2 -> margin)."""
    return margin * (p + q - margin) / (p * q)


def rest_pair_stats(D, WD, yn_rest, L):
    """rest-top-eigenvector census: PR, mass on the two largest-x
    rest atoms, their folds, their indices (in rest order)."""
    wt = WD[:, -1]
    pr = 1.0 / float(np.sum(wt ** 4))
    o = np.argsort(np.asarray(yn_rest, float))[::-1]
    j1, j2 = int(o[0]), int(o[1])
    mass2 = float(wt[j1] ** 2 + wt[j2] ** 2)
    f1 = int(round(math.acos(min(max(yn_rest[j1], -1.0), 1.0))
                   * L / (2.0 * math.pi)))
    f2 = int(round(math.acos(min(max(yn_rest[j2], -1.0), 1.0))
                   * L / (2.0 * math.pi)))
    return pr, mass2, (f1, f2), j1, j2


def ext4_domain_fresh(pool, used, zz, cap):
    """the domain-capped fresh pool: pool minus used, z^2 <= cap
    (the family's von Mangoldt table cap -- windows beyond it
    have a truncated source comb).  Consumes shape + grid only."""
    return [(h, kz) for (h, kz) in pool
            if kz not in used and zz[kz] * zz[kz] <= cap]


# ============== must-fail mutants
def mutant_wrong_block(vn):
    """m1 MUST-FAIL: the dressing at the WRONG block (two
    largest-v atoms) -- CAUGHT by the concentration check."""
    o = np.argsort(np.asarray(vn, float))[::-1]
    return int(o[0]), int(o[1])


def mutant_rdetp_readback():
    """m2 MUST-FAIL: an 'r-prime value' read off the withheld
    lambda record -- the scope audit must FLAG this."""
    return 1.0 - REC_LAM


def mutant_flatbar_posthoc(slope_fit_true):
    """m3 MUST-FAIL: the flatness bar re-picked AFTER SIGHT of
    the fit -- consumes the withheld slope; AST-FLAGGED, and the
    toy value differs from the sealed FLAT_BAR."""
    return abs(slope_fit_true) * 1.5


def mutant_double_dress(E, i1, i2):
    """m4 MUST-FAIL: 'det(I-E) == det(I-A') det(I-D'')' with BOTH
    blocks dressed -- double-counts the coupling; must break the
    exact logdet identity loudly (log-units)."""
    n = E.shape[0]
    rest = [k for k in range(n) if k != i1 and k != i2]
    A = E[np.ix_([i1, i2], [i1, i2])]
    C = E[np.ix_([i1, i2], rest)]
    D = E[np.ix_(rest, rest)]
    Ad = A + C @ np.linalg.solve(np.eye(len(rest)) - D, C.T)
    Dd = D + C.T @ np.linalg.solve(np.eye(2) - A, C)
    _s1, ld_a = np.linalg.slogdet(np.eye(2) - Ad)
    _s2, ld_d = np.linalg.slogdet(np.eye(len(rest)) - Dd)
    _s3, ld_f = np.linalg.slogdet(np.eye(n) - E)
    return abs((ld_a + ld_d) - ld_f)


def mutant_corr_of_E(E, i1, i2):
    """m5 MUST-FAIL: the correlation reserve read off E itself
    instead of (I-E)^{-1} -- must differ loudly from r'_det."""
    return 1.0 - E[i1, i2] ** 2 / (E[i1, i1] * E[i2, i2])


# ============== gate-side helpers
def extend_rung(R):
    """the r343 extension of one r342 rung bundle: resolvent
    route, spectral expansion, anatomy, bounds, shadows, peeling
    coordinates."""
    B = R["B"]
    E = B @ B.T
    i1, i2 = R["i1"], R["i2"]
    r_res, Mres = resolvent_pair_corr(E, i1, i2)
    ev, W = np.linalg.eigh(E)
    g21 = (1.0 - float(ev[-2])) / (1.0 - float(ev[-1]))
    dv, al, be, rest, D, WD = rest_expand(E, i1, i2)
    dd1, dd2, dc = dressing_from_expand(dv, al, be)
    dev_sp = max(
        abs(dd1 - (R["d1p"] - R["d1"]))
        / max(abs(R["d1p"] - R["d1"]), 1e-300),
        abs(dd2 - (R["d2p"] - R["d2"]))
        / max(abs(R["d2p"] - R["d2"]), 1e-300),
        abs(dc - (R["cp"] - R["c"]))
        / max(abs(R["cp"] - R["c"]), 1e-300))
    dev_res = abs(r_res - R["rdetp"]) / max(abs(R["rdetp"]), 1e-300)
    contrib = al * al / (1.0 - dv)
    oC = np.argsort(contrib)[::-1]
    top1 = float(contrib[oC[0]]) / max(dd1, 1e-300)
    top3 = float(np.sum(contrib[oC[:3]])) / max(dd1, 1e-300)
    lam2p = PX.pair_eigs(R["d1p"], R["d2p"], R["cp"])[0]
    m2p = 1.0 - lam2p
    pp = 1.0 - R["d1p"]
    qp = 1.0 - R["d2p"]
    rho = R["c"] / math.sqrt(R["p"] * R["q"])
    rhop = R["cp"] / math.sqrt(pp * qp)
    bounds = {K: certified_bound(R["p"], R["q"], R["c"],
                                 dv, al, be, K) for K in K_LIST}
    r_r2 = 1.0 - (abs(R["c"]) + abs(dc)) ** 2 / (pp * qp)
    shadows = {K: topk_shadow(ev, W, i1, i2, K) for K in KRES_LIST}
    k_res = 99
    for K in KRES_LIST:
        if abs(shadows[K] - R["rdetp"]) \
                <= KRES_BAR * abs(R["rdetp"]):
            k_res = K
            break
    r_sh = shadow_bare(R["p"], R["q"], R["margin"])
    yn_rest = np.asarray(R["mz"]["yn"], float)[rest]
    pr_rest, mass2, folds2, j1, j2 = rest_pair_stats(
        D, WD, yn_rest, R["mz"]["L"])
    Ad2, lam_rest2, _sr, _sf = PX.schur_dress(D, j1, j2)
    _p2, _q2, r2det = PX.det_reserve(
        float(Ad2[0, 0]), float(Ad2[1, 1]),
        float(0.5 * (Ad2[0, 1] + Ad2[1, 0])))
    u1 = E[i1, rest]
    f_rest = np.round(np.arccos(np.clip(yn_rest, -1.0, 1.0))
                      * R["mz"]["L"] / (2.0 * math.pi)).astype(int)
    u_rest = f_rest * R["mz"]["D"]
    m_arch = u_rest < math.log(2.0)
    arch_share = float(np.sum(u1[m_arch] ** 2)) \
        / max(float(np.sum(u1 ** 2)), 1e-300)
    return dict(E=E, ev=ev, W=W, r_res=r_res, dev_res=dev_res,
                dev_sp=dev_sp, dd1=dd1, dd2=dd2, dc=dc, g21=g21,
                top1=top1, top3=top3, m2p=m2p,
                m2p_ratio=(m2p / R["margin"]
                           if R["margin"] > 0 else float("nan")),
                pp=pp, qp=qp, rho=rho, rhop=rhop, bounds=bounds,
                r_r2=r_r2, shadows=shadows, k_res=k_res, r_sh=r_sh,
                pr_rest=pr_rest, mass2=mass2, folds2=folds2,
                lam_rest2=lam_rest2, r2det=r2det,
                arch_share=arch_share, D=D, WD=WD, rest=rest,
                j1=j1, j2=j2, yn_rest=yn_rest)


def frac_dressed_reserve(name):
    """EXACT-Fractions ward for the dressing on a small rational
    instance: with G the rational mu-CD kernel Gram on the nu
    atoms and E = S G S (S = diag(sqrt v)), the dressed pair block
    is A'_kl = sqrt(v_k v_l) G'_kl with the RATIONAL matrix
    G' = G_pair + G_pair,rest H G_rest,pair,
    H = (diag(1/v_rest) - G_rest)^{-1}; r'_det and the
    lambda_rest < 1 criterion (leading minors of diag(1/v) - G_r
    positive) are exact rationals.  Returns (r'_frac as Fr,
    minors_positive, f64 route value, f64 lambda_rest)."""
    xs, ws, ys, vs, _N, dep = FC.frac_instance(name)
    G = FC.frac_kernel(xs, ws, ys, dep)
    yf = np.array([float(y) for y in ys])
    vf = np.array([float(v) for v in vs])
    i1, i2 = PX.pair_select(yf)
    rest = [k for k in range(len(ys)) if k != i1 and k != i2]
    m = len(rest)
    Amat = [[(1 / vs[rest[a]] if a == b else Fr(0))
             - G[rest[a]][rest[b]] for b in range(m)]
            for a in range(m)]
    # leading minors (lambda_rest < 1 criterion, exact)
    minors_pos = True
    for k in range(1, m + 1):
        sub = [row[:k] for row in Amat[:k]]
        det = _frac_det(sub)
        minors_pos = minors_pos and (det > 0)
    H = []
    for col in range(m):
        e = [Fr(1) if r == col else Fr(0) for r in range(m)]
        H.append(FC.frac_solve(Amat, e))
    # H[col][row]: column of the inverse; symmetric matrix
    Gp = {}
    for (k, l) in ((i1, i1), (i1, i2), (i2, i2)):
        acc = G[k][l]
        for a in range(m):
            for b in range(m):
                acc += G[k][rest[a]] * H[b][a] * G[rest[b]][l]
        Gp[(k, l)] = acc
    d1p = vs[i1] * Gp[(i1, i1)]
    d2p = vs[i2] * Gp[(i2, i2)]
    c2p = vs[i1] * vs[i2] * Gp[(i1, i2)] * Gp[(i1, i2)]
    r_frac = 1 - c2p / ((1 - d1p) * (1 - d2p))
    # f64 route
    a_, b_, h0_ = V.mu_chain(np.array([float(x) for x in xs]),
                             np.array([float(w) for w in ws]), dep)
    Bf = V.b_matrix(a_, b_, h0_, yf, vf, dep)
    Ef = Bf @ Bf.T
    Ad, lr_f64, _s1, _s2 = PX.schur_dress(Ef, i1, i2)
    _pp, _qq, r_f64 = PX.det_reserve(
        float(Ad[0, 0]), float(Ad[1, 1]),
        float(0.5 * (Ad[0, 1] + Ad[1, 0])))
    return r_frac, minors_pos, r_f64, lr_f64


def _frac_det(M):
    """rational determinant by fraction-free elimination."""
    n = len(M)
    M = [list(r) for r in M]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0),
                   None)
        if piv is None:
            return Fr(0)
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            det = -det
        det *= M[col][col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(col + 1, n):
            f = M[r][col]
            if f != 0:
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
    return det


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("pair_coupling_probe -- PRIME.LSTAR.PAIR_COUPLING.01 "
          "(round 343)")
    print("SPEC_SHA %s   (r342 PX %s / r329 E3 %s / r334 FC %s)"
          % (SPEC_SHA[:16], PX.SPEC_SHA[:16], E3.SPEC_SHA[:16],
             FC.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 block; ladder, EXT3/EXT4, twin, mp "
                        "wards, fits, worlds, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: the r342 machinery imported "
          "verbatim (SPEC_SHA %s == %s*), the r329 selection "
          "machinery (%s == %s*), the resolvent/expansion/bound/"
          "shadow constructors, the EXT4 rule with its domain cap "
          "z^2 <= %d, the DISCLOSED PRIORS (rdetp slope %+.3f, "
          "restm %.3f, w9 r'_det %.4f), the sealed fit rules "
          "(FLAT_BAR %.2f, DECAY_SLOPE %.2f, CURV_BAR %.2f, band "
          "%.1f dec), every bar/tolerance, the mutants and the "
          "verdict form; pre-spec scoping s1-s3 disclosed in the "
          "spec (w9 extension, the kz277 domain fact, the six "
          "EXT4 rows seen); the STOP list forbids any L* claim "
          "and any certificate reading"
          % (PX.SPEC_SHA[:8], PX_SHA_PREFIX, E3.SPEC_SHA[:8],
             E3_SHA_PREFIX, Z2_CAP, FIT_ANCH["rdetp"],
             FIT_ANCH["restm"], W9_ANCH["rdetp"], FLAT_BAR,
             DECAY_SLOPE, CURV_BAR, BAND))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m2 = scope_audit("mutant_rdetp_readback")
    hits_m3 = scope_audit("mutant_flatbar_posthoc")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m2) and bool(hits_m3),
          "the %d module-own constructors consume kernel Gram / "
          "spectrum / weight / position arrays ONLY (%s); fragment "
          "audit (no fit primitives beyond the imported r286 "
          "Theil-Sen): %s; m2 FLAGGED (%s); m3 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- RESOLVENT IDENTITY + EXPANSION + BOUND + "
            "SHADOWS + FRACTIONS")
    # 3x3 hand toy (r342 matrix), exact Fractions
    E3t = np.array([[0.25, 0.125, 1.0 / 16.0],
                    [0.125, 0.5, 1.0 / 32.0],
                    [1.0 / 16.0, 1.0 / 32.0, 0.125]])
    a11, a12, a22 = Fr(1, 4), Fr(1, 8), Fr(1, 2)
    c1_, c2_, dd_ = Fr(1, 16), Fr(1, 32), Fr(1, 8)
    inv_ = 1 / (1 - dd_)
    d1p_ex = a11 + c1_ * c1_ * inv_
    d2p_ex = a22 + c2_ * c2_ * inv_
    cp_ex = a12 + c1_ * c2_ * inv_
    r_ex = 1 - cp_ex * cp_ex / ((1 - d1p_ex) * (1 - d2p_ex))
    r_res3, M3 = resolvent_pair_corr(E3t, 0, 1)
    # exact rational (I-E)^{-1} pair block
    IE = [[Fr(3, 4), Fr(-1, 8), Fr(-1, 16)],
          [Fr(-1, 8), Fr(1, 2), Fr(-1, 32)],
          [Fr(-1, 16), Fr(-1, 32), Fr(7, 8)]]
    cols = []
    for col in range(3):
        e = [Fr(1) if r == col else Fr(0) for r in range(3)]
        cols.append(FC.frac_solve(IE, e))
    M_ex = [[cols[b][a] for b in range(2)] for a in range(2)]
    r_res_ex = 1 - M_ex[0][1] * M_ex[0][1] / (M_ex[0][0]
                                              * M_ex[1][1])
    dv3, al3, be3, _r3, _D3, _W3 = rest_expand(E3t, 0, 1)
    dd13, dd23, dc3 = dressing_from_expand(dv3, al3, be3)
    ok_t1 = (abs(r_res3 - float(r_ex)) <= TOY_TOL
             and abs(float(r_res_ex) - float(r_ex)) == 0
             and abs(dd13 - float(c1_ * c1_ * inv_)) <= TOY_TOL
             and abs(dc3 - float(c1_ * c2_ * inv_)) <= TOY_TOL
             and abs(float(M3[0, 0]) - float(M_ex[0][0]))
             <= TOY_TOL)
    # aligned-sign bound == exact on the toy (1-dim rest, c>0)
    b_full = certified_bound(0.75, 0.5, 0.125, dv3, al3, be3, 1)
    ok_t1b = abs(b_full - float(r_ex)) <= TOY_TOL
    check("G10-toy-resolvent-identity", ok_t1 and ok_t1b,
          "3x3 HAND TOY: r'_det == 1 - M12^2/(M11 M22) with M = "
          "pair block of (I-E)^{-1}, f64 AND exact Fractions == "
          "the Schur value %s; spectral expansion (1-dim rest) "
          "Delta d1 == c1^2/(1-d) exact; ALIGNED-SIGN bound "
          "r'_lb(full) == r'_det exact (%.12f) -- the relaxation "
          "chain is tight when nothing cancels"
          % (str(r_ex), b_full))
    ev3, W3 = np.linalg.eigh(E3t)
    sh3 = topk_shadow(ev3, W3, 0, 1, 3)
    ok_t2 = abs(sh3 - float(r_ex)) <= TOY_TOL
    r_sh_toy = shadow_bare(0.75, 0.5, 1.0 - PX.pair_eigs(
        0.25, 0.5, 0.125)[0])
    rd_toy = PX.det_reserve(0.25, 0.5, 0.125)[2]
    ok_t3 = abs(r_sh_toy - rd_toy) <= TOY_TOL
    check("G11-toy-shadows", ok_t2 and ok_t3,
          "FULL-K SPECTRAL SHADOW == r'_det on the 3x3 (dev %.1e) "
          "-- the top-K truncation converges to the resolvent "
          "identity; BARE SHADOW on a pure 2x2 (no rest): "
          "margin (p+q-margin)/(pq) == r_det exact (%.12f == "
          "%.12f) -- the RESTATEMENT formula is the exact 2x2 "
          "identity" % (abs(sh3 - float(r_ex)), r_sh_toy, rd_toy))
    # block-diagonal peel toy
    E4t = np.zeros((4, 4))
    E4t[:2, :2] = [[0.25, 0.125], [0.125, 0.5]]
    E4t[2:, 2:] = [[0.3, 0.05], [0.05, 0.2]]
    Ad4, lr4, _s1, _s2 = PX.schur_dress(E4t, 0, 1)
    r4 = PX.det_reserve(float(Ad4[0, 0]), float(Ad4[1, 1]),
                        float(0.5 * (Ad4[0, 1] + Ad4[1, 0])))[2]
    lr_ex = float(np.linalg.eigvalsh(
        np.array([[0.3, 0.05], [0.05, 0.2]]))[-1])
    ok_t4 = (abs(r4 - rd_toy) <= TOY_TOL
             and abs(lr4 - lr_ex) <= TOY_TOL)
    check("G12-toy-block-diagonal", ok_t4,
          "BLOCK-DIAGONAL 4x4 (no coupling): dressed reserve == "
          "bare reserve exact (%.12f), lambda_rest == "
          "lambda_max(rest block) exact -- the dressing is "
          "inert when the coupling vanishes" % r4)
    # Fractions ward on JF9 + I2
    devs_fr = {}
    ok_minor = True
    minor_txt = {}
    for nm in ("I1", "I2"):
        r_frac, minors_pos, r_f64, lr_f64 = \
            frac_dressed_reserve(nm)
        devs_fr[nm] = abs(r_f64 - float(r_frac)) \
            / max(abs(float(r_frac)), 1e-300)
        # the rational minors criterion must AGREE with the f64
        # lambda_rest sign (the instances need not satisfy it)
        ok_minor = ok_minor and (minors_pos == (lr_f64 < 1.0))
        minor_txt[nm] = "%s (lam_rest %.4f)" % (minors_pos, lr_f64)
    check("G13-toy-fraction-ward", ok_minor
          and max(devs_fr.values()) <= FRAC_BAR,
          "EXACT-FRACTIONS DRESSING WARD (rational H = "
          "(diag(1/v_r) - G_r)^{-1} route on the r334 instances): "
          "JF9 dev %.1e, I2 dev %.1e (bar %.0e); the EXACT "
          "leading-minors criterion for lambda_rest < 1 agrees "
          "with the f64 sign on both (JF9 %s, I2 %s) -- the "
          "dressed reserve and the rest-clause criterion are "
          "route-independent at rational arithmetic grade"
          % (devs_fr["I1"], devs_fr["I2"], FRAC_BAR,
             minor_txt["I1"], minor_txt["I2"]))
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
    section("S2  W9 -- ANCHORS + RESOLVENT + ANATOMY + BOUNDS + "
            "SHADOWS + PEEL")
    R9 = PX.build_rung(MAIN_KZ)
    X9 = extend_rung(R9)
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
    ok_anch = ((R9["f1"], R9["f2"]) == SHALLOW_FOLDS
               and abs(R9["d1"] / A["d1"] - 1.0) <= 2e-5
               and abs(R9["d2"] / A["d2"] - 1.0) <= 2e-5
               and abs(R9["c"] / A["c"] - 1.0) <= 2e-5
               and abs(R9["rdet"] / A["rdet"] - 1.0) <= 1e-3
               and abs(R9["m2"] / A["m2"] - 1.0) <= 1e-3
               and abs(R9["lam_rest"] - A["lam_rest"]) <= 1e-5
               and abs(R9["d1p"] / A["d1p"] - 1.0) <= 1e-5
               and abs(R9["d2p"] / A["d2p"] - 1.0) <= 1e-5
               and abs(R9["cp"] - A["cp"]) <= 2e-6
               and abs(R9["rdetp"] / A["rdetp"] - 1.0) <= 1e-3)
    check("G21-w9-r342-anchors", ok_anch,
          "LEG 0 BIT-NEAR: pair folds %s == (2, 4); (d1, d2, c) "
          "= (%.6f, %.6f, %.6f) == r342 record; r_det %.4e, m2 "
          "%.4e; Schur row lambda_rest %.6f, dressed (%.6f, "
          "%.6f, %.6f), r'_det %.6f == r342 record %.4f -- the "
          "R343 coordinates start exactly where r342 left them"
          % (str((R9["f1"], R9["f2"])), R9["d1"], R9["d2"],
             R9["c"], R9["rdet"], R9["m2"], R9["lam_rest"],
             R9["d1p"], R9["d2p"], R9["cp"], R9["rdetp"],
             A["rdetp"]))
    check("G22-w9-resolvent-identity", X9["dev_res"] <= RES_ROUTE_BAR
          and R9["det_dev"] <= DET_ID_BAR
          and R9["schur_dev"] <= SCHUR_BAR,
          "THE RESOLVENT-CORRELATION IDENTITY: r'_det == 1 - "
          "M12^2/(M11 M22) with M = pair block of (I-E)^{-1}, "
          "independent full-inverse route dev %.1e (bar %.0e); "
          "r342 det/Schur identities re-gated (%.1e / %.1e) -- "
          "the dressed reserve IS the Cauchy-Schwarz reserve of "
          "the resolvent at the pair, exactly"
          % (X9["dev_res"], RES_ROUTE_BAR, R9["det_dev"],
             R9["schur_dev"]))
    check("G23-w9-spectral-expansion", X9["dev_sp"] <= SPECTRAL_BAR,
          "THE EXACT DECOMPOSITION r'_det = f(bare, coupling): "
          "Delta d1 = %.4e (= %.4f p), Delta d2 = %.4e (= %.4f "
          "q), Delta c = %.4e (= %+.4f c) via the rest-eigenmode "
          "sums == direct Schur (dev %.1e, bar %.0e); top-1/"
          "top-3 mode shares of Delta d1: %.3f / %.3f -- the "
          "absorption is multi-mode; ANATOMY: rho = %.6f -> "
          "rho' = %.6f (the dressing eats %.1f%% of the "
          "coupling by SIGNED cancellation), m2'/margin = %.4f, "
          "g21 = (1-lambda_2)/(1-lambda_1) = %.3f"
          % (X9["dd1"], X9["dd1"] / R9["p"], X9["dd2"],
             X9["dd2"] / R9["q"], X9["dc"], X9["dc"] / R9["c"],
             X9["dev_sp"], SPECTRAL_BAR, X9["top1"], X9["top3"],
             X9["rho"], X9["rhop"],
             100.0 * abs(X9["dc"]) / R9["c"], X9["m2p_ratio"],
             X9["g21"]))
    ok_b = all(X9["bounds"][K] <= X9["r_r2"] + 1e-9
               for K in K_LIST) and X9["r_r2"] <= R9["rdetp"]
    check("G24-w9-bound-ladder", ok_b,
          "THE RELAXATION LADDER at w9 (Leg C): r'_lb(K) = %s "
          "(K = %s); sign-only reserve r'_R2 = %.1f vs r'_det "
          "%.4f -- the triangle step |c| + |Delta c| = %.4f "
          "overshoots the cancelled |c'| = %.6f by %.0fx: the "
          "R2-R4 chain is theorem-grade but MEASURED DEAD (the "
          "s1 disclosure, now gated); ladder monotone below "
          "r'_R2 <= r'_det"
          % (str({K: ("%.2f" % v if v > -1e6 else "-inf")
                  for K, v in X9["bounds"].items()}),
             str(K_LIST), X9["r_r2"], R9["rdetp"],
             abs(R9["c"]) + abs(X9["dc"]), abs(R9["cp"]),
             (abs(R9["c"]) + abs(X9["dc"])) / abs(R9["cp"])))
    check("G25-w9-shadows", X9["k_res"] <= 3,
          "TOP-K SHADOWS: r'_K = %s vs r'_det %.4f (K_res = %d "
          "at the %.0f%% bar) -- the dressed reserve is a TOP-2-"
          "DOMINATED spectral object; BARE LAMBDA SHADOW r_shadow "
          "= %.4e = %.4f x r'_det (the RESTATEMENT formula does "
          "NOT reproduce the dressing at w9)"
          % (str({K: round(v, 4) for K, v in X9["shadows"].items()}),
             R9["rdetp"], X9["k_res"], 100 * KRES_BAR, X9["r_sh"],
             X9["r_sh"] / R9["rdetp"]))
    # dictionary sample at w9 (Leg 0 / Leg A source side)
    alpha9, M9, L9, D9, ka9, dd9, dA9, dP9 = PX.layer_split(MAIN_KZ)
    uu9 = np.asarray(V.U[:ka9], float)
    mm9 = np.asarray(V.W_VM[:ka9], float)
    dev_dict = 0.0
    for ff in (R9["f1"], R9["f2"]):
        th = 2.0 * math.pi * ff / L9
        da_c, _da_p = PX.arch_dict_density(th, alpha9, D9)
        dev_dict = max(dev_dict, abs(da_c - float(dA9[ff]))
                       / max(abs(float(dA9[ff])), 1e-300))
    dev_vrest = 0.0
    for jj in (X9["j1"], X9["j2"]):
        ff = int(round(math.acos(min(max(X9["yn_rest"][jj], -1.0),
                                     1.0)) * L9 / (2.0 * math.pi)))
        th = 2.0 * math.pi * ff / L9
        vp, _a, _p = PX.v_predict(th, alpha9, M9, L9, D9, uu9, mm9)
        # actual weight of that rest atom
        vt = float(R9["mz"]["vn"][X9["rest"][jj]])
        dev_vrest = max(dev_vrest, abs(vp - vt) / vt)
    check("G26-w9-dictionary", dev_dict <= DIGAMMA_BAR
          and dev_vrest <= V_BAR,
          "SOURCE SIDE OF THE DRESSING: digamma dictionary at the "
          "pair folds dev %.1e (bar %.2f); the REST-PAIR weights "
          "(the peeling pair, folds %s) dictionary-predicted to "
          "%.1e (bar %.2f); coupling-row arch-rim share "
          "||u1||^2(u < log 2)/||u1||^2 = %.4f (measured, census) "
          "-- the weight side of the dressing is closed-form, the "
          "kernel side stays census-grade (r342 negative #4)"
          % (dev_dict, DIGAMMA_BAR, str(X9["folds2"]), dev_vrest,
             V_BAR, X9["arch_share"]))
    # level-k cascade at w9
    casc = []
    Dk = X9["E"]
    yk = np.asarray(R9["mz"]["yn"], float)
    i1k, i2k = R9["i1"], R9["i2"]
    for lev in range(PEEL_CASCADE):
        Adk, lrk, _s1, _s2 = PX.schur_dress(Dk, i1k, i2k)
        rk = PX.det_reserve(float(Adk[0, 0]), float(Adk[1, 1]),
                            float(0.5 * (Adk[0, 1]
                                         + Adk[1, 0])))[2]
        evk, Wk = np.linalg.eigh(Dk)
        w1k = Wk[:, -1]
        mk = float(w1k[i1k] ** 2 + w1k[i2k] ** 2)
        f1k = int(round(math.acos(min(max(yk[i1k], -1.0), 1.0))
                        * L9 / (2.0 * math.pi)))
        f2k = int(round(math.acos(min(max(yk[i2k], -1.0), 1.0))
                        * L9 / (2.0 * math.pi)))
        casc.append((lev + 1, (f1k, f2k), round(mk, 4),
                     round(rk, 4), round(lrk, 6)))
        restk = [t for t in range(Dk.shape[0])
                 if t != i1k and t != i2k]
        Dk = Dk[np.ix_(restk, restk)]
        yk = yk[restk]
        o = np.argsort(yk)[::-1]
        i1k, i2k = int(o[0]), int(o[1])
    ok_casc = all(c[3] > 0 for c in casc) \
        and all(casc[t][4] > casc[t + 1][4]
                for t in range(len(casc) - 1))
    check("G27-w9-peel-cascade", ok_casc,
          "THE LEVEL-k CASCADE at w9 (level, pair folds, top-vec "
          "pair mass, r'-reserve, lambda_rest_k): %s -- the "
          "reserve stays positive and lambda_rest_k falls "
          "monotonically at every peel; the shallow-pair "
          "CONCENTRATION of the peeled top eigenvector is "
          "measured per level (it need not persist -- census, "
          "the adjudicating peeling clause lives on level 2 "
          "across the ladder)" % str(casc))

    # ---------------- S3 the ladder + EXT3 + EXT4
    section("S3  LEG A/B -- THE DRESSED LADDER (42 + 15 + 12 EXT3 "
            "+ 6 EXT4)")
    if smoke:
        for g in ("G30-ext4-selection", "G31-ladder-census",
                  "G32-ladder-identities", "G33-cohort-anchors"):
            check(g, True, "SMOKE: skipped")
        ROWS, XT = {9: R9}, {9: X9}
        core_kzs, ext_kzs, ext3_kzs, ext4_kzs = [9], [], [], []
        excl = []
    else:
        # sealed EXT4 selection
        lm_rows = LM.ext_rule()
        used = set(E3.used_kz_set(core.frame_a_zones(), lm_rows,
                                  35))
        used |= set(EXT3_KZ_B + EXT3_KZ_A)
        pool = E3.admissible_pool(core.H_MIN, EXT4_H_MAX)
        zz = {kz: int(core._NN[kz]) for (_h, kz) in pool}
        fresh = ext4_domain_fresh(pool, used, zz, Z2_CAP)
        fresh_kz = [kz for (_h, kz) in fresh]
        grels = E3.grel_col(fresh_kz, core.G_ALL)
        gr_by = {kz: g for kz, g in zip(fresh_kz, grels)}
        h_by = {kz: h for (h, kz) in fresh}
        core_kzs = list(V.admissible_indices())
        z_lo = min(int(V.PP[k]) for k in core_kzs)
        z_hi = max(int(V.PP[k]) for k in core_kzs)
        b_q = sorted((kz for kz in fresh_kz
                      if z_lo <= zz[kz] <= z_hi),
                     key=lambda kz: (gr_by[kz], kz))
        b_sel = tuple(b_q[:K_EXT4])
        a_q = [kz for (_h, kz) in sorted(fresh, reverse=True)
               if kz not in set(b_sel)]
        a_sel = tuple(a_q[:K_EXT4])
        ext4_kzs = list(b_sel + a_sel)
        grid_ok = all(int(V.PP[kz]) == int(core._NN[kz])
                      for kz in list(EXT3_KZ_B + EXT3_KZ_A)
                      + ext4_kzs)
        check("G30-ext4-selection",
              len(used) == USED_EXPECT
              and len(fresh) == FRESH_EXPECT
              and (z_lo, z_hi) == CORE_Z
              and b_sel == EXT4_KZ_B and a_sel == EXT4_KZ_A
              and grid_ok,
              "SEALED EXT4 SELECTION executed verbatim: used "
              "ledger %d (== %d), domain-capped fresh %d (== %d, "
              "z^2 <= %d), core zone [%d, %d]; stratum B4 %s "
              "(small-gap in-zone, grel %s) + A4 %s (deepest, h "
              "%s) == the s3-disclosed queues; kz-grid identity "
              "V.PP == core._NN on all 18 EXT3+EXT4 anchors"
              % (len(used), USED_EXPECT, len(fresh), FRESH_EXPECT,
                 Z2_CAP, z_lo, z_hi, str(b_sel),
                 str([round(gr_by[k], 3) for k in b_sel]),
                 str(a_sel),
                 str([h_by[k] for k in a_sel])))
        ext_kzs = [t[1] for t in lm_rows[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ROWS, XT = {}, {}
        print("    %-5s %-5s %-5s %-5s | %-10s %-10s %-9s %-9s | "
              "%-8s %-8s %-8s %-7s | %-7s %-7s %-6s %-6s"
              % ("kz", "z", "S-", "N_w", "margin", "restm",
                 "r_det", "r'_det", "dd1/p", "dc/c", "rho'",
                 "m2'/m", "g21", "mass2", "r2det", "Kres"))
        neg_rows = []
        for kz in core_kzs + ext_kzs + ext3_kzs + ext4_kzs:
            R = R9 if kz == MAIN_KZ else PX.build_rung(kz)
            X = X9 if kz == MAIN_KZ else extend_rung(R)
            ROWS[kz], XT[kz] = R, X
            if R["margin"] <= 0:
                neg_rows.append(kz)
            print("    %-5d %-5d %-5d %-5d | %.4e %.4e %.3e "
                  "%.3e | %8.4f %+8.4f %8.4f %7.4f | %7.3f "
                  "%7.4f %6.4f %6d"
                  % (kz, R["z"], R["Sm"], R["Nw"], R["margin"],
                     1.0 - R["lam_rest"], R["rdet"], R["rdetp"],
                     X["dd1"] / R["p"], X["dc"] / R["c"],
                     X["rhop"], X["m2p_ratio"], X["g21"],
                     X["mass2"], X["r2det"], X["k_res"]),
                  flush=True)
        excl = list(neg_rows)   # contingency: excluded from fits
        ok_cen = (len(core_kzs) == 42
                  and all(EXT3_NW_MIN <= ROWS[k]["Nw"]
                          <= EXT3_NW_MAX for k in ext3_kzs)
                  and all(EXT4_NW_MIN <= ROWS[k]["Nw"]
                          <= EXT4_NW_MAX for k in ext4_kzs)
                  and min(ROWS[k]["Nw"] for k in ext4_kzs)
                  == EXT4_NW_MIN
                  and max(ROWS[k]["Nw"] for k in ext4_kzs)
                  == EXT4_NW_MAX)
        check("G31-ladder-census", ok_cen and not neg_rows,
              "42 core + 15 r286 extension + 12 EXT3 (N_w %d..%d) "
              "+ 6 EXT4 (N_w %d..%d exact -- the deepest windows "
              "ever measured in the L* lane); every f64 margin "
              "positive (contingency rows: %s)"
              % (EXT3_NW_MIN, EXT3_NW_MAX, EXT4_NW_MIN,
                 EXT4_NW_MAX,
                 str(neg_rows) if neg_rows else "none"))
        all_kz = core_kzs + ext_kzs + ext3_kzs + ext4_kzs
        kz57 = core_kzs + ext_kzs
        ok_id = all(ROWS[k]["det_dev"] <= DET_ID_BAR
                    and ROWS[k]["schur_dev"] <= SCHUR_BAR
                    and ROWS[k]["margin"] <= ROWS[k]["m2"]
                    + INTERLACE_TOL
                    and XT[k]["dev_res"] <= RES_ROUTE_BAR
                    and XT[k]["dev_sp"] <= SPECTRAL_BAR
                    and (ROWS[k]["m2"] > 0) == (ROWS[k]["rdet"] > 0)
                    for k in all_kz)
        conc57 = [k for k in kz57
                  if ROWS[k]["pmass"] < MASS_BAR
                  or ROWS[k]["R2"] is None
                  or not (0.0 <= ROWS[k]["R2"] <= R2_MAX)]
        check("G32-ladder-identities", ok_id and not conc57,
              "per-rung identities on all %d rows: determinant + "
              "Schur logdet + interlacing (r342 bars) AND the NEW "
              "resolvent-route identity (<= %.0e) AND the "
              "spectral-expansion identity (<= %.0e); "
              "concentration BLIND clause on the 57: %s; r'_det "
              "range %.4f..%.4f over all rows, lambda_rest "
              "margins all positive: %s"
              % (len(all_kz), RES_ROUTE_BAR, SPECTRAL_BAR,
                 "57/57" if not conc57 else "BROKEN "
                 + str(conc57),
                 min(ROWS[k]["rdetp"] for k in all_kz),
                 max(ROWS[k]["rdetp"] for k in all_kz),
                 all(ROWS[k]["lam_rest"] < 1.0 for k in all_kz)))

        def med(vals):
            return float(np.median(np.asarray(vals, float)))

        cohR2 = dict(
            core42=med([ROWS[k]["R2"] for k in core_kzs]),
            ext15=med([ROWS[k]["R2"] for k in ext_kzs]),
            ext3B=med([ROWS[k]["R2"] for k in EXT3_KZ_B]),
            ext3A=med([ROWS[k]["R2"] for k in EXT3_KZ_A]))
        ok_coh = all(abs(cohR2[nm] - R2_COHORT_MED[nm])
                     <= R2_COHORT_TOL for nm in cohR2)
        R130 = ROWS[130]
        ok_130 = (abs(R130["d1"] / KZ130_ANCH["d1"] - 1.0) <= 1e-7
                  and abs(R130["d2"] / KZ130_ANCH["d2"] - 1.0)
                  <= 1e-7
                  and abs(R130["c"] / KZ130_ANCH["c"] - 1.0)
                  <= 1e-5
                  and abs(R130["rdet"] / KZ130_ANCH["rdet"] - 1.0)
                  <= 2e-2
                  and abs(R130["m2"] / KZ130_ANCH["m2"] - 1.0)
                  <= 2e-2
                  and abs(R130["margin"] / KZ130_ANCH["margin"]
                          - 1.0) <= 2e-2
                  and abs(R130["R2"] - KZ130_ANCH["R2"]) <= 5e-3
                  and abs(R130["pmass"] - KZ130_ANCH["pmass"])
                  <= 5e-3)
        m_min_kz = min(ext3_kzs, key=lambda k: ROWS[k]["margin"])
        ok_m_min = (m_min_kz == EXT3_MARGIN_MIN_KZ
                    and abs(ROWS[m_min_kz]["margin"]
                            / EXT3_MARGIN_MIN - 1.0)
                    <= EXT3_MARGIN_MIN_TOL)
        ok_56 = abs(ROWS[56]["R2"] - KZ56_R2) <= KZ56_R2_TOL
        check("G33-cohort-anchors", ok_coh and ok_130 and ok_m_min
              and ok_56,
              "LEG 0 COHORT ANCHORS: R2 medians %s == r342 record "
              "%s (tol %.2f); kz130 s3 row bit-near (d/c/rdet/m2/"
              "margin/R2/pmass); EXT3 margin min at kz%d == "
              "%.2e (rel %.2f); kz56 R2 = %.3f == %.3f -- the "
              "Klein-gap breaker reproduced"
              % (str({k: round(v, 3) for k, v in cohR2.items()}),
                 str(R2_COHORT_MED), R2_COHORT_TOL, m_min_kz,
                 EXT3_MARGIN_MIN, EXT3_MARGIN_MIN_TOL,
                 ROWS[56]["R2"], KZ56_R2))

    # ---------------- S4 twin + mp wards
    section("S4  TWIN + MP PRECISION WARDS")
    if smoke:
        for g in ("G40-twin", "G41-mp-wards"):
            check(g, True, "SMOKE: skipped")
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
        u2, m2c, _dens, _du = AKD.twin_rational(uu9c, mm9c, gaps9,
                                                mz9["D"], TWIN_TOL)
        mzT = TR.build_world(9, u2, m2c)
        aT, bT, h0T = V.mu_chain(mzT["xp"], mzT["wp"], mzT["Nw"])
        BT = V.b_matrix(aT, bT, h0T, mzT["yn"], mzT["vn"],
                        mzT["Nw"])
        ET = BT @ BT.T
        t1_, t2_ = PX.pair_select(mzT["yn"])
        AdT, lrT, _s1, _s2 = PX.schur_dress(ET, t1_, t2_)
        rT = PX.det_reserve(float(AdT[0, 0]), float(AdT[1, 1]),
                            float(0.5 * (AdT[0, 1]
                                         + AdT[1, 0])))[2]
        devT = max(abs(float(AdT[0, 0]) - R9["d1p"]) / R9["d1p"],
                   abs(float(AdT[1, 1]) - R9["d2p"]) / R9["d2p"],
                   abs(float(0.5 * (AdT[0, 1] + AdT[1, 0]))
                       - R9["cp"]) / abs(R9["cp"]))
        devT_r = abs(rT - R9["rdetp"]) / R9["rdetp"]
        devT_l = abs(lrT - R9["lam_rest"]) / R9["lam_rest"]
        check("G40-twin", ok_dose0 and devT <= TWIN_BAR
              and devT_r <= TWIN_BAR and devT_l <= TWIN_BAR,
              "RATIONAL TWIN at tol %.0e (dose-zero identity "
              "BITWISE %s): dressed scalars dev <= %.1e, r'_det "
              "dev %.1e, lambda_rest dev %.1e (bar %.0e) -- the "
              "dressed coordinate is twin-stable"
              % (TWIN_TOL, ok_dose0, devT, devT_r, devT_l,
                 TWIN_BAR))
        staffel = {}
        ok_mp = True
        details = []
        for (kz, dps) in MP_SET:
            R = ROWS[kz]
            d1m, d2m, cm, m2m = PX.mp_pair_ward(R["mz"], R["i1"],
                                                R["i2"], dps)
            dev_d = max(abs(R["d1"] - d1m) / abs(d1m),
                        abs(R["d2"] - d2m) / abs(d2m))
            dev_c = abs(R["c"] - cm) / abs(cm)
            dev_m2 = abs(R["m2"] - m2m) / max(abs(m2m), 1e-300)
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
        check("G41-mp-wards", ok_mp,
              "MP WARDS (r342 route verbatim): %s (bars d/c %.0e "
              "core / %.0e EXT3; m2 depth-graded); w9 STAFFEL dps "
              "30 vs 45 dev %.1e (bar %.0e)"
              % ("; ".join(details), MP_DC_CORE, MP_DC_EXT3,
                 st_dev, STAFFEL_BAR))

    # ---------------- S5 fits + adjudication inputs
    section("S5  LEG B/C/D -- SEALED FITS + FLATNESS + SHADOW + "
            "PEELING STATS")
    if smoke:
        for g in ("G50-fit-anchors", "G51-flatness",
                  "G52-restatement-top2", "G53-bound-census",
                  "G54-peeling"):
            check(g, True, "SMOKE: skipped")
        flat_ok = decays = restate = None
        peel_tag = top2_tag = bound_txt = anat_txt = lam_txt = ""
        ext4_txt = ""
    else:
        fit_kz = [k for k in kz57 if k not in excl]
        lnN = np.log(np.array([ROWS[k]["Nw"] for k in fit_kz],
                              float))
        colv = {
            "p": [ROWS[k]["p"] for k in fit_kz],
            "q": [ROWS[k]["q"] for k in fit_kz],
            "c": [ROWS[k]["c"] for k in fit_kz],
            "m2": [ROWS[k]["m2"] for k in fit_kz],
            "margin": [ROWS[k]["margin"] for k in fit_kz],
            "restm": [1.0 - ROWS[k]["lam_rest"] for k in fit_kz],
            "rdetp": [ROWS[k]["rdetp"] for k in fit_kz],
            "g21": [XT[k]["g21"] for k in fit_kz],
            "r2det": [XT[k]["r2det"] for k in fit_kz],
        }
        fits, curv = {}, {}
        o = np.argsort(lnN)
        half = len(o) // 2
        for nm, vals in colv.items():
            y = np.log(np.abs(np.asarray(vals, float)))
            ft_ = LM.ts_fit(lnN, y)
            s_lo = LM.ts_slope_free(lnN[o[:half]], y[o[:half]])
            s_hi = LM.ts_slope_free(lnN[o[half:]], y[o[half:]])
            fits[nm] = (float(ft_[0]), float(ft_[1]))
            curv[nm] = float(s_hi - s_lo)
        ok_fit_anch = all(abs(fits[nm][1] - FIT_ANCH[nm])
                          <= FIT_ANCH_TOL for nm in FIT_ANCH)
        check("G50-fit-anchors", ok_fit_anch,
              "LEG 0 FIT ANCHORS on the 57 (slope | r342 record): "
              "p %.3f | %.3f, q %.3f | %.3f, c %.3f | %.3f, m2 "
              "%.3f | %.3f, margin %.3f | %.3f, restm %.3f | "
              "%.3f, rdetp %+.3f | %+.3f (tol %.2f) -- the r342 "
              "fit instrument reproduced bit-near; NEW columns: "
              "g21 slope %+.3f (curv %+.3f), r2det slope %+.3f "
              "(curv %+.3f)"
              % (fits["p"][1], FIT_ANCH["p"], fits["q"][1],
                 FIT_ANCH["q"], fits["c"][1], FIT_ANCH["c"],
                 fits["m2"][1], FIT_ANCH["m2"], fits["margin"][1],
                 FIT_ANCH["margin"], fits["restm"][1],
                 FIT_ANCH["restm"], fits["rdetp"][1],
                 FIT_ANCH["rdetp"], FIT_ANCH_TOL, fits["g21"][1],
                 curv["g21"], fits["r2det"][1], curv["r2det"]))
        # flatness adjudication
        slope_r = fits["rdetp"][1]
        curv_r = curv["rdetp"]
        flat_57 = (abs(slope_r) <= FLAT_BAR
                   and abs(curv_r) <= CURV_BAR)
        a0, b0 = fits["rdetp"]

        def band_stats(kzs):
            n_in, n_low = 0, 0
            for kz in kzs:
                if kz in excl:
                    continue
                pred = math.exp(a0 + b0 * math.log(ROWS[kz]["Nw"]))
                lg = math.log10(ROWS[kz]["rdetp"] / pred)
                if abs(lg) <= BAND:
                    n_in += 1
                elif lg < -BAND:
                    n_low += 1
            return n_in, n_low

        e3_in, e3_low = band_stats(ext3_kzs)
        e4_in, e4_low = band_stats(ext4_kzs)
        floor_loci = [k for k in ROWS if k not in excl
                      and ROWS[k]["rdetp"] <= RDETP_FLOOR]
        hard = []
        if slope_r <= -DECAY_SLOPE and abs(curv_r) <= CURV_BAR:
            hard.append("slope_57 %.3f" % slope_r)
        if e3_low >= EXT3_LOW_KILL:
            hard.append("EXT3 n_low %d" % e3_low)
        if e4_low >= EXT4_LOW_KILL:
            hard.append("EXT4 n_low %d" % e4_low)
        if floor_loci:
            hard.append("floor loci %s" % str(sorted(floor_loci)))
        soft = []
        if not flat_57:
            soft.append("FLAT_57 (slope %.3f curv %.3f)"
                        % (slope_r, curv_r))
        if e3_in < EXT3_OK_MIN:
            soft.append("EXT3 in-band %d/12" % e3_in)
        if e4_low > 1:
            soft.append("EXT4 n_low %d" % e4_low)
        flat_ok = not hard and not soft
        decays = bool(hard or soft)
        check("G51-flatness", True,
              "SEALED FLATNESS ADJUDICATION: slope_57 = %+.3f "
              "(bar %.2f), curv %+.3f (bar %.2f) => FLAT_57 %s; "
              "EXT3 PURE TEST (blind rows): %d/12 in the %.1f-"
              "decade band, n_low %d; EXT4 (disclosed-seen): %d/6 "
              "in band, n_low %d; floor (<= %.2f): %s => %s"
              % (slope_r, FLAT_BAR, curv_r, CURV_BAR, flat_57,
                 e3_in, BAND, e3_low, e4_in, e4_low, RDETP_FLOOR,
                 str(sorted(floor_loci)) if floor_loci else "none",
                 "FLAT SURVIVES" if flat_ok else
                 ("DECAYS hard: " + "; ".join(hard) if hard
                  else "DECAYS soft: " + "; ".join(soft))))
        # restatement + top2
        sh_dev = med([abs(XT[k]["r_sh"] / ROWS[k]["rdetp"] - 1.0)
                      for k in fit_kz])
        restate = sh_dev <= RESTATE_BAR
        t2_dev = med([abs(XT[k]["shadows"][2] / ROWS[k]["rdetp"]
                          - 1.0) for k in fit_kz])
        kres_all = [XT[k]["k_res"] for k in ROWS if k not in excl]
        kres_med = med(kres_all)
        top2 = t2_dev <= TOP2_BAR
        top2_tag = ("TOP2_SPECTRAL_OBJECT(median |r'_2/r'_det - "
                    "1| = %.4f <= %.2f; K_res med %.0f max %d)"
                    % (t2_dev, TOP2_BAR, kres_med, max(kres_all))
                    if top2 else
                    "TOPK_CENSUS(median K_res %.0f, t2 dev %.4f)"
                    % (kres_med, t2_dev))
        check("G52-restatement-top2", True,
              "RESTATEMENT TEST: median |r_shadow/r'_det - 1| = "
              "%.4f (bar %.2f) => %s -- r'_det is %s a bare-"
              "scalar + lambda_max read-off; TOP-2 CENSUS: %s"
              % (sh_dev, RESTATE_BAR,
                 "FIRES" if restate else "does NOT fire",
                 "" if restate else "NOT", top2_tag))
        # bound census
        n_pos = {K: sum(1 for k in ROWS if k not in excl
                        and XT[k]["bounds"][K] > 0.0)
                 for K in K_LIST}
        lb32 = [XT[k]["bounds"][32] for k in ROWS
                if k not in excl]
        min_lb32 = min(lb32)
        o1_bound = all(XT[k]["bounds"][32] >= DELTA_BAR
                       for k in ROWS if k not in excl)
        r2_autopsy = {kz: XT[kz]["r_r2"] for kz in SAMPLE_KZ}
        bound_txt = ("n_pos(K %s) = %s of %d rows; min r'_lb(32) "
                     "= %s; sign autopsy r'_R2 on the sample: %s"
                     % (str(K_LIST),
                        str([n_pos[K] for K in K_LIST]),
                        len(lb32),
                        ("%.3f" % min_lb32 if min_lb32 > -1e6
                         else "-inf"),
                        str({("kz%d" % k): ("%.1e" % v)
                             for k, v in r2_autopsy.items()})))
        check("G53-bound-census", True,
              "THE LEG C BOUND CENSUS (theorem-grade chain, "
              "measured inputs): %s -- the R2-R4 relaxation "
              "route %s; O1 bound clause (all rows >= %.2f): %s; "
              "KERNEL_CLOSED_FORM sealed %s"
              % (bound_txt,
                 "NEVER certifies" if max(n_pos.values()) == 0
                 else "certifies %d rows at best"
                 % max(n_pos.values()),
                 DELTA_BAR, o1_bound, KERNEL_CLOSED_FORM))
        # peeling
        mass_med = med([XT[k]["mass2"] for k in fit_kz])
        mass_min_kz = min(fit_kz, key=lambda k: XT[k]["mass2"])
        r2_min = min(XT[k]["r2det"] for k in fit_kz)
        peel = (mass_med >= PEEL_MASS_BAR
                and r2_min >= PEEL_R2_FLOOR)
        peel_tag = ("PEELING_STRUCTURE_FOUND(median rest-pair "
                    "mass %.4f >= %.2f on the 57 (min %.4f at "
                    "kz%d), min r''_det %.4f >= %.2f)"
                    % (mass_med, PEEL_MASS_BAR,
                       XT[mass_min_kz]["mass2"], mass_min_kz,
                       r2_min, PEEL_R2_FLOOR)
                    if peel else
                    "NO_PEELING(mass med %.4f, r2 min %.4f)"
                    % (mass_med, r2_min))
        check("G54-peeling", True,
              "LEG D PEELING CENSUS: %s; EXT3/EXT4 medians mass "
              "%.4f / %.4f, r''_det %.2f / %.2f; lambda_rest "
              "offset (1-lambda_rest)/margin median %.1fx "
              "(range %.1f..%.1f over all rows)"
              % (peel_tag,
                 med([XT[k]["mass2"] for k in ext3_kzs]),
                 med([XT[k]["mass2"] for k in ext4_kzs]),
                 med([XT[k]["r2det"] for k in ext3_kzs]),
                 med([XT[k]["r2det"] for k in ext4_kzs]),
                 med([(1.0 - ROWS[k]["lam_rest"])
                      / ROWS[k]["margin"] for k in fit_kz]),
                 min((1.0 - ROWS[k]["lam_rest"])
                     / ROWS[k]["margin"] for k in ROWS
                     if k not in excl),
                 max((1.0 - ROWS[k]["lam_rest"])
                     / ROWS[k]["margin"] for k in ROWS
                     if k not in excl)))
        anat_txt = ("medians on the 57: dd1/p %.3f, dc/c %+.3f, "
                    "rho' %.3f, m2'/margin %.4f, g21 %.2f (slope "
                    "%+.3f)"
                    % (med([XT[k]["dd1"] / ROWS[k]["p"]
                            for k in fit_kz]),
                       med([XT[k]["dc"] / ROWS[k]["c"]
                            for k in fit_kz]),
                       med([XT[k]["rhop"] for k in fit_kz]),
                       med([XT[k]["m2p_ratio"] for k in fit_kz]),
                       med([XT[k]["g21"] for k in fit_kz]),
                       fits["g21"][1]))
        lam_txt = ("slope %.3f (prior %.3f), curv %+.3f, offset "
                   "med %.1fx"
                   % (fits["restm"][1], FIT_ANCH["restm"],
                      curv["restm"],
                      med([(1.0 - ROWS[k]["lam_rest"])
                           / ROWS[k]["margin"] for k in fit_kz])))
        ext4_txt = "; ".join(
            "kz%d(z %d, N %d, m %.2e, r' %.4f, R2 %.3f)"
            % (k, ROWS[k]["z"], ROWS[k]["Nw"], ROWS[k]["margin"],
               ROWS[k]["rdetp"], ROWS[k]["R2"])
            for k in ext4_kzs)

    # ---------------- S6 worlds
    section("S6  LEG E -- THE WORLD CENSUS (SCHUR EQUIVALENCE + "
            "KAPPA_INT)")
    if smoke:
        for g in ("G60-controls", "G61-schur-equivalence",
                  "G62-kint-anchors"):
            check(g, True, "SMOKE: skipped")
        world_txt = ""
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
            WORLDS[cn] = FC.world_from_arrays(
                cn, xs_z, ws_z, ys_z, vs_z, N_c, int(cctx["L"]))
        check("G60-controls", ok_ctrl,
              "EPST + SCR + SMOOTH + HL2 built verbatim through "
              "the r278/r280 channel at THEIR own N_w: minC == "
              "flips %s + HL2 %d"
              % (str(CTRL_FLIPS), HL2_FLIP))
        WORLDS["MAIN"] = FC.world_from_mz("MAIN", R9["mz"])
        WORLDS["TWIN"] = FC.world_from_mz("TWIN", mzT)
        cen = {}
        ok_equiv = True
        for wn in ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH",
                   "HL2"):
            Wd = WORLDS[wn]
            Ew = Wd["B"] @ Wd["B"].T
            i1w, i2w = PX.pair_select(Wd["yn"])
            restw = [k for k in range(Ew.shape[0])
                     if k != i1w and k != i2w]
            Dw = Ew[np.ix_(restw, restw)]
            lam_rw = float(np.linalg.eigvalsh(Dw)[-1])
            if lam_rw < 1.0:
                Adw, _lr, _s1, _s2 = PX.schur_dress(Ew, i1w, i2w)
                ppw = 1.0 - float(Adw[0, 0])
                qqw = 1.0 - float(Adw[1, 1])
                rw = PX.det_reserve(
                    float(Adw[0, 0]), float(Adw[1, 1]),
                    float(0.5 * (Adw[0, 1] + Adw[1, 0])))[2]
                clause2 = (ppw > 0 and qqw > 0 and rw > 0)
                r_txt = "%.4f" % rw
            else:
                clause2 = False
                r_txt = "UNDEF"
            live_schur = (lam_rw < 1.0) and clause2
            ok_equiv = ok_equiv and (live_schur
                                     == (Wd["lam"] < 1.0))
            pr_w, pm_w = PX.eig_pr(Wd)
            ki, _loc, _nint, _kaps, ncf = FC.interval_census(Wd)
            cen[wn] = dict(lam=Wd["lam"], lam_rest=lam_rw,
                           r=r_txt, pr=pr_w, pm=pm_w, kint=ki,
                           ncf=ncf)
            info("%s: lambda %.6g, lambda_rest %.6g, r'_det %s, "
                 "PR %.2f, pair mass %.3f, kappa_int %.6g"
                 % (wn, Wd["lam"], lam_rw, r_txt, pr_w, pm_w, ki))
        lr_sep = (all(cen[wn]["lam_rest"] >= 1.0
                      for wn in ("EPST", "SCR", "SMOOTH", "HL2"))
                  and all(cen[wn]["lam_rest"] < 1.0
                          for wn in ("MAIN", "TWIN")))
        check("G61-schur-equivalence", ok_equiv,
              "EXACT SCHUR EQUIVALENCE on 6/6 worlds: (lambda < "
              "1) == (lambda_rest < 1 AND dressed pair PD); "
              "WORLD SEPARATION of the FIRST clause alone: "
              "lambda_rest >= 1 on dead 4/4 and < 1 on live "
              "2/2: %s -- on the instrumented worlds the rest "
              "block is already the discriminator, the dressed "
              "pair clause never has to fire on a dead world"
              % lr_sep)
        ok_kint = (all(abs(cen[wn]["kint"] / KINT_REC[wn] - 1.0)
                       <= KINT_REC_TOL
                       for wn in ("EPST", "SCR", "SMOOTH", "HL2"))
                   and all(abs(cen[wn]["kint"] / KINT_LIVE_REC
                               - 1.0) <= KINT_LIVE_TOL
                           for wn in ("MAIN", "TWIN"))
                   and sum(cen[wn]["ncf"] for wn in cen) == 0)
        check("G62-kint-anchors", ok_kint,
              "LEG 0 KAPPA_INT ANCHORS (r334 machinery verbatim, "
              "certificates clean): EPST %.6g / SCR %.4g / "
              "SMOOTH %.4g / HL2 %.6g == r334/r342 records at "
              "%.0f%%; live MAIN %.6f / TWIN %.6f == %.6f"
              % (cen["EPST"]["kint"], cen["SCR"]["kint"],
                 cen["SMOOTH"]["kint"], cen["HL2"]["kint"],
                 100 * KINT_REC_TOL, cen["MAIN"]["kint"],
                 cen["TWIN"]["kint"], KINT_LIVE_REC))
        world_txt = ("lambda_rest separates 4/4 dead (EPST %.4g "
                     "/ SCR %.4g / SMOOTH %.4g / HL2 %.4g >= 1, "
                     "live %.6f < 1)"
                     % (cen["EPST"]["lam_rest"],
                        cen["SCR"]["lam_rest"],
                        cen["SMOOTH"]["lam_rest"],
                        cen["HL2"]["lam_rest"],
                        cen["MAIN"]["lam_rest"]))

    # ---------------- S7 must-fails
    section("S7  MUST-FAILS")
    mj1, mj2 = mutant_wrong_block(R9["mz"]["vn"])
    w19 = X9["W"][:, -1]
    mut_mass = float(w19[mj1] ** 2 + w19[mj2] ** 2)
    check("G70-m1-wrong-block", mut_mass < MUT_MASS_BAR
          and R9["pmass"] >= MASS_BAR,
          "m1 DRESSING AT THE WRONG BLOCK (two largest-v atoms "
          "%s): top-eigenvector mass %.4f < %.1f while the "
          "sealed shallow-edge pair carries %.4f >= %.2f -- "
          "CAUGHT by the concentration check"
          % (str((mj1, mj2)), mut_mass, MUT_MASS_BAR, R9["pmass"],
             MASS_BAR))
    check("G71-m2-readback", bool(hits_m2),
          "m2 r'_det READ BACK from the withheld lambda record: "
          "AST-FLAGGED (%s) -- the dressed scalars are "
          "Gram-block objects, never spectrum-record read-offs"
          % (hits_m2[0] if hits_m2 else "MISS"))
    mut3 = mutant_flatbar_posthoc(0.28)
    check("G72-m3-flatbar-posthoc", bool(hits_m3)
          and abs(mut3 - FLAT_BAR) >= MUT_MIN,
          "m3 FLATNESS BAR AFTER SIGHT: AST-FLAGGED (%s) and the "
          "toy 'recalibrated bar' %.2f != the sealed FLAT_BAR "
          "%.2f -- protocol-CAUGHT (bars are frozen module "
          "constants under the two-commit protocol)"
          % (hits_m3[0] if hits_m3 else "MISS", mut3, FLAT_BAR))
    dev_m4 = mutant_double_dress(X9["E"], R9["i1"], R9["i2"])
    check("G73-m4-double-dress", dev_m4 >= M4_BAR,
          "m4 SCHUR WITH SWAPPED/DOUBLED BLOCKS: det(I-E) == "
          "det(I-A') det(I-D'') with BOTH blocks dressed breaks "
          "the exact logdet identity by %.2f log-units (>= %.1f) "
          "-- the coupling can be absorbed into ONE block only, "
          "exactly CAUGHT" % (dev_m4, M4_BAR))
    mut5 = mutant_corr_of_E(X9["E"], R9["i1"], R9["i2"])
    dev_m5 = abs(mut5 - R9["rdetp"]) / R9["rdetp"]
    check("G74-m5-wrong-matrix", dev_m5 >= M5_BAR,
          "m5 CORRELATION OFF E INSTEAD OF (I-E)^{-1}: %.4f vs "
          "r'_det %.4f (dev %.1f >= %.1f) -- the resolvent, not "
          "the Gram, carries the dressed reserve; CAUGHT"
          % (mut5, R9["rdetp"], dev_m5, M5_BAR))

    # ---------------- S8 verdict
    section("S8  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism "
          "promoted, no certificate reading of the census bound, "
          "no posthoc bar/band/family/prior move, no derived "
          "5/7, NO RH claim; what the round adds: the resolvent-"
          "correlation identity, the exact dressing anatomy, the "
          "sealed flatness kill on EXT3 + EXT4, the bound-ladder "
          "adjudication, the lambda_rest world column and the "
          "peeling census; r243..r342 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        if not audits_ok:
            main_v = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif restate:
            main_v = ("RESTATEMENT(median shadow dev <= %.2f -- "
                      "r'_det is a bare-scalar + lambda_max "
                      "read-off)" % RESTATE_BAR)
        elif flat_ok and o1_bound and KERNEL_CLOSED_FORM:
            main_v = ("DRESSED_RESERVE_O1_CERTIFIED(flat + bound "
                      ">= %.2f on all rows + closed-form inputs)"
                      % DELTA_BAR)
        elif flat_ok:
            main_v = ("DRESSED_RESERVE_FLAT_CENSUS(slope_57 "
                      "%+.3f, curv %+.3f; EXT3 %d/12 in band "
                      "n_low %d; EXT4 %d/6 in band n_low %d -- "
                      "flatness survives every family; the O1 "
                      "clause does not fire: KERNEL_CLOSED_FORM "
                      "%s, bound clause %s)"
                      % (slope_r, curv_r, e3_in, e3_low, e4_in,
                         e4_low, KERNEL_CLOSED_FORM, o1_bound))
        else:
            main_v = ("DRESSED_RESERVE_DECAYS(%s: %s)"
                      % ("hard" if hard else "soft",
                         "; ".join(hard if hard else soft)))
        parts = [
            main_v,
            "ANATOMY(%s)" % anat_txt,
            "BOUND_LEDGER(%s)" % bound_txt,
            "LAMBDA_REST_LEDGER(%s; %s)" % (lam_txt, world_txt),
            peel_tag,
            top2_tag,
            "EXT4_CENSUS(%s)" % ext4_txt,
            "TWIN_LEDGER(dressed dev %.1e, r' dev %.1e)"
            % (devT, devT_r),
            "MUSTFAIL_LEDGER(m1-m5 + scopes)",
        ]
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED anatomy + sealed adjudication of the "
          "dressed pair reserve; NO L* claim, NO RH claim"
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
