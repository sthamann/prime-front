#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""k2_source_formula_probe --
PRIME.L2.K2_SOURCE_FORMULA.01 (round 355): THE K2 SOURCE FORMULA
-- q_max from a lower gap bound; the reviewer fork after r353.

CONTEXT (binding, from the sealed r353 record SPEC_SHA bd89e331,
SECOND_FAMILY_BUILT + FAB_LAW_BREAKS_ON_B + FLOOR_KILLS +
GREL_LOWER_BOUND_CANDIDATE(0.187, 63.4)): the FAB ceiling is
family-indexed (14.93 -> 18.07), the sliding spike coverage is
FINITE (kills at m ~ 760 on frame B), and the ONE frozen constant
that carries across the aspect change is K2: FAB grel <= 11.87
holds on ALL rows of BOTH construction families (89 frame-A rows
+ 8/8 frame-B rows, max 5.95), with Spearman(grel, FAB | family)
= -0.623 and the first measured gap floor g_min = 0.187 giving
the first non-vacuous implied ceiling 63.4 <= 4 x 18.07.  THE
REVIEWER FORK (verbatim, binding): round 355 goes to the terminal
lane but ONLY on K2 / Klein-gap geometry -- no ad-hoc fourth arm;
a fourth mechanism may only arise if it follows from the SAME gap
geometry.  Goal: a source-pure statement that controls q_max from
a LOWER gap bound -- "the smaller / more special the local gap,
the harder the spike is capped" -- as a theorem candidate with a
cross-family constant, plus the source-side origin of the lower
gap bound itself.

THE CONTRACT (this round): (LEG A) decompose the K2 product
source-side -- WHY does grel carry?  q_max = the relative cubic
mass of the dominant atom; the dominant atom lives in the
Klein-gap zone; the candidate chain
    FAB grel = (m q_max/log m) grel
             <= (ngj/log m) x (hgn grel)     [r327 group chain,
                                              EXACT one-sided]
             <= C_NG x C_H                   [r329 counting census
                                              x THE NEW C_H census
                                              candidate]
with the EXACT construction identity where grel enters: the mesh
D = 0.5 gap/NU makes the half-depth h = NU alpha/gap up to
rounding (h - NU u in (0, 1.5], u := alpha/gap the NU-FREE depth
coordinate) -- the Klein-gap zone has proportionally deeper
windows; every link typed satz / dictionary / census.  The pileup
analog C_P (pil grel) is measured in parallel (chain m pk <= nsc
pil exact; the census link uses nsc_rel, the tail gap disclosed
honestly, r351 convention).  (LEG B) the theorem candidate "for
every admissible zone with grel >= g: FAB <= C_2/g" tested with
the PRE-SEALED constant C_2 = max FAB grel over the 89 sealed
r351 rows (record expectation 11.87, anchor-gated) on: the 8
frame-B rows (regate), the NU TEST (the sealed six zones kz 111/
75/51/65/79/103 of the 89-row surface REBUILT at NU = 2 and NU =
3 -- grel is a ZONE property, NU-free by construction; is C_2
NU-free?), and the FRESH FIELD at the THIRD aspect NU_C = 3 (the
sealed r353-style selection below; the in-zone pool is EXHAUSTED
at every aspect -- 0 members, disclosed up front; the fresh field
is out-of-zone deep rows, said honestly).  (LEG C) the lower gap
bound itself: NO Baker bounds (the r289/r331 METRIC_ONLY lesson);
instead the measured g_min(u) curve over ALL admissible zones
(z^2 <= 400000 domain, aspect-free coordinate u = alpha/gap):
dyadic u bins, per bin min grel, fit-free halves-slope + a sealed
monotonicity fraction -- letters GMIN_FLAT(g_inf) / GMIN_LAW(e_g)
/ GMIN_ERRATIC; at FLAT/LAW the implied ceiling arithmetic FAB <=
C_2/g_min(m) is printed (the m <-> u census map e_um from the 97
admitted rows; the implied growth exponent e_impl = -e_g/e_um vs
CRIT_EXP = 0.224 -- is the gap-floor decay subcritical?).  (LEG
D) the composition: the two-theorem cover retyped (K2 spike
theorem cross-family + the frame-A three-arm cover bounded to its
measured range, r353), the m_0* table under the K2 ceiling
(C_2/g_min x C_M2ENV'), and the cofinal typing: with K2 as the
cross-family law candidate and g_min as the single census rest --
what EXACTLY is still missing.  (LEG E) worlds: K2 census on w9B
/ w13B twin / EPSTEIN; the frame-B SCRAMBLE control at kz80
breaks AT ADMISSION (r353 record, reproduced -- documented).

THE SEALED FRESH-FIELD SELECTION (NU_C = 3, the r353 frameb rule
VERBATIM with the aspect as the only change): USED_C = the r353
extended used ledger (104) UNION the 8 admitted r353 frame-B
anchors (== 112 gated); POOL_C = frameb_pool(NU_C, H_MIN, H_C_CAP
= 4200) under z^2 <= Z2_CAP = 400000 + the N_ATOM_MIN floor;
FRESH_C = POOL_C minus USED_C (== 16 gated); STRATUM CZ (in-zone)
= fresh kz with z inside CORE_Z = [16, 317] sorted by (grel, kz)
ascending, first K_CZ = 2 -- THE CZ QUEUE IS EMPTY (0 members,
exhaustion across aspects disclosed up front); STRATUM CD (depth)
= the remaining fresh sorted by (h, kz) DESCENDING, first K_CD =
5.  Build budget: at most MAX_BUILDS_C = 8 wpack_b calls.
ADMISSION: POSITIVE_PREFIX + chain-complete at build level with
queue replacement; post-eval fold-mult <= 2 + non-degenerate on
the law statistics (census-disclosed, r353 wording).  THE NU-TEST
SET (sealed): NU_TEST_KZ = (111, 75, 51, 65, 79, 103) -- six
zones of the sealed 89-row surface spanning grel 0.40..0.82 and
carrying the K2 extremes (kz111 = the C_FAB anchor; kz75 = the
floor anchor; kz51 = the EXT3-B FAB maximum; kz65/79/103 = EXT5)
-- rebuilt at NU in (2, 3) (12 builds; the NU = 4 columns come
from the 89-row surface itself); admission as above, failures
census.  NU-completeness (sealed): >= NUT_MIN = 9 of 12 admitted
AND >= NUT_PER_NU_MIN = 4 per aspect.

THE FOUR SEALED LETTERS:
  MAIN (exactly one, total order): TARGET_LEAK iff any purity/
      scope/literal audit hit on the module-own builders;
      LAW_STATE_NOT_EXACT iff an exact ward breaks on a live
      world (identity/chain/mesh/decomposition wards, Fractions
      pins, toys, the NU = 4 reproduction ward);
      K2_FAMILY_INDEXED iff any admitted test row (frame-B regate
      + NU-test + fresh field) has FAB grel > C_2 + K2_EPS (the
      gap language is census too -- said honestly);
      K2_LAW_CERTIFIED_NU_FREE iff 0 violations AND the NU test
      is complete AND >= FRESH_MIN_C = 2 fresh rows admitted;
      K2_HOLDS_CENSUS otherwise (0 violations, thin surface).
  SOURCE (exactly one): K2_SOURCE_FORMULA_DERIVED iff the exact
      chain wards are green AND at least one census cap carries:
      (C_H test 0 violations AND C_NG C_H <= IMPL_FAC x max
      measured FAB grel) OR (C_P test 0 violations AND C_NSC C_P
      <= IMPL_FAC x max FAB grel) -- the non-vacuity rule is
      a-priori (QGL IMPL_FAC = 4.0 verbatim);
      K2_SOURCE_CHAIN_OPEN otherwise (the failing link named).
  GMIN (exactly one): GMIN_FLAT(g_inf) iff |e_g| <= E_FLAT_G =
      0.05; GMIN_LAW(e_g) iff e_g < -E_FLAT_G AND mono_frac >=
      MONO_BAR = 0.75; GMIN_ERRATIC otherwise.
  EXTRA FLAGS: +INZONE_EXHAUSTED_ALL_NU(0) / +K2_TEST_MAX(kz,
      nu, val) / +CH_CANDIDATE(C_H, implied) / +CP_CANDIDATE /
      +GMIN_IMPLIED(m_0*, e_impl) / +NU_RATIO_CENSUS(med).

LEG 0 -- ANCHOR REGRESSION (bit-near; the COMPLETE r351 + r353
record surfaces through the same code path): the r314 identity
wards (ladder/EXT3/EXT4/EXT5/frame-B bars verbatim + the a-priori
NU-row bars); r306 C_2 = 1.069 first-5 freeze 0/57; r316 rho
anchors + C_small + n = 65; the dictionary-chain identity; the
r321 F_A top-3; THE r349 FAMILY + EXT4 RECORDS; THE r329 COUNTING
RECORD; THE r324 DIRECT RECORD; THE r351 GROWTH + FLOOR RECORDS
(C_FAB 14.93 @ kz111, C_K2(83) 11.87, min RSV 1.07 @ kz75, C_M2ENV
26.01, m_0* 10^18.9, count reserves 1.59/2.77); THE r353 FRAME-B
RECORD (the sealed selection re-executed: used 104 / fresh 24 /
BZ (69, 80) / BD head (133, 129, 124, 117, 107, 101); the 8-row
table FAB/grel bit-near: kz124 18.07/0.329, kz117 17.78/0.329,
kz133 14.33/0.337, kz129 10.43/0.337, kz107 8.39/0.318, kz69
6.94/0.187, kz80 4.91/0.408, kz101 4.09/0.340; C_K2X 11.87 with
frame-B max 5.95; g_min 0.187 -> implied 63.4; C_M2ENV' 44.18;
two-family m_0* 10^20.5; count reserves 1.61/2.79).

LEG E MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) THE CAP FUNCTION h(grel) READ BACK FROM THE SEEN COLUMN
  (protocol): mutant_hfun_posthoc returns the per-zone cap column
  rho_i/grel_i (consumes rho) -- the BOUND_FORBIDDEN scope audit
  must FLAG it AND on the sealed toy (rho (2.0, 1.0), grel (0.5,
  1.0)) it returns (4.0, 1.0) != the sealed constant-over-grel
  rule column (2.0, 1.0) at the toy constant 1.0 --
  protocol-CAUGHT twice.
(e2) C_2 AFTER SIGHT (protocol): mutant_c2_posthoc sets the K2
  constant at the seen violation maximum (consumes rho) --
  AST-FLAGGED AND on the sealed toy (rho (3.0, 2.0), grel (1.0,
  0.5)) it returns 3.0 != the sealed toy freeze 1.0 --
  protocol-CAUGHT twice.
(e3) NU TEST CONTAMINATED WITH SHARED ZONE DATA (protocol):
  mutant_nu_shared returns the NU = 4 column verbatim as the
  'NU = 2 measurement' (consumes rho) -- AST-FLAGGED AND on the
  sealed toy it returns (1.0, 2.0) != the fresh-build toy column
  (0.9, 1.8); the LIVE freshness ward demands N(NU2) < N(NU3) <
  N(NU4) strictly on every admitted NU-test zone (a shared column
  cannot pass) -- protocol-CAUGHT twice.
(e4) IDENTITY WARD WITH THE WRONG LOG POWER: mutant_fab_wrong_log
  claims FAB = m pk/lg^2 -- on the sealed Fractions toy (m = 3,
  pk = 1/2, pseudo-log lg = 2) it returns 3/8 while the exact FAB
  is 3/4 -- break factor == lg == 2 EXACT.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: a parallel worker updates rh/problem/lstar_problem.tex
(L* memo) -- NO shared files except the strictly additive rh-sync
surfaces (git pull before the sync, append-only).  Two-commit
freeze protocol (r329 convention): spec committed pre-freeze,
record tables the only post-freeze edit, committed again.

THE OBJECT (r269/r287/r298/r306/r314/r316/r317/r321/r324/r327/
r329/r339/r343/r344/r346/r349/r351/r353 machinery imported
verbatim; the r351 census/controls/extensions/EXT3/EXT4/EXT5
scaffold AND the r353 frame-B family are re-executed through the
same code path and anchor-gated against the r351/r353 records):
t_{N-2} = sum_b ct_b; F = 0.20 edge split; level-2 blocks; the
r306 RY3 layer; the r314 SCF layer; the r316 TRB layer; the r317
EFP.local_ratio; the r321 CCP layers; the r324 QMO + FAP layers;
the r327 GMC layer (group_mass_ledger + heavy_state -- the mass
mechanics of the chain); the r329 EFA layers (grel_col, gap_class,
used_kz_set); the r343 PC343 domain constants; the r339 FDD
dictionary; the r349 TSL.res_decomp; the r351 QGL.fab_of +
constants; the r353 SFE.window_data_b + SFE.wpack_b +
SFE.frameb_pool + SFE.frameb_select (the NU-parametrized
construction, reused VERBATIM for the frame-B regate, the NU test
and the NU_C fresh field) -- ALL imported verbatim and
SPEC_SHA-prefix gated (SFE bd89e331, QGL 67102e4c, TSL 9b593e63,
EFA bbfaf199, PC343 9ffc2705).  NEW in this round (module-own,
source-pure): mesh_h (the EXACT mesh identity h = NU u + rounding
in (0, 1.5], warded against frameb_pool on every pool zone),
gmin_bins (dyadic u binning, min per bin, declared floor count),
gmin_letter_rule + k2_main_tree + k2_source_letter (the sealed
trees).  FAB, grel products, hgn, pil, nsc, ngj, D and every
census on them are TARGET-SIDE DIAGNOSTICS computed in the gate
section (r321/r349/r351/r353 convention, disclosed) -- the
module-own builders consume the source grid, window shape and
SEALED thresholds only.

INDEX FIREWALL (binding, r238-r354 discipline): w = window (kz),
N_w = builder depth; ground truth enters GATES and census tables
only; the cubic target M_3/rho_2 and the q_max RECORD enter GATES
/ anchors / census tables / diagnostics only, NEVER a law or
selection builder (AST-warded); no zero/prime oracles anywhere
(AST firewall; the prime-power anchor grid U_ALL/G_ALL is the
sealed source comb, r238 convention); no fit primitives (fragment
audit; exponents are the imported r272 dyadic halves-slope,
fit-free; Spearman is the imported r321 rank correlation).
B PROVENANCE: B_w = S_{N-2} + 5/7 (imported floor, never fitted).
COFINAL LADDER (pre-sealed, r316/r324/r329/r343/r349/r351/r353
verbatim): frame-A h <= 900, 42 rungs, (N, kz)-sorted; exception
set {kz15, 20, 22, 36, 38, 39, 52}; EXTENSION 900 < h <= 1300
first 15; EXT2 r316 A5 rule; EXT3 = the sealed r329 12-anchor
list; EXT4 = the sealed r343/r345 6-anchor list; EXT5 = the
sealed r351 6-anchor list; FRAME-B = the sealed r353 rule
re-executed; NU-TEST + FRESH FIELD = THIS round's sealed rules
above.

SEALED CONSTANTS (everything not listed here is the r353 constant
set imported verbatim from SFE/QGL/TSL/FTS/FCC/EFA/PC343):
NU_TEST_KZ (111, 75, 51, 65, 79, 103); NU_TEST_NUS (2, 3);
NUT_MIN 9; NUT_PER_NU_MIN 4; NU_C 3; H_C_CAP 4200; K_CZ 2; K_CD
5; MAX_BUILDS_C 8; FRESH_MIN_C 2; USED_EXPECT_C 112;
FRESH_EXPECT_C 16; CZQ_EXPECT () EMPTY; CDQ_EXPECT (99, 115, 89,
86, 132); TB_WARD_BAR_C 1e-3 + REC3_BAR_C 1e-11 (the r353
frame-B a-priori bars adopted: every new depth 1291..3805 stays
below the r353 frame-B record depth 3972); MESH_DEV_HI 1.5 (the
exact rounding budget: ceil + 1 + even-rounding over the mesh D);
K2_EPS 1e-9; E_FLAT_G 0.05; MONO_BAR 0.75; MIN_ZONES_BIN 5;
IMPL_FAC = QGL 4.0; C_2 freeze rule = max FAB grel over the 89
sealed r351 rows; C_H freeze rule = max hgn grel over the same
89; C_P freeze rule = max pil grel over the same 89 (both columns
NEVER measured by any sealed record); R353 record anchors (tol):
frame-B table FAB tol 0.02 / grel tol 0.003 (the 8-row list
above); C_K2X 11.87 tol 0.02; frame-B K2 max 5.95 tol 0.02; g_min
0.187 tol 0.003; implied 63.4 tol 0.3; C_M2ENV' 44.18 tol 0.02;
two-family m_0* 20.5 tol 0.1; count reserves (1.61, 2.79) tol
0.05; R355_TABLE_LITERALS = the sealed r314..r353 set (SFE
verbatim) UNION the r353 record set {18.07, 17.78, 63.4, 44.18,
20.5, 5.95} (collision-prone small values 0.63, 0.95, 1.61, 2.79,
0.187, 2.91 curated OUT, r337..r353 convention, disclosed);
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the exact w9 wards + the Fractions pins + the frame-B
construction ward (w9 at NU = 4 + NU_B) + the mesh toy + w9-zone
mesh ward + the SELECTION ENUMERATION (frame-B regate queues +
NU_C pool counts + queues, no deep wpack) + e1-e4 mutants;
ladder, extensions, EXT3-5, frame-B evaluation, NU builds, curve,
records, composition and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306..r353 RECORD number adopted as-is; the
chain algebra (group chain, pileup chain, FAB identity, mesh
identity) is DERIVED from the sealed r324/r327/r351 records
(disclosed above); ONE SCOPING PASS (sizing only, r329/r343/r351/
r353 precedent) enumerated the selection surface and timed the
budget: the NU_C = 3 pool under z^2 <= 400000 at h <= 4200 has
115 members, 16 fresh under the extended 112-ledger, IN-ZONE
EMPTY at every aspect tried (NU 2 at h <= 6000: 16 fresh, 0
in-zone; NU 3 at h <= 4200/5000: 16 fresh, 0 in-zone -- the
in-zone exhaustion is aspect-independent, said out loud); the CD
queue head (99, 115, 89, 86, 132) at h 2961..3805 with queue
grels 0.325..0.668 disclosed as selection-side data; the NU-test
depths kz111/75/51/65/79/103 = h(NU2) 861..1591 / h(NU3)
1291..2386; two admission builds timed (kz99 NU3 N 3805 nf None
chain-complete 50.7 s, kz111 NU2 N 1514 nf None 1.6 s -- 17
builds + replacements feasible); NO bound value, rho, F_A, FAB,
grel product, hgn, pil, count or curve column of ANY window was
computed by the scoping pass (the two nf values are
admission-side data, disclosed exactly as the r351/r353 scoping
did).  GENUINELY OPEN: every hgn grel / pil grel value (the C_H /
C_P freezes and their non-vacuity -- these columns were never
printed by any sealed record), every NU = 2 / NU = 3 FAB and K2
column, the NU-test and fresh-field admission censuses, the
whole g_min(u) curve (bins, slope, monotonicity, letter -- never
computed; the scoping saw only the queue-head grels of 16 fresh
zones + the 6 NU-test zone grels), the m <-> u census map, the
implied exponent e_impl, and every composed number; the sealed
toys are computed BY HAND (K2 chain Fractions pin: m 4, pk 1/2,
lg 2, grel 1/2, ngj 2, hgn 1 -> FABg 1/2 == bound 1/2 EXACT, and
hgn 2 -> bound 1 with slack 1/2 EXACT; mesh toy alpha 10, gap 1,
nu 2 -> h 21, h - nu u = 1.0 <= 1.5; gmin toy A u (2, 3, 4, 5, 8,
9, 10, 11) g (.8, .7, .9, .6, .4, .5, .45, .35) -> bins mins
(.7, .6, .35), mono 1.0, slope -0.4407 -> GMIN_LAW; toy B g (.4,
.7, .9, .6, .9, .5, .95, .35) -> mins (.4, .6, .35), mono 0.5 ->
GMIN_ERRATIC; toy C g (.5, .6, .5, .7, .5, .6, .5, .6) -> mins
(.5, .5, .5), slope 0 -> GMIN_FLAT; e1 pin (4.0, 1.0) vs (2.0,
1.0); e2 pin 3.0 vs 1.0; e3 pin (1.0, 2.0) vs (0.9, 1.8); e4 pin
3/8 vs 3/4 break 2; the five main branches, the two source
branches and the three gmin branches EXACT); NUT_MIN,
NUT_PER_NU_MIN, H_C_CAP, K_CZ, K_CD, MAX_BUILDS_C, FRESH_MIN_C,
TB_WARD_BAR_C, REC3_BAR_C, E_FLAT_G, MONO_BAR, MIN_ZONES_BIN and
K2_EPS are coarse a-priori choices sized BEFORE any evaluation;
the letters are symmetric and total by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R355_ANCHORS(identity wards, r306 C_2, r316, dictionary, r321
    F_A top-3, THE r349 FAMILY + EXT4 RECORDS, THE r324 DIRECT
    RECORD, THE r329 COUNTING RECORD, THE r351 GROWTH + FLOOR
    RECORDS, THE r353 FRAME-B RECORD)
+ SEAL(purity + toys + the exact live wards: NORM identity, r324
    identity, FAB identity, decomposition, pileup chain, group
    chain, K2 chain, MESH identity, Fractions pins, the frame-B
    NU = 4 reproduction ward, the NU freshness ward)
+ K2ANATOMY(the chain table + the C_H/C_P freezes + typing)
+ K2LAW(the frozen C_2 test on frame-B regate + NU test + fresh
    field + the NU-free adjudication)
+ GMIN(the g_min(u) curve + the sealed letter + the implied
    arithmetic)
+ [exactly one of] K2_LAW_CERTIFIED_NU_FREE / K2_HOLDS_CENSUS /
    K2_FAMILY_INDEXED / LAW_STATE_NOT_EXACT / TARGET_LEAK
    [+ SOURCE letter + GMIN letter + flags]
+ COMPOSITION(the m_0* table + the two-theorem cover + the
    cofinal typing)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the identity, the chains, the mesh
identity, the Fractions toys, the NU = 4 reproduction and the
purity audits are EXACT (Fractions/AST-decided); every constant,
FAB value, grel product, count column and violation count is
MEASURED on the finite 89-row r351 surface + the 8 r353 frame-B
rows + the admitted NU rows only; the NU test buys independence
of the window ASPECT on six zones -- it is NOT a second
arithmetic world and NOT a cofinal statement; the g_min(u) curve
is a MEASURED census over the finite source grid -- the
diophantine lower-bound question (distances of prime-power
logarithms) stays OPEN mathematics, typed census by contract; the
in-zone fresh pool is exhausted at every aspect, so the fresh
field tests the out-of-zone deep regime only (said out loud); a
certified K2 law fixes a LAW CANDIDATE with frozen census
constants -- it proves NO cofinal law; r243-r354 stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA b0dd5a93a9d5b790,
pre-freeze commit 94f0683a; protocol: smoke pass 1 = 47/47
(0.8 s, run pre-commit, disclosed in the commit message);
calibration pass 1 = FIRST full evaluation = 47/47, wall
816.8 s, NO amendment -- no bar, band, rule or verdict rule
moved at any point; record run1/run2 after this insertion,
identical up to the runtime line):
MAIN VERDICT: K2_LAW_CERTIFIED_NU_FREE(0 violations at the
frozen C_2 = 11.87 on 8 frame-B + 12 NU-test + 5 fresh rows)
+ K2_SOURCE_CHAIN_OPEN(caps vacuous: C_NG C_H 373.4 / C_NSC
C_P 286.7 vs bar 4 x 11.87 = 47.5) + GMIN_LAW(e_g -0.252,
mono 0.80) + INZONE_EXHAUSTED_ALL_NU(0) + K2_TEST_MAX(kz103,
NU3, 10.62) + GMIN_IMPLIED(NONE, e_impl +0.29) +
NU_RATIO_CENSUS(med 0.19).
THE HEADLINE FINDINGS:
(1) K2 SURVIVES ITS SECOND INDEPENDENCE TEST -- THE ASPECT
CHANGE: the frozen C_2 = 11.87 holds with ZERO violations on
all 25 test rows (the 8-row frame-B regate + 12/12 admitted
NU-test rebuilds at NU 2/3 + the 5/5 fresh NU = 3 field kz99/
115/89/86/132, N_w 2961..3805, 0 queue failures, 0 post-eval
drops); the NU test is COMPLETE (12/12 vs bars 9/4/2), so the
sealed letter K2_LAW_CERTIFIED_NU_FREE fires: the Klein-gap
product is stable across BOTH construction families AND all
three window aspects ever built.  The closest call is kz103
at NU 3: FABg 10.62 = 11 pct below the ceiling (census, said
out loud).
(2) THE CENSUS CONTRAST THAT MAKES (1) MEANINGFUL: the FAB
coordinate itself is aspect-WILD -- kz99 (NU3, fresh) posts
FAB 19.38, a NEW lane record above the r353 18.07, and kz103
jumps 3.69 (NU4) -> 12.98 (NU3) while kz111 collapses 14.93
(NU4) -> 1.00 (NU2); the median FAB(NU2)/FAB(NU4) ratio on
the test zones is 0.19.  The K2 product ABSORBS this: max
FABg over every row of the round stays 11.87 (kz111, NU4).
The reviewer hope is now measured content: the gap product is
the aspect-stable coordinate of the lane, the bare FAB
ceiling is C(NU, family) census.
(3) THE SOURCE CHAIN CLOSES EXACTLY -- ITS CENSUS CAPS ARE
VACUOUS (typed honestly): FAB grel <= (ngj/lg) x (hgn grel)
holds one-sided EXACT on all 118 live worlds (K2 chain ward
0.0e+00) and the mesh identity h - NU u in (0, 1.5] is EXACT
on (114, 115, 112) pool zones at NU (2, 3, 4) -- WHERE grel
enters is now satz-grade construction algebra (the Klein gap
sets the mesh, u = alpha/gap is the NU-free depth
coordinate).  BUT the frozen caps C_H = max hgn grel = 141.71
and C_P = max pil grel = 141.53 (both at kz111) give implied
ceilings 373.4 / 286.7 >> the a-priori bar 47.5 (they DO hold
0-violation on all 25 test rows -- but vacuously):
K2_SOURCE_CHAIN_OPEN -- the r351 K3/K4 vacuity repeats at the
grel-sharpened caps; the chain loses too much at the
heavy-group step (bshare med 0.59 family / 0.41 all: the
heavy group is NOT the whole block off-family).  The counting
side holds AGAIN: nsc_rel/lg <= 2.0258 and ngj/lg <= 2.6351
on all 17 NU rows (min reserves 1.35/1.81) -- FIFTH fresh
cohort, FIRST aspect test: still the most robust asset.
(4) THE g_min(u) CURVE IS A SLOW LAW -- BUT SUPERCRITICAL AS
A CEILING ROUTE: 6 dyadic bins over the 130 admissible zones
(u 32..2035), bin minima 0.482 / 0.396 / 0.500 / 0.408 /
0.282 / 0.187, mono frac 0.80 >= 0.75, halves-slope e_g =
-0.252 -> GMIN_LAW: the measured gap floor falls like
roughly u^(-1/4), NOT erratically -- the first structured
statement about the lower gap bound (census; the depth-gap
coupling h = NU u partly builds this in, disclosed).  The
implied arithmetic: e_um = +0.883 (m tracks u on the 114
admitted rows), e_impl = -e_g/e_um = +0.286 > CRIT_EXP 0.224
-- IF the census slope were a law the K2 ceiling C_2/g_min(m)
would grow SUPERCRITICALLY: the growing-law m_0* is NONE; the
flat-floor route at the global pool floor 0.187 (kz69) gives
C_FAB^K2 = 63.4 and m_0* = 10^23.5 -- 3 decades WORSE than
the r353 direct census 10^20.5.  The K2 detour needs a
genuinely diophantine floor (or a subcritical g_min law),
not the measured envelope.
(5) THE COFINAL TYPING: SATZ links = r324 identity, r327
group chain, mesh identity, dictionary q_max; CENSUS links =
C_NG (5 cohorts), C_H/C_P (vacuous), C_2 (frozen, 0 viol
over 2 families + 3 aspects), g_min (GMIN_LAW census) -- the
whole spike mechanism now reduces to the census-to-law
promotion of [gap floor] x [counting] x [heavy-group mass],
with the gap floor as the named diophantine rest.
(6) WORLDS (census, no letter): w9B FABg 0.74 / w13B twin
1.35 / EPSTEIN 0.41 -- far below every ceiling; the frame-B
SCRAMBLE control at kz80 (seed 1) BREAKS AT ADMISSION (nf 3,
the r353 record reproduced).
THE NU TABLE (kz grel | FAB @ NU2/NU3/NU4 | FABg @
NU2/NU3/NU4): kz111 0.795 | 1.00/2.89/14.93 |
0.80/2.30/11.87; kz75 0.402 | 2.41/3.29/12.35 |
0.97/1.32/4.96; kz51 0.408 | 1.16/1.07/7.44 |
0.47/0.43/3.04; kz65 0.444 | 0.97/2.08/5.48 |
0.43/0.92/2.43; kz79 0.809 | 3.06/1.14/9.00 |
2.48/0.92/7.29; kz103 0.818 | 0.90/12.98/3.69 |
0.74/10.62/3.02.  THE FRESH NU3 FIELD (kz z N_w m grel |
FAB FABg): kz99 421 3805 779 0.325 | 19.38 6.30; kz115 509
3183 675 0.505 | 6.89 3.48; kz89 359 3178 625 0.353 | 8.57
3.02; kz86 347 3054 630 0.352 | 4.54 1.60; kz132 613 2961
597 0.668 | 5.45 3.64.
ANCHORS bit-near: r314 identity 4.5e-17 ladder / 7.5e-17
frame-B / 1.7e-16 NU rows; r306 C_2 1.069 (0/57); r316 n 65
+ quartet + C_small @ kz18; dictionary 7.8e-16; r321 F_A
top-3 2.47/2.39/2.38; THE r349 FAMILY + EXT4 RECORDS EXACT;
THE r324 DIRECT RECORD (C_INF 1.7481, violators {53, 61, 67,
76, 83}, e_G +0.158); THE r329 COUNTING RECORD (C_NSC 2.0258
/ C_NG 2.6351, EXT3 reserves 1.58/1.82); THE r351 GROWTH +
FLOOR RECORDS (C_FAB 14.93 @ kz111, EXT5 max 9.71 @ kz135,
kz79 F_ins 6.69, rc_small +0.243, 28 fam rows, min RSV 1.07
@ kz75, e_RSV -0.649, rc_fam -0.600, C_M2ENV 26.01, m_0*
10^18.9, C_K2(83) 11.87, rc_gap -0.623, reserves 1.59/2.77);
THE r353 FRAME-B RECORD (8/8 re-admitted, 0 queue failures,
FAB/grel table within tol, C_K2X 11.87, frame-B K2 max 5.95,
g_min 0.187 -> implied 63.4, C_M2ENV' 44.18, m_0* 10^20.5,
reserves 1.61/2.79) -- ALL within tol.
SEAL: NORM 9.0e-16, interpolation 0.0, FAB identity 2.0e-16,
pileup/group chains 0.0, K2 chain 0.0e+00, decomposition
1.0e-15, r316 chain 1.0e-15, mesh identity EXACT (114, 115,
112) zones + toy dev 1.0, NU = 4 reproduction 0.0 EXACT +
pool 70/70, NU freshness strict on 12 admitted test rows,
contribution ward NU rows 1.6e-12 (a-priori bar 1e-3),
purity clean (0 id + 0 literal hits on the five module-own
builders), toys exact (K2 chain pin 1/2 == 1/2 + slack 1/2,
mesh 1.0 <= 1.5, gmin LAW/ERRATIC/FLAT with slope pin
-0.4407, trees 5/5 + 2/2 + 3/3, e1 (4.0, 1.0) vs (2.0,
1.0), e2 3.0 vs 1.0, e3 (1.0, 2.0) vs (0.9, 1.8), e4 3/8 vs
3/4 break 2).  Must-fails: e1 protocol-CAUGHT twice (AST
rho@777 + toy) / e2 protocol-CAUGHT twice / e3
protocol-CAUGHT twice + the live freshness ward / e4 CAUGHT
exact (break == 2) + m5a/m5b FLAGGED.  Runtime 816.8 s
calibration / record run1/run2 identical up to WALL / 0.8 s
smoke.  AMENDMENTS AFTER FREEZE: NONE except this
record-table insertion.

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
import exception_families_probe as EFP         # noqa: E402 r317
import continuous_coordinate_probe as CCP      # noqa: E402 r321
import fa_provenance_probe as FAP              # noqa: E402 r324-pre
import qmax_m2_origin_probe as QMO             # noqa: E402 r324
import group_mass_cap_probe as GMC             # noqa: E402 r327
import companion_orbit_packing_probe as COP    # noqa: E402 r333
import ext3_fresh_anchors_probe as EFA         # noqa: E402 r329
import fold_density_dictionary_probe as FDD    # noqa: E402 r339
import fold_two_scale_balance_probe as FTS     # noqa: E402 r344
import fold_cover_canonization_probe as FCC    # noqa: E402 r346
import thirdarm_spike_law_probe as TSL         # noqa: E402 r349
import pair_coupling_probe as PC343            # noqa: E402 r343
import qmax_growth_law_probe as QGL            # noqa: E402 r351
import second_family_erosion_probe as SFE      # noqa: E402 r353
import lstar_margin_scaling_probe as LM        # noqa: E402 r286 READ-ONLY
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

# ---------------- the r351/r353 constant set, imported verbatim
MAIN_WINDOWS = FTS.MAIN_WINDOWS
CTRL_FLIPS = FTS.CTRL_FLIPS
H_CAP = FTS.H_CAP
CHEAP_EXPECT = FTS.CHEAP_EXPECT
EXC_KZ_EXPECT = FTS.EXC_KZ_EXPECT
TB_WARD_BAR = FTS.TB_WARD_BAR
TB_WARD_BAR_DEEP = FTS.TB_WARD_BAR_DEEP
TB_WARD_BAR_X3 = FTS.TB_WARD_BAR_X3
TB_WARD_BAR_CTRL = FTS.TB_WARD_BAR_CTRL
DEEP_N = FTS.DEEP_N
ID_BAR = FTS.ID_BAR
AC_BAR = FTS.AC_BAR
EXT_H_MAX = FTS.EXT_H_MAX
K_EXT = FTS.K_EXT
EXT_NW_EXPECT = FTS.EXT_NW_EXPECT
EXT2_H_MAX = FTS.EXT2_H_MAX
EXT2_POOL_CAP = FTS.EXT2_POOL_CAP
K_EXT2 = FTS.K_EXT2
EXT3_KZ_B = FTS.EXT3_KZ_B
EXT3_KZ_A = FTS.EXT3_KZ_A
EXT3_NW_MIN = FTS.EXT3_NW_MIN
EXT3_NW_MAX = FTS.EXT3_NW_MAX
ATOM_BAR = FTS.ATOM_BAR
REC3_BAR = FTS.REC3_BAR
REC3_BAR_X3 = FTS.REC3_BAR_X3
TEL_BAR = FTS.TEL_BAR
BND_BAR = FTS.BND_BAR
CHAIN_BAR = FTS.CHAIN_BAR
SA_BAR = FTS.SA_BAR
DICT_BAR = FTS.DICT_BAR
DEG_FLOOR = FTS.DEG_FLOOR
MULT_CAP = FTS.MULT_CAP
N_CAL = FTS.N_CAL
GSQ_R321 = FTS.GSQ_R321
TOY_BAR = FTS.TOY_BAR
EDGE_F = FTS.EDGE_F
CRIT_EXP = FTS.CRIT_EXP
R306_C2 = FTS.R306_C2
R306_C2_TOL = FTS.R306_C2_TOL
N355_REF = FTS.N344_REF
R316_RHO = FTS.R316_RHO
R316_RHO_TOL = FTS.R316_RHO_TOL
R316_CSMALL = FTS.R316_CSMALL
R316_CSMALL_TOL = FTS.R316_CSMALL_TOL
R316_CSMALL_KZ = FTS.R316_CSMALL_KZ
R321_FA_TOP = FTS.R321_FA_TOP
R321_FA_TOL = FTS.R321_FA_TOL
F0_SPLIT = TSL.F0_SPLIT
EXT4_KZ = TSL.EXT4_KZ
EXT4_NW_MIN = TSL.EXT4_NW_MIN
EXT4_NW_MAX = TSL.EXT4_NW_MAX
TB_WARD_BAR_X4 = TSL.TB_WARD_BAR_X4
REC3_BAR_X4 = TSL.REC3_BAR_X4
DEC_BAR = TSL.DEC_BAR
TB_WARD_BAR_X5 = QGL.TB_WARD_BAR_X5
REC3_BAR_X5 = QGL.REC3_BAR_X5
IMPL_FAC = QGL.IMPL_FAC
FAB_ID_BAR = QGL.FAB_ID_BAR
GRP_CHAIN_BAR = QGL.GRP_CHAIN_BAR
FROZEN_CNSC = EFA.FROZEN_CNSC
FROZEN_CNG = EFA.FROZEN_CNG
# the r349 record anchors (QGL verbatim)
R349_FAM_N = QGL.R349_FAM_N
R349_RSV_TRIPLE = QGL.R349_RSV_TRIPLE
R349_RSV_TOL = QGL.R349_RSV_TOL
R349_RC_FAM = QGL.R349_RC_FAM
R349_RC_TOL = QGL.R349_RC_TOL
R349_D_FAM_MED = QGL.R349_D_FAM_MED
R349_D_FAM_MAX = QGL.R349_D_FAM_MAX
R349_D_QUIET = QGL.R349_D_QUIET
R349_D_TOL = QGL.R349_D_TOL
R349_DPKB2 = QGL.R349_DPKB2
R349_DPKB2_TOL = QGL.R349_DPKB2_TOL
R349_SHARES = QGL.R349_SHARES
R349_SHARES_TOL = QGL.R349_SHARES_TOL
R349_X4_FINS = QGL.R349_X4_FINS
R349_X4_FINS_TOL = QGL.R349_X4_FINS_TOL
R349_X4_HOLES = QGL.R349_X4_HOLES
R349_X4_HOLE_TOL = QGL.R349_X4_HOLE_TOL
R324_CINF_REF = QGL.R324_CINF_REF
R324_CINF_TOL = QGL.R324_CINF_TOL
R324_VINF_SET = QGL.R324_VINF_SET
R324_EG_REF = QGL.R324_EG_REF
R324_EG_TOL = QGL.R324_EG_TOL
R329_X3_RSVC_MIN = QGL.R329_X3_RSVC_MIN
R329_X3_RSVD_MIN = QGL.R329_X3_RSVD_MIN
R329_X3_RSV_TOL = QGL.R329_X3_RSV_TOL
# the r353 frame-B machinery + constants (SFE verbatim)
NU_B = SFE.NU_B
NU_A = core.NU_MAIN
H_B_CAP = SFE.H_B_CAP
Z2_CAP = SFE.Z2_CAP
K_BZ = SFE.K_BZ
K_BD = SFE.K_BD
CORE_Z = SFE.CORE_Z
USED_EXPECT_B = SFE.USED_EXPECT_B
FRESH_EXPECT_B = SFE.FRESH_EXPECT_B
BZQ_EXPECT = SFE.BZQ_EXPECT
BDQ_HEAD_EXPECT = SFE.BDQ_HEAD_EXPECT
MAX_BUILDS_B = SFE.MAX_BUILDS_B
TB_WARD_BAR_B = SFE.TB_WARD_BAR_B
REC3_BAR_B = SFE.REC3_BAR_B
FRB_WARD_BAR = SFE.FRB_WARD_BAR
SCR_SEED_B = SFE.SCR_SEED_B
LM_RANKS_USED = EFA.LM_RANKS_USED
EXT5_KZ_B = SFE.EXT5_KZ_B
EXT5_KZ_A = SFE.EXT5_KZ_A
EXT5_NW_MIN = SFE.EXT5_NW_MIN
EXT5_NW_MAX = SFE.EXT5_NW_MAX
# the r351 record anchors (SFE verbatim)
R351_CFAB = SFE.R351_CFAB
R351_CFAB_KZ = SFE.R351_CFAB_KZ
R351_CFAB_TOL = SFE.R351_CFAB_TOL
R351_X5_FABMAX = SFE.R351_X5_FABMAX
R351_X5_FABMAX_KZ = SFE.R351_X5_FABMAX_KZ
R351_X5_FINS79 = SFE.R351_X5_FINS79
R351_X5_FINS_TOL = SFE.R351_X5_FINS_TOL
R351_FAM_N = SFE.R351_FAM_N
R351_MINRSV = SFE.R351_MINRSV
R351_MINRSV_KZ = SFE.R351_MINRSV_KZ
R351_MINRSV_TOL = SFE.R351_MINRSV_TOL
R351_ERSV = SFE.R351_ERSV
R351_RCFAM = SFE.R351_RCFAM
R351_SLOPE_TOL = SFE.R351_SLOPE_TOL
R351_X5_RSV_LO = SFE.R351_X5_RSV_LO
R351_X5_RSV_HI = SFE.R351_X5_RSV_HI
R351_X5_RSV_TOL = SFE.R351_X5_RSV_TOL
R351_M2ENV = SFE.R351_M2ENV
R351_M2ENV_TOL = SFE.R351_M2ENV_TOL
R351_M0LAW = SFE.R351_M0LAW
R351_M0LAW_TOL = SFE.R351_M0LAW_TOL
R351_CK2_83 = SFE.R351_CK2_83
R351_CK2_TOL = SFE.R351_CK2_TOL
R351_RCGAP = SFE.R351_RCGAP
R351_CNT_RES = SFE.R351_CNT_RES
R351_CNT_RES_TOL = SFE.R351_CNT_RES_TOL
R351_RC_SMALL = SFE.R351_RC_SMALL

# ---------------- NEW sealed constants of this round (spec above)
NU_TEST_KZ = (111, 75, 51, 65, 79, 103)
NU_TEST_NUS = (2, 3)
NUT_MIN = 9
NUT_PER_NU_MIN = 4
NU_C = 3
H_C_CAP = 4200
K_CZ = 2
K_CD = 5
MAX_BUILDS_C = 8
FRESH_MIN_C = 2
USED_EXPECT_C = 112
FRESH_EXPECT_C = 16
CZQ_EXPECT = ()
CDQ_EXPECT = (99, 115, 89, 86, 132)
FRAMEB_KZ = (69, 80, 133, 129, 124, 117, 107, 101)
TB_WARD_BAR_C = 1e-3
REC3_BAR_C = 1e-11
MESH_DEV_HI = 1.5
K2_EPS = 1e-9
E_FLAT_G = 0.05
MONO_BAR = 0.75
MIN_ZONES_BIN = 5
# the r353 record anchors (this round's regate targets)
R353_FB_TABLE = {124: (18.07, 0.329), 117: (17.78, 0.329),
                 133: (14.33, 0.337), 129: (10.43, 0.337),
                 107: (8.39, 0.318), 69: (6.94, 0.187),
                 80: (4.91, 0.408), 101: (4.09, 0.340)}
R353_FB_FAB_TOL = 0.02
R353_FB_GREL_TOL = 0.003
R353_CK2X = 11.87
R353_CK2X_TOL = 0.02
R353_FB_K2MAX = 5.95
R353_FB_K2MAX_TOL = 0.02
R353_GMIN = 0.187
R353_GMIN_TOL = 0.003
R353_IMPL = 63.4
R353_IMPL_TOL = 0.3
R353_M2ENV = 44.18
R353_M2ENV_TOL = 0.02
R353_M0 = 20.5
R353_M0_TOL = 0.1
R353_CNT_RES = (1.61, 2.79)
R353_CNT_RES_TOL = 0.05
# import-integrity SHA prefixes (sealed)
SFE_SHA_PREFIX = "bd89e331"
QGL_SHA_PREFIX = "67102e4c"
TSL_SHA_PREFIX = "9b593e63"
EFA_SHA_PREFIX = "bbfaf199"
PC343_SHA_PREFIX = "9ffc2705"

R355_TABLE_LITERALS = frozenset(SFE.R353_TABLE_LITERALS | {
    18.07, 17.78, 63.4, 44.18, 20.5, 5.95})

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
                       "the r244 chain rows; the prime-power anchor "
                       "grid U_ALL/G_ALL is the sealed source comb "
                       "(r238 convention); ground truth enters "
                       "gates and census tables only"
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
    lies in the sealed r314..r353 record set."""
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
                            in R355_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source hygiene: the
# ---------------- construction/curve builders consume the source
# ---------------- grid (U_ALL/G_ALL), window shape, passed values
# ---------------- and SEALED thresholds only; the withheld
# ---------------- terminal drive key, the branch label, the cubic
# ---------------- target record and the q_max record identifiers
# ---------------- are forbidden (AST identifier scan + literal
# ---------------- scan).  FAB, grel products, hgn, pil, counts
# ---------------- and every census on them are TARGET-SIDE
# ---------------- DIAGNOSTICS computed in the gate section
# ---------------- (r321/r349/r351/r353 convention, disclosed).
def mesh_h(kz, nu):
    """THE EXACT MESH IDENTITY (derived construction algebra,
    spec): the frame construction sets D = 0.5 G/nu, mz =
    ceil(alpha/D - 1e-9) + 1 rounded even, h = mz/2 -- hence with
    the NU-free depth coordinate u = alpha/G:  h - nu u in
    (0, 1.5] EXACTLY (ceil + 1 + even rounding over the mesh).
    Returns (h, h - nu u).  Consumes the source grid + the passed
    aspect only."""
    alpha = float(core.U_ALL[kz])
    gap = float(core.G_ALL[kz])
    dk = 0.5 * gap / float(nu)
    mz = int(math.ceil(alpha / dk - 1.0e-9)) + 1
    if mz % 2:
        mz += 1
    h = mz // 2
    u = alpha / gap
    return h, float(h) - float(nu) * u


def gmin_bins(us, gs, min_count):
    """the dyadic LOWER-ENVELOPE binning of the gap floor: bin
    j = floor(log2 u); per bin with >= min_count zones returns
    (median u, min g, count); bins ordered by u.  Consumes the
    passed grid columns + the sealed floor count only."""
    by = {}
    for u, g in zip(us, gs):
        j = int(math.floor(math.log2(max(float(u), 1e-300))))
        by.setdefault(j, []).append((float(u), float(g)))
    out = []
    for j in sorted(by):
        mem = by[j]
        if len(mem) < min_count:
            continue
        out.append((float(np.median([u for u, _g in mem])),
                    min(g for _u, g in mem), len(mem)))
    return out


def gmin_letter_rule(e_g, mono_frac, e_flat, mono_bar):
    """the sealed gap-floor letter (total, exactly one fires;
    order sealed): GMIN_FLAT (|slope| within the flat bar) >
    GMIN_LAW (falling slope + monotone fraction) >
    GMIN_ERRATIC."""
    if abs(e_g) <= e_flat:
        return "GMIN_FLAT"
    if e_g < -e_flat and mono_frac >= mono_bar:
        return "GMIN_LAW"
    return "GMIN_ERRATIC"


def k2_main_tree(leak, brk, indexed, nufree):
    """the sealed main-letter verdict tree (booleans only; total,
    exactly one fires; order sealed): TARGET_LEAK >
    LAW_STATE_NOT_EXACT > K2_FAMILY_INDEXED >
    K2_LAW_CERTIFIED_NU_FREE > K2_HOLDS_CENSUS."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "LAW_STATE_NOT_EXACT"
    if indexed:
        return "K2_FAMILY_INDEXED"
    if nufree:
        return "K2_LAW_CERTIFIED_NU_FREE"
    return "K2_HOLDS_CENSUS"


def k2_source_letter(chain_ok, h_go, p_go):
    """the sealed source letter (total, exactly one fires):
    K2_SOURCE_FORMULA_DERIVED iff the exact chain is green AND at
    least one census cap carries non-vacuously;
    K2_SOURCE_CHAIN_OPEN otherwise."""
    if chain_ok and (h_go or p_go):
        return "K2_SOURCE_FORMULA_DERIVED"
    return "K2_SOURCE_CHAIN_OPEN"


def mutant_hfun_posthoc(rho, grels):
    """e1 MUST-FAIL MUTANT (protocol): the cap FUNCTION h(grel)
    read back from the seen violation column (consumes rho) --
    the BOUND_FORBIDDEN scope audit must FLAG it AND on the
    sealed toy it returns (4.0, 1.0) != the sealed
    constant-over-grel rule column (2.0, 1.0)."""
    return tuple(rho[i] / max(grels[i], 1e-300)
                 for i in range(len(rho)))


def mutant_c2_posthoc(rho, grels):
    """e2 MUST-FAIL MUTANT (protocol): the K2 constant set at the
    SEEN violation maximum (consumes rho) -- the BOUND_FORBIDDEN
    scope audit must FLAG it AND on the sealed toy it returns
    3.0 != the sealed toy freeze 1.0."""
    return max(rho[i] * grels[i] for i in range(len(rho)))


def mutant_nu_shared(rho, fab_nu4):
    """e3 MUST-FAIL MUTANT (protocol): the 'NU = 2 measurement'
    returned as the NU = 4 column verbatim -- shared zone data
    instead of a fresh build (consumes rho for the flag) -- the
    BOUND_FORBIDDEN scope audit must FLAG it AND on the sealed
    toy it returns (1.0, 2.0) != the fresh-build toy column
    (0.9, 1.8); the LIVE freshness ward (strict depth ordering
    per admitted zone) is the second catch."""
    _ = rho
    return tuple(fab_nu4)


def mutant_fab_wrong_log(mm, pk, ell):
    """e4 MUST-FAIL MUTANT: the law coordinate with the WRONG log
    power (m pk/lg^2 instead of /lg) -- on the sealed Fractions
    toy it returns 3/8 while the exact FAB is 3/4 (break factor
    == lg EXACT)."""
    return mm * pk / (ell * ell)


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'law orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'law constant' consuming the branch label -- the scope audit
    must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("k2_source_formula_probe -- "
          "PRIME.L2.K2_SOURCE_FORMULA.01 (round 355,")
    print("the K2 source formula: q_max from a lower gap bound "
          "-- the reviewer fork)")
    print("SPEC_SHA %s   R353_SHA %s   R351_SHA %s   R329_SHA %s"
          % (SPEC_SHA[:16], SFE.SPEC_SHA[:16], QGL.SPEC_SHA[:16],
             EFA.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + w9 wards + Fractions "
                        "pins + frame-B construction ward + mesh "
                        "ward + selection enumeration + e1-e4; "
                        "ladder, extensions, EXT3-5, frame-B "
                        "evaluation, NU builds, curve, records, "
                        "composition and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (SFE.SPEC_SHA.startswith(SFE_SHA_PREFIX)
              and QGL.SPEC_SHA.startswith(QGL_SHA_PREFIX)
              and TSL.SPEC_SHA.startswith(TSL_SHA_PREFIX)
              and EFA.SPEC_SHA.startswith(EFA_SHA_PREFIX)
              and PC343.SPEC_SHA.startswith(PC343_SHA_PREFIX))
    check("G02-predefinition", sha_ok,
          "THE K2 SOURCE-FORMULA ROUND (the reviewer fork after "
          "r353): LEG A chain FAB grel <= (ngj/lg)(hgn grel) "
          "(r327 exact) x r329 census x THE NEW C_H/C_P freezes "
          "+ the EXACT mesh identity h = NU u + (0, %.1f]; LEG B "
          "frozen C_2 (max FAB grel, 89 sealed rows) tested on "
          "frame-B regate + NU test %s at NU %s + fresh field "
          "NU_C = %d (h <= %d, K_CZ %d [queue EMPTY, disclosed] "
          "+ K_CD %d, budget %d); LEG C g_min(u) dyadic curve "
          "(flat bar %.2f, mono bar %.2f, floor %d); verdict "
          "trees sealed BEFORE evaluation; import integrity SFE "
          "%s / QGL %s / TSL %s / EFA %s / PC343 %s"
          % (MESH_DEV_HI, str(NU_TEST_KZ), str(NU_TEST_NUS),
             NU_C, H_C_CAP, K_CZ, K_CD, MAX_BUILDS_C, E_FLAT_G,
             MONO_BAR, MIN_ZONES_BIN, SFE.SPEC_SHA[:8],
             QGL.SPEC_SHA[:8], TSL.SPEC_SHA[:8],
             EFA.SPEC_SHA[:8], PC343.SPEC_SHA[:8]))
    frag = antigate_fragment_audit()
    own_builders = ("mesh_h", "gmin_bins", "gmin_letter_rule",
                    "k2_main_tree", "k2_source_letter")
    sc_own = []
    for fn in own_builders:
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the module-own "
          "mesh/curve/tree builders clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the "
          "construction side consumes the source grid + window "
          "shape + sealed thresholds ONLY; m5a gift-bound "
          "FLAGGED (%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r353 verbatim) +
    # ---------------- extensions + EXT3/4/5 + FRAME-B regate +
    # ---------------- the sealed NU selections
    section("S1  CENSUS + CONTROLS + EXTENSIONS + EXT3/4/5 + "
            "FRAME-B (r353 REGATE) + THE SEALED NU SELECTIONS")
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
        ext4 = []
        ext5 = []
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
        ext4 = [BH.wpack(kz) for kz in EXT4_KZ]
        ext4.sort(key=lambda p: (p["N"], p["kz"]))
        ext5 = [BH.wpack(kz) for kz in EXT5_KZ_B + EXT5_KZ_A]
        ext5.sort(key=lambda p: (p["N"], p["kz"]))
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
        check("G14-ext345-adoption", True, "SMOKE: skipped")
    else:
        check("G12-extension-census",
              len(ext) == K_EXT
              and ext[0]["N"] == EXT_NW_EXPECT[0]
              and ext[-1]["N"] == EXT_NW_EXPECT[1]
              and all(p["nf"] is None for p in ext)
              and len(ext2) <= K_EXT2
              and all(p["nf"] is None for p in ext2),
              "r286-aligned extension: %d anchors, N_w %d..%d "
              "(expected %d..%d); EXT2 (r316 A5 rule verbatim): "
              "%d POSITIVE_PREFIX anchors, N_w %s..%s"
              % (len(ext), ext[0]["N"] if ext else -1,
                 ext[-1]["N"] if ext else -1, EXT_NW_EXPECT[0],
                 EXT_NW_EXPECT[1], len(ext2),
                 ext2[0]["N"] if ext2 else "-",
                 ext2[-1]["N"] if ext2 else "-"))
        check("G14-ext345-adoption",
              len(ext3) == 12
              and all(p["nf"] is None for p in ext3)
              and min(p["N"] for p in ext3) == EXT3_NW_MIN
              and max(p["N"] for p in ext3) == EXT3_NW_MAX
              and len(ext4) == 6
              and all(p["nf"] is None for p in ext4)
              and min(p["N"] for p in ext4) == EXT4_NW_MIN
              and max(p["N"] for p in ext4) == EXT4_NW_MAX
              and len(ext5) == 6
              and all(p["nf"] is None for p in ext5)
              and min(p["N"] for p in ext5) == EXT5_NW_MIN
              and max(p["N"] for p in ext5) == EXT5_NW_MAX,
              "EXT3 = the sealed r329 12-anchor list, EXT4 = the "
              "sealed r343/r345 6-anchor list, EXT5 = the sealed "
              "r351 6-anchor list -- ALL ADOPTED AS-IS: "
              "POSITIVE_PREFIX %d/12 + %d/6 + %d/6; N_w EXT3 "
              "%d..%d / EXT4 %d..%d / EXT5 %d..%d"
              % (sum(1 for p in ext3 if p["nf"] is None),
                 sum(1 for p in ext4 if p["nf"] is None),
                 sum(1 for p in ext5 if p["nf"] is None),
                 min(p["N"] for p in ext3),
                 max(p["N"] for p in ext3),
                 min(p["N"] for p in ext4),
                 max(p["N"] for p in ext4),
                 min(p["N"] for p in ext5),
                 max(p["N"] for p in ext5)))
    # THE r353 FRAME-B SELECTION (SFE verbatim, regate) + THE
    # SEALED NU_C SELECTION (runs in smoke too -- pool counts +
    # queues only, no deep wpack)
    lm_rows = LM.ext_rule()
    used = set(EFA.used_kz_set(core.frame_a_zones(), lm_rows,
                               LM_RANKS_USED))
    used |= set(PC343.EXT3_KZ_B + PC343.EXT3_KZ_A)
    used |= set(PC343.EXT4_KZ_B + PC343.EXT4_KZ_A)
    used |= set(EXT5_KZ_B + EXT5_KZ_A)
    pool_b = SFE.frameb_pool(NU_B, core.H_MIN, H_B_CAP, Z2_CAP)
    fresh_b = [(h, kz) for (h, kz) in pool_b if kz not in used]
    fresh_b_kz = [kz for (_h, kz) in fresh_b]
    grels_b = EFA.grel_col(fresh_b_kz, core.G_ALL)
    zz_b = {kz: int(core._NN[kz]) for kz in fresh_b_kz}
    b_q, d_q = SFE.frameb_select(fresh_b,
                                 [zz_b[kz] for kz in fresh_b_kz],
                                 grels_b, CORE_Z[0], CORE_Z[1],
                                 K_BZ)
    check("G16-famb-selection-regate",
          len(used) == USED_EXPECT_B
          and len(fresh_b) == FRESH_EXPECT_B
          and tuple(b_q[:K_BZ]) == BZQ_EXPECT
          and tuple(d_q[:K_BD]) == BDQ_HEAD_EXPECT,
          "THE r353 FRAME-B SELECTION re-executed verbatim: used "
          "%d (== %d), fresh %d (== %d); BZ queue %s + BD head "
          "%s == the r353 sealed queues"
          % (len(used), USED_EXPECT_B, len(fresh_b),
             FRESH_EXPECT_B, str(b_q[:K_BZ]), str(d_q[:K_BD])))
    # THE SEALED NU_C FRESH-FIELD SELECTION
    used_c = used | set(FRAMEB_KZ)
    pool_c = SFE.frameb_pool(NU_C, core.H_MIN, H_C_CAP, Z2_CAP)
    fresh_c = [(h, kz) for (h, kz) in pool_c if kz not in used_c]
    fresh_c_kz = [kz for (_h, kz) in fresh_c]
    grels_c = EFA.grel_col(fresh_c_kz, core.G_ALL)
    zz_c = {kz: int(core._NN[kz]) for kz in fresh_c_kz}
    cz_q, cd_q = SFE.frameb_select(fresh_c,
                                   [zz_c[kz] for kz in fresh_c_kz],
                                   grels_c, CORE_Z[0], CORE_Z[1],
                                   K_CZ)
    gr_c = {kz: g for kz, g in zip(fresh_c_kz, grels_c)}
    h_c = {kz: h for (h, kz) in fresh_c}
    check("G18-nuc-selection",
          len(used_c) == USED_EXPECT_C
          and len(fresh_c) == FRESH_EXPECT_C
          and tuple(cz_q[:K_CZ]) == CZQ_EXPECT
          and tuple(cd_q[:K_CD]) == CDQ_EXPECT,
          "THE SEALED NU_C = %d SELECTION executed verbatim "
          "(SFE.frameb_select, aspect the only change): used %d "
          "(== %d, incl. the 8 r353 frame-B anchors), fresh %d "
          "(== %d, h <= %d, z^2 <= %d); STRATUM CZ queue %s == "
          "EMPTY (the in-zone pool is EXHAUSTED at every aspect "
          "-- disclosed up front); CD queue head %s (h %s, grel "
          "%s)"
          % (NU_C, len(used_c), USED_EXPECT_C, len(fresh_c),
             FRESH_EXPECT_C, H_C_CAP, Z2_CAP, str(cz_q[:K_CZ]),
             str(cd_q[:K_CD]),
             str([h_c[k] for k in cd_q[:K_CD]]),
             str([round(gr_c[k], 3) for k in cd_q[:K_CD]])))
    if smoke:
        check("G17-famb-admission", True,
              "SMOKE: skipped (no deep wpack)")
        check("G19-nu-admission", True,
              "SMOKE: skipped (no deep wpack)")
        famb = []
        nut_packs = []
        nuc_packs = []
        nut_fail = []
        nuc_fail = []
    else:
        builds = [0]

        def admit_queue(queue, k, nu, budget):
            got = []
            failed = []
            for kz in queue:
                if len(got) >= k or builds[0] >= budget:
                    break
                builds[0] += 1
                pb = SFE.wpack_b(kz, nu)
                if pb["nf"] is None and pb["complete"]:
                    pb["nu"] = nu
                    got.append(pb)
                else:
                    failed.append((kz, nu, pb["nf"],
                                   pb["complete"]))
            return got, failed

        bz_packs, bz_fail = admit_queue(b_q, K_BZ, NU_B,
                                        MAX_BUILDS_B)
        bd_packs, bd_fail = admit_queue(d_q, K_BD, NU_B,
                                        MAX_BUILDS_B)
        famb = bz_packs + bd_packs
        famb.sort(key=lambda p: (p["N"], p["kz"]))
        check("G17-famb-admission",
              len(famb) == len(FRAMEB_KZ)
              and sorted(p["kz"] for p in famb)
              == sorted(FRAMEB_KZ)
              and all(p["complete"] for p in famb),
              "THE r353 FRAME-B ADMISSION re-executed: %d/%d "
              "admitted %s (== the r353 record set), queue "
              "failures BZ %s / BD %s"
              % (len(famb), K_BZ + K_BD,
                 str(sorted(p["kz"] for p in famb)),
                 str(bz_fail), str(bd_fail)))
        # THE NU TEST (12 sealed builds) + THE FRESH FIELD
        builds_nu = [0]

        def admit_list(kz_nu_list, budget):
            got = []
            failed = []
            for kz, nu in kz_nu_list:
                if builds_nu[0] >= budget:
                    break
                builds_nu[0] += 1
                pb = SFE.wpack_b(kz, nu)
                if pb["nf"] is None and pb["complete"]:
                    pb["nu"] = nu
                    got.append(pb)
                else:
                    failed.append((kz, nu, pb["nf"],
                                   pb["complete"]))
            return got, failed

        nut_list = [(kz, nu) for nu in NU_TEST_NUS
                    for kz in NU_TEST_KZ]
        nut_packs, nut_fail = admit_list(nut_list, 99)
        builds_c = [0]

        def admit_queue_c(queue, k):
            got = []
            failed = []
            for kz in queue:
                if len(got) >= k or builds_c[0] >= MAX_BUILDS_C:
                    break
                builds_c[0] += 1
                pb = SFE.wpack_b(kz, NU_C)
                if pb["nf"] is None and pb["complete"]:
                    pb["nu"] = NU_C
                    got.append(pb)
                else:
                    failed.append((kz, NU_C, pb["nf"],
                                   pb["complete"]))
            return got, failed

        cz_packs, cz_fail = admit_queue_c(cz_q, K_CZ)
        cd_packs, cd_fail = admit_queue_c(
            [kz for kz in cd_q if kz not in set(cz_q[:K_CZ])],
            K_CD)
        nuc_packs = cz_packs + cd_packs
        nuc_fail = cz_fail + cd_fail
        check("G19-nu-admission",
              len(nut_packs) + len(nut_fail) == 12
              and len(nuc_packs) >= FRESH_MIN_C,
              "NU-TEST ADMISSION (12 sealed builds): %d/12 "
              "POSITIVE_PREFIX + chain-complete %s, failures %s; "
              "FRESH FIELD NU_C = %d: %d admitted %s (budget %d "
              "builds), failures %s -- PURE TEST rows of THIS "
              "round"
              % (len(nut_packs),
                 str([(p["kz"], p["nu"], p["N"])
                      for p in nut_packs]),
                 str(nut_fail), NU_C, len(nuc_packs),
                 str([(p["kz"], p["N"]) for p in nuc_packs]),
                 MAX_BUILDS_C, str(nuc_fail)))

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
                    lo=lo, hi=hi, p=p, nf=p["nf"],
                    nu=p.get("nu", NU_A))

    recs = [rung_rec(p) for p in pool]
    erecs = [rung_rec(p) for p in ext] if not smoke else []
    e2recs = [rung_rec(p) for p in ext2] if not smoke else []
    x3recs = [rung_rec(p) for p in ext3] if not smoke else []
    x4recs = [rung_rec(p) for p in ext4] if not smoke else []
    x5recs = [rung_rec(p) for p in ext5] if not smoke else []
    fbrecs = [rung_rec(p) for p in famb] if not smoke else []
    ntrecs = [rung_rec(p) for p in nut_packs] if not smoke else []
    ncrecs = [rung_rec(p) for p in nuc_packs] if not smoke else []
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
        e_exc = [rc["kz"] for rc in erecs + e2recs + x3recs
                 + x4recs + x5recs if rc["g_branch"] < 0.0]
        nu_exc = [(rc["kz"], rc["nu"]) for rc in fbrecs + ntrecs
                  + ncrecs if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "extension exceptions %s; frame-B + NU-row branch "
              "census: %d rows, exceptions %s (census, no "
              "letter)"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 str(e_exc),
                 len(fbrecs) + len(ntrecs) + len(ncrecs),
                 str(nu_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + TREE-LEDGER WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext = 0.0
    tb_x345 = 0.0
    tb_fb = 0.0
    tb_nu = 0.0
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
    for rc in x3recs + x4recs + x5recs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_x345 = max(tb_x345, dev)
    for rc in fbrecs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_fb = max(tb_fb, dev)
    for rc in ntrecs + ncrecs:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_nu = max(tb_nu, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext <= TB_WARD_BAR_DEEP
          and tb_x345 <= max(TB_WARD_BAR_X3, TB_WARD_BAR_X4,
                             TB_WARD_BAR_X5)
          and tb_fb <= TB_WARD_BAR_B
          and tb_nu <= TB_WARD_BAR_C
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext/ext2 + %d "
          "ext3-5 + %d FRAME-B + %d NU rows + %d mains + 3 "
          "controls: worst dev/absmass %.1e main / %.1e deep / "
          "%.1e ext / %.1e ext3-5 / %.1e FRAME-B (bar %.0e) / "
          "%.1e NU rows (a-priori bar %.0e) / %.1e controls"
          % (len(recs), len(erecs) + len(e2recs),
             len(x3recs) + len(x4recs) + len(x5recs),
             len(fbrecs), len(ntrecs) + len(ncrecs), len(mrecs),
             tb_worst, tb_deep, tb_ext, tb_x345, tb_fb,
             TB_WARD_BAR_B, tb_nu, TB_WARD_BAR_C, tb_ctrl))

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
            pst = QMO.pileup_state(sct["x"], val_all, blk_all)
            hst = GMC.heavy_state(sct["x"], led327)
            dic = FDD.martingale_moment_dictionary(sct["x"])
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
            pst = dict(j=0, nsc=0, nsc_rel=0, pil=0.0, a1j=0.0,
                       tail=0.0, scut=0, scales=(), masses=())
            hst = dict(j=0, ngj=0, hga=0.0, hgn=0.0, a1j=0.0,
                       vmaxb=0.0, bshare=0.0)
            dic = dict(d1=0.0, d2=0.0, d3=0.0, ymx=0.0)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs,
                    led327=led327, pst=pst, hst=hst, dic=dic,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

    all_rc = recs + mrecs + erecs + e2recs + x3recs + x4recs \
        + x5recs + fbrecs + ntrecs + ncrecs
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
    nu_mult_drop = []
    for rc in ntrecs + ncrecs + fbrecs:
        if rc["ev"]["mx_mult"] > MULT_CAP \
                or rc["ev"]["degenerate"]:
            nu_mult_drop.append((rc["kz"], rc["nu"]))
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "r327 GMC ledger segments IDENTICALLY to the genealogy "
          "(worst dev %.1e, bar %.0e); NU-row post-eval filter "
          "(mult <= %d + non-degenerate): drops %s%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             MULT_CAP,
             str(nu_mult_drop) if nu_mult_drop else "NONE",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))
    # the admitted NU rows after the post-eval filter
    drop_set = set(nu_mult_drop)
    ntrecs_ok = [rc for rc in ntrecs
                 if (rc["kz"], rc["nu"]) not in drop_set]
    ncrecs_ok = [rc for rc in ncrecs
                 if (rc["kz"], rc["nu"]) not in drop_set]

    # ---------------- S3: Leg 0 anchors (slim set)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim set: r306/r316 "
            "+ dictionary + r321 F_A; the r349/r324/r329/r351/"
            "r353 records follow in S5)")
    xall_ids = set(id(rc) for rc in x3recs + x4recs + x5recs
                   + fbrecs + ntrecs + ncrecs)
    live_69 = [rc for rc in live if id(rc) not in xall_ids]
    rec3_w = max(rc["ev"]["rec3"] for rc in live_69)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live_69)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live_69)
    rec3_x = max((rc["ev"]["rec3"] for rc in x3recs), default=0.0)
    rec3_x4 = max((rc["ev"]["rec3"] for rc in x4recs),
                  default=0.0)
    rec3_x5 = max((rc["ev"]["rec3"] for rc in x5recs),
                  default=0.0)
    rec3_fb = max((rc["ev"]["rec3"] for rc in fbrecs),
                  default=0.0)
    rec3_nu = max((rc["ev"]["rec3"] for rc in ntrecs + ncrecs),
                  default=0.0)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR and rec3_x <= REC3_BAR_X3
          and rec3_x4 <= REC3_BAR_X4 and rec3_x5 <= REC3_BAR_X5
          and rec3_fb <= REC3_BAR_B and rec3_nu <= REC3_BAR_C,
          "the r314 identity live: ladder worlds recomposition "
          "%.1e / telescope %.1e / boundary %.1e; EXT3 %.1e; "
          "EXT4 %.1e; EXT5 %.1e; FRAME-B %.1e; NU rows %.1e "
          "(a-priori bar %.0e); DISCLOSED slim anchor set -- "
          "the full chain is re-warded by the sealed r321..r353 "
          "probes"
          % (rec3_w, tel_w, bnd_w, rec3_x, rec3_x4, rec3_x5,
             rec3_fb, rec3_nu, REC3_BAR_C))
    if smoke:
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        srt = []
        n355 = 0
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2r, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2r)
        check("G31-r306-bound-live",
              abs(C2r - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d"
              % (C2r, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        srt_all65 = sorted(recs + erecs + e2recs,
                           key=lambda rc: (rc["N"], rc["kz"]))
        srt = [rc for rc in srt_all65
               if rc["ev"]["mx_mult"] <= MULT_CAP]
        n355 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n355)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n355 == N355_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n355, N355_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
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
          "THE MOMENT DICTIONARY anchored bit-near on %d live "
          "worlds (incl. FRAME-B + NU rows): E[X_inf^2] == m M_2 "
          "(worst rel %.1e), E[X_inf^3] == rho_2 (log m)^2 "
          "(worst %.1e), max y / m == q_max (worst %.1e; bars "
          "%.0e) -- the dictionary link of the chain"
          % (len(live), dict2_w, dict3_w, dictq_w, DICT_BAR))
    if smoke:
        check("G39-r321-fa-anchors", True, "SMOKE: skipped")
    else:
        srt_x = sorted(x3recs, key=lambda rc: (rc["N"], rc["kz"]))
        srt_x = [rc for rc in srt_x
                 if rc["ev"]["mx_mult"] <= MULT_CAP
                 and not rc["ev"]["degenerate"]]
        srt_x4 = sorted(x4recs,
                        key=lambda rc: (rc["N"], rc["kz"]))
        srt_x4 = [rc for rc in srt_x4
                  if rc["ev"]["mx_mult"] <= MULT_CAP
                  and not rc["ev"]["degenerate"]]
        srt_x5 = sorted(x5recs,
                        key=lambda rc: (rc["N"], rc["kz"]))
        srt_x5 = [rc for rc in srt_x5
                  if rc["ev"]["mx_mult"] <= MULT_CAP
                  and not rc["ev"]["degenerate"]]
        srt_fb = sorted(fbrecs,
                        key=lambda rc: (rc["N"], rc["kz"]))
        srt_fb = [rc for rc in srt_fb
                  if rc["ev"]["mx_mult"] <= MULT_CAP
                  and not rc["ev"]["degenerate"]]
        srt_full = srt + srt_x
        n_full = len(srt_full)
        m_full = [rc["ev"]["m"] for rc in srt_full]
        lg_full = [math.log(float(v)) for v in m_full]
        q_lad = [srt[i]["ev"]["mqs"]["qm"] for i in range(n355)]
        fa_lad = EFP.local_ratio(q_lad)
        medloc_lad = CCP.local_median(q_lad)
        N_lad = [srt[i]["N"] for i in range(n355)]
        fa_full = list(fa_lad)
        for rc in srt_x:
            fa_full.append(CCP.world_coord(rc["ev"]["mqs"]["qm"],
                                           rc["N"], N_lad, q_lad))
        fa_kz = {srt_full[i]["kz"]: fa_full[i]
                 for i in range(n_full)}
        fa_x4 = [CCP.world_coord(rc["ev"]["mqs"]["qm"], rc["N"],
                                 N_lad, q_lad) for rc in srt_x4]
        fa_x5 = [CCP.world_coord(rc["ev"]["mqs"]["qm"], rc["N"],
                                 N_lad, q_lad) for rc in srt_x5]
        fa_fb = [CCP.world_coord(rc["ev"]["mqs"]["qm"], rc["N"],
                                 N_lad, q_lad) for rc in srt_fb]
        check("G39-r321-fa-anchors",
              all(abs(fa_kz[kz] - R321_FA_TOP[kz]) <= R321_FA_TOL
                  for kz in R321_FA_TOP),
              "the r321/r317 F_A coordinate reproduced through "
              "EFP.local_ratio on the module-own q_max column: "
              "top-3 kz53 %.2f / kz83 %.2f / kz67 %.2f (rec "
              "%.2f/%.2f/%.2f tol %.2f); EXT4/EXT5/FRAME-B via "
              "the r321 INSERTION RULE; the NEW NU rows carry NO "
              "F_ins/RSV columns (not consumed by the K2 "
              "contract, disclosed); GSQ = %.4f stays the BANKED "
              "r321 record"
              % (fa_kz[53], fa_kz[83], fa_kz[67],
                 R321_FA_TOP[53], R321_FA_TOP[83],
                 R321_FA_TOP[67], R321_FA_TOL, GSQ_R321))

    # ---------------- S4: seal + purity + toys + live wards
    section("S4  LEG 0b -- SEAL + PURITY + TOYS + LIVE WARDS")
    pure_lits = []
    for fn in own_builders:
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_hfun_posthoc", BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_c2_posthoc", BOUND_FORBIDDEN)
    e3_hits = scope_audit("mutant_nu_shared", BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e3_hits) >= 1,
          "SOURCE HYGIENE: the mesh/curve/tree builders clean vs "
          "the forbidden sets (%d id hits) and vs the sealed "
          "r314..r353 record-literal set (%d literal hits); e1 "
          "hfun-posthoc FLAGGED (%s); e2 c2-posthoc FLAGGED "
          "(%s); e3 nu-shared FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS"))
    # sealed toys (Fractions + by-hand pins, spec above)
    fab_dev = QGL.fr_fab_toy()
    fd_dev = TSL.fr_decomp_toy()
    # the K2 chain Fractions pin: m 4, pk 1/2, lg 2, grel 1/2,
    # ngj 2, hgn 1 -> FABg == bound == 1/2 EXACT; hgn 2 -> bound
    # 1 with slack 1/2 EXACT
    t_m, t_pk, t_lg, t_gr = Fr(4), Fr(1, 2), Fr(2), Fr(1, 2)
    t_fabg = QGL.fab_of(t_m, t_pk, t_lg) * t_gr
    t_bound1 = (Fr(2) / t_lg) * (Fr(1) * t_gr)
    t_bound2 = (Fr(2) / t_lg) * (Fr(2) * t_gr)
    k2toy_ok = (t_fabg == Fr(1, 2) and t_bound1 == Fr(1, 2)
                and t_bound2 - t_fabg == Fr(1, 2))
    # the mesh toy (by hand): alpha 10, gap 1, nu 2 -> h 21,
    # h - nu u = 1.0 <= MESH_DEV_HI
    t_dk = 0.5 * 1.0 / 2.0
    t_mz = int(math.ceil(10.0 / t_dk - 1.0e-9)) + 1
    if t_mz % 2:
        t_mz += 1
    t_h = t_mz // 2
    t_meshdev = float(t_h) - 2.0 * (10.0 / 1.0)
    meshtoy_ok = (t_h == 21 and abs(t_meshdev - 1.0) <= TOY_BAR
                  and 0.0 < t_meshdev <= MESH_DEV_HI)
    # the gmin toys (by hand, min_count 2)
    t_us = (2, 3, 4, 5, 8, 9, 10, 11)
    binsA = gmin_bins(t_us, (.8, .7, .9, .6, .4, .5, .45, .35), 2)
    binsB = gmin_bins(t_us, (.4, .7, .9, .6, .9, .5, .95, .35), 2)
    binsC = gmin_bins(t_us, (.5, .6, .5, .7, .5, .6, .5, .6), 2)

    def curve_stats(bins):
        gm = [g for _u, g, _n in bins]
        e_g = L2D.halves_slope([u for u, _g, _n in bins], gm) \
            if len(bins) >= 2 else 0.0
        pairs = [(gm[i + 1] <= gm[i] + 1e-12)
                 for i in range(len(gm) - 1)]
        mono = (sum(1 for p in pairs if p) / len(pairs)) \
            if pairs else 1.0
        return e_g, mono

    eA, mA = curve_stats(binsA)
    eB, mB = curve_stats(binsB)
    eC, mC = curve_stats(binsC)
    letA = gmin_letter_rule(eA, mA, E_FLAT_G, MONO_BAR)
    letB = gmin_letter_rule(eB, mB, E_FLAT_G, MONO_BAR)
    letC = gmin_letter_rule(eC, mC, E_FLAT_G, MONO_BAR)
    gmintoy_ok = ([g for _u, g, _n in binsA] == [.7, .6, .35]
                  and abs(eA - (-0.4407)) <= 0.001
                  and abs(mA - 1.0) <= TOY_BAR
                  and letA == "GMIN_LAW"
                  and [g for _u, g, _n in binsB] == [.4, .6, .35]
                  and abs(mB - 0.5) <= TOY_BAR
                  and letB == "GMIN_ERRATIC"
                  and [g for _u, g, _n in binsC] == [.5, .5, .5]
                  and abs(eC) <= TOY_BAR
                  and letC == "GMIN_FLAT")
    # mutant toys
    mut1 = mutant_hfun_posthoc((2.0, 1.0), (0.5, 1.0))
    toy1_sealed = (2.0, 1.0)
    mut2 = mutant_c2_posthoc((3.0, 2.0), (1.0, 0.5))
    toy2_sealed = 1.0
    mut3 = mutant_nu_shared((1.0, 1.0), (1.0, 2.0))
    toy3_fresh = (0.9, 1.8)
    mut4 = mutant_fab_wrong_log(Fr(3), Fr(1, 2), Fr(2))
    toy4_true = QGL.fab_of(Fr(3), Fr(1, 2), Fr(2))
    # verdict-tree toys
    tr_br = (k2_main_tree(True, True, True, True),
             k2_main_tree(False, True, True, True),
             k2_main_tree(False, False, True, True),
             k2_main_tree(False, False, False, True),
             k2_main_tree(False, False, False, False))
    ok_tr = tr_br == ("TARGET_LEAK", "LAW_STATE_NOT_EXACT",
                      "K2_FAMILY_INDEXED",
                      "K2_LAW_CERTIFIED_NU_FREE",
                      "K2_HOLDS_CENSUS")
    src_br = (k2_source_letter(True, True, False),
              k2_source_letter(True, False, False))
    ok_src = src_br == ("K2_SOURCE_FORMULA_DERIVED",
                        "K2_SOURCE_CHAIN_OPEN")
    check("G41-toy-exactness",
          fab_dev == 0 and fd_dev == 0 and k2toy_ok
          and meshtoy_ok and gmintoy_ok
          and tuple(mut1) == (4.0, 1.0) and mut1 != toy1_sealed
          and abs(mut2 - 3.0) <= TOY_BAR and mut2 != toy2_sealed
          and tuple(mut3) == (1.0, 2.0) and mut3 != toy3_fresh
          and mut4 == Fr(3, 8) and toy4_true == Fr(3, 4)
          and toy4_true / mut4 == Fr(2)
          and ok_tr and ok_src,
          "the sealed toys EXACT: FAB pin dev %s; decomp pin %s; "
          "K2 chain pin FABg %s == bound %s + slack %s; mesh toy "
          "h %d dev %.1f <= %.1f; gmin toys %s/%s/%s (slope pin "
          "%.4f); e1 pin %s != %s; e2 pin %.1f != %.1f; e3 pin "
          "%s != %s; e4 pin %s != true %s (break %s == lg); "
          "main tree %s; source tree %s"
          % (str(fab_dev), str(fd_dev), str(t_fabg),
             str(t_bound1), str(t_bound2 - t_fabg), t_h,
             t_meshdev, MESH_DEV_HI, letA, letB, letC, eA,
             str(tuple(mut1)), str(toy1_sealed), mut2,
             toy2_sealed, str(tuple(mut3)), str(toy3_fresh),
             str(mut4), str(toy4_true), str(toy4_true / mut4),
             str(tr_br), str(src_br)))
    # THE FRAME-B CONSTRUCTION WARD (r353 verbatim, exact, live)
    pb4 = SFE.wpack_b(9, NU_A)
    pa9 = packs["w9"]
    frb_dev = 0.0
    for k in range(min(pb4["N"], pa9["N"])):
        ra, rb = pa9["rows"][k], pb4["rows"][k]
        sc = max(abs(ra["alh"]), 1e-300)
        frb_dev = max(frb_dev, abs(ra["alh"] - rb["alh"]) / sc)
        if ra["sg_h"] != rb["sg_h"]:
            frb_dev = max(frb_dev, 1.0)
    pool_a_repro = sorted(kz for (_h, kz) in
                          SFE.frameb_pool(NU_A, core.H_MIN,
                                          core.HCAP, None))
    frame_ok = (pool_a_repro == sorted(core.frame_a_zones()))
    # THE MESH IDENTITY WARD on every pool zone at NU 2/3/4
    mesh_bad = []
    mesh_n = {}
    for nu, hcap in ((2, H_B_CAP), (NU_C, H_C_CAP),
                     (4, PC343.EXT4_H_MAX)):
        zones_nu = SFE.frameb_pool(nu, core.H_MIN, hcap, Z2_CAP)
        mesh_n[nu] = len(zones_nu)
        for h, kz in zones_nu:
            hh, dev = mesh_h(kz, nu)
            if hh != h or not (0.0 < dev <= MESH_DEV_HI + 1e-9):
                mesh_bad.append((kz, nu, hh, h, dev))
    mesh_ok = not mesh_bad
    # THE NU FRESHNESS WARD (live): strict depth ordering per
    # admitted NU-test zone (a shared column cannot pass)
    if smoke:
        nufresh_ok = True
        nufresh_txt = "n/a (SMOKE)"
    else:
        n_by = {}
        for rc in ntrecs:
            n_by[(rc["kz"], rc["nu"])] = rc["N"]
        n4_by = {}
        for rc in x3recs + x4recs + x5recs + recs + erecs \
                + e2recs:
            n4_by[rc["kz"]] = rc["N"]
        nufresh_ok = True
        for (kz, nu), nn in n_by.items():
            n4 = n4_by.get(kz)
            if n4 is not None and not nn < n4:
                nufresh_ok = False
            if nu == 2 and (kz, 3) in n_by \
                    and not nn < n_by[(kz, 3)]:
                nufresh_ok = False
        nufresh_txt = ("strict N(NU2) < N(NU3) < N(NU4) on %d "
                       "admitted NU-test rows" % len(ntrecs))
    check("G43-construction-wards",
          pb4["N"] == pa9["N"] and pb4["nf"] == pa9["nf"]
          and frb_dev <= FRB_WARD_BAR and frame_ok
          and mesh_ok and nufresh_ok,
          "THE NU = %d REPRODUCTION WARD (r353 verbatim): "
          "bit-identical wpack on w9 (N %d == %d, dev %.1e) AND "
          "pool == frame_a_zones %s; THE MESH IDENTITY h - NU u "
          "in (0, %.1f] EXACT on %s pool zones at NU (2, %d, 4) "
          "(violations %s) -- WHERE grel enters is now "
          "construction algebra: u = alpha/gap is the NU-free "
          "depth coordinate; THE NU FRESHNESS WARD: %s"
          % (NU_A, pb4["N"], pa9["N"], frb_dev,
             "EXACT" if frame_ok else "BROKEN", MESH_DEV_HI,
             str(tuple(mesh_n[k] for k in sorted(mesh_n))), NU_C,
             str(mesh_bad[:3]) if mesh_bad else "0",
             nufresh_txt))
    # THE ROUND'S OWN EXACT LIVE WARDS on every live world
    norm_w = 0.0
    interp_w = 0.0
    fabid_w = 0.0
    pile_w = 0.0
    pilerec_w = 0.0
    grp_w = 0.0
    k2ch_w = 0.0
    dec_w = 0.0
    chainD_w = 0.0
    chain_w = 0.0
    grel_live = {rc["kz"]: g for rc, g in zip(
        live, EFA.grel_col([rc["kz"] for rc in live],
                           core.G_ALL))}
    for rc in live:
        ev = rc["ev"]
        mloc = ev["m"]
        lgl = math.log(float(mloc))
        ax_i = np.abs(ev["sct"]["x"])
        Lx_i = float(np.sum(ax_i))
        c3q_i = float(np.sum(ax_i ** 3)) / max(Lx_i ** 3, 1e-300)
        norm_w = max(norm_w,
                     abs(ev["rho2"] * lgl ** 2 / mloc ** 2
                         - c3q_i) / max(c3q_i, 1e-300))
        pk_i = ev["mqs"]["qm"]
        m2q_i = ev["mqs"]["m2"] / float(mloc)
        if pk_i <= 0.0 or c3q_i <= 0.0:
            continue
        interp_w = max(interp_w,
                       max(0.0, c3q_i - pk_i * m2q_i)
                       / max(pk_i * m2q_i, 1e-300),
                       max(0.0, m2q_i - pk_i)
                       / max(pk_i, 1e-300))
        fab_i = QGL.fab_of(float(mloc), pk_i, lgl)
        fabid_w = max(fabid_w,
                      abs(fab_i * lgl - mloc * pk_i)
                      / max(mloc * pk_i, 1e-300))
        pst = ev["pst"]
        if pst["nsc"]:
            pile_w = max(pile_w,
                         max(0.0, mloc * pk_i
                             - pst["nsc"] * pst["pil"])
                         / max(pst["nsc"] * pst["pil"], 1e-300))
            pilerec_w = max(pilerec_w,
                            abs(sum(pst["masses"]) - pst["a1j"])
                            / max(pst["a1j"], 1e-300))
        hst = ev["hst"]
        if hst["ngj"]:
            grp_w = max(grp_w,
                        max(0.0, mloc * pk_i
                            - hst["ngj"] * hst["hgn"])
                        / max(hst["ngj"] * hst["hgn"], 1e-300))
            # THE K2 CHAIN WARD (assembled, one-sided exact):
            # FAB grel <= (ngj/lg)(hgn grel)
            g_i = grel_live[rc["kz"]]
            lhs = fab_i * g_i
            rhs = (hst["ngj"] / lgl) * (hst["hgn"] * g_i)
            k2ch_w = max(k2ch_w, max(0.0, lhs - rhs)
                         / max(rhs, 1e-300))
        dd_i = c3q_i / pk_i ** 3
        b2_i = (pk_i * mloc / lgl) ** 2
        sc_i, sm_i2, sd_i = TSL.res_decomp(GSQ_R321, b2_i, pk_i,
                                           m2q_i, c3q_i)
        rsv_dir = GSQ_R321 * 1.0 / max(ev["rho2"], 1e-300)
        dec_w = max(dec_w,
                    abs(sc_i * sm_i2 * sd_i - rsv_dir)
                    / max(rsv_dir, 1e-300))
        chainD_w = max(chainD_w,
                       abs(dd_i * pk_i ** 3 * mloc ** 2
                           / lgl ** 2 - ev["rho2"])
                       / max(ev["rho2"], 1e-300))
        trs = ev["trs"]
        nc = trs["nrm"] * ev["cube"]
        chain_w = max(chain_w, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
    check("G42-live-wards",
          norm_w <= DEC_BAR and interp_w <= CHAIN_BAR
          and fabid_w <= FAB_ID_BAR and pile_w <= CHAIN_BAR
          and pilerec_w <= GRP_CHAIN_BAR and grp_w <= CHAIN_BAR
          and k2ch_w <= CHAIN_BAR
          and dec_w <= DEC_BAR and chainD_w <= DEC_BAR
          and chain_w <= CHAIN_BAR,
          "THE ROUND'S OWN EXACT WARDS live on %d worlds (incl. "
          "FRAME-B + NU rows): NORM %.1e; interpolation %.1e; "
          "FAB identity %.1e; pileup chain %.1e + recomposition "
          "%.1e; group chain %.1e; THE K2 CHAIN FAB grel <= "
          "(ngj/lg)(hgn grel) one-sided %.1e (bar %.0e) -- the "
          "chain closes EXACTLY, its constants are census; "
          "reserve decomposition %.1e + dominance chain %.1e; "
          "r316 chain %.1e"
          % (len(live), norm_w, interp_w, fabid_w, pile_w,
             pilerec_w, grp_w, k2ch_w, CHAIN_BAR, dec_w,
             chainD_w, chain_w))

    # ---------------- S5: the r349/r324/r329/r351/r353 records
    section("S5  LEG 0c -- THE r349/r324/r329/r351/r353 RECORDS "
            "(SAME CODE PATH)")
    if smoke:
        check("G50-r349-family-record", True, "SMOKE: skipped")
        check("G51-r349-ext4-record", True, "SMOKE: skipped")
        check("G52-r329-counting-record", True, "SMOKE: skipped")
        check("G53-r324-direct-record", True, "SMOKE: skipped")
        check("G54-r351-growth-record", True, "SMOKE: skipped")
        check("G55-r351-floor-record", True, "SMOKE: skipped")
        check("G56-r353-frameb-record", True, "SMOKE: skipped")
    else:
        pk_col = []
        m2q_col = []
        c3q_col = []
        dd_col = []
        rsv_col = []
        for i in range(n_full):
            ev = srt_full[i]["ev"]
            mloc = ev["m"]
            pk = ev["mqs"]["qm"]
            m2q = ev["mqs"]["m2"] / float(mloc)
            c3q = ev["cm"]["S3"]
            dd = c3q / max(pk ** 3, 1e-300)
            rsv = GSQ_R321 * fa_full[i] ** 2 \
                / max(ev["rho2"], 1e-300)
            pk_col.append(pk)
            m2q_col.append(m2q)
            c3q_col.append(c3q)
            dd_col.append(dd)
            rsv_col.append(rsv)
        bb_col = [pk_col[i] * m_full[i]
                  / (max(fa_full[i], 1e-300) * lg_full[i])
                  for i in range(n_full)]
        fam_idx = [i for i in range(n_full)
                   if FCC.cls_rule(fa_full[i], F0_SPLIT)
                   == "SPIKE"]
        quiet_idx = [i for i in range(n_full)
                     if i not in set(fam_idx)]
        rc_fam349 = CCP.spearman_rank(
            [fa_full[i] for i in fam_idx],
            [rsv_col[i] for i in fam_idx])
        sh_fam = [(math.log10(GSQ_R321 / bb_col[i] ** 2),
                   math.log10(pk_col[i] / m2q_col[i]),
                   math.log10(pk_col[i] * m2q_col[i]
                              / c3q_col[i]))
                  for i in fam_idx]
        med_f = [float(np.median([s[k] for s in sh_fam]))
                 for k in range(3)]
        dd_fam = [dd_col[i] for i in fam_idx]
        dd_qui = [dd_col[i] for i in quiet_idx
                  if pk_col[i] > 0 and c3q_col[i] > 0]
        dpkb2_max = max(dd_col[i] * pk_col[i] * bb_col[i] ** 2
                        for i in fam_idx)
        rsv_f = [rsv_col[i] for i in fam_idx]
        check("G50-r349-family-record",
              len(fam_idx) == R349_FAM_N
              and abs(min(rsv_f) - R349_RSV_TRIPLE[0])
              <= R349_RSV_TOL
              and abs(float(np.median(rsv_f))
                      - R349_RSV_TRIPLE[1]) <= R349_RSV_TOL
              and abs(max(rsv_f) - R349_RSV_TRIPLE[2])
              <= R349_RSV_TOL
              and abs(rc_fam349 - R349_RC_FAM) <= R349_RC_TOL
              and abs(float(np.median(dd_fam)) - R349_D_FAM_MED)
              <= R349_D_TOL
              and abs(max(dd_fam) - R349_D_FAM_MAX) <= R349_D_TOL
              and abs(float(np.median(dd_qui)) - R349_D_QUIET)
              <= R349_D_TOL
              and abs(dpkb2_max - R349_DPKB2) <= R349_DPKB2_TOL
              and all(abs(med_f[k] - R349_SHARES[k])
                      <= R349_SHARES_TOL for k in range(3)),
              "THE r349 FAMILY RECORD reproduced: family %d rows "
              "(rec %d); RSV min/med/max %.2f/%.2f/%.2f; rc_fam "
              "%+.3f (rec %+.3f); D fam med/max %.2f/%.2f, quiet "
              "med %.2f; max D pk B^2 %.3f; shares "
              "%+.2f/%+.2f/%+.2f"
              % (len(fam_idx), R349_FAM_N, min(rsv_f),
                 float(np.median(rsv_f)), max(rsv_f), rc_fam349,
                 R349_RC_FAM, float(np.median(dd_fam)),
                 max(dd_fam), float(np.median(dd_qui)),
                 dpkb2_max, med_f[0], med_f[1], med_f[2]))
        x4_rows = []
        for k, rc in enumerate(srt_x4):
            ev = rc["ev"]
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            pk = ev["mqs"]["qm"]
            c3q = ev["cm"]["S3"]
            fa4 = fa_x4[k]
            rsv4 = GSQ_R321 * fa4 ** 2 / max(ev["rho2"], 1e-300)
            dd4 = c3q / max(pk ** 3, 1e-300)
            x4_rows.append(dict(kz=rc["kz"], N=rc["N"], m=mloc,
                                lg=lgl, pk=pk, fa=fa4, rsv=rsv4,
                                dd=dd4,
                                cls=FCC.cls_rule(fa4, F0_SPLIT),
                                ev=ev))
        fins4_sorted = tuple(sorted(round(r["fa"], 2)
                                    for r in x4_rows))
        hole_ok = all(
            abs(next(r["rsv"] for r in x4_rows
                     if r["kz"] == kz) - R349_X4_HOLES[kz])
            <= R349_X4_HOLE_TOL for kz in R349_X4_HOLES)
        check("G51-r349-ext4-record",
              len(x4_rows) == 6
              and all(r["cls"] == "SPIKE" for r in x4_rows)
              and all(abs(fins4_sorted[j] - R349_X4_FINS[j])
                      <= R349_X4_FINS_TOL for j in range(6))
              and hole_ok,
              "THE r349 EXT4 RECORD reproduced: all six SPIKE; "
              "sorted F_ins %s (rec %s); holes kz111 rsv %.2f / "
              "kz75 rsv %.2f (rec 1.11/1.07)"
              % (str(fins4_sorted), str(R349_X4_FINS),
                 next(r["rsv"] for r in x4_rows
                      if r["kz"] == 111),
                 next(r["rsv"] for r in x4_rows
                      if r["kz"] == 75)))
        nscl65 = [srt[i]["ev"]["pst"]["nsc_rel"]
                  / math.log(float(srt[i]["ev"]["m"]))
                  for i in range(n355)]
        cnsc_repro = max(nscl65[i] for i in ca_i)
        viol_nsc = [i for i in te_i if nscl65[i] > cnsc_repro]
        ngl65 = [srt[i]["ev"]["hst"]["ngj"]
                 / math.log(float(srt[i]["ev"]["m"]))
                 for i in range(n355)]
        cng_repro = max(ngl65[i] for i in ca_i)
        viol_ng = [i for i in te_i if ngl65[i] > cng_repro]
        x3_nscl = [rc["ev"]["pst"]["nsc_rel"]
                   / math.log(float(rc["ev"]["m"]))
                   for rc in srt_x]
        x3_ngl = [rc["ev"]["hst"]["ngj"]
                  / math.log(float(rc["ev"]["m"]))
                  for rc in srt_x]
        rsvc_min = min(FROZEN_CNSC / max(v, 1e-300)
                       for v in x3_nscl)
        rsvd_min = min(FROZEN_CNG / max(v, 1e-300)
                       for v in x3_ngl)
        check("G52-r329-counting-record",
              abs(cnsc_repro - FROZEN_CNSC) <= EFA.FROZEN_TOL
              and not viol_nsc
              and abs(cng_repro - FROZEN_CNG) <= EFA.FROZEN_TOL
              and not viol_ng
              and abs(rsvc_min - R329_X3_RSVC_MIN)
              <= R329_X3_RSV_TOL
              and abs(rsvd_min - R329_X3_RSVD_MIN)
              <= R329_X3_RSV_TOL,
              "THE r329 COUNTING RECORD reproduced: C_NSC = %.4f "
              "0/39 (viol %d); C_NG = %.4f 0/39 (viol %d); EXT3 "
              "12/12 with min count reserves %.2f/%.2f"
              % (cnsc_repro, len(viol_nsc), cng_repro,
                 len(viol_ng), rsvc_min, rsvd_min))
        fab65 = [QGL.fab_of(float(srt[i]["ev"]["m"]),
                            srt[i]["ev"]["mqs"]["qm"],
                            math.log(float(srt[i]["ev"]["m"])))
                 for i in range(n355)]
        cinf_repro = max(fab65[i] for i in ca_i)
        viol_inf = sorted(srt[i]["kz"] for i in te_i
                          if fab65[i] > cinf_repro)
        msT = [srt[i]["ev"]["m"] for i in te_i]
        eg_repro = L2D.halves_slope(msT, [max(fab65[i], 1e-300)
                                          for i in te_i])
        check("G53-r324-direct-record",
              abs(cinf_repro - R324_CINF_REF) <= R324_CINF_TOL
              and tuple(viol_inf) == tuple(sorted(R324_VINF_SET))
              and abs(eg_repro - R324_EG_REF) <= R324_EG_TOL,
              "THE r324 DIRECT RECORD reproduced through the FAB "
              "column: C_INF = %.4f, violators %s == the r324 "
              "five; e_G = %+.3f"
              % (cinf_repro, str(viol_inf), eg_repro))
        # ---- THE r351 GROWTH + FLOOR RECORDS (the 89-row
        # ---- surface through the same code path)
        allrows = []
        for i in range(n_full):
            ev = srt_full[i]["ev"]
            allrows.append(dict(
                coh="LAD" if i < n355 else "EXT3",
                kz=srt_full[i]["kz"], m=ev["m"],
                lg=lg_full[i], pk=pk_col[i], fa=fa_full[i],
                cls=FCC.cls_rule(fa_full[i], F0_SPLIT),
                dd=dd_col[i], rsv=rsv_col[i], ev=ev))
        for r in x4_rows:
            allrows.append(dict(coh="EXT4", kz=r["kz"],
                                m=r["m"], lg=r["lg"], pk=r["pk"],
                                fa=r["fa"], cls=r["cls"],
                                dd=r["dd"], rsv=r["rsv"],
                                ev=r["ev"]))
        for k, rc in enumerate(srt_x5):
            ev = rc["ev"]
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            pk = ev["mqs"]["qm"]
            c3q = ev["cm"]["S3"]
            fa5 = fa_x5[k]
            rsv5 = GSQ_R321 * fa5 ** 2 / max(ev["rho2"], 1e-300)
            dd5 = c3q / max(pk ** 3, 1e-300)
            allrows.append(dict(coh="EXT5", kz=rc["kz"],
                                m=mloc, lg=lgl, pk=pk, fa=fa5,
                                cls=FCC.cls_rule(fa5, F0_SPLIT),
                                dd=dd5, rsv=rsv5, ev=ev))
        grel_all = EFA.grel_col([r["kz"] for r in allrows],
                                core.G_ALL)
        for r, g in zip(allrows, grel_all):
            r["grel"] = g
            r["gcls"] = EFA.gap_class(g)
            r["fab"] = QGL.fab_of(float(r["m"]), r["pk"],
                                  r["lg"])
            pst = r["ev"]["pst"]
            hst = r["ev"]["hst"]
            r["pil"] = pst["pil"]
            r["nscl"] = pst["nsc_rel"] / r["lg"]
            r["ngl"] = hst["ngj"] / r["lg"]
            r["hgn"] = hst["hgn"]
            r["bsh"] = hst["bshare"]
        c_fab89 = max(r["fab"] for r in allrows)
        c_fab89_kz = max(allrows, key=lambda r: r["fab"])["kz"]
        x5max = max((r for r in allrows if r["coh"] == "EXT5"),
                    key=lambda r: r["fab"])
        fins79 = next(r["fa"] for r in allrows
                      if r["kz"] == 79 and r["coh"] == "EXT5")
        smallfam89 = [r for r in allrows
                      if r["gcls"] == "SMALL"
                      and r["cls"] == "SPIKE"]
        rc_small89 = CCP.spearman_rank(
            [r["m"] for r in smallfam89],
            [r["fab"] for r in smallfam89]) \
            if len(smallfam89) >= 2 else 0.0
        check("G54-r351-growth-record",
              abs(c_fab89 - R351_CFAB) <= R351_CFAB_TOL
              and c_fab89_kz == R351_CFAB_KZ
              and abs(x5max["fab"] - R351_X5_FABMAX)
              <= R351_CFAB_TOL
              and x5max["kz"] == R351_X5_FABMAX_KZ
              and abs(fins79 - R351_X5_FINS79)
              <= R351_X5_FINS_TOL
              and abs(rc_small89 - R351_RC_SMALL)
              <= R351_SLOPE_TOL,
              "THE r351 GROWTH RECORD reproduced on the %d-row "
              "surface: C_FAB = %.2f at kz%d (rec %.2f at "
              "kz%d); EXT5 max %.2f at kz%d; kz79 F_ins %.2f; "
              "rc_small %+.3f"
              % (len(allrows), c_fab89, c_fab89_kz, R351_CFAB,
                 R351_CFAB_KZ, x5max["fab"], x5max["kz"],
                 fins79, rc_small89))
        fam_all89 = [r for r in allrows if r["cls"] == "SPIKE"]
        rsv_min89 = min(r["rsv"] for r in fam_all89)
        rsv_min89_kz = min(fam_all89,
                           key=lambda r: r["rsv"])["kz"]
        e_rsv89 = L2D.halves_slope(
            [r["m"] for r in sorted(fam_all89,
                                    key=lambda r: r["m"])],
            [max(r["rsv"], 1e-300)
             for r in sorted(fam_all89, key=lambda r: r["m"])])
        rc_fam89 = CCP.spearman_rank(
            [r["fa"] for r in fam_all89],
            [r["rsv"] for r in fam_all89])
        x5_spk = [r for r in allrows if r["coh"] == "EXT5"
                  and r["cls"] == "SPIKE"]
        c_m2env89 = max(r["ev"]["mqs"]["m2"] for r in allrows)
        c_k2_83 = max(r["fab"] * r["grel"] for r in allrows
                      if r["coh"] != "EXT5")
        rc_gap89 = CCP.spearman_rank(
            [r["grel"] for r in fam_all89],
            [r["fab"] for r in fam_all89])
        cnt_rows89 = [r for r in allrows
                      if r["coh"] in ("EXT4", "EXT5")]
        res_nsc89 = min(FROZEN_CNSC / max(r["nscl"], 1e-300)
                        for r in cnt_rows89)
        res_ng89 = min(FROZEN_CNG / max(r["ngl"], 1e-300)
                       for r in cnt_rows89)

        def solve_m0(log_rhs):
            t = math.log(73.0)
            while t < 1e7:
                if CRIT_EXP * t >= log_rhs(t):
                    return t / math.log(10.0)
                t *= 1.02
            return None

        m0_law89 = solve_m0(lambda t: math.log(
            max(c_fab89 * c_m2env89 * t, 1e-300)))
        check("G55-r351-floor-record",
              len(fam_all89) == R351_FAM_N
              and abs(rsv_min89 - R351_MINRSV) <= R351_MINRSV_TOL
              and rsv_min89_kz == R351_MINRSV_KZ
              and abs(e_rsv89 - R351_ERSV) <= R351_SLOPE_TOL
              and abs(rc_fam89 - R351_RCFAM) <= R351_SLOPE_TOL
              and all(R351_X5_RSV_LO - R351_X5_RSV_TOL
                      <= r["rsv"]
                      <= R351_X5_RSV_HI + R351_X5_RSV_TOL
                      for r in x5_spk)
              and abs(c_m2env89 - R351_M2ENV) <= R351_M2ENV_TOL
              and m0_law89 is not None
              and abs(m0_law89 - R351_M0LAW) <= R351_M0LAW_TOL
              and abs(c_k2_83 - R351_CK2_83) <= R351_CK2_TOL
              and abs(rc_gap89 - R351_RCGAP) <= R351_SLOPE_TOL
              and abs(res_nsc89 - R351_CNT_RES[0])
              <= R351_CNT_RES_TOL
              and abs(res_ng89 - R351_CNT_RES[1])
              <= R351_CNT_RES_TOL,
              "THE r351 FLOOR RECORD reproduced: %d family rows; "
              "min RSV %.2f at kz%d; e_RSV %+.3f; rc_fam %+.3f; "
              "C_M2ENV %.2f; law m_0* 10^%.1f; C_K2(83) %.2f; "
              "rc_gap %+.3f; count reserves %.2f/%.2f"
              % (len(fam_all89), rsv_min89, rsv_min89_kz,
                 e_rsv89, rc_fam89, c_m2env89, m0_law89,
                 c_k2_83, rc_gap89, res_nsc89, res_ng89))
        # ---- THE r353 FRAME-B RECORD (regate)
        b_rows = []
        for rc in srt_fb:
            ev = rc["ev"]
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            pk = ev["mqs"]["qm"]
            pst = ev["pst"]
            hst = ev["hst"]
            b_rows.append(dict(
                coh="FAMB", kz=rc["kz"], N=rc["N"], m=mloc,
                lg=lgl, pk=pk,
                fab=QGL.fab_of(float(mloc), pk, lgl),
                pil=pst["pil"], nscl=pst["nsc_rel"] / lgl,
                ngl=hst["ngj"] / lgl, hgn=hst["hgn"],
                bsh=hst["bshare"], ev=ev))
        grel_b2 = EFA.grel_col([r["kz"] for r in b_rows],
                               core.G_ALL)
        for r, g in zip(b_rows, grel_b2):
            r["grel"] = g
        c_k2x = max(r["fab"] * r["grel"] for r in allrows)
        fbk2max = max(r["fab"] * r["grel"] for r in b_rows)
        g_min353 = min(r["grel"] for r in b_rows + fam_all89)
        fab_max_353 = max([r["fab"] for r in allrows]
                          + [r["fab"] for r in b_rows])
        impl353 = c_k2x / max(g_min353, 1e-300)
        c_m2env_p = max([r["ev"]["mqs"]["m2"] for r in allrows]
                        + [r["ev"]["mqs"]["m2"]
                           for r in b_rows])
        m0_353 = solve_m0(lambda t: math.log(
            max(fab_max_353 * c_m2env_p * t, 1e-300)))
        res_nsc_b = min(FROZEN_CNSC / max(r["nscl"], 1e-300)
                        for r in b_rows)
        res_ng_b = min(FROZEN_CNG / max(r["ngl"], 1e-300)
                       for r in b_rows)
        fb_tab_ok = all(
            abs(next(r["fab"] for r in b_rows if r["kz"] == kz)
                - R353_FB_TABLE[kz][0]) <= R353_FB_FAB_TOL
            and abs(next(r["grel"] for r in b_rows
                         if r["kz"] == kz)
                    - R353_FB_TABLE[kz][1]) <= R353_FB_GREL_TOL
            for kz in R353_FB_TABLE)
        check("G56-r353-frameb-record",
              fb_tab_ok
              and abs(c_k2x - R353_CK2X) <= R353_CK2X_TOL
              and abs(fbk2max - R353_FB_K2MAX)
              <= R353_FB_K2MAX_TOL
              and abs(g_min353 - R353_GMIN) <= R353_GMIN_TOL
              and abs(impl353 - R353_IMPL) <= R353_IMPL_TOL
              and abs(c_m2env_p - R353_M2ENV) <= R353_M2ENV_TOL
              and m0_353 is not None
              and abs(m0_353 - R353_M0) <= R353_M0_TOL
              and abs(res_nsc_b - R353_CNT_RES[0])
              <= R353_CNT_RES_TOL
              and abs(res_ng_b - R353_CNT_RES[1])
              <= R353_CNT_RES_TOL,
              "THE r353 FRAME-B RECORD reproduced: 8-row FAB/"
              "grel table within tol %s; C_K2X = %.2f (rec "
              "%.2f); frame-B K2 max %.2f (rec %.2f); g_min "
              "%.3f -> implied %.1f (rec %.3f -> %.1f); "
              "C_M2ENV' %.2f; two-family m_0* 10^%.1f (rec "
              "10^%.1f); count reserves %.2f/%.2f"
              % ("OK" if fb_tab_ok else "BROKEN", c_k2x,
                 R353_CK2X, fbk2max, R353_FB_K2MAX, g_min353,
                 impl353, R353_GMIN, R353_IMPL, c_m2env_p,
                 m0_353, R353_M0, res_nsc_b, res_ng_b))

    # ---------------- S6: Leg A -- the K2 source anatomy
    section("S6  LEG A -- THE K2 SOURCE ANATOMY (THE CHAIN "
            "TABLE + THE C_H/C_P FREEZES)")
    if smoke:
        check("G60-k2-anatomy", True, "SMOKE: skipped")
        check("G61-ch-cp-freeze", True, "SMOKE: skipped")
        nu_rows = []
    else:
        # the NU rows (test + fresh), full K2 columns
        nu_rows = []
        for rc in ntrecs_ok + ncrecs_ok:
            ev = rc["ev"]
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            pk = ev["mqs"]["qm"]
            pst = ev["pst"]
            hst = ev["hst"]
            nu_rows.append(dict(
                coh="NUT" if rc in ntrecs_ok else "NUC",
                kz=rc["kz"], nu=rc["nu"], N=rc["N"], m=mloc,
                lg=lgl, pk=pk,
                fab=QGL.fab_of(float(mloc), pk, lgl),
                pil=pst["pil"], nscl=pst["nsc_rel"] / lgl,
                ngl=hst["ngj"] / lgl, hgn=hst["hgn"],
                bsh=hst["bshare"], ev=ev))
        grel_nu = EFA.grel_col([r["kz"] for r in nu_rows],
                               core.G_ALL)
        for r, g in zip(nu_rows, grel_nu):
            r["grel"] = g
        rows89 = allrows
        rows_all = rows89 + b_rows + nu_rows
        info("THE K2 ANATOMY TABLE (family rows of both "
             "families + NU rows; kz nu m grel | FAB FABg | "
             "ngj/lg hgn hgn*g | pil pil*g nsc/lg | bshare):")
        show = [r for r in rows89 if r["cls"] == "SPIKE"] \
            + b_rows + nu_rows
        for r in sorted(show, key=lambda r: -(r["fab"]
                                              * r["grel"])):
            info("  kz%-4d NU%d m %-4d g %.3f | FAB %6.2f FABg "
                 "%5.2f | ngj/lg %.2f hgn %6.2f hgn*g %6.2f | "
                 "pil %6.2f pil*g %6.2f nsc/lg %.2f | bsh %.2f"
                 % (r["kz"], r.get("nu", NU_A) if "nu" in r
                    else (NU_B if r.get("coh") == "FAMB"
                          else NU_A),
                    r["m"], r["grel"], r["fab"],
                    r["fab"] * r["grel"], r["ngl"], r["hgn"],
                    r["hgn"] * r["grel"], r["pil"],
                    r["pil"] * r["grel"], r["nscl"], r["bsh"]))
        bsh_fam = [r["bsh"] for r in rows89
                   if r["cls"] == "SPIKE"] \
            + [r["bsh"] for r in b_rows]
        bsh_all = [r["bsh"] for r in rows_all]
        check("G60-k2-anatomy", True,
              "THE CHAIN, typed per link: FAB grel == (m q_max/"
              "lg) grel [SATZ: r324 identity, warded %.1e] <= "
              "(ngj/lg)(hgn grel) [SATZ: r327 group chain, "
              "one-sided warded %.1e] with q_max == max y/m "
              "[DICTIONARY: FDD, warded %.1e] and grel entering "
              "the construction EXACTLY via the mesh h = NU u + "
              "(0, %.1f] [SATZ, warded on %s zones]; the "
              "dominant-atom picture: bshare med %.2f (family) "
              "/ %.2f (all %d rows) -- the heavy group carries "
              "the argmax block; the REMAINING census links: "
              "ngj/lg <= C_NG [r329, 4 cohorts] and hgn grel <= "
              "C_H [THIS round's freeze, next gate]"
              % (fabid_w, k2ch_w, dictq_w, MESH_DEV_HI,
                 str(tuple(mesh_n[k] for k in sorted(mesh_n))),
                 float(np.median(bsh_fam)),
                 float(np.median(bsh_all)), len(rows_all)))
        # THE C_H / C_P FREEZES (sealed rule: max over the 89
        # sealed r351 rows), tested on frame-B + NU rows
        c_h = max(r["hgn"] * r["grel"] for r in rows89)
        c_h_kz = max(rows89,
                     key=lambda r: r["hgn"] * r["grel"])["kz"]
        c_p = max(r["pil"] * r["grel"] for r in rows89)
        c_p_kz = max(rows89,
                     key=lambda r: r["pil"] * r["grel"])["kz"]
        test_rows = b_rows + nu_rows
        ch_viol = [(r["kz"], r.get("nu", NU_B),
                    round(r["hgn"] * r["grel"], 2))
                   for r in test_rows
                   if r["hgn"] * r["grel"] > c_h + K2_EPS]
        cp_viol = [(r["kz"], r.get("nu", NU_B),
                    round(r["pil"] * r["grel"], 2))
                   for r in test_rows
                   if r["pil"] * r["grel"] > c_p + K2_EPS]
        max_fg_all = max(r["fab"] * r["grel"] for r in rows_all)
        impl_h = FROZEN_CNG * c_h
        impl_p = FROZEN_CNSC * c_p
        h_go = (not ch_viol) and impl_h <= IMPL_FAC * max_fg_all
        p_go = (not cp_viol) and impl_p <= IMPL_FAC * max_fg_all
        tail_max = max(
            (r["ev"]["pst"]["tail"]
             / max(r["ev"]["pst"]["a1j"], 1e-300))
            for r in rows_all)
        check("G61-ch-cp-freeze", True,
              "THE NEW CENSUS CAPS (frozen on the 89 sealed "
              "rows, columns never measured before): C_H = max "
              "hgn grel = %.2f (kz%d) -> implied ceiling C_NG "
              "C_H = %.1f; C_P = max pil grel = %.2f (kz%d) -> "
              "implied C_NSC C_P = %.1f; test on %d frame-B + "
              "%d NU rows: C_H %s / C_P %s; non-vacuity bar "
              "IMPL_FAC x max FABg = %.1f x %.2f = %.1f -> h_go "
              "%s / p_go %s; the nsc-vs-nsc_rel tail gap "
              "(honest, r351 convention): max tail share %.3f"
              % (c_h, c_h_kz, impl_h, c_p, c_p_kz, impl_p,
                 len(b_rows), len(nu_rows),
                 "0 viol" if not ch_viol
                 else "VIOL %s" % str(ch_viol),
                 "0 viol" if not cp_viol
                 else "VIOL %s" % str(cp_viol),
                 IMPL_FAC, max_fg_all, IMPL_FAC * max_fg_all,
                 str(h_go), str(p_go), tail_max))

    # ---------------- S7: Leg B -- the frozen C_2 test + NU test
    section("S7  LEG B -- THE FROZEN C_2 TEST + THE NU TEST + "
            "THE FRESH FIELD")
    if smoke:
        check("G70-c2-freeze-test", True, "SMOKE: skipped")
        check("G71-nu-test", True, "SMOKE: skipped")
        check("G72-fresh-count-test", True, "SMOKE: skipped")
        k2_viol = []
        nu_complete = False
    else:
        c_2 = c_k2x  # the sealed freeze rule: max FABg, 89 rows
        k2_viol = [(r["kz"], r.get("nu", NU_B),
                    round(r["fab"] * r["grel"], 2))
                   for r in b_rows + nu_rows
                   if r["fab"] * r["grel"] > c_2 + K2_EPS]
        k2max_t = max(b_rows + nu_rows,
                      key=lambda r: r["fab"] * r["grel"])
        check("G70-c2-freeze-test", True,
              "THE THEOREM CANDIDATE 'grel >= g => FAB <= "
              "C_2/g' at the FROZEN C_2 = %.2f (max FAB grel, "
              "89 sealed rows; the r353 record pin): test on %d "
              "frame-B + %d NU-test + %d fresh rows: %s; max "
              "test product %.2f at kz%d NU%d"
              % (c_2, len(b_rows),
                 sum(1 for r in nu_rows if r["coh"] == "NUT"),
                 sum(1 for r in nu_rows if r["coh"] == "NUC"),
                 "0 violations -- the K2 form carries"
                 if not k2_viol
                 else "VIOLATIONS %s -- C_2 is "
                 "ASPECT/FAMILY-INDEXED" % str(k2_viol),
                 k2max_t["fab"] * k2max_t["grel"],
                 k2max_t["kz"], k2max_t.get("nu", NU_B)))
        # the NU table: same zones at NU 2/3/4
        fab4_by = {r["kz"]: r["fab"] for r in rows89}
        g_by = {r["kz"]: r["grel"] for r in rows89}
        nut_by = {}
        for r in nu_rows:
            if r["coh"] == "NUT":
                nut_by[(r["kz"], r["nu"])] = r
        ratios = []
        info("THE NU TABLE (kz grel | FAB @ NU2/NU3/NU4 | FABg "
             "@ NU2/NU3/NU4):")
        for kz in NU_TEST_KZ:
            f2 = nut_by.get((kz, 2))
            f3 = nut_by.get((kz, 3))
            f4 = fab4_by.get(kz)
            gg = g_by.get(kz, 0.0)
            if f2 is not None and f4:
                ratios.append(f2["fab"] / f4)
            info("  kz%-4d g %.3f | %s / %s / %.2f | %s / %s / "
                 "%.2f"
                 % (kz, gg,
                    ("%.2f" % f2["fab"]) if f2 else "--",
                    ("%.2f" % f3["fab"]) if f3 else "--",
                    f4 if f4 else 0.0,
                    ("%.2f" % (f2["fab"] * gg)) if f2 else "--",
                    ("%.2f" % (f3["fab"] * gg)) if f3 else "--",
                    (f4 * gg) if f4 else 0.0))
        n_nut = len([r for r in nu_rows if r["coh"] == "NUT"])
        per_nu = {nu: sum(1 for r in nu_rows
                          if r["coh"] == "NUT"
                          and r["nu"] == nu)
                  for nu in NU_TEST_NUS}
        n_nuc = len([r for r in nu_rows if r["coh"] == "NUC"])
        nu_complete = (n_nut >= NUT_MIN
                       and all(per_nu[nu] >= NUT_PER_NU_MIN
                               for nu in NU_TEST_NUS)
                       and n_nuc >= FRESH_MIN_C)
        med_ratio = float(np.median(ratios)) if ratios else 0.0
        check("G71-nu-test", True,
              "THE NU TEST: %d/12 test rows admitted (per "
              "aspect %s; post-eval drops %s), %d fresh NU_C "
              "rows -> NU-completeness %s (bars %d total / %d "
              "per aspect / %d fresh); grel is NU-FREE by "
              "construction (zone property); FAB(NU2)/FAB(NU4) "
              "med ratio %.2f (census) -- the K2 product moves "
              "with the aspect EXACTLY as FAB does"
              % (n_nut, str(per_nu), str(nu_mult_drop), n_nuc,
                 str(nu_complete), NUT_MIN, NUT_PER_NU_MIN,
                 FRESH_MIN_C, med_ratio))
        cnt_viol_nu = [(r["kz"], r["nu"], round(r["nscl"], 2),
                        round(r["ngl"], 2)) for r in nu_rows
                       if r["nscl"] > FROZEN_CNSC
                       or r["ngl"] > FROZEN_CNG]
        check("G72-fresh-count-test", True,
              "THE COUNT TEST (r329 FROZEN constants, first "
              "ASPECT-ROBUSTNESS measurement): nsc_rel/lg <= "
              "%.4f AND ngj/lg <= %.4f on %d NU rows: %s; min "
              "count reserves NSC %.2f / NG %.2f -- the O(log "
              "m) counting side vs the aspect change"
              % (FROZEN_CNSC, FROZEN_CNG, len(nu_rows),
                 "0 violations" if not cnt_viol_nu
                 else "VIOLATIONS %s" % str(cnt_viol_nu),
                 min((FROZEN_CNSC / max(r["nscl"], 1e-300)
                      for r in nu_rows), default=0.0),
                 min((FROZEN_CNG / max(r["ngl"], 1e-300)
                      for r in nu_rows), default=0.0)))

    # ---------------- S8: Leg C -- the g_min(u) curve
    section("S8  LEG C -- THE LOWER GAP BOUND g_min(u) (THE "
            "MEASURED CURVE, NO BAKER)")
    if smoke:
        check("G80-gmin-curve", True, "SMOKE: skipped")
        check("G81-gmin-arithmetic", True, "SMOKE: skipped")
        gmin_let = "GMIN_CENSUS_SMOKE"
    else:
        zone_kz = [kz for kz in range(2, core.NZ_DEEP - 2)
                   if core.atoms_in(float(core.U_ALL[kz]))
                   >= core.N_ATOM_MIN
                   and int(core._NN[kz]) ** 2 <= Z2_CAP]
        zone_u = [float(core.U_ALL[kz]) / float(core.G_ALL[kz])
                  for kz in zone_kz]
        zone_g = EFA.grel_col(zone_kz, core.G_ALL)
        bins = gmin_bins(zone_u, zone_g, MIN_ZONES_BIN)
        e_g, mono = curve_stats(bins)
        gmin_let = gmin_letter_rule(e_g, mono, E_FLAT_G,
                                    MONO_BAR)
        g_pool_min = min(zone_g)
        g_pool_kz = zone_kz[int(np.argmin(zone_g))]
        info("THE g_min(u) CURVE (%d admissible zones, z^2 <= "
             "%d; dyadic u bins, floor %d):"
             % (len(zone_kz), Z2_CAP, MIN_ZONES_BIN))
        for u_med, g_min_b, n_b in bins:
            info("  u_med %8.1f | g_min %.3f | zones %d"
                 % (u_med, g_min_b, n_b))
        check("G80-gmin-curve", True,
              "THE SEALED CURVE LETTER: %s (e_g = %+.3f vs flat "
              "bar %.2f; mono frac %.2f vs %.2f; %d bins); "
              "global pool floor g_min = %.3f at kz%d; the "
              "diophantine reading is typed CENSUS by contract "
              "(distances of prime-power logs -- NO Baker "
              "bounds, the r289/r331 lesson); DISCLOSED: the "
              "depth-gap coupling h = NU u means deep zones ARE "
              "small-gap zones -- the falling envelope partly "
              "reflects the construction, said out loud"
              % (gmin_let, e_g, E_FLAT_G, mono, MONO_BAR,
                 len(bins), g_pool_min, g_pool_kz))
        # the implied arithmetic (census)
        adm = sorted(rows_all, key=lambda r: float(
            core.U_ALL[r["kz"]]) / float(core.G_ALL[r["kz"]]))
        u_adm = [float(core.U_ALL[r["kz"]])
                 / float(core.G_ALL[r["kz"]]) for r in adm]
        m_adm = [r["m"] for r in adm]
        e_um = L2D.halves_slope(u_adm, m_adm)
        e_impl = -e_g / max(e_um, 1e-300)
        u_ref, g_ref, _n = bins[-1]
        m_ref = float(np.median(m_adm))
        u_med_all = float(np.median(u_adm))

        def gmin_at_logm(t):
            # g_min(m) = g_ref (m/m_ref)^(e_g/e_um), census map
            return math.log(max(g_ref, 1e-300)) \
                + (e_g / max(e_um, 1e-300)) \
                * (t - math.log(max(m_ref, 1e-300)))

        m0_grow = solve_m0(lambda t: math.log(
            max(c_2 * c_m2env_p * t, 1e-300)) - gmin_at_logm(t))
        m0_flat = solve_m0(lambda t: math.log(
            max(c_2 / max(g_pool_min, 1e-300)
                * c_m2env_p * t, 1e-300)))
        check("G81-gmin-arithmetic", True,
              "THE IMPLIED CEILING ARITHMETIC (census, printed "
              "at every letter): m <-> u map e_um = %+.3f over "
              "the %d admitted rows (u med %.0f); e_impl = "
              "-e_g/e_um = %+.3f vs CRIT_EXP %.3f -> the "
              "growing-law route m_0* = %s (solve at C_2 "
              "C_M2ENV'/g_min(m)); the flat-floor route at the "
              "global pool floor %.3f: C_FAB^K2 = C_2/g = %.1f "
              "-> m_0* = %s"
              % (e_um, len(adm), u_med_all, e_impl, CRIT_EXP,
                 ("10^%.1f" % m0_grow)
                 if m0_grow is not None else "NONE "
                 "(supercritical -- no uniform horizon on this "
                 "route)",
                 g_pool_min, c_2 / max(g_pool_min, 1e-300),
                 ("10^%.1f" % m0_flat)
                 if m0_flat is not None else "NONE"))

    # ---------------- S9: Leg D -- composition + verdict
    section("S9  LEG D -- THE COMPOSITION + COFINAL TYPING + "
            "VERDICT ASSEMBLY")
    if smoke:
        check("G85-composition", True, "SMOKE: skipped")
        check("G86-cofinal-typing", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        info("THE m_0* TABLE (typed):")
        info("  r351 law route (89 rows, record):     10^%.1f"
             % m0_law89)
        info("  r353 two-family route (record):       10^%.1f"
             % m0_353)
        info("  K2 flat-floor route (C_2/g_min,pool): %s"
             % (("10^%.1f" % m0_flat)
                if m0_flat is not None else "NONE"))
        info("  K2 growing-law route (g_min(m)):      %s"
             % (("10^%.1f" % m0_grow)
                if m0_grow is not None else "NONE"))
        check("G85-composition", True,
              "THE TWO-THEOREM COVER retyped: arm 1 = the K2 "
              "candidate 'FAB <= C_2/g' -- status %s at the "
              "frozen C_2 = %.2f (max measured product %.2f); "
              "arm 2 = the frame-A three-arm cover -- bounded "
              "to its measured range (r353 FLOOR_KILLS, "
              "unchanged); the K2 route's m_0*: flat %s / "
              "growing %s vs the r353 direct census 10^%.1f -- "
              "the K2 detour is %s than the direct FAB census "
              "at current constants"
              % ("0 violations" if not k2_viol
                 else "BROKEN %s" % str(k2_viol), c_2,
                 max_fg_all,
                 ("10^%.1f" % m0_flat)
                 if m0_flat is not None else "NONE",
                 ("10^%.1f" % m0_grow)
                 if m0_grow is not None else "NONE", m0_353,
                 ("cheaper" if m0_flat is not None
                  and m0_flat < m0_353 else "MORE EXPENSIVE")))
        leak = bool(sc_own) or bool(pure_lits)
        brk_struct = (norm_w > DEC_BAR or interp_w > CHAIN_BAR
                      or fabid_w > FAB_ID_BAR
                      or pile_w > CHAIN_BAR
                      or pilerec_w > GRP_CHAIN_BAR
                      or grp_w > CHAIN_BAR
                      or k2ch_w > CHAIN_BAR
                      or dec_w > DEC_BAR or chainD_w > DEC_BAR
                      or chain_w > CHAIN_BAR
                      or fab_dev != 0 or fd_dev != 0
                      or not k2toy_ok or not meshtoy_ok
                      or not gmintoy_ok
                      or frb_dev > FRB_WARD_BAR
                      or not frame_ok or not mesh_ok
                      or not nufresh_ok)
        vkey = k2_main_tree(leak, brk_struct, bool(k2_viol),
                            nu_complete)
        src_let = k2_source_letter(not brk_struct, h_go, p_go)
        check("G86-cofinal-typing", True,
              "COFINAL TYPING at the %s reading: SATZ-grade "
              "links = the r324 identity, the r327 group chain, "
              "the mesh identity (grel -> depth), the "
              "dictionary q_max; CENSUS links = C_NG (4 "
              "cohorts + this round's aspect test), C_H/C_P "
              "(%s), C_2 itself (%s), and g_min (%s -- the "
              "diophantine rest); the WHOLE spike mechanism "
              "reduces to: [gap floor g_min] x [counting C_NG] "
              "x [heavy-group mass cap] -- what is missing for "
              "a cofinal statement is EXACTLY the census-to-"
              "law promotion of those three, none of which "
              "this round (or any) can settle by measurement"
              % (vkey,
                 src_let, "frozen, %d viol" % len(k2_viol),
                 gmin_let))
        flags = [src_let, "%s(e_g %+.3f, mono %.2f)"
                 % (gmin_let, e_g, mono)]
        flags.append("INZONE_EXHAUSTED_ALL_NU(%d)" % len(cz_q))
        flags.append("K2_TEST_MAX(kz%d, NU%d, %.2f)"
                     % (k2max_t["kz"], k2max_t.get("nu", NU_B),
                        k2max_t["fab"] * k2max_t["grel"]))
        if h_go:
            flags.append("CH_CANDIDATE(%.2f, %.1f)"
                         % (c_h, impl_h))
        if p_go:
            flags.append("CP_CANDIDATE(%.2f, %.1f)"
                         % (c_p, impl_p))
        if gmin_let in ("GMIN_FLAT", "GMIN_LAW"):
            flags.append("GMIN_IMPLIED(%s, e_impl %+.2f)"
                         % (("10^%.1f" % m0_grow)
                            if m0_grow is not None else "NONE",
                            e_impl))
        flags.append("NU_RATIO_CENSUS(med %.2f)" % med_ratio)
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a "
                           "module-own builder",
            "LAW_STATE_NOT_EXACT":
                "an exact ward broke (NORM %.1e / K2 chain "
                "%.1e / mesh %s / toys)"
                % (norm_w, k2ch_w,
                   "OK" if mesh_ok else "BROKEN"),
            "K2_FAMILY_INDEXED":
                "%s -- the frozen C_2 does NOT survive the "
                "aspect/selection change: the gap language is "
                "census too" % str(k2_viol),
            "K2_LAW_CERTIFIED_NU_FREE":
                "0 violations on frame-B + %d NU rows at the "
                "frozen C_2 = %.2f" % (len(nu_rows), c_2),
            "K2_HOLDS_CENSUS":
                "0 violations but the NU surface is thin "
                "(completeness %s)" % str(nu_complete)}
        verdict_main = "%s(%s)%s" % (
            vkey, det_v[vkey],
            ("".join(" + " + f for f in flags))
            if flags else "")

    # ---------------- S10: Leg E -- worlds + must-fails + verdict
    section("S10  LEG E -- WORLDS + MUST-FAILS + VERDICT")
    if smoke:
        pb9 = SFE.wpack_b(9, NU_B)
        check("G90-world-census", pb9["complete"],
              "SMOKE: frame-B w9 built (N %d, nf %s); twin + "
              "EPST K2 census + SCRAMBLE-B skipped"
              % (pb9["N"], pb9["nf"]))
    else:
        wlines = []
        for wkz, lab in ((9, "w9B"), (13, "w13B(twin)")):
            pbw = SFE.wpack_b(wkz, NU_B)
            if pbw["nf"] is None and pbw["complete"]:
                rcw = rung_rec(pbw)
                rcw["ev"] = eval_rung(rcw)
                ev = rcw["ev"]
                mloc = ev["m"]
                lgl = math.log(float(mloc))
                fab_w = QGL.fab_of(float(mloc),
                                   ev["mqs"]["qm"], lgl)
                g_w = EFA.grel_col([wkz], core.G_ALL)[0]
                wlines.append("%s m %d FAB %.2f grel %.3f FABg "
                              "%.2f" % (lab, mloc, fab_w, g_w,
                                        fab_w * g_w))
            else:
                wlines.append("%s NOT admitted (nf %s)"
                              % (lab, pbw["nf"]))
        ev_e = crecs["EPST"]["ev"]
        m_e = ev_e["m"]
        fab_e = QGL.fab_of(float(m_e), ev_e["mqs"]["qm"],
                           math.log(float(m_e))) if m_e else 0.0
        g_e = EFA.grel_col([9], core.G_ALL)[0]
        alpha80 = float(core.U_ALL[80])
        ka80 = core.atoms_in(alpha80)
        rng = np.random.default_rng(SCR_SEED_B)
        uu_scr = np.sort(rng.uniform(0.0, 2.0 * alpha80,
                                     size=ka80))
        pscr = SFE.wpack_b(80, NU_B,
                           comb=(uu_scr,
                                 core.MU_ALL[:ka80].copy()))
        check("G90-world-census", pscr["nf"] is not None,
              "K2 WORLD CENSUS (no letter): %s; EPSTEIN (frame "
              "A) FAB %.2f grel %.3f FABg %.2f; frame-B "
              "SCRAMBLE @ kz80 (seed %d) %s (nf %s; the r353 "
              "record: breaks at admission, nf 3) -- the dead "
              "control stays dead"
              % ("; ".join(wlines), fab_e, g_e, fab_e * g_e,
                 SCR_SEED_B,
                 "BREAKS AT ADMISSION"
                 if pscr["nf"] is not None
                 else "unexpectedly admits", str(pscr["nf"])))
    check("G91-e1-hfun-posthoc",
          len(e1_hits) >= 1 and tuple(mut1) == (4.0, 1.0)
          and mut1 != toy1_sealed,
          "e1 protocol-CAUGHT twice: the cap function h(grel) "
          "read back from the seen column -- AST-FLAGGED (%s) "
          "-- and on the toy returns %s != the sealed "
          "constant-over-grel rule %s (C_2 is frozen on the "
          "sealed 89-row surface BEFORE any test)"
          % (e1_hits[0] if e1_hits else "MISS",
             str(tuple(mut1)), str(toy1_sealed)))
    check("G92-e2-c2-posthoc",
          len(e2_hits) >= 1 and abs(mut2 - 3.0) <= TOY_BAR
          and mut2 != toy2_sealed,
          "e2 protocol-CAUGHT twice: C_2 set after sight of the "
          "violation column -- AST-FLAGGED (%s) -- and on the "
          "toy returns %.1f != the sealed toy freeze %.1f"
          % (e2_hits[0] if e2_hits else "MISS", mut2,
             toy2_sealed))
    check("G93-e3-nu-shared",
          len(e3_hits) >= 1 and tuple(mut3) == (1.0, 2.0)
          and mut3 != toy3_fresh and nufresh_ok,
          "e3 protocol-CAUGHT twice: the NU test contaminated "
          "with shared zone data -- AST-FLAGGED (%s) -- and on "
          "the toy the mutant returns the NU4 column %s "
          "verbatim != the fresh-build column %s; the LIVE "
          "freshness ward (strict depth ordering) additionally "
          "guards every admitted NU-test zone"
          % (e3_hits[0] if e3_hits else "MISS",
             str(tuple(mut3)), str(toy3_fresh)))
    check("G94-e4-fab-wrong-log",
          mut4 == Fr(3, 8) and toy4_true == Fr(3, 4)
          and toy4_true / mut4 == Fr(2),
          "e4 CAUGHT exact: the wrong log power returns %s on "
          "the sealed Fractions toy while the exact FAB is %s "
          "-- break factor %s == the pseudo-log EXACT"
          % (str(mut4), str(toy4_true),
             str(toy4_true / mut4)))
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact K2 chain with typed links, the "
          "C_H/C_P census caps, the frozen-C_2 aspect test at "
          "NU 2/3/4 + a fresh third-aspect field, and the "
          "measured g_min(u) curve -- NO new certificate "
          "promoted, NO universal bound claimed beyond the "
          "measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R355_ANCHORS(identity %.1e, r306 C2 %.3f, "
                 "r316 n %d, dict %.1e, r321 FA %.2f/%.2f/%.2f, "
                 "r349 family %d + EXT4, r324 C_INF %.4f, r329 "
                 "%.4f/%.4f, r351 C_FAB %.2f @ kz%d + floor, "
                 "r353 frame-B 8/8 + C_K2X %.2f)"
                 % (rec3_w, C2r, n355, dict3_w, fa_kz[53],
                    fa_kz[83], fa_kz[67], len(fam_idx),
                    cinf_repro, cnsc_repro, cng_repro, c_fab89,
                    c_fab89_kz, c_k2x)]
        parts.append("SEAL(NORM %.1e, FAB id %.1e, K2 chain "
                     "%.1e, mesh EXACT %s zones, NU freshness "
                     "strict, purity clean, toys exact)"
                     % (norm_w, fabid_w, k2ch_w,
                        str(tuple(mesh_n[k]
                                  for k in sorted(mesh_n)))))
        parts.append("K2ANATOMY(C_H %.2f -> impl %.1f %s, C_P "
                     "%.2f -> impl %.1f %s, bshare med %.2f)"
                     % (c_h, impl_h,
                        "GO" if h_go else "no-go",
                        c_p, impl_p,
                        "GO" if p_go else "no-go",
                        float(np.median(bsh_all))))
        parts.append("K2LAW(C_2 %.2f, viol %d, NU %d/12 + "
                     "fresh %d, complete %s)"
                     % (c_2, len(k2_viol), n_nut, n_nuc,
                        str(nu_complete)))
        parts.append("GMIN(%s, e_g %+.3f, mono %.2f, pool "
                     "floor %.3f, e_impl %+.2f)"
                     % (gmin_let, e_g, mono, g_pool_min,
                        e_impl))
        parts.append(verdict_main)
        parts.append("COMPOSITION(m_0* flat %s / grow %s vs "
                     "r353 10^%.1f)"
                     % (("10^%.1f" % m0_flat)
                        if m0_flat is not None else "NONE",
                        ("10^%.1f" % m0_grow)
                        if m0_grow is not None else "NONE",
                        m0_353))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the identity, the "
          "chains, the mesh identity, the Fractions toys, the "
          "NU = 4 reproduction and the purity audits (exact / "
          "AST-decided); MEASURED: every FAB value, grel "
          "product, cap, count column and violation count (the "
          "finite 89-row r351 surface + the 8 r353 frame-B rows "
          "+ the admitted NU rows + 2 mains + 2 live controls + "
          "the worlds); OPEN: any bound beyond the measured "
          "rungs, the census-to-law promotion of C_2/C_NG/C_H/"
          "g_min, the diophantine gap floor, the cofinal law, "
          "the actual proof; NO RH claim"
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
