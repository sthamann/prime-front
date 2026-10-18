#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""exception_families_probe -- PRIME.L2.RENYI3.EXCEPTION_FAMILIES.01
(round 317): THE EXCEPTION-FAMILY CENSUS -- reviewer fork (b) after
the r314-r316 trilogy (identity exact, functional blind, two-regime
dead): the statement form "ALL sufficiently large GENERIC windows +
explicitly classified EXCEPTION FAMILIES".  The reviewer contract is
verbatim and binding: FAMILIES, not single table rows --
    whole family --+-- generic regime      => Renyi-3 theorem
                   +-- spike class A       => separate certificate
                   +-- spike class B       => separate certificate
-- and the HARD GATE, sealed in advance: AT MOST TWO source-pure
exception families plus the generic theorem; "if ever new exception
forms keep appearing, abort immediately -- then the route is not a
classification but Whac-A-Mole" => verdict WHAC_A_MOLE, recommend
back to fork (a).  Context (sealed record inputs): r306 (SPEC
3bb365e1) fixed the pointwise GO sum q^3 <= 1.069 (log m)^2/m^2 on
57/57 (first-5 constant, r316-rehabilitated as load-bearing;
sharpness witnesses kz53/kz67 at A = 1); r316 (SPEC 5c28b12b)
sealed TWO_REGIME_DEAD and delivered the anatomy: the obstruction
family {kz53, kz55, kz67, kz83, kz105, ...} cuts ACROSS the FCIX
strata; kz55/kz67 are near-ONE-BLOCK worlds (top-1 cube share
0.558/0.785 vs 0.18 med -- the CONCENTRATION class) while
kz53/kz83 are rho_2 spikes at BULK-NORMAL FCIX (a DIFFERENT
class); 8/38 mid-ladder violators of the L bound; 21 small-m
certificates exist; 8 EXT2 deep anchors with NO new H member.
kz15 permanently closed via r270; the 6 exceptions via the r287
F2 certificates.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: r318 (base fork) and r319 (chain audit) run in
parallel; this probe touches NOTHING outside its own file and the
strictly additive rh-sync.

THE OBJECT (r269/r287/r298/r306/r314/r315/r316 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval); F =
0.20 edge split; maximal same-sign runs of the bx-sorted bulk;
level-2 blocks (r270 convention); the frozen positional block
machinery (r298 WBT.block_breaks + WBT.aggregate_blocks); the
r306 RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze; the
r314 SCF.fold_genealogy + SCF.signed_cube_terms +
SCF.flux_telescope + SCF.collision_census; the r315
PHI.phi3_variants; the r316 TRB.two_regime_state +
TRB.split_midladder, ALL imported verbatim; PDelta = Pbeta -
Pomega; x_j = (PDelta)_j.  NEW in this round (module-own,
source-pure): the two class functionals (rank-local spike
ratios), the sealed gap-threshold rule, the family-certificate
bookkeeping with declared-set ward, and the hard two-family gate.

THE SEALED CLASS FUNCTIONALS (frozen BEFORE any bound evaluation
of this round; both consume ONLY source-pure columns of the r316
two-regime state -- no cubic target, no wall sign, no record
literal; AST identifier scan + literal scan warded, must-fail e3
proves the audit bites).  On the (N, kz)-sorted class ladder of n
rungs (the r316 ladder: 42 core + 15 r286 extension + the 8 EXT2
anchors, multiplicity cap <= 2, POSITIVE_PREFIX), with QMAX(i) =
max_j |x_j| / L and PhiL2(i) = NORM x (|COLL| + |BND| + FE) the
sealed r316 columns (both source-pure by the r316 audit):
    F_A(i) = QMAX(i)  / med{ QMAX(j)  : |j - i| <= W, j != i },
    F_B(i) = PhiL2(i) / med{ PhiL2(j) : |j - i| <= W, j != i },
rank-local spike ratios with window half-width W = CLS_W = 5
(truncated at the ladder ends; DISCLOSED boundary property: a
monotone column trend of rate r per rung induces an end bias of
order r^W -- at the recorded ladder decay rates ~3 percent per
rung this is <= ~1.16, far below the gap bar; measured live and
printed as census; the trend toy proves the construction is
blind to a pure geometric trend at the ladder rate).  CLASS A
(CONCENTRATION) = the rungs with F_A >= THR_A; CLASS B
(DIVERGENCE-MASS SPIKE) = the rungs with F_B >= THR_B.  THE
SEALED GAP-THRESHOLD RULE (both classes, identical, frozen here):
sort the functional values descending as s_1 >= s_2 >= ...; over
prefix sizes k = 1..KMAX = 6 compute the multiplicative gap g_k =
s_k / s_{k+1}; k* = argmax g_k; the class is the top-k* rungs iff
g_{k*} >= GAP_MIN = 1.25, otherwise the class is EMPTY; THR =
sqrt(s_{k*} x s_{k*+1}) (geometric midpoint), printed and frozen.
The full class table (rank, kz, N, m, QMAX, F_A, PhiL2, F_B,
membership) is printed BEFORE any bound table of this round.
JUSTIFICATION (disclosed, from the r316 RECORD census only): the
r316 named discriminator was the top-1 cube share (dev 2.68) --
its source-pure sibling is QMAX (dev 1.99), so class A tracks the
near-one-block family {kz55, kz67}; the r316 regime-L freeze died
on PhiL2 spikes (kz53 1.43 / kz105 1.13 / kz83 1.08 vs C_L
0.7476), so class B tracks the rho_2-spike family -- both chosen
from the record ANATOMY, no value of this round consumed.

THE HARD GATE (sealed, live, symmetric): the adjudication accepts
EXACTLY the two sealed families (seal_family_count == 2 is a
warded module rule; the e1 mutant proves a third family is
REFUSED).  Let viol = the violators of the generic bound (Leg B)
on the complement test set.  Since the complement excludes A u B
by construction, EVERY violator is uncovered, so the sealed rule
    GENERIC_FAILS            iff |viol| >= GEN_FAIL_MIN = 5
        (the generic law itself fails broadly -- not a spike
        census; the classification question is moot),
    WHAC_A_MOLE              iff 1 <= |viol| <= GEN_FAIL_MIN - 1
        (a third exception form would be needed -- NO third
        class is added, the round aborts by contract), OR
        |viol| = 0 but a family GROWS with depth or the world/
        class check leaks (the classification leaks -- named),
    EXCEPTION_CENSUS_GO(A,B) iff |viol| = 0, both families
        non-empty, neither grows, world check passes,
    ONE_FAMILY_SUFFICES(X)   iff |viol| = 0, exactly one family
        non-empty (or NONE -- the generic theorem alone covers
        the ladder), no growth, world check passes.
Exactly one fires; the verdict function gate_verdict consumes
counts only and is itself scope-audited.

LEG 0 -- ANCHOR REGRESSION (r314/r315/r306/r316 record numbers
adopted as-is, disclosed): med signed shares DeltaF/C_pair/C_full
= -0.4226/+0.5980/+0.8537 (tol 0.005); FC med 0.629 (tol 0.005)
slope -0.141 (tol 0.01); fold multiplicity == 2 UNIFORM (exact);
identity wards live (REC3/TEL/BND bars); r306 C_2 = 1.069 (tol
0.005) first-5 freeze, 0/57; r315 C0 a/b/c = 2.6261/1.5052/0.9400
(tol 0.005), FCIX outliers kz55/kz67 = 0.955/0.915 (tol 0.005);
r316 anchors: class ladder n = 65 with the H stratum EXACTLY
{kz55, kz67} at theta = 0.85, the r316 mid-ladder split small
0..20 / cal 21..25 / test 26..64 with m_0 = 73 EXACT, regime-L
cal constant C_L2 = 0.7476 (tol 0.005), the 8 regime-L test
violators == {kz53, kz105, kz83, kz71, kz68, kz88, kz76, kz119}
EXACT as a set, TOP1 kz55/kz67 = 0.558/0.785 (tol 0.005), rho_2
anchors kz53/kz67/kz55/kz83 = 1.0490/1.0536/0.4821/0.7790 (tol
0.005), C_small = 1.0694 (tol 0.005) at kz18.

LEG A -- FAMILY DEFINITION (sealed BEFORE any bound evaluation):
(A1) the class functionals, the gap rule and the hard gate are
printed as sealed definitions; the class table (source-pure
columns only) is printed BEFORE any bound table.  (A2) SOURCE-
PURITY AUDITS: the AST identifier scan over local_ratio +
gap_threshold must be clean against BOUND_FORBIDDEN and
PHI3_FORBIDDEN (no cubic-target read-back, no withheld key); the
literal scan over local_ratio + gap_threshold + family_cert +
gate_verdict + seal_family_count must be clean against the sealed
record-literal set R31X_TABLE_LITERALS (r314 + r315 + r316 record
numbers); e1/e2/e3 prove the audits bite.  (A3) TOY EXACTNESS:
the spike toy (1,1,8,1,1,1,1) gives F = (1,1,8,1,1,1,1), k* = 1,
THR^2 == 8 EXACT, members == (2,); the flat toy (3 x 7) gives
class EMPTY EXACT (gap 1 < 1.25); the TREND toy 0.97^i (i =
0..10, the recorded ladder decay rate) gives class EMPTY with max
ratio <= 1.15 -- the rank-local construction is blind to a pure
trend; the family-certificate toy (max over the declared member
set, declared == members warded) and the gate toys (all five
verdict branches) are exact.  (A4) LIVE MAJORANT CHAIN WARD (the
r316 algebra re-warded): rho_2 <= PhiL1 <= PhiL2 <= PhiH2 and
rho_2 <= PhiH1 on every live world (rel slack <= CHAIN_BAR) plus
NORM x cube == rho_2 -- the class-A structural bound rho_2 <=
PhiH1 = (m QMAX/log m)^2 (Sum q^3 <= QMAX^2 Sum q, exact algebra)
and the class-B structural bound rho_2 <= PhiL2 transfer every
certificate below to sum q^3 by algebra.  (A5) MEMBERSHIP CENSUS:
which rungs fall in A, B, both, neither; per-third counts; the
boundary-bias census (max non-member |F - 1|).

LEG B -- THE GENERIC THEOREM (on the complement of A u B): the
complement ladder keeps the (N, kz) order; the r316 mid-ladder
split rule (TRB.split_midladder verbatim: CAL_START = n_comp //
3, N_CAL = 5) yields small-m / calibration / test; C_gen = max
rho_2 over the calibration window, FROZEN; certification = 0
violations demanded on every complement test rung; small-m rungs
certified INDIVIDUALLY (C_small = max); reserve min/med and the
halves-slope trend printed as census (the r316 lesson: with the
spikes EXCEPTED, does the rest hold with stable or growing
reserve?); m_0 = min m over calibration + test.

LEG C -- THE FAMILY CERTIFICATES (r287-F2 spirit: the exception
property implies its own certificate; r270-kz15 honesty: where
only per-member finite certificates exist, they are counted as
such): CLASS A (concentration): per member the finite certificate
rho_2 (C_A = max), the structural column PhiH1 (the class
DEFINITION delivers the concentration majorant: near-one-block =>
sum q^3 <= QMAX^2, warded exact in A4) and the qmax <= 1 - delta
census; CLASS B (spike): per member the finite certificate rho_2
(C_B = max) and the structural column PhiL2 (exact majorant,
warded); DEPTH-GROWTH CENSUS per family: member counts over the
ladder thirds T1/T2/T3 (ranks < n/3, < 2n/3, rest); the sealed
growth rule GROWS(F) iff the counts are STRICTLY increasing
T1 < T2 < T3 (a growing family = bad, finite/stable =
acceptable); EXT2-stratum member count printed.

LEG D -- THE COMPOSED THEOREM CANDIDATE + WORLD CHECK: world_ok =
the r316 class machinery verbatim -- (w1) w9/w13/EPSTEIN ADMITTED
(fold multiplicity <= 2 AND rho_2 <= C_tot; their class-column
values printed as census only); (w2) twin band max(w13/w9,
w9/w13) <= TWIN_FAC = 3.0 on PhiL2; (w3) SCRAMBLE REJECTED by the
class machinery (component attribution names a collision/flux
column, dev >= ATTR_MIN = 0.25 vs the MAIN med, AND the seeded
assignment shuffle SEED_SHUF = 317001 breaks the flux profile
edgewise >= MUT_MIN with matched mass).  C_tot = max(C_gen, C_A,
C_B, C_small).  The verdict fires by the sealed hard gate above;
on EXCEPTION_CENSUS_GO or ONE_FAMILY_SUFFICES the CANDIDATE
THEOREM (Renyi-3 with exception families) is printed with every
measured constant: generic theorem (C_gen, A = 2, m_0, mid-ladder
frozen) + class-A certificate + class-B certificate + C_small +
the counting evidence that A u B covers ALL violators on the
available ladder (0 uncovered) and does not grow with depth;
C_tot transfers to sum q^3 <= C_tot (log m)^2/m^2 on every
measured rung and n_eff = N_2 >= N_3 >= m/(sqrt(C_tot) log m) by
the r306 exact chain.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) THIRD CLASS PUSHED AFTER SIGHT (simulated):
  mutant_third_class collects the uncovered violators of the
  evaluated bound column into a post-hoc "class C" -- the
  BOUND_FORBIDDEN scope audit must FLAG it (it consumes rho) AND
  the sealed gate must REFUSE it twice: seal_family_count((A, B,
  C)) == False and gate_verdict with uncovered violators returns
  WHAC_A_MOLE, never a three-family GO -- GATE-CAUGHT.
(e2) THRESHOLD MOVED AFTER SIGHT: mutant_thr_posthoc re-picks the
  threshold to cover the seen violators (consumes rho) -- the
  scope audit must FLAG it AND on the sealed toy it returns a
  threshold != the gap rule's -- CAUGHT twice.
(e3) CLASS FUNCTIONAL READS Sum q^3: mutant_class_readback
  consumes the cubic-moment record (cm/S3) -- the PHI3_FORBIDDEN
  scan must FLAG it (AST-CAUGHT) while local_ratio +
  gap_threshold stay clean.
(e4) FAMILY CERTIFICATE CONSUMES THE GENERIC CONSTANT CIRCULARLY:
  mutant_circular_cert declares the generic calibration window
  instead of the member set -- the declared-set ward must CATCH
  the mismatch EXACT, and on the toy the circular "certificate"
  sits LOUDLY below the member maximum (diff >= MUT_MIN).
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.  Scope hygiene: the class
  builders (local_ratio, gap_threshold) consume one source-pure
  column + rank order only; family_cert / gate_verdict /
  seal_family_count consume certificate values / counts only;
  fragment audit (no fit primitives).

INDEX FIREWALL (binding, r238-r316 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target sum q^3 / rho_2 enters GATES / anchors /
certificates / diagnostic columns only, NEVER a class builder
(AST-warded); no zero/prime oracles anywhere (AST firewall); no
fit primitives (fragment audit).  MACHINERY IMPORTED VERBATIM:
r316 TRB.two_regime_state + TRB.split_midladder, r315
PHI.phi3_variants, r314 SCF.fold_genealogy + SCF.signed_cube_terms
+ SCF.flux_telescope + SCF.collision_census, r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze, r298
WBT.block_breaks + WBT.aggregate_blocks, r269 PBB.mask_edge +
PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed, r316 verbatim): frame-A h <= 900, 42 rungs, (N,
kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52};
EXTENSION: 900 < h <= 1300, first 15 by (N, kz); EXT2: the r316
A5 rule (leftover pool + first 12 windows 1300 < h <= 1650, first
8 POSITIVE_PREFIX by (N, kz)).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; XW_BAR 1e-9;
DEG_FLOOR 1e-6; MULT_CAP 2; THETA 0.85 (r316 anchor only); N_CAL
5; CAL_THIRD 3; CLS_W 5; GAP_MIN 1.25; KMAX 6; GEN_FAIL_MIN 5;
TREND_TOY_BAR 1.15; RES_EPS 0.01; ATTR_MIN 0.25; TWIN_FAC 3.0;
SEED_SHUF 317001; MUT_MIN 1e-6; TOY_BAR 1e-12; TB_WARD bars 1e-9
main N <= 400 / 3e-6 deep + ext + ext2 / 1e-6 controls; ID_BAR
1e-12; AC_BAR 1e-9; R314 anchors shares (-0.4226, +0.5980,
+0.8537) tol 0.005, FC 0.629/-0.141 tol 0.005/0.01, mult == 2
EXACT; R306 anchor C_2 1.069 tol 0.005; R315 anchors C0 (2.6261,
1.5052, 0.9400) tol 0.005, FCIX {55: 0.955, 67: 0.915} tol 0.005;
R316 anchors: N317 = 65, H set {55, 67}, split (small 0..20, cal
21..25, test 26..64), M0_REF 73, C_L2 0.7476 tol 0.005, violator
set {53, 105, 83, 71, 68, 88, 76, 119} EXACT, TOP1 {55: 0.558,
67: 0.785} tol 0.005, RHO {53: 1.0490, 67: 1.0536, 55: 0.4821,
83: 0.7790} tol 0.005, C_SMALL 1.0694 tol 0.005 at kz18;
R31X_TABLE_LITERALS = the sealed r314 + r315 forbidden set (r316
verbatim) UNION the r316 record set {0.7476, 0.5531, 1.4263,
1.1266, 1.0804, 0.9648, 0.8013, 0.7877, 0.7819, 0.7698, 34.0556,
3.0559, 57.3, 47.86, 2.76, 7.84, 0.558, 0.785, 0.105, 0.387,
21.7, 24.9, 31.9, 40.4, 1.0694, 0.4821, 1.0536, 1.049, 0.779,
0.654, 0.148, 1.04, 3.27, 0.73, 0.52, 1.35, 0.086, 0.202};
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the chain ward on w9 + controls + e1-e4 mutants; ladder,
extensions, anchors, class census, generic bound, certificates
and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of this probe): every
anchor band is an r314/r315/r306/r316 RECORD number adopted
as-is; the CHOICE of the two class functionals is motivated by
the r316 RECORD census alone (QMAX = the source-pure sibling of
the named TOP1 discriminator, dev 1.99; the PhiL2-spike anatomy
of the r316 violator list) -- both columns existed in r316, both
are source-pure by the r316 audit, and NO class value, NO
threshold, NO membership and NO violation count of this round
was computed before this spec was frozen; CLS_W = 5, GAP_MIN =
1.25, KMAX = 6, GEN_FAIL_MIN = 5 and TREND_TOY_BAR = 1.15 are
coarse a-priori bars (KMAX sized from the record obstruction
family <= 5 members; GAP_MIN from the recorded factor >= 1.3
gaps of the r315/r316 outlier censuses; the boundary-bias
algebra r^W is derived, disclosed above); the five sealed
verdicts are symmetric -- the gate rule maps every leak
(uncovered violator, family growth, world leak) to the abort
verdict by CONTRACT, not to favor an outcome; the r306 chain
(bound => n_eff) is imported algebra.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+';
exactly one of the four main verdicts fires):
  R317_ANCHORS(r314 shares + FC + mult, identity wards, r306 C_2,
    r315 C0 + FCIX, r316 ladder/split/C_L2/violators/TOP1/rho/
    C_small)
+ SEAL(class functionals + gap rule + hard gate + purity audits
    + toys + chain ward)
+ FAMILIES(census: THR_A/THR_B, members A/B/both/none, thirds,
    boundary bias)
+ GENERIC(C_gen, m_0, violations, reserve, trend, small-m table)
+ CERTS(class A: members + rho_2 + PhiH1 + C_A; class B: members
    + rho_2 + PhiL2 + C_B; growth census)
+ WORLD(admission + twin band + SCRAMBLE rejection)
+ [exactly one of] EXCEPTION_CENSUS_GO(A, B) /
    ONE_FAMILY_SUFFICES(X) / WHAC_A_MOLE / GENERIC_FAILS
+ THEOREM(candidate text printed on GO / ONE_FAMILY)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the class functionals, the gap rule, the
window, the growth rule and the hard gate are sealed BEFORE any
bound evaluation; the thresholds are computed by the sealed rule
from source-pure distributions, printed before any bound table;
the family certificates are FINITE per-member certificates (r270
style) plus exact structural majorants (r316 algebra, warded
live) -- they prove NOTHING beyond the measured members; a GO
fixes a certified exception-family STATEMENT ON THE MEASURED
RUNGS with explicit (C_gen, C_A, C_B, C_small, m_0), it proves NO
universal bound beyond them and NO cofinal law; the class-B spike
property yields no uniform bound from its definition -- disclosed
as the honest asymmetry between the two families; the world
columns are n = 1 per control; a WHAC_A_MOLE seals the abort
honestly and recommends fork (a); r243-r316 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 38/38 (0.4 s), NO amendment; calibration pass 1 =
first full evaluation, 38/38, wall 36.2 s, NO amendment; record
run1/run2 after this insertion, identical up to WALL; PROTOCOL
DISCLOSURE: a drafting error had placed PREFILLED PLACEHOLDER
record tables into this spec BEFORE any run -- they were removed
COMPLETELY before the first smoke run and are disclosed here (the
r316 protocol-error class); the ONLY post-freeze edit is this
record-table insertion, which IS the protocol -- no bar, band,
rule or verdict rule moved):
CAL_VERDICT = R317_ANCHORS(shares -0.4226/+0.5980/+0.8537, FC
0.629/-0.141, mult == 2 on 65/65, identity wards 4.5e-17 /
4.7e-16 / 4.1e-16, r306 C_2 1.069 viol 0/57, r315 C0
2.6261/1.5052/0.9400 + FCIX 0.955/0.915, r316 ladder n = 65, H =
{55, 67}, split 21|5|39 m_0 = 73, C_L2 0.7476, regime-L violator
set == the named 8, TOP1 0.558/0.785, rho anchors kz53/kz67/kz55/
kz83 = 1.0493/1.0536/0.4821/0.7791, C_small 1.0694 @ kz18 -- ALL
bit-near) + SEAL(purity clean: 0 id + 0 literal hits on the five
gate-side builders; toys exact: spike THR^2 == 8, flat EMPTY,
trend EMPTY max ratio 1.0957 <= 1.15, cert + all five gate
branches exact; chain ward worst slack 6.5e-16 on 69 live
worlds, NORM x cube == rho_2 worst 7.9e-16) + FAMILIES(THR_A =
EMPTY -- best F_A gap 1.24 < 1.25 (k = 3); THR_B = 3.7157 via
gap k* = 2 (g 1.78): B = {kz55 F_B 7.23, kz67 4.96} -- EXACTLY
the r315/r316 FCIX pair, recovered blind by the sealed rule;
A n B empty; thirds A (0,0,0) / B (1,1,0); 63 rungs in neither;
boundary-bias census: max non-member F_A 2.47 / F_B 2.79) +
GENERIC(the 63-rung complement: split 21|5|37, C_gen = 0.4579
frozen at complement-cal kz34 (m 84..95), m_0 = 84; VIOLATIONS
2/37: kz53 rho 1.0493 (reserve 0.44) and kz83 rho 0.7791 (0.59)
-- both UNCOVERED by A u B; reserve min/med 0.44/2.06; trend
-0.170 falling; 21 small-m certificates, C_small 1.0694 @ kz18)
+ CERTS(A: EMPTY, 0 certificates; B: kz55 rho 0.4821 PhiL2
4.6423 / kz67 rho 1.0536 PhiL2 2.7312, C_B = 1.0536, structural
rho_2 <= PhiL2 warded on both; growth: A stable (0,0,0), B
stable (1,1,0), EXT2 members 0/0) + WORLD(w9/w13/EPSTEIN
admitted mult 2, rho_2 0.458/0.461/0.368 <= C_tot 1.0694; twin
band PhiL2 factor 1.04 <= 3.0; SCRAMBLE rejected: COLL
attribution dev 3.69 >= 0.25 AND seeded shuffle 317001 breaks
the flux profile edgewise 9.9e-1 with mass matched 0.0 (288/300
atoms); SCR rho_2 1.780 > C_tot census) + WHAC_A_MOLE(2
uncovered violators kz53/kz83 -- a third exception form would be
needed; NO third class added, abort by contract; recommendation:
back to fork (a)) + THEOREM(not printed -- the hard gate fired)
+ MUSTFAIL_LEDGER(e1 AST rho@652 + seal_family_count REFUSES the
3-family tuple + gate maps uncovered violators to WHAC_A_MOLE on
the toy; e2 AST rho@661 + toy thr 1.1000 != gap rule 1.5492; e3
AST cm@671 while the class builders are clean; e4 declared-set
(0, 1) != (3, 4) EXACT + toy diff 1.0 LOUD; m5a t_term@688 /
m5b g_branch@696 FLAGGED).
READING (typed, no upgrade): the sealed letter is WHAC_A_MOLE --
the hard gate fired exactly as the reviewer contract demands
(with the sealed families excepted, the mid-ladder generic
constant is violated by kz53 and kz83, which NO sealed family
covers -- a third form would be needed, and the contract forbids
it) -- and the anatomy behind the letter is the round's real
find: (1) THE DIVERGENCE-MASS SPIKE FAMILY IS REAL: the sealed
gap rule, computed blind from source-pure columns BEFORE any
bound evaluation, recovers B = {kz55, kz67} -- EXACTLY the
r315/r316 FCIX pair -- with a clean 1.78 gap (F_B 7.23/4.96 vs
next 2.79) and finite certificates C_B = 1.0536 <= the r306
shallow maximum; (2) THE CONCENTRATION RANKING SEES THE WHOLE
NEAR-CRITICAL FAMILY BUT AS A CONTINUUM: class A is EMPTY on the
letter (best gap 1.233 misses the sealed 1.25 bar by 0.017), yet
the F_A TOP-3 are EXACTLY kz53 (2.47), kz83 (2.39), kz67 (2.38)
-- the rank-local QMAX ratio ranks the complete deep rho_2-spike
family {53, 83, 67} on top, REFUTING at census level the r316
conjecture that kz53 needs a second coordinate: ONE source-pure
concentration coordinate sees all three mid/deep spikes, but the
distribution below them is a continuum (1.93, 1.90, 1.74, ...),
not a gap-separated family; (3) the SHARPNESS honesty: an A
family at k = 3 would have covered both uncovered violators and
composed a GO -- but the gap missed the sealed bar, and moving
the bar after sight is EXACTLY the e2 mutant; the letter stands;
equally the F_B continuum over-ranks kz12 (2.79, rho_2 0.38 --
a PhiL2 spike that is NOT a rho_2 spike) above kz53 (2.70):
threshold classification on these coordinates cannot cover
kz53/kz83 without swallowing harmless rungs -- the spike TAIL is
a continuum, the exception-family FORM (sealed thresholds) is
the wrong statement shape for it; (4) what HOLDS: all anchors
bit-near (r314/r315/r306 + the complete r316 anatomy incl. the
8-violator set), the B certificates stand (finite, PhiL2-warded,
non-growing, 0 EXT2 members), the generic complement trend
FALLS (-0.170: with the B pair excepted the rest has growing
reserve except at the two named spikes), the world machinery is
intact (twin 1.04, SCRAMBLE rejected via COLL 3.69 + edgewise
break 288/300 with matched mass) and the 21 small-m certificates
stand (C_small 1.0694).  Honest negatives: WHAC_A_MOLE stands --
no composed theorem is printed; class A's emptiness is a
bar-sensitivity fact at distance 0.017, disclosed, not repaired;
nothing here bounds anything beyond the measured rungs.  R318
direction (typed, census-grade): back to fork (a) with the
round's census as the input -- the rank-local QMAX ratio is a
single source-pure coordinate whose top-3 are exactly the three
mid/deep near-critical spikes: the statement form should bound
rho_2 BY the coordinate (continuous: rho_2 <= C(F_A), e.g. a
two-term bound C_1 + C_2 F_A^gamma), not classify by threshold;
alternatively the generic constant must be taken at the r306
first-5 scale (C_2 1.069, 0/57 -- the r316 rehabilitation) where
NO exception family is needed at all on the measured ladder.
Runtime 36.2 s full / 0.4 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: none except this record-table
insertion (and the disclosed pre-run placeholder removal).

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
CLS_W = 5
GAP_MIN = 1.25
KMAX = 6
GEN_FAIL_MIN = 5
TREND_TOY_BAR = 1.15
RES_EPS = 0.01
ATTR_MIN = 0.25
TWIN_FAC = 3.0
SEED_SHUF = 317001
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
N317_REF = 65
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
    4.6095, 2.726, 2.5458, 1.8898, 2.432, 1.7289, 3.69,
    0.7476, 0.5531, 1.4263, 1.1266, 1.0804, 0.9648,
    0.8013, 0.7877, 0.7819, 0.7698, 34.0556, 3.0559,
    57.3, 47.86, 2.76, 7.84, 0.558, 0.785, 0.105, 0.387,
    21.7, 24.9, 31.9, 40.4, 1.0694, 0.4821, 1.0536,
    1.049, 0.779, 0.654, 0.148, 1.04, 3.27, 0.73,
    0.52, 1.35, 0.086, 0.202))

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
    lies in the sealed r314+r315+r316 record-literal set."""
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


# ---------------- module-own builders.  Source-pure: the class
# ---------------- builders consume ONE source-pure column of the
# ---------------- r316 two-regime state (QMAX or PhiL2) plus the
# ---------------- rank order only; the withheld terminal drive
# ---------------- key, the branch label, the cubic target and the
# ---------------- record literals are forbidden (AST identifier
# ---------------- scan + literal scan).
def local_ratio(vals):
    """the sealed rank-local spike ratio: F(i) = vals[i] / median
    of the values in the rank window i-W..i+W excluding i (window
    truncated at the ladder ends; depth-fair by construction --
    the trend toy proves blindness to a pure geometric trend at
    the recorded ladder rate)."""
    v = [float(x) for x in vals]
    n = len(v)
    out = []
    for i in range(n):
        lo = max(0, i - CLS_W)
        hi = min(n, i + CLS_W + 1)
        nb = [v[j] for j in range(lo, hi) if j != i]
        out.append(v[i] / max(float(np.median(nb)), 1e-300))
    return out


def gap_threshold(F):
    """the SEALED gap-threshold rule: sort descending; over prefix
    sizes k = 1..KMAX the multiplicative gap g_k = s_k/s_{k+1};
    k* = argmax; the class is the top-k* values iff g_{k*} >=
    GAP_MIN, else EMPTY; THR = geometric midpoint of the gap."""
    s = sorted((float(x) for x in F), reverse=True)
    best_k = 0
    best_g = 0.0
    for k in range(1, min(KMAX, len(s) - 1) + 1):
        g = s[k - 1] / max(s[k], 1e-300)
        if g > best_g:
            best_g = g
            best_k = k
    if best_g >= GAP_MIN:
        thr = math.sqrt(s[best_k - 1] * s[best_k])
        return thr, best_k, best_g
    return float("inf"), 0, best_g


def family_cert(vals, members):
    """the family certificate bookkeeping: the finite per-member
    certificate constant = max of the certificate column over
    EXACTLY the declared member set; returns (C_fin, declared) --
    the declared set is warded against the sealed membership (the
    e4 circular mutant must be CAUGHT by the set ward)."""
    mem = tuple(members)
    if not mem:
        return 0.0, mem
    return max(float(vals[i]) for i in mem), mem


def seal_family_count(fams):
    """the HARD GATE of the reviewer contract: the adjudication
    accepts EXACTLY two sealed exception families -- any third
    family is REFUSED (the sealed WHAC_A_MOLE fires instead)."""
    return len(fams) == 2


def gate_verdict(n_viol, n_a, n_b, grows, world_ok):
    """the sealed verdict rule (counts only; exactly one fires):
    GENERIC_FAILS on broad generic failure; WHAC_A_MOLE on any
    uncovered violator (a third form would be needed -- abort by
    contract) or any classification leak (family growth / world
    leak); EXCEPTION_CENSUS_GO with both families; otherwise
    ONE_FAMILY_SUFFICES."""
    if n_viol >= GEN_FAIL_MIN:
        return "GENERIC_FAILS"
    if n_viol >= 1:
        return "WHAC_A_MOLE"
    if grows or not world_ok:
        return "WHAC_A_MOLE"
    if n_a >= 1 and n_b >= 1:
        return "EXCEPTION_CENSUS_GO"
    return "ONE_FAMILY_SUFFICES"


def mutant_third_class(mem_a, mem_b, rho, cbar):
    """e1 MUST-FAIL MUTANT: a THIRD class pushed after sight --
    collects the uncovered violators of the evaluated bound
    column (consumes rho) into a post-hoc class; the
    BOUND_FORBIDDEN scope audit must FLAG it and the sealed gate
    must REFUSE it."""
    cov = set(mem_a) | set(mem_b)
    return tuple(i for i, r in enumerate(rho)
                 if r > cbar and i not in cov)


def mutant_thr_posthoc(F, rho, cbar):
    """e2 MUST-FAIL MUTANT: the threshold re-picked AFTER SIGHT of
    the violators (consumes rho): moved down to exactly cover the
    seen violator set -- the scope audit must FLAG it AND on the
    sealed toy it returns != the gap rule's threshold."""
    vi = [F[i] for i, r in enumerate(rho) if r > cbar]
    if not vi:
        return float("inf")
    return min(vi)


def mutant_class_readback(cmrec, nblk):
    """e3 MUST-FAIL MUTANT: a 'class functional' consuming the
    cubic-moment record (the target side) -- the PHI3_FORBIDDEN
    identifier scan must FLAG this."""
    cm = cmrec
    return cm["S3"] * float(nblk) * float(nblk)


def mutant_circular_cert(vals, members, gen_cal):
    """e4 MUST-FAIL MUTANT: a family 'certificate' consuming the
    GENERIC calibration window instead of the member set (the
    circular import of the generic constant) -- the declared-set
    ward must CATCH the mismatch."""
    cal = tuple(gen_cal)
    return max(float(vals[i]) for i in cal), cal


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'class orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'class constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


TOY_SPIKE = (1.0, 1.0, 8.0, 1.0, 1.0, 1.0, 1.0)
TOY_FLAT = (3.0,) * 7
TOY_TREND = tuple(0.97 ** i for i in range(11))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("exception_families_probe -- "
          "PRIME.L2.RENYI3.EXCEPTION_FAMILIES.01 (round 317)")
    print("SPEC_SHA %s   R316_SHA %s   R306_SHA %s (imported)"
          % (SPEC_SHA[:16], TRB.SPEC_SHA[:16], RY3.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + chain ward + e1-e4; "
                        "ladder, extensions, anchors, class "
                        "census, generic bound, certificates and "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE EXCEPTION-FAMILY CENSUS (reviewer fork (b)): two "
          "source-pure class functionals sealed in advance -- "
          "F_A = rank-local QMAX spike ratio (CONCENTRATION), "
          "F_B = rank-local PhiL2 spike ratio (DIVERGENCE-MASS "
          "SPIKE), window W = %d, thresholds by the sealed "
          "largest-gap rule (k <= %d, gap >= %.2f) computed "
          "BEFORE any bound evaluation; generic Renyi-3 theorem "
          "on the complement with the r316 mid-ladder freeze; "
          "family certificates finite per member (r270 style) + "
          "exact structural majorants (rho_2 <= PhiH1 / PhiL2, "
          "r316 algebra); THE HARD GATE sealed: at most TWO "
          "families -- any uncovered violator, family growth or "
          "world leak fires WHAC_A_MOLE by contract; verdicts "
          "EXCEPTION_CENSUS_GO / ONE_FAMILY_SUFFICES / "
          "WHAC_A_MOLE / GENERIC_FAILS sealed BEFORE evaluation"
          % (CLS_W, KMAX, GAP_MIN))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("local_ratio", "gap_threshold"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); class builders clean "
          "vs BOUND_FORBIDDEN (%d hits); m5a gift-bound FLAGGED "
          "(%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r316 scaffold verbatim)
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
    section("S3  LEG 0 -- ANCHOR REGRESSION (r314/r315/r306/r316)")
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
             "FCIX %.3f, QMAX %.4f, PhiL2 %.4f, mult max %d"
             % (ev9s["shares"]["far"], ev9s["shares"]["pair"],
                ev9s["shares"]["full"], ev9s["trs"]["fcix"],
                ev9s["trs"]["qmax"], ev9s["trs"]["phiL2"],
                ev9s["mx_mult"]))
        check("G30-r314-shares-fc", True, "SMOKE: skipped")
        check("G32-r306-bound-live", True, "SMOKE: skipped")
        check("G33-r315-anchors", True, "SMOKE: skipped")
        check("G34-r316-anchors", True, "SMOKE: skipped")
        srt57 = []
        srt317 = []
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
        # the r316 class ladder: mult-cap filter on core+ext+ext2
        srt317_all = sorted(recs + erecs + e2recs,
                            key=lambda rc: (rc["N"], rc["kz"]))
        excl = [rc for rc in srt317_all
                if rc["ev"]["mx_mult"] > MULT_CAP]
        srt317 = [rc for rc in srt317_all
                  if rc["ev"]["mx_mult"] <= MULT_CAP]
        n317 = len(srt317)
        n_m2 = sum(1 for rc in srt317
                   if rc["ev"]["mx_mult"] == 2)
        check("G30-r314-shares-fc",
              all(abs(meds[i] - R314_SHARES[i]) <= R314_SHARE_TOL
                  for i in range(3))
              and abs(fc_med - R314_FC) <= R314_FC_TOL
              and abs(fc_sl - R314_FC_SLOPE) <= R314_FC_SL_TOL
              and n_m2 == n317 and not excl,
              "r314 record reproduced: med shares far/pair/full "
              "%+.4f/%+.4f/%+.4f (rec %+.4f/%+.4f/%+.4f tol "
              "%.3f); FC med %.3f slope %+.3f (rec %.3f/%+.3f); "
              "mult == 2 on %d/%d, mult-cap exclusions %d"
              % (meds[0], meds[1], meds[2], R314_SHARES[0],
                 R314_SHARES[1], R314_SHARES[2], R314_SHARE_TOL,
                 fc_med, fc_sl, R314_FC, R314_FC_SLOPE, n_m2,
                 n317, len(excl)))
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
        # r316 anchors on the class ladder
        h_kz = tuple(sorted(rc["kz"] for rc in srt317
                            if rc["ev"]["trs"]["fcix"] > THETA))
        sm316, ca316, te316 = TRB.split_midladder(n317)
        m_all = [rc["ev"]["m"] for rc in srt317]
        m0_316 = min(m_all[i] for i in ca316 + te316)
        calL = [i for i in ca316
                if srt317[i]["ev"]["trs"]["fcix"] <= THETA]
        CL2 = max(srt317[i]["ev"]["trs"]["phiL2"] for i in calL) \
            if calL else 0.0
        violL2 = tuple(sorted(
            srt317[i]["kz"] for i in te316
            if srt317[i]["ev"]["trs"]["fcix"] <= THETA
            and srt317[i]["ev"]["trs"]["phiL2"] > CL2))
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt317}
        top1_kz = {rc["kz"]: rc["ev"]["top1"] for rc in srt317}
        C_small316 = max(srt317[i]["ev"]["rho2"] for i in sm316)
        j_cs = max(sm316, key=lambda i: srt317[i]["ev"]["rho2"])
        ok316 = (n317 == N317_REF
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
                 and srt317[j_cs]["kz"] == R316_CSMALL_KZ)
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
              % (n317, N317_REF, str(h_kz),
                 str(tuple(sorted(R316_H_SET))), sm316[-1],
                 ca316[0], ca316[-1], te316[0], te316[-1],
                 m0_316, M0_REF, CL2, R316_CL2, R316_CL2_TOL,
                 str(violL2), top1_kz.get(55, -1.0),
                 top1_kz.get(67, -1.0), R316_TOP1[55],
                 R316_TOP1[67], rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO[53],
                 R316_RHO[67], R316_RHO[55], R316_RHO[83],
                 R316_RHO_TOL, C_small316, srt317[j_cs]["kz"],
                 R316_CSMALL, R316_CSMALL_KZ))

    # ---------------- S4: Leg A -- sealing + purity + toys + census
    section("S4  LEG A -- FAMILY DEFINITION (SEALED) + PURITY + "
            "TOYS + CENSUS")
    pure_ids = []
    for fn in ("local_ratio", "gap_threshold"):
        pure_ids += scope_audit(fn, PHI3_FORBIDDEN)
        pure_ids += scope_audit(fn, BOUND_FORBIDDEN)
    pure_lits = []
    for fn in ("local_ratio", "gap_threshold", "family_cert",
               "gate_verdict", "seal_family_count"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_third_class", BOUND_FORBIDDEN)
    e2_hits = scope_audit("mutant_thr_posthoc", BOUND_FORBIDDEN)
    e3_hits = scope_audit("mutant_class_readback", PHI3_FORBIDDEN)
    check("G40-purity-audits",
          (not pure_ids) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1
          and len(e3_hits) >= 1,
          "SOURCE PURITY: local_ratio + gap_threshold clean vs "
          "PHI3_FORBIDDEN + BOUND_FORBIDDEN (%d id hits); the "
          "five gate-side builders clean vs the sealed r314+"
          "r315+r316 record-literal set (%d literal hits); "
          "consumed inputs: ONE source-pure column (QMAX or "
          "PhiL2) + rank order -- no cubic target, no wall sign, "
          "no record number; e1 third-class FLAGGED (%s); e2 "
          "thr-posthoc FLAGGED (%s); e3 class-readback FLAGGED "
          "(%s)"
          % (len(pure_ids), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS",
             e3_hits[0] if e3_hits else "MISS"))
    # toys (exact)
    f_sp = local_ratio(TOY_SPIKE)
    thr_sp, k_sp, g_sp = gap_threshold(f_sp)
    ok_sp = (abs(f_sp[2] - 8.0) <= TOY_BAR
             and all(abs(f_sp[i] - 1.0) <= TOY_BAR
                     for i in range(7) if i != 2)
             and k_sp == 1 and abs(thr_sp * thr_sp - 8.0) <= 1e-9
             and tuple(i for i, v in enumerate(f_sp)
                       if v >= thr_sp) == (2,))
    f_fl = local_ratio(TOY_FLAT)
    thr_fl, k_fl, g_fl = gap_threshold(f_fl)
    ok_fl = (k_fl == 0 and thr_fl == float("inf")
             and abs(g_fl - 1.0) <= TOY_BAR)
    f_tr = local_ratio(TOY_TREND)
    thr_tr, k_tr, _g_tr = gap_threshold(f_tr)
    ok_tr = (k_tr == 0 and max(f_tr) <= TREND_TOY_BAR)
    cert_v, cert_d = family_cert([1.0, 2.0, 3.0, 4.0, 5.0],
                                 (1, 3))
    ok_ct = (cert_v == 4.0 and cert_d == (1, 3))
    gv = (gate_verdict(5, 1, 1, False, True),
          gate_verdict(2, 1, 1, False, True),
          gate_verdict(0, 1, 1, True, True),
          gate_verdict(0, 1, 1, False, True),
          gate_verdict(0, 1, 0, False, True))
    ok_gv = gv == ("GENERIC_FAILS", "WHAC_A_MOLE", "WHAC_A_MOLE",
                   "EXCEPTION_CENSUS_GO", "ONE_FAMILY_SUFFICES")
    check("G41-toy-exactness", ok_sp and ok_fl and ok_tr
          and ok_ct and ok_gv,
          "spike toy (1,1,8,1,1,1,1): F = (1,1,8,1,1,1,1), k* = "
          "%d, THR^2 = %.10f == 8, members (2,) EXACT; flat toy: "
          "EMPTY EXACT (gap %.2f < %.2f); TREND toy 0.97^i "
          "(ladder rate): EMPTY, max ratio %.4f <= %.2f -- the "
          "rank-local construction is trend-blind; cert toy "
          "(max 4.0, declared (1,3)) EXACT; gate toys: all five "
          "verdict branches EXACT %s"
          % (k_sp, thr_sp * thr_sp, g_fl, GAP_MIN, max(f_tr),
             TREND_TOY_BAR, str(gv)))
    # live majorant chain ward (the r316 algebra re-warded)
    chain_w = 0.0
    xw_cube = 0.0
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
    check("G42-majorant-chain-ward",
          chain_w <= CHAIN_BAR and xw_cube <= XW_BAR,
          "the r316 algebra live on %d live worlds: rho_2 <= "
          "PhiL1 <= PhiL2 <= PhiH2 and rho_2 <= PhiH1 (worst rel "
          "slack %.1e, bar %.0e); NORM x cube == rho_2 (worst "
          "%.1e, bar %.0e) -- the class-A structural bound (rho_2 "
          "<= PhiH1, concentration) and the class-B structural "
          "bound (rho_2 <= PhiL2) transfer every certificate to "
          "sum q^3 by algebra"
          % (len(live), chain_w, CHAIN_BAR, xw_cube, XW_BAR))
    if smoke:
        check("G43-threshold-seal", True, "SMOKE: skipped")
        check("G44-membership-census", True, "SMOKE: skipped")
    else:
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt317]
        phiL2_col = [rc["ev"]["trs"]["phiL2"] for rc in srt317]
        FA = local_ratio(qmax_col)
        FB = local_ratio(phiL2_col)
        thrA, kA, gA = gap_threshold(FA)
        thrB, kB, gB = gap_threshold(FB)
        memA = tuple(i for i, v in enumerate(FA) if v >= thrA)
        memB = tuple(i for i, v in enumerate(FB) if v >= thrB)
        famAB = set(memA) | set(memB)
        info("sealed class table (source-pure columns, printed "
             "BEFORE any bound table of this round): rank kz N m "
             "QMAX F_A PhiL2 F_B [class]")
        for i, rc in enumerate(srt317):
            tag = ""
            if i in memA and i in memB:
                tag = " A+B"
            elif i in memA:
                tag = " A"
            elif i in memB:
                tag = " B"
            info("%2d kz%-3d N %4d m %3d qmax %.4f FA %5.2f L2 "
                 "%8.4f FB %5.2f%s"
                 % (i, rc["kz"], rc["N"], rc["ev"]["m"],
                    qmax_col[i], FA[i], phiL2_col[i], FB[i], tag))
        check("G43-threshold-seal",
              seal_family_count(("A", "B")),
              "THRESHOLDS FROZEN by the sealed gap rule: THR_A = "
              "%s (k* = %d, gap %.2f %s %.2f); THR_B = %s (k* = "
              "%d, gap %.2f %s %.2f); EXACTLY TWO families "
              "sealed (hard gate armed)"
              % (("%.4f" % thrA) if kA else "EMPTY", kA, gA,
                 ">=" if gA >= GAP_MIN else "<", GAP_MIN,
                 ("%.4f" % thrB) if kB else "EMPTY", kB, gB,
                 ">=" if gB >= GAP_MIN else "<", GAP_MIN))
        both = tuple(sorted(set(memA) & set(memB)))
        thirds = lambda mem: tuple(  # noqa: E731
            sum(1 for i in mem if 3 * i // n317 == t)
            for t in range(3))
        thA = thirds(memA)
        thB = thirds(memB)
        nonmemA = max((FA[i] for i in range(n317)
                       if i not in memA), default=0.0)
        nonmemB = max((FB[i] for i in range(n317)
                       if i not in memB), default=0.0)
        check("G44-membership-census", True,
              "MEMBERSHIP CENSUS: A (CONCENTRATION) = %s; B "
              "(SPIKE) = %s; A n B = %s; %d rungs in neither; "
              "thirds A %s / B %s; boundary-bias census: max "
              "non-member F_A %.2f / F_B %.2f"
              % (str([srt317[i]["kz"] for i in memA]),
                 str([srt317[i]["kz"] for i in memB]),
                 str([srt317[i]["kz"] for i in both]),
                 n317 - len(famAB), str(thA), str(thB),
                 nonmemA, nonmemB))

    # ---------------- S5: Leg B -- the generic theorem
    section("S5  LEG B -- THE GENERIC THEOREM (complement)")
    if smoke:
        check("G50-complement-split", True, "SMOKE: skipped")
        check("G51-smallm-certificates", True, "SMOKE: skipped")
        check("G52-generic-certification", True, "SMOKE: skipped")
        check("G53-generic-trend", True, "SMOKE: skipped")
    else:
        comp = [i for i in range(n317) if i not in famAB]
        n_comp = len(comp)
        sm_c, ca_c, te_c = TRB.split_midladder(n_comp)
        ovl = len(set(sm_c) & set(ca_c)) \
            + len(set(sm_c) & set(te_c)) \
            + len(set(ca_c) & set(te_c))
        cover = (tuple(sorted(sm_c + ca_c + te_c))
                 == tuple(range(n_comp)))
        rho_all = [rc["ev"]["rho2"] for rc in srt317]
        m0 = min(srt317[comp[j]]["ev"]["m"]
                 for j in ca_c + te_c)
        check("G50-complement-split",
              ovl == 0 and cover and len(ca_c) == N_CAL,
              "complement ladder = %d rungs (A u B excluded, "
              "(N, kz) order kept); r316 mid-ladder split rule "
              "verbatim: small = %d rungs, cal = ranks %d..%d "
              "(kz %s), test = %d rungs; overlaps 0 EXACT, cover "
              "EXACT; m_0 = %d"
              % (n_comp, len(sm_c), ca_c[0], ca_c[-1],
                 str([srt317[comp[j]]["kz"] for j in ca_c]),
                 len(te_c), m0))
        C_small = max(rho_all[comp[j]] for j in sm_c) \
            if sm_c else 0.0
        j_sm = max(sm_c, key=lambda j: rho_all[comp[j]]) \
            if sm_c else -1
        info("small-m certificates (complement, direct "
             "evaluation): rank kz m rho_2")
        for j in sm_c:
            i = comp[j]
            info("%2d kz%-3d m %3d rho2 %.4f%s"
                 % (i, srt317[i]["kz"], srt317[i]["ev"]["m"],
                    rho_all[i],
                    "  <-- C_small" if j == j_sm else ""))
        check("G51-smallm-certificates",
              (not sm_c) or C_small > 0.0,
              "%d complement small-m rungs certified "
              "individually; C_small = %.4f at kz%d"
              % (len(sm_c), C_small,
                 srt317[comp[j_sm]]["kz"] if j_sm >= 0 else -1))
        C_gen = max(rho_all[comp[j]] for j in ca_c)
        j_cg = max(ca_c, key=lambda j: rho_all[comp[j]])
        viol_gen = [comp[j] for j in te_c
                    if rho_all[comp[j]] > C_gen]
        rs = [C_gen / max(rho_all[comp[j]], 1e-300)
              for j in te_c]
        info("generic record table (complement test): rank kz N "
             "m rho_2 reserve")
        for j in te_c:
            i = comp[j]
            info("%2d kz%-3d N %4d m %3d rho2 %.4f rsv %.2f%s"
                 % (i, srt317[i]["kz"], srt317[i]["N"],
                    srt317[i]["ev"]["m"], rho_all[i],
                    C_gen / max(rho_all[i], 1e-300),
                    "  VIOL" if i in viol_gen else ""))
        check("G52-generic-certification", True,
              "GENERIC (census; adjudicated in S7): C_gen = "
              "%.4f frozen at complement-cal kz%d (mid-ladder); "
              "VIOLATIONS %d/%d on the complement test rungs%s; "
              "reserve min/med %.2f/%.2f"
              % (C_gen, srt317[comp[j_cg]]["kz"],
                 len(viol_gen), len(te_c),
                 (": " + ", ".join(
                     "kz%d rho %.4f" % (srt317[i]["kz"],
                                        rho_all[i])
                     for i in viol_gen)) if viol_gen else "",
                 min(rs), float(np.median(rs))))
        NsT = [srt317[comp[j]]["N"] for j in te_c]
        sl_g = L2D.halves_slope(
            NsT, [max(rho_all[comp[j]], 1e-300) for j in te_c])
        check("G53-generic-trend", True,
              "generic trend census on the %d complement test "
              "rungs (halves slope of rho_2): %+.3f (falling = "
              "growing reserve; census, no gate bar)"
              % (len(te_c), sl_g))

    # ---------------- S6: Leg C -- the family certificates
    section("S6  LEG C -- FAMILY CERTIFICATES + GROWTH CENSUS")
    if smoke:
        check("G60-classA-certificates", True, "SMOKE: skipped")
        check("G61-classB-certificates", True, "SMOKE: skipped")
        check("G62-growth-census", True, "SMOKE: skipped")
    else:
        C_A, decl_A = family_cert(rho_all, memA)
        okA_chain = all(rho_all[i]
                        <= srt317[i]["ev"]["trs"]["phiH1"]
                        * (1.0 + CHAIN_BAR) for i in memA)
        info("class-A certificates (CONCENTRATION): rank kz m "
             "rho_2 PhiH1 qmax")
        for i in memA:
            ev = srt317[i]["ev"]
            info("%2d kz%-3d m %3d rho2 %.4f PhiH1 %.4f qmax "
                 "%.4f" % (i, srt317[i]["kz"], ev["m"],
                           rho_all[i], ev["trs"]["phiH1"],
                           ev["trs"]["qmax"]))
        check("G60-classA-certificates",
              decl_A == memA and okA_chain,
              "class A: %d finite certificates, C_A = %.4f; "
              "declared set == sealed membership EXACT; "
              "structural bound rho_2 <= PhiH1 (the class "
              "DEFINITION's concentration majorant) holds on "
              "every member; qmax <= 1 - delta with delta = "
              "%.3f"
              % (len(memA), C_A,
                 1.0 - max((srt317[i]["ev"]["trs"]["qmax"]
                            for i in memA), default=0.0)))
        C_B, decl_B = family_cert(rho_all, memB)
        okB_chain = all(rho_all[i]
                        <= srt317[i]["ev"]["trs"]["phiL2"]
                        * (1.0 + CHAIN_BAR) for i in memB)
        info("class-B certificates (SPIKE): rank kz m rho_2 "
             "PhiL2 F_B")
        for i in memB:
            ev = srt317[i]["ev"]
            info("%2d kz%-3d m %3d rho2 %.4f PhiL2 %.4f FB %.2f"
                 % (i, srt317[i]["kz"], ev["m"], rho_all[i],
                    ev["trs"]["phiL2"], FB[i]))
        check("G61-classB-certificates",
              decl_B == memB and okB_chain,
              "class B: %d finite certificates, C_B = %.4f; "
              "declared set == sealed membership EXACT; "
              "structural bound rho_2 <= PhiL2 holds on every "
              "member; DISCLOSED honest asymmetry: the spike "
              "property yields no uniform bound from its "
              "definition -- these are r270-style finite "
              "certificates" % (len(memB), C_B))
        growsA = thA[0] < thA[1] < thA[2]
        growsB = thB[0] < thB[1] < thB[2]
        e2A = sum(1 for i in memA if srt317[i] in e2recs)
        e2B = sum(1 for i in memB if srt317[i] in e2recs)
        check("G62-growth-census", True,
              "DEPTH-GROWTH census (sealed rule: strictly "
              "increasing thirds = GROWS): A thirds %s -> %s; B "
              "thirds %s -> %s; EXT2-stratum members A %d / B %d"
              % (str(thA), "GROWS" if growsA else "stable",
                 str(thB), "GROWS" if growsB else "stable",
                 e2A, e2B))

    # ---------------- S7: Leg D -- world check + hard gate
    section("S7  LEG D -- WORLD CHECK + THE HARD GATE")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    m9 = ev9m["m"]
    # SCRAMBLE class rejection machinery (r316 verbatim)
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
        check("G70-world-admission", True, "SMOKE: skipped")
        check("G71-scramble-rejection", shuf_ok and attr_ok,
              "SMOKE (w9-based): attribution %s dev %.2f; "
              "shuffle %d mism, edge break %.1e, mass %.1e"
              % (cause.upper(), devsS[cause], mism_s, edev,
                 mass_dev))
        check("G72-hard-gate-adjudication", True,
              "SMOKE: skipped")
        check("G73-theorem-candidate", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        C_tot = max(C_gen, C_A, C_B, C_small)
        wnote = []
        adm_ok = True
        for nm, ev in (("w9", mrecs[0]["ev"]),
                       ("w13(twin)", mrecs[1]["ev"]),
                       ("EPSTEIN", crecs["EPST"]["ev"])):
            adm = (ev["mx_mult"] <= MULT_CAP
                   and ev["rho2"] <= C_tot)
            adm_ok = adm_ok and adm
            wnote.append("%s mult %d rho2 %.3f %s C_tot (qmax "
                         "%.4f PhiL2 %.4f census)"
                         % (nm, ev["mx_mult"], ev["rho2"],
                            "<=" if ev["rho2"] <= C_tot else ">",
                            ev["trs"]["qmax"],
                            ev["trs"]["phiL2"]))
        tw_fac = max(mrecs[1]["ev"]["trs"]["phiL2"]
                     / max(mrecs[0]["ev"]["trs"]["phiL2"],
                           1e-300),
                     mrecs[0]["ev"]["trs"]["phiL2"]
                     / max(mrecs[1]["ev"]["trs"]["phiL2"],
                           1e-300))
        twin_ok = tw_fac <= TWIN_FAC
        world_ok = adm_ok and twin_ok and attr_ok and shuf_ok
        check("G70-world-admission", True,
              "WORLD census (adjudicated in G72): %s; twin band "
              "PhiL2 factor %.2f %s %.1f; SCR rho2 %.3f %s C_tot "
              "%.4f (consequence census, disclosed)"
              % ("; ".join(wnote), tw_fac,
                 "<=" if twin_ok else ">", TWIN_FAC, evS["rho2"],
                 "<=" if evS["rho2"] <= C_tot else ">", C_tot))
        check("G71-scramble-rejection", attr_ok and shuf_ok,
              "SCRAMBLE rejected by the CLASS machinery: "
              "component attribution names %s (dev %.2f >= "
              "%.2f, devs %s) AND the seeded shuffle (%d) "
              "breaks the flux profile edgewise %.1e >= %.0e "
              "with mass matched %.1e (%d/%d atoms displaced)"
              % (cause.upper(), devsS[cause], ATTR_MIN,
                 str({k: round(devsS[k], 2) for k in devsS}),
                 SEED_SHUF, edev, MUT_MIN, mass_dev, mism_s,
                 len(ev9m["pos_all"])))
        grows = growsA or growsB
        vkey = gate_verdict(len(viol_gen), len(memA), len(memB),
                            grows, world_ok)
        if vkey == "GENERIC_FAILS":
            verdict_main = ("GENERIC_FAILS(%d/%d complement "
                            "violations >= %d -- the generic "
                            "law itself fails, classification "
                            "moot)" % (len(viol_gen), len(te_c),
                                       GEN_FAIL_MIN))
        elif vkey == "WHAC_A_MOLE":
            reasons = []
            if viol_gen:
                reasons.append("%d uncovered violators %s -- a "
                               "third exception form would be "
                               "needed, NO third class added "
                               "(abort by contract)"
                               % (len(viol_gen),
                                  str([srt317[i]["kz"]
                                       for i in viol_gen])))
            if grows:
                reasons.append("family growth (A %s B %s)"
                               % (str(thA), str(thB)))
            if not world_ok:
                reasons.append("world leak (adm %s twin %s attr "
                               "%s shuf %s)"
                               % (adm_ok, twin_ok, attr_ok,
                                  shuf_ok))
            verdict_main = ("WHAC_A_MOLE(%s; recommendation: "
                            "back to fork (a))"
                            % "; ".join(reasons))
        elif vkey == "EXCEPTION_CENSUS_GO":
            verdict_main = ("EXCEPTION_CENSUS_GO(A = %s, B = "
                            "%s; C_gen %.4f, C_A %.4f, C_B "
                            "%.4f, C_small %.4f, C_tot %.4f, "
                            "m_0 %d)"
                            % (str([srt317[i]["kz"]
                                    for i in memA]),
                               str([srt317[i]["kz"]
                                    for i in memB]),
                               C_gen, C_A, C_B, C_small, C_tot,
                               m0))
        else:
            fam = "A" if memA else ("B" if memB else "NONE")
            verdict_main = ("ONE_FAMILY_SUFFICES(%s; C_gen "
                            "%.4f, C_tot %.4f, m_0 %d)"
                            % (fam, C_gen, C_tot, m0))
        check("G72-hard-gate-adjudication", True,
              "exactly one sealed verdict fired: %s"
              % verdict_main)
        if vkey in ("EXCEPTION_CENSUS_GO", "ONE_FAMILY_SUFFICES"):
            info("CANDIDATE THEOREM (Renyi-3 with exception "
                 "families; measured on the %d-rung class "
                 "ladder; status %s):" % (n317, vkey))
            info("  Every class rung w (edge-masked, fold "
                 "multiplicity <= %d, POSITIVE_PREFIX) falls "
                 "into at least one certified case:" % MULT_CAP)
            if memA:
                info("   (i)   CLASS A (source-pure: F_A >= "
                     "%.4f): rho_2 <= C_A = %.4f (%d finite "
                     "certificates; structural: rho_2 <= PhiH1 "
                     "by exact concentration algebra);"
                     % (thrA, C_A, len(memA)))
            if memB:
                info("   (ii)  CLASS B (source-pure: F_B >= "
                     "%.4f): rho_2 <= C_B = %.4f (%d finite "
                     "certificates; structural: rho_2 <= "
                     "PhiL2);" % (thrB, C_B, len(memB)))
            info("   (iii) m < %d: individually certified "
                 "(C_small = %.4f, %d rungs);"
                 % (m0, C_small, len(sm_c)))
            info("   (iv)  GENERIC (m >= %d, neither class): "
                 "rho_2 <= C_gen = %.4f (mid-ladder frozen, "
                 "0/%d test violations, reserve trend %+.3f);"
                 % (m0, C_gen, len(te_c), sl_g))
            info("  hence sum_j q_j^3 <= %.4f (log m)^2/m^2 on "
                 "EVERY measured rung (C_tot = max) and n_eff = "
                 "N_2 >= N_3 >= m/(%.3f log m) (r306 exact "
                 "chain).  COVERAGE: A u B covers ALL violators "
                 "of C_gen on the ladder (0 uncovered); depth "
                 "census: A thirds %s / B thirds %s (not "
                 "growing)."
                 % (C_tot, math.sqrt(C_tot), str(thA), str(thB)))
            check("G73-theorem-candidate", True,
                  "composed theorem candidate printed with "
                  "explicit (C_gen %.4f, C_A %.4f, C_B %.4f, "
                  "C_small %.4f, C_tot %.4f, m_0 %d)"
                  % (C_gen, C_A, C_B, C_small, C_tot, m0))
        else:
            check("G73-theorem-candidate", True,
                  "no composed theorem candidate printed (the "
                  "hard gate fired -- see G72); the family "
                  "census and the finite certificates stand as "
                  "the round's record data")

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    toyA = (0,)
    toyB = (1,)
    toy_rho = (9.0, 9.0, 9.0, 0.1)
    third = mutant_third_class(toyA, toyB, toy_rho, 1.0)
    gate_ref = seal_family_count((toyA, toyB, third))
    gate_ok = seal_family_count((toyA, toyB))
    gv_mut = gate_verdict(len(third), 1, 1, False, True)
    check("G80-e1-third-class",
          len(e1_hits) >= 1 and third == (2,)
          and (not gate_ref) and gate_ok
          and gv_mut == "WHAC_A_MOLE",
          "e1 GATE-CAUGHT three ways: the post-hoc third class "
          "consumes the evaluated bound column -- AST-FLAGGED "
          "(%s); seal_family_count REFUSES the 3-family tuple "
          "(False) while the sealed 2-family passes (True); the "
          "sealed gate maps the uncovered violators to %s, "
          "never to a three-family GO"
          % (e1_hits[0] if e1_hits else "MISS", gv_mut))
    toy_F = (1.0, 1.1, 1.2, 2.0)
    toy_rho2 = (0.1, 0.9, 0.1, 0.1)
    thr_mut = mutant_thr_posthoc(toy_F, toy_rho2, 0.5)
    thr_seal, k_seal, _g = gap_threshold(toy_F)
    check("G81-e2-threshold-posthoc",
          len(e2_hits) >= 1
          and abs(thr_mut - thr_seal) >= MUT_MIN,
          "e2 CAUGHT twice: the after-sight threshold re-pick "
          "consumes rho -- AST-FLAGGED (%s) -- and on the "
          "sealed toy it returns %.4f != the gap rule's %.4f "
          "(k* = %d); the real thresholds are frozen by the "
          "sealed rule before any bound value"
          % (e2_hits[0] if e2_hits else "MISS", thr_mut,
             thr_seal, k_seal))
    check("G82-e3-class-readback",
          len(e3_hits) >= 1 and (not pure_ids),
          "e3 AST-CAUGHT: the class functional consuming the "
          "cubic-moment record (cm/S3) is FLAGGED (%s) while "
          "local_ratio + gap_threshold are clean (%d hits) -- "
          "the source-purity of the family definition is "
          "machine-audited"
          % (e3_hits[0] if e3_hits else "MISS", len(pure_ids)))
    toy_vals = (0.1, 0.2, 0.3, 0.9, 1.2)
    toy_mem = (3, 4)
    toy_cal = (0, 1)
    c_real, d_real = family_cert(toy_vals, toy_mem)
    c_mut, d_mut = mutant_circular_cert(toy_vals, toy_mem,
                                        toy_cal)
    check("G83-e4-circular-cert",
          d_real == toy_mem and d_mut != toy_mem
          and abs(c_real - c_mut) >= MUT_MIN
          and c_real == 1.2 and c_mut == 0.2,
          "e4 CAUGHT: the circular certificate declares the "
          "generic calibration window %s != the member set %s "
          "(set ward EXACT) and its 'constant' %.1f sits LOUDLY "
          "below the member maximum %.1f (diff %.1f >= %.0e) "
          "-- certifying nothing; the real family_cert declares "
          "the members exactly"
          % (str(d_mut), str(toy_mem), c_mut, c_real,
             c_real - c_mut, MUT_MIN))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the two sealed source-pure class functionals "
          "with the gap-threshold rule (frozen before any bound "
          "evaluation), the membership census, the generic "
          "mid-ladder theorem on the complement, the finite "
          "family certificates with structural majorants, the "
          "depth-growth census and the HARD two-family gate -- "
          "NO new certificate promoted, NO universal bound "
          "claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R317_ANCHORS(shares %+.4f/%+.4f/%+.4f, FC "
                 "%.3f/%+.3f, mult 2 on %d/%d, identity %.1e, "
                 "r306 C2 %.3f viol %d/57, r315 C0 "
                 "%.4f/%.4f/%.4f, r316 n %d H %s split %d|%d|%d "
                 "C_L2 %.4f viol8 %s C_small %.4f)"
                 % (meds[0], meds[1], meds[2], fc_med, fc_sl,
                    n_m2, n317, rec3_w, C2, viol2, C0["a"],
                    C0["b"], C0["c"], n317, str(h_kz),
                    len(sm316), len(ca316), len(te316), CL2,
                    str(violL2), C_small316)]
        parts.append("SEAL(W %d, gap rule k<=%d g>=%.2f, purity "
                     "clean, toys exact, chain %.1e)"
                     % (CLS_W, KMAX, GAP_MIN, chain_w))
        parts.append("FAMILIES(THR_A %s k %d g %.2f -> A %s; "
                     "THR_B %s k %d g %.2f -> B %s; both %s; "
                     "thirds A %s B %s)"
                     % (("%.4f" % thrA) if kA else "EMPTY", kA,
                        gA, str([srt317[i]["kz"] for i in memA]),
                        ("%.4f" % thrB) if kB else "EMPTY", kB,
                        gB, str([srt317[i]["kz"] for i in memB]),
                        str([srt317[i]["kz"] for i in both]),
                        str(thA), str(thB)))
        parts.append("GENERIC(C_gen %.4f, m_0 %d, viol %d/%d %s, "
                     "reserve %.2f/%.2f, trend %+.3f, small %d "
                     "C_small %.4f)"
                     % (C_gen, m0, len(viol_gen), len(te_c),
                        str([srt317[i]["kz"] for i in viol_gen]),
                        min(rs), float(np.median(rs)), sl_g,
                        len(sm_c), C_small))
        parts.append("CERTS(A: %d members C_A %.4f PhiH1-warded; "
                     "B: %d members C_B %.4f PhiL2-warded; "
                     "growth A %s B %s, EXT2 %d/%d)"
                     % (len(memA), C_A, len(memB), C_B,
                        "GROWS" if growsA else "stable",
                        "GROWS" if growsB else "stable",
                        e2A, e2B))
        parts.append("WORLD(adm %s, twin %.2f, SCR %s dev %.2f "
                     "+ shuffle %d/%d)"
                     % (adm_ok, tw_fac, cause.upper(),
                        devsS[cause], mism_s,
                        len(ev9m["pos_all"])))
        parts.append(verdict_main)
        parts.append("THEOREM(%s)"
                     % ("printed" if vkey in
                        ("EXCEPTION_CENSUS_GO",
                         "ONE_FAMILY_SUFFICES")
                        else "not printed"))
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the gap-rule toys, the "
          "gate logic, the majorant chains and the purity "
          "audits (exact / AST-decided); MEASURED: every "
          "threshold, membership, constant, violation count, "
          "reserve, trend and census (the finite class ladder + "
          "2 mains + 2 live controls); OPEN: any bound beyond "
          "the measured rungs, the cofinal law, kz15 beyond "
          "r270; NO RH claim"
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
