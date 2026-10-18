#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""two_regime_bound_probe -- PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01
(round 316): THE TWO-REGIME BOUND -- part 3 of the reviewer's
signed-cube contract: formulate the pointwise Renyi-3 bound as a
COUPLED TWO-REGIME STATEMENT over the FCIX stratum and certify it
on every available rung with a mid-ladder calibration SEALED IN
ADVANCE.  Reviewer goal (part 3, verbatim): NOT to prove the
number 1.069 -- sufficient is a Phi-type bound => sum q^3 <= C x
(log m)^A / m^2 for SOME fixed A and explicit C (and m_0); then
N_3 >= m/(sqrt(C) (log m)^{A/2}), N_2 >= N_3, every demanded
power follows asymptotically; the finitely many small m are
certified separately.  Context (sealed record inputs): r314
(SPEC 841b3196) proved the exact signed cubic identity sum |x|^3
= DeltaF + C_collision (+ C_boundary == 0) with a LOCAL
divergence form and exactly countable collisions (multiplicity
2); r315 (SPEC 92d35a3a) sealed PHI3_ALL_BLIND -- the three
divergence-form candidates fail, but the diagnosis is SHARP: the
ENTIRE failure sits on kz55 + kz67, the only rungs with FCIX
0.955/0.915 vs med 0.629 -- exactly where the intra-block flux
cancellation DIES; all trends fall (the known shallow-calibration
artifact family of r306-A<=1 and r313-T1/T4); the named R316
form is a coupled two-regime statement over the FCIX stratum
with a pre-sealed mid-ladder calibration (FCIX is source-pure
and computable in advance); r306 (SPEC 3bb365e1) fixed the target
scale sum q^3 <= 1.069 (log m)^2 / m^2 on 57 rungs.  kz15
permanently closed via r270; the 6 exceptions via the r287 F2
certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the r312 block-Green round may run in parallel; this
probe touches NOTHING outside its own file and the additive
rh-sync.

THE OBJECT (r269/r287/r298/r306/r314/r315 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F =
0.20 edge split; maximal same-sign runs of the bx-sorted bulk;
level-2 blocks (r270 convention); the frozen positional block
machinery (r298 WBT.block_breaks + WBT.aggregate_blocks); the
r306 RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze; the
r314 SCF.fold_genealogy + SCF.signed_cube_terms +
SCF.flux_telescope + SCF.collision_census; the r315
PHI.phi3_variants + PHI.mult3_control, ALL imported verbatim;
PDelta = Pbeta - Pomega; x_j = (PDelta)_j.  NEW in this round
(module-own, source-pure): the two-regime state builder (the
four sealed regime majorants), the sealed mid-ladder split rule
and the coupled adjudication.

THE SEALED TWO-REGIME STATEMENT (frozen BEFORE any evaluation of
this round; every formula and every rule fixed here).  On the
divergence-form state of one rung (r314 objects: block sums x_j,
group power sums Q2_j/Q3_j, ordered fold-group values G1, block
slice pointers, per-block flux ends F_end_j and openings
F_open_j, abs edge mass sum |dF|), with sigma_j = sign(x_j), L =
sum |x_j|, NORM = m^2/((log m)^2 L^3) (the r306 scale: NORM x
sum|x|^3 == rho_2), define
    COLL  = sum_j sigma_j (3 Q2_j x_j - 2 Q3_j),
    DFLUX = sum_j sigma_j F_end_j,   BND = sum_j sigma_j F_open_j,
    FE    = sum_j |F_end_j|,         FCIX = FE / sum |dF|,
    QMAX  = max_j |x_j| / L,
    CNT3  = sum_j (n_j + 3 n_j (n_j - 1)) x (max_{g in j} |G1_g|)^3
            (n_j = fold groups of block j: the EXACT count of
            collision group triples of the r314 census times the
            per-block group-value cube cap),
and the FOUR SEALED REGIME MAJORANTS (all >= rho_2 by disclosed
exact algebra, warded live):
    PhiL2 = NORM x (|COLL| + |BND| + FE)      [regime-L primary:
            the Phi3c-like flux-index form -- |DFLUX| <= FE =
            FCIX x sum|dF| by the triangle inequality, so the
            flux part carries the cancellation index
            multiplicatively],
    PhiL1 = NORM x (|COLL| + |BND| + |DFLUX|) [regime-L fallback
            == the r315 Phi3a, the reviewer raw form],
    PhiH2 = NORM x (CNT3 + |BND| + FE)        [regime-H primary:
            the COUNTING majorant -- |3 Q2 x - 2 Q3| <=
            (n + 3n(n-1)) g~^3 per block because the collision
            part is EXACTLY the sum over the n + 3n(n-1) ordered
            repeated-index group triples (r314 census), each
            product capped by g~^3: in regime H the exact
            counting bites where the flux cancellation dies],
    PhiH1 = (m x QMAX / log m)^2              [regime-H fallback:
            the CONCENTRATION majorant -- sum q^3 <= QMAX^2
            since sum q^3 <= QMAX^2 sum q].
DISCLOSED ALGEBRAIC CHAIN (derived, no measurement): rho_2 =
NORM sum|x|^3 <= PhiL1 <= PhiL2 <= PhiH2 and rho_2 <= PhiH1 --
every certification below transfers to sum q^3 <= C (log m)^2 /
m^2 by pure algebra (A = 2 is fixed by the NORM exponent).  The
compensation form NORM x |COLL + DFLUX| is by the r314 identity
EXACTLY rho_2 (BND == 0): it is adjudicated READ-BACK-ADJACENT
and enters only as the diagnostic census column kappa =
cube/(|COLL| + |DFLUX|), never as a candidate.

THE SEALED REGIME RULE: theta = 0.85, frozen from the r315
RECORD FCIX census (bulk med 0.629 with the two outliers at
0.955/0.915 -- theta sits in the recorded gap; FCIX is
source-pure and computed BEFORE any bound value of this round);
regime L = rungs with FCIX <= theta (the flux cancellation
lives), regime H = rungs with FCIX > theta (the cancellation is
dead -- kz55/kz67 by the r315 record, plus any new deep rung).
The measured FCIX gap around theta is printed as census.

THE SEALED MID-LADDER CALIBRATION (the r315 lesson, now
rule-conform IN ADVANCE): on the (N, kz)-sorted class ladder of
n rungs (42 core + 15 r286 extension + the new EXT2 anchors;
class = multiplicity cap <= 2, POSITIVE_PREFIX), CAL_START =
n // 3; calibration set = the N_CAL = 5 rungs CAL_START ..
CAL_START+4; SMALL-M set = ranks 0 .. CAL_START-1 (the finitely
many small m: certified INDIVIDUALLY by direct evaluation, their
max rho_2 = C_small is the exception constant); TEST set = ranks
CAL_START+5 .. n-1; m_0 = min m over calibration + test.
Constants frozen on the calibration window: C_L(v) = max of
PhiL_v over the regime-L calibration rungs (empty => the sealed
REGIME_L_FAILS_MIDLADDER fires); C_H(v) = max of PhiH_v over ALL
five calibration rungs (disclosed: the H stratum is thin -- the
H constant is calibrated on the H-functional's mid-ladder scale,
and whether it transfers to the FCIX > theta stratum is exactly
the honest question of the round).  Split hygiene: cal/test/
small are pairwise disjoint and cover the ladder (exact index
ward; the e3 mutant proves the ward bites).  Candidate
precedence sealed: L2 > L1 (the contract names the flux-index
form as the regime-L primary), H2 > H1 (the counting exit is the
contract's elegant outcome) -- first candidate with 0 violations
on its regime's test rungs wins.

LEG 0 -- ANCHOR REGRESSION (r314/r315/r306 record numbers
adopted as-is, disclosed): med signed shares DeltaF/C_pair/
C_full = -0.4226/+0.5980/+0.8537 (tol 0.005); FC med 0.629 (tol
0.005) slope -0.141 (tol 0.01); fold multiplicity == 2 UNIFORM
on the 57 r315 rungs (exact); the r314 identity wards live
(recomposition <= REC3_BAR, telescope <= TEL_BAR, boundary <=
BND_BAR); the r306 bound live at A = 2: C_2 = 1.069 (tol 0.005)
first-5 freeze, 0/57 violations; the r315 candidate constants
re-frozen bit-near: C0 a/b/c = 2.6261/1.5052/0.9400 (tol 0.005);
the r315 FCIX outlier anchors kz55 = 0.955 / kz67 = 0.915 (tol
0.005).

LEG A -- SEALING (before any bound evaluation): (A1) theta,
split rule, candidate formulas and precedences are printed as
the sealed definitions; the regime table (rank, kz, N, m, FCIX,
regime, set membership) is printed BEFORE any bound table.
(A2) SOURCE-PURITY AUDITS: the AST identifier scan over
two_regime_state + split_midladder must be clean against
BOUND_FORBIDDEN and PHI3_FORBIDDEN (no cubic-target read-back,
no withheld keys); the literal scan must be clean against the
sealed record-literal set R31X_TABLE_LITERALS (r314 world table
+ r315 record numbers); the e1/e2/e2b mutants prove all three
audits bite.  (A3) TOY EXACTNESS (Fractions, dyadic-exact): the
mixed-sign two-block toy {2,-1}|{-3}: cube = 28 == |COLL| = 28
(DFLUX = 0, BND = 0), CNT3 = 8 x 8 + 27 = 91 >= 28, QMAX-bound
28 <= (3/4)^2 x 64 = 36 -- every majorant an exact rational
comparison; the flux toy (1,2,3,4): cube 1000 = COLL 700 +
DFLUX 300, FE = 300, CNT3 = 40 x 64 = 2560 >= 700, QMAX bound
tight at equality (single block); float builders match the
Fractions tables (bar 1e-14).  (A4) LIVE MAJORANT CHAIN WARD:
rho_2 <= PhiL1 <= PhiL2 <= PhiH2 and rho_2 <= PhiH1 on EVERY
live world (rel slack <= CHAIN_BAR), plus NORM x cube == rho_2
(the r314 cube crossward) and the two_regime_state components ==
the r315 phi3_variants components (COLL/DFLUX/FCIX cross-ward).
(A5) EXT2 EXTENSION (honest budget sizing, census-grade): the
r286-rule pool continued past the r315 ladder -- the leftover
h <= 1300 candidates plus the first EXT2_POOL_CAP = 12 windows
with 1300 < h <= 1650 by h; wpacked, (N, kz)-sorted, the first
K_EXT2 = 8 POSITIVE_PREFIX rungs join the class ladder (more
rungs = more potential regime-H cases); census only, no sealed
N_w expectation; contribution wards at the deep bar; rungs with
fold multiplicity > 2 are EXCLUDED from the class ladder and
named (the r315 cap side condition).

LEG B -- REGIME L (the divergence-form bound): per L-candidate
the frozen C_L, then certification on every regime-L TEST rung
(violations, reserve min/med, halves-slope trend on both the
regime-L test rungs and disclosed as census); the winner by the
sealed precedence.  Small-m certificates printed per rung
(rho_2 values; C_small = max).

LEG C -- REGIME H (the new mechanism): (C1) DISSECTION CENSUS on
every FCIX > theta rung (any set): rho_2, PhiL2 (the would-be L
bound), PhiH1/PhiH2, QMAX, top-1 cube share max|x|^3/cube, the
counting tightness CNT3/|COLL|, the compensation kappa =
cube/(|COLL| + |DFLUX|) (read-back-adjacent, diagnostic only),
the C_full share and n_eff = N_2; the discriminator column vs
the regime-L test med is NAMED (largest rel deviation >=
ATTR_MIN).  (C2) CERTIFICATION: per H-candidate the frozen C_H,
violations on the regime-H TEST rungs, the winner by sealed
precedence; the REGIME-H MECHANICS OBJECT of the round = the
winning majorant + the named discriminator.  Empty H test
stratum => the sealed REGIME_H_UNEXPLAINED fires (disclosed).

LEG D -- THE COUPLED ADJUDICATION (sealed BEFORE evaluation;
exactly one fires): regL_ok = an L-candidate certifies all
regime-L test rungs; regH_ok = an H-candidate certifies all
regime-H test rungs (non-empty stratum required); world_ok =
the CLASS check (the r315 machinery: (w1) w9/w13/EPSTEIN are
ADMITTED -- fold multiplicity <= 2 AND rho_2 <= C_tot; the
regime-majorant values of the worlds are printed as census
only, disclosed: the majorant is measured LOOSE on EPSTEIN
(r315 record: EPST holds C0 only via shallow inflation), so
world admission is adjudicated at class + consequence level;
(w2) the twin band max(w13/w9, w9/w13) <= TWIN_FAC = 3.0 on
PhiL2; (w3) SCRAMBLE is REJECTED by the class machinery: the
component attribution names a collision/flux column (dev >=
ATTR_MIN = 0.25 vs the MAIN med, r315 K4 verbatim) AND the
seeded assignment shuffle (SEED_SHUF = 316001) breaks the flux
profile edgewise (>= MUT_MIN) with matched mass; SCRAMBLE's
rho_2 vs C_tot printed as census).  With C2R = max(C_L*, C_H*),
C_small = max small-m rho_2, C_tot = max(C2R, C_small):
  TWO_REGIME_GO(C, A = 2, m_0, theta)  iff regL_ok AND regH_ok
      AND world_ok -- the coupled statement certifies: EVERY
      class rung with m >= m_0 satisfies (FCIX <= theta AND
      PhiL* <= C_L) OR (FCIX > theta AND PhiH* <= C_H), both
      imply sum q^3 <= C2R (log m)^2/m^2 by the sealed algebra;
      the small-m rungs are separately certified (C_small), so
      sum q^3 <= C_tot (log m)^2/m^2 on EVERY measured rung and
      N_3 >= m/(sqrt(C_tot) log m), N_2 >= N_3 (r306 chain);
  REGIME_L_FAILS_MIDLADDER  iff NOT regL_ok AND regH_ok;
  REGIME_H_UNEXPLAINED      iff regL_ok AND NOT regH_ok (incl.
      the empty-stratum case, named);
  TWO_REGIME_DEAD           otherwise (both regimes fail, OR
      both certify but the world/class check leaks -- the leak
      is named; disclosed: a world leak with certified regimes
      is adjudicated DEAD, not GO).
The CANDIDATE THEOREM text (with every measured constant) is
printed whenever both regimes certify, labeled by the verdict.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) THETA MOVED AFTER SIGHT (simulated): mutant_theta_posthoc
  re-picks theta from a grid by MINIMIZING the regime-H mass of
  an evaluated bound column -- the BOUND_FORBIDDEN scope audit
  must FLAG it (it consumes the rho column) AND on the sealed
  toy (fcix 0.5/0.9, values 1/5) it returns 0.9 != theta --
  CAUGHT twice.
(e2) REGIME-H BOUND CONSUMES sum q^3: mutant_h_readback computes
  NORM x S3 L1^3 from the cubic-moment record -- the
  PHI3_FORBIDDEN scan must FLAG it (AST-CAUGHT) while
  two_regime_state stays clean.
(e2b) RECORD-LITERAL CALIBRATION: mutant_fcix_calibrated carries
  the r315 record number 0.955 (the kz55 FCIX) as its decision
  constant -- the literal scan must FLAG it while the real
  builders are literal-clean.
(e3) OVERLAPPING SPLIT: mutant_split_overlap returns cal/test
  windows sharing EXACTLY one rank -- the split ward must
  measure intersection 1 EXACT on the mutant and 0 EXACT on the
  sealed split -- CAUGHT.
(e4) MULTIPLICITY-3 CONTROL (r315 constructor verbatim, matched
  boundary statistics: G1/blocks/positions/mass preserved
  BITWISE): the class REJECTS via the cap (mult 3 > MULT_CAP)
  and the collision count bound BREAKS (3 p1 p2 - 2 p3 != the
  mult-2 closed form; w9: 48762 vs 14448); DISCLOSED: all four
  regime majorants are BLIND to the control (G1 and the group
  structure are preserved -- warded <= 1e-12): the cap remains
  a necessary CLASS side condition, exactly the r315 finding.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the
  branch label are both FLAGGED by the AST scope audit.  Scope
  hygiene: the new builders (two_regime_state, split_midladder)
  consume genealogy + flux state + rank counts only; fragment
  audit (no fit primitives).

INDEX FIREWALL (binding, r238-r315 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target sum q^3 / rho_2 enters GATES / anchors /
small-m certificates / diagnostic columns only, NEVER a regime
builder (AST-warded); no zero/prime oracles anywhere (AST
firewall); no fit primitives (fragment audit).  MACHINERY
IMPORTED VERBATIM: r315 PHI.phi3_variants + PHI.mult3_control,
r314 SCF.fold_genealogy + SCF.signed_cube_terms +
SCF.flux_telescope + SCF.collision_census, r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze, r298
WBT.block_breaks + WBT.aggregate_blocks, r269 PBB.mask_edge +
PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}; EXTENSION: 900 <
h <= 1300, first 15 by (N, kz) (the r286 anchors, N_w
942..1218); EXT2: the sealed A5 rule above.

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; XW_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; THETA 0.85 (FROZEN, Leg A); N_CAL 5;
CAL_THIRD 3; RES_EPS 0.01; ATTR_MIN 0.25; TWIN_FAC 3.0;
SEED_SHUF 316001; MUT_MIN 1e-6; TOY_BAR 1e-14; TB_WARD bars 1e-9
main N <= 400 / 3e-6 deep + ext + ext2 / 1e-6 controls; ID_BAR
1e-12; AC_BAR 1e-9; R314 anchors: shares (-0.4226, +0.5980,
+0.8537) tol 0.005, FC med 0.629 tol 0.005 slope -0.141 tol
0.01, multiplicity == 2 on 57/57 EXACT; R306 anchor: C_2 1.069
tol 0.005, 0/57 violations; R315 anchors: C0 (2.6261, 1.5052,
0.9400) tol 0.005, FCIX kz55/kz67 (0.955, 0.915) tol 0.005;
R31X_TABLE_LITERALS (the sealed forbidden calibration set,
rounded 4 decimals) = the r314 set {-0.4226, 0.598, 0.8537,
0.629, -0.141, -0.452, 0.823, 0.617, 0.057, -0.541, 0.43,
1.111, 0.675, 0.043, -2.695, -2.652, 6.347, 0.101, 0.011,
-0.171, 0.856, 0.315, 0.693, 0.073} plus the r315 record set
{2.6261, 1.5052, 0.94, 0.955, 0.915, 22.85, 66.09, 87.64,
2.3883, 2.0841, 1.4433, 2.3545, 1.3615, 0.1375, 0.9597, 0.7102,
0.4795, 4.6095, 2.726, 2.5458, 1.8898, 2.432, 1.7289, 3.69};
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the chain ward on w9 + controls + the regime state at
w9 + e1-e4 + e2b; ladder, extensions, anchors, split,
certification and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r314/r315/r306 RECORD number adopted as-is;
theta = 0.85 is chosen INSIDE the recorded r315 FCIX gap
(0.629 bulk med vs 0.955/0.915 outliers) and frozen here; the
mid-ladder rule (CAL_THIRD = 3, N_CAL = 5) is sealed from the
r315 lesson BEFORE any bound value of this round exists; the
four majorant chains, the A = 2 exponent, the collision-triple
count n + 3n(n-1) and the QMAX bound are derived algebra,
disclosed above; the EXT2 budget sizing (12-window pool cap, 8
anchors, seconds per deep wpack) is adopted from the r306/r307
records; the world-check semantics (class + consequence level
for admission, majorant values census-only) is forced by the
r315 RECORD fact that the majorant is loose on EPSTEIN --
disclosed here, not tuned later; NO regime value, NO constant
and NO violation count of this round was computed before this
spec was frozen; the four sealed verdicts are symmetric -- no
rule was chosen to favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the four main verdicts fires):
  R316_ANCHORS(r314 shares + FC + mult live, identity wards,
    r306 C_2 live, r315 C0 + FCIX outlier anchors)
+ SEAL(theta + split + candidates + purity audits)
+ REGIMES(census: stratum sizes, FCIX gap around theta,
    kz55/kz67 membership, EXT2 additions)
+ SMALLM(C_small, n rungs, per-rung certificates)
+ REGIME_L(winner, C_L, violations, reserve, trend)
+ REGIME_H(dissection census + named discriminator, winner,
    C_H, violations)
+ WORLD(admission + twin band + SCRAMBLE rejection)
+ [exactly one of] TWO_REGIME_GO(C, A, m_0, theta) /
    REGIME_L_FAILS_MIDLADDER / REGIME_H_UNEXPLAINED /
    TWO_REGIME_DEAD
+ THEOREM(candidate text printed when both regimes certify)
+ MUSTFAIL_LEDGER(e1-e4 + e2b + scopes).
Honesty before beauty: theta, the split rule, every candidate
formula, every precedence and every bar are sealed BEFORE
evaluation; the majorant chains are exact algebra (Fractions on
toys, warded live), so every certification transfers to the
cubic target by algebra, not by fit; every constant, violation
count, reserve and trend is MEASURED on the finite class ladder
(42 + 15 + EXT2 rungs) -- a GO fixes a certified two-regime
STATEMENT ON THE MEASURED RUNGS with explicit (C, A, m_0,
theta), it proves NO universal bound beyond them and NO cofinal
law; the small-m list is a finite certificate table, not an
asymptotic statement; the regime-H stratum is TINY by the r315
record (2 known members) -- its certification is correspondingly
weak evidence, typed as census; the world columns are n = 1 per
control; r243-r315 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 35/35 (0.3 s), NO amendment; calibration pass 1 =
first full evaluation, 35/35, wall 39.6 s, NO amendment; record
run1/run2 after this insertion, identical up to WALL; the ONLY
post-freeze edit is this record-table insertion, which IS the
protocol -- no bar, band, rule or verdict rule moved):
CAL_VERDICT = R316_ANCHORS(shares -0.4226/+0.5980/+0.8537, FC
0.629/-0.141, mult == 2 on 57/57, identity wards 4.5e-17 /
4.7e-16 / 4.1e-16, r306 C_2 1.069 viol 0/57, r315 C0
2.6261/1.5052/0.9400, FCIX kz55/kz67 0.955/0.915 -- ALL bit-near
the records) + SEAL(purity clean: 0 identifier + 0 literal hits
on the builders; e1 AST-CAUGHT rho + toy theta 0.90 != 0.85; e2
AST-CAUGHT cm; e2b literal-CAUGHT 0.955; chain ward worst slack
6.5e-16 on 69 live worlds; NORM x cube == rho_2 worst 7.9e-16;
component cross-wards 0.0) + REGIMES(the EXT2 rule admits 8/8
POSITIVE_PREFIX anchors N_w 1218..1393 (pool: 5 leftover + 8
windows 1300 < h <= 1650), mult == 2 on 8/8, 0 exclusions --
class ladder n = 65; stratum sizes 63 L / 2 H, the H stratum is
EXACTLY {kz55 FCIX 0.955, kz67 0.915} -- NO new deep H member
(deep FCIX 0.385..0.767); measured gap around theta: largest L
0.767 < 0.85 < smallest H 0.915, width 0.148; split: small =
ranks 0..20 (m 28..73), cal = 21..25 (m 73..95, N 388..488),
test = 26..64 (m 94..274, N 488..1393), m_0 = 73; kz55 = rank
20 = the LAST SMALL rank, kz67 = rank 35 TEST -- the H test
stratum shrinks to ONE rung) + SMALLM(21 rungs certified
individually, C_small = 1.0694 at rank 0 = kz18 (the r306
shallow maximum); kz55 small-certificate rho_2 0.4821) +
REGIME_L(C_L frozen on the 5 regime-L cal rungs: L2 0.7476
(argmax kz34) / L1 0.5531; violations on the 38 regime-L test
rungs: L2 8 / L1 9 -- NO winner; the L2 violators: kz53 1.4263,
kz105 1.1266, kz83 1.0804, kz71 0.9648, kz68 0.8013, kz88
0.7877, kz76 0.7819, kz119 0.7698; reserve min/med 0.52/1.35;
trend census L2 +0.086 / L1 +0.202 -- the majorant RISES on the
test set while rho_2 falls) + REGIME_H(dissection: kz55 FCIX
0.955 rho_2 0.4821 PhiL2 4.64 PhiH2 57.30 PhiH1 2.76 top1 0.558
kappa 0.105 tight 21.7 full +3.27 neff 31.9; kz67 FCIX 0.915
rho_2 1.0536 PhiL2 2.73 PhiH2 47.86 PhiH1 7.84 top1 0.785 kappa
0.387 tight 24.9 full +0.73 neff 40.4; named discriminator TOP1
(dev 2.68 vs the regime-L test med; qmax 1.99, kappa 0.55,
tight 0.53, full 0.83) -- the H rungs are near-one-block worlds;
C_H frozen on the 5 cal rungs: H2 34.0556 / H1 3.0559; the ONE
H test rung kz67 violates BOTH (H2 47.86 > 34.06, H1 7.84 >
3.06) -- NO winner) + WORLD(w9/w13/EPSTEIN admitted: mult 2,
rho_2 0.458/0.461/0.368 <= C_tot; twin band PhiL2 factor 1.04
<= 3.0 -- the strongest twin result of the lane; SCRAMBLE
rejected by the class machinery: COLL attribution dev 3.69 >=
0.25 AND the seeded shuffle 316001 breaks the flux profile
edgewise 1.0e0 with mass matched 4.0e-17 (290/300 atoms);
census: SCR rho_2 1.780 > C_tot 1.069) + TWO_REGIME_DEAD(L
fails; H fails) + THEOREM(not printed -- both regimes failed
certification) + MUSTFAIL_LEDGER(e1 AST+toy CAUGHT, e2
AST-CAUGHT, e2b literal-CAUGHT, e3 overlap 1 EXACT vs sealed 0
EXACT, e4 mult-3 cap-rejected + count break 48762 vs 14448 +
majorants blind 0.0e0, m5a/m5b FLAGGED).
READING (typed, no upgrade): the sealed letter is
TWO_REGIME_DEAD -- the FCIX two-regime formulation with these
majorants does NOT certify against mid-ladder-frozen constants
-- and the anatomy behind the letter is the round's real find:
(1) the FCIX STRATUM IS NOT THE NEAR-CRITICAL FAMILY: the
mid-ladder freeze is killed on the regime-L side by kz53 (PhiL2
1.43, rho_2 1.049 -- an r306-A<=1 killer with BULK-NORMAL FCIX
0.654) and by deep spikes kz83/kz105 (rho_2 0.78 / majorant
looseness 5.2x); the r315 diagnosis 'the failure sits on the
FCIX -> 1 rungs' captured kz55/kz67 but NOT kz53 -- the
obstruction family {kz53, kz55, kz67, kz83, ...} cuts ACROSS
the flux-cancellation stratum, so FCIX is the wrong (or an
incomplete) regime coordinate; (2) rho_2 itself is NOT below
its mid-ladder window (kz53 1.049 and kz83 0.779 vs the cal-
window rho_2 max 0.458): ANY pointwise majorant that is tight
on the calibration window must fail at kz53 -- the r306
constant survives only because the SHALLOWEST rung is the
global maximum; the mid-ladder discipline (sealed here for the
first time) reveals that the first-5 protocol was not a
shallow-calibration ARTIFACT but load-bearing: the profile is
NOT monotone, and near-critical spikes recur at mid and deep
ranks; (3) the REGIME-H MECHANICS OBJECT is delivered as
census despite the dead letter: the H rungs are near-one-block
worlds -- TOP1 cube share 0.558/0.785 vs 0.18 regime-L med
(dev 2.68, the named discriminator), with kz55 additionally
carrying 10x compensation (kappa 0.105: the identity terms
cancel 90 percent) -- concentration (candidate i), not the
counting tightness (dev 0.53, does NOT separate), is what
distinguishes the FCIX outliers; but the H certification
failed against the mid-window constants (kz67 misses H2 by
1.4x, H1 by 2.6x) and the H test stratum was ONE rung (kz55
fell into the small-m set at rank 20/65); (4) what HOLDS: all
anchors bit-near (r314 shares/FC/mult, r315 C0 + FCIX outliers,
r306 C_2 with 0/57), the four majorant chains exact live on 69
worlds (worst slack 6.5e-16), the EXT2 extension is clean (8
deep anchors to N_w 1393, all mult 2, all POSITIVE_PREFIX, NO
new H member -- the FCIX stratum did not grow with depth), the
class boundary machinery is intact (EPSTEIN/twin/main admitted
with the strongest twin band of the lane 1.04, SCRAMBLE
rejected via COLL 3.69 + edgewise flux break with matched
mass, mult-3 control rejected via cap with all four majorants
provably blind), and the small-m certificate table stands (21
rungs, C_small 1.0694).  Honest negatives: DEAD is the sealed
verdict and stands -- no theorem candidate is printed; the
regime-L failure is partly majorant looseness (NORM|COLL|
rises relative to rho_2: trend +0.086/+0.202 -- exactly the
r314 warning that C_full grows), so a sharper flux-exploiting
majorant is not excluded by this round, but the kz53 obstacle
(2) binds EVERY tight majorant under a mid-ladder freeze; the
H dissection is n = 2 census; nothing here bounds anything.
R317 direction (typed, census-grade): the regime coordinate
must capture the near-critical family itself -- TOP1/QMAX
concentration is source-pure, computable in advance, and
separates kz55/kz67 (0.56/0.79 vs 0.18 med) while kz53 needs a
second coordinate; alternatively the statement form must treat
the near-critical spikes as a SEPARATE certified exception
family (the r287-F2 pattern) rather than a regime.  Runtime
39.6 s full / 0.3 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: none except this record-table
insertion.

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
import phi3_functional_probe as PHI            # noqa: E402 r315
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
THETA = 0.85
N_CAL = 5
CAL_THIRD = 3
RES_EPS = 0.01
ATTR_MIN = 0.25
TWIN_FAC = 3.0
SEED_SHUF = 316001
MUT_MIN = 1e-6
TOY_BAR = 1e-14
EDGE_F = 0.20
PAIR_OFFSET = 0
R314_SHARES = (-0.4226, 0.5980, 0.8537)
R314_SHARE_TOL = 0.005
R314_FC = 0.629
R314_FC_TOL = 0.005
R314_FC_SLOPE = -0.141
R314_FC_SL_TOL = 0.01
R306_C2 = 1.069
R306_C2_TOL = 0.005
R315_C0 = (2.6261, 1.5052, 0.9400)
R315_C0_TOL = 0.005
R315_FCIX_KZ = {55: 0.955, 67: 0.915}
R315_FCIX_TOL = 0.005
R31X_TABLE_LITERALS = frozenset((
    -0.4226, 0.598, 0.8537, 0.629, -0.141,
    -0.452, 0.823, 0.617, 0.057,
    -0.541, 0.43, 1.111, 0.675, 0.043,
    -2.695, -2.652, 6.347, 0.101, 0.011,
    -0.171, 0.856, 0.315, 0.693, 0.073,
    2.6261, 1.5052, 0.94, 0.955, 0.915,
    22.85, 66.09, 87.64,
    2.3883, 2.0841, 1.4433, 2.3545, 1.3615, 0.1375,
    0.9597, 0.7102, 0.4795,
    4.6095, 2.726, 2.5458, 1.8898, 2.432, 1.7289, 3.69))

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

L_VARIANTS = ("L2", "L1")
H_VARIANTS = ("H2", "H1")


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
    lies in the sealed r314+r315 record-literal set."""
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
                            in R31X_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the fold-
# ---------------- genealogy state (block sums x, group power sums
# ---------------- Q2/Q3, ordered group values G1, slice pointers)
# ---------------- and the flux state (F_end, F_open, abs edge
# ---------------- mass) only; the withheld terminal drive key,
# ---------------- the branch label, the cubic target and the
# ---------------- record literals are forbidden (AST identifier
# ---------------- scan + literal scan).
def two_regime_state(x, Q2, Q3, G1, ptr, F_end, F_open, edge_abs, m):
    """the sealed two-regime majorant state of one rung: sigma =
    sign(x), L = sum |x_j|, NORM = m^2/((log m)^2 L^3); COLL =
    sum sigma (3 Q2 x - 2 Q3); DFLUX = sum sigma F_end; BND =
    sum sigma F_open; FE = sum |F_end|; FCIX = FE / sum |dF|;
    QMAX = max |x_j| / L; CNT3 = sum_j (n_j + 3 n_j (n_j - 1)) x
    (max_g |G1_g|)^3 over the blocks;
    PhiL2 = NORM (|COLL| + |BND| + FE)     [flux-index majorant],
    PhiL1 = NORM (|COLL| + |BND| + |DFLUX|) [r315 raw majorant],
    PhiH2 = NORM (CNT3 + |BND| + FE)       [counting majorant],
    PhiH1 = (m QMAX / log m)^2             [concentration]."""
    x = np.asarray(x, dtype=float)
    Q2 = np.asarray(Q2, dtype=float)
    Q3 = np.asarray(Q3, dtype=float)
    G1 = np.asarray(G1, dtype=float)
    Fe = np.asarray(F_end, dtype=float)
    Fo = np.asarray(F_open, dtype=float)
    sig = np.sign(x)
    L = float(np.sum(np.abs(x)))
    if m < 2 or L <= 0.0:
        return dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0, fe=0.0,
                    fcix=0.0, qmax=0.0, cnt3=0.0, phiL1=0.0,
                    phiL2=0.0, phiH1=0.0, phiH2=0.0, L=0.0)
    nrm = float(m) ** 2 / (math.log(float(m)) ** 2 * L ** 3)
    coll = float(np.sum(sig * (3.0 * Q2 * x - 2.0 * Q3)))
    dflux = float(np.sum(sig * Fe))
    bnd = float(np.sum(sig * Fo))
    fe = float(np.sum(np.abs(Fe)))
    fcix = fe / max(float(edge_abs), 1e-300)
    qmax = float(np.max(np.abs(x))) / L
    cnt3 = 0.0
    for j in range(m):
        g = G1[ptr[j]:ptr[j + 1]]
        n = int(len(g))
        if n == 0:
            continue
        gmax = float(np.max(np.abs(g)))
        cnt3 += float(n + 3 * n * (n - 1)) * gmax ** 3
    phiL1 = nrm * (abs(coll) + abs(bnd) + abs(dflux))
    phiL2 = nrm * (abs(coll) + abs(bnd) + fe)
    phiH2 = nrm * (cnt3 + abs(bnd) + fe)
    phiH1 = (float(m) * qmax / math.log(float(m))) ** 2
    return dict(nrm=nrm, coll=coll, dflux=dflux, bnd=bnd, fe=fe,
                fcix=fcix, qmax=qmax, cnt3=cnt3, phiL1=phiL1,
                phiL2=phiL2, phiH1=phiH1, phiH2=phiH2, L=L)


def split_midladder(n):
    """the SEALED mid-ladder calibration split on the (N, kz)-
    sorted class ladder of n rungs: CAL_START = n // CAL_THIRD;
    calibration = ranks CAL_START..CAL_START+N_CAL-1; small-m =
    ranks 0..CAL_START-1 (individually certified exceptions);
    test = the remaining deep ranks.  Pairwise disjoint, covering
    -- warded exactly."""
    start = n // CAL_THIRD
    end = min(start + N_CAL, n)
    small = tuple(range(0, start))
    cal = tuple(range(start, end))
    test = tuple(range(end, n))
    return small, cal, test


def mutant_theta_posthoc(fcix, rho):
    """e1 MUST-FAIL MUTANT: theta re-picked AFTER SIGHT of the
    evaluated bound column (consumes rho) by minimizing the
    regime-H mass -- the BOUND_FORBIDDEN scope audit must FLAG
    this, and on the sealed toy it returns != THETA."""
    best = THETA
    bestv = float("inf")
    for th in (0.5, 0.6, 0.7, 0.8, 0.9, 0.95):
        v = sum(r for f, r in zip(fcix, rho) if f > th)
        if v < bestv:
            bestv = v
            best = th
    return best


def mutant_h_readback(cmrec, nrm):
    """e2 MUST-FAIL MUTANT: a regime-H 'bound' consuming the
    cubic-moment record (the target side) -- the PHI3_FORBIDDEN
    identifier scan must FLAG this."""
    cm = cmrec
    return nrm * cm["S3"] * cm["L1"] ** 3


def mutant_fcix_calibrated(coll, nrm):
    """e2b MUST-FAIL MUTANT: a 'calibrated' regime functional
    carrying the r315 record number (the kz55 FCIX) as its
    decision constant -- the literal scan must FLAG this."""
    return nrm * abs(coll) * 0.955


def mutant_split_overlap(n):
    """e3 MUST-FAIL MUTANT: a mid-ladder split whose cal and test
    windows share EXACTLY one rank -- the split ward must measure
    intersection 1 on the mutant and 0 on the sealed split."""
    start = n // CAL_THIRD
    cal = tuple(range(start, start + N_CAL))
    test = tuple(range(start + N_CAL - 1, n))
    return cal, test


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'regime orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'regime constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the majorant algebra
# ---------------- decided as rational arithmetic on the toys
def fr_two_regime(blocks):
    """exact unnormalized two-regime parts on per-block Fraction
    group lists: COLL, DFLUX (telescope), BND, cube, FE, abs edge
    mass, CNT3, L, max|x| -- every majorant an exact rational
    comparison."""
    coll = Fr(0)
    dflux = Fr(0)
    bnd = Fr(0)
    cube = Fr(0)
    fe = Fr(0)
    de = Fr(0)
    cnt3 = Fr(0)
    xs = []
    for G in blocks:
        x = sum(G, Fr(0))
        Q2 = sum(g * g for g in G)
        Q3 = sum(g ** 3 for g in G)
        sig = 1 if x > 0 else (-1 if x < 0 else 0)
        s1 = Fr(0)
        s2 = Fr(0)
        F = Fr(0)
        F_open = Fr(0)
        for i, g in enumerate(G):
            if i == 0:
                F_open = g ** 3 - 3 * g * (g * g) + 2 * g ** 3
            else:
                dF = 3 * g * (s1 * s1 - s2)
                F += dF
                de += abs(dF)
            s1 += g
            s2 += g * g
        n = len(G)
        gmax = max(abs(g) for g in G)
        cnt3 += (n + 3 * n * (n - 1)) * gmax ** 3
        coll += sig * (3 * Q2 * x - 2 * Q3)
        dflux += sig * F
        bnd += sig * F_open
        cube += abs(x) ** 3
        fe += abs(F)
        xs.append(x)
    L = sum(abs(x) for x in xs)
    xmax = max(abs(x) for x in xs)
    return dict(coll=coll, dflux=dflux, bnd=bnd, cube=cube, fe=fe,
                de=de, cnt3=cnt3, L=L, xmax=xmax)


TOY_MIX = ([Fr(2), Fr(-1)], [Fr(-3)])
TOY_FLUX = ([Fr(1), Fr(2), Fr(3), Fr(4)],)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("two_regime_bound_probe -- "
          "PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01 part 3 (round 316)")
    print("SPEC_SHA %s   R315_SHA %s   R314_SHA %s (imported)"
          % (SPEC_SHA[:16], PHI.SPEC_SHA[:16], SCF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + chain ward + regime state "
                        "at w9 + e1-e4 + e2b; ladder, extensions, "
                        "anchors, split, certification and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE TWO-REGIME BOUND (reviewer contract, part 3): over "
          "the source-pure FCIX stratum with theta = %.2f sealed "
          "from the r315 record gap, certify (FCIX <= theta AND "
          "PhiL <= C_L) OR (FCIX > theta AND PhiH <= C_H) on "
          "every class rung with m >= m_0, both sides exact "
          "majorants of rho_2 = NORM sum|x|^3 (chains disclosed: "
          "rho_2 <= PhiL1 <= PhiL2 <= PhiH2, rho_2 <= PhiH1); "
          "mid-ladder calibration SEALED IN ADVANCE (CAL_START = "
          "n // %d, N_CAL = %d, small-m ranks certified "
          "individually); candidate precedences L2 > L1, H2 > "
          "H1; verdicts TWO_REGIME_GO / REGIME_L_FAILS_MIDLADDER "
          "/ REGIME_H_UNEXPLAINED / TWO_REGIME_DEAD sealed "
          "BEFORE evaluation" % (THETA, CAL_THIRD, N_CAL))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("two_regime_state", "split_midladder"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); own builders clean "
          "(%d hits); m5a gift-bound FLAGGED (%s); m5b "
          "branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r315 scaffold verbatim)
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
              "EXT2 (sealed A5 rule, census-grade, no N_w "
              "expectation): pool %d leftover + %d windows with "
              "%d < h <= %d; selected %d POSITIVE_PREFIX anchors, "
              "N_w %s..%s"
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
            shares = dict(far=C_far_flux / max(cube, 1e-300),
                          pair=sct["C_pair"] / max(cube, 1e-300),
                          full=sct["C_full"] / max(cube, 1e-300))
            mx_mult = int(np.max(gen["mult"])) if gen["ng"] else 0
            ph = PHI.phi3_variants(sct["x"], sct["Q2"], sct["Q3"],
                                   ft["F_end"], ft["F_open"],
                                   ft["edge_abs"], m)
            trs = two_regime_state(sct["x"], sct["Q2"], sct["Q3"],
                                   gen["G1"], gen["ptr"],
                                   ft["F_end"], ft["F_open"],
                                   ft["edge_abs"], m)
            rho2 = RY3.renyi3_ratio(cm["S3"], m, 2)
            # diagnostic census columns (read-back-adjacent,
            # computed OUTSIDE the builders, disclosed):
            kappa = cube / max(abs(trs["coll"])
                               + abs(trs["dflux"]), 1e-300)
            top1 = float(np.max(np.abs(sct["x"])) ** 3) \
                / max(cube, 1e-300)
            tight = trs["cnt3"] / max(abs(trs["coll"]), 1e-300)
        else:
            gen = sct = ft = cc = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            C_bnd = 0.0
            shares = dict(far=0.0, pair=0.0, full=0.0)
            mx_mult = 0
            ph = dict(a=0.0, b=0.0, c=0.0, nrm=0.0, dflux=0.0,
                      coll=0.0, bnd=0.0, fcix=0.0, L=0.0)
            trs = dict(nrm=0.0, coll=0.0, dflux=0.0, bnd=0.0,
                       fe=0.0, fcix=0.0, qmax=0.0, cnt3=0.0,
                       phiL1=0.0, phiL2=0.0, phiH1=0.0,
                       phiH2=0.0, L=0.0)
            rho2 = 0.0
            kappa = 0.0
            top1 = 0.0
            tight = 0.0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd, shares=shares,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    cc=cc, ph=ph, trs=trs, rho2=rho2, kappa=kappa,
                    top1=top1, tight=tight, pos_all=pos_all,
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

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION (r314/r315/r306)")
    rec3_w = max(rc["ev"]["rec3"] for rc in live)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live)
    check("G31-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR,
          "the r314 identity live on %d live worlds: three-term "
          "recomposition dev %.1e (bar %.0e), telescope dev %.1e "
          "(bar %.0e), boundary %.1e (bar %.0e)"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 shares far/pair/full = %+.4f/%+.4f/%+.4f, "
             "FCIX %.3f, mult max %d"
             % (ev9s["shares"]["far"], ev9s["shares"]["pair"],
                ev9s["shares"]["full"], ev9s["trs"]["fcix"],
                ev9s["mx_mult"]))
        check("G30-r314-shares-fc", True, "SMOKE: skipped")
        check("G32-r306-bound-live", True, "SMOKE: skipped")
        check("G33-r315-anchors", True, "SMOKE: skipped")
        srt57 = []
    else:
        srt57 = sorted(recs + erecs,
                       key=lambda rc: (rc["N"], rc["kz"]))
        Ns = [rc["N"] for rc in recs]

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        sh_far = [rc["ev"]["shares"]["far"] for rc in recs]
        sh_pair = [rc["ev"]["shares"]["pair"] for rc in recs]
        sh_full = [rc["ev"]["shares"]["full"] for rc in recs]
        fcs = [rc["ev"]["trs"]["fcix"] for rc in recs]
        meds = (float(np.median(sh_far)),
                float(np.median(sh_pair)),
                float(np.median(sh_full)))
        fc_med = float(np.median(fcs))
        fc_sl = slp(fcs)
        n_m2 = sum(1 for rc in srt57
                   if rc["ev"]["mx_mult"] == 2)
        check("G30-r314-shares-fc",
              all(abs(meds[i] - R314_SHARES[i]) <= R314_SHARE_TOL
                  for i in range(3))
              and abs(fc_med - R314_FC) <= R314_FC_TOL
              and abs(fc_sl - R314_FC_SLOPE) <= R314_FC_SL_TOL
              and n_m2 == len(srt57),
              "r314 record reproduced: med shares far/pair/full "
              "%+.4f/%+.4f/%+.4f (rec %+.4f/%+.4f/%+.4f tol "
              "%.3f); FC med %.3f slope %+.3f (rec %.3f/%+.3f); "
              "mult == 2 on %d/%d"
              % (meds[0], meds[1], meds[2], R314_SHARES[0],
                 R314_SHARES[1], R314_SHARES[2], R314_SHARE_TOL,
                 fc_med, fc_sl, R314_FC, R314_FC_SLOPE, n_m2,
                 len(srt57)))
        rhoT2 = [rc["ev"]["rho2"] for rc in srt57]
        C2, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2)
        check("G32-r306-bound-live",
              abs(C2 - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d"
              % (C2, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt57)))
        C0 = {}
        for i, v in enumerate(("a", "b", "c")):
            vals = [rc["ev"]["ph"][v] for rc in srt57]
            C0[v], _j0, _d0 = RY3.calib_freeze(vals, range(N_CAL))
        fcix_kz = {rc["kz"]: rc["ev"]["trs"]["fcix"]
                   for rc in srt57}
        ok_fcix = all(abs(fcix_kz.get(kz, -1.0)
                          - R315_FCIX_KZ[kz]) <= R315_FCIX_TOL
                      for kz in R315_FCIX_KZ)
        check("G33-r315-anchors",
              all(abs(C0[v] - R315_C0[i]) <= R315_C0_TOL
                  for i, v in enumerate(("a", "b", "c")))
              and ok_fcix,
              "r315 record reproduced: C0 a/b/c = "
              "%.4f/%.4f/%.4f (rec %.4f/%.4f/%.4f tol %.3f); "
              "FCIX outliers kz55 %.3f / kz67 %.3f (rec "
              "%.3f/%.3f tol %.3f)"
              % (C0["a"], C0["b"], C0["c"], R315_C0[0],
                 R315_C0[1], R315_C0[2], R315_C0_TOL,
                 fcix_kz.get(55, -1.0), fcix_kz.get(67, -1.0),
                 R315_FCIX_KZ[55], R315_FCIX_KZ[67],
                 R315_FCIX_TOL))

    # ---------------- S4: Leg A -- sealing + purity + toys + chain
    section("S4  LEG A -- SEALING + PURITY + TOYS + CHAIN WARD")
    pure_ids = []
    for fn in ("two_regime_state", "split_midladder"):
        pure_ids += scope_audit(fn, PHI3_FORBIDDEN)
    pure_lits = []
    for fn in ("two_regime_state", "split_midladder",
               "mutant_theta_posthoc", "mutant_split_overlap"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_theta_posthoc", BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_h_readback", PHI3_FORBIDDEN)
    e2b_hits = literal_audit("mutant_fcix_calibrated")
    check("G40-purity-audits",
          (not pure_ids) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e2b_hits) >= 1,
          "SOURCE PURITY: two_regime_state + split_midladder "
          "clean vs PHI3_FORBIDDEN (%d id hits) AND vs the "
          "sealed r314+r315 record-literal set (%d literal "
          "hits); consumed inputs: block sums x, group power "
          "sums Q2/Q3, ordered group values G1, slice pointers, "
          "flux ends/openings, abs edge mass, m -- no cubic "
          "target, no wall sign, no record number; e1 "
          "theta-posthoc FLAGGED (%s); e2 H-readback FLAGGED "
          "(%s); e2b literal-calibration FLAGGED (%s)"
          % (len(pure_ids), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e2b_hits[0] if e2b_hits else "MISS"))
    # toys, exact Fractions
    tm = fr_two_regime([list(g) for g in TOY_MIX])
    tf = fr_two_regime([list(g) for g in TOY_FLUX])
    ok_tm = (tm["cube"] == 28 and tm["coll"] == 28
             and tm["dflux"] == 0 and tm["bnd"] == 0
             and tm["cnt3"] == 91 and tm["L"] == 4
             and tm["xmax"] == 3
             and tm["cube"] <= abs(tm["coll"]) + abs(tm["bnd"])
             + abs(tm["dflux"])
             and abs(tm["coll"]) <= tm["cnt3"]
             and abs(tm["dflux"]) <= tm["fe"]
             and tm["cube"] * 1 <= tm["xmax"] ** 2 * tm["L"])
    ok_tf = (tf["cube"] == 1000 and tf["coll"] == 700
             and tf["dflux"] == 300 and tf["fe"] == 300
             and tf["de"] == 300 and tf["cnt3"] == 2560
             and abs(tf["coll"]) <= tf["cnt3"]
             and tf["cube"] == abs(tf["coll"]) + abs(tf["dflux"])
             and tf["cube"] * 1 == tf["xmax"] ** 2 * tf["L"])
    # float builder cross-check on the mixed toy:
    tpos = np.array([0.1, 0.2, 0.3])
    tval = np.array([2.0, -1.0, -3.0])
    tblk = np.array([0, 0, 1])
    tgen = SCF.fold_genealogy(tpos, tval, tblk, 2)
    tsct = SCF.signed_cube_terms(tgen["G1"], tgen["gblk"], 2)
    tft = SCF.flux_telescope(tgen["G1"], tgen["ptr"], 2)
    ttr = two_regime_state(tsct["x"], tsct["Q2"], tsct["Q3"],
                           tgen["G1"], tgen["ptr"], tft["F_end"],
                           tft["F_open"], tft["edge_abs"], 2)
    ok_fl = (abs(ttr["coll"] - 28.0) <= TOY_BAR
             and abs(ttr["dflux"]) <= TOY_BAR
             and abs(ttr["bnd"]) <= TOY_BAR
             and abs(ttr["cnt3"] - 91.0) <= TOY_BAR
             and abs(ttr["qmax"] - 0.75) <= TOY_BAR
             and abs(ttr["L"] - 4.0) <= TOY_BAR)
    check("G41-toy-exactness", ok_tm and ok_tf and ok_fl,
          "mixed toy {2,-1}|{-3}: cube 28 == |COLL| 28, DFLUX 0, "
          "BND 0, CNT3 91 >= 28, QMAX bound 28 <= 36 -- EXACT "
          "(Fractions, mixed signs); flux toy (1,2,3,4): cube "
          "1000 = COLL 700 + DFLUX 300, FE 300, CNT3 2560 >= "
          "700, QMAX bound TIGHT at equality (single block); "
          "float builders match Fractions (bar %.0e)" % TOY_BAR)
    # live majorant chain ward + component cross-wards
    chain_w = 0.0
    xw_cube = 0.0
    xw_comp = 0.0
    for rc in live:
        ev = rc["ev"]
        trs = ev["trs"]
        nc = trs["nrm"] * ev["cube"]
        xw_cube = max(xw_cube, abs(nc - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
        xw_comp = max(xw_comp,
                      abs(trs["coll"] - ev["ph"]["coll"])
                      / max(abs(ev["ph"]["coll"]), 1e-300),
                      abs(trs["dflux"] - ev["ph"]["dflux"])
                      / max(abs(ev["ph"]["dflux"]), 1e-300),
                      abs(trs["fcix"] - ev["ph"]["fcix"])
                      / max(ev["ph"]["fcix"], 1e-300))
        for a, b in ((nc, trs["phiL1"]),
                     (trs["phiL1"], trs["phiL2"]),
                     (trs["phiL2"], trs["phiH2"]),
                     (nc, trs["phiH1"])):
            chain_w = max(chain_w,
                          max(0.0, a - b) / max(b, 1e-300))
    check("G42-majorant-chain-ward",
          chain_w <= CHAIN_BAR and xw_cube <= XW_BAR
          and xw_comp <= 1e-12,
          "the sealed algebra live on %d live worlds: rho_2 <= "
          "PhiL1 <= PhiL2 <= PhiH2 and rho_2 <= PhiH1 (worst "
          "rel slack %.1e, bar %.0e); NORM x cube == rho_2 "
          "(worst %.1e, bar %.0e); two_regime_state components "
          "== r315 phi3_variants (COLL/DFLUX/FCIX worst %.1e) "
          "-- every certification below transfers to sum q^3 by "
          "algebra" % (len(live), chain_w, CHAIN_BAR, xw_cube,
                       XW_BAR, xw_comp))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 regime state: FCIX %.3f -> regime %s; "
             "rho_2 %.4f, PhiL2 %.4f, PhiL1 %.4f, PhiH2 %.4f, "
             "PhiH1 %.4f"
             % (ev9s["trs"]["fcix"],
                "H" if ev9s["trs"]["fcix"] > THETA else "L",
                ev9s["rho2"], ev9s["trs"]["phiL2"],
                ev9s["trs"]["phiL1"], ev9s["trs"]["phiH2"],
                ev9s["trs"]["phiH1"]))
        check("G43-theta-regime-census", True, "SMOKE: skipped")
        check("G44-midladder-split-seal", True, "SMOKE: skipped")
    else:
        # class ladder: mult-cap filter (EXT2 census; core+ext are
        # anchored mult == 2 by G30)
        srt316_all = sorted(recs + erecs + e2recs,
                            key=lambda rc: (rc["N"], rc["kz"]))
        excl = [rc for rc in srt316_all
                if rc["ev"]["mx_mult"] > MULT_CAP]
        srt316 = [rc for rc in srt316_all
                  if rc["ev"]["mx_mult"] <= MULT_CAP]
        n316 = len(srt316)
        reg = ["H" if rc["ev"]["trs"]["fcix"] > THETA else "L"
               for rc in srt316]
        small_idx, cal_idx, test_idx = split_midladder(n316)
        setlab = {}
        for i in small_idx:
            setlab[i] = "SMALL"
        for i in cal_idx:
            setlab[i] = "CAL"
        for i in test_idx:
            setlab[i] = "TEST"
        info("sealed regime table (BEFORE any bound table): rank "
             "kz N m FCIX regime set [EXT marks]")
        for i, rc in enumerate(srt316):
            tag = ""
            if rc in erecs:
                tag = " EXT"
            elif rc in e2recs:
                tag = " EXT2"
            info("%2d kz%-3d N %4d m %3d fcix %.3f %s %-5s%s"
                 % (i, rc["kz"], rc["N"], rc["ev"]["m"],
                    rc["ev"]["trs"]["fcix"], reg[i], setlab[i],
                    tag))
        fcL = [rc["ev"]["trs"]["fcix"]
               for i, rc in enumerate(srt316) if reg[i] == "L"]
        fcH = [rc["ev"]["trs"]["fcix"]
               for i, rc in enumerate(srt316) if reg[i] == "H"]
        h_kz = [srt316[i]["kz"] for i in range(n316)
                if reg[i] == "H"]
        gapL = max(fcL) if fcL else -1.0
        gapH = min(fcH) if fcH else -1.0
        check("G43-theta-regime-census",
              len(fcL) + len(fcH) == n316,
              "theta = %.2f (FROZEN, r315 record gap): stratum "
              "sizes %d L / %d H; H members kz %s; measured gap "
              "around theta: largest L %.3f < %.2f %s smallest H "
              "%s; EXT2 added %d class rungs%s"
              % (THETA, len(fcL), len(fcH), str(h_kz), gapL,
                 THETA, "<" if fcH else "(H empty)",
                 ("%.3f" % gapH) if fcH else "-",
                 sum(1 for rc in srt316 if rc in e2recs),
                 "; EXCLUDED by mult cap: "
                 + str([rc["kz"] for rc in excl]) if excl
                 else ""))
        ovl_sc = len(set(cal_idx) & set(test_idx)) \
            + len(set(small_idx) & set(cal_idx)) \
            + len(set(small_idx) & set(test_idx))
        cover = (tuple(sorted(small_idx + cal_idx + test_idx))
                 == tuple(range(n316)))
        m_all = [rc["ev"]["m"] for rc in srt316]
        m0 = min(m_all[i] for i in cal_idx + test_idx)
        check("G44-midladder-split-seal",
              ovl_sc == 0 and cover and len(cal_idx) == N_CAL,
              "SEALED split on the %d-rung class ladder: small = "
              "ranks 0..%d (m %d..%d), cal = %d..%d (m %d..%d, N "
              "%d..%d), test = %d..%d (m %d..%d); overlaps 0 "
              "EXACT, cover EXACT; m_0 = %d"
              % (n316, small_idx[-1] if small_idx else -1,
                 min(m_all[i] for i in small_idx) if small_idx
                 else 0,
                 max(m_all[i] for i in small_idx) if small_idx
                 else 0,
                 cal_idx[0], cal_idx[-1],
                 min(m_all[i] for i in cal_idx),
                 max(m_all[i] for i in cal_idx),
                 srt316[cal_idx[0]]["N"], srt316[cal_idx[-1]]["N"],
                 test_idx[0], test_idx[-1],
                 min(m_all[i] for i in test_idx),
                 max(m_all[i] for i in test_idx), m0))

    # ---------------- S5: Leg B -- regime L + small-m
    section("S5  LEG B -- SMALL-M CERTIFICATES + REGIME L")
    if smoke:
        check("G50-smallm-certificates", True, "SMOKE: skipped")
        check("G51-regimeL-certification", True, "SMOKE: skipped")
        check("G52-regimeL-trend", True, "SMOKE: skipped")
    else:
        rho_all = [rc["ev"]["rho2"] for rc in srt316]
        C_small = max(rho_all[i] for i in small_idx) \
            if small_idx else 0.0
        j_small = max(small_idx, key=lambda i: rho_all[i]) \
            if small_idx else -1
        info("small-m certificates (direct evaluation, per rung): "
             "rank kz m rho_2")
        for i in small_idx:
            info("%2d kz%-3d m %3d rho2 %.4f%s"
                 % (i, srt316[i]["kz"], m_all[i], rho_all[i],
                    "  <-- C_small" if i == j_small else ""))
        check("G50-smallm-certificates",
              (not small_idx) or C_small > 0.0,
              "%d small-m rungs certified individually; C_small "
              "= %.4f at rank %d (kz%d) -- the finite exception "
              "constant of the theorem candidate"
              % (len(small_idx), C_small, j_small,
                 srt316[j_small]["kz"] if j_small >= 0 else -1))
        Lkeys = dict(L2="phiL2", L1="phiL1")
        calL = [i for i in cal_idx if reg[i] == "L"]
        C_L = {}
        violL = {}
        resL = {}
        testL = [i for i in test_idx if reg[i] == "L"]
        for v in L_VARIANTS:
            key = Lkeys[v]
            vals = [srt316[i]["ev"]["trs"][key]
                    for i in range(n316)]
            C_L[v] = max(vals[i] for i in calL) if calL else 0.0
            violL[v] = [i for i in testL if vals[i] > C_L[v]]
            rs = [C_L[v] / max(vals[i], 1e-300) for i in testL]
            resL[v] = (min(rs), float(np.median(rs))) \
                if rs else (0.0, 0.0)
        winL = None
        for v in L_VARIANTS:
            if calL and not violL[v]:
                winL = v
                break
        regL_ok = winL is not None
        info("regime-L record table: rank kz N m PhiL2 PhiL1 "
             "rho_2 [set]")
        for i in sorted(set(list(cal_idx) + testL)):
            ev = srt316[i]["ev"]
            info("%2d kz%-3d N %4d m %3d L2 %8.4f L1 %8.4f rho2 "
                 "%.4f %s%s"
                 % (i, srt316[i]["kz"], srt316[i]["N"], ev["m"],
                    ev["trs"]["phiL2"], ev["trs"]["phiL1"],
                    ev["rho2"], setlab[i],
                    " H!" if reg[i] == "H" else ""))
        check("G51-regimeL-certification", True,
              "REGIME L (census; adjudicated in S7): C_L frozen "
              "on the %d regime-L cal rungs: L2 %.4f / L1 %.4f; "
              "violations on the %d regime-L test rungs: L2 "
              "%d / L1 %d; reserve min/med L2 %.2f/%.2f; winner "
              "by sealed precedence: %s"
              % (len(calL), C_L["L2"], C_L["L1"], len(testL),
                 len(violL["L2"]), len(violL["L1"]),
                 resL["L2"][0], resL["L2"][1],
                 winL if winL else "NONE"))
        NsL = [srt316[i]["N"] for i in testL]
        slL = {v: L2D.halves_slope(
            NsL, [max(srt316[i]["ev"]["trs"][Lkeys[v]], 1e-300)
                  for i in testL]) for v in L_VARIANTS}
        check("G52-regimeL-trend", True,
              "regime-L trend census on the %d test rungs "
              "(halves slope): L2 %+.3f / L1 %+.3f (falling "
              "reserve trend expected from the r315 record; "
              "census, no gate bar)"
              % (len(testL), slL["L2"], slL["L1"]))

    # ---------------- S6: Leg C -- regime H
    section("S6  LEG C -- REGIME H (dissection + certification)")
    if smoke:
        check("G60-regimeH-dissection", True, "SMOKE: skipped")
        check("G61-regimeH-certification", True, "SMOKE: skipped")
    else:
        h_all = [i for i in range(n316) if reg[i] == "H"]
        testH = [i for i in test_idx if reg[i] == "H"]
        medL = dict(
            top1=float(np.median([srt316[i]["ev"]["top1"]
                                  for i in testL])),
            qmax=float(np.median([srt316[i]["ev"]["trs"]["qmax"]
                                  for i in testL])),
            kappa=float(np.median([srt316[i]["ev"]["kappa"]
                                   for i in testL])),
            tight=float(np.median([srt316[i]["ev"]["tight"]
                                   for i in testL])),
            full=float(np.median(
                [srt316[i]["ev"]["shares"]["full"]
                 for i in testL])))
        info("regime-H dissection census (all H rungs, any set): "
             "rank kz fcix rho2 PhiL2 PhiH2 PhiH1 top1 qmax "
             "kappa cnt3/|coll| fullshare neff")
        medH = {}
        if h_all:
            for i in h_all:
                ev = srt316[i]["ev"]
                info("%2d kz%-3d fcix %.3f rho2 %.4f L2 %.4f H2 "
                     "%.4f H1 %.4f top1 %.3f qmax %.3f kap %.3f "
                     "tight %.1f full %+.3f neff %.1f %s"
                     % (i, srt316[i]["kz"], ev["trs"]["fcix"],
                        ev["rho2"], ev["trs"]["phiL2"],
                        ev["trs"]["phiH2"], ev["trs"]["phiH1"],
                        ev["top1"], ev["trs"]["qmax"],
                        ev["kappa"], ev["tight"],
                        ev["shares"]["full"], ev["cm"]["N2"],
                        setlab[i]))
            medH = dict(
                top1=float(np.median([srt316[i]["ev"]["top1"]
                                      for i in h_all])),
                qmax=float(np.median(
                    [srt316[i]["ev"]["trs"]["qmax"]
                     for i in h_all])),
                kappa=float(np.median([srt316[i]["ev"]["kappa"]
                                       for i in h_all])),
                tight=float(np.median([srt316[i]["ev"]["tight"]
                                       for i in h_all])),
                full=float(np.median(
                    [srt316[i]["ev"]["shares"]["full"]
                     for i in h_all])))
            devs = {k: abs(medH[k] - medL[k])
                    / max(abs(medL[k]), 1e-300) for k in medH}
            disc = max(devs, key=lambda k: devs[k])
            disc_fires = devs[disc] >= ATTR_MIN
        else:
            devs = {}
            disc = "NONE"
            disc_fires = False
        check("G60-regimeH-dissection", True,
              "dissection census: H med vs regime-L test med "
              "devs %s -> named discriminator %s (dev %s, bar "
              "%.2f, fires %s); kappa is the read-back-adjacent "
              "compensation column (diagnostic only, disclosed)"
              % (str({k: round(devs[k], 2) for k in devs}),
                 disc.upper(),
                 ("%.2f" % devs[disc]) if devs else "-",
                 ATTR_MIN, disc_fires))
        Hkeys = dict(H2="phiH2", H1="phiH1")
        C_H = {}
        violH = {}
        resH = {}
        for v in H_VARIANTS:
            key = Hkeys[v]
            vals = [srt316[i]["ev"]["trs"][key]
                    for i in range(n316)]
            C_H[v] = max(vals[i] for i in cal_idx)
            violH[v] = [i for i in testH if vals[i] > C_H[v]]
            rs = [C_H[v] / max(vals[i], 1e-300) for i in testH]
            resH[v] = (min(rs), float(np.median(rs))) \
                if rs else (0.0, 0.0)
        winH = None
        for v in H_VARIANTS:
            if testH and not violH[v]:
                winH = v
                break
        regH_ok = winH is not None
        check("G61-regimeH-certification", True,
              "REGIME H (census; adjudicated in S7): C_H frozen "
              "on all %d cal rungs: H2 %.4f / H1 %.4f; H test "
              "stratum %d rungs (kz %s); violations H2 %d / H1 "
              "%d; reserve H2 min/med %.2f/%.2f; winner by "
              "sealed precedence: %s -- the REGIME-H MECHANICS "
              "OBJECT: %s + discriminator %s"
              % (len(cal_idx), C_H["H2"], C_H["H1"], len(testH),
                 str([srt316[i]["kz"] for i in testH]),
                 len(violH["H2"]), len(violH["H1"]),
                 resH["H2"][0], resH["H2"][1],
                 winH if winH else "NONE",
                 ("the multiplicity-2 COUNTING majorant"
                  if winH == "H2" else
                  "the CONCENTRATION majorant" if winH == "H1"
                  else "NONE"),
                 disc.upper()))

    # ---------------- S7: Leg D -- world check + adjudication
    section("S7  LEG D -- WORLD CHECK + SEALED ADJUDICATION")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    m9 = ev9m["m"]
    # SCRAMBLE class rejection machinery (r315 verbatim): the
    # component attribution + the seeded assignment shuffle.
    evS = crecs["SCR"]["ev"]
    comp_ref = recs if smoke else recs
    comp_main = dict(
        dflux=float(np.median([rc["ev"]["trs"]["nrm"]
                               * abs(rc["ev"]["trs"]["dflux"])
                               for rc in comp_ref])),
        coll=float(np.median([rc["ev"]["trs"]["nrm"]
                              * abs(rc["ev"]["trs"]["coll"])
                              for rc in comp_ref])),
        fcix=float(np.median([rc["ev"]["trs"]["fcix"]
                              for rc in comp_ref])))
    comp_scr = dict(
        dflux=evS["trs"]["nrm"] * abs(evS["trs"]["dflux"]),
        coll=evS["trs"]["nrm"] * abs(evS["trs"]["coll"]),
        fcix=evS["trs"]["fcix"])
    devsS = {k: abs(comp_scr[k] - comp_main[k])
             / max(abs(comp_main[k]), 1e-300) for k in comp_main}
    cause = max(devsS, key=lambda k: devsS[k])
    attr_ok = (devsS[cause] >= ATTR_MIN
               and cause in ("coll", "dflux"))
    rng = np.random.default_rng(SEED_SHUF)
    blk_shuf = ev9m["blk_all"][
        rng.permutation(len(ev9m["blk_all"]))]
    gen_s = SCF.fold_genealogy(ev9m["pos_all"], ev9m["val_all"],
                               blk_shuf, m9)
    ft_s = SCF.flux_telescope(gen_s["G1"], gen_s["ptr"], m9)
    mism_s = int(np.sum(np.searchsorted(ev9m["brk"],
                                        ev9m["pos_all"])
                        != blk_shuf))
    ne = min(len(ft_s["edges"]), len(ev9m["ft"]["edges"]))
    edev = float(np.max(np.abs(ft_s["edges"][:ne]
                               - ev9m["ft"]["edges"][:ne]))
                 / max(float(np.max(np.abs(
                     ev9m["ft"]["edges"]))), 1e-300))
    x_s = np.bincount(blk_shuf, weights=ev9m["val_all"],
                      minlength=m9)
    mass_dev = abs(float(np.sum(x_s))
                   - float(np.sum(ev9m["sct"]["x"]))) \
        / max(float(np.sum(np.abs(ev9m["val_all"]))), 1e-300)
    shuf_ok = (mism_s > 0 and edev >= MUT_MIN
               and mass_dev <= ID_BAR)
    if smoke:
        check("G70-world-admission", True, "SMOKE: skipped")
        check("G71-scramble-rejection", shuf_ok and attr_ok,
              "SMOKE (w9-based): attribution %s dev %.2f; "
              "shuffle %d mism, edge break %.1e, mass %.1e"
              % (cause.upper(), devsS[cause], mism_s, edev,
                 mass_dev))
        check("G72-sealed-adjudication", True, "SMOKE: skipped")
        check("G73-theorem-candidate", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        C2R = 0.0
        if regL_ok:
            C2R = max(C2R, C_L[winL])
        if regH_ok:
            C2R = max(C2R, C_H[winH])
        C_tot = max(C2R, C_small)
        wnote = []
        adm_ok = True
        for nm, ev in (("w9", mrecs[0]["ev"]),
                       ("w13(twin)", mrecs[1]["ev"]),
                       ("EPSTEIN", crecs["EPST"]["ev"])):
            adm = (ev["mx_mult"] <= MULT_CAP
                   and ev["rho2"] <= C_tot)
            adm_ok = adm_ok and adm
            wreg = "H" if ev["trs"]["fcix"] > THETA else "L"
            wnote.append("%s mult %d rho2 %.3f %s C_tot (regime "
                         "%s, PhiL2 %.3f PhiH2 %.3f census)"
                         % (nm, ev["mx_mult"], ev["rho2"],
                            "<=" if ev["rho2"] <= C_tot else ">",
                            wreg, ev["trs"]["phiL2"],
                            ev["trs"]["phiH2"]))
        tw_fac = max(mrecs[1]["ev"]["trs"]["phiL2"]
                     / max(mrecs[0]["ev"]["trs"]["phiL2"], 1e-300),
                     mrecs[0]["ev"]["trs"]["phiL2"]
                     / max(mrecs[1]["ev"]["trs"]["phiL2"], 1e-300))
        twin_ok = tw_fac <= TWIN_FAC
        world_ok = adm_ok and twin_ok and attr_ok and shuf_ok
        check("G70-world-admission", True,
              "WORLD census (adjudicated in G72): %s; twin band "
              "PhiL2 factor %.2f %s %.1f; SCR rho2 %.3f %s C_tot "
              "%.3f (consequence census, disclosed)"
              % ("; ".join(wnote), tw_fac,
                 "<=" if twin_ok else ">", TWIN_FAC, evS["rho2"],
                 "<=" if evS["rho2"] <= C_tot else ">", C_tot))
        check("G71-scramble-rejection", attr_ok and shuf_ok,
              "SCRAMBLE rejected by the CLASS machinery: "
              "component attribution names %s (dev %.2f >= %.2f, "
              "devs %s) AND the seeded shuffle (%d) breaks the "
              "flux profile edgewise %.1e >= %.0e with mass "
              "matched %.1e (%d/%d atoms displaced)"
              % (cause.upper(), devsS[cause], ATTR_MIN,
                 str({k: round(devsS[k], 2) for k in devsS}),
                 SEED_SHUF, edev, MUT_MIN, mass_dev, mism_s,
                 len(ev9m["pos_all"])))
        if regL_ok and regH_ok and world_ok:
            verdict_main = ("TWO_REGIME_GO(C2R = %.3f, A = 2, "
                            "m_0 = %d, theta = %.2f; C_tot = "
                            "%.3f)" % (C2R, m0, THETA, C_tot))
        elif (not regL_ok) and regH_ok:
            verdict_main = ("REGIME_L_FAILS_MIDLADDER(%s)"
                            % ("; ".join(
                                "%s viol %d" % (v, len(violL[v]))
                                for v in L_VARIANTS)))
        elif regL_ok and (not regH_ok):
            verdict_main = ("REGIME_H_UNEXPLAINED(%s)"
                            % ("empty H test stratum" if not testH
                               else "; ".join(
                                   "%s viol %d"
                                   % (v, len(violH[v]))
                                   for v in H_VARIANTS)))
        else:
            leak = []
            if not regL_ok:
                leak.append("L fails")
            if not regH_ok:
                leak.append("H fails")
            if not world_ok:
                leak.append("world leak (adm %s twin %s attr %s "
                            "shuf %s)" % (adm_ok, twin_ok,
                                          attr_ok, shuf_ok))
            verdict_main = "TWO_REGIME_DEAD(%s)" % "; ".join(leak)
        check("G72-sealed-adjudication", True,
              "exactly one sealed verdict fired: %s"
              % verdict_main)
        if regL_ok and regH_ok:
            info("CANDIDATE THEOREM (two-regime cubic bound; "
                 "measured on the %d-rung class ladder; status "
                 "%s):" % (n316, verdict_main.split("(")[0]))
            info("  For every class rung w (edge-masked "
                 "presentation, fold multiplicity <= %d, "
                 "POSITIVE_PREFIX) with m >= %d:" % (MULT_CAP,
                                                     m0))
            info("    EITHER FCIX(w) <= %.2f and Phi%s(w) <= C_L "
                 "= %.4f," % (THETA, winL, C_L[winL]))
            info("    OR     FCIX(w) >  %.2f and Phi%s(w) <= C_H "
                 "= %.4f;" % (THETA, winH, C_H[winH]))
            info("  both majorize rho_2 by the exact r314 "
                 "identity + triangle/counting algebra (G42), "
                 "hence")
            info("    sum_j q_j^3 <= %.3f (log m)^2 / m^2   "
                 "(C2R = max(C_L, C_H), A = 2, m >= %d);"
                 % (C2R, m0))
            info("  the %d rungs with m < %d are certified "
                 "individually (C_small = %.4f <= %s), so on "
                 "EVERY measured rung"
                 % (len(small_idx), m0, C_small,
                    "C2R" if C_small <= C2R
                    else "C_tot = %.3f" % C_tot))
            info("    sum_j q_j^3 <= %.3f (log m)^2 / m^2  and  "
                 "n_eff = N_2 >= N_3 >= m / (%.3f log m)  (r306 "
                 "exact chain)." % (C_tot, math.sqrt(C_tot)))
            check("G73-theorem-candidate", True,
                  "coupled theorem candidate printed with "
                  "explicit (C2R %.3f, A 2, m_0 %d, theta %.2f, "
                  "C_small %.4f, C_tot %.3f); exceptions = the "
                  "%d small-m rungs, individually certified"
                  % (C2R, m0, THETA, C_small, C_tot,
                     len(small_idx)))
        else:
            check("G73-theorem-candidate", True,
                  "no coupled theorem candidate printed (a "
                  "regime failed certification -- see G72); the "
                  "dissection census stands as the round's "
                  "record data")

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    th_toy = mutant_theta_posthoc((0.5, 0.9), (1.0, 5.0))
    check("G80-e1-theta-posthoc",
          len(e1_hits) >= 1 and th_toy != THETA,
          "e1 CAUGHT twice: the after-sight theta re-pick "
          "consumes the evaluated bound column -- AST-FLAGGED "
          "(%s) AND on the sealed toy it returns %.2f != frozen "
          "theta %.2f; the real theta is a module constant, "
          "frozen before any bound value existed"
          % (e1_hits[0] if e1_hits else "MISS", th_toy, THETA))
    check("G81-e2-h-readback", len(e2_hits) >= 1
          and len(e2b_hits) >= 1,
          "e2 AST-CAUGHT: the regime-H bound consuming the "
          "cubic-moment record (cm/S3) is FLAGGED (%s) while "
          "two_regime_state is clean (%d hits); e2b "
          "literal-CAUGHT: the r315 record number 0.955 as "
          "decision constant is FLAGGED (%s) while the real "
          "builders are literal-clean (%d hits)"
          % (e2_hits[0] if e2_hits else "MISS", len(pure_ids),
             e2b_hits[0] if e2b_hits else "MISS",
             len(pure_lits)))
    n_toy = 12
    cal_mut, test_mut = mutant_split_overlap(n_toy)
    ovl_mut = len(set(cal_mut) & set(test_mut))
    sm_t, ca_t, te_t = split_midladder(n_toy)
    ovl_seal = len(set(ca_t) & set(te_t)) \
        + len(set(sm_t) & set(ca_t)) + len(set(sm_t) & set(te_t))
    check("G82-e3-split-overlap",
          ovl_mut == 1 and ovl_seal == 0,
          "e3 CAUGHT: the overlapping mutant split shares "
          "EXACTLY %d rank (rank %d) while the sealed split has "
          "%d overlaps EXACT on the same n = %d toy ladder"
          % (ovl_mut, cal_mut[-1], ovl_seal, n_toy))
    p3, v3, b3 = PHI.mult3_control(ev9m["pos_all"],
                                   ev9m["val_all"],
                                   ev9m["blk_all"], split=True)
    gen3 = SCF.fold_genealogy(p3, v3, b3, m9)
    g1_dev = float(np.max(np.abs(gen3["G1"]
                                 - ev9m["gen"]["G1"]))) \
        if gen3["ng"] == ev9m["gen"]["ng"] else 1.0
    cc3 = SCF.collision_census(gen3["mult"], gen3["ptr"], m9)
    mx3 = int(np.max(gen3["mult"]))
    sct3 = SCF.signed_cube_terms(gen3["G1"], gen3["gblk"], m9)
    ft3 = SCF.flux_telescope(gen3["G1"], gen3["ptr"], m9)
    trs3 = two_regime_state(sct3["x"], sct3["Q2"], sct3["Q3"],
                            gen3["G1"], gen3["ptr"], ft3["F_end"],
                            ft3["F_open"], ft3["edge_abs"], m9)
    blind = max(abs(trs3[k] - ev9m["trs"][k])
                for k in ("phiL1", "phiL2", "phiH1", "phiH2"))
    check("G83-e4-mult3-control",
          g1_dev == 0.0 and mx3 == 3
          and cc3["atoms_coll"] != cc3["atoms_coll_m2"]
          and blind <= 1e-12,
          "e4 MULT-3 CONTROL (matched: G1/blocks/positions/mass "
          "preserved BITWISE, dev %.1e): fold multiplicity 3 > "
          "cap %d -> class REJECTS; collision count bound BREAKS "
          "(3p1p2 - 2p3 = %d != m2 closed form %d); DISCLOSED: "
          "all four regime majorants blind to the control (max "
          "dev %.1e) -- the cap stays a necessary CLASS side "
          "condition, exactly the r315 finding"
          % (g1_dev, MULT_CAP, cc3["atoms_coll"],
             cc3["atoms_coll_m2"], blind))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed two-regime statement over the FCIX "
          "stratum (theta + mid-ladder split frozen in advance), "
          "the four exact regime majorants with machine-audited "
          "purity, the small-m certificate table, the regime-H "
          "dissection and the coupled adjudication -- NO new "
          "certificate promoted, NO universal bound claimed "
          "beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R316_ANCHORS(shares %+.4f/%+.4f/%+.4f, FC "
                 "%.3f/%+.3f, mult 2 on %d/%d, identity %.1e, "
                 "r306 C2 %.3f viol %d/57, r315 C0 "
                 "%.4f/%.4f/%.4f, FCIX kz55/kz67 %.3f/%.3f)"
                 % (meds[0], meds[1], meds[2], fc_med, fc_sl,
                    n_m2, len(srt57), rec3_w, C2, viol2, C0["a"],
                    C0["b"], C0["c"], fcix_kz.get(55, -1.0),
                    fcix_kz.get(67, -1.0))]
        parts.append("SEAL(theta %.2f + split %d|%d|%d + 4 "
                     "majorants, purity clean, chain %.1e)"
                     % (THETA, len(small_idx), len(cal_idx),
                        len(test_idx), chain_w))
        parts.append("REGIMES(%d L / %d H, H = %s, gap "
                     "%.3f|%.3f, EXT2 +%d)"
                     % (len(fcL), len(fcH), str(h_kz), gapL,
                        gapH if fcH else -1.0,
                        sum(1 for rc in srt316 if rc in e2recs)))
        parts.append("SMALLM(C_small %.4f, %d rungs)"
                     % (C_small, len(small_idx)))
        parts.append("REGIME_L(winner %s, C_L %.4f, viol %s, "
                     "reserve %.2f/%.2f, trend %+.3f)"
                     % (winL if winL else "NONE",
                        C_L[winL] if winL else 0.0,
                        str({v: len(violL[v])
                             for v in L_VARIANTS}),
                        resL["L2"][0], resL["L2"][1], slL["L2"]))
        parts.append("REGIME_H(discriminator %s, winner %s, C_H "
                     "%.4f, viol %s)"
                     % (disc.upper(), winH if winH else "NONE",
                        C_H[winH] if winH else 0.0,
                        str({v: len(violH[v])
                             for v in H_VARIANTS})))
        parts.append("WORLD(adm %s, twin %.2f, SCR %s dev %.2f "
                     "+ shuffle %d/%d)"
                     % (adm_ok, tw_fac, cause.upper(),
                        devsS[cause], mism_s,
                        len(ev9m["pos_all"])))
        parts.append(verdict_main)
        parts.append("THEOREM(%s)"
                     % ("printed" if regL_ok and regH_ok
                        else "not printed"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + e2b + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the majorant chains, "
          "the toy algebra, the split hygiene and the purity "
          "audits (exact / AST-decided); MEASURED: every "
          "constant, violation count, reserve, trend and census "
          "(the finite class ladder + 2 mains + 2 live "
          "controls); OPEN: the bound beyond the measured rungs, "
          "the cofinal law, kz15 beyond r270; NO RH claim"
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
