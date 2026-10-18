#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fold_density_dictionary_probe --
PRIME.L2.FOLD_DENSITY_DICTIONARY.01 (round 339): THE DENSITY
MARTINGALE AND THE MOMENT DICTIONARY -- the reviewer's
reformulation of the terminal target.

CONTEXT (binding, from the sealed records r324/r327/r333/r335/
r337): the terminal has so far been routed through a MAXIMUM --
q_max x M_2 replaces a third moment by an L-infinity bound, and
exactly this loss shows in the mid-band (kz73/76/61 + deep
kz95/98/109), where the r335 dichotomy loses a factor 6-10
although no single atom is large enough.  The reviewer
adjudication (verbatim, binding): the new currency is a REVERSE
HOLDER PROBLEM for a canonical martingale weight process on the
fold genealogy.  IMPORTANT verdict-reading rule (reviewer
verbatim): r337 tested the RAW SIGNED fold-mass process inside
the argmax block -- its letter (MARTINGALE_STRUCTURE_ONLY, and a
NOT_A_MARTINGALE would have been equally honest) is IRRELEVANT
here; the density per remaining descendant is a martingale BY
ALGEBRA.  This round is INDEPENDENT of r337.

THE PROCESS (reviewer verbatim): let the canonical fold genealogy
be a tree/forest over the m final atoms a_i = |PDelta_i| (the
level-2 block values).  For every node v: A(v) = sum_{i under v}
a_i, n(v) = #{i under v}, density d(v) = A(v)/n(v).  Draw a final
atom uniformly from the m leaves, V_k = its ancestor at level k
(root = level 0).  Normalized: X_k = d(V_k)/d(root).
THE THEOREM (exact algebra only, no fit):
  E[X_{k+1} | V_k = v]
    = X_k x sum_c (n(c)/n(v)) (A(c)/n(c)) / (A(v)/n(v))
    = X_k x sum_c A(c)/A(v) = X_k
-- X_k is a nonnegative martingale from MASS CONSERVATION alone.
THE MOMENT DICTIONARY (exact): at leaf i, X_inf = a_i/(A/m) =
m q_i, hence E[X_inf^2] = m M_2 and E[X_inf^3] = m^2 M_3.  The
terminal target M_3 <= C (log m)^A / m^2 is EQUIVALENT to
E[X_inf^3] <= C (log m)^A.  The exponent 2 is no fit -- at
uniform mass M_3 = 1/m^2 exactly (the cubic scaling of the
uniform tree).
THE LOCAL ANATOMY: for child c of v: p_c = n(c)/n(v), R_c =
d(c)/d(v); exactly sum_c p_c R_c = 1.  Local cubic inflation
Gamma(v) = sum_c p_c R_c^3, with E[X_{k+1}^3 | V_k = v] =
X_k^3 Gamma(v); at equidistribution Gamma = 1.  The whole
deviation from the optimal law is the accumulated local density
inflation.
THE DRIFT CLAUSE (reviewer clause 5): if a predictable drift
appears on the chosen genealogy, test whether it is a period-4
component expressible as a bounded coboundary A_k = G_{k+4} -
G_k -- then subtract the predictable part exactly and only the
centered rest enters the moment inequality.  (X_k itself has
ZERO drift by algebra; the drift clause is applied to the
predictable LOG drift delta_k = E[ln X_{k+1}] - E[ln X_k] <= 0,
Jensen-exact, warded live.)

LEG 0 -- THE CANONICAL GENEALOGY (adjudicated BEFORE the freeze,
sealed by this SPEC_SHA; the e4 mutant proves the protocol audit
bites).  Named canonical tree choices over the m final atoms:
  (a) THE ITERATED r270 FOLD (CHOSEN): bottom-up pairing of
      adjacent blocks in position order (PAIR_OFFSET 0, odd tail
      its own single-child node), iterated to the root.  Three
      reasons, frozen a-priori: (i) PARAMETER-FREE -- the r270
      level-2 convention verbatim, no new tunable; (ii)
      CONSTRUCTION-CANONICAL -- the final atoms PDelta_j were
      themselves created by exactly this adjacent-pair fold on
      the signed runs, so iterating it upward IS the fold
      ancestry ("which atom from which fold"); (iii)
      POSITION-CONTIGUOUS -- every node is a contiguous position
      interval, compatible with the r333/r335 support/margin
      geometry (the Leg-D bridge can talk to the r335 mass arm).
  (b) BALANCED TOP-DOWN BISECTION (ceil | floor): differs from
      (a) only in the placement of odd counts -- kept as the
      SENSITIVITY column (the exact identities are TREE-FREE by
      algebra and are warded on both trees; the Gamma budget is
      compared census-grade).
  (c) a genealogy descending INTO the blocks (leaves = fold
      groups or runs): REFUSED a-priori -- the contract fixes
      the leaves at the m final atoms a_i = |PDelta_i| (the
      dictionary X_inf = m q_i is the round's currency).
  GROUNDING (r327 mass mechanics): the leaf masses are the exact
  fold recomposition -- the r327 group partition (sum_g gabs ==
  A1_j), the L1 recomposition and the two-ancestor bound are
  re-warded live (GMC ledger cross-ward, verbatim).
  THE HEAVY-JUMP THRESHOLD (a-priori): a node is HEAVY iff
  max_c R_c > R_STAR = 3/2 -- for a balanced pair this is
  exactly "the light child falls below the band floor 1/4 of
  the pair mass", the SAME 1/4 as the r333/r335 band theorem;
  sensitivity column R_ALT = 7/4 (light share < 1/8).

LEG A -- fold_mass_tree_exact + descendant_density_martingale:
the tree built exactly; the martingale identity E[X_{k+1}|V_k]
= X_k verified EXACTLY (bit-equal Fractions: per node
sum_c A(c) == A(v) as exact rationals on the small windows w9 +
w13) and f64-warded on the full ladder + EXT3 + controls (per
node |sum_c p_c R_c - 1|, per level |E[X_k] - 1|, the exact
cubic recursion E[X_{k+1}^3] == sum_v P(v) X_v^3 Gamma(v), the
envelope E[X_inf^3] <= prod_k max_v Gamma).  This is an
IDENTITY, not a test -- must-fail e1: the wrong child weighting
(p_c without n) breaks it exactly on the uneven toy.

LEG B -- martingale_moment_dictionary: E[X_inf^2] == m M_2 and
E[X_inf^3] == m^2 M_3 exact (Fractions on the toys, f64 <=
DICT_BAR live); anchored bit-near against the r324 chain per
rung (m M_2 == the r324-pre m2 state, max y/m == the q_max
state, E[X_inf^3] == rho_2 (log m)^2 -- the r306 NORM identity).
DISCLOSED KNOWN PRE-SPEC: via the dictionary the banked r306
record C_2 = 1.069 with 0/57 violations ALREADY reads
E[X_inf^3] <= 1.069 (log m)^2 pointwise on the 57-rung set --
the genuinely open content of this round is the GAMMA BUDGET
(the pathwise Reverse-Holder question: is the worst-case
per-level product summable?), the anatomy (WHERE the inflation
sits), the good/heavy split and the drift.

LEG C -- THE GAMMA ANATOMY (the core measurement), on MAIN/
twin/EPSTEIN/SCRAMBLE over the WHOLE ladder + the 12 EXT3
anchors (r329 record, r335 adoption verbatim, PURE TEST rows),
resolved by level k: per level Gamma_max(k); the budget
W_F = prod_k Gamma_max(k) (E[X_inf^3] <= W_F exact); the good
budget W_G = prod_k max over GOOD nodes (heavy nodes excluded,
factor 1 if a level has no good node -- sealed definition); the
heavy leaf share hsh (fraction of leaves below >= 1 heavy node,
exact union); the per-level argmax anatomy (level k*, node
position third) for the named spike family kz53/83/67/55 and
the mid-band family kz73/76/61 + kz95/98/109.  Kernfragen:
(i) is log Gamma summable -- W_F <= C_F(a) (log m)^a, a in
GA_FAM = (1, 2, 3), mid-ladder max-cal freeze (TRB verbatim),
test incl. EXT3, named 4/4?  (ii) WHERE does the inflation sit
(levels, spikes vs mid-band)?  (iii) does the Gamma anatomy
separate the worlds (SCRAMBLE may break the local structure --
census, no adjudication)?  (iv) drift measurement + the
period-4 coboundary test (pooled ladder-median level profile;
direct ratio r4 = sum |delta_{k+4} - delta_k| / sum |delta_k -
mean| and the exact phase-mean subtraction ratio r4c; coboundary
letter iff r4c <= R4_BAR = 1/2, a-priori; DISCLOSED: with only
K = 7..10 levels per rung the per-rung period-4 test is weak --
the pooled profile is the honest form, census-grade).

LEG D -- THE BRIDGE (measurement only, NO claim): how much
polylog budget would the GOOD tree need if the r335 mass arm
stops the heavy jumps (max_c R_c > R_STAR)?  The per-rung
two-arm decomposition is printed (hsh = heavy leaf share,
n_heavy, W_G = accumulated good inflation, W_F) -- the
PREPARATION for R341 (Bellman / Reverse Holder), NOT its
execution.  The good budget certification W_G <= C_G(a)
(log m)^a is gated alongside.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) WRONG CHILD WEIGHTING: mutant_child_weight uses p_c =
  1/#children instead of n(c)/n(v) -- on the uneven Fractions
  toy (3, 1, 1) the conditional returns 9/10 != 1 (break 1/10
  EXACT) -- CAUGHT exact; the live census counts the uneven
  nodes the mutant would corrupt.
(e2) MOMENT DICTIONARY WITH m INSTEAD OF m^2:
  mutant_dict_m_power claims E[X_inf^3] == m M_3 -- on the
  Fractions toy the break is 20/9 - 5/9 = 5/3 EXACT -- CAUGHT
  exact.
(e3) GAMMA READ BACK FROM THE TARGET: mutant_gamma_from_target
  derives a 'Gamma column' from the cubic record (consumes
  cm/S3) -- the PHI3_FORBIDDEN scan must FLAG it (AST-CAUGHT)
  while the module-own tree builders stay clean.
(e4) TREE CHOICE AFTER RECORD SIGHT (protocol):
  mutant_tree_posthoc re-picks the pairing offset after sight of
  the evaluated bound column (consumes rho) -- the
  BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed toy
  it returns offset 1 != the canonical PAIR_OFFSET 0 --
  protocol-CAUGHT twice (the genealogy is sealed in Leg 0 BEFORE
  the freeze).
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.

SEALED VERDICTS (exactly one fires; total order):
   TARGET_LEAK                 iff any purity/scope/literal audit
       hit on the tree builders,
   MASS_TREE_NOT_CANONICAL     iff a structural ward breaks on a
       live world (martingale identity / unit mean / cubic
       recursion / dictionary / Jensen sign / the r327
       partition-recomposition grounding / the Fractions
       bit-equality on w9+w13 / the tree-free identities under
       the alternative tree),
   DENSITY_MARTINGALE_EXACT    iff all exact wards hold AND the
       FULL Gamma budget certifies at minimal a in GA_FAM
       (W_F <= C_F(a) (log m)^a, 0 test violations incl. EXT3 +
       named 4/4) -- summable inflation: the R341
       recommendation (Bellman) is printed with concrete
       constants,
   GOODTREE_A2_ONLY            iff not the full budget but the
       GOOD-TREE budget certifies at some a (the two-arm
       decomposition carries; the minimal good a is printed
       inside),
   LOCAL_INFLATION_SUPERCRITICAL  otherwise -- log Gamma is not
       summable in this language either; said honestly, with
       the measured exponents printed inside.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in
either direction.  Coexistence: r337 (raw signed fold process)
is sealed and INDEPENDENT (see the verdict-reading rule above);
r338 (reading audit) may run in parallel; this probe touches
NOTHING outside its own file and the strictly additive rh-sync
(existing entries byte-identical).  Two-commit freeze protocol
(r329 convention): spec committed pre-freeze, record tables the
only post-freeze edit, committed again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r324/r327/r333/r335
machinery imported verbatim): t_{N-2} = sum_b ct_b (r244 chain
rows, r266 eval); F = 0.20 edge split; maximal same-sign runs of
the bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy
+ SCF.signed_cube_terms + SCF.flux_telescope; the r316
TRB.two_regime_state + TRB.split_midladder; the r324
QMO.mult_ward; the r324-pre FAP.m2_qmax_state; the r327
GMC.group_mass_ledger (the Leg-0 grounding cross-ward);
PDelta = Pbeta - Pomega; x_j = (PDelta)_j; a_i = |x_i|.  NEW in
this round (module-own, source-pure): fold_mass_tree_exact (the
sealed iterated r270 pairing tree), fold_mass_tree_split (the
sensitivity alternative), descendant_density_martingale (the
per-node/per-level martingale + Gamma anatomy state),
martingale_moment_dictionary (the leaf moments) and the sealed
density_tree_verdict.

LEG 0 ANCHORS -- REGRESSION (slim set, disclosed): the r314
identity wards live; r306 C_2 = 1.069 (tol 0.005) first-5
freeze, 0/57; r316 rho anchors kz53/kz67/kz55/kz83 = 1.0490/
1.0536/0.4821/0.7790 (tol 0.005) + C_small 1.0694 at kz18 + n =
65; r324-pre C_M2 = 2.2557 (tol 0.005) with the seven m2 test
violators {53, 67, 83, 76, 61, 28, 109} EXACT as a set; the
dictionary-chain identity live on every live world (G34).

INDEX FIREWALL (binding, r238-r337 discipline): w = window (kz),
N_w = builder depth, k here = TREE LEVEL (root 0), n(v) = leaf
count; ground truth (branch labels, the true R/t/Z values)
enters GATES and census tables only; the cubic target M_3 /
rho_2 and the q_max RECORD enter GATES / anchors / composition
checks only, NEVER a tree builder (AST-warded; the tree
builders consume the abs block values + index order ONLY); no
zero/prime oracles anywhere (AST firewall); no fit primitives
(fragment audit; growth exponents are the imported r272 dyadic
halves-slope, fit-free).  MACHINERY IMPORTED VERBATIM: r327
GMC.group_mass_ledger, r324 QMO.mult_ward, r324-pre
FAP.m2_qmax_state, r316 TRB.two_regime_state +
TRB.split_midladder, r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope, r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze, r298
WBT.block_breaks + WBT.aggregate_blocks, r269 PBB.mask_edge +
PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed, r316/r324/r327/r335 verbatim): frame-A h <= 900, 42
rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39,
52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz); EXT2: the
r316 A5 rule (leftover pool + first 12 windows 1300 < h <= 1650,
first 8 POSITIVE_PREFIX by (N, kz)); EXT3: the sealed r329
12-anchor list (record committed 8cbd95f9, adopted as-is, PURE
TEST rows).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN, r270
verbatim -- also the sealed tree pairing offset); EXT_H_MAX
1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX 1650;
EXT2_POOL_CAP 12; K_EXT2 8; EXT3_KZ_B (42, 51, 54, 56, 58, 62);
EXT3_KZ_A (96, 123, 125, 127, 128, 130); EXT3_NW_MIN 1721;
EXT3_NW_MAX 2577; R_STAR 3/2 (a-priori, the band-floor tie);
R_ALT 7/4 (sensitivity); GA_FAM (1, 2, 3); R4_BAR 0.5
(a-priori); R4_MINK 8; NAMED_KZ (53, 83, 67, 55); MIDBAND_KZ
(73, 76, 61, 95, 98, 109) (the sealed r335 worst-violator six);
ATOM_BAR 1e-9; REC3_BAR 1e-13 ladder / 1e-12 EXT3; TEL_BAR
1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; SA_BAR 1e-12; TREE_BAR
1e-9; DICT_BAR 1e-9; JEN_BAR 1e-12; DEG_FLOOR 1e-6; MULT_CAP 2;
N_CAL 5 (via TRB, verbatim); MUT_MIN 1e-6; TOY_BAR 1e-12;
FR_BAR 0 (bit-equality); TB_WARD bars 1e-9 main N <= 400 / 3e-6
deep + ext + ext2 / 3e-5 EXT3 (r329 a-priori) / 1e-6 controls;
ID_BAR 1e-12; AC_BAR 1e-9; INF_SENT 1e300 / cert guard 1e299;
CRIT_EXP 0.224 (the r324 budget verbatim); N2_EXP_NEED 0.888;
R306_C2 1.069 tol 0.005; N339_REF 65; R316 RHO {53: 1.0490, 67:
1.0536, 55: 0.4821, 83: 0.7790} tol 0.005, C_SMALL 1.0694 tol
0.005 at kz18; R324P_CM2 2.2557 tol 0.005, M2VIOL {53, 67, 83,
76, 61, 28, 109} EXACT; R339_TABLE_LITERALS = the sealed
r314..r335 set (r337 verbatim) UNION the r337 record set
{0.7364, 1.5501, 1.677, 1.1012, 0.6035, 0.949, 54.40, 53.59,
48.91, 41.96, 41.68, 40.90, 0.399, 0.483, 0.755, 0.352, 0.5293,
2.09, 0.845, 0.721, 0.059, 0.204, 0.704, 1.027, 1.1159} (the
r337 displays 0.400 / 0.299 / 2.03 / 1.72 / 1.04 / 1.05 are
OMITTED from the forbidden set to avoid collisions with
innocent small toy rationals -- disclosed curation, r337
convention);
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the tree/dictionary/Jensen wards + the w9 Fractions
bit-equality + e1-e4 mutants; ladder, extensions, EXT3, anchors,
census, certification, drift pooling and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r324-pre RECORD number adopted
as-is; the martingale identity, the moment dictionary, the
local anatomy sum_c p_c R_c = 1, the envelope E[X_inf^3] <=
prod Gamma_max and the Jensen sign delta_k <= 0 are derived
algebra, disclosed above; the r306 record already bounds
E[X_inf^3] <= 1.069 (log m)^2 on the 57-rung set via the
dictionary (disclosed -- the open content is the Gamma budget
and anatomy); the genealogy choice + R_STAR + GA_FAM + R4_BAR
are a-priori (Leg 0, frozen BEFORE any evaluation); GENUINELY
OPEN quantities of this round: every Gamma column (per-level
Gamma_max, W_F, W_G, hsh, n_heavy, r4, argmax levels/thirds),
all certification constants C_F(a)/C_G(a), all violation
counts, the named/mid-band anatomy, the world census, the drift
profile and all exponents -- NONE was computed before this spec
was frozen; the five sealed letters are symmetric and total --
the tree maps every outcome to exactly one letter by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R339_ANCHORS(identity wards, r306 C_2, r316 rho + C_small + n,
    r324-pre C_M2 + violator set)
+ SEAL(tree wards: martingale f64 + Fractions bit-equal +
    unit mean + cubic recursion + envelope + dictionary-chain
    identity + Jensen + the r327 grounding + the alternative
    tree + purity audits + toys)
+ DICTIONARY(m M_2 / m^2 M_3 columns anchored to the chain)
+ GAMMA(census: per-level anatomy, W_F/W_G/hsh stats, named +
    mid-band anatomy, world table)
+ DRIFT(delta profile, r4/r4c, coboundary letter, census)
+ CERT(C_F(a) + viol + named + minimal a; C_G(a) likewise;
    exponents e(W_F)/e(W_G)/e(m^2 M_3) + halves stability;
    sensitivity: split tree + R_ALT census)
+ [exactly one of] DENSITY_MARTINGALE_EXACT / GOODTREE_A2_ONLY /
    LOCAL_INFLATION_SUPERCRITICAL / MASS_TREE_NOT_CANONICAL /
    TARGET_LEAK
+ BRIDGE(the two-arm decomposition + the R341 preparation;
    printed ALWAYS, typed)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the martingale identity, the dictionary,
the local anatomy, the envelope, the Jensen sign, the Fractions
toys, the tree logic and the purity audits are EXACT
(Fractions/AST-decided); every census, constant, violation
count and exponent is MEASURED on the finite ladder (+ the 12
adopted EXT3 anchors) only; a certifying budget fixes a proof
TARGET for R341 (Bellman), it proves NO cofinal law; the r306
dictionary reading of the banked C_2 is a disclosed pre-spec
input, not a finding of this round; r243-r338 stand.

RECORD TABLES (inserted AFTER the record run -- the only
amendment after freeze; freeze SPEC_SHA a845041cdf866543,
pre-freeze commit 907ebfd1; protocol: smoke pass 1 = 36/36
(0.7 s), NO amendment; calibration pass 1 = first full
evaluation, 36/36, wall 170.4 s, NO amendment; record run1/run2
after this insertion, identical up to the runtime line):
MAIN VERDICT: LOCAL_INFLATION_SUPERCRITICAL(NEITHER budget
certifies: full W_F viol 44/43/40 of 51 at a = 1/2/3 (C_F
39.9133/8.9841/2.0222, named 1/4, midband 1/6), good tree W_G
viol 33/20/11 (C_G 2.8325/0.6393/0.1443, named 3/4 at a >= 2,
midband 6/6 at a = 3); e(W_F) = +0.956 DECIDED supercritical,
halves +1.700/+1.756) -- the WORST-CASE per-level product
language is capped too, said honestly.  THE EXACT LAYER STANDS
AT THEOREM GRADE: the density martingale is exact on 81 live
worlds (per-node identity 2.2e-16, unit mean 4.4e-16, cubic
recursion 1.2e-15, envelope viol 0.0, Jensen 0.0; FRACTIONS
BIT-EQUALITY on w9 + w13: 76 nodes, symbolic dev == 0) and the
moment dictionary is exact against the r324 chain (d2 4.9e-16 /
d3 7.8e-16 / ymx 2.5e-16) -- the terminal target IS
E[X_inf^3] <= C (log m)^A, and the banked r306 C_2 = 1.069
(0/57, re-gated here) already certifies it at A = 2 on the
57-rung set.
THE THREE STRUCTURAL FINDINGS OF THE ROUND: (1) THE GAP IS THE
FINDING -- the true expectation e(m^2 M_3) = +0.112 grows 8x
slower than the worst-case budget e(W_F) = +0.956: Gamma_max is
dominated by NEAR-LEAF DEGENERATE PAIRS (the per-level
Gamma_max med profile rises monotonically toward the leaves,
1.05 -> 3.99, pressing against the algebraic ceiling 4 of a
balanced pair; the deep half of the levels carries med 0.712 of
log W_F) where hardly any PATH MASS sits -- the R341 Bellman
argument must weight Gamma by path probability, not take
per-level maxima (this is the concrete, measured reason the
naive Reverse-Holder budget fails).  (2) NO SHARP WORLD OR
FAMILY SEPARATION in the Gamma anatomy: named spikes W_F med
324.33 vs mid-band med 404.57 vs ladder med 265.54 (hsh named
0.877..0.992, midband 0.820..1.000); SCRAMBLE W_F 51.76 sits
BELOW the ladder median 223.86 and does NOT break the local
structure (honest negative: the per-level Gamma_max statistic
is world-blind in this reading); the worst W_F violators are
the EXT3 deep anchors kz42 (18.29x at a = 3, W_F 4364.9) +
kz51/62/123/54/125 -- the deep-anchor margin of r337 recurs in
the density language.  (3) THE DRIFT IS PRESENT BUT NOT
PERIOD-4: the pooled predictable log-drift profile is strictly
<= 0 (sum -1.1392; Jensen-exact) and monotone-deepening toward
the leaves, but the period-4 coboundary clause does NOT fire
(r4 0.934 / r4c 0.957 vs R4_BAR 0.5; per-rung r4 med 0.784 on
the 42 rungs with K >= 8) -- the r336/r337 period-4 component
does not reappear as the density drift; clause 5 subtraction is
therefore NOT applied (nothing to subtract exactly).
CENSUS: W_F min/med/max 16.17/265.54/4364.90 (max at EXT3
kz42); W_G med 13.69 max 39.14; alt-tree W_F med 487.03 (the
sensitivity choice is WORSE -- the sealed pairing tree is the
sharper canonical form); Gamma_max med 3.93 max 4.303 (the only
level value above 4 sits at an uneven 3-leaf node, ceiling 9);
hsh med 0.872 max 1.000, heavy rungs 77/77; levels K 5..10;
R_ALT 1.75 envelopes {a1 111.49, a2 17.911, a3 2.878}; EXT3
cohort e(W_F) = +0.392 (census-grade, r329 caveat); BRIDGE
envelope (NOT composed): the a = 3 envelope 18.2922 would give
m_0* 10^30.4 vs the r324 route 10^59.6 -- typed envelope only,
preparation for R341.
NAMED ANATOMY (kz, m, K, W_F, W_G, hsh, k*, Gk*): kz53 119/7/
515.67/14.11/0.882/2/4.303 (the ONE mid-tree spike Gk* at
level 2 -- the r324 single-heavy-scale event visible as an
early heavy fold); kz83 248/8/416.10/26.55/0.927/7/3.974; kz67
129/8/232.57/13.63/0.992/7/3.874; kz55 73/7/47.75/7.93/0.877/
6/2.971; MID-BAND: kz73 208.64/hsh 1.000, kz76 659.57/0.846,
kz61 505.14/1.000, kz95 265.54/0.820, kz98 393.51/0.829, kz109
415.63/0.863 -- at every mid-band rung k* = K - 1 (the
inflation sits at the LAST fold level).
WORLDS: w9 m 35 W_F 82.46 W_G 8.56 hsh 1.000; twin w13 m 35
W_F 53.34 W_G 5.05 hsh 0.857; EPSTEIN m 22 W_F 19.71; SCRAMBLE
m 30 W_F 51.76 hsh 0.867 dm3 20.59 (the SCRAMBLE dictionary
value dm3 = m^2 M_3 = 20.59 is 3.3x the ladder med 6.22 -- the
DICTIONARY separates the worlds where the Gamma_max census
does not); SMOOTH degenerate-skipped (pre-declared).
ANCHORS bit-near: r314 identity 4.5e-17; r306 C_2 1.069
(0/57); r316 n 65 + rho quartet 1.0493/1.0536/0.4821/0.7791 +
C_small 1.0694@kz18; r324-pre C_M2 2.2557 + the seven m2
violators {28, 53, 61, 67, 76, 83, 109} EXACT.
SEAL: contribution ward 2.1e-13/2.2e-12 (ladder/EXT3), r327
grounding partition 3.4e-16 / L1 recomposition 0.0 /
two-ancestor 0.0, ledger == genealogy 0.0, uneven nodes 262
(the e1 mutant surface), zero-mass leaves 0, purity clean,
toys exact; must-fails e1 CAUGHT exact (break 1/10, float
0.100) / e2 CAUGHT exact (break 5/3) / e3 AST-CAUGHT (S3) /
e4 protocol-CAUGHT twice (AST rho + toy offset 1 != 0) +
m5a/m5b FLAGGED.

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
import renyi3_probe as RY3                     # noqa: E402 r306
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
import two_regime_bound_probe as TRB           # noqa: E402 r316
import fa_provenance_probe as FAP              # noqa: E402 r324-pre
import qmax_m2_origin_probe as QMO             # noqa: E402 r324
import group_mass_cap_probe as GMC             # noqa: E402 r327
import companion_orbit_packing_probe as COP    # noqa: E402 r333
import fold_martingale_probe as FMP            # noqa: E402 r337
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
TB_WARD_BAR_X3 = 3e-5
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
EXT3_KZ_B = (42, 51, 54, 56, 58, 62)
EXT3_KZ_A = (96, 123, 125, 127, 128, 130)
EXT3_NW_MIN = 1721
EXT3_NW_MAX = 2577
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
REC3_BAR_X3 = 1e-12
TEL_BAR = 1e-13
BND_BAR = 1e-13
CHAIN_BAR = 1e-9
SA_BAR = 1e-12
TREE_BAR = 1e-9
DICT_BAR = 1e-9
JEN_BAR = 1e-12
DEG_FLOOR = 1e-6
MULT_CAP = 2
N_CAL = 5
PAIR_OFFSET = 0
R_STAR = 1.5
R_ALT = 1.75
GA_FAM = (1, 2, 3)
R4_BAR = 0.5
R4_MINK = 8
NAMED_KZ = (53, 83, 67, 55)
MIDBAND_KZ = (73, 76, 61, 95, 98, 109)
MUT_MIN = 1e-6
TOY_BAR = 1e-12
EDGE_F = 0.20
INF_SENT = 1e300
CERT_GUARD = 1e299
CRIT_EXP = 0.224
N2_EXP_NEED = 0.888
R306_C2 = 1.069
R306_C2_TOL = 0.005
N339_REF = 65
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R324P_CM2 = 2.2557
R324P_CM2_TOL = 0.005
R324P_M2VIOL = (53, 67, 83, 76, 61, 28, 109)
R339_TABLE_LITERALS = frozenset(FMP.R337_TABLE_LITERALS | {
    0.7364, 1.5501, 1.677, 1.1012, 0.6035, 0.949, 54.40, 53.59,
    48.91, 41.96, 41.68, 40.90, 0.399, 0.483, 0.755, 0.352,
    0.5293, 2.09, 0.845, 0.721, 0.059, 0.204, 0.704, 1.027,
    1.1159})

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


BOUND_FORBIDDEN = COP.BOUND_FORBIDDEN
PHI3_FORBIDDEN = COP.PHI3_FORBIDDEN
QMAX_FORBIDDEN = COP.QMAX_FORBIDDEN


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
    lies in the sealed r314..r337 record set."""
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
                            in R339_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the tree
# ---------------- builders consume the ABS BLOCK VALUES + the
# ---------------- index order ONLY; the withheld terminal drive
# ---------------- key, the branch label, the cubic target M_3 /
# ---------------- rho_2 and the q_max RECORD are forbidden (AST
# ---------------- identifier scan + literal scan).
def fold_mass_tree_exact(vals):
    """the SEALED CANONICAL GENEALOGY (Leg 0, choice (a)): the
    r270 fold operation iterated -- bottom-up pairing of adjacent
    leaves in index (= position) order from PAIR_OFFSET, odd tail
    its own single-child node, up to the root.  Levels are stored
    ROOT-FIRST; children of node i at level k are the nodes
    kptr[k][i] .. kptr[k][i+1] of level k+1.  Consumes abs values
    + index order only."""
    av = np.abs(np.asarray(vals, dtype=float))
    m = int(len(av))
    lv_mass = [av.copy()]
    lv_cnt = [np.ones(m, dtype=int)]
    while len(lv_mass[-1]) > 1:
        ms = lv_mass[-1]
        cn = lv_cnt[-1]
        n = len(ms)
        nh = (n + 1) // 2
        pm = np.zeros(nh)
        pc = np.zeros(nh, dtype=int)
        pm[:n // 2] = ms[PAIR_OFFSET:n - 1:2] + ms[1::2]
        pc[:n // 2] = cn[PAIR_OFFSET:n - 1:2] + cn[1::2]
        if n % 2:
            pm[-1] = ms[-1]
            pc[-1] = cn[-1]
        lv_mass.append(pm)
        lv_cnt.append(pc)
    lv_mass.reverse()
    lv_cnt.reverse()
    kptr = []
    for k in range(len(lv_mass) - 1):
        nk = len(lv_mass[k])
        nc = len(lv_mass[k + 1])
        pt = np.minimum(2 * np.arange(nk + 1), nc)
        pt[-1] = nc
        kptr.append(pt)
    return dict(mass=lv_mass, cnt=lv_cnt, kptr=kptr,
                depth=len(lv_mass) - 1, m=m)


def fold_mass_tree_split(vals):
    """the SENSITIVITY ALTERNATIVE (Leg 0, choice (b)): balanced
    top-down bisection (ceil | floor); differs from the sealed
    tree only in the placement of odd counts.  Same storage
    contract as fold_mass_tree_exact.  Consumes abs values +
    index order only."""
    av = np.abs(np.asarray(vals, dtype=float))
    m = int(len(av))
    cs = np.concatenate(([0.0], np.cumsum(av)))
    rng = [(0, m)]
    ranges = [list(rng)]
    while any(b - a > 1 for a, b in rng):
        nxt = []
        for a, b in rng:
            if b - a <= 1:
                nxt.append((a, b))
            else:
                h = a + (b - a + 1) // 2
                nxt.append((a, h))
                nxt.append((h, b))
        rng = nxt
        ranges.append(list(rng))
    lv_mass = []
    lv_cnt = []
    for lev in ranges:
        lv_mass.append(np.array([cs[b] - cs[a] for a, b in lev]))
        lv_cnt.append(np.array([b - a for a, b in lev], dtype=int))
    kptr = []
    for k in range(len(ranges) - 1):
        spawn = [1 if b - a <= 1 else 2 for a, b in ranges[k]]
        pt = np.concatenate(([0], np.cumsum(spawn)))
        kptr.append(pt.astype(int))
    return dict(mass=lv_mass, cnt=lv_cnt, kptr=kptr,
                depth=len(lv_mass) - 1, m=m)


def descendant_density_martingale(gtree):
    """the DENSITY MARTINGALE STATE on a mass tree: per node v the
    density d(v) = A(v)/n(v) and X(v) = d(v)/d(root); per level k
    the leaf-uniform moments; the exact per-node conditional
    identity sum_c p_c R_c == 1 (mass conservation), the exact
    per-level unit mean E[X_k] == 1, the exact cubic recursion
    E[X_{k+1}^3] == sum_v P(v) X_v^3 Gamma(v), the local cubic
    inflation Gamma(v) = sum_c p_c R_c^3, the per-level maxima
    (full and GOOD = max_c R_c <= R_STAR), the budgets W_F/W_G,
    the heavy leaf share and the predictable log drift.  Consumes
    the tree only."""
    mass = gtree["mass"]
    cnt = gtree["cnt"]
    kptr = gtree["kptr"]
    kk = gtree["depth"]
    m = gtree["m"]
    aroot = float(mass[0][0])
    if m < 2 or aroot <= 0.0:
        return dict(kk=0, ok=False, unit_dev=0.0, mart_dev=0.0,
                    rec_dev=0.0, gmx_lv=(), ggd_lv=(), arg_lv=(),
                    wf=1.0, wg=1.0, walt=1.0, hsh=0.0, nheavy=0,
                    nuneven=0, ex3=(1.0,), drift=(), nzero=0)
    droot = aroot / float(m)
    xs = [(mass[k] / np.maximum(cnt[k], 1)) / droot
          for k in range(kk + 1)]
    unit_dev = 0.0
    ex3 = []
    for k in range(kk + 1):
        wts = cnt[k].astype(float) / float(m)
        unit_dev = max(unit_dev,
                       abs(float(np.sum(wts * xs[k])) - 1.0))
        ex3.append(float(np.sum(wts * xs[k] ** 3)))
    mart_dev = 0.0
    rec_dev = 0.0
    gmx_lv = []
    ggd_lv = []
    gal_lv = []
    arg_lv = []
    nheavy = 0
    nuneven = 0
    heavy_prev = np.zeros(1, dtype=bool)
    heavy_leaf = heavy_prev
    drift = []
    nzero = int(np.sum(mass[kk] <= 0.0))
    for k in range(kk):
        pt = kptr[k]
        mv = mass[k]
        cv = cnt[k]
        nk = len(mv)
        gmx = 1.0
        ggd = 1.0
        gaa = 1.0
        arg = (0, 0)
        heavy_here = np.zeros(nk, dtype=bool)
        rec_sum = 0.0
        for i in range(nk):
            a, b = int(pt[i]), int(pt[i + 1])
            if b - a > 1:
                cchild = cnt[k + 1][a:b]
                if int(np.min(cchild)) != int(np.max(cchild)):
                    nuneven += 1
            if mv[i] <= 0.0:
                continue
            mc = mass[k + 1][a:b]
            cc = cnt[k + 1][a:b].astype(float)
            pv = cc / float(cv[i])
            rv = (mc / np.maximum(cc, 1.0)) \
                / (mv[i] / float(cv[i]))
            mart_dev = max(mart_dev,
                           abs(float(np.sum(pv * rv)) - 1.0))
            gam = float(np.sum(pv * rv ** 3))
            mxr = float(np.max(rv))
            if gam > gmx:
                gmx = gam
                arg = (i, int(cv[i]))
            if mxr > R_STAR:
                heavy_here[i] = True
                nheavy += 1
            else:
                ggd = max(ggd, gam)
            if mxr <= R_ALT:
                gaa = max(gaa, gam)
            rec_sum += (cv[i] / float(m)) * xs[k][i] ** 3 * gam
        rec_dev = max(rec_dev, abs(rec_sum - ex3[k + 1])
                      / max(abs(ex3[k + 1]), 1e-300))
        gmx_lv.append(gmx)
        ggd_lv.append(ggd)
        gal_lv.append(gaa)
        arg_lv.append(arg)
        # propagate the heavy-descendant mark to level k + 1
        nxt = np.zeros(len(mass[k + 1]), dtype=bool)
        for i in range(nk):
            a, b = int(pt[i]), int(pt[i + 1])
            nxt[a:b] = bool(heavy_prev[i]) or bool(heavy_here[i])
        heavy_prev = nxt
        heavy_leaf = nxt
        if nzero == 0:
            wa = cnt[k].astype(float) / float(m)
            wb = cnt[k + 1].astype(float) / float(m)
            ea = float(np.sum(wa * np.log(np.maximum(xs[k],
                                                     1e-300))))
            eb = float(np.sum(wb * np.log(np.maximum(xs[k + 1],
                                                     1e-300))))
            drift.append(eb - ea)
    hsh = float(np.sum(cnt[kk][heavy_leaf])) / float(m) \
        if kk else 0.0
    wf = float(np.prod(gmx_lv)) if gmx_lv else 1.0
    wg = float(np.prod(ggd_lv)) if ggd_lv else 1.0
    wa2 = float(np.prod(gal_lv)) if gal_lv else 1.0
    return dict(kk=kk, ok=True, unit_dev=unit_dev,
                mart_dev=mart_dev, rec_dev=rec_dev,
                gmx_lv=tuple(gmx_lv), ggd_lv=tuple(ggd_lv),
                arg_lv=tuple(arg_lv), wf=wf, wg=wg, walt=wa2,
                hsh=hsh, nheavy=nheavy, nuneven=nuneven,
                ex3=tuple(ex3), drift=tuple(drift), nzero=nzero)


def martingale_moment_dictionary(vals):
    """the LEAF MOMENT DICTIONARY: with y_i = a_i/(A/m) = m q_i
    the leaf-uniform moments d1 = E[X_inf] (= 1), d2 =
    E[X_inf^2] (== m M_2 exact), d3 = E[X_inf^3] (== m^2 M_3
    exact) and ymx = max y (== m q_max).  Consumes abs values
    only."""
    av = np.abs(np.asarray(vals, dtype=float))
    m = int(len(av))
    tot = float(np.sum(av))
    if m < 2 or tot <= 0.0:
        return dict(d1=0.0, d2=0.0, d3=0.0, ymx=0.0)
    y = av * (float(m) / tot)
    return dict(d1=float(np.mean(y)), d2=float(np.mean(y ** 2)),
                d3=float(np.mean(y ** 3)), ymx=float(np.max(y)))


def density_tree_verdict(leak, brk, full_go, good_go):
    """the sealed five-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    MASS_TREE_NOT_CANONICAL > DENSITY_MARTINGALE_EXACT >
    GOODTREE_A2_ONLY > LOCAL_INFLATION_SUPERCRITICAL."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "MASS_TREE_NOT_CANONICAL"
    if full_go:
        return "DENSITY_MARTINGALE_EXACT"
    if good_go:
        return "GOODTREE_A2_ONLY"
    return "LOCAL_INFLATION_SUPERCRITICAL"


def mutant_child_weight(gtree):
    """e1 MUST-FAIL MUTANT: the conditional expectation with the
    WRONG child weighting p_c = 1/#children (n(c) dropped) -- on
    any node with uneven child leaf counts the identity breaks
    exactly (the Fractions toy pins the break at 1/10)."""
    mass = gtree["mass"]
    cnt = gtree["cnt"]
    kptr = gtree["kptr"]
    worst = 0.0
    for k in range(gtree["depth"]):
        pt = kptr[k]
        for i in range(len(mass[k])):
            a, b = int(pt[i]), int(pt[i + 1])
            if mass[k][i] <= 0.0 or b - a < 1:
                continue
            mc = mass[k + 1][a:b]
            cc = cnt[k + 1][a:b].astype(float)
            dv = mass[k][i] / float(cnt[k][i])
            rv = (mc / np.maximum(cc, 1.0)) / dv
            worst = max(worst,
                        abs(float(np.sum(rv)) / (b - a) - 1.0))
    return worst


def mutant_dict_m_power(vals):
    """e2 MUST-FAIL MUTANT: the moment dictionary with m instead
    of m^2 -- claims E[X_inf^3] == m M_3 (one power of m
    dropped); on the Fractions toy the break is 5/3 EXACT."""
    av = np.abs(np.asarray(vals, dtype=float))
    m = int(len(av))
    tot = float(np.sum(av))
    m3 = float(np.sum((av / max(tot, 1e-300)) ** 3))
    return float(m) * m3


def mutant_gamma_from_target(ev):
    """e3 MUST-FAIL MUTANT: a 'Gamma column' derived from the
    cubic TARGET record (consumes cm/S3) -- the PHI3_FORBIDDEN
    scan must FLAG this while the tree builders stay clean."""
    return abs(float(ev["cm"]["S3"])) ** (1.0 / 3.0)


def mutant_tree_posthoc(off_seen, rho, cbar):
    """e4 MUST-FAIL MUTANT (protocol): the pairing offset
    re-picked AFTER SIGHT of the evaluated bound column (consumes
    rho) -- the BOUND_FORBIDDEN scope audit must FLAG it AND on
    the sealed toy it returns 1 != the canonical PAIR_OFFSET 0 --
    the genealogy is sealed in Leg 0 BEFORE the freeze."""
    pick = PAIR_OFFSET
    for o, r in zip(off_seen, rho):
        if r > cbar:
            pick = max(pick, int(o))
    return pick


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'tree orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'budget constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the martingale, the
# ---------------- dictionary, the anatomy and the mutant breaks
# ---------------- decided as rationals
def fr_pair_tree(leaves):
    """exact Fractions mass tree via the sealed pairing rule:
    returns levels root-first as lists of (A, n)."""
    lev = [[(v, 1) for v in leaves]]
    while len(lev[-1]) > 1:
        cur = lev[-1]
        nxt = []
        for i in range(0, len(cur) - 1, 2):
            nxt.append((cur[i][0] + cur[i + 1][0],
                        cur[i][1] + cur[i + 1][1]))
        if len(cur) % 2:
            nxt.append(cur[-1])
        lev.append(nxt)
    return lev[::-1]


def fr_split_tree(leaves):
    """exact Fractions mass tree via the balanced top-down
    bisection (the sensitivity alternative)."""
    m = len(leaves)
    rng = [(0, m)]
    levels = [list(rng)]
    while any(b - a > 1 for a, b in rng):
        nxt = []
        for a, b in rng:
            if b - a <= 1:
                nxt.append((a, b))
            else:
                h = a + (b - a + 1) // 2
                nxt.append((a, h))
                nxt.append((h, b))
        rng = nxt
        levels.append(list(rng))
    out = []
    for lev in levels:
        out.append([(sum(leaves[a:b], Fr(0)), b - a)
                    for a, b in lev])
    return out


def fr_mart_check(lev):
    """exact martingale check on a Fractions tree: per level the
    node masses must sum to the root mass (bit-equal), and per
    node E[X_{k+1}|V_k = v] == X_v as exact rationals.  Returns
    (ok, worst symbolic dev, #nodes checked)."""
    aroot, m = lev[0][0]
    ok = True
    worst = Fr(0)
    nchk = 0
    droot = aroot / Fr(m)
    for k in range(len(lev)):
        s = sum(a for a, _n in lev[k])
        if s != aroot:
            ok = False
            worst = max(worst, abs(s - aroot))
    for k in range(len(lev) - 1):
        cur = lev[k]
        nxt = lev[k + 1]
        j = 0
        for a, n in cur:
            take = []
            acc = 0
            while acc < n:
                take.append(nxt[j])
                acc += nxt[j][1]
                j += 1
            nchk += 1
            if a == 0:
                continue
            xv = (a / Fr(n)) / droot
            cond = sum((Fr(nc, n)) * ((ac / Fr(nc)) / droot)
                       for ac, nc in take)
            if cond != xv:
                ok = False
                worst = max(worst, abs(cond - xv))
    return ok, worst, nchk


def fr_tree_toy():
    """the sealed even toy (3, 1, 1, 1) in exact Fractions:
    d_root = 3/2; X_1 = (4/3, 2/3) with E[X_1] = 1; per-node
    conditionals EXACT; Gamma(root) = 4/3, Gamma((3,1)) = 7/4,
    Gamma((1,1)) = 1; cubic recursion E[X_1^3] = 4/3 and
    E[X_2^3] = 20/9 == m^2 M_3 EXACT; m M_2 = 4/3 == E[X_inf^2]
    EXACT; the e2 dictionary mutant claims m M_3 = 5/9 (break
    5/3 EXACT).  Returns (worst dev, e2 break)."""
    leaves = [Fr(3), Fr(1), Fr(1), Fr(1)]
    lev = fr_pair_tree(leaves)
    okm, wm, _n = fr_mart_check(lev)
    m = Fr(4)
    tot = sum(leaves, Fr(0))
    y = [v * m / tot for v in leaves]
    d2 = sum(v ** 2 for v in y) / m
    d3 = sum(v ** 3 for v in y) / m
    mm2 = m * sum((v / tot) ** 2 for v in leaves)
    m2m3 = m ** 2 * sum((v / tot) ** 3 for v in leaves)
    droot = tot / m
    d1a = (leaves[0] + leaves[1]) / Fr(2)
    d1b = (leaves[2] + leaves[3]) / Fr(2)
    g_root = (Fr(1, 2) * (d1a / droot) ** 3
              + Fr(1, 2) * (d1b / droot) ** 3)
    g_a = (Fr(1, 2) * (leaves[0] / d1a) ** 3
           + Fr(1, 2) * (leaves[1] / d1a) ** 3)
    g_b = (Fr(1, 2) * (leaves[2] / d1b) ** 3
           + Fr(1, 2) * (leaves[3] / d1b) ** 3)
    e1 = (Fr(1, 2) * (d1a / droot) ** 3
          + Fr(1, 2) * (d1b / droot) ** 3)
    e2r = (Fr(1, 2) * (d1a / droot) ** 3 * g_a
           + Fr(1, 2) * (d1b / droot) ** 3 * g_b)
    mut = m * sum((v / tot) ** 3 for v in leaves)
    brk = d3 - mut
    devs = [wm, abs(d2 - Fr(4, 3)), abs(d2 - mm2),
            abs(d3 - Fr(20, 9)), abs(d3 - m2m3),
            abs(g_root - Fr(4, 3)), abs(g_a - Fr(7, 4)),
            abs(g_b - 1), abs(e1 - Fr(4, 3)),
            abs(e2r - Fr(20, 9)),
            Fr(0) if okm else Fr(1)]
    return max(devs), brk


def fr_uneven_toy():
    """the sealed uneven toy (3, 1, 1) in exact Fractions (m = 3,
    pairing gives levels root (5, 3) / ((4, 2), (1, 1)) /
    leaves): the correct conditional at the root is EXACTLY 1
    (12/15 + 3/15); the e1 wrong-weight mutant returns 9/10
    (break 1/10 EXACT); the dictionary is tree-free: m M_2 =
    33/25 == E[X_inf^2] EXACT.  Returns (worst dev, e1
    break)."""
    leaves = [Fr(3), Fr(1), Fr(1)]
    lev = fr_pair_tree(leaves)
    okm, wm, _n = fr_mart_check(lev)
    tot = Fr(5)
    m = Fr(3)
    droot = tot / m
    d_a = Fr(4, 2)
    d_b = Fr(1)
    cond = (Fr(2, 3) * (d_a / droot)
            + Fr(1, 3) * (d_b / droot))
    mutc = (Fr(1, 2) * (d_a / droot)
            + Fr(1, 2) * (d_b / droot))
    brk = cond - mutc
    y = [v * m / tot for v in leaves]
    d2 = sum(v ** 2 for v in y) / m
    mm2 = m * sum((v / tot) ** 2 for v in leaves)
    devs = [wm, abs(cond - 1), abs(mutc - Fr(9, 10)),
            abs(brk - Fr(1, 10)), abs(d2 - Fr(33, 25)),
            abs(d2 - mm2), Fr(0) if okm else Fr(1)]
    return max(devs), brk


def fr_invariance_toy():
    """the tree-invariance toy (3, 1, 1, 1, 2), m = 5: BOTH the
    sealed pairing tree and the split alternative satisfy the
    exact martingale check, and the dictionary targets m M_2 =
    5/4 and m^2 M_3 = 475/256 are TREE-FREE.  Returns worst
    dev."""
    leaves = [Fr(3), Fr(1), Fr(1), Fr(1), Fr(2)]
    ok_a, wa, _na = fr_mart_check(fr_pair_tree(leaves))
    ok_b, wb, _nb = fr_mart_check(fr_split_tree(leaves))
    m = Fr(5)
    tot = Fr(8)
    y = [v * m / tot for v in leaves]
    d2 = sum(v ** 2 for v in y) / m
    d3 = sum(v ** 3 for v in y) / m
    devs = [wa, wb, abs(d2 - Fr(5, 4)),
            abs(d3 - Fr(475, 256)),
            Fr(0) if ok_a and ok_b else Fr(1)]
    return max(devs)


def fr_arm_toy():
    """the heavy/good split toy in exact Fractions: leaves (7, 1)
    -- R = (7/4, 1/4), max R = 7/4 > 3/2 HEAVY, Gamma = 43/16;
    leaves (5, 3) -- R = (5/4, 3/4), max R = 5/4 <= 3/2 GOOD,
    Gamma = 19/16.  The float builder reproduces flags and
    values.  Returns (worst dev, flags ok)."""
    d_h = Fr(8, 2)
    g_h = (Fr(1, 2) * (Fr(7) / d_h) ** 3
           + Fr(1, 2) * (Fr(1) / d_h) ** 3)
    d_g = Fr(8, 2)
    g_g = (Fr(1, 2) * (Fr(5) / d_g) ** 3
           + Fr(1, 2) * (Fr(3) / d_g) ** 3)
    devs = [abs(g_h - Fr(43, 16)), abs(g_g - Fr(19, 16)),
            Fr(0) if Fr(7) / d_h > Fr(3, 2) else Fr(1),
            Fr(0) if Fr(5) / d_g <= Fr(3, 2) else Fr(1)]
    st_h = descendant_density_martingale(
        fold_mass_tree_exact([7.0, 1.0]))
    st_g = descendant_density_martingale(
        fold_mass_tree_exact([5.0, 3.0]))
    flags = (abs(st_h["wf"] - float(Fr(43, 16))) <= TOY_BAR
             and st_h["nheavy"] == 1
             and abs(st_h["hsh"] - 1.0) <= TOY_BAR
             and abs(st_h["wg"] - 1.0) <= TOY_BAR
             and abs(st_g["wf"] - float(Fr(19, 16))) <= TOY_BAR
             and st_g["nheavy"] == 0
             and abs(st_g["hsh"]) <= TOY_BAR
             and abs(st_g["wg"] - st_g["wf"]) <= TOY_BAR)
    return max(devs), flags


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("fold_density_dictionary_probe -- "
          "PRIME.L2.FOLD_DENSITY_DICTIONARY.01 (round 339, the "
          "reviewer reformulation of terminal)")
    print("SPEC_SHA %s   R337_SHA %s   R327_SHA %s   R324_SHA %s"
          % (SPEC_SHA[:16], FMP.SPEC_SHA[:16], GMC.SPEC_SHA[:16],
             QMO.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + tree/dictionary/Jensen "
                        "wards + w9 Fractions bit-equality + "
                        "e1-e4; ladder, extensions, EXT3, "
                        "anchors, census, certification, drift "
                        "pooling and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE DENSITY-MARTINGALE ROUND (reviewer reformulation "
          "of terminal): the canonical fold genealogy over the m "
          "final atoms a_i = |PDelta_i| (Leg 0 SEALED: the "
          "iterated r270 pairing, PAIR_OFFSET %d; alternative "
          "= balanced bisection as sensitivity; leaves-inside-"
          "blocks REFUSED); X_k = d(V_k)/d(root) is a "
          "nonnegative martingale by mass conservation ALONE; "
          "the dictionary E[X_inf^2] == m M_2, E[X_inf^3] == "
          "m^2 M_3 EXACT; the anatomy Gamma(v) = sum p_c R_c^3 "
          "with sum p_c R_c = 1 exact; budgets W_F/W_G vs "
          "(log m)^a, a in %s (mid-ladder max-cal freeze, EXT3 "
          "pure test); heavy iff max R_c > %.2f (the band-floor "
          "1/4 tie, a-priori; sensitivity %.2f); drift clause = "
          "the period-4 coboundary test at R4_BAR %.1f; verdict "
          "tree TARGET_LEAK / MASS_TREE_NOT_CANONICAL / "
          "DENSITY_MARTINGALE_EXACT / GOODTREE_A2_ONLY / "
          "LOCAL_INFLATION_SUPERCRITICAL sealed BEFORE "
          "evaluation"
          % (PAIR_OFFSET, str(GA_FAM), R_STAR, R_ALT, R4_BAR))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("fold_mass_tree_exact", "fold_mass_tree_split",
               "descendant_density_martingale",
               "martingale_moment_dictionary",
               "density_tree_verdict"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the five module-own "
          "tree builders/trees clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the "
          "tree side consumes ONLY abs block values + index "
          "order; m5a gift-bound FLAGGED (%s); m5b branch-peek "
          "FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r335 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSIONS + EXT3")
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
        ext3 = []
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
        ext3 = [BH.wpack(kz) for kz in EXT3_KZ_B + EXT3_KZ_A]
        ext3.sort(key=lambda p: (p["N"], p["kz"]))
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
        check("G14-ext3-admission", True, "SMOKE: skipped")
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
        check("G14-ext3-admission",
              len(ext3) == 12
              and all(p["nf"] is None for p in ext3)
              and min(p["N"] for p in ext3) == EXT3_NW_MIN
              and max(p["N"] for p in ext3) == EXT3_NW_MAX,
              "EXT3 = the sealed r329 RECORD selection (committed "
              "8cbd95f9, r335 adoption verbatim): 12 anchors (B "
              "%s + A %s), POSITIVE_PREFIX %d/12, N_w %d..%d "
              "(record %d..%d) -- PURE TEST rows, never "
              "calibration"
              % (str(EXT3_KZ_B), str(EXT3_KZ_A),
                 sum(1 for p in ext3 if p["nf"] is None),
                 min(p["N"] for p in ext3),
                 max(p["N"] for p in ext3),
                 EXT3_NW_MIN, EXT3_NW_MAX))

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
    x3recs = [rung_rec(p) for p in ext3] if not smoke else []
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
        e_cheap = sum(1 for rc in erecs + e2recs + x3recs
                      if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs + e2recs + x3recs
                 if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT+EXT2+EXT3 census (no sealed expectation): %d "
              "cheap / %d exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + TREE-LEDGER WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_x3 = 0.0
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
    for rc in x3recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_x3 = max(tb_x3, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_x3 <= TB_WARD_BAR_X3
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d ext2 "
          "+ %d ext3 + %d mains + 3 controls: worst dev/absmass "
          "%.1e main N<=%d (bar %.0e) / %.1e deep / %.1e "
          "ext+ext2 (bar %.0e) / %.1e ext3 (bar %.0e) / %.1e "
          "controls (bar %.0e)"
          % (len(recs), len(erecs), len(e2recs), len(x3recs),
             len(mrecs), tb_worst, DEEP_N, TB_WARD_BAR, tb_deep,
             tb_ext, TB_WARD_BAR_DEEP, tb_x3, TB_WARD_BAR_X3,
             tb_ctrl, TB_WARD_BAR_CTRL))

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
        edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
        xw = rc["xu"][~edw]
        vw = -rc["cw"][~edw]
        jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
        jb2 = np.searchsorted(brk, xb) if m else np.zeros(0, int)
        mism = int(np.sum(jb2 != jb))
        pos_all = np.concatenate([xb, xw])
        val_all = np.concatenate([cb, vw])
        blk_all = np.concatenate([jb, jw]).astype(int)
        src_all = np.concatenate([np.zeros(len(xb)),
                                  np.ones(len(xw))])
        if m and not degenerate:
            gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
            sct = SCF.signed_cube_terms(gen["G1"], gen["gblk"], m)
            ft = SCF.flux_telescope(gen["G1"], gen["ptr"], m)
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
            trs = TRB.two_regime_state(sct["x"], sct["Q2"],
                                       sct["Q3"], gen["G1"],
                                       gen["ptr"], ft["F_end"],
                                       ft["F_open"],
                                       ft["edge_abs"], m)
            rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
            mqs = FAP.m2_qmax_state(sct["x"])
            led327 = GMC.group_mass_ledger(pos_all, val_all,
                                           blk_all, src_all, m)
            gtree = fold_mass_tree_exact(sct["x"])
            dst = descendant_density_martingale(gtree)
            atree = fold_mass_tree_split(sct["x"])
            ast_ = descendant_density_martingale(atree)
            dic = martingale_moment_dictionary(sct["x"])
        else:
            gen = sct = ft = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            C_bnd = 0.0
            mx_mult = 0
            A1 = np.zeros(0)
            trs = dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0,
                       fe=0.0, fcix=0.0, qmax=0.0, cnt3=0.0,
                       phiL1=0.0, phiL2=0.0, phiH1=0.0,
                       phiH2=0.0, L=0.0)
            rho2 = 0.0
            mqs = dict(qm=0.0, m2=0.0, ymx=0.0, maj=0.0)
            led327 = None
            gtree = None
            dst = descendant_density_martingale(
                dict(mass=[np.zeros(1)], cnt=[np.ones(1, int)],
                     kptr=[], depth=0, m=0))
            ast_ = dict(dst)
            dic = dict(d1=0.0, d2=0.0, d3=0.0, ymx=0.0)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs,
                    led327=led327, gtree=gtree, dst=dst,
                    ast=ast_, dic=dic,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs + x3recs
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
    led_dev = 0.0
    x3_mult_ok = True
    for rc in live:
        ev = rc["ev"]
        gen = ev["gen"]
        l327 = ev["led327"]
        if gen["ng"] != l327["ng"]:
            led_dev = max(led_dev, 1.0)
            continue
        if gen["ng"]:
            sc = max(float(np.max(np.abs(gen["G1"]))), 1e-300)
            led_dev = max(
                led_dev,
                float(np.max(np.abs(l327["G1"] - gen["G1"]))) / sc,
                float(np.max(np.abs(l327["mult"] - gen["mult"]))),
                float(np.max(np.abs(l327["gblk"] - gen["gblk"]))))
    for rc in x3recs:
        if rc["ev"]["mx_mult"] > MULT_CAP:
            x3_mult_ok = False
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR
          and x3_mult_ok,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "r327 GMC ledger segments IDENTICALLY to the genealogy "
          "(worst dev %.1e, bar %.0e -- the Leg-0 grounding); "
          "EXT3 fold multiplicity <= %d on 12/12 (%s)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             MULT_CAP, "OK" if x3_mult_ok else "BROKEN",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (slim)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim set)")
    x3_ids = set(id(rc) for rc in x3recs)
    live_69 = [rc for rc in live if id(rc) not in x3_ids]
    rec3_w = max(rc["ev"]["rec3"] for rc in live_69)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live_69)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live_69)
    rec3_x = max((rc["ev"]["rec3"] for rc in x3recs), default=0.0)
    tel_x = max((rc["ev"]["tel_dev"] for rc in x3recs),
                default=0.0)
    bnd_x = max((rc["ev"]["bnd_dev"] for rc in x3recs),
                default=0.0)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR and rec3_x <= REC3_BAR_X3
          and tel_x <= REC3_BAR_X3 and bnd_x <= REC3_BAR_X3,
          "the r314 identity live: ladder worlds recomposition "
          "%.1e / telescope %.1e / boundary %.1e (bars %.0e); "
          "EXT3 %.1e / %.1e / %.1e (bar %.0e, r329 a-priori); "
          "DISCLOSED slim anchor set -- the full chain is "
          "re-warded by the sealed r321..r337 probes"
          % (rec3_w, tel_w, bnd_w, REC3_BAR, rec3_x, tel_x,
             bnd_x, REC3_BAR_X3))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 m %d K %d Wf %.3f Wg %.3f hsh %.3f nH "
             "%d dm2 %.4f dm3 %.4f"
             % (ev9s["m"], ev9s["dst"]["kk"], ev9s["dst"]["wf"],
                ev9s["dst"]["wg"], ev9s["dst"]["hsh"],
                ev9s["dst"]["nheavy"], ev9s["dic"]["d2"],
                ev9s["dic"]["d3"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r324pre-m2-anchor", True, "SMOKE: skipped")
        srt = []
        n339 = 0
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2r, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2r)
        check("G31-r306-bound-live",
              abs(C2r - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d "
              "-- via the dictionary this ALREADY reads "
              "E[X_inf^3] <= C_2 (log m)^2 on the 57-rung set "
              "(disclosed pre-spec)"
              % (C2r, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        srt_all65 = sorted(recs + erecs + e2recs,
                           key=lambda rc: (rc["N"], rc["kz"]))
        srt = [rc for rc in srt_all65
               if rc["ev"]["mx_mult"] <= MULT_CAP]
        n339 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n339)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n339 == N339_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n339, N339_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
        m2_col = [rc["ev"]["mqs"]["m2"] for rc in srt]
        C_M2 = max(m2_col[i] for i in ca_i)
        viol_m2 = tuple(sorted(srt[i]["kz"] for i in te_i
                               if m2_col[i] > C_M2))
        check("G33-r324pre-m2-anchor",
              abs(C_M2 - R324P_CM2) <= R324P_CM2_TOL
              and viol_m2 == tuple(sorted(R324P_M2VIOL)),
              "the r324-pre m2 record reproduced: mid-ladder "
              "freeze C_M2 %.4f (rec %.4f tol %.3f); the seven "
              "test violators %s == the banked set EXACT"
              % (C_M2, R324P_CM2, R324P_CM2_TOL, str(viol_m2)))
    # G34 dictionary-chain identity (live, both modes)
    dict2_w = 0.0
    dict3_w = 0.0
    dictq_w = 0.0
    for rc in live:
        ev = rc["ev"]
        dic = ev["dic"]
        mloc = ev["m"]
        dict2_w = max(dict2_w, abs(dic["d2"] - ev["mqs"]["m2"])
                      / max(ev["mqs"]["m2"], 1e-300))
        rid = ev["rho2"] * (math.log(float(mloc)) ** 2)
        dict3_w = max(dict3_w, abs(dic["d3"] - rid)
                      / max(rid, 1e-300))
        dictq_w = max(dictq_w,
                      abs(dic["ymx"] / float(mloc)
                          - ev["mqs"]["qm"])
                      / max(ev["mqs"]["qm"], 1e-300))
    check("G34-dictionary-chain-identity",
          dict2_w <= DICT_BAR and dict3_w <= DICT_BAR
          and dictq_w <= DICT_BAR,
          "THE MOMENT DICTIONARY anchored bit-near to the r324 "
          "chain on %d live worlds: E[X_inf^2] == m M_2 (r324-pre "
          "state, worst rel %.1e), E[X_inf^3] == m^2 M_3 == "
          "rho_2 (log m)^2 (r306 NORM identity, worst %.1e), "
          "max y / m == q_max (worst %.1e; bars %.0e) -- the "
          "terminal target M_3 <= C (log m)^A/m^2 is EQUIVALENT "
          "to E[X_inf^3] <= C (log m)^A by this dictionary"
          % (len(live), dict2_w, dict3_w, dictq_w, DICT_BAR))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "SOURCE-PURE TABLE")
    pure_lits = []
    for fn in ("fold_mass_tree_exact", "fold_mass_tree_split",
               "descendant_density_martingale",
               "martingale_moment_dictionary",
               "density_tree_verdict", "fr_pair_tree",
               "fr_split_tree", "fr_mart_check", "fr_tree_toy",
               "fr_uneven_toy", "fr_invariance_toy",
               "fr_arm_toy"):
        pure_lits += literal_audit(fn)
    e3_hits = scope_audit("mutant_gamma_from_target",
                          PHI3_FORBIDDEN)
    e4_hits = scope_audit("mutant_tree_posthoc", BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e3_hits) >= 1 and len(e4_hits) >= 1,
          "SOURCE PURITY: the tree builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed "
          "r314..r337 record-literal set (%d literal hits); "
          "consumed inputs: abs block values + index order ONLY "
          "-- M_3, rho_2 and the q_max RECORD are TARGET-SIDE, "
          "computed outside the builders (disclosed); e3 "
          "gamma-from-target FLAGGED (%s); e4 tree-posthoc "
          "FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e3_hits[0] if e3_hits else "MISS",
             e4_hits[0] if e4_hits else "MISS"))
    fr_dev, fr_e2brk = fr_tree_toy()
    fu_dev, fu_e1brk = fr_uneven_toy()
    fi_dev = fr_invariance_toy()
    fa_dev, fa_flags = fr_arm_toy()
    st_even = descendant_density_martingale(
        fold_mass_tree_exact([3.0, 1.0, 1.0, 1.0]))
    ok_even = (st_even["ok"] and st_even["kk"] == 2
               and abs(st_even["wf"] - float(Fr(7, 3))) <= TOY_BAR
               and abs(st_even["ex3"][2] - float(Fr(20, 9)))
               <= TOY_BAR
               and st_even["mart_dev"] <= TOY_BAR
               and st_even["rec_dev"] <= TOY_BAR)
    mut1_even = mutant_child_weight(
        fold_mass_tree_exact([3.0, 1.0, 1.0, 1.0]))
    mut1_unev = mutant_child_weight(
        fold_mass_tree_exact([3.0, 1.0, 1.0]))
    mut2 = mutant_dict_m_power([3.0, 1.0, 1.0, 1.0])
    dic_toy = martingale_moment_dictionary([3.0, 1.0, 1.0, 1.0])
    tr_br = (density_tree_verdict(True, True, True, True),
             density_tree_verdict(False, True, True, True),
             density_tree_verdict(False, False, True, True),
             density_tree_verdict(False, False, False, True),
             density_tree_verdict(False, False, False, False))
    ok_tr = tr_br == ("TARGET_LEAK", "MASS_TREE_NOT_CANONICAL",
                      "DENSITY_MARTINGALE_EXACT",
                      "GOODTREE_A2_ONLY",
                      "LOCAL_INFLATION_SUPERCRITICAL")
    check("G41-toy-exactness",
          fr_dev == 0 and fu_dev == 0 and fi_dev == 0
          and fa_dev == 0 and fa_flags and ok_even
          and fr_e2brk == Fr(5, 3) and fu_e1brk == Fr(1, 10)
          and mut1_even <= TOY_BAR
          and abs(mut1_unev - float(Fr(1, 10))) <= TOY_BAR
          and abs(dic_toy["d3"] - mut2 - float(Fr(5, 3)))
          <= TOY_BAR and ok_tr,
          "the Fractions tree toys EXACT: even (3,1,1,1) worst "
          "dev %s (Gamma root 4/3, (3,1) 7/4, E[X_inf^3] 20/9 "
          "== m^2 M_3, W_F 7/3); uneven (3,1,1) worst %s "
          "(conditional == 1 EXACT, e1 wrong-weight break 1/10 "
          "EXACT); invariance (3,1,1,1,2) worst %s (BOTH trees "
          "martingale-exact, dictionary tree-free m M_2 5/4 / "
          "m^2 M_3 475/256); heavy/good toy worst %s (heavy "
          "(7,1): Gamma 43/16 maxR 7/4 > R*; good (5,3): Gamma "
          "19/16), float flags %s; e2 dictionary break 5/3 "
          "EXACT; density_tree_verdict all five branches EXACT "
          "%s"
          % (str(fr_dev), str(fu_dev), str(fi_dev), str(fa_dev),
             "OK" if fa_flags else "BROKEN", str(tr_br)))
    # live tree wards
    mart_w = 0.0
    unit_w = 0.0
    rec_w = 0.0
    env_w = 0.0
    jen_w = 0.0
    amart_w = 0.0
    adict_w = 0.0
    part_w = 0.0
    panc_w = 0.0
    l1rec_w = 0.0
    interp_w = 0.0
    chain_w = 0.0
    xw_cube = 0.0
    nz_tot = 0
    nuneven_tot = 0
    mult_all_ok = True
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
        x_abs = np.abs(ev["sct"]["x"])
        Lx = float(np.sum(x_abs))
        qv = x_abs / max(Lx, 1e-300)
        M3 = float(np.sum(qv ** 3))
        M2 = float(np.sum(qv ** 2))
        qmx = float(np.max(qv))
        interp_w = max(interp_w,
                       max(0.0, M3 - qmx * M2)
                       / max(qmx * M2, 1e-300),
                       max(0.0, M2 - qmx) / max(qmx, 1e-300))
        st = ev["dst"]
        at = ev["ast"]
        if st["ok"]:
            mart_w = max(mart_w, st["mart_dev"])
            unit_w = max(unit_w, st["unit_dev"])
            rec_w = max(rec_w, st["rec_dev"])
            env_w = max(env_w,
                        max(0.0, st["ex3"][-1] - st["wf"])
                        / max(st["wf"], 1e-300))
            jen_w = max(jen_w,
                        max((d for d in st["drift"]),
                            default=0.0))
            nz_tot += st["nzero"]
            nuneven_tot += st["nuneven"]
        if st["ok"] and at["ok"]:
            amart_w = max(amart_w, at["mart_dev"],
                          at["unit_dev"], at["rec_dev"])
            adict_w = max(adict_w,
                          abs(at["ex3"][-1] - st["ex3"][-1])
                          / max(st["ex3"][-1], 1e-300))
        led = ev["led327"]
        mloc = ev["m"]
        A1led = np.bincount(led["gblk"], weights=led["gabs"],
                            minlength=mloc)
        part_w = max(part_w,
                     float(np.max(np.abs(A1led - ev["A1"])))
                     / max(float(np.max(ev["A1"])), 1e-300))
        xled = np.bincount(led["gblk"], weights=led["G1"],
                           minlength=mloc)
        l1rec_w = max(l1rec_w,
                      abs(float(np.sum(np.abs(xled))) - Lx)
                      / max(Lx, 1e-300))
        if led["ng"]:
            panc_w = max(panc_w,
                         float(np.max(led["gabs"]
                                      - led["mult"] * led["gmax"]))
                         / max(float(np.max(led["gabs"])), 1e-300))
        mult_all_ok = mult_all_ok \
            and QMO.mult_ward(ev["gen"]["mult"])[1]
    # the Fractions bit-equality on the small windows (w9 + w13)
    fr_ok = True
    fr_nodes = 0
    for rc in mrecs:
        if rc["ev"]["degenerate"]:
            continue
        leaves = [Fr(float(abs(v)))
                  for v in rc["ev"]["sct"]["x"]]
        okx, wx, nx = fr_mart_check(fr_pair_tree(leaves))
        fr_ok = fr_ok and okx and (wx == 0)
        fr_nodes += nx
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and interp_w <= CHAIN_BAR and mart_w <= TREE_BAR
          and unit_w <= TREE_BAR and rec_w <= TREE_BAR
          and env_w <= CHAIN_BAR and jen_w <= JEN_BAR
          and amart_w <= TREE_BAR and adict_w <= DICT_BAR
          and part_w <= SA_BAR and l1rec_w <= SA_BAR
          and panc_w <= TOY_BAR and fr_ok and nz_tot == 0
          and mult_all_ok,
          "the r316 chain live on %d live worlds (worst %.1e); "
          "NORM x cube == rho_2 (%.1e); S0 interpolation (worst "
          "%.1e); THE MARTINGALE IDENTITY sum_c p_c R_c == 1 per "
          "node (worst %.1e, bar %.0e) AND E[X_k] == 1 per level "
          "(worst %.1e) AND the cubic recursion (worst %.1e) AND "
          "the envelope E[X_inf^3] <= W_F (worst viol %.1e) AND "
          "Jensen delta_k <= 0 (worst %.1e, bar %.0e); "
          "FRACTIONS BIT-EQUALITY on w9+w13: %s (%d nodes, "
          "symbolic dev == 0); the ALTERNATIVE tree satisfies "
          "the same identities (worst %.1e) with tree-free "
          "E[X_inf^3] (dev %.1e); r327 GROUNDING: partition %.1e "
          "(bar %.0e), L1 recomposition %.1e, two-ancestor %.1e; "
          "zero-mass leaves %d; uneven nodes %d (the e1 mutant "
          "surface); fold multiplicity <= %d admitted"
          % (len(live), chain_w, xw_cube, interp_w, mart_w,
             TREE_BAR, unit_w, rec_w, env_w, jen_w, JEN_BAR,
             "EXACT" if fr_ok else "BROKEN", fr_nodes, amart_w,
             adict_w, part_w, SA_BAR, l1rec_w, panc_w, nz_tot,
             nuneven_tot, MULT_CAP))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        srt_x = sorted(x3recs, key=lambda rc: (rc["N"], rc["kz"]))
        srt_x = [rc for rc in srt_x
                 if rc["ev"]["mx_mult"] <= MULT_CAP
                 and not rc["ev"]["degenerate"]]
        n_x3 = len(srt_x)
        srt_full = srt + srt_x
        n_full = len(srt_full)
        m_full = [rc["ev"]["m"] for rc in srt_full]
        kk_col = [rc["ev"]["dst"]["kk"] for rc in srt_full]
        wf_col = [rc["ev"]["dst"]["wf"] for rc in srt_full]
        wg_col = [rc["ev"]["dst"]["wg"] for rc in srt_full]
        wa_col = [rc["ev"]["dst"]["walt"] for rc in srt_full]
        hsh_col = [rc["ev"]["dst"]["hsh"] for rc in srt_full]
        nh_col = [rc["ev"]["dst"]["nheavy"] for rc in srt_full]
        d2_col = [rc["ev"]["dic"]["d2"] for rc in srt_full]
        d3_col = [rc["ev"]["dic"]["d3"] for rc in srt_full]
        gmw_col = [max(rc["ev"]["dst"]["gmx_lv"])
                   if rc["ev"]["dst"]["gmx_lv"] else 1.0
                   for rc in srt_full]
        awf_col = [rc["ev"]["ast"]["wf"] for rc in srt_full]
        r4_col = []
        for rc in srt_full:
            dr = rc["ev"]["dst"]["drift"]
            if len(dr) >= R4_MINK:
                mu = sum(dr) / len(dr)
                den = sum(abs(d - mu) for d in dr)
                num = sum(abs(dr[k + 4] - dr[k])
                          for k in range(len(dr) - 4))
                r4_col.append(num / max(den, 1e-300))
            else:
                r4_col.append(float("nan"))
        gb_cols = {}
        gg_cols = {}
        for a in GA_FAM:
            gb_cols[a] = [wf_col[i]
                          / (math.log(float(m_full[i])) ** a)
                          for i in range(n_full)]
            gg_cols[a] = [wg_col[i]
                          / (math.log(float(m_full[i])) ** a)
                          for i in range(n_full)]
        info("sealed SOURCE-PURE table (printed BEFORE any "
             "certification table): rank kz N m K Gmax WF WG "
             "WFalt hsh nH r4 dm2 dm3 GB1 GB2 GB3  [rows "
             "65..%d are EXT3 PURE TEST]" % (n_full - 1))
        for i, rc in enumerate(srt_full):
            info("%2d kz%-3d N %4d m %3d K %d Gx %6.3f WF "
                 "%8.3f WG %7.3f Wa %8.3f hsh %.3f nH %2d r4 "
                 "%5s dm2 %.3f dm3 %7.3f GB1 %7.3f GB2 %6.3f "
                 "GB3 %5.3f%s"
                 % (i, rc["kz"], rc["N"], m_full[i], kk_col[i],
                    gmw_col[i], wf_col[i], wg_col[i], awf_col[i],
                    hsh_col[i], nh_col[i],
                    ("%.2f" % r4_col[i])
                    if not math.isnan(r4_col[i]) else "-",
                    d2_col[i], d3_col[i], gb_cols[1][i],
                    gb_cols[2][i], gb_cols[3][i],
                    " X3" if i >= n339 else ""))
        check("G43-coordinate-table", True,
              "W_F range %.2f/%.2f/%.2f min/med/max (max at "
              "kz%d); W_G med %.2f max %.2f; W_F alt-tree med "
              "%.2f; Gamma_max med %.2f max %.2f; hsh med %.3f "
              "max %.3f; n_heavy med %.0f max %d; levels K "
              "%d..%d; dm3 med %.2f max %.2f; EXT3 rows %d"
              % (min(wf_col), float(np.median(wf_col)),
                 max(wf_col),
                 srt_full[int(np.argmax(wf_col))]["kz"],
                 float(np.median(wg_col)), max(wg_col),
                 float(np.median(awf_col)),
                 float(np.median(gmw_col)), max(gmw_col),
                 float(np.median(hsh_col)), max(hsh_col),
                 float(np.median(nh_col)), max(nh_col),
                 min(kk_col), max(kk_col),
                 float(np.median(d3_col)), max(d3_col), n_x3))

    # ---------------- S5: Leg C -- Gamma census + anatomy + worlds
    section("S5  LEG C -- GAMMA CENSUS + NAMED/MID-BAND ANATOMY "
            "+ WORLDS")
    if smoke:
        check("G50-gamma-census", True, "SMOKE: skipped")
        check("G51-named-midband-anatomy", True, "SMOKE: skipped")
    else:
        named_rank = {}
        for kz in NAMED_KZ + MIDBAND_KZ:
            for i in range(n_full):
                if srt_full[i]["kz"] == kz:
                    named_rank[kz] = i
        kmax = max(kk_col)
        lv_med = []
        lv_max = []
        for k in range(kmax):
            vals = [rc["ev"]["dst"]["gmx_lv"][k]
                    for rc in srt_full
                    if len(rc["ev"]["dst"]["gmx_lv"]) > k]
            lv_med.append(float(np.median(vals)))
            lv_max.append(max(vals))
        info("per-level Gamma_max ladder profile (root level 0 "
             "-> leaves): med %s | max %s"
             % (str([round(v, 3) for v in lv_med]),
                str([round(v, 3) for v in lv_max])))
        deep_share = []
        for rc in srt_full:
            gl = rc["ev"]["dst"]["gmx_lv"]
            if not gl:
                deep_share.append(0.0)
                continue
            w_all = sum(math.log(max(v, 1.0)) for v in gl)
            h = len(gl) // 2
            w_deep = sum(math.log(max(v, 1.0)) for v in gl[h:])
            deep_share.append(w_deep / max(w_all, 1e-300))
        check("G50-gamma-census", True,
              "WHERE THE INFLATION SITS (question ii): the deep "
              "half of the levels (toward the leaves) carries "
              "med %.3f / max %.3f of log W_F; per-level "
              "Gamma_max med profile %s; single worst level "
              "value %.3f"
              % (float(np.median(deep_share)), max(deep_share),
                 str([round(v, 2) for v in lv_med]),
                 max(lv_max)))
        for fam, kzs_f in (("NAMED", NAMED_KZ),
                           ("MIDBAND", MIDBAND_KZ)):
            for kz in kzs_f:
                i = named_rank[kz]
                st = srt_full[i]["ev"]["dst"]
                gl = st["gmx_lv"]
                ks = int(np.argmax([math.log(max(v, 1.0))
                                    for v in gl])) if gl else 0
                info("%s kz%-3d m %3d K %d WF %8.3f WG %7.3f "
                     "hsh %.3f nH %2d k* %d Gk* %.3f lv %s"
                     % (fam, kz, m_full[i], st["kk"], st["wf"],
                        st["wg"], st["hsh"], st["nheavy"], ks,
                        gl[ks] if gl else 1.0,
                        str([round(v, 2) for v in gl])))
        named_wf = [wf_col[named_rank[kz]] for kz in NAMED_KZ]
        mb_wf = [wf_col[named_rank[kz]] for kz in MIDBAND_KZ]
        check("G51-named-midband-anatomy", True,
              "SPIKES vs MID-BAND (question ii): named W_F %s "
              "(med %.2f) vs mid-band W_F %s (med %.2f) vs "
              "ladder med %.2f; named hsh %s; mid-band hsh %s"
              % (str([round(v, 2) for v in named_wf]),
                 float(np.median(named_wf)),
                 str([round(v, 2) for v in mb_wf]),
                 float(np.median(mb_wf)),
                 float(np.median(wf_col)),
                 str([round(hsh_col[named_rank[kz]], 3)
                      for kz in NAMED_KZ]),
                 str([round(hsh_col[named_rank[kz]], 3)
                      for kz in MIDBAND_KZ])))
    # world table (both modes)
    ev9w = (recs[0] if smoke else mrecs[0])["ev"]
    ev13 = None if smoke else mrecs[1]["ev"]
    wtab = [("w9", ev9w)] + ([("w13(twin)", ev13)]
                             if ev13 is not None else [])
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wtab.append((c, crecs[c]["ev"]))
    info("world table: world m K WF WG hsh nH dm2 dm3")
    for w, ev in wtab:
        st = ev["dst"]
        info("  %-10s m %3d K %d WF %8.3f WG %7.3f hsh %.3f "
             "nH %2d dm2 %.3f dm3 %7.3f | Gmax lv %s"
             % (w, ev["m"], st["kk"], st["wf"], st["wg"],
                st["hsh"], st["nheavy"], ev["dic"]["d2"],
                ev["dic"]["d3"],
                str([round(v, 2) for v in st["gmx_lv"]])))
    scr_ev = crecs["SCR"]["ev"]
    if smoke:
        check("G52-world-census", len(wtab) >= 2,
              "SMOKE: world table printed (w9 + live controls); "
              "the separation census needs the ladder")
    else:
        wf_med = float(np.median(wf_col[:n339]))
        check("G52-world-census", len(wtab) >= 2,
              "question (iii) WORLD SEPARATION (census, NO "
              "claim): SCRAMBLE W_F %.3f / hsh %.3f vs ladder "
              "med %.3f / %.3f (%s in W_F); EPSTEIN W_F %.3f; "
              "twin w13 W_F %.3f -- SCRAMBLE %s the local "
              "Gamma structure on this reading"
              % (scr_ev["dst"]["wf"], scr_ev["dst"]["hsh"],
                 wf_med, float(np.median(hsh_col[:n339])),
                 "ABOVE" if scr_ev["dst"]["wf"] > wf_med
                 else "BELOW", crecs["EPST"]["ev"]["dst"]["wf"],
                 ev13["dst"]["wf"],
                 "does NOT break" if scr_ev["dst"]["wf"]
                 <= max(wf_col[:n339]) else "BREAKS"))

    # ---------------- S6: Leg C/D -- certification + drift + exps
    section("S6  LEG C/D -- GAMMA BUDGET CERTIFICATION + DRIFT + "
            "EXPONENTS")
    if smoke:
        check("G60-full-budget-cert", True, "SMOKE: skipped")
        check("G61-good-budget-cert", True, "SMOKE: skipped")
        check("G62-drift-coboundary", True, "SMOKE: skipped")
        check("G63-growth-exponents", True, "SMOKE: skipped")
    else:
        te_x = list(te_i) + list(range(n339, n_full))

        def cert_max(cols):
            out = {}
            for a in GA_FAM:
                col = cols[a]
                CQ = max(col[i] for i in ca_i)
                viol = [i for i in te_x if col[i] > CQ]
                named = sum(1 for kz in NAMED_KZ
                            if col[named_rank[kz]] <= CQ)
                mb = sum(1 for kz in MIDBAND_KZ
                         if col[named_rank[kz]] <= CQ)
                out[a] = (CQ, viol, named, mb, col)
            aa = None
            for a in GA_FAM:
                if (not out[a][1] and out[a][2] == len(NAMED_KZ)
                        and out[a][0] < CERT_GUARD):
                    aa = a
                    break
            return out, aa

        certF, aF = cert_max(gb_cols)
        certG, aG = cert_max(gg_cols)
        check("G60-full-budget-cert", True,
              "THE FULL GAMMA BUDGET W_F <= C_F(a) (log m)^a "
              "(max-cal mid-ladder freeze, test incl. EXT3): "
              + "; ".join("a=%d C_F %.4f viol %d/%d named %d/4 "
                          "midband %d/6"
                          % (a, certF[a][0], len(certF[a][1]),
                             len(te_x), certF[a][2], certF[a][3])
                          for a in GA_FAM)
              + "; worst violators %s; minimal certifying a = %s"
              % (str([(srt_full[i]["kz"],
                       round(certF[GA_FAM[-1]][4][i], 3))
                      for i in sorted(
                          certF[GA_FAM[-1]][1],
                          key=lambda i:
                          -certF[GA_FAM[-1]][4][i])[:6]]),
                 str(aF)))
        check("G61-good-budget-cert", True,
              "THE GOOD-TREE BUDGET W_G <= C_G(a) (log m)^a "
              "(heavy jumps max R_c > %.2f removed -- the r335 "
              "mass-arm hand-off surface): "
              % R_STAR
              + "; ".join("a=%d C_G %.4f viol %d/%d named %d/4 "
                          "midband %d/6"
                          % (a, certG[a][0], len(certG[a][1]),
                             len(te_x), certG[a][2], certG[a][3])
                          for a in GA_FAM)
              + "; minimal certifying a = %s; TWO-ARM "
              "DECOMPOSITION per rung printed in the G43 table "
              "(hsh / nH / WG / WF); heavy hand-off census: hsh "
              "med %.3f max %.3f, heavy rungs (hsh > 0) %d/%d"
              % (str(aG), float(np.median(hsh_col)),
                 max(hsh_col),
                 sum(1 for v in hsh_col if v > 0.0), n_full))
        # drift + period-4 coboundary (question iv)
        prof = []
        for k in range(kmax):
            vals = [rc["ev"]["dst"]["drift"][k]
                    for rc in srt_full
                    if len(rc["ev"]["dst"]["drift"]) > k]
            prof.append(float(np.median(vals)))
        mu_p = sum(prof) / max(len(prof), 1)
        den_p = sum(abs(v - mu_p) for v in prof)
        num_p = sum(abs(prof[k + 4] - prof[k])
                    for k in range(len(prof) - 4)) \
            if len(prof) > 4 else 0.0
        r4_pool = num_p / max(den_p, 1e-300)
        ph = [0.0] * 4
        phn = [0] * 4
        for k, v in enumerate(prof):
            ph[k % 4] += v
            phn[k % 4] += 1
        ph = [ph[p] / max(phn[p], 1) for p in range(4)]
        res_p = sum(abs(prof[k] - ph[k % 4])
                    for k in range(len(prof)))
        r4c_pool = res_p / max(den_p, 1e-300)
        cobo = r4c_pool <= R4_BAR
        r4_ok = [v for v in r4_col if not math.isnan(v)]
        check("G62-drift-coboundary", True,
              "question (iv) DRIFT: pooled ladder-median log "
              "drift profile delta_k = %s (all <= 0, "
              "Jensen-warded in G42); period-4 direct ratio r4 "
              "= %.3f, phase-subtraction ratio r4c = %.3f vs "
              "R4_BAR %.1f -> %s (the predictable period-4 part "
              "%s subtracted exactly: phase means %s, centered "
              "residual %.4f of raw %.4f); per-rung r4 (K >= "
              "%d): n %d med %s"
              % (str([round(v, 4) for v in prof]), r4_pool,
                 r4c_pool, R4_BAR,
                 "PERIOD4_COBOUNDARY" if cobo else
                 "NO_PERIOD4_COBOUNDARY",
                 "would be" if cobo else "cannot be",
                 str([round(v, 4) for v in ph]), res_p, den_p,
                 R4_MINK, len(r4_ok),
                 ("%.3f" % float(np.median(r4_ok)))
                 if r4_ok else "-"))
        msT = [m_full[i] for i in te_i]
        e_wf = L2D.halves_slope(msT, [max(wf_col[i], 1e-300)
                                      for i in te_i])
        e_wg = L2D.halves_slope(msT, [max(wg_col[i], 1e-300)
                                      for i in te_i])
        e_d3 = L2D.halves_slope(msT, [max(d3_col[i], 1e-300)
                                      for i in te_i])
        h = len(te_i) // 2
        te_a = te_i[:h]
        te_b = te_i[h:]

        def ewf_on(idx):
            return L2D.halves_slope([m_full[i] for i in idx],
                                    [max(wf_col[i], 1e-300)
                                     for i in idx])

        e_a = ewf_on(te_a)
        e_b = ewf_on(te_b)
        decided = ((e_a < CRIT_EXP) == (e_b < CRIT_EXP)
                   and (e_a < CRIT_EXP) == (e_wf < CRIT_EXP))
        x3_idx = list(range(n339, n_full))
        e_x3 = L2D.halves_slope(
            [m_full[i] for i in x3_idx],
            [max(wf_col[i], 1e-300) for i in x3_idx]) \
            if len(x3_idx) >= 2 else 0.0
        alt_env = {a: max(wa_col[i]
                          / (math.log(float(m_full[i])) ** a)
                          for i in range(n_full))
                   for a in GA_FAM}
        check("G63-growth-exponents", True,
              "GROWTH EXPONENTS (r272 dyadic halves-slope, "
              "fit-free, over the %d 65-ladder test rungs): "
              "e(W_F) = %+.3f vs CRIT %.3f (halves %+.3f/%+.3f "
              "-> %s), e(W_G) = %+.3f, e(m^2 M_3) = %+.3f "
              "(compare the r324 route e_tot +0.172, census); "
              "EXT3 cohort e(W_F) = %+.3f (census-grade, r329 "
              "caveat); SENSITIVITY (R_ALT %.2f budget "
              "envelopes): %s"
              % (len(te_i), e_wf, CRIT_EXP, e_a, e_b,
                 "DECIDED" if decided else "UNDECIDED", e_wg,
                 e_d3, e_x3, R_ALT,
                 str({("a%d" % a): round(alt_env[a], 3)
                      for a in GA_FAM})))

    # ---------------- S7: Leg D -- adjudication + bridge
    section("S7  LEG D -- SEALED ADJUDICATION + BRIDGE")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-bridge", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(sc_own) or bool(pure_lits)
        brk_struct = (mart_w > TREE_BAR or unit_w > TREE_BAR
                      or rec_w > TREE_BAR or env_w > CHAIN_BAR
                      or jen_w > JEN_BAR or dict2_w > DICT_BAR
                      or dict3_w > DICT_BAR or dictq_w > DICT_BAR
                      or amart_w > TREE_BAR or adict_w > DICT_BAR
                      or part_w > SA_BAR or l1rec_w > SA_BAR
                      or panc_w > TOY_BAR or not fr_ok
                      or not mult_all_ok)
        full_go = aF is not None
        good_go = aG is not None
        vkey = density_tree_verdict(leak, brk_struct, full_go,
                                    good_go)
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a tree "
                           "builder",
            "MASS_TREE_NOT_CANONICAL":
                "a structural ward broke (mart %.1e / unit %.1e "
                "/ rec %.1e / dict %.1e / Jensen %.1e / "
                "grounding %.1e / Fractions %s)"
                % (mart_w, unit_w, rec_w,
                   max(dict2_w, dict3_w, dictq_w), jen_w,
                   max(part_w, l1rec_w), str(fr_ok)),
            "DENSITY_MARTINGALE_EXACT":
                "the identities are exact AND the FULL Gamma "
                "budget certifies at a = %s (C_F %.4f, 0 viol "
                "incl. EXT3, named 4/4, midband %d/6) -- "
                "summable inflation: R341 (Bellman) is GO"
                % (str(aF),
                   certF[aF][0] if aF is not None else 0.0,
                   certF[aF][3] if aF is not None else 0),
            "GOODTREE_A2_ONLY":
                "the full budget fails at every a in %s (viol "
                "%s) but the GOOD tree certifies at a = %s (C_G "
                "%.4f) -- the two-arm decomposition carries; "
                "heavy hand-off hsh med %.3f"
                % (str(GA_FAM),
                   str([len(certF[a][1]) for a in GA_FAM]),
                   str(aG),
                   certG[aG][0] if aG is not None else 0.0,
                   float(np.median(hsh_col))),
            "LOCAL_INFLATION_SUPERCRITICAL":
                "NEITHER budget certifies (full viol %s, good "
                "viol %s at a in %s) -- log Gamma is not "
                "summable in this language either (e(W_F) "
                "%+.3f, halves %+.3f/%+.3f %s); said honestly"
                % (str([len(certF[a][1]) for a in GA_FAM]),
                   str([len(certG[a][1]) for a in GA_FAM]),
                   str(GA_FAM), e_wf, e_a, e_b,
                   "DECIDED" if decided else "UNDECIDED")}
        verdict_main = "%s(%s)" % (vkey, det_v[vkey])
        check("G70-adjudication", True,
              "exactly one sealed letter fired: %s"
              % verdict_main)
        # bridge (printed ALWAYS, honestly typed)
        if vkey == "DENSITY_MARTINGALE_EXACT":
            C_use = certF[aF][0]
            a_use = aF
            hyp = "full budget CERTIFIED pointwise"
        elif vkey == "GOODTREE_A2_ONLY" and aG is not None:
            C_use = certG[aG][0]
            a_use = aG
            hyp = ("GOOD-tree budget certified; the heavy " +
                   "jumps are the r335 mass-arm hand-off " +
                   "(NOT composed this round)")
        else:
            C_use = max(gb_cols[GA_FAM[-1]])
            a_use = GA_FAM[-1]
            hyp = "NO certifying budget -- envelopes only"
        m_star_l10 = None
        t = math.log(73.0)
        while t < 1e7:
            if t * CRIT_EXP >= math.log(max(C_use, 1e-300)) \
                    + a_use * math.log(t):
                m_star_l10 = t / math.log(10.0)
                break
            t *= 1.02
        ms_txt = ("10^%.1f" % m_star_l10) \
            if m_star_l10 is not None else "NONE"
        info("BRIDGE (%s): via the dictionary E[X_inf^3] <= "
             "W_F <= %.4f (log m)^%d would read M_3 <= %.4f "
             "(log m)^%d / m^2 => N_3 >= m/sqrt(%.4f (log m)^"
             "%d), N_2 >= N_3 (r306 exact chain) => N_2 >= "
             "m^%.3f for all m >= m_0* = %s (m^{%.3f} >= C "
             "(log m)^a) -- vs the r324 MEASURED route m_0* "
             "10^59.6 (+0.172); typed: %s."
             % (hyp, C_use, a_use, C_use, a_use, C_use, a_use,
                N2_EXP_NEED, ms_txt, CRIT_EXP,
                "the full-budget chain is pointwise on the "
                "measured rungs; the ladder-to-m_0* step stays "
                "the disclosed extrapolation hypothesis"
                if vkey == "DENSITY_MARTINGALE_EXACT" else
                "NOT composed -- preparation for R341 only"))
        info("R341 PREPARATION (Bellman / Reverse Holder -- "
             "NOT executed): concrete constants: C_F %s; C_G "
             "%s; R* %.2f (R_ALT %.2f envelopes %s); per-level "
             "Gamma_max med profile %s; hsh med/max %.3f/%.3f; "
             "drift %s (r4c %.3f)."
             % (str({("a%d" % a): round(certF[a][0], 4)
                     for a in GA_FAM}),
                str({("a%d" % a): round(certG[a][0], 4)
                     for a in GA_FAM}),
                R_STAR, R_ALT,
                str({("a%d" % a): round(alt_env[a], 3)
                     for a in GA_FAM}),
                str([round(v, 2) for v in lv_med]),
                float(np.median(hsh_col)), max(hsh_col),
                "PERIOD4_COBOUNDARY" if cobo
                else "NO_PERIOD4_COBOUNDARY", r4c_pool))
        check("G71-bridge", True,
              "bridge printed with explicit constants (C %.4f, "
              "a %d, m_0* %s); the chain to "
              "terminal_positive_main is typed: martingale/"
              "dictionary/anatomy exact, every constant "
              "MEASURED on the finite ladder + EXT3, the "
              "ladder-to-m_0* step an extrapolation hypothesis "
              "-- NO cofinal claim, NO R341 execution"
              % (C_use, a_use, ms_txt))

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    check("G80-e1-child-weight",
          fu_e1brk == Fr(1, 10)
          and abs(mut1_unev - float(Fr(1, 10))) <= TOY_BAR
          and mut1_even <= TOY_BAR,
          "e1 CAUGHT exact: the wrong child weighting (p_c = "
          "1/#children, n(c) dropped) breaks the conditional on "
          "the uneven Fractions toy by EXACTLY 1/10 (float "
          "builder reproduces %.3f; the even toy is blind at "
          "%.1e -- the mutant is only visible on uneven nodes, "
          "of which the live ladder has %d)"
          % (mut1_unev, mut1_even,
             nuneven_tot))
    check("G81-e2-dict-m-power",
          fr_e2brk == Fr(5, 3)
          and abs(dic_toy["d3"] - mut2 - float(Fr(5, 3)))
          <= TOY_BAR,
          "e2 CAUGHT exact: the dictionary with m instead of "
          "m^2 claims E[X_inf^3] == m M_3 = 5/9 on the toy "
          "while the exact value is 20/9 -- break 5/3 EXACT "
          "(Fractions-warded in G41); the exponent 2 is the "
          "cubic scaling of the uniform tree, not a fit")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    g3 = mutant_gamma_from_target(ev9m)
    check("G82-e3-gamma-from-target",
          len(e3_hits) >= 1 and (not sc_own) and g3 >= 0.0,
          "e3 AST-CAUGHT: the 'Gamma column' derived from the "
          "cubic TARGET record is FLAGGED (%s) while the five "
          "module-own tree builders are clean (%d hits) -- "
          "Gamma is local mass algebra, never a target readback "
          "(mutant value %.3e computed only to prove it runs)"
          % (e3_hits[0] if e3_hits else "MISS", len(sc_own), g3))
    toy_off = (0, 1, 1)
    toy_rho = (0.1, 0.9, 0.1)
    off_mut = mutant_tree_posthoc(toy_off, toy_rho, 0.5)
    check("G83-e4-tree-posthoc",
          len(e4_hits) >= 1 and off_mut == 1
          and off_mut != PAIR_OFFSET,
          "e4 protocol-CAUGHT twice: the after-sight pairing "
          "re-pick consumes the evaluated bound column -- "
          "AST-FLAGGED (%s) -- and on the toy returns offset %d "
          "!= the sealed PAIR_OFFSET %d (the genealogy is "
          "adjudicated in Leg 0 and sealed by this SPEC_SHA "
          "BEFORE the freeze)"
          % (e4_hits[0] if e4_hits else "MISS", off_mut,
             PAIR_OFFSET))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact density martingale on the sealed "
          "fold genealogy (mass conservation alone), the exact "
          "moment dictionary E[X_inf^2] == m M_2 / E[X_inf^3] "
          "== m^2 M_3 (the terminal target restated as a "
          "Reverse-Holder problem), the per-level Gamma anatomy "
          "with the good/heavy split and the drift/coboundary "
          "census, and the budget certifications W_F/W_G -- NO "
          "new certificate promoted, NO universal bound claimed "
          "beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R339_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d rho4 bit-near, r324-pre C_M2 "
                 "%.4f viol7 EXACT)"
                 % (rec3_w, C2r, viol2, n339, C_M2)]
        parts.append("SEAL(mart %.1e, unit %.1e, rec %.1e, env "
                     "%.1e, Jensen %.1e, Fractions %s/%d nodes, "
                     "alt tree %.1e, grounding %.1e, purity "
                     "clean, toys exact)"
                     % (mart_w, unit_w, rec_w, env_w, jen_w,
                        "EXACT" if fr_ok else "BROKEN", fr_nodes,
                        max(amart_w, adict_w),
                        max(part_w, l1rec_w, panc_w)))
        parts.append("DICTIONARY(d2 %.1e, d3 %.1e, ymx %.1e)"
                     % (dict2_w, dict3_w, dictq_w))
        parts.append("GAMMA(WF med %.2f max %.2f at kz%d, WG "
                     "med %.2f, hsh med %.3f, deep-half share "
                     "med %.3f, named WF med %.2f, midband WF "
                     "med %.2f, SCR WF %.3f vs med %.3f)"
                     % (float(np.median(wf_col)), max(wf_col),
                        srt_full[int(np.argmax(wf_col))]["kz"],
                        float(np.median(wg_col)),
                        float(np.median(hsh_col)),
                        float(np.median(deep_share)),
                        float(np.median(named_wf)),
                        float(np.median(mb_wf)),
                        scr_ev["dst"]["wf"], wf_med))
        parts.append("DRIFT(%s, r4 %.3f, r4c %.3f, profile "
                     "sum %.4f)"
                     % ("PERIOD4_COBOUNDARY" if cobo
                        else "NO_PERIOD4_COBOUNDARY", r4_pool,
                        r4c_pool, sum(prof)))
        parts.append("CERT(%s minA %s; good %s minA %s; e(WF) "
                     "%+.3f %s, e(WG) %+.3f, e(m2M3) %+.3f)"
                     % ("; ".join("a%d CF %.3f v%d"
                                  % (a, certF[a][0],
                                     len(certF[a][1]))
                                  for a in GA_FAM), str(aF),
                        "; ".join("a%d CG %.3f v%d"
                                  % (a, certG[a][0],
                                     len(certG[a][1]))
                                  for a in GA_FAM), str(aG),
                        e_wf,
                        "DECIDED" if decided else "UNDECIDED",
                        e_wg, e_d3))
        parts.append(verdict_main)
        parts.append("BRIDGE(C %.4f a %d m_0* %s, R341 %s)"
                     % (C_use, a_use, ms_txt,
                        "GO" if vkey == "DENSITY_MARTINGALE_"
                        "EXACT" else "prep only"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the martingale "
          "identity, the moment dictionary, the local anatomy, "
          "the envelope, the Jensen sign, the Fractions toys, "
          "the tree logic and the purity audits (exact / "
          "AST-decided); MEASURED: every census, constant, "
          "violation count and exponent (the finite class "
          "ladder + 12 EXT3 + 2 mains + 2 live controls); OPEN: "
          "any bound beyond the measured rungs, the cofinal "
          "law, the R341 Bellman execution; NO RH claim"
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
