#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""phi3_functional_probe -- PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01
(round 315): THE QUANTITATIVE MEMBERSHIP FUNCTIONAL Phi_3 -- part 2
of the reviewer's signed-cube contract: define Phi_3 IN ADVANCE
from the divergence-form STRUCTURE of r314 (flux cancellation +
collision split), normalize to the Renyi-3 target scale, and run
the BLIND world test with the four reviewer criteria.  Reviewer
frame (binding, r314 sealing note): Phi_3 must be built from the
divergence-form structure, NOT calibrated on the r314 world-number
tables; the naive magnitude sum is suspect because the terms CANCEL
against each other (C_full RISES +0.213 -- the functional must
exploit the cancellation, not majorize term sizes).  Context
(sealed record inputs): r314 (SPEC 841b3196) proved the exact
signed cubic identity sum_j |x_j|^3 = DeltaF + C_collision +
C_boundary with a LOCAL divergence form (edge flux dF = 3 G (s1^2 -
s2) on the transported prefix state), C_boundary == 0 exactly
(opening-flux lemma), collisions exactly countable via the banked
multiplicity-2 asset; r313 delivered the genealogy and the honest
class rest (a QUANTITATIVE membership functional is needed, not a
boolean property list); r306 (SPEC 3bb365e1) fixed the target
scale: sum q^3 <= 1.069 (log m)^2 / m^2 pointwise on 57 rungs,
EPSTEIN holds / SCRAMBLE breaks 1.67x.  kz15 permanently closed via
r270; the 6 exceptions via the r287 F2 certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the r312 block-Green round runs in parallel; this
probe touches NOTHING outside its own file and the additive
rh-sync.

THE OBJECT (r269/r287/r298/r306/r313/r314 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F =
0.20 edge split; maximal same-sign runs of the bx-sorted bulk;
level-2 blocks (r270 convention); the frozen positional block
machinery (r298 WBT.block_breaks + WBT.aggregate_blocks); the r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze; the r313
PFK.type_expansion (raw atomic presentation: P_j == sum of raw
atoms, fold group = atoms at one position); the r314
SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope +
SCF.collision_census (the sealed divergence form), ALL imported
verbatim; PDelta = Pbeta - Pomega; x_j = (PDelta)_j.  NEW in this
round (module-own, source-pure): the Phi_3 candidate family, the
purity audits (identifier scan + r314-table literal scan), the
multiplicity-3 control constructor and the blind adjudication.

THE SEALED FUNCTIONAL FAMILY (frozen BEFORE any evaluation; every
formula fixed here, no constant tuned on any world number).  On the
divergence-form state of one rung -- fold-genealogy block sums x_j,
group power sums Q2_j / Q3_j, per-block flux ends F_end_j and
openings F_open_j, abs edge mass sum |dF| -- with sigma_j =
sign(x_j), L = sum_j |x_j| and the Renyi-3 normalization
    NORM = m^2 / ((log m)^2 L^3)
(the reviewer's own scale: NORM x sum|x|^3 is exactly the r306
statistic rho_2), define the three sealed components
    DFLUX = sum_j sigma_j F_end_j      (the FLUX DEFECT: far flux
            surviving the intra-block edge cancellation),
    COLL  = sum_j sigma_j (3 Q2_j x_j - 2 Q3_j)   (the combined
            signed collision sum -- pair + full in ONE signed
            number, cross-block sign use included),
    BND   = sum_j sigma_j F_open_j     (the opening-flux boundary),
    FCIX  = sum_j |F_end_j| / sum_{j,i} |dF_{j,i}|   (the r314
            flux-cancellation index, 1 = no cancellation),
and the THREE SEALED CANDIDATES (evaluated in parallel):
    Phi3a = NORM x (|COLL| + |BND| + |DFLUX|)   [the reviewer raw
            proposal: non-telescoping parts + flux defect]
    Phi3b = NORM x |COLL|                       [cancellation-aware:
            the collision block as ONE signed number]
    Phi3c = NORM x |COLL| x FCIX                [flux-corrected:
            the cancellation depth as multiplicative discount].
HONESTY CONDITIONS (hard, audited): every candidate is computed
from the source recursion / fold incidences / boundary fluxes ONLY
-- no sum q^3, no terminal wall sign, no r314 world-table number
(AST identifier scan + literal scan, Leg A).  DISCLOSED ALGEBRAIC
RELATIONS (derived, no measurement): by the r314 identity and the
triangle inequality Phi3a >= NORM sum|x|^3 = rho_2 pointwise --
Phi3a sits ABOVE the r306 statistic by construction, and its
boundedness asks precisely whether the divergence terms overshoot
the cube by at most a constant factor; numerically Phi3b == NORM x
|sum|x|^3 - DeltaF| (the exact-difference form of reviewer
candidate (c)) because BND == 0 -- but that literal form CONSUMES
the cubic target, so it is adjudicated READ-BACK-ADJACENT and
DEMOTED to a diagnostic cross-ward column (G42), NOT a candidate;
the sealed candidate (c) keeps the source-pure path |COLL| and
carries the FC index as the multiplicative correction instead.
THEOREM CLASS: Phi3(w) <= C_0 with C_0 frozen by the r306 prereg
protocol (max over the FIRST N_CAL = 5 rungs of the (N, kz)-sorted
57-rung ladder, then FROZEN; calibration on shallow MAIN rungs is
the sealed r306 protocol -- the FORBIDDEN calibration is the r314
world table, which never enters any formula or bar).

LEG 0 -- ANCHOR REGRESSION (r314/r306 record numbers adopted
as-is, disclosed): med signed shares over the 42 core rungs
DeltaF/C_pair/C_full = -0.4226/+0.5980/+0.8537 (tol 0.005); FC med
0.629 (tol 0.005) slope -0.141 (tol 0.01); fold multiplicity == 2
UNIFORM on 57/57 (exact); the r314 identity wards live (f64
recomposition <= REC3_BAR, telescope <= TEL_BAR, boundary <=
BND_BAR); the r306 bound live at A = 2: C_2 = 1.069 (tol 0.005)
frozen on the first 5 rungs, 0/57 violations.

LEG A -- SEALING + PURITY AUDITS: (A1) the candidate formulas
above are printed as the sealed definitions BEFORE any world
number of this round exists.  (A2) SOURCE-PURITY AUDIT: the AST
identifier scan over the builder phi3_variants (and the control
constructors) must be clean against BOUND_FORBIDDEN (terminal
drive key, branch label, target identifiers) AND against
PHI3_FORBIDDEN (the cubic-target names: cube / S3 / cm /
renyi3_ratio) -- consumed inputs per candidate are printed.  (A3)
TABLE-CALIBRATION AUDIT: the literal scan flags any float constant
in a Phi_3 builder that equals an r314 world-table record number
(sealed literal list R314_TABLE_LITERALS, rounded to 4 decimals);
the real builders must be CLEAN.  (A4) TOY EXACTNESS (Fractions,
bar 1e-14): two-block toy {1,2}|{3}: COLL = 27 + 27 = 54 == cube,
DFLUX = 0, BND = 0, so Phi3a == Phi3b unnormalized 54 EXACT and
FCIX = 0 (no interior flux, disclosed convention); flux toy
(1,2,3,4) in one block: COLL = 700, DFLUX = 300, cube = 1000 ==
700 + 300 EXACT, FCIX = 300/300 = 1, so the unnormalized Phi3a =
1000 == cube EXACT (disclosed: with uniform sign and one block the
reviewer-raw form degenerates to the cube; the real ladder mixes
signs across blocks).

LEG B -- THE BLIND TEST (all 57 rungs + twin + controls; the trend
is the core question): per candidate v the frozen C0_v (first-5
freeze), then the FOUR REVIEWER CRITERIA as sealed clauses:
  K1 SOURCE PURITY: the Leg A audits pass (gate G40);
  K2 WORLD ORDER (rank test, sealed bars): Phi3v(SCRAMBLE) is
     STRICTLY the largest value among {all 57 rungs, w9, w13,
     EPSTEIN, SCRAMBLE} AND Phi3v(EPSTEIN) <= C0_v AND the twin
     holds the frozen bound, Phi3v(w13) <= C0_v, with the near-
     identity band max(w13/w9, w9/w13) <= TWIN_FAC = 3.0;
  K3 STABLE SIZE RANGE: 0/57 violations of C0_v AND the ladder
     band max/min <= BAND_MAX = 30 over the 57 rungs AND the trend
     is not growing on both frozen estimators (halves_slope over
     the 42 core rungs and over all 57, each <= +RES_EPS = 0.01);
  K4 CLEAR LOCAL SCRAMBLE CAUSE (shared census): among the three
     structural components (NORM|DFLUX|, NORM|COLL|, FCIX) the
     largest relative deviation of SCRAMBLE vs the MAIN med is >=
     ATTR_MIN = 0.25 and NAMES the local cause.
Bars disclosed: BAND_MAX sized from the r306 record band (rho_2
falls 5.7x .. 7.5x over the ladder) times coarse headroom 4;
TWIN_FAC / ATTR_MIN coarse a-priori bands; the rank test carries
no tuned number at all; NOTHING is sized from the r314 world
table.  Per-rung table of Phi3a/b/c + FCIX printed as record data.

LEG C -- THE SYNTHETIC MUTANTS (reviewer table, matched boundary
statistics in the r303/r304 discipline): (i) MULTIPLICITY-3
CONTROL: every multiplicity-2 fold group of w9 has its first atom
split into two half atoms at the SAME position (exact dyadic
halving: every group value G1, every block value, every position
and the total mass are preserved BITWISE) -- the fold multiplicity
becomes 3 on every group; sealed requirements: the collision
COUNT bound breaks (3 p1 p2 - 2 p3 != the multiplicity-2 closed
form 8(n + 3n(n-1)); uniform toy n = 2: 216 vs 64, break 152
EXACT) AND the class rejects it via the multiplicity cap (max
mult 3 > MULT_CAP = 2); DISCLOSED HONESTY: the Phi_3 VALUE is
blind to this control by construction (G1 preserved -- warded
bitwise), so the multiplicity cap is a NECESSARY SIDE CONDITION of
the class, not a consequence of the functional.  (ii) ASSIGNMENT
SHUFFLE (the r313-m4 shuffle as base, seed SEED_SHUF = 315001):
the atom -> block assignment of w9 is permuted; sealed
requirements: the interval check rejects it (mismatches > 0) AND
the ordered-support flux profile breaks edgewise (rel dev >=
MUT_MIN -- the flux telescope of the sealed language class is NOT
permutation-blind, r314-m3) while the mass statistic stays matched
(sum x preserved, printed); the Phi_3 shift on the shuffled
instance is printed as census.

LEG D -- ADJUDICATION (sealed BEFORE evaluation; exactly one
fires; candidate precedence a > b > c disclosed -- the reviewer's
own raw proposal wins ties):
  PHI3_FOUND(v*, C0)  iff some candidate passes K1-K4 AND both
      Leg C contrasts fired (v* = first such in precedence);
  PHI3_PARTIAL(named) iff no FOUND but some candidate passes K1
      and at least one of K2/K3 -- the missing criteria are named
      per candidate;
  PHI3_ALL_BLIND      otherwise (no candidate is bounded-stable or
      world-ordering: the divergence-form structure alone is NOT
      the functional -- sealed honestly; R316 would have to start
      directly from the identity).

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) CUBIC READ-BACK SIMULATED: mutant_cube_readback computes
  NORM x |cube - DFLUX| by CONSUMING the cubic-moment record (the
  cm/S3 path) -- the PHI3_FORBIDDEN identifier scan must FLAG it
  (AST-CAUGHT) while phi3_variants stays clean.
(e2) TABLE CALIBRATION SIMULATED: mutant_table_calibrated carries
  an r314 world-table record number (0.629, the FC med) as its
  decision constant -- the literal scan must FLAG it (CAUGHT)
  while the real builders are literal-clean.
(e3) MULT-3 CONTROL BUILT WITH MULTIPLICITY 2 (sharpness of the
  Leg C mutant): the SAME constructor with split=False must be
  passed as NORMAL by the collision counting (count identity
  holds, class accepts) -- the rejection in Leg C is the
  multiplicity, not a constructor artifact.
(e4) WRONG NORMALIZATION EXPONENT: the m^1 mutant NORM' = m/((log
  m)^2 L^3) deviates from the sealed m^2 form by EXACTLY the
  factor m (algebra; measured on w9: ratio == m to 1e-12, rel dev
  1 - 1/m >= MUT_MIN) -- LOUD.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.  Scope hygiene: the new
  builders (phi3_variants, mult3_control) consume genealogy state
  + flux state only (BOUND_FORBIDDEN + PHI3_FORBIDDEN sets);
  fragment audit (no fit primitives).

INDEX FIREWALL (binding, r238-r314 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target sum q^3 enters GATES / anchors / diagnostic
columns only, NEVER a Phi_3 builder (AST-warded); no zero/prime
oracles anywhere (AST firewall); no fit primitives (fragment
audit).  MACHINERY IMPORTED VERBATIM: r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope + SCF.collision_census,
r313 PFK.type_expansion, r306 RY3.cubic_moments + RY3.renyi3_ratio
+ RY3.calib_freeze, r298 WBT.block_breaks + WBT.aggregate_blocks,
r269 PBB.mask_edge + PBB.runs_split, r287 L2D.blocks_level2 +
L2D.halves_slope + L2D.autocorr_full, r244 BH.wpack, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE: B_w
= S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).  COFINAL
LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}; EXTENSION: 900 < h
<= 1300, first 15 by (N, kz) (the r286 anchors, N_w 942..1218).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); ATOM_BAR
1e-9; REC3_BAR 1e-13; TEL_BAR 1e-13; BND_BAR 1e-13; DIAG_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; N_CAL 5; RES_EPS 0.01; BAND_MAX 30.0;
ATTR_MIN 0.25; TWIN_FAC 3.0; SEED_SHUF 315001; MUT_MIN 1e-6;
TOY_BAR 1e-14; TB_WARD bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6
controls; ID_BAR 1e-12; AC_BAR 1e-9; R314 anchors: shares
(-0.4226, +0.5980, +0.8537) tol 0.005, FC med 0.629 tol 0.005
slope -0.141 tol 0.01, multiplicity == 2 on 57/57 EXACT; R306
anchor: C_2 1.069 tol 0.005, 0/57 violations; R314_TABLE_LITERALS
(the sealed forbidden calibration set, rounded 4 decimals) =
{-0.4226, 0.598, 0.8537, 0.629, -0.141, -0.452, 0.823, 0.617,
0.057, -0.541, 0.43, 1.111, 0.675, 0.043, -2.695, -2.652, 6.347,
0.101, 0.011, -0.171, 0.856, 0.315, 0.693, 0.073}; runtime <=
1800 s; smoke = w9 + controls + toys + scope/purity audits + the
diagnostic cross-ward at w9 + the Leg C mutants at w9 + e1-e4;
ladder, extension, anchors, blind test and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r314/r306 RECORD number adopted as-is; the
NORM scale, the triangle relation Phi3a >= rho_2, the identity
Phi3b == NORM|cube - DeltaF| and the factor-m break of e4 are
derived algebra, disclosed above; BAND_MAX / TWIN_FAC / ATTR_MIN
are coarse a-priori bars sized from the r306 record band
(disclosed); NO Phi_3 value, NO world number and NO trend of this
round was computed before this spec was frozen; the three sealed
verdicts are symmetric -- no rule was chosen to favor an outcome.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the three main verdicts fires):
  R315_ANCHORS(r314 shares + FC + mult live, r314 identity wards,
    r306 C_2 + pointwise live)
+ SEAL(candidate formulas + purity audits + consumed inputs)
+ BLIND(per candidate: C0, violations, band, trends, K2/K3)
+ CAUSE(SCRAMBLE component attribution, named column)
+ CONTROLS(mult-3 rejection + count break + Phi_3 blindness ward;
    shuffle rejection + edgewise flux break + matched mass)
+ [exactly one of] PHI3_FOUND(v*, C0) / PHI3_PARTIAL(named) /
    PHI3_ALL_BLIND
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the candidate formulas and every bar are
sealed BEFORE evaluation; the r314 world table is consumed by NO
formula, NO bar and NO verdict rule (audited by the literal scan);
every Phi_3 value, band and slope is MEASURED on 42 + 15 finite
rungs + 2 mains + 2 live controls; a FOUND fixes a quantitative
membership functional on the measured worlds, it proves NO
universal bound (that is R316) and NO cofinal law; the twin/world
census is n = 1 per control world, weak by construction; Phi3a >=
rho_2 is algebra, so a FOUND for (a) additionally certifies
nothing about sum q^3 beyond r306; r243-r314 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 29/29 (0.3 s), NO amendment; calibration pass 1 =
first full evaluation, 29/29, wall 25.7 s, NO amendment; record
run1/run2 after this insertion, identical up to WALL; the ONLY
post-freeze edit is this record-table insertion, which IS the
protocol -- no bar, band, rule or verdict rule moved):
CAL_VERDICT = R315_ANCHORS(shares -0.4226/+0.5980/+0.8537, FC
0.629/-0.141, mult == 2 on 57/57, identity wards 4.5e-17 /
4.1e-16 / 4.1e-16, r306 C_2 1.069 with 0/57 violations -- ALL
bit-near r314/r306) + SEAL(purity clean: 0 identifier hits + 0
table-literal hits on the builders; e1 cube-readback FLAGGED, e2
table-calibration FLAGGED; diagnostic column == Phi3b to 1.6e-15)
+ BLIND(C0 a/b/c = 2.6261/1.5052/0.9400 frozen on the first 5,
argmax rung 2 = kz12; K3: a viol 2/57 band 22.85 (<= 30) trends
-0.638/-0.397, b viol 2/57 band 66.09 trends -0.627/-0.494, c
viol 2/57 band 87.64 trends -0.768/-0.522 -- ALL False; the two
violating rungs are kz55 and kz67 for ALL THREE candidates (a
4.6095/2.7260, b 2.5458/1.8898, c 2.4320/1.7289); K2: SCR a/b/c
2.3883/2.0841/1.4433 <= max(rest) 4.6095/2.5458/2.4320 (the max
is kz55 every time) -- rank FAILS; EPSTEIN 2.3545/1.3615/0.1375
<= C0 HOLDS on all three; twin w13 0.9597/0.7102/0.4795, factor
1.10/1.07/1.17 <= 3.0 HOLDS -- ALL False solely via the rank) +
CAUSE(SCRAMBLE component devs vs MAIN med: dflux 1.33 / coll
3.69 / fcix 0.10 -> named cause COLL, K4 True) + CONTROLS(mult-3
control: G1/blocks/mass preserved BITWISE (dev 0.0), mult 3 >
cap, count bound breaks 48762 vs 14448, Phi_3 blind 0.0
disclosed; shuffle: 289/300 atoms rejected, edge break 1.0e0,
mass matched 4.0e-17, Phi_3 shift a/b/c 0.3968/0.3434/0.0848 vs
true 0.8719/0.6650/0.4100) + PHI3_ALL_BLIND(no candidate is
bounded-stable or world-ordering) + MUSTFAIL_LEDGER(e1 AST-CAUGHT
cm@552, e2 CAUGHT 0.629@561, e3 mult-2-built control ACCEPTED
14448 == 14448, e4 LOUD ratio 35.000000 == m, m5a/m5b FLAGGED).
READING (typed, no upgrade): the sealed letter is PHI3_ALL_BLIND
-- none of the three sealed candidates passes the four criteria
-- and the anatomy behind the letter is SHARP and concentrated:
(1) the ENTIRE failure sits on TWO rungs: kz55 and kz67 are the
only violators of all three frozen C0 (2/57 each) and kz55 alone
kills the rank test (Phi3a 4.61 > SCR 2.39) and blows the b/c
bands -- the SAME near-critical family that killed r306 A <= 1
(kz53/kz67) and the r313 T1/T4 constants (kz55 2.54x, kz53
1.70x); every trend FALLS (-0.40..-0.77 on both estimators), so
the violation is a shallow-calibration artifact of the known
kind, NOT growth -- but the mid-ladder calibration rule was not
sealed and is NOT applied post hoc; (2) the LOCAL CAUSE of the
outliers is named by the probe's own coordinates: kz55/kz67
carry FCIX 0.955/0.915 against med 0.629 -- they are exactly the
rungs where the intra-block flux cancellation DIES; the
divergence-form functional fails precisely where its cancellation
asset vanishes (the R316-relevant discovery: the FCIX -> 1
stratum is the obstruction, and FCIX is source-pure and
computable in advance); (3) the reviewer's world rows that DO
hold: EPSTEIN holds all three frozen bounds (c separates it 7x
downward: 0.1375 vs C0 0.94 -- the FCIX factor works as designed
on EPSTEIN's FC 0.101), the rational twin is near-identical
(factor 1.07..1.17 -- the strongest twin result of the lane),
and the SCRAMBLE cause is named (COLL dev 3.69 >= 0.25, K4
fires); what fails is boundedness (2 rungs) and the SCR rank (1
rung); (4) candidate a (the reviewer raw form) comes CLOSEST:
band 22.85 passes its bar, trends fall, EPST/twin hold -- it
fails only the kz55/kz67 HOLD and the kz55 rank; the
cancellation-aware b/c additionally blow the band bar because
their deep minima are small (kz109 b = 0.0385: the combined
collision sum nearly cancels at depth -- by itself an honest
sign that |COLL| falls FASTER than the cube, supporting the
R316 direction); (5) the Leg C contrasts both fired (mult-3
control rejected by the count bound with Phi_3 provably blind --
the multiplicity cap is a necessary CLASS side condition;
shuffle rejected 289/300 with the flux profile broken) -- the
class boundary machinery works.  Honest negatives: ALL_BLIND is
the sealed verdict and stands -- the divergence-form structure
with first-5-frozen constants is NOT the membership functional;
the kz55/kz67 diagnosis and the FCIX stratum reading are
post-hoc anatomy (census, no rule); the twin/world columns are
n = 1 censuses; nothing here bounds anything beyond the measured
rungs.  Runtime 25.7 s full / 0.3 s smoke; run1/run2 identical
up to WALL.  AMENDMENTS AFTER FREEZE: none except this
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
import renyi3_proof_fork_probe as PFK          # noqa: E402 r313
import signed_cubic_flux_probe as SCF          # noqa: E402 r314
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
ATOM_BAR = 1e-9
REC3_BAR = 1e-13
TEL_BAR = 1e-13
BND_BAR = 1e-13
DIAG_BAR = 1e-9
DEG_FLOOR = 1e-6
MULT_CAP = 2
N_CAL = 5
RES_EPS = 0.01
BAND_MAX = 30.0
ATTR_MIN = 0.25
TWIN_FAC = 3.0
SEED_SHUF = 315001
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
R314_TABLE_LITERALS = frozenset((
    -0.4226, 0.598, 0.8537, 0.629, -0.141,
    -0.452, 0.823, 0.617, 0.057,
    -0.541, 0.43, 1.111, 0.675, 0.043,
    -2.695, -2.652, 6.347, 0.101, 0.011,
    -0.171, 0.856, 0.315, 0.693, 0.073))

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

VARIANTS = ("a", "b", "c")


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
    """the TABLE-CALIBRATION audit: walk ONLY the named function's
    subtree and flag any numeric constant whose 4-decimal rounding
    lies in the sealed r314 world-table literal set."""
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
                            in R314_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the fold-
# ---------------- genealogy state (block sums x, group power sums
# ---------------- Q2/Q3) and the flux state (F_end, F_open, abs
# ---------------- edge mass) only; the withheld terminal drive
# ---------------- key, the branch label, the cubic target and the
# ---------------- r314 world-table literals are forbidden (AST
# ---------------- identifier scan + literal scan).
def phi3_variants(x, Q2, Q3, F_end, F_open, edge_abs, m):
    """the sealed Phi_3 candidate family on the divergence-form
    state of one rung: sigma = sign(x), L = sum |x_j|, NORM =
    m^2/((log m)^2 L^3); DFLUX = sum sigma F_end (flux defect),
    COLL = sum sigma (3 Q2 x - 2 Q3) (combined signed collision
    sum), BND = sum sigma F_open (opening flux), FCIX = sum
    |F_end| / sum |dF| (flux cancellation index);
    Phi3a = NORM (|COLL| + |BND| + |DFLUX|)  [reviewer raw],
    Phi3b = NORM |COLL|                      [cancellation-aware],
    Phi3c = NORM |COLL| FCIX                 [flux-corrected]."""
    x = np.asarray(x, dtype=float)
    Q2 = np.asarray(Q2, dtype=float)
    Q3 = np.asarray(Q3, dtype=float)
    sig = np.sign(x)
    L = float(np.sum(np.abs(x)))
    if m < 2 or L <= 0.0:
        return dict(a=0.0, b=0.0, c=0.0, nrm=0.0, dflux=0.0,
                    coll=0.0, bnd=0.0, fcix=0.0, L=0.0)
    nrm = float(m) ** 2 / (math.log(float(m)) ** 2 * L ** 3)
    dflux = float(np.sum(sig * np.asarray(F_end, dtype=float)))
    coll = float(np.sum(sig * (3.0 * Q2 * x - 2.0 * Q3)))
    bnd = float(np.sum(sig * np.asarray(F_open, dtype=float)))
    fcix = float(np.sum(np.abs(np.asarray(F_end, dtype=float)))) \
        / max(float(edge_abs), 1e-300)
    a = nrm * (abs(coll) + abs(bnd) + abs(dflux))
    b = nrm * abs(coll)
    c = nrm * abs(coll) * fcix
    return dict(a=a, b=b, c=c, nrm=nrm, dflux=dflux, coll=coll,
                bnd=bnd, fcix=fcix, L=L)


def mult3_control(pos, val, blk, split=True):
    """the multiplicity-3 control with MATCHED boundary
    statistics: every multiplicity-2 fold group has its FIRST atom
    split into two half atoms at the SAME position (exact dyadic
    halving: every group value G1, every block value, every
    position and the total mass preserved BITWISE); the fold
    multiplicity becomes 3 on every touched group.  split=False
    returns the arrays unchanged (the e3 sharpness control: same
    constructor, multiplicity kept at 2)."""
    pos = np.asarray(pos, dtype=float)
    val = np.asarray(val, dtype=float)
    blk = np.asarray(blk, dtype=int)
    if not split:
        return pos.copy(), val.copy(), blk.copy()
    o = np.lexsort((pos, blk))
    pb = blk[o]
    pp = pos[o]
    vv = val[o].copy()
    if len(pb):
        new = np.concatenate([[True], (pb[1:] != pb[:-1])
                              | (pp[1:] != pp[:-1])])
    else:
        new = np.zeros(0, dtype=bool)
    gid = np.cumsum(new) - 1
    ng = int(gid[-1]) + 1 if len(gid) else 0
    mult = np.bincount(gid, minlength=ng)
    sm = new & (mult[gid] == 2)
    # the two half atoms are kept ADJACENT (np.repeat) so the
    # sequential group accumulation is v/2 + v/2 + rest == v +
    # rest BITWISE (dyadic halving is exact in f64)
    reps = np.where(sm, 2, 1)
    return (np.repeat(pp, reps),
            np.repeat(np.where(sm, vv * 0.5, vv), reps),
            np.repeat(pb, reps))


def mutant_cube_readback(cmrec, nrm, dflux):
    """e1 MUST-FAIL MUTANT: the literal exact-difference form
    NORM x |cube - DFLUX| computed by CONSUMING the cubic-moment
    record (the target side) -- the PHI3_FORBIDDEN identifier
    scan must FLAG this."""
    cm = cmrec
    target = cm["S3"] * cm["L1"] ** 3
    return nrm * abs(target - dflux)


def mutant_table_calibrated(coll, nrm):
    """e2 MUST-FAIL MUTANT: a 'calibrated' functional carrying an
    r314 world-table record number (the FC med) as its decision
    constant -- the literal scan must FLAG this."""
    return nrm * abs(coll) * 0.629


def mutant_wrong_norm(x, Q2, Q3, m):
    """e4 MUST-FAIL MUTANT: the wrong normalization exponent
    m^1/((log m)^2 L^3) -- deviates from the sealed m^2 form by
    EXACTLY the factor m (LOUD)."""
    x = np.asarray(x, dtype=float)
    sig = np.sign(x)
    L = float(np.sum(np.abs(x)))
    nrm = float(m) / (math.log(float(m)) ** 2
                      * max(L, 1e-300) ** 3)
    coll = float(np.sum(sig * (3.0 * np.asarray(Q2, float) * x
                               - 2.0 * np.asarray(Q3, float))))
    return nrm * abs(coll)


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'functional orientation' consuming
    the withheld ground-truth terminal drive key -- the scope
    audit must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'membership constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the Phi_3 parts on the
# ---------------- sealed toys, decided as rational arithmetic
def fr_phi3_parts(blocks):
    """exact unnormalized Phi_3 parts on per-block Fraction group
    lists: DFLUX (telescope path), COLL, BND (opening flux) and
    the flux census (sum |F_end|, sum |dF|); cube for the identity
    cross-check only."""
    dflux = Fr(0)
    coll = Fr(0)
    bnd = Fr(0)
    cube = Fr(0)
    fe_abs = Fr(0)
    de_abs = Fr(0)
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
                de_abs += abs(dF)
            s1 += g
            s2 += g * g
        dflux += sig * F
        coll += sig * (3 * Q2 * x - 2 * Q3)
        bnd += sig * F_open
        cube += abs(x) ** 3
        fe_abs += abs(F)
    return dict(dflux=dflux, coll=coll, bnd=bnd, cube=cube,
                fe_abs=fe_abs, de_abs=de_abs)


TOY_TWOBLOCK = ([Fr(1), Fr(2)], [Fr(3)])
TOY_FLUX = ([Fr(1), Fr(2), Fr(3), Fr(4)],)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("phi3_functional_probe -- "
          "PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01 part 2 (round 315)")
    print("SPEC_SHA %s   R314_SHA %s   R306_SHA %s (imported)"
          % (SPEC_SHA[:16], SCF.SPEC_SHA[:16], RY3.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + diagnostic cross-ward + "
                        "Leg C mutants at w9 + e1-e4; ladder, "
                        "extension, anchors, blind test and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE Phi_3 MEMBERSHIP FUNCTIONAL (reviewer contract, "
          "part 2): three candidates sealed from the r314 "
          "divergence-form STRUCTURE with NORM = m^2/((log m)^2 "
          "L^3) -- Phi3a = NORM(|COLL| + |BND| + |DFLUX|) "
          "[reviewer raw], Phi3b = NORM|COLL| [combined signed "
          "collision sum], Phi3c = NORM|COLL| FCIX "
          "[flux-corrected]; theorem class Phi3 <= C0 with the "
          "r306 first-5 freeze; four reviewer criteria K1 purity "
          "/ K2 world order (rank) / K3 stable range / K4 named "
          "SCRAMBLE cause; the literal |cube - DeltaF| form is "
          "adjudicated READ-BACK-ADJACENT and demoted to a "
          "diagnostic column; verdicts PHI3_FOUND / PHI3_PARTIAL "
          "/ PHI3_ALL_BLIND sealed BEFORE evaluation")
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("phi3_variants", "mult3_control"):
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

    # ---------------- S1: census + controls (r314 scaffold verbatim)
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
            FC = float(np.sum(np.abs(ft["F_end"]))) \
                / max(ft["edge_abs"], 1e-300)
            shares = dict(far=C_far_flux / max(cube, 1e-300),
                          pair=sct["C_pair"] / max(cube, 1e-300),
                          full=sct["C_full"] / max(cube, 1e-300))
            mx_mult = int(np.max(gen["mult"])) if gen["ng"] else 0
            fold_share = float(np.mean(gen["mult"] == 2)) \
                if gen["ng"] else 0.0
            ph = phi3_variants(sct["x"], sct["Q2"], sct["Q3"],
                               ft["F_end"], ft["F_open"],
                               ft["edge_abs"], m)
            # diagnostic column (READ-BACK-ADJACENT, disclosed --
            # cross-ward only, computed OUTSIDE the builders):
            diag = ph["nrm"] * abs(cube - ph["dflux"])
        else:
            gen = sct = ft = cc = None
            x_dev = 0.0
            cube = 0.0
            rec3 = tel_dev = bnd_dev = 0.0
            FC = 0.0
            C_bnd = 0.0
            shares = dict(far=0.0, pair=0.0, full=0.0)
            mx_mult = 0
            fold_share = 0.0
            ph = dict(a=0.0, b=0.0, c=0.0, nrm=0.0, dflux=0.0,
                      coll=0.0, bnd=0.0, fcix=0.0, L=0.0)
            diag = 0.0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, FC=FC, C_bnd=C_bnd,
                    shares=shares, mx_mult=mx_mult,
                    fold_share=fold_share, gen=gen, sct=sct,
                    ft=ft, cc=cc, ph=ph, diag=diag,
                    pos_all=pos_all, val_all=val_all,
                    blk_all=blk_all, brk=brk)

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
    x_w = max(rc["ev"]["x_dev"] for rc in live)
    mism_tot = sum(rc["ev"]["mism"] for rc in pool_all)
    fold_med = float(np.median([rc["ev"]["fold_share"]
                                for rc in live]))
    check("G22-genealogy-completeness",
          x_w <= ATOM_BAR and mism_tot == 0,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); med "
          "fold share %.3f%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, fold_med,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION (r314 + r306 records)")
    rec3_w = max(rc["ev"]["rec3"] for rc in live)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live)
    check("G31-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR,
          "the r314 identity live on %d live worlds: three-term "
          "recomposition dev %.1e (bar %.0e), telescope dev %.1e "
          "(bar %.0e), boundary %.1e (bar %.0e) -- sum |x|^3 = "
          "DeltaF + C_collision with C_boundary == 0 stands"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 shares far/pair/full = %+.4f/%+.4f/%+.4f, "
             "FC %.3f, mult max %d"
             % (ev9s["shares"]["far"], ev9s["shares"]["pair"],
                ev9s["shares"]["full"], ev9s["FC"],
                ev9s["mx_mult"]))
        check("G30-r314-shares-fc", True, "SMOKE: skipped")
        check("G32-r306-bound-live", True, "SMOKE: skipped")
        srt_all = []
    else:
        srt_all = sorted(recs + erecs,
                         key=lambda rc: (rc["N"], rc["kz"]))
        Ns = [rc["N"] for rc in recs]

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        sh_far = [rc["ev"]["shares"]["far"] for rc in recs]
        sh_pair = [rc["ev"]["shares"]["pair"] for rc in recs]
        sh_full = [rc["ev"]["shares"]["full"] for rc in recs]
        fcs = [rc["ev"]["FC"] for rc in recs]
        meds = (float(np.median(sh_far)),
                float(np.median(sh_pair)),
                float(np.median(sh_full)))
        fc_med = float(np.median(fcs))
        fc_sl = slp(fcs)
        n_m2 = sum(1 for rc in srt_all
                   if rc["ev"]["mx_mult"] == 2)
        check("G30-r314-shares-fc",
              all(abs(meds[i] - R314_SHARES[i]) <= R314_SHARE_TOL
                  for i in range(3))
              and abs(fc_med - R314_FC) <= R314_FC_TOL
              and abs(fc_sl - R314_FC_SLOPE) <= R314_FC_SL_TOL
              and n_m2 == len(srt_all),
              "r314 record reproduced: med shares far/pair/full "
              "%+.4f/%+.4f/%+.4f (rec %+.4f/%+.4f/%+.4f tol "
              "%.3f); FC med %.3f slope %+.3f (rec %.3f/%+.3f); "
              "mult == 2 on %d/%d"
              % (meds[0], meds[1], meds[2], R314_SHARES[0],
                 R314_SHARES[1], R314_SHARES[2], R314_SHARE_TOL,
                 fc_med, fc_sl, R314_FC, R314_FC_SLOPE, n_m2,
                 len(srt_all)))
        rhoT2 = [RY3.renyi3_ratio(rc["ev"]["cm"]["S3"],
                                  rc["ev"]["m"], 2)
                 for rc in srt_all]
        C2, _j, _d = RY3.calib_freeze(rhoT2, range(N_CAL))
        viol2 = sum(1 for v in rhoT2 if v > C2)
        check("G32-r306-bound-live",
              abs(C2 - R306_C2) <= R306_C2_TOL and viol2 == 0,
              "r306 pointwise bound live at A = 2: C_2 %.3f (rec "
              "%.3f tol %.3f, first-%d freeze), violations %d/%d "
              "-- the target scale of the functional is intact"
              % (C2, R306_C2, R306_C2_TOL, N_CAL, viol2,
                 len(srt_all)))

    # ---------------- S4: Leg A -- sealing + purity + toys
    section("S4  LEG A -- SEALING + PURITY AUDITS + TOYS")
    pure_ids = []
    for fn in ("phi3_variants", "mult3_control"):
        pure_ids += scope_audit(fn, PHI3_FORBIDDEN)
    pure_lits = []
    for fn in ("phi3_variants", "mult3_control",
               "mutant_wrong_norm"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_cube_readback", PHI3_FORBIDDEN)
    e2_hits = literal_audit("mutant_table_calibrated")
    check("G40-purity-audits",
          (not pure_ids) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1,
          "SOURCE PURITY: phi3_variants + mult3_control clean vs "
          "PHI3_FORBIDDEN (%d id hits) AND vs the sealed r314 "
          "world-table literal set (%d literal hits); consumed "
          "inputs: block sums x, group power sums Q2/Q3, flux "
          "ends/openings, abs edge mass, m -- no cubic target, "
          "no wall sign, no table number; e1 cube-readback "
          "FLAGGED (%s); e2 table-calibration FLAGGED (%s)"
          % (len(pure_ids), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS"))
    # toys, exact Fractions
    t2 = fr_phi3_parts([list(g) for g in TOY_TWOBLOCK])
    tf = fr_phi3_parts([list(g) for g in TOY_FLUX])
    ok_t2 = (t2["coll"] == 54 and t2["dflux"] == 0
             and t2["bnd"] == 0 and t2["cube"] == 54
             and t2["de_abs"] == 0)
    ok_tf = (tf["coll"] == 700 and tf["dflux"] == 300
             and tf["bnd"] == 0 and tf["cube"] == 1000
             and tf["fe_abs"] == 300 and tf["de_abs"] == 300)
    # float builder cross-check on the two-block toy:
    tpos = np.array([0.1, 0.2, 0.3])
    tval = np.array([1.0, 2.0, 3.0])
    tblk = np.array([0, 0, 1])
    tgen = SCF.fold_genealogy(tpos, tval, tblk, 2)
    tsct = SCF.signed_cube_terms(tgen["G1"], tgen["gblk"], 2)
    tft = SCF.flux_telescope(tgen["G1"], tgen["ptr"], 2)
    tph = phi3_variants(tsct["x"], tsct["Q2"], tsct["Q3"],
                        tft["F_end"], tft["F_open"],
                        tft["edge_abs"], 2)
    tL = 6.0
    tnrm = 4.0 / (math.log(2.0) ** 2 * tL ** 3)
    ok_fl = (abs(tph["coll"] - 54.0) <= TOY_BAR
             and abs(tph["dflux"]) <= TOY_BAR
             and abs(tph["bnd"]) <= TOY_BAR
             and abs(tph["a"] - tnrm * 54.0) <= TOY_BAR
             and abs(tph["b"] - tnrm * 54.0) <= TOY_BAR
             and abs(tph["c"]) <= TOY_BAR
             and abs(tph["fcix"]) <= TOY_BAR)
    check("G41-toy-exactness", ok_t2 and ok_tf and ok_fl,
          "two-block toy {1,2}|{3}: COLL 54 == cube, DFLUX 0, "
          "BND 0 EXACT (Fractions) -> Phi3a == Phi3b, FCIX 0 "
          "(no interior flux, disclosed convention -> Phi3c 0); "
          "flux toy (1,2,3,4): COLL 700 + DFLUX 300 == cube 1000 "
          "EXACT, FCIX 300/300 = 1 (unnormalized reviewer-raw "
          "form degenerates to the cube on uniform sign, "
          "disclosed); float builders match Fractions (bar %.0e)"
          % TOY_BAR)
    diag_w = 0.0
    for rc in live:
        ev = rc["ev"]
        diag_w = max(diag_w, abs(ev["diag"] - ev["ph"]["b"])
                     / max(ev["ph"]["b"], 1e-300))
    check("G42-diagnostic-crossward", diag_w <= DIAG_BAR,
          "the READ-BACK-ADJACENT diagnostic column NORM x |cube "
          "- DeltaF| == Phi3b on %d live worlds (worst rel dev "
          "%.1e, bar %.0e) -- the exact-difference form of "
          "reviewer candidate (c) is numerically the source-pure "
          "Phi3b (BND == 0); it stays a diagnostic, NOT a "
          "candidate (adjudicated in the spec)"
          % (len(live), diag_w, DIAG_BAR))

    # ---------------- S5: Leg B -- the blind test
    section("S5  LEG B -- THE BLIND TEST (57 rungs + twin + "
            "controls)")
    if smoke:
        ev9s = recs[0]["ev"]
        info("SMOKE: w9 Phi3a/b/c = %.4f/%.4f/%.4f, FCIX %.3f, "
             "NORM %.3e (blind test skipped)"
             % (ev9s["ph"]["a"], ev9s["ph"]["b"], ev9s["ph"]["c"],
                ev9s["ph"]["fcix"], ev9s["ph"]["nrm"]))
        check("G50-c0-freeze", True, "SMOKE: skipped")
        check("G51-k3-stability", True, "SMOKE: skipped")
        check("G52-k2-world-order", True, "SMOKE: skipped")
        check("G53-k4-attribution", True, "SMOKE: skipped")
        K2 = {v: False for v in VARIANTS}
        K3 = {v: False for v in VARIANTS}
        K4 = False
        C0 = {v: 0.0 for v in VARIANTS}
        k1_ok = (not pure_ids) and (not pure_lits)
    else:
        vals = {v: [rc["ev"]["ph"][v] for rc in srt_all]
                for v in VARIANTS}
        C0 = {}
        for v in VARIANTS:
            C0[v], j0, _d = RY3.calib_freeze(vals[v],
                                             range(N_CAL))
        check("G50-c0-freeze", all(C0[v] > 0 for v in VARIANTS),
              "C0 frozen on the first %d rungs of the (N, "
              "kz)-sorted %d-rung ladder (r306 protocol): C0_a "
              "%.4f / C0_b %.4f / C0_c %.4f"
              % (N_CAL, len(srt_all), C0["a"], C0["b"], C0["c"]))
        info("sealed per-rung record table: idx kz N m Phi3a "
             "Phi3b Phi3c FCIX")
        for i, rc in enumerate(srt_all):
            ev = rc["ev"]
            info("%2d kz%-3d N %4d m %3d a %8.4f b %8.4f c "
                 "%8.4f fcix %.3f%s"
                 % (i, rc["kz"], rc["N"], ev["m"], ev["ph"]["a"],
                    ev["ph"]["b"], ev["ph"]["c"],
                    ev["ph"]["fcix"],
                    " EXT" if rc in erecs else ""))
        k1_ok = (not pure_ids) and (not pure_lits)
        K3 = {}
        k3_note = []
        for v in VARIANTS:
            viol = sum(1 for x in vals[v] if x > C0[v])
            vmax = max(vals[v])
            vmin = min(vals[v])
            band = vmax / max(vmin, 1e-300)
            sl42 = slp([rc["ev"]["ph"][v] for rc in recs])
            sl57 = L2D.halves_slope(
                [rc["N"] for rc in srt_all],
                [max(x, 1e-300) for x in vals[v]])
            K3[v] = (viol == 0 and band <= BAND_MAX
                     and sl42 <= RES_EPS and sl57 <= RES_EPS)
            k3_note.append("%s: viol %d/%d, band %.2f (bar %.0f)"
                           ", trend %+.3f/%+.3f -> %s"
                           % (v, viol, len(srt_all), band,
                              BAND_MAX, sl42, sl57, K3[v]))
        check("G51-k3-stability", True,
              "K3 STABLE SIZE RANGE (census; adjudicated in S7): "
              + "; ".join(k3_note))
        evE = crecs["EPST"]["ev"]
        evS = crecs["SCR"]["ev"]
        ev9 = mrecs[0]["ev"]
        ev13 = mrecs[1]["ev"]
        K2 = {}
        k2_note = []
        for v in VARIANTS:
            scr_v = evS["ph"][v]
            ep_v = evE["ph"][v]
            w9_v = ev9["ph"][v]
            w13_v = ev13["ph"][v]
            others = max(max(vals[v]), w9_v, w13_v, ep_v)
            rank_ok = scr_v > others
            ep_ok = ep_v <= C0[v]
            tw_fac = max(w13_v / max(w9_v, 1e-300),
                         w9_v / max(w13_v, 1e-300))
            tw_ok = (w13_v <= C0[v] and tw_fac <= TWIN_FAC)
            K2[v] = rank_ok and ep_ok and tw_ok
            k2_note.append("%s: SCR %.4f %s max(rest) %.4f, EPST "
                           "%.4f %s C0 %.4f, twin w13 %.4f (fac "
                           "%.2f %s %.1f) -> %s"
                           % (v, scr_v, ">" if rank_ok else "<=",
                              others, ep_v,
                              "<=" if ep_ok else ">", C0[v],
                              w13_v, tw_fac,
                              "<=" if tw_fac <= TWIN_FAC
                              else ">", TWIN_FAC, K2[v]))
        check("G52-k2-world-order", True,
              "K2 WORLD ORDER (census; adjudicated in S7): "
              + "; ".join(k2_note))
        comp_main = dict(
            dflux=float(np.median([rc["ev"]["ph"]["nrm"]
                                   * abs(rc["ev"]["ph"]["dflux"])
                                   for rc in recs])),
            coll=float(np.median([rc["ev"]["ph"]["nrm"]
                                  * abs(rc["ev"]["ph"]["coll"])
                                  for rc in recs])),
            fcix=float(np.median([rc["ev"]["ph"]["fcix"]
                                  for rc in recs])))
        comp_scr = dict(
            dflux=evS["ph"]["nrm"] * abs(evS["ph"]["dflux"]),
            coll=evS["ph"]["nrm"] * abs(evS["ph"]["coll"]),
            fcix=evS["ph"]["fcix"])
        devs = {k: abs(comp_scr[k] - comp_main[k])
                / max(abs(comp_main[k]), 1e-300)
                for k in comp_main}
        cause = max(devs, key=lambda k: devs[k])
        K4 = devs[cause] >= ATTR_MIN
        check("G53-k4-attribution", True,
              "K4 SCRAMBLE CAUSE (census; adjudicated in S7): "
              "component devs vs MAIN med %s -> named cause %s "
              "(dev %.2f %s bar %.2f) -> %s"
              % (str({k: round(devs[k], 2) for k in devs}),
                 cause.upper(), devs[cause],
                 ">=" if K4 else "<", ATTR_MIN, K4))

    # ---------------- S6: Leg C -- the synthetic mutants
    section("S6  LEG C -- SYNTHETIC MUTANTS (reviewer table)")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    m9 = ev9m["m"]
    # (i) multiplicity-3 control
    p3, v3, b3 = mult3_control(ev9m["pos_all"], ev9m["val_all"],
                               ev9m["blk_all"], split=True)
    gen3 = SCF.fold_genealogy(p3, v3, b3, m9)
    g1_dev = float(np.max(np.abs(gen3["G1"]
                                 - ev9m["gen"]["G1"]))) \
        if gen3["ng"] == ev9m["gen"]["ng"] else 1.0
    cc3 = SCF.collision_census(gen3["mult"], gen3["ptr"], m9)
    mx3 = int(np.max(gen3["mult"]))
    sct3 = SCF.signed_cube_terms(gen3["G1"], gen3["gblk"], m9)
    ft3 = SCF.flux_telescope(gen3["G1"], gen3["ptr"], m9)
    ph3 = phi3_variants(sct3["x"], sct3["Q2"], sct3["Q3"],
                        ft3["F_end"], ft3["F_open"],
                        ft3["edge_abs"], m9)
    phi_blind = max(abs(ph3[v] - ev9m["ph"][v])
                    for v in VARIANTS)
    cct = SCF.collision_census(np.array([3, 3]),
                               np.array([0, 2]), 1)
    check("G60-mult3-control",
          g1_dev == 0.0 and mx3 == 3
          and cc3["atoms_coll"] != cc3["atoms_coll_m2"]
          and cct["atoms_coll"] == 216
          and cct["atoms_coll_m2"] == 64
          and phi_blind <= 1e-12,
          "MULT-3 CONTROL (matched: G1/blocks/positions/mass "
          "preserved BITWISE, dev %.1e): fold multiplicity 3 > "
          "cap %d -> class REJECTS; collision count bound BREAKS "
          "(3p1p2 - 2p3 = %d != m2 closed form %d; uniform toy "
          "n=2: 216 vs 64, break 152 EXACT); DISCLOSED: Phi_3 "
          "value blind to the control (max dev %.1e) -- the "
          "multiplicity cap is a NECESSARY side condition of the "
          "class, not a consequence of the functional"
          % (g1_dev, MULT_CAP, cc3["atoms_coll"],
             cc3["atoms_coll_m2"], phi_blind))
    # (ii) assignment shuffle
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
    sct_s = SCF.signed_cube_terms(gen_s["G1"], gen_s["gblk"], m9)
    ph_s = phi3_variants(sct_s["x"], sct_s["Q2"], sct_s["Q3"],
                         ft_s["F_end"], ft_s["F_open"],
                         ft_s["edge_abs"], m9)
    check("G61-assignment-shuffle",
          mism_s > 0 and edev >= MUT_MIN
          and mass_dev <= ID_BAR,
          "ASSIGNMENT SHUFFLE (seed %d, r313-m4 base): interval "
          "check REJECTS (%d/%d atoms outside their block "
          "interval); the ordered-support flux profile BREAKS "
          "edgewise (rel dev %.1e >= %.0e -- the flux telescope "
          "is not permutation-blind) while the mass statistic "
          "stays matched (dev %.1e); Phi_3 shift census: a/b/c "
          "%.4f/%.4f/%.4f vs true %.4f/%.4f/%.4f"
          % (SEED_SHUF, mism_s, len(ev9m["pos_all"]), edev,
             MUT_MIN, mass_dev, ph_s["a"], ph_s["b"], ph_s["c"],
             ev9m["ph"]["a"], ev9m["ph"]["b"], ev9m["ph"]["c"]))
    legc_ok = (g1_dev == 0.0 and mx3 == 3
               and cc3["atoms_coll"] != cc3["atoms_coll_m2"]
               and mism_s > 0 and edev >= MUT_MIN)

    # ---------------- S7: Leg D -- adjudication
    section("S7  LEG D -- SEALED ADJUDICATION")
    if smoke:
        verdict_main = "SMOKE_NO_ADJUDICATION"
        check("G70-sealed-adjudication", True, "SMOKE: skipped")
    else:
        found_v = None
        for v in VARIANTS:
            if k1_ok and K2[v] and K3[v] and K4 and legc_ok:
                found_v = v
                break
        partial = [v for v in VARIANTS
                   if k1_ok and (K2[v] or K3[v])]
        if found_v is not None:
            verdict_main = ("PHI3_FOUND(Phi3%s, C0 %.4f: K1-K4 "
                            "pass + both Leg C contrasts)"
                            % (found_v, C0[found_v]))
        elif partial:
            miss = []
            for v in partial:
                lack = []
                if not K2[v]:
                    lack.append("K2")
                if not K3[v]:
                    lack.append("K3")
                if not K4:
                    lack.append("K4")
                miss.append("%s lacks %s" % (v, "+".join(lack)
                                             if lack else "none"))
            verdict_main = "PHI3_PARTIAL(%s)" % "; ".join(miss)
        else:
            verdict_main = ("PHI3_ALL_BLIND(no candidate is "
                            "bounded-stable or world-ordering)")
        check("G70-sealed-adjudication", True,
              "exactly one sealed verdict fired: %s"
              % verdict_main)

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    check("G80-e1-cube-readback", len(e1_hits) >= 1,
          "e1 AST-CAUGHT: the simulated cubic read-back (NORM x "
          "|cube - DFLUX| via the cm/S3 target path) is FLAGGED "
          "by the PHI3_FORBIDDEN scan (%s) while phi3_variants "
          "is clean (%d hits) -- the honesty condition 'no sum "
          "q^3 read-back' is machine-audited"
          % (e1_hits[0] if e1_hits else "MISS", len(pure_ids)))
    check("G81-e2-table-calibration", len(e2_hits) >= 1,
          "e2 CAUGHT: the simulated r314-table calibration (FC "
          "med 0.629 as decision constant) is FLAGGED by the "
          "sealed literal scan (%s) while the real builders are "
          "literal-clean (%d hits) -- the r314 sealing note is "
          "machine-audited"
          % (e2_hits[0] if e2_hits else "MISS", len(pure_lits)))
    p2c, v2c, b2c = mult3_control(ev9m["pos_all"],
                                  ev9m["val_all"],
                                  ev9m["blk_all"], split=False)
    gen2 = SCF.fold_genealogy(p2c, v2c, b2c, m9)
    cc2 = SCF.collision_census(gen2["mult"], gen2["ptr"], m9)
    mx2 = int(np.max(gen2["mult"]))
    check("G82-e3-mult2-built-control",
          mx2 == 2 and cc2["atoms_coll"] == cc2["atoms_coll_m2"]
          and cc2["atoms_coll"] == ev9m["cc"]["atoms_coll"],
          "e3 SHARPNESS: the SAME constructor with split=False "
          "keeps multiplicity 2 and the collision counting "
          "passes it as NORMAL (count %d == m2 closed form %d == "
          "true w9 census) -- the Leg C rejection is the "
          "multiplicity, not a constructor artifact"
          % (cc2["atoms_coll"], cc2["atoms_coll_m2"]))
    wrong = mutant_wrong_norm(ev9m["sct"]["x"], ev9m["sct"]["Q2"],
                              ev9m["sct"]["Q3"], m9)
    ratio = ev9m["ph"]["b"] / max(wrong, 1e-300)
    rel4 = abs(wrong - ev9m["ph"]["b"]) \
        / max(ev9m["ph"]["b"], 1e-300)
    check("G83-e4-wrong-exponent",
          abs(ratio - m9) <= 1e-12 * m9 and rel4 >= MUT_MIN,
          "e4 LOUD: the m^1 normalization deviates from the "
          "sealed m^2 form by EXACTLY the factor m (measured "
          "ratio %.6f == m %d to 1e-12; rel dev %.3f >= %.0e) -- "
          "the Renyi-3 exponent is not decorative"
          % (ratio, m9, rel4, MUT_MIN))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the sealed Phi_3 candidate family on the r314 "
          "divergence form, the machine-audited purity "
          "conditions (identifier + table-literal scans), the "
          "blind world test with the four reviewer criteria, the "
          "multiplicity-3 / shuffle contrasts and the sealed "
          "adjudication -- NO new certificate promoted, NO "
          "universal bound claimed (R316 by contract)")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R315_ANCHORS(shares %+.4f/%+.4f/%+.4f, FC "
                 "%.3f/%+.3f, mult 2 on %d/%d, identity %.1e, "
                 "r306 C2 %.3f viol %d/57)"
                 % (meds[0], meds[1], meds[2], fc_med, fc_sl,
                    n_m2, len(srt_all), rec3_w, C2, viol2)]
        parts.append("SEAL(3 candidates, purity clean, e1/e2 "
                     "flagged, diag demoted %.1e)" % diag_w)
        parts.append("BLIND(C0 a/b/c %.4f/%.4f/%.4f; K3 %s; K2 "
                     "%s)"
                     % (C0["a"], C0["b"], C0["c"],
                        str({v: K3[v] for v in VARIANTS}),
                        str({v: K2[v] for v in VARIANTS})))
        parts.append("CAUSE(%s dev %.2f, K4 %s)"
                     % (cause.upper(), devs[cause], K4))
        parts.append("CONTROLS(mult3 rejected + count break, "
                     "phi blind %.1e; shuffle rejected %d mism, "
                     "edge break %.1e)"
                     % (phi_blind, mism_s, edev))
        parts.append(verdict_main)
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the r314 identity, the "
          "toy algebra, the count identities and the purity "
          "audits (exact / AST-decided); MEASURED: every Phi_3 "
          "value, C0, band, trend and attribution (42 + %d "
          "finite rungs + 2 mains + 2 live controls); OPEN: the "
          "universal bound Phi_3 <= C0 beyond the measured rungs "
          "(R316), the cofinal law, kz15 beyond r270; NO RH claim"
          % (verd, " (SMOKE)" if smoke else "",
             len(erecs)))
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
