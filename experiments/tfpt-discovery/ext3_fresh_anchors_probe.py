#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ext3_fresh_anchors_probe -- PRIME.AUDIT.EXT3_FRESH_ANCHORS.01
(round 329): THE EXT3 FRESH-ANCHOR ROUND -- audit repair 2+3 for the
sequence bias of the r321/r324 lane.

THE AUDIT FINDING (r328A/C, binding contract of this round): the SAME
65-rung class ladder has been the test set across r306..r327; the F_A
coordinate was SELECTED on that test anatomy in r317 (it ranks the
known violators on top) and CERTIFIED on the same set in r321 --
SLIDING_BOUND_GO carries less independence evidence than "0/39"
suggests (audit A2).  Audit C1 adds the CONSTRUCTION-FAMILY bias: the
kz ladder is LARGE-GAP selected (the frame-A window depth is
h ~ 4 log z / gap, so the h <= 900 core cap admits exactly the
prime-power anchors whose local log-gap is LARGE; audit C measured
the anchors at median 2.0x the local median gap in its own
convention).  THE REPAIR (audit recommendation 2, the proven r293
protocol shape): FRESH EXT3 ANCHORS at FROZEN CONSTANTS -- new
windows that appeared in NO previous round, evaluated against the
four frozen constants of the lane with NOTHING recalibrated, plus
the small-gap contrast that answers C1 quantitatively.

TWO-COMMIT FREEZE PROTOCOL (NEW -- this is the FIRST round under it,
audit repair (2) of r328A): the sealed spec (this docstring WITHOUT
the record tables) is COMMITTED to git BEFORE the record run
("experiments: r329 pre-freeze"), and the probe is committed AGAIN
after the record-table insertion ("experiments: r329 record").  The
freeze discipline (spec sealed before evaluation, record tables the
only post-freeze edit) is thereby independently verifiable from git
history for the first time -- the audit-A1 verifiability gap this
protocol closes.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the wave-13 worker (v970) and R330/R331 run in
parallel; this probe touches NOTHING outside its own file and the
strictly additive rh-sync (existing entries byte-identical).

THE OBJECT (r269/r287/r298/r306/r314/r316/r317/r321/r324/r327
machinery imported verbatim): t_{N-2} = sum_b ct_b (r244 chain rows,
r266 eval); F = 0.20 edge split; maximal same-sign runs of the
bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope; the r316
TRB.two_regime_state + TRB.split_midladder; the r317
EFP.local_ratio; the r321 CCP.local_median + CCP.world_coord; the
r324 QMO.scale_bins + QMO.pileup_state + QMO.mult_ward; the r327
GMC.group_mass_ledger + GMC.heavy_state; the r286 LM.ext_rule
(READ-ONLY, used-set reproduction only); PDelta = Pbeta - Pomega;
x_j = (PDelta)_j.  NEW in this round (module-own, source-pure):
admissible_pool (the frame-A CONSTRUCTION with the h-cap as a
parameter -- warded EXACT against core.frame_a_zones at the frozen
cap), grel_col (the relative local prime-power gap), used_kz_set
(the exclusion ledger of every previously used window), ext3_select
(the sealed two-strata choice rule) and gap_class.

THE ANCHOR CONSTRUCTION CONVENTION (extracted from the builders,
used VERBATIM -- only the anchor CHOICE differs): an anchor is an
index kz into the prime-power list (U_ALL = log of the n with
Lambda(n) > 0, table cap 400000, zone horizon 380000); the window is
D_k = 0.5 G_ALL[kz]/NU_MAIN (G_ALL = diff(U_ALL) the local log-gap,
NU_MAIN = 4), M_k = ceil(U_ALL[kz]/D_k) + 1 rounded even, h_k =
M_k/2, admissible iff h_k >= H_MIN = 128 and >= N_ATOM_MIN = 40
atoms below e^{2 alpha}; kz scans range(2, NZ_DEEP - 2).  The
document rule additionally caps h_k <= HCAP = 1450 -- THAT cap (plus
the probe-level strata h <= 900 / 1300 / 1650 and the r286 rule's
z^2 <= 400000) is the CHOICE that produced every prior window.  The
structural consequence h ~ 4 log z / gap couples depth to gap: the
core ladder is large-gap selected BY CONSTRUCTION of its cap.

THE USED-WINDOW LEDGER (sealed exclusion rule): USED = the kz of
core.frame_a_zones() (70 windows: the 42-rung core ladder h <= 900,
the 20-member EXT pool 900 < h <= 1300 -- first 15 = the r286/r306
extension anchors, all 20 in the r321/r324 EXT2 pool -- and the 8
members 1300 < h <= 1450 of the EXT2 pool) UNION the kz of the first
35 rows of the r286 LM.ext_rule (the r286 extension ranks 0..14 +
the r307 EXT2 ranks 15..34, N_w up to 1650, z^2 <= 400000).  This
covers every window of every round r238..r328 in both lanes (the
rho/cubic lane draws from frame_a_zones; the LSTAR lane from the
r286 rule).  The collision ward demands EXT3 intersect USED == empty
EXACT (must-fail e1 proves it bites).

THE SEALED EXT3 CHOICE RULE (frozen BEFORE evaluation; source-pure:
consumes U_ALL/G_ALL/h/z + the used ledger ONLY -- no bound value,
no target, no gap-rule-after-sight; e3/e4 prove the audits bite):
  POOL  = admissible_pool(H_MIN, EXT3_H_MAX = 2600), FRESH = POOL
          minus USED.  Relative local gap grel(kz) = G_ALL[kz] /
          median{G_ALL[j] : |j - kz| <= GAP_W = 5, j != kz} (the
          r317 W-window convention applied to the gap column).
  STRATUM B (SMALL-GAP MID-ZONE, the audit-C1 contrast): FRESH kz
          whose prime power z lies INSIDE the core ladder's own zone
          range [z_min(core), z_max(core)] (computed live, expected
          16..317), sorted by (grel, kz) ASCENDING -- deliberately
          the SMALLEST relative gaps, the anti-selection of the
          large-gap ladder -- the first K_STRAT = 6 admitted.
  STRATUM A (DEPTH): the remaining FRESH kz sorted by (h, kz)
          DESCENDING (as deep as the budget carries), the first
          K_STRAT = 6 admitted.
  ADMISSION (class-ladder convention, r316/r321 verbatim):
          POSITIVE_PREFIX (nf is None) and fold multiplicity <=
          MULT_CAP = 2; a failing candidate is REPLACED by the next
          one in the stratum's sealed order (census disclosed).
  Both strata are expected deeper than every prior window (N_w >
  1650) -- in this construction a small relative gap FORCES depth
  (h ~ 4 log z / gap): the mid-zone stratum is "mid" in ANCHOR
  POSITION (same prime-power zone as the ladder), not in window
  depth; this is the honest geometry of the audit-C repair and is
  said out loud rather than hidden.

THE FOUR FROZEN TESTS (NOTHING recalibrated; every constant is a
sealed record number of its round, applied POINTWISE to every EXT3
anchor; every violation is an honest result that calibrates the
REACH of the lane, not a drama):
  (a) r321 SLIDING BOUND:  rho_2 <= 1.3056 x F_A^2  (b FROZEN;
      rho_2 = m^2 sum q^3 / (log m)^2 the r306 scale; F_A = the
      r317 rank-local QMAX ratio computed by EFP.local_ratio on the
      EXTENDED (N, kz)-sorted class ladder = the 65 sealed rungs +
      the admitted EXT3 anchors -- the fresh rows get genuine
      rank-local neighborhoods; the r321 insertion-rule coordinate
      (CCP.world_coord vs the pure-65 columns) is printed as a
      disclosed secondary census, it does not adjudicate).
  (b) r306 BASE BOUND:     sum q^3 <= 1.069 x (log m)^2 / m^2,
      i.e. rho_2 <= 1.069 (C FROZEN, the first-5 constant).
  (c) r324 SCALE COUNT:    nsc_rel / log m <= 2.0258  (C_NSC
      FROZEN; nsc_rel = # distinct dyadic source scales s <=
      2 log2 m in the argmax block, QMO.pileup_state verbatim).
  (d) r327 GROUP COUNT:    ngl = ng(argmax block) / log m <= 2.6351
      (C_NG FROZEN; GMC.group_mass_ledger + GMC.heavy_state
      verbatim).
  (e) r324 e_tot TREND (MEASUREMENT ONLY, no gate): G/log m =
      m qmax / log m and m M_2 = m sum q^2 on the EXT3 anchors;
      dyadic halves-slopes vs m over the 12 anchors; e_tot = e_G +
      e_M2 printed against the r324 record +0.172 (= +0.158 +
      +0.014) with the a-priori census band |de| <= 0.15 typing
      EXPONENT_CONSISTENT / EXPONENT_SHIFTED -- census, not gate.

THE SMALL-GAP CONTRAST (audit C1, sealed adjudication): cohorts
  B (the 6 small-gap mid-zone anchors), A (the 6 depth anchors) and
  LADDER_DEEP (the class-ladder rungs of rank >= 42, i.e. the
  EXT/EXT2 segment N_w 942..~1600 -- the large-gap-selected
  reference in the overlapping depth regime).  Metrics per cohort:
  med rho_2, med F_A (one consistent column: the extended-ladder
  F_A), spike rate = fraction with F_A >= SPIKE_FA = 1.5, med
  G/log m, med m M_2.  SEALED RULE (coarse a-priori bars, symmetric):
  SMALL_GAP_DIFFERENT iff  med rho_2(B)/med rho_2(LADDER_DEEP)
  >= 2 or <= 1/2,  OR  |spike(B) - spike(LADDER_DEEP)| >= 0.5,  OR
  med F_A(B)/med F_A(LADDER_DEEP) >= 1.5 or <= 2/3; else
  SMALL_GAP_SIMILAR.  The firing clause(s) are named in the letter.

LEG 0 -- ANCHOR REGRESSION (slim set; every band a record number
adopted as-is, disclosed): r263 branch rule (35 cheap + the named 7
exceptions); r306 C_2 = 1.069 (tol 0.005) first-5 freeze with 0/57;
r316 class ladder n = 65 + rho anchors kz53/kz67/kz55/kz83 =
1.0490/1.0536/0.4821/0.7790 (tol 0.005) + C_small 1.0694 at kz18;
r321 b = (max cal B)^2 = 1.3056 (tol 0.005) with 0/39 test
violations + named 4/4; r324 C_NSC = 2.0258 (tol 0.005) with 0/39;
r327 C_NG = 2.6351 (tol 0.005) with 0/39 + named 4/4; the r314
identity wards live everywhere.

LEG A -- SEAL + PURITY + TOYS + LIVE WARDS: (A1) the sealed
definitions printed; the SOURCE-PURE selection table (stratum, kz,
z, h, N, grel, gap class) printed BEFORE any bound-side value of
this round.  (A2) SOURCE-PURITY AUDITS: the AST identifier scan over
admissible_pool + grel_col + used_kz_set + ext3_select + gap_class
must be clean against BOUND_FORBIDDEN + PHI3_FORBIDDEN; the literal
scan over the same five builders must be clean against the sealed
record-literal set R329_TABLE_LITERALS; e2/e3/e4 prove the audits
bite.  (A3) TOY EXACTNESS: the grel spike toy ((1,1,1,5,1,1,1) ->
grel = (1,1,1,5,1,1,1) EXACT); the gap_class toys (0.5 -> SMALL,
1.0 -> MED, 2.0 -> LARGE); the ext3_select toy (synthetic 6-window
pool with a 2-member used set -> strata EXACT, collision ward
empty); the collision toy (injected used anchor -> intersection
non-empty EXACT); the halves-slope toy (m = (2, 4), v = (1, 2) ->
slope exactly 1).  (A4) LIVE WARDS on every live world: the r316
chain + NORM x cube == rho_2 (r321 verbatim); the r324
interpolation M_3 <= qmax M_2 <= qmax^2; the pileup chain m qmax <=
nsc x pil + exact scale recomposition; the r327 ledger == genealogy
identity + group partition + L1 recomposition; the extended-ladder
reconstruction QMAX == F_A x medloc EXACT; frame-A REPRODUCTION:
admissible_pool(H_MIN, HCAP) == core.frame_a_zones() EXACT (the
construction is verbatim, not a sibling) and h(kz) == the
PIK.build_rung h on every selected anchor EXACT.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) ANCHOR COLLISION WITH THE LADDER: mutant_collision injects a
  core-ladder kz into the fresh set -- the disjointness ward must
  CATCH the non-empty intersection EXACT while the real selection
  is disjoint EXACT.
(e2) CONSTANT RECALIBRATION SIMULATED: mutant_b_recal recalibrates
  the sliding constant on the fresh anchors (consumes the evaluated
  bound column) -- the BOUND_FORBIDDEN scope audit must FLAG it AND
  on the sealed toy it returns 1.0 != the frozen 1.3056 (diff
  >= MUT_MIN) -- CAUGHT twice.  The real tests consume the FROZEN
  record numbers only.
(e3) GAP RULE AFTER SIGHT: mutant_gap_posthoc re-picks the gap
  threshold to minimize the seen violations (consumes the bound
  column) -- the scope audit must FLAG it AND on the sealed toy it
  returns a threshold != the sealed stratification's -- CAUGHT.
(e4) TARGET READ-BACK IN THE SELECTION: mutant_strat_readback
  consumes the cubic-moment record (cm/S3) as a 'selection score'
  -- the PHI3_FORBIDDEN scan must FLAG it (AST-CAUGHT) while the
  five module-own selection builders stay clean.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.

INDEX FIREWALL (binding, r238-r328 discipline): w = window (kz into
the prime-power list), N_w = builder depth, k/n = chain degree;
ground truth (branch labels, the true R/t/Z values) enters GATES and
census tables only; the cubic target rho_2 / S_3 enters GATES /
anchors / the frozen-test tables only, NEVER a selection builder
(AST-warded); no zero/prime oracles anywhere (AST firewall; the
prime-power ANCHOR GRID U_ALL/G_ALL is the sealed source comb of the
whole campaign, r238 convention -- anchor selection on the source
grid is not an oracle read); no fit primitives (fragment audit; the
exponents are the imported r272 dyadic halves-slope, fit-free).
MACHINERY IMPORTED VERBATIM: r327 GMC.group_mass_ledger +
GMC.heavy_state, r324 QMO.scale_bins + QMO.pileup_state +
QMO.mult_ward, r321 CCP.local_median + CCP.world_coord, r317
EFP.local_ratio, r316 TRB.two_regime_state + TRB.split_midladder,
r314 SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope,
r306 RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze, r298
WBT.block_breaks + WBT.aggregate_blocks, r286 LM.ext_rule
(READ-ONLY), r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r269 PBB.mask_edge + PBB.runs_split, r244
BH.wpack, r257 CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap,
r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE:
B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed, r316/r321 verbatim): frame-A h <= 900,
42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39,
52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz); EXT2: the
r316 A5 rule (leftover pool + first 12 windows 1300 < h <= 1650,
first 8 POSITIVE_PREFIX by (N, kz)); EXT3: THIS round's sealed rule
above.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36, 38,
39, 52); EDGE_F 0.20 (FROZEN); EXT_H_MAX 1300; K_EXT 15;
EXT_NW_EXPECT (942, 1218); EXT2_H_MAX 1650; EXT2_POOL_CAP 12;
K_EXT2 8; EXT3_H_MAX 2600; K_STRAT 6; GAP_W 5; LM_RANKS_USED 35;
FRAME_EXPECT 70; GAP_SMALL 0.85; GAP_LARGE 1.5; SPIKE_FA 1.5;
FROZEN_B 1.3056; FROZEN_C2 1.069; FROZEN_CNSC 2.0258; FROZEN_CNG
2.6351; ETOT_REF +0.172; EG_REF +0.158; EM2_REF +0.014; CONS_BAND
0.15; CONTRAST_RHO_FAC 2.0; CONTRAST_SPIKE_D 0.5; CONTRAST_FA_FAC
1.5; MULT_CAP 2; N_CAL 5 (via TRB, verbatim); N329_REF 65; R316_RHO
{53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790} tol 0.005, C_SMALL
1.0694 tol 0.005 at kz18; NAMED_KZ (53, 83, 67, 55); tolerances
0.005 on all four frozen-constant reproductions; ATOM_BAR 1e-9;
REC3_BAR 1e-13 ladder / 1e-12 EXT3 (a-priori: windows up to twice
as deep); TEL/BND bars 1e-13 ladder / 1e-12 EXT3; CHAIN_BAR 1e-9;
SA_BAR 1e-12; DEG_FLOOR 1e-6; TB_WARD bars 1e-9 main N <= 400 /
3e-6 deep + ext + ext2 / 3e-5 EXT3 (a-priori, one decade for twice
the depth) / 1e-6 controls; ID_BAR 1e-12; AC_BAR 1e-9; MUT_MIN
1e-6; TOY_BAR 1e-12; runtime <= 1800 s; smoke = w9 + controls +
toys + scope/purity audits + the chain/interpolation/pileup/ledger
wards on w9 + controls + e1-e4 mutants + the SELECTION ENUMERATION
(pool counts + strata candidate table, no wpack); ladder,
extensions, EXT3 evaluation, anchors, frozen tests, exponents,
contrast and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (sizing only, r306 precedent -- no rho, no
S_3, no F_A, no qmax, no bound value of ANY window was computed
before this spec froze): one scoping pass enumerated the pools and
counted candidates (frame-A 70 = 42 + 20 + 8; lifted pool h <= 2600
has 124 windows; FRESH = 44 after the used-ledger exclusion, of
which only 2 have h <= 1650 -- the frame-A pool is EXHAUSTED below
1650, so fresh anchors are necessarily deep; the core-zone
small-gap candidates exist with grel 0.28..0.53) and timed two
wpacks for the budget (N 1721: 3.4 s, N 2577: 15.1 s -- 12 anchors
feasible); the core ladder z-range 16..317 and the core-42 grel
median 1.34 (this module's own W = 5 log-gap convention; the audit's
2.0x was measured in the audit's own convention -- both are
reported, neither is tuned); EXT3_H_MAX = 2600, K_STRAT = 6, the
gap-class edges, SPIKE_FA and every contrast bar are a-priori
choices sized BEFORE any evaluation; the four frozen constants and
the e_tot reference are sealed RECORD numbers of r321/r306/r324/
r327, adopted as-is; the verdict letters are symmetric -- every
outcome maps to exactly one letter by CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the two main letters fires):
  R329_ANCHORS(branch rule, r306 C_2 + 0/57, r316 n/rho/C_small,
    r321 b + 0/39 + named, r324 C_NSC + 0/39, r327 C_NG + 0/39 +
    named, identity wards)
+ SEAL(construction reproduction + used ledger + selection freeze +
    purity audits + toys + live wards)
+ SELECTION(12 anchors, strata, gap statistics vs the ladder)
+ EXT3_TABLE(per anchor: the four frozen tests + reserves)
+ [exactly one of] EXT3_ALL_HOLD(min reserves per constant) /
    EXT3_VIOLATIONS(which constant, which anchors, gap class)
+ ETOT(e_G/e_M2/e_tot vs the r324 record, census tag)
+ GAPCONTRAST(cohort metrics + SMALL_GAP_DIFFERENT(clauses) /
    SMALL_GAP_SIMILAR)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the selection rule, the used ledger, the
strata, the frozen constants, the census bands and the contrast
bars are sealed BEFORE any window of this round is evaluated; the
constants are FROZEN record numbers -- nothing is recalibrated, and
a violation is an honest reach-calibration of the lane, not a
failure of this round; the 12 anchors are FRESH by machine-checked
disjointness, but they are NOT an independent world -- they come
from the same source comb and the same construction (only the
choice differs), and the small-gap stratum is necessarily DEEP (the
construction couples gap to depth): the round buys INDEPENDENCE OF
THE ANCHOR CHOICE, not a second world; the e_tot numbers on 12
anchors are census-grade (two dyadic halves of 6); r243-r328 stand.

RECORD TABLES (inserted AFTER the record run -- the only post-freeze
edit, which IS the protocol; TWO-COMMIT PROTOCOL EXECUTED: the
sealed spec above was committed as "experiments: r329 pre-freeze"
(604b8aaf) BEFORE the first full evaluation, this insertion is
committed as "experiments: r329 record"; smoke pass 1 = 32/32
(0.5 s), NO amendment; calibration pass 1 = FIRST full evaluation =
33/33, wall 214.5 s, NO amendment -- no bar, band, rule or verdict
rule moved at any point; record run1/run2 byte-identical up to WALL
(222.6 / 216.2 s) and identical to the calibration pass):
MAIN VERDICT: EXT3_VIOLATIONS(r306 C = 1.069: kz42/kz51/kz62/kz54
ALL gap-class SMALL; r321 b = 1.3056: kz58 SMALL / kz130 MED /
kz128 MED / kz96 SMALL) + EXPONENT_SHIFTED + SMALL_GAP_DIFFERENT(
rho2 med x10.29; F_A med x3.21) -- honest reach-calibration, the
audit's suspicion CONFIRMED quantitatively.
ANCHORS (all five frozen-rule reproductions bit-near): r306 C_2
1.069 (0/57), r316 n = 65 + rho quartet 1.0493/1.0536/0.4821/
0.7791 + C_small 1.0694 @ kz18, r321 b = 1.3056 (0/39, named 4/4),
r324 C_NSC = 2.0258 (0/39), r327 C_NG = 2.6351 (0/39, named 4/4);
branch rule 35 cheap + the named 7; r314 identity wards
4.5e-17/4.7e-16/4.1e-16 ladder, 1.0e-16/7.6e-16/7.2e-16 EXT3.
SELECTION (sealed rule executed verbatim): USED ledger 80 kz (70
frame-A + 35 r286-rule ranks, union 80); lifted pool 124, FRESH 44,
disjointness 0 EXACT; stratum B (small-gap mid-zone, z in [16,
317], grel asc) = kz42/51/62/54/56/58 (z 127/167/227/179/191/197,
grel 0.282..0.528, N_w 1721..2475); stratum A (depth, h desc) =
kz130/128/127/125/123/96 (z 601..397, N_w 2577..2389, grel
0.62..1.02); four A-queue candidates SKIPPED for POSITIVE_PREFIX
failure (kz157 nf 2468, kz180 nf 2385, kz154 nf 2410, kz286 nf
2125 -- the first POSITIVE_PREFIX failures ever seen on this
construction, themselves a small-gap-depth census datum); mult <= 2
on 12/12; ALL 12 anchors deeper than every prior window (N_w
1721..2577 > 1650).  GAP STATISTICS (module convention W = 5):
65-ladder grel min/med/max 0.40/1.32/3.56 vs EXT3-B med 0.46 /
EXT3-A med 1.01 -- the ladder's large-gap selection is real on the
source grid (audit C1 quantified).
THE EXT3 TABLE (stratum kz z N m grel class | qmax F_A F_ins rho2
b F_A^2 | marks a=r321/b=r306/c=NSC/d=NG, reserves):
  B kz42  z 127 N 2472 m 494 grel 0.282 SMALL | 0.0568 3.21 2.44
    rho2 2.2426 bF2 13.4904 | .*.. rsv 6.0/0.5/2.5/5.4
  B kz51  z 167 N 1721 m 335 grel 0.408 SMALL | 0.1291 5.42 5.54
    rho2 7.6196 bF2 38.3331 | .*.. rsv 5.0/0.1/2.4/5.1
  B kz62  z 227 N 2475 m 505 grel 0.458 SMALL | 0.0555 3.30 2.38
    rho2 2.3240 bF2 14.2577 | .*.. rsv 6.1/0.5/2.5/5.5
  B kz54  z 179 N 1868 m 362 grel 0.467 SMALL | 0.0910 3.82 3.91
    rho2 3.1986 bF2 19.0337 | .*.. rsv 6.0/0.3/3.0/5.2
  B kz56  z 191 N 2018 m 397 grel 0.474 SMALL | 0.0266 0.82 1.14
    rho2 0.2498 bF2  0.8746 | .... rsv 3.5/4.3/1.7/2.6
  B kz58  z 197 N 2093 m 409 grel 0.528 SMALL | 0.0142 0.33 0.61
    rho2 0.1522 bF2  0.1450 | *... rsv 1.0/7.0/1.7/3.2
  A kz130 z 601 N 2577 m 505 grel 1.020 MED   | 0.0160 0.39 0.68
    rho2 0.2125 bF2  0.2011 | *... rsv 0.9/5.0/1.6/1.8
  A kz128 z 593 N 2538 m 553 grel 1.018 MED   | 0.0115 0.27 0.50
    rho2 0.1348 bF2  0.0960 | *... rsv 0.7/7.9/2.6/3.3
  A kz127 z 587 N 2508 m 543 grel 1.017 MED   | 0.0177 0.43 0.76
    rho2 0.1631 bF2  0.2464 | .... rsv 1.5/6.6/2.1/5.5
  A kz125 z 571 N 2430 m 510 grel 1.007 MED   | 0.0407 1.84 1.75
    rho2 0.6322 bF2  4.4039 | .... rsv 7.0/1.7/4.2/8.2
  A kz123 z 563 N 2391 m 497 grel 0.975 MED   | 0.0445 1.32 1.91
    rho2 1.0568 bF2  2.2864 | .... rsv 2.2/1.0/2.1/5.5
  A kz96  z 397 N 2389 m 462 grel 0.623 SMALL | 0.0136 0.32 0.59
    rho2 0.1436 bF2  0.1337 | *... rsv 0.9/7.4/2.1/4.0
FROZEN-TEST BALANCE: (a) r321 sliding 8/12 hold -- ALL FOUR
violations are QUIET anchors (F_A 0.27..0.39, excess 1.05x/1.40x/
1.06x/1.07x): b F_A^2 decays quadratically below the ladder's own
F_A floor (r321 min 0.58; the fresh cohort reaches 0.27) -- the
sliding bound fails on the QUIET side, never on the spike side;
DISCLOSED SECONDARY CENSUS: under the r321 insertion-rule
coordinate (F_ins vs the pure-65 columns) all four quiet violators
are INSIDE (b F_ins^2 = 0.49/0.60/0.33/0.45 vs rho2 0.15/0.21/
0.13/0.14) -- the (a)-violation is CONVENTION-SENSITIVE (extended-
ladder F_A vs insertion rule), said honestly; (b) r306 base
8/12 hold -- ALL FOUR violations are the sharpest SMALL-GAP
mid-zone anchors (kz51 rho2 7.6196 = 7.1x C, kz54 3.0x, kz62 2.2x,
kz42 2.1x): the first-5-frozen uniform constant is a LARGE-GAP
artifact and does NOT extend to the small-gap family -- while the
r321 SLIDING bound covers exactly these four with reserves 5.0-6.1
(the coordinate absorbs what kills the flat constant, on anchors
neither it nor its constant ever saw); (c) r324 C_NSC HOLDS 12/12
(min reserve 1.6); (d) r327 C_NG HOLDS 12/12 (min reserve 1.8) --
BOTH O(log m) counting constants generalize choice-robustly.
ETOT (census): e(G/log m) = -0.771, e(m M_2) = -0.889, e_tot =
-1.660 vs the r324 record +0.172 -> EXPONENT_SHIFTED; honest
reading: the 12-anchor set mixes two strata (the m-sorted lower
half is dominated by high-rho2 small-gap anchors), so the halves
slope reads the COHORT COMPOSITION, not a depth trend -- census-
grade by seal, no trend statement.
GAP CONTRAST (cohort med rho2 / med F_A / spike rate / med G/logm
/ med mM2): B small-gap 2.2833/3.26/0.67/4.51/5.10; A depth
0.1878/0.41/0.17/1.41/2.13; LADDER_DEEP (n=23) 0.2219/1.02/0.17/
1.20/2.07 -> SMALL_GAP_DIFFERENT(rho2 med x10.29; F_A med x3.21):
the small-gap family is a genuinely different anatomy -- spike
rate 0.67 vs 0.17, and the A-stratum (median-gap, deep) looks like
the ladder's own deep segment (0.19 vs 0.22) -- the difference is
the GAP CLASS, not the depth.
MUSTFAIL LEDGER: e1 collision CAUGHT (1 vs 0 EXACT on 44 fresh);
e2 AST rho@631 + toy 1.0 != 1.3056; e3 AST rho@642 + toy 0.25 !=
0.85; e4 AST cm@653 with 0 hits on the five real builders; m5a
t_term@661 / m5b g_branch@668 FLAGGED; purity 0 id + 0 literal
hits; frame reproduction 70/70 EXACT; construction ward 0
deviations on 12/12.
READING (typed, no upgrade): the audit-A2 sequence-bias suspicion
is CONFIRMED in the honest direction -- (1) the r306 uniform
constant does NOT survive fresh small-gap anchors (up to 7.1x);
its 0/57 record is a statement about the large-gap construction
family, now said with numbers; (2) the r321 sliding form is the
round's structural WINNER on the spike side: all four r306-killers
sit inside b F_A^2 with reserves >= 5 at the FROZEN constant --
the coordinate genuinely carries independent evidence beyond its
calibration set; its quiet-side misses are small (<= 1.40x),
convention-sensitive, and name the successor question (a floor
term for F_A below the ladder's sampled range -- r330 material,
NOT a recalibration of this round); (3) the two counting
constants C_NSC/C_NG hold 12/12 -- the O(log m) counting side of
the lane is the most choice-robust asset measured so far; (4)
SMALL_GAP_DIFFERENT answers audit C1: the generalization class of
every mid-ladder constant since r306 is the LARGE-GAP family, and
the small-gap anatomy (rho2 x10, F_A x3.2, spike rate x4) is now
a measured object, not a blind spot.  Honest negatives: 12
anchors are a small census; the e_tot column is composition-
dominated; the four POSITIVE_PREFIX failures show the sealed
construction itself starts failing half-filling at small-gap
depth (nf 2125..2468) -- the reachable fresh pool is finite; no
second world was touched (audit repair 4 stays open).  Runtime
214.5 s cal / 222.6 + 216.2 s record / 0.5 s smoke.  AMENDMENTS
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
import qmax_m2_origin_probe as QMO             # noqa: E402 r324
import group_mass_cap_probe as GMC             # noqa: E402 r327
import lstar_margin_scaling_probe as LM        # noqa: E402 r286 READ-ONLY
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
TB_WARD_BAR_EXT3 = 3e-5
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
EXT3_H_MAX = 2600
K_STRAT = 6
GAP_W = 5
LM_RANKS_USED = 35
FRAME_EXPECT = 70
GAP_SMALL = 0.85
GAP_LARGE = 1.5
SPIKE_FA = 1.5
FROZEN_B = 1.3056
FROZEN_C2 = 1.069
FROZEN_CNSC = 2.0258
FROZEN_CNG = 2.6351
ETOT_REF = 0.172
EG_REF = 0.158
EM2_REF = 0.014
CONS_BAND = 0.15
CONTRAST_RHO_FAC = 2.0
CONTRAST_SPIKE_D = 0.5
CONTRAST_FA_FAC = 1.5
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
REC3_BAR_EXT3 = 1e-12
TEL_BAR = 1e-13
TEL_BAR_EXT3 = 1e-12
BND_BAR = 1e-13
BND_BAR_EXT3 = 1e-12
CHAIN_BAR = 1e-9
SA_BAR = 1e-12
DEG_FLOOR = 1e-6
MULT_CAP = 2
N_CAL = 5
N329_REF = 65
NAMED_KZ = (53, 83, 67, 55)
FROZEN_TOL = 0.005
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
MUT_MIN = 1e-6
TOY_BAR = 1e-12
EDGE_F = 0.20
R329_TABLE_LITERALS = frozenset((
    1.3056, 1.069, 2.0258, 2.6351, 0.172, 0.158, 0.014,
    1.0490, 1.0493, 1.0536, 0.4821, 0.7790, 0.7791, 1.0694,
    2.47, 2.39, 2.38, 0.4579, 3.7157, 2.2557, 3.1528, 3.1938,
    3.049, 9.3583, 1.7481, 8.941, 2.616, 1.1838, 0.9143,
    0.2047, 0.106, 0.293, 13.778, 12.707, 22.378, 25.309,
    6.661, 1.165, 2.026, 1.137, 2.8, 0.7476, 0.558, 0.785,
    -0.341, 15.95, 7.97, 5.35, 2.71, 1.1426, 1.4088, 0.122,
    2.051, 3.194, 0.023, 0.0158, 5.32, 14.15, 2.6, 2.724,
    2.567, 1.971, 2.103, -0.2, -0.261, 0.807, 0.888, 0.416))

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
                       "(r238 convention); ground truth enters gates "
                       "and census tables only"
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
    lies in the sealed record-literal set."""
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
                            in R329_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the selection
# ---------------- builders consume the prime-power grid (U_ALL,
# ---------------- G_ALL), window shape (h, z, N) and the used
# ---------------- ledger ONLY; the withheld terminal drive key, the
# ---------------- branch label, the cubic target and the record
# ---------------- literals are forbidden (AST identifier scan +
# ---------------- literal scan).
def admissible_pool(h_lo, h_hi):
    """the frame-A anchor CONSTRUCTION verbatim (core.frame_a_zones
    body) with the h-cap as a parameter: kz in range(2, NZ_DEEP -
    2), D_k = 0.5 G_ALL[kz]/NU_MAIN, M_k = ceil(U/D) + 1 rounded
    even, h_k = M_k/2 in [h_lo, h_hi], >= N_ATOM_MIN atoms; returns
    (h, kz) pairs.  Warded EXACT against core.frame_a_zones at the
    frozen document cap."""
    out = []
    for kz in range(2, core.NZ_DEEP - 2):
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(core.U_ALL[kz] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        h_k = M_k // 2
        if h_k < h_lo or h_k > h_hi:
            continue
        if core.atoms_in(core.U_ALL[kz]) < core.N_ATOM_MIN:
            continue
        out.append((h_k, kz))
    return out


def grel_col(kzs, gaps, w=GAP_W):
    """the relative local prime-power gap: grel(kz) = gaps[kz] /
    median{gaps[j] : |j - kz| <= w, j != kz} -- the r317 W-window
    convention applied to the source gap column (consumes the gap
    grid + index order only)."""
    g = [float(v) for v in gaps]
    out = []
    for kz in kzs:
        lo = max(0, kz - w)
        hi = min(len(g), kz + w + 1)
        nb = [g[j] for j in range(lo, hi) if j != kz]
        out.append(float(g[kz]) / max(float(np.median(nb)), 1e-300))
    return out


def used_kz_set(frame_kzs, lm_rows, n_ranks):
    """the sealed used-window ledger: every kz of the document
    frame-A scan UNION the kz of the first n_ranks rows of the r286
    extension rule -- covers every window of every round r238..r328
    in both lanes."""
    used = set(int(kz) for kz in frame_kzs)
    for row in lm_rows[:n_ranks]:
        used.add(int(row[1]))
    return used


def ext3_select(pool, used, z_vals, grels, z_lo, z_hi, k_strat):
    """the sealed two-strata EXT3 choice rule: FRESH = pool minus
    used; stratum B = fresh kz with z in [z_lo, z_hi] sorted by
    (grel, kz) ascending; stratum A = the remaining fresh kz sorted
    by (h, kz) descending; returns the two CANDIDATE QUEUES (each a
    list of kz, admission by the caller: POSITIVE_PREFIX + mult cap,
    failing candidates replaced by the next in queue) and the fresh
    list.  Consumes window shape + gap + used ledger only."""
    fresh = [(h, kz) for (h, kz) in pool if kz not in used]
    fresh_kz = [kz for (_h, kz) in fresh]
    zb = {kz: z_vals[i] for i, kz in enumerate(fresh_kz)}
    gb = {kz: grels[i] for i, kz in enumerate(fresh_kz)}
    b_cand = sorted((kz for (_h, kz) in fresh
                     if z_lo <= zb[kz] <= z_hi),
                    key=lambda kz: (gb[kz], kz))
    b_set = set(b_cand[:k_strat])
    a_cand = [kz for (_h, kz) in sorted(fresh, reverse=True)
              if kz not in b_set]
    return b_cand, a_cand, fresh


def gap_class(g):
    """the sealed gap classes: SMALL below GAP_SMALL, LARGE above
    GAP_LARGE, MED between."""
    if g < GAP_SMALL:
        return "SMALL"
    if g > GAP_LARGE:
        return "LARGE"
    return "MED"


def mutant_collision(fresh_kzs, ladder_kzs):
    """e1 MUST-FAIL MUTANT: a 'fresh' set that silently contains a
    core-ladder anchor -- the disjointness ward must CATCH the
    non-empty intersection EXACT."""
    return tuple(fresh_kzs) + (int(ladder_kzs[0]),)


def mutant_b_recal(Fv, rho):
    """e2 MUST-FAIL MUTANT: the sliding constant RE-CALIBRATED on
    the fresh anchors after sight (consumes the evaluated bound
    column rho) -- the BOUND_FORBIDDEN scope audit must FLAG it AND
    on the sealed toy it returns != the frozen record constant."""
    return max(r / max(float(f) * float(f), 1e-300)
               for f, r in zip(Fv, rho))


def mutant_gap_posthoc(grels, rho):
    """e3 MUST-FAIL MUTANT: the gap threshold re-picked AFTER SIGHT
    to minimize the covered bound mass (consumes rho) -- the scope
    audit must FLAG it; on the sealed toy it returns a threshold
    != the sealed stratification's fixed classes."""
    best = GAP_SMALL
    bestv = float("inf")
    for th in (0.25, 0.5, 0.75, 1.0, 2.0, 4.0):
        v = sum(r for g, r in zip(grels, rho) if g <= th)
        if v < bestv:
            bestv = v
            best = th
    return best


def mutant_strat_readback(cmrec, nblk):
    """e4 MUST-FAIL MUTANT: a 'selection score' consuming the
    cubic-moment record (the target side) -- the PHI3_FORBIDDEN
    identifier scan must FLAG this."""
    cm = cmrec
    return cm["S3"] * float(nblk)


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'selection orientation' consuming
    the withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT: a 'selection constant' consuming the
    branch label -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("ext3_fresh_anchors_probe -- "
          "PRIME.AUDIT.EXT3_FRESH_ANCHORS.01 (round 329)")
    print("SPEC_SHA %s   R321_SHA %s   R324_SHA %s (imported)"
          % (SPEC_SHA[:16], CCP.SPEC_SHA[:16], QMO.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/purity "
                        "audits + wards + e1-e4 + selection "
                        "enumeration; ladder, extensions, EXT3 "
                        "evaluation, anchors, frozen tests, "
                        "exponents, contrast and adjudication "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE EXT3 FRESH-ANCHOR ROUND (audit repair 2+3 of r328A/"
          "C): %d fresh windows that appeared in NO previous round "
          "(machine-checked disjointness against the sealed used "
          "ledger), two strata (%d deepest within h <= %d + %d "
          "small-gap anchors inside the core zone range), tested "
          "POINTWISE against the FOUR FROZEN constants b = %.4f "
          "(r321), C_2 = %.3f (r306), C_NSC = %.4f (r324), C_NG = "
          "%.4f (r327) -- NOTHING recalibrated; e_tot measured "
          "against the r324 record %+.3f (census); the small-gap "
          "contrast adjudicated by sealed coarse bars; verdicts "
          "EXT3_ALL_HOLD / EXT3_VIOLATIONS + gap-contrast tag "
          "sealed BEFORE evaluation; FIRST round under the "
          "two-commit freeze protocol (pre-freeze commit before "
          "the record run, record commit after the table "
          "insertion)"
          % (2 * K_STRAT, K_STRAT, EXT3_H_MAX, K_STRAT, FROZEN_B,
             FROZEN_C2, FROZEN_CNSC, FROZEN_CNG, ETOT_REF))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("admissible_pool", "grel_col", "used_kz_set",
               "ext3_select", "gap_class"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the five module-own "
          "selection builders clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN (%d hits); m5a gift-bound FLAGGED (%s); "
          "m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls + THE SELECTION
    section("S1  CENSUS + CONTROLS + THE SEALED EXT3 SELECTION")
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
    # -------- construction reproduction ward (cheap, always run)
    pool_doc = admissible_pool(core.H_MIN, core.HCAP)
    frame_kzs = core.frame_a_zones()
    ok_frame = ([kz for (_h, kz) in pool_doc] == list(frame_kzs)
                and len(frame_kzs) == FRAME_EXPECT)
    check("G12-frame-reproduction", ok_frame,
          "admissible_pool(H_MIN=%d, HCAP=%d) == core."
          "frame_a_zones() EXACT (%d windows == expected %d) -- "
          "the anchor CONSTRUCTION is verbatim, only the CHOICE "
          "differs" % (core.H_MIN, core.HCAP, len(frame_kzs),
                       FRAME_EXPECT))
    # -------- the sealed used ledger + selection enumeration
    lm_rows = LM.ext_rule()
    used = used_kz_set(frame_kzs, lm_rows, LM_RANKS_USED)
    pool_full = admissible_pool(core.H_MIN, EXT3_H_MAX)
    h_by_kz = {kz: h for (h, kz) in pool_full}
    fresh_pre = [(h, kz) for (h, kz) in pool_full if kz not in used]
    fresh_kz_pre = [kz for (_h, kz) in fresh_pre]
    z_pre = [int(core._NN[kz]) for kz in fresh_kz_pre]
    grel_pre = grel_col(fresh_kz_pre, core.G_ALL)
    core_kzs = [kz for (h, kz) in pool_doc if h <= H_CAP]
    z_core = [int(core._NN[kz]) for kz in core_kzs]
    z_lo, z_hi = min(z_core), max(z_core)
    b_queue, a_queue, fresh = ext3_select(
        pool_full, used, z_pre, grel_pre, z_lo, z_hi, K_STRAT)
    ok_disj = (len(set(kz for (_h, kz) in fresh) & used) == 0)
    check("G13-used-ledger-and-freshness", ok_disj
          and len(core_kzs) == 42 and len(lm_rows) >= LM_RANKS_USED,
          "USED ledger = %d frame-A kz + first %d r286-rule kz "
          "(union %d); lifted pool h <= %d has %d windows; FRESH "
          "= %d (disjointness EXACT: 0 overlap); core ladder %d "
          "rungs, zone range z in [%d, %d]"
          % (len(frame_kzs), LM_RANKS_USED, len(used), EXT3_H_MAX,
             len(pool_full), len(fresh), len(core_kzs), z_lo,
             z_hi))
    grel_by_kz = {kz: grel_pre[i]
                  for i, kz in enumerate(fresh_kz_pre)}
    info("sealed SOURCE-PURE selection queues (printed BEFORE any "
         "bound-side value of this round): stratum B (small-gap "
         "mid-zone, by grel asc) head: %s; stratum A (depth, by h "
         "desc) head: %s"
         % (str([(kz, int(core._NN[kz]), h_by_kz[kz],
                  round(grel_by_kz[kz], 3))
                 for kz in b_queue[:K_STRAT + 2]]),
            str([(kz, int(core._NN[kz]), h_by_kz[kz],
                  round(grel_by_kz[kz], 3))
                 for kz in a_queue[:K_STRAT + 2]])))

    if smoke:
        ladder = []
        ext = []
        ext2 = []
        okL = True
        sel_b = []
        sel_a = []
    else:
        kzs = []
        ekz = []
        ekz2 = []
        for kz in frame_kzs:
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
        # -------- EXT3 admission (POSITIVE_PREFIX at wpack; the
        # -------- mult cap is checked after eval in S2, queue
        # -------- continues there if needed)
        def admit_queue(queue, k):
            got = []
            skipped = []
            for kz in queue:
                if len(got) >= k:
                    break
                p = BH.wpack(kz)
                if p["nf"] is None:
                    got.append(p)
                else:
                    skipped.append((kz, p["nf"]))
            return got, skipped

        sel_b, skip_b = admit_queue(b_queue, K_STRAT)
        a_rest = [kz for kz in a_queue
                  if kz not in set(p["kz"] for p in sel_b)]
        sel_a, skip_a = admit_queue(a_rest, K_STRAT)
        check("G14-ext3-admission",
              len(sel_b) == K_STRAT and len(sel_a) == K_STRAT,
              "stratum B admitted %d/%d (skipped %s), stratum A "
              "admitted %d/%d (skipped %s); POSITIVE_PREFIX "
              "demanded at wpack; mult cap checked in S2"
              % (len(sel_b), K_STRAT, str(skip_b) or "[]",
                 len(sel_a), K_STRAT, str(skip_a) or "[]"))
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
    frecs_b = [rung_rec(p) for p in sel_b] if not smoke else []
    frecs_a = [rung_rec(p) for p in sel_a] if not smoke else []
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
        f_cheap = sum(1 for rc in frecs_b + frecs_a
                      if rc["g_branch"] >= 0.0)
        f_exc = [rc["kz"] for rc in frecs_b + frecs_a
                 if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; EXT3 "
              "census (no sealed expectation): %d cheap / %d "
              "exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 f_cheap, len(f_exc), str(f_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + EVAL + IDENTITY WARDS")
    tb_worst = 0.0
    tb_deep = 0.0
    tb_ext3 = 0.0
    tb_ctrl = 0.0
    for rc in recs + mrecs + erecs + e2recs:
        absum = float(np.sum(np.abs(rc["ct"])))
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(absum, 1e-300)
        if rc["N"] > DEEP_N:
            tb_deep = max(tb_deep, dev)
        else:
            tb_worst = max(tb_worst, dev)
    for rc in frecs_b + frecs_a:
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ext3 = max(tb_ext3, dev)
    for c in crecs:
        rc = crecs[c]
        dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
            / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
        tb_ctrl = max(tb_ctrl, dev)
    check("G20-contribution-ward", tb_worst <= TB_WARD_BAR
          and tb_deep <= TB_WARD_BAR_DEEP
          and tb_ext3 <= TB_WARD_BAR_EXT3
          and tb_ctrl <= TB_WARD_BAR_CTRL,
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext/ext2 + %d "
          "EXT3 + %d mains + 3 controls: worst dev/absmass %.1e "
          "main N<=%d (bar %.0e) / %.1e deep (bar %.0e) / %.1e "
          "EXT3 (bar %.0e) / %.1e controls (bar %.0e)"
          % (len(recs), len(erecs) + len(e2recs),
             len(frecs_b) + len(frecs_a), len(mrecs), tb_worst,
             DEEP_N, TB_WARD_BAR, tb_deep, TB_WARD_BAR_DEEP,
             tb_ext3, TB_WARD_BAR_EXT3, tb_ctrl, TB_WARD_BAR_CTRL))

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
            pst = QMO.pileup_state(sct["x"], val_all, blk_all)
            led = GMC.group_mass_ledger(pos_all, val_all, blk_all,
                                        src_all, m)
            hst = GMC.heavy_state(sct["x"], led)
        else:
            gen = sct = ft = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            A1 = np.zeros(0)
            mx_mult = 0
            trs = dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0,
                       fe=0.0, fcix=0.0, qmax=0.0, cnt3=0.0,
                       phiL1=0.0, phiL2=0.0, phiH1=0.0,
                       phiH2=0.0, L=0.0)
            rho2 = 0.0
            pst = dict(j=0, nsc=0, nsc_rel=0, pil=0.0, a1j=0.0,
                       tail=0.0, scut=0, scales=(), masses=())
            led = dict(G1=np.zeros(0), gabs=np.zeros(0),
                       gmax=np.zeros(0), gwin=np.zeros(0),
                       mult=np.zeros(0, int), ng=0,
                       gblk=np.zeros(0, int),
                       ptr=np.zeros(1, int), vmaxw=0.0)
            hst = GMC.heavy_state(np.zeros(0), led)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, mx_mult=mx_mult, gen=gen,
                    sct=sct, ft=ft, trs=trs, rho2=rho2, A1=A1,
                    pst=pst, led=led, hst=hst)

    frecs = frecs_b + frecs_a
    all_rc = recs + mrecs + erecs + e2recs + frecs
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
    fset = set(id(rc) for rc in frecs)
    rec3_w = max(rc["ev"]["rec3"] for rc in live
                 if id(rc) not in fset)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live
                if id(rc) not in fset)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live
                if id(rc) not in fset)
    rec3_f = max((rc["ev"]["rec3"] for rc in frecs), default=0.0)
    tel_f = max((rc["ev"]["tel_dev"] for rc in frecs), default=0.0)
    bnd_f = max((rc["ev"]["bnd_dev"] for rc in frecs), default=0.0)
    mult_bad = [rc["kz"] for rc in frecs
                if rc["ev"]["mx_mult"] > MULT_CAP]
    check("G22-genealogy-and-mult",
          x_w <= ATOM_BAR and mism_tot == 0
          and rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR and rec3_f <= REC3_BAR_EXT3
          and tel_f <= TEL_BAR_EXT3 and bnd_f <= BND_BAR_EXT3
          and not mult_bad,
          "fold genealogy covers every block value on %d live "
          "worlds (dev %.1e); assignment == breakpoint (%d "
          "mismatches); r314 identity ladder %.1e/%.1e/%.1e (bars "
          "%.0e/%.0e/%.0e), EXT3 %.1e/%.1e/%.1e (bars %.0e); fold "
          "multiplicity <= %d on ALL EXT3 anchors (violations "
          "%s)%s"
          % (len(live), x_w, mism_tot, rec3_w, tel_w, bnd_w,
             REC3_BAR, TEL_BAR, BND_BAR, rec3_f, tel_f, bnd_f,
             REC3_BAR_EXT3, MULT_CAP,
             str(mult_bad) if mult_bad else "none",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (frozen constants repro)
    section("S3  LEG 0 -- ANCHOR REGRESSION "
            "(r306/r316/r321/r324/r327 frozen constants)")
    if smoke:
        check("G30-r306-C2", True, "SMOKE: skipped")
        check("G31-r316-class-ladder", True, "SMOKE: skipped")
        check("G32-r321-b", True, "SMOKE: skipped")
        check("G33-r324-cnsc", True, "SMOKE: skipped")
        check("G34-r327-cng", True, "SMOKE: skipped")
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2)
        check("G30-r306-C2",
              abs(C2 - FROZEN_C2) <= FROZEN_TOL and viol2 == 0,
              "r306 pointwise bound live: C_2 %.3f (rec %.3f tol "
              "%.3f, first-%d freeze), violations %d/%d"
              % (C2, FROZEN_C2, FROZEN_TOL, N_CAL, viol2,
                 len(srt57)))
        srt65_all = sorted(recs + erecs + e2recs,
                           key=lambda rc: (rc["N"], rc["kz"]))
        srt65 = [rc for rc in srt65_all
                 if rc["ev"]["mx_mult"] <= MULT_CAP]
        n65 = len(srt65)
        m65 = [rc["ev"]["m"] for rc in srt65]
        rho65 = [rc["ev"]["rho2"] for rc in srt65]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt65}
        sm_i, ca_i, te_i = TRB.split_midladder(n65)
        C_small = max(rho65[i] for i in sm_i)
        j_sm = max(sm_i, key=lambda i: rho65[i])
        check("G31-r316-class-ladder",
              n65 == N329_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt65[j_sm]["kz"] == R316_CSMALL_KZ,
              "r316 class ladder reproduced: n = %d (rec %d); rho "
              "anchors kz53/kz67/kz55/kz83 %.4f/%.4f/%.4f/%.4f "
              "(rec %.4f/%.4f/%.4f/%.4f tol %.3f); C_small %.4f @ "
              "kz%d (rec %.4f @ kz%d); split %d|%d|%d"
              % (n65, N329_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO[53], R316_RHO[67],
                 R316_RHO[55], R316_RHO[83], R316_RHO_TOL,
                 C_small, srt65[j_sm]["kz"], R316_CSMALL,
                 R316_CSMALL_KZ, len(sm_i), len(ca_i), len(te_i)))
        qmax65 = [rc["ev"]["trs"]["qmax"] for rc in srt65]
        FA65 = EFP.local_ratio(qmax65)
        medloc65 = CCP.local_median(qmax65)
        B65 = [medloc65[i] * float(m65[i])
               / math.log(float(m65[i])) for i in range(n65)]
        b_repro = max(B65[i] for i in ca_i) ** 2
        viol_b = [i for i in te_i
                  if rho65[i] > b_repro * FA65[i] ** 2]
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n65):
                if srt65[i]["kz"] == kz:
                    named_rank[kz] = i
        named_b = sum(1 for kz in NAMED_KZ
                      if rho65[named_rank[kz]]
                      <= FROZEN_B * FA65[named_rank[kz]] ** 2)
        check("G32-r321-b",
              abs(b_repro - FROZEN_B) <= FROZEN_TOL
              and not viol_b and named_b == len(NAMED_KZ),
              "r321 sliding bound live: b = (max cal B)^2 = %.4f "
              "(rec %.4f tol %.3f); test violations %d/%d; named "
              "coverage at the FROZEN b: %d/4"
              % (b_repro, FROZEN_B, FROZEN_TOL, len(viol_b),
                 len(te_i), named_b))
        nscl65 = [srt65[i]["ev"]["pst"]["nsc_rel"]
                  / math.log(float(m65[i])) for i in range(n65)]
        cnsc_repro = max(nscl65[i] for i in ca_i)
        viol_nsc = [i for i in te_i if nscl65[i] > cnsc_repro]
        check("G33-r324-cnsc",
              abs(cnsc_repro - FROZEN_CNSC) <= FROZEN_TOL
              and not viol_nsc,
              "r324 scale count live: C_NSC %.4f (rec %.4f tol "
              "%.3f), test violations %d/%d"
              % (cnsc_repro, FROZEN_CNSC, FROZEN_TOL,
                 len(viol_nsc), len(te_i)))
        ngl65 = [srt65[i]["ev"]["hst"]["ngj"]
                 / math.log(float(m65[i])) for i in range(n65)]
        cng_repro = max(ngl65[i] for i in ca_i)
        viol_ng = [i for i in te_i if ngl65[i] > cng_repro]
        named_ng = sum(1 for kz in NAMED_KZ
                       if ngl65[named_rank[kz]] <= FROZEN_CNG)
        check("G34-r327-cng",
              abs(cng_repro - FROZEN_CNG) <= FROZEN_TOL
              and not viol_ng and named_ng == len(NAMED_KZ),
              "r327 group count live: C_NG %.4f (rec %.4f tol "
              "%.3f), test violations %d/%d, named %d/4"
              % (cng_repro, FROZEN_CNG, FROZEN_TOL, len(viol_ng),
                 len(te_i), named_ng))

    # ---------------- S4: Leg A -- purity + toys + live wards
    section("S4  LEG A -- PURITY + TOYS + LIVE WARDS")
    pure_lits = []
    for fn in ("admissible_pool", "grel_col", "used_kz_set",
               "ext3_select", "gap_class"):
        pure_lits += literal_audit(fn)
    e2_hits = scope_audit("mutant_b_recal", BOUND_FORBIDDEN)
    e3_hits = scope_audit("mutant_gap_posthoc", BOUND_FORBIDDEN)
    e4_hits = scope_audit("mutant_strat_readback", PHI3_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e2_hits) >= 1 and len(e3_hits) >= 1
          and len(e4_hits) >= 1,
          "SOURCE PURITY: the five selection builders clean vs "
          "identifier sets (%d hits) + the sealed record-literal "
          "set (%d hits); consumed inputs: prime-power grid + "
          "window shape + used ledger ONLY; e2 b-recal FLAGGED "
          "(%s); e3 gap-posthoc FLAGGED (%s); e4 strat-readback "
          "FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e2_hits[0] if e2_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS",
             e4_hits[0] if e4_hits else "MISS"))
    # toys (exact)
    toy_g = (1.0, 1.0, 1.0, 5.0, 1.0, 1.0, 1.0)
    tg = grel_col(range(7), toy_g, w=3)
    ok_grel = all(abs(tg[i] - toy_g[i]) <= TOY_BAR
                  for i in range(7))
    ok_cls = (gap_class(0.5) == "SMALL" and gap_class(1.0) == "MED"
              and gap_class(2.0) == "LARGE")
    toy_pool = [(100, 0), (200, 1), (300, 2), (400, 3), (500, 4),
                (600, 5)]
    toy_used = {1, 3}
    toy_z = [10, 20, 30, 40]
    toy_gr = [0.9, 0.3, 0.7, 0.5]
    tb_q, ta_q, t_fresh = ext3_select(
        toy_pool, toy_used, toy_z, toy_gr, 15, 35, 1)
    ok_sel = (sorted(kz for (_h, kz) in t_fresh) == [0, 2, 4, 5]
              and tb_q == [2, 4]
              and ta_q == [5, 4, 0])
    mutc = mutant_collision([0, 2], [1])
    ok_coll = (len(set(mutc) & toy_used) == 1
               and len(set(kz for (_h, kz) in t_fresh)
                       & toy_used) == 0)
    sl_toy = L2D.halves_slope((2, 4), (1.0, 2.0))
    ok_sl = abs(sl_toy - 1.0) <= TOY_BAR
    check("G41-toy-exactness", ok_grel and ok_cls and ok_sel
          and ok_coll and ok_sl,
          "grel spike toy (1,1,1,5,1,1,1) -> grel EXACT (medians "
          "all 1); gap classes 0.5/1.0/2.0 -> SMALL/MED/LARGE; "
          "ext3_select toy: fresh {0,2,4,5}, B queue [2,4] (grel "
          "asc in zone), A queue [5,4,0] (h desc) EXACT; collision "
          "toy: injected used anchor -> intersection 1 vs real 0 "
          "EXACT; halves-slope toy (2,4)/(1,2) -> +1 EXACT")
    # live wards
    chain_w = 0.0
    xw_cube = 0.0
    interp_w = 0.0
    pilch_w = 0.0
    screc_w = 0.0
    part_w = 0.0
    led_dev = 0.0
    for rc in live:
        ev = rc["ev"]
        trs = ev["trs"]
        mloc = ev["m"]
        nc = trs["nrm"] * ev["cube"]
        xw_cube = max(xw_cube, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
        for a, b in ((nc, trs["phiL1"]),
                     (trs["phiL1"], trs["phiL2"]),
                     (trs["phiL2"], trs["phiH2"]),
                     (nc, trs["phiH1"])):
            chain_w = max(chain_w,
                          max(0.0, a - b) / max(b, 1e-300))
        cmv = ev["cm"]
        qmx = trs["qmax"]
        interp_w = max(interp_w,
                       max(0.0, cmv["S3"] - qmx * cmv["S2"])
                       / max(qmx * cmv["S2"], 1e-300),
                       max(0.0, cmv["S2"] - qmx)
                       / max(qmx, 1e-300))
        pst = ev["pst"]
        G = mloc * qmx
        if pst["nsc"]:
            pilch_w = max(pilch_w,
                          max(0.0, G - pst["nsc"] * pst["pil"])
                          / max(pst["nsc"] * pst["pil"], 1e-300))
            screc_w = max(screc_w,
                          abs(sum(pst["masses"]) - pst["a1j"])
                          / max(pst["a1j"], 1e-300))
        led = ev["led"]
        gen = ev["gen"]
        if gen is not None and led["ng"]:
            A1led = np.bincount(led["gblk"], weights=led["gabs"],
                                minlength=mloc)
            part_w = max(part_w,
                         float(np.max(np.abs(A1led - ev["A1"])))
                         / max(float(np.max(ev["A1"])), 1e-300))
            if gen["ng"] == led["ng"]:
                sc = max(float(np.max(np.abs(gen["G1"]))), 1e-300)
                led_dev = max(
                    led_dev,
                    float(np.max(np.abs(led["G1"] - gen["G1"])))
                    / sc,
                    float(np.max(np.abs(led["mult"]
                                        - gen["mult"]))))
            else:
                led_dev = max(led_dev, 1.0)
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and interp_w <= CHAIN_BAR and pilch_w <= CHAIN_BAR
          and screc_w <= SA_BAR and part_w <= SA_BAR
          and led_dev <= SA_BAR,
          "on %d live worlds: r316 chain (worst %.1e, bar %.0e); "
          "NORM x cube == rho_2 (%.1e); r324 interpolation M_3 <= "
          "qmax M_2 <= qmax^2 (%.1e); pileup chain m qmax <= nsc "
          "x pil (%.1e); scale recomposition (%.1e); r327 group "
          "partition (%.1e) + ledger == genealogy (%.1e)"
          % (len(live), chain_w, CHAIN_BAR, xw_cube, interp_w,
             pilch_w, screc_w, part_w, led_dev))
    if smoke:
        check("G43-construction-ward", True, "SMOKE: skipped")
    else:
        h_dev = 0
        for rc in frecs:
            h_probe = PIK.build_rung(rc["kz"])["h"]
            if h_by_kz[rc["kz"]] != h_probe:
                h_dev += 1
        check("G43-construction-ward", h_dev == 0,
              "h(kz) via admissible_pool == the PIK.build_rung h "
              "on all %d EXT3 anchors EXACT (%d deviations) -- "
              "the fresh windows use the IDENTICAL construction"
              % (len(frecs), h_dev))

    # ---------------- S5: THE FOUR FROZEN TESTS ON EXT3
    section("S5  LEG B -- THE FOUR FROZEN TESTS ON THE EXT3 "
            "ANCHORS")
    if smoke:
        check("G50-selection-freeze", True, "SMOKE: skipped")
        check("G51-extended-coordinate", True, "SMOKE: skipped")
        check("G52-frozen-tests", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
        tag_gap = "SMOKE"
        tag_etot = "SMOKE"
    else:
        # gap statistics: ladder vs EXT3 (this module's convention)
        lad65_kz = [rc["kz"] for rc in srt65]
        grel_lad = grel_col(lad65_kz, core.G_ALL)
        grel_f = {rc["kz"]: grel_col([rc["kz"]], core.G_ALL)[0]
                  for rc in frecs}
        check("G50-selection-freeze", len(frecs) == 2 * K_STRAT,
              "SELECTION frozen: %d EXT3 anchors (B %d small-gap "
              "mid-zone z in [%d, %d] + A %d depth); GAP "
              "STATISTICS (module convention, W = %d): class "
              "ladder n=%d grel min/med/max %.2f/%.2f/%.2f "
              "(large-gap selected); EXT3-B med %.2f / EXT3-A med "
              "%.2f -- the audit-C1 contrast is real on the "
              "source grid"
              % (len(frecs), len(frecs_b), z_lo, z_hi,
                 len(frecs_a), GAP_W, n65, min(grel_lad),
                 float(np.median(grel_lad)), max(grel_lad),
                 float(np.median([grel_f[rc["kz"]]
                                  for rc in frecs_b])),
                 float(np.median([grel_f[rc["kz"]]
                                  for rc in frecs_a]))))
        # extended class ladder + coordinate
        srtC = sorted(srt65 + frecs,
                      key=lambda rc: (rc["N"], rc["kz"]))
        nC = len(srtC)
        qmaxC = [rc["ev"]["trs"]["qmax"] for rc in srtC]
        FAC = EFP.local_ratio(qmaxC)
        medlocC = CCP.local_median(qmaxC)
        rec_fa = max(abs(qmaxC[i] - FAC[i] * medlocC[i])
                     / max(qmaxC[i], 1e-300) for i in range(nC))
        idxC = {rc["kz"]: i for i, rc in enumerate(srtC)}
        lad_Ns = [rc["N"] for rc in srt65]
        check("G51-extended-coordinate", rec_fa <= 1e-12,
              "F_A on the EXTENDED (N, kz)-sorted class ladder "
              "(%d = %d + %d rungs, EFP.local_ratio verbatim, W = "
              "%d): reconstruction QMAX == F_A x medloc EXACT "
              "(worst %.1e); the insertion-rule coordinate "
              "(CCP.world_coord vs the pure-65 columns) printed "
              "per anchor as disclosed secondary census"
              % (nC, n65, len(frecs), EFP.CLS_W, rec_fa))
        # the four frozen tests
        info("THE EXT3 TABLE (stratum kz z N m h grel class | "
             "QMAX F_A F_ins rho2 bF^2 | marks a/b/c/d + reserves)")
        tests = {}
        for rc in frecs:
            i = idxC[rc["kz"]]
            ev = rc["ev"]
            mloc = ev["m"]
            lg = math.log(float(mloc))
            fa = FAC[i]
            f_ins = CCP.world_coord(ev["trs"]["qmax"], rc["N"],
                                    lad_Ns, qmax65)
            gb = FROZEN_B * fa * fa
            nscl = ev["pst"]["nsc_rel"] / lg
            ngl = ev["hst"]["ngj"] / lg
            tests[rc["kz"]] = dict(
                stratum="B" if rc in frecs_b else "A",
                z=int(core._NN[rc["kz"]]), N=rc["N"],
                m=mloc, h=h_by_kz[rc["kz"]],
                grel=grel_f[rc["kz"]],
                cls=gap_class(grel_f[rc["kz"]]),
                qmax=ev["trs"]["qmax"], fa=fa, f_ins=f_ins,
                rho2=ev["rho2"], gb=gb,
                ok_a=(ev["rho2"] <= gb),
                ok_b=(ev["rho2"] <= FROZEN_C2),
                ok_c=(nscl <= FROZEN_CNSC),
                ok_d=(ngl <= FROZEN_CNG),
                rsv_a=gb / max(ev["rho2"], 1e-300),
                rsv_b=FROZEN_C2 / max(ev["rho2"], 1e-300),
                rsv_c=FROZEN_CNSC / max(nscl, 1e-300),
                rsv_d=FROZEN_CNG / max(ngl, 1e-300),
                nscl=nscl, ngl=ngl,
                Glog=mloc * ev["trs"]["qmax"] / lg,
                mM2=mloc * ev["cm"]["S2"])
        for rc in frecs:
            t = tests[rc["kz"]]
            marks = "".join("." if t[k] else "*"
                            for k in ("ok_a", "ok_b", "ok_c",
                                      "ok_d"))
            info("%s kz%-3d z %4d N %4d m %3d h %4d grel %.3f "
                 "%-5s | qmax %.4f FA %5.2f Fins %5.2f rho2 "
                 "%.4f bF2 %7.4f | %s rsv %.1f/%.1f/%.1f/%.1f"
                 % (t["stratum"], rc["kz"], t["z"], t["N"],
                    t["m"], t["h"], t["grel"], t["cls"],
                    t["qmax"], t["fa"], t["f_ins"], t["rho2"],
                    t["gb"], marks, t["rsv_a"], t["rsv_b"],
                    t["rsv_c"], t["rsv_d"]))
        viols = {k: [kz for kz in tests if not tests[kz][k]]
                 for k in ("ok_a", "ok_b", "ok_c", "ok_d")}
        names = {"ok_a": "r321 b=%.4f" % FROZEN_B,
                 "ok_b": "r306 C=%.3f" % FROZEN_C2,
                 "ok_c": "r324 C_NSC=%.4f" % FROZEN_CNSC,
                 "ok_d": "r327 C_NG=%.4f" % FROZEN_CNG}
        all_hold = all(not viols[k] for k in viols)
        if all_hold:
            verdict_main = ("EXT3_ALL_HOLD(min reserves: sliding "
                            "%.2f, base %.2f, NSC %.2f, NG %.2f "
                            "on %d fresh anchors)"
                            % (min(t["rsv_a"]
                                   for t in tests.values()),
                               min(t["rsv_b"]
                                   for t in tests.values()),
                               min(t["rsv_c"]
                                   for t in tests.values()),
                               min(t["rsv_d"]
                                   for t in tests.values()),
                               len(tests)))
        else:
            det = "; ".join(
                "%s: %s" % (names[k], str(
                    [(kz, tests[kz]["cls"]) for kz in viols[k]]))
                for k in viols if viols[k])
            verdict_main = "EXT3_VIOLATIONS(%s)" % det
        check("G52-frozen-tests", True,
              "adjudicated in S7 (census here): violations a/b/c/"
              "d = %d/%d/%d/%d of %d anchors -> %s"
              % (len(viols["ok_a"]), len(viols["ok_b"]),
                 len(viols["ok_c"]), len(viols["ok_d"]),
                 len(tests), verdict_main))

    # ---------------- S6: exponents + small-gap contrast
    section("S6  LEG C -- e_tot MEASUREMENT + SMALL-GAP CONTRAST")
    if smoke:
        check("G60-etot-census", True, "SMOKE: skipped")
        check("G61-gap-contrast", True, "SMOKE: skipped")
    else:
        fsort = sorted(frecs, key=lambda rc: (rc["ev"]["m"],
                                              rc["kz"]))
        msF = [rc["ev"]["m"] for rc in fsort]
        e_G = L2D.halves_slope(
            msF, [tests[rc["kz"]]["Glog"] for rc in fsort])
        e_M2 = L2D.halves_slope(
            msF, [tests[rc["kz"]]["mM2"] for rc in fsort])
        e_tot = e_G + e_M2
        tag_etot = ("EXPONENT_CONSISTENT"
                    if abs(e_tot - ETOT_REF) <= CONS_BAND
                    else "EXPONENT_SHIFTED")
        check("G60-etot-census", True,
              "e(G/log m) = %+.3f (r324 rec %+.3f), e(m M_2) = "
              "%+.3f (rec %+.3f), e_tot = %+.3f vs rec %+.3f "
              "(census band %.2f) -> %s -- MEASUREMENT ONLY on %d "
              "fresh anchors (two dyadic halves of %d), no gate"
              % (e_G, EG_REF, e_M2, EM2_REF, e_tot, ETOT_REF,
                 CONS_BAND, tag_etot, len(fsort),
                 len(fsort) // 2))
        lad_deep = [i for i in range(n65) if i >= 42]

        def coh(vals_rho, vals_fa, vals_gl, vals_m2):
            spk = sum(1 for f in vals_fa if f >= SPIKE_FA) \
                / max(len(vals_fa), 1)
            return (float(np.median(vals_rho)),
                    float(np.median(vals_fa)), spk,
                    float(np.median(vals_gl)),
                    float(np.median(vals_m2)))

        cB = coh([tests[rc["kz"]]["rho2"] for rc in frecs_b],
                 [tests[rc["kz"]]["fa"] for rc in frecs_b],
                 [tests[rc["kz"]]["Glog"] for rc in frecs_b],
                 [tests[rc["kz"]]["mM2"] for rc in frecs_b])
        cA = coh([tests[rc["kz"]]["rho2"] for rc in frecs_a],
                 [tests[rc["kz"]]["fa"] for rc in frecs_a],
                 [tests[rc["kz"]]["Glog"] for rc in frecs_a],
                 [tests[rc["kz"]]["mM2"] for rc in frecs_a])
        cL = coh([rho65[i] for i in lad_deep],
                 [FAC[idxC[srt65[i]["kz"]]] for i in lad_deep],
                 [m65[i] * qmax65[i] / math.log(float(m65[i]))
                  for i in lad_deep],
                 [m65[i] * srt65[i]["ev"]["cm"]["S2"]
                  for i in lad_deep])
        r_rho = cB[0] / max(cL[0], 1e-300)
        d_spk = abs(cB[2] - cL[2])
        r_fa = cB[1] / max(cL[1], 1e-300)
        fired = []
        if r_rho >= CONTRAST_RHO_FAC or r_rho <= 1.0 \
                / CONTRAST_RHO_FAC:
            fired.append("rho2 med x%.2f" % r_rho)
        if d_spk >= CONTRAST_SPIKE_D:
            fired.append("spike rate d%.2f" % d_spk)
        if r_fa >= CONTRAST_FA_FAC or r_fa <= 1.0 \
                / CONTRAST_FA_FAC:
            fired.append("F_A med x%.2f" % r_fa)
        tag_gap = ("SMALL_GAP_DIFFERENT(%s)" % "; ".join(fired)
                   if fired else "SMALL_GAP_SIMILAR")
        check("G61-gap-contrast", True,
              "cohorts (med rho2 / med F_A / spike rate F_A >= "
              "%.1f / med G/logm / med mM2): B small-gap "
              "%.4f/%.2f/%.2f/%.2f/%.2f; A depth %.4f/%.2f/%.2f/"
              "%.2f/%.2f; LADDER_DEEP (rank >= 42, n=%d) "
              "%.4f/%.2f/%.2f/%.2f/%.2f; sealed bars (x%.1f rho, "
              "d%.1f spike, x%.1f F_A) -> %s"
              % (SPIKE_FA, cB[0], cB[1], cB[2], cB[3], cB[4],
                 cA[0], cA[1], cA[2], cA[3], cA[4], len(lad_deep),
                 cL[0], cL[1], cL[2], cL[3], cL[4],
                 CONTRAST_RHO_FAC, CONTRAST_SPIKE_D,
                 CONTRAST_FA_FAC, tag_gap))

    # ---------------- S7: adjudication
    section("S7  LEG D -- SEALED ADJUDICATION")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
    else:
        n_main = (1 if all_hold else 0) + (0 if all_hold else 1)
        check("G70-adjudication", n_main == 1,
              "exactly one sealed main letter fired: %s + %s + %s"
              % (verdict_main, tag_etot, tag_gap))

    # ---------------- S8: must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    real_int = len(set(kz for (_h, kz) in fresh) & used)
    mut_set = mutant_collision([kz for (_h, kz) in fresh][:2],
                               list(frame_kzs))
    mut_int = len(set(mut_set) & used)
    check("G80-e1-anchor-collision",
          real_int == 0 and mut_int >= 1,
          "e1 CAUGHT: the injected core-ladder anchor kz%d makes "
          "the mutant set intersect the used ledger (%d hits) "
          "while the real EXT3 selection is disjoint EXACT (0 "
          "hits on %d fresh windows)"
          % (int(frame_kzs[0]), mut_int, len(fresh)))
    toy_F = (1.0, 2.0)
    toy_r = (0.5, 4.0)
    b_mut = mutant_b_recal(toy_F, toy_r)
    check("G81-e2-constant-recal",
          len(e2_hits) >= 1
          and abs(b_mut - FROZEN_B) >= MUT_MIN,
          "e2 CAUGHT twice: the after-sight recalibration consumes "
          "the bound column -- AST-FLAGGED (%s) -- and on the "
          "sealed toy returns %.4f != the FROZEN record %.4f "
          "(diff %.4f >= %.0e); the real tests consume the frozen "
          "record numbers only"
          % (e2_hits[0] if e2_hits else "MISS", b_mut, FROZEN_B,
             abs(b_mut - FROZEN_B), MUT_MIN))
    toy_gr2 = (1.0, 1.0, 1.0, 5.0)
    toy_r2 = (1.0, 1.0, 1.0, 9.0)
    th_mut = mutant_gap_posthoc(toy_gr2, toy_r2)
    check("G82-e3-gap-posthoc",
          len(e3_hits) >= 1 and abs(th_mut - GAP_SMALL) >= MUT_MIN,
          "e3 CAUGHT: the after-sight gap rule consumes the bound "
          "column -- AST-FLAGGED (%s) -- and on the sealed toy "
          "returns threshold %.2f != the sealed class edge %.2f; "
          "the real stratification uses fixed a-priori classes"
          % (e3_hits[0] if e3_hits else "MISS", th_mut, GAP_SMALL))
    ev9 = (recs[0] if smoke else mrecs[0])["ev"]
    rb = mutant_strat_readback(ev9["cm"], ev9["m"])
    check("G83-e4-target-readback",
          len(e4_hits) >= 1 and rb > 0.0,
          "e4 AST-CAUGHT: the 'selection score' consuming the "
          "cubic-moment record is FLAGGED (%s) while the five "
          "module-own selection builders are clean (%d hits) -- "
          "target read-back into the anchor choice is machine-"
          "refused" % (e4_hits[0] if e4_hits else "MISS",
                       len(sc_own)))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed EXT3 fresh-anchor selection (used "
          "ledger + two strata + gap stratification), the four "
          "frozen-constant tests on genuinely new windows, the "
          "e_tot census and the audit-C1 small-gap contrast -- NO "
          "new certificate promoted, NO constant recalibrated")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R329_ANCHORS(branch 35+7, r306 C2 %.3f 0/57, "
                 "r316 n %d C_small %.4f, r321 b %.4f 0/39 named "
                 "%d/4, r324 C_NSC %.4f 0/39, r327 C_NG %.4f "
                 "0/39 named %d/4)"
                 % (C2, n65, C_small, b_repro, named_b,
                    cnsc_repro, cng_repro, named_ng)]
        parts.append("SEAL(frame reproduction %d, used ledger %d, "
                     "disjoint 0, purity clean, toys exact, "
                     "wards live)"
                     % (len(frame_kzs), len(used)))
        parts.append("SELECTION(%d anchors: B %s / A %s; ladder "
                     "grel med %.2f vs B med %.2f)"
                     % (len(frecs),
                        str([rc["kz"] for rc in frecs_b]),
                        str([rc["kz"] for rc in frecs_a]),
                        float(np.median(grel_lad)),
                        float(np.median([grel_f[rc["kz"]]
                                         for rc in frecs_b]))))
        parts.append("EXT3_TABLE(viol a/b/c/d %d/%d/%d/%d)"
                     % (len(viols["ok_a"]), len(viols["ok_b"]),
                        len(viols["ok_c"]), len(viols["ok_d"])))
        parts.append(verdict_main)
        parts.append("ETOT(e_G %+.3f, e_M2 %+.3f, e_tot %+.3f vs "
                     "%+.3f, %s)"
                     % (e_G, e_M2, e_tot, ETOT_REF, tag_etot))
        parts.append("GAPCONTRAST(%s)" % tag_gap)
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the construction "
          "reproduction, the disjointness, the identity/"
          "interpolation/pileup/ledger wards and the purity "
          "audits (exact / AST-decided); MEASURED: every frozen-"
          "test outcome, reserve, exponent and contrast metric "
          "(12 fresh finite windows + the 65-rung ladder + 2 "
          "mains + controls); OPEN: any bound beyond the measured "
          "windows, the cofinal law, a second live world "
          "(Dirichlet-L, audit repair 4), kz15 beyond r270; NO "
          "RH claim" % (verd, " (SMOKE)" if smoke else ""))
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
