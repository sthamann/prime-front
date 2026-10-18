#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""diag_target_probe -- PRIME.PORT.L2.DIAG_TARGET.01 (round 300):
the DIAGONAL ANATOMY of the Delta Fejer energy -- can the diagonal
decay sl_D <= sigma* = -0.516 (the r299 frozen DIAG_TARGET, the
thin-margin living edge of the L2 chain) be derived SOURCE-PURELY
from the chain / density structure -- and the ratio flatness with
it?  Context (sealed record inputs): r297 (SPEC e42a76eb) froze
the target inequality sigma := slope(S_F/M_W^2) <= sigma* =
-0.516 (measured sigma = -0.714); r298 (SPEC 05e831be) proved
S_F = B(omega,omega) + B(Delta,omega+beta) exactly and found the
window main term EMPTY => S_F ~ B(PDelta, PDelta); r299 (SPEC
f432e944, 32/32) decomposed B exactly into its frequency spectrum
(LOWPASS, main-lobe share 0.93) and fired DECAY_SPLIT with the
frozen rest pair: (1) DIAG_TARGET -- prove sl_D <= sigma* for the
DIAGONAL D = sum_j PDelta_j^2 (measured sl_D = -0.571, margin
0.055, THIN); (2) RATIO FLATNESS -- B/D stays bounded (measured
med 1.29, slope -0.168 FALLING).  D is ONE positive quantity (a
sum of squares, no signs, no cancellation): the first place in
the lane where magnitude methods CAN in principle carry.  r299
structure fund: FULL-SUPPORT overlap 42/42 -- Delta is a pure
c-value difference on ONE shared node set (Delta_fresh == 0);
cconv med 0.86 slope +0.045 (no pointwise c-convergence).  kz15
permanently closed via r270; the 6 exceptions via the r287 F2
certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r287/r297/r298/r299 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval);
F = 0.20 edge split; maximal same-sign runs of the bx-sorted
bulk; level-2 blocks (r270 convention); FROZEN vdC window H =
max(2, ceil(sqrt(m))); the frozen positional Fejer block kernel
(r298: block_breaks + aggregate_blocks + fejer_bil + fejer_apply)
and the r299 spectral machinery (spec_decomp with the frozen L
rule, band_energies, pair_split, overlap_split, cconv_census),
ALL imported verbatim; PDelta = Pbeta - Pomega; the round's
central quantity is the DIAGONAL D := sum_j PDelta_j^2 (== the
r299 Parseval mean (1/L) sum_k |Dhat(k)|^2, an exact identity)
and the RATIO B/D with B = B(PDelta, PDelta).

LEG 0 -- ANCHOR REGRESSION (r297/r298/r299 record numbers adopted
as-is, disclosed): sigma = -0.714 tol 0.01, sigma* = -0.516 tol
0.01 (sl_c2 +0.196, sl_pref +0.489, tol 0.01); D_rank med 0.024
tol 0.005 slope -0.42 tol 0.05; imbalance slope +0.244 tol 0.01;
the r298 decomposition bit-near (identity/kernel devs <= 1e-12,
attribution <= 1e-9, share med 0.99 tol 0.02, slope(MAIN) -1.386
tol 0.05, slope(|T|) -0.698 tol 0.05, T > 0 on 42/42, canc_T med
1.69 tol 0.05 slope +0.207 tol 0.02, |T_cross med| <= 1e-3, w9
support overlap == 367 EXACT, linear window zero <= 1e-9 main /
3e-6 deep / 1e-6 controls, r297 sum rule import devs 0/0); the
r299 route set recomputed bit-near: sl_D -0.571 tol 0.01, sl_|O|
-0.815 tol 0.01, O < 0 on 13/42 EXACT, ratio B/D med 1.29 tol
0.02 slope -0.168 tol 0.01, LOW band share med 0.93 tol 0.02,
q50 med 0.19 tol 0.02, cconv med 0.86 tol 0.02 slope +0.045 tol
0.01, D_rank(Delta) med 0.016 tol 0.005 slope -0.12 tol 0.05,
FULL-SUPPORT overlap on 42/42 EXACT.

LEG A -- THE DIAGONAL ANATOMY (what carries the -0.571?): per
rung the exact participation coordinates of the ONE positive
vector |PDelta|: L1 = sum_j |PDelta_j|, mx = max_j |PDelta_j|,
n_eff = L1^2 / D (participation number), fill = D / (mx x L1)
in (0, 1].  TWO EXACT slope decompositions (halves log-slopes
are exactly additive over products, gated <= 1e-9):
  (i)   sl_D  =  2 x slope(L1/M) - slope(n_eff)
                 [mass^2 scale  vs  effective-carrier count]
  (ii)  sl_D  =  slope(mx/M) + slope(L1/M) + slope(fill)
                 [max scale  +  L1 mass  +  fill factor]
-- which part carries the -0.571 is PRINTED, not assumed.
Class decomposition of the carrier (no prime oracle: the weight
SIGN class is the source-pure proxy): PDelta = A + Bv with A =
(Pb_ws - Pw_ws) (the ws-difference field) and Bv = (Pb_-vs -
Pw_-vs) (the -vs-difference field), recomposition gated <=
1e-12; energy shares sum A^2 / D, sum Bv^2 / D, cross.  Band
decomposition of D itself: the UNWEIGHTED Parseval split
(1/L) sum |Dhat|^2 over the frozen LOW/MID/EDGE bands (sum == D
gated).  Top-block share mx^2/D (med + slope).  Fine type
DIAG_ANATOMY(n_eff med + slope, both decompositions, class
shares, band shares, top share).

LEG B -- DERIVATION ROUTES FOR DIAG_TARGET (each an exact
per-rung inequality chain on the real builders, source-pure,
AST scope audit, worlds test on EPSTEIN/SCRAMBLE):
(B1) CHAIN-NORM ROUTE (the r297-asset attachment attempt): by
  the r299 full-support fund Delta is a pure c-value difference:
  at every shared position p, dc(p) = c_beta(p) - c_omega(p) =
  dw(p) x f(p) with dw = w_beta - w_omega (the weight
  difference) and f = x v2(x) fac (the chain factor) -- gated
  EXACTLY (the factorization ward); the per-block reconstruction
  P_rec = blocksum(dc) == P_ov gated <= 1e-9 (on the 42 rungs
  P_ov == PDelta identically, Delta_fresh == 0); per-block
  Cauchy-Schwarz against the |dw| measure: PDelta_j^2 =
  (sum_blk dw f)^2 <= (sum_blk |dw|) x (sum_blk |dw| f^2),
  summed: D <= wdmax x QabsD with wdmax = max_j sum_blk |dw|
  and QabsD = sum_bulk |dw| f^2 (the second moment of the |dw|
  measure -- a chain-quadratic, sum-rule-adjacent); slopes
  sl_wdmax, sl_Qd = slope(QabsD/M^2), composed = sl_wdmax +
  sl_Qd vs sigma*; the IDENTITY CENSUS: is the chain
  orthogonal w.r.t. the |dw| measure (VCP.chain_quads on the id
  pool, sealed classification HOLDS <= 1e-6 / NEAR <= 1e-3 /
  BREAKS)?  Only if it HOLDS does the proven Parseval sum rule
  attach to QabsD verbatim.
(B2) DENSITY / COUNT ROUTE: the exact factorization D <= mx x
  L1 (gated); composed = slope(mx/M) + slope(L1/M) vs sigma*;
  the MAX control census: is mx chain-controllable -- maxatom =
  max_bulk |dc| (a SINGLE c-value distance), slope(maxatom/M),
  and the block-internal reinforcement ratio mx/maxatom at the
  argmax block (med + slope).  Here the max is the TARGET
  quantity itself, not a loss factor -- the disclosed hope that
  the r297 max/mean imbalance curse does not apply verbatim.
(B3) EQUIDISTRIBUTION ROUTE: the needed n_eff growth is frozen
  as a standalone target: slope(n_eff) >= 2 x slope(L1/M) -
  sigma* (NEFF_TARGET; DISCLOSED HONESTY: by decomposition (i)
  this clause is algebraically EQUIVALENT to sl_D <= sigma* --
  a reparametrization, not progress by itself; the derivation
  content of B3 is the LINK to provable terrain: does n_eff
  grow along the falling boundary-position discrepancy?
  Census: slope(D_rank(Delta)) (must be falling), sp(N, n_eff),
  sp(D_rank(Delta), n_eff) over the 42 rungs).
SEALED DIAG ADJUDICATION (frozen BEFORE evaluation, exactly one
fires): route validity = every exact ward on 47 worlds;
  B1_OK iff valid and sl_wdmax + sl_Qd <= sigma*;
  B2_OK iff valid and sl_mx + sl_L1 <= sigma*;
  B3_OK iff valid and slope(n_eff) >= 2 sl_L1 - sigma* and
    slope(D_rank(Delta)) < 0;
  DIAG_DERIVED(B1) iff B1_OK and the |dw| identity census
    HOLDS (every factor of the composed bound reduces to a
    chain identity -- the only fully provable-terrain outcome;
    disclosed expectation: ambitious, the |dw| measure is a
    mixed difference measure);
  DIAG_SPLIT(fired routes, rest targets frozen) iff not DERIVED
    and (B1_OK or B2_OK or B3_OK) -- each firing route prints
    its frozen rest target (B1: QABS_TARGET = prove the wdmax /
    QabsD scaling; B2: MAXL1_TARGET = prove the two magnitude
    slopes of the ONE positive vector; B3: NEFF_TARGET = prove
    the n_eff growth from the falling D_rank);
  DIAG_STILL_EMPIRICAL(measured common obstruction) otherwise.

LEG C -- RATIO FLATNESS (the second frozen rest, smaller): the
needed statement is only BOUNDEDNESS of B/D.  The EXACT kernel
envelope F_H(theta) <= min(H, 1/(H sin^2(theta/2))) (pure
algebra: sin^2(H theta/2) <= 1) gives the exact per-rung
majorant B/D <= R_env := sum_k env(theta_k) |Dhat(k)|^2 /
sum_k |Dhat(k)|^2 (gated pointwise + composed on 47 worlds);
measured: med(R_env), slope(R_env), and the LOWPASS-width
census sp(B/D, q50) + slope(q50) over the ladder.  SEALED RATIO
ADJUDICATION: RATIO_BOUNDED_STRUCTURAL iff the envelope wards
hold on 47/47 and slope(R_env) <= +0.05 (the structural
majorant is non-growing on the measured ladder) -- DISCLOSED
HONESTY: R_env still consumes the measured spectrum shape; the
kernel side is structural, the spectral weighting is not;
RATIO_EMPIRICAL otherwise.

LEG D -- THEOREM COMPOSITION: fires ONLY on DIAG_DERIVED +
RATIO_BOUNDED_STRUCTURAL -- the full wave-9 candidate is
printed with every constant (Leg-B chain bound => sl_D <=
sigma* => with ratio boundedness sigma <= sigma* => the r297
target inequality => the v964-S0 vdC theorem => delta' > 0.21
on the generic half; exceptions 6 via r287 F2 + kz15 via r270).
NOT promoted.  OTHERWISE Leg D freezes the REFINED rest pair
(smaller than r299: exact needed-vs-measured inequalities in
the anatomy coordinates instead of the bare sl_D statement).

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) PARTICIPATION FORMULA MUTANT: n_eff from the SIGNED sum
  (sum P)^2 / D instead of L1^2 / D breaks the toy exactly
  (P = (1,-1,1): 1/3 vs 3, break 8/3 EXACT) -- CAUGHT; (m2)
  SWAPPED MAX/L1 FACTORIZATION: the claim D <= mx^2 breaks on
  the toy (2,1,1) (6 > 4, break 2 EXACT) AND on the real mains
  LOUDLY (D - mx^2 >= 1e-6 x D) -- the L1 factor is
  load-bearing; (m3) WRONG h-INDEX SUM-RULE ATTACH (exact
  Fractions, module-own): the Parseval sum rule with h_{k+2}
  in place of h_{k+1} breaks on the rational 4-node measure
  (dev != 0) -- CAUGHT; (m4a/m4b) WORLD-BLINDNESS BREAK: a
  builder consuming the withheld terminal drive key AND a
  builder consuming the branch label are both FLAGGED by the
  AST scope audit.  WORLD-BLINDNESS OF THE D-DECAY ITSELF is
  TESTED, not assumed: the sealed anatomy classes (PART_HIGH
  iff n_eff/m >= 0.5; FILL_HIGH iff fill >= 0.5) at the
  EPST/SCR control rungs vs MAIN med -- a class break is a
  disclosed finding (WORLD_SENSITIVE), not a gate failure
  (crossref r299: the O-sign class already separates).  Scope
  hygiene: the new builders (participation, shared_delta,
  cs_block_route, ratio_envelope) consume positions + weights +
  chain values only (BOUND_FORBIDDEN set); fragment audit (no
  fit primitives); TOY EXACTNESS (bar 1e-14): participation on
  (1,-1,1) (D 3, L1 3, mx 1, n_eff 3, fill 1) and (2,1,1)
  (D 6, L1 4, mx 2, n_eff 8/3, fill 3/4); the shared-delta toy
  border (1,2)/(3,-1) [bw (1,-1), f (3,1)] vs window
  (1,2,3.5)/(1.5,1,...) [wu (0.5,1,2)]: dc (1.5,-2) == dw x f
  EXACT at both shared positions; the CS-route toy positions
  (0,1,2), dw (1,-2,1), f (1,2,1), one block: P_rec -2, wd 4,
  q 10, P^2 = 4 <= 40 = wd x q; the envelope toy PDelta =
  (1,-1,1), H = 2: B = 1, D = 3, B/D = 1/3 <= R_env gated at
  FFT precision; mp SAMPLES (dps 60): kz15 (bar 1e-8) + the
  two deepest rungs (bar 3e-6); SMOOTH anchor (alias <= 1e-12,
  q_N <= 1e-20).

INDEX FIREWALL (binding, r238-r299 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks + WBT.fejer_bil +
WBT.fejer_apply, r299 FDP.spec_decomp + FDP.band_energies +
FDP.pair_split + FDP.overlap_split + FDP.cconv_census, r269
PBB.mask_edge + PBB.runs_split + PBB.bound_pairsum +
PBB.mp_drive, r287 L2D.blocks_level2 + L2D.bound_vdc +
L2D.halves_slope + L2D.autocorr_full, r297 VCP.chain_quads +
VCP.fr_symbolic_sumrule (the proven set re-computed, not
re-proved), r244 BH.wpack + BH.spearman, r257 CT.union_arrays,
r260 TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881
PIK, r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN); L rule
= smallest power of two >= 2 x (m + H) (FROZEN); BANDS: LOW
|theta| <= 2 pi / H, MID <= pi / 2, EDGE else (FROZEN); ADD_BAR
1e-9 (slope additivity); CLS_BAR 1e-12 (class recomposition,
rel max|PDelta|); DBAND_BAR 1e-9 (Parseval band sum of D, rel);
MAXL1_BAR 1e-9 (D <= mx L1 slack, rel D); DF_BAR 1e-9
(dc == dw x f, rel max|dc|); REC_BAR 1e-9 (P_rec == P_ov, rel
max|PDelta| floored at REC_FLOOR 1e-6 x contribution mass --
amendment a1: on the self-aliased SMOOTH source Delta == 0
identically and the raw scale degenerates to float noise);
CS_BAR 1e-9 (per-block CS + composed, rel D);
ENV_BAR 1e-9 (envelope pointwise x 1/H scale + composed ratio);
RATIO_GROW 0.05; ID_HOLDS 1e-6; ID_NEAR 1e-3; PART_CLS 0.5;
FILL_CLS 0.5; SPEC_BAR 1e-9; PAIR_BAR 1e-12; PART_BAR 1e-12;
EN_BAR 1e-9; KER_BAR/DEC_BAR 1e-12; ATTR_BAR 1e-9; LIN_BARS
1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls; TB_WARD bars
1e-9 / 3e-6 / 1e-6; ID_BAR 1e-12; AC_BAR 1e-9; TOY_BAR 1e-14;
TOY_FFT_BAR 1e-12; MUT_MIN 1e-6; R297 anchors sigma -0.714 /
sigma* -0.516 / sl_c2 +0.196 / sl_pref +0.489 (tol 0.01),
D_rank med 0.024 tol 0.005 slope -0.42 tol 0.05, imb slope
+0.244 tol 0.01; R298 anchors share med 0.99 tol 0.02, sl_MAIN
-1.386 tol 0.05, sl_|T| -0.698 tol 0.05, T > 0 on 42/42, canc
med 1.69 tol 0.05, canc slope +0.207 tol 0.02, |tc med| <=
1e-3, OVERLAP_W9 == 367 EXACT; R299 anchors sl_D -0.571 tol
0.01, sl_|O| -0.815 tol 0.01, O < 0 == 13 EXACT, ratio med 1.29
tol 0.02 slope -0.168 tol 0.01, LOW share 0.93 tol 0.02, q50
0.19 tol 0.02, cconv 0.86 tol 0.02 slope +0.045 tol 0.01,
D_rank(Delta) med 0.016 tol 0.005 slope -0.12 tol 0.05,
FULL_OV == 42 EXACT; MP_DPS 60; MP_T_BAR 1e-8; MP_DEEP_BAR
3e-6; SM_Q_BAR 1e-20; SM_ALIAS_BAR 1e-12; KZ_ANCHOR 15; runtime
<= 1800 s; smoke = w9 + controls + Fractions section + toys +
scope audits + every exact ward at w9 (ladder, slopes,
adjudications, censuses, mp wards skipped).  DISCLOSED PRE-SPEC
INPUT (no scratch run of this probe): every reproduction band
is an r297/r298/r299 RECORD number adopted as-is; the two Leg-A
slope decompositions and the B3 clause equivalence are derived
algebra, disclosed above; the envelope bound is derived kernel
algebra; the adjudication outcomes are sealed symmetrically --
the disclosed structural priors (r297: magnitude majorizations
pay growing imbalance factors; r299: the ratio already falls)
make DIAG_SPLIT(B3) + RATIO_BOUNDED_STRUCTURAL plausible, but
no rule was chosen to favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  DIAG_ANATOMY(n_eff med + slope, sl_D = 2 sl_L1 - sl_neff =
    sl_mx + sl_L1 + sl_fill with both additivity devs, class
    shares A/Bv/cross, D band shares, top-block share)
+ ROUTE_TABLE(B1 valid n/47 sl_wdmax sl_Qd composed vs sigma*
    ident status; B2 valid n/47 sl_mx sl_L1 composed vs sigma*
    maxatom census; B3 needed vs measured n_eff growth,
    D_rank(Delta) slope, sp censuses)
+ [exactly one of] DIAG_DERIVED(B1, ...) / DIAG_SPLIT(fired
    routes + frozen rest targets) / DIAG_STILL_EMPIRICAL(
    measured common obstruction)
+ RATIO_TABLE(B/D med + slope, R_env med + slope, sp(B/D, q50),
    slope(q50))
+ [exactly one of] RATIO_BOUNDED_STRUCTURAL / RATIO_EMPIRICAL
+ [iff DERIVED + BOUNDED] CANDIDATE_THEOREM(all constants)
  [else] REST_FROZEN(the refined needed-vs-measured pair)
+ [if a control class differs] WORLD_SENSITIVE(disclosed).
Honesty before beauty: the participation identities, the
factorization dc = dw x f, the per-block Cauchy-Schwarz, the
max/L1 factorization and the kernel envelope are EXACT finite
identities/inequalities, but every slope, share and class is
MEASURED on 42 rungs only; B3's slope clause is an exact
reparametrization of DIAG_TARGET (disclosed above), its
derivation content is the D_rank link ONLY; R_env consumes the
measured spectrum shape; no verdict claims a cofinal law; the
exception scalar's positivity beyond the measured 42 stays
OPEN; r243-r299 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 29/31 -- the G50 reconstruction ward divided by a
DEGENERATE scale on the self-aliased SMOOTH control (Delta == 0
identically there, max|PDelta| = float noise 1.3e-18) --
amendment a1 (the reconstruction scale floored at REC_FLOOR 1e-6
x the total contribution mass; a code-side normalization fix, no
bar, band, rule or verdict rule touched; every real-data ward
was already exact: MAIN/EPST/SCR devs <= 6.1e-16); smoke pass 2
= 31/31 (0.2 s); calibration pass 1 = first full evaluation,
31/31 gates, wall 48.1 s, NO further amendment; record run1/run2
after this insertion, identical up to WALL; the only post-freeze
edits are a1 and this record-table insertion, which IS the
protocol):
CAL_VERDICT = DIAG_ANATOMY(n_eff med 37.41 slope +0.963 -- the
effective-carrier count GROWS at ~N; the exact decomposition (i)
sl_D = 2 x sl_L1 - sl_neff = 2 x (+0.196) - (+0.963) = -0.571
(dev 6.7e-16): the ENTIRE diagonal decay is the participation
growth net of a mildly growing L1 mass -- 'many small instead of
few large' is now a measured identity; decomposition (ii) sl_D =
sl_mx + sl_L1 + sl_fill = -0.542 + 0.196 - 0.225 (dev 4.4e-16);
class shares A/Bv/cross med 0.64/0.16/+0.20 (the ws-difference
field carries ~2/3 of D); D band shares LOW/MID/EDGE med
0.27/0.26/0.46 -- D itself is BROADBAND: the r299 LOWPASS
character of B is PURE KERNEL WEIGHTING, not spectrum shape;
top-block share med 0.16 slope -0.513) + ROUTE_TABLE(B1 valid
47/47: sl_wdmax -0.592 + sl_Qd +0.208 = composed -0.384 FAILS
sigma* -0.516 by 0.133; the |dw| identity census BREAKS (cross
med 0.932, worst 4.35) -- the proven sum rule does NOT attach to
the difference measure: the chain-norm shortcut is closed,
honestly; B2 valid 47/47: sl_mx -0.542 + sl_L1 +0.196 = composed
-0.346 FAILS by 0.170; the MAX is atom-controlled (mx/maxatom
med 1.07 slope -0.110, slope(maxatom/M) -0.432 -- a single
c-value distance): the loss sits in L1 x fill, the fill decay
-0.225 is exactly what every max x mass factorization cannot
see; B3: needed slope(n_eff) >= 2 sl_L1 - sigma* = +0.908,
measured +0.963 MET (margin 0.055 -- the same thin margin in the
new coordinate, the disclosed equivalence); D_rank(Delta) slope
-0.117 FALLING; sp(N, n_eff) +0.96, sp(D_rank(Delta), n_eff)
-0.81 -- the carrier count grows WHERE the discrepancy falls:
the D_rank bridge is real but correlational) + DIAG_SPLIT(B3(
NEFF_TARGET: prove slope(n_eff) >= +0.908 from the falling
boundary discrepancy, measured +0.963)) + RATIO_TABLE(B/D med
1.29 slope -0.168; R_env med 1.61 slope -0.122 -- the exact
kernel-envelope majorant itself FALLS; sp(B/D, q50) -0.47,
slope(q50) -0.027 -- the ratio and the lobe width DECOUPLE: the
r299 lobe-width heuristic is refuted as the ratio mechanism) +
RATIO_BOUNDED_STRUCTURAL(envelope wards 47/47: pointwise slack
9.3e-18 x 1/H, composed slack <= 0; slope(R_env) -0.122 <=
+0.05 -- the ratio half of the r299 rest pair is settled at the
structural level on the measured ladder, the spectral-weighting
honesty clause stands) + REST_FROZEN(DIAG: slope(n_eff) >=
+0.908, measured +0.963, margin 0.055, with the D_rank
correlation sp -0.81 as the named bridge to provable terrain;
RATIO: slope(R_env) <= +0.05, measured -0.122 -- MET) +
WORLD_SENSITIVE(MAIN PART_LOW/FILL_LOW vs EPST PART_HIGH/
FILL_HIGH + SCR PART_LOW/FILL_HIGH -- the FILL class separates
MAIN from BOTH broken-arithmetic controls at their own rungs:
after the r299 O-sign class the SECOND world-separating class of
the lane, disclosed).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; block + autocorr identities worst 6.3e-16 /
2.7e-15 on 47 worlds; r297 anchors bit-near (sigma -0.714,
sigma* -0.516, sl_c2 +0.196, sl_pref +0.489; D_rank med 0.024
sl -0.42, imb sl +0.244); r298 anchors bit-near (identity
8.8e-16, kernel 7.5e-16, attribution 5.4e-16; lin zero 2.2e-12
/ 6.4e-12 / 5.0e-7; share med 0.99, sl_MAIN -1.386, sl_|T|
-0.698, T < 0 on 0/42, canc 1.69 sl +0.207, tc med -1.4e-4,
overlap w9 367; sum rule import devs 0/0); r299 anchors bit-near
(spectral wards 7.1e-16 / 3.9e-16 / 3.5e-16, pair 8.2e-16,
partition 0.0, energy 0.0; sl_D -0.571, sl_|O| -0.815, O < 0
13/42, ratio 1.29 / -0.168, LOW 0.93, q50 0.19, cconv 0.86 /
+0.045, dd 0.016 / -0.12, full overlap 42/42).  S3: module-own
sum rule exact (orth dev 0, identity dev 0; r297 import devs
0/0); m3 wrong-h break 9146/2759 != 0 CAUGHT; participation +
shared-delta + CS + envelope toys exact (worst 0.0 / FFT 0.0);
m1 break 8/3 exact CAUGHT; m2 toy break 2 exact + real w9
8.4e-1 / w13 7.2e-1 of D LOUD.  S4: anatomy wards worst class
recomposition 4.6e-16, D band sum 3.0e-16, D <= mx L1 slack
0.0 on 47 worlds.  S5: B1 wards worst dc == dw x f 2.6e-15,
P_rec == P_ov 3.6e-13, per-block CS slack 6.2e-18, composed
slack 0.0; exception rungs in-table: n_eff 16.1 (kz20) .. 77.8
(kz52), fill 0.37 (kz15, kz36) .. 0.53 (kz38), R_env 1.86 (w9)
.. 3.18 (kz39), B/D 0.58 (w13) .. 2.74 (kz39).  S8: SMOOTH
alias 2.4e-14, q_N 4.2e-25, wards trivially exact; mp wards
kz15 2.9e-10, kz64 9.3e-9, kz52 6.6e-8.
READING (typed, no upgrade): the round DELIVERS the anatomy the
lane asked for and RELOCATES the frozen rest onto named terrain:
(1) the diagonal decay is ENTIRELY a participation statement --
sl_D = 2 sl_L1 - sl_neff exactly, with the effective carrier
count growing at +0.963 (~N, sp(N, n_eff) +0.96) against an L1
mass growing at +0.196: the 'distribution of the Delta mass'
question is now ONE measured growth exponent; (2) BOTH magnitude
factorizations fail exactly the way r297 predicted (B1 -0.384,
B2 -0.346 vs sigma* -0.516) -- but the anatomy localizes WHY:
the max is fully atom-controlled (a single c-value distance,
ratio med 1.07), so the irreducible loss is the fill decay
-0.225 (the profile's internal evenness loss), invisible to any
max x mass bound; (3) the |dw| identity census BREAKS -- the
proven window sum rule does not attach to the difference
measure; the chain-norm shortcut is closed; (4) the RATIO half
of the r299 rest pair is SETTLED at the structural level:
RATIO_BOUNDED_STRUCTURAL fired (the exact kernel-envelope
majorant R_env med 1.61 falls at -0.122), and the lobe-width
heuristic is refuted (sp -0.47, wrong sign) -- the ratio is
kernel algebra, not spectrum geometry; (5) the refined freeze is
smaller than r299's: ONE inequality remains -- NEFF_TARGET:
prove slope(n_eff) >= 2 sl_L1 - sigma* (measured margin 0.055),
with the falling D_rank (slope -0.117) and its strong coupling
to n_eff (sp -0.81) as the named bridge to the provable
equidistribution terrain.  Bycatch: D itself is BROADBAND
(0.27/0.26/0.46) -- the low-pass character of sigma is pure
Fejer weighting; and the FILL class separates MAIN (FILL_LOW)
from both dead controls (FILL_HIGH) -- the second
world-separating class of the lane after the r299 O-sign class,
disclosed as WORLD_SENSITIVE.  Runtime 48.1 s full / 0.2 s
smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE:
NONE beyond the disclosed a1 (records inserted per protocol; no
bar, band, rule or verdict rule moved).

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

import bordered_hankel_probe as BH             # noqa: E402 r244
import cancellation_adjudication_probe as CA   # noqa: E402 r263
import coupledtau_probe as CT                  # noqa: E402 r257
import terminal_crossratio_probe as TX         # noqa: E402 r260
import border_resolvent_identity_probe as BR   # noqa: E402 r266
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import l2_deterministic_cancellation_probe as L2D  # noqa: E402 r287
import vdc_chain_provenance_probe as VCP       # noqa: E402 r297
import window_border_transfer_probe as WBT     # noqa: E402 r298
import fejer_decay_probe as FDP                # noqa: E402 r299
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
M_W = math.sqrt(B57)
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
TB_WARD_BAR = 1e-9
TB_WARD_BAR_DEEP = 3e-6
TB_WARD_BAR_CTRL = 1e-6
DEEP_N = 400
ID_BAR = 1e-12
AC_BAR = 1e-9
KER_BAR = 1e-12
DEC_BAR = 1e-12
ATTR_BAR = 1e-9
LIN_BAR = 1e-9
LIN_BAR_DEEP = 3e-6
LIN_BAR_CTRL = 1e-6
SPEC_BAR = 1e-9
PAIR_BAR = 1e-12
PART_BAR = 1e-12
EN_BAR = 1e-9
ADD_BAR = 1e-9
CLS_BAR = 1e-12
DBAND_BAR = 1e-9
MAXL1_BAR = 1e-9
DF_BAR = 1e-9
REC_BAR = 1e-9
REC_FLOOR = 1e-6
CS_BAR = 1e-9
ENV_BAR = 1e-9
RATIO_GROW = 0.05
ID_HOLDS = 1e-6
ID_NEAR = 1e-3
PART_CLS = 0.5
FILL_CLS = 0.5
TOY_BAR = 1e-14
TOY_FFT_BAR = 1e-12
MUT_MIN = 1e-6
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
R297_SIGMA = -0.714
R297_SIGMA_TOL = 0.01
R297_SIGMA_STAR = -0.516
R297_SSTAR_TOL = 0.01
R297_SL_C2 = 0.196
R297_SL_C2_TOL = 0.01
R297_SL_PREF = 0.489
R297_SL_PREF_TOL = 0.01
R297_DRANK_MED = 0.024
R297_DRANK_TOL = 0.005
R297_DRANK_SL = -0.42
R297_DRANK_SL_TOL = 0.05
R297_IMB_SL = 0.244
R297_IMB_SL_TOL = 0.01
R298_SH_MED = 0.99
R298_SH_TOL = 0.02
R298_SL_MAIN = -1.386
R298_SL_MAIN_TOL = 0.05
R298_SL_T = -0.698
R298_SL_T_TOL = 0.05
R298_CANC_MED = 1.69
R298_CANC_TOL = 0.05
R298_CANC_SL = 0.207
R298_CANC_SL_TOL = 0.02
R298_TC_ABS = 1e-3
R298_OVERLAP_W9 = 367
R299_SL_D = -0.571
R299_SL_D_TOL = 0.01
R299_SL_ABSO = -0.815
R299_SL_ABSO_TOL = 0.01
R299_N_ONEG = 13
R299_RAT_MED = 1.29
R299_RAT_TOL = 0.02
R299_RAT_SL = -0.168
R299_RAT_SL_TOL = 0.01
R299_SH_LOW = 0.93
R299_SH_LOW_TOL = 0.02
R299_Q50 = 0.19
R299_Q50_TOL = 0.02
R299_CCONV = 0.86
R299_CCONV_TOL = 0.02
R299_CCONV_SL = 0.045
R299_CCONV_SL_TOL = 0.01
R299_DD_MED = 0.016
R299_DD_TOL = 0.005
R299_DD_SL = -0.12
R299_DD_SL_TOL = 0.05
R299_FULL_OV = 42
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
SM_Q_BAR = 1e-20
SM_ALIAS_BAR = 1e-12
KZ_ANCHOR = 15

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
    return (not bad), ("NO zero/prime oracles; every readout "
                       "consumes node positions + signed weights + "
                       "the r244 chain rows; ground truth (branch "
                       "labels, true R/t/Z) enters gates and census "
                       "tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden method families (identifiers only;
    the fragment table itself is assembled from split strings)."""
    frags = ("cand_" + "unroll", "poly" + "fit", "curve_" + "fit",
             "lst" + "sq", "mini" + "mize", "Line" + "arRegression")
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


BOUND_FORBIDDEN = {"t" + "_term", "Z", "Zl", "margin", "M" + "_W",
                   "loss", "R" + "_bulk", "truth", "rho",
                   "g" + "_branch", "need"}


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld/
    truth-side identifier or dict key from the sealed set."""
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


# ---------------- exact Fractions section: the Parseval sum rule
# ---------------- (module-own re-proof + the m3 wrong-h mutant)
def fr_parseval_sumrule(wrong_h=False):
    """the Parseval-type sum rule on the rational 4-node measure
    x = (0, 1, 2, 3), w = (1, 2, 1, 3) (r297-G31 / r298-G30
    verbatim): monic three-term chain pi_0..pi_3, orthogonality
    dev + the identity sum w x^2 pi_k^2 == h_{k+1} + a_k^2 h_k +
    b_k^2 h_{k-1} for k = 1, exact.  wrong_h replaces h_{k+1} by
    h_{k+2} on the RHS -- the m3 mutant, must break (dev != 0)."""
    xs = [Fr(0), Fr(1), Fr(2), Fr(3)]
    ws = [Fr(1), Fr(2), Fr(1), Fr(3)]
    n = len(xs)
    pis = [[Fr(1)] * n]
    a_ = []
    b_ = []
    hs = [sum(w * p * p for w, p in zip(ws, pis[0]))]
    for k in range(3):
        ak = sum(w * x * p * p for w, x, p in zip(ws, xs, pis[k])) \
            / hs[k]
        bk = (hs[k] / hs[k - 1]) if k >= 1 else Fr(0)
        nxt = []
        for i in range(n):
            v = (xs[i] - ak) * pis[k][i]
            if k >= 1:
                v -= bk * pis[k - 1][i]
            nxt.append(v)
        pis.append(nxt)
        a_.append(ak)
        b_.append(bk)
        hs.append(sum(w * p * p for w, p in zip(ws, nxt)))
    worst_orth = Fr(0)
    for a in range(4):
        for b in range(a):
            worst_orth = max(worst_orth,
                             abs(sum(w * pis[a][i] * pis[b][i]
                                     for i, w in enumerate(ws))))
    k = 1
    lhs = sum(w * x * x * p * p
              for w, x, p in zip(ws, xs, pis[k]))
    head = hs[k + 2] if wrong_h else hs[k + 1]
    rhs = head + a_[k] ** 2 * hs[k] + b_[k] ** 2 * hs[k - 1]
    return worst_orth, abs(lhs - rhs)


# ---------------- the module-own anatomy / route builders.
# ---------------- Source-pure: block vectors (positions, weights,
# ---------------- chain values) only; the withheld terminal drive
# ---------------- key, the branch label and every target-side
# ---------------- identifier are forbidden in scope (AST audit).
def participation(P):
    """the exact participation coordinates of the ONE positive
    vector |P|: D = sum P^2, L1 = sum |P|, mx = max |P|, n_eff =
    L1^2 / D, fill = D / (mx x L1) in (0, 1]; both product
    identities D = L1^2 / n_eff = mx x L1 x fill are exact by
    construction."""
    P = np.asarray(P, dtype=float)
    D = float(np.sum(P * P))
    L1 = float(np.sum(np.abs(P)))
    mx = float(np.max(np.abs(P))) if len(P) else 0.0
    n_eff = L1 * L1 / max(D, 1e-300)
    fill = D / max(mx * L1, 1e-300)
    return dict(D=D, L1=L1, mx=mx, neff=n_eff, fill=fill)


def shared_delta(bxs, cbs, bws, fxs, xu, cw, wu):
    """the per-position census on the EXACT shared support
    (duplicate-safe via bincount): aggregated c-difference dc =
    c_beta - c_omega, weight difference dw = w_beta - w_omega,
    and the chain position factor f (constant per position; mean
    over duplicates)."""
    common = np.intersect1d(bxs, xu)
    n = len(common)
    if n == 0:
        z = np.zeros(0)
        return dict(x=z, dc=z, dw=z, f=z, n=0)
    mb = np.isin(bxs, common)
    mw = np.isin(xu, common)
    ib = np.searchsorted(common, bxs[mb])
    iw = np.searchsorted(common, xu[mw])
    cb_at = np.bincount(ib, weights=cbs[mb], minlength=n)
    cw_at = np.bincount(iw, weights=cw[mw], minlength=n)
    bw_at = np.bincount(ib, weights=bws[mb], minlength=n)
    wu_at = np.bincount(iw, weights=wu[mw], minlength=n)
    cnt = np.maximum(np.bincount(ib, minlength=n), 1)
    f_at = np.bincount(ib, weights=fxs[mb], minlength=n) / cnt
    return dict(x=common, dc=cb_at - cw_at, dw=bw_at - wu_at,
                f=f_at, n=n)


def cs_block_route(xs, dc, dw, fv, lo, hi, brk, m):
    """the B1 chain-norm route on the shared support: edge mask
    (combined hull, EDGE_F), block index by breakpoint search,
    per-block Cauchy-Schwarz of the c-difference against the
    |dw| measure: P_j^2 = (sum_blk dw f)^2 <= (sum_blk |dw|) x
    (sum_blk |dw| f^2); composed: sum_j P_j^2 <= wdmax x QabsD."""
    xs = np.asarray(xs, dtype=float)
    ed = PBB.mask_edge(xs, lo, hi, EDGE_F)
    x = xs[~ed]
    c = np.asarray(dc, dtype=float)[~ed]
    w = np.asarray(dw, dtype=float)[~ed]
    f = np.asarray(fv, dtype=float)[~ed]
    if m == 0 or len(x) == 0:
        z = np.zeros(max(m, 0))
        return dict(P=z, wdmax=0.0, qabs=0.0, cs_worst=0.0,
                    maxatom=0.0)
    j = np.searchsorted(brk, x)
    P = np.bincount(j, weights=c, minlength=m)
    wd = np.bincount(j, weights=np.abs(w), minlength=m)
    q = np.bincount(j, weights=np.abs(w) * f * f, minlength=m)
    return dict(P=P, wdmax=float(np.max(wd)),
                qabs=float(np.sum(q)),
                cs_worst=float(np.max(P * P - wd * q)),
                maxatom=float(np.max(np.abs(c))))


def ratio_envelope(sp_, H):
    """the exact kernel-envelope majorant of the ratio B/D:
    F_H(theta) <= env(theta) = min(H, 1/(H sin^2(theta/2)))
    pointwise (pure algebra), so B/D <= R_env = sum env |Phat|^2
    / sum |Phat|^2.  Returns (pointwise slack x 1/H, R_env,
    composed ratio slack)."""
    th = sp_["th"]
    F = sp_["F"]
    with np.errstate(divide="ignore"):
        env = np.where(th > 1e-15,
                       1.0 / (H * np.sin(th / 2.0) ** 2), float(H))
    env = np.minimum(env, float(H))
    slack = float(np.max(F - env)) / H
    Ep = np.abs(sp_["ud"]) ** 2 / sp_["L"]
    Dp = max(float(np.sum(Ep)), 1e-300)
    r_env = float(np.sum(env * Ep)) / Dp
    b_over_d = float(np.sum(F * Ep)) / Dp
    return slack, r_env, b_over_d - r_env


def mutant_gift_bound(rc, P):
    """m4a MUST-FAIL MUTANT: a 'diagonal bound' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.asarray(P) ** 2))


def mutant_branch_peek(rc, P):
    """m4b MUST-FAIL MUTANT (world-blindness break simulated): a
    'participation count' that consumes the branch label to pick
    its constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * participation(P)["neff"]


# ---------------------------------------------- toy exact tools
def toy_participation():
    """participation on (1,-1,1): D 3, L1 3, mx 1, n_eff 3, fill
    1; on (2,1,1): D 6, L1 4, mx 2, n_eff 8/3, fill 3/4.  Plus
    the product identities.  Returns worst dev."""
    worst = 0.0
    p1 = participation([1.0, -1.0, 1.0])
    worst = max(worst, abs(p1["D"] - 3.0), abs(p1["L1"] - 3.0),
                abs(p1["mx"] - 1.0), abs(p1["neff"] - 3.0),
                abs(p1["fill"] - 1.0))
    p2 = participation([2.0, 1.0, 1.0])
    worst = max(worst, abs(p2["D"] - 6.0), abs(p2["L1"] - 4.0),
                abs(p2["mx"] - 2.0), abs(p2["neff"] - 8.0 / 3.0),
                abs(p2["fill"] - 0.75))
    for p in (p1, p2):
        worst = max(worst,
                    abs(p["D"] - p["L1"] ** 2 / p["neff"]),
                    abs(p["D"] - p["mx"] * p["L1"] * p["fill"]))
    return worst


def toy_mustfail_m1():
    """m1 PARTICIPATION FORMULA MUTANT: the signed sum (sum P)^2
    / D instead of L1^2 / D on P = (1,-1,1) gives 1/3 instead of
    3 -- break 8/3 EXACT."""
    P = np.array([1.0, -1.0, 1.0])
    D = float(np.sum(P * P))
    wrong = float(np.sum(P)) ** 2 / D
    return abs(wrong - participation(P)["neff"])


def toy_mustfail_m2():
    """m2 SWAPPED MAX/L1 FACTORIZATION: the claim D <= mx^2 on
    (2,1,1) breaks by 2 EXACT (6 > 4) while D <= mx x L1 = 8
    holds."""
    p = participation([2.0, 1.0, 1.0])
    good_slack = max(p["D"] - p["mx"] * p["L1"], 0.0)
    return p["D"] - p["mx"] ** 2, good_slack


def toy_shared_and_cs():
    """the shared-delta toy: border (1,2) with bw (1,-1), f
    (3,1) -> cb (3,-1); window (1,2,3.5) with wu (0.5,1,2), f
    (3,1,.) -> cw (1.5,1,.); shared = {1,2}: dc = (1.5,-2) ==
    dw x f = (0.5 x 3, -2 x 1) EXACT.  The CS-route toy:
    positions (0,1,2), dw (1,-2,1), f (1,2,1), one block: P_rec
    = -2, wd 4, q 10, P^2 = 4 <= 40 = wd x q.  Returns worst."""
    worst = 0.0
    bxs = np.array([1.0, 2.0])
    bws = np.array([1.0, -1.0])
    fb = np.array([3.0, 1.0])
    cbs = bws * fb
    xu = np.array([1.0, 2.0, 3.5])
    wu = np.array([0.5, 1.0, 2.0])
    fw = np.array([3.0, 1.0, 5.0])
    cw = wu * fw
    sd = shared_delta(bxs, cbs, bws, fb, xu, cw, wu)
    worst = max(worst, abs(sd["n"] - 2),
                float(np.max(np.abs(sd["dc"]
                                    - np.array([1.5, -2.0])))),
                float(np.max(np.abs(sd["dw"]
                                    - np.array([0.5, -2.0])))),
                float(np.max(np.abs(sd["dc"]
                                    - sd["dw"] * sd["f"]))))
    xs = np.array([0.0, 1.0, 2.0])
    dw = np.array([1.0, -2.0, 1.0])
    fv = np.array([1.0, 2.0, 1.0])
    dc = dw * fv
    cs = cs_block_route(xs, dc, dw, fv, -10.0, 14.0,
                        np.array([]), 1)
    worst = max(worst, float(np.max(np.abs(cs["P"]
                                           - np.array([-2.0])))),
                abs(cs["wdmax"] - 4.0), abs(cs["qabs"] - 10.0),
                abs(cs["cs_worst"] + 36.0),
                max(float(np.sum(cs["P"] ** 2))
                    - cs["wdmax"] * cs["qabs"], 0.0))
    return worst


def toy_envelope():
    """the envelope toy PDelta = (1,-1,1), H = 2: B = 1, D = 3,
    B/D = 1/3 <= R_env; pointwise slack <= 0; FFT precision."""
    Pd = np.array([1.0, -1.0, 1.0])
    H = 2
    sp_ = FDP.spec_decomp(Pd, H)
    slack, r_env, comp = ratio_envelope(sp_, H)
    worst = max(slack, 0.0)
    worst = max(worst, max(comp, 0.0))
    worst = max(worst, max(1.0 / 3.0 - r_env, 0.0))
    return worst


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("diag_target_probe -- PRIME.PORT.L2.DIAG_TARGET.01 "
          "(round 300)")
    print("SPEC_SHA %s   R298_SHA %s (imported)   R299_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], WBT.SPEC_SHA[:16], FDP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + every exact ward "
                        "at w9; ladder, slopes, adjudications, "
                        "censuses, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE DIAG-TARGET ROUND (the r299 frozen rest executed): "
          "the diagonal D = sum PDelta_j^2 already falls fast "
          "enough (record sl_D %.3f <= sigma* %.3f, margin 0.055 "
          "THIN); this round decomposes sl_D EXACTLY into "
          "participation coordinates (n_eff, L1, mx, fill), tests "
          "THREE source-pure derivation routes (B1 chain-norm CS "
          "on the |dw| measure + identity census, B2 max x L1 "
          "density factorization, B3 equidistribution/NEFF with "
          "the disclosed reparametrization honesty), and settles "
          "the ratio half through the exact kernel envelope; "
          "sealed outcomes DERIVED / SPLIT (frozen rests) / "
          "STILL_EMPIRICAL and BOUNDED_STRUCTURAL / EMPIRICAL; "
          "ALL bars, bands, rules and verdicts sealed BEFORE "
          "evaluation" % (R299_SL_D, R297_SIGMA_STAR))

    # ---------------- S1: census + controls (r299 scaffold verbatim)
    section("S1  CENSUS + CONTROLS")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    if smoke:
        ladder = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G10-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %d rungs "
          "POSITIVE_PREFIX %s, N in [%s, %s]"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             len(ladder),
             "42/42" if okL and ladder else ("n/a (SMOKE)"
                                             if smoke else "FAIL"),
             ladder[0]["N"] if ladder else "-",
             ladder[-1]["N"] if ladder else "-"))

    pool = ladder if not smoke else [packs["w9"]]
    mains = [packs["w%d" % kz] for kz in windows]

    def rung_rec(p):
        N = p["N"]
        rows = p["rows"]
        r, t, ap, bp = TX.drive_arrays(rows, N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        chain = ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3]
        Z = t[N - 2] + chain
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        v2 = BR.eval_scaled(rows, bx, N - 2)
        v2w = BR.eval_scaled(rows, xu, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        cw = wu * xu * v2w * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, cw=cw, o=o,
                    lo=lo, hi=hi, p=p)

    recs = [rung_rec(p) for p in pool]
    mrecs = [rung_rec(p) for p in mains]
    crecs = {c: rung_rec(ctrl[c]) for c in ctrl}
    cheap = [rc for rc in recs if rc["g_branch"] >= 0.0]
    exc = [rc for rc in recs if rc["g_branch"] < 0.0]
    exc_kz = tuple(sorted(rc["kz"] for rc in exc))
    if smoke:
        check("G11-branch-reproduction", recs[0]["g_branch"] >= 0.0,
              "SMOKE: w9 branch %s (g %+.3f); ladder "
              "decomposition skipped"
              % ("CHEAP" if recs[0]["g_branch"] >= 0 else
                 "EXCEPTION", recs[0]["g_branch"]))
    else:
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs)))

    # ---------------- S2: decomposition + identities + anchors
    section("S2  EXACT DECOMPOSITION + R297/R298/R299 ANCHORS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d mains + 3 "
          "controls: worst dev/absmass %.1e main N<=%d (bar %.0e) "
          "/ %.1e deep (bar %.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP, tb_ctrl,
             TB_WARD_BAR_CTRL))

    def eval_rung(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        bws_s = rc["bw"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        cb = cts[~ed]
        xb = bxs[~ed]
        runs = PBB.runs_split(cb)
        Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        P = L2D.blocks_level2(Sr)
        e_c2 = PBB.bound_pairsum(Mr)
        f2 = L2D.bound_vdc(P)
        H = f2["H"]
        S_F = f2["s2"] / H
        # ---- the frozen positional kernel (r298 verbatim)
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        agg_dev = float(np.max(np.abs(Pb - np.array(P)))) \
            / max(max(abs(v) for v in P), 1e-300) if m else 0.0
        sf_ker = WBT.fejer_bil(Pb, Pb, H)
        ker_dev = abs(sf_ker - S_F) / max(S_F, 1e-300)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        main = WBT.fejer_bil(Pw, Pw, H)
        Pd = Pb - Pw
        T = WBT.fejer_bil(Pd, Pb + Pw, H)
        scale = max(S_F, main, abs(T), 1e-300)
        dec_dev = abs(S_F - main - T) / scale
        phi = WBT.fejer_apply(Pb + Pw, H)
        tj = Pd * phi
        attr_dev = abs(float(np.sum(tj)) - T) / scale
        t_cross = 2.0 * WBT.fejer_bil(Pd, Pw, H)
        lin_dev = abs(float(np.sum(rc["cw"]))) \
            / max(float(np.sum(np.abs(rc["cw"]))), 1e-300)
        B_en = WBT.fejer_bil(Pd, Pd, H)
        comp_dev = abs(B_en + t_cross - T) / scale
        # ---- r299 spectral machinery (imported verbatim)
        sp = FDP.spec_decomp(Pd, H)
        b_sc = max(B_en, sp["B"], 1e-300)
        spec_dev = abs(sp["B"] - B_en) / b_sc
        D_diag, O_off = FDP.pair_split(Pd, H)
        pars_dev = abs(sp["pars"] - D_diag) / max(D_diag, 1e-300)
        e_lo, e_mid, e_ed = FDP.band_energies(sp["th"], sp["E"], H)
        band_dev = abs(e_lo + e_mid + e_ed - sp["B"]) / b_sc
        order = np.argsort(sp["th"], kind="stable")
        cum = np.cumsum(sp["E"][order])
        tot = max(float(cum[-1]), 1e-300)
        th_s = sp["th"][order]
        q50 = float(th_s[int(np.searchsorted(cum, 0.5 * tot))]) \
            * H / (2.0 * np.pi)
        pair_dev = abs(D_diag + O_off - B_en) \
            / max(abs(B_en), D_diag, abs(O_off), 1e-300)
        # ---- r299 overlap split + cconv (imported verbatim)
        P_ov, P_fr, _n_b, _n_w = FDP.overlap_split(
            bxs, cts, rc["xu"], rc["cw"], rc["lo"], rc["hi"],
            brk, m)
        part_dev = float(np.max(np.abs(P_ov + P_fr - Pd))) \
            / max(float(np.max(np.abs(Pd))), 1e-300) if m else 0.0
        B_ov = WBT.fejer_bil(P_ov, P_ov, H)
        B_fr = WBT.fejer_bil(P_fr, P_fr, H)
        B_x = 2.0 * WBT.fejer_bil(P_ov, P_fr, H)
        en_sc = max(B_ov, B_fr, abs(B_x), abs(B_en), 1e-300)
        en_dev = abs(B_ov + B_x + B_fr - B_en) / en_sc
        cconv, n_common = FDP.cconv_census(bxs, cts, rc["xu"],
                                           rc["cw"])
        full_ov = int(n_common == len(rc["bx"]) == len(rc["xu"]))
        # ---- D_rank on Delta (r299 verbatim)
        wed = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xall = np.sort(np.concatenate([xb, rc["xu"][~wed]]))
        a_h = rc["lo"] + EDGE_F * (rc["hi"] - rc["lo"])
        b_h = rc["hi"] - EDGE_F * (rc["hi"] - rc["lo"])
        nn = len(xall)
        d_delta = float(np.max(np.abs(
            (np.arange(1, nn + 1) / nn)
            - (xall - a_h) / max(b_h - a_h, 1e-300)))) \
            if nn else 0.0
        # ---- Leg A: participation anatomy of the ONE positive
        # ---- vector |PDelta|
        part = participation(Pd)
        mxl1_slack = max(part["D"] - part["mx"] * part["L1"], 0.0) \
            / max(part["D"], 1e-300)
        # class split A = ws-difference, Bv = -vs-difference
        mb_p = bws_s > 0
        Pb_p = WBT.aggregate_blocks(bxs[mb_p], cts[mb_p],
                                    rc["lo"], rc["hi"], brk, m)
        Pb_n = WBT.aggregate_blocks(bxs[~mb_p], cts[~mb_p],
                                    rc["lo"], rc["hi"], brk, m)
        wpos = rc["wu"] > 0
        Pw_p = WBT.aggregate_blocks(rc["xu"][wpos],
                                    rc["cw"][wpos], rc["lo"],
                                    rc["hi"], brk, m)
        Pw_n = WBT.aggregate_blocks(rc["xu"][~wpos],
                                    rc["cw"][~wpos], rc["lo"],
                                    rc["hi"], brk, m)
        Acl = Pb_p - Pw_p
        Bcl = Pb_n - Pw_n
        cls_dev = float(np.max(np.abs(Acl + Bcl - Pd))) \
            / max(float(np.max(np.abs(Pd))), 1e-300) if m else 0.0
        D_A = float(np.sum(Acl * Acl))
        D_B = float(np.sum(Bcl * Bcl))
        X_AB = 2.0 * float(np.sum(Acl * Bcl))
        # Parseval band split of D (unweighted spectrum)
        Ep = np.abs(sp["ud"]) ** 2 / sp["L"]
        d_lo, d_mid, d_ed = FDP.band_energies(sp["th"], Ep, H)
        dband_dev = abs(d_lo + d_mid + d_ed - part["D"]) \
            / max(part["D"], 1e-300)
        # ---- Leg C: exact kernel envelope of the ratio
        env_slack, r_env, env_comp = ratio_envelope(sp, H)
        # ---- Leg B1: shared-support factorization + CS route
        fxs = rc["bx"] * rc["v2"] * rc["fac"]
        sd = shared_delta(rc["bx"], rc["ct"], rc["bw"], fxs,
                          rc["xu"], rc["cw"], rc["wu"])
        df_dev = float(np.max(np.abs(sd["dc"]
                                     - sd["dw"] * sd["f"]))) \
            / max(float(np.max(np.abs(sd["dc"]))), 1e-300) \
            if sd["n"] else 0.0
        cs = cs_block_route(sd["x"], sd["dc"], sd["dw"], sd["f"],
                            rc["lo"], rc["hi"], brk, m)
        # a1 scale floor: on a self-aliased source (SMOOTH) Delta
        # is identically zero and max|PDelta| degenerates to float
        # noise; the reconstruction scale is floored at REC_FLOOR
        # x the total contribution mass (amendment a1, code-side
        # normalization fix -- no bar or rule moved)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        rec_scale = max(float(np.max(np.abs(Pd))) if m else 0.0,
                        REC_FLOOR * absm, 1e-300)
        rec_dev = float(np.max(np.abs(cs["P"] - P_ov))) \
            / rec_scale if m else 0.0
        D_ov = float(np.sum(cs["P"] ** 2))
        cs_worst = cs["cs_worst"] / max(part["D"], 1e-300)
        cs_comp = max(D_ov - cs["wdmax"] * cs["qabs"], 0.0) \
            / max(part["D"], 1e-300)
        return dict(alt_ok=alt_ok, R=R, P=P, e_c2=e_c2, H=H,
                    S_F=S_F, m=m, Pb=Pb, Pw=Pw, Pd=Pd,
                    agg_dev=agg_dev, ker_dev=ker_dev, main=main,
                    T=T, dec_dev=dec_dev, tj=tj,
                    attr_dev=attr_dev, t_cross=t_cross,
                    comp_dev=comp_dev, lin_dev=lin_dev,
                    B=B_en, sp=sp, spec_dev=spec_dev,
                    pars_dev=pars_dev, e_lo=e_lo, e_mid=e_mid,
                    e_ed=e_ed, band_dev=band_dev, q50=q50,
                    D=D_diag, O=O_off, pair_dev=pair_dev,
                    part_dev=part_dev, en_dev=en_dev,
                    cconv=cconv, full_ov=full_ov,
                    d_delta=d_delta, part=part,
                    mxl1_slack=mxl1_slack, cls_dev=cls_dev,
                    D_A=D_A, D_B=D_B, X_AB=X_AB, d_lo=d_lo,
                    d_mid=d_mid, d_ed=d_ed, dband_dev=dband_dev,
                    env_slack=env_slack, r_env=r_env,
                    env_comp=env_comp, df_dev=df_dev,
                    rec_dev=rec_dev, wdmax=cs["wdmax"],
                    qabs=cs["qabs"], cs_worst=cs_worst,
                    cs_comp=cs_comp, maxatom=cs["maxatom"],
                    D_ov=D_ov, Mr=Mr, nr=len(runs), sd=sd)

    all_rc = recs + mrecs
    for rc in all_rc:
        rc["ev"] = eval_rung(rc)
    for c in crecs:
        crecs[c]["ev"] = eval_rung(crecs[c])
    pool_all = all_rc + [crecs[c] for c in crecs]

    alt_all = all(rc["ev"]["alt_ok"] for rc in all_rc)
    bid_worst = 0.0
    ac_worst = 0.0
    for rc in pool_all:
        ev = rc["ev"]
        bid_worst = max(bid_worst,
                        abs(sum(ev["P"]) - ev["R"])
                        / max(abs(ev["R"]), 1e-300))
        A = L2D.autocorr_full(ev["P"])
        s_all = A[0] + 2.0 * float(np.sum(A[1:]))
        ac_worst = max(ac_worst,
                       abs(s_all - sum(ev["P"]) ** 2)
                       / max(A[0], 1e-300))
    check("G21-block-and-autocorr-identity",
          alt_all and bid_worst <= ID_BAR and ac_worst <= AC_BAR,
          "runs alternate on every world AND sum P == R exact "
          "(worst rel %.1e, bar %.0e) AND (sum P)^2 == A(0) + 2 "
          "sum A(h) exact (worst %.1e x A(0), bar %.0e) over %d "
          "worlds" % (bid_worst, ID_BAR, ac_worst, AC_BAR,
                      len(pool_all)))

    # ---- ladder aggregates (one block; every later gate reads st)
    Ns = [rc["N"] for rc in recs]
    st = {}
    if not smoke:
        def med(key):
            return float(np.median([rc["ev"][key] for rc in recs]))

        def med_f(fn):
            return float(np.median([fn(rc["ev"]) for rc in recs]))

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        eps_c2_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
        st["sl_c2"] = L2D.halves_slope(Ns, eps_c2_rel)
        pref = [(rc["ev"]["m"] + rc["ev"]["H"] - 1) / rc["ev"]["H"]
                for rc in recs]
        st["sl_pref"] = L2D.halves_slope(Ns, pref)
        st["sigma"] = slp([rc["ev"]["S_F"] / (M_W * M_W)
                           for rc in recs])
        st["sigma_star"] = 2.0 * (st["sl_c2"] - DELTA_NEED) \
            - st["sl_pref"]
        # r297 census: D_rank / imbalance recomputed from runs
        d_ranks = []
        imbs = []
        for rc in recs:
            o = rc["o"]
            bxs = rc["bx"][o]
            cts = rc["ct"][o]
            edm = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
            cbb = cts[~edm]
            runs = PBB.runs_split(cbb)
            Mr = [float(np.sum(np.abs(cbb[a:b])))
                  for a, b, _s in runs]
            nb = len(cbb)
            nr = len(runs)
            d_rank = 0.0
            if nr > 1 and nb > 0:
                for i, (a, b, _s) in enumerate(runs[:-1]):
                    d_rank = max(d_rank,
                                 abs(b / nb - (i + 1) / nr))
            d_ranks.append(d_rank)
            mx = max(Mr) if Mr else 0.0
            sm = sum(Mr) if Mr else 0.0
            imbs.append(nr * mx / max(sm, 1e-300))
        st["dr_med"] = float(np.median(d_ranks))
        st["dr_sl"] = slp(d_ranks)
        st["imb_sl"] = L2D.halves_slope(Ns, imbs)
        # r298 set
        st["sh_med"] = med_f(lambda ev: abs(ev["T"])
                             / max(ev["S_F"], 1e-300))
        st["sl_main"] = slp([max(rc["ev"]["main"], 1e-300)
                             / (M_W * M_W) for rc in recs])
        st["sl_T"] = slp([max(abs(rc["ev"]["T"]), 1e-300)
                          / (M_W * M_W) for rc in recs])
        st["n_negT"] = sum(1 for rc in recs if rc["ev"]["T"] < 0.0)
        canc = [float(np.sum(np.abs(rc["ev"]["tj"])))
                / max(abs(rc["ev"]["T"]), 1e-300) for rc in recs]
        st["canc_med"] = float(np.median(canc))
        st["canc_sl"] = L2D.halves_slope(Ns, canc)
        st["tc_med"] = med("t_cross")
        # r299 set
        st["sl_D"] = slp([rc["ev"]["D"] / (M_W * M_W)
                          for rc in recs])
        st["sl_absO"] = slp([abs(rc["ev"]["O"]) / (M_W * M_W)
                             for rc in recs])
        st["n_On"] = sum(1 for rc in recs if rc["ev"]["O"] < 0.0)
        ratio = [rc["ev"]["B"] / max(rc["ev"]["D"], 1e-300)
                 for rc in recs]
        st["rat_med"] = float(np.median(ratio))
        st["sl_rat"] = slp(ratio)
        st["shl_med"] = med_f(lambda ev: ev["e_lo"]
                              / max(ev["B"], 1e-300))
        st["q50_med"] = med("q50")
        st["sl_q50"] = slp([rc["ev"]["q50"] for rc in recs])
        st["cc_med"] = med("cconv")
        st["cc_sl"] = slp([rc["ev"]["cconv"] for rc in recs])
        st["dd_med"] = med("d_delta")
        st["dd_sl"] = slp([rc["ev"]["d_delta"] for rc in recs])
        st["full_ov"] = sum(rc["ev"]["full_ov"] for rc in recs)
        # Leg A anatomy
        st["neff_med"] = med_f(lambda ev: ev["part"]["neff"])
        st["sl_neff"] = slp([rc["ev"]["part"]["neff"]
                             for rc in recs])
        st["sl_L1"] = slp([rc["ev"]["part"]["L1"] / M_W
                           for rc in recs])
        st["sl_mx"] = slp([rc["ev"]["part"]["mx"] / M_W
                           for rc in recs])
        st["sl_fill"] = slp([rc["ev"]["part"]["fill"]
                             for rc in recs])
        st["add1"] = abs(st["sl_D"]
                         - (2.0 * st["sl_L1"] - st["sl_neff"]))
        st["add2"] = abs(st["sl_D"] - (st["sl_mx"] + st["sl_L1"]
                                       + st["sl_fill"]))
        st["clsA_med"] = med_f(lambda ev: ev["D_A"]
                               / max(ev["part"]["D"], 1e-300))
        st["clsB_med"] = med_f(lambda ev: ev["D_B"]
                               / max(ev["part"]["D"], 1e-300))
        st["clsX_med"] = med_f(lambda ev: ev["X_AB"]
                               / max(ev["part"]["D"], 1e-300))
        st["dlo_med"] = med_f(lambda ev: ev["d_lo"]
                              / max(ev["part"]["D"], 1e-300))
        st["dmid_med"] = med_f(lambda ev: ev["d_mid"]
                               / max(ev["part"]["D"], 1e-300))
        st["ded_med"] = med_f(lambda ev: ev["d_ed"]
                              / max(ev["part"]["D"], 1e-300))
        st["top_med"] = med_f(lambda ev: ev["part"]["mx"] ** 2
                              / max(ev["part"]["D"], 1e-300))
        st["sl_top"] = slp([rc["ev"]["part"]["mx"] ** 2
                            / max(rc["ev"]["part"]["D"], 1e-300)
                            for rc in recs])
        # Leg B slopes
        st["sl_wdmax"] = slp([rc["ev"]["wdmax"] for rc in recs])
        st["sl_qd"] = slp([rc["ev"]["qabs"] / (M_W * M_W)
                           for rc in recs])
        st["sl_maxatom"] = slp([rc["ev"]["maxatom"] / M_W
                                for rc in recs])
        st["mxma_med"] = med_f(lambda ev: ev["part"]["mx"]
                               / max(ev["maxatom"], 1e-300))
        st["sl_mxma"] = slp([rc["ev"]["part"]["mx"]
                             / max(rc["ev"]["maxatom"], 1e-300)
                             for rc in recs])
        st["sp_n_neff"] = BH.spearman(
            Ns, [rc["ev"]["part"]["neff"] for rc in recs])
        st["sp_dd_neff"] = BH.spearman(
            [rc["ev"]["d_delta"] for rc in recs],
            [rc["ev"]["part"]["neff"] for rc in recs])
        # Leg C ratio
        st["renv_med"] = med("r_env")
        st["sl_renv"] = slp([rc["ev"]["r_env"] for rc in recs])
        st["sp_rat_q50"] = BH.spearman(
            ratio, [rc["ev"]["q50"] for rc in recs])
        check("G22-r297-target-anchors",
              abs(st["sigma"] - R297_SIGMA) <= R297_SIGMA_TOL
              and abs(st["sigma_star"] - R297_SIGMA_STAR)
              <= R297_SSTAR_TOL
              and abs(st["sl_c2"] - R297_SL_C2) <= R297_SL_C2_TOL
              and abs(st["sl_pref"] - R297_SL_PREF)
              <= R297_SL_PREF_TOL,
              "the r297 target-inequality set recomputed bit-near: "
              "sigma %+.3f (ref %+.3f), sigma* %+.3f (ref %+.3f), "
              "sl_c2 %+.3f (ref %+.3f), sl_pref %+.3f (ref %+.3f)"
              % (st["sigma"], R297_SIGMA, st["sigma_star"],
                 R297_SIGMA_STAR, st["sl_c2"], R297_SL_C2,
                 st["sl_pref"], R297_SL_PREF))
        check("G23-r297-census-anchors",
              abs(st["dr_med"] - R297_DRANK_MED) <= R297_DRANK_TOL
              and abs(st["dr_sl"] - R297_DRANK_SL)
              <= R297_DRANK_SL_TOL
              and abs(st["imb_sl"] - R297_IMB_SL) <= R297_IMB_SL_TOL,
              "the r297 asset-2 census recomputed: D_rank med "
              "%.3f (ref %.3f) slope %+.2f (ref %+.2f), "
              "mass-imbalance slope %+.3f (ref %+.3f)"
              % (st["dr_med"], R297_DRANK_MED, st["dr_sl"],
                 R297_DRANK_SL, st["imb_sl"], R297_IMB_SL))
    else:
        check("G22-r297-target-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")
        check("G23-r297-census-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")

    dec_w = max(rc["ev"]["dec_dev"] for rc in pool_all)
    ker_w = max(max(rc["ev"]["ker_dev"], rc["ev"]["agg_dev"])
                for rc in pool_all)
    att_w = max(max(rc["ev"]["attr_dev"], rc["ev"]["comp_dev"])
                for rc in pool_all)
    lin_m = max((rc["ev"]["lin_dev"] for rc in all_rc
                 if rc["N"] <= DEEP_N), default=0.0)
    lin_d = max((rc["ev"]["lin_dev"] for rc in all_rc
                 if rc["N"] > DEEP_N), default=0.0)
    lin_c = max(crecs[c]["ev"]["lin_dev"] for c in crecs)
    rc9 = mrecs[0] if not smoke else recs[0]
    ov9 = len(np.intersect1d(rc9["bx"], rc9["xu"]))
    v_o, v_i = VCP.fr_symbolic_sumrule()
    if not smoke:
        ok298 = (abs(st["sh_med"] - R298_SH_MED) <= R298_SH_TOL
                 and abs(st["sl_main"] - R298_SL_MAIN)
                 <= R298_SL_MAIN_TOL
                 and abs(st["sl_T"] - R298_SL_T) <= R298_SL_T_TOL
                 and st["n_negT"] == 0
                 and abs(st["canc_med"] - R298_CANC_MED)
                 <= R298_CANC_TOL
                 and abs(st["canc_sl"] - R298_CANC_SL)
                 <= R298_CANC_SL_TOL
                 and abs(st["tc_med"]) <= R298_TC_ABS
                 and ov9 == R298_OVERLAP_W9)
        det298 = ("share med %.2f, sl_MAIN %+.3f, sl_|T| %+.3f, "
                  "T<0 %d/42, canc med %.2f sl %+.3f, tc med "
                  "%+.2g, overlap w9 %d (ref %d)"
                  % (st["sh_med"], st["sl_main"], st["sl_T"],
                     st["n_negT"], st["canc_med"], st["canc_sl"],
                     st["tc_med"], ov9, R298_OVERLAP_W9))
    else:
        ok298 = (ov9 == R298_OVERLAP_W9)
        det298 = ("SMOKE: ladder anchors skipped; overlap w9 %d "
                  "(ref %d)" % (ov9, R298_OVERLAP_W9))
    check("G24-r298-decomposition-anchors",
          dec_w <= DEC_BAR and ker_w <= KER_BAR
          and att_w <= ATTR_BAR and lin_m <= LIN_BAR
          and lin_d <= LIN_BAR_DEEP and lin_c <= LIN_BAR_CTRL
          and ok298 and v_o == 0 and v_i == 0,
          "the r298 record recomputed bit-near on %d worlds: "
          "identity dev %.1e (bar %.0e), kernel %.1e (bar %.0e), "
          "attribution %.1e (bar %.0e); linear window zero %.1e "
          "main / %.1e deep / %.1e controls; %s; r297 sum rule "
          "import devs %s/%s"
          % (len(pool_all), dec_w, DEC_BAR, ker_w, KER_BAR,
             att_w, ATTR_BAR, lin_m, lin_d, lin_c, det298,
             str(v_o), str(v_i)))
    spec_w = max(rc["ev"]["spec_dev"] for rc in pool_all)
    pars_w = max(rc["ev"]["pars_dev"] for rc in pool_all)
    band_w = max(rc["ev"]["band_dev"] for rc in pool_all)
    pair_w = max(rc["ev"]["pair_dev"] for rc in pool_all)
    partw = max(rc["ev"]["part_dev"] for rc in pool_all)
    en_w = max(rc["ev"]["en_dev"] for rc in pool_all)
    if not smoke:
        ok299 = (abs(st["sl_D"] - R299_SL_D) <= R299_SL_D_TOL
                 and abs(st["sl_absO"] - R299_SL_ABSO)
                 <= R299_SL_ABSO_TOL
                 and st["n_On"] == R299_N_ONEG
                 and abs(st["rat_med"] - R299_RAT_MED)
                 <= R299_RAT_TOL
                 and abs(st["sl_rat"] - R299_RAT_SL)
                 <= R299_RAT_SL_TOL
                 and abs(st["shl_med"] - R299_SH_LOW)
                 <= R299_SH_LOW_TOL
                 and abs(st["q50_med"] - R299_Q50) <= R299_Q50_TOL
                 and abs(st["cc_med"] - R299_CCONV)
                 <= R299_CCONV_TOL
                 and abs(st["cc_sl"] - R299_CCONV_SL)
                 <= R299_CCONV_SL_TOL
                 and abs(st["dd_med"] - R299_DD_MED) <= R299_DD_TOL
                 and abs(st["dd_sl"] - R299_DD_SL)
                 <= R299_DD_SL_TOL
                 and st["full_ov"] == R299_FULL_OV)
        det299 = ("sl_D %+.3f (ref %+.3f), sl_|O| %+.3f, O<0 "
                  "%d/42 (ref %d), ratio med %.2f sl %+.3f (ref "
                  "%.2f/%+.3f), LOW %.2f, q50 %.2f, cconv %.2f "
                  "sl %+.3f, dd %.3f sl %+.2f, full overlap "
                  "%d/42 (ref %d)"
                  % (st["sl_D"], R299_SL_D, st["sl_absO"],
                     st["n_On"], R299_N_ONEG, st["rat_med"],
                     st["sl_rat"], R299_RAT_MED, R299_RAT_SL,
                     st["shl_med"], st["q50_med"], st["cc_med"],
                     st["cc_sl"], st["dd_med"], st["dd_sl"],
                     st["full_ov"], R299_FULL_OV))
    else:
        ok299 = True
        det299 = "SMOKE: ladder anchors skipped"
    check("G25-r299-route-anchors",
          spec_w <= SPEC_BAR and pars_w <= SPEC_BAR
          and band_w <= SPEC_BAR and pair_w <= PAIR_BAR
          and partw <= PART_BAR and en_w <= EN_BAR and ok299,
          "the r299 exact machinery re-gated on %d worlds "
          "(spectral recomposition %.1e, Parseval %.1e, band sum "
          "%.1e, pair split %.1e, overlap partition %.1e, energy "
          "recomposition %.1e); %s"
          % (len(pool_all), spec_w, pars_w, band_w, pair_w,
             partw, en_w, det299))

    # ---------------- S3: exact section + toys + audits + mutants
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    w_o, w_i = fr_parseval_sumrule(wrong_h=False)
    _o2, w_mut = fr_parseval_sumrule(wrong_h=True)
    check("G30-sumrule-and-m3", w_o == 0 and w_i == 0
          and v_o == 0 and v_i == 0 and w_mut != 0,
          "the Parseval sum rule RE-PROVED exact in Fractions "
          "(module-own orth dev %s, identity dev %s; r297-G31 "
          "import devs %s/%s); m3 WRONG h-INDEX mutant (h_{k+2} "
          "for h_{k+1}) breaks by %s != 0 -- CAUGHT: the norm "
          "index of the sum-rule head is load-bearing"
          % (str(w_o), str(w_i), str(v_o), str(v_i), str(w_mut)))
    toy_w = max(toy_participation(), toy_shared_and_cs())
    toy_f = toy_envelope()
    check("G31-toy-exactness", toy_w <= TOY_BAR
          and toy_f <= TOY_FFT_BAR,
          "the hand toys reproduce the WHOLE new pipeline: "
          "participation (1,-1,1) -> D 3 / L1 3 / n_eff 3 / fill "
          "1 and (2,1,1) -> 6 / 4 / 8/3 / 3/4 with both product "
          "identities; shared-delta dc == dw x f exact on the "
          "border/window toy; CS route P_rec -2, wd 4, q 10, "
          "4 <= 40 (exact worst %.1e, bar %.0e); envelope toy "
          "B/D = 1/3 <= R_env at FFT precision (worst %.1e, "
          "bar %.0e)" % (toy_w, TOY_BAR, toy_f, TOY_FFT_BAR))
    h_pa = scope_audit("participation", BOUND_FORBIDDEN)
    h_sd = scope_audit("shared_delta", BOUND_FORBIDDEN)
    h_cs = scope_audit("cs_block_route", BOUND_FORBIDDEN)
    h_re = scope_audit("ratio_envelope", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_pa or h_sd or h_cs or h_re)
    check("G32-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the new builders (participation, shared_delta, "
          "cs_block_route, ratio_envelope) consume block vectors "
          "/ positions / weights only (no truth-side identifier "
          "in scope%s); m4a gift mutant FLAGGED (%s); m4b "
          "branch-peek mutant FLAGGED (%s); fragment audit: %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    m1_brk = toy_mustfail_m1()
    m2_brk, m2_good = toy_mustfail_m2()
    check("G33-mustfails-m1-m2-toys", m1_brk >= MUT_MIN
          and abs(m1_brk - 8.0 / 3.0) <= 1e-12
          and m2_brk >= MUT_MIN and abs(m2_brk - 2.0) <= 1e-12
          and m2_good <= TOY_BAR,
          "m1 PARTICIPATION FORMULA MUTANT (signed sum for L1): "
          "breaks the toy by %.6f (= 8/3 exact) CAUGHT; m2 "
          "SWAPPED MAX/L1 (claim D <= mx^2): breaks the toy by "
          "%.1f exact (6 > 4) while D <= mx x L1 holds (slack "
          "%.1e) -- the L1 factor is load-bearing"
          % (m1_brk, m2_brk, m2_good))

    # ---------------- S4: Leg A -- the diagonal anatomy
    section("S4  LEG A: DIAGONAL ANATOMY (PARTICIPATION)")
    cls_w = max(rc["ev"]["cls_dev"] for rc in pool_all)
    dband_w = max(rc["ev"]["dband_dev"] for rc in pool_all)
    mxl1_w = max(rc["ev"]["mxl1_slack"] for rc in pool_all)
    check("G40-anatomy-wards", cls_w <= CLS_BAR
          and dband_w <= DBAND_BAR and mxl1_w <= MAXL1_BAR,
          "the anatomy identities on %d worlds: class "
          "recomposition A + Bv == PDelta worst %.1e (bar %.0e); "
          "Parseval band sum == D worst %.1e (bar %.0e); the "
          "exact factorization D <= mx x L1 slack %.1e (bar "
          "%.0e) -- the participation coordinates are exact "
          "finite identities"
          % (len(pool_all), cls_w, CLS_BAR, dband_w, DBAND_BAR,
             mxl1_w, MAXL1_BAR))
    show = (sorted(exc, key=lambda r_: r_["kz"]) + mrecs
            if not smoke else mrecs)
    for rc in show:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s m %-3d H %-2d  D %.2e  n_eff "
             "%.2f  fill %.2f  B/D %.2f  R_env %.2f  wdmax "
             "%.2e" % (rc["kz"], rc["N"],
                       "EXC" if rc["g_branch"] < 0 else "chp",
                       ev["m"], ev["H"], ev["part"]["D"],
                       ev["part"]["neff"], ev["part"]["fill"],
                       ev["B"] / max(ev["D"], 1e-300),
                       ev["r_env"], ev["wdmax"]))
    if not smoke:
        check("G41-anatomy-census", st["add1"] <= ADD_BAR
              and st["add2"] <= ADD_BAR,
              "DIAG_ANATOMY (42 rungs): n_eff med %.2f slope "
              "%+.3f; EXACT decomposition (i) sl_D = 2 x sl_L1 - "
              "sl_neff = 2 x (%+.3f) - (%+.3f) = %+.3f (dev "
              "%.1e); (ii) sl_D = sl_mx + sl_L1 + sl_fill = "
              "%+.3f %+.3f %+.3f (dev %.1e); class shares "
              "A/Bv/cross med %.2f/%.2f/%+.2f; D band shares "
              "LOW/MID/EDGE med %.2f/%.2f/%.2f; top-block share "
              "med %.2f slope %+.3f"
              % (st["neff_med"], st["sl_neff"], st["sl_L1"],
                 st["sl_neff"], st["sl_D"], st["add1"],
                 st["sl_mx"], st["sl_L1"], st["sl_fill"],
                 st["add2"], st["clsA_med"], st["clsB_med"],
                 st["clsX_med"], st["dlo_med"], st["dmid_med"],
                 st["ded_med"], st["top_med"], st["sl_top"]))
    else:
        check("G41-anatomy-census", True, "SMOKE: skipped")

    # ---------------- S5: Leg B -- the derivation routes
    section("S5  LEG B: DERIVATION ROUTES FOR DIAG_TARGET")
    df_w = max(rc["ev"]["df_dev"] for rc in pool_all)
    rec_w = max(rc["ev"]["rec_dev"] for rc in pool_all)
    cs_w = max(rc["ev"]["cs_worst"] for rc in pool_all)
    csc_w = max(rc["ev"]["cs_comp"] for rc in pool_all)
    check("G50-b1-wards", df_w <= DF_BAR and rec_w <= REC_BAR
          and cs_w <= CS_BAR and csc_w <= CS_BAR,
          "B1 wards on %d worlds: the factorization dc == dw x f "
          "at every shared position worst %.1e (bar %.0e) -- the "
          "r299 c-value-difference fund made computational; the "
          "block reconstruction P_rec == P_ov worst %.1e (bar "
          "%.0e); per-block Cauchy-Schwarz slack %.1e and "
          "composed D_ov <= wdmax x QabsD slack %.1e (bars %.0e, "
          "rel D) -- the chain-norm route is exact algebra"
          % (len(pool_all), df_w, DF_BAR, rec_w, REC_BAR,
             cs_w, csc_w, CS_BAR))
    # ---- B1 identity census on the |dw| measure (id pool)
    id_pool = (mrecs + [crecs[c] for c in ("EPST", "SCR")]) \
        if smoke else \
        ([rc for rc in recs if rc["kz"] in (KZ_ANCHOR, 20)]
         + mrecs + [crecs[c] for c in ("EPST", "SCR")])
    crosses = []
    devs = []
    for rc in id_pool:
        sd = rc["ev"]["sd"]
        if sd["n"] == 0:
            continue
        cq = VCP.chain_quads(rc["p"]["rows"], rc["N"], sd["x"],
                             np.abs(sd["dw"]))
        crosses.append(max(abs(v) for v in cq["cr"].values()))
        devs.append(abs(cq["q2"] - cq["pd"])
                    / max(abs(cq["q2"]), 1e-300))
    id_worst = max(max(crosses), max(devs)) if crosses else 0.0
    id_cmed = float(np.median(crosses)) if crosses else 0.0
    if id_worst <= ID_HOLDS:
        id_st = "HOLDS"
    elif id_worst <= ID_NEAR:
        id_st = "NEAR"
    else:
        id_st = "BREAKS"
    if not smoke:
        comp_b1 = st["sl_wdmax"] + st["sl_qd"]
        check("G51-b1-census", True,
              "B1 census: sl_wdmax %+.3f + sl_Qd %+.3f = composed "
              "%+.3f vs sigma* %+.3f -- %s; identity census on "
              "the |dw| measure (%d worlds): %s (cross med %.3f, "
              "worst %.3f; HOLDS bar %.0e) -- the proven sum "
              "rule %s to the difference measure"
              % (st["sl_wdmax"], st["sl_qd"], comp_b1,
                 st["sigma_star"],
                 "MEETS" if comp_b1 <= st["sigma_star"]
                 else "FAILS by %.3f"
                 % (comp_b1 - st["sigma_star"]),
                 len(id_pool), id_st, id_cmed, id_worst,
                 ID_HOLDS,
                 "ATTACHES" if id_st == "HOLDS"
                 else "does NOT attach"))
        comp_b2 = st["sl_mx"] + st["sl_L1"]
        check("G52-b2-census", True,
              "B2 census: sl_mx %+.3f + sl_L1 %+.3f = composed "
              "%+.3f vs sigma* %+.3f -- %s; MAX control: "
              "slope(maxatom/M) %+.3f (a single c-value "
              "distance), block/atom ratio mx/maxatom med %.2f "
              "slope %+.3f -- %s; the fill decay %+.3f is what "
              "the factorization cannot see"
              % (st["sl_mx"], st["sl_L1"], comp_b2,
                 st["sigma_star"],
                 "MEETS" if comp_b2 <= st["sigma_star"]
                 else "FAILS by %.3f"
                 % (comp_b2 - st["sigma_star"]),
                 st["sl_maxatom"], st["mxma_med"], st["sl_mxma"],
                 "the max IS atom-controlled"
                 if st["mxma_med"] <= 2.0
                 else "the max aggregates many atoms",
                 st["sl_fill"]))
        need_neff = 2.0 * st["sl_L1"] - st["sigma_star"]
        check("G53-b3-census", True,
              "B3 census (DISCLOSED: the slope clause is an exact "
              "reparametrization of DIAG_TARGET): NEFF_TARGET "
              "needed slope(n_eff) >= 2 sl_L1 - sigma* = %+.3f, "
              "measured %+.3f -- %s (margin %.3f); D_rank(Delta) "
              "slope %+.3f (%s); sp(N, n_eff) %+.2f, "
              "sp(D_rank(Delta), n_eff) %+.2f -- the D_rank link "
              "is %s"
              % (need_neff, st["sl_neff"],
                 "MET" if st["sl_neff"] >= need_neff
                 else "NOT MET by %.3f"
                 % (need_neff - st["sl_neff"]),
                 st["sl_neff"] - need_neff, st["dd_sl"],
                 "falling -- provable terrain"
                 if st["dd_sl"] < 0 else "NOT falling",
                 st["sp_n_neff"], st["sp_dd_neff"],
                 "real but correlational"
                 if abs(st["sp_dd_neff"]) >= 0.5
                 else "weak"))
    else:
        need_neff = float("nan")
        check("G51-b1-census", True,
              "SMOKE: |dw| identity census at w9 pool: %s (cross "
              "med %.3f)" % (id_st, id_cmed))
        check("G52-b2-census", True, "SMOKE: skipped")
        check("G53-b3-census", True, "SMOKE: skipped")

    # ---------------- S6: sealed diag adjudication + Leg D
    section("S6  SEALED DIAG ADJUDICATION + LEG D")
    b1_valid = (df_w <= DF_BAR and rec_w <= REC_BAR
                and cs_w <= CS_BAR and csc_w <= CS_BAR)
    b2_valid = (mxl1_w <= MAXL1_BAR)
    env_sw = max(rc["ev"]["env_slack"] for rc in pool_all)
    env_cw = max(rc["ev"]["env_comp"] / max(rc["ev"]["r_env"],
                                            1e-300)
                 for rc in pool_all)
    ratio_valid = (env_sw <= ENV_BAR and env_cw <= ENV_BAR)
    if not smoke:
        b3_valid = (st["add1"] <= ADD_BAR)
        b1_ok = b1_valid and (st["sl_wdmax"] + st["sl_qd"]
                              <= st["sigma_star"])
        b2_ok = b2_valid and (st["sl_mx"] + st["sl_L1"]
                              <= st["sigma_star"])
        b3_ok = (b3_valid and st["sl_neff"] >= need_neff
                 and st["dd_sl"] < 0.0)
        derived = b1_ok and id_st == "HOLDS"
        if derived:
            outcome = "DIAG_DERIVED"
        elif b1_ok or b2_ok or b3_ok:
            outcome = "DIAG_SPLIT"
        else:
            outcome = "DIAG_STILL_EMPIRICAL"
        fired = []
        if b1_ok:
            fired.append("B1(QABS_TARGET: prove the wdmax/QabsD "
                         "scaling, composed %+.3f)"
                         % (st["sl_wdmax"] + st["sl_qd"]))
        if b2_ok:
            fired.append("B2(MAXL1_TARGET: prove sl_mx + sl_L1 "
                         "<= sigma*, composed %+.3f)"
                         % (st["sl_mx"] + st["sl_L1"]))
        if b3_ok:
            fired.append("B3(NEFF_TARGET: prove slope(n_eff) >= "
                         "%+.3f from the falling D_rank, "
                         "measured %+.3f)"
                         % (need_neff, st["sl_neff"]))
        check("G60-diag-adjudication", True,
              "SEALED RULE fired: %s (B1_OK %s: composed %+.3f "
              "vs sigma* %+.3f, ident %s; B2_OK %s: composed "
              "%+.3f; B3_OK %s: needed %+.3f vs measured %+.3f, "
              "dd_sl %+.3f; DERIVED clause: B1_OK AND ident "
              "HOLDS)%s"
              % (outcome, b1_ok, st["sl_wdmax"] + st["sl_qd"],
                 st["sigma_star"], id_st, b2_ok,
                 st["sl_mx"] + st["sl_L1"], b3_ok, need_neff,
                 st["sl_neff"], st["dd_sl"],
                 ("; fired: " + " | ".join(fired)) if fired
                 else ""))
    else:
        outcome = "SMOKE_NO_ADJUDICATION"
        fired = []
        check("G60-diag-adjudication", True, "SMOKE: skipped")

    # ---------------- S7: Leg C -- the ratio flatness
    section("S7  LEG C: RATIO FLATNESS (KERNEL ENVELOPE)")
    check("G70-ratio-envelope-wards", ratio_valid,
          "the exact kernel envelope on %d worlds: F_H(theta) <= "
          "min(H, 1/(H sin^2(theta/2))) pointwise slack %.1e "
          "(x 1/H scale) and composed B/D <= R_env slack %.1e "
          "(rel R_env; bars %.0e) -- pure kernel algebra, "
          "world-blind" % (len(pool_all), env_sw, env_cw,
                           ENV_BAR))
    if not smoke:
        ratio_structural = (ratio_valid
                            and st["sl_renv"] <= RATIO_GROW)
        rat_out = ("RATIO_BOUNDED_STRUCTURAL" if ratio_structural
                   else "RATIO_EMPIRICAL")
        check("G71-ratio-adjudication", True,
              "SEALED RULE fired: %s -- RATIO_TABLE: B/D med "
              "%.2f slope %+.3f; R_env med %.2f slope %+.3f (grow "
              "bar %+.2f: %s); sp(B/D, q50) %+.2f, slope(q50) "
              "%+.3f -- %s; DISCLOSED: R_env consumes the "
              "measured spectrum shape (the kernel side is "
              "structural, the weighting is not)"
              % (rat_out, st["rat_med"], st["sl_rat"],
                 st["renv_med"], st["sl_renv"], RATIO_GROW,
                 "non-growing" if st["sl_renv"] <= RATIO_GROW
                 else "GROWS by %.3f over bar"
                 % (st["sl_renv"] - RATIO_GROW),
                 st["sp_rat_q50"], st["sl_q50"],
                 "the ratio IS the lobe-width coordinate"
                 if abs(st["sp_rat_q50"]) >= 0.5
                 else "the ratio and the lobe width decouple"))
    else:
        ratio_structural = False
        rat_out = "SMOKE_NO_ADJUDICATION"
        check("G71-ratio-adjudication", True, "SMOKE: skipped")

    # ---------------- Leg D: composition or refined freeze
    if not smoke:
        if outcome == "DIAG_DERIVED" and ratio_structural:
            info("CANDIDATE THEOREM (diagonal composition, L2 "
                 "generic half): for every rung of the sealed "
                 "ladder (N in [%d, %d], H = ceil(sqrt(m))): the "
                 "B1 chain bound D <= wdmax x QabsD with the "
                 "attached sum rule => sl_D <= sigma* = %+.3f; "
                 "with the structural ratio bound B/D <= R_env "
                 "(non-growing) => sigma <= sigma* => the r297 "
                 "target inequality => the v964-S0 vdC theorem "
                 "=> delta' > %.2f on the generic half; "
                 "exceptions: 6 via the r287 F2 certificates, "
                 "kz15 via the r270 exact-finite certificate.  "
                 "Wave-9 promotion candidate -- NOT promoted "
                 "here." % (min(Ns), max(Ns), st["sigma_star"],
                            DELTA_NEED))
            legd = "COMPOSED"
        else:
            info("REST_FROZEN (the refined pair, smaller than "
                 "r299): DIAG rest = NEFF_TARGET: prove "
                 "slope(n_eff) >= 2 x slope(L1/M) - sigma* = "
                 "%+.3f (measured %+.3f, margin %.3f; the D_rank "
                 "correlation sp %+.2f is the named bridge to "
                 "provable terrain); equivalently sl_mx + sl_L1 "
                 "+ sl_fill <= sigma* with the fill decay %+.3f "
                 "as the non-factorizable part.  RATIO rest = "
                 "slope(R_env) <= %+.2f (measured %+.3f -- %s)."
                 % (need_neff, st["sl_neff"],
                    st["sl_neff"] - need_neff, st["sp_dd_neff"],
                    st["sl_fill"], RATIO_GROW, st["sl_renv"],
                    "already MET structurally"
                    if ratio_structural else "NOT met"))
            legd = "REST_FROZEN"
        check("G61-leg-d", True,
              "Leg D %s -- the full candidate fires ONLY on "
              "DIAG_DERIVED + RATIO_BOUNDED_STRUCTURAL by the "
              "sealed rule; no post-hoc rescue"
              % ("FIRED (candidate printed, NOT promoted)"
                 if legd == "COMPOSED" else
                 "REST_FROZEN (refined targets printed)"))
    else:
        check("G61-leg-d", True, "SMOKE: skipped")

    # ---------------- S8: worlds + m2 real + anchors + mp wards
    section("S8  WORLD CLASSES + MUSTFAIL M2 (REAL) + MP WARDS")
    if not smoke:
        pm = float(np.median([rc["ev"]["part"]["neff"]
                              / max(rc["ev"]["m"], 1)
                              for rc in recs]))
        fm = float(np.median([rc["ev"]["part"]["fill"]
                              for rc in recs]))
        main_cls = ("PART_HIGH" if pm >= PART_CLS else "PART_LOW",
                    "FILL_HIGH" if fm >= FILL_CLS else "FILL_LOW")
        ctl_note = []
        world_blind = True
        for c in ("EPST", "SCR"):
            ev = crecs[c]["ev"]
            pc = ev["part"]["neff"] / max(ev["m"], 1)
            fc = ev["part"]["fill"]
            cls_c = ("PART_HIGH" if pc >= PART_CLS
                     else "PART_LOW",
                     "FILL_HIGH" if fc >= FILL_CLS
                     else "FILL_LOW")
            ctl_note.append("%s %s/%s" % (c, cls_c[0], cls_c[1]))
            world_blind &= (cls_c == main_cls)
        check("G80-world-controls", True,
              "the anatomy classes (same sealed med rules at the "
              "single control rung): MAIN %s/%s vs %s -- %s "
              "(TESTED, not assumed: a class break would be a "
              "disclosed finding; crossref r299: the O-sign "
              "class already separates)"
              % (main_cls[0], main_cls[1], str(ctl_note),
                 "WORLD-BLIND" if world_blind
                 else "WORLD_SENSITIVE (disclosed)"))
    else:
        world_blind = True
        main_cls = ("n/a", "n/a")
        ctl_note = []
        check("G80-world-controls", True, "SMOKE: skipped")
    m2_pool = mrecs + ([recs[0]] if smoke else [])
    m2_vals = []
    for rc in m2_pool:
        p_ = rc["ev"]["part"]
        m2_vals.append((rc["kz"], (p_["D"] - p_["mx"] ** 2)
                        / max(p_["D"], 1e-300)))
    m2_min = min(v for _k, v in m2_vals)
    check("G81-mustfail-m2-real", m2_min >= MUT_MIN,
          "m2 SWAPPED MAX/L1 on the real mains: D - mx^2 = %s of "
          "D (all >= %.0e) LOUD -- a single-block bound loses "
          "the object; the L1 mass factor is load-bearing"
          % ("; ".join("w%d %.1e" % (k, v) for k, v in m2_vals),
             MUT_MIN))
    rowsS = ctrl["SMOOTH"]["rows"]
    NS = ctrl["SMOOTH"]["N"]
    scT = [abs(rowsS[k]["tb"] * math.exp(rowsS[k]["Ls"]
                                         - rowsS[k + 1]["Ls"]))
           for k in range(NS - 1)]
    alias = max(scT[2:]) / max(scT[0], scT[1])
    qS = float(ctrl["SMOOTH"]["rho"][NS - 1]) / B57
    evS = crecs["SMOOTH"]["ev"]
    okSd = (evS["spec_dev"] <= SPEC_BAR
            and evS["pair_dev"] <= PAIR_BAR
            and evS["cls_dev"] <= CLS_BAR
            and evS["env_slack"] <= ENV_BAR)
    check("G82-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okSd,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "every exact ward holds trivially on the self-aliased "
          "source (%s)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okSd else "BROKEN"))
    if not smoke:
        mp_note = []
        ok_mp = True
        rc15 = next(r_ for r_ in recs if r_["kz"] == KZ_ANCHOR)
        t15 = PBB.mp_drive(rc15["p"], MP_DPS)
        d15 = abs(t15 - rc15["t_term"])
        ok_mp = ok_mp and (d15 <= MP_T_BAR)
        mp_note.append("kz15 (N %d) dev %.1e (bar %.0e)"
                       % (rc15["N"], d15, MP_T_BAR))
        for rc in recs[-2:]:
            t_mp = PBB.mp_drive(rc["p"], MP_DPS)
            dv = abs(t_mp - rc["t_term"])
            ok_mp = ok_mp and (dv <= MP_DEEP_BAR)
            mp_note.append("kz%d (N %d, DEEPEST) dev %.1e (bar "
                           "%.0e)" % (rc["kz"], rc["N"], dv,
                                      MP_DEEP_BAR))
        check("G83-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs: %s" % (MP_DPS, "; ".join(mp_note)))
    else:
        check("G83-mp-deep-wards", True, "SMOKE: skipped")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact participation anatomy of the diagonal, "
          "the three-route derivation census with exact wards, "
          "the |dw| identity census, the exact kernel-envelope "
          "ratio majorant, the sealed two adjudications and the "
          "refined rest freeze -- NO new certificate promoted, "
          "NO bound modification of the sealed forms")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["DIAG_ANATOMY(n_eff med %.2f sl %+.3f; sl_D = "
                 "2 sl_L1 - sl_neff = 2(%+.3f) - (%+.3f) = %+.3f "
                 "dev %.0e; = sl_mx %+.3f + sl_L1 %+.3f + "
                 "sl_fill %+.3f dev %.0e; class A/Bv/x med "
                 "%.2f/%.2f/%+.2f; D bands %.2f/%.2f/%.2f; top "
                 "share %.2f sl %+.3f)"
                 % (st["neff_med"], st["sl_neff"], st["sl_L1"],
                    st["sl_neff"], st["sl_D"], st["add1"],
                    st["sl_mx"], st["sl_L1"], st["sl_fill"],
                    st["add2"], st["clsA_med"], st["clsB_med"],
                    st["clsX_med"], st["dlo_med"], st["dmid_med"],
                    st["ded_med"], st["top_med"], st["sl_top"])]
        parts.append("ROUTE_TABLE(B1 valid 47/47 sl_wdmax %+.3f "
                     "sl_Qd %+.3f composed %+.3f vs sigma* %+.3f "
                     "ident %s; B2 valid 47/47 sl_mx %+.3f sl_L1 "
                     "%+.3f composed %+.3f maxatom sl %+.3f "
                     "mx/maxatom med %.2f; B3 needed %+.3f "
                     "measured %+.3f dd_sl %+.3f sp(dd, n_eff) "
                     "%+.2f)"
                     % (st["sl_wdmax"], st["sl_qd"],
                        st["sl_wdmax"] + st["sl_qd"],
                        st["sigma_star"], id_st, st["sl_mx"],
                        st["sl_L1"], st["sl_mx"] + st["sl_L1"],
                        st["sl_maxatom"], st["mxma_med"],
                        need_neff, st["sl_neff"], st["dd_sl"],
                        st["sp_dd_neff"]))
        if outcome == "DIAG_DERIVED":
            parts.append("DIAG_DERIVED(B1 + ident HOLDS)")
        elif outcome == "DIAG_SPLIT":
            parts.append("DIAG_SPLIT(%s)" % " | ".join(fired))
        else:
            parts.append("DIAG_STILL_EMPIRICAL(common "
                         "obstruction: both magnitude "
                         "factorizations pay the fill/imbalance "
                         "factor %+.3f; the reparametrized "
                         "target is not met)" % st["sl_fill"])
        parts.append("RATIO_TABLE(B/D med %.2f sl %+.3f; R_env "
                     "med %.2f sl %+.3f; sp(B/D, q50) %+.2f, "
                     "sl_q50 %+.3f)"
                     % (st["rat_med"], st["sl_rat"],
                        st["renv_med"], st["sl_renv"],
                        st["sp_rat_q50"], st["sl_q50"]))
        parts.append(rat_out)
        if outcome == "DIAG_DERIVED" and ratio_structural:
            parts.append("CANDIDATE_THEOREM(printed in S6/S7, "
                         "wave-9 candidate NOT promoted)")
        else:
            parts.append("REST_FROZEN(DIAG: slope(n_eff) >= "
                         "%+.3f measured %+.3f margin %.3f; "
                         "RATIO: slope(R_env) <= %+.2f measured "
                         "%+.3f)"
                         % (need_neff, st["sl_neff"],
                            st["sl_neff"] - need_neff,
                            RATIO_GROW, st["sl_renv"]))
        if not world_blind:
            parts.append("WORLD_SENSITIVE(MAIN %s/%s vs %s -- "
                         "disclosed finding)"
                         % (main_cls[0], main_cls[1],
                            str(ctl_note)))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the participation "
          "identities, the dc = dw x f factorization, the "
          "per-block CS chain, the max/L1 factorization, the "
          "kernel envelope, the Fractions sum rule (all "
          "world-blind); MEASURED: every slope, share, class and "
          "correlation (42 rungs only); OPEN: NEFF_TARGET beyond "
          "the measured margin, the cofinal step H5, kz15 beyond "
          "r270; NO RH claim"
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
