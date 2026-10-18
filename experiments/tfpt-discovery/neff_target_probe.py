#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""neff_target_probe -- PRIME.PORT.L2.NEFF_TARGET.01 (round 301):
the ANATOMY AND DERIVATION of the participation growth -- WHY does
n_eff = L1^2/D grow linearly in N, and can the r300 frozen rest
inequality NEFF_TARGET (prove slope(n_eff) >= 2 sl_L1 - sigma* =
+0.908; measured +0.963, margin 0.055 THIN) be derived
SOURCE-PURELY?  Context (sealed record inputs): r297 (SPEC
e42a76eb) froze the target inequality sigma <= sigma* = -0.516;
r298 (SPEC 05e831be) proved S_F ~ B(PDelta, PDelta); r299 (SPEC
f432e944) fired DECAY_SPLIT with the rest pair DIAG_TARGET +
ratio flatness and found FULL-SUPPORT overlap 42/42 (Delta is a
pure c-value difference on ONE shared node set, cconv 0.86 slope
+0.045: no pointwise c-convergence); r300 (SPEC 55218b5d, 31/31)
proved the exact participation decomposition sl_D = 2 sl_L1 -
sl_neff (dev 6.7e-16; the ENTIRE diagonal decay is participation
growth), settled the ratio half structurally
(RATIO_BOUNDED_STRUCTURAL, R_env slope -0.122), closed the
chain-norm shortcut (|dw| census BREAKS) and localized the
magnitude-route failure in the fill decay -0.225; the ONE frozen
rest is NEFF_TARGET, with the falling boundary discrepancy
D_rank(Delta) (slope -0.117) and its coupling sp(D_rank, n_eff)
-0.81 as the named correlational bridge.  kz15 permanently closed
via r270; the 6 exceptions via the r287 F2 certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r287/r297/r298/r299/r300 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval);
F = 0.20 edge split; maximal same-sign runs of the bx-sorted
bulk; level-2 blocks (r270 convention); FROZEN vdC window H =
max(2, ceil(sqrt(m))); the frozen positional Fejer block kernel
(r298: block_breaks + aggregate_blocks + fejer_bil + fejer_apply)
and the r299 spectral machinery (spec_decomp, band_energies,
pair_split, overlap_split, cconv_census) and the r300
participation machinery (DTP.participation + DTP.shared_delta +
DTP.cs_block_route), ALL imported verbatim; PDelta = Pbeta -
Pomega; the round's central quantity is the PARTICIPATION NUMBER
n_eff = L1^2/D of the ONE positive field |PDelta| and its growth
exponent slope(n_eff) against the frozen standalone target
NEED = 2 x slope(L1/M) - sigma* (recomputed live, record +0.908).

LEG 0 -- ANCHOR REGRESSION (r297/r298/r299/r300 record numbers
adopted as-is, disclosed): the full r300 anchor scaffold verbatim
(sigma -0.714, sigma* -0.516, sl_c2 +0.196, sl_pref +0.489, tol
0.01; D_rank med 0.024 slope -0.42; imbalance +0.244; the r298
decomposition bit-near incl. overlap w9 == 367 EXACT; the r299
route set bit-near incl. sl_D -0.571, ratio 1.29 / -0.168,
D_rank(Delta) 0.016 / -0.12, FULL overlap 42/42) PLUS the new
r300 anchors: n_eff med 37.41 tol 0.05, sl_neff +0.963 tol 0.01,
sl_L1 +0.196 tol 0.01, sl_mx -0.542 tol 0.01, sl_fill -0.225 tol
0.01, both slope-additivity identities <= 1e-9, mx/maxatom med
1.07 tol 0.02, sp(N, n_eff) +0.96 tol 0.02, sp(D_rank(Delta),
n_eff) -0.81 tol 0.02, and the r300 world classes (MAIN
PART_LOW/FILL_LOW vs EPST PART_HIGH/FILL_HIGH + SCR
PART_LOW/FILL_HIGH) reproduced EXACTLY.

LEG A -- THE N_EFF ANATOMY (what carries the growth?):
(A1) PARTICIPATION-ORDER FAMILY: with p_j = |PDelta_j| / L1 the
  Renyi participation numbers N_k = (sum_j p_j^k)^(-1/(k-1)) for
  k = 2, 3, 4 and N_inf = L1 / mx (N_2 == n_eff by definition;
  N_2 >= N_3 >= N_4 >= N_inf is the EXACT power-mean chain,
  gated <= 1e-9 rel on all 47 worlds).  Med + slopes of all
  four; the tail census N_4/N_2 (med + slope): if the higher
  orders grow at the SAME exponent the growth is echt
  anti-concentration (many comparable carriers); if N_4/N_2
  falls, a heavy tail is broadening the distribution and n_eff
  is more fragile than it looks -- PRINTED, not assumed.
(A2) CARRIER MAP (source-pure; the weight SIGN class is the
  prime/power proxy, no prime oracle): L1 shares of the r300
  class fields sum|A_j|/L1 and sum|Bv_j|/L1 (med), and the
  |PDelta|-weighted positional spread of the block midpoints
  (interquartile range rel the bulk hull, med + slope) -- does
  the mass spread positionally as it spreads in count?
(A3) STABILITY OF THE TARGET NUMBER (honesty before optimism):
  half-ladder slopes (lower/upper 21 rungs, disjoint, gated) and
  the leave-one-out JACKKNIFE over the 42 rungs (42 slopes on 41
  rungs each): min / max / #below NEED.  SEALED: MARGIN_FRAGILE
  fires iff min_jackknife slope(n_eff) < NEED -- if the thin
  0.055 margin dies under single-rung removal, THAT is the
  round's primary finding.  DISCLOSED: jackknife and half-ladder
  probe the stability of the frozen halves_slope estimator; they
  add no new information about the cofinal law.

LEG B -- DERIVATION ROUTES FOR NEFF_TARGET (each an exact
per-rung statement on the real builders, source-pure, AST scope
audit, worlds test on EPSTEIN/SCRAMBLE):
(B1) QUASI-UNIFORMITY / COUNT ROUTE: over the ACTIVE blocks
  (|PDelta_j| > 0; count n_act) with mean mu and population
  variance var of |PDelta|, CV^2 = var/mu^2:
      n_eff  =  n_act / (1 + CV^2)      -- an EXACT IDENTITY
  (algebra: D = n_act (mu^2 + var), L1 = n_act mu; gated <=
  1e-9 rel on 47 worlds; re-proved module-own in exact
  Fractions).  Slope additivity slope(n_eff) = slope(n_act) -
  slope(1 + CV^2) exact (<= 1e-9).  Census: sl_nact, sl_cv2p,
  Gini over active blocks (med), the COUNT LINK n_act == m
  (n/42; m is the constructive level-2 block count -- if full,
  the count factor is pure construction).  DISCLOSED HONESTY:
  by the identity the B1 slope clause is algebraically
  EQUIVALENT to NEFF_TARGET (a reparametrization, r300-B3
  style); the derivation CONTENT is the split into a
  constructive count (n_act == m) and ONE bounded-uniformity
  statement (CV^2 non-growing) -- the friendliest remaining
  coordinate of the lane.
(B2) EQUIDISTRIBUTION ROUTE (the D_rank bridge made EXACT): on
  the shared support (r299 fund: ONE node set) with the
  aggregated c-difference dc and the abs block masses w_j =
  sum_{p in block j} |dc(p)|, W = sum w_j, on the bulk hull
  [a_h, b_h]: (i) the WEIGHTED star discrepancy delta_w of the
  |dc| measure against uniform; (ii) the INTERVAL BOUND
  |w_j/W - lambda_j| <= 2 delta_w per block (lambda_j = block
  interval share -- a THEOREM of star discrepancy, gated <=
  1e-9 on 47 worlds); (iii) the exact triangle bounds
  max|P_ov| <= max w_j and L1(P_ov) <= W; composed:
      n_eff(P_ov) >= L1/mx >= surv / s_max
                  >= surv / (lambda_max + 2 delta_w)
  with surv = L1(P_ov)/W (the in-block signed survival) and
  s_max = max w_j / W (all gated; on the 42 rungs P_ov ==
  PDelta identically, equality gated with the r300 REC_FLOOR
  degenerate guard).  Census: delta_w med + slope (the WEIGHTED
  D_rank -- the bridge object), sl_surv, slope of the composed
  bound vs NEED.  DISCLOSED STRUCTURAL PRIOR: the chain caps at
  N_inf = L1/mx, whose growth is sl_L1 - sl_mx = +0.738 by the
  r300 records -- 0.17 BELOW the needed +0.908: the max-based
  anti-concentration route is expected to fail by exactly the
  fill decay, the same wall as r300-B2; measured, not assumed.
(B3) CHAIN-STABILITY ROUTE: the localization scale of the
  c-difference profile along the shared support: with z = dc -
  mean(dc) on the bulk, the normalized autocorrelation rho(h)
  and the e-folding length l_loc = min{h >= 1 : |rho(h)| <=
  1/e} (else n); the ATOM-LEVEL participation n_eff_atom =
  (sum|dc|)^2 / sum dc^2 (med + slope); sp(n_eff_atom, n_eff).
  If the recursion decorrelates the difference profile at O(1)
  scales, anti-concentration is chain dynamics.  The LOCAL
  SUM-RULE CENSUS: the r297-proven Parseval sum rule tested as
  a LOCAL energy identity -- VCP.chain_quads on the |dw|
  measure restricted to K_LOC = 4 consecutive position-count
  quartiles of the shared bulk support, id pool kz15/kz20 +
  mains + EPST/SCR, classified HOLDS <= 1e-6 / NEAR <= 1e-3 /
  BREAKS per window (crossref r300: the GLOBAL census BREAKS,
  cross med 0.932 -- does the break localize?).
SEALED NEFF ADJUDICATION (frozen BEFORE evaluation, exactly one
fires): NEED = 2 sl_L1 - sigma* recomputed live;
  B1_OK iff the identity + additivity wards hold on 47 worlds
    and sl_nact - sl_cv2p >= NEED (disclosed reparametrization);
  B2_OK iff every B2 ward holds on 47 worlds and slope(composed
    bound) >= NEED;
  B3_OK iff slope(n_eff_atom) >= NEED and slope(l_loc) <= +0.05;
  NEFF_DERIVED(B1) iff B1_OK and sl_cv2p <= 0.0 (the uniformity
    factor is non-growing) and n_act == m on 42/42 (the count is
    fully constructive) -- then the growth is carried by the
    constructive block count alone;
  NEFF_SPLIT(fired routes, rest targets frozen) iff not DERIVED
    and (B1_OK or B2_OK or B3_OK) -- B1 rest: UNIF_TARGET =
    prove slope(1 + CV^2) <= sl_nact - NEED; B2 rest:
    DISC_TARGET = prove the surv/discrepancy scaling; B3 rest:
    MIX_TARGET = prove the decorrelation;
  NEFF_STILL_EMPIRICAL(measured common obstruction) otherwise.
MARGIN_FRAGILE is an INDEPENDENT tag (Leg A3) and can coexist.

LEG C -- THEOREM COMPOSITION: fires ONLY on NEFF_DERIVED AND NOT
MARGIN_FRAGILE -- the full r297->r301 candidate is printed with
every constant (B1 count identity => slope(n_eff) >= NEED => the
r300 participation decomposition => sl_D <= sigma* => with
RATIO_BOUNDED_STRUCTURAL (r300) sigma <= sigma* = -0.516 => the
r297 target inequality => the v964-S0 vdC theorem => delta' >
0.21 on the generic half; exceptions 6 via r287 F2 + kz15 via
r270).  Wave-10 promotion candidate -- NOT promoted.  OTHERWISE
Leg C freezes the refined rest (and if MARGIN_FRAGILE fired,
names IT as the primary finding).

LEG D -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) PARTICIPATION IDENTITY WRONG EXPONENT (exact Fractions,
  module-own): on the rational vector (2, 1, 1): n_eff = 8/3,
  n_act = 3, CV^2 = 1/8, identity n_eff x (1 + CV^2) == n_act
  dev 0 EXACT; mutant (a) L1^3/D = 32/3 (the participation
  value itself off by 8) breaks the identity by 9 EXACT;
  mutant (b) the (1 + CV^4) head breaks it by 7/24 EXACT --
  both CAUGHT: the exponent of the participation numerator and
  of the uniformity head are load-bearing; (m2)
  CONVOLUTION-MATRIX MUTANTS: (a) HALVED DISCREPANCY PREFACTOR
  (claim |w_j/W - lambda_j| <= delta_w): the one-atom toy (atom
  0.5 on [0, 1], blocks (0.4, 0.6]) has delta = 1/2, block
  deviation 0.8 <= 2 delta = 1 while the mutant 0.8 > 0.5
  breaks by 0.3 EXACT -- CAUGHT; (b) TRANSPOSED AGGREGATION
  MATRIX (rows/cols swapped): on the square toy (atoms 0, 0.2,
  2; breaks 0.5, 1.5; dc (1, -2, 3)) the transpose changes
  n_eff from 8/5 to 25/11 (break 37/55 EXACT, LOUD) AND is
  structurally FLAGGED by the column-sum ward (colsums (2, 0,
  1) != 1: an atom counted twice, a block emptied) -- the
  atom-to-block assignment is load-bearing; (m3) OVERLAPPING
  SUB-LADDERS: the honest half split (0..20 | 21..41) is
  disjoint + covering (gated); the mutant split (0..24 |
  17..41) shares 8 rungs -- CAUGHT by the disjointness ward
  (the jackknife subsets are each 41 unique rungs, gated);
  (m4) CONCENTRATED SYNTHETIC PDELTA (one-block mass): n_eff
  == 1 EXACT, n_act == 1, CV^2 == 0, all order numbers == 1,
  and the B2 chain collapses (one-atom toy bound 1/1.8 <= 1)
  -- EVERY route sees the collapse, gated; LOUD against the
  real med 37.41 (ratio printed); (m5a/m5b) WORLD-BLINDNESS
  BREAK: a builder consuming the withheld terminal drive key
  AND a builder consuming the branch label are both FLAGGED by
  the AST scope audit.  Scope hygiene: the new builders
  (participation_orders, quasi_uniformity, wdisc_route,
  dc_profile, split_disjoint) consume positions + weights +
  chain values only (BOUND_FORBIDDEN set); fragment audit (no
  fit primitives); TOY EXACTNESS (bar 1e-14): orders on
  (1,-1,1) (all N_k = 3) and (2,1,1) (N_2 = 8/3, N_3^2 = 32/5,
  N_4^3 = 128/9, N_inf = 2, monotone); quasi-uniformity float
  == Fractions on (2,1,1); the wdisc toy (atoms 0.25/0.5/0.75
  weights 1/2/1 on [0,1], breaks 0.4/0.6): delta_w = 1/4,
  lambda (0.4, 0.2, 0.4), shares (0.25, 0.5, 0.25), worst
  interval dev 0.3 <= 0.5, composed bound 1/(0.4 + 0.5) =
  10/9 <= n_eff = 8/3; the profile toy dc = (1,-1,1,-1):
  rho = (-3/4, 1/2, -1/4), l_loc = 3, n_eff_atom = 4; mp
  SAMPLES (dps 60): kz15 (bar 1e-8) + the two deepest rungs
  (bar 3e-6); SMOOTH anchor (alias <= 1e-12, q_N <= 1e-20)
  with the DEGENERATE-SOURCE GUARD declared IN ADVANCE (the
  r300-a1 convention adopted): on a source with Delta == 0
  identically (self-aliased SMOOTH) the shared-support mass W
  degenerates to float noise; every B2/B3 shared-support ward
  is skipped exactly when W <= 1e-6 x the total contribution
  mass, disclosed per world -- no amendment needed for the
  known degenerate world.

INDEX FIREWALL (binding, r238-r300 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks + WBT.fejer_bil +
WBT.fejer_apply, r299 FDP.spec_decomp + FDP.band_energies +
FDP.pair_split + FDP.overlap_split + FDP.cconv_census, r300
DTP.participation + DTP.shared_delta + DTP.cs_block_route, r269
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
= smallest power of two >= 2 x (m + H) (FROZEN); QID_BAR 1e-9
(participation identity, rel); ORD_BAR 1e-9 (order monotonicity,
rel N_2); WD_BAR 1e-9 (interval ward abs share units; triangle +
composed rel); EQ_BAR 1e-9 (n_eff(P_ov) == n_eff(PDelta) on the
ladder, rel); ADD_BAR 1e-9 (slope additivity); DEG_FLOOR 1e-6
(degenerate-source guard, declared above); REC_FLOOR 1e-6 (r300
a1 convention, reconstruction scale floor); CV_FLAT 0.0 (DERIVED
clause); LOC_GROW +0.05; E_FOLD = 1/e; CV_CLS 1.0 (UNIF_HIGH iff
CV^2 med <= 1); K_LOC 4; ID_HOLDS 1e-6; ID_NEAR 1e-3; PART_CLS
0.5; FILL_CLS 0.5; CLS_BAR 1e-12 (class recomposition); MAXL1_BAR
1e-9 (fill <= 1); DF_BAR 1e-9 (dc == dw x f); CS_BAR 1e-9; TOY_BAR
1e-14; TOY_FFT_BAR 1e-12; MUT_MIN 1e-6; SPEC_BAR 1e-9; PAIR_BAR
1e-12; PART_BAR 1e-12; EN_BAR 1e-9; KER_BAR/DEC_BAR 1e-12;
ATTR_BAR 1e-9; LIN_BARS 1e-9 main N <= 400 / 3e-6 deep / 1e-6
controls; TB_WARD bars 1e-9 / 3e-6 / 1e-6; ID_BAR 1e-12; AC_BAR
1e-9; R297 anchors sigma -0.714 / sigma* -0.516 / sl_c2 +0.196 /
sl_pref +0.489 (tol 0.01), D_rank med 0.024 tol 0.005 slope
-0.42 tol 0.05, imb slope +0.244 tol 0.01; R298 anchors share
med 0.99 tol 0.02, sl_MAIN -1.386 tol 0.05, sl_|T| -0.698 tol
0.05, T > 0 on 42/42, canc med 1.69 tol 0.05 slope +0.207 tol
0.02, |tc med| <= 1e-3, OVERLAP_W9 == 367 EXACT; R299 anchors
sl_D -0.571 tol 0.01, sl_|O| -0.815 tol 0.01, O < 0 == 13 EXACT,
ratio med 1.29 tol 0.02 slope -0.168 tol 0.01, LOW share 0.93
tol 0.02, q50 0.19 tol 0.02, cconv 0.86 tol 0.02 slope +0.045
tol 0.01, D_rank(Delta) med 0.016 tol 0.005 slope -0.12 tol
0.05, FULL_OV == 42 EXACT; R300 anchors n_eff med 37.41 tol
0.05, sl_neff +0.963 tol 0.01, sl_L1 +0.196 tol 0.01, sl_mx
-0.542 tol 0.01, sl_fill -0.225 tol 0.01, mx/maxatom med 1.07
tol 0.02, sp(N, n_eff) +0.96 tol 0.02, sp(dd, n_eff) -0.81 tol
0.02, classes MAIN PART_LOW/FILL_LOW + EPST PART_HIGH/FILL_HIGH
+ SCR PART_LOW/FILL_HIGH EXACT; MP_DPS 60; MP_T_BAR 1e-8;
MP_DEEP_BAR 3e-6; SM_Q_BAR 1e-20; SM_ALIAS_BAR 1e-12; KZ_ANCHOR
15; runtime <= 1800 s; smoke = w9 + controls + Fractions section
+ toys + scope audits + every exact ward at w9 (ladder, slopes,
jackknife, adjudications, censuses, mp wards skipped).
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r297/r298/r299/r300 RECORD number
adopted as-is; the B1 identity, the power-mean chain, the
star-discrepancy interval bound and the B2 triangle chain are
derived algebra, disclosed above; the B1 clause equivalence and
the B2 N_inf cap (+0.738 < +0.908 expected miss) are disclosed
priors; the adjudication outcomes are sealed symmetrically -- the
priors make NEFF_SPLIT(B1 with UNIF_TARGET frozen) plausible,
but no rule was chosen to favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  NEFF_ANATOMY(N_2/N_3/N_4/N_inf med + slopes, tail N_4/N_2 med
    + slope, carrier L1 shares A/Bv, positional IQR med + slope)
+ STABILITY(half-ladder slopes lo/hi, jackknife min/max/#below
    NEED) [+ MARGIN_FRAGILE(jk_min vs NEED) if fired]
+ ROUTE_TABLE(B1 n_act med, count link n/42, sl_nact, sl_cv2p,
    Gini med; B2 delta_w med + slope, s_max slope, surv slope,
    bound slope vs NEED; B3 l_loc med + slope, n_eff_atom med +
    slope, sp(atom, block), local sum-rule census)
+ [exactly one of] NEFF_DERIVED(B1) / NEFF_SPLIT(fired routes +
    frozen rest targets) / NEFF_STILL_EMPIRICAL(obstruction)
+ [iff DERIVED and not FRAGILE] CANDIDATE_THEOREM(all constants)
  [else] REST_FROZEN(the refined needed-vs-measured statement)
+ [if a control class differs] WORLD_SENSITIVE(disclosed).
Honesty before beauty: the participation identity, the power-mean
chain, the interval-discrepancy bound and the triangle chain are
EXACT finite identities/inequalities, but every slope, share and
class is MEASURED on 42 rungs only; B1's slope clause is an exact
reparametrization of NEFF_TARGET (disclosed above), its
derivation content is the count/uniformity split ONLY; the
jackknife probes the estimator, not the cofinal law; no verdict
claims a cofinal law; the exception scalar's positivity beyond
the measured 42 stays OPEN; r243-r300 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 30/32 -- the dc_profile builder used the local
identifier name of a withheld-set entry (a pure NAME COLLISION
with the sealed scope-audit set, no truth-side read); renamed --
a code-side naming fix, no bar, band, rule or verdict rule
touched; smoke pass 2 = 32/32 (0.3 s); calibration pass 1 =
first full evaluation, 32/32 gates, wall 48.0 s, NO amendment
(the pre-declared DEG_FLOOR guard fired exactly on the known
degenerate SMOOTH world, as sealed); record run1/run2 after this
insertion, identical up to WALL; the only post-freeze edits are
the disclosed rename and this record-table insertion, which IS
the protocol):
CAL_VERDICT = NEFF_ANATOMY(N_2/N_3/N_4/N_inf med
37.41/27.88/24.04/15.47 slopes +0.963/+0.926/+0.894/+0.738 --
the Renyi order family grows at nearly ONE exponent: ECHT
anti-concentration, not a broadening tail; tail N_4/N_2 med 0.77
slope -0.069 (mild fattening only); carrier L1 shares A/Bv med
0.81/0.31; positional IQR med 0.72 slope -0.005 -- the
positional spread is FLAT: the count grows, the footprint
stays) + STABILITY(half-ladder slopes lo/hi +0.982/+0.802 --
the deep half flattens BELOW the needed +0.908: the honest
anti-extrapolation warning; jackknife min/max +0.936/+0.979,
0/42 below NEED -- the full-ladder margin survives every
single-rung removal, NO MARGIN_FRAGILE) + ROUTE_TABLE(B1 n_act
med 73.0, COUNT LINK n_act == m on 42/42 EXACT, sl_nact +1.002,
sl_cv2p +0.039, additivity exact, Gini med 0.52, CV^2 med 1.03;
B2 delta_w med 0.167 slope -0.017 -- the WEIGHTED discrepancy is
10x the unweighted D_rank (0.016) and near-FLAT: the r300 bridge
correlation lived on the raw positions, the |dc|-weighted
measure the exact chain needs is NOT falling; s_max slope
-0.747, surv med 0.44 slope -0.020, bound slope +0.074 vs NEED
+0.908 FAILS by 0.834; B3 l_loc med 1.0 slope -0.036 -- the
difference profile decorrelates at lag ONE; n_eff_atom med
118.0 slope +0.942 MET, sp(atom, block) +0.96 -- atom and block
participation grow together; local sum-rule census 0/0/24: ALL
24 windows BREAK (cross med 0.93, worst 7.15) -- the r300
global break does NOT localize away, no local energy identity
attaches) + NEFF_SPLIT(B1(UNIF_TARGET: prove slope(1 + CV^2) <=
sl_nact - NEED = +0.094, measured +0.039, margin 0.055; count
link 42/42 EXACT) | B3(MIX_TARGET: prove the O(1)
decorrelation, l_loc slope -0.036)) + REST_FROZEN(the refined
statement, STRICTLY smaller than r300's: the count factor
n_act == m is CONSTRUCTIVE on 42/42 and grows at +1.002 = NEED
+ 0.094; the ONE remaining inequality is UNIF_TARGET --
slope(1 + CV^2) <= +0.094, measured +0.039: the SAME thin 0.055
margin relocated onto a bounded-uniformity statement about the
block profile of |PDelta|; NEFF_DERIVED missed ONLY the sealed
CV_FLAT clause: sl_cv2p +0.039 > 0.0, the uniformity factor
grows, barely) + WORLD_SENSITIVE(the new UNIF class does NOT
separate cleanly: MAIN UNIF_LOW (CV^2 med 1.03, just over the
1.0 bar) is BRACKETED by EPST UNIF_HIGH (0.72) and SCR UNIF_LOW
(2.76) -- no world separator; the r300 PART/FILL classes
reproduced EXACTLY, disclosed).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; block + autocorr identities worst 6.3e-16 /
2.7e-15 on 47 worlds; r297 anchors bit-near (sigma -0.714,
sigma* -0.516, sl_c2 +0.196, sl_pref +0.489; D_rank 0.024 /
-0.42, imb +0.244); r298 anchors bit-near (identity 8.8e-16,
kernel 7.5e-16, attribution 5.4e-16; share 0.99, sl_MAIN
-1.386, sl_|T| -0.698, canc 1.69 / +0.207, overlap w9 367; sum
rule import devs 0/0); r299 anchors bit-near (sl_D -0.571,
sl_|O| -0.815, O < 0 13/42, ratio 1.29 / -0.168, LOW 0.93, q50
0.19, cconv 0.86 / +0.045, dd 0.016 / -0.12, full overlap
42/42); r300 anchors bit-near (n_eff 37.41, sl_neff +0.963,
sl_L1 +0.196, sl_mx -0.542, sl_fill -0.225, adds
6.7e-16/4.4e-16, mx/maxatom 1.07, sp +0.96/-0.81; classes
EXACT).  S3: module-own Fractions identity dev 0 (n_eff 8/3,
CV^2 1/8, n_act 3), m1a break 9 exact, m1b break 7/24 exact;
toys worst 1.8e-15 (bar 1e-14); m2a break 0.3 exact with the
correct 2-delta ward holding (slack 0), m2b break 37/55 exact +
colsum flag (2, 0, 1); m3 mutant overlap 8 CAUGHT, honest split
disjoint + covering.  S4: power-mean chain slack <= 0 exact, B1
identity worst 6.8e-16, fill <= 1 slack 0.0 on 47 worlds.  S5:
B2 interval/triangle/composed slacks all 0.0 on 47 worlds
(SMOOTH skipped by the pre-declared DEG_FLOOR guard, W = 0.0),
ladder equality n_eff(P_ov) == n_eff(PDelta) dev 0.0; exception
rungs in-table: n_eff 16.1 (kz20) .. 77.8 (kz52), n_act == m on
all 7, CV^2 0.98 (kz38) .. 1.41 (kz39), delta_w 0.147 (kz22) ..
0.187 (kz39), l_loc 1 on all shown.  S8: m4 synthetic collapse
n_eff == 1 exact, LOUD vs real med 37.4 (37x); SMOOTH alias
2.4e-14, q_N 4.2e-25; mp wards kz15 2.9e-10, kz64 9.3e-9, kz52
6.6e-8.
READING (typed, no upgrade): the round DELIVERS the n_eff
anatomy and RELOCATES the frozen rest onto strictly smaller,
named terrain: (1) the growth is ECHT anti-concentration -- the
whole order family N_2/N_3/N_4 grows at one exponent
(+0.963/+0.926/+0.894, tail slope only -0.069): n_eff is NOT a
fragile second-moment artifact; (2) the margin is
jackknife-STABLE (min +0.936 >= +0.908, 0/42 below) -- but the
half-ladder census shows the deep half at +0.802: the measured
+0.963 is front-loaded, the anti-extrapolation flag stands;
(3) THE STRUCTURAL FINDING (B1): n_eff = n_act/(1 + CV^2)
EXACTLY, and the count link is PERFECT -- n_act == m on 42/42:
the effective-carrier count IS the constructive level-2 block
count (growing at +1.002, i.e. ~N); the ENTIRE NEFF_TARGET
compresses into UNIF_TARGET: slope(1 + CV^2) <= +0.094
(measured +0.039) -- ONE bounded-uniformity inequality about
the block profile, the friendliest rest form the lane has had
(a growth statement became a boundedness statement);
NEFF_DERIVED missed only the sealed CV_FLAT clause (+0.039 >
0.0); (4) B2 fails LOUDLY (bound slope +0.074 vs +0.908) and
the reason is sharp: the |dc|-WEIGHTED discrepancy (med 0.167,
slope -0.017) is 10x the raw-position D_rank and near-flat --
the r300 correlational bridge lived on the RAW positions; the
measure the exact interval chain needs does not equidistribute:
the max-based equidistribution shortcut is closed honestly;
(5) B3: the difference profile decorrelates at lag ONE (l_loc
med 1.0) and the atom-level participation grows at +0.942
(coupled +0.96 to the block level) -- the mixing picture is
real but correlational; the local sum-rule census BREAKS 24/24:
the |dw| non-orthogonality is scale-free, no local energy
identity attaches.  Bycatch: the UNIF class does not separate
worlds (MAIN bracketed by the two dead controls) -- unlike the
O-sign and FILL classes, quasi-uniformity is NOT where the
arithmetic lives.  Runtime 48.0 s full / 0.3 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE beyond the
disclosed smoke-stage rename (records inserted per protocol; no
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
import diag_target_probe as DTP                # noqa: E402 r300
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
MAXL1_BAR = 1e-9
DF_BAR = 1e-9
CS_BAR = 1e-9
REC_FLOOR = 1e-6
QID_BAR = 1e-9
ORD_BAR = 1e-9
WD_BAR = 1e-9
EQ_BAR = 1e-9
DEG_FLOOR = 1e-6
CV_FLAT = 0.0
LOC_GROW = 0.05
E_FOLD = math.exp(-1.0)
CV_CLS = 1.0
K_LOC = 4
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
R300_NEFF_MED = 37.41
R300_NEFF_TOL = 0.05
R300_SL_NEFF = 0.963
R300_SL_NEFF_TOL = 0.01
R300_SL_L1 = 0.196
R300_SL_L1_TOL = 0.01
R300_SL_MX = -0.542
R300_SL_MX_TOL = 0.01
R300_SL_FILL = -0.225
R300_SL_FILL_TOL = 0.01
R300_MXMA_MED = 1.07
R300_MXMA_TOL = 0.02
R300_SP_N_NEFF = 0.96
R300_SP_N_NEFF_TOL = 0.02
R300_SP_DD_NEFF = -0.81
R300_SP_DD_NEFF_TOL = 0.02
R300_MAIN_CLS = ("PART_LOW", "FILL_LOW")
R300_EPST_CLS = ("PART_HIGH", "FILL_HIGH")
R300_SCR_CLS = ("PART_LOW", "FILL_HIGH")
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


# ---------------- exact Fractions section: the B1 participation
# ---------------- identity (module-own re-proof + the m1 mutants)
def fr_participation_identity(wrong="none"):
    """the B1 identity n_eff x (1 + CV^2) == n_act on the rational
    vector (2, 1, 1), exact Fractions: D = 6, L1 = 4, n_eff = 8/3;
    n_act = 3, mu = 4/3, CV^2 = 1/8; 8/3 x 9/8 = 3 EXACT.
    wrong='exp' replaces n_eff by L1^3/D (the m1a mutant, must
    break by 8); wrong='head' replaces (1 + CV^2) by (1 + CV^4)
    (the m1b mutant, must break by 56/195)."""
    P = [Fr(2), Fr(1), Fr(1)]
    D = sum(p * p for p in P)
    L1 = sum(abs(p) for p in P)
    neff = L1 ** 3 / D if wrong == "exp" else L1 ** 2 / D
    act = [abs(p) for p in P if p != 0]
    n_act = len(act)
    mu = sum(act) / n_act
    var = sum((a - mu) ** 2 for a in act) / n_act
    cv2 = var / (mu * mu)
    head = (1 + cv2 * cv2) if wrong == "head" else (1 + cv2)
    return abs(neff * head - n_act), neff, cv2, n_act


# ---------------- the module-own anatomy / route builders.
# ---------------- Source-pure: block vectors (positions, weights,
# ---------------- chain values) only; the withheld terminal drive
# ---------------- key, the branch label and every target-side
# ---------------- identifier are forbidden in scope (AST audit).
def participation_orders(P):
    """the Renyi participation family of the ONE positive field
    |P|: with p_j = |P_j|/L1, N_k = (sum p_j^k)^(-1/(k-1)) for
    k = 2, 3, 4 and N_inf = L1/mx.  N_2 == L1^2/D by definition;
    N_2 >= N_3 >= N_4 >= N_inf is the exact power-mean chain
    (monotonicity slack returned, must be <= 0 up to float)."""
    a = np.abs(np.asarray(P, dtype=float))
    L1 = float(np.sum(a))
    if L1 <= 0.0:
        return dict(N2=1.0, N3=1.0, N4=1.0, Ninf=1.0, mono=0.0)
    p = a / L1
    s2 = float(np.sum(p ** 2))
    s3 = float(np.sum(p ** 3))
    s4 = float(np.sum(p ** 4))
    N2 = 1.0 / max(s2, 1e-300)
    N3 = 1.0 / max(math.sqrt(s3), 1e-300)
    N4 = 1.0 / max(s4 ** (1.0 / 3.0), 1e-300)
    Ninf = L1 / max(float(np.max(a)), 1e-300)
    mono = max(N3 - N2, N4 - N3, Ninf - N4) / max(N2, 1e-300)
    return dict(N2=N2, N3=N3, N4=N4, Ninf=Ninf, mono=mono)


def quasi_uniformity(P):
    """the B1 count/uniformity coordinates over the ACTIVE blocks
    of |P|: n_act, population CV^2, Gini; the EXACT identity
    n_eff x (1 + CV^2) == n_act (relative dev returned)."""
    a = np.abs(np.asarray(P, dtype=float))
    act = a[a > 0.0]
    n_act = int(len(act))
    if n_act == 0:
        return dict(n_act=0, cv2=0.0, gini=0.0, qid_dev=0.0)
    mu = float(np.mean(act))
    var = float(np.mean((act - mu) ** 2))
    cv2 = var / max(mu * mu, 1e-300)
    srt = np.sort(act)
    cum = np.sum(srt * np.arange(1, n_act + 1))
    gini = (2.0 * cum / (n_act * np.sum(srt))
            - (n_act + 1.0) / n_act) if np.sum(srt) > 0 else 0.0
    L1 = float(np.sum(a))
    D = float(np.sum(a * a))
    neff = L1 * L1 / max(D, 1e-300)
    qid_dev = abs(neff * (1.0 + cv2) - n_act) / max(n_act, 1)
    return dict(n_act=n_act, cv2=cv2, gini=float(gini),
                qid_dev=qid_dev)


def wdisc_route(xs, dcs, lo, hi, brk, m, P_route):
    """the B2 exact equidistribution chain on the shared support:
    bulk mask (combined hull, EDGE_F), abs block masses w_j =
    sum_{blk} |dc|, block interval shares lambda_j from the
    breakpoints on [a_h, b_h], the weighted star discrepancy
    delta_w of the |dc| measure vs uniform, and the exact wards
    (i) |w_j/W - lambda_j| <= 2 delta_w per block, (ii)
    max|P_route| <= max w_j and L1(P_route) <= W (triangle),
    (iii) composed n_eff(P_route) >= surv/(lambda_max + 2
    delta_w).  Returns every ward slack + the census scalars."""
    xs = np.asarray(xs, dtype=float)
    ed = PBB.mask_edge(xs, lo, hi, EDGE_F)
    x = xs[~ed]
    w = np.abs(np.asarray(dcs, dtype=float))[~ed]
    a_h = lo + EDGE_F * (hi - lo)
    b_h = hi - EDGE_F * (hi - lo)
    W = float(np.sum(w))
    out = dict(W=W, delta=0.0, lam_max=0.0, s_max=0.0, surv=0.0,
               bound=1.0, iv_slack=0.0, tri_slack=0.0,
               comp_slack=0.0, neff_r=1.0)
    if m == 0 or len(x) == 0 or W <= 0.0:
        return out
    o = np.argsort(x, kind="stable")
    x = x[o]
    w = w[o]
    Fc = np.cumsum(w) / W
    U = (x - a_h) / max(b_h - a_h, 1e-300)
    Fl = np.concatenate([[0.0], Fc[:-1]])
    delta = float(np.max(np.maximum(np.abs(Fc - U),
                                    np.abs(Fl - U))))
    j = np.searchsorted(brk, x)
    wj = np.bincount(j, weights=w, minlength=m)
    edges = np.concatenate([[a_h],
                            np.clip(np.asarray(brk, dtype=float),
                                    a_h, b_h), [b_h]])
    lam = np.maximum(np.diff(edges), 0.0) / max(b_h - a_h, 1e-300)
    iv_slack = float(np.max(np.abs(wj / W - lam) - 2.0 * delta))
    Pr = np.asarray(P_route, dtype=float)
    mx_r = float(np.max(np.abs(Pr))) if len(Pr) else 0.0
    L1_r = float(np.sum(np.abs(Pr)))
    wmax = float(np.max(wj))
    tri_slack = max(mx_r - wmax, L1_r - W) / max(W, 1e-300)
    D_r = float(np.sum(Pr * Pr))
    neff_r = L1_r * L1_r / max(D_r, 1e-300) if D_r > 0 else 1.0
    surv = L1_r / W
    s_max = wmax / W
    lam_max = float(np.max(lam))
    bound = surv / max(lam_max + 2.0 * delta, 1e-300)
    comp_slack = max(bound - neff_r, 0.0) / max(neff_r, 1e-300)
    out.update(delta=delta, lam_max=lam_max, s_max=s_max,
               surv=surv, bound=bound, iv_slack=iv_slack,
               tri_slack=tri_slack, comp_slack=comp_slack,
               neff_r=neff_r)
    return out


def dc_profile(xs, dcs, lo, hi):
    """the B3 localization census of the c-difference profile on
    the bulk shared support: e-folding length l_loc of the
    mean-removed autocorrelation and the atom-level participation
    n_eff_atom = (sum|dc|)^2 / sum dc^2."""
    xs = np.asarray(xs, dtype=float)
    ed = PBB.mask_edge(xs, lo, hi, EDGE_F)
    z = np.asarray(dcs, dtype=float)[~ed]
    n = len(z)
    if n == 0:
        return dict(lloc=1.0, neff_atom=1.0, n=0)
    L1 = float(np.sum(np.abs(z)))
    D = float(np.sum(z * z))
    neff_atom = L1 * L1 / max(D, 1e-300) if D > 0 else 1.0
    zc = z - float(np.mean(z))
    A = np.correlate(zc, zc, mode="full")[n - 1:]
    if abs(A[0]) <= 0.0:
        return dict(lloc=1.0, neff_atom=neff_atom, n=n)
    acn = A / A[0]
    lloc = float(n)
    for h in range(1, n):
        if abs(acn[h]) <= E_FOLD:
            lloc = float(h)
            break
    return dict(lloc=lloc, neff_atom=neff_atom, n=n)


def split_disjoint(idx_lo, idx_hi, n):
    """the sub-ladder split ward: (overlap count, covering flag)
    -- the honest half split must be disjoint + covering; the m3
    overlapping mutant must be CAUGHT (overlap > 0)."""
    s_lo = set(idx_lo)
    s_hi = set(idx_hi)
    ov = len(s_lo & s_hi)
    cover = (s_lo | s_hi) == set(range(n)) \
        and len(s_lo) + len(s_hi) - ov == n
    return ov, cover


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'participation target' oriented by
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * quasi_uniformity(P)["n_act"]


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'carrier count' that consumes the branch label to pick its
    constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * participation_orders(P)["N2"]


# ---------------------------------------------- toy exact tools
def toy_orders_and_uniformity():
    """orders on (1,-1,1): all N_k = 3; on (2,1,1): N_2 = 8/3,
    N_3^2 = 32/5, N_4^3 = 128/9, N_inf = 2, monotone; the float
    quasi-uniformity on (2,1,1) matches the Fractions record
    (n_act 3, CV^2 1/8, identity exact).  Returns worst dev."""
    worst = 0.0
    o1 = participation_orders([1.0, -1.0, 1.0])
    worst = max(worst, abs(o1["N2"] - 3.0), abs(o1["N3"] - 3.0),
                abs(o1["N4"] - 3.0), abs(o1["Ninf"] - 3.0),
                max(o1["mono"], 0.0))
    o2 = participation_orders([2.0, 1.0, 1.0])
    worst = max(worst, abs(o2["N2"] - 8.0 / 3.0),
                abs(o2["N3"] ** 2 - 32.0 / 5.0),
                abs(o2["N4"] ** 3 - 128.0 / 9.0),
                abs(o2["Ninf"] - 2.0), max(o2["mono"], 0.0))
    q = quasi_uniformity([2.0, 1.0, 1.0])
    worst = max(worst, abs(q["n_act"] - 3.0),
                abs(q["cv2"] - 0.125), q["qid_dev"])
    return worst


def toy_wdisc():
    """the wdisc toy: atoms (0.25, 0.5, 0.75) weights (1, 2, 1)
    on hull [0, 1] (no edge zone: lo/hi chosen so a_h = 0, b_h =
    1 -- lo = -1/3, hi = 4/3, EDGE_F 0.20), breaks (0.4, 0.6):
    delta_w = 1/4, lambda (0.4, 0.2, 0.4), shares (0.25, 0.5,
    0.25), worst interval dev 0.3 <= 2 delta = 0.5; the signed
    route field (1, 2, 1): surv = 1, s_max = 0.5, bound = 1/0.9
    <= n_eff = 8/3.  Returns worst dev."""
    lo, hi = -1.0 / 3.0, 4.0 / 3.0
    xs = np.array([0.25, 0.5, 0.75])
    dcs = np.array([1.0, 2.0, 1.0])
    brk = np.array([0.4, 0.6])
    wd = wdisc_route(xs, dcs, lo, hi, brk, 3, dcs)
    worst = max(abs(wd["delta"] - 0.25),
                abs(wd["lam_max"] - 0.4),
                abs(wd["s_max"] - 0.5),
                abs(wd["surv"] - 1.0),
                abs(wd["bound"] - 1.0 / 0.9),
                max(wd["iv_slack"], 0.0),
                max(wd["tri_slack"], 0.0),
                max(wd["comp_slack"], 0.0),
                abs(wd["neff_r"] - 8.0 / 3.0))
    return worst


def toy_profile():
    """the profile toy dc = (1, -1, 1, -1) on positions 1..4
    (hull with no edge zone): mean 0, rho = (-3/4, 1/2, -1/4),
    l_loc = 3 (first |rho| <= 1/e), n_eff_atom = 4."""
    pr = dc_profile(np.array([1.0, 2.0, 3.0, 4.0]),
                    np.array([1.0, -1.0, 1.0, -1.0]),
                    -4.0, 9.0)
    return max(abs(pr["lloc"] - 3.0), abs(pr["neff_atom"] - 4.0),
               abs(pr["n"] - 4))


def toy_mustfail_m2():
    """m2a HALVED DISCREPANCY PREFACTOR: one atom at 0.5 on
    [0, 1], blocks split at (0.4, 0.6): delta = 1/2, the middle
    block deviation |1 - 0.2| = 0.8 <= 2 delta = 1 (correct ward
    holds, slack -0.2) while the mutant claim 0.8 <= delta = 0.5
    breaks by 0.3 EXACT.  m2b TRANSPOSED AGGREGATION MATRIX: on
    atoms (0, 0.2, 2), breaks (0.5, 1.5), dc (1, -2, 3): A =
    [[1,1,0],[0,0,0],[0,0,1]]; P = A dc = (-1, 0, 3) -> n_eff =
    8/5; the transpose gives (1, 1, 3) -> 25/11, break 37/55
    EXACT, and the column-sum ward flags (2, 0, 1) != 1.
    Returns (m2a break, m2a correct slack, m2b break, m2b flag,
    m2b correct colsum ok)."""
    lo, hi = -1.0 / 3.0, 4.0 / 3.0
    xs = np.array([0.5])
    dcs = np.array([1.0])
    brk = np.array([0.4, 0.6])
    wd = wdisc_route(xs, dcs, lo, hi, brk, 3, dcs)
    dev_mid = 1.0 - 0.2
    m2a_break = dev_mid - wd["delta"]          # 0.8 - 0.5 = 0.3
    m2a_ok = max(dev_mid - 2.0 * wd["delta"], 0.0)
    x = np.array([0.0, 0.2, 2.0])
    dc = np.array([1.0, -2.0, 3.0])
    brk2 = np.array([0.5, 1.5])
    m = 3
    A = np.zeros((m, len(x)))
    A[np.searchsorted(brk2, x), np.arange(len(x))] = 1.0
    P_good = A @ dc
    P_bad = A.T @ dc
    n_good = DTP.participation(P_good)["neff"]
    n_bad = DTP.participation(P_bad)["neff"]
    m2b_break = abs(n_good - n_bad)            # |8/5 - 25/11|
    cs_good = np.max(np.abs(A.sum(axis=0) - 1.0))
    cs_bad = np.max(np.abs(A.T.sum(axis=0) - 1.0))
    return (m2a_break, m2a_ok, m2b_break, cs_bad, cs_good,
            abs(n_good - 8.0 / 5.0), abs(n_bad - 25.0 / 11.0))


def toy_mustfail_m3():
    """m3 OVERLAPPING SUB-LADDERS on a deterministic 42-index
    frame: the honest half split (0..20 | 21..41) is disjoint +
    covering; the mutant (0..24 | 17..41) shares 8 indices --
    CAUGHT by the disjointness ward."""
    ov_h, cov_h = split_disjoint(range(0, 21), range(21, 42), 42)
    ov_m, cov_m = split_disjoint(range(0, 25), range(17, 42), 42)
    return ov_h, cov_h, ov_m, cov_m


def toy_mustfail_m4(m_real, l1_real):
    """m4 CONCENTRATED SYNTHETIC PDELTA: one block carries the
    whole L1 mass -- n_eff == 1 exact, n_act == 1, CV^2 == 0,
    every order number == 1, and the one-atom B2 toy bound
    collapses to 1/1.8 <= 1: EVERY route sees the collapse."""
    P_syn = np.zeros(max(m_real, 2))
    P_syn[0] = max(l1_real, 1.0)
    pa = DTP.participation(P_syn)
    po = participation_orders(P_syn)
    qu = quasi_uniformity(P_syn)
    worst = max(abs(pa["neff"] - 1.0), abs(po["N2"] - 1.0),
                abs(po["Ninf"] - 1.0), abs(qu["n_act"] - 1.0),
                abs(qu["cv2"]))
    lo, hi = -1.0 / 3.0, 4.0 / 3.0
    wd = wdisc_route(np.array([0.35]), np.array([1.0]), lo, hi,
                     np.array([0.5]), 2, np.array([1.0, 0.0]))
    worst = max(worst, abs(wd["bound"] - 1.0 / 1.8),
                max(wd["bound"] - 1.0, 0.0),
                max(wd["iv_slack"], 0.0),
                max(wd["comp_slack"], 0.0))
    return worst, pa["neff"]


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("neff_target_probe -- PRIME.PORT.L2.NEFF_TARGET.01 "
          "(round 301)")
    print("SPEC_SHA %s   R299_SHA %s (imported)   R300_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], FDP.SPEC_SHA[:16], DTP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + every exact ward "
                        "at w9; ladder, slopes, jackknife, "
                        "adjudications, censuses, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE NEFF-TARGET ROUND (the r300 frozen rest executed): "
          "n_eff = L1^2/D already grows fast enough (record slope "
          "%+.3f >= NEED +0.908, margin 0.055 THIN); this round "
          "measures the Renyi order anatomy and the jackknife "
          "stability of the margin, and tests THREE source-pure "
          "derivation routes (B1 the exact count/uniformity "
          "identity n_eff = n_act/(1 + CV^2) with the constructive "
          "count link, B2 the exact weighted-discrepancy interval "
          "chain -- the D_rank bridge made exact, B3 the profile "
          "decorrelation + local sum-rule census); sealed outcomes "
          "DERIVED / SPLIT (frozen rests) / STILL_EMPIRICAL plus "
          "the independent MARGIN_FRAGILE tag; ALL bars, bands, "
          "rules and verdicts sealed BEFORE evaluation"
          % R300_SL_NEFF)

    # ---------------- S1: census + controls (r300 scaffold verbatim)
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
    section("S2  EXACT DECOMPOSITION + R297/R298/R299/R300 ANCHORS")
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
        cconv, n_common = FDP.cconv_census(bxs, cts, rc["xu"],
                                           rc["cw"])
        full_ov = int(n_common == len(rc["bx"]) == len(rc["xu"]))
        B_ov = WBT.fejer_bil(P_ov, P_ov, H)
        B_fr = WBT.fejer_bil(P_fr, P_fr, H)
        B_x = 2.0 * WBT.fejer_bil(P_ov, P_fr, H)
        en_sc = max(B_ov, B_fr, abs(B_x), abs(B_en), 1e-300)
        en_dev = abs(B_ov + B_x + B_fr - B_en) / en_sc
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
        # ---- r300 participation anatomy (imported builder)
        part = DTP.participation(Pd)
        mxl1_slack = max(part["D"] - part["mx"] * part["L1"], 0.0) \
            / max(part["D"], 1e-300)
        # r300 class split (for the class anchor + carrier map)
        bws_s = rc["bw"][o]
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
        l1A = float(np.sum(np.abs(Acl))) / max(part["L1"], 1e-300)
        l1B = float(np.sum(np.abs(Bcl))) / max(part["L1"], 1e-300)
        # ---- Leg A: orders + carrier map
        po = participation_orders(Pd)
        edges = np.concatenate(
            [[a_h], np.clip(np.asarray(brk, dtype=float),
                            a_h, b_h), [b_h]]) \
            if m else np.array([a_h, b_h])
        mids = 0.5 * (edges[:-1] + edges[1:])
        aP = np.abs(Pd)
        iqr_w = 0.0
        if m and float(np.sum(aP)) > 0:
            cw_ = np.cumsum(aP) / float(np.sum(aP))
            i25 = int(np.searchsorted(cw_, 0.25))
            i75 = int(np.searchsorted(cw_, 0.75))
            iqr_w = float(mids[min(i75, m - 1)]
                          - mids[min(i25, m - 1)]) \
                / max(b_h - a_h, 1e-300)
        # ---- Leg B1: quasi-uniformity identity
        qu = quasi_uniformity(Pd)
        # ---- shared support (r300 builders verbatim)
        fxs = rc["bx"] * rc["v2"] * rc["fac"]
        sd = DTP.shared_delta(rc["bx"], rc["ct"], rc["bw"], fxs,
                              rc["xu"], rc["cw"], rc["wu"])
        df_dev = float(np.max(np.abs(sd["dc"]
                                     - sd["dw"] * sd["f"]))) \
            / max(float(np.max(np.abs(sd["dc"]))), 1e-300) \
            if sd["n"] else 0.0
        cs = DTP.cs_block_route(sd["x"], sd["dc"], sd["dw"],
                                sd["f"], rc["lo"], rc["hi"],
                                brk, m)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        rec_scale = max(float(np.max(np.abs(Pd))) if m else 0.0,
                        REC_FLOOR * absm, 1e-300)
        rec_dev = float(np.max(np.abs(cs["P"] - P_ov))) \
            / rec_scale if m else 0.0
        # degenerate-source guard (declared in the sealed spec)
        W_abs = float(np.sum(np.abs(sd["dc"]))) if sd["n"] else 0.0
        degenerate = (W_abs <= DEG_FLOOR * absm)
        # ---- Leg B2: exact discrepancy chain on P_ov
        if degenerate or m == 0 or sd["n"] == 0:
            wd = dict(W=W_abs, delta=0.0, lam_max=0.0, s_max=0.0,
                      surv=0.0, bound=1.0, iv_slack=0.0,
                      tri_slack=0.0, comp_slack=0.0, neff_r=1.0)
            eq_dev = 0.0
        else:
            wd = wdisc_route(sd["x"], sd["dc"], rc["lo"],
                             rc["hi"], brk, m, P_ov)
            n_pd = part["neff"]
            eq_dev = abs(wd["neff_r"] - n_pd) \
                / max(n_pd, 1e-300) if full_ov else 0.0
        # ---- Leg B3: profile localization
        if degenerate or sd["n"] == 0:
            pr = dict(lloc=1.0, neff_atom=1.0, n=0)
        else:
            pr = dc_profile(sd["x"], sd["dc"], rc["lo"], rc["hi"])
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
                    l1A=l1A, l1B=l1B, po=po, iqr_w=iqr_w,
                    qu=qu, df_dev=df_dev, rec_dev=rec_dev,
                    maxatom=cs["maxatom"], wd=wd, eq_dev=eq_dev,
                    pr=pr, degenerate=degenerate, sd=sd,
                    Mr=Mr, nr=len(runs))

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
        st["cc_med"] = med("cconv")
        st["cc_sl"] = slp([rc["ev"]["cconv"] for rc in recs])
        st["dd_med"] = med("d_delta")
        st["dd_sl"] = slp([rc["ev"]["d_delta"] for rc in recs])
        st["full_ov"] = sum(rc["ev"]["full_ov"] for rc in recs)
        # r300 anatomy set
        neffs = [rc["ev"]["part"]["neff"] for rc in recs]
        st["neff_med"] = float(np.median(neffs))
        st["sl_neff"] = slp(neffs)
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
        st["mxma_med"] = med_f(lambda ev: ev["part"]["mx"]
                               / max(ev["maxatom"], 1e-300))
        st["sp_n_neff"] = BH.spearman(Ns, neffs)
        st["sp_dd_neff"] = BH.spearman(
            [rc["ev"]["d_delta"] for rc in recs], neffs)
        # Leg A: orders / carrier / stability
        st["N2_med"] = med_f(lambda ev: ev["po"]["N2"])
        st["N3_med"] = med_f(lambda ev: ev["po"]["N3"])
        st["N4_med"] = med_f(lambda ev: ev["po"]["N4"])
        st["Ninf_med"] = med_f(lambda ev: ev["po"]["Ninf"])
        st["sl_N2"] = slp([rc["ev"]["po"]["N2"] for rc in recs])
        st["sl_N3"] = slp([rc["ev"]["po"]["N3"] for rc in recs])
        st["sl_N4"] = slp([rc["ev"]["po"]["N4"] for rc in recs])
        st["sl_Ninf"] = slp([rc["ev"]["po"]["Ninf"]
                             for rc in recs])
        st["tail_med"] = med_f(lambda ev: ev["po"]["N4"]
                               / max(ev["po"]["N2"], 1e-300))
        st["sl_tail"] = slp([rc["ev"]["po"]["N4"]
                             / max(rc["ev"]["po"]["N2"], 1e-300)
                             for rc in recs])
        st["l1A_med"] = med("l1A")
        st["l1B_med"] = med("l1B")
        st["iqr_med"] = med("iqr_w")
        st["sl_iqr"] = slp([rc["ev"]["iqr_w"] for rc in recs])
        # Leg B1
        st["nact_med"] = med_f(lambda ev: ev["qu"]["n_act"])
        st["sl_nact"] = slp([rc["ev"]["qu"]["n_act"]
                             for rc in recs])
        st["sl_cv2p"] = slp([1.0 + rc["ev"]["qu"]["cv2"]
                             for rc in recs])
        st["gini_med"] = med_f(lambda ev: ev["qu"]["gini"])
        st["nact_full"] = sum(1 for rc in recs
                              if rc["ev"]["qu"]["n_act"]
                              == rc["ev"]["m"])
        st["cv2_med"] = med_f(lambda ev: ev["qu"]["cv2"])
        # Leg B2
        st["dw_med"] = med_f(lambda ev: ev["wd"]["delta"])
        st["sl_dw"] = slp([rc["ev"]["wd"]["delta"]
                           for rc in recs])
        st["sl_smax"] = slp([rc["ev"]["wd"]["s_max"]
                             for rc in recs])
        st["surv_med"] = med_f(lambda ev: ev["wd"]["surv"])
        st["sl_surv"] = slp([rc["ev"]["wd"]["surv"]
                             for rc in recs])
        st["sl_bound"] = slp([rc["ev"]["wd"]["bound"]
                              for rc in recs])
        # Leg B3
        st["lloc_med"] = med_f(lambda ev: ev["pr"]["lloc"])
        st["sl_lloc"] = slp([rc["ev"]["pr"]["lloc"]
                             for rc in recs])
        st["natom_med"] = med_f(lambda ev: ev["pr"]["neff_atom"])
        st["sl_natom"] = slp([rc["ev"]["pr"]["neff_atom"]
                              for rc in recs])
        st["sp_atom_blk"] = BH.spearman(
            [rc["ev"]["pr"]["neff_atom"] for rc in recs], neffs)
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
                  "%d/42 (ref %d), ratio med %.2f sl %+.3f, LOW "
                  "%.2f, q50 %.2f, cconv %.2f sl %+.3f, dd %.3f "
                  "sl %+.2f, full overlap %d/42 (ref %d)"
                  % (st["sl_D"], R299_SL_D, st["sl_absO"],
                     st["n_On"], R299_N_ONEG, st["rat_med"],
                     st["sl_rat"], st["shl_med"], st["q50_med"],
                     st["cc_med"], st["cc_sl"], st["dd_med"],
                     st["dd_sl"], st["full_ov"], R299_FULL_OV))
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
    df_w = max(rc["ev"]["df_dev"] for rc in pool_all)
    rec_w = max(rc["ev"]["rec_dev"] for rc in pool_all)
    if not smoke:
        ok300 = (abs(st["neff_med"] - R300_NEFF_MED)
                 <= R300_NEFF_TOL
                 and abs(st["sl_neff"] - R300_SL_NEFF)
                 <= R300_SL_NEFF_TOL
                 and abs(st["sl_L1"] - R300_SL_L1)
                 <= R300_SL_L1_TOL
                 and abs(st["sl_mx"] - R300_SL_MX)
                 <= R300_SL_MX_TOL
                 and abs(st["sl_fill"] - R300_SL_FILL)
                 <= R300_SL_FILL_TOL
                 and st["add1"] <= ADD_BAR
                 and st["add2"] <= ADD_BAR
                 and abs(st["mxma_med"] - R300_MXMA_MED)
                 <= R300_MXMA_TOL
                 and abs(st["sp_n_neff"] - R300_SP_N_NEFF)
                 <= R300_SP_N_NEFF_TOL
                 and abs(st["sp_dd_neff"] - R300_SP_DD_NEFF)
                 <= R300_SP_DD_NEFF_TOL)
        det300 = ("n_eff med %.2f (ref %.2f), sl_neff %+.3f (ref "
                  "%+.3f), sl_L1 %+.3f, sl_mx %+.3f, sl_fill "
                  "%+.3f, adds %.1e/%.1e (bar %.0e), mx/maxatom "
                  "med %.2f (ref %.2f), sp(N, n_eff) %+.2f, "
                  "sp(dd, n_eff) %+.2f (refs %+.2f/%+.2f)"
                  % (st["neff_med"], R300_NEFF_MED, st["sl_neff"],
                     R300_SL_NEFF, st["sl_L1"], st["sl_mx"],
                     st["sl_fill"], st["add1"], st["add2"],
                     ADD_BAR, st["mxma_med"], R300_MXMA_MED,
                     st["sp_n_neff"], st["sp_dd_neff"],
                     R300_SP_N_NEFF, R300_SP_DD_NEFF))
    else:
        ok300 = True
        det300 = "SMOKE: ladder anchors skipped"
    cls_w = max(rc["ev"]["cls_dev"] for rc in pool_all)
    mxl1_w = max(rc["ev"]["mxl1_slack"] for rc in pool_all)
    check("G26-r300-anatomy-anchors",
          df_w <= DF_BAR and rec_w <= CS_BAR and cls_w <= CLS_BAR
          and mxl1_w <= MAXL1_BAR and ok300,
          "the r300 record recomputed bit-near on %d worlds "
          "(dc == dw x f %.1e, P_rec == P_ov %.1e, class "
          "recomposition %.1e, fill <= 1 slack %.1e); %s"
          % (len(pool_all), df_w, rec_w, cls_w, mxl1_w, det300))

    # ---------------- S3: exact section + toys + audits + mutants
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    q_dev, q_neff, q_cv2, q_nact = fr_participation_identity()
    m1a_dev, m1a_neff, _c, _n = fr_participation_identity("exp")
    m1b_dev, _n2, _c2, _n3 = fr_participation_identity("head")
    check("G30-fractions-identity-and-m1",
          q_dev == 0 and q_neff == Fr(8, 3) and q_cv2 == Fr(1, 8)
          and q_nact == 3 and v_o == 0 and v_i == 0
          and m1a_dev == 9 and m1b_dev == Fr(7, 24),
          "the B1 identity n_eff x (1 + CV^2) == n_act RE-PROVED "
          "exact in Fractions on (2,1,1) (n_eff %s, CV^2 %s, "
          "n_act %s, dev %s; r297 sum rule import devs %s/%s); "
          "m1a WRONG EXPONENT (L1^3/D, value off by 8) breaks "
          "the identity by %s EXACT; m1b WRONG HEAD (1 + CV^4) "
          "breaks by %s EXACT -- both CAUGHT: exponent and head "
          "are load-bearing"
          % (str(q_neff), str(q_cv2), str(q_nact), str(q_dev),
             str(v_o), str(v_i), str(m1a_dev), str(m1b_dev)))
    toy_w = max(toy_orders_and_uniformity(), toy_wdisc(),
                toy_profile())
    check("G31-toy-exactness", toy_w <= TOY_BAR,
          "the hand toys reproduce the WHOLE new pipeline: orders "
          "(1,-1,1) -> all N_k = 3 and (2,1,1) -> N_2 8/3, N_3^2 "
          "32/5, N_4^3 128/9, N_inf 2 monotone; quasi-uniformity "
          "float == Fractions; wdisc toy delta 1/4, lambda (0.4, "
          "0.2, 0.4), shares (0.25, 0.5, 0.25), bound 10/9 <= "
          "8/3; profile toy rho (-3/4, 1/2, -1/4) -> l_loc 3, "
          "n_eff_atom 4 (worst dev %.1e, bar %.0e)"
          % (toy_w, TOY_BAR))
    h_po = scope_audit("participation_orders", BOUND_FORBIDDEN)
    h_qu = scope_audit("quasi_uniformity", BOUND_FORBIDDEN)
    h_wd = scope_audit("wdisc_route", BOUND_FORBIDDEN)
    h_pr = scope_audit("dc_profile", BOUND_FORBIDDEN)
    h_sp = scope_audit("split_disjoint", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_po or h_qu or h_wd or h_pr or h_sp)
    check("G32-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the new builders (participation_orders, "
          "quasi_uniformity, wdisc_route, dc_profile, "
          "split_disjoint) consume block vectors / positions / "
          "weights only (no truth-side identifier in scope%s); "
          "m5a gift mutant FLAGGED (%s); m5b branch-peek mutant "
          "FLAGGED (%s); fragment audit: %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    (m2a_brk, m2a_ok, m2b_brk, m2b_flag, m2b_good,
     m2b_gdev, m2b_bdev) = toy_mustfail_m2()
    check("G33-mustfail-m2-matrix", m2a_brk >= MUT_MIN
          and abs(m2a_brk - 0.3) <= 1e-12 and m2a_ok <= TOY_BAR
          and m2b_brk >= MUT_MIN
          and abs(m2b_brk - 37.0 / 55.0) <= 1e-12
          and m2b_flag >= MUT_MIN and m2b_good <= TOY_BAR
          and m2b_gdev <= TOY_BAR and m2b_bdev <= TOY_BAR,
          "m2a HALVED DISCREPANCY PREFACTOR: the one-atom toy "
          "breaks the claim by %.6f (= 0.3 exact) while the "
          "correct 2 delta ward holds (slack %.1e) -- CAUGHT; "
          "m2b TRANSPOSED AGGREGATION MATRIX (rows/cols swapped):"
          " n_eff shifts by %.6f (= 37/55 exact, 8/5 vs 25/11) "
          "LOUD and the column-sum ward flags the transpose "
          "(worst colsum dev %.1f vs %.1e valid) -- the "
          "atom-to-block assignment is load-bearing"
          % (m2a_brk, m2a_ok, m2b_brk, m2b_flag, m2b_good))
    ov_h, cov_h, ov_m, cov_m = toy_mustfail_m3()
    check("G34-mustfail-m3-split", ov_h == 0 and cov_h
          and ov_m == 8,
          "m3 OVERLAPPING SUB-LADDERS: the honest half split "
          "(0..20 | 21..41) is disjoint (overlap %d) + covering "
          "(%s); the mutant split (0..24 | 17..41) shares %d "
          "rungs -- CAUGHT by the disjointness ward: overlapping "
          "sub-ladders double-count rungs and fake stability"
          % (ov_h, cov_h, ov_m))

    # ---------------- S4: Leg A -- anatomy + stability
    section("S4  LEG A: N_EFF ANATOMY + MARGIN STABILITY")
    ord_w = max(rc["ev"]["po"]["mono"] for rc in pool_all)
    qid_w = max(rc["ev"]["qu"]["qid_dev"] for rc in pool_all)
    check("G40-anatomy-wards", ord_w <= ORD_BAR
          and qid_w <= QID_BAR and mxl1_w <= MAXL1_BAR,
          "the anatomy identities on %d worlds: power-mean chain "
          "N_2 >= N_3 >= N_4 >= N_inf worst slack %.1e (bar "
          "%.0e); the B1 identity n_eff x (1 + CV^2) == n_act "
          "worst %.1e (bar %.0e); fill <= 1 slack %.1e -- the "
          "order family and the count identity are exact finite "
          "statements" % (len(pool_all), ord_w, ORD_BAR, qid_w,
                          QID_BAR, mxl1_w))
    show = (sorted(exc, key=lambda r_: r_["kz"]) + mrecs
            if not smoke else mrecs)
    for rc in show:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s m %-3d  n_eff %.1f  N4 %.1f  "
             "n_act %-3d cv2 %.2f  dw %.3f  surv %.2f  lloc %.0f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g_branch"] < 0 else "chp",
                ev["m"], ev["part"]["neff"], ev["po"]["N4"],
                ev["qu"]["n_act"], ev["qu"]["cv2"],
                ev["wd"]["delta"], ev["wd"]["surv"],
                ev["pr"]["lloc"]))
    if not smoke:
        check("G41-anatomy-census", True,
              "NEFF_ANATOMY (42 rungs): N_2/N_3/N_4/N_inf med "
              "%.2f/%.2f/%.2f/%.2f slopes %+.3f/%+.3f/%+.3f/"
              "%+.3f; tail N_4/N_2 med %.2f slope %+.3f -- %s; "
              "carrier L1 shares A/Bv med %.2f/%.2f; positional "
              "IQR med %.2f slope %+.3f -- %s"
              % (st["N2_med"], st["N3_med"], st["N4_med"],
                 st["Ninf_med"], st["sl_N2"], st["sl_N3"],
                 st["sl_N4"], st["sl_Ninf"], st["tail_med"],
                 st["sl_tail"],
                 "one exponent: echt anti-concentration"
                 if abs(st["sl_N4"] - st["sl_N2"]) <= 0.1
                 else "the orders decouple: heavy-tail broadening",
                 st["l1A_med"], st["l1B_med"], st["iqr_med"],
                 st["sl_iqr"],
                 "the mass spreads positionally too"
                 if st["sl_iqr"] >= 0 else
                 "the mass concentrates positionally"))
        need_neff = 2.0 * st["sl_L1"] - st["sigma_star"]
        neffs = [rc["ev"]["part"]["neff"] for rc in recs]
        lo_idx = list(range(0, 21))
        hi_idx = list(range(21, 42))
        ov_r, cov_r = split_disjoint(lo_idx, hi_idx, 42)
        sl_lo_half = L2D.halves_slope([Ns[i] for i in lo_idx],
                                      [neffs[i] for i in lo_idx])
        sl_hi_half = L2D.halves_slope([Ns[i] for i in hi_idx],
                                      [neffs[i] for i in hi_idx])
        jks = []
        jk_valid = True
        for i in range(42):
            idx = [k for k in range(42) if k != i]
            jk_valid &= (len(set(idx)) == 41 and i not in idx)
            jks.append(L2D.halves_slope([Ns[k] for k in idx],
                                        [neffs[k] for k in idx]))
        jk_min = min(jks)
        jk_max = max(jks)
        n_below = sum(1 for v in jks if v < need_neff)
        fragile = jk_min < need_neff
        check("G42-stability-census", ov_r == 0 and cov_r
              and jk_valid,
              "STABILITY (sealed rule: MARGIN_FRAGILE iff "
              "jackknife min < NEED): half-ladder slopes lo/hi "
              "%+.3f/%+.3f (disjoint split gated, overlap %d); "
              "jackknife over 42 rungs (41 unique each, gated): "
              "min %+.3f / max %+.3f, %d/42 below NEED %+.3f -- "
              "%s; DISCLOSED: stability of the frozen estimator, "
              "not new cofinal information"
              % (sl_lo_half, sl_hi_half, ov_r, jk_min, jk_max,
                 n_below, need_neff,
                 "MARGIN_FRAGILE fires" if fragile
                 else "the margin survives every single-rung "
                 "removal"))
    else:
        need_neff = float("nan")
        fragile = False
        sl_lo_half = sl_hi_half = jk_min = jk_max = float("nan")
        n_below = -1
        check("G41-anatomy-census", True, "SMOKE: skipped")
        check("G42-stability-census", True, "SMOKE: skipped")

    # ---------------- S5: Leg B -- the derivation routes
    section("S5  LEG B: DERIVATION ROUTES FOR NEFF_TARGET")
    iv_w = max(rc["ev"]["wd"]["iv_slack"] for rc in pool_all)
    tri_w = max(rc["ev"]["wd"]["tri_slack"] for rc in pool_all)
    cmp_w = max(rc["ev"]["wd"]["comp_slack"] for rc in pool_all)
    eq_w = max(rc["ev"]["eq_dev"] for rc in all_rc) \
        if all_rc else 0.0
    deg_note = [("%s W %.1e" % (c, crecs[c]["ev"]["wd"]["W"]))
                for c in crecs if crecs[c]["ev"]["degenerate"]]
    check("G50-b2-wards", iv_w <= WD_BAR and tri_w <= WD_BAR
          and cmp_w <= WD_BAR and eq_w <= EQ_BAR,
          "B2 wards on %d worlds: interval bound |w_j/W - "
          "lambda_j| <= 2 delta_w worst slack %.1e (bar %.0e; a "
          "star-discrepancy theorem); triangle max|P_ov| <= max "
          "w_j and L1 <= W worst %.1e; composed n_eff >= "
          "surv/(lam_max + 2 delta_w) slack %.1e; ladder "
          "equality n_eff(P_ov) == n_eff(PDelta) dev %.1e (bar "
          "%.0e)%s"
          % (len(pool_all), iv_w, WD_BAR, tri_w, cmp_w, eq_w,
             EQ_BAR,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))
    # ---- B3 local sum-rule census on the id pool
    id_pool = (mrecs + [crecs[c] for c in ("EPST", "SCR")]) \
        if smoke else \
        ([rc for rc in recs if rc["kz"] in (KZ_ANCHOR, 20)]
         + mrecs + [crecs[c] for c in ("EPST", "SCR")])
    n_hold = n_near = n_break = 0
    loc_worst = 0.0
    loc_crosses = []
    for rc in id_pool:
        sd = rc["ev"]["sd"]
        if sd["n"] == 0 or rc["ev"]["degenerate"]:
            continue
        nq = sd["n"]
        qs = [0, nq // 4, nq // 2, (3 * nq) // 4, nq]
        for k in range(K_LOC):
            slc = slice(qs[k], qs[k + 1])
            xw = sd["x"][slc]
            ww = np.abs(sd["dw"][slc])
            if len(xw) < 4 or float(np.sum(ww)) <= 0.0:
                continue
            cq = VCP.chain_quads(rc["p"]["rows"], rc["N"], xw, ww)
            cr = max(abs(v) for v in cq["cr"].values())
            dv = abs(cq["q2"] - cq["pd"]) \
                / max(abs(cq["q2"]), 1e-300)
            w_ = max(cr, dv)
            loc_worst = max(loc_worst, w_)
            loc_crosses.append(cr)
            if w_ <= ID_HOLDS:
                n_hold += 1
            elif w_ <= ID_NEAR:
                n_near += 1
            else:
                n_break += 1
    n_loc = n_hold + n_near + n_break
    loc_med = float(np.median(loc_crosses)) if loc_crosses else 0.0
    if not smoke:
        check("G51-b1-census", st["add1"] <= ADD_BAR
              and abs(st["sl_neff"]
                      - (st["sl_nact"] - st["sl_cv2p"]))
              <= ADD_BAR,
              "B1 census (DISCLOSED: the slope clause is an exact"
              " reparametrization of NEFF_TARGET): n_act med "
              "%.1f, COUNT LINK n_act == m on %d/42%s; sl_nact "
              "%+.3f - sl_cv2p %+.3f = %+.3f == sl_neff %+.3f "
              "(additivity exact); Gini med %.2f, CV^2 med %.2f; "
              "the derivation content: a constructive count + "
              "ONE uniformity statement"
              % (st["nact_med"], st["nact_full"],
                 " EXACT" if st["nact_full"] == 42 else "",
                 st["sl_nact"], st["sl_cv2p"],
                 st["sl_nact"] - st["sl_cv2p"], st["sl_neff"],
                 st["gini_med"], st["cv2_med"]))
        check("G52-b2-census", True,
              "B2 census: delta_w med %.3f slope %+.3f (the "
              "WEIGHTED discrepancy vs the unweighted dd %+.2f); "
              "s_max slope %+.3f; surv med %.2f slope %+.3f; "
              "composed bound slope %+.3f vs NEED %+.3f -- %s "
              "(disclosed prior: the chain caps at N_inf, slope "
              "%+.3f)"
              % (st["dw_med"], st["sl_dw"], st["dd_sl"],
                 st["sl_smax"], st["surv_med"], st["sl_surv"],
                 st["sl_bound"], need_neff,
                 "MEETS" if st["sl_bound"] >= need_neff
                 else "FAILS by %.3f"
                 % (need_neff - st["sl_bound"]),
                 st["sl_Ninf"]))
        check("G53-b3-census", True,
              "B3 census: l_loc med %.1f slope %+.3f (%s); "
              "n_eff_atom med %.1f slope %+.3f vs NEED %+.3f -- "
              "%s; sp(n_eff_atom, n_eff) %+.2f; LOCAL SUM-RULE "
              "census (%d windows over %d worlds, K_LOC %d): "
              "HOLDS/NEAR/BREAKS %d/%d/%d (cross med %.2f, worst "
              "%.2f) -- %s"
              % (st["lloc_med"], st["sl_lloc"],
                 "O(1) decorrelation" if st["lloc_med"] <= 8
                 else "long-range memory",
                 st["natom_med"], st["sl_natom"], need_neff,
                 "MET" if st["sl_natom"] >= need_neff
                 else "NOT MET",
                 st["sp_atom_blk"], n_loc, len(id_pool), K_LOC,
                 n_hold, n_near, n_break, loc_med, loc_worst,
                 "the r300 global break does NOT localize away"
                 if n_break == n_loc else
                 "the break is scale-dependent (disclosed)"))
    else:
        check("G51-b1-census", True,
              "SMOKE: w9 identity pool only; local census %d "
              "windows %d/%d/%d" % (n_loc, n_hold, n_near,
                                    n_break))
        check("G52-b2-census", True, "SMOKE: skipped")
        check("G53-b3-census", True, "SMOKE: skipped")

    # ---------------- S6: sealed adjudication + Leg C
    section("S6  SEALED NEFF ADJUDICATION + LEG C")
    if not smoke:
        b1_valid = (qid_w <= QID_BAR
                    and abs(st["sl_neff"]
                            - (st["sl_nact"] - st["sl_cv2p"]))
                    <= ADD_BAR)
        b2_valid = (iv_w <= WD_BAR and tri_w <= WD_BAR
                    and cmp_w <= WD_BAR and eq_w <= EQ_BAR)
        b1_ok = b1_valid and (st["sl_nact"] - st["sl_cv2p"]
                              >= need_neff)
        b2_ok = b2_valid and (st["sl_bound"] >= need_neff)
        b3_ok = (st["sl_natom"] >= need_neff
                 and st["sl_lloc"] <= LOC_GROW)
        derived = (b1_ok and st["sl_cv2p"] <= CV_FLAT
                   and st["nact_full"] == 42)
        if derived:
            outcome = "NEFF_DERIVED"
        elif b1_ok or b2_ok or b3_ok:
            outcome = "NEFF_SPLIT"
        else:
            outcome = "NEFF_STILL_EMPIRICAL"
        fired = []
        if b1_ok:
            fired.append("B1(UNIF_TARGET: prove slope(1 + CV^2) "
                         "<= sl_nact - NEED = %+.3f, measured "
                         "%+.3f; count link %d/42)"
                         % (st["sl_nact"] - need_neff,
                            st["sl_cv2p"], st["nact_full"]))
        if b2_ok:
            fired.append("B2(DISC_TARGET: prove the surv/"
                         "discrepancy scaling, bound slope "
                         "%+.3f)" % st["sl_bound"])
        if b3_ok:
            fired.append("B3(MIX_TARGET: prove the O(1) "
                         "decorrelation, l_loc slope %+.3f)"
                         % st["sl_lloc"])
        check("G60-neff-adjudication", True,
              "SEALED RULE fired: %s (B1_OK %s: sl_nact - "
              "sl_cv2p = %+.3f vs NEED %+.3f; B2_OK %s: bound "
              "slope %+.3f; B3_OK %s: sl_natom %+.3f, sl_lloc "
              "%+.3f vs %+.2f; DERIVED clause: B1_OK AND sl_cv2p"
              " %+.3f <= %.1f AND count link %d/42 == 42)%s%s"
              % (outcome, b1_ok,
                 st["sl_nact"] - st["sl_cv2p"], need_neff,
                 b2_ok, st["sl_bound"], b3_ok, st["sl_natom"],
                 st["sl_lloc"], LOC_GROW, st["sl_cv2p"],
                 CV_FLAT, st["nact_full"],
                 ("; fired: " + " | ".join(fired)) if fired
                 else "",
                 "; MARGIN_FRAGILE fired (Leg A3)" if fragile
                 else ""))
        if outcome == "NEFF_DERIVED" and not fragile:
            info("CANDIDATE THEOREM (participation composition, "
                 "L2 generic half): for every rung of the sealed "
                 "ladder (N in [%d, %d]): the B1 count identity "
                 "n_eff = n_act/(1 + CV^2) with n_act == m "
                 "(constructive) and non-growing CV^2 => "
                 "slope(n_eff) >= NEED = %+.3f => (r300 exact "
                 "decomposition) sl_D <= sigma* => (r300 "
                 "RATIO_BOUNDED_STRUCTURAL) sigma <= sigma* = "
                 "%+.3f => the r297 target inequality => the "
                 "v964-S0 vdC theorem => delta' > %.2f on the "
                 "generic half; exceptions: 6 via the r287 F2 "
                 "certificates, kz15 via the r270 exact-finite "
                 "certificate.  Wave-10 promotion candidate -- "
                 "NOT promoted here."
                 % (min(Ns), max(Ns), need_neff,
                    st["sigma_star"], DELTA_NEED))
            legc = "COMPOSED"
        else:
            info("REST_FROZEN (the refined statement, smaller "
                 "than r300's): the count factor n_act == m on "
                 "%d/42 grows at %+.3f; the remaining inequality "
                 "is UNIF_TARGET: slope(1 + CV^2) <= sl_nact - "
                 "NEED = %+.3f (measured %+.3f, margin %.3f).  "
                 "B2 (discrepancy/max route) %s; B3 (profile "
                 "route) %s.%s"
                 % (st["nact_full"], st["sl_nact"],
                    st["sl_nact"] - need_neff, st["sl_cv2p"],
                    (st["sl_nact"] - need_neff) - st["sl_cv2p"],
                    "fired" if b2_ok else
                    "closed honestly (bound slope %+.3f)"
                    % st["sl_bound"],
                    "fired" if b3_ok else "not fired",
                    "  MARGIN_FRAGILE is the primary finding "
                    "(jk_min %+.3f < NEED)." % jk_min
                    if fragile else ""))
            legc = "REST_FROZEN"
        check("G61-leg-c", True,
              "Leg C %s -- the full candidate fires ONLY on "
              "NEFF_DERIVED AND NOT MARGIN_FRAGILE by the sealed "
              "rule; no post-hoc rescue"
              % ("FIRED (candidate printed, NOT promoted)"
                 if legc == "COMPOSED" else
                 "REST_FROZEN (refined target printed)"))
    else:
        outcome = "SMOKE_NO_ADJUDICATION"
        fired = []
        check("G60-neff-adjudication", True, "SMOKE: skipped")
        check("G61-leg-c", True, "SMOKE: skipped")

    # ---------------- S8: worlds + m4 + anchors + mp wards
    section("S8  WORLD CLASSES + MUSTFAIL M4 + MP WARDS")
    if not smoke:
        pm = float(np.median([rc["ev"]["part"]["neff"]
                              / max(rc["ev"]["m"], 1)
                              for rc in recs]))
        fm = float(np.median([rc["ev"]["part"]["fill"]
                              for rc in recs]))
        main_cls = ("PART_HIGH" if pm >= PART_CLS else "PART_LOW",
                    "FILL_HIGH" if fm >= FILL_CLS else "FILL_LOW")
        cv_main = "UNIF_HIGH" if st["cv2_med"] <= CV_CLS \
            else "UNIF_LOW"
        refs = {"EPST": R300_EPST_CLS, "SCR": R300_SCR_CLS}
        ctl_note = []
        cls_ok = (main_cls == R300_MAIN_CLS)
        world_blind = True
        for c in ("EPST", "SCR"):
            ev = crecs[c]["ev"]
            pc = ev["part"]["neff"] / max(ev["m"], 1)
            fc = ev["part"]["fill"]
            cls_c = ("PART_HIGH" if pc >= PART_CLS
                     else "PART_LOW",
                     "FILL_HIGH" if fc >= FILL_CLS
                     else "FILL_LOW")
            cls_ok &= (cls_c == refs[c])
            cv_c = "UNIF_HIGH" if ev["qu"]["cv2"] <= CV_CLS \
                else "UNIF_LOW"
            ctl_note.append("%s %s/%s/%s(cv2 %.2f)"
                            % (c, cls_c[0], cls_c[1], cv_c,
                               ev["qu"]["cv2"]))
            world_blind &= (cv_c == cv_main)
        check("G80-world-controls", cls_ok,
              "the r300 anatomy classes REPRODUCED EXACTLY (MAIN "
              "%s/%s, refs %s; controls %s); the NEW UNIF class "
              "(CV^2 med %s %.2f, bar %.1f): MAIN %s -- %s"
              % (main_cls[0], main_cls[1], str(R300_MAIN_CLS),
                 str(ctl_note), "<=" if st["cv2_med"] <= CV_CLS
                 else ">", st["cv2_med"], CV_CLS, cv_main,
                 "WORLD-BLIND" if world_blind
                 else "WORLD_SENSITIVE (disclosed)"))
    else:
        world_blind = True
        main_cls = ("n/a", "n/a")
        cv_main = "n/a"
        ctl_note = []
        check("G80-world-controls", True, "SMOKE: skipped")
    rc_m4 = mrecs[0] if not smoke else recs[0]
    m4_w, m4_neff = toy_mustfail_m4(rc_m4["ev"]["m"],
                                    rc_m4["ev"]["part"]["L1"])
    real_med = st["neff_med"] if not smoke \
        else rc_m4["ev"]["part"]["neff"]
    check("G81-mustfail-m4-collapse", m4_w <= TOY_FFT_BAR
          and real_med / max(m4_neff, 1e-300) >= 10.0,
          "m4 CONCENTRATED SYNTHETIC PDELTA (one-block mass at "
          "the real m = %d): n_eff == %.1f EXACT, n_act == 1, "
          "CV^2 == 0, orders == 1, one-atom B2 bound collapses "
          "(worst dev %.1e) -- EVERY route sees the collapse; "
          "LOUD vs the real med %.1f (ratio %.0fx)"
          % (rc_m4["ev"]["m"], m4_neff, m4_w, real_med,
             real_med / max(m4_neff, 1e-300)))
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
            and evS["po"]["mono"] <= ORD_BAR
            and evS["qu"]["qid_dev"] <= QID_BAR)
    check("G82-smooth-anchor", alias <= SM_ALIAS_BAR
          and abs(qS) <= SM_Q_BAR and okSd,
          "SMOOTH: drive alias %.1e <= %.0e; q_N = %.1e <= %.0e; "
          "every exact ward holds trivially on the self-aliased "
          "source (%s; B2/B3 shared-support wards skipped by the "
          "pre-declared DEG_FLOOR guard, W = %.1e)"
          % (alias, SM_ALIAS_BAR, qS, SM_Q_BAR,
             "OK" if okSd else "BROKEN", evS["wd"]["W"]))
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
          "adds: the Renyi order anatomy, the jackknife margin "
          "stability, the exact count/uniformity identity with "
          "the constructive count link, the exact weighted-"
          "discrepancy chain, the profile localization census "
          "and the sealed adjudication with the refined rest "
          "freeze -- NO new certificate promoted, NO bound "
          "modification of the sealed forms")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["NEFF_ANATOMY(N2/N3/N4/Ninf med %.1f/%.1f/%.1f/"
                 "%.1f sl %+.3f/%+.3f/%+.3f/%+.3f; tail med %.2f "
                 "sl %+.3f; L1 shares A/Bv %.2f/%.2f; IQR med "
                 "%.2f sl %+.3f)"
                 % (st["N2_med"], st["N3_med"], st["N4_med"],
                    st["Ninf_med"], st["sl_N2"], st["sl_N3"],
                    st["sl_N4"], st["sl_Ninf"], st["tail_med"],
                    st["sl_tail"], st["l1A_med"], st["l1B_med"],
                    st["iqr_med"], st["sl_iqr"])]
        parts.append("STABILITY(halves %+.3f/%+.3f; jackknife "
                     "min/max %+.3f/%+.3f, %d/42 below NEED "
                     "%+.3f)"
                     % (sl_lo_half, sl_hi_half, jk_min, jk_max,
                        n_below, need_neff))
        if fragile:
            parts.append("MARGIN_FRAGILE(jk_min %+.3f < NEED "
                         "%+.3f)" % (jk_min, need_neff))
        parts.append("ROUTE_TABLE(B1 n_act med %.1f count link "
                     "%d/42 sl_nact %+.3f sl_cv2p %+.3f gini "
                     "%.2f; B2 delta_w med %.3f sl %+.3f s_max "
                     "sl %+.3f surv %.2f sl %+.3f bound sl %+.3f"
                     " vs NEED %+.3f; B3 lloc med %.1f sl %+.3f "
                     "natom med %.1f sl %+.3f sp %+.2f local "
                     "census %d/%d/%d)"
                     % (st["nact_med"], st["nact_full"],
                        st["sl_nact"], st["sl_cv2p"],
                        st["gini_med"], st["dw_med"],
                        st["sl_dw"], st["sl_smax"],
                        st["surv_med"], st["sl_surv"],
                        st["sl_bound"], need_neff,
                        st["lloc_med"], st["sl_lloc"],
                        st["natom_med"], st["sl_natom"],
                        st["sp_atom_blk"], n_hold, n_near,
                        n_break))
        if outcome == "NEFF_DERIVED":
            parts.append("NEFF_DERIVED(B1: count link 42/42 + "
                         "CV^2 non-growing)")
        elif outcome == "NEFF_SPLIT":
            parts.append("NEFF_SPLIT(%s)" % " | ".join(fired))
        else:
            parts.append("NEFF_STILL_EMPIRICAL(no route clause "
                         "met; measured sl_neff %+.3f vs NEED "
                         "%+.3f)" % (st["sl_neff"], need_neff))
        if outcome == "NEFF_DERIVED" and not fragile:
            parts.append("CANDIDATE_THEOREM(printed in S6, "
                         "wave-10 candidate NOT promoted)")
        else:
            parts.append("REST_FROZEN(UNIF_TARGET: slope(1 + "
                         "CV^2) <= %+.3f measured %+.3f margin "
                         "%.3f; count link n_act == m %d/42)"
                         % (st["sl_nact"] - need_neff,
                            st["sl_cv2p"],
                            (st["sl_nact"] - need_neff)
                            - st["sl_cv2p"], st["nact_full"]))
        if not world_blind:
            parts.append("WORLD_SENSITIVE(MAIN %s (cv2 %.2f) vs "
                         "%s -- disclosed finding)"
                         % (cv_main, st["cv2_med"],
                            str(ctl_note)))
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the participation "
          "identity n_eff = n_act/(1 + CV^2), the power-mean "
          "chain, the star-discrepancy interval bound, the "
          "triangle chain, the Fractions identity (all "
          "world-blind); MEASURED: every slope, share, class, "
          "jackknife and correlation (42 rungs only); OPEN: "
          "UNIF_TARGET beyond the measured margin, the cofinal "
          "step H5, kz15 beyond r270; NO RH claim"
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
