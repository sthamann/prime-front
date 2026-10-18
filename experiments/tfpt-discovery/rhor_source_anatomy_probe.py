#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rhor_source_anatomy_probe -- PRIME.LSTAR.RHOR_SOURCE_ANATOMY.01
(round 352): THE RHO_R SOURCE ANATOMY -- the last census member of
the closed L* exponent chain, plus the g_K12 second-instrument
lane.  The named successor round of r350 (ALPHA_SOURCE_CLOSED at
candidate-law grade): after r350 the exponent chain alpha == a_p +
a_q + rho_r - a_(p+q) closes source-side with ONE census member,
rho_r = 2.624 -- the cancellation exponent of the BARE reserve
r_det = 1 - c^2/(pq) (r342), halves-curved -0.767, no clean power
law.  Via BK3 (a_c == (a_p + a_q)/2 at 0.002) c^2 and pq share the
LEADING exponent, so rho_r measures how fast the ratio c^2/pq
saturates to 1 -- the r338-q1 backward-Cauchy-Schwarz question in
its sharpest form: rho_r is the CORRELATION structure between the
diagonal and cross kernel values at the pair.  THE ROUND'S
QUESTION: can rho_r be reduced to the candidate laws + the g_K12
fine structure -- are the two named rests (g_K12, the one dirty
census column of r350, and rho_r, the last census member) ONE
object -- and does a second instrument carry the g_K12 law on the
deep cohorts?

THE CHAIN (r342..r350, all sealed records): r342 the two-atom law
(bare decay laws p -0.754 / q -0.645 / c -0.697; digamma/tent
weight dictionary at v_pred 9.0e-4; rho_r = 2.624 named as the
open analytic remainder, halves-curved -0.767); r343 the exact
resolvent dressing + the EXT4 selection rule (domain cap z^2 <=
400000); r345 the cancellation law + the curvature-honest flatness
protocol; r347 the one-line closure; r348 the RATE_EQUALITY
theorem + the twin slow laws y0/rho_hi; r350 the alpha source
anatomy (weights WOERTERBUCH |s_v - s_vpred| = 0.0000; deficits
CANDIDATE-LAW a_p -> [3/4, 2 x 0.38], a_q -> [2/3, 1 - 0.38],
unresolvable on 57 windows; pinning SATZ-grade Fractions-exact;
kernel profile g_K11 +1.786 / g_K22 +1.683 == reciprocal weight
laws (BK2), g_K12 +0.902 THE one dirty census column (curv +0.500,
EXT3 5/12; REL2 (g_K11 + g_K22)/4 hits at 0.035, census), a_kappa
0.711 CLEAN (hits [2/3, 3/4]); BK3 0.002; CD-recursion ward
1.2e-10 on the sealed sample; rho_r = 2.624 the single census
member).  THE ROUND'S CONTRACT: (Leg A) THE RHO_R DECOMPOSITION:
from the exact pair identities d_k = v_k K_kk, c = sqrt(v1 v2) K12
the KERNEL CORRELATION at the pair is
    rho_K = K12^2/(K11 K22) = c^2/(d1 d2)
(the weights cancel EXACTLY -- rho_K is a weight-free kernel
object), and the bare reserve obeys the EXACT identities
    (i)   c^2 == rho_K d1 d2,
    (ii)  r_det == 1 - rho_K d1 d2 / (p q),
    (iii) r_det == (1 - rho_K) + rho_K (p + q - 1)/(p q)
(exact rearrangements; verified bit-near per rung and in exact
Fractions on the r342 hand toy: d1 = 1/4, d2 = 1/2, c = 1/8 gives
rho_K = 1/8 and r_det = 23/24 on all three routes).  The sealed
adjudications: (A-decor) IS 1 - rho_K THE CARRIER? -- the round's
naming hypothesis, adjudicated symmetrically (DECOR_CARRIER iff
the fitted decay exponent of 1 - rho_K is >= 0.3 AND within 0.5
of rho_r; the s1 scoping shows 1 - rho_K = 0.9989 -> 0.99994:
the kernel DEcorrelates (rho_K -> 0), it does not saturate --
the expected reading is a CLEAN REFUTATION, the r348
CARRIES_DELTA motif); (A-lead) THE LEADING CANCELLATION: the
product columns c^2 and pq are fitted DIRECTLY (compose-then-fit,
the r350-a2 instrument class) and |s_csq - s_pq| <= 0.05 -- the
leading exponents cancel EXACTLY-NEAR (the BK3 image), hence
rho_r is NOT composable from the leading candidate laws: it is a
SECOND-ORDER object; (A-fine) THE ONE-OBJECT TEST: the
fine-structure columns phi_D = log(pq) + A_LEAD ln N and phi_K =
log(c^2) + A_LEAD ln N (A_LEAD = 3/4 + 2/3 = 17/12, the sealed
first-hit candidates -- the SAME leading law subtracted from
both, so phi_D - phi_K == -log s == LR EXACTLY with s = c^2/(pq)
the saturation), both demeaned: sealed clauses corr(phi_D, phi_K)
>= FS_CORR_MIN 0.99 AND rms(phi_D - phi_K)/max(rms phi) <=
FS_RMSR_MAX 0.2 -- if they fire, the deficit fine structure and
the kernel fine structure are ONE SHARED WANDER and rho_r is
exactly the decay of their difference: the two named rests are
ONE object; (A-LR) the log-reserve column LR = -log s == log(pq)
- log(rho_K d1 d2) gets the sealed decay instrument
(|s_LR - s_rdet| <= 0.05 -- the weight-free normalization carries
the SAME law; its curvature printed: if it stays curved, the
honest reading is that no clean power law appears even in the
kernel normalization).  (Leg B) THE G_K12 SECOND INSTRUMENT:
(B-i) the CD-recursion route (r350 cd_kernel_route verbatim) is
run on ALL cohorts incl. EXT4 + EXT5 (not only the 6-rung r350
sample): graded wards (1e-6 on the re-gated r350 sample, 1e-5 for
N_w <= 3200, 1e-3 on EXT5 -- sized from the observed depth trend
1.7e-13 .. 1.2e-10, one-plus decades headroom), and the K12 law
is REFIT from the CD columns: |s_K12cd - s_K12| <= 1e-6 => the
r350 dirtiness (curv +0.500, EXT3 5/12) is a STRUCTURE effect,
not a measurement/route effect; (B-ii) the REL2-equivalent flat
column CONSTRUCTED EXPLICITLY: Q = K12/(K11 K22)^(1/4) -- its
log-flatness is EXACTLY equivalent to REL2 (slope(Q) = g_K12 -
(g_K11 + g_K22)/4); adjudicated under the r345 curvature-honest
protocol verbatim (GR.curvflat_protocol) over all arbitrated rows
incl. EXT5 (the s1 scoping shows Q spans 6.6 .. 45.6 over the
four sample rungs -- ~0.84 decades: the honest expectation is
that REL2 FAILS the flatness protocol, the r350 dirty-clause
reading restated in the flat frame); (B-iii) THE EXPLANATION
LANE: pointwise EXACTLY K12 = c / sqrt(v1 v2), so with the r342
dictionary weights (vpred) the dirty column factorizes as K12 ==
[the c law, curv +0.308 CLEAN] / sqrt[dictionary weights,
closed-form curved]: sealed clauses GK12_EXPLAINED iff (e1) the
pointwise dictionary reconstruction max_k |K12 sqrt(vp1 vp2)/c -
1| <= RECON_BAR 1e-2 (r350 BK1/a1 verbatim; scoped 5.5e-4), (e2)
the c column decay clauses are CLEAN (|curv| <= 0.35, EXT3 >=
10/12, EXT4 n_low <= 1), (e3) the kappa column re-gates CLEAN
(r350 verbatim) -- then g_K12's dirtiness is INHERITED from the
closed-form dictionary weight curvature (the curvature
bookkeeping curv(K12) vs curv(c) - (curv(vp1) + curv(vp2))/2
printed as census, Theil-Sen non-additivity disclosed), and
together with rho_K = kappa^2 the one dirty column is EXPLAINED
as the quotient/composition of clean laws -- said with numbers,
never upgraded beyond the sealed clauses.  (Leg C) THE CANDIDATE
RESOLUTION on the deep cohorts: the EXT5 TRANCHE -- the r343
selection rule verbatim (E3.admissible_pool + domain cap z^2 <=
400000, used ledger extended by EXT3 + EXT4) with the h window
RAISED to (3400, 6000]: the s2 scoping census finds 9 fresh
windows, the 6 deepest by (h, kz) descending are kz (69, 107,
101, 99, 115, 89) with h (5690, 5668, 5242, 5073, 4243, 4237)
and N_w == h (window shapes are public source geometry; the
WINDOWS themselves are never measured before the record run:
genuinely blind pure-test rows, N_w up to 5690 = 1.8x the EXT4
record depth); EXT5 rows get the REDUCED bundle (bare pair +
kernel columns + CD ward + dictionary weights; the resolvent/
pinning extension is NOT computed on EXT5 -- budget honesty,
said so); sealed separation instrument per ambiguity pair
(SEP_P (3/4, 0.76), SEP_Q (2/3, 1 - 0.38 = 0.62), SEP_D0 (0.38,
2/5)): candidate lines through the 57-fit pivot, deep-cohort
residuals (EXT3 + EXT4 + EXT5 for p/q; EXT3 + EXT4 for y0),
CANDIDATES_RESOLVED(x) iff >= 5/6 of the deep rows are closer to
one candidate AND the line gap at the deep median >= 2 x the
deep residual MAD; else UNRESOLVED with the REQUIRED depth
printed (ln N* = ln N_piv + 2 w_res ln 10 / |dA - dB|) -- honest:
if the ladder is too short, the needed depth is the deliverable.
(Leg D) THE TOTAL BALANCE: the r342/r350 composition re-gated
(|alpha_comp - alpha_meas| <= 0.1) and the fully decomposed chain
printed with every member typed (dictionary / candidate-law /
theorem-grade pinning / the one second-order object); the
irreducible-rest adjudication: if the one-object clauses fire,
the rest of the lane is EXACTLY the r338-q1 specialist question
(one object, all exponents measured, all identities exact --
the specialist package FINAL); else RHOR_IRREDUCIBLE with the
full profile.  (Leg E) worlds + twin: rho_K / 1 - rho_K / s /
r_det evaluated on the 8 instrumented worlds (the r350 world
channel verbatim; on dead worlds the pair block crosses 1 --
what the DECORRELATION does there is census, printed), the
lambda_rest separation + kappa_int records re-gated, the
rational twin ward on the new columns; must-fails >= 5.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO L* CLAIM, NO RH CLAIM in
either direction, mincut unchanged.  Coexistence: R351 (growth
law, terminal lane) may run in parallel -- this probe touches
NOTHING outside its own file and the strictly additive rh-sync.
Two-commit freeze protocol (r329 convention): spec + machinery
committed BEFORE the record run, record tables inserted after.

THE EXACT OBJECTS (all gated): per rung the r342 bundle
(PX.build_rung verbatim, SPEC_SHA prefix gated b09f8ccd), the
r343 extension (PC3.extend_rung, 9ffc2705), the r347 closure
(DA.closure_cols, bd1aa7f3), the r348 extras (DSA.rung_extras,
307814e9), the r350 kernel columns (ASA.rung_kernel_extras +
ASA.kernel_cols + ASA.cd_kernel_route, c3998c87), the r329 pool
machinery (E3.admissible_pool + used_kz_set, bbfaf199); THE NEW
COLUMNS (this round's spine): rho_K = c^2/(d1 d2) (== kappa^2
pointwise -- the Theil-Sen fit is EXACTLY homogeneous, so s_rhoK
== 2 s_kappa at 1e-9: an exact instrument gate), the saturation
s = c^2/(pq) = 1 - r_det, the log reserve LR = -log s, the
decorrelation 1 - rho_K, the REL2 column Q = K12/(K11 K22)^(1/4),
the dictionary-normalized cross kernel K12 sqrt(vp1 vp2) == c
(recon <= 1e-2), the CD-route kernel columns on every row, the
fine-structure pair (phi_D, phi_K); THE SEPARATION INSTRUMENT
(module-own, sealed): candidate lines through the 57-fit pivot,
closer-counts, gap-vs-MAD, required-depth formula.

INDEX FIREWALL (binding, r238-r350 discipline): w = window (kz
into the prime-power list), S = #union atoms, S_- = #nu atoms,
N_w = (S+1)//2; ground truth (r283..r350 records, control flips,
kappa_int records) enters GATES and record tables only; the
module-own constructors consume kernel Gram / spectrum / weight /
position / chain-coefficient arrays and measured columns ONLY
(AST scope audit; withheld identifiers are the RECORD values
ALPHA_REC and RHOR_REC and the verdict-side columns
slope_col_true, resid_spread_true, gram_k12_true); no zero/prime
oracles anywhere (AST firewall; the prime-power grid is the
sealed source comb, r238 convention); no fit primitives (fragment
audit; fits are the imported r286 Theil-Sen; the flat protocol is
the imported r345 curvflat_protocol; the decay instrument is the
imported r347 decay_law).  MACHINERY IMPORTED VERBATIM: r342
PX.{build_rung, pair_select, pair_block, pair_eigs, det_reserve,
schur_dress, v_predict} (b09f8ccd), r343 PC3.extend_rung
(9ffc2705), r345 GR.curvflat_protocol (1f99235a), r347
DA.{closure_cols, decay_law, mirror_world_row} (bd1aa7f3), r348
DSA.rung_extras (307814e9), r350 ASA.{kernel_cols,
cd_kernel_route, rung_kernel_extras, cd_ward_dev} (c3998c87),
r329 E3.{admissible_pool, used_kz_set} (bbfaf199), r330
DSW.{dirichlet_comb, dirichlet_abs_comb} (66526018), document
pipeline V.{build_measures, mu_chain, b_matrix,
admissible_indices, lam_max_at, window_shape, U, W_VM, PP}, r286
LM.{ts_fit, ts_slope_free, ext_rule}, r334 FC.{world_from_arrays,
world_from_mz, interval_census}, r278 MS.ctx_build, r280
BL.{union_of_ctx, sign_chain_f64}, v881 PIK.lambda_eps, r243
PB.smooth_comb, paircorr PC.{Grid, gen_model}, r331 TR.{base_comb,
build_world}, r289 AKD.twin_rational, r276 MF.local_gaps, v563
core READ-ONLY.

LEG 0 -- ANCHORS BIT-NEAR (r342..r350 record numbers as gates):
w9 records (S 367, N_w 184, lambda 0.99983248, margin 1.6752e-4);
the r347/r348 w9 closure row (p' 8.4606e-4, q' 1.2903e-3, m2'
1.6800e-4, bridge 1.0029, c'/c 2.7047e-2, g21 7.517, K_res 2,
rho0 0.5787, y0 0.42134, rho_hi 0.39430, lam_rest 0.996338); the
r350 w9 kernel row (v1 4.023172e-6, v2 4.360131e-6, K11
2.411068e5, K22 2.213016e5, K12 7.700682e3, kappa 3.333744e-2,
vp1 4.023992e-6, vp2 4.364056e-6); the sealed fit slopes (margin
-3.332, c -0.697, p -0.754, q -0.645, rdet -2.624, kappa -0.711,
K11 +1.786, K22 +1.683, K12 +0.902, y0 -0.401, rhi -0.393) and
curvatures (margin -0.347, c +0.308, rdet -0.767, K12 +0.500) as
DISCLOSED PRIORS; the r343 sealed EXT3/EXT4 selections adopted
AS-IS; the r334/r345 kappa_int records and control flips; the
r285/r342 kernel exponent P_BIND = 0.38 (candidate side).

LEG E -- MUST-FAILS (>= 5, each loud): (m1) THE WRONG
CORRELATION NORMALIZATION: rho_K computed against the DEFICITS
(c^2/(pq)) instead of the diagonals (c^2/(d1 d2)) -- breaks the
exact identity (ii) by >= 0.1 rel at w9 (scoped: factor ~878 off)
and by 2/69 EXACTLY on the Fractions toy; exactly CAUGHT.  (m2)
CANDIDATES / FITS AFTER SIGHT: a mutant consuming the withheld
measured slope column and returning the nearest twelfth --
AST-FLAGGED, and the toy value is in NO sealed list.  (m3) THE
SEPARATION BAR AFTER SIGHT: a mutant re-picking the gap bar from
the withheld deep residual spread -- AST-FLAGGED, and the toy
value differs from the sealed SEP_GAP_FACTOR.  (m4) THE SECOND
INSTRUMENT READ BACK FROM THE FIRST: a mutant 'CD route'
returning the withheld Gram value -- AST-FLAGGED; plus the loud
half: the CD endpoint formula WITHOUT the b_{N-1} prefactor
breaks the kernel ward by >= 0.1 rel at w9 (r350 m1 verbatim);
exactly CAUGHT.  (m5) THE REL2 COLUMN WITH THE WRONG POWER:
K12/(K11 K22)^(1/2) instead of ^(1/4) -- on the planted flat toy
the wrong power breaks the flatness by |(g1 + g2)/4| = 0.85 >=
0.5; exactly CAUGHT.  STOP LIST (anti-gates, binding): NO L*
claim, NO bound mechanism promoted, NO certificate reading of any
census, NO posthoc bar / band / family / prior / candidate move,
NO derived 5/7, NO RH claim, mincut unchanged; r243..r351 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_- 104, N_w 184);
REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN 1.6752e-4
rel 0.01; PX_SHA b09f8ccd; PC3_SHA 9ffc2705; GR_SHA 1f99235a;
DA_SHA bd1aa7f3; DSA_SHA 307814e9; ASA_SHA c3998c87; E3_SHA
bbfaf199; DSW_SHA 66526018; W9 ANCHORS (r347/r348/r350 verbatim)
d1p 0.999154 rel 1e-5 / d2p 0.998710 rel 1e-5 / ppr 8.4606e-4 rel
1e-3 / qpr 1.2903e-3 rel 1e-3 / m2p 1.6800e-4 rel 1e-3 / bridge
1.0029 abs 5e-3 / cpc 2.7047e-2 rel 1e-3 / g21 7.517 abs 0.01 /
kres 2 / lam_rest 0.996338 abs 1e-5 / rho0 0.5787 abs 5e-3 / y0
0.42134 abs 5e-3 / rho_hi 0.39430 abs 5e-3; K9 ANCHORS v1
4.023172e-6 rel 1e-3 / v2 4.360131e-6 rel 1e-3 / K11 2.411068e5
rel 1e-3 / K22 2.213016e5 rel 1e-3 / K12 7.700682e3 rel 1e-3 /
kap 3.333744e-2 rel 1e-3 / vp1 4.023992e-6 rel 1e-3 / vp2
4.364056e-6 rel 1e-3; RHO9 ANCHORS (this round's s1 scoping)
rhoK 1.111385e-3 rel 1e-3 / LR 1.1629e-2 rel 1e-3 / Q 16.0225 rel
1e-3 / cdict-ratio 1.000552 abs 1e-3 / rdet 1.1561e-2 rel 1e-3;
SAMPLE ANCHORS kap (kz44 1.746679e-2, kz56 1.547570e-2, kz130
8.014410e-3) rel 1e-3, rhoK (3.050887e-4, 2.394972e-4,
6.423076e-5) rel 1e-3, LR (1.0667e-4, 7.7500e-6, 2.0166e-6) rel
1e-3, Q (6.5991, 45.6367, 16.8488) rel 1e-3; MED ANCHORS rho0
0.839 abs 0.01 / bridge 1.0058 abs 5e-3; FIT ANCH (margin -3.332,
c -0.697, p -0.754, q -0.645, rdet -2.624, kap -0.711, K11
+1.786, K22 +1.683, K12 +0.902, y0 -0.401, rhi -0.393) tol 0.02;
CURV ANCH (margin -0.347, c +0.308, rdet -0.767, K12 +0.500) tol
0.03; ALPHA_REC 3.332 + RHOR_REC 2.624 (WITHHELD record constants
-- gates and m2 only); P_BIND 0.38; EXT3_KZ_B (42, 51, 54, 56,
58, 62); EXT3_KZ_A (96, 123, 125, 127, 128, 130); EXT3_NW (1721,
2577); EXT4_KZ_B (72, 75, 66); EXT4_KZ_A (113, 111, 108); EXT4_NW
(2656, 3181); EXT5 SELECTION (r343 rule verbatim, raised h cap):
EXT5_H_LO 3401, EXT5_H_HI 6000, K_EXT5 6, Z2_CAP 400000,
USED_EXPECT 98, FRESH5_EXPECT 9, EXT5_KZ_EXPECT (69, 107, 101,
99, 115, 89), EXT5_H_EXPECT (5690, 5668, 5242, 5073, 4243, 4237);
CSQ_ID_BAR 1e-12 (rel, identity (i)); RID_ABS 1e-9 (abs, identity
(ii)); ADD_SPLIT_BAR 1e-9 (backward, identity (iii)); HOM_BAR
1e-9; LEAD_CANCEL_BAR 0.05; A_LEAD 17/12; FS_CORR_MIN 0.99;
FS_RMSR_MAX 0.2; LR_MATCH_BAR 0.05; DECOR_MIN 0.3; DECOR_MATCH
0.5; CD_BAR 1e-6 (r350 sample re-gate); CD_BAR_MID 1e-5 (all rows
N_w <= 3200); CD_BAR_DEEP 1e-3 (EXT5); CD2_FIT_BAR 1e-6;
RECON_BAR 1e-2; DEC_CURV_BAR 0.35; DEC_EXT3_MIN 10; DEC_EXT4_LOW
1; CAND_BAR 0.05; RHOK_BAR 0.1 (the kappa bar DOUBLED for the
squared column, disclosed); CAND_KAP (1/2, 2/3, 3/4, 1.0) r350
verbatim; CAND_RHOK (1.0, 4/3, 3/2, 2.0); SEP_P (3/4, 0.76);
SEP_Q (2/3, 0.62); SEP_D0 (0.38, 2/5); SEP_FRAC 5/6;
SEP_GAP_FACTOR 2.0; COMP_BAR 0.1; REL2 column power 1/4 sealed;
SPLIT_BAR 1e-9; CPC_ID_BAR 1e-6; ID_BAR 1e-8; RDEF_BAR 1e-12;
DET_ID_BAR 1e-12; KINT RECORDS {EPST 1793.99, SCR 8.51e6, SMOOTH
2.193, HL2 1964} rel 0.05, live 0.999567 rel 1e-3; CTRL_FLIPS
{EPST 25, SCR 21, SMOOTH 27}, HL2 seed 101 flip 25; EXT 8;
TWIN_TOL 1e-8; TWIN_BAR 1e-3; M1_BAR 0.1; M4_BAR 0.1; M5_MIN 0.5;
MUT_MIN 1e-6; TOY_TOL 1e-12; EXT5 CONTINGENCIES (sealed): any f64
margin <= 0 on an EXT5 row -> excluded from margin/rdet/LR bands
and separation, reported; any nonfinite CD value -> excluded +
reported; if the EXT5 block exceeds 600 s in the calibration
pass, the record freezes the deepest 3 only (disclosed); runtime
<= 1800 s; smoke = toys + firewall + scopes + mutants + w9 block
(records, kernel + rho columns live, identities, CD route);
ladder, EXT5, twin, fits, adjudications, worlds skipped.

PRE-SPEC SCOPING (disclosed, r343-s1..r350-s1 precedent -- no
bar, band, threshold, family, candidate list or adjudication rule
was tuned after any evaluation except as sized here and said so):
(s1) FOUR sample rungs (kz9, kz44, kz56, kz130 -- all four
already printed in the r342..r350 records) were probed end-to-end
for machinery and bar sizing: the identities (i)/(ii)/(iii) hold
at 2.1e-16 / 5.5e-11-rel-to-tiny-rdet (abs <= 1.1e-16) / 4.4e-16
(sizing CSQ_ID_BAR 1e-12, RID_ABS 1e-9, ADD_SPLIT_BAR 1e-9);
rho_K = 1.111385e-3 / 3.050887e-4 / 2.394972e-4 / 6.423076e-5 and
1 - rho_K = 0.998889 -> 0.999936 (the DECORRELATION SATURATES TO
1: the sizing observation behind the DECOR clause -- the expected
reading is a clean refutation of the naive carrier hypothesis);
LR/r_det = 1.0058 / 1.0001 / 1.0000 / 1.0000 (the log reserve is
the reserve); Q = 16.0225 / 6.5991 / 45.6367 / 16.8488 (~0.84
decades spread over four rungs -- the flatness expectation for
REL2 is honest-negative); the dictionary reconstruction
K12 sqrt(vp1 vp2)/c = 1.000552 / 1.000003 / 1.000000 / 1.000000;
CD-route devs 1.6e-13 / 5.2e-13 / 1.8e-11 / 1.2e-10 (sizing the
graded CD bars); runtime 2.4 s for the four rungs.  (s2) the
EXT5 pool census (selection machinery only, NO window measured):
the r343 rule at h caps 3400/4200/6000 gives 17/20/26 fresh
domain-capped windows; used ledger 92 + 6 EXT4 = 98; fresh in
(3400, 6000] = 9; the 6 deepest are kz (69, 107, 101, 99, 115,
89) with h (5690, 5668, 5242, 5073, 4243, 4237); their window
SHAPES (public source geometry, V.window_shape) give N_w == h,
z (256, 461, 431, 419, 509, 359), all z^2 <= 400000; budget
sized from the N_w^2-ish rung cost (kz130 1.5 s at N_w 2577 ->
~25-40 s at N_w 5690 with the reduced bundle).  (s3) the
Fractions toy was solved by hand: d1 = 1/4, d2 = 1/2, c = 1/8
=> rho_K = 1/8, r_det = 23/24 on routes (ii) and (iii), and the
m1 mutant value 71/72 differs by 2/69 rel -- the toy gates are
exact-value gates.  No ladder-wide fit, median, protocol clause,
candidate adjudication, separation or law was evaluated before
this spec froze; the slopes cited above are published record
numbers or the disclosed scoping values, never sealed-fit
previews.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
precedence TARGET_LEAK > RHOR_REDUCED > RHOR_IRREDUCIBLE -- the
enum is exhaustive):
  [exactly one of]
  TARGET_LEAK(loci)  iff any firewall/scope/fragment audit fails /
  RHOR_REDUCED(one-object grade)  iff the identities (i)-(iii)
    gate AND the leading cancellation |s_csq - s_pq| <= 0.05 AND
    the one-object clauses fire (corr >= 0.99, rmsr <= 0.2) AND
    |s_LR - s_rdet| <= 0.05 -- rho_r is EXACTLY the decay of the
    difference of the two fine-structure columns, which are ONE
    shared wander: the deficit rest and the kernel rest are ONE
    object, and the composition alpha == cand_p + cand_q + rho_r
    - a_(p+q) carries this single object as its only census
    member; honesty: this is a REDUCTION AND IDENTIFICATION, not
    a source derivation of 2.624 -- the exponent itself stays
    measured /
  RHOR_IRREDUCIBLE(steckbrief)  otherwise -- the reserve resists
    the decomposition; the final specialist profile printed
  + [exactly one of] RHOK_LAW_FOUND(a_kap hits, a_rhoK = 2 a_kap,
    ambiguity printed) / RHOK_CENSUS(loci)  [always -- fires iff
    the kappa clauses re-gate CLEAN AND a sealed candidate hits
    (CAND_KAP at 0.05; the squared column inherits the law with
    doubled exponent and doubled curvature, disclosed)]
  + [exactly one of] DECOR_REFUTED(slope printed) /
    DECOR_CARRIER(law)  [always -- the round's naming hypothesis
    adjudicated symmetrically]
  + [exactly one of] GK12_EXPLAINED(e1 + e2 + e3) /
    GK12_CENSUS(failed clauses)  [always -- with the REL2
    protocol result and the second-instrument (CD) verdict
    printed inside either branch]
  + [exactly one of] CANDIDATES_RESOLVED(loci) /
    CANDIDATES_UNRESOLVED(required depths printed)  [always]
  + EXT5_LEDGER(selection gate, N_w, margins, band counts,
    contingencies) [always]
  + BALANCE_LEDGER(the r342/r350 composition re-gate + the
    candidate image + the full chain typing) [always]
  + WORLD_LEDGER(rho_K / decorrelation world columns, lambda_rest
    separation, kappa_int anchors) [always]
  + TWIN_LEDGER(new-column deviations) [always]
  + MUSTFAIL_LEDGER(m1-m5 + scopes) [always].
Honesty before beauty: the identities (i)-(iii) are exact
finite-matrix facts (theorem-grade SKELETON) whose inputs are
measured window scalars (census-grade FLESH); the one-object
clauses are a sealed census on finite windows, never an
asymptotic theorem; a candidate hit at the sealed bars is a
CANDIDATE, never an identification -- the sealed lists contain
neighbours closer than the bars and every ambiguity is printed;
the EXT5 tranche extends the ladder by a factor 1.8 in depth and
STILL cannot separate 3/4 from 2 x 0.38 (the required depths are
printed, that IS the deliverable); rho_r remains a measured
exponent under every verdict -- RHOR_REDUCED reduces and
identifies, it does not derive; the world clause is a measured
discriminator on eight instrumented worlds; no verdict claims
L*, a bound mechanism, a derived 5/7, or RH progress in any
direction.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze edit besides the ONE disclosed print-only amendment,
which IS the protocol; TWO-COMMIT PROTOCOL EXECUTED: the sealed
spec above was committed as "r352 pre-freeze" (88aae425, SPEC_SHA
freeze ad7a56682b4ecfd7) BEFORE the first full evaluation;
chronology honest: smoke pass 1 = 33/33 (0.2 s) at the sealed
rules, pass 2 byte-identical; pre-freeze commit 88aae425;
calibration pass 1 = FIRST full evaluation = 33/33 (94.2 s), NO
gate amendment; ONE disclosed PRINT-ONLY amendment a1 (r349
"every hole named" precedent): the EXT5_LEDGER prints in/low
band counts per column so every EXT5 out-row is NAMED by side --
no bar, band, family, candidate list or verdict rule moved, the
docstring and hence the freeze SPEC_SHA unchanged by a1; smoke
re-pass 33/33; record run1 = 33/33 (89.5 s), run2 = 33/33
(83.7 s), byte-identical up to WALL and identical to calibration
pass 1 except the a1 ledger field):
MAIN VERDICT = RHOR_REDUCED (ONE-OBJECT GRADE) -- THE TWO NAMED
RESTS ARE ONE OBJECT: the identities (i)-(iii) hold on all 81
rows at machine precision (max 2.1e-16 / 2.2e-16 abs / 2.2e-16),
the leading laws CANCEL (|s_csq - s_pq| = 0.0004 with s_csq
-1.3950 == 2 s_c exactly and s_pq -1.3953 -- the BK3 image:
rho_r is a SECOND-ORDER object, NOT composable from the leading
candidate laws), and the one-object clauses fire LOUDLY: at the
sealed common leading law A_LEAD = 17/12 the deficit fine
structure phi_D = log(pq) + A_LEAD ln N and the kernel fine
structure phi_K = log(c^2) + A_LEAD ln N satisfy corr = 0.999998
(clause 0.99) and rms(phi_D - phi_K)/rms(phi) = 0.0019 (clause
0.2): each column wanders 0.8787 nats, their difference is
0.0017 nats -- 500x SMALLER: THE DEFICIT REST AND THE KERNEL
REST ARE ONE SHARED WANDER, and rho_r is EXACTLY the decay of
their difference (phi_D - phi_K == LR == -log(c^2/pq) pointwise;
the LR law refits rho_r at |s_LR - s_rdet| = 0.0002 with LR curv
-0.767 == rdet curv: NO clean power law appears in the
weight-free normalization either -- the exponent 2.624 stays
curved-measured; a reduction and identification, NOT a source
derivation)
+ RHOK_LAW_FOUND(a_kap = 0.7111 re-gates CLEAN (curv +0.328,
EXT3 11/12 low 0, EXT4 5/6 low 0) and hits [2/3, 3/4] at 0.05 --
BOTH inside, mutually unresolvable, printed; the weight-free
kernel correlation rho_K = kappa^2 inherits a_rhoK = 2 a_kap =
1.4222 exactly (homogeneity gate 6.7e-16), candidate image
[4/3, 3/2] both hit at the doubled bar 0.1; doubled curvature
+0.656 > 0.35 disclosed -- the LAW lives on the kappa
normalization)
+ DECOR_REFUTED(slope(1 - rho_K) = +0.00061: the kernel
DECORRELATES (rho_K -> 0, 1 - rho_K -> 1; decay exponent
-0.0006, nowhere near rho_r and below DECOR_MIN 0.3) -- the
round's naming hypothesis is REFUTED CLEANLY, the r348
CARRIES_DELTA motif: the carrier of rho_r is not the kernel
decorrelation, it is the SATURATION of c^2/pq = the shared-
wander difference above)
+ GK12_EXPLAINED(e1 pointwise dictionary reconstruction max
|K12 sqrt(vp1 vp2)/c - 1| = 5.52e-4 <= 1e-2; e2 the c column
CLEAN (curv +0.308, EXT3 11/12, EXT4 low 0); e3 kappa CLEAN
(above) -- the ONE dirty column factorizes pointwise as K12 ==
[c, the CLEAN law] / sqrt[v1 v2, closed-form dictionary]; the
curvature bookkeeping curv(K12) +0.500 vs curv(c) - (curv(vp1)
+ curv(vp2))/2 = +0.826 (dev 0.327) is printed as CENSUS -- the
after-fit curvature sum carries the r347-C1 Theil-Sen
non-additivity on the strongly curved weight columns, the
POINTWISE factorization is the exact statement; SECOND
INSTRUMENT: the CD-recursion route reproduces the Gram route on
ALL 81 rows (r350 sample max 1.2e-10, all N_w <= 3200 max
2.4e-10, EXT5 max 7.4e-10 incl. N_w 5690 -- every graded bar
met) and the CD-refit K12 law is IDENTICAL (|s_K12cd - s_K12| =
1.5e-11): the r350 dirtiness (curv +0.500, EXT3 5/12) is a
STRUCTURE effect, not a measurement/route effect; REL2
honest-negative as expected: the flat column Q = K12/(K11
K22)^(1/4) FAILS the r345 protocol LOUDLY (CH1 21 out / 8 hard,
max dev 1.21 dec, slope +0.5359 CI [-1.14, +2.30], monotone-ish
cohort drift 0.796 dec: Q medians rise core ~10 -> EXT5 ~60) --
the r350 REL2 slope hit 0.035 was an after-fit coincidence on a
wildly scattering column, REL2 stays census)
+ CANDIDATES_UNRESOLVED(the honest deliverable -- the sealed
separation instrument on the deep cohort (EXT3 + EXT4 + EXT5 =
24 rows for p/q, EXT3 + EXT4 = 18 for y0): a_p (3/4 vs 2 x
0.38): closer-count 23/24 LEANS to 3/4 but the line gap at the
deep median is 0.0071 dec vs 2 x MAD 0.268 => UNRESOLVED,
required depth log10 N* = 29.5; a_q (2/3 vs 1 - 0.38):
closer-count 23/24 LEANS to 0.62 (the complement candidate!)
but gap 0.0329 vs 0.263 => UNRESOLVED, required log10 N* = 8.3;
delta_0 (0.38 vs 2/5): closer 12/18 leans 2/5, gap 0.0137 vs
0.0402 => UNRESOLVED, required log10 N* = 4.7 (the NEAREST
resolvable ambiguity -- one more x40 depth tranche could
separate delta_0); the closer-count leans are CENSUS, never
identifications -- the sealed gap clause refuses all three, and
the EXT5 tranche (1.8x record depth, 0.26 decades of lever)
cannot buy the ~3.3 decades a_q needs: the ladder-depth
arithmetic is the deliverable, typed for the specialists)
+ EXT5_LEDGER(selection gate PASSES: used ledger 98, fresh 9,
kz (69, 107, 101, 99, 115, 89) == the s2 queue, N_w == h on
6/6, z^2 <= 400000; THE DEEPEST L*-WINDOWS EVER MEASURED: N_w
4237..5690 = 1.8x the EXT4 record 3181; margins ALL POSITIVE
1.47e-9 .. 4.03e-9 -- THE L* CONDITION HOLDS 1.8x DEEPER THAN
EVERY PRIOR RECORD, out of sample, no contingency fired
(exclusions none, CD finite 6/6, block far under the 600 s
budget); bands from the 57-fit (in/low of 6): p 5/0, q 6/0, c
6/0, kap 6/0 -- THE BARE LAWS EXTEND -- vs K12 0/0, margin 0/0,
rdet 1/0, LR 1/0, rhoK 1/0: every out-row is HIGH side -- the
margin/reserve/cross-kernel columns sit ABOVE the 57-fit
extrapolation at EXT5 depth (the deep decay FLATTENS out of
sample: MORE margin than the naive power law predicts -- the
opposite side from the r342 EXT3 steepening reading, census,
the two-parameter running-exponent question named for r353))
+ BALANCE_LEDGER(alpha == a_p + a_q + rho_r - a_(p+q) = 0.754 +
0.645 + 2.624 - 0.690 = 3.333 vs alpha_meas 3.332 (dev 0.001);
candidate image 3/4 + 2/3 + rho_r - a_(p+q) = 3.352 (dev
0.019); THE CHAIN FULLY TYPED: weights WOERTERBUCH (r350),
deficits CANDIDATE-LAW (a_p [3/4, 2 x 0.38], a_q [2/3, 1 -
0.38], unresolved with required depths above), pinning
SATZ-grade (r350, not re-run), rho_r = THE ONE SECOND-ORDER
OBJECT == the shared-wander difference (this round) -- the
specialist package is FINAL: ONE object (the r338-q1
backward-CS fine structure), all exponents measured (a_p 0.754,
a_q 0.645, a_c 0.697, a_kap 0.711, g_K11 +1.786, g_K22 +1.683,
g_K12 +0.902, rho_r 2.624, delta_0 0.401, alpha 3.332), all
identities exact)
+ WORLD_LEDGER(the rho_K world column (census, no bar): live
MAIN/TWIN 0.00111 vs dead EPST 0.0107 / SCR ~1 / SMOOTH 0.00425
/ HL2 0.59 / DIR ~1 / ABS 0.51 -- live sits BELOW every dead
value, but the narrowest factor is only 3.8x (SMOOTH): a size
census, NOT a criterion; the SATURATION coordinate leaves [0,1]
on the dead side (EPST s = -0.021: pq < 0, a bare deficit flips
sign; SCR/DIR s ~ 1 from above) while the BARE r_det prints
POSITIVE on all six dead worlds at their own N_w -- the bare
pair reserve does NOT carry the live/dead separation, what
separates stays lambda_rest (re-gated 4/4 dead >= 1 vs live 2/2
< 1) and kappa_int == records at 5 percent (EPST 1793.99 / SCR
8.509e6 / SMOOTH 2.193 / HL2 1964.35, live 0.999567) -- honest:
the r342 'dead pair blocks cross 1' typing lives in the
DIAGONAL crossing (d >= 1 on EPST-type worlds), not in an
r_det sign flip)
+ TWIN_LEDGER(kap dev 1.4e-8, rhoK 2.7e-8, LR 1.5e-5, Q 1.3e-8
(bar 1e-3); dose-zero identity BITWISE)
+ MUSTFAIL_LEDGER(m1 wrong normalization breaks (ii) by 7.6e+04
rel at w9 + 2/69 == 0.0290 exactly on the Fractions toy; m2
AST-FLAGGED slope_col_true + toy 0.5833 in NO sealed list; m3
AST-FLAGGED resid_spread_true + toy 0.252 != sealed 2.0; m4
AST-FLAGGED gram_k12_true + CD-without-prefactor breaks by
1.2e+00 >= 0.1 at w9; m5 wrong REL2 power breaks the planted
flat toy by 0.850 == (g1 + g2)/4 exactly; constructor scopes +
fragment audit CLEAN).
Key numbers.  W9: rho_K 1.111385e-3 == kappa^2 (weights cancel),
1 - rho_K 0.998889, s 0.988439, LR 1.1629e-2 (== r_det 1.1561e-2
at 0.6 percent), Q 16.0225, K12 sqrt(vp1 vp2)/c 1.000552, CD dev
1.6e-13 -- all == the s1 scoping bit-near; the r347/r348/r350
anchor rows reproduced verbatim (bridge 1.0029, g21 7.5175,
K_res 2, rho_0 0.5787, y0 0.4213, rho_hi 0.3943, kernel row
bit-near).  LADDER: 81 rows (42 + 15 + 12 EXT3 + 6 EXT4 + 6
EXT5), every f64 margin positive; FIT ANCHORS margin -3.332 / c
-0.697 / p -0.754 / q -0.645 / rdet -2.624 / kap -0.711 / K11
+1.786 / K22 +1.683 / K12 +0.902 / y0 -0.401 / rhi -0.393 all ==
the disclosed priors at tol 0.02; curvatures margin -0.347 / c
+0.308 / rdet -0.767 / K12 +0.500 at tol 0.03; homogeneity
gates |s_rhoK - 2 s_kap| = 6.7e-16, |s_csq - 2 s_c| = 0.0
(Theil-Sen is exactly homogeneous -- instrument gates); cohort
medians rho_0 0.8392 / bridge 1.0058 == r348/r343.  HONEST
NEGATIVES: (1) RHOR_REDUCED is a REDUCTION AND IDENTIFICATION,
not a derivation: rho_r = 2.624 stays a measured, halves-curved
exponent (LR curv -0.767) -- the round proves WHERE it lives
(the difference of ONE shared fine-structure wander), not WHY it
has this value; (2) the round's naming hypothesis is refuted:
1 - rho_K saturates to 1 (slope +0.0006) -- the kernel
DEcorrelates, the carrier is the saturation of c^2/pq; (3) REL2
fails the flat protocol loudly (max dev 1.21 dec, drift 0.796)
-- the r350 slope hit 0.035 was an after-fit artifact of a
scattering column; (4) NO candidate ambiguity resolves (required
depths 10^4.7 / 10^8.3 / 10^29.5) and the closer-count leans
(3/4 for a_p, but 0.62 OVER 2/3 for a_q, 2/5 over 0.38 for
delta_0) are census leans on 18-24 rows, never identifications;
(5) the kap curvature +0.328 sits 0.02 under the 0.35 bar -- the
kappa law is CLEAN by a thin margin, said so; (6) the world
rho_K census separates by size with a thin 3.8x floor (SMOOTH)
and the bare r_det sign does NOT separate -- no new world
criterion claimed; (7) EXT5 carries the REDUCED bundle only (no
resolvent/pinning extension beyond N_w 3200, budget honesty);
the r350 det-shadow weak-rung caveat and the r348 WEAK_FAMILY
caveat stand (not re-run).  R353 SKETCH (candidates, not
commitments): (i) THE SHARED WANDER as its own lane: phi (rms
0.88 nats, the single unexplained function of the L* margin
legislation after this round) -- its cohort/atom structure and
whether the digamma/tent dictionary predicts phi itself; (ii)
the EXT5 HIGH-side flattening of the margin/reserve columns: a
sealed two-parameter running-exponent model vs the pure power on
the 81-row ladder (also the delta_0 separation at log10 N* =
4.7, the nearest resolvable ambiguity); (iii) the GRH-faithful
Dirichlet frame (U5) stays the named separate follow-up.
Runtime 89.5 / 83.7 s record, 94.2 s calibration, 0.2 s smoke;
deterministic, run1/run2 byte-identical up to WALL.  AMENDMENTS
AFTER FREEZE: the one disclosed print-only amendment a1 (the
EXT5 in/low ledger field, above) and this record-table insertion
-- nothing else.

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
import delta_alpha_closure_probe as DA           # noqa: E402 r347
import delta_source_anatomy_probe as DSA         # noqa: E402 r348
import alpha_source_anatomy_probe as ASA         # noqa: E402 r350
import ext3_fresh_anchors_probe as E3            # noqa: E402 r329
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
DA_SHA_PREFIX = "bd1aa7f3"
DSA_SHA_PREFIX = "307814e9"
ASA_SHA_PREFIX = "c3998c87"
E3_SHA_PREFIX = "bbfaf199"
DSW_SHA_PREFIX = "66526018"
W9_ANCH = dict(d1p=0.999154, d2p=0.998710, ppr=8.4606e-4,
               qpr=1.2903e-3, m2p=1.6800e-4, bridge=1.0029,
               cpc=2.7047e-2, g21=7.517, kres=2,
               lam_rest=0.996338, rho0=0.5787, y0=0.42134,
               rho_hi=0.39430)
K9_ANCH = dict(v1=4.023172e-6, v2=4.360131e-6, K11=2.411068e5,
               K22=2.213016e5, K12=7.700682e3, kap=3.333744e-2,
               vp1=4.023992e-6, vp2=4.364056e-6)
RHO9_ANCH = dict(rhoK=1.111385e-3, LR=1.1629e-2, Q=16.0225,
                 cdc=1.000552, rdet=1.1561e-2)
SAMPLE_ANCH = {44: dict(kap=1.746679e-2, rhoK=3.050887e-4,
                        LR=1.0667e-4, Q=6.5991),
               56: dict(kap=1.547570e-2, rhoK=2.394972e-4,
                        LR=7.7500e-6, Q=45.6367),
               130: dict(kap=8.014410e-3, rhoK=6.423076e-5,
                         LR=2.0166e-6, Q=16.8488)}
MED_ANCH = dict(rho0=0.839, bridge=1.0058)
FIT_ANCH = dict(margin=-3.332, c=-0.697, p=-0.754, q=-0.645,
                rdet=-2.624, kap=-0.711, K11=1.786, K22=1.683,
                K12=0.902, y0=-0.401, rhi=-0.393)
FIT_ANCH_TOL = 0.02
CURV_ANCH = dict(margin=-0.347, c=0.308, rdet=-0.767, K12=0.500)
CURV_ANCH_TOL = 0.03
ALPHA_REC = 3.332            # WITHHELD record constant
RHOR_REC = 2.624             # WITHHELD record constant
P_BIND = 0.38
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN, EXT3_NW_MAX = 1721, 2577
EXT4_KZ_B = (72, 75, 66)
EXT4_KZ_A = (113, 111, 108)
EXT4_NW_MIN, EXT4_NW_MAX = 2656, 3181
EXT5_H_LO = 3401
EXT5_H_HI = 6000
K_EXT5 = 6
Z2_CAP = 400000
USED_EXPECT = 98
FRESH5_EXPECT = 9
EXT5_KZ_EXPECT = (69, 107, 101, 99, 115, 89)
EXT5_H_EXPECT = (5690, 5668, 5242, 5073, 4243, 4237)
EXT5_BUDGET_S = 600.0
CSQ_ID_BAR = 1.0e-12
RID_ABS = 1.0e-9
ADD_SPLIT_BAR = 1.0e-9
HOM_BAR = 1.0e-9
LEAD_CANCEL_BAR = 0.05
A_LEAD = 17.0 / 12.0
FS_CORR_MIN = 0.99
FS_RMSR_MAX = 0.2
LR_MATCH_BAR = 0.05
DECOR_MIN = 0.3
DECOR_MATCH = 0.5
CD_KZ = (18, 9, 52, 119, 42, 130)
CD_BAR = 1.0e-6
CD_BAR_MID = 1.0e-5
CD_BAR_DEEP = 1.0e-3
CD_MID_NW = 3200
CD2_FIT_BAR = 1.0e-6
RECON_BAR = 1.0e-2
DEC_CURV_BAR = 0.35
DEC_EXT3_MIN = 10
DEC_EXT4_LOW = 1
CAND_BAR = 0.05
RHOK_BAR = 0.1
CAND_KAP = (0.5, 2.0 / 3.0, 0.75, 1.0)
CAND_RHOK = (1.0, 4.0 / 3.0, 1.5, 2.0)
SEP_P = (0.75, 0.76)
SEP_Q = (2.0 / 3.0, 0.62)
SEP_D0 = (0.38, 0.4)
SEP_FRAC = 5.0 / 6.0
SEP_GAP_FACTOR = 2.0
COMP_BAR = 0.1
REL2_POW = 0.25
SPLIT_BAR = 1.0e-9
CPC_ID_BAR = 1.0e-6
ID_BAR = 1.0e-8
RDEF_BAR = 1.0e-12
DET_ID_BAR = 1.0e-12
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
M4_BAR = 0.1
M5_MIN = 0.5
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


CONSTRUCTORS = ("rho_corr_cols", "fine_structure", "rel2_column",
                "cd_cols", "sep_required_depth", "sep_adjudicate")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "KINT_REC", "FIT_ANCH",
                   "CURV_ANCH", "W9_ANCH", "K9_ANCH", "RHO9_ANCH",
                   "MED_ANCH", "SAMPLE_ANCH", "ALPHA_REC",
                   "RHOR_REC", "slope_col_true",
                   "resid_spread_true", "gram_k12_true"}


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
def rho_corr_cols(d1, d2, c, p, q):
    """the kernel-correlation coordinates from the exact pair
    identities: rho_K = c^2/(d1 d2) (== K12^2/(K11 K22): the
    weights cancel), the saturation s = c^2/(pq), the log reserve
    LR = -log s; consumes pair scalars only."""
    rhoK = c * c / (d1 * d2)
    s = c * c / (p * q)
    return rhoK, s, -math.log(s)


def fine_structure(lnN, log_pq, log_csq, a_lead):
    """the fine-structure pair: phi_D = log(pq) + a_lead lnN,
    phi_K = log(c^2) + a_lead lnN, both demeaned (median); returns
    (corr, rmsr, rms_D, rms_K, rms_diff, phi_D, phi_K); consumes
    measured columns + the sealed leading exponent only."""
    lnN = np.asarray(lnN, float)
    pD = np.asarray(log_pq, float) + a_lead * lnN
    pK = np.asarray(log_csq, float) + a_lead * lnN
    pD = pD - float(np.median(pD))
    pK = pK - float(np.median(pK))
    dd = pD - pK
    dd = dd - float(np.median(dd))
    rms_D = float(np.sqrt(np.mean(pD ** 2)))
    rms_K = float(np.sqrt(np.mean(pK ** 2)))
    rms_d = float(np.sqrt(np.mean(dd ** 2)))
    corr = float(np.corrcoef(pD, pK)[0, 1])
    rmsr = rms_d / max(rms_D, rms_K, 1e-300)
    return corr, rmsr, rms_D, rms_K, rms_d, pD, pK


def rel2_column(k12, k11, k22):
    """the REL2-equivalent flat column: Q = K12/(K11 K22)^(1/4)
    -- log-flat iff g_K12 == (g_K11 + g_K22)/4; consumes kernel
    columns only."""
    return abs(k12) / (k11 * k22) ** REL2_POW


def cd_cols(xp, wp, yn, i1, i2, Nw):
    """the SECOND INSTRUMENT: the kernel columns at the pair via
    the Christoffel-Darboux endpoint route (chain recomputed from
    the measure, r350 formulas verbatim); consumes measure arrays
    + positions only."""
    aa, bb, h0 = V.mu_chain(xp, wp, Nw)
    y1 = float(yn[i1])
    y2 = float(yn[i2])
    K11c, K22c, K12c = ASA.cd_kernel_route(aa, bb, h0, y1, y2, Nw)
    return K11c, K22c, K12c, (aa, bb, h0, y1, y2)


def sep_required_depth(w_res, delta, lnN_piv):
    """the sealed required-depth formula: lnN* = lnN_piv +
    SEP_GAP_FACTOR w_res ln10 / delta -- the depth at which two
    candidate lines diverge by SEP_GAP_FACTOR x the residual
    scatter (decades); consumes scalars only."""
    return lnN_piv + SEP_GAP_FACTOR * w_res * math.log(10.0) / delta


def sep_adjudicate(lnN_deep, logv_deep, lnN_piv, y_piv, cA, cB):
    """the sealed candidate-separation instrument: lines through
    the pivot with slopes -cA/-cB, per-row closer counts, the line
    gap at the deep median vs the deep residual MAD (both in
    decades); consumes measured deep columns + the pivot + the
    frozen candidate pair only."""
    lnN_deep = np.asarray(lnN_deep, float)
    logv_deep = np.asarray(logv_deep, float)
    l10 = math.log(10.0)
    rA = (logv_deep - (y_piv - cA * (lnN_deep - lnN_piv))) / l10
    rB = (logv_deep - (y_piv - cB * (lnN_deep - lnN_piv))) / l10
    nA = int(np.sum(np.abs(rA) < np.abs(rB)))
    nB = int(np.sum(np.abs(rB) < np.abs(rA)))
    ln_med = float(np.median(lnN_deep))
    gap = abs(cA - cB) * (ln_med - lnN_piv) / l10
    r0 = rA - float(np.median(rA))
    mad = float(np.median(np.abs(r0)))
    return nA, nB, gap, mad


# ============== must-fail mutants
def mutant_rho_wrongnorm(d1, d2, c, p, q):
    """m1 MUST-FAIL: the correlation normalized by the DEFICITS
    (c^2/(pq)) instead of the diagonals -- must break the exact
    identity (ii) loudly."""
    return c * c / (p * q)


def mutant_cand_posthoc(slope_col_true):
    """m2 MUST-FAIL: the candidate re-picked AFTER SIGHT as the
    nearest twelfth of the seen slope -- consumes the withheld
    column; AST-FLAGGED."""
    s = sorted(slope_col_true)[len(slope_col_true) // 2]
    return round(abs(s) * 12.0) / 12.0


def mutant_sepbar_posthoc(resid_spread_true):
    """m3 MUST-FAIL: the separation gap bar re-picked AFTER SIGHT
    of the measured deep spread -- consumes the withheld spread;
    AST-FLAGGED."""
    return resid_spread_true * 1.2


def mutant_cd_readback(gram_k12_true):
    """m4 MUST-FAIL (AST half): a 'second instrument' that just
    returns the withheld first-route Gram value -- AST-FLAGGED."""
    return gram_k12_true


def mutant_cd_unnormalized(aa, bb, h0, y1, y2, Nw):
    """m4 MUST-FAIL (loud half): the CD endpoint formula WITHOUT
    the b_{N-1} prefactor (r350 m1 verbatim) -- must break the
    kernel ward loudly."""
    _K11, _K22, K12 = ASA.cd_kernel_route(aa, bb, h0, y1, y2, Nw)
    return K12 / bb[Nw - 1]


def mutant_rel2_wrongpower(k12, k11, k22):
    """m5 MUST-FAIL: the REL2 column with the WRONG power 1/2 --
    must break the planted flat toy loudly."""
    return abs(k12) / (k11 * k22) ** 0.5


# ============== gate-side helpers
def rung_rho_extras(R, K):
    """the r352 extension of one rung: rho_K coordinates, the
    REL2 column, the dictionary-normalized cross kernel, and the
    three identity residuals."""
    rhoK, s, LR = rho_corr_cols(R["d1"], R["d2"], R["c"], R["p"],
                                R["q"])
    id1 = abs(R["c"] ** 2 - rhoK * R["d1"] * R["d2"]) \
        / max(R["c"] ** 2, 1e-300)
    id2 = abs(R["rdet"] - (1.0 - rhoK * R["d1"] * R["d2"]
                           / (R["p"] * R["q"])))
    blk1 = 1.0 - rhoK
    blk2 = rhoK * (R["p"] + R["q"] - 1.0) / (R["p"] * R["q"])
    id3 = abs(R["rdet"] - (blk1 + blk2)) \
        / max(abs(blk1), abs(blk2), 1e-300)
    Q = rel2_column(K["K12"], K["K11"], K["K22"])
    cdc = K["K12"] * math.sqrt(K["vp1"] * K["vp2"]) / R["c"]
    return dict(rhoK=rhoK, s=s, LR=LR, omr=blk1, blk2=blk2,
                id1=id1, id2=id2, id3=id3, Q=Q, cdc=cdc)


def vpred_pair(R):
    """gate-side dictionary weights at the pair (r342 route
    verbatim, the r350 rung_kernel_extras pattern) for the
    REDUCED EXT5 bundle."""
    alpha_, M_, L_, _Nw, D_ = V.window_shape(R["kz"])
    ka_ = int(np.searchsorted(V.U, 2.0 * alpha_ + 1e-14,
                              side="right"))
    uu_ = np.asarray(V.U[:ka_], float)
    mm_ = np.asarray(V.W_VM[:ka_], float)
    vps = []
    for ff in (R["f1"], R["f2"]):
        th = 2.0 * math.pi * ff / L_
        vp, _a, _p = PX.v_predict(th, alpha_, M_, L_, D_, uu_, mm_)
        vps.append(vp)
    return vps[0], vps[1]


def slim352(R, P, keepK=None):
    """memory hygiene: keep only the fit-side scalars (kz9 keeps
    its full bundle at the caller)."""
    keep_R = {k: R[k] for k in ("kz", "z", "Nw", "Sm", "margin",
                                "c", "p", "q", "d1", "d2", "v1",
                                "v2", "rdet", "lam_rest",
                                "det_dev", "schur_dev")
              if k in R}
    return keep_R, P, keepK


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("rhor_source_anatomy_probe -- PRIME.LSTAR."
          "RHOR_SOURCE_ANATOMY.01 (round 352)")
    print("SPEC_SHA %s   (r342 PX %s / r343 PC3 %s / r345 GR %s / "
          "r347 DA %s / r348 DSA %s / r350 ASA %s / r329 E3 %s / "
          "r330 DSW %s)"
          % (SPEC_SHA[:16], PX.SPEC_SHA[:16], PC3.SPEC_SHA[:16],
             GR.SPEC_SHA[:16], DA.SPEC_SHA[:16], DSA.SPEC_SHA[:16],
             ASA.SPEC_SHA[:16], E3.SPEC_SHA[:16],
             DSW.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ w9 block; ladder, EXT5, twin, fits, "
                        "adjudications, worlds skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    ok_sha = (PX.SPEC_SHA.startswith(PX_SHA_PREFIX)
              and PC3.SPEC_SHA.startswith(PC3_SHA_PREFIX)
              and GR.SPEC_SHA.startswith(GR_SHA_PREFIX)
              and DA.SPEC_SHA.startswith(DA_SHA_PREFIX)
              and DSA.SPEC_SHA.startswith(DSA_SHA_PREFIX)
              and ASA.SPEC_SHA.startswith(ASA_SHA_PREFIX)
              and E3.SPEC_SHA.startswith(E3_SHA_PREFIX)
              and DSW.SPEC_SHA.startswith(DSW_SHA_PREFIX))
    check("G02-predefinition", ok_sha,
          "sealed BEFORE evaluation: r342/r343/r345/r347/r348/"
          "r350/r329/r330 machinery imported verbatim (SPEC_SHA "
          "%s == %s*, %s == %s*, %s == %s*, %s == %s*, %s == %s*, "
          "%s == %s*, %s == %s*, %s == %s*), the rho_K identities "
          "(bars %.0e/%.0e/%.0e), the homogeneity gates (%.0e), "
          "the one-object clauses (corr >= %.2f, rmsr <= %.1f, "
          "A_LEAD 17/12), the DECOR clause (min %.1f, match %.1f), "
          "the graded CD wards (%.0e/%.0e/%.0e), the REL2 column "
          "(power %.2f) under the r345 protocol, the GK12 clauses "
          "(recon %.0e, decay clauses %.2f/%d/%d), the EXT5 "
          "selection (h (%d, %d], K %d, cap %d, expected %s), the "
          "separation instrument (frac %.2f, gap factor %.1f, "
          "pairs P %s / Q %s / D0 %s), the candidate lists (KAP "
          "%s at %.2f, RHOK %s at %.1f), the composition re-gate "
          "(%.1f), every bar/tolerance, the mutants and the "
          "verdict form; pre-spec scoping s1-s3 disclosed in the "
          "spec; the STOP list forbids any L* claim and any "
          "certificate reading beyond the sealed census"
          % (PX.SPEC_SHA[:8], PX_SHA_PREFIX, PC3.SPEC_SHA[:8],
             PC3_SHA_PREFIX, GR.SPEC_SHA[:8], GR_SHA_PREFIX,
             DA.SPEC_SHA[:8], DA_SHA_PREFIX, DSA.SPEC_SHA[:8],
             DSA_SHA_PREFIX, ASA.SPEC_SHA[:8], ASA_SHA_PREFIX,
             E3.SPEC_SHA[:8], E3_SHA_PREFIX, DSW.SPEC_SHA[:8],
             DSW_SHA_PREFIX, CSQ_ID_BAR, RID_ABS, ADD_SPLIT_BAR,
             HOM_BAR, FS_CORR_MIN, FS_RMSR_MAX, DECOR_MIN,
             DECOR_MATCH, CD_BAR, CD_BAR_MID, CD_BAR_DEEP,
             REL2_POW, RECON_BAR, DEC_CURV_BAR, DEC_EXT3_MIN,
             DEC_EXT4_LOW, EXT5_H_LO - 1, EXT5_H_HI, K_EXT5,
             Z2_CAP, str(EXT5_KZ_EXPECT), SEP_FRAC,
             SEP_GAP_FACTOR, str(SEP_P), str(SEP_Q), str(SEP_D0),
             str(CAND_KAP), CAND_BAR, str(CAND_RHOK), RHOK_BAR,
             COMP_BAR))
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    hits_m2 = scope_audit("mutant_cand_posthoc")
    hits_m3 = scope_audit("mutant_sepbar_posthoc")
    hits_m4 = scope_audit("mutant_cd_readback")
    check("G03-scope-audits", not hits and not ag_hits
          and bool(hits_m2) and bool(hits_m3) and bool(hits_m4),
          "the %d module-own constructors consume kernel Gram / "
          "spectrum / weight / position / chain-coefficient "
          "arrays and measured columns ONLY (%s); fragment audit "
          "(no fit primitives beyond the imported r286 Theil-Sen "
          "+ r345 protocol + r347 decay instrument): %s; m2 "
          "FLAGGED (%s); m3 FLAGGED (%s); m4 FLAGGED (%s)"
          % (len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits),
             hits_m2[0] if hits_m2 else "MISS",
             hits_m3[0] if hits_m3 else "MISS",
             hits_m4[0] if hits_m4 else "MISS"))

    # ---------------- S1 toys
    section("S1  TOYS -- FRACTIONS IDENTITIES + FINE STRUCTURE + "
            "REL2 + CD + SEPARATION")
    # (T1) exact Fractions identities on the r342 hand toy
    d1f, d2f, cf = Fr(1, 4), Fr(1, 2), Fr(1, 8)
    pf, qf = 1 - d1f, 1 - d2f
    rhoKf = cf * cf / (d1f * d2f)
    rdetf = 1 - cf * cf / (pf * qf)
    r_ii = 1 - rhoKf * d1f * d2f / (pf * qf)
    r_iii = (1 - rhoKf) + rhoKf * (pf + qf - 1) / (pf * qf)
    m1f = 1 - (cf * cf / (pf * qf)) * d1f * d2f / (pf * qf)
    ok_fr = (rhoKf == Fr(1, 8) and rdetf == Fr(23, 24)
             and r_ii == Fr(23, 24) and r_iii == Fr(23, 24)
             and m1f == Fr(71, 72)
             and abs(m1f - rdetf) / rdetf == Fr(2, 69))
    rk_f, s_f, LR_f = rho_corr_cols(float(d1f), float(d2f),
                                    float(cf), float(pf),
                                    float(qf))
    ok_con = (abs(rk_f - 0.125) <= TOY_TOL
              and abs(s_f - float(1 - rdetf)) <= TOY_TOL
              and abs(LR_f - math.log(24.0)) <= TOY_TOL)
    check("G10-toy-fractions-identities", ok_fr and ok_con,
          "EXACT FRACTIONS on the r342 hand toy (d1 1/4, d2 1/2, "
          "c 1/8): rho_K == 1/8, r_det == 23/24 on the direct "
          "route AND identity (ii) AND the additive split (iii); "
          "the m1 wrong-normalization value == 71/72, off by "
          "EXACTLY 2/69; the audited constructor matches at 1e-12 "
          "(LR == log 24)")
    # (T2) fine-structure toy: shared wander + planted difference
    Nt = 200.0 * 1.25 ** np.arange(24)
    lnNt = np.log(Nt)
    kk = np.arange(24)
    wander = 0.35 * np.sin(3.0 * kk)
    A_t = 1.4
    log_pq_t = math.log(2e-3) - A_t * lnNt + wander
    e_t = 1e-3 * (Nt / 200.0) ** (-2.6)
    log_csq_t = log_pq_t + np.log(1.0 - e_t)
    co_t, rr_t, rD_t, rK_t, rd_t, _pD, _pK = fine_structure(
        lnNt, log_pq_t, log_csq_t, A_t)
    ft_lr = LM.ts_fit(lnNt, np.log(-(log_csq_t - log_pq_t)))
    wander2 = 0.35 * np.sin(3.0 * kk + 2.0)
    co_x, rr_x, _r1, _r2, _r3, _p1, _p2 = fine_structure(
        lnNt, log_pq_t, log_pq_t - 0.3 + (wander2 - wander), A_t)
    check("G11-toy-fine-structure", co_t >= 0.999 and rr_t <= 0.05
          and abs(float(ft_lr[1]) + 2.6) <= 1e-3
          and co_x < FS_CORR_MIN and rr_x > FS_RMSR_MAX,
          "FINE-STRUCTURE TOY (shared 0.35-nat wander + planted "
          "N^-2.6 difference): corr %.6f >= 0.999, rmsr %.4f <= "
          "0.05, the difference column refits the planted "
          "exponent at %.1e (rms_D %.3f, rms_K %.3f, rms_diff "
          "%.4f); INDEPENDENT-WANDER CONTROL: corr %.3f < %.2f "
          "and rmsr %.2f > %.1f -- the clause REFUSES uncorrelated "
          "fine structure" % (co_t, rr_t,
                              abs(float(ft_lr[1]) + 2.6), rD_t,
                              rK_t, rd_t, co_x, FS_CORR_MIN, rr_x,
                              FS_RMSR_MAX))
    # (T3) REL2 column toy + m5 sizing
    g1_t, g2_t = 1.8, 1.6
    K11_t = 1e3 * (Nt / 200.0) ** g1_t
    K22_t = 8e2 * (Nt / 200.0) ** g2_t
    K12_t = 5e2 * (Nt / 200.0) ** ((g1_t + g2_t) / 4.0)
    Q_t = rel2_column(K12_t, K11_t, K22_t)
    ft_q = LM.ts_fit(lnNt, np.log(Q_t))
    Qw_t = mutant_rel2_wrongpower(K12_t, K11_t, K22_t)
    ft_qw = LM.ts_fit(lnNt, np.log(Qw_t))
    dev_m5 = abs(float(ft_qw[1]))
    check("G12-toy-rel2", abs(float(ft_q[1])) <= 1e-9
          and abs(dev_m5 - (g1_t + g2_t) / 4.0) <= 1e-9,
          "REL2 COLUMN TOY (planted g_K12 == (g1 + g2)/4): the "
          "sealed column Q = K12/(K11 K22)^(1/4) is EXACTLY flat "
          "(slope %.1e); the m5 wrong-power column breaks by "
          "%.3f == (g1 + g2)/4 exactly" % (abs(float(ft_q[1])),
                                           dev_m5))
    # (T4) CD identity on a synthetic 5-atom measure (r350 T1)
    x_t = np.array([-0.8, -0.3, 0.2, 0.5, 0.9])
    w_t = np.array([0.2, 0.3, 0.1, 0.25, 0.15])
    dep_t = 4
    y_t = np.array([0.7, -0.6])
    aa_t, bb_t, h0_t = V.mu_chain(x_t, w_t, dep_t)
    B_t = V.b_matrix(aa_t, bb_t, h0_t, y_t, np.array([1.0, 1.0]),
                     dep_t)
    K12_dir = float(B_t[0] @ B_t[1])
    K11_dir = float(B_t[0] @ B_t[0])
    K22_dir = float(B_t[1] @ B_t[1])
    K11_c, K22_c, K12_c, _args_t = cd_cols(x_t, w_t, y_t, 0, 1,
                                           dep_t)
    dev_t4 = max(abs(K11_c / K11_dir - 1.0),
                 abs(K22_c / K22_dir - 1.0),
                 abs(K12_c / K12_dir - 1.0))
    check("G13-toy-cd-identity", dev_t4 <= TOY_TOL * 10.0,
          "THE CD SECOND-INSTRUMENT TOY (synthetic 5-atom "
          "measure, depth %d): the endpoint/confluent route == "
          "the direct Gram sums at %.1e -- the audited cd_cols "
          "constructor is exact on exact data" % (dep_t, dev_t4))
    # (T5) separation instrument toy
    lnD_t = np.log(np.array([2000.0, 2400.0, 2800.0, 3200.0,
                             4200.0, 5600.0]))
    piv_t = math.log(500.0)
    ypiv_t = math.log(3e-3)
    clean_t = ypiv_t - 0.75 * (lnD_t - piv_t) \
        + 0.005 * np.sin(np.arange(6.0))
    nA_t, nB_t, gap_t, mad_t = sep_adjudicate(
        lnD_t, clean_t, piv_t, ypiv_t, 0.75, 0.62)
    res_t = (nA_t >= math.ceil(SEP_FRAC * 6)
             and gap_t >= SEP_GAP_FACTOR * mad_t)
    noisy_t = ypiv_t - 0.75 * (lnD_t - piv_t) \
        + 0.5 * np.sin(np.arange(6.0) * 2.0)
    nA_n, nB_n, gap_n, mad_n = sep_adjudicate(
        lnD_t, noisy_t, piv_t, ypiv_t, 0.75, 0.76)
    res_n = (max(nA_n, nB_n) >= math.ceil(SEP_FRAC * 6)
             and gap_n >= SEP_GAP_FACTOR * mad_n)
    req_t = sep_required_depth(mad_n, 0.01, piv_t)
    ok_req = req_t > math.log(1e6)
    check("G14-toy-separation", res_t and not res_n and ok_req,
          "SEPARATION TOY: the clean planted 0.75-vs-0.62 case "
          "RESOLVES (closer %d/6, gap %.3f dec >= %.1f x MAD "
          "%.4f); the noisy 0.75-vs-0.76 case REFUSES (gap %.4f "
          "vs MAD %.3f); the required-depth formula prints ln N* "
          "= %.1f (> ln 1e6) for gap 0.01 at that scatter -- the "
          "instrument is honest about short ladders"
          % (nA_t, gap_t, SEP_GAP_FACTOR, mad_t, gap_n, mad_n,
             req_t))

    # ---------------- S2 w9 flagship
    section("S2  W9 -- RECORDS + KERNEL + RHO COLUMNS + CD ROUTE")
    R9 = PX.build_rung(MAIN_KZ)
    X9 = PC3.extend_rung(R9)
    C9 = DA.closure_cols(R9)
    Y9 = DSA.rung_extras(R9, X9, C9)
    K9 = ASA.rung_kernel_extras(R9, X9, C9, Y9)
    P9 = rung_rho_extras(R9, K9)
    mz9 = R9["mz"]
    K11cd9, K22cd9, K12cd9, cd_args9 = cd_cols(
        mz9["xp"], mz9["wp"], mz9["yn"], R9["i1"], R9["i2"],
        mz9["Nw"])
    dev_cd9 = max(abs(K11cd9 / K9["K11"] - 1.0),
                  abs(K22cd9 / K9["K22"] - 1.0),
                  abs(K12cd9 / K9["K12"] - 1.0))
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
    A = W9_ANCH
    KA = K9_ANCH
    ok_anch = (abs(R9["d1p"] / A["d1p"] - 1.0) <= 1e-5
               and abs(R9["d2p"] / A["d2p"] - 1.0) <= 1e-5
               and abs(C9["ppr"] / A["ppr"] - 1.0) <= 1e-3
               and abs(C9["qpr"] / A["qpr"] - 1.0) <= 1e-3
               and abs(C9["m2p"] / A["m2p"] - 1.0) <= 1e-3
               and abs(C9["bridge"] - A["bridge"]) <= 5e-3
               and abs(C9["cpc"] / A["cpc"] - 1.0) <= 1e-3
               and abs(X9["g21"] - A["g21"]) <= 0.01
               and X9["k_res"] == A["kres"]
               and abs(R9["lam_rest"] - A["lam_rest"]) <= 1e-5
               and abs(Y9["rho0"] - A["rho0"]) <= 5e-3
               and abs(Y9["y0"] - A["y0"]) <= 5e-3
               and abs(Y9["rho_hi"] - A["rho_hi"]) <= 5e-3
               and abs(R9["v1"] / KA["v1"] - 1.0) <= 1e-3
               and abs(R9["v2"] / KA["v2"] - 1.0) <= 1e-3
               and abs(K9["K11"] / KA["K11"] - 1.0) <= 1e-3
               and abs(K9["K22"] / KA["K22"] - 1.0) <= 1e-3
               and abs(K9["K12"] / KA["K12"] - 1.0) <= 1e-3
               and abs(K9["kap"] / KA["kap"] - 1.0) <= 1e-3
               and abs(K9["vp1"] / KA["vp1"] - 1.0) <= 1e-3
               and abs(K9["vp2"] / KA["vp2"] - 1.0) <= 1e-3)
    check("G21-w9-anchors", ok_anch,
          "LEG 0 BIT-NEAR: the r347/r348 closure row (p' %.4e, "
          "q' %.4e, m2' %.4e, bridge %.4f, c'/c %.4e, g21 %.4f, "
          "K_res %d, lambda_rest %.6f, rho_0 %.4f, y0 %.4f, "
          "rho_hi %.4f) and the r350 kernel row (v1 %.6e, v2 "
          "%.6e, K11 %.6e, K22 %.6e, K12 %.6e, kappa %.6e, vp "
          "%.6e/%.6e) reproduced -- the r352 coordinates start "
          "exactly where r342..r350 left them"
          % (C9["ppr"], C9["qpr"], C9["m2p"], C9["bridge"],
             C9["cpc"], X9["g21"], X9["k_res"], R9["lam_rest"],
             Y9["rho0"], Y9["y0"], Y9["rho_hi"], R9["v1"],
             R9["v2"], K9["K11"], K9["K22"], K9["K12"], K9["kap"],
             K9["vp1"], K9["vp2"]))
    PA = RHO9_ANCH
    ok_rho9 = (abs(P9["rhoK"] / PA["rhoK"] - 1.0) <= 1e-3
               and abs(P9["LR"] / PA["LR"] - 1.0) <= 1e-3
               and abs(P9["Q"] / PA["Q"] - 1.0) <= 1e-3
               and abs(P9["cdc"] - PA["cdc"]) <= 1e-3
               and abs(R9["rdet"] / PA["rdet"] - 1.0) <= 1e-3
               and P9["id1"] <= CSQ_ID_BAR
               and P9["id2"] <= RID_ABS
               and P9["id3"] <= ADD_SPLIT_BAR
               and dev_cd9 <= CD_BAR)
    check("G22-w9-rho-columns", ok_rho9,
          "THE RHO COLUMNS LIVE at w9: rho_K = %.6e (s1 %.6e; == "
          "kappa^2, the weights cancel), 1 - rho_K = %.6f (the "
          "DECORRELATION -- note it sits near 1, not near 0), s "
          "= c^2/pq = %.6f, LR = -log s = %.4e (== r_det %.4e "
          "at 0.6%%), Q = %.4f, dictionary-normalized cross "
          "kernel K12 sqrt(vp1 vp2)/c = %.6f; IDENTITIES: (i) "
          "%.1e (bar %.0e), (ii) %.1e abs (bar %.0e), (iii) "
          "additive split %.1e (bar %.0e); CD SECOND INSTRUMENT "
          "%.1e (bar %.0e)"
          % (P9["rhoK"], PA["rhoK"], P9["omr"], P9["s"], P9["LR"],
             R9["rdet"], P9["Q"], P9["cdc"], P9["id1"],
             CSQ_ID_BAR, P9["id2"], RID_ABS, P9["id3"],
             ADD_SPLIT_BAR, dev_cd9, CD_BAR))

    # ---------------- S3 the ladder + EXT5
    section("S3  THE LADDER (42 + 15 + 12 EXT3 + 6 EXT4) + THE "
            "EXT5 TRANCHE")
    if smoke:
        for g in ("G30-ext5-selection", "G31-ladder-census",
                  "G32-ladder-identities", "G33-cohort-anchors"):
            check(g, True, "SMOKE: skipped")
        RT, PT, KT = {9: R9}, {9: P9}, {9: K9}
        YT, CT = {9: Y9}, {9: C9}
        cd_fit = {9: (K12cd9, dev_cd9)}
        core_kzs, ext_kzs, ext3_kzs, ext4_kzs, ext5_kzs = \
            [9], [], [], [], []
        excl = []
        ext5_excl = []
    else:
        # sealed EXT5 selection (r343 rule verbatim, raised cap)
        lm_rows = LM.ext_rule()
        used = set(E3.used_kz_set(core.frame_a_zones(), lm_rows,
                                  35))
        used |= set(EXT3_KZ_B + EXT3_KZ_A)
        used |= set(EXT4_KZ_B + EXT4_KZ_A)
        pool5 = E3.admissible_pool(EXT5_H_LO, EXT5_H_HI)
        zz5 = {kz: int(core._NN[kz]) for (_h, kz) in pool5}
        fresh5 = [(h, kz) for (h, kz) in pool5
                  if kz not in used
                  and zz5[kz] * zz5[kz] <= Z2_CAP]
        fresh5.sort(reverse=True)
        ext5_sel = tuple(kz for (_h, kz) in fresh5[:K_EXT5])
        ext5_h = tuple(h for (h, _kz) in fresh5[:K_EXT5])
        grid_ok = all(int(V.PP[kz]) == int(core._NN[kz])
                      for kz in ext5_sel)
        check("G30-ext5-selection",
              len(used) == USED_EXPECT
              and len(fresh5) == FRESH5_EXPECT
              and ext5_sel == EXT5_KZ_EXPECT
              and ext5_h == EXT5_H_EXPECT and grid_ok,
              "SEALED EXT5 SELECTION executed verbatim (r343 rule "
              "with the h window RAISED to (%d, %d]): used ledger "
              "%d (== %d, incl. EXT3 + EXT4), domain-capped fresh "
              "%d (== %d, z^2 <= %d), the %d deepest by (h, kz) "
              "descending %s (h %s) == the s2-disclosed queue; "
              "kz-grid identity V.PP == core._NN on all %d"
              % (EXT5_H_LO - 1, EXT5_H_HI, len(used), USED_EXPECT,
                 len(fresh5), FRESH5_EXPECT, Z2_CAP, K_EXT5,
                 str(ext5_sel), str(ext5_h), K_EXT5))
        ext5_kzs = list(ext5_sel)
        core_kzs = list(V.admissible_indices())
        ext_kzs = [t[1] for t in lm_rows[:15]]
        ext3_kzs = list(EXT3_KZ_B + EXT3_KZ_A)
        ext4_kzs = list(EXT4_KZ_B + EXT4_KZ_A)
        RT, PT, KT, YT, CT = {}, {}, {}, {}, {}
        cd_fit = {}
        neg_rows = []
        ext5_excl = []
        t_ext5 = 0.0
        print("    %-5s %-5s %-5s %-5s | %-10s %-10s %-10s | "
              "%-10s %-10s %-9s | %-8s %-8s | %-8s"
              % ("kz", "z", "S-", "N_w", "margin", "rdet", "LR",
                 "kap", "rhoK", "1-rhoK", "Q", "cdc-1", "cd_dev"))
        for kz in (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                   + ext5_kzs):
            t_r = time.time()
            reduced = kz in set(ext5_kzs)
            if kz == MAIN_KZ:
                R, X, C, Y, K, P = R9, X9, C9, Y9, K9, P9
                cdd = (K12cd9, dev_cd9)
            else:
                R = PX.build_rung(kz)
                if reduced:
                    vp1, vp2 = vpred_pair(R)
                    K = dict(K11=R["d1"] / R["v1"],
                             K22=R["d2"] / R["v2"],
                             K12=R["c"] / math.sqrt(R["v1"]
                                                    * R["v2"]),
                             kap=None, vp1=vp1, vp2=vp2)
                    K["kap"] = K["K12"] / math.sqrt(K["K11"]
                                                    * K["K22"])
                    X = C = Y = None
                else:
                    X = PC3.extend_rung(R)
                    C = DA.closure_cols(R)
                    Y = DSA.rung_extras(R, X, C)
                    K = ASA.rung_kernel_extras(R, X, C, Y)
                P = rung_rho_extras(R, K)
                mz = R["mz"]
                _k1, _k2, K12c, _a = cd_cols(mz["xp"], mz["wp"],
                                             mz["yn"], R["i1"],
                                             R["i2"], mz["Nw"])
                dcd = max(abs(_k1 / K["K11"] - 1.0),
                          abs(_k2 / K["K22"] - 1.0),
                          abs(K12c / K["K12"] - 1.0))
                cdd = (K12c, dcd)
            cd_fit[kz] = cdd
            if R["margin"] <= 0:
                neg_rows.append(kz)
                if reduced:
                    ext5_excl.append(kz)
            if reduced:
                t_ext5 += time.time() - t_r
            print("    %-5d %-5d %-5d %-5d | %.4e %.4e %.4e | "
                  "%.4e %.4e %.7f | %8.4f %+.1e | %.1e"
                  % (kz, R["z"], R["Sm"], R["Nw"], R["margin"],
                     R["rdet"], P["LR"], K["kap"], P["rhoK"],
                     P["omr"], P["Q"], P["cdc"] - 1.0, cdd[1]),
                  flush=True)
            if kz == MAIN_KZ:
                RT[kz], PT[kz], KT[kz] = R, P, K
                YT[kz], CT[kz] = Y, C
            else:
                rs, ps, ks = slim352(R, P, dict(
                    K11=K["K11"], K22=K["K22"], K12=K["K12"],
                    kap=K["kap"], vp1=K["vp1"], vp2=K["vp2"]))
                RT[kz], PT[kz], KT[kz] = rs, ps, ks
                if not reduced:
                    YT[kz] = {k: Y[k] for k in
                              ("rho0", "y0", "rho_hi", "dev_split",
                               "dev_cpc")}
                    CT[kz] = {k: C[k] for k in
                              ("bridge", "dev_id", "dev_rdef")}
        excl = list(neg_rows)
        ok_cen = (len(core_kzs) == 42
                  and all(EXT3_NW_MIN <= RT[k]["Nw"]
                          <= EXT3_NW_MAX for k in ext3_kzs)
                  and all(EXT4_NW_MIN <= RT[k]["Nw"]
                          <= EXT4_NW_MAX for k in ext4_kzs)
                  and all(RT[k]["Nw"] == h for k, h in
                          zip(ext5_kzs, ext5_h)))
        check("G31-ladder-census", ok_cen
              and not [k for k in neg_rows if k not in ext5_kzs],
              "42 core + 15 r286 extension + 12 EXT3 (N_w %d..%d) "
              "+ 6 EXT4 (N_w %d..%d) + 6 EXT5 (N_w == h: %s -- "
              "THE DEEPEST L*-WINDOWS EVER MEASURED, 1.8x the "
              "EXT4 record); f64 margins: non-EXT5 all positive, "
              "EXT5 margins %s (sealed contingency exclusions: "
              "%s); EXT5 block within the %.0f s budget: %s"
              % (EXT3_NW_MIN, EXT3_NW_MAX, EXT4_NW_MIN,
                 EXT4_NW_MAX,
                 str([RT[k]["Nw"] for k in ext5_kzs]),
                 str(["%.2e" % RT[k]["margin"]
                      for k in ext5_kzs]),
                 str(ext5_excl) if ext5_excl else "none",
                 EXT5_BUDGET_S,
                 "YES" if t_ext5 <= EXT5_BUDGET_S else
                 "NO (contingency documented)"))
        all_kz = (core_kzs + ext_kzs + ext3_kzs + ext4_kzs
                  + [k for k in ext5_kzs if k not in ext5_excl])
        kz75 = core_kzs + ext_kzs + ext3_kzs + ext4_kzs
        kz57 = core_kzs + ext_kzs
        max_id1 = max(PT[k]["id1"] for k in all_kz)
        max_id2 = max(PT[k]["id2"] for k in all_kz)
        max_id3 = max(PT[k]["id3"] for k in all_kz)
        cd_sample_max = max(cd_fit[k][1] for k in CD_KZ)
        cd_mid_max = max(cd_fit[k][1] for k in all_kz
                         if RT[k]["Nw"] <= CD_MID_NW)
        cd_deep = [cd_fit[k][1] for k in ext5_kzs
                   if np.isfinite(cd_fit[k][1])]
        cd_deep_max = max(cd_deep) if cd_deep else 0.0
        cd_nonfin = [k for k in ext5_kzs
                     if not np.isfinite(cd_fit[k][1])]
        ok_id = (max_id1 <= CSQ_ID_BAR and max_id2 <= RID_ABS
                 and max_id3 <= ADD_SPLIT_BAR
                 and cd_sample_max <= CD_BAR
                 and cd_mid_max <= CD_BAR_MID
                 and cd_deep_max <= CD_BAR_DEEP
                 and not cd_nonfin
                 and all(RT[k]["det_dev"] <= DET_ID_BAR
                         for k in all_kz)
                 and all(YT[k]["dev_split"] <= SPLIT_BAR
                         and YT[k]["dev_cpc"] <= CPC_ID_BAR
                         for k in kz75)
                 and all(CT[k]["dev_id"] <= ID_BAR
                         and CT[k]["dev_rdef"] <= RDEF_BAR
                         for k in kz75))
        check("G32-ladder-identities", ok_id,
              "IDENTITIES on all %d rows: (i) c^2 == rho_K d1 d2 "
              "max %.1e (bar %.0e); (ii) r_det == 1 - rho_K d1 "
              "d2/pq max %.1e abs (bar %.0e); (iii) additive "
              "split max %.1e (bar %.0e); r342 det ward + r348 "
              "split/bookkeeping + r347 one-line wards re-gated "
              "on the 75; CD SECOND INSTRUMENT everywhere: r350 "
              "sample max %.1e (bar %.0e), all N_w <= %d max "
              "%.1e (bar %.0e), EXT5 max %.1e (bar %.0e, "
              "nonfinite: %s) -- K_N at the pair atoms is "
              "recursion-computable on EVERY measured depth "
              "incl. N_w 5690"
              % (len(all_kz), max_id1, CSQ_ID_BAR, max_id2,
                 RID_ABS, max_id3, ADD_SPLIT_BAR, cd_sample_max,
                 CD_BAR, CD_MID_NW, cd_mid_max, CD_BAR_MID,
                 cd_deep_max, CD_BAR_DEEP,
                 str(cd_nonfin) if cd_nonfin else "none"))

        def med(vals):
            return float(np.median(np.asarray(vals, float)))

        fit_kz = [k for k in kz57 if k not in excl]
        med_rho0 = med([YT[k]["rho0"] for k in fit_kz])
        med_br = med([CT[k]["bridge"] for k in fit_kz])
        ok_coh = (abs(med_rho0 - MED_ANCH["rho0"]) <= 0.01
                  and abs(med_br - MED_ANCH["bridge"]) <= 5e-3
                  and all(abs(KT[k]["kap"]
                              / SAMPLE_ANCH[k]["kap"] - 1.0)
                          <= 1e-3
                          and abs(PT[k]["rhoK"]
                                  / SAMPLE_ANCH[k]["rhoK"] - 1.0)
                          <= 1e-3
                          and abs(PT[k]["LR"]
                                  / SAMPLE_ANCH[k]["LR"] - 1.0)
                          <= 1e-3
                          and abs(PT[k]["Q"]
                                  / SAMPLE_ANCH[k]["Q"] - 1.0)
                          <= 1e-3
                          for k in SAMPLE_ANCH))
        check("G33-cohort-anchors", ok_coh,
              "LEG 0 COHORT ANCHORS: median rho_0 %.4f (r348 "
              "%.3f), median bridge %.4f (r343 %.4f); the scoped "
              "sample kap/rhoK/LR/Q (kz44/56/130) all bit-near "
              "-- Leg 0 closed"
              % (med_rho0, MED_ANCH["rho0"], med_br,
                 MED_ANCH["bridge"]))

    # ---------------- S4 twin
    section("S4  TWIN WARD")
    if smoke:
        check("G40-twin", True, "SMOKE: skipped")
        mzT = None
    else:
        uu9c, mm9c = TR.base_comb(9)
        mzD = TR.build_world(9, uu9c, mm9c)
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
        t1_, t2_ = PX.pair_select(mzT["yn"])
        d1T, d2T, cT = PX.pair_block(BT, t1_, t2_)
        pT, qT, _rT = PX.det_reserve(d1T, d2T, cT)
        rkT, sT, lrT = rho_corr_cols(d1T, d2T, cT, pT, qT)
        v1T = float(mzT["vn"][t1_])
        v2T = float(mzT["vn"][t2_])
        K11T, K22T, K12T, kapT = ASA.kernel_cols(d1T, d2T, cT,
                                                 v1T, v2T)
        QT = rel2_column(K12T, K11T, K22T)
        devT = dict(kap=abs(kapT / K9["kap"] - 1.0),
                    rhoK=abs(rkT / P9["rhoK"] - 1.0),
                    LR=abs(lrT / P9["LR"] - 1.0),
                    Q=abs(QT / P9["Q"] - 1.0))
        ok_twin = ok_dose0 and all(v <= TWIN_BAR
                                   for v in devT.values())
        check("G40-twin", ok_twin,
              "RATIONAL TWIN at tol %.0e (dose-zero identity "
              "BITWISE %s): new-column devs kap %.1e, rhoK %.1e, "
              "LR %.1e, Q %.1e (bar %.0e) -- the correlation "
              "coordinates are twin-stable"
              % (TWIN_TOL, ok_dose0, devT["kap"], devT["rhoK"],
                 devT["LR"], devT["Q"], TWIN_BAR))

    # ---------------- S5 fits + adjudications
    section("S5  LEG A/B/C/D -- SEALED FITS + THE RHO_R "
            "DECOMPOSITION + SECOND INSTRUMENT + SEPARATION")
    if smoke:
        for g in ("G50-fit-anchors", "G51-homogeneity",
                  "G52-legA-decomposition", "G53-rhoK-law",
                  "G54-gk12-second-instrument", "G55-balance",
                  "G56-separation"):
            check(g, True, "SMOKE: skipped")
        laws = {}
        verdict_bits = {}
    else:
        verdict_bits = {}
        lnN57 = np.log(np.array([RT[k]["Nw"] for k in fit_kz],
                                float))
        getters = {
            "margin": lambda k: RT[k]["margin"],
            "c": lambda k: abs(RT[k]["c"]),
            "csq": lambda k: RT[k]["c"] * RT[k]["c"],
            "p": lambda k: RT[k]["p"],
            "q": lambda k: RT[k]["q"],
            "pq": lambda k: RT[k]["p"] * RT[k]["q"],
            "rdet": lambda k: RT[k]["rdet"],
            "LR": lambda k: PT[k]["LR"],
            "kap": lambda k: abs(KT[k]["kap"]),
            "rhoK": lambda k: PT[k]["rhoK"],
            "omr": lambda k: PT[k]["omr"],
            "K11": lambda k: KT[k]["K11"],
            "K22": lambda k: KT[k]["K22"],
            "K12": lambda k: abs(KT[k]["K12"]),
            "K12cd": lambda k: abs(cd_fit[k][0]),
            "vp1": lambda k: KT[k]["vp1"],
            "vp2": lambda k: KT[k]["vp2"],
            "Q": lambda k: PT[k]["Q"],
            "y0": lambda k: abs(YT[k]["y0"]),
            "rhi": lambda k: abs(YT[k]["rho_hi"]),
        }
        deep75 = [k for k in ext3_kzs + ext4_kzs]
        deep_all = deep75 + [k for k in ext5_kzs
                             if k not in ext5_excl]
        laws = {}
        for nm, get in getters.items():
            e3p = [(math.log(RT[k]["Nw"]), math.log(get(k)))
                   for k in ext3_kzs]
            e4p = [(math.log(RT[k]["Nw"]), math.log(get(k)))
                   for k in ext4_kzs]
            laws[nm] = DA.decay_law(lnN57,
                                    np.log([get(k)
                                            for k in fit_kz]),
                                    e3p, e4p)
            if nm not in ("y0", "rhi"):
                # sealed contingency: only finite-positive EXT5
                # values enter the pure-test band
                e5p = [(math.log(RT[k]["Nw"]), math.log(get(k)))
                       for k in ext5_kzs if k not in ext5_excl
                       and np.isfinite(get(k)) and get(k) > 0]
                d5 = DA.decay_law(lnN57,
                                  np.log([get(k)
                                          for k in fit_kz]),
                                  [], e5p)
                laws[nm]["e5_in"] = d5["e4_in"]
                laws[nm]["e5_low"] = d5["e4_low"]
        ok_fit = (all(abs(laws[nm]["slope"] - FIT_ANCH[nm])
                      <= FIT_ANCH_TOL for nm in FIT_ANCH)
                  and all(abs(laws[nm]["curv"] - CURV_ANCH[nm])
                          <= CURV_ANCH_TOL for nm in CURV_ANCH))
        check("G50-fit-anchors", ok_fit,
              "LEG 0 FIT ANCHORS on the 57 (slope | record): "
              "margin %.3f | %.3f, c %.3f | %.3f, p %.3f | %.3f, "
              "q %.3f | %.3f, rdet %.3f | %.3f, kap %.3f | %.3f, "
              "K11 %+.3f | %+.3f, K22 %+.3f | %+.3f, K12 %+.3f | "
              "%+.3f, y0 %.3f | %.3f, rhi %.3f | %.3f (tol "
              "%.2f); CURV ANCHORS margin %+.3f | %+.3f, c %+.3f "
              "| %+.3f, rdet %+.3f | %+.3f, K12 %+.3f | %+.3f "
              "(tol %.2f); THE NEW SLOPES: rhoK %.4f, 1-rhoK "
              "%+.5f, LR %.3f (curv %+.3f), csq %.4f, pq %.4f, "
              "Q %+.4f, K12cd %+.4f"
              % (laws["margin"]["slope"], FIT_ANCH["margin"],
                 laws["c"]["slope"], FIT_ANCH["c"],
                 laws["p"]["slope"], FIT_ANCH["p"],
                 laws["q"]["slope"], FIT_ANCH["q"],
                 laws["rdet"]["slope"], FIT_ANCH["rdet"],
                 laws["kap"]["slope"], FIT_ANCH["kap"],
                 laws["K11"]["slope"], FIT_ANCH["K11"],
                 laws["K22"]["slope"], FIT_ANCH["K22"],
                 laws["K12"]["slope"], FIT_ANCH["K12"],
                 laws["y0"]["slope"], FIT_ANCH["y0"],
                 laws["rhi"]["slope"], FIT_ANCH["rhi"],
                 FIT_ANCH_TOL, laws["margin"]["curv"],
                 CURV_ANCH["margin"], laws["c"]["curv"],
                 CURV_ANCH["c"], laws["rdet"]["curv"],
                 CURV_ANCH["rdet"], laws["K12"]["curv"],
                 CURV_ANCH["K12"], CURV_ANCH_TOL,
                 laws["rhoK"]["slope"], laws["omr"]["slope"],
                 laws["LR"]["slope"], laws["LR"]["curv"],
                 laws["csq"]["slope"], laws["pq"]["slope"],
                 laws["Q"]["slope"], laws["K12cd"]["slope"]))
        hom1 = abs(laws["rhoK"]["slope"]
                   - 2.0 * laws["kap"]["slope"])
        hom2 = abs(laws["csq"]["slope"] - 2.0 * laws["c"]["slope"])
        check("G51-homogeneity", hom1 <= HOM_BAR
              and hom2 <= HOM_BAR,
              "EXACT INSTRUMENT GATES (Theil-Sen is homogeneous): "
              "|s_rhoK - 2 s_kap| = %.1e, |s_csq - 2 s_c| = %.1e "
              "(bar %.0e) -- the squared columns inherit the "
              "laws with doubled exponent AND doubled curvature "
              "(rhoK curv %+.3f == 2 x kap curv %+.3f), disclosed"
              % (hom1, hom2, HOM_BAR, laws["rhoK"]["curv"],
                 laws["kap"]["curv"]))
        # ---- Leg A adjudication
        lead_dev = abs(laws["csq"]["slope"] - laws["pq"]["slope"])
        co, rr, rmsD, rmsK, rmsd, _pD, _pK = fine_structure(
            lnN57, np.log([getters["pq"](k) for k in fit_kz]),
            np.log([getters["csq"](k) for k in fit_kz]), A_LEAD)
        lr_dev = abs(laws["LR"]["slope"] - laws["rdet"]["slope"])
        decor_exp = -laws["omr"]["slope"]
        decor_carrier = (decor_exp >= DECOR_MIN
                         and abs(decor_exp
                                 - (-laws["rdet"]["slope"]))
                         <= DECOR_MATCH)
        ga_ok = (lead_dev <= LEAD_CANCEL_BAR and co >= FS_CORR_MIN
                 and rr <= FS_RMSR_MAX and lr_dev <= LR_MATCH_BAR)
        verdict_bits["legA"] = dict(lead=lead_dev, corr=co,
                                    rmsr=rr, rmsD=rmsD, rmsK=rmsK,
                                    rmsd=rmsd, lr_dev=lr_dev,
                                    decor=decor_exp,
                                    decor_carrier=decor_carrier,
                                    ok=ga_ok)
        check("G52-legA-decomposition", lead_dev <= LEAD_CANCEL_BAR
              and lr_dev <= LR_MATCH_BAR,
              "LEG A: (A-lead) |s_csq - s_pq| = %.4f <= %.2f -- "
              "the leading laws CANCEL (the BK3 image): rho_r is "
              "a SECOND-ORDER object, not composable from the "
              "candidate laws; (A-fine) ONE-OBJECT TEST at A_LEAD "
              "17/12: corr(phi_D, phi_K) = %.6f (clause >= %.2f "
              "=> %s), rms ratio %.4f (clause <= %.1f => %s; "
              "rms_D %.4f / rms_K %.4f / rms_diff %.4f nats -- "
              "the two fine structures are %s); (A-LR) |s_LR - "
              "s_rdet| = %.4f <= %.2f, LR curv %+.3f (the "
              "weight-free normalization carries the same curved "
              "law); (A-decor) slope(1 - rho_K) = %+.5f => "
              "decay exponent %.5f: %s"
              % (lead_dev, LEAD_CANCEL_BAR, co, FS_CORR_MIN,
                 "FIRES" if co >= FS_CORR_MIN else "fails", rr,
                 FS_RMSR_MAX,
                 "FIRES" if rr <= FS_RMSR_MAX else "fails",
                 rmsD, rmsK, rmsd,
                 "ONE SHARED WANDER" if (co >= FS_CORR_MIN
                                         and rr <= FS_RMSR_MAX)
                 else "NOT identified", lr_dev, LR_MATCH_BAR,
                 laws["LR"]["curv"], laws["omr"]["slope"],
                 decor_exp,
                 "DECOR_CARRIER (the naming hypothesis holds)"
                 if decor_carrier else
                 "DECOR_REFUTED -- the kernel DEcorrelates, the "
                 "carrier is the saturation of c^2/pq"))
        # ---- rhoK law adjudication
        kap_clean = (abs(laws["kap"]["curv"]) <= DEC_CURV_BAR
                     and laws["kap"]["e3_in"] >= DEC_EXT3_MIN
                     and laws["kap"]["e4_low"] <= DEC_EXT4_LOW)
        a_kap = -laws["kap"]["slope"]
        kap_hits = [cc for cc in CAND_KAP
                    if abs(a_kap - cc) <= CAND_BAR]
        a_rhoK = -laws["rhoK"]["slope"]
        rhoK_hits = [cc for cc in CAND_RHOK
                     if abs(a_rhoK - cc) <= RHOK_BAR]
        rhoK_law = kap_clean and bool(kap_hits)
        verdict_bits["rhoK"] = dict(law=rhoK_law, a_kap=a_kap,
                                    kap_hits=kap_hits,
                                    a_rhoK=a_rhoK,
                                    rhoK_hits=rhoK_hits,
                                    clean=kap_clean)
        check("G53-rhoK-law", True,
              "THE RHO_K LAW (adjudicated on the kappa "
              "normalization, sealed): a_kap = %.4f, clauses %s "
              "(curv %+.3f, EXT3 %d/12 low %d, EXT4 %d/6 low "
              "%d), candidate hits %s of %s (bar %.2f -- every "
              "ambiguity printed); the weight-free correlation "
              "inherits a_rhoK = 2 a_kap = %.4f, candidate image "
              "%s of %s (doubled bar %.1f), doubled curv %+.3f "
              "%s 0.35 disclosed => %s"
              % (a_kap, "CLEAN" if kap_clean else "DIRTY",
                 laws["kap"]["curv"], laws["kap"]["e3_in"],
                 laws["kap"]["e3_low"], laws["kap"]["e4_in"],
                 laws["kap"]["e4_low"], str(kap_hits),
                 str(CAND_KAP), CAND_BAR, a_rhoK, str(rhoK_hits),
                 str(CAND_RHOK), RHOK_BAR, laws["rhoK"]["curv"],
                 ">" if abs(laws["rhoK"]["curv"]) > 0.35
                 else "<=",
                 "RHOK_LAW_FOUND" if rhoK_law else "RHOK_CENSUS"))
        # ---- Leg B: second instrument + REL2 + explanation
        cd2_dev = abs(laws["K12cd"]["slope"]
                      - laws["K12"]["slope"])
        recon_max = max(abs(PT[k]["cdc"] - 1.0) for k in fit_kz)
        c_clean = (abs(laws["c"]["curv"]) <= DEC_CURV_BAR
                   and laws["c"]["e3_in"] >= DEC_EXT3_MIN
                   and laws["c"]["e4_low"] <= DEC_EXT4_LOW)
        arb_kz = [k for k in all_kz]
        lnN_all = np.log(np.array([RT[k]["Nw"] for k in arb_kz],
                                  float))
        fitm = [k in set(fit_kz) for k in arb_kz]
        cohorts = [
            ("core42", [i for i, k in enumerate(arb_kz)
                        if k in set(core_kzs)]),
            ("ext15", [i for i, k in enumerate(arb_kz)
                       if k in set(ext_kzs)]),
            ("ext3", [i for i, k in enumerate(arb_kz)
                      if k in set(ext3_kzs)]),
            ("ext4", [i for i, k in enumerate(arb_kz)
                      if k in set(ext4_kzs)]),
            ("ext5", [i for i, k in enumerate(arb_kz)
                      if k in set(ext5_kzs)]),
        ]
        flatQ = GR.curvflat_protocol(
            lnN_all, np.log([PT[k]["Q"] for k in arb_kz]), fitm,
            [(nm, ix) for (nm, ix) in cohorts if ix])
        curv_book = laws["c"]["curv"] - 0.5 * (
            laws["vp1"]["curv"] + laws["vp2"]["curv"])
        gk12_expl = (recon_max <= RECON_BAR and c_clean
                     and kap_clean)
        verdict_bits["gk12"] = dict(
            expl=gk12_expl, recon=recon_max, c_clean=c_clean,
            cd2=cd2_dev, flatQ=flatQ, curv_book=curv_book)
        check("G54-gk12-second-instrument",
              cd2_dev <= CD2_FIT_BAR and recon_max <= RECON_BAR,
              "LEG B: (B-i) SECOND INSTRUMENT: the CD-refit K12 "
              "law == the Gram-route law (|s_K12cd - s_K12| = "
              "%.1e <= %.0e) -- the r350 dirtiness (curv %+.3f, "
              "EXT3 %d/12) is a STRUCTURE effect, not a "
              "measurement/route effect; (B-ii) REL2-equivalent "
              "flat column Q = K12/(K11 K22)^(1/4): protocol %s "
              "(CH1 %d out / %d hard, max dev %.2f dec; slope "
              "%+.4f CI [%+.2f, %+.2f]; cohort drift %.3f%s) -- "
              "%s; (B-iii) EXPLANATION: pointwise reconstruction "
              "max |K12 sqrt(vp1 vp2)/c - 1| = %.2e (bar %.0e); "
              "c clauses %s (curv %+.3f, EXT3 %d/12, EXT4 low "
              "%d); curvature bookkeeping curv(K12) %+.3f vs "
              "curv(c) - (curv(vp1) + curv(vp2))/2 = %+.3f "
              "(dev %.4f, Theil-Sen non-additivity census) => %s"
              % (cd2_dev, CD2_FIT_BAR, laws["K12"]["curv"],
                 laws["K12"]["e3_in"],
                 "PASSES" if flatQ["ok"] else "FAILS",
                 flatQ["n_out"], flatQ["hard"], flatQ["max_dev"],
                 flatQ["slope"], flatQ["qlo"], flatQ["qhi"],
                 flatQ["drift"],
                 " MONOTONE" if flatQ["mono"] else "",
                 "REL2 flat-protocol clean" if flatQ["ok"] else
                 "REL2 stays census (the r350 dirty-clause "
                 "reading in the flat frame)",
                 recon_max, RECON_BAR,
                 "CLEAN" if c_clean else "DIRTY",
                 laws["c"]["curv"], laws["c"]["e3_in"],
                 laws["c"]["e4_low"], laws["K12"]["curv"],
                 curv_book,
                 abs(laws["K12"]["curv"] - curv_book),
                 "GK12_EXPLAINED (the dirty column factorizes "
                 "into the CLEAN c law over the closed-form "
                 "dictionary weights)" if gk12_expl
                 else "GK12_CENSUS"))
        # ---- Leg D: balance re-gate
        alpha_meas = -laws["margin"]["slope"]
        rho_r = -laws["rdet"]["slope"]
        a_ppq = None
        ppq_col = [RT[k]["p"] + RT[k]["q"] for k in fit_kz]
        ft_ppq = LM.ts_fit(lnN57, np.log(ppq_col))
        a_ppq = -float(ft_ppq[1])
        alpha_comp = (-laws["p"]["slope"]) \
            + (-laws["q"]["slope"]) + rho_r - a_ppq
        dev_comp = abs(alpha_comp - alpha_meas)
        alpha_cand = 0.75 + 2.0 / 3.0 + rho_r - a_ppq
        dev_cand = abs(alpha_cand - alpha_meas)
        verdict_bits["bal"] = dict(alpha=alpha_meas, rho_r=rho_r,
                                   comp=alpha_comp, dev=dev_comp,
                                   cand=alpha_cand,
                                   dev_cand=dev_cand)
        check("G55-balance", dev_comp <= COMP_BAR,
              "LEG D THE TOTAL BALANCE: alpha == a_p + a_q + "
              "rho_r - a_(p+q) = %.3f + %.3f + %.3f - %.3f = "
              "%.3f vs alpha_meas %.3f (dev %.3f, bar %.1f); the "
              "candidate image 3/4 + 2/3 + rho_r - a_(p+q) = "
              "%.3f (dev %.3f); THE CHAIN TYPED: weights "
              "WOERTERBUCH, deficits CANDIDATE-LAW (unresolved, "
              "Leg C), pinning SATZ-grade (r350, not re-run), "
              "rho_r = THE ONE SECOND-ORDER OBJECT (Leg A: the "
              "shared-wander difference)"
              % (-laws["p"]["slope"], -laws["q"]["slope"], rho_r,
                 a_ppq, alpha_comp, alpha_meas, dev_comp,
                 COMP_BAR, alpha_cand, dev_cand))
        # ---- Leg C: separation
        sep_out = {}
        for nm, (cA, cB), col, dset in (
                ("a_p", SEP_P, "p", deep_all),
                ("a_q", SEP_Q, "q", deep_all),
                ("d0", SEP_D0, "y0", deep75)):
            ft = LM.ts_fit(lnN57, np.log([getters[col](k)
                                          for k in fit_kz]))
            piv = float(np.median(lnN57))
            ypiv = float(ft[0]) + float(ft[1]) * piv
            lnD = [math.log(RT[k]["Nw"]) for k in dset]
            logv = [math.log(getters[col](k)) for k in dset]
            nA, nB, gap, mad = sep_adjudicate(lnD, logv, piv,
                                              ypiv, cA, cB)
            n_need = int(math.ceil(SEP_FRAC * len(dset)))
            resolved = (max(nA, nB) >= n_need
                        and gap >= SEP_GAP_FACTOR * mad)
            req = sep_required_depth(mad, abs(cA - cB), piv)
            sep_out[nm] = dict(nA=nA, nB=nB, gap=gap, mad=mad,
                               resolved=resolved,
                               winner=(cA if nA >= nB else cB),
                               req_log10=req / math.log(10.0),
                               n=len(dset))
        verdict_bits["sep"] = sep_out
        check("G56-separation", True,
              "LEG C THE CANDIDATE SEPARATION (sealed: closer "
              ">= %d/6 of the deep rows AND gap >= %.1f x MAD): "
              "%s -- required depths (log10 N*): %s; the honest "
              "deliverable: the ladder-depth arithmetic"
              % (int(round(SEP_FRAC * 6)), SEP_GAP_FACTOR,
                 "; ".join("%s (%.4g vs %.4g): closer %d/%d vs "
                           "%d/%d, gap %.4f dec, MAD %.4f => %s"
                           % (nm, pr[0], pr[1],
                              sep_out[nm]["nA"], sep_out[nm]["n"],
                              sep_out[nm]["nB"], sep_out[nm]["n"],
                              sep_out[nm]["gap"],
                              sep_out[nm]["mad"],
                              ("RESOLVED -> %.4g"
                               % sep_out[nm]["winner"])
                              if sep_out[nm]["resolved"]
                              else "UNRESOLVED")
                           for nm, pr in (("a_p", SEP_P),
                                          ("a_q", SEP_Q),
                                          ("d0", SEP_D0))),
                 str({nm: round(sep_out[nm]["req_log10"], 1)
                      for nm in sep_out})))

    # ---------------- S6 worlds
    section("S6  LEG E -- THE WORLD CENSUS (RHO_K COLUMNS)")
    if smoke:
        for g in ("G70-controls", "G71-worlds"):
            check(g, True, "SMOKE: skipped")
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
        check("G70-controls", ok_ctrl,
              "EPST + SCR + SMOOTH + HL2 built verbatim through "
              "the r278/r280 channel at THEIR own N_w: minC == "
              "flips %s + HL2 %d; DIR/ABS from the r330 combs"
              % (str(CTRL_FLIPS), HL2_FLIP))
        WORLDS["MAIN"] = FC.world_from_mz("MAIN", mz9)
        WORLDS["TWIN"] = FC.world_from_mz("TWIN", mzT)
        cen = {}
        order = ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH", "HL2",
                 "DIR", "ABS")
        for wn in order:
            Wd = WORLDS[wn]
            E_w = Wd["B"] @ Wd["B"].T
            lam_rw, _rho32w, _cw = DA.mirror_world_row(E_w,
                                                       Wd["yn"])
            i1w, i2w = PX.pair_select(Wd["yn"])
            d1w, d2w, cw2 = PX.pair_block(Wd["B"], i1w, i2w)
            pw, qw, rdw = PX.det_reserve(d1w, d2w, cw2)
            with np.errstate(all="ignore"):
                rkw = cw2 * cw2 / (d1w * d2w)
                sw = cw2 * cw2 / (pw * qw)
            ki = None
            ncf = 0
            if wn in ("MAIN", "TWIN", "EPST", "SCR", "SMOOTH",
                      "HL2"):
                ki, _loc, _nint, _kaps, ncf = \
                    FC.interval_census(Wd)
            cen[wn] = dict(lam=Wd["lam"], lam_rest=lam_rw,
                           rhoK=rkw, omr=1.0 - rkw, s=sw,
                           rdet=rdw, kint=ki, ncf=ncf)
            info("%s: S_- %d, lambda %.6g, lambda_rest %.6g, "
                 "rho_K %.4g, 1 - rho_K %.4g, s %.4g, r_det "
                 "%+.4g%s"
                 % (wn, len(Wd["yn"]), Wd["lam"], lam_rw, rkw,
                    1.0 - rkw, sw, rdw,
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
                   and sum(cen[wn]["ncf"] for wn in cen
                           if cen[wn]["ncf"]) == 0)
        dead_names = ("EPST", "SCR", "SMOOTH", "HL2", "DIR",
                      "ABS")
        rk_live = [cen[wn]["rhoK"] for wn in ("MAIN", "TWIN")]
        rk_dead = [cen[wn]["rhoK"] for wn in dead_names]
        rk_separates = (max(rk_live) < min(rk_dead)
                        or min(rk_live) > max(rk_dead))
        sign_sep = all(cen[wn]["rdet"] < 0 for wn in dead_names) \
            and all(cen[wn]["rdet"] > 0
                    for wn in ("MAIN", "TWIN"))
        world_txt = ("rho_K census: live %s vs dead %s => the "
                     "DECORRELATION %s (census, no bar was "
                     "sealed); the SIGN of r_det separates %s "
                     "(dead pair blocks cross 1, r342 typing)"
                     % (str(["%.3g" % v for v in rk_live]),
                        str({wn: "%.3g" % cen[wn]["rhoK"]
                             for wn in dead_names}),
                        "SEPARATES" if rk_separates
                        else "DOES NOT SEPARATE",
                        "6/6 dead vs 2/2 live" if sign_sep
                        else "INCOMPLETELY"))
        check("G71-worlds", lr_sep and ok_kint,
              "WORLD LEDGER: lambda_rest >= 1 on dead 4/4 and < "
              "1 on live 2/2; kappa_int EPST %.6g / SCR %.4g / "
              "SMOOTH %.4g / HL2 %.6g == records at %.0f%%, live "
              "%.6f; %s"
              % (cen["EPST"]["kint"], cen["SCR"]["kint"],
                 cen["SMOOTH"]["kint"], cen["HL2"]["kint"],
                 100 * KINT_REC_TOL, cen["MAIN"]["kint"],
                 world_txt))

    # ---------------- S8 must-fails
    section("S8  MUST-FAILS")
    m1w = mutant_rho_wrongnorm(R9["d1"], R9["d2"], R9["c"],
                               R9["p"], R9["q"])
    expr_m1 = 1.0 - m1w * R9["d1"] * R9["d2"] \
        / (R9["p"] * R9["q"])
    dev_m1 = abs(expr_m1 / R9["rdet"] - 1.0)
    check("G80-m1-wrong-normalization", dev_m1 >= M1_BAR
          and ok_fr,
          "m1 THE WRONG CORRELATION NORMALIZATION (c^2/pq "
          "instead of c^2/(d1 d2)): identity (ii) breaks by "
          "%.1e rel at w9 (>= %.1f) and by 2/69 == 0.0290 "
          "EXACTLY on the Fractions toy -- the diagonal "
          "normalization is load-bearing, exactly CAUGHT"
          % (dev_m1, M1_BAR))
    mut2 = mutant_cand_posthoc([0.5812, 0.58, 0.579])
    all_cands = set(CAND_KAP) | set(CAND_RHOK) | set(SEP_P) \
        | set(SEP_Q) | set(SEP_D0)
    check("G81-m2-cand-posthoc", bool(hits_m2)
          and all(abs(mut2 - cc) >= MUT_MIN for cc in all_cands),
          "m2 CANDIDATES PICKED AFTER SIGHT: AST-FLAGGED (%s) "
          "and the toy posthoc candidate %.4f is in NO sealed "
          "list -- protocol-CAUGHT (the lists are frozen module "
          "constants under the two-commit protocol)"
          % (hits_m2[0] if hits_m2 else "MISS", mut2))
    mut3 = mutant_sepbar_posthoc(0.21)
    check("G82-m3-sepbar-posthoc", bool(hits_m3)
          and abs(mut3 - SEP_GAP_FACTOR) >= MUT_MIN,
          "m3 THE SEPARATION BAR AFTER SIGHT: AST-FLAGGED (%s) "
          "and the toy value %.3f differs from the sealed "
          "SEP_GAP_FACTOR %.1f -- protocol-CAUGHT"
          % (hits_m3[0] if hits_m3 else "MISS", mut3,
             SEP_GAP_FACTOR))
    aa9, bb9, h09, y19, y29 = cd_args9
    mut4a = mutant_cd_readback(K9["K12"])
    mut4b = mutant_cd_unnormalized(aa9, bb9, h09, y19, y29,
                                   R9["Nw"])
    dev_m4 = abs(mut4b / K9["K12"] - 1.0)
    check("G83-m4-cd-readback", bool(hits_m4)
          and abs(mut4a / K9["K12"] - 1.0) <= 1e-15
          and dev_m4 >= M4_BAR,
          "m4 THE SECOND INSTRUMENT READ BACK FROM THE FIRST: "
          "AST-FLAGGED (%s; the mutant returns the Gram value "
          "verbatim); the LOUD half: CD without the b_{N-1} "
          "prefactor breaks the ward by %.1e rel at w9 (>= %.1f) "
          "-- the recursion normalization is load-bearing, "
          "exactly CAUGHT"
          % (hits_m4[0] if hits_m4 else "MISS", dev_m4, M4_BAR))
    check("G84-m5-rel2-wrongpower", abs(dev_m5 - 0.85) <= 1e-9
          and dev_m5 >= M5_MIN,
          "m5 THE REL2 COLUMN WITH THE WRONG POWER (1/2 instead "
          "of 1/4): breaks the planted flat toy by %.3f == "
          "(g1 + g2)/4 EXACTLY (>= %.1f) -- the quarter power is "
          "load-bearing, exactly CAUGHT" % (dev_m5, M5_MIN))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism "
          "promoted, no certificate reading beyond the sealed "
          "census, no posthoc bar/band/family/prior/candidate "
          "move, no derived 5/7, NO RH claim, mincut unchanged; "
          "what the round adds: the rho_K identities with the "
          "one-object test, the CD second instrument on every "
          "row, the REL2 flat column, the EXT5 tranche and the "
          "separation instrument; r243..r351 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        audits_ok = okf and not hits and not ag_hits
        vA = verdict_bits["legA"]
        vK = verdict_bits["rhoK"]
        vG = verdict_bits["gk12"]
        vB = verdict_bits["bal"]
        vS = verdict_bits["sep"]
        ids_ok = (max_id1 <= CSQ_ID_BAR and max_id2 <= RID_ABS
                  and max_id3 <= ADD_SPLIT_BAR)
        if not audits_ok:
            main_v = "TARGET_LEAK(%s)" % "; ".join(hits + ag_hits)
        elif ids_ok and vA["ok"]:
            main_v = ("RHOR_REDUCED(one-object grade: the "
                      "identities (i)-(iii) exact on %d rows; "
                      "the leading laws cancel (|s_csq - s_pq| "
                      "= %.4f); the deficit and kernel fine "
                      "structures are ONE SHARED WANDER (corr "
                      "%.6f, rms ratio %.4f: rms_D %.4f / rms_K "
                      "%.4f vs rms_diff %.4f nats) whose "
                      "difference IS the log reserve; rho_r = "
                      "%.3f == -s_LR at %.4f -- THE TWO NAMED "
                      "RESTS ARE ONE OBJECT; honesty: a "
                      "reduction and identification, NOT a "
                      "source derivation of the exponent)"
                      % (len(all_kz), vA["lead"], vA["corr"],
                         vA["rmsr"], vA["rmsD"], vA["rmsK"],
                         vA["rmsd"], vB["rho_r"], vA["lr_dev"]))
        else:
            main_v = ("RHOR_IRREDUCIBLE(failed clauses: %s; THE "
                      "FINAL SPECIALIST PROFILE: a_p %.3f, a_q "
                      "%.3f, a_c %.3f, a_kap %.3f, g_K11 %+.3f, "
                      "g_K22 %+.3f, g_K12 %+.3f, rho_r %.3f, "
                      "LR curv %+.3f)"
                      % (str([nm for nm, okc in
                              (("ids", ids_ok),
                               ("lead", vA["lead"]
                                <= LEAD_CANCEL_BAR),
                               ("corr", vA["corr"]
                                >= FS_CORR_MIN),
                               ("rmsr", vA["rmsr"]
                                <= FS_RMSR_MAX),
                               ("lr", vA["lr_dev"]
                                <= LR_MATCH_BAR)) if not okc]),
                         -laws["p"]["slope"], -laws["q"]["slope"],
                         -laws["c"]["slope"], vK["a_kap"],
                         laws["K11"]["slope"],
                         laws["K22"]["slope"],
                         laws["K12"]["slope"], vB["rho_r"],
                         laws["LR"]["curv"]))
        res_loci = [nm for nm in vS if vS[nm]["resolved"]]
        parts = [
            main_v,
            (("RHOK_LAW_FOUND(a_kap %.4f hits %s, a_rhoK %.4f "
              "-> %s, ambiguity printed)"
              % (vK["a_kap"], str(vK["kap_hits"]), vK["a_rhoK"],
                 str(vK["rhoK_hits"]))) if vK["law"]
             else "RHOK_CENSUS(clauses %s, hits %s)"
             % ("clean" if vK["clean"] else "dirty",
                str(vK["kap_hits"]))),
            (("DECOR_CARRIER(exponent %.3f)" % vA["decor"])
             if vA["decor_carrier"] else
             "DECOR_REFUTED(slope(1 - rho_K) = %+.5f: the kernel "
             "DECORRELATES -- the naming hypothesis refuted "
             "cleanly, the carrier is the saturation of c^2/pq)"
             % laws["omr"]["slope"]),
            (("GK12_EXPLAINED(recon %.2e; c CLEAN; kap CLEAN; "
              "curvature bookkeeping dev %.4f; CD second "
              "instrument identical %.1e; REL2 protocol %s)"
              % (vG["recon"], abs(laws["K12"]["curv"]
                                  - vG["curv_book"]), vG["cd2"],
                 "PASSES" if vG["flatQ"]["ok"] else
                 "honest-negative")) if vG["expl"]
             else "GK12_CENSUS(recon %.2e, c %s, kap %s, REL2 %s)"
             % (vG["recon"],
                "clean" if vG["c_clean"] else "dirty",
                "clean" if vK["clean"] else "dirty",
                "ok" if vG["flatQ"]["ok"] else "fails")),
            (("CANDIDATES_RESOLVED(%s)"
              % ", ".join("%s -> %.4g" % (nm, vS[nm]["winner"])
                          for nm in res_loci)) if res_loci
             else "CANDIDATES_UNRESOLVED(required log10 N*: %s "
             "-- the ladder-depth arithmetic is the deliverable)"
             % str({nm: round(vS[nm]["req_log10"], 1)
                    for nm in vS})),
            # print-only amendment a1 (disclosed): every EXT5
            # out-row NAMED by side -- in/low of 6 (the r349
            # "every hole named" duty; no bar or rule moved)
            "EXT5_LEDGER(kz %s, N_w %s, margins %s, exclusions "
            "%s; bands (in/low of 6): p %d/%d, q %d/%d, c %d/%d, "
            "kap %d/%d, K12 %d/%d, margin %d/%d, rdet %d/%d, LR "
            "%d/%d, rhoK %d/%d -- out-rows NOT low are HIGH side)"
            % (str(tuple(ext5_kzs)),
               str([RT[k]["Nw"] for k in ext5_kzs]),
               str(["%.2e" % RT[k]["margin"] for k in ext5_kzs]),
               str(ext5_excl) if ext5_excl else "none",
               laws["p"]["e5_in"], laws["p"]["e5_low"],
               laws["q"]["e5_in"], laws["q"]["e5_low"],
               laws["c"]["e5_in"], laws["c"]["e5_low"],
               laws["kap"]["e5_in"], laws["kap"]["e5_low"],
               laws["K12"]["e5_in"], laws["K12"]["e5_low"],
               laws["margin"]["e5_in"], laws["margin"]["e5_low"],
               laws["rdet"]["e5_in"], laws["rdet"]["e5_low"],
               laws["LR"]["e5_in"], laws["LR"]["e5_low"],
               laws["rhoK"]["e5_in"], laws["rhoK"]["e5_low"]),
            "BALANCE_LEDGER(alpha %.3f == comp %.3f (dev %.3f); "
            "candidate image %.3f (dev %.3f); chain typed "
            "woerterbuch/candidate/satz/second-order)"
            % (vB["alpha"], vB["comp"], vB["dev"], vB["cand"],
               vB["dev_cand"]),
            "WORLD_LEDGER(%s)" % world_txt,
            "TWIN_LEDGER(kap %.1e, rhoK %.1e, LR %.1e, Q %.1e)"
            % (devT["kap"], devT["rhoK"], devT["LR"], devT["Q"]),
            "MUSTFAIL_LEDGER(m1-m5 + scopes)",
        ]
        verd = " + ".join(p for p in parts if p)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED anatomy + sealed adjudication of the "
          "rho_r source; NO L* claim, NO RH claim"
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
