#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""continuous_coordinate_probe -- PRIME.L2.RENYI3.CONTINUOUS_COORDINATE.01
(round 321): THE CONTINUOUS-COORDINATE ROUND -- reviewer fork (a)
in the r317-sharpened form: bound rho_2 BY the single source-pure
concentration coordinate, do NOT classify by threshold.  The r317
fallback fired (WHAC_A_MOLE: the near-critical family is a
CONTINUUM, threshold classification swallows harmless rungs or
leaves kz53/kz83 uncovered), and the r317 census delivered the
sharpened form: the rank-local QMAX ratio F_A -- ONE source-pure
coordinate, computable in advance -- ranks the COMPLETE mid/deep
near-critical family on top (top-3 EXACTLY kz53 2.47 / kz83 2.39 /
kz67 2.38, refuting the r316 conjecture that kz53 needs a second
coordinate), with a continuum below (1.93, 1.90, 1.74, ...).  THE
ONE QUESTION OF THIS ROUND: does an explicit MONOTONE function g
exist with rho_2(w) <= g(F_A(w)) pointwise on ALL rungs
(mid-ladder calibrated, sealed), so that g(F_A) x (log m)^2 / m^2
is the new SLIDING uniform Renyi-3 bound -- no regimes, no
exception families, one gliding bound -- and is the coordinate
bound world-correct (twin/EPSTEIN admitted, SCRAMBLE breaks or
stays class-rejected, honestly documented which mechanism fires)?
Context (sealed record inputs): r306 (SPEC 3bb365e1) fixed sum q^3
<= 1.069 (log m)^2/m^2 pointwise 0/57 (first-5 constant,
r316-rehabilitated as load-bearing); r316 (SPEC 5c28b12b) sealed
TWO_REGIME_DEAD and the violator anatomy (kz53 rho_2 1.0493 at
bulk-normal FCIX, kz83 0.7791, kz55/kz67 the divergence-mass
spikes; C_gen 0.4579 mid-ladder; C_small 1.0694; 21 small-m
certificates; complement rest trend -0.170); r317 (SPEC 04fbe5c0)
sealed WHAC_A_MOLE and delivered F_A (rank-local QMAX spike ratio,
window W = 5) with the top-3 ranking above.  kz15 permanently
closed via r270; the 6 exceptions via the r287 F2 certificates.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: r318 (base fork) and r320 (Lean repair) run in
parallel; this probe touches NOTHING outside its own file and the
strictly additive rh-sync.

THE OBJECT (r269/r287/r298/r306/r314/r315/r316/r317 machinery
imported verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266
eval); F = 0.20 edge split; maximal same-sign runs of the
bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298 WBT.block_breaks +
WBT.aggregate_blocks); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope + SCF.collision_census;
the r315 PHI.phi3_variants; the r316 TRB.two_regime_state +
TRB.split_midladder; the r317 EFP.local_ratio + EFP.gap_threshold,
ALL imported verbatim; PDelta = Pbeta - Pomega; x_j = (PDelta)_j.
NEW in this round (module-own, source-pure where required): the
rank-local median companion (local_median, the B-side baseline
column), the sealed monotone g-family evaluator + calibrator, the
sealed monotonicity grid check, the fit-free upper-envelope
builder with declared-set ward, the rank correlation, the
insertion-rule world coordinate and the sealed verdict tree.

THE SEALED COORDINATE (r317 verbatim, frozen): on the (N, kz)-
sorted class ladder of n rungs (42 core + 15 r286 extension + the
8 EXT2 anchors, multiplicity cap <= 2, POSITIVE_PREFIX), with
QMAX(i) = max_j |x_j| / L the sealed r316 column (source-pure by
the r316/r317 audits),
    F_A(i) = QMAX(i) / med{ QMAX(j) : |j - i| <= W, j != i },
rank-local ratio with half-width W = CLS_W = 5 (truncated at the
ladder ends), computed by the IMPORTED r317 builder
EFP.local_ratio -- no redefinition.  The companion baseline
    medloc(i) = med{ QMAX(j) : |j - i| <= W, j != i }
is computed by the module-own local_median (window verbatim) and
warded EXACT against the import: QMAX == F_A x medloc.

THE EXACT CONCENTRATION BRACKET (derived algebra, disclosed, no
measurement): with L = sum |x_j|, qmax = QMAX, rho_2 = NORM x
sum |x|^3 (NORM = m^2/((log m)^2 L^3), the r306 scale) and PhiH1 =
(m qmax / log m)^2 (the r316 concentration majorant):
    qmax^3 L^3 <= sum |x|^3 <= qmax^2 L^2 x sum |x| = qmax^2 L^3
  =>  qmax x PhiH1  <=  rho_2  <=  PhiH1,
a TWO-SIDED bracket: high F_A forces the QMAX share up and rho_2
is pinched between qmax x PhiH1 and PhiH1 -- exactly the r317
"B-certificate spirit" chain (near-one-block => QMAX high => sum
q^3 within an explicit factor of qmax^3).  Substituting qmax =
F_A x medloc gives PhiH1 == (F_A x B)^2 EXACT with
    B(i) = medloc(i) x m_i / log m_i
-- the rank-local BASELINE SCALE, source-pure (consumes the QMAX
column + rank order + m only), robust against spikes (a spike
moves F_A, not the local median).  THE UPPER DIRECTION OF THE
BRACKET IS CARRIED BY B: rho_2 <= F_A^2 x B^2 by exact algebra --
whether B is mid-ladder bounded is precisely the measurable
transfer question of Leg C, and it is a SOURCE-PURE question.
Both bracket sides and the PhiH1 == (F_A B)^2 identity are warded
live on every live world (CHAIN_BAR).

THE SEALED g-FAMILY (frozen BEFORE any evaluation of this round;
2-3 forms as the fork-(a) contract demands; every form MONOTONE
non-decreasing on F > 0 by construction, checked on the sealed
grid; constants frozen on the r316 mid-ladder calibration window
by the sealed rules below; precedence sealed by DERIVATION
STRENGTH, not by data):
  G_SQ  (STRUCTURAL QUADRATIC, precedence 1 -- derived from the
        exact bracket, not from data):  g(F) = b x F^2  with
        b = (max over CAL of B(i))^2.  By the exact bracket,
        rho_2 <= F_A^2 B^2 <= b F_A^2 holds on every rung whose
        baseline B stays below its calibration maximum -- the
        certification measures EXACTLY the source-pure
        boundedness of B (Leg C's question), and the calibration
        consumes NO target value at all (source-pure column only).
  G_TT  (TWO-TERM CUBIC, precedence 2 -- the r317-named reading
        form C_1 + C_2 F^gamma with gamma = 3 from the
        concentration heuristic: a spike of factor F in QMAX at
        fixed baseline inflates the cube-dominant term like F^3):
        g(F) = c_1 + c_2 x F^3 with c_1 = median of rho_2 over
        CAL (the generic bulk level) and c_2 = max over CAL of
        (rho_2 - c_1)_+ / F^3 (monotone since c_2 >= 0).
  G_LIN (MINIMAL FALLBACK, precedence 3): g(F) = a x F with
        a = max over CAL of rho_2 / F.
THE SEALED CALIBRATION SPLIT: TRB.split_midladder on the full
(N, kz)-sorted class ladder, VERBATIM (n = 65 expected: small =
ranks 0..20 certified individually, cal = ranks 21..25 frozen,
test = ranks 26..64); m_0 = min m over cal + test; the declared
calibration index set is warded EXACT (e1/e3 prove the wards
bite).  MONOTONICITY: every calibrated form must be non-
decreasing on the sealed grid GRID_MONO = 0.25, 0.50, ..., 3.25
(covers the measured F_A range [~0.5, 2.47] with margin); a
decrease > TOY_BAR disqualifies the form (and the e4 mutant is
LOUD).  CERTIFICATION (per form, sealed): violations = test rungs
with rho_2 > g(F_A); the form certifies iff 0 test violations AND
the four named r316/r317 violators kz53/kz83/kz67/kz55 are ALL
pointwise inside rho_2 <= g(F_A) (kz55 sits in the small-m set --
its coverage is demanded EXTRA, because covering the old
violators is the point of the sliding bound); the WINNER is the
first certifying form in the sealed precedence.  Reserve
distribution min/med and the halves-slope trend of rho_2/g(F_A)
over the test rungs are printed as census.

THE SEALED MAP + ENVELOPE RULE (Leg A): the (rho_2, F_A) map over
the full ladder; Spearman rank correlation (fit-free: Pearson on
stable rank vectors) over the TEST rungs printed as census; the
fit-free UPPER ENVELOPE over NB_ENV = 6 equal-count F_A-rank bins
computed on EXACTLY the declared TEST set (evaluating it on the
calibration split is the e3 mutant -- declared-set ward EXACT):
env_j = max rho_2 in bin j.  ENV_OK iff the top-F_A bin carries
the envelope maximum (argmax j == NB_ENV - 1) AND the Spearman
correlation of (bin index, env_j) >= ENV_RC_MIN = 0.5 -- the
upper envelope RISES with the coordinate.  NON-TRIVIALITY (the
coordinate must CARRY, the bound must not be a disguised flat
constant): GAIN = g*(max F_A over the ladder) / g*(min F_A over
the test rungs) >= GAIN_MIN = 1.5.

THE SEALED ADJUDICATION (frozen BEFORE evaluation; exactly one
fires):
    no winner:  ENVELOPE_DIFFUSE   iff NOT ENV_OK (the envelope
                    itself is diffuse -- the coordinate does not
                    carry; the primary diagnosis),
                G_FAILS_POINTWISE  iff ENV_OK (the envelope is
                    monotone but every sealed g form misses --
                    the family was wrong, not the coordinate);
    winner g*:  WORLD_LEAK         iff the world check leaks,
                ENVELOPE_DIFFUSE   iff NOT ENV_OK or GAIN <
                    GAIN_MIN (a bound exists but is effectively
                    flat/diffuse -- honest demotion),
                SLIDING_BOUND_GO(g*) otherwise.
WORLD CHECK (r316/r317 machinery verbatim, adapted to the sliding
bound): (w1) w9/w13/EPSTEIN ADMITTED -- fold multiplicity <= 2
AND rho_2 <= g*(F_A) at the world's coordinate (the sealed
INSERTION RULE for world coordinates: the world's QMAX against
the rank-local median of the ladder QMAX column at the world's
(N)-insertion point, window W ladder ranks each side, no self-
exclusion -- worlds are not ladder members; disclosed: for the
mains this differs from their ladder F_A by the self-exclusion
convention, both printed); (w2) twin band max(w13/w9, w9/w13) <=
TWIN_FAC = 3.0 on PhiL2; (w3) SCRAMBLE is rejected by EITHER
mechanism -- the coordinate bound BREAKS (rho_2 > g*(F_A), the
sliding-bound-native rejection) OR the r317 class machinery
rejects it (component attribution names a collision/flux column,
dev >= ATTR_MIN = 0.25, AND the seeded assignment shuffle
SEED_SHUF = 321001 breaks the flux profile edgewise >= MUT_MIN
with matched mass) -- WHICH mechanism fires is printed honestly;
scr_ok = coordinate break OR class rejection.

LEG 0 -- ANCHOR REGRESSION (r314/r315/r306/r316/r317 record
numbers adopted as-is, disclosed): med signed shares DeltaF/
C_pair/C_full = -0.4226/+0.5980/+0.8537 (tol 0.005); FC med 0.629
(tol 0.005) slope -0.141 (tol 0.01); fold multiplicity == 2
UNIFORM; identity wards live; r306 C_2 = 1.069 (tol 0.005)
first-5 freeze, 0/57; r315 C0 a/b/c = 2.6261/1.5052/0.9400 (tol
0.005), FCIX outliers kz55/kz67 = 0.955/0.915; r316 anchors: n =
65, H stratum {55, 67}, split 21|5|39 with m_0 = 73, C_L2 0.7476,
the 8 regime-L violators EXACT, TOP1 0.558/0.785, rho anchors
kz53/kz67/kz55/kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005),
C_small 1.0694 at kz18; NEW r317 anchors: the F_A TOP-3 ==
(kz53, kz83, kz67) EXACT as an ordered ranking with values
2.47/2.39/2.38 (tol 0.01); the sealed gap rule recovers class B
== {kz55, kz67} with THR_B = 3.7157 (tol 0.005) and class A
EMPTY; the 63-rung complement reproduces C_gen = 0.4579 (tol
0.005) with test violators EXACTLY {kz53, kz83} and complement
C_small = 1.0694 at kz18.

LEG A -- THE (rho_2, F_A) MAP: (A1) the coordinate + bracket +
g-family + envelope + adjudication rules printed as sealed
definitions; the SOURCE-PURE coordinate table (rank, kz, N, m,
QMAX, F_A, B) printed BEFORE any bound-side table of this round.
(A2) SOURCE-PURITY AUDITS: the AST identifier scan over
local_median + g_eval + mono_check + upper_envelope +
spearman_rank + world_coord must be clean against BOUND_FORBIDDEN
and PHI3_FORBIDDEN; the literal scan over those + g_calibrate +
gate_verdict must be clean against the sealed record-literal set
R32X_TABLE_LITERALS (r314 + r315 + r316 + r317 record numbers);
e1/e2/e3 prove the audits bite.  (A3) TOY EXACTNESS: the
local_median cross-ward on the r317 spike toy (medians all 1,
F == values EXACT vs EFP.local_ratio); the g toys (Fc = (1, 2),
targets (0.5, 4.0), baselines (1.0, 1.5), cal = both: SQ par
2.25 -> g(2) = 9, TT pars (2.25, 0.21875) -> g(2) = 4 EXACT, LIN
par 2 -> g(3) = 6); the monotonicity grid accepts all three toy-
calibrated forms (<= TOY_BAR) and is LOUD on the e4 mutant; the
12-point envelope toys (rising -> env rising, Spearman +1, argmax
last; falling -> Spearman -1) EXACT; the Spearman +/-1 toys; the
world_coord insertion toy (flat ladder, val 3 -> F = 3 EXACT);
the verdict tree toys (all five branch combinations EXACT).
(A4) LIVE WARDS: the r316 majorant chain (rho_2 <= PhiL1 <= PhiL2
<= PhiH2, rho_2 <= PhiH1, NORM x cube == rho_2) PLUS the new
bracket lower side qmax x PhiH1 <= rho_2 PLUS the reconstruction
QMAX == F_A x medloc PLUS PhiH1 == (F_A x B)^2, all on every live
world (CHAIN_BAR / 1e-12).  (A5) MAP CENSUS: Spearman(F_A, rho_2)
over the test rungs; the sealed upper envelope with ENV_OK.

LEG B -- THE SEALED g-FAMILY: split seal (verbatim), small-m
certificates (C_small = max rho_2 over ranks 0..20), the three
calibrations printed with declared-set wards, the bound-side map
table (rank, kz, N, m, F_A, rho_2, g_SQ/g_TT/g_LIN marks), the
per-form certification (violations, reserve min/med, trend), the
named-violator coverage (kz53/kz83/kz67/kz55) and the winner by
sealed precedence.

LEG C -- STRUCTURE + WORLD: (C1) the B census: min/med/max over
the ladder, calibration max vs test max (the SOURCE-PURE
boundedness question that carries the upper bracket direction),
halves-slope trend of B over the test rungs; the exact bracket
restated with the measured numbers.  (C2) the world check as
sealed above, with the SCRAMBLE mechanism printed honestly.

LEG D -- THE ADJUDICATION + THEOREM CANDIDATE: the sealed tree;
on SLIDING_BOUND_GO the CANDIDATE THEOREM (sliding cubic bound)
is printed with the explicit g, its constants, m_0, C_small, the
implied uniform constant C_impl = g*(max F_A) and the COROLLARY:
F_A is measured bounded on the ladder (max expected 2.47), so the
sliding bound implies the uniform bound with C = g*(F_A max); the
remaining provenance question is then ONE source-pure question --
is F_A (and for G_SQ the baseline B) source-pure bounded?  (The
new, smaller origin question of the fork-(a) program.)

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) g RE-CALIBRATED AFTER SIGHT of the test violators:
  mutant_g_posthoc consumes the evaluated bound column (rho) over
  the WHOLE ladder to inflate the constant until the seen
  violators are covered -- the BOUND_FORBIDDEN scope audit must
  FLAG it AND on the sealed toy it returns a constant != the
  frozen calibration rule's -- CAUGHT twice.
(e2) F_A READS THE CUBIC TARGET: mutant_coord_readback consumes
  the cubic-moment record (cm/S3) -- the PHI3_FORBIDDEN scan must
  FLAG it (AST-CAUGHT) while the module-own builders stay clean.
(e3) ENVELOPE ON THE CALIBRATION SPLIT: mutant_envelope_cal
  declares the calibration window -- the declared-set ward must
  CATCH the mismatch EXACT (the real envelope declares the test
  set EXACT).
(e4) MONOTONICITY BREAK: mutant_g_nonmono (g = p F (2 - F),
  decreasing beyond F = 1) -- the sealed grid check must be LOUD
  (worst decrease >= MUT_MIN) while all three sealed forms pass.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.  Scope hygiene: the
  module-own coordinate/map builders consume source-pure columns
  + rank order only; g_calibrate consumes target values on
  EXACTLY the declared frozen calibration set (the r306
  calib_freeze pattern, set-warded); fragment audit (no fit
  primitives).

INDEX FIREWALL (binding, r238-r317 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target sum q^3 / rho_2 enters GATES / anchors /
calibration (declared frozen set only) / certification /
diagnostic columns, NEVER a coordinate builder (AST-warded); no
zero/prime oracles anywhere (AST firewall); no fit primitives
(fragment audit).  MACHINERY IMPORTED VERBATIM: r317
EFP.local_ratio + EFP.gap_threshold, r316 TRB.two_regime_state +
TRB.split_midladder, r315 PHI.phi3_variants, r314
SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope +
SCF.collision_census, r306 RY3.cubic_moments + RY3.renyi3_ratio +
RY3.calib_freeze, r298 WBT.block_breaks + WBT.aggregate_blocks,
r269 PBB.mask_edge + PBB.runs_split, r287 L2D.blocks_level2 +
L2D.halves_slope + L2D.autocorr_full, r244 BH.wpack, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE: B_w
= S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).
COFINAL LADDER (pre-sealed, r316/r317 verbatim): frame-A h <=
900, 42 rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36,
38, 39, 52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz);
EXT2: the r316 A5 rule (leftover pool + first 12 windows 1300 < h
<= 1650, first 8 POSITIVE_PREFIX by (N, kz)).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; XW_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; THETA 0.85 (r316 anchor only); N_CAL
5; CAL_THIRD 3; CLS_W 5 (via EFP, verbatim); NB_ENV 6; ENV_RC_MIN
0.5; GAIN_MIN 1.5; GRID_MONO = 0.25 x (1..13); G_FORMS precedence
("SQ", "TT", "LIN"); NAMED_KZ (53, 83, 67, 55); RES_EPS 0.01;
ATTR_MIN 0.25; TWIN_FAC 3.0; SEED_SHUF 321001; MUT_MIN 1e-6;
TOY_BAR 1e-12; TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep + ext
+ ext2 / 1e-6 controls; ID_BAR 1e-12; AC_BAR 1e-9; R314 anchors
shares (-0.4226, +0.5980, +0.8537) tol 0.005, FC 0.629/-0.141 tol
0.005/0.01, mult == 2 EXACT; R306 anchor C_2 1.069 tol 0.005;
R315 anchors C0 (2.6261, 1.5052, 0.9400) tol 0.005, FCIX {55:
0.955, 67: 0.915} tol 0.005; R316 anchors (r317 verbatim): N321 =
65, H set {55, 67}, split (20, 21, 25, 26, 64), M0_REF 73, C_L2
0.7476 tol 0.005, violator set {53, 105, 83, 71, 68, 88, 76,
119} EXACT, TOP1 {55: 0.558, 67: 0.785} tol 0.005, RHO {53:
1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790} tol 0.005, C_SMALL
1.0694 tol 0.005 at kz18; R317 anchors: FA_TOP {53: 2.47, 83:
2.39, 67: 2.38} tol 0.01 ORDERED, THR_B 3.7157 tol 0.005, B set
(55, 67), class A EMPTY, C_GEN 0.4579 tol 0.005, complement
violators (53, 83) EXACT; R32X_TABLE_LITERALS = the sealed r314 +
r315 + r316 forbidden set (r317 verbatim) UNION the r317 record
set {2.47, 2.39, 2.38, 1.93, 1.9, 1.74, 3.7157, 7.23, 4.96, 2.79,
2.7, 0.4579, 1.78, 1.233, 1.24, 2.06, -0.17, 0.44, 0.59, 1.0493,
0.7791, 2.68, 1.99}; runtime <= 1800 s; smoke = w9 + controls +
toys + scope/purity audits + the chain/bracket wards on w9 +
controls + e1-e4 mutants; ladder, extensions, anchors, map,
split, calibration, certification and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r314/r315/r306/r316/r317 RECORD number adopted
as-is; the concentration bracket, the PhiH1 == (F_A B)^2
identity, the monotonicity of the three g forms and the r306
chain (bound => n_eff) are derived algebra, disclosed above; the
CHOICE of the g-family is motivated by that algebra (G_SQ) and by
the r317 RECORD reading (G_TT: "a two-term bound C_1 + C_2
F_A^gamma"; G_LIN: the minimal form named in the fork-(a)
contract) -- NO map value, NO envelope, NO calibration constant,
NO violation count of this round was computed before this spec
was frozen; NB_ENV = 6, ENV_RC_MIN = 0.5, GAIN_MIN = 1.5 and the
grid are coarse a-priori bars (NB_ENV sized so each test bin
holds >= 6 rungs; GAIN_MIN demands the sliding bound genuinely
vary; the grid covers the recorded F_A range [~0.5, 2.47] with
margin); the four sealed verdicts are symmetric -- the tree maps
every leak to its named abort by CONTRACT, not to favor an
outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the four main verdicts fires):
  R321_ANCHORS(r314 shares + FC + mult, identity wards, r306 C_2,
    r315 C0 + FCIX, r316 ladder/split/C_L2/violators/TOP1/rho/
    C_small, r317 FA-top3 + gap-B + C_gen + complement violators)
+ SEAL(coordinate + bracket + g-family + envelope + tree + purity
    audits + toys + live wards)
+ MAP(Spearman, envelope bins, ENV_OK)
+ GFAMILY(constants, per-form violations, named coverage, winner,
    reserve, trend)
+ STRUCTURE(B census: cal max vs test max, trend -- the source-
    pure upper-direction carrier)
+ WORLD(admission at the sliding bound + twin band + SCRAMBLE
    mechanism)
+ [exactly one of] SLIDING_BOUND_GO(g*) / ENVELOPE_DIFFUSE /
    G_FAILS_POINTWISE / WORLD_LEAK
+ THEOREM(candidate text printed on GO)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the coordinate is the r317 import, not a
re-tuned sibling; the g forms, their calibration rules, the
split, the envelope rule, the gain bar and the tree are sealed
BEFORE any map or bound value of this round exists; the
calibration consumes the target on EXACTLY the frozen mid-ladder
window (G_SQ consumes NO target at all); a GO fixes a certified
SLIDING statement ON THE MEASURED RUNGS with explicit (g, m_0,
C_small, C_impl), it proves NO universal bound beyond them and NO
cofinal law; the implied uniform constant C_impl is expected
LOOSER than the r306 first-5 constant -- the round buys FORM
(one gliding bound, no regimes, no exceptions), not sharpness,
and says so; the world columns are n = 1 per control; a DIFFUSE
or FAILS letter seals the negative honestly; r243-r317 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 39/39 (0.5 s), NO amendment; calibration pass 1 =
first full evaluation, 39/39, wall 36.0 s, NO amendment; record
run1/run2 after this insertion, identical up to WALL; PROTOCOL
DISCLOSURE: a drafting error had placed PREFILLED PLACEHOLDER
record tables into this spec BEFORE any run -- they were removed
COMPLETELY before the first smoke run and are disclosed here (the
r316/r317 protocol-error class); the ONLY post-freeze edit is
this record-table insertion, which IS the protocol -- no bar,
band, rule or verdict rule moved):
CAL_VERDICT = R321_ANCHORS(shares -0.4226/+0.5980/+0.8537, FC
0.629/-0.141, mult == 2 on 65/65, identity wards 4.5e-17 /
4.7e-16 / 4.1e-16, r306 C_2 1.069 viol 0/57, r315 C0
2.6261/1.5052/0.9400 + FCIX 0.955/0.915, r316 n = 65, H = {55,
67}, split 21|5|39 m_0 = 73, C_L2 0.7476, the 8-violator set
EXACT, TOP1 0.558/0.785, rho kz53/kz67/kz55/kz83 = 1.0493/
1.0536/0.4821/0.7791, C_small 1.0694 @ kz18; r317 F_A top-3
(53, 83, 67) = 2.47/2.39/2.38 EXACT ORDERED, gap-B {55, 67}
THR_B 3.7157, class A EMPTY, 63-rung complement C_gen 0.4579
with test violators (53, 83), C_small_c 1.0694 @ kz18 -- ALL
bit-near) + SEAL(purity clean: 0 id + 0 literal hits on the six
map builders + calibrator + tree; toys exact: medloc cross-ward
0.0, g toys SQ 9 / TT 4 / LIN 6, mono grid 3/3 accepted,
envelope rising/falling +1/-1, world_coord 3.0, tree 5/5
branches; live wards on 69 live worlds: r316 chain 6.5e-16,
NORM x cube 7.9e-16, NEW bracket lower side qmax PhiH1 <= rho_2
worst slack 0.0 -- the bracket is TWO-SIDED live, reconstruction
QMAX == F_A x medloc 1.6e-16, PhiH1 == (F_A B)^2 5.7e-16) +
MAP(F_A range on the 65-rung ladder min/med/max 0.58/1.01/2.47
(max at kz53); Spearman(F_A, rho_2 | 39 test) = +0.84 -- the
bulk correlation itself is STRONG, not only the envelope;
envelope bins (F_med, max rho_2): (0.69, 0.2136) (0.82, 0.2500)
(0.93, 0.2622) (1.11, 0.2809) (1.35, 0.3758) (2.15, 1.0536);
argmax = top bin, bin Spearman +1.000 -- the envelope is
STRICTLY MONOTONE in the coordinate: ENV_OK) +
GFAMILY(constants frozen on cal ranks 21..25: G_SQ b = 1.3056
(= B_cal_max 1.1426 squared, SOURCE-PURE -- no target value
consumed); G_TT c_1 = 0.3012, c_2 = 0.03846; G_LIN a = 0.3061;
mono grid 3/3; violations on the 39 test rungs: SQ 0 / TT 2
(kz53, kz67 -- the two-term form misses exactly the two deepest
spikes) / LIN 5 (kz38, kz40, kz53, kz67, kz83); named coverage
kz53/kz83/kz67/kz55: SQ 4/4, TT 1/4 (only kz83), LIN 1/4;
WINNER by sealed precedence: G_SQ; reserve min/med over test
2.71/5.35; trend of rho_2/g(F_A) -0.341 FALLING -- the sliding
reserve GROWS into depth; named-violator record at G_SQ: kz53
rho 1.0493 g 7.9714 rsv 7.6 / kz83 0.7791 g 7.4877 rsv 9.6 /
kz67 1.0536 g 7.4069 rsv 7.0 / kz55 0.4821 g 3.4841 rsv 7.2) +
STRUCTURE(B = medloc x m/log m: ladder min/med/max 0.9500/
1.1322/1.4088; CAL MAX 1.1426 vs TEST MAX 1.4088 -> NOT bounded
by its cal max (ratio 1.23), trend over test +0.122 RISING --
THE HONEST STRUCTURAL FINDING: the pure-algebra transfer route
(rho_2 <= F_A^2 B^2 with B <= B_cal) does NOT close; the G_SQ
certificate holds on the measured rho_2 DIRECTLY (the bracket
upper side is loose by the qmax factor, which falls faster than
B^2 rises); the concentration bracket qmax PhiH1 <= rho_2 <=
PhiH1 = (F_A B)^2 is live two-sided on 69 worlds) +
WORLD(w9/w13/EPSTEIN admitted at the sliding bound: mult 2,
rho_2 0.458/0.461/0.368 <= g(F_ins) 0.90/1.55/1.29 at F_ins
0.83/1.09/1.00; twin band PhiL2 factor 1.04 <= 3.0; SCRAMBLE
mechanism honestly documented: the coordinate bound HOLDS on
SCRAMBLE (rho_2 1.780 <= g(2.00) = 5.21 -- the coordinate does
NOT reject it: SCRAMBLE is a concentration spike too, F_ins
2.00) and the CLASS machinery rejects it (COLL attribution dev
3.69 >= 0.25 AND seeded shuffle 321001 edgewise 9.8e-1 with
mass matched 2.0e-17, 294/300 atoms) -- scr_ok via the class
side condition, exactly the disclosed fallback) +
SLIDING_BOUND_GO(G_SQ: rho_2 <= 1.3056 x F_A^2 on 0/39 test
violations + 4/4 named; gain 15.95 >= 1.5; ENV_OK; world clean)
+ THEOREM(printed: sum q^3 <= 1.3056 F_A(w)^2 (log m)^2/m^2 for
m >= 73; 21 small-m certificates, C_small 1.0694; COROLLARY
C_impl = g(2.47) = 7.97 = C_tot, n_eff >= m/(2.82 log m),
DISCLOSED 7.5x looser than the r306 first-5 constant -- the
round buys FORM, not sharpness; the new smaller provenance
question printed) + MUSTFAIL_LEDGER(e1 AST-FLAGGED on the rho
identifier + toy 5.0 != frozen 1.0; e2 AST-FLAGGED on the cm
read-back while the six own builders are clean (0 hits); e3
declared cal-set != test-set EXACT; e4 mono grid LOUD 1.0625 >=
1e-6 vs 3/3 sealed forms accepted; m5a t_term / m5b g_branch
FLAGGED).
READING (typed, no upgrade): the sealed letter is
SLIDING_BOUND_GO(G_SQ) -- fork (a) in the r317-sharpened form
DELIVERS the statement shape the r317 abort demanded: (1) THE
SLIDING BOUND EXISTS: rho_2 <= 1.3056 x F_A^2 pointwise on all
39 mid-ladder test rungs AND on all four named r316/r317
violators (kz53/kz83/kz67/kz55 now INSIDE with reserves
7.0..9.6 -- the exact point of the gliding form: what killed
every flat mid-ladder constant since r316 is absorbed by the
coordinate), with reserve min/med 2.71/5.35 and FALLING trend
-0.341 (the reserve grows into depth); (2) THE COORDINATE
CARRIES: the test envelope is STRICTLY monotone in F_A (bin
Spearman +1.000, top bin 1.0536 at F_med 2.15) and even the
bulk correlation is strong (+0.84) -- stronger than the r317
continuum reading suggested; the gain is 15.95 (the bound
genuinely slides; it is NOT a disguised flat constant); (3) THE
WINNING FORM IS THE ALGEBRA-DERIVED ONE: G_SQ's constant is
(max cal B)^2, a SOURCE-PURE number -- NO target value enters
the calibration; the r317-named two-term heuristic G_TT is
tight but misses exactly kz53/kz67, and G_LIN fails 5/39 (the
coordinate is quadratic-sufficient, not linear-sufficient) --
the derivation-strength precedence was the right seal; (4) THE
HONEST STRUCTURAL CAVEAT (the round's second find): the
pure-algebra transfer route does NOT close -- B = medloc x
m/log m is NOT bounded by its cal max (test max 1.4088 = 1.23 x
cal max, trend +0.122 RISING), so rho_2 <= b F_A^2 does NOT
follow from rho_2 <= F_A^2 B^2 alone; the certificate holds on
the measured rho_2 directly because the bracket's qmax slack
falls faster than B^2 rises -- the proof-side decomposition is
rho_2 = (qmax-share) x F_A^2 B^2 with the qmax-share the
remaining object; (5) THE WORLD SIGN IS HONEST AND TYPED:
SCRAMBLE is NOT rejected by the coordinate bound (its inflated
cube comes WITH an inflated concentration ratio F_ins 2.00 --
the sliding bound covers it at 5.21) -- the rejection is
carried by the r317 CLASS side condition (COLL attribution 3.69
+ seeded shuffle 294/300 with matched mass), exactly the
disclosed fallback mechanism; twin band 1.04, EPSTEIN admitted
at reserve 3.5.  Honest negatives: C_impl = 7.97 is 7.5x looser
than the r306 first-5 constant 1.069 -- the round buys FORM
(one gliding bound, no regimes, no exceptions, all old
violators inside), not sharpness, exactly as sealed; the GO
certifies the measured 65-rung ladder + 2 mains + 2 live
controls and NOTHING beyond; the SCRAMBLE non-rejection by the
coordinate alone means the sliding bound is NOT world-
separating by itself -- it needs the class side condition; B
rising is a real obstruction to the pure-algebra proof route.
R322 direction (typed, census-grade): the provenance question
is now SOURCE-PURE, LOCAL and SPLIT IN TWO -- (a) is F_A
bounded (measured max 2.47; the near-critical family is its
top), (b) what bounds the qmax-share rho_2/(F_A^2 B^2) =
(qmax L)^3-share of the cube (measured: it falls fast enough to
beat the rising B^2) -- the natural attack is the r306
SHAPE3/stationarity route applied to the LOCAL MEDIAN of the
normalized shape (B is a median-of-max object; the r302 M_2
stationarity 1.973 already pins the second moment of the same
shape).  Runtime 36.0 s full / 0.5 s smoke; run1/run2 identical
up to WALL.  AMENDMENTS AFTER FREEZE: none except this
record-table insertion (and the disclosed pre-run placeholder
removal).

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
import phi3_functional_probe as PHI            # noqa: E402 r315
import two_regime_bound_probe as TRB           # noqa: E402 r316
import exception_families_probe as EFP         # noqa: E402 r317
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
NB_ENV = 6
ENV_RC_MIN = 0.5
GAIN_MIN = 1.5
GRID_MONO = tuple(0.25 * k for k in range(1, 14))
G_FORMS = ("SQ", "TT", "LIN")
NAMED_KZ = (53, 83, 67, 55)
RES_EPS = 0.01
ATTR_MIN = 0.25
TWIN_FAC = 3.0
SEED_SHUF = 321001
MUT_MIN = 1e-6
TOY_BAR = 1e-12
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
N321_REF = 65
R316_H_SET = (55, 67)
R316_SPLIT = (20, 21, 25, 26, 64)     # small end, cal lo/hi, test lo/hi
M0_REF = 73
R316_CL2 = 0.7476
R316_CL2_TOL = 0.005
R316_VIOL_SET = (53, 105, 83, 71, 68, 88, 76, 119)
R316_TOP1 = {55: 0.558, 67: 0.785}
R316_TOP1_TOL = 0.005
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
R317_CGEN = 0.4579
R317_CGEN_TOL = 0.005
R317_VIOL2 = (53, 83)
R32X_TABLE_LITERALS = frozenset((
    -0.4226, 0.598, 0.8537, 0.629, -0.141,
    -0.452, 0.823, 0.617, 0.057,
    -0.541, 0.43, 1.111, 0.675, 0.043,
    -2.695, -2.652, 6.347, 0.101, 0.011,
    -0.171, 0.856, 0.315, 0.693, 0.073,
    2.6261, 1.5052, 0.94, 0.955, 0.915,
    22.85, 66.09, 87.64,
    2.3883, 2.0841, 1.4433, 2.3545, 1.3615, 0.1375,
    0.9597, 0.7102, 0.4795,
    4.6095, 2.726, 2.5458, 1.8898, 2.432, 1.7289, 3.69,
    0.7476, 0.5531, 1.4263, 1.1266, 1.0804, 0.9648,
    0.8013, 0.7877, 0.7819, 0.7698, 34.0556, 3.0559,
    57.3, 47.86, 2.76, 7.84, 0.558, 0.785, 0.105, 0.387,
    21.7, 24.9, 31.9, 40.4, 1.0694, 0.4821, 1.0536,
    1.049, 0.779, 0.654, 0.148, 1.04, 3.27, 0.73,
    0.52, 1.35, 0.086, 0.202,
    2.47, 2.39, 2.38, 1.93, 1.9, 1.74, 3.7157, 7.23,
    4.96, 2.79, 2.7, 0.4579, 1.78, 1.233, 1.24, 2.06,
    -0.17, 0.44, 0.59, 1.0493, 0.7791, 2.68, 1.99))

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
    lies in the sealed r314+r315+r316+r317 record-literal set."""
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
                            in R32X_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the map/
# ---------------- coordinate builders consume source-pure columns
# ---------------- (QMAX, F_A, B) plus rank order only; the
# ---------------- withheld terminal drive key, the branch label,
# ---------------- the cubic target and the record literals are
# ---------------- forbidden (AST identifier scan + literal scan).
# ---------------- g_calibrate consumes target values on EXACTLY
# ---------------- the declared frozen calibration set (the r306
# ---------------- calib_freeze pattern; declared-set warded).
def local_median(vals):
    """the rank-local median companion of the imported r317
    local_ratio (window verbatim: half-width W = EFP.CLS_W, self
    excluded, truncated at the ladder ends): the baseline column
    medloc; warded EXACT against the import via
    vals == local_ratio(vals) x local_median(vals)."""
    v = [float(x) for x in vals]
    n = len(v)
    out = []
    for i in range(n):
        lo = max(0, i - EFP.CLS_W)
        hi = min(n, i + EFP.CLS_W + 1)
        nb = [v[j] for j in range(lo, hi) if j != i]
        out.append(float(np.median(nb)))
    return out


def g_eval(form, par, F):
    """the sealed monotone g-family evaluator (frozen forms):
    SQ: par[0] x F^2; TT: par[0] + par[1] x F^3; LIN: par[0] x F.
    All non-decreasing on F > 0 for non-negative parameters
    (checked on the sealed grid by mono_check)."""
    F = float(F)
    if form == "SQ":
        return par[0] * F * F
    if form == "TT":
        return par[0] + par[1] * F ** 3
    if form == "LIN":
        return par[0] * F
    raise ValueError(form)


def g_calibrate(form, Fc, target, base, cal_idx):
    """constants frozen on EXACTLY the declared calibration index
    set (returned for the set ward):
    SQ:  par = ((max cal base)^2,)  -- consumes the SOURCE-PURE
         baseline column only, NO target value;
    TT:  c_1 = median cal target, c_2 = max cal (target-c_1)_+/F^3;
    LIN: a = max cal target/F."""
    cal = tuple(cal_idx)
    if form == "SQ":
        return ((max(float(base[i]) for i in cal) ** 2,), cal)
    if form == "TT":
        c1 = float(np.median([float(target[i]) for i in cal]))
        c2 = max(max(float(target[i]) - c1, 0.0)
                 / max(float(Fc[i]) ** 3, 1e-300) for i in cal)
        return ((c1, c2), cal)
    if form == "LIN":
        return ((max(float(target[i]) / max(float(Fc[i]), 1e-300)
                     for i in cal),), cal)
    raise ValueError(form)


def mono_check(form, par):
    """the sealed monotonicity check: evaluate the calibrated form
    on GRID_MONO and return the worst DECREASE (0 for monotone;
    the e4 mutant must be LOUD >= MUT_MIN)."""
    vals = [g_eval(form, par, f) for f in GRID_MONO]
    worst = 0.0
    for k in range(len(vals) - 1):
        worst = max(worst, vals[k] - vals[k + 1])
    return worst


def upper_envelope(Fv, vals, idx):
    """the sealed fit-free upper envelope: over EXACTLY the
    declared index tuple, sort by the coordinate, split into
    NB_ENV equal-count rank bins, per bin (median coordinate, max
    value); returns (bins, declared) -- the declared set is warded
    against the sealed test split (e3 mutant CAUGHT)."""
    idx = tuple(idx)
    o = sorted(idx, key=lambda i: float(Fv[i]))
    parts = np.array_split(np.arange(len(o)), NB_ENV)
    bins = []
    for p in parts:
        if len(p) == 0:
            continue
        mem = [o[int(k)] for k in p]
        bins.append((float(np.median([float(Fv[i]) for i in mem])),
                     max(float(vals[i]) for i in mem)))
    return bins, idx


def spearman_rank(a, b):
    """rank correlation, fit-free: Pearson on stable rank vectors
    (argsort of argsort; deterministic, no fit primitives)."""
    ra = np.argsort(np.argsort(np.asarray(a, dtype=float),
                               kind="stable"),
                    kind="stable").astype(float)
    rb = np.argsort(np.argsort(np.asarray(b, dtype=float),
                               kind="stable"),
                    kind="stable").astype(float)
    ra -= float(np.mean(ra))
    rb -= float(np.mean(rb))
    den = math.sqrt(float(np.sum(ra * ra)) * float(np.sum(rb * rb)))
    return float(np.sum(ra * rb)) / max(den, 1e-300)


def world_coord(val, depth, ladder_depths, ladder_vals):
    """the sealed INSERTION RULE for world coordinates: the
    world's column value against the rank-local median of the
    ladder column at the world's depth-insertion point (window
    W = EFP.CLS_W ladder ranks each side, no self-exclusion --
    the world is not a ladder member)."""
    ld = np.asarray(ladder_depths, dtype=float)
    j = int(np.searchsorted(ld, float(depth)))
    lo = max(0, j - EFP.CLS_W)
    hi = min(len(ladder_vals), j + EFP.CLS_W)
    nb = [float(ladder_vals[k]) for k in range(lo, hi)]
    return float(val) / max(float(np.median(nb)), 1e-300)


def gate_verdict(has_winner, world_ok, env_ok, gain_ok):
    """the sealed verdict tree (booleans only; exactly one fires):
    no winner -> ENVELOPE_DIFFUSE if the envelope is diffuse,
    else G_FAILS_POINTWISE; winner -> WORLD_LEAK on a world leak,
    ENVELOPE_DIFFUSE if the envelope is diffuse or the gain is
    trivial, else SLIDING_BOUND_GO."""
    if not has_winner:
        return "ENVELOPE_DIFFUSE" if not env_ok \
            else "G_FAILS_POINTWISE"
    if not world_ok:
        return "WORLD_LEAK"
    if (not env_ok) or (not gain_ok):
        return "ENVELOPE_DIFFUSE"
    return "SLIDING_BOUND_GO"


def mutant_g_posthoc(Fv, rho):
    """e1 MUST-FAIL MUTANT: the g constant re-calibrated AFTER
    SIGHT over the WHOLE ladder (consumes rho, covers every seen
    violator by construction) -- the BOUND_FORBIDDEN scope audit
    must FLAG it AND on the sealed toy it returns a constant !=
    the frozen calibration rule's."""
    return max(r / max(float(f), 1e-300)
               for f, r in zip(Fv, rho))


def mutant_coord_readback(cmrec, nblk):
    """e2 MUST-FAIL MUTANT: a 'coordinate' consuming the cubic-
    moment record (the target side) -- the PHI3_FORBIDDEN
    identifier scan must FLAG this."""
    cm = cmrec
    return cm["S3"] * float(nblk) * float(nblk)


def mutant_envelope_cal(Fv, vals, cal_idx):
    """e3 MUST-FAIL MUTANT: the envelope evaluated on the
    CALIBRATION split instead of the declared test set -- the
    declared-set ward must CATCH the mismatch EXACT."""
    return upper_envelope(Fv, vals, cal_idx)


def mutant_g_nonmono(par, F):
    """e4 MUST-FAIL MUTANT: a non-monotone 'bound shape'
    g = par x F x (2 - F), decreasing beyond F = 1 -- the sealed
    grid check must be LOUD on it."""
    return par * float(F) * (2.0 - float(F))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("continuous_coordinate_probe -- "
          "PRIME.L2.RENYI3.CONTINUOUS_COORDINATE.01 (round 321)")
    print("SPEC_SHA %s   R317_SHA %s   R316_SHA %s (imported)"
          % (SPEC_SHA[:16], EFP.SPEC_SHA[:16], TRB.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + chain/bracket wards + "
                        "e1-e4; ladder, extensions, anchors, map, "
                        "split, calibration, certification and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE CONTINUOUS-COORDINATE ROUND (reviewer fork (a), "
          "r317-sharpened): bound rho_2 BY the single source-pure "
          "coordinate F_A = rank-local QMAX ratio (r317 import, W "
          "= %d) -- rho_2(w) <= g(F_A(w)) pointwise with g "
          "explicit and MONOTONE, sealed family SQ (b F^2, "
          "derived from the exact bracket qmax PhiH1 <= rho_2 <= "
          "PhiH1 = (F_A B)^2) > TT (c1 + c2 F^3, the r317-named "
          "two-term form) > LIN (a F); constants frozen on the "
          "r316 mid-ladder window; envelope rule NB = %d bins on "
          "the declared TEST set, ENV_RC_MIN %.1f; gain bar "
          "%.1f; verdicts SLIDING_BOUND_GO / ENVELOPE_DIFFUSE / "
          "G_FAILS_POINTWISE / WORLD_LEAK sealed BEFORE "
          "evaluation" % (EFP.CLS_W, NB_ENV, ENV_RC_MIN, GAIN_MIN))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("local_median", "g_eval", "mono_check",
               "upper_envelope", "spearman_rank", "world_coord"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the six module-own "
          "map/coordinate builders clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN (%d hits); m5a gift-bound FLAGGED "
          "(%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r317 scaffold verbatim)
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
            shares = dict(far=C_far_flux / max(cube, 1e-300),
                          pair=sct["C_pair"] / max(cube, 1e-300),
                          full=sct["C_full"] / max(cube, 1e-300))
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
            # diagnostic census columns (read-back-adjacent,
            # computed OUTSIDE the builders, disclosed):
            top1 = float(np.max(np.abs(sct["x"])) ** 3) \
                / max(cube, 1e-300)
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
            top1 = 0.0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd, shares=shares,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    cc=cc, ph=ph, trs=trs, rho2=rho2, top1=top1,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

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
    section("S3  LEG 0 -- ANCHOR REGRESSION "
            "(r314/r315/r306/r316/r317)")
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
             "QMAX %.4f, PhiH1 %.4f, PhiL2 %.4f, mult max %d"
             % (ev9s["shares"]["far"], ev9s["shares"]["pair"],
                ev9s["shares"]["full"], ev9s["trs"]["qmax"],
                ev9s["trs"]["phiH1"], ev9s["trs"]["phiL2"],
                ev9s["mx_mult"]))
        check("G30-r314-shares-fc", True, "SMOKE: skipped")
        check("G32-r306-bound-live", True, "SMOKE: skipped")
        check("G33-r315-anchors", True, "SMOKE: skipped")
        check("G34-r316-anchors", True, "SMOKE: skipped")
        check("G35-r317-anchors", True, "SMOKE: skipped")
        srt57 = []
        srt321 = []
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
        srt321_all = sorted(recs + erecs + e2recs,
                            key=lambda rc: (rc["N"], rc["kz"]))
        excl = [rc for rc in srt321_all
                if rc["ev"]["mx_mult"] > MULT_CAP]
        srt321 = [rc for rc in srt321_all
                  if rc["ev"]["mx_mult"] <= MULT_CAP]
        n321 = len(srt321)
        n_m2 = sum(1 for rc in srt321
                   if rc["ev"]["mx_mult"] == 2)
        check("G30-r314-shares-fc",
              all(abs(meds[i] - R314_SHARES[i]) <= R314_SHARE_TOL
                  for i in range(3))
              and abs(fc_med - R314_FC) <= R314_FC_TOL
              and abs(fc_sl - R314_FC_SLOPE) <= R314_FC_SL_TOL
              and n_m2 == n321 and not excl,
              "r314 record reproduced: med shares far/pair/full "
              "%+.4f/%+.4f/%+.4f (rec %+.4f/%+.4f/%+.4f tol "
              "%.3f); FC med %.3f slope %+.3f (rec %.3f/%+.3f); "
              "mult == 2 on %d/%d, mult-cap exclusions %d"
              % (meds[0], meds[1], meds[2], R314_SHARES[0],
                 R314_SHARES[1], R314_SHARES[2], R314_SHARE_TOL,
                 fc_med, fc_sl, R314_FC, R314_FC_SLOPE, n_m2,
                 n321, len(excl)))
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
        # r316 anchors on the class ladder (r317 verbatim)
        h_kz = tuple(sorted(rc["kz"] for rc in srt321
                            if rc["ev"]["trs"]["fcix"] > THETA))
        sm316, ca316, te316 = TRB.split_midladder(n321)
        m_all = [rc["ev"]["m"] for rc in srt321]
        m0_316 = min(m_all[i] for i in ca316 + te316)
        calL = [i for i in ca316
                if srt321[i]["ev"]["trs"]["fcix"] <= THETA]
        CL2 = max(srt321[i]["ev"]["trs"]["phiL2"] for i in calL) \
            if calL else 0.0
        violL2 = tuple(sorted(
            srt321[i]["kz"] for i in te316
            if srt321[i]["ev"]["trs"]["fcix"] <= THETA
            and srt321[i]["ev"]["trs"]["phiL2"] > CL2))
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt321}
        top1_kz = {rc["kz"]: rc["ev"]["top1"] for rc in srt321}
        C_small316 = max(srt321[i]["ev"]["rho2"] for i in sm316)
        j_cs = max(sm316, key=lambda i: srt321[i]["ev"]["rho2"])
        ok316 = (n321 == N321_REF
                 and h_kz == tuple(sorted(R316_H_SET))
                 and sm316[-1] == R316_SPLIT[0]
                 and ca316 == tuple(range(R316_SPLIT[1],
                                          R316_SPLIT[2] + 1))
                 and te316[0] == R316_SPLIT[3]
                 and te316[-1] == R316_SPLIT[4]
                 and m0_316 == M0_REF
                 and abs(CL2 - R316_CL2) <= R316_CL2_TOL
                 and violL2 == tuple(sorted(R316_VIOL_SET))
                 and all(abs(top1_kz.get(kz, -1.0)
                             - R316_TOP1[kz]) <= R316_TOP1_TOL
                         for kz in R316_TOP1)
                 and all(abs(rho_kz.get(kz, -1.0)
                             - R316_RHO[kz]) <= R316_RHO_TOL
                         for kz in R316_RHO)
                 and abs(C_small316 - R316_CSMALL)
                 <= R316_CSMALL_TOL
                 and srt321[j_cs]["kz"] == R316_CSMALL_KZ)
        check("G34-r316-anchors", ok316,
              "r316 record reproduced on the class ladder: n = "
              "%d (rec %d); H stratum %s (rec %s); split small "
              "0..%d / cal %d..%d / test %d..%d, m_0 = %d (rec "
              "%d); C_L2 %.4f (rec %.4f tol %.3f); regime-L test "
              "violators %s == the named 8; TOP1 kz55/kz67 "
              "%.3f/%.3f (rec %.3f/%.3f); rho anchors kz53/kz67/"
              "kz55/kz83 %.4f/%.4f/%.4f/%.4f (rec %.4f/%.4f/"
              "%.4f/%.4f tol %.3f); C_small %.4f @ kz%d (rec "
              "%.4f @ kz%d)"
              % (n321, N321_REF, str(h_kz),
                 str(tuple(sorted(R316_H_SET))), sm316[-1],
                 ca316[0], ca316[-1], te316[0], te316[-1],
                 m0_316, M0_REF, CL2, R316_CL2, R316_CL2_TOL,
                 str(violL2), top1_kz.get(55, -1.0),
                 top1_kz.get(67, -1.0), R316_TOP1[55],
                 R316_TOP1[67], rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO[53],
                 R316_RHO[67], R316_RHO[55], R316_RHO[83],
                 R316_RHO_TOL, C_small316, srt321[j_cs]["kz"],
                 R316_CSMALL, R316_CSMALL_KZ))
        # r317 anchors: the sealed class machinery re-run bit-near
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt321]
        phiL2_col = [rc["ev"]["trs"]["phiL2"] for rc in srt321]
        FA = EFP.local_ratio(qmax_col)
        FB = EFP.local_ratio(phiL2_col)
        thrA, kA, gA = EFP.gap_threshold(FA)
        thrB, kB, gB = EFP.gap_threshold(FB)
        memA = tuple(i for i, v in enumerate(FA) if v >= thrA)
        memB = tuple(sorted(srt321[i]["kz"]
                            for i, v in enumerate(FB)
                            if v >= thrB))
        ordFA = sorted(range(n321), key=lambda i: -FA[i])
        top3_kz = tuple(srt321[i]["kz"] for i in ordFA[:3])
        top3_val = {srt321[i]["kz"]: FA[i] for i in ordFA[:3]}
        rho_all = [rc["ev"]["rho2"] for rc in srt321]
        famAB = set(memA) | set(i for i, v in enumerate(FB)
                                if v >= thrB)
        comp = [i for i in range(n321) if i not in famAB]
        sm_c, ca_c, te_c = TRB.split_midladder(len(comp))
        C_gen = max(rho_all[comp[j]] for j in ca_c)
        viol_gen = tuple(sorted(
            srt321[comp[j]]["kz"] for j in te_c
            if rho_all[comp[j]] > C_gen))
        C_small_c = max(rho_all[comp[j]] for j in sm_c)
        j_csc = max(sm_c, key=lambda j: rho_all[comp[j]])
        ok317 = (top3_kz == R317_FA_ORDER
                 and all(abs(top3_val[kz] - R317_FA_TOP[kz])
                         <= R317_FA_TOL for kz in R317_FA_TOP)
                 and memA == ()
                 and memB == tuple(sorted(R317_B_KZ))
                 and abs(thrB - R317_THRB) <= R317_THRB_TOL
                 and abs(C_gen - R317_CGEN) <= R317_CGEN_TOL
                 and viol_gen == tuple(sorted(R317_VIOL2))
                 and abs(C_small_c - R316_CSMALL)
                 <= R316_CSMALL_TOL
                 and srt321[comp[j_csc]]["kz"] == R316_CSMALL_KZ)
        check("G35-r317-anchors", ok317,
              "r317 record reproduced: F_A top-3 %s = "
              "%.2f/%.2f/%.2f (rec %s = %.2f/%.2f/%.2f tol %.2f, "
              "ORDERED); gap rule: class A %s (rec EMPTY), class "
              "B %s THR_B %.4f (rec %s / %.4f tol %.3f); %d-rung "
              "complement: C_gen %.4f (rec %.4f), test violators "
              "%s (rec %s), C_small_c %.4f @ kz%d (rec %.4f @ "
              "kz%d)"
              % (str(top3_kz), top3_val.get(top3_kz[0], -1),
                 top3_val.get(top3_kz[1], -1),
                 top3_val.get(top3_kz[2], -1),
                 str(R317_FA_ORDER), R317_FA_TOP[53],
                 R317_FA_TOP[83], R317_FA_TOP[67], R317_FA_TOL,
                 "EMPTY" if not memA else str(memA), str(memB),
                 thrB, str(tuple(sorted(R317_B_KZ))), R317_THRB,
                 R317_THRB_TOL, len(comp), C_gen, R317_CGEN,
                 str(viol_gen), str(tuple(sorted(R317_VIOL2))),
                 C_small_c, srt321[comp[j_csc]]["kz"],
                 R316_CSMALL, R316_CSMALL_KZ))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "COORDINATE TABLE")
    pure_lits = []
    for fn in ("local_median", "g_eval", "mono_check",
               "upper_envelope", "spearman_rank", "world_coord",
               "g_calibrate", "gate_verdict"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_g_posthoc", BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_coord_readback", PHI3_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1,
          "SOURCE PURITY: the six map/coordinate builders clean "
          "vs PHI3_FORBIDDEN + BOUND_FORBIDDEN (%d id hits); the "
          "eight builder+gate functions clean vs the sealed "
          "r314+r315+r316+r317 record-literal set (%d literal "
          "hits); consumed inputs: source-pure columns (QMAX, "
          "F_A, B) + rank order (g_calibrate: target on the "
          "declared frozen cal set only, SQ consumes NO target); "
          "e1 g-posthoc FLAGGED (%s); e2 coord-readback FLAGGED "
          "(%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS"))
    # toys (exact)
    f_sp = EFP.local_ratio(EFP.TOY_SPIKE)
    med_sp = local_median(EFP.TOY_SPIKE)
    rec_sp = max(abs(EFP.TOY_SPIKE[i] - f_sp[i] * med_sp[i])
                 for i in range(len(f_sp)))
    ok_med = (rec_sp <= TOY_BAR
              and all(abs(m - 1.0) <= TOY_BAR for m in med_sp))
    toy_F = (1.0, 2.0)
    toy_t = (0.5, 4.0)
    toy_b = (1.0, 1.5)
    parSQ, dSQ = g_calibrate("SQ", toy_F, toy_t, toy_b, (0, 1))
    parTT, dTT = g_calibrate("TT", toy_F, toy_t, toy_b, (0, 1))
    parLN, dLN = g_calibrate("LIN", toy_F, toy_t, toy_b, (0, 1))
    ok_g = (abs(parSQ[0] - 2.25) <= TOY_BAR
            and abs(g_eval("SQ", parSQ, 2.0) - 9.0) <= TOY_BAR
            and abs(parTT[0] - 2.25) <= TOY_BAR
            and abs(parTT[1] - 0.21875) <= TOY_BAR
            and abs(g_eval("TT", parTT, 2.0) - 4.0) <= TOY_BAR
            and abs(parLN[0] - 2.0) <= TOY_BAR
            and abs(g_eval("LIN", parLN, 3.0) - 6.0) <= TOY_BAR
            and dSQ == dTT == dLN == (0, 1))
    ok_mono = (mono_check("SQ", parSQ) <= TOY_BAR
               and mono_check("TT", parTT) <= TOY_BAR
               and mono_check("LIN", parLN) <= TOY_BAR)
    toy_Fe = tuple(float(k) for k in range(1, 13))
    toy_up = tuple(float(k) for k in range(1, 13))
    toy_dn = tuple(float(13 - k) for k in range(1, 13))
    env_up, dcl_up = upper_envelope(toy_Fe, toy_up,
                                    tuple(range(12)))
    env_dn, _dcl_dn = upper_envelope(toy_Fe, toy_dn,
                                     tuple(range(12)))
    sp_up = spearman_rank(range(len(env_up)),
                          [e[1] for e in env_up])
    sp_dn = spearman_rank(range(len(env_dn)),
                          [e[1] for e in env_dn])
    ok_env = (len(env_up) == NB_ENV
              and abs(env_up[-1][1] - 12.0) <= TOY_BAR
              and abs(sp_up - 1.0) <= TOY_BAR
              and abs(sp_dn + 1.0) <= TOY_BAR
              and dcl_up == tuple(range(12)))
    ok_sp = (abs(spearman_rank((1, 2, 3, 4), (2, 4, 6, 8)) - 1.0)
             <= TOY_BAR
             and abs(spearman_rank((1, 2, 3, 4), (8, 6, 4, 2))
                     + 1.0) <= TOY_BAR)
    wc_toy = world_coord(3.0, 5.5, tuple(range(1, 11)),
                         (1.0,) * 10)
    ok_wc = abs(wc_toy - 3.0) <= TOY_BAR
    gv = (gate_verdict(True, True, True, True),
          gate_verdict(False, True, False, True),
          gate_verdict(False, True, True, True),
          gate_verdict(True, False, True, True),
          gate_verdict(True, True, False, True))
    ok_gv = gv == ("SLIDING_BOUND_GO", "ENVELOPE_DIFFUSE",
                   "G_FAILS_POINTWISE", "WORLD_LEAK",
                   "ENVELOPE_DIFFUSE")
    check("G41-toy-exactness", ok_med and ok_g and ok_mono
          and ok_env and ok_sp and ok_wc and ok_gv,
          "medloc cross-ward on the r317 spike toy: QMAX == F_A "
          "x medloc EXACT (dev %.1e), medians all 1; g toys: SQ "
          "par 2.25 g(2) = 9, TT pars (2.25, 0.21875) g(2) = 4, "
          "LIN par 2 g(3) = 6, declared (0, 1) EXACT; mono grid "
          "accepts 3/3 toy-calibrated forms; envelope toys: "
          "rising -> env max 12 Spearman +1, falling -> Spearman "
          "-1, declared EXACT; Spearman +/-1 toys EXACT; "
          "world_coord flat-ladder toy 3.0 EXACT; verdict tree "
          "5/5 branches EXACT %s" % (rec_sp, str(gv)))
    # live wards: r316 chain + the new bracket + reconstruction
    chain_w = 0.0
    xw_cube = 0.0
    brk_low = 0.0
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
        # bracket lower side: qmax x PhiH1 <= rho_2
        brk_low = max(brk_low,
                      max(0.0, trs["qmax"] * trs["phiH1"]
                          - ev["rho2"])
                      / max(ev["rho2"], 1e-300))
    if smoke:
        rec_fa = 0.0
        ph_dev = 0.0
    else:
        medloc = local_median(qmax_col)
        rec_fa = max(abs(qmax_col[i] - FA[i] * medloc[i])
                     / max(qmax_col[i], 1e-300)
                     for i in range(n321))
        Bcol = [medloc[i] * float(m_all[i])
                / math.log(float(m_all[i]))
                for i in range(n321)]
        ph_dev = max(abs(srt321[i]["ev"]["trs"]["phiH1"]
                         - (FA[i] * Bcol[i]) ** 2)
                     / max(srt321[i]["ev"]["trs"]["phiH1"],
                           1e-300)
                     for i in range(n321))
    check("G42-bracket-and-chain-ward",
          chain_w <= CHAIN_BAR and xw_cube <= XW_BAR
          and brk_low <= CHAIN_BAR and rec_fa <= 1e-12
          and ph_dev <= CHAIN_BAR,
          "the r316 chain live on %d live worlds (worst slack "
          "%.1e, bar %.0e); NORM x cube == rho_2 (worst %.1e); "
          "NEW bracket lower side qmax x PhiH1 <= rho_2 (worst "
          "slack %.1e -- with the chain: qmax PhiH1 <= rho_2 <= "
          "PhiH1 TWO-SIDED); reconstruction QMAX == F_A x medloc "
          "(worst %.1e)%s"
          % (len(live), chain_w, CHAIN_BAR, xw_cube, brk_low,
             rec_fa,
             "; PhiH1 == (F_A x B)^2 on the ladder (worst %.1e)"
             % ph_dev if not smoke else " (ladder wards SMOKE-"
             "skipped)"))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        info("sealed SOURCE-PURE coordinate table (printed "
             "BEFORE any bound-side table of this round): rank "
             "kz N m QMAX F_A B")
        for i, rc in enumerate(srt321):
            info("%2d kz%-3d N %4d m %3d qmax %.4f FA %5.2f B "
                 "%.4f" % (i, rc["kz"], rc["N"], m_all[i],
                           qmax_col[i], FA[i], Bcol[i]))
        check("G43-coordinate-table", True,
              "the coordinate is the r317 IMPORT (EFP."
              "local_ratio, W = %d) on the sealed QMAX column; "
              "F_A range on the %d-rung ladder: min %.2f / med "
              "%.2f / max %.2f (max at kz%d); B = medloc x "
              "m/log m printed as the source-pure baseline "
              "column"
              % (EFP.CLS_W, n321, min(FA),
                 float(np.median(FA)), max(FA),
                 srt321[int(np.argmax(FA))]["kz"]))

    # ---------------- S5: Leg B -- split + calibration + certif.
    section("S5  LEG B -- SPLIT + g-FAMILY CALIBRATION + "
            "CERTIFICATION")
    if smoke:
        check("G44-split-seal", True, "SMOKE: skipped")
        check("G50-smallm-certificates", True, "SMOKE: skipped")
        check("G51-g-calibration", True, "SMOKE: skipped")
        check("G52-map-census", True, "SMOKE: skipped")
        check("G53-envelope-census", True, "SMOKE: skipped")
        check("G54-certification", True, "SMOKE: skipped")
        check("G55-reserve-trend", True, "SMOKE: skipped")
    else:
        sm_i, ca_i, te_i = TRB.split_midladder(n321)
        ovl = len(set(sm_i) & set(ca_i)) \
            + len(set(sm_i) & set(te_i)) \
            + len(set(ca_i) & set(te_i))
        cover = (tuple(sorted(sm_i + ca_i + te_i))
                 == tuple(range(n321)))
        m0 = min(m_all[i] for i in ca_i + te_i)
        check("G44-split-seal",
              ovl == 0 and cover and len(ca_i) == N_CAL,
              "SEALED split on the %d-rung class ladder "
              "(TRB.split_midladder verbatim): small = ranks "
              "0..%d, cal = %d..%d (kz %s, m %d..%d), test = "
              "%d..%d (%d rungs); overlaps 0 EXACT, cover "
              "EXACT; m_0 = %d"
              % (n321, sm_i[-1], ca_i[0], ca_i[-1],
                 str([srt321[i]["kz"] for i in ca_i]),
                 min(m_all[i] for i in ca_i),
                 max(m_all[i] for i in ca_i),
                 te_i[0], te_i[-1], len(te_i), m0))
        C_small = max(rho_all[i] for i in sm_i)
        j_sm = max(sm_i, key=lambda i: rho_all[i])
        check("G50-smallm-certificates", C_small > 0.0,
              "%d small-m rungs certified individually (direct "
              "evaluation); C_small = %.4f at kz%d -- the finite "
              "exception constant of the theorem candidate"
              % (len(sm_i), C_small, srt321[j_sm]["kz"]))
        pars = {}
        decls = {}
        monos = {}
        for form in G_FORMS:
            pars[form], decls[form] = g_calibrate(
                form, FA, rho_all, Bcol, ca_i)
            monos[form] = mono_check(form, pars[form])
        ok_decl = all(decls[f] == tuple(ca_i) for f in G_FORMS)
        check("G51-g-calibration", ok_decl
              and all(monos[f] <= TOY_BAR for f in G_FORMS),
              "constants FROZEN on the declared cal set (ward "
              "EXACT %s): G_SQ b = %.4f (= B_cal_max %.4f "
              "squared, SOURCE-PURE -- no target consumed); "
              "G_TT c_1 = %.4f, c_2 = %.5f; G_LIN a = %.4f; "
              "monotonicity grid (%d pts, %.2f..%.2f): worst "
              "decrease SQ %.1e / TT %.1e / LIN %.1e -- 3/3 "
              "accepted"
              % (ok_decl, pars["SQ"][0],
                 math.sqrt(pars["SQ"][0]), pars["TT"][0],
                 pars["TT"][1], pars["LIN"][0], len(GRID_MONO),
                 GRID_MONO[0], GRID_MONO[-1], monos["SQ"],
                 monos["TT"], monos["LIN"]))
        # the bound-side map table + census
        info("the (rho_2, F_A) map (bound-side; per-form "
             "violation marks on TEST rungs): rank kz N m FA "
             "rho_2 g_SQ g_TT g_LIN [set] marks")
        gvals = {f: [g_eval(f, pars[f], FA[i])
                     for i in range(n321)] for f in G_FORMS}
        setlab = {}
        for i in sm_i:
            setlab[i] = "SMALL"
        for i in ca_i:
            setlab[i] = "CAL"
        for i in te_i:
            setlab[i] = "TEST"
        for i in range(n321):
            marks = "".join(
                ("*" if rho_all[i] > gvals[f][i] else ".")
                for f in G_FORMS) if i in te_i else "   "
            info("%2d kz%-3d N %4d m %3d FA %5.2f rho2 %.4f g "
                 "%7.4f %7.4f %7.4f %-5s %s"
                 % (i, srt321[i]["kz"], srt321[i]["N"],
                    m_all[i], FA[i], rho_all[i],
                    gvals["SQ"][i], gvals["TT"][i],
                    gvals["LIN"][i], setlab[i], marks))
        sp_test = spearman_rank([FA[i] for i in te_i],
                                [rho_all[i] for i in te_i])
        check("G52-map-census", True,
              "MAP census: Spearman(F_A, rho_2) over the %d test "
              "rungs = %+.2f (census, no gate bar -- the "
              "envelope, not the bulk correlation, is the sealed "
              "object); ladder F_A max %.2f at kz%d"
              % (len(te_i), sp_test, max(FA),
                 srt321[int(np.argmax(FA))]["kz"]))
        env_bins, env_decl = upper_envelope(FA, rho_all, te_i)
        env_vals = [e[1] for e in env_bins]
        sp_env = spearman_rank(range(len(env_vals)), env_vals)
        env_argmax = int(np.argmax(env_vals))
        env_ok = (env_argmax == len(env_vals) - 1
                  and sp_env >= ENV_RC_MIN
                  and env_decl == tuple(te_i))
        check("G53-envelope-census", env_decl == tuple(te_i),
              "sealed upper envelope on the DECLARED test set "
              "(ward EXACT): bins (F_med, max rho_2) = %s; "
              "argmax bin %d/%d %s top; bin Spearman %+.3f %s "
              "%.1f -> ENV_%s"
              % (str([(round(a, 2), round(b, 4))
                      for a, b in env_bins]), env_argmax,
                 len(env_vals) - 1,
                 "==" if env_argmax == len(env_vals) - 1
                 else "!=", sp_env,
                 ">=" if sp_env >= ENV_RC_MIN else "<",
                 ENV_RC_MIN, "OK" if env_ok else "DIFFUSE"))
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n321):
                if srt321[i]["kz"] == kz:
                    named_rank[kz] = i
        viols = {}
        named_ok = {}
        for f in G_FORMS:
            viols[f] = [i for i in te_i
                        if rho_all[i] > gvals[f][i]]
            named_ok[f] = all(
                rho_all[named_rank[kz]]
                <= gvals[f][named_rank[kz]] for kz in NAMED_KZ)
        winner = None
        for f in G_FORMS:
            if monos[f] <= TOY_BAR and not viols[f] \
                    and named_ok[f]:
                winner = f
                break
        check("G54-certification", True,
              "per-form certification (census; adjudicated in "
              "S7): violations on the %d test rungs SQ %d / TT "
              "%d / LIN %d %s; named coverage kz53/kz83/kz67/"
              "kz55: %s; WINNER by sealed precedence (SQ > TT > "
              "LIN): %s"
              % (len(te_i), len(viols["SQ"]), len(viols["TT"]),
                 len(viols["LIN"]),
                 str({f: [srt321[i]["kz"] for i in viols[f]]
                      for f in G_FORMS if viols[f]}),
                 str({f: "%d/4" % sum(
                     1 for kz in NAMED_KZ
                     if rho_all[named_rank[kz]]
                     <= gvals[f][named_rank[kz]])
                     for f in G_FORMS}),
                 winner if winner else "NONE"))
        wf = winner if winner else G_FORMS[0]
        rsv = [gvals[wf][i] / max(rho_all[i], 1e-300)
               for i in te_i]
        NsT = [srt321[i]["N"] for i in te_i]
        sl_r = L2D.halves_slope(
            NsT, [max(rho_all[i] / max(gvals[wf][i], 1e-300),
                      1e-300) for i in te_i])
        named_note = "; ".join(
            "kz%d rho %.4f g %.4f rsv %.1f"
            % (kz, rho_all[named_rank[kz]],
               gvals[wf][named_rank[kz]],
               gvals[wf][named_rank[kz]]
               / max(rho_all[named_rank[kz]], 1e-300))
            for kz in NAMED_KZ)
        check("G55-reserve-trend", True,
              "reserve census at the %s form: min/med over test "
              "%.2f/%.2f; trend of rho_2/g(F_A) %+.3f (falling "
              "= growing reserve); the four named r316/r317 "
              "violators: %s"
              % (wf, min(rsv), float(np.median(rsv)), sl_r,
                 named_note))

    # ---------------- S6: Leg C -- structure + world
    section("S6  LEG C -- STRUCTURE (B census) + WORLD CHECK")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    m9 = ev9m["m"]
    # SCRAMBLE class rejection machinery (r317 verbatim)
    evS = crecs["SCR"]["ev"]
    comp_ref = recs
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
        check("G60-structure-census", True, "SMOKE: skipped")
        check("G61-world-admission", True, "SMOKE: skipped")
        check("G62-scramble-mechanism", shuf_ok and attr_ok,
              "SMOKE (w9-based): attribution %s dev %.2f; "
              "shuffle %d mism, edge break %.1e, mass %.1e"
              % (cause.upper(), devsS[cause], mism_s, edev,
                 mass_dev))
        world_ok = attr_ok and shuf_ok
    else:
        B_cal_max = max(Bcol[i] for i in ca_i)
        B_test_max = max(Bcol[i] for i in te_i)
        sl_B = L2D.halves_slope(
            NsT, [max(Bcol[i], 1e-300) for i in te_i])
        check("G60-structure-census", True,
              "THE UPPER-DIRECTION CARRIER (exact bracket rho_2 "
              "<= F_A^2 x B^2, warded in G42): B = medloc x "
              "m/log m is SOURCE-PURE (QMAX column + rank order "
              "+ m only) and spike-robust (local median); ladder "
              "min/med/max %.4f/%.4f/%.4f; CAL MAX %.4f vs TEST "
              "MAX %.4f -> %s on the measured ladder (ratio "
              "%.2f); trend over test %+.3f -- the transfer "
              "question 'is B mid-ladder bounded' has this "
              "measured answer, and it is the G_SQ certification "
              "by algebra"
              % (min(Bcol), float(np.median(Bcol)), max(Bcol),
                 B_cal_max, B_test_max,
                 "BOUNDED" if B_test_max <= B_cal_max
                 else "NOT bounded", B_test_max / B_cal_max,
                 sl_B))
        # world admission at the sliding bound (insertion rule)
        ladder_Ns = [rc["N"] for rc in srt321]
        wnote = []
        adm_ok = True
        for nm, wrc in (("w9", mrecs[0]), ("w13(twin)", mrecs[1]),
                        ("EPSTEIN", crecs["EPST"])):
            ev = wrc["ev"]
            f_ins = world_coord(ev["trs"]["qmax"], wrc["N"],
                                ladder_Ns, qmax_col)
            gw = g_eval(wf, pars[wf], f_ins)
            adm = (ev["mx_mult"] <= MULT_CAP
                   and ev["rho2"] <= gw)
            adm_ok = adm_ok and adm
            wnote.append("%s mult %d rho2 %.3f %s g(%.2f) = %.2f"
                         % (nm, ev["mx_mult"], ev["rho2"],
                            "<=" if ev["rho2"] <= gw else ">",
                            f_ins, gw))
        tw_fac = max(mrecs[1]["ev"]["trs"]["phiL2"]
                     / max(mrecs[0]["ev"]["trs"]["phiL2"],
                           1e-300),
                     mrecs[0]["ev"]["trs"]["phiL2"]
                     / max(mrecs[1]["ev"]["trs"]["phiL2"],
                           1e-300))
        twin_ok = tw_fac <= TWIN_FAC
        f_scr = world_coord(evS["trs"]["qmax"], crecs["SCR"]["N"],
                            ladder_Ns, qmax_col)
        g_scr = g_eval(wf, pars[wf], f_scr)
        coord_break = evS["rho2"] > g_scr
        class_reject = attr_ok and shuf_ok
        scr_ok = coord_break or class_reject
        world_ok = adm_ok and twin_ok and scr_ok
        check("G61-world-admission", True,
              "WORLD census at the %s sliding bound (insertion-"
              "rule coordinates, adjudicated in S7): %s; twin "
              "band PhiL2 factor %.2f %s %.1f"
              % (wf, "; ".join(wnote), tw_fac,
                 "<=" if twin_ok else ">", TWIN_FAC))
        check("G62-scramble-mechanism", scr_ok,
              "SCRAMBLE mechanism (honestly documented): "
              "coordinate bound %s (rho2 %.3f %s g(%.2f) = %.3f "
              "-- %s) AND class rejection %s (attribution %s "
              "dev %.2f >= %.2f; seeded shuffle %d edgewise "
              "%.1e mass %.1e, %d/%d atoms) -> scr_ok = %s"
              % ("BREAKS" if coord_break else "holds",
                 evS["rho2"], ">" if coord_break else "<=",
                 f_scr, g_scr,
                 "the sliding-bound-native rejection"
                 if coord_break else
                 "the coordinate does NOT reject it",
                 class_reject, cause.upper(), devsS[cause],
                 ATTR_MIN, SEED_SHUF, edev, mass_dev, mism_s,
                 len(ev9m["pos_all"]), scr_ok))

    # ---------------- S7: Leg D -- adjudication + theorem
    section("S7  LEG D -- SEALED ADJUDICATION + THEOREM "
            "CANDIDATE")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-theorem-candidate", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        F_max = max(FA)
        F_min_te = min(FA[i] for i in te_i)
        if winner:
            gain = g_eval(winner, pars[winner], F_max) \
                / max(g_eval(winner, pars[winner], F_min_te),
                      1e-300)
        else:
            gain = 0.0
        gain_ok = gain >= GAIN_MIN
        vkey = gate_verdict(winner is not None, world_ok,
                            env_ok, gain_ok)
        if vkey == "SLIDING_BOUND_GO":
            C_impl = g_eval(winner, pars[winner], F_max)
            verdict_main = ("SLIDING_BOUND_GO(%s: rho_2 <= "
                            "%s on 0/%d test violations + 4/4 "
                            "named; gain %.2f >= %.1f; ENV_OK; "
                            "world clean)"
                            % (winner,
                               ("%.4f x F_A^2" % pars["SQ"][0])
                               if winner == "SQ" else
                               ("%.4f + %.5f x F_A^3"
                                % pars["TT"]) if winner == "TT"
                               else "%.4f x F_A" % pars["LIN"][0],
                               len(te_i), gain, GAIN_MIN))
        elif vkey == "WORLD_LEAK":
            C_impl = 0.0
            verdict_main = ("WORLD_LEAK(adm %s twin %s scr %s)"
                            % (adm_ok, twin_ok, scr_ok))
        elif vkey == "G_FAILS_POINTWISE":
            C_impl = 0.0
            verdict_main = ("G_FAILS_POINTWISE(envelope monotone "
                            "but every sealed form misses: viol "
                            "SQ %d / TT %d / LIN %d)"
                            % (len(viols["SQ"]), len(viols["TT"]),
                               len(viols["LIN"])))
        else:
            C_impl = 0.0
            reasons = []
            if winner is None:
                reasons.append("no certifying form + envelope "
                               "diffuse")
            else:
                if not env_ok:
                    reasons.append("envelope diffuse (argmax %d, "
                                   "Spearman %+.2f)"
                                   % (env_argmax, sp_env))
                if not gain_ok:
                    reasons.append("gain %.2f < %.1f (disguised "
                                   "flat constant)"
                                   % (gain, GAIN_MIN))
            verdict_main = ("ENVELOPE_DIFFUSE(%s)"
                            % "; ".join(reasons))
        check("G70-adjudication", True,
              "exactly one sealed verdict fired: %s"
              % verdict_main)
        if vkey == "SLIDING_BOUND_GO":
            C_tot = max(C_impl, C_small)
            info("CANDIDATE THEOREM (sliding cubic bound; "
                 "measured on the %d-rung class ladder; status "
                 "SLIDING_BOUND_GO):" % n321)
            info("  Every class rung w (edge-masked, fold "
                 "multiplicity <= %d, POSITIVE_PREFIX) with m >= "
                 "%d satisfies" % (MULT_CAP, m0))
            info("    sum_j q_j^3  <=  g(F_A(w)) x (log m)^2 / "
                 "m^2   with   g(F) = %s,"
                 % (("%.4f x F^2" % pars["SQ"][0])
                    if winner == "SQ" else
                    ("%.4f + %.5f x F^3" % pars["TT"])
                    if winner == "TT" else
                    "%.4f x F" % pars["LIN"][0]))
            info("  F_A = the r317 rank-local QMAX ratio "
                 "(source-pure, W = %d, computable in advance); "
                 "g explicit, MONOTONE, mid-ladder frozen; the "
                 "%d rungs with m < %d are certified "
                 "individually (C_small = %.4f); the four named "
                 "r316/r317 violators are INSIDE the sliding "
                 "bound (the point of the gliding form)."
                 % (EFP.CLS_W, len(sm_i), m0, C_small))
            info("  COROLLARY (uniform bound): F_A <= %.2f "
                 "measured on the ladder, hence sum q^3 <= "
                 "C_impl x (log m)^2/m^2 with C_impl = g(%.2f) "
                 "= %.2f (C_tot = %.2f incl. small-m; n_eff = "
                 "N_2 >= N_3 >= m/(%.2f log m) by the r306 "
                 "exact chain).  DISCLOSED: C_impl is %.1fx "
                 "looser than the r306 first-5 constant -- the "
                 "round buys FORM (one gliding bound, no "
                 "regimes, no exceptions), not sharpness."
                 % (F_max, F_max, C_impl, C_tot,
                    math.sqrt(C_tot), C_impl / C2))
            info("  THE NEW SMALLER PROVENANCE QUESTION: is F_A "
                 "source-pure bounded%s?  Both are questions "
                 "about the LOCAL MEDIAN of the QMAX column -- "
                 "no cubic target appears in either."
                 % (" (and, for the G_SQ chain, is B = medloc x "
                    "m/log m bounded -- measured: cal max %.4f, "
                    "test max %.4f, trend %+.3f)"
                    % (B_cal_max, B_test_max, sl_B)
                    if winner == "SQ" else ""))
            check("G71-theorem-candidate", True,
                  "sliding theorem candidate printed with "
                  "explicit (g = %s, m_0 %d, C_small %.4f, "
                  "C_impl %.2f, C_tot %.2f, gain %.2f)"
                  % (winner, m0, C_small, C_impl, C_tot, gain))
        else:
            check("G71-theorem-candidate", True,
                  "no theorem candidate printed (the sealed "
                  "tree fired %s); the map, envelope and "
                  "structure censuses stand as the round's "
                  "record data" % vkey)

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    toy_Fm = (1.0, 1.0, 1.0, 1.0)
    toy_rm = (1.0, 1.0, 1.0, 5.0)
    a_mut = mutant_g_posthoc(toy_Fm, toy_rm)
    parW, _dw = g_calibrate("LIN", toy_Fm, toy_rm, toy_Fm,
                            (0, 1))
    check("G80-e1-g-posthoc",
          len(e1_hits) >= 1
          and abs(a_mut - parW[0]) >= MUT_MIN,
          "e1 CAUGHT twice: the after-sight re-calibration "
          "consumes the evaluated bound column over the whole "
          "ladder -- AST-FLAGGED (%s) -- and on the sealed toy "
          "it returns %.1f != the frozen first-2 calibration "
          "%.1f (diff %.1f >= %.0e); the real constants are "
          "frozen on the declared mid-ladder window only"
          % (e1_hits[0] if e1_hits else "MISS", a_mut, parW[0],
             abs(a_mut - parW[0]), MUT_MIN))
    check("G81-e2-coord-readback",
          len(e2_hits) >= 1 and (not sc_own),
          "e2 AST-CAUGHT: the 'coordinate' consuming the cubic-"
          "moment record (cm/S3) is FLAGGED (%s) while the six "
          "module-own builders are clean (%d hits) -- the "
          "source-purity of the coordinate is machine-audited"
          % (e2_hits[0] if e2_hits else "MISS", len(sc_own)))
    toy_Fi = tuple(float(k) for k in range(1, 13))
    toy_vi = tuple(float(k) for k in range(1, 13))
    te_toy = tuple(range(6, 12))
    ca_toy = tuple(range(0, 6))
    _envR, dclR = upper_envelope(toy_Fi, toy_vi, te_toy)
    _envM, dclM = mutant_envelope_cal(toy_Fi, toy_vi, ca_toy)
    check("G82-e3-envelope-cal",
          dclR == te_toy and dclM == ca_toy and dclM != te_toy,
          "e3 CAUGHT: the mutant envelope declares the "
          "calibration window %s != the test set %s (declared-"
          "set ward EXACT); the real envelope declares the test "
          "set EXACT -- evaluating the envelope in-sample is "
          "structurally refused"
          % (str(dclM), str(te_toy)))
    worst_mut = 0.0
    prev = None
    for f in GRID_MONO:
        v = mutant_g_nonmono(1.0, f)
        if prev is not None:
            worst_mut = max(worst_mut, prev - v)
        prev = v
    ok_seal_mono = all(
        mono_check(fm, pr) <= TOY_BAR
        for fm, pr in (("SQ", (2.25,)), ("TT", (2.25, 0.21875)),
                       ("LIN", (2.0,))))
    check("G83-e4-monotonicity-break",
          worst_mut >= MUT_MIN and ok_seal_mono,
          "e4 LOUD: the non-monotone mutant g = p F (2 - F) "
          "shows a worst grid decrease %.4f >= %.0e while all "
          "three sealed forms pass the same grid (<= %.0e) -- "
          "a monotonicity break cannot slip through the sealed "
          "check" % (worst_mut, MUT_MIN, TOY_BAR))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed continuous-coordinate statement form "
          "(monotone g of the r317 F_A import), the exact "
          "concentration bracket qmax PhiH1 <= rho_2 <= PhiH1 = "
          "(F_A B)^2 with the source-pure baseline B, the sealed "
          "three-form g-family with mid-ladder calibration, the "
          "fit-free envelope rule and the sliding-bound world "
          "check -- NO new certificate promoted, NO universal "
          "bound claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R321_ANCHORS(shares %+.4f/%+.4f/%+.4f, FC "
                 "%.3f/%+.3f, mult 2 on %d/%d, identity %.1e, "
                 "r306 C2 %.3f viol %d/57, r315 C0 "
                 "%.4f/%.4f/%.4f, r316 n %d H %s C_L2 %.4f "
                 "C_small %.4f, r317 top3 %s thrB %.4f C_gen "
                 "%.4f viol %s)"
                 % (meds[0], meds[1], meds[2], fc_med, fc_sl,
                    n_m2, n321, rec3_w, C2, viol2, C0["a"],
                    C0["b"], C0["c"], n321, str(h_kz), CL2,
                    C_small316, str(top3_kz), thrB, C_gen,
                    str(viol_gen))]
        parts.append("SEAL(coordinate import W %d, bracket "
                     "%.1e, purity clean, toys exact)"
                     % (EFP.CLS_W, brk_low))
        parts.append("MAP(Spearman %+.2f, env %s, ENV_%s)"
                     % (sp_test,
                        str([round(b, 3) for b in env_vals]),
                        "OK" if env_ok else "DIFFUSE"))
        parts.append("GFAMILY(SQ b %.4f viol %d, TT (%.4f, "
                     "%.5f) viol %d, LIN a %.4f viol %d, "
                     "winner %s, reserve %.2f/%.2f, trend "
                     "%+.3f)"
                     % (pars["SQ"][0], len(viols["SQ"]),
                        pars["TT"][0], pars["TT"][1],
                        len(viols["TT"]), pars["LIN"][0],
                        len(viols["LIN"]),
                        winner if winner else "NONE",
                        min(rsv), float(np.median(rsv)), sl_r))
        parts.append("STRUCTURE(B cal max %.4f test max %.4f "
                     "%s, trend %+.3f)"
                     % (B_cal_max, B_test_max,
                        "BOUNDED" if B_test_max <= B_cal_max
                        else "NOT-BOUNDED", sl_B))
        parts.append("WORLD(adm %s, twin %.2f, SCR coord %s + "
                     "class %s)"
                     % (adm_ok, tw_fac,
                        "BREAK" if coord_break else "hold",
                        class_reject))
        parts.append(verdict_main)
        parts.append("THEOREM(%s)"
                     % ("printed" if vkey == "SLIDING_BOUND_GO"
                        else "not printed"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the concentration "
          "bracket, the reconstruction identity, the g "
          "monotonicity, the tree logic and the purity audits "
          "(exact / AST-decided); MEASURED: every constant, "
          "violation count, envelope bin, reserve, trend and "
          "census (the finite class ladder + 2 mains + 2 live "
          "controls); OPEN: any bound beyond the measured "
          "rungs, the cofinal law, the boundedness of F_A and "
          "B beyond the ladder, kz15 beyond r270; NO RH claim"
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


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'coordinate orientation' consuming
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'coordinate constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


if __name__ == "__main__":
    sys.exit(main())
