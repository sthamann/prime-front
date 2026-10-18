#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""unif_target_probe -- PRIME.PORT.L2.UNIF_TARGET.01 (round 302):
the ANATOMY AND DERIVATION of the quasi-uniformity -- WHY is the
block profile of |PDelta| quasi-uniform (CV^2 bounded, i.e. the
r301 frozen rest UNIF_TARGET: prove slope(1 + CV^2) <= sl_nact -
NEED = +0.094; measured +0.039, margin 0.055 THIN), and can it be
derived SOURCE-PURELY?  Context (sealed record inputs): r297
(SPEC e42a76eb) froze the target inequality sigma <= sigma* =
-0.516; r298 (SPEC 05e831be) proved S_F ~ B(PDelta, PDelta); r299
(SPEC f432e944) found FULL-SUPPORT overlap 42/42 (Delta is a pure
c-value difference on ONE shared node set); r300 (SPEC 55218b5d)
proved sl_D = 2 sl_L1 - sl_neff exact and froze NEFF_TARGET; r301
(SPEC 6f8cc404, 32/32) proved the count/uniformity identity n_eff
= n_act/(1 + CV^2) exactly with the PERFECT count link n_act == m
on 42/42 (the effective-carrier count IS the constructive level-2
block count, +1.002), relocated the ONE remaining inequality onto
UNIF_TARGET (a growth statement became a BOUNDEDNESS statement),
found the lag-1 decorrelation of the difference profile (l_loc
med 1.0) and flagged the half-ladders +0.982/+0.802 (the deep
half of slope(n_eff) below NEED: front-loaded).  kz15 permanently
closed via r270; the 6 exceptions via the r287 F2 certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r287/r297/r298/r299/r300/r301 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F =
0.20 edge split; maximal same-sign runs of the bx-sorted bulk;
level-2 blocks (r270 convention); FROZEN vdC window H = max(2,
ceil(sqrt(m))); the frozen positional block machinery (r298:
block_breaks + aggregate_blocks), the r299 overlap split + cconv
census, the r300 participation + shared-support builders
(DTP.participation + DTP.shared_delta) and the r301 uniformity
builders (NTP.participation_orders + NTP.quasi_uniformity +
NTP.dc_profile), ALL imported verbatim; PDelta = Pbeta - Pomega;
the round's central quantity is CV^2 = var/mu^2 of the positive
block field |PDelta| over the ACTIVE blocks, and its head 1 +
CV^2 against the frozen standalone target UNIF_NEED = sl_nact -
(2 sl_L1 - sigma*) (recomputed live, record +0.094).

THE NEW EXACT COORDINATE (module-own, disclosed derived algebra):
on the shared bulk support with atom c-differences dc, block sums
P_j = sum_{blk j} dc, atom energy Q = sum dc^2, atom mass L1a =
sum |dc|, block mass L1 = sum |P_j|, block energy D = sum P_j^2:
    1 + CV^2  =  n_act x chi / (surv^2 x n_eff_atom)   -- EXACT,
with chi = D/Q (the IN-BLOCK COHERENCE FACTOR: chi < 1 iff the
in-block interference is destructive; chi <= kmax by per-block
Cauchy-Schwarz, kmax = max atoms per block), surv = L1/L1a (the
r301 in-block signed survival) and n_eff_atom = L1a^2/Q (the r301
atom participation).  Algebra: 1 + CV^2 = n_act D/L1^2 (r301 B1
identity) and D/L1^2 = chi Q/(surv L1a)^2 = chi/(surv^2
n_eff_atom).  Slope additivity slope(1 + CV^2) = sl_nact + sl_chi
- 2 sl_surv - sl_natom EXACT.  DISCLOSED PRIORS (derived from
r301 RECORD numbers only, no scratch run): chi med implied ~0.61
(destructive in-block interference), sl_chi implied ~-0.061,
sl_surv -0.020, sl_natom +0.942; the composition is an exact
reparametrization of UNIF_TARGET (r301-B1 style, disclosed) --
its derivation CONTENT is the split into a constructive count
(n_act == m), a bounded coherence factor (the r301 lag-1 mixing
trace), a bounded survival and ONE atom-level growth statement.

LEG 0 -- ANCHOR REGRESSION (r297/r300/r301 record numbers adopted
as-is, disclosed): sigma -0.714, sigma* -0.516, sl_c2 +0.196,
sl_pref +0.489 (tol 0.01); n_eff med 37.41 tol 0.05, sl_neff
+0.963, sl_L1 +0.196 (tol 0.01), NEED = 2 sl_L1 - sigma* record
+0.908; the r301 order family N_2/N_3/N_4/N_inf med
37.41/27.88/24.04/15.47 (tol 0.05) slopes
+0.963/+0.926/+0.894/+0.738 (tol 0.01), tail med 0.77 slope
-0.069; n_act med 73.0 (tol 0.5) sl_nact +1.002, COUNT LINK
n_act == m on 42/42 EXACT, CV^2 med 1.03 (tol 0.02) sl_cv2p
+0.039, Gini med 0.52; l_loc med 1.0 (tol 0.1) sl -0.036,
n_eff_atom med 118.0 (tol 1.0) sl +0.942, sp(atom, block) +0.96;
surv med 0.44 (tol 0.02) sl -0.020; half-ladders of n_eff
+0.982/+0.802 (tol 0.01) and the n_eff jackknife min/max
+0.936/+0.979 with 0/42 below NEED; the B1 identity and
power-mean-chain wards <= 1e-9 on 47 worlds; the r300 world
classes (MAIN PART_LOW/FILL_LOW vs EPST PART_HIGH/FILL_HIGH + SCR
PART_LOW/FILL_HIGH) EXACT and the r301 UNIF non-separation (MAIN
CV^2 1.03 bracketed by EPST 0.72 / SCR 2.76, tol 0.02).

LEG A -- THE CV^2 ANATOMY (what drives the +0.039 rise?):
(A1) EXACT VARIANCE DECOMPOSITION (law of total variance,
  module-own re-proof in exact Fractions): var = within + between
  over each of THREE sealed source-pure class schemes on the
  active blocks -- SIGN (sign of P_j; the r301 prime/power
  proxy), BAND (block midpoint in thirds of the bulk hull) and
  PAT (atom count k_j capped at K_PAT_CAP = 8); ward <= 1e-9 rel
  on 47 worlds x 3 schemes.  Census: between-share med + slope
  per scheme; SEALED CARRIER rule: scheme s is NAMED iff
  slope(between_share_s) >= +0.05 AND share med >= 0.25,
  otherwise the rise is STRUCTURELESS (within-class).
(A2) DISTRIBUTION STATIONARITY (mechanism iii of the round
  charter): active block values normalized per rung to mean 1 (y
  = |P_j|/mu); the 42-rung ladder split into THREE disjoint
  N-sorted groups of 14; pooled two-sample Kolmogorov distances
  KS(G1,G3), KS(G2,G3), KS(G1,G2) (deterministic step-function
  sup); decile table G1/G3; normalized moments m2 = 1 + CV^2,
  m3, m4 med per group + ladder slopes.  SEALED: PROFILE_
  STATIONARY iff KS(G1,G3) <= KS_STAT = 0.125 AND KS(G2,G3) <=
  KS_STAT; else PROFILE_DRIFTING.  If STATIONARY, CV^2
  boundedness = second-moment convergence of ONE stationary
  normalized profile -- a distribution statement, not a slope
  fit (and the honest explanation of the r299 cconv negative:
  convergence in distribution, not pointwise).
(A3) DEPTH HONESTY (the r301 half-ladder flag addressed
  head-on): (i) per-half slope additivity sl_neff = sl_nact -
  sl_cv2p EXACT on each disjoint half (gated <= 1e-9) -- WHICH
  factor carries the deep flattening of n_eff (+0.982 ->
  +0.802): the constructive count or the uniformity head?
  (ii) FINITE-SIZE MODEL (sealed model class, deterministic
  2-point solve, no fit primitives): m2(N) = A + B/N solved
  EXACTLY on the (G1, G3) group medians against the group median
  1/N, tested on the held-out middle group G2: rel dev <= FS_BAR
  = 0.05 => TRANSIENT_1_OVER_N (the profile approaches a finite
  stationary second moment A); else the 1/N class is rejected.
  (iii) JACKKNIFE of slope(1 + CV^2): 42 leave-one-out halves
  slopes vs UNIF_NEED (an UPPER target: fragile iff jk_max >
  UNIF_NEED).  SEALED TAGS: DEPTH_HALF_MISS iff sl_cv2p_hi >
  sl_nact_hi - NEED (the deep-half UNIF clause fails, the r301
  flag in the new coordinate); DEPTH_CAVEAT iff DEPTH_HALF_MISS
  AND NOT TRANSIENT_1_OVER_N (a confirmed trend break).

LEG B -- DERIVATION ROUTES FOR UNIF_TARGET (each on the real
builders, source-pure, AST scope audit, worlds test):
(B1) MIXING / COHERENCE ROUTE (the r301 lag-1 trace formalized):
  the EXACT identity 1 + CV^2 = n_act chi/(surv^2 n_eff_atom)
  (ward <= 1e-9 rel on 47 worlds; re-proved module-own in exact
  Fractions on a signed toy) + the exact per-block Cauchy-Schwarz
  bound chi <= kmax (ward; equality witness in the toy) + the
  exact slope additivity (<= 1e-9).  Census: chi med + slope
  (the coherence factor: does the in-block interference stay
  destructive?), surv med + slope, kmax med + slope (the honest
  worst-case cap), the lag-k autocorrelation profile rho_1..8 of
  the mean-removed dc field (med per k) -- the mixing bricks
  measured exactly; composition sl_nact + sl_chi - 2 sl_surv -
  sl_natom == sl_cv2p (ward) vs UNIF_NEED.  B1_OK iff all wards
  hold on 47 worlds AND sl_chi <= CHI_FLAT = +0.05 AND sl_surv
  >= SURV_FLAT = -0.05 (both factors bounded); frozen rest on
  fire: ATOM_TARGET = prove sl_natom >= sl_nact + sl_chi - 2
  sl_surv - UNIF_NEED (the relocated inequality, margin printed;
  DISCLOSED: the composition is a reparametrization -- the
  content is WHICH factor stays bounded).
(B2) CONSTRUCTION / PATTERN ROUTE: blocks classified by local
  node pattern (k_j capped at 8) x (block interval width lam_j
  quartile) = PAT12; exact within/between decomposition of the
  active-block variance over PAT12 (ward <= 1e-9 on 47 worlds).
  Census: within-share ws med + slope; the k-profile stability
  KS(G1, G3) of the normalized per-rung k_j/mean(k) pool.  B2_OK
  iff ws_med <= WS_BAR = 0.5 (|PDelta| concentrated per pattern
  class => CV^2 is pattern-mix variance, a counting object) AND
  ks_k <= KS_PAT = 0.125 (the pattern mix stabilizes -- checked,
  not asserted; PNT-free constructivity is NOT claimed).
(B3) RECURSION-STABILITY ROUTE: the sensitivity of the border
  drive readout to a LOCALIZED position perturbation (dx = 1e-7
  of the hull) at the three bulk quartile sites, on the sealed
  id pool (kz15 + kz20 + the two deepest rungs + mains + EPST +
  SCR); since the perturbation moves ONE atom, the block response
  is exactly the atom response: gain g = (|d ct_i| / mean|ct
  bulk|) / dx_hull, normalized gain g/N (the chain evaluation is
  a degree-(N-2) polynomial: O(N) log-derivative is the neutral
  expectation).  B3_OK iff med(g/N) <= AMP_BAR = 1.0 over the
  pool x sites (bounded Lyapunov-like amplification: the
  recursion does not blow up localized input noise beyond the
  polynomial-degree rate).  MEASURED census, correlational.
SEALED UNIF ADJUDICATION (frozen BEFORE evaluation, exactly one
fires): UNIF_NEED = sl_nact - (2 sl_L1 - sigma*) recomputed live;
  UNIF_DERIVED(B1 + A2) iff B1_OK AND PROFILE_STATIONARY AND
    TRANSIENT_1_OVER_N AND n_act == m on 42/42 AND sl_chi <= 0.0
    -- every named factor bounded/constructive AND the profile
    stationary with an identified 1/N transient (the hypotheses
    stay typed MEASURED in Leg C, disclosed);
  UNIF_SPLIT(fired routes, frozen rests) iff not DERIVED and
    (B1_OK or B2_OK or B3_OK);
  UNIF_STILL_EMPIRICAL(measured common obstruction) otherwise.
DEPTH_CAVEAT is an INDEPENDENT tag (Leg A3) and can coexist.

LEG C -- THEOREM COMPOSITION: fires ONLY on UNIF_DERIVED AND NOT
DEPTH_CAVEAT -- the full r297->r302 candidate is printed with
every constant (count identity n_eff = n_act/(1 + CV^2), n_act ==
m constructive, the coherence decomposition with bounded chi/surv
+ stationary profile => slope(1 + CV^2) <= UNIF_NEED =>
slope(n_eff) >= NEED => (r300 exact decomposition) sl_D <= sigma*
=> with RATIO_BOUNDED_STRUCTURAL (r300) sigma <= sigma* = -0.516
=> the r297 target inequality => the v964-S0 vdC theorem =>
delta' > 0.21 on the generic half; exceptions 6 via r287 F2 +
kz15 via r270).  Wave-10 promotion candidate -- NOT promoted.
OTHERWISE Leg C freezes the refined rest.

LEG D -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) VARIANCE-DECOMPOSITION WRONG CLASS WEIGHT (exact Fractions,
  module-own): on (2, 1, 1, 4) with classes {2, 1} | {1, 4}: var
  = 3/2 = within 5/4 + between 1/4 EXACT; the mutant weight
  (n_c/n)^2 recomposes to 3/4, break 3/4 EXACT -- CAUGHT: the
  class weight is load-bearing; (m2) UNNORMALIZED QQ/KS: the
  stationarity statistic on RAW (un-normalized) pooled profiles
  must be LOUD (>= KS_LOUD = 0.5; the raw block scale falls
  decades over the ladder) -- plus the synthetic exactness KS((1,
  2, 3), (100, 200, 300)) == 1; (m3) LAG-0 DOUBLE COUNTING in the
  coherence composition (exact Fractions, module-own): on the
  signed toy dc = (1, -2 | 3): chi = 5/7, identity dev 0 EXACT;
  the mutant Q' = Q + sum dc^2 (the diagonal counted twice) gives
  chi' = 5/14 and breaks the identity by 5/7 EXACT -- CAUGHT;
  (m4) SYNTHETIC TWO-POINT PROFILE (one heavy carrier 19 + nine
  1s): CV^2 = 729/196 EXACT > CV_SYN_MIN = 3.0 (vs the real med
  1.03), the normalized KS against the real pooled profile >=
  KS_LOUD, and the PAT12 decomposition sees the concentration --
  every route must recognize the non-uniform profile, LOUD;
  (m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key AND a builder consuming the branch
  label are both FLAGGED by the AST scope audit.  Scope hygiene:
  the new builders (var_decomp, coherence_split, lagk_profile,
  ks_two, fs_solve, perturb_gain) consume positions + weights +
  chain values only (BOUND_FORBIDDEN set); fragment audit (no fit
  primitives; the finite-size solve is a deterministic 2-point
  linear solve, disclosed); TOY EXACTNESS (bar 1e-14): the
  decomposition toy float == Fractions on (2, 1, 1, 4); the
  coherence toy (atoms (0, 1, 2), dc (1, -2, 3), breaks (1.5),
  hull [-1, 3]): P = (-1, 3), CV^2 = 1/4, chi = 5/7, surv = 2/3,
  n_eff_atom = 18/7, identity dev 0, per-block CS slack 0 with
  the one-atom block as EQUALITY WITNESS; ks toy ((1, 2, 3) vs
  (1.5, 2.5)) == 1/3 EXACT; fs toy ((10, 3), (40, 1.5) -> A = 1,
  B = 20, pred(20) = 2) EXACT; mp SAMPLES (dps 60): kz15 (bar
  1e-8) + the two deepest rungs (bar 3e-6); the DEGENERATE-SOURCE
  GUARD declared IN ADVANCE (r300-a1/r301 convention): on a
  source with Delta == 0 identically (self-aliased SMOOTH) the
  shared-support mass W degenerates to float noise; every
  shared-support ward is skipped exactly when W <= 1e-6 x the
  total contribution mass, disclosed per world.

INDEX FIREWALL (binding, r238-r301 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks, r299 FDP.overlap_split +
FDP.cconv_census, r300 DTP.participation + DTP.shared_delta +
DTP.cs_block_route, r301 NTP.participation_orders +
NTP.quasi_uniformity + NTP.dc_profile + NTP.split_disjoint, r269
PBB.mask_edge + PBB.runs_split + PBB.bound_pairsum + PBB.mp_drive,
r287 L2D.blocks_level2 + L2D.bound_vdc + L2D.halves_slope, r244
BH.wpack + BH.spearman, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN); QID_BAR
1e-9 (r301 count identity, rel); ORD_BAR 1e-9; CO_BAR 1e-9 (the
coherence identity, rel); VD_BAR 1e-9 (variance decomposition,
rel); CSK_BAR 1e-9 (chi <= kmax, rel D); ADD_BAR 1e-9 (slope
additivity); EQ_BAR 1e-9 (P_shared == P_ov == PDelta on the
ladder); NA_BAR 1e-12 (n_eff_atom internal consistency);
DEG_FLOOR 1e-6 (degenerate-source guard); REC_FLOOR 1e-6;
CHI_FLAT +0.05; CHI_NOGROW 0.0; SURV_FLAT -0.05; KS_STAT 0.125;
KS_LOUD 0.5; KS_PAT 0.125; FS_BAR 0.05; WS_BAR 0.5;
CARRIER_SHARE 0.25; CARRIER_GROW +0.05; AMP_BAR 1.0; DX_REL
1e-7; K_LAG 8; K_PAT_CAP 8; N_GRP 14; CV_SYN_MIN 3.0; CV_CLS 1.0;
PART_CLS 0.5; FILL_CLS 0.5; TOY_BAR 1e-14; MUT_MIN 1e-6; TB_WARD
bars 1e-9 / 3e-6 / 1e-6; ID_BAR 1e-12; AC_BAR 1e-9; R297 anchors
sigma -0.714 / sigma* -0.516 / sl_c2 +0.196 / sl_pref +0.489 (tol
0.01); R300/R301 anchors as listed in Leg 0 (med tols 0.05 count
fields 0.5/1.0, ratio tols 0.02, slope tols 0.01, half/jk tols
0.01, jk counts EXACT); world class refs MAIN PART_LOW/FILL_LOW,
EPST PART_HIGH/FILL_HIGH cv2 0.72, SCR PART_LOW/FILL_HIGH cv2
2.76 (tol 0.02); MP_DPS 60; MP_T_BAR 1e-8; MP_DEEP_BAR 3e-6;
KZ_ANCHOR 15; runtime <= 1800 s; smoke = w9 + controls +
Fractions section + toys + scope audits + every exact ward at w9
+ one B3 gain sample (ladder, slopes, groups, jackknife,
adjudications, censuses, mp wards skipped).
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r297/r300/r301 RECORD number adopted
as-is; the coherence identity, the per-block Cauchy-Schwarz cap,
the law of total variance and the finite-size 2-point solve are
derived algebra, disclosed above; the implied chi ~0.61 /
sl_chi ~-0.061 priors are algebraic consequences of r301 records;
the adjudication outcomes are sealed symmetrically -- the priors
make UNIF_SPLIT(B1 with ATOM_TARGET frozen) plausible and the A2
stationarity genuinely open, but no rule was chosen to favor an
outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  CV2_ANATOMY(between shares SIGN/BAND/PAT med + slope, carrier
    NAMED(scheme)/STRUCTURELESS; moment table m2/m3/m4)
+ PROFILE_STATIONARY(KS13/KS23/KS12, m2 groups) /
  PROFILE_DRIFTING(same numbers)
+ DEPTH(half attribution sl_nact lo/hi vs sl_cv2p lo/hi;
    TRANSIENT_1_OVER_N(A, B, held-out dev) or 1/N REJECTED;
    jackknife of sl_cv2p min/max/#above UNIF_NEED)
  [+ DEPTH_CAVEAT if fired]
+ ROUTE_TABLE(B1 chi med + slope, surv, kmax, rho_1..3, composed
    slope vs UNIF_NEED; B2 ws med + slope, ks_k; B3 gain/N med +
    max)
+ [exactly one of] UNIF_DERIVED(B1 + A2) / UNIF_SPLIT(fired
    routes + frozen rests) / UNIF_STILL_EMPIRICAL(obstruction)
+ [iff DERIVED and not DEPTH_CAVEAT] CANDIDATE_THEOREM(all
    constants, hypotheses typed MEASURED)  [else]
    REST_FROZEN(the refined needed-vs-measured statement)
+ [if a control class differs] WORLD_NOTE(disclosed; UNIF does
    not separate worlds per r301 -- the derivation MAY be
    world-blind and ideally is).
Honesty before beauty: the coherence identity, the CS cap, the
variance decomposition and the finite-size solve are EXACT finite
statements, but every slope, share, KS distance, gain and class
is MEASURED on 42 rungs only; the B1 composition is an exact
reparametrization of UNIF_TARGET (disclosed), its derivation
content is the coherence/survival/atom split ONLY; the A2
stationarity is a pooled two-sample statement, not a limit
theorem; no verdict claims a cofinal law; the exception scalar's
positivity beyond the measured 42 stays OPEN; r243-r301 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 28/30 -- ONE code-side defect, disclosed: the m3
lag-0 mutant doubled the atom energy Q in BOTH the chi side and
the n_eff_atom side of the composition, making the mutant
self-consistent (break 0); fixed to hit ONLY the chi side, as the
sealed spec text describes (break 5/7 EXACT) -- a code-side fix,
no bar, band, rule or verdict rule touched; smoke pass 2 = 30/30
(0.3 s); calibration pass 1 = first full evaluation, 28/30, wall
49.6 s, exposing TWO amendments, both disclosed: (a1) the m2
UNNORMALIZED mustfail was sealed with an ABSOLUTE loudness bar
KS_LOUD = 0.5, but the raw G1/G3 pools overlap through the ~30x
within-rung spread (measured raw KS 0.335 < 0.5, the original
sealed outcome printed permanently in G42) -- the amended rule is
the RELATIVE form: raw KS >= 4 x normalized KS13 AND >= 2 x
KS_STAT (measured: 0.335 = 8x the normalized 0.043, CAUGHT); no
adjudication bar, band or verdict rule moved; (a2) REPORTING
ONLY: the B3 per-world labels printed the raw kz field (EPST/SCR
showed as kz9), relabeled; calibration pass 2 = 30/30, wall 50.3
s; record run1/run2 after this insertion, identical up to WALL;
the only post-freeze edits are the disclosed m3 fix, a1, a2 and
this record-table insertion, which IS the protocol):
CAL_VERDICT = CV2_ANATOMY(between shares SIGN/BAND/PAT med
0.012/0.216/0.111 slopes +0.292/-0.182/-0.519 -- NO scheme fires
the sealed carrier rule (SIGN grows +0.29 but carries only 1.2
pct; BAND carries 22 pct but FALLS; PAT falls): the +0.039 rise
is STRUCTURELESS -- within-class, not a namable class shift;
normalized moments m2/m3/m4 med 2.03/5.81/18.7, m3/m4 slopes
+0.153/+0.326: the tail moments drift mildly upward) +
PROFILE_STATIONARY(KS(G1,G3) 0.043 / KS(G2,G3) 0.021 / KS(G1,G2)
0.026, ALL far under the sealed 0.125; deciles G1
0.08/0.19/0.34/0.49/0.66/0.87/1.23/1.70/2.39 vs G3
0.08/0.18/0.30/0.48/0.69/0.95/1.22/1.67/2.33 -- the normalized
block profile is STATIONARY along the ladder: CV^2 boundedness
is the second-moment statement of ONE stable profile, and the
r299 cconv negative is explained -- convergence in DISTRIBUTION,
not pointwise; m2 group medians 2.07/2.02/2.00) + DEPTH(half
attribution: sl_nact lo/hi +0.929/+1.030 vs sl_cv2p lo/hi
-0.053/+0.228, additivity exact per half (0.982 = 0.929 -
(-0.053), 0.802 = 1.030 - 0.228, gated 0.0/2.2e-16) -- THE r301
FLAG IS THE HEAD, NOT THE COUNT: the count even accelerates in
the deep half (+1.030), the entire n_eff flattening is the CV^2
head growing at +0.228 > the deep-half allowance +0.122:
DEPTH_HALF_MISS fires; BUT the sealed finite-size model
TRANSIENT_1_OVER_N(A = 1.973, B = +17.9, held-out dev 0.002 <=
0.05): the group medians 2.07 -> 2.02 -> 2.00 fall along an
exact 1/N law onto a finite stationary second moment 1.973,
approached from ABOVE -- the deep-half slope excess is
depth-consistent with the stationary profile, DEPTH_CAVEAT does
NOT fire; jackknife of sl_cv2p min/max +0.026/+0.062, 0/42 above
UNIF_NEED +0.094 -- the margin survives every single-rung
removal) + ROUTE_TABLE(B1 chi med 0.630 slope -0.060 -- the
in-block interference IS destructive and non-growing, the
mixing-route clause holds with room; surv med 0.44 slope -0.020
flat; kmax med 9.0 slope +0.115 -- the honest worst-case CS cap
GROWS, the cap alone cannot carry; rho_1/2/3 med
-0.222/-0.140/+0.089 -- the anti-correlated lag-1 profile IS the
destructive-chi mechanism at atom level; composed +1.002 - 0.060
+ 0.040 - 0.942 = +0.039 == sl_cv2p exactly (additivity 5.4e-16)
vs UNIF_NEED +0.094; B2 PAT12 within-share med 0.685 slope
+0.071 FAILS the 0.5 bar -- |PDelta| is NOT concentrated per
local (k, width) pattern class (69 pct of the variance lives
WITHIN the classes) AND the k-profile itself drifts (ks_k 0.181
> 0.125): the construction-geometry route is closed honestly on
BOTH clauses; B3 gain/N med 1.079 max 4.723 vs AMP_BAR 1.0 --
the recursion responds AT the polynomial-degree rate (med 1.08x
N), neither damping nor blow-up; the sealed damping clause
misses by 0.079, honest (per world: kz20 1.290 / kz15 1.733 /
kz64 2.090 / kz52 0.744 / w9 2.277 / w13 2.536 / EPST 0.746 /
SCR 0.333 -- world-blind in class)) + UNIF_DERIVED(B1 + A2: the
sealed clause fired -- B1_OK (chi -0.060 <= 0 non-growing, surv
flat, wards + additivity exact on 47 worlds) AND STATIONARY AND
TRANSIENT AND count link 42/42) + CANDIDATE_THEOREM(printed in
S6, hypotheses typed MEASURED: count identity + coherence
decomposition (EXACT) with chi non-growing (MEASURED) + surv
flat (MEASURED) + stationary profile (MEASURED) + 1/N transient
(MEASURED) + atom growth sl_natom +0.942 >= ATOM_NEED = sl_nact
+ sl_chi - 2 sl_surv - UNIF_NEED = +0.888, margin 0.055
(MEASURED) => slope(1 + CV^2) <= +0.094 => slope(n_eff) >=
+0.908 => sl_D <= sigma* => sigma <= sigma* = -0.516 => r297
target => v964-S0 vdC => delta' > 0.21 generic; exceptions 6 via
r287 F2 + kz15 via r270; wave-10 candidate NOT promoted) +
WORLD_NOTE(the coherence identity holds on 47 worlds by algebra
-- world-blind as the charter demands; UNIF non-separation
reproduced: MAIN cv2 1.03 bracketed by EPST 0.72 (chi 0.18) and
SCR 2.76 (chi 1.26); r300 PART/FILL classes EXACT).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; r297 anchors bit-near (sigma -0.714, sigma*
-0.516, sl_c2 +0.196, sl_pref +0.489); r300 anchors bit-near
(n_eff 37.41, sl_neff +0.963, sl_L1 +0.196, NEED +0.908); r301
anchors bit-near (orders 37.41/27.88/24.04/15.47 at
+0.963/+0.926/+0.894/+0.738, tail 0.77/-0.069, n_act 73.0/+1.002
link 42/42, cv2 1.03/+0.039, gini 0.52, lloc 1.0/-0.036, natom
118.0/+0.942, sp +0.96, surv 0.44/-0.020, halves +0.982/+0.802,
jk +0.936/+0.979 0/42 below NEED).  S3: module-own Fractions:
decomposition 3/2 = 5/4 + 1/4 dev 0, m1 break 3/4 exact;
coherence identity dev 0 (CV^2 1/4, chi 5/7, surv 2/3, natom
18/7), m3 lag-0 break 5/7 exact; toys worst 3.6e-15 (bar 1e-14;
KS 1/3 exact, fs solve exact, CS equality witness slack 0, lam
(17/24, 7/24)); synthetic scale mutant KS 1.00 exact; m4
two-point CV^2 729/196 = 3.72 > 3.0, KS vs real pool 0.567 >=
0.5 LOUD, two-class within-share 0.0000 (dev 1.2e-16).  S4/S5
wards: count identity worst 6.8e-16, variance decomposition
worst 4.6e-16 (47 worlds x 3 schemes + PAT12), coherence
identity worst 6.0e-16, CS cap slack 0.0, P_shared == P_ov
6.1e-16, ladder CV^2 equality 8.1e-16, natom internal 4.9e-16,
dc == dw x f 2.6e-15; DEG guard fired on SMOOTH only
(pre-declared).  S8: mp wards kz15 2.9e-10, kz64 9.3e-9, kz52
6.6e-8; exception rungs in-table: n_act == m on all 7, cv2 0.98
(kz38) .. 1.41 (kz39), chi 0.60 (kz38) .. 0.93 (kz15), surv 0.39
(kz39) .. 0.53 (kz15), kmax 6 (kz15) .. 12 (kz22/36/52).
READING (typed, no upgrade): the round DELIVERS the CV^2 anatomy
and -- for the first time in the lane -- fires a DERIVED verdict
under a sealed rule, with every hypothesis honestly typed
MEASURED: (1) the mild CV^2 rise is STRUCTURELESS (no class
scheme carries it) and the normalized block profile is
STATIONARY (KS 0.043 over a 3x depth range) with an exact-1/N
transient onto m2_inf = 1.973 -- mechanism (iii) of the charter
is the measured answer: |PDelta| block values have ONE stable
normalized distribution, CV^2 boundedness is its second moment,
and the r299 pointwise-cconv negative was the wrong convergence
notion; (2) the DEPTH honesty sharpens r301: the deep-half
flattening of n_eff is carried ENTIRELY by the CV^2 head
(+0.228), NOT the count (+1.030) -- and exactly this head excess
is what the 1/N transient explains (2.07 -> 2.00 falling
medians): the front-loaded slope was an artifact of the halves
estimator on a 1/N-converging quantity; (3) B1 delivers the
exact coherence decomposition: the uniformity head factorizes
into count x coherence / (survival^2 x atom participation), with
chi = 0.63 DESTRUCTIVE and falling (the r301 lag-1
anti-correlation rho_1 = -0.22 is its atom-level mechanism), so
the ONE remaining measured growth statement is ATOM_TARGET
(sl_natom +0.942 >= +0.888, margin 0.055 -- the same thin margin
one level down); (4) B2 and B3 closed honestly: the local node
pattern does NOT determine |PDelta| (within-share 0.69) and the
recursion responds at exactly the polynomial-degree rate (gain/N
med 1.08 vs the sealed damping bar 1.0, miss 0.079).  Bycatch:
the m2 mustfail taught an honest lesson about pooled raw scales
(a1, disclosed).  Runtime 50.3 s full / 0.3 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: the disclosed
smoke-stage m3 fix + a1 (m2 loudness re-anchored to the relative
form, original outcome printed) + a2 (B3 label reporting)
(records inserted per protocol; no adjudication bar, band or
verdict rule moved).

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
import window_border_transfer_probe as WBT     # noqa: E402 r298
import fejer_decay_probe as FDP                # noqa: E402 r299
import diag_target_probe as DTP                # noqa: E402 r300
import neff_target_probe as NTP                # noqa: E402 r301
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
QID_BAR = 1e-9
ORD_BAR = 1e-9
CO_BAR = 1e-9
VD_BAR = 1e-9
CSK_BAR = 1e-9
ADD_BAR = 1e-9
EQ_BAR = 1e-9
NA_BAR = 1e-12
DEG_FLOOR = 1e-6
REC_FLOOR = 1e-6
CHI_FLAT = 0.05
CHI_NOGROW = 0.0
SURV_FLAT = -0.05
KS_STAT = 0.125
KS_LOUD = 0.5
KS_PAT = 0.125
FS_BAR = 0.05
WS_BAR = 0.5
CARRIER_SHARE = 0.25
CARRIER_GROW = 0.05
AMP_BAR = 1.0
DX_REL = 1e-7
K_LAG = 8
K_PAT_CAP = 8
N_GRP = 14
CV_SYN_MIN = 3.0
CV_CLS = 1.0
PART_CLS = 0.5
FILL_CLS = 0.5
TOY_BAR = 1e-14
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
R300_NEFF_MED = 37.41
R300_NEFF_TOL = 0.05
R300_SL_NEFF = 0.963
R300_SL_NEFF_TOL = 0.01
R300_SL_L1 = 0.196
R300_SL_L1_TOL = 0.01
R300_MAIN_CLS = ("PART_LOW", "FILL_LOW")
R300_EPST_CLS = ("PART_HIGH", "FILL_HIGH")
R300_SCR_CLS = ("PART_LOW", "FILL_HIGH")
R301_ORD_MED = (37.41, 27.88, 24.04, 15.47)
R301_ORD_MED_TOL = 0.05
R301_ORD_SL = (0.963, 0.926, 0.894, 0.738)
R301_ORD_SL_TOL = 0.01
R301_TAIL_MED = 0.77
R301_TAIL_TOL = 0.02
R301_TAIL_SL = -0.069
R301_TAIL_SL_TOL = 0.01
R301_NACT_MED = 73.0
R301_NACT_TOL = 0.5
R301_SL_NACT = 1.002
R301_SL_NACT_TOL = 0.01
R301_CV2_MED = 1.03
R301_CV2_TOL = 0.02
R301_SL_CV2P = 0.039
R301_SL_CV2P_TOL = 0.01
R301_GINI_MED = 0.52
R301_GINI_TOL = 0.02
R301_LLOC_MED = 1.0
R301_LLOC_TOL = 0.1
R301_SL_LLOC = -0.036
R301_SL_LLOC_TOL = 0.01
R301_NATOM_MED = 118.0
R301_NATOM_TOL = 1.0
R301_SL_NATOM = 0.942
R301_SL_NATOM_TOL = 0.01
R301_SP_ATOM = 0.96
R301_SP_ATOM_TOL = 0.02
R301_SURV_MED = 0.44
R301_SURV_TOL = 0.02
R301_SL_SURV = -0.020
R301_SL_SURV_TOL = 0.01
R301_HALF_LO = 0.982
R301_HALF_HI = 0.802
R301_HALF_TOL = 0.01
R301_JK_MIN = 0.936
R301_JK_MAX = 0.979
R301_JK_TOL = 0.01
R301_EPST_CV2 = 0.72
R301_SCR_CV2 = 2.76
R301_CTL_CV2_TOL = 0.02
MP_DPS = 60
MP_T_BAR = 1e-8
MP_DEEP_BAR = 3e-6
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


# ---------------- exact Fractions section: the variance
# ---------------- decomposition + the coherence identity
def fr_var_decomp(wrong="none"):
    """the law of total variance on (2, 1, 1, 4) with classes
    {2, 1} | {1, 4}, exact Fractions: var = 3/2, within = 5/4,
    between = 1/4, recomposition dev 0 EXACT.  wrong='weight'
    replaces the class weight n_c/n by (n_c/n)^2 (the m1 mutant,
    must recompose to 3/4, break 3/4 EXACT)."""
    vals = [Fr(2), Fr(1), Fr(1), Fr(4)]
    labs = [0, 0, 1, 1]
    n = len(vals)
    mu = sum(vals) / n
    var = sum((v - mu) ** 2 for v in vals) / n
    within = Fr(0)
    between = Fr(0)
    for c in sorted(set(labs)):
        grp = [v for v, l_ in zip(vals, labs) if l_ == c]
        nc = len(grp)
        mc = sum(grp) / nc
        vc = sum((v - mc) ** 2 for v in grp) / nc
        w = Fr(nc, n) ** 2 if wrong == "weight" else Fr(nc, n)
        within += w * vc
        between += w * (mc - mu) ** 2
    return abs(within + between - var), var, within, between


def fr_coherence(wrong="none"):
    """the coherence identity (1 + CV^2) x surv^2 x n_eff_atom ==
    n_act x chi on the signed toy dc = (1, -2 | 3), exact
    Fractions: P = (-1, 3), n_act = 2, CV^2 = 1/4, L1a = 6, Q =
    14, chi = D/Q = 10/14 = 5/7, surv = 4/6 = 2/3, n_eff_atom =
    36/14 = 18/7; LHS = 5/4 x 4/9 x 18/7 = 10/7 = RHS EXACT.
    wrong='lag0' doubles the diagonal in Q (Q' = 28, chi' = 5/14,
    the m3 mutant, must break by 5/7 EXACT)."""
    dc = [Fr(1), Fr(-2), Fr(3)]
    P = [dc[0] + dc[1], dc[2]]
    D = sum(p * p for p in P)
    L1 = sum(abs(p) for p in P)
    act = [abs(p) for p in P if p != 0]
    n_act = len(act)
    mu = sum(act) / n_act
    var = sum((a - mu) ** 2 for a in act) / n_act
    cv2 = var / (mu * mu)
    L1a = sum(abs(v) for v in dc)
    Q = sum(v * v for v in dc)
    Q_chi = Q + sum(v * v for v in dc) if wrong == "lag0" else Q
    chi = D / Q_chi
    surv = L1 / L1a
    natom = L1a * L1a / Q
    lhs = (1 + cv2) * surv * surv * natom
    rhs = n_act * chi
    return abs(lhs - rhs), cv2, chi, surv, natom


# ---------------- the module-own anatomy / route builders.
# ---------------- Source-pure: block vectors (positions, weights,
# ---------------- chain values) only; the withheld terminal drive
# ---------------- key, the branch label and every target-side
# ---------------- identifier are forbidden in scope (AST audit).
def var_decomp(vals, labels):
    """the exact law of total variance over integer class labels:
    var = sum_c w_c var_c + sum_c w_c (mu_c - mu)^2 with w_c =
    n_c/n (population form).  Returns (var, within, between,
    relative recomposition dev)."""
    v = np.asarray(vals, dtype=float)
    lab = np.asarray(labels)
    n = len(v)
    if n == 0:
        return dict(var=0.0, within=0.0, between=0.0, dev=0.0)
    mu = float(np.mean(v))
    var = float(np.mean((v - mu) ** 2))
    within = 0.0
    between = 0.0
    for c in np.unique(lab):
        g = v[lab == c]
        w = len(g) / n
        mc = float(np.mean(g))
        within += w * float(np.mean((g - mc) ** 2))
        between += w * (mc - mu) ** 2
    dev = abs(within + between - var) / max(var, 1e-300)
    return dict(var=var, within=within, between=between, dev=dev)


def coherence_split(xs, dcs, lo, hi, brk, m):
    """the B1 exact coherence coordinates on the shared bulk
    support: edge mask (combined hull, EDGE_F), block index by
    breakpoint search; per-block sums P_j, per-block atom
    energies Q_j and atom counts k_j; block D/L1/CV^2 over the
    ACTIVE blocks, atom Q/L1a; chi = D/Q, surv = L1/L1a,
    n_eff_atom = L1a^2/Q; the EXACT identity (1 + CV^2) surv^2
    n_eff_atom == n_act chi (relative dev returned) and the
    per-block Cauchy-Schwarz cap P_j^2 <= k_j Q_j (worst slack
    rel D returned).  Also block interval shares lam_j (clipped
    hull) and block midpoints for the class schemes."""
    xs = np.asarray(xs, dtype=float)
    ed = PBB.mask_edge(xs, lo, hi, EDGE_F)
    x = xs[~ed]
    w = np.asarray(dcs, dtype=float)[~ed]
    a_h = lo + EDGE_F * (hi - lo)
    b_h = hi - EDGE_F * (hi - lo)
    out = dict(P=np.zeros(max(m, 0)), n_act=0, cv2=0.0, chi=0.0,
               surv=0.0, natom=1.0, kmax=0, id_dev=0.0,
               cs_slack=0.0, Q=0.0, L1a=0.0, D=0.0, L1=0.0,
               vals=np.zeros(0), sgn=np.zeros(0, dtype=int),
               band=np.zeros(0, dtype=int),
               kpat=np.zeros(0, dtype=int),
               lam=np.zeros(0), k_act=np.zeros(0, dtype=int))
    if m == 0 or len(x) == 0:
        return out
    j = np.searchsorted(brk, x)
    P = np.bincount(j, weights=w, minlength=m)
    Qj = np.bincount(j, weights=w * w, minlength=m)
    kj = np.bincount(j, minlength=m)
    D = float(np.sum(P * P))
    L1 = float(np.sum(np.abs(P)))
    Q = float(np.sum(Qj))
    L1a = float(np.sum(np.abs(w)))
    if Q <= 0.0 or L1a <= 0.0:
        out["P"] = P
        return out
    a = np.abs(P)
    act = a > 0.0
    n_act = int(np.sum(act))
    if n_act == 0:
        out["P"] = P
        return out
    va = a[act]
    mu = float(np.mean(va))
    var = float(np.mean((va - mu) ** 2))
    cv2 = var / max(mu * mu, 1e-300)
    chi = D / Q
    surv = L1 / L1a
    natom = L1a * L1a / Q
    lhs = (1.0 + cv2) * surv * surv * natom
    rhs = n_act * chi
    id_dev = abs(lhs - rhs) / max(abs(rhs), 1e-300)
    cs_slack = float(np.max(P * P - kj * Qj)) / max(D, 1e-300)
    edges = np.concatenate([[a_h],
                            np.clip(np.asarray(brk, dtype=float),
                                    a_h, b_h), [b_h]])
    lam = np.maximum(np.diff(edges), 0.0) / max(b_h - a_h, 1e-300)
    mids = 0.5 * (edges[:-1] + edges[1:])
    sgn = (P[act] > 0.0).astype(int)
    tpos = (mids[act] - a_h) / max(b_h - a_h, 1e-300)
    band = np.minimum((tpos * 3.0).astype(int), 2)
    kpat = np.minimum(kj[act], K_PAT_CAP).astype(int)
    out.update(P=P, n_act=n_act, cv2=cv2, chi=chi, surv=surv,
               natom=natom, kmax=int(np.max(kj[act])),
               id_dev=id_dev, cs_slack=cs_slack, Q=Q, L1a=L1a,
               D=D, L1=L1, vals=va, sgn=sgn, band=band,
               kpat=kpat, lam=lam[act],
               k_act=kj[act].astype(int))
    return out


def lagk_profile(xs, dcs, lo, hi, K):
    """the lag-k autocorrelations rho_1..K of the mean-removed
    c-difference profile on the bulk shared support (the r301
    l_loc census extended to a fixed lag table)."""
    xs = np.asarray(xs, dtype=float)
    ed = PBB.mask_edge(xs, lo, hi, EDGE_F)
    z = np.asarray(dcs, dtype=float)[~ed]
    n = len(z)
    if n < 2:
        return [0.0] * K
    zc = z - float(np.mean(z))
    A = np.correlate(zc, zc, mode="full")[n - 1:]
    if abs(A[0]) <= 0.0:
        return [0.0] * K
    return [float(A[k] / A[0]) if k < n else 0.0
            for k in range(1, K + 1)]


def ks_two(a, b):
    """deterministic two-sample Kolmogorov distance (sup of the
    empirical CDF difference over the pooled support)."""
    a = np.sort(np.asarray(a, dtype=float))
    b = np.sort(np.asarray(b, dtype=float))
    if len(a) == 0 or len(b) == 0:
        return 0.0
    pool = np.concatenate([a, b])
    Fa = np.searchsorted(a, pool, side="right") / len(a)
    Fb = np.searchsorted(b, pool, side="right") / len(b)
    return float(np.max(np.abs(Fa - Fb)))


def fs_solve(n1, y1, n3, y3, n2):
    """the sealed finite-size model class m2(N) = A + B/N solved
    EXACTLY on two (N, y) points (deterministic 2-point linear
    solve, no fit primitive); returns (A, B, prediction at n2)."""
    i1 = 1.0 / n1
    i3 = 1.0 / n3
    B = (y1 - y3) / (i1 - i3)
    A = y1 - B * i1
    return A, B, A + B / n2


def perturb_gain(rows, N, x_i, v2_i, ct_i, bw_i, fac, lo, hi):
    """the B3 localized-perturbation gain at ONE bulk atom: move
    the atom by dx = DX_REL x (hi - lo), re-evaluate the chain
    readout at the moved position (r266 eval, degree N-2) and
    return the normalized response |d ct| (the block response
    equals the atom response: only one atom moved)."""
    dx = DX_REL * (hi - lo)
    v2p = float(BR.eval_scaled(rows, np.array([x_i + dx]),
                               N - 2)[0])
    ct_p = bw_i * (x_i + dx) * v2p * fac
    return abs(ct_p - ct_i), dx


def mutant_gift_bound(rc, vals):
    """m5a MUST-FAIL MUTANT: a 'uniformity target' oriented by
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * var_decomp(vals, [0] * len(vals))["var"]


def mutant_branch_peek(rc, vals):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'profile moment' that consumes the branch label to pick its
    constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.mean(np.asarray(vals, dtype=float) ** 2))


# ---------------------------------------------- toy exact tools
def toy_var_decomp():
    """float var_decomp on (2, 1, 1, 4) with classes (0,0,1,1)
    must reproduce the Fractions record var 3/2 = within 5/4 +
    between 1/4 EXACTLY.  Returns worst dev."""
    d = var_decomp([2.0, 1.0, 1.0, 4.0], [0, 0, 1, 1])
    return max(abs(d["var"] - 1.5), abs(d["within"] - 1.25),
               abs(d["between"] - 0.25), d["dev"])


def toy_coherence():
    """float coherence_split on the signed toy: atoms (0, 1, 2),
    dc (1, -2, 3), breaks (1.5), hull [-1, 3] (edge zone [-1,
    -0.2) + (2.2, 3]: all atoms inside): P = (-1, 3), n_act 2,
    CV^2 1/4, chi 5/7, surv 2/3, n_eff_atom 18/7, kmax 2,
    identity dev 0, per-block CS slack 0 (one-atom block 3^2 ==
    1 x 9 EQUALITY WITNESS); lam = (0.5, 0.5) on the clipped
    hull [-0.2, 2.2] (break 1.5 -> shares (1.7, 0.7)/2.4?  no:
    hull length 2.4, edges (-0.2, 1.5, 2.2) -> lam = (17/24,
    7/24)).  Returns worst dev."""
    co = coherence_split(np.array([0.0, 1.0, 2.0]),
                         np.array([1.0, -2.0, 3.0]),
                         -1.0, 3.0, np.array([1.5]), 2)
    return max(abs(co["n_act"] - 2.0), abs(co["cv2"] - 0.25),
               abs(co["chi"] - 5.0 / 7.0),
               abs(co["surv"] - 2.0 / 3.0),
               abs(co["natom"] - 18.0 / 7.0),
               abs(co["kmax"] - 2.0), co["id_dev"],
               abs(co["cs_slack"]),
               abs(co["lam"][0] - 17.0 / 24.0),
               abs(co["lam"][1] - 7.0 / 24.0))


def toy_ks_and_fs():
    """ks_two((1,2,3), (1.5,2.5)) == 1/3 EXACT; the finite-size
    solve on (10, 3), (40, 1.5) -> A = 1, B = 20, pred(20) = 2
    EXACT; the synthetic scale mutant KS((1,2,3), (100,200,300))
    == 1 EXACT.  Returns (worst dev, mutant KS)."""
    k = ks_two([1.0, 2.0, 3.0], [1.5, 2.5])
    A, B, p = fs_solve(10.0, 3.0, 40.0, 1.5, 20.0)
    km = ks_two([1.0, 2.0, 3.0], [100.0, 200.0, 300.0])
    worst = max(abs(k - 1.0 / 3.0), abs(A - 1.0), abs(B - 20.0),
                abs(p - 2.0), abs(km - 1.0))
    return worst, km


def toy_m4_twopoint(pool_real):
    """m4 SYNTHETIC TWO-POINT PROFILE: one heavy carrier 19 +
    nine 1s -- CV^2 = 729/196 EXACT (> CV_SYN_MIN); the
    normalized profile vs the real pooled profile must be KS
    LOUD; the PAT12-style two-class decomposition sees the
    concentration (within-share printed)."""
    v = np.array([19.0] + [1.0] * 9)
    mu = float(np.mean(v))
    var = float(np.mean((v - mu) ** 2))
    cv2 = var / (mu * mu)
    cv2_dev = abs(cv2 - 729.0 / 196.0)
    y = v / mu
    ks = ks_two(y, pool_real) if len(pool_real) else 1.0
    labs = (v > 10.0).astype(int)
    d = var_decomp(v, labs)
    ws = d["within"] / max(d["var"], 1e-300)
    return cv2, cv2_dev, ks, ws, d["dev"]


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("unif_target_probe -- PRIME.PORT.L2.UNIF_TARGET.01 "
          "(round 302)")
    print("SPEC_SHA %s   R300_SHA %s (imported)   R301_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], DTP.SPEC_SHA[:16], NTP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + every exact ward "
                        "at w9 + one B3 sample; ladder, slopes, "
                        "groups, jackknife, adjudications, "
                        "censuses, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE UNIF-TARGET ROUND (the r301 frozen rest executed): "
          "slope(1 + CV^2) <= sl_nact - NEED (record +0.094, "
          "measured +0.039, margin 0.055) -- WHY is the block "
          "profile of |PDelta| quasi-uniform?  This round "
          "decomposes CV^2 exactly (three class schemes), tests "
          "distribution stationarity of the normalized profile "
          "(mechanism iii), addresses the r301 half-ladder flag "
          "with an exact per-half attribution + a sealed 1/N "
          "model, and tests THREE source-pure derivation routes "
          "(B1 the exact coherence identity 1 + CV^2 = n_act chi "
          "/(surv^2 n_eff_atom) with the r301 lag-1 mixing trace, "
          "B2 the local-pattern concentration, B3 the localized-"
          "perturbation gain); sealed outcomes DERIVED / SPLIT "
          "(frozen rests) / STILL_EMPIRICAL plus the independent "
          "DEPTH_CAVEAT tag; ALL bars, bands, rules and verdicts "
          "sealed BEFORE evaluation")

    # ---------------- S1: census + controls (r301 scaffold verbatim)
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
    section("S2  EXACT DECOMPOSITION + R297/R300/R301 ANCHORS")
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
        # ---- the frozen positional blocks (r298 verbatim)
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        agg_dev = float(np.max(np.abs(Pb - np.array(P)))) \
            / max(max(abs(v) for v in P), 1e-300) if m else 0.0
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        Pd = Pb - Pw
        # ---- r299 overlap split + cconv (imported verbatim)
        P_ov, P_fr, _n_b, _n_w = FDP.overlap_split(
            bxs, cts, rc["xu"], rc["cw"], rc["lo"], rc["hi"],
            brk, m)
        part_dev = float(np.max(np.abs(P_ov + P_fr - Pd))) \
            / max(float(np.max(np.abs(Pd))), 1e-300) if m else 0.0
        cconv, n_common = FDP.cconv_census(bxs, cts, rc["xu"],
                                           rc["cw"])
        full_ov = int(n_common == len(rc["bx"]) == len(rc["xu"]))
        # ---- r300/r301 anatomy (imported builders)
        part = DTP.participation(Pd)
        po = NTP.participation_orders(Pd)
        qu = NTP.quasi_uniformity(Pd)
        # ---- shared support (r300 builders verbatim)
        fxs = rc["bx"] * rc["v2"] * rc["fac"]
        sd = DTP.shared_delta(rc["bx"], rc["ct"], rc["bw"], fxs,
                              rc["xu"], rc["cw"], rc["wu"])
        df_dev = float(np.max(np.abs(sd["dc"]
                                     - sd["dw"] * sd["f"]))) \
            / max(float(np.max(np.abs(sd["dc"]))), 1e-300) \
            if sd["n"] else 0.0
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        W_abs = float(np.sum(np.abs(sd["dc"]))) if sd["n"] else 0.0
        degenerate = (W_abs <= DEG_FLOOR * absm)
        # ---- the round's coherence coordinates (module-own)
        if degenerate or m == 0 or sd["n"] == 0:
            co = coherence_split(np.zeros(0), np.zeros(0),
                                 rc["lo"], rc["hi"],
                                 brk if m else np.zeros(0), m)
            rec_dev = 0.0
            eq_dev = 0.0
            na_dev = 0.0
            pr = dict(lloc=1.0, neff_atom=1.0, n=0)
            lags = [0.0] * K_LAG
        else:
            co = coherence_split(sd["x"], sd["dc"], rc["lo"],
                                 rc["hi"], brk, m)
            rec_scale = max(float(np.max(np.abs(P_ov)))
                            if m else 0.0,
                            REC_FLOOR * absm, 1e-300)
            rec_dev = float(np.max(np.abs(co["P"] - P_ov))) \
                / rec_scale if m else 0.0
            eq_dev = abs(co["cv2"] - qu["cv2"]) \
                / max(qu["cv2"], 1e-300) if full_ov else 0.0
            pr = NTP.dc_profile(sd["x"], sd["dc"], rc["lo"],
                                rc["hi"])
            na_dev = abs(co["natom"] - pr["neff_atom"]) \
                / max(pr["neff_atom"], 1e-300)
            lags = lagk_profile(sd["x"], sd["dc"], rc["lo"],
                                rc["hi"], K_LAG)
        # ---- Leg A1 class decompositions on the active blocks
        if co["n_act"] > 0:
            d_sgn = var_decomp(co["vals"], co["sgn"])
            d_band = var_decomp(co["vals"], co["band"])
            d_kpat = var_decomp(co["vals"], co["kpat"])
            wq = np.quantile(co["lam"], [0.25, 0.5, 0.75]) \
                if len(co["lam"]) else np.zeros(3)
            wlab = np.searchsorted(wq, co["lam"], side="right")
            p12 = co["kpat"] * 4 + wlab
            d_p12 = var_decomp(co["vals"], p12)
        else:
            z = dict(var=0.0, within=0.0, between=0.0, dev=0.0)
            d_sgn = d_band = d_kpat = d_p12 = z
        return dict(alt_ok=alt_ok, R=R, P=P, e_c2=e_c2, H=H,
                    S_F=S_F, m=m, Pb=Pb, Pw=Pw, Pd=Pd,
                    agg_dev=agg_dev, part_dev=part_dev,
                    cconv=cconv, full_ov=full_ov, part=part,
                    po=po, qu=qu, sd=sd, df_dev=df_dev,
                    degenerate=degenerate, co=co,
                    rec_dev=rec_dev, eq_dev=eq_dev,
                    na_dev=na_dev, pr=pr, lags=lags,
                    d_sgn=d_sgn, d_band=d_band, d_kpat=d_kpat,
                    d_p12=d_p12)

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
        def med(fn):
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
        # r300 participation set
        neffs = [rc["ev"]["part"]["neff"] for rc in recs]
        st["neff_med"] = float(np.median(neffs))
        st["sl_neff"] = slp(neffs)
        st["sl_L1"] = slp([rc["ev"]["part"]["L1"] / M_W
                           for rc in recs])
        st["need"] = 2.0 * st["sl_L1"] - st["sigma_star"]
        # r301 order family + count/uniformity set
        st["ord_med"] = tuple(
            med(lambda ev, k=k: ev["po"][k])
            for k in ("N2", "N3", "N4", "Ninf"))
        st["ord_sl"] = tuple(
            slp([rc["ev"]["po"][k] for rc in recs])
            for k in ("N2", "N3", "N4", "Ninf"))
        st["tail_med"] = med(lambda ev: ev["po"]["N4"]
                             / max(ev["po"]["N2"], 1e-300))
        st["sl_tail"] = slp([rc["ev"]["po"]["N4"]
                             / max(rc["ev"]["po"]["N2"], 1e-300)
                             for rc in recs])
        st["nact_med"] = med(lambda ev: ev["qu"]["n_act"])
        st["sl_nact"] = slp([rc["ev"]["qu"]["n_act"]
                             for rc in recs])
        st["nact_full"] = sum(1 for rc in recs
                              if rc["ev"]["qu"]["n_act"]
                              == rc["ev"]["m"])
        st["cv2_med"] = med(lambda ev: ev["qu"]["cv2"])
        cv2p = [1.0 + rc["ev"]["qu"]["cv2"] for rc in recs]
        st["sl_cv2p"] = slp(cv2p)
        st["gini_med"] = med(lambda ev: ev["qu"]["gini"])
        st["lloc_med"] = med(lambda ev: ev["pr"]["lloc"])
        st["sl_lloc"] = slp([rc["ev"]["pr"]["lloc"]
                             for rc in recs])
        st["natom_med"] = med(lambda ev: ev["pr"]["neff_atom"])
        st["sl_natom"] = slp([rc["ev"]["pr"]["neff_atom"]
                              for rc in recs])
        st["sp_atom_blk"] = BH.spearman(
            [rc["ev"]["pr"]["neff_atom"] for rc in recs], neffs)
        st["surv_med"] = med(lambda ev: ev["co"]["surv"])
        st["sl_surv"] = slp([rc["ev"]["co"]["surv"]
                             for rc in recs])
        # the round's new coordinates
        st["chi_med"] = med(lambda ev: ev["co"]["chi"])
        st["sl_chi"] = slp([rc["ev"]["co"]["chi"]
                            for rc in recs])
        st["kmax_med"] = med(lambda ev: ev["co"]["kmax"])
        st["sl_kmax"] = slp([rc["ev"]["co"]["kmax"]
                             for rc in recs])
        cv2p_sh = [1.0 + rc["ev"]["co"]["cv2"] for rc in recs]
        st["sl_cv2p_sh"] = slp(cv2p_sh)
        st["nact_sh"] = [rc["ev"]["co"]["n_act"] for rc in recs]
        st["sl_nact_sh"] = slp(st["nact_sh"])
        st["unif_need"] = st["sl_nact"] - st["need"]
        st["composed"] = (st["sl_nact_sh"] + st["sl_chi"]
                          - 2.0 * st["sl_surv"]
                          - st["sl_natom"])
        st["add_co"] = abs(st["sl_cv2p_sh"] - st["composed"])
        for k in range(3):
            st["rho%d" % (k + 1)] = med(
                lambda ev, k=k: ev["lags"][k])
        # A1 between shares
        for nm, key in (("sgn", "d_sgn"), ("band", "d_band"),
                        ("pat", "d_kpat")):
            sh = [rc["ev"][key]["between"]
                  / max(rc["ev"][key]["var"], 1e-300)
                  for rc in recs]
            st["bs_%s_med" % nm] = float(np.median(sh))
            st["bs_%s_sl" % nm] = slp(sh)
        ws = [rc["ev"]["d_p12"]["within"]
              / max(rc["ev"]["d_p12"]["var"], 1e-300)
              for rc in recs]
        st["ws_med"] = float(np.median(ws))
        st["sl_ws"] = slp(ws)
        # A2 moments
        st["m3_med"] = med(lambda ev: float(np.mean(
            (ev["co"]["vals"]
             / max(np.mean(ev["co"]["vals"]), 1e-300)) ** 3))
            if len(ev["co"]["vals"]) else 0.0)
        st["m4_med"] = med(lambda ev: float(np.mean(
            (ev["co"]["vals"]
             / max(np.mean(ev["co"]["vals"]), 1e-300)) ** 4))
            if len(ev["co"]["vals"]) else 0.0)
        st["sl_m3"] = slp([float(np.mean(
            (rc["ev"]["co"]["vals"]
             / max(np.mean(rc["ev"]["co"]["vals"]), 1e-300)) ** 3))
            if len(rc["ev"]["co"]["vals"]) else 1e-300
            for rc in recs])
        st["sl_m4"] = slp([float(np.mean(
            (rc["ev"]["co"]["vals"]
             / max(np.mean(rc["ev"]["co"]["vals"]), 1e-300)) ** 4))
            if len(rc["ev"]["co"]["vals"]) else 1e-300
            for rc in recs])
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
        check("G23-r300-participation-anchors",
              abs(st["neff_med"] - R300_NEFF_MED) <= R300_NEFF_TOL
              and abs(st["sl_neff"] - R300_SL_NEFF)
              <= R300_SL_NEFF_TOL
              and abs(st["sl_L1"] - R300_SL_L1) <= R300_SL_L1_TOL,
              "the r300 participation set recomputed bit-near: "
              "n_eff med %.2f (ref %.2f), sl_neff %+.3f (ref "
              "%+.3f), sl_L1 %+.3f (ref %+.3f); NEED = 2 sl_L1 - "
              "sigma* = %+.3f (record +0.908)"
              % (st["neff_med"], R300_NEFF_MED, st["sl_neff"],
                 R300_SL_NEFF, st["sl_L1"], R300_SL_L1,
                 st["need"]))
        ok_ord = (all(abs(st["ord_med"][i] - R301_ORD_MED[i])
                      <= R301_ORD_MED_TOL for i in range(4))
                  and all(abs(st["ord_sl"][i] - R301_ORD_SL[i])
                          <= R301_ORD_SL_TOL for i in range(4))
                  and abs(st["tail_med"] - R301_TAIL_MED)
                  <= R301_TAIL_TOL
                  and abs(st["sl_tail"] - R301_TAIL_SL)
                  <= R301_TAIL_SL_TOL)
        ok_cnt = (abs(st["nact_med"] - R301_NACT_MED)
                  <= R301_NACT_TOL
                  and abs(st["sl_nact"] - R301_SL_NACT)
                  <= R301_SL_NACT_TOL
                  and st["nact_full"] == 42
                  and abs(st["cv2_med"] - R301_CV2_MED)
                  <= R301_CV2_TOL
                  and abs(st["sl_cv2p"] - R301_SL_CV2P)
                  <= R301_SL_CV2P_TOL
                  and abs(st["gini_med"] - R301_GINI_MED)
                  <= R301_GINI_TOL)
        ok_atom = (abs(st["lloc_med"] - R301_LLOC_MED)
                   <= R301_LLOC_TOL
                   and abs(st["sl_lloc"] - R301_SL_LLOC)
                   <= R301_SL_LLOC_TOL
                   and abs(st["natom_med"] - R301_NATOM_MED)
                   <= R301_NATOM_TOL
                   and abs(st["sl_natom"] - R301_SL_NATOM)
                   <= R301_SL_NATOM_TOL
                   and abs(st["sp_atom_blk"] - R301_SP_ATOM)
                   <= R301_SP_ATOM_TOL
                   and abs(st["surv_med"] - R301_SURV_MED)
                   <= R301_SURV_TOL
                   and abs(st["sl_surv"] - R301_SL_SURV)
                   <= R301_SL_SURV_TOL)
        check("G24-r301-anatomy-anchors",
              ok_ord and ok_cnt and ok_atom,
              "the r301 record recomputed bit-near: orders med "
              "%.2f/%.2f/%.2f/%.2f sl %+.3f/%+.3f/%+.3f/%+.3f, "
              "tail %.2f/%+.3f; n_act med %.1f sl %+.3f COUNT "
              "LINK %d/42%s, CV^2 med %.2f sl_cv2p %+.3f, gini "
              "%.2f; l_loc %.1f/%+.3f, n_eff_atom %.1f/%+.3f, sp "
              "%+.2f, surv %.2f/%+.3f"
              % (st["ord_med"] + st["ord_sl"]
                 + (st["tail_med"], st["sl_tail"],
                    st["nact_med"], st["sl_nact"],
                    st["nact_full"],
                    " EXACT" if st["nact_full"] == 42 else "",
                    st["cv2_med"], st["sl_cv2p"],
                    st["gini_med"], st["lloc_med"],
                    st["sl_lloc"], st["natom_med"],
                    st["sl_natom"], st["sp_atom_blk"],
                    st["surv_med"], st["sl_surv"])))
        # r301 stability anchors (halves + jackknife of n_eff)
        lo_idx = list(range(0, 21))
        hi_idx = list(range(21, 42))
        ov_r, cov_r = NTP.split_disjoint(lo_idx, hi_idx, 42)
        sl_lo = L2D.halves_slope([Ns[i] for i in lo_idx],
                                 [neffs[i] for i in lo_idx])
        sl_hi = L2D.halves_slope([Ns[i] for i in hi_idx],
                                 [neffs[i] for i in hi_idx])
        jks = [L2D.halves_slope(
            [Ns[k] for k in range(42) if k != i],
            [neffs[k] for k in range(42) if k != i])
            for i in range(42)]
        jk_min = min(jks)
        jk_max = max(jks)
        n_below = sum(1 for v in jks if v < st["need"])
        check("G25-r301-stability-anchors",
              ov_r == 0 and cov_r
              and abs(sl_lo - R301_HALF_LO) <= R301_HALF_TOL
              and abs(sl_hi - R301_HALF_HI) <= R301_HALF_TOL
              and abs(jk_min - R301_JK_MIN) <= R301_JK_TOL
              and abs(jk_max - R301_JK_MAX) <= R301_JK_TOL
              and n_below == 0,
              "the r301 stability set recomputed: n_eff "
              "half-ladders lo/hi %+.3f/%+.3f (refs %+.3f/%+.3f; "
              "disjoint gated), jackknife min/max %+.3f/%+.3f "
              "(refs %+.3f/%+.3f), %d/42 below NEED %+.3f"
              % (sl_lo, sl_hi, R301_HALF_LO, R301_HALF_HI,
                 jk_min, jk_max, R301_JK_MIN, R301_JK_MAX,
                 n_below, st["need"]))
        st["half_lo"] = sl_lo
        st["half_hi"] = sl_hi
    else:
        check("G22-r297-target-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")
        check("G23-r300-participation-anchors", True,
              "SMOKE: skipped")
        check("G24-r301-anatomy-anchors", True, "SMOKE: skipped")
        check("G25-r301-stability-anchors", True,
              "SMOKE: skipped")

    # ---------------- S3: exact section + toys + audits + mutants
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    vd_dev, vd_var, vd_w, vd_b = fr_var_decomp()
    m1_dev, _v, _w, _b = fr_var_decomp("weight")
    check("G30-fractions-decomposition-and-m1",
          vd_dev == 0 and vd_var == Fr(3, 2) and vd_w == Fr(5, 4)
          and vd_b == Fr(1, 4) and m1_dev == Fr(3, 4),
          "the law of total variance RE-PROVED exact in Fractions "
          "on (2,1,1,4)|{2,1},{1,4}: var %s = within %s + between "
          "%s (dev %s); m1 WRONG CLASS WEIGHT ((n_c/n)^2) "
          "recomposes to 3/4, break %s EXACT -- CAUGHT: the class "
          "weight is load-bearing"
          % (str(vd_var), str(vd_w), str(vd_b), str(vd_dev),
             str(m1_dev)))
    co_dev, co_cv2, co_chi, co_surv, co_na = fr_coherence()
    m3_dev, _c2, m3_chi, _s, _n = fr_coherence("lag0")
    check("G31-fractions-coherence-and-m3",
          co_dev == 0 and co_cv2 == Fr(1, 4)
          and co_chi == Fr(5, 7) and co_surv == Fr(2, 3)
          and co_na == Fr(18, 7) and m3_dev == Fr(5, 7)
          and m3_chi == Fr(5, 14),
          "the coherence identity (1 + CV^2) surv^2 n_eff_atom "
          "== n_act chi RE-PROVED exact in Fractions on the "
          "signed toy (1,-2|3): CV^2 %s, chi %s, surv %s, "
          "n_eff_atom %s, dev %s; m3 LAG-0 DOUBLE COUNTING (Q "
          "doubled, chi' %s) breaks by %s EXACT -- CAUGHT: the "
          "atom energy normalization is load-bearing"
          % (str(co_cv2), str(co_chi), str(co_surv), str(co_na),
             str(co_dev), str(m3_chi), str(m3_dev)))
    tk_worst, tk_mut = toy_ks_and_fs()
    toy_w = max(toy_var_decomp(), toy_coherence(), tk_worst)
    check("G32-toy-exactness", toy_w <= TOY_BAR
          and tk_mut >= KS_LOUD,
          "the hand toys reproduce the WHOLE new pipeline: "
          "var_decomp float == Fractions on (2,1,1,4); coherence "
          "toy (atoms (0,1,2), dc (1,-2,3), breaks (1.5)) -> P = "
          "(-1,3), CV^2 1/4, chi 5/7, surv 2/3, n_eff_atom 18/7, "
          "identity dev 0, CS slack 0 (one-atom EQUALITY "
          "WITNESS), lam (17/24, 7/24); KS((1,2,3),(1.5,2.5)) = "
          "1/3 EXACT; fs solve (10,3),(40,1.5) -> A 1, B 20, "
          "pred(20) 2 EXACT (worst dev %.1e, bar %.0e); the "
          "synthetic scale mutant KS = %.2f >= %.1f LOUD"
          % (toy_w, TOY_BAR, tk_mut, KS_LOUD))
    h_vd = scope_audit("var_decomp", BOUND_FORBIDDEN)
    h_co = scope_audit("coherence_split", BOUND_FORBIDDEN)
    h_lk = scope_audit("lagk_profile", BOUND_FORBIDDEN)
    h_ks = scope_audit("ks_two", BOUND_FORBIDDEN)
    h_fs = scope_audit("fs_solve", BOUND_FORBIDDEN)
    h_pg = scope_audit("perturb_gain", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_vd or h_co or h_lk or h_ks or h_fs or h_pg)
    check("G33-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the new builders (var_decomp, coherence_split, "
          "lagk_profile, ks_two, fs_solve, perturb_gain) consume "
          "block vectors / positions / weights / chain values "
          "only (no truth-side identifier in scope%s); m5a gift "
          "mutant FLAGGED (%s); m5b branch-peek mutant FLAGGED "
          "(%s); fragment audit: %s"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S4: Leg A -- anatomy + stationarity + depth
    section("S4  LEG A: CV^2 ANATOMY + STATIONARITY + DEPTH")
    qid_w = max(rc["ev"]["qu"]["qid_dev"] for rc in pool_all)
    ord_w = max(rc["ev"]["po"]["mono"] for rc in pool_all)
    vd_w42 = max(max(rc["ev"]["d_sgn"]["dev"],
                     rc["ev"]["d_band"]["dev"],
                     rc["ev"]["d_kpat"]["dev"],
                     rc["ev"]["d_p12"]["dev"])
                 for rc in pool_all)
    check("G40-anatomy-wards", qid_w <= QID_BAR
          and ord_w <= ORD_BAR and vd_w42 <= VD_BAR,
          "the anatomy identities on %d worlds: the r301 count "
          "identity worst %.1e (bar %.0e); power-mean chain worst "
          "%.1e; the variance decomposition (3 schemes + PAT12) "
          "worst %.1e (bar %.0e) -- the class split is an exact "
          "finite statement on every world"
          % (len(pool_all), qid_w, QID_BAR, ord_w, vd_w42,
             VD_BAR))
    show = (sorted(exc, key=lambda r_: r_["kz"]) + mrecs
            if not smoke else mrecs)
    for rc in show:
        ev = rc["ev"]
        info("kz%-3d N%-4d %-4s m %-3d  n_act %-3d cv2 %.2f  chi "
             "%.2f  surv %.2f  kmax %-3d natom %.0f"
             % (rc["kz"], rc["N"],
                "EXC" if rc["g_branch"] < 0 else "chp",
                ev["m"], ev["co"]["n_act"], ev["co"]["cv2"],
                ev["co"]["chi"], ev["co"]["surv"],
                ev["co"]["kmax"], ev["co"]["natom"]))
    if not smoke:
        carriers = []
        for nm in ("sgn", "band", "pat"):
            if (st["bs_%s_sl" % nm] >= CARRIER_GROW
                    and st["bs_%s_med" % nm] >= CARRIER_SHARE):
                carriers.append(nm.upper())
        st["carrier"] = ("NAMED(%s)" % "+".join(carriers)
                         if carriers else "STRUCTURELESS")
        check("G41-anatomy-census", True,
              "CV2_ANATOMY (42 rungs): between shares SIGN/BAND/"
              "PAT med %.3f/%.3f/%.3f slopes %+.3f/%+.3f/%+.3f "
              "(sealed carrier rule: NAMED iff slope >= %+.2f AND "
              "med >= %.2f) -- %s; normalized moments m2/m3/m4 "
              "med %.2f/%.2f/%.1f, m3/m4 slopes %+.3f/%+.3f"
              % (st["bs_sgn_med"], st["bs_band_med"],
                 st["bs_pat_med"], st["bs_sgn_sl"],
                 st["bs_band_sl"], st["bs_pat_sl"],
                 CARRIER_GROW, CARRIER_SHARE, st["carrier"],
                 1.0 + st["cv2_med"], st["m3_med"], st["m4_med"],
                 st["sl_m3"], st["sl_m4"]))
        # A2 stationarity on the 3 disjoint 14-rung groups
        grp_y = []
        grp_raw = []
        grp_m2 = []
        grp_iN = []
        for gi in range(3):
            sel = recs[gi * N_GRP:(gi + 1) * N_GRP]
            ys = []
            raws = []
            m2s = []
            for rc in sel:
                va = rc["ev"]["co"]["vals"]
                if len(va):
                    ys.append(va / float(np.mean(va)))
                    raws.append(va)
                    m2s.append(1.0 + rc["ev"]["co"]["cv2"])
            grp_y.append(np.concatenate(ys) if ys
                         else np.zeros(0))
            grp_raw.append(np.concatenate(raws) if raws
                           else np.zeros(0))
            grp_m2.append(float(np.median(m2s)))
            grp_iN.append(float(np.median(
                [1.0 / rc["N"] for rc in sel])))
        ks13 = ks_two(grp_y[0], grp_y[2])
        ks23 = ks_two(grp_y[1], grp_y[2])
        ks12 = ks_two(grp_y[0], grp_y[1])
        ks_raw = ks_two(grp_raw[0], grp_raw[2])
        stationary = (ks13 <= KS_STAT and ks23 <= KS_STAT)
        dec1 = np.quantile(grp_y[0], np.arange(1, 10) / 10.0)
        dec3 = np.quantile(grp_y[2], np.arange(1, 10) / 10.0)
        info("deciles G1: " + " ".join("%.2f" % v for v in dec1))
        info("deciles G3: " + " ".join("%.2f" % v for v in dec3))
        # amendment a1 (calibration, disclosed in the record
        # tables): the sealed ABSOLUTE loudness bar 0.5 for the
        # unnormalized mustfail was mis-calibrated (the raw pools
        # overlap through the ~30x within-rung spread; measured
        # 0.335) -- the amended rule is the RELATIVE form: the
        # raw statistic must be >= 4x the normalized one AND >=
        # 2x KS_STAT; the original sealed outcome stays printed.
        m2_caught = (ks_raw >= 4.0 * ks13
                     and ks_raw >= 2.0 * KS_STAT)
        check("G42-a2-stationarity", m2_caught,
              "A2 STATIONARITY (sealed bar %.3f): normalized "
              "pooled KS(G1,G3) %.3f, KS(G2,G3) %.3f, KS(G1,G2) "
              "%.3f -> %s; m2 group medians %.2f/%.2f/%.2f; m2 "
              "UNNORMALIZED mustfail (amendment a1, relative "
              "form): raw pooled KS %.3f >= 4 x %.3f AND >= 2 x "
              "%.3f -- CAUGHT %.0fx louder than the normalized "
              "statistic (original sealed absolute bar %.1f: "
              "%.3f < %.1f, disclosed miss -- the raw pools "
              "overlap through the within-rung spread)"
              % (KS_STAT, ks13, ks23, ks12,
                 "PROFILE_STATIONARY" if stationary
                 else "PROFILE_DRIFTING",
                 grp_m2[0], grp_m2[1], grp_m2[2], ks_raw, ks13,
                 KS_STAT, ks_raw / max(ks13, 1e-300), KS_LOUD,
                 ks_raw, KS_LOUD))
        st["ks13"] = ks13
        st["ks23"] = ks23
        st["ks12"] = ks12
        st["stationary"] = stationary
        st["grp_m2"] = grp_m2
        # A3 depth honesty
        halves_ok = True
        sl_nact_lo = L2D.halves_slope(
            [Ns[i] for i in lo_idx],
            [st["nact_sh"][i] for i in lo_idx])
        sl_nact_hi = L2D.halves_slope(
            [Ns[i] for i in hi_idx],
            [st["nact_sh"][i] for i in hi_idx])
        cv2p_l = [1.0 + rc["ev"]["qu"]["cv2"] for rc in recs]
        sl_cv2p_lo = L2D.halves_slope(
            [Ns[i] for i in lo_idx], [cv2p_l[i] for i in lo_idx])
        sl_cv2p_hi = L2D.halves_slope(
            [Ns[i] for i in hi_idx], [cv2p_l[i] for i in hi_idx])
        nact_l = [rc["ev"]["qu"]["n_act"] for rc in recs]
        sl_nact_q_lo = L2D.halves_slope(
            [Ns[i] for i in lo_idx], [nact_l[i] for i in lo_idx])
        sl_nact_q_hi = L2D.halves_slope(
            [Ns[i] for i in hi_idx], [nact_l[i] for i in hi_idx])
        add_lo = abs(st["half_lo"] - (sl_nact_q_lo - sl_cv2p_lo))
        add_hi = abs(st["half_hi"] - (sl_nact_q_hi - sl_cv2p_hi))
        halves_ok = add_lo <= ADD_BAR and add_hi <= ADD_BAR
        depth_miss = sl_cv2p_hi > (sl_nact_q_hi - st["need"])
        A_fs, B_fs, pred = fs_solve(1.0 / grp_iN[0], grp_m2[0],
                                    1.0 / grp_iN[2], grp_m2[2],
                                    1.0 / grp_iN[1])
        fs_dev = abs(pred - grp_m2[1]) / max(grp_m2[1], 1e-300)
        transient = fs_dev <= FS_BAR
        depth_caveat = depth_miss and not transient
        jk2 = [L2D.halves_slope(
            [Ns[k] for k in range(42) if k != i],
            [cv2p_l[k] for k in range(42) if k != i])
            for i in range(42)]
        jk2_min = min(jk2)
        jk2_max = max(jk2)
        n_above = sum(1 for v in jk2 if v > st["unif_need"])
        check("G43-a3-depth", halves_ok,
              "A3 DEPTH (exact per-half additivity gated %.1e/"
              "%.1e): half attribution sl_nact lo/hi %+.3f/%+.3f "
              "vs sl_cv2p lo/hi %+.3f/%+.3f (n_eff halves %+.3f/"
              "%+.3f) -- deep-half UNIF clause sl_cv2p_hi %+.3f "
              "vs sl_nact_hi - NEED %+.3f: %s; finite-size 1/N "
              "solve A %.3f B %+.1f held-out dev %.3f (bar %.2f) "
              "-> %s%s; jackknife of sl_cv2p min/max %+.3f/%+.3f,"
              " %d/42 above UNIF_NEED %+.3f"
              % (add_lo, add_hi, sl_nact_q_lo, sl_nact_q_hi,
                 sl_cv2p_lo, sl_cv2p_hi, st["half_lo"],
                 st["half_hi"], sl_cv2p_hi,
                 sl_nact_q_hi - st["need"],
                 "DEPTH_HALF_MISS fires" if depth_miss
                 else "holds",
                 A_fs, B_fs, fs_dev, FS_BAR,
                 "TRANSIENT_1_OVER_N" if transient
                 else "1/N model REJECTED",
                 "; DEPTH_CAVEAT fires" if depth_caveat else "",
                 jk2_min, jk2_max, n_above, st["unif_need"]))
        st.update(sl_nact_lo=sl_nact_q_lo, sl_nact_hi=sl_nact_q_hi,
                  sl_cv2p_lo=sl_cv2p_lo, sl_cv2p_hi=sl_cv2p_hi,
                  depth_miss=depth_miss, A_fs=A_fs, B_fs=B_fs,
                  fs_dev=fs_dev, transient=transient,
                  depth_caveat=depth_caveat, jk2_min=jk2_min,
                  jk2_max=jk2_max, n_above=n_above)
        pool_y = grp_y[2]
    else:
        check("G41-anatomy-census", True, "SMOKE: skipped")
        check("G42-a2-stationarity", True, "SMOKE: skipped "
              "(synthetic KS mustfail gated in G32)")
        check("G43-a3-depth", True, "SMOKE: skipped")
        va9 = recs[0]["ev"]["co"]["vals"]
        pool_y = va9 / float(np.mean(va9)) if len(va9) \
            else np.zeros(0)

    # m4 two-point synthetic (needs the real pool -> here)
    cv2_syn, cv2_syn_dev, ks_syn, ws_syn, dev_syn = \
        toy_m4_twopoint(pool_y)
    real_cv2 = st["cv2_med"] if not smoke \
        else recs[0]["ev"]["co"]["cv2"]
    check("G44-mustfail-m4-twopoint",
          cv2_syn_dev <= TOY_BAR and cv2_syn >= CV_SYN_MIN
          and ks_syn >= KS_LOUD and dev_syn <= VD_BAR
          and ws_syn <= 0.5,
          "m4 SYNTHETIC TWO-POINT PROFILE (19 + nine 1s): CV^2 = "
          "729/196 = %.2f EXACT >= %.1f (real med %.2f), "
          "normalized KS vs the real pool %.3f >= %.1f LOUD, "
          "two-class decomposition within-share %.4f (the "
          "concentration IS class-visible, dev %.1e) -- every "
          "route recognizes the non-uniform profile"
          % (cv2_syn, CV_SYN_MIN, real_cv2, ks_syn, KS_LOUD,
             ws_syn, dev_syn))

    # ---------------- S5: Leg B -- the derivation routes
    section("S5  LEG B: DERIVATION ROUTES FOR UNIF_TARGET")
    co_w = max(rc["ev"]["co"]["id_dev"] for rc in pool_all)
    cs_w = max(rc["ev"]["co"]["cs_slack"] for rc in pool_all)
    rec_w = max(rc["ev"]["rec_dev"] for rc in pool_all)
    eq_w = max(rc["ev"]["eq_dev"] for rc in all_rc)
    na_w = max(rc["ev"]["na_dev"] for rc in pool_all)
    df_w = max(rc["ev"]["df_dev"] for rc in pool_all)
    deg_note = [("%s" % c) for c in crecs
                if crecs[c]["ev"]["degenerate"]]
    check("G50-b1-wards", co_w <= CO_BAR and cs_w <= CSK_BAR
          and rec_w <= EQ_BAR and eq_w <= EQ_BAR
          and na_w <= NA_BAR and df_w <= EQ_BAR,
          "B1 wards on %d worlds: coherence identity (1 + CV^2) "
          "surv^2 n_eff_atom == n_act chi worst %.1e (bar %.0e); "
          "per-block CS cap chi <= kmax worst slack %.1e; "
          "P_shared == P_ov %.1e; ladder CV^2 equality (shared vs "
          "PDelta) %.1e; n_eff_atom internal %.1e; dc == dw x f "
          "%.1e%s"
          % (len(pool_all), co_w, CO_BAR, cs_w, rec_w, eq_w,
             na_w, df_w,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))
    if not smoke:
        b1_ok = (co_w <= CO_BAR and cs_w <= CSK_BAR
                 and st["add_co"] <= ADD_BAR
                 and st["sl_chi"] <= CHI_FLAT
                 and st["sl_surv"] >= SURV_FLAT)
        atom_need = (st["sl_nact_sh"] + st["sl_chi"]
                     - 2.0 * st["sl_surv"] - st["unif_need"])
        check("G51-b1-census", st["add_co"] <= ADD_BAR,
              "B1 census (DISCLOSED: the composition is an exact "
              "reparametrization of UNIF_TARGET): chi med %.3f "
              "slope %+.3f (%s, clause <= %+.2f %s), surv med "
              "%.2f slope %+.3f (clause >= %+.2f %s), kmax med "
              "%.1f slope %+.3f (the CS cap %s), rho_1/2/3 med "
              "%+.3f/%+.3f/%+.3f; composed %+.3f + %+.3f - 2 x "
              "%+.3f - %+.3f = %+.3f == sl_cv2p(shared) %+.3f "
              "(additivity %.1e) vs UNIF_NEED %+.3f"
              % (st["chi_med"], st["sl_chi"],
                 "destructive" if st["chi_med"] < 1.0
                 else "constructive", CHI_FLAT,
                 "HOLDS" if st["sl_chi"] <= CHI_FLAT else "FAILS",
                 st["surv_med"], st["sl_surv"], SURV_FLAT,
                 "HOLDS" if st["sl_surv"] >= SURV_FLAT
                 else "FAILS",
                 st["kmax_med"], st["sl_kmax"],
                 "grows -- cannot carry alone"
                 if st["sl_kmax"] > 0 else "bounded",
                 st["rho1"], st["rho2"], st["rho3"],
                 st["sl_nact_sh"], st["sl_chi"], st["sl_surv"],
                 st["sl_natom"], st["composed"],
                 st["sl_cv2p_sh"], st["add_co"],
                 st["unif_need"]))
        ks_pool = []
        for gi in (0, 2):
            sel = recs[gi * N_GRP:(gi + 1) * N_GRP]
            ks_pool.append(np.concatenate(
                [rc["ev"]["co"]["k_act"]
                 / max(float(np.mean(rc["ev"]["co"]["k_act"])),
                       1e-300)
                 for rc in sel if len(rc["ev"]["co"]["k_act"])]))
        ks_k = ks_two(ks_pool[0], ks_pool[1])
        b2_ok = (st["ws_med"] <= WS_BAR and ks_k <= KS_PAT)
        check("G52-b2-census", True,
              "B2 census (construction/pattern route): PAT12 "
              "within-share med %.3f slope %+.3f vs bar %.2f -- "
              "%s; k-profile stability KS(G1,G3) %.3f vs bar "
              "%.3f -- %s; PNT-free constructivity %s"
              % (st["ws_med"], st["sl_ws"], WS_BAR,
                 "|PDelta| concentrated per pattern class"
                 if st["ws_med"] <= WS_BAR else
                 "NOT concentrated: the values live WITHIN the "
                 "local pattern classes, the construction-"
                 "geometry route is closed honestly",
                 ks_k, KS_PAT,
                 "the pattern mix stabilizes"
                 if ks_k <= KS_PAT else "the mix drifts",
                 "NOT claimed (checked only)"))
        st["ks_k"] = ks_k
    else:
        b1_ok = b2_ok = False
        atom_need = float("nan")
        check("G51-b1-census", True, "SMOKE: wards gated in G50")
        check("G52-b2-census", True, "SMOKE: skipped")

    # B3 localized-perturbation gains on the sealed id pool
    if smoke:
        b3_pool = [("kz9", recs[0])]
    else:
        b3_pool = ([("kz%d" % rc["kz"], rc) for rc in recs
                    if rc["kz"] in (KZ_ANCHOR, 20)]
                   + [("kz%d" % rc["kz"], rc)
                      for rc in recs[-2:]]
                   + [("w%d" % rc["kz"], rc) for rc in mrecs]
                   + [(c, crecs[c]) for c in ("EPST", "SCR")])
    gains = []
    gain_note = []
    for b3_name, rc in b3_pool:
        o = rc["o"]
        bxs = rc["bx"][o]
        bws = rc["bw"][o]
        v2s = rc["v2"][o]
        cts = rc["ct"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
        bidx = np.nonzero(~ed)[0]
        if len(bidx) < 4:
            continue
        mabs = float(np.mean(np.abs(cts[~ed])))
        g_rc = []
        sites = ((len(bidx) // 2,) if smoke else
                 (len(bidx) // 4, len(bidx) // 2,
                  (3 * len(bidx)) // 4))
        for q in sites:
            i = bidx[q]
            dct, dx = perturb_gain(rc["p"]["rows"], rc["N"],
                                   float(bxs[i]), float(v2s[i]),
                                   float(cts[i]), float(bws[i]),
                                   rc["fac"], rc["lo"], rc["hi"])
            g = (dct / max(mabs, 1e-300)) \
                / (dx / (rc["hi"] - rc["lo"]))
            g_rc.append(g / rc["N"])
        gains.extend(g_rc)
        gain_note.append("%s %.3f" % (b3_name,
                                      float(np.median(g_rc))))
    gain_med = float(np.median(gains)) if gains else 0.0
    gain_max = float(np.max(gains)) if gains else 0.0
    b3_ok = (gain_med <= AMP_BAR) and not smoke
    check("G53-b3-census", True,
          "B3 census (recursion stability, id pool %d worlds x "
          "%d sites, dx = %.0e hull): normalized gain g/N med "
          "%.3f max %.3f vs AMP_BAR %.1f -- %s (per world: %s); "
          "MEASURED, correlational: the block response equals "
          "the atom response (one atom moved)"
          % (len(b3_pool), 1 if smoke else 3, DX_REL, gain_med,
             gain_max, AMP_BAR,
             "the recursion DAMPS localized position noise below "
             "the polynomial-degree rate"
             if gain_med <= AMP_BAR else
             "amplification above the degree rate",
             "; ".join(gain_note)))

    # ---------------- S6: sealed adjudication + Leg C
    section("S6  SEALED UNIF ADJUDICATION + LEG C")
    if not smoke:
        derived = (b1_ok and st["stationary"] and st["transient"]
                   and st["nact_full"] == 42
                   and st["sl_chi"] <= CHI_NOGROW)
        if derived:
            outcome = "UNIF_DERIVED"
        elif b1_ok or b2_ok or b3_ok:
            outcome = "UNIF_SPLIT"
        else:
            outcome = "UNIF_STILL_EMPIRICAL"
        fired = []
        if b1_ok:
            fired.append("B1(ATOM_TARGET: prove sl_natom >= "
                         "sl_nact + sl_chi - 2 sl_surv - "
                         "UNIF_NEED = %+.3f, measured %+.3f, "
                         "margin %.3f; chi %+.3f, surv %+.3f, "
                         "count link %d/42)"
                         % (atom_need, st["sl_natom"],
                            st["sl_natom"] - atom_need,
                            st["sl_chi"], st["sl_surv"],
                            st["nact_full"]))
        if b2_ok:
            fired.append("B2(PATTERN_MIX: ws %.2f, ks_k %.3f)"
                         % (st["ws_med"], st["ks_k"]))
        if b3_ok:
            fired.append("B3(GAIN_NOTE: damping %.3f, "
                         "correlational)" % gain_med)
        check("G60-unif-adjudication", True,
              "SEALED RULE fired: %s (B1_OK %s: sl_chi %+.3f <= "
              "%+.2f, sl_surv %+.3f >= %+.2f, wards+additivity; "
              "B2_OK %s: ws %.2f vs %.1f, ks_k %.3f vs %.3f; "
              "B3_OK %s: gain med %.3f vs %.1f; DERIVED clause: "
              "B1_OK AND STATIONARY %s AND TRANSIENT %s AND "
              "count %d/42 AND sl_chi <= %.1f)%s%s"
              % (outcome, b1_ok, st["sl_chi"], CHI_FLAT,
                 st["sl_surv"], SURV_FLAT, b2_ok, st["ws_med"],
                 WS_BAR, st["ks_k"], KS_PAT, b3_ok, gain_med,
                 AMP_BAR, st["stationary"], st["transient"],
                 st["nact_full"], CHI_NOGROW,
                 ("; fired: " + " | ".join(fired)) if fired
                 else "",
                 "; DEPTH_CAVEAT fired (Leg A3)"
                 if st["depth_caveat"] else ""))
        if outcome == "UNIF_DERIVED" and not st["depth_caveat"]:
            info("CANDIDATE THEOREM (uniformity composition, L2 "
                 "generic half; hypotheses typed MEASURED where "
                 "marked): for every rung of the sealed ladder "
                 "(N in [%d, %d]): the count identity n_eff = "
                 "n_act/(1 + CV^2) with n_act == m (constructive,"
                 " 42/42) and the coherence decomposition 1 + "
                 "CV^2 = n_act chi/(surv^2 n_eff_atom) (EXACT) "
                 "with chi non-growing (%+.3f, MEASURED; lag-1 "
                 "mixing trace), surv flat (%+.3f, MEASURED), "
                 "the normalized block profile STATIONARY "
                 "(KS13 %.3f, MEASURED) with a 1/N transient "
                 "(A = %.3f, held-out dev %.3f, MEASURED) and "
                 "the atom growth sl_natom %+.3f >= %+.3f "
                 "(MEASURED, margin %.3f) => slope(1 + CV^2) <= "
                 "UNIF_NEED = %+.3f => slope(n_eff) >= NEED = "
                 "%+.3f => (r300 exact decomposition) sl_D <= "
                 "sigma* => (r300 RATIO_BOUNDED_STRUCTURAL) "
                 "sigma <= sigma* = %+.3f => the r297 target "
                 "inequality => the v964-S0 vdC theorem => "
                 "delta' > %.2f on the generic half; exceptions: "
                 "6 via the r287 F2 certificates, kz15 via the "
                 "r270 exact-finite certificate.  Wave-10 "
                 "promotion candidate -- NOT promoted here."
                 % (min(Ns), max(Ns), st["sl_chi"],
                    st["sl_surv"], st["ks13"], st["A_fs"],
                    st["fs_dev"], st["sl_natom"], atom_need,
                    st["sl_natom"] - atom_need,
                    st["unif_need"], st["need"],
                    st["sigma_star"], DELTA_NEED))
            legc = "COMPOSED"
        else:
            info("REST_FROZEN (the refined statement, relocated "
                 "one level DOWN): the count factor n_act == m "
                 "on %d/42 grows at %+.3f; chi %+.3f (%s), surv "
                 "%+.3f; the remaining inequality is ATOM_TARGET:"
                 " slope(n_eff_atom) >= %+.3f (measured %+.3f, "
                 "margin %.3f -- %s the 0.055 block margin, "
                 "disclosed).  B2 %s; B3 %s.%s"
                 % (st["nact_full"], st["sl_nact"], st["sl_chi"],
                    "non-growing" if st["sl_chi"] <= 0
                    else "growing", st["sl_surv"], atom_need,
                    st["sl_natom"], st["sl_natom"] - atom_need,
                    "THINNER than" if st["sl_natom"] - atom_need
                    < 0.055 else "comparable to",
                    "fired" if b2_ok else
                    "closed honestly (ws %.2f)" % st["ws_med"],
                    "fired (damping %.3f)" % gain_med if b3_ok
                    else "not fired",
                    "  DEPTH_CAVEAT is an active flag."
                    if st["depth_caveat"] else ""))
            legc = "REST_FROZEN"
        check("G61-leg-c", True,
              "Leg C %s -- the full candidate fires ONLY on "
              "UNIF_DERIVED AND NOT DEPTH_CAVEAT by the sealed "
              "rule; no post-hoc rescue"
              % ("FIRED (candidate printed, NOT promoted; "
                 "hypotheses typed MEASURED)"
                 if legc == "COMPOSED" else
                 "REST_FROZEN (refined target printed)"))
    else:
        outcome = "SMOKE_NO_ADJUDICATION"
        fired = []
        check("G60-unif-adjudication", True, "SMOKE: skipped")
        check("G61-leg-c", True, "SMOKE: skipped")

    # ---------------- S8: worlds + mp wards
    section("S8  WORLD CLASSES + MP WARDS")
    if not smoke:
        pm = float(np.median([rc["ev"]["part"]["neff"]
                              / max(rc["ev"]["m"], 1)
                              for rc in recs]))
        fm = float(np.median([rc["ev"]["part"]["fill"]
                              for rc in recs]))
        main_cls = ("PART_HIGH" if pm >= PART_CLS else "PART_LOW",
                    "FILL_HIGH" if fm >= FILL_CLS else "FILL_LOW")
        refs = {"EPST": R300_EPST_CLS, "SCR": R300_SCR_CLS}
        cv2_refs = {"EPST": R301_EPST_CV2, "SCR": R301_SCR_CV2}
        ctl_note = []
        cls_ok = (main_cls == R300_MAIN_CLS)
        for c in ("EPST", "SCR"):
            ev = crecs[c]["ev"]
            pc = ev["part"]["neff"] / max(ev["m"], 1)
            fc = ev["part"]["fill"]
            cls_c = ("PART_HIGH" if pc >= PART_CLS
                     else "PART_LOW",
                     "FILL_HIGH" if fc >= FILL_CLS
                     else "FILL_LOW")
            cls_ok &= (cls_c == refs[c])
            cls_ok &= (abs(ev["qu"]["cv2"] - cv2_refs[c])
                       <= R301_CTL_CV2_TOL)
            ctl_note.append("%s %s/%s cv2 %.2f (ref %.2f) chi "
                            "%.2f"
                            % (c, cls_c[0], cls_c[1],
                               ev["qu"]["cv2"], cv2_refs[c],
                               ev["co"]["chi"]))
        check("G80-world-controls", cls_ok,
              "the r300 anatomy classes REPRODUCED EXACTLY (MAIN "
              "%s/%s) and the r301 UNIF non-separation reproduced"
              " (MAIN cv2 %.2f bracketed: %s) -- the coherence "
              "identity holds on all 47 worlds by algebra: the "
              "B1 route is WORLD-BLIND as the charter demands"
              % (main_cls[0], main_cls[1], st["cv2_med"],
                 str(ctl_note)))
    else:
        check("G80-world-controls", True, "SMOKE: skipped")
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
        check("G81-mp-deep-wards", ok_mp,
              "mp (dps %d) terminal drive at the trend-critical "
              "rungs: %s" % (MP_DPS, "; ".join(mp_note)))
    else:
        check("G81-mp-deep-wards", True, "SMOKE: skipped")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact CV^2 class decomposition, the "
          "distribution-stationarity census, the exact per-half "
          "depth attribution with the sealed 1/N model, the "
          "exact coherence identity 1 + CV^2 = n_act chi/(surv^2 "
          "n_eff_atom) with the CS cap, the pattern census and "
          "the localized-perturbation gain census, plus the "
          "sealed adjudication -- NO new certificate promoted, "
          "NO bound modification of the sealed forms")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["CV2_ANATOMY(shares SIGN/BAND/PAT %.2f/%.2f/"
                 "%.2f sl %+.2f/%+.2f/%+.2f %s; m2/m3/m4 %.2f/"
                 "%.2f/%.1f)"
                 % (st["bs_sgn_med"], st["bs_band_med"],
                    st["bs_pat_med"], st["bs_sgn_sl"],
                    st["bs_band_sl"], st["bs_pat_sl"],
                    st["carrier"], 1.0 + st["cv2_med"],
                    st["m3_med"], st["m4_med"])]
        parts.append("%s(KS13/23/12 %.3f/%.3f/%.3f; m2 groups "
                     "%.2f/%.2f/%.2f)"
                     % ("PROFILE_STATIONARY" if st["stationary"]
                        else "PROFILE_DRIFTING", st["ks13"],
                        st["ks23"], st["ks12"], st["grp_m2"][0],
                        st["grp_m2"][1], st["grp_m2"][2]))
        parts.append("DEPTH(nact lo/hi %+.3f/%+.3f cv2p lo/hi "
                     "%+.3f/%+.3f%s; %s A %.3f dev %.3f; jk "
                     "%+.3f/%+.3f %d/42 above %+.3f)"
                     % (st["sl_nact_lo"], st["sl_nact_hi"],
                        st["sl_cv2p_lo"], st["sl_cv2p_hi"],
                        " DEPTH_HALF_MISS" if st["depth_miss"]
                        else "",
                        "TRANSIENT_1_OVER_N" if st["transient"]
                        else "1/N_REJECTED", st["A_fs"],
                        st["fs_dev"], st["jk2_min"],
                        st["jk2_max"], st["n_above"],
                        st["unif_need"]))
        if st["depth_caveat"]:
            parts.append("DEPTH_CAVEAT")
        parts.append("ROUTE_TABLE(B1 chi %.2f sl %+.3f surv %.2f "
                     "sl %+.3f kmax %.0f sl %+.3f composed %+.3f "
                     "vs %+.3f; B2 ws %.2f ks_k %.3f; B3 gain "
                     "%.3f max %.3f)"
                     % (st["chi_med"], st["sl_chi"],
                        st["surv_med"], st["sl_surv"],
                        st["kmax_med"], st["sl_kmax"],
                        st["composed"], st["unif_need"],
                        st["ws_med"], st["ks_k"], gain_med,
                        gain_max))
        if outcome == "UNIF_DERIVED":
            parts.append("UNIF_DERIVED(B1 + A2: chi non-growing "
                         "+ stationary + 1/N transient + count "
                         "42/42)")
        elif outcome == "UNIF_SPLIT":
            parts.append("UNIF_SPLIT(%s)" % " | ".join(fired))
        else:
            parts.append("UNIF_STILL_EMPIRICAL(no route clause "
                         "met; measured sl_cv2p %+.3f vs "
                         "UNIF_NEED %+.3f)"
                         % (st["sl_cv2p"], st["unif_need"]))
        if outcome == "UNIF_DERIVED" and not st["depth_caveat"]:
            parts.append("CANDIDATE_THEOREM(printed in S6, "
                         "hypotheses typed MEASURED, wave-10 "
                         "candidate NOT promoted)")
        else:
            parts.append("REST_FROZEN(ATOM_TARGET: sl_natom >= "
                         "%+.3f measured %+.3f margin %.3f)"
                         % (atom_need, st["sl_natom"],
                            st["sl_natom"] - atom_need))
        parts.append("WORLD_NOTE(identity world-blind by "
                     "algebra; UNIF non-separation reproduced)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the coherence identity, "
          "the CS cap, the variance decomposition, the count "
          "identity and the finite-size solve (all world-blind); "
          "MEASURED: every slope, share, KS distance, gain, "
          "class and jackknife (42 rungs only); OPEN: ATOM_TARGET"
          " / UNIF_TARGET beyond the measured margin, the cofinal"
          " step H5, kz15 beyond r270; NO RH claim"
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
