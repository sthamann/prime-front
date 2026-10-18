#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""group_mass_cap_probe -- PRIME.L2.RENYI3.GROUP_MASS_CAP.01
(round 327): THE FOLD-GROUP MASS CAP -- the r324 follow-up question
on the terminal main lane.

CONTEXT (binding, from the sealed r324 record): the composition to
terminal_positive_main stands as MEASURED (PILEUP_GROWS_SUBCRITICAL,
e_tot +0.172 < CRIT 0.224, m_0* = 10^59.6 astronomical, the gap
(274, 10^59.6) the disclosed extrapolation hypothesis).  The
mechanism is HALF understood: the scale count O(log m) is pointwise
CERTIFIED (C_NSC 2.026, 0/39) but the per-scale mass O(1/m) is
REFUTED (11/39) -- the near-critical windows are a SINGLE heavy
source scale at the argmax block (kz53: s0 carries 13.78 of
G 13.02), not multiscale convergence.  The r324-named follow-up:
WHAT CAPS THE MASS OF THE DOMINANT FOLD GROUP?  The fold
multiplicity <= 2 holds uniformly (69/69, the r313/r314 banked
asset) -- the cap must come from the PER-GROUP MASS BALANCE.  A
theorem of the form  m x (mass of the heaviest group)/L <= C_G x
(log m)^A  would, via the certified scale-count bound and the exact
chain m q_max <= nsc x pil (slack 0.0, r324), deliver the direct
q_max bound and possibly push the +0.172 exponent to polylog -- or
explain its unavoidability.

THE THREE QUESTIONS (sealed):
Q1 -- ANATOMY OF THE HEAVY GROUP: what IS the dominant fold group
   at the spikes structurally?  Its two ancestors (mult 2: one
   bulk atom +ct and/or one window atom -cw at one position),
   their values and internal alignment |sum|/(sum| |), its
   position inside the block (the r322 mid/tail thirds), its gap
   to the second-heaviest group (census over the ladder), and the
   SOURCE-vs-AGGREGATION adjudication: is the r324 heavy SCALE
   carried by ONE group (source: two large source masses meet --
   then the cap is a statement about source-pair coincidences) or
   by MANY groups that the fold bundles (aggregation)?  Sealed
   rule: ANATOMY = SOURCE iff the med over the three named
   near-critical rungs of ratio = hga/(max scale mass of the
   argmax block) >= RATIO_BAR = 0.5, else AGGREGATION.
Q2 -- THE CAP CANDIDATES (source-pure, all mid-ladder frozen, TRB
   split verbatim, test pointwise, named coverage printed):
   (i) THE TWO-ANCESTOR / LAMBDA-PAIR ROUTE: per group EXACTLY
       gabs_g <= mult_g x gmax_g <= MULT_CAP x vmax (vmax = the
       maximal atom magnitude; block-local vmaxb and window-global
       vmaxw both gated) -- the von-Mangoldt size analogy: the
       maximal source-pair sum on one fold target is ~ 2 x (the
       largest atom).  The cap question reduces EXACTLY to: is
       lvb = MULT_CAP x m x vmaxb/L <= C_LV x log m pointwise?
       (the elegant exit: the cap is the source-size bound
       itself);
   (ii) THE DIRECT GROUP-MASS BALANCE: hgn = m x hga/L (hga = abs
       atom mass of the heaviest group of the argmax block) with
       the minimal-A protocol (A in {1, 2}, r313 convention): the
       L-normalization is the known difficulty (sl_L1 +0.196,
       r297) -- the balance identity sum_g gabs (block) == A1_j
       (exact partition, warded) plus the group recomposition
       sum_j |sum_g G1_g| == L1 (exact, warded) make a heavy
       group force light mass elsewhere;
   (iii) THE GROUP COUNT: ngl = n_groups(argmax block)/log m <=
       C_NG (the pigeonhole partner: the exact chain
       m q_max <= m A1_{j*}/L = sum_g m gabs_g/L <= ng x hgn
       is EXACT algebra, warded live -- with (ii) or (i) it
       composes to m q_max <= C_NG C_cap (log m)^{1+A}).
Q3 -- THE COMPOSITION: if a cap candidate certifies pointwise
   (mid-ladder freeze, ALL spikes inside): recompose -- does it
   replace the +0.172 exponent by polylog, and what becomes of
   m_0*?  (a non-astronomical m_0 would be the jump from MEASURED
   to a realistically checkable theorem candidate.)  If NO cap
   certifies: the growth exponents e_hg + e_ng + e_M2 vs CRIT =
   0.224 decide HEAVY_GROUP_UNBOUNDED vs CAP_PARTIAL -- then
   +0.172 is presumably unavoidable and the MEASURED composition
   is the honest end state of the route (sealed honestly).

SEALED VERDICTS (exactly one fires; total order):
   TARGET_LEAK              iff any purity/scope audit hit on the
       mechanism builders,
   RECOMP_BREAK             iff the group ledger breaks
       structurally (partition/recomposition/two-ancestor ward
       fails on a live world),
   LAMBDA_PAIR_CAP_GO(A=1)  iff the lambda-pair chain certifies
       pointwise: two-ancestor ward exact live AND lvb/log m 0
       test violations at the mid-ladder freeze AND named 4/4 AND
       the group count certifies (ngl 0 violations + named 4/4),
   BALANCE_CAP_GO(A)        iff not lambda-pair but the direct
       heavy-group cap certifies at minimal A in {1, 2} (0
       violations + named 4/4) AND the group count certifies,
   HEAVY_GROUP_UNBOUNDED    iff no GO and the decided route
       exponent e_route = e(hgn/log m) + e(ngl) + e(m M_2) >=
       CRIT = 0.224 (both test halves agree),
   CAP_PARTIAL(rest)        otherwise (named rest printed).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the r326 Lean round runs in parallel; this probe
touches NOTHING outside its own file and the strictly additive
rh-sync (existing entries byte-identical).

THE OBJECT (r269/r287/r298/r302/r306/r314/r316/r324 machinery +
the r324 module imported verbatim): t_{N-2} = sum_b ct_b (r244
chain rows, r266 eval); F = 0.20 edge split; maximal same-sign
runs of the bx-sorted bulk; level-2 blocks (r270 convention); the
frozen positional block machinery (r298); the r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze; the r314
SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope;
the r316 TRB.two_regime_state + TRB.split_midladder; the r324
QMO.scale_bins + QMO.pileup_state + QMO.mult_ward; the r324-pre
FAP.m2_qmax_state; PDelta = Pbeta - Pomega; x_j = (PDelta)_j.
NEW in this round (module-own, source-pure): group_mass_ledger
(the per-group abs-mass/max-atom/source-flag ledger on the
identical fold segmentation), heavy_state (the argmax-block
heavy-group anatomy + the cap coordinates) and the sealed
cap_tree.

LEG 0 -- ANCHOR REGRESSION (slim set + the r324 record,
disclosed): the r314 identity wards live; r306 C_2 = 1.069 (tol
0.005) first-5 freeze, 0/57; r316 rho anchors kz53/kz67/kz55/
kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005) + C_small 1.0694
at kz18 + n = 65; r324 RECORD anchors reproduced bit-near:
C_NSC 2.0258 (tol 0.005) with 0/39 test violations, C_PIL 9.3583
(tol 0.005) with 11/39, C_INF 1.7481 (tol 0.005) with 5/39, the
named heavy-scale masses {kz53: 13.778, kz83: 12.707, kz67:
22.378} (tol 0.02, == pil at the named rungs), exponents
e(G/log m) +0.158 / e(m M_2) +0.014 / e_tot +0.172 (tol 0.005);
r324-pre C_M2 = 2.2557 (tol 0.005) with the seven-violator set
{53, 67, 83, 76, 61, 28, 109} EXACT.

LEG A -- SEAL + PURITY + TOYS + LIVE WARDS: (A1) sealed
definitions printed; the SOURCE-PURE table (rank, kz, N, m, G =
m qmax, ng, hgn, hgn/log m, lvb/log m, gap, align, ratio, third,
nwin) printed BEFORE any certification table.  (A2) SOURCE-PURITY
AUDITS: the AST identifier scan over group_mass_ledger +
heavy_state + cap_tree must be clean against BOUND_FORBIDDEN +
PHI3_FORBIDDEN + QMAX_FORBIDDEN (no M_3 read-back, no terminal
value, no q_max record read-back -- the cap builders consume atom
values / positions / block assignments / group order ONLY; the
block-value argmax is the same access class as the r324
pileup_state, disclosed); the literal scan over the builders must
be clean against the sealed record-literal set
R327_TABLE_LITERALS (the r314..r324-pre set UNION the r324 record
numbers); e3/e4 prove the audits bite.  (A3) TOY EXACTNESS
(Fractions): the group toy (block j*: group A = atoms (3, 2) at
one position (mult 2, G1 = 5 = gabs), group B = atom (1); block
1: atom (1)): x = (6, 1), L = 7, m = 2, m qmax = 12/7; hga = 5,
hgn = 10/7, ng = 2, chain m qmax = 12/7 <= ng x hgn = 20/7
(slack 8/7 EXACT); vmaxb = 3, two-ancestor 5 <= 2 x 3 (slack 1
EXACT); partition 5 + 1 == A1 = 6 EXACT; the aligned/cancelling
group toy (3, -2): G1 = 1, gabs = 5, align = 1/5 EXACT; the
drop-group mutant breaks the L1 recomposition by EXACTLY 1
(LOUD); the wrong-window-max mutant bound 2 x 2 = 4 < hga 5
breaks the two-ancestor ward by EXACTLY 1 (CAUGHT); the cap_tree
on all six branches EXACT.  (A4) LIVE WARDS on every live world:
the r316 chain + NORM x cube == rho_2 (r324 verbatim); the S0
interpolation M_3 <= qmax M_2 AND M_2 <= qmax; THE GROUP LEDGER
WARDS: ledger G1/mult/ng == the r314 genealogy EXACTLY; the
partition sum_g gabs == A1_j (bar SA_BAR); the L1 recomposition
sum_j |sum_g G1_g| == L (bar SA_BAR); the two-ancestor bound
gabs_g <= MULT_CAP x gmax_g on every group (exact, bar TOY_BAR
relative); THE CAP CHAIN m qmax <= ng x hgn AND hgn <= lvb
(exact algebra, bar CHAIN_BAR); the r324 pileup chain m qmax <=
nsc x pil re-warded.

LEG B -- Q1 ANATOMY (census + sealed adjudication): the heavy-
group profile at the three named near-critical rungs (ancestor
values, alignment, bulk/window composition, position third, gap
to the second group, ratio to the r324 heavy scale mass); ladder
censuses gap med/max, align med, third histogram, nwin histogram;
the sealed SOURCE/AGGREGATION letter (RATIO_BAR).

LEG C -- Q2 CAPS (mid-ladder freeze, TRB verbatim; small ranks
individually certified): (i) C_LV = max cal lvb/log m, test
violations, named coverage; the window-global lvw census printed
alongside (disclosed: the block-local vmaxb is the sharper exact
form; the window-global bound is gated as census); (ii) C_HG1 =
max cal hgn/log m and C_HG2 = max cal hgn/(log m)^2, minimal-A
protocol, violations, named; (iii) C_NG = max cal ngl, test
violations, named; growth exponents (r272 dyadic halves-slope
over the test rungs, fit-free): e_hg = e(hgn/log m), e_lv =
e(lvb/log m), e_ng = e(ngl), e_M2 = e(m M_2), e_route = e_hg +
e_ng + e_M2 vs CRIT = 0.224, stability = the two test halves
must agree on the criticality side (else undecided ->
CAP_PARTIAL).

LEG D -- Q3 COMPOSITION (printed ALWAYS, honestly typed): on a
GO branch: m qmax <= C_NG x C_cap x (log m)^{1+A} => sum q^3 <=
C_NG C_cap C_2env (log m)^{1+A}/m^2 (C_2env = the measured m M_2
envelope, typed MEASURED) => N_3 >= m/sqrt(C (log m)^{1+A}) and
N_2 >= N_3 (r306 exact chain) => N_2 >= m^0.888 for all m >=
m_0* = the smallest m with m^{0.224} >= C (log m)^{1+A}
(log-space solve, r324 verbatim) -- the NEW m_0* printed against
the r324 record 10^59.6; on the no-GO branch: the r324 MEASURED
composition restated unchanged (the cap route does not improve
it) with the measured cap-route envelopes printed.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) GROUP RECOMPOSITION != L1: mutant_group_drop drops the last
  group of the argmax block -- the L1 recomposition breaks by
  exactly the dropped |G1| (toy break == 1 EXACT; live rel dev >=
  MUT_MIN) -- LOUD.
(e2) LAMBDA-PAIR BOUND WITH THE WRONG WINDOW MAXIMUM:
  mutant_wrong_window_max computes the source maximum on a
  truncated atom set (the global maximal atom dropped) -- on the
  sealed toy the mutant cap 2 x 2 = 4 < hga = 5 breaks the
  two-ancestor ward by EXACTLY 1 while the true cap holds
  (slack 1) -- CAUGHT (exact).
(e3) CAP CONSTANT AFTER SIGHT OF THE SPIKES: mutant_cap_posthoc
  re-picks the cap constant to cover the seen violators (consumes
  rho) -- the BOUND_FORBIDDEN scope audit must FLAG it AND on the
  sealed toy it returns a constant != the mid-ladder rule's --
  CAUGHT twice.
(e4) QMAX READ-BACK: mutant_qmax_readback consumes the q_max
  record (trs/qmax) as a 'cap coordinate' -- the QMAX_FORBIDDEN
  scan must FLAG it (AST-CAUGHT) while the module-own builders
  stay clean.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.

INDEX FIREWALL (binding, r238-r324 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target M_3 / rho_2 and the q_max RECORD enter
GATES / anchors / composition checks only, NEVER a cap builder
(AST-warded); no zero/prime oracles anywhere (AST firewall); no
fit primitives (fragment audit; the growth exponents are the
imported r272 dyadic halves-slope, fit-free).  MACHINERY IMPORTED
VERBATIM: r324 QMO.scale_bins + QMO.pileup_state + QMO.mult_ward,
r324-pre FAP.m2_qmax_state, r316 TRB.two_regime_state +
TRB.split_midladder, r314 SCF.fold_genealogy +
SCF.signed_cube_terms + SCF.flux_telescope, r306
RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze, r298
WBT.block_breaks + WBT.aggregate_blocks, r269 PBB.mask_edge +
PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed, r316/r324 verbatim): frame-A h <= 900, 42 rungs,
(N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39, 52};
EXTENSION: 900 < h <= 1300, first 15 by (N, kz); EXT2: the r316
A5 rule (leftover pool + first 12 windows 1300 < h <= 1650,
first 8 POSITIVE_PREFIX by (N, kz)).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; SA_BAR 1e-12;
DEG_FLOOR 1e-6; MULT_CAP 2; N_CAL 5 (via TRB, verbatim);
RATIO_BAR 0.5; A_FAM (1, 2); CRIT_EXP 0.224; N2_EXP_NEED 0.888;
NEED_SLOPE 0.908; SIGMA_STAR -0.516; DELTA_NEED 0.21; NAMED_KZ
(53, 83, 67, 55); NAMED_HV_KZ (53, 83, 67); MUT_MIN 1e-6;
TOY_BAR 1e-12; FR_BAR 1e-14; TB_WARD bars 1e-9 main N <= 400 /
3e-6 deep + ext + ext2 / 1e-6 controls; ID_BAR 1e-12; AC_BAR
1e-9; R306 anchor C_2 1.069 tol 0.005; N327_REF 65; R316 RHO
{53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790} tol 0.005,
C_SMALL 1.0694 tol 0.005 at kz18; R324 anchors C_NSC 2.0258 /
C_PIL 9.3583 / C_INF 1.7481 (tol 0.005) with violation counts
0/11/5 EXACT, named heavy-scale masses {53: 13.778, 83: 12.707,
67: 22.378} tol 0.02, exponents +0.158/+0.014/+0.172 tol 0.005;
R324P C_M2 2.2557 tol 0.005, violator set {53, 67, 83, 76, 61,
28, 109} EXACT; R327_TABLE_LITERALS = the sealed r314..r324-pre
forbidden set (r324 verbatim) UNION the r324 record set {2.0258,
9.3583, 1.7481, 0.158, 0.014, 0.172, 0.141, -0.16, 13.778,
22.378, 12.707, 25.309, 14.15, 2.724, 2.8, 1.971, 2.103, 2.567,
8.941, 59.6, 6.661, 1.165, 2.026, 1.137, 3.1938, 2.613, 0.71,
1.1, 5.32};
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the ledger/chain/two-ancestor wards on w9 + controls +
e1-e4 mutants; ladder, extensions, anchors, anatomy census, cap
certification, exponents and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r324/r324-pre RECORD number adopted
as-is (incl. the known r324 heavy-scale anatomy at the named
rungs -- that the heavy SCALE is near the block total is known;
whether ONE GROUP carries it is genuinely open); the two-ancestor
bound gabs <= mult x gmax <= MULT_CAP x vmax, the partition
identity, the L1 recomposition and the cap chain m qmax <= ng x
hgn are derived algebra, disclosed above; GENUINELY OPEN
quantities of this round: every heavy-group column (hga, hgn,
gap, align, third, nwin, ratio), all cap constants C_LV/C_HG/
C_NG, all violation counts, all four growth exponents, the
anatomy letter and the recomposed m_0* -- NONE was computed
before this spec was frozen; RATIO_BAR = 0.5, A_FAM = (1, 2) and
CRIT_EXP = 0.224 are a-priori (the criticality budget is the
r324 budget verbatim); the six sealed letters are symmetric and
total -- the tree maps every outcome to exactly one letter by
CONTRACT.

RECORD TABLES (inserted AFTER the record run -- the only
amendment after freeze; freeze SPEC_SHA 71f8b7b423a3f847;
protocol: smoke pass 1 = 34/34 (0.4 s), NO amendment;
calibration pass 1 = first full evaluation, 34/34, wall 36.4 s,
NO amendment; record run1/run2 after this insertion, identical
up to the runtime line):
MAIN VERDICT: CAP_PARTIAL(lambda-pair 19 viol; direct cap fails
at A <= 2 (8/39); exponent halves straddle +0.411/-1.183;
e_route +0.106 < CRIT 0.224 UNDECIDED) -- no cap candidate
certifies pointwise at the mid-ladder freeze; the r324 MEASURED
composition (m_0* = 10^59.6) stays the honest state of the
route.
Q1 ANATOMY: SOURCE (sealed rule, med named ratio 1.057 >=
RATIO_BAR 0.5; kz53 1.081 / kz83 1.057 / kz67 0.460) -- the
r324 single heavy scale IS a single fold group at the two
sharpest spikes; the STRUCTURAL FINDING of the round: on ALL 65
rungs the heaviest group of the argmax block is EXACTLY ONE
beta/omega fold pair (window-atom histogram [0, 65, 0]: one
bulk atom + one window atom at one position) with median
alignment 1.000 (min 0.099 -- NO internal cancellation at the
median: the two ancestors REINFORCE); kz53: the single pair
carries bshare 0.888 of the argmax block's atom mass at gap
0.076 (the second group is 13x lighter) -- the spike is
literally ONE bulk/window coincidence; kz67 is the exception
shape (6 groups, bshare 0.416, ratio 0.460); position thirds
[21, 29, 15] (mid-heavy, the r322 mid/tail echo); ladder gap
med 0.807 (generic rungs have near-tied top groups; the spikes
have dominant ones).
Q2 CAPS (mid-ladder freeze, TRB verbatim, 39 test rungs):
(i) lambda-pair C_LV = 1.1838: FAILS 19/39 (worst kz55 6.853,
kz53 5.766, kz83 4.609, kz67 4.132 -- named coverage 0/4): the
two-ancestor bound hga <= 2 vmaxb is EXACT (live slack 0.0) but
the SOURCE-SIZE coordinate m x vmaxb/L itself spikes -- the
von-Mangoldt size analogy does NOT close as a mid-ladder
polylog cap; (ii) direct cap A = 1 C 0.9143 FAILS 18/39, A = 2
C 0.2047 FAILS 8/39 (kz53 0.652 3.2x), minimal A = None;
(iii) THE GROUP COUNT CERTIFIES: ngl <= C_NG = 2.6351 with
0/39 violations and named 4/4 (ng med 5 max 13) -- the third
certified O(log m) count of the lane (after the r324 scale
count C_NSC 2.0258).
EXPONENTS (fit-free dyadic halves-slope over test): e(hgn/
log m) = -0.200 FALLING, e(lvb/log m) = -0.261 FALLING, e(ngl)
= +0.293, e(m M_2) = +0.014 -> e_route = +0.106 < CRIT 0.224
but halves +0.411/-1.183 STRADDLE -- UNDECIDED by the sealed
stability rule (the deep half falls steeply: the heavy-group
coordinate DECAYS with depth; the spike set is a shallow/mid
phenomenon, not growth) -- HEAVY_GROUP_UNBOUNDED does NOT fire.
Q3 COMPOSITION: no certifying cap -> the r324 chain restated
unchanged (sum q^3 <= 8.941 (log m) m^{+0.172}/m^2, N_2 >=
m^0.888 for m >= 10^59.6); measured cap-route envelope
max(ngl x hgL) = 2.616 with e_route +0.106 -- the cap route is
SUBCRITICAL in the median but pointwise-blocked by the same
named spike family as every mid-ladder constant since r316.
ANCHORS bit-near: r306 C_2 1.069 (0/57), r316 n 65 + rho
quartet + C_small 1.0694@kz18, r324 C_NSC 2.0258 (0/39) /
C_PIL 9.3583 (11/39) / C_INF 1.7481 (5/39) + named scale
masses 3/3 + e_tot +0.172, r324-pre C_M2 2.2557 + the seven-
violator set EXACT; r314 identity 4.5e-17.
SEAL: partition 3.4e-16, L1 recomposition 0.0, two-ancestor
slack 0.0, cap chain m qmax <= ng x hgn slack 0.0, ledger ==
genealogy 0.0; must-fails e1 LOUD (toy break 1 EXACT, live rel
1.3e-1) / e2 CAUGHT (toy break 1 EXACT) / e3 CAUGHT twice
(AST rho + toy 3.0 != 1.0) / e4 AST-CAUGHT (trs) + m5a/m5b
FLAGGED.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R327_ANCHORS(identity wards, r306 C_2, r316 rho + C_small + n,
    r324 C_NSC/C_PIL/C_INF + viols + named scale masses +
    exponents, r324-pre C_M2 + violator set)
+ SEAL(ledger wards + partition + L1 recomposition +
    two-ancestor + cap chain + purity audits + toys)
+ ANATOMY(the heavy-group census + the sealed SOURCE/AGGREGATION
    letter + gap/align/third/nwin statistics)
+ CAPS(C_LV/C_HG/C_NG, violations, named coverage, minimal A,
    exponents e_hg/e_lv/e_ng/e_route, stability)
+ [exactly one of] LAMBDA_PAIR_CAP_GO / BALANCE_CAP_GO /
    CAP_PARTIAL / HEAVY_GROUP_UNBOUNDED / RECOMP_BREAK /
    TARGET_LEAK
+ COMPOSITION(the recomposed chain with explicit constants +
    the new m_0* vs the r324 record; printed ALWAYS, typed)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the partition, the recomposition, the
two-ancestor bound and the cap chain are EXACT algebra; every
constant, violation count, census and exponent is MEASURED on
the finite ladder only; a certifying cap fixes a proof TARGET
and recomposes the r324 chain, it proves NO cofinal law; a
non-certifying outcome seals the honest end state of the route;
the r324 record numbers are disclosed pre-spec inputs; r243-r325
stand.

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
SA_BAR = 1e-12
DEG_FLOOR = 1e-6
MULT_CAP = 2
N_CAL = 5
RATIO_BAR = 0.5
A_FAM = (1, 2)
CRIT_EXP = 0.224
N2_EXP_NEED = 0.888
NEED_SLOPE = 0.908
SIGMA_STAR = -0.516
DELTA_NEED = 0.21
NAMED_KZ = (53, 83, 67, 55)
NAMED_HV_KZ = (53, 83, 67)
MUT_MIN = 1e-6
TOY_BAR = 1e-12
FR_BAR = 1e-14
EDGE_F = 0.20
PAIR_OFFSET = 0
R306_C2 = 1.069
R306_C2_TOL = 0.005
N327_REF = 65
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R324_CNSC = 2.0258
R324_CPIL = 9.3583
R324_CINF = 1.7481
R324_C_TOL = 0.005
R324_VNSC = 0
R324_VPIL = 11
R324_VINF = 5
R324_S0 = {53: 13.778, 83: 12.707, 67: 22.378}
R324_S0_TOL = 0.02
R324_EG = 0.158
R324_EM2 = 0.014
R324_ETOT = 0.172
R324_E_TOL = 0.005
R324P_CM2 = 2.2557
R324P_CM2_TOL = 0.005
R324P_M2VIOL = (53, 67, 83, 76, 61, 28, 109)
R327_TABLE_LITERALS = frozenset(QMO.R324B_TABLE_LITERALS | {
    2.0258, 9.3583, 1.7481, 0.158, 0.014, 0.172, 0.141, -0.16,
    13.778, 22.378, 12.707, 25.309, 14.15, 2.724, 2.8, 1.971,
    2.103, 2.567, 8.941, 59.6, 6.661, 1.165, 2.026, 1.137,
    3.1938, 2.613, 0.71, 1.1, 5.32})

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
QMAX_FORBIDDEN = {"q" + "max", "q" + "m", "tr" + "s", "mq" + "s",
                  "G" + "L_col", "G" + "_col"}


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
    lies in the sealed r314..r324 + r324 record set."""
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
                            in R327_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the cap
# ---------------- builders consume atom values / positions / block
# ---------------- assignments / source flags / group order only;
# ---------------- the withheld terminal drive key, the branch
# ---------------- label, the cubic target M_3 and the q_max RECORD
# ---------------- are forbidden (AST identifier scan + literal
# ---------------- scan).
def group_mass_ledger(pos, val, blk, src, m):
    """the per-group MASS LEDGER on the identical fold segmentation
    as the r314 genealogy (same lexsort key (block, position)):
    per fold group g returns the signed value G1_g, the abs atom
    mass gabs_g = sum |v|, the maximal atom magnitude gmax_g, the
    multiplicity mult_g, the window-atom count gwin_g (source
    flag), the block index gblk and the block slice pointers ptr;
    plus the rung-global maximal atom magnitude vmaxw.  Consumes
    atom positions + values + block assignments + source flags
    only."""
    pos = np.asarray(pos, dtype=float)
    val = np.asarray(val, dtype=float)
    blk = np.asarray(blk, dtype=int)
    src = np.asarray(src, dtype=float)
    o = np.lexsort((pos, blk))
    pb = blk[o]
    pp = pos[o]
    vv = val[o]
    ss = src[o]
    av = np.abs(vv)
    if len(pb):
        new = np.concatenate([[True], (pb[1:] != pb[:-1])
                              | (pp[1:] != pp[:-1])])
    else:
        new = np.zeros(0, dtype=bool)
    gid = np.cumsum(new) - 1
    ng = int(gid[-1]) + 1 if len(gid) else 0
    G1 = np.bincount(gid, weights=vv, minlength=ng)
    gabs = np.bincount(gid, weights=av, minlength=ng)
    gwin = np.bincount(gid, weights=ss, minlength=ng)
    mult = np.bincount(gid, minlength=ng)
    gblk = pb[new] if ng else np.zeros(0, dtype=int)
    if ng:
        starts = np.nonzero(new)[0]
        gmax = np.maximum.reduceat(av, starts)
    else:
        gmax = np.zeros(0)
    ptr = np.searchsorted(gblk, np.arange(m + 1))
    vmaxw = float(np.max(av)) if len(av) else 0.0
    return dict(G1=G1, gabs=gabs, gmax=gmax, gwin=gwin, mult=mult,
                ng=ng, gblk=gblk, ptr=ptr, vmaxw=vmaxw)


def heavy_state(x, led):
    """the ARGMAX-BLOCK heavy-group anatomy + the cap coordinates:
    on block values x (length m) and a group_mass_ledger led:
    j* = argmax |x|, L = sum |x|; over the groups of j* (position
    ordered): hga = max gabs (the heaviest group's abs atom mass),
    hgv = the same group's |G1|, hga2 = the second-heaviest gabs,
    gap = hga2/hga, align = hgv/hga, third = the position third of
    the heavy group inside the block, nwin = its window-atom
    count, npair = its multiplicity; vmaxb = max atom magnitude
    inside j*; the cap coordinates hgn = m x hga/L, lvb = MULT_CAP
    x m x vmaxb/L, lvw = MULT_CAP x m x vmaxw/L, ngj = the group
    count of j*, bshare = hga/A1_{j*}.  Consumes block values +
    the ledger only (the argmax access is the same class as the
    r324 pileup_state, disclosed)."""
    ax = np.abs(np.asarray(x, dtype=float))
    m = int(len(ax))
    tot = float(np.sum(ax))
    if m < 2 or tot <= 0.0 or led["ng"] == 0:
        return dict(j=0, ngj=0, hga=0.0, hgv=0.0, hga2=0.0,
                    gap=0.0, align=0.0, third=0, nwin=0, npair=0,
                    vmaxb=0.0, hgn=0.0, lvb=0.0, lvw=0.0,
                    bshare=0.0, a1j=0.0)
    j = int(np.argmax(ax))
    a, b = int(led["ptr"][j]), int(led["ptr"][j + 1])
    ga = led["gabs"][a:b]
    gv = np.abs(led["G1"][a:b])
    gm = led["gmax"][a:b]
    gw = led["gwin"][a:b]
    mu = led["mult"][a:b]
    ngj = b - a
    if ngj == 0:
        return dict(j=j, ngj=0, hga=0.0, hgv=0.0, hga2=0.0,
                    gap=0.0, align=0.0, third=0, nwin=0, npair=0,
                    vmaxb=0.0, hgn=0.0, lvb=0.0, lvw=0.0,
                    bshare=0.0, a1j=0.0)
    i1 = int(np.argmax(ga))
    hga = float(ga[i1])
    hgv = float(gv[i1])
    hga2 = float(np.max(np.delete(ga, i1))) if ngj > 1 else 0.0
    a1j = float(np.sum(ga))
    vmaxb = float(np.max(gm))
    third = min(2, (3 * i1) // ngj)
    return dict(j=j, ngj=ngj, hga=hga, hgv=hgv, hga2=hga2,
                gap=hga2 / max(hga, 1e-300),
                align=hgv / max(hga, 1e-300), third=third,
                nwin=int(round(float(gw[i1]))),
                npair=int(mu[i1]), vmaxb=vmaxb,
                hgn=float(m) * hga / tot,
                lvb=float(MULT_CAP) * float(m) * vmaxb / tot,
                lvw=float(MULT_CAP) * float(m) * led["vmaxw"] / tot,
                bshare=hga / max(a1j, 1e-300), a1j=a1j)


def cap_tree(leak, brk, lam_go, bal_go, unbounded):
    """the sealed six-letter verdict tree (booleans only; total,
    exactly one fires; order sealed):
    TARGET_LEAK > RECOMP_BREAK > LAMBDA_PAIR_CAP_GO >
    BALANCE_CAP_GO > HEAVY_GROUP_UNBOUNDED > CAP_PARTIAL."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "RECOMP_BREAK"
    if lam_go:
        return "LAMBDA_PAIR_CAP_GO"
    if bal_go:
        return "BALANCE_CAP_GO"
    if unbounded:
        return "HEAVY_GROUP_UNBOUNDED"
    return "CAP_PARTIAL"


def mutant_group_drop(gvals):
    """e1 MUST-FAIL MUTANT: an L1 'recomposition' that drops the
    last group of the block -- the recomposition ward must measure
    the exact break (LOUD)."""
    gs = tuple(float(v) for v in gvals)
    return sum(gs[:-1]) if gs else 0.0


def mutant_wrong_window_max(vals):
    """e2 MUST-FAIL MUTANT: the 'window maximum' computed on a
    TRUNCATED atom set (the global maximal atom dropped) -- the
    two-ancestor ward must break EXACTLY on the sealed toy."""
    av = sorted(abs(float(v)) for v in vals)
    return av[-2] if len(av) >= 2 else 0.0


def mutant_cap_posthoc(cap_col, rho, cbar):
    """e3 MUST-FAIL MUTANT: the cap constant re-picked AFTER SIGHT
    of the violators (consumes rho): raised until every seen
    violator is covered -- the BOUND_FORBIDDEN scope audit must
    FLAG it AND on the toy it returns != the mid-ladder rule's."""
    return max((float(c) for c, r in zip(cap_col, rho)
                if r > cbar), default=0.0)


def mutant_qmax_readback(state):
    """e4 MUST-FAIL MUTANT: a 'cap coordinate' consuming the q_max
    RECORD (the target-side concentration coordinate) -- the
    QMAX_FORBIDDEN identifier scan must FLAG this."""
    tr = state["trs"]
    return float(tr["qmax"]) * float(state["m"])


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: a 'cap orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): a
    'cap constant' consuming the branch label -- the scope audit
    must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the group toy, the cap
# ---------------- chain and the e1/e2 breaks decided as rationals
def fr_group_toy():
    """the sealed group toy in exact Fractions: block j* holds
    group A = atoms (3, 2) at one position (G1 = gabs = 5) and
    group B = atom (1); block 1 holds atom (1).  x = (6, 1),
    L = 7, m = 2: m qmax = 12/7; hga = 5, hgn = 10/7, ng = 2;
    chain slack ng x hgn - m qmax = 8/7 EXACT; vmaxb = 3,
    two-ancestor slack 2 x 3 - 5 = 1 EXACT; partition 5 + 1 == 6
    EXACT; L1 recomposition 6 + 1 == 7 EXACT; the drop-group
    mutant breaks the L1 recomposition by EXACTLY 1; the
    wrong-window-max mutant cap 2 x 2 = 4 breaks the two-ancestor
    ward by EXACTLY 1.  Returns (worst dev, chain slack, pair
    slack, drop break, wrongmax break)."""
    atoms = (Fr(3), Fr(2), Fr(1))          # block 0
    x0 = sum(atoms)
    x1 = Fr(1)
    L = abs(x0) + abs(x1)
    m = Fr(2)
    qmx = x0 / L
    hga = Fr(3) + Fr(2)
    hgn = m * hga / L
    ng = Fr(2)
    chain_slack = ng * hgn - m * qmx
    vmaxb = Fr(3)
    pair_slack = Fr(MULT_CAP) * vmaxb - hga
    part = hga + Fr(1)
    rec = abs(x0) + abs(x1)
    drop = rec - (abs(Fr(mutant_group_drop((5.0, 1.0)))) + abs(x1))
    wmx = Fr(mutant_wrong_window_max((3.0, 2.0, 1.0, 1.0)))
    wbrk = hga - Fr(MULT_CAP) * wmx
    devs = [abs(m * qmx - Fr(12, 7)), abs(hgn - Fr(10, 7)),
            abs(chain_slack - Fr(8, 7)), abs(pair_slack - 1),
            abs(part - 6), abs(rec - 7), abs(drop - 1),
            abs(wbrk - 1),
            Fr(0) if m * qmx <= ng * hgn else Fr(1),
            Fr(0) if hga <= Fr(MULT_CAP) * vmaxb else Fr(1)]
    return max(devs), chain_slack, pair_slack, drop, wbrk


def fr_align_toy():
    """the aligned/cancelling group toy: atoms (3, -2) at one
    position: G1 = 1, gabs = 5, align = 1/5 EXACT; atoms (3, 2):
    align = 1 EXACT.  Returns worst dev."""
    g1c = Fr(3) + Fr(-2)
    gac = Fr(3) + Fr(2)
    al_c = abs(g1c) / gac
    g1a = Fr(3) + Fr(2)
    al_a = abs(g1a) / gac
    return max(abs(al_c - Fr(1, 5)), abs(al_a - 1))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("group_mass_cap_probe -- "
          "PRIME.L2.RENYI3.GROUP_MASS_CAP.01 (round 327, the "
          "r324 follow-up)")
    print("SPEC_SHA %s   R324_SHA %s   R314_SHA %s   R316_SHA %s"
          % (SPEC_SHA[:16], QMO.SPEC_SHA[:16], SCF.SPEC_SHA[:16],
             TRB.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + ledger/chain/two-"
                        "ancestor wards + e1-e4; ladder, "
                        "extensions, anchors, anatomy, caps, "
                        "exponents and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE FOLD-GROUP MASS CAP ROUND (the r324 follow-up): "
          "Q1 anatomy of the dominant fold group at the spikes "
          "(ancestors, alignment, mid/tail third, gap, the "
          "sealed SOURCE/AGGREGATION letter at RATIO_BAR %.1f); "
          "Q2 the three cap candidates source-pure -- (i) the "
          "two-ancestor/lambda-pair route hga <= %d x vmax with "
          "lvb <= C_LV log m, (ii) the direct balance cap hgn <= "
          "C_HG (log m)^A (A in %s minimal), (iii) the group "
          "count ngl <= C_NG -- with the EXACT chain m qmax <= "
          "ng x hgn; Q3 recomposition to N_2 >= m^%.3f with the "
          "new m_0* vs the r324 record 10^59.6; verdict tree "
          "TARGET_LEAK / RECOMP_BREAK / LAMBDA_PAIR_CAP_GO / "
          "BALANCE_CAP_GO / HEAVY_GROUP_UNBOUNDED / CAP_PARTIAL "
          "sealed BEFORE evaluation (CRIT_EXP %.3f the r324 "
          "budget verbatim)"
          % (RATIO_BAR, MULT_CAP, str(A_FAM), N2_EXP_NEED,
             CRIT_EXP))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("group_mass_ledger", "heavy_state", "cap_tree"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the three module-own "
          "cap builders/trees clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the cap "
          "side consumes ONLY atom values / positions / block "
          "assignments / source flags / group order; m5a "
          "gift-bound FLAGGED (%s); m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r324 scaffold verbatim)
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
    section("S2  EXACT DECOMPOSITION + GROUP-LEDGER WARDS")
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
            pst = QMO.pileup_state(sct["x"], val_all, blk_all)
            led = group_mass_ledger(pos_all, val_all, blk_all,
                                    src_all, m)
            hst = heavy_state(sct["x"], led)
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
            pst = dict(j=0, nsc=0, nsc_rel=0, pil=0.0, a1j=0.0,
                       tail=0.0, scut=0, scales=(), masses=())
            led = dict(G1=np.zeros(0), gabs=np.zeros(0),
                       gmax=np.zeros(0), gwin=np.zeros(0),
                       mult=np.zeros(0, int), ng=0,
                       gblk=np.zeros(0, int),
                       ptr=np.zeros(1, int), vmaxw=0.0)
            hst = heavy_state(np.zeros(0), led)
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs, pst=pst,
                    led=led, hst=hst,
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
    led_dev = 0.0
    for rc in live:
        ev = rc["ev"]
        gen = ev["gen"]
        led = ev["led"]
        if gen["ng"] != led["ng"]:
            led_dev = max(led_dev, 1.0)
            continue
        if gen["ng"]:
            sc = max(float(np.max(np.abs(gen["G1"]))), 1e-300)
            led_dev = max(
                led_dev,
                float(np.max(np.abs(led["G1"] - gen["G1"]))) / sc,
                float(np.max(np.abs(led["mult"] - gen["mult"]))),
                float(np.max(np.abs(led["gblk"] - gen["gblk"]))))
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "module-own group ledger segments IDENTICALLY to the "
          "genealogy (G1/mult/gblk worst dev %.1e, bar %.0e)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (slim + r324 record)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim + the r324 "
            "record)")
    rec3_w = max(rc["ev"]["rec3"] for rc in live)
    tel_w = max(rc["ev"]["tel_dev"] for rc in live)
    bnd_w = max(rc["ev"]["bnd_dev"] for rc in live)
    check("G30-r314-identity-wards",
          rec3_w <= REC3_BAR and tel_w <= TEL_BAR
          and bnd_w <= BND_BAR,
          "the r314 identity live on %d live worlds: three-term "
          "recomposition dev %.1e (bar %.0e), telescope dev %.1e "
          "(bar %.0e), boundary %.1e (bar %.0e); DISCLOSED slim "
          "anchor set -- the full chain is re-warded by the "
          "sealed r321/r324 probes"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        hs = ev9s["hst"]
        info("SMOKE: w9 G %.3f ng %d hgn %.4f lvb %.4f gap %.3f "
             "align %.3f third %d nwin %d"
             % (ev9s["m"] * ev9s["trs"]["qmax"], hs["ngj"],
                hs["hgn"], hs["lvb"], hs["gap"], hs["align"],
                hs["third"], hs["nwin"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r324-pileup-anchors", True, "SMOKE: skipped")
        check("G34-r324pre-m2-anchor", True, "SMOKE: skipped")
        srt = []
        n327 = 0
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
        srt_all = sorted(recs + erecs + e2recs,
                         key=lambda rc: (rc["N"], rc["kz"]))
        srt = [rc for rc in srt_all
               if rc["ev"]["mx_mult"] <= MULT_CAP]
        n327 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n327)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n327 == N327_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n327, N327_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n327):
                if srt[i]["kz"] == kz:
                    named_rank[kz] = i
        # r324 record anchors: pileup columns re-derived
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt]
        G_col = [m_all[i] * qmax_col[i] for i in range(n327)]
        GL_col = [G_col[i] / math.log(float(m_all[i]))
                  for i in range(n327)]
        nscr_col = [rc["ev"]["pst"]["nsc_rel"] for rc in srt]
        pil_col = [rc["ev"]["pst"]["pil"] for rc in srt]
        nsclog = [nscr_col[i] / math.log(float(m_all[i]))
                  for i in range(n327)]
        C_NSC = max(nsclog[i] for i in ca_i)
        viol_nsc = [i for i in te_i if nsclog[i] > C_NSC]
        C_PIL = max(pil_col[i] for i in ca_i)
        viol_pil = [i for i in te_i if pil_col[i] > C_PIL]
        C_INF = max(GL_col[i] for i in ca_i)
        viol_G = [i for i in te_i if GL_col[i] > C_INF]
        msT = [m_all[i] for i in te_i]
        e_G = L2D.halves_slope(msT, [max(GL_col[i], 1e-300)
                                     for i in te_i])
        m2_col = [rc["ev"]["mqs"]["m2"] for rc in srt]
        e_M2 = L2D.halves_slope(msT, [max(m2_col[i], 1e-300)
                                      for i in te_i])
        e_tot = e_G + e_M2
        s0_ok = all(abs(pil_col[named_rank[kz]] - R324_S0[kz])
                    <= R324_S0_TOL for kz in R324_S0)
        check("G33-r324-pileup-anchors",
              abs(C_NSC - R324_CNSC) <= R324_C_TOL
              and abs(C_PIL - R324_CPIL) <= R324_C_TOL
              and abs(C_INF - R324_CINF) <= R324_C_TOL
              and len(viol_nsc) == R324_VNSC
              and len(viol_pil) == R324_VPIL
              and len(viol_G) == R324_VINF
              and s0_ok
              and abs(e_G - R324_EG) <= R324_E_TOL
              and abs(e_M2 - R324_EM2) <= R324_E_TOL
              and abs(e_tot - R324_ETOT) <= R324_E_TOL,
              "the r324 RECORD reproduced bit-near: C_NSC %.4f "
              "(rec %.4f) viol %d/%d (rec %d), C_PIL %.4f (rec "
              "%.4f) viol %d (rec %d), C_INF %.4f (rec %.4f) "
              "viol %d (rec %d); named heavy-scale masses "
              "kz53/kz83/kz67 = %.3f/%.3f/%.3f (rec 13.778/"
              "12.707/22.378 tol %.2f); exponents e(G/log m) "
              "%+.3f / e(m M_2) %+.3f / e_tot %+.3f (rec "
              "%+.3f/%+.3f/%+.3f tol %.3f)"
              % (C_NSC, R324_CNSC, len(viol_nsc), len(te_i),
                 R324_VNSC, C_PIL, R324_CPIL, len(viol_pil),
                 R324_VPIL, C_INF, R324_CINF, len(viol_G),
                 R324_VINF, pil_col[named_rank[53]],
                 pil_col[named_rank[83]], pil_col[named_rank[67]],
                 R324_S0_TOL, e_G, e_M2, e_tot, R324_EG,
                 R324_EM2, R324_ETOT, R324_E_TOL))
        C_M2 = max(m2_col[i] for i in ca_i)
        viol_m2 = tuple(sorted(srt[i]["kz"] for i in te_i
                               if m2_col[i] > C_M2))
        C_M2env = max(m2_col)
        check("G34-r324pre-m2-anchor",
              abs(C_M2 - R324P_CM2) <= R324P_CM2_TOL
              and viol_m2 == tuple(sorted(R324P_M2VIOL)),
              "the r324-pre m2 record reproduced: mid-ladder "
              "freeze C_M2 %.4f (rec %.4f tol %.3f); the seven "
              "test violators %s == the banked set EXACT; ladder "
              "envelope C_2env = %.4f (the composition's M_2 "
              "side)" % (C_M2, R324P_CM2, R324P_CM2_TOL,
                         str(viol_m2), C_M2env))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "SOURCE-PURE TABLE")
    pure_lits = []
    for fn in ("group_mass_ledger", "heavy_state", "cap_tree",
               "fr_group_toy", "fr_align_toy"):
        pure_lits += literal_audit(fn)
    e3_hits = scope_audit("mutant_cap_posthoc", BOUND_FORBIDDEN)
    e4_hits = scope_audit("mutant_qmax_readback", QMAX_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e3_hits) >= 1 and len(e4_hits) >= 1,
          "SOURCE PURITY: the cap builders clean vs the forbidden "
          "sets (%d id hits) and vs the sealed r314..r324 record-"
          "literal set (%d literal hits); consumed inputs: atom "
          "values / positions / block assignments / source flags "
          "/ group order -- M_3, rho_2 and the q_max RECORD are "
          "TARGET-SIDE, computed outside the builders "
          "(disclosed); e3 cap-posthoc FLAGGED (%s); e4 "
          "qmax-readback FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e3_hits[0] if e3_hits else "MISS",
             e4_hits[0] if e4_hits else "MISS"))
    fr_dev, fr_chain, fr_pair, fr_drop, fr_wmx = fr_group_toy()
    fr_al = fr_align_toy()
    toy_pos = np.array([0.1, 0.1, 0.2, 0.3])
    toy_val = np.array([3.0, 2.0, 1.0, 1.0])
    toy_blk = np.array([0, 0, 0, 1])
    toy_src = np.array([0.0, 1.0, 0.0, 0.0])
    led_t = group_mass_ledger(toy_pos, toy_val, toy_blk, toy_src, 2)
    hst_t = heavy_state(np.array([6.0, 1.0]), led_t)
    ok_led = (led_t["ng"] == 3
              and abs(led_t["gabs"][0] - 5.0) <= FR_BAR
              and abs(led_t["gmax"][0] - 3.0) <= FR_BAR
              and int(led_t["mult"][0]) == 2
              and abs(led_t["vmaxw"] - 3.0) <= FR_BAR)
    ok_hst = (hst_t["j"] == 0 and hst_t["ngj"] == 2
              and abs(hst_t["hga"] - 5.0) <= FR_BAR
              and abs(hst_t["hgn"] - 10.0 / 7.0) <= FR_BAR
              and abs(hst_t["lvb"] - 12.0 / 7.0) <= FR_BAR
              and abs(hst_t["gap"] - 0.2) <= FR_BAR
              and abs(hst_t["align"] - 1.0) <= FR_BAR
              and hst_t["nwin"] == 1 and hst_t["npair"] == 2)
    tr_br = (cap_tree(True, True, True, True, True),
             cap_tree(False, True, True, True, True),
             cap_tree(False, False, True, True, True),
             cap_tree(False, False, False, True, True),
             cap_tree(False, False, False, False, True),
             cap_tree(False, False, False, False, False))
    ok_tr = tr_br == ("TARGET_LEAK", "RECOMP_BREAK",
                      "LAMBDA_PAIR_CAP_GO", "BALANCE_CAP_GO",
                      "HEAVY_GROUP_UNBOUNDED", "CAP_PARTIAL")
    check("G41-toy-exactness",
          fr_dev == 0 and fr_al == 0 and ok_led and ok_hst
          and ok_tr,
          "the Fractions group toy EXACT (worst dev %s): chain "
          "slack %s, two-ancestor slack %s, drop break %s LOUD, "
          "wrong-window-max break %s CAUGHT; align toy EXACT "
          "(worst %s); the float ledger/heavy_state match the "
          "toy (ng 3, gabs (5,1,1), hga 5, hgn 10/7, lvb 12/7, "
          "gap 1/5, align 1, nwin 1, npair 2); cap_tree all six "
          "branches EXACT %s"
          % (str(fr_dev), str(fr_chain), str(fr_pair),
             str(fr_drop), str(fr_wmx), str(fr_al), str(tr_br)))
    # live wards
    chain_w = 0.0
    xw_cube = 0.0
    interp_w = 0.0
    part_w = 0.0
    l1rec_w = 0.0
    panc_w = 0.0
    capch_w = 0.0
    lvch_w = 0.0
    pilch_w = 0.0
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
        mloc = ev["m"]
        interp_w = max(interp_w,
                       max(0.0, M3 - qmx * M2)
                       / max(qmx * M2, 1e-300),
                       max(0.0, M2 - qmx) / max(qmx, 1e-300))
        led = ev["led"]
        # partition: per-block sum of gabs == A1_j
        A1led = np.bincount(led["gblk"], weights=led["gabs"],
                            minlength=mloc)
        part_w = max(part_w,
                     float(np.max(np.abs(A1led - ev["A1"])))
                     / max(float(np.max(ev["A1"])), 1e-300))
        # L1 recomposition: sum_j |sum_g G1_g| == L
        xled = np.bincount(led["gblk"], weights=led["G1"],
                           minlength=mloc)
        l1rec_w = max(l1rec_w,
                      abs(float(np.sum(np.abs(xled))) - Lx)
                      / max(Lx, 1e-300))
        # two-ancestor bound per group: gabs <= mult x gmax
        if led["ng"]:
            panc_w = max(panc_w,
                         float(np.max(led["gabs"]
                                      - led["mult"] * led["gmax"]))
                         / max(float(np.max(led["gabs"])), 1e-300))
        # the cap chain: m qmax <= ng x hgn  AND  hgn <= lvb
        hs = ev["hst"]
        G = mloc * qmx
        capch_w = max(capch_w,
                      max(0.0, G - hs["ngj"] * hs["hgn"])
                      / max(hs["ngj"] * hs["hgn"], 1e-300))
        lvch_w = max(lvch_w,
                     max(0.0, hs["hgn"] - hs["lvb"])
                     / max(hs["lvb"], 1e-300))
        # the r324 pileup chain re-warded
        pst = ev["pst"]
        pilch_w = max(pilch_w,
                      max(0.0, G - pst["nsc"] * pst["pil"])
                      / max(pst["nsc"] * pst["pil"], 1e-300))
        mult_all_ok = mult_all_ok \
            and QMO.mult_ward(rc["ev"]["gen"]["mult"])[1]
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and interp_w <= CHAIN_BAR and part_w <= SA_BAR
          and l1rec_w <= SA_BAR and panc_w <= TOY_BAR
          and capch_w <= CHAIN_BAR and lvch_w <= CHAIN_BAR
          and pilch_w <= CHAIN_BAR and mult_all_ok,
          "the r316 chain live on %d live worlds (worst %.1e); "
          "NORM x cube == rho_2 (%.1e); S0 interpolation (worst "
          "%.1e); GROUP PARTITION sum_g gabs == A1_j (worst "
          "%.1e, bar %.0e); L1 RECOMPOSITION sum_j |sum_g G1| == "
          "L (worst %.1e); TWO-ANCESTOR gabs <= mult x gmax on "
          "every group (worst slack %.1e); THE CAP CHAIN m qmax "
          "<= ng x hgn (worst %.1e) AND hgn <= lvb (worst %.1e); "
          "the r324 pileup chain re-warded (%.1e); fold "
          "multiplicity <= %d admitted on ALL live worlds"
          % (len(live), chain_w, xw_cube, interp_w, part_w,
             SA_BAR, l1rec_w, panc_w, capch_w, lvch_w, pilch_w,
             MULT_CAP))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        ng_col = [rc["ev"]["hst"]["ngj"] for rc in srt]
        hgn_col = [rc["ev"]["hst"]["hgn"] for rc in srt]
        lvb_col = [rc["ev"]["hst"]["lvb"] for rc in srt]
        lvw_col = [rc["ev"]["hst"]["lvw"] for rc in srt]
        gap_col = [rc["ev"]["hst"]["gap"] for rc in srt]
        al_col = [rc["ev"]["hst"]["align"] for rc in srt]
        th_col = [rc["ev"]["hst"]["third"] for rc in srt]
        nw_col = [rc["ev"]["hst"]["nwin"] for rc in srt]
        bs_col = [rc["ev"]["hst"]["bshare"] for rc in srt]
        rat_col = []
        for rc in srt:
            pmx = max(rc["ev"]["pst"]["masses"]) \
                if rc["ev"]["pst"]["masses"] else 0.0
            rat_col.append(rc["ev"]["hst"]["hga"]
                           / max(pmx, 1e-300))
        hgl_col = [hgn_col[i] / math.log(float(m_all[i]))
                   for i in range(n327)]
        lvl_col = [lvb_col[i] / math.log(float(m_all[i]))
                   for i in range(n327)]
        ngl_col = [ng_col[i] / math.log(float(m_all[i]))
                   for i in range(n327)]
        info("sealed SOURCE-PURE table (printed BEFORE any "
             "certification table): rank kz N m G ng hgn "
             "hgn/logm lvb/logm gap align ratio third nwin")
        for i, rc in enumerate(srt):
            info("%2d kz%-3d N %4d m %3d G %6.3f ng %2d hgn "
                 "%6.3f hgL %.3f lvL %.3f gap %.3f al %.3f rat "
                 "%.3f t%d w%d"
                 % (i, rc["kz"], rc["N"], m_all[i], G_col[i],
                    ng_col[i], hgn_col[i], hgl_col[i],
                    lvl_col[i], gap_col[i], al_col[i],
                    rat_col[i], th_col[i], nw_col[i]))
        check("G43-coordinate-table", True,
              "hgn range %.2f/%.2f/%.2f min/med/max (max at "
              "kz%d); hgn/log m med %.3f max %.3f; lvb/log m "
              "med %.3f max %.3f (window-global lvw med %.3f "
              "max %.3f census); ng med %.0f max %d; gap med "
              "%.3f max %.3f; align med %.3f; bshare med %.3f; "
              "ratio med %.3f"
              % (min(hgn_col), float(np.median(hgn_col)),
                 max(hgn_col),
                 srt[int(np.argmax(hgn_col))]["kz"],
                 float(np.median(hgl_col)), max(hgl_col),
                 float(np.median(lvl_col)), max(lvl_col),
                 float(np.median([lvw_col[i]
                                  / math.log(float(m_all[i]))
                                  for i in range(n327)])),
                 max(lvw_col[i] / math.log(float(m_all[i]))
                     for i in range(n327)),
                 float(np.median(ng_col)), max(ng_col),
                 float(np.median(gap_col)), max(gap_col),
                 float(np.median(al_col)),
                 float(np.median(bs_col)),
                 float(np.median(rat_col))))

    # ---------------- S5: Leg B -- Q1 anatomy
    section("S5  LEG B -- Q1 HEAVY-GROUP ANATOMY (census + "
            "sealed adjudication)")
    if smoke:
        check("G50-heavy-census", True, "SMOKE: skipped")
        check("G51-source-vs-aggregation", True, "SMOKE: skipped")
        anatomy = "SMOKE"
    else:
        info("the heavy group at the named near-critical rungs "
             "(the r324 spikes):")
        for kz in NAMED_HV_KZ:
            i = named_rank[kz]
            hs = srt[i]["ev"]["hst"]
            pmx = max(srt[i]["ev"]["pst"]["masses"]) \
                if srt[i]["ev"]["pst"]["masses"] else 0.0
            info("  kz%-3d G %.2f | hga %.4f (m hga/L %.3f) vs "
                 "heavy scale mass %.4f -> ratio %.3f | ng %d "
                 "gap %.3f align %.3f third %d nwin %d npair %d "
                 "bshare %.3f"
                 % (kz, G_col[i], hs["hga"], hs["hgn"],
                    pmx * 1.0, rat_col[i], hs["ngj"], hs["gap"],
                    hs["align"], hs["third"], hs["nwin"],
                    hs["npair"], hs["bshare"]))
        th_hist = [sum(1 for t in th_col if t == k)
                   for k in (0, 1, 2)]
        nw_hist = [sum(1 for w in nw_col if w == k)
                   for k in (0, 1, 2)]
        check("G50-heavy-census", True,
              "ladder census: gap med %.3f max %.3f (second/"
              "first heaviest group); align med %.3f min %.3f "
              "(1 = no internal cancellation); position thirds "
              "%s (the r322 mid/tail question); heavy-group "
              "window-atom count histogram %s (0 = pure bulk, "
              "1 = beta/omega fold, 2 = pure window); bshare "
              "med %.3f max %.3f (in-block share of the heavy "
              "group)"
              % (float(np.median(gap_col)), max(gap_col),
                 float(np.median(al_col)), min(al_col),
                 str(th_hist), str(nw_hist),
                 float(np.median(bs_col)), max(bs_col)))
        named_ratio = [rat_col[named_rank[kz]]
                       for kz in NAMED_HV_KZ]
        med_ratio = float(np.median(named_ratio))
        anatomy = "SOURCE" if med_ratio >= RATIO_BAR \
            else "AGGREGATION"
        check("G51-source-vs-aggregation", True,
              "SEALED ADJUDICATION (RATIO_BAR %.1f): med named "
              "ratio hga/(heavy scale mass) = %.3f %s -> "
              "ANATOMY = %s (%s); ladder ratio med %.3f -- the "
              "heavy SCALE of the r324 spikes is %s"
              % (RATIO_BAR, med_ratio,
                 str([round(v, 3) for v in named_ratio]),
                 anatomy,
                 "one group carries the scale: the heaviness is "
                 "a SOURCE property (two source masses meet at "
                 "one fold target)" if anatomy == "SOURCE" else
                 "no single group carries the scale: the "
                 "heaviness is AGGREGATION (the fold bundles "
                 "many groups inside one scale)",
                 float(np.median(rat_col)),
                 "single-group-carried" if anatomy == "SOURCE"
                 else "many-group aggregated"))

    # ---------------- S6: Leg C -- Q2 cap certification
    section("S6  LEG C -- Q2 CAP CANDIDATES (mid-ladder freeze + "
            "exponents)")
    if smoke:
        check("G60-lambda-pair-cap", True, "SMOKE: skipped")
        check("G61-balance-cap", True, "SMOKE: skipped")
        check("G62-group-count-cap", True, "SMOKE: skipped")
        check("G63-growth-exponents", True, "SMOKE: skipped")
    else:
        C_LV = max(lvl_col[i] for i in ca_i)
        viol_lv = [i for i in te_i if lvl_col[i] > C_LV]
        named_lv = sum(1 for kz in NAMED_KZ
                       if lvl_col[named_rank[kz]] <= C_LV)
        C_LVs = max(lvl_col[i] for i in sm_i)
        check("G60-lambda-pair-cap", True,
              "(i) THE LAMBDA-PAIR CAP lvb = %d x m x vmaxb/L <= "
              "C_LV x log m: C_LV = %.4f (mid-ladder frozen at "
              "kz%d; small-m C %.4f); test violations %d/%d %s; "
              "named coverage %d/4 %s"
              % (MULT_CAP, C_LV,
                 srt[max(ca_i, key=lambda i: lvl_col[i])]["kz"],
                 C_LVs, len(viol_lv), len(te_i),
                 str([(srt[i]["kz"], round(lvl_col[i], 3))
                      for i in viol_lv]) if viol_lv else "[]",
                 named_lv,
                 str({("kz%d" % kz): round(lvl_col[named_rank[kz]],
                                           3)
                      for kz in NAMED_KZ})))
        hg_caps = {}
        for A in A_FAM:
            col = [hgn_col[i] / (math.log(float(m_all[i])) ** A)
                   for i in range(n327)]
            C_A = max(col[i] for i in ca_i)
            viol_A = [i for i in te_i if col[i] > C_A]
            named_A = sum(1 for kz in NAMED_KZ
                          if col[named_rank[kz]] <= C_A)
            hg_caps[A] = (C_A, viol_A, named_A, col)
        minA = None
        for A in A_FAM:
            if not hg_caps[A][1] and hg_caps[A][2] == len(NAMED_KZ):
                minA = A
                break
        check("G61-balance-cap", True,
              "(ii) THE DIRECT GROUP-MASS CAP hgn <= C_HG x "
              "(log m)^A: A=1 C %.4f viol %d/%d named %d/4 %s; "
              "A=2 C %.4f viol %d/%d named %d/4 %s; minimal "
              "certifying A = %s"
              % (hg_caps[1][0], len(hg_caps[1][1]), len(te_i),
                 hg_caps[1][2],
                 str([(srt[i]["kz"],
                       round(hg_caps[1][3][i], 3))
                      for i in hg_caps[1][1]])
                 if hg_caps[1][1] else "[]",
                 hg_caps[2][0], len(hg_caps[2][1]), len(te_i),
                 hg_caps[2][2],
                 str([(srt[i]["kz"],
                       round(hg_caps[2][3][i], 3))
                      for i in hg_caps[2][1]])
                 if hg_caps[2][1] else "[]",
                 str(minA)))
        C_NG = max(ngl_col[i] for i in ca_i)
        viol_ng = [i for i in te_i if ngl_col[i] > C_NG]
        named_ng = sum(1 for kz in NAMED_KZ
                       if ngl_col[named_rank[kz]] <= C_NG)
        check("G62-group-count-cap", True,
              "(iii) THE GROUP COUNT ngl = ng(argmax block)/"
              "log m <= C_NG: C_NG = %.4f; test violations "
              "%d/%d %s; named %d/4; ng med %.0f max %d "
              "(compare the r324 certified scale count C_NSC "
              "%.4f)"
              % (C_NG, len(viol_ng), len(te_i),
                 str([(srt[i]["kz"], round(ngl_col[i], 3))
                      for i in viol_ng]) if viol_ng else "[]",
                 named_ng, float(np.median(ng_col)), max(ng_col),
                 C_NSC))
        e_hg = L2D.halves_slope(msT, [max(hgl_col[i], 1e-300)
                                      for i in te_i])
        e_lv = L2D.halves_slope(msT, [max(lvl_col[i], 1e-300)
                                      for i in te_i])
        e_ng = L2D.halves_slope(msT, [max(ngl_col[i], 1e-300)
                                      for i in te_i])
        e_route = e_hg + e_ng + e_M2
        h = len(te_i) // 2
        te_a = te_i[:h]
        te_b = te_i[h:]

        def eroute_on(idx):
            ms = [m_all[i] for i in idx]
            ea = L2D.halves_slope(ms, [max(hgl_col[i], 1e-300)
                                       for i in idx])
            eb = L2D.halves_slope(ms, [max(ngl_col[i], 1e-300)
                                       for i in idx])
            ec = L2D.halves_slope(ms, [max(m2_col[i], 1e-300)
                                       for i in idx])
            return ea + eb + ec

        e_a = eroute_on(te_a)
        e_b = eroute_on(te_b)
        decided = ((e_a >= CRIT_EXP) == (e_b >= CRIT_EXP)
                   and (e_a >= CRIT_EXP) == (e_route >= CRIT_EXP))
        check("G63-growth-exponents", True,
              "GROWTH EXPONENTS (r272 dyadic halves-slope vs m "
              "over the %d test rungs, fit-free): e(hgn/log m) "
              "= %+.3f, e(lvb/log m) = %+.3f, e(ngl) = %+.3f, "
              "e(m M_2) = %+.3f -> e_route = %+.3f vs CRIT %.3f "
              "(the r324 budget; r324 e_tot %+.3f for "
              "comparison); stability halves %+.3f / %+.3f -> "
              "%s, %s"
              % (len(te_i), e_hg, e_lv, e_ng, e_M2, e_route,
                 CRIT_EXP, e_tot, e_a, e_b,
                 "DECIDED" if decided else "UNDECIDED",
                 ("UNBOUNDED-SIDE" if e_route >= CRIT_EXP
                  else "SUBCRITICAL-SIDE") if decided else "open"))

    # ---------------- S7: Leg D -- adjudication + composition
    section("S7  LEG D -- SEALED ADJUDICATION + Q3 COMPOSITION")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-composition", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(sc_own) or bool(pure_lits)
        brk_struct = (part_w > SA_BAR or l1rec_w > SA_BAR
                      or panc_w > TOY_BAR or capch_w > CHAIN_BAR
                      or led_dev > SA_BAR or not mult_all_ok)
        ng_ok = (not viol_ng) and named_ng == len(NAMED_KZ)
        lam_go = ((not viol_lv) and named_lv == len(NAMED_KZ)
                  and ng_ok and panc_w <= TOY_BAR)
        bal_go = (not lam_go) and (minA is not None) and ng_ok
        unbounded = ((not lam_go) and (not bal_go)
                     and decided and e_route >= CRIT_EXP)
        vkey = cap_tree(leak, brk_struct, lam_go, bal_go,
                        unbounded)
        rest = []
        if viol_lv:
            rest.append("lambda-pair %d viol" % len(viol_lv))
        elif named_lv < len(NAMED_KZ):
            rest.append("lambda-pair named %d/4" % named_lv)
        if minA is None:
            rest.append("direct cap fails at A<=2 (%d/%d viol)"
                        % (len(hg_caps[2][1]), len(te_i)))
        if not ng_ok:
            rest.append("group count %d viol named %d/4"
                        % (len(viol_ng), named_ng))
        if not decided:
            rest.append("exponent halves straddle %+.3f/%+.3f"
                        % (e_a, e_b))
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on a cap "
                           "builder",
            "RECOMP_BREAK": "the group ledger breaks "
                            "structurally",
            "LAMBDA_PAIR_CAP_GO":
                "A = 1: hga <= %d vmaxb exact + lvb/log m 0 "
                "viol (C_LV %.4f) + group count 0 viol (C_NG "
                "%.4f)" % (MULT_CAP, C_LV, C_NG),
            "BALANCE_CAP_GO":
                "A = %s: hgn/(log m)^A 0 viol (C %.4f) + group "
                "count 0 viol (C_NG %.4f)"
                % (str(minA),
                   hg_caps[minA][0] if minA else 0.0, C_NG),
            "HEAVY_GROUP_UNBOUNDED":
                "e_route %+.3f >= %.3f DECIDED (halves "
                "%+.3f/%+.3f) -- the +0.172 exponent is "
                "presumably unavoidable on this route"
                % (e_route, CRIT_EXP, e_a, e_b),
            "CAP_PARTIAL":
                "rest: %s; e_route %+.3f %s CRIT %.3f (halves "
                "%+.3f/%+.3f)"
                % ("; ".join(rest) if rest else "none",
                   e_route, ">=" if e_route >= CRIT_EXP
                   else "<", CRIT_EXP, e_a, e_b)}
        verdict_main = "%s(%s)" % (vkey, det_v[vkey])
        check("G70-adjudication", True,
              "exactly one sealed letter fired: %s"
              % verdict_main)
        # Q3 composition (printed ALWAYS, honestly typed)
        if vkey == "LAMBDA_PAIR_CAP_GO":
            A_use = 1
            C_qmx = C_NG * C_LV
            hyp = ("lambda-pair + group count mid-ladder "
                   "CERTIFIED pointwise (0 violations)")
        elif vkey == "BALANCE_CAP_GO":
            A_use = minA
            C_qmx = C_NG * hg_caps[minA][0]
            hyp = ("direct cap (A = %d) + group count "
                   "mid-ladder CERTIFIED pointwise" % minA)
        else:
            A_use = None
            C_qmx = max(ngl_col[i] * hgl_col[i]
                        for i in range(n327))
            hyp = ("NO certifying cap -- the r324 MEASURED "
                   "composition stands unchanged; the cap-route "
                   "envelope is printed as census")
        info("Q3 COMPOSITION (%s):" % hyp)
        if A_use is not None:
            Atot = 1 + A_use
            C_full = C_qmx * C_M2env
            m_star_l10 = None
            t = math.log(73.0)
            while t < 1e7:
                if t * CRIT_EXP >= math.log(C_full) \
                        + Atot * math.log(t):
                    m_star_l10 = t / math.log(10.0)
                    break
                t *= 1.02
            ms_txt = ("10^%.1f" % m_star_l10) \
                if m_star_l10 is not None else "NONE"
            info("  m qmax <= ng x hgn <= C_NG C_cap (log m)^%d "
                 "= %.3f (log m)^%d  =>  sum q^3 <= %.3f x "
                 "(log m)^%d / m^2 (C_2env %.4f measured "
                 "envelope, typed MEASURED);"
                 % (Atot, C_qmx, Atot, C_full, Atot, C_M2env))
            info("  => N_3 >= m/sqrt(%.3f (log m)^%d), N_2 >= "
                 "N_3 (r306 exact chain) => N_2 >= m^%.3f for "
                 "all m >= m_0* = %s (m^{%.3f} >= %.3f "
                 "(log m)^%d) -- vs the r324 record m_0* = "
                 "10^59.6: the exponent m^{+0.172} is REPLACED "
                 "by polylog;"
                 % (C_full, Atot, N2_EXP_NEED, ms_txt, CRIT_EXP,
                    C_full, Atot))
            info("  => slope(n_eff) >= %+.3f => sigma <= sigma* "
                 "= %.3f => the r297 target => the v964-S0 vdC "
                 "theorem => delta' > %.2f => the "
                 "terminal_positive_main edge; all measured m "
                 "<= %d closed by the finite certificates; the "
                 "gap (%d, m_0*) stays the disclosed "
                 "extrapolation hypothesis."
                 % (NEED_SLOPE, SIGMA_STAR, DELTA_NEED,
                    max(m_all), max(m_all)))
            comp_ok = (m_star_l10 is not None)
            comp_txt = "m_0* %s (A_tot %d, C %.3f)" \
                % (ms_txt, Atot, C_full)
        else:
            info("  the r324 MEASURED composition restated "
                 "(anchor-gated in G33): sum q^3 <= 8.941 x "
                 "(log m) x m^{%+.3f}/m^2 => N_2 >= m^%.3f for "
                 "all m >= m_0* = 10^59.6 -- the fold-group cap "
                 "route does NOT improve it; measured cap-route "
                 "envelope max(ngl x hgL) = %.3f, e_route "
                 "%+.3f."
                 % (e_tot, N2_EXP_NEED, C_qmx, e_route))
            comp_ok = True
            comp_txt = "r324 restated (m_0* 10^59.6, e_tot " \
                "%+.3f); cap envelope %.3f" % (e_tot, C_qmx)
        check("G71-composition", comp_ok,
              "composition printed with explicit constants "
              "(%s); the chain to terminal_positive_main is "
              "typed: partition/recomposition/two-ancestor/cap "
              "chain exact, every constant MEASURED on the "
              "finite ladder, the ladder-to-m_0* step an "
              "extrapolation hypothesis -- NO cofinal claim"
              % comp_txt)

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    led9 = ev9m["led"]
    hs9 = ev9m["hst"]
    j9 = hs9["j"]
    a9, b9 = int(led9["ptr"][j9]), int(led9["ptr"][j9 + 1])
    g9 = led9["G1"][a9:b9]
    x9j = float(np.sum(g9))
    drop9 = mutant_group_drop(tuple(float(v) for v in g9))
    dev1 = abs(drop9 - x9j) / max(abs(x9j), 1e-300) \
        if b9 - a9 > 1 else 1.0
    check("G80-e1-group-drop",
          fr_drop == 1 and dev1 >= MUT_MIN,
          "e1 LOUD: the drop-group 'recomposition' breaks the "
          "toy L1 by EXACTLY %s (Fractions-warded in G41) and "
          "the real argmax block value by rel %.1e >= %.0e -- "
          "an incomplete group ledger cannot slip through the "
          "recomposition ward (live worst %.1e)"
          % (str(fr_drop), dev1, MUT_MIN, l1rec_w
             if not smoke else 0.0))
    wmx9 = mutant_wrong_window_max(tuple(
        float(v) for v in ev9m["val_all"]))
    true9 = float(np.max(np.abs(ev9m["val_all"])))
    check("G81-e2-wrong-window-max",
          fr_wmx == 1 and wmx9 <= true9,
          "e2 CAUGHT (exact): the truncated-window 'maximum' "
          "breaks the two-ancestor ward on the sealed toy by "
          "EXACTLY %s (mutant cap 4 < hga 5, true slack 1) "
          "while the true window maximum holds it exactly "
          "(live worst slack %.1e); real w9 mutant max %.3e <= "
          "true %.3e -- a lambda-pair bound with the wrong "
          "window maximum is structurally refused"
          % (str(fr_wmx), panc_w, wmx9, true9))
    toy_capcol = (1.0, 3.0, 2.0)
    toy_rho = (0.1, 0.9, 0.1)
    cap_mut = mutant_cap_posthoc(toy_capcol, toy_rho, 0.5)
    cap_seal = max(toy_capcol[:1])
    check("G82-e3-cap-posthoc",
          len(e3_hits) >= 1 and cap_mut == 3.0
          and cap_mut != cap_seal,
          "e3 CAUGHT twice: the after-sight cap re-pick "
          "consumes the evaluated bound column -- AST-FLAGGED "
          "(%s) -- and on the toy returns %.1f != the sealed "
          "mid-ladder freeze rule's %.1f (a cap constant chosen "
          "after sight of the spikes is structurally refused)"
          % (e3_hits[0] if e3_hits else "MISS", cap_mut,
             cap_seal))
    rb9 = mutant_qmax_readback(dict(trs=ev9m["trs"],
                                    m=ev9m["m"]))
    check("G83-e4-qmax-readback",
          len(e4_hits) >= 1 and (not sc_own) and rb9 >= 0.0,
          "e4 AST-CAUGHT: the 'cap coordinate' consuming the "
          "q_max RECORD is FLAGGED (%s) while the three "
          "module-own cap builders are clean (%d hits) -- the "
          "target-side concentration coordinate cannot enter "
          "the cap side (the mutant value %.3f is computed only "
          "to prove the mutant runs)"
          % (e4_hits[0] if e4_hits else "MISS", len(sc_own),
             rb9))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact per-group mass ledger on the r314 "
          "fold segmentation (partition + L1 recomposition + "
          "two-ancestor bound), the heavy-group anatomy with "
          "the sealed SOURCE/AGGREGATION adjudication, the "
          "three cap candidates with mid-ladder certification "
          "and the exact cap chain m qmax <= ng x hgn, the "
          "route growth exponent and the Q3 recomposition -- "
          "NO new certificate promoted, NO universal bound "
          "claimed beyond the measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R327_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d rho4 bit-near, r324 C_NSC "
                 "%.4f/C_PIL %.4f/C_INF %.4f viols %d/%d/%d, s0 "
                 "named 3/3, e_tot %+.3f, r324-pre C_M2 %.4f "
                 "viol7 EXACT)"
                 % (rec3_w, C2r, viol2, n327, C_NSC, C_PIL,
                    C_INF, len(viol_nsc), len(viol_pil),
                    len(viol_G), e_tot, C_M2)]
        parts.append("SEAL(partition %.1e, L1 recomposition "
                     "%.1e, two-ancestor %.1e, cap chain %.1e, "
                     "ledger %.1e, purity clean, toys exact)"
                     % (part_w, l1rec_w, panc_w, capch_w,
                        led_dev))
        parts.append("ANATOMY(%s: named ratio %.3f, gap med "
                     "%.3f, align med %.3f, thirds %s, nwin "
                     "%s)"
                     % (anatomy, med_ratio,
                        float(np.median(gap_col)),
                        float(np.median(al_col)), str(th_hist),
                        str(nw_hist)))
        parts.append("CAPS(C_LV %.4f viol %d named %d/4, C_HG1 "
                     "%.4f viol %d, C_HG2 %.4f viol %d, minA "
                     "%s, C_NG %.4f viol %d, e_hg %+.3f e_lv "
                     "%+.3f e_ng %+.3f e_route %+.3f %s)"
                     % (C_LV, len(viol_lv), named_lv,
                        hg_caps[1][0], len(hg_caps[1][1]),
                        hg_caps[2][0], len(hg_caps[2][1]),
                        str(minA), C_NG, len(viol_ng), e_hg,
                        e_lv, e_ng, e_route,
                        "DECIDED" if decided else "UNDECIDED"))
        parts.append(verdict_main)
        parts.append("COMPOSITION(%s)" % comp_txt)
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the partition, the L1 "
          "recomposition, the two-ancestor bound, the cap "
          "chain, the Fractions toys, the tree logic and the "
          "purity audits (exact / AST-decided); MEASURED: every "
          "constant, violation count, census and exponent (the "
          "finite class ladder + 2 mains + 2 live controls); "
          "OPEN: any bound beyond the measured rungs, the "
          "cofinal law, the ladder-to-m_0* extrapolation, kz15 "
          "beyond r270; NO RH claim"
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
