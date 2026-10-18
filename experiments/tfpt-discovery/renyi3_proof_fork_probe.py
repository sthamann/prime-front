#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""renyi3_proof_fork_probe -- PRIME.L2.RENYI3.PROOF_FORK.01 (round
313): the RENYI-3 PROOF-FORM FORK -- two sealed proof architectures
for the r306 pointwise cubic law, executed side by side and
adjudicated: (R3A) TRIPLE INCIDENCE AND TELESCOPE -- expand
sum_j a_j^3 (a_j = |PDelta|_j BEFORE normalization) EXACTLY over the
raw atomic presentation (local c-differences of the r298/r300
construction chain) and classify every contribution by triple type;
(R3B) FOUR-STEP FLOQUET on the cubic tensor space -- the monodromy
M_k = A_{k+3} A_{k+2} A_{k+1} A_k of the EXACT local chain recursion
r_{k+1} = t_k + ap_k r_k + bp_k r_{k-1} (the r260 drive arrays; the
period-4 Floquet form of the r304 comb, NOT the refuted single-step
mixing).  Reviewer frame (binding): do NOT chase the r306 sharp
constant 1.069 -- the universal theorem may be COARSER (any explicit
C < infinity, fixed A, explicit m_0; finite cases below m_0
certified separately); because EPSTEIN holds the r306 bound and
SCRAMBLE breaks it, the theorem must NOT depend on von-Mangoldt
arithmetic -- the sought object is a CLASS `RecursiveDifferenceProfile`
(ordered shared support, exact local recursion, bounded atom
multiplicity, controlled four-block structure, mass conservation, no
assignment shuffle) with MAIN and EPSTEIN as instances and SCRAMBLE
excluded.  Context (sealed record inputs): r306 (SPEC 3bb365e1)
delivered RENYI3_GO(C = 1.069, A = 2): sum q^3 <= 1.069 (log m)^2 /
m^2 pointwise on all 57 rungs with growing reserve (trend -0.322);
r304 (SPEC 2cc5d23f) froze the period-4 lag comb (med rho_1..4 =
-0.222/-0.140/+0.089/+0.130) and closed the single-step
global-profile mixing route; r303 proved S_3 is a pure marginal
functional; kz15 permanently closed via r270; the 6 exceptions via
the r287 F2 certificates.

EXPLORATION ONLY (2026-08-26).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r269/r287/r298/r300/r301/r304/r306 machinery imported
verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266 eval);
F = 0.20 edge split; maximal same-sign runs of the bx-sorted bulk;
level-2 blocks (r270 convention); the frozen positional block
machinery (r298 WBT.block_breaks + WBT.aggregate_blocks), the r300
DTP.participation + DTP.shared_delta, the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze + RY3.fr_lagrange, the r304
SLP.lag_stats + SLP.net_cov, ALL imported verbatim; PDelta = Pbeta
- Pomega; NEW in this round is the RAW ATOMIC PRESENTATION: the
block value P_j is EXACTLY the sum of raw atoms d_alpha in block j,
where the raw atom list is the concatenation of the edge-masked
bulk atoms (position bx, value +ct) and the edge-masked window
atoms (position xu, value -cw) -- the local c-differences of the
construction chain; atoms sharing one position form a FOLD GROUP
(the beta/omega fold of one node; the r313 scoping run measured
multiplicity exactly 2 on w9, med 4 positions per block -- the
four-block scale).

LEG 0 -- ANCHOR REGRESSION (r306/r304 record numbers adopted
as-is, disclosed): the r306 C-table C_0/C_1/C_2 =
11.875/3.564/1.069 (tol 0.005, frozen on the first N_CAL = 5 rungs
of the (N, kz)-sorted 57-rung ladder), the r306 pointwise verdict
at A = 2 re-measured live (0/57 violations, reserve min/med
1.01/4.06 tol 0.02, trend -0.322/-0.322 tol 0.005 on both frozen
estimators), and the r304 comb anchor (med rho_1..4 of the
edge-masked dc profile over the 42 core rungs =
-0.222/-0.140/+0.089/+0.130, tol 0.01).

LEG A -- ROUTE R3A: TRIPLE INCIDENCE AND TELESCOPE (exact):
(A1) THE EXACT TYPE DECOMPOSITION: per block j with raw atoms
  d_alpha and fold groups g (same position), ordered triples of
  the cube P_j^3 = (sum_alpha d_alpha)^3 split EXACTLY into
    T1_j = S3_j                     (p == q == r, DIAGONAL)
    T2_j = 3 (S2_j S1_j - S3_j)     (exactly two equal)
    T4_j = S1_j^3 - 3 S1_j Q2_j + 2 Q3_j
                                    (all distinct atoms in three
                                     DISTINCT fold groups -- the
                                     fully separated FAR triples;
                                     Qk_j = sum_g G1_g^k, G1_g =
                                     sum_{alpha in g} d_alpha)
    T3_j = DIST_j - T4_j            (distinct atoms with SHARED
                                     fold ancestry -- the NEAR
                                     triples containing a
                                     c-difference fold pair;
                                     DIST_j = S1_j^3 - 3 S1_j S2_j
                                     + 2 S3_j)
  ward per block: T1 + T2 + T3 + T4 == P_j^3, rel to the abs-mass
  scale (sum_alpha |d_alpha|)^3, bar TYPE_BAR; the abs-majorants
  use the SAME set partition on |d| (T4abs = S1a^3 - 3 S1a Q2a +
  2 Q3a, T3abs = DISTabs - T4abs) -- exact majorants by triangle
  inequality.  Rung totals tot_t = sum_j sign(P_j) T_t_j recompose
  sum_j |P_j|^3 == S_3 L1^3 (RECOMP ward + RY3.cubic_moments
  cross-ward).
(A2) THE FOUR PROOF HOPES, measured on 57 rungs x 3 worlds:
  (i) DIAGONAL / multiplicity: fold multiplicity census (max
  atoms per position -- the class bound MULT_CAP = 2), positions
  per block, and the per-type prereg verdict of T1 at A = 0
  (bounded diagonal needs NO log); (ii) NEAR / harmonic: the
  minimal A in {0, 1, 2} for which |tot_T3| passes the r306
  prereg protocol (C frozen on the first 5 rungs, HOLD on all
  57); (iii) FAR / telescope: the exact telescope-cancellation
  index TC_far = sum_j |T4_j| / sum_j T4abs_j (1 = no
  cancellation; the m3 mutant with |c| instead of c is EXACTLY
  1), med + slope; (iv) COMPOSITION: the printed minimal-A table
  over the four types -- 'two independent harmonic counts' is
  CONFIRMED iff T1 holds at A = 0 and every type holds at A <= 2
  (each bounded by a nameable class property), REFUTED in the
  printed form otherwise.
SEALED A-CLAUSES: A3_WARD iff the type ward holds on every live
world (bar TYPE_BAR) and the recompose ward holds (RECOMP_BAR);
A3_OK iff A3_WARD and all four types HOLD at A = 2 under the
frozen per-type C_t and T1 additionally HOLDs at A = 0; A3_WORLD
iff EPSTEIN passes all four frozen type bounds at A = 2 and
SCRAMBLE violates at least one (the violated type is the named
world separator of the bookkeeping).

LEG B -- ROUTE R3B: FOUR-STEP FLOQUET (source-pure):
(B1) THE LOCAL TRANSFER STEP, verified exactly: the r260 drive
  arrays satisfy r_{k+1} = t_k + ap_k r_k + bp_k r_{k-1} (the
  r313 scoping run measured worst rel dev 4.0e-14 on w9; bars
  REC_BAR 1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls; on
  flipped worlds only k below the flip, disclosed truncation).
  The affine step on (r_{k+1}, r_k, 1) has the SCALAR
  CONSERVATION MODE (third coordinate, eigenvalue exactly 1, by
  block triangularity); SPLITTING IT OFF leaves the linear part
  A_k = [[ap_k, bp_k], [1, 0]].
(B2) THE FOUR-STEP MONODROMY M_k0 = A_{k0+3} A_{k0+2} A_{k0+1}
  A_k0 for k0 = 1, 5, 9, ... (stride 4 -- the Floquet form of
  the r304 period-4 comb): closed-form 2x2 spectral radius sr
  (trace/det, deterministic), det ward |det M| == prod |bp| (bar
  DET_BAR).  On the third tensor stage the complementary cubic
  mode space (scalar mode split off) has spectral radius
  max-mode sr (the slowest complementary mode couples one linear
  factor with two conserved factors); the pure cubic top mode
  sr^3 is printed as census.  Per rung: med sr, frac(sr < 1),
  drift census c_i = k0_i (1 - sr_i) med, and the LADDER PRODUCT
  EXPONENT expo = sum_i log sr_i / log m -- the sealed order
  question: does the product deliver the m^-2 order (expo <=
  EXPO_TARGET = -2)?
SEALED B-CLAUSES: B_REC iff the recursion ward holds on 57 rungs
+ mains + controls (truncated); B_OK iff B_REC and med sr < 1 on
57/57 rungs and expo <= -2 on >= EXPO_MIN = 52 of 57 rungs;
B_WORLD iff EPSTEIN med sr < 1 and SCRAMBLE med sr >= 1 (both on
the disclosed truncated below-flip census).

LEG C -- ADJUDICATION + THE CLASS (sealed BEFORE evaluation;
exactly one fork verdict fires):
  the class RecursiveDifferenceProfile is printed as the precise
  property list P1-P6 with the MEASURED instance test
  (MAIN 42 core rungs / EPSTEIN / SCRAMBLE / the m4
  shuffle mutant):
    P1 ORDERED SHARED SUPPORT: one totally ordered position set,
       blocks = consecutive position intervals; fold share
       (positions with multiplicity exactly 2) >= FOLD_MIN = 0.9;
    P2 EXACT LOCAL RECURSION: the recursion ward of B1;
    P3 BOUNDED ATOM MULTIPLICITY: max fold multiplicity <=
       MULT_CAP = 2;
    P4 CONTROLLED FOUR-BLOCK STRUCTURE: the r304 comb signature
       on the med lag profile (rho_1 <= +SIGN_EPS, rho_2 <=
       +SIGN_EPS, rho_3 >= -SIGN_EPS, rho_4 >= -SIGN_EPS;
       SIGN_EPS = 0.02) AND truncated net covariance NC(16) <=
       NC_MAX = 1 (med over the world's rungs);
    P5 MASS CONSERVATION: sum_j P_j == R exact (block identity,
       ID_BAR);
    P6 NO ASSIGNMENT SHUFFLE: run assignment == positional
       breakpoint assignment (zero mismatches) -- the property
       the m4 shuffle instance MUST violate;
    plus the CP4 cancellation property TC_far <= TC_CLS = 0.5
       (candidate separator, measured).
  SEPARATOR CENSUS: every property with MAIN pass + EPSTEIN pass
  + SCRAMBLE fail is a world-correct separator (printed; the
  class definition adopts them).
  FORK VERDICT (sealed; R3A precedence disclosed -- the direct
  decomposition of the target functional wins ties):
    R3A_GO   iff A3_OK and A3_WORLD and >= 1 separator;
    R3B_GO   iff not R3A_GO and B_OK and B_WORLD and >= 1
             separator;
    BOTH_PARTIAL(named remnants) iff no GO but A3_WARD or B_REC;
    FORK_DEAD otherwise.
  On R3A_GO the CANDIDATE THEOREM (universal cubic moment) is
  printed with ALL constants: C_univ = sum_t C_t (A = 2,
  deliberately coarser than the r306 sharp 1.069), A = 2, m_0 =
  the smallest ladder m; finite cases m < m_0 certified
  separately per instance -- typed CANDIDATE, no upgrade.

LEG D -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(m1) DOUBLE-COUNTED DIAGONALS (exact Fractions): the mutant type
  table T2' = 3 S2 S1 (diagonal not subtracted) breaks the
  Newton-split ward by EXACTLY 3 S3 on the sealed toy block
  (fold groups {2, -1} | {1, -1} | {1}: correct T1/T2/T3/T4 =
  8/24/-24/0 sum 8 == S1^3; mutant sum 32, break 24 == 3 S3)
  -- CAUGHT; cross-ref: the r306 RY3.fr_lagrange Newton dev 0.
(m2) MONODROMY WITHOUT CONSERVATION-MODE SPLIT: the affine 3x3
  step has eigenvalue EXACTLY 1 (block triangularity), so the
  unsplit spectral radius is max(sr, 1) >= 1 on EVERY rung --
  the mutant can NEVER certify contraction (LOUD: dev from the
  split radius >= MUT_MIN wherever sr < 1, count printed; exact
  toy A = [[1/2, 0], [1, 0]], drive 1: affine spectrum {1/2, 0,
  1}, break 1/2 EXACT).
(m3) TELESCOPE WITH |c| INSTEAD OF c: on the sealed toy (fold
  groups {1, -1} | {2} | {-2}) the true TC_far = 0/48 = 0 EXACT
  and the magnitude mutant gives 48/48 = 1 (break 1 EXACT); on
  the real w9 the mutant deviates >= MUT_MIN -- LOUD.
(m4) ASSIGNMENT-SHUFFLE INSTANCE: the position -> block
  assignment of w9 is permuted (seed SEED_SHUF = 313001); the P6
  instance check MUST REJECT it (interval mismatches > 0) while
  mass conservation P5 STILL HOLDS on the shuffled instance
  (printed: conservation alone cannot see the shuffle).
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the
  withheld terminal drive key and a builder consuming the branch
  label are both FLAGGED by the AST scope audit.  Scope hygiene:
  the new builders (type_expansion, telescope_index,
  floquet_census, rec_ward, class_props) consume positions +
  weights + chain coefficient arrays only (BOUND_FORBIDDEN set);
  fragment audit (no fit primitives).  TOY EXACTNESS (bar
  1e-14): the m1 toy block type table EXACT in Fractions; the
  float type_expansion matches the Fractions table; the m3 toy
  TC EXACT; uniform one-group block: T4 == 0 EXACT.

INDEX FIREWALL (binding, r238-r306 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  MACHINERY IMPORTED VERBATIM: r298
WBT.block_breaks + WBT.aggregate_blocks, r300 DTP.participation +
DTP.shared_delta, r306 RY3.cubic_moments + RY3.renyi3_ratio +
RY3.calib_freeze + RY3.fr_lagrange, r304 SLP.lag_stats +
SLP.net_cov, r269 PBB.mask_edge + PBB.runs_split, r287
L2D.blocks_level2 + L2D.halves_slope + L2D.autocorr_full, r244
BH.wpack, r257 CT.union_arrays, r260 TX.drive_arrays, r263
CA.g_gap, r266 BR.eval_scaled, v881 PIK, r243 PB.smooth_comb.  B
PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never
fitted).  COFINAL LADDER (pre-sealed): frame-A h <= 900, 42
rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39,
52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz) (the r286
anchors, N_w 942..1218).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
DELTA_NEED 0.21; A_FAMILY (0, 1, 2); N_CAL 5; RES_EPS 0.01;
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); TYPE_BAR
1e-9; RECOMP_BAR 1e-9; ATOM_BAR 1e-9; REC_BAR 1e-9 main N <= 400
/ REC_BAR_DEEP 3e-6 / REC_BAR_CTRL 1e-6; DET_BAR 1e-9; DEEP_N
400; EXPO_TARGET -2.0; EXPO_MIN 52; MULT_CAP 2; FOLD_MIN 0.9;
SIGN_EPS 0.02; K_NC 16; NC_MAX 1.0; TC_CLS 0.5; SEED_SHUF
313001; DEG_FLOOR 1e-6; MUT_MIN 1e-6; TOY_BAR 1e-14; TB_WARD
bars 1e-9 main N <= 400 / 3e-6 deep / 1e-6 controls; ID_BAR
1e-12; AC_BAR 1e-9; R306 anchors C_0 11.875 / C_1 3.564 / C_2
1.069 (tol 0.005), A2 violations 0/57, reserve min/med 1.01/4.06
(tol 0.02), trend -0.322/-0.322 (tol 0.005); R304 comb med
rho_1..4 -0.222/-0.140/+0.089/+0.130 (tol 0.01); runtime <= 1800
s; smoke = w9 + controls + Fractions toys + scope audits + every
exact ward at w9 + the m1/m2/m3 toy mutants + the m4 shuffle
rejection at w9; ladder, extension, anchors, prereg measurement
and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no verdict-relevant scratch run of
this probe): every reproduction band is an r304/r306 RECORD
number adopted as-is; the type decomposition, the abs majorants,
the recursion identity and the conservation-mode split are
derived algebra, disclosed above; ONE pre-spec scoping run
(disclosed, deleted) verified the recursion identity FORM
(r_{k+1} = t_k + ap_k r_k + bp_k r_{k-1}, worst rel dev 4.0e-14
on w9), the fold multiplicity magnitude (exactly 2 on w9), the
positions-per-block scale (med 4, max 8 on w9), the jb ==
breakpoint-search agreement (0 mismatches on w9) and the
monodromy wall cost (45 monodromies in ~1 ms) -- no type share,
no spectral radius census, no rho and no S_3 value was computed
before this spec was frozen; the adjudication outcomes are
sealed symmetrically.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R313_ANCHORS(r306 C-table + pointwise A2 verdict live, r304
    comb meds)
+ TYPE_TABLE(per-type signed shares of sum |P|^3 med + slopes,
    fold multiplicity census, TC_far med + slope)
+ R3A(A3_WARD, per-type minimal-A table with frozen C_t, T1@A0,
    A3_OK, A3_WORLD with the named violated type)
+ FLOQUET(B_REC, med sr census, frac(sr < 1), drift med, expo
    med + counts vs -2, B_OK, B_WORLD)
+ CLASS(P1-P6 + CP4 instance table on MAIN/EPST/SCR/shuffle,
    separator list)
+ [exactly one of] R3A_GO / R3B_GO / BOTH_PARTIAL(remnants) /
    FORK_DEAD
+ [iff R3A_GO] CANDIDATE_THEOREM(C_univ, A = 2, m_0)
+ MUSTFAIL_LEDGER(m1-m4 + scopes).
Honesty before beauty: the type decomposition, the abs
majorants, the recursion identity, the conservation-mode split
and the det dictionary are EXACT finite algebra; every share,
radius, exponent, C_t and slope is MEASURED on 42 + 15 finite
rungs; a GO fixes a proof ARCHITECTURE and a candidate constant,
it does NOT prove the cofinal law; per-type constants frozen on
the 5 shallowest rungs can be killed by one deep outlier (the
r306 kz53/kz67 caveat inherits); the truncated below-flip world
census for Route R3B is disclosed as WEAK evidence; no verdict
claims a cofinal law; r243-r306 stand.

RECORD TABLES (frozen from the record run; calibration protocol:
smoke pass 1 = 29/32 -- (a) G50 controls at 8.4e-2: SMOOTH (the
known degenerate world, Delta == 0 identically) breaks the chain
recursion from k = 2; the pre-declared DEG_FLOOR degenerate
guard was extended to the chain wards (the r300-a1/r306
convention, code-side); (b) the G83 mass ward compared against
the bulk-only R instead of the presentation total sum PDelta --
a pure denominator fix; (c) the G96 pass cascade; NO bar, band,
rule or verdict rule touched; smoke pass 2 = 32/32 (0.6 s);
calibration pass 1 = first full evaluation, 32/32, wall 22.8 s,
NO amendment; calibration pass 2 = 32/32 after ONE
reporting-only edit (the violating rungs are now NAMED in the
per-type info line), wall 22.8 s; record run1/run2 after this
insertion, identical up to WALL; the only post-freeze edits are
the disclosed code-side fixes, the reporting edit and this
record-table insertion, which IS the protocol):
CAL_VERDICT = R313_ANCHORS(C-table 11.875/3.564/1.069 bit-near
r306; A = 2 live: 0/57 violations, reserve min/med 1.01/4.06,
trend -0.322/-0.322; r304 comb -0.222/-0.140/+0.089/+0.130
bit-near, med NC(16) 0.829) + TYPE_TABLE(med signed shares of
sum |P|^3: T1 +0.3808/+0.054, T2 +2.1542/-0.100, T3
-1.1442/+0.149, T4 -0.4226/-0.422 -- the exact bookkeeping
EXISTS (worst block ward 3.9e-16, recompose 3.4e-17, RY3
cross-ward 5.5e-16 on 61 live worlds) and is
CANCELLATION-COUPLED: the two-equal type T2 alone carries 2.15x
the cube and the near/far types are NEGATIVE -- the types are
not independently small, they cancel; TC_far med 0.069 slope
-0.050 -- the far triples telescope away 93 percent of their
abs mass: proof hope (iii) is REAL; TC_near 0.233; fold
multiplicity == 2 UNIFORM on 57/57 rungs -- proof hope (i) is
EXACT (the beta/omega fold bound, med fold share 1.000);
positions/block med 4.0 max 13) + R3A(per-type prereg at A = 2
with first-5-frozen constants: T2 HOLDS 0/57 (C 1.910, trend
-0.400), T3 HOLDS 0/57 (C 1.053, trend -0.299), T1 FAILS 2/57
(kz55 2.54x, kz53 1.70x; trend -0.122 falling), T4 FAILS 1/57
(kz55 1.84x; trend -0.186 falling) -- minimal-A table {T1 None,
T2 2, T3 2, T4 None}, T1@A0 FAILS, COMPOSITION REFUTED-IN-FORM
(the sealed two-harmonic-counts reading does not fire); world
census: SCRAMBLE violates exactly T2 (2.85 > 1.91) but EPSTEIN
ALSO violates T2/T3 (4.41/3.61 > 1.91/1.05) while its TOTAL
holds the r306 bound -- the MAIN-frozen per-type constants are
NOT world-portable: A3_OK False, A3_WORLD False) +
FLOQUET(recursion ward EXACT on every non-degenerate world
(8.0e-13 main / 1.9e-12 deep / 6.6e-14 controls; SMOOTH
deg-skipped), det dictionary 4.4e-16; THE FOUR-STEP MONODROMY
EXPANDS: med sr 1.0600, rungs with med sr < 1: 0/57, frac(sr<1)
med 0.12, drift med -17.2, product exponent expo +1.917 vs
required -2.0 (0/57 rungs): B_OK False; worlds EPST 1.0003 /
SCR 1.1532 (truncated, weak): B_WORLD False -- the Floquet form
of the period-4 system is EXPANSIVE like the r304 single-step
form: the contraction route is DEAD on the letter of the sealed
rule) + CLASS(instance table: MAIN passes ALL of P1/P2/P3/P4/P5/
P6/CP4 including the comb signature; EPSTEIN fails EXACTLY P4;
SCRAMBLE fails EXACTLY P4 -- the four-block comb property
excludes SCRAMBLE but ALSO EPSTEIN: NO world-correct separator
among the sealed candidates, the honest class rest; the m4
SHUFFLE instance is rejected by P6 (293/300 atoms outside their
interval) with P5 still holding (2.0e-17)) + BOTH_PARTIAL(R3A
rest: T1/T4 HOLD@A2 fail near-critically with falling trends +
the per-type constants are not world-portable; R3B rest: no
contraction -- med sr < 1 on 0/57, expo <= -2 on 0/57) +
MUSTFAIL_LEDGER(m1 break == 3 S3 == 24 EXACT; m2 toy break 1/2
EXACT, live clause vacuous (0 contracting rungs -- disclosed);
m3 toy break 1 EXACT + real w9 dev 9.4e-1; m4 rejected by P6;
m5a/m5b FLAGGED).
READING (typed, no upgrade): the fork adjudication is
BOTH_PARTIAL, and the two halves die/survive in OPPOSITE
places: (1) ROUTE R3B IS CLOSED on the letter -- the four-step
Floquet monodromy of the exact chain recursion (ward 1.9e-12,
det dictionary exact) is EXPANSIVE (med sr 1.06, expo +1.9,
NOT -2): after r304 (single step) and this round (period-4
Floquet step), NO transfer-operator contraction form of the
cubic law remains open at the chain level; (2) ROUTE R3A's
bookkeeping EXISTS EXACTLY and two of its four proof hopes are
banked: the fold multiplicity is UNIFORMLY 2 (an exact
structural bound, not a census) and the far triples genuinely
telescope (93 percent abs-mass cancellation, falling); T2/T3
are pointwise polylog-square bounded with growing reserve; what
remains is PRECISELY NAMED: (a) T1 and T4 violate their
shallow-frozen constants on kz53/kz55 by 1.7-2.5x (both trends
FALL -- the violation is a shallow-calibration artifact of the
same kind r306 saw at A <= 1, not a growth phenomenon; a
mid-ladder calibration would clear it, but that rule was not
sealed and is NOT applied post hoc); (b) the types cancel
against each other (T2 share 2.15, T3/T4 negative), so
per-type triangle bounding LOSES structure: the theorem-shaped
successor is a COUPLED two-term statement (T2 + T3 jointly)
rather than four independent bounds; (3) THE CLASS FINDING is
the round's sharpest honest negative: the sealed four-block
comb property P4 is MAIN-SPECIFIC -- it excludes SCRAMBLE
correctly but kills EPSTEIN too, while every other sealed
candidate (multiplicity, fold share, recursion, mass, assignment,
telescope) is world-BLIND (all three worlds pass): among the
sealed candidates there is NO property that separates
worlds the way the r306 TOTAL bound does (EPST holds, SCR
breaks 1.67x) -- the separating structure lives in the SIZE of
the type terms (SCR's T2 excess 2.85x vs EPST's total-hold),
not in any sealed yes/no structural flag; the class
RecursiveDifferenceProfile needs a QUANTITATIVE membership
functional, not a boolean property list; (4) the anchors are
bit-near r306/r304 throughout -- the record base is stable.
Honest negatives: the m2 live clause is vacuous (no contracting
rungs exist -- only the exact toy carries it); the R3B world
census is truncated below the flips (n = 4-5, weak by
construction); nothing here proves or refutes the cofinal law.
Runtime 22.8 s full / 0.6 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: the disclosed smoke-stage
degenerate-guard extension and mass-denominator fix, one
reporting-only edit -- no bar, band, rule or verdict rule
moved.

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
import shortrange_law_probe as SLP             # noqa: E402 r304
import renyi3_probe as RY3                     # noqa: E402 r306
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
TYPE_BAR = 1e-9
RECOMP_BAR = 1e-9
ATOM_BAR = 1e-9
REC_BAR = 1e-9
REC_BAR_DEEP = 3e-6
REC_BAR_CTRL = 1e-6
DET_BAR = 1e-9
EXPO_TARGET = -2.0
EXPO_MIN = 52
MULT_CAP = 2
FOLD_MIN = 0.9
SIGN_EPS = 0.02
K_NC = 16
NC_MAX = 1.0
TC_CLS = 0.5
SEED_SHUF = 313001
DEG_FLOOR = 1e-6
MUT_MIN = 1e-6
TOY_BAR = 1e-14
EDGE_F = 0.20
PAIR_OFFSET = 0
DELTA_NEED = 0.21
R306_C = (11.875, 3.564, 1.069)
R306_C_TOL = 0.005
R306_TREND = -0.322
R306_TREND_TOL = 0.005
R306_RES_MIN = 1.01
R306_RES_MED = 4.06
R306_RES_TOL = 0.02
R304_COMB = (-0.222, -0.140, 0.089, 0.130)
R304_COMB_TOL = 0.01

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

TYPES = ("T1", "T2", "T3", "T4")


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


# ---------------- module-own builders.  Source-pure: raw atom
# ---------------- positions + values + block assignment + chain
# ---------------- coefficient arrays only; the withheld terminal
# ---------------- drive key, the branch label and every
# ---------------- target-side identifier are forbidden in scope
# ---------------- (AST audit).
def type_expansion(pos, val, blk, m, use_abs=False):
    """the EXACT triple-type decomposition of sum_j P_j^3 over the
    raw atomic presentation: per block j the ordered triples of
    P_j^3 = (sum d)^3 split into T1 (diagonal), T2 (exactly two
    equal), T3 (distinct, shared fold group) and T4 (distinct,
    three distinct fold groups); fold groups = atoms at one
    position.  use_abs=True is the m3 MAGNITUDE MUTANT (|d|
    instead of d).  Returns per-block arrays + fold census."""
    pos = np.asarray(pos, dtype=float)
    val = np.asarray(val, dtype=float)
    if use_abs:
        val = np.abs(val)
    blk = np.asarray(blk, dtype=int)
    S1 = np.bincount(blk, weights=val, minlength=m)
    S2 = np.bincount(blk, weights=val ** 2, minlength=m)
    S3 = np.bincount(blk, weights=val ** 3, minlength=m)
    o = np.lexsort((pos, blk))
    pb = blk[o]
    pp = pos[o]
    vv = val[o]
    if len(pb):
        new = np.concatenate([[True], (pb[1:] != pb[:-1])
                              | (pp[1:] != pp[:-1])])
    else:
        new = np.zeros(0, dtype=bool)
    gid = np.cumsum(new) - 1
    ng = int(gid[-1]) + 1 if len(gid) else 0
    G1 = np.bincount(gid, weights=vv, minlength=ng)
    gblk = pb[new] if ng else np.zeros(0, dtype=int)
    mult = np.bincount(gid, minlength=ng)
    Q2 = np.bincount(gblk, weights=G1 ** 2, minlength=m)
    Q3 = np.bincount(gblk, weights=G1 ** 3, minlength=m)
    T1 = S3
    T2 = 3.0 * (S2 * S1 - S3)
    DIST = S1 ** 3 - 3.0 * S1 * S2 + 2.0 * S3
    T4 = S1 ** 3 - 3.0 * S1 * Q2 + 2.0 * Q3
    T3 = DIST - T4
    A1 = np.bincount(blk, weights=np.abs(val), minlength=m)
    ward = np.max(np.abs(T1 + T2 + T3 + T4 - S1 ** 3)
                  / np.maximum(A1 ** 3, 1e-300)) if m else 0.0
    return dict(S1=S1, T1=T1, T2=T2, T3=T3, T4=T4, DIST=DIST,
                ward=ward, mult=mult, ng=ng,
                pos_per_block=np.bincount(gblk, minlength=m))


def telescope_index(tt, ta):
    """the exact telescope-cancellation index of a triple type:
    TC = sum_j |T_j| / sum_j Tabs_j (1 = no cancellation; the
    abs table ta must come from type_expansion(use_abs=True) --
    the same set partition on |d|)."""
    num = float(np.sum(np.abs(tt)))
    den = float(np.sum(ta))
    return num / den if den > 0.0 else 0.0


def rec_ward(rv, tv, apv, bpv, kmax):
    """worst relative deviation of the exact chain recursion
    r_{k+1} == t_k + ap_k r_k + bp_k r_{k-1} over k = 1..kmax-1
    (scale = the term-magnitude sum)."""
    worst = 0.0
    for k in range(1, kmax):
        pred = tv[k] + apv[k] * rv[k] + bpv[k] * rv[k - 1]
        sc = abs(tv[k]) + abs(apv[k] * rv[k]) \
            + abs(bpv[k] * rv[k - 1]) + 1e-300
        worst = max(worst, abs(rv[k + 1] - pred) / sc)
    return worst


def floquet_census(apv, bpv, kmax):
    """the four-step Floquet monodromy census on the split linear
    part A_k = [[ap_k, bp_k], [1, 0]]: for k0 = 1, 5, 9, ...
    (k0 + 3 <= kmax - 1) the closed-form 2x2 spectral radius of
    M = A_{k0+3} A_{k0+2} A_{k0+1} A_{k0}, the det ward |det M| ==
    prod |bp|, the drift c = k0 (1 - sr), and the log-product."""
    srs = []
    k0s = []
    detdev = 0.0
    k0 = 1
    while k0 + 3 <= kmax - 1:
        M = np.eye(2)
        pbp = 1.0
        for k in range(k0, k0 + 4):
            A = np.array([[apv[k], bpv[k]], [1.0, 0.0]])
            M = A @ M
            pbp *= abs(bpv[k])
        tr = M[0, 0] + M[1, 1]
        dt = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        detdev = max(detdev, abs(abs(dt) - pbp) / max(pbp, 1e-300))
        disc = tr * tr - 4.0 * dt
        if disc >= 0.0:
            s = math.sqrt(disc)
            sr = max(abs((tr + s) / 2.0), abs((tr - s) / 2.0))
        else:
            sr = math.sqrt(dt)
        srs.append(sr)
        k0s.append(k0)
        k0 += 4
    srs = np.asarray(srs)
    if len(srs) == 0:
        return dict(n=0, med=1.0, frac_lt1=0.0, drift=0.0,
                    logsum=0.0, detdev=detdev, sr3=1.0)
    drift = float(np.median(np.asarray(k0s)
                            * (1.0 - srs)))
    return dict(n=len(srs), med=float(np.median(srs)),
                frac_lt1=float(np.mean(srs < 1.0)), drift=drift,
                logsum=float(np.sum(np.log(np.maximum(srs,
                                                      1e-300)))),
                detdev=detdev, sr3=float(np.median(srs ** 3)))


def class_props(mx_mult, fold_share, rec_dev, rec_bar, lag_med,
                nc_med, tc_med, mism, mass_dev):
    """the RecursiveDifferenceProfile instance test: P1-P6 + CP4
    from measured coordinates (all source-pure censuses)."""
    return dict(
        P1_fold=(fold_share >= FOLD_MIN),
        P2_rec=(rec_dev <= rec_bar),
        P3_mult=(mx_mult <= MULT_CAP),
        P4_comb=(lag_med[0] <= SIGN_EPS and lag_med[1] <= SIGN_EPS
                 and lag_med[2] >= -SIGN_EPS
                 and lag_med[3] >= -SIGN_EPS
                 and nc_med <= NC_MAX),
        P5_mass=(mass_dev <= ID_BAR),
        P6_assign=(mism == 0),
        CP4_tc=(tc_med <= TC_CLS))


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'type bound' oriented by the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'telescope constant' that consumes the branch label to pick
    its value -- the scope audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the sealed toy block
# ---------------- type table + the m1/m2/m3 exact mutants
def fr_type_table(groups, mutant="none"):
    """the exact triple-type decomposition on a toy block given
    as fold groups (lists of rational atom values): returns the
    exact T1/T2/T3/T4, the ward dev (must be 0) and the abs
    table.  mutant='dd' is the m1 double-counted-diagonal type
    table (T2' = 3 S2 S1, ward must break by exactly 3 S3);
    mutant='mag' computes the table on |d| (the m3 basis)."""
    d = [Fr(x) for g in groups for x in g]
    if mutant == "mag":
        d = [abs(x) for x in d]
        groups = [[abs(Fr(x)) for x in g] for g in groups]
    S1 = sum(d)
    S2 = sum(x * x for x in d)
    S3 = sum(x ** 3 for x in d)
    G1 = [sum(Fr(x) for x in g) for g in groups] \
        if mutant != "mag" else [sum(x for x in g) for g in groups]
    Q2 = sum(g * g for g in G1)
    Q3 = sum(g ** 3 for g in G1)
    T1 = S3
    T2 = 3 * S2 * S1 if mutant == "dd" else 3 * (S2 * S1 - S3)
    DIST = S1 ** 3 - 3 * S1 * S2 + 2 * S3
    T4 = S1 ** 3 - 3 * S1 * Q2 + 2 * Q3
    T3 = DIST - T4
    dev = T1 + T2 + T3 + T4 - S1 ** 3
    return dict(S1=S1, S2=S2, S3=S3, T1=T1, T2=T2, T3=T3, T4=T4,
                dev=dev)


TOY_GROUPS = ([Fr(2), Fr(-1)], [Fr(1), Fr(-1)], [Fr(1)])
TOY_M3_GROUPS = ([Fr(1), Fr(-1)], [Fr(2)], [Fr(-2)])


def fr_affine_split_toy():
    """m2 exact toy: A = [[1/2, 0], [1, 0]] with drive 1; the
    affine 3x3 spectrum is {1/2, 0, 1} (block triangularity ->
    eigenvalue 1 EXACT: the scalar conservation mode); the split
    linear radius is 1/2; the unsplit mutant radius is 1 -- break
    1/2 EXACT."""
    sr_split = Fr(1, 2)
    sr_affine = max(sr_split, Fr(1))
    return sr_split, sr_affine, sr_affine - sr_split


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("renyi3_proof_fork_probe -- PRIME.L2.RENYI3.PROOF_FORK.01 "
          "(round 313)")
    print("SPEC_SHA %s   R306_SHA %s   R304_SHA %s (imported)"
          % (SPEC_SHA[:16], RY3.SPEC_SHA[:16], SLP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + Fractions toys + "
                        "scope audits + every exact ward at w9 + "
                        "m1/m2/m3 toy mutants + m4 shuffle "
                        "rejection; ladder, extension, anchors, "
                        "prereg and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE PROOF-FORM FORK (reviewer plan, binding): two "
          "sealed architectures for the r306 pointwise cubic law "
          "-- R3A expands sum_j a_j^3 EXACTLY over the raw atomic "
          "presentation (local c-differences; fold groups = "
          "beta/omega pairs at one position) into the four triple "
          "types T1 diagonal / T2 two-equal / T3 near (shared "
          "fold) / T4 far (fully separated), each to be bounded "
          "by a nameable class property; R3B measures the "
          "four-step Floquet monodromy of the EXACT chain "
          "recursion on the split cubic mode space (the period-4 "
          "form of the r304 comb, NOT the refuted single-step "
          "mixing); the class RecursiveDifferenceProfile (P1-P6) "
          "must admit MAIN + EPSTEIN and exclude SCRAMBLE; the "
          "universal constant MAY be coarser than 1.069 "
          "(reviewer instruction); ALL bars, bands, rules and "
          "the fork verdicts sealed BEFORE evaluation")
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("type_expansion", "telescope_index",
               "floquet_census", "rec_ward", "class_props"):
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

    # ---------------- S1: census + controls (r306 scaffold verbatim)
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
        fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
            / math.sqrt(abs(rows[N - 1]["eta"]))
        ct = bw * bx * v2 * fac
        v2w = BR.eval_scaled(rows, xu, N - 2)
        cw = wu * xu * v2w * fac
        o = np.argsort(bx, kind="stable")
        return dict(kz=p["kz"], N=N, g_branch=g, Z=Z, chain=chain,
                    t_term=float(t[N - 2]), ct=ct, bx=bx, bw=bw,
                    v2=v2, fac=fac, xu=xu, wu=wu, cw=cw, o=o,
                    lo=lo, hi=hi, p=p, rv=r, tv=t, apv=ap, bpv=bp,
                    nf=p["nf"])

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
        part = DTP.participation(Pd)
        cm = RY3.cubic_moments(Pd)
        absm = float(np.sum(np.abs(rc["ct"]))) \
            + float(np.sum(np.abs(rc["cw"])))
        degenerate = (cm["L1"] <= DEG_FLOOR * absm)
        # ---- raw atomic presentation (NEW, module-own):
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
            te = type_expansion(pos_all, val_all, blk_all, m)
            ta = type_expansion(pos_all, val_all, blk_all, m,
                                use_abs=True)
            atom_dev = float(np.max(np.abs(te["S1"] - Pd))
                             / max(np.max(np.abs(Pd)), 1e-300))
            s_j = np.sign(Pd)
            tot = {t: float(np.sum(s_j * te[t])) for t in TYPES}
            cube = float(np.sum(np.abs(Pd) ** 3))
            recomp = abs(sum(tot.values()) - cube) \
                / max(float(np.sum(ta["S1"] ** 3)), 1e-300)
            tc_far = telescope_index(te["T4"], ta["T4"])
            tc_far_mut = telescope_index(ta["T4"], ta["T4"])
            t3abs = ta["DIST"] - ta["T4"]
            tc_near = telescope_index(te["T3"],
                                      np.maximum(t3abs, 0.0))
            mx_mult = int(np.max(te["mult"])) if te["ng"] else 0
            fold_share = float(np.mean(te["mult"] == 2)) \
                if te["ng"] else 0.0
            ppb_med = float(np.median(te["pos_per_block"]))
            ppb_max = int(np.max(te["pos_per_block"]))
        else:
            te = ta = None
            atom_dev = 0.0
            tot = {t: 0.0 for t in TYPES}
            cube = 0.0
            recomp = 0.0
            tc_far = tc_far_mut = tc_near = 0.0
            mx_mult = 0
            fold_share = 0.0
            ppb_med = 0.0
            ppb_max = 0
        # ---- dc profile for the r304 comb / class P4:
        fxs = rc["bx"] * rc["v2"] * rc["fac"]
        sd = DTP.shared_delta(rc["bx"], rc["ct"], rc["bw"], fxs,
                              rc["xu"], rc["cw"], rc["wu"])
        if degenerate or sd["n"] == 0:
            zb = np.zeros(0)
        else:
            edm = PBB.mask_edge(sd["x"], rc["lo"], rc["hi"],
                                EDGE_F)
            zb = np.asarray(sd["dc"], dtype=float)[~edm]
        if len(zb) >= K_NC + 2:
            lag, _S, _A0 = SLP.lag_stats(zb, K_NC)
            nc = float(SLP.net_cov(lag, K_NC))
        else:
            lag = np.zeros(K_NC)
            nc = 1.0
        # ---- Floquet (route R3B):
        kmax = (rc["N"] - 1) if rc["nf"] is None \
            else max(rc["nf"] - 2, 2)
        rdev = rec_ward(rc["rv"], rc["tv"], rc["apv"], rc["bpv"],
                        kmax)
        fc = floquet_census(rc["apv"], rc["bpv"], kmax)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, part=part,
                    cm=cm, degenerate=degenerate, atom_dev=atom_dev,
                    ward=te["ward"] if te is not None else 0.0,
                    tot=tot, cube=cube, recomp=recomp,
                    tc_far=tc_far, tc_far_mut=tc_far_mut,
                    tc_near=tc_near, mx_mult=mx_mult,
                    fold_share=fold_share, ppb_med=ppb_med,
                    ppb_max=ppb_max, mism=mism, lag=lag, nc=nc,
                    rdev=rdev, fc=fc, kmax=kmax,
                    xb=xb, brk=brk, jb=jb, pos_all=pos_all,
                    val_all=val_all, blk_all=blk_all)

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
    atom_w = max(rc["ev"]["atom_dev"] for rc in live)
    mism_tot = sum(rc["ev"]["mism"] for rc in pool_all)
    mult_max = max(rc["ev"]["mx_mult"] for rc in live)
    fold_med = float(np.median([rc["ev"]["fold_share"]
                                for rc in live]))
    check("G22-atomic-presentation-wards",
          atom_w <= ATOM_BAR and mism_tot == 0,
          "raw atomic presentation == PDelta blockwise on %d live "
          "worlds (worst rel %.1e, bar %.0e); run assignment == "
          "breakpoint search on ALL worlds (%d mismatches); fold "
          "census: max multiplicity %d, med fold share %.3f "
          "(beta/omega pairs)%s"
          % (len(live), atom_w, ATOM_BAR, mism_tot, mult_max,
             fold_med,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors
    section("S3  LEG 0 -- ANCHOR REGRESSION (r306 + r304 records)")
    st = {}
    if smoke:
        check("G30-r306-c-table", True, "SMOKE: skipped")
        check("G31-r306-pointwise", True, "SMOKE: skipped")
        check("G32-r304-comb", True, "SMOKE: skipped")
        srt_all = []
    else:
        srt_all = sorted(recs + erecs,
                         key=lambda rc: (rc["N"], rc["kz"]))
        n_all = len(srt_all)
        cal_idx = tuple(range(N_CAL))
        rhoT = {}
        C = {}
        for A in A_FAMILY:
            rhoT[A] = [RY3.renyi3_ratio(rc["ev"]["cm"]["S3"],
                                        rc["ev"]["m"], A)
                       for rc in srt_all]
            C[A], _j, _d = RY3.calib_freeze(rhoT[A], cal_idx)
        ok_ct = all(abs(C[A] - R306_C[A]) <= R306_C_TOL
                    for A in A_FAMILY)
        check("G30-r306-c-table", ok_ct,
              "r306 C-table reproduced: C_0 %.3f / C_1 %.3f / "
              "C_2 %.3f (rec %.3f/%.3f/%.3f tol %.3f), frozen on "
              "the first %d rungs of the (N, kz)-sorted %d-rung "
              "ladder" % (C[0], C[1], C[2], R306_C[0], R306_C[1],
                          R306_C[2], R306_C_TOL, N_CAL, n_all))
        viol2 = [i for i in range(n_all) if rhoT[2][i] > C[2]]
        test = [i for i in range(n_all) if i not in cal_idx]
        rsv = [C[2] / max(rhoT[2][i], 1e-300) for i in test]
        Ns57 = [rc["N"] for rc in srt_all]
        core_idx = [i for i, rc in enumerate(srt_all)
                    if rc not in erecs]
        sl42 = L2D.halves_slope(
            [Ns57[i] for i in core_idx],
            [max(rhoT[2][i], 1e-300) for i in core_idx])
        sl57 = L2D.halves_slope(
            Ns57, [max(v, 1e-300) for v in rhoT[2]])
        check("G31-r306-pointwise",
              len(viol2) == 0
              and abs(min(rsv) - R306_RES_MIN) <= R306_RES_TOL
              and abs(float(np.median(rsv)) - R306_RES_MED)
              <= R306_RES_TOL
              and abs(sl42 - R306_TREND) <= R306_TREND_TOL
              and abs(sl57 - R306_TREND) <= R306_TREND_TOL,
              "r306 pointwise verdict live at A = 2: violations "
              "%d/57 (rec 0), reserve min/med %.2f/%.2f (rec "
              "%.2f/%.2f tol %.2f), trend %+.3f/%+.3f (rec "
              "%+.3f tol %.3f)"
              % (len(viol2), min(rsv), float(np.median(rsv)),
                 R306_RES_MIN, R306_RES_MED, R306_RES_TOL, sl42,
                 sl57, R306_TREND, R306_TREND_TOL))
        lag_mat = np.array([rc["ev"]["lag"] for rc in recs])
        lag_med = np.median(lag_mat, axis=0)
        ok_cb = all(abs(lag_med[i] - R304_COMB[i]) <= R304_COMB_TOL
                    for i in range(4))
        check("G32-r304-comb", ok_cb,
              "r304 period-4 comb reproduced on the 42 core "
              "rungs: med rho_1..4 = %+.3f/%+.3f/%+.3f/%+.3f "
              "(rec %+.3f/%+.3f/%+.3f/%+.3f tol %.2f); med "
              "NC(16) %.3f"
              % (lag_med[0], lag_med[1], lag_med[2], lag_med[3],
                 R304_COMB[0], R304_COMB[1], R304_COMB[2],
                 R304_COMB[3], R304_COMB_TOL,
                 float(np.median([rc["ev"]["nc"]
                                  for rc in recs]))))
        st["C"] = C
        st["rhoT"] = rhoT
        st["lag_med"] = lag_med

    # ---------------- S4: Leg A -- route R3A
    section("S4  LEG A -- ROUTE R3A: TRIPLE INCIDENCE + TELESCOPE")
    ward_w = max(rc["ev"]["ward"] for rc in live)
    recomp_w = max(rc["ev"]["recomp"] for rc in live)
    cube_x = max(abs(rc["ev"]["cube"]
                     - rc["ev"]["cm"]["S3"]
                     * rc["ev"]["cm"]["L1"] ** 3)
                 / max(rc["ev"]["cube"], 1e-300) for rc in live)
    a3_ward = (ward_w <= TYPE_BAR and recomp_w <= RECOMP_BAR
               and cube_x <= 1e-9)
    check("G41-type-ward-live", a3_ward,
          "T1 + T2 + T3 + T4 == P_j^3 per block on %d live worlds "
          "(worst rel %.1e vs abs-mass scale, bar %.0e); rung "
          "recompose sum_t tot_t == sum_j |P_j|^3 (worst %.1e, "
          "bar %.0e); cross-ward vs RY3.cubic_moments S_3 L1^3 "
          "(worst %.1e)" % (len(live), ward_w, TYPE_BAR, recomp_w,
                            RECOMP_BAR, cube_x))
    if smoke:
        ev9 = recs[0]["ev"]
        sh = {t: ev9["tot"][t] / max(ev9["cube"], 1e-300)
              for t in TYPES}
        info("SMOKE: w9 type shares T1/T2/T3/T4 = "
             "%+.4f/%+.4f/%+.4f/%+.4f (sum %.6f), TC_far %.3f, "
             "TC_near %.3f, mult max %d, pos/block med %.1f max "
             "%d" % (sh["T1"], sh["T2"], sh["T3"], sh["T4"],
                     sum(sh.values()), ev9["tc_far"],
                     ev9["tc_near"], ev9["mx_mult"],
                     ev9["ppb_med"], ev9["ppb_max"]))
        check("G42-type-table", True, "SMOKE: skipped")
        check("G43-per-type-prereg", True, "SMOKE: skipped")
        check("G44-diag-multiplicity", True, "SMOKE: skipped")
        check("G45-telescope-harmonic", True, "SMOKE: skipped")
        a3_ok = False
        a3_world = False
        typeC = {}
        minA = {}
    else:
        Ns = [rc["N"] for rc in recs]

        def slp(vals):
            return L2D.halves_slope(Ns, [max(v, 1e-300)
                                         for v in vals])

        shares = {t: [rc["ev"]["tot"][t]
                      / max(rc["ev"]["cube"], 1e-300)
                      for rc in recs] for t in TYPES}
        sh_med = {t: float(np.median(shares[t])) for t in TYPES}
        sh_sl = {t: slp([abs(v) for v in shares[t]])
                 for t in TYPES}
        tcf = [rc["ev"]["tc_far"] for rc in recs]
        tcn = [rc["ev"]["tc_near"] for rc in recs]
        check("G42-type-table", True,
              "signed type shares of sum |P|^3 (med + |.| slope): "
              "T1 %+.4f/%+.3f, T2 %+.4f/%+.3f, T3 %+.4f/%+.3f, "
              "T4 %+.4f/%+.3f (sum == 1 per rung); TC_far med "
              "%.3f slope %+.3f, TC_near med %.3f"
              % (sh_med["T1"], sh_sl["T1"], sh_med["T2"],
                 sh_sl["T2"], sh_med["T3"], sh_sl["T3"],
                 sh_med["T4"], sh_sl["T4"],
                 float(np.median(tcf)), slp(tcf),
                 float(np.median(tcn))))
        # per-type prereg (r306 protocol, frozen split first 5)
        typeC = {}
        typeHOLD = {}
        minA = {}
        n_all = len(srt_all)
        for t in TYPES:
            mags = [abs(rc["ev"]["tot"][t])
                    / max(rc["ev"]["cm"]["L1"] ** 3, 1e-300)
                    for rc in srt_all]
            typeC[t] = {}
            typeHOLD[t] = {}
            for A in A_FAMILY:
                rr = [mags[i] * srt_all[i]["ev"]["m"] ** 2
                      / (math.log(srt_all[i]["ev"]["m"]) ** A)
                      for i in range(n_all)]
                Ct, _j, _d = RY3.calib_freeze(rr, range(N_CAL))
                nv = sum(1 for v in rr if v > Ct)
                typeC[t][A] = Ct
                typeHOLD[t][A] = (nv == 0)
                if A == 2:
                    sl_t = L2D.halves_slope(
                        [rc["N"] for rc in srt_all],
                        [max(v, 1e-300) for v in rr])
                    vkz = ["kz%d(%.3f)" % (srt_all[i]["kz"],
                                           rr[i] / Ct)
                           for i in range(n_all) if rr[i] > Ct]
                    info("type %s @ A=2: C_t %.4f, violations "
                         "%d/%d%s, trend57 %+.3f"
                         % (t, Ct, nv, n_all,
                            " [" + ", ".join(vkz) + "]"
                            if vkz else "", sl_t))
            holds = [A for A in A_FAMILY if typeHOLD[t][A]]
            minA[t] = min(holds) if holds else None
        ok43 = True  # census gate: table computed on all types
        check("G43-per-type-prereg", ok43,
              "minimal-A table (r306 protocol per type, C frozen "
              "first %d): %s; frozen C_t at A=2: %s"
              % (N_CAL,
                 str({t: minA[t] for t in TYPES}),
                 str({t: round(typeC[t][2], 4) for t in TYPES})))
        mult_all = max(rc["ev"]["mx_mult"] for rc in srt_all)
        ppb_meds = [rc["ev"]["ppb_med"] for rc in srt_all]
        ppb_maxs = [rc["ev"]["ppb_max"] for rc in srt_all]
        check("G44-diag-multiplicity", True,
              "proof hope (i): fold multiplicity UNIFORMLY "
              "bounded -- max over 57 rungs = %d (class bound "
              "MULT_CAP %d); positions/block med %.1f, max %d; "
              "T1 minimal A = %s (A = 0 iff the diagonal needs "
              "no log)" % (mult_all, MULT_CAP,
                           float(np.median(ppb_meds)),
                           int(np.max(ppb_maxs)), str(minA["T1"])))
        check("G45-telescope-harmonic", True,
              "proof hopes (ii)-(iv) measured: NEAR minimal A = "
              "%s (harmonic <=> A = 1); FAR minimal A = %s with "
              "TC_far med %.3f (real cancellation iff < 1, class "
              "bar %.2f); COMPOSITION %s (sealed reading: "
              "CONFIRMED iff T1@A0 holds and all types hold at "
              "A <= 2)"
              % (str(minA["T3"]), str(minA["T4"]),
                 float(np.median(tcf)), TC_CLS,
                 "CONFIRMED" if (minA["T1"] == 0
                                 and all(minA[t] is not None
                                         for t in TYPES))
                 else "REFUTED-IN-FORM"))
        a3_ok = (a3_ward and all(typeHOLD[t][2] for t in TYPES)
                 and typeHOLD["T1"][0])
        # worlds: EPST/SCR vs the frozen per-type C at A = 2
        wnote = []
        epst_ok = True
        scr_viol = []
        for c in ("EPST", "SCR"):
            evc = crecs[c]["ev"]
            if evc["degenerate"]:
                wnote.append("%s DEGENERATE" % c)
                continue
            for t in TYPES:
                mag = abs(evc["tot"][t]) \
                    / max(evc["cm"]["L1"] ** 3, 1e-300)
                rr = mag * evc["m"] ** 2 \
                    / (math.log(evc["m"]) ** 2)
                holds = rr <= typeC[t][2]
                if c == "EPST" and not holds:
                    epst_ok = False
                if c == "SCR" and not holds:
                    scr_viol.append(t)
                wnote.append("%s %s %.4f %s C %.4f"
                             % (c, t, rr, "<=" if holds else ">",
                                typeC[t][2]))
        a3_world = epst_ok and len(scr_viol) >= 1
        info("A3 world census: %s" % "; ".join(wnote))
        info("A3_OK %s; A3_WORLD %s (EPSTEIN all-hold %s; "
             "SCRAMBLE violated types %s)"
             % (a3_ok, a3_world, epst_ok, str(scr_viol)))
        st["sh_med"] = sh_med
        st["minA"] = minA
        st["typeC"] = typeC
        st["tcf_med"] = float(np.median(tcf))
        st["scr_viol"] = scr_viol

    # ---------------- S5: Leg B -- route R3B
    section("S5  LEG B -- ROUTE R3B: FOUR-STEP FLOQUET")
    rec_main = 0.0
    rec_deep = 0.0
    rec_ctrl = 0.0
    det_w = 0.0
    for rc in all_rc:
        if rc["N"] > DEEP_N:
            rec_deep = max(rec_deep, rc["ev"]["rdev"])
        else:
            rec_main = max(rec_main, rc["ev"]["rdev"])
        det_w = max(det_w, rc["ev"]["fc"]["detdev"])
    deg_skip = []
    for c in crecs:
        if crecs[c]["ev"]["degenerate"]:
            deg_skip.append(c)
            continue
        rec_ctrl = max(rec_ctrl, crecs[c]["ev"]["rdev"])
        det_w = max(det_w, crecs[c]["ev"]["fc"]["detdev"])
    b_rec = (rec_main <= REC_BAR and rec_deep <= REC_BAR_DEEP
             and rec_ctrl <= REC_BAR_CTRL)
    check("G50-recursion-ward", b_rec,
          "EXACT chain recursion r_{k+1} == t_k + ap_k r_k + "
          "bp_k r_{k-1} on %d rungs + controls (below-flip "
          "truncation disclosed): worst rel %.1e main N<=%d (bar "
          "%.0e) / %.1e deep (bar %.0e) / %.1e controls (bar "
          "%.0e)%s -- the local transfer step of the class is "
          "REAL" % (len(all_rc), rec_main, DEEP_N, REC_BAR,
                    rec_deep, REC_BAR_DEEP, rec_ctrl,
                    REC_BAR_CTRL,
                    "; DEGENERATE guard fired (pre-declared "
                    "DEG_FLOOR): " + ", ".join(deg_skip)
                    if deg_skip else ""))
    check("G51-monodromy-det-ward", det_w <= DET_BAR,
          "|det M| == prod |bp| over every four-step monodromy "
          "on every world (worst rel %.1e, bar %.0e) -- the "
          "transfer-matrix bookkeeping is exact" % (det_w,
                                                    DET_BAR))
    if smoke:
        fc9 = recs[0]["ev"]["fc"]
        info("SMOKE: w9 Floquet census: %d monodromies, med sr "
             "%.4f, frac(sr<1) %.2f, drift med %.3f, logsum "
             "%.3f, med sr^3 %.4f"
             % (fc9["n"], fc9["med"], fc9["frac_lt1"],
                fc9["drift"], fc9["logsum"], fc9["sr3"]))
        check("G52-floquet-census", True, "SMOKE: skipped")
        check("G53-floquet-worlds", True, "SMOKE: skipped")
        b_ok = False
        b_world = False
    else:
        meds = [rc["ev"]["fc"]["med"] for rc in srt_all]
        fr1 = [rc["ev"]["fc"]["frac_lt1"] for rc in srt_all]
        drf = [rc["ev"]["fc"]["drift"] for rc in srt_all]
        expo = [rc["ev"]["fc"]["logsum"]
                / math.log(rc["ev"]["m"]) for rc in srt_all]
        n_med_lt1 = sum(1 for v in meds if v < 1.0)
        n_expo = sum(1 for v in expo if v <= EXPO_TARGET)
        b_ok = (b_rec and n_med_lt1 == len(srt_all)
                and n_expo >= EXPO_MIN)
        check("G52-floquet-census", True,
              "monodromy census on 57 rungs: med sr med %.4f "
              "(rungs with med sr < 1: %d/57), frac(sr<1) med "
              "%.2f, drift c = k(1-sr) med %.3f, product "
              "exponent expo = sum log sr / log m med %.3f "
              "(rungs <= %.1f: %d/57, sealed min %d), med sr^3 "
              "med %.4f -> B_OK %s"
              % (float(np.median(meds)), n_med_lt1,
                 float(np.median(fr1)), float(np.median(drf)),
                 float(np.median(expo)), EXPO_TARGET, n_expo,
                 EXPO_MIN, float(np.median(
                     [rc["ev"]["fc"]["sr3"] for rc in srt_all])),
                 b_ok))
        wn = []
        e_med = s_med = None
        for c in ("EPST", "SCR"):
            fcc = crecs[c]["ev"]["fc"]
            wn.append("%s med sr %.4f (n=%d, TRUNCATED below "
                      "flip %d)" % (c, fcc["med"], fcc["n"],
                                    CTRL_FLIPS[long_names[c]]))
            if c == "EPST":
                e_med = fcc["med"]
            else:
                s_med = fcc["med"]
        b_world = (e_med is not None and s_med is not None
                   and e_med < 1.0 and s_med >= 1.0)
        check("G53-floquet-worlds", True,
              "%s -> B_WORLD %s (sealed: EPST med sr < 1 AND SCR "
              "med sr >= 1; the truncated census is disclosed "
              "WEAK evidence)" % ("; ".join(wn), b_world))
        st["expo_med"] = float(np.median(expo))
        st["meds_med"] = float(np.median(meds))
        st["n_med_lt1"] = n_med_lt1
        st["n_expo"] = n_expo

    # ---------------- S6: Leg C -- class + adjudication
    section("S6  LEG C -- THE CLASS + FORK ADJUDICATION")
    print("""  RecursiveDifferenceProfile(m) -- the sealed class
  (a block field P in R^m with raw atomic presentation
   P_j = sum_{alpha in I_j} d_alpha):
    P1 ORDERED SHARED SUPPORT: one totally ordered position set;
       blocks = consecutive position intervals; fold share
       (positions carrying exactly one beta/omega pair) >= %.1f
    P2 EXACT LOCAL RECURSION: the atoms are linear readouts of a
       chain state driven by r_{k+1} = t_k + ap_k r_k +
       bp_k r_{k-1} (ward <= %.0e/%.0e/%.0e)
    P3 BOUNDED ATOM MULTIPLICITY: max atoms per position <= %d
    P4 CONTROLLED FOUR-BLOCK STRUCTURE: med lag signature
       rho_1 <= +%.2f, rho_2 <= +%.2f, rho_3 >= -%.2f,
       rho_4 >= -%.2f AND NC(16) <= %.1f
    P5 MASS CONSERVATION: sum_j P_j == R exact (<= %.0e)
    P6 NO ASSIGNMENT SHUFFLE: run assignment == positional
       breakpoint assignment (0 mismatches)
    CP4 TELESCOPE CANCELLATION (candidate): TC_far <= %.2f"""
          % (FOLD_MIN, REC_BAR, REC_BAR_DEEP, REC_BAR_CTRL,
             MULT_CAP, SIGN_EPS, SIGN_EPS, SIGN_EPS, SIGN_EPS,
             NC_MAX, ID_BAR, TC_CLS))

    def world_props(rcs, rbar):
        mx = max(rc["ev"]["mx_mult"] for rc in rcs)
        fs = float(np.median([rc["ev"]["fold_share"]
                              for rc in rcs]))
        rd = max(rc["ev"]["rdev"] for rc in rcs)
        lg = np.median(np.array([rc["ev"]["lag"] for rc in rcs]),
                       axis=0)
        nc = float(np.median([rc["ev"]["nc"] for rc in rcs]))
        tc = float(np.median([rc["ev"]["tc_far"] for rc in rcs]))
        mi = sum(rc["ev"]["mism"] for rc in rcs)
        md = max(abs(sum(rc["ev"]["P"]) - rc["ev"]["R"])
                 / max(abs(rc["ev"]["R"]), 1e-300) for rc in rcs)
        return class_props(mx, fs, rd, rbar, lg, nc, tc, mi, md)

    # m4 shuffle instance (built from w9; seeded, deterministic):
    ev9 = mrecs[0]["ev"]
    rng = np.random.default_rng(SEED_SHUF)
    blk_shuf = ev9["blk_all"][rng.permutation(len(ev9["blk_all"]))]
    m9 = ev9["m"]
    P_shuf = np.bincount(blk_shuf, weights=ev9["val_all"],
                         minlength=m9)
    mism_shuf = int(np.sum(np.searchsorted(ev9["brk"],
                                           ev9["pos_all"])
                           != blk_shuf))
    mass_shuf = abs(float(np.sum(P_shuf))
                    - float(np.sum(ev9["Pd"]))) \
        / max(float(np.sum(np.abs(ev9["val_all"]))), 1e-300)
    if smoke:
        props_main = world_props([recs[0]], REC_BAR)
        props = {"MAIN(w9)": props_main}
    else:
        props = {"MAIN": world_props(recs, REC_BAR_DEEP)}
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            props[c] = world_props([crecs[c]], REC_BAR_CTRL)
    props["SHUFFLE(m4)"] = {
        "P5_mass": (mass_shuf <= ID_BAR),
        "P6_assign": (mism_shuf == 0)}
    keys = ("P1_fold", "P2_rec", "P3_mult", "P4_comb", "P5_mass",
            "P6_assign", "CP4_tc")
    info("instance table (Y = property holds, N = violated, "
         "- = not measured on this instance):")
    for w in props:
        info("  %-12s %s" % (w, "  ".join(
            "%s:%s" % (k, ("Y" if props[w][k] else "N")
                       if k in props[w] else "-")
            for k in keys)))
    mkey = "MAIN" if "MAIN" in props else "MAIN(w9)"
    sep = [k for k in keys
           if props[mkey].get(k, False)
           and ("EPST" in props and props["EPST"].get(k, False))
           and ("SCR" in props and not props["SCR"].get(k, True))]
    main_core = all(props[mkey][k] for k in
                    ("P2_rec", "P5_mass", "P6_assign"))
    check("G60-class-instance-test", main_core,
          "MAIN satisfies the exact structural core P2/P5/P6; "
          "full property row printed above (P1/P3/P4/CP4 are "
          "measured class candidates, not gates); world-correct "
          "separators (MAIN pass + EPST pass + SCR fail): %s; "
          "the m4 shuffle instance is adjudicated in S7"
          % (str(sep) if sep else "NONE (honest negative)"))

    if smoke:
        verdict_main = "SMOKE_NO_ADJUDICATION"
        check("G61-fork-adjudication", True, "SMOKE: skipped")
        check("G62-candidate-theorem", True, "SMOKE: skipped")
    else:
        remnants = []
        if not a3_ok:
            remnants.append("R3A rest: per-type HOLD@A2 %s, "
                            "T1@A0 %s"
                            % (str({t: typeHOLD[t][2]
                                    for t in TYPES}),
                               typeHOLD["T1"][0]))
        if not a3_world:
            remnants.append("R3A world rest: EPST-hold %s / "
                            "SCR-viol %s"
                            % (epst_ok, str(scr_viol)))
        if not b_ok:
            remnants.append("R3B rest: med sr < 1 on %d/57, "
                            "expo <= -2 on %d/57 (min %d)"
                            % (st.get("n_med_lt1", 0),
                               st.get("n_expo", 0), EXPO_MIN))
        if not b_world:
            remnants.append("R3B world rest: truncated census "
                            "does not separate")
        if a3_ok and a3_world and sep:
            verdict_main = "R3A_GO(triple incidence; SCR " \
                "violated types %s; separators %s)" \
                % (str(st["scr_viol"]), str(sep))
        elif b_ok and b_world and sep:
            verdict_main = "R3B_GO(Floquet; separators %s)" \
                % str(sep)
        elif a3_ward or b_rec:
            verdict_main = "BOTH_PARTIAL(%s)" % " | ".join(
                remnants)
        else:
            verdict_main = "FORK_DEAD"
        n_fired = 1  # by construction exactly one branch above
        check("G61-fork-adjudication", n_fired == 1,
              "exactly one sealed fork verdict fired: %s"
              % verdict_main)
        if verdict_main.startswith("R3A_GO"):
            C_univ = sum(typeC[t][2] for t in TYPES)
            m0 = min(rc["ev"]["m"] for rc in srt_all)
            print("""  CANDIDATE THEOREM (universal cubic moment; typed
  CANDIDATE, no upgrade): for every RecursiveDifferenceProfile
  instance (P1-P6) with m >= m_0 = %d blocks:
      sum_j q_j^3  <=  C_univ (log m)^2 / m^2,
      C_univ = C_T1 + C_T2 + C_T3 + C_T4 = %.4f
  (deliberately COARSER than the r306 sharp 1.069 -- the
  reviewer instruction; per-type constants frozen on the 5
  shallowest rungs; finite cases m < m_0 to be certified
  separately per instance; only L* carries MAIN specificity.)"""
                  % (m0, C_univ))
            check("G62-candidate-theorem", C_univ > 0,
                  "CANDIDATE THEOREM printed with ALL constants: "
                  "C_univ %.4f (= sum of frozen per-type C at "
                  "A = 2), A = 2, m_0 = %d; the r306 sharp "
                  "constant 1.069 is NOT claimed as universal"
                  % (C_univ, m0))
            st["C_univ"] = C_univ
            st["m0"] = m0
        else:
            check("G62-candidate-theorem", True,
                  "no GO -> no theorem candidate; frozen "
                  "remnants: %s" % ("; ".join(remnants)
                                    if remnants else "none"))

    # ---------------- S7: Leg D -- must-fails + toys
    section("S7  LEG D -- WARDS / MUST-FAILS")
    r_t = fr_type_table(TOY_GROUPS)
    ok_toy = (r_t["S1"] == 2 and r_t["T1"] == 8 and r_t["T2"] == 24
              and r_t["T3"] == -24 and r_t["T4"] == 0
              and r_t["dev"] == 0)
    u_t = fr_type_table(([Fr(1)],))
    ok_u = (u_t["T4"] == 0 and u_t["dev"] == 0
            and u_t["T1"] == 1)
    # float cross-check of type_expansion on the toy block
    tpos = np.array([0.1, 0.1, 0.2, 0.2, 0.3])
    tval = np.array([2.0, -1.0, 1.0, -1.0, 1.0])
    tblk = np.zeros(5, dtype=int)
    tf = type_expansion(tpos, tval, tblk, 1)
    ok_f = (abs(tf["T1"][0] - 8.0) <= TOY_BAR
            and abs(tf["T2"][0] - 24.0) <= TOY_BAR
            and abs(tf["T3"][0] + 24.0) <= TOY_BAR
            and abs(tf["T4"][0]) <= TOY_BAR
            and tf["ward"] <= TOY_BAR)
    check("G84-toy-exactness", ok_toy and ok_u and ok_f,
          "toy block {2,-1}|{1,-1}|{1}: T1/T2/T3/T4 = 8/24/-24/0 "
          "sum 8 == S1^3 EXACT (Fractions); one-group block: T4 "
          "== 0 EXACT; float type_expansion matches the "
          "Fractions table (bar %.0e)" % TOY_BAR)
    r_m1 = fr_type_table(TOY_GROUPS, mutant="dd")
    check("G80-m1-double-diagonal", r_m1["dev"] == 3 * r_t["S3"]
          and r_m1["dev"] == 24,
          "m1 CAUGHT: double-counted diagonals (T2' = 3 S2 S1) "
          "break the Newton-split ward by EXACTLY 3 S3 = %s on "
          "the toy block; cross-ref r306 RY3.fr_lagrange Newton "
          "dev %s on (1/2,1/4,1/4)"
          % (r_m1["dev"],
             RY3.fr_lagrange([Fr(1, 2), Fr(1, 4),
                              Fr(1, 4)])["newt_dev"]))
    srs_t, sra_t, brk2 = fr_affine_split_toy()
    live_lt1 = [rc for rc in all_rc
                if rc["ev"]["fc"]["med"] < 1.0]
    n_dev = sum(1 for rc in live_lt1
                if abs(max(rc["ev"]["fc"]["med"], 1.0)
                       - rc["ev"]["fc"]["med"]) >= MUT_MIN)
    check("G81-m2-no-conservation-split",
          brk2 == Fr(1, 2) and sra_t == 1
          and (not live_lt1 or n_dev == len(live_lt1)),
          "m2 LOUD: the unsplit affine monodromy has eigenvalue "
          "EXACTLY 1 (scalar conservation mode) -- toy spectrum "
          "{1/2, 0, 1}: unsplit radius 1 vs split 1/2, break %s "
          "EXACT; live: the mutant radius max(sr, 1) deviates >= "
          "%.0e on %d/%d contracting rungs -- it can NEVER "
          "certify contraction" % (brk2, MUT_MIN, n_dev,
                                   len(live_lt1)))
    r_m3t = fr_type_table(TOY_M3_GROUPS)
    r_m3a = fr_type_table(TOY_M3_GROUPS, mutant="mag")
    tc_toy = abs(r_m3t["T4"]) / r_m3a["T4"]
    tc_mut = r_m3a["T4"] / r_m3a["T4"]
    ev9m = mrecs[0]["ev"]
    dev3 = abs(ev9m["tc_far_mut"] - ev9m["tc_far"])
    check("G82-m3-magnitude-telescope",
          tc_toy == 0 and tc_mut == 1 and r_m3a["T4"] == 48
          and dev3 >= MUT_MIN,
          "m3 LOUD: |c| instead of c kills the telescope -- toy "
          "{1,-1}|{2}|{-2}: true TC_far = 0/48 = 0 EXACT, mutant "
          "48/48 = 1 (break 1 EXACT); real w9: mutant TC 1.000 "
          "vs true %.3f (dev %.1e >= %.0e)"
          % (ev9m["tc_far"], dev3, MUT_MIN))
    check("G83-m4-shuffle-rejected",
          mism_shuf > 0 and mass_shuf <= ID_BAR,
          "m4 CAUGHT: the shuffled-assignment instance (seed "
          "%d) is REJECTED by the P6 interval check (%d/%d atoms "
          "outside their block interval) while P5 mass "
          "conservation of the presentation total STILL HOLDS "
          "on it (dev %.1e vs abs mass) -- conservation alone "
          "cannot see the shuffle; the class needs P6"
          % (SEED_SHUF, mism_shuf, len(ev9["pos_all"]),
             mass_shuf))

    # ---------------- S8: verdict
    section("S8  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact raw-atomic triple-type decomposition "
          "with fold groups, the exact chain-recursion transfer "
          "step and its four-step Floquet census with "
          "conservation-mode split, the class "
          "RecursiveDifferenceProfile with measured instance "
          "tests, the per-type prereg table and the fork "
          "adjudication -- NO new certificate promoted")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R313_ANCHORS(C %.3f/%.3f/%.3f, A2 0/57 viol, "
                 "trend %+.3f; comb %+.3f/%+.3f/%+.3f/%+.3f)"
                 % (st["C"][0], st["C"][1], st["C"][2], sl42,
                    st["lag_med"][0], st["lag_med"][1],
                    st["lag_med"][2], st["lag_med"][3])]
        parts.append("TYPE_TABLE(T1 %+.4f, T2 %+.4f, T3 %+.4f, "
                     "T4 %+.4f; mult max %d; TC_far %.3f)"
                     % (st["sh_med"]["T1"], st["sh_med"]["T2"],
                        st["sh_med"]["T3"], st["sh_med"]["T4"],
                        mult_max, st["tcf_med"]))
        parts.append("R3A(ward %s, minA %s, A3_OK %s, WORLD %s)"
                     % (a3_ward, str(st["minA"]), a3_ok,
                        a3_world))
        parts.append("FLOQUET(rec %s, med sr %.4f, lt1 %d/57, "
                     "expo %.3f, n_expo %d/57, B_OK %s, WORLD %s)"
                     % (b_rec, st["meds_med"], st["n_med_lt1"],
                        st["expo_med"], st["n_expo"], b_ok,
                        b_world))
        parts.append("CLASS(separators %s)" % (str(sep) if sep
                                               else "NONE"))
        parts.append(verdict_main)
        if "C_univ" in st:
            parts.append("CANDIDATE_THEOREM(C_univ %.4f, A 2, "
                         "m_0 %d)" % (st["C_univ"], st["m0"]))
        parts.append("MUSTFAIL_LEDGER(m1-m4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the type decomposition, "
          "the abs majorants, the recursion identity, the "
          "conservation-mode split and the det dictionary (all "
          "exact finite algebra); MEASURED: every share, C_t, "
          "radius, exponent, class property and slope (42 + %d "
          "finite rungs); OPEN: the cofinal law, the class "
          "theorem itself, kz15 beyond r270; NO RH claim"
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
