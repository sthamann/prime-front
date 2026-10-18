#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""companion_orbit_packing_probe -- PRIME.TERMINAL.COMPANION_PACKING.01
(round 333): THE BETA/OMEGA COMPANION-ORBIT PACKING -- reviewer rank 1
after the r327 carrier finding.

CONTEXT (binding, from the sealed r327 record): on ALL 65 rungs the
heaviest group of the argmax block is EXACTLY ONE beta/omega fold
pair (one bulk + one window atom at one position, window-atom
histogram [0, 65, 0], median alignment 1.000); at kz53 the single
pair carries 88.8 percent of the argmax block's atom mass.  The
question is no longer "why is the profile broad?" but: WHY CAN A
SINGLE CANONICAL BULK/WINDOW PAIR NOT CARRY TOO LARGE A SHARE OF
THE TOTAL MASS?  The reviewer theorem candidate (beta-omega
companion packing): to every heavy group g* there exists a
companion set O(g*) CONSTRUCTED CANONICALLY FROM ITS SOURCE
POSITION with
  (T1) |O(g*)| >= c_0 m/(log m)^a,
  (T2) gabs(g) >= c_1/(log m)^b x gabs(g*) for every g in O(g*),
  (T3) overlap <= 2 (every source atom in at most two companions).
Then L1 >= (c_0 c_1/2) m/(log m)^{a+b} gabs(g*) forces q_max <=
C (log m)^{a+b}/m, hence M_3 <= q_max^2 and N_2 >= m/(C (log
m)^{a+b}) -- stronger than any needed power.  SUBCRITICAL ALSO
SUFFICES: hgn <= C m^delta with delta < 0.112 (with n_g = O(log m)
certified, the r327 banked C_NG).

THE CONSTRUCTION (binding -- from the SOURCE, NOT a similarity
search): for the dominant pair four data: (1) SOURCE SCALE = the
dyadic bin of its maximal ancestor atom, s* = floor(log2(vmax /
gmax(g*))) (QMO.scale_bins on the group gmax column, verbatim);
(2) FOLD PARITY = (window-atom count nwin, sign of the group value
G1); (3) POSITION relative to the window edge: gpos(g*) and its
distance to the masked support edges [pmin, pmax]; (4) its
beta/omega ancestor pair (bulk value, window value; printed).
COMPANIONS: O(g*) = all fold groups of the SAME source-scale bin
AND the SAME fold parity whose position lies in the MAXIMAL INNER
INTERVAL I = [pmin + BOUNDARY_F W, pmax - BOUNDARY_F W] (W = pmax
- pmin, BOUNDARY_F frozen a-priori).  INNER CASE: gpos(g*) in I
(g* is then its own companion); BOUNDARY CASE: gpos(g*) outside I
-- fewer companions, measured one-sidedly (census of same-key
groups on g*'s edge side), the finitely many head rungs typed
exactly.  THE BAND DISCIPLINE (the weight comparability NOT via
the global v_max -- that route failed in r327 -- but inside the
pre-defined dyadic source band): for two groups g, g' in the same
gmax bin s the EXACT algebra gmax in (vmax 2^{-(s+1)}, vmax
2^{-s}] together with the proven two-ancestor bound gmax <= gabs
<= 2 gmax forces
    1/4 < gabs(g)/gabs(g') < 4      (EXACT, Fractions-decided),
so T2 holds with c_1 = 1/4 and b = 0 AT THEOREM GRADE inside the
band; C_band <= 4 exact.  (T3) is partition algebra: the fold
groups partition the atoms (each atom in exactly one group, the
proven multiplicity <= 2), so every atom lies in at most ONE
companion of the single per-rung orbit -- overlap <= 2 holds with
reserve (measured membership 1, the theorem's factor-2 unused).

THE COMPOSED DETERMINISTIC CHAIN (exact algebra, warded live on
every live world):
    q_max = |x_{j*}|/L <= A1_{j*}/L <= ng_{j*} gabs(g*)/L
          = ng_{j*} (gabs(g*)/L1_atom) kappa
          <= ng_{j*} kappa / (|O| rmin)     =: Q_b
with rmin = min_{g in O} gabs(g)/gabs(g*) > 1/4 (band theorem),
L1_atom = sum_j A1_j >= sum_{g in O} gabs(g) >= |O| rmin gabs(g*)
(partition), and kappa = L1_atom/L >= 1 the measured global
cancellation transfer (block values, target-adjacent, computed
OUTSIDE the builders, disclosed).  The polylog question per rung:
is B_a = m Q_b/(log m)^{1+a} bounded (mid-ladder freeze, TRB
verbatim)?

THE FOUR MEASUREMENTS (sealed):
Q1 -- ORBIT CENSUS: |O| per rung, inner/boundary split, edge
   distance, T1 certification |O| (log m)^a/m >= c_0(a) (c_0 =
   min over the cal window; minimal a in A_FAM = (0, 1, 2)).
Q2 -- BAND RELATION: rmin and C_band per rung, the exact band
   ward (T2, theorem grade), the overlap census (T3, must be <=
   2, warded via the partition).
Q3 -- THE COMPOSED Q_MAX BOUND: Q_b per rung, the exact chain
   ward q_max <= Q_b, pointwise certification B_a <= C_Q(a)
   (max over cal, minimal a), named coverage kz53/kz83/kz67/kz55;
   the spike hardness test: at the named rungs, WHICH mechanism
   blocks -- orbit small (|O| below the ladder median) or band
   heavy (hgn above the median)?  SUBCRITICAL fallback: delta =
   e(hgn) (r272 dyadic halves-slope over test, fit-free) vs
   DELTA_CRIT = 0.112 with the halves stability rule.
Q4 -- WORLD CHECK: twin w13 (identical protocol, all exact wards
   live), EPSTEIN (different band structure -- band histogram
   census), SCRAMBLE (the orbit construction should decay --
   |O|/parity census); SMOOTH degenerate-skipped (pre-declared).

SEALED VERDICTS (exactly one fires; total order):
   TARGET_LEAK                    iff any purity/scope/literal
       audit hit on the orbit builders,
   WEIGHT_COMPARABILITY_FAIL      iff the exact band ward breaks
       on a live world (rmin <= 1/4 or C_band >= 4 beyond bar) or
       the overlap ward breaks (> 2) -- then the martingale
       second route is next (NAMED ONLY, not executed),
   COMPANION_PACKING_POLYLOG(a,b) iff T1 certifies at minimal a
       (0 test violations + named 4/4) AND the composed bound
       certifies at minimal a (0 test violations + named 4/4);
       b = 0 by the band theorem,
   BOUNDARY_FINITE_HEAD           iff not polylog and at a =
       max(A_FAM) EVERY T1/composed test violator is a
       boundary-case rung while the inner subset certifies (0
       inner violations + inner named coverage),
   COMPANION_PACKING_SUBCRITICAL(delta) iff not above and delta =
       e(hgn) < 0.112 DECIDED (both test halves agree),
   ORBIT_TOO_SHORT                otherwise (the honest rest:
       the orbit is too small at the named spikes or the
       exponent is undecided; rest printed).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: wave 13 (r329-r332, r334) runs in parallel; this
probe touches NOTHING outside its own file and the strictly
additive rh-sync (existing entries byte-identical).
EXT3 DISCLOSURE (git log checked at spec time): the r329 EXT3
probe is committed PRE-FREEZE ONLY (604b8aaf, no record commit)
-- the EXT3 anchors are NOT adopted; the ladder is the sealed 65
(42 + 15 ext + 8 ext2, r316/r324/r327 verbatim).

THE OBJECT (r269/r287/r298/r306/r314/r316/r324/r327 machinery
imported verbatim): t_{N-2} = sum_b ct_b (r244 chain rows, r266
eval); F = 0.20 edge split; maximal same-sign runs of the
bx-sorted bulk; level-2 blocks (r270 convention); the frozen
positional block machinery (r298); the r306 RY3.cubic_moments +
RY3.renyi3_ratio + RY3.calib_freeze; the r314 SCF.fold_genealogy
+ SCF.signed_cube_terms + SCF.flux_telescope; the r316
TRB.two_regime_state + TRB.split_midladder; the r324
QMO.scale_bins + QMO.mult_ward; the r324-pre FAP.m2_qmax_state;
the r327 GMC.group_mass_ledger (cross-ward only); PDelta = Pbeta
- Pomega; x_j = (PDelta)_j.  NEW in this round (module-own,
source-pure): orbit_ledger (the r327 group ledger EXTENDED by the
group position gpos on the identical fold segmentation),
dominant_state (the argmax-block dominant pair with its four
source data; the argmax access is the same class as the r324
pileup_state, disclosed), companion_orbit (the sealed canonical
companion selection: ledger + key + inner interval ONLY -- no
block value, no q_max, no target) and the sealed packing_tree.

LEG 0 -- ANCHOR REGRESSION (slim set + the r327 record,
disclosed): the r314 identity wards live; r306 C_2 = 1.069 (tol
0.005) first-5 freeze, 0/57; r316 rho anchors kz53/kz67/kz55/
kz83 = 1.0490/1.0536/0.4821/0.7790 (tol 0.005) + C_small 1.0694
at kz18 + n = 65; r327 RECORD anchors reproduced bit-near:
C_NG 2.6351 (tol 0.005) with 0/39 test violations + named 4/4,
window-atom histogram of the heavy group == (0, 65, 0) EXACT,
kz53 bshare 0.888 (tol 0.02), ladder gap med 0.807 (tol 0.005),
align med 1.000 (tol 0.005), position thirds (21, 29, 15) EXACT.

LEG A -- SEAL + PURITY + TOYS + LIVE WARDS: (A1) sealed
definitions printed; the SOURCE-PURE table (rank, kz, N, m, G,
ng, hgn, |O|, rmin, cband, kappa, Q_b, B_1, case, s*, parity,
d*) printed BEFORE any certification table.  (A2) SOURCE-PURITY
AUDITS: the AST identifier scan over orbit_ledger +
dominant_state + companion_orbit + packing_tree must be clean
against BOUND_FORBIDDEN + PHI3_FORBIDDEN + QMAX_FORBIDDEN (no
M_3 read-back, no terminal value, no q_max record read-back --
the orbit is sealed BEFORE any q_max sight: the companion
selection consumes group scale bins / parities / positions /
the inner interval ONLY); the literal scan over the builders
must be clean against the sealed record-literal set
R333_TABLE_LITERALS (the r314..r324 set UNION the r327 record
numbers); e1/e2 prove the audits bite.  (A3) TOY EXACTNESS
(Fractions): the five-block orbit toy (vmax 5; g* = pair (5, 3)
at 0.5 bin 0 parity (1, +); companion pair (9/2, 3) at 0.45 bin
0 SAME parity; wrong-parity pair (-23/5, -3) at 0.48 EXCLUDED;
light atoms (1) at 0.1/0.9 bin 2 EXCLUDED): O = {g*, c} EXACT,
rmin = 15/16, cband = 16/15, chain q_max = 80/251 <= Q_b = 8/15
with slack EXACT; the band-extremes toy (gmax 8 with gabs 16 vs
gmax 33/8 with gabs 33/8, both bin 0): ratio 33/128 > 1/4 with
margin 1/128 EXACT (the band theorem is sharp near 1/4); the
overlap toy: membership 1 on every atom, the triple-assignment
mutant REFUSED (3 > 2, break 1 EXACT); the similarity mutant
returns {wrong-parity, companion} != the canonical orbit
(set-mismatch CAUGHT); packing_tree all six branches EXACT.
(A4) LIVE WARDS on every live world: the r316 chain + NORM x
cube == rho_2 (r327 verbatim); the S0 interpolation; ledger ==
genealogy (G1/mult/gblk) + gpos sorted within blocks + ledger ==
the r327 GMC ledger EXACT; the partition sum_g gabs == A1_j; THE
BAND WARD rmin > 1/4 and cband < 4 on every orbit (bar BAND_TOL
relative); THE OVERLAP WARD membership <= 2 (measured 1); THE
COMPOSED CHAIN q_max <= A1*/L <= ng hga/L AND q_max <= Q_b
(exact algebra, bar CHAIN_BAR); kappa >= 1; the fold
multiplicity <= 2 admitted (QMO.mult_ward verbatim).

LEG B -- Q1/Q4 ORBIT CENSUS: |O| ladder statistics, inner/
boundary split census (count, kz list, one-sided companion
count for boundary rungs), edge-distance statistics, the named
spike anatomy (|O|, rmin, band, mechanism letter SMALL_ORBIT /
HEAVY_BAND / COVERED per named rung, measurement only), the
world table (twin/EPSTEIN/SCRAMBLE orbit + band census).

LEG C -- Q2/Q3 CERTIFICATION (mid-ladder freeze, TRB verbatim):
T1 c_0(a) = min cal |O| (log m)^a/m, test violations, named,
minimal a; T2 the exact band theorem (b = 0, c_1 = 1/4) gated as
live ward; composed C_Q(a) = max cal B_a, test violations,
named, minimal a; exponents e(hgn) vs DELTA_CRIT = 0.112 and
e(B_1) (census) with the halves stability rule.

LEG D -- COMPOSITION (printed ALWAYS, honestly typed): on the
polylog branch: q_max <= C_Q (log m)^{1+a}/m pointwise =>
M_3 <= q_max M_2 <= q_max^2 (S0 exact) => N_2 >= 1/q_max >=
m/(C_Q (log m)^{1+a}) => N_2 >= m^0.888 for all m >= m_0*
(log-space solve of m^{0.112} >= C_Q (log m)^{1+a}) => the r297
target chain; on the subcritical branch: m q_max <= ng hgn <=
C_NG C log m m^{delta}, N_2 >= m^{1-delta}/(C_NG C log m),
delta < 0.112 => N_2 >= m^0.888 asymptotically; else the r324
MEASURED composition restated unchanged with the measured
orbit-route envelopes printed.

LEG E -- WARDS / MUST-FAILS (>= 4 mutants + 2 scope mutants):
(e1) ORBIT CONSTRUCTION AFTER Q_MAX SIGHT: mutant_orbit_posthoc
  consumes the q_max record (trs/qmax) as an 'orbit coordinate'
  -- the QMAX_FORBIDDEN scan must FLAG it (AST-CAUGHT) while the
  module-own builders stay clean.
(e2) BAND BOUNDARIES AFTER SIGHT: mutant_band_posthoc widens the
  band width until every seen violator is covered (consumes rho)
  -- the BOUND_FORBIDDEN scope audit must FLAG it AND on the
  sealed toy it returns width 2 != the canonical rule's 0 --
  CAUGHT twice.
(e3) SYNTHETIC OVERLAP BREAK: mutant_overlap_triple presents a
  membership census with one atom in THREE companions -- the
  overlap ward must REFUSE it (3 > 2, break 1 EXACT) while every
  live orbit passes at membership 1 -- LOUD.
(e4) COMPANION SELECTION VIA SIMILARITY SEARCH:
  mutant_similarity_pick selects the k groups nearest in |gabs -
  gabs(g*)| (a value-side similarity search, ignoring scale /
  parity / position) -- on the sealed toy it returns a set
  containing the wrong-parity group and differing from the
  canonical source orbit (exact set mismatch) -- CAUGHT.
(m5a/m5b) WORLD-BLINDNESS BREAK: a builder consuming the withheld
  terminal drive key and a builder consuming the branch label are
  both FLAGGED by the AST scope audit.

INDEX FIREWALL (binding, r238-r327 discipline): w = window (kz),
N_w = builder depth, k/n = chain degree; ground truth (branch
labels, the true R/t/Z values) enters GATES and census tables
only; the cubic target M_3 / rho_2 and the q_max RECORD enter
GATES / anchors / composition checks only, NEVER an orbit
builder (AST-warded); kappa = L1_atom/L consumes block values
and is computed OUTSIDE the builders (target-adjacent,
disclosed -- the same access class as the r324 pileup chain);
no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit; the growth exponents are the
imported r272 dyadic halves-slope, fit-free).  MACHINERY
IMPORTED VERBATIM: r327 GMC.group_mass_ledger (cross-ward),
r324 QMO.scale_bins + QMO.mult_ward, r324-pre FAP.m2_qmax_state,
r316 TRB.two_regime_state + TRB.split_midladder, r314
SCF.fold_genealogy + SCF.signed_cube_terms + SCF.flux_telescope,
r306 RY3.cubic_moments + RY3.renyi3_ratio + RY3.calib_freeze,
r298 WBT.block_breaks + WBT.aggregate_blocks, r269 PBB.mask_edge
+ PBB.runs_split, r287 L2D.blocks_level2 + L2D.halves_slope +
L2D.autocorr_full, r244 BH.wpack, r257 CT.union_arrays, r260
TX.drive_arrays, r263 CA.g_gap, r266 BR.eval_scaled, v881 PIK,
r243 PB.smooth_comb.  B PROVENANCE: B_w = S_{N-2} + 5/7
(r241/r243 IMPORTED floor, never fitted).  COFINAL LADDER
(pre-sealed, r316/r324/r327 verbatim): frame-A h <= 900, 42
rungs, (N, kz)-sorted; exception set {kz15, 20, 22, 36, 38, 39,
52}; EXTENSION: 900 < h <= 1300, first 15 by (N, kz); EXT2: the
r316 A5 rule (leftover pool + first 12 windows 1300 < h <= 1650,
first 8 POSITIVE_PREFIX by (N, kz)); NO EXT3 (disclosed above).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); EDGE_F 0.20 (FROZEN); PAIR_OFFSET 0 (FROZEN);
EXT_H_MAX 1300; K_EXT 15; EXT_NW_EXPECT (942, 1218); EXT2_H_MAX
1650; EXT2_POOL_CAP 12; K_EXT2 8; ATOM_BAR 1e-9; REC3_BAR 1e-13;
TEL_BAR 1e-13; BND_BAR 1e-13; CHAIN_BAR 1e-9; SA_BAR 1e-12;
DEG_FLOOR 1e-6; MULT_CAP 2; N_CAL 5 (via TRB, verbatim);
BOUNDARY_F 0.10 (a-priori); A_FAM (0, 1, 2); RBAND_MIN 1/4
(exact algebra); CBAND_MAX 4 (exact algebra); BAND_TOL 1e-9;
OVERLAP_CAP 2; DELTA_CRIT 0.112 (the reviewer budget verbatim);
N2_EXP_NEED 0.888; NEED_SLOPE 0.908; SIGMA_STAR -0.516;
DELTA_NEED 0.21; NAMED_KZ (53, 83, 67, 55); NAMED_HV_KZ (53, 83,
67); MUT_MIN 1e-6; TOY_BAR 1e-12; FR_BAR 1e-14; TB_WARD bars
1e-9 main N <= 400 / 3e-6 deep + ext + ext2 / 1e-6 controls;
ID_BAR 1e-12; AC_BAR 1e-9; INF_SENT 1e300 / cert guard 1e299;
R306 anchor C_2 1.069 tol 0.005; N333_REF 65; R316 RHO {53:
1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790} tol 0.005, C_SMALL
1.0694 tol 0.005 at kz18; R327 anchors C_NG 2.6351 tol 0.005
viol 0 named 4/4, NWIN_HIST (0, 65, 0) EXACT, kz53 BSHARE 0.888
tol 0.02, GAP_MED 0.807 tol 0.005, ALIGN_MED 1.000 tol 0.005,
THIRDS (21, 29, 15) EXACT; R333_TABLE_LITERALS = the sealed
r314..r324 + r324-record set (r327 verbatim) UNION the r327
record set {2.6351, 0.807, 0.888, 0.076, 0.416, 1.057, 1.081,
0.46, 2.616, 0.106, 0.411, -1.183, -0.2, -0.261, 0.293, 0.9143,
0.2047, 1.1838, 6.853, 5.766, 4.609, 4.132, 0.652};
runtime <= 1800 s; smoke = w9 + controls + toys + scope/purity
audits + the ledger/band/overlap/chain wards on w9 + controls +
e1-e4 mutants; ladder, extensions, anchors, census,
certification, exponents and adjudication skipped.
DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe): every
anchor band is an r306/r316/r327 RECORD number adopted as-is
(incl. the known r327 anatomy: the dominant group is ALWAYS one
beta/omega fold pair, kz53 bshare 0.888, mid-heavy thirds); the
band theorem (1/4 < ratio < 4 inside one dyadic gmax bin), the
partition/overlap algebra and the composed chain q_max <= ng
kappa/(|O| rmin) are derived algebra, disclosed above;
GENUINELY OPEN quantities of this round: every orbit column
(|O|, rmin, cband, kappa, Q_b, B_a, case, d*), all
certification constants c_0(a)/C_Q(a), all violation counts,
the boundary census, the named-spike mechanism letters, the
world censuses and both growth exponents -- NONE was computed
before this spec was frozen; BOUNDARY_F = 0.10, A_FAM =
(0, 1, 2) and DELTA_CRIT = 0.112 are a-priori (the reviewer
budget verbatim); the six sealed letters are symmetric and
total -- the tree maps every outcome to exactly one letter by
CONTRACT.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  R333_ANCHORS(identity wards, r306 C_2, r316 rho + C_small + n,
    r327 C_NG + nwin hist + bshare + gap/align/thirds)
+ SEAL(ledger wards + partition + band theorem + overlap +
    composed chain + purity audits + toys)
+ ORBIT(census: |O| stats, inner/boundary split, edge distance,
    named anatomy + mechanism letters, world table)
+ CERT(T1 c_0(a) + violations + named + minimal a; T2 band b=0
    exact; composed C_Q(a) + violations + named + minimal a;
    e(hgn) vs 0.112, stability)
+ [exactly one of] COMPANION_PACKING_POLYLOG /
    BOUNDARY_FINITE_HEAD / COMPANION_PACKING_SUBCRITICAL /
    ORBIT_TOO_SHORT / WEIGHT_COMPARABILITY_FAIL / TARGET_LEAK
+ COMPOSITION(the recomposed chain with explicit constants;
    printed ALWAYS, typed)
+ MUSTFAIL_LEDGER(e1-e4 + scopes).
Honesty before beauty: the band theorem, the partition/overlap
algebra, the composed chain, the Fractions toys, the tree logic
and the purity audits are EXACT (Fractions/AST-decided); every
census, constant, violation count and exponent is MEASURED on
the finite ladder only; a certifying letter fixes a proof
TARGET, it proves NO cofinal law; kappa is a measured
target-adjacent transfer factor, disclosed as the honest gap of
the composed chain; the r327 record numbers are disclosed
pre-spec inputs; r243-r332 stand.

RECORD TABLES (inserted AFTER the record run -- the only
amendment after freeze; freeze SPEC_SHA 5567af41c0d4bc82;
protocol: smoke pass 1 = 34/34 (0.5 s), NO amendment;
calibration pass 1 = first full evaluation, 34/34, wall 36.9 s,
NO amendment; record run1/run2 after this insertion, identical
up to the runtime line):
MAIN VERDICT: ORBIT_TOO_SHORT(T1 fails at all a in (0, 1, 2);
composed bound fails at all a; exponent halves straddle
+0.148/+0.674, delta -0.004 < 0.112 UNDECIDED by the sealed
stability rule) -- the r324 MEASURED composition (m_0* 10^59.6)
stays the honest state of the route.  THE STRUCTURAL FINDING OF
THE ROUND: THE BOUNDARY CASE IS THE RULE, NOT THE EXCEPTION --
on 44/65 rungs the dominant beta/omega pair sits in the outer
BOUNDARY_F = 0.10 margin of the masked support (edge distance
d* med 0.072, min 0.002), so the inner-interval orbit is EMPTY
at three of the four named spikes (kz53/kz83/kz55: |O| = 0;
kz67: |O| = 2) while the ONE-SIDED census shows same-key
companions DO exist on the edge side (kz53: 1, kz83: 1, kz55:
1, up to 25 at kz37) -- the reviewer's inner/boundary split is
real but inverted in frequency: the spike coincidence is an
EDGE phenomenon, and any viable packing theorem must be stated
one-sidedly at the edge, not on the inner interval.
T2/T3 AT THEOREM GRADE (the round's positive): the BAND
DISCIPLINE CERTIFIES EXACTLY -- rmin worst 0.2819 > 1/4 and
cband worst 3.5473 < 4 on every live orbit (69 worlds; the
Fractions extremes toy shows sharpness near 1/4: the measured
0.2819 sits 11 percent above the algebraic floor); the OVERLAP
ward is partition-exact (max membership 1 <= 2, the factor-2
reserve unused); the composed chain q_max <= A1*/L <= ng hga/L
<= Q_b = ng kappa/(|O| rmin) has worst slack violation 0.0
(exact algebra live).
CERT (mid-ladder freeze, 39 test rungs): T1 min-cal c_0 =
0.0238/0.1055/0.4674 at a = 0/1/2 with 18/17/15 violations,
named 0/4 -> minimal a None; composed max-cal C_Q =
233.66/54.46/12.69 at a = 0/1/2 with 19/14/10 violations,
named 0/4 -> minimal a None (worst violators kz53/kz70/kz83 at
the |O| = 0 sentinel, then kz76 44.8 / kz38 37.5 / kz100
25.3); |O| med 5 min 0 max 52, |O|/m med 0.051; kappa med ~3.4
min 3.1836 max 6.7 (the L-cancellation transfer is a stable
factor ~3-4, NOT the blocker); delta = e(hgn) = -0.004 (halves
+0.148/+0.674 STRADDLE -- the deep half RISES here, measured
honestly against the r327 falling hgn/log m).
SPIKE HARDNESS TEST: all four named rungs are SMALL_ORBIT +
HEAVY_BAND simultaneously (hgn 14.89/13.43/10.30/15.17 vs med
3.70 AND |O| 0/0/2/0 vs med 5, all at s* = 0, three of four in
case B) -- BOTH mechanisms fire together at the spikes: the
heavy pair is a bin-0 edge coincidence with (almost) no
same-key inner companion.
WORLDS: twin w13 runs the identical sealed construction (|O|
3, rmin 0.443, case B -- same protocol, all exact wards live);
EPSTEIN: 10 occupied bands vs w9 13, live orbit |O| 7 (the
band structure differs but the construction operates); SCRAMBLE
|O| = 0 (case B) -- THE ORBIT CONSTRUCTION DECAYS ON SCRAMBLE
as predicted while w9 holds |O| = 6.
ANCHORS bit-near: r314 identity 4.5e-17; r306 C_2 1.069
(0/57); r316 n 65 + rho quartet + C_small 1.0694@kz18; r327
C_NG 2.6351 (0 viol, named 4/4) + nwin histogram (0, 65, 0)
EXACT + kz53 bshare 0.888 + gap med 0.807 + align med 1.000 +
thirds (21, 29, 15) EXACT.
SEAL: partition 3.4e-16, ledger == genealogy == GMC 0.0,
overlap 1, chain 0.0, purity clean, toys exact; must-fails e1
AST-CAUGHT (trs) / e2 CAUGHT twice (AST rho + toy width 2 !=
0) / e3 LOUD (break 1 EXACT, 3 > 2 REFUSED) / e4 CAUGHT (toy
set mismatch, wrong-parity pick) + m5a/m5b FLAGGED.

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
BOUNDARY_F = 0.10
A_FAM = (0, 1, 2)
RBAND_MIN = 0.25
CBAND_MAX = 4.0
BAND_TOL = 1e-9
OVERLAP_CAP = 2
DELTA_CRIT = 0.112
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
INF_SENT = 1e300
CERT_GUARD = 1e299
R306_C2 = 1.069
R306_C2_TOL = 0.005
N333_REF = 65
R316_RHO = {53: 1.0490, 67: 1.0536, 55: 0.4821, 83: 0.7790}
R316_RHO_TOL = 0.005
R316_CSMALL = 1.0694
R316_CSMALL_TOL = 0.005
R316_CSMALL_KZ = 18
R327_CNG = 2.6351
R327_CNG_TOL = 0.005
R327_VNG = 0
R327_NWIN_HIST = (0, 65, 0)
R327_BSHARE53 = 0.888
R327_BSHARE_TOL = 0.02
R327_GAP_MED = 0.807
R327_GAP_TOL = 0.005
R327_ALIGN_MED = 1.000
R327_ALIGN_TOL = 0.005
R327_THIRDS = (21, 29, 15)
R333_TABLE_LITERALS = frozenset(GMC.R327_TABLE_LITERALS | {
    2.6351, 0.807, 0.888, 0.076, 0.416, 1.057, 1.081, 0.46,
    2.616, 0.106, 0.411, -1.183, -0.2, -0.261, 0.293, 0.9143,
    0.2047, 1.1838, 6.853, 5.766, 4.609, 4.132, 0.652})

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
    lies in the sealed r314..r327 record set."""
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
                            in R333_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders.  Source-pure: the orbit
# ---------------- builders consume atom values / positions / block
# ---------------- assignments / source flags / group order / the
# ---------------- inner interval ONLY; the withheld terminal drive
# ---------------- key, the branch label, the cubic target M_3 and
# ---------------- the q_max RECORD are forbidden (AST identifier
# ---------------- scan + literal scan).  The dominant-pair argmax
# ---------------- access is the r324 pileup_state class, disclosed.
def orbit_ledger(pos, val, blk, src, m):
    """the r327 group ledger EXTENDED by the group position on the
    identical fold segmentation (same lexsort key (block,
    position)): per fold group g returns the signed value G1_g,
    the abs atom mass gabs_g, the maximal atom magnitude gmax_g,
    the multiplicity mult_g, the window-atom count gwin_g, the
    block index gblk, the POSITION gpos_g and the block slice
    pointers ptr; plus the rung-global maximal atom magnitude
    vmaxw and the masked support edges pmin/pmax.  Consumes atom
    positions + values + block assignments + source flags only."""
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
    gpos = pp[new] if ng else np.zeros(0)
    if ng:
        starts = np.nonzero(new)[0]
        gmax = np.maximum.reduceat(av, starts)
    else:
        gmax = np.zeros(0)
    ptr = np.searchsorted(gblk, np.arange(m + 1))
    vmaxw = float(np.max(av)) if len(av) else 0.0
    pmin = float(np.min(pos)) if len(pos) else 0.0
    pmax = float(np.max(pos)) if len(pos) else 0.0
    return dict(G1=G1, gabs=gabs, gmax=gmax, gwin=gwin, mult=mult,
                ng=ng, gblk=gblk, gpos=gpos, ptr=ptr, vmaxw=vmaxw,
                pmin=pmin, pmax=pmax)


def dominant_state(x, led, sbins):
    """the ARGMAX-BLOCK dominant pair with its four source data:
    on block values x (length m), an orbit_ledger led and the
    group scale-bin column sbins: j* = argmax |x|, L = sum |x|;
    the heaviest group of j* (by gabs) is the dominant pair;
    returns its global group index gi, hga = gabs(g*), its scale
    bin sb, its fold parity (nw = window-atom count, sg = sign of
    G1), its position ps and edge distance d, the inner interval
    [ilo, ihi] (BOUNDARY_F rule), the case flag inner, plus
    ng_{j*}, hgn = m hga/L and bshare.  Consumes block values +
    the ledger only (the argmax access is the r324 pileup_state
    class, disclosed)."""
    ax = np.abs(np.asarray(x, dtype=float))
    m = int(len(ax))
    tot = float(np.sum(ax))
    W = led["pmax"] - led["pmin"]
    ilo = led["pmin"] + BOUNDARY_F * W
    ihi = led["pmax"] - BOUNDARY_F * W
    if m < 2 or tot <= 0.0 or led["ng"] == 0:
        return dict(j=0, gi=-1, ngj=0, hga=0.0, gmaxs=0.0, sb=-1,
                    nw=0, sg=0.0, ps=0.0, d=0.0, ilo=ilo, ihi=ihi,
                    inner=False, hgn=0.0, bshare=0.0, a1j=0.0,
                    bulkv=0.0, winv=0.0)
    j = int(np.argmax(ax))
    a, b = int(led["ptr"][j]), int(led["ptr"][j + 1])
    ga = led["gabs"][a:b]
    ngj = b - a
    if ngj == 0:
        return dict(j=j, gi=-1, ngj=0, hga=0.0, gmaxs=0.0, sb=-1,
                    nw=0, sg=0.0, ps=0.0, d=0.0, ilo=ilo, ihi=ihi,
                    inner=False, hgn=0.0, bshare=0.0, a1j=0.0,
                    bulkv=0.0, winv=0.0)
    i1 = int(np.argmax(ga))
    gi = a + i1
    hga = float(led["gabs"][gi])
    gmaxs = float(led["gmax"][gi])
    nw = int(round(float(led["gwin"][gi])))
    sg = float(np.sign(led["G1"][gi]))
    ps = float(led["gpos"][gi])
    d = min(ps - led["pmin"], led["pmax"] - ps)
    a1j = float(np.sum(ga))
    # ancestor pair (printed data): with mult <= 2 the pair is
    # (the gmax carrier, the other atom) in abs mass.
    otherv = hga - gmaxs
    return dict(j=j, gi=gi, ngj=ngj, hga=hga, gmaxs=gmaxs,
                sb=int(sbins[gi]), nw=nw, sg=sg, ps=ps, d=d,
                ilo=ilo, ihi=ihi, inner=bool(ilo <= ps <= ihi),
                hgn=float(m) * hga / tot,
                bshare=hga / max(a1j, 1e-300), a1j=a1j,
                bulkv=gmaxs, winv=otherv)


def companion_orbit(led, sbins, sb, nw, sg, ilo, ihi):
    """the SEALED CANONICAL COMPANION SELECTION (source-pure,
    sealed BEFORE any q_max sight): all fold groups of the SAME
    source-scale bin sb AND the SAME fold parity (window-atom
    count nw, group-value sign sg) whose position lies in the
    maximal inner interval [ilo, ihi] and whose abs mass is
    positive.  Consumes the ledger + the key + the interval ONLY
    -- no block value, no target, no record."""
    gw = np.round(led["gwin"]).astype(int)
    sel = ((sbins == sb) & (gw == nw)
           & (np.sign(led["G1"]) == sg)
           & (led["gpos"] >= ilo) & (led["gpos"] <= ihi)
           & (led["gabs"] > 0.0))
    return np.nonzero(sel)[0]


def packing_tree(leak, wfail, polylog, bhead, subcrit):
    """the sealed six-letter verdict tree (booleans only; total,
    exactly one fires; order sealed):
    TARGET_LEAK > WEIGHT_COMPARABILITY_FAIL >
    COMPANION_PACKING_POLYLOG > BOUNDARY_FINITE_HEAD >
    COMPANION_PACKING_SUBCRITICAL > ORBIT_TOO_SHORT."""
    if leak:
        return "TARGET_LEAK"
    if wfail:
        return "WEIGHT_COMPARABILITY_FAIL"
    if polylog:
        return "COMPANION_PACKING_POLYLOG"
    if bhead:
        return "BOUNDARY_FINITE_HEAD"
    if subcrit:
        return "COMPANION_PACKING_SUBCRITICAL"
    return "ORBIT_TOO_SHORT"


def mutant_orbit_posthoc(state):
    """e1 MUST-FAIL MUTANT: an 'orbit coordinate' consuming the
    q_max RECORD (the target-side concentration coordinate) --
    the QMAX_FORBIDDEN identifier scan must FLAG this (the orbit
    must be sealed BEFORE any q_max sight)."""
    tr = state["trs"]
    return float(tr["qmax"]) * float(state["m"])


def mutant_band_posthoc(sb_col, rho, cbar):
    """e2 MUST-FAIL MUTANT: the band width re-picked AFTER SIGHT
    of the violators (consumes rho): widened until every seen
    violator's bin is covered -- the BOUND_FORBIDDEN scope audit
    must FLAG it AND on the sealed toy it returns != the
    canonical same-bin rule's width 0."""
    worst = max((abs(int(s)) for s, r in zip(sb_col, rho)
                 if r > cbar), default=0)
    return worst


def mutant_overlap_triple():
    """e3 MUST-FAIL MUTANT: a synthetic membership census with one
    atom in THREE companions -- the overlap ward must REFUSE it
    (3 > OVERLAP_CAP, break 1 EXACT)."""
    return (1, 1, 3)


def mutant_similarity_pick(gabs_col, target, k):
    """e4 MUST-FAIL MUTANT: companion selection via a VALUE-SIDE
    SIMILARITY SEARCH (the k groups nearest in |gabs - target|,
    ignoring scale / parity / position) -- on the sealed toy it
    returns a set differing from the canonical source orbit
    (exact set mismatch, CAUGHT)."""
    d = [(abs(float(g) - float(target)), i)
         for i, g in enumerate(gabs_col)]
    d.sort()
    return tuple(sorted(i for _v, i in d[:k]))


def mutant_gift_bound(rc, P):
    """m5a MUST-FAIL MUTANT: an 'orbit orientation' consuming the
    withheld ground-truth terminal drive key -- the scope audit
    must FLAG this."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m5b MUST-FAIL MUTANT (world-blindness break simulated): an
    'orbit constant' consuming the branch label -- the scope
    audit must FLAG this."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- exact Fractions section: the orbit toy, the band
# ---------------- theorem and the composed chain decided as
# ---------------- rationals
def fr_orbit_toy():
    """the sealed five-block orbit toy in exact Fractions:
    atoms -- block 0: bulk 5 + window 3 at pos 1/2 (g*); block 1:
    bulk 9/2 + window 3 at pos 9/20 (companion c); block 2: bulk
    -23/5 + window -3 at pos 12/25 (wrong parity); block 3: bulk
    1 at pos 1/10; block 4: bulk 1 at pos 9/10.  vmax = 5; bins:
    gmax 5 -> 0, 9/2 -> 0, 23/5 -> 0, 1 -> 2 (5/1 = 5, floor
    log2 = 2).  W = 4/5, I = [9/50, 41/50]: g* and c and the
    wrong-parity group inside, the light atoms outside.  Orbit
    key (bin 0, nwin 1, +): O = {g*, c} EXACT; rmin = (15/2)/8 =
    15/16; cband = 16/15; x = (8, 15/2, -38/5, 1, 1), L =
    251/10, q_max = 80/251; ng(j*) = 1, kappa = 1, Q_b = 1/(2 x
    15/16) = 8/15; chain slack Q_b - q_max = 8/15 - 80/251 =
    808/3765 EXACT > 0.  The similarity mutant (k = 2, target 8
    over the group gabs list) picks {c, wrong-parity} != O.
    Returns (worst dev, chain slack, orbit set ok, mutant set
    mismatch ok)."""
    gabs = (Fr(8), Fr(15, 2), Fr(38, 5), Fr(1), Fr(1))
    x = (Fr(8), Fr(15, 2), Fr(-38, 5), Fr(1), Fr(1))
    L = sum(abs(v) for v in x)
    qmx = max(abs(v) for v in x) / L
    rmin = (Fr(15, 2)) / Fr(8)
    cband = Fr(8) / Fr(15, 2)
    ngj = Fr(1)
    kap = Fr(1)
    nO = Fr(2)
    Qb = ngj * kap / (nO * rmin)
    slack = Qb - qmx
    devs = [abs(L - Fr(251, 10)), abs(qmx - Fr(80, 251)),
            abs(rmin - Fr(15, 16)), abs(cband - Fr(16, 15)),
            abs(Qb - Fr(8, 15)), abs(slack - Fr(808, 3765)),
            Fr(0) if qmx <= Qb else Fr(1),
            Fr(0) if rmin > Fr(1, 4) else Fr(1),
            Fr(0) if cband < Fr(4) else Fr(1)]
    # float construction cross-check via the real builders:
    pos = np.array([0.5, 0.5, 0.45, 0.45, 0.48, 0.48, 0.1, 0.9])
    val = np.array([5.0, 3.0, 4.5, 3.0, -4.6, -3.0, 1.0, 1.0])
    blk = np.array([0, 0, 1, 1, 2, 2, 3, 4])
    srcf = np.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0])
    led = orbit_ledger(pos, val, blk, srcf, 5)
    sbins = QMO.scale_bins(led["gmax"])
    xs = np.array([8.0, 7.5, -7.6, 1.0, 1.0])
    ds = dominant_state(xs, led, sbins)
    orb = companion_orbit(led, sbins, ds["sb"], ds["nw"],
                          ds["sg"], ds["ilo"], ds["ihi"])
    # expected orbit = the groups of block 0 and block 1
    exp = tuple(sorted(int(i) for i in np.nonzero(
        (led["gblk"] == 0) | (led["gblk"] == 1))[0]))
    orb_ok = (tuple(sorted(int(i) for i in orb)) == exp
              and ds["inner"] and ds["sb"] == 0 and ds["nw"] == 1
              and ds["sg"] > 0 and ds["ngj"] == 1)
    mut = mutant_similarity_pick([float(g) for g in gabs],
                                 8.0, 2)
    # nearest to 8 among (8, 7.5, 7.6, 1, 1) excluding self-dist 0
    # is {0 (self), 2 (wrong parity 7.6)} -- differs from the
    # canonical orbit {0, 1} -> exact set mismatch
    mut_ok = (mut != exp and 2 in mut)
    return max(devs), slack, orb_ok, mut_ok


def fr_band_toy():
    """the band-extremes toy: bin 0 of vmax = 8 is gmax in (4, 8];
    g with gmax 8 and gabs 16 (= 2 gmax, the two-ancestor
    maximum) vs g' with gmax 33/8 and gabs 33/8 (mult 1): ratio
    (33/8)/16 = 33/128 > 1/4 = 32/128 with margin 1/128 EXACT --
    the band theorem is sharp near 1/4; cband = 16/(33/8) =
    128/33 < 4 with margin 4/33 EXACT.  Returns worst dev."""
    r = Fr(33, 8) / Fr(16)
    cb = Fr(16) / Fr(33, 8)
    return max(abs(r - Fr(33, 128)),
               abs(r - Fr(1, 4) - Fr(1, 128)),
               abs(cb - Fr(128, 33)),
               abs(Fr(4) - cb - Fr(4, 33)),
               Fr(0) if r > Fr(1, 4) else Fr(1),
               Fr(0) if cb < Fr(4) else Fr(1))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("companion_orbit_packing_probe -- "
          "PRIME.TERMINAL.COMPANION_PACKING.01 (round 333, "
          "reviewer rank 1)")
    print("SPEC_SHA %s   R327_SHA %s   R324_SHA %s   R314_SHA %s"
          % (SPEC_SHA[:16], GMC.SPEC_SHA[:16], QMO.SPEC_SHA[:16],
             SCF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 + controls + toys + scope/"
                        "purity audits + ledger/band/overlap/"
                        "chain wards + e1-e4; ladder, "
                        "extensions, anchors, census, "
                        "certification and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "THE COMPANION-ORBIT PACKING ROUND (the r327 carrier "
          "follow-up): for every rung the dominant beta/omega "
          "pair g* is identified (r327 machinery) and its "
          "companion orbit O(g*) constructed CANONICALLY FROM "
          "THE SOURCE (same dyadic gmax bin + same fold parity "
          "(nwin, sign) + the maximal inner interval, BOUNDARY_F "
          "%.2f) -- NOT a similarity search; (T1) |O| >= c_0 "
          "m/(log m)^a (A_FAM %s, min-cal freeze), (T2) the "
          "BAND THEOREM 1/4 < gabs/gabs(g*) < 4 exact inside "
          "one bin (b = 0), (T3) overlap <= %d via the "
          "partition; composed chain q_max <= ng kappa/(|O| "
          "rmin) warded exact; verdict tree TARGET_LEAK / "
          "WEIGHT_COMPARABILITY_FAIL / COMPANION_PACKING_"
          "POLYLOG / BOUNDARY_FINITE_HEAD / COMPANION_PACKING_"
          "SUBCRITICAL / ORBIT_TOO_SHORT sealed BEFORE "
          "evaluation (DELTA_CRIT %.3f the reviewer budget "
          "verbatim); EXT3 NOT adopted (r329 record uncommitted "
          "at spec time, disclosed)"
          % (BOUNDARY_F, str(A_FAM), OVERLAP_CAP, DELTA_CRIT))
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in ("orbit_ledger", "dominant_state", "companion_orbit",
               "packing_tree"):
        sc_own += scope_audit(fn, BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, QMAX_FORBIDDEN)
    sc_a = scope_audit("mutant_gift_bound", BOUND_FORBIDDEN)
    sc_b = scope_audit("mutant_branch_peek", BOUND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_a) >= 1 and len(sc_b) >= 1,
          "fragment audit clean (%d hits); the four module-own "
          "orbit builders/trees clean vs BOUND_FORBIDDEN + "
          "PHI3_FORBIDDEN + QMAX_FORBIDDEN (%d hits) -- the "
          "companion selection consumes ONLY group scale bins / "
          "parities / positions / the inner interval (sealed "
          "BEFORE any q_max sight); m5a gift-bound FLAGGED (%s); "
          "m5b branch-peek FLAGGED (%s)"
          % (len(frag), len(sc_own),
             sc_a[0] if sc_a else "MISS",
             sc_b[0] if sc_b else "MISS"))

    # ---------------- S1: census + controls (r327 scaffold verbatim)
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
              "selected %d POSITIVE_PREFIX anchors, N_w %s..%s; "
              "NO EXT3 (r329 record uncommitted, disclosed)"
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
    section("S2  EXACT DECOMPOSITION + ORBIT-LEDGER WARDS")
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
            led = orbit_ledger(pos_all, val_all, blk_all,
                               src_all, m)
            led327 = GMC.group_mass_ledger(pos_all, val_all,
                                           blk_all, src_all, m)
            sbins = QMO.scale_bins(led["gmax"])
            dst = dominant_state(sct["x"], led, sbins)
            orb = companion_orbit(led, sbins, dst["sb"],
                                  dst["nw"], dst["sg"],
                                  dst["ilo"], dst["ihi"])
            nO = int(len(orb))
            memb = np.bincount(orb) if nO else np.zeros(0, int)
            ovl = int(np.max(memb)) if nO else 0
            if nO:
                oab = led["gabs"][orb]
                rmin = float(np.min(oab)) / max(dst["hga"],
                                                1e-300)
                cband = float(np.max(oab)) \
                    / max(float(np.min(oab)), 1e-300)
                S_O = float(np.sum(oab))
            else:
                rmin = 0.0
                cband = 0.0
                S_O = 0.0
            L1a = float(np.sum(led["gabs"]))
            Lb = float(np.sum(np.abs(sct["x"])))
            kap = L1a / max(Lb, 1e-300)
            if nO and rmin > 0.0:
                Qb = dst["ngj"] * kap / (nO * rmin)
            else:
                Qb = INF_SENT
            # one-sided boundary census (same key, edge side)
            if not dst["inner"] and dst["gi"] >= 0:
                gw = np.round(led["gwin"]).astype(int)
                if dst["ps"] < dst["ilo"]:
                    side = (led["gpos"] < dst["ilo"])
                else:
                    side = (led["gpos"] > dst["ihi"])
                sel_s = ((sbins == dst["sb"]) & (gw == dst["nw"])
                         & (np.sign(led["G1"]) == dst["sg"])
                         & side & (led["gabs"] > 0.0))
                nO_side = int(np.sum(sel_s))
            else:
                nO_side = 0
            nband = int(len(set(int(s) for s in sbins[
                led["gabs"] > 0.0]))) if led["ng"] else 0
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
            led = dict(G1=np.zeros(0), gabs=np.zeros(0),
                       gmax=np.zeros(0), gwin=np.zeros(0),
                       mult=np.zeros(0, int), ng=0,
                       gblk=np.zeros(0, int), gpos=np.zeros(0),
                       ptr=np.zeros(1, int), vmaxw=0.0,
                       pmin=0.0, pmax=0.0)
            led327 = None
            sbins = np.zeros(0, int)
            dst = dominant_state(np.zeros(0), led, sbins)
            orb = np.zeros(0, int)
            nO = 0
            ovl = 0
            rmin = 0.0
            cband = 0.0
            S_O = 0.0
            L1a = 0.0
            kap = 0.0
            Qb = INF_SENT
            nO_side = 0
            nband = 0
        return dict(alt_ok=alt_ok, R=R, P=P, m=m, Pd=Pd, cm=cm,
                    degenerate=degenerate, mism=mism, x_dev=x_dev,
                    cube=cube, rec3=rec3, tel_dev=tel_dev,
                    bnd_dev=bnd_dev, C_bnd=C_bnd,
                    mx_mult=mx_mult, gen=gen, sct=sct, ft=ft,
                    trs=trs, rho2=rho2, A1=A1, mqs=mqs,
                    led=led, led327=led327, sbins=sbins, dst=dst,
                    orb=orb, nO=nO, ovl=ovl, rmin=rmin,
                    cband=cband, S_O=S_O, L1a=L1a, kap=kap,
                    Qb=Qb, nO_side=nO_side, nband=nband,
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
    gpos_ok = True
    for rc in live:
        ev = rc["ev"]
        gen = ev["gen"]
        led = ev["led"]
        l327 = ev["led327"]
        if gen["ng"] != led["ng"] or l327["ng"] != led["ng"]:
            led_dev = max(led_dev, 1.0)
            continue
        if gen["ng"]:
            sc = max(float(np.max(np.abs(gen["G1"]))), 1e-300)
            led_dev = max(
                led_dev,
                float(np.max(np.abs(led["G1"] - gen["G1"]))) / sc,
                float(np.max(np.abs(led["mult"] - gen["mult"]))),
                float(np.max(np.abs(led["gblk"] - gen["gblk"]))),
                float(np.max(np.abs(led["gabs"]
                                    - l327["gabs"]))) / sc,
                float(np.max(np.abs(led["gmax"]
                                    - l327["gmax"]))) / sc)
            for j in range(ev["m"]):
                a, b = int(led["ptr"][j]), int(led["ptr"][j + 1])
                if b - a > 1:
                    gp = led["gpos"][a:b]
                    if np.any(gp[1:] < gp[:-1]):
                        gpos_ok = False
    check("G22-genealogy-ledger-identity",
          x_w <= ATOM_BAR and mism_tot == 0 and led_dev <= SA_BAR
          and gpos_ok,
          "the r314 fold genealogy covers every block value on %d "
          "live worlds (group-sum dev %.1e, bar %.0e); run "
          "assignment == breakpoint search (%d mismatches); the "
          "module-own orbit ledger segments IDENTICALLY to the "
          "genealogy AND to the r327 GMC ledger (worst dev %.1e, "
          "bar %.0e); gpos position-sorted within every block "
          "(%s)%s"
          % (len(live), x_w, ATOM_BAR, mism_tot, led_dev, SA_BAR,
             "OK" if gpos_ok else "BROKEN",
             "; DEGENERATE guard fired (pre-declared): "
             + ", ".join(deg_note) if deg_note else ""))

    # ---------------- S3: Leg 0 anchors (slim + r316/r327 record)
    section("S3  LEG 0 -- ANCHOR REGRESSION (slim + the r327 "
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
          "sealed r321/r324/r327 probes"
          % (len(live), rec3_w, REC3_BAR, tel_w, TEL_BAR, bnd_w,
             BND_BAR))
    if smoke:
        ev9s = recs[0]["ev"]
        ds9 = ev9s["dst"]
        info("SMOKE: w9 m %d G %.3f ng* %d hgn %.4f |O| %d rmin "
             "%.3f cband %.3f kappa %.3f Qb %.4f case %s s* %d "
             "par (%d,%+.0f)"
             % (ev9s["m"], ev9s["m"] * ev9s["trs"]["qmax"],
                ds9["ngj"], ds9["hgn"], ev9s["nO"], ev9s["rmin"],
                ev9s["cband"], ev9s["kap"], ev9s["Qb"],
                "I" if ds9["inner"] else "B", ds9["sb"],
                ds9["nw"], ds9["sg"]))
        check("G31-r306-bound-live", True, "SMOKE: skipped")
        check("G32-r316-anchors", True, "SMOKE: skipped")
        check("G33-r327-anchors", True, "SMOKE: skipped")
        srt = []
        n333 = 0
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
        n333 = len(srt)
        rho_all = [rc["ev"]["rho2"] for rc in srt]
        m_all = [rc["ev"]["m"] for rc in srt]
        rho_kz = {rc["kz"]: rc["ev"]["rho2"] for rc in srt}
        sm_i, ca_i, te_i = TRB.split_midladder(n333)
        C_small = max(rho_all[i] for i in sm_i)
        j_cs = max(sm_i, key=lambda i: rho_all[i])
        check("G32-r316-anchors",
              n333 == N333_REF
              and all(abs(rho_kz.get(kz, -1.0) - R316_RHO[kz])
                      <= R316_RHO_TOL for kz in R316_RHO)
              and abs(C_small - R316_CSMALL) <= R316_CSMALL_TOL
              and srt[j_cs]["kz"] == R316_CSMALL_KZ,
              "r316 anchors reproduced: class ladder n = %d (rec "
              "%d); rho kz53/kz67/kz55/kz83 = %.4f/%.4f/%.4f/"
              "%.4f (rec tol %.3f); C_small %.4f @ kz%d"
              % (n333, N333_REF, rho_kz.get(53, -1.0),
                 rho_kz.get(67, -1.0), rho_kz.get(55, -1.0),
                 rho_kz.get(83, -1.0), R316_RHO_TOL, C_small,
                 srt[j_cs]["kz"]))
        named_rank = {}
        for kz in NAMED_KZ:
            for i in range(n333):
                if srt[i]["kz"] == kz:
                    named_rank[kz] = i
        # r327 anchors: group count + anatomy re-derived
        ng_col = [rc["ev"]["dst"]["ngj"] for rc in srt]
        ngl_col = [ng_col[i] / math.log(float(m_all[i]))
                   for i in range(n333)]
        C_NG = max(ngl_col[i] for i in ca_i)
        viol_ng = [i for i in te_i if ngl_col[i] > C_NG]
        named_ng = sum(1 for kz in NAMED_KZ
                       if ngl_col[named_rank[kz]] <= C_NG)
        nw_col = [rc["ev"]["dst"]["nw"] for rc in srt]
        nw_hist = tuple(sum(1 for w in nw_col if w == k)
                        for k in (0, 1, 2))
        bsh53 = srt[named_rank[53]]["ev"]["dst"]["bshare"]
        gap_col = []
        al_col = []
        th_col = []
        for rc in srt:
            ev = rc["ev"]
            ds = ev["dst"]
            a, b = int(ev["led"]["ptr"][ds["j"]]), \
                int(ev["led"]["ptr"][ds["j"] + 1])
            ga = ev["led"]["gabs"][a:b]
            gv = np.abs(ev["led"]["G1"][a:b])
            i1 = int(np.argmax(ga))
            hga2 = float(np.max(np.delete(ga, i1))) \
                if b - a > 1 else 0.0
            gap_col.append(hga2 / max(float(ga[i1]), 1e-300))
            al_col.append(float(gv[i1])
                          / max(float(ga[i1]), 1e-300))
            th_col.append(min(2, (3 * i1) // (b - a)))
        th_hist = tuple(sum(1 for t in th_col if t == k)
                        for k in (0, 1, 2))
        check("G33-r327-anchors",
              abs(C_NG - R327_CNG) <= R327_CNG_TOL
              and len(viol_ng) == R327_VNG
              and named_ng == len(NAMED_KZ)
              and nw_hist == R327_NWIN_HIST
              and abs(bsh53 - R327_BSHARE53) <= R327_BSHARE_TOL
              and abs(float(np.median(gap_col)) - R327_GAP_MED)
              <= R327_GAP_TOL
              and abs(float(np.median(al_col)) - R327_ALIGN_MED)
              <= R327_ALIGN_TOL
              and th_hist == R327_THIRDS,
              "the r327 RECORD reproduced bit-near: C_NG %.4f "
              "(rec %.4f) viol %d/%d (rec %d) named %d/4; "
              "window-atom histogram %s == (0, 65, 0) EXACT "
              "(every dominant group IS one beta/omega pair); "
              "kz53 bshare %.3f (rec 0.888 tol %.2f); gap med "
              "%.3f (rec 0.807); align med %.3f (rec 1.000); "
              "thirds %s == (21, 29, 15) EXACT"
              % (C_NG, R327_CNG, len(viol_ng), len(te_i),
                 R327_VNG, named_ng, str(nw_hist), bsh53,
                 R327_BSHARE_TOL, float(np.median(gap_col)),
                 float(np.median(al_col)), str(th_hist)))

    # ---------------- S4: Leg A -- seal + purity + toys + wards
    section("S4  LEG A -- SEAL + PURITY + TOYS + LIVE WARDS + "
            "SOURCE-PURE TABLE")
    pure_lits = []
    for fn in ("orbit_ledger", "dominant_state", "companion_orbit",
               "packing_tree", "fr_orbit_toy", "fr_band_toy"):
        pure_lits += literal_audit(fn)
    e1_hits = scope_audit("mutant_orbit_posthoc", QMAX_FORBIDDEN)
    e2_hits = scope_audit("mutant_band_posthoc", BOUND_FORBIDDEN)
    check("G40-purity-audits",
          (not sc_own) and (not pure_lits)
          and len(e1_hits) >= 1 and len(e2_hits) >= 1,
          "SOURCE PURITY: the orbit builders clean vs the "
          "forbidden sets (%d id hits) and vs the sealed r314..."
          "r327 record-literal set (%d literal hits); consumed "
          "inputs: group scale bins / parities / positions / the "
          "inner interval -- M_3, rho_2 and the q_max RECORD are "
          "TARGET-SIDE, computed outside the builders "
          "(disclosed; kappa likewise); e1 orbit-posthoc FLAGGED "
          "(%s); e2 band-posthoc FLAGGED (%s)"
          % (len(sc_own), len(pure_lits),
             e1_hits[0] if e1_hits else "MISS",
             e2_hits[0] if e2_hits else "MISS"))
    fr_dev, fr_slack, fr_orb_ok, fr_mut_ok = fr_orbit_toy()
    fr_bdev = fr_band_toy()
    ovl_mut = max(mutant_overlap_triple())
    ovl_break = ovl_mut - OVERLAP_CAP
    tr_br = (packing_tree(True, True, True, True, True),
             packing_tree(False, True, True, True, True),
             packing_tree(False, False, True, True, True),
             packing_tree(False, False, False, True, True),
             packing_tree(False, False, False, False, True),
             packing_tree(False, False, False, False, False))
    ok_tr = tr_br == ("TARGET_LEAK", "WEIGHT_COMPARABILITY_FAIL",
                      "COMPANION_PACKING_POLYLOG",
                      "BOUNDARY_FINITE_HEAD",
                      "COMPANION_PACKING_SUBCRITICAL",
                      "ORBIT_TOO_SHORT")
    check("G41-toy-exactness",
          fr_dev == 0 and fr_orb_ok and fr_mut_ok
          and fr_bdev == 0 and ovl_break == 1 and ok_tr,
          "the Fractions orbit toy EXACT (worst dev %s): O = "
          "{g*, companion}, rmin 15/16, cband 16/15, q_max "
          "80/251 <= Q_b 8/15, chain slack %s EXACT; the real "
          "builders reproduce the toy orbit (keys, inner case, "
          "set) and EXCLUDE the wrong-parity and out-of-band "
          "groups; the similarity mutant picks the wrong-parity "
          "group (set mismatch CAUGHT); band-extremes toy EXACT "
          "(worst %s; ratio 33/128 > 1/4 margin 1/128 -- sharp "
          "near 1/4); overlap triple-mutant break %d EXACT "
          "(REFUSED); packing_tree all six branches EXACT %s"
          % (str(fr_dev), str(fr_slack), str(fr_bdev),
             ovl_break, str(tr_br)))
    # live wards
    chain_w = 0.0
    xw_cube = 0.0
    interp_w = 0.0
    part_w = 0.0
    band_ok = True
    band_worst_r = 1.0
    band_worst_c = 1.0
    ovl_worst = 0
    qb_w = 0.0
    a1_w = 0.0
    kap_min = float("inf")
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
        A1led = np.bincount(led["gblk"], weights=led["gabs"],
                            minlength=mloc)
        part_w = max(part_w,
                     float(np.max(np.abs(A1led - ev["A1"])))
                     / max(float(np.max(ev["A1"])), 1e-300))
        ds = ev["dst"]
        # exact chain q_max <= A1*/L <= ng* hga/L <= Q_b
        a1_w = max(a1_w,
                   max(0.0, mloc * qmx - mloc * ds["a1j"] / Lx)
                   / max(mloc * ds["a1j"] / Lx, 1e-300),
                   max(0.0, ds["a1j"] - ds["ngj"] * ds["hga"])
                   / max(ds["ngj"] * ds["hga"], 1e-300))
        if ev["nO"]:
            band_worst_r = min(band_worst_r, ev["rmin"])
            band_worst_c = max(band_worst_c, ev["cband"])
            if not (ev["rmin"] > RBAND_MIN * (1.0 - BAND_TOL)
                    and ev["cband"] < CBAND_MAX
                    * (1.0 + BAND_TOL)):
                band_ok = False
            ovl_worst = max(ovl_worst, ev["ovl"])
            qb_w = max(qb_w, max(0.0, qmx - ev["Qb"])
                       / max(ev["Qb"], 1e-300))
            kap_min = min(kap_min, ev["kap"])
        mult_all_ok = mult_all_ok \
            and QMO.mult_ward(ev["gen"]["mult"])[1]
    check("G42-live-wards",
          chain_w <= CHAIN_BAR and xw_cube <= CHAIN_BAR
          and interp_w <= CHAIN_BAR and part_w <= SA_BAR
          and band_ok and ovl_worst <= OVERLAP_CAP
          and qb_w <= CHAIN_BAR and a1_w <= CHAIN_BAR
          and kap_min >= 1.0 - CHAIN_BAR and mult_all_ok,
          "the r316 chain live on %d live worlds (worst %.1e); "
          "NORM x cube == rho_2 (%.1e); S0 interpolation (worst "
          "%.1e); GROUP PARTITION sum_g gabs == A1_j (worst "
          "%.1e, bar %.0e); THE BAND THEOREM live: rmin worst "
          "%.4f > 1/4 AND cband worst %.4f < 4 on every orbit "
          "(T2 at b = 0, exact algebra); THE OVERLAP WARD: max "
          "membership %d <= %d (T3, partition-exact -- the "
          "theorem's factor-2 reserve unused); THE COMPOSED "
          "CHAIN q_max <= A1*/L <= ng* hga/L (worst %.1e) AND "
          "q_max <= Q_b = ng* kappa/(|O| rmin) (worst %.1e); "
          "kappa min %.4f >= 1; fold multiplicity <= %d "
          "admitted on ALL live worlds"
          % (len(live), chain_w, xw_cube, interp_w, part_w,
             SA_BAR, band_worst_r, band_worst_c, ovl_worst,
             OVERLAP_CAP, a1_w, qb_w, kap_min, MULT_CAP))
    if smoke:
        check("G43-coordinate-table", True, "SMOKE: skipped")
    else:
        qmax_col = [rc["ev"]["trs"]["qmax"] for rc in srt]
        G_col = [m_all[i] * qmax_col[i] for i in range(n333)]
        hgn_col = [rc["ev"]["dst"]["hgn"] for rc in srt]
        nO_col = [rc["ev"]["nO"] for rc in srt]
        rmin_col = [rc["ev"]["rmin"] for rc in srt]
        cb_col = [rc["ev"]["cband"] for rc in srt]
        kap_col = [rc["ev"]["kap"] for rc in srt]
        Qb_col = [rc["ev"]["Qb"] for rc in srt]
        inner_col = [rc["ev"]["dst"]["inner"] for rc in srt]
        sb_col = [rc["ev"]["dst"]["sb"] for rc in srt]
        d_col = [rc["ev"]["dst"]["d"] for rc in srt]
        B1_col = [min(m_all[i] * Qb_col[i]
                      / (math.log(float(m_all[i])) ** 2),
                      INF_SENT) for i in range(n333)]
        info("sealed SOURCE-PURE table (printed BEFORE any "
             "certification table): rank kz N m G ng* hgn |O| "
             "rmin cband kappa Qb B1 case s* nw d*")
        for i, rc in enumerate(srt):
            ds = rc["ev"]["dst"]
            info("%2d kz%-3d N %4d m %3d G %6.3f ng %2d hgn "
                 "%6.3f |O| %3d rmin %.3f cb %.3f kap %.3f Qb "
                 "%8.4f B1 %8.4f %s s%d w%d d %.3f"
                 % (i, rc["kz"], rc["N"], m_all[i], G_col[i],
                    ng_col[i], hgn_col[i], nO_col[i],
                    rmin_col[i], cb_col[i], kap_col[i],
                    min(Qb_col[i], 9999.0), min(B1_col[i],
                                                9999.0),
                    "I" if inner_col[i] else "B", sb_col[i],
                    ds["nw"], d_col[i]))
        check("G43-coordinate-table", True,
              "|O| range %d/%.0f/%d min/med/max; rmin med %.3f; "
              "cband med %.3f; kappa med %.3f max %.3f; Qb med "
              "%.3f max %.2f (max at kz%d); hgn med %.3f max "
              "%.2f; inner %d / boundary %d; s* histogram %s"
              % (min(nO_col), float(np.median(nO_col)),
                 max(nO_col), float(np.median(rmin_col)),
                 float(np.median(cb_col)),
                 float(np.median(kap_col)), max(kap_col),
                 float(np.median(Qb_col)), max(Qb_col),
                 srt[int(np.argmax(Qb_col))]["kz"],
                 float(np.median(hgn_col)), max(hgn_col),
                 sum(1 for v in inner_col if v),
                 sum(1 for v in inner_col if not v),
                 str(sorted(set(sb_col)))))

    # ---------------- S5: Leg B -- orbit census + worlds
    section("S5  LEG B -- ORBIT CENSUS + NAMED ANATOMY + WORLDS")
    if smoke:
        check("G50-orbit-census", True, "SMOKE: skipped")
        check("G51-named-anatomy", True, "SMOKE: skipped")
    else:
        bnd_i = [i for i in range(n333) if not inner_col[i]]
        info("boundary-case rungs (%d): %s"
             % (len(bnd_i),
                str([(srt[i]["kz"], m_all[i],
                      srt[i]["ev"]["nO_side"]) for i in bnd_i])))
        check("G50-orbit-census", True,
              "ORBIT CENSUS: |O| med %.0f; inner %d/%d rungs; "
              "boundary %d rungs %s with one-sided same-key "
              "companion counts %s (the one-sided calculation "
              "as measurement); edge distance d* med %.3f min "
              "%.3f; |O|/m med %.3f"
              % (float(np.median(nO_col)),
                 sum(1 for v in inner_col if v), n333,
                 len(bnd_i), str([srt[i]["kz"] for i in bnd_i]),
                 str([srt[i]["ev"]["nO_side"] for i in bnd_i]),
                 float(np.median(d_col)), min(d_col),
                 float(np.median([nO_col[i] / float(m_all[i])
                                  for i in range(n333)]))))
        nO_med = float(np.median(nO_col))
        hgn_med = float(np.median(hgn_col))
        mech = {}
        for kz in NAMED_KZ:
            i = named_rank[kz]
            small = nO_col[i] < 0.5 * nO_med
            heavy = hgn_col[i] > 2.0 * hgn_med
            mech[kz] = ("SMALL_ORBIT+HEAVY_BAND" if small and
                        heavy else "SMALL_ORBIT" if small
                        else "HEAVY_BAND" if heavy else "COVERED")
            info("named kz%-3d: |O| %d (med %.0f) rmin %.3f "
                 "cband %.3f kappa %.3f hgn %.2f (med %.2f) Qb "
                 "%.3f B1 %.3f case %s s* %d -> %s"
                 % (kz, nO_col[i], nO_med, rmin_col[i],
                    cb_col[i], kap_col[i], hgn_col[i], hgn_med,
                    min(Qb_col[i], 9999.0),
                    min(B1_col[i], 9999.0),
                    "I" if inner_col[i] else "B", sb_col[i],
                    mech[kz]))
        check("G51-named-anatomy", True,
              "THE SPIKE HARDNESS TEST (measurement, sealed "
              "letters SMALL_ORBIT / HEAVY_BAND / COVERED at "
              "med-relative bars 0.5x / 2x): %s -- which "
              "mechanism blocks the orbit bound at the "
              "near-critical windows" % str(mech))
    # world census (both modes; uses w9 or mains + controls)
    ev9w = (recs[0] if smoke else mrecs[0])["ev"]
    ev13 = None if smoke else mrecs[1]["ev"]
    wtab = [("w9", ev9w)] + ([("w13(twin)", ev13)]
                             if ev13 is not None else [])
    for c in ("EPST", "SCR"):
        if not crecs[c]["ev"]["degenerate"]:
            wtab.append((c, crecs[c]["ev"]))
    info("world table: world m |O| rmin cband kappa Qb case "
         "nbands(occupied dyadic gmax bins)")
    for w, ev in wtab:
        ds = ev["dst"]
        info("  %-10s m %3d |O| %3d rmin %.3f cb %.3f kap %.3f "
             "Qb %8.4f %s nbands %d"
             % (w, ev["m"], ev["nO"], ev["rmin"], ev["cband"],
                ev["kap"], min(ev["Qb"], 9999.0),
                "I" if ds["inner"] else "B", ev["nband"]))
    scr_ev = crecs["SCR"]["ev"]
    check("G52-world-census", len(wtab) >= 2,
          "Q4 WORLD CHECK (census, NO claim): twin w13 runs the "
          "IDENTICAL sealed construction (all exact wards above "
          "include it); EPSTEIN band structure: %d occupied "
          "bins vs w9 %d (|O| %d vs %d); SCRAMBLE orbit: |O| %d "
          "rmin %.3f vs w9 |O| %d rmin %.3f -- the orbit decay "
          "question answered by these numbers"
          % (crecs["EPST"]["ev"]["nband"], ev9w["nband"],
             crecs["EPST"]["ev"]["nO"], ev9w["nO"],
             scr_ev["nO"], scr_ev["rmin"], ev9w["nO"],
             ev9w["rmin"]))

    # ---------------- S6: Leg C -- certification + exponents
    section("S6  LEG C -- T1/T2/COMPOSED CERTIFICATION + "
            "EXPONENTS")
    if smoke:
        check("G60-T1-orbit-size", True, "SMOKE: skipped")
        check("G61-T2-band", True, "SMOKE: skipped")
        check("G62-composed-qmax", True, "SMOKE: skipped")
        check("G63-growth-exponents", True, "SMOKE: skipped")
    else:
        t1 = {}
        for a in A_FAM:
            col = [nO_col[i] * (math.log(float(m_all[i])) ** a)
                   / float(m_all[i]) for i in range(n333)]
            c0 = min(col[i] for i in ca_i)
            viol = [i for i in te_i if col[i] < c0]
            named = sum(1 for kz in NAMED_KZ
                        if col[named_rank[kz]] >= c0)
            t1[a] = (c0, viol, named, col)
        aT1 = None
        for a in A_FAM:
            if not t1[a][1] and t1[a][2] == len(NAMED_KZ):
                aT1 = a
                break
        check("G60-T1-orbit-size", True,
              "T1 |O| >= c_0 m/(log m)^a (min-cal freeze): "
              + "; ".join("a=%d c_0 %.4f viol %d/%d named %d/4"
                          % (a, t1[a][0], len(t1[a][1]),
                             len(te_i), t1[a][2])
                          for a in A_FAM)
              + "; worst violators %s; minimal certifying a = %s"
              % (str([(srt[i]["kz"], round(t1[A_FAM[-1]][3][i],
                                           4))
                      for i in t1[A_FAM[-1]][1][:6]]),
                 str(aT1)))
        check("G61-T2-band", band_ok,
              "T2 THE BAND THEOREM (b = 0, c_1 = 1/4, EXACT "
              "inside one dyadic gmax bin): rmin worst %.4f > "
              "0.25 and cband worst %.4f < 4 on every live "
              "orbit -- certified at theorem grade (gated in "
              "G42; the Fractions extremes toy shows sharpness "
              "near 1/4)" % (band_worst_r, band_worst_c))
        comp = {}
        for a in A_FAM:
            col = [min(m_all[i] * Qb_col[i]
                       / (math.log(float(m_all[i]))
                          ** (1 + a)), INF_SENT)
                   for i in range(n333)]
            CQ = max(col[i] for i in ca_i)
            viol = [i for i in te_i if col[i] > CQ]
            named = sum(1 for kz in NAMED_KZ
                        if col[named_rank[kz]] <= CQ)
            comp[a] = (CQ, viol, named, col)
        aC = None
        for a in A_FAM:
            if (not comp[a][1] and comp[a][2] == len(NAMED_KZ)
                    and comp[a][0] < CERT_GUARD):
                aC = a
                break
        check("G62-composed-qmax", True,
              "COMPOSED q_max BOUND B_a = m Q_b/(log m)^{1+a} "
              "<= C_Q(a) (max-cal freeze): "
              + "; ".join("a=%d C_Q %.4f viol %d/%d named %d/4"
                          % (a, min(comp[a][0], 9999.0),
                             len(comp[a][1]), len(te_i),
                             comp[a][2]) for a in A_FAM)
              + "; worst violators %s; minimal certifying a = %s"
              % (str([(srt[i]["kz"],
                       round(min(comp[A_FAM[-1]][3][i],
                                 9999.0), 3))
                      for i in sorted(
                          comp[A_FAM[-1]][1],
                          key=lambda i:
                          -comp[A_FAM[-1]][3][i])[:6]]),
                 str(aC)))
        msT = [m_all[i] for i in te_i]
        e_hgn = L2D.halves_slope(msT, [max(hgn_col[i], 1e-300)
                                       for i in te_i])
        e_B1 = L2D.halves_slope(msT, [max(min(B1_col[i],
                                              INF_SENT), 1e-300)
                                      for i in te_i])
        h = len(te_i) // 2
        te_a = te_i[:h]
        te_b = te_i[h:]

        def ehgn_on(idx):
            return L2D.halves_slope([m_all[i] for i in idx],
                                    [max(hgn_col[i], 1e-300)
                                     for i in idx])

        e_a = ehgn_on(te_a)
        e_b = ehgn_on(te_b)
        decided = ((e_a < DELTA_CRIT) == (e_b < DELTA_CRIT)
                   and (e_a < DELTA_CRIT)
                   == (e_hgn < DELTA_CRIT))
        check("G63-growth-exponents", True,
              "GROWTH EXPONENTS (r272 dyadic halves-slope vs m "
              "over the %d test rungs, fit-free): delta = "
              "e(hgn) = %+.3f vs DELTA_CRIT %.3f (the reviewer "
              "subcritical budget; n_g = O(log m) is the r327 "
              "banked certificate); e(B_1) = %+.3f (census); "
              "stability halves %+.3f / %+.3f -> %s, %s"
              % (len(te_i), e_hgn, DELTA_CRIT, e_B1, e_a, e_b,
                 "DECIDED" if decided else "UNDECIDED",
                 ("SUBCRITICAL-SIDE" if e_hgn < DELTA_CRIT
                  else "SUPERCRITICAL-SIDE") if decided
                 else "open"))

    # ---------------- S7: Leg D -- adjudication + composition
    section("S7  LEG D -- SEALED ADJUDICATION + COMPOSITION")
    if smoke:
        check("G70-adjudication", True, "SMOKE: skipped")
        check("G71-composition", True, "SMOKE: skipped")
        verdict_main = "SMOKE_NO_ADJUDICATION"
    else:
        leak = bool(sc_own) or bool(pure_lits)
        wfail = (not band_ok) or ovl_worst > OVERLAP_CAP
        polylog = (aT1 is not None) and (aC is not None)
        aG = A_FAM[-1]
        violG = set(t1[aG][1]) | set(comp[aG][1])
        inner_te = [i for i in te_i if inner_col[i]]
        inner_ok = all(i not in violG for i in inner_te)
        named_inner_ok = all(
            (not inner_col[named_rank[kz]])
            or (t1[aG][3][named_rank[kz]] >= t1[aG][0]
                and comp[aG][3][named_rank[kz]] <= comp[aG][0])
            for kz in NAMED_KZ)
        bhead = ((not polylog) and bool(violG)
                 and all(not inner_col[i] for i in violG)
                 and inner_ok and named_inner_ok)
        subcrit = decided and e_hgn < DELTA_CRIT
        vkey = packing_tree(leak, wfail, polylog, bhead, subcrit)
        rest = []
        if aT1 is None:
            rest.append("T1 fails at all a in %s (worst "
                        "violators incl. %s)"
                        % (str(A_FAM),
                           str([srt[i]["kz"]
                                for i in t1[aG][1][:4]])))
        if aC is None:
            rest.append("composed bound fails at all a (worst "
                        "%s)" % str([srt[i]["kz"]
                                     for i in comp[aG][1][:4]]))
        if not decided:
            rest.append("exponent halves straddle %+.3f/%+.3f"
                        % (e_a, e_b))
        det_v = {
            "TARGET_LEAK": "purity/scope audit hit on an orbit "
                           "builder",
            "WEIGHT_COMPARABILITY_FAIL":
                "the exact band/overlap ward broke (rmin %.4f, "
                "cband %.4f, ovl %d) -- the martingale second "
                "route is next (NAMED ONLY, not executed)"
                % (band_worst_r, band_worst_c, ovl_worst),
            "COMPANION_PACKING_POLYLOG":
                "a = %s, b = 0: T1 c_0 %.4f (0 viol, named 4/4) "
                "+ T2 band exact + composed C_Q %.4f (0 viol, "
                "named 4/4)"
                % (str(aC), t1[aT1][0] if aT1 is not None
                   else 0.0, comp[aC][0] if aC is not None
                   else 0.0),
            "BOUNDARY_FINITE_HEAD":
                "every violator at a = %d is boundary-case %s; "
                "the inner subset certifies -- the finite head "
                "is the boundary family"
                % (aG, str([srt[i]["kz"] for i in violG])),
            "COMPANION_PACKING_SUBCRITICAL":
                "delta = e(hgn) = %+.3f < %.3f DECIDED (halves "
                "%+.3f/%+.3f) with n_g = O(log m) certified "
                "(r327 C_NG)" % (e_hgn, DELTA_CRIT, e_a, e_b),
            "ORBIT_TOO_SHORT":
                "rest: %s; delta %+.3f %s %.3f (halves %+.3f/"
                "%+.3f); named mechanisms %s"
                % ("; ".join(rest) if rest else "none", e_hgn,
                   "<" if e_hgn < DELTA_CRIT else ">=",
                   DELTA_CRIT, e_a, e_b, str(mech))}
        verdict_main = "%s(%s)" % (vkey, det_v[vkey])
        check("G70-adjudication", True,
              "exactly one sealed letter fired: %s"
              % verdict_main)
        # composition (printed ALWAYS, honestly typed)
        if vkey == "COMPANION_PACKING_POLYLOG":
            Atot = 1 + aC
            C_full = comp[aC][0]
            m_star_l10 = None
            t = math.log(73.0)
            while t < 1e7:
                if t * DELTA_CRIT >= math.log(C_full) \
                        + Atot * math.log(t):
                    m_star_l10 = t / math.log(10.0)
                    break
                t *= 1.02
            ms_txt = ("10^%.1f" % m_star_l10) \
                if m_star_l10 is not None else "NONE"
            info("COMPOSITION (T1 + T2 + T3 pointwise-"
                 "certified, mid-ladder): q_max <= %.4f x "
                 "(log m)^%d/m => M_3 <= q_max M_2 <= q_max^2 "
                 "(S0 exact) => N_2 >= 1/q_max >= m/(%.4f "
                 "(log m)^%d) => N_2 >= m^%.3f for all m >= "
                 "m_0* = %s (m^{%.3f} >= C (log m)^%d) => the "
                 "r297 target chain; all measured m <= %d "
                 "closed by the finite tables; the ladder-to-"
                 "m_0* step stays the disclosed extrapolation "
                 "hypothesis."
                 % (C_full, Atot, C_full, Atot, N2_EXP_NEED,
                    ms_txt, DELTA_CRIT, Atot, max(m_all)))
            comp_ok = True
            comp_txt = "polylog: q_max <= %.4f (log m)^%d/m, " \
                "m_0* %s" % (C_full, Atot, ms_txt)
        elif vkey == "COMPANION_PACKING_SUBCRITICAL":
            info("COMPOSITION (subcritical, typed MEASURED): "
                 "m q_max <= ng hgn <= C_NG log m x C m^{%+.3f} "
                 "(C_NG %.4f certified r327-anchor-gated; hgn "
                 "envelope %.3f) => N_2 >= m^{%.3f}/(C_NG C "
                 "log m) >= m^%.3f asymptotically (delta < "
                 "%.3f); the ladder-to-cofinal step stays the "
                 "disclosed extrapolation hypothesis."
                 % (e_hgn, C_NG, max(hgn_col), 1.0 - e_hgn,
                    N2_EXP_NEED, DELTA_CRIT))
            comp_ok = True
            comp_txt = "subcritical: delta %+.3f, hgn env " \
                "%.3f" % (e_hgn, max(hgn_col))
        else:
            info("COMPOSITION: no certifying letter -- the r324 "
                 "MEASURED composition stands unchanged (sum "
                 "q^3 <= 8.941 (log m) m^{+0.172}/m^2, N_2 >= "
                 "m^0.888 for m >= 10^59.6); measured orbit-"
                 "route envelopes: max B_1 %.3f, max B_2 %.3f, "
                 "e(hgn) %+.3f, e(B_1) %+.3f."
                 % (min(max(comp[1][3]), 9999.0),
                    min(max(comp[2][3]), 9999.0), e_hgn, e_B1))
            comp_ok = True
            comp_txt = "r324 restated; orbit envelopes B1 " \
                "%.3f / B2 %.3f" \
                % (min(max(comp[1][3]), 9999.0),
                   min(max(comp[2][3]), 9999.0))
        check("G71-composition", comp_ok,
              "composition printed with explicit constants "
              "(%s); the chain to terminal_positive_main is "
              "typed: band/overlap/chain algebra exact, every "
              "constant MEASURED on the finite ladder, the "
              "ladder-to-m_0* step an extrapolation hypothesis "
              "-- NO cofinal claim" % comp_txt)

    # ---------------- S8: Leg E -- must-fails
    section("S8  LEG E -- WARDS / MUST-FAILS")
    ev9m = (recs[0] if smoke else mrecs[0])["ev"]
    rb9 = mutant_orbit_posthoc(dict(trs=ev9m["trs"],
                                    m=ev9m["m"]))
    check("G80-e1-orbit-posthoc",
          len(e1_hits) >= 1 and (not sc_own) and rb9 >= 0.0,
          "e1 AST-CAUGHT: the 'orbit coordinate' consuming the "
          "q_max RECORD is FLAGGED (%s) while the four "
          "module-own orbit builders are clean (%d hits) -- an "
          "orbit constructed after q_max sight is structurally "
          "refused (the mutant value %.3f is computed only to "
          "prove the mutant runs)"
          % (e1_hits[0] if e1_hits else "MISS", len(sc_own),
             rb9))
    toy_sb = (0, 2, 1)
    toy_rho = (0.1, 0.9, 0.1)
    bw_mut = mutant_band_posthoc(toy_sb, toy_rho, 0.5)
    check("G81-e2-band-posthoc",
          len(e2_hits) >= 1 and bw_mut == 2 and bw_mut != 0,
          "e2 CAUGHT twice: the after-sight band re-pick "
          "consumes the evaluated bound column -- AST-FLAGGED "
          "(%s) -- and on the toy returns width %d != the "
          "canonical same-bin rule's 0 (band boundaries chosen "
          "after sight are structurally refused)"
          % (e2_hits[0] if e2_hits else "MISS", bw_mut))
    check("G82-e3-overlap-break",
          ovl_break == 1 and max(mutant_overlap_triple()) >
          OVERLAP_CAP and ovl_worst <= OVERLAP_CAP,
          "e3 LOUD: the synthetic triple-membership census "
          "(one atom in 3 companions) breaks the overlap ward "
          "by EXACTLY %d (3 > %d, REFUSED) while every live "
          "orbit passes at membership %d -- an overlap break "
          "cannot slip through the partition ward"
          % (ovl_break, OVERLAP_CAP, max(ovl_worst, 1)))
    check("G83-e4-similarity-pick", fr_mut_ok,
          "e4 CAUGHT (exact set mismatch): the value-side "
          "similarity search picks the wrong-parity group on "
          "the sealed toy and differs from the canonical "
          "source orbit (Fractions-warded in G41) -- companion "
          "selection by similarity instead of source position "
          "is structurally refused")

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the canonical companion-orbit construction "
          "from the dominant pair's source data (scale bin + "
          "fold parity + inner interval), the exact band "
          "theorem (T2 at b = 0), the partition-exact overlap "
          "ward (T3), the composed deterministic q_max chain "
          "q_max <= ng kappa/(|O| rmin) with pointwise "
          "certification, the boundary one-sided census and "
          "the spike mechanism letters -- NO new certificate "
          "promoted, NO universal bound claimed beyond the "
          "measured rungs")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = ["R333_ANCHORS(identity %.1e, r306 C2 %.3f viol "
                 "%d/57, r316 n %d rho4 bit-near, r327 C_NG "
                 "%.4f viol %d named %d/4, nwin %s, bshare53 "
                 "%.3f, gap %.3f, align %.3f, thirds %s)"
                 % (rec3_w, C2r, viol2, n333, C_NG,
                    len(viol_ng), named_ng, str(nw_hist), bsh53,
                    float(np.median(gap_col)),
                    float(np.median(al_col)), str(th_hist))]
        parts.append("SEAL(partition %.1e, ledger %.1e, band "
                     "rmin %.4f / cband %.4f, overlap %d, "
                     "chain %.1e, kappa min %.4f, purity "
                     "clean, toys exact)"
                     % (part_w, led_dev, band_worst_r,
                        band_worst_c, ovl_worst, qb_w, kap_min))
        parts.append("ORBIT(|O| med %.0f min %d max %d, inner "
                     "%d/%d, boundary %s, mech %s)"
                     % (float(np.median(nO_col)), min(nO_col),
                        max(nO_col),
                        sum(1 for v in inner_col if v), n333,
                        str([srt[i]["kz"] for i in bnd_i]),
                        str(mech)))
        parts.append("CERT(T1 %s minA %s; T2 b=0 exact; "
                     "composed %s minA %s; delta %+.3f %s)"
                     % ("; ".join("a%d c0 %.3f v%d" %
                                  (a, t1[a][0], len(t1[a][1]))
                                  for a in A_FAM), str(aT1),
                        "; ".join("a%d CQ %.3f v%d" %
                                  (a, min(comp[a][0], 9999.0),
                                   len(comp[a][1]))
                                  for a in A_FAM), str(aC),
                        e_hgn,
                        "DECIDED" if decided else "UNDECIDED"))
        parts.append(verdict_main)
        parts.append("COMPOSITION(%s)" % comp_txt)
        parts.append("MUSTFAIL_LEDGER(e1-e4 + scopes)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the band theorem, the "
          "partition/overlap algebra, the composed chain, the "
          "Fractions toys, the tree logic and the purity "
          "audits (exact / AST-decided); MEASURED: every "
          "census, constant, violation count and exponent (the "
          "finite class ladder + 2 mains + 2 live controls); "
          "OPEN: any bound beyond the measured rungs, the "
          "cofinal law, kappa's behavior beyond the ladder, "
          "kz15 beyond r270; NO RH claim"
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
