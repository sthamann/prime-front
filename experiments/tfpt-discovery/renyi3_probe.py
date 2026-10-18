#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""renyi3_probe -- PRIME.L2.ATOM.RENYI3.01 (round 306): the
POINTWISE CUBIC MOMENT THEOREM TEST -- prove or refute a pointwise
polylogarithmic upper bound for the cubic normalized moment of the
atomic |PDelta| profile:

    S_3 := sum_j q_j^3  <=  C x (log m)^A / m^2      (every rung)

with q_j = a_j / sum_k a_k, a_j = |PDelta|_j over the m constructive
level-2 position blocks, PREREGISTERED constants (A in {0, 1, 2}; C
calibrated on the FIRST 5 rungs of the (N, kz)-sorted ladder and
then FROZEN -- calibration/test split disclosed).  By the exact
Renyi/Hill monotonicity N_2 >= N_3 (power-mean chain, Leg A) the
bound implies N_3 = S_3^(-1/2) >= m / (sqrt(C) (log m)^(A/2)) and
hence N_2 = n_eff >= the same bound -- asymptotically beating every
demanded power m^0.888.  Context (sealed record inputs): r301 (SPEC
6f8cc404) measured the Renyi family N_2/N_3/N_4/N_inf med
37.41/27.88/24.04/15.47 slopes +0.963/+0.926/+0.894/+0.738; r303
(SPEC c37d478d) proved the cascade r297->r302 is a DICTIONARY
around ONE core slack S = sigma* - sl_D = +0.0547 and closed the
max-/discrepancy routes; r304 closed the global-profile mixing
route (period-4 comb).  Reviewer adjudication (binding): slope
targets are NOT natural end statements -- the theorem-shaped
successor must be POINTWISE; the Renyi-3 route is the sharpest new
fiber attack (pointwise, source-pure, no maximum, no star
discrepancy, cubic moments expand over local triple configurations,
Renyi monotonicity is immediately Lean-ready).  kz15 permanently
closed via r270; the 6 exceptions via the r287 F2 certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r287/r297-r301 machinery imported verbatim):
t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F = 0.20 edge
split; maximal same-sign runs of the bx-sorted bulk; level-2 blocks
(r270 convention); the frozen positional block machinery (r298
WBT.block_breaks + WBT.aggregate_blocks), the r300
DTP.participation + DTP.shared_delta, the r301
NTP.participation_orders + NTP.quasi_uniformity + NTP.dc_profile,
ALL imported verbatim; PDelta = Pbeta - Pomega; the round's central
quantity is the CUBIC NORMALIZED MOMENT S_3 of the ONE positive
field |PDelta| against the preregistered polylog/m^2 bound family,
judged POINTWISE on every rung.

LEG 0 -- ANCHOR REGRESSION (r297/r299/r300/r301/r303 record numbers
adopted as-is, disclosed): sigma* -0.516, sl_c2 +0.196, sl_pref
+0.489 (tol 0.01); sl_D -0.571 (tol 0.01); Renyi family meds
37.41/27.88/24.04/15.47 (tol 0.05) slopes
+0.963/+0.926/+0.894/+0.738 (tol 0.01); n_act med 73.0 (tol 0.5)
sl_nact +1.002 (tol 0.01), COUNT LINK n_act == m on 42/42 EXACT;
n_eff_atom med 118.0 (tol 1.0) slope +0.942 (tol 0.01); the r303
margin chain: S = sigma* - sl_D = +0.0547 (tol 0.005) with the
dictionary invariance |m_NEFF - m_D| <= 1e-9 (exact halves_slope
log-additivity over the r300 product identity); the r303
marginal-functional fact re-warded live: S_3 and n_eff_atom are
PURE MARGINAL functionals (sort-invariance <= 1e-12 rel on every
world -- the mixing structure cannot move them).

LEG A -- EXACT ALGEBRA (module-own, Fractions):
(A1) RENYI/HILL MONOTONICITY as an exact finite theorem via two
  LAGRANGE IDENTITIES on rational probability vectors q (sum q = 1):
      sum_{i,j} q_i q_j (q_i - q_j)^2        == 2 (S_1 S_3 - S_2^2)
      sum_{i,j} q_i^2 q_j^2 (q_i - q_j)^2    == 2 (S_2 S_4 - S_3^2)
  (both sides EXACT in Fractions, dev 0) => S_2^2 <= S_3 and
  S_3^2 <= S_2 S_4; composed EXACTLY: S_3^4 <= S_2^2 S_4^2
  <= S_3 S_4^2 => S_3^3 <= S_4^2; hence N_2 = 1/S_2 >= N_3 =
  S_3^(-1/2) >= N_4 = S_4^(-1/3), with EQUALITY exactly on the
  uniform vector (gated on the uniform toy).  Float wards on all
  worlds: max(S_2^2 - S_3, 0)/S_3 <= MONO_BAR and max(S_3^3 -
  S_4^2, 0)/S_4^2 <= MONO_BAR; cross-ward against the r301
  participation_orders mono slack and N_2 == n_eff (rel 1e-12).
(A2) THE BRIDGE INEQUALITY with all constants, exact Fractions
  (rational stand-in L for the positive real (log m)^A, disclosed):
  S_3 <= C L / m^2  =>  N_3^2 = 1/S_3 >= m^2/(C L)  and by (A1)
  N_2^2 = 1/S_2^2 >= 1/S_3 >= m^2/(C L), i.e. n_eff = N_2 >=
  m / sqrt(C L) -- every step verified as an exact rational
  comparison on the toy witness (equality-tight C).
(A3) THE TRIPLE-CONFIGURATION EXPANSION (Newton), exact: with
  e_3 = sum_{i<j<k} q_i q_j q_k,  6 e_3 == 1 - 3 S_2 + 2 S_3, i.e.
      1 == S_3  +  3 (S_2 - S_3)  +  6 e_3
  (diagonal + mixed-pair + strict-triple shares of the cube of the
  total mass) -- Fractions-exact on toys (e_3 by direct triple
  sum), float-warded per rung via an independent prefix-sum
  computation of e_3 (NEWT_BAR).

LEG B -- PREREGISTRATION + MEASUREMENT (the pass bar is an
EXPLICIT INEQUALITY on every rung, NOT a regression):
(B1) SEALED FAMILY: A in A_FAMILY = {0, 1, 2}; rho_A(rung) = S_3
  x m^2 / (log m)^A (natural log; rho_0 is exactly the THIRD SHAPE
  MOMENT M_3 = mean((m q)^3) over the m blocks -- the third-moment
  analog of the r302 stationary second moment m2_inf = 1.973).
  CALIBRATION SPLIT (sealed): the calibration set is EXACTLY the
  first N_CAL = 5 rungs of the (N, kz)-sorted 42-rung ladder;
  C_A = max over the calibration set of rho_A, then FROZEN; the
  test set is the remaining 37 rungs PLUS the extension.
(B2) THE EXTENSION LADDER (r286-aligned, sealed rule): the
  admissible pool core.frame_a_zones() with the window cap lifted,
  900 < h <= EXT_H_MAX = 1300 (enumeration cap, budget-sized),
  sorted by (N, kz) ascending, the FIRST K_EXT = 15 are the
  extension anchors (pre-spec scoping disclosed below: the rule
  admits 20 candidates <= 1300, the first 15 have N_w 942..1218 --
  the same anchors as r286).  Extension rungs join the pointwise
  verdict and the identity/contribution wards (deep bars); they do
  NOT enter the frozen 42-rung anchor slopes; their branch class
  and count link are printed as census (no sealed expectation).
(B3) POINTWISE ADJUDICATION (sealed BEFORE evaluation; exactly one
  fires): HOLD(A) iff rho_A(r) <= C_A on ALL 57 rungs (42 core +
  15 extension; calibration rungs hold by construction, argmax has
  reserve exactly 1 -- disclosed); GROW(A) iff halves_slope(rho_A)
  <= -RES_EPS on the 42 core rungs AND on the 57-rung extended
  ladder (the reserve grows into depth on both frozen estimators);
    RENYI3_GO(C_A*, A*)  iff exists A with HOLD and GROW
                              (A* = smallest such A);
    RENYI3_TIGHT(A')     iff no GO but exists A with HOLD
                              (A' = smallest such A);
    RENYI3_DEAD(rungs)   iff NO A in the family holds -- the
      violating rungs of A = 2 are the counterexample list,
      honestly sealed.
  Reserve census per A: min/med of C_A/rho_A over the 52 test
  rungs; violation count; both trend slopes.  WORLD CONTROLS:
  EPSTEIN and SCRAMBLE (w9-based, one rung each) are tested
  pointwise against the SAME frozen C_A at the verdict's A (tag
  WORLD_BLIND iff both hold, WORLD_SENSITIVE otherwise -- a
  world-blind bound would be BETTER provable); SMOOTH is the known
  degenerate world (Delta == 0 identically): the pre-declared
  guard L1(PDelta) <= DEG_FLOOR x total contribution mass skips
  it, disclosed.
  DISCLOSED ALGEBRAIC PRIORS (no scratch run of this probe): from
  the r301 records slope(rho_0) = 2 sl_nact - 2 sl_N3 ~ +2.004 -
  1.852 = +0.152 > 0 -- A = 0 is EXPECTED to violate a
  first-5-frozen C (the third shape moment grows); the per-A log
  correction to the halves slope is ~ sl_nact / log(m_med) ~
  +1.002/log(73) ~ +0.23, so A = 1 (~ -0.08) and A = 2 (~ -0.31)
  are expected falling; the adjudication rules are sealed
  symmetrically -- no rule was chosen to favor an outcome.

LEG C -- STRUCTURE OF THE CUBIC MOMENT (the pre-stage of a proof):
(C1) MASS LAYERS: dyadic layers L_l = {j : q_j in (2^-(l+1) q_max,
  2^-l q_max]}, l = 0..LAYERS-1 (rest = tail); per rung the S_3
  share and count per layer; census med of the layer-0+1 share
  (few heavy atoms?) and the S_3-weighted mean layer.
(C2) TOP-K ATOMS: share of S_3 carried by the top k = 1 / 3 / 8
  atoms (med + halves slope over the 42 core rungs) -- few heavy
  carriers vs broad contributions, MEASURED.
(C3) TRIPLE CONFIGURATIONS: the exact A3 split (diagonal S_3,
  mixed pairs 3(S_2 - S_3), strict triples 6 e_3) med shares +
  Newton ward per rung; worlds census (EPST/SCR).
(C4) THE MINIMAL STRUCTURE STATEMENT is NAMED from the measured
  anatomy (printed, typed, no upgrade): if the top-8 share is
  small and the layer profile broad, the natural sufficient
  statement is SHAPE3_TARGET -- prove that the third moment M_3 =
  m^2 S_3 of the stationary normalized shape u = m q (r302
  PROFILE_STATIONARY, m2_inf = 1.973) is polylog-bounded; the
  measured M_2 = m S_2 med is printed as the cross-reference.

LEG D -- LEAN PREPARATION (small): the exact Renyi monotonicity +
bridge statement is printed in Lean-ready form (statement text
only; the Lean worker takes over later).

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) POWER-MEAN DIRECTION FLIPPED (exact Fractions): the mutant
  claim S_3 <= S_2^2 on q = (1/2, 1/4, 1/4) breaks by 1/64 EXACT
  (S_3 = 5/32 > S_2^2 = 9/64) -- CAUGHT; the Lagrange witnesses
  are dev-0 on the same vector.
(m2) PREREGISTRATION BREACH (calibration from the whole ladder):
  the mutant computes C from ALL rungs instead of the frozen
  first-5 split -- CAUGHT structurally by the split ward (declared
  calibration index set != frozen set) AND loudly on the toy
  rho-list (1..10): C_mut = 10 != C_cal = 5, diff 5 EXACT; on the
  record ladder the real C_full/C_cal ratio is printed (a growing
  rho_0 makes the breach material, not cosmetic).
(m3) UNNORMALIZED q: using a_j instead of q_j changes the cubic
  moment by the factor L1^3 -- LOUD (rel dev printed, >= MUT_MIN).
(m4) ONE-ATOM SYNTHETIC PROFILE: q = delta_j gives S_2 = S_3 =
  S_4 = 1 EXACT, all N_k == 1 EXACT, and rho_0 = m^2 breaks the
  real w9 cubic moment by a factor >= M4_LOUD_MIN = 100 -- the
  bound MUST break loudly on concentration.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.  Scope hygiene: the new
  builders (cubic_moments, cubic_layers, renyi3_ratio,
  calib_freeze) consume positions + weights only (BOUND_FORBIDDEN
  set); fragment audit (no fit primitives).  TOY EXACTNESS (bar
  1e-14): q = (1/2, 1/4, 1/4): S_2 = 3/8, S_3 = 5/32, S_4 = 9/128,
  slack1 = 1/64, slack2 = 37/32768, e_3 = 1/32, Newton 3/16 ==
  6/32; uniform (1/3, 1/3, 1/3): BOTH slacks 0 EXACT (equality
  case); the float cubic_moments on (2, 1, 1) matches the
  Fractions values.

INDEX FIREWALL (binding, r238-r304 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks, r300 DTP.participation +
DTP.shared_delta, r301 NTP.participation_orders +
NTP.quasi_uniformity + NTP.dc_profile, r269 PBB.mask_edge +
PBB.runs_split + PBB.bound_pairsum, r287 L2D.blocks_level2 +
L2D.bound_vdc + L2D.halves_slope + L2D.autocorr_full, r244
BH.wpack, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B
PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never
fitted).  COFINAL LADDER (pre-sealed): frame-A h <= 900, 42 rungs,
(N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52};
EXTENSION: 900 < h <= 1300, first 15 by (N, kz).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; H rule = max(2, ceil(sqrt(m))) (FROZEN);
A_FAMILY (0, 1, 2); N_CAL 5; RES_EPS 0.01; EXT_H_MAX 1300; K_EXT
15; EXT_NW_EXPECT (942, 1218); MONO_BAR 1e-9; NEWT_BAR 1e-9;
QID_BAR 1e-9; SINV_BAR 1e-12; N2X_BAR 1e-12; PROP_BAR 1e-9;
DEG_FLOOR 1e-6; LAYERS 12; TOPK (1, 3, 8); M4_LOUD_MIN 100;
MUT_MIN 1e-6; TOY_BAR 1e-14; TB_WARD bars 1e-9 main N <= 400 /
3e-6 deep / 1e-6 controls; ID_BAR 1e-12; AC_BAR 1e-9; R297
anchors sigma* -0.516 / sl_c2 +0.196 / sl_pref +0.489 (tol 0.01);
R299_SL_D -0.571 tol 0.01; R301 Renyi meds
37.41/27.88/24.04/15.47 tol 0.05, slopes
+0.963/+0.926/+0.894/+0.738 tol 0.01; R301_NACT_MED 73.0 tol 0.5,
R301_SL_NACT +1.002 tol 0.01; R301_NATOM_MED 118.0 tol 1.0,
R301_SL_NATOM +0.942 tol 0.01; MARGIN_REF +0.0547 tol 0.005;
R302_M2_INF 1.973 (INFO cross-reference only, no gate); runtime
<= 1800 s; smoke = w9 + controls + Fractions section + toys +
scope audits + every exact ward at w9 + the m2 toy breach + m3/m4
mutants; ladder, extension, anchors, slopes, prereg measurement
and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
reproduction band is an r297-r303 RECORD number adopted as-is;
the Lagrange identities, the power-mean chain, the bridge and the
Newton expansion are derived algebra, disclosed above; the B3
priors (slope(rho_0) ~ +0.152 expected positive, per-A log
correction ~ +0.23) are algebraic consequences of the r301
records; ONE pre-spec scoping run (disclosed) enumerated the
extension pool for budget sizing only: 20 candidates with 900 < h
<= 1300, first 15 with N_w 942..1218 (the r286 anchor set), wpack
cost 0.4-1.2 s per deep rung -- no rho, no S_3, no bound value
was computed before this spec was frozen; the adjudication
outcomes are sealed symmetrically.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  RENYI3_ANCHORS(Renyi meds + slopes, margin chain S, count link,
    n_eff_atom, marginal invariance)
+ PREREG(C_0/C_1/C_2 with calibration argmax rungs, split 5|37+15)
+ POINTWISE(per A: violations n/57, min/med reserve over the 52
    test rungs, trend slopes 42/57)
+ [exactly one of] RENYI3_GO(C, A) / RENYI3_TIGHT(A) /
    RENYI3_DEAD(violating rungs at A = 2)
+ ANATOMY(top-1/3/8 S_3 shares med + slope, layer-0+1 share,
    mean layer, triple-config split, M_2/M_3 shape moments)
+ [tag] WORLD_BLIND / WORLD_SENSITIVE(EPST/SCR vs frozen C)
+ LEAN_STMT(printed in Leg D).
Honesty before beauty: the Lagrange identities, the power-mean
chain, the bridge and the Newton split are EXACT finite algebra;
every C_A, reserve, share and slope is MEASURED on 42 + 15 finite
rungs; a GO fixes the new pointwise proof target of the fiber, it
does NOT prove the cofinal law; a DEAD seals the counterexample
honestly; no verdict claims a cofinal law; the exception scalar's
positivity beyond the measured rungs stays OPEN; r243-r304 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = crashed at G96 with a format-string TypeError (25
gates printed PASS before the crash) -- a pure PRINT-FORMAT fix
(one missing argument), no bar, band, rule or verdict rule
touched; smoke pass 2 = 27/27 (0.2 s); calibration pass 1 = first
full evaluation, 25/27 -- G83 FAILED because the m3/m4 mutant
reference used the smallest ladder rung instead of the sealed
spec's "real w9"; the code was aligned to the spec (mrecs[0] =
w9), the sealed M4_LOUD_MIN = 100 unchanged (G96 was the pass
cascade); calibration pass 2 = 27/27, wall 23.8 s, NO further
amendment; record run1/run2 after this insertion, identical up to
WALL; the only post-freeze edits are the two disclosed code-side
fixes and this record-table insertion, which IS the protocol):
CAL_VERDICT = RENYI3_ANCHORS(Renyi meds 37.41/27.88/24.04/15.47
slopes +0.963/+0.926/+0.894/+0.738 bit-near r301; S = sigma* -
sl_D = +0.0547 with dictionary invariance 6.7e-16; COUNT LINK
n_act == m on 42/42 AND on the 15 extension anchors 15/15;
n_eff_atom 118.0 / +0.942; marginal invariance <= 8.7e-16) +
PREREG(C_0 11.875 / C_1 3.564 / C_2 1.069, ALL three at rung 0
(kz18, N 142) -- the calibration maximum is the SHALLOWEST rung;
split 5 | 37 + 15) + POINTWISE(A = 0: 3/57 violations (kz53 rho
23.97, kz67 24.89, kz76 11.93 EXT), reserve min/med 0.48/1.97,
trend +0.153/+0.128 RISES -- the bare third shape moment is NOT
pointwise bounded by its shallow maximum; A = 1: 2/57 violations
(kz53 5.02, kz67 5.12 > C_1 3.564), reserve 0.70/2.91, trend
-0.084/-0.097 falls; A = 2: 0/57 VIOLATIONS, reserve min/med
1.01/4.06, trend -0.322/-0.322 falls on BOTH estimators) +
RENYI3_GO(C = 1.069, A = 2) -- the preregistered inequality
    sum_j q_j^3 <= 1.069 x (log m)^2 / m^2
HOLDS POINTWISE on every one of the 42 + 15 rungs with falling
rho (growing reserve); via the exact chain this fixes the NEW
POINTWISE PROOF TARGET of the fiber: n_eff = N_2 >= N_3 >=
m/(1.034 x log m) -- asymptotically above every demanded power
m^0.888 + ANATOMY(top-1/3/8 S_3 shares med 0.256/0.512/0.780
slopes -0.363/-0.353/-0.268 -- the carriers BROADEN with depth,
no heavy-few obstruction; layer-0+1 share 0.974 with mean layer
0.25 -- the cubic mass lives within a factor 4 of q_max: a
NARROW-BAND profile, not a heavy tail; triple-config split med
S_3 0.13 percent / pairs 7.6 percent / strict triples 92.2
percent; shape moments M_2 med 2.03 (r302 m2_inf 1.973), M_3 med
5.81; SHAPE3_TARGET named as the minimal sufficient statement) +
WORLD_SENSITIVE(at A = 2: EPSTEIN rho 0.368 <= C HOLDS, SCRAMBLE
rho 1.780 > C VIOLATES by 1.67x -- scrambling the comb BREAKS the
bound: the pointwise cubic law is a structural property of the
real recursion profile, not of block combinatorics; SMOOTH
skipped by the pre-declared DEG_FLOOR guard) + LEAN_STMT(printed).
Key numbers.  S2: contribution ward 2.1e-13 main / 3.9e-13 deep /
4.9e-13 ext / 2.4e-8 controls; block + autocorr identities worst
6.3e-16 / 3.0e-15 on 62 worlds; cubic identity wards: power-mean
slacks 0.0 EXACT on 61 live worlds, Newton prefix 1.0e-15, S_3 /
n_eff_atom sort-invariance 2.9e-16 / 8.7e-16, N_2 == n_eff
3.8e-16.  S1: extension census 15 anchors N_w 942..1218 (the
r286 set), POSITIVE_PREFIX 15/15, branch census 12 cheap / 3
exception (kz109, kz57, kz97).  S5: the rho_2 profile falls
7.5x from C_2 = 1.069 (rung 0) to 0.186 (kz41, N 1218); the two
near-critical rungs kz53 (1.049) and kz67 (1.054) sit 1.4-1.9
percent under C_2 -- the SAME two rungs are the A <= 1 killers;
the deepest 15 rungs (the whole extension) hold with reserve
2.6..5.7.  S8: m1 break 1/64 EXACT; m2 toy diff 5 EXACT + real
C_full/C_cal 2.10/1.44/1.00 (A = 0 argmax rung 35 = kz67 outside
the split -- the breach is material exactly where the bound is
tight); m3 rel dev 9.3e-1 (L1^3 = 6.6e-2); m4 S_3 = 1 EXACT,
212 x the real w9 cubic moment; m5a/m5b FLAGGED.
READING (typed, no upgrade): the round DELIVERS the first
pointwise theorem-shaped statement of the fiber since the r303
dictionary adjudication: (1) RENYI3_GO -- the cubic normalized
moment of the atomic |PDelta| profile obeys S_3 <= 1.069 (log
m)^2/m^2 on EVERY one of the 57 measured rungs (42 core + the 15
r286 extension anchors), with the reserve GROWING into depth
(trend -0.322 on both frozen estimators, deepest 15 rungs at
reserve 2.6..5.7): the pointwise successor statement demanded by
the reviewer adjudication exists and is measured, not fitted;
(2) the polylog exponent is REAL: A = 0 fails (the third shape
moment itself rises +0.153 before decaying -- exactly the
disclosed algebraic prior) and A = 1 fails on precisely the two
near-critical rungs kz53/kz67; A = 2 is the smallest
preregistered exponent that clears the whole ladder -- the honest
form of the target is polylog-squared, and the same two rungs
are the sharpness witnesses; (3) the ANATOMY is the friendliest
possible: the cubic mass is a NARROW-BAND functional (97 percent
within a factor 4 of q_max) carried ever more BROADLY (top-8
share 0.780 falling at -0.268), and strict triples carry 92
percent of the cube -- no heavy-few obstruction stands between
the measured bound and a proof; the minimal sufficient statement
is SHAPE3_TARGET (M_3 = m^2 S_3 polylog-bounded, the third-moment
sibling of the r302-PROVEN M_2 stationarity 1.973 -- M_2 med here
2.03); (4) the world census carries the right sign: EPSTEIN holds
the bound, SCRAMBLE BREAKS it by 1.67x -- the law is recursion
structure, destroyed by scrambling, NOT block combinatorics: a
world-separating (not world-blind) pointwise law, the first of
the lane; (5) the exact algebra is banked Lean-ready: the two
Lagrange witnesses close the Renyi/Hill chain N_2 >= N_3 >= N_4
in pure Fractions, and the bridge n_eff >= m/(sqrt(C) log m) is
rational algebra given the bound.  Honest negatives: C_2 was
frozen on the SHALLOWEST rung and the margin at kz53/kz67 is
1.4-1.9 percent -- a single mid-ladder outlier of the kz53/kz67
type at greater depth would kill the constant (the trend says it
should not exist, but the trend is measured, not proved); the
GO fixes a proof TARGET, it proves nothing beyond the 57 rungs;
n_eff_atom (dc level, 118/+0.942) is NOT bounded by this block
statement -- the atom-level sibling stays unformalized.  Runtime
23.8 s full / 0.2 s smoke; run1/run2 identical up to WALL.
AMENDMENTS AFTER FREEZE: the two disclosed code-side fixes above
(print format; mutant reference aligned to the spec's w9); no
bar, band, rule or verdict rule moved.

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
A_FAMILY = (0, 1, 2)
N_CAL = 5
RES_EPS = 0.01
EXT_H_MAX = 1300
K_EXT = 15
EXT_NW_EXPECT = (942, 1218)
MONO_BAR = 1e-9
NEWT_BAR = 1e-9
QID_BAR = 1e-9
SINV_BAR = 1e-12
N2X_BAR = 1e-12
PROP_BAR = 1e-9
DEG_FLOOR = 1e-6
LAYERS = 12
TOPK = (1, 3, 8)
M4_LOUD_MIN = 100.0
MUT_MIN = 1e-6
TOY_BAR = 1e-14
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
R297_SIGMA_STAR = -0.516
R297_SL_C2 = 0.196
R297_SL_PREF = 0.489
R297_TOL = 0.01
R299_SL_D = -0.571
R299_SL_D_TOL = 0.01
R301_RENYI_MEDS = (37.41, 27.88, 24.04, 15.47)
R301_RENYI_MED_TOL = 0.05
R301_RENYI_SLOPES = (0.963, 0.926, 0.894, 0.738)
R301_RENYI_SL_TOL = 0.01
R301_NACT_MED = 73.0
R301_NACT_TOL = 0.5
R301_SL_NACT = 1.002
R301_SL_NACT_TOL = 0.01
R301_NATOM_MED = 118.0
R301_NATOM_TOL = 1.0
R301_SL_NATOM = 0.942
R301_SL_NATOM_TOL = 0.01
MARGIN_REF = 0.0547
MARGIN_TOL = 0.005
R302_M2_INF = 1.973

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


# ---------------- module-own builders.  Source-pure: block
# ---------------- vectors (positions, weights) only; the withheld
# ---------------- terminal drive key, the branch label and every
# ---------------- target-side identifier are forbidden in scope
# ---------------- (AST audit).
def cubic_moments(P):
    """the cubic-moment coordinates of the ONE positive field |P|:
    q_j = |P_j|/L1, power sums S_2/S_3/S_4, the Renyi numbers
    N_2/N_3/N_4, the power-mean chain slacks (must be <= 0 up to
    float: S_2^2 - S_3 and S_3^3 - S_4^2), the Newton triple ward
    (6 e_3 == 1 - 3 S_2 + 2 S_3 with e_3 from an independent
    prefix-sum computation), and the sort-invariance dev of S_3
    (marginal-functional ward)."""
    a = np.abs(np.asarray(P, dtype=float))
    L1 = float(np.sum(a))
    if L1 <= 0.0:
        return dict(L1=0.0, S2=1.0, S3=1.0, S4=1.0, N2=1.0, N3=1.0,
                    N4=1.0, mono1=0.0, mono2=0.0, newt=0.0,
                    sinv=0.0, degenerate=True)
    q = a / L1
    S2 = float(np.sum(q ** 2))
    S3 = float(np.sum(q ** 3))
    S4 = float(np.sum(q ** 4))
    N2 = 1.0 / max(S2, 1e-300)
    N3 = 1.0 / max(math.sqrt(S3), 1e-300)
    N4 = 1.0 / max(S4 ** (1.0 / 3.0), 1e-300)
    mono1 = max(S2 * S2 - S3, 0.0) / max(S3, 1e-300)
    mono2 = max(S3 ** 3 - S4 * S4, 0.0) / max(S4 * S4, 1e-300)
    # independent prefix-sum e_3: e_3 = sum_k q_k * e_2(q_{<k})
    qs = np.sort(q[q > 0.0])
    c1 = np.concatenate([[0.0], np.cumsum(qs)[:-1]])
    c2 = np.concatenate([[0.0], np.cumsum(qs ** 2)[:-1]])
    e3_pref = float(np.sum(qs * (c1 * c1 - c2) * 0.5))
    newt = abs(6.0 * e3_pref - (1.0 - 3.0 * S2 + 2.0 * S3))
    S3_s = float(np.sum(np.sort(q) ** 3))
    sinv = abs(S3_s - S3) / max(S3, 1e-300)
    return dict(L1=L1, S2=S2, S3=S3, S4=S4, N2=N2, N3=N3, N4=N4,
                mono1=mono1, mono2=mono2, newt=newt, sinv=sinv,
                e3=e3_pref, degenerate=False)


def cubic_layers(P, topk=TOPK, nlayers=LAYERS):
    """the mass-layer / top-k anatomy of the cubic moment: dyadic
    layers relative to q_max (share + count of S_3 per layer), the
    S_3 share of the top-k atoms, the S_3-weighted mean layer."""
    a = np.abs(np.asarray(P, dtype=float))
    L1 = float(np.sum(a))
    if L1 <= 0.0:
        return dict(top={k: 1.0 for k in topk}, lay01=1.0,
                    mean_layer=0.0, n_occ=0)
    q = np.sort(a[a > 0.0] / L1)[::-1]
    S3 = float(np.sum(q ** 3))
    top = {k: float(np.sum(q[:k] ** 3)) / max(S3, 1e-300)
           for k in topk}
    qmax = float(q[0])
    lay = np.minimum(np.floor(np.log2(qmax / q)).astype(int),
                     nlayers)
    s3c = q ** 3 / max(S3, 1e-300)
    lay01 = float(np.sum(s3c[lay <= 1]))
    mean_layer = float(np.sum(lay * s3c))
    n_occ = int(len(np.unique(lay)))
    return dict(top=top, lay01=lay01, mean_layer=mean_layer,
                n_occ=n_occ)


def renyi3_ratio(S3, m, A):
    """rho_A = S_3 x m^2 / (log m)^A -- the preregistered bound
    ratio (natural log; rho_0 is the third shape moment M_3)."""
    return S3 * float(m) * float(m) / (math.log(float(m)) ** A)


def calib_freeze(rhos, cal_idx):
    """C = max of rho over EXACTLY the frozen calibration index
    set; returns (C, argmax index, the declared set) -- the
    declared set is warded against the frozen split (m2 mutant
    must be CAUGHT)."""
    cal = list(cal_idx)
    j = max(cal, key=lambda i: rhos[i])
    return rhos[j], j, tuple(cal)


def mutant_calib_full(rhos):
    """m2 MUST-FAIL MUTANT: preregistration breach -- calibrates C
    on the WHOLE ladder instead of the frozen first-N_CAL split;
    the split ward must CATCH the declared set mismatch."""
    return calib_freeze(rhos, range(len(rhos)))


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'cubic target' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * cubic_moments(P)["S3"]


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'moment constant' that consumes the branch label to pick its
    value -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * cubic_moments(P)["S3"]


# ---------------- exact Fractions section: Lagrange identities,
# ---------------- power-mean chain, Newton split, bridge
def fr_lagrange(qv, wrong="none"):
    """the two Lagrange witnesses + the composed power-mean chain
    on a rational probability vector, EXACT: dev1 = sum q_i q_j
    (q_i - q_j)^2 - 2 (S_1 S_3 - S_2^2), dev2 = the q^2-weighted
    analog - 2 (S_2 S_4 - S_3^2), both must be 0; slack1 = S_3 -
    S_2^2 >= 0, slack2 = S_4^2 - S_3^3 >= 0 (composed exactly via
    S_3^4 <= S_2^2 S_4^2 <= S_3 S_4^2).  wrong='flip' returns the
    mutant slack S_2^2 - S_3 which must be NEGATIVE (CAUGHT)."""
    q = [Fr(x) for x in qv]
    n = len(q)
    S1 = sum(q)
    S2 = sum(x * x for x in q)
    S3 = sum(x ** 3 for x in q)
    S4 = sum(x ** 4 for x in q)
    lag1 = sum(q[i] * q[j] * (q[i] - q[j]) ** 2
               for i in range(n) for j in range(n))
    lag2 = sum(q[i] ** 2 * q[j] ** 2 * (q[i] - q[j]) ** 2
               for i in range(n) for j in range(n))
    dev1 = lag1 - 2 * (S1 * S3 - S2 * S2)
    dev2 = lag2 - 2 * (S2 * S4 - S3 * S3)
    slack1 = S3 - S2 * S2
    slack2 = S4 * S4 - S3 ** 3
    comp_ok = (S3 ** 4 <= S2 * S2 * S4 * S4) \
        and (S2 * S2 * S4 * S4 <= S3 * S4 * S4)
    e3 = sum(q[i] * q[j] * q[k]
             for i in range(n) for j in range(i + 1, n)
             for k in range(j + 1, n))
    newt_dev = 6 * e3 - (1 - 3 * S2 + 2 * S3)
    if wrong == "flip":
        slack1 = S2 * S2 - S3
    return dict(S1=S1, S2=S2, S3=S3, S4=S4, dev1=dev1, dev2=dev2,
                slack1=slack1, slack2=slack2, comp_ok=comp_ok,
                e3=e3, newt_dev=newt_dev)


def fr_bridge():
    """the bridge with all constants, exact rational witness: q =
    (1/2, 1/4, 1/4), m = 3, rational stand-in L = 6/5 for the
    positive real (log m)^A; C chosen equality-tight C = S_3 m^2 /
    L; verify S_3 <= C L / m^2 (equality), N_3^2 = 1/S_3 >=
    m^2/(C L) (equality) and N_2^2 = 1/S_2^2 >= 1/S_3 >= m^2/(C L)
    -- every comparison exact in Fractions."""
    q = [Fr(1, 2), Fr(1, 4), Fr(1, 4)]
    m = Fr(3)
    L = Fr(6, 5)
    S2 = sum(x * x for x in q)
    S3 = sum(x ** 3 for x in q)
    C = S3 * m * m / L
    ok_bound = S3 <= C * L / (m * m)
    ok_n3 = Fr(1, 1) / S3 >= m * m / (C * L)
    ok_chain = Fr(1, 1) / (S2 * S2) >= Fr(1, 1) / S3
    ok_n2 = Fr(1, 1) / (S2 * S2) >= m * m / (C * L)
    return dict(C=C, ok=ok_bound and ok_n3 and ok_chain and ok_n2,
                S2=S2, S3=S3)


LEAN_STMT = """\
-- Renyi/Hill monotonicity (exact finite algebra; Lean-ready):
theorem renyi_hill_mono (n : Nat) (q : Fin n -> Rat)
    (hq : forall i, 0 <= q i) (hsum : (Finset.univ.sum q) = 1) :
    ((Finset.univ.sum fun i => (q i)^2))^2
        <= (Finset.univ.sum fun i => (q i)^3)
  /\\ ((Finset.univ.sum fun i => (q i)^3))^2
        <= (Finset.univ.sum fun i => (q i)^2)
           * (Finset.univ.sum fun i => (q i)^4) := by
  -- Lagrange witnesses (both sides expand to the same polynomial):
  --   sum_ij q i * q j * (q i - q j)^2
  --     = 2*((sum q)*(sum q^3) - (sum q^2)^2)
  --   sum_ij (q i)^2*(q j)^2*(q i - q j)^2
  --     = 2*((sum q^2)*(sum q^4) - (sum q^3)^2)
  -- nonnegativity of the LHS closes both conjuncts.
  sorry
-- corollary (composed, real-valued): S3^3 <= S4^2 and, given
--   S3 <= C*(Real.log m)^A/m^2  (0 < C, 2 <= m),
--   n_eff = 1/S2 >= m/(Real.sqrt C * (Real.log m)^(A/2))."""


def toy_fractions():
    """toy exactness: q = (1/2, 1/4, 1/4) exact table + uniform
    equality case + float cross-check on (2, 1, 1)."""
    r = fr_lagrange([Fr(1, 2), Fr(1, 4), Fr(1, 4)])
    ok = (r["S2"] == Fr(3, 8) and r["S3"] == Fr(5, 32)
          and r["S4"] == Fr(9, 128) and r["dev1"] == 0
          and r["dev2"] == 0 and r["slack1"] == Fr(1, 64)
          and r["slack2"] == Fr(37, 32768) and r["comp_ok"]
          and r["e3"] == Fr(1, 32) and r["newt_dev"] == 0)
    u = fr_lagrange([Fr(1, 3)] * 3)
    ok_u = (u["slack1"] == 0 and u["slack2"] == 0
            and u["dev1"] == 0 and u["dev2"] == 0)
    cm = cubic_moments(np.array([2.0, 1.0, 1.0]))
    ok_f = (abs(cm["S2"] - 3.0 / 8.0) <= TOY_BAR
            and abs(cm["S3"] - 5.0 / 32.0) <= TOY_BAR
            and abs(cm["S4"] - 9.0 / 128.0) <= TOY_BAR
            and cm["mono1"] == 0.0 and cm["mono2"] == 0.0
            and cm["newt"] <= TOY_BAR)
    return ok, ok_u, ok_f, r, cm


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("renyi3_probe -- PRIME.L2.ATOM.RENYI3.01 (round 306)")
    print("SPEC_SHA %s   R300_SHA %s   R301_SHA %s (imported)"
          % (SPEC_SHA[:16], DTP.SPEC_SHA[:16], NTP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions section "
                        "+ toys + scope audits + every exact ward "
                        "at w9 + m2 toy breach + m3/m4 mutants; "
                        "ladder, extension, anchors, prereg "
                        "measurement and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE RENYI-3 ROUND (reviewer plan section 5, the "
          "sharpest new fiber attack): prove or refute the "
          "POINTWISE cubic moment bound S_3 <= C (log m)^A / m^2 "
          "on every rung, with the constant family A in {0, 1, 2} "
          "preregistered and C frozen on the first %d rungs; the "
          "exact Renyi/Hill chain N_2 >= N_3 (Leg A, Fractions "
          "Lagrange witnesses) turns a GO into the new pointwise "
          "proof target n_eff >= m / (sqrt(C) (log m)^(A/2)) -- "
          "beating every demanded power m^0.888; sealed outcomes "
          "RENYI3_GO / RENYI3_TIGHT / RENYI3_DEAD; extension "
          "ladder r286-aligned (first %d anchors > H_CAP); ALL "
          "bars, bands, rules and verdicts sealed BEFORE "
          "evaluation" % (N_CAL, K_EXT))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("cubic_moments", "cubic_layers", "renyi3_ratio",
               "calib_freeze"):
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

    # ---------------- S1: census + controls (r303 scaffold verbatim)
    section("S1  CENSUS + CONTROLS + EXTENSION")
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
        okL = True
    else:
        kzs = []
        ekz = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= H_CAP:
                kzs.append(kz)
            elif h <= EXT_H_MAX:
                ekz.append(kz)
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:K_EXT]
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
    erecs = [rung_rec(p) for p in ext] if not smoke else []
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
        e_cheap = sum(1 for rc in erecs if rc["g_branch"] >= 0.0)
        e_exc = [rc["kz"] for rc in erecs if rc["g_branch"] < 0.0]
        check("G11-branch-reproduction",
              len(cheap) == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT))
              and all(rc["g_branch"] >= 0 for rc in mrecs),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7; mains %s; "
              "EXT census (no sealed expectation): %d cheap / %d "
              "exception %s"
              % (len(cheap), str(exc_kz),
                 "; ".join("w%d g %+.3f CHEAP" % (rc["kz"],
                                                  rc["g_branch"])
                           for rc in mrecs),
                 e_cheap, len(e_exc), str(e_exc)))

    # ---------------- S2: decomposition wards + eval
    section("S2  EXACT DECOMPOSITION + IDENTITY WARDS")
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
    for rc in erecs:
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
          "sum_b ct_b == t_{N-2} on %d rungs + %d ext + %d mains "
          "+ 3 controls: worst dev/absmass %.1e main N<=%d (bar "
          "%.0e) / %.1e deep / %.1e ext (bar %.0e) / %.1e "
          "controls (bar %.0e)"
          % (len(recs), len(erecs), len(mrecs), tb_worst, DEEP_N,
             TB_WARD_BAR, tb_deep, tb_ext, TB_WARD_BAR_DEEP,
             tb_ctrl, TB_WARD_BAR_CTRL))

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
        brk, m, jb = WBT.block_breaks(xb, runs)
        Pb = np.bincount(jb, weights=cb, minlength=m) \
            if m else np.zeros(0)
        Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                                  rc["hi"], brk, m)
        Pd = Pb - Pw
        part = DTP.participation(Pd)
        qu = NTP.quasi_uniformity(Pd)
        po = NTP.participation_orders(Pd)
        cm = cubic_moments(Pd)
        cl = cubic_layers(Pd)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        degenerate = (cm["L1"] <= DEG_FLOOR * absm)
        fxs = rc["bx"] * rc["v2"] * rc["fac"]
        sd = DTP.shared_delta(rc["bx"], rc["ct"], rc["bw"], fxs,
                              rc["xu"], rc["cw"], rc["wu"])
        if degenerate or sd["n"] == 0:
            pr = dict(lloc=1.0, neff_atom=1.0, n=0)
            na_sinv = 0.0
        else:
            pr = NTP.dc_profile(sd["x"], sd["dc"], rc["lo"],
                                rc["hi"])
            edm = PBB.mask_edge(sd["x"], rc["lo"], rc["hi"],
                                EDGE_F)
            z = np.sort(np.asarray(sd["dc"], dtype=float)[~edm])
            L1z = float(np.sum(np.abs(z)))
            Dz = float(np.sum(z * z))
            na_s = L1z * L1z / max(Dz, 1e-300) if Dz > 0 else 1.0
            na_sinv = abs(na_s - pr["neff_atom"]) \
                / max(pr["neff_atom"], 1e-300)
        return dict(alt_ok=alt_ok, R=R, P=P, e_c2=e_c2, H=H,
                    S_F=S_F, m=m, Pd=Pd, part=part, qu=qu, po=po,
                    cm=cm, cl=cl, degenerate=degenerate, pr=pr,
                    na_sinv=na_sinv, Mr=Mr)

    all_rc = recs + mrecs + erecs
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
    qid_w = max(rc["ev"]["qu"]["qid_dev"] for rc in pool_all)
    mono1_w = max(rc["ev"]["cm"]["mono1"] for rc in live)
    mono2_w = max(rc["ev"]["cm"]["mono2"] for rc in live)
    newt_w = max(rc["ev"]["cm"]["newt"] for rc in live)
    sinv_w = max(rc["ev"]["cm"]["sinv"] for rc in live)
    nasi_w = max(rc["ev"]["na_sinv"] for rc in pool_all)
    n2x_w = max(abs(rc["ev"]["cm"]["N2"] - rc["ev"]["part"]["neff"])
                / max(rc["ev"]["part"]["neff"], 1e-300)
                for rc in live)
    pox_w = max(rc["ev"]["po"]["mono"] for rc in live)
    check("G22-cubic-identity-wards",
          qid_w <= QID_BAR and mono1_w <= MONO_BAR
          and mono2_w <= MONO_BAR and newt_w <= NEWT_BAR
          and sinv_w <= SINV_BAR and nasi_w <= SINV_BAR
          and n2x_w <= N2X_BAR and pox_w <= MONO_BAR,
          "on %d live worlds: count identity %.1e (bar %.0e); "
          "power-mean slacks S2^2<=S3 %.1e / S3^3<=S4^2 %.1e (bar "
          "%.0e); Newton prefix ward %.1e (bar %.0e); S_3 "
          "sort-invariance %.1e + n_eff_atom sort-invariance %.1e "
          "(bar %.0e, MARGINAL functionals); N_2 == n_eff %.1e "
          "(bar %.0e); r301 order-chain cross-ward %.1e%s"
          % (len(live), qid_w, QID_BAR, mono1_w, mono2_w,
             MONO_BAR, newt_w, NEWT_BAR, sinv_w, nasi_w, SINV_BAR,
             n2x_w, N2X_BAR, pox_w,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION (r297-r303 records)")
    Ns = [rc["N"] for rc in recs]
    st = {}
    if smoke:
        check("G30-renyi-anchors", True, "SMOKE: skipped")
        check("G31-margin-chain", True, "SMOKE: skipped")
        check("G32-count-atom-anchors", True, "SMOKE: skipped")
    else:
        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        eps_c2_rel = [rc["ev"]["e_c2"] / M_W for rc in recs]
        st["sl_c2"] = L2D.halves_slope(Ns, eps_c2_rel)
        pref = [(rc["ev"]["m"] + rc["ev"]["H"] - 1) / rc["ev"]["H"]
                for rc in recs]
        st["sl_pref"] = L2D.halves_slope(Ns, pref)
        st["sigma_star"] = 2.0 * (st["sl_c2"] - DELTA_NEED) \
            - st["sl_pref"]
        st["sl_D"] = slp([rc["ev"]["part"]["D"] for rc in recs])
        st["sl_L1"] = slp([rc["ev"]["part"]["L1"] / M_W
                           for rc in recs])
        meds = []
        slps = []
        for key in ("N2", "N3", "N4", "Ninf"):
            vals = [rc["ev"]["po"][key] for rc in recs]
            meds.append(float(np.median(vals)))
            slps.append(slp(vals))
        st["renyi_meds"] = meds
        st["renyi_slps"] = slps
        ok_r = all(abs(meds[i] - R301_RENYI_MEDS[i])
                   <= R301_RENYI_MED_TOL for i in range(4)) \
            and all(abs(slps[i] - R301_RENYI_SLOPES[i])
                    <= R301_RENYI_SL_TOL for i in range(4)) \
            and abs(st["sl_c2"] - R297_SL_C2) <= R297_TOL \
            and abs(st["sl_pref"] - R297_SL_PREF) <= R297_TOL \
            and abs(st["sigma_star"] - R297_SIGMA_STAR) <= R297_TOL \
            and abs(st["sl_D"] - R299_SL_D) <= R299_SL_D_TOL
        check("G30-renyi-anchors", ok_r,
              "Renyi meds %.2f/%.2f/%.2f/%.2f (rec "
              "37.41/27.88/24.04/15.47 tol %.2f), slopes "
              "%+.3f/%+.3f/%+.3f/%+.3f (rec +0.963/+0.926/+0.894/"
              "+0.738 tol %.2f); sigma* %+.3f, sl_D %+.3f"
              % (meds[0], meds[1], meds[2], meds[3],
                 R301_RENYI_MED_TOL, slps[0], slps[1], slps[2],
                 slps[3], R301_RENYI_SL_TOL, st["sigma_star"],
                 st["sl_D"]))
        st["sl_neff"] = slp([rc["ev"]["part"]["neff"]
                             for rc in recs])
        need = 2.0 * st["sl_L1"] - st["sigma_star"]
        m_D = st["sigma_star"] - st["sl_D"]
        m_NEFF = st["sl_neff"] - need
        dev_mc = abs(m_NEFF - m_D)
        st["m_D"] = m_D
        check("G31-margin-chain",
              abs(m_D - MARGIN_REF) <= MARGIN_TOL
              and dev_mc <= PROP_BAR,
              "the r303 core slack live: S = sigma* - sl_D = "
              "%+.4f (rec %+.4f tol %.3f); dictionary invariance "
              "|m_NEFF - m_D| = %.1e (bar %.0e, exact halves_slope "
              "log-additivity)" % (m_D, MARGIN_REF, MARGIN_TOL,
                                   dev_mc, PROP_BAR))
        nacts = [rc["ev"]["qu"]["n_act"] for rc in recs]
        st["nact_med"] = float(np.median(nacts))
        st["sl_nact"] = slp(nacts)
        link = sum(1 for rc in recs
                   if rc["ev"]["qu"]["n_act"] == rc["ev"]["m"])
        elink = sum(1 for rc in erecs
                    if rc["ev"]["qu"]["n_act"] == rc["ev"]["m"])
        natoms = [rc["ev"]["pr"]["neff_atom"] for rc in recs]
        st["natom_med"] = float(np.median(natoms))
        st["sl_natom"] = slp(natoms)
        check("G32-count-atom-anchors",
              abs(st["nact_med"] - R301_NACT_MED) <= R301_NACT_TOL
              and abs(st["sl_nact"] - R301_SL_NACT)
              <= R301_SL_NACT_TOL
              and link == 42
              and abs(st["natom_med"] - R301_NATOM_MED)
              <= R301_NATOM_TOL
              and abs(st["sl_natom"] - R301_SL_NATOM)
              <= R301_SL_NATOM_TOL,
              "n_act med %.1f (rec %.1f) slope %+.3f (rec %+.3f); "
              "COUNT LINK n_act == m on %d/42 (EXT census: "
              "%d/%d); n_eff_atom med %.1f (rec %.1f) slope %+.3f "
              "(rec %+.3f)"
              % (st["nact_med"], R301_NACT_MED, st["sl_nact"],
                 R301_SL_NACT, link, elink, len(erecs),
                 st["natom_med"], R301_NATOM_MED, st["sl_natom"],
                 R301_SL_NATOM))

    # ---------------- S4: Leg A exact algebra
    section("S4  LEG A -- EXACT ALGEBRA (Fractions)")
    vecs = ([Fr(1, 2), Fr(1, 4), Fr(1, 4)],
            [Fr(1, 3), Fr(1, 3), Fr(1, 3)],
            [Fr(2, 3), Fr(1, 6), Fr(1, 6)],
            [Fr(2, 5), Fr(1, 5), Fr(1, 5), Fr(1, 10), Fr(1, 10)])
    ok_lag = True
    worst = []
    for v in vecs:
        r = fr_lagrange(v)
        ok_lag = ok_lag and r["dev1"] == 0 and r["dev2"] == 0 \
            and r["slack1"] >= 0 and r["slack2"] >= 0 \
            and r["comp_ok"] and r["newt_dev"] == 0 \
            and r["S1"] == 1
        worst.append("(%s: s1 %s s2 %s)"
                     % ("/".join(str(x) for x in v[:2]) + "..",
                        r["slack1"], r["slack2"]))
    check("G40-lagrange-chain-exact", ok_lag,
          "both Lagrange witnesses dev 0 EXACT + power-mean chain "
          "slacks >= 0 + composed S_3^3 <= S_4^2 + Newton dev 0 "
          "on %d rational probability vectors: %s"
          % (len(vecs), "; ".join(worst[:2])))
    br = fr_bridge()
    check("G41-bridge-exact", br["ok"],
          "bridge with all constants EXACT (q = (1/2,1/4,1/4), "
          "m = 3, L = 6/5 rational stand-in, C = %s "
          "equality-tight): S_3 <= C L/m^2, N_3^2 >= m^2/(C L), "
          "N_2^2 >= 1/S_3 >= m^2/(C L) -- all rational "
          "comparisons hold" % br["C"])

    # ---------------- S5: Leg B prereg + measurement
    section("S5  LEG B -- PREREGISTRATION + POINTWISE MEASUREMENT")
    if smoke:
        ev9 = recs[0]["ev"]
        r9 = renyi3_ratio(ev9["cm"]["S3"], ev9["m"], 0)
        info("SMOKE: w9 rho_0 = %.3f (m %d, S_3 %.3e); prereg "
             "measurement + adjudication skipped"
             % (r9, ev9["m"], ev9["cm"]["S3"]))
        check("G50-calibration-freeze", True, "SMOKE: skipped")
        check("G51-pointwise-adjudication", True, "SMOKE: skipped")
        check("G52-world-controls", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        srt_all = sorted(recs + erecs,
                         key=lambda rc: (rc["N"], rc["kz"]))
        rhoT = {}
        for A in A_FAMILY:
            rhoT[A] = [renyi3_ratio(rc["ev"]["cm"]["S3"],
                                    rc["ev"]["m"], A)
                       for rc in srt_all]
        n_all = len(srt_all)
        cal_idx = tuple(range(N_CAL))
        C = {}
        argm = {}
        decl = {}
        for A in A_FAMILY:
            C[A], argm[A], decl[A] = calib_freeze(rhoT[A], cal_idx)
        ok_split = all(decl[A] == cal_idx for A in A_FAMILY)
        check("G50-calibration-freeze", ok_split,
              "C frozen on EXACTLY the first %d rungs of the "
              "(N, kz)-sorted ladder: C_0 %.3f @ rung %d (kz%d) / "
              "C_1 %.3f @ rung %d / C_2 %.3f @ rung %d; test set "
              "= %d core + %d ext rungs"
              % (N_CAL, C[0], argm[0], srt_all[argm[0]]["kz"],
                 C[1], argm[1], C[2], argm[2],
                 42 - N_CAL, len(erecs)))
        # per-rung table (compact, full record)
        info("rung table: idx kz N m S_3 rho_0 rho_1 rho_2 "
             "[EXT marks]")
        for i, rc in enumerate(srt_all):
            is_ext = rc in erecs
            marks = "".join(
                "*" if rhoT[A][i] > C[A] else "." for A in A_FAMILY)
            info("%2d kz%-3d N %4d m %3d S3 %.3e rho %7.3f %6.3f "
                 "%6.3f %s%s"
                 % (i, rc["kz"], rc["N"], rc["ev"]["m"],
                    rc["ev"]["cm"]["S3"], rhoT[0][i], rhoT[1][i],
                    rhoT[2][i], marks, " EXT" if is_ext else ""))
        Ns57 = [rc["N"] for rc in srt_all]
        core_idx = [i for i, rc in enumerate(srt_all)
                    if rc not in erecs]
        res = {}
        for A in A_FAMILY:
            viol = [i for i in range(n_all) if rhoT[A][i] > C[A]]
            test = [i for i in range(n_all) if i not in cal_idx]
            rsv = [C[A] / max(rhoT[A][i], 1e-300) for i in test]
            sl42 = L2D.halves_slope(
                [Ns57[i] for i in core_idx],
                [max(rhoT[A][i], 1e-300) for i in core_idx])
            sl57 = L2D.halves_slope(
                Ns57, [max(v, 1e-300) for v in rhoT[A]])
            res[A] = dict(viol=viol, rmin=min(rsv),
                          rmed=float(np.median(rsv)),
                          sl42=sl42, sl57=sl57,
                          hold=(len(viol) == 0),
                          grow=(sl42 <= -RES_EPS
                                and sl57 <= -RES_EPS))
            info("A=%d: C %.3f, violations %d/%d, reserve "
                 "min/med %.2f/%.2f, trend slope42 %+.3f "
                 "slope57 %+.3f -> %s%s"
                 % (A, C[A], len(res[A]["viol"]), n_all,
                    res[A]["rmin"], res[A]["rmed"], sl42, sl57,
                    "HOLD" if res[A]["hold"] else "VIOLATED",
                    "+GROW" if res[A]["grow"] else ""))
        go_As = [A for A in A_FAMILY
                 if res[A]["hold"] and res[A]["grow"]]
        hold_As = [A for A in A_FAMILY if res[A]["hold"]]
        if go_As:
            A_star = min(go_As)
            verdict_main = "RENYI3_GO(C = %.3f, A = %d)" \
                % (C[A_star], A_star)
            A_rep = A_star
        elif hold_As:
            A_star = min(hold_As)
            verdict_main = "RENYI3_TIGHT(A = %d, C = %.3f, " \
                "trend %+.3f/%+.3f)" \
                % (A_star, C[A_star], res[A_star]["sl42"],
                   res[A_star]["sl57"])
            A_rep = A_star
        else:
            A_rep = max(A_FAMILY)
            vl = res[A_rep]["viol"]
            vtxt = ", ".join(
                "kz%d (N %d, rho %.3f%s)"
                % (srt_all[i]["kz"], srt_all[i]["N"],
                   rhoT[A_rep][i],
                   " EXT" if srt_all[i] in erecs else "")
                for i in vl[:6])
            verdict_main = "RENYI3_DEAD(violating rungs at A = " \
                "%d: %s; worst excess %.1f%%)" \
                % (A_rep, vtxt,
                   100.0 * max(rhoT[A_rep][i] / C[A_rep] - 1.0
                               for i in vl))
        n_fired = (1 if go_As else 0) + \
            (1 if (not go_As and hold_As) else 0) + \
            (1 if not hold_As else 0)
        check("G51-pointwise-adjudication", n_fired == 1,
              "exactly one sealed verdict fired: %s"
              % verdict_main)
        wnote = []
        w_ok = []
        for c in ("EPST", "SCR"):
            evc = crecs[c]["ev"]
            if evc["degenerate"]:
                wnote.append("%s DEGENERATE (skipped)" % c)
                continue
            rw = renyi3_ratio(evc["cm"]["S3"], evc["m"], A_rep)
            holds = rw <= C[A_rep]
            w_ok.append(holds)
            wnote.append("%s rho_%d %.3f %s C %.3f"
                         % (c, A_rep, rw,
                            "<=" if holds else ">", C[A_rep]))
        if crecs["SMOOTH"]["ev"]["degenerate"]:
            wnote.append("SMOOTH skipped (pre-declared DEG_FLOOR "
                         "guard, L1 degenerate)")
        world_tag = "WORLD_BLIND" if w_ok and all(w_ok) \
            else "WORLD_SENSITIVE"
        check("G52-world-controls", True,
              "%s (census, no sealed expectation): %s"
              % (world_tag, "; ".join(wnote)))
        st["res"] = res
        st["C"] = C
        st["A_rep"] = A_rep
        st["world_tag"] = world_tag
        st["wnote"] = wnote

    # ---------------- S6: Leg C anatomy
    section("S6  LEG C -- STRUCTURE OF THE CUBIC MOMENT")
    if smoke:
        ev9 = recs[0]["ev"]
        info("SMOKE: w9 top-1/3/8 shares %.3f/%.3f/%.3f, layer01 "
             "%.3f" % (ev9["cl"]["top"][1], ev9["cl"]["top"][3],
                       ev9["cl"]["top"][8], ev9["cl"]["lay01"]))
        check("G60-anatomy-census", True, "SMOKE: skipped")
    else:
        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        tmed = {}
        tsl = {}
        for k in TOPK:
            vals = [rc["ev"]["cl"]["top"][k] for rc in recs]
            tmed[k] = float(np.median(vals))
            tsl[k] = slp(vals)
        lay01 = float(np.median([rc["ev"]["cl"]["lay01"]
                                 for rc in recs]))
        mlay = float(np.median([rc["ev"]["cl"]["mean_layer"]
                                for rc in recs]))
        # triple-config split shares of the total cube (== 1)
        s3s = [rc["ev"]["cm"]["S3"] for rc in recs]
        prs = [3.0 * (rc["ev"]["cm"]["S2"] - rc["ev"]["cm"]["S3"])
               for rc in recs]
        trs = [1.0 - s3s[i] - prs[i] for i in range(len(recs))]
        m2s = [rc["ev"]["m"] * rc["ev"]["cm"]["S2"] for rc in recs]
        m3s = [rc["ev"]["m"] ** 2 * rc["ev"]["cm"]["S3"]
               for rc in recs]
        ok_sh = all(0.0 <= v <= 1.0 for v in
                    [tmed[k] for k in TOPK] + [lay01]) \
            and all(t >= 0.0 for t in trs)
        check("G60-anatomy-census", ok_sh,
              "top-1/3/8 S_3 shares med %.3f/%.3f/%.3f slopes "
              "%+.3f/%+.3f/%+.3f; layer-0+1 share med %.3f, "
              "S_3-weighted mean layer %.2f; triple-config split "
              "med S_3 %.4f / pairs %.3f / triples %.3f (sum == 1 "
              "by A3); shape moments M_2 med %.2f (r302 m2_inf "
              "%.3f) M_3 med %.2f"
              % (tmed[1], tmed[3], tmed[8], tsl[1], tsl[3],
                 tsl[8], lay01, mlay, float(np.median(s3s)),
                 float(np.median(prs)), float(np.median(trs)),
                 float(np.median(m2s)), R302_M2_INF,
                 float(np.median(m3s))))
        st["tmed"] = tmed
        st["tsl"] = tsl
        st["lay01"] = lay01
        st["mlay"] = mlay
        st["m2_med"] = float(np.median(m2s))
        st["m3_med"] = float(np.median(m3s))
        few = tmed[8] >= 0.5 and tsl[8] >= 0.0
        info("MINIMAL STRUCTURE STATEMENT (named, typed, no "
             "upgrade): %s"
             % ("HEAVY-FEW form disfavored by the reviewer tree "
                "(max-adjacent)" if few else
                "SHAPE3_TARGET -- prove M_3 = m^2 S_3 of the "
                "stationary normalized shape u = m q is "
                "polylog-bounded (the third-moment analog of the "
                "r302 M_2 -> %.3f stationarity)" % R302_M2_INF))

    # ---------------- S7: Leg D Lean statement
    section("S7  LEG D -- LEAN-READY STATEMENT")
    print(LEAN_STMT)
    check("G70-lean-statement", "renyi_hill_mono" in LEAN_STMT
          and "Lagrange" in LEAN_STMT,
          "exact Renyi/Hill monotonicity + bridge corollary "
          "printed in Lean-ready form (statement text only; the "
          "Lean worker takes over)")

    # ---------------- S8: Leg E mustfails + toys
    section("S8  LEG E -- WARDS / MUST-FAILS")
    ok_t, ok_u, ok_f, rt, cmt = toy_fractions()
    check("G84-toy-exactness", ok_t and ok_u and ok_f,
          "q = (1/2,1/4,1/4): S_2 3/8, S_3 5/32, S_4 9/128, "
          "slacks 1/64 + 37/32768, e_3 1/32, Newton 0 -- EXACT; "
          "uniform: both slacks 0 EXACT (equality case); float "
          "cubic_moments matches Fractions (bar %.0e)" % TOY_BAR)
    rm = fr_lagrange([Fr(1, 2), Fr(1, 4), Fr(1, 4)], wrong="flip")
    check("G80-m1-powermean-flip", rm["slack1"] < 0
          and rm["slack1"] == Fr(-1, 64),
          "m1 CAUGHT: the flipped claim S_3 <= S_2^2 breaks by "
          "%s EXACT on (1/2, 1/4, 1/4)" % (-rm["slack1"]))
    toy_rho = [float(i) for i in range(1, 11)]
    Ct, jt, dt = calib_freeze(toy_rho, range(N_CAL))
    Cm, jm, dm = mutant_calib_full(toy_rho)
    caught2 = (dm != dt) and (Cm - Ct == 5.0)
    note2 = ""
    if not smoke:
        rr = [Cm2 for Cm2 in
              (mutant_calib_full(rhoT[A])[0] / st["C"][A]
               for A in A_FAMILY)]
        note2 = "; real ladder C_full/C_cal %.2f/%.2f/%.2f " \
            "(argmax rung %d outside the split)" \
            % (rr[0], rr[1], rr[2],
               int(np.argmax(rhoT[0])))
    check("G81-m2-prereg-breach", caught2,
          "m2 CAUGHT: whole-ladder calibration declares set "
          "0..9 != frozen 0..%d, C_mut - C_cal = %s EXACT on the "
          "toy rho list%s" % (N_CAL - 1, Cm - Ct, note2))
    ev9 = mrecs[0]["ev"]
    a9 = np.abs(ev9["Pd"])
    S3_un = float(np.sum(a9 ** 3))
    dev3 = abs(S3_un - ev9["cm"]["S3"]) \
        / max(ev9["cm"]["S3"], 1e-300)
    check("G82-m3-unnormalized", dev3 >= MUT_MIN,
          "m3 LOUD: unnormalized cubic moment deviates rel %.1e "
          ">= %.0e (factor L1^3 = %.1e)"
          % (dev3, MUT_MIN, ev9["cm"]["L1"] ** 3))
    m9 = max(ev9["m"], 3)
    syn = np.zeros(m9)
    syn[0] = 1.0
    cms = cubic_moments(syn)
    loud4 = cms["S3"] / max(ev9["cm"]["S3"], 1e-300)
    check("G83-m4-oneatom-collapse",
          cms["S2"] == 1.0 and cms["S3"] == 1.0
          and cms["S4"] == 1.0 and cms["N2"] == 1.0
          and cms["N3"] == 1.0 and loud4 >= M4_LOUD_MIN,
          "m4 LOUD: one-atom profile S_2 = S_3 = S_4 = 1 EXACT, "
          "all N_k == 1; the bound breaks by %.0f x the real w9 "
          "cubic moment (min %.0f)" % (loud4, M4_LOUD_MIN))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact Renyi/Hill chain with Lagrange "
          "witnesses (Fractions + live wards), the exact bridge "
          "with all constants, the preregistered pointwise cubic "
          "bound family with frozen calibration split, the r286 "
          "extension anchors, the mass-layer/triple-configuration "
          "anatomy and the Lean-ready statement -- NO new "
          "certificate promoted")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        res = st["res"]
        parts = ["RENYI3_ANCHORS(meds %.2f/%.2f/%.2f/%.2f slopes "
                 "%+.3f/%+.3f/%+.3f/%+.3f; S %+.4f; link 42/42; "
                 "natom %.1f/%+.3f)"
                 % (st["renyi_meds"][0], st["renyi_meds"][1],
                    st["renyi_meds"][2], st["renyi_meds"][3],
                    st["renyi_slps"][0], st["renyi_slps"][1],
                    st["renyi_slps"][2], st["renyi_slps"][3],
                    st["m_D"], st["natom_med"], st["sl_natom"])]
        parts.append("PREREG(C %.3f/%.3f/%.3f, split %d|%d+%d)"
                     % (st["C"][0], st["C"][1], st["C"][2],
                        N_CAL, 42 - N_CAL, len(erecs)))
        parts.append("POINTWISE(%s)"
                     % "; ".join(
                         "A=%d viol %d/57 rsv %.2f/%.2f sl "
                         "%+.3f/%+.3f"
                         % (A, len(res[A]["viol"]),
                            res[A]["rmin"], res[A]["rmed"],
                            res[A]["sl42"], res[A]["sl57"])
                         for A in A_FAMILY))
        parts.append(verdict_main)
        parts.append("ANATOMY(top8 %.3f/%+.3f, lay01 %.3f, M_3 "
                     "med %.2f)"
                     % (st["tmed"][8], st["tsl"][8], st["lay01"],
                        st["m3_med"]))
        parts.append(st["world_tag"])
        parts.append("LEAN_STMT(printed)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the Lagrange identities, "
          "the power-mean chain, the bridge, the Newton split and "
          "the marginal invariance (all world-blind algebra); "
          "MEASURED: every C, reserve, share, slope and world "
          "census (42 + %d finite rungs); OPEN: the pointwise "
          "bound beyond the measured rungs, the cofinal step H5, "
          "kz15 beyond r270; NO RH claim"
          % (verd, " (SMOKE)" if smoke else "", len(erecs)))
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
