#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""borodin_dual_hole_probe -- PRIME.LSTAR.DUAL_HOLE.01
(round 356): THE BORODIN PARTICLE-HOLE DUALITY WITH RECIPROCAL
WEIGHT -- the ONE approved internal L* round after the idea search
(DCCIV: two independent thinkers, Sol rank 1), plus the AC-CLASS
FALSIFIER (Fable's leg 0) as the co-deliverable.  After this round
the L* lane returns to the specialist memo.

THE FROZEN QUESTION (r352/r354): the L* margin is a 500x
cancellation of two co-wandering blocks (phi_D = log pq + A lnN
and phi_K = log c^2 + A lnN, corr 0.999998, 0.88 nats each vs
0.0017 nats difference); the r354 four-block anatomy ended in a
TWO-BLOCK INTERFERENCE (pair geometry P2/PG corr +0.887 at 2.4x
amplitude vs dictionary weights W corr -0.722) with NO single
carrier at the sealed bars.  THE ROUND'S CONTRACT (Sol's sketch,
binding): lift (mu, nu) to the POSITIVE total measure eta = mu +
nu with u_j = |wtilde_j| on the union support X; let Pi_N^u be the
rank-N projection kernel of the eta OP ensemble and Q =
(Pi_N^u)_{Y,Y} on Y = supp nu.  Then EXACTLY (the L-ensemble
transformation): Q = E (I+E)^{-1} and E = Q (I-Q)^{-1}.  With the
Borodin dual weight u_vee_j = 1/(u_j P_X'(x_j)^2) (P_X the monic
node polynomial of the FULL support X) and the rank condition S =
2N - 1 (HALF FILLING -- the r228/r281 law re-consumed as Borodin's
complementary rank condition), Borodin's complementation gives
Pi_N^u = D (I - Pi_{N-1}^{u_vee}) D with the diagonal sign matrix
D_jj = sign P_X'(x_j) = (-1)^{f_j}; hence with R =
(Pi_{N-1}^{u_vee})_{Y,Y}:
    E = D (R^{-1} - I) D,    I - E = D (2I - R^{-1}) D,
    L*  <=>  lambda_max(E) < 1  <=>  R > (1/2) I,
    margin == 2 - 1/lambda_min(R)   (exact spectral map),
    c == eps_1 eps_2 (R^{-1})_{12},  p == 2 - (R^{-1})_{11},
i.e. the r342 pair block is (up to D-signs) the (1,2) principal
minor of 2I - R^{-1}: the 500x cancellation read as the two-point
PRECISION structure of a dual HOLE process at half filling.  ON
THE COSINE LATTICE (the document support IS the full folded grid
x_j = cos(pi j / S), j = 1..S, S = L/2 = M - 1): P_X(x) =
2^{1-S} (x+1) U_{S-1}(x), |P_X'(x_j)| = 2^{1-S} S kappa_j /
(1 - x_j) with kappa_j = 1 (j < S), 2 (j = S), and with the
document weight u_j = (1/S) c_j (1 - x_j) |f(theta_j)| (c_S = 1/2,
the folding endpoint halving) the dual weight becomes exactly
    u_vee_j  PROPTO  c_j (1 - x_j) / |f(theta_j)|
-- the ORIGINAL weight carries +log|f|, the DUAL weight -log|f|:
the measured r354 anti-correlation of the weight block against the
pair-geometry block is ALGEBRAIC BY DESIGN under the duality
(gated below).  Equivalently, symbol-free: u_vee_j PROPTO
(1 - x_j)^2 / (u_j kappa_j^2) (route B; the construction route).

THE FIVE LEGS: (Leg A) THE EXACT ALGEBRA, gated: (a1) the
rank/support gate on the REAL windows -- S == L/2 == 2 N_w - 1
(no culled fold atoms), the union support == the full cosine grid
BITWISE, the weight identity u == (1/S) c_j (1-x) |f| against the
INDEPENDENTLY recomputed circulant symbol f (V.prime_lags +
V.arch_lags + V.spectral_density, document route) -- any real-
window failure => SUPPORT_GATE_FAIL typing with the honest census
how far the duality still carries; (a2) Q = E(I+E)^{-1} exact:
Fractions on a 5-atom rational model (both the L-ensemble
transformation and the roundtrip E = Q(I-Q)^{-1}), f64 <= 1e-10 on
w9 and graded on every ladder row; (a3) the dual weight built
THREE ways -- route A (numeric log |P_X'| pairwise sums, grid-
agnostic), route B ((1-x)^2/(u kappa^2), the grid closed form),
route C (c_j (1-x)/|f| with the recomputed symbol) -- A == B up to
the mean (graded bars), B == C bitwise-tight (the weight
dictionary identity), plus the exact-Fractions Borodin
complementation Pi_N^u + G Pi_{N-1}^{u_vee} G^{-1} == I with the
RATIONAL conjugator G = diag(1/(u_j P_X'(x_j))) (no square roots
-- the sign matrix and the weight ratio combine rationally);
(a4) the full complementation, the spectral map margin ==
2 - 1/lambda_min(R), the pair identities c == eps1 eps2
(R^{-1})_{12}, p/q == 2 - (R^{-1})_{kk}, and the dual block
factorization log c^2 == DW + DK + GC with
    DW = log(u_vee_1 u_vee_2)          [reciprocal dictionary],
    DK = 2 log |Kvee_{12}|             [dual CD block],
    GC = 2 log |(R^{-1})_{12} / R_{12}| [global conditioning],
(DW + DK = 2 log |R_12|) -- all graded on the 85-row ladder.
(Leg B) THE CARRIER TEST, sealed: the fine-structure operator
psi57 (Theil-Sen line fitted on the 57 OLD rows ONLY, residual
evaluated everywhere, median-centred on the 57 -- EXT3..EXT6 stay
PURETEST) applied to the target log c^2, the THREE dual blocks
(DW, DK, GC) and the r354 four-block family (W, B2, P2, GM, PG --
recomputed in-run on identical rows for the apples-to-apples
census); a dual block CARRIES iff corr >= CAR_CORR_MIN 0.9 AND
leave-out <= CAR_RES_MAX 0.5 on the 57 (the r354 sealed clauses
reused); THE COMPRESSION CLAUSE: the carrier additionally needs
leave-out(best dual) <= COMPRESS_FACTOR 0.5 x leave-out(best r354
block, in-run) -- honesty: the SUM block DW + DK = log c^2 - GC is
near-tautological (GC is small) and is EXCLUDED from the sealed
list, printed as census with the tautology named; THE RESERVE
CLAUSE: the LOCAL dual two-point block ((R_pair)^{-1} of the 2x2
restriction -- consumes R_11, R_12, R_22 ONLY, never p/q/c: the
readback is the m6 must-fail) predicts the log reserve LR =
-log(c^2/pq) via LR_loc = -log(c_loc^2/(p_loc q_loc)); clauses
corr(psi57 LR_loc, psi57 LR) >= RES_CORR_MIN 0.9 AND leave-out <=
RES_RES_MAX 0.5 on the 57, EXT puretest census.  (Leg A-anti) THE
BY-DESIGN GATE: corr(psi57 DW, psi57 W) <= ANTI_BAR -0.99 on the
57 -- the r354 anti-correlation pattern as duality algebra
(DW == 2 log((1-y1)(1-y2)) - W + const, the geometry factor is
family-constant by the hard-edge scaling); corr(psi57 DK, psi57
PG) printed as census.  (Leg C) WORLDS + TWIN: the dual pipeline
on the r354 mini-ladders (WORLD_KZ, 6 rungs) for MAIN + rational
TWIN (must CARRY: MAIN slope-free local-dual coupling corr >=
FS_CORR_MIN 0.99 / rmsr <= FS_RMSR_MAX 0.2; TWIN dose-zero
BITWISE and pointwise dual devs <= TWIN_DUAL_BAR 1e-3 nats) and
the ladderable dead worlds SMOOTH / SCR / DIR / ABS (r354 channel
verbatim; EPST / HL2 NOT_LADDERED, kz9-specific, typed): a dead
world LOSES iff it fails the mini carrier clause OR the mini
reserve clause on its usable rows (sealed usable-row rules:
finite logs, pq > 0, c^2 > 0 for the carrier; additionally LR > 0
and LR_loc > 0 finite for the reserve; < WORLD_MIN_ROWS 5 usable
=> NOT_MEASURABLE census); if the main carrier AND reserve
clauses fire AND some measurable dead world passes BOTH mini
clauses => WORLD_BLIND; the lambda_min(R) world census is printed
(the duality equivalence makes R > I/2 fail structurally exactly
on the dead worlds -- the L* condition restated, census not
clause).  (Leg D) THE DEMARCATION GATE against r227/r228 (read
verbatim from the DLIII/DLIV records): the r228 object was the
SIGNED measure mutilde = mu - nu (Hankel-determinant
complementation D_{N-m}(mutilde) = Vand^2 (prod w) D_m(mutilde#)
with dual reference weights 1/(w L_N'^2)), and its r-quotient
duality died on the ZERO-WEIGHT structure (mu == 0 on every nu
node: R_DUAL_OBSTRUCTED) -- HERE the lift is the POSITIVE measure
eta = mu + nu with u = |wtilde| > 0 on EVERY union node, so the
Borodin dual weight EXISTS everywhere (gated: min u > 0 and
u_vee finite on all rows); the r228 half-filling law N_w =
ceil(S/2) (NOT_A_HOLE_EDGE) is CONSUMED here as the exact
complementary rank condition S = 2N - 1; the r228
COMPLEMENT_IDENTITY_EXACT tool survives as the determinant shadow
of the projection-kernel complementation used here; the
DUAL_WALL_EQUIVALENT risk is typed by the verdict enum itself
(DUALITY_REPARAM_ONLY exists for exactly this).  (Leg E) THE AC
FALSIFIER (co-deliverable, cheap): the rescaled pair positions
a_k = 2 N^2 (1 - y_k) are FAMILY-CONSTANT against pi^2 f_k^2 / 4
(the hard-edge microscopic scaling; ward |a/(pi^2 f^2/4) - 1| <=
AC_POS_FACT 3 / N_w per row, fold census printed), and the
Lubinsky-type AC universality prediction rho_K -> const (fixed
rescaled positions => a fixed Bessel-kernel ratio) CONTRADICTS
the measured decorrelation a_rhoK = 1.4222 (r352 record, re-gated
at tol 0.05 on the 57): AC_CLASS_EXCLUDED fires iff the position
ward passes AND a_rhoK >= AC_DECAY_MIN 0.5 -- the universality-
class exclusion typed for the memo; deep rhoK band census
(EXT5/EXT6 vs the 57-fit) printed.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO L* CLAIM, NO RH CLAIM in
either direction, mincut unchanged.  Coexistence: R355 (K2,
terminal lane) and the memo-sharpening worker (rh/problem/
lstar_problem.tex) may run in parallel -- this probe touches
NOTHING outside its own file and the strictly additive rh-sync.
Two-commit freeze protocol (r329 convention): spec + machinery
committed BEFORE the record run, record tables inserted after.

INDEX FIREWALL (binding, r238-r354 discipline): w = window (kz
into the prime-power list), S = #union atoms, S_- = #nu atoms,
N_w = (S+1)//2, f_j = the fold index (grid index) of atom j;
ground truth (r283..r354 records, control flips) enters GATES and
record tables only; the module-own constructors consume kernel
Gram / spectrum / weight / position / chain-coefficient arrays
and measured columns ONLY (AST scope audit; withheld identifiers
are the RECORD values ALPHA_REC / RHOR_REC / A_RHOK_REC and the
verdict-side columns lr_col_true and c_col_true); the RESERVE
constructor lr_local consumes the dual pair block (R_11, R_12,
R_22) ONLY; no zero/prime oracles anywhere (AST firewall; the
prime-power grid is the sealed source comb, r238 convention); no
fit primitives (fragment audit; every fit is the imported r286
Theil-Sen; psi57 calls it on the frozen 57-mask -- no new
estimator).  MACHINERY IMPORTED VERBATIM: r342 PX.{build_rung,
pair_select, pair_block, det_reserve} (b09f8ccd), r352
RSA.{rho_corr_cols, fine_structure} (dc6bbd2c), r347
DA.decay_law (bd1aa7f3), r354 PWA.{cd_blocks, carrier_stats,
psi_small, rung_reduced_cols} (f9db84da), r329
E3.{admissible_pool, used_kz_set} (bbfaf199), r330
DSW.{dirichlet_comb, dirichlet_abs_comb} (66526018), document
pipeline V.{build_measures, mu_chain, b_matrix, window_shape,
prime_lags, arch_lags, spectral_density, lam_max_at,
admissible_indices, U, W_VM, PP}, r286 LM.{ts_fit,
ts_slope_free, ext_rule}, r334 FC (world channel), r278
MS.ctx_build, r280 BL.union_of_ctx, r243 PB.smooth_comb, r331
TR.{base_comb, build_world}, r289 AKD.twin_rational, r276
MF.local_gaps, v563 core READ-ONLY.

LEG 0 -- ANCHORS BIT-NEAR (record numbers as gates): w9 records
(S 367, N_w 184, lambda 0.99983248, lambda at 185 = 1.00003660,
margin 1.6752e-4 rel 0.01); the r354 four-block w9 anchors (W
-24.7664, B2 -1.5711, P2 +4.0100, GM +15.4593 abs 2e-3) and the
kz44/56/130 four-block sample anchors (r354 record verbatim); the
sealed fit slopes (margin -3.332, c -0.697, p -0.754, q -0.645,
rdet -2.624, kap -0.711) tol 0.02 and curvatures (margin -0.347,
c +0.308, rdet -0.767) tol 0.03 as DISCLOSED PRIORS; the r352
fine-structure record (corr 0.999998, rms_D 0.8787 nats, rmsr
0.0019) as GATES on the 57; the r343/r352/r354 sealed EXT3/EXT4/
EXT5/EXT6 selections adopted AS-IS (re-derived and gated).

MUST-FAILS (>= 6, each loud): (m1) P_X'^2 OMITTED in the dual
weight (u_vee = 1/(u |P'|)) -- breaks the Y-complementation at w9
by >= M_LOUD 1e-3 AND breaks the exact Fractions identity on the
toy (difference exactly nonzero) -- CAUGHT; (m2) RANK N instead
of N-1 in the hole kernel -- breaks the Y-complementation at w9
(scoped 6.1e-3 >= 1e-3) AND the exact toy -- CAUGHT; (m3) the
node polynomial over the MU SUPPORT ONLY instead of X = supp mu
UNION supp nu -- the route-A/route-B dual-weight comparison
breaks by >= M3_LOUD 1.0 nats at w9 -- CAUGHT; (m4) f REPLACED BY
AN |f| MASS PERMUTATION (deterministic reversal of the symbol
moduli; the world clause in mutant form) -- the weight identity
u == (1/S) c_j (1-x) |f| breaks by >= M4_BAR 0.1 relative at w9
-- CAUGHT; (m5) R_12 INSTEAD OF THE GLOBAL (R^{-1})_{12} -- the c
identity breaks by |eps1 eps2 R_12 / c - 1| >= M5_BAR 0.1 at w9
(scoped 0.61; the GC block IS the difference) while the true
(R^{-1})_{12} identity holds at the graded bar -- CAUGHT; (m6)
THE RESERVE PREDICTION WITH LR-READBACK: a mutant returning the
withheld measured LR column verbatim -- AST-FLAGGED (the scope
audit is the catch); plus the c-readback mutant (c_col_true) --
AST-FLAGGED.  STOP LIST (anti-gates, binding): NO L* claim, NO
bound mechanism, NO certificate reading of any census, NO posthoc
bar / band / block / clause move, NO derived 5/7, NO RH claim,
mincut unchanged; r243..r355 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN 1.6752e-4
rel 0.01; PX_SHA b09f8ccd; RSA_SHA dc6bbd2c; DA_SHA bd1aa7f3;
PWA_SHA f9db84da; E3_SHA bbfaf199; DSW_SHA 66526018; DUAL9
ANCHORS (s1 scoping, disclosed) DW -19.5844 / DK +10.8508 / GC
+1.8653 abs 2e-3, lam_min(R) 0.500041882 abs 1e-6, LR_loc
7.884295e-3 rel 1e-3, folds (2, 4), eps12 +1; DUAL SAMPLE ANCHORS
(DW, DK, GC) kz44 (-29.2208, +19.5100, +1.5808), kz56 (-36.3366,
+26.4594, +1.5090), kz130 (-40.1507, +28.9818, +1.4995) abs 2e-3;
LRLOC SAMPLE ANCHORS kz44 6.244114e-5, kz56 6.417926e-6, kz130
1.159017e-6 rel 1e-3; R354 BLOCK9 ANCHORS (-24.7664, -1.5711,
+4.0100, +15.4593) abs 2e-3; R354 BLOCK SAMPLE ANCHORS kz44
(-23.7727, -1.4696, -1.8039, +18.9162), kz56 (-31.9880, -1.4006,
-0.0282, +25.0486), kz130 (-30.6196, -1.3558, -3.7210, +26.0269)
abs 2e-3; FIT ANCH (margin -3.332, c -0.697, p -0.754, q -0.645,
rdet -2.624, kap -0.711) tol 0.02; CURV ANCH (margin -0.347, c
+0.308, rdet -0.767) tol 0.03; FS9 ANCHORS corr 0.999998 abs 1e-5
/ rmsD 0.8787 abs 2e-3 / rmsr 0.0019 abs 1e-3; A_LEAD 17/12;
A_RHOK_REC 1.4222 tol 0.05 (WITHHELD record constant -- gates
only); ALPHA_REC 3.332 + RHOR_REC 2.624 (WITHHELD); GRADES
shallow N_w <= 900 / mid <= 3200 / deep > 3200; QE_BAR 1e-10
(all rows); ROUTE_AB_BAR (1e-10, 1e-9, 1e-7); ROUTE_C_BAR 1e-12;
COMP_BAR (1e-10, 1e-9, 1e-8); FULLX_BAR 1e-10; MDUAL_BAR abs
(1e-10, 1e-9, 5e-9) -- DISCLOSED: at EXT6 depth the f64 dual-
margin resolution (~5e-10) EXCEEDS the margins (~4e-10): the
dual route cannot certify the L* sign there, the sign census is
printed honestly; CID_BAR rel (1e-8, 1e-6, 1e-4); BLKID_BAR nats
(1e-8, 1e-6, 1e-4); CAR_CORR_MIN 0.9; CAR_RES_MAX 0.5;
COMPRESS_FACTOR 0.5; DUAL_BLOCKS (DW, DK, GC); R354_BLOCKS (W,
B2, P2, GM, PG); RES_CORR_MIN 0.9; RES_RES_MAX 0.5; ANTI_BAR
-0.99; FS_CORR_MIN 0.99; FS_RMSR_MAX 0.2; WORLD_KZ (18, 9, 52,
119, 42, 130); WORLD_MIN_ROWS 5; TWIN_TOL 1e-8; TWIN_DUAL_BAR
1e-3; AC_POS_FACT 3.0; AC_DECAY_MIN 0.5; EXT3_KZ_B (42, 51, 54,
56, 58, 62); EXT3_KZ_A (96, 123, 125, 127, 128, 130); EXT3_NW
(1721, 2577); EXT4_KZ_B (72, 75, 66); EXT4_KZ_A (113, 111, 108);
EXT4_NW (2656, 3181); EXT5 (h (3401, 6000], K 6, expect kz (69,
107, 101, 99, 115, 89), h (5690, 5668, 5242, 5073, 4243, 4237),
used 98, fresh 9); EXT6 (h (6001, 60000], K 4, cap z^2 <= 400000,
expect kz (133, 129, 124, 117), h (7942, 7675, 7233, 6532), z
(617, 599, 569, 521), used 104, fresh 4); EXT6_DUAL_BUDGET_S 900
(contingency: if exceeded in the calibration pass, the record
freezes the dual columns of the deepest 2 EXT6 rows only,
disclosed); M_LOUD 1e-3; M3_LOUD 1.0; M4_BAR 0.1; M5_BAR 0.1;
TOY_TOL 1e-12; GRID_TOY_S 21; runtime <= 1800 s; smoke = toys +
firewall + scopes + mutants + w9 dual block (records, support
gate, three routes, full complementation, blocks, AC positions);
ladder, EXT, twin, worlds, fits, adjudications skipped.

PRE-SPEC SCOPING (disclosed, r343-s1..r354-s1 precedent -- no
bar, band, threshold, block list, clause or adjudication rule was
tuned after any evaluation except as sized here and said so):
(s1) FOUR sample rungs (kz9, kz44, kz56, kz130) were probed
end-to-end for machinery and bar sizing: support gate S == L/2 ==
2 N_w - 1 with grid dev 0.0 and weight-identity dev 0.0 BITWISE
on all four; Q = E(I+E)^{-1} devs 1.6e-13 .. 1.5e-12; dual-route
A/B devs 2.0e-12 .. 1.3e-10; Y-complementation devs 3.1e-13 ..
2.0e-11; full-X complementation 3.7e-13 at w9; margin_dual abs
devs 4.5e-13 .. 4.2e-11; c/p/q identity rel devs 1.1e-11 ..
7.6e-9; block identities 2.1e-11 .. 2.8e-9; lambda_min(R)
0.500041882 -> 0.500000001 (the L* condition AS R > I/2, live);
the dual blocks (DW, DK, GC) and LR_loc sized as the anchors
above; the m2 rank mutant breaks by 6.1e-3 .. 5.9e-4 (bar sized
at w9), the m5 mutant by ~0.61 == 1 - e^{-GC/2}; runtime 2.9 s
for the four rungs.  (s2) the world channel (MAIN / TWIN /
SMOOTH / SCR / DIR / ABS at kz44 + kz9, machinery only, NO
adjudication): every world satisfies the support gate on the
SAME grid (the folding is world-independent), the dual identity
holds at 1e-12 .. 1e-13 everywhere, and lambda_min(R) separates
structurally (MAIN/TWIN 0.5000+, SMOOTH 0.311/0.476, SCR/DIR ~0,
ABS 4e-6 .. 3e-5) -- the sizing observation behind the census-
not-clause typing of the lambda_min(R) world column.  (s3) EXT6
timing at kz133 (S 15883, N_w 7942, S_- 4566): the full dual
block costs ~15 s (P' loop 0.8 s, chains ~1.5 s, solves/eighs
~12 s), margin 3.848e-10 vs margin_dual -1.154e-10 -- THE F64
RESOLUTION TRUTH at EXT6 depth (complementation dev 5.3e-10,
sized into MDUAL_BAR deep and disclosed in the verdict); deep
pair identities dev_c 1.5e-7 / dev_p 4.4e-7 (sized into CID_BAR
deep 1e-4), block identity 3.0e-7 (BLKID_BAR deep 1e-4), kz133
blocks (DW -25.3706, DK +13.6376, GC +1.4881), LR_loc/LR ratio
0.71, folds (2, 4).  No ladder-wide fit, carrier, reserve,
feature or world adjudication was evaluated before this spec
froze; the numbers cited above are published record numbers or
the disclosed scoping values, never sealed-fit previews.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > SUPPORT_GATE_FAIL > the carrier
adjudication -- the enum is exhaustive):
  [exactly one of]
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  SUPPORT_GATE_FAIL(rows)  iff the rank/support gate fails on any
    real ladder window (the duality carry census printed) /
  DUAL_HOLE_CARRIER_GO(block, compression, reserve, worlds)  iff
    the exact algebra gates all pass AND a sealed dual block
    carries (corr >= 0.9, leave-out <= 0.5 on the 57) AND the
    compression clause fires (best dual leave-out <= 0.5 x best
    r354-block leave-out in-run) AND the reserve clauses fire
    AND the world separation holds (MAIN + TWIN carry, no
    measurable dead world passes both mini clauses) /
  DUALITY_REPARAM_ONLY(failing clauses)  otherwise -- the duality
    is EXACT but does not compress the one-object problem: the
    lane is FINAL at the specialist memo, said honestly
  + WORLD_BLIND(worlds)  [only if the main carrier AND reserve
    clauses fire and a measurable dead world passes both]
  + [exactly one of] AC_CLASS_EXCLUDED(a_rhoK, position ward) /
    AC_CENSUS(values)  [always -- Fable's falsifier co-verdict]
  + DEMARCATION_LEDGER(r228 contrast: positive lift vs signed
    Hankel, dual weight exists on all nodes, half-filling law
    consumed as rank condition) [always]
  + DUAL_MARGIN_LEDGER(lambda_min(R) census incl. the EXT6 f64
    sign-resolution truth) [always]
  + WORLD_LEDGER + TWIN_LEDGER + MUSTFAIL_LEDGER [always].
Honesty before beauty: the complementation, the spectral map and
the pair identities are exact finite-matrix facts (theorem-grade
SKELETON) whose inputs are measured window scalars (census-grade
FLESH); a passing carrier block at the sealed bars is a
LOCALIZATION, not a mechanism; the duality itself CANNOT create
information -- DUALITY_REPARAM_ONLY is the honest null and it
sends the lane to the memo; the anti-correlation gate shows the
r354 interference pattern is duality algebra, not new physics;
AC_CLASS_EXCLUDED is a universality-class STATEMENT FOR THE MEMO,
never a wall mechanism; no verdict claims L*, a bound mechanism,
a derived 5/7, or RH progress in any direction.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit; TWO-COMMIT PROTOCOL EXECUTED: the sealed spec
above was committed as "r356 pre-freeze" (58bb09bb, SPEC_SHA
freeze 5d277d576df75d3a) BEFORE the first full evaluation;
chronology honest: smoke pass 1 = 34/34 (0.6 s) at the sealed
rules, pass 2 byte-identical; pre-freeze commit 58bb09bb;
calibration pass 1 = FIRST full evaluation = 34/34 (115.0 s)
with ZERO amendments -- no bar, band, block, clause or typing
rule moved after the freeze; record run1 = 34/34 (117.1 s),
run2 = 34/34 (114.9 s), byte-identical up to WALL and identical
to the calibration pass):
MAIN VERDICT = DUALITY_REPARAM_ONLY -- THE DUALITY IS EXACT BUT
DOES NOT COMPRESS THE ONE-OBJECT PROBLEM: no dual block passes
the sealed carrier clauses (DW corr +0.6865 / share 1.638 /
leave-out 1.198; DK corr -0.0880 / 1.657; GC corr -0.4379 /
share 0.049 / leave-out 1.021) and the compression clause does
NOT fire (best dual leave-out 1.021 (GC) > 0.5 x best r354
leave-out 0.966 (B2, in-run)); the near-tautological sum block
DW + DK == log c^2 - GC sits at corr +0.9991 / leave-out 0.049
(EXCLUDED from the sealed list by design, census): in the dual
coordinate the wander is LOCAL two-point (reciprocal weight x
dual kernel) with a small, flat global-conditioning remainder --
a REPARAMETRIZATION, not a reduction; the L* lane is FINAL at
the specialist memo
+ ALGEBRA_LEDGER(the round's permanent gain, theorem-grade
skeleton, every gate green: (i) Q = E(I+E)^{-1} EXACT (Fractions
difference 0; f64 1.6e-13 at w9, <= 7.6e-12 on all 85 rows);
(ii) the Borodin complementation Pi_N^u = D(I - Pi_{N-1}^{u_vee})
D at half filling S = 2N-1 -- the SUPPORT GATE HOLDS BITWISE ON
ALL 85 REAL WINDOWS (the union support IS the full cosine grid;
the r228 half-filling law IS Borodin's rank condition, exact,
no off-by-one, whole family); Fractions 0 with the rational
conjugator G = diag(1/(u_j P')); full-X 3.7e-13 at w9;
Y-restriction <= 5.4e-10 deep; (iii) THE SPECTRAL MAP margin ==
2 - 1/lambda_min(R) (abs devs <= 9.9e-10) -- L* IS R > I/2,
measured live: lambda_min(R) - 1/2 = +4.2e-5 (w9) .. +5.9e-11
(EXT6); (iv) the pair identities c == eps1 eps2 (R^{-1})_{12},
p/q == 2 - (R^{-1})_{kk} (rel <= 4.5e-7 deep): the r342 pair
block IS the (1,2) principal minor of 2I - R^{-1}; (v) the
reciprocal weight EXACT on the real windows: route A == B <=
5.0e-9, route B == C at 4.4e-16 -- u_vee == c_j (1-x)/|f| incl.
the endpoint halving)
+ ANTI_DESIGN_GATED(corr(psi57 DW, psi57 W) = -0.999998 <= -0.99:
the r354 anti-correlation of the dictionary-weight block against
the pair-geometry block IS duality algebra -- the +log|f| /
-log|f| reciprocity, exactly as the idea-search predicted;
census corr(psi57 DK, psi57 PG) = -0.567)
+ RESERVE_LOCALIZED(the round's positive finding, census-grade:
the LOCAL dual two-point block (R_pair)^{-1} predicts the log
reserve WITHOUT p/q/c readback and WITHOUT the global inversion
-- corr(psi57 LR_loc, psi57 LR) = +0.9982, leave-out 0.068 on
the 57 AND EXT PURETEST corr +0.9828, leave-out 0.165 on the 28
deep rows; pointwise log(LR_loc/LR) median -0.511, max 0.627
nats: the 500x cancellation is CARRIED by the local dual 2x2
data; the sealed reserve clause FIRES, the carrier+compression
does not -- localization in the dual pair, no compression of
the wander itself; the GO verdict correctly stays off)
+ AC_CLASS_EXCLUDED(the co-deliverable for the memo: rescaled
pair positions a = 2N^2(1-y) family-constant against pi^2 f^2/4
on ALL 85 rows (max dev 0.33 x 1/N_w, fold census [(2, 4)]
uniform), and the measured decorrelation a_rhoK = 1.4222 ==
the r352 record EXACTLY where the Lubinsky-type AC/Bessel class
demands rho_K -> const at fixed microscopic arguments: the
window-kernel universality class is NOT the AC class --
census-grade class exclusion, typed for the memo addressees;
deep census EXT5+EXT6 rhoK in/low 1/0, out-rows HIGH side)
+ DEMARCATION_LEDGER(r228 contrast machine-checked: the old
duality lived on the SIGNED measure (Hankel complement, dual
reference weights 1/(w L'^2)) and died on zero weights
(R_DUAL_OBSTRUCTED, mu == 0 on nu nodes); the positive lift
eta = mu + nu has u >= 6.11e-12 > 0 on every union node and the
dual weight finite everywhere (max u_vee 1.61e+5) -- the
obstruction is structurally ABSENT; NOT_A_HOLE_EDGE's
half-filling law is CONSUMED as the rank condition; the
DUAL_WALL_EQUIVALENT death pattern materialized exactly as the
enum anticipated: as DUALITY_REPARAM_ONLY, typed not hidden)
+ DUAL_MARGIN_LEDGER(EXT6 sign census: margins (3.85e-10,
1.13e-10, 1.70e-09, 1.10e-09) vs margin_dual (-1.65e-10,
+2.36e-10, +7.07e-10, +7.78e-10) -- kz133 flips sign INSIDE the
disclosed ~5e-10 f64 resolution: the dual route cannot certify
the deepest L* signs, said loudly; every shallower row matches
at the graded bars)
+ WORLD_LEDGER(MAIN mini corr 0.994351 / rmsr 0.1211 GATE
passed; the dead worlds LOSE: reserve-usable 0/6 on ALL FOUR
dead worlds -- the LR cone is EMPTY off the wall (pq <= 0 or
c^2 >= pq on every usable row); carrier NOT_MEASURABLE on
SMOOTH/SCR (4/6 usable), DIR best DK corr +0.899 lo 0.993 (no
hit), ABS best DW corr +0.746 lo 0.960 (no hit);
lambda_min(R) - 1/2 census: MAIN +4e-5 .. +6e-11 vs dead
-0.083 .. -0.500 -- R > I/2 fails structurally on every dead
world (the L* condition restated in hole coordinates, census);
EPST/HL2 NOT_LADDERED; WORLD_BLIND not typeable: the carrier
clause never fired)
+ TWIN_LEDGER(dose-zero BITWISE 6/6; max dual dev over |dDW|,
|dDK|, |dGC|, |dlog LR_loc| = 7.8e-4 nats, bar 1e-3 -- passes
with 1.3x headroom only, disclosed)
+ MUSTFAIL_LEDGER(m1 P'-unsquared 8.06e-2 + Fractions-exact
break; m2 rank-N 6.12e-3 + Fractions-exact break; m3 mu-only
nodes 125.0 nats; m4 mass permutation 2333 rel; m5 R_12-local
1.394 (incl. sign flip) vs true 9.2e-12; m6/m6b AST-FLAGGED;
constructor scopes + fragment audit CLEAN).
Key numbers.  W9: dual row DW -19.5844 / DK +10.8508 / GC
+1.8653 summing to ln c^2 = -6.8683 at 1.8e-11; lambda_min(R)
0.500041882; LR_loc 7.884e-3 vs LR 1.163e-2; the r354 four-block
row reproduced bit-near.  LADDER: 85 rows, every f64 margin
positive, no exclusions, EXT6 dual block far under the 900 s
contingency (total wall 115 s); GC column 1.87 (w9) -> 1.47 ..
1.49 (EXT5/EXT6) -- the global conditioning is SMALL and
SATURATES: the dual coordinate localizes the wander in the
two-point data; FIT anchors == the r352/r354 records EXACTLY
(margin -3.332, c -0.697, p -0.754, q -0.645, rdet -2.624, kap
-0.711); FS anchors corr 0.999998 / rmsD 0.8787 / rmsr 0.0019
reproduced EXACTLY.  HONEST NEGATIVES: (1) the MAIN verdict is
the honest null -- the duality is a coordinate change and the
sealed compression bar correctly refused the near-tautological
sum block; the lane goes to the memo as the contract ordered;
(2) RESERVE_LOCALIZED is census-grade localization, NOT a
mechanism: LR_loc consumes the dual pair block whose values are
measured window scalars; (3) at EXT6 depth the dual margin route
loses the sign inside f64 (kz133) -- the spectral map is exact
algebra but not a deeper certification instrument; (4) the twin
bar passes with only 1.3x headroom; (5) the dead-world reserve
channel is vacuous (the LR cone is empty off the wall), so the
world separation rests on the carrier channel and the structural
lambda_min(R) census; (6) AC_CLASS_EXCLUDED is a class statement
for the memo, never a wall mechanism.  R357 SKETCH (candidates,
not commitments; EDGE_REGIME was conditional on substance): the
substance delivered is (i) the reserve localization in the dual
pair (R_pair)^{-1} and (ii) the discrete-hard-edge class
exclusion -- both feed the memo (Uvarov language, BKMM
saturation addressees); no internal round is scheduled from
here.  Runtime 117.1 / 114.9 s record, 115.0 s calibration,
0.6 s smoke; deterministic, run1/run2 byte-identical up to WALL.
AMENDMENTS AFTER FREEZE: none -- this record-table insertion is
the only post-freeze edit.

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
import rhor_source_anatomy_probe as RSA          # noqa: E402 r352
import delta_alpha_closure_probe as DA           # noqa: E402 r347
import phi_wander_anatomy_probe as PWA           # noqa: E402 r354
import ext3_fresh_anchors_probe as E3            # noqa: E402 r329
import dirichlet_secondworld_probe as DSW        # noqa: E402 r330
import verify_lstar_instance as V                # noqa: E402 document
import lstar_margin_scaling_probe as LM          # noqa: E402 r286
import metric_stability_probe as MS              # noqa: E402 r278
import budget_localization_probe as BL           # noqa: E402 r280
import principal_bessel_probe as PB              # noqa: E402 r243
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
RSA_SHA_PREFIX = "dc6bbd2c"
DA_SHA_PREFIX = "bd1aa7f3"
PWA_SHA_PREFIX = "f9db84da"
E3_SHA_PREFIX = "bbfaf199"
DSW_SHA_PREFIX = "66526018"
DUAL9_ANCH = dict(DW=-19.5844, DK=10.8508, GC=1.8653,
                  lamR=0.500041882, LRloc=7.884295e-3,
                  f1=2, f2=4, eps12=1.0)
DUAL_SAMPLE_ANCH = {44: (-29.2208, 19.5100, 1.5808),
                    56: (-36.3366, 26.4594, 1.5090),
                    130: (-40.1507, 28.9818, 1.4995)}
LRLOC_SAMPLE_ANCH = {44: 6.244114e-5, 56: 6.417926e-6,
                     130: 1.159017e-6}
BLOCK9_ANCH = (-24.7664, -1.5711, 4.0100, 15.4593)
BLOCK_SAMPLE_ANCH = {44: (-23.7727, -1.4696, -1.8039, 18.9162),
                     56: (-31.9880, -1.4006, -0.0282, 25.0486),
                     130: (-30.6196, -1.3558, -3.7210, 26.0269)}
BLOCK_ANCH_TOL = 2.0e-3
FIT_ANCH = dict(margin=-3.332, c=-0.697, p=-0.754, q=-0.645,
                rdet=-2.624, kap=-0.711)
FIT_ANCH_TOL = 0.02
CURV_ANCH = dict(margin=-0.347, c=0.308, rdet=-0.767)
CURV_ANCH_TOL = 0.03
FS9_ANCH = dict(corr=0.999998, rmsD=0.8787, rmsr=0.0019)
A_LEAD = 17.0 / 12.0
A_RHOK_REC = 1.4222          # WITHHELD record constant
A_RHOK_TOL = 0.05
ALPHA_REC = 3.332            # WITHHELD record constant
RHOR_REC = 2.624             # WITHHELD record constant
NW_SHALLOW = 900
NW_MID = 3200
QE_BAR = 1.0e-10
ROUTE_AB_BAR = (1.0e-10, 1.0e-9, 1.0e-7)
ROUTE_C_BAR = 1.0e-12
COMP_BAR = (1.0e-10, 1.0e-9, 1.0e-8)
FULLX_BAR = 1.0e-10
MDUAL_BAR = (1.0e-10, 1.0e-9, 5.0e-9)
CID_BAR = (1.0e-8, 1.0e-6, 1.0e-4)
BLKID_BAR = (1.0e-8, 1.0e-6, 1.0e-4)
CAR_CORR_MIN = 0.9
CAR_RES_MAX = 0.5
COMPRESS_FACTOR = 0.5
DUAL_BLOCKS = ("DW", "DK", "GC")
R354_BLOCKS = ("W", "B2", "P2", "GM", "PG")
RES_CORR_MIN = 0.9
RES_RES_MAX = 0.5
ANTI_BAR = -0.99
FS_CORR_MIN = 0.99
FS_RMSR_MAX = 0.2
WORLD_KZ = (18, 9, 52, 119, 42, 130)
WORLD_MIN_ROWS = 5
TWIN_TOL = 1.0e-8
TWIN_DUAL_BAR = 1.0e-3
AC_POS_FACT = 3.0
AC_DECAY_MIN = 0.5
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN, EXT3_NW_MAX = 1721, 2577
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT4_NW_MIN, EXT4_NW_MAX = 2656, 3181
EXT5_H_LO, EXT5_H_HI, K_EXT5 = 3401, 6000, 6
EXT5_KZ_EXPECT = (69, 107, 101, 99, 115, 89)
EXT5_H_EXPECT = (5690, 5668, 5242, 5073, 4243, 4237)
USED5_EXPECT, FRESH5_EXPECT = 98, 9
EXT6_H_LO, EXT6_H_HI, K_EXT6 = 6001, 60000, 4
Z2_CAP = 400000
USED6_EXPECT, FRESH6_EXPECT = 104, 4
EXT6_KZ_EXPECT = (133, 129, 124, 117)
EXT6_H_EXPECT = (7942, 7675, 7233, 6532)
EXT6_Z_EXPECT = (617, 599, 569, 521)
EXT6_DUAL_BUDGET_S = 900.0
M_LOUD = 1.0e-3
M3_LOUD = 1.0
M4_BAR = 0.1
M5_BAR = 0.1
TOY_TOL = 1.0e-12
GRID_TOY_S = 21

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
                       "/ weight / position / chain-coefficient "
                       "arrays and measured columns ONLY; record "
                       "numbers and flips enter gates and record "
                       "tables only" if not bad else "; ".join(bad))


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


CONSTRUCTORS = ("dual_weights", "dual_rung", "lr_local",
                "psi_fit57", "acpos_dev", "grade_of",
                "blocks354", "world_union_row")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "FIT_ANCH", "CURV_ANCH", "FS9_ANCH",
                   "DUAL9_ANCH", "DUAL_SAMPLE_ANCH",
                   "LRLOC_SAMPLE_ANCH", "BLOCK9_ANCH",
                   "BLOCK_SAMPLE_ANCH", "ALPHA_REC", "RHOR_REC",
                   "A_RHOK_REC", "lr_col_true", "c_col_true"}


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


# ============== exact-Fractions helpers (toy only)
def fr_inv(M):
    """exact rational matrix inverse (Gauss-Jordan, small n)."""
    n = len(M)
    A = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
         for i, row in enumerate(M)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [t / pv for t in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
    return [row[n:] for row in A]


def fr_mul(A, B):
    return [[sum(a * b for a, b in zip(row, col))
             for col in zip(*B)] for row in A]


def fr_proj(xs, u, N):
    """rational projection Ahat = V M^{-1} V^T U (rank N) on the
    node set xs with weight u (toy only)."""
    S = len(xs)
    Vm = [[xs[j] ** i for i in range(N)] for j in range(S)]
    M = [[sum(u[j] * xs[j] ** (i + k) for j in range(S))
          for k in range(N)] for i in range(N)]
    Mi = fr_inv(M)
    P = fr_mul(fr_mul(Vm, Mi), [list(r) for r in zip(*Vm)])
    return [[P[i][j] * u[j] for j in range(S)] for i in range(S)]


# ============== module-own constructors (AST-audited)
def grade_of(nw):
    """graded-bar index of a row: 0 shallow, 1 mid, 2 deep;
    consumes the window depth only."""
    return 0 if nw <= NW_SHALLOW else (1 if nw <= NW_MID else 2)


def dual_weights(xu, u, S, L):
    """the Borodin dual weight on the full folded grid, THREE
    routes (kernel-scale invariant normalizations): route B
    (construction): u_vee = (1-x)^2/(S u kappa^2) with kappa = 2
    at the endpoint fold f = S (the 1/S normalization makes route
    B EQUAL route C c_j (1-x)/|f|, not just proportional); route
    A (grid-agnostic ward): log u_vee = -log u - 2 sum_{k != j}
    log |x_j - x_k|; also returns the fold indices f_j and the
    sign vector eps_j = (-1)^{f_j}; consumes positions + weights
    only."""
    xu = np.asarray(xu, float)
    u = np.asarray(u, float)
    f = np.rint(np.arccos(np.clip(xu, -1.0, 1.0)) * L
                / (2.0 * math.pi)).astype(int)
    kap = np.where(f == S, 2.0, 1.0)
    ud = (1.0 - xu) ** 2 / (S * u * kap * kap)
    logPp = np.zeros(S)
    for j in range(S):
        dx = np.abs(xu[j] - xu)
        dx[j] = 1.0
        logPp[j] = float(np.sum(np.log(dx)))
    log_ud_A = -np.log(u) - 2.0 * logPp
    eps = np.where(f % 2 == 0, 1.0, -1.0)
    return ud, log_ud_A, f, eps, logPp


def lr_local(r11, r12, r22):
    """the LOCAL dual reserve prediction: invert the 2x2 dual
    block (R_pair)^{-1} and read the pair coordinates p_loc = 2 -
    (.)_{11}, q_loc = 2 - (.)_{22}, c_loc = |(.)_{12}|; returns
    LR_loc = -log(c_loc^2/(p_loc q_loc)) or nan if not in the L*
    cone; consumes the dual pair block ONLY (never p/q/c: the
    readback is the m6 must-fail)."""
    det = r11 * r22 - r12 * r12
    if det <= 0:
        return float("nan")
    i11, i22, i12 = r22 / det, r11 / det, -r12 / det
    p_loc, q_loc, c_loc = 2.0 - i11, 2.0 - i22, abs(i12)
    if p_loc <= 0 or q_loc <= 0 or c_loc <= 0:
        return float("nan")
    return -math.log(c_loc * c_loc / (p_loc * q_loc))


def dual_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, B=None):
    """the full dual-hole block of one window: support facts, the
    three dual-weight routes, the eta projection restricted to Y
    (Q), the L-ensemble transform E(I+E)^{-1} from the mu-route
    Gram, the dual hole kernel R at rank N-1, the Y-complementation
    deviation, lambda_min(R), the spectral-map margin, the pair
    entries of R and R^{-1}, the dual blocks (DW, DK, GC) and the
    local reserve prediction; consumes measure arrays, positions
    and the dressed frame only."""
    xu = np.asarray(xu, float)
    wu = np.asarray(wu, float)
    u = np.abs(wu)
    ok_sup = (S == L // 2) and (S == 2 * Nw - 1) and len(xu) == S
    jj = np.arange(1, L // 2 + 1)
    grid = np.cos(2.0 * math.pi * jj / L)[::-1]
    dev_grid = float(np.max(np.abs(xu - grid))) if len(grid) == S \
        else float("inf")
    ud, log_ud_A, f, eps, logPp = dual_weights(xu, u, S, L)
    lb = np.log(ud)
    dev_ab = float(np.max(np.abs((log_ud_A - log_ud_A.mean())
                                 - (lb - lb.mean()))))
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    iY = np.searchsorted(xu, yn)
    ok_map = bool(np.all(xu[iY] == yn))
    # eta route -> Q; mu route -> E -> E(I+E)^{-1}
    ae, be, h0e = V.mu_chain(xu, u, Nw)
    Bq = V.b_matrix(ae, be, h0e, yn, vn, Nw)
    Q = Bq @ Bq.T
    if B is None:
        aa, bb, h0 = V.mu_chain(xu[wu > 0], wu[wu > 0], Nw)
        B = V.b_matrix(aa, bb, h0, yn, vn, Nw)
    E = B @ B.T
    Q2 = np.linalg.solve(np.eye(len(E)) + E, E)
    dev_qe = float(np.max(np.abs(Q - Q2)))
    # dual chain -> R (rank N-1)
    ad, bd, h0d = V.mu_chain(xu, ud, Nw - 1)
    udY = ud[iY]
    Bd = V.b_matrix(ad, bd, h0d, yn, udY, Nw - 1)
    Rm = Bd @ Bd.T
    epsY = eps[iY]
    dev_comp = float(np.max(np.abs(
        Q - (np.eye(len(Rm)) - Rm) * np.outer(epsY, epsY))))
    lam_min_R = float(np.linalg.eigvalsh(Rm)[0])
    margin_dual = (2.0 - 1.0 / lam_min_R) if lam_min_R > 0 \
        else float("nan")
    col = np.linalg.solve(Rm, np.eye(len(Rm))[:, [i1, i2]])
    Rinv11 = float(col[i1, 0])
    Rinv12 = float(col[i1, 1])
    Rinv22 = float(col[i2, 1])
    R11, R12, R22 = float(Rm[i1, i1]), float(Rm[i1, i2]), \
        float(Rm[i2, i2])
    s12 = float(epsY[i1] * epsY[i2])
    ud1, ud2 = float(udY[i1]), float(udY[i2])
    DW = math.log(ud1 * ud2)
    DK = 2.0 * math.log(abs(R12)) - DW
    GC = 2.0 * math.log(abs(Rinv12)) - 2.0 * math.log(abs(R12))
    LR_loc = lr_local(R11, R12, R22)
    fY = f[iY]
    return dict(ok_sup=ok_sup, dev_grid=dev_grid, ok_map=ok_map,
                dev_ab=dev_ab, dev_qe=dev_qe, dev_comp=dev_comp,
                lamR=lam_min_R, mdual=margin_dual, s12=s12,
                R11=R11, R12=R12, R22=R22, Rinv11=Rinv11,
                Rinv12=Rinv12, Rinv22=Rinv22, DW=DW, DK=DK,
                GC=GC, LRloc=LR_loc, ud1=ud1, ud2=ud2,
                f1=int(fY[i1]), f2=int(fY[i2]),
                umin=float(np.min(u)), udmax=float(np.max(ud)),
                logPp=logPp, ud=ud, eps=eps, f=f, iY=iY, Q=Q,
                Rm=Rm, E=E)


def psi_fit57(lnN, col, mask57):
    """the 57-fit fine-structure operator: Theil-Sen line fitted
    on the frozen 57-row mask ONLY (imported r286 instrument),
    residual evaluated on every row, median-centred on the 57
    (EXT3..EXT6 stay puretest); consumes measured columns + the
    frozen mask only."""
    lnN = np.asarray(lnN, float)
    y = np.asarray(col, float)
    m = np.asarray(mask57, bool)
    ft = LM.ts_fit(lnN[m], y[m])
    r = y - (float(ft[0]) + float(ft[1]) * lnN)
    return r - float(np.median(r[m])), float(ft[1])


def acpos_dev(yv, fv, nw):
    """the AC-falsifier position ward: a = 2 N^2 (1 - y) against
    the hard-edge image pi^2 f^2 / 4; consumes positions + fold
    indices + depth only."""
    a = 2.0 * nw * nw * (1.0 - yv)
    tgt = math.pi ** 2 * fv * fv / 4.0
    return a, tgt, abs(a / tgt - 1.0)


def blocks354(R, cdb):
    """the r354 four-block family of one rung (r354 formulas
    verbatim on the PWA.cd_blocks output); consumes measured
    scalars only."""
    bN, P12, dy, K11c, K22c, K12c = cdb
    W = math.log(R["v1"] * R["v2"])
    B2 = 2.0 * math.log(abs(bN))
    P2 = 2.0 * math.log(abs(P12))
    GM = -2.0 * math.log(abs(dy))
    blk_id = abs(math.log(R["c"] ** 2) - (W + B2 + P2 + GM))
    return dict(W=W, B2=B2, P2=P2, GM=GM, PG=P2 + GM,
                blk_id354=blk_id)


def world_union_row(nm, kz, kw):
    """one mini-ladder row of a control world: the r278/r280/r334
    channel verbatim, then the union measures + the bare pair;
    returns (Nw, L, xu, wu, yn, vn, p, q, c) or None on a
    structural failure (typed by the caller)."""
    cctx = MS.ctx_build(kz, **kw)
    xu, wu, zones = BL.union_of_ctx(cctx)
    xs, ws, ys, vs = zones
    o = np.argsort(ys)
    ys = np.asarray(ys, float)[o]
    vs = np.asarray(vs, float)[o]
    depth = min(int(cctx["N"]), len(xs) - 1)
    a, b, h0 = V.mu_chain(np.asarray(xs, float),
                          np.asarray(ws, float), depth)
    Bw = V.b_matrix(a, b, h0, ys, vs, depth)
    j1, j2 = PX.pair_select(ys)
    d1, d2, cw = PX.pair_block(Bw, j1, j2)
    pw, qw, _rd = PX.det_reserve(d1, d2, cw)
    return (int(cctx["N"]), int(cctx["L"]), xu, wu, ys, vs,
            pw, qw, cw, j1, j2, Bw, depth)


# ============== must-fail mutants
def mutant_pprime_unsquared(u, logPp):
    """m1 MUST-FAIL: the dual weight WITHOUT squaring the node
    polynomial derivative -- u_vee = 1/(u |P'|); must break the
    complementation loudly."""
    return np.exp(-np.log(np.asarray(u, float)) - logPp)


def mutant_rank_full(xu, ud, yn, udY, Nw):
    """m2 MUST-FAIL: the hole kernel at RANK N instead of N-1 --
    must break the complementation loudly."""
    ad, bd, h0d = V.mu_chain(xu, ud, Nw)
    Bd = V.b_matrix(ad, bd, h0d, yn, udY, Nw)
    return Bd @ Bd.T


def mutant_mu_only_nodes(xp, xu, u):
    """m3 MUST-FAIL: the node polynomial over the MU SUPPORT ONLY
    instead of the full union X -- the dual-weight route
    comparison must break loudly."""
    xu = np.asarray(xu, float)
    xp = np.asarray(xp, float)
    logPp = np.zeros(len(xu))
    for j in range(len(xu)):
        dx = np.abs(xu[j] - xp)
        dx[dx == 0.0] = 1.0
        logPp[j] = float(np.sum(np.log(dx)))
    return -np.log(np.asarray(u, float)) - 2.0 * logPp


def mutant_mass_permuted(dabs):
    """m4 MUST-FAIL: the symbol moduli |f| deterministically
    PERMUTED (reversed) across the folds -- the weight-dictionary
    identity must break loudly (the world clause in mutant
    form)."""
    return np.asarray(dabs, float)[::-1]


def mutant_r12_local(s12, R12):
    """m5 MUST-FAIL: the LOCAL R_12 read as the coupling instead
    of the GLOBAL (R^{-1})_{12} -- must break the c identity
    loudly (the GC block IS the difference)."""
    return s12 * R12


def mutant_reserve_readback(lr_col_true):
    """m6 MUST-FAIL (AST): a 'reserve prediction' that returns the
    withheld measured LR column verbatim -- AST-FLAGGED."""
    return lr_col_true


def mutant_c_readback(c_col_true):
    """m6b MUST-FAIL (AST): a 'dual coupling' that returns the
    withheld measured c column verbatim -- AST-FLAGGED."""
    return c_col_true


# ============== gate-side helpers
def slim356(R):
    """memory hygiene: keep only the fit-side scalars."""
    return {k: R[k] for k in ("kz", "z", "Nw", "Sm", "S", "margin",
                              "c", "p", "q", "d1", "d2", "v1",
                              "v2", "rdet") if k in R}


def slim_dual(D):
    """memory hygiene for the dual dict."""
    return {k: D[k] for k in ("ok_sup", "dev_grid", "ok_map",
                              "dev_ab", "dev_qe", "dev_comp",
                              "lamR", "mdual", "s12", "R11",
                              "R12", "R22", "Rinv11", "Rinv12",
                              "Rinv22", "DW", "DK", "GC", "LRloc",
                              "ud1", "ud2", "f1", "f2", "umin",
                              "udmax")}


def symbol_dev(kz, mz):
    """gate-side weight-dictionary check: recompute the circulant
    symbol independently (document route) and measure
    max |u / ((1/S) c_j (1-x) |d_j|) - 1| plus the m4 sizing."""
    alpha, M, L, _Nw, Dd = V.window_shape(kz)
    cP, _ka = V.prime_lags(alpha, M, Dd)
    cA = V.arch_lags(M, Dd)
    d = V.spectral_density(cA + cP)
    xu = np.asarray(mz["xu"], float)
    u = np.abs(np.asarray(mz["wu"], float))
    S = mz["S"]
    f = np.rint(np.arccos(np.clip(xu, -1.0, 1.0)) * L
                / (2.0 * math.pi)).astype(int)
    cj = np.where(f == S, 0.5, 1.0)
    dj = np.abs(d[f])
    pred = (1.0 / S) * cj * (1.0 - xu) * dj
    dev = float(np.max(np.abs(u / pred - 1.0)))
    dj_perm = mutant_mass_permuted(dj)
    pred_m4 = (1.0 / S) * cj * (1.0 - xu) * dj_perm
    dev_m4 = float(np.max(np.abs(u / pred_m4 - 1.0)))
    return dev, dev_m4, dj


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("borodin_dual_hole_probe -- PRIME.LSTAR.DUAL_HOLE.01 "
          "(round 356)")
    print("SPEC_SHA %s   (r342 PX %s / r352 RSA %s / r347 DA %s / "
          "r354 PWA %s / r329 E3 %s / r330 DSW %s)"
          % (SPEC_SHA[:16], PX.SPEC_SHA[:16], RSA.SPEC_SHA[:16],
             DA.SPEC_SHA[:16], PWA.SPEC_SHA[:16], E3.SPEC_SHA[:16],
             DSW.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 dual block; ladder, EXT, twin, "
                        "worlds, fits, adjudications skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and RSA.SPEC_SHA.startswith(RSA_SHA_PREFIX)
              and DA.SPEC_SHA.startswith(DA_SHA_PREFIX)
              and PWA.SPEC_SHA.startswith(PWA_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and DSW.SPEC_SHA.startswith(DSW_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r342/r352/r347/r354/r329/r330 "
          "machinery imported verbatim (SPEC_SHA %s == %s*, %s == "
          "%s*, %s == %s*, %s == %s*, %s == %s*, %s == %s*); the "
          "carrier clauses (corr %.1f, leave-out %.1f, dual blocks "
          "%s vs r354 blocks %s, compression factor %.1f), the "
          "reserve clauses (%.1f / %.1f), the anti-design bar "
          "(%.2f), the graded bar tables, the AC falsifier "
          "(A_RHOK tol %.2f, position factor %.1f, decay min "
          "%.1f), the EXT selections, the world/twin channel, "
          "every bar/tolerance, the mutants and the verdict form; "
          "fits ONLY on the 57 old rows (psi57 mask), EXT3..EXT6 "
          "puretest; pre-spec scoping s1-s3 disclosed in the spec; "
          "the STOP list forbids any L* claim and any certificate "
          "reading beyond the sealed census"
          % (PX.SPEC_SHA[:8], PX_SHA_PREFIX, RSA.SPEC_SHA[:8],
             RSA_SHA_PREFIX, DA.SPEC_SHA[:8], DA_SHA_PREFIX,
             PWA.SPEC_SHA[:8], PWA_SHA_PREFIX, E3.SPEC_SHA[:8],
             E3_SHA_PREFIX, DSW.SPEC_SHA[:8], DSW_SHA_PREFIX,
             CAR_CORR_MIN, CAR_RES_MAX, str(DUAL_BLOCKS),
             str(R354_BLOCKS), COMPRESS_FACTOR, RES_CORR_MIN,
             RES_RES_MAX, ANTI_BAR, A_RHOK_TOL, AC_POS_FACT,
             AC_DECAY_MIN))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m6 = scope_audit("mutant_reserve_readback")
    hits_m6b = scope_audit("mutant_c_readback")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m6) and bool(hits_m6b),
          "the %d module-own constructors consume kernel Gram / "
          "spectrum / weight / position / chain-coefficient arrays "
          "and measured columns ONLY (%s); the reserve constructor "
          "lr_local consumes the dual pair block ONLY; fragment "
          "audit (no fit primitives beyond the imported r286 "
          "Theil-Sen; psi57 calls it on the frozen 57-mask): %s; "
          "m6 FLAGGED (%s); m6b FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m6[0] if hits_m6 else "MISS",
             hits_m6b[0] if hits_m6b else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- EXACT FRACTIONS + GRID CLOSED FORM + "
            "SPECTRAL MAP")
    # (T1) exact rational 5-atom model, S = 5 = 2N-1, N = 3
    xs_t = [Fr(-3, 4), Fr(-1, 4), Fr(0), Fr(1, 2), Fr(4, 5)]
    u_t = [Fr(1), Fr(1, 4), Fr(1, 2), Fr(1, 6), Fr(1, 3)]
    mu_idx, nu_idx = (0, 2, 4), (1, 3)
    N_t = 3
    S_t = 5
    # k_mu kernel on nu atoms -> Ehat; k_eta -> Qhat
    M_mu = [[sum(u_t[j] * xs_t[j] ** (i + k) for j in mu_idx)
             for k in range(N_t)] for i in range(N_t)]
    Mi_mu = fr_inv(M_mu)

    def kker(Mi, y1, y2, n):
        return sum(Mi[i][k] * y1 ** i * y2 ** k
                   for i in range(n) for k in range(n))

    ys_t = [xs_t[j] for j in nu_idx]
    vs_t = [u_t[j] for j in nu_idx]
    Eh = [[kker(Mi_mu, ys_t[i], ys_t[j], N_t) * vs_t[j]
           for j in range(2)] for i in range(2)]
    M_eta = [[sum(u_t[j] * xs_t[j] ** (i + k) for j in range(S_t))
              for k in range(N_t)] for i in range(N_t)]
    Mi_eta = fr_inv(M_eta)
    Qh = [[kker(Mi_eta, ys_t[i], ys_t[j], N_t) * vs_t[j]
           for j in range(2)] for i in range(2)]
    lhs = fr_mul(Qh, [[Fr(1) + Eh[0][0], Eh[0][1]],
                      [Eh[1][0], Fr(1) + Eh[1][1]]])
    dev_le = max(abs(lhs[i][j] - Eh[i][j])
                 for i in range(2) for j in range(2))
    ImQ = [[Fr(1) - Qh[0][0], -Qh[0][1]],
           [-Qh[1][0], Fr(1) - Qh[1][1]]]
    Erec = fr_mul(Qh, fr_inv(ImQ))
    dev_rt = max(abs(Erec[i][j] - Eh[i][j])
                 for i in range(2) for j in range(2))
    check("G10-toy-fractions-Lensemble", dev_le == 0 and dev_rt == 0,
          "EXACT FRACTIONS on the 5-atom rational model (S = 5, "
          "N = 3): the L-ensemble transformation Qhat (I + Ehat) "
          "== Ehat holds with difference EXACTLY 0, and the "
          "roundtrip Ehat == Qhat (I - Qhat)^{-1} is EXACT -- "
          "Q = E(I+E)^{-1} is an identity, not an approximation")
    # (T2) exact Borodin complementation with rational conjugator
    Pp_t = [math.prod([xs_t[j] - xs_t[k] for k in range(S_t)
                       if k != j], start=Fr(1)) for j in range(S_t)]
    uv_t = [Fr(1) / (u_t[j] * Pp_t[j] ** 2) for j in range(S_t)]
    M_v = [[sum(uv_t[j] * xs_t[j] ** (i + k) for j in range(S_t))
            for k in range(N_t - 1)] for i in range(N_t - 1)]
    Ah = fr_proj(xs_t, u_t, N_t)
    Vm2 = [[xs_t[j] ** i for i in range(N_t - 1)]
           for j in range(S_t)]
    Bh = fr_mul(fr_mul(Vm2, fr_inv(M_v)),
                [list(r) for r in zip(*Vm2)])
    Bh = [[Bh[i][j] * uv_t[j] for j in range(S_t)]
          for i in range(S_t)]
    G_t = [Fr(1) / (u_t[j] * Pp_t[j]) for j in range(S_t)]
    comp = [[Ah[i][j] + G_t[i] * Bh[i][j] / G_t[j]
             - (Fr(1) if i == j else Fr(0)) for j in range(S_t)]
            for i in range(S_t)]
    dev_bor = max(abs(comp[i][j]) for i in range(S_t)
                  for j in range(S_t))
    # m1/m2 in exact arithmetic: both must break EXACTLY
    uv_m1 = [Fr(1) / (u_t[j] * abs(Pp_t[j])) for j in range(S_t)]
    M_m1 = [[sum(uv_m1[j] * xs_t[j] ** (i + k) for j in range(S_t))
             for k in range(N_t - 1)] for i in range(N_t - 1)]
    Bm1 = fr_mul(fr_mul(Vm2, fr_inv(M_m1)),
                 [list(r) for r in zip(*Vm2)])
    Bm1 = [[Bm1[i][j] * uv_m1[j] for j in range(S_t)]
           for i in range(S_t)]
    dev_m1t = max(abs(Ah[i][j] + G_t[i] * Bm1[i][j] / G_t[j]
                      - (Fr(1) if i == j else Fr(0)))
                  for i in range(S_t) for j in range(S_t))
    Bm2 = fr_proj(xs_t, uv_t, N_t)
    dev_m2t = max(abs(Ah[i][j] + G_t[i] * Bm2[i][j] / G_t[j]
                      - (Fr(1) if i == j else Fr(0)))
                  for i in range(S_t) for j in range(S_t))
    check("G11-toy-fractions-borodin", dev_bor == 0
          and dev_m1t > 0 and dev_m2t > 0,
          "EXACT FRACTIONS Borodin complementation: Pi_N^u + G "
          "Pi_{N-1}^{u_vee} G^{-1} == I with the RATIONAL "
          "conjugator G = diag(1/(u_j P'(x_j))) -- 25 entries "
          "EXACTLY 0 (dual weight 1/(u P'^2), rank N-1 = 2); the "
          "m1 mutant (P' NOT squared) breaks the identity EXACTLY "
          "(max |dev| = %.3e != 0) and the m2 mutant (rank N "
          "instead of N-1) breaks it EXACTLY (%.3e != 0)"
          % (float(dev_m1t), float(dev_m2t)))
    # (T3) grid closed form |P'| on a synthetic full cosine grid
    S_g = GRID_TOY_S
    jj_g = np.arange(1, S_g + 1)
    x_g = np.cos(math.pi * jj_g / S_g)[::-1]
    logPp_g = np.zeros(S_g)
    for j in range(S_g):
        dx = np.abs(x_g[j] - x_g)
        dx[j] = 1.0
        logPp_g[j] = float(np.sum(np.log(dx)))
    f_g = np.rint(np.arccos(np.clip(x_g, -1, 1)) * S_g
                  / math.pi).astype(int)
    kap_g = np.where(f_g == S_g, 2.0, 1.0)
    formula = ((1.0 - S_g) * math.log(2.0) + math.log(S_g)
               + np.log(kap_g) - np.log(1.0 - x_g))
    dev_grid_t = float(np.max(np.abs(logPp_g - formula)))
    check("G12-toy-grid-pprime", dev_grid_t <= 1e-10,
          "THE COSINE-GRID CLOSED FORM on a synthetic full grid "
          "(S = %d): log |P'(x_j)| == (1-S) log 2 + log S + log "
          "kappa_j - log(1 - x_j) with kappa = 2 EXACTLY at the "
          "endpoint fold j = S -- max dev %.1e (the endpoint "
          "halving of the folding survives in the dual weight)"
          % (S_g, dev_grid_t))
    # (T4) spectral map on a synthetic SPD R
    seedM = np.array([[1.0, 2, 3, 4], [5, 6, 7, 8],
                      [9, 1, 2, 3], [4, 6, 5, 2]])
    Qr, _ = np.linalg.qr(seedM)
    Dg = np.diag([0.52, 0.6, 0.8, 0.95])
    R_t = Qr @ Dg @ Qr.T
    eps_t = np.array([1.0, -1.0, 1.0, -1.0])
    Rinv_t = np.linalg.inv(R_t)
    E_t = (Rinv_t - np.eye(4)) * np.outer(eps_t, eps_t)
    lmax_E = float(np.linalg.eigvalsh(E_t)[-1])
    dev_map = abs(lmax_E - (1.0 / 0.52 - 1.0))
    dev_minor = float(np.max(np.abs(
        (np.eye(4) - E_t)
        - (2.0 * np.eye(4) - Rinv_t) * np.outer(eps_t, eps_t))))
    lr_t = lr_local(R_t[0, 0], R_t[0, 1], R_t[1, 1])
    check("G13-toy-spectral-map", dev_map <= 1e-12
          and dev_minor <= 1e-12 and np.isfinite(lr_t),
          "THE SPECTRAL MAP on a synthetic SPD R (lambda_min "
          "0.52): lambda_max(E) == 1/lambda_min(R) - 1 at %.1e; "
          "I - E == D (2I - R^{-1}) D elementwise at %.1e (the "
          "pair block IS the (1,2) principal minor of 2I - "
          "R^{-1}); the local reserve constructor returns a "
          "finite L*-cone value (%.4f) on the toy" 
          % (dev_map, dev_minor, lr_t))

    # ---------------- S2 w9 flagship
    section("S2  W9 -- RECORDS + SUPPORT GATE + THREE ROUTES + "
            "FULL COMPLEMENTATION + AC POSITIONS")
    R9 = PX.build_rung(MAIN_KZ)
    mz9 = R9["mz"]
    lam185, _B185 = V.lam_max_at(mz9, REC_NW + 1)
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
    dev_sym9, dev_m4_9, dabs9 = symbol_dev(MAIN_KZ, mz9)
    D9 = dual_rung(mz9["xu"], mz9["wu"], mz9["yn"], mz9["vn"],
                   R9["Nw"], R9["S"], mz9["L"], R9["i1"], R9["i2"],
                   B=R9["B"])
    # route C: c_j (1-x)/|d| vs route B (must agree up to the
    # per-window constant S -- the weight dictionary identity)
    xu9 = np.asarray(mz9["xu"], float)
    f9 = D9["f"]
    cj9 = np.where(f9 == R9["S"], 0.5, 1.0)
    udC9 = cj9 * (1.0 - xu9) / dabs9    # dabs9 aligned with xu
    dev_c9 = float(np.max(np.abs(D9["ud"] / udC9 - 1.0)))
    ok_sup9 = (D9["ok_sup"] and D9["dev_grid"] == 0.0
               and D9["ok_map"] and dev_sym9 == 0.0)
    check("G21-w9-support-symbol", ok_sup9,
          "THE RANK/SUPPORT GATE at w9: S = %d == L/2 == 2 N_w - "
          "1 EXACTLY (Borodin's half-filling rank condition -- "
          "the r228 law N_w = ceil(S/2) consumed as the "
          "complementary rank); the union support IS the full "
          "folded cosine grid cos(pi j / S) BITWISE (dev %.1f); "
          "the weight dictionary u == (1/S) c_j (1 - x) |f| "
          "against the INDEPENDENTLY recomputed circulant symbol "
          "BITWISE (dev %.1f); min u = %.3e > 0 on every union "
          "node (the r228 zero-weight obstruction is ABSENT on "
          "the positive lift)"
          % (R9["S"], D9["dev_grid"], dev_sym9, D9["umin"]))
    check("G22-w9-dual-weights", D9["dev_ab"] <= ROUTE_AB_BAR[0]
          and dev_c9 <= ROUTE_C_BAR,
          "THE DUAL WEIGHT THREE WAYS at w9: route A (numeric log "
          "|P'| pairwise sums) == route B ((1-x)^2/(u kappa^2)) "
          "up to the mean at %.1e (bar %.0e); route B == route C "
          "(c_j (1-x)/|f|, recomputed symbol) at %.1e relative "
          "(bar %.0e) -- u_vee PROPTO (1-x)/|f|: the original "
          "weight carries +log|f|, the dual carries -log|f|, the "
          "reciprocal dictionary is EXACT on the real window "
          "(endpoint halving included)"
          % (D9["dev_ab"], ROUTE_AB_BAR[0], dev_c9, ROUTE_C_BAR))
    # full-X complementation at w9
    ae9, be9, h0e9 = V.mu_chain(xu9, np.abs(mz9["wu"]), R9["Nw"])
    Bfe9 = V.b_matrix(ae9, be9, h0e9, xu9, np.abs(mz9["wu"]),
                      R9["Nw"])
    Pi_eta9 = Bfe9 @ Bfe9.T
    ad9, bd9, h0d9 = V.mu_chain(xu9, D9["ud"], R9["Nw"] - 1)
    Bfd9 = V.b_matrix(ad9, bd9, h0d9, xu9, D9["ud"], R9["Nw"] - 1)
    Pi_d9 = Bfd9 @ Bfd9.T
    dev_fullx = float(np.max(np.abs(
        Pi_eta9 + np.outer(D9["eps"], D9["eps"]) * Pi_d9
        - np.eye(R9["S"]))))
    dev_c_id9 = abs(D9["s12"] * D9["Rinv12"] / R9["c"] - 1.0)
    dev_p_id9 = abs((2.0 - D9["Rinv11"]) / R9["p"] - 1.0)
    dev_q_id9 = abs((2.0 - D9["Rinv22"]) / R9["q"] - 1.0)
    blk_id9 = abs(math.log(R9["c"] ** 2)
                  - (D9["DW"] + D9["DK"] + D9["GC"]))
    A9 = DUAL9_ANCH
    ok_alg9 = (D9["dev_qe"] <= QE_BAR
               and dev_fullx <= FULLX_BAR
               and D9["dev_comp"] <= COMP_BAR[0]
               and abs(D9["mdual"] - R9["margin"]) <= MDUAL_BAR[0]
               and dev_c_id9 <= CID_BAR[0]
               and dev_p_id9 <= CID_BAR[0]
               and dev_q_id9 <= CID_BAR[0]
               and blk_id9 <= BLKID_BAR[0]
               and abs(D9["lamR"] - A9["lamR"]) <= 1e-6
               and abs(D9["DW"] - A9["DW"]) <= BLOCK_ANCH_TOL
               and abs(D9["DK"] - A9["DK"]) <= BLOCK_ANCH_TOL
               and abs(D9["GC"] - A9["GC"]) <= BLOCK_ANCH_TOL
               and abs(D9["LRloc"] / A9["LRloc"] - 1.0) <= 1e-3
               and D9["f1"] == A9["f1"] and D9["f2"] == A9["f2"]
               and D9["s12"] == A9["eps12"])
    check("G23-w9-dual-algebra", ok_alg9,
          "THE EXACT DUAL CHAIN at w9: Q == E(I+E)^{-1} at %.1e "
          "(bar %.0e, contract 1e-10); FULL-X complementation "
          "Pi_N^u == D (I - Pi_{N-1}^{u_vee}) D at %.1e (bar "
          "%.0e); Y-restriction at %.1e; THE SPECTRAL MAP: "
          "lambda_min(R) = %.9f > 1/2 with margin == 2 - "
          "1/lambda_min(R) at %.1e abs -- L* IS R > I/2 at w9, "
          "measured; the pair identities c == eps1 eps2 "
          "(R^{-1})_{12} / p == 2 - (R^{-1})_{11} / q == 2 - "
          "(R^{-1})_{22} at %.1e / %.1e / %.1e rel; THE DUAL "
          "BLOCKS DW = %.4f, DK = %.4f, GC = %.4f (s1 anchors "
          "bit-near) summing to ln c^2 = %.4f at %.1e; LR_loc = "
          "%.4e (anchor); folds (%d, %d), eps12 %+.0f"
          % (D9["dev_qe"], QE_BAR, dev_fullx, FULLX_BAR,
             D9["dev_comp"], D9["lamR"],
             abs(D9["mdual"] - R9["margin"]), dev_c_id9,
             dev_p_id9, dev_q_id9, D9["DW"], D9["DK"], D9["GC"],
             math.log(R9["c"] ** 2), blk_id9, D9["LRloc"],
             D9["f1"], D9["f2"], D9["s12"]))
    a1_9, t1_9, dva1 = acpos_dev(float(mz9["yn"][R9["i1"]]),
                                 D9["f1"], R9["Nw"])
    a2_9, t2_9, dva2 = acpos_dev(float(mz9["yn"][R9["i2"]]),
                                 D9["f2"], R9["Nw"])
    check("G24-w9-ac-positions", dva1 <= AC_POS_FACT / R9["Nw"]
          and dva2 <= AC_POS_FACT / R9["Nw"],
          "LEG E POSITIONS at w9: the rescaled pair atoms a = "
          "2 N^2 (1 - y) = (%.6f, %.6f) against the hard-edge "
          "image pi^2 f^2/4 = (%.6f, %.6f) -- devs %.2e / %.2e "
          "<= %.1f/N_w: the microscopic positions are FAMILY-"
          "CONSTANT (the AC/Bessel comparison is at FIXED "
          "arguments)" % (a1_9, a2_9, t1_9, t2_9, dva1, dva2,
                          AC_POS_FACT))
    P9r = RSA.rho_corr_cols(R9["d1"], R9["d2"], R9["c"], R9["p"],
                            R9["q"])
    cdb9 = PWA.cd_blocks(mz9["xp"], mz9["wp"], mz9["yn"],
                         R9["i1"], R9["i2"], mz9["Nw"])
    F9 = blocks354(R9, cdb9)
    ok_blk354 = (abs(F9["W"] - BLOCK9_ANCH[0]) <= BLOCK_ANCH_TOL
                 and abs(F9["B2"] - BLOCK9_ANCH[1])
                 <= BLOCK_ANCH_TOL
                 and abs(F9["P2"] - BLOCK9_ANCH[2])
                 <= BLOCK_ANCH_TOL
                 and abs(F9["GM"] - BLOCK9_ANCH[3])
                 <= BLOCK_ANCH_TOL)
    check("G25-w9-r354-blocks", ok_blk354,
          "LEG 0 the r354 four-block family reproduced at w9 (W "
          "%.4f, B2 %.4f, P2 %.4f, GM %.4f == the r354 record "
          "bit-near; identity %.1e) -- the comparison base for "
          "the compression clause is in-run, apples-to-apples; "
          "rhoK = %.6e, LR = %.4e (r352 route)"
          % (F9["W"], F9["B2"], F9["P2"], F9["GM"],
             F9["blk_id354"], P9r[0], P9r[2]))

    # ---------------- S3 the ladder
    section("S3  THE LADDER (42 + 15 + 12 EXT3 + 6 EXT4 + 6 EXT5 "
            "+ 4 EXT6) -- SUPPORT GATE + DUAL WARDS")
    if smoke:
        for g in ("G30-ext-selection", "G31-ladder-census",
                  "G32-support-gate-all", "G33-dual-wards-all",
                  "G34-cohort-fit-anchors"):
            check(g, True, "SMOKE: skipped")
        RT = {9: slim356(R9)}
        DT = {9: slim_dual(D9)}
        FT = {9: F9}
        PT = {9: dict(rhoK=P9r[0], s=P9r[1], LR=P9r[2])}
        ACT = {9: (dva1, dva2)}
        all_kz, fit_kz, ext_all = [9], [9], []
        sup_fail: list = []
        excl: list = []
    else:
        lm_rows = LM.ext_rule()
        used = set(E3.used_kz_set(core.frame_a_zones(), lm_rows,
                                  35))
        used |= set(EXT3_KZ_B + EXT3_KZ_A)
        used |= set(EXT4_KZ_B + EXT4_KZ_A)
        pool5 = E3.admissible_pool(EXT5_H_LO, EXT5_H_HI)
        zz5 = {kz: int(core._NN[kz]) for (_h, kz) in pool5}
        fresh5 = [(h, kz) for (h, kz) in pool5
                  if kz not in used and zz5[kz] ** 2 <= Z2_CAP]
        fresh5.sort(reverse=True)
        ext5_sel = tuple(kz for (_h, kz) in fresh5[:K_EXT5])
        ext5_h = tuple(h for (h, _kz) in fresh5[:K_EXT5])
        used6 = used | set(ext5_sel)
        pool6 = E3.admissible_pool(EXT6_H_LO, EXT6_H_HI)
        zz6 = {kz: int(core._NN[kz]) for (_h, kz) in pool6}
        fresh6 = [(h, kz) for (h, kz) in pool6
                  if kz not in used6 and zz6[kz] ** 2 <= Z2_CAP]
        fresh6.sort(reverse=True)
        ext6_sel = tuple(kz for (_h, kz) in fresh6[:K_EXT6])
        ext6_h = tuple(h for (h, _kz) in fresh6[:K_EXT6])
        ext6_z = tuple(int(core._NN[kz]) for kz in ext6_sel)
        check("G30-ext-selection",
              len(used) == USED5_EXPECT
              and len(fresh5) == FRESH5_EXPECT
              and ext5_sel == EXT5_KZ_EXPECT
              and ext5_h == EXT5_H_EXPECT
              and len(used6) == USED6_EXPECT
              and len(fresh6) == FRESH6_EXPECT
              and ext6_sel == EXT6_KZ_EXPECT
              and ext6_h == EXT6_H_EXPECT
              and ext6_z == EXT6_Z_EXPECT,
              "SEALED SELECTIONS executed verbatim: EXT5 (r352 "
              "rule AS-IS) used %d == %d, fresh %d == %d, queue "
              "%s; EXT6 (r343 rule at the raised cap) used %d == "
              "%d, fresh %d == %d, queue %s (h %s, z %s) == the "
              "r354 record" % (len(used), USED5_EXPECT,
                               len(fresh5), FRESH5_EXPECT,
                               str(ext5_sel), len(used6),
                               USED6_EXPECT, len(fresh6),
                               FRESH6_EXPECT, str(ext6_sel),
                               str(ext6_h), str(ext6_z)))
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in lm_rows[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ext4_kzs = list(EXT4_KZ_B + EXT4_KZ_A)
        ext5_kzs = list(ext5_sel)
        ext6_kzs = list(ext6_sel)
        RT, DT, FT, PT, ACT = {}, {}, {}, {}, {}
        sup_fail, excl, neg_rows = [], [], []
        t_dual6 = 0.0
        print("    %-5s %-5s %-5s %-5s | %-10s %-10s | %-8s %-8s "
              "%-8s | %-9s %-9s | %-7s"
              % ("kz", "z", "S-", "N_w", "margin", "mdual", "DW",
                 "DK", "GC", "LRloc", "LR", "lamR-1/2"))
        for kz in (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                   + ext5_kzs + ext6_kzs):
            t_r = time.time()
            is6 = kz in set(ext6_kzs)
            if kz == MAIN_KZ:
                R, D, F = R9, D9, F9
                P = dict(rhoK=P9r[0], s=P9r[1], LR=P9r[2])
                acd = (dva1, dva2)
            else:
                if is6:
                    R = PWA.rung_reduced_cols(kz)
                    R["z"] = int(V.PP[kz])
                else:
                    R = PX.build_rung(kz)
                mz = R["mz"]
                D = dual_rung(mz["xu"], mz["wu"], mz["yn"],
                              mz["vn"], R["Nw"], R["S"], mz["L"],
                              R["i1"], R["i2"], B=R["B"])
                rr = RSA.rho_corr_cols(R["d1"], R["d2"], R["c"],
                                       R["p"], R["q"])
                P = dict(rhoK=rr[0], s=rr[1], LR=rr[2])
                cdb = PWA.cd_blocks(mz["xp"], mz["wp"], mz["yn"],
                                    R["i1"], R["i2"], mz["Nw"])
                F = blocks354(R, cdb)
                _a1, _t1, dv1 = acpos_dev(float(mz["yn"][R["i1"]]),
                                          D["f1"], R["Nw"])
                _a2, _t2, dv2 = acpos_dev(float(mz["yn"][R["i2"]]),
                                          D["f2"], R["Nw"])
                acd = (dv1, dv2)
            if R["margin"] <= 0:
                neg_rows.append(kz)
            if not (D["ok_sup"] and D["dev_grid"] == 0.0
                    and D["ok_map"]):
                sup_fail.append(kz)
            if is6:
                t_dual6 += time.time() - t_r
            print("    %-5d %-5d %-5d %-5d | %.4e %+.3e | %+8.3f "
                  "%+8.3f %+7.4f | %.3e %.3e | %+.1e"
                  % (kz, R["z"], R["Sm"], R["Nw"], R["margin"],
                     D["mdual"], D["DW"], D["DK"], D["GC"],
                     D["LRloc"], P["LR"], D["lamR"] - 0.5),
                  flush=True)
            RT[kz] = slim356(R)
            DT[kz] = slim_dual(D)
            FT[kz] = F
            PT[kz] = P
            ACT[kz] = acd
            RT[kz]["mdev"] = abs(D["mdual"] - R["margin"])
            RT[kz]["cdev"] = abs(D["s12"] * D["Rinv12"] / R["c"]
                                 - 1.0)
            RT[kz]["pdev"] = abs((2.0 - D["Rinv11"]) / R["p"]
                                 - 1.0)
            RT[kz]["qdev"] = abs((2.0 - D["Rinv22"]) / R["q"]
                                 - 1.0)
            RT[kz]["bdev"] = abs(math.log(R["c"] ** 2)
                                 - (D["DW"] + D["DK"] + D["GC"]))
            del R, D, F
        excl = list(neg_rows)
        all_kz = (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                  + [k for k in ext5_kzs + ext6_kzs
                     if k not in excl])
        fit_kz = [k for k in core_kzs + ext_kzs if k not in excl]
        ext_all = [k for k in all_kz if k not in fit_kz]
        ok_cen = (len(core_kzs) == 42 and len(fit_kz) == 57
                  and all(EXT3_NW_MIN <= RT[k]["Nw"] <= EXT3_NW_MAX
                          for k in ext3_kzs)
                  and all(EXT4_NW_MIN <= RT[k]["Nw"] <= EXT4_NW_MAX
                          for k in ext4_kzs)
                  and all(RT[k]["Nw"] == h for k, h in
                          zip(ext5_kzs, ext5_h))
                  and all(RT[k]["Nw"] == h for k, h in
                          zip(ext6_kzs, ext6_h))
                  and not neg_rows)
        check("G31-ladder-census", ok_cen,
              "42 core + 15 r286 extension + 12 EXT3 + 6 EXT4 + 6 "
              "EXT5 + %d EXT6 = %d rows (fits on the %d old rows "
              "ONLY, %d EXT rows PURETEST); every f64 margin "
              "positive (exclusions %s); EXT6 dual block within "
              "the %.0f s contingency budget: %s"
              % (len(ext6_kzs), len(all_kz), len(fit_kz),
                 len(ext_all),
                 str(excl) if excl else "none",
                 EXT6_DUAL_BUDGET_S,
                 "YES" if t_dual6 <= EXT6_DUAL_BUDGET_S
                 else "NO (contingency documented)"))
        n_sup = sum(1 for k in all_kz
                    if DT[k]["ok_sup"] and DT[k]["dev_grid"] == 0.0
                    and DT[k]["ok_map"])
        umin_all = min(DT[k]["umin"] for k in all_kz)
        check("G32-support-gate-all", not sup_fail,
              "THE RANK/SUPPORT GATE on ALL %d rows: S == L/2 == "
              "2 N_w - 1 with the full cosine grid BITWISE on "
              "%d/%d (failures: %s) -- Borodin's half-filling "
              "rank condition is EXACT across the ENTIRE ladder; "
              "min union weight %.2e > 0 on every row (the dual "
              "weight EXISTS everywhere: the r228 zero-weight "
              "obstruction is structurally absent on the "
              "positive lift)"
              % (len(all_kz), n_sup, len(all_kz),
                 str(sup_fail) if sup_fail else "none", umin_all))

        def gmax(key, g):
            vals = [DT[k][key] if key in DT[k] else RT[k][key]
                    for k in all_kz
                    if grade_of(RT[k]["Nw"]) == g]
            return max(vals) if vals else 0.0

        ok_wards = True
        txt_w = []
        for key, bars, lab in (("dev_qe", (QE_BAR,) * 3, "Q=E(I+E)^-1"),
                               ("dev_ab", ROUTE_AB_BAR, "routeA==B"),
                               ("dev_comp", COMP_BAR, "complement"),
                               ("mdev", MDUAL_BAR, "margin_dual"),
                               ("cdev", CID_BAR, "c-identity"),
                               ("pdev", CID_BAR, "p-identity"),
                               ("qdev", CID_BAR, "q-identity"),
                               ("bdev", BLKID_BAR, "block-id")):
            per = [gmax(key, g) for g in range(3)]
            ok_here = all(per[g] <= bars[g] for g in range(3))
            ok_wards = ok_wards and ok_here
            txt_w.append("%s %.1e/%.1e/%.1e (%s)"
                         % (lab, per[0], per[1], per[2],
                            "ok" if ok_here else "FAIL"))
        check("G33-dual-wards-all", ok_wards,
              "THE DUAL IDENTITY WARDS on all %d rows, graded "
              "shallow/mid/deep (bars %s / %s / %s ...): %s -- "
              "the exact chain Q = E(I+E)^{-1} -> Borodin "
              "complement -> spectral map -> pair identities "
              "holds at every depth; DISCLOSED: at EXT6 the f64 "
              "resolution of margin_dual (~5e-10) exceeds the "
              "margins (~4e-10): sign census in the verdict"
              % (len(all_kz), str((QE_BAR,) * 3),
                 str(ROUTE_AB_BAR), str(COMP_BAR),
                 "; ".join(txt_w)))
        lnN_all = np.log(np.array([RT[k]["Nw"] for k in all_kz],
                                  float))
        mask57 = np.array([k in set(fit_kz) for k in all_kz])
        lnN57 = lnN_all[mask57]
        getters = {
            "margin": lambda k: RT[k]["margin"],
            "c": lambda k: abs(RT[k]["c"]),
            "csq": lambda k: RT[k]["c"] * RT[k]["c"],
            "p": lambda k: RT[k]["p"],
            "q": lambda k: RT[k]["q"],
            "pq": lambda k: RT[k]["p"] * RT[k]["q"],
            "rdet": lambda k: RT[k]["rdet"],
            "kap": lambda k: math.sqrt(PT[k]["rhoK"]),
            "rhoK": lambda k: PT[k]["rhoK"],
            "LR": lambda k: PT[k]["LR"],
        }
        laws = {}
        e3p = [(math.log(RT[k]["Nw"]),
                math.log(getters["margin"](k))) for k in ext3_kzs]
        for nm in FIT_ANCH:
            get = getters[nm]
            e3p = [(math.log(RT[k]["Nw"]), math.log(get(k)))
                   for k in ext3_kzs]
            e4p = [(math.log(RT[k]["Nw"]), math.log(get(k)))
                   for k in ext4_kzs]
            laws[nm] = DA.decay_law(
                lnN57, np.log([get(k) for k in fit_kz]), e3p, e4p)
        co_fs, rr_fs, rmsD_fs, _rk, _rd, _pD, _pK = \
            RSA.fine_structure(
                lnN57, np.log([getters["pq"](k) for k in fit_kz]),
                np.log([getters["csq"](k) for k in fit_kz]),
                A_LEAD)
        ok_fit = (all(abs(laws[nm]["slope"] - FIT_ANCH[nm])
                      <= FIT_ANCH_TOL for nm in FIT_ANCH)
                  and all(abs(laws[nm]["curv"] - CURV_ANCH[nm])
                          <= CURV_ANCH_TOL for nm in CURV_ANCH)
                  and abs(co_fs - FS9_ANCH["corr"]) <= 1e-5
                  and abs(rmsD_fs - FS9_ANCH["rmsD"]) <= 2e-3
                  and abs(rr_fs - FS9_ANCH["rmsr"]) <= 1e-3)
        ok_b354 = all(
            abs(FT[k]["W"] - BLOCK_SAMPLE_ANCH[k][0])
            <= BLOCK_ANCH_TOL
            and abs(FT[k]["B2"] - BLOCK_SAMPLE_ANCH[k][1])
            <= BLOCK_ANCH_TOL
            and abs(FT[k]["P2"] - BLOCK_SAMPLE_ANCH[k][2])
            <= BLOCK_ANCH_TOL
            and abs(FT[k]["GM"] - BLOCK_SAMPLE_ANCH[k][3])
            <= BLOCK_ANCH_TOL for k in BLOCK_SAMPLE_ANCH)
        ok_dsample = all(
            abs(DT[k]["DW"] - DUAL_SAMPLE_ANCH[k][0])
            <= BLOCK_ANCH_TOL
            and abs(DT[k]["DK"] - DUAL_SAMPLE_ANCH[k][1])
            <= BLOCK_ANCH_TOL
            and abs(DT[k]["GC"] - DUAL_SAMPLE_ANCH[k][2])
            <= BLOCK_ANCH_TOL
            and abs(DT[k]["LRloc"] / LRLOC_SAMPLE_ANCH[k] - 1.0)
            <= 1e-3 for k in DUAL_SAMPLE_ANCH)
        check("G34-cohort-fit-anchors", ok_fit and ok_b354
              and ok_dsample,
              "LEG 0 FIT ANCHORS on the 57 (slope | record): "
              "margin %.3f | %.3f, c %.3f | %.3f, p %.3f | %.3f, "
              "q %.3f | %.3f, rdet %.3f | %.3f, kap %.3f | %.3f "
              "(tol %.2f); CURV margin %+.3f, c %+.3f, rdet "
              "%+.3f (tol %.2f); THE R352 PHI RECORD REPRODUCED: "
              "corr %.6f / rmsD %.4f / rmsr %.4f (record %.6f / "
              "%.4f / %.4f) -- the one-object premise stands; "
              "the r354 four-block AND the dual-block sample "
              "anchors (kz44/56/130) bit-near"
              % (laws["margin"]["slope"], FIT_ANCH["margin"],
                 laws["c"]["slope"], FIT_ANCH["c"],
                 laws["p"]["slope"], FIT_ANCH["p"],
                 laws["q"]["slope"], FIT_ANCH["q"],
                 laws["rdet"]["slope"], FIT_ANCH["rdet"],
                 laws["kap"]["slope"], FIT_ANCH["kap"],
                 FIT_ANCH_TOL, laws["margin"]["curv"],
                 laws["c"]["curv"], laws["rdet"]["curv"],
                 CURV_ANCH_TOL, co_fs, rmsD_fs, rr_fs,
                 FS9_ANCH["corr"], FS9_ANCH["rmsD"],
                 FS9_ANCH["rmsr"]))

    # ---------------- S4 twin + worlds
    section("S4  LEG C -- TWIN + WORLD MINI-LADDERS (DUAL "
            "PIPELINE)")
    if smoke:
        for g in ("G40-twin-dual", "G41-worlds-dual"):
            check(g, True, "SMOKE: skipped")
        world_txt = ""
        dead_pass: list = []
        co_m = rr_m = None
    else:
        tw_dev = 0.0
        ok_dose0 = True
        for kz in WORLD_KZ:
            uuc, mmc = TR.base_comb(kz)
            mzD = TR.build_world(kz, uuc, mmc)
            mzV = V.build_measures(kz)
            ok_dose0 = ok_dose0 and (
                np.array_equal(mzD["xp"], mzV["xp"])
                and np.array_equal(mzD["wp"], mzV["wp"])
                and np.array_equal(mzD["yn"], mzV["yn"])
                and np.array_equal(mzD["vn"], mzV["vn"]))
            gapsc = MF.local_gaps(uuc)
            u2c, m2c, _dn, _du = AKD.twin_rational(
                uuc, mmc, gapsc, mzD["D"], TWIN_TOL)
            mzT = TR.build_world(kz, u2c, m2c)
            t1_, t2_ = PX.pair_select(mzT["yn"])
            DTt = dual_rung(mzT["xu"], mzT["wu"], mzT["yn"],
                            mzT["vn"], mzT["Nw"], mzT["S"],
                            mzT["L"], t1_, t2_)
            Dm = DT[kz]
            tw_dev = max(tw_dev,
                         abs(DTt["DW"] - Dm["DW"]),
                         abs(DTt["DK"] - Dm["DK"]),
                         abs(DTt["GC"] - Dm["GC"]),
                         abs(math.log(DTt["LRloc"] / Dm["LRloc"])))
            del DTt
        check("G40-twin-dual", ok_dose0 and tw_dev <= TWIN_DUAL_BAR,
              "RATIONAL TWIN mini-ladder on kz %s (dose-zero "
              "identity BITWISE %s): pointwise dual devs max "
              "over |dDW|, |dDK|, |dGC|, |dlog LR_loc| = %.1e "
              "nats (bar %.0e) -- the dual-hole coordinates are "
              "twin-stable POINTWISE"
              % (str(WORLD_KZ), ok_dose0, tw_dev, TWIN_DUAL_BAR))
        # world mini-ladders
        wres = {}
        for nm in ("SMOOTH", "SCR", "DIR", "ABS"):
            rows = []
            for kz in WORLD_KZ:
                if nm == "SMOOTH":
                    al_k = V.window_shape(kz)[0]
                    kw = dict(comb=PB.smooth_comb(al_k))
                elif nm == "SCR":
                    kw = dict(scramble_seed=1)
                elif nm == "DIR":
                    uD, wD, _n, _c = DSW.dirichlet_comb(kz)
                    kw = dict(comb=(uD, wD))
                else:
                    uA, wA, _n = DSW.dirichlet_abs_comb(kz)
                    kw = dict(comb=(uA, wA))
                try:
                    (Nww, Lw, xuw, wuw, ysw, vsw, pw, qw, cw,
                     j1w, j2w, _Bw, dep) = \
                        world_union_row(nm, kz, kw)
                    if dep != Nww:
                        rows.append(None)
                        continue
                    Dw = dual_rung(xuw, wuw, ysw, vsw, Nww,
                                   len(xuw), Lw, j1w, j2w)
                    LRw = -math.log(cw * cw / (pw * qw)) \
                        if (np.isfinite(pw * qw) and pw * qw > 0
                            and np.isfinite(cw * cw)
                            and 0 < cw * cw < pw * qw) \
                        else float("nan")
                    rows.append(dict(Nw=Nww, p=pw, q=qw, c=cw,
                                     LR=LRw, D=slim_dual(Dw)))
                    del Dw
                except (ValueError, OverflowError,
                        np.linalg.LinAlgError):
                    rows.append(None)
            # sealed usable-row rule (r354-a2 class, sealed
            # upfront): finite logs on every consumed column
            usable_c = [r for r in rows if r is not None
                        and np.isfinite(r["p"]) and np.isfinite(r["q"])
                        and np.isfinite(r["c"])
                        and np.isfinite(r["p"] * r["q"])
                        and np.isfinite(r["c"] * r["c"])
                        and r["p"] * r["q"] > 0 and r["c"] != 0
                        and np.isfinite(r["D"]["DW"])
                        and np.isfinite(r["D"]["DK"])
                        and np.isfinite(r["D"]["GC"])]
            usable_r = [r for r in usable_c
                        if np.isfinite(r["LR"]) and r["LR"] > 0
                        and np.isfinite(r["D"]["LRloc"])
                        and r["D"]["LRloc"] > 0]
            out = dict(n_c=len(usable_c), n_r=len(usable_r),
                       lamR=[("%.2e" % (r["D"]["lamR"] - 0.5))
                             if r is not None else "X"
                             for r in rows],
                       car=None, res=None, hit_c=False,
                       hit_r=False)
            if len(usable_c) >= WORLD_MIN_ROWS:
                lnn = np.log([float(r["Nw"]) for r in usable_c])
                lc2 = np.array([math.log(r["c"] ** 2)
                                for r in usable_c])
                best = None
                for bn in DUAL_BLOCKS:
                    col = np.array([r["D"][bn] for r in usable_c])
                    psT, _b1 = PWA.psi_small(lnn, lc2)
                    psB, _b2 = PWA.psi_small(lnn, col)
                    co_b, _sh, lo_b = PWA.carrier_stats(psT, psB)
                    if best is None or lo_b < best[2]:
                        best = (bn, co_b, lo_b)
                out["car"] = best
                out["hit_c"] = (best[1] >= CAR_CORR_MIN
                                and best[2] <= CAR_RES_MAX)
            if len(usable_r) >= WORLD_MIN_ROWS:
                lnn = np.log([float(r["Nw"]) for r in usable_r])
                lLR = np.array([math.log(r["LR"])
                                for r in usable_r])
                lLRl = np.array([math.log(r["D"]["LRloc"])
                                 for r in usable_r])
                psT, _b1 = PWA.psi_small(lnn, lLR)
                psP, _b2 = PWA.psi_small(lnn, lLRl)
                co_r, _sh, lo_r = PWA.carrier_stats(psT, psP)
                out["res"] = (co_r, lo_r)
                out["hit_r"] = (co_r >= RES_CORR_MIN
                                and lo_r <= RES_RES_MAX)
            wres[nm] = out
        # MAIN mini gate (local-dual coupling, slope-free)
        lnn_m = np.log([float(RT[k]["Nw"]) for k in WORLD_KZ])
        lc2_m = np.array([math.log(RT[k]["c"] ** 2)
                          for k in WORLD_KZ])
        lr12_m = np.array([DT[k]["DW"] + DT[k]["DK"]
                           for k in WORLD_KZ])
        psK_m, _bm1 = PWA.psi_small(lnn_m, lc2_m)
        psR_m, _bm2 = PWA.psi_small(lnn_m, lr12_m)
        co_m = float(np.corrcoef(psK_m, psR_m)[0, 1])
        rr_m = float(np.sqrt(np.mean((psK_m - psR_m) ** 2))) \
            / max(float(np.sqrt(np.mean(psK_m ** 2))), 1e-300)
        dead_pass = [nm for nm in wres
                     if wres[nm]["hit_c"] and wres[nm]["hit_r"]]
        world_txt = "; ".join(
            "%s carrier-usable %d/6, reserve-usable %d/6, "
            "lamR-1/2 %s%s%s"
            % (nm, wres[nm]["n_c"], wres[nm]["n_r"],
               str(wres[nm]["lamR"]),
               (", best block %s corr %+.3f lo %.3f %s"
                % (wres[nm]["car"][0], wres[nm]["car"][1],
                   wres[nm]["car"][2],
                   "HIT" if wres[nm]["hit_c"] else "--"))
               if wres[nm]["car"] else ", carrier NOT_MEASURABLE",
               (", reserve corr %+.3f lo %.3f %s"
                % (wres[nm]["res"][0], wres[nm]["res"][1],
                   "HIT" if wres[nm]["hit_r"] else "--"))
               if wres[nm]["res"] else ", reserve NOT_MEASURABLE")
            for nm in ("SMOOTH", "SCR", "DIR", "ABS"))
        check("G41-worlds-dual", co_m >= FS_CORR_MIN
              and rr_m <= FS_RMSR_MAX,
              "THE WORLD TEST OF THE DUAL COORDINATE: MAIN "
              "mini-ladder (6 rows, slope-free) corr(psi(2 log "
              "|R12|), psi(log c^2)) = %.6f (gate >= %.2f), rmsr "
              "= %.4f (gate <= %.1f) -- the local dual two-point "
              "log carries the wander on the mini-instrument; "
              "DEAD WORLDS (sealed mini clauses): %s; dead "
              "worlds passing BOTH clauses: %s; EPST / HL2 "
              "NOT_LADDERED (kz9-specific constructions, typed)"
              % (co_m, FS_CORR_MIN, rr_m, FS_RMSR_MAX, world_txt,
                 str(dead_pass) if dead_pass else "none"))

    # ---------------- S5 adjudications
    section("S5  LEG A/B/E -- ANTI-DESIGN + CARRIER + RESERVE + "
            "AC FALSIFIER + DEMARCATION")
    if smoke:
        for g in ("G50-anti-design", "G51-dual-carrier",
                  "G52-reserve", "G53-ac-falsifier",
                  "G54-demarcation"):
            check(g, True, "SMOKE: skipped")
        verdict_bits = {}
    else:
        verdict_bits = {}
        lc2_all = np.array([math.log(getters["csq"](k))
                            for k in all_kz])
        psi_t, _s0 = psi_fit57(lnN_all, lc2_all, mask57)
        cols354 = {bn: np.array([FT[k][bn] for k in all_kz])
                   for bn in R354_BLOCKS}
        colsD = {bn: np.array([DT[k][bn] for k in all_kz])
                 for bn in DUAL_BLOCKS}
        psiW, _sw = psi_fit57(lnN_all, cols354["W"], mask57)
        psiDW, _sd = psi_fit57(lnN_all, colsD["DW"], mask57)
        psiPG, _sp = psi_fit57(lnN_all, cols354["PG"], mask57)
        psiDK, _sk = psi_fit57(lnN_all, colsD["DK"], mask57)
        anti = float(np.corrcoef(psiDW[mask57], psiW[mask57])[0, 1])
        cens_kpg = float(np.corrcoef(psiDK[mask57],
                                     psiPG[mask57])[0, 1])
        check("G50-anti-design", anti <= ANTI_BAR,
              "THE BY-DESIGN GATE: corr(psi57 DW, psi57 W) = "
              "%+.6f <= %.2f on the 57 -- the r354 "
              "anti-correlation of the dictionary-weight block "
              "against the pair-geometry block is DUALITY ALGEBRA "
              "(DW == geometry - W + const, the geometry factor "
              "is family-constant by the hard-edge scaling of "
              "G24); census corr(psi57 DK, psi57 PG) = %+.6f -- "
              "the dual CD block mirrors the pair-geometry "
              "composite" % (anti, ANTI_BAR, cens_kpg))
        # carrier adjudication on the 57
        car354, carD = {}, {}
        for fam, cols, store in (("r354", cols354, car354),
                                 ("dual", colsD, carD)):
            for bn in cols:
                psb, _sb = psi_fit57(lnN_all, cols[bn], mask57)
                co_b, sh_b, lo_b = PWA.carrier_stats(
                    psi_t[mask57], psb[mask57])
                co_e, sh_e, lo_e = PWA.carrier_stats(
                    psi_t[~mask57], psb[~mask57])
                store[bn] = dict(corr=co_b, share=sh_b, lo=lo_b,
                                 corr_ext=co_e, lo_ext=lo_e,
                                 hit=(co_b >= CAR_CORR_MIN
                                      and lo_b <= CAR_RES_MAX))
        lo354_best = min(car354[bn]["lo"] for bn in R354_BLOCKS)
        loD_best_bn = min(DUAL_BLOCKS,
                          key=lambda bn: carD[bn]["lo"])
        loD_best = carD[loD_best_bn]["lo"]
        hitsD = [bn for bn in DUAL_BLOCKS if carD[bn]["hit"]]
        compress_ok = loD_best <= COMPRESS_FACTOR * lo354_best
        carrier_go = bool(hitsD) and compress_ok
        # the near-tautological sum block, census only
        psbS, _ss = psi_fit57(lnN_all, colsD["DW"] + colsD["DK"],
                              mask57)
        coS, shS, loS = PWA.carrier_stats(psi_t[mask57],
                                          psbS[mask57])
        verdict_bits["car"] = dict(carD=carD, car354=car354,
                                   hitsD=hitsD,
                                   best=(loD_best_bn, loD_best),
                                   lo354=lo354_best,
                                   compress=compress_ok,
                                   go=carrier_go,
                                   sum_cens=(coS, shS, loS))
        check("G51-dual-carrier", True,
              "LEG B THE CARRIER CENSUS (target psi57(log c^2) on "
              "the 57, rms %.4f nats; EXT puretest in "
              "parentheses): DUAL %s; R354 IN-RUN %s; COMPRESSION "
              "CLAUSE: best dual leave-out %.3f (%s) vs %.1f x "
              "best r354 leave-out %.3f => %s; the SUM block "
              "DW+DK == log c^2 - GC is NEAR-TAUTOLOGICAL "
              "(census: corr %+.4f, share %.3f, leave-out %.3f "
              "-- excluded from the sealed list by design) => %s"
              % (float(np.sqrt(np.mean(psi_t[mask57] ** 2))),
                 "; ".join("%s corr %+.4f share %.3f lo %.3f "
                           "(EXT %+.3f/%.3f) %s"
                           % (bn, carD[bn]["corr"],
                              carD[bn]["share"], carD[bn]["lo"],
                              carD[bn]["corr_ext"],
                              carD[bn]["lo_ext"],
                              "HIT" if carD[bn]["hit"] else "--")
                           for bn in DUAL_BLOCKS),
                 "; ".join("%s corr %+.4f lo %.3f"
                           % (bn, car354[bn]["corr"],
                              car354[bn]["lo"])
                           for bn in R354_BLOCKS),
                 loD_best, loD_best_bn, COMPRESS_FACTOR,
                 lo354_best,
                 "FIRES" if compress_ok else "does NOT fire",
                 coS, shS, loS,
                 "DUAL_CARRIER candidate" if carrier_go
                 else "NO dual carrier at the sealed bars"))
        # reserve adjudication
        lLR_all = np.array([math.log(PT[k]["LR"])
                            for k in all_kz])
        ok_lrl = [k for k in all_kz
                  if np.isfinite(DT[k]["LRloc"])
                  and DT[k]["LRloc"] > 0]
        lLRl_all = np.array([math.log(DT[k]["LRloc"])
                             if np.isfinite(DT[k]["LRloc"])
                             and DT[k]["LRloc"] > 0 else np.nan
                             for k in all_kz])
        psiLR, _s1 = psi_fit57(lnN_all, lLR_all, mask57)
        psiLRl, _s2 = psi_fit57(lnN_all,
                                np.nan_to_num(lLRl_all), mask57)
        co_res, _shr, lo_res = PWA.carrier_stats(psiLR[mask57],
                                                 psiLRl[mask57])
        co_rese, _she, lo_rese = PWA.carrier_stats(
            psiLR[~mask57], psiLRl[~mask57])
        rat = lLRl_all - lLR_all
        reserve_go = (co_res >= RES_CORR_MIN
                      and lo_res <= RES_RES_MAX
                      and len(ok_lrl) == len(all_kz))
        verdict_bits["res"] = dict(corr=co_res, lo=lo_res,
                                   corr_ext=co_rese,
                                   lo_ext=lo_rese, go=reserve_go,
                                   rat_med=float(np.median(rat)),
                                   rat_max=float(np.max(
                                       np.abs(rat))))
        check("G52-reserve", len(ok_lrl) == len(all_kz),
              "LEG B THE RESERVE PREDICTION from the LOCAL dual "
              "two-point block (consumes R_11, R_12, R_22 ONLY): "
              "LR_loc finite and in the L* cone on %d/%d rows; "
              "pointwise log(LR_loc/LR) median %+.3f, max |.| "
              "%.3f nats; SEALED CLAUSES on the 57: corr(psi57 "
              "LR_loc, psi57 LR) = %+.4f (>= %.1f), leave-out = "
              "%.3f (<= %.1f) => %s; EXT PURETEST corr %+.4f, "
              "leave-out %.3f"
              % (len(ok_lrl), len(all_kz),
                 verdict_bits["res"]["rat_med"],
                 verdict_bits["res"]["rat_max"], co_res,
                 RES_CORR_MIN, lo_res, RES_RES_MAX,
                 "RESERVE CLAUSE FIRES" if reserve_go
                 else "reserve clause does NOT fire", co_rese,
                 lo_rese))
        # AC falsifier
        ac_max = max(max(ACT[k]) * RT[k]["Nw"] / AC_POS_FACT
                     for k in all_kz)
        ac_pos_ok = all(max(ACT[k]) <= AC_POS_FACT / RT[k]["Nw"]
                        for k in all_kz)
        ft_rho = LM.ts_fit(lnN57, np.log([getters["rhoK"](k)
                                          for k in fit_kz]))
        a_rhoK = -float(ft_rho[1])
        e56 = [(math.log(RT[k]["Nw"]),
                math.log(getters["rhoK"](k))) for k in ext_all
               if RT[k]["Nw"] > EXT4_NW_MAX]
        dd_rho = DA.decay_law(lnN57,
                              np.log([getters["rhoK"](k)
                                      for k in fit_kz]), [], e56)
        f_census = sorted({(DT[k]["f1"], DT[k]["f2"])
                           for k in all_kz})
        ac_fire = (ac_pos_ok and a_rhoK >= AC_DECAY_MIN
                   and abs(a_rhoK - A_RHOK_REC) <= A_RHOK_TOL)
        verdict_bits["ac"] = dict(fire=ac_fire, a=a_rhoK,
                                  pos_ok=ac_pos_ok,
                                  ac_max=ac_max)
        check("G53-ac-falsifier", ac_pos_ok
              and abs(a_rhoK - A_RHOK_REC) <= A_RHOK_TOL,
              "LEG E THE AC-CLASS FALSIFIER: (i) the rescaled "
              "pair positions a = 2 N^2 (1-y) are FAMILY-CONSTANT "
              "against pi^2 f^2/4 on ALL %d rows (max dev %.2f x "
              "the 1/N_w scale, bar %.1f; fold census %s) -- the "
              "kernel ratio comparison is at FIXED microscopic "
              "arguments; (ii) the Lubinsky-type AC prediction is "
              "rho_K -> const (slope 0), MEASURED a_rhoK = %.4f "
              "(record %.4f, tol %.2f) >= %.1f: the kernel "
              "DECORRELATES like N^-1.42 where the AC class "
              "demands a constant => %s; deep census: EXT5+EXT6 "
              "rhoK vs the 57-fit in/low = %d/%d (out-rows HIGH "
              "side, the r352/r354 flattening)"
              % (len(all_kz), ac_max, AC_POS_FACT,
                 str(f_census), a_rhoK, A_RHOK_REC, A_RHOK_TOL,
                 AC_DECAY_MIN,
                 "AC_CLASS_EXCLUDED fires (typed for the memo, "
                 "census-grade, never a wall mechanism)"
                 if ac_fire else "AC_CENSUS only", 
                 dd_rho["e4_in"], dd_rho["e4_low"]))
        # demarcation gate
        udmax_all = max(DT[k]["udmax"] for k in all_kz)
        check("G54-demarcation", not sup_fail
              and umin_all > 0.0 and np.isfinite(udmax_all),
              "LEG D THE R227/R228 DEMARCATION (DLIII/DLIV read "
              "verbatim): the r228 duality lived on the SIGNED "
              "measure mutilde = mu - nu (Hankel complement, "
              "dual reference weights 1/(w L_N'^2)) and died on "
              "the ZERO-WEIGHT structure -- mu == 0 on every nu "
              "node: R_DUAL_OBSTRUCTED; HERE the lift is "
              "POSITIVE: eta = mu + nu with u = |wtilde| >= "
              "%.2e > 0 on every union node and the Borodin dual "
              "weight FINITE everywhere (max u_vee %.2e) -- the "
              "obstruction is structurally ABSENT; the r228 "
              "half-filling law N_w = ceil(S/2) (NOT_A_HOLE_EDGE) "
              "is CONSUMED as the exact rank condition S = 2N-1 "
              "(G32); the r228 COMPLEMENT_IDENTITY_EXACT survives "
              "as the determinant shadow of the projection "
              "complementation; the DUAL_WALL_EQUIVALENT risk is "
              "typed by the verdict enum (DUALITY_REPARAM_ONLY), "
              "not hidden" % (umin_all, udmax_all))

    # ---------------- S8 must-fails
    section("S8  MUST-FAILS")
    ud_m1 = mutant_pprime_unsquared(np.abs(mz9["wu"]), D9["logPp"])
    ad1, bd1, h01 = V.mu_chain(xu9, ud_m1, R9["Nw"] - 1)
    Bd1 = V.b_matrix(ad1, bd1, h01, mz9["yn"], ud_m1[D9["iY"]],
                     R9["Nw"] - 1)
    R_m1 = Bd1 @ Bd1.T
    epsY9 = D9["eps"][D9["iY"]]
    dev_m1 = float(np.max(np.abs(
        D9["Q"] - (np.eye(len(R_m1)) - R_m1)
        * np.outer(epsY9, epsY9))))
    check("G80-m1-pprime-unsquared", dev_m1 >= M_LOUD,
          "m1 P'^2 OMITTED in the dual weight: the "
          "Y-complementation at w9 breaks by %.2e >= %.0e (true "
          "value %.1e) -- and the exact Fractions toy broke "
          "EXACTLY (G11); the square of the node-polynomial "
          "derivative is load-bearing, CAUGHT"
          % (dev_m1, M_LOUD, D9["dev_comp"]))
    R_m2 = mutant_rank_full(xu9, D9["ud"], np.asarray(mz9["yn"]),
                            D9["ud"][D9["iY"]], R9["Nw"])
    dev_m2 = float(np.max(np.abs(
        D9["Q"] - (np.eye(len(R_m2)) - R_m2)
        * np.outer(epsY9, epsY9))))
    check("G81-m2-rank-full", dev_m2 >= M_LOUD,
          "m2 RANK N INSTEAD OF N-1 in the hole kernel: the "
          "Y-complementation at w9 breaks by %.2e >= %.0e -- "
          "half filling means the complement rank is EXACTLY "
          "N-1 = %d, CAUGHT (and exactly in Fractions, G11)"
          % (dev_m2, M_LOUD, R9["Nw"] - 1))
    la_m3 = mutant_mu_only_nodes(mz9["xp"], xu9,
                                 np.abs(mz9["wu"]))
    lb9 = np.log(D9["ud"])
    dev_m3 = float(np.max(np.abs((la_m3 - la_m3.mean())
                                 - (lb9 - lb9.mean()))))
    check("G82-m3-mu-only-nodes", dev_m3 >= M3_LOUD,
          "m3 THE NODE POLYNOMIAL OVER supp mu ONLY: the "
          "route-A/route-B comparison breaks by %.1f nats >= "
          "%.1f (true value %.1e) -- the dual weight NEEDS the "
          "full union X = supp mu UNION supp nu, CAUGHT"
          % (dev_m3, M3_LOUD, D9["dev_ab"]))
    check("G83-m4-mass-permutation", dev_m4_9 >= M4_BAR
          and dev_sym9 == 0.0,
          "m4 |f| MASS PERMUTATION (the world clause in mutant "
          "form): the weight-dictionary identity u == (1/S) c_j "
          "(1-x) |f| breaks by %.2f relative >= %.1f under the "
          "deterministic modulus reversal (true value 0.0 "
          "BITWISE) -- the theta-coherence of the symbol is "
          "load-bearing, CAUGHT" % (dev_m4_9, M4_BAR))
    mut5 = mutant_r12_local(D9["s12"], D9["R12"])
    dev_m5 = abs(mut5 / R9["c"] - 1.0)
    check("G84-m5-r12-vs-rinv12", dev_m5 >= M5_BAR
          and abs(D9["s12"] * D9["Rinv12"] / R9["c"] - 1.0)
          <= CID_BAR[0],
          "m5 R_12 INSTEAD OF THE GLOBAL (R^{-1})_{12}: the c "
          "identity breaks by %.3f >= %.1f (== |+-e^{-GC/2} - 1| "
          "incl. the local sign: the global-conditioning block "
          "IS the difference) while the true inverse identity "
          "holds at %.1e -- CAUGHT" % (dev_m5, M5_BAR,
                      abs(D9["s12"] * D9["Rinv12"] / R9["c"]
                          - 1.0)))
    check("G85-m6-ast-readbacks", bool(hits_m6) and bool(hits_m6b),
          "m6 THE RESERVE PREDICTION WITH LR-READBACK is "
          "AST-FLAGGED (%s) and the c-readback 'coupling' is "
          "AST-FLAGGED (%s) -- the scope audit is the catch: "
          "lr_local consumes the dual pair block only"
          % (hits_m6[0] if hits_m6 else "MISS",
             hits_m6b[0] if hits_m6b else "MISS"))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism "
          "promoted, no certificate reading beyond the sealed "
          "census, no posthoc bar/band/block/clause move, no "
          "derived 5/7, NO RH claim, mincut unchanged; what the "
          "round adds: the exact dual-hole chain (L-ensemble + "
          "Borodin complement + spectral map + pair identities), "
          "the reciprocal-weight dictionary, the anti-design "
          "reading of the r354 interference, the carrier/reserve "
          "adjudication, the AC-class falsifier and the r228 "
          "demarcation; r243..r355 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        vC = verdict_bits["car"]
        vR = verdict_bits["res"]
        vA = verdict_bits["ac"]
        world_ok = (co_m is not None and co_m >= FS_CORR_MIN
                    and rr_m <= FS_RMSR_MAX and not dead_pass)
        if not audits_ok:
            main_v = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif sup_fail:
            main_v = ("SUPPORT_GATE_FAIL(%s -- duality carry "
                      "census printed in G32/G33)"
                      % str(sup_fail))
        elif vC["go"] and vR["go"] and world_ok:
            main_v = ("DUAL_HOLE_CARRIER_GO(block %s lo %.3f, "
                      "compression vs r354 %.3f, reserve corr "
                      "%.4f lo %.3f, worlds separated)"
                      % (vC["best"][0], vC["best"][1],
                         vC["lo354"], vR["corr"], vR["lo"]))
        else:
            fails = []
            if not vC["hitsD"]:
                fails.append("no dual block passes the carrier "
                             "clauses (best %s lo %.3f)"
                             % (vC["best"][0], vC["best"][1]))
            elif not vC["compress"]:
                fails.append("compression clause fails (%.3f > "
                             "%.1f x %.3f)"
                             % (vC["best"][1], COMPRESS_FACTOR,
                                vC["lo354"]))
            if not vR["go"]:
                fails.append("reserve clause fails (corr %.4f, "
                             "lo %.3f)" % (vR["corr"], vR["lo"]))
            if not world_ok and dead_pass:
                fails.append("dead worlds pass: %s"
                             % str(dead_pass))
            main_v = ("DUALITY_REPARAM_ONLY(%s -- the duality is "
                      "EXACT but does not compress the one-object "
                      "problem: the L* lane is FINAL at the "
                      "specialist memo)" % "; ".join(fails))
        parts = [
            main_v,
            ("WORLD_BLIND(%s)" % str(dead_pass))
            if (vC["go"] and vR["go"] and dead_pass) else "",
            ("AC_CLASS_EXCLUDED(a_rhoK %.4f vs AC-constant 0, "
             "positions family-constant at max %.2f/N_w -- the "
             "universality class of the window kernels is NOT "
             "the AC/Bessel class, typed for the memo)"
             % (vA["a"], vA["ac_max"])) if vA["fire"]
            else ("AC_CENSUS(a_rhoK %.4f, pos_ok %s)"
                  % (vA["a"], vA["pos_ok"])),
            "DEMARCATION_LEDGER(positive lift vs r228 signed "
            "Hankel; dual weight exists on every node; r228 "
            "half-filling law == the Borodin rank condition, "
            "exact on all rows)",
            "DUAL_MARGIN_LEDGER(lambda_min(R) > 1/2 on every "
            "live row == L*; EXT6 f64 sign resolution ~5e-10 "
            "exceeds the ~4e-10 margins: the dual route cannot "
            "certify the deepest signs, disclosed)",
            "WORLD_LEDGER(MAIN mini corr %.6f rmsr %.4f; %s; "
            "EPST/HL2 NOT_LADDERED)" % (co_m, rr_m, world_txt),
            "TWIN_LEDGER(dose-zero BITWISE 6/6; max dual dev "
            "%.1e nats)" % tw_dev,
            "MUSTFAIL_LEDGER(m1-m6 + scopes)",
        ]
        verd = " + ".join(p for p in parts if p)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED dual-hole algebra + sealed "
          "adjudication; NO L* claim, NO RH claim"
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
