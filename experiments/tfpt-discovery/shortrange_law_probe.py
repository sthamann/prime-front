#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shortrange_law_probe -- PRIME.PORT.L2.SHORTRANGE_LAW.01 (round
304): the reviewer-mandated SHORT-RANGE LAW round.  r303
(atom_target_probe, 26/26, SPEC 375e9f2b) closed the reduction
cascade r297->r302 as an exact DICTIONARY (REGRESS_CONFIRMED: one
measured core S = sigma* - sl_D = +0.0547; the 1/2-conversion
refuted; sigma* - sigma = S + ratio surplus +0.1429 exact) and
delivered MIXING_INSUFFICIENT with a monotone causal ladder on
1008 sealed synthetic builds: chi 0.630 (real) -> 0.764 (rho_1
matched) -> 1.029 (rho_1 = 0) -> 1.342 (rho_1 flipped); end
margin +0.055 -> +0.057 -> +0.032 -> -0.044 -- the sign flip
KILLS the target inequality; rho_1 matching reproduces the slopes
AND the end margin but misses the destructive coherence LEVEL by
0.134.  The NAMED gap: the within-block / short-range structure
beyond lag 1.  Bycatch: n_eff_atom is a pure MARGINAL functional
(invariance 1e-15); rho_1 < 0 holds on 41/42 rungs only
(Fractions negatives kz18/kz23) -- no raw per-rung theorem.

THE REVIEWER CONTRACT FOR THIS ROUND (binding, quoted): "a single
lag can deceive.  For a cofinal statement you ultimately need
control of the whole correlation sum, roughly 1 + 2 sum_{k>=1}
rho_k.  Even if rho_1 < 0, rho_2, rho_3, ... could be positive
enough to eat the advantage again.  R304 must therefore
additionally adjudicate: is the anti-correlation genuinely
SHORT-RANGE and SUMMABLE?  Ideal would be a theorem candidate
like sum_{k>=1} |rho_k| < C with negative net covariance or
sufficiently fast mixing."  Plus the graduated causal ladder
rho_1 in {+0.2, 0, -0.1, -0.2, -0.3} with slack response (r303
had only three levels).  HARD RULE (r303 adjudication, binding):
a round counts as progress ONLY if it adds NEW information --
not if it re-expresses the same slack in a new coordinate.  This
round introduces NO coordinate change; it tests exclusively the
reviewer-named mechanism object.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE TWO QUESTIONS (both mandatory, sealed order):
(Q1, Leg A FIRST) measure and FREEZE the short-range law on the
real dc profile (all 42 rungs, 3 worlds): the centered lag
profile rho_k for k = 1..16, the truncated net covariance 1 + 2
sum rho_k, the summability sum |rho_k| with tail behavior, the
EXACT lag decomposition of the destructive coherence chi, the
halves stability and the world comparison.  Is the law
short-range (rho_k ~ 0 for k >= k0 small) and stable?
(Q2, Leg B) does the law CLOSE the r303 gap?  Extend the r303
synthetic machinery to lag-k matching: does a family with
rho_1..rho_k0 matched reproduce the chi LEVEL and the end margin
within the sealed bands -- i.e. is the short-range law the
COMPLETE mechanism?

THE OBJECT (r269/r287/r297-r303 machinery imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split; maximal same-sign runs of the bx-sorted bulk; level-2
blocks (r270 convention); the frozen positional block machinery
(r298 WBT), the r299 FDP splits, the r300 DTP.participation +
DTP.shared_delta, the r301 NTP.quasi_uniformity + NTP.dc_profile,
the r302 UTP.coherence_split + UTP.lagk_profile + UTP.ks_two +
UTP.fs_solve, and the r303 ATP.margin_chain + ATP.rho1_stat +
ATP.swap_arrange + ATP.alt_census + ATP.fr_rho1 +
ATP.fr_margin_chain (the audited synthetic machinery -- EXTENDED
to lag k here, not rebuilt), ALL imported verbatim; the round's
central objects are (Q1) the lag profile rho_1..16 of the dc
profile on the shared bulk support and (Q2) the sealed lag-k0
matching family measured through the UNCHANGED r303 pipeline.

DISCLOSED ALGEBRAIC FACTS (derived before any run, no scratch):
(F1) ZERO-SUM TAUTOLOGY: for the MEAN-REMOVED finite profile the
  full lag sum obeys 1 + 2 sum_{k=1}^{n-1} rho_k = 0 EXACTLY
  (because sum zc_i = 0 forces (sum zc_i)^2 = A0 + 2 sum_k S_k =
  0).  The reviewer's net covariance is therefore read as the
  TRUNCATED NC(K) = 1 + 2 sum_{k<=K} rho_k with K = 16 << n
  (~120-900): the short-range content is the PLATEAU of NC(k) by
  a small k0 and the smallness of the per-lag tail -- NOT the
  full sum, which is a tautology; the finite-n per-lag bias is
  about -1/(2(n-1)) ~ -0.004, negligible against RHO_SMALL.
(F2) CHI LAG DECOMPOSITION: on the shared bulk support (blocks
  are runs of consecutive position indices) chi = D/Q = 1 + 2
  sum_{k>=1} T_k / Q EXACT with T_k = sum over within-block
  position pairs at lag k of z_i z_{i+k} (raw values, no
  centering); the per-lag shares c_k = 2 T_k / Q recompose chi
  exactly (live ward on every world).
(F3) WITHIN-BLOCK MATCHING PINS CHI: a family matching all T_k
  reproduces D and chi BY ALGEBRA (and n_eff_atom is marginal,
  r303); the information content of such a diagnostic family is
  in the REMAINING coordinates (CV^2 level and slope) -- typed
  accordingly, disclosed in advance.
(F4) the identity permutation achieves the lag-k0 targets
  exactly; the family therefore starts from seeded random
  permutations and gates the fixed-point share (FIX_MAX).

LEG 0 -- ANCHOR REGRESSION (r297-r303 record numbers adopted
as-is, disclosed): the r297-r302 anchor set exactly as gated in
r303 (sigma -0.714, sigma* -0.516, sl_D -0.571, n_eff/n_act/CV^2/
n_eff_atom/surv/chi/rho/KS/A_fs rows, tolerances unchanged); the
margin chain live: m_D = m_NEFF = m_UNIF = m_ATOM = +0.0547
(MARGIN_REF 0.055 tol 0.01, invariance devs <= PROP_BAR 1e-9)
plus the Fractions re-proof 3/50 x 4; the r303 three-family
ladder REPLICATED with the SAME seeds (SEED_BASE 303000, 8
replicates, bit-identical machinery): chi 0.764 / 1.029 / 1.342
(tol 0.02), end margins +0.057 / +0.032 / -0.044 (tol 0.01),
n_eff_atom invariance <= NA_INV_BAR; RHO_SIGN 41/42 with the
kz18/kz23 Fractions negatives.

LEG A -- THE LAW, MEASURED AND FROZEN (Q1): per rung the centered
lag profile rho_1..16 (module-own lag_stats, gated ==
UTP.lagk_profile on k <= 8 at LAG_CONS_BAR); ladder MEDIAN per k
with IQR bands; the zero-sum tautology as a live ward (F1, ZS_BAR
on every rung); k0 = the SMALLEST k in [1, K0_MAX = 8] such that
|med rho_j| <= RHO_SMALL = 0.05 for ALL j in (k, 16]; tail sum
sum_{j>k0} |med rho_j| and the sealed bar TAIL_MAX = 0.15;
truncated net covariance NC(k0) and NC(16) with the sealed bar
NC(16) < NC_MAX = 1.0 (net-NEGATIVE correlation sum, the
reviewer's sign condition); summability SUM(16) = sum |med
rho_k|; halves stability (first 21 vs last 21 rungs by N: per-k
medians, sign agreement on k <= 3 -- anti-extrapolation honesty,
census); world comparison (EPST / SCR lag profiles, census: is
the law world-specific or generic?); the exact chi lag
decomposition c_k = 2 T_k / Q per rung (F2, recomposition ward <=
DEC_BAR on every non-degenerate world).  SEALED FINE TYPE
(exactly one fires): SHORTRANGE_LAW(k0, NC, SUM) iff k0 exists
AND tail sum <= TAIL_MAX AND NC(16) < NC_MAX;
LONGRANGE_STRUCTURE otherwise.  DISCLOSED PRIOR: the r302 medians
rho_1/2/3 = -0.222/-0.140/+0.089 force k0 >= 3 if the rule fires
at all; rho_4..16, the tail and the stability are genuinely open.

LEG B -- THE SUFFICIENCY TEST (Q2): sealed families on the same
per-rung bulk profiles, marginal preserved BITWISE (permutation),
measured through the UNCHANGED r303 pipeline (UTP.coherence_split
-> chi med over rungs, sl_cv2p + sl_D via L2D.halves_slope, end
margin margin_syn = sigma* - sl_D_syn; family value = median over
replicates, min/max printed):
(a) LAGK_MATCH: rho_1..k0 steered JOINTLY to the rung's measured
  values (module-own swap_arrange_k: seeded greedy pairwise
  swaps, L2 objective on the lag vector, O(k0) local update,
  deterministic restarts; convergence max_k |rho_k - target_k|
  <= RHO_TOL_K = 0.02 on the recomputed best arrangement, share
  >= CONV_MIN_K = 0.90 over all builds), R_REP_K = 6 replicates
  per rung, seeds seed = SEED_BASE_K + rung_index x 100 + family
  x 10 + replicate (SEED_BASE_K 314000; disjoint from the r303
  range [303000, 307128), gated collision-free globally);
  fixed-point share <= FIX_MAX (F4); n_eff_atom invariance <=
  NA_INV_BAR; ALSO measured: the family's own c_k decomposition
  (does global lag matching move the within-block terms?);
(b) the r303 REPLICATION (RHO_MATCH / RHO_ZERO / RHO_FLIP, 8
  replicates, SEED_BASE 303000) as the bit-anchor (Leg 0) AND
  the rho_1-only column of the sufficiency table;
(c) GRADUATED LADDER (reviewer wish): ABSOLUTE rho_1 targets
  {+0.2, 0.0, -0.1, -0.2, -0.3} via the UNCHANGED r303
  ATP.swap_arrange (tol RHO_TOL = 0.01, share >= CONV_MIN =
  0.95), R_REP_G = 4 replicates per rung and level; the SLACK
  RESPONSE table (level -> chi, sl_cv2p, sl_D, end margin,
  margin - margin_real) with the monotonicity census (chi
  increasing in rho_1, margin decreasing -- r303 direction).
CHI-GAP ATTRIBUTION: med c_k real vs med c_k of the
rho_1-matched r303 family per k (which lag range carries the
0.134 chi-level miss?), summed over k <= 3 / 4..8 / 9..16 / >16.
SEALED REPRODUCTION RULE (r303 bands, unchanged): family F
reproduces MAIN iff |chi_F - chi| <= CHI_BAND = 0.05 AND
|sl_cv2p_F - sl_cv2p| <= SLP_BAND = 0.02 AND |sl_D_F - sl_D| <=
SLP_BAND.  SEALED ADJUDICATION (exactly one fires):
LAW_LONGRANGE iff Leg A returned LONGRANGE_STRUCTURE (the
reviewer stop case); else LAW_SUFFICIENT iff family (a)
reproduces all three quantities -- then the short-range law IS
the complete mechanism and the lane's proof goal is printed;
else LAW_INSUFFICIENT(rest named per family x quantity).
DISCLOSED PRIORS: whether lag-k0 matching closes the chi level is
genuinely OPEN (r303 showed lag-1 alone leaves 0.134); the
graduated ladder direction is expected monotone per r303 but the
intermediate levels are new measurements; outcomes sealed
symmetrically.

LEG C -- CONSEQUENCE (sealed map, printed after A x B):
(i) LAW_SUFFICIENT => print the lane's final proof goal VERBATIM:
  "SHORTRANGE_GOAL: derive the short-range law (the rho profile
  up to k0, net covariance <= c < 1) from the three-term
  recursion + the stationary limit distribution" -- plus the
  exact mini-test: Fractions-EXACT signs of S_k, k = 1..4, on
  the TWO smallest rungs vs the ladder median sign pattern
  (measurement / exact finite certificates only, NO derivation
  claimed);
(ii) LAW_INSUFFICIENT => name the rest precisely (which quantity
  misses) and run ONE targeted diagnostic: the WITHIN-BLOCK
  MATCH family (T_1..T_k0 steered to the rung's values,
  module-own swap_arrange_wb, R_REP_D = 4, convergence |c_k -
  target| <= C_TOL = 0.02 share >= CONV_MIN_K; chi and D pinned
  BY ALGEBRA -- F3 disclosed; the readout is whether the CV^2
  level/slope and the m_UNIF-side follow): if it reproduces, the
  rest is the BLOCK-CONDITIONAL pair placement (the global lag
  law alone under-determines the within-block terms); if not,
  the rest is beyond-pair structure (higher moments / triplet
  placement of the pair distribution);
(iii) LAW_LONGRANGE => document the stop state (the reviewer stop
  case: the lane closes; L2 <=> anti-concentration of an
  explicit block field with LONG-RANGE structure, honest).
The sign-pattern mini-census (i) is measured in EVERY branch
(cheap, honest); it is adjudicated as the lane goal's first
evidence only under LAW_SUFFICIENT.

LEG D -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) NET COVARIANCE WITH FACTOR 1 INSTEAD OF 2 (exact Fractions,
  module-own): on the toy (1,-1,1,-1) the exact lag profile is
  rho = (-3/4, +1/2, -1/4) and the full sum obeys 1 + 2(-1/2) =
  0 EXACT (the F1 tautology); the factor-1 mutant gives 1/2 != 0
  EXACT -- CAUGHT; the same factor mutant on the chi
  decomposition toy (1,-2|3) gives 6/7 instead of chi = 5/7
  (break 1/7 EXACT) -- the factor 2 on the cross terms is
  load-bearing on BOTH identities;
(m2) LAG MATCHING WITHOUT MARGINAL PRESERVATION: the constant-
  |value| two-sign profile with the same L1a must break the
  construction LOUDLY: sorted-multiset ward fails AND the atom
  energy deviates rel >= MUT_MIN (r303 m2 adopted);
(m3) RHO PROFILE ON THE UNNORMALIZED FIELD: on the toy (2,0,2,0)
  the uncentered ratio sum z_i z_{i+1} / sum z_i^2 gives 0 vs
  the centered -3/4, break 3/4 EXACT (Fractions) -- CAUGHT; on
  the real w9 profile the uncentered lag-1 ratio deviates from
  the centered one by >= MUT_MIN -- the centering is
  load-bearing;
(m4) FAMILY SMUGGLE: a rho_1-only-matched build (the r303 (a)
  construction, fixed disclosed seed M4_SEED) fed to the lag-k0
  ward must FAIL the per-lag ward on the lag set 1..max(k0, 3)
  (max dev > RHO_TOL_K) -- CAUGHT: the lag-k0 ward separates the
  r303-(a) family from the Leg B (a) family; a sufficiency
  verdict cannot be smuggled with the weaker family;
(m5a/m5b) WORLD-BLINDNESS BREAK: the r303 scope mutants (a
  builder consuming the withheld terminal drive key / the branch
  label) are both FLAGGED by the AST scope audit.  Scope
  hygiene: the new builders (lag_stats, net_cov, chi_lag_terms,
  swap_arrange_k, swap_arrange_wb, lagk_ward) consume profile
  values / positions / block indices only (BOUND_FORBIDDEN set);
  fragment audit (no fit primitives; both swap searches are
  deterministic seeded greedy descents, disclosed).  TOY
  EXACTNESS (bar 1e-14): lag_stats on (1,-1,1,-1) ==
  (-3/4, +1/2, -1/4) EXACT (float == Fractions); net_cov float
  == Fractions on the toy; swap_arrange_k on the 4-toy
  (-1,-1,1,1) hits the achievable pair (-3/4, +1/2) EXACTLY with
  the multiset preserved bitwise; the chi decomposition toy ==
  5/7 EXACT; the DEGENERATE-SOURCE GUARD as r303 (SMOOTH,
  pre-declared: shared-support wards skipped iff W <= 1e-6 x the
  total contribution mass, disclosed per world).

INDEX FIREWALL (binding, r238-r303 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks, r299 FDP.overlap_split +
FDP.cconv_census, r300 DTP.participation + DTP.shared_delta,
r301 NTP.quasi_uniformity + NTP.dc_profile, r302
UTP.coherence_split + UTP.lagk_profile + UTP.ks_two +
UTP.fs_solve, r303 ATP.margin_chain + ATP.rho1_stat +
ATP.swap_arrange + ATP.alt_census + ATP.fr_rho1 +
ATP.fr_margin_chain, r269 PBB.mask_edge + PBB.runs_split +
PBB.bound_pairsum + PBB.mp_drive, r287 L2D.blocks_level2 +
L2D.bound_vdc + L2D.halves_slope + L2D.autocorr_full, r244
BH.wpack, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.
B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor,
never fitted).  COFINAL LADDER (pre-sealed): frame-A h <= 900,
42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38,
39, 52}.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN);
PROP_BAR 1e-9; QID_BAR 1e-9; CO_BAR 1e-9; CSK_BAR 1e-9; EQ_BAR
1e-9; NA_BAR 1e-12; NA_INV_BAR 1e-12; RHO_CONS_BAR 1e-12;
LAG_CONS_BAR 1e-12; DEC_BAR 1e-12; ZS_BAR 1e-9; DEG_FLOOR 1e-6;
REC_FLOOR 1e-6; R_REP 8; SEED_BASE 303000; RHO_TOL 0.01; SWAP_F
40; SWAP_CAP 60000; CONV_MIN 0.95; FIX_MAX 0.2; CHI_BAND 0.05;
SLP_BAND 0.02; MISS_F 2.0; K_LAG 8; N_GRP 14; KS_STAT 0.125;
FS_BAR 0.05; TOY_BAR 1e-14; MUT_MIN 1e-6; K_FULL 16; RHO_SMALL
0.05; K0_MIN 1; K0_MAX 8; TAIL_MAX 0.15; NC_MAX 1.0; RHO_TOL_K
0.02; CONV_MIN_K 0.90; R_REP_K 6; R_REP_G 4; R_REP_D 4;
GRAD_LEVELS (+0.2, 0.0, -0.1, -0.2, -0.3); SEED_BASE_K 314000;
SWAP_F_K 120; SWAP_CAP_K 120000; C_TOL 0.02; M4_SEED 999001
(disclosed, outside every family range); TB_WARD bars 1e-9 /
3e-6 / 1e-6; ID_BAR 1e-12; AC_BAR 1e-9; R297 anchors sigma
-0.714 / sigma* -0.516 / sl_c2 +0.196 / sl_pref +0.489 (tol
0.01); R299 sl_D -0.571 (tol 0.01); R300 anchors n_eff 37.41
(0.05) / sl_neff +0.963 / sl_L1 +0.196 (tol 0.01); R301 anchors
n_act 73.0 (0.5) / sl_nact +1.002 / cv2 1.03 (0.02) / sl_cv2p
+0.039 / natom 118.0 (1.0) / sl_natom +0.942 / surv 0.44 (0.02) /
sl_surv -0.020 (tol 0.01); R302 anchors chi 0.630 (0.02) / sl_chi
-0.060 (0.01) / rho1/2/3 -0.222/-0.140/+0.089 (0.01) / KS13 0.043
/ KS23 0.021 (0.01) / A_fs 1.973 (0.01) / fs_dev <= 0.05;
MARGIN_REF 0.055 (tol 0.01); R303 family anchors chi_A 0.764 /
chi_B 1.029 / chi_C 1.342 (tol 0.02), margins mA +0.057 / mB
+0.032 / mC -0.044 (tol 0.01), RHO_SIGN 41/42, alt med 0.523
(tol 0.02); MP_DPS 60; MP_T_BAR 1e-8; MP_DEEP_BAR 3e-6; KZ_ANCHOR
15; runtime <= 1800 s; smoke = w9 + controls + Fractions section
+ toys + scope audits + every exact ward at w9 + ONE lag-k build
(w9, k = 3, rep 0) + the m2/m3/m4 mutants (ladder, slopes,
families, adjudications, censuses, mp wards skipped).
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r297-r303 RECORD number adopted as-is;
the F1-F4 facts are derived algebra, disclosed above; the k0
rule, the bands and the adjudication outcomes are sealed
symmetrically -- the Leg A tail (rho_4..16), the stability and
the Leg B sufficiency are genuinely open; no rule was chosen to
favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  LAG_PROFILE(med rho_1..8 + NC(k0)/NC(16) + SUM(16) + tail)
+ [exactly one of] SHORTRANGE_LAW(k0, NC, SUM) /
    LONGRANGE_STRUCTURE
+ CHI_GAP(lag attribution real vs rho_1-matched, by range)
+ LAGK_TABLE(chi / sl_cv2p / sl_D / margin, replicate min..max;
    natom-invariance ward; own c_k decomposition)
+ [exactly one of] LAW_SUFFICIENT / LAW_INSUFFICIENT(rest named)
    / LAW_LONGRANGE
+ SLACK_RESPONSE(5-level graduated table + monotonicity census)
+ SIGN_PATTERN(Fractions census, two smallest rungs vs ladder)
+ CONSEQUENCE(the sealed Leg C map)
+ [if a control class differs] WORLD_NOTE(disclosed).
Honesty before beauty: the zero-sum tautology, the chi lag
decomposition, the margin chain and every Fractions statement are
EXACT finite statements; every med, band, slope, census and
family comparison is MEASURED on 42 rungs and seeded replicates
only; the synthetic families falsify or fail to falsify a
MECHANISM CANDIDATE -- no verdict claims a derivation of the law,
no verdict claims a cofinal statement; the exception scalar's
positivity beyond the measured 42 stays OPEN; r243-r303 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 crashed at the G32 print (a MISSING FORMAT ARGUMENT
in the gate detail string -- print-layer only, fixed BEFORE any
full evaluation, no bar/band/rule touched); smoke pass 2 = 32/32
(0.3 s, no defect); calibration pass 1 = first full evaluation,
37/37 gates, wall 55.4 s, NO amendment (every sealed rule fired
as written; every construction ward held: r303 replication
1008/1008 converged with the chi ladder and margins bit-near,
LAGK 252/252 at tol 0.02 with k0_eff = 8 fallback, graduated
840/840, seeds 2100 collision-free; the pre-declared DEG guard
fired on SMOOTH only); record run1/run2 after this insertion,
identical up to WALL; the only post-freeze edit is this
record-table insertion, which IS the protocol):
CAL_VERDICT = LAG_PROFILE(med rho_1..16 = -0.222 / -0.140 /
+0.089 / +0.130 / -0.028 / -0.149 / +0.021 / +0.164 / -0.011 /
-0.144 / +0.009 / +0.133 / -0.009 / -0.152 / +0.017 / +0.147 --
a STABLE PERIOD-4 COMB (strong lags at k = 4m and 4m + 2, signs
-, +), NOT a decaying tail; NC(1) 0.556 NC(2) 0.277 NC(4) 0.715
NC(8) 0.731 NC(16) 0.712 < 1: the reviewer's NET-NEGATIVITY
condition HOLDS; SUM(16) 1.563; halves sign agreement 3/3, max
half-dev 0.077 -- the comb is stable along the ladder) +
LONGRANGE_STRUCTURE(k0 NONE <= 8: |med rho_j| > 0.05 recurs at
every j in {4m, 4m + 2} up to 16 -- the sealed short-range rule
FAILS on the letter; the summability-with-small-tail half of the
reviewer condition is REFUTED on the global profile while the
net-covariance half HOLDS) + CHI_GAP(the r303 chi-level miss
0.134 lives at k <= 3: d c_1 +0.045, d c_2 +0.181, d c_3 -0.068;
range sums k <= 3 +0.158 / 4..8 -0.002 / 9..16 0.000 / >16
0.000; the real WITHIN-BLOCK shares die out by k ~ 4 (c_1
-0.345, c_2 -0.139, c_3 +0.068, c_4 +0.028, sum(5..16) -0.026,
tail(>16) 0.000): the chi-relevant structure IS short-range --
the long-range comb lives in the GLOBAL profile only, invisible
to chi) + LAGK_TABLE(k0_eff = 8: chi 0.652 [0.631, 0.660] -- the
destructive chi LEVEL now REPRODUCES (|d| 0.022 <= 0.05; the
r303 rho_1-only family missed by 0.134); sl_cv2p +0.068 misses
by 0.028, sl_D -0.598 misses by 0.027 (both > 0.02), margin
+0.082: matching 8 lags fixes the LEVEL and slightly breaks the
SLOPES -- the exact complement of r303 (a); the mechanism has
TWO scales: level from the short lags, slopes from the rung-wise
lag-1 trend) + LAW_LONGRANGE(the sealed stop case fires: no
family verdict can override the Leg A type) +
SLACK_RESPONSE(rho_1 = +0.2 / 0.0 / -0.1 / -0.2 / -0.3: chi
1.361 / 1.019 / 0.889 / 0.765 / 0.632 MONOTONE in rho_1; margin
+0.036 / +0.074 / +0.019 / +0.045 / +0.059 NOT monotone --
HONEST NEGATIVE: absolute-level targets leave the margin noisy
positive at 4 replicates; the r303 kill (-0.044) came from
PER-RUNG flipped targets, not from an absolute level: the margin
responds to the rung-wise TREND of rho_1, not to its level) +
SIGN_PATTERN(ladder med signs S_1..4 = -/-/+/+; Fractions-EXACT
on kz18 (N 142) -/-/+/+ and kz23 (N 149) -/-/+/+ -- 4/4 match on
both smallest rungs) + CONSEQUENCE((iii) the reviewer stop case
on the LETTER of the sealed rule -- the lane closes on the
global-profile route: L2 <=> anti-concentration of an explicit
block field with LONG-RANGE (period-4 comb) structure; the
honest FULL reading below) + WORLD_NOTE(the comb is
WORLD-SPECIFIC: EPST rho_1..4 -0.34/+0.01/+0.05/-0.13, SCR
-0.05/+0.15/+0.02/-0.08 vs MAIN -0.22/-0.14/+0.09/+0.13;
identity wards world-blind by algebra; SMOOTH degenerate,
pre-declared).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep
/ 2.4e-8 controls; identity wards on 47 worlds: count 6.8e-16,
coherence 6.0e-16, CS slack 0.0, P_shared == P_ov 6.1e-16, CV^2
equality 8.1e-16, natom internal 4.9e-16, dc == dw x f 2.6e-15,
rho1_stat == lagk 1.1e-16; r297-r302 anchors bit-near (sigma
-0.714, sigma* -0.516, sl_D -0.571, n_eff 37.41/+0.963, n_act
73.0/+1.002 link 42/42, cv2 1.03/+0.039, natom 118.0/+0.942,
surv 0.44/-0.020, chi 0.630/-0.060, rho -0.222/-0.140/+0.089,
KS 0.043/0.021, A_fs 1.973 dev 0.002).  S3: netcov toy 0 EXACT
(m1 mutant 1/2 EXACT), chi decomposition toy 5/7 EXACT (factor-1
mutant 6/7), margin chain 3/50 x 4 devs 0, uncentered toy break
3/4 EXACT, toys float == Fractions worst 0.0.  S4: margin chain
live +0.0547 x 4, invariance devs <= 8.7e-16; RHO_SIGN 41/42,
alternation med 0.523; lag_stats == lagk worst 1.1e-16; zero-sum
live 3.5e-15; F2 recomposition worst 4.7e-16.  S5: replication
worst |rho1 - target| 1.00e-2 at tol, fixed points max 0.029,
natom invariance 1.0e-15 over all 2100 builds, LAGK worst max_k
dev 0.020 at tol; m2 sorted ward BREAKS + atom energy dev
5.9e-1 LOUD; m3 real-w9 dev 0.028 CAUGHT; m4 smuggle dev 0.332
> 0.02 CAUGHT.  S8: mp wards kz15 2.9e-10, kz64 9.3e-9, kz52
6.6e-8.
READING (typed, no upgrade): the round answers the reviewer's
question with a MEASURED SPLIT VERDICT that is genuinely NEW
information (no coordinate change): (1) the global lag law of
the dc profile is NOT a decaying short-range law -- it is a
STABLE PERIOD-4 COMB (strong alternating lags at k = 4m, 4m + 2
up to 16, halves-stable, world-specific); the sealed rule
therefore fires LONGRANGE_STRUCTURE and the reviewer's stop case
LAW_LONGRANGE stands for the GLOBAL-profile route; (2) BOTH
halves of the reviewer condition were adjudicated separately and
split: the net-covariance condition HOLDS (NC(16) = 0.712 < 1,
net-negative) while summability-with-small-tail FAILS; (3) the
chi-relevant structure IS short-range: the exact decomposition
chi = 1 + 2 sum T_k/Q (F2, ward 4.7e-16) shows the within-block
shares die out by k ~ 4 and attributes the r303 miss 0.134 to
k <= 3 (dominated by lag 2: +0.181) -- the long-range comb is
INVISIBLE to chi; (4) matching rho_1..8 closes the chi level
(0.652 vs 0.630, |d| 0.022 <= 0.05) at the price of the slopes
(sl_cv2p/sl_D miss by 0.028/0.027 > 0.02) -- the exact
complement of the r303 rho_1-only family: the mechanism is
TWO-SCALE (level from short lags, slopes from the rung-wise
lag-1 trend); no single lag-matching family reproduces BOTH
within the sealed bands; (5) the graduated reviewer ladder is
monotone in chi but NOT in the margin (honest negative:
absolute-level targets do not kill the inequality; the r303
kill came from per-rung flipped targets -- the margin responds
to the rung-wise trend, not the level); (6) the sign pattern
-/-/+/+ of S_1..4 carries exact-finite Fractions certificates
on both smallest rungs.  CONSEQUENCE ((iii)): the lane's
global-profile mixing route is CLOSED (documented stop, the
reviewer case); what survives as honest structure: the exact
within-block short-range decomposition of chi, the two-scale
mechanism split, the net-negativity NC < 1 and the exact sign
pattern -- typed MEASURED, no proof target is claimed on the
closed route.
Runtime 55.4 s full / 0.3 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE (record-table insertion per
protocol; the pre-record G32 print fix disclosed above; no bar,
band, rule or verdict rule moved).

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
import unif_target_probe as UTP                # noqa: E402 r302
import atom_target_probe as ATP                # noqa: E402 r303
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
CO_BAR = 1e-9
CSK_BAR = 1e-9
EQ_BAR = 1e-9
NA_BAR = 1e-12
PROP_BAR = 1e-9
NA_INV_BAR = 1e-12
RHO_CONS_BAR = 1e-12
LAG_CONS_BAR = 1e-12
DEC_BAR = 1e-12
ZS_BAR = 1e-9
DEG_FLOOR = 1e-6
REC_FLOOR = 1e-6
R_REP = 8
SEED_BASE = 303000
RHO_TOL = 0.01
SWAP_F = 40
SWAP_CAP = 60000
CONV_MIN = 0.95
FIX_MAX = 0.2
CHI_BAND = 0.05
SLP_BAND = 0.02
MISS_F = 2.0
K_LAG = 8
N_GRP = 14
KS_STAT = 0.125
FS_BAR = 0.05
TOY_BAR = 1e-14
MUT_MIN = 1e-6
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
K_FULL = 16
RHO_SMALL = 0.05
K0_MIN = 1
K0_MAX = 8
TAIL_MAX = 0.15
NC_MAX = 1.0
RHO_TOL_K = 0.02
CONV_MIN_K = 0.90
R_REP_K = 6
R_REP_G = 4
R_REP_D = 4
GRAD_LEVELS = ((0.2, "P02"), (0.0, "Z00"), (-0.1, "M01"),
               (-0.2, "M02"), (-0.3, "M03"))
SEED_BASE_K = 314000
SWAP_F_K = 120
SWAP_CAP_K = 120000
C_TOL = 0.02
M4_SEED = 999001
R297_SIGMA = -0.714
R297_SIGMA_STAR = -0.516
R297_SL_C2 = 0.196
R297_SL_PREF = 0.489
R297_TOL = 0.01
R299_SL_D = -0.571
R299_SL_D_TOL = 0.01
R300_NEFF_MED = 37.41
R300_NEFF_TOL = 0.05
R300_SL_NEFF = 0.963
R300_SL_L1 = 0.196
R300_SL_TOL = 0.01
R301_NACT_MED = 73.0
R301_NACT_TOL = 0.5
R301_SL_NACT = 1.002
R301_CV2_MED = 1.03
R301_CV2_TOL = 0.02
R301_SL_CV2P = 0.039
R301_NATOM_MED = 118.0
R301_NATOM_TOL = 1.0
R301_SL_NATOM = 0.942
R301_SURV_MED = 0.44
R301_SURV_TOL = 0.02
R301_SL_SURV = -0.020
R301_SL_TOL = 0.01
R302_CHI_MED = 0.630
R302_CHI_TOL = 0.02
R302_SL_CHI = -0.060
R302_RHO = (-0.222, -0.140, 0.089)
R302_RHO_TOL = 0.01
R302_KS13 = 0.043
R302_KS23 = 0.021
R302_KS_TOL = 0.01
R302_A_FS = 1.973
R302_A_TOL = 0.01
R302_UNIF_NEED = 0.094
R302_ATOM_NEED = 0.888
R302_NEED_TOL = 0.01
MARGIN_REF = 0.055
MARGIN_TOL = 0.01
R303_FAM_CHI = {"A_RHO_MATCH": 0.764, "B_RHO_ZERO": 1.029,
                "C_RHO_FLIP": 1.342}
R303_FAM_MARGIN = {"A_RHO_MATCH": 0.057, "B_RHO_ZERO": 0.032,
                   "C_RHO_FLIP": -0.044}
R303_FAM_CHI_TOL = 0.02
R303_FAM_MARGIN_TOL = 0.01
R303_NNEG = 41
R303_ALT_MED = 0.523
R303_ALT_TOL = 0.02
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


# ---------------- the module-own Leg A / Leg B builders.
# ---------------- Source-pure: profile values, positions and block
# ---------------- indices only; the withheld terminal drive key,
# ---------------- the branch label and every target-side identifier
# ---------------- are forbidden in scope (AST audit).
def lag_stats(z, K):
    """the centered lag-1..K autocovariances of a profile in
    position order: (r vector, S vector, A0) with S_k = sum
    zc_i zc_{i+k}, A0 = sum zc_i^2, r_k = S_k / A0 (module-own;
    gated == UTP.lagk_profile on k <= K_LAG)."""
    z = np.asarray(z, dtype=float)
    n = len(z)
    if n < 2:
        return np.zeros(K), np.zeros(K), 0.0
    zc = z - float(np.mean(z))
    A0 = float(np.dot(zc, zc))
    if A0 <= 0.0:
        return np.zeros(K), np.zeros(K), A0
    S = np.array([float(np.dot(zc[:-k], zc[k:])) if k < n else 0.0
                  for k in range(1, K + 1)])
    return S / A0, S, A0


def net_cov(rvec, K=None, fac=2):
    """the truncated net covariance NC(K) = 1 + fac x sum_{k<=K}
    r_k (fac = 2 sealed; fac = 1 is the m1 mutant).  Works on
    floats AND exact Fractions."""
    rl = list(rvec)
    if K is None:
        K = len(rl)
    return 1 + fac * sum(rl[:K])


def fr_lag_stats(vals, K):
    """exact Fractions lag-1..K statistics of a profile (Fraction
    arithmetic on the float inputs is exact)."""
    zf = [Fr(float(v)) for v in vals]
    n = len(zf)
    mu = sum(zf) / n
    zc = [v - mu for v in zf]
    A0 = sum(v * v for v in zc)
    S = [sum(zc[i] * zc[i + k] for i in range(n - k))
         if k < n else Fr(0) for k in range(1, K + 1)]
    if A0 == 0:
        return [Fr(0)] * K, S, A0
    return [s / A0 for s in S], S, A0


def chi_lag_terms(z, jb):
    """the EXACT lag decomposition of the coherence ratio on the
    shared bulk support (F2): with block sums P_j over the block
    index jb (non-decreasing: blocks are runs of consecutive
    indices), D = Q + 2 sum_{k>=1} T_k with T_k = sum_{i: jb_i ==
    jb_{i+k}} z_i z_{i+k} (raw values); the recomposed ratio 1 +
    2 sum T_k / Q equals D/Q EXACTLY.  Returns (T list up to the
    maximal in-block lag, Q, recomposed ratio)."""
    z = np.asarray(z, dtype=float)
    jb = np.asarray(jb)
    n = len(z)
    Q = float(np.dot(z, z))
    T = []
    k = 1
    while k < n:
        eq = jb[:-k] == jb[k:]
        if not np.any(eq):
            break
        T.append(float(np.dot(z[:-k][eq], z[k:][eq])))
        k += 1
    ratio = 1.0 + 2.0 * sum(T) / max(Q, 1e-300)
    return T, Q, ratio


def swap_arrange_k(z, tvec, seed, cap, tol):
    """the multi-lag extension of the r303 swap construction: a
    permutation of the profile values with the lag-1..K0
    autocovariance vector steered JOINTLY to the target vector by
    seeded greedy pairwise swaps (L2 objective on the lag vector,
    O(K0) local update, strict improvement, deterministic restarts
    after 5n non-improving attempts; the best arrangement is
    kept).  Returns (values in arrangement order, permutation,
    r vector recomputed on the best arrangement, attempts,
    converged)."""
    z = np.asarray(z, dtype=float)
    n = len(z)
    K0 = len(tvec)
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    zc_full = z - float(np.mean(z))
    A0 = float(np.dot(zc_full, zc_full))
    if n < 4 or A0 <= 0.0:
        return z[perm], perm, np.zeros(K0), 0, True
    y = list(zc_full[perm])
    St = [float(t) * A0 for t in tvec]
    tol_abs = tol * A0

    def s_full(yl):
        return [sum(yl[i] * yl[i + k] for i in range(n - k))
                if k < n else 0.0 for k in range(1, K0 + 1)]

    def dsum(k, p, q):
        s = 0.0
        i = p - k
        if i >= 0:
            s += y[i] * y[i + k]
        if p + k < n:
            s += y[p] * y[p + k]
        i = q - k
        if i >= 0 and i != p and i != p - k:
            s += y[i] * y[i + k]
        if q + k < n:
            s += y[q] * y[q + k]
        return s

    Sv = s_full(y)
    err = sum((Sv[j] - St[j]) ** 2 for j in range(K0))
    best_perm = perm.copy()
    best_dev = max(abs(Sv[j] - St[j]) for j in range(K0))
    best_err = err
    pairs = rng.integers(0, n, size=(int(cap), 2))
    since = 0
    att = 0
    for p, q in pairs:
        att += 1
        if best_dev <= tol_abs:
            break
        if p == q:
            continue
        if p > q:
            p, q = q, p
        old = [dsum(k, p, q) for k in range(1, K0 + 1)]
        y[p], y[q] = y[q], y[p]
        new = [dsum(k, p, q) for k in range(1, K0 + 1)]
        S2 = [Sv[j] + new[j] - old[j] for j in range(K0)]
        e2 = sum((S2[j] - St[j]) ** 2 for j in range(K0))
        if e2 < err:
            Sv = S2
            err = e2
            perm[p], perm[q] = perm[q], perm[p]
            if err < best_err:
                best_err = err
                best_perm = perm.copy()
                best_dev = max(abs(Sv[j] - St[j])
                               for j in range(K0))
            since = 0
        else:
            y[p], y[q] = y[q], y[p]
            since += 1
            if since >= 5 * n:
                perm = rng.permutation(n)
                y = list(zc_full[perm])
                Sv = s_full(y)
                err = sum((Sv[j] - St[j]) ** 2 for j in range(K0))
                if err < best_err:
                    best_err = err
                    best_perm = perm.copy()
                    best_dev = max(abs(Sv[j] - St[j])
                                   for j in range(K0))
                since = 0
    yb = zc_full[best_perm]
    Sb = [float(np.dot(yb[:-k], yb[k:])) if k < n else 0.0
          for k in range(1, K0 + 1)]
    rr = np.array(Sb) / A0
    conv = bool(np.max(np.abs(rr - np.asarray(tvec, float)))
                <= tol)
    return z[best_perm], best_perm, rr, att, conv


def swap_arrange_wb(z, jb, t_T, seed, cap, tol_abs):
    """the within-block diagnostic construction (Leg C (ii), F3
    disclosed): a permutation of the RAW profile values with the
    within-block lag cross sums T_1..K0 (pairs with equal block
    index jb; jb FIXED, values permuted) steered to the target
    vector by seeded greedy pairwise swaps (L2 objective, strict
    improvement, deterministic restarts).  Returns (values,
    permutation, T vector recomputed, attempts, converged with
    max_k |T_k - target| <= tol_abs)."""
    z = np.asarray(z, dtype=float)
    jb = list(np.asarray(jb))
    n = len(z)
    K0 = len(t_T)
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    if n < 4:
        return z[perm], perm, np.zeros(K0), 0, True
    y = list(z[perm])
    St = [float(t) for t in t_T]

    def t_full(yl):
        out = []
        for k in range(1, K0 + 1):
            tot = 0.0
            for i in range(n - k):
                if jb[i] == jb[i + k]:
                    tot += yl[i] * yl[i + k]
            out.append(tot)
        return out

    def dsum(k, p, q):
        s = 0.0
        i = p - k
        if i >= 0 and jb[i] == jb[i + k]:
            s += y[i] * y[i + k]
        if p + k < n and jb[p] == jb[p + k]:
            s += y[p] * y[p + k]
        i = q - k
        if i >= 0 and i != p and i != p - k and jb[i] == jb[i + k]:
            s += y[i] * y[i + k]
        if q + k < n and jb[q] == jb[q + k]:
            s += y[q] * y[q + k]
        return s

    Sv = t_full(y)
    err = sum((Sv[j] - St[j]) ** 2 for j in range(K0))
    best_perm = perm.copy()
    best_dev = max(abs(Sv[j] - St[j]) for j in range(K0))
    best_err = err
    pairs = rng.integers(0, n, size=(int(cap), 2))
    since = 0
    att = 0
    for p, q in pairs:
        att += 1
        if best_dev <= tol_abs:
            break
        if p == q:
            continue
        if p > q:
            p, q = q, p
        old = [dsum(k, p, q) for k in range(1, K0 + 1)]
        y[p], y[q] = y[q], y[p]
        new = [dsum(k, p, q) for k in range(1, K0 + 1)]
        S2 = [Sv[j] + new[j] - old[j] for j in range(K0)]
        e2 = sum((S2[j] - St[j]) ** 2 for j in range(K0))
        if e2 < err:
            Sv = S2
            err = e2
            perm[p], perm[q] = perm[q], perm[p]
            if err < best_err:
                best_err = err
                best_perm = perm.copy()
                best_dev = max(abs(Sv[j] - St[j])
                               for j in range(K0))
            since = 0
        else:
            y[p], y[q] = y[q], y[p]
            since += 1
            if since >= 5 * n:
                perm = rng.permutation(n)
                y = list(z[perm])
                Sv = t_full(y)
                err = sum((Sv[j] - St[j]) ** 2 for j in range(K0))
                if err < best_err:
                    best_err = err
                    best_perm = perm.copy()
                    best_dev = max(abs(Sv[j] - St[j])
                                   for j in range(K0))
                since = 0
    yl = list(z[best_perm])
    y = yl
    Sb = t_full(yl)
    dev = max(abs(Sb[j] - St[j]) for j in range(K0))
    return (z[best_perm], best_perm, np.array(Sb), att,
            dev <= tol_abs)


def lagk_ward(z_arr, tvec, tol):
    """the family separation ward (single source for the
    construction gate and the m4 smuggle catch): max_k |r_k(z) -
    target_k| <= tol on the measured centered profile.  Returns
    (ok, dev)."""
    rr, _S, _A0 = lag_stats(z_arr, len(tvec))
    dev = float(np.max(np.abs(rr - np.asarray(tvec, float))))
    return dev <= tol, dev


def mutant_gift_bound(rc, vals):
    """m5a MUST-FAIL MUTANT: a 'lag target' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * lag_stats(vals, 1)[0][0]


def mutant_branch_peek(rc, vals):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'profile statistic' that consumes the branch label to pick
    its constant -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * net_cov(lag_stats(vals, 4)[0])


# ---------------- exact Fractions section
def fr_netcov_toy(fac=2):
    """the m1 Fractions re-proof on the toy (1,-1,1,-1): the exact
    lag profile is (-3/4, +1/2, -1/4); the FULL net covariance
    1 + 2 sum r_k = 0 EXACT (the F1 zero-sum tautology); the
    fac = 1 mutant gives 1/2 EXACT -- CAUGHT."""
    rl, _S, _A0 = fr_lag_stats([1.0, -1.0, 1.0, -1.0], 3)
    return rl, net_cov(rl, fac=fac)


def fr_chi_decomp(fac=2):
    """the chi lag decomposition RE-PROVED exact in Fractions on
    the r302 signed toy dc = (1, -2 | 3) with blocks (0, 0, 1):
    the single within-block pair gives T_1 = -2, Q = 14, chi = 1
    + 2 T_1 / Q = 5/7 EXACT == D/Q; the fac = 1 mutant gives 6/7
    (break 1/7 EXACT)."""
    dc = [Fr(1), Fr(-2), Fr(3)]
    jb = [0, 0, 1]
    n = len(dc)
    Q = sum(v * v for v in dc)
    T = [sum(dc[i] * dc[i + k] for i in range(n - k)
             if jb[i] == jb[i + k]) for k in range(1, n)]
    ratio = 1 + Fr(fac) * sum(T) / Q
    P = [dc[0] + dc[1], dc[2]]
    D = sum(p * p for p in P)
    return ratio, D / Q, T


def fr_uncentered_toy():
    """the m3 Fractions re-proof on the toy (2, 0, 2, 0): the
    centered lag-1 ratio is -3/4; the UNCENTERED mutant ratio
    sum z_i z_{i+1} / sum z_i^2 = 0; break 3/4 EXACT."""
    vals = [2.0, 0.0, 2.0, 0.0]
    rl, _S, _A0 = fr_lag_stats(vals, 1)
    zf = [Fr(float(v)) for v in vals]
    s1_raw = sum(zf[i] * zf[i + 1] for i in range(len(zf) - 1))
    a0_raw = sum(v * v for v in zf)
    return rl[0], s1_raw / a0_raw


def toy_lag_and_swapk():
    """lag_stats on (1,-1,1,-1) == (-3/4, +1/2, -1/4) EXACT (float
    == Fractions); net_cov float == Fractions; swap_arrange_k on
    the 4-toy (-1,-1,1,1) hits the achievable pair (-3/4, +1/2)
    exactly with the multiset preserved bitwise.  Returns (worst
    dev, toy converged)."""
    rf, _S, _A = lag_stats([1.0, -1.0, 1.0, -1.0], 3)
    rl, _Sf, _Af = fr_lag_stats([1.0, -1.0, 1.0, -1.0], 3)
    worst = max(abs(rf[0] + 0.75), abs(rf[1] - 0.5),
                abs(rf[2] + 0.25),
                abs(float(rl[0]) + 0.75), abs(float(rl[1]) - 0.5),
                abs(float(rl[2]) + 0.25),
                abs(net_cov(rf) - float(net_cov(rl))))
    zs, _p, rr, _att, conv = swap_arrange_k(
        np.array([-1.0, -1.0, 1.0, 1.0]), (-0.75, 0.5), seed=7,
        cap=800, tol=RHO_TOL_K)
    ok_ms = np.array_equal(np.sort(zs),
                           np.array([-1.0, -1.0, 1.0, 1.0]))
    worst = max(worst, abs(rr[0] + 0.75), abs(rr[1] - 0.5))
    return worst, (conv and ok_ms)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("shortrange_law_probe -- PRIME.PORT.L2.SHORTRANGE_LAW.01 "
          "(round 304)")
    print("SPEC_SHA %s   R302_SHA %s   R303_SHA %s (imported)"
          % (SPEC_SHA[:16], UTP.SPEC_SHA[:16], ATP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + every exact ward "
                        "at w9 + one lag-k build + m2/m3/m4 "
                        "mutants; ladder, slopes, families, "
                        "adjudications, censuses, mp wards skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE SHORT-RANGE LAW ROUND (reviewer contract): Leg A "
          "measures and freezes the full lag structure of the dc "
          "profile (rho_1..16, truncated net covariance, "
          "summability, exact chi lag decomposition, stability, "
          "worlds) with the sealed fine type SHORTRANGE_LAW / "
          "LONGRANGE_STRUCTURE; Leg B extends the r303 synthetic "
          "machinery to lag-k0 matching plus the graduated "
          "5-level rho_1 ladder and adjudicates LAW_SUFFICIENT / "
          "LAW_INSUFFICIENT(rest named) / LAW_LONGRANGE against "
          "the UNCHANGED r303 pipeline and bands; Leg C prints "
          "the sealed consequence map (proof goal / diagnostic / "
          "stop); NO coordinate change is introduced; ALL bars, "
          "bands, rules and verdicts sealed BEFORE evaluation")

    # ---------------- S1: census + controls (r303 scaffold verbatim)
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

    # ---------------- S2: decomposition + Leg 0 anchors
    section("S2  EXACT DECOMPOSITION + R297-R302 ANCHORS")
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
        Sr = [float(np.sum(cb[a:b])) for a, b, _s in runs]
        sg = [s for _a, _b, s in runs]
        alt_ok = all(sg[i + 1] == -sg[i]
                     for i in range(len(sg) - 1))
        R = sum(Sr)
        P = L2D.blocks_level2(Sr)
        f2 = L2D.bound_vdc(P)
        H = f2["H"]
        S_F = f2["s2"] / H
        Mr = [float(np.sum(np.abs(cb[a:b]))) for a, b, _s in runs]
        e_c2 = PBB.bound_pairsum(Mr)
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        Pd = Pb - Pw
        P_ov, P_fr, _n_b, _n_w = FDP.overlap_split(
            bxs, cts, rc["xu"], rc["cw"], rc["lo"], rc["hi"],
            brk, m)
        cconv, n_common = FDP.cconv_census(bxs, cts, rc["xu"],
                                           rc["cw"])
        full_ov = int(n_common == len(rc["bx"]) == len(rc["xu"]))
        part = DTP.participation(Pd)
        qu = NTP.quasi_uniformity(Pd)
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
        if degenerate or m == 0 or sd["n"] == 0:
            co = UTP.coherence_split(np.zeros(0), np.zeros(0),
                                     rc["lo"], rc["hi"],
                                     brk if m else np.zeros(0), m)
            rec_dev = 0.0
            eq_dev = 0.0
            na_dev = 0.0
            pr = dict(lloc=1.0, neff_atom=1.0, n=0)
            lags = [0.0] * K_LAG
            xb_sh = np.zeros(0)
            zb_sh = np.zeros(0)
            jb_sh = np.zeros(0, dtype=int)
            rho1c = 0.0
        else:
            co = UTP.coherence_split(sd["x"], sd["dc"], rc["lo"],
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
            lags = UTP.lagk_profile(sd["x"], sd["dc"], rc["lo"],
                                    rc["hi"], K_LAG)
            edm = PBB.mask_edge(sd["x"], rc["lo"], rc["hi"],
                                EDGE_F)
            xb_sh = sd["x"][~edm]
            zb_sh = sd["dc"][~edm]
            jb_sh = np.searchsorted(brk, xb_sh) if m \
                else np.zeros(0, dtype=int)
            rho1c = ATP.rho1_stat(zb_sh)[0]
        return dict(alt_ok=alt_ok, R=R, P=P, e_c2=e_c2, H=H,
                    S_F=S_F, m=m, Pd=Pd, brk=brk,
                    full_ov=full_ov, part=part, qu=qu, sd=sd,
                    df_dev=df_dev, degenerate=degenerate, co=co,
                    rec_dev=rec_dev, eq_dev=eq_dev,
                    na_dev=na_dev, pr=pr, lags=lags,
                    xb=xb_sh, zb=zb_sh, jb=jb_sh, rho1=rho1c)

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

    qid_w = max(rc["ev"]["qu"]["qid_dev"] for rc in pool_all)
    co_w = max(rc["ev"]["co"]["id_dev"] for rc in pool_all)
    cs_w = max(rc["ev"]["co"]["cs_slack"] for rc in pool_all)
    rec_w = max(rc["ev"]["rec_dev"] for rc in pool_all)
    eq_w = max(rc["ev"]["eq_dev"] for rc in all_rc)
    na_w = max(rc["ev"]["na_dev"] for rc in pool_all)
    df_w = max(rc["ev"]["df_dev"] for rc in pool_all)
    rcons_w = max(abs(rc["ev"]["rho1"] - rc["ev"]["lags"][0])
                  for rc in all_rc if rc["ev"]["sd"]["n"])
    deg_note = [("%s" % c) for c in crecs
                if crecs[c]["ev"]["degenerate"]]
    check("G22-identity-wards", qid_w <= QID_BAR and co_w <= CO_BAR
          and cs_w <= CSK_BAR and rec_w <= EQ_BAR
          and eq_w <= EQ_BAR and na_w <= NA_BAR
          and df_w <= EQ_BAR and rcons_w <= RHO_CONS_BAR,
          "identity wards on %d worlds: count identity worst %.1e "
          "(bar %.0e); coherence identity worst %.1e (bar %.0e); "
          "CS cap slack %.1e; P_shared == P_ov %.1e; CV^2 "
          "equality %.1e; n_eff_atom internal %.1e; dc == dw x f "
          "%.1e; rho1_stat == lagk consistency %.1e (bar %.0e)%s"
          % (len(pool_all), qid_w, QID_BAR, co_w, CO_BAR, cs_w,
             rec_w, eq_w, na_w, df_w, rcons_w, RHO_CONS_BAR,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

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
        neffs = [rc["ev"]["part"]["neff"] for rc in recs]
        st["neff_med"] = float(np.median(neffs))
        st["sl_neff"] = slp(neffs)
        st["sl_L1"] = slp([rc["ev"]["part"]["L1"] / M_W
                           for rc in recs])
        st["sl_D"] = slp([rc["ev"]["part"]["D"] for rc in recs])
        st["nact_med"] = med(lambda ev: ev["qu"]["n_act"])
        st["sl_nact"] = slp([rc["ev"]["qu"]["n_act"]
                             for rc in recs])
        st["nact_full"] = sum(1 for rc in recs
                              if rc["ev"]["qu"]["n_act"]
                              == rc["ev"]["m"])
        st["cv2_med"] = med(lambda ev: ev["qu"]["cv2"])
        st["sl_cv2p"] = slp([1.0 + rc["ev"]["qu"]["cv2"]
                             for rc in recs])
        st["sl_cv2p_sh"] = slp([1.0 + rc["ev"]["co"]["cv2"]
                                for rc in recs])
        st["natom_med"] = med(lambda ev: ev["pr"]["neff_atom"])
        st["sl_natom"] = slp([rc["ev"]["pr"]["neff_atom"]
                              for rc in recs])
        st["surv_med"] = med(lambda ev: ev["co"]["surv"])
        st["sl_surv"] = slp([rc["ev"]["co"]["surv"]
                             for rc in recs])
        st["chi_med"] = med(lambda ev: ev["co"]["chi"])
        st["sl_chi"] = slp([rc["ev"]["co"]["chi"]
                            for rc in recs])
        st["sl_nact_sh"] = slp([rc["ev"]["co"]["n_act"]
                                for rc in recs])
        st["sl_D_sh"] = slp([rc["ev"]["co"]["D"] for rc in recs])
        for k in range(3):
            st["rho%d" % (k + 1)] = med(
                lambda ev, k=k: ev["lags"][k])
        nact_eq = all(rc["ev"]["co"]["n_act"]
                      == rc["ev"]["qu"]["n_act"] for rc in recs)
        check("G23-r297-r300-anchors",
              abs(st["sigma"] - R297_SIGMA) <= R297_TOL
              and abs(st["sigma_star"] - R297_SIGMA_STAR)
              <= R297_TOL
              and abs(st["sl_c2"] - R297_SL_C2) <= R297_TOL
              and abs(st["sl_pref"] - R297_SL_PREF) <= R297_TOL
              and abs(st["sl_D"] - R299_SL_D) <= R299_SL_D_TOL
              and abs(st["neff_med"] - R300_NEFF_MED)
              <= R300_NEFF_TOL
              and abs(st["sl_neff"] - R300_SL_NEFF) <= R300_SL_TOL
              and abs(st["sl_L1"] - R300_SL_L1) <= R300_SL_TOL,
              "the r297/r299/r300 set recomputed bit-near: sigma "
              "%+.3f (ref %+.3f), sigma* %+.3f (ref %+.3f), sl_c2 "
              "%+.3f, sl_pref %+.3f; sl_D %+.3f (ref %+.3f); "
              "n_eff med %.2f sl %+.3f, sl_L1 %+.3f"
              % (st["sigma"], R297_SIGMA, st["sigma_star"],
                 R297_SIGMA_STAR, st["sl_c2"], st["sl_pref"],
                 st["sl_D"], R299_SL_D, st["neff_med"],
                 st["sl_neff"], st["sl_L1"]))
        check("G24-r301-anchors",
              abs(st["nact_med"] - R301_NACT_MED) <= R301_NACT_TOL
              and abs(st["sl_nact"] - R301_SL_NACT) <= R301_SL_TOL
              and st["nact_full"] == 42 and nact_eq
              and abs(st["cv2_med"] - R301_CV2_MED) <= R301_CV2_TOL
              and abs(st["sl_cv2p"] - R301_SL_CV2P) <= R301_SL_TOL
              and abs(st["natom_med"] - R301_NATOM_MED)
              <= R301_NATOM_TOL
              and abs(st["sl_natom"] - R301_SL_NATOM)
              <= R301_SL_TOL
              and abs(st["surv_med"] - R301_SURV_MED)
              <= R301_SURV_TOL
              and abs(st["sl_surv"] - R301_SL_SURV)
              <= R301_SL_TOL,
              "the r301 set recomputed bit-near: n_act med %.1f "
              "sl %+.3f COUNT LINK %d/42%s (co == qu n_act %s), "
              "CV^2 med %.2f sl_cv2p %+.3f (shared %+.3f), "
              "n_eff_atom med %.1f sl %+.3f, surv %.2f/%+.3f"
              % (st["nact_med"], st["sl_nact"], st["nact_full"],
                 " EXACT" if st["nact_full"] == 42 else "",
                 "EXACT" if nact_eq else "BROKEN",
                 st["cv2_med"], st["sl_cv2p"], st["sl_cv2p_sh"],
                 st["natom_med"], st["sl_natom"],
                 st["surv_med"], st["sl_surv"]))
        grp_y = []
        grp_m2 = []
        grp_iN = []
        for gi in range(3):
            sel = recs[gi * N_GRP:(gi + 1) * N_GRP]
            ys = []
            m2s = []
            for rc in sel:
                va = rc["ev"]["co"]["vals"]
                if len(va):
                    ys.append(va / float(np.mean(va)))
                    m2s.append(1.0 + rc["ev"]["co"]["cv2"])
            grp_y.append(np.concatenate(ys) if ys
                         else np.zeros(0))
            grp_m2.append(float(np.median(m2s)))
            grp_iN.append(float(np.median(
                [1.0 / rc["N"] for rc in sel])))
        ks13 = UTP.ks_two(grp_y[0], grp_y[2])
        ks23 = UTP.ks_two(grp_y[1], grp_y[2])
        A_fs, B_fs, pred = UTP.fs_solve(
            1.0 / grp_iN[0], grp_m2[0], 1.0 / grp_iN[2],
            grp_m2[2], 1.0 / grp_iN[1])
        fs_dev = abs(pred - grp_m2[1]) / max(grp_m2[1], 1e-300)
        st.update(ks13=ks13, ks23=ks23, A_fs=A_fs, fs_dev=fs_dev)
        check("G25-r302-anchors",
              abs(st["chi_med"] - R302_CHI_MED) <= R302_CHI_TOL
              and abs(st["sl_chi"] - R302_SL_CHI) <= R301_SL_TOL
              and all(abs(st["rho%d" % (k + 1)] - R302_RHO[k])
                      <= R302_RHO_TOL for k in range(3))
              and abs(ks13 - R302_KS13) <= R302_KS_TOL
              and abs(ks23 - R302_KS23) <= R302_KS_TOL
              and ks13 <= KS_STAT
              and abs(A_fs - R302_A_FS) <= R302_A_TOL
              and fs_dev <= FS_BAR,
              "the r302 set recomputed bit-near: chi med %.3f sl "
              "%+.3f (destructive, falling); rho_1/2/3 med "
              "%+.3f/%+.3f/%+.3f; stationarity KS(G1,G3) %.3f "
              "KS(G2,G3) %.3f (STATIONARY %s); 1/N transient A "
              "%.3f held-out dev %.3f (bar %.2f)"
              % (st["chi_med"], st["sl_chi"], st["rho1"],
                 st["rho2"], st["rho3"], ks13, ks23,
                 ks13 <= KS_STAT, A_fs, fs_dev, FS_BAR))
    else:
        check("G23-r297-r300-anchors", True,
              "SMOKE: skipped (needs the 42-rung ladder)")
        check("G24-r301-anchors", True, "SMOKE: skipped")
        check("G25-r302-anchors", True, "SMOKE: skipped")

    # ---------------- S3: exact section + toys + audits
    section("S3  EXACT SECTION (FRACTIONS) + TOYS + SCOPE AUDITS")
    rl_toy, nc_toy = fr_netcov_toy()
    _rl1, nc_m1 = fr_netcov_toy(fac=1)
    ok_nc = (rl_toy[0] == Fr(-3, 4) and rl_toy[1] == Fr(1, 2)
             and rl_toy[2] == Fr(-1, 4) and nc_toy == 0
             and nc_m1 == Fr(1, 2))
    chi_fr, chi_dq, T_fr = fr_chi_decomp()
    chi_m1, _dq1, _T1 = fr_chi_decomp(fac=1)
    ok_chi = (chi_fr == Fr(5, 7) and chi_dq == Fr(5, 7)
              and chi_m1 == Fr(6, 7)
              and T_fr[0] == Fr(-2) and T_fr[1] == 0)
    check("G30-fractions-netcov-m1", ok_nc and ok_chi,
          "the F1 zero-sum tautology RE-PROVED exact in Fractions "
          "on (1,-1,1,-1): lag profile (%s, %s, %s), full net "
          "covariance 1 + 2 sum = %s EXACT; m1 FACTOR-1 MUTANT "
          "gives %s != 0 EXACT -- CAUGHT; the F2 chi "
          "decomposition on (1,-2|3): 1 + 2 T_1/Q = %s == D/Q = "
          "%s EXACT (T = %s); factor-1 mutant %s (break 1/7 "
          "EXACT) -- the factor 2 on the cross terms is "
          "load-bearing on BOTH identities"
          % (rl_toy[0], rl_toy[1], rl_toy[2], nc_toy, nc_m1,
             chi_fr, chi_dq, T_fr, chi_m1))
    mc_fr = ATP.fr_margin_chain()
    ok_fr = (mc_fr["mD"] == Fr(3, 50) and mc_fr["mN"] == Fr(3, 50)
             and mc_fr["mU"] == Fr(3, 50)
             and mc_fr["mA"] == Fr(3, 50)
             and mc_fr["dN"] == 0 and mc_fr["dU"] == 0
             and mc_fr["dB"] == 0 and mc_fr["dA"] == 0)
    r_cent, r_unc = fr_uncentered_toy()
    ok_m3 = (r_cent == Fr(-3, 4) and r_unc == 0
             and abs(r_cent - r_unc) == Fr(3, 4))
    check("G31-fractions-marginchain-m3",
          ok_fr and ok_m3,
          "the r303 margin chain RE-PROVED exact in Fractions "
          "(all four margins == 3/50, devs 0 -- Leg 0 anchor); "
          "m3 UNCENTERED-FIELD MUTANT on the toy (2,0,2,0): "
          "centered lag-1 ratio %s vs uncentered %s, break 3/4 "
          "EXACT -- CAUGHT: the centering is load-bearing"
          % (r_cent, r_unc))
    toy_w, toy_conv = toy_lag_and_swapk()
    check("G32-toy-exactness", toy_w <= TOY_BAR and toy_conv,
          "lag_stats toys EXACT ((1,-1,1,-1) -> (-3/4, +1/2, "
          "-1/4); float == Fractions; net_cov float == Fractions; "
          "worst dev %.1e, bar %.0e); swap_arrange_k hits the "
          "achievable pair (-3/4, +1/2) on the 4-toy with the "
          "multiset preserved bitwise (%s)"
          % (toy_w, TOY_BAR,
             "converged" if toy_conv else "MISS"))
    h_ls = scope_audit("lag_stats", BOUND_FORBIDDEN)
    h_nc = scope_audit("net_cov", BOUND_FORBIDDEN)
    h_cl = scope_audit("chi_lag_terms", BOUND_FORBIDDEN)
    h_sk = scope_audit("swap_arrange_k", BOUND_FORBIDDEN)
    h_sw = scope_audit("swap_arrange_wb", BOUND_FORBIDDEN)
    h_lw = scope_audit("lagk_ward", BOUND_FORBIDDEN)
    h_gift = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    h_peek = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    clean = not (h_ls or h_nc or h_cl or h_sk or h_sw or h_lw)
    check("G33-scope-audits", clean and bool(h_gift)
          and bool(h_peek) and not ag_hits,
          "the new builders (lag_stats, net_cov, chi_lag_terms, "
          "swap_arrange_k, swap_arrange_wb, lagk_ward) consume "
          "profile values / positions / block indices only (no "
          "truth-side identifier in scope%s); m5a gift mutant "
          "FLAGGED (%s); m5b branch-peek mutant FLAGGED (%s); "
          "fragment audit: %s (both swap searches are seeded "
          "greedy descents, no fit primitive)"
          % ("" if clean else " VIOLATION",
             "; ".join(h_gift) if h_gift else "NOT FLAGGED",
             "; ".join(h_peek) if h_peek else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S4: Leg 0b + Leg A -- the law
    section("S4  LEG A: THE SHORT-RANGE LAW (MEASURED)")
    if not smoke:
        mc = ATP.margin_chain(st["sigma_star"], st["sl_D"],
                              st["sl_L1"], st["sl_neff"],
                              st["sl_nact"], st["sl_cv2p"],
                              st["sl_cv2p_sh"], st["sl_chi"],
                              st["sl_surv"], st["sl_natom"])
        inv_ok = (mc["dN"] <= PROP_BAR and mc["dU"] <= PROP_BAR
                  and mc["dB"] <= PROP_BAR
                  and mc["dA"] <= PROP_BAR)
        marg_ok = all(abs(v - MARGIN_REF) <= MARGIN_TOL
                      for v in (mc["mD"], mc["mN"], mc["mU"],
                                mc["mA"]))
        check("G40-margin-chain-anchor", inv_ok and marg_ok,
              "the r303 MARGIN_CHAIN live (Leg 0): m_D %+.4f / "
              "m_NEFF %+.4f / m_UNIF %+.4f (blk) %+.4f (sh) / "
              "m_ATOM %+.4f (record +0.0547 each); invariance "
              "devs %.1e/%.1e/%.1e/%.1e (bar %.0e); the ONE core "
              "S = sigma* - sl_D = %+.4f"
              % (mc["mD"], mc["mN"], mc["mU"], mc["mUs"],
                 mc["mA"], mc["dN"], mc["dU"], mc["dB"],
                 mc["dA"], PROP_BAR, mc["mD"]))
        st["mc"] = mc
        s1_signs = []
        alts = []
        for rc in recs:
            _r1, S1, _A0 = ATP.rho1_stat(rc["ev"]["zb"])
            s1_signs.append(S1 < 0.0)
            alts.append(ATP.alt_census(rc["ev"]["zb"]))
        n_neg = sum(s1_signs)
        alt_med = float(np.median(alts))
        check("G41-rho-sign-census",
              n_neg == R303_NNEG
              and abs(alt_med - R303_ALT_MED) <= R303_ALT_TOL,
              "RHO_SIGN reproduced (Leg 0): S1 < 0 on %d/42 rungs "
              "(record %d/42, NOT uniform -- honest), alternation "
              "med %.3f (record %.3f)"
              % (n_neg, R303_NNEG, alt_med, R303_ALT_MED))
        st["n_neg"] = n_neg

        # ---- the lag profile
        rho_mat = np.array([lag_stats(rc["ev"]["zb"], K_FULL)[0]
                            for rc in recs])
        cons_w = 0.0
        zs_w = 0.0
        for rc in recs:
            rr_, S_, A0_ = lag_stats(rc["ev"]["zb"], K_LAG)
            cons_w = max(cons_w, float(np.max(np.abs(
                rr_ - np.asarray(rc["ev"]["lags"])))))
            zb = rc["ev"]["zb"]
            zc = zb - float(np.mean(zb))
            Afull = np.correlate(zc, zc, mode="full")[len(zc) - 1:]
            zs_w = max(zs_w, abs(Afull[0] + 2.0
                                 * float(np.sum(Afull[1:])))
                       / max(Afull[0], 1e-300))
        med_k = np.median(rho_mat, axis=0)
        q25 = np.percentile(rho_mat, 25, axis=0)
        q75 = np.percentile(rho_mat, 75, axis=0)
        check("G42-lag-profile-table",
              cons_w <= LAG_CONS_BAR and zs_w <= ZS_BAR,
              "lag_stats == UTP.lagk_profile on k <= %d over 42 "
              "rungs (worst dev %.1e, bar %.0e); F1 zero-sum "
              "tautology live: |1 + 2 sum_all| <= %.1e x A0 (bar "
              "%.0e) -- the truncated NC is the content, the full "
              "sum is a tautology (disclosed)"
              % (K_LAG, cons_w, LAG_CONS_BAR, zs_w, ZS_BAR))
        for k in range(K_FULL):
            info("rho_%-2d med %+.4f  IQR [%+.4f, %+.4f]"
                 % (k + 1, med_k[k], q25[k], q75[k]))
        k0 = None
        for k in range(K0_MIN, K0_MAX + 1):
            if all(abs(med_k[j]) <= RHO_SMALL
                   for j in range(k, K_FULL)):
                k0 = k
                break
        nc_cum = 1.0 + 2.0 * np.cumsum(med_k)
        sum_abs = float(np.sum(np.abs(med_k)))
        tail_sum = float(np.sum(np.abs(med_k[k0:]))) \
            if k0 else float("nan")
        nc_k0 = float(nc_cum[k0 - 1]) if k0 else float("nan")
        nc_K = float(nc_cum[-1])
        head_abs = float(np.mean(np.abs(med_k[:8])))
        tail_abs = float(np.mean(np.abs(med_k[8:])))
        check("G43-netcov-summability", True,
              "NC(k) = 1 + 2 sum med rho: NC(1) %.3f NC(2) %.3f "
              "NC(3) %.3f NC(4) %.3f NC(8) %.3f NC(16) %.3f; "
              "SUM(16) = sum |med rho_k| = %.3f; k0 candidate %s "
              "(rule: |med rho_j| <= %.2f for all j > k0); tail "
              "sum %s; mean |med rho| k 1..8 %.4f vs k 9..16 "
              "%.4f (tail/head %.2f)"
              % (nc_cum[0], nc_cum[1], nc_cum[2], nc_cum[3],
                 nc_cum[7], nc_K, sum_abs,
                 str(k0) if k0 else "NONE <= %d" % K0_MAX,
                 RHO_SMALL,
                 "%.3f" % tail_sum if k0 else "n/a",
                 head_abs, tail_abs,
                 tail_abs / max(head_abs, 1e-300)))
        h1 = np.median(rho_mat[:21], axis=0)
        h2 = np.median(rho_mat[21:], axis=0)
        k0_eff = k0 if k0 else K0_MAX
        st["k0_eff"] = k0_eff
        half_dev = float(np.max(np.abs(h1[:k0_eff]
                                       - h2[:k0_eff])))
        sign_agree = sum(1 for j in range(3)
                         if h1[j] * h2[j] > 0)
        wnote = []
        for c in ("EPST", "SCR"):
            rw, _S, _A = lag_stats(crecs[c]["ev"]["zb"], K_LAG)
            wnote.append("%s (%s)" % (c, "/".join(
                "%+.2f" % v for v in rw[:4])))
        check("G44-stability-worlds", True,
              "halves stability (first 21 vs last 21 rungs by N): "
              "med rho_1..3 %+.3f/%+.3f/%+.3f vs "
              "%+.3f/%+.3f/%+.3f, sign agreement %d/3, max |dev| "
              "over k <= %d: %.3f (census, anti-extrapolation "
              "honesty); world lag profiles rho_1..4: %s vs MAIN "
              "(%s) -- census"
              % (h1[0], h1[1], h1[2], h2[0], h2[1], h2[2],
                 sign_agree, k0_eff, half_dev,
                 "; ".join(wnote),
                 "/".join("%+.2f" % v for v in med_k[:4])))

        # ---- the exact chi lag decomposition (real profile)
        c_real = np.zeros(K_FULL + 1)
        c_cnt = np.zeros(K_FULL + 1)
        c_rows = []
        dec_w = 0.0
        for rc in recs:
            ev = rc["ev"]
            T, Qv, ratio = chi_lag_terms(ev["zb"], ev["jb"])
            dec_w = max(dec_w, abs(ratio - ev["co"]["chi"])
                        / max(abs(ev["co"]["chi"]), 1e-300))
            row = np.zeros(K_FULL + 1)
            for kk, tv in enumerate(T):
                b = min(kk, K_FULL)
                row[b] += 2.0 * tv / max(Qv, 1e-300)
            c_rows.append(row)
        for c in ("EPST", "SCR"):
            ev = crecs[c]["ev"]
            if ev["degenerate"] or len(ev["zb"]) == 0:
                continue
            T, Qv, ratio = chi_lag_terms(ev["zb"], ev["jb"])
            dec_w = max(dec_w, abs(ratio - ev["co"]["chi"])
                        / max(abs(ev["co"]["chi"]), 1e-300))
        c_rows = np.array(c_rows)
        c_med = np.median(c_rows, axis=0)
        check("G45-chi-lag-decomposition", dec_w <= DEC_BAR,
              "F2 EXACT on every non-degenerate world: chi == 1 + "
              "2 sum_k T_k/Q, worst recomposition dev %.1e (bar "
              "%.0e); real med shares c_k: c_1 %+.4f c_2 %+.4f "
              "c_3 %+.4f c_4 %+.4f sum(5..16) %+.4f tail(>16) "
              "%+.4f -- the destructive chi level in lag "
              "coordinates"
              % (dec_w, DEC_BAR, c_med[0], c_med[1], c_med[2],
                 c_med[3], float(np.sum(c_med[4:K_FULL])),
                 c_med[K_FULL]))
        shortrange = (k0 is not None and tail_sum <= TAIL_MAX
                      and nc_K < NC_MAX)
        if shortrange:
            law_a = ("SHORTRANGE_LAW(k0 = %d, NC(k0) %.3f, "
                     "NC(16) %.3f, SUM %.3f)"
                     % (k0, nc_k0, nc_K, sum_abs))
        else:
            law_a = ("LONGRANGE_STRUCTURE(k0 %s, tail %s, "
                     "NC(16) %.3f)"
                     % (str(k0),
                        "%.3f" % tail_sum if k0 else "n/a", nc_K))
        check("G46-shortrange-adjudication", True,
              "SEALED RULE fired: %s -- rule: k0 exists <= %d AND "
              "tail sum <= %.2f AND NC(16) < %.1f (net-negative "
              "correlation sum, the reviewer's sign condition); "
              "measured on 42 rungs, medians"
              % (law_a, K0_MAX, TAIL_MAX, NC_MAX))
        st["shortrange"] = shortrange
        st["law_a"] = law_a
        st["k0"] = k0
        st["med_k"] = med_k
        st["c_med"] = c_med
        st["nc_K"] = nc_K
        st["sum_abs"] = sum_abs
    else:
        for g in ("G40-margin-chain-anchor", "G41-rho-sign-census",
                  "G42-lag-profile-table", "G43-netcov-summability",
                  "G44-stability-worlds",
                  "G45-chi-lag-decomposition",
                  "G46-shortrange-adjudication"):
            check(g, True, "SMOKE: skipped (needs the ladder)")
        st["k0_eff"] = 3
        st["shortrange"] = None

    # ---------------- S5: Leg B -- families
    section("S5  LEG B: SYNTHETIC FAMILIES (R303 REPLICATION + "
            "LAG-K0 + GRADUATED)")
    fam_defs = (("A_RHO_MATCH", 0, lambda r1: r1),
                ("B_RHO_ZERO", 1, lambda r1: 0.0),
                ("C_RHO_FLIP", 2, lambda r1: -r1))
    seeds_used = set()
    if smoke:
        rc0 = recs[0]
        ev0 = rc0["ev"]
        tg0 = lag_stats(ev0["zb"], 3)[0]
        zs, perm, rr_s, att, conv = swap_arrange_k(
            ev0["zb"], tg0, SEED_BASE_K,
            min(SWAP_F_K * len(ev0["zb"]), SWAP_CAP_K), RHO_TOL_K)
        ok_ms = np.array_equal(np.sort(zs), np.sort(ev0["zb"]))
        co_s = UTP.coherence_split(ev0["xb"], zs, rc0["lo"],
                                   rc0["hi"], ev0["brk"],
                                   ev0["m"])
        na_inv = abs(co_s["natom"] - ev0["co"]["natom"]) \
            / max(ev0["co"]["natom"], 1e-300)
        fix = float(np.mean(perm == np.arange(len(ev0["zb"]))))
        check("G50-r303-family-replication", conv and ok_ms
              and na_inv <= NA_INV_BAR and fix <= FIX_MAX,
              "SMOKE build (w9, lag-3 match, rep 0): converged %s "
              "(rho %s target %s), marginal sorted-bitwise %s, "
              "natom invariance %.1e (bar %.0e), fixed-point "
              "share %.3f; real w9 chi %.3f -> synthetic chi %.3f"
              % (conv, "/".join("%+.3f" % v for v in rr_s),
                 "/".join("%+.3f" % v for v in tg0), ok_ms,
                 na_inv, NA_INV_BAR, fix, ev0["co"]["chi"],
                 co_s["chi"]))
        fam_res = {}
    else:
        fam_res = {}
        conv_n = 0
        n_builds = 0
        worst_rho_miss = 0.0
        worst_fix = 0.0
        na_inv_worst = 0.0
        ms_ok_all = True
        cA_rows = []
        for fname, fi, tfun in fam_defs:
            reps = []
            for rep in range(R_REP):
                chi_l = []
                cv2p_l = []
                D_l = []
                natom_l = []
                for ri, rc in enumerate(recs):
                    ev = rc["ev"]
                    seed = SEED_BASE + ri * 100 + fi * 10 + rep
                    seeds_used.add(seed)
                    tgt = tfun(ev["rho1"])
                    zb = ev["zb"]
                    zs, perm, r1s, att, conv = ATP.swap_arrange(
                        zb, tgt, seed,
                        min(SWAP_F * len(zb), SWAP_CAP))
                    n_builds += 1
                    conv_n += int(conv)
                    worst_rho_miss = max(worst_rho_miss,
                                         abs(r1s - tgt))
                    if fi == 0:
                        fixshare = float(np.mean(
                            perm == np.arange(len(zb))))
                        worst_fix = max(worst_fix, fixshare)
                        T_s, Q_s, _rat = chi_lag_terms(zs,
                                                       ev["jb"])
                        rowc = np.zeros(K_FULL + 1)
                        for kk, tv in enumerate(T_s):
                            b = min(kk, K_FULL)
                            rowc[b] += 2.0 * tv / max(Q_s, 1e-300)
                        cA_rows.append(rowc)
                    ms_ok_all = ms_ok_all and np.array_equal(
                        np.sort(zs), np.sort(zb))
                    co_s = UTP.coherence_split(
                        ev["xb"], zs, rc["lo"], rc["hi"],
                        ev["brk"], ev["m"])
                    na_inv_worst = max(
                        na_inv_worst,
                        abs(co_s["natom"] - ev["co"]["natom"])
                        / max(ev["co"]["natom"], 1e-300))
                    chi_l.append(co_s["chi"])
                    cv2p_l.append(1.0 + co_s["cv2"])
                    D_l.append(co_s["D"])
                    natom_l.append(co_s["natom"])
                reps.append(dict(
                    chi=float(np.median(chi_l)),
                    slc=L2D.halves_slope(Ns, cv2p_l),
                    slD=L2D.halves_slope(Ns, D_l),
                    sln=L2D.halves_slope(Ns, natom_l)))
            fam_res[fname] = dict(
                chi=float(np.median([r["chi"] for r in reps])),
                chi_lo=min(r["chi"] for r in reps),
                chi_hi=max(r["chi"] for r in reps),
                slc=float(np.median([r["slc"] for r in reps])),
                slD=float(np.median([r["slD"] for r in reps])),
                slD_lo=min(r["slD"] for r in reps),
                slD_hi=max(r["slD"] for r in reps),
                sln=float(np.median([r["sln"] for r in reps])))
        conv_share = conv_n / max(n_builds, 1)
        anch_ok = all(
            abs(fam_res[f]["chi"] - R303_FAM_CHI[f])
            <= R303_FAM_CHI_TOL
            and abs((st["sigma_star"] - fam_res[f]["slD"])
                    - R303_FAM_MARGIN[f]) <= R303_FAM_MARGIN_TOL
            for f, _fi, _t in fam_defs)
        check("G50-r303-family-replication",
              conv_share >= CONV_MIN and ms_ok_all
              and worst_fix <= FIX_MAX
              and na_inv_worst <= NA_INV_BAR and anch_ok,
              "the r303 ladder REPLICATED with the SAME seeds "
              "(%d builds): convergence %d/%d (share %.3f >= "
              "%.2f), worst |rho1 - target| %.2e, fixed-point "
              "max %.3f, marginal bitwise %s, natom invariance "
              "%.1e; chi ladder %.3f / %.3f / %.3f (records "
              "0.764 / 1.029 / 1.342), margins %+.3f / %+.3f / "
              "%+.3f (records +0.057 / +0.032 / -0.044) -- "
              "bit-near anchors %s"
              % (n_builds, conv_n, n_builds, conv_share, CONV_MIN,
                 worst_rho_miss, worst_fix,
                 "OK" if ms_ok_all else "BROKEN", na_inv_worst,
                 fam_res["A_RHO_MATCH"]["chi"],
                 fam_res["B_RHO_ZERO"]["chi"],
                 fam_res["C_RHO_FLIP"]["chi"],
                 st["sigma_star"] - fam_res["A_RHO_MATCH"]["slD"],
                 st["sigma_star"] - fam_res["B_RHO_ZERO"]["slD"],
                 st["sigma_star"] - fam_res["C_RHO_FLIP"]["slD"],
                 "HELD" if anch_ok else "MISSED"))
        cA_med = np.median(np.array(cA_rows), axis=0)
        d_c = cA_med - st["c_med"]
        rng_note = ("k<=3 %+.4f | k 4..8 %+.4f | k 9..16 %+.4f | "
                    ">16 %+.4f"
                    % (float(np.sum(d_c[:3])),
                       float(np.sum(d_c[3:8])),
                       float(np.sum(d_c[8:K_FULL])),
                       d_c[K_FULL]))
        check("G51-chi-gap-attribution", True,
              "CHI_GAP lag attribution (med c_k rho1-matched "
              "minus real): c_1 %+.4f c_2 %+.4f c_3 %+.4f c_4 "
              "%+.4f; by range: %s; total %+.4f (the r303 chi "
              "level miss 0.134 in lag coordinates) -- census"
              % (d_c[0], d_c[1], d_c[2], d_c[3], rng_note,
                 float(np.sum(d_c))))
        st["d_c"] = d_c

        # ---- the lag-k0 matching family (a)
        k0_eff = st["k0_eff"]
        tg_all = [lag_stats(rc["ev"]["zb"], k0_eff)[0]
                  for rc in recs]
        conv_k = 0
        n_k = 0
        worst_kdev = 0.0
        fix_k = 0.0
        na_k = 0.0
        ms_k = True
        dec_k = 0.0
        cK_rows = []
        reps_k = []
        for rep in range(R_REP_K):
            chi_l = []
            cv2p_l = []
            D_l = []
            for ri, rc in enumerate(recs):
                ev = rc["ev"]
                seed = SEED_BASE_K + ri * 100 + 0 * 10 + rep
                seeds_used.add(seed)
                zb = ev["zb"]
                zs, perm, rr_s, att, conv = swap_arrange_k(
                    zb, tg_all[ri], seed,
                    min(SWAP_F_K * len(zb), SWAP_CAP_K),
                    RHO_TOL_K)
                n_k += 1
                conv_k += int(conv)
                _ok_w, dv = lagk_ward(zs, tg_all[ri], RHO_TOL_K)
                worst_kdev = max(worst_kdev, dv)
                fix_k = max(fix_k, float(np.mean(
                    perm == np.arange(len(zb)))))
                ms_k = ms_k and np.array_equal(np.sort(zs),
                                               np.sort(zb))
                co_s = UTP.coherence_split(
                    ev["xb"], zs, rc["lo"], rc["hi"], ev["brk"],
                    ev["m"])
                na_k = max(na_k,
                           abs(co_s["natom"] - ev["co"]["natom"])
                           / max(ev["co"]["natom"], 1e-300))
                T_s, Q_s, rat = chi_lag_terms(zs, ev["jb"])
                dec_k = max(dec_k, abs(rat - co_s["chi"])
                            / max(abs(co_s["chi"]), 1e-300))
                rowc = np.zeros(K_FULL + 1)
                for kk, tv in enumerate(T_s):
                    b = min(kk, K_FULL)
                    rowc[b] += 2.0 * tv / max(Q_s, 1e-300)
                cK_rows.append(rowc)
                chi_l.append(co_s["chi"])
                cv2p_l.append(1.0 + co_s["cv2"])
                D_l.append(co_s["D"])
            reps_k.append(dict(
                chi=float(np.median(chi_l)),
                slc=L2D.halves_slope(Ns, cv2p_l),
                slD=L2D.halves_slope(Ns, D_l)))
        lagk = dict(
            chi=float(np.median([r["chi"] for r in reps_k])),
            chi_lo=min(r["chi"] for r in reps_k),
            chi_hi=max(r["chi"] for r in reps_k),
            slc=float(np.median([r["slc"] for r in reps_k])),
            slc_lo=min(r["slc"] for r in reps_k),
            slc_hi=max(r["slc"] for r in reps_k),
            slD=float(np.median([r["slD"] for r in reps_k])),
            slD_lo=min(r["slD"] for r in reps_k),
            slD_hi=max(r["slD"] for r in reps_k))
        conv_share_k = conv_k / max(n_k, 1)
        check("G52-lagk-construction-wards",
              conv_share_k >= CONV_MIN_K and ms_k
              and fix_k <= FIX_MAX and na_k <= NA_INV_BAR
              and dec_k <= DEC_BAR,
              "LAGK_MATCH construction (42 rungs x %d replicates "
              "= %d builds, k0 = %d, per-rung targets): "
              "convergence %d/%d (share %.3f >= %.2f), worst "
              "max_k |rho_k - target| %.3f (tol %.2f), "
              "fixed-point max %.3f, marginal bitwise %s, natom "
              "invariance %.1e, F2 recomposition on builds %.1e"
              % (R_REP_K, n_k, k0_eff, conv_k, n_k, conv_share_k,
                 CONV_MIN_K, worst_kdev, RHO_TOL_K, fix_k,
                 "OK" if ms_k else "BROKEN", na_k, dec_k))
        cK_med = np.median(np.array(cK_rows), axis=0)
        d_cK = cK_med - st["c_med"]
        real = dict(chi=st["chi_med"], slc=st["sl_cv2p_sh"],
                    slD=st["sl_D_sh"])
        d_chi = abs(lagk["chi"] - real["chi"])
        d_slc = abs(lagk["slc"] - real["slc"])
        d_slD = abs(lagk["slD"] - real["slD"])
        repro_k = (d_chi <= CHI_BAND and d_slc <= SLP_BAND
                   and d_slD <= SLP_BAND)
        info("REAL        chi %.3f          sl_cv2p %+.3f "
             "sl_D %+.3f margin %+.3f"
             % (real["chi"], real["slc"], real["slD"],
                st["sigma_star"] - real["slD"]))
        info("LAGK_MATCH  chi %.3f [%.3f, %.3f] sl_cv2p %+.3f "
             "[%+.3f, %+.3f] sl_D %+.3f [%+.3f, %+.3f] margin "
             "%+.3f"
             % (lagk["chi"], lagk["chi_lo"], lagk["chi_hi"],
                lagk["slc"], lagk["slc_lo"], lagk["slc_hi"],
                lagk["slD"], lagk["slD_lo"], lagk["slD_hi"],
                st["sigma_star"] - lagk["slD"]))
        info("RHO1_MATCH  chi %.3f [%.3f, %.3f] (r303 (a), the "
             "anchor column)"
             % (fam_res["A_RHO_MATCH"]["chi"],
                fam_res["A_RHO_MATCH"]["chi_lo"],
                fam_res["A_RHO_MATCH"]["chi_hi"]))
        check("G53-lagk-sufficiency-table", True,
              "LAGK_TABLE: |d chi| %.3f (band %.2f), |d sl_cv2p| "
              "%.3f (band %.2f), |d sl_D| %.3f (band %.2f) -- "
              "%s; the family's own within-block shares vs real: "
              "d c_1 %+.4f d c_2 %+.4f d c_3 %+.4f (does GLOBAL "
              "lag matching move the WITHIN-BLOCK terms?)"
              % (d_chi, CHI_BAND, d_slc, SLP_BAND, d_slD,
                 SLP_BAND,
                 "ALL WITHIN BANDS" if repro_k else
                 "MISSES (see G60)",
                 d_cK[0], d_cK[1], d_cK[2]))
        st["lagk"] = lagk
        st["repro_k"] = repro_k
        st["d_kq"] = (d_chi, d_slc, d_slD)
        st["d_cK"] = d_cK

        # ---- the graduated rho_1 ladder (c)
        conv_g = 0
        n_g = 0
        ms_g = True
        na_g = 0.0
        grad_tab = {}
        for li, (lev, ltag) in enumerate(GRAD_LEVELS):
            reps_g = []
            for rep in range(R_REP_G):
                chi_l = []
                cv2p_l = []
                D_l = []
                for ri, rc in enumerate(recs):
                    ev = rc["ev"]
                    seed = SEED_BASE_K + ri * 100 \
                        + (1 + li) * 10 + rep
                    seeds_used.add(seed)
                    zb = ev["zb"]
                    zs, perm, r1s, att, conv = ATP.swap_arrange(
                        zb, lev, seed,
                        min(SWAP_F * len(zb), SWAP_CAP))
                    n_g += 1
                    conv_g += int(conv)
                    ms_g = ms_g and np.array_equal(
                        np.sort(zs), np.sort(zb))
                    co_s = UTP.coherence_split(
                        ev["xb"], zs, rc["lo"], rc["hi"],
                        ev["brk"], ev["m"])
                    na_g = max(na_g,
                               abs(co_s["natom"]
                                   - ev["co"]["natom"])
                               / max(ev["co"]["natom"], 1e-300))
                    chi_l.append(co_s["chi"])
                    cv2p_l.append(1.0 + co_s["cv2"])
                    D_l.append(co_s["D"])
                reps_g.append(dict(
                    chi=float(np.median(chi_l)),
                    slc=L2D.halves_slope(Ns, cv2p_l),
                    slD=L2D.halves_slope(Ns, D_l)))
            grad_tab[ltag] = dict(
                lev=lev,
                chi=float(np.median([r["chi"] for r in reps_g])),
                slc=float(np.median([r["slc"] for r in reps_g])),
                slD=float(np.median([r["slD"] for r in reps_g])))
        conv_share_g = conv_g / max(n_g, 1)
        check("G54-graduated-construction-wards",
              conv_share_g >= CONV_MIN and ms_g
              and na_g <= NA_INV_BAR,
              "GRADUATED LADDER construction (42 rungs x 5 levels "
              "x %d replicates = %d builds, absolute targets, "
              "r303 swap_arrange UNCHANGED): convergence %d/%d "
              "(share %.3f >= %.2f), marginal bitwise %s, natom "
              "invariance %.1e"
              % (R_REP_G, n_g, conv_g, n_g, conv_share_g,
                 CONV_MIN, "OK" if ms_g else "BROKEN", na_g))
        m_real = st["sigma_star"] - real["slD"]
        chis = []
        mrgs = []
        for lev, ltag in GRAD_LEVELS:
            g = grad_tab[ltag]
            mg = st["sigma_star"] - g["slD"]
            chis.append(g["chi"])
            mrgs.append(mg)
            info("rho1 = %+.1f: chi %.3f sl_cv2p %+.3f sl_D "
                 "%+.3f margin %+.3f (d vs real %+.3f) "
                 "inequality %s"
                 % (lev, g["chi"], g["slc"], g["slD"], mg,
                    mg - m_real,
                    "HOLDS" if mg > 0 else "FAILS"))
        mono_chi = all(chis[i] > chis[i + 1]
                       for i in range(len(chis) - 1))
        mono_mrg = all(mrgs[i] < mrgs[i + 1]
                       for i in range(len(mrgs) - 1))
        check("G55-graduated-slack-response", True,
              "SLACK_RESPONSE (levels +0.2 / 0.0 / -0.1 / -0.2 / "
              "-0.3): chi %s; margin %s; monotone chi in rho_1 "
              "%s, anti-monotone margin %s -- the reviewer's "
              "graduated causal ladder, measured"
              % ("/".join("%.3f" % c for c in chis),
                 "/".join("%+.3f" % m for m in mrgs),
                 mono_chi, mono_mrg))
        st["grad_tab"] = grad_tab
        st["grad_chis"] = chis
        st["grad_mrgs"] = mrgs
        st["fam_res"] = fam_res
    # m2 + m3 + m4 mutants (on w9, both modes)
    rc0 = recs[0]
    ev0 = rc0["ev"]
    zb0 = ev0["zb"]
    n0 = len(zb0)
    L1a0 = float(np.sum(np.abs(zb0)))
    Q0 = float(np.sum(zb0 * zb0))
    z_m2 = (L1a0 / n0) * np.where(np.arange(n0) % 2 == 0, 1.0,
                                  -1.0)
    m2_sorted_breaks = not np.array_equal(np.sort(z_m2),
                                          np.sort(zb0))
    Q_m2 = float(np.sum(z_m2 * z_m2))
    m2_qdev = abs(Q_m2 - Q0) / max(Q0, 1e-300)
    r1c, S1c, A0c = lag_stats(zb0, 1)
    S1_raw = float(np.dot(zb0[:-1], zb0[1:]))
    r1_raw = S1_raw / max(Q0, 1e-300)
    m3_dev = abs(float(r1c[0]) - r1_raw)
    k_m4 = max(st.get("k0_eff", 3), 3)
    tg_m4 = lag_stats(zb0, k_m4)[0]
    zs_m4, _p4, _r4, _a4, _c4 = ATP.swap_arrange(
        zb0, float(tg_m4[0]), M4_SEED,
        min(SWAP_F * n0, SWAP_CAP))
    ok_m4w, dev_m4 = lagk_ward(zs_m4, tg_m4, RHO_TOL_K)
    check("G56-mustfails-m2-m3-m4",
          m2_sorted_breaks and m2_qdev >= MUT_MIN
          and m3_dev >= MUT_MIN and not ok_m4w,
          "m2 UNMATCHED MARGINAL: sorted-multiset ward BREAKS "
          "(%s) AND atom energy deviates rel %.1e >= %.0e LOUD; "
          "m3 UNCENTERED FIELD on real w9: |rho_1 centered - "
          "raw| = %.3f >= %.0e -- CAUGHT; m4 FAMILY SMUGGLE: the "
          "rho_1-only build (seed %d) FAILS the lag-%d ward (max "
          "dev %.3f > tol %.2f) -- CAUGHT: the lag-k0 ward "
          "separates the families"
          % (m2_sorted_breaks, m2_qdev, MUT_MIN, m3_dev, MUT_MIN,
             M4_SEED, k_m4, dev_m4, RHO_TOL_K))

    # ---------------- S6: the law adjudication
    section("S6  LAW ADJUDICATION")
    if not smoke:
        seeds_ok = len(seeds_used) == (1008 + 42 * R_REP_K
                                       + 42 * 5 * R_REP_G)
        if not st["shortrange"]:
            law = "LAW_LONGRANGE"
            rest = ("the reviewer stop case: the measured lag "
                    "structure is NOT short-range under the "
                    "sealed rule")
        elif st["repro_k"]:
            law = "LAW_SUFFICIENT"
            rest = ""
        else:
            d_chi, d_slc, d_slD = st["d_kq"]
            parts = []
            if d_chi > CHI_BAND:
                parts.append("chi by %.3f" % d_chi)
            if d_slc > SLP_BAND:
                parts.append("sl_cv2p by %.3f" % d_slc)
            if d_slD > SLP_BAND:
                parts.append("sl_D by %.3f" % d_slD)
            law = "LAW_INSUFFICIENT(%s)" % ", ".join(parts)
            rest = ", ".join(parts)
        check("G60-law-adjudication", seeds_ok,
              "SEALED RULE fired: %s -- LAW_LONGRANGE iff Leg A "
              "LONGRANGE; else LAW_SUFFICIENT iff LAGK_MATCH "
              "reproduces chi AND sl_cv2p AND sl_D within the "
              "r303 bands (%.2f / %.2f / %.2f); seeds "
              "collision-free globally %s (%d used, r303 range + "
              "SEED_BASE_K range disjoint)"
              % (law, CHI_BAND, SLP_BAND, SLP_BAND, seeds_ok,
                 len(seeds_used)))
        st["law"] = law
        # ---- the conditional within-block diagnostic
        if law.startswith("LAW_INSUFFICIENT"):
            k0_eff = st["k0_eff"]
            conv_d = 0
            n_d = 0
            ms_d = True
            reps_d = []
            for rep in range(R_REP_D):
                chi_l = []
                cv2p_l = []
                D_l = []
                for ri, rc in enumerate(recs):
                    ev = rc["ev"]
                    seed = SEED_BASE_K + ri * 100 + 6 * 10 + rep
                    seeds_used.add(seed)
                    zb = ev["zb"]
                    T_r, Q_r, _rt = chi_lag_terms(zb, ev["jb"])
                    tT = [(T_r[j] if j < len(T_r) else 0.0)
                          for j in range(k0_eff)]
                    tol_abs = C_TOL * Q_r / 2.0
                    zs, perm, T_b, att, conv = swap_arrange_wb(
                        zb, ev["jb"], tT, seed,
                        min(SWAP_F_K * len(zb), SWAP_CAP_K),
                        tol_abs)
                    n_d += 1
                    conv_d += int(conv)
                    ms_d = ms_d and np.array_equal(
                        np.sort(zs), np.sort(zb))
                    co_s = UTP.coherence_split(
                        ev["xb"], zs, rc["lo"], rc["hi"],
                        ev["brk"], ev["m"])
                    chi_l.append(co_s["chi"])
                    cv2p_l.append(1.0 + co_s["cv2"])
                    D_l.append(co_s["D"])
                reps_d.append(dict(
                    chi=float(np.median(chi_l)),
                    slc=L2D.halves_slope(Ns, cv2p_l),
                    slD=L2D.halves_slope(Ns, D_l)))
            wb = dict(
                chi=float(np.median([r["chi"] for r in reps_d])),
                slc=float(np.median([r["slc"] for r in reps_d])),
                slD=float(np.median([r["slD"] for r in reps_d])))
            conv_share_d = conv_d / max(n_d, 1)
            real = dict(chi=st["chi_med"], slc=st["sl_cv2p_sh"],
                        slD=st["sl_D_sh"])
            wd_chi = abs(wb["chi"] - real["chi"])
            wd_slc = abs(wb["slc"] - real["slc"])
            wd_slD = abs(wb["slD"] - real["slD"])
            wb_repro = (wd_chi <= CHI_BAND and wd_slc <= SLP_BAND
                        and wd_slD <= SLP_BAND)
            if wb_repro:
                named = ("the BLOCK-CONDITIONAL pair placement: "
                         "matching the within-block lag cross "
                         "sums T_1..k0 (chi pinned by algebra, "
                         "F3) also reproduces CV^2 and sl_D -- "
                         "the pair level closes it; the GLOBAL "
                         "lag law alone under-determines the "
                         "within-block terms")
            else:
                named = ("beyond-pair structure: even the "
                         "within-block pair sums do not "
                         "reproduce (%s) -- higher moments / "
                         "triplet placement of the pair "
                         "distribution carry the rest"
                         % ("; ".join(p for p in (
                             "chi %.3f" % wd_chi
                             if wd_chi > CHI_BAND else "",
                             "sl_cv2p %.3f" % wd_slc
                             if wd_slc > SLP_BAND else "",
                             "sl_D %.3f" % wd_slD
                             if wd_slD > SLP_BAND else "")
                             if p)))
            check("G61-insufficiency-diagnostic",
                  conv_share_d >= CONV_MIN_K and ms_d,
                  "WITHINBLOCK_MATCH diagnostic (%d builds, "
                  "T_1..%d targets, F3 disclosed: chi/D pinned "
                  "by construction): convergence %d/%d (share "
                  "%.3f), marginal bitwise %s; chi %.3f sl_cv2p "
                  "%+.3f sl_D %+.3f margin %+.3f -- %s; the "
                  "REST NAMED: %s"
                  % (n_d, k0_eff, conv_d, n_d, conv_share_d,
                     "OK" if ms_d else "BROKEN", wb["chi"],
                     wb["slc"], wb["slD"],
                     st["sigma_star"] - wb["slD"],
                     "REPRODUCES" if wb_repro else "MISSES",
                     named))
            st["named_rest"] = named
            st["wb"] = wb
        else:
            check("G61-insufficiency-diagnostic", True,
                  "skipped by the sealed map (verdict %s): the "
                  "within-block diagnostic runs only on "
                  "LAW_INSUFFICIENT" % st["law"])
            st["named_rest"] = ""
    else:
        check("G60-law-adjudication", True, "SMOKE: skipped")
        check("G61-insufficiency-diagnostic", True,
              "SMOKE: skipped")
        st["law"] = "SMOKE"

    # ---------------- S7: Leg C -- consequence + sign pattern
    section("S7  LEG C: CONSEQUENCE + THE EXACT MINI-TEST")
    if not smoke:
        by_N = sorted(recs, key=lambda r_: r_["N"])[:2]
        med_sgn = [1 if st["med_k"][j] > 0 else -1
                   for j in range(4)]
        fr_note = []
        match_n = []
        for rc in by_N:
            _rl, Sf, _A0f = fr_lag_stats(rc["ev"]["zb"], 4)
            sgs = [1 if s > 0 else (-1 if s < 0 else 0)
                   for s in Sf]
            nm = sum(1 for j in range(4)
                     if sgs[j] == med_sgn[j])
            match_n.append(nm)
            fr_note.append("kz%d (N %d) signs %s (%d/4 match)"
                           % (rc["kz"], rc["N"],
                              "/".join("%+d" % s for s in sgs),
                              nm))
        check("G71-fractions-sign-pattern", True,
              "SIGN_PATTERN (exact mini-test, measured in every "
              "branch): ladder med signs S_1..4 = %s; "
              "Fractions-EXACT on the two smallest rungs: %s -- "
              "exact finite certificates only; whether the "
              "adjacent-pi orthogonality FORCES this pattern "
              "stays OPEN, typed"
              % ("/".join("%+d" % s for s in med_sgn),
                 "; ".join(fr_note)))
        law = st["law"]
        if law == "LAW_SUFFICIENT":
            cons = ("(i) SHORTRANGE_GOAL: derive the short-range "
                    "law (the rho profile up to k0 = %d, net "
                    "covariance <= c < 1) from the three-term "
                    "recursion + the stationary limit "
                    "distribution -- the lane's ONE proof goal; "
                    "the sign-pattern census above is its first "
                    "exact-finite evidence" % (st["k0"] or 0))
        elif law.startswith("LAW_INSUFFICIENT"):
            cons = ("(ii) the short-range law is real but NOT "
                    "the complete mechanism: LAGK_MATCH misses "
                    "%s; the rest is %s; the lane's honest state: "
                    "the mechanism = the measured lag law PLUS "
                    "the named remainder -- no further "
                    "coordinate change counts as progress"
                    % (", ".join(p for p in st["law"]
                                 [len("LAW_INSUFFICIENT("):-1]
                                 .split(", ")),
                       st["named_rest"] or "unnamed"))
        else:
            cons = ("(iii) the reviewer stop case: the lag "
                    "structure is NOT short-range under the "
                    "sealed rule -- the lane closes on this "
                    "route; honest record: L2 <=> "
                    "anti-concentration of an explicit block "
                    "field with LONG-RANGE structure")
        check("G70-consequence-map", True,
              "CONSEQUENCE(%s)" % cons)
        st["cons"] = cons
    else:
        check("G71-fractions-sign-pattern", True,
              "SMOKE: skipped")
        check("G70-consequence-map", True, "SMOKE: skipped")

    # ---------------- S8: worlds + mp wards
    section("S8  WORLD CLASSES + MP WARDS")
    ctl_note = []
    for c in ("EPST", "SCR"):
        ev = crecs[c]["ev"]
        ctl_note.append("%s chi %.2f rho1 %+.2f natom %.0f"
                        % (c, ev["co"]["chi"], ev["rho1"],
                           ev["co"]["natom"]))
    check("G80-world-controls",
          crecs["EPST"]["ev"]["co"]["id_dev"] <= CO_BAR
          and crecs["SCR"]["ev"]["co"]["id_dev"] <= CO_BAR,
          "the coherence identity holds on the live controls by "
          "algebra (world-blind): %s; SMOOTH degenerate "
          "(pre-declared guard); r302/r303 bracket MAIN chi 0.63 "
          "between EPST 0.18 and SCR 1.26 -- reproduced in-table"
          % "; ".join(ctl_note))
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
          "adds: the measured and frozen short-range law of the "
          "dc profile (lag table, truncated net covariance, "
          "summability, exact chi lag decomposition), the lag-k0 "
          "sufficiency test, the graduated reviewer ladder and "
          "the sealed consequence map -- NO new certificate "
          "promoted, NO coordinate change, NO bound modification")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["LAG_PROFILE(med rho_1..4 %s; NC(k0) %.3f "
                 "NC(16) %.3f; SUM %.3f)"
                 % ("/".join("%+.3f" % v
                             for v in st["med_k"][:4]),
                    (1.0 + 2.0 * float(np.sum(
                        st["med_k"][:st["k0"]])))
                    if st["k0"] else float("nan"),
                    st["nc_K"], st["sum_abs"])]
        parts.append(st["law_a"])
        parts.append("CHI_GAP(d c by range: k<=3 %+.3f, 4..8 "
                     "%+.3f, 9..16 %+.3f, >16 %+.3f)"
                     % (float(np.sum(st["d_c"][:3])),
                        float(np.sum(st["d_c"][3:8])),
                        float(np.sum(st["d_c"][8:K_FULL])),
                        st["d_c"][K_FULL]))
        parts.append("LAGK_TABLE(chi %.2f slc %+.3f slD %+.3f "
                     "mrg %+.3f)"
                     % (st["lagk"]["chi"], st["lagk"]["slc"],
                        st["lagk"]["slD"],
                        st["sigma_star"] - st["lagk"]["slD"]))
        parts.append(st["law"])
        parts.append("SLACK_RESPONSE(chi %s; mrg %s)"
                     % ("/".join("%.2f" % c
                                 for c in st["grad_chis"]),
                        "/".join("%+.2f" % m
                                 for m in st["grad_mrgs"])))
        parts.append("SIGN_PATTERN(med %s)"
                     % "/".join("%+d" % (1 if st["med_k"][j] > 0
                                         else -1)
                                for j in range(4)))
        parts.append("CONSEQUENCE(%s)" % st["cons"][:60])
        parts.append("WORLD_NOTE(identity world-blind by "
                     "algebra; EPST/SCR bracket reproduced)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the zero-sum tautology, "
          "the chi lag decomposition, the margin chain and every "
          "Fractions statement (all world-blind, exact-finite); "
          "MEASURED: every med, band, slope, census and family "
          "comparison (42 rungs, seeded replicates); OPEN: the "
          "law beyond the measured 42, its derivation from the "
          "recursion, the cofinal step H5, kz15 beyond r270; NO "
          "RH claim"
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
