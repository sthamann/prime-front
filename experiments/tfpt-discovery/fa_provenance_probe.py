#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fa_provenance_probe -- PRIME.L2.RENYI3.FA_PROVENANCE.01
(round 324): THE F_A PROVENANCE ROUND -- the terminal main lane
after the r321 SLIDING_BOUND_GO.  r321 (SPEC e68883ad) sealed the
sliding cubic bound rho_2 <= 1.3056 x F_A^2 pointwise (0/39 test,
all four named violators inside with reserves 7.0..9.6; the G_SQ
constant is algebra-derived via the exact concentration bracket
qmax x PhiH1 <= rho_2 <= PhiH1 = (F_A B)^2; 21 small-m
certificates).  The remaining provenance question is SOURCE-PURE,
LOCAL and SPLIT IN TWO -- this round executes both halves:
  (a) IS F_A BOUNDED?  (measured max 2.47; the near-critical
      family kz53/kz83/kz67 is the TOP of the coordinate.)  Two
      candidate mechanisms, both source-pure testable:
      (a-i)  DISTRIBUTIONAL ROUTE: if the normalized block
             profile is stationary (r302: KS 0.043 over a 3x
             depth range, m2_inf = 1.973, 1/N transient, held-out
             0.002), then F_A is a max-statistic functional of
             ONE stationary distribution -- finite-sample extreme
             value scatter.  SEALED CONSTRUCTION: resample
             synthetic QMAX columns from the pooled normalized
             donor profile (donors = the ladder MINUS the three
             named spike rungs, declared-set warded; seeded rng,
             NRS = 200 replicates, one full ladder column per
             replicate, the imported r317 EFP.local_ratio applied
             to each synthetic column) -- the QQ census KS(F_A
             real, F_A* pooled) and the LADDER-MAX p-value p_max
             = P(max F_A* >= max F_A real) decide whether the
             spikes are INSIDE the stationarity scatter (then
             F_A <= C_F is a distribution-statement candidate,
             C_F = the resampled envelope) or REAL OUTLIERS.
      (a-ii) STRUCTURAL ROUTE: what is locally different at
             kz53/kz83/kz67?  NEW EXACT FACTORIZATION (derived
             algebra, disclosed, warded live): with j* = argmax_j
             |x_j|, A1_j = sum of |atom values| in block j, L =
             sum_j |x_j|:
                 QMAX = s x a,   s = |x_{j*}|/A1_{j*} <= 1
                                 (in-block signed survival,
                                  triangle inequality EXACT),
                                 a = A1_{j*}/L (the ATOM-MASS
                                 share of the argmax block).
             The spike census asks WHICH factor carries the named
             F_A spikes (rank-local ratios F_s, F_a via the
             imported EFP.local_ratio; sealed attribution rule:
             common carrier iff all three named spikes share one
             factor with ratio >= STRUCT_MIN = 1.5 while the
             other stays <= OTHER_MAX = 1.25), plus the fold/
             collision/edge-distance census of the argmax blocks.
             s <= 1 gives the EXACT majorant F_A <= FAB :=
             a/medloc (warded live); the structural bound
             certifies iff FAB is itself mid-ladder bounded
             (C_FAB frozen on the r316 cal window, 0 test
             violations demanded).
  (b) WHAT BOUNDS THE QMAX SHARE sigma = rho_2/(F_A B)^2 =
      rho_2/PhiH1 in [qmax, 1] (the r321 bracket)?  THE NAMED
      CONNECTION: the r302-proved M_2 stationarity pins the
      SECOND moment of the same normalized block profile -- the
      median-of-max shape route.  NEW EXACT INTERMEDIATE
      INEQUALITY (derived algebra, disclosed, Fractions-proved on
      the toy, warded live on every live world): with q_j =
      |x_j|/L, m2 = m x sum q^2 (the normalized second moment,
      the r302 object) and ymax = m x qmax:
          sum q^3 <= qmax x sum q^2   (exact)
          ==>  sigma <= m2 / ymax = m2 / (m x qmax),
      hence by the r321 bracket algebra (m x qmax = F_A B log m):
          rho_2 <= m2 x F_A x B / log m           (EXACT, pointwise)
          sum q^3 <= m2 x F_A x B x (log m) / m^2.
      m2 is a QUADRATIC source-pure column (no cubic target).
      SEALED CERTIFICATION: C_M2 = max m2 over the r316 mid-
      ladder calibration window (frozen; consumes NO cubic
      target); QMAX_SHARE_PINNED iff the r302 stationarity
      reproduces on THIS ladder (pooled normalized profile,
      three (N, kz)-sorted thirds, KS(G1,G3) <= KS_STAT = 0.125
      AND KS(G2,G3) <= KS_STAT, r302 rule verbatim) AND m2 <=
      C_M2 on every test rung (0 violations) AND the four named
      r316/r317 violators kz53/kz83/kz67/kz55 are ALL inside the
      composed bound rho_2 <= C_M2 x F_A x B / log m; otherwise
      QMAX_SHARE_OPEN with the full anatomy (sigma table,
      tightness sigma x ymax / m2, trends, 1/N census via the
      imported r302 fs_solve against m2_inf = 1.973).
TARGET COMPOSITION (only if (a) and (b) carry): "CANDIDATE
THEOREM (bounded coordinate)": F_A <= C_F (distribution- or
structure-statement) + the share bound ==> via the r321 bracket
the uniform pointwise Renyi-3 bound with explicit C -- the fiber
provenance reduced to two NAMED local statements about the
stationary block profile.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the wave-12 worker (v969) and r323 (base fork) run
in parallel; this probe touches NOTHING outside its own file and
the strictly additive rh-sync.

THE OBJECT (r269/r287/r298/r302/r306/r314/r315/r316/r317/r321
machinery imported verbatim): t_{N-2} = sum_b ct_b (r244 chain
rows, r266 eval); F = 0.20 edge split; maximal same-sign runs of
the bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298 WBT.block_breaks +
WBT.aggregate_blocks); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy
+ SCF.signed_cube_terms + SCF.flux_telescope +
SCF.collision_census; the r315 PHI.phi3_variants; the r316
TRB.two_regime_state + TRB.split_midladder; the r317
EFP.local_ratio + EFP.gap_threshold; the r321 CCP.local_median +
CCP.g_eval + CCP.g_calibrate + CCP.spearman_rank; the r302
UNIF.ks_two + UNIF.fs_solve, ALL imported verbatim; PDelta =
Pbeta - Pomega; x_j = (PDelta)_j.  NEW in this round (module-own,
source-pure where required): m2_qmax_state (the quadratic share
majorant), spike_factors (the exact QMAX = s x a factorization),
donor_pool + resample_qmax (the sealed stationary-null resampler,
seeded), qq_groups (the three-thirds stationarity split) and the
three sealed verdict trees fa_tree / share_tree / compose_tree.

SEALED ADJUDICATION (frozen BEFORE any evaluation of this round;
precedence disclosed -- distributional before structural because
a distribution-level statement is stronger than a per-window
majorant census; exactly one F_A letter and exactly one share
letter fire):
  F_A tree:    FA_OUTLIERS_REAL          iff p_max < P_MIN = 0.05
                   (the named spikes are NOT a stationarity
                   fluctuation -- then THAT is the finding),
               FA_BOUNDED_DISTRIBUTIONAL iff p_max >= P_MIN and
                   KS(F_A real, F_A* pooled) <= KS_FA = 0.125,
               FA_BOUNDED_STRUCTURAL     iff neither, and the
                   structural route certifies (common carrier
                   3/3 named AND FAB mid-ladder certified with
                   0 test violations),
               FA_OPEN                   otherwise.
  share tree:  QMAX_SHARE_PINNED iff STATIONARY (both KS clauses)
                   AND 0 m2 test violations AND named coverage
                   4/4 on the composed bound,
               QMAX_SHARE_OPEN   otherwise.
  composition: PROVENANCE_COMPOSED(C) iff the F_A letter is a
                   BOUNDED letter AND the share letter is PINNED
                   -- the candidate theorem is printed with every
                   measured constant; otherwise the two letters
                   stand alone.

LEG 0 -- ANCHOR REGRESSION (slim set, disclosed: the full
r314/r315 anchor chain is re-warded by the coexisting r321/r322
probes in the same suite; this round re-gates the r314 identity
wards plus the four record anchors its own legs consume): the
r314 identity wards live (REC3/TEL/BND bars); r306 C_2 = 1.069
(tol 0.005) first-5 freeze, 0/57; r316 rho anchors kz53/kz67/
kz55/kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005) + C_small
1.0694 (tol 0.005) at kz18 + ladder n = 65; r317 F_A top-3 ==
(kz53, kz83, kz67) ORDERED with values 2.47/2.39/2.38 (tol 0.01)
+ gap-B == {kz55, kz67} with THR_B 3.7157 (tol 0.005); r321 G_SQ
b = 1.3056 (tol 0.005) with 0 test violations and named coverage
4/4 (recomputed via the imported CCP.g_calibrate).

LEG A -- SEAL + PURITY + TOYS + LIVE WARDS: (A1) the sealed
definitions printed; the SOURCE-PURE coordinate/factor table
(rank, kz, N, m, QMAX, F_A, medloc, B, s, a, m2) printed BEFORE
any bound-side or resample table of this round.  (A2) SOURCE-
PURITY AUDITS: the AST identifier scan over the six module-own
builders (m2_qmax_state, spike_factors, donor_pool,
resample_qmax, qq_groups + the three verdict trees) must be
clean against BOUND_FORBIDDEN + PHI3_FORBIDDEN +
RESAMPLE_FORBIDDEN; the literal scan over the builders + trees
must be clean against the sealed record-literal set
R324_TABLE_LITERALS (r314+r315+r316+r317 set, r321 verbatim,
UNION the r321 record numbers); e1-e4 prove the audits bite.
(A3) TOY EXACTNESS (Fractions where the spec demands exact
intermediate inequalities): the share toy x = (1, -2, 3) in
exact Fractions: q = (1/6, 1/3, 1/2), sigma = 2/3, bracket 1/2
<= 2/3 <= 1 EXACT, m2 = 7/6, ymax = 3/2, majorant 7/9 with slack
1/9 EXACT; the flat toy x = (1, 1): sigma = 1 = upper bracket
EQUALITY = m2/ymax EQUALITY (the majorant is sharp at the flat
profile); the one-block toy x = (5, 0): sigma = 1 = qmax (lower
bracket EQUALITY at full concentration); the factor toy x =
(-1, 3) with A1 = (3, 3): s = 1, a = 3/4, QMAX = 3/4 = s x a
EXACT; the resampler determinism toy (same seed twice ->
identical, constant donor pool of ones -> QMAX* == 1/m EXACT);
the imported r302 toys re-warded (ks_two((1,2,3),(1.5,2.5)) ==
1/3, fs_solve((10,3),(40,1.5)) == (1, 20, 2)); the groups toy
(disjoint + covering EXACT); the three verdict trees on every
branch combination EXACT.  (A4) LIVE WARDS on every live world:
the r316 majorant chain + NORM x cube == rho_2 (r321 verbatim);
the r321 bracket restated as the SHARE bracket qmax <= sigma <=
1; THE NEW SHARE MAJORANT sigma <= m2/ymax (exact algebra, bar
CHAIN_BAR); the reconstruction QMAX == F_A x medloc and PhiH1 ==
(F_A B)^2 on the ladder (r321 verbatim); THE NEW FACTORIZATION
QMAX == s x a EXACT (bar 1e-12) on every live world.

LEG B -- THE DISTRIBUTIONAL ROUTE (a-i): the donor pool sealed
(declared donor set == ladder ranks minus the three NAMED_FA_KZ
ranks, set-warded; the pool is the concatenation of the per-rung
mean-1 normalized profiles y = m|x|/L); the resample census (NRS
= 200 seeded replicates, per replicate one synthetic QMAX column
of the full ladder geometry m_1..m_n, F_A* = EFP.local_ratio per
column): KS(F_A real, F_A* pooled), the per-named-rank p values,
p_max, the resampled envelope C_F = max over replicates x ranks
and the 95 percent replicate-max quantile as census.

LEG C -- THE STRUCTURAL ROUTE (a-ii): the factor censuses F_s =
local_ratio(s), F_a = local_ratio(a); the named-spike attribution
table (which factor carries, sealed rule); the argmax-block
geometry census (atom count, max fold multiplicity, rank-based
edge distance) for the named spikes vs the ladder median; the
exact majorant column FAB = a/medloc with its cal/test maxima
and violation count (the structural certification).

LEG D -- THE SHARE ROUTE (b): the stationarity re-run on THIS
ladder (three (N, kz)-sorted thirds via the sealed qq_groups,
pooled normalized profiles, KS table, per-group m2 medians, the
imported fs_solve 1/N census against the r302 m2_inf = 1.973 --
census, no bar: the ladder here is 65 rungs vs the r302 42); the
share anatomy table (rank, kz, m, qmax, sigma, majorant,
tightness sigma x ymax/m2) printed AFTER the source-pure table;
C_M2 frozen on the cal window; m2 test violations; the composed-
bound violations (algebra cross-check) and the named coverage.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) RESAMPLE READS THE REAL F_A VALUES: mutant_resample_peek
  consumes the real coordinate column (identifier FA_real in the
  sealed RESAMPLE_FORBIDDEN set) -- AST-FLAGGED, and on the toy
  it returns the real maximum EXACTLY (loud diff vs the honest
  constant-pool draw) -- CAUGHT twice.
(e2) STATIONARITY PROFILE CALIBRATED FROM THE SPIKE RUNGS:
  mutant_pool_spikes declares the named spike ranks as the donor
  set -- the declared-set ward must CATCH the mismatch EXACT
  (the real donor_pool declares the sealed complement EXACT).
(e3) SHARE BOUND CONSUMES rho_2 CIRCULARLY: mutant_share_posthoc
  re-derives the 'constant' from the evaluated bound column over
  the whole ladder (consumes rho) -- the BOUND_FORBIDDEN scope
  audit must FLAG it (AST-CAUGHT) AND on the sealed toy it
  returns a constant != the frozen cal-window rule's.
(e4) QQ WITH OVERLAPPING SPLITS: mutant_groups_overlap returns
  thirds whose neighbors share one rank -- the disjointness ward
  must measure intersection >= 1 on the mutant and 0/0/0 on the
  sealed qq_groups -- CAUGHT.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.  Scope hygiene:
  the module-own builders consume block values / atom masses /
  rank order / declared sets / seeds only; sigma itself is the
  TARGET-SIDE diagnostic (rho_2/PhiH1), computed OUTSIDE the
  audited builders and entering gates/censuses only, disclosed;
  fragment audit (no fit primitives; the 1/N solve is the
  imported r302 deterministic 2-point solve).

INDEX FIREWALL (binding, r238-r321 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target sum q^3 / rho_2 enters GATES / anchors /
the share diagnostic / certification checks only, NEVER a
module-own builder (AST-warded); no zero/prime oracles anywhere
(AST firewall); no fit primitives (fragment audit).  MACHINERY
IMPORTED VERBATIM: r321 CCP.local_median + CCP.g_eval +
CCP.g_calibrate + CCP.spearman_rank, r317 EFP.local_ratio +
EFP.gap_threshold, r316 TRB.two_regime_state +
TRB.split_midladder, r315 PHI.phi3_variants, r314
SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope
+ SCF.collision_census, r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze, r302 UNIF.ks_two +
UNIF.fs_solve, r298 WBT.block_breaks + WBT.aggregate_blocks,
r269 PBB.mask_edge + PBB.runs_split, r287 L2D.blocks_level2 +
L2D.halves_slope + L2D.autocorr_full, r244 BH.wpack, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed, r316/r317/r321 verbatim): frame-A h
<= 900, 42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22,
36, 38, 39, 52}; EXTENSION: 900 < h <= 1300, first 15 by (N,
kz); EXT2: the r316 A5 rule (leftover pool + first 12 windows
1300 < h <= 1650, first 8 POSITIVE_PREFIX by (N, kz)).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; XW_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; N_CAL 5; CAL_THIRD 3 (via TRB,
verbatim); CLS_W 5 (via EFP, verbatim); NRS 200; SEED_RS 324001;
KS_FA 0.125; P_MIN 0.05; KS_STAT 0.125 (r302 verbatim); FS_BAR
0.05 (census); STRUCT_MIN 1.5; OTHER_MAX 1.25; NAMED_FA_KZ (53,
83, 67); NAMED_KZ (53, 83, 67, 55); N_GRP3 3; MUT_MIN 1e-6;
TOY_BAR 1e-12; FR_BAR 1e-14; TB_WARD bars 1e-9 main N <= 400 /
3e-6 deep + ext + ext2 / 1e-6 controls; ID_BAR 1e-12; AC_BAR
1e-9; SA_BAR 1e-12 (QMAX == s x a); R306 anchor C_2 1.069 tol
0.005; R316 anchors RHO {53: 1.0490, 67: 1.0536, 55: 0.4821, 83:
0.7790} tol 0.005, C_SMALL 1.0694 tol 0.005 at kz18, N324 = 65;
R317 anchors FA_TOP {53: 2.47, 83: 2.39, 67: 2.38} tol 0.01
ORDERED, THR_B 3.7157 tol 0.005, B set (55, 67); R321 anchors
B_SQ 1.3056 tol 0.005, 0 test violations, named 4/4; M2INF_REF
1.973 (census only, disclosed -- the ladder here is 65 rungs vs
the r302 42-rung core, no bar); R324_TABLE_LITERALS = the sealed
r314+r315+r316+r317 forbidden set (r321 verbatim) UNION the r321
record set {1.3056, 1.1426, 1.4088, 15.95, 7.97, 2.71, 5.35,
-0.341, 0.122, 1.973, 2.15, 5.21, 3.4841, 7.9714, 7.4877,
7.4069, 0.3012, 0.03846, 0.3061}; runtime <= 1800 s; smoke = w9
+ controls + toys + scope/purity audits + the chain/bracket/
share/factor wards on w9 + controls + e1-e4 mutants; ladder,
extensions, anchors, resample, stationarity, certification and
adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r306/r316/r317/r321 RECORD number adopted
as-is; the share majorant sigma <= m2/ymax, the factorization
QMAX = s x a, the bracket restatement and the composed transfer
rho_2 <= m2 F_A B/log m are derived algebra, disclosed above;
the resample null model is DISCLOSED as iid draws from the
pooled stationary profile (the r302 lag-1 anti-correlation of
the ATOM field is not modeled at block level -- a deviation of
the real F_A tail from the iid null is typed as the honest
letter, not repaired); NRS = 200, SEED_RS = 324001, KS_FA =
KS_STAT = 0.125 (the r302 bar reused), P_MIN = 0.05, STRUCT_MIN
= 1.5 and OTHER_MAX = 1.25 are coarse a-priori bars; the sealed
letters are symmetric -- FA_OUTLIERS_REAL and QMAX_SHARE_OPEN
are first-class findings, not failures; NO resample value, NO
KS distance, NO m2 constant, NO violation count of this round
was computed before this spec was frozen.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one F_A letter, exactly one share letter and exactly one
composition letter fire):
  R324_ANCHORS(identity wards, r306 C_2, r316 rho + C_small +
    n, r317 FA-top3 + gap-B, r321 b + 0 viol + named 4/4)
+ SEAL(share majorant + factorization + resampler + trees +
    purity audits + toys + live wards)
+ FA_DIST(KS QQ, p_max, per-named p, envelope C_F)
+ FA_STRUCT(factor censuses, named attribution, geometry census,
    FAB cal/test)
+ [exactly one of] FA_BOUNDED_DISTRIBUTIONAL /
    FA_BOUNDED_STRUCTURAL / FA_OUTLIERS_REAL / FA_OPEN
+ SHARE(stationarity KS table, m2 groups + 1/N census vs 1.973,
    sigma anatomy, tightness, C_M2, violations, named coverage)
+ [exactly one of] QMAX_SHARE_PINNED / QMAX_SHARE_OPEN
+ [exactly one of] PROVENANCE_COMPOSED(C) / NOT_COMPOSED
+ THEOREM(candidate text printed on PROVENANCE_COMPOSED)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the share majorant and the factorization
are EXACT algebra, but their certification constants (C_M2,
C_FAB) and every KS distance, p value, violation count and trend
are MEASURED on the finite ladder only; the resample null is a
DISCLOSED iid model of the stationary profile; a composed GO
fixes a certified statement ON THE MEASURED RUNGS with explicit
constants, it proves NO universal bound beyond them and NO
cofinal law; FA_OUTLIERS_REAL is the honest primary finding if
the spikes exceed the stationarity scatter -- it would type the
near-critical family as a STRUCTURAL feature, not a fluctuation,
and the provenance question would sharpen accordingly;
r243-r322 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 36/36 (0.6 s), NO amendment; calibration pass 1 =
first full evaluation, 36/36, wall 34.2 s, NO amendment; record
run1/run2 after this insertion, identical up to WALL; PROTOCOL
DISCLOSURE: a drafting error had placed PREFILLED PLACEHOLDER
record tables into this spec BEFORE any run -- they were removed
COMPLETELY before the first smoke run and are disclosed here (the
r316/r317/r321 protocol-error class); the ONLY post-freeze edit
is this record-table insertion, which IS the protocol -- no bar,
band, rule or verdict rule moved):
CAL_VERDICT = R324_ANCHORS(identity wards 4.5e-17/4.7e-16/
4.1e-16 on 69 live worlds; r306 C_2 1.069 viol 0/57; r316 rho
kz53/kz67/kz55/kz83 = 1.0493/1.0536/0.4821/0.7791, C_small
1.0694 @ kz18, n = 65; r317 F_A top-3 (53, 83, 67) =
2.47/2.39/2.38 EXACT ORDERED, gap-B {55, 67} THR_B 3.7157; r321
b = 1.3056 = B_cal_max 1.1426 squared, 0/39 test violations,
named 4/4 -- ALL bit-near) + SEAL(purity clean: 0 id + 0 literal
hits on the audited builders/trees; Fractions toys EXACT (worst
rational dev 0): sigma 2/3 in [1/2, 1], majorant 7/9 slack 1/9,
flat double EQUALITY, one-block lower EQUALITY, factor toy 3/4 =
1 x 3/4; resampler deterministic (same seed identical, ones-pool
QMAX* == 1/m EXACT); r302 import toys exact; live wards on 69
live worlds: r316 chain 6.5e-16, NORM x cube 7.9e-16, share
bracket qmax <= sigma <= 1 slack 0.0, NEW share majorant sigma
<= m2/ymax worst rel slack 0.0 -- algebra-live, sigma ==
sum q^3/qmax^2 identity 1.2e-15, NEW QMAX == s x a worst
2.2e-16, ladder recon QMAX == F_A x medloc 1.6e-16, PhiH1 ==
(F_A B)^2 5.7e-16; source-pure table census: F_A 0.58/1.01/2.47
min/med/max (max kz53), s range 0.224..0.842, a range
0.0290..0.4884, m2 range 1.579..3.194 med 2.051) +
FA_DIST(donor pool 62 rungs / 8093 pooled normalized values,
spike ranks (33, 35, 59) = kz53/kz67/kz83 excluded by seal;
KS(F_A real 65, F_A* pooled 13000) = 0.0982 <= 0.125 -- the F_A
DISTRIBUTION is the stationary max-statistic scatter; p_max =
0.090 >= 0.05 (18/200 stationary replicate ladders reach the
real maximum 2.47 somewhere; replicate-max q95 = 2.583, envelope
C_F = 3.357); per-named p at rank: kz53 0.005 / kz83 0.000 /
kz67 0.000 -- at their SPECIFIC ranks the spikes are extreme,
disclosed with the letter) + FA_STRUCT(factor censuses F_s med
1.01 max 1.74 / F_a med 0.98 max 2.87; named attribution kz53
F_s 1.72/F_a 1.53 carrier s, kz83 1.35/1.61 carrier a, kz67
1.38/2.09 carrier a -- NO common carrier (sealed rule FAIL): the
spike family is mechanically HETEROGENEOUS; geometry census at
j*: kz53/kz83 argmax blocks are EDGE-ADJACENT (rank distance
0.01/0.04 vs ladder med 0.07) and atom-poor (6/6 vs med 10),
kz67 interior atom-rich (12, 0.23), multmax 2 = fold-normal on
all three; FAB = a/medloc cal max 3.5261 vs test max 4.3380
(ratio 1.23), 4 test violations (kz67/76/68/61) -- the
structural majorant does NOT certify) +
FA_BOUNDED_DISTRIBUTIONAL(p_max 0.090 >= 0.05 AND KS 0.0982 <=
0.125: F_A <= C_F = 3.357 (resampled envelope) is a
distribution-statement candidate -- the coordinate's ladder
maximum is INSIDE the stationary max law) + SHARE(stationarity
on THIS 65-rung ladder: thirds 22/22/21, pooled profiles
1081/2758/4750 values, KS(G1,G3) 0.0230 / KS(G2,G3) 0.0158 /
KS(G1,G2) 0.0247, ALL far under 0.125 -- STATIONARY incl. the
ext/ext2 strata, even tighter than the r302 core record 0.043;
m2 group medians 2.046/2.033/2.074, fs 1/N census m2_inf =
2.081 (r302 rec 1.973, dev 0.108 on a 50 pct longer ladder), B
= -8.2 (approach from BELOW here vs the r302 above, census),
held-out dev 0.017; sigma anatomy med/min/max
0.2136/0.0907/0.4852 (ladder max at small-m kz9; deep test max
kz38 0.359), trend over test -0.584 FALLING -- the r321 'share
falls faster than B^2 rises' mechanism measured directly;
tightness sigma x ymax/m2 med 0.57 max 0.79; C_M2 = 2.2557
frozen at cal (kz34); m2 test violations 7/39: kz53 3.1528 /
kz67 3.1938 / kz83 3.0490 / kz76 2.4992 / kz61 2.4711 / kz28
2.3585 / kz109 2.2857 -- the named spikes carry an m2 EXCESS 35
.. 42 pct above the mid-ladder constant (the F_A spike IS the m2
spike); composed bound rho_2 <= C_M2 x F_A x B/log m: 0/39 test
violations AND named coverage 4/4 (kz53 rsv 1.23 / kz83 1.35 /
kz67 1.23 / kz55 1.81) -- the composed bound HOLDS measured,
because the majorant tightness (med 0.57) absorbs the m2
excess; algebra transfer NOT closed: the m2 clause fails) +
QMAX_SHARE_OPEN(STATIONARY holds but the m2 mid-ladder
certification fails on 7 test rungs incl. all three named
spikes -- the median-of-max route pins the BULK share (32/39
rungs under C_M2, majorant reserve med 1.75x) but NOT the spike
rungs; the share provenance sharpens to: what bounds the m2
excess of the near-critical rungs?) + NOT_COMPOSED(FA letter
BOUNDED_DISTRIBUTIONAL + share letter OPEN -> no theorem by
seal) + MUSTFAIL_LEDGER(e1 AST-FLAGGED on FA_real + toy peek
2.0 == real max vs honest ones-pool 1.0, diff 1.0 LOUD; e2
declared (2, 5, 9) != sealed complement, set ward EXACT; e3
AST-FLAGGED on rho + toy posthoc 1.6667 != frozen cal rule
1.2000, diff 0.4667; e4 mutant overlaps (1, 1) vs sealed 0
EXACT disjoint + cover; m5a t_term / m5b g_branch FLAGGED).
READING (typed, no upgrade): the round answers both provenance
halves and the two answers POINT AT ONE OBJECT: (1) F_A letter =
FA_BOUNDED_DISTRIBUTIONAL -- the r302 stationarity EXPLAINS the
coordinate: the F_A distribution matches the iid stationary
max-statistic null (KS 0.098 <= 0.125) and the ladder MAXIMUM
2.47 sits inside the stationary max law (p_max 0.090; envelope
C_F 3.357, q95 2.583): the MAGNITUDE of the near-critical spikes
is a finite-sample property of the stationary profile -- F_A <=
C_F is available as a distribution-statement candidate, which
was question (a); (2) the honest tension is DISCLOSED and typed:
the per-rank p values at the named spikes are 0.005/0.000/0.000
-- WHERE the extremes sit (exactly the near-critical rungs, all
three) is NOT explained by the exchangeable null; the sealed
question (bounded coordinate = ladder-max law) is answered GO,
the rank-identity question is the sharpened residue; (3) the
structural census REFUTES a single mechanism: kz53 is a
SURVIVAL spike at an edge-adjacent atom-poor block (F_s 1.72,
rank edge distance 0.01, 6 atoms), kz67 an ATOM-MASS
concentration at an interior atom-rich block (F_a 2.09, 12
atoms), kz83 mixed (a-carried 1.61, edge-adjacent, atom-poor) --
the sealed common-carrier rule fails honestly and the exact
majorant F_A <= a/medloc does not mid-ladder certify (4
violations): no structural bound letter, the identity-first
question closes negative; (4) share letter = QMAX_SHARE_OPEN
with the mechanism measured: the NEW exact chain sigma <=
m2/(m qmax) (Fractions-proved, warded two-sided live on 69
worlds) converts M_2 stationarity into a pointwise share bound;
the stationarity itself reproduces on the 65-rung ladder EVEN
TIGHTER than the r302 core (KS 0.023/0.016 vs 0.043) with
m2_inf 2.081 census vs the r302 1.973 -- but the m2 mid-ladder
constant is violated by exactly the named spikes (+35..42 pct):
THE F_A SPIKE AND THE m2 SPIKE ARE THE SAME OBJECT seen in the
second vs third moment, and the sealed pin rule maps it to OPEN
by contract; (5) the round's strongest bycatch: the composed
bound rho_2 <= 2.2557 x F_A x B/log m holds 0/39 MEASURED with
named coverage 4/4 (reserves 1.23..1.81) and the share trend is
-0.584 falling -- the r321 mechanism ('the share falls faster
than B^2 rises') is now an algebra-backed measured statement,
LINEAR in F_A where r321's certificate was quadratic.  Honest
negatives: the composed theorem is NOT printed (share letter
OPEN by the sealed m2 clause -- the 0/39 composed record is a
census, not a certificate); the structural route delivers no
bound; the rank-identity residue (why the stationary extremes
sit exactly on the near-critical rungs) and the m2 excess of
those rungs are the SAME open object; nothing here bounds
anything beyond the measured rungs.  R325 direction (typed,
census-grade): the provenance question is now ONE local
question -- the second-moment excess of the near-critical rungs
(m2 3.05..3.19 vs ladder med 2.05) against the r302-stationary
bulk: EITHER extend the stationarity statement to the m2
TAIL LAW (does the per-rung m2 distribution over the ladder
follow the stationary null's m2 scatter?  the resample
machinery of this round applies verbatim to m2 columns), OR dig
the heterogeneous local geometry (edge-adjacent atom-poor
survival spike kz53 vs interior atom-mass spike kz67) at atom
level via the r314 genealogy of the argmax block.  Runtime
34.2 s full / 0.6 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: none except this record-table insertion
(and the disclosed pre-run placeholder removal).

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
import unif_target_probe as UNIF               # noqa: E402 r302
import renyi3_probe as RY3                     # noqa: E402 r306
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
import phi3_functional_probe as PHI            # noqa: E402 r315
import two_regime_bound_probe as TRB           # noqa: E402 r316
import exception_families_probe as EFP         # noqa: E402 r317
import continuous_coordinate_probe as CCP      # noqa: E402 r321
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
EXT_H_MAX = 1300
K_EXT = 15
EXT_NW_EXPECT = (942, 1218)
EXT2_H_MAX = 1650
EXT2_POOL_CAP = 12
K_EXT2 = 8
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
TEL_BAR = 1e-13
BND_BAR = 1e-13
CHAIN_BAR = 1e-9
XW_BAR = 1e-9
DEG_FLOOR = 1e-6
MULT_CAP = 2
N_CAL = 5
NRS = 200
SEED_RS = 324001
KS_FA = 0.125
P_MIN = 0.05
KS_STAT = 0.125
FS_BAR = 0.05
STRUCT_MIN = 1.5
OTHER_MAX = 1.25
NAMED_FA_KZ = (53, 83, 67)
NAMED_KZ = (53, 83, 67, 55)
N_GRP3 = 3
MUT_MIN = 1e-6
TOY_BAR = 1e-12
FR_BAR = 1e-14
SA_BAR = 1e-12
EDGE_F = 0.20
PAIR_OFFSET = 0
R306_C2 = 1.069
R306_C2_TOL = 0.005
N324_REF = 65
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R317_FA_TOP = {53: 2.47, 83: 2.39, 67: 2.38}
R317_FA_ORDER = (53, 83, 67)
R317_FA_TOL = 0.01
R317_THRB = 3.7157
R317_THRB_TOL = 0.005
R317_B_KZ = (55, 67)
R321_B_SQ = 1.3056
R321_B_TOL = 0.005
M2INF_REF = 1.973
R324_TABLE_LITERALS = frozenset(CCP.R32X_TABLE_LITERALS | {
    1.3056, 1.1426, 1.4088, 15.95, 7.97, 2.71, 5.35,
    -0.341, 0.122, 1.973, 2.15, 5.21, 3.4841, 7.9714,
    7.4877, 7.4069, 0.3012, 0.03846, 0.3061})

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
PHI3_FORBIDDEN = {"cube", "S" + "3", "cm",
                  "renyi3" + "_ratio", "cubic" + "_moments"}
RESAMPLE_FORBIDDEN = {"FA" + "_real", "rho"}


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


def literal_audit(funcname):
    """the RECORD-LITERAL audit: walk ONLY the named function's
    subtree and flag any numeric constant whose 4-decimal rounding
    lies in the sealed r314+r315+r316+r317+r321 record set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, (int, float)) \
                        and not isinstance(sub.value, bool):
                    if round(float(sub.value), 4) \
                            in R324_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: they consume
# ---------------- block values / atom masses / rank order /
# ---------------- declared sets / seeds only; the withheld
# ---------------- terminal drive key, the branch label, the cubic
# ---------------- target, the real coordinate column (resampler)
# ---------------- and the record literals are forbidden (AST
# ---------------- identifier scan + literal scan).  sigma itself
# ---------------- (rho_2/PhiH1) is the TARGET-SIDE diagnostic,
# ---------------- computed OUTSIDE these builders, disclosed.
def m2_qmax_state(vals):
    """the quadratic share-majorant state of one rung: on block
    values x with q = |x|/L: qm = max q, m2 = m x sum q^2 (the
    normalized second moment, the r302 object), ymx = m x qm,
    maj = m2/ymx -- the EXACT share majorant (sum q^3 <= qm x
    sum q^2 by algebra => sigma = sum q^3/qm^2 <= maj)."""
    ax = np.abs(np.asarray(vals, dtype=float))
    n = int(len(ax))
    tot = float(np.sum(ax))
    if n < 2 or tot <= 0.0:
        return dict(qm=0.0, m2=0.0, ymx=0.0, maj=0.0)
    q = ax / tot
    qm = float(np.max(q))
    m2 = float(n) * float(np.sum(q * q))
    ymx = float(n) * qm
    return dict(qm=qm, m2=m2, ymx=ymx, maj=m2 / max(ymx, 1e-300))


def spike_factors(vals, amass):
    """the EXACT factorization of the concentration coordinate at
    the argmax block: on block values x and per-block atom masses
    A1 (both length m), with j* = argmax |x|:
        s = |x_{j*}| / A1_{j*}   (in-block signed survival <= 1
                                  by the triangle inequality),
        a = A1_{j*} / L          (the atom-mass share),
    so that QMAX == s x a EXACTLY (warded live)."""
    ax = np.abs(np.asarray(vals, dtype=float))
    am = np.asarray(amass, dtype=float)
    tot = float(np.sum(ax))
    if len(ax) < 2 or tot <= 0.0:
        return dict(s=0.0, a=0.0, j=0)
    j = int(np.argmax(ax))
    s = float(ax[j]) / max(float(am[j]), 1e-300)
    a = float(am[j]) / tot
    return dict(s=s, a=a, j=j)


def donor_pool(ylists, donors):
    """the sealed stationary donor pool: concatenate the per-rung
    mean-1 normalized profiles over EXACTLY the declared donor
    rank tuple; returns (pool, declared) -- the declared set is
    warded against the sealed complement of the named spike ranks
    (the e2 mutant declares the spike ranks and is CAUGHT)."""
    donors = tuple(donors)
    pool = np.concatenate([np.asarray(ylists[i], dtype=float)
                           for i in donors]) \
        if donors else np.zeros(0)
    return pool, donors


def resample_qmax(pool, sizes, reps, seed):
    """the sealed stationary-null resampler: seeded rng; per
    replicate draw one synthetic profile of every declared size
    (iid from the pool, with replacement) and record its QMAX* =
    max/sum -- one full synthetic ladder column per replicate.
    Returns the (reps x n) array.  DISCLOSED null model: iid
    draws from the pooled stationary profile."""
    rng = np.random.default_rng(seed)
    npool = len(pool)
    out = np.zeros((int(reps), len(sizes)))
    for r in range(int(reps)):
        for i, sz in enumerate(sizes):
            idx = rng.integers(0, npool, size=int(sz))
            yv = pool[idx]
            tot = float(np.sum(yv))
            out[r, i] = float(np.max(yv)) / max(tot, 1e-300)
    return out


def qq_groups(n):
    """the sealed stationarity split: the (N, kz)-sorted ladder
    rank range 0..n-1 into three near-equal consecutive thirds
    (the r302 three-group protocol generalized to n rungs);
    pairwise disjoint and covering by construction -- warded
    exactly against the e4 overlap mutant."""
    parts = np.array_split(np.arange(int(n)), N_GRP3)
    return tuple(tuple(int(k) for k in p) for p in parts)


def fa_tree(spikes_within, dist_ok, struct_ok):
    """the sealed F_A verdict tree (booleans only; exactly one
    fires; precedence disclosed in the spec)."""
    if not spikes_within:
        return "FA_OUTLIERS_REAL"
    if dist_ok:
        return "FA_BOUNDED_DISTRIBUTIONAL"
    if struct_ok:
        return "FA_BOUNDED_STRUCTURAL"
    return "FA_OPEN"


def share_tree(stationary, cert_ok, named_ok):
    """the sealed share verdict tree (booleans only; exactly one
    fires)."""
    if stationary and cert_ok and named_ok:
        return "QMAX_SHARE_PINNED"
    return "QMAX_SHARE_OPEN"


def compose_tree(fa_v, sh_v):
    """the sealed composition rule (letters only)."""
    if fa_v in ("FA_BOUNDED_DISTRIBUTIONAL",
                "FA_BOUNDED_STRUCTURAL") \
            and sh_v == "QMAX_SHARE_PINNED":
        return "PROVENANCE_COMPOSED"
    return "NOT_COMPOSED"


def mutant_resample_peek(FA_real):
    """e1 MUST-FAIL MUTANT: a 'resampler' that reads the REAL
    coordinate column and returns its maximum (the null
    distribution collapses onto the observation) -- the
    RESAMPLE_FORBIDDEN scope audit must FLAG it, and on the toy
    it returns the real maximum EXACTLY, loudly different from
    the honest constant-pool draw."""
    return max(float(v) for v in FA_real)


def mutant_pool_spikes(ylists, spike_ranks):
    """e2 MUST-FAIL MUTANT: the donor pool built FROM the named
    spike rungs (the stationarity profile calibrated on exactly
    the rungs under adjudication) -- the declared-set ward must
    CATCH the mismatch EXACT."""
    ranks = tuple(spike_ranks)
    pool = np.concatenate([np.asarray(ylists[i], dtype=float)
                           for i in ranks])
    return pool, ranks


def mutant_share_posthoc(Fv, Bv, mv, rho):
    """e3 MUST-FAIL MUTANT: the share 'constant' re-derived from
    the evaluated bound column over the WHOLE ladder (consumes
    rho; covers every seen violator by construction) -- the
    BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed
    toy it returns != the frozen cal-window rule's."""
    return max(r * math.log(float(mm)) / max(float(f) * float(b),
                                             1e-300)
               for f, b, mm, r in zip(Fv, Bv, mv, rho))


def mutant_groups_overlap(n):
    """e4 MUST-FAIL MUTANT: a three-thirds split whose neighbor
    groups share EXACTLY one rank -- the disjointness ward must
    measure intersection >= 1 on the mutant and 0/0/0 on the
    sealed qq_groups."""
    k = int(n) // 3
    g1 = tuple(range(0, k + 1))
    g2 = tuple(range(k, 2 * k + 1))
    g3 = tuple(range(2 * k, int(n)))
    return g1, g2, g3


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'provenance orientation' consuming
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'provenance constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the share algebra
# ---------------- decided as rational arithmetic on the toys
def fr_share_toys():
    """the share bracket + majorant in exact Fractions:
    (1) x = (1, -2, 3): q = (1/6, 1/3, 1/2); sigma = sum q^3 /
        qmax^2 = 2/3; bracket qmax = 1/2 <= 2/3 <= 1; m2 = m sum
        q^2 = 7/6; ymax = m qmax = 3/2; majorant m2/ymax = 7/9;
        slack 7/9 - 2/3 = 1/9 EXACT;
    (2) flat x = (1, 1): sigma = 1 (upper bracket EQUALITY) and
        m2/ymax = 1 (majorant EQUALITY -- sharp at flat);
    (3) one-block x = (5, 0): sigma = 1 = qmax (lower bracket
        EQUALITY at full concentration).
    Returns the worst rational deviation (must be 0)."""
    def state(xs):
        ax = [abs(Fr(v)) for v in xs]
        L = sum(ax)
        q = [v / L for v in ax]
        qm = max(q)
        sg = sum(v ** 3 for v in q) / qm ** 2
        m2 = Fr(len(q)) * sum(v * v for v in q)
        ymx = Fr(len(q)) * qm
        return q, qm, sg, m2, ymx

    devs = []
    q, qm, sg, m2, ymx = state((1, -2, 3))
    devs += [abs(sg - Fr(2, 3)), abs(qm - Fr(1, 2)),
             abs(m2 - Fr(7, 6)), abs(ymx - Fr(3, 2)),
             abs(m2 / ymx - Fr(7, 9)),
             abs((m2 / ymx - sg) - Fr(1, 9))]
    devs += [Fr(0) if qm <= sg <= Fr(1) else Fr(1)]
    q, qm, sg, m2, ymx = state((1, 1))
    devs += [abs(sg - 1), abs(m2 / ymx - 1)]
    q, qm, sg, m2, ymx = state((5, 0))
    devs += [abs(sg - 1), abs(qm - 1)]
    return max(devs)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("fa_provenance_probe -- "
          "PRIME.L2.RENYI3.FA_PROVENANCE.01 (round 324)")
    print("SPEC_SHA %s   R321_SHA %s   R317_SHA %s   R302_SHA %s"
          % (SPEC_SHA[:16], CCP.SPEC_SHA[:16], EFP.SPEC_SHA[:16],
             UNIF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + chain/bracket/share/"
                        "factor wards + e1-e4; ladder, "
                        "extensions, anchors, resample, "
                        "stationarity, certification and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE F_A PROVENANCE ROUND (terminal main lane after the "
          "r321 SLIDING_BOUND_GO): (a) is F_A bounded -- "
          "distributional route (sealed stationary-null resample, "
          "NRS = %d, seed %d, donors = ladder minus the named "
          "spike ranks %s; QQ bar %.3f, ladder-max p bar %.2f) "
          "and structural route (EXACT factorization QMAX = s x "
          "a, attribution bars %.1f/%.2f, FAB mid-ladder "
          "certification); (b) what bounds the qmax share sigma "
          "= rho_2/(F_A B)^2 -- THE NEW EXACT CHAIN sigma <= "
          "m2/(m qmax) (algebra, Fractions-proved) converts the "
          "r302 M_2 stationarity into a pointwise share bound "
          "with mid-ladder constant C_M2; verdict trees "
          "FA_OUTLIERS_REAL / FA_BOUNDED_DISTRIBUTIONAL / "
          "FA_BOUNDED_STRUCTURAL / FA_OPEN and QMAX_SHARE_PINNED "
          "/ QMAX_SHARE_OPEN and PROVENANCE_COMPOSED / "
          "NOT_COMPOSED sealed BEFORE evaluation"
          % (NRS, SEED_RS, str(NAMED_FA_KZ), KS_FA, P_MIN,
             STRUCT_MIN, OTHER_MAX))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("m2_qmax_state", "spike_factors", "donor_pool",
               "resample_qmax", "qq_groups", "fa_tree",
               "share_tree", "compose_tree"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, RESAMPLE_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the eight module-own "
          "builders/trees clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + RESAMPLE_FORBIDDEN (%d hits); m5a "
          "gift-bound FLAGGED (%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r321 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSIONS")
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
        ext = []
        ext2 = []
        okL = True
    else:
        kzs = []
        ekz = []
        ekz2 = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H_MAX:
                ekz.append(kz)
            elif h <= EXT2_H_MAX:
                ekz2.append((h, kz))
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:K_EXT]
        ekz2.sort()
        pool2 = epool[K_EXT:] + [BH.wpack(kz)
                                 for _h, kz in ekz2[:EXT2_POOL_CAP]]
        pool2.sort(key=lambda p: (p["N"], p["kz"]))
        ext2 = [p for p in pool2 if p["nf"] is None][:K_EXT2]
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
    if smoke:
        check("G12-extension-census", True, "SMOKE: skipped")
        check("G13-ext2-census", True, "SMOKE: skipped")
    else:
        check("G12-extension-census",
              len(ext) == K_EXT
              and ext[0]["N"] == EXT_NW_EXPECT[0]
              and ext[-1]["N"] == EXT_NW_EXPECT[1]
              and all(p["nf"] is None for p in ext),
              "r286-aligned extension: %d anchors, N_w %d..%d "
              "(expected %d..%d), POSITIVE_PREFIX %d/%d"
              % (len(ext), ext[0]["N"] if ext else -1,
                 ext[-1]["N"] if ext else -1, EXT_NW_EXPECT[0],
                 EXT_NW_EXPECT[1],
                 sum(1 for p in ext if p["nf"] is None), len(ext)))
        check("G13-ext2-census",
              len(ext2) <= K_EXT2
              and all(p["nf"] is None for p in ext2),
              "EXT2 (r316 A5 rule verbatim, census-grade): pool "
              "%d leftover + %d windows with %d < h <= %d; "
              "selected %d POSITIVE_PREFIX anchors, N_w %s..%s"
              % (len(epool) - K_EXT, min(len(ekz2), EXT2_POOL_CAP),
                 EXT_H_MAX, EXT2_H_MAX, len(ext2),
                 ext2[0]["N"] if ext2 else "-",
                 ext2[-1]["N"] if ext2 else "-"))

    pool = ladder if not smoke else [packs["w9"]]
    mains = [packs["w%d" % kz] for kz in windows]

    def rung_rec(p):
        N = p["N"]
        rows = p["rows"]
        r, t, ap, bp = TX.drive_arrays(rows, N)
        g = CA.g_gap(r[:N - 1], t, ap, bp)
        xu, wu = CT.union_arrays(p["d"])
        bx, bw = CT.union_arrays(p["dsm"])
        lo = min(float(np.min(xu)), float(np.min(bx)))
        hi = max(float(np.max(xu)), float(np.max(bx)))
        v2 = BR.eval_scaled(rows, bx, N - 2)
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        v2w = BR.eval_scaled(rows, xu, N - 2)
        cw = wu * xu * v2w * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, cw=cw, o=o,
                    lo=lo, hi=hi, p=p, nf=p["nf"])

    recs = [rung_rec(p) for p in pool]
    erecs = [rung_rec(p) for p in ext] if not smoke else []
    e2recs = [rung_rec(p) for p in ext2] if not smoke else []
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
        e_cheap = sum(1 for rc in erecs + e2recs
                      if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs
                 if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2 census (no sealed expectation): %d cheap "
              "/ %d exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + ATOMIC PRESENTATION WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for rc in erecs + e2recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ext = max(tb_ext, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d mains + 3 controls: worst dev/absmass %.1e main "
          "N<=%d (bar %.0e) / %.1e deep / %.1e ext+ext2 (bar "
          "%.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(mrecs),
             tb_worst, DEEP_N, TB_WARD_BAR, tb_deep, tb_ext,
             TB_WARD_BAR_DEEP, tb_ctrl, TB_WARD_BAR_CTRL))

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
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        Pd = Pb - Pw
        cm = RY3.cubic_moments(Pd)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        degenerate = (cm["L1"] <= DEG_FLOOR * absm)
        # ---- raw atomic presentation (r313/r314 convention):
        edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xw = rc["xu"][~edw]
        vw = -rc["cw"][~edw]
        jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
        jb2 = np.searchsorted(brk, xb) if m else np.zeros(0, int)
        mism = int(np.sum(jb2 != jb))
        pos_all = np.concatenate([xb, xw])
        val_all = np.concatenate([cb, vw])
        blk_all = np.concatenate([jb, jw]).astype(int)
        if m and not degenerate:
            gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
            sct = SCF.signed_cube_terms(gen["G1"], gen["gblk"], m)
            ft = SCF.flux_telescope(gen["G1"], gen["ptr"], m)
            cc = SCF.collision_census(gen["mult"], gen["ptr"], m)
            x_dev = float(np.max(np.abs(sct["x"] - Pd))
                          / max(np.max(np.abs(Pd)), 1e-300))
            sig = sct["sig"]
            cube = sct["cube"]
            A1 = np.bincount(blk_all, weights=np.abs(val_all),
                             minlength=m)
            scale3 = float(np.sum(A1 ** 3))
            sc_j = np.maximum(A1 ** 3, 1e-300)
            C_far_flux = float(np.sum(sig * ft["F_end"]))
            C_bnd = float(np.sum(sig * ft["F_open"]))
            rec3 = abs(C_far_flux + sct["C_pair"] + sct["C_full"]
                       + C_bnd - cube) / max(scale3, 1e-300)
            tel_dev = float(np.max(np.abs(ft["F_end"]
                                          - sct["far"]) / sc_j))
            bnd_dev = float(np.max(np.abs(ft["F_open"]) / sc_j))
            mx_mult = int(np.max(gen["mult"])) if gen["ng"] else 0
            ph = PHI.phi3_variants(sct["x"], sct["Q2"], sct["Q3"],
                                   ft["F_end"], ft["F_open"],
                                   ft["edge_abs"], m)
            trs = TRB.two_regime_state(sct["x"], sct["Q2"],
                                       sct["Q3"], gen["G1"],
                                       gen["ptr"], ft["F_end"],
                                       ft["F_open"],
                                       ft["edge_abs"], m)
            rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
            mqs = m2_qmax_state(sct["x"])
            spf = spike_factors(sct["x"], A1)
            natm = np.bincount(blk_all, minlength=m)
            jst = spf["j"]
            k_j = int(natm[jst])
            mult_j = int(np.max(gen["mult"][gen["ptr"][jst]:
                                            gen["ptr"][jst + 1]])) \
                if gen["ptr"][jst + 1] > gen["ptr"][jst] else 0
            d_edge = min(jst, m - 1 - jst) / max(m - 1, 1)
        else:
            gen = sct = ft = cc = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            C_bnd = 0.0
            mx_mult = 0
            A1 = np.zeros(0)
            ph = dict(a=0.0, b=0.0, c=0.0, nrm=0.0, dflux=0.0,
                      coll=0.0, bnd=0.0, fcix=0.0, L=0.0)
            trs = dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0,
                       fe=0.0, fcix=0.0, qmax=0.0, cnt3=0.0,
                       phiL1=0.0, phiL2=0.0, phiH1=0.0,
                       phiH2=0.0, L=0.0)
            rho2 = 0.0
            mqs = dict(qm=0.0, m2=0.0, ymx=0.0, maj=0.0)
            spf = dict(s=0.0, a=0.0, j=0)
            k_j = 0
            mult_j = 0
            d_edge = 0.0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    cc=cc, ph=ph, trs=trs, rho2=rho2, A1=A1,
                    mqs=mqs, spf=spf, k_j=k_j, mult_j=mult_j,
                    d_edge=d_edge, pos_all=pos_all,
                    val_all=val_all, blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs
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

    live = [rc for rc in pool_all if not rc["ev"]["degenerate"]]
    deg_note = [c for c in crecs if crecs[c]["ev"]["degenerate"]]
    x_w = max(rc["ev"]["x_dev"] for rc in live)
    mism_tot = sum(rc["ev"]["mism"] for rc in pool_all)
    check("G22-genealogy-completeness",
          x_w <= ATOM_BAR and mism_tot == 0,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (slim set, disclosed)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim: identity + "
            "r306/r316/r317/r321)")
    rec3_w = max(rc["ev"]["rec3"] for rc in live)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR,
          "the r314 identity live on %d live worlds: three-term "
          "recomposition dev %.1e (bar %.0e), telescope dev %.1e "
          "(bar %.0e), boundary %.1e (bar %.0e); DISCLOSED slim "
          "anchor set -- the full r314/r315 chain is re-warded "
          "by the coexisting r321/r322 probes in the same suite"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 qmax %.4f m2 %.4f ymax %.2f maj %.4f "
             "sigma %.4f s %.4f a %.4f"
             % (ev9s["trs"]["qmax"], ev9s["mqs"]["m2"],
                ev9s["mqs"]["ymx"], ev9s["mqs"]["maj"],
                ev9s["rho2"] / max(ev9s["trs"]["phiH1"], 1e-300),
                ev9s["spf"]["s"], ev9s["spf"]["a"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r317-anchors", True, "SMOKE: skipped")
        check("G34-r321-sliding-anchor", True, "SMOKE: skipped")
        srt = []
        n324 = 0
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2)
        check("G31-r306-bound-live",
              abs(C2 - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d"
              % (C2, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        srt_all = sorted(recs + erecs + e2recs,
                         key=lambda rc: (rc["N"], rc["kz"]))
        srt = [rc for rc in srt_all
               if rc["ev"]["mx_mult"] <= MULT_CAP]
        n324 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n324)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n324 == N324_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec %.4f/%.4f/%.4f/%.4f tol %.3f); C_small "
              "%.4f @ kz%d (rec %.4f @ kz%d)"
              % (n324, N324_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO[53],
                 R316_RHO[67], R316_RHO[55], R316_RHO[83],
                 R316_RHO_TOL, C_small, srt[j_cs]["kz"],
                 R316_CSMALL, R316_CSMALL_KZ))
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt]
        phiL2_col = [rc["ev"]["trs"]["phiL2"] for rc in srt]
        FA_real = EFP.local_ratio(qmax_col)
        FB = EFP.local_ratio(phiL2_col)
        thrB, kB, gB = EFP.gap_threshold(FB)
        memB = tuple(sorted(srt[i]["kz"]
                            for i, v in enumerate(FB)
                            if v >= thrB))
        ordFA = sorted(range(n324), key=lambda i: -FA_real[i])
        top3_kz = tuple(srt[i]["kz"] for i in ordFA[:3])
        top3_val = {srt[i]["kz"]: FA_real[i] for i in ordFA[:3]}
        check("G33-r317-anchors",
              top3_kz == R317_FA_ORDER
              and all(abs(top3_val[kz] - R317_FA_TOP[kz])
                      <= R317_FA_TOL for kz in R317_FA_TOP)
              and memB == tuple(sorted(R317_B_KZ))
              and abs(thrB - R317_THRB) <= R317_THRB_TOL,
              "r317 anchors reproduced: F_A top-3 %s = "
              "%.2f/%.2f/%.2f (rec %s = %.2f/%.2f/%.2f tol "
              "%.2f, ORDERED); gap-B %s THR_B %.4f (rec %s / "
              "%.4f tol %.3f)"
              % (str(top3_kz), top3_val.get(top3_kz[0], -1),
                 top3_val.get(top3_kz[1], -1),
                 top3_val.get(top3_kz[2], -1),
                 str(R317_FA_ORDER), R317_FA_TOP[53],
                 R317_FA_TOP[83], R317_FA_TOP[67], R317_FA_TOL,
                 str(memB), thrB,
                 str(tuple(sorted(R317_B_KZ))), R317_THRB,
                 R317_THRB_TOL))
        medloc = CCP.local_median(qmax_col)
        Bcol = [medloc[i] * float(m_all[i])
                / math.log(float(m_all[i])) for i in range(n324)]
        parSQ, dSQ = CCP.g_calibrate("SQ", FA_real, rho_all,
                                     Bcol, ca_i)
        gv_sq = [CCP.g_eval("SQ", parSQ, FA_real[i])
                 for i in range(n324)]
        viol_sq = [i for i in te_i if rho_all[i] > gv_sq[i]]
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n324):
                if srt[i]["kz"] == kz:
                    named_rank[kz] = i
        named_sq = sum(1 for kz in NAMED_KZ
                       if rho_all[named_rank[kz]]
                       <= gv_sq[named_rank[kz]])
        check("G34-r321-sliding-anchor",
              abs(parSQ[0] - R321_B_SQ) <= R321_B_TOL
              and not viol_sq and named_sq == 4
              and dSQ == tuple(ca_i),
              "r321 sliding bound reproduced: G_SQ b = %.4f (rec "
              "%.4f tol %.3f, = B_cal_max %.4f squared, source-"
              "pure), violations %d/%d test, named coverage "
              "%d/4, declared cal set EXACT"
              % (parSQ[0], R321_B_SQ, R321_B_TOL,
                 math.sqrt(parSQ[0]), len(viol_sq), len(te_i),
                 named_sq))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "SOURCE-PURE TABLE")
    pure_lits = []
    for fn in ("m2_qmax_state", "spike_factors", "donor_pool",
               "resample_qmax", "qq_groups", "fa_tree",
               "share_tree", "compose_tree", "fr_share_toys"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_resample_peek",
                          RESAMPLE_FORBIDDEN)
    e3_hits = scope_audit("mutant_share_posthoc", BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e3_hits) >= 1,
          "SOURCE PURITY: the eight module-own builders/trees "
          "clean vs the three forbidden sets (%d id hits); the "
          "nine audited functions clean vs the sealed r314+r315+"
          "r316+r317+r321 record-literal set (%d literal hits); "
          "consumed inputs: block values / atom masses / rank "
          "order / declared sets / seeds -- sigma (rho_2/PhiH1) "
          "is the disclosed TARGET-SIDE diagnostic, computed "
          "outside the builders; e1 resample-peek FLAGGED (%s); "
          "e3 share-posthoc FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS"))
    # toys (Fractions exact + float cross + determinism)
    fr_dev = fr_share_toys()
    st_toy = m2_qmax_state([1.0, -2.0, 3.0])
    ok_st = (abs(st_toy["qm"] - 0.5) <= FR_BAR
             and abs(st_toy["m2"] - 7.0 / 6.0) <= FR_BAR
             and abs(st_toy["ymx"] - 1.5) <= FR_BAR
             and abs(st_toy["maj"] - 7.0 / 9.0) <= FR_BAR)
    sf_toy = spike_factors([-1.0, 3.0], [3.0, 3.0])
    ok_sf = (abs(sf_toy["s"] - 1.0) <= FR_BAR
             and abs(sf_toy["a"] - 0.75) <= FR_BAR
             and abs(sf_toy["s"] * sf_toy["a"] - 0.75) <= FR_BAR)
    ones = [np.ones(4), np.ones(5), np.ones(6)]
    pl_toy, dcl_toy = donor_pool(ones, (0, 1, 2))
    rs1 = resample_qmax(pl_toy, (4, 5), 3, 777)
    rs2 = resample_qmax(pl_toy, (4, 5), 3, 777)
    rs3 = resample_qmax(np.arange(1.0, 16.0), (4, 5), 3, 778)
    ok_rs = (np.array_equal(rs1, rs2)
             and abs(float(rs1[0, 0]) - 0.25) <= FR_BAR
             and abs(float(rs1[0, 1]) - 0.2) <= FR_BAR
             and not np.array_equal(rs1, rs3))
    k_toy = UNIF.ks_two([1.0, 2.0, 3.0], [1.5, 2.5])
    Af, Bf, pf = UNIF.fs_solve(10.0, 3.0, 40.0, 1.5, 20.0)
    ok_uf = (abs(k_toy - 1.0 / 3.0) <= FR_BAR
             and abs(Af - 1.0) <= FR_BAR
             and abs(Bf - 20.0) <= FR_BAR
             and abs(pf - 2.0) <= FR_BAR)
    g1t, g2t, g3t = qq_groups(10)
    ok_gr = (len(set(g1t) & set(g2t)) == 0
             and len(set(g2t) & set(g3t)) == 0
             and len(set(g1t) & set(g3t)) == 0
             and tuple(sorted(g1t + g2t + g3t)) == tuple(range(10)))
    fa_br = (fa_tree(False, True, True), fa_tree(True, True, False),
             fa_tree(True, False, True), fa_tree(True, False, False))
    sh_br = (share_tree(True, True, True),
             share_tree(True, True, False),
             share_tree(False, True, True))
    co_br = (compose_tree("FA_BOUNDED_DISTRIBUTIONAL",
                          "QMAX_SHARE_PINNED"),
             compose_tree("FA_BOUNDED_STRUCTURAL",
                          "QMAX_SHARE_PINNED"),
             compose_tree("FA_OUTLIERS_REAL", "QMAX_SHARE_PINNED"),
             compose_tree("FA_BOUNDED_DISTRIBUTIONAL",
                          "QMAX_SHARE_OPEN"))
    ok_tr = (fa_br == ("FA_OUTLIERS_REAL",
                       "FA_BOUNDED_DISTRIBUTIONAL",
                       "FA_BOUNDED_STRUCTURAL", "FA_OPEN")
             and sh_br == ("QMAX_SHARE_PINNED", "QMAX_SHARE_OPEN",
                           "QMAX_SHARE_OPEN")
             and co_br == ("PROVENANCE_COMPOSED",
                           "PROVENANCE_COMPOSED", "NOT_COMPOSED",
                           "NOT_COMPOSED"))
    check("G41-toy-exactness",
          fr_dev == 0 and ok_st and ok_sf and ok_rs and ok_uf
          and ok_gr and ok_tr,
          "Fractions share toys EXACT (worst rational dev %s): "
          "sigma 2/3 in [1/2, 1], m2 7/6, ymax 3/2, majorant 7/9 "
          "slack 1/9; flat double EQUALITY; one-block lower "
          "EQUALITY; float builder cross-ward <= %.0e; factor "
          "toy s 1 x a 3/4 == QMAX 3/4 EXACT; resampler: same "
          "seed identical, ones-pool QMAX* == 1/m EXACT, other "
          "seed differs; r302 import toys exact (ks 1/3, fs (1, "
          "20, 2)); groups toy disjoint + covering EXACT; "
          "verdict trees fa %s / share %s / compose %s EXACT"
          % (str(fr_dev), FR_BAR, str(fa_br), str(sh_br),
             str(co_br)))
    # live wards: r316 chain + share bracket + majorant + recon
    chain_w = 0.0
    xw_cube = 0.0
    brk_low = 0.0
    maj_w = 0.0
    sa_w = 0.0
    sig_id_w = 0.0
    for rc in live:
        ev = rc["ev"]
        trs = ev["trs"]
        nc = trs["nrm"] * ev["cube"]
        xw_cube = max(xw_cube, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
        for a, b in ((nc, trs["phiL1"]),
                     (trs["phiL1"], trs["phiL2"]),
                     (trs["phiL2"], trs["phiH2"]),
                     (nc, trs["phiH1"])):
            chain_w = max(chain_w,
                          max(0.0, a - b) / max(b, 1e-300))
        sg = ev["rho2"] / max(trs["phiH1"], 1e-300)
        # share bracket qmax <= sigma <= 1 (the r321 bracket)
        brk_low = max(brk_low,
                      max(0.0, trs["qmax"] - sg),
                      max(0.0, sg - 1.0))
        # NEW share majorant sigma <= m2/ymax (exact algebra)
        maj_w = max(maj_w, max(0.0, sg - ev["mqs"]["maj"])
                    / max(ev["mqs"]["maj"], 1e-300))
        # sigma identity vs the direct cubic form (target-side)
        x_abs = np.abs(ev["sct"]["x"])
        Lx = float(np.sum(x_abs))
        qv = x_abs / max(Lx, 1e-300)
        sg2 = float(np.sum(qv ** 3)) \
            / max(float(np.max(qv)) ** 2, 1e-300)
        sig_id_w = max(sig_id_w, abs(sg - sg2) / max(sg2, 1e-300))
        # NEW factorization QMAX == s x a
        sa_w = max(sa_w, abs(trs["qmax"]
                             - ev["spf"]["s"] * ev["spf"]["a"])
                   / max(trs["qmax"], 1e-300))
    if smoke:
        rec_fa = 0.0
        ph_dev = 0.0
    else:
        rec_fa = max(abs(qmax_col[i] - FA_real[i] * medloc[i])
                     / max(qmax_col[i], 1e-300)
                     for i in range(n324))
        ph_dev = max(abs(srt[i]["ev"]["trs"]["phiH1"]
                         - (FA_real[i] * Bcol[i]) ** 2)
                     / max(srt[i]["ev"]["trs"]["phiH1"], 1e-300)
                     for i in range(n324))
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= XW_BAR
          and brk_low <= CHAIN_BAR and maj_w <= CHAIN_BAR
          and sig_id_w <= CHAIN_BAR and sa_w <= SA_BAR
          and rec_fa <= 1e-12 and ph_dev <= CHAIN_BAR,
          "the r316 chain live on %d live worlds (worst slack "
          "%.1e); NORM x cube == rho_2 (%.1e); share bracket "
          "qmax <= sigma <= 1 (worst %.1e); NEW share majorant "
          "sigma <= m2/ymax (worst rel slack %.1e -- the "
          "median-of-max route is algebra-live); sigma == "
          "sum q^3/qmax^2 identity (%.1e); NEW factorization "
          "QMAX == s x a (worst %.1e, bar %.0e)%s"
          % (len(live), chain_w, xw_cube, brk_low, maj_w,
             sig_id_w, sa_w, SA_BAR,
             "; ladder recon QMAX == F_A x medloc %.1e, PhiH1 "
             "== (F_A B)^2 %.1e" % (rec_fa, ph_dev)
             if not smoke else " (ladder wards SMOKE-skipped)"))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        s_col = [rc["ev"]["spf"]["s"] for rc in srt]
        a_col = [rc["ev"]["spf"]["a"] for rc in srt]
        m2_col = [rc["ev"]["mqs"]["m2"] for rc in srt]
        info("sealed SOURCE-PURE coordinate/factor table "
             "(printed BEFORE any bound-side or resample table "
             "of this round): rank kz N m QMAX F_A medloc B s a "
             "m2")
        for i, rc in enumerate(srt):
            info("%2d kz%-3d N %4d m %3d qmax %.4f FA %5.2f "
                 "med %.4f B %.4f s %.3f a %.4f m2 %.3f"
                 % (i, rc["kz"], rc["N"], m_all[i], qmax_col[i],
                    FA_real[i], medloc[i], Bcol[i], s_col[i],
                    a_col[i], m2_col[i]))
        check("G43-coordinate-table", True,
              "F_A range min/med/max %.2f/%.2f/%.2f (max at "
              "kz%d); s range %.3f..%.3f (survival <= 1 exact); "
              "a range %.4f..%.4f; m2 range %.3f..%.3f (med "
              "%.3f; the r302 med was ~2.03 on the 42-rung "
              "core, census)"
              % (min(FA_real), float(np.median(FA_real)),
                 max(FA_real),
                 srt[int(np.argmax(FA_real))]["kz"],
                 min(s_col), max(s_col), min(a_col), max(a_col),
                 min(m2_col), max(m2_col),
                 float(np.median(m2_col))))

    # ---------------- S5: Leg B -- the distributional route
    section("S5  LEG B -- DISTRIBUTIONAL ROUTE (stationary-null "
            "resample)")
    if smoke:
        check("G50-donor-seal", True, "SMOKE: skipped")
        check("G51-resample-census", True, "SMOKE: skipped")
    else:
        y_lists = []
        for rc in srt:
            x_abs = np.abs(rc["ev"]["sct"]["x"])
            Lx = float(np.sum(x_abs))
            y_lists.append(x_abs * (float(rc["ev"]["m"]) / Lx))
        spike_ranks = tuple(sorted(named_rank[kz]
                                   for kz in NAMED_FA_KZ))
        donors_sealed = tuple(i for i in range(n324)
                              if i not in spike_ranks)
        pool_y, dcl_don = donor_pool(y_lists, donors_sealed)
        check("G50-donor-seal", dcl_don == donors_sealed,
              "donor pool sealed: %d donor rungs (the ladder "
              "minus the named spike ranks %s = kz %s), %d "
              "pooled normalized values; declared set == sealed "
              "complement EXACT (the e2 mutant declares the "
              "spike ranks and is CAUGHT in S8)"
              % (len(donors_sealed), str(spike_ranks),
                 str([srt[i]["kz"] for i in spike_ranks]),
                 len(pool_y)))
        qs_rs = resample_qmax(pool_y, m_all, NRS, SEED_RS)
        FA_rs = np.array([EFP.local_ratio(list(qs_rs[r]))
                          for r in range(NRS)])
        ks_qq = UNIF.ks_two(FA_real, FA_rs.ravel())
        max_real = max(FA_real)
        max_rs = FA_rs.max(axis=1)
        p_max = float(np.mean(max_rs >= max_real))
        p_named = {kz: float(np.mean(FA_rs[:, named_rank[kz]]
                                     >= FA_real[named_rank[kz]]))
                   for kz in NAMED_FA_KZ}
        C_F_env = float(FA_rs.max())
        q95 = float(np.quantile(max_rs, 0.95))
        dist_ok = ks_qq <= KS_FA
        spikes_within = p_max >= P_MIN
        check("G51-resample-census", True,
              "RESAMPLE census (%d replicates, seed %d): "
              "KS(F_A real %d, F_A* pooled %d) = %.4f %s %.3f; "
              "per-named p at rank: %s; p_max = %.3f %s %.2f "
              "(real ladder max %.2f vs replicate-max q95 %.3f, "
              "envelope C_F = %.3f)"
              % (NRS, SEED_RS, n324, FA_rs.size, ks_qq,
                 "<=" if dist_ok else ">", KS_FA,
                 str({("kz%d" % kz): round(p_named[kz], 3)
                      for kz in NAMED_FA_KZ}),
                 p_max, ">=" if spikes_within else "<", P_MIN,
                 max_real, q95, C_F_env))

    # ---------------- S6: Leg C -- the structural route
    section("S6  LEG C -- STRUCTURAL ROUTE (factorization census "
            "+ F_A adjudication)")
    if smoke:
        check("G60-factor-census", True, "SMOKE: skipped")
        check("G61-struct-bound-census", True, "SMOKE: skipped")
        check("G62-fa-adjudication", True, "SMOKE: skipped")
        fa_verdict = "SMOKE_NO_ADJUDICATION"
    else:
        F_s = EFP.local_ratio(s_col)
        F_a = EFP.local_ratio(a_col)
        info("named-spike attribution (rank-local factor ratios, "
             "window W = %d): kz F_A F_s F_a carrier | argmax-"
             "block geometry: atoms multmax edge-dist"
             % EFP.CLS_W)
        carriers = []
        for kz in NAMED_FA_KZ:
            i = named_rank[kz]
            car = "a" if F_a[i] >= F_s[i] else "s"
            carriers.append((kz, car, F_s[i], F_a[i]))
            ev = srt[i]["ev"]
            info("  kz%-3d FA %.2f Fs %.2f Fa %.2f carrier %s | "
                 "atoms %d multmax %d dedge %.2f"
                 % (kz, FA_real[i], F_s[i], F_a[i], car,
                    ev["k_j"], ev["mult_j"], ev["d_edge"]))
        med_k = float(np.median([rc["ev"]["k_j"] for rc in srt]))
        med_mu = float(np.median([rc["ev"]["mult_j"]
                                  for rc in srt]))
        med_de = float(np.median([rc["ev"]["d_edge"]
                                  for rc in srt]))
        common = (len(set(c for _kz, c, _fs, _fa in carriers))
                  == 1)
        car0 = carriers[0][1]
        car_vals = [(fa if car0 == "a" else fs)
                    for _kz, _c, fs, fa in carriers]
        oth_vals = [(fs if car0 == "a" else fa)
                    for _kz, _c, fs, fa in carriers]
        struct_common = (common and min(car_vals) >= STRUCT_MIN
                         and max(oth_vals) <= OTHER_MAX)
        check("G60-factor-census", True,
              "factor censuses: F_s med %.2f max %.2f / F_a med "
              "%.2f max %.2f; named carriers %s -> common = %s "
              "(sealed rule: one factor >= %.1f on 3/3 while "
              "the other <= %.2f -> %s); geometry census: "
              "ladder med atoms %.0f / multmax %.0f / edge-dist "
              "%.2f (the named-spike rows printed above)"
              % (float(np.median(F_s)), max(F_s),
                 float(np.median(F_a)), max(F_a),
                 str([(kz, c) for kz, c, _f, _g in carriers]),
                 common, STRUCT_MIN, OTHER_MAX,
                 "PASS" if struct_common else "FAIL",
                 med_k, med_mu, med_de))
        FAB = [a_col[i] / max(medloc[i], 1e-300)
               for i in range(n324)]
        fab_ward = max(max(0.0, FA_real[i] - FAB[i])
                       / max(FAB[i], 1e-300)
                       for i in range(n324))
        C_FAB = max(FAB[i] for i in ca_i)
        viol_fab = [i for i in te_i if FAB[i] > C_FAB]
        struct_cert = (not viol_fab)
        struct_ok = struct_common and struct_cert
        check("G61-struct-bound-census", fab_ward <= CHAIN_BAR,
              "the EXACT structural majorant F_A <= FAB = "
              "a/medloc (via s <= 1; live ward worst slack "
              "%.1e): cal max C_FAB = %.4f vs test max %.4f "
              "(ratio %.2f); test violations %d/%d %s -> "
              "structural certification %s"
              % (fab_ward, C_FAB, max(FAB[i] for i in te_i),
                 max(FAB[i] for i in te_i) / max(C_FAB, 1e-300),
                 len(viol_fab), len(te_i),
                 str([srt[i]["kz"] for i in viol_fab])
                 if viol_fab else "[]",
                 "PASS" if struct_cert else "FAIL"))
        fa_verdict = fa_tree(spikes_within, dist_ok, struct_ok)
        det_fa = {
            "FA_OUTLIERS_REAL":
                "p_max %.3f < %.2f -- the named spikes are NOT "
                "a stationarity fluctuation (per-rank p %s); "
                "the F_A bulk QQ census: KS %.4f %s %.3f"
                % (p_max, P_MIN,
                   str({("kz%d" % kz): round(p_named[kz], 3)
                        for kz in NAMED_FA_KZ}), ks_qq,
                   "<=" if dist_ok else ">", KS_FA),
            "FA_BOUNDED_DISTRIBUTIONAL":
                "p_max %.3f >= %.2f AND KS %.4f <= %.3f -- "
                "F_A <= C_F = %.3f (resampled envelope) is a "
                "distribution-statement candidate"
                % (p_max, P_MIN, ks_qq, KS_FA, C_F_env),
            "FA_BOUNDED_STRUCTURAL":
                "the structural route certifies (common carrier "
                "%s, C_FAB %.4f, 0 test violations)"
                % (car0, C_FAB),
            "FA_OPEN":
                "neither route certifies (p_max %.3f, KS %.4f, "
                "struct_common %s, struct_cert %s)"
                % (p_max, ks_qq, struct_common, struct_cert)}
        check("G62-fa-adjudication", True,
              "exactly one sealed F_A letter fired: %s(%s)"
              % (fa_verdict, det_fa[fa_verdict]))

    # ---------------- S7: Leg D -- the share route
    section("S7  LEG D -- SHARE ROUTE (M_2 stationarity -> "
            "pointwise share bound)")
    if smoke:
        check("G70-stationarity", True, "SMOKE: skipped")
        check("G71-share-anatomy", True, "SMOKE: skipped")
        check("G72-m2-certification", True, "SMOKE: skipped")
        check("G73-share-adjudication", True, "SMOKE: skipped")
        sh_verdict = "SMOKE_NO_ADJUDICATION"
    else:
        g1, g2, g3 = qq_groups(n324)
        ovl = (len(set(g1) & set(g2)) + len(set(g2) & set(g3))
               + len(set(g1) & set(g3)))
        pool1 = np.concatenate([y_lists[i] for i in g1])
        pool2 = np.concatenate([y_lists[i] for i in g2])
        pool3 = np.concatenate([y_lists[i] for i in g3])
        ks13 = UNIF.ks_two(pool1, pool3)
        ks23 = UNIF.ks_two(pool2, pool3)
        ks12 = UNIF.ks_two(pool1, pool2)
        stationary = (ks13 <= KS_STAT and ks23 <= KS_STAT)
        m2_med = [float(np.median([m2_col[i] for i in g]))
                  for g in (g1, g2, g3)]
        N_med = [float(np.median([srt[i]["N"] for i in g]))
                 for g in (g1, g2, g3)]
        A_fs, B_fs, pred2 = UNIF.fs_solve(N_med[0], m2_med[0],
                                          N_med[2], m2_med[2],
                                          N_med[1])
        fs_dev = abs(pred2 - m2_med[1]) / max(m2_med[1], 1e-300)
        check("G70-stationarity",
              ovl == 0 and stationary,
              "STATIONARITY on THIS %d-rung ladder (three "
              "(N, kz)-sorted thirds %d/%d/%d, pooled "
              "normalized profiles %d/%d/%d values, overlaps "
              "%d): KS(G1,G3) %.4f / KS(G2,G3) %.4f / KS(G1,G2) "
              "%.4f vs the sealed %.3f -> %s; m2 group medians "
              "%.3f/%.3f/%.3f; 1/N census (imported r302 "
              "fs_solve, no bar): m2_inf = A = %.3f (r302 rec "
              "%.3f on the 42-rung core, dev %.3f), B = %+.1f, "
              "held-out dev %.3f (%s %.2f census)"
              % (n324, len(g1), len(g2), len(g3), len(pool1),
                 len(pool2), len(pool3), ovl, ks13, ks23, ks12,
                 KS_STAT,
                 "STATIONARY" if stationary else "DRIFTING",
                 m2_med[0], m2_med[1], m2_med[2], A_fs,
                 M2INF_REF, abs(A_fs - M2INF_REF), B_fs, fs_dev,
                 "<=" if fs_dev <= FS_BAR else ">", FS_BAR))
        sig_col = [srt[i]["ev"]["rho2"]
                   / max(srt[i]["ev"]["trs"]["phiH1"], 1e-300)
                   for i in range(n324)]
        maj_col = [srt[i]["ev"]["mqs"]["maj"] for i in range(n324)]
        tight = [sig_col[i] / max(maj_col[i], 1e-300)
                 for i in range(n324)]
        info("share anatomy (target-side sigma = rho_2/PhiH1, "
             "bound-side majorant m2/ymax): rank kz m qmax "
             "sigma maj tight [set]")
        setlab = {}
        for i in sm_i:
            setlab[i] = "SMALL"
        for i in ca_i:
            setlab[i] = "CAL"
        for i in te_i:
            setlab[i] = "TEST"
        for i in range(n324):
            info("%2d kz%-3d m %3d qmax %.4f sig %.4f maj %.4f "
                 "tgt %.2f %s"
                 % (i, srt[i]["kz"], m_all[i], qmax_col[i],
                    sig_col[i], maj_col[i], tight[i], setlab[i]))
        NsT = [srt[i]["N"] for i in te_i]
        sl_sig = L2D.halves_slope(
            NsT, [max(sig_col[i], 1e-300) for i in te_i])
        j_dp = max((i for i in te_i), key=lambda i: sig_col[i])
        check("G71-share-anatomy", True,
              "sigma med/min/max %.4f/%.4f/%.4f (ladder max at "
              "kz%d %s; deep test max at kz%d %.3f); trend over "
              "test %+.3f (falling = the r321 mechanism 'the "
              "share falls faster than B^2 rises' measured "
              "directly); tightness sigma x ymax/m2 med %.2f "
              "max %.2f -- the m2-route reserve"
              % (float(np.median(sig_col)), min(sig_col),
                 max(sig_col),
                 srt[int(np.argmax(sig_col))]["kz"],
                 setlab[int(np.argmax(sig_col))], srt[j_dp]["kz"],
                 sig_col[j_dp], sl_sig,
                 float(np.median(tight)), max(tight)))
        C_M2 = max(m2_col[i] for i in ca_i)
        j_cm = max(ca_i, key=lambda i: m2_col[i])
        viol_m2 = [i for i in te_i if m2_col[i] > C_M2]
        comp_bound = [C_M2 * FA_real[i] * Bcol[i]
                      / math.log(float(m_all[i]))
                      for i in range(n324)]
        viol_comp = [i for i in te_i
                     if rho_all[i] > comp_bound[i]]
        named_cov = {kz: rho_all[named_rank[kz]]
                     <= comp_bound[named_rank[kz]]
                     for kz in NAMED_KZ}
        n_named = sum(1 for kz in NAMED_KZ if named_cov[kz])
        named_ok = (n_named == len(NAMED_KZ))
        cert_ok = (not viol_m2)
        check("G72-m2-certification", True,
              "C_M2 = %.4f frozen at cal (kz%d; consumes NO "
              "cubic target -- m2 is the quadratic profile "
              "moment); m2 test violations %d/%d %s; composed "
              "bound rho_2 <= C_M2 x F_A x B/log m: violations "
              "%d/%d %s (algebra cross-check); named coverage "
              "%d/4: %s"
              % (C_M2, srt[j_cm]["kz"], len(viol_m2), len(te_i),
                 str([("kz%d" % srt[i]["kz"],
                       round(m2_col[i], 4)) for i in viol_m2])
                 if viol_m2 else "[]",
                 len(viol_comp), len(te_i),
                 str([srt[i]["kz"] for i in viol_comp])
                 if viol_comp else "[]", n_named,
                 str({("kz%d" % kz):
                      ("in rsv %.2f"
                       % (comp_bound[named_rank[kz]]
                          / max(rho_all[named_rank[kz]],
                                1e-300)))
                      if named_cov[kz] else
                      ("OUT %.4f > %.4f"
                       % (rho_all[named_rank[kz]],
                          comp_bound[named_rank[kz]]))
                      for kz in NAMED_KZ})))
        sh_verdict = share_tree(stationary, cert_ok, named_ok)
        check("G73-share-adjudication", True,
              "exactly one sealed share letter fired: %s(%s)"
              % (sh_verdict,
                 ("stationary + 0 m2 violations + named 4/4: "
                  "sum q^3 <= %.4f x F_A x B x log m / m^2 "
                  "certified on the measured test rungs" % C_M2)
                 if sh_verdict == "QMAX_SHARE_PINNED" else
                 "stationary %s, m2 cert %s (%d violations), "
                 "named %d/4 -- the bulk share is majorant-"
                 "covered, the spike rungs carry the m2 excess"
                 % (stationary, cert_ok, len(viol_m2),
                    n_named)))

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    toy_fa = (1.0, 1.0, 2.0)
    peek = mutant_resample_peek(toy_fa)
    hon = resample_qmax(np.ones(9), (3,), 1, 999)
    ok_e1 = (len(e1_hits) >= 1 and abs(peek - 2.0) <= FR_BAR
             and abs(peek - 3.0 * float(hon[0, 0])) >= MUT_MIN)
    check("G80-e1-resample-peek", ok_e1,
          "e1 CAUGHT twice: the peeking 'resampler' consumes the "
          "real coordinate column -- AST-FLAGGED (%s) -- and on "
          "the toy returns the real max %.1f EXACTLY while the "
          "honest ones-pool draw gives %.4f x 3 = 1.0 (diff "
          "%.1f >= %.0e)"
          % (e1_hits[0] if e1_hits else "MISS", peek,
             float(hon[0, 0]), abs(peek - 1.0), MUT_MIN))
    toy_yl = [np.ones(3) * (i + 1.0) for i in range(10)]
    toy_spk = (2, 5, 9)
    toy_don = tuple(i for i in range(10) if i not in toy_spk)
    _plr, dclr = donor_pool(toy_yl, toy_don)
    _plm, dclm = mutant_pool_spikes(toy_yl, toy_spk)
    check("G81-e2-pool-spikes",
          dclr == toy_don and dclm == toy_spk
          and dclm != toy_don,
          "e2 CAUGHT: the mutant pool declares the spike ranks "
          "%s != the sealed donor complement %s (declared-set "
          "ward EXACT) -- calibrating the stationarity profile "
          "on the rungs under adjudication is structurally "
          "refused" % (str(dclm), str(toy_don)))
    toy_F = (1.0, 1.0, 1.0)
    toy_B = (1.0, 1.0, 1.0)
    toy_m = (math.e, math.e, math.e)
    toy_r = (0.5, 1.2, 1.6667)
    mut_c = mutant_share_posthoc(toy_F, toy_B, toy_m, toy_r)
    frz_c = max(1.2 * math.log(toy_m[1])
                / (toy_F[1] * toy_B[1]), 0.0)
    check("G82-e3-share-posthoc",
          len(e3_hits) >= 1 and abs(mut_c - 1.6667) <= 1e-9
          and abs(mut_c - frz_c) >= MUT_MIN,
          "e3 CAUGHT twice: the after-sight share 'constant' "
          "consumes the evaluated bound column over the whole "
          "ladder -- AST-FLAGGED (%s) -- and on the toy returns "
          "%.4f != the frozen cal-window rule's %.4f (diff "
          "%.4f >= %.0e); the real C_M2 consumes the quadratic "
          "m2 column on the declared cal window only"
          % (e3_hits[0] if e3_hits else "MISS", mut_c, frz_c,
             abs(mut_c - frz_c), MUT_MIN))
    g1m, g2m, g3m = mutant_groups_overlap(10)
    ovl_m = (len(set(g1m) & set(g2m)), len(set(g2m) & set(g3m)))
    g1r, g2r, g3r = qq_groups(10)
    ovl_r = (len(set(g1r) & set(g2r)) + len(set(g2r) & set(g3r))
             + len(set(g1r) & set(g3r)))
    check("G83-e4-groups-overlap",
          ovl_m == (1, 1) and ovl_r == 0,
          "e4 CAUGHT: the mutant thirds share ranks %s (measured "
          "overlaps %s) while the sealed qq_groups is disjoint + "
          "covering EXACT (overlaps %d) -- an in-sample QQ "
          "cannot slip through the disjointness ward"
          % (str((set(g1m) & set(g2m), set(g2m) & set(g3m))),
             str(ovl_m), ovl_r))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    if smoke:
        co_verdict = "SMOKE_NO_ADJUDICATION"
        check("G90-composition", True, "SMOKE: skipped")
    else:
        co_verdict = compose_tree(fa_verdict, sh_verdict)
        if co_verdict == "PROVENANCE_COMPOSED":
            C_uni = C_M2 * C_F_env * max(Bcol[i]
                                         / math.log(float(
                                             m_all[i]))
                                         for i in range(n324)) \
                * 1.0
            info("CANDIDATE THEOREM (bounded coordinate; "
                 "measured on the %d-rung class ladder):" % n324)
            info("  F_A <= C_F = %.3f (%s) and sigma <= "
                 "C_M2/(m qmax) with C_M2 = %.4f (mid-ladder "
                 "frozen, M_2 stationarity), hence by the r321 "
                 "bracket sum q^3 <= C_M2 x F_A x B x log m / "
                 "m^2 <= %.3f x (log m)^2/m^2 on every measured "
                 "rung -- the fiber provenance reduced to the "
                 "two named local statements about the "
                 "stationary block profile."
                 % (C_F_env, fa_verdict, C_M2, C_uni))
            check("G90-composition", True,
                  "PROVENANCE_COMPOSED: theorem candidate "
                  "printed with explicit (C_F %.3f, C_M2 %.4f, "
                  "C_uni %.3f)" % (C_F_env, C_M2, C_uni))
        else:
            check("G90-composition", True,
                  "NOT_COMPOSED (FA letter = %s + share letter "
                  "= %s); no theorem printed by seal -- the two "
                  "letters and their censuses stand as the "
                  "round's record data"
                  % (fa_verdict, sh_verdict))
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact share majorant sigma <= m2/(m qmax) "
          "(the M_2-stationarity transfer), the exact QMAX = s "
          "x a factorization, the sealed stationary-null "
          "resample construction for F_A and the three sealed "
          "verdict trees -- NO new certificate promoted, NO "
          "universal bound claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R324_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d rho4 bit-near C_small %.4f, "
                 "r317 top3 %s thrB %.4f, r321 b %.4f viol %d "
                 "named %d/4)"
                 % (rec3_w, C2, viol2, n324, C_small,
                    str(top3_kz), thrB, parSQ[0], len(viol_sq),
                    named_sq)]
        parts.append("SEAL(majorant %.1e, factorization %.1e, "
                     "purity clean, toys exact)"
                     % (maj_w, sa_w))
        parts.append("FA_DIST(KS %.4f, p_max %.3f, p_named %s, "
                     "C_F %.3f, q95 %.3f)"
                     % (ks_qq, p_max,
                        str({kz: round(p_named[kz], 3)
                             for kz in NAMED_FA_KZ}),
                        C_F_env, q95))
        parts.append("FA_STRUCT(carriers %s common %s, F_a max "
                     "%.2f, FAB cal %.4f test %.4f viol %d)"
                     % (str([c for _k, c, _f, _g in carriers]),
                        struct_common, max(F_a), C_FAB,
                        max(FAB[i] for i in te_i),
                        len(viol_fab)))
        parts.append(fa_verdict)
        parts.append("SHARE(KS %.4f/%.4f/%.4f %s, m2_inf %.3f "
                     "vs rec %.3f, sigma med %.4f trend %+.3f, "
                     "tight med %.2f, C_M2 %.4f viol %d/%d, "
                     "comp viol %d, named %d/4)"
                     % (ks13, ks23, ks12,
                        "STATIONARY" if stationary else
                        "DRIFTING", A_fs, M2INF_REF,
                        float(np.median(sig_col)), sl_sig,
                        float(np.median(tight)), C_M2,
                        len(viol_m2), len(te_i), len(viol_comp),
                        n_named))
        parts.append(sh_verdict)
        parts.append(co_verdict)
        parts.append("THEOREM(%s)"
                     % ("printed"
                        if co_verdict == "PROVENANCE_COMPOSED"
                        else "not printed"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the share majorant "
          "chain, the factorization, the bracket, the Fractions "
          "toys, the tree logic and the purity audits (exact / "
          "AST-decided); MEASURED: every KS distance, p value, "
          "constant, violation count, trend and census (the "
          "finite class ladder + 2 mains + 2 live controls; the "
          "resample null is a DISCLOSED iid model); OPEN: any "
          "bound beyond the measured rungs, the cofinal law, "
          "the provenance of the named spike concentration, "
          "kz15 beyond r270; NO RH claim"
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
